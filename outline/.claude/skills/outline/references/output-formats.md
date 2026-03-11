# Output Formats

Outline supports three output formats for generated presentation structures.

## Format Precedence

**`--format` flag > template's `format` field > default (`slidev`)**

The `--format` command-line flag always wins. If not specified, the template's `format` field is used. If the template has no format field, `slidev` is the default.

## Format: `slidev`

Slide-based format compatible with the `/slidev` skill. Each slide is a heading with bullet points.

### Structure

```markdown
## Slide 1: Title Slide
- Main title of the presentation
- Subtitle or tagline
- Speaker name / date

## Slide 2: Problem Statement
- Key pain point
- Statistics or evidence
- Why this matters now

## Slide 3: Solution Overview
- Core solution description
- Key differentiator
- How it addresses the problem
```

### Rules
- Use `## Slide N: Title` format for each slide
- Bullets describe the content/talking points for each slide
- 8-12 slides is the typical range
- Directly compatible with `/slidev` — output can be fed into the slidev skill as an outline

## Format: `universal`

Tool-agnostic format with sections, theses, and speaker notes. Suitable for any presentation tool.

### Structure

```markdown
# Presentation Title

## Section 1: Introduction

**Thesis:** Establish the problem and why the audience should care.

Key points:
- Opening hook or question
- Context and background
- Stakes — what happens if we don't act

> Speaker notes: Open with the statistic about X. Pause after the question to let it sink in. This section should take ~2 minutes.

## Section 2: Current Landscape

**Thesis:** Show the current state and its limitations.

Key points:
- Current approaches
- Their shortcomings
- Gap in the market / knowledge

> Speaker notes: Use the comparison chart here. Reference competitor Y specifically.
```

### Rules
- Use `## Section N: Title` for each section
- Each section has a **Thesis** statement (one sentence summarizing the section's purpose)
- Key points as bullet lists
- Speaker notes in blockquotes (`>`)
- No fixed slide count — sections map to logical units, not necessarily individual slides

## Format: `custom`

Template-defined format. The format is described by the `custom_format_description` field in `template.md`.

### How It Works

1. The template author writes a `custom_format_description` in `template.md`
2. This description is injected into the `{{output_format}}` variable
3. Generator agents use it to structure their output accordingly

### Example template.md

```yaml
---
name: workshop-plan
description: "Interactive workshop session plan"
keywords: [workshop, training, interactive, hands-on]
format: custom
custom_format_description: |
  Structure as a timed workshop agenda:
  - Each segment has: title, duration (minutes), format (lecture/exercise/discussion), content points
  - Include transition notes between segments
  - Mark interactive segments with [INTERACTIVE]
  - Total duration should be specified at the top
---
```

### Example output

```markdown
# Workshop: Introduction to API Design
**Total duration: 90 minutes**

## Segment 1: Welcome & Context (10 min) [lecture]
- Introductions
- Workshop objectives
- What we'll build today

> Transition: "Now that we know what we're building, let's look at the principles..."

## Segment 2: REST Principles (15 min) [lecture]
- Resource-oriented design
- HTTP methods and status codes
- Naming conventions

## Segment 3: Design Your First Endpoint (20 min) [INTERACTIVE]
- Exercise: design an endpoint for a given scenario
- Pair review
- Group discussion of approaches
```

## How `{{output_format}}` Is Constructed

The orchestrator builds the `{{output_format}}` variable based on the active format:

| Format | `{{output_format}}` content |
|--------|---------------------------|
| `slidev` | `"Используй формат slidev-аутлайна: ## Slide N: Заголовок, затем буллиты. Целься на 8-12 слайдов. Весь контент на русском языке."` |
| `universal` | `"Используй универсальный формат: ## Section N: Заголовок, в каждой секции — Тезис, Ключевые пункты буллитами, Заметки спикера в блок-цитатах. Весь контент на русском языке."` |
| `custom` | The literal `custom_format_description` text from `template.md` |
