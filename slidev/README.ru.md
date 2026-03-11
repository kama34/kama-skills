# Slidev Skill — Тестовая площадка

[![en](https://img.shields.io/badge/lang-English-blue)](README.md) [![ru](https://img.shields.io/badge/lang-Русский-green)](README.ru.md)

Эта директория выполняет две функции:

1. **Исходники скилла** — сам скилл лежит в `.claude/skills/slidev/`
2. **Песочница** — запускайте эксперименты, генерируйте презентации, дорабатывайте скилл прямо здесь

## Структура директории

```
slidev/
  .claude/skills/slidev/     # ← Отслеживается git (сам скилл)
    SKILL.md
    references/
    assets/
  .gitignore                  # ← Отслеживается git
  README.md                   # ← Отслеживается git
  README.ru.md                # ← Отслеживается git
  my-presentation/            # ← Игнорируется git (ваши эксперименты)
  another-test/               # ← Игнорируется git
  notes.txt                   # ← Игнорируется git
```

## Как работает .gitignore

`.gitignore` в этой директории использует паттерн **белого списка**:

```gitignore
# Игнорировать всё
*

# Кроме этого
!.gitignore
!.claude/
!.claude/**
!README.md
!README.ru.md
```

**Зачем?** Эта директория — песочница. Генерируйте презентации, ставьте npm-пакеты, экспортируйте PDF — ничего из этого не попадёт в репозиторий. Коммитятся только изменения самого скилла (внутри `.claude/`).

## Рабочий процесс

```bash
# 1. Экспериментируйте свободно — создавайте презентации, тестируйте скилл
/slidev my-outline.md
/slidev --export png2pdf

# 2. Если вы улучшили скилл, изменения в .claude/ — git их видит
git diff slidev/.claude/

# 3. Коммитьте только улучшения скилла
git add slidev/.claude/
git commit -m "fix(slidev): улучшена обработка overlay для PDF-экспорта"
```

## Документация скилла

Подробнее о скилле: [.claude/skills/slidev/Readme.md](.claude/skills/slidev/Readme.md)
