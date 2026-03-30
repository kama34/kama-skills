# Figma Extraction Procedure

Extract a Figma presentation template into a preset with archetypes. Called when `/figmadeck <URL>` is used.

All output is namespaced as `figmadeck-<name>-*` — never use `figma-<name>-*`.

---

## FIG-1: File Structure Reconnaissance

Use `mcp__figma__use_figma` (Plugin API) to run JavaScript that traverses the node tree on the target page:

```javascript
// Pseudocode for the JS to run via use_figma:
// 1. Get the target page (by nodeId or first page)
// 2. Iterate page.children — find all FRAME nodes
// 3. Filter: abs(width/height - 16/9) < 0.05 * (16/9)  (aspect ratio ~16:9 ±5%)
// 4. Sort by y position (top to bottom), then x (left to right)
// 5. Return: [{id, name, width, height, index}]
```

**Result**: ordered list of slide frames.

- If 0 frames found → error: `No slides found (frames with ~16:9 aspect ratio). Check file structure.`
- If > 20 frames → take first 20, warn: `Found <N> slides, using first 20 (maximum for extraction).`

---

## FIG-2: Global Style Extraction

For ALL slide frames, collect design statistics via `mcp__figma__use_figma` (Plugin API). Run a single JS call that traverses all children recursively and collects:

### Colors

Group all `fills` by frequency:

- Frame background fills (direct children fills covering full area) → most frequent = `--bg-base`, second = `--bg-alt`
- Small bright-colored elements (used in <20% of nodes) → `--color-accent`
- Text node colors by frequency → most frequent = `--color-text`, second = `--color-muted`
- Derive `--color-accent-rgb` (R,G,B triple), `--bg-accent` (accent at 12% opacity over bg-base)
- **AI Color Blacklist check**: if accent hue 240–290 at saturation >50% → shift to nearest safe hue (teal #0D9488, amber #D97706, emerald #059669, rose #E11D48). Log replacement.

### Fonts

Collect all `fontFamily`, `fontSize`, `fontWeight` from text nodes:

- Heading font: most frequent fontFamily in nodes with fontSize ≥ 24px → `fonts.sans`
- Body font: most frequent fontFamily in nodes with fontSize < 24px → `fonts.body`
- **Serif check**: if either font is serif → find nearest sans-serif equivalent. Log: `Font "<name>" (serif) → "<replacement>" (sans-serif)`

### Spacing

Collect from auto-layout frames:

- Median `itemSpacing` across all auto-layout frames → standard gap
- Median `paddingLeft` / `paddingTop` → base padding

### Shapes

Collect `cornerRadius` values:

- Median cornerRadius of frames with width 100–400px (card-sized) → `card_radius`
- Nodes with cornerRadius ≥ 50% of min(width, height) → `icon_container: circle`
- Nodes with cornerRadius 8–16px → `icon_container: rounded-square`

### Effects

Collect `effects` array:

- Drop shadows → extract offset, blur, color for aesthetic description
- Background blurs → note in aesthetic section

**Output**: convert all collected data into `.preset.md` format per `references/preset-format.md` (YAML frontmatter + aesthetic description + CSS block with `:root` variables).

---

## FIG-3: Per-Slide Extraction

For each slide frame from FIG-1, extract four levels of data:

### Level 1 — Screenshot (visual reference)

- Call `mcp__figma__get_design_context(nodeId, fileKey)` → returns screenshot inline + React+Tailwind code
- Call `mcp__figma__get_screenshot(nodeId, fileKey)` → returns screenshot URL. Download via WebFetch and save to `figmadeck-<name>-figma/slide-<N>-<name>/reference.png` — this is the persistent visual reference used as fallback when Figma API is unavailable during learning cycles.
- Save React+Tailwind code as code hint for layout understanding

### Level 2 — Structure (positions and sizes)

- Call `mcp__figma__get_metadata(nodeId, fileKey)` → XML with node IDs, layer types, names, positions, sizes
- Parse into a structured list: `[{name, type, x, y, width, height, children: [...]}]`

### Level 3 — Detailed properties (exact CSS values)

Call `mcp__figma__use_figma` with JS that for each child element (recursive, max depth 3) extracts:

- `fills` (array of paint objects), `strokes`, `effects` (shadow, blur)
- `fontSize`, `fontFamily`, `fontWeight`, `lineHeight`, `letterSpacing`
- `layoutMode` (HORIZONTAL/VERTICAL/NONE), `itemSpacing`, `paddingLeft/Right/Top/Bottom`
- `constraints`, `layoutAlign`, `layoutGrow`, `layoutSizingHorizontal/Vertical`
- `cornerRadius`, `opacity`
- `characters` (text content — for determining which elements become slots)
- `type` (TEXT, FRAME, RECTANGLE, ELLIPSE, etc.)

Save as `blueprint.json` in `figmadeck-<name>-figma/slide-<N>-<name>/blueprint.json`:

```json
{
  "slideIndex": 1,
  "slideName": "Cover",
  "frameWidth": 1440,
  "frameHeight": 810,
  "elements": [
    {
      "name": "Title",
      "type": "TEXT",
      "x": 120, "y": 280, "width": 1200, "height": 80,
      "fontSize": 48, "fontFamily": "Inter", "fontWeight": 700,
      "lineHeight": 1.1, "letterSpacing": -0.02,
      "fills": [{"type": "SOLID", "color": "#1A1A2E"}],
      "characters": "Presentation Title Here",
      "slot": "TITLE"
    },
    {
      "name": "Card Container",
      "type": "FRAME",
      "x": 120, "y": 400, "width": 1200, "height": 300,
      "layoutMode": "HORIZONTAL", "itemSpacing": 24,
      "paddingLeft": 0, "paddingTop": 0,
      "cornerRadius": 0,
      "children": [
        {
          "name": "Card 1",
          "type": "FRAME",
          "x": 0, "y": 0, "width": 384, "height": 300,
          "cornerRadius": 12,
          "fills": [{"type": "SOLID", "color": "#F5F5F0"}],
          "layoutMode": "VERTICAL", "itemSpacing": 12,
          "paddingLeft": 24, "paddingTop": 24,
          "children": ["..."]
        }
      ]
    }
  ]
}
```

### Level 4 — Code hint

Already obtained in Level 1 via `get_design_context` — the React+Tailwind code. Used as supplementary hint for understanding grid structure (flex vs grid, column ratios).

---

## FIG-4: Archetype Conversion

From FIG-3 data, for each slide, build a composition archetype.

### Step 4-pre: Deduplication

Before converting, group slides by layout similarity. Two slides are **duplicates** (merged into one archetype) ONLY if ALL of the following match exactly:

1. Same number of direct children at the top level
2. Same `layoutMode` (HORIZONTAL/VERTICAL/NONE) on the root frame
3. Same grid structure (column/row count, same fr ratios ±5%)
4. Same element type sequence (TEXT, FRAME, FRAME, TEXT vs TEXT, FRAME, TEXT, FRAME = different)
5. Same nesting depth

If ANY detail differs — different spacing, different element sizes, different decorative elements, different number of sub-elements inside cards, different background treatment — they are **separate archetypes**. Err on the side of keeping more archetypes. Name duplicates: first occurrence becomes the archetype, others reference it via `duplicateOf` in `source.json`.

**Image-only and decoration-only slides** (no text children, only images/shapes/fills): these are NOT skipped. Create archetypes with `{{IMAGE}}` or `{{BACKGROUND}}` slots. Content type: `visual-break`. Slots: `{{IMAGE_URL}}` for the primary image area, optionally `{{CAPTION}}` if small text is present.

### Step 4a: Content Type Detection

Analyze elements in the blueprint using these heuristics:

| Pattern | Content type |
|---------|-------------|
| First slide, large heading (fontSize ≥ 36px) + subtitle + minimal other content | `intro` |
| Last slide with button-like element or CTA text | `cta` |
| 1–2 very large numbers (fontSize ≥ 48px) + small label | `metric` |
| 3+ similarly-sized child frames in a row/grid | `scope` or `credentials` |
| Circular image containers + text blocks | `team` |
| Ordered steps or numbered items | `process` |
| One large heading + one paragraph, minimal decoration | `vision` |
| No text, only images/shapes/fills | `visual-break` |
| Unrecognized pattern | `context` |

### Step 4b: HTML Skeleton

Convert Figma layout to HTML with `{{SLOT}}` markers:

**Layout mapping:**

- **Auto-layout HORIZONTAL** → `display:flex; flex-direction:row; gap:<itemSpacing>px`
- **Auto-layout VERTICAL** → `display:flex; flex-direction:column; gap:<itemSpacing>px`
- **No auto-layout (absolute positioning)** → `position:relative` container with `position:absolute` children
- **Nested frames** → nested `<div>` elements. **Max 3 levels** — if deeper, flatten (merge intermediate frames' styles into parent or child). Log: `Slide <N>: nesting flattened from <X> to 3 levels`

**Slot naming convention:**

- Single heading → `{{TITLE}}`
- Single subtitle/paragraph → `{{SUBTITLE}}` or `{{DESCRIPTION}}`
- Items in repeated grid → `{{CARD_1_TITLE}}`, `{{CARD_1_DESC}}`, `{{CARD_2_TITLE}}`, etc.
- Large number → `{{METRIC_VALUE}}`
- Small label above metric → `{{METRIC_LABEL}}`
- Primary image area → `{{IMAGE_URL}}`
- Optional caption → `{{CAPTION}}`

**Viewport conversion** — Figma uses arbitrary coords (e.g., 1440×810), figmadeck renders at 960×540:

- Position: `figma_x / figma_frame_width * 100` → percentage
- Font size: `figma_fontSize / 16` → rem, then apply Font Size Floor: body ≥ 1.25rem, heading ≥ 2.2rem, label ≥ 0.65rem
- Spacing (gap, padding): `figma_px / 16` → rem
- Proportions (width ratios between siblings) → preserved as fr units or percentages

Wrap entire skeleton in:

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:...">
  <!-- archetype content here -->
</div>
```

All slides use `layout: none` + `.slidev-layout { padding: 0 !important; overflow: hidden; }`.

### Step 4c: Flexibility Rules

For each archetype, generate a `flexibility.yaml` stored alongside the archetype:

```yaml
archetype: figmadeck-<name>
content_type: <detected type from step 4a>
figma_source:
  nodeId: "<nodeId>"
  name: "<frame name from Figma>"

slots:
  title:
    max_length: <estimated from text box width: width_px / avg_char_width>
    overflow: shrink-font     # shrink-font | truncate | wrap
  cards:                       # only if repeated elements detected
    count_in_figma: <N>
    min: <max(2, N-1)>
    max: <N+2>
    scaling: grid-auto         # grid-auto (change columns) | wrap (overflow row) | stack (vertical)

layout:
  grid_columns: flexible       # flexible (can change col count) | fixed (exact match required)
  preserve:                    # IMMUTABLE — must match Figma
    - spacing-ratio
    - font-size-hierarchy
    - color-usage
    - border-radius
  flexible:                    # ADAPTABLE — can change to fit content
    - column-count
    - card-count
    - text-length
```

---

## FIG-5: Preset Assembly

Assemble all outputs into a complete preset.

### Directory Structure

```
.slidev-presets/
  figmadeck-<name>.preset.md               # global style + CSS (from FIG-2)
  figmadeck-<name>-theme/                   # Slidev theme directory
    package.json
    styles/index.css
    layouts/none.vue
    layouts/default.vue
    layouts/cover.vue
    layouts/section.vue
    layouts/end.vue
  figmadeck-<name>-figma/                   # Figma reference data
    source.json                             # file metadata + node index
    slide-1-<name>/
      blueprint.json                        # element properties (FIG-3 Level 3)
      archetype.html                        # HTML skeleton with {{SLOT}} (FIG-4b)
      flexibility.yaml                      # scaling rules (FIG-4c)
    slide-2-<name>/
      blueprint.json
      archetype.html
      flexibility.yaml
    ...
```

### Preset Frontmatter

Add `figma` section to the standard preset YAML:

```yaml
---
name: figmadeck-<name>
figma:
  fileKey: "<fileKey>"
  sourceUrl: "<full Figma URL>"
  extractedAt: "<ISO 8601 timestamp>"
  slideCount: <N>
  archetypes:
    - id: figmadeck-<slide-1-name>
      nodeId: "<nodeId>"
      contentType: <detected type>
    - id: figmadeck-<slide-2-name>
      nodeId: "<nodeId>"
      contentType: <detected type>
# ... rest of standard preset fields (fonts, theme, colorSchema, accentColor, etc.)
---
```

### Archetypes Block

```archetypes
preferred: [figmadeck-<slide-1-name>, figmadeck-<slide-2-name>, ...]
avoid: []
cta_style: figmadeck-<cta-slide-name>
cover_style: figmadeck-<cover-slide-name>
```

### Theme Directory

Generate from the CSS block (same as `--create-preset` step 4b): `package.json`, `styles/index.css`, layout Vue files (`none.vue`, `default.vue`, `cover.vue`, `section.vue`, `end.vue`).

### source.json

```json
{
  "fileKey": "<key>",
  "sourceUrl": "<URL>",
  "extractedAt": "<ISO 8601>",
  "figmaFrameWidth": 1440,
  "figmaFrameHeight": 810,
  "slideNodes": [
    {"index": 1, "nodeId": "1:2", "name": "Cover", "contentType": "intro"},
    {"index": 2, "nodeId": "1:3", "name": "Scope", "contentType": "scope"},
    {"index": 3, "nodeId": "1:4", "name": "Metric", "contentType": "metric"}
  ]
}
```

### Extraction Summary

Print after completing FIG-5:

```
━━━ Figma Extraction Complete ━━━
Source: <URL>
Slides extracted: <N>
Preset: .slidev-presets/figmadeck-<name>.preset.md

Archetypes:
  1. figmadeck-<name>-cover (intro) — 3 slots, absolute layout
  2. figmadeck-<name>-scope (scope) — 5 slots, 3-col grid
  3. figmadeck-<name>-metric (metric) — 2 slots, centered
  ...

Fonts: <heading font> + <body font>
Palette: <bg-base> / <accent> / <text>
```

---

## Error Handling

| Situation | Behavior |
|-----------|----------|
| URL not `figma.com/design/` | Error, stop |
| No file access | Error, stop |
| No 16:9 frames found | Error: `No slides found (frames with ~16:9 aspect ratio). Check file structure.` |
| > 20 slides | Take first 20, warn user |
| Nesting > 3 levels | Flatten during extraction, log |
| Serif font detected | Replace with sans-serif, log |
| Accent hue in blacklist (240–290, sat >50%) | Shift hue, log replacement |
| Figma API unavailable during later learning cycles | Use cached `blueprint.json` + `reference.png` |
