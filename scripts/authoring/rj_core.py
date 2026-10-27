"""Rajasthan — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-16."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.newsonair.gov.in/haribhau-kisanrao-bagde-takes-oath-as-governor-of-rajasthan-at-raj-bhawan/"
CM = "https://www.tribuneindia.com/news/rajasthan/bhajan-lal-takes-oath-as-rajasthans-14th-chief-minister-572282"
SPK = "https://www.dailypioneer.com/2023/india/vasudev-picked-as-rajasthan-speaker.html"
REF_APR = "https://www.pmindia.gov.in/?p=16831064"
REF_JUL = "https://www.pmindia.gov.in/en/news_updates/pm-dedicates-inaugurates-and-lays-the-foundation-stone-for-development-projects-worth-around-%e2%82%b91-06-lakh-crore-in-balotra-rajasthan/"
PKC = "https://www.newsonair.gov.in/pm-modi-to-inaugurate-24-development-projects-in-rajasthan-worth-over-%e2%82%b946300-crore"

rj = research("mospi_rj.json")
r = read("regions/IN-RJ.json")
m = r["metrics"]
m["population2011"] = dp(68548437, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 3,55,50,997; females 3,29,97,440.")
m["area"] = dp(342239, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026). The largest of India's States.")
m["density2011"] = dp(200, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 6,85,48,437 ÷ area 3,42,239 km² = 200.3.")
m["sexRatio2011"] = dp(928, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (921 in 2001).")
m["childSexRatio2011"] = dp(888, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 909 in 2001.")
m["literacyRate2011"] = dp(66.1, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(rj["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25: ₹{inr(rj['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(rj["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(rj['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(4.84, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 16,548.21 km² ÷ geographical area 3,42,239 km².")

r["officialPortal"] = "https://rajasthan.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Chinkara (wild animal); camel (livestock animal)", "चिंकारा (वन्य पशु); ऊँट (पालतू पशु)", "चिंकारा (वन्य प्राणी); उंट (पाळीव प्राणी)", "Gazella bennettii; Camelus dromedarius"),
    "bird": sym("Great Indian bustard (godawan)", "गोडावण (सोन चिरैया)", "माळढोक (गोडावण)", "Ardeotis nigriceps"),
    "flower": sym("Rohida", "रोहिड़ा", "रोहिडा", "Tecomella undulata"),
    "tree": sym("Khejri", "खेजड़ी", "खेजडी (शमी)", "Prosopis cineraria"),
}

r["government"] = {
    "headOfState": office("governor", L("Haribhau Kisanrao Bagde", "हरिभाऊ किसनराव बागडे", "हरिभाऊ किसनराव बागडे"), None, "2024-07-31",
                          "newsonair", GOV, "https://igod.gov.in",
                          note="Sworn in at Raj Bhavan, Jaipur, by Chief Justice Manindra Mohan Shrivastava on 31 July 2024 (News On AIR). Former Speaker of the Maharashtra Legislative Assembly."),
    "headOfGovernment": office("chief-minister", L("Bhajan Lal Sharma", "भजनलाल शर्मा", "भजनलाल शर्मा"), "BJP", "2023-12-15",
                               "tribune", CM, "https://rajasthan.gov.in", conf="Third-party verified",
                               note="Sworn in on 15 December 2023 as Rajasthan's 14th Chief Minister (The Tribune). No change of Chief Minister was found in 2026 sources; confirm on the State portal."),
    "others": [
        office('deputy-chief-minister', L('Diya Kumari', 'दीया कुमारी', 'दिया कुमारी'), 'BJP', '2023-12-15', 'newsonair', 'https://www.newsonair.gov.in/rajasthan-deputy-cm-finance-minister-diya-kumari-presents-budget-2026-27-in-assembly', 'https://rajasthan.gov.in', note='Official confirmation: News On AIR 11 Feb 2026: Deputy Chief Minister and Finance Minister Diya Kumari presented the budget. Sworn in with the Chief Minister (The Tribune).', as_of='2026-10-27'),
        office("deputy-chief-minister", L("Prem Chand Bairwa", "प्रेमचंद बैरवा", "प्रेमचंद बैरवा"), "BJP", "2023-12-15", "tribune", CM, "https://rajasthan.gov.in",
               conf="Third-party verified", note="Sworn in with the Chief Minister (The Tribune)."),
        office("speaker", L("Vasudev Devnani", "वासुदेव देवनानी", "वासुदेव देवनानी"), "BJP", "2023-12-20", "pioneer", SPK, "https://assembly.rajasthan.gov.in",
               conf="Third-party verified", note="Elected unopposed in December 2023 (The Pioneer). Confirm the date on the Assembly website."),
    ],
}

r["projects"] = [
    proj("rajasthan-refinery", L("Rajasthan Refinery (HPCL), Pachpadra", "राजस्थान रिफ़ाइनरी (एचपीसीएल), पचपदरा", "राजस्थान रिफायनरी (एचपीसीएल), पचपदरा"),
         L("India's first greenfield integrated refinery-cum-petrochemical complex, with a refining capacity of 9 million tonnes a year and 2.4 million tonnes of petrochemicals, built as a joint venture of HPCL and the Government of Rajasthan. The Prime Minister dedicated it to the nation at Balotra on 4 July 2026.",
           "भारत का पहला ग्रीनफ़ील्ड एकीकृत रिफ़ाइनरी-सह-पेट्रोरसायन परिसर, जिसकी शोधन क्षमता 90 लाख टन प्रति वर्ष और पेट्रोरसायन क्षमता 24 लाख टन है, एचपीसीएल और राजस्थान सरकार के संयुक्त उद्यम के रूप में बना। प्रधानमंत्री ने 4 जुलाई 2026 को बालोतरा में इसे राष्ट्र को समर्पित किया।",
           "भारतातील पहिले ग्रीनफिल्ड एकात्मिक रिफायनरी-सह-पेट्रोरसायन संकुल, वार्षिक 90 लाख टन शुद्धीकरण व 24 लाख टन पेट्रोरसायन क्षमतेचे, एचपीसीएल व राजस्थान सरकारच्या संयुक्त उपक्रमातून उभारलेले. पंतप्रधानांनी 4 जुलै 2026 रोजी बालोतरा येथे ते राष्ट्राला समर्पित केले."),
         "industry", "HPCL Rajasthan Refinery Ltd (HPCL–Government of Rajasthan JV)", 79450, "Over ₹79,450 crore (PMO release of April 2026).", "2026", "2018", "4 July 2026", "Completed", "pmindia", REF_JUL,
         challenges=L("Commissioning was delayed for years and the cost was revised upwards.", "चालू होने में वर्षों की देरी हुई और लागत ऊपर संशोधित हुई।", "कार्यान्वयनास अनेक वर्षे विलंब झाला व खर्च वाढवून सुधारला गेला.")),
    proj("jaipur-metro-2", L("Jaipur Metro Phase 2", "जयपुर मेट्रो चरण 2", "जयपूर मेट्रो टप्पा 2"),
         L("A north–south metro line for Jaipur that will take the city's network beyond 50 km and connect with the existing east–west line. The Prime Minister laid the foundation stone on 4 July 2026.",
           "जयपुर के लिए उत्तर–दक्षिण मेट्रो लाइन, जो शहर के नेटवर्क को 50 किमी से आगे ले जाएगी और मौजूदा पूर्व–पश्चिम लाइन से जुड़ेगी। प्रधानमंत्री ने 4 जुलाई 2026 को इसकी आधारशिला रखी।",
           "जयपूरसाठी उत्तर–दक्षिण मेट्रो मार्गिका, जी शहराचे जाळे 50 किमीच्या पुढे नेईल व सध्याच्या पूर्व–पश्चिम मार्गिकेला जोडेल. पंतप्रधानांनी 4 जुलै 2026 रोजी पायाभरणी केली."),
         "urban", "Jaipur Metro Rail Corporation", None, None, None, "July 2026", None, "Under Construction", "pmindia", REF_JUL),
    proj("ramjal-setu", L("Ramjal Setu (Parbati–Kalisindh–Chambal–ERCP) link project", "रामजल सेतु (पार्बती–कालीसिंध–चंबल–ईआरसीपी) लिंक परियोजना", "रामजल सेतू (पार्बती–कालीसिंध–चंबळ–ईआरसीपी) जोड प्रकल्प"),
         L("A river-linking project to carry water from the Parbati, Kalisindh and Chambal basins to eastern Rajasthan and parts of Madhya Pradesh for drinking water and irrigation. Rajasthan and Madhya Pradesh signed an agreement in the Prime Minister's presence at Jaipur on 17 December 2024.",
           "पार्बती, कालीसिंध और चंबल बेसिन से पूर्वी राजस्थान और मध्य प्रदेश के कुछ भागों तक पेयजल और सिंचाई के लिए पानी ले जाने वाली नदी-जोड़ परियोजना। राजस्थान और मध्य प्रदेश ने 17 दिसंबर 2024 को जयपुर में प्रधानमंत्री की उपस्थिति में समझौता किया।",
           "पार्बती, कालीसिंध व चंबळ खोऱ्यांतून पूर्व राजस्थान व मध्य प्रदेशच्या काही भागांत पिण्यासाठी व सिंचनासाठी पाणी नेणारा नदीजोड प्रकल्प. राजस्थान व मध्य प्रदेशने 17 डिसेंबर 2024 रोजी जयपूर येथे पंतप्रधानांच्या उपस्थितीत करार केला."),
         "water", "Governments of Rajasthan and Madhya Pradesh / Ministry of Jal Shakti", None, None, None, None, None, "Announced", "newsonair", PKC,
         challenges=L("Approved cost, phasing and land acquisition to be confirmed from official sources.", "स्वीकृत लागत, चरण और भूमि अधिग्रहण की पुष्टि आधिकारिक स्रोतों से करनी है।", "मंजूर खर्च, टप्पे व भूसंपादन यांची अधिकृत स्रोतांतून खात्री करायची आहे.")),
]

GI_NAMES = {
 "Sojat Mehndi": ("सोजत मेहंदी", "सोजत मेंदी"),
 "Nagori Ashwagandha": ("नागौरी अश्वगंधा", "नागौरी अश्वगंधा"),
 "Bikaneri Bhujia": ("बीकानेरी भुजिया", "बिकानेरी भुजिया"),
 "Kota Doria": ("कोटा डोरिया", "कोटा डोरिया"),
 "Blue Pottery of Jaipur": ("जयपुर की ब्लू पॉटरी", "जयपूरची निळी मृद्भांडी"),
 "Molela Clay Work": ("मोलेला मृण्मूर्ति शिल्प", "मोलेला मातीकाम"),
 "Kathputlis of Rajasthan": ("राजस्थान की कठपुतलियाँ", "राजस्थानच्या कठपुतळ्या"),
 "Sanganeri Hand Block Printing": ("सांगानेरी हाथ ठप्पा छपाई", "सांगानेरी हस्त ठसे छपाई"),
 "Bagru Hand Block Print": ("बगरू हाथ ठप्पा छपाई", "बगरू हस्त ठसे छपाई"),
 "Kota Doria (Logo)": ("कोटा डोरिया (लोगो)", "कोटा डोरिया (बोधचिन्ह)"),
 "Thewa Art Work": ("थेवा कला", "थेवा कला"),
 "Pokaran Pottery": ("पोकरण मिट्टी के बर्तन", "पोखरण मृद्भांडी"),
 "Molela Clay Work of Rajasthan (Logo)": ("राजस्थान का मोलेला मृण्मूर्ति शिल्प (लोगो)", "राजस्थानचे मोलेला मातीकाम (बोधचिन्ह)"),
 "Blue Pottery of Jaipur (Logo)": ("जयपुर की ब्लू पॉटरी (लोगो)", "जयपूरची निळी मृद्भांडी (बोधचिन्ह)"),
 "Kathputlis of Rajasthan (Logo)": ("राजस्थान की कठपुतलियाँ (लोगो)", "राजस्थानच्या कठपुतळ्या (बोधचिन्ह)"),
 "Nathdwara Pichhwai Painting": ("नाथद्वारा पिछवाई चित्रकला", "नाथद्वारा पिछवाई चित्रकला"),
 "Udaipur Koftgari Metal Craft": ("उदयपुर कोफ़्तगरी धातु शिल्प", "उदयपूर कोफ्तगरी धातुकला"),
 "Bikaner Kashidakari Craft": ("बीकानेर कशीदाकारी शिल्प", "बिकानेर कशिदाकारी कला"),
 "Jodhpur Bandhej Craft": ("जोधपुर बंधेज शिल्प", "जोधपूर बांधणी कला"),
 "Bikaner Usta Kala Craft": ("बीकानेर उस्ता कला", "बिकानेर उस्ता कला"),
 "Makrana Marble": ("मकराना संगमरमर", "मकराना संगमरवर"),
 "Phulkari": ("फुलकारी", "फुलकारी"),
}
TEXTILE = {"Kota Doria", "Kota Doria (Logo)", "Sanganeri Hand Block Printing", "Bagru Hand Block Print", "Bikaner Kashidakari Craft", "Jodhpur Bandhej Craft", "Phulkari"}
r["giProducts"] = gi_list("gi_rj.tsv", GI_NAMES, {"PB,HR,RJ": ["Punjab", "Haryana"]}, TEXTILE)
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-RJ.json", r)
print("rj core ok", len(r["giProducts"]), "GIs")
