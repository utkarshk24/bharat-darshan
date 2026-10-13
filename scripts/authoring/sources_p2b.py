"""Add the sources used for Keralam, Delhi and Ladakh (idempotent)."""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "sources.json")
src = json.load(open(P))
have = {s["id"] for s in src}

NEW = [
    dict(id="kl-spb", short="Kerala State Planning Board", name="Economic Review (Kerala State Planning Board)",
         publisher="Kerala State Planning Board, Government of Kerala", url="https://spb.kerala.gov.in", category="economy", priority=4,
         notes="State-published compilation of Census 2011 and economic data."),
    dict(id="kl-gov", short="Government of Kerala", name="Government of Kerala portal", publisher="Government of Kerala",
         url="https://kerala.gov.in", category="governance", priority=7),
    dict(id="prs", short="PRS Legislative Research", name="PRS Bill Track", publisher="PRS Legislative Research (independent, non-profit)",
         url="https://prsindia.org", category="governance", priority=10,
         notes="Independent tracker of Parliament's legislative record; used for bill dates."),
    dict(id="onmanorama", short="Onmanorama", name="Onmanorama (Malayala Manorama)", publisher="Malayala Manorama (news, third party)",
         url="https://www.onmanorama.com", category="governance", priority=20,
         notes="Third-party. Replace with the Gazette of India notification once linked."),
    dict(id="keralakaumudi", short="Kerala Kaumudi", name="Kerala Kaumudi", publisher="Kerala Kaumudi (news, third party)",
         url="https://keralakaumudi.com", category="governance", priority=21, notes="Third-party."),
    dict(id="uni", short="UNI", name="United News of India", publisher="United News of India (news agency, third party)",
         url="https://www.uniindia.com", category="governance", priority=22, notes="Third-party."),
    dict(id="cag", short="CAG", name="Comptroller and Auditor General of India — State Finances Audit Report",
         publisher="Office of the Comptroller and Auditor General of India", url="https://cag.gov.in", category="economy", priority=7),
    dict(id="pmindia", short="PMO", name="Prime Minister's Office — news updates", publisher="Prime Minister's Office",
         url="https://www.pmindia.gov.in", category="governance", priority=6),
    dict(id="dl-planning", short="Economic Survey of Delhi", name="Economic Survey of Delhi 2023-24",
         publisher="Planning Department, Government of NCT of Delhi", url="https://delhiplanning.delhi.gov.in", category="economy", priority=4),
    dict(id="dl-gov", short="Government of NCT of Delhi", name="Government of NCT of Delhi portal",
         publisher="Government of NCT of Delhi", url="https://delhi.gov.in", category="governance", priority=7),
    dict(id="dl-lg", short="Lok Niwas, Delhi", name="Office of the Lieutenant Governor, Delhi", publisher="Lok Niwas, Delhi",
         url="https://lg.delhi.gov.in", category="governance", priority=8),
    dict(id="pioneer", short="The Pioneer", name="The Pioneer", publisher="The Pioneer (news, third party)",
         url="https://www.dailypioneer.com", category="governance", priority=23, notes="Third-party."),
    dict(id="tribune", short="The Tribune", name="The Tribune", publisher="The Tribune (news, third party)",
         url="https://www.tribuneindia.com", category="governance", priority=24, notes="Third-party."),
    dict(id="la-gov", short="UT Administration of Ladakh", name="Union Territory of Ladakh portal",
         publisher="Administration of Union Territory of Ladakh", url="https://ladakh.gov.in", category="governance", priority=7),
    dict(id="kargil-nic", short="District Kargil", name="District Kargil — Demography", publisher="District Administration Kargil",
         url="https://kargil.nic.in", category="demographics", priority=5),
    dict(id="ncrtc", short="NCRTC", name="National Capital Region Transport Corporation", publisher="NCRTC (Government of India and participating States)",
         url="https://ncrtc.in", category="transport-energy", priority=9),
    dict(id="dmrc", short="DMRC", name="Delhi Metro Rail Corporation", publisher="DMRC (Government of India and GNCTD)",
         url="https://www.delhimetrorail.com", category="transport-energy", priority=9),
]
added = 0
for s in NEW:
    if s["id"] not in have:
        src.append(s); added += 1
json.dump(src, open(P, "w"), ensure_ascii=False, indent=2)
print("sources added", added, "total", len(src))
