# Improvements from Learn Iteration 1

## Applied Changes (critical + major systemic issues only)

### Change 1: Add inline HTML decorative element pattern to Step 5
- **File**: SKILL.md
- **Section**: Step 5 → point 8 "Apply Decorative Layer (Principle 6)"
- **Type**: expand_checklist
- **Description**: CSS ::after pseudo-elements via class names don't render in Slidev's headless export. Decorative elements MUST be real HTML div elements with inline styles inside the background layer.
- **Before**: "Add the chosen decorative motifs to 30-50% of slides as CSS pseudo-elements or background layers."
- **After**: "Add the chosen decorative motifs to 30-50% of slides as REAL HTML div elements with inline styles inside the background layer div (z-index:0). CSS pseudo-elements (::after, ::before) via class names DO NOT render reliably in Slidev's headless PNG export. Instead, create actual positioned div elements. Example dot grid: `<div style=\"position:absolute;top:0;right:0;width:280px;height:280px;background-image:radial-gradient(circle,rgba(var(--accent-rgb),0.18) 1.2px,transparent 1.2px);background-size:18px 18px;pointer-events:none;\"></div>`. Example radial glow: `<div style=\"position:absolute;bottom:-60px;right:-60px;width:400px;height:400px;background:radial-gradient(circle,rgba(var(--accent-rgb),0.10),transparent 65%);pointer-events:none;\"></div>`. Example arc: `<div style=\"position:absolute;top:-100px;left:-100px;width:300px;height:300px;border:2.5px solid rgba(var(--accent-rgb),0.18);border-radius:50%;pointer-events:none;\"></div>`. Rotate motif types across slides — no two adjacent slides use the same motif."

### Change 2: Add structural break enforcement rule to Step 5
- **File**: SKILL.md
- **Section**: Step 5 → after "CRITICAL — Layout Diversity (Principle 2)" block
- **Type**: add_rule
- **Description**: Generator produces 7+ consecutive slides with identical "label → heading → grid" structure despite using different archetype names. Need explicit structural break rule.
- **Before**: N/A (new rule)
- **After**: "**STRUCTURAL BREAK RULE**: Track the heading position pattern across consecutive content slides. After 2 content slides with 'label-top-left + heading-below + grid/cards-below' structure, the 3rd MUST break the pattern using one of: (a) centered layout — heading centered, no label, content centered below (stat-hero, section-divider), (b) visual-dominant — a large metric or visual element occupies left 40%, text is secondary, (c) heading-only — no label above the heading. This rule applies regardless of archetype names — what matters is the VISUAL structure as rendered."

### Change 3: Increase bg-alt usage minimum
- **File**: SKILL.md
- **Section**: Step 4.5 → background level assignment algorithm step 6
- **Type**: modify_rule
- **Description**: bg-alt appeared on only 1/10 slides (10%), making the deck visually monotone. Need minimum 25% for non-bookend slides.
- **Before**: "Assign bg-alt to floor(R * 0.15) additional slides, spaced every 5th-6th"
- **After**: "Assign bg-alt to floor(R * 0.25) additional slides, spaced every 3rd-4th content slide. bg-alt MUST appear on at least 25% of non-cover/CTA slides (minimum 2 slides in a 10-slide deck, minimum 3 in a 12+ slide deck)."

## Deferred (minor issues — logged for review)
- Icon container shape uniformity (all rounded-square, no circles) — minor, addressed by preset shapes section
- Stat-hero heading repeating the hero number — minor content issue
