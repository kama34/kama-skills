# Design Memory

Persistent memory of design patterns and their effectiveness across slidegen presentations.

**Storage:** `~/.claude/slidegen-design-memory.json`

## JSON Structure

```json
{
  "version": 1,
  "max_entries": 50,
  "entries": [
    {
      "date": "2026-03-14",
      "topic": "AI in Healthcare",
      "type": "success",
      "overall_score": 8.2,
      "provider": "polza",
      "model": "google/gemini-3.1-flash-image-preview",
      "aspect_ratio": "16:9",
      "style_suffix": "Dark gradient background, geometric accents, clean sans-serif...",
      "mood": "professional",
      "palette_description": "deep navy + electric blue accent",
      "prompt_patterns": [
        "Include explicit font size instructions",
        "Specify text alignment per element",
        "Always describe background gradient direction"
      ],
      "what_worked": "Detailed typography instructions produced consistent readable text",
      "what_failed": "Vague color descriptions led to inconsistent palettes across slides"
    }
  ]
}
```

## Write Protocol

Called after QA scoring completes (Phase 3, Step 6g) and after each `--learn` iteration.

1. Read `~/.claude/slidegen-design-memory.json`. If it doesn't exist, create with empty entries array.
2. Build entry from current project:
   - `date`: current date
   - `topic`: extracted from the first slide's heading or the outline title
   - `type`: based on average score:
     - Average >= 7 → `"success"`
     - Average 5-6 → `"neutral"`
     - Average < 5 → `"failure"`
   - `overall_score`: from score-report.md
   - `provider`, `model`, `aspect_ratio`: from meta.json
   - `style_suffix`: from prompts.json
   - `mood`: Claude's assessment of the visual mood
   - `palette_description`: Claude's description of the color palette used
   - `prompt_patterns`: list of prompt techniques that were effective or ineffective
   - `what_worked`: 1-2 sentence summary of successful design choices
   - `what_failed`: 1-2 sentence summary of unsuccessful design choices
3. FIFO eviction: if entries.length >= max_entries (50), remove the oldest entry.
4. Append new entry and write file.

`--learn` writes an entry after every iteration regardless of score.

## Read Protocol

Called during Design Thinking (Step 3 of generation procedure), in Unique and Custom Style modes.

1. Read `~/.claude/slidegen-design-memory.json`. Skip silently if it doesn't exist.
2. From `"success"` entries:
   - Draw inspiration but DON'T copy — extract the PRINCIPLE behind what worked
   - Note effective prompt patterns
   - Note palettes and moods that scored well
3. From `"failure"` entries:
   - Actively AVOID these patterns
   - Note prompt patterns that produced poor results
4. From `"neutral"` entries:
   - Use for context but don't prioritize

**CRITICAL:** Memory informs but doesn't constrain. Unique mode must still produce unique designs. Never reuse a style suffix verbatim from memory.
