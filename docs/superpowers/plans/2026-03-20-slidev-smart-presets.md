# Slidev Smart Preset Generation — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add smart preset generation to the slidev skill: auto-preset before generation with LLM matching, --learn=N for preset creation with visual critique, --deep_learn=N for iterative auto-refinement, and --no-preset flag.

**Architecture:** All changes in a single file (`SKILL.md`). Four logical sections: (1) frontmatter + help updates, (2) auto-preset Step 0 with --no-preset flag, (3) --learn=N preset learning procedure, (4) --deep_learn=N preset deep learning procedure. The existing `--learn=N` (which improves SKILL.md itself) remains unchanged — the new preset learn triggers when `--preset` is also specified.

**Tech Stack:** Markdown prompt files (LLM agent instructions, no code)

**Spec:** `docs/superpowers/specs/2026-03-20-slidev-smart-presets-design.md`

---

### Task 1: Update frontmatter and help text

**Files:**
- Modify: `slidev/.claude/skills/slidev/SKILL.md:3-4` (frontmatter argument-hint)
- Modify: `slidev/.claude/skills/slidev/SKILL.md:36-56` (help table)

- [ ] **Step 1: Update argument-hint in frontmatter**

Change line 4 from:
```
argument-hint: "[--help | --dev [dir] | --export <format> [dir] | --edit [dir] <comment> | --picture [auto|paths...] [dir] | --create-preset <name> | --learn=N | --preset <name> | style: <desc>] <outline or file path>"
```
to:
```
argument-hint: "[--help | --dev [dir] | --export <format> [dir] | --edit [dir] <comment> | --picture [auto|paths...] [dir] | --create-preset <name> | --learn=N | --deep_learn=N | --no-preset | --preset <name> | style: <desc>] <outline or file path>"
```

- [ ] **Step 2: Add new commands to help table**

In the help text block (lines 36-56), add these lines after the `--learn=N` line and before the `--help` line:

```
  /slidev --learn=N --preset <name>            Preset learning (create + refine with visual critic)
  /slidev --deep_learn=N                       Preset deep learning (auto-refine N cycles)
  /slidev --deep_learn=N --preset <name>       Deep learn a specific preset
  /slidev --no-preset <outline>                Generate without auto-preset (Unique mode)
```

- [ ] **Step 3: Verify the frontmatter and help table**

Read lines 1-60 and confirm:
- Frontmatter `argument-hint` includes `--deep_learn=N`, `--no-preset`
- Help table has all new commands listed
- Existing commands are untouched

- [ ] **Step 4: Commit**

```bash
git add slidev/.claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): add smart preset flags to frontmatter and help"
```

---

### Task 2: Add --no-preset flag and Step 0 (Auto-Preset) to generation flow

**Files:**
- Modify: `slidev/.claude/skills/slidev/SKILL.md:630-634` (Generation Modes section)

- [ ] **Step 1: Add Step 0 and --no-preset to Generation Modes**

Find the section "### Generation Modes" (line 630). Replace the current content:

```markdown
### Generation Modes

1. **Preset mode**: Input contains `--preset <name|path>` → extract preset identifier, remainder is outline
2. **Custom style mode**: Input starts with `style:` → extract style description, remainder is outline
3. **Unique mode**: No flags → generate a completely unique design
```

with:

```markdown
### Generation Modes

**`--no-preset` flag**: If present, skip Step 0 entirely and proceed directly to mode selection below.

#### Step 0: Auto-Preset (runs before mode selection if no `--preset`, no `--no-preset`, and no `style:` prefix)

When the user calls `/slidev <topic>` without explicit style flags:

**Step 0.1: Scan existing presets** — Collect all `.preset.md` files from:
- `.slidev-presets/` (local project directory)
- `~/.claude/slidev-presets/` (global)
- `~/.claude/slidev-presets.json` (registry — read JSON, resolve all mapped paths)

If no presets found anywhere, skip to Step 0.4 (create new).

**Step 0.2: LLM matching** — Evaluate the presentation topic against each preset's name and aesthetic description. For each preset, consider: does this preset's mood, color scheme, and visual style fit the topic? Output one of:
- `MATCH: <preset-name>` — a suitable preset was found
- `NO_MATCH` — no existing preset fits this topic

**Step 0.3: If MATCH** — Load the matched preset using the standard Preset Resolution (4-tier lookup). Continue to mode "Preset mode" below.

**Step 0.4: If NO_MATCH (or no presets exist)** — Create and refine a new preset:
1. Generate an initial `.preset.md` based on the topic — infer mood, colors, fonts, CSS from the presentation subject (e.g., a tech startup pitch → bold modern with dark theme; a healthcare lecture → clean professional with calming palette)
2. Save it to `.slidev-presets/<inferred-name>.preset.md` (local)
3. Run the **Preset Deep Learn Procedure (PDL-1 through PDL-5)** with N=3 as an inline variant:
   - PDL-6 (save prompt) is skipped — preset is already saved locally
   - PDL-7 (cleanup prompt) is skipped — working directory is cleaned up automatically
   - All other steps (scaffolding, 3 cycles of visual critique, auto-apply, convergence) run normally
4. Continue to mode "Preset mode" with the refined preset

#### Mode Selection

1. **Preset mode**: Input contains `--preset <name|path>` (or auto-preset matched/created one) → extract preset identifier, remainder is outline
2. **Custom style mode**: Input starts with `style:` → extract style description, remainder is outline
3. **Unique mode**: `--no-preset` flag present → generate a completely unique design (current default behavior, no preset involvement)
```

- [ ] **Step 2: Verify the Generation Modes section**

Read the Generation Modes section and confirm:
- Step 0 flow is complete (scan → match → create if needed)
- `--no-preset` skips Step 0
- Mode Selection lists all 3 modes correctly
- The rest of the file below is untouched (Outline Source, Hard Constraint, etc.)

- [ ] **Step 3: Commit**

```bash
git add slidev/.claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): add auto-preset Step 0 and --no-preset flag"
```

---

### Task 3: Add --learn=N --preset preset learning procedure (PL-1 to PL-6)

**Files:**
- Modify: `slidev/.claude/skills/slidev/SKILL.md:79` (--learn=N subcommand description)
- Modify: `slidev/.claude/skills/slidev/SKILL.md` (insert PL procedure after existing Learning Loop Procedure, before Visual QA Loop)

- [ ] **Step 1: Update --learn=N subcommand to branch on --preset**

Find line 79:
```
**`--learn=N`**: Self-improving learning loop. Parse N from the argument (e.g., `--learn=5`). Follow the Learning Loop Procedure (L-1 through L-5). Stop here — do not proceed to generation.
```

Replace with:
```
**`--learn=N`**: Learning loop. Parse N from the argument (e.g., `--learn=5`).
- **Without `--preset`**: Self-improving skill loop. Follow the Learning Loop Procedure (L-1 through L-5) — improves SKILL.md and design-principles.md based on visual critique.
- **With `--preset <name>`**: Preset learning loop. Creates (or uses named) preset, generates N demo presentations, visual critic evaluates and proposes CSS/font/color improvements. Follow the Preset Learning Procedure (PL-1 through PL-6).

Stop here — do not proceed to generation.
```

- [ ] **Step 2: Insert PL-1 through PL-6 procedure**

Insert the following AFTER the existing L-5 report section (after the line "Stop here — do not proceed to generation." around line 493) and BEFORE the "## Visual QA Loop" section (line 495):

```markdown

### Preset Learning Procedure

Triggered by `--learn=N --preset <name>` or `--learn=N` (with preset specified). Creates/refines a preset through N visual test runs with user-confirmed improvements.

**PL-1: Initialization**
- If `--preset <name>` specified: generate an initial `.preset.md` from the name — infer mood, colors, fonts, CSS from the name/description. Save to `.slidev-presets/<name>.preset.md`.
- If `--preset` not specified: run the interactive wizard (7 questions, same as `--create-preset`) to create the initial preset.
- Create working directory: `preset-learn-<name>/`
- Scaffold the Slidev project once inside the working directory:
  - Write `package.json` with standard Slidev deps (`@slidev/cli: latest`, `@slidev/theme-default: latest`)
  - Run `npm install`
  - Run `npx playwright install chromium`
  - This scaffolding is reused for ALL N runs — only `slides.md` and `styles/index.css` change between runs.

**PL-2: Generate demo presentations**
- Generate N diverse outlines (ALL in Russian). Vary across industries, formats, sizes (8-16 slides), and tones. Use `assets/demo-outline.md` as structural reference.
- For each outline i = 1 to N:
  1. Write `slides.md` by running the full generation procedure (Steps 1-8) using the current preset in Preset mode. Output to `preset-learn-<name>/run-<i>/`.
  2. Apply the current preset's CSS to `styles/index.css`.
  3. Export PNGs: `cd preset-learn-<name>/run-<i> && npx slidev export --format png --output slides`
  4. **Optimization**: Copy `node_modules/` from the scaffolded project to each run directory via symlink or reuse — do NOT run `npm install` for every run. The simplest approach: run all generations in the same scaffolded directory, moving `slides.md` and `styles/index.css` between runs, and copying exported PNGs to `run-<i>/slides/`.

**PL-3: Visual critic**
- Launch a subagent (Agent tool) as a **demanding visual design critic** for presets. Provide:
  - All exported PNGs from all N runs (read ALL visually)
  - The current `.preset.md` file content
  - `references/scoring-subroutine.md` — apply the 6-axis scoring (1-10 scale): visual impact, layout uniqueness, typography drama, color conviction, content clarity, decorative quality
  - `references/design-principles.md` — check compliance

- Critic output — write to `preset-learn-<name>/critic-report.md`:

```
# Preset Critic Report: <name>

## Overall Score: X/10

## Scoring Per Run
- Run 1 ([topic]): X/10 — [strongest axis], [weakest axis]
- Run 2 ([topic]): X/10 — ...
...

## Systemic CSS/Style Issues

### Issue 1: [Title]
- **Severity**: critical | major | minor
- **Frequency**: N/N runs affected
- **Description**: What's wrong visually
- **Evidence**: Which PNGs show the problem
- **Root cause**: Which part of .preset.md causes this
- **Proposed fix**:
  - **Before**: [relevant excerpt from .preset.md]
  - **After**: [proposed replacement text]

## What Works Well
- [list CSS patterns, font choices, color decisions that scored well]
```

**PL-4: Propose changes**
- Read the critic report. Present a numbered list of proposed changes to the user:
```
Предлагаемые изменения для пресета '<name>':
1. [description] — Severity: critical
   Было: "<excerpt>"
   Стало: "<proposed text>"
2. [description] — Severity: major
   ...

Применить изменения? (да / нет / выбрать)
```
- `да` — apply all
- `нет` — discard all
- `выбрать` — user picks by number

**PL-5: Apply**
- For each approved change: read `.preset.md`, apply via Edit tool, verify.
- Only modify `.preset.md` (YAML frontmatter + CSS block). Do NOT change preset name.

**PL-6: Report**
```
Preset learning complete: <name>

  Runs: N
  Score: X/10
  Changes applied: N
  Changes skipped: N
  Preset: .slidev-presets/<name>.preset.md
```

Stop here — do not proceed to generation.

```

- [ ] **Step 3: Verify the procedure**

Read the new PL section and confirm:
- PL-1 through PL-6 are all present and complete
- The section is correctly placed between the existing L-5 and Visual QA Loop
- No disruption to surrounding sections

- [ ] **Step 4: Commit**

```bash
git add slidev/.claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): add --learn=N --preset preset learning procedure"
```

---

### Task 4: Add --deep_learn=N preset deep learning procedure (PDL-1 to PDL-7)

**Files:**
- Modify: `slidev/.claude/skills/slidev/SKILL.md` (add subcommand after --learn=N, insert PDL procedure after PL-6)

- [ ] **Step 1: Add --deep_learn=N subcommand**

Insert after the updated `--learn=N` subcommand block (after "Stop here — do not proceed to generation.") and before the `--polish=N` subcommand:

```markdown

**`--deep_learn=N`**: Preset deep learning loop. Creates (or uses named) preset, then iteratively auto-refines it through N cycles of 3 visual test runs with convergence detection. N must be >= 2.
- **With `--preset <name>`**: deep learn a specific preset
- **Without `--preset`**: interactive wizard creates the initial preset (same as `--create-preset`)

Follow the Preset Deep Learning Procedure (PDL-1 through PDL-7). Stop here — do not proceed to generation.
```

- [ ] **Step 2: Insert PDL-1 through PDL-7 procedure**

Insert AFTER the PL-6 report section (after "Stop here — do not proceed to generation.") and BEFORE the "## Visual QA Loop" section:

```markdown

### Preset Deep Learning Procedure

Triggered by `--deep_learn=N` (with or without `--preset <name>`). Creates/refines a preset through N cycles of automated visual critique and improvement. Also used internally by Step 0.4 (auto-preset) as an inline variant with N=3.

**PDL-1: Initialization**
- Parse N. If N < 2, error: `--deep_learn requires N >= 2 (minimum two cycles to observe improvement).` Stop.
- If `--preset <name>` specified: generate initial `.preset.md` from the name. Save to `.slidev-presets/<name>.preset.md`.
- If `--preset` not specified: run the interactive wizard (7 questions) to create the initial preset.
- If called as inline variant from Step 0.4: the initial preset is already created — skip wizard.
- Create working directory: `preset-deep-learn-<name>/`
- Snapshot the original preset: copy `.preset.md` to `preset-deep-learn-<name>/preset-snapshot-original.preset.md`
- Scaffold the Slidev project once inside the working directory:
  - Write `package.json` with standard Slidev deps
  - Run `npm install`
  - Run `npx playwright install chromium`
  - This scaffolding is reused for ALL cycles and runs.

**PDL-2: Training cycle** — Repeat for c = 1 to N:

**PDL-2.1: Generate outlines** — Generate 3 diverse outlines (ALL in Russian). Topics MUST NOT repeat across cycles. Vary: industry, scope, complexity, geography.

**PDL-2.2: Run presentations** — For each of the 3 outlines:
1. Re-read `.preset.md` from disk (it may have been modified by the previous cycle)
2. Write `slides.md` using the full generation procedure (Steps 1-8) with the current preset in Preset mode
3. Update `styles/index.css` from the current preset's CSS block
4. Export PNGs: `npx slidev export --format png --output slides`
5. Copy PNGs to `preset-deep-learn-<name>/cycle-<c>/run-<i>/slides/`
6. **Optimization**: Reuse the scaffolded `node_modules/` — only swap `slides.md` and `styles/index.css` between runs.

**PDL-2.3: Visual critic** — Launch a subagent as a demanding visual critic. Provide:
- All PNGs from the 3 runs in this cycle
- Current `.preset.md` content
- `references/scoring-subroutine.md` and `references/design-principles.md`
- **For cycle > 1**: also provide the previous cycle's critic report (`cycle-<c-1>/critic-report.md`). Instruct the critic to:
  - Check whether issues from the previous cycle were fixed
  - If an issue persists despite a fix attempt: **escalate its severity** (minor → major, major → critical)
  - If new issues appeared after fixes: flag as **REGRESSION**

Critic output — write to `preset-deep-learn-<name>/cycle-<c>/critic-report.md` (same format as PL-3 critic, plus escalation/regression annotations).

**PDL-2.4: Auto-apply changes** — **CRITICAL: Changes are applied automatically without user confirmation.**
- `critical` severity: always apply
- `major` severity: always apply
- `minor` severity: auto-apply only if the fix touches a single CSS property or font value; otherwise skip and log as deferred

For each change: read `.preset.md`, apply via Edit tool, verify the edit took effect.

Log all changes (applied and skipped) to `preset-deep-learn-<name>/cycle-<c>/changes-applied.md`:
```
# Cycle <c> Changes

## Applied
1. [description] — severity: critical
   Before: "<excerpt>"
   After: "<new text>"

## Skipped
1. [description] — severity: minor, reason: multi-property change
```

**Safety guardrails (NEVER violated):**
- Changes ONLY to `.preset.md` (CSS + YAML frontmatter)
- NEVER delete the preset file
- NEVER change the preset's `name` field
- If an Edit fails (old_string not found in file): log as skipped, continue to next change

**PDL-2.5: Cycle status** — Print:
```
Цикл <c>/<N> завершён.
  Качество:    <score>/10
  Прогоны:     3/3 успешных
  Правки:      <X applied, Y skipped>
  Регрессии:   <count or "нет">
```

**PDL-3: Convergence detection (early stopping)** — After each cycle's status, check:
- If the critic's overall quality score is **9 or 10 for two consecutive cycles**: stop early.
  ```
  Раннее завершение: качество стабилизировалось на <score>/10 в циклах <c-1> и <c>.
  ```
  Skip remaining cycles, proceed to PDL-5.
- If score decreased vs. previous cycle (regression): warn but do NOT stop — the next cycle will attempt to fix it.

**PDL-4: (reserved for future use)**

**PDL-5: Final report** — Write to `preset-deep-learn-<name>/final-report.md` and print:
```
# Preset Deep Learning Report: <name>

## Summary
- Cycles executed: <actual> / <N planned>
- Early stop: yes/no (reason)
- Final score: X/10

## Score Progression
Cycle 1: ██████░░░░ 6.2
Cycle 2: ████████░░ 7.8
Cycle 3: █████████░ 9.1

## Total Changes
- Applied: N
- Skipped: N
- Regressions: N

## Preset Diff (original → final)
[Show before/after of key sections of .preset.md that changed]
```

**PDL-6: Save** — Ask the user where to save the final preset:
```
Пресет '<name>' готов. Сохранить:
1. Локально: .slidev-presets/<name>.preset.md (уже сохранён)
2. Глобально: ~/.claude/slidev-presets/<name>.preset.md

Выбор (1/2):
```
If global: copy the preset to `~/.claude/slidev-presets/` and add to registry if `~/.claude/slidev-presets.json` exists.

**Note**: When called as inline variant from Step 0.4, PDL-6 is skipped — preset stays in `.slidev-presets/` automatically.

**PDL-7: Cleanup** — Ask user: `Удалить рабочую директорию preset-deep-learn-<name>/? (да/нет)`

**Note**: When called as inline variant from Step 0.4, PDL-7 is skipped — working directory is cleaned up automatically.

Stop here — do not proceed to generation (unless called as inline variant from Step 0.4, in which case return to Step 0.4 flow).

```

- [ ] **Step 3: Verify the complete addition**

Read the full new sections and confirm:
- `--deep_learn=N` subcommand is listed after `--learn=N`
- PDL-1 through PDL-7 are all present
- Safety guardrails are present
- Convergence detection is present
- Inline variant notes for Step 0.4 are present
- The section is correctly placed between PL-6 and Visual QA Loop
- No disruption to surrounding sections

- [ ] **Step 4: Commit**

```bash
git add slidev/.claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): add --deep_learn=N preset deep learning procedure"
```
