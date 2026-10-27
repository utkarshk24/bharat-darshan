"""Add the official sources used by the Phase 4 freshness pass on officeholder cards — idempotent."""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "sources.json")
src = json.load(open(P))
have = {s["id"] for s in src}
G = dict(category="governance", priority=5)
NEW = [
    dict(id="gj-assembly", short="Gujarat Assembly", name="Gujarat Legislative Assembly — notifications (NeVA)", publisher="Gujarat Legislature Secretariat",
         url="https://cms.neva.gov.in", **G),
    dict(id="goa-gov", short="Govt of Goa", name="Government of Goa — official portal and press notes", publisher="Government of Goa",
         url="https://www.goa.gov.in", **G),
    dict(id="hr-assembly", short="Haryana Vidhan Sabha", name="Haryana Vidhan Sabha — official website", publisher="Haryana Vidhan Sabha Secretariat",
         url="https://haryanaassembly.gov.in", **G),
    dict(id="nl-ipr", short="DIPR Nagaland", name="Directorate of Information & Public Relations, Nagaland — press releases", publisher="Government of Nagaland",
         url="https://ipr.nagaland.gov.in", **G),
    dict(id="or-assembly", short="Odisha Assembly", name="Odisha Legislative Assembly — official website", publisher="Odisha Legislative Assembly Secretariat",
         url="https://odishaassembly.nic.in", **G),
    dict(id="pb-ipr", short="DIPR Punjab", name="Department of Information & Public Relations, Punjab — press releases", publisher="Government of Punjab",
         url="https://ipr.punjab.gov.in", **G),
    dict(id="tg-gov", short="Govt of Telangana", name="Telangana State Portal", publisher="Government of Telangana",
         url="https://www.telangana.gov.in", **G),
    dict(id="tr-lokbhavan", short="Raj Bhavan Tripura", name="Raj Bhavan, Tripura — official website", publisher="Office of the Governor of Tripura",
         url="https://rajbhavan.tripura.gov.in", **G),
    dict(id="uk-lokbhavan", short="Lok Bhavan Uttarakhand", name="Lok Bhavan, Uttarakhand — press notes", publisher="Office of the Governor of Uttarakhand",
         url="https://governoruk.gov.in", **G),
]
added = 0
for s in NEW:
    if s["id"] not in have:
        src.append(s); added += 1
json.dump(src, open(P, "w"), ensure_ascii=False, indent=2)
print("sources added", added, "total", len(src))
