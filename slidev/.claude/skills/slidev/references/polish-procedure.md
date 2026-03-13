# Polish Procedure

The iterative design improvement cycle for a single presentation. Subcommand: `--polish=N [dir]`.

## Input

- `N` — iteration count (default: 3, max: 5). If N > 5, cap at 5 and notify.
- `dir` — project directory. Defaults to auto-detection: look for `slides.md` in the current working directory; if not found, scan one level deep for the most recently modified directory containing `slides.md`.

## Prerequisite

The presentation must already exist (generated via `/slidev`). If resolved `dir` doesn't contain `slides.md`, print error and stop:

```
Error: No slides.md found in <dir>. Generate a presentation first with /slidev.
```

## Procedure

### POL-1: Validate

1. Verify `<dir>/slides.md` exists
2. Detect current theme from `slides.md` headmatter (`theme:` field, default: `default`). Pass this to Visual QA and A/B testing steps — theme-conditional rules (Rules 9, 10, 24, 29, 32) only apply when theme == "default".
3. `npm install` if no `node_modules/` in `<dir>`
4. `npx playwright install chromium`
5. Initialize `changed_slides = []` (tracking list for progressive export)
6. Set `iteration = 0`

### POL-2: Initial State

1. Run Export Subroutine for `<dir>` `--output slides-qa` (full export)
2. Run Scoring Subroutine (`references/scoring-subroutine.md`) for `<dir>` → produces `<dir>/score-report.md`
3. Run Content Review Subroutine (`references/content-review-subroutine.md`) for `<dir>` → produces content issues
4. Print: `"Polish iteration 0 (baseline): overall score X.X/10"`

### POL-3: Check Exit Conditions

- If overall score >= 9 (approximately — use judgment) → goto **POL-8** (early exit with message: "Score already excellent, skipping further iterations")
- If `iteration == N` → goto **POL-8** (max iterations reached)

### POL-4: Redesign Weak Slides

For each slide with avg **< 7** (from score report):
1. Run A/B Testing Subroutine (`references/ab-testing.md`) for this slide
2. Best variant replaces the slide in `slides.md`
3. Add slide number to `changed_slides`

For slides scoring **7-8** (improvable but not weak):
1. Apply targeted fix on the **lowest-scoring axis only** (e.g., if decoration scored 5 but other axes scored 7-8, add decorative elements)
2. Add slide number to `changed_slides`

**NEVER** touch slides scoring **>= 9**.

### POL-5: Fix Content Issues

1. Apply **critical** and **major** content review fixes from POL-2
2. Add affected slide numbers to `changed_slides`
3. Skip **minor** issues

### POL-6: Visual QA Pass (Bug-Fix Only)

Run the existing Visual QA Loop for `<dir>` (from SKILL.md). Pass the detected theme from POL-1. This catches CSS/rendering issues introduced by redesign — alignment breaks, text overflow, color mismatches.

### POL-7: Re-Score

1. Run Export Subroutine for `<dir>` `--output slides-qa` `--only-slides <changed_slides>` (progressive export — only re-export changed slides)
2. Run Scoring Subroutine for `<dir>` → updates `score-report.md`
3. Print: `"Polish iteration M: overall score X.X/10 (delta +Y.Y from baseline)"`
4. Reset `changed_slides = []`
5. Increment `iteration` → goto **POL-3**

### POL-8: Finalize

1. Run Export Subroutine for `<dir>` `--output slides-final` (full export: PNGs + PDF via `npx slidev export --output slides-final/slides.pdf`)
2. Write Design Memory entry — follow Write Protocol in `references/design-memory.md`
3. Cleanup: `rm -rf <dir>/slides-qa <dir>/score-report.md`

### POL-9: Preset Auto-Capture

If final overall score >= 9 (approximately):

1. Ask user: `"Score X.X/10! Save this aesthetic as a preset? Enter name (or press Enter to skip):"`
2. If user provides a name:
   a. Extract from project:
      - `fonts` from `slides.md` headmatter
      - `colorSchema` from `slides.md` headmatter
      - `transition` from `slides.md` headmatter
      - CSS variables block from `styles/index.css` (`:root { ... }`)
      - Card style definitions (`.card-solid`, `.card-ghost`, `.card-accent`, `.card-glass`)
      - Decorative motif classes (`.decor-*`)
      - Blockquote reset rule
      - `accentColor` derived from `--color-accent` CSS variable value
   b. Write to `~/.claude/slidev-presets/<name>.preset.md` following the format in `references/preset-format.md`
   c. Read `~/.claude/slidev-presets.json` (create `{}` if doesn't exist)
   d. Add entry: `"<name>": "~/.claude/slidev-presets/<name>.preset.md"`
   e. Write updated JSON
   f. Print: `"Preset '<name>' saved to ~/.claude/slidev-presets/<name>.preset.md"`
3. If user skips: continue to POL-10

### POL-10: Report

Print:

```
Polish complete: <dir>

  Iterations: M (of max N)
  Score progression: X.X → Y.Y → Z.Z
  Slides redesigned: [3, 7, 11]
  Content fixes: N issues resolved
  A/B variants: <dir>/ab-variants/ (N alternatives saved for comparison)
  Preset saved: <name>.preset.md (or "not saved")

  Final export:
    <dir>/slides-final/*.png
    <dir>/slides-final/slides.pdf
```
