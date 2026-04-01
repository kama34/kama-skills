# QA Cycle — Figma-Native

Runs after Step 5 (fill content). Loops until Fidelity Score ≥ 9/10.

## Overview

All checks run INSIDE Figma — no Slidev export, no HTML/CSS comparison, no pixel diff tools.

```
repeat:
  Phase A: Structural check (programmatic via use_figma) → collect issues
  Phase B: Visual comparison (get_screenshot original vs adapted) → style assessment
  Phase C: Design critique (design-rules.md) → per-slide evaluation
  Phase D: Score + fix → if ≥ 9/10, DONE; else apply fixes, next iteration
  Safety stop: 5 iterations with score delta < 0.3
```

Every slide is checked on every iteration. Fixes are applied via `use_figma` before the next iteration.

---

## Phase A: Structural Check (programmatic)

One `use_figma` call per slide (or batch per page).

**MANDATORY:** `await figma.setCurrentPageAsync(generatedPage)` at start of every call.

### Overlap Detection

For each pair of visible nodes on a slide, compute bounding boxes using `absoluteTransform` + `width` / `height`:

```js
const ax = nodeA.absoluteTransform[0][2], ay = nodeA.absoluteTransform[1][2];
const bx = nodeB.absoluteTransform[0][2], by = nodeB.absoluteTransform[1][2];
const overlap =
  ax < bx + nodeB.width && ax + nodeA.width > bx &&
  ay < by + nodeB.height && ay + nodeA.height > by;
```

Intersection → severity **CRITICAL**

### Boundary Check

For each TEXT node: `node.y + node.height > parent.height` → severity **CRITICAL**

### Gap Check

Distance between adjacent elements < 8px → severity **FAIL**

### Footer Zone

Content enters bottom 44–56px of frame → severity **FAIL**

### Text Truncation

`node.textAutoResize === "TRUNCATE"` or text visually clipped → severity **CRITICAL**

### Return Format

```js
return {
  slide: slideIndex,
  issues: [
    { type: "CRITICAL" | "FAIL", description: "...", nodeIds: ["..."] }
  ]
}
```

---

## Phase B: Visual Comparison

For each slide, call `get_screenshot` twice and compare visually.

```
1. mcp__figma__get_screenshot(originalSlideNodeId, fileKey)  → original template screenshot
2. mcp__figma__get_screenshot(adaptedSlideNodeId, fileKey)   → adapted version screenshot
3. Compare both images side by side — agent evaluates visually
```

**Content will differ** (different text is expected). Compare STYLE, not content:

- Fonts look the same family and weight?
- Colors unchanged (backgrounds, accents, text)?
- Whitespace distribution balanced vs cramped?
- No visual glitches (missing elements, broken layout, stray shapes)?
- Same overall mood and density?

Score this phase 1–10 based on style correspondence.

---

## Phase C: Design Critique

Read `references/design-rules.md` before running this phase.

Per slide, evaluate three areas:

### Element Integrity (highest priority)

| Issue | Severity | Auto-fix |
|-------|----------|----------|
| Text overlaps another element | **CRITICAL** | Shorten or reposition |
| Text extends beyond container boundary | **CRITICAL** | `textAutoResize = "HEIGHT"` + check |
| Elements too close (< 8px gap) | **FAIL** | Increase gap |
| Footer zone (bottom 44–56px) occupied | **FAIL** | Push content up |

### Visual Hierarchy

- Focal point preserved? Heading is the largest element on the slide?
- Logical reading order? (heading → subheading → body → footer)
- Any two elements competing equally for attention?

### Consistency

- Slide looks like it belongs in the same presentation as the original template?
- Fonts, colors, and spacing uniform across all slides?
- Adapted content (different length text) still visually balanced?

---

## Phase D: Score + Fix

### Scoring Formula

**Fidelity Score = Structural (40%) + Visual (30%) + Design Critique (30%)**

Each sub-score is 0–10. Weighted sum = final score out of 10.

| Component | Weight | Scoring Logic |
|-----------|--------|---------------|
| Structural | 40% | 10 if zero CRITICAL/FAIL. Deduct 3 per CRITICAL, 1 per FAIL (min 0). |
| Visual | 30% | Agent score 1–10 based on style correspondence (Phase B). |
| Design Critique | 30% | 10 if zero integrity issues. Deduct 3 per CRITICAL, 1 per FAIL (min 0). |

**Target: ≥ 9/10**

### Fixes via `use_figma`

One `use_figma` call per fix — incremental, not batched:

| Issue | Fix |
|-------|-----|
| Overlap | `node.resize(smallerWidth, height)` or shorten `node.characters` |
| Boundary breach | `node.textAutoResize = "HEIGHT"`, then reduce `fontSize` if still overflowing |
| Gap too small | Adjust `node.y` or `node.x` to restore ≥ 8px gap |
| Footer invaded | Shift all content elements upward |

**MANDATORY on every fix call:** `await figma.setCurrentPageAsync(generatedPage)` at the top, `await figma.loadFontAsync(font)` before any text change.

### Safety Stop

Stop after 5 iterations if score delta < 0.3 between consecutive iterations. Report the plateau and best score achieved.

### Iteration Report

Print after each Phase D:

```
━━━ QA Iteration <N> ━━━
Fidelity: X.X/10
  Structural:       X/10 (CRITICAL: X, FAIL: X)
  Visual:           X/10
  Design Critique:  X/10

Fixed: <list of fixes applied this iteration>
Remaining: <list of unresolved issues>
```

### Final Summary (on DONE)

Print when score reaches ≥ 9/10:

```
━━━ QA Complete ━━━
Final Fidelity: X.X/10
Iterations: N
Total fixes applied: X
Generated page: <pageId>
```

---

## use_figma Rules (reminder)

- MUST `await figma.setCurrentPageAsync(page)` at start of EVERY `use_figma` call
- MUST `await figma.loadFontAsync(font)` before ANY text change
- MUST `return` all results — do not use `console.log` or `figma.notify`
- Make live calls on EACH iteration — do not cache `get_screenshot` results across iterations
- Colors are 0–1 range, not 0–255
- On error: STOP, read the error message, fix, retry
