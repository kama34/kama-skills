# Сравнительный анализ — Цикл 1: PayBridge FinTech

## Stitch vs Наш генератор — 6 измерений

### BACKGROUNDS
```
Stitch: 1 фоновый слой (solid surface color), фоновое изображение на обложке (opacity-20)
        5+ уровней surface (#000000, #0e0e0f, #131314, #1a191b, #201f21, #262627)
        Глубина создаётся РАЗЛИЧИЕМ поверхностей между слайдами, а не наложениями
Ours:   2-3 слоя (solid + radial-glow + dot-grid), декоративные кольца
        3 bg-level (#0C1524, #13203A, #0D1F1E) — менее нюансированно
Gap:    Stitch создаёт глубину через ГРАДАЦИИ поверхностей (5+ оттенков), что тоньше и профессиональнее.
        Мы используем декоративные наложения (glows, dots) — добавляют характер, но могут перегружать.
→ RULE: Добавить систему "surface depth" — 4-5 оттенков поверхности вместо 3-х bg-levels.
         Новые переменные: --surface-0, --surface-1, --surface-2, --surface-3, --surface-4
         Для карточек разной вложенности использовать разные уровни surface.
```

### LAYOUT
```
Stitch: 12-колоночный grid как базовая система. Пропорции: 7/5, 4/8, 2/3, 5/7
        КАЖДЫЙ слайд — уникальная пропорция колонок
Ours:   Именованные архетипы с фиксированными grid-template. Повторяющийся 60/40 split.
        bento-grid: 1.25fr/1fr, asymmetric-split: тоже ~60/40
Gap:    Stitch варьирует пропорции СИЛЬНЕЕ. 7/5 ≠ 4/8 ≠ 2/3 — каждый слайд читается иначе.
        Наши архетипы склоняются к одинаковой пропорции.
→ RULE: В архетипах добавить больше вариаций пропорций:
         - "wide-left": 65/35 или 7/5
         - "narrow-left": 35/65 или 4/8
         - "golden": 61.8/38.2
         Архетип при рендеринге должен ВАРЬИРОВАТЬ пропорцию, а не повторять одну.
```

### TYPOGRAPHY
```
Stitch: Hero числа: text-[10rem] ($8.5 трлн), text-[12rem] (50 000 TPS)
        Заголовки: text-5xl до text-7xl (3.5-4.5rem)
        Body: text-lg до text-2xl (1.1-1.5rem)
        Labels: text-xs, uppercase, tracking-[0.2em]
        RATIO hero:body = 10:1 (12rem vs 1.1rem)
Ours:   Hero числа: ~4-5rem ($8.5 трлн)
        Заголовки: 2.5-3rem
        Body: 1.25rem
        RATIO hero:body = 4:1 (5rem vs 1.25rem)
Gap:    Stitch ГОРАЗДО смелее с размерами. "$8.5 трлн" у Stitch = 10rem, у нас = ~5rem.
        "50 000 TPS" у Stitch = 12rem — ВДВОЕ больше нашего максимума.
        Stitch ratio 10:1 создаёт немедленный фокус. Наш 4:1 — осторожный.
→ RULE: Увеличить минимум hero-чисел на stat-hero слайдах до 7-10rem (сейчас 4rem).
         Целевой ratio фокальной точки: 6:1 минимум для breathing-слайдов (было 2:1).
         Для центрированных hero-слайдов разрешить до 12rem.
```

### DECORATION
```
Stitch: Минимальная — акцентные линии (h-1.5 w-32), border-top на карточках,
        surface depth. БЕЗ blob'ов, radial glow, dot-grid.
        Чистый, корпоративный look.
Ours:   Активная — radial-glow, dot-grid, кольца, ghost-типографика.
        Каждый слайд имеет 2-3 декоративных элемента.
Gap:    Stitch ЧИЩЕ. Наш декор более "дизайнерский", но может перегружать,
        особенно для корпоративных/финтех тем. Stitch достигает глубины
        через вариации поверхности, а не наложенные формы.
→ RULE: Для корпоративных/финтех тем — снижать количество декоративных элементов.
         Добавить "decoration intensity" в preset: "minimal", "moderate", "rich".
         minimal = только accent lines + surface depth, никаких blob'ов.
         Текущий default = moderate.
```

### CARDS
```
Stitch: 4+ стиля:
        (1) bg-surface-container — стандартный
        (2) bg-surface-container-low + border — тонкая рамка
        (3) bg-surface-container-high + border-t-2 border-primary + shadow-2xl — акцентная полоса сверху
        (4) bg-surface-container-low + border-primary/10 + rounded-3xl — крупный метрический блок
        ПАТТЕРН: border-t-2 border-primary на case-study карточках — профессиональный штрих
Ours:   3 стиля: card-solid, card-ghost, card-accent.
        Нет паттерна "цветная полоса сверху".
Gap:    Stitch's border-top colored strip — профессиональный паттерн, которого у нас нет.
        Также Stitch использует тени (shadow-2xl) на ключевых карточках.
→ RULE: Добавить card-stripe — карточка с цветной border-top (2-3px solid accent).
         Использовать для case-study и portfolio карточек.
         CSS: .card-stripe { border-top: 3px solid var(--color-accent); box-shadow: 0 25px 50px rgba(0,0,0,0.15); }
```

### HIERARCHY
```
Stitch: Фокальная точка ДОМИНИРУЕТ — 10rem hero vs 1rem body = ratio 10:1
        Глаз немедленно знает, куда смотреть
        Метрики вложены в иерархию: 7rem primary → 4rem secondary → 1rem body
Ours:   Фокальная точка заметна, но не доминирует — 5rem hero vs 1.25rem body = ratio 4:1
        Все элементы ближе по размеру — конкуренция за внимание
Gap:    Stitch's ratio 10:1 создаёт драматизм. Наш 4:1 — слишком равномерный.
        Stitch также использует 3-уровневую иерархию метрик: primary→secondary→body
→ RULE: Ввести 3-уровневую иерархию метрик для слайдов с несколькими числами:
         Level 1 (hero): 7-10rem, единственное число
         Level 2 (supporting): 3-4rem, 2-3 числа
         Level 3 (context): 1.25rem body text
         Текущее правило допускает все числа одинакового размера — запретить это.
```

## Stitch Score: 7.5/10
## Our Score: 6.5/10
## Delta: -1.0 (Stitch лучше)

### Что Stitch делает лучше
1. Hero typography boldness (10-12rem vs our 4-5rem)
2. Surface depth system (5+ levels vs 3)
3. Grid ratio variety (7/5, 4/8, 2/3 vs fixed 60/40)
4. Card accent patterns (border-top strips)
5. Cleaner decoration for corporate themes
6. Detailed dashboard mockup (routing engine wireframe)

### Что мы делаем лучше
1. AI-safe color palette (teal vs Stitch's purple #a3a6ff)
2. 2-font discipline (Stitch uses 3)
3. Font size minimums enforced (Stitch goes to 8px)
4. Warm accent variety (#D97706 amber)
5. Decorative personality (ghost typography, dot-grids)
6. Composition archetype system (structured planning)
7. Shape vocabulary (icon containers, pills)
