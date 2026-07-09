# LLM Wiki Projects

[![en](https://img.shields.io/badge/lang-English-blue)](README.md) [![ru](https://img.shields.io/badge/lang-Русский-green)](README.ru.md)

Create, audit, migrate, and maintain projects as compact Obsidian-like LLM Wiki knowledge bases.

This skill turns a project folder into a durable wiki with `wiki-home`, source wrappers, atomic notes, project dashboards, maps, logs, governance files, and validation. The wiki becomes the long-lived project memory; chat stays the working surface.

## What It Does

- Audits a project before migration.
- Creates a wiki layout with `00-inbox`, `10-sources`, `20-notes`, `30-maps`, `40-projects`, `90-meta`, and `assets`.
- Keeps code repositories intact and creates a repo-local `_wiki/` when needed.
- Migrates note-like folders conservatively.
- Generates source notes, project dashboards, maps, logs, Obsidian Bases, and Canvas templates.
- Validates wikilinks, frontmatter, duplicate note names, orphan notes, and common Obsidian table-link hazards.

## Requirements

- Python 3.
- Claude Code or another agent that can read skill files and run local scripts.
- Optional: Obsidian for browsing the generated markdown wiki.

No external Python packages are required.

## Installation

### Claude Code style

```bash
mkdir -p .claude/skills
cp -r llm-wiki-projects/.claude/skills/llm-wiki-projects .claude/skills/
```

Register in `.claude/settings.json`:

```json
{
  "skills": {
    "llm-wiki-projects": {
      "path": ".claude/skills/llm-wiki-projects/SKILL.md",
      "description": "Create and maintain Obsidian-like LLM Wiki project knowledge bases",
      "trigger": "/wiki"
    }
  }
}
```

### Codex style

```bash
mkdir -p ~/.codex/skills
cp -r llm-wiki-projects/.claude/skills/llm-wiki-projects ~/.codex/skills/
```

## Usage

Ask the agent to use the skill:

```text
/wiki create an LLM Wiki for this project
/wiki audit this repository knowledge structure
/wiki migrate these research notes into a governed project wiki
/wiki validate the wiki and write a health report
```

The helper scripts can also be run directly:

```bash
python3 .claude/skills/llm-wiki-projects/scripts/audit_project.py /path/to/project
python3 .claude/skills/llm-wiki-projects/scripts/migrate_project.py /path/to/project
python3 .claude/skills/llm-wiki-projects/scripts/validate_wiki.py /path/to/project --write-report
```

## Safety Notes

- The audit script is read-only.
- For code repositories, migration keeps source code, package files, lockfiles, tests, `README`, `LICENSE`, and `CHANGELOG` in place.
- For knowledge-only projects, migration may move recognized note/source files into wiki zones. Run audit first if you want to inspect the plan.
- Raw sources are preserved as evidence; synthesis goes into wiki notes.

## Skill Contents

- `SKILL.md` — main agent workflow.
- `scripts/` — audit, migration, and validation tools.
- `references/` — methodology, schemas, workflows, governance, source lifecycle, and Obsidian integration notes.
- `assets/templates/` — generated note templates.
- `assets/bases/` and `assets/canvas/` — Obsidian Bases and Canvas starter assets.

## License

MIT
