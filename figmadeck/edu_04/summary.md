# edu_04 — FDL Convergence Report (7 iterations)
Preset: figmadeck-pitch-figma. Figma file: 6iJhgnLC8oiDd4r6Tyqtl2.

## Iterations

| # | Project | Domain | Slides | QA rounds | Fidelity |
|---|---------|--------|--------|-----------|----------|
| 1 | MedPulse HealthTech Pitch | healthtech | 12 | 2 | 9/10 |
| 2 | ИнтеллектПлюс EdTech Launch | edtech | 10 | 1 | 9/10 |
| 3 | Marketland Стратегический кейнот | retail/marketplace | 16 | 1 | 9/10 |
| 4 | ЭкоГород Питч для грантового фонда | govtech/green | 8 | 1 | 9/10 |
| 5 | Кредит360 Series A Pitch | fintech | 14 | 1 | 9/10 |
| 6 | NeuralOps AI Strategy 2027 | AI/MLOps | 12 | 1 | 9/10 |
| 7 | ПродуктАкадемия Запуск курса | education | 15 | 1 | 9/10 |

**Total**: 87 slides across 7 diverse Russian-language presentations. All reached 9/10 fidelity. 6/7 in first QA round (convergence after learn_1).

## Key Rules Learned

### Discovered in learn_1 (required 2 QA rounds)
- **Shape label Cyr limit**: Single Cyrillic word in shape SVG container max **6 chars** at Staatliches 1.3125rem + letter-spacing. overflow-wrap:break-word causes mid-word splits at 7+ chars. Multi-word OK (space enables natural break).
  - Confirmed: АЛЕРТЫ(6)✓ МОНИТОР(7)✗→ДАТЧИК(6) СКОРОСТЬ(8)✗→БЫСТРО(6) КОМАНДА(7)✗→ЛЮДИ(4) ОБУЧЕНИЕ(8)✗→ШКОЛЫ(5) ПЕРЕХОД(7)✗→СМЕНА(5)

### Applied consistently from learn_2 onward
- **NUM slot max 2 chars**: BioRhyme Expanded 11.72rem — condensed forms: ₽3,2B→"3B", ₽2,1M→"2M", ×2,4→"2X", 4,8/5→"4+" etc.
- **vision-dark DESCRIPTION max 150 chars**: BioRhyme Expanded uppercase 1.41rem. Shorten if outline provides longer text.
- **vision-light DESCRIPTION max 200 chars**: Body font 2.03rem weight-300 centered.
- **list items max 65 chars** (items 1-3), **80 chars** (item 4) at 2.03rem for 2-line wrap.
- **Logo names 4-char Latin**: renders cleanly in colored badge boxes at 0.65rem Staatliches.
- **Visual slide placeholder**: #cccccc SVG for `var(--color-text)` dark title readability.
- **Team/gallery photo placeholder**: `%23bbb` data-URI SVG (light bg), `%23222/%23333/%23444/%23555` (dark bg).

### Extended in later iterations
- **Latin abbreviations for shapes**: Tech abbrevs (A/B, SRE, MVP) work in shape containers — no Cyr length concern.
- **Archetype reuse**: Acceptable when content clearly differs. 13 archetypes for 8-16 slide decks handled via reuse. Documented in improvements.md.
- **Process pill labels**: 2-char code + 1-word label fits pill at 0.78rem without overflow (М1/РОСТ, Q1/ПИЛОТ, Ш1/ЗАЯВКА).

## Archetype Coverage Across edu_04

| Archetype | l1 | l2 | l3 | l4 | l5 | l6 | l7 |
|-----------|----|----|----|----|----|----|-----|
| cover | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| numbers | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| team | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| shapes | ✓ | ✓ | ✓ | ✓ | ✓×2 | ✓ | ✓ |
| vision-light | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓×2 |
| vision-dark | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| list | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| cards4 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓×2 |
| process | ✓ | ✓ | ✓×2 | — | ✓ | — | ✓×2 |
| visual | ✓ | — | — | — | ✓ | ✓ | — |
| gallery | ✓ | ✓ | ✓ | — | ✓ | — | ✓ |
| logos | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| cta | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

All 13 archetypes exercised across the 7 iterations. No archetype exposed new bugs after learn_1.

## Conclusion
The preset is stable at 9/10 fidelity. The single systemic rule (6-char Cyr shape label) was discovered in iteration 1 and applied cleanly in all subsequent iterations. No structural archetype issues found. The preset handles 8–16 slide decks across domains (healthtech, edtech, fintech, AI, green, education, retail) without modification.
