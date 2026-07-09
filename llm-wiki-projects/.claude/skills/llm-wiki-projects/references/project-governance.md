# Project Governance

Use this reference when a wiki is not just a note archive but a working project control surface.

## Live Project Dashboard

A project note is the first page a future agent or human should read. Keep it current after meaningful work.

Minimum dashboard sections:

- goal and scope;
- current status and current stage;
- artifact table with links to the canonical files;
- decisions, append-only or dated;
- open questions;
- next steps that reflect the current state, not the original plan;
- links to sources, maps, and related atomic notes.

If a workflow changes `draft.md`, generated artifacts, reports, or key decisions, sync the dashboard before declaring the project done.

## Project-as-Folder

Use a folder under `40-projects/<project-id>/` when work has multiple stages, generated outputs, or review cycles.

Recommended files:

```text
40-projects/<project-id>/
  <project-id>.md or index.md
  <project-id>-orchestration.md
  versions/
  reports/
  assets/
```

Keep only one active dashboard. Use `versions/` for snapshots and `reports/` for verification output. Prefer unique stems such as `<project-id>-orchestration.md` so stem-based wikilinks stay unambiguous.

## Orchestration Logs

Use `orchestration.md` for long-running or resumable workflows. Append; do not rewrite history.

Each entry should include:

- timestamp;
- stage and iteration;
- pre-state;
- action taken;
- metrics or checks;
- convergence/result;
- post-state;
- decision for the next step.

## Gates and Caps

Use human gates for irreversible, expensive, or judgment-heavy transitions. Use caps for loops so an agent cannot spin indefinitely. When a stage reaches its cap, stop with a clear report and ask for human direction.

## Skills Registry

If a project has local skills, scripts, recurring workflows, or preferred entry points, maintain `90-meta/skills-registry.md`.

Recommended fields per item:

- name;
- status: planned | built | deprecated;
- when to use;
- inputs and outputs;
- files it reads or writes;
- owner or maintenance note;
- related wiki rules or lessons.

The registry should make the default entry point obvious and label component skills as components.
