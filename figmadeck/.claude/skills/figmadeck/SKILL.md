---
name: figmadeck
description: Create presentations directly in Figma. Clones a template page, adapts it to an outline by replacing text and reordering slides, then runs QA cycles for design fidelity. Also handles --learn, --export, --edit subcommands.
argument-hint: "[<figma-url> <outline> | <figma-url> --learn=N | --export pdf|png [figma-url] | --edit <figma-url> <comment> | --help]"
---

# Figmadeck — Figma-Native Presentation Generator

Create presentations by cloning and adapting Figma templates directly. No conversion to HTML/CSS — work inside Figma, preserving every gradient, shadow, image, and font exactly.

## References

Before executing, read the relevant reference for the current mode:
- `references/figma-generation.md` — **Generation mode**: clone → analyze → match → fill
- `references/qa-cycle.md` — **QA**: Figma-native structural + visual + design critique cycle
- `references/figma-learning.md` — **Learn mode**: calibration + iterative improvement
- `references/auth.md` — **Authentication**: Playwright login to Figma
- `references/design-rules.md` — **Universal design rules** (readability, spacing, hierarchy)

**MANDATORY**: Before any `use_figma` call, load the `figma-use` skill (from the Figma MCP plugin). It contains critical Plugin API rules.

## Input Parsing

### Help

**`--help`**: Display usage and stop:

```
Figmadeck — Figma-Native Presentation Generator

Usage:
  /figmadeck <figma-url> <outline>          Create presentation in Figma
  /figmadeck <figma-url> --learn=N          Calibration + learning (N cycles)
  /figmadeck --export pdf|png [figma-url]   Export via Playwright
  /figmadeck --edit <figma-url> <comment>   Edit existing generated page
  /figmadeck --help                         Show this help
```

### Subcommands

**`--export <format> [figma-url]`**: Export presentation.
1. Run auth check (`references/auth.md`)
2. Playwright: open Figma file → navigate to generated page ("Generated: ...")
3. For `pdf`: File → Export PDF, or Presentation Mode → Print to PDF
4. For `png`: `get_screenshot` per slide → save locally
5. Fallback: export each frame via `get_screenshot` → combine to PDF via Python/Pillow

**`--edit <figma-url> <comment>`**: Edit existing presentation.
1. Open Figma file, find generated page (name prefix "Generated:")
2. Read user's edit comment
3. Apply changes via `use_figma`
4. Run QA cycle (`references/qa-cycle.md`) to validate

### Mode Detection

1. **Figma URL + `--learn=N`** → Learning mode: read `references/figma-learning.md`. Max N: 10.
2. **Figma URL + outline** → Generation mode: read `references/figma-generation.md`, then `references/qa-cycle.md`.
3. **`--export`** → Export mode: read `references/auth.md`, execute export.
4. **`--edit`** → Edit mode: find generated page, apply changes, run QA.

### URL Parsing

Extract `fileKey` from Figma URL:
- `figma.com/design/:fileKey/:fileName` → fileKey
- `figma.com/design/:fileKey/branch/:branchKey/:fileName` → use branchKey
- If URL is not `figma.com/design/...` → error

## Hard Constraint

**The generated presentation MUST have exactly the same number of slides, in exactly the same order, with exactly the same content as the outline.** Never add, remove, merge, or reorder slides beyond what the outline specifies.

### Content Adaptation

When outline content is longer than the template placeholder text:
1. **Shorten/rephrase** to fit (preserve core meaning)
2. **textAutoResize = "HEIGHT"** to let text grow
3. **Reduce fontSize** (minimum = current × 0.85)
4. Last resort: move overflow detail to a note

## Autonomous Execution

**CRITICAL:** Execute all steps autonomously without stopping for confirmation. If blocked, attempt to resolve (2-3 attempts). Only stop if truly unresolvable.
