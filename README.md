<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logo.svg">
    <img src="logo.svg" alt="Loot Drop" width="110">
  </picture>
</p>

<h1 align="center">Loot Drop</h1>

<p align="center">
  <b>Market research from 1,000 failed startups.</b><br>
  <i>Find the gap before you build. Validate before you commit.</i>
</p>

<p align="center">
  <a href="https://github.com/jithindeepjc/loot-drop-tools/stargazers">
    <img src="https://img.shields.io/github/stars/jithindeepjc/loot-drop-tools?style=flat&label=★%20Stars&color=7c3aed" alt="Stars">
  </a>
  <a href="https://github.com/jithindeepjc/loot-drop-tools/forks">
    <img src="https://img.shields.io/github/forks/jithindeepjc/loot-drop-tools?style=flat&label=⑂%20Forks&color=7c3aed" alt="Forks">
  </a>
  <a href="https://github.com/jithindeepjc/loot-drop-tools/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-7c3aed" alt="MIT">
  </a>
  <a href="./skill/SKILL.md">
    <img src="https://img.shields.io/badge/🧠_AI_Skill-v1.3.0-7c3aed" alt="AI Skill">
  </a>
  <a href="./cli/">
    <img src="https://img.shields.io/badge/🛠_CLI-ready-7c3aed" alt="CLI">
  </a>
</p>

<br>

```



                                                                    ██
          ██████                                                    ██
          ██░░░░██                                                  ██
          ██░░░░░░░░████████  ██████  ██    ██  ████████  ████████  ████████
          ██░░░░░░████░░░░████░░░░████░░██  ██░░██░░░░░░████░░░░████░░░░██
          ██░░░░░░██░░░░░░░░██░░░░██░░░░████░░░░████████  ██████████  ██
          ██░░░░░░██░░░░░░░░████████  ██░░░░████░░░░░░░░  ██░░░░░░░░  ██
          ██░░░░░░░░████░░████░░░░██████░░░░██░░████████  ██░░░░░░░░  ██
          ░░░████████░░████░░  ░░░░████░░░░██░░░░░░░░░░██░░██░░░░░░░░░░██
            ░░░░░░    ░░░░      ░░░░  ░░░░    ░░░░░░░░  ░░░░  ░░░░░░  ░░░░


```

<p align="center">
  <b>A CLI</b> <code>·</code> <b>An AI Skill</b> <code>·</code> <b>1,000 Startup Ideas</b>
</p>

<p align="center">
  <a href="#-the-why">Why</a> •
  <a href="#-see-it-in-action">Demo</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-cli-reference">CLI</a> •
  <a href="#-ai-skill">AI Skill</a> •
  <a href="#-the-dataset">Data</a> •
  <a href="#-share">Share</a>
</p>

<br>

---

## 💀 The Why

**90% of startups fail.**

Every postmortem tells the same story: a founder bet on an idea nobody validated, in a market they didn't understand, with a model that couldn't sustain them.

This is 1,000 of those ideas — extracted, categorized, tagged, and ranked. Not guesses. Not "what if." Real ideas that real people bet their careers on and lost.

**This is not a startup ideas list. It's a graveyard map.**

| Use case | What you get |
|----------|-------------|
| 🎯 Find underserved markets | Categories with ≤3 ideas = first-mover territory |
| 🛡️ Validate your idea | 6-step stress-test against similar failures |
| 🧠 Spot antipatterns | 7 recurring patterns that killed companies |
| ⚡ Ship faster | Know which model+effort combos actually work |
| 🎲 Explore randomly | Surface ideas from categories you'd never consider |

<br>

---

## ⚡ See It in Action

### Find gaps before anyone else

```ansi
[35m$ loot analyze gaps[0m

┌──────────────────────────┬───────────┬──────────────────────────────────────┐
│ [32m Tier                  [0m │ [32m Ideas    [0m │ [32m Categories                         [0m │
├──────────────────────────┼───────────┼──────────────────────────────────────┤
│ 🛜 First-mover           │    ≤3     │ LegalTech, TravelTech, CleanTech      │
│ 🟡 Emerging              │    4-7    │ PropTech, CareerTech, Local Services  │
│ 🟠 Competitive           │    8-12   │ Fintech, Health, EdTech, MarTech     │
│ 🔴 Crowded               │   13+     │ DevTools, Ecommerce, Media, AI-Tools │
└──────────────────────────┴───────────┴──────────────────────────────────────┘

[2mContrarian take: DevTools is crowded, but no idea targets CI pipeline audits.
That's a wedge. (Tag: Enterprise, Model: SaaS, Effort: 3-6mo)[0m
```

### Stress-test your idea in 6 steps

```ansi
[35m$ loot analyze validate --category Fintech --model SaaS[0m

┌──────────────────┬────┬──────────────────────────────────────┐
│ [36m Axis             [0m │ [33m ║  [0m │ [36m Signal                               [0m │
├──────────────────┼────┼──────────────────────────────────────┤
│ Gap Clarity      │  6 │ Exists but partially served           │
│ Model Fit        │  8 │ Fits buyer and effort profile         │
│ Effort Realism   │  4 │ Optimistic for solo founder           │
│ Speed vs Runway  │  5 │ Survivable with bridge round          │
└──────────────────┴────┴──────────────────────────────────────┘

[33mVerdict: Validate further — Low confidence — Effort axis drove it
→ Ship a manual version first. Validate demand before building automation.[0m
```

### Let chance decide

```ansi
[35m$ loot random --category First-mover[0m

╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   [1mLegalFlow[0m                                                ║
║   Automated contract review for SMBs                         ║
║                                                              ║
║   [2mModel:[0m SaaS       [2mEffort:[0m 3-6 months   [2mSpeed:[0m Medium     ║
║   [2mCategory:[0m LegalTech  [2m(only 2 ideas exist)[0m                ║
║   [2mTags:[0m B2B · Bootstrap-Friendly · Low Churn                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

<br>

---

## 🚀 Quick Start

```bash
# Install
pip install loot-cli

# See what's possible
loot --help

# Your first command — what's underserved?
loot analyze gaps

# Get a random idea
loot random

# Search for weekend projects
loot search --effort "Weekend Project" --speed "Quick Cash"
```

> **No Python?** Use the [AI Skill](#-ai-skill) instead — it runs through any coding agent without installing anything.

<br>

---

## 🛠 CLI Reference

| Command | Action | Powered by |
|---------|--------|------------|
| `loot search` | Filter 1,000 ideas by 8 dimensions | `data.py` |
| `loot analyze gaps` | Find underserved categories | `analyze.py` |
| `loot analyze competitive` | Deep-dive into a category | `analyze.py` |
| `loot analyze persona` | Match ideas to builder type | `analyze.py` |
| `loot analyze trends` | Surface model+tag patterns | `analyze.py` |
| `loot analyze stats` | Dataset distribution | `analyze.py` |
| `loot validate` | 4-axis stress-test + verdict | `analyze.py` |
| `loot random` | Explore with filters | `data.py` |
| `loot export` | JSON / CSV export | `data.py` |

```bash
# Advanced usage
loot search --category DevTools --model Freemium --effort "Weekend Project"
loot analyze competitive --category Fintech
loot export --format json --output ideas.json
```

**→ Full CLI docs:** [`./cli/`](./cli/)

<br>

---

## 🧠 AI Skill

This repo includes a self-contained skill for **OpenCode, Claude Code, Cursor, Copilot, Gemini CLI, and any AI coding agent** that supports skills.

No CLI. No install. The agent becomes a market researcher.

```bash
cp -r skill /path/to/your/skills/loot-drop-market-researcher
```

Then just ask:

> *"What's the most underserved category?"*<br>
> *"Validate my idea for a fintech SaaS"*<br>
> *"Find a wedge in DevTools"*<br>
> *"Compare these 3 ideas"*<br>
> *"I've been building for 2 months — assess my market"*<br>
> *"Show me bootstrap-friendly weekend projects"*<br>

**→ Skill docs:** [`./skill/SKILL.md`](./skill/SKILL.md) — 7 analysis types, persona self-selector, risk flags, scoring rubric

<br>

---

## 📊 The Dataset

```


                        ╔════════════╗
                        ║  1,000     ║
                        ║  IDEAS     ║
                        ╚════════════╝
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   ╔════════════╗      ╔════════════╗      ╔════════════╗
   ║  28        ║      ║  18        ║      ║  142       ║
   ║ CATEGORIES ║      ║  MODELS    ║      ║  TAGS      ║
   ╚════════════╝      ╚════════════╝      ╚════════════╝


```

| Dimension | Details |
|-----------|---------|
| **Categories** | DevTools, Health, Fintech, CyberSec, Ecommerce, EdTech, Media, CleanTech, HRTech, LegalTech, Logistics, PropTech, MarTech, Data-Service, Productivity, Gaming, Design, Creative, Healthcare, Crypto, Travel, Wellness, CareerTech, AI-Tools, TravelTech, Lifestyle, Local Services |
| **Models** | Freemium, Subscription, SaaS, Marketplace, Agency, One-time, Usage-based, Open Source, Affiliate, Vertical SaaS, API-First, Shopify App, Chrome Extension, Licensing, Job Board, App Purchase |
| **Effort** | Weekend Project → 1-3 Months → 3-6 Months → 6+ Months |
| **Speed** | Quick Cash → Medium Runway → Long Game |
| **Personas** | B2B SaaS Veteran · Realistic Side-Hustler · Tech Visionary · Trend Surfer · Vibe Coder |
| **Source** | Real failed startup postmortems — execution failures, not market guesses |

**Free. Open source. MIT.** Use it, ship it, build on it.

<br>

---

## 📢 Spread the Word

One share = one founder who builds in a gap instead of a graveyard.

<p align="center">
  <a href="https://twitter.com/intent/tweet?text=I%20analyzed%201%2C000%20failed%20startups%20so%20you%20don%27t%20have%20to.%20Meet%20Loot%20Drop%20%E2%80%94%20a%20free%20CLI%20%2B%20AI%20skill%20that%20finds%20market%20gaps%20from%20real%20postmortems.%20%E2%9C%94%EF%B8%8F%20Validate%20before%20you%20build.&url=https%3A%2F%2Fgithub.com%2Fjithindeepjc%2Floot-drop-tools">
    <img src="https://img.shields.io/badge/Share_on_X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X">
  </a>
  <a href="https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fgithub.com%2Fjithindeepjc%2Floot-drop-tools&t=Loot%20Drop%20%E2%80%94%20Market%20research%20from%201%2C000%20failed%20startups">
    <img src="https://img.shields.io/badge/Post_on_HN-FF6600?style=for-the-badge&logo=ycombinator&logoColor=white" alt="HN">
  </a>
  <a href="https://www.reddit.com/r/startups/submit?url=https%3A%2F%2Fgithub.com%2Fjithindeepjc%2Floot-drop-tools&title=Loot%20Drop%20%E2%80%94%20I%20analyzed%201%2C000%20failed%20startups%20so%20you%20can%20find%20market%20gaps%20before%20building">
    <img src="https://img.shields.io/badge/Share_on_Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white" alt="Reddit">
  </a>
  <a href="https://www.producthunt.com/posts/loot-drop?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-loot-drop">
    <img src="https://img.shields.io/badge/Upvote_on_PH-DA552F?style=for-the-badge&logo=producthunt&logoColor=white" alt="PH">
  </a>
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fgithub.com%2Fjithindeepjc%2Floot-drop-tools">
    <img src="https://img.shields.io/badge/Share_on_LI-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
</p>

<details>
<summary><b>📋 Copy-paste posts for every platform</b></summary>

<br>

**🐦 Twitter/X (5-part thread)**
```
1/5 I analyzed 1,000 failed startups so you don't have to.
The biggest killer isn't competition. It's building in a category where nobody
failed before you. LegalTech has 2 ideas. DevTools has 14. Guess which is easier?

2/5 Business model matters more than your idea. Freemium + Quick Cash = most
survivable. Marketplace + Long Game = deadliest. Pick your model like your life
depends on it.

3/5 Weekend projects exist. AI-Wrapper + Chrome Extension + Freemium = ship
in 48 hours, revenue in 2 weeks. Found 12 of these in the data.

4/5 The 7 antipatterns that keep appearing: Cold Start, VC+Bootstrap (pick one),
Marketplace built in a weekend, Regulatory blind spot, High churn with no lock-in,
Building for "everyone", Speed mismatch (Long Game, zero funding).

5/5 Full dataset + CLI + AI skill — free, open source.
→ github.com/jithindeepjc/loot-drop-tools
Star it so the next founder finds it. ⭐
```

**📰 Show HN / Product Hunt**
```
Title: Loot Drop — Market research from 1,000 failed startups

I scraped failed startup postmortems and extracted 1,000 ideas into a searchable
dataset. Every idea is tagged by category, business model, build effort, monetization
speed, and risk flags.

Comes with:
• A Python CLI (pip install loot-cli)
• An AI skill for Claude Code / OpenCode
• 7 analysis types: gaps, competitive, persona, trends, search, validate, score

Most "startup ideas" lists are guesses from people who've never started a company.
This one is derived from people who did — and failed.
```

**💬 Reddit (r/startups)**
```
Title: I analyzed 1,000 failed startups and built a free tool to find market gaps

I went through failed startup postmortems and extracted the ideas these companies
bet on. 1,000 ideas mapped to 28 categories, 18 business models, 142 tags.

The dataset reveals patterns you won't find in success stories:
• Which categories have the least competition
• Which business models survive longest in each category
• Which effort-speed combos actually produce revenue
• The 7 antipatterns in every failure cluster

Free CLI + AI skill. → github.com/jithindeepjc/loot-drop-tools
```

</details>

<br>

---

## 🚀 Launch Checklist

| Step | Action | Time |
|------|--------|------|
| ✅ | Repo public | Done |
| ✅ | README optimized | Done |
| ✅ | Share buttons | Done |
| ✅ | Pre-written posts | Done |
| ✅ | Logo + banner | Done |
| 🔲 | Post Twitter/X thread | 5 min |
| 🔲 | Submit to Show HN | 5 min |
| 🔲 | Post on r/startups | 3 min |
| 🔲 | Create Product Hunt → [ph.new](https://www.producthunt.com/posts/new) | 15 min |
| 🔲 | Record terminal demo with `asciinema` | 10 min |
| 🔲 | Post on LinkedIn | 3 min |

<br>

---

<p align="center">
  <b>Star ⭐ this repo.</b> One star = one founder who finds an underserved market instead of building in a graveyard.
</p>

<p align="center">
  <sub>MIT · Open source · Built from failures · For builders who want to win</sub>
</p>
