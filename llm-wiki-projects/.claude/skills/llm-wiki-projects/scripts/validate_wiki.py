#!/usr/bin/env python3
"""Validate an Obsidian-like LLM Wiki."""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import defaultdict, deque
from datetime import datetime
from pathlib import Path
from typing import Any

BASE_SKIP_DIRS = {".git", ".obsidian", ".cache", "__pycache__", "node_modules", "vendor"}
TOOLING_SKIP_DIRS = {
    ".agents",
    ".claude",
    ".codex",
    ".idea",
    ".vscode",
    "scripts",
    "versions",
    "reports",
    "format-checklists",
    "journal-templates",
}
SKIP_DIRS = BASE_SKIP_DIRS | TOOLING_SKIP_DIRS
SKIP_FILES = {"AGENTS.md", "CLAUDE.md"}
WIKILINK_RE = re.compile(r"!?\[\[([^\]]+)\]\]")
TABLE_LINE_RE = re.compile(r"^\s*\|.*\|\s*$")
SEPARATOR_LINE_RE = re.compile(r"^\s*\|[\s\-:|]+\|\s*$")
REQUIRED_META = ["90-meta/index.md", "90-meta/log.md", "90-meta/wiki-rules.md"]
ENTRYPOINTS = [
    "wiki-home.md",
    "00-inbox.md",
    "10-sources.md",
    "20-notes.md",
    "30-maps.md",
    "40-projects.md",
    "90-meta.md",
    "assets.md",
    "90-meta/index.md",
]


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def find_wiki_root(project: Path) -> Path:
    project = project.expanduser().resolve()
    if (project / "_wiki" / "90-meta").exists():
        return project / "_wiki"
    if (project / "90-meta").exists():
        return project
    return project / "_wiki" if (project / "_wiki").exists() else project


def iter_files(root: Path, suffix: str | None = None, skip_dirs: set[str] | None = None):
    ignored = SKIP_DIRS if skip_dirs is None else skip_dirs
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ignored]
        for name in filenames:
            if name in SKIP_FILES:
                continue
            path = Path(dirpath) / name
            if suffix is None or path.suffix.lower() == suffix:
                yield path


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    block = text[4:end].splitlines()
    data: dict[str, Any] = {}
    current_key: str | None = None
    for line in block:
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, []).append(line[4:].strip())
            continue
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            current_key = key.strip()
            value = value.strip()
            data[current_key] = [] if value == "" else value
    return data


def wikilink_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return target


def resolve_wikilink(target: str, root: Path, page_by_stem: dict[str, list[Path]]) -> bool:
    if not target:
        return True
    if target.startswith(("http://", "https://")):
        return True
    normalized = target.replace("\\", "/")
    if "/" in normalized or Path(normalized).suffix:
        candidates = [
            root / normalized,
            root / f"{normalized}.md",
        ]
        return any(candidate.exists() for candidate in candidates)
    return target in page_by_stem or f"{target}.md" in page_by_stem


def resolved_wikilink_paths(target: str, root: Path, page_by_stem: dict[str, list[Path]]) -> list[Path]:
    if not target or target.startswith(("http://", "https://")):
        return []
    normalized = target.replace("\\", "/")
    if "/" in normalized or Path(normalized).suffix:
        candidates = [root / normalized, root / f"{normalized}.md"]
        return [candidate for candidate in candidates if candidate.exists()]
    return page_by_stem.get(target) or page_by_stem.get(f"{target}.md") or []


def is_in_inline_code(line: str, index: int) -> bool:
    return line[:index].count("`") % 2 == 1


def strip_inline_code(line: str) -> str:
    return re.sub(r"`[^`]*`", "", line)


def find_wikilinks_in_tables(text: str, rel: str) -> list[str]:
    issues: list[str] = []
    in_table = False
    in_code_block = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if SEPARATOR_LINE_RE.match(line):
            in_table = True
            continue
        if not TABLE_LINE_RE.match(line):
            in_table = False
            continue
        if not in_table:
            continue
        scan_line = strip_inline_code(line)
        for match in re.findall(r"\[\[[^\]]*(?:\\\||\|)[^\]]*\]\]", scan_line):
            issues.append(f"wikilink with alias/pipe inside Markdown table in {rel}:{lineno}: {match}")
        cells = [cell.strip() for cell in scan_line.strip().strip("|").split("|")]
        for cell in cells:
            if cell.count("[[") != cell.count("]]"):
                issues.append(f"unbalanced wikilink brackets inside Markdown table in {rel}:{lineno}: {cell}")
                break
    return issues


def find_relative_wikilinks(text: str, rel: str) -> list[str]:
    issues: list[str] = []
    in_code_block = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        for match in WIKILINK_RE.finditer(line):
            if is_in_inline_code(line, match.start()):
                continue
            target = wikilink_target(match.group(1))
            if target.startswith("../") or target.startswith("./") or "/../" in target:
                issues.append(f"relative path inside wikilink in {rel}:{lineno}: [[{target}]]")
    return issues


def find_unbalanced_wikilinks(text: str, rel: str) -> list[str]:
    issues: list[str] = []
    in_code_block = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        scan_line = strip_inline_code(line)
        if scan_line.count("[[") != scan_line.count("]]"):
            issues.append(f"unbalanced wikilink brackets in {rel}:{lineno}")
    return issues


def find_frontmatter_syntax_errors(text: str, rel: str) -> list[str]:
    issues: list[str] = []
    if not text.startswith("---\n"):
        return issues
    end = text.find("\n---", 4)
    if end == -1:
        return [f"frontmatter opens but does not close in {rel}:1"]
    for lineno, line in enumerate(text[4:end].splitlines(), 2):
        stripped = line.rstrip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith(" ") or stripped.startswith("- "):
            continue
        if ":" not in stripped:
            issues.append(f"frontmatter line has no colon in {rel}:{lineno}: {stripped}")
    return issues


def validate(project: Path, include_tooling: bool = False) -> dict[str, Any]:
    root = find_wiki_root(project)
    skip_dirs = BASE_SKIP_DIRS if include_tooling else SKIP_DIRS
    markdown_files = list(iter_files(root, ".md", skip_dirs))
    page_by_stem: dict[str, list[Path]] = defaultdict(list)
    frontmatter: dict[str, dict[str, Any]] = {}
    inbound: dict[Path, int] = defaultdict(int)
    graph: dict[Path, set[Path]] = defaultdict(set)
    errors: list[str] = []
    warnings: list[str] = []

    for path in markdown_files:
        page_by_stem[path.stem].append(path)
        page_by_stem[path.name].append(path)
        frontmatter[str(path)] = parse_frontmatter(read_text(path))

    for required in REQUIRED_META:
        if not (root / required).exists():
            errors.append(f"missing required file: {required}")

    for key, paths in sorted(page_by_stem.items()):
        if key.endswith(".md"):
            continue
        unique_paths = sorted({p for p in paths})
        if len(unique_paths) > 1:
            errors.append("duplicate note stem `{}`: {}".format(key, ", ".join(p.relative_to(root).as_posix() for p in unique_paths)))

    broken_links = []
    for path in markdown_files:
        text = read_text(path)
        rel = path.relative_to(root).as_posix()
        errors.extend(find_wikilinks_in_tables(text, rel))
        errors.extend(find_relative_wikilinks(text, rel))
        errors.extend(find_unbalanced_wikilinks(text, rel))
        errors.extend(find_frontmatter_syntax_errors(text, rel))
        in_code_block = False
        for line in text.splitlines():
            if line.lstrip().startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue
            for match in WIKILINK_RE.finditer(line):
                if is_in_inline_code(line, match.start()):
                    continue
                target = wikilink_target(match.group(1))
                if not resolve_wikilink(target, root, page_by_stem):
                    broken_links.append({"file": rel, "target": target})
                else:
                    for candidate in resolved_wikilink_paths(target, root, page_by_stem):
                        inbound[candidate] += 1
                        graph[path].add(candidate)
    for link in broken_links:
        errors.append(f"broken wikilink in {link['file']}: [[{link['target']}]]")

    for path in markdown_files:
        rel = path.relative_to(root).as_posix()
        fm = frontmatter.get(str(path), {})
        if rel.startswith("90-meta/") and path.name in {"log.md", "migration-manifest.md"}:
            continue
        if not fm:
            warnings.append(f"missing frontmatter: {rel}")
            continue
        if "type" not in fm:
            warnings.append(f"missing frontmatter field `type`: {rel}")
        if "status" not in fm:
            warnings.append(f"missing frontmatter field `status`: {rel}")

    for path in markdown_files:
        rel = path.relative_to(root).as_posix()
        if rel.startswith("90-meta/") or path.name == "index.md":
            continue
        if rel.startswith("30-maps/"):
            continue
        if inbound[path] == 0:
            warnings.append(f"orphan note: {rel}")

    home = root / "wiki-home.md"
    if home.exists():
        reachable_from_home = reachable_notes([home], graph)
        for path in sorted(set(markdown_files) - reachable_from_home):
            rel = path.relative_to(root).as_posix()
            warnings.append(f"unreachable from wiki-home: {rel}")
    else:
        warnings.append("missing wiki-home.md for reachability check")

    entrypoints = [root / name for name in ENTRYPOINTS if (root / name).exists()]
    reachable_from_entrypoints = reachable_notes(entrypoints, graph)
    for path in sorted(set(markdown_files) - reachable_from_entrypoints):
        rel = path.relative_to(root).as_posix()
        warnings.append(f"unreachable from root entrypoints: {rel}")

    return {
        "wiki_root": str(root),
        "markdown_files": len(markdown_files),
        "include_tooling": include_tooling,
        "skipped_dirs": sorted(skip_dirs),
        "errors": errors,
        "warnings": warnings,
        "ok": not errors,
}


def reachable_notes(starts: list[Path], graph: dict[Path, set[Path]]) -> set[Path]:
    seen = set(starts)
    queue: deque[Path] = deque(starts)
    while queue:
        current = queue.popleft()
        for linked in graph.get(current, set()):
            if linked not in seen:
                seen.add(linked)
                queue.append(linked)
    return seen


def write_report(result: dict[str, Any]) -> Path:
    root = Path(result["wiki_root"])
    path = root / "90-meta" / "health-report.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    content = (
        "---\n"
        "type: meta\n"
        "status: active\n"
        f"created: {today()}\n"
        f"updated: {today()}\n"
        "tags:\n"
        "  - llm-wiki/health\n"
        "---\n\n"
        "# Wiki Health Report\n\n"
        f"- Wiki root: `{result['wiki_root']}`\n"
        f"- Markdown files: `{result['markdown_files']}`\n"
        f"- Status: `{'ok' if result['ok'] else 'errors'}`\n\n"
        "## Errors\n\n"
        + ("\n".join(f"- {item}" for item in result["errors"]) or "- none")
        + "\n\n## Warnings\n\n"
        + ("\n".join(f"- {item}" for item in result["warnings"]) or "- none")
        + "\n"
    )
    path.write_text(content, encoding="utf-8")
    return path


def print_markdown(result: dict[str, Any], report_path: Path | None = None) -> None:
    print("# LLM Wiki Validation")
    print()
    print(f"- Wiki root: `{result['wiki_root']}`")
    print(f"- Markdown files: {result['markdown_files']}")
    print(f"- OK: {result['ok']}")
    if report_path:
        print(f"- Health report: `{report_path}`")
    print()
    print("## Errors")
    if result["errors"]:
        for item in result["errors"]:
            print(f"- {item}")
    else:
        print("- none")
    print()
    print("## Warnings")
    if result["warnings"]:
        for item in result["warnings"]:
            print(f"- {item}")
    else:
        print("- none")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an LLM Wiki project.")
    parser.add_argument("project", nargs="?", default=".", help="Project or wiki directory")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    parser.add_argument("--write-report", action="store_true", help="Write 90-meta/health-report.md")
    parser.add_argument("--include-tooling", action="store_true", help="Include local agent/tooling directories in validation")
    args = parser.parse_args()
    result = validate(Path(args.project), include_tooling=args.include_tooling)
    report_path = write_report(result) if args.write_report else None
    if args.json:
        payload = dict(result)
        if report_path:
            payload["health_report"] = str(report_path)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_markdown(result, report_path)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
