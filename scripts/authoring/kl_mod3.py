import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-KL"
KL_SPB = "https://spb.kerala.gov.in/economic-review/ER2015/Chapter1/chapter01.html"
PRS = "https://prsindia.org/billtrack/the-kerala-alteration-of-name-bill-2026"
VIZ = "https://www.newsonair.gov.in/pm-modi-to-dedicate-vizhinjam-international-port-indias-1st-semi-automated-port/"
kl = read("regions/IN-KL.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Keralam is one of India's greenest States: forest cover was about 56.8% of its area in ISFR 2023, against 21.8% nationally. Most of the forest lies along the Western Ghats, a UNESCO World Heritage biodiversity hotspot, ranging from tropical wet evergreen forest to the high-altitude shola grasslands where the Nilgiri tahr lives. Silent Valley holds one of the last undisturbed rainforests in the peninsula, and the Neelakurinji shrub blankets the Munnar hills in blue roughly once every twelve years.\n\nThe coast has mangroves, lagoons and three Ramsar wetlands — Vembanad-Kol, Ashtamudi and Sasthamkotta. Periyar and Parambikulam are tiger reserves, and the Ghats forests also hold one of India's largest elephant populations.",
        "केरलम भारत के सबसे हरे-भरे राज्यों में है: आईएसएफ़आर 2023 में इसके लगभग 56.8% क्षेत्र पर वन आवरण था, जबकि राष्ट्रीय स्तर 21.8% है। अधिकांश वन पश्चिमी घाट के साथ हैं, जो यूनेस्को विश्व धरोहर और जैव विविधता हॉटस्पॉट है; यहाँ उष्णकटिबंधीय सदाबहार वनों से लेकर ऊँचाई वाले शोला घास के मैदान तक हैं, जहाँ नीलगिरि ताहर रहता है। साइलेंट वैली प्रायद्वीप के अंतिम अछूते वर्षावनों में से एक है, और नीलकुरिंजी की झाड़ी लगभग हर बारह साल में मुन्नार की पहाड़ियों को नीले रंग से ढक देती है।\n\nतट पर मैंग्रोव, लैगून और तीन रामसर आर्द्रभूमियाँ हैं — वेम्बनाड-कोल, अष्टमुडी और शास्तामकोट्टा। पेरियार और परम्बिकुलम बाघ अभयारण्य हैं, और घाट के वनों में भारत की सबसे बड़ी हाथी आबादियों में से एक भी है।",
        "केरळम हे भारतातील सर्वांत हिरव्यागार राज्यांपैकी एक आहे: आयएसएफआर 2023 नुसार राज्याच्या सुमारे 56.8% क्षेत्रावर वनाच्छादन होते, तर राष्ट्रीय प्रमाण 21.8% आहे. बहुतांश वने पश्चिम घाटालगत आहेत — युनेस्को जागतिक वारसा आणि जैवविविधता हॉटस्पॉट — जिथे उष्णकटिबंधीय सदाहरित वनांपासून उंचावरील शोला गवताळ प्रदेशांपर्यंत विविधता आहे; निलगिरी ताहर याच प्रदेशात राहतो. सायलेंट व्हॅली हे द्वीपकल्पातील शेवटच्या अबाधित वर्षावनांपैकी एक आहे, आणि नीलकुरिंजीचे झुडूप साधारण दर बारा वर्षांनी मुन्नारचे डोंगर निळ्या रंगात न्हाऊन टाकते.\n\nकिनाऱ्यावर खारफुटी, खारकच्छ आणि तीन रामसर पाणथळ स्थळे आहेत — वेंबनाड-कोल, अष्टमुडी आणि शास्तामकोट्टा. पेरियार आणि परंबिकुळम हे व्याघ्र प्रकल्प आहेत, आणि घाटातील वनांत भारतातील सर्वांत मोठ्या हत्ती लोकसंख्येपैकी एक आहे."),
        sources=["fsi", "indian-wetlands", "unesco-whc"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(22059.36, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(21925.94, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), kl["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right")],
          [[L("Vembanad-Kol wetland", "वेम्बनाड-कोल आर्द्रभूमि", "वेंबनाड-कोल पाणथळ"), "19 Aug 2002"],
           [L("Ashtamudi wetland (Kollam)", "अष्टमुडी आर्द्रभूमि (कोल्लम)", "अष्टमुडी पाणथळ (कोल्लम)"), "19 Aug 2002"],
           [L("Sasthamkotta Lake (Kollam)", "शास्तामकोट्टा झील (कोल्लम)", "शास्तामकोट्टा सरोवर (कोल्लम)"), "19 Aug 2002"]],
          "indian-wetlands", RAMSAR, note=L("India has 99 Ramsar sites (list as on 21 April 2026). Areas to be added from the official list.", "भारत में 99 रामसर स्थल हैं (21 अप्रैल 2026 की सूची)। क्षेत्रफल आधिकारिक सूची से जोड़ा जाएगा।", "भारतात 99 रामसर स्थळे आहेत (21 एप्रिल 2026 ची यादी). क्षेत्रफळ अधिकृत यादीतून जोडले जाईल.")),
    lst("protected", [
        it3("periyar", "Periyar Tiger Reserve", "पेरियार बाघ अभयारण्य", "पेरियार व्याघ्र प्रकल्प", m=("Idukki–Pathanamthitta", "इडुक्की–पत्तनमतिट्टा", "इडुक्की–पत्तनमतिट्टा")),
        it3("parambikulam", "Parambikulam Tiger Reserve", "परम्बिकुलम बाघ अभयारण्य", "परंबिकुळम व्याघ्र प्रकल्प", m=("Palakkad", "पालक्काड", "पालक्काड")),
        it3("silent", "Silent Valley National Park", "साइलेंट वैली राष्ट्रीय उद्यान", "सायलेंट व्हॅली राष्ट्रीय उद्यान", m=("Palakkad", "पालक्काड", "पालक्काड")),
        it3("eravikulam", "Eravikulam National Park", "एरविकुलम राष्ट्रीय उद्यान", "एरविकुळम राष्ट्रीय उद्यान", m=("Munnar; Nilgiri tahr", "मुन्नार; नीलगिरि ताहर", "मुन्नार; निलगिरी ताहर")),
        it3("wayanad", "Wayanad Wildlife Sanctuary", "वायनाड वन्यजीव अभयारण्य", "वायनाड वन्यजीव अभयारण्य", m=("Part of the Nilgiri Biosphere Reserve", "नीलगिरि बायोस्फ़ीयर रिज़र्व का भाग", "निलगिरी जीवावरण राखीव क्षेत्राचा भाग")),
        it3("thattekad", "Thattekad Bird Sanctuary", "तट्टेक्काड पक्षी अभयारण्य", "तट्टेक्काड पक्षी अभयारण्य", m=("Ernakulam", "एर्नाकुलम", "एर्णाकुलम")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("elephant", "Asian elephant", "एशियाई हाथी", "आशियाई हत्ती"), it3("tahr", "Nilgiri tahr", "नीलगिरि ताहर", "निलगिरी ताहर"),
        it3("lionmacaque", "Lion-tailed macaque", "शेरपूँछ मकाक (सिंहपुच्छ बंदर)", "सिंहपुच्छ माकड"), it3("hornbill", "Great hornbill", "ग्रेट हॉर्नबिल", "राज धनेश"),
        it3("tiger", "Bengal tiger", "बंगाल बाघ", "पट्टेरी वाघ"), it3("kurinji", "Neelakurinji", "नीलकुरिंजी", "नीलकुरिंजी"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger reserve areas (core, buffer)", "बाघ अभयारण्य क्षेत्रफल (कोर, बफ़र)", "व्याघ्र प्रकल्प क्षेत्र (गाभा, बफर)"), "ntca", "NTCA tiger reserve list."),
        (L("Ramsar site areas", "रामसर स्थलों का क्षेत्रफल", "रामसर स्थळांचे क्षेत्रफळ"), "indian-wetlands", "MoEFCC Ramsar list."),
        (L("National parks and sanctuaries (count, area)", "राष्ट्रीय उद्यान और अभयारण्य (संख्या, क्षेत्रफल)", "राष्ट्रीय उद्याने व अभयारण्ये (संख्या, क्षेत्र)"), "moefcc", "ENVIS / Wildlife Institute of India database."),
        (L("Mangrove cover", "मैंग्रोव आवरण", "खारफुटी आच्छादन"), "fsi", "ISFR 2023, Kerala chapter."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Despite heavy rainfall, water is a seasonal worry in Keralam. The short rivers carry rain to the sea quickly, so summer shortages are common in the midlands, and saline water pushes up the estuaries in the dry months; the Thanneermukkom barrage on Vembanad Lake was built to keep salt water out of the Kuttanad paddy fields, much of which lie below sea level. Open dug wells remain an important household source. The Mullaperiyar dam, on the Periyar in Keralam but operated by Tamil Nadu, has been the subject of a long inter-State dispute.",
        "भारी वर्षा के बावजूद केरलम में पानी मौसमी चिंता है। छोटी नदियाँ बारिश का पानी जल्दी समुद्र तक पहुँचा देती हैं, इसलिए मध्य क्षेत्र में गर्मियों में कमी आम है, और सूखे महीनों में खारा पानी मुहानों में ऊपर चढ़ आता है; वेम्बनाड झील पर थन्नीरमुक्कम बराज कुट्टनाड के धान के खेतों — जिनका बड़ा हिस्सा समुद्र तल से नीचे है — से खारे पानी को दूर रखने के लिए बना। खुले कुएँ आज भी घरों का महत्त्वपूर्ण जल स्रोत हैं। पेरियार पर केरलम में स्थित लेकिन तमिलनाडु द्वारा संचालित मुल्लपेरियार बाँध लंबे अंतर-राज्यीय विवाद का विषय रहा है।",
        "भरपूर पाऊस असूनही केरळममध्ये पाणी ही हंगामी चिंता आहे. लहान नद्या पावसाचे पाणी लवकर समुद्रात वाहून नेतात, त्यामुळे मधल्या पट्ट्यात उन्हाळ्यात टंचाई सामान्य आहे, आणि कोरड्या महिन्यांत खारे पाणी नदीमुखांत वर चढते; कुट्टनाडची भातशेती — जिचा मोठा भाग समुद्रसपाटीखाली आहे — खाऱ्या पाण्यापासून वाचवण्यासाठी वेंबनाड सरोवरावर थण्णीरमुक्कम बंधारा बांधला गेला. उघड्या विहिरी आजही घरगुती पाण्याचा महत्त्वाचा स्रोत आहेत. पेरियार नदीवरील, केरळममध्ये असलेले पण तमिळनाडूकडून चालवले जाणारे मुल्लपेरियार धरण दीर्घ आंतरराज्य वादाचा विषय राहिले आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Large dams (count) and storage", "बड़े बाँध (संख्या) और भंडारण", "मोठी धरणे (संख्या) व साठा"), "kl-gov", "Central Water Commission National Register of Large Dams."),
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "kl-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
        (L("Net irrigated area", "शुद्ध सिंचित क्षेत्र", "निव्वळ सिंचित क्षेत्र"), "kl-spb", "Economic Review / Land Use Statistics."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Keralam's main hazards are monsoon floods and landslides. The floods of August 2018 affected almost every district, and the landslides in Wayanad's Mundakkai–Chooralmala area in July 2024 were among the deadliest in the State's history. The coast faces erosion, rough seas during the monsoon and occasional cyclones such as Ockhi (2017). The State has also handled several outbreaks of Nipah virus since 2018, building rapid contact-tracing and isolation systems.\n\nFor visitors, the main precautions are following ghat-road and beach warnings during the monsoon and checking official alerts before trekking.",
        "केरलम के मुख्य ख़तरे मानसूनी बाढ़ और भूस्खलन हैं। अगस्त 2018 की बाढ़ ने लगभग हर ज़िले को प्रभावित किया, और जुलाई 2024 में वायनाड के मुंडक्कई–चूरलमला क्षेत्र के भूस्खलन राज्य के इतिहास के सबसे घातक भूस्खलनों में थे। तट पर कटाव, मानसून में ऊँची लहरें और कभी-कभी ओखी (2017) जैसे चक्रवात आते हैं। 2018 से राज्य ने निपाह वायरस के कई प्रकोपों का भी सामना किया है और तेज़ संपर्क-अनुरेखण और आइसोलेशन व्यवस्थाएँ बनाई हैं।\n\nपर्यटकों के लिए मुख्य सावधानी मानसून में घाट सड़कों और समुद्र तटों की चेतावनियों का पालन करना और ट्रेकिंग से पहले आधिकारिक अलर्ट देखना है।",
        "केरळममधील प्रमुख धोके म्हणजे मोसमी पूर आणि दरडी. ऑगस्ट 2018 च्या पुराचा जवळपास प्रत्येक जिल्ह्याला फटका बसला, आणि जुलै 2024 मध्ये वायनाडच्या मुंडक्कई–चूरलमला परिसरातील भूस्खलन राज्याच्या इतिहासातील सर्वांत प्राणघातक घटनांपैकी होते. किनाऱ्यावर धूप, पावसाळ्यात खवळलेला समुद्र आणि अधूनमधून ओखीसारखी (2017) चक्रीवादळे येतात. 2018 पासून राज्याने निपाह विषाणूच्या अनेक उद्रेकांनाही तोंड दिले असून जलद संपर्क-शोध आणि विलगीकरण यंत्रणा उभारल्या आहेत.\n\nपर्यटकांसाठी मुख्य काळजी म्हणजे पावसाळ्यात घाटरस्ते व समुद्रकिनाऱ्यांवरील इशाऱ्यांचे पालन करणे आणि ट्रेकिंगपूर्वी अधिकृत सूचना तपासणे."),
        conf="Editorial"),
    emergency_table(("Keralam", "केरलम", "केरळम")),
    lst("links", [
        it3("sdma", "Kerala State Disaster Management Authority", "केरल राज्य आपदा प्रबंधन प्राधिकरण", "केरळ राज्य आपत्ती व्यवस्थापन प्राधिकरण", url="https://sdma.kerala.gov.in", src="kl-gov"),
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Landslide susceptibility zones", "भूस्खलन संवेदनशील क्षेत्र", "दरड प्रवण क्षेत्रे"), "ndma", "GSI / KSDMA hazard maps."),
        (L("Flood-prone area", "बाढ़-प्रवण क्षेत्र", "पूरप्रवण क्षेत्र"), "ndma", "KSDMA flood hazard atlas."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Keralam has 41 registered Geographical Indications in the GI Registry's list as on 31 December 2025, including four shared with neighbouring States (Malabar pepper, Alleppey green cardamom and two monsooned Malabar coffees). Aranmula Kannadi, a hand-cast metal mirror, was among the first GIs registered in India. The list is strong on traditional rice varieties (Navara, Palakkadan Matta, Pokkali, Kaipad and Wayanad's scented rices), handloom saris and dhotis from Balaramapuram, Kuthampully, Chendamangalam and Kasaragod, and crafts such as coir, screw-pine weaving and coconut-shell work.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में केरलम के 41 पंजीकृत भौगोलिक संकेतक हैं, जिनमें चार पड़ोसी राज्यों के साथ साझा हैं (मलबार काली मिर्च, अलेप्पी हरी इलायची और दो मॉनसून्ड मलबार कॉफ़ी)। हाथ से ढाला जाने वाला धातु दर्पण आरनमुला कण्णाडी भारत में पंजीकृत पहले जीआई में था। सूची में पारंपरिक धान की किस्में (नवारा, पालक्काडन मट्टा, पोक्काली, कैपाड और वायनाड के सुगंधित चावल), बलरामपुरम, कुत्ताम्पुल्ली, चेंदमंगलम और कासरगोड की हथकरघा साड़ियाँ और धोतियाँ, तथा नारियल रेशा, केवड़ा बुनाई और नारियल खोल जैसे शिल्प प्रमुख हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत केरळमची 41 नोंदणीकृत भौगोलिक मानांकने आहेत, त्यापैकी चार शेजारी राज्यांसोबत सामायिक आहेत (मलबार मिरी, अलेप्पी हिरवी वेलची आणि दोन मॉन्सून्ड मलबार कॉफी). हाताने ओतलेला धातूचा आरसा, आरनमुळा कण्णाडी, हे भारतात नोंदणी झालेल्या पहिल्या जीआयपैकी एक होते. यादीत पारंपरिक भाताच्या जाती (नवारा, पालक्काडन मट्टा, पोक्काली, कैपाड आणि वायनाडचे सुगंधी तांदूळ), बलरामपुरम, कुत्ताम्पुल्ली, चेंदमंगलम व कासारगोडच्या हातमाग साड्या व धोतरे, आणि काथ्या, केवडा विणकाम आणि करवंटी हस्तकला यांचा मोठा वाटा आहे."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
        (L("One District One Product (ODOP) items", "एक ज़िला एक उत्पाद (ओडीओपी)", "एक जिल्हा एक उत्पादन (ओडीओपी)"), "dpiit", "DPIIT ODOP list for Keralam."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Tourism is one of Keralam's most visible industries, marketed for decades under the \"God's Own Country\" tagline. Visitors come for houseboat cruises on the Alappuzha and Kumarakom backwaters, the tea hills of Munnar and the forests of Thekkady and Wayanad, beaches at Kovalam and Varkala, and the layered history of Fort Kochi and Mattancherry. Ayurveda retreats, temple festivals and the Kochi-Muziris Biennale of contemporary art draw their own audiences.",
        "पर्यटन केरलम के सबसे नज़र आने वाले उद्योगों में है, जिसका दशकों से \"गॉड्स ओन कंट्री\" टैगलाइन के साथ प्रचार होता रहा है। पर्यटक आलप्पुझा और कुमारकोम के बैकवाटर में हाउसबोट सैर, मुन्नार की चाय पहाड़ियों, तेक्कडी और वायनाड के जंगलों, कोवलम और वर्कला के समुद्र तटों, और फ़ोर्ट कोच्चि व मट्टनचेरी के परतदार इतिहास के लिए आते हैं। आयुर्वेद केंद्र, मंदिर उत्सव और समकालीन कला का कोच्चि-मुज़िरिस बिएनाले अपने-अपने दर्शक खींचते हैं।",
        "पर्यटन हा केरळमच्या सर्वांत ठळक उद्योगांपैकी एक आहे; अनेक दशके \"गॉड्स ओन कंट्री\" या घोषवाक्याने त्याचा प्रचार होत आला आहे. पर्यटक अलप्पुझा आणि कुमारकोमच्या बॅकवॉटर्समधील हाऊसबोट सफर, मुन्नारचे चहाचे डोंगर, तेक्कडी व वायनाडची जंगले, कोवळम आणि वर्कलाचे समुद्रकिनारे, आणि फोर्ट कोची व मट्टांचेरीचा बहुपदरी इतिहास पाहण्यासाठी येतात. आयुर्वेद केंद्रे, मंदिरोत्सव आणि समकालीन कलेचे कोची-मुझिरिस बिएनाले यांनाही स्वतंत्र प्रेक्षक लाभतो."),
        conf="Editorial"),
    lst("places", [
        it3("backwaters", "Alappuzha and Kumarakom backwaters", "आलप्पुझा और कुमारकोम बैकवाटर", "अलप्पुझा व कुमारकोम बॅकवॉटर्स", m=("Backwaters", "बैकवाटर", "बॅकवॉटर्स")),
        it3("kochi", "Fort Kochi and Mattancherry", "फ़ोर्ट कोच्चि और मट्टनचेरी", "फोर्ट कोची व मट्टांचेरी", m=("Heritage", "धरोहर", "वारसा")),
        it3("munnar", "Munnar", "मुन्नार", "मुन्नार", m=("Hill station, tea", "हिल स्टेशन, चाय", "थंड हवेचे ठिकाण, चहा")),
        it3("thekkady", "Thekkady (Periyar)", "तेक्कडी (पेरियार)", "तेक्कडी (पेरियार)", m=("Wildlife, spice gardens", "वन्यजीव, मसाला बागान", "वन्यजीव, मसाल्याच्या बागा")),
        it3("wayanad", "Wayanad", "वायनाड", "वायनाड", m=("Forests, Edakkal caves", "जंगल, एडक्कल गुफ़ाएँ", "जंगले, एडक्कल लेणी")),
        it3("beaches", "Kovalam and Varkala", "कोवलम और वर्कला", "कोवळम व वर्कला", m=("Beaches", "समुद्र तट", "समुद्रकिनारे")),
        it3("temples", "Padmanabhaswamy, Guruvayur and Sabarimala", "पद्मनाभस्वामी, गुरुवायूर और सबरीमला", "पद्मनाभस्वामी, गुरुवायूर व शबरीमला", m=("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        it3("bekal", "Bekal Fort", "बेकल क़िला", "बेकल किल्ला", m=("Coastal fort, Kasaragod", "तटीय क़िला, कासरगोड", "किनारी किल्ला, कासारगोड")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Kochi: Fort Kochi, Chinese fishing nets, Mattancherry Palace and the Paradesi Synagogue; a Kathakali performance.", "कोच्चि: फ़ोर्ट कोच्चि, चीनी मछली जाल, मट्टनचेरी महल और परदेसी सिनेगॉग; कथकली प्रदर्शन।", "कोची: फोर्ट कोची, चिनी मासेमारी जाळी, मट्टांचेरी राजवाडा आणि परदेसी सिनेगॉग; कथकलीचा प्रयोग.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Add an overnight houseboat on the Alappuzha backwaters.", "आलप्पुझा बैकवाटर में एक रात हाउसबोट पर जोड़ें।", "अलप्पुझाच्या बॅकवॉटर्समध्ये हाऊसबोटवर एक रात्र जोडा.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Kochi, Munnar's tea hills and Thekkady's forest and spice gardens.", "कोच्चि, मुन्नार की चाय पहाड़ियाँ और तेक्कडी के जंगल व मसाला बागान।", "कोची, मुन्नारचे चहाचे डोंगर आणि तेक्कडीची जंगले व मसाल्याच्या बागा.")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Continue south via the backwaters to Thiruvananthapuram, Kovalam and Varkala.", "बैकवाटर के रास्ते दक्षिण में तिरुवनंतपुरम, कोवलम और वर्कला तक जाएँ।", "बॅकवॉटर्समार्गे दक्षिणेकडे तिरुवनंतपुरम, कोवळम आणि वर्कलापर्यंत जा.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("kt", "Kerala Tourism (official)", "केरल पर्यटन (आधिकारिक)", "केरळ पर्यटन (अधिकृत)", url="https://www.keralatourism.org", src="kl-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits", "घरेलू और विदेशी पर्यटक यात्राएँ", "देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Statistics / Kerala Tourism Statistics (latest year)."),
        (L("Earnings from tourism", "पर्यटन से आय", "पर्यटनातून उत्पन्न"), "tourism", "Kerala Tourism Statistics."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "cities", [
    lst("cities", [
        city("tvm", ("Thiruvananthapuram", "तिरुवनंतपुरम", "तिरुवनंतपुरम"), ("State capital; Padmanabhaswamy temple, Technopark, ISRO's Vikram Sarabhai Space Centre and the new Vizhinjam port.", "राज्य की राजधानी; पद्मनाभस्वामी मंदिर, टेक्नोपार्क, इसरो का विक्रम साराभाई अंतरिक्ष केंद्र और नया विझिंजम बंदरगाह।", "राज्याची राजधानी; पद्मनाभस्वामी मंदिर, टेक्नोपार्क, इस्रोचे विक्रम साराभाई अंतराळ केंद्र आणि नवे विझिंजम बंदर."), ("Capital", "राजधानी", "राजधानी")),
        city("kochi", ("Kochi", "कोच्चि", "कोची"), ("Main port and commercial city; shipyard, naval base, metro and Water Metro, and the Kochi-Muziris Biennale.", "मुख्य बंदरगाह और व्यावसायिक शहर; शिपयार्ड, नौसैनिक अड्डा, मेट्रो और वाटर मेट्रो, और कोच्चि-मुज़िरिस बिएनाले।", "प्रमुख बंदर व व्यापारी शहर; जहाजबांधणी कारखाना, नौदल तळ, मेट्रो व वॉटर मेट्रो, आणि कोची-मुझिरिस बिएनाले."), ("Port, commerce", "बंदरगाह, वाणिज्य", "बंदर, व्यापार")),
        city("kozhikode", ("Kozhikode", "कोझिकोड", "कोझिकोड"), ("Historic Zamorin port; UNESCO City of Literature (2023); halwa and Malabar cuisine.", "ज़मोरिन का ऐतिहासिक बंदरगाह; यूनेस्को साहित्य नगर (2023); हलवा और मलबारी व्यंजन।", "झामोरिनचे ऐतिहासिक बंदर; युनेस्को साहित्य नगरी (2023); हलवा आणि मलबारी पदार्थ."), ("Malabar", "मलबार", "मलबार")),
        city("thrissur", ("Thrissur", "त्रिशूर", "त्रिशूर"), ("Cultural capital; Thrissur Pooram, Kerala Kalamandalam nearby at Cheruthuruthy, gold trade.", "सांस्कृतिक राजधानी; त्रिशूर पूरम, पास में चेरुतुरुत्ती में केरल कलामंडलम, सोने का व्यापार।", "सांस्कृतिक राजधानी; त्रिशूर पूरम, जवळच चेरुतुरुत्ती येथे केरळ कलामंडलम, सोन्याचा व्यापार."), ("Culture", "संस्कृति", "संस्कृती")),
        city("kollam", ("Kollam", "कोल्लम", "कोल्लम"), ("Old trading port; cashew industry; gateway to Ashtamudi Lake.", "पुराना व्यापारिक बंदरगाह; काजू उद्योग; अष्टमुडी झील का प्रवेश द्वार।", "जुने व्यापारी बंदर; काजू उद्योग; अष्टमुडी सरोवराचे प्रवेशद्वार."), ("Cashew, port", "काजू, बंदरगाह", "काजू, बंदर")),
        city("kannur", ("Kannur", "कण्णूर", "कण्णूर"), ("Handloom town and home of Theyyam; St Angelo Fort.", "हथकरघा नगर और थेय्यम की भूमि; सेंट एंजेलो क़िला।", "हातमाग नगरी आणि थेय्यमची भूमी; सेंट अँजेलो किल्ला."), ("Handloom, Theyyam", "हथकरघा, थेय्यम", "हातमाग, थेय्यम")),
        city("alappuzha", ("Alappuzha", "आलप्पुझा", "अलप्पुझा"), ("Canals, coir and houseboats; the Nehru Trophy boat race.", "नहरें, नारियल रेशा और हाउसबोट; नेहरू ट्रॉफ़ी नौका दौड़।", "कालवे, काथ्या आणि हाऊसबोटी; नेहरू ट्रॉफी नौका शर्यत."), ("Backwaters", "बैकवाटर", "बॅकवॉटर्स")),
        city("kottayam", ("Kottayam", "कोट्टयम", "कोट्टयम"), ("Centre of publishing and rubber trade; gateway to Kumarakom.", "प्रकाशन और रबर व्यापार का केंद्र; कुमारकोम का प्रवेश द्वार।", "प्रकाशन व रबर व्यापाराचे केंद्र; कुमारकोमचे प्रवेशद्वार."), ("Print, rubber", "प्रकाशन, रबर", "प्रकाशन, रबर")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z]", "", e.lower()), e, h, m) for e, h, m in [
        ("Thiruvananthapuram", "तिरुवनंतपुरम", "तिरुवनंतपुरम"), ("Kollam", "कोल्लम", "कोल्लम"), ("Pathanamthitta", "पत्तनमतिट्टा", "पत्तनमतिट्टा"),
        ("Alappuzha", "आलप्पुझा", "अलप्पुझा"), ("Kottayam", "कोट्टयम", "कोट्टयम"), ("Idukki", "इडुक्की", "इडुक्की"), ("Ernakulam", "एर्नाकुलम", "एर्णाकुलम"),
        ("Thrissur", "त्रिशूर", "त्रिशूर"), ("Palakkad", "पालक्काड", "पालक्काड"), ("Malappuram", "मलप्पुरम", "मलप्पुरम"), ("Kozhikode", "कोझिकोड", "कोझिकोड"),
        ("Wayanad", "वायनाड", "वायनाड"), ("Kannur", "कण्णूर", "कण्णूर"), ("Kasaragod", "कासरगोड", "कासारगोड")]],
        layout="chips", title=L("The 14 districts (south to north)", "14 ज़िले (दक्षिण से उत्तर)", "14 जिल्हे (दक्षिण ते उत्तर)"), src="kl-spb", url=KL_SPB, conf="Official", access=TODAY),
    gaps("g", [
        (L("District populations (Census 2011)", "ज़िलावार जनसंख्या (जनगणना 2011)", "जिल्हानिहाय लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 A-1 / District Census Handbooks."),
        (L("Urban agglomeration populations and city tiers", "नगरीय समूह जनसंख्या और शहर श्रेणी", "नागरी समूह लोकसंख्या व शहर श्रेणी"), "census", "Census 2011 UA tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Football has a passionate following, especially in Malabar, where sevens tournaments draw big crowds; Kerala has won the national Santosh Trophy several times, and Kerala Blasters FC plays in the Indian Super League at Kochi. Athletics has produced Olympians and Asian Games medallists, P. T. Usha the best known among them. Volleyball, cricket and the traditional snake-boat races are also widely followed, and Kalaripayattu is both a sport and a living martial tradition.",
        "फ़ुटबॉल के प्रति गहरा लगाव है, ख़ासकर मलबार में, जहाँ सेवन्स टूर्नामेंट में भारी भीड़ जुटती है; केरल ने राष्ट्रीय संतोष ट्रॉफ़ी कई बार जीती है, और केरला ब्लास्टर्स एफ़सी कोच्चि से इंडियन सुपर लीग में खेलता है। एथलेटिक्स ने ओलंपियन और एशियाई खेलों के पदक विजेता दिए हैं, जिनमें पी. टी. उषा सबसे प्रसिद्ध हैं। वॉलीबॉल, क्रिकेट और पारंपरिक सर्प-नौका दौड़ भी ख़ूब लोकप्रिय हैं, और कलरीपयट्टु खेल भी है और जीवित युद्ध परंपरा भी।",
        "फुटबॉलचे वेड मोठे आहे, विशेषतः मलबारमध्ये, जिथे सेव्हन्स स्पर्धांना प्रचंड गर्दी होते; केरळने राष्ट्रीय संतोष ट्रॉफी अनेकदा जिंकली आहे आणि केरळा ब्लास्टर्स एफसी कोचीतून इंडियन सुपर लीगमध्ये खेळतो. अॅथलेटिक्सने ऑलिम्पियन आणि आशियाई स्पर्धांतील पदकविजेते दिले आहेत; पी. टी. उषा त्यांतील सर्वांत प्रसिद्ध. व्हॉलीबॉल, क्रिकेट आणि पारंपरिक सर्प-नौका शर्यतीही लोकप्रिय आहेत, आणि कळरीपयट्टू हा खेळही आहे आणि जिवंत युद्धपरंपराही."),
        conf="Editorial"),
    lst("venues", [
        it3("greenfield", "Greenfield International Stadium, Thiruvananthapuram", "ग्रीनफ़ील्ड अंतरराष्ट्रीय स्टेडियम, तिरुवनंतपुरम", "ग्रीनफिल्ड आंतरराष्ट्रीय स्टेडियम, तिरुवनंतपुरम"),
        it3("jln", "Jawaharlal Nehru Stadium, Kochi", "जवाहरलाल नेहरू स्टेडियम, कोच्चि", "जवाहरलाल नेहरू स्टेडियम, कोची"),
        it3("ems", "EMS Stadium, Kozhikode", "ईएमएस स्टेडियम, कोझिकोड", "ईएमएस स्टेडियम, कोझिकोड"),
        it3("punnamada", "Punnamada Lake (Nehru Trophy), Alappuzha", "पुन्नमडा झील (नेहरू ट्रॉफ़ी), आलप्पुझा", "पुन्नमडा सरोवर (नेहरू ट्रॉफी), अलप्पुझा"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [
        (L("Santosh Trophy titles (official count)", "संतोष ट्रॉफ़ी ख़िताब (आधिकारिक संख्या)", "संतोष ट्रॉफी विजेतेपदे (अधिकृत संख्या)"), "india-gov", "All India Football Federation records."),
        (L("Sports academies and Khelo India centres", "खेल अकादमियाँ और खेलो इंडिया केंद्र", "क्रीडा अकादमी व खेलो इंडिया केंद्रे"), "india-gov", "Sports Authority of India."),
    ]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("shankara", ("Adi Shankaracharya", "आदि शंकराचार्य", "आद्य शंकराचार्य"), ("Philosopher of Advaita Vedanta, born at Kalady.", "अद्वैत वेदांत के दार्शनिक, कालडी में जन्मे।", "अद्वैत वेदान्ताचे तत्त्वज्ञ, कालडी येथे जन्म."), ("Philosophy", "दर्शन", "तत्त्वज्ञान")),
        person("swathi", ("Swathi Thirunal", "स्वाति तिरुनाल", "स्वाती तिरुनाळ"), ("19th-century ruler of Travancore and composer of Carnatic music.", "19वीं सदी के त्रावणकोर के शासक और कर्नाटक संगीत के रचनाकार।", "एकोणिसाव्या शतकातील त्रावणकोरचे राजे आणि कर्नाटक संगीताचे रचनाकार."), ("Music", "संगीत", "संगीत")),
        person("ravivarma", ("Raja Ravi Varma", "राजा रवि वर्मा", "राजा रविवर्मा"), ("Painter who brought Indian mythological subjects to oil and print.", "चित्रकार, जिन्होंने भारतीय पौराणिक विषयों को तैलचित्र और छपाई तक पहुँचाया।", "भारतीय पौराणिक विषय तैलचित्र आणि छापचित्रांपर्यंत नेणारे चित्रकार."), ("Art", "कला", "कला")),
        person("narayanaguru", ("Sree Narayana Guru", "श्री नारायण गुरु", "श्री नारायण गुरू"), ("Saint and social reformer: \"one caste, one religion, one God for humankind\".", "संत और समाज सुधारक: \"मनुष्य के लिए एक जाति, एक धर्म, एक ईश्वर\"।", "संत व समाजसुधारक: \"मानवासाठी एक जात, एक धर्म, एक ईश्वर\"."), ("Reform", "समाज सुधार", "समाजसुधारणा")),
        person("ayyankali", ("Ayyankali", "अय्यंकाली", "अय्यंकाळी"), ("Leader of Dalit rights, education and labour struggles in Travancore.", "त्रावणकोर में दलित अधिकार, शिक्षा और श्रमिक संघर्षों के नेता।", "त्रावणकोरमधील दलित हक्क, शिक्षण व कामगार लढ्यांचे नेते."), ("Reform", "समाज सुधार", "समाजसुधारणा")),
        person("narayanan", ("K. R. Narayanan", "के. आर. नारायणन", "के. आर. नारायणन"), ("Tenth President of India (1997–2002).", "भारत के दसवें राष्ट्रपति (1997–2002)।", "भारताचे दहावे राष्ट्रपती (1997–2002)."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("kurien", ("Verghese Kurien", "वर्गीज़ कुरियन", "व्हर्गिस कुरियन"), ("Born in Kozhikode; architect of the White Revolution and the Amul co-operative model.", "कोझिकोड में जन्मे; श्वेत क्रांति और अमूल सहकारी मॉडल के शिल्पकार।", "कोझिकोडमध्ये जन्म; धवलक्रांती आणि अमूल सहकारी प्रारूपाचे शिल्पकार."), ("Co-operatives", "सहकारिता", "सहकार")),
        person("basheer", ("Vaikom Muhammad Basheer", "वैकम मुहम्मद बशीर", "वैकम मुहम्मद बशीर"), ("Malayalam novelist and short-story writer of wit and compassion.", "हास्य और करुणा से भरे मलयालम उपन्यासकार और कहानीकार।", "विनोद आणि करुणेने भरलेले मल्याळम कादंबरीकार व कथाकार."), ("Literature", "साहित्य", "साहित्य")),
        person("kamaladas", ("Kamala Das (Kamala Surayya)", "कमला दास (कमला सुरैया)", "कमला दास (कमला सुरय्या)"), ("Poet in English and Malayalam (as Madhavikutty).", "अंग्रेज़ी और मलयालम (माधविकुट्टी नाम से) की कवयित्री।", "इंग्रजी आणि मल्याळममधील (माधविकुट्टी नावाने) कवयित्री."), ("Literature", "साहित्य", "साहित्य")),
        person("mt", ("M. T. Vasudevan Nair", "एम. टी. वासुदेवन नायर", "एम. टी. वासुदेवन नायर"), ("Novelist and screenwriter; Jnanpith Award 1995.", "उपन्यासकार और पटकथा लेखक; 1995 में ज्ञानपीठ पुरस्कार।", "कादंबरीकार व पटकथाकार; 1995 चा ज्ञानपीठ पुरस्कार."), ("Literature, cinema", "साहित्य, सिनेमा", "साहित्य, चित्रपट")),
        person("usha", ("P. T. Usha", "पी. टी. उषा", "पी. टी. उषा"), ("Sprinter and hurdler; multiple Asian Games and Asian Championships gold medallist.", "धाविका और बाधा दौड़ एथलीट; कई एशियाई खेलों और एशियाई चैंपियनशिप की स्वर्ण पदक विजेता।", "धावपटू व अडथळा शर्यतपटू; अनेक आशियाई स्पर्धा व आशियाई अजिंक्यपद स्पर्धांतील सुवर्णपदक विजेत्या."), ("Sport", "खेल", "क्रीडा")),
        person("yesudas", ("K. J. Yesudas", "के. जे. येसुदास", "के. जे. येसुदास"), ("Playback and classical singer with a career of over six decades.", "छह दशकों से अधिक के करियर वाले पार्श्व और शास्त्रीय गायक।", "सहा दशकांहून अधिक कारकीर्द असलेले पार्श्व व शास्त्रीय गायक."), ("Music", "संगीत", "संगीत")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Emigration has shaped modern Keralam more than almost any other State. Since the oil boom of the 1970s, hundreds of thousands of Keralites have worked in the Gulf countries — as nurses, engineers, drivers, shop staff and construction workers — and many more have settled in Europe, North America and Australia. Remittances built houses and schools across the State, and \"Gulf money\" became part of the culture and literature. The State government's NORKA department and NORKA Roots support emigrants and returnees, and the Loka Kerala Sabha brings diaspora representatives together.",
        "आधुनिक केरलम को प्रवास ने लगभग किसी भी अन्य राज्य से अधिक आकार दिया है। 1970 के दशक के तेल उछाल के बाद से लाखों केरलवासी खाड़ी देशों में काम करते रहे हैं — नर्स, इंजीनियर, ड्राइवर, दुकान कर्मचारी और निर्माण मज़दूर के रूप में — और बहुत से लोग यूरोप, उत्तरी अमेरिका और ऑस्ट्रेलिया में बस गए हैं। भेजे गए पैसों से पूरे राज्य में घर और स्कूल बने, और \"गल्फ़ का पैसा\" संस्कृति और साहित्य का हिस्सा बन गया। राज्य सरकार का नोर्का विभाग और नोर्का रूट्स प्रवासियों और लौटने वालों की सहायता करते हैं, और लोक केरल सभा प्रवासी प्रतिनिधियों को एक मंच पर लाती है।",
        "आधुनिक केरळमला स्थलांतराने इतर जवळपास कोणत्याही राज्यापेक्षा जास्त आकार दिला आहे. 1970 च्या दशकातील तेलतेजीपासून लाखो केरळीय आखाती देशांत काम करत आले आहेत — परिचारिका, अभियंते, चालक, दुकान कर्मचारी आणि बांधकाम कामगार म्हणून — आणि अनेक जण युरोप, उत्तर अमेरिका व ऑस्ट्रेलियात स्थायिक झाले आहेत. पाठवलेल्या पैशांतून राज्यभर घरे आणि शाळा उभ्या राहिल्या, आणि \"गल्फचा पैसा\" संस्कृती व साहित्याचा भाग बनला. राज्य सरकारचा नोर्का विभाग आणि नोर्का रूट्स स्थलांतरित व परतलेल्यांना साहाय्य करतात, आणि लोक केरळ सभा परदेशस्थ प्रतिनिधींना एकत्र आणते."),
        conf="Editorial"),
    lst("links", [
        it3("norka", "NORKA Roots", "नोर्का रूट्स", "नोर्का रूट्स", url="https://norkaroots.kerala.gov.in", src="kl-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Number of emigrants and return migrants", "प्रवासियों और लौटे प्रवासियों की संख्या", "स्थलांतरित व परतलेल्यांची संख्या"), "kl-spb", "Kerala Migration Survey (latest round)."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Kerala portal", "केरल सरकार पोर्टल", "केरळ शासन संकेतस्थळ", url="https://kerala.gov.in", src="kl-gov"),
        it3("edistrict", "e-District Kerala — certificates and services", "ई-डिस्ट्रिक्ट केरल — प्रमाणपत्र और सेवाएँ", "ई-डिस्ट्रिक्ट केरळ — प्रमाणपत्रे व सेवा", url="https://edistrict.kerala.gov.in", src="kl-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Kerala Tourism", "केरल पर्यटन", "केरळ पर्यटन", url="https://www.keralatourism.org", src="kl-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Thiruvananthapuram", "तिरुवनंतपुरम", "तिरुवनंतपुरम"), "0471"], [L("Kochi (Ernakulam)", "कोच्चि (एर्नाकुलम)", "कोची (एर्णाकुलम)"), "0484"],
           [L("Kozhikode", "कोझिकोड", "कोझिकोड"), "0495"], [L("Thrissur", "त्रिशूर", "त्रिशूर"), "0487"], [L("Kollam", "कोल्लम", "कोल्लम"), "0474"],
           [L("Kannur", "कण्णूर", "कण्णूर"), "0497"], [L("Alappuzha", "आलप्पुझा", "अलप्पुझा"), "0477"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("Verified local business directory (MSMEs, co-operatives, FPOs, artisan clusters)", "सत्यापित स्थानीय व्यवसाय निर्देशिका (एमएसएमई, सहकारी, एफ़पीओ, कारीगर क्लस्टर)", "पडताळलेली स्थानिक उद्योग सूची (एमएसएमई, सहकारी संस्था, एफपीओ, कारागीर समूह)"), "india-gov", "Udyam Registration, Kudumbashree and co-operative registrars."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("name", ("Kerala became Keralam on 25 August 2026, two weeks after Parliament passed the renaming bill and more than two years after the Assembly's resolution.",
                      "केरल 25 अगस्त 2026 को केरलम बना — संसद द्वारा नाम परिवर्तन विधेयक पारित होने के दो हफ़्ते बाद और विधानसभा के प्रस्ताव के दो साल से अधिक बाद।",
                      "केरळ 25 ऑगस्ट 2026 रोजी केरळम झाले — संसदेने नावबदल विधेयक मंजूर केल्यानंतर दोन आठवड्यांनी आणि विधानसभेच्या ठरावानंतर दोन वर्षांहून अधिक काळाने."), PRS, "prs"),
        triv("sexratio", ("At the 2011 Census it had 1,084 women per 1,000 men — the highest of any State.", "2011 की जनगणना में यहाँ प्रति 1,000 पुरुषों पर 1,084 महिलाएँ थीं — किसी भी राज्य में सबसे अधिक।", "2011 च्या जनगणनेत येथे दर 1,000 पुरुषांमागे 1,084 स्त्रिया होत्या — सर्व राज्यांत सर्वाधिक."), KL_SPB, "kl-spb"),
        triv("u5mr", ("Its under-five mortality, 8 per 1,000 live births in 2021, is among the lowest in the SRS.", "2021 में यहाँ पाँच वर्ष से कम आयु की मृत्यु दर 8 प्रति 1,000 जीवित जन्म थी — एसआरएस में सबसे कम दरों में से एक।", "2021 मध्ये येथील पाच वर्षांखालील मृत्युदर दर 1,000 जिवंत जन्मांमागे 8 होता — एसआरएसमधील सर्वांत कमी दरांपैकी एक."), SRS, "srs"),
        triv("vizhinjam", ("Vizhinjam is India's first dedicated container transshipment port (2025).", "विझिंजम भारत का पहला समर्पित कंटेनर ट्रांसशिपमेंट बंदरगाह है (2025)।", "विझिंजम हे भारतातील पहिले समर्पित कंटेनर ट्रान्सशिपमेंट बंदर आहे (2025)."), VIZ, "newsonair"),
        triv("aranmula", ("Aranmula Kannadi, a metal mirror, was among the first products to receive a GI in India.", "धातु दर्पण आरनमुला कण्णाडी भारत में जीआई पाने वाले पहले उत्पादों में था।", "धातूचा आरसा आरनमुळा कण्णाडी हा भारतात जीआय मिळालेल्या पहिल्या उत्पादनांपैकी एक होता."), GI_PDF, "gi-registry"),
        triv("monsoon", ("The south-west monsoon usually reaches mainland India first over Keralam.", "दक्षिण-पश्चिम मानसून आम तौर पर भारत की मुख्य भूमि पर सबसे पहले केरलम में पहुँचता है।", "नैर्ऋत्य मोसमी पाऊस साधारणपणे भारताच्या मुख्य भूमीवर सर्वप्रथम केरळममध्ये दाखल होतो.")),
        triv("kuttanad", ("Farmers in Kuttanad grow rice below sea level, behind dykes, on reclaimed backwater land.", "कुट्टनाड के किसान बाँधों के पीछे, बैकवाटर से निकाली गई ज़मीन पर समुद्र तल से नीचे धान उगाते हैं।", "कुट्टनाडचे शेतकरी बांधांच्या आड, बॅकवॉटर्समधून मिळवलेल्या जमिनीवर समुद्रसपाटीखाली भात पिकवतात.")),
        triv("kozhikode", ("Kozhikode became India's first UNESCO City of Literature in 2023.", "कोझिकोड 2023 में भारत का पहला यूनेस्को साहित्य नगर बना।", "कोझिकोड 2023 मध्ये भारताची पहिली युनेस्को साहित्य नगरी बनले.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("kl mod3 ok")
