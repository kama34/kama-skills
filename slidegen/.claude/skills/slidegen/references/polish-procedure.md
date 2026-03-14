# Polish Procedure

Iterative design improvement cycle. Subcommand: `--polish=N [dir]` (default N=3, max N=5).

**Prerequisite:** Project directory with `slides/`, `prompts.json`, and `meta.json` must exist.

## Procedure

### POL-1: Validate

1. Resolve project directory (use `[dir]` or auto-detect via `prompts.json` lookup).
2. Verify `prompts.json`, `meta.json`, and `slides/` exist.
3. Load metadata: provider, model, style anchor index, mode.
4. Initialize: `changed_slides = []`, `iteration = 0`.

### POL-2: Initial State

1. Run Scoring Subroutine (`scoring-subroutine.md`) → `score-report.md`.
2. Run Content Review Subroutine (`content-review-subroutine.md`).
3. Print baseline: overall score, per-slide summary, content issues.

### POL-3: Check Exit

If `overall_avg >= 9` OR `iteration == N`:
- Goto POL-8 (Finalize).

### POL-4: Redesign Weak Slides

For each slide with any axis < 6:
- Run A/B Testing Subroutine (`ab-testing.md`).
- Best variant replaces the original slide in `slides/`.
- Add slide index to `changed_slides`.

For each slide with avg 6-7 (above threshold but weak):
- Targeted fix: identify the single lowest-scoring axis.
- Modify the prompt to specifically address that axis.
- Regenerate the slide (with style anchor if in reference mode).
- Add slide index to `changed_slides`.

**NEVER touch slides with avg >= 9.**

### POL-5: Fix Content Issues

Apply CRITICAL and MAJOR content fixes from the content review:
- For text/content issues: modify the affected slide's prompt and regenerate.
- Add regenerated slide indices to `changed_slides`.
- Skip MINOR issues.

### POL-6: QA Pass

For each slide in `changed_slides`:
- Read the regenerated PNG.
- Verify text readability, stylistic consistency, composition.
- If any obvious issues (garbled text, wrong colors, broken layout): regenerate once more with adjusted prompt.

### POL-7: Re-Score

1. Run Scoring Subroutine on all slides (not just changed ones — scores are relative).
2. Update `score-report.md`.
3. Print: current score, delta from previous iteration, slides improved/degraded.
4. Reset `changed_slides = []`.
5. Increment `iteration`.
6. Goto POL-3.

### POL-8: Finalize

1. Reassemble PDF from all PNGs.
2. Write Design Memory entry (`design-memory.md` write protocol).
3. Clean up: remove `score-report.md` (scores are now in design memory).

### POL-9: Preset Auto-Capture

If final overall avg >= 9:
- Ask user: "This design scored X.X/10. Would you like to save it as a preset? (name)"
- If yes: extract style suffix from `prompts.json`, mood/palette from the prompts, write `.preset.md` to the location the user chooses (global/local).

### POL-10: Report

Print summary:
```
Polish complete!

  Iterations:        N
  Score progression:  6.2 → 7.1 → 8.3
  Slides redesigned: N (A/B tested: N)
  Content fixes:     N
  Final score:       X.X / 10
  PDF:               <dir>/slides.pdf

  Preset saved:      ~/.claude/slidegen-presets/<name>.preset.md (or "not saved")
```
