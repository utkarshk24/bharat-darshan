"""West Bengal modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-WB"
wb = read("regions/IN-WB.json")["metrics"]; ind = read("india.json")["metrics"]

RAMSAR_WB = [
    ("East Kolkata Wetlands", "पूर्वी कोलकाता आर्द्रभूमि", "पूर्व कोलकाता पाणथळ", "19 Aug 2002", "12,500"),
    ("Sundarban Wetland", "सुंदरबन आर्द्रभूमि", "सुंदरबन पाणथळ", "30 Jan 2019", "4,23,000"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About 19% of West Bengal is forest (ISFR 2023), in two very different landscapes. In the south, the Sundarbans — shared with Bangladesh — are the largest mangrove forest in the world, a maze of tidal channels and islands home to Royal Bengal tigers that swim between them, estuarine crocodiles, fishing cats and Gangetic and Irrawaddy dolphins. In the north, the forests of the Terai and the Dooars — Jaldapara, Gorumara and Buxa — hold one-horned rhinoceroses, elephants, gaur and leopards, while the high forests of Singalila and Neora Valley near Darjeeling shelter red pandas.\n\nThe State has two Ramsar sites: the Sundarban Wetland, at 4,23,000 ha the largest in India, and the East Kolkata Wetlands, which naturally treat much of the city's wastewater while supporting fish farms and vegetable fields.",
        "पश्चिम बंगाल का लगभग 19% भाग वन है (आईएसएफ़आर 2023), जो दो बिल्कुल अलग भूदृश्यों में है। दक्षिण में सुंदरबन — जो बांग्लादेश के साथ साझा है — दुनिया का सबसे बड़ा मैंग्रोव वन है, ज्वारीय नालों और द्वीपों की भूलभुलैया, जहाँ उनके बीच तैरने वाले रॉयल बंगाल टाइगर, खारे पानी के मगरमच्छ, मछुआ बिल्लियाँ और गंगा व इरावदी डॉल्फ़िन रहती हैं। उत्तर में तराई और डुआर्स के वन — जलदापाड़ा, गोरुमारा और बक्सा — एक सींग वाले गैंडे, हाथी, गौर और तेंदुए रखते हैं, जबकि दार्जिलिंग के पास सिंगालीला और नेओरा घाटी के ऊँचे वन लाल पांडा का आश्रय हैं।\n\nराज्य में दो रामसर स्थल हैं: सुंदरबन आर्द्रभूमि, जो 4,23,000 हेक्टेयर के साथ भारत में सबसे बड़ी है, और पूर्वी कोलकाता आर्द्रभूमि, जो शहर के अधिकांश अपशिष्ट जल का प्राकृतिक उपचार करती है और मछली तालाबों व सब्ज़ी के खेतों को सहारा देती है।",
        "पश्चिम बंगालचा सुमारे 19% भाग वनाच्छादित आहे (आयएसएफआर 2023), आणि तो दोन अगदी वेगळ्या प्रदेशांत आहे. दक्षिणेला सुंदरबन — बांगलादेशसोबत सामायिक — हे जगातील सर्वांत मोठे खारफुटीचे जंगल आहे; भरती-ओहोटीच्या खाड्या व बेटांच्या चक्रव्यूहात त्यांच्यामधून पोहणारे रॉयल बंगाल वाघ, खाऱ्या पाण्यातील मगरी, मासेमार मांजरी आणि गांगेय व इरावदी डॉल्फिन राहतात. उत्तरेला तराई व डुआर्सची जंगले — जलदापाडा, गोरुमारा व बक्सा — एकशिंगी गेंडे, हत्ती, गवे व बिबटे राखतात, तर दार्जिलिंगजवळील सिंगालीला व नेओरा खोऱ्यातील उंचावरची जंगले लाल पांडाचे आश्रयस्थान आहेत.\n\nराज्यात दोन रामसर स्थळे आहेत: सुंदरबन पाणथळ — 4,23,000 हेक्टरसह भारतातील सर्वांत मोठे — आणि पूर्व कोलकाता पाणथळ, जे शहराच्या बहुतांश सांडपाण्यावर नैसर्गिक प्रक्रिया करते आणि मत्स्यतळी व भाजीपाल्याच्या शेतांना आधार देते."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(16832.33, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(16782.11, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), wb["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(2, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026 (India total 99)."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_WB], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026.", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी.")),
    lst("protected", [
        it3("sundarban", "Sundarban Tiger Reserve and National Park", "सुंदरबन बाघ अभयारण्य और राष्ट्रीय उद्यान", "सुंदरबन व्याघ्र प्रकल्प व राष्ट्रीय उद्यान", m=("UNESCO 1987", "यूनेस्को 1987", "युनेस्को 1987")),
        it3("buxa", "Buxa Tiger Reserve", "बक्सा बाघ अभयारण्य", "बक्सा व्याघ्र प्रकल्प", m=("Alipurduar", "अलीपुरद्वार", "अलिपूरद्वार")),
        it3("jaldapara", "Jaldapara National Park", "जलदापाड़ा राष्ट्रीय उद्यान", "जलदापाडा राष्ट्रीय उद्यान", m=("One-horned rhino", "एक सींग वाला गैंडा", "एकशिंगी गेंडा")),
        it3("gorumara", "Gorumara National Park", "गोरुमारा राष्ट्रीय उद्यान", "गोरुमारा राष्ट्रीय उद्यान", m=("Dooars", "डुआर्स", "डुआर्स")),
        it3("neora", "Neora Valley National Park", "नेओरा घाटी राष्ट्रीय उद्यान", "नेओरा खोरे राष्ट्रीय उद्यान", m=("Red panda", "लाल पांडा", "लाल पांडा")),
        it3("singalila", "Singalila National Park", "सिंगालीला राष्ट्रीय उद्यान", "सिंगालीला राष्ट्रीय उद्यान", m=("Sandakphu trek", "संदकफू ट्रेक", "संदकफू ट्रेक")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("tiger", "Royal Bengal tiger", "रॉयल बंगाल टाइगर", "रॉयल बंगाल वाघ"), it3("fishingcat", "Fishing cat (State animal)", "मछुआ बिल्ली (राज्य पशु)", "मासेमार मांजर (राज्यप्राणी)"),
        it3("rhino", "One-horned rhinoceros", "एक सींग वाला गैंडा", "एकशिंगी गेंडा"), it3("redpanda", "Red panda", "लाल पांडा", "लाल पांडा"),
        it3("croc", "Estuarine crocodile", "खारे पानी का मगरमच्छ", "खाऱ्या पाण्यातील मगर"), it3("dolphin", "Gangetic dolphin", "गंगा डॉल्फ़िन", "गांगेय डॉल्फिन"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger estimates (Sundarban, Buxa)", "बाघों का अनुमान (सुंदरबन, बक्सा)", "वाघांचा अंदाज (सुंदरबन, बक्सा)"), "ntca", "NTCA All India Tiger Estimation."),
        (L("Mangrove cover", "मैंग्रोव आवरण", "खारफुटी आच्छादन"), "fsi", "ISFR 2023 mangrove chapter."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "West Bengal has plenty of water overall but serious problems of quality and timing. Arsenic in groundwater affects large parts of the delta districts — Malda, Murshidabad, Nadia, North 24 Parganas and others — and fluoride occurs in some western districts, which has led to piped surface-water supply schemes. The Farakka Barrage diverts Ganga water into the Hooghly to keep Kolkata's port navigable. Floods are frequent in the lower Damodar, Ajay and Rupnarayan basins and in the north, while the western plateau districts are drier. In the Sundarbans, rising salinity and embankment breaches after cyclones damage farmland and drinking water.",
        "पश्चिम बंगाल में कुल मिलाकर पानी प्रचुर है, लेकिन गुणवत्ता और समय की गंभीर समस्याएँ हैं। डेल्टा के ज़िलों — मालदा, मुर्शिदाबाद, नदिया, उत्तर 24 परगना और अन्य — के बड़े हिस्सों में भूजल में आर्सेनिक है, और कुछ पश्चिमी ज़िलों में फ़्लोराइड, जिससे पाइप से सतही जल आपूर्ति योजनाएँ बनी हैं। फ़रक्का बराज गंगा का पानी हुगली में मोड़ता है ताकि कोलकाता का बंदरगाह नौवहन योग्य रहे। निचले दामोदर, अजय और रूपनारायण बेसिन में और उत्तर में बाढ़ अक्सर आती है, जबकि पश्चिमी पठारी ज़िले अधिक सूखे हैं। सुंदरबन में बढ़ती लवणता और चक्रवातों के बाद तटबंधों के टूटने से खेती और पेयजल को नुक़सान होता है।",
        "पश्चिम बंगालमध्ये एकूण पाणी भरपूर आहे, पण गुणवत्ता व वेळेच्या गंभीर समस्या आहेत. त्रिभुज प्रदेशातील जिल्ह्यांच्या — मालदा, मुर्शिदाबाद, नदिया, उत्तर 24 परगणा व इतर — मोठ्या भागांत भूजलात आर्सेनिक आहे, आणि काही पश्चिमी जिल्ह्यांत फ्लोराइड, त्यामुळे नळाद्वारे भूपृष्ठजल पुरवठा योजना उभारल्या गेल्या आहेत. कोलकाता बंदर जलवाहतुकीयोग्य राहावे म्हणून फरक्का बंधारा गंगेचे पाणी हुगळीत वळवतो. खालच्या दामोदर, अजय व रूपनारायण खोऱ्यांत आणि उत्तरेत वारंवार पूर येतात, तर पश्चिमेकडील पठारी जिल्हे अधिक कोरडे आहेत. सुंदरबनमध्ये वाढती क्षारता आणि चक्रीवादळांनंतर बांध फुटल्याने शेती व पिण्याच्या पाण्याचे नुकसान होते."),
        conf="Editorial"),
    gaps("g", [
        (L("Arsenic-affected habitations", "आर्सेनिक प्रभावित बस्तियाँ", "आर्सेनिकबाधित वस्त्या"), "india-gov", "Jal Jeevan Mission water-quality data."),
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Cyclones from the Bay of Bengal are West Bengal's most damaging hazard: Aila (2009), Amphan (2020) and Yaas (2021) devastated the Sundarbans and the coast. Floods affect the lower Gangetic plain and the north in heavy monsoons, landslides cut hill roads around Darjeeling and Kalimpong, and kalbaishakhi storms and lightning are common before the monsoon. Parts of the north lie in a high seismic zone.\n\nFor visitors, the main precautions are watching cyclone warnings on the coast and in the Sundarbans, checking road conditions in the hills during the monsoon, and travelling in the Sundarbans only with licensed boats and guides.",
        "बंगाल की खाड़ी के चक्रवात पश्चिम बंगाल का सबसे विनाशकारी ख़तरा हैं: आइला (2009), अम्फान (2020) और यास (2021) ने सुंदरबन और तट को तबाह किया। भारी मानसून में निचले गंगा मैदान और उत्तर में बाढ़ आती है, भूस्खलन दार्जिलिंग और कालिम्पोंग के आसपास पहाड़ी सड़कें काट देते हैं, और मानसून से पहले कालबैसाखी आँधी और आकाशीय बिजली आम हैं। उत्तर के कुछ हिस्से ऊँचे भूकंपीय क्षेत्र में हैं।\n\nपर्यटकों के लिए मुख्य सावधानियाँ हैं: तट और सुंदरबन में चक्रवात चेतावनियों पर नज़र रखना, मानसून में पहाड़ों की सड़कों की स्थिति जाँचना, और सुंदरबन में केवल लाइसेंसशुदा नावों और गाइडों के साथ जाना।",
        "बंगालच्या उपसागरातील चक्रीवादळे हा पश्चिम बंगालवरील सर्वांत विनाशकारी धोका आहे: आयला (2009), अम्फान (2020) व यास (2021) यांनी सुंदरबन व किनारपट्टी उद्ध्वस्त केली. मुसळधार पावसाळ्यात खालच्या गांगेय मैदानात व उत्तरेत पूर येतात, दार्जिलिंग व कालिम्पोंगभोवती दरडी कोसळून डोंगरी रस्ते बंद होतात, आणि मान्सूनपूर्वी कालबैसाखी वादळे व वीज कोसळणे नेहमीचे आहे. उत्तरेकडील काही भाग अधिक भूकंपप्रवण क्षेत्रात आहेत.\n\nपर्यटकांसाठी मुख्य काळजी: किनाऱ्यावर व सुंदरबनमध्ये चक्रीवादळ इशाऱ्यांवर लक्ष ठेवणे, पावसाळ्यात डोंगरी रस्त्यांची स्थिती तपासणे, आणि सुंदरबनमध्ये केवळ परवानाधारक बोटी व मार्गदर्शकांसोबत जाणे."),
        conf="Editorial"),
    emergency_table(("West Bengal", "पश्चिम बंगाल", "पश्चिम बंगाल")),
    lst("links", [
        it3("imd", "IMD weather and cyclone warnings", "आईएमडी मौसम और चक्रवात चेतावनियाँ", "आयएमडी हवामान व चक्रीवादळ इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Department — verified link", "राज्य आपदा प्रबंधन विभाग — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन विभाग — पडताळलेला दुवा"), "ndma", "Add the official West Bengal disaster management address."),
        (L("Cyclone damage figures (Amphan, Yaas)", "चक्रवात से हानि के आँकड़े (अम्फान, यास)", "चक्रीवादळ हानीचे आकडे (अम्फान, यास)"), "ndma", "Official memoranda / NDMA reports."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "West Bengal has 35 registered Geographical Indications in the GI Registry's list as on 31 December 2025, and shares Dalle Khursani chilli with Sikkim. Darjeeling Tea was India's first registered GI (application numbers 1 and 2, filed in 2003). The list is rich in sweets — Banglar Rasogolla, Nolen Gur Sandesh, Bardhaman Mihidana and Sitabhog, Joynagar Moa, Bishnupur Motichur Laddu and Murshidabad Chhanabora — and in rice, from Gobindabhog and Tulaipanji to Kalonunia and Radhunipagal. Crafts include Baluchari, Shantipur, Dhaniakhali, Tangail, Garad and Korial saris, Nakshi Kantha, Bankura terracotta, Bengal dokra and patachitra, Purulia Chhau masks and Madurkathi mats, along with Malda's mangoes and Sundarban honey.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में पश्चिम बंगाल के 35 पंजीकृत भौगोलिक संकेतक हैं, और डल्ले खुर्सानी मिर्च सिक्किम के साथ साझा है। दार्जिलिंग चाय भारत का पहला पंजीकृत जीआई थी (आवेदन संख्या 1 और 2, 2003 में दायर)। सूची में मिठाइयाँ भरपूर हैं — बंगाल का रसगुल्ला, नोलेन गुड़ संदेश, बर्धमान मिहिदाना और सीताभोग, जयनगर मोआ, बिष्णुपुर मोतीचूर लड्डू और मुर्शिदाबाद छानाबोड़ा — और चावल भी, गोबिंदभोग और तुलाईपांजी से कालोनुनिया और राधुनीपागल तक। शिल्पों में बालूचरी, शांतिपुर, धनियाखाली, टांगाइल, गरद और कोरियाल साड़ियाँ, नक्शी कांथा, बाँकुड़ा टेराकोटा, बंगाल डोकरा और पटचित्र, पुरुलिया छऊ मुखौटे और मादुरकाठी चटाइयाँ हैं, साथ में मालदा के आम और सुंदरबन का शहद।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत पश्चिम बंगालची 35 नोंदणीकृत भौगोलिक मानांकने आहेत, आणि डल्ले खुर्सानी मिरची सिक्कीमसोबत सामायिक आहे. दार्जिलिंग चहा हे भारताचे पहिले नोंदणीकृत जीआय होते (अर्ज क्रमांक 1 व 2, 2003 मध्ये दाखल). यादीत मिठायांची रेलचेल आहे — बंगालचा रसगुल्ला, नोलेन गूळ संदेश, बर्धमान मिहिदाना व सीताभोग, जयनगर मोआ, बिष्णुपूर मोतीचूर लाडू आणि मुर्शिदाबाद छानाबोडा — आणि तांदळाचेही प्रकार, गोबिंदभोग व तुलाईपांजीपासून कालोनुनिया व राधुनीपागलपर्यंत. हस्तकलेत बालुचरी, शांतिपूर, धनियाखाली, टांगाइल, गरद व कोरियाल साड्या, नक्शी कांथा, बांकुडा टेराकोटा, बंगाल डोकरा व पटचित्र, पुरुलिया छाऊ मुखवटे आणि मादुरकाठी चटया आहेत, सोबत मालदाचे आंबे व सुंदरबनचे मध."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "West Bengal combines a great colonial-era city with mountains, mangroves and heritage towns. Kolkata's Victoria Memorial, Howrah Bridge, Dakshineswar and Belur Math, the Indian Museum and its Durga Puja draw large crowds. Darjeeling, Kalimpong and the Singalila ridge offer tea gardens, monasteries and views of Kangchenjunga; the Dooars have wildlife parks; the Sundarbans can be explored by boat; and Bishnupur, Murshidabad and Santiniketan are heritage centres. Digha and Mandarmani are popular beach towns, and Gangasagar on Sagar Island hosts a large pilgrimage fair every January.",
        "पश्चिम बंगाल एक महान औपनिवेशिक-युगीन शहर को पहाड़ों, मैंग्रोव और धरोहर नगरों से जोड़ता है। कोलकाता का विक्टोरिया मेमोरियल, हावड़ा ब्रिज, दक्षिणेश्वर और बेलूर मठ, भारतीय संग्रहालय और इसकी दुर्गा पूजा बड़ी भीड़ खींचते हैं। दार्जिलिंग, कालिम्पोंग और सिंगालीला रिज चाय बागान, मठ और कंचनजंगा के दृश्य देते हैं; डुआर्स में वन्यजीव उद्यान हैं; सुंदरबन नाव से घूमा जा सकता है; और बिष्णुपुर, मुर्शिदाबाद और शांतिनिकेतन धरोहर केंद्र हैं। दीघा और मंदारमणि लोकप्रिय समुद्र तटीय नगर हैं, और सागर द्वीप पर गंगासागर में हर जनवरी बड़ा तीर्थ मेला लगता है।",
        "पश्चिम बंगाल एका महान वसाहतकालीन शहराला पर्वत, खारफुटी व वारसा नगरांशी जोडते. कोलकात्याचे व्हिक्टोरिया मेमोरियल, हावडा पूल, दक्षिणेश्वर व बेलूर मठ, भारतीय संग्रहालय आणि तिथली दुर्गापूजा मोठी गर्दी खेचतात. दार्जिलिंग, कालिम्पोंग व सिंगालीला डोंगररांग चहामळे, मठ व कांचनजंगाचे दर्शन देतात; डुआर्समध्ये वन्यजीव उद्याने आहेत; सुंदरबन बोटीतून पाहता येते; आणि बिष्णुपूर, मुर्शिदाबाद व शांतिनिकेतन ही वारसा केंद्रे आहेत. दिघा व मंदारमणी ही लोकप्रिय समुद्रकिनाऱ्याची गावे आहेत, आणि सागर बेटावरील गंगासागर येथे दर जानेवारीत मोठी तीर्थयात्रा जत्रा भरते."),
        conf="Editorial"),
    lst("places", [
        it3("kolkata", "Kolkata: Victoria Memorial, Howrah Bridge, College Street", "कोलकाता: विक्टोरिया मेमोरियल, हावड़ा ब्रिज, कॉलेज स्ट्रीट", "कोलकाता: व्हिक्टोरिया मेमोरियल, हावडा पूल, कॉलेज स्ट्रीट", m=("City heritage", "नगर धरोहर", "शहरी वारसा")),
        it3("darjeeling", "Darjeeling and the toy train", "दार्जिलिंग और टॉय ट्रेन", "दार्जिलिंग व टॉय ट्रेन", m=("UNESCO railway", "यूनेस्को रेल", "युनेस्को रेल्वे")),
        it3("sundarbans", "Sundarbans", "सुंदरबन", "सुंदरबन", m=("Mangroves, tigers", "मैंग्रोव, बाघ", "खारफुटी, वाघ")),
        it3("santiniketan", "Santiniketan", "शांतिनिकेतन", "शांतिनिकेतन", m=("UNESCO heritage", "यूनेस्को धरोहर", "युनेस्को वारसा")),
        it3("bishnupur", "Bishnupur", "बिष्णुपुर", "बिष्णुपूर", m=("Terracotta temples", "टेराकोटा मंदिर", "टेराकोटा मंदिरे")),
        it3("dooars", "Jaldapara and Gorumara (Dooars)", "जलदापाड़ा और गोरुमारा (डुआर्स)", "जलदापाडा व गोरुमारा (डुआर्स)", m=("Wildlife (Sep–Jun)", "वन्यजीव (सितंबर–जून)", "वन्यजीव (सप्टें.–जून)")),
        it3("murshidabad", "Murshidabad", "मुर्शिदाबाद", "मुर्शिदाबाद", m=("Nawabi heritage", "नवाबी धरोहर", "नवाबी वारसा")),
        it3("gangasagar", "Gangasagar", "गंगासागर", "गंगासागर", m=("Pilgrimage (January)", "तीर्थ (जनवरी)", "तीर्थक्षेत्र (जानेवारी)")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Kolkata: Victoria Memorial, Howrah Bridge at dawn, Kumartuli, Dakshineswar and Belur Math.", "कोलकाता: विक्टोरिया मेमोरियल, भोर में हावड़ा ब्रिज, कुमारटुली, दक्षिणेश्वर और बेलूर मठ।", "कोलकाता: व्हिक्टोरिया मेमोरियल, पहाटे हावडा पूल, कुमारटुली, दक्षिणेश्वर व बेलूर मठ.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Sundarbans by boat from Godkhali, with nights on the islands.", "गोदखाली से नाव द्वारा सुंदरबन, द्वीपों पर रात्रि विश्राम के साथ।", "गोदखालीहून बोटीने सुंदरबन, बेटांवर मुक्कामासह.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Darjeeling and Kalimpong via Siliguri, with the toy train and Tiger Hill sunrise.", "सिलीगुड़ी होकर दार्जिलिंग और कालिम्पोंग, टॉय ट्रेन और टाइगर हिल के सूर्योदय के साथ।", "सिलिगुडीमार्गे दार्जिलिंग व कालिम्पोंग, टॉय ट्रेन व टायगर हिलच्या सूर्योदयासह.")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Kolkata, Santiniketan and Bishnupur, then Murshidabad.", "कोलकाता, शांतिनिकेतन और बिष्णुपुर, फिर मुर्शिदाबाद।", "कोलकाता, शांतिनिकेतन व बिष्णुपूर, नंतर मुर्शिदाबाद.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("wbt", "West Bengal Tourism (official)", "पश्चिम बंगाल पर्यटन (आधिकारिक)", "पश्चिम बंगाल पर्यटन (अधिकृत)", url="https://wbtourism.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
        (L("Earnings from tourism", "पर्यटन से आय", "पर्यटनातून उत्पन्न"), "tourism", "State tourism department."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Alipurduar", "अलीपुरद्वार", "अलिपूरद्वार"), ("Bankura", "बाँकुड़ा", "बांकुडा"), ("Birbhum", "बीरभूम", "बीरभूम"), ("Cooch Behar", "कूचबिहार", "कूचबिहार"),
    ("Dakshin Dinajpur", "दक्षिण दिनाजपुर", "दक्षिण दिनाजपूर"), ("Darjeeling", "दार्जिलिंग", "दार्जिलिंग"), ("Hooghly", "हुगली", "हुगळी"), ("Howrah", "हावड़ा", "हावडा"),
    ("Jalpaiguri", "जलपाईगुड़ी", "जलपाईगुडी"), ("Jhargram", "झाड़ग्राम", "झाडग्राम"), ("Kalimpong", "कालिम्पोंग", "कालिम्पोंग"), ("Kolkata", "कोलकाता", "कोलकाता"),
    ("Malda", "मालदा", "मालदा"), ("Murshidabad", "मुर्शिदाबाद", "मुर्शिदाबाद"), ("Nadia", "नदिया", "नदिया"), ("North 24 Parganas", "उत्तर 24 परगना", "उत्तर 24 परगणा"),
    ("Paschim Bardhaman", "पश्चिम बर्धमान", "पश्चिम बर्धमान"), ("Paschim Medinipur", "पश्चिम मेदिनीपुर", "पश्चिम मेदिनीपूर"), ("Purba Bardhaman", "पूर्व बर्धमान", "पूर्व बर्धमान"), ("Purba Medinipur", "पूर्व मेदिनीपुर", "पूर्व मेदिनीपूर"),
    ("Purulia", "पुरुलिया", "पुरुलिया"), ("South 24 Parganas", "दक्षिण 24 परगना", "दक्षिण 24 परगणा"), ("Uttar Dinajpur", "उत्तर दिनाजपुर", "उत्तर दिनाजपूर"),
]
assert len(DISTRICTS) == 23, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("kolkata", ("Kolkata", "कोलकाता", "कोलकाता"), ("State capital; port, commerce, culture; India's first metro.", "राज्य की राजधानी; बंदरगाह, वाणिज्य, संस्कृति; भारत की पहली मेट्रो।", "राज्याची राजधानी; बंदर, व्यापार, संस्कृती; भारतातील पहिली मेट्रो."), ("Capital", "राजधानी", "राजधानी")),
        city("howrah", ("Howrah", "हावड़ा", "हावडा"), ("Twin city across the Hooghly; railway terminus and engineering works.", "हुगली के पार जुड़वाँ शहर; रेलवे टर्मिनस और इंजीनियरिंग कारख़ाने।", "हुगळीपलीकडील जुळे शहर; रेल्वे टर्मिनस व अभियांत्रिकी कारखाने."), ("Industry", "उद्योग", "उद्योग")),
        city("siliguri", ("Siliguri", "सिलीगुड़ी", "सिलिगुडी"), ("Gateway to the hills, Sikkim and the North-East; tea trade.", "पहाड़ियों, सिक्किम और पूर्वोत्तर का प्रवेश द्वार; चाय व्यापार।", "डोंगर, सिक्कीम व ईशान्येचे प्रवेशद्वार; चहा व्यापार."), ("North Bengal", "उत्तर बंगाल", "उत्तर बंगाल")),
        city("durgapur", ("Durgapur and Asansol", "दुर्गापुर और आसनसोल", "दुर्गापूर व आसनसोल"), ("Steel, power and the Raniganj coalfield.", "इस्पात, बिजली और रानीगंज कोयला क्षेत्र।", "पोलाद, वीज व राणीगंज कोळसा क्षेत्र."), ("Industry", "उद्योग", "उद्योग")),
        city("haldia", ("Haldia", "हल्दिया", "हल्दिया"), ("Port and petrochemical hub on the Hooghly estuary.", "हुगली मुहाने पर बंदरगाह और पेट्रोरसायन केंद्र।", "हुगळीच्या मुखावरील बंदर व पेट्रोरसायन केंद्र."), ("Port", "बंदरगाह", "बंदर")),
        city("darjeeling", ("Darjeeling", "दार्जिलिंग", "दार्जिलिंग"), ("Hill town of tea gardens and the toy train.", "चाय बागानों और टॉय ट्रेन का पहाड़ी नगर।", "चहामळे व टॉय ट्रेनचे डोंगरी शहर."), ("Hills", "पहाड़", "डोंगर")),
        city("bardhaman", ("Bardhaman", "बर्धमान", "बर्धमान"), ("Rice bowl of Bengal; mihidana and sitabhog.", "बंगाल का धान का कटोरा; मिहिदाना और सीताभोग।", "बंगालचे भाताचे कोठार; मिहिदाना व सीताभोग."), ("Agriculture", "कृषि", "शेती")),
        city("malda", ("Malda", "मालदा", "मालदा"), ("Mangoes, silk; ruins of Gaur and Pandua.", "आम, रेशम; गौड़ और पांडुआ के खंडहर।", "आंबे, रेशीम; गौड व पांडुआचे अवशेष."), ("Heritage", "धरोहर", "वारसा")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 23 districts (alphabetical)", "23 ज़िले (वर्णानुक्रम)", "23 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Official district list (State notification)", "आधिकारिक ज़िला सूची (राज्य अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य अधिसूचना)"), "india-gov", "Link the State's list of districts."),
        (L("District populations (Census 2011)", "ज़िलावार जनसंख्या (जनगणना 2011)", "जिल्हानिहाय लोकसंख्या (जनगणना 2011)"), "census", "District Census Handbooks."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Football is a passion in West Bengal. The Kolkata derby between Mohun Bagan and East Bengal is one of the oldest club rivalries in Asia, and Mohun Bagan's barefoot win over the East Yorkshire Regiment in the 1911 IFA Shield is celebrated as a milestone of the national movement. The Salt Lake (Vivekananda Yuva Bharati Krirangan) stadium is one of India's largest. Cricket is followed just as keenly at Eden Gardens, one of the world's great Test venues, and Sourav Ganguly is the State's best-known cricketer. Chuni Goswami, P. K. Banerjee and Leander Paes are among other sporting figures from the State.",
        "पश्चिम बंगाल में फ़ुटबॉल जुनून है। मोहन बागान और ईस्ट बंगाल के बीच कोलकाता डर्बी एशिया की सबसे पुरानी क्लब प्रतिद्वंद्विताओं में है, और 1911 के आईएफ़ए शील्ड में ईस्ट यॉर्कशायर रेजिमेंट पर मोहन बागान की नंगे पैर जीत को राष्ट्रीय आंदोलन के एक पड़ाव के रूप में याद किया जाता है। साल्ट लेक (विवेकानंद युवा भारती क्रीड़ांगन) स्टेडियम भारत के सबसे बड़े स्टेडियमों में है। क्रिकेट भी उतने ही उत्साह से ईडन गार्डन्स में देखा जाता है, जो दुनिया के महान टेस्ट मैदानों में है, और सौरव गांगुली राज्य के सबसे प्रसिद्ध क्रिकेटर हैं। चुन्नी गोस्वामी, पी. के. बनर्जी और लिएंडर पेस राज्य के अन्य खेल व्यक्तित्वों में हैं।",
        "पश्चिम बंगालमध्ये फुटबॉल हे वेड आहे. मोहन बागान व ईस्ट बंगाल यांच्यातील कोलकाता डर्बी ही आशियातील सर्वांत जुन्या क्लब प्रतिस्पर्धांपैकी आहे, आणि 1911 च्या आयएफए शील्डमध्ये ईस्ट यॉर्कशायर रेजिमेंटवर मोहन बागानने अनवाणी मिळवलेला विजय राष्ट्रीय चळवळीतील एक टप्पा म्हणून साजरा केला जातो. सॉल्ट लेक (विवेकानंद युवा भारती क्रीडांगण) स्टेडियम भारतातील सर्वांत मोठ्या मैदानांपैकी आहे. क्रिकेटही तितक्याच उत्साहाने ईडन गार्डन्सवर पाहिले जाते — जगातील महान कसोटी मैदानांपैकी एक — आणि सौरव गांगुली हे राज्याचे सर्वांत प्रसिद्ध क्रिकेटपटू आहेत. चुनी गोस्वामी, पी. के. बॅनर्जी व लिअँडर पेस हे राज्यातील इतर क्रीडा व्यक्तिमत्त्व आहेत."),
        conf="Editorial"),
    lst("venues", [
        it3("eden", "Eden Gardens, Kolkata", "ईडन गार्डन्स, कोलकाता", "ईडन गार्डन्स, कोलकाता"),
        it3("saltlake", "Vivekananda Yuva Bharati Krirangan (Salt Lake Stadium)", "विवेकानंद युवा भारती क्रीड़ांगन (साल्ट लेक स्टेडियम)", "विवेकानंद युवा भारती क्रीडांगण (सॉल्ट लेक स्टेडियम)"),
        it3("mohunbagan", "Mohun Bagan and East Bengal grounds, Maidan", "मोहन बागान और ईस्ट बंगाल मैदान, मैदान क्षेत्र", "मोहन बागान व ईस्ट बंगाल मैदाने, मैदान परिसर"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from West Bengal (official list)", "पश्चिम बंगाल के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "पश्चिम बंगालचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "State youth services and sports department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("rammohan", ("Raja Ram Mohan Roy", "राजा राममोहन राय", "राजा राममोहन रॉय"), ("Reformer who founded the Brahmo Sabha and campaigned against sati.", "सुधारक, जिन्होंने ब्रह्म सभा की स्थापना की और सती प्रथा के विरुद्ध अभियान चलाया।", "ब्राह्मो सभेचे संस्थापक व सतीप्रथेविरुद्ध लढलेले सुधारक."), ("Reform", "सुधार", "सुधारणा")),
        person("vidyasagar", ("Ishwar Chandra Vidyasagar", "ईश्वरचंद्र विद्यासागर", "ईश्वरचंद्र विद्यासागर"), ("Educator and reformer; championed widow remarriage and girls' schooling.", "शिक्षाविद और सुधारक; विधवा पुनर्विवाह और बालिका शिक्षा के समर्थक।", "शिक्षणतज्ज्ञ व सुधारक; विधवा पुनर्विवाह व मुलींच्या शिक्षणाचे पुरस्कर्ते."), ("Reform", "सुधार", "सुधारणा")),
        person("bankim", ("Bankim Chandra Chattopadhyay", "बंकिमचंद्र चट्टोपाध्याय", "बंकिमचंद्र चट्टोपाध्याय"), ("Novelist; wrote 'Vande Mataram' in Anandamath.", "उपन्यासकार; आनंदमठ में 'वंदे मातरम्' लिखा।", "कादंबरीकार; आनंदमठमध्ये 'वंदे मातरम्' लिहिले."), ("Literature", "साहित्य", "साहित्य")),
        person("vivekananda", ("Swami Vivekananda", "स्वामी विवेकानंद", "स्वामी विवेकानंद"), ("Disciple of Ramakrishna; founded the Ramakrishna Mission; Chicago address of 1893.", "रामकृष्ण के शिष्य; रामकृष्ण मिशन के संस्थापक; 1893 का शिकागो भाषण।", "रामकृष्णांचे शिष्य; रामकृष्ण मिशनचे संस्थापक; 1893 चे शिकागो भाषण."), ("Spiritual", "आध्यात्मिक", "आध्यात्मिक")),
        person("tagore", ("Rabindranath Tagore", "रवींद्रनाथ टैगोर", "रवींद्रनाथ टागोर"), ("Poet, composer and educator; Nobel Prize in Literature 1913; founded Visva-Bharati.", "कवि, संगीतकार और शिक्षाविद; 1913 में साहित्य का नोबेल; विश्व-भारती के संस्थापक।", "कवी, संगीतकार व शिक्षणतज्ज्ञ; 1913 चे साहित्याचे नोबेल; विश्वभारतीचे संस्थापक."), ("Literature", "साहित्य", "साहित्य")),
        person("jcbose", ("Jagadish Chandra Bose", "जगदीश चंद्र बोस", "जगदीशचंद्र बोस"), ("Physicist and plant physiologist; pioneer of radio and microwave research.", "भौतिक विज्ञानी और पादप शरीर क्रिया वैज्ञानिक; रेडियो और माइक्रोवेव शोध के अग्रणी।", "भौतिकशास्त्रज्ञ व वनस्पती शरीरशास्त्रज्ञ; रेडिओ व मायक्रोवेव संशोधनाचे प्रणेते."), ("Science", "विज्ञान", "विज्ञान")),
        person("netaji", ("Netaji Subhas Chandra Bose", "नेताजी सुभाष चंद्र बोस", "नेताजी सुभाषचंद्र बोस"), ("Led the Indian National Army in the freedom struggle.", "स्वतंत्रता संग्राम में आज़ाद हिंद फ़ौज का नेतृत्व किया।", "स्वातंत्र्यलढ्यात आझाद हिंद सेनेचे नेतृत्व केले."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("snbose", ("Satyendra Nath Bose", "सत्येंद्र नाथ बोस", "सत्येंद्रनाथ बोस"), ("Physicist of Bose–Einstein statistics; the boson is named after him.", "बोस–आइंस्टाइन सांख्यिकी के भौतिक विज्ञानी; बोसॉन उनके नाम पर है।", "बोस–आइन्स्टाइन सांख्यिकीचे भौतिकशास्त्रज्ञ; बोसॉन त्यांच्या नावाने आहे."), ("Science", "विज्ञान", "विज्ञान")),
        person("nazrul", ("Kazi Nazrul Islam", "काज़ी नज़रुल इस्लाम", "काझी नजरुल इस्लाम"), ("'Rebel poet' and composer, born at Churulia; national poet of Bangladesh.", "'विद्रोही कवि' और संगीतकार, चुरुलिया में जन्मे; बांग्लादेश के राष्ट्रकवि।", "'विद्रोही कवी' व संगीतकार, चुरुलिया येथे जन्म; बांगलादेशचे राष्ट्रकवी."), ("Literature", "साहित्य", "साहित्य")),
        person("ray", ("Satyajit Ray", "सत्यजीत राय", "सत्यजित राय"), ("Film-maker of the Apu Trilogy; honorary Academy Award 1992; Bharat Ratna.", "अपु त्रयी के फ़िल्मकार; 1992 में मानद ऑस्कर; भारत रत्न।", "अपू त्रयीचे चित्रपटकार; 1992 चा मानद ऑस्कर; भारतरत्न."), ("Cinema", "सिनेमा", "चित्रपट")),
        person("teresa", ("Mother Teresa", "मदर टेरेसा", "मदर तेरेसा"), ("Founded the Missionaries of Charity in Kolkata; Nobel Peace Prize 1979.", "कोलकाता में मिशनरीज़ ऑफ़ चैरिटी की स्थापना की; 1979 का नोबेल शांति पुरस्कार।", "कोलकात्यात मिशनरीज ऑफ चॅरिटीची स्थापना; 1979 चे नोबेल शांतता पारितोषिक."), ("Service", "सेवा", "सेवा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Bengalis from West Bengal have settled in large numbers in other Indian cities — Delhi, Mumbai, Bengaluru and Pune — and abroad in the United Kingdom, the United States and Canada, many as doctors, academics and engineers, keeping up Durga Puja and Tagore celebrations wherever they live. Workers from the State, especially from Murshidabad, Malda and the Sundarbans, migrate in large numbers to other States and to the Gulf. Ties of language, family and culture run deep with Bangladesh across the border, and Darjeeling's Nepali-speaking community has close links with Nepal and Sikkim.",
        "पश्चिम बंगाल के बांग्लाभाषी बड़ी संख्या में भारत के अन्य शहरों — दिल्ली, मुंबई, बेंगलूरु और पुणे — और विदेश में ब्रिटेन, अमेरिका और कनाडा में बसे हैं, जिनमें बहुत से डॉक्टर, शिक्षाविद और इंजीनियर हैं, और वे जहाँ भी रहते हैं दुर्गा पूजा और टैगोर उत्सव मनाते हैं। राज्य के श्रमिक, ख़ासकर मुर्शिदाबाद, मालदा और सुंदरबन से, बड़ी संख्या में दूसरे राज्यों और खाड़ी देशों में जाते हैं। सीमा पार बांग्लादेश के साथ भाषा, परिवार और संस्कृति के गहरे संबंध हैं, और दार्जिलिंग के नेपाली-भाषी समुदाय के नेपाल और सिक्किम से निकट संबंध हैं।",
        "पश्चिम बंगालमधील बांगलाभाषक मोठ्या संख्येने भारतातील इतर शहरांत — दिल्ली, मुंबई, बंगळूरु व पुणे — आणि परदेशात ब्रिटन, अमेरिका व कॅनडात स्थायिक झाले आहेत, त्यांतील अनेक डॉक्टर, प्राध्यापक व अभियंते आहेत, आणि ते जिथे राहतात तिथे दुर्गापूजा व टागोर उत्सव साजरे करतात. राज्यातील कामगार, विशेषतः मुर्शिदाबाद, मालदा व सुंदरबनमधून, मोठ्या संख्येने इतर राज्यांत व आखाती देशांत जातात. सीमेपलीकडील बांगलादेशशी भाषा, कुटुंब व संस्कृतीचे खोल नाते आहे, आणि दार्जिलिंगमधील नेपाळीभाषक समुदायाचे नेपाळ व सिक्कीमशी निकटचे संबंध आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants and internal migrants", "प्रवासियों और आंतरिक प्रवासियों की संख्या", "परदेशी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; MEA."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of West Bengal portal", "पश्चिम बंगाल सरकार पोर्टल", "पश्चिम बंगाल शासन संकेतस्थळ", url="https://wb.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "West Bengal Tourism", "पश्चिम बंगाल पर्यटन", "पश्चिम बंगाल पर्यटन", url="https://wbtourism.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Kolkata and Howrah", "कोलकाता और हावड़ा", "कोलकाता व हावडा"), "033"], [L("Siliguri", "सिलीगुड़ी", "सिलिगुडी"), "0353"], [L("Darjeeling", "दार्जिलिंग", "दार्जिलिंग"), "0354"],
           [L("Durgapur", "दुर्गापुर", "दुर्गापूर"), "0343"], [L("Asansol", "आसनसोल", "आसनसोल"), "0341"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("State e-services portal — verified link", "राज्य ई-सेवा पोर्टल — सत्यापित लिंक", "राज्य ई-सेवा संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "Certificates and services portal of the State."),
        (L("Verified local business directory", "सत्यापित स्थानीय व्यवसाय निर्देशिका", "पडताळलेली स्थानिक उद्योग सूची"), "india-gov", "Udyam Registration and co-operative registrars."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("tea", ("Darjeeling Tea was India's first registered Geographical Indication — application numbers 1 and 2.", "दार्जिलिंग चाय भारत का पहला पंजीकृत भौगोलिक संकेतक थी — आवेदन संख्या 1 और 2।", "दार्जिलिंग चहा हे भारताचे पहिले नोंदणीकृत भौगोलिक मानांकन होते — अर्ज क्रमांक 1 व 2."), GI_PDF, "gi-registry"),
        triv("sundarban", ("The Sundarban Wetland, at 4,23,000 ha, is the largest Ramsar site in India.", "4,23,000 हेक्टेयर वाली सुंदरबन आर्द्रभूमि भारत का सबसे बड़ा रामसर स्थल है।", "4,23,000 हेक्टरचे सुंदरबन पाणथळ हे भारतातील सर्वांत मोठे रामसर स्थळ आहे."), RAMSAR, "indian-wetlands"),
        triv("metro", ("Kolkata opened India's first metro line in 1984 and its first under-river metro tunnel in 2024.", "कोलकाता ने 1984 में भारत की पहली मेट्रो लाइन और 2024 में पहली नदी-तल मेट्रो सुरंग खोली।", "कोलकात्याने 1984 मध्ये भारतातील पहिली मेट्रो मार्गिका आणि 2024 मध्ये पहिला नदीतळ मेट्रो बोगदा सुरू केला.")),
        triv("durgapuja", ("Durga Puja in Kolkata was added to UNESCO's Intangible Cultural Heritage list in 2021.", "कोलकाता की दुर्गा पूजा 2021 में यूनेस्को की अमूर्त सांस्कृतिक धरोहर सूची में शामिल हुई।", "कोलकात्याची दुर्गापूजा 2021 मध्ये युनेस्कोच्या अमूर्त सांस्कृतिक वारसा यादीत समाविष्ट झाली.")),
        triv("anthems", ("Rabindranath Tagore wrote the national anthems of both India and Bangladesh.", "रवींद्रनाथ टैगोर ने भारत और बांग्लादेश दोनों के राष्ट्रगान लिखे।", "रवींद्रनाथ टागोरांनी भारत व बांगलादेश दोघांची राष्ट्रगीते लिहिली.")),
        triv("hc", ("The Calcutta High Court, established in 1862, is the oldest High Court in India.", "1862 में स्थापित कलकत्ता उच्च न्यायालय भारत का सबसे पुराना उच्च न्यायालय है।", "1862 मध्ये स्थापन झालेले कलकत्ता उच्च न्यायालय हे भारतातील सर्वांत जुने उच्च न्यायालय आहे.")),
        triv("ls", ("The State elects 42 members to the Lok Sabha.", "राज्य से लोकसभा के 42 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 42 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("wb mod3 ok")
