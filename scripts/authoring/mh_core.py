import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from bd import *

SDB = "https://mahasdb.maharashtra.gov.in/maagCmpIndia.do"
SW = "https://socialwelfare.maharashtra.gov.in/en/general-and-scheduled-caste-population-census-2011/"
PIB_CSR = "https://www.pib.gov.in/newsite/printrelease.aspx?relid=103437&reg=48&lang=2"
LS_FOREST = "https://eparlib.sansad.in/bitstream/123456789/3021702/1/AU1550_C0eysl.pdf"
MOSPI = "https://mospi.gov.in"
GI_PDF = "https://ipindia.gov.in/frontend/pdf/gi/registered/State_wise_Registered_GI_of_India.pdf"

r = read("regions/IN-MH.json")
r["officialPortal"] = "https://www.maharashtra.gov.in"
m = r["metrics"]
m["population2011"] = dp(112374333, "persons", "2011", "census", "census", SW,
    note="Census 2011 state total as published by the Social Welfare Department, Government of Maharashtra; matches the State Data Bank (1,12,374 thousand).")
m["area"] = dp(307713, "km²", "2023", "calendar", "fsi", LS_FOREST,
    note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026). Census 2011 rounds this to 3.08 lakh km².")
m["density2011"] = dp(365, "persons per km²", "2011", "census", "census", SW,
    note="Computed: Census 2011 population ÷ 3,07,713 km² = 365.2. Matches the Census-published density of 365.")
m["sexRatio2011"] = dp(929, "females per 1000 males", "2011", "census", "census", SDB, note="Via Maharashtra State Data Bank.")
m["childSexRatio2011"] = dp(894, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR,
    note="PIB release of 11 Feb 2014 (RGI data). Was 913 in 2001.")
m["literacyRate2011"] = dp(82.34, "%", "2011", "census", "census", SDB,
    note="Population aged 7+. The State Data Bank shows 82.3 (rounded).")
m["urbanisation2011"] = dp(45.2, "%", "2011", "census", "census", SDB, note="Urban population 5,08,18 thousand of 11,23,74 thousand (State Data Bank).")
m["gsdpCurrent"] = dp(5100597, "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional",
    base={"type": "current"}, note="MoSPI state-wise GSDP, base 2011-12, current series. Latest year — treat as an early estimate. FY2024-25: ₹46,22,138 crore.")
m["perCapitaNsdpCurrent"] = dp(347903, "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional",
    base={"type": "current"}, note="MoSPI, base 2011-12. FY2024-25: ₹3,17,801.")
m["forestCoverPct"] = dp(16.53, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 50,858.53 km² ÷ geographical area 3,07,713 km².")
r["timeSeries"] = {}

r["symbols"] = {
    "animal": {"name": L("Indian giant squirrel (Shekru)", "शेकरू (भारतीय विशाल गिलहरी)", "शेकरू"), "scientificName": "Ratufa indica",
               "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"},
    "bird": {"name": L("Yellow-footed green pigeon (Hariyal)", "हरियल", "हरियाल"), "scientificName": "Treron phoenicopterus",
             "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"},
    "flower": {"name": L("Pride of India (Jarul)", "जारुल", "ताम्हण"), "scientificName": "Lagerstroemia speciosa",
               "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"},
    "tree": {"name": L("Mango", "आम", "आंबा"), "scientificName": "Mangifera indica",
             "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"},
    "butterfly": {"name": L("Blue Mormon", "ब्लू मॉर्मन", "ब्लू मॉरमॉन"), "scientificName": "Papilio polymnestor",
                  "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"},
    "fish": {"name": L("Silver pomfret", "सिल्वर पॉम्फ्रेट (पापलेट)", "पापलेट (सिल्व्हर पॉम्फ्रेट)"), "scientificName": "Pampus argenteus",
             "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"},
}

SDMA = "https://sdma.maharashtra.gov.in/en/whos-who/"
def office(role, name, party, since, src, url, verify, note=None):
    o = {"role": role, "name": name, "party": party, "since": since, "asOf": TODAY, "sourceId": src, "url": url,
         "verifyUrl": verify, "revisionStatus": "final", "confidence": "Official"}
    if note: o["note"] = note
    return o

r["government"] = {
    "headOfState": office("governor", L("Jishnu Dev Varma", "जिष्णु देव वर्मा", "जिष्णु देव वर्मा"), None, "2026-03-10",
                          "mh-lokbhavan", "https://lokbhavan.maharashtra.gov.in/", "https://lokbhavan.maharashtra.gov.in/",
                          note="Sworn in on 10 March 2026 as Maharashtra's 22nd Governor (Lok Bhavan; News On AIR)."),
    "headOfGovernment": office("chief-minister", L("Devendra Fadnavis", "देवेंद्र फडणवीस", "देवेंद्र फडणवीस"), "BJP", "2024-12-05",
                               "mh-gov", SDMA, SDMA, note="Took oath on 5 December 2024 (News On AIR). Listed on Government of Maharashtra department pages."),
    "others": [
        office("deputy-chief-minister", L("Eknath Shinde", "एकनाथ शिंदे", "एकनाथ शिंदे"), "Shiv Sena", "2024-12-05", "mh-gov", SDMA, SDMA),
        office("deputy-chief-minister", L("Sunetra Pawar", "सुनेत्रा पवार", "सुनेत्रा पवार"), "NCP", "2026-01-31", "mh-gov", SDMA, SDMA,
               note="Sworn in on 31 January 2026 (date per news reports); first woman Deputy CM of Maharashtra."),
        {"role": "speaker", "name": None, "party": None, "since": None, "asOf": None, "sourceId": "mh-gov", "url": None,
         "verifyUrl": "https://mls.org.in", "revisionStatus": "TODO", "confidence": "Official",
         "note": "Verify on the Maharashtra Legislature website and record asOf."},
        {"role": "leader-of-opposition", "name": None, "party": None, "since": None, "asOf": None, "sourceId": "mh-gov", "url": None,
         "verifyUrl": "https://mls.org.in", "revisionStatus": "TODO", "confidence": "Official",
         "note": "News reports in 2025–26 said no Leader of Opposition had been recognised in either House. Confirm with the Legislature Secretariat."},
    ],
}

def proj(id, name, objective, sector, agency, cost, costnote, costperiod, start, completion, status, src, url, challenges=None):
    p = {"id": id, "name": name, "objective": objective, "sector": sector, "agency": agency,
         "start": start, "completion": completion, "status": status, "asOf": TODAY, "sourceId": src, "url": url, "confidence": "Official"}
    if cost is not None:
        p["cost"] = dp(cost, "₹ crore", costperiod, "calendar", src, url, note=costnote)
    if challenges: p["challenges"] = challenges
    return p

r["projects"] = [
    proj("atal-setu", L("Atal Bihari Vajpayee Sewri–Nhava Sheva Atal Setu (Mumbai Trans Harbour Link)", "अटल बिहारी वाजपेयी शिवडी–न्हावा शेवा अटल सेतु (मुंबई ट्रांस हार्बर लिंक)", "अटल बिहारी वाजपेयी शिवडी–न्हावा शेवा अटल सेतू (मुंबई ट्रान्स हार्बर लिंक)"),
         L("A 21.8 km six-lane bridge, about 16.5 km of it over the sea, linking Sewri in Mumbai with Nhava Sheva in Navi Mumbai.",
           "लगभग 21.8 किमी लंबा छह लेन का पुल, जिसका करीब 16.5 किमी हिस्सा समुद्र के ऊपर है; यह मुंबई के शिवडी को नवी मुंबई के न्हावा शेवा से जोड़ता है।",
           "सुमारे 21.8 किमी लांबीचा सहापदरी पूल, ज्यापैकी सुमारे 16.5 किमी भाग समुद्रावर आहे; तो मुंबईतील शिवडीला नवी मुंबईतील न्हावा शेव्याशी जोडतो."),
         "transport", "MMRDA", 17840, "more than ₹17,840 crore", "2024", None, "January 2024", "Completed",
         "pib", "https://www.pib.gov.in/PressReleasePage.aspx?PRID=1995650"),
    proj("samruddhi", L("Hindu Hrudaysamrat Balasaheb Thackeray Maharashtra Samruddhi Mahamarg (Mumbai–Nagpur Expressway)", "हिंदू हृदयसम्राट बालासाहेब ठाकरे महाराष्ट्र समृद्धि महामार्ग (मुंबई–नागपुर एक्सप्रेसवे)", "हिंदुहृदयसम्राट बाळासाहेब ठाकरे महाराष्ट्र समृद्धी महामार्ग (मुंबई–नागपूर द्रुतगती मार्ग)"),
         L("A 701 km access-controlled expressway between Nagpur and the Mumbai region. The final 75 km stretch, Igatpuri to Amane, was inaugurated on 5 June 2025.",
           "नागपुर और मुंबई क्षेत्र के बीच 701 किमी लंबा प्रवेश-नियंत्रित एक्सप्रेसवे। अंतिम 75 किमी का हिस्सा, इगतपुरी से आमणे, 5 जून 2025 को शुरू हुआ।",
           "नागपूर आणि मुंबई परिसर यांच्यातील 701 किमी लांबीचा प्रवेश-नियंत्रित द्रुतगती मार्ग. इगतपुरी ते आमणे हा शेवटचा 75 किमीचा टप्पा 5 जून 2025 रोजी खुला झाला."),
         "transport", "MSRDC", None, None, None, None, "June 2025", "Completed",
         "newsonair", "https://www.newsonair.gov.in/maharashtra-cm-fadnavis-to-inaugurate-final-75-km-phase-of-samruddhi-highway/"),
    proj("nmia", L("Navi Mumbai International Airport (Phase 1)", "नवी मुंबई अंतरराष्ट्रीय हवाई अड्डा (चरण 1)", "नवी मुंबई आंतरराष्ट्रीय विमानतळ (टप्पा 1)"),
         L("A second airport for the Mumbai region on 1,160 hectares, planned for an eventual 90 million passengers a year. Inaugurated on 8 October 2025.",
           "मुंबई क्षेत्र का दूसरा हवाई अड्डा, 1,160 हेक्टेयर में; अंततः सालाना 9 करोड़ यात्रियों की क्षमता की योजना। 8 अक्टूबर 2025 को उद्घाटन हुआ।",
           "मुंबई परिसरासाठी दुसरा विमानतळ, 1,160 हेक्टरवर; अंतिम टप्प्यात वर्षाला 9 कोटी प्रवाशांची क्षमता नियोजित. 8 ऑक्टोबर 2025 रोजी उद्घाटन झाले."),
         "transport", None, 19650, "about ₹19,650 crore for Phase 1", "2025", None, "October 2025", "Completed",
         "pib", "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2176402"),
    proj("metro-3", L("Mumbai Metro Line 3 (Aqua Line)", "मुंबई मेट्रो लाइन 3 (एक्वा लाइन)", "मुंबई मेट्रो मार्गिका 3 (ॲक्वा लाइन)"),
         L("A 33.5 km line with 27 stations from Cuffe Parade to Aarey JVLR. The full line was dedicated on 8 October 2025.",
           "कफ़ परेड से आरे जेवीएलआर तक 33.5 किमी लंबी लाइन, 27 स्टेशनों के साथ। पूरी लाइन 8 अक्टूबर 2025 को राष्ट्र को समर्पित की गई।",
           "कफ परेड ते आरे जेव्हीएलआर अशी 33.5 किमीची मार्गिका, 27 स्थानकांसह. संपूर्ण मार्गिका 8 ऑक्टोबर 2025 रोजी राष्ट्राला समर्पित झाली."),
         "transport", "MMRCL", 37270, "more than ₹37,270 crore for the full line", "2025", None, "October 2025", "Completed",
         "pib", "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2176402"),
    proj("mahsr", L("Mumbai–Ahmedabad High-Speed Rail (Bullet Train)", "मुंबई–अहमदाबाद हाई-स्पीड रेल (बुलेट ट्रेन)", "मुंबई–अहमदाबाद अतिजलद रेल्वे (बुलेट ट्रेन)"),
         L("A 508 km high-speed line. The Maharashtra section includes a 21 km tunnel, about 7 km of it under Thane Creek. The first service is targeted for August 2027.",
           "508 किमी लंबी हाई-स्पीड रेल लाइन। महाराष्ट्र वाले हिस्से में 21 किमी लंबी सुरंग है, जिसका लगभग 7 किमी भाग ठाणे खाड़ी के नीचे है। पहली सेवा का लक्ष्य अगस्त 2027 है।",
           "508 किमी लांबीचा अतिजलद रेल्वेमार्ग. महाराष्ट्रातील भागात 21 किमीचा बोगदा असून त्यापैकी सुमारे 7 किमी ठाणे खाडीखालून जातो. पहिली सेवा ऑगस्ट 2027 पर्यंत सुरू करण्याचे उद्दिष्ट आहे."),
         "transport", "NHSRCL", None, None, None, None, "First service targeted August 2027", "Under Construction",
         "pib", "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2272190&lang=1&reg=48",
         challenges=L("Land acquisition delayed the Maharashtra section in earlier years.", "पहले के वर्षों में भूमि अधिग्रहण के कारण महाराष्ट्र खंड में देरी हुई।", "पूर्वीच्या वर्षांत भूसंपादनामुळे महाराष्ट्रातील टप्प्याला विलंब झाला.")),
    proj("vadhavan", L("Vadhavan Port", "वाढवण बंदरगाह", "वाढवण बंदर"),
         L("A deep-draft port being built at Vadhavan in Palghar district. PIB cites an investment of about ₹76,000 crore.",
           "पालघर ज़िले के वाढवण में बन रहा गहरे पानी का बंदरगाह। पीआईबी के अनुसार निवेश लगभग ₹76,000 करोड़ है।",
           "पालघर जिल्ह्यातील वाढवण येथे उभारले जात असलेले खोल पाण्याचे बंदर. पीआयबीनुसार गुंतवणूक सुमारे ₹76,000 कोटी आहे."),
         "ports", None, 76000, "about ₹76,000 crore", "2025", None, None, "Under Construction",
         "pib", "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2176402",
         challenges=L("Fishing communities and environmental groups have raised concerns about the project's coastal impact.", "मछुआरा समुदायों और पर्यावरण समूहों ने तटीय प्रभाव को लेकर चिंताएँ जताई हैं।", "मच्छीमार समुदाय आणि पर्यावरण गटांनी किनारी परिणामांबद्दल चिंता व्यक्त केली आहे.")),
]

GI_NAMES = {
 "Alphonso": ("अल्फांसो आम", "हापूस (आल्फान्सो) आंबा"),
 "Mahabaleshwar Strawberry": ("महाबलेश्वर स्ट्रॉबेरी", "महाबळेश्वर स्ट्रॉबेरी"),
 "Nashik Grapes": ("नासिक के अंगूर", "नाशिकची द्राक्षे"),
 "Ajara Ghansal Rice": ("आजरा घनसाळ चावल", "आजरा घनसाळ तांदूळ"),
 "Waigaon Turmeric": ("वायगांव हल्दी", "वायगाव हळद"),
 "Mangalwedha Jowar": ("मंगलवेढा ज्वार", "मंगळवेढा ज्वारी"),
 "Bhiwapur Chilli": ("भिवापुर मिर्च", "भिवापूर मिरची"),
 "Sindhudurg & Ratnagiri Kokum": ("सिंधुदुर्ग और रत्नागिरी कोकम", "सिंधुदुर्ग व रत्नागिरी कोकम"),
 "Waghya Ghevada": ("वाघ्या घेवडा", "वाघ्या घेवडा"),
 "Navapur Tur Dal": ("नवापुर तुअर दाल", "नवापूर तूरडाळ"),
 "Ambemohar Rice": ("आंबेमोहर चावल", "आंबेमोहर तांदूळ"),
 "Vengurla Cashew": ("वेंगुर्ला काजू", "वेंगुर्ला काजू"),
 "Sangli Raisins": ("सांगली किशमिश", "सांगलीचे बेदाणे"),
 "Lasalgaon Onion": ("लासलगांव प्याज़", "लासलगाव कांदा"),
 "Dahanu Gholvad Chikoo": ("डहाणू घोलवड चीकू", "डहाणू घोलवड चिकू"),
 "Beed Custard Apple": ("बीड सीताफल", "बीड सीताफळ"),
 "Jalna Sweet Orange": ("जालना मौसंबी", "जालना मोसंबी"),
 "Sangli Turmeric": ("सांगली हल्दी", "सांगली हळद"),
 "Jalgaon Banana": ("जलगांव केला", "जळगाव केळी"),
 "Marathwada Kesar Mango": ("मराठवाड़ा केसर आम", "मराठवाडा केशर आंबा"),
 "Purandar Fig": ("पुरंदर अंजीर", "पुरंदर अंजीर"),
 "Jalgaon Bharit Brinjal": ("जलगांव भरित बैंगन", "जळगाव भरीत वांगी"),
 "Solapur Pomegranate": ("सोलापुर अनार", "सोलापूर डाळिंब"),
 "Alibag White Onion": ("अलीबाग सफ़ेद प्याज़", "अलिबागचा पांढरा कांदा"),
 "Bhandara Chinoor Rice": ("भंडारा चिनूर चावल", "भंडारा चिनूर तांदूळ"),
 "Vasmat Haldi (Turmeric)": ("वसमत हल्दी", "वसमत हळद"),
 "Nandurbar Amchur": ("नंदुरबार अमचूर", "नंदुरबार आमचूर"),
 "Nandurbar Mirchi": ("नंदुरबार मिर्च", "नंदुरबार मिरची"),
 "Panchincholi Tamarind": ("पानचिंचोली इमली", "पानचिंचोली चिंच"),
 "Borsuri Tur Dal": ("बोरसुरी तुअर दाल", "बोरसुरी तूरडाळ"),
 "Kasti Coriander": ("कास्ती धनिया", "कास्ती धणे"),
 "Badlapur Jamun": ("बदलापुर जामुन", "बदलापूर जांभूळ"),
 "Bahadoli Jamun": ("बहाडोली जामुन", "बहाडोली जांभूळ"),
 "Dagdi Jowar of Jalna": ("जालना की दगडी ज्वार", "जालन्याची दगडी ज्वारी"),
 "Akola Kagzi Lime": ("अकोला कागज़ी नींबू", "अकोला कागदी लिंबू"),
 "Amravati Pippal": ("अमरावती पिप्पली", "अमरावती पिंपळी"),
 "Amravati Chana": ("अमरावती चना", "अमरावती हरभरा"),
 "Kolhapur Jaggery": ("कोल्हापुर गुड़", "कोल्हापुरी गूळ"),
 "Kunthalgiri Khawa": ("कुंथलगिरी खोया", "कुंथलगिरी खवा"),
 "Solapur Chaddar": ("सोलापुरी चादर", "सोलापुरी चादर"),
 "Solapur Terry Towel": ("सोलापुरी टेरी तौलिया", "सोलापुरी टेरी टॉवेल"),
 "Puneri Pagadi": ("पुणेरी पगड़ी", "पुणेरी पगडी"),
 "Paithani Sarees and Fabrics": ("पैठणी साड़ियाँ और वस्त्र", "पैठणी साड्या व वस्त्रे"),
 "Sawantwadi Ganjifa Cards": ("सावंतवाड़ी गंजीफ़ा पत्ते", "सावंतवाडी गंजिफा"),
 "Karvath Kati Sarees and Fabrics": ("करवत काठी साड़ियाँ और वस्त्र", "करवत काठी साड्या व वस्त्रे"),
 "Miraj Tanpura": ("मिरज तानपूरा", "मिरज तानपुरा"),
 "Hupari Silver Craft": ("हुपरी चाँदी शिल्प", "हुपरी चांदीकाम"),
 "Miraj Sitar": ("मिरज सितार", "मिरज सतार"),
 "Sawantwadi Wooden Craft": ("सावंतवाड़ी काष्ठ शिल्प", "सावंतवाडी लाकडी हस्तकला"),
 "Pen Ganesh Idol": ("पेण गणेश मूर्तियाँ", "पेणच्या गणेशमूर्ती"),
 "Kavdi Maal of Tuljapur": ("तुलजापुर की कवड़ी माला", "तुळजापूरची कवडी माळ"),
 "Nashik Valley Wine": ("नासिक वैली वाइन", "नाशिक व्हॅली वाइन"),
 "Kolhapuri Chappal": ("कोल्हापुरी चप्पल", "कोल्हापुरी चप्पल"),
 "Nagpur Orange": ("नागपुर संतरा", "नागपुरी संत्री"),
 "Warli Painting": ("वारली चित्रकला", "वारली चित्रकला"),
}
TEXTILE = {"Paithani Sarees and Fabrics", "Karvath Kati Sarees and Fabrics", "Solapur Chaddar", "Solapur Terry Towel"}
SHARED = {"KA,MH": ["Karnataka"], "MH,MP": ["Madhya Pradesh"], "MH,GJ,DNH,DD": ["Gujarat", "Dadra & Nagar Haveli and Daman & Diu"]}
import re
gis = []
for line in open(__import__("os").path.join(__import__("os").path.dirname(__file__), "research") + "/gi_mh.tsv"):
    app, name, cat, date, states = line.rstrip("\n").split("\t")
    hi, mr = GI_NAMES[name]
    cats = [cat] + (["textile"] if name in TEXTILE else [])
    g = {"id": re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-"), "name": L(name, hi, mr), "categories": cats,
         "applicationNo": app, "filingDate": date, "registrationYear": None, "region": None, "description": None,
         "sourceId": "gi-registry", "url": GI_PDF, "revisionStatus": "final", "confidence": "Official",
         "note": "Registered GI as listed by the GI Registry (as on 31 Dec 2025). Date shown is the filing date."}
    if states in SHARED: g["sharedWith"] = SHARED[states]
    gis.append(g)
r["giProducts"] = gis
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-MH.json", r)

# India reference row
ind = read("india.json")
im = ind["metrics"]
for k in im: im[k]["dataLevel"] = "national"
im["population2011"] = dp(1210854977, "persons", "2011", "census", "census", SDB, level="national",
    note="Census 2011 final total; State Data Bank shows 12,10,855 thousand.")
im["area"] = dp(3287469, "km²", "2023", "calendar", "fsi", LS_FOREST, level="national",
    note="Geographical area used in ISFR 2023 (includes areas under the Government of India's map).")
im["sexRatio2011"] = dp(943, "females per 1000 males", "2011", "census", "census", SDB, level="national")
im["childSexRatio2011"] = dp(919, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, level="national")
im["literacyRate2011"] = dp(73.0, "%", "2011", "census", "census", SDB, level="national", note="Population aged 7+, as rounded by the State Data Bank.")
im["urbanisation2011"] = dp(31.1, "%", "2011", "census", "census", SDB, level="national")
im["forestCoverPct"] = dp(21.76, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST, level="national",
    note="Computed from ISFR 2023 forest cover 7,15,342.61 km² ÷ 32,87,469 km².")
ind["meta"]["lastUpdated"] = TODAY
write("india.json", ind)
print("core ok", len(gis), "GIs")
