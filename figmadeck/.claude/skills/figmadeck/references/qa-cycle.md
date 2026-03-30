# QA Cycle — Iterative Figma Comparison

Runs after slides.md is generated (Step 5 of generation-pipeline.md). Loops until Fidelity Score >= 9/10.

## Overview

The cycle runs three phases per iteration:

```
repeat:
  Phase A: CSS + Figma structural/style comparison → fix issues
  Phase B: Visual export + Figma screenshot comparison → fix issues
  Phase C: Score → if >= 9/10, DONE; else next iteration
  Safety stop: 5 iterations with score delta < 0.3 → stop with report
```

Every slide is compared on every iteration. Fixes are applied to slides.md before moving to the next phase.

## Comparison Scope

EVERY slide is compared — including those with adapted archetypes. Each slide is compared against the closest Figma original from the SAME preset. Read `nodeId` from `source.json` in the figmadeck-`<name>`-figma/ directory.

Adapted archetypes (content type had no exact match) are compared against the archetype they were adapted from, with a relaxed content-fit criterion: the slide must visually belong to the same presentation family.

## Phase A: CSS + Figma Structural/Style Comparison

### Basic Checks

Run these on every slide before calling Figma APIs:

- **Font-size floor**: body >= 1.25rem, heading >= 2.2rem, label >= 0.65rem
- **layout: none enforcement**: every slide that uses raw HTML absolute positioning must declare `layout: none`
- **Hardcoded hex scan**: find any `#rrggbb` / `rgb(...)` literals → replace with `var(--*)` CSS variables
- **Content overflow**: text fits within slot boundaries, no element overlap between content blocks

Fix any violations directly in slides.md before proceeding to Figma structural comparison.

### Figma Structural Comparison

For each slide, call using its archetype's `nodeId`:

```
mcp__figma__get_metadata(nodeId, fileKey)
```

Returns positions and sizes of all elements. Compare:

- **Element positions**: tolerance +-5% of viewport width/height
- **Element proportions** (width/height ratios): tolerance +-10%
- **Nesting hierarchy**: exact match — wrapper → section → element structure must be preserved

### Figma Style Comparison

For each slide, call:

```
mcp__figma__use_figma  (JS extraction: fonts, colors, spacing, radius)
```

Compare extracted values against slides.md CSS:

| Property | Tolerance |
|----------|-----------|
| font-size | +-0.15rem |
| font-weight | exact |
| color | deltaE < 5 (CIEDE2000) |
| spacing (gap) | +-0.25rem |
| padding | +-0.5rem |
| border-radius | +-2px |
| position | +-5% viewport |

Fix all issues found → modify slides.md before Phase B.

## Phase B: Visual Export + Figma Screenshot Comparison

### Export

```bash
npm install && npx playwright install chromium   # only if deps missing
npx slidev export --format png --output slides-qa
```

### Per-slide comparison

For EACH slide:

1. Call `mcp__figma__get_screenshot(nodeId, fileKey)` — fresh screenshot, not cached
2. Compare the exported PNG side by side against the Figma screenshot
3. Evaluate:
   - Overall visual impression and color mood correspondence
   - Typography proportions (size hierarchy visible, weights correct)
   - Whitespace balance (padding, breathing room between elements)
   - Content not cut off at edges or behind decorative elements
   - Footer / slide number visible if present in Figma archetype
4. For adapted archetypes: verify the slide looks like it belongs in the same presentation (consistent palette, type scale, corner radii)

Fix all visual issues → modify slides.md.

### Cleanup

```bash
rm -rf slides-qa
```

Run after each iteration (before the next Phase A) to avoid stale PNGs.

## Phase C: Score

**Fidelity Score = Visual (40%) + Structural (30%) + Style (30%)**

Each sub-score is 0–10. Weighted sum gives the final score out of 10.

- Score **>= 9/10** → **DONE**. Clean up temp files, print Final Summary.
- Score **< 9/10** → apply fixes, start next iteration from Phase A.
- **Safety stop**: after 5 consecutive iterations where score delta < 0.3 → stop and print a report of unresolved issues. Do not loop further.

## Figma API Usage

- Make **live calls on EACH iteration** — do not cache get_screenshot, get_metadata, or use_figma results across iterations.
- If Figma API is unavailable: retry 2x with a 10-second pause between attempts.
- After 2 failed retries: fall back to cached `blueprint.json` + `reference.png` from the figmadeck-`<name>`-figma/ directory. Note the fallback in the iteration report.

## Iteration Report

Print after each Phase C:

```
━━━ QA Iteration <N> ━━━
Fidelity: X/10 (Visual: X | Structural: X | Style: X)
Fixed: <list of fixes applied this iteration>
Remaining: <list of unresolved issues>
```

## Final Summary (on DONE)

Print when score reaches >= 9/10:

```
━━━ QA Complete ━━━
Final Fidelity: X/10
Iterations: N
Total fixes applied: X
Presentation: <project path>
```
