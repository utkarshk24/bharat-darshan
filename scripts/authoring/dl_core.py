import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

ESD = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/chapter_19_0.pdf"
mo = research("mospi_dl.json")

r = read("regions/IN-DL.json")
r["officialPortal"] = "https://delhi.gov.in"
m = r["metrics"]
m["population2011"] = dp(16787941, "persons", "2011", "census", "census", ESD,
    note="Census 2011 total as published in the Economic Survey of Delhi 2023-24, Chapter 19 (Demographic Profile).")
m["area"] = dp(1483, "km²", "2011", "census", "census", ESD,
    note="369.35 km² rural and 1,113.65 km² urban (Economic Survey of Delhi 2023-24). ISFR 2023 uses the same 1,483 km².")
m["density2011"] = dp(11320, "persons per km²", "2011", "census", "census", ESD, note="Highest of any State or UT at the 2011 Census; India 382.")
m["sexRatio2011"] = dp(868, "females per 1000 males", "2011", "census", "census", ESD, note="Up from 821 in 2001.")
m["childSexRatio2011"] = dp(871, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR,
    note="PIB release of 11 Feb 2014 (RGI data). Was 868 in 2001.")
m["literacyRate2011"] = dp(86.2, "%", "2011", "census", "census", ESD, note="Population aged 7+. Male 90.9%, female 80.8%.")
m["urbanisation2011"] = dp(97.5, "%", "2011", "census", "census", ESD, note="Economic Survey of Delhi gives 97.50%.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2025-26 not yet published for Delhi. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note="MoSPI, base 2011-12.")
m["forestCoverPct"] = dp(13.17, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 195.28 km² ÷ geographical area 1,483 km².")
r["symbols"] = {}

LG = "https://lg.delhi.gov.in/node/11076"
CM = "https://www.newsonair.gov.in/rekha-gupta-takes-charge-as-delhi-cm-becomes-bjps-2nd-woman-leader-to-hold-office/"
SPK = "https://www.newsonair.gov.in/winter-session-of-delhi-assembly-to-begin-tomorrow"
LOP = "https://dailypioneer.com/news/assembly-monsoon-session-ends-4-bills-passed-2-cag-reports-tabled"
r["government"] = {
    "headOfState": office("lieutenant-governor", L("Taranjit Singh Sandhu", "तरनजीत सिंह संधू", "तरनजीत सिंग संधू"), None, "2026-03-11",
                          "dl-lg", LG, "https://lg.delhi.gov.in",
                          note="Took over as the 23rd Lieutenant Governor of Delhi at Lok Niwas on 11 March 2026 (Lok Niwas). Former Ambassador of India to the United States."),
    "headOfGovernment": office("chief-minister", L("Rekha Gupta", "रेखा गुप्ता", "रेखा गुप्ता"), "BJP", "2025-02-20",
                               "newsonair", CM, "https://delhi.gov.in",
                               note="Sworn in on 20 February 2025 at Ramlila Maidan (News On AIR)."),
    "others": [
        office("speaker", L("Vijender Gupta", "विजेंद्र गुप्ता", "विजेंद्र गुप्ता"), "BJP", None, "newsonair", SPK, "https://delhiassembly.delhi.gov.in",
               note="Named as Speaker in News On AIR (4 January 2026) and in reports of the August 2026 monsoon session."),
        office("leader-of-opposition", L("Atishi", "आतिशी", "आतिशी"), "AAP", None, "pioneer", LOP, "https://delhiassembly.delhi.gov.in",
               conf="Third-party verified",
               note="Referred to as Leader of Opposition in reports of March 2025 (The Tribune) and August 2026 (The Pioneer). Former Chief Minister (2024–25)."),
    ],
}

NOA_RRTS = "https://www.newsonair.gov.in/pm-modi-flags-off-meerut-metro-namo-bharat-train-in-uttar-pradesh"
PMI_RRTS = "https://www.pmindia.gov.in/en/news_updates/pm-to-visit-meerut-on-22-february"
PMI_METRO = "https://www.pmindia.gov.in/en/news_updates/cabinet-approves-two-corridors-of-delhi-metro-phase-iv-projects-namely-i-lajpat-nagar-to-saket-g-block-and-ii-inderlok-to-indraprastha/"
r["projects"] = [
    proj("namo-bharat", L("Delhi–Ghaziabad–Meerut Namo Bharat (RRTS) corridor", "दिल्ली–ग़ाज़ियाबाद–मेरठ नमो भारत (आरआरटीएस) कॉरिडोर", "दिल्ली–गाझियाबाद–मेरठ नमो भारत (आरआरटीएस) मार्गिका"),
         L("India's first regional rapid transit line, 82 km from Sarai Kale Khan in Delhi to Modipuram in Meerut. The whole corridor was dedicated to the nation on 22 February 2026, when the last sections — including 5 km in Delhi from Sarai Kale Khan to New Ashok Nagar — opened.",
           "भारत की पहली क्षेत्रीय रैपिड ट्रांज़िट लाइन, दिल्ली के सराय काले ख़ाँ से मेरठ के मोदीपुरम तक 82 किमी। पूरा कॉरिडोर 22 फ़रवरी 2026 को राष्ट्र को समर्पित हुआ, जब अंतिम खंड — दिल्ली में सराय काले ख़ाँ से न्यू अशोक नगर तक 5 किमी सहित — खुले।",
           "भारतातील पहिली प्रादेशिक जलद परिवहन मार्गिका, दिल्लीतील सराय काले खाँ ते मेरठमधील मोदीपुरम अशी 82 किमी. 22 फेब्रुवारी 2026 रोजी शेवटचे टप्पे — दिल्लीतील सराय काले खाँ ते न्यू अशोक नगर हा 5 किमीचा भाग धरून — खुले झाले आणि संपूर्ण मार्गिका राष्ट्राला समर्पित झाली."),
         "transport", "NCRTC", None, None, None, None, "February 2026", "Completed", "newsonair", NOA_RRTS),
    proj("metro-p4", L("Delhi Metro Phase IV", "दिल्ली मेट्रो चरण IV", "दिल्ली मेट्रो टप्पा IV"),
         L("The fourth phase of Delhi Metro expansion. In March 2024, when DMRC was already building about 65 km of Phase IV, the Union Cabinet approved two more corridors — Lajpat Nagar–Saket G Block and Inderlok–Indraprastha (20.762 km together) — expected to be completed in stages.",
           "दिल्ली मेट्रो विस्तार का चौथा चरण। मार्च 2024 में, जब डीएमआरसी पहले से चरण IV के लगभग 65 किमी का निर्माण कर रहा था, केंद्रीय मंत्रिमंडल ने दो और कॉरिडोर — लाजपत नगर–साकेत जी ब्लॉक और इंद्रलोक–इंद्रप्रस्थ (कुल 20.762 किमी) — मंज़ूर किए, जिन्हें चरणों में पूरा किया जाना है।",
           "दिल्ली मेट्रो विस्ताराचा चौथा टप्पा. मार्च 2024 मध्ये, डीएमआरसी टप्पा IV चे सुमारे 65 किमी काम आधीच करत असताना, केंद्रीय मंत्रिमंडळाने आणखी दोन मार्गिका — लाजपत नगर–साकेत जी ब्लॉक आणि इंद्रलोक–इंद्रप्रस्थ (एकूण 20.762 किमी) — मंजूर केल्या; त्या टप्प्याटप्प्याने पूर्ण होणार आहेत."),
         "transport", "DMRC", 8399, "₹8,399 crore for the two corridors approved in March 2024 (not the whole phase)", "2024", None, "In stages", "Under Construction",
         "pmindia", PMI_METRO,
         challenges=L("The Cabinet release targeted completion of the two new corridors by March 2026 in stages; current progress needs an official update.",
                      "मंत्रिमंडल की विज्ञप्ति में दो नए कॉरिडोर मार्च 2026 तक चरणों में पूरे करने का लक्ष्य था; वर्तमान प्रगति के लिए आधिकारिक अद्यतन चाहिए।",
                      "मंत्रिमंडळाच्या निवेदनात दोन नव्या मार्गिका मार्च 2026 पर्यंत टप्प्याटप्प्याने पूर्ण करण्याचे उद्दिष्ट होते; सद्यस्थितीसाठी अधिकृत अद्ययावत माहिती हवी.")),
]

GI_NAMES = {"Basmati": ("बासमती", "बासमती")}
SHARED = {"PB,HR,HP,DL,UK,UP,JK": ["Punjab", "Haryana", "Himachal Pradesh", "Uttarakhand", "Uttar Pradesh", "Jammu & Kashmir"]}
r["giProducts"] = gi_list("gi_dl.tsv", GI_NAMES, SHARED)
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-DL.json", r)
print("dl core ok")
