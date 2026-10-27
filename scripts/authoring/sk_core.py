"""Sikkim — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://eastmojo.com/sikkim/2026/10/19/dushyant-kumar-gautam-sworn-in-as-sikkim-governor/"
CM = "https://scroll.in/latest/1069105/prem-singh-tamang-sworn-in-as-sikkim-chief-minister-for-second-consecutive-term"
SPK = "https://sikkim.gov.in/uploads//Notifications/Speaker_SLA_73_20240621.pdf"
PAKYONG = "https://www.pmindia.gov.in/en/news_updates/pm-inaugurates-pakyong-airport-as-air-connectivity-reaches-sikkim/"
SEVOKE = "https://morungexpress.com/railways-panel-inspects-sivokrangpo-line-works"

mo = research("mospi_sk.json")
C = research("census_b5plus.json")
r = read("regions/IN-SK.json")
m = r["metrics"]
p = C["pop"]["SK"]
m["population2011"] = dp(p[0], "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 3,23,070; females 2,87,507.")
m["area"] = dp(7096, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(86, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 6,10,577 ÷ area 7,096 km² = 86.0.")
m["sexRatio2011"] = dp(890, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (875 in 2001).")
m["childSexRatio2011"] = dp(957, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 963 in 2001.")
m["literacyRate2011"] = dp(81.4, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25 is the latest year published for Sikkim. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2023-24: ₹{inr(mo['pcnsdp']['FY2023-24'][0])}. The highest of the 30 regions with a FY2024-25 figure in the MoSPI series.")
m["forestCoverPct"] = dp(47.33, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 3,358.40 km² ÷ geographical area 7,096 km². Much of the north is alpine meadow, rock, snow and glacier above the tree line.")

r["officialPortal"] = "https://sikkim.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Red panda", "लाल पांडा", "लाल पांडा", "Ailurus fulgens"),
    "bird": sym("Blood pheasant", "रक्त तीतर (ब्लड फ़ेज़ेंट)", "रक्त तितर (ब्लड फेझंट)", "Ithaginis cruentus"),
    "flower": sym("Noble dendrobium (orchid)", "नोबल डेंड्रोबियम (ऑर्किड)", "नोबल डेंड्रोबियम (ऑर्किड)", "Dendrobium nobile"),
}

r["government"] = {
    "headOfState": office('governor', L('Dushyant Kumar Gautam', 'दुष्यंत कुमार गौतम', 'दुष्यंत कुमार गौतम'), None, '2026-10-19', 'president-of-india', 'https://presidentofindia.nic.in/press_releases/press-communique-38', 'https://rajbhavansikkim.gov.in', note='Official confirmation: Rashtrapati Bhavan communique 12 Oct 2026: Dushyant Gautam appointed Governor of Sikkim. Sworn in as the 19th Governor of Sikkim at Lok Bhavan, Gangtok, on 19 October 2026 by Chief Justice A. Muhamed Mustaque of the Sikkim High Court, after his appointment by the President on 12 October; succeeded Om Prakash Mathur (EastMojo).', as_of='2026-10-27'),
    "headOfGovernment": office('chief-minister', L('Prem Singh Tamang (Golay)', 'प्रेम सिंह तमांग (गोले)', 'प्रेम सिंह तमांग (गोले)'), 'SKM', '2024-06-10', 'sk-gov', 'https://ipr.sikkim.gov.in/Home/HcmProfile', 'https://sikkim.gov.in', note="Official confirmation: IPR Sikkim, Hon'ble Chief Minister profile: Shri Prem Singh Tamang (Golay); first sworn in 27 May 2019. Sworn in for a second consecutive term on 10 June 2024 in Gangtok by Governor Lakshman Acharya, after the Sikkim Krantikari Morcha won the 2024 Assembly election; MLA from Rhenock (Scroll).", as_of='2026-10-27'),
    "others": [
        office("speaker", L("Mingma Norbu Sherpa", "मिंगमा नोर्बु शेर्पा", "मिंगमा नोर्बु शेर्पा"), "SKM", "2024-06-12", "sk-gov", SPK, "https://sikkim.gov.in", conf="Official",
               note="Elected Speaker of the Eleventh Sikkim Legislative Assembly on 12 June 2024 (Sikkim Legislative Assembly notification, 21 June 2024)."),
    ],
}

r["projects"] = [
    proj("pakyong-airport", L("Pakyong Airport", "पाक्योंग हवाई अड्डा", "पाकयोंग विमानतळ"),
         L("Sikkim's first airport, at Pakyong about 30 km from Gangtok, inaugurated by the Prime Minister on 24 September 2018 as India's 100th airport and part of the UDAN regional connectivity scheme. Before it, the nearest airport was Bagdogra in West Bengal, a four-hour drive away. Flights have been irregular because of the hill-top runway and frequent low cloud.",
           "पाक्योंग में, गंगटोक से लगभग 30 किमी दूर, सिक्किम का पहला हवाई अड्डा, जिसका प्रधानमंत्री ने 24 सितंबर 2018 को देश के 100वें हवाई अड्डे और उड़ान क्षेत्रीय संपर्क योजना के भाग के रूप में उद्घाटन किया। इससे पहले निकटतम हवाई अड्डा पश्चिम बंगाल का बागडोगरा था, जो चार घंटे की दूरी पर है। पहाड़ी पर बने रनवे और बार-बार नीचे छाए बादलों के कारण उड़ानें अनियमित रही हैं।",
           "पाकयोंग येथे, गंगटोकपासून सुमारे 30 किमी, सिक्कीमचा पहिला विमानतळ, ज्याचे पंतप्रधानांनी 24 सप्टेंबर 2018 रोजी देशाचा 100 वा विमानतळ व उडान प्रादेशिक संपर्क योजनेचा भाग म्हणून उद्घाटन केले. त्यापूर्वी जवळचा विमानतळ पश्चिम बंगालमधील बागडोगरा होता, चार तासांच्या अंतरावर. डोंगरमाथ्यावरील धावपट्टी व वारंवार खाली येणाऱ्या ढगांमुळे उड्डाणे अनियमित राहिली आहेत."),
         "aviation", "Airports Authority of India", None, None, None, None, "24 September 2018", "Completed", "pmindia", PAKYONG),
    proj("sivok-rangpo-rail", L("Sivok–Rangpo new railway line", "सेवक–रंगपो नई रेल लाइन", "सेवक–रंगपो नवा रेल्वेमार्ग"),
         L("A 44.96-km broad-gauge line from Sivok in West Bengal to Rangpo on the Sikkim border, mostly in tunnels and on bridges along the Teesta valley, which will give Sikkim its first rail link. IRCON told a parliamentary committee in June 2026 that physical progress was 77% and that the line is targeted for completion by December 2027.",
           "पश्चिम बंगाल के सेवक से सिक्किम सीमा पर रंगपो तक 44.96 किमी लंबी बड़ी लाइन, जो तीस्ता घाटी में अधिकतर सुरंगों और पुलों पर है और सिक्किम को पहला रेल संपर्क देगी। इरकॉन ने जून 2026 में एक संसदीय समिति को बताया कि भौतिक प्रगति 77% थी और लाइन को दिसंबर 2027 तक पूरा करने का लक्ष्य है।",
           "पश्चिम बंगालमधील सेवक ते सिक्कीम सीमेवरील रंगपोपर्यंतचा 44.96 किमी लांबीचा ब्रॉडगेज मार्ग, जो तिस्ता खोऱ्यात बहुतांश बोगदे व पुलांवर आहे आणि सिक्कीमला पहिला रेल्वे संपर्क देईल. इरकॉनने जून 2026 मध्ये संसदीय समितीला सांगितले की भौतिक प्रगती 77% होती आणि मार्ग डिसेंबर 2027 पर्यंत पूर्ण करण्याचे उद्दिष्ट आहे."),
         "railways", "IRCON International (for Indian Railways)", None, None, None, None, "December 2027 (target)", "Under Construction", "morung-express", SEVOKE, conf="Third-party verified"),
]

GI_NAMES = {
 "Sikkim Large Cardamom": ("सिक्किम बड़ी इलायची", "सिक्कीम मोठी वेलची"),
 "Sikkim Lepcha Tungbuk": ("सिक्किम लेप्चा तुंगबुक", "सिक्कीम लेप्चा तुंगबुक"),
 "Sikkim Lepcha Pumtong Pulit (Flute)": ("सिक्किम लेप्चा पुमतोंग पुलित (बाँसुरी)", "सिक्कीम लेप्चा पुमतोंग पुलित (बासरी)"),
 "Dalle Khursani": ("डल्ले खुर्सानी (मिर्च)", "डल्ले खुर्सानी (मिरची)"),
}
r["giProducts"] = gi_list("gi_sk.tsv", GI_NAMES, {"SK,WB": ["West Bengal"]}, set())
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-SK.json", r)
print("sk core ok", len(r["giProducts"]), "GIs")
