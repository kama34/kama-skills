# Layout CSS Patterns

Battle-tested CSS patterns for Slidev layouts. Use these as the foundation — customize aesthetics but NEVER remove the structural rules.

## Critical Rule: Explicit Text Alignment

Slidev's `@slidev/theme-default` (and other themes) set `text-align: left` on child elements with CSS specificity that **overrides inherited `text-align`** from parent containers. You MUST set `text-align` explicitly on every text element (`h1`, `h2`, `p`, `li`, `div`) inside centered layouts — never rely on inheritance from the parent `.slidev-layout`.

**Wrong** (inheritance will be overridden by theme):
```css
.slidev-layout { text-align: center; }
```

**Correct** (explicit on each element):
```css
.slidev-layout { text-align: center; }
h1, h2, p { text-align: center; }
```

## Critical Rule: Background Images

When using `background:` frontmatter prop on any layout, the image is rendered on a **parent container above** `.slidev-layout`. The layout's own `background-color` (from theme or `styles/index.css`) is **opaque** and **blocks** the parent's background image.

**Fix**: Always set `background-color: transparent !important` and `background-image: none !important` on `.slidev-layout` in the per-slide `<style>` for any slide that uses the `background:` frontmatter prop.

Alternatively, set the background image **directly on `.slidev-layout`** via per-slide CSS `background: url(...)` instead of using the frontmatter prop — this is more reliable.

## Cover Layout (with background image)

```css
/* Per-slide <style> for cover with background image */
.slidev-layout {
  background: url('/images/cover.jpg') center/cover no-repeat !important;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  position: relative;
}
.slidev-layout::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 0;
}
.slidev-layout > * {
  position: relative;
  z-index: 1;
}
h1 {
  text-align: center;
  color: #ffffff !important;
}
p {
  text-align: center;
  color: rgba(255, 255, 255, 0.8);
}
```

## Cover Layout (no background image)

```css
.slidev-layout {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
h1 { text-align: center; }
p { text-align: center; }
```

## Section Layout (with background image)

```css
.slidev-layout {
  background: url('/images/section.jpg') center/cover no-repeat !important;
  position: relative;
}
.slidev-layout::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  z-index: 0;
}
.slidev-layout > * {
  position: relative;
  z-index: 1;
}
h1 { text-align: center; color: #ffffff !important; }
p { text-align: center; color: rgba(255, 255, 255, 0.85); }
```

## Section Layout (no background image)

```css
.slidev-layout {
  background-image: none;
}
.slidev-layout::before { display: none; }
h1 { text-align: center; }
p { text-align: center; }
```

## Fact Layout

```css
.slidev-layout {
  background-image: none;
}
h1 {
  text-align: center;
  font-size: 5em !important;
  color: var(--color-accent) !important;
}
p {
  text-align: center;
  max-width: 500px;
  margin: 0 auto;
}
```

## End Layout

```css
.slidev-layout {
  background-image: none;
}
h1 {
  text-align: center;
  max-width: 700px;
  margin: 0 auto;
}
p, div { text-align: center; }
```

## Statement / Center Layout

```css
h1, h2, p { text-align: center; }
blockquote, blockquote p { text-align: center; }
```

**CRITICAL — Blockquote centering**: Setting `text-align: center` on the flex container is NOT sufficient for centering `<blockquote>` content. The theme's specificity overrides inherited alignment. Always set `text-align: center` explicitly on the `<blockquote>` element and on every `<p>` inside it.

## Overlay CSS for styles/index.css

When background images are used on cover/section slides, add this to `styles/index.css`:

```css
/* Background image overlay support */
.slidev-layout.cover,
.slidev-layout.section {
  position: relative;
}
.slidev-layout.cover::before,
.slidev-layout.section::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  z-index: 0;
}
.slidev-layout.cover > *,
.slidev-layout.section > * {
  position: relative;
  z-index: 1;
}
```

**IMPORTANT**: Even with this global overlay CSS, each slide's per-slide `<style>` must still:
1. Set `background-color: transparent !important` if using frontmatter `background:` prop
2. Set `text-align: center` explicitly on `h1`, `p`, etc.
3. Set text colors for readability against the dark overlay (white/near-white)
