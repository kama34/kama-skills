# План исправлений — Итерация 5

## Проблема 1: Eyebrow Label Overuse (СЕРЬЁЗНАЯ)

### Корневая причина (5 Why)
1. Почему на 6/8 слайдов есть eyebrow labels? Потому что они создаются автоматически для каждого архетипа
2. Почему каждый архетип имеет eyebrow? Потому что архетипные скелеты в composition-archetypes.md включают `{{LABEL}}` слот
3. Почему `{{LABEL}}` заполняется для каждого слайда? Потому что в Step 5 нет механизма остановки — правило существует но без трекинга
4. Почему нет трекинга? Потому что правило сформулировано как "track usage" без конкретного счётчика или блокирующего шага
5. Корень: **Отсутствие обязательного счётчика eyebrow labels** в процедуре написания slides.md

### Источник решения
- SKILL.md Rule 32 (All-caps eyebrow labels limit): "max 30% of slides. When limit is reached, omit the eyebrow"
- Решение: добавить в Step 5 "Enforcement rules during writing" явный счётчик с блокировкой

### Варианты
A) Добавить строку в Enforcement rules: отслеживать счётчик перед каждым слайдом, блокировать при достижении 30%
B) Добавить в QA-0c Anti-Pattern Scan: автоматическое обнаружение и исправление (post-hoc)

**Выбранный вариант: A** — причина: превентивная мера лучше пост-фактум исправления. QA-0c как резервный.

### Конкретные правки
- Файл: SKILL.md
- Секция: Step 5, "Enforcement rules during writing", пункт "Eyebrow label limit (30%)"
- Было: `"Eyebrow labels (0.7rem uppercase letter-spaced text above headings) are permitted on AT MOST 30% of slides in the deck. For a 10-slide deck: max 3 slides with eyebrows. Track usage during writing — when the limit is reached, omit the eyebrow on remaining slides and let the heading speak for itself."`
- Стало: добавить `"**MANDATORY COUNTER**: Before writing each slide, compute: allowed = floor(total_slides × 0.30). Exempt: cover slide (slide 1) and CTA slide (last). Counter tracks content slides only. When eyebrow_count reaches allowed for content slides, ALL subsequent slides must have NO eyebrow label — heading speaks for itself. Example: 8-slide deck → allowed = floor(6 × 0.30) = 1 eyebrow on content slides (cover+CTA exempt). Write the counter state as a comment before each slide: <!-- eyebrow: N/allowed -->"`

---

## Проблема 2: Section Divider — Label Not Insight (СЕРЬЁЗНАЯ)

### Корневая причина (5 Why)
1. Почему section-divider heading — это label, а не insight? Потому что архетип section-divider используется для "transition between major sections" и heading = section name
2. Почему section names — это labels? Потому что Ghost Deck test освобождает section dividers от проверки action titles
3. Почему освобождает? Потому что в SKILL.md написано "Cover and CTA slides are exempt (aligns with Rule 30)" — но это неточно описывает только cover+CTA, а section dividers попадают в серую зону
4. Почему серая зона? Потому что правило Rule 30 говорит "Exception: cover and CTA slides may use short titles" — section dividers не упомянуты явно
5. Корень: **Ghost Deck test не определяет минимальное требование для section-divider slides** — они могут быть labels без проверки

### Источник решения
- SKILL.md Rule 30 (Action titles) + Ghost Deck test в Step 4.5
- Решение: добавить требование к section-divider: если heading = label, то description ДОЛЖЕН содержать claim/insight

### Конкретные правки
- Файл: SKILL.md
- Секция: Step 4.5, Ghost Deck test — ENHANCED, в секции "FAIL conditions"
- Было: "Cover slide (slide 1) and CTA slide (last slide) are exempt (aligns with Rule 30)."
- Стало: добавить: `"Section divider slides: heading may be a topic label ONLY IF the description below it contains a claim, number, or outcome. If description is also generic (no number, comparison, verb, outcome), FAIL — rewrite the heading as an insight. Pattern: 'Почему клиенты остаются' (heading) + 'Долгосрочные партнёрства — главный показатель' (description) → acceptable. 'Почему клиенты остаются' (heading) + 'Ценности нашей компании' (description) → FAIL, rewrite heading."`

---

## Незначительные (отложены)

1. **3-slide fingerprint window** — расширить visual fingerprint dedup с 2 до 3 слайдов. Незначительно: средний слайд (слайд 4, asymmetric-split) достаточно различен визуально. Отложено — не мешает читабельности.

2. **Slide 7 gap 16px → 20px** — незначительная проблема с плотностью карточек. Отложено — карточки читаются нормально, 16px ≥ минимальный gap (16px).

3. **Cover dot grid placement** — незначительно — тексту не мешает, только небольшое визуальное наложение.
