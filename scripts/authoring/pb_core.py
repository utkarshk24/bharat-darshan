"""Punjab — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-16."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.newsonair.gov.in/gulab-chand-kataria-takes-oath-as-governor-of-punjab/"
CM = "https://www.deccanherald.com/amp/story/india%2Fpunjab-cm-bhagwant-mann-assumes-office-1091892.html"
SPK = "https://www.etvbharat.com/english/state/punjab/aap-mla-kultar-sandhwan-elected-punjab-assembly-speaker/na20220321205119608"
AIIMS = "https://pmindia.gov.in/?p=16392426"
SEMI = "https://www.pmindia.gov.in/en/news_updates/cabinet-approves-semiconductor-manufacturing-units-in-odisha-punjab-and-andhra-pradesh-with-an-outlay-of-rs-4600-crore"

mo = research("mospi_pb.json")
r = read("regions/IN-PB.json")
m = r["metrics"]
m["population2011"] = dp(27743338, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 1,46,39,465; females 1,31,03,873.")
m["area"] = dp(50362, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(551, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 2,77,43,338 ÷ area 50,362 km² = 550.9.")
m["sexRatio2011"] = dp(895, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (876 in 2001).")
m["childSexRatio2011"] = dp(846, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 798 in 2001.")
m["literacyRate2011"] = dp(75.8, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25 is the latest year published for Punjab. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2023-24: ₹{inr(mo['pcnsdp']['FY2023-24'][0])}.")
m["forestCoverPct"] = dp(3.67, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 1,846.09 km² ÷ geographical area 50,362 km².")

r["officialPortal"] = "https://punjab.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Blackbuck", "काला हिरण", "काळवीट", "Antilope cervicapra"),
    "bird": sym("Northern goshawk (baaz)", "बाज़", "ससाणा (बाज)", "Accipiter gentilis"),
    "tree": sym("Shisham", "शीशम", "शिसम", "Dalbergia sissoo"),
}

r["government"] = {
    "headOfState": office("governor", L("Gulab Chand Kataria", "गुलाब चंद कटारिया", "गुलाबचंद कटारिया"), None, "2024-07-31",
                          "newsonair", GOV, "https://punjabrajbhavan.gov.in",
                          note="Also Administrator of the Union Territory of Chandigarh. Sworn in at Punjab Raj Bhavan on 31 July 2024 by Chief Justice Sheel Nagu of the Punjab and Haryana High Court (News On AIR)."),
    "headOfGovernment": office("chief-minister", L("Bhagwant Mann", "भगवंत मान", "भगवंत मान"), "AAP", "2022-03-16",
                               "deccan-herald", CM, "https://punjab.gov.in", conf="Third-party verified",
                               note="Sworn in on 16 March 2022 at Khatkar Kalan, the ancestral village of Bhagat Singh, by Governor Banwarilal Purohit (Deccan Herald / PTI)."),
    "others": [
        office('speaker', L('Kultar Singh Sandhwan', 'कुलतार सिंह संधवां', 'कुलतार सिंह संधवां'), 'AAP', '2022-03-21', 'pb-ipr', 'https://ipr.punjab.gov.in/en/press-releases/hq-press-releases/punjab-vidhan-sabha-speaker-s-kultar-singh-sandhwan-attends-85th-all-india-presiding-officers-conference-in-patna-pays-obeisance-at-vaishali-stupa', 'https://punjabassembly.gov.in', note="Official confirmation: DIPR Punjab release, Chandigarh 22 Jan 2025: Punjab Vidhan Sabha Speaker S. Kultar Singh Sandhwan. Elected unanimously as Speaker of the 16th Punjab Vidhan Sabha on 21 March 2022; MLA from Kotkapura (ETV Bharat). The Assembly's notification of 22 March 2022 could not be read here.", as_of='2026-10-27'),
    ],
}

r["projects"] = [
    proj("aiims-bathinda", L("AIIMS Bathinda", "एम्स बठिंडा", "एम्स भटिंडा"),
         L("Punjab's All India Institute of Medical Sciences at Bathinda, dedicated to the nation by the Prime Minister on 25 February 2024 together with AIIMS Rajkot, Raebareli, Mangalagiri and Kalyani. The same day a 300-bed PGIMER satellite centre at Sangrur was dedicated and the foundation stone of a 100-bed centre at Ferozepur laid.",
           "बठिंडा में पंजाब का अखिल भारतीय आयुर्विज्ञान संस्थान, जिसे प्रधानमंत्री ने 25 फ़रवरी 2024 को एम्स राजकोट, रायबरेली, मंगलगिरि और कल्याणी के साथ राष्ट्र को समर्पित किया। उसी दिन संगरूर में पीजीआईएमईआर का 300 बिस्तरों वाला उपग्रह केंद्र समर्पित किया गया और फ़िरोज़पुर में 100 बिस्तरों वाले केंद्र की आधारशिला रखी गई।",
           "भटिंडा येथील पंजाबचे अखिल भारतीय आयुर्विज्ञान संस्थान, जे पंतप्रधानांनी 25 फेब्रुवारी 2024 रोजी एम्स राजकोट, रायबरेली, मंगलगिरी व कल्याणीसोबत राष्ट्राला समर्पित केले. त्याच दिवशी संगरूर येथील पीजीआयएमईआरचे 300 खाटांचे उपकेंद्र समर्पित करण्यात आले व फिरोजपूर येथील 100 खाटांच्या केंद्राची पायाभरणी झाली."),
         "health", "Ministry of Health and Family Welfare", None, None, None, None, "25 February 2024", "Completed", "pmindia", AIIMS),
    proj("cdil-mohali", L("CDIL power-semiconductor expansion, Mohali", "सीडीआईएल पावर सेमीकंडक्टर विस्तार, मोहाली", "सीडीआयएल पॉवर सेमीकंडक्टर विस्तार, मोहाली"),
         L("A brownfield expansion by Continental Device India Ltd at Mohali to make high-power discrete semiconductors — MOSFETs, IGBTs, Schottky bypass diodes and transistors — in silicon and silicon carbide, with an annual capacity of 158.38 million units. Approved by the Union Cabinet on 12 August 2025 among four units with a combined investment of about ₹4,600 crore.",
           "मोहाली में कॉन्टिनेंटल डिवाइस इंडिया लि. द्वारा सिलिकॉन और सिलिकॉन कार्बाइड में उच्च-शक्ति डिस्क्रीट सेमीकंडक्टर — मॉसफ़ेट, आईजीबीटी, शॉटकी बाईपास डायोड और ट्रांज़िस्टर — बनाने के लिए विस्तार, जिसकी वार्षिक क्षमता 15.838 करोड़ इकाइयाँ है। केंद्रीय मंत्रिमंडल ने 12 अगस्त 2025 को लगभग ₹4,600 करोड़ के संयुक्त निवेश वाली चार इकाइयों में इसे मंज़ूरी दी।",
           "मोहाली येथे कॉन्टिनेंटल डिव्हाइस इंडिया लि.कडून सिलिकॉन व सिलिकॉन कार्बाइडमध्ये उच्च-शक्ती डिस्क्रीट सेमीकंडक्टर — मॉसफेट, आयजीबीटी, शॉटकी बायपास डायोड व ट्रान्झिस्टर — बनवण्यासाठीचा विस्तार, ज्याची वार्षिक क्षमता 15.838 कोटी युनिट्स आहे. केंद्रीय मंत्रिमंडळाने 12 ऑगस्ट 2025 रोजी सुमारे ₹4,600 कोटींच्या एकत्रित गुंतवणुकीच्या चार प्रकल्पांत याला मंजुरी दिली."),
         "industry", "Continental Device India Pvt Ltd (India Semiconductor Mission)", None, None, None, "Approved 12 August 2025", None, "Announced", "pmindia", SEMI),
]

GI_NAMES = {
 "Basmati": ("बासमती", "बासमती"),
 "Phulkari": ("फुलकारी", "फुलकारी"),
}
SHARED = {"PB,HR,HP,DL,UK,UP,JK": ["Haryana", "Himachal Pradesh", "Delhi", "Uttarakhand", "Uttar Pradesh", "Jammu & Kashmir"],
          "PB,HR,RJ": ["Haryana", "Rajasthan"]}
r["giProducts"] = gi_list("gi_pb.tsv", GI_NAMES, SHARED, {"Phulkari"})
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-PB.json", r)
print("pb core ok", len(r["giProducts"]), "GIs")
