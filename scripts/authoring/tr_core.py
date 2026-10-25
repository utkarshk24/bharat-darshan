"""Tripura — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.sentinelassam.com/amp/story/north-east-india-news/tripura-news/tripura-indra-sena-reddy-nallu-sworn-in-as-20th-governor-672580"
CM = "https://www.theweek.in/news/india/2023/03/08/manik-saha-takes-oath-as-tripura-cm-8-ministers-also-sworn-in.amp.html"
SPK_DEATH = "https://www.deccanherald.com/india/tripura/tripura-assembly-speaker-biswa-bandhu-sen-dies-at-72-3843164"

mo = research("mospi_tr.json")
C = research("census_b5plus.json")
r = read("regions/IN-TR.json")
m = r["metrics"]
p = C["pop"]["TR"]
m["population2011"] = dp(p[0], "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 18,74,376; females 17,99,541.")
m["area"] = dp(10486, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(350, "persons per km²", "2011", "census", "census", PYD, note="Calculated: Census 2011 population 36,73,917 ÷ area 10,486 km² = 350.4.")
m["sexRatio2011"] = dp(960, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (948 in 2001).")
m["childSexRatio2011"] = dp(957, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 966 in 2001.")
m["literacyRate2011"] = dp(87.2, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25 is the latest year published for Tripura. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2023-24: ₹{inr(mo['pcnsdp']['FY2023-24'][0])}.")
m["forestCoverPct"] = dp(72.33, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 7,584.77 km² ÷ geographical area 10,486 km².")
r["officialPortal"] = "https://tripura.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Phayre's leaf monkey", "फ़ेयर का पत्ती बंदर", "फेअरचे पानमाकड", "Trachypithecus phayrei"),
    "bird": sym("Green imperial pigeon", "हरा शाही कबूतर", "हिरवे शाही कबूतर", "Ducula aenea"),
    "flower": sym("Nageshwar", "नागकेसर", "नागचाफा", "Mesua ferrea"),
    "tree": sym("Agarwood", "अगर", "अगर", "Aquilaria malaccensis"),
}

r["government"] = {
    "headOfState": office("governor", L("N. Indrasena Reddy", "एन. इंद्रसेना रेड्डी", "एन. इंद्रसेना रेड्डी"), None, "2023-10-26",
                          "sentinel-assam", GOV, "https://rajbhavan.tripura.gov.in", conf="Third-party verified",
                          note="Sworn in as the 20th Governor of Tripura at Raj Bhavan, Agartala, by Chief Justice Aparesh Kumar Singh of the Tripura High Court, succeeding Satyadeo Narain Arya (The Sentinel, 26 Oct 2023)."),
    "headOfGovernment": office("chief-minister", L("Manik Saha", "माणिक साहा", "माणिक साहा"), "BJP", "2023-03-08",
                               "the-week", CM, "https://tripura.gov.in", conf="Third-party verified",
                               note="Sworn in for a second term on 8 March 2023 after the BJP-led alliance won the 2023 Assembly election (The Week/PTI). He first became Chief Minister in May 2022."),
    "others": [
        office_todo("speaker", "deccan-herald", "https://tripura.gov.in",
                    "Speaker Biswa Bandhu Sen died on 26 December 2025 (Deccan Herald/PTI). His successor is to be confirmed from the Tripura Legislative Assembly before a name is shown."),
    ],
}

r["projects"] = []

GI_NAMES = {
 "Tripura Queen Pineapple": ("त्रिपुरा क्वीन अनानास", "त्रिपुरा क्वीन अननस"),
 "Tripura Matabari Peda": ("त्रिपुरा माताबाड़ी पेड़ा", "त्रिपुरा माताबाडी पेढा"),
 "Tripura Risa Textile": ("त्रिपुरा रिसा वस्त्र", "त्रिपुरा रिसा वस्त्र"),
 "Tripura Pachra-Rignai Textile": ("त्रिपुरा पाछरा-रिग्नाई वस्त्र", "त्रिपुरा पाछरा-रिग्नाई वस्त्र"),
}
r["giProducts"] = gi_list("gi_tr.tsv", GI_NAMES, {}, {"Tripura Risa Textile", "Tripura Pachra-Rignai Textile"})
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-TR.json", r)
print("tr core ok", len(r["giProducts"]), "GIs")
