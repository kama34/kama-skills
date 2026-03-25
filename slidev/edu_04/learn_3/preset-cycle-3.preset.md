---
name: learn-auto-20260325
theme: default
colorSchema: light
fonts:
  sans: Sora
  body: IBM Plex Sans
  mono: JetBrains Mono
aspectRatio: 16/9
transition: fade
accentColor: "#0D9488"
iconStyle: outlined
densityProfile: balanced
maxFonts: 2
---

Professional light editorial theme with warm cream base and teal accent. Clean, authoritative feel for business presentations across industries — tech, healthcare, education, finance. Follows `editorial` trend with generous whitespace, strong typographic hierarchy, and subtle geometric decoration (dot grids, thin arcs). Warm amber secondary accent for CTAs and key metrics creates temperature contrast against cool teal. Backgrounds use warm cream tones (#FAF9F6 base, #F0EDE8 alt, #0D9488 accent). Cards use ghost and solid styles with 14px radius. Decorative layer uses radial-gradient glows and dot grids at high opacity for light background visibility.

```archetypes
preferred: [stat-hero, bento-grid, asymmetric-split, icon-trio, comparison-table]
avoid: [timeline-zigzag]
cta_style: cta-warm
cover_style: cover-hero
bg_alternation: every 3rd content slide uses --bg-alt; section dividers always --bg-alt; cover+CTA use --bg-accent
icon_container_rule: alternate between circle and rounded-square across deck; no two consecutive icon-trio or bento slides use same icon container; ghost reserved for secondary items only
stat_hero_variants: [centered, left-number-right-text, split-50-50]
stat_hero_rule: no two consecutive stat slides may use same variant; max 1 centered stat per presentation
warm_accent_rule: use --color-accent-warm for at least 1 metric highlight or CTA element per presentation; pricing CTAs and key ROI numbers are warm-accent candidates
```

```shapes
card_radius: 14px
icon_container: [circle, rounded-square]
stat_display: typographic
label_style: pill
divider_style: gradient-fade
photo_mask: rounded-rect
```

```css
/* === learn-auto-20260325 — Light Editorial Professional === */

:root {
  /* Core palette */
  --slidev-theme-primary: #0D9488;
  --slidev-theme-background: #FAF9F6;
  --slidev-theme-code-background: #F0EDE8;

  /* Background levels */
  --bg-base: #FAF9F6;
  --bg-alt: #F0EDE8;
  --bg-accent: #0D9488;

  /* Text */
  --color-text: #1A1A1A;
  --color-muted: #6B6B6B;
  /* --color-muted contrast: vs bg-base (#FAF9F6) = 5.2:1 ✓, vs bg-alt (#F0EDE8) = 4.8:1 ✓, vs bg-accent (#0D9488) = 3.1:1 — use white text on accent */

  /* Accent hierarchy */
  --color-accent: #0D9488;
  --color-accent-dim: rgba(13, 148, 136, 0.50);
  --color-accent-bg: rgba(13, 148, 136, 0.10);
  --color-accent-warm: #D97706;

  /* Surfaces */
  --color-surface: #FFFFFF;
  --color-surface-border: rgba(13, 148, 136, 0.18);

  /* Decomposed RGB for rgba() composability */
  --accent-rgb: 13, 148, 136;
  --bg-base-rgb: 250, 249, 246;
  --text-rgb: 26, 26, 26;

  /* Fonts */
  --font-heading: 'Sora', sans-serif;
  --font-body: 'IBM Plex Sans', sans-serif;

  /* Decorative gradient type: radial-gradient */
}

/* === Base layout === */
.slidev-layout {
  font-family: var(--font-body);
  color: var(--color-text);
  background: var(--bg-base);
}

.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3 {
  font-family: var(--font-heading);
  color: var(--color-text);
}

/* === Blockquote reset === */
.slidev-layout blockquote {
  background: transparent !important;
  border-left: none !important;
  border: none !important;
  padding: 0 !important;
  margin: 0 !important;
  color: inherit !important;
}

/* === layout:none reset === */
.slidev-layout {
  overflow: hidden;
}

/* === Card styles === */
.card-solid {
  background: var(--color-surface);
  border: 1px solid var(--color-surface-border);
  border-radius: 14px;
  padding: 24px;
}

.card-ghost {
  background: transparent;
  border: 1.5px solid var(--color-surface-border);
  border-radius: 14px;
  padding: 24px;
}

.card-accent {
  background: var(--color-accent-bg);
  border: 1.5px solid var(--color-accent-dim);
  border-radius: 14px;
  padding: 24px;
}

.card-glass {
  background: rgba(255, 255, 255, 0.65);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(13, 148, 136, 0.12);
  border-radius: 14px;
  padding: 24px;
}

/* === Shape vocabulary === */
.icon-circle {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--color-accent-bg);
  border: 1.5px solid var(--color-accent-dim);
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-rounded {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  background: var(--color-accent-bg);
  border: 1.5px solid var(--color-accent-dim);
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-ghost {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: transparent;
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
  background: var(--color-accent-bg);
  border: 1.5px solid var(--color-accent-dim);
  border-radius: 20px;
  padding: 6px 18px;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--color-accent);
  font-weight: 600;
  line-height: 1;
}

/* === LAYOUT-SPECIFIC STYLES === */

/* Cover layout — centered text */
.slidev-layout.cover { text-align: center; }
.slidev-layout.cover h1,
.slidev-layout.cover p,
.slidev-layout.cover div { text-align: center; }

/* Section layout */
.slidev-layout.section { text-align: center; }
.slidev-layout.section h1,
.slidev-layout.section p { text-align: center; }

/* Fact layout */
.slidev-layout.fact { text-align: center; }
.slidev-layout.fact h1,
.slidev-layout.fact p { text-align: center; }

/* End layout */
.slidev-layout.end { text-align: center; }
.slidev-layout.end h1,
.slidev-layout.end p,
.slidev-layout.end div { text-align: center; }

/* Statement / Center layouts */
.slidev-layout.statement h1,
.slidev-layout.statement p,
.slidev-layout.center h1,
.slidev-layout.center p { text-align: center; }

/* Background image overlay — gated behind .has-bg-image class */
.slidev-layout.cover,
.slidev-layout.section { position: relative; }
.slidev-layout.cover::before,
.slidev-layout.section::before {
  content: none; /* No overlay by default — cream/teal base shows */
}
.slidev-layout.cover.has-bg-image::before,
.slidev-layout.section.has-bg-image::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, rgba(0,0,0,0.75) 0%, rgba(0,0,0,0.55) 100%);
  z-index: 0;
  pointer-events: none;
}
.slidev-layout.cover > *,
.slidev-layout.section > * {
  position: relative;
  z-index: 1;
}

/* === Accent background text overrides === */
.slidev-layout.cover,
.slidev-layout.end,
.bg-accent-slide {
  color: #FFFFFF;
}
.slidev-layout.cover h1,
.slidev-layout.cover h2,
.slidev-layout.end h1,
.slidev-layout.end h2 {
  color: #FFFFFF;
}
.slidev-layout.cover p,
.slidev-layout.end p,
.slidev-layout.cover span,
.slidev-layout.end span {
  color: rgba(255,255,255,0.85);
}
.slidev-layout.cover .label-pill,
.slidev-layout.end .label-pill {
  background: rgba(255,255,255,0.15);
  border-color: rgba(255,255,255,0.35);
  color: #FFFFFF;
}

/* === Cover heading minimum size === */
.slidev-layout.cover h1 {
  font-size: clamp(3.5rem, 7vw, 6rem);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -0.02em;
}

/* === Background level utilities === */
.bg-base  { background: var(--bg-base) !important; }
.bg-alt   { background: var(--bg-alt) !important; }
.bg-accent-slide { background: var(--bg-accent) !important; }

/* === Decorative layer utilities (light theme — high opacity) === */
.deco-glow-teal {
  position: absolute;
  width: 480px;
  height: 480px;
  background: radial-gradient(circle, rgba(13,148,136,0.18) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
}
.deco-dot-grid {
  position: absolute;
  width: 280px;
  height: 280px;
  background-image: radial-gradient(circle, rgba(13,148,136,0.42) 1.5px, transparent 1.5px);
  background-size: 22px 22px;
  pointer-events: none;
}
.deco-arc {
  position: absolute;
  width: 300px;
  height: 300px;
  border: 2px solid rgba(13,148,136,0.25);
  border-radius: 50%;
  pointer-events: none;
}

/* === Warm accent utilities === */
.label-pill-warm {
  display: inline-flex;
  align-items: center;
  background: rgba(217,119,6,0.10);
  border: 1.5px solid rgba(217,119,6,0.35);
  border-radius: 20px;
  padding: 6px 18px;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: #D97706;
  font-weight: 600;
  line-height: 1;
}
.stat-warm {
  font-size: 5rem;
  font-weight: 800;
  color: #D97706;
  line-height: 1;
  font-family: var(--font-heading);
}
.card-warm {
  background: rgba(217,119,6,0.07);
  border: 1.5px solid rgba(217,119,6,0.25);
  border-radius: 14px;
  padding: 24px;
}

/* === Render failure safeguard === */
.slidev-layout pre:not([class]),
.slidev-layout code:not([class]) {
  display: none !important;
}
```
