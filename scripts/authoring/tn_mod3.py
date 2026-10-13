"""Tamil Nadu modules P–Z: nature, water, safety, GI, tourism, cities, sports, personalities, diaspora, civic, trivia."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-TN"
TN23 = "https://des.tn.gov.in/sites/default/files/2024-01/At_a_glance_%2029_12_2023.pdf"
TOUR = "https://tourism.gov.in/sites/default/files/2026-03/usq.3834%20for%2016.03.2026.pdf"
PAMBAN = "https://pmindia.gov.in/?p=16587222"
tn = read("regions/IN-TN.json")["metrics"]; ind = read("india.json")["metrics"]
NAME = L("Tamil Nadu", "तमिलनाडु", "तमिळनाडू")

# ---------------- P. Nature ----------------
RAMSAR_TN = [
    ("Point Calimere Wildlife and Bird Sanctuary", "पॉइंट कैलिमेर वन्यजीव एवं पक्षी अभयारण्य", "पॉइंट कॅलिमेर वन्यजीव व पक्षी अभयारण्य", "19 Aug 2002", "38,500"),
    ("Koonthankulam Bird Sanctuary", "कूंतनकुलम पक्षी अभयारण्य", "कूंतनकुळम पक्षी अभयारण्य", "8 Nov 2021", "72"),
    ("Chitrangudi Bird Sanctuary", "चित्रांगुडी पक्षी अभयारण्य", "चित्रांगुडी पक्षी अभयारण्य", "8 Nov 2021", "260"),
    ("Karikili Bird Sanctuary", "करिकिली पक्षी अभयारण्य", "करिकिली पक्षी अभयारण्य", "8 Apr 2022", "58"),
    ("Pichavaram Mangrove", "पिच्चावरम मैंग्रोव", "पिच्चावरम खारफुटी", "8 Apr 2022", "1,479"),
    ("Pallikaranai Marsh Reserve Forest", "पल्लिकरणै दलदल आरक्षित वन", "पल्लिकरणै दलदल राखीव वन", "8 Apr 2022", "1,248"),
    ("Gulf of Mannar Marine Biosphere Reserve", "मन्नार की खाड़ी समुद्री जैवमंडल रिज़र्व", "मन्नारचे आखात सागरी जीवावरण राखीव क्षेत्र", "8 Apr 2022", "52,672"),
    ("Vembannur Wetland Complex", "वेम्बन्नूर आर्द्रभूमि परिसर", "वेंबन्नूर पाणथळ संकुल", "8 Apr 2022", "20"),
    ("Vellode Bird Sanctuary", "वेल्लोड पक्षी अभयारण्य", "वेल्लोड पक्षी अभयारण्य", "8 Apr 2022", "77"),
    ("Udhayamarthandapuram Bird Sanctuary", "उदयमार्तंडपुरम पक्षी अभयारण्य", "उदयमार्तंडपुरम पक्षी अभयारण्य", "8 Apr 2022", "44"),
    ("Vedanthangal Bird Sanctuary", "वेदांतांगल पक्षी अभयारण्य", "वेदांतांगल पक्षी अभयारण्य", "8 Apr 2022", "40"),
    ("Suchindram Theroor Wetland Complex", "शुचींद्रम तेरूर आर्द्रभूमि परिसर", "शुचींद्रम तेरूर पाणथळ संकुल", "8 Apr 2022", "94"),
    ("Vaduvur Bird Sanctuary", "वडुवूर पक्षी अभयारण्य", "वडुवूर पक्षी अभयारण्य", "8 Apr 2022", "113"),
    ("Kanjirankulam Bird Sanctuary", "कांजिरनकुलम पक्षी अभयारण्य", "कांजिरनकुळम पक्षी अभयारण्य", "8 Apr 2022", "97"),
    ("Karaivetti Bird Sanctuary", "करैवेट्टी पक्षी अभयारण्य", "करैवेट्टी पक्षी अभयारण्य", "24 May 2023", "453.72"),
    ("Longwood Shola Reserve Forest", "लॉन्गवुड शोला आरक्षित वन", "लाँगवुड शोला राखीव वन", "24 May 2023", "116.01"),
    ("Kazhuveli Bird Sanctuary", "कझुवेली पक्षी अभयारण्य", "कळुवेली पक्षी अभयारण्य", "16 Jan 2024", "5,151.60"),
    ("Nanjarayan Bird Sanctuary", "नंजरायन पक्षी अभयारण्य", "नंजरायन पक्षी अभयारण्य", "16 Jan 2024", "125.87"),
    ("Sakkarakottai Bird Sanctuary", "सक्करकोट्टै पक्षी अभयारण्य", "सक्करकोट्टै पक्षी अभयारण्य", "15 Jul 2024", "230.50"),
    ("Therthangal Bird Sanctuary", "तेर्तांगल पक्षी अभयारण्य", "तेर्तांगल पक्षी अभयारण्य", "15 Jul 2024", "29.30"),
]
module(R, "nature", [
    prose("p1", L(
        "Tamil Nadu's forests cover about 20.3% of its area (ISFR 2023), concentrated on the Western Ghats in the west — the Nilgiris, Anamalai, Palani and Agasthyamalai hills — and on the scattered Eastern Ghats ranges. The Nilgiri Biosphere Reserve, India's first, spans Tamil Nadu, Keralam and Karnataka and holds one of the largest populations of Asian elephants and tigers in the country. The shola forests and grasslands of the high Nilgiris are home to the Nilgiri tahr, the State animal.\n\nThe coast is just as rich. The Gulf of Mannar Marine Biosphere Reserve protects coral reefs, seagrass beds and dugongs; Pichavaram has one of India's largest mangrove forests; and Point Calimere draws flamingos and other migratory birds. With 20 sites, Tamil Nadu has more Ramsar wetlands than any other State — many of them small village tanks that have hosted heronries for generations, such as Vedanthangal.",
        "तमिलनाडु के वन इसके लगभग 20.3% क्षेत्र पर हैं (आईएसएफ़आर 2023), जो मुख्यतः पश्चिम में पश्चिमी घाट — नीलगिरि, अनामलै, पलनी और अगस्त्यमलै पहाड़ियों — और बिखरी पूर्वी घाट शृंखलाओं पर हैं। भारत का पहला जैवमंडल रिज़र्व, नीलगिरि जैवमंडल रिज़र्व, तमिलनाडु, केरलम और कर्नाटक में फैला है और देश में एशियाई हाथियों और बाघों की सबसे बड़ी आबादियों में से एक का घर है। ऊँची नीलगिरि के शोला वन और घास के मैदान राज्य पशु नीलगिरि ताहर का निवास हैं।\n\nतट भी उतना ही समृद्ध है। मन्नार की खाड़ी समुद्री जैवमंडल रिज़र्व प्रवाल भित्तियों, समुद्री घास और डुगोंग की रक्षा करता है; पिच्चावरम में भारत के सबसे बड़े मैंग्रोव वनों में से एक है; और पॉइंट कैलिमेर में फ़्लेमिंगो और अन्य प्रवासी पक्षी आते हैं। 20 स्थलों के साथ तमिलनाडु में किसी भी अन्य राज्य से अधिक रामसर आर्द्रभूमियाँ हैं — इनमें से कई गाँव के छोटे तालाब हैं, जहाँ पीढ़ियों से बगुलों की बस्तियाँ रही हैं, जैसे वेदांतांगल।",
        "तमिळनाडूतील वने राज्याच्या सुमारे 20.3% क्षेत्रावर आहेत (आयएसएफआर 2023); ती मुख्यतः पश्चिमेकडील पश्चिम घाट — निलगिरी, अनामलै, पळनी व अगस्त्यमलै डोंगर — आणि विखुरलेल्या पूर्व घाट रांगांवर आहेत. भारतातील पहिले जीवावरण राखीव क्षेत्र, निलगिरी जीवावरण, तमिळनाडू, केरळम व कर्नाटकात पसरलेले असून देशातील आशियाई हत्ती व वाघांच्या सर्वांत मोठ्या लोकसंख्येपैकी एक तिथे आहे. उंच निलगिरीतील शोला वने व गवताळ प्रदेश हे राज्यप्राणी निलगिरी ताहरचे निवासस्थान आहे.\n\nकिनारपट्टीही तितकीच समृद्ध आहे. मन्नारच्या आखातातील सागरी जीवावरण राखीव क्षेत्र प्रवाळ, सागरी गवत आणि डुगाँगचे संरक्षण करते; पिच्चावरम येथे भारतातील सर्वांत मोठ्या खारफुटी वनांपैकी एक आहे; आणि पॉइंट कॅलिमेरला रोहित (फ्लेमिंगो) व इतर स्थलांतरित पक्षी येतात. 20 स्थळांसह तमिळनाडूत इतर कोणत्याही राज्यापेक्षा जास्त रामसर पाणथळ स्थळे आहेत — त्यांतील अनेक गावांचे लहान तलाव आहेत, जिथे पिढ्यानपिढ्या बगळ्यांच्या वसाहती आहेत, जसे वेदांतांगल."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(26450.22, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(26511.18, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), tn["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(20, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026 (India total 99)."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_TN],
          "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026. Areas as given in the list.", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची। क्षेत्रफल सूची के अनुसार।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी. क्षेत्रफळ यादीनुसार.")),
    lst("protected", [
        it3("mudumalai", "Mudumalai Tiger Reserve", "मुदुमलै बाघ अभयारण्य", "मुदुमलै व्याघ्र प्रकल्प", m=("Nilgiris", "नीलगिरि", "निलगिरी")),
        it3("anamalai", "Anamalai Tiger Reserve", "अनामलै बाघ अभयारण्य", "अनामलै व्याघ्र प्रकल्प", m=("Coimbatore–Tiruppur", "कोयंबटूर–तिरुप्पुर", "कोइंबतूर–तिरुप्पूर")),
        it3("sathy", "Sathyamangalam Tiger Reserve", "सत्यमंगलम बाघ अभयारण्य", "सत्यमंगलम व्याघ्र प्रकल्प", m=("Erode", "इरोड", "इरोड")),
        it3("kmtr", "Kalakad Mundanthurai Tiger Reserve", "कलक्काड मुंडनतुरै बाघ अभयारण्य", "कलक्काड मुंडनतुरै व्याघ्र प्रकल्प", m=("Tirunelveli–Kanniyakumari", "तिरुनेलवेली–कन्याकुमारी", "तिरुनेलवेली–कन्याकुमारी")),
        it3("smtr", "Srivilliputhur–Megamalai Tiger Reserve", "श्रीविल्लिपुत्तूर–मेघमलै बाघ अभयारण्य", "श्रीविल्लिपुत्तूर–मेघमलै व्याघ्र प्रकल्प", m=("Virudhunagar–Theni", "विरुधुनगर–थेनी", "विरुधुनगर–थेनी")),
        it3("nilgiri-br", "Nilgiri Biosphere Reserve", "नीलगिरि जैवमंडल रिज़र्व", "निलगिरी जीवावरण राखीव क्षेत्र", m=("Shared with Keralam and Karnataka", "केरलम और कर्नाटक के साथ साझा", "केरळम व कर्नाटकसोबत सामायिक")),
        it3("gom", "Gulf of Mannar Marine National Park", "मन्नार की खाड़ी समुद्री राष्ट्रीय उद्यान", "मन्नारचे आखात सागरी राष्ट्रीय उद्यान", m=("Coral islands", "प्रवाल द्वीप", "प्रवाळ बेटे")),
        it3("guindy", "Guindy National Park", "गिंडी राष्ट्रीय उद्यान", "गिंडी राष्ट्रीय उद्यान", m=("Inside Chennai city", "चेन्नई शहर के भीतर", "चेन्नई शहरात")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("tahr", "Nilgiri tahr", "नीलगिरि ताहर", "निलगिरी ताहर"), it3("elephant", "Asian elephant", "एशियाई हाथी", "आशियाई हत्ती"),
        it3("tiger", "Bengal tiger", "बंगाल बाघ", "पट्टेरी वाघ"), it3("lionmacaque", "Lion-tailed macaque", "शेरपूँछ मकाक", "सिंहपुच्छ माकड"),
        it3("dugong", "Dugong", "डुगोंग", "डुगाँग"), it3("blackbuck", "Blackbuck (Point Calimere, Vallanadu)", "काला हिरण (पॉइंट कैलिमेर, वल्लनाडु)", "काळवीट (पॉइंट कॅलिमेर, वल्लनाडू)"),
        it3("olive", "Olive ridley turtle", "ऑलिव रिडले कछुआ", "ऑलिव्ह रिडले कासव"), it3("kurinji", "Neelakurinji", "नीलकुरिंजी", "नीलकुरिंजी"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger reserve areas and tiger estimates", "बाघ अभयारण्य क्षेत्रफल और बाघों का अनुमान", "व्याघ्र प्रकल्प क्षेत्र व वाघांचा अंदाज"), "ntca", "NTCA tiger reserve list and All-India Tiger Estimation."),
        (L("National parks and sanctuaries (count, area)", "राष्ट्रीय उद्यान और अभयारण्य (संख्या, क्षेत्रफल)", "राष्ट्रीय उद्याने व अभयारण्ये (संख्या, क्षेत्र)"), "moefcc", "ENVIS / Wildlife Institute of India database."),
        (L("Mangrove cover", "मैंग्रोव आवरण", "खारफुटी आच्छादन"), "fsi", "ISFR 2023, Tamil Nadu chapter."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Water is a defining issue in Tamil Nadu. Most of the State lies in the rain shadow of the Western Ghats and depends on the north-east monsoon, so storage and sharing matter enormously. The Kaveri's waters have long been shared with Karnataka under tribunal awards and Supreme Court orders, now administered by the Cauvery Water Management Authority; the Mettur dam (1934) and the ancient Grand Anicut (Kallanai) regulate the flow into the delta.\n\nFor centuries villages have depended on networks of tanks (eris) that store monsoon run-off for irrigation and recharge groundwater. Chennai draws on several reservoirs, Krishna water from Andhra Pradesh and the Veeranam lake, and runs seawater desalination plants; floods in 2015 and droughts in 2017 and 2019 showed how exposed the city is to both extremes.",
        "तमिलनाडु में पानी एक निर्णायक मुद्दा है। राज्य का अधिकांश भाग पश्चिमी घाट की वृष्टि-छाया में है और उत्तर-पूर्व मानसून पर निर्भर है, इसलिए भंडारण और बँटवारा बहुत मायने रखते हैं। कावेरी का पानी लंबे समय से न्यायाधिकरण के निर्णयों और सर्वोच्च न्यायालय के आदेशों के तहत कर्नाटक के साथ बँटता रहा है, जिसका प्रबंधन अब कावेरी जल प्रबंधन प्राधिकरण करता है; मेट्टूर बाँध (1934) और प्राचीन ग्रैंड अनिकट (कल्लणै) डेल्टा में बहाव को नियंत्रित करते हैं।\n\nसदियों से गाँव तालाबों (एरी) के जाल पर निर्भर रहे हैं, जो सिंचाई के लिए मानसून का पानी जमा करते हैं और भूजल को भरते हैं। चेन्नई कई जलाशयों, आंध्र प्रदेश से आने वाले कृष्णा जल और वीरानम झील पर निर्भर है, और समुद्री जल के विलवणीकरण संयंत्र भी चलाता है; 2015 की बाढ़ और 2017 व 2019 के सूखे ने दिखाया कि शहर दोनों अतियों के सामने कितना असुरक्षित है।",
        "तमिळनाडूत पाणी हा निर्णायक प्रश्न आहे. राज्याचा बहुतांश भाग पश्चिम घाटाच्या पर्जन्यछायेत असून ईशान्य मोसमी पावसावर अवलंबून आहे, त्यामुळे साठवण आणि वाटप फार महत्त्वाचे ठरते. कावेरीचे पाणी दीर्घकाळापासून लवाद निवाडे व सर्वोच्च न्यायालयाच्या आदेशांनुसार कर्नाटकसोबत वाटले जाते, आणि आता त्याचे व्यवस्थापन कावेरी जल व्यवस्थापन प्राधिकरण करते; मेट्टूर धरण (1934) आणि प्राचीन ग्रँड अनिकट (कल्लणै) त्रिभुज प्रदेशातील प्रवाह नियंत्रित करतात.\n\nशतकानुशतके गावे तलावांच्या (एरी) जाळ्यावर अवलंबून राहिली आहेत — ते सिंचनासाठी पावसाचे पाणी साठवतात आणि भूजल पुनर्भरण करतात. चेन्नई अनेक जलाशय, आंध्र प्रदेशातून येणारे कृष्णेचे पाणी आणि वीरानम तलावावर अवलंबून आहे, आणि समुद्राचे पाणी गोडे करणारे प्रकल्पही चालवते; 2015 चा पूर आणि 2017 व 2019 चा दुष्काळ यांनी शहर दोन्ही टोकांना किती असुरक्षित आहे हे दाखवले."),
        conf="Editorial"),
    gaps("g", [
        (L("Large dams (count) and storage", "बड़े बाँध (संख्या) और भंडारण", "मोठी धरणे (संख्या) व साठा"), "tn-gov", "Central Water Commission National Register of Large Dams."),
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "tn-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Number of irrigation tanks", "सिंचाई तालाबों की संख्या", "सिंचन तलावांची संख्या"), "tn-gov", "Water Resources Department."),
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Tamil Nadu's main natural hazards come from the Bay of Bengal. Cyclones strike the coast most often in October to December — Vardah (2016) hit Chennai, Gaja (2018) devastated the Kaveri delta and Michaung (2023) flooded the capital. Intense north-east monsoon rain causes urban flooding, as in Chennai in 2015. The 2004 Indian Ocean tsunami killed thousands along the coast, especially in Nagapattinam and Kanniyakumari, and led to India's tsunami early-warning system. Droughts and summer heat affect the interior.\n\nFor visitors, the main precautions are following IMD cyclone and heavy-rain warnings during the north-east monsoon, heeding beach-safety signs, and staying hydrated in the April–June heat.",
        "तमिलनाडु के मुख्य प्राकृतिक ख़तरे बंगाल की खाड़ी से आते हैं। चक्रवात अक्सर अक्टूबर से दिसंबर में तट से टकराते हैं — वरदा (2016) ने चेन्नई को, गाजा (2018) ने कावेरी डेल्टा को तबाह किया और मिचौंग (2023) ने राजधानी को जलमग्न किया। तेज़ उत्तर-पूर्व मानसूनी बारिश से शहरी बाढ़ आती है, जैसे 2015 में चेन्नई में। 2004 की हिंद महासागर सुनामी ने तट पर, ख़ासकर नागपट्टिनम और कन्याकुमारी में, हज़ारों लोगों की जान ली और इसके बाद भारत की सुनामी पूर्व-चेतावनी प्रणाली बनी। भीतरी भाग में सूखा और गर्मी की लहर असर डालते हैं।\n\nपर्यटकों के लिए मुख्य सावधानियाँ हैं: उत्तर-पूर्व मानसून के दौरान आईएमडी की चक्रवात और भारी वर्षा चेतावनियों का पालन, समुद्र तट सुरक्षा संकेतों पर ध्यान, और अप्रैल–जून की गर्मी में पानी पीते रहना।",
        "तमिळनाडूतील प्रमुख नैसर्गिक धोके बंगालच्या उपसागरातून येतात. चक्रीवादळे बहुतेक ऑक्टोबर ते डिसेंबरमध्ये किनाऱ्यावर आदळतात — वरदा (2016) चेन्नईवर, गाजा (2018) ने कावेरी त्रिभुज प्रदेश उद्ध्वस्त केला आणि मिचौंग (2023) ने राजधानी जलमय केली. ईशान्य मोसमी पावसाच्या तीव्र सरींमुळे शहरांत पूर येतात, जसा 2015 मध्ये चेन्नईत आला. 2004 च्या हिंदी महासागरातील त्सुनामीने किनाऱ्यावर, विशेषतः नागपट्टिनम व कन्याकुमारीत हजारो बळी घेतले, आणि त्यानंतर भारताची त्सुनामी पूर्वसूचना यंत्रणा उभी राहिली. अंतर्गत भागात दुष्काळ आणि उष्णतेची लाट परिणाम करतात.\n\nपर्यटकांसाठी मुख्य काळजी: ईशान्य मोसमी काळात आयएमडीच्या चक्रीवादळ व मुसळधार पावसाच्या इशाऱ्यांचे पालन, समुद्रकिनाऱ्यावरील सुरक्षा सूचनांकडे लक्ष, आणि एप्रिल–जूनच्या उष्म्यात पुरेसे पाणी पिणे."),
        conf="Editorial"),
    emergency_table(("Tamil Nadu", "तमिलनाडु", "तमिळनाडू")),
    lst("links", [
        it3("sdma", "Tamil Nadu State Disaster Management Authority", "तमिलनाडु राज्य आपदा प्रबंधन प्राधिकरण", "तमिळनाडू राज्य आपत्ती व्यवस्थापन प्राधिकरण", url="https://tnsdma.tn.gov.in", src="tn-gov"),
        it3("imd", "IMD weather and cyclone warnings", "आईएमडी मौसम और चक्रवात चेतावनियाँ", "आयएमडी हवामान व चक्रीवादळ इशारे", url="https://mausam.imd.gov.in", src="imd"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Cyclone and flood hazard zones", "चक्रवात और बाढ़ ख़तरा क्षेत्र", "चक्रीवादळ व पूर धोका क्षेत्रे"), "ndma", "TNSDMA vulnerability atlas."),
        (L("Coastal erosion status", "तटीय कटाव की स्थिति", "किनारी धूप स्थिती"), "ndma", "National Centre for Coastal Research shoreline change atlas."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Tamil Nadu has 74 Geographical Indications under its own name in the GI Registry's list as on 31 December 2025 — 40 handicrafts, 23 agricultural products, 9 foodstuffs and 2 manufactured goods — one of the longest lists of any State; two more, Malabar pepper and Alleppey green cardamom, are shared with Keralam and appear under Keralam in this directory. Salem fabric was among the very first GIs filed in India (2004), and Kancheepuram silk followed the same year. The list spans Thanjavur's paintings, art plates, dolls and veena, Swamimalai bronzes, Madurai's jasmine and sungudi saris, sweets such as Srivilliputtur palkova, Kovilpatti kadalai mittai and Palani panchamirtham, and industrial products such as Dindigul locks and the Coimbatore wet grinder.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में तमिलनाडु के अपने नाम से 74 भौगोलिक संकेतक हैं — 40 हस्तशिल्प, 23 कृषि उत्पाद, 9 खाद्य पदार्थ और 2 विनिर्मित वस्तुएँ — जो किसी भी राज्य की सबसे लंबी सूचियों में है; दो और, मलबार काली मिर्च और अलेप्पी हरी इलायची, केरलम के साथ साझा हैं और इस निर्देशिका में केरलम के अंतर्गत दिखते हैं। सेलम वस्त्र भारत में दर्ज पहले जीआई में था (2004), और उसी वर्ष कांचीपुरम रेशम भी। सूची में तंजावुर की चित्रकला, कला थालियाँ, गुड़ियाँ और वीणा, स्वामीमलै की कांस्य प्रतिमाएँ, मदुरै की चमेली और सुंगुडी साड़ियाँ, श्रीविल्लिपुत्तूर पालकोवा, कोविलपट्टी कडलै मिट्टाई और पलनी पंचामृतम जैसी मिठाइयाँ, और डिंडीगुल ताले व कोयंबटूर वेट ग्राइंडर जैसे औद्योगिक उत्पाद शामिल हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत तमिळनाडूच्या स्वतःच्या नावाने 74 भौगोलिक मानांकने आहेत — 40 हस्तकला, 23 कृषी उत्पादने, 9 खाद्यपदार्थ आणि 2 उत्पादित वस्तू — कोणत्याही राज्याच्या सर्वांत मोठ्या यादींपैकी एक; आणखी दोन, मलबार मिरी आणि अलेप्पी हिरवी वेलची, केरळमसोबत सामायिक असून या सूचीत केरळमखाली दिसतात. सेलम वस्त्र हे भारतात दाखल झालेल्या पहिल्या जीआयपैकी एक होते (2004), आणि त्याच वर्षी कांचीपुरम रेशीमही. यादीत तंजावूरची चित्रकला, कलात्मक ताटे, बाहुल्या आणि वीणा, स्वामीमलैच्या कांस्य मूर्ती, मदुराईचा मोगरा आणि सुंगुडी साड्या, श्रीविल्लिपुत्तूर पालकोवा, कोविलपट्टी कडलै मिट्टाई व पळनी पंचामृतमसारख्या मिठाया, आणि दिंडीगुल कुलपे व कोइंबतूर वेट ग्राइंडरसारखी औद्योगिक उत्पादने आहेत."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
        (L("One District One Product (ODOP) items", "एक ज़िला एक उत्पाद (ओडीओपी)", "एक जिल्हा एक उत्पादन (ओडीओपी)"), "dpiit", "DPIIT ODOP list for Tamil Nadu."),
    ]),
])

# ---------------- T. Tourism ----------------
TV = [("2016", 343812413, 4721978), ("2017", 345061140, 4860455), ("2018", 385909376, 6074345), ("2019", 494865257, 6866327),
      ("2020", 140651241, 1228323), ("2021", 115336719, 57622), ("2022", 218584846, 407126), ("2023", 286011515, 1174899),
      ("2024", 306842014, 1161302), ("2025", 357095556, 1545988)]
tdp = lambda v, y, level="state": dp(v, "visits", y, "calendar", "tourism", TOUR, level=level, rev="provisional" if y == "2025" else "final",
                                     note="Lok Sabha Unstarred Q. 3834, 16 March 2026 (Ministry of Tourism, from State Tourism Departments). 2025 is provisional." if y == "2025" else None)
module(R, "tourism", [
    prose("p1", L(
        "Tamil Nadu is one of India's most visited States. In the Ministry of Tourism's figures it recorded about 35.7 crore domestic tourist visits in 2025 (provisional), up from 30.7 crore in 2024; foreign tourist visits were about 15.5 lakh in 2025, still well below the 68.7 lakh of 2019. Much of the travel is pilgrimage — to Madurai, Rameswaram, Tiruchendur, Palani, Srirangam, Tiruvannamalai, Velankanni and Nagore — alongside the heritage circuit of Mamallapuram, Kanchipuram, Thanjavur and Chettinad, the hill stations of Ooty, Kodaikanal and Yercaud, and Kanniyakumari at the tip of the peninsula.",
        "तमिलनाडु भारत के सबसे ज़्यादा देखे जाने वाले राज्यों में है। पर्यटन मंत्रालय के आँकड़ों में 2025 में यहाँ लगभग 35.7 करोड़ घरेलू पर्यटक यात्राएँ (अनंतिम) दर्ज हुईं, जो 2024 के 30.7 करोड़ से अधिक हैं; विदेशी पर्यटक यात्राएँ 2025 में लगभग 15.5 लाख थीं, जो 2019 के 68.7 लाख से अब भी काफ़ी कम हैं। अधिकांश यात्राएँ तीर्थ हैं — मदुरै, रामेश्वरम, तिरुचेंदूर, पलनी, श्रीरंगम, तिरुवण्णामलै, वेलांकन्नी और नागोर — साथ में मामल्लपुरम, कांचीपुरम, तंजावुर और चेट्टिनाड का धरोहर परिपथ, ऊटी, कोडैकनाल और येरकॉड के हिल स्टेशन, और प्रायद्वीप के छोर पर कन्याकुमारी।",
        "तमिळनाडू हे भारतातील सर्वाधिक भेट दिल्या जाणाऱ्या राज्यांपैकी एक आहे. पर्यटन मंत्रालयाच्या आकडेवारीनुसार 2025 मध्ये येथे सुमारे 35.7 कोटी देशी पर्यटक भेटी (तात्पुरत्या) नोंदल्या गेल्या — 2024 मधील 30.7 कोटींपेक्षा जास्त; परदेशी पर्यटक भेटी 2025 मध्ये सुमारे 15.5 लाख होत्या, 2019 मधील 68.7 लाखांपेक्षा अजूनही बऱ्याच कमी. बहुतेक प्रवास तीर्थयात्रा असतात — मदुराई, रामेश्वरम, तिरुचेंदूर, पळनी, श्रीरंगम, तिरुवण्णामलै, वेलांकण्णी आणि नागोर — सोबत मामल्लपुरम, कांचीपुरम, तंजावूर व चेट्टिनाडचे वारसा परिक्रमा मार्ग, ऊटी, कोडैकनाल व येरकॉडची थंड हवेची ठिकाणे, आणि द्वीपकल्पाच्या टोकावरील कन्याकुमारी."),
        sources=["tourism"], conf="Official"),
    facts("f", [
        fact("dtv", L("Domestic tourist visits", "घरेलू पर्यटक यात्राएँ", "देशी पर्यटक भेटी"), tdp(357095556, "2025"), "count", "neutral",
             previous=tdp(306842014, "2024"), national=tdp(4132840356, "2025", "national")),
        fact("ftv", L("Foreign tourist visits", "विदेशी पर्यटक यात्राएँ", "परदेशी पर्यटक भेटी"), tdp(1545988, "2025"), "count", "neutral",
             previous=tdp(1161302, "2024"), national=tdp(24018320, "2025", "national")),
    ], title=L("Tourist visits", "पर्यटक यात्राएँ", "पर्यटक भेटी")),
    {"type": "series", "id": "tv-series", "title": L("Tourist visits, 2016–2025", "पर्यटक यात्राएँ, 2016–2025", "पर्यटक भेटी, 2016–2025"),
     "kind": "count", "polarity": "neutral",
     "series": [
         {"id": "dtv", "label": L("Domestic", "घरेलू", "देशी"), "points": [tdp(d, y) for y, d, f in TV]},
         {"id": "ftv", "label": L("Foreign", "विदेशी", "परदेशी"), "points": [tdp(f, y) for y, d, f in TV]},
     ],
     "note": L("The fall in 2020–21 reflects the pandemic. Visits are counted by State tourism departments and include repeat visits.",
               "2020–21 की गिरावट महामारी को दर्शाती है। यात्राएँ राज्य पर्यटन विभाग गिनते हैं और इनमें दोबारा की गई यात्राएँ भी शामिल हैं।",
               "2020–21 मधील घसरण महामारीमुळे आहे. भेटी राज्य पर्यटन विभाग मोजतात आणि त्यात पुनर्भेटींचाही समावेश असतो.")},
    lst("places", [
        it3("madurai", "Meenakshi Amman temple, Madurai", "मीनाक्षी अम्मन मंदिर, मदुरै", "मीनाक्षी अम्मन मंदिर, मदुराई", m=("Temple town", "मंदिर नगर", "मंदिरनगरी")),
        it3("mamallapuram", "Mamallapuram (Mahabalipuram)", "मामल्लपुरम (महाबलीपुरम)", "मामल्लपुरम (महाबलीपुरम)", m=("UNESCO heritage, beach", "यूनेस्को धरोहर, समुद्र तट", "युनेस्को वारसा, समुद्रकिनारा")),
        it3("thanjavur", "Thanjavur and the Chola temples", "तंजावुर और चोल मंदिर", "तंजावूर व चोळ मंदिरे", m=("UNESCO heritage", "यूनेस्को धरोहर", "युनेस्को वारसा")),
        it3("rameswaram", "Rameswaram and Dhanushkodi", "रामेश्वरम और धनुषकोडी", "रामेश्वरम व धनुष्कोडी", m=("Pilgrimage, Pamban bridge", "तीर्थ, पंबन पुल", "तीर्थक्षेत्र, पंबन पूल")),
        it3("ooty", "Ooty and the Nilgiri Mountain Railway", "ऊटी और नीलगिरि पर्वतीय रेल", "ऊटी व निलगिरी पर्वतीय रेल्वे", m=("Hill station", "हिल स्टेशन", "थंड हवेचे ठिकाण")),
        it3("kodaikanal", "Kodaikanal", "कोडैकनाल", "कोडैकनाल", m=("Hill station, lake", "हिल स्टेशन, झील", "थंड हवेचे ठिकाण, तलाव")),
        it3("kanyakumari", "Kanniyakumari", "कन्याकुमारी", "कन्याकुमारी", m=("Land's end, Vivekananda Rock", "भूमि का छोर, विवेकानंद शिला", "भूमीचे टोक, विवेकानंद शिला")),
        it3("chettinad", "Chettinad mansions (Karaikudi)", "चेट्टिनाड हवेलियाँ (कराइकुडी)", "चेट्टिनाड वाडे (कराइकुडी)", m=("Architecture, cuisine", "स्थापत्य, व्यंजन", "स्थापत्य, खाद्यपदार्थ")),
        it3("kanchipuram", "Kanchipuram", "कांचीपुरम", "कांचीपुरम", m=("Temples, silk", "मंदिर, रेशम", "मंदिरे, रेशीम")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Chennai: Kapaleeshwarar temple, Marina beach, Fort St George and the Government Museum; a day trip to Mamallapuram.", "चेन्नई: कपालीश्वरर मंदिर, मरीना बीच, फ़ोर्ट सेंट जॉर्ज और सरकारी संग्रहालय; मामल्लपुरम की एक दिन की यात्रा।", "चेन्नई: कपालीश्वरर मंदिर, मरीना किनारा, फोर्ट सेंट जॉर्ज आणि शासकीय संग्रहालय; मामल्लपुरमची एकदिवसीय सहल.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Add Kanchipuram's temples and silk weavers.", "कांचीपुरम के मंदिर और रेशम बुनकर जोड़ें।", "कांचीपुरमची मंदिरे व रेशीम विणकर जोडा.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Temple trail: Thanjavur, Gangaikonda Cholapuram, Kumbakonam, Srirangam and Madurai.", "मंदिर पथ: तंजावुर, गंगैकोंड चोलपुरम, कुंभकोणम, श्रीरंगम और मदुरै।", "मंदिर मार्ग: तंजावूर, गंगैकोंड चोळपुरम, कुंभकोणम, श्रीरंगम व मदुराई.")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Continue from Madurai to Rameswaram and Kanniyakumari, or up to Kodaikanal.", "मदुरै से रामेश्वरम और कन्याकुमारी तक, या कोडैकनाल तक आगे बढ़ें।", "मदुराईहून रामेश्वरम व कन्याकुमारीपर्यंत, किंवा कोडैकनालपर्यंत पुढे जा.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("tt", "Tamil Nadu Tourism (official)", "तमिलनाडु पर्यटन (आधिकारिक)", "तमिळनाडू पर्यटन (अधिकृत)", url="https://www.tamilnadutourism.tn.gov.in", src="tn-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Earnings from tourism", "पर्यटन से आय", "पर्यटनातून उत्पन्न"), "tourism", "State tourism department statistics."),
        (L("Most visited sites (ASI ticketed monuments)", "सबसे अधिक देखे गए स्थल (एएसआई टिकट वाले स्मारक)", "सर्वाधिक भेट दिलेली स्थळे (एएसआय तिकीट स्मारके)"), "asi", "India Tourism Statistics, monument-wise visitors."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Ariyalur", "अरियलूर", "अरियलूर"), ("Chengalpattu", "चेंगलपट्टु", "चेंगलपट्टू"), ("Chennai", "चेन्नई", "चेन्नई"), ("Coimbatore", "कोयंबटूर", "कोइंबतूर"),
    ("Cuddalore", "कडलूर", "कडलूर"), ("Dharmapuri", "धर्मपुरी", "धर्मपुरी"), ("Dindigul", "डिंडीगुल", "दिंडीगुल"), ("Erode", "इरोड", "इरोड"),
    ("Kallakurichi", "कल्लकुरिची", "कल्लकुरिची"), ("Kancheepuram", "कांचीपुरम", "कांचीपुरम"), ("Kanniyakumari", "कन्याकुमारी", "कन्याकुमारी"), ("Karur", "करूर", "करूर"),
    ("Krishnagiri", "कृष्णगिरि", "कृष्णगिरी"), ("Madurai", "मदुरै", "मदुराई"), ("Mayiladuthurai", "मयिलाडुतुरै", "मयिलाडुतुरै"), ("Nagapattinam", "नागपट्टिनम", "नागपट्टिनम"),
    ("Namakkal", "नामक्कल", "नामक्कल"), ("Nilgiris", "नीलगिरि", "निलगिरी"), ("Perambalur", "पेरम्बलूर", "पेरंबलूर"), ("Pudukkottai", "पुदुक्कोट्टै", "पुदुक्कोट्टै"),
    ("Ramanathapuram", "रामनाथपुरम", "रामनाथपुरम"), ("Ranipet", "रानीपेट", "राणीपेट"), ("Salem", "सेलम", "सेलम"), ("Sivaganga", "शिवगंगा", "शिवगंगा"),
    ("Tenkasi", "तेनकासी", "तेनकासी"), ("Thanjavur", "तंजावुर", "तंजावूर"), ("Theni", "थेनी", "थेनी"), ("Thoothukudi", "थूथुकुडी", "थुथुकुडी"),
    ("Tiruchirappalli", "तिरुचिरापल्ली", "तिरुचिरापल्ली"), ("Tirunelveli", "तिरुनेलवेली", "तिरुनेलवेली"), ("Tirupathur", "तिरुपत्तूर", "तिरुपत्तूर"), ("Tiruppur", "तिरुप्पुर", "तिरुप्पूर"),
    ("Tiruvallur", "तिरुवल्लूर", "तिरुवल्लूर"), ("Tiruvannamalai", "तिरुवण्णामलै", "तिरुवण्णामलै"), ("Tiruvarur", "तिरुवारूर", "तिरुवारूर"), ("Vellore", "वेल्लोर", "वेल्लोर"),
    ("Viluppuram", "विलुप्पुरम", "विलुप्पुरम"), ("Virudhunagar", "विरुधुनगर", "विरुधुनगर"),
]
assert len(DISTRICTS) == 38
module(R, "cities", [
    lst("cities", [
        city("chennai", ("Chennai", "चेन्नई", "चेन्नई"), ("State capital (Madras until 1996); port, car and electronics industry, IT corridor, Marina beach and the December music season.", "राज्य की राजधानी (1996 तक मद्रास); बंदरगाह, कार और इलेक्ट्रॉनिक्स उद्योग, आईटी कॉरिडोर, मरीना बीच और दिसंबर का संगीत सीज़न।", "राज्याची राजधानी (1996 पर्यंत मद्रास); बंदर, मोटार व इलेक्ट्रॉनिक्स उद्योग, आयटी कॉरिडॉर, मरीना किनारा आणि डिसेंबरचा संगीत हंगाम."), ("Capital", "राजधानी", "राजधानी")),
        city("coimbatore", ("Coimbatore", "कोयंबटूर", "कोइंबतूर"), ("Textile and engineering hub — pumps, motors, wet grinders — and gateway to the Nilgiris.", "कपड़ा और इंजीनियरिंग केंद्र — पंप, मोटर, वेट ग्राइंडर — और नीलगिरि का प्रवेश द्वार।", "कापड व अभियांत्रिकी केंद्र — पंप, मोटर, वेट ग्राइंडर — आणि निलगिरीचे प्रवेशद्वार."), ("Industry", "उद्योग", "उद्योग")),
        city("madurai", ("Madurai", "मदुरै", "मदुराई"), ("Ancient Pandya capital around the Meenakshi temple; jasmine and sungudi saris.", "मीनाक्षी मंदिर के चारों ओर बसी प्राचीन पांड्य राजधानी; चमेली और सुंगुडी साड़ियाँ।", "मीनाक्षी मंदिराभोवती वसलेली प्राचीन पांड्य राजधानी; मोगरा व सुंगुडी साड्या."), ("Temple city", "मंदिर नगर", "मंदिरनगरी")),
        city("trichy", ("Tiruchirappalli", "तिरुचिरापल्ली", "तिरुचिरापल्ली"), ("Rock Fort temple and Srirangam on the Kaveri; BHEL and education hub.", "कावेरी तट पर रॉक फ़ोर्ट मंदिर और श्रीरंगम; भेल और शिक्षा केंद्र।", "कावेरीकाठी रॉक फोर्ट मंदिर व श्रीरंगम; भेल आणि शिक्षण केंद्र."), ("Delta gateway", "डेल्टा का द्वार", "त्रिभुज प्रदेशाचे द्वार")),
        city("salem", ("Salem", "सेलम", "सेलम"), ("Steel plant, sago and textiles; gateway to Yercaud.", "इस्पात संयंत्र, साबूदाना और कपड़ा; येरकॉड का प्रवेश द्वार।", "पोलाद प्रकल्प, साबुदाणा व कापड; येरकॉडचे प्रवेशद्वार."), ("Industry", "उद्योग", "उद्योग")),
        city("tiruppur", ("Tiruppur", "तिरुप्पुर", "तिरुप्पूर"), ("India's knitwear capital, exporting garments worldwide.", "भारत की निटवियर राजधानी, जहाँ से दुनिया भर में परिधान निर्यात होते हैं।", "भारताची विणलेल्या कपड्यांची राजधानी; जगभर कपडे निर्यात."), ("Knitwear", "निटवियर", "विणलेले कपडे")),
        city("tirunelveli", ("Tirunelveli", "तिरुनेलवेली", "तिरुनेलवेली"), ("Nellaiappar temple, the Thamirabarani and Tirunelveli halwa.", "नेल्लैयप्पर मंदिर, ताम्रपर्णी नदी और तिरुनेलवेली हलवा।", "नेल्लैयप्पर मंदिर, ताम्रपर्णी नदी आणि तिरुनेलवेली हलवा."), ("South", "दक्षिण", "दक्षिण")),
        city("vellore", ("Vellore", "वेल्लोर", "वेल्लोर"), ("Vellore Fort, Christian Medical College and the leather belt.", "वेल्लोर क़िला, क्रिश्चियन मेडिकल कॉलेज और चमड़ा पट्टी।", "वेल्लोर किल्ला, ख्रिश्चन मेडिकल कॉलेज आणि चामडे पट्टा."), ("Health, leather", "स्वास्थ्य, चमड़ा", "आरोग्य, चामडे")),
        city("thoothukudi", ("Thoothukudi", "थूथुकुडी", "थुथुकुडी"), ("Major port, salt pans and pearl-fishing history; the new spaceport nearby.", "बड़ा बंदरगाह, नमक के खेत और मोती निकालने का इतिहास; पास में नया अंतरिक्ष प्रक्षेपण केंद्र।", "मोठे बंदर, मिठागरे आणि मोतीमासेमारीचा इतिहास; जवळच नवे अंतराळ प्रक्षेपण केंद्र."), ("Port", "बंदरगाह", "बंदर")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 38 districts (alphabetical)", "38 ज़िले (वर्णानुक्रम)", "38 जिल्हे (वर्णक्रमानुसार)"), src="tn-des", url=TN23, conf="Official", access=TODAY),
    gaps("g", [
        (L("District populations (Census 2011, adjusted for new districts)", "ज़िलावार जनसंख्या (जनगणना 2011, नए ज़िलों के अनुसार)", "जिल्हानिहाय लोकसंख्या (जनगणना 2011, नव्या जिल्ह्यांनुसार)"), "census", "District Census Handbooks; several districts were created after 2011."),
        (L("Urban agglomeration populations and city tiers", "नगरीय समूह जनसंख्या और शहर श्रेणी", "नागरी समूह लोकसंख्या व शहर श्रेणी"), "census", "Census 2011 UA tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Chennai is India's chess capital. Viswanathan Anand became India's first grandmaster in 1988 and a five-time world champion, and the city has produced a long line of grandmasters since; India hosted the 44th Chess Olympiad at Mamallapuram in 2022. Cricket draws the biggest crowds — the M. A. Chidambaram Stadium at Chepauk is one of the country's oldest Test grounds — and kabaddi, hockey, athletics and squash all have strong followings.\n\nTraditional sports remain part of village festival life: jallikattu, the bull-embracing sport held around Pongal at Alanganallur, Palamedu and Avaniyapuram near Madurai; silambam, the staff-fighting art; and rekla bullock-cart races.",
        "चेन्नई भारत की शतरंज राजधानी है। विश्वनाथन आनंद 1988 में भारत के पहले ग्रैंडमास्टर बने और पाँच बार विश्व चैंपियन रहे, और तब से शहर ने ग्रैंडमास्टरों की लंबी कतार दी है; भारत ने 2022 में मामल्लपुरम में 44वें शतरंज ओलंपियाड की मेज़बानी की। क्रिकेट सबसे बड़ी भीड़ खींचता है — चेपॉक का एम. ए. चिदंबरम स्टेडियम देश के सबसे पुराने टेस्ट मैदानों में है — और कबड्डी, हॉकी, एथलेटिक्स और स्क्वैश के भी बड़े प्रशंसक हैं।\n\nपारंपरिक खेल गाँवों के उत्सवों का हिस्सा बने हुए हैं: जल्लीकट्टु, पोंगल के आसपास मदुरै के पास अलंगनल्लूर, पालमेडु और अवनियापुरम में होने वाला बैल-आलिंगन खेल; सिलंबम, लाठी युद्धकला; और रेकला बैलगाड़ी दौड़।",
        "चेन्नई ही भारताची बुद्धिबळ राजधानी आहे. विश्वनाथन आनंद 1988 मध्ये भारताचे पहिले ग्रँडमास्टर झाले आणि पाच वेळा जगज्जेते ठरले, आणि तेव्हापासून शहराने ग्रँडमास्टरांची मोठी परंपरा दिली आहे; भारताने 2022 मध्ये मामल्लपुरम येथे 44 व्या बुद्धिबळ ऑलिम्पियाडचे यजमानपद भूषवले. क्रिकेटला सर्वाधिक गर्दी होते — चेपॉकचे एम. ए. चिदंबरम स्टेडियम देशातील सर्वांत जुन्या कसोटी मैदानांपैकी एक आहे — आणि कबड्डी, हॉकी, अॅथलेटिक्स व स्क्वॉशचेही मोठे चाहते आहेत.\n\nपारंपरिक खेळ गावांतील उत्सवांचा भाग आहेत: जल्लीकट्टू, पोंगलच्या सुमारास मदुराईजवळ अलंगनल्लूर, पालमेडू व अवनियापुरम येथे होणारा बैल-झुंजीचा खेळ; सिलंबम, काठीयुद्ध कला; आणि रेकला बैलगाडी शर्यती."),
        conf="Editorial"),
    lst("venues", [
        it3("chepauk", "M. A. Chidambaram Stadium (Chepauk), Chennai", "एम. ए. चिदंबरम स्टेडियम (चेपॉक), चेन्नई", "एम. ए. चिदंबरम स्टेडियम (चेपॉक), चेन्नई"),
        it3("jln", "Jawaharlal Nehru Stadium, Chennai", "जवाहरलाल नेहरू स्टेडियम, चेन्नई", "जवाहरलाल नेहरू स्टेडियम, चेन्नई"),
        it3("hockey", "Mayor Radhakrishnan Hockey Stadium, Chennai", "मेयर राधाकृष्णन हॉकी स्टेडियम, चेन्नई", "महापौर राधाकृष्णन हॉकी स्टेडियम, चेन्नई"),
        it3("alanganallur", "Alanganallur jallikattu arena, Madurai", "अलंगनल्लूर जल्लीकट्टु मैदान, मदुरै", "अलंगनल्लूर जल्लीकट्टू मैदान, मदुराई"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [
        (L("Number of chess grandmasters from Tamil Nadu (official)", "तमिलनाडु के शतरंज ग्रैंडमास्टर (आधिकारिक संख्या)", "तमिळनाडूचे बुद्धिबळ ग्रँडमास्टर (अधिकृत संख्या)"), "india-gov", "All India Chess Federation / FIDE records."),
        (L("Sports academies and Khelo India centres", "खेल अकादमियाँ और खेलो इंडिया केंद्र", "क्रीडा अकादमी व खेलो इंडिया केंद्रे"), "india-gov", "Sports Authority of India."),
    ]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("valluvar", ("Thiruvalluvar", "तिरुवल्लुवर", "तिरुवल्लुवर"), ("Poet-philosopher of the Thirukkural, the classic of ethics in 1,330 couplets.", "1,330 दोहों के नीति-ग्रंथ तिरुक्कुरल के कवि-दार्शनिक।", "1,330 द्विपदींच्या तिरुक्कुरळ या नीतिग्रंथाचे कवी-तत्त्वज्ञ."), ("Literature", "साहित्य", "साहित्य")),
        person("rajaraja", ("Rajaraja Chola I", "राजराज चोल प्रथम", "राजराज चोळ पहिला"), ("Chola emperor who built the Brihadisvara temple at Thanjavur.", "चोल सम्राट, जिन्होंने तंजावुर का बृहदीश्वर मंदिर बनवाया।", "तंजावूरचे बृहदीश्वर मंदिर बांधणारा चोळ सम्राट."), ("History", "इतिहास", "इतिहास")),
        person("bharati", ("Subramania Bharati", "सुब्रमण्य भारती", "सुब्रमण्य भारती"), ("Poet of the freedom movement and of social reform.", "स्वतंत्रता आंदोलन और समाज सुधार के कवि।", "स्वातंत्र्यलढा व समाजसुधारणेचे कवी."), ("Literature", "साहित्य", "साहित्य")),
        person("periyar", ("E. V. Ramasamy (Periyar)", "ई. वी. रामासामी (पेरियार)", "ई. व्ही. रामासामी (पेरियार)"), ("Founder of the Self-Respect Movement; campaigned against caste and for women's rights.", "आत्मसम्मान आंदोलन के संस्थापक; जाति के विरुद्ध और महिला अधिकारों के लिए संघर्ष किया।", "स्वाभिमान चळवळीचे संस्थापक; जातीविरोधात व स्त्रीहक्कांसाठी लढा दिला."), ("Reform", "समाज सुधार", "समाजसुधारणा")),
        person("rajaji", ("C. Rajagopalachari", "सी. राजगोपालाचारी", "सी. राजगोपालाचारी"), ("Freedom fighter and the last Governor-General of India (1948–50).", "स्वतंत्रता सेनानी और भारत के अंतिम गवर्नर-जनरल (1948–50)।", "स्वातंत्र्यसैनिक आणि भारताचे शेवटचे गव्हर्नर-जनरल (1948–50)."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("kamaraj", ("K. Kamaraj", "के. कामराज", "के. कामराज"), ("Chief Minister of Madras State (1954–63) who expanded free schooling and school meals.", "मद्रास राज्य के मुख्यमंत्री (1954–63), जिन्होंने निःशुल्क स्कूली शिक्षा और स्कूल भोजन का विस्तार किया।", "मद्रास राज्याचे मुख्यमंत्री (1954–63); मोफत शालेय शिक्षण व शालेय आहाराचा विस्तार केला."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("ramanujan", ("Srinivasa Ramanujan", "श्रीनिवास रामानुजन", "श्रीनिवास रामानुजन"), ("Mathematician from Erode and Kumbakonam whose work on numbers and series still inspires research.", "इरोड और कुंभकोणम के गणितज्ञ, जिनका संख्याओं और श्रेणियों पर काम आज भी शोध को प्रेरित करता है।", "इरोड व कुंभकोणमचे गणितज्ञ; संख्या व श्रेढींवरील त्यांचे कार्य आजही संशोधनाला प्रेरणा देते."), ("Science", "विज्ञान", "विज्ञान")),
        person("raman", ("C. V. Raman", "सी. वी. रामन", "सी. व्ही. रामन"), ("Physicist born at Tiruchirappalli; Nobel Prize in Physics, 1930, for the Raman effect.", "तिरुचिरापल्ली में जन्मे भौतिक विज्ञानी; रामन प्रभाव के लिए 1930 का भौतिकी नोबेल पुरस्कार।", "तिरुचिरापल्लीत जन्मलेले भौतिकशास्त्रज्ञ; रामन परिणामासाठी 1930 चे भौतिकशास्त्राचे नोबेल."), ("Science", "विज्ञान", "विज्ञान")),
        person("mss", ("M. S. Subbulakshmi", "एम. एस. सुब्बुलक्ष्मी", "एम. एस. सुब्बुलक्ष्मी"), ("Carnatic vocalist; the first musician to receive the Bharat Ratna (1998).", "कर्नाटक गायिका; भारत रत्न पाने वाली पहली संगीतकार (1998)।", "कर्नाटक गायिका; भारतरत्न मिळालेल्या पहिल्या संगीतकार (1998)."), ("Music", "संगीत", "संगीत")),
        person("kalam", ("A. P. J. Abdul Kalam", "ए. पी. जे. अब्दुल कलाम", "ए. पी. जे. अब्दुल कलाम"), ("Aerospace scientist from Rameswaram; 11th President of India (2002–07).", "रामेश्वरम के एयरोस्पेस वैज्ञानिक; भारत के 11वें राष्ट्रपति (2002–07)।", "रामेश्वरमचे अवकाश-वैज्ञानिक; भारताचे 11 वे राष्ट्रपती (2002–07)."), ("Science, public life", "विज्ञान, सार्वजनिक जीवन", "विज्ञान, सार्वजनिक जीवन")),
        person("swaminathan", ("M. S. Swaminathan", "एम. एस. स्वामीनाथन", "एम. एस. स्वामीनाथन"), ("Agricultural scientist central to India's Green Revolution.", "भारत की हरित क्रांति के केंद्रीय कृषि वैज्ञानिक।", "भारताच्या हरितक्रांतीतील केंद्रस्थानी असलेले कृषिशास्त्रज्ञ."), ("Science", "विज्ञान", "विज्ञान")),
        person("anand", ("Viswanathan Anand", "विश्वनाथन आनंद", "विश्वनाथन आनंद"), ("India's first chess grandmaster (1988) and five-time world champion.", "भारत के पहले शतरंज ग्रैंडमास्टर (1988) और पाँच बार के विश्व चैंपियन।", "भारताचे पहिले बुद्धिबळ ग्रँडमास्टर (1988) आणि पाच वेळा जगज्जेते."), ("Sport", "खेल", "क्रीडा")),
        person("rahman", ("A. R. Rahman", "ए. आर. रहमान", "ए. आर. रहमान"), ("Composer; two Academy Awards (2009).", "संगीतकार; दो अकादमी पुरस्कार (2009)।", "संगीतकार; दोन अकादमी पुरस्कार (2009)."), ("Music, cinema", "संगीत, सिनेमा", "संगीत, चित्रपट")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "The Tamil diaspora is one of the oldest and most widespread from India. In the 19th and early 20th centuries, workers from the Tamil country went to plantations and public works in Sri Lanka, Malaya, Burma, Mauritius, South Africa, Fiji and the Caribbean, and many communities there still speak Tamil; it is one of the four official languages of Singapore. Since the 1970s many have gone to work in the Gulf, and professionals — especially engineers, doctors and IT specialists — have settled in North America, the United Kingdom, Australia and Europe. The State government has a department for the welfare of non-resident Tamils.",
        "तमिल प्रवासी समुदाय भारत से सबसे पुराने और सबसे व्यापक प्रवासी समुदायों में है। 19वीं और 20वीं सदी के शुरुआती दौर में तमिल देश के मज़दूर श्रीलंका, मलाया, बर्मा, मॉरीशस, दक्षिण अफ़्रीका, फ़िजी और कैरिबियन के बागानों और सार्वजनिक निर्माण कार्यों में गए, और वहाँ के कई समुदाय आज भी तमिल बोलते हैं; यह सिंगापुर की चार राजभाषाओं में से एक है। 1970 के दशक से बहुत से लोग खाड़ी देशों में काम करने गए, और पेशेवर — ख़ासकर इंजीनियर, डॉक्टर और आईटी विशेषज्ञ — उत्तरी अमेरिका, ब्रिटेन, ऑस्ट्रेलिया और यूरोप में बस गए हैं। राज्य सरकार में अनिवासी तमिलों के कल्याण के लिए एक विभाग है।",
        "तमिळ परदेशस्थ समुदाय भारतातील सर्वांत जुन्या व व्यापक समुदायांपैकी आहे. एकोणिसाव्या व विसाव्या शतकाच्या सुरुवातीला तमिळ प्रदेशातील मजूर श्रीलंका, मलाया, ब्रह्मदेश, मॉरिशस, दक्षिण आफ्रिका, फिजी आणि कॅरिबियनमधील मळे व सार्वजनिक बांधकामांवर गेले, आणि तिथले अनेक समुदाय आजही तमिळ बोलतात; सिंगापूरच्या चार राजभाषांपैकी ती एक आहे. 1970 च्या दशकापासून अनेक जण आखाती देशांत कामाला गेले, आणि व्यावसायिक — विशेषतः अभियंते, डॉक्टर व आयटी तज्ज्ञ — उत्तर अमेरिका, ब्रिटन, ऑस्ट्रेलिया आणि युरोपात स्थायिक झाले आहेत. राज्य सरकारमध्ये अनिवासी तमिळांच्या कल्याणासाठी विभाग आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants by destination", "गंतव्यवार प्रवासियों की संख्या", "गंतव्यनिहाय स्थलांतरितांची संख्या"), "india-gov", "Ministry of External Affairs / Tamil Nadu Migration Survey."),
        (L("Official link: non-resident Tamils welfare department", "आधिकारिक लिंक: अनिवासी तमिल कल्याण विभाग", "अधिकृत दुवा: अनिवासी तमिळ कल्याण विभाग"), "tn-gov", "Add the department's verified web address."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Tamil Nadu portal", "तमिलनाडु सरकार पोर्टल", "तमिळनाडू शासन संकेतस्थळ", url="https://www.tn.gov.in", src="tn-gov"),
        it3("esevai", "TN e-Sevai — certificates and services", "टीएन ई-सेवै — प्रमाणपत्र और सेवाएँ", "टीएन ई-सेवै — प्रमाणपत्रे व सेवा", url="https://www.tnesevai.tn.gov.in", src="tn-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Tamil Nadu Tourism", "तमिलनाडु पर्यटन", "तमिळनाडू पर्यटन", url="https://www.tamilnadutourism.tn.gov.in", src="tn-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Chennai", "चेन्नई", "चेन्नई"), "044"], [L("Coimbatore", "कोयंबटूर", "कोइंबतूर"), "0422"], [L("Madurai", "मदुरै", "मदुराई"), "0452"],
           [L("Tiruchirappalli", "तिरुचिरापल्ली", "तिरुचिरापल्ली"), "0431"], [L("Salem", "सेलम", "सेलम"), "0427"], [L("Tirunelveli", "तिरुनेलवेली", "तिरुनेलवेली"), "0462"],
           [L("Vellore", "वेल्लोर", "वेल्लोर"), "0416"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("Verified local business directory (MSMEs, co-operatives, FPOs, artisan clusters)", "सत्यापित स्थानीय व्यवसाय निर्देशिका (एमएसएमई, सहकारी, एफ़पीओ, कारीगर क्लस्टर)", "पडताळलेली स्थानिक उद्योग सूची (एमएसएमई, सहकारी संस्था, एफपीओ, कारागीर समूह)"), "india-gov", "Udyam Registration, co-operative registrars and handloom clusters."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("ramsar", ("Tamil Nadu has 20 Ramsar wetlands — more than any other State.", "तमिलनाडु में 20 रामसर आर्द्रभूमियाँ हैं — किसी भी अन्य राज्य से अधिक।", "तमिळनाडूत 20 रामसर पाणथळ स्थळे आहेत — इतर कोणत्याही राज्यापेक्षा जास्त."), RAMSAR, "indian-wetlands"),
        triv("pamban", ("The New Pamban bridge to Rameswaram (2025) is India's first vertical-lift sea bridge; its span rises 17 m to let ships through.", "रामेश्वरम का नया पंबन पुल (2025) भारत का पहला वर्टिकल-लिफ़्ट समुद्री पुल है; जहाज़ों के लिए इसका स्पैन 17 मीटर ऊपर उठता है।", "रामेश्वरमचा नवा पंबन पूल (2025) हा भारतातील पहिला उभा उचलला जाणारा सागरी पूल आहे; जहाजांसाठी त्याचा गाळा 17 मीटर वर उचलला जातो."), PAMBAN, "pmindia"),
        triv("salem", ("Salem fabric was filed as a GI in February 2004, among the very first in India.", "सेलम वस्त्र फ़रवरी 2004 में जीआई के रूप में दर्ज हुआ — भारत के बिल्कुल पहले जीआई में।", "सेलम वस्त्र फेब्रुवारी 2004 मध्ये जीआय म्हणून दाखल झाले — भारतातील अगदी पहिल्या जीआयपैकी एक."), GI_PDF, "gi-registry"),
        triv("nmr", ("Tamil Nadu was one of only six States and UTs to have met the SDG target for neonatal mortality in SRS 2021.", "एसआरएस 2021 में तमिलनाडु नवजात मृत्यु दर का एसडीजी लक्ष्य पा चुके केवल छह राज्यों/केंद्र शासित प्रदेशों में था।", "एसआरएस 2021 नुसार नवजात मृत्युदराचे एसडीजी उद्दिष्ट गाठलेल्या केवळ सहा राज्य/केंद्रशासित प्रदेशांपैकी तमिळनाडू एक होते."), SRS, "srs"),
        triv("classical", ("Tamil was the first language to be declared a classical language by the Government of India, in 2004.", "2004 में भारत सरकार द्वारा शास्त्रीय भाषा घोषित होने वाली पहली भाषा तमिल थी।", "2004 मध्ये भारत सरकारने अभिजात भाषा म्हणून घोषित केलेली पहिली भाषा तमिळ होती.")),
        triv("chess", ("India's first chess grandmaster, Viswanathan Anand, is from Chennai, and Mamallapuram hosted the 2022 Chess Olympiad.", "भारत के पहले शतरंज ग्रैंडमास्टर विश्वनाथन आनंद चेन्नई से हैं, और मामल्लपुरम ने 2022 के शतरंज ओलंपियाड की मेज़बानी की।", "भारताचे पहिले बुद्धिबळ ग्रँडमास्टर विश्वनाथन आनंद चेन्नईचे आहेत, आणि मामल्लपुरमने 2022 च्या बुद्धिबळ ऑलिम्पियाडचे यजमानपद भूषवले.")),
        triv("kallanai", ("The Grand Anicut (Kallanai) on the Kaveri, attributed to the early Chola king Karikalan, is among the oldest water-regulation structures still in use.", "कावेरी पर ग्रैंड अनिकट (कल्लणै), जिसका श्रेय आरंभिक चोल राजा करिकालन को दिया जाता है, आज भी उपयोग में आने वाली सबसे पुरानी जल-नियमन संरचनाओं में है।", "कावेरीवरील ग्रँड अनिकट (कल्लणै), ज्याचे श्रेय प्रारंभिक चोळ राजा करिकालनला दिले जाते, आजही वापरात असलेल्या सर्वांत जुन्या जलनियंत्रण रचनांपैकी एक आहे.")),
        triv("nilgiri", ("The Nilgiri Mountain Railway climbs to Ooty on a rack-and-pinion track, the only one of its kind in India.", "नीलगिरि पर्वतीय रेल रैक-एंड-पिनियन पटरी पर ऊटी तक चढ़ती है — भारत में अपनी तरह की इकलौती।", "निलगिरी पर्वतीय रेल्वे दातेरी रुळांवरून ऊटीपर्यंत चढते — भारतातील अशा प्रकारची एकमेव.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("tn mod3 ok")
