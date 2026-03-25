# Critique: Зелёная энергетика для бизнеса — Инвесторский апдейт Q1 2026 (Learn Iteration 10/10 — FINAL)

## Overall Score: 8.3/10

---

## Per-Slide Scores

| Slide | Comp | Shape | Font | Impact | Layout | Typo | Color | Content | Decor | AVG |
|-------|------|-------|------|--------|--------|------|-------|---------|-------|-----|
| 1 Cover | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | **9.0** |
| 2 Market 420млрд | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | **9.0** |
| 3 Section Div 01 | 8 | 7 | 9 | 8 | 8 | 8 | 9 | 8 | 8 | **8.1** |
| 4 Revenue 340млн | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | **8.0** |
| 5 Projects mosaic | 9 | 8 | 8 | 9 | 9 | 8 | 8 | 9 | 8 | **8.4** |
| 6 ROI 3.2yr split | 8 | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | **8.1** |
| 7 Section Div 02 | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | **9.0** |
| 8 Panel comparison | 7 | 7 | 8 | 7 | 7 | 7 | 8 | 8 | 7 | **7.4** |
| 9 Team bento | 7 | 8 | 7 | 7 | 8 | 7 | 7 | 7 | 7 | **7.2** |
| 10 COI text-hero | 9 | 7 | 9 | 9 | 9 | 9 | 8 | 9 | 8 | **8.6** |
| 11 Round B timeline | 7 | 7 | 7 | 7 | 7 | 7 | 8 | 8 | 7 | **7.2** |
| 12 CTA CEO | 8 | 8 | 8 | 8 | 8 | 8 | 9 | 9 | 8 | **8.2** |

**Overall: 8.3/10**

---

## AI Detection Score

Applying the 50-point AI detection rubric:

- **Color** (0-8): 1 — Teal accent avoids purple blacklist; warm cream palette; 3-level bg system correctly distributed. No AI tells.
- **Typography** (0-8): 1 — Outfit/DM Sans pair, zero Inter/Roboto. Clear 3+ type scales. Hero numbers at 5.5rem.
- **Layout** (0-8): 2 — Good composition variety. Minor: slides 9 and 11 both render as "2×2 grid" — structural fingerprint overlap despite different archetypes.
- **Visual effects** (0-6): 1 — Radial glows, dot grids, arcs consistently used. Single decorative gradient type. No glassmorphism.
- **Imagery** (0-6): 0 — No photos. CSS-based atmosphere only.
- **Content structure** (0-6): 2 — Action titles present. Ghost deck reads coherently. Section dividers have substantive descriptions. One issue: cover title wraps across 4 lines.
- **Content quality** (0-6): 1 — Numbers sourced (IRENA 2025). No hallucinated stats. Word counts within limits.
- **Metadata** (0-2): 0 — Correct slide count, no placeholder text.

**AI Detection Score: 8/50** — Well below the 16-point threshold. Presentation does NOT look AI-generated.

---

## Systemic Issues (affect the skill itself)

### Issue 1: Bento-grid — Icon BESIDE hero number defeats card hierarchy
- **Severity**: major
- **Category**: typography, layout
- **Frequency**: 1 slide (slide 9), but pattern is common across iterations
- **Description**: The featured bento cell places the users icon BESIDE the "180" number in a flex row. The icon takes horizontal space forcing the number to sit beside smaller text. The archetype rule says "place icon ABOVE the metric in a separate row, NOT beside it." This was in SKILL.md but not enforced in slide 9's implementation — icon+number in the same flex row.
- **Evidence**: Slide 9 PNG — "180" appears in a horizontal row with the users icon to its left, rather than icon above the number. The number reads at ~3.5rem which is below the bento minimum 3.5rem threshold, and is visually compressed.
- **Root cause**: The bento-grid archetype note in composition-archetypes.md says "place icon ABOVE the metric" but the HTML skeleton shows both in a flex row with `display:flex;align-items:center;gap:14px`. Generators follow the skeleton literally.
- **Proposed skill fix**: Update bento-grid archetype skeleton in `references/composition-archetypes.md` — change the featured cell template to stack icon ABOVE the number, not beside it. Also add a QA-0b check: "Featured bento cell: if icon and hero number are in same row, auto-fix to column layout."

### Issue 2: Two-col comparison slide lacks a column-header separation line
- **Severity**: minor
- **Category**: layout, content
- **Frequency**: 1 slide (slide 8)
- **Description**: The comparison slide 8 uses two columns (SolarTech vs Jinko Solar) but the visual separation between the two companies is only the gap between columns. There's no vertical rule or strong header treatment. The slide works but lacks the visual polish of a McKinsey-style comparison table.
- **Evidence**: Slide 8 PNG — both columns have identical row backgrounds (alternating teal/white), making the left and right columns feel like one wide table rather than a true comparison. The company headers are readable but small relative to the data rows.
- **Root cause**: The two-col-text archetype skeleton has no column header treatment beyond a label span. For comparison contexts, a more prominent column header with a bottom border line would clarify the "vs" structure.
- **Proposed skill fix**: Add a note to `references/composition-archetypes.md` under `two-col-text`: "For comparison mode, add a 2px bottom border to each column header and increase column header font-size to 1.4rem minimum."

### Issue 3: Timeline-horizontal 2×2 and card-mosaic 2×2 share identical visual fingerprint
- **Severity**: major
- **Category**: composition variety, layout
- **Frequency**: Slides 5 and 11 — both render as heading + 2×2 card grid
- **Description**: Card-mosaic (slide 5) with 1 featured + 2 stacked cards vs timeline (slide 11) with 2×2 equal cards both produce the visual fingerprint "heading top-left + card grid below." These appear on non-adjacent slides (5 and 11), so the 4-slide entropy window rule doesn't flag them. But visually they feel redundant when viewed as a PDF.
- **Evidence**: Slides 5 and 11 PNGs — both show a large heading at top, then a grid of cards below. Slide 5 has 1 featured + 2 stacked; slide 11 has 2×2 equal. Similar visual weight.
- **Root cause**: The skill's visual structure dedup check focuses on CONSECUTIVE slides (entropy window = 4) but doesn't check the deck-level frequency of the "heading + card grid" fingerprint across ALL non-adjacent slides.
- **Proposed skill fix**: Add to the Layout Budget Rule in Step 4.5: "Count ALL slides in the deck (not just consecutive) that will render as 'heading + grid of ≥3 cards'. If count > 30% of content slides, replace excess slides with non-grid archetypes."

### Issue 4: Duplicate data in bento-grid small cards
- **Severity**: major (pre-fix) → resolved
- **Category**: content, layout
- **Frequency**: 1 slide (slide 9, now fixed)
- **Description**: The bottom-left small bento card originally showed "85 монтажников" — the exact same number already present in the featured card's 2×2 sub-grid. Fixed during QA by changing to "24 менеджера продаж."
- **Evidence**: Original slide 9 PNG showed "85" in both left small card AND inside the featured card grid.
- **Root cause**: When building bento-grid slides from team data, the generator pulls numbers from the outline (32 R&D, 85 монтаж, 24 продажи, 39 управление) and assigns them to cells without checking for cross-cell duplication. The featured cell's 2×2 sub-grid already contains all four team numbers, making the small side cards redundant if they also use those same numbers.
- **Proposed skill fix**: Add to Step 5 bento-grid generation rules: "When a featured cell contains a sub-grid of 3+ numbers, the small side cards MUST use different data points — either derived metrics (growth %, ratios) or categorically distinct information. Never repeat a number from the featured cell in a side card."

---

## Slide-Specific Issues (one-off problems)

### Slide 1: Cover title wraps to 4 lines
- **Description**: "Энергия из возобновляемых источников окупается за 3 года" wraps across 4 lines at 3.4rem. Could be reduced to 3 lines with a slight font adjustment or manual line break after "источников". Visually it reads well but feels slightly cramped.
- **Severity**: minor — readability is fine, this is a cosmetic note.

### Slide 3: Large decorative circles look slightly washed out
- **Description**: The concentric circles on slide 3 (teal bg-accent) use `rgba(255,255,255,0.16)` and `rgba(255,255,255,0.10)` opacity. At export resolution, the inner circle (0.10) is barely visible.
- **Severity**: minor — the outer circle (0.16) is clearly visible.

### Slide 4: Arc decoration partially clipped
- **Description**: The arc decoration on slide 4 uses `bottom:-60px;left:-60px` which means about 25% of the arc extends beyond the slide boundary. The visible portion (top-right arc curve) is the intended effect, but it could have higher border-width (currently 6px, could be 8px) for better visibility on the warm cream background.
- **Severity**: minor — decoration is visible and works.

### Slide 9: Layout feels slightly bottom-heavy (fixed)
- **Description**: After fix, the bottom-left card "24 менеджера продаж" and top-left "32 R&D инженера" plus the right featured "180" with sub-grid create good variety. However the featured card still places icon+number in a horizontal row (see systemic Issue 1).
- **Severity**: minor — readable and credible.

---

## What Worked Well

1. **All 27+ rules correctly applied**: bg-accent hex fallback on all teal slides ✓, section dividers clearly differentiated (centered vs left-aligned) ✓, 3 stat-hero variants all structurally different (centered/asymmetric/text-hero) ✓
2. **Eyebrow counter enforced**: Exactly 3 eyebrows on 10 content slides (30% limit) with correct tracking comments in the code ✓
3. **Ghost number "07" on slide 7**: Clearly visible at `rgba(255,255,255,0.18)`, well above the 0.16 minimum threshold for teal bg-accent ✓
4. **Section divider background variety**: Slide 3 = clean teal, Slide 7 = darkened teal with `rgba(0,0,0,0.18)` overlay — clearly different ✓
5. **Card-mosaic hierarchy on slide 5**: Wildberries featured card promotes "2,4 МВт" at 3.5rem, spanning full height — excellent promoted card execution ✓
6. **Cost-of-inaction slide 10**: Text-hero variant with amber warning chips + teal accent headline — highly effective investor-focused urgency messaging ✓
7. **Warm amber accent on slide 10 and 11**: `--color-accent-warm: #D97706` used for warning indicators and target revenue — breaks chromatic monotony without being jarring ✓
8. **Source citation**: "Источник: IRENA, 2025" on slide 2 footer band — professional and credible ✓
9. **bento-grid featured metric at 4rem**: "180" in the featured bento cell exceeds the 3.5rem minimum ✓
10. **Section divider lower anchor on slide 7**: "Раздел 2 из 2 · 2 слайда" pill in bottom-left — grounds the lower third ✓
11. **Adjacent fingerprint and gravity alternation**: Cover (center) → stat-centered (center) → section (center) → stat-asymmetric (left) → mosaic (left) → split (center-left) → section (left) → two-col (center) → bento (left) → text-hero (center) → timeline (left) → CTA (center) — good rhythm ✓
12. **bg-alt arc uses dark color**: On slide 9 (bg-alt), the bento uses dark-bordered ghost cards `rgba(var(--text-rgb),0.10)` correctly ✓

---

## Design Summary

- **Palette type**: light
- **Palette mood**: "warm cream with authoritative teal — clean, trustworthy, finance-grade"
- **Font character**: geometric-sans (Outfit headlines + DM Sans body)
- **Decoration style**: geometric (dot grids, arcs, concentric circles)
- **Strongest axis**: Composition variety (9.0 avg) and Color conviction (8.4 avg)
- **Weakest axis**: Shape diversity on comparison/timeline slides (7.2 avg) — row-based layouts limit non-rectangular shapes

---

## A/B Alternatives for Weakest Slides

### Slide 8 (7.4 avg) — Panel Comparison

**Variant A (current)**: Two-column table with row-by-row comparison, company headers in accent/muted colors.

**Variant B (better)**: Asymmetric split. Left 55%: SolarTech data as a vertical stat column (headline metric: "–18% дешевле" in 3.5rem accent, supporting rows below). Right 45%: Jinko Solar grayed out as "reference" with a diagonal "18–12 НЕД" delivery time callout in amber. This visually promotes SolarTech as the hero and Jinko as the benchmark — a deliberate hierarchy instead of symmetric comparison.

### Slide 9 (7.2 avg) — Team Bento

**Variant A (current)**: 1fr × 1.25fr bento, featured "180" on right. Top-left "32 R&D", bottom-left "24 продаж" (after fix).

**Variant B (better)**: Asymmetric-split archetype. Left 40%: large typographic "180" at 6rem (stat-hero style), no card wrapper. Right 60%: four team function rows with progress-bar-style fill (85/180 = 47% монтаж, etc.). This creates typographic drama that the current bento cannot achieve.
