# Improvements from Learn Iteration 10/10 (FINAL)

## Applied Changes (critical + major systemic issues only)

### Change 1: Bento-grid featured cell — icon must be ABOVE the metric, not beside it
- **File**: references/composition-archetypes.md
- **Section**: bento-grid archetype
- **Type**: modify_rule + add_example
- **Description**: The current bento-grid featured cell HTML skeleton places icon and hero number in a horizontal flex row (`display:flex;align-items:center;gap:14px`). This causes the number to sit beside the icon at reduced apparent size, violating the "place icon ABOVE the metric" rule already documented in the note. The skeleton itself must enforce this.
- **Before**: `<div style="display:flex;align-items:center;gap:14px;margin-bottom:20px;">` (icon + number in horizontal row)
- **After**: Featured cell content uses a column layout — icon first in its own row, then number below: `<div style="display:flex;flex-direction:column;align-items:flex-start;margin-bottom:16px;">` with icon div then number div stacked vertically. Add QA check: "Scan all bento featured cells — if icon and hero number share a flex row, auto-fix to column stacking."

### Change 2: Bento-grid side cards must not duplicate featured cell numbers
- **File**: SKILL.md
- **Section**: Step 5 — bento-grid generation rules (under "Layout Diversity" note)
- **Type**: add_rule
- **Description**: When a featured bento cell contains a sub-grid of 3+ numbers (team breakdown, multi-metric), small side cards must use DIFFERENT data. The generator pulled "85 монтажников" for the bottom-left card even though "85" already appeared inside the featured cell's sub-grid.
- **Before**: No rule preventing duplication between featured cell sub-grid and side cards.
- **After**: Add explicit rule: "**Bento side card dedup**: When the featured bento cell contains a sub-grid of 3+ numbers, side cards MUST use data not already shown in the sub-grid. Options: growth percentages, period comparisons, or qualitatively different metrics. NEVER repeat a number from the featured sub-grid in a side card."

### Change 3: Deck-level grid fingerprint frequency cap
- **File**: SKILL.md
- **Section**: Step 4.5 — Layout Budget Rule
- **Type**: add_rule
- **Description**: The Layout Budget Rule checks consecutive slides within a 4-slide entropy window, but doesn't check the deck-level total frequency of "heading + card grid" slides. In this deck, slides 5 (card-mosaic) and 11 (timeline 2×2) both render as heading + grid, which is within tolerance for a 12-slide deck. However, the rule should explicitly state the deck-level cap.
- **Before**: Layout Budget Rule only addresses same-group within consecutive windows and >40% per group. No explicit deck-level check for the visual fingerprint "heading + grid of ≥3 cards."
- **After**: Add to Layout Budget Rule: "**Deck-level grid fingerprint cap**: Count ALL slides in the deck (consecutive or not) that render as 'heading + grid of 3+ cards' regardless of archetype name. If count > 35% of content slides (e.g., >3 in a 10-slide deck, >4 in a 12-slide deck), replace excess slides with non-grid archetypes (stat-hero, asymmetric-split, quote-pull, comparison-table with row layout)."

---

## Deferred (minor issues — logged for review)

- **Slide 1 title wraps 4 lines**: "Энергия из возобновляемых источников окупается за 3 года" at 3.4rem creates 4 text lines. Could add a `<br>` after "источников" for a 3-line layout. Minor — readability unaffected.
- **Two-col comparison column headers**: For comparison slides, a more prominent column header treatment (bottom border line, larger font) would improve clarity. Consider adding a "comparison mode" variant to the two-col-text archetype skeleton.
- **Concentric circles inner ring opacity**: Section divider decorative circles at `rgba(255,255,255,0.10)` are barely visible on teal bg-accent at export resolution. Minimum should be 0.14. Apply same opacity floor as ghost numbers.
- **Arc decoration visibility**: Arcs at bottom-left with `border:6px solid rgba(accent,0.55)` are partially clipped. Consider increasing border-width to 8px for better visibility when the arc is partially outside the slide boundary.
