# Critique: MLOps Воркшоп (Learn Iteration 9/10)

## Overall Score: 7.4/10

---

## Per-Slide Scores

| Slide | Comp | Shape | Font | Impact | Layout | Typo | Color | Content | Decor | AVG |
|-------|------|-------|------|--------|--------|------|-------|---------|-------|-----|
| 1 (Cover) | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 8 | 8 | **8.7** |
| 2 (87%) | 8 | 8 | 9 | 9 | 8 | 9 | 8 | 9 | 7 | **8.3** |
| 3 (Section A) | 9 | 7 | 8 | 8 | 9 | 8 | 9 | 8 | 7 | **8.1** |
| 4 (Icon trio) | 7 | 8 | 8 | 7 | 7 | 7 | 8 | 7 | 7 | **7.3** |
| 5 (Levels) | 8 | 7 | 8 | 7 | 8 | 7 | 8 | 8 | 7 | **7.6** |
| 6 (Section B) | 9 | 7 | 8 | 9 | 9 | 8 | 9 | 8 | 8 | **8.3** |
| 7 (Bento min) | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 7 | **7.9** |
| 8 (Mosaic adv) | 8 | 8 | 8 | 7 | 8 | 7 | 8 | 8 | 7 | **7.7** |
| 9 (Section C) | 8 | 7 | 8 | 8 | 9 | 8 | 9 | 8 | 8 | **8.1** |
| 10 (Pipeline) | 8 | 7 | 8 | 7 | 8 | 8 | 8 | 8 | 7 | **7.7** |
| 11 (Monitor) | 9 | 9 | 8 | 8 | 9 | 8 | 8 | 8 | 8 | **8.3** |
| 12 (Section D) | 9 | 8 | 8 | 9 | 9 | 8 | 9 | 7 | 8 | **8.3** |
| 13 (Mistakes) | 7 | 7 | 8 | 6 | 7 | 7 | 7 | 8 | 6 | **7.0** |
| 14 (Text hero) | 7 | 7 | 8 | 7 | 7 | 8 | 8 | 7 | 7 | **7.3** |
| 15 (Checklist) | 7 | 8 | 8 | 7 | 7 | 7 | 7 | 8 | 7 | **7.3** |
| 16 (CTA) | 8 | 8 | 8 | 9 | 8 | 8 | 9 | 9 | 9 | **8.4** |

## Overall: 7.9/10

---

## AI Detection Score (50-point rubric)

| Category | Max | Score | Notes |
|----------|-----|-------|-------|
| Color | 8 | 1 | Teal is distinctive, non-AI-default. Warm amber secondary used. No purple/indigo. |
| Typography | 8 | 2 | Outfit + DM Sans is a strong non-generic pair. Good scale drama. |
| Layout | 8 | 2 | 4 section divider variants is a strong differentiator. Multiple archetypes. |
| Visual effects | 6 | 2 | Decorative elements present but relatively mild on content slides. |
| Imagery | 6 | 0 | No photos — CSS atmospheric treatment only. |
| Content structure | 6 | 2 | Narrative flow is logical. Action titles mostly strong. |
| Content quality | 4 | 1 | Good specificity (Gartner source, 15% revenue drop). |
| Metadata | 4 | 0 | Speaker, date, event visible. |

**Total AI Detection Score: 10/50** — Does NOT look AI-generated.

---

## Systemic Issues (affect the skill itself)

### Issue 1: Icon-trio with 4 items creates imbalance at deck-wide level
- **Severity**: major
- **Category**: composition, layout
- **Frequency**: Slide 4 — 4 icon items in a single row creates uneven horizontal spacing. The archetype specification says "3-5 items" but 4-wide at 52px gap creates a very compressed horizontal row on 16:9.
- **Description**: The icon-trio archetype is defined for 3-5 items but 4 items in one horizontal row gets crowded. At 180px max-width each + 52px gaps = approx 900px total for 4 items which barely fits in a 960px content area.
- **Evidence**: Slide 4 PNG shows all 4 icons fitting but text below is clearly wrapping to 3 lines on some items, creating uneven vertical heights.
- **Root cause**: Archetype description says "3-5 items" without specifying max items for horizontal layout. 4-5 items work better as 2×2 or 2+3 grid, not a single row.
- **Proposed skill fix**: Add to icon-trio archetype spec: "For 4+ items: prefer 2-row layout (2×2 grid) or cap description length at 8 words maximum when using single-row to prevent multi-line text wrapping per item."

### Issue 2: Content slides 7 and 8 use same structural fingerprint (label+heading+card-grid)
- **Severity**: major
- **Category**: layout diversity (Principle 2)
- **Frequency**: Slides 7 → 8 consecutive
- **Description**: Slides 7 (bento-grid featured-left) and 8 (card-mosaic 2×2) both start with: `[eyebrow label]` + `[2.4rem heading]` + `[card grid filling remaining space]`. While the card configurations differ, the overall visual fingerprint is identical: top-left anchor heading, content fills below. No structural break between them.
- **Evidence**: Looking at slides 7 and 8 PNG back-to-back, both have heading at top-left, grid filling 70% of slide. Only the card layouts inside differ.
- **Root cause**: The composition plan assigns different archetypes (bento-grid vs card-mosaic) but both belong to the `grid` group and both render with the same top-level structural pattern. The adjacent structural fingerprint check in Step 4.5 should catch this but didn't flag it.
- **Proposed skill fix**: Strengthen the adjacent structural fingerprint rule in SKILL.md Step 4.5: "After assigning archetypes, explicitly check slides in the `grid` group that appear consecutively. Even if their internal card configurations differ, they share the `label-top-left + heading + card-grid` fingerprint. When two consecutive grid-group slides are unavoidable, at least ONE must use an asymmetric grid ratio (e.g., 1.5fr/1fr vs 1fr/1fr) to create visual variety within the grid pattern."

### Issue 3: Section dividers on bg-accent use the same bg-accent value — 4 in a row all look like "teal slides"
- **Severity**: major
- **Category**: visual rhythm, section differentiation
- **Frequency**: Slides 3, 6, 9, 12 — all 4 section dividers use `--bg-accent` (#0D9488 solid teal)
- **Description**: All 4 section dividers share the same background color. While their layouts differ (centered, left+ghost, rule, asymmetric), they all produce a "solid teal slide" feel. A viewer watching in sequence sees: teal → content → content → teal → content → content → teal → ... The sections don't feel structurally distinct from each other.
- **Evidence**: Slides 3, 6, 9, 12 all render as the same solid teal green. Slide 12 adds a dark right panel which helps, but slides 3/6/9 are all the same hue.
- **Root cause**: The section divider differentiation rule (Step 4.5) specifies layout variants but does NOT specify background color variants. The rule says "4 different composition variants" but allows the same bg-accent for all.
- **Proposed skill fix**: Add to Step 4.5 section divider differentiation rule: "When a deck has 3+ section dividers, they MUST vary on at least one background dimension in addition to layout. Options: (A) bg-accent at full opacity (standard), (B) bg-accent with a 15% black overlay: `rgba(0,0,0,0.15)` creating a darker teal, (C) bg-alt with oversized accent-colored type (2× normal heading size) to compensate for the lighter background, (D) bg-base with a full-bleed accent color block occupying 60%+ of slide area. The goal: no two section dividers should look like the same solid color panel."

### Issue 4: Slide 13 — lower half of slide is blank/empty
- **Severity**: minor
- **Category**: spacing, visual arc
- **Frequency**: Slide 13 only
- **Description**: The two-col layout with heading + 4 items left + 3 items right leaves a significant empty zone below the content (approximately 35% of slide height). The content block is compact (~280px) while the full content area is ~450px, leaving ~170px blank below.
- **Evidence**: Slide 13 PNG shows heading at top, content in middle, large empty space below.
- **Root cause**: `flex-direction:column; justify-content:flex-start; padding-top:8px` causes content to sit at the top of the available area without distributing vertically.
- **Proposed skill fix**: Add to two-col-text archetype note: "When content height is less than 65% of available slide area, add a summary/insight callout below the two columns as a visual anchor. Example: a single teal-bordered box with the key takeaway spanning full width."

---

## Slide-Specific Issues

### Slide 4: Icon descriptions vary in line count
- **Description**: "Дрейф данных и деградация качества в реальном времени" wraps to 3 lines while "Любой результат можно повторить точно" is 2 lines. Creates uneven vertical heights across the icon row.
- **Severity**: minor

### Slide 5: Level cards — content wraps inconsistently
- **Description**: Level 0 card ("Jupyter Notebooks, деплой вручную, нет версионирования") wraps to 3 lines while Level 2 wraps to 2 lines. Cards look visually uneven.
- **Severity**: minor

### Slide 13: Decorative arc barely visible
- **Description**: The `slide-decor-arc` class renders a thin arc at bottom-left but on bg-base (warm cream) the arc is very faint. The decorative element adds almost no visual character to this slide.
- **Severity**: minor

---

## What Worked Well

1. **4 section divider variants** — All 4 are genuinely visually distinct (centered+glow, left+ghost number, full-width rule, asymmetric+warning panel). This is the strongest design achievement in the deck.
2. **2 timeline layout variants** — Slide 5 (4×1 horizontal progression) vs Slide 10 (2×2 grid with accented steps) are structurally different despite both showing 4 sequential items.
3. **2 card-mosaic variants** — Slide 7 (bento featured-left with large card) vs Slide 15 (checklist 2×2 with icon+text) are genuinely different card patterns.
4. **Eyebrow discipline** — Exactly 4 eyebrows on 14 content slides (28.5%, within the 30% limit). Section dividers correctly exempt.
5. **Cover quality** — The teal cover with Outfit headings, nested circles, metadata dots row makes a strong first impression.
6. **Asymmetric split on slide 11** — The 5% metric on the left + text rows on the right is the strongest content slide in the deck.
7. **Section 12 warning tone** — The asymmetric dark right panel with ghost alert icon creates genuinely distinct "danger zone" feel.
8. **Source citation** — Gartner 2025 citation on slide 2. 15% revenue incident on slide 13. Good specificity.
9. **No "Спасибо" ending** — CTA has clear action (GitHub link, next workshop date, community).
10. **Warm amber** used on slide 13 for mistake numbering — creates semantic color variety without breaking the primary palette.

---

## Design Summary

- **Palette type**: light
- **Palette mood**: professional teal warmth — cream backgrounds, teal accent, warm amber secondary
- **Font character**: geometric-sans (Outfit heading) + humanist (DM Sans body)
- **Decoration style**: geometric + minimal (arcs, dot grids, radial glows)
- **Strongest axis**: Composition variety (section divider differentiation, multiple archetypes)
- **Weakest axis**: Decorative quality (motifs are present but subtle; content slides feel slightly plain)

---

## A/B Alternatives (for weakest slides)

### Slide 13 Alternative (avg 7.0 — weakest)

**Current**: Two-col text — numbered items left, consequence bullets right, large bottom gap.

**Alternative A** — Add a bottom callout spanning both columns:
```
After the two columns: a single full-width teal-bordered card:
"Итог: каждая из этих ошибок стоила команде > 40 часов ручной работы"
```
This anchors the bottom zone and creates a clear takeaway.

**Alternative B** — Switch to comparison-table archetype:
4 rows: [mistake number] | [mistake] | [consequence]. Fills vertical space naturally, very scannable for technical audience.

**Recommendation**: Alternative B better serves a technical ML workshop audience — engineers prefer structured tables over prose-heavy columns.
