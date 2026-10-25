"""Arunachal Pradesh — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://arunachalgovernor.gov.in/pr/2023/230216_Swearing in.pdf"
GOV_NOW = "https://arunachalgovernor.gov.in/pr/2026/260815_Governor inaugurates Chief Ministers office.pdf"
CM = "https://www.etvbharat.com/amp/en/!state/pema-khandu-sworn-in-as-arunachal-pradesh-cm-enn24061302061"
SPK = "https://newsonair.gov.in/tesam-pongte-elected-as-new-speaker-of-arunachal-pradesh"
SELA = "https://morungexpress.com/pm-inaugurates-strategically-vital-worlds-longest-bi-lane-sela-tunnel-at-13000-feet-in-arunachal-pradesh"
DONYI = "https://newindiasamachar.pib.gov.in/WriteReadData/flipbook/2022/Dec/2nd/English/files/basic-html/page45.html"

mo = research("mospi_ar.json")
C = research("census_b5plus.json")
r = read("regions/IN-AR.json")
m = r["metrics"]
p = C["pop"]["AR"]
m["population2011"] = dp(p[0], "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 7,13,912; females 6,69,815.")
m["area"] = dp(83743, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(17, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 13,83,727 ÷ area 83,743 km² = 16.5.")
m["sexRatio2011"] = dp(938, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (893 in 2001).")
m["childSexRatio2011"] = dp(972, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 964 in 2001.")
m["literacyRate2011"] = dp(65.4, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2025-26 is the latest year published for Arunachal Pradesh. FY2024-25: ₹{inr(mo['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(mo['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(78.67, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 65,881.57 km² ÷ geographical area 83,743 km².")

r["officialPortal"] = "https://arunachalpradesh.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Mithun (gayal)", "मिथुन (गयाल)", "मिथुन (गयाल)", "Bos frontalis"),
    "bird": sym("Great hornbill", "बड़ा धनेश", "महाधनेश", "Buceros bicornis"),
    "flower": sym("Foxtail orchid", "फ़ॉक्सटेल ऑर्किड", "फॉक्सटेल ऑर्किड", "Rhynchostylis retusa"),
}

r["government"] = {
    "headOfState": office("governor", L("Lt Gen Kaiwalya Trivikram Parnaik (Retd)", "लेफ़्टिनेंट जनरल कैवल्य त्रिविक्रम परनाइक (सेवानिवृत्त)", "लेफ्टनंट जनरल कैवल्य त्रिविक्रम परनाईक (निवृत्त)"), None, "2023-02-16",
                          "ar-governor", GOV, "https://arunachalgovernor.gov.in", conf="Official",
                          note="Sworn in at Raj Bhavan, Itanagar, on 16 February 2023; Justice Nani Tagia of the Gauhati High Court administered the oath (Lok Bhavan press release). Still in office per the Lok Bhavan release of 15 August 2026."),
    "headOfGovernment": office("chief-minister", L("Pema Khandu", "पेमा खांडू", "पेमा खांडू"), "BJP", "2024-06-13",
                               "etv-bharat", CM, "https://arunachalpradesh.gov.in", conf="Third-party verified",
                               note="Sworn in for a third consecutive term on 13 June 2024 by Governor K. T. Parnaik; Chowna Mein was sworn in as Deputy Chief Minister (ETV Bharat). Named as Chief Minister in the Lok Bhavan release of 15 August 2026."),
    "others": [
        office("speaker", L("Tesam Pongte", "तेसाम पोंग्ते", "तेसाम पोंग्ते"), "BJP", "2024-06-15", "newsonair", SPK, "https://arunachalpradesh.gov.in", conf="Official",
               note="Elected unanimously as Speaker of the 8th Arunachal Pradesh Legislative Assembly (News On AIR, 15 June 2024); MLA from Changlang North."),
    ],
}

r["projects"] = [
    proj("sela-tunnel", L("Sela Tunnel", "सेला सुरंग", "सेला बोगदा"),
         L("Two road tunnels of 1,003 m and 1,595 m, with 8.6 km of approach and link roads, under the Sela Pass at about 13,000 ft on the Balipara–Charduar–Tawang road. Built by the Border Roads Organisation at about ₹825 crore, they give Tawang all-weather road access; the Prime Minister dedicated them to the nation on 9 March 2024.",
           "बालीपारा–चारद्वार–तवांग सड़क पर लगभग 13,000 फ़ुट पर सेला दर्रे के नीचे 1,003 मीटर और 1,595 मीटर की दो सड़क सुरंगें, 8.6 किमी की पहुँच और संपर्क सड़कों के साथ। सीमा सड़क संगठन ने इन्हें लगभग ₹825 करोड़ में बनाया, और ये तवांग को हर मौसम में सड़क संपर्क देती हैं; प्रधानमंत्री ने 9 मार्च 2024 को इन्हें राष्ट्र को समर्पित किया।",
           "बालिपारा–चारद्वार–तवांग रस्त्यावर सुमारे 13,000 फूट उंचीवर सेला खिंडीखाली 1,003 मीटर व 1,595 मीटरचे दोन रस्ते बोगदे, 8.6 किमी जोडरस्त्यांसह. सीमा रस्ते संघटनेने ते सुमारे ₹825 कोटी खर्चून बांधले, आणि ते तवांगला सर्व ऋतूंत रस्ते संपर्क देतात; पंतप्रधानांनी 9 मार्च 2024 रोजी ते राष्ट्राला समर्पित केले."),
         "transport", "Border Roads Organisation", 825, "IANS report via The Morung Express.", "2024", None, "9 March 2024", "Completed", "morung-express", SELA, conf="Third-party verified"),
    proj("donyi-polo-airport", L("Donyi Polo Airport, Itanagar", "दोन्यी पोलो हवाई अड्डा, ईटानगर", "दोन्यी पोलो विमानतळ, इटानगर"),
         L("A greenfield airport at Hollongi, about 25 km from Itanagar, built at a cost of ₹645 crore and dedicated to the nation by the Prime Minister on 19 November 2022, together with the Kameng hydro power station. It gave the State capital its own airport.",
           "ईटानगर से लगभग 25 किमी दूर होल्लोंगी में ₹645 करोड़ की लागत से बना नया हवाई अड्डा, जिसे प्रधानमंत्री ने 19 नवंबर 2022 को कामेंग जलविद्युत केंद्र के साथ राष्ट्र को समर्पित किया। इससे राज्य की राजधानी को अपना हवाई अड्डा मिला।",
           "इटानगरपासून सुमारे 25 किमीवरील होल्लोंगी येथे ₹645 कोटी खर्चून बांधलेला नवा विमानतळ, जो पंतप्रधानांनी 19 नोव्हेंबर 2022 रोजी कामेंग जलविद्युत केंद्रासह राष्ट्राला समर्पित केला. यामुळे राज्याच्या राजधानीला स्वतःचा विमानतळ मिळाला."),
         "aviation", "Airports Authority of India", 645, "New India Samachar (PIB), 16–31 December 2022.", "2022", None, "19 November 2022", "Completed", "new-india-samachar", DONYI),
]

GI_NAMES = {
 "Arunachal Orange": ("अरुणाचल संतरा", "अरुणाचल संत्रे"),
 "Arunachal Pradesh Khaw Tai (Khamti Rice)": ("अरुणाचल प्रदेश खाव ताई (खामती चावल)", "अरुणाचल प्रदेश खाव ताई (खामती तांदूळ)"),
 "Arunachal Pradesh Adi Kekir (Ginger)": ("अरुणाचल प्रदेश आदी केकिर (अदरक)", "अरुणाचल प्रदेश आदी केकिर (आले)"),
 "Arunachal Pradesh Angnyat Millet": ("अरुणाचल प्रदेश अंग्न्यात बाजरा", "अरुणाचल प्रदेश अंग्न्यात भरडधान्य"),
 "Arunachal Pradesh Yak Churpi": ("अरुणाचल प्रदेश याक छुरपी", "अरुणाचल प्रदेश याक छुरपी"),
 "Idu Mishmi Textiles": ("इदु मिश्मी वस्त्र", "इदु मिश्मी वस्त्रे"),
 "Arunachal Pradesh Tangsa Textile Product": ("अरुणाचल प्रदेश तांगसा वस्त्र उत्पाद", "अरुणाचल प्रदेश तांगसा वस्त्र उत्पादने"),
 "Arunachal Pradesh Handmade Carpet": ("अरुणाचल प्रदेश हस्तनिर्मित क़ालीन", "अरुणाचल प्रदेश हाताने बनवलेले गालिचे"),
 "Arunachal Pradesh Wancho Wooden Craft": ("अरुणाचल प्रदेश वांचो काष्ठ शिल्प", "अरुणाचल प्रदेश वांचो काष्ठकला"),
 "Arunachal Pradesh Apatani Textile": ("अरुणाचल प्रदेश अपातानी वस्त्र", "अरुणाचल प्रदेश आपातानी वस्त्रे"),
 "Arunachal Pradesh Monpa Textile": ("अरुणाचल प्रदेश मोनपा वस्त्र", "अरुणाचल प्रदेश मोनपा वस्त्रे"),
 "Arunachal Pradesh Nyishi Textile": ("अरुणाचल प्रदेश न्यिशी वस्त्र", "अरुणाचल प्रदेश न्यिशी वस्त्रे"),
 "Arunachal Pradesh Monpa Handmade Paper": ("अरुणाचल प्रदेश मोनपा हस्तनिर्मित काग़ज़", "अरुणाचल प्रदेश मोनपा हातकागद"),
 "Arunachal Pradesh Adi Textile": ("अरुणाचल प्रदेश आदी वस्त्र", "अरुणाचल प्रदेश आदी वस्त्रे"),
 "Arunachal Pradesh Galo Textile": ("अरुणाचल प्रदेश गालो वस्त्र", "अरुणाचल प्रदेश गालो वस्त्रे"),
 "Arunachal Pradesh Tai Khamti Textile": ("अरुणाचल प्रदेश ताई खामती वस्त्र", "अरुणाचल प्रदेश ताई खामती वस्त्रे"),
 "Arunachal Pradesh Adi Apong": ("अरुणाचल प्रदेश आदी आपोंग", "अरुणाचल प्रदेश आदी आपोंग"),
 "Arunachal Pradesh Dao (Sword)": ("अरुणाचल प्रदेश दाओ (तलवार)", "अरुणाचल प्रदेश दाओ (तलवार)"),
 "Arunachal Pradesh Marua Apo (Marua Millet Beverage)": ("अरुणाचल प्रदेश मरुआ आपो (मड़ुआ पेय)", "अरुणाचल प्रदेश मरुआ आपो (नाचणी पेय)"),
 "Arunachal Pradesh Singpho Phalap (Singpho Tea)": ("अरुणाचल प्रदेश सिंगफ़ो फलाप (सिंगफ़ो चाय)", "अरुणाचल प्रदेश सिंगफो फलाप (सिंगफो चहा)"),
 "Assam Mishing Handloom Products": ("असम मिसिंग हथकरघा उत्पाद", "आसाम मिसिंग हातमाग उत्पादने"),
}
TEXTILE = {"Idu Mishmi Textiles", "Arunachal Pradesh Tangsa Textile Product", "Arunachal Pradesh Apatani Textile", "Arunachal Pradesh Monpa Textile",
           "Arunachal Pradesh Nyishi Textile", "Arunachal Pradesh Adi Textile", "Arunachal Pradesh Galo Textile", "Arunachal Pradesh Tai Khamti Textile",
           "Assam Mishing Handloom Products"}
r["giProducts"] = gi_list("gi_ar.tsv", GI_NAMES, {"AR,AS": ["Assam"], "AS,AR": ["Assam"]}, TEXTILE)
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-AR.json", r)
print("ar core ok", len(r["giProducts"]), "GIs")
