# Improvements from Learn Iteration 8

## Applied Changes (critical + major systemic issues only)

### Change 1: Ghost number opacity — teal/medium bg-accent minimum
- **File**: SKILL.md
- **Section**: Rule 28 — Ghost decorative number opacity enforcement
- **Type**: modify_rule
- **Description**: The current minimum 0.10 opacity for ghost numbers was validated for dark (navy) bg-accent. This cycle confirmed that teal (#0D9488, luminance ~28%) requires a higher minimum — 0.10 renders as nearly invisible in PNG export. Added luminance-conditional minimums.
- **Before**: "Any ghost number at opacity below 0.15 on a warm background will be invisible in exported PNGs."
- **After**: "Any ghost number at opacity below 0.15 on a warm background will be invisible in exported PNGs. **Additional luminance rule**: On teal or medium-luminance bg-accent (luminance 20–40%), white ghost numbers require minimum opacity **0.16**. On dark (navy, charcoal) bg-accent (luminance <15%), minimum is 0.10. On light bg-accent (rare), minimum is 0.25."

### Change 2: Icon-trio — left-align for titles >15 characters
- **File**: references/composition-archetypes.md
- **Section**: icon-trio archetype — Visual description and skeleton note
- **Type**: add_rule
- **Description**: When icon-trio column titles exceed 15 characters, they wrap to 2 lines in a ~200px column. Centering a 2-line heading creates a "hourglass" visual instability (wide icon → narrow centered text → wide description). Left-aligning the whole column resolves this and is more consistent with analytics/data-report contexts.
- **Before**: "**Visual:** 3 circle icon containers in a horizontal row with labels below each. Clean, spaced."
- **After**: "**Visual:** 3 circle icon containers in a horizontal row with labels below each. Clean, spaced. **Title alignment rule**: Center-align ITEM_TITLE only when titles are ≤15 characters (1–2 words). For longer titles, switch the column to left-aligned: remove `align-items:center` from the column div, set `text-align:left` on title and description. This prevents the hourglass centering pattern (wide icon → narrow wrapped centered title → wide description)."

### Change 3: Decorative motif layout compatibility — glow vs full-width layouts
- **File**: SKILL.md
- **Section**: Step 5, point 8 (Apply Decorative Layer)
- **Type**: add_rule
- **Description**: The 600px radial glow positioned at bottom-right overflows into the content area of the rightmost column on full-width symmetric layouts (icon-trio, profile-grid). For these layouts, glow must be replaced with dots or arc, or reduced to 300px centered at bottom-center.
- **Before**: "Rotate motif types across slides — no two adjacent slides use the same motif."
- **After**: "Rotate motif types across slides — no two adjacent slides use the same motif. **Layout-motif compatibility**: For full-width symmetric layouts (icon-trio, two-col-text, profile-grid), prefer `slide-decor-dots` or `slide-decor-arc` — avoid `slide-decor-glow` (600px bottom-right glow bleeds into content columns on the right). If glow is needed on a full-width layout, reduce size to 280px and position at `bottom:0;left:50%;transform:translateX(-50%)` (centered) instead of bottom-right corner."

## Deferred (minor issues — logged for review)
- Slide 4 ghost "04" — immediately fixed in this iteration by adjusting opacity (slide-specific, not skill-level)
- Market share bars (slide 3) — thin bars as data encoding is acceptable for competitive landscape card layouts; not a skill rule gap
- Section divider description content in analytics contexts — topic labels for section dividers are permitted per current rules when the description contains a structural claim
