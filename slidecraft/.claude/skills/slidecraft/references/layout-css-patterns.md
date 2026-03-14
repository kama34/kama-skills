# Layout CSS Patterns

SlideCraft uses `layout:none` for ALL slides with absolute positioning for every text element. This is a fundamentally different approach from standard Slidev layouts — there are no `cover`, `section`, or `default` layout patterns. Everything is zone-based.

## Core Architecture

Every SlideCraft slide follows this structure:

```yaml
---
layout: none
---
```

```html
<div class="slide-bg">
  <img src="./slides/slide-01.png" alt="" />
</div>

<div class="zone zone-main">
  <!-- text content here -->
</div>

<style>
/* Per-slide styles — zone positions and text colors */
</style>
```

## Full-Bleed Background Image

The AI-generated PNG background fills the entire slide frame:

```css
.slide-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
  overflow: hidden;
}

.slide-bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}
```

This pattern is used on every slide. The `object-fit: cover` ensures the AI PNG scales correctly at any aspect ratio without distortion or letterboxing.

## Zone Base Pattern

All text zones share this base:

```css
.zone {
  position: absolute;
  z-index: 1;
  box-sizing: border-box;
}
```

Zone position is set per-slide using `top`, `left`, `width`, `height` as percentages:

```css
.zone-main {
  top: 15%;
  left: 5%;
  width: 58%;
  height: 70%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0 2%;
}
```

**Percentages are preferred over px** — they scale proportionally when Slidev renders at different resolutions.

## Flexbox Within Zones

Use flexbox inside zones for content alignment, not for positioning the zone itself:

```css
/* Vertically centered content within zone */
.zone-main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.75rem;
}

/* Top-aligned content within zone */
.zone-content {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  gap: 0.5rem;
}

/* Centered stat (single large number) */
.zone-stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}
```

## Text Element Patterns

### Heading

```css
.zone h1 {
  font-size: 2.6rem;
  font-weight: 700;
  line-height: 1.15;
  color: #ffffff;
  margin: 0 0 0.5rem;
}

.zone h2 {
  font-size: 1.8rem;
  font-weight: 600;
  line-height: 1.2;
  color: #ffffff;
  margin: 0 0 0.4rem;
}
```

### Bullet List

```css
.zone ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.zone ul li {
  font-size: 1.25rem;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.9);
  padding-left: 1.2em;
  position: relative;
}

.zone ul li::before {
  content: '▸';
  position: absolute;
  left: 0;
  color: var(--color-accent, #4f8ef7);
}
```

### Large Stat / Fact

```css
.zone-stat .stat-number {
  font-size: 5rem;
  font-weight: 800;
  color: var(--color-accent, #4f8ef7);
  line-height: 1;
  margin-bottom: 0.25rem;
}

.zone-stat .stat-label {
  font-size: 1.4rem;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 400;
}
```

### Quote / Callout

```css
.zone blockquote {
  border-left: 3px solid var(--color-accent, #4f8ef7);
  padding-left: 1rem;
  margin: 0;
  font-style: italic;
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.4rem;
  line-height: 1.6;
}

.zone blockquote cite {
  display: block;
  margin-top: 0.5rem;
  font-size: 0.9rem;
  font-style: normal;
  color: rgba(255, 255, 255, 0.6);
}
```

## Zone Fallback: Semi-Transparent Backdrop

When the AI-generated PNG creates a visually busy region behind a text zone, apply a semi-transparent backdrop to ensure readability. Use this as a **fallback** — prefer fixing the PNG prompt first.

```css
/* Light backdrop for contrast issues — light-on-dark mode */
.zone-main {
  background: rgba(0, 0, 0, 0.45);
  border-radius: 4px;
  padding: 1.5rem 1.8rem;
}

/* Dark backdrop for dark-on-light mode */
.zone-main {
  background: rgba(255, 255, 255, 0.75);
  border-radius: 4px;
  padding: 1.5rem 1.8rem;
}

/* Gradient fade — less visible than a solid box */
.zone-main {
  background: linear-gradient(
    to right,
    rgba(0, 0, 0, 0.6) 0%,
    rgba(0, 0, 0, 0.3) 70%,
    transparent 100%
  );
  padding: 1.5rem 2rem;
}
```

**When to use:**
- Visual inspection reveals text is unreadable against the background
- Layer harmony score < 6 due to contrast issues
- Prefer the gradient fade over solid box for aesthetic results

**When NOT to use:**
- When the PNG prompt can be adjusted to keep the zone area visually clear (preferred fix)
- When the AI background already has a clean low-texture zone for text

## Common Zone Strategies

### text-left-60 (default for content slides)

```css
.zone-main {
  top: 12%;
  left: 4%;
  width: 56%;
  height: 76%;
}
```

### text-center (section dividers, title slides)

```css
.zone-main {
  top: 20%;
  left: 15%;
  width: 70%;
  height: 60%;
  text-align: center;
  align-items: center;
}
```

### text-right-60

```css
.zone-main {
  top: 12%;
  left: 40%;
  width: 56%;
  height: 76%;
}
```

### split-40-60 (two-column)

```css
.zone-left {
  top: 15%;
  left: 4%;
  width: 36%;
  height: 70%;
}

.zone-right {
  top: 15%;
  left: 44%;
  width: 52%;
  height: 70%;
}
```

## Global Styles (styles/index.css)

These base rules go in `styles/index.css` — they apply to all slides:

```css
/* Reset Slidev defaults that conflict with zone-based layout */
.slidev-layout {
  padding: 0 !important;
  background: transparent !important;
}

/* Zone base — must be available globally */
.zone {
  position: absolute;
  z-index: 1;
  box-sizing: border-box;
}

.slide-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
  overflow: hidden;
}

.slide-bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* CSS variable defaults — override per preset */
:root {
  --color-accent: #4f8ef7;
}
```
