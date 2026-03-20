# Slidev Visual Diversity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Eliminate visual monotony in generated presentations by implementing content-aware composition selection with 15 named archetypes, font discipline, icon style control, and extended preset format.

**Architecture:** Add a Composition Planning step (Step 4.5) to the generation procedure that classifies outline slides by content type, selects composition archetypes from a library of 15, applies entropy rules, and outputs a plan consumed by Step 5. Extend the preset format with `archetypes`, `shapes`, and new YAML fields. Update scoring from 6 to 9 axes.

**Tech Stack:** Slidev skill files (Markdown), reference documents, preset format specification.

**Spec:** `docs/superpowers/specs/2026-03-21-slidev-visual-diversity-design.md`

---

## File Structure

| File | Action | Responsibility |
|------|--------|---------------|
| `.claude/skills/slidev/SKILL.md` | Modify | Font blacklist, 2-font rule, Step 4.5, --add_archetype, --help update, wizard 8 questions, PL-1/PDL-1 refs, Design Quality Rules, 6→9 axes refs |
| `.claude/skills/slidev/references/composition-archetypes.md` | Create | 15 archetype definitions with HTML skeletons + content-type mapping table |
| `.claude/skills/slidev/references/design-principles.md` | Modify | Principle 4 (icon styles), Principle 7 (CTA transition) |
| `.claude/skills/slidev/references/scoring-subroutine.md` | Modify | Expand 6→9 axes |
| `.claude/skills/slidev/references/ab-testing.md` | Modify | Update 6→9 axes reference |
| `.claude/skills/slidev/references/preset-format.md` | Modify | New YAML fields, archetypes/shapes sections, example |

---

### Task 1: Font discipline rules in SKILL.md

**Files:**
- Modify: `.claude/skills/slidev/SKILL.md:981-988` (Font Selection section)
- Modify: `.claude/skills/slidev/SKILL.md:1341-1367` (Design Quality Rules)

- [ ] **Step 1: Add font number blacklist to Font Selection section**

After line 988 (`Monospace: JetBrains Mono...`), insert:

```markdown
### Font Number Blacklist
- **CRITICAL — Number-heavy presentations** (financial, metrics, data): NEVER select these fonts for headings — their digits render unevenly in Chromium headless export: `Syne, Playfair Display, Bodoni Moda`
- Before selecting a heading font, check if the outline contains 3+ slides with prominent numbers (budgets, metrics, percentages). If yes, verify the chosen font is NOT on the blacklist.

### Strict 2-Font Rule
- **Maximum 2 visual font identities in the entire presentation.** Heading font (sans) for: headings, numbers, labels, hero text. Body font (serif) for: descriptions, bullets, supporting text.
- Labels differ from headings only via `text-transform`, `letter-spacing`, `font-size` — same font-family.
- Hero numbers use heading font, just larger. Not a separate visual style.
- Monospace fonts used exclusively in code blocks (`<code>`, `<pre>`) do not count as a visual font identity — they serve a functional role.
```

- [ ] **Step 2: Add font discipline to Design Quality Rules**

After line 1367 (rule 24 "Visible decoration"), insert new rule 25:

```markdown
25. **Font discipline**: Maximum 2 visual font identities per presentation (heading + body). Numbers, labels, and hero text use the heading font — never a third font. Check font number blacklist for number-heavy decks. See Font Number Blacklist in Mode: Unique.
```

- [ ] **Step 3: Commit Phase 1a**

```bash
git add .claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): add font blacklist and 2-font discipline rule"
```

---

### Task 2: Icon style and CTA transition in design-principles.md

**Files:**
- Modify: `.claude/skills/slidev/references/design-principles.md:104-244` (Principle 4)
- Modify: `.claude/skills/slidev/references/design-principles.md:372-431` (Principle 7)

- [ ] **Step 1: Expand Principle 4 with iconStyle support**

After the Icon.vue template code block (around line 240), before the `Usage in slides` line, insert:

```markdown
**Icon Style Selection**: The preset format supports an `iconStyle` field: `"outlined"` (default — stroke icons as above), `"filled"` (solid fill, no stroke), `"duotone"` (two-tone with fill + lighter overlay).

- If preset defines `iconStyle: filled`, generate Icon.vue with `fill="currentColor"` and `stroke="none"` instead of the stroke-based template above. Adjust SVG paths accordingly for filled rendering.
- If preset defines `iconStyle: duotone`, generate Icon.vue with primary shapes using `fill` at full opacity and secondary shapes using `fill` at 40% opacity.
- **Thematic specificity**: Icons must be thematically relevant to the presentation topic. A construction proposal needs building, crane, helmet, blueprint icons — not abstract geometric shapes. A tech startup needs rocket, chart, code, cloud icons. Generic Lucide-style icons signal "AI-generated."
```

- [ ] **Step 2: Add CTA color transition rule to Principle 7**

After the "Same-hue section-break → climax differentiation rule" section (around line 431), insert:

```markdown
**CTA slide color transition smoothness**: The CTA/closing slide background MUST share at least one color channel with the preceding slide. Rules:
- If the deck is dark, CTA may use accent color as background but with base color overlay (30-40% opacity) — creating "warm dark" instead of full color inversion.
- The penultimate slide MUST begin the color transition: slightly warmer background, brighter accent usage, ~5% luminance shift toward the CTA's target color.
- No full color inversion between adjacent slides. The audience should feel a gradual warm-up, not a jarring switch.
- Acceptable CTA backgrounds on a dark deck: `linear-gradient(145deg, accent 0%, darken(accent, 30%) 100%)` with `rgba(base, 0.30)` overlay. This reads as "warm and inviting" rather than "shocking change."
```

- [ ] **Step 3: Commit Phase 1b**

```bash
git add .claude/skills/slidev/references/design-principles.md
git commit -m "feat(slidev): add icon style selection and CTA transition rules"
```

---

### Task 3: Create composition-archetypes.md

**Files:**
- Create: `.claude/skills/slidev/references/composition-archetypes.md`

This is the largest single deliverable. The file contains: a content-type → archetype mapping table at the top, then 15 archetype records each with HTML skeleton.

- [ ] **Step 1: Write the mapping table and first 5 archetypes (hero/low-density group)**

Create `.claude/skills/slidev/references/composition-archetypes.md` with:

```markdown
# Composition Archetypes

Named slide composition patterns for content-aware layout selection. Each archetype defines a complete visual structure with HTML skeleton. Used by Step 4.5 (Composition Planning) during generation.

## Content Type → Archetype Mapping

| Content Type | Candidate Archetypes (in preference order) |
|---|---|
| `intro` | cover-hero |
| `credentials` | bento-grid, icon-trio, card-mosaic |
| `context` | two-col-text, asymmetric-split |
| `vision` | section-divider, asymmetric-split, quote-pull |
| `scope` | bento-grid, icon-trio, two-col-text |
| `process` | timeline-horizontal, timeline-zigzag |
| `team` | profile-grid, card-mosaic |
| `metric` | stat-hero, data-spotlight |
| `portfolio` | card-mosaic, bento-grid |
| `trust` | icon-trio, two-col-text, bento-grid |
| `terms` | two-col-text, comparison-table |
| `cta` | cta-warm |

## Archetypes

### cover-hero
**Group:** hero
**Density:** low
**Content types:** intro
**Use when:** First slide of the presentation — title, company, key metadata.
**Visual:** Full-bleed decorative background. Title centered and oversized. Subtitle in body font. Metadata (date, region) as small dots row.
**Shape elements:** Chip/pill badge for label, dot separators for metadata.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <div style="display:inline-flex;align-items:center;background:rgba(255,255,255,0.06);border:1.5px solid rgba(var(--accent-rgb),0.55);border-radius:20px;padding:6px 18px;margin-bottom:28px;">
    <span style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;">{{LABEL}}</span>
  </div>
  <h1 style="font-size:3.4rem;font-weight:800;color:var(--color-text);margin:0 0 12px;font-family:var(--font-heading);line-height:1.08;">{{TITLE}}</h1>
  <p style="font-size:1.15rem;color:var(--color-muted);margin:0 0 28px;font-family:var(--font-body);font-style:italic;">{{SUBTITLE}}</p>
  <div style="display:flex;align-items:center;gap:16px;color:var(--color-muted);font-size:0.88rem;">
    {{METADATA_DOTS_ROW}}
  </div>
</div>
```

### section-divider
**Group:** hero
**Density:** low
**Content types:** vision
**Use when:** Transition between major sections. One big idea or section title.
**Visual:** Centered large heading (3.5rem+). Lifted background with centered glow. Minimal content — just heading + optional subtitle.
**Shape elements:** None — pure typography.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:16px;">{{LABEL}}</span>
  <h1 style="font-size:3.5rem;font-weight:800;color:var(--color-text);margin:0 0 24px;font-family:var(--font-heading);line-height:1.1;">{{HEADING}}</h1>
  <p style="font-size:1.05rem;color:var(--color-muted);max-width:700px;line-height:1.6;font-family:var(--font-body);">{{DESCRIPTION}}</p>
</div>
```

### stat-hero
**Group:** hero
**Density:** low
**Content types:** metric
**Use when:** Slide has 1-2 key metrics to emphasize (budget, KPI, headline number).
**Visual:** Giant centered number (5em+). Brief label above. Supporting context below. Optional small stat pills at bottom.
**Shape elements:** Number as typographic hero (no card wrapper), pill badges for supporting stats.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:16px;">{{LABEL}}</span>
  <h1 style="font-size:5.5rem;font-weight:800;color:var(--color-accent);margin:0;line-height:1;font-family:var(--font-heading);">{{HERO_NUMBER}}</h1>
  <p style="font-size:1.1rem;color:var(--color-text);margin:8px 0 32px;font-family:var(--font-body);">{{SUPPORTING_CONTEXT}}</p>
  <div style="display:flex;gap:12px;">
    {{SUPPORTING_STATS_AS_PILLS}}
  </div>
</div>
```

### quote-pull
**Group:** hero
**Density:** low
**Content types:** vision
**Use when:** Slide centers on a key quote, mission statement, or visionary text.
**Visual:** Oversized quote text in serif/body font. Attribution below. No cards or blocks.
**Shape elements:** Decorative quotation marks as CSS pseudo-element.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 100px;">
  <p style="font-size:2rem;font-weight:400;color:var(--color-text);line-height:1.5;font-family:var(--font-body);font-style:italic;max-width:800px;">{{QUOTE_TEXT}}</p>
  <span style="display:block;margin-top:20px;font-size:0.85rem;color:var(--color-muted);font-family:var(--font-heading);text-transform:uppercase;letter-spacing:0.1em;">{{ATTRIBUTION}}</span>
</div>
```

### cta-warm
**Group:** cta
**Density:** low
**Content types:** cta
**Use when:** Final CTA slide — call to action, contact info, next steps.
**Visual:** Warm background (accent with base overlay). Centered heading. Numbered steps in semi-transparent pills. Contact info row at bottom.
**Shape elements:** Numbered pills for steps, dot separators for contact.

```html
<div style="position:absolute;inset:0;z-index:0;background:linear-gradient(145deg, var(--color-accent) 0%, color-mix(in srgb, var(--color-accent) 70%, black) 100%);"></div>
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:60px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-bg);font-weight:600;margin-bottom:16px;">{{LABEL}}</span>
  <h1 style="font-size:2.8rem;font-weight:800;color:var(--color-bg);margin:0 0 28px;font-family:var(--font-heading);line-height:1.15;">{{HEADING}}</h1>
  <div style="display:flex;flex-direction:column;gap:10px;max-width:600px;width:100%;margin-bottom:32px;">
    {{NUMBERED_STEPS_AS_PILLS}}
  </div>
  <div style="display:flex;align-items:center;gap:24px;color:var(--color-bg);font-size:0.9rem;">
    {{CONTACT_INFO_ROW}}
  </div>
</div>
```
```

- [ ] **Step 2: Add 5 medium-density archetypes (grid/split group)**

Append to the file:

```markdown
### icon-trio
**Group:** grid
**Density:** medium
**Content types:** credentials, scope, trust
**Use when:** 3-5 features, benefits, or capabilities to present with icons.
**Visual:** 3 circle icon containers in a horizontal row with labels below each. Clean, spaced.
**Shape elements:** Circle containers for icons (not rectangles), short text labels.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">{{LABEL}}</span>
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);">{{HEADING}}</h1>
  <div style="flex:1;display:flex;justify-content:center;align-items:center;gap:48px;">
    {{REPEAT_3_5:
    <div style="display:flex;flex-direction:column;align-items:center;text-align:center;max-width:200px;">
      <div style="width:72px;height:72px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;margin-bottom:16px;">
        <Icon name="{{ICON}}" :size="28" color="var(--color-accent)" />
      </div>
      <span style="font-size:1rem;font-weight:700;color:var(--color-text);margin-bottom:4px;">{{ITEM_TITLE}}</span>
      <span style="font-size:0.82rem;color:var(--color-muted);line-height:1.4;">{{ITEM_DESC}}</span>
    </div>
    }}
  </div>
</div>
```

### bento-grid
**Group:** grid
**Density:** medium-high
**Content types:** credentials, scope, portfolio, trust
**Use when:** 3-5 items of varying importance — one featured, others supporting.
**Visual:** One large zone (60% width) + 2-3 smaller zones stacked beside it. Different card sizes create visual interest.
**Shape elements:** Cards of different sizes (large featured + small supporting), accent card for the most important item.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">{{LABEL}}</span>
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">{{HEADING}}</h1>
  <div style="flex:1;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:1fr 1fr;gap:14px;">
    <div style="grid-row:1/3;background:linear-gradient(135deg,rgba(var(--accent-rgb),0.12),var(--color-surface));border:1.5px solid var(--color-accent-dim);border-radius:14px;padding:24px;display:flex;flex-direction:column;justify-content:center;">
      {{FEATURED_ITEM}}
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
      {{ITEM_2}}
    </div>
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:14px;padding:18px 22px;display:flex;align-items:center;gap:14px;">
      {{ITEM_3}}
    </div>
  </div>
</div>
```

### two-col-text
**Group:** split
**Density:** medium
**Content types:** context, scope, terms, trust
**Use when:** Content splits naturally into 2 groups or a before/after comparison.
**Visual:** Equal-width columns separated by a subtle vertical divider or gap. Heading spans full width.
**Shape elements:** Vertical divider line (optional), pill labels for column headers.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">{{LABEL}}</span>
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 20px;font-family:var(--font-heading);">{{HEADING}}</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:32px;align-content:center;">
    <div>
      {{LEFT_COLUMN_CONTENT}}
    </div>
    <div>
      {{RIGHT_COLUMN_CONTENT}}
    </div>
  </div>
</div>
```

### asymmetric-split
**Group:** split
**Density:** medium
**Content types:** context, vision
**Use when:** One visual element (icon, illustration, metric) paired with explanatory text.
**Visual:** 40/60 split — left side has a large visual element or hero metric, right side has text content.
**Shape elements:** Large circle or rounded container for the visual element on the narrow side.

```html
<div style="position:absolute;inset:0;z-index:1;display:grid;grid-template-columns:2fr 3fr;padding:44px 64px;gap:40px;align-items:center;">
  <div style="display:flex;justify-content:center;align-items:center;">
    {{VISUAL_ELEMENT}}
  </div>
  <div style="display:flex;flex-direction:column;justify-content:center;">
    <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">{{LABEL}}</span>
    <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">{{HEADING}}</h1>
    {{TEXT_CONTENT}}
  </div>
</div>
```

### card-mosaic
**Group:** grid
**Density:** medium-high
**Content types:** credentials, team, portfolio
**Use when:** 4 items of equal importance — portfolio pieces, team cards, project examples.
**Visual:** 2x2 grid of cards. One card uses accent styling for emphasis. Cards have different internal layouts (some with titles, some with icons).
**Shape elements:** Cards with varying borders (solid + accent highlight for one), rounded corners.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">{{LABEL}}</span>
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">{{HEADING}}</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;align-items:stretch;">
    {{CARD_1_SOLID}}
    {{CARD_2_SOLID}}
    {{CARD_3_SOLID}}
    {{CARD_4_ACCENT}}
  </div>
</div>
```
```

- [ ] **Step 3: Add 5 medium-density archetypes (timeline/people group)**

Append:

```markdown
### timeline-horizontal
**Group:** timeline
**Density:** medium
**Content types:** process
**Use when:** 4-6 sequential steps or stages.
**Visual:** 3×2 grid of stage cards with stage number/period labels. Footer with milestones.
**Shape elements:** Stage number labels in accent color, milestone dots at bottom.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">{{LABEL}}</span>
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">{{HEADING}}</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;align-items:stretch;">
    {{REPEAT_STAGES:
    <div style="background:var(--color-surface);border:1px solid var(--color-surface-border);border-radius:12px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;">
      <span style="display:block;font-size:0.65rem;color:var(--color-accent);font-weight:700;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:4px;">{{STAGE_LABEL}}</span>
      <span style="font-size:0.85rem;color:var(--color-text);line-height:1.35;">{{STAGE_CONTENT}}</span>
    </div>
    }}
  </div>
  <div style="display:flex;justify-content:center;gap:24px;margin-top:12px;padding:10px 0;border-top:1px solid var(--color-surface-border);">
    {{MILESTONES_ROW}}
  </div>
</div>
```

### timeline-zigzag
**Group:** timeline
**Density:** medium
**Content types:** process
**Use when:** Long process (6+ steps) that needs compact vertical presentation.
**Visual:** Alternating left-right entries along a vertical center line. Each entry has a number badge and description.
**Shape elements:** Circle number badges, vertical connector line (CSS pseudo-element).

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">{{LABEL}}</span>
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">{{HEADING}}</h1>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;">
    {{REPEAT_STEPS:
    <div style="display:flex;align-items:center;gap:16px;">
      <div style="width:36px;height:36px;border-radius:50%;background:var(--color-accent-bg);border:1.5px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <span style="font-size:0.8rem;font-weight:700;color:var(--color-accent);">{{STEP_NUM}}</span>
      </div>
      <span style="font-size:0.88rem;color:var(--color-text);line-height:1.35;">{{STEP_TEXT}}</span>
    </div>
    }}
  </div>
</div>
```

### profile-grid
**Group:** grid
**Density:** medium
**Content types:** team
**Use when:** Showing team members, advisors, or key personnel.
**Visual:** 2×3 grid of profile cards. Each has a circle container for photo/icon + name + role. Ghost card style.
**Shape elements:** Circle containers for profile icons/photos, ghost border cards.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">{{LABEL}}</span>
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">{{HEADING}}</h1>
  <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr 1fr;gap:10px;align-items:stretch;">
    {{REPEAT_MEMBERS:
    <div style="display:flex;align-items:center;gap:14px;background:transparent;border:1.5px solid var(--color-accent-dim);border-radius:12px;padding:0 20px;">
      <div style="width:40px;height:40px;border-radius:50%;background:var(--color-accent-bg);border:1px solid var(--color-accent-dim);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
        <Icon name="{{ICON}}" :size="20" color="var(--color-accent)" />
      </div>
      <span style="font-size:0.88rem;color:var(--color-text);line-height:1.35;">{{MEMBER_INFO}}</span>
    </div>
    }}
  </div>
</div>
```
```

- [ ] **Step 4: Add 2 high-density archetypes (table group)**

Append:

```markdown
### data-spotlight
**Group:** table
**Density:** high
**Content types:** metric, trust
**Use when:** Detailed breakdown — cost table, statistics grid, KPI dashboard.
**Visual:** 3×2 grid of metric cards. Top row has larger numbers, bottom row smaller. One row may use accent styling.
**Shape elements:** Centered numbers as typographic elements (no wrapping cards for the number itself), compact info cards.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:48px 80px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.18em;color:var(--color-accent);font-weight:600;margin-bottom:16px;">{{LABEL}}</span>
  <h1 style="font-size:2.2rem;font-weight:700;color:var(--color-text);margin:0 0 24px;font-family:var(--font-heading);">{{HEADING}}</h1>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;max-width:720px;width:100%;">
    {{METRIC_CARDS_AS_CENTERED_NUMBERS}}
  </div>
  <p style="font-size:0.95rem;color:var(--color-accent);margin-top:20px;font-weight:600;">{{BOTTOM_CALLOUT}}</p>
</div>
```

### comparison-table
**Group:** table
**Density:** high
**Content types:** terms, scope
**Use when:** Side-by-side comparison or structured list of conditions/features.
**Visual:** Vertical rows with icons. Ghost card style. Last row may have accent highlight.
**Shape elements:** Row-based layout with icons, ghost borders, optional accent on last row.

```html
<div style="position:absolute;inset:0;z-index:1;display:flex;flex-direction:column;padding:44px 64px;">
  <span style="display:block;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.15em;color:var(--color-accent);font-weight:600;margin-bottom:6px;">{{LABEL}}</span>
  <h1 style="font-size:2.1rem;font-weight:700;color:var(--color-text);margin:0 0 16px;font-family:var(--font-heading);">{{HEADING}}</h1>
  <div style="flex:1;display:grid;grid-template-rows:repeat({{N}},1fr);gap:8px;align-items:stretch;">
    {{REPEAT_ROWS:
    <div style="display:flex;align-items:center;gap:14px;background:transparent;border:1px solid var(--color-surface-border);border-radius:10px;padding:0 20px;">
      <Icon name="{{ICON}}" :size="20" color="var(--color-accent)" />
      <span style="font-size:0.88rem;color:var(--color-text);">{{ROW_CONTENT}}</span>
    </div>
    }}
  </div>
</div>
```
```

- [ ] **Step 5: Commit Phase 2**

```bash
git add .claude/skills/slidev/references/composition-archetypes.md
git commit -m "feat(slidev): add 15 composition archetypes with HTML skeletons"
```

---

### Task 4: Add Step 4.5 Composition Planning to SKILL.md

**Files:**
- Modify: `.claude/skills/slidev/SKILL.md:1119` (between Step 4 and Step 5)

- [ ] **Step 1: Insert Step 4.5 after Step 4 (styles/index.css)**

After line 1118 ("If preset mode with CSS block, write the preset's CSS verbatim..."), insert:

```markdown
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

5. **Output Composition Plan** as a table in the generation context:
   ```
   | Slide | Content Type | Archetype | Group | Density |
   |-------|-------------|-----------|-------|---------|
   | 1     | intro       | cover-hero | hero | low     |
   | 2     | credentials | bento-grid | grid | medium-high |
   ...
   ```

This plan is consumed by Step 5: for each slide, use the archetype's HTML skeleton from `references/composition-archetypes.md` and fill `{{SLOT}}` markers with content from the outline. Apply the preset's shape vocabulary when rendering elements.
```

- [ ] **Step 2: Update Step 5 to reference the Composition Plan**

In Step 5 (Write slides.md), replace the current layout selection logic (lines 1128-1136):

Replace:
```
1. **Choose layout** based on content type (reference `slidev-layouts.md`) AND **Design Principles**:
   - Title/intro → `cover`
   - Section break → `section`
   - Bullet points → `default`
   - Single statement → `statement` or `center`
   - Statistic → `fact`
   - Quote → `quote`
   - Comparison → `two-cols`
   - Closing → `end`
```

With:
```
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
```

- [ ] **Step 3: Commit Phase 3a**

```bash
git add .claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): add Step 4.5 Composition Planning with content-aware selection"
```

---

### Task 5: Add --add_archetype subcommand to SKILL.md

**Files:**
- Modify: `.claude/skills/slidev/SKILL.md:33-60` (--help output)
- Modify: `.claude/skills/slidev/SKILL.md:62-81` (Subcommands section, after --create-preset)

- [ ] **Step 1: Add --add_archetype to --help output**

In the --help block (around line 58), before the `--no-preset` line, insert:

```
  /slidev --add_archetype [name]              Add a new composition archetype
```

- [ ] **Step 2: Add --add_archetype subcommand handler**

After the `--create-preset` section (after line 81), insert:

```markdown
**`--add_archetype [name]`**: Add a new composition archetype to the library.

1. If `name` not provided — ask "Как назвать архетип? (kebab-case)"
2. Ask: **"Для какого типа контента этот архетип? Опишите ситуацию, когда существующие 15 архетипов не подходят."**
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
```

- [ ] **Step 3: Commit Phase 3b**

```bash
git add .claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): add --add_archetype subcommand"
```

---

### Task 6: Extend preset-format.md

**Files:**
- Modify: `.claude/skills/slidev/references/preset-format.md:9-110` (file structure example)
- Modify: `.claude/skills/slidev/references/preset-format.md:113-125` (frontmatter fields table)

- [ ] **Step 1: Add new YAML fields to frontmatter table**

In the frontmatter fields table (around line 125), add 3 new rows:

```markdown
| `iconStyle` | No | Icon rendering style: `outlined` (default), `filled`, `duotone` |
| `densityProfile` | No | Archetype density preference: `minimal`, `balanced` (default), `dense` |
| `maxFonts` | No | Max visual font identities. Default: `2` |
```

- [ ] **Step 2: Add archetypes and shapes sections to body description**

In the body section description, insert NEW items 2 and 3 BEFORE the existing CSS block description (which becomes item 4). The actual preset body order must be: aesthetic description → archetypes → shapes → CSS block.

```markdown
2. **Archetypes block** (optional fenced `archetypes` block): Configures composition archetype preferences for this preset.

   ```archetypes
   preferred: [bento-grid, asymmetric-split, icon-trio, stat-hero]
   avoid: [timeline-zigzag]
   cta_style: cta-warm
   cover_style: cover-hero
   ```

   - `preferred` — acts as a tie-breaker within the candidate set from content-type mapping. Does NOT override the mapping.
   - `avoid` — archetypes removed from candidate set before filtering. Takes absolute priority.
   - `cta_style` / `cover_style` — fixed archetypes for first and last slide.

3. **Shapes block** (optional fenced `shapes` block): Configures sub-slide visual element shapes.

   ```shapes
   card_radius: 14px
   icon_container: circle        # circle | rounded-square | hexagon | none
   stat_display: typographic     # typographic | pill-badge | card-inset
   label_style: pill             # pill | uppercase-text | accent-line
   divider_style: diagonal       # diagonal | horizontal | gradient-fade | none
   photo_mask: circle            # circle | rounded-rect | hexagon
   ```

   When generating slides, archetype HTML skeletons use these shape values to render elements. Defaults when absent: `icon_container: none`, `stat_display: card-inset`, `label_style: uppercase-text`, `divider_style: horizontal`, `photo_mask: rounded-rect`.

4. **CSS block** (REQUIRED fenced `css` block): Written verbatim to `styles/index.css`. Must include all existing required sections (see current preset-format.md). When `shapes` block is present, the CSS block should include corresponding utility classes.
```

- [ ] **Step 3: Commit Phase 4a**

```bash
git add .claude/skills/slidev/references/preset-format.md
git commit -m "feat(slidev): extend preset format with archetypes, shapes, and new fields"
```

---

### Task 6b: Add shapes→CSS generation to Step 4 in SKILL.md

**Files:**
- Modify: `.claude/skills/slidev/SKILL.md:1111-1118` (Step 4: Write styles/index.css)

- [ ] **Step 1: Add shapes CSS generation instruction**

In Step 4 (Write styles/index.css), after the existing bullet about card style variants (around line 1116), add:

```markdown
- **Shape vocabulary CSS** (if preset has `shapes` section): Generate CSS classes corresponding to the shape settings. For `icon_container: circle` → `.icon-container { width:56px; height:56px; border-radius:50%; background:var(--color-accent-bg); border:1.5px solid var(--color-accent-dim); display:flex; align-items:center; justify-content:center; }`. For `stat_display: typographic` → `.stat-hero { font-size:5rem; font-weight:800; color:var(--color-accent); line-height:1; }` (no card wrapper). For `label_style: pill` → `.label-pill { display:inline-flex; background:rgba(255,255,255,0.06); border:1.5px solid var(--color-accent-dim); border-radius:20px; padding:6px 18px; font-size:0.7rem; text-transform:uppercase; letter-spacing:0.15em; color:var(--color-accent); font-weight:600; }`. For `photo_mask: circle` → `.photo-circle { border-radius:50%; overflow:hidden; }`. These classes are used by archetype HTML skeletons.
```

- [ ] **Step 2: Commit**

```bash
git add .claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): add shapes→CSS generation in Step 4"
```

---

### Task 7: Update --create-preset wizard and PL-1/PDL-1

**Files:**
- Modify: `.claude/skills/slidev/SKILL.md:65` ("Ask 7 questions")
- Modify: `.claude/skills/slidev/SKILL.md:71-72` (between Textures and Transitions questions)
- Modify: `.claude/skills/slidev/SKILL.md:515` (PL-1 "7 questions")
- Modify: `.claude/skills/slidev/SKILL.md:605` (PDL-1 "7 questions")

- [ ] **Step 1: Add 8th question to wizard**

On line 65, change `Ask 7 questions` to `Ask 8 questions`. (Note: SKILL.md currently says "7 questions" with 7 design questions + Save location as a separate logistic step. After adding slide types, it becomes 8 design questions + Save location.)

Between the Textures question (line 71) and the Transitions question (line 72), insert:

```markdown
   - **Slide types**: "Какие типы слайдов чаще всего будут? (метрики/числа, таймлайны, команда, портфолио, сравнения, данные...)"
```

- [ ] **Step 2: Add archetypes/shapes generation to step 3 of wizard**

In the wizard's step 3 (line 74, "Synthesize answers..."), after the existing instructions, add:

```markdown
   Based on the "Slide types" answer, generate the `archetypes` section with `preferred`/`avoid` lists and the `shapes` section with appropriate defaults. For example, if the user said "метрики и команда", set `preferred: [stat-hero, profile-grid, bento-grid]` and `icon_container: circle`.
```

- [ ] **Step 3: Update PL-1 and PDL-1 references**

Change "7 questions" to "8 questions" at:
- Line 515 (PL-1: "run the interactive wizard (7 questions, same as `--create-preset`)")
- Line 605 (PDL-1: "run the interactive wizard (7 questions)")

- [ ] **Step 4: Commit Phase 4b**

```bash
git add .claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): update preset wizard to 8 questions with archetype preferences"
```

---

### Task 8: Update deep_learn for archetypes

**Files:**
- Modify: `.claude/skills/slidev/SKILL.md:630-640` (PDL-2.3 critic instructions)
- Modify: `.claude/skills/slidev/SKILL.md:650-660` (PDL-2.4 auto-apply scope)
- Modify: `.claude/skills/slidev/SKILL.md:888-895` (Step 0.4 auto-preset)

- [ ] **Step 1: Expand PDL-2.3 critic scope**

In the PDL-2.3 visual critic section, after the existing instructions about scoring and design-principles, add:

```markdown
- Evaluate composition archetype adequacy: was the right archetype selected for each content type? Are there slides where a different archetype would create better visual variety?
- Check archetype preferences: does the preset's `preferred` list match what actually works well? Should any archetypes be added to or removed from `preferred`/`avoid`?
- Evaluate shape vocabulary: are circle containers, pill badges, and other non-rectangular shapes being used effectively? Or does the presentation still look like "all rectangles"?
```

- [ ] **Step 2: Expand PDL-2.4 auto-apply scope**

In the PDL-2.4 auto-apply section, update the safety guardrails to include:

```markdown
- Changes to `.preset.md`: CSS + YAML frontmatter + `archetypes` section + `shapes` section
```

- [ ] **Step 3: Update Step 0.4 auto-preset**

In Step 0.4 (auto-preset creation when no match found), after "Generate an initial `.preset.md` based on the topic", add:

```markdown
   Include `archetypes` and `shapes` sections based on the presentation type:
   - Commercial proposal (КП) → `preferred: [bento-grid, stat-hero, profile-grid, card-mosaic]`, `icon_container: circle`, `stat_display: typographic`
   - Pitch deck → `preferred: [stat-hero, icon-trio, timeline-horizontal, asymmetric-split]`, `icon_container: circle`
   - Technical talk → `preferred: [two-col-text, data-spotlight, comparison-table, timeline-horizontal]`, `icon_container: rounded-square`
   - Educational lecture → `preferred: [icon-trio, timeline-zigzag, bento-grid, quote-pull]`, `icon_container: circle`
```

- [ ] **Step 4: Commit Phase 4c**

```bash
git add .claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): integrate archetypes into deep_learn and auto-preset"
```

---

### Task 9: Update scoring from 6 to 9 axes

**Files:**
- Modify: `.claude/skills/slidev/references/scoring-subroutine.md:11-21`
- Modify: `.claude/skills/slidev/references/scoring-subroutine.md:31`
- Modify: `.claude/skills/slidev/references/ab-testing.md:54`
- Modify: `.claude/skills/slidev/SKILL.md:20` (References section)
- Modify: `.claude/skills/slidev/SKILL.md:355` (L-3c critic prompt)
- Modify: `.claude/skills/slidev/SKILL.md:535` (PL-3 critic)

- [ ] **Step 1: Expand scoring-subroutine.md to 9 axes**

Replace the scoring table (lines 11-20) with:

```markdown
Read **EVERY** exported PNG from `<dir>/slides-qa/` with the Read tool. For each slide, evaluate and score 1-10 on these 9 axes:

| Axis | What to evaluate | Low (1-3) | Mid (4-6) | High (7-10) |
|---|---|---|---|---|
| **Composition variety** | Different archetype structures used, no repetition | Same layout every slide | Some variation, 2-3 patterns | Each slide structurally distinct |
| **Shape diversity** | Non-rectangular elements (circles, pills, badges) | All rectangles with same border-radius | Some shape variation | Rich mix of circles, pills, asymmetric splits |
| **Font discipline** | Strictly 2 font identities, numbers in heading font | 3+ fonts, numbers in different font | Mostly 2 but some inconsistency | Exactly 2 fonts, numbers consistent |
| **Visual impact** | First impression, memorability | Forgettable, generic | Decent but not striking | Would remember after seeing 20 others |
| **Layout uniqueness** | Structural difference from neighbors | Same layout as adjacent slides | Some variation | Clearly distinct composition |
| **Typography drama** | Scale contrast, hero numbers, weight pairing | Everything same size | Some hierarchy | Clear 3+ scale levels, hero elements pop |
| **Color conviction** | Bold intentional palette vs timid/generic | Washed out, no accent | Accent exists but mild | Bold, purposeful, memorable palette |
| **Content clarity** | Main message readable in 3 seconds | Cluttered, competing elements | Message findable but slow | Instant comprehension |
| **Decorative quality** | Visible decorative elements, personality | Flat background, no personality | Some decoration but subtle | Clearly visible motifs adding character |
```

- [ ] **Step 2: Update score report table header**

Replace the score report table (line 31) with:

```markdown
| Slide | Comp | Shape | Font | Impact | Layout | Typo | Color | Content | Decor | AVG |
|-------|------|-------|------|--------|--------|------|-------|---------|-------|-----|
```

- [ ] **Step 3: Update ab-testing.md**

Replace the entire line 54 with:
`Run the Scoring Subroutine evaluation (read the PNG, score on 9 axes) for each variant's exported PNG. This is a single-slide scoring — apply the same 9-axis evaluation from references/scoring-subroutine.md.`

- [ ] **Step 4: Update all SKILL.md references**

- Line 20: `Slide scoring (1-10 on 6 axes)` → `Slide scoring (1-10 on 9 axes)`
- Line 355 (L-3c critic): `score each slide on 6 axes (visual impact, layout uniqueness, typography drama, color conviction, content clarity, decorative quality)` → `score each slide on 9 axes (composition variety, shape diversity, font discipline, visual impact, layout uniqueness, typography drama, color conviction, content clarity, decorative quality)`
- Line 535 (PL-3): `apply the 6-axis scoring (1-10 scale): visual impact, layout uniqueness, typography drama, color conviction, content clarity, decorative quality` → `apply the 9-axis scoring (1-10 scale): composition variety, shape diversity, font discipline, visual impact, layout uniqueness, typography drama, color conviction, content clarity, decorative quality`

- [ ] **Step 5: Commit Phase 5**

```bash
git add .claude/skills/slidev/references/scoring-subroutine.md
git add .claude/skills/slidev/references/ab-testing.md
git add .claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): expand scoring from 6 to 9 axes (composition, shape, font)"
```

---

### Task 10: Add Design Quality Rules for new features

**Files:**
- Modify: `.claude/skills/slidev/SKILL.md:1352-1367` (Design Quality Rules section)

- [ ] **Step 1: Add 3 new Design Quality Rules**

After rule 25 (font discipline, added in Task 1), add:

```markdown
26. **Composition-aware layouts**: Use the Composition Plan (Step 4.5) to select archetype for each slide. Never default to the same card-grid layout. Each slide uses a named archetype from `references/composition-archetypes.md`. Entropy rule: no archetype repeats within a 4-slide window.
27. **Shape variety**: At least 20-30% of visual elements should be non-rectangular: circle icon containers, pill badges, typographic heroes without card wrappers. Check the preset's shape vocabulary and apply it. All-rectangles = design failure.
28. **CTA color smoothness**: CTA slide background shares at least one color channel with the preceding slide. Penultimate slide begins the color transition. See Principle 7 CTA transition rule.
```

- [ ] **Step 2: Commit**

```bash
git add .claude/skills/slidev/SKILL.md
git commit -m "feat(slidev): add design quality rules for composition, shapes, CTA"
```

---

### Task 11: Final integration commit and verification

- [ ] **Step 1: Verify all files are consistent**

Read through all modified files to check:
- SKILL.md references `references/composition-archetypes.md` correctly
- Step 4.5 placement is between Step 4 and Step 5
- All "6 axes" → "9 axes" changes are applied
- All "7 questions" → "8 questions" changes are applied
- --help includes --add_archetype
- Preset format docs match SKILL.md descriptions

- [ ] **Step 2: Final commit if any fixes needed**

```bash
git add -A .claude/skills/slidev/
git commit -m "fix(slidev): integration fixes after visual diversity implementation"
```

- [ ] **Step 3: Generate summary**

Print:
```
Implementation complete. Files modified:

  .claude/skills/slidev/SKILL.md
    - Font blacklist + 2-font rule
    - Step 4.5: Composition Planning
    - --add_archetype subcommand
    - Wizard: 8 questions
    - PL-1/PDL-1: updated refs
    - Deep learn: archetype-aware critic
    - Auto-preset: archetype generation
    - Design Quality Rules: 3 new rules
    - All scoring refs: 6→9 axes

  .claude/skills/slidev/references/composition-archetypes.md (NEW)
    - 15 archetype definitions with HTML skeletons
    - Content type → archetype mapping table

  .claude/skills/slidev/references/design-principles.md
    - Principle 4: icon style selection
    - Principle 7: CTA color transition

  .claude/skills/slidev/references/scoring-subroutine.md
    - 9-axis scoring (3 new: composition, shape, font)

  .claude/skills/slidev/references/ab-testing.md
    - 6→9 axes reference

  .claude/skills/slidev/references/preset-format.md
    - New fields: iconStyle, densityProfile, maxFonts
    - New sections: archetypes, shapes

To validate: run /slidev on a new outline — it should use Step 4.5
to create a Composition Plan and select diverse archetypes.
```
