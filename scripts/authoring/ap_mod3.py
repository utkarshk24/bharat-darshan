"""Andhra Pradesh modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-AP"
DIST = "https://www.etvbharat.com/en/state/andhra-pradesh-cabinet-approves-formation-of-two-new-districts-enn25123002492"
ap = read("regions/IN-AP.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About 18.5% of Andhra Pradesh is forest (ISFR 2023), mostly along the Eastern Ghats. The Nallamala hills hold the Nagarjunasagar–Srisailam Tiger Reserve, one of India's largest tiger reserves, which adjoins Telangana's Amrabad Tiger Reserve across the Krishna. The Seshachalam hills around Tirupati are the home of the red sanders tree, found naturally only in this region. In the north, the Papikonda hills line the Godavari gorge, and the Araku and Paderu hills are a stronghold of tribal farming and coffee.\n\nThe coast has the Coringa mangroves at the mouth of the Godavari, the Krishna mangroves, and the Pulicat lagoon on the Tamil Nadu border, an important winter home of flamingos. Kolleru Lake, between the two deltas, is the State's one Ramsar site, designated in 2002 and covering 90,100 ha.",
        "आंध्र प्रदेश का लगभग 18.5% भाग वन है (आईएसएफ़आर 2023), जो अधिकतर पूर्वी घाट के साथ है। नल्लमला पहाड़ियों में नागार्जुनसागर–श्रीशैलम बाघ अभयारण्य है, जो भारत के सबसे बड़े बाघ अभयारण्यों में है और कृष्णा के पार तेलंगाना के अमराबाद बाघ अभयारण्य से सटा है। तिरुपति के आसपास की शेषाचलम पहाड़ियाँ लाल चंदन के पेड़ का घर हैं, जो प्राकृतिक रूप से केवल इसी क्षेत्र में मिलता है। उत्तर में पापिकोंडा पहाड़ियाँ गोदावरी घाटी के किनारे हैं, और अराकू व पाडेरू पहाड़ियाँ आदिवासी खेती और कॉफ़ी का गढ़ हैं।\n\nतट पर गोदावरी के मुहाने पर कोरिंगा मैंग्रोव, कृष्णा मैंग्रोव, और तमिलनाडु सीमा पर पुलिकट लैगून है, जो फ़्लेमिंगो का महत्त्वपूर्ण शीतकालीन आवास है। दोनों डेल्टाओं के बीच कोल्लेरु झील राज्य का एकमात्र रामसर स्थल है, जो 2002 में घोषित हुआ और 90,100 हेक्टेयर में फैला है।",
        "आंध्र प्रदेशचा सुमारे 18.5% भाग वनाच्छादित आहे (आयएसएफआर 2023), बहुतांश पूर्व घाटालगत. नल्लमला डोंगरांत नागार्जुनसागर–श्रीशैलम व्याघ्र प्रकल्प आहे — भारतातील सर्वांत मोठ्या व्याघ्र प्रकल्पांपैकी एक — जो कृष्णेपलीकडील तेलंगणाच्या अमराबाद व्याघ्र प्रकल्पाला लागून आहे. तिरुपतीभोवतीचे शेषाचलम डोंगर हे रक्तचंदनाच्या झाडाचे घर आहे, जे नैसर्गिकरीत्या फक्त याच प्रदेशात आढळते. उत्तरेला पापिकोंडा डोंगर गोदावरीच्या घळीलगत आहेत, आणि अराकू व पाडेरू डोंगर आदिवासी शेती व कॉफीचे केंद्र आहेत.\n\nकिनाऱ्यावर गोदावरीच्या मुखाशी कोरिंगा खारफुटी, कृष्णा खारफुटी, आणि तमिळनाडू सीमेवर पुलिकत खाजण आहे — रोहित पक्ष्यांचे महत्त्वाचे हिवाळी आश्रयस्थान. दोन्ही त्रिभुज प्रदेशांमधील कोल्लेरू सरोवर हे राज्यातील एकमेव रामसर स्थळ आहे, 2002 मध्ये घोषित व 90,100 हेक्टरवर पसरलेले."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(30084.96, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(30223.62, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), ap["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(1, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="Kolleru Lake, designated 19 Aug 2002, 90,100 ha (MoEFCC list as on 21 April 2026)."), "number"),
    ]),
    lst("protected", [
        it3("nstr", "Nagarjunasagar–Srisailam Tiger Reserve", "नागार्जुनसागर–श्रीशैलम बाघ अभयारण्य", "नागार्जुनसागर–श्रीशैलम व्याघ्र प्रकल्प", m=("Nallamala hills", "नल्लमला पहाड़ियाँ", "नल्लमला डोंगर")),
        it3("svnp", "Sri Venkateswara National Park", "श्री वेंकटेश्वर राष्ट्रीय उद्यान", "श्री वेंकटेश्वर राष्ट्रीय उद्यान", m=("Seshachalam; red sanders", "शेषाचलम; लाल चंदन", "शेषाचलम; रक्तचंदन")),
        it3("papikonda", "Papikonda National Park", "पापिकोंडा राष्ट्रीय उद्यान", "पापिकोंडा राष्ट्रीय उद्यान", m=("Godavari gorge", "गोदावरी घाटी", "गोदावरी घळ")),
        it3("coringa", "Coringa Wildlife Sanctuary", "कोरिंगा वन्यजीव अभयारण्य", "कोरिंगा वन्यजीव अभयारण्य", m=("Mangroves", "मैंग्रोव", "खारफुटी")),
        it3("kolleru", "Kolleru Lake", "कोल्लेरु झील", "कोल्लेरू सरोवर", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
        it3("pulicat", "Pulicat Lake Bird Sanctuary", "पुलिकट झील पक्षी अभयारण्य", "पुलिकत सरोवर पक्षी अभयारण्य", m=("Flamingos", "फ़्लेमिंगो", "रोहित पक्षी")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("blackbuck", "Blackbuck (State animal)", "काला हिरण (राज्य पशु)", "काळवीट (राज्यप्राणी)"), it3("tiger", "Tiger", "बाघ", "वाघ"),
        it3("redsanders", "Red sanders", "लाल चंदन", "रक्तचंदन"), it3("pelican", "Spot-billed pelican", "चित्तीदार चोंच वाला पेलिकन", "ठिपकेदार चोचीचा पाणकोळी"),
        it3("olive", "Olive ridley turtle", "ओलिव रिडले कछुआ", "ऑलिव्ह रिडले कासव"), it3("fishingcat", "Fishing cat", "मछुआ बिल्ली", "मासेमार मांजर"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger estimate (Nagarjunasagar–Srisailam)", "बाघों का अनुमान (नागार्जुनसागर–श्रीशैलम)", "वाघांचा अंदाज (नागार्जुनसागर–श्रीशैलम)"), "ntca", "NTCA All India Tiger Estimation."),
        (L("Mangrove cover", "मैंग्रोव आवरण", "खारफुटी आच्छादन"), "fsi", "ISFR 2023 mangrove chapter."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "The Godavari and Krishna deltas are among India's oldest irrigated areas, watered by the Dowleswaram (Sir Arthur Cotton) and Prakasam barrages built in the 19th century. Upstream, the Srisailam and Nagarjuna Sagar dams on the Krishna are shared with Telangana, and the division of Krishna waters between the two States is managed by the Krishna River Management Board. Rayalaseema depends on canals such as the Telugu Ganga and Handri–Neeva that carry Krishna water south, and on groundwater; droughts are frequent there. The Polavaram project on the Godavari is meant to irrigate the uplands of the coastal districts and divert water to the Krishna delta.",
        "गोदावरी और कृष्णा डेल्टा भारत के सबसे पुराने सिंचित क्षेत्रों में हैं, जिन्हें 19वीं सदी में बने धवलेश्वरम (सर आर्थर कॉटन) और प्रकाशम बराज सींचते हैं। ऊपर की ओर कृष्णा पर श्रीशैलम और नागार्जुन सागर बाँध तेलंगाना के साथ साझा हैं, और दोनों राज्यों के बीच कृष्णा जल का बँटवारा कृष्णा नदी प्रबंधन बोर्ड देखता है। रायलसीमा तेलुगु गंगा और हंद्री–नीवा जैसी नहरों पर, जो कृष्णा का पानी दक्षिण ले जाती हैं, और भूजल पर निर्भर है; वहाँ सूखा अक्सर पड़ता है। गोदावरी पर पोलावरम परियोजना का उद्देश्य तटीय ज़िलों के ऊपरी भागों की सिंचाई करना और पानी को कृष्णा डेल्टा की ओर मोड़ना है।",
        "गोदावरी व कृष्णेचे त्रिभुज प्रदेश हे भारतातील सर्वांत जुन्या सिंचित भागांपैकी आहेत, ज्यांना एकोणिसाव्या शतकात बांधलेले धवलेश्वरम (सर आर्थर कॉटन) व प्रकाशम बंधारे पाणी देतात. वरच्या भागात कृष्णेवरील श्रीशैलम व नागार्जुन सागर धरणे तेलंगणासोबत सामायिक आहेत, आणि दोन्ही राज्यांमधील कृष्णेच्या पाण्याचे वाटप कृष्णा नदी व्यवस्थापन मंडळ पाहते. रायलसीमा तेलुगु गंगा व हंद्री–नीवा यांसारख्या कालव्यांवर, जे कृष्णेचे पाणी दक्षिणेकडे नेतात, आणि भूजलावर अवलंबून आहे; तिथे दुष्काळ वारंवार पडतो. गोदावरीवरील पोलावरम प्रकल्पाचा उद्देश किनारी जिल्ह्यांच्या उंचावरील भागांना सिंचन देणे आणि पाणी कृष्णा त्रिभुज प्रदेशाकडे वळवणे हा आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
        (L("Net irrigated area", "शुद्ध सिंचित क्षेत्र", "निव्वळ सिंचित क्षेत्र"), "india-gov", "Land-use statistics, Ministry of Agriculture."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Cyclones are the main natural hazard on the Andhra coast: the 1977 Diviseema cyclone killed thousands, and Hudhud (2014) badly damaged Visakhapatnam. Heavy rain causes floods in the deltas and in cities — Vijayawada was flooded in September 2024 when the Budameru stream overflowed. Heatwaves are severe in April and May, and Rayalaseema faces recurring drought.\n\nVisitors should follow IMD cyclone warnings on the coast, avoid the midday sun in summer, and use the official Tirumala Tirupati Devasthanams booking systems for darshan.",
        "चक्रवात आंध्र तट का मुख्य प्राकृतिक ख़तरा हैं: 1977 के दिविसीमा चक्रवात में हज़ारों लोग मारे गए, और हुदहुद (2014) ने विशाखापत्तनम को भारी नुक़सान पहुँचाया। भारी वर्षा से डेल्टा और शहरों में बाढ़ आती है — सितंबर 2024 में बुडमेरु नाले के उफनने से विजयवाड़ा में बाढ़ आई। अप्रैल और मई में लू तीव्र होती है, और रायलसीमा बार-बार सूखे का सामना करता है।\n\nपर्यटकों को तट पर आईएमडी की चक्रवात चेतावनियों का पालन करना चाहिए, गर्मियों में दोपहर की धूप से बचना चाहिए, और दर्शन के लिए तिरुमला तिरुपति देवस्थानम की आधिकारिक बुकिंग प्रणाली का उपयोग करना चाहिए।",
        "चक्रीवादळे हा आंध्र किनाऱ्यावरील मुख्य नैसर्गिक धोका आहे: 1977 च्या दिविसीमा चक्रीवादळात हजारो लोक मरण पावले, आणि हुदहुदने (2014) विशाखापट्टणमचे मोठे नुकसान केले. मुसळधार पावसामुळे त्रिभुज प्रदेशांत व शहरांत पूर येतात — सप्टेंबर 2024 मध्ये बुडमेरू ओढा फुगल्याने विजयवाड्यात पूर आला. एप्रिल-मेमध्ये उष्णतेच्या लाटा तीव्र असतात, आणि रायलसीमा वारंवार दुष्काळाला तोंड देतो.\n\nपर्यटकांनी किनाऱ्यावर आयएमडीच्या चक्रीवादळ इशाऱ्यांचे पालन करावे, उन्हाळ्यात दुपारचे ऊन टाळावे, आणि दर्शनासाठी तिरुमला तिरुपती देवस्थानमची अधिकृत आरक्षण प्रणाली वापरावी."),
        conf="Editorial"),
    emergency_table(("Andhra Pradesh", "आंध्र प्रदेश", "आंध्र प्रदेश")),
    lst("links", [
        it3("imd", "IMD weather and cyclone warnings", "आईएमडी मौसम और चक्रवात चेतावनियाँ", "आयएमडी हवामान व चक्रीवादळ इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official APSDMA address."),
        (L("Damage figures for major cyclones and floods", "बड़े चक्रवातों और बाढ़ों से हानि के आँकड़े", "मोठी चक्रीवादळे व पुरांच्या हानीचे आकडे"), "ndma", "Official memoranda / NDMA reports."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Andhra Pradesh has 20 registered Geographical Indications of its own in the GI Registry's list as on 31 December 2025, and shares two more: Banaganapalle mangoes with Telangana and Araku Valley Arabica coffee with Odisha. Crafts dominate — Srikalahasthi and Machilipatnam Kalamkari, Kondapalli and Etikoppaka toys, leather puppetry, Budithi bell-metal, Durgi and Allagadda stone carving, the Bobbili veena and Udayagiri wooden cutlery — along with the handloom saris of Uppada, Venkatagiri, Mangalagiri and Dharmavaram, Narasapur crochet lace and Ponduru khadi. Food GIs include Guntur Sannam chilli and three sweets: the Tirupati laddu, Bandar laddu and Atreyapuram pootharekulu.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में आंध्र प्रदेश के अपने 20 पंजीकृत भौगोलिक संकेतक हैं, और दो और साझा हैं: बंगनपल्ले आम तेलंगाना के साथ और अराकू घाटी अरेबिका कॉफ़ी ओडिशा के साथ। शिल्प प्रमुख हैं — श्रीकालहस्ती और मछलीपट्टनम कलमकारी, कोंडापल्ली और एटिकोप्पाका खिलौने, चमड़ा कठपुतली, बुदिथी घंटा-धातु, दुर्गी और आल्लगड्डा पत्थर नक्काशी, बोब्बिली वीणा और उदयगिरि लकड़ी की कटलरी — साथ में उप्पाडा, वेंकटगिरि, मंगलगिरि और धर्मावरम की हथकरघा साड़ियाँ, नरसापुर क्रोशिया लेस और पोंदुरु खादी। खाद्य जीआई में गुंटूर सन्नम मिर्च और तीन मिठाइयाँ हैं: तिरुपति लड्डू, बंदर लड्डू और आत्रेयपुरम पूतरेकुलु।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत आंध्र प्रदेशची स्वतःची 20 नोंदणीकृत भौगोलिक मानांकने आहेत, आणि आणखी दोन सामायिक आहेत: बंगनपल्ले आंबे तेलंगणासोबत आणि अराकू खोरे अरेबिका कॉफी ओडिशासोबत. हस्तकलेचे वर्चस्व आहे — श्रीकालहस्ती व मछलीपट्टणम कलमकारी, कोंडापल्ली व एटिकोप्पाका खेळणी, चामडी कठपुतळी, बुदिथी घंटा-धातू, दुर्गी व आल्लगड्डा दगडी कोरीवकाम, बोब्बिली वीणा आणि उदयगिरी लाकडी कटलरी — सोबत उप्पाडा, वेंकटगिरी, मंगळगिरी व धर्मावरमच्या हातमाग साड्या, नरसापूर क्रोशा लेस व पोंदुरू खादी. खाद्य जीआयमध्ये गुंटूर सन्नम मिरची आणि तीन मिठाया आहेत: तिरुपती लाडू, बंदर लाडू व आत्रेयपुरम पूतरेकुलू."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Pilgrimage brings the largest numbers: the Sri Venkateswara temple at Tirumala, Srisailam, Srikalahasti, Kanaka Durga at Vijayawada, Simhachalam and Annavaram. Visakhapatnam combines beaches, the submarine museum and the Kailasagiri hill; from there a scenic railway climbs to the Araku Valley and the Borra Caves. Buddhist sites at Amaravati, Nagarjunakonda, Thotlakonda and Bavikonda, the Vijayanagara murals of Lepakshi, the Gandikota gorge and the Belum Caves are other highlights, along with boat trips through the Papikonda hills on the Godavari.",
        "तीर्थयात्रा सबसे अधिक लोगों को लाती है: तिरुमला का श्री वेंकटेश्वर मंदिर, श्रीशैलम, श्रीकालहस्ती, विजयवाड़ा की कनक दुर्गा, सिंहाचलम और अन्नावरम। विशाखापत्तनम में समुद्र तट, पनडुब्बी संग्रहालय और कैलासगिरि पहाड़ी हैं; वहाँ से एक मनोरम रेल अराकू घाटी और बोर्रा गुफाओं तक चढ़ती है। अमरावती, नागार्जुनकोंडा, तोट्लाकोंडा और बाविकोंडा के बौद्ध स्थल, लेपाक्षी के विजयनगर भित्तिचित्र, गंडिकोटा घाटी और बेलम गुफाएँ अन्य आकर्षण हैं, साथ में गोदावरी पर पापिकोंडा पहाड़ियों के बीच नौका-यात्रा।",
        "तीर्थयात्रा सर्वाधिक लोकांना आणते: तिरुमलाचे श्री वेंकटेश्वर मंदिर, श्रीशैलम, श्रीकालहस्ती, विजयवाड्याची कनकदुर्गा, सिंहाचलम व अन्नवरम. विशाखापट्टणममध्ये समुद्रकिनारे, पाणबुडी संग्रहालय व कैलासगिरी टेकडी आहेत; तिथून एक निसर्गरम्य रेल्वे अराकू खोरे व बोर्रा गुहांपर्यंत चढते. अमरावती, नागार्जुनकोंडा, तोट्लाकोंडा व बाविकोंडा येथील बौद्ध स्थळे, लेपाक्षीची विजयनगर भित्तिचित्रे, गंडिकोटा घळ व बेलम गुहा ही इतर आकर्षणे आहेत, सोबत गोदावरीवर पापिकोंडा डोंगरांतून नौकाविहार."),
        conf="Editorial"),
    lst("places", [
        it3("tirumala", "Tirumala–Tirupati", "तिरुमला–तिरुपति", "तिरुमला–तिरुपती", m=("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        it3("vizag", "Visakhapatnam", "विशाखापत्तनम", "विशाखापट्टणम", m=("Beaches, hills", "समुद्र तट, पहाड़ियाँ", "समुद्रकिनारे, टेकड्या")),
        it3("araku", "Araku Valley and Borra Caves", "अराकू घाटी और बोर्रा गुफाएँ", "अराकू खोरे व बोर्रा गुहा", m=("Hills, coffee", "पहाड़, कॉफ़ी", "डोंगर, कॉफी")),
        it3("srisailam", "Srisailam", "श्रीशैलम", "श्रीशैलम", m=("Jyotirlinga, Nallamala", "ज्योतिर्लिंग, नल्लमला", "ज्योतिर्लिंग, नल्लमला")),
        it3("lepakshi", "Lepakshi", "लेपाक्षी", "लेपाक्षी", m=("Vijayanagara art", "विजयनगर कला", "विजयनगर कला")),
        it3("gandikota", "Gandikota and Belum Caves", "गंडिकोटा और बेलम गुफाएँ", "गंडिकोटा व बेलम गुहा", m=("Landscapes", "भूदृश्य", "निसर्गदृश्ये")),
        it3("amaravati", "Amaravati and Nagarjunakonda", "अमरावती और नागार्जुनकोंडा", "अमरावती व नागार्जुनकोंडा", m=("Buddhist heritage", "बौद्ध धरोहर", "बौद्ध वारसा")),
        it3("papikonda", "Papikonda boat trip on the Godavari", "गोदावरी पर पापिकोंडा नौका-यात्रा", "गोदावरीवर पापिकोंडा नौकाविहार", m=("River", "नदी", "नदी")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Tirupati and Tirumala, with Srikalahasti.", "तिरुपति और तिरुमला, साथ में श्रीकालहस्ती।", "तिरुपती व तिरुमला, सोबत श्रीकालहस्ती.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Visakhapatnam, then the train to Araku and the Borra Caves.", "विशाखापत्तनम, फिर अराकू और बोर्रा गुफाओं तक रेल।", "विशाखापट्टणम, नंतर अराकू व बोर्रा गुहांपर्यंत रेल्वे.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Vijayawada, Amaravati, Kondapalli and the Godavari at Rajamahendravaram.", "विजयवाड़ा, अमरावती, कोंडापल्ली और राजमहेंद्रवरम में गोदावरी।", "विजयवाडा, अमरावती, कोंडापल्ली व राजमहेंद्रवरम येथील गोदावरी.")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Rayalaseema: Lepakshi, Gandikota, Belum Caves and Srisailam.", "रायलसीमा: लेपाक्षी, गंडिकोटा, बेलम गुफाएँ और श्रीशैलम।", "रायलसीमा: लेपाक्षी, गंडिकोटा, बेलम गुहा व श्रीशैलम.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("apt", "Andhra Pradesh Tourism (official)", "आंध्र प्रदेश पर्यटन (आधिकारिक)", "आंध्र प्रदेश पर्यटन (अधिकृत)", url="https://tourism.ap.gov.in", src="india-gov"),
        it3("ttd", "Tirumala Tirupati Devasthanams", "तिरुमला तिरुपति देवस्थानम", "तिरुमला तिरुपती देवस्थानम", url="https://www.tirumala.org", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Alluri Sitharama Raju", "अल्लूरी सीताराम राजू", "अल्लुरी सीताराम राजू"), ("Anakapalli", "अनकापल्ली", "अनकापल्ली"), ("Ananthapuramu", "अनंतपुरमु", "अनंतपुरमू"),
    ("Annamayya", "अन्नमय्या", "अन्नमय्या"), ("Bapatla", "बापटला", "बापटला"), ("Chittoor", "चित्तूर", "चित्तूर"),
    ("Dr. B. R. Ambedkar Konaseema", "डॉ. बी. आर. आंबेडकर कोनसीमा", "डॉ. बी. आर. आंबेडकर कोनसीमा"), ("East Godavari", "पूर्वी गोदावरी", "पूर्व गोदावरी"), ("Eluru", "एलुरु", "एलुरू"),
    ("Guntur", "गुंटूर", "गुंटूर"), ("Kakinada", "काकीनाडा", "काकिनाडा"), ("Krishna", "कृष्णा", "कृष्णा"), ("Kurnool", "कुरनूल", "कर्नूल"),
    ("Markapuram", "मार्कापुरम", "मार्कापुरम"), ("Nandyal", "नंद्याल", "नंद्याल"), ("NTR", "एनटीआर", "एनटीआर"), ("Palnadu", "पलनाडु", "पलनाडू"),
    ("Parvathipuram Manyam", "पार्वतीपुरम मन्यम", "पार्वतीपुरम मन्यम"), ("Polavaram", "पोलावरम", "पोलावरम"), ("Prakasam", "प्रकाशम", "प्रकाशम"),
    ("Sri Potti Sriramulu Nellore", "श्री पोट्टि श्रीरामुलु नेल्लोर", "श्री पोट्टी श्रीरामुलू नेल्लोर"), ("Sri Sathya Sai", "श्री सत्य साईं", "श्री सत्य साई"),
    ("Srikakulam", "श्रीकाकुलम", "श्रीकाकुलम"), ("Tirupati", "तिरुपति", "तिरुपती"), ("Visakhapatnam", "विशाखापत्तनम", "विशाखापट्टणम"),
    ("Vizianagaram", "विजयनगरम", "विजयनगरम"), ("West Godavari", "पश्चिमी गोदावरी", "पश्चिम गोदावरी"), ("YSR Kadapa", "वाईएसआर कडपा", "वायएसआर कडपा"),
]
assert len(DISTRICTS) == 28, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("amaravati", ("Amaravati", "अमरावती", "अमरावती"), ("State capital under construction on the Krishna; seat of the Secretariat, Legislature and High Court.", "कृष्णा के किनारे निर्माणाधीन राजधानी; सचिवालय, विधानमंडल और उच्च न्यायालय का स्थान।", "कृष्णेकाठी उभारली जात असलेली राजधानी; सचिवालय, विधिमंडळ व उच्च न्यायालयाचे ठिकाण."), ("Capital", "राजधानी", "राजधानी")),
        city("vizag", ("Visakhapatnam", "विशाखापत्तनम", "विशाखापट्टणम"), ("Largest city; port, steel, navy and IT.", "सबसे बड़ा शहर; बंदरगाह, इस्पात, नौसेना और आईटी।", "सर्वांत मोठे शहर; बंदर, पोलाद, नौदल व आयटी."), ("Port city", "बंदरगाह नगर", "बंदर शहर")),
        city("vijayawada", ("Vijayawada", "विजयवाड़ा", "विजयवाडा"), ("Commercial centre and railway junction on the Krishna.", "कृष्णा पर वाणिज्यिक केंद्र और रेलवे जंक्शन।", "कृष्णेवरील व्यापारी केंद्र व रेल्वे जंक्शन."), ("Commerce", "वाणिज्य", "व्यापार")),
        city("guntur", ("Guntur", "गुंटूर", "गुंटूर"), ("Chilli and tobacco trade; education centre.", "मिर्च और तंबाकू व्यापार; शिक्षा केंद्र।", "मिरची व तंबाखू व्यापार; शिक्षण केंद्र."), ("Agri-trade", "कृषि व्यापार", "कृषी व्यापार")),
        city("tirupati", ("Tirupati", "तिरुपति", "तिरुपती"), ("Temple town at the foot of Tirumala; universities and IIT.", "तिरुमला की तलहटी में मंदिर नगर; विश्वविद्यालय और आईआईटी।", "तिरुमलाच्या पायथ्याशी मंदिरनगरी; विद्यापीठे व आयआयटी."), ("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        city("nellore", ("Nellore", "नेल्लोर", "नेल्लोर"), ("Rice, aquaculture and the Krishnapatnam port.", "धान, जलकृषि और कृष्णापट्टनम बंदरगाह।", "भात, जलशेती व कृष्णापट्टणम बंदर."), ("Coast", "तट", "किनारा")),
        city("kurnool", ("Kurnool", "कुरनूल", "कर्नूल"), ("Capital of Andhra State (1953–56); gateway to Rayalaseema.", "आंध्र राज्य की राजधानी (1953–56); रायलसीमा का प्रवेश द्वार।", "आंध्र राज्याची राजधानी (1953–56); रायलसीमाचे प्रवेशद्वार."), ("Rayalaseema", "रायलसीमा", "रायलसीमा")),
        city("rjy", ("Rajamahendravaram", "राजमहेंद्रवरम", "राजमहेंद्रवरम"), ("Cultural town on the Godavari; Pushkaram bathing festival.", "गोदावरी पर सांस्कृतिक नगर; पुष्करम स्नान पर्व।", "गोदावरीवरील सांस्कृतिक शहर; पुष्करम स्नानपर्व."), ("Heritage", "धरोहर", "वारसा")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 28 districts (alphabetical)", "28 ज़िले (वर्णानुक्रम)", "28 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    lst("dsrc", [it3("etv", "ETV Bharat: Cabinet approves two new districts (30 Dec 2025)", "ईटीवी भारत: मंत्रिमंडल ने दो नए ज़िलों को मंज़ूरी दी (30 दिसंबर 2025)", "ईटीव्ही भारत: मंत्रिमंडळाकडून दोन नव्या जिल्ह्यांना मंजुरी (30 डिसेंबर 2025)", url=DIST, src="etv-bharat")],
        title=L("Source for the district count", "ज़िलों की संख्या का स्रोत", "जिल्हा संख्येचा स्रोत"), conf="Third-party verified"),
    gaps("g", [
        (L("Official district list (State gazette notification)", "आधिकारिक ज़िला सूची (राज्य राजपत्र अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य राजपत्र अधिसूचना)"), "india-gov", "Link the State notification forming Markapuram and Polavaram districts."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Andhra Pradesh has produced several pioneering sportspeople. Weightlifter Karnam Malleswari of Srikakulam won bronze at the Sydney Olympics in 2000, the first Olympic medal won by an Indian woman. Pullela Gopichand, born in Prakasam district, won the All England badminton title in 2001 and became India's best-known badminton coach. Koneru Humpy of Gudivada is one of the world's leading women chess players and a world rapid champion. Cricket is followed keenly, with international matches at the ACA–VDCA Stadium in Visakhapatnam.",
        "आंध्र प्रदेश ने कई अग्रणी खिलाड़ी दिए हैं। श्रीकाकुलम की भारोत्तोलक कर्णम मल्लेश्वरी ने 2000 के सिडनी ओलंपिक में कांस्य जीता — किसी भारतीय महिला का पहला ओलंपिक पदक। प्रकाशम ज़िले में जन्मे पुल्लेला गोपीचंद ने 2001 में ऑल इंग्लैंड बैडमिंटन ख़िताब जीता और भारत के सबसे प्रसिद्ध बैडमिंटन कोच बने। गुडिवाडा की कोनेरु हम्पी दुनिया की प्रमुख महिला शतरंज खिलाड़ियों में हैं और विश्व रैपिड चैंपियन रही हैं। क्रिकेट उत्साह से देखा जाता है, और विशाखापत्तनम के एसीए–वीडीसीए स्टेडियम में अंतरराष्ट्रीय मैच होते हैं।",
        "आंध्र प्रदेशने अनेक अग्रणी खेळाडू दिले आहेत. श्रीकाकुलमच्या भारोत्तोलक कर्णम मल्लेश्वरी यांनी 2000 च्या सिडनी ऑलिम्पिकमध्ये कांस्यपदक जिंकले — भारतीय स्त्रीचे पहिले ऑलिम्पिक पदक. प्रकाशम जिल्ह्यात जन्मलेल्या पुल्लेला गोपीचंद यांनी 2001 मध्ये ऑल इंग्लंड बॅडमिंटन विजेतेपद जिंकले आणि ते भारताचे सर्वांत प्रसिद्ध बॅडमिंटन प्रशिक्षक झाले. गुडिवाडाच्या कोनेरू हम्पी जगातील आघाडीच्या महिला बुद्धिबळपटूंपैकी असून जागतिक रॅपिड विजेत्या राहिल्या आहेत. क्रिकेट उत्साहाने पाहिले जाते, आणि विशाखापट्टणमच्या एसीए–व्हीडीसीए स्टेडियमवर आंतरराष्ट्रीय सामने होतात."),
        conf="Editorial"),
    lst("venues", [
        it3("vdca", "ACA–VDCA Cricket Stadium, Visakhapatnam", "एसीए–वीडीसीए क्रिकेट स्टेडियम, विशाखापत्तनम", "एसीए–व्हीडीसीए क्रिकेट स्टेडियम, विशाखापट्टणम"),
        it3("igmc", "Indira Gandhi Municipal Corporation Stadium, Vijayawada", "इंदिरा गांधी नगर निगम स्टेडियम, विजयवाड़ा", "इंदिरा गांधी महापालिका स्टेडियम, विजयवाडा"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from Andhra Pradesh (official list)", "आंध्र प्रदेश के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "आंध्र प्रदेशचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Sports Authority of Andhra Pradesh.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("annamacharya", ("Annamacharya", "अन्नमाचार्य", "अन्नमाचार्य"), ("15th-century poet-saint of Tallapaka; composed songs to Lord Venkateswara.", "ताल्लपाका के 15वीं सदी के संत-कवि; भगवान वेंकटेश्वर के लिए गीत रचे।", "ताळ्ळपाकाचे पंधराव्या शतकातील संतकवी; भगवान वेंकटेश्वरासाठी पदे रचली."), ("Music", "संगीत", "संगीत")),
        person("vemana", ("Vemana", "वेमना", "वेमना"), ("Poet of short, popular verses on morals and society.", "नैतिकता और समाज पर छोटी, लोकप्रिय कविताओं के कवि।", "नीती व समाजावरील छोट्या, लोकप्रिय कवितांचे कवी."), ("Literature", "साहित्य", "साहित्य")),
        person("gurajada", ("Gurajada Apparao", "गुरजाड अप्पाराव", "गुरजाड अप्पाराव"), ("Playwright of 'Kanyasulkam' and pioneer of modern Telugu writing.", "'कन्याशुल्कम' के नाटककार और आधुनिक तेलुगु लेखन के अग्रदूत।", "'कन्याशुल्कम'चे नाटककार व आधुनिक तेलुगु लेखनाचे प्रणेते."), ("Literature", "साहित्य", "साहित्य")),
        person("alluri", ("Alluri Sitarama Raju", "अल्लूरी सीताराम राजू", "अल्लुरी सीताराम राजू"), ("Led the Rampa rebellion of tribal people against British rule (1922–24).", "ब्रिटिश शासन के विरुद्ध आदिवासियों के रम्पा विद्रोह (1922–24) का नेतृत्व किया।", "इंग्रजी राजवटीविरुद्ध आदिवासींच्या रम्पा उठावाचे (1922–24) नेतृत्व केले."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("pingali", ("Pingali Venkayya", "पिंगलि वेंकय्या", "पिंगळी वेंकय्या"), ("Designed the flag on which India's national flag is based.", "उस ध्वज की रूपरेखा बनाई जिस पर भारत का राष्ट्रीय ध्वज आधारित है।", "ज्या ध्वजावर भारताचा राष्ट्रध्वज आधारित आहे त्याची रचना केली."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("prakasam", ("Tanguturi Prakasam", "तंगुटूरि प्रकाशम", "तंगुटुरी प्रकाशम"), ("'Andhra Kesari'; first Chief Minister of Andhra State.", "'आंध्र केसरी'; आंध्र राज्य के पहले मुख्यमंत्री।", "'आंध्र केसरी'; आंध्र राज्याचे पहिले मुख्यमंत्री."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("sriramulu", ("Potti Sriramulu", "पोट्टि श्रीरामुलु", "पोट्टी श्रीरामुलू"), ("Fasted unto death in 1952 for a Telugu-speaking State.", "1952 में तेलुगु-भाषी राज्य के लिए आमरण अनशन किया।", "1952 मध्ये तेलुगुभाषक राज्यासाठी आमरण उपोषण केले."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("sanjiva", ("Neelam Sanjiva Reddy", "नीलम संजीव रेड्डी", "नीलम संजीव रेड्डी"), ("First Chief Minister of Andhra Pradesh and sixth President of India.", "आंध्र प्रदेश के पहले मुख्यमंत्री और भारत के छठे राष्ट्रपति।", "आंध्र प्रदेशचे पहिले मुख्यमंत्री व भारताचे सहावे राष्ट्रपती."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("ntr", ("N. T. Rama Rao", "एन. टी. रामाराव", "एन. टी. रामाराव"), ("Film star who founded the Telugu Desam Party (1982) and became Chief Minister.", "फ़िल्म स्टार जिन्होंने तेलुगु देशम पार्टी (1982) की स्थापना की और मुख्यमंत्री बने।", "चित्रपट अभिनेते, ज्यांनी तेलुगु देसम पक्षाची (1982) स्थापना केली व मुख्यमंत्री झाले."), ("Cinema, politics", "सिनेमा, राजनीति", "चित्रपट, राजकारण")),
        person("spb", ("S. P. Balasubrahmanyam", "एस. पी. बालसुब्रह्मण्यम", "एस. पी. बालसुब्रह्मण्यम"), ("Playback singer from Nellore who sang in many Indian languages.", "नेल्लोर के पार्श्वगायक, जिन्होंने कई भारतीय भाषाओं में गाया।", "नेल्लोरचे पार्श्वगायक, ज्यांनी अनेक भारतीय भाषांत गायन केले."), ("Music", "संगीत", "संगीत")),
        person("malleswari", ("Karnam Malleswari", "कर्णम मल्लेश्वरी", "कर्णम मल्लेश्वरी"), ("First Indian woman to win an Olympic medal (Sydney 2000).", "ओलंपिक पदक जीतने वाली पहली भारतीय महिला (सिडनी 2000)।", "ऑलिम्पिक पदक जिंकणारी पहिली भारतीय महिला (सिडनी 2000)."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Telugu-speaking people from Andhra Pradesh form a large and well-established diaspora. Many engineers, doctors and students have settled in the United States, where Telugu associations are active in most large cities, and in the United Kingdom, Canada and Australia. Workers from the Godavari districts and Rayalaseema have long gone to the Gulf countries. Within India, large Telugu communities live in Hyderabad, Bengaluru, Chennai and Mumbai, and older migrations took Telugu people to Myanmar, Malaysia, Mauritius, Fiji and South Africa.",
        "आंध्र प्रदेश के तेलुगु-भाषी लोग एक बड़ा और सुस्थापित प्रवासी समुदाय बनाते हैं। बहुत से इंजीनियर, डॉक्टर और छात्र अमेरिका में बसे हैं, जहाँ अधिकांश बड़े शहरों में तेलुगु संघ सक्रिय हैं, और ब्रिटेन, कनाडा और ऑस्ट्रेलिया में भी। गोदावरी ज़िलों और रायलसीमा के श्रमिक लंबे समय से खाड़ी देशों में जाते रहे हैं। भारत में हैदराबाद, बेंगलूरु, चेन्नई और मुंबई में बड़े तेलुगु समुदाय हैं, और पुराने प्रवास तेलुगु लोगों को म्यांमार, मलेशिया, मॉरीशस, फ़िजी और दक्षिण अफ़्रीका ले गए।",
        "आंध्र प्रदेशातील तेलुगुभाषक लोकांचा मोठा व सुस्थापित परदेशस्थ समुदाय आहे. अनेक अभियंते, डॉक्टर व विद्यार्थी अमेरिकेत स्थायिक झाले आहेत, जिथे बहुतेक मोठ्या शहरांत तेलुगु संघटना सक्रिय आहेत, तसेच ब्रिटन, कॅनडा व ऑस्ट्रेलियातही. गोदावरी जिल्हे व रायलसीमामधील कामगार दीर्घकाळापासून आखाती देशांत जात आहेत. भारतात हैदराबाद, बंगळूरु, चेन्नई व मुंबईत मोठे तेलुगु समुदाय आहेत, आणि जुन्या स्थलांतरांनी तेलुगु लोकांना म्यानमार, मलेशिया, मॉरिशस, फिजी व दक्षिण आफ्रिकेत नेले."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants and internal migrants", "प्रवासियों और आंतरिक प्रवासियों की संख्या", "परदेशी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; MEA."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Andhra Pradesh portal", "आंध्र प्रदेश सरकार पोर्टल", "आंध्र प्रदेश शासन संकेतस्थळ", url="https://www.ap.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Andhra Pradesh Tourism", "आंध्र प्रदेश पर्यटन", "आंध्र प्रदेश पर्यटन", url="https://tourism.ap.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Visakhapatnam", "विशाखापत्तनम", "विशाखापट्टणम"), "0891"], [L("Vijayawada", "विजयवाड़ा", "विजयवाडा"), "0866"], [L("Guntur", "गुंटूर", "गुंटूर"), "0863"],
           [L("Tirupati", "तिरुपति", "तिरुपती"), "0877"], [L("Nellore", "नेल्लोर", "नेल्लोर"), "0861"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("State e-services portal — verified link", "राज्य ई-सेवा पोर्टल — सत्यापित लिंक", "राज्य ई-सेवा संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "Certificates and services portal of the State."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("andhra", ("Andhra State (1953) was the first Indian State formed on the basis of language.", "आंध्र राज्य (1953) भाषा के आधार पर बना पहला भारतीय राज्य था।", "आंध्र राज्य (1953) हे भाषेच्या आधारावर बनलेले पहिले भारतीय राज्य होते.")),
        triv("flag", ("Pingali Venkayya of Machilipatnam designed the flag on which India's national flag is based.", "मछलीपट्टनम के पिंगलि वेंकय्या ने उस ध्वज की रूपरेखा बनाई जिस पर भारत का राष्ट्रीय ध्वज आधारित है।", "मछलीपट्टणमच्या पिंगळी वेंकय्या यांनी ज्या ध्वजावर भारताचा राष्ट्रध्वज आधारित आहे त्याची रचना केली.")),
        triv("shar", ("All of ISRO's orbital launches lift off from Sriharikota, on the coast of Tirupati district.", "इसरो के सभी कक्षीय प्रक्षेपण तिरुपति ज़िले के तट पर श्रीहरिकोटा से होते हैं।", "इस्रोची सर्व कक्षीय प्रक्षेपणे तिरुपती जिल्ह्याच्या किनाऱ्यावरील श्रीहरिकोट्याहून होतात.")),
        triv("laddu", ("The Tirupati laddu is a registered Geographical Indication (filed 2008).", "तिरुपति लड्डू पंजीकृत भौगोलिक संकेतक है (2008 में दायर)।", "तिरुपती लाडू हे नोंदणीकृत भौगोलिक मानांकन आहे (2008 मध्ये दाखल)."), GI_PDF, "gi-registry"),
        triv("kolleru", ("Kolleru Lake, a Ramsar site of 90,100 ha, lies between the Godavari and Krishna deltas.", "90,100 हेक्टेयर का रामसर स्थल कोल्लेरु झील गोदावरी और कृष्णा डेल्टाओं के बीच है।", "90,100 हेक्टरचे रामसर स्थळ कोल्लेरू सरोवर गोदावरी व कृष्णा त्रिभुज प्रदेशांदरम्यान आहे."), RAMSAR, "indian-wetlands"),
        triv("ls", ("The State elects 25 members to the Lok Sabha.", "राज्य से लोकसभा के 25 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 25 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("ap mod3 ok")
