"""Add the sources used for Phase 3 batch 5 (Haryana, Himachal Pradesh, Uttarakhand, Jammu and Kashmir, Goa) — idempotent."""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "sources.json")
src = json.load(open(P))
have = {s["id"] for s in src}

NEW = [
    dict(id="hr-lokbhavan", short="Lok Bhavan Haryana", name="Lok Bhavan (Raj Bhavan), Haryana", publisher="Office of the Governor of Haryana",
         url="https://lokbhavan.haryana.gov.in", category="governance", priority=5),
    dict(id="hr-finance", short="Haryana Finance Dept.", name="Haryana Finance Department — FRBM statements laid in the Vidhan Sabha", publisher="Government of Haryana (via NeVA)",
         url="https://cms.neva.gov.in", category="economy", priority=6),
    dict(id="goa-dip", short="DIP Goa", name="Department of Information and Publicity, Goa", publisher="Government of Goa",
         url="https://dip.goa.gov.in", category="governance", priority=5),
    dict(id="jk-des", short="DES J&K", name="Directorate of Economics and Statistics, Jammu and Kashmir", publisher="Planning, Development & Monitoring Department, Government of Jammu and Kashmir",
         url="https://ecostatjk.nic.in", category="demographics", priority=5),
    dict(id="jk-planning", short="J&K Planning", name="Planning, Development & Monitoring Department, Jammu and Kashmir", publisher="Government of Jammu and Kashmir",
         url="https://jkplanning.gov.in", category="governance", priority=6),
    dict(id="deccan-chronicle", short="Deccan Chronicle", name="Deccan Chronicle", publisher="Deccan Chronicle (news, third party)",
         url="https://www.deccanchronicle.com", category="governance", priority=27, notes="Third-party."),
    dict(id="the-week", short="The Week", name="The Week (PTI wire)", publisher="The Week (news, third party)",
         url="https://www.theweek.in", category="governance", priority=27, notes="Third-party (PTI copy)."),
    dict(id="kashmir-life", short="Kashmir Life", name="Kashmir Life", publisher="Kashmir Life (news, third party)",
         url="https://kashmirlife.net", category="governance", priority=27, notes="Third-party."),
    dict(id="kashmir-reader", short="Kashmir Reader", name="Kashmir Reader", publisher="Kashmir Reader (news, third party)",
         url="https://kashmirreader.com", category="governance", priority=27, notes="Third-party."),
    dict(id="the-goan", short="The Goan", name="The Goan", publisher="The Goan (news, third party)",
         url="https://www.thegoan.net", category="governance", priority=27, notes="Third-party."),
    dict(id="drishti", short="Drishti IAS", name="Drishti IAS current affairs", publisher="Drishti IAS (third party)",
         url="https://www.drishtiias.com", category="governance", priority=28, notes="Third-party summary; replace with the Vidhan Sabha notice in review."),
]
added = 0
for s in NEW:
    if s["id"] not in have:
        src.append(s); added += 1
json.dump(src, open(P, "w"), ensure_ascii=False, indent=2)
print("sources added", added, "total", len(src))
