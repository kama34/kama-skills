# SlideCraft — Design Spec

## Overview

SlideCraft is a new Claude Code skill that combines the image generation capabilities of slidegen with the web-based presentation engine of slidev. It produces two-layer slides: AI-generated visual backgrounds (without text) + HTML/CSS text overlay rendered by Slidev.

**Motivation:** AI image models render text unreliably (garbled characters, inconsistent sizing). By separating the visual layer (AI-generated PNG) from the text layer (Slidev HTML/CSS), slidecraft delivers beautiful AI visuals with pixel-perfect, crisp typography.

**Trigger:** `/slidecraft`

## Architecture: Standalone Skill

SlideCraft is a fully independent skill with its own SKILL.md and reference files. It does not modify or depend on slidegen or slidev at runtime. Reference files are copied and adapted — this trades duplication for reliability and independent evolution.

## Pipeline

```
Outline → Layout Planning → Image Prompt Generation → Image Generation → Slidev Assembly → Dual QA → Export
```

### Step 1: Outline Parsing

Receive user outline (topic, slide structure, text content). Assign roles to each slide: `cover`, `section`, `content`, `stat`, `quote`, `comparison`, `end`.

### Step 2: Layout Planning

For each slide, Claude:

1. Determines semantic layout: where heading, subheading, bullets, stats, decorative elements should go
2. Converts to precise coordinates in percentages
3. Writes `layout-plan.json`

#### layout-plan.json Format

```json
{
  "slides": [
    {
      "slide": 1,
      "role": "cover",
      "zones": [
        {
          "id": "title",
          "type": "heading",
          "text": "Заголовок презентации",
          "position": { "x": "10%", "y": "35%", "w": "80%", "h": "15%" },
          "style": {
            "fontSize": "3em",
            "fontWeight": "bold",
            "color": "white",
            "textAlign": "center"
          }
        },
        {
          "id": "subtitle",
          "type": "subheading",
          "text": "Подзаголовок",
          "position": { "x": "15%", "y": "55%", "w": "70%", "h": "8%" },
          "style": {
            "fontSize": "1.4em",
            "color": "rgba(255,255,255,0.7)",
            "textAlign": "center"
          }
        }
      ],
      "visual_description": "Dark gradient background with geometric decorative elements on edges",
      "prompt_hint": "Leave central 80%x30% area (from 35% to 65% vertically) completely empty for title and subtitle. Place decorative elements only on edges and corners."
    }
  ]
}
```

**Zone types:** `heading`, `subheading`, `list`, `body`, `stat`, `quote`, `cta`, `caption`

**prompt_hint:** Auto-generated English instruction for the AI model, derived from zone positions. Explicitly tells the model which areas must remain clean.

### Step 3: Image Prompt Generation

Prompts follow a modified slidegen structure:

```
[Slide type + format]
→ [Layout & composition with explicit empty zones]
→ [Visual details: decorations, icons, charts, shapes]
→ [Explicit empty zones: "Leave area at X,Y size W×H completely empty"]
→ [Style suffix]
```

**Key differences from slidegen prompts:**

| Aspect | slidegen | slidecraft |
|--------|----------|------------|
| Text in prompt | Every word explicit: `"Heading reads 'Market Overview'"` | No text — only zones: `"Leave 55%×12% at top-left clean"` |
| Empty zones | No concept | Explicit instructions: `"This area must be completely empty — uniform background, no decorative elements crossing into it"` |
| Visual elements | Placed anywhere | Placed ONLY outside text zones |
| Contrast | Text+background in prompt | Zones must have uniform, predictable background for text overlay |

**Zone Contrast Guarantee:** The prompt explicitly requires that empty zones have a uniform, predictable background (dark or light) so that overlaid text is guaranteed to be readable. Text color in `layout-plan.json` is chosen based on the planned zone background.

### Step 4: Image Generation (slidegen engine)

AI generates PNG for each slide via Polza (default), OpenAI, or custom provider.

**Reference mode** (default, ≥3 slides):
1. Generate slide 1 (cover) — no reference
2. Generate slide 2 — no reference
3. Style anchor selection: score both, higher wins
4. Slides 3..N — anchor PNG as reference image

**Image QA (Phase 1):** Before text overlay, Claude reads each PNG and verifies:
- Text zones are actually empty (no text, no decorative elements crossing into zones)
- Background in zones is uniform enough for planned text color
- Visual elements (icons, charts, decorations) are in correct positions
- Stylistic consistency between slides

If zone is not empty → regeneration with reinforced prompt: `"CRITICAL: the area at X,Y must be COMPLETELY empty"`

### Step 5: Slidev Project Assembly

Create a Slidev project with AI images as backgrounds and text overlay via CSS absolute positioning.

**Project structure:**
```
<output-dir>/
  package.json          # @slidev/cli + @slidev/theme-default
  slides.md             # All slides with layout: none
  styles/index.css      # CSS variables, zone classes, background refs
  slides/               # AI-generated PNGs
    slide-01.png
    slide-02.png
    ...
  components/
    Icon.vue            # SVG icon component (no emoji)
  layout-plan.json      # Zone coordination data
  prompts.json          # AI prompts used
  meta.json             # Generation metadata
```

**Slide structure in slides.md:**

```markdown
---
layout: none
---

<div class="slide-container">
  <div class="slide-bg slide-03"></div>

  <div class="zone zone-heading" style="left:5%;top:8%;width:55%;height:12%;">
    <h1>Наше решение</h1>
  </div>

  <div class="zone zone-bullets" style="left:5%;top:32%;width:55%;height:50%;">
    <v-clicks>

    - Анализ данных
    - Построение модели
    - Внедрение

    </v-clicks>
  </div>
</div>
```

**CSS patterns:**

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

.slide-03 { background-image: url('./slides/slide-03.png'); }

.zone {
  position: absolute;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
```

**Key decisions:**
- `layout: none` mandatory — no Slidev theme interference
- PNG as `background-image` via CSS — not frontmatter `background:` (theme blocks it)
- `position: absolute` + coordinates from layout-plan.json — direct `%` → CSS conversion
- v-clicks work — text remains native markdown inside `<div>`, animations preserved
- Fonts via Google Fonts in headmatter — rendered by browser with perfect quality
- z-index layers: background (0) → text (1) → optional decorative CSS elements (2)

### Step 6: Dual QA

Two-phase quality assurance process.

**Phase 1 — Image QA** (after PNG generation, before text overlay):
- Text zones actually empty?
- No decorative elements crossing into zones?
- Background in zones uniform enough for text?
- If violated → regenerate PNG with reinforced prompt

**Phase 2 — Composite QA** (after Slidev assembly, export via `npx slidev export --format png`):
- Text readable? Contrast sufficient?
- Positioning correct? Text doesn't overflow zones?
- Text doesn't overlap important visual elements?
- Typography: sizes, line-height, alignment
- Overall composition: balance of text and visuals

**Scoring — adapted 6-axis system (1-10 each):**

| Axis | What is evaluated |
|------|-------------------|
| Visual impact | AI background quality + overall impression |
| Layout precision | Text positioning accuracy in zones |
| Typography quality | Readability, contrast, font hierarchy |
| Color conviction | AI layer palette + harmony with text layer |
| Content clarity | Information hierarchy, clarity |
| Layer harmony | How well the two layers work together |

**Remediation:**
- Slide < 6 on any axis → determine source:
  - Image problem → regenerate PNG (Phase 1)
  - Text problem → adjust CSS/positioning (Phase 2)
  - Harmony problem → may require both
- Up to 2 regeneration attempts per slide

### Step 7: Export

Final export via Slidev export engine:
- `--export pdf` — PDF via Slidev
- `--export png2pdf` — PNG export → Pillow assembly (pixel-perfect)
- `--export pngs` — individual PNG files
- `--export png_N` — single slide PNG

## Subcommands

| Command | Behavior |
|---------|----------|
| **generation** (main) | Full pipeline: outline → layout-plan → image gen → slidev assembly → dual QA |
| `--edit [dir] <comment>` | Detects edit type: **text** → Slidev layer only, **visual** → regenerate PNG + reassemble, **both** → full cycle. Does not regenerate unaffected slides |
| `--polish=N [dir]` | N iterations of dual QA. Scoring → identify weak layer → A/B test at appropriate layer → re-score |
| `--compare <dir1> <dir2>` | Export both, score on 6 axes, delta table. Compares both AI layer and composite |
| `--notes [dir]` | Adds 4-point speaker notes (Opening/Key message/Details/Transition) |
| `--learn=N` | N iterations: generate → dual QA → analyze → adjust prompt AND positioning strategy → improvements.md |
| `--create-preset <name>` | 7-question wizard. Preset includes: visual style (for AI) + typography (for text layer) + zone layout templates |
| `--dev [dir]` | `sleep infinity \| npx slidev` — live preview with background PNGs and text overlay |
| `--export <format> [dir]` | pdf / png2pdf / pngs / png_N — final composite export via Slidev |
| `--responsive [dir]` | Switch aspectRatio to 4/3, check: zones don't overflow? Background scales correctly? |
| `--picture [auto\|paths]` | Adds additional photos (via Brave search) into non-text zones on top of AI background |

### --edit Detail

Edit type detection:

```
Text edit:   "Change heading on slide 3" → update HTML in slides.md + CSS if needed → Phase 2 QA only
Visual edit: "Make background brighter on slide 5" → modify prompt → regenerate PNG → Phase 1 + Phase 2 QA
Both:        "Move bullets to the right on slide 3" → update layout-plan.json → update prompt_hint → regenerate PNG → update CSS → full dual QA
```

## Design Memory

Separate file: `~/.claude/slidecraft-design-memory.json`

- Independent from slidegen/slidev — different prompt strategies
- Entries include both visual style (what worked for AI) and text style (fonts/sizes/positioning results)
- Max 50 entries, FIFO eviction

```json
{
  "date": "2026-03-14",
  "topic": "AI Product Pitch",
  "type": "success",
  "score": 8.5,
  "visual": {
    "style_suffix": "Dark gradient navy-to-indigo...",
    "palette": "navy, indigo, cyan accent",
    "effective_patterns": ["geometric decorative cards in right 35%"],
    "zone_clarity": "95% — zones were clean on first attempt"
  },
  "text": {
    "fonts": "Outfit + Source Serif 4",
    "positioning_accuracy": "high — no QA repositioning needed",
    "contrast_issues": false
  }
}
```

## Preset Format

Presets are `.preset.md` files with extended YAML frontmatter covering both layers:

```yaml
---
name: corporate-dark
# Visual layer (AI generation)
mood: professional, minimal, dark
palette: "#1a1a2e, #16213e, #0f3460, #4facfe accent"
decoration: geometric shapes, subtle gradients
zone_strategy: text-left-60, visuals-right-35
# Text layer (Slidev)
fonts:
  sans: Outfit
  serif: Source Serif 4
colorSchema: dark
text_color: "white"
accent_color: "#4facfe"
transition: slide-left
---

Style suffix for AI image generation:
Professional dark presentation slide...

```css
:root {
  --color-accent: #4facfe;
  --color-accent-dim: rgba(79, 172, 254, 0.5);
  --color-accent-bg: rgba(79, 172, 254, 0.1);
}
```

**zone_strategy** — default zone placement template (`text-left-60`, `text-center`, `text-bottom-40`, etc.), overridable per slide.

Lookup order: direct path → `./.slidecraft-presets/<name>.preset.md` → `~/.claude/slidecraft-presets/<name>.preset.md`

## File Structure

```
slidecraft/
  .claude/skills/slidecraft/
    SKILL.md
    assets/
      demo-outline.md
    references/
      providers.md
      image-prompt-guide.md          # Modified for text-free generation
      layout-plan-format.md          # NEW: layout-plan.json specification
      text-overlay-rules.md          # NEW: CSS positioning rules for text over AI images
      scoring-subroutine.md          # Adapted for dual-layer scoring
      content-review-subroutine.md
      polish-procedure.md
      ab-testing.md
      design-memory.md
      compare-procedure.md
      notes-procedure.md
      preset-format.md               # Extended for two-layer presets
      design-principles.md           # 12 design principles from slidev
      layout-css-patterns.md         # CSS patterns for text overlay
      slidev-syntax.md
      slidev-layouts.md
      slidev-animations.md
      responsive-check.md
  .gitignore
  README.md
```

## Output Structure

```
<output-dir>/
  package.json
  uno.config.ts
  slides.md
  styles/index.css
  slides/
    slide-01.png ... slide-NN.png
  components/
    Icon.vue
  layout-plan.json
  prompts.json
  meta.json
  score-report.md
```
