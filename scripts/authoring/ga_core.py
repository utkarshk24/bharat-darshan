"""Goa — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-24."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://dip.goa.gov.in/pusapati-ashok-gajapathi-raju-sworn-in-as-governor/"
CM = "https://www.theweek.in/news/india/2022/03/28/pramod-sawant-takes-oath-goa-cm.html"
SPK = "https://www.newsonair.gov.in/bjp-mla-ganesh-gaonkar-elected-speaker-of-goa-legislative-assembly"
MOPA = "https://www.deccanherald.com/amp/story/india%2Fpm-modi-inaugurates-first-phase-of-mopa-international-airport-in-goa-1170718.html"

mo = research("mospi_ga.json")
r = read("regions/IN-GA.json")
m = r["metrics"]
m["population2011"] = dp(1458545, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 7,39,140; females 7,19,405.")
m["area"] = dp(3702, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(394, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 14,58,545 ÷ area 3,702 km² = 394.0.")
m["sexRatio2011"] = dp(973, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (961 in 2001).")
m["childSexRatio2011"] = dp(942, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 938 in 2001.")
m["literacyRate2011"] = dp(88.7, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25 is the latest year published for Goa. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2023-24: ₹{inr(mo['pcnsdp']['FY2023-24'][0])}. Second only to Sikkim among the 30 regions with a FY2024-25 figure in the MoSPI series.")
m["forestCoverPct"] = dp(61.20, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 2,265.72 km² ÷ geographical area 3,702 km².")

r["officialPortal"] = "https://www.goa.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Gaur", "गौर (भारतीय बाइसन)", "गवा", "Bos gaurus"),
    "bird": sym("Flame-throated bulbul", "लाल-कंठ बुलबुल", "लालकंठी बुलबुल", "Rubigula gularis"),
    "tree": sym("Matti (crocodile bark)", "मत्ती (असन)", "माटी (ऐन)", "Terminalia elliptica"),
}

r["government"] = {
    "headOfState": office("governor", L("Pusapati Ashok Gajapathi Raju", "पुसपति अशोक गजपति राजू", "पुसपती अशोक गजपती राजू"), None, "2025-07-26",
                          "goa-dip", GOV, "https://lokbhavan.goa.gov.in",
                          note="Sworn in as the 22nd Governor of Goa at Raj Bhavan, Dona Paula, on 26 July 2025 by Chief Justice Alok Aradhe of the Bombay High Court; succeeded P. S. Sreedharan Pillai (Department of Information and Publicity, Goa)."),
    "headOfGovernment": office('chief-minister', L('Pramod Sawant', 'प्रमोद सावंत', 'प्रमोद सावंत'), 'BJP', '2022-03-28', 'goa-gov', 'https://www.goa.gov.in/wp-content/uploads/2026/05/CHIEF-MINISTER-EXTENDS-GREETINGS.pdf', 'https://www.goa.gov.in', note='Official confirmation: Government of Goa press note, Panaji 29 May 2026: Chief Minister Dr Pramod Sawant extended greetings. Sworn in for a second term on 28 March 2022 at the Dr Syama Prasad Mookerjee stadium, Bambolim, by Governor P. S. Sreedharan Pillai, with eight ministers; MLA from Sanquelim (PTI via The Week). He first became Chief Minister in March 2019.', as_of='2026-10-27'),
    "others": [
        office("speaker", L("Ganesh Gaonkar", "गणेश गावकर", "गणेश गावकर"), "BJP", "2025-09-25", "newsonair", SPK, "https://goavidhansabha.gov.in", conf="Official",
               note="Elected Speaker on 25 September 2025 with 31 votes against 7, after Ramesh Tawadkar resigned to join the Cabinet (News On AIR); MLA from Sanvordem."),
    ],
}

r["projects"] = [
    proj("mopa-airport", L("Manohar International Airport, Mopa", "मनोहर अंतरराष्ट्रीय हवाई अड्डा, मोपा", "मनोहर आंतरराष्ट्रीय विमानतळ, मोपा"),
         L("A greenfield international airport at Mopa in Pernem taluka, North Goa, named after former Chief Minister Manohar Parrikar. Its first phase, with a capacity of about 40 lakh passengers a year that can be expanded to about 3.5 crore, was inaugurated by the Prime Minister on 11 December 2022. Goa's older airport at Dabolim, a civil enclave at a naval air station, continues to operate.",
           "उत्तर गोवा के पेरनेम तालुका के मोपा में नया अंतरराष्ट्रीय हवाई अड्डा, जिसका नाम पूर्व मुख्यमंत्री मनोहर पर्रिकर के नाम पर है। इसके पहले चरण का, जिसकी क्षमता प्रति वर्ष लगभग 40 लाख यात्रियों की है और जिसे लगभग 3.5 करोड़ तक बढ़ाया जा सकता है, प्रधानमंत्री ने 11 दिसंबर 2022 को उद्घाटन किया। नौसेना हवाई स्टेशन पर नागरिक परिसर के रूप में गोवा का पुराना डाबोलिम हवाई अड्डा भी चलता रहता है।",
           "उत्तर गोव्याच्या पेडणे तालुक्यातील मोपा येथील नवा आंतरराष्ट्रीय विमानतळ, ज्याला माजी मुख्यमंत्री मनोहर पर्रीकर यांचे नाव दिले आहे. वर्षाला सुमारे 40 लाख प्रवासी क्षमतेच्या व सुमारे 3.5 कोटींपर्यंत वाढवता येणाऱ्या त्याच्या पहिल्या टप्प्याचे पंतप्रधानांनी 11 डिसेंबर 2022 रोजी उद्घाटन केले. नौदल हवाई तळावरील नागरी विभाग म्हणून गोव्याचा जुना दाबोळी विमानतळही सुरू आहे."),
         "aviation", "GMR Goa International Airport Ltd (concessionaire)", None, None, None, None, "11 December 2022 (phase 1)", "Completed", "deccan-herald", MOPA, conf="Third-party verified"),
]

GI_NAMES = {
 "Khola Chilli": ("खोला मिर्च", "खोला मिरची"),
 "Harmal Chilli": ("हरमल मिर्च", "हरमल मिरची"),
 "Myndoli Banana": ("मैंदोली केला", "मैंदोळी केळे"),
 "Goa Cashew (Kaju or Caju)": ("गोवा काजू", "गोवा काजू"),
 "Agsechi Vayingim (Agassaim Brinjal)": ("आगशी वायंगिम (आगशी बैंगन)", "आगशी वायंगी (आगशी वांगे)"),
 "Sat Shiro Bheno (Sat Shirancho Bhendo)": ("सात शिरांचो भेंडो (सात धारियों वाली भिंडी)", "सात शिरांचो भेंडो (सात शिरांची भेंडी)"),
 "Goa Mankurad Mango": ("गोवा मानकुराद आम", "गोवा मानकुराद आंबा"),
 "Taleigao Vayingim (Taleigao Brinjal)": ("ताळगाँव वायंगिम (ताळगाँव बैंगन)", "ताळगाव वायंगी (ताळगाव वांगे)"),
 "Goa Hilario Mango": ("गोवा हिलारियो आम", "गोवा हिलारियो आंबा"),
 "Goa Korgut Rice": ("गोवा कोरगुट चावल", "गोवा कोरगुट तांदूळ"),
 "Goa Kaju Apple": ("गोवा काजू फल", "गोवा काजूबोंड"),
 "Goa Mussarad Mango": ("गोवा मुसराद आम", "गोवा मुसराद आंबा"),
 "Goan Khaje": ("गोवा खाजे", "गोमंतकीय खाजे"),
 "Goan Bebinca": ("गोवा बेबिंका", "गोमंतकीय बेबिंका"),
 "Feni": ("फ़ेनी", "फेणी"),
}
r["giProducts"] = gi_list("gi_ga.tsv", GI_NAMES, {}, set())
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-GA.json", r)
print("ga core ok", len(r["giProducts"]), "GIs")
