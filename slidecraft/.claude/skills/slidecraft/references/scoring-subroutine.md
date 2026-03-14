# Scoring Subroutine

A reusable subroutine for scoring SlideCraft two-layer presentation slides on design quality. Called by `--polish`, `--learn`, and `--compare`.

**Input:** `<dir>` — project directory containing `slides/slide-*.png` (composited previews with Slidev text overlay rendered as screenshots, OR AI-only PNGs when text layer is not yet applied)

**Important:** Scores are Claude's subjective visual assessment of the composited slide output, not deterministic metrics. Used for relative comparison within a single session.

**Two-layer context:** Each slide is the product of an AI-generated PNG background (no text) and a Slidev HTML/CSS text overlay. When diagnosing low scores, identify which layer is the source of the problem — this determines the remediation path.

## Process

Read EVERY PNG from `<dir>/slides/`. For each slide, evaluate and score 1-10 on 6 axes:

| Axis | What to evaluate | Low (1-3) | Below threshold (4-5) | Acceptable (6-7) | Good (8-9) | Exceptional (10) |
|---|---|---|---|---|---|---|
| Visual Impact | AI background quality + overall first impression and memorability of the composited slide | Forgettable background, generic or auto-generated feel, no visual pull | Recognizable as a presentation but not striking; background adds nothing | Decent background quality, professional enough, competent composition | Would stand out in a conference; background is visually polished and purposeful | Background could be showcased as a design reference; immediately arresting |
| Layout Precision | Accuracy of text positioning within zones — text fits bounds, no overflow, balanced spacing, zones correctly utilized | Text visibly overflows zones, misaligned, or zones completely ignored | Text roughly in zone but clipping or poor spacing; minor misalignment | Text fits zones with acceptable spacing; no visible overflow | Text sits cleanly within zones with strong spatial balance and breathing room | Perfect zone utilization; text and zones feel designed together |
| Typography Quality | Readability of text overlay against the AI background; font hierarchy; contrast; line-height | Text unreadable against background, no hierarchy, garbled or clashing | Text readable with effort; weak hierarchy; contrast borderline | Clear heading/body distinction, text readable against background | Strong 3+ scale levels; text crisp and clear against background in all zones | Hero elements pop beautifully; type treatment enhances the visual background |
| Color Conviction | AI background palette coherence + harmony between background colors and Slidev text/accent colors | Clashing palettes between layers; incoherent background colors | Palette exists in each layer but layers don't complement each other | Consistent background palette; text colors workably aligned with background | Background and text layer colors feel designed as a single cohesive system | Palette across both layers tells a unified story; perfectly balanced |
| Content Clarity | Information hierarchy and readability at presentation scale; logical flow across slides | Cluttered, competing elements, message buried or invisible | Message findable but requires effort; layout hinders comprehension | Message clear on first glance; adequate information density | Instant comprehension; perfect density; hierarchy is immediately obvious | Information hierarchy is effortless; could be understood at a glance from 5 meters |
| Layer Harmony | How well the AI background and text overlay work together — text complements rather than fights the visual; compositional synergy | Layers actively conflict — text invisible, background overwhelms, zones filled with visuals | Layers coexist but don't reinforce each other; background indifferent to text placement | Layers work acceptably; background provides neutral surface for text | Background and text feel designed together; visual draws eye toward text zones | Seamless integration — text and background appear as a single composed design |

## Remediation Source Detection

For each axis scoring < 7, identify the source layer and apply the appropriate remediation:

| Axis | Source layer | Remediation |
|------|-------------|-------------|
| Visual Impact | Image (AI PNG) | Regenerate PNG with modified prompt — improve atmosphere, lighting, decorative quality |
| Layout Precision | Both | Adjust zone coordinates in `layout-plan.json` → regenerate PNG with updated zone hints → update Slidev CSS positioning |
| Typography Quality | Text (Slidev CSS) | Adjust font sizes, weights, line-heights, and text colors in Slidev slide CSS |
| Color Conviction | Image (AI PNG) | Regenerate PNG with adjusted palette instructions in prompt; also verify Slidev accent colors match |
| Content Clarity | Text (Slidev content) | Restructure text, adjust information hierarchy, reduce density, improve heading/body distinction |
| Layer Harmony | Both | Analyze which layer causes the dissonance — if background visual elements bleed into zones, fix prompt; if text color clashes with background tone, fix CSS |

## Output

Write score report to `<dir>/score-report.md`:

```markdown
# Score Report

Generated: <timestamp>
Provider: <provider> / <model>
Mode: <reference|no-reference>

## Per-Slide Scores

| Slide | Role | Impact | Precision | Typo | Color | Clarity | Harmony | AVG |
|-------|------|--------|-----------|------|-------|---------|---------|-----|
| 1     | cover | 8    | —         | 7    | 8     | 9       | 8       | 8.0 |
| 2     | content | 7 | 6         | 8    | 7     | 8       | 7       | 7.2 |
| ...   | ...  | ...    | ...       | ...  | ...   | ...     | ...     | ... |

**Layout Precision note:** Slide 1 (cover) is scored "—" for Layout Precision because it has no adjacent slide for structural comparison. It is excluded from the Layout Precision average only when used in layout-variety analysis.

## Overall Score: X.X / 10

## Weakest Slides (avg < 7)
- Slide N: avg X.X — [axis] is low because [reason] — source layer: [Image/Text/Both] — remediation: [action]

## Strongest Slides (avg >= 9)
- Slide N: avg X.X — [what makes it strong across both layers]

## Slides Below Threshold (any axis < 6)
- Slide N: [axis] scored X — [reason] — source layer: [Image/Text/Both] — **candidate for [regeneration/CSS fix/both]**

## Layer Analysis
- Image layer issues: [list slides where Visual Impact, Color Conviction, or Layer Harmony is low due to background]
- Text layer issues: [list slides where Typography Quality or Content Clarity is low due to CSS/content]
- Both-layer issues: [list slides where Layout Precision or Layer Harmony requires coordinated fix]
```

## Thresholds

- **Any single axis < 6** → slide is a remediation candidate (per-axis gate)
- **Slide avg < 7** → weak (candidate for redesign in `--polish`)
- **Slide avg >= 9** → strong (do not touch in `--polish`)
- **Overall avg >= 9** → consider early exit from polish cycle
