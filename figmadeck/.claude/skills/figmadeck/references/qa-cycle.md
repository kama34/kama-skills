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

**PROOF OF EXECUTION:** Phase A MUST produce a `use_figma` return value for EACH slide containing:
```js
return {
  slide: slideIndex,
  checks: {
    overlapCount: N,        // how many TEXT↔ALL overlaps found
    boundaryBreaches: N,    // how many texts exceed parent
    wordBreaks: N,          // how many mid-word breaks detected
    proximityViolations: N, // how many unrelated elements too close
    innerPaddingFails: N,   // how many texts touching container edge
    oversizedOverflows: N,  // how many fontSize>80 texts overflowing
    unchangedPlaceholders: N, // how many original texts unchanged
    contentCoverage: 0.XX,  // visible content area / slide area (programmatic)
  },
  issues: [...]             // detailed issue list
}
```

**If this return structure is missing → Phase A was NOT executed → Structural score = 0/10.**
**If `contentCoverage < 0.30` → CRITICAL: slide is too empty → needs retemplate.**
**If `contentCoverage < 0.40` → FAIL: slide needs rebalancing.**

### Content Coverage Calculation (MANDATORY — programmatic, not visual estimate)

```js
// Calculate actual content coverage for the slide
const allVisible = frame.findAll(n => n.visible && n.type !== "PAGE");
let contentArea = 0;
for (const node of allVisible) {
  if (node.type === "TEXT" || node.type === "FRAME" || node.type === "RECTANGLE" || node.type === "GROUP") {
    contentArea += node.width * node.height;
  }
}
const slideArea = frame.width * frame.height;
const contentCoverage = Math.min(1.0, contentArea / slideArea); // cap at 1.0 (overlapping elements)
```

**Do NOT estimate coverage visually.** Use the programmatic calculation above.

One `use_figma` call per slide (or batch of 3-5 slides).

**MANDATORY:** `await figma.setCurrentPageAsync(generatedPage)` at start of every call.

### Overlap Detection (TEXT ↔ ALL elements)

Check overlap between EVERY visible TEXT node and EVERY other visible node on the slide — not just TEXT↔TEXT. This catches text overlapping dashed lines, shapes, icons, rectangles, vectors.

```js
const allVisible = frame.findAll(n => n.visible && n.id !== frame.id);
const textNodes = allVisible.filter(n => n.type === "TEXT");

for (const text of textNodes) {
  for (const other of allVisible) {
    if (text.id === other.id) continue;
    if (text.parent === other || other.parent === text) continue; // skip parent-child

    const ax = text.absoluteTransform[0][2], ay = text.absoluteTransform[1][2];
    const bx = other.absoluteTransform[0][2], by = other.absoluteTransform[1][2];
    const overlap =
      ax < bx + other.width && ax + text.width > bx &&
      ay < by + other.height && ay + text.height > by;

    if (overlap) {
      issues.push({ type: "CRITICAL",
        desc: `Text "${text.characters.substring(0,20)}" overlaps ${other.type} "${other.name}"` });
    }
  }
}
```

This catches: text overlapping dashed lines (LINE), decorative shapes (RECTANGLE, ELLIPSE, VECTOR), icons (GROUP, FRAME), and other text nodes.

→ severity **CRITICAL**

### Boundary Check

For each TEXT node, check using absolute coordinates:

```js
const nodeBottom = node.absoluteTransform[1][2] + node.height;
const frameBottom = parentFrame.absoluteTransform[1][2] + parentFrame.height;
if (nodeBottom > frameBottom)
```

→ severity **CRITICAL**

### Word-Break Detection (NEW)

After text fill, check if text is breaking mid-word due to narrow container:

```js
for (const textNode of frame.findAll(n => n.type === "TEXT" && n.visible)) {
  const fontSize = typeof textNode.fontSize === 'number' ? textNode.fontSize : 16;
  const charsPerLine = Math.floor(textNode.width / (fontSize * 0.6));

  // If any word in the text is longer than charsPerLine → it WILL break mid-word
  const words = textNode.characters.split(/\s+/);
  const longWords = words.filter(w => w.length > charsPerLine);

  if (longWords.length > 0) {
    issues.push({ type: "CRITICAL",
      desc: `Word-break: "${longWords[0]}" (${longWords[0].length} chars) exceeds container width (${charsPerLine} chars/line)`,
      nodeId: textNode.id });
  }

  // Also check: if text height grew beyond 150% of what a single line would be,
  // the container is probably too narrow for this content
  const singleLineHeight = fontSize * 1.3;
  const expectedLines = Math.ceil(textNode.characters.length / charsPerLine);
  const actualHeight = textNode.height;
  if (actualHeight > singleLineHeight * expectedLines * 1.3) {
    issues.push({ type: "FAIL",
      desc: `Text overflow: "${textNode.characters.substring(0,20)}" wraps excessively — container too narrow`,
      nodeId: textNode.id });
  }
}
```

**Auto-fix**: expand container width (`node.resize(node.width * 1.3, node.height)` + `textAutoResize = "HEIGHT"`), or shorten text to fit.

→ severity **CRITICAL** for mid-word breaks, **FAIL** for excessive wrapping

### Proximity Check for Unrelated Elements (NEW)

Check distance between elements that are NOT in the same group/auto-layout:

```js
for (const text of textNodes) {
  for (const other of allVisible) {
    if (text.id === other.id) continue;
    if (text.parent === other.parent && text.parent.type !== "PAGE") continue; // siblings in same group = OK

    const tx = text.absoluteTransform[0][2], ty = text.absoluteTransform[1][2];
    const ox = other.absoluteTransform[0][2], oy = other.absoluteTransform[1][2];

    // Calculate minimum distance between bounding boxes
    const dx = Math.max(0, Math.max(ox - (tx + text.width), tx - (ox + other.width)));
    const dy = Math.max(0, Math.max(oy - (ty + text.height), ty - (oy + other.height)));
    const distance = Math.sqrt(dx * dx + dy * dy);

    if (distance > 0 && distance < 16) {
      issues.push({ type: "FAIL",
        desc: `Proximity: "${text.characters.substring(0,20)}" is ${Math.round(distance)}px from ${other.type} "${other.name}" — min 16px required`,
        nodeIds: [text.id, other.id] });
    }
  }
}
```

This catches: title pressed against a card edge, text too close to decorative shapes.

→ severity **FAIL**

### Inner Padding Check (NEW)

For each TEXT node inside a FRAME container, check distance from text edges to container edges:

```js
for (const textNode of frame.findAll(n => n.type === "TEXT" && n.visible)) {
  const parent = textNode.parent;
  if (parent.type !== "FRAME" || parent.id === frame.id) continue; // only check nested containers

  const tx = textNode.absoluteTransform[0][2], ty = textNode.absoluteTransform[1][2];
  const px = parent.absoluteTransform[0][2], py = parent.absoluteTransform[1][2];

  const paddingLeft = tx - px;
  const paddingTop = ty - py;
  const paddingRight = (px + parent.width) - (tx + textNode.width);
  const paddingBottom = (py + parent.height) - (ty + textNode.height);

  const minPadding = 8;
  if (paddingLeft < minPadding || paddingRight < minPadding) {
    issues.push({ type: "FAIL",
      desc: `Inner padding: "${textNode.characters.substring(0,20)}" has ${Math.round(Math.min(paddingLeft, paddingRight))}px horizontal padding in "${parent.name}" — min ${minPadding}px`,
      nodeId: textNode.id });
  }
  if (paddingBottom < minPadding && paddingBottom < paddingTop * 0.5) {
    issues.push({ type: "FAIL",
      desc: `Inner padding: "${textNode.characters.substring(0,20)}" touches bottom of "${parent.name}" — ${Math.round(paddingBottom)}px padding`,
      nodeId: textNode.id });
  }
}
```

This catches: text touching the edge of a card/container without proper padding.

→ severity **FAIL**

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

### Group Homogeneity Check

For each slide that contains **repeated elements** (cards, list items, process steps, agenda items — identified by multiple child frames with similar structure):

1. **Identify the group**: child frames with ≥ 2 TEXT nodes each, similar width/height (±20%), and consistent internal layout
2. **For each element**, record:
   - Hero text node: `characters.length`, `fontSize`, overflow status (does text extend beyond container?)
   - Body text node: `characters.length`, overflow status
3. **Pattern detection**: determine the dominant pattern across the group:
   - If ≥ 2/3 of hero texts are 1 character → pattern is "single char"
   - If ≥ 2/3 of hero texts are 1-3 words → pattern is "short phrase"
   - If ≥ 2/3 of body texts are ≤ N words → pattern is "brief"
4. **Outlier detection**: any element that deviates from the dominant pattern AND has overflow → severity **FAIL**
   - Description must include: `"Group homogeneity: {N-1} elements follow pattern '{pattern}', element {i} deviates with '{actual}' and overflows"`
   - Suggested fix: 3 alternatives that match the group pattern (e.g., single symbol, abbreviation, shorter phrasing)
5. **Even without overflow**: if one element is 3× longer than the group median → severity **WARN** (visual imbalance)

**Example**: Cards with hero text `["P", "S", "I", "5с"]` → pattern is "single char" (3/4 match). "5с" deviates + overflows → **FAIL**. Suggested alternatives: `["!", "★", "✓"]`.

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

**Structural score is COMPUTED from Phase A return data — not from visual impression:**

```
structural_score = 10
for each slide:
  structural_score -= 3 * checks.overlapCount
  structural_score -= 3 * checks.boundaryBreaches
  structural_score -= 3 * checks.wordBreaks
  structural_score -= 3 * checks.oversizedOverflows
  structural_score -= 2 * checks.unchangedPlaceholders
  structural_score -= 1 * checks.proximityViolations
  structural_score -= 1 * checks.innerPaddingFails
  if checks.contentCoverage < 0.30: structural_score -= 3  // too empty
  if checks.contentCoverage < 0.40: structural_score -= 1  // needs rebalance
structural_score = max(0, structural_score)
```

| Component | Weight | Scoring Logic |
|-----------|--------|---------------|
| Structural | 40% | **Computed from Phase A data** (formula above). NOT from visual impression. |
| Visual | 30% | Agent score 1–10 based on style correspondence (Phase B). |
| Design Critique | 30% | 10 if zero integrity issues. Deduct 3 per CRITICAL, 1 per FAIL (min 0). |

**Target: ≥ 9/10**

**HARD GATE 1:** If Phase A `checks` structure is missing from ANY slide → Structural = **0/10**. No exceptions.

**HARD GATE 2:** If ANY unchanged placeholder text found → score capped at **5/10**.

**HARD GATE 3:** If ANY slide has `contentCoverage < 0.30` → score capped at **7/10** until retemplated.

### Fix Strategy — MANDATORY PRIORITY ORDER

When fixing issues, you MUST try strategies in this EXACT order. Do NOT jump to shortening text first.

**For text overflow / word-break / proximity issues:**
1. **FIRST: Expand container width** — `node.resize(node.width * 1.2, node.height); node.textAutoResize = "HEIGHT"`. Try up to 30% wider. This is the PREFERRED fix because it doesn't lose content.
2. **SECOND: Expand container and move siblings** — if expanding would overlap with a neighbor, move the neighbor to make room.
3. **THIRD: Shorten text** — rephrase to ~70% length, preserving core meaning.
4. **FOURTH: Reduce fontSize** — minimum = original × 0.85.
5. **LAST RESORT: Retemplate** — if nothing works, swap to a different template (Phase E2b).

**NEVER as a fix:**
- Do NOT create new elements (no new shapes, arrows, icons, text nodes)
- Do NOT replace meaningful content with a symbol/arrow unless it's a Group Homogeneity pattern match
- Do NOT "restore" hidden irrelevant elements
- Do NOT set text to empty string

### Fixes via `use_figma`

One `use_figma` call per fix — incremental, not batched:

| Issue | Fix (in priority order) |
|-------|-----|
| Word-break | 1. Expand width → 2. Shorten text → 3. Reduce font |
| Overlap TEXT↔element | 1. Expand width of text → 2. Move text away → 3. Shorten text |
| Boundary breach | 1. Expand container → 2. `textAutoResize = "HEIGHT"` → 3. Reduce font |
| Proximity < 16px | 1. Move element → 2. Expand text width (reduces height) → 3. Shorten text |
| Inner padding < 8px | 1. Move text inward → 2. Reduce text width → 3. Shorten text |
| Content coverage < 40% | Phase E → retemplate |
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
