"""Uttarakhand — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-24."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.deccanchronicle.com/nation/bisen-takes-oath-as-uttarakhand-governor-1997286"
CM = "https://www.tribuneindia.com/news/nation/pushkar-dhami-takes-oath-as-uttarakhand-cm-8-ministers-also-sworn-in-380048"
SPK = "https://drishtiias.com/state-pcs-current-affairs/ritu-khanduri-speaker-of-uttarakhand-legislative-assembly"
ROPE = "https://www.newsonair.gov.in/cabinet-approves-%f0%9d%90%ab%f0%9d%90%a8%f0%9d%90%a9%f0%9d%90%9e%f0%9d%90%b0%f0%9d%90%9a%f0%9d%90%b2-%f0%9d%90%a9%f0%9d%90%ab%f0%9d%90%a8%f0%9d%90%a3%f0%9d%90%9e%f0%9d%90%9c%f0%9d%90%ads-revision-of"
RKRL = "https://www.etvbharat.com/en/!bharat/no-timeline-set-for-completion-of-rishikesh-karnaprayag-rail-line-vaishnaw-enn25080703839"

mo = research("mospi_uk.json")
C = research("census_b5plus.json")
r = read("regions/IN-UK.json")
m = r["metrics"]
m["population2011"] = dp(10086292, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 51,37,773; females 49,48,519.")
m["area"] = dp(53483, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(189, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 1,00,86,292 ÷ area 53,483 km² = 188.6.")
m["sexRatio2011"] = dp(963, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (962 in 2001).")
m["childSexRatio2011"] = dp(890, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 908 in 2001.")
m["literacyRate2011"] = dp(78.8, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2025-26 is the latest year published for Uttarakhand. FY2024-25: ₹{inr(mo['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(mo['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(45.44, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 24,303.83 km² ÷ geographical area 53,483 km².")

r["officialPortal"] = "https://uk.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Alpine musk deer", "कस्तूरी मृग", "कस्तुरी मृग", "Moschus chrysogaster"),
    "bird": sym("Himalayan monal", "मोनाल", "मोनाल", "Lophophorus impejanus"),
    "tree": sym("Burans (tree rhododendron)", "बुरांस", "बुरांस (र्‍होडोडेंड्रॉन वृक्ष)", "Rhododendron arboreum"),
    "flower": sym("Brahma kamal", "ब्रह्म कमल", "ब्रह्मकमळ", "Saussurea obvallata"),
}

r["government"] = {
    "headOfState": office('governor', L('Dhal Singh Bisen', 'ढाल सिंह बिसेन', 'ढालसिंह बिसेन'), None, '2026-10-19', 'president-of-india', 'https://presidentofindia.nic.in/press_releases/press-communique-38', 'https://governoruk.gov.in', note='Official confirmation: Rashtrapati Bhavan communique 12 Oct 2026: Dr Dhal Singh Bisen appointed Governor of Uttarakhand. Sworn in as the ninth Governor of Uttarakhand at Lok Bhavan, Dehradun, on 19 October 2026 by Justice Manoj Kumar Tiwari (Deccan Chronicle). A former Madhya Pradesh minister and Lok Sabha member. Appointed in the Rashtrapati Bhavan communiqué of 12 October 2026.', as_of='2026-10-27'),
    "headOfGovernment": office('chief-minister', L('Pushkar Singh Dhami', 'पुष्कर सिंह धामी', 'पुष्करसिंह धामी'), 'BJP', '2022-03-23', 'uk-lokbhavan', 'https://governoruk.gov.in/01-02-2026-the-honble-chief-minister-of-uttarakhand-shri-pushkar-singh-dhami-paid-a-courtesy-call-on-the-honble-governor-at-lok-bhavan/', 'https://uk.gov.in', note='Official confirmation: Lok Bhavan Dehradun press note 1 Feb 2026: Chief Minister of Uttarakhand Shri Pushkar Singh Dhami paid a courtesy call on the Governor. Sworn in for a second consecutive term on 23 March 2022 at Parade Ground, Dehradun, by Governor Lt Gen Gurmit Singh (retd), with eight ministers (The Tribune). He first became Chief Minister in July 2021.', as_of='2026-10-27'),
    "others": [
        office('speaker', L('Ritu Khanduri Bhushan', 'ऋतु खंडूड़ी भूषण', 'ऋतू खंडुरी भूषण'), 'BJP', '2022-03-26', 'uk-lokbhavan', 'https://governoruk.gov.in/18-03-2026-the-speaker-of-the-legislative-assembly-smt-ritu-khanduri-bhushan-called-on-the-governor-lieutenant-general-gurmit-singh-retd-at-lok-bhavan-on-wednesday/', 'https://ukvidhansabha.uk.gov.in', note='Official confirmation: Lok Bhavan Dehradun press note 18 Mar 2026: Speaker of the Legislative Assembly Smt Ritu Khanduri Bhushan called on the Governor. Elected unopposed on 26 March 2022 as Speaker of the fifth Uttarakhand Assembly — the first woman in the post; MLA from Kotdwar (Drishti IAS summary; replace with the Vidhan Sabha notice).', as_of='2026-10-27'),
    ],
}

r["projects"] = [
    proj("rishikesh-karnaprayag", L("Rishikesh–Karnaprayag new rail line", "ऋषिकेश–कर्णप्रयाग नई रेल लाइन", "ऋषिकेश–कर्णप्रयाग नवीन रेल्वे मार्गिका"),
         L("A 125-km broad-gauge railway from Rishikesh into the Garhwal hills to Karnaprayag, most of it in tunnels. In a written reply to the Lok Sabha reported in August 2025, the Railway Minister said 199 km of the 213 km of tunnelling was complete — 13 of 16 main-line tunnels and 9 of 12 escape tunnels — and that an exact completion date could not yet be fixed.",
           "ऋषिकेश से गढ़वाल की पहाड़ियों में कर्णप्रयाग तक 125 किमी लंबी ब्रॉड गेज रेलवे, जिसका अधिकांश भाग सुरंगों में है। अगस्त 2025 में प्रकाशित लोकसभा में लिखित उत्तर में रेल मंत्री ने बताया कि 213 किमी सुरंग कार्य में से 199 किमी पूरा हो चुका है — 16 में से 13 मुख्य सुरंगें और 12 में से 9 निकास सुरंगें — और पूरा होने की सटीक तिथि अभी तय नहीं की जा सकती।",
           "ऋषिकेशहून गढवालच्या डोंगरांत कर्णप्रयागपर्यंतची 125 किमी लांबीची ब्रॉड गेज रेल्वे, जिचा बहुतांश भाग बोगद्यांत आहे. ऑगस्ट 2025 मध्ये प्रसिद्ध झालेल्या लोकसभेतील लेखी उत्तरात रेल्वेमंत्र्यांनी सांगितले की 213 किमी बोगदा कामापैकी 199 किमी पूर्ण झाले आहे — 16 पैकी 13 मुख्य बोगदे व 12 पैकी 9 सुटका बोगदे — आणि पूर्ण होण्याची नेमकी तारीख अजून ठरवता येत नाही."),
         "rail", "Rail Vikas Nigam Ltd (Ministry of Railways)", None, None, None, None, None, "Under Construction", "etv-bharat", RKRL, conf="Third-party verified"),
    proj("kedarnath-ropeway", L("Sonprayag–Kedarnath and Govindghat–Hemkund Sahib ropeways", "सोनप्रयाग–केदारनाथ और गोविंदघाट–हेमकुंड साहिब रोपवे", "सोनप्रयाग–केदारनाथ व गोविंदघाट–हेमकुंड साहिब रोपवे"),
         L("Two ropeways approved by the Union Cabinet on 5 March 2025: a 12.9-km line from Sonprayag to Kedarnath costing over ₹4,000 crore, which would cut the climb of 8–9 hours to about 36 minutes, and a 12.4-km line from Govindghat to Hemkund Sahib costing ₹2,730 crore.",
           "5 मार्च 2025 को केंद्रीय मंत्रिमंडल द्वारा स्वीकृत दो रोपवे: सोनप्रयाग से केदारनाथ तक 12.9 किमी लंबी लाइन, जिसकी लागत ₹4,000 करोड़ से अधिक है और जो 8–9 घंटे की चढ़ाई को लगभग 36 मिनट कर देगी, और गोविंदघाट से हेमकुंड साहिब तक ₹2,730 करोड़ की 12.4 किमी लंबी लाइन।",
           "5 मार्च 2025 रोजी केंद्रीय मंत्रिमंडळाने मंजूर केलेले दोन रोपवे: सोनप्रयागहून केदारनाथपर्यंतची 12.9 किमी लांबीची मार्गिका, जिचा खर्च ₹4,000 कोटींहून अधिक असून ती 8–9 तासांची चढण सुमारे 36 मिनिटांवर आणेल, आणि गोविंदघाटहून हेमकुंड साहिबपर्यंतची ₹2,730 कोटींची 12.4 किमी मार्गिका."),
         "transport", "Ministry of Road Transport and Highways", None, None, None, "Approved 5 March 2025", None, "Announced", "newsonair", ROPE),
]

GI_NAMES = {
 "Uttarakhand Tejpat": ("उत्तराखंड तेजपात", "उत्तराखंड तमालपत्र"),
 "Kumaon Chyura Oil": ("कुमाऊँ च्यूरा तेल", "कुमाऊँ च्यूरा तेल"),
 "Munsyari Rajma": ("मुनस्यारी राजमा", "मुनस्यारी राजमा"),
 "Uttarakhand Berinag Tea": ("उत्तराखंड बेरीनाग चाय", "उत्तराखंड बेरीनाग चहा"),
 "Uttarakhand Mandua": ("उत्तराखंड मंडुआ", "उत्तराखंड मंडुआ (नाचणी)"),
 "Uttarakhand Jhangora": ("उत्तराखंड झंगोरा", "उत्तराखंड झंगोरा"),
 "Uttarakhand Gahat": ("उत्तराखंड गहत", "उत्तराखंड गहत (कुळीथ)"),
 "Uttarakhand Lal Chawal (Red Rice)": ("उत्तराखंड लाल चावल", "उत्तराखंड लाल तांदूळ"),
 "Uttarakhand Kala Bhat": ("उत्तराखंड काला भट", "उत्तराखंड काळा भट"),
 "Uttarakhand Malta Fruit": ("उत्तराखंड माल्टा फल", "उत्तराखंड माल्टा फळ"),
 "Uttarakhand Chaulai (Ramdana)": ("उत्तराखंड चौलाई (रामदाना)", "उत्तराखंड राजगिरा (रामदाणा)"),
 "Almora Lakhori Mirchi": ("अल्मोड़ा लखोरी मिर्च", "अल्मोडा लखोरी मिरची"),
 "Uttarakhand Pahari Toor Dal": ("उत्तराखंड पहाड़ी तूर दाल", "उत्तराखंड पहाडी तूरडाळ"),
 "Ramnagar Nainital Litchi": ("रामनगर नैनीताल लीची", "रामनगर नैनीताल लिची"),
 "Ramgarh Nainital Aadu (Peach)": ("रामगढ़ नैनीताल आड़ू", "रामगड नैनीताल पीच (आडू)"),
 "Uttarakhand Bedu (Fruit)": ("उत्तराखंड बेड़ू (फल)", "उत्तराखंड बेडू (फळ)"),
 "Uttarakhand Buransh": ("उत्तराखंड बुरांस", "उत्तराखंड बुरांस"),
 "Uttarakhand Badri Cow Ghee": ("उत्तराखंड बद्री गाय घी", "उत्तराखंड बद्री गाय तूप"),
 "Bhotia Dann of Uttarakhand": ("उत्तराखंड का भोटिया दन", "उत्तराखंडचा भोटिया दन"),
 "Uttarakhand Aipan": ("उत्तराखंड ऐपण", "उत्तराखंड ऐपण"),
 "Uttarakhand Ringal Craft": ("उत्तराखंड रिंगाल शिल्प", "उत्तराखंड रिंगाल हस्तकला"),
 "Uttarakhand Tamta Product": ("उत्तराखंड ताम्र उत्पाद", "उत्तराखंड तांब्याच्या वस्तू"),
 "Uttarakhand Thulma": ("उत्तराखंड थुलमा", "उत्तराखंड थुलमा"),
 "Uttarakhand Bichhu Buti (Nettle) Fabrics": ("उत्तराखंड बिच्छू बूटी वस्त्र", "उत्तराखंड बिच्छू बुटी (खाजकुइली) वस्त्र"),
 "Rangwali Pichhoda of Kumaon": ("कुमाऊँ का रंगवाली पिछौड़ा", "कुमाऊँचा रंगवाली पिछौडा"),
 "Chamoli Wooden Ramman Mask": ("चमोली लकड़ी का रम्माण मुखौटा", "चमोली लाकडी रम्माण मुखवटा"),
 "Uttarakhand Likhai (Wood Carving)": ("उत्तराखंड लिखाई (काष्ठ नक़्क़ाशी)", "उत्तराखंड लिखाई (काष्ठकोरीव काम)"),
 "Nainital Mombatti (Candle)": ("नैनीताल मोमबत्ती", "नैनीताल मेणबत्ती"),
 "Basmati": ("बासमती", "बासमती"),
}
SHARED = {"PB,HR,HP,DL,UK,UP,JK": ["Punjab", "Haryana", "Himachal Pradesh", "Delhi", "Uttar Pradesh", "Jammu & Kashmir"]}
r["giProducts"] = gi_list("gi_uk.tsv", GI_NAMES, SHARED, {"Bhotia Dann of Uttarakhand", "Uttarakhand Thulma", "Uttarakhand Bichhu Buti (Nettle) Fabrics", "Rangwali Pichhoda of Kumaon"})
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-UK.json", r)
print("uk core ok", len(r["giProducts"]), "GIs")
