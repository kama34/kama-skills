# План исправлений — Итерация 2

## Проблема 1: icon-trio ghost container невидим на bg-alt
### Корневая причина
1. icon-ghost использует transparent bg + border в accent color
2. На bg-alt (#E8E6DF) тонкая teal граница сливается с тёплым серым
3. Скилл не дифференцирует container стили по bg-level
### Выбранный вариант: ghost container на bg-alt использует более контрастный стиль
### Правки: SKILL.md Step 5 enforcement — icon containers must match bg-level

## Проблема 2: 33% слайдов = identical 2x2 grid (layout budget violation)
### Корневая причина
1. two-col-text, card-mosaic и timeline-horizontal все рендерятся как 2×2 grid визуально
2. Скилл проверяет archetype names, но не визуальную структуру
3. timeline-horizontal использует 2×2 grid вместо горизонтальной линии
### Выбранный вариант: добавить visual structure dedup rule
### Правки: SKILL.md Step 4.5 — visual structure dedup check

## Проблема 3: Идентичные секционные слайды
### Корневая причина
1. Скилл имеет только один section-divider шаблон
2. Нет правила чередования для множественных секций
### Выбранный вариант: добавить section variant alternation rule
### Правки: SKILL.md Step 5 — section divider differentiation

## Проблема 4: Stat-hero структурные близнецы
### Корневая причина
1. stat-hero archetype имеет один шаблон
2. Нет правила вариации при множественных stat slides
### Выбранный вариант: stat-hero variants (centered vs asymmetric)
### Правки: SKILL.md Step 5 — stat slide variation rule
