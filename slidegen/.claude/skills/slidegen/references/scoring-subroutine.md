# Scoring Subroutine

A reusable subroutine for scoring presentation slide images on design quality. Called by `--polish`, `--learn`, and `--compare`.

**Input:** `<dir>` — project directory containing `slides/slide-*.png`

**Important:** Scores are Claude's subjective visual assessment of the generated PNG images, not deterministic metrics. Used for relative comparison within a single session.

## Process

Read EVERY PNG from `<dir>/slides/`. For each slide, evaluate and score 1-10 on 6 axes:

| Axis | What to evaluate | Low (1-3) | Below threshold (4-5) | Acceptable (6-7) | Good (8-9) | Exceptional (10) |
|---|---|---|---|---|---|---|
| Visual Impact | First impression, memorability, "wow" factor | Forgettable, generic, looks auto-generated | Recognizable as a presentation but not striking | Decent presentation quality, professional enough | Would stand out in a conference, visually polished | Could be showcased as a design reference |
| Layout Uniqueness | Structural difference from neighboring slides | Same composition as adjacent slides | Minor variation (same layout, different content) | Noticeably different composition from neighbors | Clearly distinct, creative layout approach | Surprising, inventive composition |
| Typography Drama | Scale contrast, readability, hierarchy | Everything same size, poor readability, garbled text | Some hierarchy but weak contrast, text hard to read | Clear heading/body distinction, fully readable | Strong 3+ scale levels, text is crisp and clear | Hero elements pop, beautiful type treatment |
| Color Conviction | Bold intentional palette, consistency | Random or clashing colors, no palette coherence | Palette exists but timid, washed out | Consistent palette, clear accent usage | Bold, purposeful, memorable color choices | Palette tells a story, perfectly balanced |
| Content Clarity | Main message readable in 3 seconds | Cluttered, competing elements, text unreadable | Message findable but requires effort | Message clear on first glance | Instant comprehension, perfect information density | Information hierarchy is effortless |
| Decorative Quality | Visible decorative elements, personality | No personality, flat/empty background | Some decoration but generic or distracting | Appropriate decorations that add character | Decorations enhance the message and brand | Decorative layer is distinctive and cohesive |

## Output

Write score report to `<dir>/score-report.md`:

```markdown
# Score Report

Generated: <timestamp>
Provider: <provider> / <model>
Mode: <reference|no-reference>

## Per-Slide Scores

| Slide | Role | Impact | Layout | Typo | Color | Clarity | Decor | AVG |
|-------|------|--------|--------|------|-------|---------|-------|-----|
| 1     | cover | 8     | —      | 7    | 8     | 9       | 7     | 7.8 |
| 2     | content | 7  | 6      | 8    | 7     | 8       | 6     | 7.0 |
| ...   | ...  | ...    | ...    | ...  | ...   | ...     | ...   | ... |

**Layout Uniqueness note:** Slide 1 (cover) is scored "—" for Layout Uniqueness because it has no previous slide to compare against. It is excluded from the Layout Uniqueness average.

## Overall Score: X.X / 10

## Weakest Slides (avg < 7)
- Slide N: avg X.X — [axis] is low because [reason]

## Strongest Slides (avg >= 9)
- Slide N: avg X.X — [what makes it strong]

## Slides Below Threshold (any axis < 6)
- Slide N: [axis] scored X — [reason] — **candidate for regeneration**
```

## Thresholds

- **Any single axis < 6** → slide is a regeneration candidate (per-axis gate)
- **Slide avg < 7** → weak (candidate for redesign in `--polish`)
- **Slide avg >= 9** → strong (do not touch in `--polish`)
- **Overall avg >= 9** → consider early exit from polish cycle
