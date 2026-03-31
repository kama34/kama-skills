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

Preset already created by FIG-Extract (see `figma-extraction.md`).

**Create education directory**: Scan for existing `edu_*` directories in the working directory. Create the next sequential one:
```bash
# Example: if edu_01/ and edu_02/ exist → create edu_03/
ls -d edu_* 2>/dev/null   # check what exists
mkdir -p edu_03/           # create next sequential
```
If no `edu_*` directories exist, start with `edu_01/`.

Store `fileKey` and `nodeId` list from `source.json` for screenshot comparison in each QA cycle.

## FDL-0: Pixel-Perfect Calibration (learn_0)

**Purpose:** Before learning with diverse outlines, verify that the extracted archetypes + preset can reproduce the original Figma template exactly. This is the "ground truth test" — if the system can't match the original, it can't produce good variations.

### FDL-0a: Build calibration outline from Figma

For each **unique archetype** (one slide per archetype, not all 20 Figma slides), extract the original text content from `blueprint.json` (`characters` fields). Assemble into a calibration outline at `<edu_dir>/learn_0/outline.md`.

Example: if the preset has 15 unique archetypes → calibration outline has 15 slides, each using its archetype's original Figma text.

### FDL-0b: Generate calibration presentation

Run `generation-pipeline.md` with the calibration outline. Each slide must use its corresponding archetype — no composition planning needed, the mapping is 1:1.

Output to `<edu_dir>/learn_0/`.

### FDL-0c: Pixel-perfect QA cycle

Run a **strict variant** of `qa-cycle.md`:
- **Skip all design-rules checks** — no text density, hierarchy, or contrast checks. The goal is pixel-perfect reproduction, not design quality.
- **Run ONLY Figma comparison** (Phase A structural/style + Phase B visual) with **zero tolerance for FAIL/CRITICAL**:
  - ALL properties must be within the tolerance table thresholds
  - Zero element overlap
  - Zero position deviations beyond ±5%
  - Zero font-size deviations beyond ±0.15rem
  - Zero color deviations beyond ΔE 5
- **Pass condition**: every slide passes ALL checks with zero FAIL and zero CRITICAL. This is a checklist, not a score — one failure means another iteration.
- **Fix cycle**: fix issues → re-generate → re-compare. Fixes go to archetype.html + preset.md + flexibility.yaml (same as regular learn).
- Export PDF after each iteration for visual review.

### FDL-0d: Verification from scratch

After FDL-0c achieves zero-FAIL on all slides:

1. **Delete** `<edu_dir>/learn_0/slides.md` and all generated artifacts (keep outline.md)
2. **Re-generate** the calibration presentation from scratch using the updated archetypes/preset — a clean generation with NO manual fixes carried over
3. **Run the same strict QA** (FDL-0c checks)
4. If pixel-perfect **without any QA iterations** → **learn_0 PASSED**
5. If not → return to FDL-0c with the new issues, fix archetypes, repeat verification

### FDL-0e: Commit + report

```bash
git add <edu_dir>/learn_0/
git add .slidev-presets/figmadeck-<name>.preset.md
git add .slidev-presets/figmadeck-<name>-figma/
git commit -m "learn(figmadeck): learn_0 pixel-perfect calibration PASSED"
git tag figmadeck-learn-<edu_dir>-calibration
```

Print:
```
━━━ learn_0: Pixel-Perfect Calibration ━━━

Status: PASSED
QA iterations to achieve pixel-perfect: <N>
Verification from scratch: PASSED (zero issues on first run)
Archetypes calibrated: <count>/<total>
Archetype fixes applied: <list>

Proceeding to learn_1..N with diverse outlines.
```

**If learn_0 fails** after 10 iterations without reaching zero-FAIL → STOP. Report which archetypes/properties cannot be reproduced. Do NOT proceed to learn_1..N — the extraction needs to be re-run or archetypes manually reviewed.

---

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

### FDL-3b2: Export PDF

After QA cycle completes, export the presentation to PDF for review:

```bash
cd <edu_dir>/learn_<i>
npx slidev export --format png --output slides-tmp
python -c "
from PIL import Image
import glob, os
pngs = sorted(glob.glob('slides-tmp/*.png'), key=lambda f: int(os.path.basename(f).split('.')[0]))
if pngs:
    imgs = [Image.open(p).convert('RGB') for p in pngs]
    imgs[0].save('slides.pdf', save_all=True, append_images=imgs[1:])
    print(f'PDF created: {len(imgs)} slides')
"
rm -rf slides-tmp
```

The PDF is saved as `<edu_dir>/learn_<i>/slides.pdf` — can be opened immediately to review the iteration result.

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
