"""Haryana — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-24."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
CAG_HR = "https://cag.gov.in/uploads/download_audit_report/2026/Chapter-1-Overview-of-Finances-of-the-State-06a97fa816bb794.11409406.pdf"
FRBM_HR = "https://cms.neva.gov.in/NeVA/HR/FileStructure/PaperLaid/14/18/14_18_O_1413_V1.pdf"
GOV = "https://lokbhavan.haryana.gov.in/?p=19662"
CM = "https://www.theweek.in/wire-updates/national/2024/10/17/del48-hr-saini-5thld-oath.html"
SPK = "https://www.tribuneindia.com/news/top-headlines/three-time-mla-harvinder-kalyan-is-haryana-speaker"
DWARKA = "https://pmindia.gov.in/?p=16403991"

C = research("census_b5plus.json")
r = read("regions/IN-HR.json")
m = r["metrics"]
p = C["pop"]["HR"]
m["population2011"] = dp(p[0], "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 1,34,94,734; females 1,18,56,728.")
m["area"] = dp(44212, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(573, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 2,53,51,462 ÷ area 44,212 km² = 573.4.")
m["sexRatio2011"] = dp(879, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (861 in 2001).")
m["childSexRatio2011"] = dp(834, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 819 in 2001.")
m["literacyRate2011"] = dp(75.6, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(1213951, "₹ crore", "FY2024-25", "fy", "cag", CAG_HR, rev="provisional", base=CUR,
    note="CAG, State Finances Audit Report of Haryana for 2024-25, chapter 1 (Table 1.2): GSDP at current prices ₹12,13,951 crore, 11.83% above FY2023-24 (₹10,85,510 crore). MoSPI's state-wise API returned no Haryana series at access time, so the CAG figure is used; the estimate type is not stated in the chapter read.")
m["perCapitaNsdpCurrent"] = dp(325759, "₹", "FY2023-24", "fy", "hr-finance", FRBM_HR, rev="provisional", base=CUR,
    note="Per capita income at current prices, FY2023-24 advance estimate (₹2,96,592 in FY2022-23), from the Haryana Finance Department's Statements of Fiscal Policy laid with Budget 2024-25. Per capita income here is per capita NSDP. A FY2024-25 figure from an official source was not reached.")
m["forestCoverPct"] = dp(3.65, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 1,614.26 km² ÷ geographical area 44,212 km².")

r["officialPortal"] = "https://haryana.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Blackbuck", "काला हिरण", "काळवीट", "Antilope cervicapra"),
    "bird": sym("Black francolin", "काला तीतर", "काळा तित्तर", "Francolinus francolinus"),
    "tree": sym("Peepal", "पीपल", "पिंपळ", "Ficus religiosa"),
    "flower": sym("Lotus", "कमल", "कमळ", "Nelumbo nucifera"),
}

r["government"] = {
    "headOfState": office("governor", L("Ashim Kumar Ghosh", "असीम कुमार घोष", "असीम कुमार घोष"), None, "2025-07-21",
                          "hr-lokbhavan", GOV, "https://lokbhavan.haryana.gov.in",
                          note="Sworn in as the 19th Governor of Haryana on 21 July 2025 at Raj Bhavan, Chandigarh, by Chief Justice Sheel Nagu of the Punjab and Haryana High Court; succeeded Bandaru Dattatreya (Lok Bhavan Haryana)."),
    "headOfGovernment": office("chief-minister", L("Nayab Singh Saini", "नायब सिंह सैनी", "नायबसिंह सैनी"), "BJP", "2024-10-17",
                               "the-week", CM, "https://haryana.gov.in", conf="Third-party verified",
                               note="Sworn in for a second time on 17 October 2024 at the Dussehra ground in Panchkula by Governor Bandaru Dattatreya, with 13 ministers (PTI via The Week). He first became Chief Minister in March 2024, succeeding Manohar Lal; MLA from Ladwa."),
    "others": [
        office("speaker", L("Harvinder Kalyan", "हरविंद्र कल्याण", "हरविंदर कल्याण"), "BJP", "2024-10-25", "tribune", SPK, "https://haryanaassembly.gov.in", conf="Third-party verified",
               note="Elected unopposed as Speaker of the 15th Haryana Vidhan Sabha on 25 October 2024; MLA from Gharaunda (The Tribune)."),
    ],
}

r["projects"] = [
    proj("dwarka-expressway-hr", L("Dwarka Expressway, Haryana section", "द्वारका एक्सप्रेसवे, हरियाणा खंड", "द्वारका द्रुतगती मार्ग, हरियाणा टप्पा"),
         L("The 19-km, eight-lane Haryana section of the Dwarka Expressway, from the Delhi–Haryana border to Kherki Daula, built in two packages (10.2 km to the Basai rail-over-bridge and 8.7 km on to Kherki Daula) at about ₹4,100 crore. It gives Gurugram direct links to IGI Airport and the Gurugram bypass. Inaugurated by the Prime Minister on 11 March 2024, the same day the foundation stone of the Shamli–Ambala highway was laid.",
           "द्वारका एक्सप्रेसवे का 19 किमी लंबा आठ-लेन हरियाणा खंड, दिल्ली–हरियाणा सीमा से खेड़की दौला तक, जो लगभग ₹4,100 करोड़ की लागत से दो पैकेज में बना (बसई रेल ओवरब्रिज तक 10.2 किमी और आगे खेड़की दौला तक 8.7 किमी)। यह गुरुग्राम को आईजीआई हवाई अड्डे और गुरुग्राम बाईपास से सीधे जोड़ता है। प्रधानमंत्री ने 11 मार्च 2024 को इसका उद्घाटन किया; उसी दिन शामली–अंबाला राजमार्ग की आधारशिला रखी गई।",
           "द्वारका द्रुतगती मार्गाचा 19 किमी लांबीचा आठपदरी हरियाणा टप्पा, दिल्ली–हरियाणा सीमेपासून खेडकी दौलापर्यंत, जो सुमारे ₹4,100 कोटी खर्चून दोन पॅकेजमध्ये बांधला गेला (बसई रेल्वे उड्डाणपुलापर्यंत 10.2 किमी व पुढे खेडकी दौलापर्यंत 8.7 किमी). तो गुरुग्रामला आयजीआय विमानतळ व गुरुग्राम बायपासशी थेट जोडतो. पंतप्रधानांनी 11 मार्च 2024 रोजी त्याचे उद्घाटन केले; त्याच दिवशी शामली–अंबाला महामार्गाची पायाभरणी झाली."),
         "transport", "National Highways Authority of India", 4100, "About ₹4,100 crore (PMIndia).", "2024", None, "11 March 2024", "Completed", "pmindia", DWARKA),
]

GI_NAMES = {
 "Basmati": ("बासमती", "बासमती"),
 "Phulkari": ("फुलकारी", "फुलकारी"),
}
SHARED = {"PB,HR,HP,DL,UK,UP,JK": ["Punjab", "Himachal Pradesh", "Delhi", "Uttarakhand", "Uttar Pradesh", "Jammu & Kashmir"],
          "PB,HR,RJ": ["Punjab", "Rajasthan"]}
r["giProducts"] = gi_list("gi_hr.tsv", GI_NAMES, SHARED, {"Phulkari"})
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-HR.json", r)
print("hr core ok", len(r["giProducts"]), "GIs")
