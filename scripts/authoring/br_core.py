"""Bihar — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-16."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.newsonair.gov.in/bihar-lieutenant-general-retired-syed-ata-hasnain-takes-oath-as-43rd-governor-of-state"
CM = "https://newsonair.gov.in/pm-modi-congratulates-samrat-choudhary-on-taking-oath-as-cm-of-bihar/"
CM_PRE = "https://www.newsonair.gov.in/bihar-samrat-choudhary-elected-as-bjp-legislature-party-leader/"
SPK = "https://www.newsonair.gov.in/senior-bjp-leader-dr-prem-kumar-elected-new-speaker-of-18th-bihar-legislative-assembly/"
AIIMS = "https://www.newsonair.gov.in/pm-modi-to-visit-darbhanga-bihar-to-inaugurate-and-launch-development-projects-worth-over-%e2%82%b912000-crore"
METRO = "https://www.newsonair.gov.in/bihar-chief-minister-nitish-kumar-to-inaugurate-first-phase-of-patna-metro-rail-service-today"

br = research("mospi_br.json")
r = read("regions/IN-BR.json")
m = r["metrics"]
m["population2011"] = dp(104099452, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 5,42,78,157; females 4,98,21,295.")
m["area"] = dp(94163, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(1106, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 10,40,99,452 ÷ area 94,163 km² = 1,105.5 — the highest of any State.")
m["sexRatio2011"] = dp(918, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (919 in 2001).")
m["childSexRatio2011"] = dp(935, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 942 in 2001.")
m["literacyRate2011"] = dp(61.8, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(br["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25: ₹{inr(br['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(br["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(br['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(8.00, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 7,532.45 km² ÷ geographical area 94,163 km².")

r["officialPortal"] = "https://state.bihar.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Gaur (Indian bison)", "गौर (भारतीय बाइसन)", "गवा", "Bos gaurus"),
    "bird": sym("House sparrow", "गौरैया", "चिमणी", "Passer domesticus"),
    "flower": sym("Marigold", "गेंदा", "झेंडू", "Tagetes erecta"),
    "tree": sym("Peepal", "पीपल", "पिंपळ", "Ficus religiosa"),
}

r["government"] = {
    "headOfState": office("governor", L("Syed Ata Hasnain", "सैयद अता हसनैन", "सय्यद अता हसनैन"), None, "2026-03-14",
                          "newsonair", GOV, "https://governor.bih.nic.in",
                          note="Lt Gen (Retd). Appointed by the President's communiqué of 5 March 2026; sworn in as the 43rd Governor of Bihar at Lok Bhavan, Patna, on 14 March 2026 by Patna High Court Chief Justice Sangam Kumar Sahu (News On AIR)."),
    "headOfGovernment": office("chief-minister", L("Samrat Choudhary", "सम्राट चौधरी", "सम्राट चौधरी"), "BJP", "2026-04-15",
                               "newsonair", CM, "https://state.bihar.gov.in",
                               note="Elected leader of the NDA legislature party on 14 April 2026 after Nitish Kumar resigned on election to the Rajya Sabha; sworn in on 15 April 2026 at Lok Bhavan, Patna (News On AIR)."),
    "others": [
        office("deputy-chief-minister", L("Vijay Kumar Chaudhary", "विजय कुमार चौधरी", "विजय कुमार चौधरी"), "JD(U)", "2026-04-15", "newsonair", CM, "https://state.bihar.gov.in",
               note="Named as Deputy Chief Minister in the Prime Minister's congratulations of 15 April 2026 (News On AIR)."),
        office("deputy-chief-minister", L("Bijendra Prasad Yadav", "बिजेंद्र प्रसाद यादव", "बिजेंद्र प्रसाद यादव"), "JD(U)", "2026-04-15", "newsonair", CM, "https://state.bihar.gov.in",
               note="Named as Deputy Chief Minister in the Prime Minister's congratulations of 15 April 2026 (News On AIR)."),
        office("speaker", L("Prem Kumar", "प्रेम कुमार", "प्रेम कुमार"), "BJP", "2025-12-02", "newsonair", SPK, "https://vidhansabha.bih.nic.in",
               note="Elected Speaker of the 18th Bihar Legislative Assembly on 2 December 2025 (News On AIR). Nine-time MLA from Gaya Town."),
    ],
}

r["projects"] = [
    proj("patna-metro", L("Patna Metro — priority corridor", "पटना मेट्रो — प्राथमिकता गलियारा", "पाटणा मेट्रो — प्राधान्य मार्गिका"),
         L("The first elevated stretch of about 3.6 km between the Inter-State Bus Terminal and Bhootnath, inaugurated on 6 October 2025, with passenger services from the next day — Bihar's first metro.",
           "अंतरराज्यीय बस टर्मिनल और भूतनाथ के बीच लगभग 3.6 किमी का पहला एलिवेटेड खंड, 6 अक्टूबर 2025 को उद्घाटित, और अगले दिन से यात्री सेवा — बिहार की पहली मेट्रो।",
           "आंतरराज्य बस टर्मिनल व भूतनाथदरम्यानचा सुमारे 3.6 किमीचा पहिला उन्नत टप्पा, 6 ऑक्टोबर 2025 रोजी उद्घाटित, आणि दुसऱ्या दिवसापासून प्रवासी सेवा — बिहारची पहिली मेट्रो."),
         "urban", "Patna Metro Rail Corporation", None, None, None, None, "6 October 2025", "Completed", "newsonair", METRO),
    proj("aiims-darbhanga", L("AIIMS Darbhanga", "एम्स दरभंगा", "एम्स दरभंगा"),
         L("Bihar's second AIIMS, with a super-speciality hospital, AYUSH block, medical and nursing colleges and housing. The Prime Minister laid the foundation stone on 13 November 2024; it was expected to take about three years.",
           "बिहार का दूसरा एम्स, जिसमें सुपर-स्पेशियलिटी अस्पताल, आयुष ब्लॉक, मेडिकल और नर्सिंग कॉलेज और आवास होंगे। प्रधानमंत्री ने 13 नवंबर 2024 को इसकी आधारशिला रखी; इसमें लगभग तीन वर्ष लगने की अपेक्षा थी।",
           "बिहारचे दुसरे एम्स, ज्यात सुपर-स्पेशालिटी रुग्णालय, आयुष विभाग, वैद्यकीय व परिचारिका महाविद्यालये आणि निवासस्थाने असतील. पंतप्रधानांनी 13 नोव्हेंबर 2024 रोजी पायाभरणी केली; सुमारे तीन वर्षे लागणे अपेक्षित होते."),
         "health", "Ministry of Health and Family Welfare", 1260, "Over ₹1,260 crore (News On AIR).", "2024", "November 2024", "c. 2027 (expected)", "Under Construction", "newsonair", AIIMS),
]

GI_NAMES = {
 "Bhagalpuri Zardalu": ("भागलपुरी ज़र्दालू (आम)", "भागलपुरी जर्दाळू (आंबा)"),
 "Shahi Litchi of Bihar": ("बिहार की शाही लीची", "बिहारची शाही लिची"),
 "Katarni Rice": ("कतरनी चावल", "कतरनी तांदूळ"),
 "Magahi Paan": ("मगही पान", "मगही पान"),
 "Mithila Makhana": ("मिथिला मखाना", "मिथिला मखाणा"),
 "Marcha Rice": ("मर्चा चावल", "मर्चा तांदूळ"),
 "Silao Khaja": ("सिलाव खाजा", "सिलाव खाजा"),
 "Madhubani Painting": ("मधुबनी चित्रकला", "मधुबनी चित्रकला"),
 "Applique (Khatwa) Work of Bihar": ("बिहार का एप्लिक (खटवा) काम", "बिहारचे ऍप्लिक (खटवा) काम"),
 "Sujini Embroidery Work of Bihar": ("बिहार की सुजनी कढ़ाई", "बिहारचे सुजनी भरतकाम"),
 "Sikki Grass Products of Bihar": ("बिहार के सिक्की घास उत्पाद", "बिहारची सिक्की गवत उत्पादने"),
 "Bhagalpur Silk": ("भागलपुरी रेशम", "भागलपुरी रेशीम"),
 "Sikki Grass Products of Bihar (Logo)": ("बिहार के सिक्की घास उत्पाद (लोगो)", "बिहारची सिक्की गवत उत्पादने (बोधचिन्ह)"),
 "Applique (Khatwa) Work of Bihar (Logo)": ("बिहार का एप्लिक (खटवा) काम (लोगो)", "बिहारचे ऍप्लिक (खटवा) काम (बोधचिन्ह)"),
 "Sujini Embroidery Work of Bihar (Logo)": ("बिहार की सुजनी कढ़ाई (लोगो)", "बिहारचे सुजनी भरतकाम (बोधचिन्ह)"),
 "Manjusha Art": ("मंजूषा कला", "मंजूषा कला"),
}
TEXTILE = {"Bhagalpur Silk", "Applique (Khatwa) Work of Bihar", "Applique (Khatwa) Work of Bihar (Logo)", "Sujini Embroidery Work of Bihar", "Sujini Embroidery Work of Bihar (Logo)"}
r["giProducts"] = gi_list("gi_br.tsv", GI_NAMES, {}, TEXTILE)
for g in r["giProducts"]:
    if g["applicationNo"] in ("536", "537", "538"):
        g["note"] += " The GI Registry's list prints this second registration without the word 'Logo'; it was filed on 28 Dec 2015 together with other logo marks and is treated here as the logo registration."
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-BR.json", r)
print("br core ok", len(r["giProducts"]), "GIs")
