"""Mizoram — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.newsonair.gov.in/general-v-k-singh-sworn-in-as-governor-of-mizoram"
CM = "https://english.udayavani.com/article/lalduhoma-sworn-in-as-mizoram-cm/1571458"
SPK = "https://mizoramassembly.in/storage/bulletins/December2023/xSSgEja0GhYUSJda0FGz.pdf"
RAIL = "https://www.newsonair.gov.in/pm-modi-inaugurates-%E2%82%B98070-crore-bairabi-sairang-rail-line-mizoram-gets-first-rail-link"

mo = research("mospi_mz.json")
C = research("census_b5plus.json")
r = read("regions/IN-MZ.json")
m = r["metrics"]
p = C["pop"]["MZ"]
m["population2011"] = dp(p[0], "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 5,55,339; females 5,41,867.")
m["area"] = dp(21081, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(52, "persons per km²", "2011", "census", "census", PYD, note="Calculated: Census 2011 population 10,97,206 ÷ area 21,081 km² = 52.0.")
m["sexRatio2011"] = dp(976, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (935 in 2001).")
m["childSexRatio2011"] = dp(970, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 964 in 2001.")
m["literacyRate2011"] = dp(91.3, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25 is the latest year published for Mizoram. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2023-24: ₹{inr(mo['pcnsdp']['FY2023-24'][0])}.")
m["forestCoverPct"] = dp(85.34, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 17,990.46 km² ÷ geographical area 21,081 km².")
r["officialPortal"] = "https://mizoram.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Himalayan serow", "हिमालयी सीरो", "हिमालयी सेरो", "Capricornis sumatraensis thar"),
    "bird": sym("Mrs Hume's pheasant", "मिसेज़ ह्यूम्स फ़ेज़ेंट", "मिसेस ह्यूम्स फेझंट", "Syrmaticus humiae"),
    "flower": sym("Red vanda (orchid)", "लाल वांडा (ऑर्किड)", "लाल वांडा (ऑर्किड)", "Renanthera imschootiana"),
}

r["government"] = {
    "headOfState": office("governor", L("Gen. V. K. Singh (Retd)", "जनरल वी. के. सिंह (सेवानिवृत्त)", "जनरल व्ही. के. सिंह (निवृत्त)"), None, "2025-01-16",
                          "newsonair", GOV, "https://rajbhavan.mizoram.gov.in", conf="Official",
                          note="Former Chief of the Army Staff; sworn in as Governor of Mizoram on 16 January 2025 at Raj Bhavan, Aizawl, by Chief Justice Vijay Bishnoi of the Gauhati High Court (All India Radio News)."),
    "headOfGovernment": office('chief-minister', L('Lalduhoma', 'लालदुहोमा', 'लालदुहोमा'), 'ZPM', '2023-12-08', 'newsonair', 'https://newsonair.gov.in/wp-content/uploads/2026/09/aizwal.pdf', 'https://mizoram.gov.in', note="Official confirmation: Akashvani Aizawl regional bulletin 1 Sep 2026: Chief Minister Pu Lalduhoma on the Winter Festival. Sworn in on 8 December 2023 at Raj Bhavan, Aizawl, by Governor Kambhampati Hari Babu, after the Zoram People's Movement won 27 of the 40 seats (Udayavani/PTI).", as_of='2026-10-27'),
    "others": [
        office("speaker", L("Lalbiakzama", "लालबियाकज़ामा", "लालबियाकझामा"), "ZPM", "2023-12-12", "mz-assembly", SPK, "https://mizoramassembly.in", conf="Official",
               note="Elected unopposed as Speaker of the Ninth Mizoram Legislative Assembly on 12 December 2023 (Assembly bulletin)."),
    ],
}

r["projects"] = [
    proj("bairabi-sairang-rail", L("Bairabi–Sairang new railway line", "बइराबी–सैरांग नई रेल लाइन", "बइराबी–सैरांग नवा रेल्वेमार्ग"),
         L("A broad-gauge line from Bairabi on the Assam border to Sairang near Aizawl, built through steep hills with many tunnels and tall bridges, which put Mizoram's capital on the railway map. The Prime Minister inaugurated it on 13 September 2025 at a reported cost of ₹8,070 crore and flagged off a Rajdhani Express to Delhi and trains to Guwahati and Kolkata.",
           "असम सीमा पर बइराबी से आइज़ोल के पास सैरांग तक बड़ी लाइन, जो खड़ी पहाड़ियों से होकर कई सुरंगों और ऊँचे पुलों के साथ बनी और जिसने मिज़ोरम की राजधानी को रेल मानचित्र पर ला दिया। प्रधानमंत्री ने 13 सितंबर 2025 को ₹8,070 करोड़ की बताई गई लागत वाली इस लाइन का उद्घाटन किया और दिल्ली के लिए राजधानी एक्सप्रेस तथा गुवाहाटी और कोलकाता के लिए ट्रेनों को हरी झंडी दिखाई।",
           "आसाम सीमेवरील बइराबीपासून आयझॉलजवळील सैरांगपर्यंतचा ब्रॉडगेज मार्ग, जो तीव्र डोंगरांतून अनेक बोगदे व उंच पुलांसह बांधला गेला आणि ज्याने मिझोरामची राजधानी रेल्वे नकाशावर आणली. पंतप्रधानांनी 13 सप्टेंबर 2025 रोजी ₹8,070 कोटी खर्चाच्या या मार्गाचे उद्घाटन केले आणि दिल्लीसाठी राजधानी एक्सप्रेस व गुवाहाटी आणि कोलकात्यासाठी गाड्यांना हिरवा झेंडा दाखवला."),
         "railways", "Northeast Frontier Railway", 8070, "Cost as stated at the inauguration (All India Radio News, 13 Sep 2025).", "2025",
         None, "13 September 2025", "Completed", "newsonair", RAIL),
]

GI_NAMES = {
 "Mizo Chilli": ("मिज़ो मिर्च", "मिझो मिरची"),
 "Mizo Ginger": ("मिज़ो अदरक", "मिझो आले"),
 "Tawlhlohpuan": ("तॉल्ह्लोहपुआन (वस्त्र)", "तॉल्ह्लोहपुआन (वस्त्र)"),
 "Mizo Puanchei": ("मिज़ो पुआनचेई (वस्त्र)", "मिझो पुआनचेई (वस्त्र)"),
 "Pawndum": ("पॉनदुम (वस्त्र)", "पॉनदुम (वस्त्र)"),
 "Ngotekherh": ("ङोतेखेर्ह (वस्त्र)", "ङोतेखेर्ह (वस्त्र)"),
 "Hmaram": ("ह्मारम (वस्त्र)", "ह्मारम (वस्त्र)"),
}
r["giProducts"] = gi_list("gi_mz.tsv", GI_NAMES, {}, {"Tawlhlohpuan", "Mizo Puanchei", "Pawndum", "Ngotekherh", "Hmaram"})
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-MZ.json", r)
print("mz core ok", len(r["giProducts"]), "GIs")
