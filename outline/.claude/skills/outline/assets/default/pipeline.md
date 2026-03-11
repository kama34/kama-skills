---
steps:
  - agent: default-generator
    role: create
  - agent: default-reviewer
    role: review
    loop_with: default-generator
    stop_when: approved
---

Default 2-agent pipeline using the no-fixer pattern:
- Generator creates the initial structure
- Reviewer evaluates and provides feedback
- If NEEDS_REVISION, generator re-runs with the feedback as context
- Loop continues until APPROVED or max_iterations reached
