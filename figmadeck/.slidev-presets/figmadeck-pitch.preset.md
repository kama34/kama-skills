---
name: figmadeck-pitch
figma:
  fileKey: "6iJhgnLC8oiDd4r6Tyqtl2"
  sourceUrl: "https://www.figma.com/design/6iJhgnLC8oiDd4r6Tyqtl2/pitch?node-id=0-1"
  extractedAt: "2026-03-31T12:00:00Z"
  slideCount: 14
  archetypes:
    - id: figmadeck-pitch-cover
      nodeId: "1:32"
      contentType: intro
    - id: figmadeck-pitch-agenda-numbers
      nodeId: "1:49"
      contentType: scope
    - id: figmadeck-pitch-team
      nodeId: "1:63"
      contentType: team
    - id: figmadeck-pitch-agenda-shapes
      nodeId: "1:84"
      contentType: scope
    - id: figmadeck-pitch-vision-light
      nodeId: "1:102"
      contentType: vision
    - id: figmadeck-pitch-vision-dark
      nodeId: "1:119"
      contentType: vision
    - id: figmadeck-pitch-list
      nodeId: "1:124"
      contentType: process
    - id: figmadeck-pitch-cards4
      nodeId: "1:141"
      contentType: scope
    - id: figmadeck-pitch-process
      nodeId: "1:165"
      contentType: process
    - id: figmadeck-pitch-visual
      nodeId: "1:202"
      contentType: visual-break
    - id: figmadeck-pitch-clients-gallery
      nodeId: "1:204"
      contentType: credentials
    - id: figmadeck-pitch-clients-logos
      nodeId: "1:214"
      contentType: credentials
    - id: figmadeck-pitch-cta
      nodeId: "1:225"
      contentType: cta
    - id: figmadeck-pitch-vision-light
      nodeId: "1:185"
      contentType: vision
      duplicateOf: figmadeck-pitch-vision-light
fonts:
  sans: Staatliches
  body: Archivo
theme: ./figmadeck-pitch-theme
colorSchema: light
accentColor: "#ff6a3b"
---

Vibrant brutalist editorial pitch deck. Warm beige (#ded8cb) and pure black backgrounds. Eclectic font system: Staatliches (condensed display) + BioRhyme Expanded (section headings) + Archivo (body) + Work Sans (meta). Bold four-color accent palette (orange, teal, blue, gold, magenta). Signature notebook spiral-binder card motif on cover/vision slides. Stardos Stencil decorative hero numerals. Heavy uppercase typography with wide letter-spacing. Colored tall card columns for principles/scope slides.

```archetypes
preferred: [figmadeck-pitch-cover, figmadeck-pitch-agenda-numbers, figmadeck-pitch-team, figmadeck-pitch-agenda-shapes, figmadeck-pitch-vision-light, figmadeck-pitch-vision-dark, figmadeck-pitch-list, figmadeck-pitch-cards4, figmadeck-pitch-process, figmadeck-pitch-visual, figmadeck-pitch-clients-gallery, figmadeck-pitch-clients-logos, figmadeck-pitch-cta]
avoid: []
cta_style: figmadeck-pitch-cta
cover_style: figmadeck-pitch-cover
```

```css
:root {
  --bg-base: #ded8cb;
  --bg-alt: #000000;
  --color-text: #000000;
  --color-muted: #ded8cb;
  --color-accent: #ff6a3b;
  --color-accent-rgb: 255, 106, 59;
  --bg-accent: rgba(255, 106, 59, 0.12);
  --color-text-on-dark: #ded8cb;
  --color-teal: #15857a;
  --color-blue: #4076ba;
  --color-gold: #a97c50;
  --color-pink: #c04277;
  --font-display: 'Stardos Stencil', sans-serif;
  --font-heading: 'Staatliches', sans-serif;
  --font-section: 'BioRhyme Expanded', sans-serif;
  --font-body: 'Archivo', sans-serif;
  --font-meta: 'Work Sans', sans-serif;
  --gap: 1.5rem;
  --pad: 2rem;
  --card-radius: 1.25rem;
  --card-radius-xl: 3.125rem;
  --slidev-font-sans: 'Archivo', sans-serif;
  --slidev-font-mono: 'Fira Code', monospace;
  --slidev-theme-primary: #ff6a3b;
}
```
