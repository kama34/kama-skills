# Improvements from Learn Iteration 7

## Applied Changes (major systemic issues only)

### Change 1: bento-grid featured cell — stat metric minimum size rule
- **File**: references/composition-archetypes.md
- **Section**: ### bento-grid — description block
- **Type**: add_rule
- **Description**: Featured card in bento-grid must have primary metric ≥3.5rem, with icon placed above the number (not beside it). Side-by-side icon+number shrinks the number visually and defeats the "featured" hierarchy.
- **Before**: "**Use when:** 3-5 items of varying importance — one featured, others supporting."
- **After**: "**Use when:** 3-5 items of varying importance — one featured, others supporting. **CRITICAL**: Featured card primary metric MUST be ≥3.5rem — place icon ABOVE the metric in a separate row, NOT beside it. Side-by-side icon+number shrinks the number and defeats featured-card hierarchy."

### Change 2: two-col-text / asymmetric-split — heading length cap
- **File**: SKILL.md
- **Section**: Step 5 — FONT SIZE FLOOR block
- **Type**: add_rule
- **Description**: For split-layout archetypes, headings longer than 50 characters must be reduced to 2.0–2.1rem AND the text shortened to fit ≤2 visual lines. Prevents heading from consuming >20% of slide vertical space and compressing the content area.
- **Before**: (no rule for split-layout heading length)
- **After**: Add after "Hero/stat numbers: ≥4rem" line: "Split-layout heading cap: two-col-text and asymmetric-split archetypes — if heading exceeds 50 characters, reduce font-size to 2.0–2.1rem AND shorten text to ≤2 visual lines. Move secondary detail to card content, not heading."

### Change 3: bg-alt — arc/border decorations use dark color, not teal
- **File**: SKILL.md
- **Section**: Step 5 point 8 (Apply Decorative Layer) — bg-alt special case paragraph
- **Type**: modify_rule
- **Description**: On bg-alt slides, border/arc decorations should use var(--color-text) at 0.15–0.20 opacity instead of teal, because dark-on-warm-gray has higher luminance contrast than teal-on-warm-gray. Filled glows remain teal.
- **Before**: "Alternatively, use a contrasting decorative color (e.g., dark text color at 0.15 opacity instead of accent color) for better differentiation on warm surfaces."
- **After**: "**RULE — bg-alt arc/border color**: On bg-alt slides, arc and border stroke decorations MUST use `rgba(var(--text-rgb), 0.15)` (dark color, not teal) — dark-on-warm-gray creates stronger luminance contrast than teal-on-warm-gray. Filled radial glows (background property) remain teal. Pattern: arcs/border strokes → dark color 0.15–0.20 opacity; glows/dot fills → teal rgba(var(--accent-rgb), 0.35+)."

## Deferred (minor issues — logged for review)
- Profile-grid 4+footer: need explicit height convention for full-span bottom row (72px = stat-footer-band height). Minor — not systemic enough to require immediate rule change.
- Slide 6 focal gravity clustering (slides 6-8 all left-dominant): existing adjacent gravity audit rule should catch this. Deferred — no new rule needed, current rule not followed in this specific case.
- "100 к" abbreviation ambiguity: Russian notation edge case. Not systemic.
- Timeline Q3 cell density: 3-line wrap in tight grid. Minor.
