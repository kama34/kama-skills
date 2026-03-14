# Polish Procedure

Iterative design improvement cycle. Subcommand: `--polish=N [dir]` (default N=3, max N=5).

**Prerequisite:** Project directory with `slides/` (PNG backgrounds), `slides.md` (Slidev source), `prompts.json`, and `meta.json` must exist.

## Dual-Layer Architecture

SlideCraft slides have two layers:
- **Image layer** — AI-generated PNG backgrounds (stored in `slides/`)
- **Text layer** — Slidev HTML/CSS overlays (in `slides.md` with `layout:none` + absolute positioning)

Polish targets both layers independently and in combination.

## Dual-Layer Remediation Table

| Axis | Layer | Remediation action |
|------|-------|--------------------|
| Visual impact | Image | Regenerate PNG with A/B variant prompts |
| Layout precision | Both | Adjust zone coordinates → regenerate PNG → update CSS |
| Typography quality | Text | Adjust font sizes, weights, colors, line-height in CSS |
| Color conviction | Image | Regenerate PNG with A/B variant palettes |
| Content clarity | Text | Restructure text content, simplify bullets |
| Layer harmony | Both | Analyze which layer causes dissonance → targeted fix |

## Procedure

### POL-1: Validate

1. Resolve project directory (use `[dir]` or auto-detect via `prompts.json` lookup).
2. Verify `prompts.json`, `meta.json`, `slides/` (PNG backgrounds), and `slides.md` (Slidev text layer) exist.
3. Load metadata: provider, model, style anchor index, mode.
4. Initialize: `changed_slides = []`, `changed_text_layers = []`, `iteration = 0`.

### POL-2: Initial State

1. Run Scoring Subroutine (`scoring-subroutine.md`) → `score-report.md`.
2. Run Content Review Subroutine (`content-review-subroutine.md`).
3. Print baseline: overall score, per-slide summary across all 6 axes, content issues.

### POL-3: Check Exit

If `overall_avg >= 9` OR `iteration == N`:
- Goto POL-8 (Finalize).

Early exit at overall score >= 9 — no further polish cycles are needed.

### POL-4: Redesign Weak Slides

For each slide with any axis < 6:
- Identify which layer is responsible (see remediation table above).
- Run A/B Testing Subroutine (`ab-testing.md`) — layer-aware.
- Best variant replaces the original in `slides/` (image layer) or in the slide's `<style>` block (text layer).
- Add slide index to `changed_slides` (image changed) and/or `changed_text_layers` (CSS changed).

For each slide with avg 6-7 (above threshold but weak):
- Identify the single lowest-scoring axis.
- Apply targeted fix per the remediation table — image-only, text-only, or both.
- If image layer: modify prompt in `prompts.json` and regenerate PNG.
- If text layer: update font sizes, weights, positioning, or content in `slides.md`.
- If both: coordinate zone coordinates between PNG prompt and CSS absolute positions.
- Add slide index to appropriate changed list.

**NEVER touch slides with avg >= 9.**

### POL-5: Fix Content Issues

Apply CRITICAL and MAJOR content fixes from the content review:
- For text/content issues: modify the affected slide's text in `slides.md` and re-export.
- For layout issues affecting both layers: update zone coordinates in PNG prompt AND CSS.
- Add regenerated slide indices to `changed_slides` or `changed_text_layers`.
- Skip MINOR issues.

### POL-6: QA Pass

For each slide in `changed_slides` or `changed_text_layers`:
- Read the PNG and the corresponding slide section in `slides.md`.
- Verify text readability against AI background, stylistic consistency, zone alignment.
- Check layer harmony — does text color work with the actual background palette?
- If any obvious issues (garbled text, wrong colors, broken layout, zone misalignment): apply targeted fix per remediation table and retry once.

### POL-7: Re-Score

1. Run Scoring Subroutine on all slides (not just changed ones — scores are relative).
2. Update `score-report.md`.
3. Print: current score, delta from previous iteration, slides improved/degraded.
4. Reset `changed_slides = []`, `changed_text_layers = []`.
5. Increment `iteration`.
6. Goto POL-3.

### POL-8: Finalize

1. Export composite screenshots (Playwright) for final review.
2. Write Design Memory entry (`design-memory.md` write protocol).
3. Clean up: remove `score-report.md` (scores are now in design memory).

### POL-9: Preset Auto-Capture

If final overall avg >= 9:
- Ask user: "This design scored X.X/10. Would you like to save it as a preset? (name)"
- If yes: extract style suffix from `prompts.json`, mood/palette from prompts, CSS config from `slides.md`, write `.preset.md` to the location the user chooses (global/local).
- Preset captures BOTH visual layer (style suffix, palette, zone strategy) and text layer (fonts, positioning, contrast mode).

### POL-10: Report

Print summary:
```
Polish complete!

  Iterations:          N
  Score progression:   6.2 → 7.1 → 8.3
  Slides redesigned:   N (A/B tested: N)
    → Image layer:     N regenerated
    → Text layer:      N CSS updates
  Content fixes:       N
  Final score:         X.X / 10
  Composite export:    <dir>/export/

  Preset saved:        ~/.claude/slidecraft-presets/<name>.preset.md (or "not saved")
```
