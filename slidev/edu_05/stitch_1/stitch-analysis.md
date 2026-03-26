# Stitch HTML Analysis — Cycle 1: PayBridge FinTech

## Design Decisions Stitch Made

### Fonts
- **Heading**: Manrope (400, 600, 700, 800)
- **Body**: Inter (400, 500)
- **Label**: Space Grotesk (400, 500, 700)
- **Note**: Uses 3 font families (vs our 2-font rule)

### Color Palette
- Background: #0e0e0f (near-black)
- Primary: #a3a6ff (lavender/periwinkle — AI BLACKLIST hue ~238!)
- Secondary: #69f6b8 (mint green)
- Tertiary: #ff8ed2 (pink)
- Error: #ff6e84 (coral)
- Surface levels: #000000, #0e0e0f, #131314, #1a191b, #201f21, #262627, #2c2c2d
- Text: #ffffff (main), #adaaab (muted)
- Outline: #767576, border-variant: #484849

### Grid System
- 12-column base grid: `grid-template-columns: repeat(12, 1fr)`
- Flexible column spans: 7/5, 4/8, 5/7, 2/3

### Slide Layouts
| Slide | Layout Pattern | Grid Ratio |
|-------|---------------|------------|
| 1 Cover | Centered hero + bg image | — |
| 2 Market | Asymmetric bento 7/5 | Hero left, 2 cards right |
| 3 Pain | Equal 2-col | Text+quote left, solution card right |
| 4 Solution | Heading + 3-col cards | 3 equal |
| 5 Traction | Asymmetric 4/8 | Hero stat left, 3 cards right |
| 6 Tech | Asymmetric 2/3 | Text left, dashboard mockup right |
| 7 Scale | Centered hero | Massive 12rem + 4-stat row |
| 8 Business | Bento 5/7 | Text left, metric card right |
| 9 Team | 3-col cards | Photo + bio |
| 10 CTA | 2-col | Contact left, donut chart right |

### Typography Sizes (observed)
- Cover title: text-8xl (6rem)
- Hero number slide 2: text-[10rem]
- Hero number slide 7: text-[12rem] (biggest!)
- Section headings: text-5xl to text-7xl
- Body: text-lg to text-2xl
- Labels: text-xs, uppercase, tracking-widest
- Tiny: text-[8px], text-[10px] (below our min!)

### Decoration
- Minimal — relies on surface depth, not gradient/blob decoration
- Accent lines under headings (h-1.5 w-32 bg-primary)
- Card border-top accents (border-t-2 border-primary)
- Quote border-left-4
- Glass panel effect on nav
- Dashboard mockup wireframe on slide 6
- SVG donut chart on CTA

### Card Styles
1. `bg-surface-container` — default surface card
2. `bg-surface-container-low border border-outline-variant/20` — subtle bordered
3. `bg-surface-container-high border-t-2 border-primary shadow-2xl` — accent top stripe
4. `bg-surface-container-low border border-primary/10 rounded-3xl` — large metric card

### Notable Patterns
- Fixed sidebar navigation with icons (web-app pattern, not presentation)
- Top navigation bar (unnecessary for slides)
- Footer (web-app artifact)
- Team photos with grayscale→color hover
- Material Symbols icons used naturally
- Background image on cover with opacity-20 overlay

## Strengths (what Stitch does better)
1. **12-column grid flexibility** — truly asymmetric ratios (7/5, 4/8, 2/3)
2. **Hero number boldness** — 10rem and 12rem for key stats
3. **Dashboard mockup detail** — routing engine UI with status bars, gateways
4. **Surface depth system** — 5+ levels for subtle slide differentiation
5. **Card accent patterns** — border-top colored strips
6. **SVG donut chart** — clean implementation with center label
7. **Quote callout design** — border-left + italic + attribution
8. **Team photos** — grayscale-to-color interactive effect

## Weaknesses (what we do better)
1. Primary #a3a6ff is in AI color blacklist (purple family)
2. 3 fonts violates 2-font discipline
3. Text sizes text-[8px], text-[10px] violate our minimums
4. Pure white (#fff) and near-black (#0e0e0f) — no warm tinting
5. No decorative background layers — slides feel flat
6. No ghost typography effects
7. Nav/sidebar/footer are web-app patterns, not slide patterns
8. No shape vocabulary variety — all rectangular cards
