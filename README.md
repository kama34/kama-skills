# Kama Skills (Claude Code Skills)

[![en](https://img.shields.io/badge/lang-English-blue)](README.md) [![ru](https://img.shields.io/badge/lang-Русский-green)](README.ru.md)

Community-driven collection of **skills** for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — drop-in prompt modules that give Claude new capabilities.

> A skill is a markdown file that teaches Claude Code how to do something it couldn't do before: generate presentations, scaffold projects, run complex workflows, and more.

## Available Skills

| Skill | Description | Complexity |
|-------|-------------|------------|
| **[slidev](./skills/slidev/)** | Generate polished Slidev presentations from text outlines. Supports presets, auto-image placement, visual QA, PDF/PNG export, and a self-improving learning loop. | Advanced |

## What Are Skills?

Skills are markdown instruction files (`.md`) that live in `.claude/skills/` inside your project. When invoked, Claude reads the skill and follows its instructions precisely — like giving an expert a detailed playbook.

Unlike simple prompts, skills can:
- Define multi-step procedures with decision trees
- Reference other files (design principles, syntax guides, presets)
- Include reusable code templates and patterns
- Chain subcommands (`--edit`, `--export`, `--dev`, `--learn`)
- Self-improve through feedback loops

## Quick Start

### 1. Copy a skill into your project

```bash
# Create the skills directory
mkdir -p .claude/skills

# Copy the skill you want (e.g., slidev)
cp -r path/to/claude-code-skills/skills/slidev .claude/skills/
```

### 2. Register the skill

Add to your `.claude/settings.json`:

```json
{
  "skills": {
    "slidev": {
      "path": ".claude/skills/slidev/SKILL.md",
      "description": "Generate Slidev presentations from outlines",
      "trigger": "/slidev"
    }
  }
}
```

### 3. Use it

```
/slidev my-outline.md
/slidev --preset corporate my-outline.md
/slidev --export png2pdf
/slidev --edit "make it darker"
```

## Skill Structure

Each skill follows this directory layout:

```
skills/
  my-skill/
    SKILL.md              # Main instruction file (entry point)
    references/           # Supporting docs, syntax guides, examples
      some-guide.md
      patterns.md
    assets/               # Templates, demo files
      demo-outline.md
```

**`SKILL.md`** is the core — it contains the full procedure Claude follows. Think of it as a detailed SOP (Standard Operating Procedure) written for an AI that can execute code, read files, and make decisions.

## Contributing

We welcome contributions! Here's how you can help:

### Add a New Skill

1. Fork the repo
2. Create `skills/your-skill-name/SKILL.md`
3. Add references and assets as needed
4. Test it thoroughly with Claude Code
5. Submit a PR with:
   - A clear description of what the skill does
   - Example usage and output
   - Any dependencies (npm packages, Python libs, etc.)

### Improve an Existing Skill

Found a bug? Have a better approach? Skills are living documents:

1. Fork the repo
2. Edit the skill's `SKILL.md` or reference files
3. Describe what you changed and why in the PR
4. Bonus: include before/after examples

### Skill Quality Guidelines

A good skill should be:

- **Specific** — solves a concrete problem, not a vague one
- **Self-contained** — all instructions in one place, no implicit knowledge
- **Testable** — produces observable output that can be verified
- **Documented** — explains its subcommands, options, and edge cases
- **Robust** — handles errors, validates inputs, has fallback strategies

## Writing Your Own Skill

### Start Simple

```markdown
# My Skill

You do X when the user asks for Y.

## Procedure

1. Read the input
2. Do the thing
3. Output the result
```

### Then Iterate

The best skills are built through real usage. Use Claude Code's `--learn` pattern:

1. Write a basic skill
2. Use it on real tasks
3. Note what breaks or produces poor results
4. Add rules to handle those cases
5. Repeat

### Key Principles

- **Be explicit** — Claude follows instructions literally. "Make it look good" fails; "Use 3+ type scales, accent hierarchy with 3 opacity levels, and alternate dense/breathing slides" works.
- **Include examples** — Show the exact code/output you expect, not just descriptions.
- **Add guardrails** — Mark critical rules with `**CRITICAL**` or `MUST`. Claude respects emphasis hierarchy.
- **Reference files** — Split complex skills into a main SKILL.md + reference docs. Keeps the main file focused.
- **Test edge cases** — Run the skill 10+ times with varied inputs. Every failure = a new rule.

## FAQ

**Q: How is this different from system prompts or CLAUDE.md?**
Skills are invocable on demand (via `/command`), while CLAUDE.md is always loaded. Use CLAUDE.md for project-wide conventions, skills for specific workflows.

**Q: Can skills call other skills?**
Not directly, but a skill can instruct Claude to read another skill's files.

**Q: What's the max skill size?**
No hard limit, but keep SKILL.md under ~4000 lines. Split into references if larger.

**Q: Do skills work with other AI coding tools?**
Skills are designed for Claude Code but the concept (structured markdown instructions) works with any AI that reads files. The tool-specific parts (Bash, Read, Edit, etc.) would need adaptation.

## License

MIT — use, modify, and share freely.
