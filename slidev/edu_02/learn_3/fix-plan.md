# План исправлений — Итерация 3

## Проблема 1: Structural clones (slides 5/6) — adjacent slides identical layout
### Корневая причина: Composition plan assigns different archetype names but they render identically (both asymmetric grids)
### Решение: Add visual structure fingerprint check — after assigning archetypes, verify adjacent slides differ in RENDERED structure

## Проблема 2: Section divider visually empty on bg-accent
### Корневая причина: White text + faint glow on solid teal = no visual weight, section feels like "pause slide"
### Решение: Section dividers on bg-accent MUST include prominent decorative element

## Проблема 3: Mechanical icon shape rotation
### Корневая причина: circle→rounded→ghost applied identically = still predictable
### Решение: Vary by semantic purpose, not by position order

## Проблема 4: Decorative motifs invisible on bg-alt
### Корневая причина: bg-alt (#E8E6DF) is warm grey, teal decoratives at 0.50 blend in
### Решение: On bg-alt, increase decorative opacity to 0.65+ or use contrasting color
