# A/B Testing Subroutine

Called by `--polish` (POL-4) for each weak slide. Not a standalone subcommand. Generates 2 design variants for a weak slide, scores them, picks the best.

## Procedure

### AB-1: Identify Weak Slide

Input:
- Slide number from score report (avg < 7)
- Current `score-report.md` with per-axis breakdown
- Current `slides.md`

### AB-2: Analyze Weakness

Read the slide's per-axis scores. Determine:
- Which axes scored lowest?
- What specific elements are weak? (layout structure, typography scale, color usage, decoration presence, content structure)

### AB-3: Generate 2 Variants

Create two alternative designs for the slide:

**Variant A — Aggressive fix**: Radically redesign the weakest axis.
- If layout scored lowest → completely change the layout structure (e.g., 2-column grid → centered hero)
- If typography scored lowest → dramatically change type scales and weight pairing
- If decoration scored lowest → add strong decorative elements

**Variant B — Balanced fix**: Moderate improvement across all low axes.
- Improve layout + typography + decoration together
- Less dramatic changes per axis, but broader coverage

**Both variants MUST**:
- Preserve the same CONTENT (text, data, messaging) — only visual treatment changes
- Maintain consistency with the overall presentation aesthetic (same CSS variables, fonts, motifs)
- Follow all Slide Authoring Rules from SKILL.md

### AB-4: Write and Export Variants

For each variant (A, then B):

1. Rename `<dir>/slides.md` to `<dir>/slides-backup.md`
2. Write the variant's slide into `<dir>/slides.md` (replacing only the target slide, keeping all other slides unchanged)
3. Run Export Subroutine for `<dir>` `--only-slides <N>` `--output slides-qa`
4. Copy the exported PNG to `<dir>/ab-variants/slide-<N>/variant-<x>.png`
5. Restore: rename `<dir>/slides-backup.md` back to `<dir>/slides.md`

Before the first variant, also save the original:
- Copy the current export of slide N to `<dir>/ab-variants/slide-<N>/original.png`
- Write the original's average score to `<dir>/ab-variants/slide-<N>/original-score.txt`

### AB-5: Score Variants

Run the Scoring Subroutine evaluation (read the PNG, score on 9 axes) for each variant's exported PNG. This is a single-slide scoring — apply the same 9-axis evaluation from `references/scoring-subroutine.md`.

Compare: original avg vs variant A avg vs variant B avg.

### AB-6: Select Winner

- **Highest scoring variant** → apply its slide content to `slides.md` (replace the target slide permanently)
- **If BOTH variants score LOWER than original** → keep original unchanged. Log in the polish report: "Slide N: A/B testing did not improve (original X.X, variant A Y.Y, variant B Z.Z)"

### AB-7: Save All Variants

Ensure this directory structure persists for user comparison:

```
<dir>/ab-variants/
  slide-<N>/
    original.png
    original-score.txt    (e.g., "6.3")
    variant-a.png
    variant-a-score.txt   (e.g., "7.2")
    variant-b.png
    variant-b-score.txt   (e.g., "8.1 ← winner")
```

Write score files with the average score and a "← winner" marker on the winning variant.

### AB-8: Cleanup

- Remove `<dir>/slides-backup.md` if still present (safety check)
- Keep `<dir>/ab-variants/` directory — it persists for user review
