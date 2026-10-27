"""Telangana — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-16.

Census 2011 figures are for the present State (10 districts of 2011), as recast in the MSME-DI Hyderabad
State Profile. Tables that show undivided Andhra Pradesh are not used for State-level figures."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

MSME = "https://dcmsme.gov.in/old/dips/state_wise_dips/TS-Profile.pdf"
GOV = "https://ianslive.in/shiv-pratap-shukla-sworn-in-as-new-governor-of-telangana--20260311113839"
CM = "https://www.tribuneindia.com/news/india/reddy-takes-oath-as-telangana-cm-vikramarka-his-deputy-569773"
SPK = "https://thesouthfirst.com/telangana/telangana-gets-its-first-dalit-speaker-as-gaddam-prasad-kumar-is-elected-unopposed/"
PMO = "https://www.pmindia.gov.in/?p=16839420"

tg = research("mospi_tg.json")
r = read("regions/IN-TG.json")
m = r["metrics"]
RNOTE = "Census 2011 recast for the present State of Telangana, from the MSME-DI Hyderabad 'State Profile of Telangana 2015-16'."
m["population2011"] = dp(35003674, "persons", "2011", "census", "msme-di", MSME, note=RNOTE + " Males 1,76,11,633; females 1,73,92,041.")
m["area"] = dp(112077, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(312, "persons per km²", "2011", "census", "msme-di", MSME,
    note="Calculated: Census 2011 population 3,50,03,674 ÷ area 1,12,077 km² = 312.3; the State Profile also gives 312.")
m["sexRatio2011"] = dp(988, "females per 1000 males", "2011", "census", "msme-di", MSME, note=RNOTE)
m["childSexRatio2011"] = dp(932, "girls per 1000 boys (0–6 yrs)", "2011", "census", "msme-di", MSME, note=RNOTE)
m["literacyRate2011"] = dp(66.54, "%", "2011", "census", "msme-di", MSME, note=RNOTE + " Males 75.04%, females 57.99%.")
m["urbanisation2011"] = dp(38.88, "%", "2011", "census", "msme-di", MSME, note=RNOTE + " Urban population 1,36,08,665.")
m["gsdpCurrent"] = dp(tg["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25: ₹{inr(tg['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(tg["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(tg['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(18.90, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 21,179.04 km² ÷ geographical area 1,12,077 km².")

r["officialPortal"] = "https://www.telangana.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Spotted deer (chital)", "चीतल", "चितळ", "Axis axis"),
    "bird": sym("Indian roller (palapitta)", "नीलकंठ (पालपिट्टा)", "नीलकंठ (पालपिट्टा)", "Coracias benghalensis"),
    "flower": sym("Tangedu", "तंगेडु (अवारम)", "तरवड (तंगेडू)", "Senna auriculata"),
    "tree": sym("Jammi", "शमी (जम्मी)", "शमी (जम्मी)", "Prosopis cineraria"),
}

r["government"] = {
    "headOfState": office('governor', L('Shiv Pratap Shukla', 'शिव प्रताप शुक्ल', 'शिव प्रताप शुक्ला'), None, '2026-03-11', 'president-of-india', 'https://presidentofindia.nic.in/press_releases/press-communique-32', 'https://igod.gov.in', note="Official confirmation: Rashtrapati Bhavan communique 5 Mar 2026: Shiv Pratap Shukla appointed Governor of Telangana. Moved from Himachal Pradesh (President's communiqué of 5 March 2026). Sworn in as the fourth Governor of Telangana on 11 March 2026 by Chief Justice Aparesh Kumar, succeeding Jishnu Dev Varma (IANS). Confirm on the Lok Bhavan, Telangana website.", as_of='2026-10-27'),
    "headOfGovernment": office('chief-minister', L('A. Revanth Reddy', 'ए. रेवंत रेड्डी', 'ए. रेवंत रेड्डी'), 'INC', '2023-12-07', 'tg-gov', 'https://www.telangana.gov.in', 'https://www.telangana.gov.in', note="Official confirmation: Telangana State Portal (current; lists Governor Shiv Pratap Shukla): Chief Minister Sri Anumula Revanth Reddy. Sworn in on 7 December 2023 (The Tribune). Attended the Governor's swearing-in as Chief Minister on 11 March 2026 (IANS).", as_of='2026-10-27'),
    "others": [
        office('deputy-chief-minister', L('Mallu Bhatti Vikramarka', 'मल्लु भट्टि विक्रमार्क', 'मल्लू भट्टी विक्रमार्क'), 'INC', '2023-12-07', 'newsonair', 'https://www.newsonair.gov.in/telangana-budget-session-begins-today-governor-to-address-joint-sitting-of-both-houses', 'https://www.telangana.gov.in', note='Official confirmation: News On AIR 16 Mar 2026: Deputy Chief Minister Mallu Bhatti Vikramarka to present the budget. Sworn in with the Chief Minister on 7 December 2023 (The Tribune).', as_of='2026-10-27'),
        office("speaker", L("Gaddam Prasad Kumar", "गड्डम प्रसाद कुमार", "गड्डम प्रसाद कुमार"), "INC", "2023-12-14", "thesouthfirst", SPK, "https://www.telangana.gov.in",
               conf="Third-party verified", note="Elected unopposed on 14 December 2023, the State's first Dalit Speaker (The South First). Confirm on the Legislature website."),
    ],
}

r["projects"] = [
    proj("pm-mitra-warangal", L("PM MITRA Park — Kakatiya Mega Textile Park, Warangal", "पीएम मित्र पार्क — काकतीय मेगा टेक्सटाइल पार्क, वारंगल", "पीएम मित्र पार्क — काकतीय मेगा टेक्सटाइल पार्क, वरंगळ"),
         L("An integrated textile park from fibre to garment under the PM MITRA scheme. The Prime Minister's Office listed it for inauguration by the Prime Minister on 10 May 2026.",
           "पीएम मित्र योजना के अंतर्गत रेशे से परिधान तक का एकीकृत वस्त्र पार्क। प्रधानमंत्री कार्यालय ने 10 मई 2026 को प्रधानमंत्री द्वारा इसके उद्घाटन की सूचना दी।",
           "पीएम मित्र योजनेअंतर्गत धाग्यापासून कपड्यापर्यंतचे एकात्मिक वस्त्र उद्यान. पंतप्रधान कार्यालयाने 10 मे 2026 रोजी पंतप्रधानांच्या हस्ते त्याच्या उद्घाटनाची माहिती दिली."),
         "industry", "Ministry of Textiles / Government of Telangana", 1700, "About ₹1,700 crore (PMO).", "2026", None, "10 May 2026", "Completed", "pmindia", PMO,
         challenges=L("Track the number of units in operation.", "चालू इकाइयों की संख्या पर नज़र रखें।", "कार्यरत कारखान्यांची संख्या तपासा.")),
    proj("zaheerabad", L("Zaheerabad Industrial Area (Hyderabad–Nagpur Industrial Corridor)", "ज़हीराबाद औद्योगिक क्षेत्र (हैदराबाद–नागपुर औद्योगिक गलियारा)", "झहीराबाद औद्योगिक क्षेत्र (हैदराबाद–नागपूर औद्योगिक मार्गिका)"),
         L("An industrial area of 3,245 acres in Sangareddy district under the National Industrial Corridor Development Programme; the Prime Minister laid the foundation stone on 10 May 2026.",
           "राष्ट्रीय औद्योगिक गलियारा विकास कार्यक्रम के अंतर्गत संगारेड्डी ज़िले में 3,245 एकड़ का औद्योगिक क्षेत्र; प्रधानमंत्री ने 10 मई 2026 को इसकी आधारशिला रखी।",
           "राष्ट्रीय औद्योगिक मार्गिका विकास कार्यक्रमांतर्गत संगारेड्डी जिल्ह्यातील 3,245 एकरांचे औद्योगिक क्षेत्र; पंतप्रधानांनी 10 मे 2026 रोजी पायाभरणी केली."),
         "industry", "NICDC / Government of Telangana", 2350, "Over ₹2,350 crore (PMO).", "2026", "May 2026", None, "Under Construction", "pmindia", PMO),
    proj("nh167", L("NH-167 four-laning, Gudebellur–Mahabubnagar", "एनएच-167 चार-लेन, गुडेबेल्लूर–महबूबनगर", "एनएच-167 चौपदरीकरण, गुडेबेल्लूर–महबूबनगर"),
         L("Widening of a section of the Hyderabad–Panaji Economic Corridor linking Telangana and Karnataka; foundation stone laid on 10 May 2026.",
           "तेलंगाना और कर्नाटक को जोड़ने वाले हैदराबाद–पणजी आर्थिक गलियारे के एक खंड का चौड़ीकरण; 10 मई 2026 को आधारशिला रखी गई।",
           "तेलंगणा व कर्नाटकला जोडणाऱ्या हैदराबाद–पणजी आर्थिक मार्गिकेच्या एका टप्प्याचे रुंदीकरण; 10 मे 2026 रोजी पायाभरणी."),
         "transport", "NHAI / MoRTH", 3175, "Over ₹3,175 crore (PMO).", "2026", "May 2026", None, "Under Construction", "pmindia", PMO),
]

GI_NAMES = {
 "Tandur Redgram": ("तांडूर अरहर", "तांडूर तूर"),
 "Warangal Chapata Chilli": ("वारंगल चपाटा मिर्च", "वरंगळ चपाटा मिरची"),
 "Hyderabad Haleem": ("हैदराबाद हलीम", "हैदराबाद हलीम"),
 "Pochampally Ikat": ("पोचमपल्ली इकत", "पोचमपल्ली इकत"),
 "Silver Filigree of Karimnagar": ("करीमनगर की चाँदी की तारकशी", "करीमनगरचे चांदीचे तारकाम"),
 "Nirmal Toys and Craft": ("निर्मल खिलौने और शिल्प", "निर्मल खेळणी व हस्तकला"),
 "Nirmal Furniture": ("निर्मल फ़र्नीचर", "निर्मल फर्निचर"),
 "Nirmal Paintings": ("निर्मल चित्रकला", "निर्मल चित्रकला"),
 "Gadwal Sarees": ("गदवाल साड़ियाँ", "गदवाल साड्या"),
 "Siddipet Gollabama": ("सिद्दिपेट गोल्लभामा", "सिद्दिपेट गोल्लभामा"),
 "Cheriyal Paintings": ("चेरियाल चित्रकला", "चेरियाल चित्रकला"),
 "Pembarthi Metal Craft": ("पेम्बर्थी धातु शिल्प", "पेम्बर्थी धातुकला"),
 "Narayanpet Handloom Sarees": ("नारायणपेट हथकरघा साड़ियाँ", "नारायणपेठ हातमाग साड्या"),
 "Adilabad Dokra": ("आदिलाबाद डोकरा", "आदिलाबाद डोकरा"),
 "Warangal Durries": ("वारंगल दरियाँ", "वरंगळ सतरंज्या"),
 "Pochampally Ikat (Logo)": ("पोचमपल्ली इकत (लोगो)", "पोचमपल्ली इकत (बोधचिन्ह)"),
 "Telia Rumal": ("तेलिया रुमाल", "तेलिया रुमाल"),
 "Hyderabad Lac Bangles": ("हैदराबाद लाख की चूड़ियाँ", "हैदराबाद लाखेच्या बांगड्या"),
 "Banaganapalle Mangoes": ("बंगनपल्ले आम", "बंगनपल्ले आंबे"),
}
TEXTILE = {"Pochampally Ikat", "Pochampally Ikat (Logo)", "Gadwal Sarees", "Siddipet Gollabama", "Narayanpet Handloom Sarees", "Telia Rumal", "Warangal Durries"}
r["giProducts"] = gi_list("gi_tg.tsv", GI_NAMES, {"AP,TG": ["Andhra Pradesh"]}, TEXTILE)
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-TG.json", r)
print("tg core ok", len(r["giProducts"]), "GIs")
