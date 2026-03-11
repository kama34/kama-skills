# Slidev Animations & Transitions

## Click Animations

### v-click

Reveal elements one click at a time:

```markdown
<v-click>

- First item (appears on click 1)

</v-click>

<v-click>

- Second item (appears on click 2)

</v-click>
```

### v-clicks

Auto-apply `v-click` to all direct children:

```markdown
<v-clicks>

- Item 1 (click 1)
- Item 2 (click 2)
- Item 3 (click 3)

</v-clicks>
```

### v-after

Appear at the same click as the previous `v-click`:

```markdown
<v-click>

Main content

</v-click>
<v-after>

Appears simultaneously with the above

</v-after>
```

### Click Ranges

```markdown
<v-click at="3">

Appears at click 3

</v-click>

<v-clicks at="2">

- Starts appearing from click 2

</v-clicks>
```

### Hide on Click

```markdown
<v-click hide>

Visible initially, hidden on click

</v-click>
```

## Slide Transitions

### Global Transition (Headmatter)

```yaml
---
transition: slide-left
---
```

### Per-Slide Transition

```yaml
---
transition: fade
---
```

### Available Transitions

| Transition | Effect |
|-----------|--------|
| `fade` | Fade in/out |
| `fade-out` | Fade out only |
| `slide-left` | Slide from right to left |
| `slide-right` | Slide from left to right |
| `slide-up` | Slide from bottom to top |
| `slide-down` | Slide from top to bottom |
| `view-transition` | Browser View Transitions API |
| `none` | No transition |

### Custom Transition

```yaml
---
transition: my-transition
---
```

Define in `styles/index.css`:

```css
.my-transition-enter-active,
.my-transition-leave-active {
  transition: all 0.5s ease;
}

.my-transition-enter-from {
  opacity: 0;
  transform: translateX(100px);
}

.my-transition-leave-to {
  opacity: 0;
  transform: translateX(-100px);
}
```

## CSS Animation Patterns

### Slide-Scoped Animations

```markdown
---
---

# Animated Slide

<div class="animated-element">
  Content
</div>

<style>
.animated-element {
  animation: slideIn 0.8s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
```

### UnoCSS Animation Utilities

```markdown
<div class="animate-fade-in animate-duration-500">
  Fades in
</div>

<div class="animate-bounce-in">
  Bounces in
</div>
```

### Motion Preferences

Always respect `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Best Practices

1. Use `v-clicks` for bullet lists — keeps audience focused
2. Use step highlighting `{1|2-3|5}` for code walkthroughs
3. Match transition style to presentation mood (e.g., `fade` for calm, `slide-left` for dynamic)
4. Don't overuse animations — one effect per slide maximum
5. Keep transition duration under 500ms for professional feel
