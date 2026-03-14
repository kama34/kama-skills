# Content Review Subroutine

A reusable subroutine for reviewing presentation content quality. Called by `--polish`, QA (Phase 3), and `--learn`.

**Input:** `<dir>` — project directory containing `slides/slide-*.png` and `prompts.json`

## Process

Read `prompts.json` for slide roles and text content. Read all PNGs from `<dir>/slides/` for visual verification. Check 5 aspects:

### 1. Three-Second Test

Can each slide's main message be understood in 3 seconds?

Flag:
- Too much text (> 4-5 distinct text blocks visible)
- Competing equal-weight elements (nothing stands out)
- No clear focal point (eye wanders)
- Main message requires reading body text to understand

### 2. Narrative Flow

Logical progression through the deck: Problem → Solution → Evidence → CTA (or similar arc).

Flag:
- Gaps: "Slide N introduces solution but slide N-1 doesn't establish the problem"
- Jumps: traction data before product explanation
- Missing setup: data without context
- Abrupt ending: no summary or CTA before the end slide

### 3. Redundancy

Same information appearing on multiple slides.

Flag:
- Same metric on multiple slides
- Same concept explained twice with different words
- Repeated visual patterns (same chart type used 3+ times)

Recommend: show data once on the stronger slide.

### 4. CTA Clarity

On Ask/CTA/End slides:
- Is the ask unambiguous? (specific amount, timeline, next step)
- Is there a clear action the audience should take?

Flag:
- Vague CTAs ("Get in touch")
- Missing specifics (no timeline, no amount, no next step)
- Multiple competing asks on one slide

### 5. Information Hierarchy

ONE clear focal element per slide.

Flag:
- All elements equal size/weight (no hierarchy)
- Hero metric smaller than or equal to heading size
- No visual distinction between primary and supporting content
- Body text competing with heading for attention

## Output

Write structured issue list with severity levels:

- **CRITICAL**: audience will be confused or lost
  - Fails 3-second test
  - Narrative gap before CTA
  - Key slide has unreadable text
- **MAJOR**: quality degraded but message comes through
  - Redundancy between slides
  - Weak information hierarchy
  - Narrative flow has minor gaps
- **MINOR**: polish issue, not a comprehension problem
  - Slightly verbose text
  - Minor redundancy
  - Could benefit from better visual emphasis

Format:
```
## Content Review Results

### CRITICAL
- [Slide N] Fails 3-second test: too much text competing for attention

### MAJOR
- [Slides 3, 7] Redundancy: both show "market size" metric
- [Slide 5] Weak hierarchy: heading and body text appear same weight

### MINOR
- [Slide 4] Slightly verbose: body text could be condensed

### Passed
- Narrative flow: logical progression ✓
- CTA clarity: clear ask on slide 10 ✓
```
