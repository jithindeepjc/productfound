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


def compare_ideas(ideas, names):
    results = []
    from productfound.postmortems_data import POSTMORTEMS
    for name in names:
        name_lower = name.lower()
        matches = [i for i in ideas if name_lower in (i.get("title") or "").lower()
                   or name_lower in (i.get("desc") or "").lower()]
        if matches:
            idea = matches[0]
            score = 50
            risks = []
            tags = idea.get("tags", [])
            if "hardware" in tags or "regulatory" in tags:
                risks.append("High barrier to entry")
                score -= 15
            if "crypto" in tags or "blockchain" in tags:
                risks.append("Regulatory uncertainty")
                score -= 10
            if "enterprise" in tags:
                risks.append("Long enterprise sales cycle")
                score -= 5
            effort = idea.get("effort", "?")
            if effort in ("6+ Months", "3-6 Months"):
                score -= 5 if effort == "3-6 Months" else 10
            cat = idea.get("category", "?")
            cat_count = sum(1 for i in ideas if i.get("category") == cat)
            if cat_count < 10:
                score += 15
                risks.append(f"Unvalidated category ({cat_count} ideas in dataset)")
            elif cat_count > 50:
                score -= 10
                risks.append(f"Crowded category ({cat_count} ideas)")

            similar_failures = [p["title"] for p in POSTMORTEMS if p.get("category") == idea.get("category")][:3]

            results.append({
                "name": idea.get("title", name),
                "score": max(0, min(100, score)),
                "category": idea.get("category", "?"),
                "model": idea.get("model", "?"),
                "effort": effort,
                "speed": idea.get("speed", "?"),
                "persona": idea.get("persona", "?"),
                "risks": risks,
                "verdict": "Go" if score >= 60 else ("Pivot" if score >= 30 else "Avoid"),
                "similar_failures": similar_failures,
            })
        else:
            cat = _guess_category(name, ideas)
            results.append({
                "name": name,
                "score": 40,
                "category": cat,
                "model": "Unknown",
                "effort": "Unknown",
                "speed": "Unknown",
                "persona": "Unknown",
                "risks": ["No direct dataset match — unvalidated concept"],
                "verdict": "Needs Research",
                "similar_failures": [],
            })
    return results


def _guess_category(name, ideas):
    cats = set(i.get("category", "") for i in ideas)
    keyword_map = {
        "ai": "DevTools", "app": "Mobile", "platform": "DevTools", "market": "Ecommerce",
        "shop": "Ecommerce", "pay": "Fintech", "finance": "Fintech", "health": "Health",
        "med": "Health", "learn": "EdTech", "edu": "EdTech", "green": "CleanTech",
        "energy": "CleanTech", "food": "Food", "travel": "Travel", "game": "Gaming",
        "crypto": "Crypto", "blockchain": "Crypto", "social": "Social", "media": "Media",
        "real": "PropTech", "estate": "PropTech", "dev": "DevTools", "tool": "DevTools",
        "saas": "DevTools", "logistics": "Logistics", "delivery": "Logistics",
    }
    name_lower = name.lower()
    for keyword, cat in keyword_map.items():
        if keyword in name_lower:
            return cat
    return "General"


def assess_product(ideas, name, desc=""):
    from productfound.postmortems_data import POSTMORTEMS

    name_lower = name.lower()
    matches = [i for i in ideas if name_lower in (i.get("title") or "").lower()
               or name_lower in (i.get("desc") or "").lower()
               or any(name_lower in t.lower() for t in (i.get("tags") or []))]
    if desc:
        matches.extend([i for i in ideas if desc.lower()[:30] in (i.get("desc") or "").lower()])
    matches = list({i.get("id"): i for i in matches}.values())

    if matches:
        idea = matches[0]
        cat = idea.get("category", "General")
        cat_count = sum(1 for i in ideas if i.get("category") == cat)
        category_fit = "Strong" if matches else "Weak"
        competitive_density = "Low"
        if cat_count < 10:
            competitive_density = "Very Low (first mover)"
        elif cat_count < 30:
            competitive_density = "Moderate"
        elif cat_count < 60:
            competitive_density = "High"
        else:
            competitive_density = "Very High (crowded)"

        strengths = []
        risks = []
        tags = idea.get("tags", [])

        if competitive_density in ("Very Low", "Low"):
            strengths.append("First-mover opportunity in this category")
        if idea.get("effort") in ("Weekend Project", "1-3 Months"):
            strengths.append("Low time-to-market")
        if idea.get("speed") == "Quick Cash":
            strengths.append("Fast monetization potential")
        if idea.get("model") in ("Subscription/SaaS",):
            strengths.append("Recurring revenue model")

        if "hardware" in tags:
            risks.append("Hardware complexity and supply chain risk")
        if "regulatory" in tags:
            risks.append("Regulatory compliance burden")
        if "enterprise" in tags:
            risks.append("Enterprise sales cycle (6-18 months)")
        if "marketplace" in tags:
            risks.append("Two-sided marketplace chicken-and-egg problem")
        if competitive_density in ("High", "Very High"):
            risks.append(f"Crowded category ({cat_count} ideas in dataset)")

        all_pm_cats = set(p["category"] for p in POSTMORTEMS)
        similar = [p["title"] for p in POSTMORTEMS if p.get("category") == cat and p.get("funding", "N/A") != "N/A"][:3]
        if not similar:
            similar = [p["title"] for p in POSTMORTEMS if p.get("category") in all_pm_cats][:3]

        score = 50
        if category_fit == "Strong":
            score += 10
        if competitive_density in ("Very Low", "Low"):
            score += 15
        elif competitive_density == "High":
            score -= 10
        elif competitive_density == "Very High":
            score -= 15
        if "hardware" in tags or "regulatory" in tags:
            score -= 10
        if idea.get("effort") in ("Weekend Project", "1-3 Months"):
            score += 5
        score = max(0, min(100, score))

        return {
            "product": name,
            "score": score,
            "category_fit": category_fit,
            "competitive_density": competitive_density,
            "strengths": strengths or ["Differentiated concept"],
            "risks": risks or ["Unvalidated market assumptions"],
            "similar_failures": similar,
        }
    else:
        cat = _guess_category(name, ideas)
        cat_count = sum(1 for i in ideas if i.get("category") == cat)
        return {
            "product": name,
            "score": 35,
            "category_fit": f"Assumed ({cat}) — no direct dataset match",
            "competitive_density": "Low" if cat_count < 20 else "Moderate",
            "strengths": ["Novel concept (no direct analog in dataset)"],
            "risks": ["No dataset validation — unproven category fit",
                      f"Category '{cat}' has {cat_count} reference ideas — limited signal"],
            "similar_failures": [p["title"] for p in POSTMORTEMS if p.get("category") == cat][:3],
        }
