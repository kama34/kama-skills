# Learning Run Summary: edu_02

## Overview
- **Iterations**: 10
- **Date**: 2026-03-25
- **Starting skill version**: 65590f9
- **Final skill version**: ce66f2c
- **Starting score**: 4.2/10 (AI-detect 31/50)
- **Final score**: 8.3/10 (AI-detect 8/50)
- **Total improvement**: +4.1 points (+98% relative)

## Score Progression
```
Learn  1: ████░░░░░░ 4.2  (Логистика 4.0, warm teal/cream)
Learn  2: █████░░░░░ 5.8  (AI в образовании, warm teal/cream)
Learn  3: ██████░░░░ 6.2  (Телемедицина, warm teal/cream)
Learn  4: ███████░░░ 7.4  (Финансы Q4, warm teal/cream)
Learn  5: ███████░░░ 7.2  (Креативное агентство, warm teal/cream)
Learn  6: ███████░░░ 7.2  (TaskFlow SaaS, warm teal/cream)
Learn  7: ███████░░░ 7.8  (НКО годовой отчёт, warm teal/cream)
Learn  8: ███████░░░ 7.9  (E-grocery, warm teal/cream)
Learn  9: ███████░░░ 7.9  (MLOps воркшоп, warm teal/cream)
Learn 10: ████████░░ 8.3  (Зелёная энергетика, warm teal/cream)
```

## AI Detection Progression
```
Learn  1: ██████████████████████████████░ 31/50  FAIL
Learn  2: ██████████████████████████████░ 31/50  FAIL
Learn  3: ██████░░░░░░░░░░░░░░░░░░░░░░░░  6/50  PASS
Learn  4: ████████░░░░░░░░░░░░░░░░░░░░░░  8/50  PASS
Learn  5: ██████████████░░░░░░░░░░░░░░░░ 14/50  PASS
Learn  6: ████████████░░░░░░░░░░░░░░░░░░ 12/50  PASS
Learn  7: █████████░░░░░░░░░░░░░░░░░░░░░  9/50  PASS
Learn  8: ███████████░░░░░░░░░░░░░░░░░░░ 11/50  PASS
Learn  9: ██████████░░░░░░░░░░░░░░░░░░░░ 10/50  PASS
Learn 10: ████████░░░░░░░░░░░░░░░░░░░░░░  8/50  PASS
```

## Iterations Detail

### Learn 1: Логистика 4.0 (10 slides)
- Score: 4.2/10 | AI: 31/50
- Critical: Cover/CTA blank (CSS var not resolving), section dividers indistinguishable, 100% identical icon containers
- Changes: +6 rules (bg-accent fallback, section bg-accent light, counting titles FAIL, eyebrow 30%, decorative 3x, icon diversity)

### Learn 2: AI в образовании (14 slides)
- Score: 5.8/10 | AI: 31/50
- Issues: icon-trio ghost invisible on bg-alt, 33% slides = same 2×2 grid, identical section dividers, stat-hero twins
- Changes: +4 rules (icon bg-level, visual structure dedup, section differentiation, stat-hero variation)

### Learn 3: Телемедицина (9 slides)
- Score: 6.2/10 | AI: 6/50
- Issues: adjacent structural clones, empty section divider, mechanical icon rotation, decor invisible on bg-alt
- Changes: +4 rules (adjacent fingerprint, section decorative weight, icon semantic purpose, bg-alt opacity 1.5x)

### Learn 4: Финансы Q4 (10 slides)
- Score: 7.4/10 | AI: 8/50
- Issues: ghost number too faint, adjacent focal gravity same, card-mosaic equal hierarchy
- Changes: +3 rules (ghost opacity 0.12, focal gravity audit, card-mosaic hierarchy)

### Learn 5: Креативное агентство (8 slides)
- Score: 7.2/10 | AI: 14/50 | Regression: -0.2
- Issues: eyebrow overuse despite existing rule (no counter), section divider label exempt from Ghost Deck
- Changes: +2 rules (mandatory eyebrow counter, section Ghost Deck standard)

### Learn 6: TaskFlow SaaS (15 slides)
- Score: 7.2/10 | AI: 12/50
- Issues: 2 bento-grids same column ratio, section-divider left variant empty lower third
- Changes: +2 rules (bento-grid global dedup, section-divider lower anchor)

### Learn 7: НКО годовой отчёт (12 slides)
- Score: 7.8/10 | AI: 9/50
- Issues: heading >50 chars wraps in split layout, bento featured cell too small, bg-alt arc teal-on-warm low contrast
- Changes: +3 rules (bento featured ≥3.5rem, split heading cap, bg-alt dark color rule)

### Learn 8: E-grocery (10 slides)
- Score: 7.9/10 | AI: 11/50
- Issues: ghost number 0.10 on teal, icon-trio centered titles cramp, glow bleeds into symmetric layouts
- Changes: +3 rules (ghost opacity 0.16 teal, icon-trio left-align, glow layout compat)

### Learn 9: MLOps воркшоп (16 slides)
- Score: 7.9/10 | AI: 10/50
- Issues: icon-trio 4+ items cramped, consecutive grid-group same fingerprint, 4 section dividers all same bg
- Changes: +3 rules (icon-trio 4+ → 2×2, grid-group fingerprint break, section bg variety)

### Learn 10: Зелёная энергетика (12 slides)
- Score: 8.3/10 | AI: 8/50
- Issues: bento icon beside number (should be above), side-card content duplication, too many grid slides
- Changes: +3 rules (bento icon-above-number, side-card dedup, deck-level grid cap 35%)

## Cumulative Skill Changes

**Total rules added/modified**: 33 across 10 iterations

### By category:
- **Background/Color** (7): bg-accent hex fallback, section bg-accent light, ghost number opacity 0.12/0.16, bg-alt dark decor, section bg variety, bg-alt opacity 1.5x
- **Layout/Composition** (9): visual structure dedup, adjacent fingerprint, adjacent gravity, card-mosaic hierarchy, bento-grid dedup, section differentiation, section lower anchor, grid-group fingerprint break, deck-level grid cap
- **Typography/Content** (5): counting titles FAIL, eyebrow 30%, mandatory counter, split heading cap, section Ghost Deck standard
- **Icons/Shapes** (4): icon diversity, icon bg-level, icon semantic purpose, icon-trio 4+ → 2×2
- **Decorative** (4): decorative 3x, section decorative weight, glow layout compat, bento featured ≥3.5rem
- **Data/Archetype** (4): stat-hero variation, bento icon-above-number, side-card dedup, icon-trio left-align

## Deferred Issues (minor — need human review)
- Ruble symbol (₽) glyph weight in Outfit font at 800 weight
- Unicode bullet characters in timeline footer strips
- Profile-grid 5-cell layout (no convention for full-span bottom row)
- Feature-description vs benefit-framing in content copy
- CTA button visual weight (needs archetype redesign consideration)

## Patterns Observed
- Dark-themed presentations were not tested (all used light teal/cream preset)
- Scores plateau around 7.8-8.0 with diminishing returns per rule
- AI detection dropped from 31 to 8 — biggest gains from: removing identical icon containers, varying section dividers, hex fallback fixing blank slides
- Regression in cycle 5 (-0.2) was due to eyebrow overuse — rule existed but lacked enforcement mechanism
- Larger decks (15-16 slides) exposed more diversity issues than smaller ones (8-10)
- Financial/data decks scored higher than creative portfolios with same rules
- Ghost Deck test improvements had the largest single impact on "Content clarity" scores

## Recommendations
1. Test dark theme preset through a separate --learn run
2. Consider redesigning CTA archetype for more visual impact
3. Profile-grid archetype needs a 5-cell variant
4. Content copy quality (benefit framing) is beyond current structural rules — may need a content-rewriting step
5. The 33 accumulated rules may benefit from consolidation to reduce cognitive load during generation
