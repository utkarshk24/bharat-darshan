"""Goa modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-GA"
ga = read("regions/IN-GA.json")["metrics"]; ind = read("india.json")["metrics"]
C = research("census_b5plus.json"); F = C["forest"]["GA"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About 61% of Goa is forest (ISFR 2023), one of the highest shares of any State, most of it in the Western Ghats along the eastern border, a global biodiversity hotspot. A chain of protected areas — Mhadei, Bhagwan Mahavir with Mollem National Park, Netravali and Cotigao wildlife sanctuaries — runs along the Ghats and links with Karnataka's forests; they shelter gaur, the State animal, leopards, sloth bears, king cobras, hornbills and occasionally tigers. Bondla is a smaller sanctuary with a zoo. On the coast, mangroves line the estuaries — the Salim Ali Bird Sanctuary on Chorao island protects them — and Morjim and Galgibag beaches are nesting sites of the olive ridley turtle.\n\nGoa's one Ramsar site is Nanda Lake at Curchorem, a freshwater wetland designated in 2022.",
        "गोवा का लगभग 61% भाग वन है (आईएसएफ़आर 2023), जो किसी भी राज्य के सबसे अधिक हिस्सों में है; इसका अधिकांश भाग पूर्वी सीमा पर पश्चिमी घाट में है, जो वैश्विक जैव विविधता हॉटस्पॉट है। घाटों के साथ संरक्षित क्षेत्रों की एक शृंखला — म्हादई, मोल्लेम राष्ट्रीय उद्यान सहित भगवान महावीर, नेत्रावली और कोटिगाओ वन्यजीव अभयारण्य — कर्नाटक के वनों से जुड़ती है; ये राज्य पशु गौर, तेंदुओं, स्लॉथ भालुओं, किंग कोबरा, धनेशों और कभी-कभी बाघों को आश्रय देते हैं। बोंडला चिड़ियाघर वाला छोटा अभयारण्य है। तट पर मुहानों के किनारे मैंग्रोव हैं — चोडण द्वीप का सालिम अली पक्षी अभयारण्य उन्हें संरक्षित करता है — और मोरजिम व गालजीबाग समुद्र तट ऑलिव रिडले कछुओं के अंडे देने के स्थल हैं।\n\nगोवा का एकमात्र रामसर स्थल कुडचडे की नंदा झील है, जो 2022 में घोषित मीठे पानी की आर्द्रभूमि है।",
        "गोव्याचा सुमारे 61% भाग वनाच्छादित आहे (आयएसएफआर 2023), जो कोणत्याही राज्यातील सर्वाधिक वाट्यांपैकी आहे; त्यापैकी बहुतांश पूर्व सीमेवरील पश्चिम घाटात आहे, जो जागतिक जैवविविधता हॉटस्पॉट आहे. घाटांच्या बाजूने संरक्षित क्षेत्रांची साखळी — म्हादई, मोले राष्ट्रीय उद्यानासह भगवान महावीर, नेत्रावळी व कोटिगाव वन्यजीव अभयारण्ये — कर्नाटकच्या वनांशी जोडलेली आहे; ती राज्यप्राणी गवा, बिबटे, अस्वले, नागराज, धनेश व कधीकधी वाघांना आश्रय देतात. बोंडला हे प्राणिसंग्रहालय असलेले लहान अभयारण्य आहे. किनाऱ्यावर खाड्यांच्या कडेला खारफुटी आहे — चोडण बेटावरील सालिम अली पक्षी अभयारण्य तिचे संरक्षण करते — आणि मोरजी व गालजीबाग किनारे ऑलिव्ह रिडले कासवांची अंडी घालण्याची ठिकाणे आहेत.\n\nगोव्याचे एकमेव रामसर स्थळ कुडचडेचे नंदा तळे आहे, 2022 मध्ये घोषित गोड्या पाण्याचे पाणथळ."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), ga["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(1, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: Nanda Lake, designated 8 June 2022, 42 ha."), "number"),
    ]),
    lst("protected", [
        it3("mollem", "Bhagwan Mahavir WLS and Mollem National Park", "भगवान महावीर वन्यजीव अभयारण्य और मोल्लेम राष्ट्रीय उद्यान", "भगवान महावीर वन्यजीव अभयारण्य व मोले राष्ट्रीय उद्यान", m=("Dudhsagar falls", "दूधसागर जलप्रपात", "दूधसागर धबधबा")),
        it3("mhadei", "Mhadei Wildlife Sanctuary", "म्हादई वन्यजीव अभयारण्य", "म्हादई वन्यजीव अभयारण्य", m=("Sattari", "सत्तरी", "सत्तरी")),
        it3("netravali", "Netravali Wildlife Sanctuary", "नेत्रावली वन्यजीव अभयारण्य", "नेत्रावळी वन्यजीव अभयारण्य", m=("Sanguem", "सांगे", "सांगे")),
        it3("cotigao", "Cotigao Wildlife Sanctuary", "कोटिगाओ वन्यजीव अभयारण्य", "कोटिगाव वन्यजीव अभयारण्य", m=("Canacona", "काणकोण", "काणकोण")),
        it3("salimali", "Salim Ali Bird Sanctuary", "सालिम अली पक्षी अभयारण्य", "सालिम अली पक्षी अभयारण्य", m=("Mangroves, Chorao", "मैंग्रोव, चोडण", "खारफुटी, चोडण")),
        it3("nanda", "Nanda Lake", "नंदा झील", "नंदा तळे", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("gaur", "Gaur (State animal)", "गौर (राज्य पशु)", "गवा (राज्यप्राणी)"), it3("bulbul", "Flame-throated bulbul (State bird)", "लाल-कंठ बुलबुल (राज्य पक्षी)", "लालकंठी बुलबुल (राज्यपक्षी)"),
        it3("kingcobra", "King cobra", "किंग कोबरा", "नागराज"), it3("hornbill", "Great hornbill", "बड़ा धनेश", "महाधनेश"),
        it3("turtle", "Olive ridley turtle", "ऑलिव रिडले कछुआ", "ऑलिव्ह रिडले कासव"), it3("mangrove", "Mangroves", "मैंग्रोव", "खारफुटी"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Proposed Mhadei tiger reserve — status", "प्रस्तावित म्हादई बाघ अभयारण्य — स्थिति", "प्रस्तावित म्हादई व्याघ्र प्रकल्प — स्थिती"), "ntca", "NTCA / Goa Forest Department; court proceedings."),
        (L("Olive ridley nesting counts", "ऑलिव रिडले घोंसलों की संख्या", "ऑलिव्ह रिडले घरट्यांची संख्या"), "india-gov", "Goa Forest Department."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Goa's rivers are short and tidal near the sea, so fresh water is stored behind dams such as Selaulim, Anjunem and the inter-State Tillari project, and drawn from the upper Mandovi and other rivers for drinking-water plants. Khazan lands — estuarine paddy fields managed for centuries by village communities with bunds and sluice gates — combine farming with fish and salt production. The diversion of water from the Mhadei (upper Mandovi) by Karnataka has been a long-running dispute, decided by the Mhadei Water Disputes Tribunal in 2018 and still contested. Sand mining, coastal erosion and pollution from mining and sewage affect rivers and beaches.",
        "गोवा की नदियाँ छोटी हैं और समुद्र के पास ज्वारीय, इसलिए मीठा पानी सालावली, अंजुणे और अंतरराज्यीय तिळारी परियोजना जैसे बाँधों के पीछे जमा किया जाता है, और पेयजल संयंत्रों के लिए ऊपरी मांडवी व अन्य नदियों से लिया जाता है। खाज़न भूमि — मुहानों के धान के खेत, जिन्हें गाँव समुदाय सदियों से बाँधों और जलद्वारों से संभालते आए हैं — खेती को मछली और नमक उत्पादन से जोड़ती है। कर्नाटक द्वारा म्हादई (ऊपरी मांडवी) से पानी मोड़ना लंबे समय से विवाद रहा है, जिस पर म्हादई जल विवाद न्यायाधिकरण ने 2018 में निर्णय दिया और जो अब भी विवादित है। रेत खनन, तटीय कटाव और खनन व सीवेज से प्रदूषण नदियों और समुद्र तटों को प्रभावित करते हैं।",
        "गोव्याच्या नद्या लहान असून समुद्राजवळ भरती-ओहोटीच्या, म्हणून गोडे पाणी साळावली, अंजुणे व आंतरराज्यीय तिळारी प्रकल्पासारख्या धरणांमागे साठवले जाते, आणि पेयजल प्रकल्पांसाठी वरच्या मांडवी व इतर नद्यांतून घेतले जाते. खाजन जमीन — खाड्यांतील भातशेते, जी गावसमुदाय शतकानुशतके बांध व मानशींनी सांभाळत आले आहेत — शेतीला मासे व मीठ उत्पादनाशी जोडते. कर्नाटकने म्हादईतून (वरच्या मांडवीतून) पाणी वळवणे हा दीर्घकाळचा वाद आहे, ज्यावर म्हादई जलविवाद लवादाने 2018 मध्ये निर्णय दिला आणि जो अजूनही वादग्रस्त आहे. वाळूउपसा, किनाऱ्याची धूप आणि खाणकाम व सांडपाण्यामुळे होणारे प्रदूषण नद्या व किनाऱ्यांवर परिणाम करतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Mhadei Water Disputes Tribunal award (2018) — official text", "म्हादई जल विवाद न्यायाधिकरण निर्णय (2018) — आधिकारिक पाठ", "म्हादई जलविवाद लवाद निवाडा (2018) — अधिकृत मजकूर"), "india-gov", "Ministry of Jal Shakti."),
        (L("Drinking-water supply and reservoir storage", "पेयजल आपूर्ति और जलाशय भंडारण", "पेयजल पुरवठा व जलाशय साठा"), "india-gov", "Goa Water Resources and Drinking Water departments."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Drowning is the main danger for visitors: strong currents, rip tides and the rough monsoon sea make swimming risky, and beaches are patrolled by lifeguards who put up red flags where swimming is unsafe. Heavy monsoon rain causes local floods and landslides in the Ghats, Arabian Sea cyclones such as Tauktae in 2021 bring high winds, and road accidents involving two-wheelers are common. Visitors should swim only between the lifeguard flags, avoid the sea in the monsoon, and follow official advisories.",
        "डूबना पर्यटकों के लिए मुख्य ख़तरा है: तेज़ धाराएँ, रिप करंट और मानसून का उग्र समुद्र तैरना जोखिम भरा बनाते हैं, और समुद्र तटों पर लाइफ़गार्ड गश्त करते हैं, जो जहाँ तैरना असुरक्षित है वहाँ लाल झंडे लगाते हैं। मानसून की भारी वर्षा से स्थानीय बाढ़ और घाटों में भूस्खलन होते हैं, 2021 के ताउते जैसे अरब सागर के चक्रवात तेज़ हवाएँ लाते हैं, और दोपहिया वाहनों से जुड़ी सड़क दुर्घटनाएँ आम हैं। पर्यटकों को केवल लाइफ़गार्ड के झंडों के बीच तैरना चाहिए, मानसून में समुद्र से दूर रहना चाहिए और आधिकारिक परामर्श का पालन करना चाहिए।",
        "बुडणे हा पर्यटकांसाठी मुख्य धोका आहे: जोरदार प्रवाह, रिप करंट व मान्सूनमधील खवळलेला समुद्र पोहणे धोकादायक करतात, आणि किनाऱ्यांवर जीवरक्षक गस्त घालतात, जे पोहणे असुरक्षित असेल तिथे लाल झेंडे लावतात. मुसळधार मान्सून पावसामुळे स्थानिक पूर व घाटांत भूस्खलन होतात, 2021 मधील तौक्तेसारखी अरबी समुद्रातील चक्रीवादळे जोरदार वारे आणतात, आणि दुचाकींचे रस्ते अपघात सामान्य आहेत. पर्यटकांनी केवळ जीवरक्षकांच्या झेंड्यांदरम्यान पोहावे, मान्सूनमध्ये समुद्रापासून दूर राहावे व अधिकृत सूचनांचे पालन करावे."),
        conf="Editorial"),
    emergency_table(("Goa", "गोवा", "गोव्या")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Beach drownings and rescues by year", "वर्षवार समुद्र तट पर डूबने और बचाव की घटनाएँ", "वर्षनिहाय किनाऱ्यावरील बुडण्याच्या व बचावाच्या घटना"), "india-gov", "Goa Tourism / lifeguard agency reports."),
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official address."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Fifteen GIs are registered for Goa on the GI Registry's list as on 31 December 2025, almost all of them foods and crops. Feni, filed in 2007, was the first. Since 2018 Goa has added local varieties that farmers had kept for generations: Khola and Harmal chillies, Myndoli banana, Agassaim and Taleigao brinjals, the seven-ridged Sat Shiro okra, Korgut rice, the Mankurad, Hilario and Mussarad mangoes, Goa cashew and the cashew apple, and the sweets bebinca and khaje.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में गोवा के लिए पंद्रह जीआई पंजीकृत हैं, जिनमें लगभग सभी खाद्य पदार्थ और फ़सलें हैं। 2007 में दायर फ़ेनी पहला था। 2018 से गोवा ने उन स्थानीय किस्मों को जोड़ा है जिन्हें किसान पीढ़ियों से सँजोते आए: खोला और हरमल मिर्च, मैंदोली केला, आगशी और ताळगाँव बैंगन, सात धारियों वाली सात शिरांचो भिंडी, कोरगुट चावल, मानकुराद, हिलारियो और मुसराद आम, गोवा काजू और काजू फल, और मिठाइयाँ बेबिंका व खाजे।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत गोव्यासाठी पंधरा जीआय नोंदणीकृत आहेत, ज्यांपैकी जवळपास सर्व खाद्यपदार्थ व पिके आहेत. 2007 मध्ये दाखल फेणी हे पहिले होते. 2018 पासून गोव्याने शेतकऱ्यांनी पिढ्यानपिढ्या जपलेले स्थानिक वाण जोडले आहेत: खोला व हरमल मिरची, मैंदोळी केळे, आगशी व ताळगाव वांगी, सात शिरांची भेंडी, कोरगुट तांदूळ, मानकुराद, हिलारियो व मुसराद आंबे, गोवा काजू व काजूबोंड, आणि बेबिंका व खाजे या मिठाया."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Pending GI applications from Goa", "गोवा के लंबित जीआई आवेदन", "गोव्याचे प्रलंबित जीआय अर्ज"), "gi-registry", "GI Registry application status search."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "North Goa's beaches — Calangute, Baga, Anjuna, Vagator, Morjim and Arambol — are lively with shacks, markets and nightlife, while South Goa's Colva, Benaulim, Agonda, Palolem and Cola are quieter. Old Goa's churches and convents, including the Basilica of Bom Jesus with the relics of St Francis Xavier and the Sé Cathedral, are a UNESCO World Heritage site, and Panaji's Fontainhas quarter, the forts of Aguada, Chapora and Reis Magos, and Indo-Portuguese houses in Chandor and Loutolim show the colonial past. Inland, the temples of Mangeshi and Shantadurga near Ponda, spice plantations, the Dudhsagar falls and the Mollem and Cotigao forests offer a different Goa.",
        "उत्तर गोवा के समुद्र तट — कलंगुट, बागा, अंजुना, वागातोर, मोरजिम और अरंबोल — शैक, बाज़ारों और रात्रि जीवन से जीवंत हैं, जबकि दक्षिण गोवा के कोलवा, बाणावली, आगोंद, पाळोळे और कोला शांत हैं। संत फ़्रांसिस ज़ेवियर के अवशेषों वाले बेसिलिका ऑफ़ बॉम जीसस और से कैथेड्रल सहित पुराने गोवा के चर्च और कॉन्वेंट यूनेस्को विश्व धरोहर स्थल हैं, और पणजी का फ़ॉन्टेनहास क्षेत्र, अगुआदा, शापोरा और रेइस मागोस के क़िले, और चांदोर व लोटली के भारतीय-पुर्तगाली घर औपनिवेशिक अतीत दिखाते हैं। भीतरी भाग में फोंडा के पास मंगेशी और शांतादुर्गा के मंदिर, मसाला बाग़ान, दूधसागर जलप्रपात और मोल्लेम व कोटिगाओ के वन एक अलग गोवा दिखाते हैं।",
        "उत्तर गोव्याचे किनारे — कळंगुट, बागा, हणजूण, वागातोर, मोरजी व हरमल — शॅक, बाजार व रात्रजीवनाने गजबजलेले असतात, तर दक्षिण गोव्याचे कोलवा, बाणावली, आगोंद, पाळोळे व कोला शांत आहेत. संत फ्रान्सिस झेविअरचे अवशेष असलेल्या बॅसिलिका ऑफ बॉम जीझस व से कॅथेड्रलसह जुन्या गोव्याची चर्च व कॉन्व्हेंट युनेस्को जागतिक वारसा स्थळ आहेत, आणि पणजीचा फोंतेनास भाग, आग्वाद, शापोरा व रेईश मागूश किल्ले, आणि चांदोर व लोटलीची इंडो-पोर्तुगीज घरे वसाहतकालीन भूतकाळ दाखवतात. आतल्या भागात फोंड्याजवळील मंगेशी व शांतादुर्गेची देवळे, मसाल्यांच्या बागा, दूधसागर धबधबा व मोले आणि कोटिगावची वने वेगळा गोवा दाखवतात."),
        conf="Editorial"),
    lst("places", [
        it3("northbeaches", "North Goa beaches", "उत्तर गोवा के समुद्र तट", "उत्तर गोव्याचे किनारे", m=("Calangute, Baga, Anjuna, Arambol", "कलंगुट, बागा, अंजुना, अरंबोल", "कळंगुट, बागा, हणजूण, हरमल")),
        it3("southbeaches", "South Goa beaches", "दक्षिण गोवा के समुद्र तट", "दक्षिण गोव्याचे किनारे", m=("Colva, Agonda, Palolem", "कोलवा, आगोंद, पाळोळे", "कोलवा, आगोंद, पाळोळे")),
        it3("oldgoa", "Old Goa", "पुराना गोवा", "जुने गोवा", m=("UNESCO churches and convents", "यूनेस्को चर्च और कॉन्वेंट", "युनेस्को चर्च व कॉन्व्हेंट")),
        it3("panaji", "Panaji and Fontainhas", "पणजी और फ़ॉन्टेनहास", "पणजी व फोंतेनास", m=("Latin quarter", "लैटिन क्वार्टर", "लॅटिन क्वार्टर")),
        it3("ponda", "Ponda temples and spice farms", "फोंडा के मंदिर और मसाला बाग़ान", "फोंड्याची देवळे व मसाल्यांच्या बागा", m=("Mangeshi, Shantadurga", "मंगेशी, शांतादुर्गा", "मंगेशी, शांतादुर्गा")),
        it3("dudhsagar", "Dudhsagar falls", "दूधसागर जलप्रपात", "दूधसागर धबधबा", m=("Best after the monsoon", "मानसून के बाद सबसे अच्छा", "मान्सूननंतर सर्वोत्तम")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Panaji and Fontainhas, Old Goa, and a day on the North Goa beaches.", "पणजी और फ़ॉन्टेनहास, पुराना गोवा, और उत्तर गोवा के तटों पर एक दिन।", "पणजी व फोंतेनास, जुने गोवा, आणि उत्तर गोव्याच्या किनाऱ्यांवर एक दिवस.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Add Ponda's temples and spice farms, Chandor's houses and the South Goa beaches.", "फोंडा के मंदिर व मसाला बाग़ान, चांदोर के घर और दक्षिण गोवा के तट जोड़ें।", "फोंड्याची देवळे व मसाल्यांच्या बागा, चांदोरची घरे व दक्षिण गोव्याचे किनारे जोडा.")),
        it3("d2m", "2 days (monsoon)", "2 दिन (मानसून)", "2 दिवस (मान्सून)", d=("Dudhsagar falls, Mollem forest and the hinterland villages.", "दूधसागर जलप्रपात, मोल्लेम वन और भीतरी गाँव।", "दूधसागर धबधबा, मोले जंगल व आतील गावे.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("gt", "Goa Tourism (official)", "गोवा पर्यटन (आधिकारिक)", "गोवा पर्यटन (अधिकृत)", url="https://goa-tourism.com", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium / Goa Department of Tourism."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [("Kushavati", "कुशावती", "कुशावती"), ("North Goa", "उत्तर गोवा", "उत्तर गोवा"), ("South Goa", "दक्षिण गोवा", "दक्षिण गोवा")]
module(R, "cities", [
    lst("cities", [
        city("panaji", ("Panaji", "पणजी", "पणजी"), ("Capital on the Mandovi; Fontainhas and IFFI.", "मांडवी किनारे राजधानी; फ़ॉन्टेनहास और इफ़्फ़ी।", "मांडवीकाठची राजधानी; फोंतेनास व इफ्फी."), ("Capital", "राजधानी", "राजधानी")),
        city("margao", ("Margao (Madgaon)", "मडगाँव", "मडगाव"), ("Commercial capital of the south; South Goa headquarters.", "दक्षिण की वाणिज्यिक राजधानी; दक्षिण गोवा मुख्यालय।", "दक्षिणेची व्यापारी राजधानी; दक्षिण गोवा मुख्यालय."), ("Commerce", "वाणिज्य", "व्यापार")),
        city("vasco", ("Vasco da Gama", "वास्को द गामा", "वास्को द गामा"), ("Port town of Mormugao; Goa Shipyard and Dabolim airport.", "मुरगाँव का बंदरगाह नगर; गोवा शिपयार्ड और डाबोलिम हवाई अड्डा।", "मुरगावचे बंदरशहर; गोवा शिपयार्ड व दाबोळी विमानतळ."), ("Port", "बंदरगाह", "बंदर")),
        city("mapusa", ("Mapusa", "म्हापसा", "म्हापसा"), ("Market town of Bardez; Friday market.", "बारदेश का बाज़ार नगर; शुक्रवार का बाज़ार।", "बार्देशचे बाजारशहर; शुक्रवारचा बाजार."), ("Market", "बाज़ार", "बाजार")),
        city("ponda", ("Ponda", "फोंडा", "फोंडा"), ("Temple town and industrial centre.", "मंदिर नगर और औद्योगिक केंद्र।", "देवळांचे शहर व औद्योगिक केंद्र."), ("Heritage", "धरोहर", "वारसा")),
        city("quepem", ("Quepem", "केपे", "केपे"), ("Headquarters of the new Kushavati district.", "नए कुशावती ज़िले का मुख्यालय।", "नव्या कुशावती जिल्ह्याचे मुख्यालय."), ("Administration", "प्रशासन", "प्रशासन")),
    ], title=L("Major towns", "प्रमुख नगर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 3 districts (alphabetical)", "3 ज़िले (वर्णानुक्रम)", "3 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Talukas by district after December 2025", "दिसंबर 2025 के बाद ज़िलेवार तालुके", "डिसेंबर 2025 नंतर जिल्हानिहाय तालुके"), "india-gov", "Per The Goan: Kushavati — Quepem, Sanguem, Dharbandora, Canacona; North Goa — Pernem, Bardez, Bicholim, Sattari, Tiswadi; South Goa — Ponda, Salcete, Mormugao. Link the notification."),
        (L("Town populations (Census 2011)", "नगरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Football is Goa's passion. Village clubs and the historic sides Dempo, Salgaocar and Churchill Brothers have won national titles, FC Goa plays in the Indian Super League at the Jawaharlal Nehru Stadium in Fatorda, and Goa has produced many India internationals, among them the goalkeeper Brahmanand Sankhwalkar and the midfielder Bruno Coutinho. The Fatorda stadium hosted matches of the FIFA U-17 World Cup in 2017, and Goa hosted the 37th National Games in 2023. Beach sports, sailing, kayaking and kite-surfing are growing, and Dilip Sardesai of Margao was a noted Test cricketer.",
        "फ़ुटबॉल गोवा का जुनून है। गाँवों के क्लबों और ऐतिहासिक टीमों डेम्पो, सालगांवकर और चर्चिल ब्रदर्स ने राष्ट्रीय ख़िताब जीते हैं, एफ़सी गोवा फातोर्डा के जवाहरलाल नेहरू स्टेडियम में इंडियन सुपर लीग खेलती है, और गोवा ने कई भारतीय अंतरराष्ट्रीय खिलाड़ी दिए हैं, जिनमें गोलकीपर ब्रह्मानंद शंखवालकर और मिडफ़ील्डर ब्रूनो कुटिन्हो हैं। फातोर्डा स्टेडियम ने 2017 में फ़ीफ़ा अंडर-17 विश्व कप के मैचों की मेज़बानी की, और गोवा ने 2023 में 37वें राष्ट्रीय खेलों की मेज़बानी की। समुद्र तट खेल, नौकायन, कयाकिंग और काइट-सर्फ़िंग बढ़ रहे हैं, और मडगाँव के दिलीप सरदेसाई प्रसिद्ध टेस्ट क्रिकेटर थे।",
        "फुटबॉल ही गोव्याची आवड आहे. गावचे क्लब व डेंपो, साळगावकर आणि चर्चिल ब्रदर्स या ऐतिहासिक संघांनी राष्ट्रीय विजेतेपदे जिंकली आहेत, एफसी गोवा फातोर्ड्याच्या जवाहरलाल नेहरू स्टेडियमवर इंडियन सुपर लीग खेळते, आणि गोव्याने अनेक भारतीय आंतरराष्ट्रीय खेळाडू दिले आहेत, ज्यांत गोलरक्षक ब्रह्मानंद शंखवाळकर व मध्यरक्षक ब्रुनो कुतिन्हो आहेत. फातोर्डा स्टेडियमने 2017 मध्ये फिफा 17 वर्षांखालील विश्वचषकाचे सामने आयोजित केले, आणि गोव्याने 2023 मध्ये 37 व्या राष्ट्रीय क्रीडा स्पर्धांचे यजमानपद भूषवले. किनाऱ्यावरील खेळ, नौकानयन, कयाकिंग व काइट-सर्फिंग वाढत आहेत, आणि मडगावचे दिलीप सरदेसाई प्रसिद्ध कसोटी क्रिकेटपटू होते."),
        conf="Editorial"),
    lst("venues", [
        it3("fatorda", "Jawaharlal Nehru Stadium, Fatorda", "जवाहरलाल नेहरू स्टेडियम, फातोर्डा", "जवाहरलाल नेहरू स्टेडियम, फातोर्डा"),
        it3("tilak", "Tilak Maidan, Vasco", "तिलक मैदान, वास्को", "टिळक मैदान, वास्को"),
        it3("campal", "Campal sports complex, Panaji", "कांपाल खेल परिसर, पणजी", "कांपाल क्रीडा संकुल, पणजी"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("National football titles of Goan clubs — official list", "गोवा के क्लबों के राष्ट्रीय फ़ुटबॉल ख़िताब — आधिकारिक सूची", "गोमंतकीय क्लबांची राष्ट्रीय फुटबॉल विजेतेपदे — अधिकृत यादी"), "india-gov", "All India Football Federation records.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("tbcunha", ("Tristão de Bragança Cunha", "त्रिस्ताओ ब्रागांसा कुन्हा", "त्रिस्तांव ब्रागांस कुन्हा"), ("Called the father of Goan nationalism; founded the Goa Congress Committee in 1928.", "गोवा राष्ट्रवाद के जनक कहे जाते हैं; 1928 में गोवा कांग्रेस समिति की स्थापना की।", "गोमंतकीय राष्ट्रवादाचे जनक म्हटले जातात; 1928 मध्ये गोवा काँग्रेस समितीची स्थापना केली."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("faria", ("Abbé Faria", "आबे फ़ारिया", "आबे फारिया"), ("18th-century priest from Candolim, a pioneer of the scientific study of hypnosis.", "कांदोळी के 18वीं सदी के पादरी, सम्मोहन के वैज्ञानिक अध्ययन के अग्रदूत।", "कांदोळीचे अठराव्या शतकातील धर्मगुरू, संमोहनाच्या वैज्ञानिक अभ्यासाचे प्रणेते."), ("Science", "विज्ञान", "विज्ञान")),
        person("borkar", ("B. B. Borkar (Bakibab)", "बा. भ. बोरकर (बाकीबाब)", "बा. भ. बोरकर (बाकीबाब)"), ("Poet in Marathi and Konkani, known for his songs of Goa's landscape.", "मराठी और कोंकणी के कवि, जो गोवा के भूदृश्य के गीतों के लिए जाने जाते हैं।", "मराठी व कोकणीचे कवी, गोव्याच्या निसर्गावरील गीतांसाठी ओळखले जातात."), ("Literature", "साहित्य", "साहित्य")),
        person("kelekar", ("Ravindra Kelekar", "रवींद्र केळेकर", "रवींद्र केळेकर"), ("Konkani writer and Jnanpith laureate who campaigned for Konkani's recognition.", "कोंकणी लेखक और ज्ञानपीठ विजेता, जिन्होंने कोंकणी की मान्यता के लिए अभियान चलाया।", "कोकणी लेखक व ज्ञानपीठ विजेते, ज्यांनी कोकणीच्या मान्यतेसाठी चळवळ केली."), ("Literature", "साहित्य", "साहित्य")),
        person("mauzo", ("Damodar Mauzo", "दामोदर मावजो", "दामोदर मावजो"), ("Konkani novelist and Jnanpith laureate.", "कोंकणी उपन्यासकार और ज्ञानपीठ विजेता।", "कोकणी कादंबरीकार व ज्ञानपीठ विजेते."), ("Literature", "साहित्य", "साहित्य")),
        person("mario", ("Mario Miranda", "मारियो मिरांडा", "मारिओ मिरांडा"), ("Cartoonist whose drawings captured Goan village life.", "कार्टूनिस्ट, जिनके चित्रों ने गोवा के गाँव के जीवन को दर्ज किया।", "व्यंगचित्रकार, ज्यांच्या चित्रांनी गोव्याचे गावजीवन टिपले."), ("Art", "कला", "कला")),
        person("mashelkar", ("Raghunath Mashelkar", "रघुनाथ माशेलकर", "रघुनाथ माशेलकर"), ("Chemical engineer and former Director-General of CSIR, born at Mashel.", "रासायनिक अभियंता और सीएसआईआर के पूर्व महानिदेशक, माशेल में जन्मे।", "रासायनिक अभियंते व सीएसआयआरचे माजी महासंचालक, माशेल येथे जन्मलेले."), ("Science", "विज्ञान", "विज्ञान")),
        person("sardesai", ("Dilip Sardesai", "दिलीप सरदेसाई", "दिलीप सरदेसाई"), ("Test batsman from Margao who starred in India's 1971 series win in the West Indies.", "मडगाँव के टेस्ट बल्लेबाज़, जो 1971 में वेस्ट इंडीज़ में भारत की सीरीज़ जीत के सितारे रहे।", "मडगावचे कसोटी फलंदाज, जे 1971 मध्ये वेस्ट इंडिजमधील भारताच्या मालिकाविजयाचे तारे ठरले."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Goans have emigrated for generations — to Bombay (Mumbai) and Karachi, to East Africa and the Gulf, to Portugal, and in recent decades to the United Kingdom (notably Swindon and London), Canada and Australia. Many Goan men worked as seafarers and on cruise ships. Because people born in Goa before 1961, and their descendants, could claim Portuguese citizenship, many younger Goans have taken Portuguese passports to work in Europe. Remittances have long supported Goan households and village churches and temples.",
        "गोवावासी पीढ़ियों से विदेश जाते रहे हैं — बंबई (मुंबई) और कराची, पूर्वी अफ़्रीका और खाड़ी देशों, पुर्तगाल, और हाल के दशकों में ब्रिटेन (विशेषकर स्विंडन और लंदन), कनाडा और ऑस्ट्रेलिया। बहुत से गोवा के पुरुष नाविकों और क्रूज़ जहाज़ों पर काम करते रहे हैं। क्योंकि 1961 से पहले गोवा में जन्मे लोग और उनके वंशज पुर्तगाली नागरिकता का दावा कर सकते थे, बहुत से युवा गोवावासियों ने यूरोप में काम करने के लिए पुर्तगाली पासपोर्ट लिए हैं। भेजी गई रक़म लंबे समय से गोवा के परिवारों और गाँवों के चर्चों व मंदिरों को सहारा देती रही है।",
        "गोंयकार पिढ्यानपिढ्या स्थलांतर करत आले आहेत — मुंबई व कराची, पूर्व आफ्रिका व आखाती देश, पोर्तुगाल, आणि अलीकडच्या दशकांत ब्रिटन (विशेषतः स्विंडन व लंडन), कॅनडा व ऑस्ट्रेलिया. अनेक गोमंतकीय पुरुषांनी खलाशी म्हणून व क्रूझ जहाजांवर काम केले. 1961 पूर्वी गोव्यात जन्मलेले लोक व त्यांचे वंशज पोर्तुगीज नागरिकत्वाचा दावा करू शकत असल्याने अनेक तरुण गोंयकारांनी युरोपात काम करण्यासाठी पोर्तुगीज पासपोर्ट घेतले आहेत. पाठवलेल्या पैशांनी दीर्घकाळ गोमंतकीय कुटुंबे व गावांतील चर्च आणि देवळांना आधार दिला आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Size of the Goan diaspora by country", "देशवार गोवा प्रवासी समुदाय का आकार", "देशनिहाय गोमंतकीय प्रवासी समुदायाचा आकार"), "india-gov", "Office of the NRI Commissioner, Goa."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Goa portal", "गोवा सरकार पोर्टल", "गोवा शासन संकेतस्थळ", url="https://www.goa.gov.in", src="india-gov"),
        it3("goaonline", "Goa Online (citizen services)", "गोवा ऑनलाइन (नागरिक सेवाएँ)", "गोवा ऑनलाइन (नागरी सेवा)", url="https://goaonline.gov.in", src="india-gov"),
        it3("dip", "Department of Information and Publicity", "सूचना एवं प्रचार विभाग", "माहिती व प्रसिद्धी खाते", url="https://dip.goa.gov.in", src="goa-dip"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD code", "एसटीडी कोड", "एसटीडी कोड"),
          [col(L("Area", "क्षेत्र", "क्षेत्र")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("All of Goa", "पूरा गोवा", "संपूर्ण गोवा"), "0832"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; Goa uses a single STD code. To be checked against the Department of Telecommunications numbering plan.", "संपादकीय; गोवा में एक ही एसटीडी कोड है। दूरसंचार विभाग की नंबरिंग योजना से जाँचा जाएगा।", "संपादकीय; गोव्यात एकच एसटीडी कोड आहे. दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळले जाईल.")),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("small", ("Goa is India's smallest State by area — 3,702 km².", "गोवा क्षेत्रफल में भारत का सबसे छोटा राज्य है — 3,702 वर्ग किमी।", "गोवा हे क्षेत्रफळाने भारतातील सर्वांत लहान राज्य आहे — 3,702 चौ.किमी."), LS_FOREST, "fsi"),
        triv("pc", ("Goa's per capita NSDP in FY2024-25 was second only to Sikkim's among the regions in the MoSPI series.", "वित्त वर्ष 2024-25 में गोवा का प्रति व्यक्ति एनएसडीपी मोस्पी शृंखला के क्षेत्रों में केवल सिक्किम से कम था।", "आ.व. 2024-25 मध्ये गोव्याचे दरडोई एनएसडीपी मोस्पी मालिकेतील प्रदेशांत केवळ सिक्कीमखालोखाल होते."), MOSPI, "mospi"),
        triv("forest", ("Over 61% of Goa is covered by forest (ISFR 2023).", "गोवा का 61% से अधिक भाग वन से ढका है (आईएसएफ़आर 2023)।", "गोव्याचा 61% हून अधिक भाग वनाच्छादित आहे (आयएसएफआर 2023)."), LS_FOREST, "fsi"),
        triv("poll", ("In the 1967 opinion poll, Goans voted to remain separate rather than merge with Maharashtra.", "1967 के जनमत सर्वेक्षण में गोवावासियों ने महाराष्ट्र में विलय के बजाय अलग रहने के पक्ष में मत दिया।", "1967 च्या जनमत कौलात गोंयकारांनी महाराष्ट्रात विलीन होण्याऐवजी वेगळे राहण्याच्या बाजूने मत दिले.")),
        triv("iffi", ("The International Film Festival of India has been held in Goa every year since 2004.", "भारत का अंतरराष्ट्रीय फ़िल्म महोत्सव 2004 से हर वर्ष गोवा में होता है।", "भारतीय आंतरराष्ट्रीय चित्रपट महोत्सव 2004 पासून दरवर्षी गोव्यात भरतो.")),
        triv("ls", ("The State elects 2 members to the Lok Sabha.", "राज्य से लोकसभा के 2 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 2 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("ga mod3 ok")
