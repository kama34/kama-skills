# Design: Research-Driven Presentation Quality Improvements

**Date:** 2026-03-21
**Status:** Approved
**Scope:** 20 gaps identified from deep research (beautiful/ugly/AI-detection guides)
**Approach:** Cross-cutting changes across generation, QA, edit, scoring, and critic

---

## Context

Three research documents were produced analyzing professional presentation design:
- `beautiful-presentations-guide.md` — Reynolds, Duarte, Tufte, McKinsey, Apple, TED, YC standards
- `ugly-presentations-anti-patterns.md` — 76 anti-patterns with severity ratings
- `ai-presentation-detection-guide.md` — 7 categories of AI tells, 50-point detection checklist

Gap analysis against current SKILL.md revealed 20 concrete, implementable improvements organized into 6 design sections.

**Key principle:** Every rule must be enforced across ALL parts of the skill — generation (Steps 1-6), QA (Phases 1-4), --edit procedure, scoring subroutine, and critic agents (--learn, --deep_learn). No rule lives in only one place.

---

## Section 1: Typography & Readability (gaps 1, 2, 3, 14, 16)

### 1.1 Font Size Minimums (gap #1) — BREAKING CHANGE

Replace Rule 20 completely. New thresholds for Slidev (980px canvas):

| Element | Minimum | Recommended | Current (broken) |
|---------|---------|-------------|------------------|
| Body text | `1.25rem` (20px) | `1.4rem` (22px) | `0.875rem` (14px) |
| Headings | `2.2rem` (35px) | `2.8rem` (45px) | `1.8rem` |
| Labels/captions | `0.85rem` (13.6px) | `0.95rem` (15px) | `0.7rem` |
| Hero numbers | `4rem` (64px) | `5rem+` (80px+) | `4rem` (floor matches existing Principle 3 "4-8em" range) |
| Footnotes (only exception) | `0.75rem` (12px) | — | — |

**Enforced in:** Generation (Step 5), QA-0b (update existing Rule 18 reference to use new 1.25rem minimum instead of old text-sm/14px), QA-0c (redundant check for completeness), --edit, scoring (font discipline axis), critic agents. Note: QA-0b Rule 18 must be explicitly updated to reference the new threshold — otherwise QA-0b enforces 14px while QA-0c enforces 20px.

### 1.2 Word Count Limits (gap #2)

New explicit rule with thresholds:

| Metric | Threshold | Action |
|--------|-----------|--------|
| Words per content slide | max 40 | Split into 2 slides or move to speaker notes |
| Words per slide | 75+ | CRITICAL — "wall of text". Rewrite immediately |
| Words per slide | 150+ | FORBIDDEN — this is a document, not a slide |
| Bullets per slide | max 4 | Already exists (Rule 21), preserved |
| Words per bullet | max 12 | New — bullet = fragment, not sentence |
| Text lines per slide | max 6 | More than 6 = cognitive overload |

**Exceptions:** Table/comparison slides: limit 60 words. Speaker notes: no limit. Cover/CTA: typically low anyway.

**Enforced in:** Generation (Step 5), QA-0b (pre-render word count scan), QA-0c (anti-pattern checklist), --edit (recount after modifications), critic agents.

### 1.3 Centered vs Left-Aligned Body (gap #3) — BREAKING CHANGE

Change Rule 9:
- **Headings** (h1, h2): `text-align: center` on centered layouts — **preserved**
- **Body text** (p, li, span with content >60 chars or >1 line): `text-align: left` even on centered layouts — **new rule**
- **Single-line text** (date, subtitle, attribution): `text-align: center` — **preserved**

Update layout-css-patterns.md: for cover/section/statement add `p { text-align: left; max-width: 600px; margin: 0 auto; }` — left-aligned text in centered container.

**Enforced in:** Generation (Step 5, per-slide styles), QA-0a (CSS correctness — MUST be updated: narrow centered check to h1/h2 only; p/li with multi-line content require left-align), QA-0c (anti-pattern scan, redundant), --edit, layout-css-patterns.md, archetype HTML skeletons.

### 1.4 Line-Height (gap #14)

New rule: body text `line-height: 1.3–1.45`. Headings: `1.05–1.15`. Current default preset uses 1.7 — too loose.

**Enforced in:** Generation (Step 4 styles), QA-0c, --edit.

### 1.5 Bold/Emphasis Limits (gap #16)

New rule: max 10-15% of text may be bold. Max 1 emphasis technique per element (bold OR color OR size, not all three).

**Enforced in:** Generation (Step 5), QA-0c, --edit, critic agents.

---

## Section 2: Color & Contrast (gaps 5, 7, 8, 15)

### 2.1 AI Color Blacklist (gap #5)

Explicit blacklist of AI-default colors as primary/dominant palette:

Banned as primary accent: `#6366F1` (indigo-500), `#8B5CF6` (violet-500), `#A855F7` (purple-500), `#06B6D4` (cyan-500), and any hue 240-290 at saturation >50%.

Acceptable: as secondary/ambient accent (≤10% coverage), but not as primary.

**Enforced in:** Generation (Step 1 design params, Step 4 CSS vars), QA-0c, --create-preset (in Step 3 synthesis: after determining accent color, check against blacklist; if hue 240-290 at sat >50%, reject and regenerate), auto-preset (Step 0.4), --deep_learn critic, Design Quality Rules.

### 2.2 60-30-10 Color Distribution (gap #7)

New rule:
- **60%** — dominant color (background)
- **30%** — secondary (text, surfaces, cards)
- **10%** — accent (CTA, key metrics, highlights)
- **Max 4 colors** in entire presentation palette

Extend Principle 12 (Accent Hierarchy) in design-principles.md.

**Enforced in:** Generation (Step 1, Step 4), QA-4 (visual review), critic agents.

### 2.3 WCAG Contrast Ratios (gap #8)

Replace vague "sufficient contrast" with specific numbers:

| Element | Minimum contrast ratio |
|---------|----------------------|
| Body text (< 18pt) | 4.5:1 (WCAG AA) |
| Large text (≥ 18pt / 14pt bold) | 3:1 |
| UI elements (borders, icons) | 3:1 |

**Enforced in:** QA-0c (anti-pattern scan), QA-4 (visual review checklist), --edit, scoring subroutine.

### 2.4 Colorblind Safety (gap #15)

Prohibited pairs for data encoding:
- Red + Green
- Green + Brown
- Blue + Purple
- Green + Black

Recommended alternative: **Blue + Orange** for binary pairs.

**Enforced in:** Generation (Principle 8 data viz), QA-0b (design principles compliance), QA-0c, --edit.

---

## Section 3: Content Structure & Anti-AI (gaps 4, 6, 10, 11, 12, 17)

### 3.1 Action Titles (gap #4)

Every slide title must be a statement, not a label.

| Bad (label) | Good (action title) |
|-------------|---------------------|
| "Финансовые показатели" | "Выручка выросла на 23% за квартал" |
| "О компании" | "18 лет опыта в жилищном строительстве МО" |
| "Команда" | "Команда закрывает все ключевые компетенции" |
| "Рынок" | "Рынок подготовки к ЕГЭ — 85 млрд ₽ ежегодно" |

**Ghost Deck test:** reading only slide titles in sequence must tell a coherent story/argument. Add as a check in Step 4.5 (after Composition Plan — verify title sequence).

**Exception:** Cover slide and CTA — may use short titles.

**Enforced in:** Generation (Step 4.5, Step 5), QA-0c (title scan), --edit (title modification check), critic agents, scoring (content clarity axis).

### 3.2 Three-Column Icon Grid Limit (gap #6)

Archetype `icon-trio` may appear **max 1 time** per deck. Second appearance = AI tell.

Add to Step 4.5 entropy rules alongside existing `profile-grid` limit.

**Enforced in:** Step 4.5, QA-0c, critic agents.

### 3.3 Recommendation by Slide 3 (gap #10)

For business presentations (KP, pitch, report): main conclusion/recommendation must appear as title or hero element by slide 2-3.

Add to Step 4.5: "Classify the outline's main conclusion. It must appear by slide 2-3. If buried after slide 5 — formulate action titles that surface the conclusion early."

**Hard constraint:** Does not reorder outline slides. Uses action titles to surface the conclusion.

**Enforced in:** Step 4.5, QA-0c (recommendation placement check), critic agents, scoring (content clarity axis).

### 3.4 Generic Phrase Prohibition (gap #11)

Blacklisted slide titles: "Ключевые выводы", "Обзор", "В заключение", "Наше решение", "Наш подход", "О нас", "Введение", "Итоги", "Резюме", "Key Takeaways", "Overview", "In Conclusion", "Our Approach", "Summary"

**Test:** "Could any competitor send this presentation without changing more than the logo?"

**Enforced in:** Generation (Step 5), QA-0c (title scan), --edit, critic agents.

### 3.5 All-Caps Eyebrow Labels Limit (gap #12)

All-caps eyebrow labels allowed on **max 30% of slides**. Others use normal-case with accent color, or no label at all.

Labels must be specific: "Q1 2025" not "ОБЗОР". "МОСКВА · 120 ТОЧЕК" not "КОНТЕКСТ".

**Enforced in:** Generation (Step 5), QA-0c (label count), --edit, critic agents.

### 3.6 "Thank You" Ending Prohibition (gap #17)

Last slide NEVER ends with "Спасибо" / "Thank You" / "Вопросы?". Last slide = specific CTA with action and contact.

**Enforced in:** Generation (cta-warm archetype), QA-0c (last slide scan), --edit, Design Quality Rules.

---

## Section 4: Data Viz & Charts (gaps 13, 18)

### 4.1 Chart-Specific Rules (gap #13)

Expand Principle 8 with per-chart-type rules:

**Bar charts:**
- Y-axis MUST start at zero — bar length encodes value, truncated axis = lie
- Max 7-8 bars per chart
- Value labels mandatory on every bar

**Line charts:**
- Do NOT require zero baseline (acceptable to truncate for trend detail)
- Max 5 lines per chart
- Labels directly on lines, not separate legend

**Pie/Donut:**
- Max 5-6 segments, rest → "Other"
- Largest segment starts at 12 o'clock, clockwise descending
- Donut preferred over pie (better readability)
- 3D effects FORBIDDEN

**General:**
- No legends — label data directly
- Chart title = insight, not description ("Revenue grew 23%" not "Revenue chart")
- Dual Y-axes FORBIDDEN

**Enforced in:** Generation (Step 5), Principle 8 in design-principles.md, QA-0c, --edit, critic agents.

### 4.2 Statistics Source Citations (gap #18)

Every statistic from external source needs footnote or inline citation: `(source: McKinsey, 2024)`.

**Enforced in:** Generation (Step 5), QA-0c (scan for large numbers without source), --edit (remind when adding statistics).

---

## Section 5: Layout & Visual Consistency (gaps 9, 19, 20)

### 5.1 Whitespace Minimum (gap #9)

Min 30% of slide area = whitespace. Padding from edges min 44px, gap between elements min 16px, max 2 large elements per slide.

**Enforced in:** Generation (Step 5, archetype skeletons), QA-4 (visual review), --edit, scoring (content clarity axis).

### 5.2 Image Style Consistency (gap #19)

For `--picture`: all photos must have unified visual style — same color temperature, contrast, style (all photos or all illustrations, not mixed).

Add to Picture Procedure (P-3): after acquiring images, verify consistency. Apply CSS filter to harmonize if needed.

**Enforced in:** Picture Placement Procedure (P-3, P-6), QA-4, --edit --picture.

### 5.3 Sub-Bullet Depth Limit (gap #20)

Max 2 levels of bullet nesting. Sub-sub-bullets forbidden. If hierarchy deeper than 2 needed — restructure as cards or separate blocks.

**Enforced in:** Generation (Step 5), QA-0c, --edit.

---

## Section 6: Cross-Cutting — QA Anti-Prompts & Integration

### 6.1 QA-0c: Anti-Pattern Scan (NEW PHASE)

Add new sub-phase to Visual QA Phase 1, after QA-0b. A systematic anti-pattern checklist run BEFORE rendering.

**Scope note:** QA-0c covers pattern-specific anti-pattern scanning. Some items overlap with QA-0a/QA-0b checks — this is intentional redundancy for defense-in-depth. Do not remove items from QA-0a or QA-0b when adding QA-0c. Overlapping items are marked (redundant).

**Content density:**
- [ ] Words per content slide ≤40 (WARNING >40, CRITICAL >75; exception: table/comparison slides ≤60)
- [ ] Bullets per slide ≤4
- [ ] Words per bullet ≤12
- [ ] Text lines ≤6

**Typography:**
- [ ] Body text ≥1.25rem (CRITICAL if smaller) (redundant with QA-0b Rule 18 update)
- [ ] Headings ≥2.2rem (CRITICAL if smaller)
- [ ] Line-height 1.3–1.45 for body
- [ ] Bold ≤15% of text
- [ ] No centered multi-line body text (CRITICAL) (redundant with QA-0a update)

**Color:**
- [ ] Primary accent not in AI blacklist (hue 240-290, sat >50%)
- [ ] Body text contrast ≥4.5:1 (CRITICAL)
- [ ] No colorblind-unsafe data pairs (red+green)

**AI tells:**
- [ ] No generic slide titles from blacklist (CRITICAL)
- [ ] icon-trio archetype ≤1 per deck
- [ ] All-caps eyebrow labels ≤30% of slides
- [ ] Last slide is not "Thank You" (CRITICAL)
- [ ] Action title by slide 2-3 surfaces main conclusion (business decks)

**Data viz:**
- [ ] Bar chart Y-axis starts at zero (CRITICAL)
- [ ] Charts ≤5-6 series/slices
- [ ] Statistics have source citations

**Structure:**
- [ ] Sub-bullet nesting ≤2 levels (CRITICAL)
- [ ] Ghost Deck test: title sequence tells a story

### 6.2 Scoring Subroutine Enhancement

Add checks to existing 9 axes:

- **Composition variety**: icon-trio max 1, no >30% same layout
- **Shape diversity**: (no new checks — existing checks sufficient)
- **Font discipline**: body ≥1.25rem, headings ≥2.2rem, line-height 1.3-1.45, bold ≤15%
- **Visual impact**: whitespace ≥30%, max 2 large elements per slide
- **Layout uniqueness**: (no new checks — existing checks sufficient)
- **Typography drama**: (no new checks — existing checks sufficient, reinforced by font minimums)
- **Color conviction**: WCAG 4.5:1 contrast, no AI-blacklisted primary colors, 60-30-10 distribution
- **Content clarity**: ≤40 words/slide, action titles not labels, recommendation by slide 3, no generic phrases
- **Decorative quality**: chart titles as insights, source citations on statistics

### 6.3 --edit Integration

Add to --edit procedure:
- Word count awareness: recount after edits, warn if >40
- Action title check: new/modified titles must be statements
- Source citations: remind when adding statistics
- Font size check: new text ≥1.25rem body, ≥2.2rem heading
- Centered body check: new multi-line body must be left-aligned
- Emphasis limit: don't over-bold edited content

### 6.4 Critic Agent Updates (--learn, --deep_learn)

Add to L-3c and PDL-2.3 critic prompts:

"When critiquing, actively check for these AI tells and anti-patterns:
- Generic label titles instead of action titles
- Purple/indigo as primary palette
- Three-column icon grid repeated >1 time
- All-caps eyebrow labels on every slide
- 'Thank You' ending
- Recommendation buried after slide 5
- Body text centered on multi-line content
- Font sizes below 1.25rem for body
- >40 words on a content slide
- Bold on >15% of text
- Bar charts not starting at zero
- Statistics without source citations"

### 6.5 Design Principles Anti-Patterns Reference

Add to `references/design-principles.md` new section:

```markdown
## Anti-Patterns Quick Reference

What makes a presentation look AI-generated (avoid ALL):
1. Same layout on >30% of slides
2. Purple/indigo/cyan as primary color
3. Three-column icon grid repeated
4. All-caps label on every slide
5. Generic titles ("Overview", "Our Approach")
6. "Thank You" ending
7. Recommendation at the end, not beginning
8. Body text centered on multiple lines
9. Font below 20px for body content
10. >40 words on a content slide
```

---

## Files Modified

| File | Changes |
|------|---------|
| `SKILL.md` | Rule 9 (centered body fix), Rule 18 in QA-0b (update font threshold to 1.25rem), Rule 20 (font sizes), new rules 29-40 (word count, action titles, generic phrases, emphasis limits, chart rules, sub-bullets, whitespace, etc.), QA-0a (narrow centered check to h1/h2 only; p/li multi-line → left-align), QA-0c (new anti-pattern scan phase), Step 4.5 (icon-trio limit, recommendation placement, Ghost Deck test), Step 5 (action titles, word count, line-height), --edit procedure updates, QA-4 (WCAG contrast, background variation check), L-3c and PDL-2.3 critic prompt updates, --help examples |
| `references/design-principles.md` | Principle 8 expansion (chart-specific rules), Principle 12 expansion (60-30-10), new Anti-Patterns Quick Reference section, colorblind safety rules |
| `references/scoring-subroutine.md` | Enhanced checks within existing 9 axes (composition, font discipline, content clarity) |
| `references/layout-css-patterns.md` | Updated centered layout patterns (body left-align in centered containers) |
| `references/composition-archetypes.md` | Updated archetype skeletons: body text from `font-size:0.875rem`/`text-sm` → `font-size:1.25rem`/`text-base`; headings below 2.2rem raised; icon-trio deck-level constraint (max 1) added to mapping notes |

---

## Breaking Changes

1. **Font sizes**: body minimum raised from 14px to 20px. All existing archetype HTML skeletons need font size updates.
2. **Centered body text**: multi-line body text becomes left-aligned on centered layouts. Rule 9 modified. layout-css-patterns.md updated.
3. **Word count**: slides with >40 words will be flagged. Existing dense slides in generated presentations will need content reduction.

---

## Decision Log

| Decision | Rationale |
|----------|-----------|
| Body min 1.25rem (20px) not 24pt | Slidev 980px canvas ≠ projector. Proportional scaling. Confirmed by user feedback that current 14px is unreadable. |
| Breaking change on centered body | Research unanimously says centered body text >2 lines = readability failure. User approved breaking change. |
| AI color blacklist by hue range | Specific hex values alone are insufficient — AI tools vary exact shades. Hue 240-290 at sat >50% catches the entire purple-indigo spectrum. |
| Word count 40 not 30 | YC says 30-40. Using 40 as threshold gives slightly more room for technical presentations while still preventing wall-of-text. |
| Action titles as rule not suggestion | Ghost Deck test is the strongest single differentiator between professional and AI presentations (McKinsey's #1 commandment). Must be a rule. |
| QA-0c as separate phase | Anti-pattern scan is distinct from CSS correctness (QA-0a) and design principles compliance (QA-0b). It checks for specific bad patterns, not good pattern compliance. |
| Cross-cutting enforcement | User explicitly requested that every rule touches generation + QA + edit + scoring + critic. No rule lives in one place. |
