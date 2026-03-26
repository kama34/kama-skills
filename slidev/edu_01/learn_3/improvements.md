# Improvements from Learn Iteration 3

## Applied Changes

### Change 1: Decoration library bg-alt override enforcement
- **File**: SKILL.md
- **Section**: Step 5 — BACKGROUND LAYER SYSTEM
- **Type**: add_rule
- **Description**: Decoration library defaults often produce 0.25 opacity which passes bg-base but fails bg-alt. Need explicit override note.
- **Before**: Opacity calibration exists but decoration library doesn't reference it per bg-level
- **After**: Add note: when placing decorations on bg-alt slides, explicitly use 0.35+ opacity (override library defaults)

### Change 2: Card-mosaic minimum decoration
- **File**: SKILL.md
- **Section**: Step 5 — decorative layer guidance
- **Type**: add_rule
- **Description**: Card-mosaic slides tend to be under-decorated because cards fill most space. Need minimum.
- **Before**: No archetype-specific decoration minimum
- **After**: Card-mosaic and comparison-table: at minimum 1 decorative element (corner circle/arc) to prevent flat-document appearance

## Deferred
- Bento-grid used twice in same deck (justified by content, but could suggest alternative check)
