# Stitch Learn Summary: edu_05

## Overview
- **Mode**: `--stitch=learn=3`
- **Date**: 2026-03-26
- **Cycles planned**: 3
- **Cycles with Stitch data**: 1 (API failed for cycles 2-3)
- **Total improvements applied**: 5

## Cycle Results

### Cycle 1: PayBridge FinTech (10 slides, dark theme)
- **Stitch score**: 7.5/10
- **Our score**: 6.5/10
- **Delta**: -1.0 (Stitch better)
- **Key findings**: Stitch uses dramatically larger hero numbers (10-12rem vs our 4-5rem), 12-column grid with varied ratios, card border-top accents, surface depth system
- **Changes applied**: 5 rules updated in SKILL.md

### Cycle 2: SmartDistrict GovTech (12 slides, light theme)
- **Stitch**: API failed (2 projects, 20+ minutes total wait)
- **Our output**: Generated successfully, renders cleanly
- **Verification**: Hero numbers at 8-9rem confirmed (cycle 1 improvement applied)

### Cycle 3: GreenHarvest AgTech (8 slides, light theme)
- **Stitch**: API failed (10 minutes wait)
- **Our output**: Generated, partial rendering (2 slides have raw HTML errors)
- **Verification**: Hero +42% at 9rem confirmed, but Rule 45 violations persist

## Cumulative Skill Changes (SKILL.md)

1. **Hero number minimum**: 4rem → 6rem (centered stat-hero: ≥8rem)
2. **Focal point ratio**: 2x → 4x minimum, hero range 6-10rem, breathing slides up to 12rem
3. **Card variant**: Added `.card-stripe` with border-top accent + box-shadow
4. **Metric hierarchy**: New 3-level rule — Level 1 (7-10rem) → Level 2 (3-4rem) → Level 3 (1.25rem), ratio ~7:3:1
5. **Typography scale**: hero range expanded to 6-12em for centered slides

## Patterns Extracted (stitch-learned-patterns.md)

| Pattern | Source | CSS | Applied to |
|---------|--------|-----|------------|
| Hero Number Scale 10rem+ | Slide 2, 7 | font-size: 10-12rem | SKILL.md Step 5 |
| Card Border-Top Accent | Slide 5 | border-top: 2px solid accent | styles/index.css |
| 12-Column Grid Ratios | All slides | grid-column: span 7/5, 4/8 | composition-archetypes note |
| Surface Depth System | Tailwind config | 5+ surface levels | design-principles note |
| 3-Level Metric Hierarchy | Slides 2, 8 | 7-10rem / 3-4rem / 1.1-1.5rem | SKILL.md focal point |

## Stitch vs Us — Strengths Summary

### Stitch does better:
- Typography boldness (10-12rem hero numbers)
- Surface depth variation (5+ levels)
- Grid ratio variety (7/5, 4/8, 2/3 vs fixed 60/40)
- Card accent patterns (border-top strips)
- Minimal decoration for corporate themes
- Detailed UI mockups (routing engine wireframe)

### We do better:
- AI-safe color palette (avoid purple blacklist)
- 2-font discipline (Stitch uses 3)
- Font size minimums enforced (Stitch goes to 8px)
- Warm accent system (amber secondary)
- Decorative personality (ghost typography, dot-grids)
- Structured composition planning (archetype system)
- Shape vocabulary variety (icon containers, pills)

## Stitch API Reliability Issues
- Success rate: ~25% (1 of 4 attempts)
- First attempt typically fails; retry with new project sometimes works
- Light theme prompts had 0% success rate (both cycles 2-3)
- Dark theme prompt succeeded on 2nd attempt (cycle 1)
- Recommendation: always create 2 projects per prompt; budget 15-20 min per Stitch call

## Score Progression
```
Cycle 1: ███████░░░ 6.5/10 (PayBridge FinTech, dark, with Stitch comparison)
Cycle 2: ████████░░ ~7.5/10 (SmartDistrict GovTech, light, no Stitch data, renders well)
Cycle 3: ██████░░░░ ~6.0/10 (GreenHarvest AgTech, light, partial render failures)
```

## Recommendations
1. Hero number scaling improvements are the highest-impact change from this learning run
2. Consider adding "surface depth" CSS variable system (--surface-0 through --surface-4) for dark themes
3. Grid ratio variety should be formalized in archetype definitions
4. Rendering reliability (Rule 45) remains the biggest quality risk — slides with complex nested HTML still fail
5. Stitch API is unreliable for batch operations — consider using it for single high-value design consultations rather than learning loops
