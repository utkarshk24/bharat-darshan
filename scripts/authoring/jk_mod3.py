"""Jammu and Kashmir (UT) modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-JK"
C = research("census_b5plus.json"); F = C["forest"]["JK"]; J = C["jk_ut"]

RAMSAR_JK = [
    ("Wular Lake", "वुलर झील", "वुलर सरोवर", "1990", "18,900"),
    ("Surinsar-Mansar Lakes", "सुरिनसर-मानसर झीलें", "सुरिनसर-मानसर सरोवरे", "2005", "350"),
    ("Hokera Wetland", "होकरसर आर्द्रभूमि", "होकरसर पाणथळ", "2005", "1,375"),
    ("Hygam Wetland Conservation Reserve", "हायगाम आर्द्रभूमि संरक्षण आरक्षित क्षेत्र", "हायगाम पाणथळ संवर्धन राखीव क्षेत्र", "2022", "802"),
    ("Shallbugh Wetland Conservation Reserve", "शालबुग आर्द्रभूमि संरक्षण आरक्षित क्षेत्र", "शालबुग पाणथळ संवर्धन राखीव क्षेत्र", "2022", "1,675"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Jammu and Kashmir's forests range from subtropical scrub and chir pine in the Jammu foothills to deodar, blue pine, fir and birch in the Pir Panjal and the valley, with alpine meadows (margs) such as Gulmarg, Sonamarg and Tosamaidan above them. ISFR 2023 put its forest cover at 21,346 km², and the J&K Directorate of Economics and Statistics records 20,194 km² of forest area. Dachigam National Park above Srinagar is the last stronghold of the hangul, the Kashmir stag, and also shelters Asiatic black bears and leopards; Kishtwar and Kazinag national parks protect snow leopards and markhor.\n\nThe UT has five Ramsar wetlands: the Wular lake, one of the largest freshwater lakes in India; Hokera (Hokersar), Hygam and Shallbugh in the valley, wintering grounds for migratory ducks and geese; and the Surinsar–Mansar lakes near Jammu. The Dal and Nigeen lakes in Srinagar are famous but face pollution and encroachment.",
        "जम्मू और कश्मीर के वन जम्मू की तलहटी में उपोष्ण झाड़ियों और चीड़ से लेकर पीर पंजाल और घाटी में देवदार, कैल, फ़र और भोजपत्र तक फैले हैं, और उनके ऊपर गुलमर्ग, सोनमर्ग और तोसामैदान जैसे अल्पाइन घास के मैदान (मर्ग) हैं। आईएसएफ़आर 2023 ने इसका वन आवरण 21,346 वर्ग किमी बताया, और जम्मू-कश्मीर अर्थशास्त्र एवं सांख्यिकी निदेशालय 20,194 वर्ग किमी वन क्षेत्र दर्ज करता है। श्रीनगर के ऊपर दाचीगाम राष्ट्रीय उद्यान कश्मीरी बारहसिंगे हंगुल का अंतिम गढ़ है और एशियाई काले भालुओं व तेंदुओं को भी आश्रय देता है; किश्तवाड़ और काज़ीनाग राष्ट्रीय उद्यान हिम तेंदुओं और मारख़ोर को संरक्षण देते हैं।\n\nकेंद्र शासित प्रदेश में पाँच रामसर आर्द्रभूमियाँ हैं: भारत की सबसे बड़ी मीठे पानी की झीलों में से एक वुलर झील; घाटी में होकरसर, हायगाम और शालबुग, जो प्रवासी बत्तखों और हंसों के शीतकालीन ठिकाने हैं; और जम्मू के पास सुरिनसर–मानसर झीलें। श्रीनगर की डल और निगीन झीलें प्रसिद्ध हैं, लेकिन प्रदूषण और अतिक्रमण का सामना करती हैं।",
        "जम्मू व काश्मीरची वने जम्मूच्या पायथ्याशी उपोष्ण झुडपे व चीड पाइनपासून पीर पंजाल व खोऱ्यातील देवदार, ब्लू पाइन, फर व भूर्जपत्रांपर्यंत पसरलेली आहेत, आणि त्यांच्या वर गुलमर्ग, सोनमर्ग व तोसामैदानसारखी अल्पाइन कुरणे (मर्ग) आहेत. आयएसएफआर 2023 नुसार त्याचे वनाच्छादन 21,346 चौ.किमी होते, आणि जम्मू-काश्मीर अर्थशास्त्र व सांख्यिकी संचालनालय 20,194 चौ.किमी वनक्षेत्र नोंदवते. श्रीनगरच्या वरील दाचीगाम राष्ट्रीय उद्यान हे काश्मिरी बारशिंगा हंगुलचा शेवटचा आधार आहे आणि आशियाई काळी अस्वले व बिबट्यांनाही आश्रय देते; किश्तवाड व काझीनाग राष्ट्रीय उद्याने हिमबिबटे व मारखोरचे संरक्षण करतात.\n\nकेंद्रशासित प्रदेशात पाच रामसर पाणथळे आहेत: भारतातील सर्वांत मोठ्या गोड्या पाण्याच्या सरोवरांपैकी एक वुलर सरोवर; खोऱ्यातील होकरसर, हायगाम व शालबुग, जी स्थलांतरित बदके व हंसांची हिवाळी ठिकाणे आहेत; आणि जम्मूजवळील सुरिनसर–मानसर सरोवरे. श्रीनगरची दल व निगीन सरोवरे प्रसिद्ध आहेत, पण प्रदूषण व अतिक्रमणाला तोंड देत आहेत."),
        sources=["fsi", "indian-wetlands", "jk-des"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023. ISFR uses a geographical area of 2,22,236 km² for J&K, which includes areas under the occupation of Pakistan and China, so no percentage is shown."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fa", L("Recorded forest area (2023-24)", "अभिलिखित वन क्षेत्र (2023-24)", "नोंदीकृत वनक्षेत्र (2023-24)"),
             dp(J["forest_area_2023_24_km2"], "km²", "FY2023-24", "fy", "jk-des", J["url"], note="J&K DES, UT at a Glance 2024-25 (Jammu division 12,066 km², Kashmir division 8,128 km²). Recorded forest area is an administrative category, not satellite-measured forest cover."), "number"),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(5, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_JK], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026 (year of designation).", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची (घोषणा वर्ष)।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी (घोषणा वर्ष).")),
    lst("protected", [
        it3("dachigam", "Dachigam National Park", "दाचीगाम राष्ट्रीय उद्यान", "दाचीगाम राष्ट्रीय उद्यान", m=("Hangul", "हंगुल", "हंगुल")),
        it3("kishtwar", "Kishtwar National Park", "किश्तवाड़ राष्ट्रीय उद्यान", "किश्तवाड राष्ट्रीय उद्यान", m=("Snow leopard", "हिम तेंदुआ", "हिमबिबट्या")),
        it3("kazinag", "Kazinag National Park", "काज़ीनाग राष्ट्रीय उद्यान", "काझीनाग राष्ट्रीय उद्यान", m=("Markhor", "मारख़ोर", "मारखोर")),
        it3("wular", "Wular Lake", "वुलर झील", "वुलर सरोवर", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
        it3("hokersar", "Hokersar wetland", "होकरसर आर्द्रभूमि", "होकरसर पाणथळ", m=("Migratory waterfowl", "प्रवासी जलपक्षी", "स्थलांतरित पाणपक्षी")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("hangul", "Hangul (Kashmir stag)", "हंगुल (कश्मीरी बारहसिंगा)", "हंगुल (काश्मिरी बारशिंगा)"), it3("markhor", "Markhor", "मारख़ोर", "मारखोर"),
        it3("snowleopard", "Snow leopard", "हिम तेंदुआ", "हिमबिबट्या"), it3("bear", "Asiatic black bear", "एशियाई काला भालू", "आशियाई काळे अस्वल"),
        it3("chinar", "Chinar", "चिनार", "चिनार"), it3("ducks", "Migratory ducks and geese", "प्रवासी बत्तख और हंस", "स्थलांतरित बदके व हंस"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Hangul population estimate", "हंगुल की अनुमानित संख्या", "हंगुलची अंदाजित संख्या"), "moefcc", "J&K Wildlife Protection Department census."),
        (L("Forest cover as a share of the area under Indian administration", "भारतीय प्रशासन के अधीन क्षेत्र में वन आवरण का हिस्सा", "भारतीय प्रशासनाखालील क्षेत्रातील वनाच्छादनाचा वाटा"), "fsi", "Needs an agreed area basis from FSI or the UT."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "The Jhelum and its tributaries water the Kashmir valley, where an old system of canals (kuls) irrigates paddy and orchards, and the Chenab and Tawi serve the Jammu division. Lakes such as the Dal, Wular and Manasbal are central to the valley's ecology and economy, supporting fisheries, lotus stems (nadru) and floating gardens. The use of the Indus, Jhelum and Chenab is governed by the Indus Waters Treaty of 1960 between India and Pakistan, which India placed in abeyance in April 2025. Floods are a recurring risk: the September 2014 flood submerged much of Srinagar.",
        "झेलम और उसकी सहायक नदियाँ कश्मीर घाटी को सींचती हैं, जहाँ नहरों (कुलों) की पुरानी प्रणाली धान और बाग़ों को पानी देती है, और चिनाब व तवी जम्मू संभाग को सेवा देती हैं। डल, वुलर और मानसबल जैसी झीलें घाटी की पारिस्थितिकी और अर्थव्यवस्था का केंद्र हैं, जो मत्स्य पालन, कमल ककड़ी (नदरू) और तैरते बाग़ों को सहारा देती हैं। सिंधु, झेलम और चिनाब का उपयोग भारत और पाकिस्तान के बीच 1960 की सिंधु जल संधि से नियंत्रित होता है, जिसे भारत ने अप्रैल 2025 में स्थगित कर दिया। बाढ़ बार-बार का ख़तरा है: सितंबर 2014 की बाढ़ में श्रीनगर का बड़ा भाग डूब गया था।",
        "झेलम व तिच्या उपनद्या काश्मीर खोरे भिजवतात, जिथे कालव्यांची (कुलांची) जुनी पद्धत भातशेती व बागांना पाणी देते, आणि चिनाब व तवी जम्मू विभागाला सेवा देतात. दल, वुलर व मानसबलसारखी सरोवरे खोऱ्याच्या परिसंस्थेचे व अर्थव्यवस्थेचे केंद्र आहेत, जी मासेमारी, कमळकाकडी (नदरू) व तरंगत्या बागांना आधार देतात. सिंधू, झेलम व चिनाबचा वापर भारत व पाकिस्तानदरम्यानच्या 1960 च्या सिंधू पाणी कराराने नियंत्रित होतो, जो भारताने एप्रिल 2025 मध्ये स्थगित ठेवला. पूर हा वारंवारचा धोका आहे: सप्टेंबर 2014 च्या पुरात श्रीनगरचा बराच भाग पाण्याखाली गेला होता."),
        conf="Editorial"),
    gaps("g", [
        (L("Indus Waters Treaty — official statement of April 2025", "सिंधु जल संधि — अप्रैल 2025 का आधिकारिक वक्तव्य", "सिंधू पाणी करार — एप्रिल 2025 चे अधिकृत निवेदन"), "india-gov", "MEA / Ministry of Jal Shakti."),
        (L("Dal lake conservation — area and water quality", "डल झील संरक्षण — क्षेत्रफल और जल गुणवत्ता", "दल सरोवर संवर्धन — क्षेत्रफळ व पाण्याची गुणवत्ता"), "india-gov", "J&K Lake Conservation and Management Authority."),
        (L("September 2014 flood — official damage figures", "सितंबर 2014 की बाढ़ — नुकसान के आधिकारिक आँकड़े", "सप्टेंबर 2014 चा पूर — नुकसानाचे अधिकृत आकडे"), "ndma", "NDMA / J&K Disaster Management Department."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Jammu and Kashmir lies in high earthquake zones — the 2005 Kashmir earthquake caused deaths and damage in Uri, Kupwara and Baramulla — and floods, landslides on the Jammu–Srinagar highway, avalanches and heavy snow are seasonal hazards; the highway and the Mughal Road are often closed in winter. The UT also has a long history of militancy, and a large security presence. Visitors should follow official travel advisories, register for the Amarnath Yatra through the official board, and respect restrictions near the Line of Control and international border.",
        "जम्मू और कश्मीर ऊँचे भूकंपीय क्षेत्रों में है — 2005 के कश्मीर भूकंप से उड़ी, कुपवाड़ा और बारामूला में मौतें और नुकसान हुआ — और बाढ़, जम्मू–श्रीनगर राजमार्ग पर भूस्खलन, हिमस्खलन और भारी बर्फ़ मौसमी ख़तरे हैं; सर्दियों में राजमार्ग और मुग़ल रोड अक्सर बंद रहते हैं। केंद्र शासित प्रदेश में उग्रवाद का लंबा इतिहास और सुरक्षा बलों की बड़ी उपस्थिति भी है। आगंतुकों को आधिकारिक यात्रा परामर्श का पालन करना चाहिए, अमरनाथ यात्रा के लिए आधिकारिक बोर्ड से पंजीकरण कराना चाहिए, और नियंत्रण रेखा व अंतरराष्ट्रीय सीमा के पास के प्रतिबंधों का सम्मान करना चाहिए।",
        "जम्मू व काश्मीर उच्च भूकंपप्रवण क्षेत्रांत आहे — 2005 च्या काश्मीर भूकंपामुळे उरी, कुपवाडा व बारामुल्लामध्ये मृत्यू व नुकसान झाले — आणि पूर, जम्मू–श्रीनगर महामार्गावरील भूस्खलन, हिमस्खलन व मुसळधार बर्फवृष्टी हे हंगामी धोके आहेत; हिवाळ्यात महामार्ग व मुघल रोड अनेकदा बंद असतात. केंद्रशासित प्रदेशात दहशतवादाचा दीर्घ इतिहास आणि सुरक्षा दलांची मोठी उपस्थितीही आहे. पर्यटकांनी अधिकृत प्रवास सूचनांचे पालन करावे, अमरनाथ यात्रेसाठी अधिकृत मंडळाकडे नोंदणी करावी, आणि नियंत्रण रेषा व आंतरराष्ट्रीय सीमेजवळील निर्बंधांचा आदर करावा."),
        conf="Editorial"),
    emergency_table(("Jammu and Kashmir", "जम्मू और कश्मीर", "जम्मू व काश्मीर")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Shri Amarnathji Shrine Board — verified registration link", "श्री अमरनाथजी श्राइन बोर्ड — सत्यापित पंजीकरण लिंक", "श्री अमरनाथजी श्राइन बोर्ड — पडताळलेला नोंदणी दुवा"), "india-gov", "Add the official address."),
        (L("Highway status service — verified link", "राजमार्ग स्थिति सेवा — सत्यापित लिंक", "महामार्ग स्थिती सेवा — पडताळलेला दुवा"), "india-gov", "J&K Traffic Police."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Jammu and Kashmir has 24 GIs registered for the UT alone on the GI Registry's list as on 31 December 2025, plus Basmati rice, which it shares with six other States and Union Territories. Most are crafts of the Kashmir valley: Kashmir Pashmina, Kani shawls, sozani and chain-stitch embroidery, crewel, tweed, papier-mâché, walnut-wood carving, khatamband ceilings, hand-knotted carpets, namda and gabba rugs, the wagguv mat, the shikara and the Kashmir willow bat. Kashmir saffron, Mushqbudji rice, Bhaderwah rajmash, Ramban anardana, Ramban sulai honey and Udhampur kaladi are its agricultural and food GIs, and the Basohli painting and Basohli pashmina come from Kathua district.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में केवल जम्मू और कश्मीर के लिए 24 जीआई पंजीकृत हैं, साथ में बासमती चावल, जिसे यह छह अन्य राज्यों और केंद्र शासित प्रदेशों के साथ साझा करता है। अधिकांश कश्मीर घाटी के शिल्प हैं: कश्मीर पश्मीना, कानी शॉल, सोज़नी और चेन स्टिच कढ़ाई, क्रूएल, ट्वीड, पेपर माशी, अखरोट की लकड़ी की नक़्क़ाशी, ख़तमबंद छतें, हाथ से गाँठे क़ालीन, नमदा और गब्बा, वग्गुव चटाई, शिकारा और कश्मीर विलो बल्ला। कश्मीर केसर, मुश्कबुदजी चावल, भद्रवाह राजमाश, रामबन अनारदाना, रामबन सुलाई शहद और उधमपुर कलाड़ी इसके कृषि और खाद्य जीआई हैं, और बसोहली चित्रकला व बसोहली पश्मीना कठुआ ज़िले के हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत केवळ जम्मू व काश्मीरसाठी 24 जीआय नोंदणीकृत आहेत, सोबत बासमती तांदूळ, जो ते इतर सहा राज्ये व केंद्रशासित प्रदेशांसोबत सामायिक करते. बहुतेक काश्मीर खोऱ्यातील हस्तकला आहेत: काश्मीर पश्मीना, कानी शाली, सोझनी व चेन स्टिच भरतकाम, क्रुएल, ट्वीड, पेपर-माशे, अक्रोडाच्या लाकडावरील कोरीवकाम, खतमबंद छते, हाताने विणलेले गालिचे, नमदा व गब्बा, वग्गुव चटई, शिकारा आणि काश्मीर विलो बॅट. काश्मीर केशर, मुश्कबुदजी तांदूळ, भद्रवाह राजमा, रामबन अनारदाणा, रामबन सुलाई मध व उधमपूर कलाडी हे त्याचे कृषी व खाद्य जीआय आहेत, आणि बसोहली चित्रकला व बसोहली पश्मीना कठुआ जिल्ह्यातील आहेत."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Pending GI applications from J&K", "जम्मू-कश्मीर के लंबित जीआई आवेदन", "जम्मू-काश्मीरचे प्रलंबित जीआय अर्ज"), "gi-registry", "GI Registry application status search."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Srinagar is the heart of Kashmir tourism: houseboats and shikara rides on the Dal and Nigeen lakes, the Mughal gardens of Shalimar, Nishat and Chashme Shahi, the Hazratbal shrine, the Shankaracharya temple and the old city's wooden mosques and bazaars, and Asia's largest tulip garden in spring. Gulmarg has a gondola and India's best-known ski slopes; Pahalgam and Sonamarg are bases for treks and for the Amarnath Yatra; and Doodhpathri, Yusmarg and Gurez are quieter valleys. In the Jammu division, Katra is the base for the Vaishno Devi shrine, and Jammu city, Patnitop, Bhaderwah and the Mansar and Surinsar lakes are popular.",
        "श्रीनगर कश्मीर पर्यटन का हृदय है: डल और निगीन झीलों पर हाउसबोट और शिकारा सवारी, शालीमार, निशात और चश्मे शाही के मुग़ल बाग़, हज़रतबल दरगाह, शंकराचार्य मंदिर और पुराने शहर की लकड़ी की मस्जिदें व बाज़ार, और वसंत में एशिया का सबसे बड़ा ट्यूलिप उद्यान। गुलमर्ग में गोंडोला और भारत की सबसे प्रसिद्ध स्की ढलानें हैं; पहलगाम और सोनमर्ग ट्रेक और अमरनाथ यात्रा के आधार हैं; और दूधपथरी, यूसमर्ग और गुरेज़ शांत घाटियाँ हैं। जम्मू संभाग में कटरा वैष्णो देवी धाम का आधार है, और जम्मू शहर, पटनीटॉप, भद्रवाह और मानसर व सुरिनसर झीलें लोकप्रिय हैं।",
        "श्रीनगर हे काश्मीर पर्यटनाचे हृदय आहे: दल व निगीन सरोवरांवर हाउसबोट व शिकारा सफर, शालिमार, निशात व चश्मे शाहीच्या मुघल बागा, हजरतबल दर्गा, शंकराचार्य मंदिर आणि जुन्या शहरातील लाकडी मशिदी व बाजार, आणि वसंतात आशियातील सर्वांत मोठे ट्युलिप उद्यान. गुलमर्गमध्ये गोंडोला व भारतातील सर्वांत प्रसिद्ध स्की उतार आहेत; पहलगाम व सोनमर्ग हे ट्रेक व अमरनाथ यात्रेचे तळ आहेत; आणि दूधपथरी, यूसमर्ग व गुरेझ ही शांत खोरी आहेत. जम्मू विभागात कटरा हे वैष्णोदेवी धामाचे तळ आहे, आणि जम्मू शहर, पटनीटॉप, भद्रवाह व मानसर आणि सुरिनसर सरोवरे लोकप्रिय आहेत."),
        conf="Editorial"),
    lst("places", [
        it3("srinagar", "Srinagar", "श्रीनगर", "श्रीनगर", m=("Dal lake; Mughal gardens", "डल झील; मुग़ल बाग़", "दल सरोवर; मुघल बागा")),
        it3("gulmarg", "Gulmarg", "गुलमर्ग", "गुलमर्ग", m=("Gondola; skiing", "गोंडोला; स्कीइंग", "गोंडोला; स्कीइंग")),
        it3("pahalgam", "Pahalgam", "पहलगाम", "पहलगाम", m=("Lidder valley", "लिद्दर घाटी", "लिद्दर खोरे")),
        it3("sonamarg", "Sonamarg", "सोनमर्ग", "सोनमर्ग", m=("Thajiwas glacier", "थाजीवास हिमनद", "थाजीवास हिमनदी")),
        it3("vaishno", "Vaishno Devi, Katra", "वैष्णो देवी, कटरा", "वैष्णोदेवी, कटरा", m=("Pilgrimage", "तीर्थयात्रा", "तीर्थयात्रा")),
        it3("patnitop", "Patnitop", "पटनीटॉप", "पटनीटॉप", m=("Hill resort", "पर्वतीय स्थल", "थंड हवेचे ठिकाण")),
        it3("gurez", "Gurez", "गुरेज़", "गुरेझ", m=("Remote valley near the LoC", "नियंत्रण रेखा के पास दूरस्थ घाटी", "नियंत्रण रेषेजवळील दुर्गम खोरे")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Srinagar: a night on a houseboat, Mughal gardens and the old city.", "श्रीनगर: हाउसबोट पर एक रात, मुग़ल बाग़ और पुराना शहर।", "श्रीनगर: हाउसबोटवर एक रात्र, मुघल बागा व जुने शहर.")),
        it3("d6", "6 days", "6 दिन", "6 दिवस", d=("Srinagar, Gulmarg, Pahalgam and Sonamarg.", "श्रीनगर, गुलमर्ग, पहलगाम और सोनमर्ग।", "श्रीनगर, गुलमर्ग, पहलगाम व सोनमर्ग.")),
        it3("d4j", "4 days", "4 दिन", "4 दिवस", d=("Jammu, Vaishno Devi from Katra and Patnitop.", "जम्मू, कटरा से वैष्णो देवी और पटनीटॉप।", "जम्मू, कटराहून वैष्णोदेवी व पटनीटॉप.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("jkt", "J&K Tourism (official)", "जम्मू-कश्मीर पर्यटन (आधिकारिक)", "जम्मू-काश्मीर पर्यटन (अधिकृत)", url="https://jktourism.jk.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Tourist and pilgrim arrivals by year", "वर्षवार पर्यटक और तीर्थयात्री आगमन", "वर्षनिहाय पर्यटक व यात्रेकरू आगमन"), "tourism", "J&K Tourism Department; Shri Mata Vaishno Devi Shrine Board."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Anantnag", "अनंतनाग", "अनंतनाग"), ("Bandipora", "बांदीपोरा", "बांदीपोरा"), ("Baramulla", "बारामूला", "बारामुल्ला"), ("Budgam", "बडगाम", "बडगाम"), ("Doda", "डोडा", "डोडा"),
    ("Ganderbal", "गांदरबल", "गांदरबल"), ("Jammu", "जम्मू", "जम्मू"), ("Kathua", "कठुआ", "कठुआ"), ("Kishtwar", "किश्तवाड़", "किश्तवाड"), ("Kulgam", "कुलगाम", "कुलगाम"),
    ("Kupwara", "कुपवाड़ा", "कुपवाडा"), ("Poonch", "पुंछ", "पुंछ"), ("Pulwama", "पुलवामा", "पुलवामा"), ("Rajouri", "राजौरी", "राजौरी"), ("Ramban", "रामबन", "रामबन"),
    ("Reasi", "रियासी", "रियासी"), ("Samba", "सांबा", "सांबा"), ("Shopian", "शोपियाँ", "शोपियां"), ("Srinagar", "श्रीनगर", "श्रीनगर"), ("Udhampur", "उधमपुर", "उधमपूर"),
]
assert len(DISTRICTS) == 20, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("srinagar", ("Srinagar", "श्रीनगर", "श्रीनगर"), ("Summer capital and largest city, on the Jhelum and the Dal lake.", "ग्रीष्मकालीन राजधानी और सबसे बड़ा शहर, झेलम और डल झील के किनारे।", "उन्हाळी राजधानी व सर्वांत मोठे शहर, झेलम व दल सरोवराकाठी."), ("Capital", "राजधानी", "राजधानी")),
        city("jammu", ("Jammu", "जम्मू", "जम्मू"), ("Winter capital; 'city of temples' on the Tawi.", "शीतकालीन राजधानी; तवी किनारे 'मंदिरों का शहर'।", "हिवाळी राजधानी; तवीकाठचे 'मंदिरांचे शहर'."), ("Capital", "राजधानी", "राजधानी")),
        city("anantnag", ("Anantnag", "अनंतनाग", "अनंतनाग"), ("Main town of south Kashmir; springs and Martand.", "दक्षिण कश्मीर का मुख्य नगर; झरने और मार्तंड।", "दक्षिण काश्मीरचे मुख्य शहर; झरे व मार्तंड."), ("Valley", "घाटी", "खोरे")),
        city("baramulla", ("Baramulla", "बारामूला", "बारामुल्ला"), ("Gateway of the Jhelum's exit from the valley.", "घाटी से झेलम के निकास का द्वार।", "खोऱ्यातून झेलम बाहेर पडते ते प्रवेशद्वार."), ("Valley", "घाटी", "खोरे")),
        city("sopore", ("Sopore", "सोपोर", "सोपोर"), ("One of Asia's largest fruit markets.", "एशिया की सबसे बड़ी फल मंडियों में से एक।", "आशियातील सर्वांत मोठ्या फळबाजारांपैकी एक."), ("Horticulture", "बाग़वानी", "फलोत्पादन")),
        city("kathua", ("Kathua", "कठुआ", "कठुआ"), ("Industrial town on the Punjab border.", "पंजाब सीमा पर औद्योगिक नगर।", "पंजाब सीमेवरील औद्योगिक शहर."), ("Industry", "उद्योग", "उद्योग")),
        city("udhampur", ("Udhampur", "उधमपुर", "उधमपूर"), ("Army Northern Command headquarters; kaladi cheese.", "सेना की उत्तरी कमान का मुख्यालय; कलाड़ी।", "लष्कराच्या उत्तर कमांडचे मुख्यालय; कलाडी."), ("Defence", "रक्षा", "संरक्षण")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 20 districts (alphabetical)", "20 ज़िले (वर्णानुक्रम)", "20 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Official district list", "आधिकारिक ज़िला सूची", "अधिकृत जिल्हा यादी"), "jk-des", "J&K DES gives 20 districts, 207 tehsils and 285 blocks."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Winter sports centre on Gulmarg, which has hosted the Khelo India Winter Games, and the skier Arif Khan of Baramulla represented India at the 2022 Winter Olympics in Beijing. Cricket is hugely popular: Parvez Rasool became the first player from J&K to play for India, and the fast bowler Umran Malik from Jammu followed; bats made from Kashmir willow are used around the world. Real Kashmir FC has brought professional football to Srinagar, and the valley has produced champions in wushu, kickboxing and martial arts. The Bakshi Stadium in Srinagar and the Maulana Azad Stadium in Jammu are the main venues.",
        "शीतकालीन खेल गुलमर्ग पर केंद्रित हैं, जिसने खेलो इंडिया शीतकालीन खेलों की मेज़बानी की है, और बारामूला के स्कीयर आरिफ़ ख़ान ने 2022 बीजिंग शीतकालीन ओलंपिक में भारत का प्रतिनिधित्व किया। क्रिकेट बहुत लोकप्रिय है: परवेज़ रसूल भारत के लिए खेलने वाले जम्मू-कश्मीर के पहले खिलाड़ी बने, और उनके बाद जम्मू के तेज़ गेंदबाज़ उमरान मलिक; कश्मीरी विलो से बने बल्ले दुनिया भर में उपयोग होते हैं। रियल कश्मीर एफ़सी श्रीनगर में पेशेवर फ़ुटबॉल लाया है, और घाटी ने वुशु, किकबॉक्सिंग और मार्शल आर्ट्स में चैंपियन दिए हैं। श्रीनगर का बख़्शी स्टेडियम और जम्मू का मौलाना आज़ाद स्टेडियम मुख्य मैदान हैं।",
        "हिवाळी खेळ गुलमर्गवर केंद्रित आहेत, ज्याने खेलो इंडिया हिवाळी स्पर्धांचे यजमानपद भूषवले आहे, आणि बारामुल्लाचा स्कीयर आरिफ खान याने 2022 बीजिंग हिवाळी ऑलिम्पिकमध्ये भारताचे प्रतिनिधित्व केले. क्रिकेट अतिशय लोकप्रिय आहे: परवेझ रसूल भारताकडून खेळणारा जम्मू-काश्मीरचा पहिला खेळाडू ठरला, आणि त्यानंतर जम्मूचा वेगवान गोलंदाज उमरान मलिक; काश्मिरी विलोपासून बनवलेल्या बॅट जगभर वापरल्या जातात. रियल काश्मीर एफसीने श्रीनगरमध्ये व्यावसायिक फुटबॉल आणला आहे, आणि खोऱ्याने वुशु, किकबॉक्सिंग व मार्शल आर्ट्समध्ये विजेते दिले आहेत. श्रीनगरचे बक्षी स्टेडियम व जम्मूचे मौलाना आझाद स्टेडियम ही मुख्य मैदाने आहेत."),
        conf="Editorial"),
    lst("venues", [
        it3("gulmarg", "Gulmarg ski slopes and gondola", "गुलमर्ग स्की ढलान और गोंडोला", "गुलमर्ग स्की उतार व गोंडोला"),
        it3("bakshi", "Bakshi Stadium, Srinagar", "बख़्शी स्टेडियम, श्रीनगर", "बक्षी स्टेडियम, श्रीनगर"),
        it3("maulana", "Maulana Azad Stadium, Jammu", "मौलाना आज़ाद स्टेडियम, जम्मू", "मौलाना आझाद स्टेडियम, जम्मू"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Khelo India Winter Games editions at Gulmarg — official list", "गुलमर्ग में खेलो इंडिया शीतकालीन खेलों के संस्करण — आधिकारिक सूची", "गुलमर्ग येथील खेलो इंडिया हिवाळी स्पर्धांच्या आवृत्त्या — अधिकृत यादी"), "india-gov", "Sports Authority of India.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("lalitaditya", ("Lalitaditya Muktapida", "ललितादित्य मुक्तापीड", "ललितादित्य मुक्तापीड"), ("8th-century king of the Karkota dynasty who built the Martand temple.", "कर्कोट वंश के 8वीं सदी के राजा, जिन्होंने मार्तंड मंदिर बनवाया।", "कर्कोट घराण्याचे आठव्या शतकातील राजे, ज्यांनी मार्तंड मंदिर बांधले."), ("History", "इतिहास", "इतिहास")),
        person("abhinava", ("Abhinavagupta", "अभिनवगुप्त", "अभिनवगुप्त"), ("Philosopher of Kashmir Shaivism and aesthetics (10th–11th century).", "कश्मीर शैव दर्शन और सौंदर्यशास्त्र के दार्शनिक (10वीं–11वीं सदी)।", "काश्मीर शैव तत्त्वज्ञान व सौंदर्यशास्त्राचे तत्त्वज्ञ (दहावे–अकरावे शतक)."), ("Philosophy", "दर्शन", "तत्त्वज्ञान")),
        person("kalhana", ("Kalhana", "कल्हण", "कल्हण"), ("Author of the Rajatarangini, the chronicle of Kashmir's kings (12th century).", "कश्मीर के राजाओं के इतिहास राजतरंगिणी के लेखक (12वीं सदी)।", "काश्मीरच्या राजांचा इतिहास असलेल्या राजतरंगिणीचे लेखक (बारावे शतक)."), ("Literature", "साहित्य", "साहित्य")),
        person("lalded", ("Lal Ded (Lalleshwari)", "लल द्यद (ललेश्वरी)", "लल द्यद (ललेश्वरी)"), ("14th-century mystic poet whose vakhs began Kashmiri literature.", "14वीं सदी की संत कवयित्री, जिनके वाखों से कश्मीरी साहित्य शुरू हुआ।", "चौदाव्या शतकातील संत कवयित्री, जिच्या वाखांनी काश्मिरी साहित्याची सुरुवात झाली."), ("Literature", "साहित्य", "साहित्य")),
        person("nundrishi", ("Sheikh Noor-ud-din (Nund Rishi)", "शेख़ नूरुद्दीन (नुंद ऋषि)", "शेख नूरुद्दीन (नुंद ऋषी)"), ("Sufi saint and poet, founder of the Rishi order; his shrine is at Chrar-i-Sharief.", "सूफ़ी संत और कवि, ऋषि सिलसिले के संस्थापक; उनकी दरगाह चरार-ए-शरीफ़ में है।", "सूफी संत व कवी, ऋषी परंपरेचे संस्थापक; त्यांचा दर्गा चरार-ए-शरीफ येथे आहे."), ("Religion", "धर्म", "धर्म")),
        person("habba", ("Habba Khatoon", "हब्बा ख़ातून", "हब्बा खातून"), ("16th-century poet-queen whose love songs are still sung.", "16वीं सदी की कवयित्री रानी, जिनके प्रेम गीत आज भी गाए जाते हैं।", "सोळाव्या शतकातील कवयित्री राणी, जिची प्रेमगीते आजही गायली जातात."), ("Literature", "साहित्य", "साहित्य")),
        person("zain", ("Zain-ul-Abidin (Budshah)", "ज़ैनुल आबिदीन (बडशाह)", "झैनुल आबिदीन (बडशाह)"), ("15th-century sultan remembered for tolerance and patronage of crafts.", "15वीं सदी के सुल्तान, जिन्हें सहिष्णुता और शिल्पों के संरक्षण के लिए याद किया जाता है।", "पंधराव्या शतकातील सुलतान, ज्यांना सहिष्णुता व हस्तकलांच्या आश्रयासाठी स्मरले जाते."), ("History", "इतिहास", "इतिहास")),
        person("gulab", ("Maharaja Gulab Singh", "महाराजा गुलाब सिंह", "महाराजा गुलाबसिंह"), ("Dogra ruler who became the first Maharaja of Jammu and Kashmir in 1846.", "डोगरा शासक, जो 1846 में जम्मू और कश्मीर के पहले महाराजा बने।", "डोग्रा राज्यकर्ते, जे 1846 मध्ये जम्मू व काश्मीरचे पहिले महाराजा झाले."), ("History", "इतिहास", "इतिहास")),
        person("shivkumar", ("Pandit Shivkumar Sharma", "पंडित शिवकुमार शर्मा", "पंडित शिवकुमार शर्मा"), ("Santoor maestro from Jammu who brought the instrument to the concert stage.", "जम्मू के संतूर वादक, जो इस वाद्य को शास्त्रीय मंच पर लाए।", "जम्मूचे संतूरवादक, ज्यांनी हे वाद्य शास्त्रीय मैफिलीत आणले."), ("Music", "संगीत", "संगीत")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Kashmiri traders in shawls, carpets and dry fruit have long travelled across India and abroad in the winter months. Most Kashmiri Pandits left the valley during the insurgency of 1989–90 and now live in Jammu, Delhi and other cities and countries; their return and resettlement remain a public issue. Families from the region also live in the Gulf, the United Kingdom and North America, and students from J&K study in large numbers in other States.",
        "शॉल, क़ालीन और मेवों के कश्मीरी व्यापारी लंबे समय से सर्दियों के महीनों में भारत भर और विदेश में यात्रा करते रहे हैं। अधिकांश कश्मीरी पंडितों ने 1989–90 के उग्रवाद के दौरान घाटी छोड़ी और अब जम्मू, दिल्ली व अन्य शहरों और देशों में रहते हैं; उनकी वापसी और पुनर्वास एक सार्वजनिक मुद्दा बना हुआ है। इस क्षेत्र के परिवार खाड़ी देशों, ब्रिटेन और उत्तरी अमेरिका में भी रहते हैं, और जम्मू-कश्मीर के छात्र बड़ी संख्या में अन्य राज्यों में पढ़ते हैं।",
        "शाली, गालिचे व सुकामेव्याचे काश्मिरी व्यापारी दीर्घकाळापासून हिवाळ्याच्या महिन्यांत भारतभर व परदेशात प्रवास करत आले आहेत. बहुतेक काश्मिरी पंडितांनी 1989–90 च्या दहशतवादाच्या काळात खोरे सोडले आणि आता ते जम्मू, दिल्ली व इतर शहरांत आणि देशांत राहतात; त्यांचे पुनरागमन व पुनर्वसन हा सार्वजनिक प्रश्न राहिला आहे. या प्रदेशातील कुटुंबे आखाती देश, ब्रिटन व उत्तर अमेरिकेतही राहतात, आणि जम्मू-काश्मीरचे विद्यार्थी मोठ्या संख्येने इतर राज्यांत शिकतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Registered displaced families", "पंजीकृत विस्थापित परिवार", "नोंदणीकृत विस्थापित कुटुंबे"), "india-gov", "J&K Relief and Rehabilitation Commissioner (Migrants)."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Jammu and Kashmir portal", "जम्मू और कश्मीर सरकार पोर्टल", "जम्मू व काश्मीर शासन संकेतस्थळ", url="https://jk.gov.in", src="india-gov"),
        it3("des", "Directorate of Economics and Statistics, J&K", "अर्थशास्त्र एवं सांख्यिकी निदेशालय, जम्मू-कश्मीर", "अर्थशास्त्र व सांख्यिकी संचालनालय, जम्मू-काश्मीर", url="https://ecostatjk.nic.in", src="jk-des"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Srinagar", "श्रीनगर", "श्रीनगर"), "0194"], [L("Jammu", "जम्मू", "जम्मू"), "0191"], [L("Anantnag", "अनंतनाग", "अनंतनाग"), "01932"],
           [L("Baramulla", "बारामूला", "बारामुल्ला"), "01952"], [L("Udhampur", "उधमपुर", "उधमपूर"), "01992"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("chenab", ("The Chenab rail bridge, opened in 2025, is described as the world's highest railway arch bridge.", "2025 में खुले चिनाब रेल पुल को दुनिया का सबसे ऊँचा रेलवे आर्च पुल बताया गया है।", "2025 मध्ये खुल्या झालेल्या चिनाब रेल्वे पुलाचे वर्णन जगातील सर्वांत उंच रेल्वे कमान पूल असे केले जाते."), "https://www.newsonair.gov.in/rail-network-connects-country-from-kashmir-to-kanyakumari-says-pm-modi", "newsonair"),
        triv("ramsar", ("The UT has five Ramsar wetlands; Wular lake was designated in 1990, among India's first.", "केंद्र शासित प्रदेश में पाँच रामसर आर्द्रभूमियाँ हैं; वुलर झील 1990 में घोषित हुई, भारत की पहली में।", "केंद्रशासित प्रदेशात पाच रामसर पाणथळे आहेत; वुलर सरोवर 1990 मध्ये घोषित झाले, भारतातील पहिल्यांपैकी."), RAMSAR, "indian-wetlands"),
        triv("langs", ("Kashmiri, Dogri, Hindi, Urdu and English are all official languages of the UT.", "कश्मीरी, डोगरी, हिंदी, उर्दू और अंग्रेज़ी सभी केंद्र शासित प्रदेश की राजभाषाएँ हैं।", "काश्मिरी, डोगरी, हिंदी, उर्दू व इंग्रजी या सर्व केंद्रशासित प्रदेशाच्या राजभाषा आहेत.")),
        triv("lfpr", (f"{AP['plfs_lfpr_2025']['JK']['female']}% of women aged 15 and above were in the labour force in 2025, against {AP['plfs_lfpr_2025']['IN']['female']}% nationally.", f"2025 में 15 वर्ष से अधिक आयु की {AP['plfs_lfpr_2025']['JK']['female']}% महिलाएँ श्रम बल में थीं, जबकि राष्ट्रीय स्तर पर {AP['plfs_lfpr_2025']['IN']['female']}%।", f"2025 मध्ये 15 वर्षांवरील {AP['plfs_lfpr_2025']['JK']['female']}% स्त्रिया श्रमशक्तीत होत्या, तर राष्ट्रीय पातळीवर {AP['plfs_lfpr_2025']['IN']['female']}%."), MOSPI, "plfs"),
        triv("capitals", ("The UT has two capitals: Srinagar in summer and Jammu in winter.", "केंद्र शासित प्रदेश की दो राजधानियाँ हैं: गर्मियों में श्रीनगर और सर्दियों में जम्मू।", "केंद्रशासित प्रदेशाच्या दोन राजधान्या आहेत: उन्हाळ्यात श्रीनगर व हिवाळ्यात जम्मू.")),
        triv("ls", ("The UT elects 5 members to the Lok Sabha.", "केंद्र शासित प्रदेश से लोकसभा के 5 सदस्य चुने जाते हैं।", "केंद्रशासित प्रदेशातून लोकसभेवर 5 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("jk mod3 ok")
