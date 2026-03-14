# Slidegen — AI Image Presentation Generator

A Claude Code skill that generates complete presentations as AI-generated images.

## Usage

```
/slidegen <outline or topic>                          Generate with unique design
/slidegen --preset <name> <outline>                   Generate with preset style
/slidegen style: <desc> <outline>                     Generate with custom style
/slidegen --provider polza --model <id> <outline>     Use specific provider/model
/slidegen --no-ref <outline>                          Generate without style references
/slidegen --polish=N [dir]                            Iterative quality improvement
/slidegen --edit [dir] <comment>                      Edit existing presentation
/slidegen --compare <dir1> <dir2>                     Compare two presentations
/slidegen --notes [dir]                               Generate speaker notes
/slidegen --learn=N                                   Self-improving loop
/slidegen --create-preset <name>                      Create a new preset
/slidegen --export pdf [dir]                          Reassemble PDF from PNGs
/slidegen --help                                      Show help
```

## Output

Each generation produces:
- `slides/slide-01.png`, `slide-02.png`, ... — individual slide images
- `slides.pdf` — assembled PDF
- `prompts.json` — saved prompts for editing/regeneration
- `meta.json` — generation metadata (provider, model, style anchor)

## Default Provider

Polza.ai with model `google/gemini-3.1-flash-image-preview`. Override with `--provider` and `--model` flags.
