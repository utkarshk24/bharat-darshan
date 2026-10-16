"""Assam — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-16."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
CAG_AS = "https://www.digitalreports.cag.gov.in/assam/chapter/1"
GOV = "https://www.newsonair.gov.in/lakshman-prasad-acharya-takes-oath-as-new-governor-of-assam"
CM = "https://newsonair.gov.in/senior-bjp-leader-himanta-biswa-sarma-to-be-sworn-in-as-cm-of-assam-in-guwahati-today/"
SPK = "https://newsonair.gov.in/ls-speaker-om-birla-congratulates-ranjeet-kumar-dass-on-election-as-assam-speaker/"
BOGI = "https://newindiasamachar.pib.gov.in/WriteReadData/flipbook/2026/Mar/1st/English/files/basic-html/page22.html"
TSAT = "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2024/nov/doc20241117435901.pdf"

r = read("regions/IN-AS.json")
m = r["metrics"]
m["population2011"] = dp(31205576, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 1,59,39,443; females 1,52,66,133.")
m["area"] = dp(78438, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(398, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 3,12,05,576 ÷ area 78,438 km² = 397.8.")
m["sexRatio2011"] = dp(958, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (935 in 2001).")
m["childSexRatio2011"] = dp(962, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 965 in 2001.")
m["literacyRate2011"] = dp(72.2, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(643667, "₹ crore", "FY2024-25", "fy", "cag", CAG_AS, rev="provisional", base=CUR,
    note="CAG, State Finances Audit Report of Assam 2024-25, chapter 1 (Table 1.2): GSDP at current prices ₹6,43,667 crore, growth 13.07% over the previous year; ₹3,39,803 crore in 2020-21. MoSPI's state-wise API had no Assam series at access time, so the CAG figure is used; the estimate type (advance, quick, revised) is not stated in the excerpt read.")
m["perCapitaNsdpCurrent"] = dp(159185, "₹", "FY2024-25", "fy", "cag", CAG_AS, rev="provisional", base=CUR,
    note="CAG, State Finances Audit Report of Assam 2024-25: per capita income ₹1,59,185 (₹86,947 in 2020-21). Assumed to be per capita NSDP at current prices; confirm against the Assam Economic Survey.")
m["forestCoverPct"] = dp(36.10, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 28,313.55 km² ÷ geographical area 78,438 km².")

r["officialPortal"] = "https://assam.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Indian one-horned rhinoceros", "एक सींग वाला गैंडा", "एकशिंगी गेंडा", "Rhinoceros unicornis"),
    "bird": sym("White-winged wood duck", "सफ़ेद पंखों वाली वन बत्तख़", "पांढऱ्या पंखांचे वनबदक", "Asarcornis scutulata"),
    "flower": sym("Foxtail orchid (kopou phool)", "कोपोउ फूल (फॉक्सटेल ऑर्किड)", "कोपोउ फूल (फॉक्सटेल ऑर्किड)", "Rhynchostylis retusa"),
    "tree": sym("Hollong", "होलोंग", "होलोंग", "Dipterocarpus retusus"),
}

r["government"] = {
    "headOfState": office("governor", L("Lakshman Prasad Acharya", "लक्ष्मण प्रसाद आचार्य", "लक्ष्मण प्रसाद आचार्य"), None, "2024-07-30",
                          "newsonair", GOV, "https://rajbhavan.assam.gov.in",
                          note="Sworn in on 30 July 2024; the oath was administered by Gauhati High Court Chief Justice Vijay Bishnoi (News On AIR). Administered the oath to the new Chief Minister on 12 May 2026."),
    "headOfGovernment": office("chief-minister", L("Himanta Biswa Sarma", "हिमंत बिस्व सरमा", "हिमंत बिस्व सरमा"), "BJP", "2026-05-12",
                               "newsonair", CM, "https://cm.assam.gov.in",
                               note="Sworn in for a second consecutive term on 12 May 2026 at the Veterinary College ground, Khanapara, Guwahati, after the NDA won 102 of the 126 seats — BJP 82, AGP 10, BPF 10 (News On AIR). First sworn in on 10 May 2021."),
    "others": [
        office("speaker", L("Ranjeet Kumar Dass", "रंजीत कुमार दास", "रंजीत कुमार दास"), None, "2026-05-21", "newsonair", SPK, "https://assamassembly.gov.in",
               note="Elected Speaker of the 16th Assam Legislative Assembly; the Lok Sabha Speaker's congratulations were reported on 21 May 2026 (News On AIR). Party and exact election date to be confirmed from the Assembly bulletin."),
    ],
}

r["projects"] = [
    proj("bogibeel", L("Bogibeel rail-cum-road bridge", "बोगीबील रेल-सह-सड़क पुल", "बोगीबील रेल्वे-सह-रस्ता पूल"),
         L("A 4.94 km double-deck bridge over the Brahmaputra between Dibrugarh and Dhemaji districts, with the road above and railway below — India's longest rail-cum-road bridge and its first fully steel bridge. Sanctioned in 1997 and opened on 25 December 2018, it cut the Dhemaji–Dibrugarh journey from about 500 km to 100 km.",
           "डिब्रूगढ़ और धेमाजी ज़िलों के बीच ब्रह्मपुत्र पर 4.94 किमी लंबा दो-मंज़िला पुल, ऊपर सड़क और नीचे रेल — भारत का सबसे लंबा रेल-सह-सड़क पुल और पहला पूर्णतः इस्पात का पुल। 1997 में स्वीकृत और 25 दिसंबर 2018 को खुले इस पुल ने धेमाजी–डिब्रूगढ़ की दूरी लगभग 500 किमी से घटाकर 100 किमी कर दी।",
           "डिब्रुगड व धेमाजी जिल्ह्यांदरम्यान ब्रह्मपुत्रेवरील 4.94 किमी लांबीचा दुमजली पूल, वर रस्ता व खाली रेल्वे — भारतातील सर्वांत लांब रेल्वे-सह-रस्ता पूल व पहिला संपूर्ण पोलादी पूल. 1997 मध्ये मंजूर व 25 डिसेंबर 2018 रोजी खुल्या झालेल्या या पुलाने धेमाजी–डिब्रुगड अंतर सुमारे 500 किमीवरून 100 किमीवर आणले."),
         "rail", "Northeast Frontier Railway", 5920, "₹5,920 crore (New India Samachar, March 2026).", "2018", "March 1997 (sanctioned)", "25 December 2018", "Completed", "new-india-samachar", BOGI),
    proj("tsat-morigaon", L("Tata semiconductor assembly and test unit, Jagiroad (Morigaon)", "टाटा सेमीकंडक्टर असेंबली और टेस्ट इकाई, जागीरोड (मोरीगाँव)", "टाटा सेमीकंडक्टर असेंब्ली व चाचणी प्रकल्प, जागीरोड (मोरीगाव)"),
         L("A ₹27,000 crore chip assembly and testing plant of Tata Semiconductor Assembly and Test Pvt Ltd, designed to handle up to 48 million chips a day. The PIB backgrounder of November 2024 projected completion by mid-2025; third-party reports in 2026 describe pilot production, but full commercial operation had not been confirmed by an official source when this card was checked.",
           "टाटा सेमीकंडक्टर असेंबली एंड टेस्ट प्रा. लि. का ₹27,000 करोड़ का चिप असेंबली और परीक्षण संयंत्र, जिसकी क्षमता प्रतिदिन 4.8 करोड़ चिप तक है। नवंबर 2024 के पीआईबी विवरण में मध्य-2025 तक पूरा होने का अनुमान था; 2026 की तीसरे पक्ष की रिपोर्टों में पायलट उत्पादन का उल्लेख है, लेकिन इस कार्ड की जाँच के समय पूर्ण व्यावसायिक संचालन की आधिकारिक पुष्टि नहीं हुई थी।",
           "टाटा सेमीकंडक्टर असेंब्ली अँड टेस्ट प्रा. लि.चा ₹27,000 कोटींचा चिप जोडणी व चाचणी प्रकल्प, ज्याची क्षमता दररोज 4.8 कोटी चिप्सपर्यंत आहे. नोव्हेंबर 2024 च्या पीआयबी माहितीपत्रात मध्य-2025 पर्यंत पूर्ण होण्याचा अंदाज होता; 2026 मधील त्रयस्थ वृत्तांत प्रायोगिक उत्पादनाचा उल्लेख आहे, पण हे कार्ड तपासले तेव्हा पूर्ण व्यावसायिक कामकाजाला अधिकृत दुजोरा मिळालेला नव्हता."),
         "industry", "Tata Semiconductor Assembly and Test Pvt Ltd (India Semiconductor Mission)", 27000, "₹27,000 crore (PIB, Nov 2024).", "2024", None, "Mid-2025 (projected in 2024)", "Under Construction", "pib", TSAT),
]

GI_NAMES = {
 "Assam (Orthodox)": ("असम (ऑर्थोडॉक्स) चाय", "आसाम (ऑर्थोडॉक्स) चहा"),
 "Assam Karbi Anglong Ginger": ("असम कार्बी आंगलोंग अदरक", "आसाम कार्बी आंगलोंग आले"),
 "Tezpur Litchi": ("तेजपुर लीची", "तेजपूर लिची"),
 "Joha Rice of Assam": ("असम का जोहा चावल", "आसामचा जोहा तांदूळ"),
 "Boka Chaul": ("बोका चाउल", "बोका चाउल"),
 "Chokuwa Rice of Assam": ("असम का चोकुवा चावल", "आसामचा चोकुवा तांदूळ"),
 "Kaji Nemu": ("काजी नेमू", "काजी नेमू"),
 "Bodo Keradapini": ("बोडो केराडापिनी", "बोडो केराडापिनी"),
 "Bodo Gongar Dunjia": ("बोडो गोंगर दुंजिया", "बोडो गोंगर दुंजिया"),
 "Bodo Khardwi": ("बोडो खारद्वि", "बोडो खारद्वी"),
 "Bodo Narzi": ("बोडो नारजी", "बोडो नारजी"),
 "Bodo Napham – Fermented Fish": ("बोडो नाफाम – ख़मीरी मछली", "बोडो नाफाम – आंबवलेला मासा"),
 "Bodo Ondla": ("बोडो ओंदला", "बोडो ओंदला"),
 "Bodo Gwkha – Gwkhwi": ("बोडो ग्वखा – ग्वख्वि", "बोडो ग्वखा – ग्वख्वी"),
 "Muga Silk of Assam": ("असम का मूगा रेशम", "आसामचे मुगा रेशीम"),
 "Muga Silk of Assam (Logo)": ("असम का मूगा रेशम (लोगो)", "आसामचे मुगा रेशीम (बोधचिन्ह)"),
 "Gamosa of Assam": ("असम का गमोसा", "आसामचा गमोसा"),
 "Majuli Mask of Assam": ("असम का माजुली मुखौटा", "आसामचा माजुली मुखवटा"),
 "Assam Majuli Manuscript Painting": ("असम माजुली पांडुलिपि चित्रकला", "आसाम माजुली हस्तलिखित चित्रकला"),
 "Bodo Aronai": ("बोडो अरोनाई", "बोडो अरोनाई"),
 "Bodo Dokhona": ("बोडो दोखोना", "बोडो दोखोना"),
 "Bodo Eri Silk": ("बोडो एरी रेशम", "बोडो एरी रेशीम"),
 "Bodo Jwmgra": ("बोडो ज्वमग्रा", "बोडो ज्वमग्रा"),
 "Bodo Gamsa": ("बोडो गामसा", "बोडो गामसा"),
 "Bodo Thorkha": ("बोडो थोरखा", "बोडो थोरखा"),
 "Bodo Kham": ("बोडो खाम (ढोल)", "बोडो खाम (ढोल)"),
 "Bodo Serja": ("बोडो सेरजा", "बोडो सेरजा"),
 "Bodo Sifung": ("बोडो सिफुंग (बाँसुरी)", "बोडो सिफुंग (बासरी)"),
 "Bodo Gongona": ("बोडो गोंगोना", "बोडो गोंगोना"),
 "Bodo Jotha": ("बोडो जोथा", "बोडो जोथा"),
 "Assam Jaapi": ("असम जापी", "आसाम जापी"),
 "Assam Asharikandi Terracotta Craft": ("असम आशारीकांदी टेराकोटा शिल्प", "आसाम आशारीकांदी टेराकोटा हस्तकला"),
 "Assam Bihu Dhol": ("असम बिहू ढोल", "आसाम बिहू ढोल"),
 "Assam Pani Meteka Craft": ("असम पानी मेटेका शिल्प", "आसाम पानी मेटेका हस्तकला"),
 "Sarthebari Metal Craft": ("सार्थेबाड़ी धातु शिल्प", "सार्थेबारी धातू हस्तकला"),
 "Axomiya Gohona (Assamese Jewellery)": ("अखोमिया गहना (असमिया आभूषण)", "अखोमिया गहना (आसामी दागिने)"),
 "Judima": ("जुडिमा", "जुडिमा"),
 "Bodo Jou Gwran": ("बोडो जौ ग्वरान", "बोडो जौ ग्वरान"),
 "Bodo Jou Gishi": ("बोडो जौ गिशी", "बोडो जौ गिशी"),
 "Bodo Maibra Jou Bidwi": ("बोडो माइब्रा जौ बिद्वि", "बोडो माइब्रा जौ बिद्वी"),
 "Arunachal Pradesh Singpho Phalap (Singpho Tea)": ("अरुणाचल प्रदेश सिंगफो फलाप (सिंगफो चाय)", "अरुणाचल प्रदेश सिंगफो फलाप (सिंगफो चहा)"),
 "Assam Mishing Handloom Products": ("असम मिसिंग हथकरघा उत्पाद", "आसाम मिसिंग हातमाग उत्पादने"),
}
TEXTILE = {"Muga Silk of Assam", "Muga Silk of Assam (Logo)", "Gamosa of Assam", "Bodo Aronai", "Bodo Dokhona", "Bodo Eri Silk",
           "Bodo Jwmgra", "Bodo Gamsa", "Assam Mishing Handloom Products"}
SHARED = {"AR,AS": ["Arunachal Pradesh"], "AS,AR": ["Arunachal Pradesh"]}
r["giProducts"] = gi_list("gi_as.tsv", GI_NAMES, SHARED, TEXTILE)
for g in r["giProducts"]:
    if "&" in g["applicationNo"]:
        g["note"] += " The registry lists two application numbers (filed 19 and 22 Nov 2007); the date shown is the earlier filing."
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-AS.json", r)
print("as core ok", len(r["giProducts"]), "GIs")
