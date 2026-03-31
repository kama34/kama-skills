# EDU_03 — FDL Learning Report

**Preset**: figmadeck-pitch-figma
**Figma file**: 6iJhgnLC8oiDd4r6Tyqtl2 (pitch)
**Iterations completed**: 3/3
**Convergence**: ✅ Early stop — learn_2 + learn_3 both 9/10

---

## Results Summary

| Iteration | Topic | Slides | Fidelity | QA Rounds |
|-----------|-------|--------|----------|-----------|
| learn_1 | PlatformAI investor pitch | 13 | 9/10 | 2 |
| learn_2 | Кедр onboarding | 10 | 9/10 | 1 |
| learn_3 | Студия Арка agency pitch | 14 | 9/10 | 1 |

## Systemic Fixes Applied to Preset (across edu_01–03)

### 1. Cyrillic Hero Text Overflow (cover + CTA)
- Cover WORD_1: max 4 Cyr / Latin 5. WORD_2: max 3 narrow Cyr / Latin 4
- CTA WORD_1: max 5 Cyr (wider 57.92% container)
- **Files**: slide-1-cover/flexibility.yaml, slide-14-cta/flexibility.yaml

### 2. Shape Label Single-Word Clipping (slide-4-agenda-shapes)
- `overflow-wrap:break-word` added to all LABEL `<p>` elements
- Single-word labels max 8–10 Cyr chars; two-word phrases preferred
- **File**: slide-4-agenda-shapes/archetype.html

### 3. Logo Badge Cyrillic Constraints (slide-12-clients-logos)
- max_length_cyrillic: 4 at 1.3125rem + 0.3125rem letter-spacing in 9.95% badge
- **File**: slide-12-clients-logos/flexibility.yaml

### 4. List Item Length Limit (slide-7-list) [NEW in edu_03]
- ITEM_1–3: max 65 Cyr chars → 2-line wrap within 169px row height at 2.03rem
- ITEM_4: max 80 (last row, no collision below)
- **File**: slide-7-list/flexibility.yaml

## Stable Patterns (zero regression across all 3 iterations)

- data URI SVG placeholder pattern (avoids Vite module import errors)
- BioRhyme Expanded "4." open-bottom letterform quirk (font characteristic, not bug)
- vision-light gold card for approach/culture statements
- vision-dark uppercase large statement for challenge/insight slides
- Process archetype phase names: single-word (БРИФ) or short two-word (МЫ НАЧНЁМ)
- Cards4 with Russian titles + body descriptions

## Preset Quality Assessment

The figmadeck-pitch-figma preset is **production-ready** for Russian-language B2B presentations across:
- Investor pitch (formal/data-heavy)
- Onboarding deck (friendly/casual)
- Agency pitch (inspirational/storytelling)
