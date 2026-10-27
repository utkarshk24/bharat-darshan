"""Andhra Pradesh — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-16.

Census 2011 figures are for the residual State (13 districts after the 2014 bifurcation, including the
Polavaram mandals), as recast by the AP School Education department. Tables that still show undivided
Andhra Pradesh are not used for State-level figures."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

CSE = "https://cse.ap.gov.in/MISdownload/MIS_REPORT_NOTIFICATION/Educational%20Statistics%202017-18.pdf"
ANI_AP = "https://aninews.in/news/national/politics/andhra-assembly-budget-session-begins-with-governors-address-amid-protest-by-ysrcp-leaders20260211111711/"
NOA_CM = "https://newsonair.gov.in/andhra-pradesh-nara-chandrababu-naidu-to-take-oath-as-cm-for-fourth-term-today"
SPK = "https://thesouthfirst.com/andhrapradesh/tdps-ayyannapatrudu-unanimously-elected-speaker-of-andhra-assembly/"
BHOG = "https://www.pmindia.gov.in/?p=16891150"
AMR = "https://www.newsonair.gov.in/pm-modi-arrives-in-vijayawada-to-launch-amaravati-development-projects-worth-%E2%82%B958000-crore"
POL = "https://eparlib.sansad.in/bitstream/123456789/2978868/1/AU1723_DYjh7U.pdf"

ap = research("mospi_ap.json")
r = read("regions/IN-AP.json")
m = r["metrics"]
RES_NOTE = "Census 2011 recast for the residual State of Andhra Pradesh (13 districts, including the Polavaram mandals transferred in 2014), from the State's 'Educational Statistics 2017-18'."
m["population2011"] = dp(49577103, "persons", "2011", "census", "ap-cse", CSE,
    note=RES_NOTE + " Males 2,48,30,513; females 2,47,46,590.")
m["area"] = dp(162968, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(304, "persons per km²", "2011", "census", "ap-cse", CSE,
    note="Calculated: Census 2011 population 4,95,77,103 ÷ area 1,62,968 km² = 304.2; the State publication also gives 304.")
m["sexRatio2011"] = dp(997, "females per 1000 males", "2011", "census", "ap-cse", CSE, note=RES_NOTE)
m["childSexRatio2011"] = dp(None, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", None,
    note="Not shown: no official figure for the residual State was found. The PIB table of 2014 gives 939 for undivided Andhra Pradesh, which included Telangana.")
m["literacyRate2011"] = dp(67.35, "%", "2011", "census", "ap-cse", CSE, note=RES_NOTE + " Males 74.77%, females 59.96%.")
m["urbanisation2011"] = dp(29.47, "%", "2011", "census", "ap-cse", CSE,
    note="Calculated: urban population 1,46,10,410 ÷ total 4,95,77,103 (residual State, Census 2011).")
m["gsdpCurrent"] = dp(ap["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25: ₹{inr(ap['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(ap["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(ap['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(18.46, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 30,084.96 km² ÷ geographical area 1,62,968 km².")

r["officialPortal"] = "https://www.ap.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Blackbuck", "काला हिरण", "काळवीट", "Antilope cervicapra"),
    "bird": sym("Rose-ringed parakeet", "तोता (गुलाबी कंठी)", "पोपट (गुलाबी कंठी)", "Psittacula krameri"),
    "flower": sym("Jasmine", "चमेली", "मोगरा", "Jasminum officinale"),
    "tree": sym("Neem", "नीम", "कडुलिंब", "Azadirachta indica"),
}

r["government"] = {
    "headOfState": office('governor', L('S. Abdul Nazeer', 'एस. अब्दुल नज़ीर', 'एस. अब्दुल नझीर'), None, '2023-02-24', 'newsonair', 'https://www.newsonair.gov.in/andhra-pradesh-govt-officially-renamed-raj-bhavan-as-lok-bhavan/', 'https://igod.gov.in', note='Official confirmation: News On AIR 3 Dec 2025: Raj Bhavan renamed Lok Bhavan following approval of Governor S. Abdul Nazeer. Former Supreme Court judge. Addressed the opening of the Assembly Budget Session as Governor on 11 Feb 2026 (ANI). Confirm the start date on the Lok Bhavan, Andhra Pradesh website.', as_of='2026-10-27'),
    "headOfGovernment": office("chief-minister", L("N. Chandrababu Naidu", "एन. चंद्रबाबू नायडू", "एन. चंद्राबाबू नायडू"), "TDP", "2024-06-12",
                               "newsonair", NOA_CM, "https://www.ap.gov.in",
                               note="Sworn in on 12 June 2024 for his fourth term as Chief Minister (News On AIR). Named as Chief Minister in News On AIR reports of 2026."),
    "others": [
        office('deputy-chief-minister', L('Pawan Kalyan', 'पवन कल्याण', 'पवन कल्याण'), 'JSP', '2024-06-12', 'newsonair', 'https://www.newsonair.gov.in/portfolios-allotted-to-newly-sworn-in-ministers-in-andhra-pradesh', 'https://www.ap.gov.in', note="Official confirmation: News On AIR 14 Jun 2024: Pawan Kalyan made Deputy Chief Minister. Sworn in with the Council of Ministers in June 2024; named as Deputy Chief Minister in ANI's report of 11 Feb 2026.", as_of='2026-10-27'),
        office("speaker", L("C. Ayyanna Patrudu", "सी. अय्यन्ना पात्रुडु", "सी. अय्यन्ना पात्रुडू"), "TDP", "2024-06-22", "thesouthfirst", SPK, "https://www.aplegislature.org",
               conf="Third-party verified", note="Elected unopposed in June 2024 (The South First). Confirm the date on the Legislature website."),
    ],
}

r["projects"] = [
    proj("bhogapuram-airport", L("Alluri Sitarama Raju International Airport, Bhogapuram", "अल्लूरी सीताराम राजू अंतरराष्ट्रीय हवाई अड्डा, भोगापुरम", "अल्लुरी सीताराम राजू आंतरराष्ट्रीय विमानतळ, भोगापुरम"),
         L("A new greenfield airport for Visakhapatnam in Vizianagaram district, built in public–private partnership mode with a capacity of 6 million passengers a year. The Prime Minister's Office announced its inauguration by the Prime Minister on 1 August 2026.",
           "विजयनगरम ज़िले में विशाखापत्तनम के लिए नया ग्रीनफ़ील्ड हवाई अड्डा, जो सार्वजनिक–निजी भागीदारी से बना है और जिसकी क्षमता हर साल 60 लाख यात्रियों की है। प्रधानमंत्री कार्यालय ने 1 अगस्त 2026 को प्रधानमंत्री द्वारा इसके उद्घाटन की घोषणा की।",
           "विजयनगरम जिल्ह्यात विशाखापट्टणमसाठी नवे ग्रीनफिल्ड विमानतळ, सार्वजनिक–खासगी भागीदारीतून उभारलेले, वार्षिक 60 लाख प्रवासी क्षमतेचे. पंतप्रधान कार्यालयाने 1 ऑगस्ट 2026 रोजी पंतप्रधानांच्या हस्ते त्याचे उद्घाटन होणार असल्याचे जाहीर केले."),
         "transport", "GMR Visakhapatnam International Airport Ltd (PPP)", 5640, "Over ₹5,640 crore (PMO release).", "2026", None, "1 August 2026", "Completed", "pmindia", BHOG,
         challenges=L("Confirm the start of commercial flights with the Airports Authority of India.", "वाणिज्यिक उड़ानों की शुरुआत भारतीय विमानपत्तन प्राधिकरण से पुष्टि करें।", "व्यावसायिक उड्डाणांच्या सुरुवातीची भारतीय विमानतळ प्राधिकरणाकडून खात्री करा.")),
    proj("amaravati-capital", L("Amaravati capital city works", "अमरावती राजधानी नगर कार्य", "अमरावती राजधानी शहर कामे"),
         L("Restart of construction of the State capital at Amaravati, including core capital facilities. The Prime Minister launched works there on 2 May 2025 as part of projects worth over ₹58,000 crore. In 2026 Parliament passed the Andhra Pradesh Reorganisation (Amendment) Bill naming Amaravati as the capital.",
           "अमरावती में राज्य की राजधानी के निर्माण को फिर शुरू करना, जिसमें मुख्य राजधानी सुविधाएँ शामिल हैं। प्रधानमंत्री ने 2 मई 2025 को ₹58,000 करोड़ से अधिक की परियोजनाओं के हिस्से के रूप में वहाँ काम शुरू कराया। 2026 में संसद ने अमरावती को राजधानी घोषित करने वाला आंध्र प्रदेश पुनर्गठन (संशोधन) विधेयक पारित किया।",
           "अमरावती येथे राज्याच्या राजधानीचे बांधकाम पुन्हा सुरू करणे, मुख्य राजधानी सुविधांसह. पंतप्रधानांनी 2 मे 2025 रोजी ₹58,000 कोटींहून अधिक प्रकल्पांचा भाग म्हणून तिथे कामांना सुरुवात केली. 2026 मध्ये संसदेने अमरावतीला राजधानी ठरवणारे आंध्र प्रदेश पुनर्रचना (सुधारणा) विधेयक मंजूर केले."),
         "urban", "Government of Andhra Pradesh / APCRDA", None, None, None, "May 2025", None, "Under Construction", "newsonair", AMR),
    proj("polavaram", L("Polavaram Irrigation Project (Phase 1)", "पोलावरम सिंचाई परियोजना (चरण 1)", "पोलावरम सिंचन प्रकल्प (टप्पा 1)"),
         L("A multipurpose dam on the Godavari, declared a national project in the Andhra Pradesh Reorganisation Act, 2014. Phase 1 stores water up to 41.15 m; in August 2024 the Union Government told the Lok Sabha that it was scheduled for completion by March 2026.",
           "गोदावरी पर बहुउद्देशीय बाँध, जिसे आंध्र प्रदेश पुनर्गठन अधिनियम, 2014 में राष्ट्रीय परियोजना घोषित किया गया। चरण 1 में 41.15 मीटर तक जल भंडारण है; अगस्त 2024 में केंद्र सरकार ने लोकसभा को बताया कि इसे मार्च 2026 तक पूरा करने का कार्यक्रम है।",
           "गोदावरीवरील बहुउद्देशीय धरण, आंध्र प्रदेश पुनर्रचना अधिनियम, 2014 मध्ये राष्ट्रीय प्रकल्प म्हणून घोषित. टप्पा 1 मध्ये 41.15 मीटरपर्यंत पाणीसाठा; ऑगस्ट 2024 मध्ये केंद्र सरकारने लोकसभेत सांगितले की तो मार्च 2026 पर्यंत पूर्ण करण्याचे वेळापत्रक आहे."),
         "water", "Polavaram Project Authority / Water Resources Department, Andhra Pradesh", None, None, None, None, "March 2026 (scheduled, as of Aug 2024)", "Under Construction", "sansad", POL,
         challenges=L("The latest official completion status after March 2026 still needs to be linked.", "मार्च 2026 के बाद की नवीनतम आधिकारिक स्थिति अभी जोड़नी है।", "मार्च 2026 नंतरची नवीनतम अधिकृत स्थिती अजून जोडायची आहे.")),
]

GI_NAMES = {
 "Guntur Sannam Chilli": ("गुंटूर सन्नम मिर्च", "गुंटूर सन्नम मिरची"),
 "Tirupathi Laddu": ("तिरुपति लड्डू", "तिरुपती लाडू"),
 "Bandar Laddu": ("बंदर लड्डू", "बंदर लाडू"),
 "Atreyapuram Pootharekulu": ("आत्रेयपुरम पूतरेकुलु", "आत्रेयपुरम पूतरेकुलू"),
 "Srikalahasthi Kalamkari": ("श्रीकालहस्ती कलमकारी", "श्रीकालहस्ती कलमकारी"),
 "Kondapalli Bommalu": ("कोंडापल्ली बोम्मलु (खिलौने)", "कोंडापल्ली बोम्मलू (खेळणी)"),
 "Budithi Bell & Brass Metal Craft": ("बुदिथी घंटा और पीतल धातु शिल्प", "बुदिथी घंटा व पितळ धातुकला"),
 "Machilipatnam Kalamkari": ("मछलीपट्टनम कलमकारी", "मछलीपट्टणम कलमकारी"),
 "Andhra Pradesh Leather Puppetry": ("आंध्र प्रदेश चमड़ा कठपुतली", "आंध्र प्रदेश चामडी कठपुतळी"),
 "Uppada Jamdani Sarees": ("उप्पाडा जामदानी साड़ियाँ", "उप्पाडा जामदानी साड्या"),
 "Venkatagiri Sarees": ("वेंकटगिरि साड़ियाँ", "वेंकटगिरी साड्या"),
 "Mangalagiri Sarees And Fabrics": ("मंगलगिरि साड़ियाँ और वस्त्र", "मंगळगिरी साड्या व वस्त्रे"),
 "Bobbili Veena": ("बोब्बिली वीणा", "बोब्बिली वीणा"),
 "Dharmavaram Handloom Pattu Sarees And Paavadas": ("धर्मावरम हथकरघा पट्टू साड़ियाँ और पावडा", "धर्मावरम हातमाग पट्टू साड्या व पावडा"),
 "Durgi Stone Carvings": ("दुर्गी पत्थर नक्काशी", "दुर्गी दगडी कोरीवकाम"),
 "Etikoppaka Toys": ("एटिकोप्पाका खिलौने", "एटिकोप्पाका खेळणी"),
 "Udayagiri Wooden Cutlery": ("उदयगिरि लकड़ी की कटलरी", "उदयगिरी लाकडी कटलरी"),
 "Allagadda Stone Carving": ("आल्लगड्डा पत्थर नक्काशी", "आल्लगड्डा दगडी कोरीवकाम"),
 "Narasapur Crochet Lace Products": ("नरसापुर क्रोशिया लेस उत्पाद", "नरसापूर क्रोशा लेस उत्पादने"),
 "Ponduru Khadi": ("पोंदुरु खादी", "पोंदुरू खादी"),
 "Araku Valley Arabica Coffee": ("अराकू घाटी अरेबिका कॉफ़ी", "अराकू खोरे अरेबिका कॉफी"),
 "Banaganapalle Mangoes": ("बंगनपल्ले आम", "बंगनपल्ले आंबे"),
}
TEXTILE = {"Srikalahasthi Kalamkari", "Machilipatnam Kalamkari", "Uppada Jamdani Sarees", "Venkatagiri Sarees", "Mangalagiri Sarees And Fabrics",
           "Dharmavaram Handloom Pattu Sarees And Paavadas", "Narasapur Crochet Lace Products", "Ponduru Khadi"}
r["giProducts"] = gi_list("gi_ap.tsv", GI_NAMES, {"AP,OR": ["Odisha"], "AP,TG": ["Telangana"]}, TEXTILE)
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-AP.json", r)
print("ap core ok", len(r["giProducts"]), "GIs")
