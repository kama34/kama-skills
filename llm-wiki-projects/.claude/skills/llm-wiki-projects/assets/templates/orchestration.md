---
type: project
status: active
created: {{date}}
updated: {{date}}
language: {{language}}
tags:
  - orchestration
---

# Orchestration Log

Append-only log for staged or resumable project work.

## Entry Format

```markdown
## YYYY-MM-DD HH:MM | Stage <n> | <name> | iter <m>
- Pre-state:
- Action:
- Metrics:
- Result:
- Post-state:
- Decision:
- Notes:
```
