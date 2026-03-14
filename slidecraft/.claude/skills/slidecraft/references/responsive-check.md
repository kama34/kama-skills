# Responsive Check

Check presentation rendering at 4:3 aspect ratio. Subcommand: `--responsive [dir]`.

SlideCraft uses percentage-based absolute positioning, so zone layouts generally scale well — but edge cases exist, especially where zone dimensions assume 16:9 proportions.

## Input

- `dir` — project directory (optional). Auto-detection: look for `slides.md` in cwd; if not found, scan one level deep for most recently modified directory containing `slides.md`.

## Procedure

### RESP-1: Validate

1. Auto-detect dir
2. Verify `<dir>/slides.md` and `<dir>/slides/` (PNG backgrounds) exist
3. `npm install` if no `node_modules/`
4. `npx playwright install chromium`

### RESP-2: Read Current Aspect Ratio

Parse `aspectRatio` from `slides.md` headmatter. Default: `16/9`. Save the original value for restoration.

### RESP-3: Export Baseline

Run Export Subroutine for `<dir>` `--output slides-qa` (at current aspect ratio). This serves as the reference composite (both layers).

### RESP-4: Test 4:3

1. Temporarily change `aspectRatio` in `slides.md` headmatter to `4/3`
2. Run Export Subroutine for `<dir>` `--output slides-responsive`

### RESP-5: Visual Comparison

Read ALL PNGs from `<dir>/slides-responsive/`. For each slide, check:

**Zone layout checks:**
- Text zone overflow or clipping outside visible area — percentage positions scale, but a `width: 56%; left: 4%` zone that fitted at 16:9 may feel cramped at 4:3
- Zone content (bullets, headings) overflowing zone boundaries vertically — 4:3 is taller relative to width, so vertical content may have more room but horizontal zones are narrower
- Two-column zones (split-40-60) collapsing or overlapping due to narrower frame

**Background image checks:**
- AI-generated PNG background scales correctly via `object-fit: cover; object-position: center`
- Important visual elements in the PNG are not cropped by the tighter 4:3 frame — check if zone-clarity areas (where the PNG is visually clean for text) still align with the text zones
- PNG composition designed for 16:9 (e.g., right-35% visual interest) may appear differently cropped at 4:3

**Text readability checks:**
- Font sizes still readable at narrower aspect ratio
- Long headings that fit on one line at 16:9 may wrap at 4:3 (zone is narrower in absolute pixels)
- Bullet lists: check line wrapping does not overflow zone height

**Layer harmony at 4:3:**
- Does the text zone still land on the visually clear region of the background PNG?
- If the PNG had its "clean zone" on the left, does the 4:3 crop preserve that clean zone?

### RESP-6: Restore

Set `aspectRatio` back to original value in `slides.md` headmatter. This is critical — never leave the file modified.

### RESP-7: Report

**If issues found:**
```
Responsive check: <dir>

  Tested: 16:9 → 4:3
  Issues found: N

  Slide 3: [description of issue — e.g., "zone-main overflows at 4:3 — heading wraps to 3 lines, bottom bullet clipped"]
  Slide 7: [description of issue — e.g., "PNG background crops right side, loses visual interest area; text zone still readable"]
  Slide 9: [description of issue — e.g., "split zone layout collapses — right zone overlaps left zone at 4:3"]

  Recommendation: Use /slidecraft --edit <dir> "fix responsive issues: [list specific issues]"
  Note: PNG backgrounds cannot be cropped differently at 4:3 — zone strategy or content must adapt.
```

**If no issues found:**
```
Responsive check: <dir>

  Tested: 16:9 → 4:3
  Issues found: 0

  Background scaling: ✓ object-fit:cover handles aspect change correctly
  Zone overflow:      ✓ all zones within bounds at 4:3
  Text readability:   ✓ no line wrapping or clipping issues

  Recommendation: Presentation renders cleanly at 4:3. No changes needed.
```

Note: fixes are NOT auto-applied. Use `--edit` to address specific slides.

### RESP-8: Cleanup

```bash
rm -rf <dir>/slides-responsive
```
