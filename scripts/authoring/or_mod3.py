"""Odisha modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-OR"
od = read("regions/IN-OR.json")["metrics"]; ind = read("india.json")["metrics"]

RAMSAR_OR = [
    ("Chilika Lake", "चिलिका झील", "चिलिका सरोवर", "1981", "1,16,500"),
    ("Bhitarkanika Mangroves", "भितरकनिका मैंग्रोव", "भितरकनिका खारफुटी", "2002", "65,000"),
    ("Satkosia Gorge", "सतकोसिया घाटी", "सातकोसिया घळ", "2021", "98,197"),
    ("Tampara Lake", "तामपारा झील", "तामपारा सरोवर", "2021", "300"),
    ("Hirakud Reservoir", "हीराकुद जलाशय", "हिराकुड जलाशय", "2021", "65,400"),
    ("Ansupa Lake", "अंशुपा झील", "अंशुपा सरोवर", "2021", "231"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About a third of Odisha — 33.7% in ISFR 2023 — is under forest, from the sal forests of Similipal and the Eastern Ghats to the mangroves of the coast. Similipal, in Mayurbhanj, is a tiger reserve and biosphere reserve known for its waterfalls and melanistic tigers, and Satkosia, where the Mahanadi cuts a gorge through the hills, is the State's second tiger reserve. Bhitarkanika, in the Brahmani–Baitarani delta, has one of India's largest populations of saltwater crocodiles, and the beaches of Gahirmatha, Rushikulya and Devi are among the world's biggest mass-nesting sites of olive ridley sea turtles. Chilika lagoon hosts Irrawaddy dolphins and, in winter, huge flocks of migratory birds.\n\nOdisha has six Ramsar sites: Chilika (designated in 1981), Bhitarkanika, and, from 2021, Satkosia Gorge, Tampara, Hirakud and Ansupa.",
        "ओडिशा का लगभग एक-तिहाई भाग — आईएसएफ़आर 2023 में 33.7% — वनों से ढका है, सिमलीपाल और पूर्वी घाट के साल वनों से लेकर तट के मैंग्रोव तक। मयूरभंज का सिमलीपाल बाघ अभयारण्य और जैवमंडल आरक्षित क्षेत्र है, जो अपने झरनों और काले (मेलानिस्टिक) बाघों के लिए जाना जाता है, और सतकोसिया, जहाँ महानदी पहाड़ियों को काटकर घाटी बनाती है, राज्य का दूसरा बाघ अभयारण्य है। ब्राह्मणी–वैतरणी डेल्टा के भितरकनिका में खारे पानी के मगरमच्छों की भारत की सबसे बड़ी आबादियों में से एक है, और गहिरमाथा, ऋषिकुल्या और देवी के तट ऑलिव रिडले समुद्री कछुओं के विश्व के सबसे बड़े सामूहिक प्रजनन स्थलों में हैं। चिलिका लैगून में इरावदी डॉल्फ़िन रहती हैं और सर्दियों में प्रवासी पक्षियों के विशाल झुंड आते हैं।\n\nओडिशा में छह रामसर स्थल हैं: चिलिका (1981 में घोषित), भितरकनिका, और 2021 से सतकोसिया घाटी, तामपारा, हीराकुद और अंशुपा।",
        "ओडिशाचा सुमारे एक-तृतीयांश भाग — आयएसएफआर 2023 नुसार 33.7% — वनाच्छादित आहे, सिमलीपाल व पूर्व घाटाच्या साल वनांपासून किनाऱ्यावरील खारफुटीपर्यंत. मयूरभंजमधील सिमलीपाल हा व्याघ्र प्रकल्प व जैवमंडल राखीव क्षेत्र आहे, जो धबधबे व काळ्या (मेलॅनिस्टिक) वाघांसाठी ओळखला जातो, आणि सातकोसिया, जिथे महानदी डोंगर कापून घळ बनवते, हा राज्याचा दुसरा व्याघ्र प्रकल्प आहे. ब्राह्मणी–वैतरणी त्रिभुज प्रदेशातील भितरकनिकात खाऱ्या पाण्यातील मगरींची भारतातील सर्वांत मोठ्या संख्यांपैकी एक आहे, आणि गहिरमाथा, ऋषिकुल्या व देवीचे किनारे ऑलिव्ह रिडले सागरी कासवांच्या जगातील सर्वांत मोठ्या सामूहिक अंडी घालण्याच्या स्थळांपैकी आहेत. चिलिका खारकच्छात इरावडी डॉल्फिन आढळतात आणि हिवाळ्यात स्थलांतरित पक्ष्यांचे प्रचंड थवे येतात.\n\nओडिशात सहा रामसर स्थळे आहेत: चिलिका (1981 मध्ये घोषित), भितरकनिका, आणि 2021 पासून सातकोसिया घळ, तामपारा, हिराकुड व अंशुपा."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(52433.56, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(52281.67, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), od["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(6, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_OR], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026 (year of designation). The list prints Chilika as 'Chilka Lake'.", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची (घोषणा वर्ष)। सूची में चिलिका 'Chilka Lake' छपा है।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी (घोषणा वर्ष). यादीत चिलिका 'Chilka Lake' असे छापले आहे.")),
    lst("protected", [
        it3("similipal", "Similipal Tiger Reserve and National Park", "सिमलीपाल बाघ अभयारण्य और राष्ट्रीय उद्यान", "सिमलीपाल व्याघ्र प्रकल्प व राष्ट्रीय उद्यान", m=("Mayurbhanj; biosphere reserve", "मयूरभंज; जैवमंडल आरक्षित क्षेत्र", "मयूरभंज; जैवमंडल राखीव")),
        it3("satkosia", "Satkosia Tiger Reserve", "सतकोसिया बाघ अभयारण्य", "सातकोसिया व्याघ्र प्रकल्प", m=("Mahanadi gorge", "महानदी घाटी", "महानदी घळ")),
        it3("bhitarkanika", "Bhitarkanika National Park", "भितरकनिका राष्ट्रीय उद्यान", "भितरकनिका राष्ट्रीय उद्यान", m=("Mangroves; crocodiles", "मैंग्रोव; मगरमच्छ", "खारफुटी; मगरी")),
        it3("gahirmatha", "Gahirmatha Marine Sanctuary", "गहिरमाथा समुद्री अभयारण्य", "गहिरमाथा सागरी अभयारण्य", m=("Olive ridley nesting", "ऑलिव रिडले प्रजनन", "ऑलिव्ह रिडले अंडी घालणे")),
        it3("chilika", "Chilika Lake (Nalabana Bird Sanctuary)", "चिलिका झील (नलबन पक्षी अभयारण्य)", "चिलिका सरोवर (नलबन पक्षी अभयारण्य)", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
        it3("debrigarh", "Debrigarh Wildlife Sanctuary", "देबरीगढ़ वन्यजीव अभयारण्य", "देब्रिगड वन्यजीव अभयारण्य", m=("Hirakud", "हीराकुद", "हिराकुड")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("ridley", "Olive ridley sea turtle", "ऑलिव रिडले समुद्री कछुआ", "ऑलिव्ह रिडले सागरी कासव"), it3("croc", "Saltwater crocodile", "खारे पानी का मगरमच्छ", "खाऱ्या पाण्यातील मगर"),
        it3("irrawaddy", "Irrawaddy dolphin", "इरावदी डॉल्फ़िन", "इरावडी डॉल्फिन"), it3("tiger", "Tiger", "बाघ", "वाघ"),
        it3("elephant", "Asian elephant", "एशियाई हाथी", "आशियाई हत्ती"), it3("sambar", "Sambar (State animal)", "सांभर (राज्य पशु)", "सांबर (राज्यप्राणी)"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger estimate (Similipal, Satkosia)", "बाघों का अनुमान (सिमलीपाल, सतकोसिया)", "वाघांचा अंदाज (सिमलीपाल, सातकोसिया)"), "ntca", "NTCA All India Tiger Estimation."),
        (L("Olive ridley nesting count by season", "मौसमवार ऑलिव रिडले प्रजनन संख्या", "हंगामनिहाय ऑलिव्ह रिडले अंडी घालण्याची संख्या"), "india-gov", "Odisha Forest Department."),
        (L("Elephant population", "हाथियों की संख्या", "हत्तींची संख्या"), "moefcc", "Project Elephant synchronised census."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Odisha's rivers bring both irrigation and floods. The Hirakud dam on the Mahanadi near Sambalpur, completed in the 1950s, is one of the world's longest earthen dams and irrigates much of western Odisha; Rengali on the Brahmani, Upper Indravati and Upper Kolab irrigate other regions. The deltas of the Mahanadi, Brahmani and Baitarani flood when heavy monsoon rain coincides with high tides, and storm surges during cyclones push sea water inland. Odisha and Chhattisgarh dispute the sharing of the Mahanadi's water, a matter before an inter-State tribunal. Western districts such as Bolangir and Kalahandi have faced recurring drought, and fluoride affects groundwater in some areas.",
        "ओडिशा की नदियाँ सिंचाई और बाढ़ दोनों लाती हैं। संबलपुर के पास महानदी पर 1950 के दशक में पूरा हुआ हीराकुद बाँध दुनिया के सबसे लंबे मिट्टी के बाँधों में से है और पश्चिमी ओडिशा के बड़े भाग की सिंचाई करता है; ब्राह्मणी पर रेंगाली, अपर इंद्रावती और अपर कोलाब अन्य क्षेत्रों की सिंचाई करते हैं। महानदी, ब्राह्मणी और वैतरणी के डेल्टा तब डूबते हैं जब भारी मानसूनी वर्षा और ऊँचा ज्वार एक साथ आते हैं, और चक्रवातों में तूफ़ानी लहरें समुद्री पानी को भीतर धकेलती हैं। महानदी के पानी के बँटवारे पर ओडिशा और छत्तीसगढ़ में विवाद है, जो एक अंतरराज्यीय न्यायाधिकरण के समक्ष है। बलांगीर और कालाहांडी जैसे पश्चिमी ज़िलों ने बार-बार सूखा झेला है, और कुछ क्षेत्रों के भूजल में फ़्लोराइड है।",
        "ओडिशाच्या नद्या सिंचन व पूर दोन्ही आणतात. संबलपूरजवळ महानदीवर 1950 च्या दशकात पूर्ण झालेले हिराकुड धरण हे जगातील सर्वांत लांब मातीच्या धरणांपैकी एक असून पश्चिम ओडिशाच्या मोठ्या भागाला सिंचन देते; ब्राह्मणीवरील रेंगाली, अपर इंद्रावती व अपर कोलाब इतर भागांना सिंचन देतात. महानदी, ब्राह्मणी व वैतरणीचे त्रिभुज प्रदेश मुसळधार मान्सूनी पाऊस व उंच भरती एकत्र आल्यावर पुराखाली जातात, आणि चक्रीवादळांत वादळी लाटा समुद्राचे पाणी आत ढकलतात. महानदीच्या पाणीवाटपावरून ओडिशा व छत्तीसगडमध्ये वाद आहे, जो आंतरराज्य लवादासमोर आहे. बलांगीर व कालाहांडीसारख्या पश्चिमेकडील जिल्ह्यांनी वारंवार दुष्काळ सोसला आहे, आणि काही भागांतील भूजलात फ्लोराइड आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Flood-affected area and population by year", "वर्षवार बाढ़ प्रभावित क्षेत्र और जनसंख्या", "वर्षनिहाय पूरग्रस्त क्षेत्र व लोकसंख्या"), "india-gov", "Odisha Special Relief Commissioner reports."),
        (L("Irrigated area", "सिंचित क्षेत्र", "सिंचित क्षेत्र"), "india-gov", "Odisha Economic Survey / Water Resources Department."),
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Cyclones are Odisha's defining hazard. The super cyclone of October 1999 killed thousands of people. Since then the State has built a network of multipurpose cyclone shelters, set up the Odisha State Disaster Management Authority — the first such body in India — and the Odisha Disaster Rapid Action Force, and perfected mass evacuations; during cyclones Phailin (2013) and Fani (2019) very large numbers of people were moved to safety before landfall. Floods hit the deltas in most monsoons, lightning kills many people each year, and the western districts suffer severe heatwaves in April–May.\n\nVisitors should follow IMD and OSDMA advisories during the cyclone seasons, and crowd advisories at the Rath Yatra in Puri.",
        "चक्रवात ओडिशा का निर्णायक ख़तरा हैं। अक्टूबर 1999 के महाचक्रवात में हज़ारों लोग मारे गए। तब से राज्य ने बहुउद्देशीय चक्रवात आश्रयों का जाल बनाया है, ओडिशा राज्य आपदा प्रबंधन प्राधिकरण — भारत में ऐसी पहली संस्था — और ओडिशा आपदा त्वरित कार्य बल की स्थापना की है, और बड़े पैमाने पर निकासी में दक्षता पाई है; फ़ाइलिन (2013) और फ़ानी (2019) चक्रवातों के दौरान तट से टकराने से पहले बहुत बड़ी संख्या में लोगों को सुरक्षित पहुँचाया गया। अधिकांश मानसूनों में डेल्टाओं में बाढ़ आती है, आकाशीय बिजली से हर साल बहुत लोग मरते हैं, और पश्चिमी ज़िले अप्रैल–मई में भीषण लू झेलते हैं।\n\nपर्यटकों को चक्रवात के मौसम में आईएमडी और ओएसडीएमए की सलाह और पुरी की रथयात्रा में भीड़ संबंधी सलाह माननी चाहिए।",
        "चक्रीवादळे हा ओडिशावरील निर्णायक धोका आहे. ऑक्टोबर 1999 च्या महाचक्रीवादळात हजारो लोक मरण पावले. तेव्हापासून राज्याने बहुउद्देशीय चक्रीवादळ निवाऱ्यांचे जाळे उभारले, ओडिशा राज्य आपत्ती व्यवस्थापन प्राधिकरण — भारतातील अशी पहिली संस्था — व ओडिशा आपत्ती जलद कृती दल स्थापन केले, आणि मोठ्या प्रमाणावरील स्थलांतरात प्रावीण्य मिळवले; फायलिन (2013) व फणी (2019) चक्रीवादळांत किनाऱ्यावर धडकण्यापूर्वी फार मोठ्या संख्येने लोकांना सुरक्षित स्थळी हलवण्यात आले. बहुतेक पावसाळ्यांत त्रिभुज प्रदेशांत पूर येतो, वीज कोसळून दरवर्षी अनेक लोक मरण पावतात, आणि पश्चिमेकडील जिल्हे एप्रिल–मेमध्ये तीव्र उष्णतेची लाट सोसतात.\n\nपर्यटकांनी चक्रीवादळाच्या हंगामात आयएमडी व ओएसडीएमएच्या सूचना आणि पुरीच्या रथयात्रेत गर्दीविषयक सूचना पाळाव्यात."),
        conf="Editorial"),
    emergency_table(("Odisha", "ओडिशा", "ओडिशा")),
    lst("links", [
        it3("imd", "IMD weather and cyclone warnings", "आईएमडी मौसम और चक्रवात चेतावनियाँ", "आयएमडी हवामान व चक्रीवादळ इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("osdma", "Odisha State Disaster Management Authority", "ओडिशा राज्य आपदा प्रबंधन प्राधिकरण", "ओडिशा राज्य आपत्ती व्यवस्थापन प्राधिकरण", url="https://www.osdma.org", src="india-gov"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Deaths in the 1999 super cyclone — official figure", "1999 महाचक्रवात में मृत्यु — आधिकारिक आँकड़ा", "1999 महाचक्रीवादळातील मृत्यू — अधिकृत आकडा"), "ndma", "Government of Odisha / NDMA report."),
        (L("People evacuated in Phailin (2013) and Fani (2019)", "फ़ाइलिन (2013) और फ़ानी (2019) में निकाले गए लोग", "फायलिन (2013) व फणी (2019) मध्ये हलवलेले लोक"), "ndma", "OSDMA / NDMA reports."),
        (L("Number of cyclone and flood shelters", "चक्रवात और बाढ़ आश्रयों की संख्या", "चक्रीवादळ व पूर निवाऱ्यांची संख्या"), "india-gov", "OSDMA."),
        (L("Lightning deaths by year", "वर्षवार आकाशीय बिजली से मौतें", "वर्षनिहाय वीज कोसळून मृत्यू"), "india-gov", "NCRB Accidental Deaths and Suicides in India."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Odisha has 26 registered Geographical Indications in the GI Registry's list as on 31 December 2025, with no shared entries. Handicrafts and handlooms dominate: Kotpad handloom fabric (filed in 2004) was one of India's first GIs, followed by Orissa Ikat, Pipli appliqué, Konark stone carving, Pattachitra (with a separate logo registration), Sambalpuri Bandha, Bomkai, Habaspuri, Khandua and other saris, Cuttack silver filigree, Saura idital painting and the Dongria Kondh shawl. Food GIs include Odisha Rasagola, Kendrapara Rasabali, Similipal Kai chutney (made from red weaver ants) and Khajuri guda, and agricultural GIs include Kandhamal turmeric, Koraput Kalajeera rice and Ganjam kewda.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में ओडिशा के 26 पंजीकृत भौगोलिक संकेतक हैं, और कोई साझा प्रविष्टि नहीं है। हस्तशिल्प और हथकरघा प्रमुख हैं: कोटपाड हथकरघा वस्त्र (2004 में दायर) भारत के पहले जीआई में से एक था, जिसके बाद उड़ीसा इकत, पिपली एप्लिक, कोणार्क पत्थर नक्काशी, पट्टचित्र (अलग लोगो पंजीकरण सहित), संबलपुरी बांधा, बोमकाई, हबासपुरी, खंडुआ और अन्य साड़ियाँ, कटक की चाँदी की तारकशी, सौरा इडिताल चित्रकला और डोंगरिया कोंध शॉल आए। खाद्य जीआई में ओडिशा रसगोला, केंद्रापाड़ा रसाबली, सिमलीपाल काई चटनी (लाल बुनकर चींटियों से बनी) और खजूरी गुड़ हैं, और कृषि जीआई में कंधमाल हल्दी, कोरापुट कालाजीरा चावल और गंजाम केवड़ा शामिल हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत ओडिशाची 26 नोंदणीकृत भौगोलिक मानांकने आहेत, आणि एकही सामायिक नोंद नाही. हस्तकला व हातमाग प्रमुख आहेत: कोटपाड हातमाग वस्त्र (2004 मध्ये दाखल) हे भारतातील पहिल्या जीआयपैकी एक होते, त्यानंतर ओरिसा इकत, पिपली ऍप्लिक, कोणार्क दगडी कोरीवकाम, पट्टचित्र (स्वतंत्र बोधचिन्ह नोंदणीसह), संबलपुरी बांधा, बोमकाई, हबासपुरी, खंडुआ व इतर साड्या, कटकचे चांदीचे जाळीकाम, सौरा इडिताल चित्रकला व डोंगरिया कोंध शाल आली. खाद्य जीआयमध्ये ओडिशा रसगोला, केंद्रापाडा रसाबली, सिमलीपाल काई चटणी (लाल विणकर मुंग्यांपासून बनवलेली) व खजुरी गूळ आहेत, आणि कृषी जीआयमध्ये कंधमाल हळद, कोरापुट कालाजीरा तांदूळ व गंजाम केवडा यांचा समावेश आहे."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Odisha's 'golden triangle' links Bhubaneswar's temples, Puri's Jagannath temple and beach, and the Sun Temple at Konark. Nearby are the Jain caves of Udayagiri and Khandagiri, the Ashokan edicts at Dhauli, the crafts village of Raghurajpur and the appliqué shops of Pipli. Chilika offers boat trips to see dolphins and birds; Similipal and Bhitarkanika are wildlife destinations; the Buddhist sites of Ratnagiri, Lalitgiri and Udayagiri lie in Jajpur; and the hills of Koraput, with Duduma falls and tribal markets, attract travellers to the south. Gopalpur and Chandipur are quieter beaches.",
        "ओडिशा का 'स्वर्ण त्रिकोण' भुवनेश्वर के मंदिरों, पुरी के जगन्नाथ मंदिर और समुद्र तट, और कोणार्क के सूर्य मंदिर को जोड़ता है। पास में उदयगिरि और खंडगिरि की जैन गुफाएँ, धौली के अशोक शिलालेख, शिल्प ग्राम रघुराजपुर और पिपली की एप्लिक दुकानें हैं। चिलिका में डॉल्फ़िन और पक्षी देखने के लिए नौका विहार होता है; सिमलीपाल और भितरकनिका वन्यजीव स्थल हैं; रत्नगिरि, ललितगिरि और उदयगिरि के बौद्ध स्थल जाजपुर में हैं; और दुदुमा जलप्रपात व जनजातीय हाटों वाली कोरापुट की पहाड़ियाँ दक्षिण में यात्रियों को खींचती हैं। गोपालपुर और चांदीपुर शांत समुद्र तट हैं।",
        "ओडिशाचा 'सुवर्ण त्रिकोण' भुवनेश्वरची मंदिरे, पुरीचे जगन्नाथ मंदिर व किनारा आणि कोणार्कचे सूर्य मंदिर यांना जोडतो. जवळच उदयगिरी व खंडगिरीची जैन लेणी, धौलीचे अशोकाचे शिलालेख, रघुराजपूर हे हस्तकलेचे गाव व पिपलीची ऍप्लिकची दुकाने आहेत. चिलिकेत डॉल्फिन व पक्षी पाहण्यासाठी नौकाविहार होतो; सिमलीपाल व भितरकनिका ही वन्यजीव स्थळे आहेत; रत्नगिरी, ललितगिरी व उदयगिरीची बौद्ध स्थळे जाजपूरमध्ये आहेत; आणि दुदुमा धबधबा व आदिवासी बाजारांचे कोरापुटचे डोंगर दक्षिणेत प्रवाशांना आकर्षित करतात. गोपाळपूर व चांदीपूर हे शांत किनारे आहेत."),
        conf="Editorial"),
    lst("places", [
        it3("puri", "Puri", "पुरी", "पुरी", m=("Jagannath temple; beach", "जगन्नाथ मंदिर; समुद्र तट", "जगन्नाथ मंदिर; किनारा")),
        it3("konark", "Konark", "कोणार्क", "कोणार्क", m=("UNESCO Sun Temple", "यूनेस्को सूर्य मंदिर", "युनेस्को सूर्य मंदिर")),
        it3("bbsr", "Bhubaneswar", "भुवनेश्वर", "भुवनेश्वर", m=("Temple city; Udayagiri caves", "मंदिर नगरी; उदयगिरि गुफाएँ", "मंदिरनगरी; उदयगिरी लेणी")),
        it3("chilika", "Chilika Lake", "चिलिका झील", "चिलिका सरोवर", m=("Dolphins and birds", "डॉल्फ़िन और पक्षी", "डॉल्फिन व पक्षी")),
        it3("similipal", "Similipal", "सिमलीपाल", "सिमलीपाल", m=("Tiger reserve; waterfalls", "बाघ अभयारण्य; झरने", "व्याघ्र प्रकल्प; धबधबे")),
        it3("bhitarkanika", "Bhitarkanika", "भितरकनिका", "भितरकनिका", m=("Mangroves and crocodiles", "मैंग्रोव और मगरमच्छ", "खारफुटी व मगरी")),
        it3("koraput", "Koraput", "कोरापुट", "कोरापुट", m=("Hills and tribal haats", "पहाड़ियाँ और जनजातीय हाट", "डोंगर व आदिवासी बाजार")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Bhubaneswar's temples, Udayagiri–Khandagiri and Dhauli.", "भुवनेश्वर के मंदिर, उदयगिरि–खंडगिरि और धौली।", "भुवनेश्वरची मंदिरे, उदयगिरी–खंडगिरी व धौली.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("The golden triangle: Bhubaneswar, Puri and Konark, with Raghurajpur.", "स्वर्ण त्रिकोण: भुवनेश्वर, पुरी और कोणार्क, साथ में रघुराजपुर।", "सुवर्ण त्रिकोण: भुवनेश्वर, पुरी व कोणार्क, सोबत रघुराजपूर.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Golden triangle plus Chilika (Satapada or Rambha) and Bhitarkanika.", "स्वर्ण त्रिकोण के साथ चिलिका (सातपाड़ा या रंभा) और भितरकनिका।", "सुवर्ण त्रिकोणासोबत चिलिका (सातपाडा किंवा रंभा) व भितरकनिका.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("ot", "Odisha Tourism (official)", "ओडिशा पर्यटन (आधिकारिक)", "ओडिशा पर्यटन (अधिकृत)", url="https://odishatourism.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Angul", "अंगुल", "अंगुल"), ("Balangir", "बलांगीर", "बलांगीर"), ("Balasore", "बालेश्वर", "बालेश्वर"), ("Bargarh", "बरगढ़", "बरगड"), ("Bhadrak", "भद्रक", "भद्रक"),
    ("Boudh", "बौद्ध", "बौद्ध"), ("Cuttack", "कटक", "कटक"), ("Deogarh", "देवगढ़", "देवगड"), ("Dhenkanal", "ढेंकानाल", "ढेंकानाल"), ("Gajapati", "गजपति", "गजपती"),
    ("Ganjam", "गंजाम", "गंजाम"), ("Jagatsinghpur", "जगतसिंहपुर", "जगतसिंहपूर"), ("Jajpur", "जाजपुर", "जाजपूर"), ("Jharsuguda", "झारसुगुड़ा", "झारसुगुडा"), ("Kalahandi", "कालाहांडी", "कालाहांडी"),
    ("Kandhamal", "कंधमाल", "कंधमाल"), ("Kendrapara", "केंद्रापाड़ा", "केंद्रापाडा"), ("Kendujhar", "केंदुझर", "केंदुझर"), ("Khordha", "खोर्धा", "खोर्धा"), ("Koraput", "कोरापुट", "कोरापुट"),
    ("Malkangiri", "मलकानगिरि", "मलकानगिरी"), ("Mayurbhanj", "मयूरभंज", "मयूरभंज"), ("Nabarangpur", "नबरंगपुर", "नबरंगपूर"), ("Nayagarh", "नयागढ़", "नयागड"), ("Nuapada", "नुआपाड़ा", "नुआपाडा"),
    ("Puri", "पुरी", "पुरी"), ("Rayagada", "रायगड़ा", "रायगडा"), ("Sambalpur", "संबलपुर", "संबलपूर"), ("Subarnapur", "सुवर्णपुर", "सुवर्णपूर"), ("Sundargarh", "सुंदरगढ़", "सुंदरगड"),
]
assert len(DISTRICTS) == 30, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("bbsr", ("Bhubaneswar", "भुवनेश्वर", "भुवनेश्वर"), ("Planned capital and temple city; IT and education hub.", "नियोजित राजधानी और मंदिर नगरी; आईटी और शिक्षा केंद्र।", "नियोजित राजधानी व मंदिरनगरी; आयटी व शिक्षण केंद्र."), ("Capital", "राजधानी", "राजधानी")),
        city("cuttack", ("Cuttack", "कटक", "कटक"), ("Thousand-year-old city between the Mahanadi and Kathajodi; silver filigree.", "महानदी और काठजोड़ी के बीच हज़ार वर्ष पुराना नगर; चाँदी की तारकशी।", "महानदी व काठजोडीदरम्यानचे हजार वर्षांचे शहर; चांदीचे जाळीकाम."), ("Old capital", "पुरानी राजधानी", "जुनी राजधानी")),
        city("rourkela", ("Rourkela", "राउरकेला", "राउरकेला"), ("Steel city built around the public-sector steel plant.", "सार्वजनिक क्षेत्र के इस्पात संयंत्र के चारों ओर बसा इस्पात नगर।", "सार्वजनिक क्षेत्रातील पोलाद कारखान्याभोवती वसलेले पोलादनगर."), ("Industry", "उद्योग", "उद्योग")),
        city("berhampur", ("Berhampur", "बरहमपुर", "बेरहमपूर"), ("Silk city of southern Odisha.", "दक्षिणी ओडिशा की रेशम नगरी।", "दक्षिण ओडिशाची रेशीमनगरी."), ("Commerce", "वाणिज्य", "व्यापार")),
        city("sambalpur", ("Sambalpur", "संबलपुर", "संबलपूर"), ("Centre of western Odisha; Sambalpuri textiles and Hirakud dam.", "पश्चिमी ओडिशा का केंद्र; संबलपुरी वस्त्र और हीराकुद बाँध।", "पश्चिम ओडिशाचे केंद्र; संबलपुरी वस्त्रे व हिराकुड धरण."), ("Textiles", "वस्त्र", "वस्त्रे")),
        city("puri", ("Puri", "पुरी", "पुरी"), ("Pilgrimage town of Jagannath on the Bay of Bengal.", "बंगाल की खाड़ी पर जगन्नाथ का तीर्थ नगर।", "बंगालच्या उपसागरावरील जगन्नाथाचे तीर्थनगर."), ("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        city("balasore", ("Balasore", "बालेश्वर", "बालेश्वर"), ("Northern coastal town; missile test range at Chandipur.", "उत्तरी तटीय नगर; चांदीपुर में मिसाइल परीक्षण रेंज।", "उत्तरेकडील किनारी शहर; चांदीपूर येथे क्षेपणास्त्र चाचणी केंद्र."), ("Coast", "तट", "किनारा")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 30 districts (alphabetical)", "30 ज़िले (वर्णानुक्रम)", "30 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Official district list (State notification)", "आधिकारिक ज़िला सूची (राज्य अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य अधिसूचना)"), "india-gov", "Link the State's list of districts."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Hockey is Odisha's signature sport. Sundargarh district, with its strong tribal hockey tradition, has produced many India players, including Dilip Tirkey and Amit Rohidas, and the State has sponsored India's national hockey teams since 2018. Bhubaneswar's Kalinga Stadium hosted the men's Hockey World Cup in 2018 and co-hosted the 2023 edition with the new Birsa Munda stadium in Rourkela. Sprinter Dutee Chand has won Asian Games medals, and the Barabati Stadium in Cuttack is a well-known cricket ground. The Kalinga Stadium also has a high-performance athletics centre.",
        "हॉकी ओडिशा का पहचान वाला खेल है। मज़बूत जनजातीय हॉकी परंपरा वाले सुंदरगढ़ ज़िले ने दिलीप तिर्की और अमित रोहिदास सहित भारत के कई खिलाड़ी दिए हैं, और राज्य 2018 से भारत की राष्ट्रीय हॉकी टीमों का प्रायोजक है। भुवनेश्वर के कलिंग स्टेडियम ने 2018 में पुरुष हॉकी विश्व कप की मेज़बानी की और 2023 का संस्करण राउरकेला के नए बिरसा मुंडा स्टेडियम के साथ मिलकर आयोजित किया। धाविका दुती चंद ने एशियाई खेलों में पदक जीते हैं, और कटक का बाराबाटी स्टेडियम प्रसिद्ध क्रिकेट मैदान है। कलिंग स्टेडियम में एक उच्च-प्रदर्शन एथलेटिक्स केंद्र भी है।",
        "हॉकी हा ओडिशाचा ओळख असलेला खेळ आहे. मजबूत आदिवासी हॉकी परंपरा असलेल्या सुंदरगड जिल्ह्याने दिलीप तिर्की व अमित रोहिदास यांच्यासह भारताचे अनेक खेळाडू दिले आहेत, आणि राज्य 2018 पासून भारताच्या राष्ट्रीय हॉकी संघांचे प्रायोजक आहे. भुवनेश्वरच्या कलिंग स्टेडियमने 2018 मध्ये पुरुष हॉकी विश्वचषक आयोजित केला आणि 2023 ची स्पर्धा राउरकेलाच्या नव्या बिरसा मुंडा स्टेडियमसोबत संयुक्तपणे आयोजित केली. धावपटू दुती चंद यांनी आशियाई स्पर्धांत पदके जिंकली आहेत, आणि कटकचे बाराबाटी स्टेडियम हे प्रसिद्ध क्रिकेट मैदान आहे. कलिंग स्टेडियममध्ये उच्च-कामगिरी ॲथलेटिक्स केंद्रही आहे."),
        conf="Editorial"),
    lst("venues", [
        it3("kalinga", "Kalinga Stadium, Bhubaneswar", "कलिंग स्टेडियम, भुवनेश्वर", "कलिंग स्टेडियम, भुवनेश्वर"),
        it3("birsa", "Birsa Munda Hockey Stadium, Rourkela", "बिरसा मुंडा हॉकी स्टेडियम, राउरकेला", "बिरसा मुंडा हॉकी स्टेडियम, राउरकेला"),
        it3("barabati", "Barabati Stadium, Cuttack", "बाराबाटी स्टेडियम, कटक", "बाराबाटी स्टेडियम, कटक"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from Odisha (official list)", "ओडिशा के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "ओडिशाचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Odisha Sports and Youth Services Department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("kharavela", ("Kharavela", "खारवेल", "खारवेल"), ("King of Kalinga in the 1st century BCE, known from the Hathigumpha inscription.", "ई.पू. पहली सदी के कलिंग नरेश, हाथीगुंफा अभिलेख से ज्ञात।", "इ.स.पू. पहिल्या शतकातील कलिंगचा राजा, हाथीगुंफा शिलालेखातून ज्ञात."), ("History", "इतिहास", "इतिहास")),
        person("jayadeva", ("Jayadeva", "जयदेव", "जयदेव"), ("12th-century Sanskrit poet of the Gita Govinda, sung in the Puri temple.", "गीतगोविंद के 12वीं सदी के संस्कृत कवि, जो पुरी मंदिर में गाया जाता है।", "पुरी मंदिरात गायल्या जाणाऱ्या गीतगोविंदाचे बाराव्या शतकातील संस्कृत कवी."), ("Literature", "साहित्य", "साहित्य")),
        person("sarala", ("Sarala Das", "सारला दास", "सारला दास"), ("15th-century poet of the Odia Mahabharata.", "ओड़िया महाभारत के 15वीं सदी के कवि।", "ओडिया महाभारताचे पंधराव्या शतकातील कवी."), ("Literature", "साहित्य", "साहित्य")),
        person("fakirmohan", ("Fakir Mohan Senapati", "फ़कीर मोहन सेनापति", "फकीर मोहन सेनापती"), ("Father of modern Odia fiction; author of Chha Mana Atha Guntha.", "आधुनिक ओड़िया कथा के जनक; 'छ माण आठ गुंठ' के लेखक।", "आधुनिक ओडिया कथेचे जनक; 'छ माण आठ गुंठ' चे लेखक."), ("Literature", "साहित्य", "साहित्य")),
        person("madhusudan", ("Madhusudan Das", "मधुसूदन दास", "मधुसूदन दास"), ("'Utkal Gourab'; lawyer and leader of the movement for a separate Odisha.", "'उत्कल गौरव'; वकील और अलग ओडिशा आंदोलन के नेता।", "'उत्कल गौरव'; वकील व स्वतंत्र ओडिशा चळवळीचे नेते."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("gopabandhu", ("Gopabandhu Das", "गोपबंधु दास", "गोपबंधू दास"), ("'Utkalmani'; social reformer, educationist and freedom fighter.", "'उत्कलमणि'; समाज सुधारक, शिक्षाविद और स्वतंत्रता सेनानी।", "'उत्कलमणी'; समाजसुधारक, शिक्षणतज्ज्ञ व स्वातंत्र्यसैनिक."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("raghunath", ("Pandit Raghunath Murmu", "पंडित रघुनाथ मुर्मू", "पंडित रघुनाथ मुर्मू"), ("Creator of the Ol Chiki script for Santali, from Mayurbhanj.", "मयूरभंज के, संताली के लिए ओल चिकी लिपि के निर्माता।", "मयूरभंजचे, संतालीसाठी ओल चिकी लिपीचे निर्माते."), ("Language", "भाषा", "भाषा")),
        person("biju", ("Biju Patnaik", "बीजू पटनायक", "बिजू पटनायक"), ("Aviator, freedom fighter and twice Chief Minister of Odisha.", "विमानचालक, स्वतंत्रता सेनानी और दो बार ओडिशा के मुख्यमंत्री।", "वैमानिक, स्वातंत्र्यसैनिक व दोनदा ओडिशाचे मुख्यमंत्री."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("kelucharan", ("Kelucharan Mohapatra", "केलुचरण महापात्र", "केलुचरण महापात्र"), ("Guru who revived and shaped modern Odissi dance.", "आधुनिक ओडिसी नृत्य को पुनर्जीवित करने और गढ़ने वाले गुरु।", "आधुनिक ओडिसी नृत्याचे पुनरुज्जीवन करणारे व त्याला आकार देणारे गुरू."), ("Dance", "नृत्य", "नृत्य")),
        person("murmu", ("Droupadi Murmu", "द्रौपदी मुर्मू", "द्रौपदी मुर्मू"), ("President of India since 2022, from Mayurbhanj; the first tribal woman to hold the office.", "2022 से भारत की राष्ट्रपति, मयूरभंज से; इस पद पर पहली आदिवासी महिला।", "2022 पासून भारताच्या राष्ट्रपती, मयूरभंजच्या; या पदावरील पहिल्या आदिवासी महिला."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("sitakant", ("Sitakant Mahapatra", "सीताकांत महापात्र", "सीताकांत महापात्र"), ("Odia poet; Jnanpith Award.", "ओड़िया कवि; ज्ञानपीठ पुरस्कार।", "ओडिया कवी; ज्ञानपीठ पुरस्कार."), ("Literature", "साहित्य", "साहित्य")),
        person("dilip", ("Dilip Tirkey", "दिलीप तिर्की", "दिलीप तिर्की"), ("Former India hockey captain from Sundargarh.", "सुंदरगढ़ के पूर्व भारतीय हॉकी कप्तान।", "सुंदरगडचे माजी भारतीय हॉकी कर्णधार."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Odisha's links overseas are ancient: Kalinga's sailors traded with Sri Lanka, Bali, Java and other parts of South-East Asia, a memory celebrated each year at Cuttack's Bali Jatra. In modern times many workers from Ganjam and other districts have migrated to Surat's textile and diamond industries, to Kerala, Tamil Nadu and Andhra Pradesh, and to the Gulf. Odia communities in the United States and elsewhere hold Rath Yatras of their own, and the State government runs an annual conclave for the Odia diaspora.",
        "ओडिशा के विदेशी संबंध प्राचीन हैं: कलिंग के नाविक श्रीलंका, बाली, जावा और दक्षिण-पूर्व एशिया के अन्य भागों से व्यापार करते थे, जिसकी स्मृति हर वर्ष कटक की बाली जात्रा में मनाई जाती है। आधुनिक समय में गंजाम और अन्य ज़िलों के बहुत से श्रमिक सूरत के वस्त्र और हीरा उद्योगों, केरल, तमिलनाडु और आंध्र प्रदेश, और खाड़ी देशों में गए हैं। संयुक्त राज्य अमेरिका और अन्य जगहों के ओड़िया समुदाय अपनी रथयात्राएँ निकालते हैं, और राज्य सरकार ओड़िया प्रवासियों के लिए वार्षिक सम्मेलन आयोजित करती है।",
        "ओडिशाचे परदेशाशी संबंध प्राचीन आहेत: कलिंगचे नाविक श्रीलंका, बाली, जावा व आग्नेय आशियाच्या इतर भागांशी व्यापार करत, ज्याची आठवण दरवर्षी कटकच्या बाली जात्रेत साजरी होते. आधुनिक काळात गंजाम व इतर जिल्ह्यांतील अनेक कामगार सुरतच्या वस्त्र व हिरे उद्योगांत, केरळ, तमिळनाडू व आंध्र प्रदेशात आणि आखाती देशांत गेले आहेत. अमेरिका व इतरत्र ओडिया समुदाय स्वतःच्या रथयात्रा काढतात, आणि राज्य सरकार ओडिया प्रवासी समुदायासाठी वार्षिक संमेलन भरवते."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants and internal migrants", "प्रवासियों और आंतरिक प्रवासियों की संख्या", "परदेशी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; MEA."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Odisha portal", "ओडिशा सरकार पोर्टल", "ओडिशा शासन संकेतस्थळ", url="https://odisha.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Odisha Tourism", "ओडिशा पर्यटन", "ओडिशा पर्यटन", url="https://odishatourism.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Bhubaneswar", "भुवनेश्वर", "भुवनेश्वर"), "0674"], [L("Cuttack", "कटक", "कटक"), "0671"], [L("Rourkela", "राउरकेला", "राउरकेला"), "0661"],
           [L("Sambalpur", "संबलपुर", "संबलपूर"), "0663"], [L("Berhampur", "बरहमपुर", "बेरहमपूर"), "0680"], [L("Puri", "पुरी", "पुरी"), "06752"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("State e-services portal — verified link", "राज्य ई-सेवा पोर्टल — सत्यापित लिंक", "राज्य ई-सेवा संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "Odisha One / e-District portal."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("province", ("Odisha, formed on 1 April 1936, was the first province created on the basis of language.", "1 अप्रैल 1936 को बना ओडिशा भाषा के आधार पर बना पहला प्रांत था।", "1 एप्रिल 1936 रोजी बनलेला ओडिशा हा भाषेच्या आधारावर निर्माण झालेला पहिला प्रांत होता.")),
        triv("chilika", ("Chilika lake was designated a Ramsar site on 1 October 1981, among the first in India.", "चिलिका झील 1 अक्टूबर 1981 को रामसर स्थल घोषित हुई, भारत के पहले स्थलों में।", "चिलिका सरोवर 1 ऑक्टोबर 1981 रोजी रामसर स्थळ घोषित झाले, भारतातील पहिल्या स्थळांपैकी."), RAMSAR, "indian-wetlands"),
        triv("kotpad", ("Kotpad handloom fabric, filed in 2004, was among India's first Geographical Indications.", "2004 में दायर कोटपाड हथकरघा वस्त्र भारत के पहले भौगोलिक संकेतकों में था।", "2004 मध्ये दाखल कोटपाड हातमाग वस्त्र हे भारतातील पहिल्या भौगोलिक मानांकनांपैकी होते."), GI_PDF, "gi-registry"),
        triv("konark", ("The Sun Temple at Konark is designed as a giant chariot with carved stone wheels.", "कोणार्क का सूर्य मंदिर पत्थर के नक़्क़ाशीदार पहियों वाले विशाल रथ के रूप में बना है।", "कोणार्कचे सूर्य मंदिर कोरीव दगडी चाकांच्या प्रचंड रथाच्या रूपात बांधले आहे."), UNESCO, "unesco-whc"),
        triv("olchiki", ("The Ol Chiki script for Santali was created in Mayurbhanj by Pandit Raghunath Murmu.", "संताली की ओल चिकी लिपि मयूरभंज में पंडित रघुनाथ मुर्मू ने बनाई।", "संतालीची ओल चिकी लिपी मयूरभंजमध्ये पंडित रघुनाथ मुर्मू यांनी निर्माण केली.")),
        triv("ls", ("The State elects 21 members to the Lok Sabha.", "राज्य से लोकसभा के 21 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 21 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("or mod3 ok")
