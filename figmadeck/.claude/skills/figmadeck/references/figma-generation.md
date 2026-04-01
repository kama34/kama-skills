# Figma-Native Generation Pipeline

Steps 2-5 of the figmadeck pipeline. Runs after auth check (Step 1). Followed by `qa-cycle.md` (Step 6).

---

## Step 2: Clone Template Page

**One `use_figma` call.**

```js
// 1. Set context to Page 1 (the template)
const page1 = figma.root.children[0];
await figma.setCurrentPageAsync(page1);

// 2. Create the new page
const newPage = figma.createPage();
newPage.name = "Generated: <outline-name>";  // e.g. "Generated: Q1 Sales Review"

// 3. Clone all children from the template, preserving exact positions
const slides = [];
for (const child of page1.children) {
  const clone = child.clone();
  newPage.appendChild(clone);
  clone.x = child.x;   // MUST set after appendChild
  clone.y = child.y;
  slides.push({ id: clone.id, name: clone.name, origId: child.id, x: clone.x });
}

// 4. Return identifiers for subsequent steps
return { pageId: newPage.id, slides };
```

**What clone preserves:** gradients, images, shadows, auto-layout, variable bindings, effects, fonts, colors — pixel-perfect by definition. No conversion artifacts.

**Return shape:** `{ pageId: string, slides: [{ id, name, origId, x }] }`

---

## Step 3: Analyze Template Slides

**One `use_figma` call on the cloned page.**

```js
const generatedPage = figma.root.children.find(p => p.id === pageId);
await figma.setCurrentPageAsync(generatedPage);

const slideMap = [];

for (const frame of generatedPage.children) {
  const textNodes = frame.findAll(n => n.type === "TEXT");

  const texts = textNodes.map(node => ({
    id: node.id,
    name: node.name,
    characters: node.characters,
    fontSize: node.fontSize,
    x: node.absoluteTransform[0][2],
    y: node.absoluteTransform[1][2],
    width: node.width,
    height: node.height,
    role: detectRole(node, frame, textNodes),
  }));

  slideMap.push({
    id: frame.id,
    name: frame.name,
    index: generatedPage.children.indexOf(frame),
    contentType: detectContentType(frame, texts, generatedPage),
    textNodes: texts,
  });
}

return { slideMap };
```

### Text Node Role Detection (hybrid: name priority + heuristics)

Apply rules in order — first match wins:

| Priority | Condition | Role |
|---|---|---|
| 1 | `node.name` includes "Title" or "Heading" (case-insensitive) | `title` |
| 2 | `node.name` includes "description", "body", or "desc" (case-insensitive) | `description` |
| 3 | Largest `fontSize` on slide AND `fontSize >= 36` | `title` |
| 4 | Second largest `fontSize`, in range 16-24px, `characters.length > 50` | `description` |
| 5 | `node.y > frame.height * 0.9` AND `fontSize < 14` | `footer` |
| 6 | `characters.length < 20` AND `characters === characters.toUpperCase()` | `label` |
| 7 | Everything else | `body` |

**Use `includes()` not `===` for name checks** — Unicode normalization differs after clone.

### Content Type Detection

Evaluate per frame after collecting text roles:

| Condition | contentType |
|---|---|
| First frame on page AND has a `title` role node with `fontSize >= 48` | `intro` |
| Last frame on page AND text includes CTA patterns ("contact", "next steps", "start", "connect") | `cta` |
| Single text node, numeric content, `fontSize >= 64` | `metric` |
| Frame has 3+ direct children that are frames (similar width/height) | `cards` |
| `< 30` total text characters AND 1+ image fills on child nodes | `visual-break` |
| Default | `content` |

---

## Step 4: Match Outline → Template Slides

Parse the outline to determine count and content type for each slide, then reconcile against the template `slideMap`.

### Matching Algorithm

```
for each outlineSlide:
  1. Determine outlineSlide.contentType (same heuristics as Step 3)
  2. Find templateSlides where templateSlide.contentType === outlineSlide.contentType
  3. If multiple matches → context-based variant selection:
     - Warm color palette in template + positive/growth theme in outline → prefer
     - Cool/analytical palette + data/metrics theme → prefer
     - When ambiguous → pick first unassigned match
  4. Mark matched template slide as assigned
```

### When Outline Has MORE Slides Than Template Slots

If no unassigned template slide matches the required content type, clone an existing one:

```js
// Additional use_figma call
await figma.setCurrentPageAsync(generatedPage);
const donor = generatedPage.children.find(f => f.id === bestMatchId);
const cloned = donor.clone();
generatedPage.appendChild(cloned);
cloned.x = donor.x + donor.width + 100;  // temporary position
cloned.y = donor.y;
return { newSlideId: cloned.id };
```

### Remove Unused Slides

```js
// In the same or a separate use_figma call
await figma.setCurrentPageAsync(generatedPage);
for (const unusedId of unusedTemplateIds) {
  const node = figma.getNodeById(unusedId);
  if (node) node.remove();
}
```

### Reorder by Outline Position

Set `node.x` so slides flow left-to-right in outline order:

```js
await figma.setCurrentPageAsync(generatedPage);
let xOffset = 0;
for (const slideId of orderedSlideIds) {
  const node = figma.getNodeById(slideId);
  node.x = xOffset;
  xOffset += node.width + 100;  // 100px gap between slides
}
```

---

## Step 5: Fill Content

**One `use_figma` call PER SLIDE** (incremental, not batched). This keeps errors isolated — if one slide fails, others are unaffected.

```js
// Called once per slide
await figma.setCurrentPageAsync(generatedPage);  // MANDATORY every call

const frame = figma.getNodeById(slideId);
const outlineSlide = /* matching outline slide data */;

for (const textNode of frame.findAll(n => n.type === "TEXT")) {
  const role = detectRole(textNode, frame, frame.findAll(n => n.type === "TEXT"));
  const newText = outlineSlide.content[role];
  if (!newText) continue;

  await applyText(textNode, newText, frame);
}

return { slideId, filled: true };
```

### Font Handling

**MUST `loadFontAsync` before any text change.** Never skip this step.

```js
async function applyText(node, newText, parentFrame) {
  // 1. Check availability
  const available = await figma.listAvailableFontsAsync();
  const fontFamily = node.fontName.family;
  const fontStyle = node.fontName.style;

  const isAvailable = available.some(
    f => f.fontName.family === fontFamily && f.fontName.style === fontStyle
  );

  // 2. Resolve font (original or fallback)
  let resolvedFont = node.fontName;
  if (!isAvailable) {
    resolvedFont = resolveFallback(fontFamily, fontStyle);
    console.log(`Font fallback: ${fontFamily} → ${resolvedFont.family}`);
    node.fontName = resolvedFont;  // set before characters
  }

  // 3. Load font — MANDATORY before characters assignment
  await figma.loadFontAsync(resolvedFont);

  // 4. Assign text
  node.characters = newText;

  // 5. Overflow handling
  node.textAutoResize = "HEIGHT";
  if (node.y + node.height > parentFrame.height) {
    handleOverflow(node, newText, parentFrame);
  }
}
```

### Font Fallback Table

| Original Family | Fallback Family |
|---|---|
| Whyte | Inter |
| Whyte Inktrap | Inter |
| Darker Grotesque | Manrope |
| Neue Haas Grotesk | Inter |
| GT Walsheim | Inter |
| Playfair Display | DM Serif Display |
| Custom serif (unknown) | DM Serif Display |
| Any other unavailable | Inter |

Always match the original `style` (Regular, Bold, Italic, etc.) in the fallback family. If the exact style is also unavailable, use Regular.

### Text Overflow Handling

Applied in order — stop at first resolution:

1. **textAutoResize = "HEIGHT"** — let text grow downward (always set this first)
2. **Check overflow:** `node.y + node.height > parentFrame.height`
3. If still overflowing: **shorten/rephrase** the text (preserve core meaning, aim for ~70% length)
4. If still overflowing: **reduce fontSize** — minimum = `current × 0.85` (never go below 85% of original)
5. If still overflowing: **expand container** — increase `node.height` if space exists below
6. Last resort: add a note text node positioned below the slide frame (visible in Figma but outside slide bounds)

### Special Characters

After clone, Unicode normalization may differ. Rules:

- Use `node.characters.includes(searchTerm)` not `===` for text matching
- For footer/breadcrumb nodes: find by **position** (`node.y > frame.height * 0.9` AND `node.fontSize < 14`) rather than by exact text content
- Do not hardcode special characters (em-dash, bullet, arrow) as string literals — use the node's existing character content as reference

### Return Shape (per slide call)

```js
return {
  slideId,
  filled: true,
  fontSubstitutions: [{ original, fallback }],  // empty if none
  overflowsResolved: number,
};
```

---

## use_figma Rules

These apply to ALL `use_figma` calls in the pipeline:

- **MUST** `await figma.setCurrentPageAsync(page)` at the START of every `use_figma` call — page context resets between calls
- **MUST** `await figma.loadFontAsync(font)` BEFORE any `node.characters` assignment — even if the font was loaded in a previous call
- **`layoutSizingHorizontal = "FILL"`** MUST be set AFTER `parent.appendChild(child)`, never before
- **MUST** `return` all created or mutated node IDs — do not use `console.log` or `figma.notify` for output
- Colors are in 0–1 range, not 0–255
- Use `includes()` not `===` for text/name matching (Unicode differences after clone)
- On any error: STOP — read the full error message, fix the script, retry. Do not ignore errors.
