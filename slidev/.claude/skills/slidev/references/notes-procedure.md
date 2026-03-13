# Notes Procedure

Generate speaker notes for slides that don't have them. Subcommand: `--notes [dir]`.

## Input

- `dir` — project directory (optional). Defaults to auto-detection: look for `slides.md` in the current working directory; if not found, scan one level deep for the most recently modified directory containing `slides.md`.

## Procedure

### NOTES-1: Resolve Dir

If `[dir]` provided → use it. Otherwise auto-detect as described above.

Verify `<dir>/slides.md` exists. If not, print error and stop.

### NOTES-2: Read slides.md

1. Parse all slides (split by `---` separators)
2. For each slide, check if it already contains a presenter notes block: look for `<!--` comment blocks that contain speaking points

### NOTES-3: Generate Notes

For each slide **WITHOUT** existing notes:

1. Analyze slide content: title, bullet points, metrics, visual elements, layout type
2. Generate 4 structured speaking points:
   - **Opening**: What to say when this slide appears (1 sentence)
   - **Key message**: The ONE thing the audience should remember (1 sentence)
   - **Details**: 1-2 supporting points to elaborate on
   - **Transition**: How to bridge to the next slide (1 sentence)

3. Write using Slidev presenter notes syntax — a comment block at the end of the slide's content section, before the next `---` separator:

```markdown
Slide content here...

<!--
Opening: This slide introduces our core product capabilities.
Key message: We solve the three biggest pain points in the industry.
Details: Each capability maps directly to customer feedback from Q4 surveys. The AI-powered feature alone reduced processing time by 60%.
Transition: Now let's look at the traction these capabilities have generated.
-->
```

**Language**: Generate notes in the same language as the slide content.

### NOTES-4: Skip Existing Notes

If a slide already has a `<!--` comment block containing speaking points:
- Do NOT overwrite or modify
- Log: `"Slide N: skipped (has existing notes)"`

### NOTES-5: Report

```
Speaker notes added: <dir>

  Slides with new notes: N
  Slides skipped (existing notes): M
  Total slides: N + M
```
