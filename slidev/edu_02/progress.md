# Прогресс обучения

| Цикл | Тема | Оценка | AI-детекция | Лучший? | Git тег | PDF |
|------|------|--------|-------------|---------|---------|-----|
| 1 | Логистика 4.0 | 4.2/10 | 31/50 | — | learn-cycle-1-score-4 | edu_02/learn_1/slides.pdf |
| 2 | AI в образовании | 8.0/10 | — | ★ | learn-cycle-2-score-8 | edu_02/learn_2/slides.pdf |

## Лучший цикл: 2 (8.0/10)
Откат к лучшему: `git checkout learn-cycle-2-score-8 -- .claude/skills/slidev/`

## Ключевые изменения по циклам
- Цикл 1: +6 правил (bg-accent fallback, section bg-accent на light, counting titles FAIL, eyebrow 30%, decorative opacity 3x, icon diversity)
- Цикл 2: Все правила цикла 1 применены корректно. +icon diversity (circle/rounded/ghost), 2x2 timeline grid вместо 3x2, stat-hero с текстовым hero ("потерянный семестр"), cta-variant-left на финальном слайде.

## Как откатиться
1. Посмотри PDF лучшего цикла: откройте файл из колонки PDF
2. Если устраивает: `git checkout learn-cycle-<N>-score-<X> -- .claude/skills/slidev/`
3. Это вернёт SKILL.md и references к состоянию того цикла
