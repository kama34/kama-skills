# SlideCraft Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a standalone Claude Code skill that generates two-layer presentations — AI-generated visual backgrounds (text-free) + Slidev HTML/CSS text overlay.

**Architecture:** SlideCraft is a self-contained skill at `slidecraft/.claude/skills/slidecraft/`. It adapts reference files from slidegen and slidev but operates independently. The pipeline is: outline → layout-plan.json (zone coordinates) → text-free image prompts → AI image generation → Slidev project assembly with CSS absolute positioning → dual-phase QA → export.

**Tech Stack:** Slidev (markdown-based presentation framework), Polza.ai / OpenAI (image generation APIs), Python Pillow (PDF assembly), Playwright Chromium (PNG/PDF export)

**Design spec:** `docs/superpowers/specs/2026-03-14-slidecraft-design.md`

**Source skills for reference:**
- slidegen: `slidegen/.claude/skills/slidegen/`
- slidev: `slidev/.claude/skills/slidev/`

---

## File Map

### Files to CREATE (new):

| File | Responsibility |
|------|---------------|
| `slidecraft/.gitignore` | Allowlist pattern — only `.claude/` tracked |
| `slidecraft/README.md` | Skill test area docs |
| `slidecraft/.claude/skills/slidecraft/SKILL.md` | Main entry point — full procedure |
| `slidecraft/.claude/skills/slidecraft/assets/demo-outline.md` | Demo outline for --learn / --create-preset |
| `slidecraft/.claude/skills/slidecraft/references/layout-plan-format.md` | NEW: layout-plan.json spec, zone types, coordinate-to-CSS mapping |
| `slidecraft/.claude/skills/slidecraft/references/text-overlay-rules.md` | NEW: CSS positioning rules for text over AI images |

### Files to COPY and ADAPT:

| File | Source | Key adaptations |
|------|--------|----------------|
| `references/providers.md` | `slidegen/references/providers.md` | Copy verbatim — same API providers |
| `references/image-prompt-guide.md` | `slidegen/references/image-prompt-guide.md` | Replace text-in-image rules with text-free zone rules |
| `references/scoring-subroutine.md` | `slidegen/references/scoring-subroutine.md` | Replace 6 axes with slidecraft axes (add Layout precision, Layer harmony) |
| `references/content-review-subroutine.md` | `slidegen/references/content-review-subroutine.md` | Copy verbatim — same content quality checks |
| `references/polish-procedure.md` | `slidegen/references/polish-procedure.md` | Add dual-layer remediation table per axis |
| `references/ab-testing.md` | `slidegen/references/ab-testing.md` | Adapt for two-layer A/B (image variants vs text variants) |
| `references/design-memory.md` | `slidegen/references/design-memory.md` | Extend entry format with visual + text sub-objects, max 50 |
| `references/compare-procedure.md` | `slidegen/references/compare-procedure.md` | Score on slidecraft 6 axes, composite comparison |
| `references/notes-procedure.md` | `slidegen/references/notes-procedure.md` | Copy verbatim — same speaker notes format |
| `references/preset-format.md` | `slidev/references/preset-format.md` | Add zone_strategy, text_color, text_contrast_mode fields |
| `references/design-principles.md` | `slidev/references/design-principles.md` | Copy verbatim — same 12 principles apply |
| `references/layout-css-patterns.md` | `slidev/references/layout-css-patterns.md` | Adapt for layout:none + absolute positioning paradigm |
| `references/slidev-syntax.md` | `slidev/references/slidev-syntax.md` | Copy verbatim |
| `references/slidev-layouts.md` | `slidev/references/slidev-layouts.md` | Copy verbatim (reference only — slidecraft uses layout:none) |
| `references/slidev-animations.md` | `slidev/references/slidev-animations.md` | Copy verbatim |
| `references/responsive-check.md` | `slidev/references/responsive-check.md` | Adapt for zone-based layout (check zone overflow at 4:3) |

---

## Chunk 1: Scaffold & Infrastructure

### Task 1: Create directory structure and scaffold files

**Files:**
- Create: `slidecraft/.gitignore`
- Create: `slidecraft/README.md`
- Create: `slidecraft/.claude/skills/slidecraft/assets/demo-outline.md`

- [ ] **Step 1: Create the directory structure**

```bash
mkdir -p slidecraft/.claude/skills/slidecraft/assets
mkdir -p slidecraft/.claude/skills/slidecraft/references
```

- [ ] **Step 2: Write .gitignore (allowlist pattern)**

Copy from `slidev/.gitignore` — same allowlist pattern that only tracks `.claude/` contents:

```gitignore
# Ignore everything
*

# But not these files...
!.gitignore
!README.md

# Track the skill
!.claude/
!.claude/**
```

- [ ] **Step 3: Write README.md**

```markdown
# SlideCraft

Two-layer presentation generator: AI-generated visuals + Slidev text overlay.

## Usage

```
/slidecraft <outline or file>
/slidecraft --help
```

## Test Area

This directory is a playground for testing slidecraft output. Only `.claude/` contents are tracked by git.
```

- [ ] **Step 4: Write demo-outline.md**

Copy from `slidegen/.claude/skills/slidegen/assets/demo-outline.md` — same 5-slide demo outline used by `--learn` and `--create-preset`. Read the file at `slidegen/.claude/skills/slidegen/assets/demo-outline.md` and copy it verbatim.

**Verify:** The copied demo-outline.md must have ≥3 slides (required for reference mode) and include varied roles (cover, content, stat, end) to exercise the full pipeline during `--learn` and `--create-preset`.

- [ ] **Step 5: Commit scaffold**

```bash
git add slidecraft/.gitignore slidecraft/README.md slidecraft/.claude/
git commit -m "feat(slidecraft): scaffold directory structure and assets"
```

---

## Chunk 2: Verbatim Reference Files

Copy reference files that need no adaptation from source skills.

### Task 2: Copy verbatim reference files

**Files:**
- Create: `slidecraft/.claude/skills/slidecraft/references/providers.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/content-review-subroutine.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/notes-procedure.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/design-principles.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/slidev-syntax.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/slidev-layouts.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/slidev-animations.md`

- [ ] **Step 1: Copy each file**

For each file listed above, read the source file and write it verbatim to the slidecraft references directory:

| Target | Source |
|--------|--------|
| `references/providers.md` | `slidegen/.claude/skills/slidegen/references/providers.md` |
| `references/content-review-subroutine.md` | `slidegen/.claude/skills/slidegen/references/content-review-subroutine.md` |
| `references/notes-procedure.md` | `slidegen/.claude/skills/slidegen/references/notes-procedure.md` |
| `references/design-principles.md` | `slidev/.claude/skills/slidev/references/design-principles.md` |
| `references/slidev-syntax.md` | `slidev/.claude/skills/slidev/references/slidev-syntax.md` |
| `references/slidev-layouts.md` | `slidev/.claude/skills/slidev/references/slidev-layouts.md` |
| `references/slidev-animations.md` | `slidev/.claude/skills/slidev/references/slidev-animations.md` |

Read each source file completely and write it to the target path without modifications.

- [ ] **Step 2: Commit verbatim references**

```bash
git add slidecraft/.claude/skills/slidecraft/references/providers.md \
       slidecraft/.claude/skills/slidecraft/references/content-review-subroutine.md \
       slidecraft/.claude/skills/slidecraft/references/notes-procedure.md \
       slidecraft/.claude/skills/slidecraft/references/design-principles.md \
       slidecraft/.claude/skills/slidecraft/references/slidev-syntax.md \
       slidecraft/.claude/skills/slidecraft/references/slidev-layouts.md \
       slidecraft/.claude/skills/slidecraft/references/slidev-animations.md
git commit -m "feat(slidecraft): add verbatim reference files from slidegen/slidev"
```

---

## Chunk 3: NEW Reference Files

Create the two entirely new reference files that don't exist in either source skill.

### Task 3: Write layout-plan-format.md

**Files:**
- Create: `slidecraft/.claude/skills/slidecraft/references/layout-plan-format.md`

- [ ] **Step 1: Write the file**

This is a NEW reference file. Write it with the following content structure:

```markdown
# Layout Plan Format

The layout plan (`layout-plan.json`) is the coordination layer between AI image generation and Slidev text overlay. It defines where text zones are placed on each slide.

## JSON Schema

```json
{
  "slides": [
    {
      "slide": <number>,
      "role": "<cover|section|content|stat|quote|comparison|end>",
      "zones": [ <zone objects> ],
      "visual_description": "<English description of visual elements>",
      "prompt_hint": "<auto-generated empty-zone instructions for AI>"
    }
  ]
}
```

## Zone Object

```json
{
  "id": "<unique identifier within slide>",
  "type": "<heading|subheading|list|body|stat|quote|cta|caption>",
  "text": "<string or null>",
  "items": ["<array of strings — for list type only>"],
  "position": {
    "x": "<left edge, percentage>",
    "y": "<top edge, percentage>",
    "w": "<width, percentage>",
    "h": "<height, percentage>"
  },
  "style": {
    "fontSize": "<CSS em value>",
    "fontWeight": "<normal|bold>",
    "color": "<CSS color>",
    "textAlign": "<left|center|right>",
    "lineHeight": "<CSS value, optional>"
  }
}
```

## Coordinate-to-CSS Mapping

Layout plan positions map directly to CSS `position: absolute`:

| layout-plan.json | CSS property |
|------------------|-------------|
| `x` | `left` |
| `y` | `top` |
| `w` | `width` |
| `h` | `height` |

## Zone Types

| Type | Usage | Typical position |
|------|-------|-----------------|
| `heading` | Main slide title | Top area, 40-80% width |
| `subheading` | Secondary title | Below heading, 50-70% width |
| `list` | Bullet points | Left or center, 50-65% width |
| `body` | Paragraph text | Center or left, 50-70% width |
| `stat` | Large number/metric | Center, 30-50% width |
| `quote` | Quotation text | Center, 60-80% width |
| `cta` | Call to action | Bottom center, 50-70% width |
| `caption` | Small annotation | Bottom edge, 30-50% width |

## prompt_hint Generation

For each zone, convert coordinates to an English instruction:

Template:
```
"Leave the area from [x] to [x+w] horizontally, [y] to [y+h] vertically completely empty —
no text, no decorative elements. Background must be uniform [dark|light] in this region."
```

- Multiple zones are listed sequentially in prompt_hint
- `[dark|light]` is derived from planned text color: white/light text → zone must be dark, dark text → zone must be light
- Add at the end: "Place all decorative elements, icons, and visual details ONLY in the remaining areas outside these zones."

## Zone Strategy Presets

Default zone placement templates that can be specified in presets or per-slide:

| Strategy | Description | Typical zones |
|----------|-------------|---------------|
| `text-left-60` | Text in left 60%, visuals in right 35% | heading at (5%, 8%, 55%, 12%), bullets at (5%, 28%, 55%, 55%) |
| `text-right-60` | Mirror of text-left-60 | heading at (40%, 8%, 55%, 12%), bullets at (40%, 28%, 55%, 55%) |
| `text-center` | Centered text, visuals on edges | heading at (15%, 30%, 70%, 15%), body at (20%, 50%, 60%, 30%) |
| `text-bottom-40` | Visual top 55%, text bottom 40% | heading at (5%, 58%, 90%, 12%), body at (5%, 72%, 90%, 25%) |
| `text-split-50-50` | Left and right halves | left zones at (3%, y, 44%, h), right zones at (53%, y, 44%, h) |

## Per-Role Default Layouts

When no zone_strategy is specified, use these defaults per slide role:

| Role | Default strategy | Notes |
|------|-----------------|-------|
| `cover` | `text-center` | Title and subtitle centered |
| `section` | `text-center` | Section heading centered |
| `content` | `text-left-60` | Content with visual accent right |
| `stat` | `text-center` | Large number centered |
| `quote` | `text-center` | Quote centered with attribution |
| `comparison` | `text-split-50-50` | Two items side by side |
| `end` | `text-center` | CTA centered |
```

- [ ] **Step 2: Commit**

```bash
git add slidecraft/.claude/skills/slidecraft/references/layout-plan-format.md
git commit -m "feat(slidecraft): add layout-plan-format.md reference"
```

### Task 4: Write text-overlay-rules.md

**Files:**
- Create: `slidecraft/.claude/skills/slidecraft/references/text-overlay-rules.md`

- [ ] **Step 1: Write the file**

This is a NEW reference file. Write it with the following content structure:

```markdown
# Text Overlay Rules

Rules for positioning HTML/CSS text over AI-generated background images in Slidev.

## Core Architecture

Every slide uses `layout: none` to bypass all Slidev theme CSS. The slide consists of two layers:

1. **Background layer** (z-index: 0) — AI-generated PNG as `background-image`
2. **Text layer** (z-index: 1) — HTML elements with CSS `position: absolute`

## Slide Container Pattern

```html
<div class="slide-container">
  <div class="slide-bg slide-NN"></div>
  <div class="zone zone-<id>" style="left:X%;top:Y%;width:W%;height:H%;">
    <!-- text content -->
  </div>
</div>
```

## Required CSS Classes

```css
.slide-container {
  position: absolute;
  inset: 0;
}

.slide-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  z-index: 0;
}

.zone {
  position: absolute;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
```

## Why layout: none

Slidev's built-in layouts (`cover`, `default`, `section`, etc.) apply high-specificity CSS that:
- Overrides `text-align` with theme defaults
- Applies padding and margins that conflict with absolute positioning
- Sets `background-color` that blocks the AI background image
- Changes font sizes on `statement` and `fact` layouts

`layout: none` bypasses ALL of this, giving full CSS control.

## Background Image via CSS (NOT frontmatter)

**CRITICAL:** Use CSS `background-image`, NOT Slidev's frontmatter `background:` property.

```css
/* CORRECT — CSS background */
.slide-03 { background-image: url('./slides/slide-03.png'); }

/* WRONG — frontmatter background is blocked by theme */
/* background: ./slides/slide-03.png */
```

The frontmatter `background:` renders on a parent element that the theme's opaque `background-color` covers.

## v-clicks Compatibility

`<v-clicks>` works inside zone divs when wrapping markdown content:

```html
<div class="zone zone-bullets" style="left:5%;top:32%;width:55%;height:50%;">
  <v-clicks>

  - Item one
  - Item two
  - Item three

  </v-clicks>
</div>
```

**Rules:**
- `<v-clicks>` only works on top-level markdown content
- Blank line required after `<v-clicks>` and before `</v-clicks>`
- Does NOT work inside nested HTML `<div>` structures
- For custom HTML layouts, use static presentation instead

## Text Contrast Guarantee

The AI image generation prompt requires uniform backgrounds in text zones. Text color is chosen to contrast:

| Zone background | Text color | Fallback if mismatch |
|----------------|------------|---------------------|
| Dark (planned) | `white` or `rgba(255,255,255,0.9)` | Add `text-shadow: 0 1px 3px rgba(0,0,0,0.5)` |
| Light (planned) | `#1a1a2e` or `rgba(0,0,0,0.85)` | Add `text-shadow: 0 1px 3px rgba(255,255,255,0.5)` |

**Background mismatch remediation:** If Phase 1 QA finds that zone background differs from planned:
1. Update text color in `layout-plan.json` to match actual background
2. Regenerate CSS for affected zones
3. If background is inconsistent (gradient/pattern in zone), add a semi-transparent backdrop:

```css
.zone-heading-fallback {
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(4px);
  border-radius: 8px;
  padding: 12px 16px;
}
```

## Font Rendering

Fonts are loaded via Google Fonts in Slidev headmatter:

```yaml
fonts:
  sans: Outfit
  serif: Source Serif 4
```

The browser renders text at native resolution — always crisp, no aliasing artifacts from image generation.

**Forbidden fonts:** Inter, Roboto, Arial, Open Sans, Lato, Space Grotesk (too generic).

**Recommended pairs:** Outfit + Source Serif 4, Syne + Literata, Cabinet Grotesk + Newsreader, Plus Jakarta Sans + Fraunces, Bricolage Grotesque + Lora.

## HTML Nesting Limit

Maximum 3 levels of HTML nesting inside zone divs. Deeper nesting causes Slidev to output raw HTML source instead of rendered content. Flatten with CSS Grid/Flexbox on a single wrapper.

## z-index Stacking (with --picture)

When `--picture` adds photos, the stacking order changes:

| Layer | z-index | Content |
|-------|---------|---------|
| AI background | 0 | Generated PNG |
| Photo layer | 1 | Additional photos from Brave search |
| Text zones | 2 | HTML text overlay |
```

- [ ] **Step 2: Commit**

```bash
git add slidecraft/.claude/skills/slidecraft/references/text-overlay-rules.md
git commit -m "feat(slidecraft): add text-overlay-rules.md reference"
```

---

## Chunk 4: Adapted Reference Files

Copy and adapt reference files from source skills.

### Task 5: Adapt image-prompt-guide.md

**Files:**
- Create: `slidecraft/.claude/skills/slidecraft/references/image-prompt-guide.md`
- Source: `slidegen/.claude/skills/slidegen/references/image-prompt-guide.md`

- [ ] **Step 1: Read source and write adapted version**

Read `slidegen/.claude/skills/slidegen/references/image-prompt-guide.md` completely. Create the slidecraft version with these changes:

1. **Replace prompt structure.** Slidegen structure is:
   ```
   [Slide type + format] → [Layout & composition] → [Text content] → [Visual details] → [Style suffix]
   ```
   Slidecraft structure is:
   ```
   [Slide type + format] → [Layout & composition with empty zones] → [Visual details OUTSIDE zones] → [Explicit empty zone instructions] → [Style suffix]
   ```

2. **Remove all "text content in prompt" rules.** Slidegen says "every word must be written out explicitly." Slidecraft says NO text in prompts — only zone instructions.

3. **Add empty zone instruction rules:**
   - "For each text zone in layout-plan.json, include: 'Leave the area from [x] to [x+w] horizontally, [y] to [y+h] vertically completely empty — no text, no decorative elements. Background must be uniform [dark|light] in this region.'"
   - "All visual elements (icons, decorative shapes, charts, illustrations) MUST be placed ONLY outside text zones"
   - "Zone backgrounds must be uniform and predictable for text overlay contrast"

4. **Add Zone Contrast Guarantee section:** Explain that the prompt must ensure zones have uniform backgrounds for text readability.

5. **Keep:** Word count targets (adapted — shorter since no text content), aspect ratio rules, style suffix rules, spatial description rules, background specification rules.

6. **Replace all examples** with text-free equivalents. E.g., instead of `"Heading reads 'Market Overview'"`, use `"Leave upper-left 60%×15% area clean for heading text — uniform dark background in this zone"`.

- [ ] **Step 2: Commit**

```bash
git add slidecraft/.claude/skills/slidecraft/references/image-prompt-guide.md
git commit -m "feat(slidecraft): add adapted image-prompt-guide.md for text-free generation"
```

### Task 6: Adapt scoring-subroutine.md

**Files:**
- Create: `slidecraft/.claude/skills/slidecraft/references/scoring-subroutine.md`
- Source: `slidegen/.claude/skills/slidegen/references/scoring-subroutine.md`

- [ ] **Step 1: Read source and write adapted version**

Read `slidegen/.claude/skills/slidegen/references/scoring-subroutine.md`. Replace the 6 axes with slidecraft's axes:

| Axis | What is evaluated (1-10) |
|------|--------------------------|
| Visual impact | AI background quality + overall impression |
| Layout precision | Text positioning accuracy in zones — text fits zones, no overflow, balanced spacing |
| Typography quality | Readability, contrast against AI background, font hierarchy, line-height |
| Color conviction | AI layer palette coherence + harmony with text layer colors |
| Content clarity | Information hierarchy, readability at presentation scale, logical flow |
| Layer harmony | How well the two layers work together — text doesn't fight the visual, complementary composition |

Keep the scoring procedure (read PNG, evaluate, score 1-10, write report), but adapt the rubric descriptions and examples for the two-layer paradigm.

**Add remediation source detection:** For each axis scoring < 7 (matching --polish threshold), add guidance on identifying whether the problem is in the image layer, text layer, or both (per the spec's remediation table).

- [ ] **Step 2: Commit**

```bash
git add slidecraft/.claude/skills/slidecraft/references/scoring-subroutine.md
git commit -m "feat(slidecraft): add adapted scoring-subroutine.md with dual-layer axes"
```

### Task 7: Adapt remaining reference files

**Files:**
- Create: `slidecraft/.claude/skills/slidecraft/references/polish-procedure.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/ab-testing.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/design-memory.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/compare-procedure.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/preset-format.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/layout-css-patterns.md`
- Create: `slidecraft/.claude/skills/slidecraft/references/responsive-check.md`

- [ ] **Step 1: Adapt polish-procedure.md**

Read `slidegen/.claude/skills/slidegen/references/polish-procedure.md`. Adapt by adding the remediation table from the design spec:

| Axis | Layer | Remediation action |
|------|-------|--------------------|
| Visual impact | Image | Regenerate PNG with A/B variant prompts |
| Layout precision | Both | Adjust zone coordinates → regenerate PNG → update CSS |
| Typography quality | Text | Adjust font sizes, weights, colors, line-height in CSS |
| Color conviction | Image | Regenerate PNG with A/B variant palettes |
| Content clarity | Text | Restructure text content, simplify bullets, adjust hierarchy |
| Layer harmony | Both | Analyze which layer causes dissonance → targeted fix |

Max 5 polish cycles. Early exit if overall score ≥ 9. Auto-capture preset if final score ≥ 9.

- [ ] **Step 2: Adapt ab-testing.md**

Read `slidegen/.claude/skills/slidegen/references/ab-testing.md`. Adapt for two-layer A/B testing:
- **Image A/B**: Generate two variant PNG prompts (different visual directions) for the same slide
- **Text A/B**: Generate two CSS/positioning variants for the same text content
- **Layer-aware selection**: Score both variants on the slidecraft 6 axes, pick the better composite

- [ ] **Step 3: Adapt design-memory.md**

Read `slidegen/.claude/skills/slidegen/references/design-memory.md`. Adapt:
- Change file path to `~/.claude/slidecraft-design-memory.json`
- Change max entries to 50 (add note: "higher than slidegen's 20 — two-layer entries contain richer data")
- Extend entry format with `visual` and `text` sub-objects per the design spec:
  ```json
  {
    "visual": { "style_suffix", "palette", "effective_patterns", "zone_clarity" },
    "text": { "fonts", "positioning_accuracy", "contrast_issues" }
  }
  ```

- [ ] **Step 4: Adapt compare-procedure.md**

Read `slidegen/.claude/skills/slidegen/references/compare-procedure.md`. Adapt:
- Score on slidecraft's 6 axes (not slidegen's)
- Comparison is on composite exports (final PNG with both layers merged)
- Include example delta table from design spec

- [ ] **Step 5: Adapt preset-format.md**

Read `slidev/.claude/skills/slidev/references/preset-format.md`. Extend YAML frontmatter with:
- `zone_strategy` — default zone placement template
- `text_color` — default text color for zones
- `text_contrast_mode: light-on-dark | dark-on-light` — add to frontmatter after `text_color` (new for slidecraft)
- Remove `background` field from slidev presets — AI-generated PNGs replace static backgrounds
- Keep `mood`, `palette`, `decoration`, `fonts`, `colorSchema`, `accent_color`, `transition`
- Add `css` block for Slidev styles (same as slidev presets)
- Add style suffix body for AI image generation prompts
- Lookup order: direct path → `./.slidecraft-presets/<name>.preset.md` → `~/.claude/slidecraft-presets/<name>.preset.md`

- [ ] **Step 6: Adapt layout-css-patterns.md**

Read `slidev/.claude/skills/slidev/references/layout-css-patterns.md`. Adapt for slidecraft's `layout: none` + absolute positioning paradigm:
- Remove layout-specific patterns (cover, section, default, etc.) — slidecraft doesn't use them
- Keep the core CSS patterns: `position: absolute; inset: 0` for full-bleed, two-layer flexbox for vertical centering within zones
- Add zone-specific patterns: how to handle lists, stats, quotes within absolute-positioned zones
- Add background-image patterns for AI-generated PNGs
- Add zone fallback patterns (semi-transparent backdrop for contrast issues)

- [ ] **Step 7: Adapt responsive-check.md**

Read `slidev/.claude/skills/slidev/references/responsive-check.md`. Adapt:
- Instead of checking Slidev layout overflow, check zone-based layout:
  - Do zones overflow at 4:3? (percentages should scale, but check edge cases)
  - Does the AI background scale correctly via `background-size: cover`?
  - Are text zones still readable at the narrower aspect ratio?

- [ ] **Step 8: Commit all adapted references**

```bash
git add slidecraft/.claude/skills/slidecraft/references/
git commit -m "feat(slidecraft): add adapted reference files for dual-layer architecture"
```

---

## Chunk 5: SKILL.md — Header, Input Parsing & Subcommands

### Task 8: Write SKILL.md frontmatter, references block, and input parsing

**Files:**
- Create: `slidecraft/.claude/skills/slidecraft/SKILL.md`

- [ ] **Step 1: Write the file header section**

Write the first section of SKILL.md (frontmatter through subcommand handlers). The structure follows slidegen's SKILL.md pattern but with slidecraft-specific content.

**Frontmatter:**
```yaml
---
name: slidecraft
description: Use when generating a two-layer presentation from a slide outline. Generates AI background images (text-free) via configurable APIs (Polza.ai default), then assembles a Slidev project with HTML/CSS text overlay. Supports preset styles, custom style descriptions, reference-based consistency, dual-layer QA scoring, and all management subcommands.
argument-hint: "[--help | --edit [dir] <comment> | --polish=N [dir] | --compare <dir1> <dir2> | --notes [dir] | --learn=N | --create-preset <name> | --export <format> [dir] | --dev [dir] | --responsive [dir] | --picture [auto|paths...] [dir] | --preset <name> | --provider <name> | --model <id> | --no-ref | style: <desc>] <outline or file path>"
---
```

**Title and intro:** "SlideCraft — Two-Layer Presentation Generator. You generate complete presentations by combining AI-generated visual backgrounds (without text) with Slidev HTML/CSS text overlay. Every generation produces a Slidev project with pixel-perfect typography over AI-designed visuals."

**References block:** List all 18 reference files with CRITICAL markers on: `providers.md`, `image-prompt-guide.md`, `layout-plan-format.md`, `text-overlay-rules.md`, `design-principles.md`, `layout-css-patterns.md`.

**Input Parsing section:** Same structure as slidegen — global flags (`--provider`, `--model`, `--no-ref`, `--base-url`, `--api-key-env`) followed by subcommand dispatch.

**Subcommand handlers — write each following the pattern from slidegen/slidev SKILL.md:**

1. `--help` — Usage table showing all commands (follow slidegen's format, add slidecraft-specific commands)
2. `--create-preset <name>` — 9-question wizard per design spec (7 from slidegen + zone_strategy + text_contrast_mode). Generate demo from `assets/demo-outline.md`, run dual QA, score.
3. `--learn=N` — Parse N (default 3, max 10). 7-step procedure:
   1. Generate N diverse outlines (varied topics, slide counts 3-10, all roles represented)
   2. For each outline: run full pipeline (Steps 1–7)
   3. Dual QA scoring on composite output
   4. Analyze patterns: which prompt strategies produced clean zones? Which zone_strategies gave best layout precision? Which font pairings scored highest on typography?
   5. Write `improvements.md` with findings for both image-layer (prompt wording, zone instruction clarity) and text-layer (font choices, zone sizing, CSS patterns)
   6. Apply improvements to next iteration's generation parameters
   7. Write design memory entry after each iteration
   Early exit if overall avg ≥ 9.
4. `--polish=N [dir]` — Reference `references/polish-procedure.md`. Note dual-layer remediation.
5. `--compare <dir1> <dir2>` — Reference `references/compare-procedure.md`. Composite scoring.
6. `--notes [dir]` — Reference `references/notes-procedure.md`. Unchanged.
7. `--responsive [dir]` — Reference `references/responsive-check.md`. Zone overflow check.
8. `--dev [dir]` — Full pattern: resolve dir → `npm install` if needed → `cd <dir> && (sleep infinity | npx slidev) 2>&1` with `run_in_background: true` → wait for ready URL → report.
9. `--export <format> [dir]` — Formats: `html`, `pdf`, `png2pdf`, `pngs`, `png_N`. Follow slidev's export procedure.
10. `--edit [dir] <comment>` — Three-type detection per design spec decision tree: TEXT → Slidev layer only, VISUAL → regenerate PNG, BOTH → full cycle. **Include overflow escalation:** if a TEXT edit causes content to overflow the zone (e.g., adding bullets that don't fit), escalate to BOTH type (resize zone → update prompt_hint → regenerate PNG → update CSS).
11. `--picture [auto|paths...] [dir]` — 6-step procedure per design spec. **IMPORTANT:** When photos are added, SKILL.md must instruct to change text zone z-index from 1 to 2, placing photos at z-index 1 between AI background (0) and text (2).

**Directory Auto-Detection:** Same as slidegen but look for `layout-plan.json` instead of `prompts.json`.

- [ ] **Step 2: Commit SKILL.md header**

```bash
git add slidecraft/.claude/skills/slidecraft/SKILL.md
git commit -m "feat(slidecraft): write SKILL.md header, input parsing, and subcommands"
```

---

## Chunk 6: SKILL.md — Main Generation Pipeline

### Task 9: Write the generation procedure (Steps 1–7)

**Files:**
- Modify: `slidecraft/.claude/skills/slidecraft/SKILL.md` (append after subcommands section)

**Step numbering mapping (Spec → SKILL.md):**

| Spec Step | SKILL.md Section | Plan Step |
|-----------|-----------------|-----------|
| Step 1: Outline Parsing | "Step 1: Parse Outline" | Step 1 below |
| Step 2: Layout Planning | "Step 2: Layout Planning" | Step 5 below |
| Step 3: Image Prompt Gen | "Step 3: Image Prompt Generation" | Step 6 below |
| Step 4: Image Generation | "Step 4: Image Generation" | Step 7 below |
| Step 5: Slidev Assembly | "Step 5: Slidev Project Assembly" | Step 8 below |
| Step 5.5: Install Deps | "Step 5.5: Install Dependencies" | Step 9 below |
| Step 6: Dual QA | "Step 6: Dual QA" | Step 10 below |
| Step 7: Export | "Step 7: Export & Output Summary" | Step 11 below |

Use the spec's step numbers in SKILL.md to maintain consistency.

- [ ] **Step 1: Write Outline Parsing section (Spec Step 1)**

Write the "Step 1: Parse Outline" section of SKILL.md:

1. Accept outline as inline text or file path (if file path, read the file)
2. Count slides from the outline
3. Assign a role to each slide from: `cover`, `section`, `content`, `stat`, `quote`, `comparison`, `end`
4. Role assignment heuristics:
   - First slide → `cover`
   - Last slide → `end`
   - Slides with "Section:", "Part:", or divider titles → `section`
   - Slides with numbers, percentages, metrics → `stat`
   - Slides with quoted text → `quote`
   - Slides with "vs", "compared to", side-by-side items → `comparison`
   - All others → `content`
5. Print slide list with assigned roles for user confirmation

- [ ] **Step 2: Write Generation Modes section**

Three modes (same structure as slidegen):
1. **Preset mode** — `--preset <name>`: Load preset per `references/preset-format.md` lookup order. Apply visual style suffix + text layer config.
2. **Custom Style mode** — `style: <desc>`: Parse style description into visual + text parameters.
3. **Unique mode** (default): Design unique visual direction + text styling. Read Design Memory for inspiration.

- [ ] **Step 2: Write Step 1 — Resolve Provider and API Key**

Follow `references/providers.md`. Same as slidegen — resolve provider, model, endpoint, API key. Print error with Polza referral link if key not set.

- [ ] **Step 3: Write Step 2 — Read Design Memory**

Same as slidegen but read from `~/.claude/slidecraft-design-memory.json`. Draw inspiration from `visual` and `text` sub-objects.

- [ ] **Step 4: Write Step 3 — Design Thinking**

Combines slidegen's design thinking (palette, typography mood, background, decorative elements, style suffix) with slidev's design thinking (Google Fonts selection, CSS variables, UnoCSS shortcuts). Output:
- **Style suffix** for AI image prompts (same concept as slidegen)
- **Text styling plan**: fonts, accent colors, CSS variable values
- **Zone strategy**: default zone placement template for this presentation

- [ ] **Step 5: Write Step 2 — Layout Planning (NEW — slidecraft-specific)**

This is the core new step. For each slide in the outline:

1. Assign role (`cover`, `section`, `content`, `stat`, `quote`, `comparison`, `end`)
2. Determine text content (heading, subheading, bullets, stats — from outline)
3. Apply zone strategy (from preset or default per role — see `references/layout-plan-format.md`)
4. Generate zone objects with precise coordinates in percentages
5. Generate `prompt_hint` per template in `references/layout-plan-format.md`
6. Generate `visual_description` for non-zone areas

Write `layout-plan.json` to `<output-dir>/layout-plan.json`.

- [ ] **Step 6: Write Step 3 — Image Prompt Generation**

For each slide, compose the prompt per `references/image-prompt-guide.md`:
```
[Slide type + format: "16:9 aspect ratio presentation slide. This is a <role> slide."]
→ [Layout with empty zones: "Upper-left 60%×15% area must be completely empty..."]
→ [Visual details OUTSIDE zones: decorations, icons, charts, shapes]
→ [Explicit zone instructions from prompt_hint]
→ [Style suffix]
```

**Prompt review:** Before generation, verify each prompt contains zone instructions, style suffix, role description, no contradictions. Fix issues.

Save to `prompts.json` (similar format to slidegen but with zone data):
```json
{
  "slides": [
    {
      "index": 1,
      "role": "cover",
      "zones": [ /* zone objects from layout-plan.json */ ],
      "prompt": "Full prompt text...",
      "prompt_hint": "Leave area...",
      "style_suffix": "Style: Dark navy..."
    }
  ],
  "style_suffix": "Style: Dark navy...",
  "generation_mode": "unique"
}
```

- [ ] **Step 7: Write Step 4 — Image Generation**

Same as slidegen Step 5 with these differences (≥3 slides required for reference mode — same as slidegen):
- Output dir naming: same slugification from topic
- Reference mode: same anchor selection process
- Error handling: same timeouts and retries
- **Phase 1 QA (inline):** After generating ALL images, read each PNG and verify:
  - Text zones are empty (no text, no decorative elements crossing zones)
  - Zone backgrounds are uniform enough for planned text color
  - Visual elements are in correct positions outside zones
  - Stylistic consistency between slides
  - Cap: 2 regen attempts per slide
  - **Background mismatch remediation:** If zone background differs from planned, update text color in `layout-plan.json`

Save `meta.json` (same as slidegen + add `zone_strategy` field).

- [ ] **Step 8: Write Step 5 — Slidev Project Assembly**

**7a. Scaffold `package.json`** — minimal: `@slidev/cli` + `@slidev/theme-default`

**7b. Write `uno.config.ts`** — UnoCSS shortcuts: `slide-heading`, `slide-subheading`, `slide-accent`

**7c. Write `styles/index.css`** — CSS variables + zone classes + per-slide background refs:
```css
/* CSS variables from design thinking */
:root {
  --color-accent: <hex>;
  --color-accent-dim: <rgba>;
  --color-accent-bg: <rgba>;
}

/* Core layout classes */
.slide-container { position: absolute; inset: 0; }
.slide-bg { position: absolute; inset: 0; background-size: cover; background-position: center; z-index: 0; }
.zone { position: absolute; z-index: 1; display: flex; flex-direction: column; justify-content: center; }

/* Per-slide backgrounds */
.slide-01 { background-image: url('./slides/slide-01.png'); }
.slide-02 { background-image: url('./slides/slide-02.png'); }
/* ... */
```

**7d. Write `slides.md`** — headmatter (theme, title, fonts, colorSchema, transition, aspectRatio) + per-slide content:
- Every slide uses `layout: none`
- Each slide has `<div class="slide-container">` with background + zones
- Zone positions from layout-plan.json → inline CSS `style="left:X%;top:Y%;width:W%;height:H%;"`
- Text content from layout-plan.json zones
- `<v-clicks>` on list-type zones
- Per-slide `<style>` blocks for typography overrides

**7e. Write `components/Icon.vue`** — Copy from slidev skill (SVG icon component, no emoji). Read `slidev/.claude/skills/slidev/SKILL.md` for the Icon.vue specification and copy the component definition.

**7f. Copy `slides/` PNGs** — Already generated in Step 6. Ensure they're in `<output-dir>/slides/`.

**7g. Copy `layout-plan.json` and `prompts.json`** — Already written in Steps 4-5.

- [ ] **Step 9: Write Step 5.5 — Install Dependencies**

```bash
cd <output-dir> && npm install && npx playwright install chromium
```

Runs once after assembly. Required before QA or dev server.

- [ ] **Step 10: Write Step 6 — Dual QA (Phase 2 — Composite)**

Phase 1 already ran inline during Step 6. Phase 2:

1. Export composite PNGs: `cd <output-dir> && npx slidev export --format png --output slides-qa`
2. Read EVERY exported PNG. Evaluate per scoring subroutine (`references/scoring-subroutine.md`)
3. Score on 6 slidecraft axes
4. Write `score-report.md`
5. Remediation: slide < 6 on any axis → determine source (image/text/both) → fix → re-export → re-score. Max 2 image regens, 3 CSS adjustments per slide.
6. Content review per `references/content-review-subroutine.md`
7. Cleanup: `rm -rf slides-qa`

- [ ] **Step 11: Write Step 7 — Export & Output Summary**

**PDF Assembly** (same as slidegen — Python Pillow script). Check Python available, ensure Pillow, assemble.

**Design Memory Write** — per `references/design-memory.md` write protocol. Score-based entry type (success/neutral/failure).

**Output Summary:**
```
SlideCraft complete!

  Project:   <output-dir>/ (Slidev project)
  Slides:    <output-dir>/slides/ (N AI-generated PNGs)
  PDF:       <output-dir>/slides.pdf
  Layout:    <output-dir>/layout-plan.json
  Prompts:   <output-dir>/prompts.json
  Metadata:  <output-dir>/meta.json
  Score:     <overall-avg>/10
  Report:    <output-dir>/score-report.md

  Provider:  <provider> / <model>
  Mode:      reference (anchor: slide N) | no-reference
  QA:        Phase 1: N image regens, Phase 2: N CSS fixes

  Preview:   cd <output-dir> && npm run dev
  Export:    /slidecraft --export pdf <output-dir>
```

- [ ] **Step 12: Write Slide Prompt Authoring Rules**

Adapted from slidegen's rules. Key changes:
1. **No text in prompts** — replaced with zone instructions
2. **Always specify empty zones** with coordinates from layout-plan.json
3. **Always specify zone background requirement** (uniform dark or light)
4. Keep: style suffix rule, 16:9 rule, 2000 char limit, English prompts, spatial descriptions, background specification, role descriptions
5. Remove: "specify exact text" rule, typography-in-prompt rules (typography is in CSS now)

- [ ] **Step 13: Commit SKILL.md generation pipeline**

```bash
git add slidecraft/.claude/skills/slidecraft/SKILL.md
git commit -m "feat(slidecraft): write main generation pipeline (steps 1-9)"
```

---

## Chunk 7: Registration & Smoke Test

### Task 10: Register skill in settings.json

**Files:**
- Modify: `.claude/settings.json`

- [ ] **Step 1: Read current settings.json**

Read `.claude/settings.json` to understand the current skill registration format.

- [ ] **Step 2: Add slidecraft entry**

Follow the exact pattern used for existing slidegen and slidev entries (including path, description, and trigger fields). Do NOT assume the structure — read settings.json first and replicate the existing pattern exactly.

- [ ] **Step 3: Commit registration**

```bash
git add .claude/settings.json
git commit -m "feat(slidecraft): register skill in settings.json"
```

### Task 11: Update CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Add slidecraft to Current Skills table**

Add a new row to the skills table in CLAUDE.md:

```markdown
| SlideCraft (Two-Layer Presentations) | `slidecraft/` | `/slidecraft` |
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: register slidecraft skill in CLAUDE.md"
```

### Task 12: Smoke test

- [ ] **Step 1: Verify skill loads**

Run `/slidecraft --help` and verify it prints the usage table without errors.

- [ ] **Step 2: Verify references load**

Run `/slidecraft` with a minimal 3-slide outline and verify:
- layout-plan.json is generated correctly
- Image prompts contain zone instructions (no text content)
- Images are generated (requires API key)
- Slidev project assembles with correct CSS positioning
- Dual QA runs both phases

**Note:** Full smoke test requires a `POLZA_API_KEY` environment variable. If not available, verify up to the prompt generation step and confirm prompts follow the text-free format.

- [ ] **Step 3: Final commit if any fixes needed**

```bash
git add slidecraft/.claude/
git commit -m "fix(slidecraft): smoke test fixes"
```
