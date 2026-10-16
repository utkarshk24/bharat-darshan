"""Add the sources used for Phase 3 batch 3 (Andhra Pradesh, Telangana, Rajasthan, Madhya Pradesh, Bihar) — idempotent."""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "sources.json")
src = json.load(open(P))
have = {s["id"] for s in src}

NEW = [
    dict(id="ap-cse", short="Educational Statistics, Andhra Pradesh", name="Educational Statistics 2017-18 (Commissionerate of School Education)",
         publisher="Government of Andhra Pradesh", url="https://cse.ap.gov.in", category="demographics", priority=9,
         notes="Gives Census 2011 figures recast for the residual (post-2014) State of Andhra Pradesh."),
    dict(id="ap-fin", short="Socio Economic Survey, Andhra Pradesh", name="Socio Economic Survey 2024-25 (Planning Department)",
         publisher="Government of Andhra Pradesh", url="https://apfinance.gov.in", category="economy", priority=8,
         notes="The PDF is served from the Finance Department's document store (apfinance.gov.in)."),
    dict(id="msme-di", short="MSME-DI State Profile", name="State Profile of Telangana 2015-16 (MSME-Development Institute, Hyderabad)",
         publisher="Ministry of MSME, Government of India", url="https://dcmsme.gov.in", category="demographics", priority=10,
         notes="Gives Census 2011 figures recast for the State of Telangana."),
    dict(id="tg-plan", short="Telangana Socio Economic Outlook", name="Telangana Socio Economic Outlook 2024 (Planning Department)",
         publisher="Government of Telangana", url="https://www.telangana.gov.in", category="economy", priority=8,
         notes="The PDF is linked from the OpenCity data portal copy of the Government of Telangana publication; replace with the State link in review."),
    dict(id="bihar-lokbhavan", short="Lok Bhavan, Bihar", name="Lok Bhavan (formerly Raj Bhavan), Bihar", publisher="Office of the Governor of Bihar",
         url="https://governor.bih.nic.in", category="governance", priority=8),
    dict(id="scroll", short="Scroll", name="Scroll.in", publisher="Scroll (news, third party)", url="https://scroll.in",
         category="governance", priority=27, notes="Third-party."),
    dict(id="thesouthfirst", short="The South First", name="The South First", publisher="The South First (news, third party)",
         url="https://thesouthfirst.com", category="governance", priority=27, notes="Third-party."),
    dict(id="fpj", short="Free Press Journal", name="Free Press Journal", publisher="Free Press Journal (news, third party)",
         url="https://www.freepressjournal.in", category="governance", priority=27, notes="Third-party."),
    dict(id="ians", short="IANS", name="Indo-Asian News Service (IANS)", publisher="IANS (news agency, third party)",
         url="https://ianslive.in", category="governance", priority=27, notes="Third-party. Replace with the Lok Bhavan page once available."),
    dict(id="etv-bharat", short="ETV Bharat", name="ETV Bharat", publisher="ETV Bharat (news, third party)",
         url="https://www.etvbharat.com", category="governance", priority=27, notes="Third-party."),
]
added = 0
for s in NEW:
    if s["id"] not in have:
        src.append(s); added += 1
json.dump(src, open(P, "w"), ensure_ascii=False, indent=2)
print("sources added", added, "total", len(src))
