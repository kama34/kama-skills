# Workflows

Use this reference when carrying out an end-to-end task with the skill.

## Create a New Project Wiki

1. Run `audit_project.py` to detect whether the folder is empty, code-oriented, or knowledge-oriented.
2. Run `migrate_project.py` to create the layout, index, log, wiki rules, governance meta files, source workflow, project dashboard, orchestration log, Bases, and Canvas.
3. Keep the generated project note as a live dashboard when the user has provided a real goal, sources, or constraints.
4. Run `validate_wiki.py`.
5. Report the wiki root, created files, and validation result.

## Migrate an Existing Project

1. Run `audit_project.py`.
2. Read `references/schemas.md` if folder choice or frontmatter policy is unclear.
3. Run `migrate_project.py`.
4. Inspect `90-meta/migration-manifest.md`.
5. Run `validate_wiki.py --write-report`.
6. Fix validation errors if the task asks for implementation, then re-run validation.

## Ingest a Source

1. Create one source wrapper in `10-sources/<source-id>.md`.
2. Put raw evidence in `assets/sources/<source-id>.<ext>` when a local copy is allowed.
3. Fill provenance fields: original URL/path, authors, year, title, venue, and read status.
4. Extract key claims, definitions, examples, contradictions, methods, limitations, and reusable concepts.
5. Promote durable ideas into `20-notes` as atomic notes.
6. Link the source to projects via `used-in` and a project note section.
7. Update relevant maps, `90-meta/index.md`, and `90-meta/log.md`.
8. Validate links.

Read `references/source-lifecycle.md` when source evidence, deep reading, citation provenance, or raw-file placement matters.

## Distill Chat or Work Into Wiki

At the end of meaningful work, ask whether the result should persist. Persist it when it includes:

- a decision that affects future work;
- project architecture or setup knowledge;
- a reusable explanation, comparison, or synthesis;
- a source interpretation;
- a task outcome future agents should know.

Use `40-projects` for project state and decisions, `20-notes` for reusable ideas, and `30-maps` for navigation.

## Run or Maintain a Project

1. Read the project dashboard first.
2. If the work spans multiple stages, keep an append-only `orchestration.md`.
3. Snapshot important states into `versions/` before risky edits.
4. Save check outputs in `reports/`.
5. Use human gates for irreversible, expensive, or judgment-heavy transitions.
6. After each meaningful change, sync the dashboard: status, artifacts, decisions, open questions, next steps.

Read `references/project-governance.md` for project-as-folder, stage caps, human gates, resume, and skills-registry patterns.

## Promote a Lesson

1. When a user notices a wiki/process failure, append it to `90-meta/lessons-learned.md`.
2. Capture context, what went wrong, root cause, fix, and promotion trigger.
3. If the failure is likely to recur, promote it into `90-meta/wiki-rules.md`, a validator check, a template, or a local skill.
4. Update `90-meta/log.md` and validate.

Read `references/self-learning.md` for the full loop.

## Add a Local Rule Pack

Use `90-meta/rule-packs/` for domain-specific rules that should travel with the project rather than the global skill: journal requirements, style rubrics, compliance rules, coding standards, review checklists, or evaluation criteria.

1. Create a focused rule-pack note under `90-meta/rule-packs/`.
2. State when to load it and which workflows depend on it.
3. Prefer checklists or YAML-like tables when rules are mechanically checkable.
4. Link the rule pack from `90-meta/index.md`, relevant project dashboards, and `90-meta/skills-registry.md` if local skills use it.
5. Promote recurring mistakes from `lessons-learned` into the relevant rule pack.

## Query the Wiki

1. Read `90-meta/index.md` first.
2. Follow relevant maps and notes.
3. Use source notes when citations or exact provenance matters.
4. If the answer produces reusable synthesis, file it as a note and update the log.

## Health Check

Run `validate_wiki.py --write-report` and then look for:

- broken or ambiguous wikilinks;
- missing frontmatter;
- relative wikilinks and wikilinks with aliases inside Markdown tables;
- unbalanced wikilink brackets;
- orphan atomic notes;
- source notes with `read-status: not-read` or `key-claims-extracted: false`;
- maps that do not link to important notes;
- stale claims or unresolved contradictions;
- useful notes still trapped in `00-inbox`.

When validating a repository that has local agent tooling, ignore tool directories such as `.agents`, `.claude`, `.codex`, `scripts`, `versions`, and `reports` unless the user explicitly wants those files treated as wiki notes.

## Maintenance Style

Prefer small incremental edits. Keep raw sources stable, wiki pages current, and project rules explicit. Do not let the wiki become a dumping ground; every page should either preserve source provenance, explain a reusable idea, organize a topic, or record project state.
