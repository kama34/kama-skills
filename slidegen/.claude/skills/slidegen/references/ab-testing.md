# A/B Testing Subroutine

Called by `--polish` (POL-4) for each weak slide. Not a standalone command. Generates 2 design variants of a slide, scores them, picks the best.

**Input:** slide index, score-report.md per-axis breakdown, prompts.json, meta.json

## Procedure

### AB-1: Analyze Weakness

Read the slide's per-axis scores from `score-report.md`. Identify:
- Which axes scored lowest (< 6)
- What specific elements are weak (from the score report's reasoning)

### AB-2: Generate 2 Variants

**Variant A — Aggressive fix:**
Radically redesign the weakest axis:
- If Visual Impact lowest → completely change background treatment, add bold decorative elements
- If Typography Drama lowest → dramatically change text sizes, add hero numbers, increase contrast
- If Color Conviction lowest → switch to a bolder palette, increase accent usage
- If Content Clarity lowest → simplify layout, reduce text, enlarge key message
- If Decorative Quality lowest → add strong decorative elements (patterns, shapes, overlays)
- If Layout Uniqueness lowest → completely change composition (centered → asymmetric, or vice versa)

**Variant B — Balanced fix:**
Moderate improvement across all low-scoring axes simultaneously. Less dramatic changes but addresses multiple weaknesses.

**Both variants MUST:**
- Preserve the original text content (headings, bullets, metrics)
- Maintain consistency with the style suffix
- Keep the same slide role

### AB-3: Generate and Save

For each variant (A and B):
1. Modify the slide's prompt in `prompts.json` according to the variant strategy
2. Generate the image using the provider API (with style anchor if in reference mode)
3. Save to `<dir>/ab-variants/slide-<N>/variant-a.png` and `variant-b.png`
4. Also copy the original slide to `<dir>/ab-variants/slide-<N>/original.png`

### AB-4: Score Variants

Run single-slide 6-axis scoring for:
- Original PNG
- Variant A PNG
- Variant B PNG

### AB-5: Select Winner

Compare average scores:
- If Variant A is highest → use Variant A
- If Variant B is highest → use Variant B
- If Original is highest → keep original (both variants scored lower — log this)

### AB-6: Apply Winner

1. Copy winning PNG to `<dir>/slides/slide-<NN>.png` (overwrite)
2. Update `prompts.json` with the winning variant's prompt (if original lost, revert prompt)

### AB-7: Save All Variants

Persist `<dir>/ab-variants/slide-<N>/`:
```
original.png
original-score.txt         # 6-axis scores
variant-a.png
variant-a-score.txt        # ← winner (if A won)
variant-b.png
variant-b-score.txt
```

Score text file format:
```
Visual Impact: 7
Layout Uniqueness: 6
Typography Drama: 8
Color Conviction: 7
Content Clarity: 9
Decorative Quality: 6
Average: 7.2
```
