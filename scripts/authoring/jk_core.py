"""Jammu and Kashmir (UT) — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-24."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

C = research("census_b5plus.json"); J = C["jk_ut"]
DES = J["url"]
JKP = "https://jkplanning.gov.in/profile.html"
LG = "https://kashmirreader.com/2020/08/07/manoj-sinha-takes-oath-as-new-lg-of-jammu-and-kashmir/"
CM = "https://www.etvbharat.com/amp/en/!bharat/omar-abdullah-sworn-in-as-jammu-and-kashmir-chief-minister-enn24101602274"
SPK = "https://www.etvbharat.com/en/!state/nc-leader-rahim-rather-elected-speaker-of-maiden-jammu-kashmir-ut-legislative-assembly-enn24110401547"
USBRL = "https://www.newsonair.gov.in/rail-network-connects-country-from-kashmir-to-kanyakumari-says-pm-modi"
DES_NOTE = "Directorate of Economics & Statistics, J&K, 'UT of Jammu & Kashmir at a Glance 2024-25' (Census 2011 figures for the area of the present Union Territory, excluding Leh and Kargil)."

mo = research("mospi_jk.json")
r = read("regions/IN-JK.json")
m = r["metrics"]
m["population2011"] = dp(J["pop"], "persons", "2011", "census", "jk-des", DES,
    note=f"{DES_NOTE} Males 64,83,906; females 57,83,107. The former State, including Ladakh, had 1,25,41,302 people.")
m["area"] = dp(J["area_km2"], "km²", "2011", "census", "jk-des", DES,
    note="Census 2011 geographical area of the present UT as given by the J&K DES (Jammu division 26,293 km², Kashmir division 15,948 km²). The UT's area including the areas under the occupation of Pakistan (PoK) is 1,20,355 km² (J&K Planning Department).")
m["density2011"] = dp(J["density"], "persons per km²", "2011", "census", "jk-des", DES, note=DES_NOTE)
m["sexRatio2011"] = dp(J["sex_ratio"], "females per 1000 males", "2011", "census", "jk-des", DES, note=f"{DES_NOTE} The former State's figure was 889.")
m["childSexRatio2011"] = dp(J["csr"], "girls per 1000 boys (0–6 yrs)", "2011", "census", "jk-des", DES, note=f"{DES_NOTE} The former State's figure was 862 (941 in 2001).")
m["literacyRate2011"] = dp(J["literacy"], "%", "2011", "census", "jk-des", DES, note=f"{DES_NOTE} Jammu division 71.98%, Kashmir division 62.98%.")
m["urbanisation2011"] = dp(J["urban_pct"], "%", "2011", "census", "jk-des", DES, note=f"{DES_NOTE} Urban population 33,71,233; rural 88,95,780.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2025-26 is the latest year published for J&K. FY2024-25: ₹{inr(mo['gsdp']['FY2024-25'][0])} crore (the J&K DES gives ₹2,62,458 crore as its second advance estimate).")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(mo['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(None, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="ISFR 2023 puts J&K's forest cover at 21,346.39 km², but its geographical area (2,22,236 km²) covers the whole former State including areas under the occupation of Pakistan and China, so its percentage (9.6%) is not comparable with other regions; measured against the 42,241 km² used by the J&K DES it would be about 50%. Not shown until an agreed basis is chosen; see the Nature module.")

r["officialPortal"] = "https://jk.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Hangul (Kashmir stag)", "हंगुल (कश्मीरी बारहसिंगा)", "हंगुल (काश्मिरी बारशिंगा)", "Cervus hanglu hanglu"),
    "tree": sym("Chinar", "चिनार", "चिनार", "Platanus orientalis"),
}

r["government"] = {
    "headOfState": office("lieutenant-governor", L("Manoj Sinha", "मनोज सिन्हा", "मनोज सिन्हा"), None, "2020-08-07",
                          "kashmir-reader", LG, "https://jk.gov.in", conf="Third-party verified",
                          note="Sworn in as Lieutenant Governor at Raj Bhavan, Srinagar, on 7 August 2020 by Chief Justice Gita Mittal; succeeded Girish Chandra Murmu (Kashmir Reader). He addressed the Assembly's budget session in 2026 as Lieutenant Governor (News On AIR)."),
    "headOfGovernment": office("chief-minister", L("Omar Abdullah", "उमर अब्दुल्ला", "उमर अब्दुल्ला"), "JKNC", "2024-10-16",
                               "etv-bharat", CM, "https://jk.gov.in", conf="Third-party verified",
                               note="Sworn in on 16 October 2024 at the Sher-i-Kashmir International Convention Centre, Srinagar, by Lieutenant Governor Manoj Sinha, with five ministers — the first Chief Minister of the Union Territory. He had also been Chief Minister of the former State in 2009–2015 (ETV Bharat)."),
    "others": [
        office("speaker", L("Abdul Rahim Rather", "अब्दुल रहीम राथर", "अब्दुल रहीम राथर"), "JKNC", "2024-11-04", "etv-bharat", SPK, "https://jkla.nic.in", conf="Third-party verified",
               note="Elected unanimously as Speaker of the first Legislative Assembly of the Union Territory on 4 November 2024; a seven-time MLA (ETV Bharat)."),
    ],
}

r["projects"] = [
    proj("usbrl", L("Udhampur–Srinagar–Baramulla Rail Link", "उधमपुर–श्रीनगर–बारामूला रेल लिंक", "उधमपूर–श्रीनगर–बारामुल्ला रेल्वे मार्ग"),
         L("The railway that links the Kashmir valley with the national network through the Pir Panjal and Chenab gorge, built at a cost of around ₹44,000 crore. It includes the Chenab bridge, described as the world's highest railway arch bridge, and the Anji Khad bridge, India's first cable-stayed rail bridge. Dedicated to the nation by the Prime Minister on 6 June 2025, when two Vande Bharat trains between Shri Mata Vaishno Devi Katra and Srinagar were flagged off.",
           "वह रेलवे जो पीर पंजाल और चिनाब घाटी से होकर कश्मीर घाटी को राष्ट्रीय नेटवर्क से जोड़ती है, लगभग ₹44,000 करोड़ की लागत से बनी। इसमें दुनिया का सबसे ऊँचा रेलवे आर्च पुल बताया गया चिनाब पुल और भारत का पहला केबल-स्टेड रेल पुल अंजी खड्ड पुल शामिल हैं। प्रधानमंत्री ने 6 जून 2025 को इसे राष्ट्र को समर्पित किया, जब श्री माता वैष्णो देवी कटरा और श्रीनगर के बीच दो वंदे भारत ट्रेनों को हरी झंडी दिखाई गई।",
           "पीर पंजाल व चिनाबच्या घळीतून काश्मीर खोऱ्याला राष्ट्रीय जाळ्याशी जोडणारी रेल्वे, सुमारे ₹44,000 कोटी खर्चून बांधलेली. तिच्यात जगातील सर्वांत उंच रेल्वे कमान पूल म्हणून वर्णन केलेला चिनाब पूल व भारतातील पहिला केबल-स्टेड रेल्वे पूल अंजी खड्ड पूल यांचा समावेश आहे. पंतप्रधानांनी 6 जून 2025 रोजी ती राष्ट्राला समर्पित केली, तेव्हा श्री माता वैष्णोदेवी कटरा व श्रीनगरदरम्यान दोन वंदे भारत गाड्यांना हिरवा झेंडा दाखवला गेला."),
         "rail", "Northern Railway (Ministry of Railways)", 44000, "Around ₹44,000 crore (News On AIR).", "2025", None, "6 June 2025", "Completed", "newsonair", USBRL),
]

GI_NAMES = {
 "Kashmir Saffron": ("कश्मीर केसर", "काश्मीर केशर"),
 "Mushqbudji Rice": ("मुश्कबुदजी चावल", "मुश्कबुदजी तांदूळ"),
 "Bhaderwah Rajmash": ("भद्रवाह राजमाश", "भद्रवाह राजमा"),
 "Ramban Anardana": ("रामबन अनारदाना", "रामबन अनारदाणा"),
 "Ramban Sulai Honey": ("रामबन सुलाई शहद", "रामबन सुलाई मध"),
 "Udhampur Kaladi": ("उधमपुर कलाड़ी", "उधमपूर कलाडी"),
 "Kashmir Pashmina": ("कश्मीर पश्मीना", "काश्मीर पश्मीना"),
 "Kashmir Sozani Craft": ("कश्मीर सोज़नी शिल्प", "काश्मीर सोझनी हस्तकला"),
 "Kani Shawl": ("कानी शॉल", "कानी शाल"),
 "Kashmir Paper Machie": ("कश्मीर पेपर माशी", "काश्मीर पेपर-माशे"),
 "Kashmir Walnut Wood Carving": ("कश्मीर अखरोट काष्ठ नक़्क़ाशी", "काश्मीर अक्रोड लाकूड कोरीवकाम"),
 "Khatamband": ("ख़तमबंद", "खतमबंद"),
 "Kashmiri Hand Knotted Carpet": ("कश्मीरी हाथ से गाँठे क़ालीन", "काश्मिरी हाताने विणलेले गालिचे"),
 "Basohli Painting": ("बसोहली चित्रकला", "बसोहली चित्रकला"),
 "Rajouri Chikri Wood Craft": ("राजौरी चिकरी काष्ठ शिल्प", "राजौरी चिकरी काष्ठहस्तकला"),
 "Basohli Pashmina Woolen Products": ("बसोहली पश्मीना ऊनी उत्पाद", "बसोहली पश्मीना लोकरी उत्पादने"),
 "Kashmir Namda": ("कश्मीर नमदा", "काश्मीर नमदा"),
 "Kashmir Wagguv": ("कश्मीर वग्गुव", "काश्मीर वग्गुव"),
 "Shikara": ("शिकारा", "शिकारा"),
 "Gabba": ("गब्बा", "गब्बा"),
 "Kashmir Willow Bat": ("कश्मीर विलो बल्ला", "काश्मीर विलो बॅट"),
 "Kashmir Chain Stitch": ("कश्मीर चेन स्टिच", "काश्मीर चेन स्टिच"),
 "Kashmir Crewel": ("कश्मीर क्रूएल", "काश्मीर क्रुएल"),
 "Kashmir Tweed": ("कश्मीर ट्वीड", "काश्मीर ट्वीड"),
 "Basmati": ("बासमती", "बासमती"),
}
SHARED = {"PB,HR,HP,DL,UK,UP,JK": ["Punjab", "Haryana", "Himachal Pradesh", "Delhi", "Uttarakhand", "Uttar Pradesh"]}
TEXT = {"Kashmir Pashmina", "Kashmir Sozani Craft", "Kani Shawl", "Basohli Pashmina Woolen Products", "Kashmir Chain Stitch", "Kashmir Crewel", "Kashmir Tweed", "Kashmir Namda", "Gabba"}
r["giProducts"] = gi_list("gi_jk.tsv", GI_NAMES, SHARED, TEXT)
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-JK.json", r)
print("jk core ok", len(r["giProducts"]), "GIs")
