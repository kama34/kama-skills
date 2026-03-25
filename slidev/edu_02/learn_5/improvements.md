# Improvements from Learn Iteration 5

## Applied Changes (critical + major systemic issues)

### Change 1: Mandatory Eyebrow Counter in Step 5 Enforcement
- **File**: SKILL.md
- **Section**: Step 5, "Enforcement rules during writing", item "Eyebrow label limit (30%)"
- **Type**: modify_rule
- **Description**: Add a mandatory per-slide counter that prevents exceeding the 30% eyebrow limit. The rule exists but lacked a concrete tracking mechanism — writers would accumulate eyebrows on all slides because each archetype template includes a `{{LABEL}}` slot. This change adds an explicit counter with example.
- **Before**: `"Track usage during writing — when the limit is reached, omit the eyebrow on remaining slides and let the heading speak for itself. Section dividers count toward the limit. Cover and CTA slides are exempt (they have their own label patterns)."`
- **After**: `"Track usage during writing — when the limit is reached, omit the eyebrow on remaining slides and let the heading speak for itself. Section dividers count toward the limit. Cover and CTA slides are exempt (they have their own label patterns).\n   **MANDATORY COUNTER**: Before writing each slide, compute: allowed = floor(total_content_slides × 0.30). Track with a comment before each slide in the plan: <!-- eyebrow: N/allowed -->. When eyebrow_count reaches 'allowed', all subsequent slides get NO eyebrow label — the heading speaks for itself. Example: 8-slide deck (6 content slides) → allowed = floor(6 × 0.30) = 1 eyebrow. After that 1 eyebrow is used, the remaining 5 content slides have NO eyebrow label."`

### Change 2: Ghost Deck Test — Section Divider Minimum Standard
- **File**: SKILL.md
- **Section**: Step 4.5, Ghost Deck test — ENHANCED, "FAIL conditions" (the line about Cover/CTA exemption)
- **Type**: modify_rule
- **Description**: Section divider slides currently have no title quality requirement — they can use pure topic labels ("Почему клиенты остаются") without any claim. This creates weak narration in the Ghost Deck test. Adding a rule that section dividers must have either (a) an action heading, or (b) a description with a claim.
- **Before**: `"Cover slide (slide 1) and CTA slide (last slide) are exempt (aligns with Rule 30)."`
- **After**: `"Cover slide (slide 1) and CTA slide (last slide) are exempt (aligns with Rule 30).\n     **Section divider slides**: Heading may be a topic label ONLY IF the description below it contains a claim, number, comparison, or outcome. If the description is also generic (no number, verb, or outcome), FAIL — upgrade the heading to an insight. Pattern: 'Почему клиенты остаются' (heading) + 'Долгосрочные партнёрства — главный показатель' (description with claim) → PASS. 'Наши достижения' (heading) + 'Результаты нашей работы' (description, no claim) → FAIL."`

## Deferred (minor issues — logged for review)

- **3-slide fingerprint window**: Extend visual fingerprint dedup check from adjacent pairs to 3-slide triplets (N, N+1, N+2). Currently only adjacent slides are checked. When a breathing slide separates two 2×2 grids, the check doesn't fire. Low priority — spacing of 1 different slide usually sufficient.
- **Metric card gap 16px→20px**: For asymmetric stat-hero with 3 stacked metric cards, recommend gap:20px instead of gap:16px. Currently acceptable at 16px but slightly crowded.
- **Cover dot grid placement**: On cover slides with centered headings, avoid dot grids in upper-center zone (heading collision zone). Place in corners only.
