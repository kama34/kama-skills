# Slidev Layouts Reference

## Built-in Layouts

| Layout | When to Use | Key Props / Slots |
|--------|------------|-------------------|
| `default` | Standard content slides with text, lists, images | — |
| `cover` | Opening slide with title and subtitle | `background` |
| `center` | Centered content, statements, single ideas | — |
| `two-cols` | Side-by-side comparison or content | `::left::`, `::right::` slots |
| `image-left` | Image on left, content on right | `image: '/path.jpg'` |
| `image-right` | Image on right, content on left | `image: '/path.jpg'` |
| `image` | Full-bleed background image with overlay text | `image: '/path.jpg'` |
| `section` | Section divider between major topics | — |
| `statement` | Bold single statement or quote | — |
| `fact` | Highlight a key metric or statistic | — |
| `quote` | Attributed quotation | — |
| `end` | Closing/thank-you slide | — |
| `intro` | Speaker introduction with photo | `image: '/photo.jpg'` |
| `iframe` | Embed an iframe | `url: 'https://...'` |
| `full` | Full-page content without padding | — |
| `none` | Completely blank canvas | — |

## Layout Selection Guide

### By Content Type

- **Title / opening** → `cover`
- **Section break** → `section`
- **Bullet points** → `default`
- **Single statement / takeaway** → `statement` or `center`
- **Statistic / number** → `fact`
- **Quote** → `quote`
- **Code walkthrough** → `default` (with code block)
- **Comparison** → `two-cols`
- **Image showcase** → `image`, `image-left`, or `image-right`
- **Closing** → `end`

### Named Slots

Some layouts support named slots to place content in specific regions:

```markdown
---
layout: two-cols
---

# Left Side

Content for the left column

::right::

# Right Side

Content for the right column
```

Available slot syntax:
```
::slotname::
```

Common slots by layout:
- `two-cols`: `::right::` (default content goes left)
- `image-left` / `image-right`: `::default::` for the text side
- Custom layouts may define: `::header::`, `::footer::`, `::left::`, `::right::`

## Custom Layouts

Create custom layouts in `layouts/` directory:

```
layouts/
  my-layout.vue
```

```vue
<!-- layouts/my-layout.vue -->
<template>
  <div class="slidev-layout my-layout">
    <slot name="header" />
    <div class="content">
      <slot />
    </div>
    <slot name="footer" />
  </div>
</template>
```

Use in slides:

```markdown
---
layout: my-layout
---

::header::
# Header Content

Main content here

::footer::
Footer text
```

## Layout + Background Combination

```markdown
---
layout: cover
background: /images/hero.jpg
class: text-white
---

# Title over image
```

The `background` prop works with any layout but is most commonly used with `cover`, `section`, and `end`.
