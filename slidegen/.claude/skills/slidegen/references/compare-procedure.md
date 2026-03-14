# Compare Procedure

Side-by-side comparison of two presentations with scoring. Subcommand: `--compare <dir1> <dir2>`.

## Procedure

### CMP-1: Validate

1. Verify both directories exist and contain `slides/`, `prompts.json`, and `meta.json`.
2. Load metadata from both.

### CMP-2: Score

Run Scoring Subroutine (`scoring-subroutine.md`) for each directory → respective `score-report.md` files.

### CMP-3: Generate Comparison Report

If slide counts differ, compare up to the shorter count. Note the remainder.

Print comparison report:

```
# Comparison Report: <dir1> vs <dir2>

## Overall Scores
  <dir1>: X.X / 10
  <dir2>: Y.Y / 10
  Winner: <dir1|dir2> (+Z.Z)

## Per-Slide Comparison

| Slide | <dir1> | <dir2> | Delta | Winner |
|-------|--------|--------|-------|--------|
| 1     | 7.8    | 8.2    | +0.4  | dir2   |
| 2     | 7.0    | 6.5    | -0.5  | dir1   |
| ...   | ...    | ...    | ...   | ...    |

## Extra slides
  <dir1> has N additional slides (N+1 through M)

## Design Differences
  <dir1>: [mood], [palette summary], [provider/model]
  <dir2>: [mood], [palette summary], [provider/model]

  Key differences: [what visually distinguishes the two]
```

Read `prompts.json` from both to extract style suffix and mood for the design differences section.

### CMP-4: Cleanup

Remove `score-report.md` from both directories (scores are in the comparison output).
