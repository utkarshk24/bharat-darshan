"""Helpers for authoring Bharat Darshan data files."""
import json, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data")
TODAY = "2026-10-13"


def L(en, hi, mr, status="draft"):
    return {"en": en, "hi": hi, "mr": mr, "_status": {"hi": status, "mr": status}}


def dp(value, unit, period, ptype, src, url, *, level="state", rev="final", conf="Official",
       note=None, base=None, access=TODAY):
    d = {"value": value, "unit": unit, "period": period, "periodType": ptype, "sourceId": src,
         "url": url, "accessDate": access if value is not None else None, "dataLevel": level,
         "revisionStatus": rev if value is not None else "TODO", "confidence": conf}
    if base:
        d["priceBase"] = base
    if note:
        d["note"] = note
    return d


def todo(unit, period, ptype, src, note, level="state", base=None):
    return dp(None, unit, period, ptype, src, None, level=level, note=note, base=base)


def write(rel, obj):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def read(rel):
    with open(os.path.join(ROOT, rel)) as f:
        return json.load(f)


def module(region, key, blocks, as_of=TODAY):
    write(f"modules/{region}/{key}.json", {"region": region, "module": key, "asOf": as_of, "status": "draft", "blocks": blocks})


# Block helpers
def prose(id, body, sources=(), conf="Editorial", title=None):
    b = {"type": "prose", "id": id, "body": body, "sourceIds": list(sources), "confidence": conf}
    if title:
        b["title"] = title
    return b


def facts(id, items, title=None):
    b = {"type": "facts", "id": id, "items": items}
    if title:
        b["title"] = title
    return b


def fact(id, label, d, kind, polarity="neutral", previous=None, national=None):
    f = {"id": id, "label": label, "dp": d, "kind": kind, "polarity": polarity}
    if previous:
        f["previous"] = previous
    if national:
        f["national"] = national
    return f


def lst(id, items, layout="cards", title=None, src=None, url=None, conf="Editorial", access=None):
    b = {"type": "list", "id": id, "layout": layout, "items": items, "sourceId": src, "url": url,
         "accessDate": access, "confidence": conf}
    if title:
        b["title"] = title
    return b


def item(id, name, detail=None, meta=None, url=None, src=None):
    i = {"id": id, "name": name}
    if detail:
        i["detail"] = detail
    if meta:
        i["meta"] = meta
    if url:
        i["url"] = url
    if src:
        i["sourceId"] = src
    return i


def table(id, title, columns, rows, src, url, conf="Official", access=TODAY, period=None, note=None):
    b = {"type": "table", "id": id, "title": title, "columns": columns, "rows": rows, "sourceId": src,
         "url": url, "accessDate": access, "confidence": conf}
    if period:
        b["period"] = period
    if note:
        b["note"] = note
    return b


def col(label, align="left"):
    return {"label": label, "align": align}


def gaps(id, items):
    return {"type": "gaps", "id": id, "items": [{"label": l, "sourceId": s, "note": n} for l, s, n in items]}


def inr(n):
    """Indian digit grouping for notes: 3306814 -> '33,06,814'."""
    s = str(int(n)); neg = s.startswith("-"); s = s.lstrip("-")
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:]); head = head[:-2]
        if head: parts.insert(0, head)
        s = ",".join(parts + [tail])
    return ("-" if neg else "") + s
