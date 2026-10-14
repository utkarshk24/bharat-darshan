"""Tamil Nadu — Phase 3 profile: identity, officeholders, projects, GIs.
Core Census/MoSPI metrics are written by tn_up_core.py (run it first)."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

GOV_URL = "https://lokbhavan.tn.gov.in/?p=15099"
CM_URL = "https://newsonair.gov.in/tvk-founder-c-joseph-vijay-to-take-oath-as-tamil-nadu-chief-minister-today/"
SPK_URL = "https://newsonair.gov.in/tvk-legislator-jcd-prabhakar-elected-as-tamil-nadu-assembly-speaker/"
CMRL2 = "https://www.pmindia.gov.in/en/news_updates/cabinet-approves-chennai-metro-rail-project-phase-ii-comprising-three-corridors-i-madhavaram-to-sipcot-ii-light-house-to-poonamallee-bypass-and-iii-madhavaram-to-sholinganallur/"
CMRL2_OPEN = "https://newsonair.gov.in/pm-modi-to-visit-chennai-inaugurate-metro-and-railway-projects-on-october-11/"
PAMBAN = "https://pmindia.gov.in/?p=16587222"
KSP = "https://www.isro.gov.in/Second_Spaceport_FoundationStone_Laid_Hon_PrimeMinister.html"
KKNPP = "https://thefederal.com/the-federal-special/kudankulam-hydro-test-russian-collaboration-nuclear-plant-241133"

r = read("regions/IN-TN.json")
r["officialPortal"] = "https://www.tn.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Nilgiri tahr", "नीलगिरि ताहर", "निलगिरी ताहर", "Nilgiritragus hylocrius"),
    "bird": sym("Emerald dove", "हरित कपोत (एमराल्ड डव)", "पाचू कबूतर (एमराल्ड डव्ह)", "Chalcophaps indica"),
    "flower": sym("Flame lily (Senganthal)", "कलिहारी (सेंगांतल)", "कळलावी (सेंगांतल)", "Gloriosa superba"),
    "tree": sym("Palmyra palm", "ताड़", "ताड", "Borassus flabellifer"),
    "fruit": sym("Jackfruit", "कटहल", "फणस", "Artocarpus heterophyllus"),
    "butterfly": sym("Tamil yeoman", "तमिल योमन", "तमिळ योमन", "Cirrochroa thais"),
}

r["government"] = {
    "headOfState": office("governor", L("Rajendra Vishwanath Arlekar", "राजेंद्र विश्वनाथ आर्लेकर", "राजेंद्र विश्वनाथ आर्लेकर"), None, "2026-03-12",
                          "tn-lokbhavan", GOV_URL, "https://lokbhavan.tn.gov.in",
                          note="Sworn in at Lok Bhavan, Chennai, on 12 March 2026 by the Chief Justice of the Madras High Court (Lok Bhavan, Tamil Nadu). Took additional charge of Tamil Nadu while Governor of Keralam, succeeding R. N. Ravi, who moved to West Bengal. On 12 October 2026 the President appointed him Governor of Tamil Nadu and named Om Prakash Mathur Governor of Keralam (Rashtrapati Bhavan communiqué, reported by UNI and ANI)."),
    "headOfGovernment": office("chief-minister", L("C. Joseph Vijay", "सी. जोसेफ़ विजय", "सी. जोसेफ विजय"), "TVK", "2026-05-10",
                               "newsonair", CM_URL, "https://www.tn.gov.in",
                               note="Founder of Tamilaga Vettri Kazhagam (TVK). Sworn in on 10 May 2026 with nine ministers, with the support of INC, CPI, CPI(M), VCK and IUML — 120 of 234 MLAs-elect (News On AIR)."),
    "others": [
        office("speaker", L("J. C. D. Prabhakar", "जे. सी. डी. प्रभाकर", "जे. सी. डी. प्रभाकर"), "TVK", "2026-05-12", "newsonair", SPK_URL, "https://www.assembly.tn.gov.in",
               note="Elected unopposed on 12 May 2026 (News On AIR)."),
        office("leader-of-opposition", L("Udhayanidhi Stalin", "उदयनिधि स्टालिन", "उदयनिधी स्टालिन"), "DMK", None, "newsonair", SPK_URL, "https://www.assembly.tn.gov.in",
               conf="Third-party verified", rev="provisional",
               note="Named as Opposition leader in News On AIR's report of 12 May 2026. Date of formal recognition by the Speaker not yet found; confirm on the Assembly website."),
    ],
}

r["projects"] = [
    proj("chennai-metro-2", L("Chennai Metro Rail Phase II", "चेन्नई मेट्रो रेल चरण II", "चेन्नई मेट्रो रेल टप्पा II"),
         L("118.9 km of new lines with 128 stations on three corridors — Madhavaram–SIPCOT (45.8 km), Lighthouse–Poonamallee Bypass (26.1 km) and Madhavaram–Sholinganallur (47 km) — taking Chennai's network to 173 km. Approved by the Union Cabinet on 3 October 2024 with a 2027 target. The first stretch, 14.6 km from Poonamallee to Vadapalani, was inaugurated on 11 October 2026 (News On AIR).",
           "तीन कॉरिडोर पर 128 स्टेशनों वाली 118.9 किमी नई लाइनें — माधवरम–सिपकॉट (45.8 किमी), लाइटहाउस–पूनमल्ली बाइपास (26.1 किमी) और माधवरम–शोलिंगनल्लूर (47 किमी) — जिनसे चेन्नई का नेटवर्क 173 किमी हो जाएगा। केंद्रीय मंत्रिमंडल ने 3 अक्टूबर 2024 को 2027 के लक्ष्य के साथ मंज़ूरी दी। पहला खंड, पूनमल्ली से वडपलनी तक 14.6 किमी, 11 अक्टूबर 2026 को शुरू हुआ (न्यूज़ ऑन एयर)।",
           "तीन मार्गिकांवर 128 स्थानकांसह 118.9 किमी नवे मार्ग — माधवरम–सिपकॉट (45.8 किमी), लाइटहाऊस–पूनमल्ली बायपास (26.1 किमी) आणि माधवरम–शोलिंगनल्लूर (47 किमी) — ज्यामुळे चेन्नईचे जाळे 173 किमी होईल. केंद्रीय मंत्रिमंडळाने 3 ऑक्टोबर 2024 रोजी 2027 च्या उद्दिष्टासह मंजुरी दिली. पहिला टप्पा, पूनमल्ली ते वडपलनी 14.6 किमी, 11 ऑक्टोबर 2026 रोजी सुरू झाला (न्यूज ऑन एअर)."),
         "transport", "Chennai Metro Rail Limited (CMRL)", 63246, "Cost as approved by the Union Cabinet, 3 October 2024.", "2024",
         "2024", "2027 (target at approval)", "Under Construction", "pmindia", CMRL2),
    proj("pamban-bridge", L("New Pamban Rail Bridge", "नया पंबन रेल पुल", "नवा पंबन रेल्वे पूल"),
         L("A 2.08 km sea bridge with 99 spans linking Rameswaram island to the mainland, replacing the 1914 bridge. Its 72.5 m vertical-lift span rises 17 m to let ships pass. Inaugurated on 6 April 2025.",
           "रामेश्वरम द्वीप को मुख्य भूमि से जोड़ने वाला 99 स्पैन का 2.08 किमी समुद्री पुल, जिसने 1914 के पुल की जगह ली। इसका 72.5 मीटर का वर्टिकल-लिफ़्ट स्पैन जहाज़ों के गुज़रने के लिए 17 मीटर ऊपर उठता है। 6 अप्रैल 2025 को उद्घाटन।",
           "रामेश्वरम बेट मुख्य भूमीशी जोडणारा 99 गाळ्यांचा 2.08 किमी सागरी पूल, ज्याने 1914 च्या पुलाची जागा घेतली. त्याचा 72.5 मीटरचा उभा उचलला जाणारा गाळा जहाजांसाठी 17 मीटर वर उचलला जातो. 6 एप्रिल 2025 रोजी उद्घाटन."),
         "transport", "Ministry of Railways", 700, "\"Over ₹700 crore\" (PMO).", "2025",
         None, "April 2025", "Completed", "pmindia", PAMBAN),
    proj("kulasekarapattinam", L("ISRO launch complex, Kulasekarapattinam", "इसरो प्रक्षेपण परिसर, कुलशेखरपट्टिनम", "इस्रो प्रक्षेपण संकुल, कुलशेखरपट्टिनम"),
         L("India's second spaceport, on the coast of Thoothukudi district, for small launch vehicles; its location allows direct southward launches. Foundation stone laid on 28 February 2024; ISRO gave a commissioning timeline of 24 months.",
           "छोटे प्रक्षेपण यानों के लिए थूथुकुडी ज़िले के तट पर भारत का दूसरा अंतरिक्ष प्रक्षेपण केंद्र; इसकी स्थिति सीधे दक्षिण की ओर प्रक्षेपण संभव बनाती है। 28 फ़रवरी 2024 को शिलान्यास; इसरो ने चालू होने के लिए 24 महीने की समय-सीमा बताई थी।",
           "लहान प्रक्षेपकांसाठी थुथुकुडी जिल्ह्याच्या किनाऱ्यावरील भारताचे दुसरे अंतराळ प्रक्षेपण केंद्र; त्याच्या स्थानामुळे थेट दक्षिणेकडे प्रक्षेपण शक्य होते. 28 फेब्रुवारी 2024 रोजी पायाभरणी; इस्रोने कार्यान्वित होण्यासाठी 24 महिन्यांची कालमर्यादा सांगितली होती."),
         "space", "Indian Space Research Organisation (ISRO)", None, None, None,
         "2024", None, "Under Construction", "isro", KSP),
    proj("kudankulam-3-6", L("Kudankulam Nuclear Power Project, Units 3–6", "कुडनकुलम परमाणु विद्युत परियोजना, इकाइयाँ 3–6", "कुडनकुलम अणुऊर्जा प्रकल्प, युनिट 3–6"),
         L("Four 1,000 MW pressurised-water reactors being built alongside the two operating units in Tirunelveli district. Units 3 and 4 were reported at about 81% physical progress and Units 5 and 6 at about 42% as of January 2026, with commissioning expected in 2027 and 2030 respectively.",
           "तिरुनेलवेली ज़िले में चल रही दो इकाइयों के साथ बन रहे चार 1,000 मेगावाट के प्रेशराइज़्ड-वॉटर रिएक्टर। जनवरी 2026 तक इकाई 3 और 4 की भौतिक प्रगति लगभग 81% और इकाई 5 व 6 की लगभग 42% बताई गई; इनके क्रमशः 2027 और 2030 में चालू होने की उम्मीद है।",
           "तिरुनेलवेली जिल्ह्यात चालू असलेल्या दोन युनिटांसोबत उभारल्या जात असलेल्या चार 1,000 मेगावॉटच्या प्रेशराइज्ड-वॉटर अणुभट्ट्या. जानेवारी 2026 पर्यंत युनिट 3 व 4 ची प्रत्यक्ष प्रगती सुमारे 81% आणि युनिट 5 व 6 ची सुमारे 42% नोंदवली गेली; ते अनुक्रमे 2027 आणि 2030 मध्ये कार्यान्वित होणे अपेक्षित आहे."),
         "power", "Nuclear Power Corporation of India Limited (NPCIL)", None, None, None,
         None, "2027 (Units 3–4), 2030 (Units 5–6), as reported", "Under Construction", "thefederal", KKNPP, conf="Third-party verified"),
]

GI_NAMES = {
 "Eathomozhy Tall Coconut": ("एतमोझी लंबा नारियल", "एतमोझी उंच नारळ"),
 "Nilgiri (Orthodox) Logo": ("नीलगिरि (ऑर्थोडॉक्स) चाय लोगो", "निलगिरी (ऑर्थोडॉक्स) चहा बोधचिन्ह"),
 "Virupakshi Hill Banana": ("विरुपाक्षी पहाड़ी केला", "विरुपाक्षी डोंगरी केळी"),
 "Sirumalai Hill Banana": ("सिरुमलै पहाड़ी केला", "सिरुमलै डोंगरी केळी"),
 "Erode Manjal (Erode Turmeric)": ("इरोड मंजल (इरोड हल्दी)", "इरोड मंजळ (इरोड हळद)"),
 "Madurai Malli": ("मदुरै मल्ली (मोगरा)", "मदुराई मल्ली (मोगरा)"),
 "Kodaikanal Malai Poondu": ("कोडैकनाल मलै पूंडु (पहाड़ी लहसुन)", "कोडैकनाल मलै पूंडू (डोंगरी लसूण)"),
 "Kanniyakumari Clove": ("कन्याकुमारी लौंग", "कन्याकुमारी लवंग"),
 "Ramnathapuram Mundu Chilli": ("रामनाथपुरम मुंडु मिर्च", "रामनाथपुरम मुंडू मिरची"),
 "Vellore Spiny Brinjal": ("वेल्लोर काँटेदार बैंगन", "वेल्लोर काटेरी वांगे"),
 "Authoor Vetrilai": ("आत्तूर वेत्रिलै (पान)", "आत्तूर वेत्रिलै (विड्याचे पान)"),
 "Cumbum Panneer Thratchai": ("कम्बम पन्नीर अंगूर", "कंबम पन्नीर द्राक्ष"),
 "Sholavandan Vetrilai": ("शोलवंदन वेत्रिलै (पान)", "शोलवंदन वेत्रिलै (विड्याचे पान)"),
 "Kanyakumari Matti Banana": ("कन्याकुमारी मट्टी केला", "कन्याकुमारी मट्टी केळी"),
 "Madurai Marikolunthu (Davana)": ("मदुरै मरिकोलुंतु (दवना)", "मदुराई मरिकोलुंतू (दवणा)"),
 "Kumbakonam Vetrilai (Kumbakonam Betel Leaf)": ("कुंभकोणम वेत्रिलै (कुंभकोणम पान)", "कुंभकोणम वेत्रिलै (कुंभकोणम विड्याचे पान)"),
 "Panruti Palappazham (Panruti Jack Fruit)": ("पनरुटी पलाप्पझम (पनरुटी कटहल)", "पनरुटी पलाप्पझम (पनरुटी फणस)"),
 "Panruti Cashew": ("पनरुटी काजू", "पनरुटी काजू"),
 "Puliyankudi Acid Lime": ("पुलियंकुडी कागज़ी नींबू", "पुलियंकुडी कागदी लिंबू"),
 "Virudhunagar Samba Vathal": ("विरुधुनगर सांबा वत्तल (सूखी मिर्च)", "विरुधुनगर सांबा वत्तल (सुकी मिरची)"),
 "Chettikulam Small Onion": ("चेट्टिकुलम छोटा प्याज़", "चेट्टिकुलम छोटा कांदा"),
 "Ramanadu Chithiraikar Rice": ("रामनाडु चित्तिरैकार चावल", "रामनाडू चित्तिरैकार तांदूळ"),
 "Thooyamalli Rice": ("तूयमल्ली चावल", "तूयमल्ली तांदूळ"),
 "Srivilliputtur Palkova": ("श्रीविल्लिपुत्तूर पालकोवा", "श्रीविल्लिपुत्तूर पालकोवा"),
 "Kovilpatti Kadalai Mittai": ("कोविलपट्टी कडलै मिट्टाई (मूंगफली चिक्की)", "कोविलपट्टी कडलै मिट्टाई (शेंगदाणा चिक्की)"),
 "Palani Panchamirtham": ("पलनी पंचामृतम", "पळनी पंचामृतम"),
 "Manapparai Murukku": ("मनप्पारै मुरुक्कु", "मनप्पारै मुरुक्कू (चकली)"),
 "Ooty Varkey": ("ऊटी वर्की", "ऊटी वर्की"),
 "Udangudi Panangkarupatti": ("उडनगुडी पनंकरुपट्टी (ताड़ गुड़)", "उडनगुडी पनंकरुपट्टी (ताडगूळ)"),
 "Salem Sago (Javvarisi)": ("सेलम साबूदाना (जव्वरिसि)", "सेलम साबुदाणा (जव्वरिसी)"),
 "Marthandam Honey": ("मार्तंडम शहद", "मार्तंडम मध"),
 "Kavindhapadi Nattu Sakkarai": ("कविंदपाडी नाट्टु सक्करै (देसी शक्कर)", "कविंदपाडी नाट्टू सक्करै (देशी साखर)"),
 "Salem Fabric": ("सेलम वस्त्र", "सेलम वस्त्र"),
 "Kancheepuram Silk": ("कांचीपुरम रेशम", "कांचीपुरम रेशीम"),
 "Bhavani Jamakkalam": ("भवानी जमक्कालम (दरी)", "भवानी जमक्काळम (सतरंजी)"),
 "Madurai Sungudi": ("मदुरै सुंगुडी", "मदुराई सुंगुडी"),
 "Thanjavur Painting": ("तंजावुर चित्रकला", "तंजावूर चित्रकला"),
 "Thanjavur Art Plate": ("तंजावुर कला थाली", "तंजावूर कलात्मक ताट"),
 "Swamimalai Bronze Icons": ("स्वामीमलै कांस्य प्रतिमाएँ", "स्वामीमलै कांस्य मूर्ती"),
 "Temple Jewellery of Nagercoil": ("नागरकोइल के मंदिर आभूषण", "नागरकोइलचे मंदिर दागिने"),
 "Arani Silk": ("आरणी रेशम", "आरणी रेशीम"),
 "Kovai Kora Cotton Sarees": ("कोवै कोरा सूती साड़ियाँ", "कोवै कोरा सुती साड्या"),
 "Salem Silk known as Salem Venpattu": ("सेलम रेशम (सेलम वेनपट्टु)", "सेलम रेशीम (सेलम वेनपट्टू)"),
 "Thanjavur Doll": ("तंजावुर गुड़िया", "तंजावूर बाहुली"),
 "Toda Embroidery": ("तोडा कढ़ाई", "तोडा भरतकाम"),
 "Pattamadai Pai (\"Pattamadai Mat\")": ("पत्तमडै पाय (पत्तमडै चटाई)", "पत्तमडै पाय (पत्तमडै चटई)"),
 "Nachiarkoil Kuthuvilakku (\"Nachiarkoil Lamp\")": ("नाच्चियारकोइल कुत्तुविलक्कु (दीपस्तंभ)", "नाच्चियारकोइल कुत्तुविळक्कू (समई)"),
 "Chettinad Kottan": ("चेट्टिनाड कोट्टन (टोकरी)", "चेट्टिनाड कोट्टन (टोपली)"),
 "Thanjavur Veenai": ("तंजावुर वीणा", "तंजावूर वीणा"),
 "Kandangi Saree": ("कंडांगी साड़ी", "कंडांगी साडी"),
 "Thanjavur Netti Works": ("तंजावुर नेट्टी शिल्प", "तंजावूर नेट्टी कलाकुसर"),
 "Mahabalipuram Stone Sculpture": ("महाबलीपुरम पाषाण मूर्तिकला", "महाबलीपुरम पाषाण शिल्प"),
 "Arumbavur Wood Carvings": ("अरुम्बावूर काष्ठ नक़्क़ाशी", "अरुंबावूर काष्ठ कोरीवकाम"),
 "Thirubuvanam Silk Sarees": ("तिरुभुवनम रेशमी साड़ियाँ", "तिरुभुवनम रेशमी साड्या"),
 "Thanjavur Art Plate (Logo)": ("तंजावुर कला थाली (लोगो)", "तंजावूर कलात्मक ताट (बोधचिन्ह)"),
 "Swamimalai Bronze Icons (Logo)": ("स्वामीमलै कांस्य प्रतिमाएँ (लोगो)", "स्वामीमलै कांस्य मूर्ती (बोधचिन्ह)"),
 "Temple Jewellery of Nagercoil (Logo)": ("नागरकोइल के मंदिर आभूषण (लोगो)", "नागरकोइलचे मंदिर दागिने (बोधचिन्ह)"),
 "Karuppur Kalamkari Paintings": ("करुप्पूर कलमकारी चित्र", "करुप्पूर कलमकारी चित्रे"),
 "Kallakurichi Wood Carving": ("कल्लकुरिची काष्ठ नक़्क़ाशी", "कल्लकुरिची काष्ठ कोरीवकाम"),
 "Narasinghapettai Nagaswaram": ("नरसिंगपेट्टै नागस्वरम", "नरसिंगपेट्टै नागस्वरम"),
 "Dindigul Locks": ("डिंडीगुल ताले", "दिंडीगुल कुलपे"),
 "Myladi Stone Carvings": ("मयिलाडी पाषाण नक़्क़ाशी", "मयिलाडी पाषाण कोरीवकाम"),
 "Manamadurai Pottery": ("मानामदुरै मिट्टी के बर्तन", "मानामदुराई मातीची भांडी"),
 "Thaikkal Rattan Craft": ("तैक्काल बेंत शिल्प", "तैक्काल वेत हस्तकला"),
 "Jaderi Namakatti": ("जडेरी नामकट्टी", "जडेरी नामकट्टी"),
 "Negamam Cotton Saree": ("नेगमम सूती साड़ी", "नेगमम सुती साडी"),
 "Chedibutta Saree": ("चेडिबुट्टा साड़ी", "चेडिबुट्टा साडी"),
 "Vilachery Clay Toys": ("विलाचेरी मिट्टी के खिलौने", "विलाचेरी मातीची खेळणी"),
 "Thovalai Maanika Maalai": ("तोवालै माणिक्क मालै", "तोवाळै माणिक्क माळै"),
 "Ambasamudram Choppu Saman (Wooden Toys)": ("अंबासमुद्रम चोप्पु सामान (लकड़ी के खिलौने)", "अंबासमुद्रम चोप्पू सामान (लाकडी खेळणी)"),
 "Woraiyur Cotton Saree": ("वोरैयूर सूती साड़ी", "वोरैयूर सुती साडी"),
 "Namakkal Maakkal Paattirangal": ("नामक्कल माक्कल पात्तिरंगल (सेलखड़ी बर्तन)", "नामक्कल माक्कल पात्तिरंगळ (शिरगोळ्याची भांडी)"),
 "Coimbatore Wet Grinder": ("कोयंबटूर वेट ग्राइंडर", "कोइंबतूर वेट ग्राइंडर"),
 "East India Leather": ("ईस्ट इंडिया चमड़ा", "ईस्ट इंडिया चामडे"),
}
TEXTILE = {"Salem Fabric", "Kancheepuram Silk", "Bhavani Jamakkalam", "Madurai Sungudi", "Arani Silk", "Kovai Kora Cotton Sarees",
           "Salem Silk known as Salem Venpattu", "Toda Embroidery", "Kandangi Saree", "Thirubuvanam Silk Sarees", "Negamam Cotton Saree",
           "Chedibutta Saree", "Woraiyur Cotton Saree"}
r["giProducts"] = gi_list("gi_tn.tsv", GI_NAMES, {}, TEXTILE)
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-TN.json", r)
print("tn core ok", len(r["giProducts"]), "GIs")
