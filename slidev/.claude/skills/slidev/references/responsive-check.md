# Responsive Check

Check presentation rendering at 4:3 aspect ratio. Subcommand: `--responsive [dir]`.

## Input

- `dir` — project directory (optional). Auto-detection: look for `slides.md` in cwd; if not found, scan one level deep for most recently modified directory containing `slides.md`.

## Procedure

### RESP-1: Validate

1. Auto-detect dir
2. Verify `<dir>/slides.md` exists
3. `npm install` if no `node_modules/`
4. `npx playwright install chromium`

### RESP-2: Read Current Aspect Ratio

Parse `aspectRatio` from `slides.md` headmatter. Default: `16/9`. Save the original value for restoration.

### RESP-3: Export Baseline

Run Export Subroutine for `<dir>` `--output slides-qa` (at current aspect ratio). This serves as the reference.

### RESP-4: Test 4:3

1. Temporarily change `aspectRatio` in `slides.md` headmatter to `4/3`
2. Run Export Subroutine for `<dir>` `--output slides-responsive`

### RESP-5: Visual Comparison

Read ALL PNGs from `<dir>/slides-responsive/`. For each slide, check:
- Text overflow or clipping outside visible area
- Column layouts collapsing or overlapping
- Image cropping that loses important content
- Font sizes still readable at new ratio
- Decorative elements positioned correctly (not clipped off-screen)
- Vertical content still fitting (4:3 is taller relative to width — content may need less vertical centering)

### RESP-6: Restore

Set `aspectRatio` back to original value in `slides.md` headmatter. This is critical — never leave the file modified.

### RESP-7: Report

**If issues found:**
```
Responsive check: <dir>

  Tested: 16:9 → 4:3
  Issues found: N

  Slide 3: [description of issue]
  Slide 7: [description of issue]
  ...

  Recommendation: Use /slidev --edit <dir> "fix responsive issues: [list specific issues]"
```

**If no issues found:**
```
Responsive check: <dir>

  Tested: 16:9 → 4:3
  Issues found: 0

  Recommendation: Presentation renders cleanly at 4:3. No changes needed.
```

Note: fixes are NOT auto-applied. Use `--edit` to address specific slides.

### RESP-8: Cleanup

```bash
rm -rf <dir>/slides-responsive
```
