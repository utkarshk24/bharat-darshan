"""Officeholder changes checked on 24 Oct 2026 — patches only the affected cards (other cards keep their own asOf).
The same values are mirrored in or_core.py, kl_core.py and tn_core.py so a full re-run gives the same result.
Run with BD_TODAY=2026-10-24."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

OR_GOV = office("governor", L("Braj Mohan Ram", "ब्रज मोहन राम", "ब्रज मोहन राम"), None, "2026-10-18",
                "theprint", "https://theprint.in/india/bjp-leader-braj-mohan-ram-takes-oath-as-odisha-governor/3075069/", "https://rajbhavanodisha.gov.in",
                conf="Third-party verified",
                note="Appointed by the President on 12 October 2026 and sworn in as the 28th Governor of Odisha at Lok Bhavan, Bhubaneswar, on 18 October 2026 by Orissa High Court Chief Justice Harish Tandon (ThePrint / PTI). Three-time Lok Sabha member from Palamu, Jharkhand. Succeeded Dr Hari Babu Kambhampati (Governor from 3 January 2025).")
KL_GOV = office("governor", L("Om Prakash Mathur", "ओम प्रकाश माथुर", "ओम प्रकाश माथुर"), None, "2026-10-23",
                "etv-bharat", "https://www.etvbharat.com/en/state/om-prakash-mathur-sworn-in-as-29th-governor-of-keralam-enn26102302966", "https://igod.gov.in",
                conf="Third-party verified",
                note="Previously Governor of Sikkim. Appointed by the President on 12 October 2026 and sworn in as the 29th Governor of Keralam at the Lok Bhavan auditorium, Thiruvananthapuram, on 23 October 2026 by Chief Justice Soumen Sen of the Keralam High Court (ETV Bharat). Succeeded Rajendra Vishwanath Arlekar, who moved to Tamil Nadu.")
TN_NOTE = (" On 15 October 2026 he formally assumed charge as the full-time Governor of Tamil Nadu at Lok Bhavan, Chennai (UNI), after the President's appointment of 12 October;"
           " Om Prakash Mathur succeeded him in Keralam on 23 October 2026.")


def main():
    for code, gov in (("IN-OR", OR_GOV), ("IN-KL", KL_GOV)):
        r = read(f"regions/{code}.json")
        r["government"]["headOfState"] = gov
        r["meta"]["lastUpdated"] = TODAY
        write(f"regions/{code}.json", r)

    r = read("regions/IN-TN.json")
    h = r["government"]["headOfState"]
    if "15 October 2026" not in h["note"]:
        h["note"] = h["note"].rstrip() + TN_NOTE
    h["asOf"] = TODAY
    r["meta"]["lastUpdated"] = TODAY
    write("regions/IN-TN.json", r)
    print("officeholder updates ok")


if __name__ == "__main__":
    main()
