---
name: llm-wiki-projects
description: Create, audit, migrate, and maintain projects as compact Obsidian-like LLM Wiki knowledge bases. Use when an AI coding agent should create a new markdown/Obsidian project, convert an existing code repository or knowledge folder into a Karpathy-style LLM Wiki, improve project knowledge architecture, reorganize files into linked notes, create Maps of Content, Obsidian Bases or Canvas files, validate wikilinks/frontmatter, or maintain a repo-local `_wiki` for agent memory.
---

# LLM Wiki Projects

Build projects as living markdown wikis that compound over time. The wiki is the durable artifact; chat is only the working surface.

## Quick Start

1. Inspect the target with `scripts/audit_project.py <project>`.
2. For new or migrated projects, run `scripts/migrate_project.py <project>` unless the user only asked for analysis.
3. Validate with `scripts/validate_wiki.py <project>`.
4. Read references only as needed:
   - `references/methodology.md` for Karpathy LLM Wiki + Zettelkasten principles.
   - `references/schemas.md` for folders, frontmatter, naming, and link conventions.
   - `references/workflows.md` for create, migrate, ingest, query, lint, and maintenance flows.
   - `references/project-governance.md` for project dashboards, project-as-folder, orchestration logs, gates, and skills registry patterns.
   - `references/source-lifecycle.md` for source evidence wrappers, raw files, deep reads, and source-to-note promotion.
   - `references/self-learning.md` for lessons learned, rule promotion, and wiki self-improvement loops.
   - `references/obsidian-integrations.md` for Obsidian Markdown, Bases, Canvas, CLI, and web clipping skills.

Use absolute paths when running scripts from outside this skill, for example:

```bash
python3 .claude/skills/llm-wiki-projects/scripts/audit_project.py /path/to/project
python3 .claude/skills/llm-wiki-projects/scripts/migrate_project.py /path/to/project
python3 .claude/skills/llm-wiki-projects/scripts/validate_wiki.py /path/to/project

python3 ~/.codex/skills/llm-wiki-projects/scripts/audit_project.py /path/to/project
python3 ~/.codex/skills/llm-wiki-projects/scripts/migrate_project.py /path/to/project
python3 ~/.codex/skills/llm-wiki-projects/scripts/validate_wiki.py /path/to/project
```

## Operating Contract

- Preserve raw sources. Source files are evidence; the wiki is synthesis.
- In code repositories, keep code in place and create the wiki under `_wiki/`.
- In knowledge-only projects, use the project root as the wiki root.
- Use these zones: `00-inbox`, `10-sources`, `20-notes`, `30-maps`, `40-projects`, `90-meta`, `assets`.
- Create root zone index notes for each zone (`10-sources.md`, `20-notes.md`, etc.) and link to those with `[[10-sources]]` style wikilinks. Do not use Markdown links to folders for zone navigation; Obsidian may create empty notes from them.
- Use Obsidian wikilinks for internal notes and Markdown links for external URLs or local non-note files.
- Keep notes small and connected. Prefer one durable idea per atomic note, with links to source notes.
- Treat project notes as live dashboards: keep status, decisions, current artifacts, and next steps synchronized after meaningful work.
- Maintain `90-meta/index.md` as the content catalog, `90-meta/log.md` as the chronological activity log, `90-meta/lessons-learned.md` as the self-learning loop, and `90-meta/skills-registry.md` when the project has local skills or recurring agent workflows.
- Keep domain rules as local rule packs under `90-meta/rule-packs/` instead of hardcoding domain-specific policy into the global skill.
- Detect the project language from existing files. If empty or mixed, default generated service files to Russian.
- For migrations, write `90-meta/migration-manifest.md` and keep the final answer focused on what changed, what was skipped, and validation results.

## Script Roles

- `audit_project.py`: classify the project, detect language, locate existing wiki structure, count content types, and list migration risks.
- `migrate_project.py`: create the wiki structure, governance meta files, source workflow, project dashboard, orchestration log, Obsidian Bases/Canvas templates, and migration manifest; move or register recognized knowledge materials.
- `validate_wiki.py`: check required files, frontmatter, duplicate note names, broken wikilinks, orphan notes, reachability, Obsidian table-link hazards, relative wikilinks, unbalanced wikilinks, and frontmatter syntax. Use `--write-report` when the user wants a saved health report.

## Migration Policy

The skill may auto-migrate when the user asks to convert or improve a project. Be conservative about code repositories:

- Never move source code, build config, package manifests, lockfiles, tests, or canonical repo files such as `README.md`, `LICENSE`, and `CHANGELOG.md`.
- Move note-like folders such as `notes`, `research`, `knowledge`, `sources`, `clips`, `vault`, and `zettelkasten` into the wiki when safe.
- For important code-repo docs that should stay in place, create source notes in `_wiki/10-sources/` that link back to the original files.
- In knowledge-only folders, move recognized source and note files into wiki zones unless a name conflict or unsupported path makes that unsafe.
- Keep raw evidence in `assets/sources/` when the wiki owns the file; use `source-path` to point from `10-sources/<id>.md` to the raw file. For files that must stay outside the wiki, create a source wrapper that links to the original path.

## Obsidian Compatibility

When editing generated notes, use the local Obsidian skills when available:

- `obsidian-markdown` for properties, wikilinks, embeds, callouts, and note syntax.
- `obsidian-bases` for `.base` files.
- `json-canvas` for `.canvas` maps.
- `obsidian-cli` when the user asks to operate inside a real Obsidian vault.
- `defuddle` for turning web pages into clean markdown sources before ingest.

## Output Expectations

After acting, report:

- wiki root path;
- files or folders created/moved;
- manifest and health report paths;
- validation errors or remaining warnings;
- next useful maintenance step, if there is one.
