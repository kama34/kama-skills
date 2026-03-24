# Improvements from Learn Iteration 2

## Applied Changes (critical + major systemic issues only)

### Change 1: Add light-theme opacity multiplier for decorative elements
- **File**: SKILL.md
- **Section**: Step 5 → point 8 "Apply Decorative Layer"
- **Type**: add_rule
- **Description**: Decorative elements at 0.10-0.18 opacity are invisible on light cream backgrounds. Need theme-aware opacity.
- **Before**: Fixed opacity values in examples (0.18, 0.10)
- **After**: Add: "**Light-theme opacity adjustment**: On light backgrounds (luminance >70%), MULTIPLY all decorative opacity values by 2.5x. Dot grid: 0.18 → 0.40. Radial glow: 0.10 → 0.25. Arc border: 0.18 → 0.40. Also increase decorative element SIZE by 1.5x on light themes (280px → 420px for dot grid, 400px → 600px for glow). Light backgrounds need stronger, larger decorative marks to be visible."

### Change 2: Add label+heading+grid total frequency cap
- **File**: SKILL.md
- **Section**: Step 5 → STRUCTURAL BREAK RULE
- **Type**: expand_checklist
- **Description**: Even with the 2-consecutive rule, 50% of content slides still use the same label+heading+grid pattern.
- **Before**: Only consecutive rule (2 in a row max)
- **After**: Add: "Additionally, the label-top-left + heading + grid/cards pattern may NOT appear on more than 40% of content slides in total. For a 10-slide deck (8 content), max 3. For a 12-slide deck (10 content), max 4. Count and verify."

### Change 3: Icon component rendering note
- **File**: SKILL.md
- **Section**: Step 6 → "6a. Icon component"
- **Type**: add_rule
- **Description**: Custom icon names (brain, dna, microscope) don't render if not defined in Icon.vue with actual SVG paths.
- **Before**: "Include icons relevant to the presentation topic"
- **After**: Add: "**CRITICAL: Every icon name used in slides.md MUST have a matching v-if branch in Icon.vue with a complete SVG path.** Before finalizing slides.md, cross-reference all `<Icon name="...">` calls with Icon.vue's v-if branches. If a needed icon is not defined, ADD it with a real SVG path (not a placeholder). Common icon SVG paths can be sourced from Heroicons (outline style). Never use an icon name that doesn't exist in Icon.vue."

## Deferred (minor issues — logged for review)
- Two stat-hero slides identical layout — content/archetype issue, not skill rule
- Cover empty lower half — could be addressed by cover archetype adjustment
