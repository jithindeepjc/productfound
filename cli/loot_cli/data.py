import json
import base64
import gzip
import io

DATA = None

def get_data_b64():
    from loot_cli.data_b64 import DATA_B64
    return DATA_B64

def load_ideas(force_reload=False):
    global DATA
    if DATA is not None and not force_reload:
        return DATA
    raw = get_data_b64()
    compressed = base64.b64decode(raw)
    decompressed = gzip.GzipFile(fileobj=io.BytesIO(compressed)).read()
    DATA = json.loads(decompressed)
    return DATA


def filter_ideas(ideas, model=None, effort=None, speed=None, category=None, keyword=None, tags=None, persona=None):
    results = []
    for idea in ideas:
        if model and model != "all":
            if idea.get("model", "").lower() != model.lower():
                continue
        if effort and effort != "all":
            if idea.get("effort", "").lower() != effort.lower():
                continue
        if speed and speed != "all":
            if idea.get("speed", "").lower() != speed.lower():
                continue
        if category and category != "all":
            idea_cat = (idea.get("category") or "").lower()
            if idea_cat != category.lower():
                continue
        if persona and persona != "all":
            if (idea.get("persona") or "").lower() != persona.lower():
                continue
        if keyword:
            kw = keyword.lower()
            title = (idea.get("title") or "").lower()
            desc = (idea.get("desc") or "").lower()
            if kw not in title and kw not in desc:
                continue
        if tags:
            idea_tags = [t.lower() for t in (idea.get("tags") or [])]
            if not any(t.lower() in idea_tags for t in tags):
                continue
        results.append(idea)
    return results


def get_unique_values(ideas, field):
    vals = set()
    for i in ideas:
        v = i.get(field)
        if v:
            vals.add(v)
    return sorted(vals)


def get_all_tags(ideas):
    tags = set()
    for i in ideas:
        if i.get("tags"):
            tags.update(i["tags"])
    return sorted(tags)


def compute_stats(ideas):
    from collections import Counter
    cats = Counter(i.get("category") for i in ideas if i.get("category"))
    models = Counter(i.get("model") for i in ideas if i.get("model"))
    efforts = Counter(i.get("effort") for i in ideas if i.get("effort"))
    speeds = Counter(i.get("speed") for i in ideas if i.get("speed"))
    personas = Counter(i.get("persona") for i in ideas if i.get("persona"))
    all_tags = []
    for i in ideas:
        if i.get("tags"):
            all_tags.extend(i["tags"])
    tags = Counter(all_tags)
    return {
        "total": len(ideas),
        "categories": cats,
        "models": models,
        "efforts": efforts,
        "speeds": speeds,
        "personas": personas,
        "tags": tags,
    }
