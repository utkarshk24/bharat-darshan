"""West Bengal — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-14."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
NOA_CM = "https://newsonair.gov.in/suvendu-adhikari-takes-oath-as-first-bjp-cm-of-west-bengal/"
SPK = "https://www.dailypioneer.com/news/rathindra-bose-elected-speaker-of-west-bengal-assembly"
METRO = "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2159869&reg=48&lang=2"

wb = research("mospi_wb.json")
r = read("regions/IN-WB.json")
m = r["metrics"]
m["population2011"] = dp(91276115, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 4,68,09,027; females 4,44,67,088.")
m["area"] = dp(88752, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026); NITI Aayog also gives 88,752 km².")
m["density2011"] = dp(1028, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 9,12,76,115 ÷ area 88,752 km² = 1,028.4.")
m["sexRatio2011"] = dp(950, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (934 in 2001).")
m["childSexRatio2011"] = dp(956, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 960 in 2001.")
m["literacyRate2011"] = dp(76.3, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011). Was 68.6% in 2001.")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(wb["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25: ₹{inr(wb['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(wb["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(wb['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(18.97, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 16,832.33 km² ÷ geographical area 88,752 km².")

r["officialPortal"] = "https://wb.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Fishing cat", "मछुआ बिल्ली", "मासेमार मांजर", "Prionailurus viverrinus"),
    "bird": sym("White-throated kingfisher", "सफ़ेद गले वाला किलकिला", "पांढऱ्या गळ्याचा खंड्या", "Halcyon smyrnensis"),
    "flower": sym("Night-flowering jasmine (shiuli)", "हरसिंगार (शिउली)", "पारिजातक (शिउली)", "Nyctanthes arbor-tristis"),
    "tree": sym("Chhatim (devil's tree)", "सप्तपर्णी (छातिम)", "सप्तपर्णी (छातिम)", "Alstonia scholaris"),
}

r["government"] = {
    "headOfState": office("governor", L("R. N. Ravi", "आर. एन. रवि", "आर. एन. रवी"), None, "2026-03-12",
                          "newsonair", NOA_CM, "https://igod.gov.in",
                          note="Moved from Tamil Nadu to West Bengal in March 2026 (Lok Bhavan, Tamil Nadu). He administered the oath to the Chief Minister on 9 May 2026 (News On AIR). Confirm the start date on the Lok Bhavan, West Bengal website."),
    "headOfGovernment": office("chief-minister", L("Suvendu Adhikari", "शुभेंदु अधिकारी", "शुभेंदू अधिकारी"), "BJP", "2026-05-09",
                               "newsonair", NOA_CM, "https://wb.gov.in",
                               note="Sworn in by Governor R. N. Ravi at the Brigade Parade Ground, Kolkata, on 9 May 2026, with five Cabinet ministers (News On AIR)."),
    "others": [
        office("speaker", L("Rathindra Bose", "रथींद्र बोस", "रथींद्र बोस"), "BJP", "2026-05-15", "pioneer", SPK, "https://wbassembly.gov.in",
               conf="Third-party verified", note="Elected unopposed in May 2026 (The Pioneer; IANS). Confirm the date on the Assembly website."),
    ],
}

r["projects"] = [
    proj("kolkata-metro-2025", L("Kolkata Metro — three new stretches (August 2025)", "कोलकाता मेट्रो — तीन नए खंड (अगस्त 2025)", "कोलकाता मेट्रो — तीन नवे टप्पे (ऑगस्ट 2025)"),
         L("Three stretches totalling 13.61 km — Noapara–Jai Hind Bimanbandar (airport), Sealdah–Esplanade and Beleghata–Hemanta Mukhopadhyay — opened by the Prime Minister on 22 August 2025, along with a subway at Howrah Metro station.",
           "कुल 13.61 किमी के तीन खंड — नोआपाड़ा–जय हिंद बिमानबंदर (हवाई अड्डा), सियालदह–एस्प्लेनेड और बेलेघाटा–हेमंत मुखोपाध्याय — 22 अगस्त 2025 को प्रधानमंत्री ने खोले, साथ में हावड़ा मेट्रो स्टेशन पर एक सबवे भी।",
           "एकूण 13.61 किमीचे तीन टप्पे — नोआपाडा–जय हिंद बिमानबंदर (विमानतळ), सियालदह–एस्प्लनेड व बेलेघाटा–हेमंत मुखोपाध्याय — 22 ऑगस्ट 2025 रोजी पंतप्रधानांनी सुरू केले, सोबत हावडा मेट्रो स्थानकावरील भुयारी मार्गही."),
         "transport", "Metro Railway, Kolkata", None, None, None, None, "August 2025", "Completed", "pib", METRO),
    proj("kona-expressway", L("Kona Expressway elevated corridor", "कोना एक्सप्रेसवे एलिवेटेड कॉरिडोर", "कोना द्रुतगती मार्ग उन्नत मार्गिका"),
         L("A 7.2 km six-lane elevated road on the Kona Expressway linking Howrah to Kolkata; the Prime Minister laid the foundation stone on 22 August 2025.",
           "हावड़ा को कोलकाता से जोड़ने वाले कोना एक्सप्रेसवे पर 7.2 किमी लंबी छह-लेन एलिवेटेड सड़क; 22 अगस्त 2025 को प्रधानमंत्री ने इसकी आधारशिला रखी।",
           "हावडाला कोलकात्याशी जोडणाऱ्या कोना द्रुतगती मार्गावरील 7.2 किमीचा सहापदरी उन्नत रस्ता; 22 ऑगस्ट 2025 रोजी पंतप्रधानांनी पायाभरणी केली."),
         "transport", "NHAI", 1200, "Over ₹1,200 crore (PIB).", "2025", "August 2025", None, "Under Construction", "pib", METRO),
]

GI_NAMES = {
 "Darjeeling Tea (word & Logo)": ("दार्जिलिंग चाय (शब्द और लोगो)", "दार्जिलिंग चहा (शब्द व बोधचिन्ह)"),
 "Malda Laxman Bhog Mango": ("मालदा लक्ष्मण भोग आम", "मालदा लक्ष्मणभोग आंबा"),
 "Malda Khirsapati (Himsagar) Mango": ("मालदा खीरसापाती (हिमसागर) आम", "मालदा खीरसापाती (हिमसागर) आंबा"),
 "Malda Fazli Mango": ("मालदा फ़ज़ली आम", "मालदा फजली आंबा"),
 "Tulaipanji Rice": ("तुलाईपांजी चावल", "तुलाईपांजी तांदूळ"),
 "Gobindabhog Rice": ("गोबिंदभोग चावल", "गोबिंदभोग तांदूळ"),
 "Kalonunia Rice": ("कालोनुनिया चावल", "कालोनुनिया तांदूळ"),
 "Baruipur Guava": ("बारुईपुर अमरूद", "बारुईपूर पेरू"),
 "Radhunipagal Rice": ("राधुनीपागल चावल", "राधुनीपागल तांदूळ"),
 "Darjeeling Mandarin": ("दार्जिलिंग संतरा", "दार्जिलिंग संत्रे"),
 "Bardhaman Sitabhog": ("बर्धमान सीताभोग", "बर्धमान सीताभोग"),
 "Bardhaman Mihidana": ("बर्धमान मिहिदाना", "बर्धमान मिहिदाना"),
 "Banglar Rasogolla": ("बंगाल का रसगुल्ला", "बंगालचा रसगुल्ला"),
 "Sundarban Honey": ("सुंदरबन शहद", "सुंदरबन मध"),
 "Kamarpukur Sada Bode": ("कामारपुकुर सादा बोंदे", "कामारपुकूर सादा बोंदे"),
 "Banglar Nolen Gur Sandesh": ("बंगाल का नोलेन गुड़ संदेश", "बंगालचा नोलेन गूळ संदेश"),
 "Murshidabad Chhanabora": ("मुर्शिदाबाद छानाबोड़ा", "मुर्शिदाबाद छानाबोडा"),
 "Bishnupur Motichur Laddu": ("बिष्णुपुर मोतीचूर लड्डू", "बिष्णुपूर मोतीचूर लाडू"),
 "Joynagar Moa": ("जयनगर मोआ", "जयनगर मोआ"),
 "Nakshi Kantha": ("नक्शी कांथा", "नक्शी कांथा"),
 "Santiniketan Leather Goods": ("शांतिनिकेतन चमड़े का सामान", "शांतिनिकेतन चामडी वस्तू"),
 "Santipore Saree": ("शांतिपुर साड़ी", "शांतिपूर साडी"),
 "Baluchari Saree": ("बालूचरी साड़ी", "बालुचरी साडी"),
 "Dhaniakhali Saree": ("धनियाखाली साड़ी", "धनियाखाली साडी"),
 "Bankura Panchmura Terracotta Craft": ("बाँकुड़ा पाँचमुड़ा टेराकोटा शिल्प", "बांकुडा पांचमुडा टेराकोटा कला"),
 "Bengal Dokra": ("बंगाल डोकरा", "बंगाल डोकरा"),
 "Bengal Patachitra": ("बंगाल पटचित्र", "बंगाल पटचित्र"),
 "Purulia Chau Mask": ("पुरुलिया छऊ मुखौटा", "पुरुलिया छाऊ मुखवटा"),
 "Wooden Mask of Kushmandi": ("कुशमंडी का लकड़ी का मुखौटा", "कुशमंडीचा लाकडी मुखवटा"),
 "Madurkathi": ("मादुरकाठी (चटाई)", "मादुरकाठी (चटई)"),
 "Tangail Saree of Bengal": ("बंगाल की टांगाइल साड़ी", "बंगालची टांगाइल साडी"),
 "Garad Saree": ("गरद साड़ी", "गरद साडी"),
 "Korial saree": ("कोरियाल साड़ी", "कोरियाल साडी"),
 "Banglar Muslin": ("बंगाल का मलमल", "बंगालची मलमल"),
 "Malda Nistari Silk Yarn": ("मालदा निस्तारी रेशम धागा", "मालदा निस्तारी रेशीम धागा"),
}
TEXTILE = {"Nakshi Kantha", "Santipore Saree", "Baluchari Saree", "Dhaniakhali Saree", "Tangail Saree of Bengal", "Garad Saree",
           "Korial saree", "Banglar Muslin", "Malda Nistari Silk Yarn"}
r["giProducts"] = gi_list("gi_wb.tsv", GI_NAMES, {}, TEXTILE)
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-WB.json", r)
print("wb core ok", len(r["giProducts"]), "GIs")
