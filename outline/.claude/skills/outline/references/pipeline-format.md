# Pipeline Format

The `pipeline.md` file defines the execution order of agents, loop behavior, and stop criteria.

## YAML Schema

The file contains a YAML frontmatter block with a single `steps` array:

```yaml
---
steps:
  - agent: <agent-name>
    role: <create|review|fix|enhance>
    # ... additional fields
---
```

Optional body text after the frontmatter is ignored (can be used for comments/documentation).

## Step Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `agent` | string | **Yes** | Name of the agent file (without `.md` extension). Must match a file in `agents/`. |
| `role` | string | **Yes** | Agent's role: `create`, `review`, `fix`, or `enhance`. |
| `loop_with` | string | No | Name of another agent to loop with. Creates a review→fix cycle. |
| `stop_when` | string | **Yes** when `loop_with` is set | Stop condition: `approved` (reviewer outputs `APPROVED`). |
| `optional` | boolean | No | If `true`, agent is not critical to the pipeline. Default: `false`. |
| `run_after` | string | No | When to run: `loop` means after the main loop completes. |

## Roles

| Role | Purpose | Typical Count |
|------|---------|--------------|
| `create` | Generates the initial structure from the topic | 1 |
| `review` | Evaluates the current draft and gives verdict | 1 |
| `fix` | Revises the draft based on reviewer feedback | 0-1 |
| `enhance` | Post-loop improvement (e.g., Q&A generation) | 0+ |

## Loop Semantics

The loop follows this pattern:

```
Generator runs once (role: create)
  └─→ Review → Fix → Review → Fix → ... (up to max_iterations)
         └─→ Exit when: APPROVED or max_iterations reached
```

**Full loop shape:** 1 generation + up to `max_iterations` rounds of (review → fix).

So `max_iterations: 3` means: 1 initial generation + up to 3 rounds of (review → fix) = maximum 4 total agent invocations for the generator/fixer.

## Reviewer Output Protocol

**CRITICAL:** The reviewer agent MUST output one of these as its **last line**:

- `APPROVED` — structure meets quality standards, exit loop
- `NEEDS_REVISION: <specific feedback>` — issues found, continue loop

The orchestrator parses the reviewer's last non-empty line to determine the verdict.

## No-Fixer Pattern

When `loop_with` points to a `create`-role agent (instead of a `fix`-role agent), the generator itself re-runs with the reviewer's feedback as additional context. The generator serves as both creator and fixer.

This is the default pipeline pattern — simpler, fewer agents, works well for most cases.

## Example 1: Default 2-Agent Pipeline

```yaml
---
steps:
  - agent: default-generator
    role: create
  - agent: default-reviewer
    role: review
    loop_with: default-generator
    stop_when: approved
---
```

Flow: generator creates → reviewer evaluates → if NEEDS_REVISION, generator re-runs with feedback → reviewer evaluates again → ... until APPROVED or max_iterations.

## Example 2: 4-Agent Pipeline with Post-Loop Agent

```yaml
---
steps:
  - agent: structure-generator
    role: create
  - agent: investor-reviewer
    role: review
  - agent: structure-fixer
    role: fix
    loop_with: investor-reviewer
    stop_when: approved
  - agent: qa-generator
    role: enhance
    optional: true
    run_after: loop
---
```

Flow: generator creates → reviewer evaluates → if NEEDS_REVISION, fixer revises → reviewer evaluates → ... until APPROVED or max_iterations → then qa-generator runs once.

## Validation Rules

The orchestrator validates the pipeline before execution:

1. Every `agent` value in `steps` MUST have a corresponding `agents/<agent>.md` file
2. Every `loop_with` value MUST reference an agent defined in `steps`
3. A `stop_when` field is required whenever `loop_with` is present
4. At least one agent with `role: create` must exist
5. At least one agent with `role: review` must exist

If validation fails, the orchestrator reports the specific error and stops.

## Standard Context Variables

These variables are available for substitution in agent prompts:

| Variable | Description | Available To |
|----------|-------------|-------------|
| `{{topic}}` | User's original topic | All agents |
| `{{current_draft}}` | Latest version of the structure | review, fix, enhance agents |
| `{{feedback}}` | Reviewer's feedback text (after `NEEDS_REVISION:`) | fix agents (or create agents in no-fixer pattern) |
| `{{iteration}}` | Current iteration number (1-based) | All agents |
| `{{output_format}}` | Format instructions for the output | create, fix agents |
