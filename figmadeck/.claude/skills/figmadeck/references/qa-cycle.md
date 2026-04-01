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

**HARD GATE — Phase A is MANDATORY.** You MUST run `use_figma` programmatic checks BEFORE taking any screenshots. Do NOT skip to Phase B. Phase A catches problems that are invisible in screenshots (text 1px beyond boundary, 6px gaps, unchanged placeholder text). If you only do screenshots, you WILL miss critical issues.

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

For each TEXT node, check using absolute coordinates:

```js
const nodeBottom = node.absoluteTransform[1][2] + node.height;
const frameBottom = parentFrame.absoluteTransform[1][2] + parentFrame.height;
if (nodeBottom > frameBottom)
```

→ severity **CRITICAL**

### Gap Check

Distance between adjacent elements < 8px → severity **FAIL**

### Footer Zone

Content enters bottom `frame.height * 0.08` of frame → severity **FAIL**

### Text Truncation

`node.textAutoResize === "TRUNCATE"` or text visually clipped → severity **CRITICAL**

### Oversized Text Overflow

For each TEXT node with fontSize > 80px:
- Check: is the text visually contained within its bounding box?
- Check: does `node.width` contain all characters without overlap? (`node.characters.length * fontSize * 0.6 > node.width * maxLines` → overflow)
- Check: `node.absoluteTransform[1][2] + node.height > parentFrame.absoluteTransform[1][2] + parentFrame.height`?

If ANY oversized text is unreadable or overflowing → severity **CRITICAL**

**This is NOT "decorative design" — it is a fill error. Oversized decorative titles (like "PITCH DECK") are designed for 1-3 short words. Longer text MUST be shortened to fit the character budget, or the slide must be retemplated (Phase E).**

### Unchanged Placeholder Text Detection

Compare each text node's content against the ORIGINAL template text:

1. For each TEXT node on the adapted slide, find the corresponding
   original node using the `origId` mapping from Step 2 (clone step)
2. Call `use_figma` to read the original node's `.characters` on the template page
3. If `adaptedText === originalText` AND this node has role
   title/description/subtitle/body (not footer, not decorative) →
   **CRITICAL: text was never replaced**

This is template-agnostic — works for any template, any language.

Also check footer breadcrumbs specifically:
- Footer text that still contains the ORIGINAL TEMPLATE language (English in a Russian presentation, or generic "Reviews / Mobile Strategy") → **CRITICAL**
- Page numbers that don't match sequential 1..N order → **FAIL**

### Return Format

```js
return {
  slide: slideIndex,
  issues: [
    { type: "CRITICAL" | "FAIL", description: "...", nodeIds: ["..."] }
  ]
}
```

**Phase A MUST produce a non-empty result for every slide** — even if zero issues found. If Phase A returns nothing, it was not run correctly.

---

## Phase B: Visual Comparison

**IMPORTANT:** The `originalSlideNodeId` used for comparison comes from
the clone step (Step 2) return value — the `origId` field for each slide.
This is the node ID on the ORIGINAL template page, NOT the cloned page.

```js
slideMapping = {
  adaptedSlideId: "99:125",      // on generated page
  originalSlideNodeId: "1:42",   // on template page (Page 1)
}
```

Pass this mapping through the entire pipeline. Do NOT guess or
reconstruct node IDs — use exactly what the clone step returned.

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
| Footer zone (bottom `frame.height * 0.08`) occupied | **FAIL** | Push content up |

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

**HARD GATE:** If Phase A was not executed (no `use_figma` structural check calls were made), the Structural sub-score is automatically **0/10**. You CANNOT score ≥ 9 without Phase A. This prevents the agent from skipping programmatic checks and relying only on screenshots.

**HARD GATE:** If ANY unchanged placeholder text is found (Phase A "Unchanged Placeholder" check), the score is automatically capped at **5/10** regardless of other sub-scores. Placeholder text = the presentation is not adapted.

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

Print when score reaches ≥ 9/10 AND Phase E passed (no poor fits remaining):

```
━━━ QA Complete ━━━
Final Fidelity: X.X/10
Iterations: N
Total fixes applied: X
Generated page: <pageId>
```

---

## Phase E: Content-Template Fit Assessment

Runs AFTER Phase D score is computed, BEFORE declaring DONE.

### Step E0: Remove Interactive/Widget Elements

**BEFORE visual assessment**, scan each slide for interactive elements that should NEVER appear in generated presentations:

```js
// Find and REMOVE interactive/widget elements
const toRemove = frame.findAll(n =>
  n.type === "WIDGET" ||
  n.type === "SHAPE_WITH_TEXT" ||
  n.name.toLowerCase().match(/poll|vote|facepile|slider|survey|quiz|reaction/)
);
for (const node of toRemove) {
  node.remove();  // Use remove(), NOT visible=false — widgets may ignore visibility
}
```

These are FigJam/interactive elements from the template (polls, voting scales, reactions). They are never relevant to generated content — always **remove** them (not just hide). Figma WIDGET nodes may not respect `visible = false` — `remove()` is the only reliable way to eliminate them.

### Step E1: Visual Assessment

For each slide, get a fresh screenshot (`get_screenshot`) and evaluate:

1. **Does the text content match the visual style?** Playful illustrations + serious financial data = bad fit. Clean layout + wrong content type = bad fit.
2. **Is the text-to-visual ratio preserved?** Template had 30% text / 70% visual, but after fill it's 80% text / 20% visual = bad fit.
3. **Are visual elements (illustrations, icons, decorative images) relevant to the content?**
   - Shopping cart illustration + team structure content = irrelevant
   - Computer/monitor icon + financial data = irrelevant
   - Abstract geometric shapes or gradients = neutral (always OK)
   - Icons that match the topic (chart icon + data slide) = relevant

If fit is **good** → skip to DONE.
If **only specific visual elements are irrelevant** (but template layout fits) → proceed to Step E2a.
If **entire template layout doesn't fit the content** → proceed to Step E2b.

### Step E2a: Hide Irrelevant Visual Elements (cascade)

When the template layout is fine but specific illustrations/icons don't match the content:

**Step 1 — Hide:** Set `node.visible = false` on the irrelevant elements via `use_figma`. Hide only the elements identified as irrelevant — do not expand the scope to related elements.

**Step 2 — Empty space check:** Get a fresh screenshot. Evaluate content coverage:
- Visible content area / total slide area
- If content occupies **less than 30% of slide area** → the slide is TOO EMPTY → go directly to Step 4
- If content occupies 30-50% → rebalanceable → proceed to Step 3
- If content occupies > 50% → looks good → **DONE**

**CRITICAL RULE: A slide with > 40% empty whitespace after hiding is NOT a "statement slide" or "generous whitespace" — it is a broken slide that needs retemplate.** Do NOT accept it as valid. Do NOT score it 9/10.

**Step 3 — Rebalance (only if 30-50% content coverage):**
- Expand text containers to fill available width
- Move remaining content towards center if pushed to one side
- Get screenshot, re-evaluate
- If still looks empty or awkward → proceed to Step 4

**Step 4 — Retemplate decision (MANDATORY if hiding failed):**

After hiding + optional rebalancing, evaluate content coverage again.

**Decision tree:**
- Content coverage ≥ 50% AND no irrelevant visuals visible → **DONE**, slide is fixed
- Content coverage 40-50% AND slide looks balanced → **DONE**, accept as "statement" variant
- Content coverage < 40% OR irrelevant visuals still visible OR slide looks empty/broken:
  → **MUST proceed to E2b** (full retemplate with a different template)
  → Do NOT undo hides and keep the original — the original had irrelevant content, that's why we're here
  → Do NOT "restore" irrelevant illustrations as "visual anchors" — they are WRONG for this content

**CRITICAL: There are only two acceptable outcomes from Phase E:**
1. Slide looks good after hiding + rebalancing → keep
2. Slide doesn't look good after hiding → **retemplate with a different template** (E2b)

**NEVER go back to the original with irrelevant visuals.** "Original with wrong illustrations" is NOT better than "retemplated with correct text-only layout". If E1 identified visuals as irrelevant, they stay irrelevant — restoring them is not a valid fix.

### Step E2b: Retemplate (full swap)

The entire template doesn't fit this content. Swap to a different template:

1. Review ALL available templates from the slide map (Step 3 analysis)
2. Select better-fitting template:
   - Text-heavy content with no matching visuals → text-only or two-column template
   - Metrics/numbers → stat or metric template
   - Process/steps without matching illustrations → timeline or simple list template
3. If NO better template exists → keep current with hidden elements, log "best available"
4. Delete current filled slide → clone new template → fill with same content → run Phases A-D for this slide only
5. Run Step E1 on the new version
6. If still poor fit → keep the better of the two (original with hidden elements vs retemplate)

### Step E3: Compare and Keep

If retemplate was tried: compare original (with hidden elements) vs retemplated version on:
- Structural score (Phase A)
- Visual balance
- Content readability

Keep the winner, delete the loser.

**Phase E cascade per slide:** E0 (widgets) → E1 (assess) → E2a (hide + rebalance) → E2b (retemplate) → E3 (compare). At most 1 retemplate attempt per slide per QA iteration.

---

## use_figma Rules (reminder)

- MUST `await figma.setCurrentPageAsync(page)` at start of EVERY `use_figma` call
- MUST `await figma.loadFontAsync(font)` before ANY text change
- MUST `return` all results — do not use `console.log` or `figma.notify`
- Make live calls on EACH iteration — do not cache `get_screenshot` results across iterations
- Colors are 0–1 range, not 0–255
- On error: STOP, read the error message, fix, retry
