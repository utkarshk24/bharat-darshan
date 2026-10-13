"""Add the sources used for the Tamil Nadu profile (idempotent)."""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "sources.json")
src = json.load(open(P))
have = {s["id"] for s in src}

NEW = [
    dict(id="tn-lokbhavan", short="Lok Bhavan, Tamil Nadu", name="Lok Bhavan (formerly Raj Bhavan), Tamil Nadu",
         publisher="Office of the Governor of Tamil Nadu", url="https://lokbhavan.tn.gov.in", category="governance", priority=8),
    dict(id="tn-gov", short="Government of Tamil Nadu", name="Government of Tamil Nadu portal", publisher="Government of Tamil Nadu",
         url="https://www.tn.gov.in", category="governance", priority=7),
    dict(id="isro", short="ISRO", name="Indian Space Research Organisation — news and updates", publisher="Department of Space, Government of India",
         url="https://www.isro.gov.in", category="governance", priority=6),
    dict(id="thefederal", short="The Federal", name="The Federal", publisher="The Federal (news, third party)",
         url="https://thefederal.com", category="transport-energy", priority=25,
         notes="Third-party. Replace with an NPCIL or Department of Atomic Energy status page once linked."),
    dict(id="theprint", short="ThePrint", name="ThePrint", publisher="ThePrint (news, third party)",
         url="https://theprint.in", category="transport-energy", priority=26, notes="Third-party."),
]
added = 0
for s in NEW:
    if s["id"] not in have:
        src.append(s); added += 1
json.dump(src, open(P, "w"), ensure_ascii=False, indent=2)
print("sources added", added, "total", len(src))
