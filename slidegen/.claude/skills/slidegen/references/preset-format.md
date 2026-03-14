# Preset Format

Presets are `.preset.md` files defining reusable prompt templates for consistent visual style across generations.

## File Structure

YAML frontmatter + body (prompt template with placeholders).

```yaml
---
name: corporate-dark
description: Dark corporate theme with blue accents
mood: professional, clean
palette: "dark background (#1a1a2e), white text, blue accent (#0066ff)"
typography: "modern sans-serif, large headings, minimal text"
decoration: "subtle gradient overlays, thin line separators"
aspect_ratio: "16:9"
---

Generate a 16:9 aspect ratio presentation slide with dark navy background (#1a1a2e).
Use clean modern sans-serif typography, white text for headings (approximately 48pt),
light gray (#e0e0e0) for body text (approximately 24pt). Electric blue (#0066ff) accent
for highlights, decorative lines, and emphasis elements. Subtle gradient overlay from
navy to deep purple in bottom-right corner. Thin horizontal line separators between
sections.
{{SLIDE_CONTENT}}
{{SLIDE_ROLE}}
```

## Frontmatter Fields

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Preset identifier (kebab-case) |
| `description` | No | Human-readable description (recommended) |
| `mood` | Yes | Visual mood keywords |
| `palette` | Yes | Color palette description with hex values |
| `typography` | Yes | Typography personality description |
| `decoration` | Yes | Decorative element description |
| `aspect_ratio` | No | Default: "16:9" |

## Placeholders

The prompt template body MUST include these placeholders:

### `{{SLIDE_CONTENT}}`

Replaced at generation time with the slide's text content. Example substitution:

> Heading text reads "Market Overview". Three bullet points: "• $4.2B market size", "• 23% growth", "• 3 competitors". Each bullet has a small relevant icon to its left.

### `{{SLIDE_ROLE}}`

Replaced at generation time with the slide role description:

| Role | Substitution text |
|---|---|
| `cover` | "This is a cover/title slide — prominent title, minimal body text" |
| `section` | "This is a section divider slide — section heading, transitional" |
| `content` | "This is a content slide — heading with body text, bullets, or key points" |
| `stat` | "This is a statistics/data slide — large numbers, charts, or key metrics" |
| `quote` | "This is a quote slide — prominent quotation with attribution" |
| `comparison` | "This is a comparison slide — two or more items side by side" |
| `end` | "This is a closing/thank-you slide — call to action or contact info" |

## Storage Locations

- **Global:** `~/.claude/slidegen-presets/<name>.preset.md`
- **Local:** `./.slidegen-presets/<name>.preset.md`

## Lookup Order

When `--preset <name>` is used:

1. **Direct path**: if `<name>` is a file path, use it directly
2. **Local**: `./.slidegen-presets/<name>.preset.md`
3. **Global**: `~/.claude/slidegen-presets/<name>.preset.md`

First match wins. If not found, print error with available presets:
```
Preset "<name>" not found.

Available presets:
  Local:  corporate-dark, minimal-light
  Global: tech-blue, warm-gradient
```
