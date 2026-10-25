"""Add the sources used for Phase 3 batch 7 (Mizoram, Tripura, A&N, Chandigarh, DNH&DD, Lakshadweep, Puducherry) — idempotent."""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "sources.json")
src = json.load(open(P))
have = {s["id"] for s in src}
NEW = [
    dict(id="mz-assembly", short="Mizoram Assembly", name="Mizoram Legislative Assembly — bulletins", publisher="Mizoram Legislative Assembly Secretariat",
         url="https://mizoramassembly.in", category="governance", priority=5),
    dict(id="py-assembly", short="Puducherry Assembly", name="Puducherry Legislative Assembly (NeVA portal)", publisher="Puducherry Legislative Assembly Secretariat",
         url="https://puddu.neva.gov.in", category="governance", priority=5),
    dict(id="ld-gov", short="UT Lakshadweep", name="Union Territory of Lakshadweep — official portal", publisher="Lakshadweep Administration",
         url="https://lakshadweep.gov.in", category="governance", priority=5),
    dict(id="sentinel-assam", short="Sentinel Assam", name="The Sentinel (Assam)", publisher="The Sentinel, Guwahati (news, third party)",
         url="https://www.sentinelassam.com", category="governance", priority=27, notes="Third-party."),
    dict(id="udayavani", short="Udayavani", name="Udayavani (English)", publisher="Udayavani (news, third party)",
         url="https://english.udayavani.com", category="governance", priority=27, notes="Third-party (PTI copy)."),
    dict(id="organiser", short="Organiser", name="Organiser", publisher="Organiser (news weekly, third party)",
         url="https://organiser.org", category="governance", priority=27, notes="Third-party."),
]
added = 0
for s in NEW:
    if s["id"] not in have:
        src.append(s); added += 1
json.dump(src, open(P, "w"), ensure_ascii=False, indent=2)
print("sources added", added, "total", len(src))
