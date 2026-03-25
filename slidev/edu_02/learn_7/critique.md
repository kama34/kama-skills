# Critique: Фонд «Шаг вперёд» — Годовой отчёт (Learn Iteration 7)

## Overall Score: 7.8/10

## AI Detection Score: 9/50 — Well within "AI-assisted, well customized" range

### AI Detection Breakdown
- Color (max 10): 1/10 — Teal is borderline (not purple, hue ~174°, safe), warm cream backgrounds, no purple/indigo
- Typography (max 8): 0/8 — Outfit + DM Sans, no generic fonts
- Layout (max 8): 2/8 — Asymmetric layouts present; no 3+ column icon-trio repetition; one section follows center pattern but slides 3 and 8 differ visually
- Visual effects (max 8): 2/8 — Consistent rounded corners (present but purposeful), no glassmorphism, no dramatic float-shadows
- Images (max 8): 0/8 — No stock photos, CSS-only visuals
- Content structure (max 8): 2/8 — Cost-of-inaction slide present (slide 11); action titles mostly strong; one statistic (18% growth) lacks source citation
- Content quality (max 6): 2/6 — Content is fund-specific with real names and numbers; tone is appropriately mission-driven
- Metadata (max 4): 0/4 — No AI tool metadata

**Total: 9/50** → "AI-assisted, well customized"

---

## Per-Slide Scores

| Slide | Comp | Shape | Font | Impact | Layout | Typo | Color | Content | Decor | AVG |
|-------|------|-------|------|--------|--------|------|-------|---------|-------|-----|
| 1 (cover-hero) | 9 | 8 | 9 | 9 | 9 | 8 | 9 | 8 | 8 | 8.6 |
| 2 (stat-hero centered) | 8 | 8 | 9 | 8 | 8 | 9 | 8 | 8 | 7 | 8.1 |
| 3 (section-div A) | 8 | 7 | 8 | 8 | 8 | 8 | 9 | 7 | 8 | 7.9 |
| 4 (bento-grid) | 8 | 8 | 8 | 7 | 8 | 7 | 8 | 8 | 7 | 7.7 |
| 5 (asymmetric-split) | 8 | 9 | 8 | 8 | 9 | 8 | 8 | 8 | 7 | 8.1 |
| 6 (two-col-text) | 7 | 7 | 8 | 7 | 7 | 7 | 7 | 8 | 6 | 7.1 |
| 7 (stat-hero asymmetric) | 9 | 8 | 8 | 8 | 9 | 8 | 8 | 8 | 8 | 8.2 |
| 8 (section-div B) | 9 | 7 | 9 | 9 | 9 | 9 | 9 | 8 | 8 | 8.6 |
| 9 (timeline-horiz) | 8 | 7 | 8 | 7 | 8 | 7 | 8 | 8 | 7 | 7.6 |
| 10 (profile-grid) | 8 | 8 | 8 | 7 | 8 | 7 | 7 | 8 | 7 | 7.6 |
| 11 (stat-hero text) | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8.0 |
| 12 (cta-warm) | 8 | 7 | 8 | 8 | 8 | 8 | 9 | 9 | 8 | 8.1 |

**Overall: 7.8/10**

---

## Systemic Issues (affect the skill itself)

### Issue 1: Profile-grid — 3-row layout leaves bottom padding insufficient when last row spans full width
- **Severity**: minor
- **Category**: layout, spacing
- **Frequency**: 1 slide (slide 10)
- **Description**: The profile-grid with 4 regular cells + 1 full-span cell creates a 5-item layout in a 2×3 grid, but the 5th cell spans both columns, making the grid asymmetric with empty visual space in the right column at row 3. The 5-cell layout works but the full-span bottom row creates a "footer" feel that competes with the slide's heading for visual weight.
- **Evidence**: Slide 10 PNG — bottom row (spanning both columns) with mission text renders with noticeably more whitespace in padding than the cells above it. Height is auto, while above cells have equal height by 1fr.
- **Root cause**: The SKILL.md profile-grid archetype only describes a 2×3 grid with 6 equal cells. There's no guidance on the special case where the team has <6 members, causing improvised adaptations.
- **Proposed skill fix**: Add a note to the profile-grid archetype in composition-archetypes.md: "For teams with <6 members, use the 4+footer pattern: 2×2 grid of member cards + 1 full-span contextual row at bottom. The footer row MUST have explicit `height: 72px; padding: 0 24px;` to match the stat-footer-band height convention. Never leave a grid cell with auto height when adjacent cells have 1fr."

### Issue 2: Two-col-text heading too large — wraps onto two lines reducing whitespace
- **Severity**: major
- **Category**: spacing, typography
- **Frequency**: 1 slide (slide 6), but could recur with long Russian titles
- **Description**: Slide 6 heading "«Рядом» — 1 200 сессий в месяц, 4 минуты до психолога" is 59 characters and wraps to 2 lines at 2.3rem. This consumes ~25% of the vertical space, leaving the card grid below cramped. The heading font size for two-col-text should scale DOWN for longer titles.
- **Evidence**: Slide 6 PNG — heading wraps to 2 lines, card grid below is visibly compressed. The bottom edge of the grid cards is near the slide bottom with insufficient padding.
- **Root cause**: SKILL.md Step 5 specifies heading minimum 2.2rem but doesn't specify a MAXIMUM or a scaling rule for long headings in split-layout archetypes.
- **Proposed skill fix**: Add to SKILL.md Step 5 heading writing rules: "For two-col-text and asymmetric-split archetypes, if the planned heading exceeds 50 characters, reduce to 2.1rem maximum and shorten the text. Target: heading occupies at most 2 visual lines. Long Russian action titles in these layouts should omit conjunctions or compress the supporting context: move secondary detail to the card content."

### Issue 3: bento-grid featured card stat number too small relative to available space
- **Severity**: minor
- **Category**: typography, visual impact
- **Frequency**: 1 slide (slide 4)
- **Description**: In the bento-grid featured card (left 60% area), the 72% metric sits at approximately 2.8rem with an icon to its left. The card occupies a large area but the hero number inside it is not dramatically oversized. Industry standard: featured cells in bento grids should have their primary metric at 3.5-4rem minimum.
- **Evidence**: Slide 4 PNG — the 72% number is visually smaller than expected given the card's footprint. It does not feel like a "featured" metric; it reads as a regular card stat.
- **Root cause**: The bento-grid archetype skeleton in composition-archetypes.md shows `{{FEATURED_ITEM}}` as a placeholder without specifying the minimum font size for the featured metric within it. The generation rule about hero numbers (≥4rem) applies to full stat-hero slides but is not explicitly extended to featured bento-grid cells.
- **Proposed skill fix**: Add to the bento-grid archetype description: "Featured card (spanning full row height): primary metric MUST be ≥3.5rem. Do NOT pair the metric with an icon at the same flex row — put the icon separately in a smaller container above or below the number to allow the number to expand to full size."

### Issue 4: Decorative elements on bg-alt slides still subtle
- **Severity**: minor
- **Category**: decoration
- **Frequency**: slides 5 and 10 (bg-alt slides)
- **Description**: Both bg-alt slides (5 and 10) have decorative radial glows that are somewhat visible but not dramatically so. The composition-archetypes.md bg-alt guidance specifies 1.5x opacity boost, which was applied, but the warm gray (#E8E6DF) background still somewhat absorbs the teal glow.
- **Evidence**: Slide 5 PNG — top-right glow is visible but soft. Slide 10 PNG — arc and glow are present but need more contrast against the warm gray.
- **Root cause**: The rule says "increase opacity by additional 1.5x on bg-alt" but doesn't specify whether to ALSO use a darker decorative color (navy at low opacity) as an alternative for better differentiation.
- **Proposed skill fix**: Add to SKILL.md Rule 8 (decorative motifs on bg-alt): "On bg-alt slides, PREFER using dark accent color (var(--color-text) at 0.12-0.18 opacity) for arc and border decorations instead of teal — warm-on-warm creates stronger contrast than teal-on-warm-gray. Filled glows (radial-gradient with teal) remain effective. The rule: arcs/borders → dark color; fills/glows → teal color."

---

## Slide-Specific Issues (one-off problems)

### Slide 2: Stat pill badges render at correct size but line-height may cause slight vertical offset
- **Description**: The 3 stat pills ("2 800 образование", "890 медицина", "510 психология") render correctly but the icon numbers sit slightly close to the top of the pill container. Minor visual.
- **Severity**: minor

### Slide 9: Timeline grid — Q3 2026 card content wraps to 3 lines (slightly dense)
- **Description**: "5 новых корпоративных партнёров · Расширение «Рядом»" wraps to 3 short lines in the timeline grid cell. The cell height is constrained by 1fr grid.
- **Severity**: minor — grid rows are even but this cell feels slightly tighter.

### Slide 11: "100 к" renders as "100 к" — the Cyrillic "к" (thousands abbreviation) should be "100 т" or "100K ₽" for clarity
- **Description**: "100 к" using Cyrillic к (similar to Latin K) is ambiguous. Should be "100 000 ₽" or "100 тыс ₽" for unambiguous reading.
- **Severity**: minor — cosmetic

---

## What Worked Well

1. **Section divider differentiation** (slides 3 and 8): Two visually distinct variants — centered with circles (variant A) vs. left-aligned with ghost number (variant B). This is the first cycle where section dividers are genuinely different compositions.

2. **Stat-hero variation** (slides 2, 7, 11): Three distinctly different stat-hero structures: centered with pills (slide 2), asymmetric with bars (slide 7), text-hero statement (slide 11). All feel unique.

3. **Adjacent fingerprint uniqueness**: No two adjacent slides share the same visual composition. The focal gravity alternates: center (slide 1) → center (slide 2) → center (slide 3) → upper-left (slide 4) → right (slide 5) → left (slide 6) → left (slide 7) → left (slide 8) → left-grid (slide 9) → upper-left (slide 10) → center (slide 11) → center (slide 12). Issue: slides 6-8 are all left-dominant — a minor gravity clustering.

4. **bg-alt opacity rule applied**: Slides 5 and 10 show enhanced decorative opacity on warm backgrounds. Rule works, just needs the dark-color alternative noted above.

5. **Ghost number "08"** on slide 8: Clearly visible at ~0.14 opacity against teal. Passes the minimum 0.12 threshold.

6. **Action titles**: All 12 slide titles pass the Ghost Deck test — reading them in sequence tells a coherent story about the nonprofit.

7. **Cost-of-inaction slide** (slide 11): Present and effective. "2 800 детей останутся без программ" is a compelling COI frame for a nonprofit fundraising deck.

8. **Eyebrow discipline**: 3 eyebrows used on 3/3 allowed content slides. All others have headings that speak for themselves.

9. **Icon shape diversity**: Circle (slides 4 featured, 5), rounded-square (slides 4 small cards, 6), star-circle with amber (slides 4, 10). Not all identical.

---

## Design Summary
- **Palette type**: light
- **Palette mood**: "warm cream with teal conviction — nonprofit warmth, professional clarity"
- **Font character**: geometric-sans + humanist (Outfit / DM Sans)
- **Decoration style**: radial-gradient glows + dot grids + arc rings — all teal-based, consistently radial
- **Strongest axis**: Layout uniqueness (9.0 avg) — archetypes genuinely differ per slide
- **Weakest axis**: Decorative quality (7.4 avg) — bg-alt slides need stronger motifs

---

## A/B Alternatives (weakest slides)

### Slide 6 (score 7.1) — Alternative A: Reduce heading, add more card padding
Instead of the current wrapping 2-line heading:
- Shorten to "«Рядом» — психологическая поддержка онлайн" (40 chars, fits 1 line at 2.2rem)
- Move "1 200 сессий" and "4 минуты" from bottom cards to a hero stat row directly under heading
- Use 2 text-only cards for qualitative info (hotline, team)

### Slide 6 — Alternative B: Convert to asymmetric-split
- Left side: large centered "4 мин" in teal circle (like slide 5 pattern)
- Right side: bulleted list with icon + text rows
- Would create stronger visual contrast and break the consecutive left-anchor fingerprint (slides 6, 7, 8 are all left-dominant)
