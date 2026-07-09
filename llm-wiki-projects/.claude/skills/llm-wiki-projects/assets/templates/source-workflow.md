---
type: meta
status: active
created: {{date}}
updated: {{date}}
language: {{language}}
tags:
  - llm-wiki/sources
---

# Source Workflow

Every durable source gets a markdown wrapper in `10-sources/`. Raw evidence lives in `assets/sources/` when a local copy is allowed.

## Two-Layer Model

```text
10-sources/<source-id>.md
assets/sources/<source-id>.<ext>
```

## Source ID Rules

- Papers/books: `<lastname>-<year>-<slug>`
- Laws/standards: `<type>-<number>-<year>-<slug>`
- Repositories: `<repo-name>-repo`
- Interviews/transcripts: `interview-<person>-<date>`
- Web pages without authors: `<domain>-<slug>-<year>`

## Workflow

1. Create or update the source wrapper.
2. Save raw evidence under `assets/sources/` when possible.
3. Fill provenance fields.
4. Extract key claims only from inspected material.
5. Promote reusable ideas into `20-notes/`.
6. Link the source to project dashboards through `used-in`.
7. Update maps, index, and log.
8. Validate.
