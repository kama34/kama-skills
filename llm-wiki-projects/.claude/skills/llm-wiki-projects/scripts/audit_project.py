#!/usr/bin/env python3
"""Audit a project before creating or migrating an LLM Wiki."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".cache",
    ".next",
    ".nuxt",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    "node_modules",
    "vendor",
    "dist",
    "build",
    "target",
    "coverage",
    ".obsidian",
    ".agents",
    ".claude",
    ".codex",
    ".idea",
    ".vscode",
}

CODE_MANIFESTS = {
    "package.json",
    "pyproject.toml",
    "Cargo.toml",
    "go.mod",
    "pom.xml",
    "build.gradle",
    "settings.gradle",
    "composer.json",
    "Gemfile",
    "mix.exs",
    "deno.json",
    "tsconfig.json",
    "Makefile",
    "Dockerfile",
}

CODE_EXTS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".go",
    ".rs",
    ".java",
    ".kt",
    ".c",
    ".cc",
    ".cpp",
    ".h",
    ".hpp",
    ".cs",
    ".rb",
    ".php",
    ".swift",
    ".m",
    ".mm",
    ".scala",
    ".clj",
    ".ex",
    ".exs",
    ".sh",
    ".sql",
}

MARKDOWN_EXTS = {".md", ".markdown"}
SOURCE_EXTS = {
    ".pdf",
    ".doc",
    ".docx",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
    ".csv",
    ".tsv",
    ".txt",
    ".html",
    ".htm",
    ".epub",
}
MEDIA_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".mp3", ".wav", ".mp4", ".mov", ".m4a"}
ZONE_DIRS = {"00-inbox", "10-sources", "20-notes", "30-maps", "40-projects", "90-meta", "assets"}


def is_hidden_or_skipped(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def iter_project_files(root: Path, include_existing_wiki: bool = False):
    for dirpath, dirnames, filenames in os.walk(root):
        current = Path(dirpath)
        rel_parts = current.relative_to(root).parts if current != root else ()
        dirnames[:] = [
            d
            for d in dirnames
            if d not in SKIP_DIRS and (include_existing_wiki or d != "_wiki")
        ]
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        for filename in filenames:
            path = current / filename
            if not include_existing_wiki and "_wiki" in path.relative_to(root).parts:
                continue
            yield path


def read_text_sample(path: Path, limit: int = 200_000) -> str:
    try:
        data = path.read_bytes()[:limit]
    except OSError:
        return ""
    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return ""


def detect_language(root: Path, files: list[Path]) -> tuple[str, str]:
    priority = []
    for name in ("README.md", "Readme.md", "readme.md", "AGENTS.md"):
        candidate = root / name
        if candidate.exists():
            priority.append(candidate)
    priority.extend([p for p in files if p.suffix.lower() in MARKDOWN_EXTS and p not in priority])
    sample = "\n".join(read_text_sample(p, 40_000) for p in priority[:20])
    cyrillic = len(re.findall(r"[А-Яа-яЁё]", sample))
    latin = len(re.findall(r"[A-Za-z]", sample))
    if cyrillic == 0 and latin == 0:
        return "ru", "no text found; defaulting to Russian"
    ratio = cyrillic / max(cyrillic + latin, 1)
    if ratio >= 0.18:
        return "ru", f"cyrillic ratio {ratio:.2f}"
    if cyrillic > 0:
        return "ru", f"mixed language with cyrillic ratio {ratio:.2f}; defaulting to Russian"
    return "en", "latin text with no cyrillic"


def classify_project(root: Path, files: list[Path]) -> tuple[str, list[str]]:
    manifest_hits = sorted(str((root / name).relative_to(root)) for name in CODE_MANIFESTS if (root / name).exists())
    code_count = sum(1 for p in files if p.suffix.lower() in CODE_EXTS)
    markdown_count = sum(1 for p in files if p.suffix.lower() in MARKDOWN_EXTS)
    reasons = []
    if manifest_hits:
        reasons.append("code manifests: " + ", ".join(manifest_hits[:8]))
    if code_count >= 5:
        reasons.append(f"{code_count} code-like files")
    if manifest_hits or code_count >= 5:
        return "code", reasons
    if markdown_count or files:
        return "knowledge", [f"{markdown_count} markdown files", f"{len(files)} total files"]
    return "empty", ["no project files found"]


def audit(root: Path) -> dict[str, Any]:
    root = root.expanduser().resolve()
    files = list(iter_project_files(root))
    all_files = list(iter_project_files(root, include_existing_wiki=True))
    language, language_reason = detect_language(root, files)
    project_kind, kind_reasons = classify_project(root, files)
    manifest_hits = sorted(name for name in CODE_MANIFESTS if (root / name).exists())
    counts = {
        "files_total": len(files),
        "markdown": sum(1 for p in files if p.suffix.lower() in MARKDOWN_EXTS),
        "code": sum(1 for p in files if p.suffix.lower() in CODE_EXTS),
        "source_documents": sum(1 for p in files if p.suffix.lower() in SOURCE_EXTS),
        "media": sum(1 for p in files if p.suffix.lower() in MEDIA_EXTS),
        "existing_wiki_files": sum(1 for p in all_files if "_wiki" in p.relative_to(root).parts),
    }
    existing_wiki = {
        "has_wiki_dir": (root / "_wiki").is_dir(),
        "has_meta_index": (root / "_wiki" / "90-meta" / "index.md").exists()
        or (root / "90-meta" / "index.md").exists(),
        "has_meta_log": (root / "_wiki" / "90-meta" / "log.md").exists()
        or (root / "90-meta" / "log.md").exists(),
    }
    root_zone_conflicts = sorted(name for name in ZONE_DIRS if (root / name).exists() and project_kind == "code")
    risks = []
    if existing_wiki["has_wiki_dir"]:
        risks.append("existing _wiki directory will be updated, not replaced")
    if root_zone_conflicts:
        risks.append("root already has wiki-like folders: " + ", ".join(root_zone_conflicts))
    if counts["markdown"] > 25 and project_kind != "code":
        risks.append("many markdown files; migration may produce many moves")
    if counts["code"] > 0 and project_kind != "code":
        risks.append("some code-like files in a knowledge project; review before moving")
    wiki_root = "_wiki" if project_kind == "code" else "."
    return {
        "root": str(root),
        "project_name": root.name,
        "project_kind": project_kind,
        "project_kind_reasons": kind_reasons,
        "language": language,
        "language_reason": language_reason,
        "recommended_wiki_root": wiki_root,
        "counts": counts,
        "code_manifests": manifest_hits,
        "existing_wiki": existing_wiki,
        "risks": risks,
    }


def print_markdown(report: dict[str, Any]) -> None:
    print(f"# LLM Wiki Project Audit: {report['project_name']}")
    print()
    print(f"- Root: `{report['root']}`")
    print(f"- Project kind: `{report['project_kind']}`")
    print(f"- Recommended wiki root: `{report['recommended_wiki_root']}`")
    print(f"- Language: `{report['language']}` ({report['language_reason']})")
    print()
    print("## Counts")
    for key, value in report["counts"].items():
        print(f"- {key}: {value}")
    print()
    print("## Signals")
    for reason in report["project_kind_reasons"]:
        print(f"- {reason}")
    if report["code_manifests"]:
        print("- manifests: " + ", ".join(report["code_manifests"]))
    print()
    print("## Existing Wiki")
    for key, value in report["existing_wiki"].items():
        print(f"- {key}: {value}")
    print()
    print("## Risks")
    if report["risks"]:
        for risk in report["risks"]:
            print(f"- {risk}")
    else:
        print("- none detected")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a project for LLM Wiki creation or migration.")
    parser.add_argument("project", nargs="?", default=".", help="Project directory")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown")
    args = parser.parse_args()
    report = audit(Path(args.project))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
