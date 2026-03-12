# Analyze Mode Reference

Retrospective activity analysis over N days (default 7).
Parsing: `--analyze=N`, `analyze N`, `a N`, `a` (default N=7).

## Data Collection

1. Load state.json
2. Compute date_from = today - N days
3. **Load ALL task lists** via `list-tasklists`
4. For EACH list: `list-tasks(tasklist_id, showCompleted=true)`
5. Filter tasks with `completed` date >= date_from
6. Also collect all `needsAction` tasks (stale detection)

## 7 Analysis Blocks

### Block 1: Velocity

```
total_completed = tasks closed in N days (across all lists)
velocity = total_completed / N (tasks/day)
trend = compare first vs second half of period
```

Output:
```markdown
### 1. Velocity

**Tasks closed**: {total} in {N} days ({velocity:.1f} tasks/day)
**Trend**: {up / stable / down} (first half: {X}, second: {Y})
```

### Block 2: Priority Alignment

```
For each closed task, determine priority by prefix [P0]/[P1]/[P2]/[P3]
No prefix = "no priority"
Compare: % of P0 tasks closed vs P1/P2/P3
```

Output:
```markdown
### 2. Priority Alignment

| Priority | Closed | % of total |
|----------|--------|------------|
| P0       | {n}    | {pct}%     |
| P1       | {n}    | {pct}%     |
| P2       | {n}    | {pct}%     |
| P3       | {n}    | {pct}%     |
| None     | {n}    | {pct}%     |

**Alignment Score**: {score}/100
```

Scoring:
- 100: >50% closed tasks = P0
- 75: >30% P0
- 50: P1 dominates (normal if few P0)
- 25: P2/P3 dominate (drift!)
- 0: only unprioritized tasks

### Block 3: Goal Distribution

```
Group closed tasks by task list name
Show top-5 lists by completed task count
Show % of total
```

Output:
```markdown
### 3. Goal Distribution

| Project | Closed | % | Bar |
|---------|--------|---|-----|
| {list1} | {n} | {pct}% | {bar} |
| {list2} | {n} | {pct}% | {bar} |

**Focus Index**: {score}/100 (100 = all in 1 project, 0 = spread across 10+)
```

Focus index = (max_project_pct / 100) * 100.

### Block 4: Stale Tasks

```
Find tasks with needsAction status where:
- due date has passed (overdue)
- OR no due date and created > 7 days ago
These are "stale" tasks — may need deletion or re-evaluation
```

Output:
```markdown
### 4. Stale Tasks

{If stale tasks exist:}
| List | Task | Age |
|------|------|-----|
| {list} | {title} | {days}d |

**Recommendation**: Remove or re-prioritize {count} stale tasks.

{If none:}
No stale tasks — clean!
```

### Block 5: Consistency & Patterns

```
From state.json:
- streak.current, streak.best
- history.checkins for period (approximate from streak data)

From tasks:
- Group closed tasks by day of week (Mon-Sun)
- Find most productive day
- Find "dead days" (0 tasks)
```

Output:
```markdown
### 5. Consistency

**Streak**: {current} days (best: {best})
**Checkins in period**: ~{N_checkins}
**Most productive day**: {day} ({count} tasks)
**Days without completions**: {count} of {N}
```

### Block 6: Pareto Analysis (80/20)

```
Which 1 project produced the most results?
Which tasks were "high impact" (P0 closed)?
```

Output:
```markdown
### 6. Pareto (80/20)

**Top project**: {name} — {pct}% of all completions
**High-impact tasks** (P0 closed):
- {task1}
- {task2}

{If few P0 tasks:}
Warning: Few P0 tasks closed. Focus may be diluted on minor items.
```

### Block 7: Recommendations

Generate 3-5 actionable recommendations based on blocks 1-6:

```markdown
### 7. Recommendations

1. **{Type}**: {Recommendation}
   _Why_: {Data from analysis}

2. **{Type}**: {Recommendation}
   _Why_: {Data from analysis}
```

Recommendation types (pick relevant ones):
- **Focus**: if Goal Distribution is spread out -> "Concentrate on {top goal}"
- **Priorities**: if Alignment Score < 50 -> "More P0 tasks, fewer minor items"
- **Velocity**: if trend down -> "Pace declining. Possible reason: {hypothesis}"
- **Stale cleanup**: if >3 stale -> "Review {N} stale tasks"
- **Consistency**: if many dead days -> "Try closing at least 1 task per day"
- **Pareto**: if 1 project = 80%+ -> "Great focus!" or "Other goals abandoned?"
- **Streak**: if streak < 3 -> "Restore daily checkin habit"
- **Mentor**: if mentors = 0 for period -> "Run `/game mentor` to reassess goals"

### Summary Table

```markdown
## Summary for {N} days

| Metric | Value | Rating |
|--------|-------|--------|
| Velocity | {X} tasks/day | {good/ok/low} |
| Priority Alignment | {score}/100 | {good/ok/low} |
| Focus Index | {score}/100 | {good/ok/low} |
| Consistency | {X}/{N} active days | {good/ok/low} |
| Stale tasks | {count} | {good/ok/high} |

**Overall score**: {avg_score}/100
```

Ratings: good (>=70), ok (40-69), low (<40)

### After Analysis

- Do NOT award XP for analyze (informational mode only)
- Do NOT update state.json
- Suggest: "Want to run `/game mentor` based on analysis results?"
