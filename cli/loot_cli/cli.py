import argparse
import sys
import random

from loot_cli.data import load_ideas, filter_ideas, get_unique_values, get_all_tags, compute_stats
from loot_cli.display import (
    print_ideas, print_idea_detail, print_stats, print_market_gap,
    print_competitive_analysis, print_persona_breakdown, print_tags,
)
from loot_cli.analyze import (
    market_gap_analysis, competitive_analysis, persona_analysis, trend_analysis,
)


def cmd_search(args):
    ideas = load_ideas()
    results = filter_ideas(
        ideas,
        model=args.model,
        effort=args.effort,
        speed=args.speed,
        category=args.category,
        keyword=args.keyword,
        tags=args.tags.split(",") if args.tags else None,
        persona=args.persona,
    )
    if args.detail:
        for idea in results:
            print_idea_detail(idea)
    else:
        count = len(results) if args.all else (args.count or 20)
        print_ideas(results, count)
    return results


def cmd_analyze(args):
    ideas = load_ideas()
    if args.type == "gaps" or args.type == "market-gaps":
        analysis = market_gap_analysis(ideas)
        print_market_gap(analysis)
    elif args.type == "competitive":
        analysis = competitive_analysis(
            filter_ideas(ideas, category=args.category) if args.category else ideas
        )
        print_competitive_analysis(analysis)
    elif args.type == "persona":
        analysis = persona_analysis(ideas)
        print_persona_breakdown(analysis)
    elif args.type == "trends":
        trends = trend_analysis(ideas)
        for effort, models in trends["models_by_effort"].items():
            print(f"\n--- {effort} ---")
            for model, count in models.most_common():
                print(f"  {model:<20} {count}")
        for speed, tags in trends["tags_by_speed"].items():
            print(f"\n--- {speed} (top tags) ---")
            for tag, count in tags.most_common(10):
                print(f"  {tag:<25} {count}")
    elif args.type == "stats":
        stats = compute_stats(ideas)
        print_stats(stats)


def cmd_random(args):
    ideas = load_ideas()
    results = filter_ideas(
        ideas,
        model=args.model,
        effort=args.effort,
        speed=args.speed,
        category=args.category,
        persona=args.persona,
    )
    if not results:
        print("No ideas match your filters.")
        return
    n = min(args.count or 5, len(results))
    picked = random.sample(results, n)
    for idea in picked:
        print_idea_detail(idea)


def cmd_tags(args):
    ideas = load_ideas()
    if args.category:
        ideas = filter_ideas(ideas, category=args.category)
    tags = get_all_tags(ideas)
    if args.counts:
        from collections import Counter
        all_tags = []
        for i in ideas:
            if i.get("tags"):
                all_tags.extend(i["tags"])
        counts = Counter(all_tags)
        print_tags(tags, counts)
    else:
        print_tags(tags)


def cmd_models(args):
    ideas = load_ideas()
    if args.category:
        ideas = filter_ideas(ideas, category=args.category)
    models = get_unique_values(ideas, "model")
    print("\nAvailable business models:")
    for m in models:
        print(f"  • {m}")


def cmd_categories(args):
    ideas = load_ideas()
    cats = get_unique_values(ideas, "category")
    print(f"\nCategories ({len(cats)}):")
    for c in cats:
        print(f"  • {c}")


def cmd_export(args):
    import csv
    import json as json_mod
    import sys
    ideas = load_ideas()
    results = filter_ideas(
        ideas,
        model=args.model,
        effort=args.effort,
        speed=args.speed,
        category=args.category,
        keyword=args.keyword,
        tags=args.tags.split(",") if args.tags else None,
        persona=args.persona,
    )
    if args.count:
        results = results[:args.count]
    if args.format == "csv":
        writer = csv.writer(sys.stdout)
        writer.writerow(["id", "title", "desc", "model", "effort", "speed", "category", "persona", "tags"])
        for idea in results:
            tags = ";".join(idea.get("tags") or [])
            writer.writerow([
                idea.get("id", ""),
                idea.get("title", ""),
                idea.get("desc", ""),
                idea.get("model", ""),
                idea.get("effort", ""),
                idea.get("speed", ""),
                idea.get("category", ""),
                idea.get("persona", ""),
                tags,
            ])
    elif args.format == "json":
        out = []
        for idea in results:
            out.append({
                "id": idea.get("id"),
                "title": idea.get("title"),
                "desc": idea.get("desc"),
                "model": idea.get("model"),
                "effort": idea.get("effort"),
                "speed": idea.get("speed"),
                "category": idea.get("category"),
                "persona": idea.get("persona"),
                "tags": idea.get("tags", []),
            })
        json_mod.dump(out, sys.stdout, indent=2)
    return results


def cmd_filters(args):
    ideas = load_ideas()
    print("Available filter values:\n")
    print("Models:")
    for m in get_unique_values(ideas, "model"):
        print(f"  {m}")
    print("\nEffort:")
    for e in get_unique_values(ideas, "effort"):
        print(f"  {e}")
    print("\nSpeed:")
    for s in get_unique_values(ideas, "speed"):
        print(f"  {s}")
    print("\nCategories:")
    for c in get_unique_values(ideas, "category"):
        print(f"  {c}")
    print("\nPersonas:")
    for p in get_unique_values(ideas, "persona"):
        print(f"  {p}")
    print("\nTags (first 30):")
    tags = get_all_tags(ideas)
    for t in tags[:30]:
        print(f"  {t}")
    print(f"  ... and {len(tags)-30} more")


def main():
    parser = argparse.ArgumentParser(
        prog="loot",
        description="🔍 Loot Drop Market Researcher — Analyze 1,000 startup ideas from failed startups.",
        epilog="More info: https://github.com/loot-drop/loot-cli",
    )
    sub = parser.add_subparsers(dest="command")

    p_search = sub.add_parser("search", help="Search and filter ideas")
    p_search.add_argument("--model", help="Business model filter")
    p_search.add_argument("--effort", help="Effort filter (Weekend Project, 1-3 Months, 3-6 Months, 6+ Months)")
    p_search.add_argument("--speed", help="Monetization speed (Quick Cash, Medium Runway, Long Game)")
    p_search.add_argument("--category", help="Industry category")
    p_search.add_argument("--persona", help="Builder persona")
    p_search.add_argument("--tags", help="Comma-separated tags")
    p_search.add_argument("--keyword", "-k", help="Search keyword in title/description")
    p_search.add_argument("--count", "-n", type=int, default=20, help="Results to show (default 20)")
    p_search.add_argument("--all", "-a", action="store_true", help="Show all results")
    p_search.add_argument("--detail", "-d", action="store_true", help="Show full idea details")
    p_search.set_defaults(func=cmd_search)

    p_analyze = sub.add_parser("analyze", help="Market analysis")
    p_analyze.add_argument("type", choices=["gaps", "market-gaps", "competitive", "persona", "trends", "stats"],
                           help="Analysis type")
    p_analyze.add_argument("--category", help="Filter analysis to category (for competitive)")
    p_analyze.set_defaults(func=cmd_analyze)

    p_random = sub.add_parser("random", help="Get random ideas")
    p_random.add_argument("--count", "-n", type=int, default=5)
    p_random.add_argument("--model")
    p_random.add_argument("--effort")
    p_random.add_argument("--speed")
    p_random.add_argument("--category")
    p_random.add_argument("--persona")
    p_random.set_defaults(func=cmd_random)

    p_tags = sub.add_parser("tags", help="List available tags")
    p_tags.add_argument("--category", help="Filter tags by category")
    p_tags.add_argument("--counts", "-c", action="store_true", help="Show tag counts")
    p_tags.set_defaults(func=cmd_tags)

    p_models = sub.add_parser("models", help="List available business models")
    p_models.add_argument("--category", help="Filter by category")
    p_models.set_defaults(func=cmd_models)

    p_cats = sub.add_parser("categories", help="List available industry categories")
    p_cats.set_defaults(func=cmd_categories)

    p_export = sub.add_parser("export", help="Export results to CSV or JSON")
    p_export.add_argument("--format", choices=["csv", "json"], default="csv", help="Export format (default csv)")
    p_export.add_argument("--model", help="Business model filter")
    p_export.add_argument("--effort", help="Effort filter")
    p_export.add_argument("--speed", help="Monetization speed")
    p_export.add_argument("--category", help="Industry category")
    p_export.add_argument("--persona", help="Builder persona")
    p_export.add_argument("--tags", help="Comma-separated tags")
    p_export.add_argument("--keyword", "-k", help="Search keyword")
    p_export.add_argument("--count", "-n", type=int, help="Max results to export")
    p_export.set_defaults(func=cmd_export)

    p_filters = sub.add_parser("filters", help="Show all available filter values")
    p_filters.set_defaults(func=cmd_filters)

    args = parser.parse_args()
    if args.command:
        args.func(args)
    else:
        parser.print_help()
        print("\nTIP: Run 'loot filters' to see available filter values.")
        print("     Run 'loot search --category DevTools' to search ideas.")
        print("     Run 'loot analyze stats' for dataset overview.")
        print("     Run 'loot random' for random ideas.")
