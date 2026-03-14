# Preset Format Specification

Presets are `.preset.md` files that define reusable design configurations for SlideCraft presentations. Each preset captures both the **visual layer** (AI image generation) and the **text layer** (Slidev CSS/positioning) configuration.

## File Structure

A preset file consists of YAML frontmatter followed by two body sections: an aesthetic description and a style suffix block.

```markdown
---
name: preset-name
colorSchema: dark
fonts:
  sans: Outfit
  serif: Source Serif 4
  mono: JetBrains Mono
aspectRatio: 16/9
transition: slide-left
accent_color: "#4f8ef7"
mood: professional
palette: "navy, indigo, cyan accent"
zone_strategy: text-left-60
text_color: "#ffffff"
text_contrast_mode: light-on-dark
---

Free-text aesthetic description guiding design decisions for BOTH layers.
Describe the mood, visual metaphors, background textures, geometric elements,
and how text zones should relate to the background composition.

Also describe: where visual focal points land relative to text zones, what
contrast approach works for this palette, and any zone-specific notes
(e.g., "stat slides use centered single zone; content slides use left 60% zone").

## Style Suffix

The style suffix below is appended to every AI image generation prompt.
It defines the visual layer's core aesthetic — keep it text-free and zone-aware.

```
Dark gradient background from navy (#0d1b3e) to indigo (#1e1b4b).
Geometric accent shapes in the right 35% — subtle grid lines, angular cards.
Cyan accent (#4f8ef7) used for borders and glow effects.
Left 60% of the slide kept visually clear (low texture) for text overlay.
No text, labels, or lettering in the image. Photorealistic quality.
Professional, modern enterprise aesthetic.
```
```

## Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique preset identifier (kebab-case) |
| `colorSchema` | No | `light`, `dark`, or `auto`. Default: `auto` |
| `fonts.sans` | No | Primary sans-serif font (Google Fonts) |
| `fonts.serif` | No | Serif font for accents/headings |
| `fonts.mono` | No | Monospace font for code blocks |
| `aspectRatio` | No | Slide aspect ratio. Default: `16/9` |
| `transition` | No | Default slide transition |
| `accent_color` | No | Primary accent color (hex) — used in CSS overlays |
| `mood` | No | Visual mood descriptor (professional, bold, playful, etc.) |
| `palette` | No | Short color description for design memory |
| `zone_strategy` | No | Default zone placement: `text-left-60`, `text-center`, `text-right-60`, `split-40-60` |
| `text_color` | No | Default text color for all zones (hex or CSS value) |
| `text_contrast_mode` | No | `light-on-dark` or `dark-on-light` — drives contrast remediation logic |

**Removed from slidegen/slidev presets:** `background` — AI PNGs replace static background images entirely.

**Kept from slidev presets:** `colorSchema`, `fonts`, `aspectRatio`, `transition`, `accent_color`.

## Body Sections

### 1. Aesthetic Description (plain text)

Free-form text describing the visual direction for **both layers**:
- Background visual style (textures, geometry, gradient direction)
- How background composition relates to text zone placement
- Contrast approach for this palette
- Zone-specific notes (centered stat slides, split-content slides, etc.)

This is used during Design Thinking to make layout decisions not covered by frontmatter.

### 2. Style Suffix Block (fenced code block, REQUIRED)

A ```` ``` ```` fenced block containing the style suffix appended to every AI image generation prompt. Rules:
- **No text in image** — the suffix must reinforce that the PNG contains no rendered text
- **Zone clarity** — describe which screen regions are visually clear for text overlay
- **Palette specifics** — hex values help reproducibility
- **No layout markup** — this is a natural language prompt fragment, not CSS

## Preset Lookup Order

When resolving `--preset <name>`:

1. **Direct path**: If `<name>` is a file path (contains `/` or `\` or ends in `.md`), read directly
2. **Local**: Check `./.slidecraft-presets/<name>.preset.md` (current project directory)
3. **Global convention**: Look for `~/.claude/slidecraft-presets/<name>.preset.md`

Local presets take priority over global ones, allowing project-specific overrides.

If none found, emit an error listing all paths tried.

## Storage Locations

Presets can be stored in two locations:

- **Global**: `~/.claude/slidecraft-presets/<name>.preset.md` — available across all projects
- **Local**: `./.slidecraft-presets/<name>.preset.md` — scoped to the current project, committed with the repo

## How Presets Are Applied

When a preset is loaded:

1. **Frontmatter values** are merged into the Slidev `slides.md` headmatter (`fonts`, `colorSchema`, `aspectRatio`, `transition`)
2. **`zone_strategy`** sets default zone layout for all slides (overridable per-slide)
3. **`text_color` / `text_contrast_mode`** sets default CSS text color in zone overlays
4. **`accent_color`** is set as `--color-accent` CSS variable
5. **Style suffix** (the fenced block) is appended to every entry in `prompts.json`

## Example: Dark Enterprise Preset

```markdown
---
name: dark-enterprise
colorSchema: dark
fonts:
  sans: Outfit
  serif: Source Serif 4
aspectRatio: 16/9
transition: fade
accent_color: "#4f8ef7"
mood: professional
palette: "navy, indigo, cyan"
zone_strategy: text-left-60
text_color: "#ffffff"
text_contrast_mode: light-on-dark
---

Enterprise technology aesthetic. Background uses a navy-to-indigo gradient
with subtle geometric grid lines. Text zones occupy the left 60% of the slide,
with the right 40% reserved for visual interest (geometric cards, glows).

Stat slides use a single centered zone with a large number at 5em.
Section dividers use a full-width center zone over a minimal background.

## Style Suffix

```
Dark gradient from navy (#0d1b3e) to indigo (#1e1b4b). Subtle geometric grid
in the right 35% with angular cards and cyan (#4f8ef7) glow borders.
Left 60% visually clear — low texture, no shapes — reserved for text overlay.
No text, labels, or lettering anywhere in the image.
Cinematic lighting, professional enterprise aesthetic, 4K quality.
```
```
