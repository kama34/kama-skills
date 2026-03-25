# Critique: Ремесло (Learn Iteration 2)

## Overall Score: 7.2/10

Major rendering breakthrough — all 8 content slides render correctly. Rule 45 (inline style whitelist) completely solved the raw HTML failure. Only 1 ghost slide remains from global headmatter (Rule 46 fix applied).

## Systemic Issues (affect the skill itself)

### Issue 1: Ghost slide from global headmatter structure
- **Severity**: major
- **Category**: rendering
- **Frequency**: 1/1 presentations
- **Description**: Slide 1 is blank. The global frontmatter creates slide 1 with no content because the first slide's HTML comes after an extra `---` separator.
- **Evidence**: slides/1.png is blank cream
- **Root cause**: Rule 46 was incorrectly worded in iteration 1. Now corrected to explain that slide 1 content must follow immediately after global frontmatter.
- **Proposed skill fix**: Already applied — Rule 46 rewritten to clarify correct pattern.

### Issue 2: Decorative elements too subtle on light background
- **Severity**: minor
- **Category**: decoration
- **Frequency**: 5/8 slides
- **Description**: Decorative glows and arcs are barely visible on cream background. Only the dot grid on cover is clearly visible. Content slide decorations (radial glows) blend into bg-base.
- **Evidence**: Slides 3, 5, 6 — decorative elements not clearly visible in PNG
- **Root cause**: Glow opacity 0.18 is insufficient on light backgrounds. Need 0.25+ minimum.
- **Proposed skill fix**: Increase minimum glow opacity from 0.18 to 0.25 for light themes in design-principles.md

### Issue 3: bg-alt and bg-base visually too similar
- **Severity**: minor
- **Category**: rhythm
- **Frequency**: across deck
- **Description**: #FAF9F6 (bg-base) and #F0EDE8 (bg-alt) are only ~4 luminance points apart. The alternation is barely perceptible in exported PNGs. Section transitions don't create visual breathing.
- **Evidence**: Comparing slides 3→5, 4→6 — backgrounds almost identical
- **Root cause**: Preset bg-alt is too close to bg-base in luminance
- **Proposed skill fix**: Add rule: for light themes, bg-base/bg-alt luminance delta must be ≥8 points. Darken bg-alt to #E8E4DE.

## Slide-Specific Issues

### Slide 5 (icon-trio): Icon containers all same style
- Description: All 3 icons use rounded-square (icon-rounded) containers — no variety within the slide
- Severity: minor — the variety is across slides (circle vs rounded-square), acceptable per preset rule

## What Worked Well
1. **Rule 45 completely solved rendering** — zero raw HTML leakage, all 8 slides render
2. **Typography drama**: hero numbers (89, 265, 72, 2 млрд) are dramatic and arresting at 4-5rem
3. **Layout diversity**: 6 different archetypes across 8 slides — no repetition
4. **Warm amber accent**: visible on slides 3 (68%), 6 (8%→3.5% trend), 7 (Day 3 card) — temperature contrast works
5. **Cover slide**: teal + white + dot grid is the strongest slide — professional, distinctive
6. **CTA slide**: teal background, clear ask (250 млн ₽), investment allocation pills — clean
7. **Bento-grid**: "2 млрд ₽" featured with side cards — well-composed hierarchy
8. **Timeline**: Day 1→2→3 progression with warm accent on Day 3 — effective storytelling

## Design Summary
- **Palette type**: light
- **Palette mood**: warm cream with teal conviction, amber warmth
- **Font character**: geometric-sans (Sora heading) + corporate-humanist (IBM Plex body)
- **Decoration style**: minimal (glows and arcs, barely visible on light bg)
- **Strongest axis**: content clarity + layout diversity
- **Weakest axis**: decorative quality (too subtle on light background)
