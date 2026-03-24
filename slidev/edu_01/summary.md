# Learning Run Summary: edu_01

## Overview
- **Iterations**: 3
- **Date**: 2026-03-24
- **Starting skill version**: 98048bb
- **Final skill version**: 4f47831
- **Preset used**: learn-auto-20260324 (auto-created, refined via PDL N=3)

## Iterations

### Learn 1: Цифровая трансформация ритейла (10 слайдов)
- Score: 5.0/10
- Key findings:
  - CSS ::after pseudo-elements via class names don't render in Slidev headless export
  - 7 consecutive slides with identical "label → heading → grid" structure
  - bg-alt appeared only 1/10 slides
- Changes applied:
  1. Decorative elements must be real HTML divs with inline styles (not pseudo-elements)
  2. Structural break rule: after 2 same-pattern slides, 3rd must break
  3. bg-alt minimum raised from 15% to 25% of content slides

### Learn 2: Нейросети в медицине (12 слайдов)
- Score: 6.4/10
- Key findings:
  - Decorative div elements exist but invisible at 0.10-0.18 opacity on light cream backgrounds
  - label+heading+grid still dominates 50% of content slides despite consecutive rule
  - Custom icon names render as broken placeholders if not in Icon.vue
- Changes applied:
  1. Light-theme opacity multiplier 2.5x for decorative elements
  2. Total frequency cap: label+heading+grid max 40% of content slides
  3. Icon name verification: must cross-reference all names with Icon.vue

### Learn 3: Зелёная энергетика для бизнеса (12 слайдов)
- Score: 6.9/10
- Key findings:
  - 100% teal accent creates chromatic monotony — no temperature contrast
  - Arc hairline strokes invisible on light backgrounds even at 2.5x
  - Typography flat — all headings cluster at 2.2-2.8rem
- Changes applied:
  1. Mandatory --color-accent-warm variable for temperature contrast (1-2 slides)
  2. Light-theme filled shape rule: 50%+ decorative elements must be area-filling
  3. Typography tier system: TIER 1 (4-8rem), TIER 2 (3-3.5rem), TIER 3 (2.2-2.8rem)

## Cumulative Skill Changes

### SKILL.md changes (9 total):
1. **Step 5.8** — Decorative elements as real HTML divs (not CSS pseudo-elements)
2. **Step 5.8** — Light-theme opacity 2.5x multiplier
3. **Step 5.8** — Light-theme filled shape rule (50%+ area-filling)
4. **Step 5** — Structural break rule (2-consecutive + 40% total cap)
5. **Step 4.5** — bg-alt minimum 25% of content slides (was 15%)
6. **Step 6a** — Icon name verification against Icon.vue
7. **Step 4** — Mandatory --color-accent-warm variable
8. **Step 5.5** — Typography tier assignment (TIER 1/2/3)
9. **Step 5** — Layout Diversity total frequency cap

### PDL (Preset Deep Learning) findings:
- CSS class names for element styling (icon-container, label-pill, card variants) are reliable
- CSS class names for backgrounds FAIL — backgrounds must be inline styles
- bg-alt luminance delta must be ≥10% from bg-base to be visually distinguishable

## Deferred Issues (minor — need human review)
- Layout cap hard enforcement — needs counter mechanism in generator, not just rule text
- CTA action hierarchy (primary vs secondary button differentiation)
- Cover archetype empty lower half
- Two stat-hero slides can look identical if both use centered layout
- Icon container shape uniformity (all same shape across deck)

## Recommendations
- Consider adding a hard layout counter to Step 4.5 that pre-assigns visual structures
- Research whether Slidev supports CSS custom properties on HTML elements in export mode
- The warm accent variable needs concrete usage examples in archetype skeletons
- Light-theme decorative elements may benefit from a completely different approach (colored surface cards vs atmospheric overlays)

## Score Progression
```
Learn 1: █████░░░░░ 5.0  (Ритейл, light cream + teal — no decorative elements)
Learn 2: ██████▍░░░ 6.4  (Медицина, light cream + teal — partially visible decor)
Learn 3: ██████▉░░░ 6.9  (Энергетика, light cream + teal — visible decor, icons work)
```

## Patterns Observed
- **Rendering reliability**: Inline styles > CSS classes > pseudo-elements. Each step down in this hierarchy introduces increasing risk of silent rendering failures.
- **Light themes need 2-3x stronger decorative treatment** than dark themes — opacity values calibrated for dark backgrounds are invisible on cream/white.
- **Layout monotony is the hardest issue to fix** — the generator gravitates toward "label + heading + grid" regardless of archetype name. Hard caps help but need enforcement.
- **Chromatic range** improves engagement — single-accent decks feel monotonous even when well-executed.
- **Typography drama** requires explicit tier assignment — without it, all headings converge to the same safe 2.2-2.8rem range.
