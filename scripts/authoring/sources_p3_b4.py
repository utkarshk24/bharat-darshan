"""Add the sources used for Phase 3 batch 4 (Odisha, Jharkhand, Chhattisgarh, Assam, Punjab) — idempotent."""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "sources.json")
src = json.load(open(P))
have = {s["id"] for s in src}

NEW = [
    dict(id="deccan-herald", short="Deccan Herald", name="Deccan Herald", publisher="Deccan Herald (news, third party)",
         url="https://www.deccanherald.com", category="governance", priority=27, notes="Third-party (PTI copy). Replace with the official page in review."),
    dict(id="thestatesman", short="The Statesman", name="The Statesman", publisher="The Statesman (news, third party)",
         url="https://www.thestatesman.com", category="governance", priority=27, notes="Third-party."),
    dict(id="hitavada", short="The Hitavada", name="The Hitavada", publisher="The Hitavada (news, third party)",
         url="https://www.thehitavada.com", category="governance", priority=27, notes="Third-party."),
    dict(id="odishabytes", short="OdishaBytes", name="OdishaBytes", publisher="OdishaBytes (news, third party)",
         url="https://odishabytes.com", category="governance", priority=27, notes="Third-party."),
    dict(id="new-india-samachar", short="New India Samachar", name="New India Samachar (fortnightly)", publisher="Press Information Bureau, Government of India",
         url="https://newindiasamachar.pib.gov.in", category="governance", priority=6),
]
added = 0
for s in NEW:
    if s["id"] not in have:
        src.append(s); added += 1
json.dump(src, open(P, "w"), ensure_ascii=False, indent=2)
print("sources added", added, "total", len(src))
