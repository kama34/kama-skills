# План исправлений — Итерация 1

## Проблема 1: Обложка и CTA рендерятся белыми при экспорте
### Корневая причина (5 Why)
1. PNG-экспорт показывает белые слайды
2. CSS-переменные на position:absolute дочерних элементах не резолвятся
3. Slidev headless export не гарантирует resolution CSS custom properties на inner divs
### Выбранный вариант: добавить fallback hex-значения в var()
### Конкретные правки
- Файл: SKILL.md
- Секция: Step 5 (slides.md rules) — после enforcement rules
- Добавить новое правило о CSS variable fallbacks для bg-accent слайдов

## Проблема 2: Секционные слайды неотличимы от контентных (light theme)
### Корневая причина
1. bg-alt (#E8E6DF) vs bg-base (#FAF9F6) — delta только 6%
2. Скилл не дифференцирует section slides для light themes
### Выбранный вариант: section dividers на light themes используют bg-accent с белым текстом
### Конкретные правки
- Файл: references/design-principles.md
- Секция: Principle 1 — Background Level System, slide-type to bg-level mapping

## Проблема 3: 100% идентичные icon-контейнеры
### Корневая причина
1. Только один CSS-класс .icon-container
2. Нет требования чередовать формы
### Выбранный вариант: добавить 3 варианта + enforcement rule
### Конкретные правки
- Файл: SKILL.md
- Секция: Step 4 (styles/index.css) — Shape vocabulary CSS

## Проблема 4: Eyebrow labels на 80% слайдов (лимит 30%)
### Корневая причина
1. Все архетипы содержат eyebrow slot
2. Нет enforcement правила с лимитом
### Выбранный вариант: добавить правило лимита в Step 5
### Конкретные правки
- Файл: SKILL.md
- Секция: Step 5 enforcement rules

## Проблема 5: Ghost Deck тест — counting titles pass incorrectly
### Корневая причина
1. "Три барьера" содержит число, но это label а не insight
### Выбранный вариант: ужесточить FAIL conditions
### Конкретные правки
- Файл: SKILL.md
- Секция: Step 4.5 Ghost Deck test

## Проблема 6: Декоративные элементы невидимы при экспорте на light themes
### Корневая причина
1. Opacity 0.32 на 1.5px dots на #FAF9F6 — недостаточный контраст в PNG
### Выбранный вариант: увеличить минимумы opacity для light themes
### Конкретные правки
- Файл: SKILL.md
- Секция: Step 5, rule 8 (Decorative Layer)
