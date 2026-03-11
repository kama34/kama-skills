---
name: outline
description: "Use when creating presentation outlines/structures. Supports agent pipeline templates, auto-selection, template creation, and agent training. Handles --template, --format, --create-template, --learn=N, and --help."
argument-hint: "[--help | --template <name> | --format <fmt> | --create-template | --learn=N [template]] [<topic>]"
---

# Outline — Presentation Structure Generator

You generate presentation structures using agent pipelines. Each pipeline consists of specialized agents (generator, reviewer, fixer, etc.) that iteratively create, review, and refine a presentation outline.

## References

Before executing, internalize these references:
- `references/template-format.md` — **CRITICAL**: Template directory specification (metadata, storage, naming, collisions)
- `references/pipeline-format.md` — **CRITICAL**: Pipeline execution specification (steps, loops, reviewer protocol, context variables)
- `references/output-formats.md` — Output format specs (slidev, universal, custom)

## Input Parsing

Parse the user's input to determine the subcommand or mode:

### Subcommands (handle before anything else)

**`--help`**: Display usage help and stop. Show:

```
Outline — Presentation Structure Generator

Usage:
  /outline <topic>                              Generate structure (auto-select template)
  /outline --template <name> <topic>            Use specific template
  /outline --format <slidev|universal|custom>   Override output format
  /outline --create-template                    Create new agent pipeline template
  /outline --learn=N [template]                 Train agents with N test runs
  /outline --help                               This help text

How it works:
  Outline uses agent pipelines to iteratively create, review, and refine
  presentation structures. Each template is a set of specialized agents
  (generator, reviewer, fixer, etc.) tailored to a specific presentation type.

  When no template is specified, the skill auto-selects the best match
  or falls back to default agents (universal generator + reviewer).

Output formats:
  slidev      (default) ## Slide N: Title + bullets — compatible with /slidev
  universal   Sections, theses, speaker notes — tool-agnostic
  custom      Defined by the template

Templates stored at:
  Local:   .outline-templates/<name>/
  Global:  ~/.claude/outline-templates/<name>/
  Lookup:  local first, then global
```

Stop here — do not proceed to generation.

---

**`--create-template`**: Run the Create Template Procedure (CT-1 through CT-8). Stop here — do not proceed to generation.

---

**`--learn=N [template]`**: Run the Learn Procedure (L-1 through L-6). Parse N from the argument (e.g., `--learn=5`). Optional `template` argument specifies which template to train. Stop here — do not proceed to generation.

---

**Otherwise** — this is a generation request. Parse `--template`, `--format`, and extract the topic. Run the Generate Procedure (G-1 through G-7).

---

## Generate Procedure

### G-1: Parse Command

Extract from the user's input:
- **Topic** — the presentation subject (everything that isn't a flag)
- **`--template <name>`** — optional, specific template to use
- **`--format <slidev|universal|custom>`** — optional, output format override

If no topic is provided, ask the user: "What is the presentation about?"

### G-2: Select Template

Three paths, in priority order:

**Path A: `--template <name>` specified**

1. Look up `<name>` in local storage: `.outline-templates/<name>/`
2. If not found, look up in global storage: `~/.claude/outline-templates/<name>/`
3. If not found in either, error:
   ```
   Template '<name>' not found.
   Searched: .outline-templates/<name>/, ~/.claude/outline-templates/<name>/
   Available templates: <list all found templates, or "none">
   ```
   Stop here.

**Path B: Auto-select from available templates**

1. Scan for templates in both locations:
   - `.outline-templates/*/template.md`
   - `~/.claude/outline-templates/*/template.md`
2. If templates exist, read each `template.md` to extract `name`, `description`, `keywords`
3. Make a single LLM call (use the Agent tool) with the user's topic and all template metadata:

   ```
   Given the presentation topic: "<topic>"

   Available templates:
   1. <name>: <description> (keywords: <keywords>)
   2. <name>: <description> (keywords: <keywords>)
   ...

   Which template best matches this topic? Reply with ONLY the template name,
   or "none" if no template is a good match.
   ```

4. If the agent responds with a template name → use that template
5. If the agent responds "none" → use default (Path C)

**Path C: Use built-in default**

Use the default template from `assets/default/` within the skill directory. This path is used when:
- No templates exist in local or global storage
- Auto-selection returns "none"

### G-3: Load & Validate Pipeline

1. Read the template directory:
   - `template.md` — extract frontmatter fields
   - `pipeline.md` — extract `steps` array
   - `agents/*.md` — read all agent files

2. **Validate pipeline:**
   - Every `agent` value in `steps` must have a corresponding file in `agents/`
   - Every `loop_with` value must reference an agent in `steps`
   - `stop_when` is required when `loop_with` is present
   - At least one `role: create` agent exists
   - At least one `role: review` agent exists

   If validation fails:
   ```
   Pipeline validation error: <specific issue>
   Example: Agent 'investor-reviewer' referenced in pipeline.md but no file agents/investor-reviewer.md found.
   ```
   Stop here.

3. **Determine active settings:**
   - `max_iterations` — from template.md (default: 3)
   - **Active format** — `--format` flag > template `format` field > `slidev`
   - Build `{{output_format}}` variable based on active format:
     - `slidev` → `"Use slidev outline format: ## Slide N: Title followed by bullet points. Aim for 8-12 slides."`
     - `universal` → `"Use universal format: ## Section N: Title, each with a Thesis statement, Key points as bullets, and Speaker notes in blockquotes."`
     - `custom` → use the literal `custom_format_description` text from template.md

### G-4: Run Pipeline Cycle

Initialize context variables:
```
topic         = user's topic
current_draft = "" (empty initially)
feedback      = "" (empty initially)
iteration     = 1
output_format = <constructed in G-3>
```

**Execute pipeline steps in order:**

For each step in the `steps` array:

#### Step with `role: create` (Generator)

1. Read the agent file from `agents/<agent>.md`
2. Substitute all `{{variables}}` in the agent prompt with current context values
3. Dispatch via the **Agent tool** as a subagent:
   - Provide the substituted prompt as the agent's task
   - Instruct the agent to output ONLY the structure, no preamble
4. Collect the agent's output → set `current_draft` to this output

#### Step with `role: review` + `loop_with` (Reviewer in a loop)

This step initiates the review→fix cycle:

1. Read the reviewer agent file from `agents/<agent>.md`
2. Substitute `{{variables}}` (including `{{current_draft}}`)
3. Dispatch the reviewer via the **Agent tool**
4. Parse the reviewer's output:
   - Find the last non-empty line
   - If it starts with `APPROVED` → exit loop, proceed to post-loop steps
   - If it starts with `NEEDS_REVISION:` → extract feedback text after the prefix

5. If `NEEDS_REVISION` and `iteration < max_iterations`:
   - Increment `iteration`
   - Set `feedback` to the extracted feedback text
   - Look up the `loop_with` agent:
     - If it has `role: fix` → read fixer agent, substitute variables, dispatch, collect output → update `current_draft`
     - If it has `role: create` (no-fixer pattern) → re-run the generator with feedback in context → update `current_draft`
   - Go back to step 1 (re-run reviewer)

6. If `NEEDS_REVISION` and `iteration >= max_iterations`:
   - Log: "Reached maximum iterations (N). Using latest draft."
   - Exit loop with current draft

#### Step with `role: review` WITHOUT `loop_with`

Run the reviewer once as a standalone evaluation. The output is informational only (no looping).

#### Step with `role: enhance` + `run_after: loop`

Skip during the main loop. These are handled in G-5.

### G-5: Run Optional Post-Loop Agents

After the main loop completes, run any steps with `run_after: loop`:

1. Read the agent file
2. Substitute `{{variables}}` (including final `current_draft`)
3. Dispatch via Agent tool
4. Append the agent's output to `current_draft` (separated by a blank line and `---`)

If an optional agent fails (`optional: true`), log the failure and continue. Do not abort.

### G-6: Save Output

**Topic slug rules:**
1. Lowercase the topic
2. Replace spaces with hyphens
3. Strip all non-alphanumeric characters except hyphens
4. Collapse consecutive hyphens into one
5. Truncate to max 50 characters at a word boundary (don't cut mid-word)

**File naming:**
- Primary: `outline-<topic-slug>.md`
- If file exists: `outline-<topic-slug>-2.md`, `outline-<topic-slug>-3.md`, etc.

**Save location:** Current working directory.

Write the final `current_draft` to the output file.

### G-7: Report

Print a summary:
```
Outline generated successfully.

  Template:   <template name or "default">
  Format:     <active format>
  Iterations: <number of iterations used> / <max_iterations>
  Output:     <file path>

To use with /slidev (if format is slidev):
  /slidev <file path>
```

---

## Create Template Procedure

### CT-1: Ask Template Name

Ask the user:
```
What name for this template? (kebab-case, e.g., investor-pitch, tech-talk)
```

Validate: must be kebab-case (lowercase letters, numbers, hyphens only). If invalid, explain and ask again.

### CT-2: Ask Description

Ask the user:
```
What is this template for? (brief description)
```

### CT-3: Ask Target Audience

Ask the user:
```
Who is the target audience? (e.g., investors, students, engineering team, general public)
```

### CT-4: Ask Output Format

Ask the user:
```
Output format?
  1. slidev — ## Slide N: Title + bullets (compatible with /slidev)
  2. universal — Sections, theses, speaker notes
  3. custom — You describe the format

Choice (1/2/3):
```

If the user chooses "custom" (3), follow up:
```
Describe the output format the generator should produce:
```

### CT-5: Ask Storage Location

Ask the user:
```
Where to save this template?
  1. global — ~/.claude/outline-templates/ (available everywhere)
  2. local — .outline-templates/ (this project only)

Choice (1/2):
```

### CT-6: Ask Additional Context (Optional)

Ask the user:
```
Any additional context or constraints? (optional — press Enter to skip)
```

### CT-6.5: Collision Check

Now that the storage location is known, check if a template with this name already exists:

- If global: check `~/.claude/outline-templates/<name>/`
- If local: check `.outline-templates/<name>/`

**CRITICAL:** A template with the same name in the OTHER location is NOT a collision.

If collision detected:
```
A template named '<name>' already exists at <path>.

  1. Overwrite — replace the existing template
  2. Rename — choose a different name
  3. Abort — cancel template creation

Choice (1/2/3):
```

- Overwrite → continue, files will be replaced
- Rename → go back to CT-1
- Abort → stop here

### CT-7: Autonomous Pipeline Design

Using the collected information, autonomously design the agent pipeline. Do NOT ask the user for agent details — design everything yourself.

**Design decisions to make:**

1. **How many agents?** Minimum 2 (generator + reviewer). Add a fixer if the audience requires specialized revision logic. Add enhance agents if post-loop processing adds value (e.g., Q&A for educational content).

2. **Agent roles and prompts:** For each agent:
   - Name (kebab-case, descriptive)
   - Role (`create`, `review`, `fix`, `enhance`)
   - Input variables it needs
   - A detailed prompt tailored to the template's audience, goals, and format

3. **Pipeline design:** Define the `steps` array in `pipeline.md`:
   - Execution order
   - Which agents loop together
   - Stop conditions
   - Optional post-loop agents

4. **Keywords:** Generate comprehensive keywords for `template.md` based on the description and audience

**Write files to the storage location:**

```
<storage-path>/<name>/
  ├── template.md
  ├── pipeline.md
  └── agents/
      ├── <agent-1>.md
      ├── <agent-2>.md
      └── ...
```

Use `max_iterations: 3` unless the template type clearly benefits from more or fewer iterations.

### CT-8: Confirmation Summary

Print:
```
Template '<name>' created successfully.

  Path:     <full path to template directory>
  Agents:   <list of agent names and roles>
  Pipeline: <brief flow description>
  Format:   <format>

Usage:
  /outline --template <name> <topic>

Or just use /outline <topic> — auto-selection will pick this template
when the topic matches its keywords.
```

---

## Learn Procedure

### L-1: Parse Arguments

- If `template` is specified:
  1. Look up by name: local (`.outline-templates/<name>/`) → global (`~/.claude/outline-templates/<name>/`)
  2. If not found, error:
     ```
     Template '<name>' not found.
     Searched: .outline-templates/<name>/, ~/.claude/outline-templates/<name>/
     ```
     Stop here.
  3. Train only this template.

- If no template specified:
  - Scan both local and global storage for all templates
  - If no templates found:
    ```
    No templates found to train. Create one first:
      /outline --create-template
    ```
    Stop here.
  - Train all found templates.

### L-2: Generate Test Topics and Run Pipelines

For each template being trained:

1. Generate N test topics that match the template's description and keywords. Topics should be diverse — vary industry, scope, and complexity.

2. For each test topic (i = 1 to N):
   a. Run the full Generate Procedure (G-1 through G-7) using this template and topic
   b. Save the output to `learn-<template-name>/run-<i>/outline.md`
   c. Save metadata (topic, iterations used, final verdict) to `learn-<template-name>/run-<i>/meta.md`

### L-3: Critic Analysis

After all N runs complete, construct a critic agent on-the-fly. Dispatch it via the Agent tool with this prompt:

```
You are a demanding presentation structure critic. Analyze N generated
presentation outlines and evaluate the agent pipeline that produced them.

INPUTS:
- Template metadata: <template.md content>
- Pipeline: <pipeline.md content>
- Agent prompts: <all agents/*.md contents>
- Generated outlines: <all N outline outputs>
- Run metadata: <all N meta.md files — topics, iterations, verdicts>

ANALYSIS:
1. Evaluate each outline for: structure quality, logical flow, coverage,
   pacing, opening/closing strength
2. Look for SYSTEMIC patterns — issues that appear across multiple runs
3. Evaluate agent effectiveness:
   - Generator: Does it produce good first drafts?
   - Reviewer: Does it catch real issues? Is it too strict or too lenient?
   - Fixer (if any): Does it actually address feedback?
4. Check if the pipeline structure itself is effective:
   - Are there enough agents?
   - Is the loop count appropriate?
   - Would adding/removing agents help?

OUTPUT FORMAT:

# Critic Report: <template-name>

## Overall Quality: X/10

## Systemic Issues

### Issue 1: [Title]
- **Severity**: critical | major | minor
- **Frequency**: N/N runs affected
- **Description**: What's wrong
- **Root cause**: Which agent's prompt allows this
- **Proposed fix**: Specific change to agent prompt — quote the
  relevant section, show before/after

## Pipeline-Level Suggestions
- [Any suggestions to modify pipeline.md — add/remove agents, change iterations]

## What Works Well
- [Patterns to preserve]
```

### L-4: Propose Changes

Based on the critic's report:

1. Generate a diff-style summary of all proposed changes:
   ```
   Proposed changes for template '<name>':

   1. [agent-name.md] — <brief description of change>
      - Before: "<relevant excerpt>"
      - After: "<proposed text>"

   2. [pipeline.md] — <brief description of change>
      - <details>

   Apply these changes? (yes / no / select)
   ```

2. Wait for user confirmation:
   - **yes** → apply all changes
   - **no** → discard all changes
   - **select** → let user pick which changes to apply (number them)

**CRITICAL:** Do NOT apply changes without user confirmation. Always show the diff summary and wait for explicit approval.

### L-5: Apply Changes

For each approved change:

1. Read the target file
2. Apply the modification using the Edit tool
3. Verify the edit was applied correctly

**Failure handling:**
- If an agent produced zero usable output across ALL N runs → mark as "critically broken", do NOT modify it, flag for user attention
- If partial runs failed → apply improvements from successful runs, note failures in report

### L-6: Report

Print a final summary:
```
Learning complete for template '<name>'.

  Runs:     N total, M successful
  Changes:  X applied, Y deferred, Z skipped (critically broken agents)
  Files modified:
    - agents/<agent>.md — <what changed>
    - pipeline.md — <what changed> (if applicable)

  Agents needing manual attention:
    - <agent-name> — <reason>
```

Clean up: the `learn-<template-name>/` directory with test outputs can be kept for reference or deleted — ask the user.

---

## Utility: Topic Slug Generation

Used by G-6 to create file names from topics.

**Rules:**
1. Convert to lowercase
2. Replace spaces with hyphens
3. Strip all characters that are not alphanumeric or hyphens
4. Collapse consecutive hyphens into a single hyphen
5. Remove leading/trailing hyphens
6. If longer than 50 characters, truncate at the last word boundary before 50 characters

**Examples:**
| Topic | Slug |
|-------|------|
| "Q4 Investor Pitch" | `q4-investor-pitch` |
| "Introduction to Machine Learning: A Primer" | `introduction-to-machine-learning-a-primer` |
| "Why Our Team Needs to Adopt CI/CD Practices ASAP!!!" | `why-our-team-needs-to-adopt-cicd-practices-asap` |
| "A Very Long Topic That Goes On And On And Definitely Exceeds Fifty Characters Limit" | `a-very-long-topic-that-goes-on-and-on-and` |
