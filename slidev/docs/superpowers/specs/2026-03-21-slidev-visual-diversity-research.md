# Research: Visual Diversity in Presentation Generation

**Date:** 2026-03-21
**Context:** Feedback from [S26] group on generated KP presentation revealed systematic visual monotony issues. This document captures research findings and all explored approaches.

## Feedback Summary

| Problem | Who | Details |
|---------|-----|---------|
| Font rendering on numbers | Maka, Anna | Syne renders digits unevenly — "то сверху, то снизу, то длинный, то сплющенные" |
| Too many fonts | Vladimir, Anna | Should be strictly 2 fonts (headings + text), not 3+ visual voices |
| Repetitive rectangular blocks | Anna | Boring identical card blocks. Reference from Behance: circular inserts, photos, asymmetry, whitespace |
| AI-looking icons | Vladimir | SVG icons look generic/AI-generated |
| Sharp color transition | Vladimir | Last amber slide too contrasting against dark deck |
| Content overload | Vladimir | "Too much junk material for a commercial proposal" |

### Reference: @ness_shch (KPD Ecosystem)
Anna shared a Behance-style portfolio piece showing: light theme, real photos, diverse block shapes (circles, full-width, pills, asymmetric compositions), single font family, unique composition per slide.

---

## Industry Research Findings

### How Professional Tools Solve Visual Monotony

**Beautiful.ai** — Smart Slide system with ~300 layout types organized into 6 functional categories (Charts, Impact, Comparison, People, Diagram, Big Number). Key innovation: **Bento Grid** — mixed-size rectangular zones creating density variety. Layout variety is achieved through function-specific layout logic, not randomization.

**Gamma.app** — Content-aware layout selection, but reviewers found it "reuses the same designs for every deck — just in different colors." Having the architecture isn't enough — the selection algorithm must actively resist repetition.

**Canva** — Brute force: thousands of templates organized by topic. Works for human-driven design, not automated generation.

**Pitch.com** — Template library + AI cohesion. Good deck-level consistency, but doesn't solve in-deck layout variety algorithmically.

### 6 Signatures of AI-Generated Slides

1. **Uniform information density** — every slide has same amount of text/visuals
2. **Same layout on 80%+ slides** — "title + content block" repeated
3. **Rectangular block uniformity** — all elements are rectangles with identical border-radius
4. **Hedged color palette** — safe navy + white + one accent
5. **Generic stock imagery** — smiling office people, abstract circuits
6. **Structural predictability** — Problem → Solution → Features → Team → CTA every time

### What Breaks the AI Pattern

**Content level:** Specific titles, real data, purposeful images
**Layout level:** Enforce layout rotation (no repeat in 5-slide window), vary density, use non-rectangular shapes for 20-30% of elements, include pure-typographic and full-bleed slides
**System level:** Content-aware forced diversity — classify content type → assign composition archetype → enforce architectural rules

---

## Full Taxonomy: Visual Block Types Beyond Rectangles

### Slide-Level Composition Archetypes (15-20 needed minimum)

| Archetype | Visual Structure | Best For |
|-----------|-----------------|----------|
| `cover` | Full-bleed image + oversized title overlay | Opening, section starts |
| `statement` | Single bold sentence, centered, minimal | Key insight, transition |
| `stat-hero` | Oversized number (80%+ of slide) + brief label | Metrics, impressive data |
| `full-bleed` | Edge-to-edge photo/color, text minimal | Emotion, pause moments |
| `two-col-text` | Left/right equal division | Comparison, contrast |
| `asymmetric-split` | 30/70 or 40/60 division, large image + text | Visual + context |
| `diagonal-split` | Angular division line between zones | Dynamic, modern |
| `icon-trio` | 3-5 icons with labels, horizontal | Features, benefits |
| `bento-3` | One large zone + two smaller zones | Multi-fact, overview |
| `timeline-h` | Horizontal sequence with markers | Process, history |
| `timeline-zigzag` | Alternating left-right along vertical axis | Steps, evolution |
| `profile-grid` | Circle photos + name/role blocks | Team introductions |
| `quote-pull` | Large quotation marks, oversized text | Testimonials, impact |
| `section-divider` | Minimal text, bold color/number | Chapter breaks |
| `data-spotlight` | Chart dominant + one annotation callout | Insights from data |
| `funnel` | Narrowing stages | Conversion, pipeline |
| `comparison-table` | Rows + columns, checkmarks | Feature comparison |
| `image-left` | 40% photo + 60% content | Photo-supported content |
| `image-right` | 60% content + 40% photo | Content with visual |
| `masonry` | Irregular overlapping image layout | Portfolio, creativity |

### Sub-Slide Shape Vocabulary

- **Pill/Badge** — rounded rectangle for labels, tags, status indicators
- **Circle callout** — circular container for icons, people, key numbers
- **Diamond/Rhombus** — decision points, highlight elements
- **Hexagon tile** — feature grids, technical capability maps
- **Arrow shapes** — directional flow, process steps
- **Overlapping shapes** — depth, connection between concepts
- **Diagonal rule lines** — section separators with energy
- **Gradient blobs/organic shapes** — modern, editorial feel
- **Cutout/masked photos** — image shaped to circle, hexagon, or custom shape
- **Number badges** — large numerals as structural decorative elements

### Shape Semantics (from Material Design / Apple HIG)

- **Circles** — continuity, process, people/faces
- **Triangles** — direction, hierarchy, achievement
- **Hexagons** — capabilities, features, technical topics
- **Curves/Arcs** — growth, flow, timelines
- **Spirals** — journeys, expansion
- **Lines** — dividers, timelines, organizational structures
- **Rounded corners** — approachable, modern
- **Sharp corners** — authoritative, precise

---

## Explored Approaches

### Approach A: Component Vocabulary (extend shape dictionary)

Define a full set of visual blocks in the preset beyond cards: `circle-callout`, `pill-badge`, `stat-hero`, `card-wide`, `hexagon-tile`, `diagonal-split`.

| Pros | Cons |
|------|------|
| Maximum flexibility | Without strict rules, AI still picks 2-3 "safe" forms (the Gamma problem) |
| Easy to add new forms | Doesn't guarantee slide-level diversity |
| Simple implementation | Requires "design intuition" from LLM during assembly |

**Verdict:** Necessary but not sufficient. Good as a building block layer, not as the primary diversity mechanism.

### Approach B: Composition Templates (slide archetypes)

Define 15-20 named composition archetypes: `stat-hero`, `icon-trio`, `bento-3`, `timeline-h`, `image-left`, `profile-grid`, `quote-pull`, `full-bleed`, etc. Each is a complete slide structure with HTML/CSS.

| Pros | Cons |
|------|------|
| Guaranteed visual variety | May not fit specific content |
| Predictable output | Can feel formulaic |
| No design intuition needed from LLM | Requires large upfront investment in template library |
| Easy to test and QA | Rigid — limited adaptation to content |

**Verdict:** Strong for guaranteeing variety, but too rigid alone. Works best combined with content classification.

### Approach C: Content-Aware Selection (RECOMMENDED)

Classify content type of each slide → select archetype from library → populate with components. Plus **entropy rules**: no archetype repeat within 4-slide window, mandatory density alternation.

Architecture:
```
1. Content Analysis → detect type (data, quote, team, process, comparison, etc.)
2. Template Selection → choose from 15-25 named composition archetypes
3. Component Population → fill template slots with appropriate components
4. Entropy Rules → prevent same template repeating within N slides
```

Content type → archetype mapping:
```
"intro"         → cover, statement
"metric"        → stat-hero, data-spotlight
"quote"         → quote-pull
"transition"    → section-divider, statement, full-bleed
"feature_list"  → icon-trio, bento-3, two-col-text
"comparison"    → comparison-table, two-col-text
"process"       → timeline-h, timeline-zigzag, funnel
"team"          → profile-grid
"photo_story"   → image-left, image-right, full-bleed
"data"          → data-spotlight, bento-3
```

Deck-level entropy rules:
- No archetype repeats within a 4-slide window
- Every 10-slide deck must include: 1+ full-bleed/statement, 1+ stat-hero or data slide, 1+ image-dominant slide
- Adjacent slides must differ in information density

| Pros | Cons |
|------|------|
| **Proven approach** (Beautiful.ai's core architecture) | Most complex to implement |
| Contextually appropriate layouts | Needs content type classifier |
| Forced diversity through rules | Needs archetype library (~15 compositions) |
| Solves root cause, not symptom | |

**Verdict:** Best overall. This is the approach Beautiful.ai uses. Selected for implementation.

### Approach D: Composition Rules (parametric rules instead of templates)

Instead of fixed templates, define parametric rules. Example: "split composition = one zone takes 30-70% of horizontal space (visual), other takes remainder (text); visual can be left or right." One rule generates many specific layouts.

| Pros | Cons |
|------|------|
| More variability than fixed templates | Harder to implement and debug |
| Fewer templates needed | Less predictable results |
| Elegant architecture | Harder to guarantee quality per layout |
| Good for advanced iteration | Higher risk of broken outputs |

**Verdict:** Elegant but risky for automated generation. Good as a future evolution of Approach C — once the archetype library is stable, some archetypes could be replaced with parametric rules.

---

## Recommended Implementation Plan (Approach C)

### Phase 1: Fix immediate issues (SKILL.md point fixes)
- Font blacklist: ban Syne for number-heavy presentations, add number rendering check
- Strict 2-font rule enforcement
- Icon style diversification (not just Lucide-stroke)
- Smoother CTA slide color transition

### Phase 2: Build composition archetype library
- Define 15 named archetypes with HTML/CSS reference implementations
- Add to `references/composition-archetypes.md`
- Each archetype includes: visual structure, HTML skeleton, when to use, density level

### Phase 3: Content-aware selection logic
- Add content type classification step to generation procedure
- Add mapping rules (content type → candidate archetypes)
- Add entropy rules (no repeat in 4-slide window, density alternation)

### Phase 4: Extend preset format
- Add optional `preferred-archetypes` section to .preset.md
- Add `shape-vocabulary` section (which sub-slide shapes to use)
- Add `density-profile` (minimal / balanced / dense)

### Phase 5: Validation via --learn
- Run --learn=5 with new rules
- Compare scores before/after
- Iterate on archetype library based on visual critic feedback

---

## Decision

**Selected approach: C (Content-Aware Selection)**

Rationale: proven in industry (Beautiful.ai), solves root cause (structural monotony not just stylistic), and compatible with existing skill architecture (adds a classification step before the current generation procedure).
