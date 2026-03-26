# План исправлений — Итерация 1

## Проблема 1: Icon-trio не проверяет длину заголовков (CRITICAL)
### Корневая причина (5 Why)
1. Slide 4 renders centered titles on icon columns with >15 char titles
2. Archetype docs mention the rule but generation step doesn't enforce it
3. No character-count gate in the generation procedure

### Источник решения
- composition-archetypes.md — existing rule not enforced
- Beautiful presentations guide — left-aligned text scans 2x faster than centered

### Выбранный вариант: Add mandatory pre-render check in SKILL.md Step 5
### Конкретные правки
- Файл: SKILL.md
- Секция: Step 5 (Write slides.md) — icon-trio enforcement
- Добавить правило проверки длины заголовков при использовании icon-trio

## Проблема 2: Timeline-horizontal без визуального коннектора (MAJOR)
### Корневая причина
1. Timeline renders as 3 disconnected cards
2. No connecting line/arrow between phases
3. Archetype skeleton doesn't include connector element

### Выбранный вариант: Add connector line to timeline archetype description in SKILL.md
### Конкретные правки
- Файл: SKILL.md
- Секция: Step 5 — timeline enforcement
- Добавить обязательный коннектор

## Проблема 3: Декорации невидимы на light theme (MAJOR)
### Корневая причина
1. Generated HTML uses opacity 0.10-0.15 (dark theme defaults)
2. Preset says 0.25-0.35 but values aren't enforced in generation
3. No hard minimum in SKILL.md

### Выбранный вариант: Add hard opacity minimums for light themes
### Конкретные правки
- Файл: SKILL.md
- Секция: BACKGROUND LAYER SYSTEM
- Изменить OPACITY CALIBRATION

## Проблема 4: Нет источников статистик (MAJOR)
### Корневая причина
1. No rule in SKILL.md requiring source citations
2. Archetypes don't include source attribution element

### Выбранный вариант: Add source citation rule to content checks
### Конкретные правки
- Файл: SKILL.md
- Секция: Step 5 content quality checks
- Добавить обязательную цитату источника

## Проблема 5: bg-level checkerboard pattern (MAJOR)
### Корневая причина
1. Background assignment alternates mechanically
2. No semantic purpose rule for bg-alt

### Выбранный вариант: Add semantic guidance to bg distribution
### Конкретные правки
- Файл: SKILL.md
- Секция: Step 4.5 — Assign background levels

## Проблема 6: Data-spotlight 3 equal stats without hierarchy (MAJOR)
### Корневая причина
1. When showing 3+ metrics, no rule promotes the best one
2. data-spotlight archetype allows flat equal treatment

### Выбранный вариант: Add hero-metric promotion rule
### Конкретные правки
- Файл: SKILL.md
- Секция: Step 5 — FOCAL POINT rule expansion
