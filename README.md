<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logo.svg">
    <img src="logo.svg" alt="Loot Drop" width="100">
  </picture>
</p>

<h1 align="center">Loot Drop</h1>

<p align="center">
  <b>1,000 startup ideas.</b> Derived from real failed postmortems.<br>
  Find the gap before you build. Validate before you commit.
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
    <img src="https://img.shields.io/badge/🧠%20AI%20Skill-ready-7c3aed" alt="AI Skill">
  </a>
</p>

<p align="center">
  <a href="#-why-this-exists">Why</a> •
  <a href="#-quick-demo">Demo</a> •
  <a href="#-cli">CLI</a> •
  <a href="#-ai-agent-skill">AI Skill</a> •
  <a href="#-share">Share</a>
</p>

---

## 💀 Why This Exists

**90% of startups fail. That's 9,000 dead companies for every unicorn.**

I scraped their postmortems, extracted the ideas they bet on, and organized 1,000 of them into a searchable dataset. Every idea comes from a real failure — which means every idea comes with a warning label.

**This is not a "startup ideas" list. It's a graveyard map.** The gaps are where nobody tried, the clusters are where everyone died trying, and the patterns are what killed them.

Use it to:
- **Find underserved categories** before they get crowded
- **Validate your idea** against 1,000 similar bets that failed
- **Spot antipatterns** that killed companies in your space
- **Ship faster** by knowing which effort-model-speed combos actually work

---

## ⚡ Quick Demo

### Find your underserved category

```
$ loot analyze gaps
┌─────────────────────┬──────┬──────────────────────────────┐
│ Tier                │ Count │ Categories                   │
├─────────────────────┼──────┼──────────────────────────────┤
│ 🟢 First-mover (≤3) │    4 │ LegalTech, TravelTech, ...    │
│ 🟡 Emerging (4-7)   │    8 │ PropTech, CleanTech, ...      │
│ 🟠 Competitive (8-12)│   10 │ Fintech, Health, ...          │
│ 🔴 Crowded (13+)     │    6 │ DevTools, Ecommerce, ...     │
└─────────────────────┴──────┴──────────────────────────────┘
```

### Stress-test your idea

```
$ loot analyze validate --category Fintech --model SaaS
┌────────────────┬────┬─────────────────────────────────┐
│ Axis           │ ║  │ Signal                          │
├────────────────┼────┼─────────────────────────────────┤
│ Gap Clarity    │  6 │ Exists but partially served      │
│ Model Fit      │  8 │ Fits buyer and effort profile    │
│ Effort Realism │  4 │ Optimistic for solo founder      │
│ Speed/Runway   │  5 │ Survivable with bridge round     │
└────────────────┴────┴─────────────────────────────────┘
Verdict: Validate further — Low confidence — Effort axis
```

### Get a random idea to explore

```
$ loot random --category First-mover
╔══════════════════════════════════════════════════╗
║  LegalFlow                                        ║
║  Automated contract review for SMBs              ║
║  Model: SaaS · Effort: 3-6 Months · Speed: Medium║
║  Category: LegalTech (only 2 ideas exist)         ║
╚══════════════════════════════════════════════════╝
```

---

## 🛠️ CLI

```bash
pip install loot-cli
```

| Command | What it does |
|---------|-------------|
| `loot search` | Filter 1,000 ideas by category, model, effort, speed, tags |
| `loot analyze` | Market gaps, competitive deep-dives, persona fit, trends |
| `loot validate` | 4-axis stress-test with verdict |
| `loot random` | Explore with optional filters |
| `loot export` | JSON/CSV export for your own analysis |

**Full docs:** [CLI README](./cli/)

---

## 🧠 AI Agent Skill

This repo includes an OpenCode/Claude Code compatible skill that turns any AI coding agent into a market researcher:

```bash
cp -r skill /path/to/your/skills/loot-drop-market-researcher
```

Then ask your agent: *"What's the most underserved category?"* or *"Validate my idea for a fintech SaaS"*

The skill runs all 7 analysis types — gaps, competitive, persona, trends, search, validate, score — directly through the agent. No CLI required.

**Full skill docs:** [SKILL.md](./skill/SKILL.md)

---

## 📊 By the Numbers

| Dimension | Count |
|-----------|-------|
| Ideas | 1,000 |
| Categories | 28 (DevTools, Fintech, Health, AI-Tools, LegalTech, etc.) |
| Business models | 18 (SaaS, Marketplace, Freemium, API-First, etc.) |
| Tags | 142 |
| Builder personas | 5 |
| Effort levels | 4 (Weekend → 6+ Months) |
| Speed tiers | 3 (Quick Cash → Long Game) |
| Source | Real failed startup postmortems |

**Free. Open source. MIT.**

---

## 📢 Share

If this is useful, share it with someone who's about to build in a crowded market:

<p align="center">
  <a href="https://twitter.com/intent/tweet?text=I%20analyzed%201%2C000%20failed%20startups%20so%20you%20don%27t%20have%20to.%20Meet%20Loot%20Drop%20%E2%80%94%20a%20free%20CLI%20%2B%20AI%20skill%20that%20finds%20market%20gaps%20from%20real%20postmortems.%20%E2%9C%94%EF%B8%8F%20Validate%20before%20you%20build.&url=https%3A%2F%2Fgithub.com%2Fjithindeepjc%2Floot-drop-tools">
    <img src="https://img.shields.io/badge/Tweet-000?logo=x&style=for-the-badge" alt="Share on X">
  </a>
  <a href="https://www.producthunt.com/posts/loot-drop?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-loot-drop" target="_blank">
    <img src="https://img.shields.io/badge/Upvote%20on%20Product%20Hunt-da552f?logo=producthunt&style=for-the-badge" alt="Product Hunt">
  </a>
  <a href="https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fgithub.com%2Fjithindeepjc%2Floot-drop-tools&t=Loot%20Drop%20%E2%80%94%20Market%20research%20from%201%2C000%20failed%20startups">
    <img src="https://img.shields.io/badge/Post%20on%20HN-f60?logo=ycombinator&style=for-the-badge" alt="Hacker News">
  </a>
  <a href="https://www.reddit.com/r/startups/submit?url=https%3A%2F%2Fgithub.com%2Fjithindeepjc%2Floot-drop-tools&title=Loot%20Drop%20%E2%80%94%20I%20analyzed%201%2C000%20failed%20startups%20so%20you%20can%20find%20market%20gaps%20before%20building">
    <img src="https://img.shields.io/badge/Share%20on%20Reddit-ff4500?logo=reddit&style=for-the-badge" alt="Reddit">
  </a>
</p>

### Pre-written posts — copy, paste, ship

<details>
<summary><b>🐦 Twitter/X thread</b> (tweet 1/5)</summary>

```
I analyzed 1,000 failed startups so you don't have to.

Here's what kills companies — and the gaps you should build in instead. 🧵

1/5 The biggest killer isn't competition. It's building in a category where nobody failed before you. LegalTech has only 2 ideas in the dataset. DevTools has 14. Guess which one is easier to enter?

2/5 Business model matters more than your idea. In 28 categories, Freemium + Quick Cash is the most survivable combo. Marketplace + Long Game is the deadliest. Pick your model like your life depends on it.

3/5 "Weekend project" ideas exist. They're just not where you're looking. AI-Wrapper + Chrome Extension + Freemium = shipped in 48 hours, revenue in 2 weeks. I found 12 of these in the data.

4/5 The 7 antipatterns that keep appearing:
• Cold Start (needs users before it's useful)
• VC+Bootstrap (pick one)
• Marketplace built in a weekend
• Regulatory blind spot
• High churn with no lock-in
• Building for "everyone"
• Speed mismatch (Long Game, zero funding)

5/5 Full dataset + CLI + AI skill — free, open source, MIT.

→ github.com/jithindeepjc/loot-drop-tools

Found this useful? Star it so the next builder finds it too. ⭐
```
</details>

<details>
<summary><b>📰 Show HN / Product Hunt</b></summary>

```
Title: Loot Drop — Market research from 1,000 failed startups

I scraped failed startup postmortems and extracted 1,000 ideas into a searchable
dataset. Every idea is tagged by category, business model, build effort, monetization
speed, and risk flags.

Comes with:
• A Python CLI (pip install loot-cli)
• An AI skill for Claude Code / OpenCode
• 7 analysis types: gaps, competitive, persona, trends, search, validate, score

Why this exists: Most "startup ideas" lists are guesses from people who've never
started a company. This one is derived from people who did — and failed. The patterns
in the failure data tell you more about what works than any success story.

Looking for feedback on:
1. Is the CLI useful in your workflow?
2. What analysis would you add?
3. Would you pay for a hosted version?
```
</details>

<details>
<summary><b>💬 Reddit post (r/startups)</b></summary>

```
Title: I analyzed 1,000 failed startups and built a free tool to find market gaps

I spent time going through failed startup postmortems and extracting the actual ideas
these companies bet on. The result: 1,000 ideas mapped to 28 categories, 18 business
models, and tagged with 142 attributes.

The dataset reveals patterns you won't find in success stories:
- Which categories have the least competition (and why)
- Which business models survive longest in each category
- Which effort-speed combos actually produce revenue
- The 7 antipatterns that show up in every failure cluster

I built a free CLI and an AI skill so anyone can query this without writing code.

Would love feedback from founders who've been through the trenches.

→ github.com/jithindeepjc/loot-drop-tools
```
</details>

---

## 🚀 Launch Kit

Ready to launch? Here's what's prepped:

| Asset | Status | Action |
|-------|--------|--------|
| GitHub repo | ✅ Live | Star, fork, share |
| README | ✅ Optimized | Already done |
| Share buttons | ✅ Added | Tweet, PH, HN, Reddit |
| Pre-written posts | ✅ 3 platforms | Copy from above |
| CLI | ✅ Working | `pip install loot-cli` |
| AI Skill | ✅ v1.3.0 | [SKILL.md](./skill/SKILL.md) |
| Product Hunt page | 🔲 Create | [ph.new](https://www.producthunt.com/posts/new) |
| Demo GIF | 🔲 Record | `terminalizer` or `asciinema` recommended |

**Product Hunt checklist:**
1. Go to [ph.new](https://www.producthunt.com/posts/new)
2. Title: **Loot Drop — Market research from 1,000 failed startups**
3. Tagline: *Find the gap before you build. Validate before you commit.*
4. Use the Show HN text above as the description
5. Upload a CLI screencast GIF (record with `asciinema`)

---

## 📜 License

MIT — use it, ship it, build on it.

<p align="center">
  <b>Star ⭐ this repo if you found it useful — it helps the next founder find it.</b>
</p>
