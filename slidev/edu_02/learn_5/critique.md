# Critique: FORMA — Креативное агентство (Learn Iteration 5)

## Overall Score: 7.1/10

---

## AI Detection Score: 14/50

**Result: PASS** — presentation does NOT read as AI-generated. Below the 16-point threshold.

### AI Detection Breakdown

| Category | Points | Notes |
|---|---|---|
| Color | 1 | Teal (#0D9488) is safe, not in purple/indigo blacklist. Warm cream bg. |
| Typography | 2 | Outfit+DM Sans pair is distinctive. No Inter/Roboto/Space Grotesk. |
| Layout | 2 | 5 different archetype structures across 8 slides — good variety. |
| Visual effects | 2 | Subtle radial glows and dot grids. No glassmorphism stack. No dramatic shadows. |
| Imagery | 0 | No images used. |
| Content structure | 3 | Some eyebrow labels on all slides (over 30% limit). Cover→stat→process→asymmetric→bento→section→asymmetric-stat→CTA — good variety. |
| Content quality | 3 | Titles are mostly action-oriented. One generic element: slide 6 has no stat/claim, just a section title. |
| Metadata | 1 | Dots metadata row on cover is a minor AI-tell (overused pattern in templates). |

**Total: 14/50** — Below detection threshold. ✓

---

## Scoring Per Slide (9 axes)

| Slide | Comp | Shape | Font | Impact | Layout | Typo | Color | Content | Decor | AVG |
|-------|------|-------|------|--------|--------|------|-------|---------|-------|-----|
| 1 Cover | 8 | 7 | 8 | 8 | 9 | 8 | 8 | 7 | 7 | 7.8 |
| 2 140+ | 7 | 8 | 8 | 8 | 7 | 8 | 8 | 7 | 8 | 7.7 |
| 3 Method | 7 | 6 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7.0 |
| 4 Ozon | 8 | 8 | 7 | 8 | 8 | 7 | 7 | 7 | 7 | 7.4 |
| 5 VK | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7.0 |
| 6 Section | 8 | 6 | 8 | 8 | 8 | 8 | 8 | 6 | 7 | 7.4 |
| 7 78% | 7 | 7 | 8 | 7 | 8 | 8 | 7 | 7 | 7 | 7.3 |
| 8 CTA | 8 | 7 | 8 | 7 | 7 | 8 | 8 | 8 | 8 | 7.7 |

**Overall: 7.2/10**

---

## Systemic Issues (affect the skill itself)

### Issue 1: Eyebrow Label Overuse — All Slides Have Labels
- **Severity**: major
- **Category**: structure, ai-detection
- **Frequency**: 6/8 non-exempt slides (cover and CTA are exempt). 75% of content slides have eyebrow labels. Rule: max 30%.
- **Description**: Every non-cover, non-CTA slide uses a small uppercase eyebrow label above the heading. This creates visual repetition and is a strong AI-generation signal — AI defaults to labelling every section because it's "safe and structured." In this 8-slide deck, max allowed = floor(6 × 0.30) = 1–2 labels on content slides. Current count: 6.
- **Evidence**: Slides 2,3,4,5,6,7 all have eyebrow labels visible in exported PNGs. The pattern is visually monotonous — every slide starts with a small teal tag, then a heading. Same rhythm = AI tell.
- **Root cause**: SKILL.md Rule on eyebrow labels (max 30%) is correctly stated but the enforcement during Step 5 (writing slides) lacks a concrete **tracking mechanism**. The rule says "track usage during writing" but no explicit counter or check-point is defined in the procedure that would fire during writing iteration.
- **Proposed skill fix**: Add to Step 5 (Write slides.md) under "Enforcement rules during writing" a mandatory tracking comment:
  > **EYEBROW LABEL TRACKING**: Before writing each slide, check `eyebrow_count / (total_content_slides - 2)`. If ratio >= 0.30, STOP adding eyebrows and write the heading directly. Keep a running tally: slides with eyebrows: [list]. This check fires before writing every slide.
  Also add to QA-0c Anti-Pattern Scan: explicitly count eyebrow usage and auto-fix excess by removing labels from slides where the heading is self-explanatory (the heading already contains context — e.g., "Кейс · Ozon Fresh" as eyebrow is redundant when the heading already says "Ребрендинг за 8 недель").

### Issue 2: Section Divider Slide Has Insufficient CTA/Claim Energy
- **Severity**: major
- **Category**: content, structure
- **Frequency**: 1/1 section-divider slides
- **Description**: Slide 6 ("Почему клиенты остаются") is a pure section break with a descriptive subtitle. It works visually — ghost "06", left alignment, teal bg — but the subtitle "Долгосрочные партнёрства — главный показатель качества" is a claim that deserves to be the *main heading*, not subordinate text. The heading is a label ("Почему клиенты остаются") while the subtitle carries the real insight. This inverts the hierarchy. Ghost Deck test: reading this slide's title tells you nothing about what FORMA wants you to believe.
- **Evidence**: Slide 6 PNG. The teal heading says "Почему клиенты остаются" (generic section label). The subtitle has the actual insight but is 1.3rem vs heading 3.8rem — the weaker message is dominant.
- **Root cause**: Section divider archetype uses `{{HEADING}}` for the section name and `{{DESCRIPTION}}` for supporting text. SKILL.md Ghost Deck test checks titles but the section-divider archetype is used for breathing/transitions, and the Ghost Deck check has an exemption gap — it doesn't enforce action titles on section slides, only on content slides.
- **Proposed skill fix**: Add to SKILL.md Ghost Deck test:
  > **Section divider exception boundary**: Section dividers are allowed topic-label headings ONLY if the description below contains a claim/insight. If the description is also generic/neutral (no number, comparison, or outcome), the heading MUST be promoted to a claim. Pattern: "78% клиентов остаются — проверено на 140+ проектах" is better than "Почему клиенты остаются."

### Issue 3: Slide 3 (Method) — 2×2 Grid Pattern Shared with Slide 5 (VK Bento)
- **Severity**: minor
- **Category**: rhythm, layout
- **Frequency**: 2 slides (3 and 5)
- **Description**: Slide 3 uses a 2×2 grid of cards (timeline-horizontal rendering). Slide 5 uses a bento-grid that also results in a 2×2 visual structure. The "Visual structure dedup" rule in Step 4.5 is supposed to catch this — both slides have the same visual fingerprint "left-heading + 2×2 grid." They are not adjacent (slides 3 and 5 have slide 4 between them), so the adjacent fingerprint check doesn't fire. But visually they create a repeated grid rhythm in the first half of the deck.
- **Evidence**: PNG 3 and PNG 5 — both show a heading at top and a 2×2 card grid below. Slide 4 breaks the pattern, but the 3-5 sequence still feels repetitive.
- **Root cause**: The "visual structure dedup" check in Step 4.5 uses a 30% cap on "4-cell grid" slides but only checks adjacency for fingerprint dedup, not a 3-slide window.
- **Proposed skill fix**: Extend the visual fingerprint dedup to a 3-slide window (not just adjacent pairs). Add to Step 4.5:
  > **3-slide fingerprint window**: After completing the composition plan, check every triplet of consecutive slides (slides N, N+1, N+2). If two or more in the triplet share the same fingerprint (even with one different slide between them), replace one with a structurally different archetype. Exception: if the middle slide is a breathing slide (section-divider, stat-hero, quote-pull), the triplet check passes.

### Issue 4: Slide 7 (78%) — Right Column Metric Cards Feel Vertically Clustered
- **Severity**: minor
- **Category**: spacing, rhythm
- **Frequency**: 1/1 asymmetric stat-hero slides
- **Description**: The right column of slide 7 shows three metric cards stacked vertically with `gap:16px`. Each card is `padding:20px 24px` with modest content (icon + number + label). The gap between cards is adequate but the cards look compressed — they each have ~2 lines of content plus icon, yet they share equal height from the grid's `1fr 1fr 1fr` rows. At 16px gap, the three cards with their labels look slightly squeezed against each other.
- **Evidence**: PNG 7 — right column cards are readable but tight. The "3,8" number card, NPS 84 card, and "<2 ч" card each have adequate space but the overall column feels packed.
- **Root cause**: Rule 30 (two-layer pattern with grid 1fr rows) is applied but the gap value (16px) is at the minimum. For 3 stacked metric cards, 20-24px gap creates better breathing.
- **Proposed skill fix**: Add to SKILL.md Rule 30 footnote:
  > **Metric card column spacing**: When stacking 3 metric cards in a column (asymmetric stat-hero), use `gap:20px` minimum. At 16px gap with 3 cards each containing icon + hero number + label, the column reads as crowded. 20-24px creates visual separation between cards without wasting slide space.

### Issue 5: Cover Slide — Dot Grid Decorative Pattern Partially Obscured
- **Severity**: minor
- **Category**: decoration
- **Frequency**: 1/1 cover slides
- **Description**: The cover slide has a dot grid in the top-left (white dots on teal), but the grid is partially obscured by the slide heading text which also occupies the center. The decorative dot grid is visible but the overlap with text creates a slightly noisy background in the upper-left area behind the heading. The dot grid would be better placed in the bottom-left or right side without text overlap.
- **Evidence**: PNG 1 — white dot grid faintly visible behind/around the "FORMA создаёт бренды" text. Low visual interference but visible.
- **Root cause**: The cover-hero archetype always places the heading in the center, and the dot grid was placed top-left. With a 3.6rem heading spanning ~600px width, the dots appear behind the left portion of the heading text on teal bg.
- **Proposed skill fix**: Add to cover-hero archetype notes in SKILL.md:
  > **Cover decorative placement**: On cover slides with centered headings, do NOT place dot grids or dense patterns in the upper-center zone (300px × 300px centered box). Use bottom-left, bottom-right, or extreme top-right corners for dot grids. The center/top area is the heading zone and decoration there creates noise rather than atmosphere.

---

## Slide-Specific Issues

### Slide 3: Card labels skip "02" numbering context
- **Description**: The second card in the 2×2 grid is styled with the accent gradient (teal tint + teal border) to visually promote it. However, this accent treatment is the SAME as the accent card style used in slide 5's bento-grid. The visual accent technique repeats exactly.
- **Severity**: minor

### Slide 6: Ghost "06" has good opacity but competes with text
- **Description**: The ghost "06" numeral is at ~0.14 opacity — clearly visible, as intended. However, the numeral's positioning (right-center) creates an implicit right visual weight that the left-aligned text tries to balance. The result is a slightly lopsided composition. Moving the numeral to bottom-right or slightly lower would allow the heading text more visual breathing room.
- **Severity**: minor

---

## What Worked Well

1. **Archetype variety**: 6 distinct archetypes used across 8 slides (cover-hero, stat-hero centered, timeline-horizontal, asymmetric-split, bento-grid, section-divider, stat-hero asymmetric, cta-warm). Excellent structural variety.
2. **Section divider visual weight**: Slide 6 uses left-alignment + ghost "06" + horizontal rule — a genuinely different visual pattern from slide 1's centered cover. The "Section divider differentiation" rule from recent iterations is working.
3. **Stat-hero variation**: Slide 2 uses centered stat-hero, slide 7 uses asymmetric stat-hero (left hero + right metric stack). Two stat-hero slides that are visually distinct — the stat-hero variation rule is working.
4. **Bento-grid execution (slide 5)**: Featured card left (1.2fr), two smaller cards right (1fr) — proper large+small hierarchy. The accent card at bottom-right (solid teal) creates strong visual climax within the slide.
5. **Color conviction**: Teal palette is clean, non-AI (not purple/indigo). Warm cream base + teal accent + warm white surface. All text contrast passes WCAG.
6. **CTA slide (slide 8)**: Clear action title "Давайте обсудим — первая встреча бесплатно." Contact info visible. Not "Спасибо" — ✓.
7. **Ghost "06" on section divider**: Section divider on bg-accent with ghost number is the most visually memorable slide. The ghost number opacity is above 0.14 — visible but not intrusive.
8. **Font discipline**: Exactly 2 font identities (Outfit headings + DM Sans body). No mixing, no 3rd font. Hero numbers use Outfit. ✓

---

## Design Summary

- **Palette type**: light
- **Palette mood**: professional warmth — teal on warm cream
- **Font character**: geometric-sans (Outfit) + humanist (DM Sans)
- **Decoration style**: geometric (dot grids, arcs, radial glows)
- **Strongest axis**: Typography drama (hero numbers at 5.8rem, good 3-level scale)
- **Weakest axis**: Composition variety (slides 3 and 5 share 2×2 grid fingerprint, eyebrows on all slides reduce diversity)

---

## A/B Alternatives (weakest slides)

### Slide 3 A/B (current avg 7.0 — weakest with slide 5)

**Current**: 2×2 grid of 4 process cards — label + heading top, grid below
**Alternative B**: Timeline zigzag variant — 4 steps in a single vertical flow with numbered badges on the left, description text right. Creates left-right visual movement. Avoids 2×2 grid that duplicates slide 5.
```
Step 1 (circle badge) → Исследование | detail text
Step 2 (square badge) → Позиционирование | detail text
Step 3 (circle badge) → Визуальная система | detail text
Step 4 (square badge) → Внедрение | detail text
```
**Why B is better**: The vertical flow with alternating badge shapes creates motion through the slide. Currently avoided (preset `avoid: timeline-zigzag`) but for 4 steps this would differentiate from the bento-grid on slide 5. If timeline-horizontal continues to produce 2×2 grids that visually duplicate bento-grids, the `avoid` list should be reconsidered for process slides.

### Slide 5 A/B (current avg 7.0 — weakest with slide 3)

**Current**: Bento-grid — large featured card left (icon + "Задача" description), two small cards right
**Alternative B**: Asymmetric-split variant — left 40% shows large "200K" typographic hero (no card wrapper), right 60% shows context: task, solution, result as 3 rows with colored left-borders.
```
[200K]      | Задача: доверие к платформе с нуля
регистраций | Решение: модульная система + живая типографика
            | Эффект: +первый месяц запуска
```
**Why B is better**: Two portfolio slides (4 and 5) both now use a visual element prominently — slide 4 has +47% circle, slide 5 would have 200K typographic hero. The key metric would be visually dominant and immediately readable. Currently the "200K" is buried in a small accent card on the right side of slide 5.
