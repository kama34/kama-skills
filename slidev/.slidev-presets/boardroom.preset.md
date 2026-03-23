---
name: boardroom
theme: default
colorSchema: light
fonts:
  sans: Outfit
  body: DM Sans
  mono: IBM Plex Mono
aspectRatio: 16/9
transition: fade
accentColor: "#0D9488"
iconStyle: outlined
densityProfile: balanced
maxFonts: 2
---

Editorial confidence for investor and board-level presentations. Warm white backgrounds with teal accent punches. Magazine-quality typography — Outfit delivers geometric precision for numbers and headings, Source Serif 4 provides refined body text. Authority through whitespace and scale, not decoration. Subtle radial-gradient circles as the sole decorative motif. Clean card surfaces with thin borders. Data-first: numbers dominate, text supports.

```archetypes
preferred: [stat-hero, bento-grid, comparison-table, card-mosaic, asymmetric-split, data-spotlight]
avoid: [timeline-zigzag]
cta_style: cta-warm
cover_style: cover-hero
```

```shapes
card_radius: 14px
icon_container: circle
stat_display: typographic
label_style: pill
divider_style: horizontal
photo_mask: circle
```

```css
:root {
  --slidev-theme-primary: #0D9488;
  --slidev-theme-background: #FAFAF8;
  --slidev-theme-code-background: #F0F0ED;

  --color-bg: #FAFAF8;
  --color-text: #1C1C1A;
  --color-accent: #0D9488;
  --color-accent-dim: rgba(13, 148, 136, 0.45);
  --color-accent-bg: rgba(13, 148, 136, 0.08);
  --color-surface: #EDEDEA;
  --color-surface-border: rgba(28, 28, 26, 0.08);
  --color-muted: #5A5A55;

  /* Background level system — warm temperature */
  --bg-base: #FAFAF8;
  --bg-alt: #F0F0ED;
  --bg-accent: #0D3B44;
  /* Contrast: --color-muted (#5A5A55) vs --bg-base (#FAFAF8): 7.0:1 ✓ */
  /* Contrast: --color-muted (#5A5A55) vs --bg-alt (#F0F0ED): 6.4:1 ✓ */
  /* Contrast: --color-muted (#5A5A55) vs accent-bg surface: 6.5:1 ✓ */

  --font-heading: 'Outfit', sans-serif;
  --font-body: 'DM Sans', sans-serif;

  --accent-rgb: 13, 148, 136;

  /* Decorative gradient type: radial-gradient */
}

.slidev-layout {
  background-color: var(--color-bg);
  color: var(--color-text);
}

.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3 {
  color: var(--color-text);
  font-family: var(--font-heading);
  letter-spacing: -0.02em;
}

.slidev-layout p,
.slidev-layout li {
  color: var(--color-text);
  line-height: 1.4;
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

/* === LAYOUT-SPECIFIC STYLES === */
.slidev-layout.cover { text-align: center; }
.slidev-layout.cover h1,
.slidev-layout.cover p { text-align: center; }

.slidev-layout.section { text-align: center; }
.slidev-layout.section h1,
.slidev-layout.section p { text-align: center; }

.slidev-layout.fact { text-align: center; }
.slidev-layout.fact h1,
.slidev-layout.fact p { text-align: center; }

.slidev-layout.end { text-align: center; }
.slidev-layout.end h1,
.slidev-layout.end p,
.slidev-layout.end div { text-align: center; }

.slidev-layout.statement h1,
.slidev-layout.statement p,
.slidev-layout.center h1,
.slidev-layout.center p { text-align: center; }

/* Background image overlay support */
.slidev-layout.cover,
.slidev-layout.section { position: relative; }
.slidev-layout.cover::before,
.slidev-layout.section::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  z-index: 0;
  pointer-events: none;
}
.slidev-layout.cover > *,
.slidev-layout.section > * {
  position: relative;
  z-index: 1;
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

.stat-hero-num {
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
  background: var(--color-surface);
  border: 1.5px solid var(--color-accent-dim);
  border-radius: 20px;
  padding: 6px 18px;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--color-accent);
  font-weight: 600;
}
```
