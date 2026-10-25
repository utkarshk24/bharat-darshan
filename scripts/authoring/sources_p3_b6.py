"""Add the sources used for Phase 3 batch 6 (Sikkim, Arunachal Pradesh, Nagaland, Manipur, Meghalaya) — idempotent."""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "sources.json")
src = json.load(open(P))
have = {s["id"] for s in src}

NEW = [
    dict(id="sk-gov", short="Govt of Sikkim", name="Government of Sikkim — notifications", publisher="Government of Sikkim",
         url="https://sikkim.gov.in", category="governance", priority=5),
    dict(id="ar-governor", short="Lok Bhavan Arunachal", name="Office of the Governor of Arunachal Pradesh — press releases", publisher="Lok Bhavan (Raj Bhavan), Itanagar",
         url="https://arunachalgovernor.gov.in", category="governance", priority=5),
    dict(id="ml-governor", short="Lok Bhavan Meghalaya", name="Office of the Governor of Meghalaya — press releases", publisher="Lok Bhavan (Raj Bhavan), Shillong",
         url="https://meggovernor.gov.in", category="governance", priority=5),
    dict(id="mn-assembly", short="Manipur Assembly", name="Manipur Legislative Assembly — bulletins", publisher="Manipur Legislative Assembly Secretariat",
         url="https://assembly.mn.gov.in", category="governance", priority=5),
    dict(id="eastmojo", short="EastMojo", name="EastMojo", publisher="EastMojo (news, third party)",
         url="https://eastmojo.com", category="governance", priority=27, notes="Third-party."),
    dict(id="eastern-mirror", short="Eastern Mirror", name="Eastern Mirror", publisher="Eastern Mirror, Nagaland (news, third party)",
         url="https://www.easternmirrornagaland.com", category="governance", priority=27, notes="Third-party."),
    dict(id="morung-express", short="Morung Express", name="The Morung Express", publisher="The Morung Express, Nagaland (news, third party)",
         url="https://morungexpress.com", category="governance", priority=27, notes="Third-party (often IANS/PTI copy)."),
]
added = 0
for s in NEW:
    if s["id"] not in have:
        src.append(s); added += 1
json.dump(src, open(P, "w"), ensure_ascii=False, indent=2)
print("sources added", added, "total", len(src))
