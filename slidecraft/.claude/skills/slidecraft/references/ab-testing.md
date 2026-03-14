# A/B Testing Subroutine

Called by `--polish` (POL-4) for each weak slide. Not a standalone command. Generates 2 design variants of a slide, scores them, picks the best.

SlideCraft A/B testing is **layer-aware** — variants target the image layer, text layer, or both depending on which axes are weak.

**Input:** slide index, score-report.md per-axis breakdown, prompts.json, meta.json, slides.md

## Procedure

### AB-1: Analyze Weakness

Read the slide's per-axis scores from `score-report.md`. Identify:
- Which axes scored lowest (< 6)
- What specific elements are weak (from the score report's reasoning)
- Which layer is responsible (per dual-layer remediation table in `polish-procedure.md`)

Classify the A/B test type:
- **Image A/B** — weakness is in Visual impact or Color conviction (image layer only)
- **Text A/B** — weakness is in Typography quality or Content clarity (text layer only)
- **Full A/B** — weakness is in Layout precision or Layer harmony (both layers)

### AB-2: Generate 2 Variants

#### Image A/B — Two variant PNG prompts (different visual directions)

**Variant A — Aggressive visual fix:**
Radically redesign the weakest image-layer axis:
- If Visual Impact lowest → completely change background treatment, add bold decorative geometry, shift focal point
- If Color Conviction lowest → switch to a bolder palette, increase accent saturation, change contrast ratio

**Variant B — Balanced visual fix:**
Moderate improvement: soften the aggressive change, keep the same palette family but optimize tonal range and composition.

Both image variants MUST:
- Keep zones text-free (no rendered text in the PNG)
- Maintain the same zone layout dimensions so text overlay CSS does not need changes
- Maintain consistency with the style suffix

#### Text A/B — Two CSS/positioning variants for the same text content

**Variant A — Aggressive text fix:**
- If Typography Quality lowest → dramatically change font sizes, weights, line-height; try bold/display weight for headings
- If Content Clarity lowest → restructure to fewer bullets, larger key stat, increase whitespace

**Variant B — Balanced text fix:**
Moderate changes: smaller sizing adjustments, incremental clarity improvements, preserve layout proportions.

Both text variants MUST:
- Preserve the original text content (headings, bullets, metrics) — only change presentation
- Keep absolute positioning within established zone boundaries
- Maintain `layout:none` and `position:absolute` structure

#### Full A/B — Coordinate both layers

Generate two complete direction pairs:
- **Direction A**: New PNG prompt + corresponding CSS zone adjustments
- **Direction B**: Alternative PNG prompt + alternative CSS zone adjustments

Zone coordinates in the PNG prompt MUST match the CSS `top`/`left`/`width`/`height` percentages in both directions.

**All variants MUST:**
- Preserve the original text content (headings, bullets, metrics)
- Keep slides text-free in the image layer (zones only, no rendered text in PNG)
- Maintain consistency with the style suffix

### AB-3: Generate and Save

For each variant (A and B):
1. **Image layer**: modify the slide's prompt in `prompts.json` per variant strategy; generate PNG using the provider API (with style anchor if in reference mode); save to `<dir>/ab-variants/slide-<N>/variant-a-bg.png` and `variant-b-bg.png`
2. **Text layer**: write variant CSS to `<dir>/ab-variants/slide-<N>/variant-a-overlay.md` and `variant-b-overlay.md` (the slide's full Slidev block with updated styles)
3. Also copy the originals: `original-bg.png` and `original-overlay.md`

### AB-4: Score Variants

Composite both layers (use Playwright screenshot or image compositing) before scoring.

Run single-slide 6-axis scoring on the composite for:
- Original (bg + overlay)
- Variant A composite
- Variant B composite

Scoring axes: Visual impact, Layout precision, Typography quality, Color conviction, Content clarity, Layer harmony.

### AB-5: Select Winner

Compare average scores across all 6 axes:
- If Variant A is highest → use Variant A
- If Variant B is highest → use Variant B
- If Original is highest → keep original (both variants scored lower — log this)

In case of a tie on average, prefer the variant with the higher Layer harmony score.

### AB-6: Apply Winner

1. **Image layer**: copy winning PNG to `<dir>/slides/slide-<NN>.png` (overwrite); update `prompts.json` with winning variant's prompt (if original won, revert prompt)
2. **Text layer**: apply winning overlay's CSS/content to the corresponding slide block in `slides.md`

### AB-7: Save All Variants

Persist `<dir>/ab-variants/slide-<N>/`:
```
original-bg.png
original-overlay.md
original-score.txt         # 6-axis scores

variant-a-bg.png
variant-a-overlay.md
variant-a-score.txt        # ← winner marker if A won

variant-b-bg.png
variant-b-overlay.md
variant-b-score.txt
```

Score text file format:
```
Visual Impact:      7
Layout Precision:   6
Typography Quality: 8
Color Conviction:   7
Content Clarity:    9
Layer Harmony:      6
Average:            7.2
```
