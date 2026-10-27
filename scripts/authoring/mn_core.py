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
         L("A 111-km broad-gauge line from Jiribam on the Assam border to Imphal through the hills of Noney and Tamenglong, with 54 tunnels totalling about 66.5 km — the longest, Tunnel 12, is 11.55 km — and the Noney bridge, whose 141-m piers Northeast Frontier Railway describes as the tallest railway piers in the world. The estimated cost is about ₹22,000 crore. In August 2026 NFR officials inspected the Jiribam–Khongsang, Khongsang–Awangkhul and Awangkhul–Imphal sections, and the line is targeted to reach Imphal by June 2029.",
           "असम सीमा पर जिरीबाम से नोनी और तामेंगलोंग की पहाड़ियों से होकर इंफाल तक 111 किमी लंबी बड़ी लाइन, जिसमें कुल लगभग 66.5 किमी की 54 सुरंगें हैं — सबसे लंबी, सुरंग 12, 11.55 किमी की है — और नोनी पुल, जिसके 141 मीटर ऊँचे खंभों को पूर्वोत्तर सीमांत रेलवे दुनिया के सबसे ऊँचे रेलवे खंभे बताता है। अनुमानित लागत लगभग ₹22,000 करोड़ है। अगस्त 2026 में एनएफ़आर अधिकारियों ने जिरीबाम–खोंगसांग, खोंगसांग–अवांगखुल और अवांगखुल–इंफाल खंडों का निरीक्षण किया, और जून 2029 तक लाइन को इंफाल पहुँचाने का लक्ष्य है।",
           "आसाम सीमेवरील जिरीबामपासून नोनी व तामेंगलोंगच्या डोंगरांतून इंफाळपर्यंतचा 111 किमी लांबीचा ब्रॉडगेज मार्ग, ज्यात एकूण सुमारे 66.5 किमीचे 54 बोगदे आहेत — सर्वांत लांब, बोगदा 12, 11.55 किमीचा आहे — आणि नोनी पूल, ज्याच्या 141 मीटर उंच खांबांना ईशान्य सीमा रेल्वे जगातील सर्वांत उंच रेल्वे खांब म्हणते. अंदाजित खर्च सुमारे ₹22,000 कोटी आहे. ऑगस्ट 2026 मध्ये एनएफआर अधिकाऱ्यांनी जिरीबाम–खोंगसांग, खोंगसांग–अवांगखुल व अवांगखुल–इंफाळ टप्प्यांची पाहणी केली, आणि जून 2029 पर्यंत मार्ग इंफाळला पोहोचवण्याचे उद्दिष्ट आहे."),
         "railways", "Northeast Frontier Railway", 22000, "About ₹22,000 crore, as reported (IANS via The Morung Express, 25 Aug 2026); sanctioned cost to be confirmed from the Ministry of Railways.", "2026", None, "June 2029 (target)", "Under Construction", "morung-express", RAIL, conf="Third-party verified"),
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
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-MN.json", r)
print("mn core ok", len(r["giProducts"]), "GIs")
