# XP Engine Reference

## XP Table

| Action | XP |
|--------|-----|
| checkin | 25 |
| task_p0 | 80 |
| task_p1 | 50 |
| task_p2 | 30 |
| task_p3 | 15 |
| mentor_session | 75 |
| streak_bonus | current_streak x 5 |
| quest_weekly | 100-150 |
| quest_monthly | 200-300 |
| okr_created | 50 |

---

## Level Thresholds

| Level | Title | XP Threshold | Unlock |
|-------|-------|-------------|--------|
| 1 | Startup Dreamer | 0 | Weekly quests |
| 2 | Trailblazer | 200 | Streaks |
| 3 | Focus Warrior | 500 | Advanced quests |
| 4 | Goal-Driven | 1000 | WOOP sessions |
| 5 | Strategist | 2000 | Monthly quests |
| 6 | Focus Master | 4000 | Custom badges |
| 7 | Visionary | 6500 | Mentor deep-dives |
| 8 | Success Architect | 9500 | OKR tracking |
| 9 | Studio Legend | 13000 | Full stats |
| 10 | Titan | 17000 | All features |

### Level Calculation
```
LEVEL_THRESHOLDS = [0, 200, 500, 1000, 2000, 4000, 6500, 9500, 13000, 17000]

def get_level(xp):
    for i in range(len(LEVEL_THRESHOLDS) - 1, -1, -1):
        if xp >= LEVEL_THRESHOLDS[i]:
            return i + 1
    return 1

def xp_for_next_level(level):
    if level >= 10: return None
    return LEVEL_THRESHOLDS[level]  # next threshold
```

---

## Badges (15)

### Badge Definitions
```json
[
  {"id": "streak_3", "icon": "fire", "name": "Three Days of Fire", "condition": "streak.current >= 3"},
  {"id": "streak_7", "icon": "fire", "name": "Week in Flow", "condition": "streak.current >= 7"},
  {"id": "streak_14", "icon": "fire", "name": "Two-Week Marathon", "condition": "streak.current >= 14"},
  {"id": "streak_30", "icon": "fire", "name": "Month of Discipline", "condition": "streak.current >= 30"},
  {"id": "first_checkin", "icon": "star", "name": "First Step", "condition": "history.checkins >= 1"},
  {"id": "first_goal", "icon": "target", "name": "Goal Setter", "condition": "first goal set in mentor session"},
  {"id": "first_okr", "icon": "clipboard", "name": "OKR Master", "condition": "first OKR created"},
  {"id": "tasks_10", "icon": "check", "name": "Ten Down", "condition": "history.tasks_done >= 10"},
  {"id": "tasks_50", "icon": "check", "name": "Fifty Strong", "condition": "history.tasks_done >= 50"},
  {"id": "tasks_100", "icon": "check", "name": "Century", "condition": "history.tasks_done >= 100"},
  {"id": "first_mentor", "icon": "brain", "name": "Mentor Path", "condition": "history.mentors >= 1"},
  {"id": "first_quest", "icon": "trophy", "name": "Quest Complete", "condition": "first quest completed"},
  {"id": "level_5", "icon": "gem", "name": "Strategist", "condition": "profile.level >= 5"},
  {"id": "level_10", "icon": "crown", "name": "Titan", "condition": "profile.level >= 10"},
  {"id": "perfect_week", "icon": "lightning", "name": "Perfect Week", "condition": "5 checkins Mon-Fri"}
]
```

### Badge Check Workflow
After any state change:
1. Iterate all badge definitions
2. For each badge NOT in `state.badges`:
   - Evaluate condition against current state
   - If met: add to `state.badges`, show celebration

---

## Quest System

### Weekly Quests (available from Level 1)
| Quest | Target | XP |
|-------|--------|-----|
| 3 steps to {P0 goal} | complete 3 tasks from goal's dedicated list this week | 100 |
| Close 3 P1 tasks | tasks_p1 >= 3 | 100 |
| Run a mentor session | mentors_this_week >= 1 | 100 |
| 5 checkins in a row | streak >= 5 (within week) | 150 |

### Goal-Linked Quest Assignment
```
Quest Assignment (Monday or first checkin of week):
1. Find highest priority goal where goal.task_list is set
2. Create quest: "3 steps to {goal.name}"
3. Target: 3 tasks from goal's dedicated list completed this week
4. Progress: count tasks completed in dedicated list since Monday
```

### Monthly Quests (unlock at level 5)
| Quest | Target | XP |
|-------|--------|-----|
| Reach 70% on a Key Result | any KR progress >= 70% | 200 |
| 14-day streak | streak.current >= 14 | 250 |
| Close 20 tasks this month | tasks_done_month >= 20 | 300 |

### Quest Format in state.json
```json
{
  "weekly": {
    "id": "close_3_p1",
    "description": "Close 3 P1 tasks",
    "target": 3,
    "progress": 1,
    "xp_reward": 100,
    "started": "2026-03-10",
    "expires": "2026-03-17"
  }
}
```

---

## Streak Logic

```
def update_streak(state, today):
    last = state.streak.last_checkin
    if last is None:
        state.streak.current = 1
    elif today == last:
        pass  # already checked in today, no change
    elif today == last + 1 day:
        state.streak.current += 1
    else:
        state.streak.current = 1  # reset

    state.streak.last_checkin = today
    state.streak.best = max(state.streak.best, state.streak.current)

    streak_bonus = state.streak.current * 5
    return streak_bonus
```

---

## Progress Bar Helper

```
def progress_bar(pct, width=10):
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)
```
