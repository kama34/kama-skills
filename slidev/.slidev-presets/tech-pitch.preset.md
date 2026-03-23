---
name: tech-pitch
theme: default
colorSchema: light
fonts:
  sans: Plus Jakarta Sans
  body: Nunito
  mono: JetBrains Mono
aspectRatio: 16/9
transition: fade
accentColor: "#0D9488"
iconStyle: outlined
densityProfile: balanced
maxFonts: 2
---

Confident, modern tech startup aesthetic. Warm cream base with strong teal accent — communicates trust, innovation, and growth. Clean editorial feel with generous whitespace. Typography-driven: bold geometric headings in Plus Jakarta Sans, friendly rounded body in Nunito for narrative credibility. Backgrounds use subtle warm tints with soft geometric decorative touches (corner arcs, gradient orbs). Data-forward — numbers are heroes, not decorations. Professional enough for investors, distinctive enough to remember.

Follows the `editorial` trend with tech-forward energy. Light cream backgrounds create openness; teal accent at varying intensities (full for CTAs, 40% for borders, 10% for card fills) builds visual hierarchy. No purple, no gradients-for-gradients-sake. Every element serves communication.

**Composition diversity rule (CRITICAL)**: No archetype may appear more than twice per deck. Consecutive slides may not share the same archetype. The sequence MUST include at least one slide where content anchors to the right half, one slide where the heading is de-emphasized (small, muted), and one slide with a typographic hero (single number or phrase at 6rem+) as the primary visual element.

**CRITICAL icon-trio enforcement**: Within a single deck, the icon-trio archetype MUST use different structural forms for each occurrence. If the deck contains two icon-trio slides, they MUST use different lettered forms: first occurrence uses form (b) large-icon-left + stacked-list-right or form (c) 2-column with one featured card spanning full height; second may use form (a) 3-equal-column row. Form (a) is the LOWEST PRIORITY form and should only appear if it is the only occurrence in the deck.

**Decorative element rule (CRITICAL)**: At least 40% of slides MUST include a VISIBLE decorative element. Orb opacity on cream background must be ≥0.18. Arc border opacity on cream must be ≥0.25. On teal backgrounds, use white-tinted variants (rgba(255,255,255,0.10) for orbs, rgba(255,255,255,0.18) for arcs). A decorative element that cannot be seen at arm's length does not count toward the 40% requirement. Use inline `<div style="position:absolute;top:-80px;right:-80px;width:350px;height:350px;border-radius:50%;background:radial-gradient(circle,rgba(13,148,136,0.18) 0%,transparent 65%);pointer-events:none;z-index:0;"></div>` for orbs. Use `<div style="position:absolute;bottom:20px;right:20px;width:200px;height:200px;border:2px solid rgba(13,148,136,0.25);border-radius:50%;pointer-events:none;z-index:0;"></div>` for arcs.

**Cover variety rule**: Each deck MUST use one of three cover sub-forms: (a) cover-centered — logotype+tagline centered, arc bottom-left; (b) cover-left — logotype large left-aligned, tagline below-left, decorative arc right side; (c) cover-split — left 55% with content left-aligned, right 45% with large decorative orb and arc. Never use the same sub-form in consecutive generated decks.

**Market slide variation**: The TAM/SAM/SOM slide MUST NOT use a plain stacked list. Choose one of: (a) three horizontal bars with proportional widths showing scale, (b) TAM as a `.stat-hero` with SAM/SOM as indented subordinate text, (c) a visual funnel with three labeled sections.

**Team slide rule**: Team slides MUST use `.photo-circle` containers (60–80px) with initials in a `--bg-accent` circle instead of generic icon containers. Name at 1.4rem bold. Role at 0.9rem muted. Previous company as a `.label-pill`. This distinguishes team slides from product/feature slides visually.

**Stat number rule**: Stat numbers MUST use `.stat-hero` class. Unit labels (млн, %, тыс) MUST be wrapped in `<span class="suffix">` to subordinate them visually. Hero numbers must be dramatically larger than surrounding text — minimum 2:1 ratio vs heading size.

**Table layout rule**: Financial tables must be accompanied by a supporting annotation or stat callout below the table to fill remaining vertical space. Tables should use full-width layout with min-row-height of 4rem.

**Vertical fill rule (CRITICAL)**: Content slides must occupy ≥70% of the slide height with visible content or structural elements. If a card grid or table does not reach 65% height, add: expanded card padding (2rem 1.5rem minimum), a secondary annotation row, or a stat-callout below. Never leave more than 30% blank cream below the last content element. Use `flex:1` on content containers and `justify-content:center` or `align-items:stretch` to distribute content vertically.

**Financial slide heading rule**: The financial slide heading must be derived from the company's primary metric goal, not a generic phrase. Format: "[Primary metric] [value] к [year]" — e.g., "ARR 240 млн ₽ к 2027 году". The phrase "Выход на прибыльность" is BANNED as a financial slide heading.

**Investment slide variation**: Investment slides MUST vary layout. Options: (a) allocation-left + stat-right, (b) stat-left + allocation-right (mirror), (c) full-width allocation bars with ₽ amounts, (d) bento-grid 2×2 with [total], [equity%], [use-1], [use-2] as cards.

**Traction slide rule**: Traction slides MUST include at least one of: (a) a trend annotation beside each metric ("×2 за квартал"), (b) a secondary contextual sentence below the card row, (c) a fourth highlight metric card spanning full width below the 3-card row. Bare number cards with no context are insufficient.

```archetypes
preferred: [stat-hero, icon-trio, timeline-horizontal, asymmetric-split, bento-grid]
avoid: [timeline-zigzag]
cta_style: cta-warm
cover_style: cover-hero
```

```shapes
card_radius: 14px
icon_container: circle
stat_display: typographic
label_style: pill
divider_style: gradient-fade
photo_mask: circle
```

```css
:root {
  --slidev-theme-primary: #0D9488;
  --slidev-theme-background: #FAF9F6;
  --slidev-theme-code-background: #F0EFEC;

  --color-bg: #FAF9F6;
  --color-text: #1C1917;
  --color-accent: #0D9488;
  --color-accent-dim: rgba(13, 148, 136, 0.45);
  --color-accent-bg: rgba(13, 148, 136, 0.10);
  --color-surface: #F0EFEC;
  --color-surface-border: #E2E0DC;
  --color-muted: #6B7280;
  --accent-rgb: 13, 148, 136;

  --bg-base: #FAF9F6;    /* 60% — warm cream content */
  --bg-alt: #F0EFEC;     /* 30% — warm stone sections */
  --bg-accent: #0F766E;  /* 10% — deep teal cover/CTA */

  --font-heading: 'Plus Jakarta Sans', sans-serif;
  --font-body: 'Nunito', sans-serif;

  /* Contrast ratios:
     --color-muted (#6B7280) vs --bg-base (#FAF9F6): 4.8:1 ✓
     --color-muted (#6B7280) vs --bg-alt (#F0EFEC): 4.5:1 ✓
     --color-muted (#6B7280) vs --bg-accent (#0F766E): 2.8:1 — use white text on accent
     --color-text (#1C1917) vs --bg-base (#FAF9F6): 15.2:1 ✓
     --color-text (#1C1917) vs --bg-alt (#F0EFEC): 14.1:1 ✓
  */

  /* Decorative gradient type: radial-gradient */
}

/* Base layout */
.slidev-layout {
  background-color: var(--bg-base);
  color: var(--color-text);
  font-family: var(--font-body);
}

.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3 {
  color: var(--color-text);
  font-family: var(--font-heading);
  letter-spacing: -0.02em;
  line-height: 1.1;
}

.slidev-layout p,
.slidev-layout li {
  color: var(--color-text);
  line-height: 1.45;
  font-size: 1.25rem;
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

/* Cover layout — full-bleed teal */
.slidev-layout.cover {
  text-align: center;
  background-color: var(--bg-accent) !important;
  color: #FFFFFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100%;
  padding: 3rem;
}
.slidev-layout.cover h1,
.slidev-layout.cover p { text-align: center; color: #FFFFFF; }
.slidev-layout.cover::before { display: none; }

/* Section layout */
.slidev-layout.section { text-align: center; }
.slidev-layout.section h1,
.slidev-layout.section p { text-align: center; }

/* Fact layout */
.slidev-layout.fact { text-align: center; }
.slidev-layout.fact h1,
.slidev-layout.fact p { text-align: center; }

/* End layout — full-bleed teal */
.slidev-layout.end {
  text-align: center;
  background: var(--bg-accent) !important;
  background-color: var(--bg-accent) !important;
  color: #FFFFFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100%;
  padding: 3rem;
}
.slidev-layout.end h1,
.slidev-layout.end p,
.slidev-layout.end div { text-align: center; color: #FFFFFF; }

/* Statement / Center */
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

/* === SHAPE VOCABULARY === */

/* Circle icon container */
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

/* Typographic stat hero */
.stat-hero {
  font-size: clamp(4rem, 8vw, 7rem);
  font-weight: 800;
  color: var(--color-accent);
  line-height: 0.95;
  font-family: var(--font-heading);
  letter-spacing: -0.03em;
}
.stat-hero .unit {
  font-size: 0.4em;
  font-weight: 600;
  vertical-align: super;
  letter-spacing: 0;
}
.stat-hero .suffix {
  font-size: 0.35em;
  font-weight: 500;
  color: var(--color-muted);
  margin-left: 0.15em;
}

/* Pill label */
.label-pill {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: max-content;
  max-width: 220px;
  line-height: 1;
  background: var(--bg-base);
  border: 1.5px solid var(--color-accent-dim);
  border-radius: 20px;
  padding: 6px 18px;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--color-accent);
  font-weight: 600;
}

/* Photo circle mask */
.photo-circle { border-radius: 50%; overflow: hidden; }

/* === CARD VARIANTS === */

.card-solid {
  background: var(--color-surface);
  border: 1px solid var(--color-surface-border);
  border-radius: 14px;
}

.card-ghost {
  background: transparent;
  border: 1.5px solid var(--color-accent-dim);
  border-radius: 14px;
}

.card-accent {
  background: linear-gradient(135deg, var(--color-accent-bg), var(--color-surface));
  border: 1.5px solid var(--color-accent-dim);
  border-radius: 14px;
}

/* === TABLE STYLES === */

.slidev-layout table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}
.slidev-layout table tr {
  height: 4rem;
}
.slidev-layout table td,
.slidev-layout table th {
  padding: 1rem 1.25rem;
  border-bottom: 1px solid var(--color-surface-border);
  font-size: 1.1rem;
}
.slidev-layout table thead th {
  background: var(--color-accent);
  color: #FFFFFF;
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

/* === DECORATIVE === */

/* Decorative gradient type: radial-gradient */
.decor-orb::before {
  content: '';
  position: absolute;
  width: 350px;
  height: 350px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(13, 148, 136, 0.18) 0%, transparent 65%);
  pointer-events: none;
  z-index: 0;
}

.decor-arc::after {
  content: '';
  position: absolute;
  width: 200px;
  height: 200px;
  border: 2px solid rgba(13, 148, 136, 0.25);
  border-radius: 50%;
  pointer-events: none;
  z-index: 0;
}

@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
