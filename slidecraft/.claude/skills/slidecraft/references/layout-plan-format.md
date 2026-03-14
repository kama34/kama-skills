# Layout Plan Format

The layout plan (`layout-plan.json`) is the coordination layer between AI image generation and Slidev text overlay. It defines where text zones are placed on each slide.

## JSON Schema

```json
{
  "slides": [
    {
      "slide": 1,
      "role": "cover",
      "zones": [],
      "visual_description": "English description of visual elements for AI",
      "prompt_hint": "Auto-generated empty-zone instructions for AI"
    }
  ]
}
```

## Zone Object

```json
{
  "id": "heading",
  "type": "heading",
  "text": "Заголовок",
  "items": null,
  "position": {
    "x": "10%",
    "y": "35%",
    "w": "80%",
    "h": "15%"
  },
  "style": {
    "fontSize": "3em",
    "fontWeight": "bold",
    "color": "white",
    "textAlign": "center",
    "lineHeight": "1.2"
  }
}
```

**Fields:**
- `id` — unique identifier within slide (e.g., "heading", "bullets", "stat-1")
- `type` — zone type (see Zone Types below)
- `text` — string content for single-text zones, null for list zones
- `items` — array of strings for `list` type zones, null for others
- `position` — coordinates as CSS percentages
- `style` — CSS styling directives for the text overlay

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
| `list` | Bullet points (uses `items` array) | Left or center, 50-65% width |
| `body` | Paragraph text | Center or left, 50-70% width |
| `stat` | Large number/metric | Center, 30-50% width |
| `quote` | Quotation text | Center, 60-80% width |
| `cta` | Call to action | Bottom center, 50-70% width |
| `caption` | Small annotation | Bottom edge, 30-50% width |

## prompt_hint Generation

For each zone, convert coordinates to an English instruction using this template:

```
"Leave the area from [x] to [x+w] horizontally, [y] to [y+h] vertically completely empty —
no text, no decorative elements. Background must be uniform [dark|light] in this region."
```

**Rules:**
- Multiple zones are listed sequentially in prompt_hint
- `[dark|light]` is derived from planned text color: white/light text → zone must be dark, dark text → zone must be light
- Add at the end: "Place all decorative elements, icons, and visual details ONLY in the remaining areas outside these zones."

**Example:**
```
"Leave the area from 10% to 90% horizontally, 30% to 65% vertically completely empty — no text, no decorative elements. Background must be uniform dark in this region. Leave the area from 15% to 85% horizontally, 70% to 78% vertically completely empty — background must be uniform dark. Place all decorative elements, icons, and visual details ONLY in the remaining areas outside these zones."
```

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
