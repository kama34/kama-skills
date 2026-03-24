# Improvements from Learn Iteration 3

## Applied Changes (critical + major systemic issues only)

### Change 1: Add mandatory warm accent variable requirement
- **File**: SKILL.md
- **Section**: Step 4 → CSS variable definitions
- **Type**: add_rule
- **Description**: 100% teal accent creates chromatic monotony. Need a secondary warm accent for contrast.
- **Before**: Only --color-accent (single accent)
- **After**: Add requirement: "**MUST also define `--color-accent-warm`**: a warm-toned secondary accent (amber, coral, terracotta) for CTA buttons, key metrics on 1-2 slides, and any element needing temperature contrast. This breaks chromatic monotony. Example: if primary accent is teal (#0D9488), warm accent could be amber (#D97706) or coral (#E76F51). Use sparingly (1-2 slides max) but it MUST exist."

### Change 2: Add filled decorative shapes requirement for light themes
- **File**: SKILL.md
- **Section**: Step 5 → point 8 "Apply Decorative Layer"
- **Type**: expand_checklist
- **Description**: Arc hairline strokes are invisible on light cream backgrounds even at 2.5x opacity. Need at least one filled shape.
- **Before**: Three motif options (dot grid, radial glow, arc)
- **After**: Add: "**Light-theme filled shape rule**: On light backgrounds, at least 50% of decorative elements MUST be area-filling (dot grid, radial glow) not just outlines (arc). Arcs and border strokes have insufficient visual mass on cream/white backgrounds. For every arc used on a light slide, pair it with a filled glow or increase arc border-width to 4px minimum."

### Change 3: Add typography tier system
- **File**: SKILL.md
- **Section**: Step 5 → point 5 "Apply Typographic Drama"
- **Type**: expand_checklist
- **Description**: All headings cluster at 2.2-2.8rem creating flat typography. Need explicit size tiers.
- **Before**: "Key numbers and metrics must use hero scale (4-8em). Statement/fact slides should have 3-5em text minimum."
- **After**: Add: "**Typography tier assignment**: Before writing slides, assign each slide to a tier: TIER 1 (hero, 1-2 slides): 4-8rem for the single most important number/statement. TIER 2 (emphasis, 2-3 slides): 3-3.5rem for section headings and key insights. TIER 3 (standard, remaining): 2.2-2.8rem for content headings. Every deck MUST have at least 1 TIER 1 and 2 TIER 2 slides. If all headings are the same size, the deck has failed typographic drama."

## Deferred (minor issues — logged for review)
- CTA lacks action hierarchy (primary vs secondary button) — minor UI issue
- Layout cap still at 50% vs 40% — needs hard counter in generation, not just rule text
