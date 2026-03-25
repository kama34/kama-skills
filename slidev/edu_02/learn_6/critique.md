# Critique: Онбординг в TaskFlow SaaS (Learn Iteration 6)

## Overall Score: 7.2/10

## AI Detection Score: 12/50

**Categories breakdown:**
- Color (0-8): 1 — Teal palette is deliberate and distinctive, not AI-default purple/indigo
- Typography (0-7): 1 — Outfit/DM Sans is a strong, non-generic pairing
- Layout (0-8): 2 — 4 section dividers differ visually (centered/left/full-rule) — good, some content slides still feel templated
- Visual effects (0-6): 1 — Decorative motifs (dot grids, glows, arcs) are present and varied
- Imagery (0-5): 0 — No photos, all CSS/SVG visual elements
- Content structure (0-8): 4 — Main weakness: some slides still feel repetitive in structure (bento-grid on 4 and 12 are visually similar)
- Content quality (0-4): 2 — Action titles are mostly strong, some slides still have eyebrow density issues in earlier slides
- Metadata (0-4): 1 — Clean professional finish

**Total: 12/50 → Below 16 threshold → Does NOT look AI-generated** ✓

---

## Systemic Issues (affect the skill itself)

### Issue 1: Section Divider Lower Empty Space
- **Severity**: major
- **Category**: rhythm / layout
- **Frequency**: 2/4 section slides (slides 3, 11 — though fixed by centered content; slide 7 has partial empty lower half)
- **Description**: Section dividers using left-aligned layout (variant B) leave a large empty lower third after the subtitle. The horizontal rule footer anchor helps but the slide still feels top-heavy at 40% height utilization.
- **Evidence**: Slide 7 PNG — all content is concentrated in the upper 45% of the slide. Lower 40% is empty teal with only the footer rule.
- **Root cause**: SKILL.md section-divider archetype does not specify minimum content block height or a lower anchor requirement beyond the decorative rule. The left-aligned variant lacks a structural "lower zone" element to balance the composition.
- **Proposed skill fix**: Add to section-divider differentiation rule: "When using left-aligned variant B, add a tertiary element in the lower zone — either a row of status/progress pill chips showing section count ('01 of 03'), or a translucent feature-list preview of what's coming in this section. This grounds the lower half without adding information density."

### Issue 2: Two Bento-Grid Slides with Visually Similar Structure
- **Severity**: major
- **Category**: layout / rhythm
- **Frequency**: 2 slides (4 and 12) — both use 1.25fr/1fr two-column bento grid with identical grid proportions
- **Description**: Slides 4 (Step 1: Project creation) and 12 (Dashboard) both use bento-grid with a large featured left card spanning 2 rows and 2 smaller right cards. The visual fingerprint is identical. The heading is top-left in both, same proportion split.
- **Evidence**: Comparing slide 4 and slide 12 PNGs — same grid ratio, same featured left card visual weight, same 2-row right column. Only content differs.
- **Root cause**: The composition plan correctly assigned bento-grid to both, but the entropy window (4 slides) rule didn't catch that slides 4 and 12 — separated by 8 slides — would render with the same structural fingerprint. The visual fingerprint dedup rule checks ADJACENT slides only, not global.
- **Proposed skill fix**: Add to composition plan validation: "Run visual fingerprint dedup not just for adjacent slides but globally — flag any two non-adjacent slides sharing the same fingerprint if they are both bento-grid or card-mosaic with the same column ratio. When detected, vary the grid proportions: if slide 4 uses 1.25fr/1fr, slide 12 must use 1fr/1.25fr (reverse) or 1.5fr/1fr. This creates mirror variation that reads as intentional, not accidental."

### Issue 3: Icon Container bg-alt Visibility (Partial)
- **Severity**: minor
- **Category**: icons
- **Frequency**: 1 slide (slide 5 — bg-alt background)
- **Description**: On slide 5 (bg-alt warm grey), the third icon container (Guest) uses `rgba(text-rgb, 0.06)` background which is nearly invisible against bg-alt. The icon itself is teal-colored but the container border is barely visible. The rule about icon-ghost on bg-alt being invisible applies here.
- **Evidence**: Slide 5 PNG — third icon container (Guest) has a visibly weaker presence than Owner/Admin containers. Container boundary is faint.
- **Root cause**: SKILL.md Rule for icon-container bg-level adaptation specifies "on bg-alt slides, replace icon-ghost with icon-circle" but doesn't cover the case where the designer intentionally uses a lower-opacity container to signal semantic hierarchy (primary/secondary/tertiary roles). The rule needs to distinguish between accessibility failure (invisible) and intentional hierarchy.
- **Proposed skill fix**: Update icon container bg-alt rule: "On bg-alt slides, when using 3 icon containers with intentional visual hierarchy (primary/secondary/tertiary), use: primary = icon-container (teal bg), secondary = icon-rounded (teal bg), tertiary = icon-container with `rgba(text-rgb, 0.12)` minimum background + `rgba(text-rgb, 0.18)` border — NOT rgba(0.06). The 0.06 opacity is invisible on warm grey bg-alt."

### Issue 4: Asymmetric-Split Visual Element Sizing Inconsistency
- **Severity**: minor
- **Category**: layout
- **Frequency**: 2 slides (8 and 13) — both use asymmetric-split
- **Description**: Both asymmetric-split slides (8: board, 13: reports) use a large circle container for the visual element on one side. The circles render at 160-180px which is appropriately large. However, slide 13 has the text content on the left (3fr) and visual on the right (2fr) while slide 8 has visual on the left (2fr) and text on right (3fr). This is GOOD differentiation — alternating dominant side correctly.
- **Evidence**: Slides 8 and 13 — visual elements correctly alternate sides. This is working well.
- **Note**: This is actually a positive finding — the stat-hero variation rule IS being applied correctly to asymmetric-split layouts.

### Issue 5: CTA Slide Subtle Color Smoothness
- **Severity**: minor
- **Category**: arc / cta
- **Frequency**: 1 slide (slide 15)
- **Description**: The CTA slide uses `linear-gradient(145deg, --bg-accent 0%, #0a6e65 100%)`. The penultimate slide (14: Support) uses bg-base (cream). The bg-level transition from cream to teal is abrupt — the pre-CTA slide should ideally use bg-alt as a bridge per the CTA color smoothness rule. However, the warm amber glow on the CTA slide provides a subtle temperature bridge.
- **Evidence**: Slide 14 is pure cream/warm-grey, slide 15 is teal. No visual bridge in slide 14.
- **Root cause**: Composition plan assigned bg-base to slide 14, not bg-alt. The pre-CTA bridge rule was not applied.
- **Proposed skill fix**: In composition plan background level algorithm, explicitly enforce: "The slide immediately before the CTA (position N-1) MUST use --bg-alt if the CTA uses --bg-accent and the N-2 slide uses --bg-base. If N-1 is already an icon-trio or content slide on bg-base, change it to bg-alt."

---

## Slide-Specific Issues (one-off problems in this presentation)

### Slide 10: Heading Stack Too Tall
- **Description**: Without the eyebrow, the 3rem heading "Документация живёт / рядом с задачами" wraps to 4 lines at the given width (3fr column ~540px). This pushes the body text and pills quite low.
- **Severity**: minor — legible and functional, just visually top-heavy

### Slide 11: Subtitle Text Center-Alignment Issue
- **Description**: The subtitle "Видеть — значит управлять..." appears centered but has a slightly awkward word wrap ("в реальном / времени" on a new line). The max-width:600px doesn't fully constrain the wrap at this font size.
- **Severity**: minor

### Slide 12: Burndown Chart Mock Bars Too Small
- **Description**: The mock burndown chart using CSS bars (6 bars, h-48px) is clearly decorative but the bars are very thin and the visual reads as "5 thin rectangles" rather than a chart. Adding min-height: 8px and slightly wider bars would make it more legible.
- **Severity**: minor

---

## What Worked Well

1. **4 visually distinct section dividers** — centered+glow, left+ghost-number+dotgrid, full-width+rule+circles — all genuinely different. The ghost number "01/02/03" system creates a professional numbering convention.
2. **Eyebrow discipline** — Only 3 eyebrows used across 15 slides (slides 2, 5, 9), well under the 30% limit. Headings speak for themselves on 12 slides.
3. **Hero stat slide (slide 2)** — "12 часов" at 6rem with footer band is visually strong. The stat-footer-band component grounds the slide well.
4. **Section divider differentiation rule fully followed** — All 4 section slides (3, 7, 11 + cover as pseudo-section) use different compositions. The ghost number progression (01/02/03) is a strong narrative device.
5. **Asymmetric-split alternation** — Slides 8 (visual-left) and 13 (text-left) correctly alternate the dominant side.
6. **Icon container variety** — circle, rounded-square, and neutral-ghost used across the deck. No single-type uniformity.
7. **Warm accent (amber) used sparingly** — Only on WIP-limits bullet (slide 8) and promo star (slide 15). Correct restraint.
8. **CTA slide** — Strong visual finish. The amber promo row is a genuine attention-grabber without over-designing.
9. **Decorative motif rotation** — dot grids, radial glows, arcs, and ghost numbers rotate correctly across slides. No two adjacent slides share the same motif.
10. **Action titles** — "12 часов экономит TaskFlow каждой команде каждую неделю", "Спринт-планирование за 10 минут", "Поддержка — ответ за 5 минут, сообщество 8 000+" — all strong, specific, claim-based.

---

## Design Summary
- **Palette type**: light
- **Palette mood**: warm cream with teal authority — professional SaaS warmth
- **Font character**: geometric-sans (Outfit heading) + humanist (DM Sans body)
- **Decoration style**: geometric (circles, arcs) + pattern (dot grids) + atmospheric (radial glows)
- **Strongest axis**: typography drama (stat-hero slide 2, strong heading hierarchy throughout)
- **Weakest axis**: composition variety (bento-grid structural fingerprint reuse on slides 4 and 12)

---

## Scoring Per Axis (9-axis scoring subroutine)

| Axis | Score | Notes |
|------|-------|-------|
| Composition variety | 6/10 | Bento-grid repeat (slides 4+12) and some templated feel on steps slides |
| Shape diversity | 7/10 | Good mix of circles, rounded squares, ghost containers |
| Font discipline | 9/10 | Strict 2-font rule followed, no blacklist violations |
| Visual impact | 7/10 | Stat hero and section dividers are strong; step slides are functional but not dramatic |
| Layout uniqueness | 7/10 | Good archetype variety; icon-trio used twice (slides 5+14) — at the limit |
| Typography drama | 8/10 | 6rem stat hero, 4rem section dividers, clear 3-tier hierarchy |
| Color conviction | 8/10 | Teal with amber warmth — decisive palette without hedging |
| Content clarity | 7/10 | Clean headlines, appropriate density; slide 10 heading slightly too tall |
| Decorative quality | 7/10 | Visible, varied motifs; ghost numbers excellent; bg-alt glow slightly muddy |

**Average: 7.33/10**

---

## A/B Alternatives (weakest slides)

### Slide 4 (bento-grid, score 6/10) — Alternative composition
**Current**: 1.25fr/1fr bento with large featured card spanning 2 rows
**Alternative A** (timeline-horizontal): Show the 3 steps (Choose template → Import → Configure) as a 3-step horizontal timeline with stage cards. Visual structure completely different from slide 12, shows the process flow.
**Alternative B** (stat-hero variant): "2 минуты" as hero number in large text, template badges as pills below, import/configure as two supporting feature chips at bottom. More drama, less information.

### Slide 14 (icon-trio, score 6/10) — Alternative composition
**Current**: Large heading + 3 icon circles at equal size
**Alternative**: comparison-table with 4 rows (docs / tutorials / chat / community) each with icon, label, and URL/detail. More specific and actionable, breaks from the icon-trio archetype used on slide 5.
