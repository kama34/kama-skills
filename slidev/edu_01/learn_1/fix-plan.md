# План исправлений — Итерация 1

## Проблема 1: Декоративные CSS-классы не рендерятся в экспорте
### Корневая причина (5 Why)
1. Декоративные элементы невидимы в экспортированных PNG
2. Потому что CSS ::after pseudo-elements на div-элементах не срабатывают
3. Потому что Slidev обрабатывает class= на inline HTML иначе — scoped styles и per-slide <style> не поддерживают ::after на элементах, определённых в styles/index.css через class-names в inline HTML

### Источник решения
- PDL cycle 3 regression подтвердил: CSS-class-only подход ненадёжен
- Решение: декоративные элементы должны быть РЕАЛЬНЫМИ HTML-элементами с inline styles, а не pseudo-elements через CSS classes

### Варианты
A) Использовать реальные HTML div элементы для декора с inline styles — плюсы: 100% надёжно, видимо в экспорте; минусы: больше HTML-кода
B) Использовать SVG data URI в background-image inline style — плюсы: компактно; минусы: менее гибко

### Выбранный вариант: A — реальные HTML div-элементы с inline styles

### Конкретные правки
- Файл: SKILL.md
- Секция: "Step 5: Write slides.md" → "Apply Decorative Layer (Principle 6)"
- Добавить: конкретный HTML-паттерн для декоративных элементов как inline div-элементы внутри background layer

## Проблема 2: Template lock — 7+ одинаковых структур подряд
### Корневая причина (5 Why)
1. 7 слайдов подряд имеют идентичную структуру "label → heading → grid"
2. Потому что генератор не отслеживает реальную визуальную структуру, только название архетипа
3. Корень: правило "каждые 2-3 слайда менять структуру" недостаточно конкретно — все архетипы выглядят одинаково, если имеют одинаковую внутреннюю компоновку

### Источник решения
- design-principles.md Principle 2: "Mandatory structural variation on every 3rd content slide"

### Варианты
A) Добавить в SKILL.md строгое правило: каждый 3-й контентный слайд ОБЯЗАН использовать centered или inverted layout — плюсы: простое правило; минусы: может быть слишком жёстким
B) Добавить в Step 4.5 проверку визуальной структуры: если 3+ слайда подряд начинаются с "label top-left → heading → grid below", принудительно вставить centered hero layout

### Выбранный вариант: A + усиление в Step 5

### Конкретные правки
- Файл: SKILL.md
- Секция: Step 5 enforcement rules
- Добавить: "STRUCTURAL BREAK RULE: After 2 content slides with 'label-top-left + heading + grid/cards-below' pattern, the 3rd MUST use either: (a) centered layout with hero number/statement, (b) asymmetric split with visual element dominating left side, (c) no label — heading-only entry. Track the pattern and enforce rotation."

## Проблема 3: bg-alt недоиспользован
### Корневая причина
Правило в Step 4.5 говорит "bg-alt for 15% additional slides, spaced every 5th-6th" — но это слишком размыто.

### Выбранный вариант: Усилить правило

### Конкретные правки
- Файл: SKILL.md
- Секция: Step 4.5 background level assignment
- Изменить: правило должно говорить "bg-alt MUST appear on at least 25% of non-cover/CTA slides"
