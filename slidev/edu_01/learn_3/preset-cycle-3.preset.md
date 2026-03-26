---
name: learn-auto-2025
theme: default
colorSchema: light
fonts:
  sans: Manrope
  body: DM Sans
  mono: JetBrains Mono
aspectRatio: 16/9
transition: fade
accentColor: "#0D9488"
archetypes:
  preferred: [stat-hero, bento-grid, timeline-horizontal, asymmetric-split, card-mosaic]
  avoid: [profile-grid]
shapes:
  icon_container: circle
  stat_display: typographic
  label_style: pill
  card_radius: 14px
  photo_mask: circle
---

Warm professional aesthetic with cream backgrounds and teal accent. Clean editorial feel — generous whitespace, confident typography, subtle atmospheric gradients. Designed for business presentations across industries: commercial proposals, educational lectures, financial reports.

Mood: trustworthy, modern, competent. Not flashy — quietly confident.
Background personality: warm cream base with subtle radial glows in teal. Alt backgrounds shift slightly cooler.
Card treatment: rounded corners (14px), ghost borders, occasional solid accent card for hierarchy. Ghost-card on bg-base: use border rgba(accent,0.30) for sufficient visibility — rgba(0.15) disappears on cream. Ghost-card on bg-alt: rgba(0.18) is sufficient. Bento side-card numbers: min 2.4rem for fast scanning.
Decorative layer: circles and arcs at VISIBLE opacity (0.25-0.35 for atmosphere, 0.25-0.30 for arc/ring borders on light backgrounds), dot-grids on 30% of slides. Light theme requires higher opacity than dark — decorations must be clearly visible in PNG export. Ring/arc border width: 2px minimum (not 1.5px) for visibility. Section-divider archetype: use TWO concentric rings (outer at full size, inner at 60% size) for richer visual texture. Icon-2×2 grid: vary card styles — one accent-card (bg-accent + border-accent), one ghost-card (transparent bg, border-only), remaining surface-cards — to create internal hierarchy.
Typography drama: hero numbers at 5.5-6rem in teal, headings at 2.4-2.8rem in near-black, body at 1.25rem in warm grey. Stat-hero atmosphere: primary glow opacity 0.28 (up from 0.22), warm amber secondary glow opacity 0.14 — two glow layers create depth. CTA double rings: outer top:-100px/left:-100px, inner top:-65px/left:-65px for consistent cross-run positioning.

```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=DM+Sans:wght@400;500;600;700&display=swap');

:root {
  /* === PALETTE === */
  --color-accent: #0D9488;
  --color-accent-dim: rgba(13, 148, 136, 0.50);
  --color-accent-bg: rgba(13, 148, 136, 0.10);
  --color-accent-warm: #D97706;
  --color-text: #1C1917;
  --color-muted: #6B7280;
  --color-surface: rgba(13, 148, 136, 0.05);
  --color-surface-border: rgba(13, 148, 136, 0.15);

  /* === BACKGROUND LEVELS === */
  --bg-base: #FAF9F6;
  --bg-alt: #E8E6DF;
  --bg-accent: #0D9488;

  /* === RGB DECOMPOSED === */
  --accent-rgb: 13, 148, 136;
  --bg-base-rgb: 250, 249, 246;
  --text-rgb: 28, 25, 23;

  /* === FONTS === */
  --font-heading: 'Manrope', sans-serif;
  --font-body: 'DM Sans', sans-serif;

  --slidev-theme-primary: #0D9488;
  --slidev-theme-background: #FAF9F6;

  /* Decorative gradient type: radial-gradient */
  /* Muted contrast: #6B7280 vs #FAF9F6 = 5.1:1 ✓, vs #E8E6DF = 4.5:1 ✓, vs #0D9488 bg+white text ✓ */
  /* Light theme decoration opacity: atmosphere 0.25-0.35, borders 0.25-0.30 (higher than dark theme) */
  /* Arc/ring border-width: 2px minimum for light backgrounds (1.5px disappears on cream) */
}

/* === BASE LAYOUT === */
.slidev-layout {
  font-family: 'DM Sans', sans-serif;
  color: var(--color-text);
}

.slidev-layout h1, .slidev-layout h2, .slidev-layout h3 {
  font-family: 'Manrope', sans-serif;
}

/* === BLOCKQUOTE RESET === */
.slidev-layout blockquote {
  background: transparent !important;
  border-left: none !important;
  border: none !important;
  padding: 0 !important;
  margin: 0 !important;
  color: inherit !important;
}

/* === CENTERED LAYOUTS === */
.slidev-layout.cover,
.slidev-layout.section,
.slidev-layout.fact,
.slidev-layout.end,
.slidev-layout.statement,
.slidev-layout.center {
  text-align: center;
}
.slidev-layout.cover h1, .slidev-layout.cover p, .slidev-layout.cover div,
.slidev-layout.section h1, .slidev-layout.section p, .slidev-layout.section div,
.slidev-layout.fact h1, .slidev-layout.fact p, .slidev-layout.fact div,
.slidev-layout.end h1, .slidev-layout.end p, .slidev-layout.end div,
.slidev-layout.statement h1, .slidev-layout.statement p,
.slidev-layout.center h1, .slidev-layout.center p {
  text-align: center;
}

/* === SHAPE VOCABULARY === */
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
.icon-rounded {
  width: 52px;
  height: 52px;
  border-radius: 14px;
  background: var(--color-accent-bg);
  border: 1.5px solid var(--color-accent-dim);
  display: flex;
  align-items: center;
  justify-content: center;
}
.icon-ghost {
  width: 52px;
  height: 52px;
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

/* === CARD STYLES === */
.card-solid {
  background: var(--bg-base);
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
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(var(--accent-rgb), 0.12);
  border-radius: 14px;
  padding: 24px;
}
```
