# Design Memory

Persistent memory of design patterns and their effectiveness. Stores what worked and what failed across presentations to inform future unique/custom style generation.

## Storage

File: `~/.claude/slidev-design-memory.json`

## JSON Structure

```json
{
  "version": 1,
  "max_entries": 50,
  "entries": [
    {
      "date": "YYYY-MM-DD",
      "topic": "presentation topic",
      "overall_score": 8.5,
      "fonts": {
        "sans": "Font Name",
        "serif": "Font Name",
        "mono": "Font Name"
      },
      "colorSchema": "dark",
      "palette_mood": "short description of color feeling",
      "accent_color": "#hexcolor",
      "decorative_motifs": ["motif1", "motif2"],
      "layout_rotation": ["layout-type-1", "layout-type-2"],
      "card_styles_used": ["solid", "accent", "glass"],
      "what_worked": "Description of what made this design effective (or null)",
      "what_failed": "Description of what didn't work (or null)",
      "type": "high | low"
    }
  ]
}
```

## Write Protocol

**Called after:**
- `--polish` completes (POL-8 in `references/polish-procedure.md`)
- `--learn` iteration completes (after L-3e apply improvements)

**Process:**
1. Read `~/.claude/slidev-design-memory.json`. If file doesn't exist, create with:
   ```json
   { "version": 1, "max_entries": 50, "entries": [] }
   ```
2. Build entry from current project:
   - `date`: today's date
   - `topic`: derived from presentation title in slides.md headmatter
   - `overall_score`: from score-report.md (overall)
   - `fonts`, `colorSchema`: from slides.md headmatter
   - `palette_mood`: short description of the color feeling (Claude's assessment)
   - `accent_color`: from `--color-accent` in styles/index.css
   - `decorative_motifs`: from `.decor-*` class names in styles/index.css
   - `layout_rotation`: distinct layout types used across slides
   - `card_styles_used`: card variant class names used
   - `what_worked` / `what_failed`: Claude's assessment of why the design scored high/low
   - `type`: `"high"` if score >= 8, `"low"` if score < 6, **skip write entirely** if 6-8 (not distinctive enough)
3. If `entries.length >= 50`: remove the oldest entry (first in array — FIFO)
4. Append new entry to end of array
5. Write file

## Read Protocol

**Called during:** Design Thinking (Unique and Custom Style modes, before design decisions).

**Process:**
1. Read `~/.claude/slidev-design-memory.json` (skip silently if doesn't exist — no error)
2. From `"type": "high"` entries: note what worked. Draw inspiration but DON'T copy. Use as a "palette of proven ideas" — vary the specific implementation.
3. From `"type": "low"` entries: note what failed. **Actively avoid** these patterns.

**CRITICAL**: Memory informs but doesn't constrain. Unique mode must still produce unique designs.

Example: If memory says "gold accent on navy works well", don't always use gold on navy. Extract the PRINCIPLE (strong warm accent on cool dark base) and vary the implementation (amber on charcoal, copper on midnight blue, etc.).
