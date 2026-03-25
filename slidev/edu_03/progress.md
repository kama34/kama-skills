# Прогресс обучения

| Цикл | Тема | Оценка | AI-детекция | Лучший? | Git тег | PDF |
|------|------|--------|-------------|---------|---------|-----|
| 1 | Кибербезопасность | 3.1/10 | ~25/50 | — | learn-cycle-1-score-3 | edu_03/learn_1/slides.pdf |
| 2 | Маркетплейс handmade | 7.2/10 | ~12/50 | ✓ лучший | learn-cycle-2-score-7 | edu_03/learn_2/slides.pdf |
| 3 | Цифровая трансформация | 1.5/10 | N/A | ✗ регрессия | learn-cycle-3-score-1 | N/A |
| 4 | Корпоративный wellness | 7.8/10 | ~10/50 | ✓ лучший | learn-cycle-4-score-7.8 | edu_03/learn_4/slides.pdf |
| 5 | Умный город транспорт | 7.5/10 | ~11/50 | ~ (=4) | learn-cycle-5-score-7.5 | edu_03/learn_5/slides.pdf |
| 6 | Онлайн-школа английского | 8.0/10 | ~9/50 | ✓ лучший | learn-cycle-6-score-8 | edu_03/learn_6/slides.pdf |
| 7 | Блокчейн supply chain | 7.8/10 | ~10/50 | ~ (=4) | learn-cycle-7-score-7.8 | edu_03/learn_7/slides.pdf |

## Лучший цикл: 6 (8.0/10)
Откат к лучшему: `git checkout learn-cycle-6-score-8 -- .claude/skills/slidev/`

## Ключевые изменения по циклам
- Цикл 1: +3 правила (inline style whitelist Rule 45, no layout in global headmatter Rule 46, QA-2b render verification)
- Цикл 2: +1 правка (Rule 46 rewrite — global frontmatter IS slide 1, content follows immediately)
- Цикл 3: +1 правило (Rule 47 — root div must use position:absolute;inset:0, every slide needs own style block)
- Цикл 4: 0 новых правил — рендеринг стабилен, все 11/11 слайдов, ноль ghost slides
- Цикл 5: 0 новых — 15/15 слайдов, keynote format
- Цикл 6: 0 новых — 9/9 слайдов, лучший дизайн (bento +320% MRR)
- Цикл 7: 0 новых — 13/13 слайдов, workshop format

## Как откатиться
1. Посмотри PDF лучшего цикла: откройте файл из колонки PDF
2. Если устраивает: `git checkout learn-cycle-<N>-score-<X> -- .claude/skills/slidev/`
3. Это вернёт SKILL.md и references к состоянию того цикла
