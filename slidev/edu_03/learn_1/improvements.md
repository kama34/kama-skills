# Improvements from Learn Iteration 1

## Applied Changes (critical + major systemic issues only)

### Change 1: Remove layout:none from global headmatter
- **File**: SKILL.md
- **Section**: Step 5: Write slides.md — headmatter
- **Type**: modify_rule
- **Description**: Global frontmatter must NOT contain `layout: none`. Only per-slide frontmatter should set layout. Having `layout: none` in global causes a blank first slide.
- **Before**: Rule 25 says "Global frontmatter must contain `layout: none`"
- **After**: Global frontmatter must NOT contain `layout: none`. Each per-slide frontmatter sets `layout: none` individually.

### Change 2: Mandate CSS classes over inline styles for complex layouts
- **File**: SKILL.md
- **Section**: Step 5: Write slides.md — new rule after Rule 23
- **Type**: add_rule
- **Description**: Slidev's markdown parser fails to render HTML blocks that contain deeply nested inline `style="..."` attributes with CSS variable references like `var(--color-accent)`. The parser treats these as text nodes instead of DOM elements. The fix: ALL visual styling must go into per-slide `<style>` blocks using CSS class selectors. Inline styles are ONLY permitted for `position`, `inset`, `z-index`, `display`, `flex-direction`, `gap`, `padding`, `margin`, `width`, `height`, `grid-template-*` — structural layout properties. Colors, fonts, backgrounds, borders, border-radius, opacity MUST use CSS classes in `<style>` blocks.
- **Before**: N/A (no explicit rule about inline style limitations)
- **After**: New Rule 45: "Inline style property whitelist"

### Change 3: Add mandatory post-export render check
- **File**: SKILL.md
- **Section**: Visual QA Loop — Phase 2
- **Type**: add_rule
- **Description**: After exporting PNGs, check slide 1 is NOT blank and no slide shows raw HTML text. If either condition is true, the rendering pipeline has failed — fix and re-export before proceeding.
- **Before**: QA-2 just exports PNGs
- **After**: QA-2 exports PNGs + mandatory render verification

## Deferred (minor issues — logged for review)
- Structural monotony (LABEL → H1 → content pattern too uniform) — addressed by existing structural break rules
- ABABAB background checkerboard — addressed by existing bg-level distribution rules
