# Compare Procedure

Side-by-side comparison of two presentations with scoring. Subcommand: `--compare <dir1> <dir2>`.

## Input

- `dir1`, `dir2` — two project directories, each containing `slides.md`

## Procedure

### CMP-1: Validate

1. Verify both `<dir1>/slides.md` and `<dir2>/slides.md` exist
2. `npm install` in each dir if no `node_modules/`
3. `npx playwright install chromium` (once)

### CMP-2: Export

1. Run Export Subroutine for `<dir1>` `--output slides-qa` (skip if `slides-qa/` already exists and is up-to-date)
2. Run Export Subroutine for `<dir2>` `--output slides-qa`

### CMP-3: Score

1. Run Scoring Subroutine (`references/scoring-subroutine.md`) for `<dir1>` → `<dir1>/score-report.md`
2. Run Scoring Subroutine for `<dir2>` → `<dir2>/score-report.md`

### CMP-4: Generate Comparison Report

If slide counts differ, compare slides up to the shorter count, then note the remainder. Overall scores are based on ALL slides in each respective deck.

Print:

```
Comparison: <dir1> vs <dir2>

  Overall: <dir1> X.X/10 (N slides) vs <dir2> Y.Y/10 (M slides) → Winner: <dirN>

  Per-Slide Comparison (slides 1-min(N,M)):
  | Slide | <dir1> | <dir2> | Delta | Winner |
  |-------|--------|--------|-------|--------|
  | 1     | 7.8    | 8.5    | +0.7  | dir2   |
  | 2     | 9.1    | 6.3    | -2.8  | dir1   |
  ...

  [<dir2> has 3 additional slides not compared]   ← only if counts differ

  Design Differences:
    Fonts: <dir1> uses X + Y, <dir2> uses A + B
    Palette: <dir1> [mood], <dir2> [mood]
    Layouts: <dir1> N unique structures, <dir2> M
    Decoration: <dir1> [motifs], <dir2> [motifs]
```

Read both `slides.md` files and `styles/index.css` to extract design differences (fonts, palette, layout variety, decoration).

### CMP-5: Cleanup

```bash
rm -rf <dir1>/slides-qa
rm -rf <dir2>/slides-qa
```
