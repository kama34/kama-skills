# План исправлений — Итерация 9

## Проблема 1: Icon-trio с 4+ items создаёт переполненную строку

### Корневая причина (5 Why)
1. Почему иконки выглядят неравномерно? → Потому что описания разной длины оборачиваются на разное количество строк
2. Почему переносы строк — проблема? → Потому что в горизонтальном ряду иконки выравнены по bottom (align-items:center) — разная высота текста сдвигает вертикальный центр
3. Почему 4 items в одну строку? → Потому что archetype icon-trio позволяет 3-5 items без специального поведения для 4+
4. Корень: правило archetype не различает оптимальный макет для 3 items (одна строка, 48px gap) vs 4 items (две строки по 2, или строгий word cap на описаниях)

### Источник решения
- Design Principles Principle 2: Layout Diversity — "vary across: heading position, content structure, visual weight"
- Anti-pattern from research: "uniform-height elements in icon grids signal template thinking"

### Варианты
A) Добавить правило в archetype: для 4+ items использовать 2×2 grid вместо 1×4 row
   - Плюсы: чистое решение, меняет visual fingerprint
   - Минусы: требует изменения HTML skeleton archetype

B) Добавить правило в SKILL.md Step 5: при 4+ items в icon-trio обрезать описание до max 8 слов
   - Плюсы: не трогает skeleton, легко применить
   - Минусы: не решает структурную проблему 4-items в ряду

### Выбранный вариант: A — изменение archetype icon-trio для поддержки 2×2 варианта при 4+ items
- Изменение минимальное и решает структурную проблему

### Конкретные правки
- Файл: .claude/skills/slidev/references/composition-archetypes.md
- Секция: icon-trio → Use when / Visual
- Добавить: примечание о 4-item grid layout

---

## Проблема 2: Consecutive grid-group slides (7→8) с одинаковым fingerprint

### Корневая причина (5 Why)
1. Почему slides 7 и 8 выглядят похоже? → Оба используют `[eyebrow]+[heading]+[card grid]`
2. Почему Composition Plan не поймал это? → Потому что правило fingerprint проверяет "named archetypes" не "visual structure rendered"
3. Почему bento-grid и card-mosaic имеют одинаковый fingerprint? → Оба: label top-left + heading 2.4rem + grid-fill-bottom. Разница только внутри grid.
4. Корень: Adjacent structural fingerprint check в Step 4.5 не охватывает "top-level slide structure" — только смотрит на archetype group, не на rendered visual pattern (heading position + content area layout)

### Источник решения
- SKILL.md Step 4.5: "Adjacent focal gravity audit" — already exists but focuses on gravity direction, not structural pattern
- Composition archetype rule: "Layout Budget Rule" — grid group max 40% of content slides

### Варианты
A) Добавить явное правило: "два consecutive grid-group слайда MUST различаться heading position" — один top-left, другой centered или right
   - Плюсы: легко проверить, решает root cause
   - Минусы: ограничивает некоторые валидные комбинации

B) Добавить в Layout Budget Rule: "max 1 consecutive slide из grid group ИЛИ если 2 подряд — один должен использовать asymmetric column ratio (1.4fr+ для featured vs 1fr)"
   - Плюсы: сохраняет гибкость, требует только изменения column ratio
   - Минусы: subtle change, может не создать достаточного различия

### Выбранный вариант: B — требование asymmetric column ratio для consecutive grid slides
- Конкретно, измеримо, minimal change

### Конкретные правки
- Файл: .claude/skills/slidev/SKILL.md
- Секция: Step 4.5, Visual structure dedup section
- Было: "when two bento-grid slides share the same column ratio..."
- Стало: расширить правило на "any two consecutive grid-group slides"

---

## Проблема 3: Все section dividers имеют одинаковый bg-accent цвет

### Корневая причина (5 Why)
1. Почему все 4 section dividers одного цвета? → Composition Plan назначает bg-accent всем section-dividers по правилу "Section dividers → bg-accent (LIGHT themes)"
2. Почему это проблема? → Многократное использование одного цвета делает секции неразличимыми структурно, лишь layout разный
3. Почему правило такое? → Исторически: section dividers нужен яркий фон для контраста с content slides. Но правило не учитывает что 4 teal-colored sections подряд создают монотонию
4. Корень: Background assignment algorithm (Step 4.5 rule 4) не добавляет background variation requirement когда 3+ section dividers используют одинаковый bg-accent

### Источник решения
- Design Principles Principle 1 (section divider min contrast delta): "if section uses same bg as adjacent, must compensate"
- Section divider differentiation rule already requires layout variants but not bg variants

### Варианты
A) Требовать что 3+ section dividers варьируют background: первый bg-accent, последующие могут использовать bg-alt с oversized type
   - Плюсы: создаёт реальное различие по цвету
   - Минусы: bg-alt секции могут потерять структурный "пробой" если не достаточно отличаются от content slides

B) Добавить overlay rule: для 3+ section dividers, каждый subsequent добавляет progressively darker overlay: `rgba(0,0,0,0.0)`, `rgba(0,0,0,0.12)`, `rgba(0,0,0,0.22)` создавая subtle dark-to-darker progression
   - Плюсы: минимальное изменение, создаёт visual progression
   - Минусы: различие очень subtle, может не заметно на печатных слайдах

### Выбранный вариант: A + B combined
- Primary: 1-й section divider bg-accent clean; 2-й может bg-alt с 4rem+ heading; 3-й bg-accent + overlay; 4-й принципиально иной treatment (как variant D asymmetric)
- Это соответствует тому что уже сделано в этой презентации (slide 12 asymmetric+dark panel работало хорошо)

### Конкретные правки
- Файл: .claude/skills/slidev/SKILL.md
- Секция: Step 4.5, Section divider differentiation rule
- Добавить: When deck has 3+ section dividers, at least ONE must use bg-alt (not bg-accent) with heading ≥4rem to create background color variety across section slides
