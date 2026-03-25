# План исправлений — Итерация 7

## Проблема 1: bento-grid featured card — stat number too small
### Корневая причина (5 Why)
1. 72% выглядит маленьким в большой featured-карточке
2. Потому что icon+number расположены side-by-side, делая number меньше
3. Потому что архетип bento-grid не задаёт минимальный размер числа в featured-ячейке
4. Потому что правило ≥4rem hero number в SKILL.md применяется к full stat-hero слайдам, но не расширено на featured cells
5. Корень: нет правила "featured cell in bento-grid = mini stat-hero with ≥3.5rem number"

### Источник решения
- references/design-principles.md Principle 3 (Typography Drama): hero numbers must be oversized
- Rule 23 (Hero metric prominence): one card MUST be visually promoted

### Варианты
A) Add rule to bento-grid archetype description: featured cell primary metric ≥3.5rem, icon above not beside
B) Add to SKILL.md Step 5 bento-grid writing: do not put icon beside the featured metric

### Выбранный вариант: A — add directly to composition-archetypes.md bento-grid entry
- Rationale: spec close to where it's used; applies at composition time, not just write-time

### Конкретные правки
- Файл: .claude/skills/slidev/references/composition-archetypes.md
- Секция: ### bento-grid — description
- Было: "**Use when:** 3-5 items of varying importance — one featured, others supporting."
- Стало: "**Use when:** 3-5 items of varying importance — one featured, others supporting. **CRITICAL**: Featured card primary metric MUST be ≥3.5rem — icon goes ABOVE the metric in a separate row, NOT beside it. Side-by-side icon+number shrinks the number visually."

---

## Проблема 2: two-col-text long heading wraps to 2 lines, compressing card grid
### Корневая причина (5 Why)
1. Heading occupies too much vertical space
2. Because heading is 59 chars at 2.3rem — wraps to 2 lines
3. Because heading font size isn't scaled for long Russian action titles
4. Because SKILL.md only has minimum (2.2rem) without a max or length-based scale rule
5. Корень: no "long heading" handling in split-layout archetypes

### Источник решения
- ugly-presentations-anti-patterns-ru.md: content density — heading should not consume >20% of slide height
- SKILL.md Rule 20: font size minimum exists but no maximum guidance for two-col/asymmetric

### Варианты
A) Add rule: two-col-text/asymmetric-split headings >50 chars → reduce to 2.0rem and compress text
B) Add instruction to shorten heading before writing (content edit rule)

### Выбранный вариант: A — font scaling rule; combined with B (shorten text guidance)

### Конкретные правки
- Файл: .claude/skills/slidev/SKILL.md
- Секция: Step 5 — FONT SIZE FLOOR
- После: "Hero/stat numbers: ≥4rem"
- Добавить: "Split-layout heading length cap: For two-col-text and asymmetric-split archetypes, if heading exceeds 50 characters → reduce to 2.0–2.1rem AND shorten text. Heading must fit in ≤2 visual lines. Move secondary detail to card/content area."

---

## Проблема 3: bg-alt decorative arc/border color — teal-on-warm-gray lacks contrast
### Корневая причина (5 Why)
1. Decorative arcs on slides 5 and 10 (bg-alt) are subtle
2. Because teal arc borders blend into warm gray background
3. Because the current rule says "increase opacity 1.5x" but doesn't specify color alternatives
4. Because arc borders are specified as teal (accent-rgb) regardless of background surface
5. Корень: no surface-aware color switching for decorative arc/border elements

### Источник решения
- SKILL.md existing rule for bg-alt: "increase opacity by additional 1.5x on bg-alt"
- Design principle: contrast = luminance delta between element and surface

### Варианты
A) On bg-alt: switch arc/border decorations to var(--color-text) at 0.15 opacity (navy-on-warm-gray has high contrast)
B) Keep teal but raise opacity further (0.55+) — risks being too heavy visually

### Выбранный вариант: A — use dark accent color for border/arc decorations on bg-alt

### Конкретные правки
- Файл: .claude/skills/slidev/SKILL.md
- Секция: Step 5 rule 8 (Decorative Layer / Apply Decorative Layer)
- В абзаце про "bg-alt special case":
- Было: "Alternatively, use a contrasting decorative color (e.g., dark text color at 0.15 opacity instead of accent color) for better differentiation on warm surfaces."
- Стало: "**RULE**: On bg-alt slides, arc and border stroke decorations MUST use var(--color-text) at 0.15–0.20 opacity (not teal) — dark color on warm gray creates stronger contrast than same-temperature teal. Filled radial glows (background: radial-gradient) remain teal as they blend well. Pattern: arcs/borders → var(--color-text) opacity 0.15–0.20; glows/dots → teal (rgba(var(--accent-rgb), 0.35+))."
