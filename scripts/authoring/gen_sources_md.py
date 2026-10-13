"""Regenerate SOURCES.md from data/sources.json."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
src = json.load(open(os.path.join(ROOT, "data", "sources.json")))
NAMES = {"demographics": "Demographics", "economy": "Economy", "development": "Development", "health": "Health", "education": "Education",
         "environment": "Environment", "transport-energy": "Transport & energy", "tourism-heritage": "Tourism & heritage", "gi": "GI",
         "governance": "Governance", "tribal-social": "Tribal & social", "climate-hazards": "Climate & hazards", "maps": "Maps", "standards": "Standards"}
out = ["# SOURCES", "", "Generated from `data/sources.json` by `scripts/authoring/gen_sources_md.py` — edit the JSON, not this file. Order within each category is the order of preference (Section 15). Every data point references a source by `sourceId`; the validator rejects unknown ids. Sources whose publisher is marked *third party* are used only where no official page was reachable, and are labelled in the UI.", ""]
for c, title in NAMES.items():
    rows = sorted([s for s in src if s["category"] == c], key=lambda s: s["priority"])
    if not rows: continue
    out += [f"## {title}", "", "| id | Source | Publisher | Notes |", "|---|---|---|---|"]
    out += [f"| `{s['id']}` | [{s['name']}]({s['url']}) | {s['publisher']} | {s.get('notes', '')} |" for s in rows]
    out.append("")
open(os.path.join(ROOT, "SOURCES.md"), "w").write("\n".join(out))
print(len(src), "sources")
