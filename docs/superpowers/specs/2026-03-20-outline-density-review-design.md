# Outline: Information Density Review

**Date:** 2026-03-20
**Scope:** Extend default preset's reviewer and generator with text density checks

## Problem

The default outline reviewer checks logical flow, clarity, coverage, pacing, single-message-per-slide, and opening/closing — but does not validate information density. Slides can end up overloaded with text (too many bullets, long sentences, paragraph-style content) which hurts presentation quality.

## Solution

Synchronized update to both generator and reviewer in the default preset.

### 1. Generator (`default-generator.md`)

Add three density rules to `Structure Quality Rules`:

```markdown
- **5-7 bullets max per slide** — if you need more, split into two slides
- **Concise bullets** — each bullet is 10-12 words max; it's a cue, not a sentence
- **No text walls** — if a slide reads like a paragraph, it needs restructuring
```

These rules are appended after the existing 7 rules. The generator will produce structures that respect density limits from the first iteration, reducing the number of review cycles needed.

### 2. Reviewer (`default-reviewer.md`)

Add evaluation criterion #7 after the existing 6 criteria:

```markdown
### 7. Information Density
- Does each slide have no more than 5-7 bullet points?
- Is each bullet concise (10-12 words max), serving as a cue rather than a full sentence?
- Are there slides that look like text walls (dense paragraphs instead of structured points)?
- If a slide exceeds density limits, can it be split into two or trimmed without losing meaning?
```

The reviewer will flag density violations in `NEEDS_REVISION` feedback with specific slide references and actionable suggestions.

## Files Changed

| File | Change |
|------|--------|
| `outline/.claude/skills/outline/assets/default/agents/default-generator.md` | Add 3 density rules to Structure Quality Rules |
| `outline/.claude/skills/outline/assets/default/agents/default-reviewer.md` | Add criterion #7 Information Density |

## Design Rationale

- **Why both files?** Generator producing dense content that reviewer then rejects wastes iteration cycles. Teaching both sides the same limits is more efficient.
- **Why numerical limits?** "One key idea per slide" is already in the generator but is too abstract for density. Concrete limits (5-7 bullets, 10-12 words) give the LLM clear thresholds to check against.
- **Why not a separate agent?** A new agent would add pipeline complexity and an extra subagent dispatch. The reviewer already evaluates structure quality — density is a natural extension of that responsibility.
