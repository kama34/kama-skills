# Compare Procedure

Side-by-side comparison of two SlideCraft presentations with scoring. Subcommand: `--compare <dir1> <dir2>`.

Comparison is performed on **composite exports** — final screenshots with both the AI-generated PNG background and the Slidev text overlay merged — so scores reflect the complete two-layer result.

## Procedure

### CMP-1: Validate

1. Verify both directories exist and contain `slides/` (PNG backgrounds), `slides.md` (text layer), `prompts.json`, and `meta.json`.
2. Load metadata from both.

### CMP-2: Export Composites

For each directory, generate composite screenshots (Playwright) that merge both layers:
- PNG background + Slidev HTML/CSS overlay rendered together
- Save to `<dir>/slides-compare/` as `slide-NN.png`

This ensures scoring reflects true layer harmony, not just individual layers in isolation.

### CMP-3: Score

Run Scoring Subroutine (`scoring-subroutine.md`) on the composite exports for each directory → respective `score-report.md` files.

Scoring axes (all 6 must be reported per slide):
- Visual impact
- Layout precision
- Typography quality
- Color conviction
- Content clarity
- Layer harmony

### CMP-4: Generate Comparison Report

If slide counts differ, compare up to the shorter count. Note the remainder.

Print comparison report:

```
# Comparison Report: <dir1> vs <dir2>

## Overall Scores
  <dir1>: X.X / 10
  <dir2>: Y.Y / 10
  Winner: <dir1|dir2> (+Z.Z)

## Per-Slide, Per-Axis Delta

| Slide | Axis               | Dir1 | Dir2 | Delta |
|-------|--------------------|------|------|-------|
| 1     | Visual impact      | 8    | 7    | +1    |
| 1     | Layout precision   | 7    | 8    | -1    |
| 1     | Typography quality | 9    | 7    | +2    |
| 1     | Color conviction   | 7    | 7    |  0    |
| 1     | Content clarity    | 8    | 9    | -1    |
| 1     | Layer harmony      | 8    | 6    | +2    |
| 1     | **Slide avg**      | 7.8  | 7.3  | +0.5  |
| 2     | Visual impact      | ...  | ...  | ...   |
| ...   | ...                | ...  | ...  | ...   |
| Overall                   | 7.8  | 6.5  | +1.3  |

## Per-Slide Summary

| Slide | <dir1> | <dir2> | Delta | Winner |
|-------|--------|--------|-------|--------|
| 1     | 7.8    | 7.3    | +0.5  | dir1   |
| 2     | 7.0    | 6.5    | -0.5  | dir1   |
| ...   | ...    | ...    | ...   | ...    |

## Extra slides
  <dir1> has N additional slides (N+1 through M)

## Design Differences
  <dir1>: [mood], [palette summary], [provider/model]
    Visual: [style suffix summary]
    Text:   [font pair, positioning approach]

  <dir2>: [mood], [palette summary], [provider/model]
    Visual: [style suffix summary]
    Text:   [font pair, positioning approach]

  Key differences: [what visually distinguishes the two — focus on layer harmony and zone strategy]

## Layer Analysis
  <dir1> layer harmony avg:  X.X
  <dir2> layer harmony avg:  Y.Y
  Note: [which presentation had better image/text coordination and why]
```

Read `prompts.json` and `slides.md` from both to extract style suffix, font config, mood, and zone strategy for the design differences and layer analysis sections.

### CMP-5: Cleanup

1. Remove composite exports: `rm -rf <dir1>/slides-compare <dir2>/slides-compare`
2. Remove `score-report.md` from both directories (scores are in the comparison output).
