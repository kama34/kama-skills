# Прогресс обучения

| Цикл | Тема | Оценка | AI-детекция | Лучший? | Git тег | PDF |
|------|------|--------|-------------|---------|---------|-----|
| 1 | AgroTech точное земледелие | 8.0/10 | ~9/50 | ✓ лучший | learn-edu04-cycle-1 | edu_04/learn_1/slides.pdf |
| 2 | Микросервисы DevOps | 8.2/10 | ~8/50 | ✓ лучший | learn-edu04-cycle-2 | edu_04/learn_2/slides.pdf |
| 3 | Маркетинг Q1 отчёт | 8.0/10 | ~9/50 | ~ (=1) | learn-edu04-cycle-3 | edu_04/learn_3/slides.pdf |

## Лучший цикл: 2 (8.2/10)
Откат к лучшему: `git checkout learn-edu04-cycle-2 -- .claude/skills/slidev/`

## Ключевые изменения по циклам
- Цикл 1: 0 новых правил — rendering stable at 100%, 10/10 slides
- Цикл 2: 0 новых правил — rendering stable, 10/10 slides, best design
- Цикл 3: 0 новых правил — rendering stable, 9/9 slides

## Особенности edu_04
- Все 29/29 слайдов рендерятся (100% success rate)
- Правила 45-47 из edu_03 полностью стабильны
- Фокус сместился на дизайн-качество, не рендеринг
- Паттерн: CSS-классы в `<style>` + position:absolute;inset:0 = стабильный

## Как откатиться
1. Посмотри PDF лучшего цикла
2. `git checkout learn-edu04-cycle-2 -- .claude/skills/slidev/`
