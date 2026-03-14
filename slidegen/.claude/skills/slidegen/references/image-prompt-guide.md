# Image Prompt Composition Guide

How to write effective prompts for image generation models to produce high-quality presentation slides.

## Prompt Structure

Every slide prompt follows this structure:

```
[Slide type and format] + [Layout and composition] + [Text content] + [Visual details] + [Style suffix]
```

### 1. Slide Type and Format (always first)

Start every prompt with the format declaration:

> "A 16:9 aspect ratio presentation slide. This is a [role] slide."

Role substitutions:
- `cover` → "This is a cover/title slide — prominent title, minimal body text"
- `section` → "This is a section divider slide — section heading, transitional"
- `content` → "This is a content slide — heading with body text, bullets, or key points"
- `stat` → "This is a statistics/data slide — large numbers, charts, or key metrics"
- `quote` → "This is a quote slide — prominent quotation with attribution"
- `comparison` → "This is a comparison slide — two or more items side by side"
- `end` → "This is a closing/thank-you slide — call to action or contact info"

### 2. Layout and Composition

Describe WHERE elements go on the slide:

**Good (spatial):**
- "Title centered in the upper third"
- "Three bullet points in the left two-thirds, illustration in the right third"
- "Large number '85%' centered vertically, label text below"

**Bad (vague):**
- "Put the title somewhere"
- "Add some bullet points"
- "Include a statistic"

### 3. Text Content

Write out EVERY word that must appear on the slide. The model renders text from your prompt — if you don't specify it, it won't appear (or will be hallucinated).

**Good:**
> Heading text reads "Market Overview". Three bullet points read: "• $4.2B market size in 2025", "• 23% year-over-year growth", "• 3 major competitors"

**Bad:**
> Add a heading about the market and some statistics

### 4. Visual Details

Include specific visual instructions:
- **Background**: "Deep navy (#1a1a2e) solid background" or "Gradient from dark blue (#1a1a2e) to deep purple (#2d1b4e)"
- **Text colors**: "White heading text", "Light gray (#e0e0e0) body text"
- **Typography**: "Large bold heading approximately 48pt", "Body text approximately 24pt regular weight"
- **Decorative elements**: "Thin horizontal blue (#0066ff) line below the heading", "Subtle geometric pattern in the bottom-right corner"
- **Icons/graphics**: "Small simple icon of a chart next to each bullet point" (be specific about icon style)

### 5. Style Suffix

Append the style suffix (defined during Design Thinking) to every prompt. This ensures consistency across slides.

## Example Prompts

### Cover Slide
> A 16:9 aspect ratio presentation slide. This is a cover/title slide — prominent title, minimal body text. Dark navy background (#1a1a2e) with a subtle diagonal gradient to deep purple (#2d1b4e). Large centered heading reads "AI in Healthcare" in white bold text, approximately 64pt. Below it, smaller text reads "Transforming Patient Care with Machine Learning" in light gray (#b0b0b0), approximately 28pt. A thin horizontal electric blue (#0066ff) line separates the title from the subtitle. Subtle geometric hexagon pattern in the bottom-right corner, very low opacity. Clean modern sans-serif typography throughout. Professional, technology-focused mood.

### Content Slide
> A 16:9 aspect ratio presentation slide. This is a content slide — heading with body text, bullets, or key points. Dark navy background (#1a1a2e). Heading in the top-left reads "Key Benefits" in white bold text, approximately 40pt. Below the heading, a thin electric blue (#0066ff) horizontal line. Three bullet points in white text, approximately 24pt, with blue bullet markers: "• Reduced diagnosis time by 40%", "• 99.2% accuracy in image analysis", "• 24/7 automated monitoring". Each bullet has a small relevant icon to its left (clock, target, monitor). Right third of the slide has a subtle abstract medical illustration in low opacity blue tones. Clean modern sans-serif typography.

### Stat Slide
> A 16:9 aspect ratio presentation slide. This is a statistics/data slide — large numbers, charts, or key metrics. Dark navy background (#1a1a2e). Centered large number "85%" in electric blue (#0066ff) bold text, approximately 120pt. Below it, label text reads "Accuracy Improvement" in white, approximately 28pt. A subtle circular progress indicator behind the number, thin stroke. Small text at the bottom reads "Based on 10,000 patient records" in light gray (#888888), approximately 16pt. Clean modern sans-serif typography.

## Anti-Patterns

| Problem | Why it fails | Fix |
|---|---|---|
| "Make a nice slide" | Too vague, model guesses everything | Specify every visual element |
| "Professional business presentation" | Generic, no distinctive style | Describe specific colors, typography, mood |
| Prompt > 2000 chars | Model may ignore details | Prioritize, be concise |
| Missing text content | Model invents random text | Write every word explicitly |
| "Use Arial font" | Model can't use specific fonts | Describe the font mood: "clean geometric sans-serif" |
| Conflicting instructions | "Minimalist with many decorative elements" | Pick one direction |
| No background specified | Model uses random backgrounds | Always describe background explicitly |
| No text color specified | Model picks poor contrast colors | Always specify text color relative to background |

## Prompt Length Guidelines

- **Cover/End slides**: 100-200 words (simple layout, fewer elements)
- **Content slides**: 150-300 words (more elements to describe)
- **Stat slides**: 100-200 words (simple but precise)
- **Comparison slides**: 200-350 words (multiple sections to describe)

Stay under 2000 characters total. If the prompt is getting too long, simplify decorative elements first.
