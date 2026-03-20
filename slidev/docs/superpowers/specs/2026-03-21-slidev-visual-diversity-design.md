# Design: Slidev Visual Diversity Improvement

**Date:** 2026-03-21
**Status:** Approved
**Approach:** C — Content-Aware Selection
**Scope:** All 5 phases (point fixes + archetype library + content-aware selection + preset format extension + validation)

---

## Context

Feedback from [S26] group on a generated KP presentation revealed systematic visual monotony issues:

1. **Font number rendering** — Syne renders digits unevenly
2. **Too many fonts** — should be strictly 2, not 3+ visual voices
3. **Repetitive rectangular blocks** — identical card grids, no shape variety
4. **AI-looking icons** — generic Lucide-stroke SVGs
5. **Sharp color transition** — CTA slide too jarring
6. **Content overload** — too dense for a commercial proposal

Reference from Anna (Behance @ness_shch): light, airy, real photos, diverse block shapes, single font, unique composition per slide.

Deep research confirmed: the root cause is **structural monotony** (same layout pattern repeated), not just stylistic sameness. The proven solution (Beautiful.ai) is content-aware composition selection with forced diversity.

---

## Phase 1: Point Fixes in SKILL.md

### 1.1 Font Number Blacklist

Add to SKILL.md a **font number blacklist**: fonts where digits render unevenly in Chromium headless export.

Blacklisted fonts: `Syne, Playfair Display, Bodoni Moda`

Rule: when a presentation is number-heavy (financial, metrics, data), never select a blacklisted font for headings. The generation procedure checks against this list during font selection.

### 1.2 Strict 2-Font Rule

New rule: **"Maximum 2 visual font identities in the entire presentation."**

- Heading font (sans) for: headings, numbers, labels, hero text
- Body font (serif) for: descriptions, bullets, supporting text
- Labels differ from headings only via `text-transform`, `letter-spacing`, `font-size` — same font-family
- Hero numbers use heading font, just larger. Not a separate visual style.
- Monospace fonts used exclusively in code blocks (`<code>`, `<pre>`) do not count as a visual font identity — they serve a functional role and are perceptually distinct from display/body text.

### 1.3 Icon Style Diversification

Add `iconStyle` field to preset format: `"outlined"` (current default), `"filled"`, `"duotone"`.

Expand Principle 4 in design-principles.md:
- If preset defines `iconStyle`, Icon.vue is generated accordingly
- For corporate/formal presets, recommend `filled` or `duotone` over outlined
- Icons must be thematically specific to the presentation topic (construction = cranes, helmets, blueprints; not abstract Lucide shapes)

### 1.4 Smoother CTA Color Transition

New rule in Visual Arc (Principle 7): **"CTA slide background must share at least one color channel with the preceding slide."**

- If deck is dark, CTA uses accent color as background but with base color overlay (30-40% opacity) — creating "warm dark" instead of "pure amber"
- Penultimate slide begins the color transition — slightly warmer background, brighter accent
- No full color inversion between adjacent slides

---

## Phase 2: Composition Archetype Library

Create `references/composition-archetypes.md` with 15 named archetypes.

### Archetype List

| # | Archetype | Structure | Density | When |
|---|-----------|-----------|---------|------|
| 1 | `cover-hero` | Centered title + subtitle + meta, decorative bg | low | First slide |
| 2 | `section-divider` | Big number/text centered, full-color bg | low | Between sections |
| 3 | `stat-hero` | Giant number (5em+) centered + supporting row | low | Key metric |
| 4 | `quote-pull` | Oversized quote text + attribution, no cards | low | Quotes, mission |
| 5 | `icon-trio` | 3 circle icon-containers + labels, horizontal | medium | Features, benefits |
| 6 | `bento-grid` | 1 large zone + 2-3 smaller zones of varying size | medium-high | Overview, multi-fact |
| 7 | `two-col-text` | Equal columns, text/lists | medium | Comparison, details |
| 8 | `asymmetric-split` | 40/60 — visual + text (or reverse) | medium | Visual + context |
| 9 | `timeline-horizontal` | Horizontal steps with markers | medium | Process, stages |
| 10 | `timeline-zigzag` | Vertical zigzag left-right | medium | Long process |
| 11 | `profile-grid` | Circle photo-containers + name/role | medium | Team |
| 12 | `data-spotlight` | Large chart/table + 1 callout annotation | high | Data, analytics |
| 13 | `comparison-table` | Rows + columns, check/x icons | high | Feature comparison |
| 14 | `card-mosaic` | 2x2 or irregular grid, cards of different sizes | medium-high | Portfolio, cases |
| 15 | `cta-warm` | Centered heading + numbered steps + contact, warm bg shift | low | Final CTA |

### Archetype Record Format

Each archetype in `references/composition-archetypes.md` contains:
- **Name** (kebab-case)
- **Group** — category for entropy rules: `hero`, `grid`, `split`, `timeline`, `table`, `cta`
- **Density** (low / medium / medium-high / high)
- **Content types** — which content types this archetype serves (used by the mapping)
- **Use when** — content type signal
- **Visual description** — what makes this archetype distinct
- **Shape elements** — which non-rectangular shapes it uses
- **HTML skeleton** — Slidev-ready HTML using `layout: none` with `{{SLOT}}` markers. Must respect Rule 19 (max 3 div nesting levels). All styling via inline styles for reliability (Rule 23).

#### Example: `stat-hero` archetype record

```markdown
### stat-hero
**Group:** hero
**Density:** low
**Content types:** metric
**Use when:** Slide has 1-2 key metrics to emphasize
**Visual:** Giant centered number + brief label. Supporting metrics in small pill-badge row below.
**Shape elements:** Number as typographic hero (no card wrapper), pill badges for supporting stats

HTML skeleton:
​```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:16px;">{{LABEL}}</span>
  <h1 style="font-size:5.5rem;font-weight:800;color:var(--color-accent);margin:0;line-height:1;font-family:var(--font-heading);">{{HERO_NUMBER}}</h1>
  <p style="font-size:1.1rem;color:var(--color-text);margin:8px 0 32px;font-family:var(--font-body);">{{SUPPORTING_CONTEXT}}</p>
  <div style="display:flex;gap:12px;">
    {{SUPPORTING_STATS_AS_PILL_BADGES}}
  </div>
</div>
​```
```

Slot markers use `{{SLOT_NAME}}` convention. LLM replaces each slot with content from the outline, styled according to the preset's shape vocabulary.

### Key Differentiators from Current Approach

1. **Shape variety**: `icon-trio` uses circle containers, `profile-grid` uses circular photo cutouts, `bento-grid` uses zones of different sizes
2. **Density labeling**: explicit low/medium/high for alternation rules
3. **HTML skeletons**: LLM fills content slots, doesn't invent layout from scratch

---

## Phase 3: Content-Aware Selection Logic

### 3.1 Content Type Classification

New step in generation: classify each outline slide into a content type.

| Content Type | Signals in Outline |
|---|---|
| `intro` | First slide, company/product name |
| `credentials` | Experience, company stats, certifications |
| `context` | Task description, project parameters |
| `vision` | Visualization, concept, design |
| `scope` | List of works, features, capabilities |
| `process` | Stages, timeline, steps |
| `team` | People, roles, team |
| `metric` | Key number, budget, KPI |
| `portfolio` | Cases, projects, examples |
| `trust` | Guarantees, certificates, quality control |
| `terms` | Conditions, legal, payment |
| `cta` | Call to action, contacts, next steps |

### 3.2 Content Type → Archetype Mapping

```
intro       → cover-hero
credentials → bento-grid | icon-trio | card-mosaic
context     → two-col-text | asymmetric-split
vision      → section-divider | asymmetric-split | quote-pull
scope       → bento-grid | icon-trio | two-col-text
process     → timeline-horizontal | timeline-zigzag
team        → profile-grid | card-mosaic
metric      → stat-hero | data-spotlight
portfolio   → card-mosaic | bento-grid
trust       → icon-trio | two-col-text | bento-grid
terms       → two-col-text | comparison-table
cta         → cta-warm
```

### 3.3 Archetype Selection Algorithm

For each slide (in outline order):

1. Classify content type
2. Get candidate archetypes from mapping
3. **Filter**: remove archetypes used in last 3 slides (entropy window = 4)
4. **Filter**: remove archetypes with same density as previous slide (if previous was high → select low/medium)
5. Select most suitable from remaining candidates
6. If empty after filtering → relax entropy window to 2 and retry
7. If still empty → ignore density filter AND entropy window. Select the candidate with the lowest recent-use count. This guarantees a result is always returned.

### 3.4 Deck-Level Entropy Rules

Validated after all archetypes are selected:

- Every 10-slide deck contains minimum: 1 low-density, 1 medium, 1 image-dominant/visual slide
- No more than 2 consecutive high-density archetypes
- Cover always first, CTA always last
- `profile-grid` appears at most once per deck
- At least 3 different archetype groups (hero/grid/split/timeline/table/cta) in any 10-slide deck

### 3.5 Integration Point in SKILL.md

New **Step 4.5: Composition Planning** — inserted between Step 4 (Write styles/index.css) and Step 5 (Write slides.md). This placement ensures the preset is already resolved (Step 0 → Step 1) and styles are written, so the composition planner has access to `preferred`/`avoid` from the preset's archetypes section.

Procedure:
1. Read outline
2. Read preset's `archetypes` section (if present) for `preferred`/`avoid`
3. Classify each slide's content type
4. Select archetype for each (applying entropy rules + preset preferences)
5. Validate deck-level constraints
6. Output **Composition Plan** — table: "Slide N → content type → archetype → density"

This plan is consumed by Step 5 (Write slides.md): instead of current "choose layout based on content type", LLM takes archetype from the plan and uses its HTML skeleton from `references/composition-archetypes.md`.

### 3.6 --add_archetype Subcommand

```
/slidev --add_archetype [name]
```

Procedure:
1. If `name` not provided — ask "Как назвать архетип? (kebab-case)"
2. Ask: **"Для какого типа контента этот архетип? Опишите ситуацию, когда существующие архетипы не подходят."**
3. Based on answer, LLM determines:
   - How many archetypes are actually needed (may be 1, may be 2-3)
   - Density level for each
   - Which content types it serves
   - Which shape elements it uses
4. Generate HTML skeleton
5. Append to `references/composition-archetypes.md` (both the archetype record AND its content-type associations in the mapping table at the top of that file)
6. Generate a test slide for visual verification

**Note:** The content type → archetype mapping lives in `references/composition-archetypes.md` (not SKILL.md) to avoid self-modification of the skill file. SKILL.md references the mapping by pointer: "See `references/composition-archetypes.md` for the current mapping."

---

## Phase 4: Preset Format Extension

### 4.1 New YAML Frontmatter Fields

```yaml
iconStyle: filled           # outlined | filled | duotone
densityProfile: balanced    # minimal | balanced | dense
maxFonts: 2                 # strict font identity count
```

- `iconStyle` — determines how Icon.vue is generated
- `densityProfile` — influences archetype selection: `minimal` prefers low-density, `dense` allows more high-density consecutive
- `maxFonts` — hard limit on visual font identities (default: 2)

### 4.2 New Section: Preferred Archetypes

In preset body, after aesthetic description, before CSS block:

````markdown
```archetypes
preferred: [bento-grid, asymmetric-split, icon-trio, stat-hero, profile-grid]
avoid: [timeline-zigzag, comparison-table]
cta_style: cta-warm
cover_style: cover-hero
```
````

- `preferred` — acts as a **tie-breaker** within the already-filtered candidate set from content-type mapping. Does NOT override the content-type → archetype mapping. If a preferred archetype is not in the candidate set for a given content type, it is ignored for that slide.
- `avoid` — archetypes removed from the candidate set **before** content-type filtering. Takes absolute priority.
- `cta_style` / `cover_style` — fixed archetypes for first and last slide

### 4.3 New Section: Shape Vocabulary

````markdown
```shapes
card_radius: 14px
icon_container: circle        # circle | rounded-square | hexagon | none
stat_display: typographic     # typographic | pill-badge | card-inset
label_style: pill             # pill | uppercase-text | accent-line
divider_style: diagonal       # diagonal | horizontal | gradient-fade | none
photo_mask: circle            # circle | rounded-rect | hexagon
```
````

### 4.4 Usage During Generation

1. **Step 0.5 (Composition Planning)**: reads `preferred` / `avoid` → influences archetype selection
2. **Step 4 (styles/index.css)**: reads `shapes` → generates CSS classes for circle-containers, pill-labels, etc.
3. **Step 5 (slides.md)**: each archetype uses preset's shape vocabulary when filling HTML skeleton
4. **Step 6 (Icon.vue)**: reads `iconStyle` → generates filled/outlined/duotone version

### 4.5 Backward Compatibility

All new sections are **optional**. Missing sections use defaults:
- `preferred: []`, `avoid: []`
- `icon_container: none` (current behavior)
- `stat_display: card-inset` (current behavior)
- `densityProfile: balanced`
- `maxFonts: 2`

Existing presets continue to work without changes.

### 4.6 Archetypes in --create-preset and --deep_learn

**--create-preset:**
- Add 8th question to wizard (inserted as question 7, between "Textures" and "Save location"): **"Какие типы слайдов чаще всего будут в презентациях с этим пресетом?"** (metrics, timelines, team, portfolio, comparisons...)
- Auto-populate `preferred` / `avoid` based on answer
- HTML skeletons are styled with preset's CSS during demo generation
- **Note:** PL-1 and PDL-1 wizard references must be updated from "7 questions" to "8 questions"

**--deep_learn:**
- Visual critic (PDL-2.3) evaluates archetype adequacy — is bento-grid right for this content? Are structures repeating?
- Critic can propose changes to preset's `archetypes` and `shapes` sections
- Auto-apply (PDL-2.4) is authorized to modify `archetypes` and `shapes` sections, not just CSS

**Auto-preset (Step 0.4):**
- When creating new preset from topic, `archetypes` and `shapes` sections are generated based on presentation type (KP → bento + stat-hero + profile-grid; pitch → stat-hero + icon-trio + timeline)
- Deep learn inline (N=3) tests and refines these sections alongside CSS

---

## Phase 5: Validation via --learn

### 5.1 What We Test

After implementing Phases 1-4, run `--learn=3` to verify:
1. Archetypes are selected correctly (content type → archetype mapping works)
2. Entropy rules are respected (no repeats in 4-slide window)
3. Density alternates (no 3 high-density in a row)
4. Shape vocabulary is applied (circle containers, pill badges — not only rectangles)
5. Fonts — strictly 2 visual identities
6. Numbers render correctly (no blacklisted fonts)
7. CTA transition is smooth

### 5.2 Extended Critic Axes

Scoring subroutine expands from 6 to 9 axes:

| Axis | What It Checks | Score 1-10 |
|------|---------------|------------|
| **Composition variety** (NEW) | How many different archetypes used? Any repeats? | |
| **Shape diversity** (NEW) | Non-rectangular elements present? Circles, pills, badges? | |
| **Font discipline** (NEW) | Strictly 2 font identities? Numbers in same font as text? | |
| Visual impact | (existing) | |
| Layout uniqueness | (existing — reinforced by composition variety) | |
| Typography drama | (existing) | |
| Color conviction | (existing) | |
| Content clarity | (existing) | |
| Decorative quality | (existing) | |

### 5.3 Target Scores

| Axis | Before (estimated) | Target After |
|------|-------------------|-------------|
| Composition variety | 3-4/10 | 7+/10 |
| Shape diversity | 2/10 | 7+/10 |
| Font discipline | 5/10 | 9+/10 |

### 5.4 Scoring Subroutine Update Cascade

When adding 3 new axes to `references/scoring-subroutine.md`:
- Update the critic prompt template in L-3c to reference 9 axes (not 6)
- `references/compare-procedure.md` and `references/polish-procedure.md` invoke the scoring subroutine by reference — they inherit the change automatically and do NOT need hardcoded axis count updates
- `references/ab-testing.md` may reference axis names — verify and update if needed

### 5.5 If --learn Reveals Issues

Critic generates improvements.md as usual. But now improvements can touch:
- `references/composition-archetypes.md` — adding/editing archetypes and mapping
- Entropy rules in SKILL.md (window size, density rules)
- Specific HTML skeletons of archetypes

---

## Files Modified

| File | Changes |
|------|---------|
| `SKILL.md` | Font blacklist, 2-font rule, Step 4.5 (Composition Planning), --add_archetype subcommand, updated generation procedure, CTA transition rule, wizard updated to 8 questions, PL-1/PDL-1 refs updated |
| `references/design-principles.md` | Updated Principle 4 (icon styles), updated Principle 7 (CTA transition), font discipline rules |
| `references/composition-archetypes.md` | NEW — 15 archetype definitions with HTML skeletons + content-type → archetype mapping table |
| `references/scoring-subroutine.md` | 3 new scoring axes (composition variety, shape diversity, font discipline) |
| `references/preset-format.md` | New fields (iconStyle, densityProfile, maxFonts), new sections (archetypes, shapes) |

---

## Decision Log

| Decision | Rationale |
|----------|-----------|
| Approach C (Content-Aware Selection) | Proven by Beautiful.ai, solves root cause (structural monotony) |
| 15 archetypes initial | Sufficient for 12-slide decks with choice. Expandable via --add_archetype |
| Entropy window = 4 | Prevents repeat within 4 slides while allowing reuse in long decks |
| All new preset fields optional | Backward compatibility with existing presets |
| Archetypes in deep_learn | Critic must evaluate and refine archetype choices, not just CSS |
| maxFonts default = 2 | Direct response to feedback: too many font voices |
| --add_archetype as wizard | LLM determines how many archetypes needed, not user |
