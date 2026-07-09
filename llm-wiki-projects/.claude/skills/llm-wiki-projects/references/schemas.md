# Schemas

Use this reference when creating or repairing wiki folders, note frontmatter, names, and links.

## Folder Layout

For code repositories:

```text
_wiki/
  wiki-home.md
  00-inbox.md
  10-sources.md
  20-notes.md
  30-maps.md
  40-projects.md
  90-meta.md
  assets.md
  index.md
  00-inbox/
  10-sources/
  20-notes/
  30-maps/
  40-projects/
  90-meta/
  assets/
```

For knowledge-only projects, use the same folders at the project root.

Folder meanings:

- `00-inbox`: unprocessed captures and temporary working notes.
- `10-sources`: source wrapper notes. Each durable source gets one markdown page.
- `20-notes`: atomic concept notes and durable synthesis.
- `30-maps`: Maps of Content, outlines, topic hubs, and `.canvas` files.
- `40-projects`: live project dashboards, decisions, orchestration logs, versions, reports, hypotheses, retrospectives.
- `90-meta`: index, log, wiki rules, migration manifests, health reports, lessons, skills registry, source workflow, local rule packs, `.base` files.
- `assets`: local images, media, and raw evidence files. Put source evidence under `assets/sources/`.

Every zone folder should also have a root-level zone index note with the same stem
(`10-sources.md`, `20-notes.md`, etc.). Link to those notes with Obsidian
wikilinks such as `[[10-sources]]`; do not link to folders like
`[10-sources](10-sources/)`, because Obsidian may create an empty note instead
of opening the folder.

## Frontmatter Contract

All wiki notes should start with YAML frontmatter.

Common fields:

```yaml
---
type: source | atomic | map | project | decision | meta
status: inbox | active | draft | stable | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - llm-wiki
aliases: []
---
```

Source note:

```yaml
---
type: source
status: active
source-kind: article-pdf | article-web | book | law | standard | dataset | repository | interview | document | transcript | file | other
source-path: assets/sources/<id>.<ext>
original-url:
doi:
authors: []
year:
title:
venue:
read-status: not-read | reading | read | extracted | reading-meta-only
key-claims-extracted: false
used-in: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - source
---
```

Always prefer a two-layer source model:

- `10-sources/<source-id>.md`: metadata, summary, key claims, provenance, citations, and project use.
- `assets/sources/<source-id>.<ext>`: raw PDF, DOCX, HTML snapshot, transcript, dataset, or other evidence when the wiki owns a local copy.

If the raw file must remain outside the wiki, keep it in place and point `source-path` or `original-url` at it.

Atomic note:

```yaml
---
type: atomic
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_notes: []
tags:
  - note
---
```

Decision note:

```yaml
---
type: decision
status: active
decision_status: proposed | accepted | superseded | rejected
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - decision
---
```

Project note:

```yaml
---
type: project
status: active | planned | blocked | paused | done | archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner:
project-id:
current-stage:
artifacts: []
tags:
  - project
---
```

A project note is a live dashboard, not a historical brief. Keep it synchronized after meaningful work with current status, artifact links, decisions, open questions, and next steps.

Project-as-folder layout for longer work:

```text
40-projects/<project-id>/
  <project-id>.md or index.md   # live dashboard
  <project-id>-orchestration.md # append-only run log; use a unique stem
  versions/                     # immutable snapshots
  reports/                      # check reports and stage outputs
  assets/                       # project-local generated artifacts when useful
```

## Naming

- Use short descriptive file names.
- Prefer kebab-case for generated files.
- Preserve original names when moving user notes if preserving them reduces risk.
- Avoid duplicate stems because `[[Name]]` links become ambiguous.
- Use dates as `YYYY-MM-DD`.

## Linking

- Use `[[Note Name]]` for internal wiki notes.
- Use `[label](relative/path.ext)` for non-note files and files that intentionally remain outside the wiki.
- Link atomic notes back to source notes.
- Link source notes forward to key atomic notes after processing.
- Link every project decision to the project note or map it affects.
- Avoid `[[target|alias]]` inside Markdown tables because the pipe conflicts with table syntax. Use Markdown links inside tables, or put wikilinks outside the table.
- Avoid `../` or `./` inside wikilinks unless the project explicitly uses path-based resolution. Prefer unique note stems; if a stem is ambiguous, rename one file or use a Markdown link.

## Required Meta Files

- `90-meta/index.md`: catalog of pages and maps.
- `90-meta/log.md`: append-only activity log.
- `90-meta/wiki-rules.md`: project-specific maintenance rules.
- `90-meta/lessons-learned.md`: self-learning log that turns repeated failures into rules or skill updates.
- `90-meta/source-workflow.md`: local source evidence and provenance policy.
- `90-meta/skills-registry.md`: local skill and workflow registry when the project has agent skills, scripts, or recurring workflows.
- `90-meta/rule-packs/`: local domain rules, checklists, rubrics, journal requirements, coding standards, or other project-specific policy.
- `90-meta/migration-manifest.md`: latest migration record when migration was performed.

## Bases

Put generated `.base` files under `90-meta/bases/` unless the user prefers another Obsidian convention. Keep formulas simple and quote strings that contain special YAML characters.
