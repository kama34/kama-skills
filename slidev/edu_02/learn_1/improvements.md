# Improvements from Learn Iteration 1

## Applied Changes (critical + major systemic issues)

### Change 1: CSS variable fallback for bg-accent slides
- **File**: SKILL.md
- **Section**: Step 5, enforcement rules
- **Type**: add_rule
- **Description**: Cover and CTA slides render blank in PNG export because CSS custom properties on inner divs don't resolve in Slidev headless export. Added rule requiring hex fallback values in var() for all bg-accent slides.

### Change 2: Section dividers use bg-accent on light themes
- **File**: SKILL.md
- **Section**: Step 4.5, background level distribution
- **Type**: modify_rule
- **Description**: bg-alt (#E8E6DF) is too close to bg-base (#FAF9F6) on light themes — section slides are visually indistinguishable from content. Changed: section dividers on light themes now use bg-accent with white text.

### Change 3: Tighten Ghost Deck FAIL for counting titles
- **File**: SKILL.md
- **Section**: Step 4.5, Ghost Deck test
- **Type**: add_rule
- **Description**: Titles like "Три барьера" contain a number but are labels, not insights. Added FAIL condition for counting-number titles without claims.

### Change 4: Eyebrow label 30% enforcement
- **File**: SKILL.md
- **Section**: Step 5, enforcement rules
- **Type**: add_rule
- **Description**: All archetypes have eyebrow slots, resulting in 80% eyebrow usage. Added hard limit: max 30% of slides with eyebrows, tracked during generation.

### Change 5: Increase decorative opacity for light themes
- **File**: SKILL.md
- **Section**: Step 5, rule 8 (Decorative Layer)
- **Type**: modify_rule
- **Description**: Decorative motifs at opacity 0.32 are invisible in PNG export on light backgrounds. Increased minimums to 0.50 (dots), 0.40 (glow), 0.55 (arc) with larger sizes.

### Change 6: Icon container diversity enforcement
- **File**: SKILL.md
- **Section**: Step 5, Icon Container Selection
- **Type**: add_rule
- **Description**: 100% identical circle containers is the strongest AI-tell. Added rule: never 3+ identical containers on one slide, alternate shapes on icon-trio slides.

## Deferred (minor issues)
- Section slide heading overflow/crop — needs investigation of exact padding calculation
- Stat-hero empty bottom space — architectural change to archetype needed
