"""Jharkhand — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-16."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.newsonair.gov.in/santosh-kumar-gangwar-takes-oath-as-governor-of-jharkhand"
CM = "https://www.newsonair.gov.in/hemant-soren-to-be-sworn-in-as-jharkhand-cm-tomorrow"
SPK = "https://www.newsonair.gov.in/jmm-leader-rabindra-nath-mahto-re-elected-unanimously-as-speaker-of-jharkhand-legislative-assembly"
DGH = "https://newindiasamachar.pib.gov.in/WriteReadData/flipbook/2022/Aug/1st/English/files/basic-html/page14.html"

mo = research("mospi_jh.json")
r = read("regions/IN-JH.json")
m = r["metrics"]
m["population2011"] = dp(32988134, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 1,69,30,315; females 1,60,57,819.")
m["area"] = dp(79716, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(414, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 3,29,88,134 ÷ area 79,716 km² = 413.8.")
m["sexRatio2011"] = dp(948, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (941 in 2001).")
m["childSexRatio2011"] = dp(948, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 965 in 2001.")
m["literacyRate2011"] = dp(66.4, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25 is the latest year published for Jharkhand. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2023-24: ₹{inr(mo['pcnsdp']['FY2023-24'][0])}.")
m["forestCoverPct"] = dp(29.81, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 23,765.78 km² ÷ geographical area 79,716 km².")

r["officialPortal"] = "https://www.jharkhand.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Asian elephant", "हाथी", "हत्ती", "Elephas maximus"),
    "bird": sym("Asian koel", "कोयल", "कोकिळा", "Eudynamys scolopaceus"),
    "flower": sym("Palash (flame of the forest)", "पलाश", "पळस", "Butea monosperma"),
    "tree": sym("Sal", "साल", "साल", "Shorea robusta"),
}

r["government"] = {
    "headOfState": office("governor", L("Santosh Kumar Gangwar", "संतोष कुमार गंगवार", "संतोष कुमार गंगवार"), None, "2024-07-31",
                          "newsonair", GOV, "https://www.jharkhand.gov.in",
                          note="Former Union Minister. Sworn in at Raj Bhavan, Ranchi, on 31 July 2024 by the acting Chief Justice of the Jharkhand High Court, Sujit Narayan Prasad (News On AIR)."),
    "headOfGovernment": office("chief-minister", L("Hemant Soren", "हेमंत सोरेन", "हेमंत सोरेन"), "JMM", "2024-11-28",
                               "newsonair", CM, "https://www.jharkhand.gov.in",
                               note="Sworn in for a fourth term on 28 November 2024 at Morhabadi Maidan, Ranchi, after the INDIA bloc won 56 of the 81 Assembly seats (News On AIR)."),
    "others": [
        office("speaker", L("Rabindra Nath Mahato", "रवींद्र नाथ महतो", "रवींद्र नाथ महतो"), "JMM", "2024-12-10", "newsonair", SPK, "https://jharkhandvidhansabha.nic.in",
               note="Re-elected unanimously as Speaker of the sixth Assembly on 10 December 2024 — his second term (News On AIR)."),
    ],
}

r["projects"] = [
    proj("deoghar-airport", L("Deoghar Airport", "देवघर हवाई अड्डा", "देवघर विमानतळ"),
         L("Jharkhand's second commercial airport, built under the UDAN regional connectivity scheme near the Baba Baidyanath Dham pilgrimage town. The Prime Minister inaugurated it on 12 July 2022, when commercial flights also began.",
           "उड़ान क्षेत्रीय संपर्क योजना के तहत बाबा बैद्यनाथ धाम तीर्थ नगर के पास बना झारखंड का दूसरा व्यावसायिक हवाई अड्डा। प्रधानमंत्री ने 12 जुलाई 2022 को इसका उद्घाटन किया, जिस दिन व्यावसायिक उड़ानें भी शुरू हुईं।",
           "उडान प्रादेशिक संपर्क योजनेअंतर्गत बाबा बैद्यनाथ धाम तीर्थक्षेत्राजवळ उभारलेले झारखंडचे दुसरे व्यावसायिक विमानतळ. पंतप्रधानांनी 12 जुलै 2022 रोजी त्याचे उद्घाटन केले, त्याच दिवशी व्यावसायिक उड्डाणेही सुरू झाली."),
         "aviation", "Airports Authority of India", None, None, None, None, "12 July 2022", "Completed", "new-india-samachar", DGH),
]

GI_NAMES = {"Sohrai – Khovar Painting": ("सोहराय – खोवर चित्रकला", "सोहराय – खोवर चित्रकला")}
r["giProducts"] = gi_list("gi_jh.tsv", GI_NAMES, {}, set())
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-JH.json", r)
print("jh core ok", len(r["giProducts"]), "GIs")
