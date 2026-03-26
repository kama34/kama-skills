# Improvements from Learn Iteration 1

## Applied Changes (critical + major systemic issues only)

### Change 1: Icon-trio title length enforcement
- **File**: SKILL.md
- **Section**: Step 5 (Write slides.md) — after "Content quality checks during writing"
- **Type**: add_rule
- **Description**: Add mandatory character-count check for icon-trio column titles
- **Before**: N/A (new addition)
- **After**: Rule text about checking title length and switching to left-align if >15 chars

### Change 2: Timeline-horizontal connector requirement
- **File**: SKILL.md
- **Section**: Step 5 (Write slides.md) — after icon-trio rule
- **Type**: add_rule
- **Description**: Require visual connector between timeline phases
- **Before**: N/A
- **After**: Rule about mandatory horizontal connector line

### Change 3: Light theme decoration opacity hard minimums
- **File**: SKILL.md
- **Section**: BACKGROUND LAYER SYSTEM — OPACITY CALIBRATION
- **Type**: modify_rule
- **Description**: Raise opacity values for light backgrounds to ensure visibility
- **Before**: "Light backgrounds (luminance > 70%): atmosphere 0.15-0.30, texture 0.06-0.12"
- **After**: "Light backgrounds (luminance > 70%): atmosphere 0.25-0.35 (HARD MINIMUM 0.25), texture 0.15-0.22 (HARD MINIMUM 0.15). These minimums are non-negotiable — decoration below these values is INVISIBLE in PNG export on cream/white backgrounds."

### Change 4: Statistics source citation rule
- **File**: SKILL.md
- **Section**: Step 5 — content quality checks during writing
- **Type**: add_rule
- **Description**: Require source attribution on all specific statistics
- **Before**: N/A
- **After**: Rule about mandatory source citations

### Change 5: bg-level anti-checkerboard rule
- **File**: SKILL.md
- **Section**: Step 4.5 — background level assignment algorithm
- **Type**: modify_rule
- **Description**: Add semantic purpose requirement for bg-alt and anti-checkerboard check
- **Before**: Algorithm assigns bg-alt to every 3rd-4th content slide
- **After**: Add anti-checkerboard validation step after assignment

### Change 6: Data-spotlight hero metric promotion
- **File**: SKILL.md
- **Section**: Step 5 — FOCAL POINT rule
- **Type**: modify_rule
- **Description**: When data-spotlight shows 3+ metrics, promote the most impactful to hero size
- **Before**: "Every content slide MUST have ONE dominant element visually 2x+ larger than the next largest. Stat slides: hero number 4-8rem, supporting 1-1.5rem."
- **After**: Add specific data-spotlight guidance

## Deferred (minor issues — logged for review)
- CTA heading minimum 3.2rem (minor upgrade from 2.8rem)
- Eyebrow label distribution (already partially documented)
- Density-compensated heading sizing
- Bento-grid side card style variation
- Card-mosaic qualitative card needs number
