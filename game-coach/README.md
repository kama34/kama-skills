# Game Coach

[![en](https://img.shields.io/badge/lang-English-blue)](README.md) [![ru](https://img.shields.io/badge/lang-Русский-green)](README.ru.md)

Gamified goal coaching system that turns goal management into a game with XP, levels (10), badges (15), quests, and streaks. Built on **Octalysis** (White Hat motivational drivers) + **GROW/WOOP** coaching methodologies.

## What It Does

- **Daily check-in** (5 min) — streak tracking, XP rewards, daily habit reset, focus for the day
- **Mentor session** — deep GROW+WOOP coaching for goal clarity and planning (supports daily habit creation)
- **Dashboard** — full progress visualization with goals, daily habits, quests, badges
- **Status** — one-line quick status
- **Analyze** — retrospective activity analysis over N days (7 metrics)

## Requirements

- **Google Tasks MCP** — for task management (goals stored as dedicated task lists)
- Claude Code with MCP support

## Installation

```bash
# Copy into your project
cp -r game-coach/.claude/skills/game-coach .claude/skills/

# Create state directory
mkdir -p .claude/agent-memory/game-coach

# Initialize state
cp .claude/skills/game-coach/assets/state-template.json .claude/agent-memory/game-coach/state.json
```

Register in `.claude/settings.json`:

```json
{
  "skills": {
    "game-coach": {
      "path": ".claude/skills/game-coach/SKILL.md",
      "description": "Gamified goal coaching with XP, levels, badges, and quests",
      "trigger": "/game"
    }
  }
}
```

## Usage

```
/game checkin     # Daily 5-min check-in (+25 XP + streak bonus)
/game mentor      # GROW+WOOP deep coaching session (+75 XP)
/game dashboard   # Full progress dashboard
/game status      # Quick one-line status
/game --analyze=7 # Retrospective analysis (last 7 days)
/game --help      # Full help
```

## XP System

| Action | XP |
|--------|-----|
| Daily checkin | 25 |
| Streak bonus (per day) | day x 5 |
| P0 task completed | 80 |
| P1 task completed | 50 |
| P2 task completed | 30 |
| P3 task completed | 15 |
| Mentor session | 75 |
| Quest completion | 100-300 |
| 🔄 Daily habit (at checkin) | by priority (P0=80..P3=15) |

**🔄 Daily tasks** are recurring habits that reset every checkin. XP is awarded for yesterday's completions. Each daily task tracks its own streak.

## 10 Levels

| Lvl | Title | XP | Unlock |
|-----|-------|----|--------|
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

## Methodologies

- **GROW**: Goal > Reality > Options > Will — structured coaching
- **WOOP**: Wish > Outcome > Obstacle > Plan — evidence-based goal achievement
- **Octalysis White Hat**: motivation through meaning, accomplishment, and empowerment (no pressure/FOMO)

## License

MIT
