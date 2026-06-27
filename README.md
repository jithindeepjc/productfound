<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logo.svg">
    <img src="logo.svg" alt="Loot Drop" width="120">
  </picture>
</p>

<h1 align="center">Loot Drop Tools</h1>

<p align="center"><b>Market research toolkit</b> powered by the Loot Drop startup failure graveyard — 1,000+ ideas extracted from real failed startup postmortems.</p>

## What's Inside

### [`cli/`](./cli) — `loot` CLI Tool

A Python CLI for market researchers, founders, and builders to search, filter, and analyze startup ideas.

```bash
pip install loot-cli
```

**Commands:**

| Command | Description |
|---|---|
| `loot search` | Search/filter 1,000 ideas by model, effort, speed, category, persona, tags, keyword |
| `loot analyze` | Market analysis: gaps, competitive landscape, persona breakdowns, trends, stats |
| `loot random` | Get random ideas (optionally filtered) |
| `loot tags` | Browse tag taxonomy with counts |
| `loot models` | List business models |
| `loot categories` | List industry categories |
| `loot filters` | Show all available filter values |

### [`skill/`](./skill) — OpenCode Skill

An OpenCode/Claude Code compatible skill that turns any coding agent into a market researcher. Installs as a skill that the agent auto-discovers when you ask market research questions.

## Installation

### CLI Tool

```bash
# From PyPI
pip install loot-cli

# Or from source
cd cli && pip install -e .
```

### OpenCode Skill

```bash
cp -r skill /path/to/your/skills/loot-drop-market-researcher
```

Or reference in CLAUDE.md / AGENTS.md.

## Data

1,000 ideas with 9-field schema:
- `title`, `desc` — idea and description
- `model` — business model (18 types: Freemium, Subscription, SaaS, Marketplace, etc.)
- `effort` — build effort (Weekend Project, 1-3 Months, 3-6 Months, 6+ Months)
- `speed` — monetization speed (Quick Cash, Medium Runway, Long Game)
- `category` — industry (28 categories: DevTools, Health, Fintech, Ecommerce, etc.)
- `persona` — target builder persona (5 types)
- `tags` — 142 descriptive tags (B2B, AI-Wrapper, Bootstrap-Friendly, No-Code, etc.)

## License

MIT
