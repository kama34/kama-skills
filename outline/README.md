# Outline — Presentation Structure Generator

Author: Kamyshnikov Dmitry — more at: https://t.me/typicalinnopolisyanin

## What is this?

Outline is a meta-skill for Claude Code that creates **agent pipelines** to iteratively develop presentation structures. Instead of using a fixed template, it designs specialized agents (generator, reviewer, fixer, etc.) tailored to your specific presentation type and audience.

## How it works

Each "template" is actually a set of agents that work together in a cycle:

1. **Generator** creates the initial structure
2. **Reviewer** evaluates it from the audience's perspective (e.g., as an investor, a student, a colleague)
3. **Fixer** revises the structure based on feedback
4. Cycle repeats until the reviewer approves or the iteration limit is reached
5. **Optional agents** run after the main cycle (e.g., Q&A question generator)

## Commands

```
/outline <topic>                              Generate structure (auto-select template)
/outline --template <name> <topic>            Use a specific template
/outline --format <slidev|universal|custom>   Override output format
/outline --create-template                    Create new agent pipeline template
/outline --learn=N [template]                 Train agents with N test runs
/outline --help                               Show usage help
```

## Output formats

- **slidev** (default) — `## Slide N: Title` + bullets, directly compatible with `/slidev`
- **universal** — sections, theses, speaker notes — tool-agnostic
- **custom** — format defined by the template itself

## Templates

Templates are stored as directories with agent prompts:

```
<template-name>/
  ├── template.md       # Metadata: name, description, keywords, format
  ├── pipeline.md       # Agent execution order, loops, stop criteria
  └── agents/
      ├── generator.md
      ├── reviewer.md
      ├── fixer.md
      └── ...
```

Storage locations:
- **Local:** `.outline-templates/<name>/` (project-specific)
- **Global:** `~/.claude/outline-templates/<name>/` (available everywhere)

## Creating templates

Run `/outline --create-template` — Claude Code will ask you a few questions (name, description, audience, format) and then **autonomously design the agent pipeline**: decide how many agents are needed, write their prompts, and set up the execution order.

## Training agents

Run `/outline --learn=N [template]` to improve agent prompts. The skill generates N test topics, runs the pipeline, and a critic agent analyzes the results and proposes prompt improvements.

## Contributing

This skill is open for experimentation and improvement. Ideas:
- Create new templates for specific presentation types
- Improve the default agents
- Add new output formats
- Enhance the `--learn` critic

If you improve something, please share the result!

## Spec

Full design spec: [docs/superpowers/specs/2026-03-11-outline-skill-design.md](../../docs/superpowers/specs/2026-03-11-outline-skill-design.md)
