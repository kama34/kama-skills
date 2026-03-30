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

### Design Rules Checks

Read `references/design-rules.md` before running these checks. Apply AFTER basic checks and BEFORE Figma comparison — fix foundational problems first.

**Text density (per slide):**
- Count words (excluding HTML tags and CSS). If > 75 → **FAIL**. Auto-fix: shorten text, move secondary details to speaker notes. Keep core message.
- Count bullet items (`<li>` or `-` items). If > 6 → **FAIL**. Auto-fix: merge related bullets or move least critical to speaker notes.
- Check bullet nesting depth. If > 2 levels → **FAIL**. Auto-fix: flatten to 2 levels max.

**Typography:**
- Scan for multi-line body text (`<p>`, `<li>` with > 60 chars) with `text-align: center` → **FAIL**. Auto-fix: set `text-align: left; max-width: 65ch; margin: 0 auto`.
- Estimate bold percentage: count characters inside `<strong>`, `<b>`, `font-weight: 700/800/900` vs total text. If > 20% → **WARNING**. Log: "Overemphasis — bold exceeds 20% on slide N".
- Count distinct `font-size` values in one slide's `<style>` + inline styles. If > 3 → **WARNING**. Log: "Too many font sizes on slide N".

**Spacing & overlap:**
- For each slide, check whether any content element's bottom edge + its margin enters the footer zone (bottom 44-56px of slide). If yes → **CRITICAL**. Auto-fix: shorten text or reduce top padding to push content up.
- For footer specifically: if footer uses fixed positioning (`position: absolute; left: Xpx`) or fixed `margin-left` values, and total text width of all footer spans > 900px (slide width minus margins) → **FAIL**. Auto-fix: convert footer to `display: flex; gap: 24px; align-items: center` with `white-space: nowrap; overflow: hidden; text-overflow: ellipsis` on each span.
- Check margins: if any content element is < 5% from any slide edge (48px on 960px width) → **WARNING**. Log: "Content too close to edge on slide N".

**Hierarchy:**
- Calculate heading-to-body font size ratio on each slide. If < 2:1 → **WARNING**. Log: "Weak hierarchy — heading/body ratio X:1 on slide N".
- Compare largest and second-largest elements by font-size. If ratio < 1.5:1 → **WARNING**. Log: "No clear focal point on slide N".

**Contrast:**
- For each text-on-background pair, calculate contrast ratio. Body text (< 24px) with ratio < 4.5:1 → **FAIL**. Large text (≥ 24px) with ratio < 3:1 → **FAIL**. Auto-fix: adjust text color to meet minimum. Log computed ratios.

**Severity handling:**
- **CRITICAL** (overlap into footer zone): auto-fix immediately, re-check after fix
- **FAIL** (density, alignment, contrast, footer overflow): auto-fix immediately, re-check after fix
- **WARNING** (hierarchy, bold, font-size count, edge proximity): log to iteration report only, do not block

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
