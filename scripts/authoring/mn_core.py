"""Manipur — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.newsonair.gov.in/former-union-home-secretary-ajay-kumar-bhalla-sworn-in-as-governor-of-manipur"
CM = "https://www.thehitavada.com/Encyc/2026/2/5/presidents-rule-revoked-khemchand-singh-is-manipurs-new-cm.html"
SPK = "https://assembly.mn.gov.in/user/pages/files/bulletin/part-ii/No.%206%20Election%20of%20Speaker.pdf"
RAIL = "https://morungexpress.com/imphal-to-become-fifth-northeast-capital-city-on-national-railway-map-by-june-2029"

mo = research("mospi_mn.json")
C = research("census_b5plus.json")
r = read("regions/IN-MN.json")
m = r["metrics"]
p = C["pop"]["MN"]
EXCL = "Census 2011 figures for Manipur exclude the Mao-Maram, Paomata and Purul sub-divisions of Senapati district, where the results were not used."
m["population2011"] = dp(p[0], "persons", "2011", "census", "census", PYD,
    note=f"Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 12,90,171; females 12,80,219. {EXCL}")
m["area"] = dp(22327, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(115, "persons per km²", "2011", "census", "census", PYD,
    note=f"Calculated: Census 2011 population 25,70,390 ÷ area 22,327 km² = 115.1. {EXCL}")
m["sexRatio2011"] = dp(992, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (978 in 2001).")
m["childSexRatio2011"] = dp(936, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 957 in 2001.")
m["literacyRate2011"] = dp(76.9, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25 is the latest year published for Manipur. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2023-24: ₹{inr(mo['pcnsdp']['FY2023-24'][0])}.")
m["forestCoverPct"] = dp(74.28, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 16,585.46 km² ÷ geographical area 22,327 km².")

r["officialPortal"] = "https://manipur.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Sangai (brow-antlered deer)", "संगाई (भौंह-सींग वाला हिरण)", "संगाई (भुवई-शिंगी हरिण)", "Rucervus eldii eldii"),
    "bird": sym("Mrs Hume's pheasant (nongyeen)", "मिसेज़ ह्यूम्स फ़ेज़ेंट (नोंगयीन)", "मिसेस ह्यूम्स फेझंट (नोंगयीन)", "Syrmaticus humiae"),
    "flower": sym("Shirui lily", "शिरुई लिली", "शिरुई लिली", "Lilium mackliniae"),
}

r["government"] = {
    "headOfState": office("governor", L("Ajay Kumar Bhalla", "अजय कुमार भल्ला", "अजय कुमार भल्ला"), None, "2025-01-03",
                          "newsonair", GOV, "https://rajbhavanmanipur.nic.in", conf="Official",
                          note="Former Union Home Secretary; sworn in as Governor of Manipur on 3 January 2025 in the Durbar Hall of Raj Bhavan, Imphal, by Chief Justice D. Krishnakumar of the Manipur High Court, succeeding Lakshman Prasad Acharya, who had held additional charge (All India Radio News)."),
    "headOfGovernment": office('chief-minister', L('Yumnam Khemchand Singh', 'युमनाम खेमचंद सिंह', 'युमनाम खेमचंद सिंह'), 'BJP', '2026-02-04', 'newsonair', 'https://www.newsonair.gov.in/manipur-cm-yumnam-khemchand-meets-pm-modi-at-pms-office-in-seva-teerth', 'https://manipur.gov.in', note="Official confirmation: News On AIR 24 Feb 2026: Manipur Chief Minister Yumnam Khemchand met the Prime Minister. Sworn in on 4 February 2026 by Governor Ajay Kumar Bhalla, hours after President's Rule (in force since 13 February 2025) was revoked. Nemcha Kipgen (BJP) and L. Dikho (NPF) were sworn in as Deputy Chief Ministers (The Hitavada, 5 February 2026).", as_of='2026-10-27'),
    "others": [
        office("speaker", L("Thokchom Satyabrata Singh", "थोकचोम सत्यव्रत सिंह", "थोकचोम सत्यव्रत सिंह"), "BJP", "2022-03-24", "mn-assembly", SPK, "https://assembly.mn.gov.in", conf="Official",
               note="Elected Speaker of the Twelfth Manipur Legislative Assembly on 24 March 2022; Member from 14-Yaiskul (Assembly Bulletin Part II, No. 6)."),
    ],
}

r["projects"] = [
    proj("jiribam-imphal-rail", L("Jiribam–Imphal new railway line", "जिरीबाम–इंफाल नई रेल लाइन", "जिरीबाम–इंफाळ नवा रेल्वेमार्ग"),
         L("A 111-km (110.625-km) broad-gauge line from Jiribam on the Assam border to Imphal, through Noney district. The 11.8-km Jiribam–Vangaichungpao section opened in February 2017 and the Vangaichungpao–Khongsang section followed; in September 2025 the remaining sections were targeted for March 2026 (Khongsang–Awangkhul), March 2027 (Awangkhul–Noney) and March 2028 (Noney–Imphal). The line has 54 tunnels totalling about 66.5 km, the longest being the 11.55-km Tunnel 12, and the Noney bridge, with a 141-m pier reported as the world's tallest railway pier. In August 2026 Northeast Frontier Railway's General Manager inspected the line, and it was then expected to be fully operational by June 2029.",
           "असम सीमा पर जिरीबाम से नोनी ज़िले से होकर इंफाल तक 111 किमी (110.625 किमी) लंबी बड़ी लाइन। 11.8 किमी का जिरीबाम–वांगाईचुंगपाओ खंड फरवरी 2017 में खुला और उसके बाद वांगाईचुंगपाओ–खोंगसांग खंड; सितंबर 2025 में शेष खंडों के लक्ष्य मार्च 2026 (खोंगसांग–अवांगखुल), मार्च 2027 (अवांगखुल–नोनी) और मार्च 2028 (नोनी–इंफाल) थे। लाइन में कुल लगभग 66.5 किमी की 54 सुरंगें हैं, जिनमें सबसे लंबी 11.55 किमी की सुरंग 12 है, और नोनी पुल है, जिसके 141 मीटर ऊँचे खंभे को दुनिया का सबसे ऊँचा रेलवे खंभा बताया गया है। अगस्त 2026 में पूर्वोत्तर सीमांत रेलवे के महाप्रबंधक ने लाइन का निरीक्षण किया, और तब इसके जून 2029 तक पूरी तरह चालू होने की उम्मीद थी।",
           "आसाम सीमेवरील जिरीबामपासून नोनी जिल्ह्यातून इंफाळपर्यंतचा 111 किमी (110.625 किमी) लांबीचा ब्रॉडगेज मार्ग. 11.8 किमीचा जिरीबाम–वांगाईचुंगपाओ टप्पा फेब्रुवारी 2017 मध्ये सुरू झाला आणि त्यानंतर वांगाईचुंगपाओ–खोंगसांग टप्पा; सप्टेंबर 2025 मध्ये उर्वरित टप्प्यांचे उद्दिष्ट मार्च 2026 (खोंगसांग–अवांगखुल), मार्च 2027 (अवांगखुल–नोनी) आणि मार्च 2028 (नोनी–इंफाळ) होते. मार्गात एकूण सुमारे 66.5 किमीचे 54 बोगदे आहेत, त्यांपैकी सर्वांत लांब 11.55 किमीचा बोगदा 12 आहे, आणि नोनी पूल आहे, ज्याचा 141 मीटर उंच खांब जगातील सर्वांत उंच रेल्वे खांब असल्याचे सांगितले जाते. ऑगस्ट 2026 मध्ये ईशान्य सीमा रेल्वेच्या महाव्यवस्थापकांनी मार्गाची पाहणी केली, आणि तेव्हा तो जून 2029 पर्यंत पूर्णपणे कार्यान्वित होणे अपेक्षित होते."),
         "railways", "Northeast Frontier Railway", 22000, "About ₹22,000 crore, as reported (IANS via The Morung Express, 25 Aug 2026); sanctioned cost to be confirmed from the Ministry of Railways.", "2026", None, "June 2029 (target)", "Under Construction", "pib", "https://pib.gov.in/FactsheetDetails.aspx?Id=149284",
         as_of="2026-10-28", cost_src=("morung-express", RAIL, "Third-party verified"),
         supporting=[("morung-express", RAIL, L("the tunnels, the Noney pier, the cost, the August 2026 inspection and the June 2029 target (IANS)",
                                                "सुरंगें, नोनी का खंभा, लागत, अगस्त 2026 का निरीक्षण और जून 2029 का लक्ष्य (आईएएनएस)",
                                                "बोगदे, नोनीचा खांब, खर्च, ऑगस्ट 2026 ची पाहणी आणि जून 2029 चे उद्दिष्ट (आयएएनएस)"))]),
]

GI_NAMES = {
 "Kachai Lemon": ("काचाई नींबू", "काचाई लिंबू"),
 "Tamenglong Orange": ("तामेंगलोंग संतरा", "तामेंगलोंग संत्रे"),
 "Sirarakhong Hathei": ("सिरारखोंग हथेई (मिर्च)", "सिरारखोंग हथेई (मिरची)"),
 "Shaphee Lanphee": ("शफ़ी लानफ़ी", "शफी लानफी"),
 "Wangkhei Phee": ("वांगखेई फ़ी", "वांगखेई फी"),
 "Moirang Phee": ("मोइरांग फ़ी", "मोइरांग फी"),
 "Chak-Hao": ("चाक-हाओ (काला चावल)", "चाक-हाओ (काळा तांदूळ)"),
}
r["giProducts"] = gi_list("gi_mn.tsv", GI_NAMES, {"MN,NL": ["Nagaland"]}, {"Shaphee Lanphee", "Wangkhei Phee", "Moirang Phee"})
r["meta"] = {"lastUpdated": "2026-10-28",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-MN.json", r)
print("mn core ok", len(r["giProducts"]), "GIs")
