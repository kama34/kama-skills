# Template Directory Format

A template is a directory containing agent definitions and pipeline configuration for a specific presentation type.

## Directory Layout

```
<template-name>/
  ├── template.md              # Metadata: name, description, keywords, format
  ├── pipeline.md              # Agent execution order, loops, stop criteria
  └── agents/
      ├── <generator>.md       # Agent with role: create
      ├── <reviewer>.md        # Agent with role: review
      ├── <fixer>.md           # Agent with role: fix (optional)
      └── <enhancer>.md        # Agent with role: enhance (optional)
```

All three components are required: `template.md`, `pipeline.md`, and at least one agent file in `agents/`.

## template.md — Metadata File

YAML frontmatter followed by optional description text.

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Template identifier. **MUST** be kebab-case (lowercase, hyphens only). |
| `description` | string | What this template is for. Used for auto-selection matching. |
| `keywords` | list | Terms for auto-selection. Include synonyms and related concepts. |

### Optional Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `format` | string | `slidev` | Output format: `slidev`, `universal`, or `custom`. |
| `max_iterations` | integer | `3` | Hard limit on review→fix cycles. One iteration = one pass through (review → fix). |
| `custom_format_description` | string | — | Free-text format instructions for generator agents. **Required** when `format: custom`. |

### Example

```yaml
---
name: investor-pitch
description: "Pitch for investors, seed/series A rounds"
keywords: [investor, pitch, funding, seed, series, startup, VC, fundraising]
format: slidev
max_iterations: 3
---

This template designs presentation structures for startup pitches
targeting seed and series A investors. The reviewer agent evaluates
from the investor's perspective, checking for clear problem/solution
framing, market sizing, and ask clarity.
```

## Storage Locations

Templates are stored in one of two locations:

| Location | Path | Scope |
|----------|------|-------|
| **Local** | `.outline-templates/<name>/` | Project-specific, relative to CWD |
| **Global** | `~/.claude/outline-templates/<name>/` | Available across all projects |

### Lookup Order

When resolving a template by name: **local first, then global**. The first match wins.

### Default Template

The built-in default template is stored at `assets/default/` within the skill directory. It is used when:
- No templates exist in local or global storage
- Auto-selection returns "none" (no template matches the topic)

## Naming Rules

- **MUST** use kebab-case: lowercase letters, numbers, and hyphens only
- No spaces, underscores, or special characters
- Examples: `investor-pitch`, `tech-talk-101`, `quarterly-review`

## Collision Rules

A collision occurs when a template with the **same name** exists in the **same storage location**. A template with the same name in the other location is NOT a collision.

When a collision is detected during `--create-template`:
1. Warn the user
2. Offer three options: **overwrite**, **rename**, or **abort**
