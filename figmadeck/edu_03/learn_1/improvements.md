# Learn_1 Improvements — FDL Iteration Report

**Preset**: figmadeck-pitch-figma
**Outline**: PlatformAI investor pitch, 13 slides, Russian, formal/data-heavy
**Fidelity achieved**: 9/10
**QA rounds**: 2

---

## Systemic Fixes Applied

### 1. Cyrillic Hero Text Overflow (slide-1-cover, slide-14-cta)
**Problem**: Staatliches Cyrillic characters are ~44% wider than Latin at the same font-size (15.16rem). "УМНАЯ" (5 wide Cyrillic) and "ЛОГИСТИКА" (9 chars) both overflowed the notebook card boundaries.
**Fix (archetype)**: Updated `flexibility.yaml` for both slide-1-cover and slide-14-cta with `max_length_cyrillic` constraints.
**Rule**: Latin max 5 / Cyrillic max 4 for WORD_1 (cover). Latin max 4 / Cyrillic max 3 for WORD_2 (cover). CTA has wider WORD_1 container: Cyrillic max 5.

### 2. Shape Label Single-Word Clipping (slide-4-agenda-shapes)
**Problem**: Long single Russian words like "НЕПРОЗРАЧНОСТЬ" (14 chars) clipped at shape boundaries — `white-space:pre-line` only wraps at spaces, can't break single words.
**Fix (archetype)**: Added `overflow-wrap:break-word` to all 4 LABEL `<p>` elements in `archetype.html`.
**Rule**: Shape LABEL slots should contain two-word phrases (space enables natural wrapping). Single-word labels should be max 8-10 Cyrillic chars.

### 3. Logo Badge Cyrillic Constraints (slide-12-clients-logos)
**Problem**: At 1.3125rem + 0.3125rem letter-spacing, 6-char Cyrillic names like "МАГНИТ" overflow the badge width (9.95% of canvas ≈ 97px).
**Fix**: Updated `flexibility.yaml` with `max_length: 6`, `max_length_cyrillic: 4` for all LOGO slots.
**Rule**: Use abbreviations for client names > 4 Cyrillic chars in this archetype.

---

## Content Adjustments (Outline-Specific)

| Slide | Slot | Original | Final | Reason |
|-------|------|----------|-------|--------|
| 1 | WORD_1 | УМНАЯ | РОСТ | 5 Cyrillic in narrow font overflows card |
| 1 | WORD_2 | ЛОГИСТИКА | AI | 9 Cyrillic far exceeds max_length |
| 2 | NUM_1 | $2.1M | 2M | max_length:2 for number slots |
| 4 | LABEL_1 | НЕПРОЗРАЧНОСТЬ | НЕТ ДАННЫХ | Two words enable natural wrap |
| 4 | LABEL_3 | РАЗРОЗНЕННОСТЬ | НЕТ СВЯЗИ | Two words enable natural wrap |
| All images | IMAGE_URL | placeholder.jpg | data URI SVG | Vite treats relative paths as module imports |

---

## Remaining Minor Issues

- **Slide 10 (visual)**: Title "PLATFORMAI" has low contrast on dark placeholder background. Inherent to placeholder image — no fix needed; resolves with real image.
- **Slide 12 (logos)**: Long names like МАГНИТ, ЭНЕРГО display with tight letter-spacing. Systemic fix added to flexibility.yaml.
