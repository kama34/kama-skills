# Slidev Skill — Test Area

[![en](https://img.shields.io/badge/lang-English-blue)](README.md) [![ru](https://img.shields.io/badge/lang-Русский-green)](README.ru.md)

This directory serves two purposes:

1. **Skill source** — the actual skill lives in `.claude/skills/slidev/`
2. **Test playground** — run experiments, generate presentations, iterate on the skill right here

## Directory Layout

```
slidev/
  .claude/skills/slidev/     # ← Tracked by git (the skill itself)
    SKILL.md
    references/
    assets/
  .gitignore                  # ← Tracked by git
  README.md                   # ← Tracked by git
  README.ru.md                # ← Tracked by git
  my-presentation/            # ← Ignored by git (your experiments)
  another-test/               # ← Ignored by git
  notes.txt                   # ← Ignored by git
```

## How .gitignore Works Here

The `.gitignore` in this directory uses an **allowlist** pattern:

```gitignore
# Ignore everything
*

# Except these
!.gitignore
!.claude/
!.claude/**
!README.md
!README.ru.md
```

**Why?** This directory is a sandbox. You can generate presentations, install npm packages, export PDFs — none of that pollutes the repo. Only changes to the skill itself (inside `.claude/`) get committed.

## Workflow

```bash
# 1. Experiment freely — create presentations, test the skill
/slidev my-outline.md
/slidev --export png2pdf

# 2. If you improve the skill, the changes are in .claude/ — git sees them
git diff slidev/.claude/

# 3. Commit only the skill improvements
git add slidev/.claude/
git commit -m "fix(slidev): improve overlay handling for PDF export"
```

## Skill Details

See [.claude/skills/slidev/Readme.md](.claude/skills/slidev/Readme.md) for the skill's own documentation.
