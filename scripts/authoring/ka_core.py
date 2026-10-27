"""Karnataka — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-14."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
KAES24 = "https://data.opencity.in/dataset/90aaf1df-999b-4d84-a0d0-443aee3d0bfc/resource/b96f076f-9b1c-48b2-bc1b-f081f1beca84/download/economic_survey_2023-24_finalenglish_compressed.pdf"
NOA_CAB = "https://newsonair.gov.in/cabinet-expansion-in-karnataka-19-new-ministers-inducted/"
UNI_SPK = "https://test.uniindia.com/speaker-s-chair-must-remain-above-party-politics-ashoka-tells-gs-patil/south/news/3943280.html"
UNI_GOV = "https://www.uniindia.com/south-india/karnataka-governor-appointed/211799"
ANI_GOV = "https://www.aninews.in/news/national/general-news/sudha-yadav-takes-oath-as-karnataka-governor-at-raj-bhavan-in-bengaluru20261016112255/"
METRO = "https://www.pmindia.gov.in/en/news_updates/pm-inaugurates-lays-foundation-stone-of-metro-projects-worth-around-rs-22800-crore-in-bengaluru-karnataka/"

ka = research("mospi_ka.json")
r = read("regions/IN-KA.json")
m = r["metrics"]
m["population2011"] = dp(61095297, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 3,09,66,657; females 3,01,28,640.")
m["area"] = dp(191791, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026); the same figure is given by the Economic Survey of Karnataka.")
m["density2011"] = dp(319, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 6,10,95,297 ÷ area 1,91,791 km² = 318.6, rounded.")
m["sexRatio2011"] = dp(973, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (965 in 2001).")
m["childSexRatio2011"] = dp(948, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 946 in 2001.")
m["literacyRate2011"] = dp(75.4, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011). Was 66.6% in 2001.")
m["urbanisation2011"] = dp(38.67, "%", "2011", "census", "ka-des", KAES24, note="Economic Survey of Karnataka 2023-24, Introduction (Census 2011).")
m["gsdpCurrent"] = dp(ka["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25: ₹{inr(ka['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(ka["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(ka['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(20.47, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 39,254.27 km² ÷ geographical area 1,91,791 km².")

r["officialPortal"] = "https://www.karnataka.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Indian elephant", "भारतीय हाथी", "भारतीय हत्ती", "Elephas maximus indicus"),
    "bird": sym("Indian roller", "नीलकंठ", "नीलकंठ (चास)", "Coracias benghalensis"),
    "flower": sym("Lotus", "कमल", "कमळ", "Nelumbo nucifera"),
    "tree": sym("Sandalwood", "चंदन", "चंदन", "Santalum album"),
}

r["government"] = {
    "headOfState": office('governor', L('Sudha Yadav', 'सुधा यादव', 'सुधा यादव'), None, '2026-10-16', 'newsonair', 'https://www.newsonair.gov.in/dr-sudha-yadav-assumes-office-as-governor-of-karnataka/', 'https://igod.gov.in', note='Official confirmation: News On AIR 16 Oct 2026: Dr Sudha Yadav assumed office as Governor at Lok Bhavan, Bengaluru. Appointed by the President on 12 October 2026 (Rashtrapati Bhavan communiqué) and sworn in at Raj Bhavan, Bengaluru, on 16 October 2026 by Chief Justice Vibhu Bakhru of the Karnataka High Court (ANI). Former Lok Sabha member from Mahendragarh, Haryana. Succeeded Thaawarchand Gehlot (Governor from July 2021). Confirm on the Raj Bhavan / Lok Bhavan, Karnataka website.', as_of='2026-10-27'),
    "headOfGovernment": office("chief-minister", L("D. K. Shivakumar", "डी. के. शिवकुमार", "डी. के. शिवकुमार"), "INC", "2026-06-03",
                               "newsonair", NOA_CAB, "https://www.karnataka.gov.in",
                               note="Assumed office as Chief Minister on 3 June 2026 with 13 ministers, succeeding Siddaramaiah (News On AIR, 3 August 2026)."),
    "others": [
        office("speaker", L("G. S. Patil", "जी. एस. पाटिल", "जी. एस. पाटील"), "INC", "2026-08-14", "uni", UNI_SPK, "https://kla.kar.nic.in",
               conf="Third-party verified", note="Described as the newly elected Speaker by UNI on 14 August 2026. Confirm on the Legislative Assembly website."),
        office("leader-of-opposition", L("R. Ashoka", "आर. अशोक", "आर. अशोक"), "BJP", "2023-11-17", "uni", UNI_SPK, "https://kla.kar.nic.in",
               conf="Third-party verified", note="Named as Leader of Opposition by UNI on 14 August 2026; chosen by the BJP legislature party in November 2023."),
    ],
}

r["projects"] = [
    proj("namma-metro-yellow", L("Namma Metro Yellow Line (RV Road–Bommasandra)", "नम्मा मेट्रो येलो लाइन (आरवी रोड–बोम्मसंद्रा)", "नम्मा मेट्रो यलो लाईन (आरव्ही रोड–बोम्मसंद्रा)"),
         L("A 19 km elevated line with 16 stations from RV Road (Ragigudda) to Bommasandra, serving the Electronic City technology hub. Part of Bangalore Metro Phase 2; opened by the Prime Minister on 10 August 2025, taking the city's operational metro network past 96 km.",
           "आरवी रोड (रागीगुड्डा) से बोम्मसंद्रा तक 16 स्टेशनों वाली 19 किमी की एलिवेटेड लाइन, जो इलेक्ट्रॉनिक सिटी प्रौद्योगिकी केंद्र को सेवा देती है। बैंगलोर मेट्रो चरण 2 का हिस्सा; 10 अगस्त 2025 को प्रधानमंत्री ने इसका उद्घाटन किया, जिससे शहर का चालू मेट्रो नेटवर्क 96 किमी से अधिक हो गया।",
           "आरव्ही रोड (रागीगुड्डा) ते बोम्मसंद्रा अशी 16 स्थानकांची 19 किमीची उन्नत मार्गिका, जी इलेक्ट्रॉनिक सिटी तंत्रज्ञान केंद्राला सेवा देते. बंगळूरु मेट्रो टप्पा 2 चा भाग; 10 ऑगस्ट 2025 रोजी पंतप्रधानांच्या हस्ते उद्घाटन, ज्यामुळे शहरातील कार्यरत मेट्रो जाळे 96 किमीच्या पुढे गेले."),
         "transport", "Bangalore Metro Rail Corporation Limited (BMRCL)", 7160, "About ₹7,160 crore (PMO).", "2025",
         None, "August 2025", "Completed", "pmindia", METRO),
    proj("namma-metro-phase3", L("Bangalore Metro Phase 3", "बैंगलोर मेट्रो चरण 3", "बंगळूरु मेट्रो टप्पा 3"),
         L("More than 44 km of new elevated lines with 31 stations, including the Orange Line along the Outer Ring Road; the Prime Minister laid the foundation stone on 10 August 2025. Together with the Yellow Line, the lines are expected to serve about 25 lakh passengers a day.",
           "44 किमी से अधिक नई एलिवेटेड लाइनें और 31 स्टेशन, जिनमें आउटर रिंग रोड के साथ ऑरेंज लाइन शामिल है; प्रधानमंत्री ने 10 अगस्त 2025 को इसकी आधारशिला रखी। येलो लाइन के साथ मिलकर इन लाइनों से रोज़ लगभग 25 लाख यात्रियों को सेवा मिलने की उम्मीद है।",
           "44 किमीहून अधिक नव्या उन्नत मार्गिका व 31 स्थानके, ज्यात आउटर रिंग रोडलगतची ऑरेंज लाईन आहे; पंतप्रधानांनी 10 ऑगस्ट 2025 रोजी पायाभरणी केली. यलो लाईनसह या मार्गिकांतून दररोज सुमारे 25 लाख प्रवाशांना सेवा मिळणे अपेक्षित आहे."),
         "transport", "Bangalore Metro Rail Corporation Limited (BMRCL)", 15610, "Over ₹15,610 crore (PMO).", "2025",
         "August 2025", None, "Under Construction", "pmindia", METRO),
]

GI_NAMES = {
 "Coorg Orange": ("कुर्ग संतरा", "कूर्ग संत्रे"),
 "Mysore Betel Leaf": ("मैसूर पान", "म्हैसूर विड्याचे पान"),
 "Nanjanagud Banana": ("नंजनगूड केला", "नंजनगूड केळे"),
 "Mysore Malligae": ("मैसूर मल्लिगे (चमेली)", "म्हैसूर मल्लिगे (मोगरा)"),
 "Udupi Malligae": ("उडुपी मल्लिगे (चमेली)", "उडुपी मल्लिगे (मोगरा)"),
 "Hadagali Malligae": ("हडगली मल्लिगे (चमेली)", "हडगली मल्लिगे (मोगरा)"),
 "Coorg Green Cardamom": ("कुर्ग हरी इलायची", "कूर्ग हिरवी वेलची"),
 "Byadagi Chilli": ("ब्याडगी मिर्च", "ब्याडगी मिरची"),
 "Devanahalli Pomello": ("देवनहल्ली चकोतरा", "देवनहळ्ळी पपनस"),
 "Appemidi Mango": ("अप्पेमिडी आम", "अप्पेमिडी आंबा"),
 "Kamalapur Red Banana": ("कमलापुर लाल केला", "कमलापूर लाल केळे"),
 "Udupi Mattu Gulla Brinjal": ("उडुपी मट्टू गुल्ला बैंगन", "उडुपी मट्टू गुल्ला वांगे"),
 "Bangalore Blue Grapes": ("बैंगलोर ब्लू अंगूर", "बंगळूरु ब्लू द्राक्षे"),
 "Bangalore Rose Onion": ("बैंगलोर रोज़ प्याज़", "बंगळूरु रोझ कांदा"),
 "Sirsi Supari": ("सिरसी सुपारी", "सिरसी सुपारी"),
 "Gulbarga Tur Dal": ("गुलबर्गा अरहर दाल", "गुलबर्गा तूरडाळ"),
 "Coorg Arabica Coffee": ("कुर्ग अरेबिका कॉफ़ी", "कूर्ग अरेबिका कॉफी"),
 "Chikmagalur Arabica Coffee": ("चिकमगलूर अरेबिका कॉफ़ी", "चिकमगळूर अरेबिका कॉफी"),
 "Bababudangiris Arabica Coffee": ("बाबाबुदनगिरि अरेबिका कॉफ़ी", "बाबाबुदनगिरी अरेबिका कॉफी"),
 "Indi Limbe": ("इंडी नींबू", "इंडी लिंबू"),
 "Kari Ishad Mango": ("करी इशाड आम", "करी इशाड आंबा"),
 "Dharwad Pedha": ("धारवाड़ पेड़ा", "धारवाड पेढा"),
 "Mysore Silk": ("मैसूर सिल्क", "म्हैसूर सिल्क"),
 "Bidriware": ("बिदरी शिल्प", "बिदरी कला"),
 "Channapatna Toys And Dolls": ("चन्नपट्टण खिलौने और गुड़िया", "चन्नपट्टण खेळणी व बाहुल्या"),
 "Mysore Rosewood Inlay": ("मैसूर शीशम पच्चीकारी", "म्हैसूर शिसवी जडावकाम"),
 "Kasuti Embroidery": ("कसूती कढ़ाई", "कसूती भरतकाम"),
 "Mysore Traditional Paintings": ("मैसूर पारंपरिक चित्रकला", "म्हैसूर पारंपरिक चित्रकला"),
 "Ganjifa Cards of Mysore": ("मैसूर के गंजीफ़ा पत्ते", "म्हैसूरचे गंजिफा पत्ते"),
 "Navalgund Durries": ("नवलगुंद दरियाँ", "नवलगुंद सतरंज्या"),
 "Karnataka Bronzeware": ("कर्नाटक काँसा शिल्प", "कर्नाटक कांस्यकला"),
 "Ilkal Sarees": ("इलकल साड़ियाँ", "इळकल साड्या"),
 "Molakalmuru Sarees": ("मोलकालमुरु साड़ियाँ", "मोळकाल्मुरू साड्या"),
 "Sandur Lambani Embroidery": ("संडूर लंबाणी कढ़ाई", "संडूर लमाणी भरतकाम"),
 "Guledgudd Khana": ("गुलेदगुड्ड खण", "गुळेदगुड्ड खण"),
 "Kinhal Toys": ("किन्हाल खिलौने", "किन्हाळ खेळणी"),
 "Udupi Sarees": ("उडुपी साड़ियाँ", "उडुपी साड्या"),
 "Karnataka Bronzeware (Logo)": ("कर्नाटक काँसा शिल्प (लोगो)", "कर्नाटक कांस्यकला (बोधचिन्ह)"),
 "Ganjifa cards of Mysore (Logo)": ("मैसूर के गंजीफ़ा पत्ते (लोगो)", "म्हैसूरचे गंजिफा पत्ते (बोधचिन्ह)"),
 "Navalgund Durries (Logo)": ("नवलगुंद दरियाँ (लोगो)", "नवलगुंद सतरंज्या (बोधचिन्ह)"),
 "Mysore Silk (Logo)": ("मैसूर सिल्क (लोगो)", "म्हैसूर सिल्क (बोधचिन्ह)"),
 "Patteda Anchu Saree & Fabrics": ("पट्टेद अंचु साड़ी और वस्त्र", "पट्टेद अंचू साडी व वस्त्रे"),
 "Mysore Agarbathi": ("मैसूर अगरबत्ती", "म्हैसूर अगरबत्ती"),
 "Mysore Sandalwood Oil": ("मैसूर चंदन तेल", "म्हैसूर चंदनाचे तेल"),
 "Mysore Sandal Soap": ("मैसूर चंदन साबुन", "म्हैसूर चंदनी साबण"),
}
TEXTILE = {"Mysore Silk", "Kasuti Embroidery", "Navalgund Durries", "Ilkal Sarees", "Molakalmuru Sarees", "Sandur Lambani Embroidery",
           "Guledgudd Khana", "Udupi Sarees", "Navalgund Durries (Logo)", "Mysore Silk (Logo)", "Patteda Anchu Saree & Fabrics"}
r["giProducts"] = gi_list("gi_ka.tsv", GI_NAMES, {}, TEXTILE)
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-KA.json", r)
print("ka core ok", len(r["giProducts"]), "GIs")
