# Outline Information Density Review — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add information density checks to the outline skill's default generator and reviewer agents.

**Architecture:** Two-file edit — extend generator's quality rules so it produces slide-appropriate content from the start, and extend reviewer's evaluation criteria so it catches density violations during the review loop.

**Tech Stack:** Markdown prompt files (no code, no tests — these are LLM agent prompts)

**Spec:** `docs/superpowers/specs/2026-03-20-outline-density-review-design.md`

---

### Task 1: Add density rules to generator

**Files:**
- Modify: `outline/.claude/skills/outline/assets/default/agents/default-generator.md:40-47` (Structure Quality Rules section)

- [ ] **Step 1: Add three density rules to Structure Quality Rules**

Append after the existing last rule (`- **No filler** — every slide must earn its place`):

```markdown
- **5-7 bullets max per slide** — if you need more, split into two slides
- **Concise bullets** — each bullet is 10-12 words max; it's a cue, not a sentence
- **No text walls** — if a slide reads like a paragraph, it needs restructuring
```

- [ ] **Step 2: Verify the file reads correctly**

Read the full file and confirm:
- All 10 rules are present (7 original + 3 new)
- No formatting issues
- The rest of the file is untouched

- [ ] **Step 3: Commit**

```bash
git add outline/.claude/skills/outline/assets/default/agents/default-generator.md
git commit -m "feat(outline): add density rules to default generator"
```

---

### Task 2: Add Information Density criterion to reviewer

**Files:**
- Modify: `outline/.claude/skills/outline/assets/default/agents/default-reviewer.md:48-51` (after criterion #6)

- [ ] **Step 1: Add criterion #7 after the Opening and Closing section**

Insert after the `### 6. Opening and Closing` block (after line 50):

```markdown
### 7. Information Density
- Does each slide have no more than 5-7 bullet points?
- Is each bullet concise (10-12 words max), serving as a cue rather than a full sentence?
- Are there slides that look like text walls (dense paragraphs instead of structured points)?
- If a slide exceeds density limits, can it be split into two or trimmed without losing meaning?
```

- [ ] **Step 2: Verify the file reads correctly**

Read the full file and confirm:
- All 7 criteria are present (6 original + 1 new)
- The Iteration Guidance and Output sections are untouched
- APPROVED/NEEDS_REVISION protocol is intact

- [ ] **Step 3: Commit**

```bash
git add outline/.claude/skills/outline/assets/default/agents/default-reviewer.md
git commit -m "feat(outline): add information density criterion to default reviewer"
```
