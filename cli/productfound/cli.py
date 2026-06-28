import argparse
import sys
import random

from productfound.data import load_ideas, filter_ideas, get_unique_values, get_all_tags, compute_stats
from productfound.display import (
    print_ideas, print_idea_detail, print_stats, print_market_gap,
    print_competitive_analysis, print_persona_breakdown, print_tags,
    print_assessment, print_comparison,
)
from productfound.analyze import (
    market_gap_analysis, competitive_analysis, persona_analysis, trend_analysis,
    compare_ideas, assess_product,
)
from productfound.analyze_postmortems import (
    get_all as get_all_pm,
    search as pm_search,
    region_summary as pm_region_summary,
    failure_reasons as pm_failure_reasons,
    category_breakdown as pm_category_breakdown,
    compare_regions as pm_compare_regions,
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
    import json as json_mod
    ideas = load_ideas()
    if args.type == "gaps" or args.type == "market-gaps":
        analysis = market_gap_analysis(ideas)
        if args.json:
            print(json_mod.dumps(analysis, indent=2))
        else:
            print_market_gap(analysis)
    elif args.type == "competitive":
        analysis = competitive_analysis(
            filter_ideas(ideas, category=args.category) if args.category else ideas
        )
        if args.json:
            print(json_mod.dumps(analysis, indent=2))
        else:
            print_competitive_analysis(analysis)
    elif args.type == "persona":
        analysis = persona_analysis(ideas)
        if args.json:
            print(json_mod.dumps(analysis, indent=2))
        else:
            print_persona_breakdown(analysis)
    elif args.type == "trends":
        trends = trend_analysis(ideas)
        if args.json:
            print(json_mod.dumps({k: dict(v) for k, v in trends.items()}, indent=2))
        else:
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
        if args.json:
            print(json_mod.dumps(stats, indent=2))
        else:
            print_stats(stats)
    elif args.type == "compare":
        if not args.ideas:
            print("Usage: productfound analyze compare \"Idea 1\" \"Idea 2\" [--json]")
            return
        analysis = compare_ideas(ideas, args.ideas)
        if args.json:
            print(json_mod.dumps(analysis, indent=2))
        else:
            print_comparison(analysis)
    elif args.type == "assess":
        if not args.product:
            print("Usage: productfound analyze assess \"Product Name\" [--desc \"description\"] [--json]")
            return
        analysis = assess_product(ideas, args.product, args.desc or "")
        if args.json:
            print(json_mod.dumps(analysis, indent=2))
        else:
            print_assessment(analysis)


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


def format_funding(val):
    if val >= 1e9:
        return f"${val/1e9:.1f}B"
    elif val >= 1e6:
        return f"${val/1e6:.0f}M"
    else:
        return "N/A"


def cmd_pm_search(args):
    results = pm_search(
        region=args.region,
        category=args.category,
        failure_reason=args.reason,
        keyword=args.keyword,
    )
    if not results:
        print("No matching postmortems found.")
        return
    print(f"\n{'Company':<22} {'Region':<10} {'Category':<16} {'Funding':<12} {'Failure Reason'}")
    print("-" * 90)
    for p in results:
        print(f"{p['title']:<22} {p['region']:<10} {p['category']:<16} {p['funding']:<12} {p['failure_reason']}")
    print(f"\n{len(results)} postmortems found.")


def cmd_pm_stats(args):
    all_pm = get_all_pm()
    regions, total_funding = pm_region_summary()
    reasons = pm_failure_reasons()
    cats, funding_by_cat = pm_category_breakdown()

    print(f"\n=== Global Postmortem Dataset ===")
    print(f"Total companies: {len(all_pm)}")
    print(f"Total capital lost: ${sum(total_funding.values())/1e9:.1f}B")
    print(f"Regions covered: {len(regions)}")
    print(f"Categories covered: {len(cats)}")
    print()

    print("By Region:")
    for r, n in regions.most_common():
        print(f"  {r:<12} {n:>3} companies — {format_funding(total_funding.get(r, 0))}")
    print()

    print("Failure Reasons:")
    for r, n in reasons.most_common():
        print(f"  {r:<25} {n:>2}")
    print()

    print("By Category:")
    for c, n in cats.most_common():
        print(f"  {c:<16} {n:>2} companies — {format_funding(funding_by_cat.get(c, 0))} lost")


def cmd_pm_compare(args):
    pm_compare_regions(args.region1, args.region2)
    result = pm_compare_regions(args.region1, args.region2)
    r1 = result[args.region1]
    r2 = result[args.region2]

    print(f"\n{'':<20} {args.region1:<30} {args.region2}")
    print("-" * 70)
    print(f"{'Companies':<20} {r1['count']:<30} {r2['count']}")
    print(f"{'Capital lost':<20} {format_funding(r1['funding']):<30} {format_funding(r2['funding'])}")
    print(f"{'Top reasons':<20}")
    for i in range(max(len(r1['top_reasons']), len(r2['top_reasons']))):
        r1r = f"{r1['top_reasons'][i][0]} ({r1['top_reasons'][i][1]})" if i < len(r1['top_reasons']) else ""
        r2r = f"{r2['top_reasons'][i][0]} ({r2['top_reasons'][i][1]})" if i < len(r2['top_reasons']) else ""
        print(f"  {i+1}.{r1r:<48} {r2r}")
    print()


def main():
    parser = argparse.ArgumentParser(
        prog="productfound",
        description="Productfound — Market research from 1,000 failed startups.",
        epilog="More info: https://github.com/jithindeepjc/productfound",
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
    p_analyze.add_argument("type", choices=["gaps", "market-gaps", "competitive", "persona", "trends", "stats", "compare", "assess"],
                           help="Analysis type")
    p_analyze.add_argument("--category", help="Filter analysis to category (for competitive)")
    p_analyze.add_argument("--json", action="store_true", help="Output as JSON")
    p_analyze.add_argument("--ideas", nargs="+", help="Idea names to compare (for compare)")
    p_analyze.add_argument("--product", help="Product name to assess (for assess)")
    p_analyze.add_argument("--desc", help="Product description (for assess)")
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

    # Postmortems commands
    p_pm = sub.add_parser("postmortems", help="Analyze real failed startup postmortems worldwide")
    p_pm_sub = p_pm.add_subparsers(dest="pm_cmd")

    p_pm_search = p_pm_sub.add_parser("search", help="Search postmortems by region, category, keyword")
    p_pm_search.add_argument("--region", choices=["India", "US", "Europe", "SEA", "LATAM", "Africa", "Global"], help="Filter by region")
    p_pm_search.add_argument("--category", help="Filter by industry category")
    p_pm_search.add_argument("--reason", help="Filter by failure reason keyword")
    p_pm_search.add_argument("--keyword", "-k", help="Search by company name or description")
    p_pm_search.set_defaults(func=cmd_pm_search)

    p_pm_stats = p_pm_sub.add_parser("stats", help="Postmortem dataset statistics")
    p_pm_stats.set_defaults(func=cmd_pm_stats)

    p_pm_compare = p_pm_sub.add_parser("compare", help="Compare failure patterns across regions")
    p_pm_compare.add_argument("region1", help="First region (India, US, Europe, SEA, LATAM, Africa, Global)")
    p_pm_compare.add_argument("region2", help="Second region")
    p_pm_compare.set_defaults(func=cmd_pm_compare)

    args = parser.parse_args()
    if args.command:
        args.func(args)
    else:
        parser.print_help()
        print("\nTIP: Run 'productfound filters' to see available filter values.")
        print("     Run 'productfound search --category DevTools' to search ideas.")
        print("     Run 'productfound analyze stats' for dataset overview.")
        print("     Run 'productfound random' for random ideas.")
        print("     Run 'productfound postmortems search --region India' for real failure data.")
