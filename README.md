<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logo.svg">
    <img src="logo.svg" alt="Loot Drop" width="90">
  </picture>
</p>

<h1 align="center">Loot Drop</h1>

<p align="center">
  <em>Market research from 1,000 failed startups.</em><br>
  Find the gap before you build. Validate before you commit.
</p>

<p align="center">
  <a href="https://github.com/jithindeepjc/loot-drop-tools/stargazers">
    <img src="https://img.shields.io/github/stars/jithindeepjc/loot-drop-tools?style=flat&label=Stars&color=7c3aed" alt="Stars">
  </a>
  <a href="https://github.com/jithindeepjc/loot-drop-tools/forks">
    <img src="https://img.shields.io/github/forks/jithindeepjc/loot-drop-tools?style=flat&label=Forks&color=7c3aed" alt="Forks">
  </a>
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-7c3aed" alt="MIT">
  </a>
  <a href="./skill/SKILL.md">
    <img src="https://img.shields.io/badge/AI_Skill-v1.3.0-7c3aed" alt="AI Skill">
  </a>
  <a href="./cli/">
    <img src="https://img.shields.io/badge/CLI-ready-7c3aed" alt="CLI">
  </a>
</p>

<p align="center">
  <a href="#why">Why</a> ·
  <a href="#demo">Demo</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#cli">CLI</a> ·
  <a href="#ai-skill">AI Skill</a> ·
  <a href="#dataset">Dataset</a>
</p>

---

## Why

90% of startups fail. Every postmortem tells the same story: a founder bet on an idea nobody validated, in a market they didn't understand, with a model that couldn't sustain them.

This is 1,000 of those ideas — extracted, categorized, tagged, and ranked. Not guesses. Not speculation. Real ideas that real people bet their careers on.

**Use this to:**

- **Find underserved markets** — categories with the fewest attempts signal the largest gaps
- **Validate your idea** — stress-test against similar bets that failed
- **Spot antipatterns** — recurring patterns that killed companies in your space
- **Ship faster** — know which model-effort-speed combos actually work

---

## Demo

### Find underserved categories

```
$ loot analyze gaps

Tier                Ideas  Categories
─────────────────  ─────  ─────────────────────────
First-mover          ≤3    LegalTech, TravelTech, CleanTech
Emerging            4-7    PropTech, CareerTech, Local Services
Competitive         8-12   Fintech, Health, EdTech, MarTech
Crowded             13+    DevTools, Ecommerce, Media, AI-Tools
```

### Stress-test your idea

```
$ loot analyze validate --category Fintech --model SaaS

Axis              Score  Signal
───────────────  ─────  ──────────────────────────────────
Gap Clarity          6  Exists but partially served
Model Fit            8  Fits buyer and effort profile
Effort Realism       4  Optimistic for solo founder
Speed vs Runway      5  Survivable with bridge round

Verdict: Validate further — Low confidence — Effort axis
```

### Explore randomly

```
$ loot random --category First-mover

  LegalFlow
  Automated contract review for SMBs
  SaaS · 3-6 months · Medium speed
  Category: LegalTech (only 2 ideas exist)
```

---

## Quick Start

```bash
pip install loot-cli

# What's underserved?
loot analyze gaps

# Search for weekend projects
loot search --effort "Weekend Project"

# Stress-test your idea
loot analyze validate --category Fintech --model SaaS
```

---

## CLI

| Command | Description |
|---------|-------------|
| `loot search` | Filter 1,000 ideas by category, model, effort, speed, tags, keyword |
| `loot analyze gaps` | Identify underserved categories |
| `loot analyze competitive` | Deep-dive into a specific category |
| `loot analyze persona` | Match ideas to builder personality |
| `loot analyze trends` | Surface model-tag-effort patterns |
| `loot analyze stats` | Full dataset distribution |
| `loot validate` | 4-axis stress-test with verdict |
| `loot random` | Explore with optional filters |
| `loot export` | Export to JSON or CSV |

```bash
loot search --category DevTools --model Freemium --effort "Weekend Project"
loot analyze competitive --category Fintech
loot export --format json --output ideas.json
```

**Full reference:** [`cli/README.md`](./cli/)

---

## AI Skill

This repository includes a self-contained skill for AI coding agents (Claude Code, OpenCode, Cursor, Copilot, Gemini CLI):

```bash
cp -r skill /path/to/your/skills/loot-drop-market-researcher
```

The skill turns any agent into a market researcher. No install required. Ask:

> *"What's the most underserved category?"*</br>
> *"Validate my idea for a fintech SaaS"*</br>
> *"Compare these three ideas"*</br>
> *"I've been building for two months — assess my market"*

Includes 7 analysis types, persona self-selector, risk flag detection, and a 4-axis scoring rubric.

**Full documentation:** [`skill/SKILL.md`](./skill/SKILL.md)

---

## Dataset

| Dimension | Details |
|-----------|---------|
| Ideas | 1,000 |
| Categories | 28 (DevTools, Health, Fintech, Ecommerce, AI-Tools, LegalTech, etc.) |
| Business models | 18 (SaaS, Marketplace, Freemium, API-First, etc.) |
| Tags | 142 |
| Builder personas | 5 |
| Effort levels | Weekend Project — 6+ Months |
| Speed tiers | Quick Cash — Long Game |
| Source | Real failed startup postmortems |

MIT license. Free. Open source.

---

## Share

<p align="center">
  <a href="https://twitter.com/intent/tweet?text=I%20analyzed%201%2C000%20failed%20startups%20so%20you%20don%27t%20have%20to.%20Meet%20Loot%20Drop%20%E2%80%94%20a%20free%20CLI%20%2B%20AI%20skill%20that%20finds%20market%20gaps%20from%20real%20postmortems.&url=https%3A%2F%2Fgithub.com%2Fjithindeepjc%2Floot-drop-tools">
    <img src="https://img.shields.io/badge/X-000000?style=flat-square&logo=x&logoColor=white" alt="X">
  </a>
  <a href="https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fgithub.com%2Fjithindeepjc%2Floot-drop-tools&t=Loot%20Drop%20%E2%80%94%20Market%20research%20from%201%2C000%20failed%20startups">
    <img src="https://img.shields.io/badge/Hacker%20News-FF6600?style=flat-square&logo=ycombinator&logoColor=white" alt="HN">
  </a>
  <a href="https://www.reddit.com/r/startups/submit?url=https%3A%2F%2Fgithub.com%2Fjithindeepjc%2Floot-drop-tools&title=Loot%20Drop%20%E2%80%94%20I%20analyzed%201%2C000%20failed%20startups%20so%20you%20can%20find%20market%20gaps%20before%20building">
    <img src="https://img.shields.io/badge/Reddit-FF4500?style=flat-square&logo=reddit&logoColor=white" alt="Reddit">
  </a>
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fgithub.com%2Fjithindeepjc%2Floot-drop-tools">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
</p>

<details>
<summary><b>Pre-written posts for X, HN, Reddit</b></summary>

<br>

**X / Twitter (thread)**

```
1/5 I analyzed 1,000 failed startups so you don't have to.
The biggest killer isn't competition. It's building in a category where nobody
failed before you. LegalTech has 2 ideas. DevTools has 14. Guess which is easier?

2/5 Business model matters more than your idea. Freemium + Quick Cash = most
survivable. Marketplace + Long Game = deadliest.

3/5 Weekend projects exist. AI-Wrapper + Chrome Extension + Freemium = ship
in 48 hours, revenue in 2 weeks.

4/5 The 7 antipatterns: Cold Start, VC+Bootstrap conflict, Marketplace-weekend
mismatch, regulatory blind spots, high churn with no lock-in, building for
"everyone", speed mismatch.

5/5 Full dataset + CLI + AI skill — free, open source.
→ github.com/jithindeepjc/loot-drop-tools
```

**Hacker News / Product Hunt**

```
Title: Loot Drop — Market research from 1,000 failed startups

I extracted 1,000 startup ideas from real failed postmortems into a searchable
dataset tagged by category, business model, effort, speed, and risk flags.

Includes a Python CLI (pip install loot-cli) and an AI skill for Claude Code.
Seven analysis types: gaps, competitive, persona, trends, search, validate, score.

Most "startup ideas" lists are guesses. This is built from actual failures.
```

**Reddit (r/startups)**

```
Title: I analyzed 1,000 failed startups and built a free tool to find market gaps

1,000 ideas mapped to 28 categories, 18 business models, 142 tags. Derived from
real failed startup postmortems — execution failures, not speculation.

The dataset reveals: which categories have the least competition, which business
models survive longest, which effort-speed combos produce revenue, and the 7
antipatterns in every failure cluster.

Free CLI + AI skill. → github.com/jithindeepjc/loot-drop-tools
```

</details>

---

<p align="center">
  <a href="https://github.com/jithindeepjc/loot-drop-tools">GitHub</a> ·
  <a href="https://github.com/jithindeepjc/loot-drop-tools/issues">Issues</a> ·
  <a href="https://github.com/jithindeepjc/loot-drop-tools/blob/master/LICENSE">MIT License</a>
</p>
