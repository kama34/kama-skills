# Design Lessons — Learned From Real Generations

Read this file BEFORE reviewing any slide. These are real problems found in real generations. Each lesson = a specific failure that was missed by structural checks and visual checklist.

This file grows with each generation. Add new lessons when users report problems that QA missed.

---

## Cover / Title Slides

**Single word in oversized title = empty.** The original template "PITCH DECK" fills the space with 2 heavy words. "ПИТЧ" alone leaves 60% of the title area blank. If the content has only 1-2 short words for an oversized slot → either add a second line (subtitle) or reduce fontSize to fill the space more naturally.

**Subtitle wrapping to 3+ lines = cramped.** If subtitle container was designed for 1-2 lines of English and the Russian text takes 3+ lines, either shorten the text or expand the container width.

## Footer / Breadcrumb

**Breadcrumb "Презентация, которая убеждает" wrapping to 2 lines = FAIL.** This was consistently missed by structural checks because each word fits, but the full phrase doesn't fit in a narrow container. ALWAYS check if breadcrumb renders as ONE line. If not → expand container width to 460px+.

**Breadcrumb fix must be applied to ALL slides.** When one subagent fixes a breadcrumb on one slide, the same fix must be applied to all slides in the Global Consistency Pass. Inconsistent breadcrumbs across slides = obvious defect.

**Footer placeholder text ("Reviews / Mobile Strategy", "Product review — Month XX") = CRITICAL.** These are English placeholders from templates. In a Russian presentation they MUST be replaced with real content.

**Page numbers must be sequential 1..N.** After deleting/reordering template slides, original numbers (5, 7, 14...) remain. Must be renumbered.

## Text Overflow

**Russian text is 20-40% longer than English.** EVERY text replacement needs overflow checking. The most common failures:
- Labels inside narrow shapes ("СТРУКТУРА ПИТЧА" in a 240px blob → breaks to "СТРУКТ УРА")
- Descriptions below cards (grow down → overlap with cards/lines below)
- Footer text (wraps to 2 lines in narrow container)

**Text touching container edge = no padding.** Text inside a card/container must have ≥8px padding from all edges. Text flush against the bottom of a brown card = unprofessional.

**Text crossing dashed line separators = FAIL.** If the template has dashed lines between items and the Russian text grows beyond its zone → the text crosses the line. Fix: shorten text OR move the line down.

## Decorative Elements

**Widget/poll elements from FigJam = remove.** Templates from Figma Community often contain interactive elements (polls, votes, sliders). These must be removed (`node.remove()`) not hidden.

**Stray arrows / artifacts from previous fixes = remove.** If a previous QA iteration created a small white arrow on top of a pink arrow, or any other element that wasn't in the original template → it's an artifact. Remove it.

**"ЕЩЁ" or "→" as placeholder label on a decorative element = smells like a hack.** If the original had meaningful text and we replaced it with a single symbol because the real text didn't fit → this is NOT a fix. Either find text that fits or retemplate the slide.

## Template Fit

**Illustrations that don't match content.** E-commerce illustrations (cart, box, monitor) on a slide about P-S-I framework = wrong fit. Hide the illustrations → if slide becomes empty → retemplate.

**"Template-inherent" is NOT an excuse.** If the template doesn't work for the content, swap to a different template from the original page. "Cannot fix, template design" is only valid if you tried: expand → shorten → retemplate, and NONE worked.

**Inverted hierarchy (body fontSize > heading fontSize) on statement slides.** Some templates put body text larger than the heading. This is template design, but if it confuses the message → retemplate to a layout with clear hierarchy.

## Content Integrity

**NEVER invent content.** Fixer agents have been caught adding sentences not in the outline ("Обменяйтесь скелетами с соседней командой..."). Only text from the outline is allowed. Shortening/rephrasing is OK, inventing is NOT.

**One-word cover title looks like a placeholder.** "УБЕЖДАЕТ" alone on a huge cover → looks unfinished. The cover should clearly identify what this presentation is about.

## Consistency Across Slides

**Header positions must be consistent.** If slides 1-8 have headers at Y=40, and slide 3 has header at Y=200 after a QA fix moved it down → the fix broke deck consistency. Fixer must check all slides before applying position changes.

**Same elements should look the same across slides.** If one subagent fixed a breadcrumb on slide 3 but not slide 5, the deck looks inconsistent. Global Consistency Pass exists for this reason.

## Stale Issues That Keep Recurring

These are problems that QA consistently misses despite having rules for them:

1. **Breadcrumb wrapping** — missed because word-break check passes (each word fits, but the phrase doesn't)
2. **Text-on-line overlap** — missed when overlap check filters out "same top-level section" siblings
3. **Empty slides after hiding visuals** — missed because coverage exception says "template is sparse"
4. **Artifacts from previous fixes** — missed because structural check doesn't know what was in the original generation vs what was added by a fix
5. **Single-word oversized titles** — missed because there's no "word count too low" check for oversized slots
