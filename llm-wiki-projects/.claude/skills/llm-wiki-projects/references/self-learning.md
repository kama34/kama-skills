# Self-Learning Loop

Use this reference when a wiki process fails, a user corrects the agent, or a repeated maintenance problem appears.

## Lesson Format

Append lessons to `90-meta/lessons-learned.md`:

```markdown
## L-NNN: Short title
- **Date:** YYYY-MM-DD
- **Context:** what was happening when the issue appeared
- **What went wrong:** concrete observation
- **Root cause:** mechanism, not just "forgot"
- **Fix:** file, rule, validator, template, or skill updated
- **Promotion trigger:** when this should become a general rule
```

## Promotion Ladder

Promote a lesson when it is likely to recur:

1. One-off: keep it in lessons.
2. Repeated or high-risk: add a rule to `90-meta/wiki-rules.md`.
3. Mechanically detectable: add a validator check.
4. Workflow-level: update a template, reference, or local skill.
5. Broadly reusable: consider updating the global skill.

## Maintenance Rule

After promoting a lesson, update `90-meta/log.md` and run validation. If the fix changes how future agents should work, update `90-meta/skills-registry.md` or the relevant project dashboard.

## Good Root Causes

Good root causes describe the system failure:

- the validator ignored tool directories;
- the project dashboard was treated as input-only;
- raw evidence and source summaries were mixed;
- service notes leaked into a final artifact;
- a Markdown/Obsidian syntax interaction was not covered by validation.

Avoid vague root causes such as "agent forgot" unless paired with the missing rule, check, or artifact.
