# Improvements from Learn Iteration 6

## Applied Changes (critical + major systemic issues only)

### Change 1: Bento-grid global structural fingerprint dedup
- **File**: SKILL.md
- **Section**: Step 4.5 — "Visual structure dedup" validation
- **Type**: modify_rule
- **Description**: The current visual fingerprint dedup only checks adjacent slides. Two bento-grid slides with identical column proportions appeared on slides 4 and 12 (8 slides apart). The rule must also flag non-adjacent bento-grid/card-mosaic pairs that share the same column ratio globally.
- **Before**: `"Two-col-text, card-mosaic (2×2), and timeline-horizontal (2×2 grid) all render as "4-cell grid" visually. Count slides that will render as a 2×2 or similar grid — if >30% of content slides share this visual pattern, replace excess with non-grid archetypes (asymmetric-split, stat-hero, quote-pull, bento-grid with asymmetric sizing)."`
- **After**: Add to the end of that paragraph: `"Additionally, when two bento-grid slides share the same column ratio (e.g., both use 1.25fr/1fr), alternate the ratio: if slide A uses 1.25fr/1fr (featured-left), slide B must use 1fr/1.25fr (featured-right). This creates mirror variation that reads as intentional, not accidental. Apply globally across all bento-grid instances in the deck, not just adjacent ones."`

### Change 2: Section-divider left-aligned variant lower anchor
- **File**: SKILL.md
- **Section**: Step 4.5 — "Section divider differentiation"
- **Type**: modify_rule
- **Description**: The left-aligned section divider variant (B) produces a large empty lower third when content is placed in the upper 40-50% of the slide. A structural lower-anchor element is needed.
- **Before**: `"(B) left-aligned heading at 3.5rem+ with a large decorative number or geometric shape on the right side"`
- **After**: `"(B) left-aligned heading at 3.5rem+ with a large decorative number or geometric shape on the right side, PLUS a tertiary lower anchor: either (i) a row of section-count pills at bottom-left ('Раздел 1 из 3 · 3 слайда'), or (ii) a progress indicator row with 3 dots (filled=current, empty=future). This grounds the lower third and transforms the empty space into intentional navigation cues."`

## Deferred (minor issues — logged for review)

- **Slide 13 asymmetric layout rows** — The 3-row grid uses `grid-template-rows:1fr 1fr 1fr` but the heading is not inside the grid, resulting in tight visual spacing. Using `gap:14px` instead of `12px` would add breathing room. (Too cosmetic to auto-apply.)
- **CTA pre-slide bridge** — Slide 14 (Support) should ideally be on bg-alt as a bridge before the teal CTA. However, changing the bg-level of slide 14 would require also adjusting the icon-ghost container (which would become invisible on bg-alt). Requires manual review.
- **Burndown chart mini bars** — The CSS bar mockup on slide 12 has bars as thin as 8px width each. Increasing to 12px minimum width would make the decorative chart more readable. Minor aesthetic improvement.
- **Slide 10 heading line count** — "Документация живёт / рядом с задачами" wraps to 4 lines at 3rem in a 3fr column. Reducing to 2.7rem would fit in 3 lines. Minor.
