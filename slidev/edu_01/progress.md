# Прогресс обучения

| Цикл | Тема | Оценка | Лучший? | Git тег | PDF |
|------|------|--------|---------|---------|-----|
| 1 | Цифровая трансформация логистики | 5.6/10 | — | learn-cycle-1-score-5 | edu_01/learn_1/slides.pdf |
| 2 | Осознанное питание | 6.0/10 | | learn-cycle-2-score-6 | edu_01/learn_2/slides.pdf |
| 3 | Квартальный отчёт SaaS Q1 | 8.8/10 | ✓ лучший | learn-cycle-3-score-8 | edu_01/learn_3/slides.pdf |

## Лучший цикл: 3 (8.8/10)
Откат к лучшему: `git checkout learn-cycle-3-score-8 -- .claude/skills/slidev/`

## Ключевые изменения по циклам
- Цикл 1: базовая оценка. Применено 6 правил: opacity calibration, icon-trio gates, timeline connector, source citations, anti-checkerboard, focal point expansion
- Цикл 1 → 2: +0.4. Источники и anti-checkerboard работают. Применено 2 правила: bg-alt отдельная opacity (0.35+), bento featured cell ≥3.5rem
- Цикл 2 → 3: +2.8. Все 8 накопленных правил работают. Добавлено 2: bg-alt decoration override, card-mosaic min decoration

## Как откатиться
1. Посмотри PDF лучшего цикла: откройте файл из колонки PDF
2. Если устраивает: `git checkout learn-cycle-<N>-score-<X> -- .claude/skills/slidev/`
3. Это вернёт SKILL.md и references к состоянию того цикла
