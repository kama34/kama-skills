# Figma Learning Procedure (FDL)

Triggered by `/figmadeck <URL> --learn=N`. Uses the same QA cycle as regular generation, but fixes propagate to archetypes permanently. Maximum N: 10.

## Regular vs Learn

| | Regular Generation | Learn Mode |
|---|---|---|
| Presentations | 1 | N (diverse outlines) |
| Fixes go to | slides.md (one-time) | archetype.html + preset.md + flexibility.yaml (permanent) |
| Figma comparison | qa-cycle.md (same) | qa-cycle.md (same) |
| Result | Ready presentation | Improved archetypes for future |

## FDL-1: Initialization

Preset already created by FIG-Extract (see `figma-extraction.md`). Create next sequential `edu_XX/` directory under the working area. Store `fileKey` and `nodeId` list from `source.json` for screenshot comparison in each QA cycle.

## FDL-2: Generate N Diverse Outlines

All outlines in Russian. Must vary across:

- **Industries**: tech, education, healthcare, finance, creative, nonprofit, SaaS, retail, AI/ML, sustainability
- **Formats**: pitch, lecture, product launch, report, onboarding, keynote
- **Sizes**: 8-10 slides (short), 12-14 slides (medium), 15-16 slides (long)
- **Tone**: formal, casual, inspirational, data-heavy, storytelling, technical

Save each outline to `edu_dir/learn_i/outline.md` before the learning cycle begins.

## FDL-3: Learning Cycle (i = 1..N)

### FDL-3a: Generate Presentation

Launch subagent to run `generation-pipeline.md`. Re-read `.preset.md` from disk before each iteration — it may have been modified by a previous cycle's systemic fixes. Use outline from `learn_i/outline.md`. Output all artifacts to `learn_i/`.

### FDL-3b: Run QA Cycle

Run `qa-cycle.md` until Fidelity >= 9/10. This is the same iterative Figma comparison loop as regular generation — screenshot each slide, compare against source node, identify deltas, apply fixes.

### FDL-3c: Extract Systemic Fixes

**KEY STEP.** Analyze which fixes from the QA cycle were systemic vs. content-specific.

**Systemic fix** = the same issue appeared on multiple slides using the same archetype, OR the fix changes a CSS value that is hardcoded in `archetype.html`.

Content-specific fix = the fix only corrects a text value, image, or data point unique to this presentation — do NOT propagate these.

Apply systemic fixes to:
- `archetype.html` — layout, positioning, grid structure
- `figmadeck-<name>.preset.md` CSS block — colors, fonts, spacing constants
- `flexibility.yaml` — if scaling or flex rules were wrong

### FDL-3d: Intermediate Report

Print after each completed iteration:

```
━━━ Figma Learning: Итерация <i>/<N> ━━━

Figma Fidelity: X/10
Systemic fixes applied: <count>
  - [archetype: <name>] <description>
Archetype changes: <list or "none">
Flexibility updates: <list or "none">
```

### FDL-3e: Git Commit + Tag

Stage all artifacts from this iteration:

```bash
git add edu_dir/learn_i/
git add .slidev-presets/figmadeck-<name>.preset.md
git add .slidev-presets/figmadeck-<name>-figma/
git commit -m "learn(figmadeck): iteration i/N — fidelity X/10"
git tag figmadeck-learn-edu_dir-iter-i
```

## FDL-4: Convergence

If Fidelity >= 9/10 for **two consecutive cycles** → early stop.

Print: `"Раннее завершение: fidelity стабилизировался на X/10 в циклах c-1 и c."`

If score decreased from the previous cycle → warn but do not stop. Continue learning.

## FDL-5: Final Report

```
# Figma Learning Report

## Source: <Figma URL>
## Cycles: <actual> / <N planned>
## Early stop: yes/no (reason)
## Final Fidelity: X/10

## Fidelity Progression
Cycle 1: X/10
Cycle 2: X/10
...

## Archetype Changes Summary
- figmadeck-<name>: <N> fixes (<list>)
...

## Flexibility Rules Updated
- <archetype>: <what changed>
...

## Final Preset State
- Path: .slidev-presets/figmadeck-<name>.preset.md
- Archetypes: <N>
- Theme: .slidev-presets/figmadeck-<name>-theme/
```
