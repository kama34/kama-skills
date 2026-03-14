# Image Prompt Composition Guide

How to write effective prompts for image generation models to produce high-quality **background-only** presentation slides for SlideCraft's two-layer architecture.

**Key principle:** SlideCraft AI images contain NO text. Text is rendered by Slidev as an HTML/CSS overlay on top of the PNG background. Prompts must describe visual zones reserved for text — leaving them clean, uniform, and ready for overlay.

## Prompt Structure

Every slide prompt follows this structure:

```
[Slide type and format] + [Layout with empty zones] + [Visual details OUTSIDE zones] + [Explicit empty zone instructions] + [Style suffix]
```

### 1. Slide Type and Format (always first)

Start every prompt with the format declaration:

> "A 16:9 aspect ratio presentation slide background. This is a [role] slide."

Role substitutions:
- `cover` → "This is a cover/title slide — pure background, all text areas left empty"
- `section` → "This is a section divider slide — pure background, text zones left clear"
- `content` → "This is a content slide — heading zone and body zone left empty for overlay"
- `stat` → "This is a statistics/data slide — central metric zone and label zone left clear"
- `quote` → "This is a quote slide — quotation zone left empty for text overlay"
- `comparison` → "This is a comparison slide — both column text zones left empty"
- `end` → "This is a closing slide — call-to-action zone left clear for overlay"

### 2. Layout with Empty Zones

Describe WHERE zones are reserved (empty), and WHERE decorative visual elements appear (outside zones). Reference coordinates from `layout-plan.json` zone definitions.

**Good (spatial with empty zones):**
- "Upper-left zone (60% wide, 15% tall, starting at top-left) left completely empty for heading text — visual elements only in remaining areas"
- "Left two-thirds contains body zone — clean uniform surface in that region; illustration placed only in the right third"
- "Central zone (40% wide, 30% tall, centered) left clear for stat display — decorative elements at outer edges only"

**Bad (vague or zone-free):**
- "Put a heading somewhere"
- "Add some visual interest"
- "Include a background pattern"

### 3. Visual Details OUTSIDE Zones

Describe decorative and atmospheric elements that appear only in non-zone regions:

- **Background**: "Deep navy (#1a1a2e) solid background" or "Gradient from dark blue (#1a1a2e) to deep purple (#2d1b4e)"
- **Atmospheric elements**: Place illustrations, patterns, or geometric shapes explicitly outside zone boundaries
- **Decorative accents**: "Thin horizontal electric blue (#0066ff) line at 18% from top — below the heading zone"
- **Icons/graphics**: Specify exact position outside zones: "Subtle geometric pattern in the bottom-right 20% corner only"

### 4. Explicit Empty Zone Instructions

**CRITICAL:** For each text zone defined in `layout-plan.json`, include a zone-clearing instruction using this pattern:

> "Leave the [position description] area — [width%]×[height%] starting at [x%, y%] from top-left — completely empty. This zone must have a uniform, clean [color/surface description] suitable for [light/dark] text overlay."

Rules for zone instructions:
- Reference the exact `prompt_hint` text from the zone's entry in `layout-plan.json` when available
- Every zone defined in `layout-plan.json` MUST have a corresponding clearing instruction in the prompt
- All visual elements MUST be placed ONLY outside text zones
- Zone backgrounds must be uniform and predictable for text overlay contrast — no textures, gradients, or patterns inside zones
- State the expected text color (light or dark) so the zone surface provides appropriate contrast
- **CRITICAL: Zones must blend seamlessly into the background.** Do NOT instruct the AI to "create a panel", "draw a rectangle", or "add a box" for zones. The zone should be an organic part of the background — simply a calm region where the same base color/gradient continues, free of decorative elements. Use language like "leave this area as calm, uncluttered background" NOT "create an empty panel/box here"

### 5. Style Suffix

Append the style suffix (defined during Design Thinking) to every prompt. This ensures consistency across slides.

## Zone Contrast Guarantee

Every zone instruction must guarantee readable contrast for the text overlay. The prompt must specify:

1. **Zone surface color**: "uniform dark navy (#1a1a2e)" or "clean off-white (#f5f5f5)" — never gradients or textures
2. **Expected text color class**: "suitable for white text" or "suitable for dark text"
3. **Zone isolation**: "no decorative elements crossing into this zone"

If a zone sits over a complex visual region, the prompt must either:
- Push visual complexity away from the zone entirely, OR
- Specify a solid color block behind the zone area

## Example Prompts

### Cover Slide

> A 16:9 aspect ratio presentation slide background. This is a cover/title slide — pure background, all text areas left empty. Dark navy (#1a1a2e) base with a diagonal gradient toward deep purple (#2d1b4e) in the lower-right quadrant. Subtle geometric hexagon pattern in the lower-right corner only — bottom 35% and right 30% of the slide — very low opacity, does not enter the title zone. A thin electric blue (#0066ff) horizontal accent line at 62% from the top, spanning the full width, marking the visual division between title and subtitle regions. Leave the upper-center zone — 80% wide, 30% tall, starting at 10% from left and 15% from top — completely empty with uniform dark navy (#1a1a2e) surface suitable for white text overlay. Leave the lower-center zone — 60% wide, 12% tall, starting at 20% from left and 52% from top — completely empty with the same uniform dark navy surface suitable for light gray text overlay. Professional, technology-focused mood. Clean, no clutter in the reserved zones.

### Content Slide

> A 16:9 aspect ratio presentation slide background. This is a content slide — heading zone and body zone left empty for overlay. Dark navy (#1a1a2e) base. Leave the upper-left zone — 65% wide, 14% tall, starting at 5% from left and 6% from top — completely empty with uniform dark navy suitable for white heading text. Leave the left body zone — 60% wide, 55% tall, starting at 5% from left and 24% from top — completely empty with uniform dark navy suitable for white body text. A thin electric blue (#0066ff) horizontal line at 22% from top, spanning 60% of width from the left — placed below the heading zone as a decorative separator, not crossing into zones. Right third of slide (from 68% to 100% width) contains a subtle abstract illustration in low-opacity blue tones — entirely outside the text zones. Clean modern sans-serif mood.

### Stat Slide

> A 16:9 aspect ratio presentation slide background. This is a statistics/data slide — central metric zone and label zone left clear. Dark navy (#1a1a2e) base. Leave the central metric zone — 40% wide, 35% tall, centered horizontally at 30% from top — completely empty with uniform dark navy (#1a1a2e) suitable for large electric blue stat text. Leave the label zone — 50% wide, 12% tall, centered horizontally at 67% from top — completely empty with uniform dark navy suitable for white label text. A thin circular ring decorative element centered on the slide, radius extending only to the outer edge of the metric zone — does not enter the empty zone. Subtle radiating line pattern in the four outer corners only, very low opacity. Clean modern sans-serif mood.

## Style Consistency Reinforcement

When generating slides 3+ in reference mode, prepend an **anchor palette description** to each prompt. This is a 3-4 sentence description of the anchor slide's visual characteristics that reinforces consistency even when the reference image alone is insufficient.

Format:
```
STYLE CONSISTENCY: This presentation uses [dominant color with hex] to [secondary color with hex] background with [accent color with hex] accent elements. Decorative motifs are [motif type], positioned in [position]. The mood is [mood]. ALL slides MUST maintain this exact palette and decoration style — do not introduce new colors, warm tones, or different decoration styles.
```

**This is CRITICAL for maintaining visual consistency.** Without it, the AI model may drift to completely different palettes (e.g., switching from teal to orange) even with a reference image.

## Anti-Patterns

| Problem | Why it fails | Fix |
|---|---|---|
| Text content in prompt | AI renders unreadable or hallucinated text into the PNG | Remove ALL text from prompt — use zone instructions instead |
| "Make a nice slide background" | Too vague, no zone guidance | Specify every zone coordinate and visual element placement |
| Zones without clearing instructions | AI fills zones with visuals, blocking text overlay | Add explicit empty zone instructions for every zone |
| Patterns or textures inside zones | Text overlay becomes unreadable | Keep zones uniform and solid-colored |
| Visible rectangles/borders marking zones | Zones look like "holes" cut in the design | Use "leave area as calm background" — never "draw empty panel/box" |
| Prompt > 2000 chars | Model may ignore details | Prioritize zone instructions, simplify decorative descriptions |
| Missing zone contrast spec | Model picks surface that conflicts with text color | Always specify zone surface color AND expected text color |
| "Use Arial font" | Model cannot use specific fonts | Irrelevant — fonts are handled by Slidev CSS, not the image |
| Conflicting instructions | "Minimalist with many decorative elements" | Pick one direction for decorative regions |
| No background specified | Model uses random backgrounds | Always describe base background color explicitly |
| Visual elements crossing zone boundaries | Bleeds into text overlay area | Explicitly constrain each element to non-zone regions |
| Missing anchor palette description | Slides 3+ drift to different color palettes | Always prepend STYLE CONSISTENCY block for slides 3+ |

## Prompt Length Guidelines

- **Cover/End slides**: 100-200 words (simple layout, fewer zones to clear)
- **Content slides**: 150-300 words (multiple zones, decorative right panel)
- **Stat slides**: 100-200 words (central zones, minimal decoration)
- **Comparison slides**: 200-350 words (multiple column zones to clear)

Stay under 2000 characters total. If the prompt is getting too long, simplify decorative element descriptions first — zone clearing instructions are never optional.
