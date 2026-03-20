---
name: slidev
description: Use when generating a Slidev presentation from a slide outline. Supports preset styles, unique designs, custom style descriptions, and image placement. Scaffolds a complete Slidev project. Also handles --help, --dev, --export, --edit, --picture, --create-preset, and --learn subcommands.
argument-hint: "[--help | --dev [dir] | --export <format> [dir] | --edit [dir] <comment> | --picture [auto|paths...] [dir] | --create-preset <name> | --learn=N | --deep_learn=N | --no-preset | --preset <name> | style: <desc>] <outline or file path>"
---

# Slidev Presentation Generator

You generate complete Slidev presentation projects from slide outlines. Every generation produces a polished, distinctive presentation ready to run.

## References

Before generating, internalize these references:
- `references/slidev-syntax.md` — Slidev markdown syntax
- `references/slidev-layouts.md` — Layout selection guide
- `references/slidev-animations.md` — Animations & transitions
- `references/preset-format.md` — Preset file specification
- `references/layout-css-patterns.md` — **CRITICAL**: Battle-tested CSS patterns for each layout type (alignment, backgrounds, overlays)
- `references/design-principles.md` — **CRITICAL**: Gamma-level design quality principles (visual rhythm, layout diversity, typography drama, icon system, card variation, decorative layer, visual arc, data viz, mockups, SVG diagrams, spacing, accent hierarchy). Apply in ALL modes: generation, editing, presets, Visual QA.
- `references/scoring-subroutine.md` — Slide scoring (1-10 on 6 axes), used by --polish, --learn, --compare
- `references/content-review-subroutine.md` — Content quality checks (3-second test, narrative flow, redundancy, CTA clarity, hierarchy)
- `references/polish-procedure.md` — `--polish=N` iterative improvement cycle
- `references/ab-testing.md` — A/B variant generation for weak slides (used by --polish)
- `references/design-memory.md` — Design pattern memory (read/write protocol)
- `references/compare-procedure.md` — `--compare` side-by-side scoring
- `references/notes-procedure.md` — `--notes` speaker notes generation
- `references/responsive-check.md` — `--responsive` aspect ratio check

## Input Parsing

Parse the user's input to determine the subcommand or mode:

### Subcommands (handle before anything else)

**`--help`**: Display usage help and stop. Show:

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
  /slidev --learn=N --preset <name>            Preset learning (create + refine with visual critic)
  /slidev --deep_learn=N                       Preset deep learning (auto-refine N cycles)
  /slidev --deep_learn=N --preset <name>       Deep learn a specific preset
  /slidev --add_archetype [name]              Add a new composition archetype
  /slidev --no-preset <outline>                Generate without auto-preset (Unique mode)
  /slidev --help                                 Show this help
```

**`--create-preset <name>`**: Interactive preset creation wizard.

1. Extract preset name from arguments. If missing, ask for one (kebab-case).
2. Ask 7 questions **ONE AT A TIME**, waiting for each answer:
   - **Mood**: "What mood? (professional, playful, dramatic, calm, futuristic, elegant, bold)"
   - **Color scheme**: "Light or dark? (dark, light, deep navy, warm cream...)"
   - **Accent color**: "Accent color? (#ff6b35, electric blue, warm coral...)"
   - **Typography**: "Font personality? (geometric & modern, classic & refined, rounded & friendly, sharp & technical)"
   - **Density**: "Content density? (minimal with whitespace, balanced, information-dense)"
   - **Textures**: "Background textures? (subtle noise, gradient mesh, geometric patterns, clean flat, frosted glass)"
   - **Transitions**: "Slide transitions? (fade, slide-left, none...)"
   - **Save location**: "Save preset globally or locally? (global: ~/.claude/slidev-presets/, local: ./.slidev-presets/ in current project)"
3. Synthesize answers into concrete design params using `/frontend-design` principles (distinctive Google Fonts — never Inter/Roboto/Arial/generic choices, cohesive palette with dominant+accent hierarchy, atmospheric backgrounds, CSS). The CSS block MUST include layout-specific styles per `references/preset-format.md` — explicit `text-align: center` on `h1`, `p`, `div` for all centered layouts (cover, section, fact, end, statement, center), plus background image overlay support for cover/section. See `references/layout-css-patterns.md` for the required patterns.
4. Based on save location answer:
   - **Global**: Create `~/.claude/slidev-presets/` if needed, write `<name>.preset.md` there
   - **Local**: Create `.slidev-presets/` in the current working directory if needed, write `<name>.preset.md` there
   Write per `references/preset-format.md`.
5. Generate demo presentation using `assets/demo-outline.md` with that preset, output to `demo-<name>/`.
6. **Visual QA** — Run the Visual QA Loop for `demo-<name>/`.
7. Print summary: preset path (noting global vs local), demo path, Visual QA results, how to preview, how to use.

**`--add_archetype [name]`**: Add a new composition archetype to the library.

1. If `name` not provided — ask "Как назвать архетип? (kebab-case)"
2. Ask: **"Для какого типа контента этот архетип? Опишите ситуацию, когда существующие архетипы не подходят."**
3. Based on the answer, determine:
   - How many archetypes are actually needed (may be 1, may be 2-3 for different aspects)
   - Density level for each (low / medium / medium-high / high)
   - Group classification (hero / grid / split / timeline / table / cta)
   - Which content types it serves
   - Which shape elements it uses (circles, pills, hexagons, etc.)
4. Generate HTML skeleton following the format in `references/composition-archetypes.md` (using `{{SLOT}}` markers, `layout: none`, max 3 div nesting levels, inline styles)
5. Append the archetype record(s) to `references/composition-archetypes.md` — both the archetype definition AND its content-type association in the mapping table at the top
6. Generate a test slide using the new archetype with sample content and export as PNG for visual verification
7. Report: archetype name(s), density, content types served, and the test slide PNG path

Stop here — do not proceed to generation.

**`--learn=N`**: Learning loop. Parse N from the argument (e.g., `--learn=5`).
- **Without `--preset`**: Self-improving skill loop. Follow the Learning Loop Procedure (L-1 through L-5) — improves SKILL.md and design-principles.md based on visual critique.
- **With `--preset <name>`**: Preset learning loop. Creates (or uses named) preset, generates N demo presentations, visual critic evaluates and proposes CSS/font/color improvements. Follow the Preset Learning Procedure (PL-1 through PL-6).

Stop here — do not proceed to generation.

**`--deep_learn=N`**: Preset deep learning loop. Creates (or uses named) preset, then iteratively auto-refines it through N cycles of 3 visual test runs with convergence detection. N must be >= 2.
- **With `--preset <name>`**: deep learn a specific preset
- **Without `--preset`**: interactive wizard creates the initial preset (same as `--create-preset`)

Follow the Preset Deep Learning Procedure (PDL-1 through PDL-7). Stop here — do not proceed to generation.

**`--polish=N [dir]`**: Iterative design improvement cycle. Runs N rounds (default 3, max 5) of score → redesign weak slides → re-score. Includes A/B testing for weak slides and content review. Follow the Polish Procedure in `references/polish-procedure.md`. Stop here — do not proceed to generation.

**`--compare <dir1> <dir2>`**: Compare two presentations side-by-side with scoring. Follow the Compare Procedure in `references/compare-procedure.md`. Stop here — do not proceed to generation.

**`--notes [dir]`**: Generate speaker notes for slides that don't have them. Follow the Notes Procedure in `references/notes-procedure.md`. Stop here — do not proceed to generation.

**`--responsive [dir]`**: Check presentation rendering at 4:3 aspect ratio. Follow the Responsive Check in `references/responsive-check.md`. Stop here — do not proceed to generation.

**`--dev [dir]`**: Launch the Slidev dev server for an existing presentation.

1. **Resolve project directory**:
   - If `dir` is provided, use it directly
   - Otherwise, auto-detect: look for `slides.md` in the current working directory. If not found, look for subdirectories containing `slides.md` (one level deep). If multiple found, list them and ask the user to pick.
   - If no Slidev project found, emit error: `No Slidev project found. Run /slidev <outline> to create one.`
2. **Install dependencies** if `node_modules/` doesn't exist: run `npm install` in the project directory
3. **Start dev server**: run in the background using this exact pattern to keep the process alive (slidev reads stdin for keyboard shortcuts and exits on EOF):
   ```bash
   cd <project-dir> && (sleep infinity | npx slidev) 2>&1
   ```
   Run this via Bash with `run_in_background: true`.
4. **Wait for ready**: use `TaskOutput` with `block: true, timeout: 15000` to capture initial output showing the URL
5. **Report**: print the local URL (e.g. `http://localhost:3030/`) once the server is ready. Note: the server continues running in the background.

Stop here — do not proceed to generation.

**`--export <format> [dir]`**: Export the presentation to various formats.

Formats:
- `html` — Build as a static SPA (hostable HTML)
- `pdf` — Export as PDF (Chromium print mode — may lose `filter:blur`, `backdrop-filter`, overlay gradients)
- `png2pdf` — Export as PDF via PNG screenshots (pixel-perfect, recommended for presentations with CSS effects)
- `pngs` — Export all slides as individual PNG images
- `png_N` — Export a single slide N as PNG (e.g. `png_3` for slide 3)

Procedure:

1. **Resolve project directory** (same rules as `--dev`): use `dir` if provided, otherwise auto-detect.
2. **Install dependencies** if `node_modules/` doesn't exist: run `npm install` in the project directory.
3. **Ensure playwright-chromium** is installed (required for pdf/png exports):
   - For `pdf`, `png2pdf`, `pngs`, or `png_N` formats: run `npx playwright install chromium` if not already available.
4. **Run export command** based on format:
   - `html`: `cd <dir> && npx slidev build --base /` — output goes to `<dir>/dist/`
   - `pdf`: `cd <dir> && npx slidev export --output slides.pdf` — output is `<dir>/slides.pdf`
   - `png2pdf`: Pixel-perfect PDF via PNG screenshots. Procedure:
     1. Export PNGs: `cd <dir> && npx slidev export --format png --output slides-tmp`
     2. Ensure Python `Pillow` is available: `pip install Pillow` (skip if already installed)
     3. Combine PNGs into PDF using this Python script:
        ```python
        from PIL import Image
        import os, re

        png_dir = 'slides-tmp'
        files = [f for f in os.listdir(png_dir) if f.endswith('.png')]
        files.sort(key=lambda x: int(re.match(r'(\d+)', x).group()))

        images = []
        for f in files:
            images.append(Image.open(os.path.join(png_dir, f)).convert('RGB'))

        images[0].save(
            'slides.pdf',
            save_all=True,
            append_images=images[1:],
            resolution=150.0,
            quality=95
        )

        for img in images:
            img.close()
        ```
     4. Clean up: `rm -rf <dir>/slides-tmp`
     5. Output is `<dir>/slides.pdf`
   - `pngs`: `cd <dir> && npx slidev export --format png --output slides` — output is `<dir>/slides/` directory with numbered PNGs
   - `png_N`: `cd <dir> && npx slidev export --format png --range N --output slide-N` — output is single PNG for slide N
5. **Report**: print the output file/directory path and format.

**`--edit [dir] <comment>`**: Edit an existing Slidev presentation based on a free-text comment.

The comment describes what to change — content, styling, structure, animations, or any combination. Examples:
- `"сделай тёмную тему"` — switch color scheme to dark
- `"добавь слайд после 3-го про статистику"` — insert a new slide
- `"убери все анимации"` — remove v-clicks and transitions
- `"увеличь шрифт заголовков"` — adjust typography
- `"замени палитру на синюю"` — change color scheme
- `"перепиши слайд 5 более кратко"` — rewrite specific slide content
- `"добавь заметки для спикера"` — add presenter notes

Procedure:

1. **Resolve project directory** (same rules as `--dev`): use `dir` if provided, otherwise auto-detect by looking for `slides.md`.
2. **Read all project files** to understand the current state:
   - `slides.md` (required — the main presentation)
   - `styles/index.css` (if exists)
   - `uno.config.ts` (if exists)
   - All files in `components/` (if directory exists)
   - `package.json` (if exists)
3. **Analyze the comment** to determine what needs to change:
   - **Content edits**: adding/removing/rewriting slides or bullet points
   - **Style edits**: colors, fonts, backgrounds, spacing, layout changes
   - **Structure edits**: reordering slides, changing layouts, splitting/merging
   - **Animation edits**: transitions, v-clicks, reveals
   - **Component edits**: adding/modifying Vue components
4. **Invoke `/frontend-design` thinking AND `references/design-principles.md`** for any visual or style-related edits. Before changing colors, fonts, layouts, backgrounds, components, or adding new slides:
   - Understand the existing aesthetic direction from the current `styles/index.css`, headmatter, and per-slide styles
   - Apply `/frontend-design` principles to ensure edits are cohesive, bold, and intentional — not generic
   - New slides must match the existing visual language (same palette, typography, spatial rhythm)
   - Style changes must be holistic: don't just swap a color — reconsider contrast, accent hierarchy, background treatment, and typography pairing as a system
   - Even for content-only edits, consider whether layout choice and spacing deserve `/frontend-design`-level attention (e.g., a new slide with a single stat deserves `fact` layout with dramatic styling, not a plain `default`)
   - Apply ALL Design Principles: new slides must maintain visual rhythm (Principle 1), not repeat the layout of adjacent slides (Principle 2), use the Icon component instead of emoji (Principle 4), and match the presentation's accent hierarchy (Principle 12)
5. **Apply changes surgically** using the Edit tool:
   - Only modify files and sections that the comment requires
   - Preserve everything the comment doesn't mention
   - Maintain consistency: if changing accent color in `styles/index.css`, also update it in per-slide `<style>` blocks and headmatter if referenced there
   - When adding slides, maintain the `---` separator convention and assign appropriate layouts
   - When changing design (colors, fonts, backgrounds), update all relevant locations: CSS variables, headmatter fonts, per-slide styles
5. **Verify consistency** after edits:
   - Slide count matches intent (unchanged unless comment asks to add/remove)
   - No broken references (e.g., deleted component still used in slides)
   - CSS variables are consistent between `styles/index.css` and inline usage
   - Headmatter and CSS don't contradict each other
6. **Visual QA** — Run the Visual QA Loop for the project directory.
7. **Report** what was changed:
   - List each file modified and a brief summary of changes
   - If slides were added/removed, show the new slide count
   - Include Visual QA results
   - Remind how to preview: `cd <dir> && npm run dev` or `/slidev --dev <dir>`

Key principles:
- **Minimal diff**: Change only what's needed. Don't rewrite `slides.md` from scratch when only one slide needs editing.
- **Preserve design intent**: If the presentation uses a preset style, respect its aesthetic when making changes. Don't introduce clashing visual elements.
- **Cascade awareness**: A color change in CSS variables should be the only edit needed if the slides reference variables correctly. But if per-slide `<style>` blocks use hardcoded colors, update those too.
- **Content fidelity**: When rewriting content, maintain the same level of detail and tone unless the comment explicitly asks for a different approach.

Stop here — do not proceed to generation.

**`--picture [source] [dir]`**: Add images to an existing Slidev presentation.

Syntax:
```
/slidev --picture auto [dir]                    Standalone: auto-search images
/slidev --picture <path1> [path2...] [dir]      Standalone: user-provided images
/slidev --preset X --picture auto <outline>     Modifier on generation
/slidev --edit --picture auto <dir> "<comment>" Modifier on edit
```

#### Picture Placement Procedure

**P-1: Read slides.md** — parse all slides: number, layout, title, content.

**P-2: Select candidate slides** — which slides should get images:
- Always: `cover`, `section`, `image-left`, `image-right`, `image` layouts
- Consider: content slides describing concrete visual subjects
- Skip: `fact`, `statement`, `end` layouts; code-heavy slides; slides already with images

**P-3: Acquire images**

*Auto mode:*
- For each candidate slide: derive search query from title + key content words
- Search via `mcp__brave-search__brave_web_search` (query + "high quality photo")
- Download to `<dir>/public/images/slide-N-keyword.jpg` via `curl -L -o`
- Verify file is non-empty; skip slide on failure

*User-provided mode:*
- Copy files to `<dir>/public/images/` (or reference if already in `public/`)
- Distribute across candidate slides in order
- Fewer images than candidates → remaining slides unchanged
- Fewer candidates than images → extras unused, noted in report

**P-4: Update slides.md** — for each slide that got an image:
- `cover`/`section` → set background via **per-slide `<style>` CSS** (NOT frontmatter `background:` prop, which gets blocked by theme's opaque `background-color`). Use: `background: url('/images/slide-N-keyword.jpg') center/cover no-repeat !important;` on `.slidev-layout`.
- `default` (text-heavy) → change layout to `image-right`, add `image:` prop
- `image-left`/`image-right`/`image` → update `image:` prop
- For any slide with background image: add dark overlay via `::before`, set ALL text elements to `text-align: center` explicitly, set text colors to white/near-white. See `references/layout-css-patterns.md` for exact CSS patterns.

**P-5: Add CSS overlay** (if background images on cover/section):
In `styles/index.css`, add overlay support. But **each per-slide `<style>` must also**:
1. Set `background: url(...) center/cover no-repeat !important` on `.slidev-layout` (overrides theme's background-color)
2. Set `text-align: center` explicitly on `h1`, `p`, and other text elements (overrides theme's text-align)
3. Set text colors to white/near-white for readability against dark overlay
4. **CRITICAL — Use gradient overlay, not uniform opacity**, especially on cover/statement slides with multiple text elements at different vertical positions. Uniform overlays fail on high-contrast photos (bright spots bleed through). Use: `background: linear-gradient(to bottom, rgba(bg, 0.92) 0%, rgba(bg, 0.80) 60%, rgba(bg, 0.70) 100%)` — stronger where text is densest (usually top/center), lighter at edges where the image can show through.
5. **Minimum overlay opacity**: 0.85 in any zone where text appears. After adding images, verify that the SMALLEST text on the slide (subtitles, dates, attributions) is fully legible.

```css
/* styles/index.css — background image overlay support */
.slidev-layout.cover, .slidev-layout.section { position: relative; }
.slidev-layout.cover::before, .slidev-layout.section::before {
  content: ''; position: absolute; inset: 0;
  /* Gradient overlay — stronger where text lives (top/center), lighter at bottom */
  background: linear-gradient(to bottom, rgba(0,0,0,0.88) 0%, rgba(0,0,0,0.75) 70%, rgba(0,0,0,0.65) 100%);
  z-index: 0; pointer-events: none;
}
.slidev-layout.cover > *, .slidev-layout.section > * { position: relative; z-index: 1; }
```

**P-6: Run Visual QA Loop** — always triggered after picture placement.

**P-7: Report** — which slides got images, sources, skipped slides and why.

Stop here — do not proceed to generation.

**`--learn=N`**: Self-improving learning loop. Runs N autonomous cycles of generate → export → critique → improve. Each cycle creates a presentation from a unique outline, analyzes it visually and structurally, then applies improvements to the skill itself.

**Maximum N**: 10. If N > 10, cap at 10 and notify the user.

### Learning Loop Procedure

**L-1: Create education folder** — Scan for existing `edu_*` directories in the working directory. Create the next sequential one (e.g., `edu_01`, `edu_02`). All iterations for this learning run go inside this folder.

**L-2: Generate N diverse outlines** — Create all outlines upfront to ensure diversity. Save each as `<edu_dir>/learn_<i>/outline.md`. **All outlines MUST be written in Russian** (titles, slide names, bullet points — everything in Russian). Outlines must vary across:
- **Industries**: tech startup, education, healthcare, finance, creative agency, nonprofit, SaaS, retail, AI/ML, sustainability
- **Formats**: pitch deck, educational lecture, product launch, quarterly report, team onboarding, keynote talk, investor update, workshop
- **Sizes**: mix of 8-10 slides (short), 12-14 (medium), 15-16 (long)
- **Tone**: formal, casual, inspirational, data-heavy, storytelling, technical

Each outline follows the standard outline format:
```markdown
# Presentation Title
## Slide 1: Title
- Point 1
- Point 2
## Slide 2: Another Title
- Content here
```

**L-3: Learning iteration loop** — For i = 1 to N:

**L-3a: Create presentation** — Launch a subagent (Agent tool) to run the full `/slidev` generation pipeline for `<edu_dir>/learn_<i>/outline.md`. The subagent:
- Reads the current SKILL.md (to pick up any improvements from prior iterations)
- Uses the outline from `<edu_dir>/learn_<i>/outline.md`
- Outputs the project to `<edu_dir>/learn_<i>/`
- Runs the full generation procedure (Steps 1-7) including Visual QA
- Uses unique mode (auto-generated design) — each iteration should produce a different aesthetic

**L-3b: Export** — After creation, export the presentation:
```bash
cd <edu_dir>/learn_<i> && npm install && npx playwright install chromium
npx slidev export --format png --output slides
npx slidev export --output slides.pdf
```
If export fails (missing deps, rendering errors), log the error in `<edu_dir>/learn_<i>/critique.md` and skip to L-3f with a note about the export failure. Do NOT abort the entire learning loop.

**L-3c: Critic agent** — Launch a subagent (Agent tool) as a **demanding design critic**. Provide it with:

Critic agent prompt:
```
You are a demanding presentation design critic. Your job is to analyze a Slidev presentation and find every design flaw, comparing against professional Gamma-quality standards.

INPUTS:
- Presentation slides: <edu_dir>/learn_<i>/slides.md
- Exported slide images: <edu_dir>/learn_<i>/slides/*.png (read ALL of them visually)
- Current skill rules: .claude/skills/slidev/SKILL.md
- Design principles: .claude/skills/slidev/references/design-principles.md
- Scoring Subroutine: .claude/skills/slidev/references/scoring-subroutine.md
- Content Review Subroutine: .claude/skills/slidev/references/content-review-subroutine.md

ANALYSIS PROCESS:
1. Read slides.md — check compliance with ALL Slide Authoring Rules and Design Quality Rules
2. Read EVERY exported PNG — apply the full QA-4 visual checklist + QA-8 critic checklist
3. Cross-reference: do the rules in SKILL.md and design-principles.md actually produce good results? Are there gaps?
4. Look for SYSTEMIC issues — patterns that appear across multiple slides, not just one-off problems
5. Run the Scoring Subroutine — score each slide on 6 axes (visual impact, layout uniqueness, typography drama, color conviction, content clarity, decorative quality)
6. Run the Content Review Subroutine — check 3-second test, narrative flow, redundancy, CTA clarity, information hierarchy

OUTPUT FORMAT — write to <edu_dir>/learn_<i>/critique.md:

# Critique: [Presentation Title] (Learn Iteration <i>)

## Overall Score: X/10

## Systemic Issues (affect the skill itself)

### Issue 1: [Title]
- **Severity**: critical | major | minor
- **Category**: rhythm | layout | typography | icons | cards | decoration | arc | data-viz | mockups | diagrams | spacing | accent | rendering | content | structure
- **Frequency**: How many slides affected
- **Description**: What's wrong
- **Evidence**: What was observed in specific PNGs and/or MD structure
- **Root cause**: Why the current skill rules allowed this to happen
- **Proposed skill fix**: Specific change to SKILL.md or design-principles.md — be precise about WHAT to add/change and WHERE

## Slide-Specific Issues (one-off problems in this presentation)

### Slide N: [issue]
- **Description**: ...
- **Severity**: ...

## What Worked Well
- List things the skill got right — these rules should be preserved

## Design Summary
- **Palette type**: dark | light | mixed
- **Palette mood**: [short description, e.g., "warm gold on deep navy"]
- **Font character**: serif-heavy | geometric-sans | humanist | monospace-accent
- **Decoration style**: geometric | organic | linear | pattern | minimal
- **Strongest axis**: [which scoring axis scored highest on average]
- **Weakest axis**: [which scoring axis scored lowest on average]
```

**L-3c2: A/B on weakest slides** — After critique, if any slide scores < 6, run the A/B Testing Subroutine (`references/ab-testing.md`) on the 2 weakest slides. Include the variant comparison in `critique.md` under a "## A/B Alternatives" section showing what could have been done differently. This provides concrete before/after examples for the improvement spec.

**L-3d: Generate improvement spec** — Based on the critique, create `<edu_dir>/learn_<i>/improvements.md`:

```markdown
# Improvements from Learn Iteration <i>

## Applied Changes (critical + major systemic issues only)

### Change 1: [Title]
- **File**: SKILL.md | references/design-principles.md
- **Section**: [exact section name]
- **Type**: add_rule | modify_rule | add_example | expand_checklist
- **Description**: What to change and why
- **Before**: [relevant excerpt or "N/A" for new additions]
- **After**: [exact text to write]

## Deferred (minor issues — logged for review)
- [minor issue 1]
- [minor issue 2]
```

**L-3e: Apply improvements** — Read the improvements.md and apply changes to the skill files:
- Only apply changes marked as critical or major severity
- Before applying, verify the change doesn't contradict an existing rule
- If a contradiction is detected, note it in improvements.md and skip that change
- Use the Edit tool for surgical modifications

After applying improvements, write the iteration's design pattern to Design Memory using the overall score from `critique.md`. Follow the Write Protocol in `references/design-memory.md`. Only write if score >= 8 (type "high") or score < 6 (type "low"). Skip write for scores 6-8 (not distinctive enough to learn from).

**L-3f: Git commit** — Stage and commit only the learning artifacts + skill changes:

```bash
# Stage presentation artifacts (not Slidev system files)
git add <edu_dir>/learn_<i>/outline.md
git add <edu_dir>/learn_<i>/slides.md
git add <edu_dir>/learn_<i>/slides/*.png
git add <edu_dir>/learn_<i>/slides.pdf
git add <edu_dir>/learn_<i>/critique.md
git add <edu_dir>/learn_<i>/improvements.md

# Stage skill changes (if any were made)
git add .claude/skills/slidev/SKILL.md
git add .claude/skills/slidev/references/design-principles.md

# Commit
git commit -m "learn(<i>/<N>): [outline topic] — [brief summary of improvements]"
```

**Do NOT stage**: `node_modules/`, `package.json`, `uno.config.ts`, `styles/`, `components/`, `dist/`, `slides-qa/`, or any other Slidev project files.

**L-4: Summary** — After all N iterations, create `<edu_dir>/summary.md`:

```markdown
# Learning Run Summary: edu_XX

## Overview
- **Iterations**: N
- **Date**: YYYY-MM-DD
- **Starting skill version**: [git hash before learning]
- **Final skill version**: [git hash after learning]

## Iterations

### Learn 1: [Topic]
- Score: X/10
- Key findings: ...
- Changes applied: ...

### Learn 2: [Topic]
...

## Cumulative Skill Changes
[Diff summary of all changes made to SKILL.md and design-principles.md across all iterations]

## Deferred Issues (minor — need human review)
- [all minor issues from all iterations]

## Recommendations
- [patterns observed across iterations]
- [suggested areas for manual improvement]

## Score Progression
```
Learn 1: ██████░░░░ 5.8  (topic, palette mood from Design Summary)
Learn 2: ████████░░ 7.5  (topic, palette mood)
...
```

## Patterns Observed
Synthesize across all critique.md Design Summary blocks:
- [pattern 1 with delta, e.g., "Dark themes score +1.2 avg on decoration visibility"]
- [pattern 2 with delta]
```

Commit the summary:
```bash
git add <edu_dir>/summary.md
git commit -m "learn(summary): edu_XX — N iterations completed, [total changes] improvements applied"
```

**L-5: Report** — Print to the user:
```
Learning complete: edu_XX

  Iterations: N
  Outlines: [list topics]
  Skill improvements: [count] changes applied
  Deferred issues: [count] minor issues for review

  Results: <edu_dir>/summary.md
  Each iteration: <edu_dir>/learn_<i>/
```

Stop here — do not proceed to generation.

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
  3. Export PNGs: `cd preset-learn-<name> && npx slidev export --format png --output run-<i>/slides`
  4. **Optimization**: Reuse the scaffolded `node_modules/` — do NOT run `npm install` for every run. Run all generations in the same scaffolded directory, moving `slides.md` and `styles/index.css` between runs, and copying exported PNGs to `run-<i>/slides/`.

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

**PDL-2: Training cycle** — **MUST execute ALL N cycles.** Do NOT skip, abbreviate, or reduce the number of cycles for any reason. Repeat for c = 1 to N:

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

## Visual QA Loop

A reusable subroutine for visual quality assurance. Input: `<dir>` (project directory). Called after generation, editing, preset demo creation, and picture placement.

### Phase 1: CSS Code Review (before rendering)

**QA-0: Pre-render code review** — Before exporting PNGs, read `slides.md` and check the CSS code directly. This catches structural issues that are hard to spot visually.

**QA-0a: CSS correctness checks** — For EACH slide in the file, verify:
- **Centered layouts** (`cover`, `section`, `fact`, `end`, `statement`, `center`): confirm that `text-align: center` is set **explicitly** on `h1`, `p`, and other text elements in the per-slide `<style>` block — not just on the parent `.slidev-layout`. If missing, **add it immediately** before proceeding.
- **Background image slides**: confirm the background is set via per-slide CSS (`background: url(...) center/cover no-repeat !important` on `.slidev-layout`), NOT via frontmatter `background:` prop. If using frontmatter prop, switch to CSS approach. Confirm `::before` overlay is present for readability. Confirm text colors are white/near-white.
- **Text-on-image contrast**: if a slide has a background image or dark background, confirm text colors are explicitly set to white/light values.
- **No reliance on CSS inheritance** for text alignment, colors, or font properties on centered layouts — all must be explicit due to Slidev theme specificity overrides.

**QA-0b: Design Principles compliance** — Review the ENTIRE slides.md against `references/design-principles.md`:
- **Principle 1 (Rhythm)**: Count consecutive dense content slides. If 3+ `default` layouts in a row without a breathing slide (`section`/`statement`/`fact`), insert one.
- **Principle 2 (Layout diversity)**: Check that consecutive slides have different visual structures. If 2+ slides share the same pattern (e.g., "label + line + 2-column grid"), restructure one.
- **Principle 3 (Typography)**: Verify at least 3 type scales exist. Key metrics should be hero-sized (4-8em). If all headings are the same size, fix it. **CRITICAL**: Measure statement/fact/section slide main text against 3em minimum — if below, flag as critical and fix immediately.
- **Principle 4 (Icons)**: Search for emoji characters (📱💳⭐🧠📊🚗 etc.). If found, replace with `<Icon>` component. Ensure `components/Icon.vue` exists.
- **Principle 5 (Cards)**: Check if all cards use identical styling. If yes, differentiate with at least 2 card styles.
- **Principle 7 (Visual arc)**: Confirm the climax slide (Ask/CTA) has distinct visual treatment — different background, larger type, or unique color.
- **Principle 8 (Data viz)**: Check bar charts for value labels, tables for hero-column highlights.
- **Principle 9 (Mockups)**: Check device mockups for wireframe content. If empty, add wireframe UI.
- **Principle 10 (Diagrams)**: Check for text arrows (→ ↓ ← ↑) used as diagram connectors. Replace with SVG.
- **Principle 11 (Spacing)**: Check content vertical distribution — should not be crammed to top.
- **Principle 12 (Accent hierarchy)**: Verify accent color is used at varying intensities, not full saturation everywhere.
- **HTML nesting depth (Rule 17)**: Scan for HTML nesting deeper than 3 levels (3+ opening `<div>` tags before content). Slidev will render these as raw HTML code. Flatten immediately.
- **Font size minimum (Rule 18)**: Search for `text-xs` usage. If used for body content (not footnotes), replace with `text-sm`. If this makes content overflow, the slide has too much content — split it.
- **Content density (Rule 22)**: Count visual blocks per slide. If any slide has 6+ distinct elements (cards, tables, charts, lists), split or remove secondary content.
- **Breathing slides (Visual Rhythm Override)**: Count consecutive dense `default` layout slides. If 4+ in a row, convert 1-2 to statement/fact layout.
- **Background image overlays (Rule P-5)**: If cover/section slides have background images, verify overlay uses gradient (not uniform opacity) with minimum 0.85 in text zones.

Fix any issues found before proceeding to visual review.

### Phase 2: Visual Export & Review

**QA-1: Prepare** — `npm install` if no `node_modules/` in `<dir>`, then `npx playwright install chromium`.

**QA-2: Export PNGs** — `cd <dir> && npx slidev export --format png --output slides-qa` → produces `slides-qa/1.png, 2.png, ...`

**QA-3: Count slides** — glob `<dir>/slides-qa/*.png` to get the list.

**QA-4: Per-slide visual review** — Read **EVERY** slide PNG with the Read tool (no skipping). Apply `/frontend-design` thinking — evaluate each slide as a designer who cares deeply about visual quality. For each slide, run this full checklist:

#### Text & Readability
- [ ] All text is fully legible — no text blends into the background
- [ ] Sufficient contrast ratio between text and background (white text on dark overlay ≥ 0.4 opacity, dark text on light bg)
- [ ] No text is clipped, cut off, or overflowing outside the visible slide area
- [ ] Text hierarchy is clear — heading visually dominant over body text
- [ ] Font rendering looks correct (not missing, not fallback system font)

#### Alignment & Positioning
- [ ] On centered layouts (cover, section, fact, end, statement, center): ALL text elements are actually centered — not left-shifted or right-shifted
- [ ] On default/content layouts: text and bullets are properly left-aligned with consistent indentation
- [ ] On two-cols: both columns are visible, roughly equal width, content doesn't overlap
- [ ] On image-left/image-right: image is on the correct side, text content is on the other side
- [ ] No unexpected empty space that suggests a positioning error
- [ ] Elements are vertically balanced — content isn't crammed at top or floating at bottom

#### Images (if applicable)
- [ ] Background images are visible (not blocked by opaque theme background-color)
- [ ] Background images have sufficient overlay for text readability
- [ ] Images in image-left/image-right layouts are visible and properly sized
- [ ] Image content is appropriate for the slide topic (not random, not broken)
- [ ] Images don't distract from text content — proper visual hierarchy maintained

#### Color & Palette
- [ ] Colors match the defined CSS variables / preset palette
- [ ] Accent color is used consistently across slides (headings, bullets, borders)
- [ ] No jarring color inconsistencies between slides
- [ ] Background treatment is consistent across similar slide types

#### Layout & Composition
- [ ] Layout matches the intended type (cover looks like cover, fact shows big number, etc.)
- [ ] Content density is balanced — not overcrowded, not too empty
- [ ] Whitespace is intentional and consistent
- [ ] Slide doesn't feel "broken" or "unfinished"

#### Design Principles Compliance
- [ ] **No emoji** visible — all icons are SVG-based (Principle 4)
- [ ] **Device mockups** (if any) contain wireframe UI, not empty boxes (Principle 9)
- [ ] **Diagrams** (if any) use SVG arrows, not text characters (Principle 10)
- [ ] **Charts** (if any) have value labels on key data points (Principle 8)
- [ ] **Card variety** — if multiple cards on slide, at least some visual differentiation (Principle 5)
- [ ] **Accent hierarchy** — accent color appears at varying intensities, not uniform (Principle 12)
- [ ] **Vertical balance** — content is well-distributed, not pushed to top (Principle 11)
- [ ] **Typographic drama** — key numbers/statements are oversized relative to body text (Principle 3)

#### v-click note
- Elements in initial hidden state due to `v-click`/`v-clicks` are **expected** to be invisible in static export — this is NOT a bug unless the slide is completely empty with no visible content at all.

**QA-5: Compile issues** — build a list of `slide N — [category] issue description`. If none → proceed to Phase 3.

**QA-6: Fix** — Edit tool, apply `/frontend-design` thinking, targeted fixes only. Reference `references/layout-css-patterns.md` for proven CSS patterns.

**QA-7: Iterate** — if issues were found and fixed → go to QA-2 for another cycle. Repeat until NO issues remain. The agent decides when quality is sufficient — there is no iteration limit. Only proceed to Phase 3 when the visual review passes clean.

### Phase 3: Design Critic Review

After all visual issues are resolved (or max iterations reached), perform a final holistic review as a **demanding design critic** who loves beautiful presentations and nitpicks every detail.

**QA-8: Critic pass** — Re-read all slide PNGs one final time. Step into the role of an exacting presentation designer reviewing a colleague's work. Evaluate with `/frontend-design` principles:

- **Overall cohesion**: Do all slides feel like they belong to the same presentation? Is there a consistent visual language (color, spacing, typography, decoration) across every slide?
- **First impression**: Does the cover slide make a strong opening statement? Would you remember this presentation after seeing 20 others?
- **Visual rhythm**: Is there a good alternation between high-impact slides (cover, fact, section) and content slides? Does the pacing feel intentional?
- **Typography quality**: Are fonts distinctive and well-paired? Or do they feel generic? Is the hierarchy (heading > subheading > body) clear and consistent?
- **Color conviction**: Does the palette feel bold and intentional, or timid and forgettable? Is the accent color doing work or just decorating?
- **Spatial quality**: Is whitespace generous and purposeful? Or are slides either cramped or wastefully empty?
- **Image integration** (if images present): Do images enhance the message or just fill space? Are overlays creating good text-image relationships?
- **Professional polish**: Would you be confident presenting this to a demanding audience? Any slide that feels "off" or "cheap"?
- **No AI slop**: Does anything feel like generic AI output — overused fonts, cliched gradients, predictable layouts, emoji icons, empty device mockups, text-arrow diagrams?
- **Visual rhythm**: Is there good pacing — breathing slides between dense content? Or is it an unbroken wall of information?
- **Layout diversity**: Does each slide feel like its own composition? Or do they blur into one repeating template?
- **Typographic drama**: Are key numbers/statements dramatically large? Or is everything the same cautious size?
- **Decorative personality**: Do the slides have visual character beyond content? Or are they just text on a background?
- **Visual arc**: Does the presentation build to a climax? Is the Ask/CTA slide the most visually impactful?
- **Accent system**: Is the accent color used purposefully at varying intensities? Or is it the same brightness everywhere?

**QA-9: Critic fixes** — If the critic identifies issues, fix them. These are quality-of-life improvements, not bugs — adjust colors, spacing, typography, or composition to elevate the overall feel. Apply `/frontend-design` thinking. After fixes, re-export and re-run the critic pass (QA-8). Repeat until the critic is satisfied — there is no iteration limit. The agent decides when the presentation meets the quality bar.

### Phase 4: Cleanup & Report

**QA-10: Cleanup** — `rm -rf <dir>/slides-qa`

**QA-10b: Design Memory Write (conditional)** — If Scoring Subroutine was run during this session (e.g., as part of `--polish`), write the result to Design Memory. Follow the Write Protocol in `references/design-memory.md`.

**QA-11: Report** — Include all phases:
```
Visual QA Results:
  Code review: N issues found and fixed pre-render
  Visual review: N iteration(s), [all resolved | N issues remain]
  Design critic: [pass — presentation is polished | N refinements applied]
```

<HARD-GATE>
**MANDATORY QUALITY GATES — NEVER SKIP:**
1. **Step 0.4 PDL**: When creating a new preset (NO_MATCH), you MUST run Preset Deep Learn (PDL-1 through PDL-5) with N=3. No exceptions. No "for practicality". No "the user just wants export". The preset MUST be visually validated before use.
2. **Step 7 Visual QA Loop**: After generating slides.md, you MUST run the full Visual QA Loop (Phase 1-4). No exceptions. This includes CSS code review, PNG export, per-slide visual inspection, and design critic review.
Skipping either of these gates produces untested output. If you skip them, the presentation is defective by definition regardless of how it looks.
</HARD-GATE>

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
3. **CRITICAL — MUST NOT SKIP**: Run the **Preset Deep Learn Procedure (PDL-1 through PDL-5)** with N=3 as an inline variant. This step is **mandatory** — do NOT skip it for any reason (speed, practicality, token savings, or any other justification). The entire point of auto-preset is visual validation through iterative critique. A preset without PDL is an untested guess.
   - PDL-6 (save prompt) is skipped — preset is already saved locally
   - PDL-7 (cleanup prompt) is skipped — working directory is cleaned up automatically
   - All other steps (scaffolding, 3 cycles of visual critique, auto-apply, convergence) MUST run fully
4. Continue to mode "Preset mode" with the refined preset

#### Mode Selection

1. **Preset mode**: Input contains `--preset <name|path>` (or auto-preset matched/created one) → extract preset identifier, remainder is outline
2. **Custom style mode**: Input starts with `style:` → extract style description, remainder is outline
3. **Unique mode**: `--no-preset` flag present → generate a completely unique design (current default behavior, no preset involvement)

### Outline Source

The outline can be:
- **Inline text** provided directly after the command/flags
- **File path** (e.g. `./my-outline.md`) → read the file to get the outline

Extract the outline: a structured list of slides with titles and content points.

## Hard Constraint

**The generated presentation MUST have exactly the same number of slides, in exactly the same order, with exactly the same content as the outline.** Never add, remove, merge, or reorder slides. The outline is the contract.

### Visual Rhythm Override

**When the outline has 4+ consecutive dense content slides without any natural section break**, you MUST convert 1-2 of them to a breathing layout (`statement`, `fact`, or `center`) — choosing the slide with the single most impactful number, quote, or insight. **This is NOT adding or removing slides** — it's changing the LAYOUT of an existing outline slide to create visual breathing room. The slide content is preserved but presented as a dramatic centerpiece instead of a dense grid.

**Example**: An outline slide with "Traction: +20% MoM growth, 5000 users, NPS 70" → promote "+20% MoM" to a full-screen `fact` layout with hero-sized typography, and integrate the other two metrics as small supporting text below it.

**Target**: In a 10+ slide deck, at least 2-3 slides should use breathing layouts (statement/fact/center) distributed throughout the deck. In a 15+ slide deck, at least 3-4.

## Mode: Preset

### Preset Resolution

Resolve the preset name using this 4-tier lookup (local takes priority over global):

1. **Direct path**: If the name contains `/`, `\`, or ends in `.md` → read as file path
2. **Local**: Read `./.slidev-presets/<name>.preset.md` (current project directory)
3. **Registry**: Read `~/.claude/slidev-presets.json` → look up name in the JSON object → read the mapped path
4. **Global convention**: Read `~/.claude/slidev-presets/<name>.preset.md`

If none found, emit a clear error:
```
Preset "<name>" not found. Tried:
  1. As file path: <name>
  2. Local: ./.slidev-presets/<name>.preset.md
  3. In registry: ~/.claude/slidev-presets.json
  4. Global: ~/.claude/slidev-presets/<name>.preset.md
```

### Applying Preset

Parse the preset's YAML frontmatter and body:
- Map frontmatter fields to Slidev headmatter (theme, colorSchema, fonts, aspectRatio, transition)
- Use `accentColor` for CSS variable `--slidev-theme-primary`
- Use the aesthetic description to guide layout choices, background treatments, and styling decisions
- If the preset contains a fenced `css` block, write it verbatim to `styles/index.css`

## Design Thinking (applies to Unique and Custom Style modes)

Before making any design decisions, invoke `/frontend-design` thinking AND read `references/design-principles.md`. Understand the context and commit to a BOLD aesthetic direction:

- **Purpose**: What is this presentation about? Who is the audience? A developer talk, a sales pitch, an academic lecture, and a creative portfolio all demand radically different aesthetics.
- **Tone**: Pick a clear direction — don't be generic. Options include: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian. Use these as inspiration but design one that is true to the content.
- **Differentiation**: What makes this presentation UNFORGETTABLE? What's the one thing someone will remember about its visual identity?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work — the key is intentionality, not intensity. Match implementation complexity to the aesthetic vision: maximalist designs need elaborate CSS with extensive effects; minimalist designs need restraint, precision, and careful attention to spacing and typography.

### Design Decisions Checklist (from Design Principles)

During Design Thinking, you MUST also decide:
1. **Visual rhythm plan**: Which slides will be "breathing" slides (section/statement/fact)? Map the pacing before writing any content.
2. **Layout rotation plan**: What 4-5 different layout structures will you use? Assign them across slides to avoid repetition.
3. **Decorative motif**: What 1-2 decorative elements define this presentation's personality? (geometric circles, gradient blobs, dot grids, diagonal lines, etc.)
4. **Accent hierarchy**: Define 3 levels of accent color (primary/secondary/ambient) as CSS variables.
5. **Visual arc**: Which slide is the climax? How will visual intensity build toward it?
6. **Typography scales**: Define hero (4-8em), heading (1.8-2.5em), and body (0.85-1.1em) scales.
7. **Card styles**: Which 2-3 card variations will you use and where?
8. **Icon approach**: outlined or filled SVG style? What stroke width?

### Design Memory Consultation

Before finalizing design decisions in Unique and Custom Style modes, read `~/.claude/slidev-design-memory.json` (if it exists). Follow the Read Protocol in `references/design-memory.md`. Use high-scoring patterns as inspiration (not templates) and avoid low-scoring patterns.

## Mode: Unique

Generate a completely unique design. Apply `/frontend-design` aesthetic principles:

### Font Selection
- Choose fonts that are beautiful, unique, and interesting — unexpected, characterful choices that elevate the presentation
- NEVER use generic fonts: Inter, Roboto, Arial, Open Sans, Lato, or system fonts
- NEVER converge on common AI-favorite choices (e.g., Space Grotesk) across generations
- Pair a distinctive display font with a refined body font from Google Fonts
- Good pairs: Outfit + Source Serif 4, Syne + Literata, Cabinet Grotesk + Newsreader, Plus Jakarta Sans + Fraunces, Instrument Serif + DM Sans, Bricolage Grotesque + Lora, Familjen Grotesk + Crimson Pro
- Vary between geometric/humanist sans + old-style/transitional serif
- Monospace: JetBrains Mono, Fira Code, IBM Plex Mono, Source Code Pro

### Font Number Blacklist
- **CRITICAL — Number-heavy presentations** (financial, metrics, data): NEVER select these fonts for headings — their digits render unevenly in Chromium headless export: `Syne, Playfair Display, Bodoni Moda`
- Before selecting a heading font, check if the outline contains 3+ slides with prominent numbers (budgets, metrics, percentages). If yes, verify the chosen font is NOT on the blacklist.

### Strict 2-Font Rule
- **Maximum 2 visual font identities in the entire presentation.** Heading font (sans) for: headings, numbers, labels, hero text. Body font (serif) for: descriptions, bullets, supporting text.
- Labels differ from headings only via `text-transform`, `letter-spacing`, `font-size` — same font-family.
- Hero numbers use heading font, just larger. Not a separate visual style.
- Monospace fonts used exclusively in code blocks (`<code>`, `<pre>`) do not count as a visual font identity — they serve a functional role.

### Color & Theme
- Commit to a cohesive aesthetic. Dominant colors with sharp accents outperform timid, evenly-distributed palettes
- Build a dominant palette (2-3 base colors) + one sharp accent
- Define as CSS variables: `--color-bg`, `--color-text`, `--color-accent`, `--color-surface`
- Map to Slidev variables: `--slidev-theme-primary`, `--slidev-theme-background`
- Vary between dark and light schemes across generations
- Never use plain white (#fff) or plain black (#000) as backgrounds — always tinted
- Avoid cliched color schemes (particularly purple gradients on white backgrounds)

### Backgrounds & Visual Details
- Create atmosphere and depth rather than defaulting to solid colors
- Use gradient meshes, noise textures, geometric SVG patterns, layered transparencies, dramatic shadows, or grain overlays
- Apply via CSS `background` on `:root` or specific slide classes
- Can use inline SVG data URIs for patterns
- Vary between organic (blurs, gradients) and geometric (grids, dots) across generations
- Backgrounds should add contextual effects that match the overall aesthetic

### Spatial Composition
- Use unexpected layouts where appropriate: asymmetry, overlap, diagonal flow, grid-breaking elements
- Generous negative space OR controlled density — both work when intentional
- Don't default to predictable, cookie-cutter slide layouts

### Motion & Transitions
- Match transition to the aesthetic mood
- Calm/elegant → `fade`
- Dynamic/energetic → `slide-left` or `slide-up`
- Technical → `none` or very short `fade`
- Focus on high-impact moments: one well-orchestrated reveal creates more delight than scattered micro-interactions

## Mode: Custom Style

Parse the style description after `style:`. Apply `/frontend-design` thinking to translate descriptive terms into a bold, cohesive aesthetic direction:
- Mood words → color temperature, contrast level, spatial density
- Style references (brutalist, minimal, corporate, playful) → font choices, spacing, decoration, background treatment
- Color mentions → full palette construction with dominant/accent hierarchy
- Interpret creatively — don't just map keywords literally, build a complete visual identity
- Then follow the same generation procedure as Unique mode

## Theme Support

**`--theme <name>`**: Use a non-default Slidev theme. This is a modifier — combine with generation modes (unique, preset, custom style). Example: `/slidev --theme seriph <outline>`.

### Supported Themes
- **Primary**: `default` (current behavior), `seriph`, `apple-basic`
- **Experimental**: `bricks`, `shibainu`, `penguin`, `dracula`
- **Unknown**: print warning, attempt best-effort generation

### Generation Changes

**Step 2 (package.json)**: If `--theme` is not `default`, replace `"@slidev/theme-default": "latest"` with `"@slidev/theme-<name>": "latest"`.

**Step 5 (slides.md headmatter)**: Set `theme: <name>`.

**Step 4 (styles/index.css)**: For non-default themes, skip theme-default-specific CSS overrides (blockquote reset, explicit text-align for centered layouts). Instead add:
```css
/* Theme: <name> — theme-specific overrides may be needed.
   Check exported PNGs for CSS specificity issues. */
```

### Visual QA Theme Conditioning

Rules about `@slidev/theme-default` CSS specificity (Rules 9, 10, 24, 29, 32) become conditional:
- If `theme == "default"`: apply these rules as written
- If `theme != "default"`: skip these rules. Instead, during QA-4 visual review, pay extra attention to text alignment, background rendering, and blockquote styling — flag any visual issues that suggest theme CSS conflicts.

### Theme Detection in Post-Generation Operations

`--polish`, `--edit`, `--compare` and other post-generation subcommands detect the current theme by reading `theme:` from `slides.md` headmatter. This theme context is passed to Visual QA and A/B testing steps.

## Generation Procedure

### Step 1: Resolve Design Parameters

Apply the Design Thinking section above (for Unique/Custom Style modes) or parse the preset (for Preset mode). Based on mode, determine:
- `theme`: Slidev theme (usually `default`)
- `colorSchema`: `light` or `dark`
- `fonts`: `{ sans, serif, mono }` from Google Fonts
- `palette`: CSS variables for colors
- `transition`: default slide transition
- `aspectRatio`: usually `16/9`
- `backgroundCSS`: CSS for backgrounds/textures
- `aesthetic`: free-text description for guiding per-slide decisions

### Step 2: Scaffold package.json

```json
{
  "name": "<project-name>",
  "private": true,
  "scripts": {
    "dev": "slidev",
    "build": "slidev build",
    "export": "slidev export"
  },
  "dependencies": {
    "@slidev/cli": "latest",
    "@slidev/theme-default": "latest"
  }
}
```

If using a non-default theme, add the theme package to dependencies.

### Step 3: Write uno.config.ts

```ts
import { defineConfig } from 'unocss'

export default defineConfig({
  shortcuts: {
    'slide-heading': 'text-4xl font-bold tracking-tight',
    'slide-subheading': 'text-2xl font-light opacity-80',
    'slide-accent': 'text-[var(--color-accent)]',
  },
})
```

Customize shortcuts based on the design aesthetic.

### Step 4: Write styles/index.css

Include:
- CSS variable definitions (palette) — **MUST include 3-level accent hierarchy** (Principle 12): `--color-accent` (full), `--color-accent-dim` (40-60% opacity), `--color-accent-bg` (8-15% opacity)
- Background textures/gradients
- Font overrides if needed
- Custom utility classes
- **Card style variants** (Principle 5): `.card-solid`, `.card-ghost`, `.card-accent`, `.card-glass` — at least 2-3 distinct styles
- **Decorative motif classes** (Principle 6): CSS pseudo-element patterns for the chosen decorative motifs (geometric circles, gradient blobs, dot grids, diagonal lines, etc.)
- If preset mode with CSS block, write the preset's CSS verbatim (can extend but not contradict)

### Step 4.5: Composition Planning

Before writing slides, create a Composition Plan that maps each outline slide to a named archetype from `references/composition-archetypes.md`. This replaces ad-hoc layout selection with structured, content-aware composition.

**Procedure:**

1. **Read preset archetypes** (if present): load `preferred` and `avoid` lists from the preset's `archetypes` section. If no archetypes section, use empty defaults.

2. **Classify each slide's content type**: For each slide in the outline, determine its content type from this taxonomy:
   - `intro` — first slide, company/product name
   - `credentials` — experience, stats, certifications
   - `context` — task description, parameters
   - `vision` — visualization, concept, design
   - `scope` — list of works, features
   - `process` — stages, timeline, steps
   - `team` — people, roles
   - `metric` — key number, budget, KPI
   - `portfolio` — cases, projects, examples
   - `trust` — guarantees, quality control
   - `terms` — conditions, legal, payment
   - `cta` — call to action, contacts

3. **Select archetype for each slide** using the mapping table in `references/composition-archetypes.md`:
   a. Get candidate archetypes from content type mapping
   b. Remove any archetypes in the preset's `avoid` list
   c. Remove archetypes used in the last 3 slides (entropy window = 4)
   d. If previous slide was high-density, prefer low/medium-density candidates
   e. If a candidate is in the preset's `preferred` list AND matches the content type, select it (tie-breaker)
   f. Select the most suitable remaining candidate
   g. **Fallback**: if empty after filtering → relax entropy window to 2 and retry. If still empty → ignore density filter AND entropy window, select the candidate with the lowest recent-use count.

4. **Validate deck-level constraints**:
   - Every 10-slide deck contains minimum: 1 low-density, 1 medium, 1 high-density archetype
   - No more than 2 consecutive high-density archetypes
   - At least 3 different archetype groups (hero/grid/split/timeline/table/cta) in any 10-slide deck
   - `profile-grid` appears at most once per deck
   - Cover archetype always first, CTA archetype always last

5. **Output Composition Plan** as a table in the generation context:
   ```
   | Slide | Content Type | Archetype | Group | Density |
   |-------|-------------|-----------|-------|---------|
   | 1     | intro       | cover-hero | hero | low     |
   | 2     | credentials | bento-grid | grid | medium-high |
   ...
   ```

This plan is consumed by Step 5: for each slide, use the archetype's HTML skeleton from `references/composition-archetypes.md` and fill `{{SLOT}}` markers with content from the outline. Apply the preset's shape vocabulary when rendering elements.

### Step 5: Write slides.md

Structure:
1. **Headmatter** — theme, title, fonts, colorSchema, transition, aspectRatio, etc.
2. **Slides** — each separated by `---`, with per-slide frontmatter

For each slide in the outline:

1. **Use the Composition Plan from Step 4.5**: For each slide, look up its assigned archetype. Use `layout: none` and the archetype's HTML skeleton from `references/composition-archetypes.md`. Fill `{{SLOT}}` markers with content from the outline. Apply the preset's shape vocabulary (icon containers, stat display style, label style, photo masks) when rendering elements within the skeleton.

   If no Composition Plan exists (Step 4.5 was not executed for any reason), fall back to the legacy layout selection:
   - Title/intro → `cover`
   - Section break → `section`
   - Bullet points → `default`
   - Single statement → `statement` or `center`
   - Statistic → `fact`
   - Quote → `quote`
   - Comparison → `two-cols`
   - Closing → `end`

   **CRITICAL — Visual Rhythm (Principle 1)**: Insert `section`, `statement`, or `fact` breathing slides every 2-3 content slides. If the outline doesn't explicitly include them, use section dividers between major topic shifts, or promote a key insight from a content slide into a standalone statement/fact slide.

   **CRITICAL — Layout Diversity (Principle 2)**: Do NOT repeat the same visual structure (heading position + content arrangement) on more than 2 consecutive slides. Rotate between: hero-left/content-right, cards grid, timeline/stepper, centered hero, asymmetric split, full-bleed visual, comparison table, quote/callout. Track your layout choices — if you used "title top-left + 2-column grid" on slide 3, use something different on slide 4.

2. **Apply animations**:
   - Bullet lists → wrap in `<v-clicks>`
   - Code blocks → use step highlighting `{1|2-3|5}`
   - Key reveals → use `<v-click>`

3. **Style with UnoCSS** classes for spacing, alignment, typography

4. **Add per-slide `<style>`** block — REQUIRED for centered layouts. Reference `references/layout-css-patterns.md` for proven CSS patterns. For `cover`, `section`, `fact`, `end`, `statement`, `center` layouts: ALWAYS include explicit `text-align: center` on `h1`, `p`, and other text elements. For slides with background images: use CSS `background:` on `.slidev-layout` (not frontmatter prop), add `::before` overlay, and set white text colors.

5. **Apply Typographic Drama (Principle 3)**: Key numbers and metrics must use hero scale (4-8em). Statement/fact slides should have 3-5em text minimum. Ensure at least 3 distinct type scales across the presentation.

6. **Apply Visual Arc (Principle 7)**: Make the climax slide (usually Ask/CTA) the most visually distinct — different background, larger type, unique color treatment. Build visual intensity gradually from calm beginning to dramatic climax.

7. **Apply Vertical Spacing (Principle 11)**: Content should feel vertically balanced. Use flexbox centering or generous padding. Content should not cram to the top leaving empty bottom space.

8. **Apply Decorative Layer (Principle 6)**: Add the chosen decorative motifs to 30-50% of slides as CSS pseudo-elements or background layers. Vary placement (corner circles, bottom blobs, side lines) for visual interest.

### Step 6: Write Custom Components (REQUIRED)

**ALWAYS create these components** for every presentation:

**6a. Icon component (REQUIRED — Principle 4)**: Create `components/Icon.vue` using the template from `references/design-principles.md`. This replaces ALL emoji usage. Include icons relevant to the presentation topic. Use `<Icon name="..." :size="32" color="var(--color-accent)" />` in slides.

**6b. Custom cards/metrics** (if needed): Create component variants with different visual styles per Principle 5 (Card Variation). Not all cards should look identical.

**6c. Device mockups** (if showing product UI — Principle 9): If the presentation shows phone/laptop screens, create a `components/PhoneMock.vue` with proper wireframe UI — status bar, navigation, colored placeholder blocks, buttons. NEVER create empty gray rectangles with text labels.

**6d. Other custom elements** (animated counters, gradient text, etc.): Create Vue SFCs in `components/`:

```vue
<!-- components/GradientText.vue -->
<template>
  <span class="gradient-text"><slot /></span>
</template>

<style scoped>
.gradient-text {
  background: linear-gradient(135deg, var(--color-accent), var(--color-primary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
```

Components in `components/` are auto-registered and available in slides.

**6e. SVG diagrams (Principle 10)**: For flywheel, flow charts, cycles — use inline SVG in slides with proper `<path>` arrows and `<marker>` arrowheads. See `references/design-principles.md` for SVG patterns. NEVER use text arrows (→ ↓ ← ↑) or CSS absolute positioning to simulate diagrams.

### Step 6.5: Picture Placement (conditional)

If `--picture` modifier is present on the generation command, run the Picture Placement Procedure (P-1 through P-7) on the generated project directory. This adds images to the slides before the Visual QA step verifies them.

### Step 7: Visual QA

**CRITICAL — MUST NOT SKIP.** Run the full Visual QA Loop (all 4 phases) for `<project-dir>`. This is mandatory after EVERY generation, regardless of whether `--export` is also specified. Export happens AFTER Visual QA, not instead of it.

### Step 8: Output Summary

After writing all files, print (include Visual QA results):

```
Created Slidev presentation:

  <project-dir>/
    package.json
    slides.md
    uno.config.ts
    styles/
      index.css
    components/       (if created)
      ...
    public/           (if created)
      ...

To run:
  cd <project-dir>
  npm install
  npm run dev
```

## Slide Authoring Rules

1. **v-clicks for bullets**: Always wrap bullet lists in `<v-clicks>` for progressive reveal. **CRITICAL — v-clicks compatibility**: `v-clicks` and `v-click` ONLY work reliably on standard Markdown content (bullet lists, paragraphs) at the top level of a slide, NOT inside custom HTML `<div>` wrappers. If a slide uses a custom HTML layout (flex grids, card containers, custom steppers), DO NOT use `v-clicks` — either present the slide as static, or restructure it to use only Markdown content at the top level with layout applied via global CSS classes on a single root wrapper div.
2. **Step highlighting for code**: Use `{1|2-3|5}` syntax for code walkthroughs
3. **Layout matching**: Choose layout per slide based on content type — don't default everything to `default`
4. **Scoped styles**: Use per-slide `<style>` blocks for slide-specific styling
5. **UnoCSS utilities**: Use utility classes for spacing, flex, grid — avoid inline styles
6. **Presenter notes**: Add `<!-- notes -->` with speaking points when the outline suggests them
7. **No placeholder images**: Don't reference images that don't exist. Use CSS gradients, SVG patterns, or Icon components as visual elements instead
8. **Semantic HTML**: Use proper heading hierarchy within each slide
9. **CRITICAL — Explicit text-align on centered layouts**: For `cover`, `section`, `fact`, `end`, `statement`, `center` layouts — ALWAYS set `text-align: center` explicitly on `h1`, `h2`, `p`, `li`, `div` in the per-slide `<style>` block. NEVER rely on inheritance from the parent `.slidev-layout` — Slidev themes override inherited `text-align` with higher-specificity selectors. See `references/layout-css-patterns.md`.
10. **CRITICAL — Background images via CSS, not frontmatter**: When adding background images to `cover` or `section` slides, set the background via per-slide `<style>` CSS (`background: url(...) center/cover no-repeat !important` on `.slidev-layout`), NOT via the `background:` frontmatter prop. The frontmatter prop renders on a parent element, but the theme's opaque `background-color` on `.slidev-layout` blocks it. Per-slide CSS overrides the theme directly.
11. **CRITICAL — No emoji icons (Principle 4)**: NEVER use emoji (📱💳⭐🧠📊 etc.) as visual elements. Always use the `<Icon>` component with SVG icons that match the presentation's style. Emoji are inconsistent across platforms and look unprofessional.
12. **CRITICAL — No empty mockups (Principle 9)**: Device mockups (phones, laptops) must contain wireframe-level UI — status bar, navigation, colored placeholder blocks, buttons. NEVER show empty gray rectangles with text labels.
13. **SVG diagrams (Principle 10)**: For flywheels, flow charts, cycles — use inline SVG with `<path>`, `<marker>`, and proper arrowheads. NEVER simulate diagrams with CSS absolute positioning and text arrow characters. **CRITICAL — SVG `<text>` element incompatibility**: NEVER use `<text>` elements inside inline SVG diagrams in Slidev. Chromium's headless export renderer treats SVG `font-size` attributes as document-scale CSS pixels, causing text to render 5–15× larger than expected and overflow the containing shapes. Instead: (A) use a CSS flexbox HTML flow diagram for any diagram requiring text labels (flex column of styled divs with CSS arrows between them), or (B) if SVG shape-only diagrams are needed, keep them label-free. SVG `<path>`, `<rect>`, `<circle>`, `<line>`, `<marker>`, and `<polygon>` elements without `<text>` are safe.
14. **Data viz labels (Principle 8)**: Bar charts must show value labels on key bars. Tables must highlight the hero column. Donut/pie charts must have text labels.
15. **Card diversity (Principle 5)**: Use 2-3 visually distinct card styles (solid, ghost, gradient, glass) — not the same surface style everywhere.
16. **Accent hierarchy (Principle 12)**: Use accent color at 3 intensities: primary (full), secondary (40-60% opacity), ambient (8-15% opacity). Don't use full-intensity accent everywhere.
17. **CRITICAL — Image path discipline**: Never generate `background: url('/images/...')` unless (a) the `--picture` subcommand was invoked and the file exists, OR (b) a CSS-only atmospheric fallback is provided that looks good WITHOUT the image. For cover/section slides without real images, use multi-layer CSS gradients + decorative pseudo-elements to create atmosphere. Example: `background: radial-gradient(ellipse 80% 60% at 30% 40%, rgba(accent, 0.12), transparent 60%), radial-gradient(ellipse 60% 80% at 80% 70%, rgba(secondary, 0.15), transparent 60%), var(--color-bg);`
18. **CRITICAL — Icon name verification**: Before using `<Icon name="X">`, verify that `X` is defined in Icon.vue's `v-if` branches. If a new icon is needed, ADD it to Icon.vue first. Never reference an undefined icon name. Icon.vue should include a `v-else` fallback that renders a visible placeholder (a question-mark circle) so missing icons are immediately obvious during QA.

    **Icon centering**: When an `<Icon>` must appear centered (e.g., in a card header or feature cell), always wrap it in an explicit flex div: `<div style="display:flex;justify-content:center;align-items:center;margin-bottom:8px;"><Icon name="..." /></div>`. Do NOT rely on the card's parent flex/grid container to center an inline SVG element — `<Icon>` renders as `display:inline` by default and will left-align within block containers without an explicit centering wrapper.
19. **CRITICAL — HTML nesting depth limit**: Keep HTML nesting to maximum 3 levels deep inside slides. Slidev's markdown parser fails to render deeply nested HTML — it outputs raw source code instead of rendered content. Flatten structures: instead of `<div><div><div><table>...</table></div></div></div>`, use `<table>` directly at the top level of the slide. Use UnoCSS utility classes on elements themselves instead of wrapping in container divs. When a complex layout is needed, prefer CSS Grid/Flexbox on a single wrapper div rather than nesting multiple wrappers. **Test pattern**: if you count more than 3 opening `<div>` tags before reaching the actual content element, you need to flatten.
20. **CRITICAL — Minimum readable font size**: Body text and card content must be at least `text-sm` (14px / 0.875rem). Use `text-xs` (12px) ONLY for footnotes, source attributions, or slide numbers — never for content the audience needs to read. Presentations are viewed on screens and projectors, not read on a monitor. If content doesn't fit at 14px+, the slide has too much content — split it across two slides or move details to presenter notes.
21. **Maximum items per action/list slide**: A single content slide MUST NOT exceed 4 distinct items or bullet points with descriptions. If an outline section has 5+ items, split across 2 slides with a clear part indicator, or reduce to the 3 most critical items and place others in speaker notes. Action plan slides with 5+ steps are particularly prone to density failure.
22. **Maximum visual blocks per slide**: A content slide should contain at most 4-5 distinct visual elements (cards, chart sections, tables, list groups). If the outline demands more content on one slide, SPLIT it into 2 slides or PRIORITIZE the 3-4 most impactful elements and move details to presenter notes. Exception: a single data table counts as one visual block even if it has many rows.
23. **CRITICAL — Per-slide CSS reliability hierarchy**: When styling slides with custom HTML layouts, follow this reliability order from most to least reliable: (1) Per-slide `<style>` with a SINGLE root wrapper div containing all content — works reliably when all slide content is inside one top-level element. (2) 100% inline styles on every element — most reliable for complex multi-column or deeply nested layouts. (3) Never rely on per-slide CSS classes applying to elements more than 2 nesting levels deep. If a slide requires 3+ levels of nesting, use 100% inline styles instead of CSS class names. Note: this reliability constraint is separate from the nesting depth rendering limit (Rule 19) — both apply simultaneously.
24. **CRITICAL — `end` layout background override**: The `@slidev/theme-default` `end` layout applies an opaque dark background that cannot be overridden without `!important`. To set a custom background on an `end` slide, use BOTH: `background: <color> !important; background-color: <color> !important;` in the per-slide `<style>` block. Setting only `background` is insufficient. Also explicitly set `color` on all child text elements, as the theme defaults to white text for the dark end layout.
25. **CRITICAL — Full-bleed slide layout height guarantee**: When building custom full-bleed slides using a background div + content div pattern, NEVER use `height:100%` on the content wrapper. Slidev injects padding into `.slidev-layout` that makes `height:100%` smaller than the full viewport, pushing `justify-content:center` content downward. Instead, use `position:absolute;inset:0` on BOTH the background and content wrappers:
    ```html
    <!-- Background layer -->
    <div style="position:absolute;inset:0;z-index:0;overflow:hidden;">
      <!-- decorative elements -->
    </div>
    <!-- Content layer -->
    <div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;padding:48px 80px;">
      <!-- slide content -->
    </div>
    ```
    Also set `padding:0 !important; overflow:hidden` on `.slidev-layout` in the per-slide `<style>` block as a supplementary safeguard.
26. **CRITICAL — Tag pill / accent chip on dark backgrounds**: `rgba(accent, 0.10–0.18)` background ONLY works on light/white backgrounds. On dark backgrounds (luminance < 30%), this formula produces a muddy dark tint — use one of these alternatives instead: (A) `background: rgba(255,255,255,0.08)` + `border: 1.5px solid rgba(accent, 0.60)` — "ghost chip with bright border"; (B) raise opacity to `rgba(accent, 0.25–0.30)` on dark slides; (C) fully saturated `background: rgba(accent, 1.0)` for small micro-chips. NEVER use `rgba(accent, 0.10–0.18)` as a chip background when the slide background is navy, charcoal, or any color with luminance below 25%.
27. **MANDATORY — Background variation in 3+ consecutive same-chapter content slides**: When 3+ content slides of the same type appear in sequence (e.g., three value slides), each slide MUST differ from its neighbors on at least one background dimension. Apply at minimum ONE of: (A) Progressive background lightening — shift 2–4% luminance per slide; (B) Decorative motif rotation — each slide gets a different motif (diagonal lines, dot grid, arc ring — never the same motif on two adjacent slides); (C) Accent blob corner rotation — place decorative blobs in different corners across the sequence. Identical backgrounds on 3+ consecutive content slides = visual rhythm failure.
28. **CRITICAL — Ghost decorative number opacity enforcement**: When using large background numerals ("01", "02") as decorative elements on content slides, apply the hue proximity rule (Principle 6): on warm peach/cream backgrounds, pink ghost numbers require minimum opacity **0.20** (same temperature family). On warm backgrounds, use navy ghost numbers at minimum **0.10** opacity instead — navy provides stronger contrast than same-hue pink. Any ghost number at opacity below 0.15 on a warm background will be invisible in exported PNGs. If you cannot meet the minimum opacity without it looking too heavy, remove the ghost number entirely rather than keeping an invisible element.
29. **CRITICAL — Override blockquote default styling**: `@slidev/theme-default` applies an opaque dark background (`background: <dark color>`) and a left accent border (`border-left: 4px solid var(--slidev-theme-primary)`) to ALL `<blockquote>` elements. Any slide using `<blockquote>` for a quote or statement will render as a "callout box" — not clean typographic text. ALWAYS add the following reset to `styles/index.css` for every presentation:
    ```css
    .slidev-layout blockquote {
      background: transparent !important;
      border-left: none !important;
      border: none !important;
      padding: 0 !important;
      margin: 0 !important;
      color: inherit !important;
    }
    ```
    Additionally, for centered layouts (statement/center/fact/end), set `text-align: center` explicitly on the `<blockquote>` element itself AND on every `<p>` inside it — flex container centering alone is insufficient because `<blockquote>` renders as a block element that can inherit left-alignment from theme selectors.
30. **CRITICAL — Content grid vertical centering (two-layer pattern)**: When a content slide uses `position:absolute;inset:0` layout with a label + heading + content grid/list, DO NOT put `justify-content:center` on the outer wrapper div. This centers the entire column (heading + content) as a block, which pulls the visual center upward by the heading height (~100-120px) and leaves an empty gap at the bottom. Instead, use the **two-layer pattern**:
    - Outer wrapper: `position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px 44px` — NO `justify-content`
    - Label + heading block: static top-anchored, no special flex behavior
    - Content grid/list container: `flex:1;display:flex;flex-direction:column;justify-content:center` — centers the CONTENT within the space BELOW the heading
    ```html
    <div style="position:absolute;inset:0;z-index:1;padding:44px 64px 44px;display:flex;flex-direction:column;">
      <div style="...label styles...">LABEL</div>
      <h1 style="...heading styles;margin:0 0 20px;">Heading</h1>
      <!-- Content is centered in the remaining space -->
      <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:12px;">
        <!-- cards/rows/items here -->
      </div>
    </div>
    ```
    This ensures the heading anchors near the top while the content block centers in the remaining space, producing vertically balanced slides with content visible throughout the middle 60% of the slide height.

    **Grid rows for 4+ item lists (PREFERRED over space-evenly)**: When a content slide has a heading consuming >20% of slide height AND the content area contains 4+ items (cards, rows, list items), use `display:grid;grid-template-rows:repeat(N,1fr)` on the content container (where N = number of items), with `align-items:stretch`. Then give each item `height:100%;display:flex;align-items:center` so it fills its grid cell. This guarantees equal distribution regardless of item content size.

    `justify-content:space-evenly` is **NOT reliable** for vertical item lists: it only distributes whitespace BETWEEN auto-height items without stretching them — items cluster in the upper portion with a gap at the bottom. Reserve `space-evenly` only for horizontal flex containers where items have equal natural widths.

    ```html
    <!-- ✅ CORRECT: Grid 1fr rows — items stretch to fill available height -->
    <div style="flex:1;display:grid;grid-template-rows:1fr 1fr 1fr 1fr;gap:12px;align-items:stretch;">
      <div style="display:flex;align-items:center;gap:16px;background:...;border-radius:14px;padding:0 24px;">
        <!-- icon + text — no fixed padding-top/bottom; height comes from grid row -->
      </div>
      <!-- repeat for each item -->
    </div>

    <!-- ❌ WRONG: flex+space-evenly leaves gap at bottom when items have auto heights -->
    <div style="flex:1;display:flex;flex-direction:column;justify-content:space-evenly;gap:12px;">
      <div style="...;padding:20px 24px;">...</div>
    </div>
    ```

31. **CRITICAL — Blank slide prevention (separator + frontmatter discipline)**: When a slide requires per-slide frontmatter (`layout`, `transition`, `class`, etc.), the frontmatter block MUST immediately follow the `---` separator with NO blank lines, HTML comments, or other content between the `---` and the opening `---` of the frontmatter. Placing a comment or blank line between them creates TWO slides — one blank and one with content. **Correct pattern:**
    ```markdown
    ---
    layout: section
    ---

    <!-- comment about this slide goes HERE, after the frontmatter -->
    Slide content here
    ```
    **Wrong pattern (creates blank slide):**
    ```markdown
    ---

    <!-- comment about next slide -->
    ---
    layout: section
    ---
    ```
    For full-HTML custom slides using `layout: none`, consolidate the separator and frontmatter into a single block with the HTML content immediately following.

32. **CRITICAL — statement/fact layout CSS override limitation**: The `@slidev/theme-default` `statement` and `fact` layouts apply font sizes, text alignment, and colors with high-specificity CSS selectors that per-slide `<style>` blocks cannot reliably override. Symptoms: setting `h1 { font-size: 2.5em }` in a per-slide style for a `statement` slide renders at the theme default (~1em) instead. **Fix**: For any `statement` or `fact` slide requiring custom typography or visual treatment beyond what the theme provides, use `layout: none` with a full custom HTML div using inline styles. Reserve `layout: statement` and `layout: fact` ONLY when the theme's default rendering is acceptable.

33. **Non-default theme exploratory render**: For non-default themes, perform an exploratory render before full generation. Write a minimal 2-slide test (`cover` + `default` layout), export PNGs, check for unexpected styling. If the theme applies unusual defaults (different font rendering, unexpected background colors, unusual spacing), note them and adapt the generation accordingly. This prevents wasting a full generation on a theme that behaves unexpectedly.
34. **Theme + preset interaction**: When using `--theme` with `--preset`, the preset's CSS block takes precedence over theme defaults. Theme provides base styling; preset provides customization layer on top. If the preset was designed for `theme: default`, it may not work correctly with other themes — warn the user if the preset's `theme` field doesn't match the `--theme` flag.

## Design Quality Rules (powered by /frontend-design + Design Principles)

These rules combine `/frontend-design` aesthetic principles with the Gamma-level design principles from `references/design-principles.md`. Apply in ALL modes.

### Aesthetic Foundation
1. **Never repeat aesthetics**: Each unique-mode generation should feel different — vary dark/light, geometric/organic, warm/cool. No design should look the same across generations
2. **Typography drives design**: Font choice sets the tone. Choose fonts that are beautiful, unique, and characterful. Pair a distinctive display font with a refined body font. NEVER default to generic AI-favorite fonts
3. **Color with conviction**: Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Ensure accent color has sufficient contrast against backgrounds and text. Avoid cliched color schemes
4. **Whitespace is design**: Don't overcrowd slides. Generous negative space OR controlled density — both work when intentional
5. **Consistent visual language**: Once you choose a visual direction (e.g., rounded vs sharp, dense vs airy), maintain it across all slides with precision
6. **Background depth**: Create atmosphere and depth — gradient meshes, noise textures, geometric patterns, layered transparencies, grain overlays. Never default to flat solid colors
7. **Transition coherence**: Match transition style to overall aesthetic — don't mix competing motion styles
8. **No AI slop**: Never use generic AI-generated aesthetics — overused fonts (Inter, Roboto), cliched purple-on-white gradients, predictable layouts, cookie-cutter patterns, emoji as icons, empty device mockups, text-arrow diagrams. Every presentation must feel genuinely designed for its specific content and context
9. **Spatial intentionality**: Use unexpected layouts where appropriate — asymmetry, overlap, grid-breaking elements. Avoid predictable, evenly-spaced component patterns

### Presentation-Specific Quality (from Design Principles)
10. **Visual rhythm**: Alternate dense content slides with breathing slides (section/statement/fact). Never 3+ dense slides in a row. See Principle 1.
11. **Layout diversity**: Every slide must be visually distinguishable from its neighbors. Rotate 4-5 different layout structures per deck. See Principle 2.
12. **Typographic drama**: Use 3+ distinct type scales (hero 4-8em, heading 1.8-2.5em, body 0.85-1.1em). Key numbers must be oversized. See Principle 3.
13. **Professional iconography**: SVG icons via `<Icon>` component only. Zero emoji. See Principle 4.
14. **Card differentiation**: 2-3 visually distinct card styles per presentation. See Principle 5.
15. **Decorative personality**: 1-2 decorative motifs on 30-50% of slides. See Principle 6.
16. **Visual narrative arc**: Build visual intensity toward the climax (Ask/CTA). See Principle 7.
17. **Data viz polish**: Charts with value labels, highlighted hero columns, SVG with labels. See Principle 8.
18. **Realistic mockups**: Device frames with wireframe UI, not empty boxes. See Principle 9.
19. **Vector diagrams**: SVG diagrams with proper arrows, not CSS+text. See Principle 10.
20. **Vertical balance**: Content centered or well-distributed, not crammed to top. See Principle 11.
21. **Accent weight system**: 3 levels of accent intensity (primary/secondary/ambient). See Principle 12.
22. **Content density limit**: Max 4-5 visual blocks per slide. If a slide needs 6+ elements, split into 2 slides or move secondary details to presenter notes. Dense information walls overwhelm the audience and shrink text to unreadable sizes.
23. **Hero metric prominence**: When a slide shows 3-4 key metrics, DON'T make them all equal-sized cards. Pick the MOST impactful metric, make it hero-sized (centered, 3-6em), place the rest as smaller supporting elements below. If all metrics are equally important, use 2.5-3em minimum — never smaller than the heading text.
24. **Visible decoration**: Decorative elements (grain, scanlines, dot grids, blobs) must be visible in exported PNGs. Minimum opacity: 0.08-0.15 for patterns. If a decorative element isn't noticeable in a static screenshot, increase its opacity or size. Better 2-3 clearly visible decorative touches than 10 invisible ones.
25. **Font discipline**: Maximum 2 visual font identities per presentation (heading + body). Numbers, labels, and hero text use the heading font — never a third font. Check font number blacklist for number-heavy decks. See Font Number Blacklist in Mode: Unique.

## Output Directory

- If user specifies a directory, use it
- Otherwise create a directory named after the presentation title (kebab-case)
- If generating a demo for a preset, use `demo-<preset-name>/`
