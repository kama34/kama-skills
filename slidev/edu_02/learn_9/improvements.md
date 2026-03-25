# Improvements from Learn Iteration 9/10

## Applied Changes (major systemic issues only)

### Change 1: Icon-trio 4+ items should use 2-row grid
- **File**: references/composition-archetypes.md
- **Section**: icon-trio → Use when / Visual
- **Type**: modify_rule, add_example
- **Description**: When icon-trio has 4+ items, horizontal single-row layout creates uneven text wrapping and cramped spacing. Rule should recommend 2×2 grid for 4 items.
- **Before**: `**Use when:** 3-5 features, benefits, or capabilities to present with icons.`
- **After**: `**Use when:** 3-5 features, benefits, or capabilities to present with icons. For 4+ items prefer 2×2 grid layout (2 rows × 2 columns) instead of a single horizontal row — single-row 4+ items causes cramped spacing and uneven text wrapping. Limit item descriptions to 8 words max when forced to use single-row.`

### Change 2: Consecutive grid-group slides must differ visually
- **File**: SKILL.md
- **Section**: Step 4.5, Visual structure dedup
- **Type**: modify_rule
- **Description**: Two consecutive grid-group slides (bento-grid + card-mosaic) share the same top-level structural fingerprint (label-top-left + heading + card-grid-below). The rule needs to catch this.
- **Before**: `Additionally, when two bento-grid slides share the same column ratio (e.g., both use 1.25fr/1fr), alternate the ratio globally`
- **After**: `Additionally, when two bento-grid slides share the same column ratio (e.g., both use 1.25fr/1fr), alternate the ratio globally: if slide A uses 1.25fr/1fr (featured-left), slide B must use 1fr/1.25fr (featured-right). **CRITICAL — consecutive grid-group slides**: When two consecutive content slides both belong to the grid group (icon-trio, bento-grid, card-mosaic, profile-grid), they share the visual fingerprint "heading-top-left + card-grid-below" regardless of their internal card configuration. At least ONE of the two must break this pattern by: (A) using a centered heading instead of top-left, (B) placing the heading INSIDE the grid as an oversized card, or (C) changing the grid column ratio to 1.4fr+ vs 1fr to create a featured-left asymmetry. Equal-column 2×2 grids on back-to-back slides = layout monotony.`

### Change 3: 3+ section dividers must vary on background color
- **File**: SKILL.md
- **Section**: Step 4.5, Section divider differentiation
- **Type**: add_rule
- **Description**: When a deck has 3+ section dividers and all use bg-accent, the presentation produces a monotonous "solid teal every 3 slides" rhythm. Need to require at least 1 section divider to use a different background.
- **Before**: `**Section divider differentiation**: When a deck has 2+ section-divider slides, they MUST differ visually.`
- **After**: `**Section divider differentiation**: When a deck has 2+ section-divider slides, they MUST differ visually. Alternate between: (A) centered heading with radial glow (current template), (B) left-aligned heading at 3.5rem+ with a large decorative number or geometric shape on the right side, PLUS a tertiary lower anchor: either (i) a row of section-count pills at bottom-left ('Раздел 1 из 3 · 3 слайда'), or (ii) a progress indicator row with 3 dots (filled=current, empty=future). This grounds the lower third of the slide and transforms empty space into intentional navigation cues. (C) full-width heading with a horizontal accent line below. No two section slides may use the same composition variant. **CRITICAL — 3+ section dividers background variety**: When a deck has 3 or more section dividers, they MUST NOT all use the same background color. At least ONE section divider must use either: (A) bg-alt background with heading ≥4rem (compensating for lighter bg with oversized type), or (B) bg-accent with a 15-25% black overlay (creates a perceptibly darker teal vs the clean bg-accent), or (C) the asymmetric panel variant (dark diagonal fills 40%+ of slide area, creating a two-tone effect). Goal: if someone flips through only the section divider slides, each should feel visually distinct in color/value, not just layout.`

## Deferred (minor issues — logged for review)
- Slide 13 lower-half empty gap — content-specific, not systemic
- Icon text wrapping variance (slides 4, 5) — inherent to variable-length content
- Decorative arc barely visible on bg-base — increase arc opacity in CSS class (minor style tweak)
