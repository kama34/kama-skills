# План исправлений — Итерация 8

## Проблема 1: icon-trio centered titles in narrow columns

### Корневая причина (5 Why)
1. Почему заголовки в icon-trio выглядят нестабильно? — Потому что они центрированы в узкой колонке (~200px) и переносятся на 2 строки.
2. Почему 2-строчный центрированный заголовок проблематичен? — Потому что создаёт "песочные часы": широкий иконка-контейнер сверху → узкий 2-строчный заголовок → снова широкое описание — нарушает законы Gestalt (единство формы).
3. Корень: Архетип icon-trio в composition-archetypes.md задаёт `text-align:center` для ITEM_TITLE и ITEM_DESC без условия длины заголовка. Нет правила для разрешения конфликта с правилом "многострочный текст = left-align".

### Источник решения
- SKILL.md Rule 9: "Multi-line body text MUST be text-align: left"
- design-principles.md Principle 2: "Every slide must be visually distinguishable"
- Решение: добавить в composition-archetypes.md условие: если ITEM_TITLE > 15 символов — использовать left-align для всей колонки

### Варианты
A) Добавить примечание в archetype skeleton (icon-trio): "Long titles (>15 chars) → switch column to left-aligned (remove align-items:center, add text-align:left)"
B) Изменить дефолт archetype на left-aligned columns и оставить center только для коротких titles

### Выбранный вариант: A — минимальное изменение, сохраняет обратную совместимость

### Конкретные правки
- Файл: .claude/skills/slidev/references/composition-archetypes.md
- Секция: icon-trio archetype "Use when" / "Visual" description
- Добавить: примечание о left-align для длинных заголовков

---

## Проблема 2: Ghost number opacity 0.10 too low on teal bg-accent

### Корневая причина (5 Why)
1. Почему ghost "04" невидим? — Opacity 0.10 rgba(255,255,255,0.10) на teal (#0D9488) даёт недостаточный luminance контраст.
2. Почему использовано 0.10? — SKILL.md Rule 28 задаёт минимум 0.10 на bg-accent и называет его "minimum".
3. Корень: Минимум 0.10 был определён для тёмных (navy/charcoal) bg-accent фонов. Teal (#0D9488) имеет luminance ~28% — это средний тон, требующий более высокого opacity для white ghost numbers.

### Источник решения
- SKILL.md Rule 28: "ghost number at opacity below 0.15 on a warm background will be invisible"
- Текущий пример section-divider в slides (slide 4) подтверждает: 0.10 на teal невидим в PNG export.

### Варианты
A) Поднять минимум ghost number opacity для teal/medium-luminance bg-accent с 0.10 до 0.16 minimum
B) Добавить условие: "dark (navy) bg-accent → 0.10 min; medium (teal) bg-accent → 0.16 min; light bg-accent (rare) → 0.25 min"

### Выбранный вариант: B — более точное правило, учитывает разные оттенки bg-accent

### Конкретные правки
- Файл: SKILL.md
- Секция: Rule 28 (CRITICAL — Ghost decorative number opacity enforcement)
- Было: "Any ghost number at opacity below 0.15 on a warm background will be invisible in exported PNGs."
- Стало: добавить уточнение о bg-accent luminance levels

---

## Проблема 3: Radial glow overflow on full-width symmetric layouts

### Корневая причина (5 Why)
1. Почему glow перекрывает правую колонку icon-trio? — slide-decor-glow класс размещает 600px glow в bottom-right. Для full-width layouts правая колонка — это контентная зона.
2. Почему нет ограничения? — Правило в Principle 6 (decorative layer) говорит "30-50% slides have decorative motifs" но не указывает какие motifs подходят для каких layout-типов.
3. Корень: Нет маппинга archetype-type → preferred-motif. Glow в bottom-right подходит для асимметричных/bento layouts, не для full-width.

### Источник решения
- design-principles.md Principle 6: описывает типы мотивов но не их compatible layouts
- Решение: добавить guidance в Principle 6 или Step 5 о выборе motif по layout-type

### Варианты
A) Добавить в Step 5 bullet: "For full-width symmetric layouts (icon-trio, two-col-text), prefer slide-decor-dots or slide-decor-arc. Avoid slide-decor-glow which bleeds into right content columns."
B) Уменьшить size glow до 300px для всех случаев

### Выбранный вариант: A — сохраняет текущий glow size для asymmetric layouts (где он работает)

### Конкретные правки
- Файл: SKILL.md
- Секция: Step 5, point 8 (Apply Decorative Layer — Principle 6)
- Добавить: layout-motif compatibility guidance
