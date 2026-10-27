"""Himachal Pradesh — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-24."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://kashmirlife.net/kavinder-gupta-sworn-in-as-himachal-pradesh-governor-427832/"
CM = "https://scroll.in/latest/1039488/sukhvinder-singh-sukhu-takes-oath-as-chief-minister-of-himachal-pradesh"
SPK = "https://www.etvbharat.com/english/bharat/kuldeep-singh-pathania-elected-speaker-of-himachal-assembly/na20230105164418859859297"
ATAL = "https://pmindia.gov.in/?p=8160111"
AIIMS = "https://pmindia.gov.in/?p=13271571"
NH = "https://pmindia.gov.in/?p=16403991"

mo = research("mospi_hp.json")
C = research("census_b5plus.json")
r = read("regions/IN-HP.json")
m = r["metrics"]
p = C["pop"]["HP"]
m["population2011"] = dp(p[0], "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 34,81,873; females 33,82,729.")
m["area"] = dp(55673, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(123, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 68,64,602 ÷ area 55,673 km² = 123.3.")
m["sexRatio2011"] = dp(972, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (968 in 2001).")
m["childSexRatio2011"] = dp(909, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 896 in 2001.")
m["literacyRate2011"] = dp(82.8, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25 is the latest year published for Himachal Pradesh. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2023-24: ₹{inr(mo['pcnsdp']['FY2023-24'][0])}.")
m["forestCoverPct"] = dp(27.99, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 15,580.35 km² ÷ geographical area 55,673 km². Much of the rest is alpine pasture, rock and snow above the tree line.")

r["officialPortal"] = "https://himachal.nic.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Snow leopard", "हिम तेंदुआ", "हिमबिबट्या", "Panthera uncia"),
    "bird": sym("Western tragopan (jujurana)", "जाजुराना (पश्चिमी ट्रैगोपैन)", "जुजुराना (पश्चिमी ट्रॅगोपॅन)", "Tragopan melanocephalus"),
    "tree": sym("Deodar", "देवदार", "देवदार", "Cedrus deodara"),
    "flower": sym("Pink rhododendron", "गुलाबी बुरांस", "गुलाबी बुरांस (र्‍होडोडेंड्रॉन)", "Rhododendron campanulatum"),
}

r["government"] = {
    "headOfState": office('governor', L('Kavinder Gupta', 'कविंद्र गुप्ता', 'कविंदर गुप्ता'), None, '2026-03-10', 'newsonair', 'https://www.newsonair.gov.in/governor-designate-kavinder-gupta-receives-warm-welcome-in-shimla', 'https://himachal.nic.in', note='Official confirmation: News On AIR 9 Mar 2026: Governor-designate Kavinder Gupta to take oath as 30th Governor on 10 Mar 2026. Sworn in as the 30th Governor of Himachal Pradesh at Raj Bhavan (Lok Bhavan), Shimla, on 10 March 2026 by Chief Justice Gurmeet Singh Sandhawalia of the Himachal Pradesh High Court (Kashmir Life; also reported by PTI). Previously Lieutenant Governor of Ladakh; succeeded Shiv Pratap Shukla.', as_of='2026-10-27'),
    "headOfGovernment": office('chief-minister', L('Sukhvinder Singh Sukhu', 'सुखविंदर सिंह सुक्खू', 'सुखविंदर सिंह सुक्खू'), 'INC', '2022-12-11', 'newsonair', 'https://www.newsonair.gov.in/budget-session-of-14th-himachal-pradesh-legislative-assembly-begins-today', 'https://himachal.nic.in', note='Official confirmation: News On AIR 16 Feb 2026: Chief Minister Sukhvinder Singh Sukhu. Sworn in on 11 December 2022 in Shimla by Governor Rajendra Vishwanath Arlekar; Mukesh Agnihotri was sworn in as Deputy Chief Minister (Scroll).', as_of='2026-10-27'),
    "others": [
        office('speaker', L('Kuldeep Singh Pathania', 'कुलदीप सिंह पठानिया', 'कुलदीप सिंह पठानिया'), 'INC', '2023-01-05', 'newsonair', 'https://www.newsonair.gov.in/budget-session-of-14th-himachal-pradesh-legislative-assembly-begins-today', 'https://hpvidhansabha.nic.in', note='Official confirmation: News On AIR 16 Feb 2026: Speaker of the Legislative Assembly Kuldeep Singh Pathania. Elected unanimously by voice vote as Speaker of the 14th Vidhan Sabha on 5 January 2023; MLA from Bhattiyat, Chamba (ETV Bharat).', as_of='2026-10-27'),
    ],
}

r["projects"] = [
    proj("atal-tunnel", L("Atal Tunnel, Rohtang", "अटल सुरंग, रोहतांग", "अटल बोगदा, रोहतांग"),
         L("A 9.02-km highway tunnel under the Rohtang Pass on the Manali–Leh road, at about 3,000 m above sea level (south portal 3,060 m, north portal 3,071 m). It cuts the road distance between Manali and Leh by 46 km and saves about 4–5 hours, and keeps the Lahaul valley connected through winter. Dedicated to the nation by the Prime Minister on 3 October 2020; built by the Border Roads Organisation.",
           "मनाली–लेह मार्ग पर रोहतांग दर्रे के नीचे 9.02 किमी लंबी राजमार्ग सुरंग, समुद्र तल से लगभग 3,000 मीटर पर (दक्षिणी द्वार 3,060 मीटर, उत्तरी द्वार 3,071 मीटर)। यह मनाली और लेह के बीच सड़क दूरी 46 किमी घटाती है और लगभग 4–5 घंटे बचाती है, और लाहौल घाटी को सर्दियों में भी जोड़े रखती है। प्रधानमंत्री ने 3 अक्टूबर 2020 को इसे राष्ट्र को समर्पित किया; सीमा सड़क संगठन ने इसे बनाया।",
           "मनाली–लेह मार्गावर रोहतांग खिंडीखालील 9.02 किमी लांबीचा महामार्ग बोगदा, समुद्रसपाटीपासून सुमारे 3,000 मीटर उंचीवर (दक्षिण द्वार 3,060 मीटर, उत्तर द्वार 3,071 मीटर). तो मनाली व लेहदरम्यानचे रस्त्याचे अंतर 46 किमीने कमी करतो व सुमारे 4–5 तास वाचवतो, आणि लाहौल खोरे हिवाळ्यातही जोडलेले ठेवतो. पंतप्रधानांनी 3 ऑक्टोबर 2020 रोजी तो राष्ट्राला समर्पित केला; सीमा रस्ते संघटनेने तो बांधला."),
         "transport", "Border Roads Organisation", None, None, None, None, "3 October 2020", "Completed", "pmindia", ATAL),
    proj("aiims-bilaspur", L("AIIMS Bilaspur", "एम्स बिलासपुर", "एम्स बिलासपूर"),
         L("Himachal Pradesh's All India Institute of Medical Sciences at Kothipura, Bilaspur, built at about ₹1,470 crore with 750 beds including 64 ICU beds. The Prime Minister laid its foundation stone in October 2017 and dedicated it to the nation on 5 October 2022.",
           "कोठीपुरा, बिलासपुर में हिमाचल प्रदेश का अखिल भारतीय आयुर्विज्ञान संस्थान, जो लगभग ₹1,470 करोड़ की लागत से 64 आईसीयू बिस्तरों सहित 750 बिस्तरों के साथ बना। प्रधानमंत्री ने अक्टूबर 2017 में इसकी आधारशिला रखी और 5 अक्टूबर 2022 को इसे राष्ट्र को समर्पित किया।",
           "कोठीपुरा, बिलासपूर येथील हिमाचल प्रदेशचे अखिल भारतीय आयुर्विज्ञान संस्थान, जे सुमारे ₹1,470 कोटी खर्चून 64 आयसीयू खाटांसह 750 खाटांचे उभारले गेले. पंतप्रधानांनी ऑक्टोबर 2017 मध्ये त्याची पायाभरणी केली व 5 ऑक्टोबर 2022 रोजी ते राष्ट्राला समर्पित केले."),
         "health", "Ministry of Health and Family Welfare", 1470, "About ₹1,470 crore (PMIndia).", "2022", "October 2017", "5 October 2022", "Completed", "pmindia", AIIMS),
    proj("kiratpur-nerchowk", L("Kiratpur–Nerchowk four-lane highway (NH-21)", "कीरतपुर–नेरचौक चार-लेन राजमार्ग (एनएच-21)", "कीरतपूर–नेरचौक चौपदरी महामार्ग (एनएच-21)"),
         L("Four-lane section of National Highway 21 from Kiratpur in Punjab to Nerchowk near Mandi, built in two packages at about ₹3,400 crore, shortening the road to Mandi, Kullu and Manali. Inaugurated by the Prime Minister on 11 March 2024 among 112 national highway projects.",
           "पंजाब के कीरतपुर से मंडी के पास नेरचौक तक राष्ट्रीय राजमार्ग 21 का चार-लेन खंड, जो लगभग ₹3,400 करोड़ की लागत से दो पैकेज में बना और मंडी, कुल्लू व मनाली का रास्ता छोटा करता है। प्रधानमंत्री ने 11 मार्च 2024 को 112 राष्ट्रीय राजमार्ग परियोजनाओं के साथ इसका उद्घाटन किया।",
           "पंजाबमधील कीरतपूरपासून मंडीजवळील नेरचौकपर्यंत राष्ट्रीय महामार्ग 21 चा चौपदरी टप्पा, जो सुमारे ₹3,400 कोटी खर्चून दोन पॅकेजमध्ये बांधला गेला आणि मंडी, कुल्लू व मनालीचा रस्ता कमी करतो. पंतप्रधानांनी 11 मार्च 2024 रोजी 112 राष्ट्रीय महामार्ग प्रकल्पांसोबत त्याचे उद्घाटन केले."),
         "transport", "National Highways Authority of India", 3400, "About ₹3,400 crore for two packages (PMIndia).", "2024", None, "11 March 2024", "Completed", "pmindia", NH),
]

GI_NAMES = {
 "Kangra Tea": ("कांगड़ा चाय", "कांगडा चहा"),
 "Himachali Kala Zeera": ("हिमाचली काला ज़ीरा", "हिमाचली काळे जिरे"),
 "Kullu Shawl": ("कुल्लू शॉल", "कुल्लू शाल"),
 "Chamba Rumal": ("चंबा रूमाल", "चंबा रुमाल"),
 "Kinnauri Shawl": ("किन्नौरी शॉल", "किन्नौरी शाल"),
 "Kangra Paintings": ("कांगड़ा चित्रकला", "कांगडा चित्रकला"),
 "Kullu Shawl (Logo)": ("कुल्लू शॉल (लोगो)", "कुल्लू शाल (लोगो)"),
 "Chamba Chappal": ("चंबा चप्पल", "चंबा चप्पल"),
 "Lahauli Knitted Socks & Gloves": ("लाहौली बुने हुए मोज़े और दस्ताने", "लाहौली विणलेले मोजे व हातमोजे"),
 "Himachali Chulli Oil": ("हिमाचली चुल्ली तेल", "हिमाचली चुल्ली तेल"),
 "Basmati": ("बासमती", "बासमती"),
}
SHARED = {"PB,HR,HP,DL,UK,UP,JK": ["Punjab", "Haryana", "Delhi", "Uttarakhand", "Uttar Pradesh", "Jammu & Kashmir"]}
r["giProducts"] = gi_list("gi_hp.tsv", GI_NAMES, SHARED, {"Kullu Shawl", "Kinnauri Shawl", "Kullu Shawl (Logo)", "Chamba Rumal", "Lahauli Knitted Socks & Gloves"})
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-HP.json", r)
print("hp core ok", len(r["giProducts"]), "GIs")
