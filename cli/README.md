# productfound CLI

Command-line market research tool for the Productfound dataset — 1,000 startup ideas derived from failed startup postmortems.

## Install

```bash
pip install productfound
```

Or from source:

```bash
cd cli
pip install -e .
```

## Usage

```
productfound [command] [options]
```

### Commands

| Command | Description |
|---------|-------------|
| `productfound search` | Search and filter ideas |
| `productfound analyze` | Market analysis (gaps, competitive, persona, trends, stats) |
| `productfound validate` | 4-axis stress-test with verdict |
| `productfound random` | Random idea exploration |
| `productfound tags` | Browse tag taxonomy |
| `productfound models` | List business models |
| `productfound categories` | List industry categories |
| `productfound filters` | Show available filter values |
| `productfound export` | Export dataset to JSON or CSV |

### Search filters

| Filter | Values |
|--------|--------|
| `--category` | DevTools, Health, Fintech, Ecommerce, AI-Tools, LegalTech ... (28 total) |
| `--model` | SaaS, Freemium, Marketplace, Subscription, API-First ... (18 total) |
| `--effort` | Weekend Project, 1-3 Months, 3-6 Months, 6+ Months |
| `--speed` | Quick Cash, Medium Runway, Long Game |
| `--persona` | B2B SaaS Veteran, Realistic Side-Hustler, Tech Visionary, Trend Surfer, Vibe Coder |
| `--tags` | B2B, AI-Wrapper, Bootstrap-Friendly, No-Code, Enterprise ... (142 total) |
| `--keyword` | Free text search across title and description |

### Examples

```bash
# Find underserved categories
productfound analyze gaps

# Deep-dive into a category
productfound analyze competitive --category Fintech

# Search for weekend projects
productfound search --effort "Weekend Project" --speed "Quick Cash"

# Validate an idea
productfound analyze validate --category DevTools --model SaaS

# Export for custom analysis
productfound export --format csv --output ideas.csv
```

## Data

1,000 ideas with 9-field schema: title, description, business model, effort, speed, category, persona, tags, id.

All data is bundled with the package — no API key or network connection required.

## License

MIT
