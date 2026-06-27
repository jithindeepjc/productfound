from collections import Counter, defaultdict
from .postmortems_data import POSTMORTEMS


def get_all():
    return POSTMORTEMS


def search(region=None, category=None, failure_reason=None, keyword=None, min_funding=None):
    results = POSTMORTEMS
    if region:
        rl = region.lower()
        results = [p for p in results if p.get("region", "").lower() == rl]
    if category:
        cl = category.lower()
        results = [p for p in results if p.get("category", "").lower() == cl]
    if failure_reason:
        fl = failure_reason.lower()
        results = [p for p in results if fl in p.get("failure_reason", "").lower()]
    if keyword:
        kw = keyword.lower()
        results = [p for p in results if kw in p.get("title", "").lower() or kw in p.get("desc", "").lower()]
    return results


def region_summary():
    regions = Counter(p["region"] for p in POSTMORTEMS)
    total_funding = defaultdict(float)
    for p in POSTMORTEMS:
        total_funding[p["region"]] += _parse_funding(p.get("funding"))
    return regions, total_funding


def failure_reasons():
    reasons = Counter()
    for p in POSTMORTEMS:
        r = p.get("failure_reason", "Unknown")
        # Normalize to bucket
        rl = r.lower()
        if "fraud" in rl or "governance" in rl:
            bucket = "Fraud / Governance"
        elif "unit economics" in rl or "unprofitable" in rl or "uneconomic" in rl:
            bucket = "Unit Economics"
        elif "market" in rl or "demand" in rl or "relevance" in rl:
            bucket = "No Market Need"
        elif "capital" in rl or "cash" in rl or "funding" in rl:
            bucket = "Cash / Funding"
        elif "competition" in rl:
            bucket = "Competition"
        elif "scale" in rl or "overexpansion" in rl or "overambitious" in rl:
            bucket = "Premature Scaling"
        elif "regulatory" in rl:
            bucket = "Regulation"
        elif "pivot" in rl or "timing" in rl or "feature" in rl:
            bucket = "Pivot / Timing"
        else:
            bucket = "Execution"
        reasons[bucket] += 1
    return reasons


def category_breakdown():
    cats = Counter(p["category"] for p in POSTMORTEMS)
    funding_by_cat = defaultdict(float)
    for p in POSTMORTEMS:
        funding_by_cat[p["category"]] += _parse_funding(p.get("funding"))
    return cats, funding_by_cat


def _parse_funding(val):
    if not val or val == "N/A":
        return 0.0
    try:
        return float(val.replace("$", "").replace("B", "e9").replace("M", "e6"))
    except:
        return 0.0


def compare_regions(r1, r2):
    r1_data = [p for p in POSTMORTEMS if p["region"] == r1]
    r2_data = [p for p in POSTMORTEMS if p["region"] == r2]
    r1_reasons = Counter(p["failure_reason"] for p in r1_data)
    r2_reasons = Counter(p["failure_reason"] for p in r2_data)
    return {
        r1: {"count": len(r1_data), "funding": sum(_parse_funding(p.get("funding")) for p in r1_data), "top_reasons": r1_reasons.most_common(3)},
        r2: {"count": len(r2_data), "funding": sum(_parse_funding(p.get("funding")) for p in r2_data), "top_reasons": r2_reasons.most_common(3)},
    }
