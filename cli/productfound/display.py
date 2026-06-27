import shutil

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich.layout import Layout
    from rich import box
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

console = Console() if HAS_RICH else None

TERM_WIDTH = shutil.get_terminal_size().columns


def _wrap(text, width=80):
    if not text:
        return ""
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) + 1 > width:
            lines.append(current)
            current = w
        else:
            current = (current + " " + w).strip()
    if current:
        lines.append(current)
    return "\n".join(lines)


def print_ideas(ideas, count=20):
    if not ideas:
        print("No ideas found matching criteria.")
        return
    if HAS_RICH:
        table = Table(show_header=True, header_style="bold cyan", box=box.MINIMAL)
        table.add_column("#", style="dim", width=4)
        table.add_column("Idea", style="bold white", width=30)
        table.add_column("Model", width=14)
        table.add_column("Effort", width=14)
        table.add_column("Speed", width=14)
        table.add_column("Category", width=14)
        for idx, idea in enumerate(ideas[:count], 1):
            table.add_row(
                str(idx),
                idea.get("title", "?"),
                idea.get("model", "?"),
                idea.get("effort", "?"),
                idea.get("speed", "?"),
                idea.get("category", "?"),
            )
        console.print(table)
    else:
        print(f"{'#':<4} {'Idea':<30} {'Model':<14} {'Effort':<14} {'Speed':<14} {'Category':<14}")
        print("-" * 90)
        for idx, idea in enumerate(ideas[:count], 1):
            print(f"{idx:<4} {idea.get('title', '?'):<30} {idea.get('model', '?'):<14} {idea.get('effort', '?'):<14} {idea.get('speed', '?'):<14} {idea.get('category', '?'):<14}")
    remaining = len(ideas) - count
    if remaining > 0:
        print(f"\n... and {remaining} more results (use --all to show all)")


def print_idea_detail(idea):
    if HAS_RICH:
        tags_str = ", ".join(idea.get("tags") or [])
        detail = (
            f"[bold]Title:[/bold] {idea.get('title', '?')}\n"
            f"[bold]Description:[/bold] {idea.get('desc', '?')}\n"
            f"[bold]Model:[/bold] {idea.get('model', '?')}\n"
            f"[bold]Effort:[/bold] {idea.get('effort', '?')}\n"
            f"[bold]Monetization Speed:[/bold] {idea.get('speed', '?')}\n"
            f"[bold]Category:[/bold] {idea.get('category', '?')}\n"
            f"[bold]Persona:[/bold] {idea.get('persona', '?')}\n"
            f"[bold]Tags:[/bold] {tags_str}"
        )
        console.print(Panel(detail, title=f"Idea #{idea.get('id', '?')}", border_style="cyan"))
    else:
        print(f"ID:          {idea.get('id', '?')}")
        print(f"Title:       {idea.get('title', '?')}")
        print(f"Description: {_wrap(idea.get('desc', ''), 70)}")
        print(f"Model:       {idea.get('model', '?')}")
        print(f"Effort:      {idea.get('effort', '?')}")
        print(f"Speed:       {idea.get('speed', '?')}")
        print(f"Category:    {idea.get('category', '?')}")
        print(f"Persona:     {idea.get('persona', '?')}")
        print(f"Tags:        {', '.join(idea.get('tags') or [])}")
    print()


def print_stats(stats):
    if HAS_RICH:
        layout = Layout()
        layout.split_column(
            Layout(Panel(f"[bold]Total Ideas: {stats['total']}[/bold]", style="cyan")),
        )
        console.print(layout)

        for title, counter in [
            ("Categories", stats["categories"]),
            ("Business Models", stats["models"]),
            ("Effort Required", stats["efforts"]),
            ("Monetization Speed", stats["speeds"]),
            ("Builder Persona", stats["personas"]),
        ]:
            table = Table(title=title, box=box.MINIMAL, header_style="bold magenta")
            table.add_column("Value")
            table.add_column("Count", justify="right")
            for val, cnt in counter.most_common():
                table.add_row(val, str(cnt))
            console.print(table)

        table = Table(title="Top 30 Tags", box=box.MINIMAL, header_style="bold green")
        table.add_column("Tag")
        table.add_column("Count", justify="right")
        for tag, cnt in stats["tags"].most_common(30):
            table.add_row(tag, str(cnt))
        console.print(table)
    else:
        print(f"Total Ideas: {stats['total']}\n")
        for title, counter in [
            ("Categories", stats["categories"]),
            ("Business Models", stats["models"]),
            ("Effort Required", stats["efforts"]),
            ("Monetization Speed", stats["speeds"]),
            ("Builder Persona", stats["personas"]),
        ]:
            print(f"\n--- {title} ---")
            for val, cnt in counter.most_common():
                print(f"  {val:<20} {cnt}")
        print("\n--- Top 30 Tags ---")
        for tag, cnt in stats["tags"].most_common(30):
            print(f"  {tag:<25} {cnt}")


def print_market_gap(analysis):
    if HAS_RICH:
        for gap in analysis:
            title = f"{gap['category']} — {gap['focus']}"
            detail = (
                f"[bold]Total Ideas:[/bold] {gap['count']}\n"
                f"[bold]Models:[/bold] {', '.join(gap['models'][:5])}\n"
                f"[bold]Top Tags:[/bold] {', '.join(gap['top_tags'][:5])}\n"
                f"[bold]Observation:[/bold] {gap['insight']}"
            )
            console.print(Panel(detail, title=title, border_style="yellow"))
    else:
        for gap in analysis:
            print(f"\n{gap['category']} — {gap['focus']}")
            print(f"  Ideas: {gap['count']}")
            print(f"  Models: {', '.join(gap['models'][:5])}")
            print(f"  Tags: {', '.join(gap['top_tags'][:5])}")
            print(f"  Insight: {gap['insight']}")


def print_competitive_analysis(analysis):
    if HAS_RICH:
        table = Table(title="Competitive Landscape", box=box.MINIMAL, header_style="bold red")
        table.add_column("Category")
        table.add_column("Idea Count", justify="right")
        table.add_column("Dominant Model")
        table.add_column("Avg Effort")
        table.add_column("Key Risk Tags")
        for row in analysis:
            table.add_row(
                row["category"],
                str(row["count"]),
                row["top_model"],
                row["avg_effort"],
                ", ".join(row["risk_tags"][:3]),
            )
        console.print(table)
    else:
        print(f"{'Category':<20} {'Count':<8} {'Top Model':<18} {'Effort':<14} {'Risk Tags'}")
        print("-" * 90)
        for row in analysis:
            print(f"{row['category']:<20} {row['count']:<8} {row['top_model']:<18} {row['avg_effort']:<14} {', '.join(row['risk_tags'][:3])}")


def print_persona_breakdown(analysis):
    if HAS_RICH:
        for persona, data in analysis.items():
            detail = (
                f"[bold]Ideas:[/bold] {data['count']}\n"
                f"[bold]Top Categories:[/bold] {', '.join(data['top_categories'][:5])}\n"
                f"[bold]Top Models:[/bold] {', '.join(data['top_models'][:5])}\n"
                f"[bold]Signature:[/bold] {data['signature']}"
            )
            console.print(Panel(detail, title=f"👤 {persona}", border_style="blue"))
    else:
        for persona, data in analysis.items():
            print(f"\n{persona} ({data['count']} ideas)")
            print(f"  Categories: {', '.join(data['top_categories'][:5])}")
            print(f"  Models: {', '.join(data['top_models'][:5])}")
            print(f"  Signature: {data['signature']}")


def print_tags(tags, counts=None):
    if HAS_RICH:
        if counts:
            table = Table(box=box.MINIMAL, header_style="bold green")
            table.add_column("Tag")
            table.add_column("Count", justify="right")
            for tag, cnt in counts.most_common():
                table.add_row(tag, str(cnt))
            console.print(table)
        else:
            console.print(f"[bold]Tags ({len(tags)}):[/bold]")
            console.print(", ".join(tags))
    else:
        if counts:
            print(f"{'Tag':<25} {'Count'}")
            print("-" * 35)
            for tag, cnt in counts.most_common():
                print(f"{tag:<25} {cnt}")
        else:
            print(f"Tags ({len(tags)}):")
            print(", ".join(tags))
