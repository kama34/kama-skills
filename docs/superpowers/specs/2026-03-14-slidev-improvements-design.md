# Slidev Skill Improvements — Design Spec

**Date**: 2026-03-14
**Scope**: 11 improvements to the slidev presentation generator skill
**Architecture**: Shared subroutines in references/, SKILL.md as hub

## Overview

Add iterative polish cycle, content quality review, A/B testing, preset auto-capture, design memory, improved --learn, --compare, --notes, --responsive, --theme support, and progressive export to the existing slidev skill.

## Architecture Decision

**Pattern**: Shared subroutines (approach B). Heavy procedures live in `references/` files. SKILL.md references them by name ("Run the Scoring Subroutine for `<dir>`"). This keeps SKILL.md under ~1250 lines while total reference material grows to ~2000 lines.

**Design memory location**: `~/.claude/slidev-design-memory.json` (global, not per-project).

**New subcommands**: `--polish=N`, `--compare <dir1> <dir2>`, `--notes [dir]`, `--responsive [dir]`, `--theme <name>` (modifier).

**Internal mechanisms** (not subcommands): A/B testing, content review, preset auto-capture, design memory, progressive export, improved --learn metrics.

## New File Structure

```
references/
  # Existing (unchanged):
  slidev-syntax.md
  slidev-layouts.md
  slidev-animations.md
  preset-format.md
  layout-css-patterns.md
  design-principles.md

  # New subroutines:
  scoring-subroutine.md          # ~80 lines
  content-review-subroutine.md   # ~60 lines

  # New procedures:
  polish-procedure.md            # ~120 lines
  ab-testing.md                  # ~70 lines
  design-memory.md               # ~50 lines
  compare-procedure.md           # ~40 lines
  notes-procedure.md             # ~40 lines
  responsive-check.md            # ~30 lines
```

## Implementation Phases

- **Phase 1** (core): Scoring Subroutine, Content Review, Export Subroutine improvements, `--polish=N`, A/B testing, Preset auto-capture
- **Phase 2** (extensions): Design Memory, Improved `--learn`, `--compare`, progressive export integration
- **Phase 3** (nice-to-have): `--theme`, `--notes`, `--responsive`

---

## Section 1: Shared Subroutines

### 1.1 Scoring Subroutine (`references/scoring-subroutine.md`)

**Input**: `<dir>` — project directory with exported PNGs in `slides-qa/`.

**Process**: Read every exported PNG. For each slide, score 1-10 on 6 axes:

| Axis | What it evaluates |
|---|---|
| Visual impact | First impression, memorability, "would I remember this slide?" |
| Layout uniqueness | Structural difference from neighboring slides |
| Typography drama | Scale contrast, hero-sized numbers, weight pairing |
| Color conviction | Bold intentional palette vs timid/generic |
| Content clarity | Main message readable in 3 seconds |
| Decorative quality | Visible decorative elements, visual personality |

**Output**: Score report written to `<dir>/score-report.md`:

```markdown
# Score Report

## Per-Slide Scores

| Slide | Impact | Layout | Typo | Color | Content | Decor | AVG |
|-------|--------|--------|------|-------|---------|-------|-----|
| 1     | 8      | 9      | 7    | 8     | 9       | 6     | 7.8 |
| 2     | 6      | 5      | 7    | 7     | 8       | 5     | 6.3 |
...

## Overall: 7.8/10

## Weakest Slides
- Slide 2 (avg 6.3): low layout uniqueness, weak decoration
- Slide 7 (avg 6.8): typography flat, content unclear

## Strongest Slides
- Slide 1 (avg 7.8): strong first impression
- Slide 5 (avg 9.1): excellent typography drama
```

**Thresholds**:
- Slide avg < 7 → "weak" — candidate for redesign in polish
- Slide avg >= 9 → "strong" — do not touch
- Overall avg >= 9 → early exit from polish cycle

**Usage**: Called by `--polish`, `--learn` critic, `--compare`.

### 1.2 Content Review Subroutine (`references/content-review-subroutine.md`)

**Input**: `<dir>` — project directory.

**Process**: Read `slides.md` and exported PNGs. Check 5 aspects:

1. **3-second test** — for each slide: can you understand the main message in 3 seconds? If the slide has too much text, competing focal points, or unclear hierarchy → flag it.

2. **Narrative flow** — read slides in sequence. Check for logical progression: problem → solution → evidence → CTA. Flag gaps: "Slide 4 introduces a solution but slide 3 doesn't establish a problem." Flag jumps: "Slide 6 shows traction data but the product hasn't been explained yet."

3. **Redundancy** — do any slides repeat the same information? Flag: "Slide 5 metric ($1.5M ARR) already shown on slide 4."

4. **CTA clarity** — on the Ask/CTA slide: is it unambiguous what the audience should do next? Flag: "Ask slide says 'Let's talk' but doesn't specify what about, or what the ask amount is."

5. **Information hierarchy** — on each slide: is there ONE clear focal element? Flag: "Slide 8 has 5 equally-sized cards with no hero element."

**Output**: List of issues with severity and fix suggestions:

```markdown
# Content Review

## Issues Found

### CRITICAL: Slide 8 — fails 3-second test
- 5 equally-weighted cards compete for attention
- Fix: promote the most important card to hero size, demote others

### MAJOR: Slides 4→5 — narrative gap
- Slide 4 jumps to solution without establishing the problem
- Fix: add a problem-framing element to slide 4, or swap order

### MINOR: Slide 3 — redundant metric
- "$1.5M ARR" appears here and on slide 7
- Fix: show it once on the stronger slide, replace on the other

## No Issues
- CTA clarity: Ask slide is clear and specific
- Overall narrative arc: good progression
```

**Usage**: Called by `--polish`, Visual QA (as optional enhancement), `--learn` critic.

### 1.3 Export Subroutine (enhancement to existing export logic)

**Progressive mode**: When a list of changed slide numbers is provided, export only those slides instead of the full deck. This saves time during polish iterations where only 2-3 slides changed.

```
Run Export Subroutine for <dir> [--only-slides 3,7,11] [--output <folder>]
```

**Implementation**:
- `--only-slides` provided: export with `npx slidev export --format png --per-slide --output <folder>`, then copy only the specified slide PNGs. If `--per-slide` is not supported by the installed version, fall back to full export.
- No `--only-slides`: full export as before (`npx slidev export --format png --output <folder>`).
- Always ensure `npm install` and `npx playwright install chromium` before first export in a session.

**Usage**: Called by every procedure that needs PNGs — Visual QA, Scoring, Polish, Learn, Compare, Responsive.

---

## Section 2: `--polish=N` Procedure (`references/polish-procedure.md`)

The core iterative improvement cycle for a single presentation.

**Input**: `--polish=N [dir]` where N = iteration count (default 3, max 5). `dir` defaults to the most recently generated presentation directory.

**Prerequisite**: The presentation must already exist (generated via `/slidev`). If `dir` doesn't contain `slides.md`, error and stop.

### Procedure

```
POL-1: Validate
  - Verify <dir>/slides.md exists
  - npm install if no node_modules/
  - npx playwright install chromium

POL-2: Initial state
  - Run Export Subroutine for <dir> --output slides-qa
  - Run Scoring Subroutine for <dir> → initial score report
  - Run Content Review Subroutine for <dir> → content issues
  - Print: "Polish iteration 0 (baseline): overall score X.X/10"

POL-3: Check exit conditions
  - If overall score >= 9 → goto POL-8 (early exit)
  - If iteration count == N → goto POL-8 (max iterations)

POL-4: Redesign weak slides
  - For each slide with avg < 7:
    - Run A/B Testing Subroutine (Section 3) → generates variants
    - Best variant replaces the slide in slides.md
  - For slides scoring 7-8: apply targeted fixes (the lowest axis only)
  - NEVER touch slides scoring >= 9

POL-5: Fix content issues
  - Apply critical and major content review fixes
  - Skip minor issues

POL-6: Visual QA pass (bug-fix only)
  - Run the existing Visual QA Loop for <dir>
  - This catches any CSS/rendering issues introduced by redesign

POL-7: Re-score
  - Run Export Subroutine for <dir> --output slides-qa
    (progressive: --only-slides for changed slides after first full export)
  - Run Scoring Subroutine for <dir>
  - Print: "Polish iteration M: overall score X.X/10 (delta +Y.Y)"
  - Increment iteration count → goto POL-3

POL-8: Finalize
  - Run Export Subroutine for <dir> --output slides-final (full export: PNGs + PDF)
  - Write Design Memory entry (Section 5)
  - Cleanup: rm -rf <dir>/slides-qa

POL-9: Preset auto-capture
  - If final overall score >= 9:
    - Ask user: "Score X.X/10! Save this aesthetic as a preset? Enter name or skip:"
    - If user provides name:
      - Extract from project: fonts, CSS variables, background treatment, decorative motifs, card styles
      - Write to ~/.claude/slidev-presets/<name>.preset.md
      - Register in ~/.claude/slidev-presets.json (create if doesn't exist)
      - Print: "Preset '<name>' saved to ~/.claude/slidev-presets/<name>.preset.md"
    - If user skips: continue

POL-10: Report
  Print:
  ```
  Polish complete: <dir>

    Iterations: M (of max N)
    Score progression: 6.5 → 7.8 → 9.1
    Slides redesigned: [3, 7, 11]
    Content fixes: N issues resolved
    A/B variants: <dir>/ab-variants/ (N alternatives saved)
    Preset saved: <name>.preset.md (if applicable)

    Final export:
      <dir>/slides-final/*.png
      <dir>/slides-final/slides.pdf
  ```
```

---

## Section 3: A/B Testing (`references/ab-testing.md`)

Called by `--polish` (POL-4) for each weak slide. Not a standalone subcommand.

### Procedure

```
AB-1: Identify weak slide
  - Input: slide number, current score report, current slides.md

AB-2: Analyze weakness
  - Which axes scored lowest?
  - What specific elements are weak? (layout, typography, colors, decoration, content structure)

AB-3: Generate 2 variants
  - Variant A: aggressive fix — radically redesign the weakest axis
    (e.g., if layout scored 4, completely change the layout structure)
  - Variant B: balanced fix — moderate improvement across all low axes
    (e.g., improve layout + typography + decoration together)
  - Both variants preserve the same CONTENT (text, data, messaging)
  - Both variants maintain consistency with the overall presentation aesthetic

AB-4: Write variants
  - Create temporary slides.md copies with each variant swapped in
  - Export just that slide for each variant

AB-5: Score variants
  - Run Scoring Subroutine on each variant (single slide)
  - Compare: original score vs variant A vs variant B

AB-6: Select winner
  - Highest scoring variant → goes into slides.md
  - If both variants score LOWER than original → keep original, log failure

AB-7: Save all variants
  - Create directory structure:
    <dir>/ab-variants/
      slide-<N>/
        original.png
        original-score.txt    (e.g., "6.3")
        variant-a.png
        variant-a-score.txt   (e.g., "7.2")
        variant-b.png
        variant-b-score.txt   (e.g., "8.1 ← winner")
  - This directory persists for user comparison

AB-8: Cleanup
  - Remove temporary slides.md copies
  - Keep ab-variants/ directory
```

---

## Section 4: Preset Auto-Capture

Integrated into `--polish` (POL-9) and can also trigger after standard generation (Step 8) when Visual QA produces high scores.

### Trigger Conditions
- After `--polish`: final overall score >= 9
- After standard generation: if Visual QA critic pass gives an explicit "excellent" rating

### Extraction Process
From the project directory, extract:
- `fonts` from slides.md headmatter
- `colorSchema` from slides.md headmatter
- CSS variables block from `styles/index.css` (everything between `:root {` and `}`)
- Card style definitions (`.card-solid`, `.card-ghost`, etc.)
- Decorative motif classes (`.decor-*`)
- Blockquote reset and layout-specific overrides
- `accentColor` derived from `--color-accent` value

### Output
Write a `.preset.md` file following the existing preset-format.md spec:
```markdown
---
theme: default
colorSchema: dark
accentColor: "#06C1A7"
fonts:
  sans: Instrument Serif
  serif: DM Sans
  mono: JetBrains Mono
transition: fade
---

Aesthetic description derived from the presentation's visual identity...

\`\`\`css
/* Full CSS block extracted from styles/index.css */
...
\`\`\`
```

Register in `~/.claude/slidev-presets.json`:
```json
{
  "<name>": "~/.claude/slidev-presets/<name>.preset.md"
}
```

---

## Section 5: Design Memory (`references/design-memory.md`)

### Storage
File: `~/.claude/slidev-design-memory.json`

### Structure
```json
{
  "version": 1,
  "max_entries": 50,
  "entries": [
    {
      "date": "2026-03-14",
      "topic": "fintech pitch deck",
      "overall_score": 9.2,
      "fonts": {
        "sans": "Instrument Serif",
        "serif": "DM Sans",
        "mono": "JetBrains Mono"
      },
      "colorSchema": "dark",
      "palette_mood": "warm gold on deep navy",
      "accent_color": "#D4A843",
      "decorative_motifs": ["diagonal lines", "corner glow orbs"],
      "layout_rotation": ["hero-left", "cards-grid", "centered-hero", "split-asymmetric"],
      "card_styles_used": ["solid", "accent", "glass"],
      "what_worked": "Gold accent on navy with serif headings created luxury feel. Diagonal lines at 0.12 opacity clearly visible.",
      "what_failed": null,
      "type": "high"
    },
    {
      "date": "2026-03-13",
      "topic": "education platform overview",
      "overall_score": 5.8,
      "fonts": {
        "sans": "Open Sans",
        "serif": "Lora",
        "mono": "Fira Code"
      },
      "colorSchema": "light",
      "palette_mood": "pastel purple on white",
      "accent_color": "#A78BFA",
      "decorative_motifs": ["dot grid"],
      "what_worked": null,
      "what_failed": "Pastel palette on light background — no contrast, decorations invisible at 0.05 opacity. Generic font choice.",
      "type": "low"
    }
  ]
}
```

### Write Protocol
Called after:
- `--polish` completes (POL-8)
- `--learn` iteration completes (L-3e addition)
- Standard generation with Visual QA (if scoring was performed)

Process:
1. Read existing `~/.claude/slidev-design-memory.json` (create with empty entries if doesn't exist)
2. Build entry from current project data
3. If `entries.length >= 50`: remove oldest entry (FIFO)
4. Append new entry
5. Write file

### Read Protocol
Called during Design Thinking (unique mode, before design decisions):
1. Read `~/.claude/slidev-design-memory.json` (skip if doesn't exist)
2. From `high` entries: note what worked — draw inspiration but DON'T copy. Use as a "palette of proven ideas" to vary from.
3. From `low` entries: note what failed — actively avoid these patterns.
4. CRITICAL: memory informs but doesn't constrain. Unique mode must still produce unique designs. If memory says "gold on navy works", don't always use gold on navy — use the PRINCIPLE (strong warm accent on cool dark base) and vary the specific implementation.

---

## Section 6: Improved `--learn`

Changes to the existing Learning Loop Procedure (L-1 through L-5).

### L-3c Enhancement: Structured Critique

Replace the current free-form critic agent prompt with structured scoring:

**Current**: Critic writes freestyle `critique.md` with subjective analysis.
**New**: Critic runs:
1. Scoring Subroutine → numeric per-slide scores
2. Content Review Subroutine → structured content issues
3. THEN writes `critique.md` incorporating both structured outputs + free-form analysis of systemic issues

This gives `improvements.md` concrete data to work with instead of vague descriptions.

### L-3c2 Addition: A/B on Weakest Slides

After critique, if any slide scores < 6:
1. Run A/B Testing Subroutine on the 2 weakest slides
2. Include the variant comparison in `critique.md` as "what could have been done differently"
3. This gives the improvement spec concrete before/after examples

### L-3e Enhancement: Design Memory Write

After applying improvements, write the iteration's design pattern to Design Memory:
- Score >= 8: write as `"type": "high"` with `what_worked`
- Score < 6: write as `"type": "low"` with `what_failed`
- Score 6-8: don't write (not distinctive enough to learn from)

### L-4 Enhancement: Score Progression Visualization

Summary includes a text-based score progression:
```
Score Progression:
  Learn 1: ██████░░░░ 5.8  (healthcare pitch, light pastel)
  Learn 2: ████████░░ 7.5  (fintech deck, dark luxury)
  Learn 3: █████████░ 8.3  (SaaS onboarding, minimal)
  Learn 4: █████████▌ 9.1  (AI keynote, brutalist)
```

And a patterns summary:
```
Patterns Observed:
  - Dark themes consistently score higher on decoration visibility (+1.2 avg)
  - Serif heading fonts score higher on typography drama (+0.8 avg)
  - Presentations with 3+ breathing slides score higher on rhythm (+1.5 avg)
```

---

## Section 7: `--compare <dir1> <dir2>` (`references/compare-procedure.md`)

### Procedure

```
CMP-1: Validate
  - Both dirs exist and contain slides.md
  - npm install + playwright install for both if needed

CMP-2: Export
  - Run Export Subroutine for <dir1> --output slides-qa (if not already exported)
  - Run Export Subroutine for <dir2> --output slides-qa (if not already exported)

CMP-3: Score
  - Run Scoring Subroutine for <dir1>
  - Run Scoring Subroutine for <dir2>

CMP-4: Generate comparison report
  Print:
  ```
  Comparison: <dir1> vs <dir2>

  Overall: <dir1> X.X/10 vs <dir2> Y.Y/10 → Winner: <dirN>

  Per-Slide Comparison:
  | Slide | <dir1> | <dir2> | Delta | Winner |
  |-------|--------|--------|-------|--------|
  | 1     | 7.8    | 8.5    | +0.7  | dir2   |
  | 2     | 9.1    | 6.3    | -2.8  | dir1   |
  ...

  Design Differences:
    Fonts: <dir1> uses Instrument Serif + DM Sans, <dir2> uses Syne + Literata
    Palette: <dir1> dark navy + gold, <dir2> light cream + emerald
    Layouts: <dir1> 5 unique structures, <dir2> 3 (less diverse)
    Decoration: <dir1> diagonal lines + glow, <dir2> dot grid only
  ```

CMP-5: Cleanup
  - rm -rf <dir1>/slides-qa <dir2>/slides-qa
```

---

## Section 8: `--notes [dir]` (`references/notes-procedure.md`)

### Procedure

```
NOTES-1: Resolve dir
  - If [dir] provided → use it
  - Else → look for most recently modified directory with slides.md

NOTES-2: Read slides.md
  - Parse all slides
  - Identify which slides already have <!-- notes --> blocks

NOTES-3: Generate notes for each slide WITHOUT existing notes
  For each slide:
  - Analyze slide content (title, bullet points, metrics, visuals)
  - Generate 3-5 speaking points:
    a) Opening: what to say when this slide appears (1 sentence)
    b) Key message: the ONE thing the audience should remember (1 sentence)
    c) Details: 1-2 supporting points to elaborate on
    d) Transition: how to bridge to the next slide (1 sentence)
  - Write as a <!-- notes --> block at the end of the slide

NOTES-4: Skip slides WITH existing notes
  - Do not overwrite or modify existing notes
  - Log: "Slide N: skipped (has existing notes)"

NOTES-5: Report
  Print:
  ```
  Speaker notes added: <dir>

    Slides with new notes: N
    Slides skipped (existing notes): M
    Total slides: N + M
  ```
```

---

## Section 9: `--responsive [dir]` (`references/responsive-check.md`)

### Procedure

```
RESP-1: Resolve dir and validate
  - Verify slides.md exists
  - npm install + playwright install if needed

RESP-2: Read current aspectRatio
  - Parse from slides.md headmatter (default: 16/9)
  - Save original value

RESP-3: Export baseline
  - Run Export Subroutine for <dir> --output slides-qa (at current aspect ratio)

RESP-4: Test alternative aspect ratio
  - Temporarily change aspectRatio in slides.md headmatter to 4/3
  - Run Export Subroutine for <dir> --output slides-responsive

RESP-5: Visual comparison
  - Read ALL PNGs from slides-responsive/
  - For each slide, check:
    - Text overflow or clipping
    - Column layouts collapsing or overlapping
    - Image cropping that loses important content
    - Font sizes still readable at new ratio
    - Decorative elements positioned correctly (not clipped off-screen)
    - Vertical content still fitting (4:3 is taller relative to width)

RESP-6: Restore original aspect ratio
  - Set aspectRatio back to original value in slides.md headmatter

RESP-7: Report
  Print:
  ```
  Responsive check: <dir>

    Tested: 16:9 → 4:3
    Issues found: N

    Slide 3: Two-column layout overlaps at 4:3 — columns need min-width or stack
    Slide 7: Right-side decorative glow clipped — reposition to stay within bounds
    Slide 11: Large hero text (6em) overflows — reduce to 4.5em at 4:3

    Recommendation: [N issues found — consider adding responsive fallbacks]
    Note: fixes not auto-applied — use --edit to address specific slides
  ```

RESP-8: Cleanup
  - rm -rf <dir>/slides-responsive
```

---

## Section 10: `--theme <name>` (modifier)

### Supported Themes
Primary: `default` (current), `seriph`, `apple-basic`
Experimental: `bricks`, `shibainu`, `penguin`, `dracula`
Unknown: warning + best-effort attempt

### Changes to Generation

**Step 2 (package.json)**:
- If `--theme` specified and not `default`:
  - Add `"@slidev/theme-<name>": "latest"` to dependencies
  - Remove `"@slidev/theme-default": "latest"`

**Step 5 (slides.md headmatter)**:
- Set `theme: <name>`

**Step 4 (styles/index.css)**:
- For `default` theme: apply all current CSS override rules (blockquote reset, text-align fixes, etc.)
- For other themes: skip theme-default-specific overrides. Instead add a comment:
  ```css
  /* Theme: <name> — theme-specific overrides may be needed.
     Check exported PNGs for CSS specificity issues. */
  ```

**Visual QA (QA-0a)**:
- Rules about theme-default CSS specificity (Rules 9, 10, 24, 29, 32) become conditional:
  ```
  If theme == "default":
    Apply Rules 9, 10, 24, 29, 32 as written
  Else:
    Skip these rules — different themes have different CSS specificity patterns
    Instead: during QA-4 visual review, pay extra attention to text alignment,
    background rendering, and blockquote styling — flag any visual issues
    that suggest theme CSS conflicts
  ```

**New Rules 33-34**:
- Rule 33: For non-default themes, perform an exploratory render before full generation. Write a minimal 2-slide test (cover + default), export PNGs, check for unexpected styling. If the theme applies unusual defaults, note them and adapt the generation accordingly.
- Rule 34: When using `--theme` with `--preset`, the preset's CSS block takes precedence. Theme provides base styling; preset provides customization layer on top.

---

## Section 11: Changes to SKILL.md

### 11.1 Input Parsing — new subcommands

Add to the subcommands section:

```
**`--polish=N [dir]`**: Iterative design improvement cycle. Runs N rounds (default 3, max 5)
of score → redesign weak slides → re-score. Includes A/B testing for weak slides and content
review. Follow the Polish Procedure in `references/polish-procedure.md`. Stop here.

**`--compare <dir1> <dir2>`**: Compare two presentations side-by-side with scoring.
Follow the Compare Procedure in `references/compare-procedure.md`. Stop here.

**`--notes [dir]`**: Generate speaker notes for slides that don't have them.
Follow the Notes Procedure in `references/notes-procedure.md`. Stop here.

**`--responsive [dir]`**: Check presentation rendering at 4:3 aspect ratio.
Follow the Responsive Check in `references/responsive-check.md`. Stop here.

**`--theme <name>`**: Use a non-default Slidev theme. This is a modifier —
combine with generation modes (unique, preset, custom style).
See Section 10 of this spec for theme handling rules.
```

### 11.2 References section

Add to the references list:

```
- `references/scoring-subroutine.md` — Slide scoring (1-10 on 6 axes)
- `references/content-review-subroutine.md` — Content quality checks
- `references/polish-procedure.md` — `--polish=N` iterative improvement
- `references/ab-testing.md` — A/B variant generation for weak slides
- `references/design-memory.md` — Design pattern memory (read/write)
- `references/compare-procedure.md` — `--compare` side-by-side scoring
- `references/notes-procedure.md` — `--notes` speaker notes generation
- `references/responsive-check.md` — `--responsive` aspect ratio check
```

### 11.3 Design Thinking section

Add after the current Design Decisions Checklist:

```
### Design Memory Consultation

Before finalizing design decisions in Unique mode, read `~/.claude/slidev-design-memory.json`
(if it exists). Follow the Read Protocol in `references/design-memory.md`.
Use high-scoring patterns as inspiration (not templates) and avoid low-scoring patterns.
```

### 11.4 Step 8 (Output Summary)

Add after the current output:

```
### Preset Auto-Capture (conditional)

If Visual QA critic rated the presentation as excellent (or if scoring was performed
and overall >= 9), offer to save the aesthetic as a preset. Follow the extraction process
in Section 4 of the design spec (implemented inline in SKILL.md or referenced).
```

### 11.5 Visual QA Phase 4 addition

Add to QA-10 (cleanup):

```
### Design Memory Write (conditional)

If Scoring Subroutine was run during this QA session, write the result to Design Memory.
Follow the Write Protocol in `references/design-memory.md`.
```

### 11.6 --help output

Update the help text to include all new subcommands:

```
Slidev Presentation Generator

Usage:
  /slidev <outline or file>                     Generate with unique design
  /slidev --preset <name> <outline>              Generate with preset style
  /slidev style: <desc> <outline>                Generate with custom style
  /slidev --theme <name> <outline>               Generate with specific theme
  /slidev --polish=N [dir]                       Iterative quality improvement (N cycles)
  /slidev --edit [dir] <comment>                 Edit existing presentation
  /slidev --picture [auto|paths...] [dir]        Add images to slides
  /slidev --compare <dir1> <dir2>                Compare two presentations
  /slidev --notes [dir]                          Generate speaker notes
  /slidev --responsive [dir]                     Check 4:3 rendering
  /slidev --export <format> [dir]                Export (html|pdf|png2pdf|pngs|png_N)
  /slidev --dev [dir]                            Launch dev server
  /slidev --create-preset <name>                 Create a new preset
  /slidev --learn=N                              Self-improving loop (N cycles)
  /slidev --help                                 Show this help
```

### 11.7 --learn updates

Update the L-3c, add L-3c2, update L-3e, update L-4 as described in Section 6.

---

## Appendix: Size Estimates

| File | Current lines | Estimated after |
|---|---|---|
| SKILL.md | 1037 | ~1250 |
| references/ (existing 6 files) | 1540 | ~1540 (unchanged) |
| references/ (new 8 files) | 0 | ~490 |
| **Total** | **2577** | **~3280** |

All files stay well under the 4000-line limit per file.
