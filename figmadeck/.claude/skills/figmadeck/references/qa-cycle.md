# QA Cycle — Per-Slide Sequential

Process slides ONE AT A TIME. Check → fix → confirm → next slide.

## Critical Rules

1. **NEVER add content not in the outline.** Only use text from the outline. Do not invent, expand, or rephrase beyond what the outline provides.
2. **NEVER skip the structural check.** Every slide gets a `use_figma` call BEFORE screenshots.
3. **Every fix gets a screenshot.** Fix → screenshot → verify. If problem remains → fix again.
4. **Fix priority: expand first, shorten last.** Expand container width → move elements → shorten text → reduce font → retemplate.
5. **Overlap with ANY element is CRITICAL.** Text overlapping lines, shapes, separators, icons — all unacceptable. Move the decorative elements OR shorten the text.
6. **Expand width guardrail:** Never expand beyond `frame.width - node.x - 70px`.

---

## Per-Slide Loop

```
for each slide (in order, 1 to N):

  STEP 1: Structural check (use_figma)
  STEP 2: Screenshot + visual check
  STEP 3: Fix issues (if any)
  STEP 4: Re-check until clean
  STEP 5: Content-template fit (Phase E)

when all slides clean → final score
```

---

## STEP 1: Structural Check

One `use_figma` call for THIS slide. Returns a `checks` object.

```js
await figma.setCurrentPageAsync(generatedPage);
const frame = figma.getNodeById(slideId);
const fY = frame.absoluteTransform[1][2], fH = frame.height, fW = frame.width;

const checks = {
  overlapCount: 0, boundaryBreaches: 0, wordBreaks: 0,
  proximityViolations: 0, innerPaddingFails: 0,
  oversizedOverflows: 0, unchangedPlaceholders: 0,
  contentCoverage: 0, artifactsFound: 0
};
const issues = [];

// --- Coverage ---
let contentArea = 0;
for (const n of frame.findAll(n => n.visible)) {
  if (["TEXT","FRAME","RECTANGLE","GROUP"].includes(n.type))
    contentArea += n.width * n.height;
}
checks.contentCoverage = Math.min(1.0, contentArea / (fW * fH));

// --- All visible nodes ---
const allVisible = frame.findAll(n => n.visible && n.id !== frame.id);
const textNodes = allVisible.filter(n => n.type === "TEXT");

for (const t of textNodes) {
  const tx = t.absoluteTransform[0][2], ty = t.absoluteTransform[1][2];
  const fs = typeof t.fontSize === 'number' ? t.fontSize : 16;

  // Boundary: text exceeds slide frame
  if (ty + t.height > fY + fH + 1) {
    checks.boundaryBreaches++;
    issues.push({ type: "CRITICAL", desc: `Boundary: "${t.characters.substring(0,20)}" +${Math.round(ty+t.height-fY-fH)}px` });
  }

  // Word-break: word longer than container width in chars
  const cpl = Math.floor(t.width / (fs * 0.6));
  if (cpl > 0) {
    for (const w of t.characters.split(/\s+/)) {
      if (w.length > cpl) {
        checks.wordBreaks++;
        issues.push({ type: "CRITICAL", desc: `Word-break: "${w}" (${w.length}>${cpl})`, nodeId: t.id });
        break;
      }
    }
  }

  // Oversized text overflow (fontSize > 80px)
  if (fs > 80 && ty + t.height > fY + fH) {
    checks.oversizedOverflows++;
    issues.push({ type: "CRITICAL", desc: `Oversized: "${t.characters.substring(0,15)}" fs=${fs}` });
  }

  // Inner padding: text touching container edge
  if (t.parent && t.parent.type === "FRAME" && t.parent.id !== frame.id) {
    const px = t.parent.absoluteTransform[0][2], py = t.parent.absoluteTransform[1][2];
    const padL = tx - px, padR = (px + t.parent.width) - (tx + t.width);
    const padB = (py + t.parent.height) - (ty + t.height);
    if (padL < 8 || padR < 8 || padB < 4) {
      checks.innerPaddingFails++;
      issues.push({ type: "FAIL", desc: `Padding: "${t.characters.substring(0,15)}" pad=${Math.round(Math.min(padL,padR,padB))}px` });
    }
  }

  // Overlap: text vs ALL other visible elements (lines, shapes, rectangles)
  for (const other of allVisible) {
    if (t.id === other.id) continue;
    // Skip ancestor/descendant relationships
    let isRelated = false;
    let c = t.parent; while(c) { if(c.id===other.id) { isRelated=true; break; } c=c.parent; }
    c = other.parent; while(c) { if(c.id===t.id) { isRelated=true; break; } c=c.parent; }
    if (isRelated) continue;
    // Skip siblings in same top-level section
    let tTop = t, oTop = other;
    while(tTop.parent && tTop.parent.id !== frame.id) tTop = tTop.parent;
    while(oTop.parent && oTop.parent.id !== frame.id) oTop = oTop.parent;
    if (tTop.id === oTop.id) continue;

    const bx = other.absoluteTransform[0][2], by = other.absoluteTransform[1][2];
    if (tx < bx+other.width && tx+t.width > bx && ty < by+other.height && ty+t.height > by) {
      checks.overlapCount++;
      issues.push({ type: "CRITICAL", desc: `Overlap: "${t.characters.substring(0,15)}" ↔ ${other.type} "${other.name}"` });
    }
  }
}

// --- Unchanged placeholders ---
// (compare with original template - use origId from clone step)
await figma.setCurrentPageAsync(templatePage);
const origFrame = figma.getNodeById(origSlideId);
if (origFrame) {
  const origChars = origFrame.findAll(n => n.type === "TEXT").map(n => n.characters);
  await figma.setCurrentPageAsync(generatedPage);
  for (const t of textNodes) {
    if (typeof t.fontSize === 'number' && t.fontSize > 14 &&
        origChars.includes(t.characters) && t.characters.length > 3) {
      checks.unchangedPlaceholders++;
      issues.push({ type: "CRITICAL", desc: `Placeholder: "${t.characters.substring(0,25)}"` });
    }
  }
}

// --- Artifacts: elements created by agent that don't belong ---
// Small shapes/arrows that weren't in the original template
// (compare child count: if adapted has MORE children than original → suspicious)

return { slide: slideIndex, checks, issues };
```

**If `checks` structure is missing → this slide was NOT checked → cannot proceed.**

---

## STEP 2: Screenshot + Visual Check

Take screenshot of THIS slide: `get_screenshot(adaptedSlideId, fileKey)`

Look at it and check:
- Does it look clean and professional?
- Any visual glitches, broken elements, stray shapes?
- Text readable, not cramped, not overflowing?
- Consistent with the template's design language?

---

## STEP 3: Fix Issues

If STEP 1 or STEP 2 found problems, fix them. **One fix at a time, verify after each.**

### Fix Priority (MANDATORY ORDER)

1. **Expand container width** — make text block wider so text wraps less. Cap: `frame.width - node.x - 70px`
2. **Move decorative elements** — shift lines/shapes to make room for text
3. **Shorten text** — rephrase shorter (ONLY with outline content, NEVER invent new text)
4. **Reduce fontSize** — minimum = original × 0.85
5. **Retemplate** — swap to a different template (see Phase E below)

### Fix Rules

- **Overlap with lines/separators**: move the lines apart OR shorten text. Both are valid.
- **Inner padding < 8px**: shrink text node width slightly OR move text inward
- **Breadcrumb wrapping**: if footer/breadcrumb text wraps to 2+ lines, expand width or shorten label
- **Artifacts from previous fixes**: if you see elements you created in a previous iteration that look wrong (white arrows, extra shapes) → `node.remove()` them

After EACH fix: take new screenshot → verify the fix worked.

---

## STEP 4: Re-Check

After all fixes for this slide:
1. Run STEP 1 (structural check) again
2. Run STEP 2 (screenshot) again
3. If zero CRITICAL and zero FAIL → slide is **CLEAN** → move to next slide
4. If issues remain → STEP 3 again (max 3 fix iterations per slide)
5. After 3 iterations if not clean → log remaining issues, move to next slide

---

## STEP 5: Content-Template Fit (Phase E)

After the slide is structurally clean, evaluate fit:

### E0: Remove widgets
```js
frame.findAll(n => n.type === "WIDGET" || n.type === "SHAPE_WITH_TEXT")
  .forEach(n => n.remove());
```

### E1: Does this template fit the content?
- Do visual elements (illustrations, icons) match the content topic?
- Is the text-to-visual ratio reasonable?
- If **poor fit** → E2

### E2: Fix poor fit
1. **Hide irrelevant visuals** → check coverage → if < 40% empty → E2b
2. **Rebalance** if 30-50% coverage → expand text, center content
3. **Retemplate** (E2b) if still broken: clone different template → fill → re-run Steps 1-4

**NEVER restore irrelevant visuals. NEVER go back to original if visuals were identified as wrong.**

---

## Final Score

After ALL slides are processed:

```
clean_slides = slides with zero CRITICAL and zero FAIL
total_slides = N
score = clean_slides / total_slides * 10

If score >= 9 → DONE
If score < 9 → report which slides still have issues
```

### Final Report

```
━━━ QA Complete ━━━
Score: X.X/10
Clean slides: X/N
Issues remaining: [slide numbers + descriptions]
Generated page: <pageId>
```

---

## use_figma Rules

- `await figma.setCurrentPageAsync(page)` at START of EVERY call
- `await figma.loadFontAsync(font)` BEFORE any text change
- `return` all results (not console.log, not figma.notify)
- Colors 0–1 range, not 0–255
- On error: STOP, read, fix, retry
