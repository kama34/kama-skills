# Improvements from Learn Iteration 2

## Applied Changes (critical + major systemic issues only)

### Change 1: Fix Rule 46 — correct global frontmatter/slide 1 pattern
- **File**: SKILL.md
- **Section**: Rule 46
- **Type**: modify_rule
- **Description**: Clarified that global frontmatter IS slide 1. Content must follow immediately after closing `---`. No extra separator before slide 1's content.
- **Before**: "Global headmatter must NOT contain layout: none"
- **After**: "Global frontmatter IS slide 1. Content must come immediately after. layout:none in global is correct."

### Change 2: Increase light-theme decorative opacity minimum
- **File**: design-principles.md (Principle 6)
- **Section**: Light-theme opacity adjustment
- **Type**: modify_rule
- **Description**: Radial glow opacity 0.18 is invisible on light backgrounds. Increase minimum to 0.25.
- **Before**: "Radial glow: opacity 0.40+"
- **After**: "Radial glow on light bg: opacity 0.25+ minimum in CSS definition, 0.40+ in actual rendering"

## Deferred (minor issues — logged for review)
- bg-base/bg-alt luminance too similar (#FAF9F6 vs #F0EDE8) — preset-specific, not skill issue
- Icon container variety within single slide — existing rules allow same shape on icon-trio
