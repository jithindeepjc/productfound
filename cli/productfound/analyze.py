from collections import Counter


def market_gap_analysis(ideas):
    categories = {}
    for i in ideas:
        cat = i.get("category") or "Unknown"
        if cat not in categories:
            categories[cat] = {"ideas": [], "models": set(), "tags": []}
        categories[cat]["ideas"].append(i)
        categories[cat]["models"].add(i.get("model", ""))
        if i.get("tags"):
            categories[cat]["tags"].extend(i["tags"])

    gaps = []
    for cat, data in sorted(categories.items(), key=lambda x: len(x[1]["ideas"])):
        tag_counts = Counter(data["tags"])
        models = sorted(data["models"], key=lambda m: -sum(1 for i in data["ideas"] if i.get("model") == m))
        gap = {
            "category": cat,
            "count": len(data["ideas"]),
            "models": models,
            "top_tags": [t for t, _ in tag_counts.most_common(8)],
            "focus": "underserved" if len(data["ideas"]) < 20 else "crowded",
            "insight": _generate_gap_insight(cat, len(data["ideas"]), models, tag_counts),
        }
        gaps.append(gap)
    return gaps


def _generate_gap_insight(category, count, models, tag_counts):
    if count < 10:
        return f"Underserved category ({count} ideas). First-mover opportunity in {category}. Consider {' or '.join(models[:3]) if models else 'various'} models."
    elif count < 30:
        return f"Emerging category ({count} ideas). Growing space — differentiate with unique model or niche within {category}."
    elif count < 60:
        return f"Active category ({count} ideas). Competitive landscape forming. Top tags: {', '.join(t for t, _ in tag_counts.most_common(3))}."
    else:
        return f"Crowded category ({count} ideas). High competition. Need strong differentiation. Dominant tags: {', '.join(t for t, _ in tag_counts.most_common(3))}."


def competitive_analysis(ideas):
    from collections import Counter
    cats = {}
    for i in ideas:
        cat = i.get("category") or "Unknown"
        if cat not in cats:
            cats[cat] = {"ideas": [], "models": Counter(), "efforts": Counter()}
        cats[cat]["ideas"].append(i)
        cats[cat]["models"][i.get("model", "?")] += 1
        cats[cat]["efforts"][i.get("effort", "?")] += 1

    analysis = []
    for cat, data in sorted(cats.items(), key=lambda x: -len(x[1]["ideas"])):
        all_tags = []
        for i in data["ideas"]:
            if i.get("tags"):
                all_tags.extend(i["tags"])
        tag_counts = Counter(all_tags)
        risk_tags = [t for t, _ in tag_counts.most_common(10)
                     if t.lower() in ("hardware", "crypto", "regulatory", "enterprise", "high ticket", "blockchain")]
        avg_effort = data["efforts"].most_common(1)[0][0] if data["efforts"] else "?"
        analysis.append({
            "category": cat,
            "count": len(data["ideas"]),
            "top_model": data["models"].most_common(1)[0][0] if data["models"] else "?",
            "avg_effort": avg_effort,
            "risk_tags": risk_tags or [t for t, _ in tag_counts.most_common(3)],
        })
    return analysis


def persona_analysis(ideas):
    from collections import Counter
    personas = {}
    for i in ideas:
        p = i.get("persona") or "Unknown"
        if p not in personas:
            personas[p] = {"ideas": [], "categories": Counter(), "models": Counter()}
        personas[p]["ideas"].append(i)
        personas[p]["categories"][i.get("category", "?")] += 1
        personas[p]["models"][i.get("model", "?")] += 1

    analysis = {}
    signatures = {
        "The Vibe Coder": "Quick builds, weekend projects, trend-surfing",
        "The B2B SaaS Veteran": "Subscription/SaaS, enterprise, 6+ month builds",
        "The Realistic Side-Hustler": "Freemium/affiliate, quick cash, bootstrap-friendly",
        "The Trend Surfer": "Early-stage markets, viral potential, media/creative",
        "The Tech Visionary": "Deep tech, VC-backable, long game plays",
    }
    for p, data in sorted(personas.items()):
        top_cats = [c for c, _ in data["categories"].most_common(5)]
        top_models = [m for m, _ in data["models"].most_common(5)]
        analysis[p] = {
            "count": len(data["ideas"]),
            "top_categories": top_cats,
            "top_models": top_models,
            "signature": signatures.get(p, "Mixed profile"),
        }
    return analysis


def trend_analysis(ideas):
    models_by_effort = {}
    for i in ideas:
        effort = i.get("effort")
        model = i.get("model")
        if effort and model:
            if effort not in models_by_effort:
                models_by_effort[effort] = Counter()
            models_by_effort[effort][model] += 1

    tags_by_speed = {}
    for i in ideas:
        speed = i.get("speed")
        if speed and i.get("tags"):
            if speed not in tags_by_speed:
                tags_by_speed[speed] = Counter()
            for t in i["tags"]:
                tags_by_speed[speed][t] += 1

    return {
        "models_by_effort": models_by_effort,
        "tags_by_speed": tags_by_speed,
    }
