"""Nagaland — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.newsonair.gov.in/wp-content/uploads/2026/03/kohima-text-1920-2.pdf"
CM = "https://www.tribuneindia.com/news/nation/rio-becomes-nagaland-cm-for-5th-term-486121"
MERGER = "https://www.newsonair.gov.in/wp-content/uploads/2025/10/kohiam-en-g1920.pdf"
SPK = "https://eastmojo.com/nagaland/2023/03/20/sharingain-longkumer-re-elected-as-nagaland-speaker-for-second-time/"
RAIL = "https://morungexpress.com/railways-target-2029-completion-of-dimapurkohima-line"

E = research("econ_nl.json")
C = research("census_b5plus.json")
r = read("regions/IN-NL.json")
m = r["metrics"]
p = C["pop"]["NL"]
m["population2011"] = dp(p[0], "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 10,24,649; females 9,53,853.")
m["area"] = dp(16579, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(119, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 19,78,502 ÷ area 16,579 km² = 119.3.")
m["sexRatio2011"] = dp(931, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (900 in 2001).")
m["childSexRatio2011"] = dp(943, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 964 in 2001.")
m["literacyRate2011"] = dp(79.6, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(E["gsdp_current"]["FY2025-26"], "₹ crore", "FY2025-26", "fy", "morung-express", E["url"], rev="provisional", base=CUR, conf="Third-party verified",
    note="Nagaland Economic Survey 2025-26 (advance estimate), as reported by The Morung Express on 9 March 2026. MoSPI's state series has no figure for Nagaland. FY2024-25 (provisional): ₹45,133 crore.")
m["perCapitaNsdpCurrent"] = dp(E["per_capita_income"]["FY2025-26"], "₹", "FY2025-26", "fy", "morung-express", E["url"], rev="provisional", base=CUR, conf="Third-party verified",
    note="Per capita income, Nagaland Economic Survey 2025-26 (advance estimate), as reported by The Morung Express. Not from the MoSPI series, so compare with other States with care.")
m["forestCoverPct"] = dp(73.72, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 12,222.47 km² ÷ geographical area 16,579 km².")

r["officialPortal"] = "https://www.nagaland.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Mithun", "मिथुन", "मिथुन", "Bos frontalis"),
    "bird": sym("Blyth's tragopan", "ब्लाइथ ट्रैगोपैन", "ब्लायथ ट्रॅगोपॅन", "Tragopan blythii"),
    "tree": sym("Alder", "आल्डर", "आल्डर", "Alnus nepalensis"),
}

r["government"] = {
    "headOfState": office("governor", L("Nand Kishore Yadav", "नंद किशोर यादव", "नंदकिशोर यादव"), None, "2026-03-13",
                          "newsonair", GOV, "https://rajbhavan.nagaland.gov.in", conf="Official",
                          note="Sworn in as the 23rd Governor of Nagaland on 13 March 2026; the oath was administered by Chief Justice Ashutosh Kumar of the Gauhati High Court (All India Radio News, Kohima). He was appointed by the President on 5 March and succeeded Ajay Kumar Bhalla, who had held additional charge."),
    "headOfGovernment": office("chief-minister", L("Neiphiu Rio", "नेफ़्यू रियो", "नेफ्यू रियो"), "NPF", "2023-03-07",
                               "tribune", CM, "https://www.nagaland.gov.in", conf="Third-party verified",
                               note=f"Sworn in for a fifth term on 7 March 2023 at the Capital Cultural Hall, Kohima, by Governor La Ganesan, with T. R. Zeliang and Y. Patton as Deputy Chief Ministers (The Tribune). He then led the NDPP, which merged with the Naga People's Front on 18 October 2025; Rio was elected leader of the NPF legislature party (All India Radio News, {MERGER})."),
    "others": [
        office("speaker", L("Sharingain Longkumer", "शरिंगेन लोंगकुमेर", "शरिंगेन लोंगकुमेर"), None, "2023-03-20", "eastmojo", SPK, "https://www.nagaland.gov.in", conf="Third-party verified",
               note="Re-elected unopposed as Speaker of the 14th Nagaland Legislative Assembly on 20 March 2023 (EastMojo); MLA from Aonglenden. He was first elected Speaker in 2020."),
    ],
}

r["projects"] = [
    proj("dimapur-kohima-rail", L("Dhansiri (Dimapur)–Zubza (Kohima) new railway line", "धनसिरी (दीमापुर)–ज़ुबज़ा (कोहिमा) नई रेल लाइन", "धनसिरी (दिमापूर)–झुबझा (कोहिमा) नवा रेल्वेमार्ग"),
         L("A 78.42-km broad-gauge line from Dhansiri near Dimapur to Zubza near Kohima, through Assam's Karbi Anglong and Nagaland's Chümoukedima and Kohima districts, which will bring the railway to the State capital. The 16.5-km Dhansiri–Shokhuvi section opened in October 2021 and the 14.64-km Shokhuvi–Molvom section in March 2025; 20 tunnels and 27 major bridges remained, and Northeast Frontier Railway targets completion by 2029.",
           "दीमापुर के पास धनसिरी से कोहिमा के पास ज़ुबज़ा तक 78.42 किमी लंबी बड़ी लाइन, जो असम के कार्बी आंगलोंग और नागालैंड के चुमौकेदिमा और कोहिमा ज़िलों से गुज़रेगी और राज्य की राजधानी तक रेल लाएगी। 16.5 किमी का धनसिरी–शोखुवी खंड अक्टूबर 2021 में और 14.64 किमी का शोखुवी–मोलवोम खंड मार्च 2025 में खुला; 20 सुरंगें और 27 बड़े पुल शेष थे, और पूर्वोत्तर सीमांत रेलवे ने 2029 तक पूरा करने का लक्ष्य रखा है।",
           "दिमापूरजवळील धनसिरी ते कोहिमाजवळील झुबझापर्यंतचा 78.42 किमी लांबीचा ब्रॉडगेज मार्ग, जो आसाममधील कार्बी आंगलोंग व नागालँडमधील चुमौकेदिमा आणि कोहिमा जिल्ह्यांतून जाईल व राज्याच्या राजधानीपर्यंत रेल्वे आणेल. 16.5 किमीचा धनसिरी–शोखुवी टप्पा ऑक्टोबर 2021 मध्ये व 14.64 किमीचा शोखुवी–मोलवोम टप्पा मार्च 2025 मध्ये सुरू झाला; 20 बोगदे व 27 मोठे पूल बाकी होते, आणि ईशान्य सीमा रेल्वेने 2029 पर्यंत पूर्णत्वाचे उद्दिष्ट ठेवले आहे."),
         "railways", "Northeast Frontier Railway", None, None, None, None, "2029 (target)", "Under Construction", "morung-express", RAIL, conf="Third-party verified"),
]

GI_NAMES = {
 "Naga Mircha": ("नागा मिर्च", "नागा मिरची"),
 "Naga Tree Tomato": ("नागा ट्री टमाटर", "नागा झाड-टोमॅटो"),
 "Naga Cucumber": ("नागा खीरा", "नागा काकडी"),
 "Chakhesang Shawl": ("चाखेसांग शॉल", "चाखेसांग शाल"),
 "Chak-Hao": ("चाक-हाओ (काला चावल)", "चाक-हाओ (काळा तांदूळ)"),
}
r["giProducts"] = gi_list("gi_nl.tsv", GI_NAMES, {"MN,NL": ["Manipur"]}, {"Chakhesang Shawl"})
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-NL.json", r)
print("nl core ok", len(r["giProducts"]), "GIs")
