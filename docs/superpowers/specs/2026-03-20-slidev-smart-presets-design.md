# Slidev: Smart Preset Generation

**Date:** 2026-03-20
**Scope:** Add learn/deep_learn modes for preset creation, auto-preset generation before presentation, `--no-preset` flag

## Problem

Slidev's preset system is static — presets are created via a one-shot wizard (`--create-preset`) or manually. There's no iterative refinement based on visual results. When generating a presentation without `--preset`, the skill falls back to Unique mode (ad-hoc styling) with no attempt to find or create a suitable preset. This leads to inconsistent quality and missed opportunities to reuse good design systems.

## Solution

Three interconnected features:

1. **Auto-preset before generation** — LLM matches topic against existing presets; if no match, creates and refines one via deep_learn=3
2. **`--learn=N`** — create a preset and refine it through N visual test runs with user-confirmed changes
3. **`--deep_learn=N`** — create a preset and auto-refine it through N cycles of 3 visual test runs with convergence detection

### 1. Auto-Preset Generation (Step 0)

When user calls `/slidev <topic>` without `--preset` and without `--no-preset`:

**Step 0.1: Scan existing presets**
Collect all `.preset.md` files from:
- `.slidev-presets/` (local)
- `~/.claude/slidev-presets/` (global)
- `~/.claude/slidev-presets.json` (registry)

**Step 0.2: LLM matching**
Pass the presentation topic + list of presets (name + aesthetic description) to LLM. Output:
- `MATCH: <preset-name>` — suitable preset found
- `NO_MATCH` — no suitable preset

**Step 0.3: If MATCH**
Load the matched preset, continue as `--preset <name>`.

**Step 0.4: If NO_MATCH**
- Generate an initial preset based on the topic (mood, colors, fonts, CSS)
- Run **deep_learn=3** on this preset — 3 cycles of visual critique and auto-refinement (inline variant: runs PDL-1 through PDL-5 silently, skips PDL-6 save prompt and PDL-7 cleanup prompt — preset is saved to `.slidev-presets/` automatically, working directory is cleaned up automatically)
- Continue presentation generation with this preset

**`--no-preset` flag:** Skips Step 0 entirely. Generation proceeds in Unique mode (current default behavior).

### 2. `--learn=N` for Presets

**Command:** `/slidev --learn=N` or `/slidev --learn=N --preset <name>`

**PL-1: Initialization**
- If `--preset` specified: create initial preset from name/description
- If not specified: interactive wizard (7 questions, same as current `--create-preset`)
- Create working directory `preset-learn-<name>/`
- Scaffold once: `package.json` + `npm install` + `npx playwright install chromium`

**PL-2: Generate demo presentations**
- Generate N diverse outlines (varied topics, formats, tones) using `assets/demo-outline.md` as base
- For each: apply current preset → write `slides.md` + `styles/index.css` → export PNG
- Reuse scaffolding between runs (only change slides.md + index.css)

**PL-3: Visual critic**
- Subagent receives: all PNGs from N runs + current `.preset.md` + scoring-subroutine.md
- Scores on 6 axes: visual impact, layout uniqueness, typography drama, color conviction, content clarity, decorative quality
- Outputs: overall score, systemic CSS/font/color issues, specific before/after proposals for `.preset.md`

**PL-4: Propose changes**
- Display numbered list of edits with before/after
- User chooses: `yes` / `no` / `select` (by number)

**PL-5: Apply**
- Update `.preset.md` (YAML frontmatter + CSS)
- Only styles — no structural changes

**PL-6: Report**
- Final score, changes applied, changes skipped

### 3. `--deep_learn=N` for Presets

**Command:** `/slidev --deep_learn=N` or `/slidev --deep_learn=N --preset <name>`

**PDL-1: Initialization**
- N >= 2 (minimum 2 cycles). If N < 2, error and stop.
- Create preset (from `--preset` or wizard)
- Working directory: `preset-deep-learn-<name>/`
- Snapshot original preset to `preset-snapshot-original/`
- Scaffold once: `package.json` + `npm install` + `npx playwright install chromium`

**PDL-2: Training cycle (repeated N times)**

- **PDL-2.1:** Generate 3 diverse outlines (topics MUST NOT repeat across cycles)
- **PDL-2.2:** For each: update only `slides.md` + `styles/index.css` from current preset → export PNG. Reuse scaffolding.
- **PDL-2.3:** Visual critic receives PNGs from all 3 runs + current preset + (for cycle > 1) previous critic report. Scores on 6 axes. Persisting issues from previous cycle get **severity escalation**. New issues after fixes get flagged as **REGRESSION**.
- **PDL-2.4:** Auto-apply: `critical`/`major` fixes applied without confirmation. `minor` — auto-applied only if they touch a single CSS property or font value; otherwise skipped. Log to `cycle-<c>/changes-applied.md`.
- **PDL-2.5:** Cycle status: score, runs, changes applied, regressions.

**PDL-3: Safety guardrails**
- Changes only to `.preset.md` (CSS + YAML frontmatter)
- NEVER delete the preset or change its name
- If an edit cannot be applied — skip, log, continue

**PDL-4: Convergence (early stopping)**
- Score >= 9 for two consecutive cycles → stop early
- Score regression (decreased vs previous): warn but continue training

**PDL-5: Final report**
- Score progression across cycles, all changes, regressions
- Diff of original preset vs final (from snapshot)

**PDL-6: Save**
- Final preset saved to `.slidev-presets/` (local) or `~/.claude/slidev-presets/` (global — ask user)

**PDL-7: Cleanup**
- Ask user: delete working directory?

## Render Optimization

All modes share a single scaffolding optimization:
- `package.json` + `npm install` + `npx playwright install chromium` — done **once** per learn/deep_learn session
- Between runs/cycles: only `slides.md` and `styles/index.css` are updated
- Export via `npx slidev export --format png` reuses installed dependencies
- This reduces per-run overhead from ~30s (full setup) to ~5s (export only)

## Files Changed

| File | Change |
|------|--------|
| `slidev/.claude/skills/slidev/SKILL.md` | Add Step 0 (auto-preset), `--no-preset` flag, `--learn=N` preset mode, `--deep_learn=N` preset mode, render optimization |

All changes are in SKILL.md — no new reference files needed. The learn/deep_learn procedures follow the same subagent dispatch pattern already used by the existing `--learn=N` mode (which improves SKILL.md). The visual critic uses the existing `references/scoring-subroutine.md` (already present in the skill directory — defines the 6-axis scoring scale from 1 to 10).

## Design Rationale

- **Why deep_learn=3 for auto-generation?** A one-shot preset has no visual validation. 3 cycles of critique produce a battle-tested preset before the actual presentation. The overhead (3 cycles × 3 demos = 9 renders) pays off with a reliably good visual foundation.
- **Why LLM matching over keyword matching?** Presentation topics are diverse and nuanced. "AI in Healthcare" might match a "tech" preset or a "medical" preset — LLM judgment handles this better than keyword overlap.
- **Why reuse scaffolding?** npm install + playwright install is the slowest part (~20-30s). Doing it once and only swapping CSS/slides between runs makes learn/deep_learn practical for N > 3.
- **Why only modify `.preset.md`?** Presets are self-contained style definitions. The critic should improve colors, fonts, CSS patterns — not change the skill's generation logic (that's what the existing `--learn` does).
