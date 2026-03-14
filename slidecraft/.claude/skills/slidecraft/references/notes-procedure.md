# Notes Procedure

Generate speaker notes for the presentation. Subcommand: `--notes [dir]`.

## Procedure

### NOTES-1: Resolve Directory

Use provided `[dir]` or auto-detect (see Directory Auto-Detection in SKILL.md). Verify `prompts.json` and `slides/` exist.

### NOTES-2: Read Slides

1. Load `prompts.json` for slide roles, headings, and text content.
2. Read each PNG from `slides/` for visual context.
3. Check if `notes.md` already exists in the directory. If yes, parse it for existing notes.

### NOTES-3: Generate Notes

For each slide WITHOUT existing notes, generate 4 structured speaking points:

1. **Opening** (1 sentence): What appears on this slide and how to introduce it.
2. **Key message** (1 sentence): The ONE thing the audience should remember from this slide.
3. **Details** (1-2 sentences): Supporting elaboration, data context, or talking points.
4. **Transition** (1 sentence): Bridge to the next slide's topic.

Write to `<dir>/notes.md`:

```markdown
# Speaker Notes

## Slide 1: [heading]
**Role:** cover

- **Opening:** Welcome the audience and introduce the topic of AI in Healthcare.
- **Key message:** We're here to explore how machine learning is transforming patient care.
- **Details:** This presentation covers three key areas: diagnosis, monitoring, and treatment optimization.
- **Transition:** Let's start by looking at the current landscape.

## Slide 2: [heading]
**Role:** content

- **Opening:** This slide shows the three key benefits we've identified.
- **Key message:** AI reduces diagnosis time by 40% while improving accuracy.
- **Details:** The 99.2% accuracy figure comes from our 2025 clinical trial across 12 hospitals. The 24/7 monitoring capability replaces manual overnight checks.
- **Transition:** Now let's look at the numbers behind these improvements.

...
```

**Language:** Notes should match the language of the slide content. If slides are in Russian, notes are in Russian.

### NOTES-4: Skip Existing Notes

If `notes.md` already exists and has notes for a slide, do NOT overwrite. Log: "Slide N: skipped (has existing notes)".

### NOTES-5: Report

Print:
```
Speaker notes generated!

  New notes:     N slides
  Skipped:       M slides (existing notes preserved)
  Total:         K slides
  Output:        <dir>/notes.md
```
