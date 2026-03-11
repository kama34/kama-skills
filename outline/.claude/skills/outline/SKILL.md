---
name: outline
description: "Use when creating presentation outlines/structures. Supports agent pipeline presets, auto-selection, preset creation, and agent training. Handles --preset, --format, --new-preset, --learn=N, and --help."
argument-hint: "[--help | --preset <name> | --format <fmt> | --new-preset | --learn=N [preset]] [<topic>]"
---

# Outline — Presentation Structure Generator

You generate presentation structures using agent pipelines. Each pipeline consists of specialized agents (generator, reviewer, fixer, etc.) that iteratively create, review, and refine a presentation outline.

## Language Rule

**CRITICAL:** All user-facing output MUST be in Russian. This includes:
- Help text, prompts, error messages, reports, summaries
- Generated presentation structures (slide titles, bullet points, speaker notes)
- Wizard questions and confirmations
- Agent-generated content (structures, reviews, feedback)

Internal skill logic, variable names, file names, and YAML fields remain in English.

## References

Before executing, internalize these references:
- `references/preset-format.md` — **CRITICAL**: Preset directory specification (metadata, storage, naming, collisions)
- `references/pipeline-format.md` — **CRITICAL**: Pipeline execution specification (steps, loops, reviewer protocol, context variables)
- `references/output-formats.md` — Output format specs (slidev, universal, custom)

## Input Parsing

Parse the user's input to determine the subcommand or mode:

### Subcommands (handle before anything else)

**`--help`**: Display usage help and stop. Show:

```
Outline — Генератор структуры презентаций

Использование:
  /outline <тема>                               Сгенерировать структуру (авто-выбор пресета)
  /outline --preset <имя> <тема>                Использовать конкретный пресет
  /outline --format <slidev|universal|custom>   Переопределить формат вывода
  /outline --new-preset                         Создать новый пресет агентного пайплайна
  /outline --learn=N [пресет]                   Обучить агентов на N тестовых прогонах
  /outline --help                               Эта справка

Как это работает:
  Outline использует агентные пайплайны для итеративного создания, рецензирования
  и улучшения структур презентаций. Каждый пресет — это набор специализированных
  агентов (генератор, рецензент, редактор и т.д.), настроенных под конкретный тип
  презентации.

  Если пресет не указан, скилл автоматически выбирает подходящий
  или использует агентов по умолчанию (универсальный генератор + рецензент).

Форматы вывода:
  slidev      (по умолчанию) ## Слайд N: Заголовок + буллиты — совместим с /slidev
  universal   Секции, тезисы, заметки спикера — не привязан к инструменту
  custom      Определяется пресетом

Хранение пресетов:
  Локально:  .outline-presets/<имя>/
  Глобально: ~/.claude/outline-presets/<имя>/
  Поиск:     сначала локально, потом глобально
```

Stop here — do not proceed to generation.

---

**`--new-preset`**: Run the Create Preset Procedure (CP-1 through CP-8). Stop here — do not proceed to generation.

---

**`--learn=N [preset]`**: Run the Learn Procedure (L-1 through L-6). Parse N from the argument (e.g., `--learn=5`). Optional `preset` argument specifies which preset to train. Stop here — do not proceed to generation.

---

**Otherwise** — this is a generation request. Parse `--preset`, `--format`, and extract the topic. Run the Generate Procedure (G-1 through G-7).

---

## Generate Procedure

### G-1: Parse Command

Extract from the user's input:
- **Topic** — the presentation subject (everything that isn't a flag)
- **`--preset <name>`** — optional, specific preset to use
- **`--format <slidev|universal|custom>`** — optional, output format override

If no topic is provided, ask the user: "О чём будет презентация?"

### G-2: Select Preset

Three paths, in priority order:

**Path A: `--preset <name>` specified**

1. Look up `<name>` in local storage: `.outline-presets/<name>/`
2. If not found, look up in global storage: `~/.claude/outline-presets/<name>/`
3. If not found in either, error:
   ```
   Пресет '<name>' не найден.
   Искали в: .outline-presets/<name>/, ~/.claude/outline-presets/<name>/
   Доступные пресеты: <list all found presets, or "нет">
   ```
   Stop here.

**Path B: Auto-select from available presets**

1. Scan for presets in both locations:
   - `.outline-presets/*/preset.md`
   - `~/.claude/outline-presets/*/preset.md`
2. If presets exist, read each `preset.md` to extract `name`, `description`, `keywords`
3. Make a single LLM call (use the Agent tool) with the user's topic and all preset metadata:

   ```
   Given the presentation topic: "<topic>"

   Available presets:
   1. <name>: <description> (keywords: <keywords>)
   2. <name>: <description> (keywords: <keywords>)
   ...

   Which preset best matches this topic? Reply with ONLY the preset name,
   or "none" if no preset is a good match.
   ```

4. If the agent responds with a preset name → use that preset
5. If the agent responds "none" → use default (Path C)

**Path C: Use built-in default**

Use the default preset from `assets/default/` within the skill directory. This path is used when:
- No presets exist in local or global storage
- Auto-selection returns "none"

### G-3: Load & Validate Pipeline

1. Read the preset directory:
   - `preset.md` — extract frontmatter fields
   - `pipeline.md` — extract `steps` array
   - `agents/*.md` — read all agent files

2. **Validate pipeline:**
   - Every `agent` value in `steps` must have a corresponding file in `agents/`
   - Every `loop_with` value must reference an agent in `steps`
   - `stop_when` is required when `loop_with` is present
   - At least one `role: create` agent exists
   - At least one `role: review` agent exists

   If validation fails:
   ```
   Ошибка валидации пайплайна: <specific issue>
   Пример: Агент 'investor-reviewer' указан в pipeline.md, но файл agents/investor-reviewer.md не найден.
   ```
   Stop here.

3. **Determine active settings:**
   - `max_iterations` — from preset.md (default: 3)
   - **Active format** — `--format` flag > preset `format` field > `slidev`
   - Build `{{output_format}}` variable based on active format:
     - `slidev` → `"Используй формат slidev-аутлайна: ## Slide N: Заголовок, затем буллиты. Целься на 8-12 слайдов. Весь контент на русском языке."`
     - `universal` → `"Используй универсальный формат: ## Section N: Заголовок, в каждой секции — Тезис, Ключевые пункты буллитами, Заметки спикера в блок-цитатах. Весь контент на русском языке."`
     - `custom` → use the literal `custom_format_description` text from preset.md

### G-4: Run Pipeline Cycle

Initialize context variables:
```
topic         = user's topic
current_draft = "" (empty initially)
feedback      = "" (empty initially)
iteration     = 1
output_format = <constructed in G-3>
```

**Execute pipeline steps in order:**

For each step in the `steps` array:

#### Step with `role: create` (Generator)

1. Read the agent file from `agents/<agent>.md`
2. Substitute all `{{variables}}` in the agent prompt with current context values
3. Dispatch via the **Agent tool** as a subagent:
   - Provide the substituted prompt as the agent's task
   - Instruct the agent to output ONLY the structure, no preamble
4. Collect the agent's output → set `current_draft` to this output

#### Step with `role: review` + `loop_with` (Reviewer in a loop)

This step initiates the review→fix cycle:

1. Read the reviewer agent file from `agents/<agent>.md`
2. Substitute `{{variables}}` (including `{{current_draft}}`)
3. Dispatch the reviewer via the **Agent tool**
4. Parse the reviewer's output:
   - Find the last non-empty line
   - If it starts with `APPROVED` → exit loop, proceed to post-loop steps
   - If it starts with `NEEDS_REVISION:` → extract feedback text after the prefix

5. If `NEEDS_REVISION` and `iteration < max_iterations`:
   - Increment `iteration`
   - Set `feedback` to the extracted feedback text
   - Look up the `loop_with` agent:
     - If it has `role: fix` → read fixer agent, substitute variables, dispatch, collect output → update `current_draft`
     - If it has `role: create` (no-fixer pattern) → re-run the generator with feedback in context → update `current_draft`
   - Go back to step 1 (re-run reviewer)

6. If `NEEDS_REVISION` and `iteration >= max_iterations`:
   - Log: "Достигнут лимит итераций (N). Используем последний черновик."
   - Exit loop with current draft

#### Step with `role: review` WITHOUT `loop_with`

Run the reviewer once as a standalone evaluation. The output is informational only (no looping).

#### Step with `role: enhance` + `run_after: loop`

Skip during the main loop. These are handled in G-5.

### G-5: Run Optional Post-Loop Agents

After the main loop completes, run any steps with `run_after: loop`:

1. Read the agent file
2. Substitute `{{variables}}` (including final `current_draft`)
3. Dispatch via Agent tool
4. Append the agent's output to `current_draft` (separated by a blank line and `---`)

If an optional agent fails (`optional: true`), log the failure and continue. Do not abort.

### G-6: Save Output

**Topic slug rules:**
1. Lowercase the topic
2. Replace spaces with hyphens
3. Strip all non-alphanumeric characters except hyphens
4. Collapse consecutive hyphens into one
5. Truncate to max 50 characters at a word boundary (don't cut mid-word)

**File naming:**
- Primary: `outline-<topic-slug>.md`
- If file exists: `outline-<topic-slug>-2.md`, `outline-<topic-slug>-3.md`, etc.

**Save location:** Current working directory.

Write the final `current_draft` to the output file.

### G-7: Report

Print a summary:
```
Структура презентации готова.

  Пресет:     <preset name or "по умолчанию">
  Формат:     <active format>
  Итерации:   <number of iterations used> / <max_iterations>
  Файл:       <file path>

Для использования с /slidev (если формат slidev):
  /slidev <file path>
```

---

## Create Preset Procedure

### CP-1: Ask Preset Name

Ask the user:
```
Как назвать пресет? (kebab-case, например: investor-pitch, tech-talk)
```

Validate: must be kebab-case (lowercase letters, numbers, hyphens only). If invalid, explain and ask again.

### CP-2: Ask Description

Ask the user:
```
Для чего этот пресет? (краткое описание)
```

### CP-3: Ask Target Audience

Ask the user:
```
Кто целевая аудитория? (например: инвесторы, студенты, команда разработки, широкая публика)
```

### CP-4: Ask Output Format

Ask the user:
```
Формат вывода?
  1. slidev — ## Слайд N: Заголовок + буллиты (совместим с /slidev)
  2. universal — Секции, тезисы, заметки спикера
  3. custom — Вы опишете формат сами

Выбор (1/2/3):
```

If the user chooses "custom" (3), follow up:
```
Опишите формат, в котором генератор должен выдавать структуру:
```

### CP-5: Ask Storage Location

Ask the user:
```
Где сохранить пресет?
  1. глобально — ~/.claude/outline-presets/ (доступен везде)
  2. локально — .outline-presets/ (только в этом проекте)

Выбор (1/2):
```

### CP-6: Ask Additional Context (Optional)

Ask the user:
```
Дополнительный контекст или ограничения? (необязательно — нажмите Enter, чтобы пропустить)
```

### CP-6.5: Collision Check

Now that the storage location is known, check if a preset with this name already exists:

- If global: check `~/.claude/outline-presets/<name>/`
- If local: check `.outline-presets/<name>/`

**CRITICAL:** A preset with the same name in the OTHER location is NOT a collision.

If collision detected:
```
Пресет с именем '<name>' уже существует: <path>

  1. Перезаписать — заменить существующий пресет
  2. Переименовать — выбрать другое имя
  3. Отмена — прекратить создание

Выбор (1/2/3):
```

- Перезаписать → continue, files will be replaced
- Переименовать → go back to CP-1
- Отмена → stop here

### CP-7: Autonomous Pipeline Design

Using the collected information, autonomously design the agent pipeline. Do NOT ask the user for agent details — design everything yourself.

**Design decisions to make:**

1. **How many agents?** Minimum 2 (generator + reviewer). Add a fixer if the audience requires specialized revision logic. Add enhance agents if post-loop processing adds value (e.g., Q&A for educational content).

2. **Agent roles and prompts:** For each agent:
   - Name (kebab-case, descriptive)
   - Role (`create`, `review`, `fix`, `enhance`)
   - Input variables it needs
   - A detailed prompt tailored to the preset's audience, goals, and format

3. **Pipeline design:** Define the `steps` array in `pipeline.md`:
   - Execution order
   - Which agents loop together
   - Stop conditions
   - Optional post-loop agents

4. **Keywords:** Generate comprehensive keywords for `preset.md` based on the description and audience

**Write files to the storage location:**

```
<storage-path>/<name>/
  ├── preset.md
  ├── pipeline.md
  └── agents/
      ├── <agent-1>.md
      ├── <agent-2>.md
      └── ...
```

Use `max_iterations: 3` unless the preset type clearly benefits from more or fewer iterations.

### CP-8: Confirmation Summary

Print:
```
Пресет '<name>' создан.

  Путь:       <full path to preset directory>
  Агенты:     <list of agent names and roles>
  Пайплайн:   <brief flow description>
  Формат:     <format>

Использование:
  /outline --preset <name> <тема>

Или просто /outline <тема> — авто-выбор подберёт этот пресет,
если тема совпадёт с его ключевыми словами.
```

---

## Learn Procedure

### L-1: Parse Arguments

- If `preset` is specified:
  1. Look up by name: local (`.outline-presets/<name>/`) → global (`~/.claude/outline-presets/<name>/`)
  2. If not found, error:
     ```
     Пресет '<name>' не найден.
     Искали в: .outline-presets/<name>/, ~/.claude/outline-presets/<name>/
     ```
     Stop here.
  3. Train only this preset.

- If no preset specified:
  - Scan both local and global storage for all presets
  - If no presets found:
    ```
    Пресетов для обучения не найдено. Сначала создайте пресет:
      /outline --new-preset
    ```
    Stop here.
  - Train all found presets.

### L-2: Generate Test Topics and Run Pipelines

For each preset being trained:

1. Generate N test topics that match the preset's description and keywords. Topics should be diverse — vary industry, scope, and complexity.

2. For each test topic (i = 1 to N):
   a. Run the full Generate Procedure (G-1 through G-7) using this preset and topic
   b. Save the output to `learn-<preset-name>/run-<i>/outline.md`
   c. Save metadata (topic, iterations used, final verdict) to `learn-<preset-name>/run-<i>/meta.md`

### L-3: Critic Analysis

After all N runs complete, construct a critic agent on-the-fly. Dispatch it via the Agent tool with this prompt:

```
You are a demanding presentation structure critic. Analyze N generated
presentation outlines and evaluate the agent pipeline that produced them.

INPUTS:
- Preset metadata: <preset.md content>
- Pipeline: <pipeline.md content>
- Agent prompts: <all agents/*.md contents>
- Generated outlines: <all N outline outputs>
- Run metadata: <all N meta.md files — topics, iterations, verdicts>

ANALYSIS:
1. Evaluate each outline for: structure quality, logical flow, coverage,
   pacing, opening/closing strength
2. Look for SYSTEMIC patterns — issues that appear across multiple runs
3. Evaluate agent effectiveness:
   - Generator: Does it produce good first drafts?
   - Reviewer: Does it catch real issues? Is it too strict or too lenient?
   - Fixer (if any): Does it actually address feedback?
4. Check if the pipeline structure itself is effective:
   - Are there enough agents?
   - Is the loop count appropriate?
   - Would adding/removing agents help?

OUTPUT FORMAT:

# Critic Report: <preset-name>

## Overall Quality: X/10

## Systemic Issues

### Issue 1: [Title]
- **Severity**: critical | major | minor
- **Frequency**: N/N runs affected
- **Description**: What's wrong
- **Root cause**: Which agent's prompt allows this
- **Proposed fix**: Specific change to agent prompt — quote the
  relevant section, show before/after

## Pipeline-Level Suggestions
- [Any suggestions to modify pipeline.md — add/remove agents, change iterations]

## What Works Well
- [Patterns to preserve]
```

### L-4: Propose Changes

Based on the critic's report:

1. Generate a diff-style summary of all proposed changes:
   ```
   Предлагаемые изменения для пресета '<name>':

   1. [agent-name.md] — <brief description of change>
      - Было: "<relevant excerpt>"
      - Стало: "<proposed text>"

   2. [pipeline.md] — <brief description of change>
      - <details>

   Применить изменения? (да / нет / выбрать)
   ```

2. Wait for user confirmation:
   - **да** → apply all changes
   - **нет** → discard all changes
   - **выбрать** → let user pick which changes to apply (number them)

**CRITICAL:** Do NOT apply changes without user confirmation. Always show the diff summary and wait for explicit approval.

### L-5: Apply Changes

For each approved change:

1. Read the target file
2. Apply the modification using the Edit tool
3. Verify the edit was applied correctly

**Failure handling:**
- If an agent produced zero usable output across ALL N runs → mark as "critically broken", do NOT modify it, flag for user attention
- If partial runs failed → apply improvements from successful runs, note failures in report

### L-6: Report

Print a final summary:
```
Обучение завершено для пресета '<name>'.

  Прогоны:       N всего, M успешных
  Изменения:     X применено, Y отложено, Z пропущено (критически сломанные агенты)
  Изменённые файлы:
    - agents/<agent>.md — <what changed>
    - pipeline.md — <what changed> (if applicable)

  Агенты, требующие внимания:
    - <agent-name> — <reason>
```

Clean up: the `learn-<preset-name>/` directory with test outputs can be kept for reference or deleted — ask the user: "Удалить директорию с тестовыми результатами learn-<preset-name>/? (да/нет)"

---

## Utility: Topic Slug Generation

Used by G-6 to create file names from topics.

**Rules:**
1. Convert to lowercase
2. Replace spaces with hyphens
3. Strip all characters that are not alphanumeric or hyphens
4. Collapse consecutive hyphens into a single hyphen
5. Remove leading/trailing hyphens
6. If longer than 50 characters, truncate at the last word boundary before 50 characters

**Examples:**
| Topic | Slug |
|-------|------|
| "Q4 Investor Pitch" | `q4-investor-pitch` |
| "Introduction to Machine Learning: A Primer" | `introduction-to-machine-learning-a-primer` |
| "Why Our Team Needs to Adopt CI/CD Practices ASAP!!!" | `why-our-team-needs-to-adopt-cicd-practices-asap` |
| "A Very Long Topic That Goes On And On And Definitely Exceeds Fifty Characters Limit" | `a-very-long-topic-that-goes-on-and-on-and` |
