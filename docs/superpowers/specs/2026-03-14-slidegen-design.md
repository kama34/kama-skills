# Slidegen — AI Image Presentation Generator

**Date:** 2026-03-14
**Status:** Approved

## Overview

Slidegen is a Claude Code skill that generates complete presentations as AI-generated images. Unlike the existing slidev skill (which produces Markdown+CSS code presentations), slidegen uses image generation APIs to create each slide as a standalone image, then assembles them into a PDF.

The skill supports multiple API providers and models through a flexible provider abstraction, with Polza.ai as the default provider.

## Problem Statement

Current slidev skill generates code-based presentations (Slidev framework). For some use cases, AI-generated image slides offer advantages: richer visuals, no need for a dev server, simpler output (PNG+PDF). The skill fills this gap while reusing slidev's proven quality assurance system.

## Architecture

### Three-Phase Generation Pipeline

**Phase 1 — Planning:**
1. Claude receives an outline from the user (topic/structure, same as slidev)
2. Determines a unified presentation style: palette, typography mood, decorative elements, composition approach
3. For each slide generates:
   - Role (cover, section, content, stat, end, etc.)
   - Text content (heading, subheading, bullets, figures)
   - Visual description (style, colors, mood, composition)
   - Final prompt for the image API (English), combining content + visual + typography instructions
4. All prompts saved to `prompts.json`
5. Style parameters encoded as a "style suffix" appended to every prompt for baseline consistency

**Phase 2 — Image Generation:**

Slides are generated **sequentially** (one at a time) in both modes. This is required because reference mode needs the anchor image before generating subsequent slides, and sequential generation allows surfacing progress to the user (e.g., "Generating slide 3/10...").

*Reference mode (default, requires 3+ slides):*
1. Generate slide 1 (cover) — no reference
2. Generate slide 2 — no reference
3. Claude reads both PNGs and selects the **style anchor** using the anchor selection rubric (see below)
4. Slides 3..N generated sequentially, each with the style anchor passed as `images[]` in the API request
5. Style anchor index recorded in `meta.json`
6. Progress reported to user after each slide: "Generated slide N/total"

*No-reference mode (`--no-ref`, or decks with fewer than 3 slides):*
All slides generated independently. Consistency maintained only through the style suffix in prompts. Decks with 1-2 slides automatically use this mode even without `--no-ref`.

**Phase 3 — QA:**
1. Visual review — Claude reads each PNG and evaluates: text readability (size, contrast, not clipped), stylistic consistency with anchor, composition and balance, empty/overcrowded areas
2. Scoring — 6-axis evaluation (adapted from slidev): visual impact, layout uniqueness, typography drama, color conviction, content clarity, decorative quality
3. Regeneration — slides scoring < 6 on any single axis are regenerated with an improved prompt (max 2 retries per slide). This is a deliberate departure from slidev's average-based threshold: since image slides cannot be surgically fixed (unlike CSS), the per-axis gate catches any dimension of failure early.
4. PDF assembly — final PNGs assembled into PDF (see Dependencies section for tooling)

### Style Anchor Selection

The style anchor is the slide that serves as the visual reference for all subsequent slides.

**Selection rubric — Claude scores slides 1 and 2 on these criteria (1-5 each):**

| Criterion | Description |
|---|---|
| Layout density | Has multiple content elements (heading, body, accents) — not just a single centered title |
| Background complexity | Background represents the intended visual style (gradients, textures, patterns) |
| Decorative elements | Contains representative decorative details (lines, shapes, icons, overlays) |
| Typography variety | Shows both heading and body text styles, demonstrating the font hierarchy |

The slide with the higher total score becomes the anchor. On tie — slide 2 wins (cover slides are more likely to be atypical).

**Minimum deck size:** Reference mode requires 3+ slides. Decks with 1-2 slides automatically fall back to no-reference mode.

The anchor is stored in `meta.json` and reused by `--edit` and `--polish` commands.

## Project Structure

### Skill Files (tracked by git)

```
slidegen/
  .gitignore                              # Allowlist pattern (same as slidev)
  README.md
  .claude/
    skills/
      slidegen/
        SKILL.md                          # Entry point — full procedure
        references/
          providers.md                    # Provider configs (endpoints, request formats, auth)
          image-prompt-guide.md           # How to compose effective prompts for image gen models
          scoring-subroutine.md           # 6-axis scoring adapted from slidev
          content-review-subroutine.md    # Content quality checks (from slidev)
          polish-procedure.md             # --polish iterative improvement cycle
          ab-testing.md                   # A/B variant generation for weak slides
          design-memory.md               # Read/write protocol for design pattern memory
          compare-procedure.md            # --compare side-by-side scoring
          notes-procedure.md              # --notes speaker notes generation
          preset-format.md                # Prompt-template preset specification
        assets/
          demo-outline.md                 # Demo outline for --create-preset
```

### Generated Output Structure

```
my-presentation/
  slides/
    slide-01.png
    slide-02.png
    ...
  slides.pdf
  prompts.json       # Saved prompts (for --edit, regeneration)
  meta.json           # Provider, model, mode, style anchor index
```

`prompts.json` enables `--edit` and `--polish` to modify existing prompts rather than generating from scratch.

`meta.json` example:
```json
{
  "provider": "polza",
  "model": "google/gemini-3.1-flash-image-preview",
  "mode": "reference",
  "style_anchor": 2,
  "aspect_ratio": "16:9",
  "created": "2026-03-14T12:00:00Z",
  "slide_count": 10
}
```

## Provider Abstraction

### Default Provider: Polza.ai

- Endpoint: `POST https://polza.ai/api/v1/media`
- Auth: `Authorization: Bearer $POLZA_API_KEY`
- Default model: `google/gemini-3.1-flash-image-preview`

### Universal Request Format

```json
{
  "model": "<model-id>",
  "input": {
    "prompt": "<slide prompt>",
    "aspect_ratio": "16:9",
    "images": [
      { "type": "base64", "data": "<style anchor slide>" }
    ]
  }
}
```

### Provider Resolution

1. `--provider=polza --model=...` — explicit flags
2. No flags — Polza + default model
3. `--provider=openai` — redirects to `POST /v1/images/generations` (different request format)
4. `--provider=custom --base-url=... --model=...` — arbitrary OpenAI-compatible endpoint

### API Key Resolution

Environment variable by provider name:
- Polza → `POLZA_API_KEY`
- OpenAI → `OPENAI_API_KEY`
- Custom → `CUSTOM_API_KEY` (or override with `--api-key-env=MY_VAR`)

If the key is not found, the skill prints an error with instructions on how to set it.

### Async Response Handling

Polza may return `status: "pending"` for long-running generations. Handling:

1. Poll `GET {provider_base_url}/v1/media/{id}` every 5 seconds (for Polza: `https://polza.ai/api/v1/media/{id}`)
2. Per-slide timeout: 120 seconds (image generation can take 30-90 seconds)
3. On timeout: print warning with slide number, skip the slide, continue generating remaining slides
4. At the end: report all skipped slides and suggest re-running with `--edit` to regenerate them
5. On rate limit (429): exponential backoff — wait 5s, 10s, 20s (max 3 retries per slide)

## Preset System

### Preset Format (`<name>.preset.md`)

```yaml
---
name: corporate-dark
description: Dark corporate theme
mood: professional, clean
palette: "dark background (#1a1a2e), white text, blue accent (#0066ff)"
typography: "modern sans-serif, large headings, minimal text"
decoration: "subtle gradient overlays, thin line separators"
aspect_ratio: "16:9"
---

Generate a presentation slide with dark navy background (#1a1a2e).
Use clean modern sans-serif typography, white text for headings,
light gray for body text. Blue (#0066ff) accent for highlights
and decorative elements. Subtle gradient overlays.
{{SLIDE_CONTENT}}
{{SLIDE_ROLE}}
```

`{{SLIDE_CONTENT}}` and `{{SLIDE_ROLE}}` are placeholders replaced during generation.

**`{{SLIDE_ROLE}}` valid values and substitution text:**
- `cover` → "This is a cover/title slide — prominent title, minimal body text"
- `section` → "This is a section divider slide — section heading, transitional"
- `content` → "This is a content slide — heading with body text, bullets, or key points"
- `stat` → "This is a statistics/data slide — large numbers, charts, or key metrics"
- `quote` → "This is a quote slide — prominent quotation with attribution"
- `comparison` → "This is a comparison slide — two or more items side by side"
- `end` → "This is a closing/thank-you slide — call to action or contact info"

### Storage

- Global: `~/.claude/slidegen-presets/`
- Local: `./.slidegen-presets/`
- Lookup order: local → global

### `--create-preset <name>` Wizard

7 questions asked one at a time:
1. Mood (professional, playful, dramatic, calm, futuristic, elegant, bold)
2. Color scheme (dark, light, deep navy, warm cream...)
3. Accent color
4. Typography personality (geometric & modern, classic & refined, rounded & friendly, sharp & technical)
5. Content density (minimal, balanced, information-dense)
6. Background textures (gradient mesh, geometric patterns, clean flat, frosted glass, noise)
7. Save location (global / local)

After answers: synthesize prompt template → save `.preset.md` → generate demo presentation from `assets/demo-outline.md` → run QA → print score report. If overall average score < 7, print a warning advising the user to refine the preset. Do not block — let the user decide.

## Subcommands (Flags)

### From slidev (adapted)

| Flag | Behavior |
|---|---|
| `--help` | Display usage table and stop |
| `--preset <name>` | Generate using a prompt-template preset |
| `style: <desc>` | Generate with a custom style description |
| `--edit [dir] <comment>` | Edit procedure: (1) load `prompts.json` + `meta.json`, (2) list all slides with their roles and prompt summaries, (3) Claude identifies which slides the comment applies to — if ambiguous, ask user to confirm slide numbers, (4) modify affected prompts, (5) regenerate only those slides with style anchor as reference, (6) run QA on regenerated slides, (7) reassemble PDF |
| `--polish=N [dir]` | N cycles (default 3, max 5): score → regenerate weak slides (per-axis score < 6, same threshold as QA) with improved prompts → A/B test (2 variants, pick best) → reassemble PDF → re-score |
| `--compare <dir1> <dir2>` | Score both presentations, side-by-side report |
| `--notes [dir]` | Generate speaker notes in `notes.md`: Opening, Key message, Details, Transition per slide |
| `--learn=N` | Self-improving loop (N iterations, default 3, max 10): generate → score → analyze errors → adjust prompt approach → regenerate. After each iteration, write findings to design memory using the write protocol (see Design Memory section) |
| `--create-preset <name>` | Preset creation wizard (see Preset System section) |
| `--export pdf [dir]` | Validate all PNGs exist and have consistent dimensions, then reassemble PDF. If any are missing or mismatched, report which files are problematic |

### New flags

| Flag | Behavior |
|---|---|
| `--provider <name>` | Select API provider (polza, openai, custom) |
| `--model <id>` | Select model |
| `--no-ref` | Generate without reference images (no style anchor) |
| `--base-url <url>` | Endpoint for custom provider |
| `--api-key-env <VAR>` | Environment variable name for the API key |

### Not applicable (from slidev)

| Slidev flag | Why not applicable |
|---|---|
| `--dev [dir]` | No dev server — output is static images |
| `--responsive [dir]` | Aspect ratio set at generation time |
| `--picture` | The slides themselves are images |
| `--theme` | No Slidev themes — use `--preset` or `style:` instead |

## QA and Scoring

### Scoring (6 axes, 1-10)

| Axis | What is evaluated |
|---|---|
| Visual Impact | Overall impression, attractiveness, "wow" factor |
| Layout Uniqueness | Variety of compositions across slides (not all identical) |
| Typography Drama | Readability, text hierarchy, font contrast |
| Color Conviction | Palette consistency, confident use of color |
| Content Clarity | Text readable, not overloaded, key message understood in 3 seconds |
| Decorative Quality | Backgrounds, accents, decorative elements — appropriate, not distracting |

**Regeneration threshold:** score < 6 on any single axis (per-axis gate, not average). This is stricter than slidev's average-based approach because image slides cannot be partially fixed — a full regeneration is needed.

**Score band definitions:**
- **1-3 (Low):** Fundamentally broken — unreadable text, clashing colors, empty/broken layout
- **4-5 (Below threshold):** Noticeable problems — poor contrast, inconsistent style, cluttered composition
- **6-7 (Acceptable):** Functional — readable, consistent, but not impressive
- **8-9 (Good):** Polished — strong visual impact, clear hierarchy, cohesive style
- **10 (Exceptional):** Outstanding — could be used as a design reference

### Content Review (from slidev)

- 3-second test — is the slide's essence understood instantly?
- Narrative flow — logical transitions between slides?
- Redundancy — no content duplication?
- CTA clarity — clear call to action (if present)?
- Information hierarchy — key points emphasized?

### Design Memory (`~/.claude/slidegen-design-memory.json`)

- Read before every generation to inform prompt construction
- Written after every generation that completes QA scoring

**JSON schema:**
```json
{
  "entries": [
    {
      "date": "2026-03-14",
      "topic": "AI in Healthcare",
      "type": "success | neutral | failure",
      "overall_score": 8.2,
      "provider": "polza",
      "model": "google/gemini-3.1-flash-image-preview",
      "aspect_ratio": "16:9",
      "style_suffix": "Dark gradient background, geometric accents...",
      "mood": "professional",
      "palette_description": "deep navy + electric blue accent",
      "prompt_patterns": ["Include explicit font size instructions", "Specify text alignment per element"],
      "what_worked": "Detailed typography instructions produced consistent readable text",
      "what_failed": "Vague color descriptions led to inconsistent palettes across slides"
    }
  ]
}
```

**Write protocol:** After scoring:
- Average score >= 7: write a `success` entry (aligns with `--create-preset` quality threshold)
- Average score 5-6: write a `neutral` entry (type: `"neutral"`) — useful for tracking trends
- Average score < 5: write a `failure` entry
- `--learn` writes an entry after every iteration regardless of score

### Difference from slidev QA

No CSS code review phase (no CSS). Instead: prompt review before sending — is the prompt detailed enough, does it contain the style suffix, are there contradictions?

## Directory Auto-Detection

Several commands accept an optional `[dir]` argument. When omitted, the skill auto-detects:

1. Look for `prompts.json` in the current working directory
2. If not found, scan one level deep for the most recently modified subdirectory containing `prompts.json`
3. If multiple found, list them and ask the user to pick
4. If none found, print error: "No slidegen project found. Run `/slidegen <outline>` to create one."

## Dependencies

- **Python 3** — required for PDF assembly
- **Pillow** (`pip install Pillow`) — PNG-to-PDF conversion
- **curl** — API calls (available on all platforms)

If Pillow is not installed, the skill runs `pip install Pillow` automatically before PDF assembly. If Python is not available, the skill prints an error with installation instructions and outputs only PNG files (no PDF).

## Error Handling

- **API key missing:** Print error with instructions for the specific provider
- **API rate limit (429):** Wait and retry with exponential backoff (max 3 retries)
- **Generation timeout:** Print warning, skip slide, continue with remaining slides, report skipped slides at the end
- **Model not available:** Print error suggesting alternative models for the provider
- **Invalid provider:** Print list of supported providers

## Success Criteria

1. A user can run `/slidegen <outline>` and get a complete PNG+PDF presentation
2. Style is consistent across slides (reference mode)
3. Text on slides is readable and properly formatted
4. The scoring system catches and regenerates low-quality slides
5. Different providers/models work through the same interface
6. Presets produce reproducible style directions
