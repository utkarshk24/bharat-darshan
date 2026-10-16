"""Chhattisgarh — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-16."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.thestatesman.com/india/ramen-deka-sworn-in-as-the-10th-governor-of-chhattisgarh-1503326677.html"
CM = "https://www.deccanherald.com/amp/story/india%2Fchhattisgarh%2Fbjps-vishnu-deo-sai-takes-oath-as-chhattisgarh-chief-minister-2809340"
CAB = "https://www.newsonair.gov.in/chhattisgarh-cabinet-expanded-gajendra-yadav-rajesh-agrawal-and-guru-khushwant-saheb-sworn-in-as-ministers"
SPK = "https://thehitavada.com/Encyc/2023/12/20/Dr-Raman-Singh-New-Speaker-of-C-garh-Assembly.html"
BASTAR = "https://www.newsonair.gov.in/pm-narendra-modi-launches-27-thousand-crore-rupee-development-projects-in-chhattisgarh"

mo = research("mospi_ct.json")
r = read("regions/IN-CT.json")
m = r["metrics"]
m["population2011"] = dp(25545198, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 1,28,32,895; females 1,27,12,303.")
m["area"] = dp(135192, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(189, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 2,55,45,198 ÷ area 1,35,192 km² = 189.0.")
m["sexRatio2011"] = dp(991, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (989 in 2001).")
m["childSexRatio2011"] = dp(969, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 975 in 2001.")
m["literacyRate2011"] = dp(70.3, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25: ₹{inr(mo['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(mo['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(41.28, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 55,811.75 km² ÷ geographical area 1,35,192 km².")

r["officialPortal"] = "https://cgstate.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Wild water buffalo", "वन भैंसा", "रानरेडा (जंगली म्हैस)", "Bubalus arnee"),
    "bird": sym("Hill myna", "पहाड़ी मैना", "पहाडी मैना", "Gracula religiosa"),
    "tree": sym("Sal", "साल", "साल", "Shorea robusta"),
}

r["government"] = {
    "headOfState": office("governor", L("Ramen Deka", "रमेन डेका", "रमेन डेका"), None, "2024-07-31",
                          "thestatesman", GOV, "https://rajbhavancg.gov.in", conf="Third-party verified",
                          note="Former Lok Sabha MP from Assam. Sworn in as the 10th Governor of Chhattisgarh in the Darbar Hall of Raj Bhavan, Raipur, on 31 July 2024 by Chief Justice Ramesh Sinha (The Statesman). Appointment by the President announced on 27–28 July 2024 (News On AIR)."),
    "headOfGovernment": office("chief-minister", L("Vishnu Deo Sai", "विष्णु देव साय", "विष्णुदेव साय"), "BJP", "2023-12-13",
                               "deccan-herald", CM, "https://cgstate.gov.in", conf="Third-party verified",
                               note="Sworn in on 13 December 2023 at the Science College ground, Raipur (Deccan Herald / PTI). News On AIR's report of the cabinet expansion of 20 August 2025 confirms him as Chief Minister."),
    "others": [
        office("deputy-chief-minister", L("Arun Sao", "अरुण साव", "अरुण साव"), "BJP", "2023-12-13", "newsonair", CAB, "https://cgstate.gov.in",
               note="Sworn in with the Chief Minister on 13 December 2023; named as Deputy Chief Minister in News On AIR's report of 20 August 2025."),
        office("deputy-chief-minister", L("Vijay Sharma", "विजय शर्मा", "विजय शर्मा"), "BJP", "2023-12-13", "newsonair", CAB, "https://cgstate.gov.in",
               note="Sworn in with the Chief Minister on 13 December 2023; named as Deputy Chief Minister in News On AIR's report of 20 August 2025."),
        office("speaker", L("Raman Singh", "रमन सिंह", "रमण सिंह"), "BJP", "2023-12-19", "hitavada", SPK, "https://cgvidhansabha.gov.in", conf="Third-party verified",
               note="Former three-term Chief Minister; elected Speaker on the first day of the sixth Assembly's first session (The Hitavada, 20 December 2023). Confirm the date on the Assembly website."),
    ],
}

r["projects"] = [
    proj("nagarnar-steel", L("NMDC steel plant, Nagarnar", "एनएमडीसी इस्पात संयंत्र, नगरनार", "एनएमडीसी पोलाद कारखाना, नगरनार"),
         L("A greenfield integrated steel plant built by the public-sector NMDC at Nagarnar near Jagdalpur in Bastar, using iron ore from Bailadila. The Prime Minister dedicated it to the nation on 3 October 2023.",
           "बस्तर में जगदलपुर के पास नगरनार में सार्वजनिक क्षेत्र के एनएमडीसी द्वारा बैलाडीला के लौह अयस्क से बना नया एकीकृत इस्पात संयंत्र। प्रधानमंत्री ने 3 अक्टूबर 2023 को इसे राष्ट्र को समर्पित किया।",
           "बस्तरमध्ये जगदलपूरजवळ नगरनार येथे सार्वजनिक क्षेत्रातील एनएमडीसीने बैलाडिलाच्या लोहखनिजावर उभारलेला नवा एकात्मिक पोलाद कारखाना. पंतप्रधानांनी 3 ऑक्टोबर 2023 रोजी तो राष्ट्राला समर्पित केला."),
         "industry", "NMDC Limited", 24000, "About ₹24,000 crore (News On AIR).", "2023", None, "3 October 2023", "Completed", "newsonair", BASTAR),
    proj("antagarh-taroki", L("Antagarh–Taroki new rail line", "अंतागढ़–तारोकी नई रेल लाइन", "अंतागड–तारोकी नवा रेल्वेमार्ग"),
         L("A section of the new railway line being built into north Bastar from Dalli Rajhara towards Rowghat and Jagdalpur. The Prime Minister dedicated the Antagarh–Taroki stretch on 3 October 2023, along with the doubled Jagdalpur–Dantewada line, and flagged off a Taroki–Raipur train.",
           "दल्ली राजहरा से रावघाट और जगदलपुर की ओर उत्तर बस्तर में बन रही नई रेल लाइन का एक खंड। प्रधानमंत्री ने 3 अक्टूबर 2023 को दोहरी जगदलपुर–दंतेवाड़ा लाइन के साथ अंतागढ़–तारोकी खंड राष्ट्र को समर्पित किया और तारोकी–रायपुर ट्रेन को हरी झंडी दिखाई।",
           "दल्ली राजहराहून रावघाट व जगदलपूरकडे उत्तर बस्तरमध्ये बांधल्या जाणाऱ्या नव्या रेल्वेमार्गाचा एक टप्पा. पंतप्रधानांनी 3 ऑक्टोबर 2023 रोजी दुहेरी जगदलपूर–दंतेवाडा मार्गासोबत अंतागड–तारोकी टप्पा राष्ट्राला समर्पित केला आणि तारोकी–रायपूर गाडीला हिरवा झेंडा दाखवला."),
         "rail", "Ministry of Railways", None, None, None, None, "3 October 2023", "Completed", "newsonair", BASTAR),
]

GI_NAMES = {
 "Jeeraphool": ("जीराफूल (चावल)", "जीराफूल (तांदूळ)"),
 "Nagri Dubraj": ("नगरी दुबराज (चावल)", "नगरी दुबराज (तांदूळ)"),
 "Bastar Iron Craft": ("बस्तर लौह शिल्प", "बस्तर लोखंडी हस्तकला"),
 "Bastar Dhokra": ("बस्तर ढोकरा", "बस्तर ढोकरा"),
 "Bastar Wooden Craft": ("बस्तर काष्ठ शिल्प", "बस्तर लाकडी हस्तकला"),
 "Champa Silk Saree And Fabrics": ("चांपा रेशम साड़ी और वस्त्र", "चांपा रेशीम साडी व वस्त्र"),
 "Bastar Dhokra (Logo)": ("बस्तर ढोकरा (लोगो)", "बस्तर ढोकरा (बोधचिन्ह)"),
}
TEXTILE = {"Champa Silk Saree And Fabrics"}
r["giProducts"] = gi_list("gi_ct.tsv", GI_NAMES, {}, TEXTILE)
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-CT.json", r)
print("ct core ok", len(r["giProducts"]), "GIs")
