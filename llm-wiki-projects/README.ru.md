# LLM Wiki Projects

[![en](https://img.shields.io/badge/lang-English-blue)](README.md) [![ru](https://img.shields.io/badge/lang-Русский-green)](README.ru.md)

Скилл для создания, аудита, миграции и поддержки проектов как компактных Obsidian-like LLM Wiki баз знаний.

Он превращает папку проекта в живую wiki-систему с `wiki-home`, обёртками источников, атомарными заметками, проектными дашбордами, картами, логами, governance-файлами и проверкой структуры. Wiki становится долговременной памятью проекта, а чат остаётся рабочей поверхностью.

## Что делает

- Аудитит проект перед миграцией.
- Создаёт структуру `00-inbox`, `10-sources`, `20-notes`, `30-maps`, `40-projects`, `90-meta`, `assets`.
- В кодовых репозиториях не трогает код и создаёт локальную `_wiki/`.
- Консервативно переносит note-like папки.
- Создаёт source notes, project dashboards, maps, logs, Obsidian Bases и Canvas-шаблоны.
- Проверяет wikilinks, frontmatter, дубли имён заметок, orphan notes и частые проблемы Obsidian-ссылок внутри таблиц.

## Требования

- Python 3.
- Claude Code или другой агент, который умеет читать skill-файлы и запускать локальные скрипты.
- Опционально: Obsidian для удобного просмотра получившейся markdown-wiki.

Внешние Python-пакеты не нужны.

## Установка

### В стиле Claude Code

```bash
mkdir -p .claude/skills
cp -r llm-wiki-projects/.claude/skills/llm-wiki-projects .claude/skills/
```

Добавить в `.claude/settings.json`:

```json
{
  "skills": {
    "llm-wiki-projects": {
      "path": ".claude/skills/llm-wiki-projects/SKILL.md",
      "description": "Create and maintain Obsidian-like LLM Wiki project knowledge bases",
      "trigger": "/wiki"
    }
  }
}
```

### В стиле Codex

```bash
mkdir -p ~/.codex/skills
cp -r llm-wiki-projects/.claude/skills/llm-wiki-projects ~/.codex/skills/
```

## Использование

Попросите агента использовать скилл:

```text
/wiki create an LLM Wiki for this project
/wiki audit this repository knowledge structure
/wiki migrate these research notes into a governed project wiki
/wiki validate the wiki and write a health report
```

Скрипты можно запускать и напрямую:

```bash
python3 .claude/skills/llm-wiki-projects/scripts/audit_project.py /path/to/project
python3 .claude/skills/llm-wiki-projects/scripts/migrate_project.py /path/to/project
python3 .claude/skills/llm-wiki-projects/scripts/validate_wiki.py /path/to/project --write-report
```

## Безопасность

- Audit-скрипт работает только на чтение.
- В кодовых репозиториях миграция оставляет на месте исходники, package-файлы, lockfiles, тесты, `README`, `LICENSE` и `CHANGELOG`.
- В knowledge-only проектах миграция может переносить найденные note/source файлы в wiki-зоны. Если нужно сначала посмотреть план, начните с audit.
- Raw sources сохраняются как доказательная база; синтез пишется в wiki-заметки.

## Состав скилла

- `SKILL.md` — основной workflow агента.
- `scripts/` — инструменты аудита, миграции и валидации.
- `references/` — методология, схемы, workflows, governance, lifecycle источников и интеграции с Obsidian.
- `assets/templates/` — шаблоны генерируемых заметок.
- `assets/bases/` и `assets/canvas/` — стартовые Obsidian Bases и Canvas.

## Лицензия

MIT
