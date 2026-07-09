#!/usr/bin/env python3
"""Create or migrate a project into the LLM Wiki layout."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

from audit_project import MARKDOWN_EXTS, MEDIA_EXTS, SKIP_DIRS, SOURCE_EXTS, audit, iter_project_files

ZONE_DIRS = ["00-inbox", "10-sources", "20-notes", "30-maps", "40-projects", "90-meta", "assets"]
ZONE_DESCRIPTIONS = {
    "00-inbox": "unprocessed captures and temporary working notes",
    "10-sources": "source notes and evidence files",
    "20-notes": "atomic notes and durable synthesis",
    "30-maps": "Maps of Content, outlines, and canvases",
    "40-projects": "project state, decisions, and tasks",
    "90-meta": "rules, logs, manifests, health reports, and bases",
    "assets": "local images and other media used by notes",
}
ZONE_START_LINKS = {
    "10-sources": [
        ("90-meta/index", "Wiki Catalog"),
        ("30-maps/project-map", "Project Map"),
    ],
    "20-notes": [
        ("30-maps/project-map", "Project Map"),
        ("40-projects", "Projects"),
    ],
    "30-maps": [
        ("30-maps/project-map", "Project Map"),
        ("wiki-home", "Wiki Home"),
    ],
    "40-projects": [
        ("30-maps/project-map", "Project Map"),
    ],
    "90-meta": [
        ("90-meta/index", "Wiki Catalog"),
        ("90-meta/log", "Activity Log"),
        ("90-meta/wiki-rules", "Wiki Rules"),
    ],
}
NOTE_LIKE_DIRS = {"notes", "research", "knowledge", "sources", "source", "clips", "vault", "zettelkasten", "inbox"}
CANONICAL_CODE_DOCS = {
    "README.md",
    "Readme.md",
    "readme.md",
    "CHANGELOG.md",
    "Changelog.md",
    "LICENSE",
    "LICENSE.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "AGENTS.md",
}


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\s.-]+", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s_.]+", "-", value)
    value = value.strip(".-")
    return value or "untitled"


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem, suffix = path.stem, path.suffix
    parent = path.parent
    for index in range(2, 10_000):
        candidate = parent / f"{stem}-{index}{suffix}"
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"Could not find unique path for {path}")


def rel(from_dir: Path, target: Path) -> str:
    return Path(target).resolve().relative_to(from_dir.resolve()).as_posix()


def safe_read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def has_frontmatter(text: str) -> bool:
    return text.startswith("---\n") and text.find("\n---", 4) != -1


def localized(language: str) -> dict[str, str]:
    if language == "ru":
        return {
            "wiki_entry": "Вход в wiki проекта.",
            "start": "С чего начать",
            "areas": "Основные зоны",
            "catalog": "Каталог wiki",
            "rules": "Правила ведения wiki",
            "log": "Журнал изменений",
            "created_by": "Создано автоматической миграцией LLM Wiki.",
            "purpose": "Назначение",
            "summary": "Кратко",
            "moved": "Перемещено",
            "registered": "Зарегистрировано без перемещения",
            "skipped": "Пропущено",
            "validation": "Проверка",
        }
    return {
        "wiki_entry": "Entry point for the project wiki.",
        "start": "Start Here",
        "areas": "Main Areas",
        "catalog": "Wiki Catalog",
        "rules": "Wiki Rules",
        "log": "Activity Log",
        "created_by": "Created by the LLM Wiki migration.",
        "purpose": "Purpose",
        "summary": "Summary",
        "moved": "Moved",
        "registered": "Registered Without Moving",
        "skipped": "Skipped",
        "validation": "Validation",
    }


def render_frontmatter(note_type: str, status: str, language: str, tags: list[str] | None = None) -> str:
    date = today()
    tag_lines = "\n".join(f"  - {tag}" for tag in (tags or ["llm-wiki"]))
    return (
        "---\n"
        f"type: {note_type}\n"
        f"status: {status}\n"
        f"created: {date}\n"
        f"updated: {date}\n"
        f"language: {language}\n"
        "tags:\n"
        f"{tag_lines}\n"
        "---\n\n"
    )


def render_template(path: Path, values: dict[str, str]) -> str:
    content = safe_read(path)
    for key, value in values.items():
        content = content.replace("{{" + key + "}}", value)
    return content


def note_type_for_target(target: Path) -> tuple[str, list[str]]:
    parts = set(target.parts)
    if "10-sources" in parts:
        return "source", ["source"]
    if "30-maps" in parts:
        return "map", ["map"]
    if "40-projects" in parts and "decisions" in parts:
        return "decision", ["decision"]
    if "40-projects" in parts:
        return "project", ["project"]
    return "atomic", ["note"]


def normalize_moved_markdown(path: Path, language: str) -> None:
    if path.suffix.lower() not in MARKDOWN_EXTS:
        return
    text = safe_read(path)
    if has_frontmatter(text):
        return
    note_type, tags = note_type_for_target(path)
    status = "active" if note_type in {"source", "map", "project", "decision"} else "draft"
    title = path.stem.replace("-", " ").replace("_", " ").strip().title()
    frontmatter = render_frontmatter(note_type, status, language, tags)
    if not text.lstrip().startswith("# "):
        text = f"# {title}\n\n{text}"
    path.write_text(frontmatter + text, encoding="utf-8")


def write_once(path: Path, content: str, operations: list[dict[str, Any]], dry_run: bool) -> None:
    if path.exists():
        operations.append({"action": "skip", "path": str(path), "reason": "already exists"})
        return
    operations.append({"action": "create", "path": str(path)})
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def write_zone_index_once(wiki: Path, zone: str, lang: str, operations: list[dict[str, Any]], dry_run: bool) -> None:
    path = wiki / f"{zone}.md"
    if path.exists() and safe_read(path).strip():
        operations.append({"action": "skip", "path": str(path), "reason": "already exists"})
        return
    action = "repair-empty-zone-index" if path.exists() else "create"
    operations.append({"action": action, "path": str(path)})
    if dry_run:
        return
    links = ZONE_START_LINKS.get(zone, [])
    link_lines = "\n".join(f"- [[{target}|{label}]]" for target, label in links) or "- [[wiki-home|Wiki Home]]"
    content = (
        render_frontmatter("map", "active", lang, ["llm-wiki/zone"])
        + f"# {zone}\n\n"
        + f"{ZONE_DESCRIPTIONS[zone]}.\n\n"
        + "## Start Here\n\n"
        + f"{link_lines}\n\n"
        + "## Folder\n\n"
        + f"The backing folder is `{zone}/`.\n"
    )
    path.write_text(content, encoding="utf-8")


def copy_once(src: Path, dst: Path, operations: list[dict[str, Any]], dry_run: bool) -> None:
    if dst.exists():
        operations.append({"action": "skip", "path": str(dst), "reason": "already exists"})
        return
    operations.append({"action": "copy-template", "from": str(src), "to": str(dst)})
    if not dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def create_core_files(project: Path, wiki: Path, report: dict[str, Any], operations: list[dict[str, Any]], dry_run: bool) -> None:
    lang = report["language"]
    text = localized(lang)
    name = report["project_name"]
    for zone in ZONE_DIRS:
        target = wiki / zone
        operations.append({"action": "ensure-dir", "path": str(target)})
        if not dry_run:
            target.mkdir(parents=True, exist_ok=True)
    for nested in (
        wiki / "assets" / "sources",
        wiki / "90-meta" / "bases",
        wiki / "90-meta" / "rule-packs",
    ):
        operations.append({"action": "ensure-dir", "path": str(nested)})
        if not dry_run:
            nested.mkdir(parents=True, exist_ok=True)
    for zone in ZONE_DIRS:
        write_zone_index_once(wiki, zone, lang, operations, dry_run)

    entry = (
        render_frontmatter("meta", "active", lang, ["llm-wiki/index"])
        + f"# {name} Wiki\n\n"
        + f"{text['wiki_entry']}\n\n"
        + f"## {text['start']}\n\n"
        + "- [[90-meta/index|{catalog}]]\n"
        + "- [[90-meta/wiki-rules|{rules}]]\n"
        + "- [[90-meta/log|{log}]]\n\n"
        + f"## {text['areas']}\n\n"
        + "- [[00-inbox|00-inbox]]\n"
        + "- [[10-sources|10-sources]]\n"
        + "- [[20-notes|20-notes]]\n"
        + "- [[30-maps|30-maps]]\n"
        + "- [[40-projects|40-projects]]\n"
        + "- [[90-meta|90-meta]]\n"
        + "- [[assets|assets]]\n"
    ).format(catalog=text["catalog"], rules=text["rules"], log=text["log"])
    write_once(wiki / "wiki-home.md", entry, operations, dry_run)

    meta_index = (
        render_frontmatter("meta", "active", lang, ["llm-wiki/catalog"])
        + f"# {text['catalog']}\n\n"
        + f"{text['created_by']}\n\n"
        + "## Pages\n\n"
        + "- [[wiki-home|Wiki Entry]]\n"
        + "- [[wiki-rules|Wiki Rules]]\n"
        + "- [[source-workflow|Source Workflow]]\n"
        + "- [[skills-registry|Skills Registry]]\n"
        + "- [[lessons-learned|Lessons Learned]]\n"
        + "- [[90-meta/rule-packs/general|Rule Pack: General]]\n"
        + "- [[log|Activity Log]]\n"
        + "- [[migration-manifest|Migration Manifest]]\n"
        + "- [[30-maps/project-map|Project Map]]\n\n"
        + "## Zones\n\n"
        + "\n".join(f"- [[{zone}|{zone}]] - {ZONE_DESCRIPTIONS[zone]}" for zone in ZONE_DIRS)
        + "\n"
    )
    write_once(wiki / "90-meta" / "index.md", meta_index, operations, dry_run)

    rules = (
        render_frontmatter("meta", "active", lang, ["llm-wiki/rules"])
        + f"# {text['rules']}\n\n"
        + "- Preserve raw sources and record provenance.\n"
        + "- Keep generated synthesis in linked markdown notes.\n"
        + "- Update `90-meta/index.md` and `90-meta/log.md` after meaningful changes.\n"
        + "- Keep project notes synchronized with current status, artifacts, decisions, and next steps.\n"
        + "- Each durable source should have a wrapper note in `10-sources/`; raw evidence belongs in `assets/sources/` when local copies are allowed.\n"
        + "- Record repeated process failures in `90-meta/lessons-learned.md` and promote recurring lessons into rules, templates, validators, or local skills.\n"
        + "- Keep domain-specific rules in `90-meta/rule-packs/` rather than hardcoding them into global workflows.\n"
        + "- Use wikilinks for notes and Markdown links for non-note files.\n"
        + "- Avoid wikilinks with aliases inside Markdown tables; use Markdown links there or move wikilinks outside the table.\n"
        + "- Avoid relative paths inside wikilinks unless the project explicitly uses path-based resolution.\n"
        + "- Prefer atomic notes for reusable ideas and maps for navigation.\n"
        + "- Run validation after migrations and major edits.\n"
    )
    write_once(wiki / "90-meta" / "wiki-rules.md", rules, operations, dry_run)

    skill_dir = Path(__file__).resolve().parents[1]
    template_values = {
        "date": today(),
        "language": lang,
        "project_name": name,
        "title": name,
        "project_id": slugify(name),
    }
    for template_name, target_name in (
        ("lessons-learned.md", "lessons-learned.md"),
        ("source-workflow.md", "source-workflow.md"),
        ("skills-registry.md", "skills-registry.md"),
    ):
        content = render_template(skill_dir / "assets" / "templates" / template_name, template_values)
        write_once(wiki / "90-meta" / target_name, content, operations, dry_run)
    rule_pack = render_template(skill_dir / "assets" / "templates" / "rule-pack.md", template_values)
    write_once(wiki / "90-meta" / "rule-packs" / "general.md", rule_pack, operations, dry_run)

    log_path = wiki / "90-meta" / "log.md"
    log_entry = f"\n## [{today()}] migrate | LLM Wiki initialized\n\n- Project kind: `{report['project_kind']}`\n- Wiki root: `{wiki}`\n"
    if log_path.exists():
        operations.append({"action": "append-log", "path": str(log_path)})
        if not dry_run:
            with log_path.open("a", encoding="utf-8") as handle:
                handle.write(log_entry)
    else:
        log = render_frontmatter("meta", "active", lang, ["llm-wiki/log"]) + f"# {text['log']}\n" + log_entry
        write_once(log_path, log, operations, dry_run)

    project_id = slugify(name)
    project_dir = wiki / "40-projects" / project_id
    operations.append({"action": "ensure-dir", "path": str(project_dir)})
    if not dry_run:
        project_dir.mkdir(parents=True, exist_ok=True)
        (project_dir / "versions").mkdir(exist_ok=True)
        (project_dir / "reports").mkdir(exist_ok=True)
        (project_dir / "assets").mkdir(exist_ok=True)
    project_note = render_template(
        skill_dir / "assets" / "templates" / "project-note.md",
        template_values,
    )
    write_once(project_dir / f"{project_id}.md", project_note, operations, dry_run)
    orchestration = render_template(
        skill_dir / "assets" / "templates" / "orchestration.md",
        template_values,
    )
    write_once(project_dir / f"{project_id}-orchestration.md", orchestration, operations, dry_run)

    map_note = (
        render_frontmatter("map", "active", lang, ["map"])
        + "# Project Map\n\n"
        + "- [[90-meta/index|Wiki Index]]\n"
        + f"- [[40-projects/{project_id}/{project_id}|{name}]]\n"
    )
    write_once(wiki / "30-maps" / "project-map.md", map_note, operations, dry_run)

    for base in ("sources.base", "atomic-notes.base", "projects.base"):
        copy_once(skill_dir / "assets" / "bases" / base, wiki / "90-meta" / "bases" / base, operations, dry_run)
    copy_once(skill_dir / "assets" / "canvas" / "project-map.canvas", wiki / "30-maps" / "project-map.canvas", operations, dry_run)


def note_like(path: Path, root: Path) -> bool:
    parts = {p.lower() for p in path.relative_to(root).parts[:-1]}
    return bool(parts & NOTE_LIKE_DIRS)


def classify_target(path: Path, root: Path) -> Path:
    name = path.name.lower()
    suffix = path.suffix.lower()
    text = safe_read(path)[:4000] if suffix in MARKDOWN_EXTS else ""
    if suffix not in MARKDOWN_EXTS:
        if suffix in SOURCE_EXTS:
            return Path("assets/sources")
        if suffix in MEDIA_EXTS:
            return Path("assets")
        return Path("assets")
    if "decision" in name or name.startswith("adr-") or "/adr/" in path.as_posix().lower():
        return Path("40-projects/decisions")
    if "project" in name or "roadmap" in name or "task" in name:
        return Path("40-projects")
    if "moc" in name or "map" in name or name in {"index.md", "overview.md"}:
        return Path("30-maps")
    if re.search(r"source[-_ ]?|source:|source_url:|source-path:|original-url:|url:", text, re.IGNORECASE) or "source" in {p.lower() for p in path.relative_to(root).parts}:
        return Path("10-sources")
    if note_like(path, root):
        return Path("20-notes")
    return Path("20-notes")


def should_ignore_candidate(path: Path, root: Path, wiki: Path) -> bool:
    try:
        rel_parts = path.relative_to(root).parts
    except ValueError:
        return True
    if any(part in SKIP_DIRS for part in rel_parts):
        return True
    if path.parent == wiki and path.name in {f"{zone}.md" for zone in ZONE_DIRS}:
        return True
    if wiki == root:
        if rel_parts and rel_parts[0] in ZONE_DIRS:
            return True
        if path.name == "wiki-home.md":
            return True
        return False
    try:
        path.relative_to(wiki)
        return True
    except ValueError:
        return False


def create_source_stub(original: Path, root: Path, wiki: Path, lang: str, operations: list[dict[str, Any]], dry_run: bool) -> None:
    title = original.stem.replace("-", " ").replace("_", " ").strip().title() or original.name
    stub_name = unique_path(wiki / "10-sources" / f"{slugify(original.stem)}.md")
    relative_link = os.path.relpath(original, start=stub_name.parent)
    try:
        source_path = original.relative_to(wiki).as_posix()
    except ValueError:
        try:
            source_path = original.relative_to(root).as_posix()
        except ValueError:
            source_path = original.as_posix()
    content = (
        "---\n"
        "type: source\n"
        "status: active\n"
        "source-kind: file\n"
        f"source-path: {source_path}\n"
        "original-url:\n"
        "doi:\n"
        "authors: []\n"
        "year:\n"
        f"title: \"{title}\"\n"
        "venue:\n"
        "read-status: not-read\n"
        "key-claims-extracted: false\n"
        "used-in: []\n"
        f"created: {today()}\n"
        f"updated: {today()}\n"
        f"language: {lang}\n"
        "tags:\n"
        "  - source\n"
        "---\n\n"
        f"# {title}\n\n"
        "## What This Is\n\n"
        "## Where It Lives\n\n"
        f"- Wiki copy: [{original.name}]({relative_link})\n"
        "- Original:\n"
        "- Identifier:\n\n"
        "## Original Abstract or Summary\n\n"
        "## Key Claims\n\n"
        "- Claim:\n"
        "  - Evidence:\n"
        "  - Location:\n\n"
        "## Methods, Results, Limitations\n\n"
        "## What To Use In Projects\n\n"
        "## Citation or Reuse Notes\n\n"
        "## Derived Notes\n"
    )
    operations.append({"action": "register-source", "from": str(original), "to": str(stub_name)})
    if not dry_run:
        stub_name.parent.mkdir(parents=True, exist_ok=True)
        stub_name.write_text(content, encoding="utf-8")


def migrate_candidates(root: Path, wiki: Path, report: dict[str, Any], operations: list[dict[str, Any]], dry_run: bool) -> None:
    project_kind = report["project_kind"]
    lang = report["language"]
    for path in list(iter_project_files(root, include_existing_wiki=False)):
        if should_ignore_candidate(path, root, wiki):
            continue
        suffix = path.suffix.lower()
        if suffix not in MARKDOWN_EXTS and suffix not in SOURCE_EXTS and suffix not in MEDIA_EXTS:
            continue
        if path.name in CANONICAL_CODE_DOCS and project_kind != "code":
            operations.append({"action": "skip", "path": str(path), "reason": "canonical project file"})
            continue
        if path.name in CANONICAL_CODE_DOCS and project_kind == "code":
            create_source_stub(path, root, wiki, lang, operations, dry_run)
            continue
        if project_kind == "code" and not note_like(path, root):
            if suffix in MARKDOWN_EXTS and (path.parent.name.lower() in {"docs", "documentation"} or path.parent == root):
                create_source_stub(path, root, wiki, lang, operations, dry_run)
            else:
                operations.append({"action": "skip", "path": str(path), "reason": "not a note-like code-repo document"})
            continue
        if suffix in SOURCE_EXTS and suffix not in MARKDOWN_EXTS:
            target_dir = wiki / "assets" / "sources"
            target = unique_path(target_dir / path.name)
            operations.append({"action": "move", "from": str(path), "to": str(target)})
            if not dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(path), str(target))
            create_source_stub(target, wiki, wiki, lang, operations, dry_run)
            continue
        target_dir = wiki / classify_target(path, root)
        target = unique_path(target_dir / path.name)
        operations.append({"action": "move", "from": str(path), "to": str(target)})
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(target))
            normalize_moved_markdown(target, lang)


def wikilink_for(wiki: Path, path: Path) -> str:
    relative = path.relative_to(wiki).with_suffix("").as_posix()
    return f"[[{relative}|{path.stem}]]"


def update_catalog(wiki: Path, operations: list[dict[str, Any]], dry_run: bool) -> None:
    page_ops = [
        op
        for op in operations
        if op["action"] in {"move", "register-source"}
        and Path(op["to"]).suffix.lower() in MARKDOWN_EXTS
        and Path(op["to"]).is_relative_to(wiki)
    ]
    if not page_ops:
        return
    catalog = wiki / "90-meta" / "index.md"
    lines = [f"\n## Migration {today()}\n"]
    for op in page_ops:
        lines.append(f"- {wikilink_for(wiki, Path(op['to']))}")
    operations.append({"action": "update-catalog", "path": str(catalog), "pages": len(page_ops)})
    if not dry_run:
        with catalog.open("a", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")


def write_manifest(wiki: Path, report: dict[str, Any], operations: list[dict[str, Any]], dry_run: bool) -> Path:
    text = localized(report["language"])
    manifest = wiki / "90-meta" / "migration-manifest.md"
    moved = [op for op in operations if op["action"] == "move"]
    registered = [op for op in operations if op["action"] == "register-source"]
    skipped = [op for op in operations if op["action"] == "skip"]
    content = (
        render_frontmatter("meta", "active", report["language"], ["llm-wiki/migration"])
        + "# Migration Manifest\n\n"
        + f"- Timestamp: `{timestamp()}`\n"
        + f"- Project kind: `{report['project_kind']}`\n"
        + f"- Wiki root: `{wiki}`\n"
        + f"- Language: `{report['language']}`\n\n"
        + f"## {text['moved']}\n\n"
    )
    content += "\n".join(f"- `{op['from']}` -> `{op['to']}`" for op in moved) or "- none"
    content += f"\n\n## {text['registered']}\n\n"
    content += "\n".join(f"- `{op['from']}` -> `{op['to']}`" for op in registered) or "- none"
    content += f"\n\n## {text['skipped']}\n\n"
    content += "\n".join(f"- `{op.get('path', op.get('from', ''))}` - {op.get('reason', op['action'])}" for op in skipped[:200]) or "- none"
    content += "\n\n## Raw Audit\n\n```json\n" + json.dumps(report, ensure_ascii=False, indent=2) + "\n```\n"
    operations.append({"action": "write-manifest", "path": str(manifest)})
    if not dry_run:
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(content, encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Create or migrate a project into an Obsidian-like LLM Wiki.")
    parser.add_argument("project", nargs="?", default=".", help="Project directory")
    parser.add_argument("--dry-run", action="store_true", help="Print planned operations without writing")
    parser.add_argument("--wiki-root", choices=["auto", "_wiki", "."], default="auto", help="Override wiki root")
    parser.add_argument("--json", action="store_true", help="Print JSON summary")
    args = parser.parse_args()

    root = Path(args.project).expanduser().resolve()
    report = audit(root)
    if args.wiki_root == "auto":
        wiki = root / "_wiki" if report["project_kind"] == "code" else root
    elif args.wiki_root == "_wiki":
        wiki = root / "_wiki"
    else:
        wiki = root

    operations: list[dict[str, Any]] = []
    create_core_files(root, wiki, report, operations, args.dry_run)
    migrate_candidates(root, wiki, report, operations, args.dry_run)
    update_catalog(wiki, operations, args.dry_run)
    manifest = write_manifest(wiki, report, operations, args.dry_run)

    summary = {
        "project": str(root),
        "wiki_root": str(wiki),
        "manifest": str(manifest),
        "dry_run": args.dry_run,
        "operations": operations,
    }
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"# LLM Wiki Migration: {root.name}")
        print()
        print(f"- Wiki root: `{wiki}`")
        print(f"- Manifest: `{manifest}`")
        print(f"- Dry run: `{args.dry_run}`")
        print()
        print("## Operations")
        for op in operations:
            if op["action"] == "move":
                print(f"- move `{op['from']}` -> `{op['to']}`")
            elif op["action"] == "register-source":
                print(f"- register `{op['from']}` -> `{op['to']}`")
            elif op["action"] in {"create", "copy-template", "write-manifest", "append-log"}:
                print(f"- {op['action']} `{op.get('path', op.get('to', ''))}`")
        print()
        print("Run validate_wiki.py next.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
