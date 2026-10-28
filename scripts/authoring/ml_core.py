"""Meghalaya — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://meggovernor.gov.in/img/PressRelease-SwearingInCeremony.pdf"
CM = "https://morungexpress.com/conrad-sangma-takes-oath-as-meghalaya-cm-for-2nd-term"
SPK = "https://meghalaya.gov.in/circulars/content/44326"
HWY = "https://swarajyamag.com/amp/story/news-brief/pm-modi-to-lay-foundation-stone-of-rs-22864-crore-shillong-silchar-corridor-on-14-march-report"

mo = research("mospi_ml.json")
C = research("census_b5plus.json")
r = read("regions/IN-ML.json")
m = r["metrics"]
p = C["pop"]["ML"]
m["population2011"] = dp(p[0], "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 14,91,832; females 14,75,057.")
m["area"] = dp(22429, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(132, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 29,66,889 ÷ area 22,429 km² = 132.3.")
m["sexRatio2011"] = dp(989, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (972 in 2001).")
m["childSexRatio2011"] = dp(970, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 973 in 2001.")
m["literacyRate2011"] = dp(74.4, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25 is the latest year published for Meghalaya. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2023-24: ₹{inr(mo['pcnsdp']['FY2023-24'][0])}.")
m["forestCoverPct"] = dp(75.65, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 16,966.84 km² ÷ geographical area 22,429 km².")

r["officialPortal"] = "https://meghalaya.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Clouded leopard", "धूमिल तेंदुआ", "ढगाळ बिबट्या", "Neofelis nebulosa"),
    "bird": sym("Hill myna", "पहाड़ी मैना", "डोंगरी मैना", "Gracula religiosa"),
    "flower": sym("Lady's slipper orchid", "लेडीज़ स्लिपर ऑर्किड", "लेडीज स्लिपर ऑर्किड", "Paphiopedilum insigne"),
    "tree": sym("Gamhar", "गम्हार", "शिवण", "Gmelina arborea"),
}

r["government"] = {
    "headOfState": office("governor", L("C. H. Vijayashankar", "सी. एच. विजयशंकर", "सी. एच. विजयशंकर"), None, "2024-07-30",
                          "ml-governor", GOV, "https://meggovernor.gov.in", conf="Official",
                          note="Sworn in as Governor of Meghalaya on 30 July 2024 at Raj Bhavan, Shillong, by Chief Justice S. Vaidyanathan of the Meghalaya High Court (Lok Bhavan Meghalaya press release). He succeeded Phagu Chauhan."),
    "headOfGovernment": office('chief-minister', L('Conrad K. Sangma', 'कॉनराड के. संगमा', 'कॉनराड के. संगमा'), 'NPP', '2023-03-07', 'newsonair', 'https://www.newsonair.gov.in/wp-content/uploads/2026/02/shillong-4.pdf', 'https://meghalaya.gov.in', note="Official confirmation: Akashvani Shillong bulletin 16 Feb 2026: Chief Minister Conrad K Sangma, who holds the finance portfolio, to present the 2026-27 budget. Sworn in for a second term on 7 March 2023 in Shillong, heading the Meghalaya Democratic Alliance (MDA 2.0) led by the National People's Party, with Prestone Tynsong and Sniawbhalang Dhar as Deputy Chief Ministers (The Morung Express). First sworn in as Chief Minister in March 2018.", as_of='2026-10-27'),
    "others": [
        office("speaker", L("Thomas A. Sangma", "थॉमस ए. संगमा", "थॉमस ए. संगमा"), "NPP", "2023-03-09", "ml-gov", SPK, "https://meghalaya.gov.in", conf="Official",
               note="Elected Speaker of the Eleventh Meghalaya Legislative Assembly on 9 March 2023 (Legislative Assembly Secretariat notice No. LB.5/LA/2023/5)."),
    ],
}

r["projects"] = [
    proj("shillong-silchar-corridor", L("Shillong–Silchar greenfield high-speed corridor (NH-06)", "शिलांग–सिलचर ग्रीनफ़ील्ड हाई-स्पीड कॉरिडोर (एनएच-06)", "शिलाँग–सिलचर ग्रीनफिल्ड हाय-स्पीड कॉरिडॉर (एनएच-06)"),
         L("A 166.80-km four-lane, access-controlled greenfield highway on NH-06 from Mawlyngkhung near Shillong to Panchgram near Silchar in Assam — 144.80 km in Meghalaya and 22 km in Assam — approved by the Cabinet Committee on Economic Affairs on 30 April 2025 at a capital cost of ₹22,864 crore under the hybrid annuity mode. It is meant to ease congestion on the existing NH-06 and improve links to Tripura, Mizoram, Manipur and the Barak Valley. In March 2026 NHIDCL was inviting bids for its four packages, and the Prime Minister was to lay the foundation stone at Silchar on 14 March 2026.",
           "शिलांग के पास मावलिंगखुंग से असम में सिलचर के पास पंचग्राम तक एनएच-06 पर 166.80 किमी लंबा चार-लेन, नियंत्रित प्रवेश वाला ग्रीनफ़ील्ड राजमार्ग — 144.80 किमी मेघालय में और 22 किमी असम में — जिसे आर्थिक मामलों की मंत्रिमंडलीय समिति ने 30 अप्रैल 2025 को हाइब्रिड एन्युटी मोड में ₹22,864 करोड़ की पूँजी लागत पर स्वीकृति दी। इसका उद्देश्य मौजूदा एनएच-06 पर भीड़ घटाना और त्रिपुरा, मिज़ोरम, मणिपुर और बराक घाटी से संपर्क बेहतर करना है। मार्च 2026 में एनएचआईडीसीएल इसके चार पैकेजों के लिए बोलियाँ आमंत्रित कर रहा था, और प्रधानमंत्री को 14 मार्च 2026 को सिलचर में आधारशिला रखनी थी।",
           "शिलाँगजवळील मावलिंगखुंग ते आसाममधील सिलचरजवळील पंचग्रामपर्यंत एनएच-06 वरील 166.80 किमी लांबीचा चौपदरी, नियंत्रित प्रवेशाचा ग्रीनफिल्ड महामार्ग — 144.80 किमी मेघालयात व 22 किमी आसाममध्ये — ज्याला आर्थिक व्यवहार मंत्रिमंडळ समितीने 30 एप्रिल 2025 रोजी हायब्रिड अॅन्युइटी पद्धतीने ₹22,864 कोटी भांडवली खर्चास मंजुरी दिली. विद्यमान एनएच-06 वरील कोंडी कमी करणे आणि त्रिपुरा, मिझोराम, मणिपूर व बराक खोऱ्याशी संपर्क सुधारणे हा त्याचा उद्देश आहे. मार्च 2026 मध्ये एनएचआयडीसीएल त्याच्या चार पॅकेजसाठी निविदा मागवत होते, आणि पंतप्रधान 14 मार्च 2026 रोजी सिलचर येथे पायाभरणी करणार होते."),
         "roads", "NHIDCL (Ministry of Road Transport and Highways)", 22864, "Total capital cost approved by the CCEA on 30 April 2025, including ₹12,087 crore civil cost and ₹3,503 crore land acquisition (PIB).", "2025",
         None, None, "Tendering", "pib", "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2125467", as_of="2026-10-28",
         supporting=[("swarajya", HWY, L("the four packages, NHIDCL's bidding and the foundation-stone plan (March 2026)",
                                         "चार पैकेज, एनएचआईडीसीएल की बोली प्रक्रिया और आधारशिला की योजना (मार्च 2026)",
                                         "चार पॅकेज, एनएचआयडीसीएलची निविदा प्रक्रिया आणि पायाभरणीचे नियोजन (मार्च 2026)"))]),
]

GI_NAMES = {
 "Memong Narang": ("मेमोंग नारंग (संतरा)", "मेमोंग नारंग (संत्रे)"),
 "Khasi Mandarin": ("खासी संतरा", "खासी संत्रे"),
 "Lakadong Turmeric": ("लाकाडोंग हल्दी", "लाकाडोंग हळद"),
 "Meghalaya Garo Textile": ("मेघालय गारो वस्त्र", "मेघालय गारो वस्त्र"),
 "Meghalaya Lyrnai Pottery": ("मेघालय लिरनाई मिट्टी के बर्तन", "मेघालय लिरनाई मातीची भांडी"),
 "Meghalaya Ryndia Textile": ("मेघालय रिंदिया वस्त्र", "मेघालय रिंदिया वस्त्र"),
 "Meghalaya Khasi Handloom Products": ("मेघालय खासी हथकरघा उत्पाद", "मेघालय खासी हातमाग उत्पादने"),
 "Meghalaya Chubitchi": ("मेघालय चुबित्ची (चावल पेय)", "मेघालय चुबित्ची (तांदळाचे पेय)"),
}
r["giProducts"] = gi_list("gi_ml.tsv", GI_NAMES, {}, {"Meghalaya Garo Textile", "Meghalaya Ryndia Textile", "Meghalaya Khasi Handloom Products"})
r["meta"] = {"lastUpdated": "2026-10-28",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-ML.json", r)
print("ml core ok", len(r["giProducts"]), "GIs")
