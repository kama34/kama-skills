# Game Coach

[![en](https://img.shields.io/badge/lang-English-blue)](README.md) [![ru](https://img.shields.io/badge/lang-Русский-green)](README.ru.md)

Геймифицированная система коучинга целей. Превращает управление целями в игру с XP, уровнями (10), бейджами (15), квестами и стриками. Построена на **Octalysis** (White Hat мотивационные драйверы) + методиках **GROW/WOOP**.

## Что делает

- **Ежедневный чекин** (5 мин) — трекинг стриков, XP, сброс daily-привычек, фокус на день
- **Менторская сессия** — глубокий GROW+WOOP коучинг для проработки целей (поддержка создания daily-привычек)
- **Dashboard** — полная визуализация прогресса с целями, daily-привычками, квестами, бейджами
- **Статус** — быстрый статус одной строкой
- **Анализ** — ретроспективный анализ активности за N дней (7 метрик)

## Требования

- **Google Tasks MCP** — для управления задачами (цели хранятся как отдельные списки задач)
- Claude Code с поддержкой MCP

## Установка

```bash
# Скопировать в проект
cp -r game-coach/.claude/skills/game-coach .claude/skills/

# Создать директорию состояния
mkdir -p .claude/agent-memory/game-coach

# Инициализировать состояние
cp .claude/skills/game-coach/assets/state-template.json .claude/agent-memory/game-coach/state.json
```

Зарегистрировать в `.claude/settings.json`:

```json
{
  "skills": {
    "game-coach": {
      "path": ".claude/skills/game-coach/SKILL.md",
      "description": "Геймифицированный коучинг целей с XP, уровнями, бейджами и квестами",
      "trigger": "/game"
    }
  }
}
```

## Использование

```
/game checkin     # Ежедневный чекин (+25 XP + streak bonus)
/game mentor      # GROW+WOOP менторская сессия (+75 XP)
/game dashboard   # Полный dashboard прогресса
/game status      # Быстрый статус одной строкой
/game --analyze=7 # Ретроспектива за 7 дней
/game --help      # Полная справка
```

## XP система

| Действие | XP |
|----------|-----|
| Ежедневный checkin | 25 |
| Streak bonus (за каждый день) | день x 5 |
| Закрытие задачи P0 | 80 |
| Закрытие задачи P1 | 50 |
| Закрытие задачи P2 | 30 |
| Закрытие задачи P3 | 15 |
| Mentor-сессия | 75 |
| Завершение квеста | 100-300 |
| 🔄 Daily привычка (при checkin) | по приоритету (P0=80..P3=15) |

**🔄 Daily задачи** — повторяющиеся привычки, которые сбрасываются каждый checkin. XP начисляется за вчерашнее выполнение. У каждой daily-задачи свой стрик.

## 10 уровней

| Lvl | Название | XP | Что открывается |
|-----|----------|----|-----------------|
| 1 | Стартап Мечтатель | 0 | Weekly quests |
| 2 | Первопроходец | 200 | Streak tracking |
| 3 | Фокус Воин | 500 | Advanced quests |
| 4 | Целеустремлённый | 1000 | WOOP sessions |
| 5 | Стратег | 2000 | Monthly quests |
| 6 | Мастер Фокуса | 4000 | Custom badges |
| 7 | Визионер | 6500 | Mentor deep-dives |
| 8 | Архитектор Успеха | 9500 | OKR tracking |
| 9 | Легенда Студии | 13000 | Full stats |
| 10 | Титан | 17000 | All features |

## Методики

- **GROW**: Goal > Reality > Options > Will — структурированный коучинг
- **WOOP**: Wish > Outcome > Obstacle > Plan — научно доказанная методика достижения целей
- **Octalysis White Hat**: мотивация через смысл, достижение и самовыражение (без давления и FOMO)

## Лицензия

MIT
