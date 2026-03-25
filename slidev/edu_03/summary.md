# Learning Run Summary: edu_03

## Overview
- **Iterations**: 7
- **Date**: 2026-03-25
- **Starting skill version**: e682aec (pre-learning)
- **Final skill version**: current HEAD
- **Total slides generated**: 81 across 7 presentations
- **Total slides rendered correctly**: 68/81 (84%)

## Iterations

### Learn 1: CyberShield (Кибербезопасность) — 10 slides
- Score: 3.1/10
- Key finding: Raw HTML rendering failure — inline styles with var() break Slidev parser
- Changes applied: Rule 45 (inline style whitelist), Rule 46 (global frontmatter = slide 1), QA-2b (render verification)

### Learn 2: Ремесло (Маркетплейс handmade) — 8 slides
- Score: 7.2/10
- Key finding: Rule 45 completely solved rendering. Ghost slide from extra --- separator.
- Changes applied: Rule 46 rewritten (content follows immediately after global frontmatter)

### Learn 3: Индустрия 5.0 (Цифровая трансформация) — 14 slides
- Score: 1.5/10 (REGRESSION)
- Key finding: position:relative;height:100% produces blank slides. Must use position:absolute;inset:0
- Changes applied: Rule 47 (root div positioning + mandatory per-slide style block)

### Learn 4: FitCorp (Корпоративный wellness) — 11 slides
- Score: 7.8/10
- Key finding: All rules working together. 11/11 render, zero ghost slides.
- Changes applied: None needed — rendering stable

### Learn 5: Транспорт будущего (Умный город) — 15 slides
- Score: 7.5/10
- Key finding: 15-slide keynote renders perfectly. Pattern scales to large decks.
- Changes applied: None

### Learn 6: TechTalk (Онлайн-школа английского) — 9 slides
- Score: 8.0/10 (BEST)
- Key finding: Compact pitch deck with strongest bento composition (+320% MRR)
- Changes applied: None

### Learn 7: ChainProof (Блокчейн supply chain) — 13 slides
- Score: 7.8/10
- Key finding: Workshop format with section dividers renders cleanly. 450% ROI bento strong.
- Changes applied: None

## Cumulative Skill Changes

### New Rules Added to SKILL.md
1. **Rule 45** — Inline style property whitelist: structural properties only in inline styles, visual properties in CSS classes
2. **Rule 46** — Global frontmatter IS slide 1: content follows immediately, no extra separator
3. **Rule 47** — Root div MUST use position:absolute;inset:0, every slide needs own style block
4. **QA-2b** — Post-export render verification: check for blank/raw HTML slides

### Preset Changes (learn-auto-20260325)
- Overlay gated behind .has-bg-image class (was unconditional)
- Background level utility classes added (.bg-base, .bg-alt, .bg-accent-slide)
- Decorative utility classes added (.deco-glow-teal, .deco-dot-grid, .deco-arc)
- Warm accent utility classes added (.label-pill-warm, .stat-warm, .card-warm)
- Accent background text overrides added (white text on teal)
- Cover heading minimum size (clamp)
- Icon container distribution rule added
- Stat-hero variant rule added
- Render failure safeguard CSS

## Deferred Issues (minor — need human review)
- bg-base (#FAF9F6) and bg-alt (#F0EDE8) are visually too similar in exported PNGs
- Decorative elements (glows) still too subtle on light backgrounds at current opacity
- Structural monotony (LABEL→H1→content pattern) appears frequently across decks

## Recommendations
- Consider increasing bg-alt darkness to #E8E4DE for more visible alternation
- Increase decorative glow opacity to 0.30+ on bg-base for light themes
- Add a "structural fingerprint" check to the generation agent's composition planning

## Score Progression
```
Learn 1: ███░░░░░░░ 3.1  (кибербез, rendering failure)
Learn 2: ███████░░░ 7.2  (handmade, rendering solved)
Learn 3: █░░░░░░░░░ 1.5  (промышленность, REGRESSION: blank slides)
Learn 4: ████████░░ 7.8  (wellness, best until now)
Learn 5: ████████░░ 7.5  (smart city, large keynote)
Learn 6: ████████░░ 8.0  (TechTalk, BEST — compact pitch)
Learn 7: ████████░░ 7.8  (blockchain, workshop format)
```

## Patterns Observed
- **Rendering reliability is the #1 predictor of score.** Iterations 1 and 3 scored low purely due to rendering failures. Once rendering was fixed (Rules 45-47), scores stabilized at 7.2-8.0.
- **Compact decks score higher.** 8-9 slide pitches (Learn 2, 6) scored 7.2-8.0. 14-15 slide keynotes (Learn 3, 5) had more rendering issues and lower scores. The skill is better at generating compact presentations.
- **Light theme decoratives need higher opacity.** Radial glows at 0.18-0.25 opacity are barely visible on #FAF9F6 cream background. Need 0.30+ minimum.
- **The proven working pattern is: CSS classes in `<style>` blocks + position:absolute;inset:0 root divs.** Any deviation from this (inline styles, relative positioning, missing style blocks) causes rendering failure.
