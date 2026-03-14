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

**prompt_hint generation template:** For each zone, convert coordinates to English:
```
"Leave the area from [x] to [x+w] horizontally, [y] to [y+h] vertically completely empty —
no text, no decorative elements. Background must be uniform [dark|light] in this region."
```
Multiple zones are listed sequentially. The `[dark|light]` value is derived from the planned text color: white/light text → zone must be dark, dark text → zone must be light.

**Coordinate-to-CSS mapping:** Layout plan positions map directly to CSS `position: absolute`:
| layout-plan.json | CSS property |
|------------------|-------------|
| `x` | `left` |
| `y` | `top` |
| `w` | `width` |
| `h` | `height` |

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

**Phase 1 regeneration cap:** Up to 2 attempts per slide. If zone is still not empty after 2 attempts, proceed to assembly and rely on Phase 2 QA to catch remaining issues (CSS adjustments like semi-transparent overlay behind text can compensate).

**"Uniform enough" definition:** No visible pattern variation, gradient discontinuity, or decorative element edges within the zone area. The zone should read as a single flat or smoothly graduated color region when viewed at presentation scale.

**Background mismatch remediation:** If Phase 1 QA finds that zone background differs from planned (e.g., planned dark but AI generated light), update text color in `layout-plan.json` to match the actual background before proceeding to Step 5 assembly.

### Step 4.5: Install Dependencies

Before QA or dev server, install npm dependencies and Playwright:

```bash
cd <output-dir> && npm install && npx playwright install chromium
```

This step runs once after project scaffold (Step 5) and is required before any `npx slidev export` or `npx slidev` command.

### Step 5: Slidev Project Assembly

Create a Slidev project with AI images as backgrounds and text overlay via CSS absolute positioning.

**Project structure:**
```
<output-dir>/
  package.json          # @slidev/cli + @slidev/theme-default
  uno.config.ts         # UnoCSS shortcuts: slide-heading, slide-subheading, slide-accent
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

**Step 5b: Write `uno.config.ts`** — UnoCSS shortcuts for consistent text styling:
```ts
// Defines shortcuts: slide-heading, slide-subheading, slide-accent
// Used as utility classes in zone HTML for consistent typography
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
- `--export pdf` — PDF via Slidev's built-in PDF export
- `--export png2pdf` — Two-stage: first `npx slidev export --format png --output slides-export`, then Python Pillow assembles PNGs into PDF at 150 DPI, quality 95 (pixel-perfect, no browser PDF artifacts)
- `--export pngs` — Individual PNG files via `npx slidev export --format png`
- `--export png_N` — Single slide PNG (export all, return only slide N)
- `--export html` — Static SPA build via `npx slidev build --base /` for self-hosted presentations

**Write `score-report.md`** to `<output-dir>/score-report.md` after Phase 2 scoring.

## Subcommands

| Command | Behavior |
|---------|----------|
| **generation** (main) | Full pipeline: outline → layout-plan → image gen → slidev assembly → dual QA |
| `--edit [dir] <comment>` | Detects edit type: **text** → Slidev layer only, **visual** → regenerate PNG + reassemble, **both** → full cycle. Does not regenerate unaffected slides |
| `--polish=N [dir]` | N iterations of dual QA. Scoring → identify weak layer → A/B test at appropriate layer → re-score. See polish remediation table below |
| `--compare <dir1> <dir2>` | Export both, score on 6 axes, delta table. Compares both AI layer and composite |
| `--notes [dir]` | Adds 4-point speaker notes (Opening/Key message/Details/Transition) |
| `--learn=N` | N iterations: generate → dual QA → analyze → adjust prompt AND positioning strategy → improvements.md |
| `--create-preset <name>` | 7-question wizard. Preset includes: visual style (for AI) + typography (for text layer) + zone layout templates |
| `--dev [dir]` | Dev server: `cd <dir> && (sleep infinity \| npx slidev) 2>&1` run in background. Wait for "ready" URL in output, report to user. Requires `npm install` first |
| `--export <format> [dir]` | pdf / png2pdf / pngs / png_N — final composite export via Slidev |
| `--responsive [dir]` | Switch aspectRatio to 4/3, check: zones don't overflow? Background scales correctly? |
| `--picture [auto\|paths]` | Adds additional photos (via Brave search) into non-text zones on top of AI background |

### --polish Remediation Table

When `--polish` identifies a weak slide (< 7 on any axis), the remediation action depends on which axis scored low:

| Axis | Layer | Remediation action |
|------|-------|--------------------|
| Visual impact | Image | Regenerate PNG with A/B variant prompts (two visual directions) |
| Layout precision | Both | Adjust zone coordinates in layout-plan.json → regenerate PNG → update CSS |
| Typography quality | Text | Adjust font sizes, weights, colors, line-height in CSS |
| Color conviction | Image | Regenerate PNG with A/B variant palettes |
| Content clarity | Text | Restructure text content, simplify bullets, adjust hierarchy |
| Layer harmony | Both | Analyze which layer causes dissonance → targeted fix |

Max 5 polish cycles. Early exit if overall score ≥ 9. Auto-capture preset if final score ≥ 9.

### --learn=N Procedure

1. Generate N diverse outlines (varied topics, slide counts, roles)
2. For each outline: run full pipeline (steps 1–7)
3. Dual QA scoring on composite output
4. Analyze patterns: which prompt strategies produced clean zones? Which zone_strategies gave best layout precision? Which font pairings scored highest on typography?
5. Write `improvements.md` with findings for both image-layer and text-layer strategies
6. Apply improvements to next iteration's generation parameters
7. Write design memory entry after each iteration

### --create-preset Wizard

9-question wizard (7 from slidegen/slidev + 2 new for slidecraft):

1. **Mood** — What feeling should the presentation convey? (professional, playful, bold, minimal...)
2. **Color palette** — Primary colors and accent? (dark/light, specific hex values)
3. **Typography** — Font personality? (geometric, humanist, serif, mixed)
4. **Decoration** — Decorative elements? (geometric shapes, organic blobs, minimal lines, none)
5. **Background treatment** — Gradients, textures, solid colors?
6. **Transition** — Slide transition style?
7. **Aspect ratio** — 16:9 or 4:3?
8. **Zone strategy** (NEW) — Default text placement? (text-left-60, text-center, text-bottom-40, text-split-50-50)
9. **Text contrast mode** (NEW) — Light text on dark zones or dark text on light zones?

After wizard: generate demo from `assets/demo-outline.md`, run dual QA, score. If score ≥ 7, save preset.

### --picture Procedure

Adds real photos to non-text zones of AI-generated backgrounds:

1. Identify free zones — areas NOT occupied by text zones in layout-plan.json
2. Search photos via Brave Image Search (or use provided paths)
3. Download and place into `slides/` directory
4. For each slide with photos: add CSS `background-image` layer between AI background and text layer (z-index: 0.5 via stacking order)
5. Apply gradient overlay on photo edges to blend with AI background
6. Phase 2 QA on affected slides — verify photos don't interfere with text readability

### --compare Detail

Comparison is performed on composite exports (Phase 2 output — final PNG with both layers merged). Scoring uses slidecraft's 6 axes. Output format:

```
| Slide | Axis           | Dir1 | Dir2 | Delta |
|-------|----------------|------|------|-------|
| 1     | Visual impact  | 8    | 7    | +1    |
| 1     | Layer harmony  | 9    | 6    | +3    |
...
| Overall               | 7.8  | 6.5  | +1.3  |
```

### --edit Detail

**Edit type detection decision tree:**

1. Does the edit change zone coordinates (move, resize, reposition text)? → **BOTH** (full cycle: update layout-plan.json → update prompt_hint → regenerate PNG → update CSS → dual QA)
2. Does the edit change only visual style (colors, mood, decorative elements, background) without moving zones? → **VISUAL** (modify prompt → regenerate PNG → Phase 1 + Phase 2 QA)
3. Does the edit change only text content, font size, or text styling without moving zones? → **TEXT** (update HTML/CSS in slides.md → Phase 2 QA only)

**Examples:**

```
"Change heading on slide 3"           → TEXT  — update HTML, Phase 2 QA only
"Make font size bigger"               → TEXT  — update CSS, Phase 2 QA only (zone dimensions may still fit)
"Make background brighter on slide 5" → VISUAL — modify prompt, regenerate PNG, Phase 1+2 QA
"Make accent color brighter"          → TEXT  — CSS-only change (accent is in text layer)
"Move bullets to the right"           → BOTH  — update layout-plan + prompt + PNG + CSS, dual QA
"Add a new bullet point"              → TEXT  — update HTML, Phase 2 QA only (if text fits zone)
```

## Design Memory

Separate file: `~/.claude/slidecraft-design-memory.json`

- Independent from slidegen/slidev — different prompt strategies
- Entries include both visual style (what worked for AI) and text style (fonts/sizes/positioning results)
- Max 50 entries, FIFO eviction (higher than slidegen's 20 — two-layer entries contain richer data covering both visual and text strategies)

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
      layout-plan-format.md          # NEW — covers: JSON schema, zone types, position format,
                                     #   prompt_hint generation template, coordinate-to-CSS mapping,
                                     #   zone_strategy presets, per-role default zone layouts
      text-overlay-rules.md          # NEW — covers: CSS absolute positioning over background-image,
                                     #   z-index layering, Slidev layout:none requirements,
                                     #   v-clicks compatibility in zone divs, text contrast guarantees,
                                     #   font rendering considerations, background mismatch remediation
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
