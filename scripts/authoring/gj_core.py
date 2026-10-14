"""Gujarat — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-14."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
NOA_GOV = "https://newsonair.gov.in/governor-acharya-devvrat-cm-bhupendra-patel-deputy-cm-harsh-sanghvi-extend-their-greetings-to-people-on-occasion-of-dhuleti/"
NOA_RESHUFFLE = "https://newsonair.gov.in/gujarat-cabinet-reshuffle-all-16-ministers-resign-ahead-of-strategic-reset/"
SPK = "https://theprint.in/india/shankar-chaudhary-elected-unopposed-as-speaker-of-gujarat-assembly/1272525/"
HSR = "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2272190&lang=1&reg=48"
FAB = "https://www.pmindia.gov.in/en/news_updates/pm-to-participate-in-indias-techade-chips-for-viksit-bharat-and-lay-the-foundation-stone-of-three-semiconductor-facilities-worth-about-rs-1-25-lakh-crore-on-13th-march/"

gj = research("mospi_gj.json")
r = read("regions/IN-GJ.json")
m = r["metrics"]
m["population2011"] = dp(60439692, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 3,14,91,260; females 2,89,48,432.")
m["area"] = dp(196244, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026); NITI Aayog also gives 1,96,244 km².")
m["density2011"] = dp(308, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 6,04,39,692 ÷ area 1,96,244 km² = 308.0.")
m["sexRatio2011"] = dp(919, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (920 in 2001).")
m["childSexRatio2011"] = dp(890, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 883 in 2001.")
m["literacyRate2011"] = dp(78.0, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011). Was 69.1% in 2001.")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: the State's Socio-Economic Review gives only rounded totals (urban 2.57 crore of 6.04 crore). Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(gj["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25: ₹{inr(gj['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(gj["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(gj['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(7.65, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 15,016.64 km² ÷ geographical area 1,96,244 km².")

r["officialPortal"] = "https://gujaratindia.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Asiatic lion", "एशियाई सिंह", "आशियाई सिंह", "Panthera leo persica"),
    "bird": sym("Greater flamingo", "बड़ा राजहंस (फ़्लेमिंगो)", "मोठा रोहित (फ्लेमिंगो)", "Phoenicopterus roseus"),
    "flower": sym("Marigold", "गेंदा", "झेंडू", "Tagetes"),
    "tree": sym("Banyan", "बरगद", "वड", "Ficus benghalensis"),
}

r["government"] = {
    "headOfState": office("governor", L("Acharya Devvrat", "आचार्य देवव्रत", "आचार्य देवव्रत"), None, "2019-07-22",
                          "newsonair", NOA_GOV, "https://igod.gov.in",
                          note="Governor since July 2019; named as Governor in News On AIR's report of 4 March 2026. Confirm on the Raj Bhavan / Lok Bhavan, Gujarat website."),
    "headOfGovernment": office("chief-minister", L("Bhupendra Patel", "भूपेंद्र पटेल", "भूपेंद्र पटेल"), "BJP", "2021-09-13",
                               "newsonair", NOA_GOV, "https://gujaratindia.gov.in",
                               note="Chief Minister since 13 September 2021; sworn in for a second term on 12 December 2022 after the Assembly election. Named as Chief Minister by News On AIR on 4 March 2026."),
    "others": [
        office("deputy-chief-minister", L("Harsh Sanghavi", "हर्ष संघवी", "हर्ष संघवी"), "BJP", "2025-10-17", "newsonair", NOA_GOV, "https://gujaratindia.gov.in",
               note="Became Deputy Chief Minister in the October 2025 cabinet reshuffle; named as Deputy CM by News On AIR on 4 March 2026."),
        office("speaker", L("Shankar Chaudhary", "शंकर चौधरी", "शंकर चौधरी"), "BJP", "2022-12-20", "theprint", SPK, "https://gujaratassembly.gov.in",
               conf="Third-party verified", note="Elected unopposed on 20 December 2022 (ThePrint, PTI). Confirm on the Assembly website."),
    ],
}

r["projects"] = [
    proj("mahsr-gujarat", L("Mumbai–Ahmedabad High-Speed Rail (Gujarat section)", "मुंबई–अहमदाबाद हाई-स्पीड रेल (गुजरात खंड)", "मुंबई–अहमदाबाद अतिजलद रेल्वे (गुजरात भाग)"),
         L("A 508 km high-speed line, about 90% of it elevated. Eight of its 12 stations — Vapi, Bilimora, Surat, Bharuch, Vadodara, Anand, Ahmedabad and Sabarmati — and 21 of its 25 river bridges are in Gujarat. Track laying on the viaduct began in April 2026; the first service is expected in August 2027.",
           "508 किमी लंबी हाई-स्पीड लाइन, जिसका लगभग 90% हिस्सा एलिवेटेड है। इसके 12 में से 8 स्टेशन — वापी, बिलिमोरा, सूरत, भरूच, वडोदरा, आणंद, अहमदाबाद और साबरमती — और 25 में से 21 नदी पुल गुजरात में हैं। वायाडक्ट पर पटरी बिछाने का काम अप्रैल 2026 में शुरू हुआ; पहली सेवा अगस्त 2027 में अपेक्षित है।",
           "508 किमीचा अतिजलद रेल्वेमार्ग, ज्याचा सुमारे 90% भाग उन्नत आहे. त्याच्या 12 पैकी 8 स्थानके — वापी, बिलिमोरा, सुरत, भरूच, वडोदरा, आणंद, अहमदाबाद व साबरमती — आणि 25 पैकी 21 नदीपूल गुजरातमध्ये आहेत. व्हायाडक्टवर रूळ टाकण्याचे काम एप्रिल 2026 मध्ये सुरू झाले; पहिली सेवा ऑगस्ट 2027 मध्ये अपेक्षित आहे."),
         "transport", "NHSRCL", None, None, None, None, "First service expected August 2027", "Under Construction", "pib", HSR),
    proj("dholera-fab", L("Semiconductor fab, Dholera", "सेमीकंडक्टर फ़ैब, धोलेरा", "सेमीकंडक्टर फॅब, धोलेरा"),
         L("India's first commercial semiconductor fabrication plant, being set up by Tata Electronics in the Dholera Special Investment Region under the Modified Scheme for Semiconductor Fabs. The Prime Minister laid the foundation stone on 13 March 2024, together with an assembly-and-test (OSAT) unit at Sanand.",
           "भारत का पहला वाणिज्यिक सेमीकंडक्टर फ़ैब्रिकेशन संयंत्र, जिसे टाटा इलेक्ट्रॉनिक्स सेमीकंडक्टर फ़ैब की संशोधित योजना के तहत धोलेरा विशेष निवेश क्षेत्र में बना रही है। प्रधानमंत्री ने 13 मार्च 2024 को इसकी आधारशिला रखी, साथ में साणंद में एक असेंबली-एवं-परीक्षण (ओसैट) इकाई की भी।",
           "भारतातील पहिला व्यावसायिक सेमीकंडक्टर फॅब्रिकेशन प्रकल्प, जो टाटा इलेक्ट्रॉनिक्स सेमीकंडक्टर फॅबच्या सुधारित योजनेअंतर्गत धोलेरा विशेष गुंतवणूक क्षेत्रात उभारत आहे. पंतप्रधानांनी 13 मार्च 2024 रोजी पायाभरणी केली, सोबत साणंद येथील जुळणी-व-चाचणी (ओसॅट) युनिटचीही."),
         "industry", "Tata Electronics Private Limited", 91000, "Over ₹91,000 crore (PMO).", "2024",
         "March 2024", None, "Under Construction", "pmindia", FAB),
]

GI_NAMES = {
 "Gir Kesar Mango": ("गिर केसर आम", "गीर केशर आंबा"),
 "Bhalia Wheat": ("भालिया गेहूँ", "भालिया गहू"),
 "Kachchhi Kharek": ("कच्छी खारेक (छुहारा)", "कच्छी खारीक"),
 "Amalsad Chikoo": ("अमलसाड चीकू", "अमलसाड चिकू"),
 "Sankheda Furniture": ("संखेडा फ़र्नीचर", "संखेडा फर्निचर"),
 "Agates of Cambay": ("खंभात के अकीक", "खंबायतचे अकीक"),
 "Kutch Embroidery": ("कच्छ कढ़ाई", "कच्छ भरतकाम"),
 "Tangaliya Shawl": ("तंगलिया शॉल", "तंगलिया शाल"),
 "Surat Zari Craft": ("सूरत ज़री शिल्प", "सुरत जरीकाम"),
 "Kachchh Shawls": ("कच्छ शॉल", "कच्छ शाली"),
 "Jamnagari Bandhani": ("जामनगरी बांधनी", "जामनगरी बांधणी"),
 "Patan Patola": ("पाटन पटोला", "पाटण पटोला"),
 "RajKot Patola": ("राजकोट पटोला", "राजकोट पटोला"),
 "Sankheda Furniture (Logo)": ("संखेडा फ़र्नीचर (लोगो)", "संखेडा फर्निचर (बोधचिन्ह)"),
 "Agates of Cambay (Logo)": ("खंभात के अकीक (लोगो)", "खंबायतचे अकीक (बोधचिन्ह)"),
 "Kutch Embroidery (Logo)": ("कच्छ कढ़ाई (लोगो)", "कच्छ भरतकाम (बोधचिन्ह)"),
 "Pethapur Printing Blocks": ("पेथापुर छपाई ठप्पे", "पेथापूर छपाईचे ठसे"),
 "Pithora": ("पिथोरा चित्रकला", "पिथोरा चित्रकला"),
 "Mata ni Pachhedi": ("माता नी पछेडी", "माता नी पछेडी"),
 "Kutch Rogan Craft": ("कच्छ रोगन कला", "कच्छ रोगन कला"),
 "Kutch Bandhani": ("कच्छ बांधनी", "कच्छ बांधणी"),
 "Gharchola Craft of Gujarat": ("गुजरात का घरचोला शिल्प", "गुजरातचे घरचोळा वस्त्र"),
 "Gujarat Suf Embroidery": ("गुजरात सूफ़ कढ़ाई", "गुजरात सूफ भरतकाम"),
 "Ahmedabad Sodagari Block Print": ("अहमदाबाद सोदागरी ठप्पा छपाई", "अहमदाबाद सोदागरी ठसा छपाई"),
 "Surat Sadeli Craft": ("सूरत सादेली शिल्प", "सुरत सादेली कला"),
 "Bharuch Sujani Weaving": ("भरूच सुजनी बुनाई", "भरूच सुजनी विणकाम"),
 "Kutch Ajrakh": ("कच्छ अजरख", "कच्छ अजरख"),
 "Ambaji White Marble": ("अंबाजी सफ़ेद संगमरमर", "अंबाजी पांढरा संगमरवर"),
 "Surat Cut Diamond": ("सूरत तराशा हीरा", "सुरत पैलू पाडलेला हिरा"),
}
TEXTILE = {"Kutch Embroidery", "Tangaliya Shawl", "Surat Zari Craft", "Kachchh Shawls", "Jamnagari Bandhani", "Patan Patola", "RajKot Patola",
           "Kutch Embroidery (Logo)", "Mata ni Pachhedi", "Kutch Bandhani", "Gharchola Craft of Gujarat", "Gujarat Suf Embroidery",
           "Ahmedabad Sodagari Block Print", "Bharuch Sujani Weaving", "Kutch Ajrakh"}
r["giProducts"] = gi_list("gi_gj.tsv", GI_NAMES, {}, TEXTILE)
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-GJ.json", r)
print("gj core ok", len(r["giProducts"]), "GIs")
