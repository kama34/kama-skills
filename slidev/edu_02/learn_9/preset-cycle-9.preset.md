---
name: learn-auto-20260324
description: Clean professional light theme with teal accent — warm cream backgrounds, geometric heading + humanist body fonts, balanced density for business/tech presentations
theme: default
colorSchema: light
accentColor: "#0D9488"
fonts:
  heading: Outfit
  body: DM Sans
  mono: JetBrains Mono
transition: fade
aspectRatio: "16/9"
archetypes:
  preferred:
    - stat-hero
    - bento-grid
    - timeline-horizontal
    - two-col-text
    - card-mosaic
  avoid:
    - timeline-zigzag
shapes:
  icon_container: circle
  stat_display: typographic
  label_style: pill
  photo_mask: circle
---

## Aesthetic Direction

Professional warmth meets modern clarity. Warm cream backgrounds with teal accents create trust and readability. Geometric Outfit headings deliver authority, while humanist DM Sans ensures comfortable reading.

**CRITICAL RENDERING RULES:**
1. **Background colors MUST be inline** — Cover/CTA slides: `style="...background:var(--bg-accent)..."` on the background div. Content slides: `style="...background:var(--bg-base)..."`. Sections: `style="...background:var(--bg-alt)..."`. NEVER rely only on CSS classes for backgrounds — always set background as inline style.
2. **Decorative elements** — Content slide background div should include a decorative CSS class (`slide-decor-dots`, `slide-decor-glow`, or `slide-decor-arc`) IN ADDITION to its inline background style. These add ::after pseudo-elements. Rotate across slides.
3. **Shape vocabulary** — Icons: wrap in `<div class="icon-container">`. Labels: use `<span class="label-pill">` on light bg, `<span class="label-pill-cover">` on teal bg. Stat captions: `<span class="stat-caption">`. These classes are defined in styles/index.css.
4. **Card diversity** — NEVER use 3 identical cards. Alternate: first=`class="card-solid"`, second=`class="card-ghost"`, third=`class="card-accent"`. Or use bento-grid (1 large + 2 small).
5. **Teal accent color** — All pill text, icon container borders, stat numbers, and decorative elements MUST use `var(--color-accent)` (#0D9488). If teal is not visible on any slide, the slide is broken.
6. **Cover styling** — Cover background div: `style="position:absolute;inset:0;z-index:0;background:var(--bg-accent);"`. Content div over it with white text. A CSS class (cover-variant-a/b/c) adds subtle decorative overlay. ALWAYS add a `<div class="cover-circle-accent"></div>` inside the background div to anchor the upper-right area — it prevents the top half from feeling empty.
7. **Stat layout** — When showing 2-3 stat numbers in a row, wrap them in `<div class="stat-row">`. NEVER place 3 stat-heroes in a raw flex row without the stat-row class — it causes overflow/clipping. Each stat block needs a `<span class="stat-caption">` beneath it.
8. **Stat slides need a bottom anchor** — Stat-hero slides MUST have a footer element (a highlight box, pill-tag row, or `.stat-footer-band`) to fill the lower third. An empty bottom half makes the slide look unfinished.
   - **2-stat layouts specifically:** When showing only 2 stat numbers, ALWAYS add a supporting body paragraph or a row of context chips (3–4 `label-pill` elements with short labels) between the stat-row and the footer band. Two stats alone leave a visually empty middle zone even with the footer anchored.
9. **CTA layout variety** — Not all CTAs should be centered. Alternate: use centered layout (`align-items:center;text-align:center`) for slides 1-2, left-aligned (`class="cta-variant-left"`) for slides 3+ in the deck.
10. **Timeline slides need density** — Timeline layouts with 3 or fewer rows leave the bottom third empty. ALWAYS use 4+ rows, or increase row card padding to `20px 18px`, or add a summary chip row at the bottom to anchor the lower zone. A timeline slide with visible empty space below the last row is broken.
11. **Bento grid height** — Bento grid containers MUST fill the available vertical space. Set the outer grid div to `flex:1` (inside a flex-column slide layout) so grid rows stretch naturally. Do NOT hardcode `height:340px` — use `min-height:280px` on the grid container and let `grid-template-rows:1fr 1fr` (or similar) fill it.
12. **Stat numbers in bento/card contexts** — When embedding a stat number inside a card (not a full stat-hero slide), ALWAYS follow the number with `<span class="stat-caption">label text</span>`. Never leave a large number without a caption — it loses context and the caption class ensures correct muted color and sizing.
13. **Icon containers on teal backgrounds** — When placing an icon container on a teal (--bg-accent) slide, use `class="icon-container-cover"` instead of `class="icon-container"`. This gives stronger white background/border visibility. Never use the default icon-container style on teal — it becomes invisible.

## CSS

```css
:root {
  /* Background levels */
  --bg-base: #FAF9F6;
  --bg-alt: #E8E6DF;
  --bg-accent: #0D9488;

  /* Text */
  --color-text: #1A2332;
  --color-muted: #5A6577;

  /* Accent hierarchy */
  --color-accent: #0D9488;
  --color-accent-dim: rgba(13, 148, 136, 0.50);
  --color-accent-bg: rgba(13, 148, 136, 0.10);

  /* Surfaces */
  --color-surface: #FFFFFF;
  --color-surface-border: rgba(26, 35, 50, 0.08);

  /* Decomposed RGB */
  --accent-rgb: 13, 148, 136;
  --bg-base-rgb: 250, 249, 246;
  --text-rgb: 26, 35, 50;

  /* Fonts */
  --font-heading: 'Outfit', sans-serif;
  --font-body: 'DM Sans', sans-serif;

  /* Decorative gradient type: radial-gradient */
}

/* Contrast ratios:
   --color-text (#1A2332) vs --bg-base (#FAF9F6): 14.8:1 ✓
   --color-text (#1A2332) vs --bg-alt (#F0EFEB): 13.2:1 ✓
   --color-muted (#5A6577) vs --bg-base (#FAF9F6): 5.4:1 ✓
   --color-muted (#5A6577) vs --bg-alt (#E8E6DF): 4.5:1 ✓
   --color-muted (#5A6577) vs --color-accent-bg: 4.6:1 ✓
*/

.slidev-layout {
  font-family: var(--font-body);
  color: var(--color-text);
}

.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3 {
  font-family: var(--font-heading);
  color: var(--color-text);
}

/* Blockquote reset */
.slidev-layout blockquote {
  background: transparent !important;
  border-left: none !important;
  border: none !important;
  padding: 0 !important;
  margin: 0 !important;
  color: inherit !important;
}

/* Card variants */
.card-solid {
  background: var(--color-surface);
  border: 1px solid var(--color-surface-border);
  border-radius: 14px;
  padding: 20px 24px;
}

.card-ghost {
  background: rgba(var(--bg-base-rgb), 0.55);
  border: 1.5px solid rgba(var(--text-rgb), 0.10);
  border-radius: 14px;
  padding: 20px 24px;
}

.card-accent {
  background: linear-gradient(135deg, rgba(var(--accent-rgb), 0.08), rgba(var(--accent-rgb), 0.03));
  border: 1.5px solid var(--color-accent-dim);
  border-radius: 14px;
  padding: 20px 24px;
}

/* Shape vocabulary */
.icon-container {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--color-accent-bg);
  border: 1.5px solid var(--color-accent-dim);
  display: flex;
  align-items: center;
  justify-content: center;
}

.stat-hero {
  font-size: 5rem;
  font-weight: 800;
  color: var(--color-accent);
  line-height: 1;
  font-family: var(--font-heading);
}

.label-pill {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  background: rgba(var(--accent-rgb), 0.08);
  border: 1.5px solid var(--color-accent-dim);
  border-radius: 20px;
  padding: 6px 18px;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--color-accent);
  font-weight: 600;
}

/* === DECORATIVE MOTIFS (apply to background div with position:absolute;inset:0;z-index:0) === */
/* Rotate across slides: slide-decor-dots → slide-decor-glow → slide-decor-arc → repeat */
/* NOTE: overflow:hidden on .slidev-layout clips anything outside the slide boundary.
   All motif offsets are calibrated to keep the visible portion INSIDE the frame. */

/* Dot grid — top-right quadrant */
.slide-decor-dots::after {
  content: '';
  position: absolute;
  top: 0; right: 0;
  width: 300px; height: 300px;
  background-image: radial-gradient(circle, rgba(var(--accent-rgb), 0.32) 1.5px, transparent 1.5px);
  background-size: 20px 20px;
  pointer-events: none;
}

/* Radial glow — bottom-right corner, center at slide edge for visible bleed */
.slide-decor-glow::after {
  content: '';
  position: absolute;
  bottom: 0; right: 0;
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(var(--accent-rgb), 0.25), transparent 65%);
  pointer-events: none;
}

/* Arc accent — bottom-left, quarter arc visible inside slide. Stronger for light bg compatibility. */
.slide-decor-arc::after {
  content: '';
  position: absolute;
  bottom: -60px; left: -60px;
  width: 260px; height: 260px;
  border: 4px solid rgba(var(--accent-rgb), 0.35);
  border-radius: 50%;
  pointer-events: none;
}

/* === COVER VARIANTS (apply to cover background div) === */

/* Variant A: radial glow from bottom-right, stronger */
.cover-variant-a {
  background: radial-gradient(ellipse 70% 60% at 85% 75%, rgba(255,255,255,0.22), transparent 58%);
}

/* Variant B: diagonal stripe — more opaque for visibility */
.cover-variant-b::after {
  content: '';
  position: absolute;
  top: 0; right: 0;
  width: 40%; height: 100%;
  background: linear-gradient(135deg, transparent 35%, rgba(255,255,255,0.10) 35%, rgba(255,255,255,0.10) 65%, transparent 65%);
  pointer-events: none;
}

/* Variant C: dot grid overlay — stronger dots */
.cover-variant-c::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: radial-gradient(circle, rgba(255,255,255,0.18) 1.5px, transparent 1.5px);
  background-size: 24px 24px;
  pointer-events: none;
}

/* Cover circle accent — anchors upper-right on cover slides, always add inside background div */
.cover-circle-accent {
  position: absolute;
  top: -80px; right: -80px;
  width: 320px; height: 320px;
  border-radius: 50%;
  border: 2px solid rgba(255,255,255,0.18);
  pointer-events: none;
}
.cover-circle-accent::after {
  content: '';
  position: absolute;
  top: 40px; left: 40px;
  right: 40px; bottom: 40px;
  border-radius: 50%;
  border: 1.5px solid rgba(255,255,255,0.10);
}

/* Section slide atmospheric glow */
.section-glow::after {
  content: '';
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 500px; height: 400px;
  background: radial-gradient(ellipse, rgba(var(--accent-rgb), 0.07), transparent 65%);
  pointer-events: none;
}

/* Stat caption — ensures ≥1.25rem on text under hero numbers */
.stat-caption {
  font-size: 1.25rem;
  color: var(--color-muted);
  font-family: var(--font-body);
  line-height: 1.4;
}

/* Stat row layout — prevents overflow for 2–3 stat blocks, use instead of raw flex */
.stat-row {
  display: flex;
  align-items: flex-end;
  gap: 40px;
  flex-wrap: nowrap;
  overflow: hidden;
}
.stat-row .stat-hero {
  font-size: clamp(3rem, 5vw, 5rem);
}

/* Stat footer band — grounds stat-hero slides, place at bottom of slide */
.stat-footer-band {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 72px;
  background: var(--bg-alt);
  border-top: 1px solid var(--color-surface-border);
  display: flex;
  align-items: center;
  padding: 0 72px;
  gap: 24px;
}

/* Cover pill variant — use on teal backgrounds instead of inline-overriding label-pill */
.label-pill-cover {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  background: rgba(255, 255, 255, 0.20);
  border: 1.5px solid rgba(255, 255, 255, 0.45);
  border-radius: 20px;
  padding: 6px 18px;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: #ffffff;
  font-weight: 600;
}

/* CTA variant B — left-aligned for visual variety across multiple CTAs */
.cta-variant-left {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding: 64px 72px;
  text-align: left;
}

/* Icon container on teal/accent backgrounds — stronger white fill for legibility */
.icon-container-cover {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.25);
  border: 2px solid rgba(255, 255, 255, 0.55);
  display: flex;
  align-items: center;
  justify-content: center;
}
```
