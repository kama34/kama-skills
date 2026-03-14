# Design Memory

Persistent memory of design patterns and their effectiveness across SlideCraft presentations.

**Storage:** `~/.claude/slidecraft-design-memory.json`

**Max entries: 50** — higher than slidegen's 20 because two-layer entries contain richer data (both visual and text layer metadata per entry).

## JSON Structure

```json
{
  "version": 1,
  "max_entries": 50,
  "entries": [
    {
      "date": "2026-03-14",
      "topic": "AI Product Pitch",
      "type": "success",
      "score": 8.5,
      "provider": "polza",
      "model": "google/gemini-3.1-flash-image-preview",
      "aspect_ratio": "16:9",
      "mood": "professional",
      "palette": "navy, indigo, cyan accent",
      "visual": {
        "style_suffix": "Dark gradient background, geometric cards in right 35%, navy-to-indigo gradient, no text in image...",
        "palette": "navy, indigo, cyan accent",
        "effective_patterns": [
          "geometric cards in right 35%",
          "diagonal accent stripe at bottom-left",
          "zone borders rendered as subtle glows"
        ],
        "zone_clarity": "95% — zones clean on first attempt"
      },
      "text": {
        "fonts": "Outfit + Source Serif 4",
        "positioning_accuracy": "high — no QA repositioning needed",
        "contrast_issues": false,
        "effective_patterns": [
          "h1 at 2.8rem with font-weight:700 readable on dark gradient",
          "bullet list with 1.6rem line-height fits 4-item lists cleanly"
        ]
      },
      "what_worked": "Geometric zone indicators in the PNG made CSS zone placement straightforward. Outfit at 700 weight gave clear visual hierarchy against dark backgrounds.",
      "what_failed": "First attempt at section divider slides had low Layer harmony — text zone sat over a visually busy area; fixed by adjusting the PNG prompt to keep the center-left clear."
    }
  ]
}
```

## Entry Fields

| Field | Description |
|-------|-------------|
| `date` | ISO date of the session |
| `topic` | Extracted from first slide heading or outline title |
| `type` | `success` (score >= 7), `neutral` (5-6), `failure` (< 5) |
| `score` | Overall average from score-report.md |
| `provider` / `model` | From meta.json |
| `aspect_ratio` | From meta.json |
| `mood` | Claude's assessment of the visual mood |
| `palette` | Short color description (top-level, mirrors visual.palette) |
| `visual.style_suffix` | Style suffix used for PNG generation |
| `visual.palette` | Detailed color description |
| `visual.effective_patterns` | PNG prompt patterns that produced clean zones |
| `visual.zone_clarity` | How many zones needed repositioning after QA |
| `text.fonts` | Font pair used (sans + serif) |
| `text.positioning_accuracy` | Whether CSS zones matched PNG zones on first try |
| `text.contrast_issues` | Boolean — did any text zone have contrast failures? |
| `text.effective_patterns` | CSS patterns that worked well for readability |
| `what_worked` | 1-2 sentence summary of successful dual-layer choices |
| `what_failed` | 1-2 sentence summary of unsuccessful choices |

## Write Protocol

Called after QA scoring completes and after each `--polish` iteration that reaches finalization.

1. Read `~/.claude/slidecraft-design-memory.json`. If it doesn't exist, create with empty entries array.
2. Build entry from current project:
   - `date`: current date
   - `topic`: extracted from the first slide's heading or the outline title
   - `type`: based on average score: >= 7 → `"success"`, 5-6 → `"neutral"`, < 5 → `"failure"`
   - `score`: from score-report.md
   - `provider`, `model`, `aspect_ratio`: from meta.json
   - `mood`: Claude's assessment of the visual mood
   - `palette`: Claude's short color description
   - `visual`: extract style suffix from prompts.json, palette from prompts, zone clarity from QA log
   - `text`: extract font config from slides.md frontmatter, positioning accuracy from QA log, contrast flag from scoring
   - `what_worked`: 1-2 sentence summary of successful design choices
   - `what_failed`: 1-2 sentence summary of unsuccessful choices
3. FIFO eviction: if `entries.length >= 50`, remove the oldest entry.
4. Append new entry and write file.

## Read Protocol

Called during Design Thinking (Step 3 of generation procedure), in Unique and Custom Style modes.

1. Read `~/.claude/slidecraft-design-memory.json`. Skip silently if it doesn't exist.
2. From `"success"` entries:
   - Draw inspiration from `visual.effective_patterns` — extract the PRINCIPLE, don't copy verbatim
   - Note `text.effective_patterns` for CSS patterns that aided readability
   - Note font pairings and palettes that scored well
   - Note `visual.zone_clarity` — prefer prompting patterns that yielded clean zones
3. From `"failure"` entries:
   - Actively AVOID these patterns in both layers
   - Note whether failures were in the image layer, text layer, or layer harmony
4. From `"neutral"` entries:
   - Use for context but don't prioritize

**CRITICAL:** Memory informs but doesn't constrain. Unique mode must still produce unique designs. Never reuse a style suffix verbatim from memory.
