# Research-Driven Presentation Quality Improvements Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement 20 research-backed quality improvements across the slidev skill — typography, color, content structure, data viz, layout, and cross-cutting QA enforcement.

**Architecture:** All changes target 5 existing files. Each rule is enforced cross-cuttingly: generation + QA + edit + scoring + critic. New QA-0c phase adds anti-pattern scanning before render.

**Tech Stack:** Slidev skill files (Markdown), reference documents.

**Spec:** `docs/superpowers/specs/2026-03-21-research-driven-improvements-design.md`

---

## File Structure

| File | Action | Changes |
|------|--------|---------|
| `.claude/skills/slidev/SKILL.md` | Modify | Rules 9/18/20 updated, 12 new rules (29-40), QA-0a narrowed, QA-0c added, QA-4 enhanced, Step 4.5/5 updated, --edit updated, L-3c/PDL-2.3 updated, Picture P-3 updated |
| `.claude/skills/slidev/references/design-principles.md` | Modify | Principle 8 expanded (chart rules), Principle 12 expanded (60-30-10), new Anti-Patterns Quick Reference section |
| `.claude/skills/slidev/references/scoring-subroutine.md` | Modify | Enhanced checks in 6 of 9 axes |
| `.claude/skills/slidev/references/layout-css-patterns.md` | Modify | Centered layout body text → left-align |
| `.claude/skills/slidev/references/composition-archetypes.md` | Modify | All body font sizes raised to ≥1.25rem |

---

### Task 1: SKILL.md — Typography & Content Rules (gaps 1, 2, 3, 14, 16, 20)

**Files:**
- Modify: `.claude/skills/slidev/SKILL.md:1334` (Rule 9)
- Modify: `.claude/skills/slidev/SKILL.md:1347` (Rule 20)
- Modify: `.claude/skills/slidev/SKILL.md:1473` (after last rule 28)

- [ ] **Step 1: Update Rule 9 — narrow centered text to headings only**

Find Rule 9 (line 1334). Replace the rule text. Keep the rule number and CRITICAL label. Change the body to:

```
9. **CRITICAL — Text alignment on centered layouts**: For `cover`, `section`, `fact`, `end`, `statement`, `center` layouts — set `text-align: center` on `h1`, `h2` and single-line elements (date, subtitle, attribution) in the per-slide `<style>` block. **Multi-line body text** (`p`, `li`, `span` with >60 characters or >1 line of content) MUST be `text-align: left` with `max-width: 600px; margin: 0 auto` — left-aligned text in a centered container. NEVER center bullet lists or multi-line paragraphs — this is a major readability anti-pattern. See `references/layout-css-patterns.md`.
```

- [ ] **Step 2: Update Rule 20 — new font size minimums**

Find Rule 20 (line 1347). Replace entirely:

```
20. **CRITICAL — Font size minimums**: Body text minimum `1.25rem` (20px). Headings minimum `2.2rem` (35px). Labels/captions minimum `0.85rem` (13.6px). Hero numbers minimum `4rem` (64px). Footnotes (only exception) minimum `0.75rem` (12px). Use `text-xs` (12px) ONLY for footnotes and source attributions — never for audience-readable content. If content doesn't fit at 1.25rem, the slide has too much content — split it or move details to speaker notes.
```

- [ ] **Step 3: Add new rules 29-36 after rule 28**

After rule 28 (line 1473, "CTA color smoothness"), append:

```
29. **Word count limits**: Maximum 40 words per content slide. 75+ words = CRITICAL "wall of text" — rewrite immediately. 150+ words = FORBIDDEN (document, not slide). Maximum 12 words per bullet point. Maximum 6 text lines per slide. Exception: table/comparison slides allow up to 60 words. If content exceeds limits, split across slides or move to speaker notes.
30. **Action titles**: Every slide title MUST be a statement/insight, not a label. "Выручка выросла на 23%" not "Финансовые показатели". "18 лет опыта в строительстве МО" not "О компании". Ghost Deck test: reading only slide titles in sequence must tell a coherent story. Exception: cover and CTA slides may use short titles.
31. **Generic phrase prohibition**: These phrases are BANNED as slide titles: "Ключевые выводы", "Обзор", "В заключение", "Наше решение", "Наш подход", "О нас", "Введение", "Итоги", "Резюме", "Key Takeaways", "Overview", "In Conclusion", "Our Approach", "Summary". Test: could any competitor send this presentation changing only the logo? If yes — titles are too generic.
32. **All-caps eyebrow labels limit**: All-caps uppercase labels (`text-transform: uppercase; letter-spacing`) allowed on max 30% of slides. Others use normal-case with accent color, or no label. Labels must be specific: "Q1 2025" not "ОБЗОР", "МОСКВА · 120 ТОЧЕК" not "КОНТЕКСТ".
33. **"Thank You" ending prohibition**: Last slide NEVER ends with "Спасибо", "Thank You", or "Вопросы?". Last slide = specific CTA with action and contact info. Use `cta-warm` archetype.
34. **Bold/emphasis limits**: Maximum 10-15% of text may be bold. Maximum 1 emphasis technique per element (bold OR accent color OR larger size — not all three simultaneously). Over-emphasis defeats emphasis.
35. **Line-height**: Body text `line-height: 1.3–1.45`. Headings `line-height: 1.05–1.15`. Values below 1.2 (too tight) or above 1.5 (too loose) for body text = WARNING.
36. **Sub-bullet depth limit**: Maximum 2 levels of bullet nesting. Sub-sub-bullets are forbidden. If hierarchy deeper than 2 is needed, restructure as cards, separate blocks, or split across slides.
```

- [ ] **Step 4: Commit**

```bash
cd C:/Users/progr/Workspace/kama-skills && git add slidev/.claude/skills/slidev/SKILL.md && git commit -m "feat(slidev): update typography rules and add content quality rules 29-36

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 2: SKILL.md — Color & Anti-AI Rules (gaps 5, 7, 8, 13, 15, 17, 18, 9)

**Files:**
- Modify: `.claude/skills/slidev/SKILL.md:1473+` (after rules from Task 1)

- [ ] **Step 1: Add rules 37-44 after rule 36**

Append after rule 36 (added in Task 1):

```
37. **AI color blacklist**: These colors are BANNED as primary/dominant accent: any hue in range 240-290 (purple-indigo-violet spectrum) at saturation >50%. Specific examples: `#6366F1` (indigo-500), `#8B5CF6` (violet-500), `#A855F7` (purple-500), `#06B6D4` (cyan-500). Acceptable as secondary/ambient (≤10% coverage) but never as primary palette color. These are statistically the most common AI-default colors (Tailwind `bg-indigo-500` training bias).
38. **60-30-10 color distribution**: 60% dominant color (background), 30% secondary (text, surfaces, cards), 10% accent (CTA, key metrics, highlights). Maximum 4 distinct colors in entire presentation palette. See Principle 12 expansion in design-principles.md.
39. **WCAG contrast ratios**: Body text (<18pt) requires minimum 4.5:1 contrast ratio against background (WCAG AA). Large text (≥18pt or 14pt bold) requires minimum 3:1. UI elements (borders, icons) require 3:1. Do not round — 4.47:1 FAILS. Verify in QA-4 visual review.
40. **Colorblind-safe data encoding**: Prohibited pairs for data visualization: red+green, green+brown, blue+purple, green+black. Recommended alternative for binary pairs: blue+orange. Never use color as the ONLY differentiator — always add shape, pattern, or label.
41. **Chart-specific rules**: Bar charts: Y-axis MUST start at zero. Line charts: may truncate Y-axis. Pie/donut: max 5-6 segments (rest → "Other"), largest at 12 o'clock clockwise descending, donut preferred over pie. All charts: max 5-6 series/lines, no legends (label directly on data), chart title = insight not description ("Revenue grew 23%" not "Revenue chart"). 3D effects and dual Y-axes FORBIDDEN. See Principle 8 expansion.
42. **Statistics source citations**: Every statistic from external sources needs footnote or inline citation: `(source: McKinsey, 2024)`. Unsourced large numbers are a hallucination tell.
43. **Whitespace minimum**: Minimum 30% of slide area must be whitespace (empty space without text, icons, or cards). Padding from edges minimum 44px. Gap between elements minimum 16px. Maximum 2 large/dominant elements per slide.
44. **Image style consistency**: All photos in a presentation must share unified visual style — same color temperature, contrast level, and compositional approach. Do not mix photos and illustrations. If images vary, apply CSS filter to harmonize (e.g., `filter: saturate(0.8) contrast(1.1)` on all images).
```

- [ ] **Step 2: Commit**

```bash
cd C:/Users/progr/Workspace/kama-skills && git add slidev/.claude/skills/slidev/SKILL.md && git commit -m "feat(slidev): add color, data viz, and layout quality rules 37-44

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 3: SKILL.md — QA Updates (QA-0a, QA-0b Rule 18, QA-0c, QA-4)

**Files:**
- Modify: `.claude/skills/slidev/SKILL.md:767` (QA-0a)
- Modify: `.claude/skills/slidev/SKILL.md:786` (QA-0b Rule 18)
- Modify: `.claude/skills/slidev/SKILL.md:791` (after QA-0b, insert QA-0c)
- Modify: `.claude/skills/slidev/SKILL.md:825` (QA-4 Color & Palette)

- [ ] **Step 1: Update QA-0a — narrow centered check**

In QA-0a (line 767), find the bullet about centered layouts. It currently says to confirm `text-align: center` on `h1`, `p`, and other text elements. Change to:

Replace the centered layouts bullet text to say: confirm `text-align: center` is set on `h1`, `h2` and single-line elements (subtitle, date, attribution). Confirm multi-line `p` and `li` (>60 chars or >1 line) use `text-align: left` with `max-width: 600px; margin: 0 auto` — left-aligned in centered container. If multi-line body text is centered, fix immediately.

- [ ] **Step 2: Update QA-0b Rule 18 — new font threshold**

At line 786, find the Rule 18 check that mentions `text-xs`. Update to reference the new 1.25rem minimum:

Change from: `Search for text-xs usage. If used for body content (not footnotes), replace with text-sm.`
To: `Check all font sizes. Body text below 1.25rem (20px) = CRITICAL — raise to minimum. Headings below 2.2rem = CRITICAL. Use text-xs (12px) ONLY for footnotes/source attributions. If raising font size causes overflow, the slide has too much content — split it.`

- [ ] **Step 3: Insert QA-0c Anti-Pattern Scan after QA-0b**

After line 791 ("Fix any issues found before proceeding to visual review."), insert the entire QA-0c section:

```markdown
**QA-0c: Anti-Pattern Scan** — Before rendering, scan slides.md for these specific anti-patterns. This phase catches problems that QA-0a (CSS) and QA-0b (design principles) miss — pattern-specific bad practices identified by industry research.

**Scope note:** Some items overlap with QA-0a/QA-0b — this is intentional redundancy for defense-in-depth.

**Content density:**
- [ ] Words per content slide ≤40 (WARNING >40, CRITICAL >75; exception: table/comparison slides ≤60)
- [ ] Bullets per slide ≤4 (reinforces Rule 21)
- [ ] Words per bullet ≤12
- [ ] Text lines per slide ≤6

**Typography:**
- [ ] Body text ≥1.25rem (CRITICAL if smaller) (redundant with QA-0b)
- [ ] Headings ≥2.2rem (CRITICAL if smaller)
- [ ] Line-height 1.3–1.45 for body text
- [ ] Bold usage ≤15% of total text
- [ ] No centered multi-line body text (CRITICAL) (redundant with QA-0a)

**Color:**
- [ ] Primary accent not in AI blacklist (hue 240-290, sat >50%) = WARNING
- [ ] Body text contrast ≥4.5:1 against background (CRITICAL)
- [ ] No colorblind-unsafe data pairs (red+green, green+brown, blue+purple)

**AI tells:**
- [ ] No generic slide titles from blacklist: "Обзор", "Ключевые выводы", "О нас", "Наше решение", "Введение", "Итоги", "Резюме" (CRITICAL)
- [ ] `icon-trio` archetype used ≤1 time per deck
- [ ] All-caps eyebrow labels on ≤30% of slides
- [ ] Last slide is NOT "Спасибо" / "Thank You" / "Вопросы?" (CRITICAL)
- [ ] Action title by slide 2-3 surfaces main conclusion (business decks)

**Data viz:**
- [ ] Bar chart Y-axis starts at zero (CRITICAL if not)
- [ ] Charts have ≤5-6 series/slices
- [ ] Statistics have source citations (WARNING if missing)

**Structure:**
- [ ] Sub-bullet nesting ≤2 levels (CRITICAL if deeper)
- [ ] Ghost Deck test: read slide titles in sequence — must tell coherent story (manual check)

Fix all CRITICAL items before proceeding to visual review. Log WARNINGs for reviewer attention.
```

- [ ] **Step 4: Update QA-4 Color & Palette checklist**

At line 825 (Color & Palette section), after the existing 4 checklist items, add:

```markdown
- [ ] **CRITICAL — WCAG contrast**: Body text contrast ≥4.5:1 against background. Large text ≥3:1. Verify — do not estimate.
- [ ] **CRITICAL — Background variation (dark themes)**: Compare this slide's background to previous slide. Are they visually distinguishable? Section dividers MUST be noticeably different.
- [ ] **Colorblind safety**: No data visualization uses red+green as only differentiator
- [ ] **Whitespace**: Slide has ≥30% empty space, padding ≥44px from edges, gaps ≥16px between elements
```

- [ ] **Step 5: Update QA-0b — add colorblind check**

In QA-0b (around line 773), after the Principle 8 data viz check, add:
```markdown
- **Colorblind safety (Principle 8 expansion)**: Check that no data visualization uses red+green, green+brown, blue+purple, or green+black as the only differentiator. Recommend blue+orange for binary pairs.
```

- [ ] **Step 6: Commit**

```bash
cd C:/Users/progr/Workspace/kama-skills && git add slidev/.claude/skills/slidev/SKILL.md && git commit -m "feat(slidev): add QA-0c anti-pattern scan and update QA-0a/0b/4

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 4: SKILL.md — Generation & Edit Updates (Step 4.5, Step 5, --edit, critics, gaps 6, 10, 11, 12, 17, 5-partial)

**Files:**
- Modify: `.claude/skills/slidev/SKILL.md:1202-1207` (Step 4.5 entropy rules)
- Modify: `.claude/skills/slidev/SKILL.md:1228` (Step 5 layout choice)
- Modify: `.claude/skills/slidev/SKILL.md:224-241` (--edit steps 4 and 5)
- Modify: `.claude/skills/slidev/SKILL.md:367` (L-3c critic)
- Modify: `.claude/skills/slidev/SKILL.md:659` (PDL-2.3 critic)
- Modify: `.claude/skills/slidev/SKILL.md:280` (Picture P-3)

- [ ] **Step 1: Update Step 4.5 — add icon-trio limit, recommendation, Ghost Deck**

In Step 4.5 deck-level constraints (around line 1202), after existing constraints, add:

```markdown
   - `icon-trio` appears at most once per deck (same as `profile-grid`)
   - For business presentations (KP, pitch, report): main conclusion must be surfaced as action title by slide 2-3. If outline buries it after slide 5, formulate action titles that bring the conclusion forward.
   - **Ghost Deck test**: After creating the Composition Plan, read the planned action titles in sequence. They must tell a coherent argument. If the title sequence is a list of labels ("About", "Team", "Product"), rewrite as statements.
```

- [ ] **Step 2: Update Step 5 — add word count and action title awareness**

In Step 5 (after the layout choice section, around line 1238), add a new paragraph:

```markdown
   **Content quality checks during writing**: For each slide, verify: (a) word count ≤40 (≤60 for tables), (b) title is an action title (statement, not label), (c) body text uses `font-size ≥1.25rem`, (d) no more than 4 bullets with ≤12 words each, (e) multi-line body text is left-aligned even on centered layouts, (f) line-height 1.3-1.45 for body, (g) if slide contains a chart, apply chart-specific rules from Rule 41 — bar chart Y-axis starts at zero, chart title = insight, ≤5-6 series.
```

- [ ] **Step 3: Update --edit procedure — add research-driven checks**

In --edit step 4 (around line 224, frontend-design thinking), after the existing archetype/shape/font discipline bullets, add:

```markdown
   - **Word count**: After editing, recount words on modified slides. If >40 (>60 for tables) — warn and suggest splitting or moving content to speaker notes.
   - **Action titles**: If editing a slide title, ensure it's a statement/insight, not a label. Check against generic phrase blacklist.
   - **Source citations**: If adding a statistic, include source citation.
   - **Emphasis check**: Don't over-bold edited content — max 10-15% of text bold.
```

In --edit step 5 (around line 234, apply changes), after the existing archetype/composition bullets, add:

```markdown
   - When editing content: verify word count ≤40, font size ≥1.25rem for body, ≥2.2rem for headings
   - When changing images: verify visual style consistency with existing images (same color temperature, contrast)
   - When editing layout: verify whitespace ≥30%, padding ≥44px, gap ≥16px
```

- [ ] **Step 3b: Update --create-preset and Step 0.4 — AI color blacklist check**

In --create-preset Step 3 (synthesis), after the existing archetype synthesis instruction, add:
```markdown
   After determining the accent color, check it against the AI color blacklist (hue 240-290 at saturation >50%). If the accent falls in this range, regenerate with a different hue. Common safe alternatives: teal (#0D9488), amber (#D97706), emerald (#059669), rose (#E11D48).
```

In Step 0.4 (auto-preset), after the existing archetype type-mapping, add the same blacklist check:
```markdown
   Verify the generated accent color is not in the AI color blacklist (hue 240-290, sat >50%). If it is, shift hue to nearest safe alternative.
```

- [ ] **Step 4: Update L-3c critic prompt — add anti-pattern awareness**

In L-3c (around line 367), in the critic prompt after the existing scoring instructions, add:

```markdown
7. Check for anti-patterns from industry research:
   - Generic label titles instead of action titles (Ghost Deck test: do titles tell a story?)
   - Purple/indigo as primary palette (AI color blacklist)
   - Three-column icon grid repeated >1 time
   - All-caps eyebrow labels on every slide (max 30%)
   - "Thank You" ending instead of CTA
   - Recommendation buried after slide 5
   - Body text centered on multi-line content
   - Font sizes below 1.25rem for body, below 2.2rem for headings
   - >40 words on a content slide
   - Bold on >15% of text
   - Bar charts not starting at zero
   - Statistics without source citations
   - Sub-bullets deeper than 2 levels
```

- [ ] **Step 5: Update PDL-2.3 critic — same anti-pattern list**

In PDL-2.3 (around line 659), after the existing archetype/shape evaluation bullets, add the same anti-pattern checklist as in Step 4 above.

- [ ] **Step 6: Update Picture Procedure P-3 — image consistency**

In P-3 (around line 280), after acquiring images (both auto and user-provided modes), add:

```markdown
After acquiring all images, verify visual style consistency across the set. All images should share similar color temperature, contrast level, and compositional style. If images vary significantly, apply a CSS harmonization filter on all image elements: `filter: saturate(0.85) contrast(1.05)` to unify the look. Do not mix photographic images with illustrations or AI-generated imagery.
```

- [ ] **Step 7: Commit**

```bash
cd C:/Users/progr/Workspace/kama-skills && git add slidev/.claude/skills/slidev/SKILL.md && git commit -m "feat(slidev): update generation, edit, and critic with research-driven checks

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 5: design-principles.md — Principle 8, 12, Anti-Patterns Reference

**Files:**
- Modify: `.claude/skills/slidev/references/design-principles.md:468-510` (Principle 8)
- Modify: `.claude/skills/slidev/references/design-principles.md:611-633` (Principle 12)
- Modify: `.claude/skills/slidev/references/design-principles.md:652` (append Anti-Patterns)

- [ ] **Step 1: Expand Principle 8 with chart-specific rules**

After the existing Principle 8 content (around line 510, before the `---` divider), insert:

```markdown
**Chart-Specific Rules (from research):**

**Bar charts:**
- Y-axis MUST start at zero — bar length encodes value, truncated axis = visual lie
- Maximum 7-8 bars per chart
- Value labels mandatory on every bar
- Title = insight: "Revenue grew 23%" not "Revenue chart"

**Line charts:**
- Do NOT require zero baseline (acceptable to truncate for trend detail)
- Maximum 5 lines per chart
- Labels directly on lines — no separate legend

**Pie/Donut:**
- Maximum 5-6 segments, remainder → "Other"
- Largest segment at 12 o'clock, clockwise descending by size
- Donut preferred over pie (better readability, center can hold label)
- 3D effects FORBIDDEN

**General chart rules:**
- No legends — label data directly on the chart element
- Chart title = finding/insight, not chart type name
- Dual Y-axes FORBIDDEN (implies false correlation)
- Every statistic needs source citation: `(source: Name, Year)`

**Colorblind-safe data encoding:**
- Prohibited pairs: red+green, green+brown, blue+purple, green+black
- Recommended binary pair: blue+orange
- Never use color as ONLY differentiator — add shape, pattern, or text label
```

- [ ] **Step 2: Expand Principle 12 with 60-30-10 rule**

After the existing Principle 12 content (around line 633, before the `---` divider), insert:

```markdown
**60-30-10 Color Distribution Rule:**

- **60%** — dominant color (background). One color family across the deck.
- **30%** — secondary (text, card surfaces, borders).
- **10%** — accent (CTA buttons, key metrics, highlights, active states).
- **Maximum 4 distinct colors** in the entire presentation palette (dominant + secondary + accent + optional warm/cool variant).

**AI Color Blacklist:**
These colors are statistically the most common AI-default choices (Tailwind training bias). BANNED as primary/dominant accent:
- Hue range 240-290 (purple-indigo-violet) at saturation >50%
- Specific: `#6366F1`, `#8B5CF6`, `#A855F7`, `#06B6D4`
- Acceptable as secondary/ambient (≤10% coverage), never as primary.
```

- [ ] **Step 3: Append Anti-Patterns Quick Reference at end of file**

After line 652 (end of file), append:

```markdown

---

## Anti-Patterns Quick Reference

What makes a presentation look AI-generated — avoid ALL of these:

1. **Same layout on >30% of slides** — every slide must be structurally distinct from neighbors
2. **Purple/indigo/cyan as primary color** — AI-default from Tailwind training data
3. **Three-column icon grid repeated** — `icon-trio` max once per deck
4. **All-caps label on every slide** — max 30%, and labels must be specific not generic
5. **Generic titles** — "Overview", "Our Approach", "Key Takeaways" = AI tell. Use action titles.
6. **"Thank You" ending** — last slide must be CTA with specific action, not gratitude
7. **Recommendation at the end** — main conclusion by slide 2-3, not buried in final third
8. **Body text centered on multiple lines** — multi-line body MUST be left-aligned
9. **Font below 20px (1.25rem) for body** — audience can't read small text on projected slides
10. **>40 words on a content slide** — that's a document, not a slide
11. **>15% of text bold** — over-emphasis kills emphasis
12. **Bar charts not starting at zero** — truncated Y-axis is a visual lie
13. **Statistics without sources** — unsourced numbers signal hallucination
14. **Sub-bullets 3+ levels deep** — max 2 levels, then restructure

**The test:** Would a professional presentation designer approve this slide? Would a McKinsey partner present it? If not — fix it.
```

- [ ] **Step 4: Commit**

```bash
cd C:/Users/progr/Workspace/kama-skills && git add slidev/.claude/skills/slidev/references/design-principles.md && git commit -m "feat(slidev): expand Principles 8/12 and add Anti-Patterns Quick Reference

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 6: Other References (scoring, layout-css-patterns, archetypes)

**Files:**
- Modify: `.claude/skills/slidev/references/scoring-subroutine.md:13-23`
- Modify: `.claude/skills/slidev/references/layout-css-patterns.md:141-146`
- Modify: `.claude/skills/slidev/references/composition-archetypes.md` (multiple lines)

- [ ] **Step 1: Enhance scoring-subroutine.md axes**

In the 9-axes table (lines 13-23), update the evaluation descriptions for 6 axes:

For **Font discipline** row — change "What to evaluate" to: `Strictly 2 font identities, body ≥1.25rem, headings ≥2.2rem, line-height 1.3-1.45, bold ≤15%`

For **Visual impact** row — change "What to evaluate" to: `First impression, memorability, whitespace ≥30%, max 2 large elements per slide`

For **Color conviction** row — change "What to evaluate" to: `Bold intentional palette, WCAG 4.5:1 contrast, no AI-blacklisted primary colors, 60-30-10 distribution`

For **Content clarity** row — change "What to evaluate" to: `Main message in 3 seconds, ≤40 words/slide, action titles not labels, recommendation by slide 3`

For **Composition variety** row — change "What to evaluate" to: `Different archetype structures, icon-trio max 1, no >30% same layout`

For **Decorative quality** row — change "What to evaluate" to: `Visible decorative elements, chart titles as insights, source citations on statistics`

- [ ] **Step 2: Update layout-css-patterns.md — centered body fix**

In the Statement / Center Layout section (line 141), change:

From: `h1, h2, p { text-align: center; }`
To:
```css
h1, h2 { text-align: center; }
p, li { text-align: left; max-width: 600px; margin: 0 auto; }
```

Also update the critical rule text near line 7 to note that body text on centered layouts is now left-aligned within a centered container.

Add the same pattern to Cover (no bg) and Section (no bg) layouts — headings centered, p left-aligned.

- [ ] **Step 3: Update composition-archetypes.md — raise body font sizes**

Find all body-text font-size values below 1.25rem and raise them:

| Current | New |
|---------|-----|
| `font-size:0.82rem` | `font-size:1.25rem` |
| `font-size:0.85rem` | `font-size:1.25rem` |
| `font-size:0.88rem` | `font-size:1.25rem` |
| `font-size:0.9rem` | `font-size:1.25rem` |
| `font-size:0.92rem` | `font-size:1.25rem` |
| `font-size:0.95rem` | `font-size:1.25rem` |
| `font-size:1.0rem` | `font-size:1.25rem` |
| `font-size:1.05rem` | `font-size:1.25rem` |
| `font-size:1.1rem` | `font-size:1.25rem` |
| `font-size:1.15rem` | `font-size:1.25rem` |

**Exception**: Keep `font-size:0.85rem` for labels/captions (elements with `text-transform:uppercase` or label-pill class). Keep `font-size:0.7rem` for eyebrow labels. Only raise audience-readable body content.

For heading fonts already ≥2.2rem — no change needed. For headings below 2.2rem — raise to 2.2rem.

- [ ] **Step 4: Commit**

```bash
cd C:/Users/progr/Workspace/kama-skills && git add slidev/.claude/skills/slidev/references/scoring-subroutine.md slidev/.claude/skills/slidev/references/layout-css-patterns.md slidev/.claude/skills/slidev/references/composition-archetypes.md && git commit -m "feat(slidev): update scoring axes, layout patterns, and archetype font sizes

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

---

### Task 7: Final Verification

- [ ] **Step 1: Verify cross-cutting consistency**

Run these checks:

1. Grep SKILL.md for "1.25rem" — should appear in Rule 20, QA-0b, QA-0c, --edit, Step 5
2. Grep SKILL.md for "action title" — should appear in Rule 30, QA-0c, Step 4.5, --edit, L-3c/PDL-2.3
3. Grep SKILL.md for "40 words" — should appear in Rule 29, QA-0c, --edit, Step 5
4. Grep SKILL.md for "QA-0c" — should appear in Phase 1 section
5. Grep design-principles.md for "Anti-Patterns" — should find the new section
6. Grep scoring-subroutine.md for "1.25rem" — should appear in font discipline axis
7. Grep layout-css-patterns.md for "text-align: left" — should appear in centered layouts
8. Grep composition-archetypes.md for "0.82rem" or "0.85rem" — should return 0 hits for body content (only labels)
9. Verify Rule 9 no longer says center `p` and `li`
10. Verify all new rules 29-44 exist in Design Quality Rules section
11. Grep SKILL.md for "icon-trio" near Step 4.5 — should appear in entropy rules
12. Grep SKILL.md for "4.5:1" near QA-4 — should appear in Color & Palette checklist
13. Grep SKILL.md for "action title" near --edit — should appear in edit procedure
14. Grep SKILL.md for "anti-pattern" near L-3c or PDL-2.3 — should appear in critic prompts
15. Grep scoring-subroutine.md for "4.5:1" — should appear in Color conviction axis
16. Grep SKILL.md for "blacklist" near --create-preset — should appear in synthesis step

- [ ] **Step 2: Fix any issues found**

If any verification fails, apply targeted fix and commit:

```bash
cd C:/Users/progr/Workspace/kama-skills && git add -A slidev/.claude/skills/slidev/ && git commit -m "fix(slidev): integration fixes for research-driven improvements

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
```

- [ ] **Step 3: Summary**

Print:
```
Research-driven improvements complete:

  SKILL.md:
    - Rule 9: centered body → left-aligned (BREAKING)
    - Rule 18/20: font minimums raised to 1.25rem body / 2.2rem heading
    - Rules 29-44: 16 new quality rules (word count, action titles, AI blacklist, etc.)
    - QA-0c: new anti-pattern scan phase (22 checks)
    - QA-0a: narrowed centered text check
    - QA-4: WCAG contrast + colorblind safety
    - Step 4.5: icon-trio limit, recommendation placement, Ghost Deck test
    - --edit: word count, action titles, source citations awareness
    - L-3c/PDL-2.3: anti-pattern checklist for critics

  design-principles.md:
    - Principle 8: chart-specific rules (bar/line/pie/donut)
    - Principle 12: 60-30-10 rule + AI color blacklist
    - Anti-Patterns Quick Reference: 14 items

  scoring-subroutine.md:
    - 6 of 9 axes enhanced with new criteria

  layout-css-patterns.md:
    - Centered layouts: body text left-aligned in centered container

  composition-archetypes.md:
    - All body font sizes raised to ≥1.25rem
```
