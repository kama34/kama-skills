# Text Overlay Rules

Rules for positioning HTML/CSS text over AI-generated background images in Slidev.

## Core Architecture

Every slide uses `layout: none` to bypass all Slidev theme CSS. The slide consists of two layers:

1. **Background layer** (z-index: 0) — AI-generated PNG as `background-image`
2. **Text layer** (z-index: 1) — HTML elements with CSS `position: absolute`

## Slide Container Pattern

```html
<div class="slide-container">
  <div class="slide-bg slide-NN"></div>
  <div class="zone zone-heading" style="left:X%;top:Y%;width:W%;height:H%;">
    <h1>Heading text</h1>
  </div>
  <div class="zone zone-bullets" style="left:X%;top:Y%;width:W%;height:H%;">
    <v-clicks>

    - Item one
    - Item two

    </v-clicks>
  </div>
</div>
```

## Required CSS Classes

```css
.slide-container {
  position: absolute;
  inset: 0;
}

.slide-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  z-index: 0;
}

.zone {
  position: absolute;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
```

## Why layout: none is MANDATORY

Slidev's built-in layouts (`cover`, `default`, `section`, etc.) apply high-specificity CSS that:
- Overrides `text-align` with theme defaults
- Applies padding and margins that conflict with absolute positioning
- Sets `background-color` that blocks the AI background image
- Changes font sizes on `statement` and `fact` layouts

`layout: none` bypasses ALL of this, giving full CSS control.

## Background Image via CSS (NOT frontmatter)

**CRITICAL:** Use CSS `background-image`, NOT Slidev's frontmatter `background:` property.

```css
/* CORRECT — CSS background */
.slide-03 { background-image: url('./slides/slide-03.png'); }

/* WRONG — frontmatter background is blocked by theme */
/* background: ./slides/slide-03.png */
```

The frontmatter `background:` renders on a parent element that the theme's opaque `background-color` covers.

## v-clicks Compatibility

`<v-clicks>` works inside zone divs when wrapping markdown content:

```html
<div class="zone zone-bullets" style="left:5%;top:32%;width:55%;height:50%;">
  <v-clicks>

  - Item one
  - Item two
  - Item three

  </v-clicks>
</div>
```

**Rules:**
- `<v-clicks>` only works on top-level markdown content
- Blank line required after `<v-clicks>` and before `</v-clicks>`
- Does NOT work inside nested HTML `<div>` structures
- For custom HTML layouts, use static presentation instead

## CSS Card Containers (NOT AI-drawn)

**CRITICAL RULE:** If the design calls for panels, cards, or containers around text, they MUST be created in the CSS layer — NEVER drawn by the AI in the image. This is because AI coordinates are approximate while CSS coordinates are exact, so AI-drawn borders and CSS-positioned text will always misalign.

Three card styles are available as CSS classes on `.zone` divs:

```html
<!-- Glass card — subtle frosted glass effect -->
<div class="zone zone-card" style="left:5%;top:8%;width:55%;height:80%;">
  <h1>Heading perfectly aligned with card border</h1>
  <p>Content inside a glass card</p>
</div>

<!-- Solid dark card — semi-transparent dark overlay -->
<div class="zone zone-card-solid" style="left:5%;top:8%;width:55%;height:80%;">
  <h1>Heading</h1>
</div>

<!-- Accent card — gradient with accent color border -->
<div class="zone zone-card-accent" style="left:40%;top:20%;width:55%;height:60%;">
  <h1>Highlighted content</h1>
</div>
```

**CSS definitions (in `styles/index.css`):**

```css
.zone-card {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 24px 28px;
  backdrop-filter: blur(8px);
}
.zone-card-solid {
  background: rgba(0, 0, 30, 0.55);
  border-radius: 12px;
  padding: 24px 28px;
}
.zone-card-accent {
  background: linear-gradient(135deg, var(--color-accent-bg), rgba(0,0,0,0.3));
  border: 1px solid var(--color-accent-dim);
  border-radius: 12px;
  padding: 24px 28px;
}
```

**Why CSS cards instead of AI cards:**
- Card border and text are the SAME DOM element → always perfectly aligned
- Cards adapt to actual text length (CSS flexbox)
- Easy to change card style without regenerating AI images
- Consistent border-radius, padding, and blur across all slides

## Text Contrast Guarantee

The AI image generation prompt requires uniform backgrounds in text zones. Text color is chosen to contrast:

| Zone background | Text color | Fallback if mismatch |
|----------------|------------|---------------------|
| Dark (planned) | `white` or `rgba(255,255,255,0.9)` | Add `text-shadow: 0 1px 3px rgba(0,0,0,0.5)` |
| Light (planned) | `#1a1a2e` or `rgba(0,0,0,0.85)` | Add `text-shadow: 0 1px 3px rgba(255,255,255,0.5)` |

**Background mismatch remediation:** If Phase 1 QA finds that zone background differs from planned:
1. Update text color in `layout-plan.json` to match actual background
2. Regenerate CSS for affected zones
3. If background is inconsistent (gradient/pattern in zone), add a semi-transparent backdrop:

```css
.zone-heading-fallback {
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(4px);
  border-radius: 8px;
  padding: 12px 16px;
}
```

## Font Rendering

Fonts are loaded via Google Fonts in Slidev headmatter:

```yaml
fonts:
  sans: Outfit
  serif: Source Serif 4
```

The browser renders text at native resolution — always crisp, no aliasing artifacts from image generation.

**Forbidden fonts:** Inter, Roboto, Arial, Open Sans, Lato, Space Grotesk (too generic).

**Recommended pairs:** Outfit + Source Serif 4, Syne + Literata, Cabinet Grotesk + Newsreader, Plus Jakarta Sans + Fraunces, Bricolage Grotesque + Lora.

## HTML Nesting Limit

Maximum 3 levels of HTML nesting inside zone divs. Deeper nesting causes Slidev to output raw HTML source instead of rendered content. Flatten with CSS Grid/Flexbox on a single wrapper.

## z-index Stacking (with --picture)

When `--picture` adds photos, the stacking order changes:

| Layer | z-index | Content |
|-------|---------|---------|
| AI background | 0 | Generated PNG |
| Photo layer | 1 | Additional photos from Brave search |
| Text zones | 2 | HTML text overlay |

When photos are present, update zone CSS to `z-index: 2`.
