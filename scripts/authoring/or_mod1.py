"""Odisha modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-OR"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
od = read("regions/IN-OR.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Odisha lies on the Bay of Bengal in eastern India, between West Bengal and Andhra Pradesh, with Jharkhand to the north and Chhattisgarh to the west. A fertile coastal plain formed by the deltas of the Mahanadi, Brahmani and Baitarani rises inland to the forested hills of the Eastern Ghats and the plateaus of the north and west. It had 4.20 crore people at the 2011 Census. Bhubaneswar, the 'temple city', is the capital; Cuttack, the old capital, Rourkela, Berhampur, Sambalpur and Puri are other major cities.\n\nOdisha became a separate province on 1 April 1936 — the first province formed on the basis of language — and the State's English name changed from Orissa to Odisha in 2011. Odia, one of India's classical languages, is the official language.",
        "ओडिशा पूर्वी भारत में बंगाल की खाड़ी के तट पर, पश्चिम बंगाल और आंध्र प्रदेश के बीच स्थित है; इसके उत्तर में झारखंड और पश्चिम में छत्तीसगढ़ है। महानदी, ब्राह्मणी और वैतरणी के डेल्टाओं से बना उपजाऊ तटीय मैदान भीतर की ओर पूर्वी घाट की वनाच्छादित पहाड़ियों और उत्तर व पश्चिम के पठारों तक उठता है। 2011 की जनगणना में इसकी जनसंख्या 4.20 करोड़ थी। 'मंदिरों का नगर' भुवनेश्वर राजधानी है; पुरानी राजधानी कटक, राउरकेला, बरहमपुर, संबलपुर और पुरी अन्य प्रमुख शहर हैं।\n\nओडिशा 1 अप्रैल 1936 को एक अलग प्रांत बना — भाषा के आधार पर बना पहला प्रांत — और 2011 में राज्य का अंग्रेज़ी नाम Orissa से बदलकर Odisha हुआ। भारत की शास्त्रीय भाषाओं में से एक ओड़िया राजभाषा है।",
        "ओडिशा पूर्व भारतात बंगालच्या उपसागराच्या किनाऱ्यावर, पश्चिम बंगाल व आंध्र प्रदेशदरम्यान आहे; त्याच्या उत्तरेला झारखंड व पश्चिमेला छत्तीसगड आहे. महानदी, ब्राह्मणी व वैतरणीच्या त्रिभुज प्रदेशांनी बनलेले सुपीक किनारी मैदान आत पूर्व घाटाच्या वनाच्छादित डोंगररांगा व उत्तर-पश्चिमेच्या पठारांपर्यंत चढत जाते. 2011 च्या जनगणनेनुसार त्याची लोकसंख्या 4.20 कोटी होती. 'मंदिरांचे शहर' भुवनेश्वर ही राजधानी आहे; जुनी राजधानी कटक, राउरकेला, बेरहमपूर, संबलपूर व पुरी ही इतर प्रमुख शहरे आहेत.\n\nओडिशा 1 एप्रिल 1936 रोजी स्वतंत्र प्रांत बनला — भाषेच्या आधारावर बनलेला पहिला प्रांत — आणि 2011 मध्ये राज्याचे इंग्रजी नाव Orissa वरून Odisha झाले. भारताच्या अभिजात भाषांपैकी एक असलेली ओडिया ही राजभाषा आहे."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Odisha is the land of Lord Jagannath. The Rath Yatra at Puri, when the deities ride huge wooden chariots through the town, is one of India's best-known festivals, and the 13th-century Sun Temple at Konark is a UNESCO World Heritage Site. Bhubaneswar's hundreds of temples trace the Kalinga style of architecture over a thousand years. Odissi is one of India's classical dances, and Pattachitra painting, silver filigree from Cuttack and Sambalpuri ikat textiles are prized. Chilika, India's largest coastal lagoon, Bhitarkanika's mangroves and the olive ridley turtle nesting beaches of Gahirmatha and Rushikulya are natural treasures. Odisha is also India's mineral heartland, with large reserves of iron ore, bauxite and chromite, and about a fifth of its people are from Scheduled Tribes.",
        "ओडिशा भगवान जगन्नाथ की भूमि है। पुरी की रथयात्रा, जब देवता विशाल लकड़ी के रथों पर नगर में निकलते हैं, भारत के सबसे प्रसिद्ध उत्सवों में से है, और 13वीं सदी का कोणार्क सूर्य मंदिर यूनेस्को विश्व धरोहर स्थल है। भुवनेश्वर के सैकड़ों मंदिर एक हज़ार वर्षों में कलिंग स्थापत्य शैली के विकास को दिखाते हैं। ओडिसी भारत के शास्त्रीय नृत्यों में से एक है, और पट्टचित्र चित्रकला, कटक की चाँदी की तारकशी और संबलपुरी इकत वस्त्र बहुमूल्य हैं। भारत का सबसे बड़ा तटीय लैगून चिलिका, भितरकनिका के मैंग्रोव और गहिरमाथा व ऋषिकुल्या के ऑलिव रिडले कछुओं के प्रजनन तट प्राकृतिक धरोहर हैं। ओडिशा भारत का खनिज केंद्र भी है, जहाँ लौह अयस्क, बॉक्साइट और क्रोमाइट के बड़े भंडार हैं, और इसकी लगभग पाँचवाँ हिस्सा आबादी अनुसूचित जनजातियों की है।",
        "ओडिशा ही भगवान जगन्नाथाची भूमी आहे. पुरीची रथयात्रा, जेव्हा देवता प्रचंड लाकडी रथांतून नगरात निघतात, हा भारतातील सर्वांत प्रसिद्ध उत्सवांपैकी एक आहे, आणि तेराव्या शतकातील कोणार्कचे सूर्य मंदिर युनेस्को जागतिक वारसा स्थळ आहे. भुवनेश्वरची शेकडो मंदिरे हजार वर्षांतील कलिंग स्थापत्यशैलीचा विकास दाखवतात. ओडिसी हे भारताच्या शास्त्रीय नृत्यांपैकी एक आहे, आणि पट्टचित्र चित्रकला, कटकचे चांदीचे जाळीकाम व संबलपुरी इकत वस्त्रे मौल्यवान मानली जातात. भारतातील सर्वांत मोठे किनारी खारकच्छ चिलिका, भितरकनिकाची खारफुटी आणि गहिरमाथा व ऋषिकुल्याचे ऑलिव्ह रिडले कासवांचे अंडी घालण्याचे किनारे हा निसर्गाचा ठेवा आहे. ओडिशा हे भारताचे खनिज केंद्रही आहे, जिथे लोहखनिज, बॉक्साइट व क्रोमाइटचे मोठे साठे आहेत, आणि त्याच्या लोकसंख्येचा सुमारे पाचवा भाग अनुसूचित जमातींचा आहे."),
        title=L("What makes Odisha unique?", "ओडिशा को ख़ास क्या बनाता है?", "ओडिशाचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed", "गठन", "निर्मिती"), L("1 April 1936 (Utkal Divas)", "1 अप्रैल 1936 (उत्कल दिवस)", "1 एप्रिल 1936 (उत्कल दिवस)")],
           [L("Districts / revenue divisions", "ज़िले / राजस्व मंडल", "जिल्हे / महसूल विभाग"), "30 / 3"],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Odia", "ओड़िया", "ओडिया")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Orissa High Court, Cuttack (1948)", "उड़ीसा उच्च न्यायालय, कटक (1948)", "ओरिसा उच्च न्यायालय, कटक (1948)")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "OD"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be linked to the State's notifications in review.", "संपादकीय; समीक्षा में राज्य की अधिसूचनाओं से जोड़ा जाएगा।", "संपादकीय; तपासणीत राज्याच्या अधिसूचनांशी जोडले जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Odisha has four broad regions. The coastal plain, built by the deltas of the Mahanadi, Brahmani, Baitarani, Subarnarekha and Rushikulya, is flat, fertile and densely settled. Inland, the Eastern Ghats run north-east to south-west through Kandhamal, Koraput and Rayagada, with the State's highest peaks; the northern plateau of Mayurbhanj, Kendujhar and Sundargarh holds the Similipal hills and most of the mineral belt; and the western uplands around Sambalpur, Bolangir and Kalahandi are drained by the middle Mahanadi and its tributaries. Chilika, a lagoon joined to the sea near Puri, is India's largest coastal lagoon.",
        "ओडिशा के चार व्यापक क्षेत्र हैं। महानदी, ब्राह्मणी, वैतरणी, सुवर्णरेखा और ऋषिकुल्या के डेल्टाओं से बना तटीय मैदान समतल, उपजाऊ और घनी आबादी वाला है। भीतर, पूर्वी घाट कंधमाल, कोरापुट और रायगड़ा से होकर उत्तर-पूर्व से दक्षिण-पश्चिम की ओर फैले हैं, जहाँ राज्य की सबसे ऊँची चोटियाँ हैं; मयूरभंज, केंदुझर और सुंदरगढ़ के उत्तरी पठार में सिमलीपाल की पहाड़ियाँ और अधिकांश खनिज पट्टी है; और संबलपुर, बलांगीर और कालाहांडी के आसपास के पश्चिमी उच्च क्षेत्र मध्य महानदी और उसकी सहायक नदियों से सिंचित हैं। पुरी के पास समुद्र से जुड़ा लैगून चिलिका भारत का सबसे बड़ा तटीय लैगून है।",
        "ओडिशाचे चार मुख्य प्रदेश आहेत. महानदी, ब्राह्मणी, वैतरणी, सुवर्णरेखा व ऋषिकुल्याच्या त्रिभुज प्रदेशांनी बनलेले किनारी मैदान सपाट, सुपीक व दाट वस्तीचे आहे. आत, पूर्व घाट कंधमाल, कोरापुट व रायगडामधून ईशान्येकडून नैर्ऋत्येकडे पसरला आहे, जिथे राज्यातील सर्वांत उंच शिखरे आहेत; मयूरभंज, केंदुझर व सुंदरगडच्या उत्तरेकडील पठारात सिमलीपालचे डोंगर व बहुतांश खनिज पट्टा आहे; आणि संबलपूर, बलांगीर व कालाहांडीभोवतीचा पश्चिमेकडील उंचवटा मध्य महानदी व तिच्या उपनद्यांनी भिजतो. पुरीजवळ समुद्राला जोडलेले चिलिका हे भारतातील सर्वांत मोठे किनारी खारकच्छ आहे."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), od["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("wb", "West Bengal (north-east)", "पश्चिम बंगाल (उत्तर-पूर्व)", "पश्चिम बंगाल (ईशान्य)"), it3("jh", "Jharkhand (north)", "झारखंड (उत्तर)", "झारखंड (उत्तर)"),
        it3("ct", "Chhattisgarh (west)", "छत्तीसगढ़ (पश्चिम)", "छत्तीसगड (पश्चिम)"), it3("ap", "Andhra Pradesh (south)", "आंध्र प्रदेश (दक्षिण)", "आंध्र प्रदेश (दक्षिण)"),
        it3("bay", "Bay of Bengal (east)", "बंगाल की खाड़ी (पूर्व)", "बंगालचा उपसागर (पूर्व)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("mahanadi", "Mahanadi", "महानदी", "महानदी", d=("Rises in Chhattisgarh; dammed at Hirakud and forms a large delta around Cuttack.", "छत्तीसगढ़ से निकलती है; हीराकुद पर बाँधी गई है और कटक के आसपास बड़ा डेल्टा बनाती है।", "छत्तीसगडमध्ये उगम; हिराकुड येथे धरण, आणि कटकभोवती मोठा त्रिभुज प्रदेश.")),
        it3("brahmani", "Brahmani", "ब्राह्मणी", "ब्राह्मणी", d=("Formed at Vedavyas near Rourkela; flows past Talcher to the sea.", "राउरकेला के पास वेदव्यास में बनती है; तालचेर से होकर समुद्र तक बहती है।", "राउरकेलाजवळ वेदव्यास येथे निर्माण होते; तालचेरमार्गे समुद्रापर्यंत वाहते.")),
        it3("baitarani", "Baitarani", "वैतरणी", "वैतरणी", d=("Rises in Kendujhar; joins the Brahmani delta near Bhitarkanika.", "केंदुझर से निकलती है; भितरकनिका के पास ब्राह्मणी डेल्टा से मिलती है।", "केंदुझरमध्ये उगम; भितरकनिकाजवळ ब्राह्मणीच्या त्रिभुज प्रदेशाला मिळते.")),
        it3("subarnarekha", "Subarnarekha", "सुवर्णरेखा", "सुवर्णरेखा", d=("Crosses the far north near Balasore.", "बालेश्वर के पास सुदूर उत्तर से गुज़रती है।", "बालेश्वरजवळ अगदी उत्तरेकडून वाहते.")),
        it3("rushikulya", "Rushikulya", "ऋषिकुल्या", "ऋषिकुल्या", d=("Southern river of Ganjam; turtle nesting at its mouth.", "गंजाम की दक्षिणी नदी; मुहाने पर कछुओं का प्रजनन।", "गंजामची दक्षिणेकडील नदी; मुखाशी कासवांचे अंडी घालणे.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point — official elevation", "सर्वोच्च बिंदु — आधिकारिक ऊँचाई", "सर्वोच्च शिखर — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Length of coastline", "तटरेखा की लंबाई", "किनारपट्टीची लांबी"), "survey-of-india", "Survey of India / MoEFCC coastal statistics."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Odisha has a tropical climate. Summers (March–June) are hot and humid on the coast, and the western districts around Titlagarh and Sambalpur are among the hottest places in India in April and May. The south-west monsoon (June–September) brings most of the rain, and depressions from the Bay of Bengal can cause floods in the deltas. Cyclones are most likely in October–November and, less often, in April–May. Winters (December–February) are mild on the coast and cool in the hills of Koraput and Kandhamal.",
        "ओडिशा की जलवायु उष्णकटिबंधीय है। गर्मियाँ (मार्च–जून) तट पर गर्म और उमस भरी होती हैं, और अप्रैल–मई में टिटिलागढ़ और संबलपुर के आसपास के पश्चिमी ज़िले भारत के सबसे गर्म स्थानों में होते हैं। दक्षिण-पश्चिम मानसून (जून–सितंबर) अधिकांश वर्षा लाता है, और बंगाल की खाड़ी के अवदाब डेल्टाओं में बाढ़ ला सकते हैं। चक्रवात अक्टूबर–नवंबर में और कभी-कभी अप्रैल–मई में सबसे अधिक आते हैं। सर्दियाँ (दिसंबर–फ़रवरी) तट पर हल्की और कोरापुट व कंधमाल की पहाड़ियों में ठंडी होती हैं।",
        "ओडिशाचे हवामान उष्णकटिबंधीय आहे. उन्हाळा (मार्च–जून) किनाऱ्यावर उष्ण व दमट असतो, आणि एप्रिल–मेमध्ये टिटिलागड व संबलपूरभोवतीचे पश्चिमेकडील जिल्हे भारतातील सर्वांत उष्ण ठिकाणांपैकी असतात. नैर्ऋत्य मान्सून (जून–सप्टेंबर) बहुतेक पाऊस आणतो, आणि बंगालच्या उपसागरातील कमी दाबाचे पट्टे त्रिभुज प्रदेशात पूर आणू शकतात. चक्रीवादळे ऑक्टोबर–नोव्हेंबरमध्ये व कधीकधी एप्रिल–मेमध्ये सर्वाधिक येतात. हिवाळा (डिसेंबर–फेब्रुवारी) किनाऱ्यावर सौम्य व कोरापुट आणि कंधमालच्या डोंगरांत थंड असतो."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Bhubaneswar", "भुवनेश्वर", "भुवनेश्वर"), "lat": 20.2961, "lon": 85.8245},
        {"name": L("Puri", "पुरी", "पुरी"), "lat": 19.8135, "lon": 85.8312},
        {"name": L("Sambalpur", "संबलपुर", "संबलपूर"), "lat": 21.4669, "lon": 83.9812},
        {"name": L("Koraput", "कोरापुट", "कोरापुट"), "lat": 18.8135, "lon": 82.7123},
    ]},
    lst("best", [
        it3("winter", "October to March", "अक्टूबर से मार्च", "ऑक्टोबर ते मार्च", d=("Best for temples, beaches and Chilika's migratory birds; Konark Dance Festival in December.", "मंदिरों, समुद्र तटों और चिलिका के प्रवासी पक्षियों के लिए सबसे अच्छा; दिसंबर में कोणार्क नृत्य महोत्सव।", "मंदिरे, किनारे व चिलिकाच्या स्थलांतरित पक्ष्यांसाठी उत्तम; डिसेंबरमध्ये कोणार्क नृत्य महोत्सव.")),
        it3("summer", "April to June", "अप्रैल से जून", "एप्रिल ते जून", d=("Hot; Rath Yatra usually falls in June–July.", "गर्मी; रथयात्रा प्रायः जून–जुलाई में।", "उष्ण; रथयात्रा सहसा जून–जुलैमध्ये.")),
        it3("monsoon", "July to September", "जुलाई से सितंबर", "जुलै ते सप्टेंबर", d=("Green hills and waterfalls in Koraput; floods possible in the deltas.", "कोरापुट में हरी पहाड़ियाँ और झरने; डेल्टाओं में बाढ़ संभव।", "कोरापुटमध्ये हिरवे डोंगर व धबधबे; त्रिभुज प्रदेशात पुराची शक्यता.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (Odisha sub-division)", "सामान्य वार्षिक वर्षा (ओडिशा उप-मंडल)", "सरासरी वार्षिक पाऊस (ओडिशा उपविभाग)"), "imd", "IMD rainfall statistics."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Odisha's rhythm is set by Jagannath and the seasons. In Puri, life moves around the temple and its kitchen, whose mahaprasad is shared by all, and the whole State follows the Rath Yatra. Coastal villages grow paddy, coconut and betel, and fishing boats work the shore; the western hills have their own Sambalpuri songs, dances and the harvest festival Nuakhai, and tribal villages in Koraput and Mayurbhanj keep weekly haats and their own languages. A bowl of pakhala — fermented rice in water — is the classic summer meal, chhena poda and rasagola are favourite sweets, and evenings in Bhubaneswar and Cuttack fill with Durga Puja pandals and Bali Jatra fairs in autumn.",
        "ओडिशा की लय जगन्नाथ और मौसमों से तय होती है। पुरी में जीवन मंदिर और उसकी रसोई के इर्द-गिर्द चलता है, जिसका महाप्रसाद सब बाँटते हैं, और पूरा राज्य रथयात्रा का अनुसरण करता है। तटीय गाँवों में धान, नारियल और पान उगता है, और मछली पकड़ने वाली नावें तट पर काम करती हैं; पश्चिमी पहाड़ियों के अपने संबलपुरी गीत, नृत्य और फ़सल का त्योहार नुआखाई है, और कोरापुट व मयूरभंज के आदिवासी गाँव साप्ताहिक हाट और अपनी भाषाएँ सँजोए हुए हैं। पखाल — पानी में भिगोया ख़मीरी भात — गर्मियों का पारंपरिक भोजन है, छेना पोड़ा और रसगोला पसंदीदा मिठाइयाँ हैं, और शरद में भुवनेश्वर व कटक की शामें दुर्गा पूजा पंडालों और बाली जात्रा मेलों से भर जाती हैं।",
        "ओडिशाची लय जगन्नाथ व ऋतूंनी ठरते. पुरीत जीवन मंदिर व त्याच्या स्वयंपाकघराभोवती फिरते, ज्याचा महाप्रसाद सर्वजण वाटून घेतात, आणि संपूर्ण राज्य रथयात्रेकडे लक्ष ठेवते. किनारी गावांत भात, नारळ व विड्याची पाने पिकतात, आणि मासेमारीच्या होड्या किनाऱ्यावर काम करतात; पश्चिमेकडील डोंगरांची स्वतःची संबलपुरी गाणी, नृत्ये व नुआखाई हा सुगीचा सण आहे, आणि कोरापुट व मयूरभंजमधील आदिवासी गावे आठवडी बाजार व आपल्या भाषा जपतात. पखाल — पाण्यात भिजवलेला आंबवलेला भात — हे उन्हाळ्याचे पारंपरिक जेवण आहे, छेना पोडा व रसगोला आवडत्या मिठाया आहेत, आणि शरदात भुवनेश्वर व कटकच्या संध्याकाळी दुर्गापूजा मंडप व बाली जात्रा जत्रांनी भरून जातात."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Odisha had 4.20 crore people at the 2011 Census, with about 270 people per km². The sex ratio was 979 women per 1,000 men — well above the national average — but the child sex ratio fell from 953 in 2001 to 941 in 2011. Literacy was 72.9%, close to the national 73.0%. Scheduled Tribes made up 22.8% of the population, among the highest shares outside the north-east, and Scheduled Castes 17.1%.\n\nOdia is the official language and the mother tongue of most people. Santali, written in the Ol Chiki script developed in Mayurbhanj, is a scheduled language, and many other tribal languages — Ho, Mundari, Kui, Sora and others — are spoken, as are Sambalpuri (Kosli) in the west, Telugu in the south and Bengali in the north.",
        "2011 की जनगणना में ओडिशा की जनसंख्या 4.20 करोड़ थी, और प्रति वर्ग किमी लगभग 270 लोग। लिंगानुपात प्रति 1,000 पुरुषों पर 979 महिलाएँ था — राष्ट्रीय औसत से काफ़ी ऊपर — लेकिन शिशु लिंगानुपात 2001 के 953 से घटकर 2011 में 941 रह गया। साक्षरता 72.9% थी, जो राष्ट्रीय 73.0% के क़रीब है। अनुसूचित जनजातियाँ जनसंख्या का 22.8% थीं, जो पूर्वोत्तर के बाहर सबसे ऊँचे हिस्सों में है, और अनुसूचित जातियाँ 17.1%।\n\nओड़िया राजभाषा और अधिकांश लोगों की मातृभाषा है। मयूरभंज में विकसित ओल चिकी लिपि में लिखी जाने वाली संताली अनुसूचित भाषा है, और हो, मुंडारी, कुई, सोरा जैसी कई अन्य जनजातीय भाषाएँ बोली जाती हैं, साथ ही पश्चिम में संबलपुरी (कोसली), दक्षिण में तेलुगु और उत्तर में बांग्ला भी।",
        "2011 च्या जनगणनेनुसार ओडिशाची लोकसंख्या 4.20 कोटी होती, आणि प्रति चौ.किमी सुमारे 270 लोक. दर 1,000 पुरुषांमागे 979 स्त्रिया होत्या — राष्ट्रीय सरासरीपेक्षा बरेच अधिक — पण बाल लिंग गुणोत्तर 2001 मधील 953 वरून 2011 मध्ये 941 वर घसरले. साक्षरता 72.9% होती, राष्ट्रीय 73.0% च्या जवळ. अनुसूचित जमाती लोकसंख्येच्या 22.8% होत्या — ईशान्येबाहेरील सर्वाधिक वाट्यांपैकी — आणि अनुसूचित जाती 17.1%.\n\nओडिया ही राजभाषा व बहुतेक लोकांची मातृभाषा आहे. मयूरभंजमध्ये विकसित झालेल्या ओल चिकी लिपीत लिहिली जाणारी संताली ही अनुसूचित भाषा आहे, आणि हो, मुंडारी, कुई, सोरा यांसारख्या अनेक आदिवासी भाषा बोलल्या जातात, तसेच पश्चिमेत संबलपुरी (कोसली), दक्षिणेत तेलुगू व उत्तरेत बंगाली."),
        sources=["census", "es-india", "dl-planning"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), od["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), od["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(972, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), od["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(953, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), od["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), od["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(17.1, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 71.88 lakh people (listed as Orissa)."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(22.8, "%", "2011", "census", "dl-planning", SCST, note="Same table: 95.91 lakh people."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("or", "Odia", "ओड़िया", "ओडिया", m=("Official language; classical language", "राजभाषा; शास्त्रीय भाषा", "राजभाषा; अभिजात भाषा")),
        it3("sat", "Santali", "संताली", "संताली", m=("Scheduled language", "अनुसूचित भाषा", "अनुसूचित भाषा")),
        it3("kos", "Sambalpuri (Kosli)", "संबलपुरी (कोसली)", "संबलपुरी (कोसली)"), it3("ho", "Ho", "हो", "हो"),
        it3("kui", "Kui", "कुई", "कुई"), it3("mun", "Mundari", "मुंडारी", "मुंडारी"), it3("te", "Telugu", "तेलुगु", "तेलुगू"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Final Population Totals for Odisha."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Number of Scheduled Tribes and PVTGs", "अनुसूचित जनजातियों और पीवीटीजी की संख्या", "अनुसूचित जमाती व पीव्हीटीजींची संख्या"), "tribal-affairs", "Ministry of Tribal Affairs list for Odisha."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Ancient Kalinga was a powerful maritime kingdom. Ashoka's conquest of Kalinga around 261 BCE, and the bloodshed that led him to embrace non-violence, is recorded in his rock edicts at Dhauli and Jaugada. In the 1st century BCE, Kharavela of the Mahameghavahana dynasty ruled from near present-day Bhubaneswar; his Hathigumpha inscription at Udayagiri is a key historical record. The Somavamshis, and then the Eastern Gangas, built the great temples: the Lingaraja at Bhubaneswar, the Jagannath temple at Puri under Anantavarman Chodaganga in the 12th century, and the Sun Temple at Konark under Narasimhadeva I in the 13th. The Gajapati kings ruled until the 16th century, after which Odisha passed to the Afghans, the Mughals and the Marathas.\n\nThe British took Odisha in 1803, and the Paika rebellion of 1817 was an early armed uprising against them. The famine of 1866 killed a very large part of the coastal population. Leaders such as Madhusudan Das and Gopabandhu Das led the movement for an Odia-speaking province, achieved on 1 April 1936. The princely States joined in 1948–49, and Cuttack was replaced by Bhubaneswar as capital. The super cyclone of 1999 changed how the State prepares for disasters.",
        "प्राचीन कलिंग एक शक्तिशाली समुद्री राज्य था। लगभग 261 ई.पू. में अशोक की कलिंग विजय, और उस रक्तपात के बाद उनका अहिंसा अपनाना, धौली और जौगड़ के उनके शिलालेखों में दर्ज है। ई.पू. पहली सदी में महामेघवाहन वंश के खारवेल ने वर्तमान भुवनेश्वर के पास से शासन किया; उदयगिरि में उनका हाथीगुंफा अभिलेख एक प्रमुख ऐतिहासिक स्रोत है। सोमवंशियों और फिर पूर्वी गंगों ने महान मंदिर बनाए: भुवनेश्वर का लिंगराज, 12वीं सदी में अनंतवर्मन चोडगंग के समय पुरी का जगन्नाथ मंदिर, और 13वीं सदी में नरसिंहदेव प्रथम के समय कोणार्क का सूर्य मंदिर। गजपति राजाओं ने 16वीं सदी तक शासन किया, जिसके बाद ओडिशा अफ़ग़ानों, मुग़लों और मराठों के अधीन गया।\n\nअंग्रेज़ों ने 1803 में ओडिशा लिया, और 1817 का पाइक विद्रोह उनके विरुद्ध एक प्रारंभिक सशस्त्र विद्रोह था। 1866 के अकाल में तटीय आबादी का बहुत बड़ा हिस्सा मारा गया। मधुसूदन दास और गोपबंधु दास जैसे नेताओं ने ओड़िया-भाषी प्रांत के आंदोलन का नेतृत्व किया, जो 1 अप्रैल 1936 को साकार हुआ। रियासतें 1948–49 में शामिल हुईं, और कटक के स्थान पर भुवनेश्वर राजधानी बना। 1999 के महाचक्रवात ने राज्य की आपदा तैयारी का तरीका बदल दिया।",
        "प्राचीन कलिंग हे एक बलाढ्य सागरी राज्य होते. सुमारे इ.स.पू. 261 मध्ये अशोकाने केलेला कलिंगविजय, आणि त्या रक्तपातानंतर त्याने स्वीकारलेली अहिंसा, धौली व जौगडच्या त्याच्या शिलालेखांत नोंदलेली आहे. इ.स.पू. पहिल्या शतकात महामेघवाहन घराण्याच्या खारवेलाने सध्याच्या भुवनेश्वरजवळून राज्य केले; उदयगिरीतील त्याचा हाथीगुंफा शिलालेख हा महत्त्वाचा ऐतिहासिक पुरावा आहे. सोमवंशी व नंतर पूर्व गंगांनी महान मंदिरे बांधली: भुवनेश्वरचे लिंगराज, बाराव्या शतकात अनंतवर्मन चोडगंगाच्या काळात पुरीचे जगन्नाथ मंदिर, आणि तेराव्या शतकात नरसिंहदेव पहिल्याच्या काळात कोणार्कचे सूर्य मंदिर. गजपती राजांनी सोळाव्या शतकापर्यंत राज्य केले, त्यानंतर ओडिशा अफगाण, मुघल व मराठ्यांच्या अधिपत्याखाली गेला.\n\nइंग्रजांनी 1803 मध्ये ओडिशा घेतला, आणि 1817 चा पाईक उठाव हा त्यांच्याविरुद्धचा एक सुरुवातीचा सशस्त्र उठाव होता. 1866 च्या दुष्काळात किनारी लोकसंख्येचा फार मोठा भाग मृत्युमुखी पडला. मधुसूदन दास व गोपबंधू दास यांसारख्या नेत्यांनी ओडियाभाषक प्रांताच्या चळवळीचे नेतृत्व केले, जी 1 एप्रिल 1936 रोजी साकार झाली. संस्थाने 1948–49 मध्ये सामील झाली, आणि कटकऐवजी भुवनेश्वर राजधानी झाली. 1999 च्या महाचक्रीवादळाने राज्याची आपत्ती-तयारीची पद्धत बदलली."),
        conf="Editorial"),
    timeline([
        ev("kalinga", -261, L("c. 261 BCE", "लगभग 261 ई.पू.", "सुमारे इ.स.पू. 261"), L("Ashoka's Kalinga war", "अशोक का कलिंग युद्ध", "अशोकाचे कलिंग युद्ध")),
        ev("kharavela", -50, L("1st century BCE", "ई.पू. पहली सदी", "इ.स.पू. पहिले शतक"), L("Kharavela's Hathigumpha inscription", "खारवेल का हाथीगुंफा अभिलेख", "खारवेलाचा हाथीगुंफा शिलालेख")),
        ev("puri", 1135, L("12th century", "12वीं सदी", "बारावे शतक"), L("Jagannath temple at Puri built under the Eastern Gangas", "पूर्वी गंगों के समय पुरी का जगन्नाथ मंदिर बना", "पूर्व गंगांच्या काळात पुरीचे जगन्नाथ मंदिर बांधले")),
        ev("konark", 1250, L("13th century", "13वीं सदी", "तेरावे शतक"), L("Sun Temple at Konark", "कोणार्क का सूर्य मंदिर", "कोणार्कचे सूर्य मंदिर")),
        ev("british", 1803, L("1803", "1803", "1803"), L("British conquest of Odisha", "ओडिशा पर अंग्रेज़ों का अधिकार", "इंग्रजांनी ओडिशा जिंकला")),
        ev("paika", 1817, L("1817", "1817", "1817"), L("Paika rebellion", "पाइक विद्रोह", "पाईक उठाव")),
        ev("famine", 1866, L("1866", "1866", "1866"), L("Great Odisha famine (Na Anka)", "ओडिशा का महा-अकाल (न अंक)", "ओडिशाचा महादुष्काळ (न अंक)")),
        ev("province", 1936, L("1 April 1936", "1 अप्रैल 1936", "1 एप्रिल 1936"), L("Odisha province formed (Utkal Divas)", "ओडिशा प्रांत बना (उत्कल दिवस)", "ओडिशा प्रांताची निर्मिती (उत्कल दिवस)")),
        ev("cyclone", 1999, L("October 1999", "अक्टूबर 1999", "ऑक्टोबर 1999"), L("Super cyclone strikes the coast", "महाचक्रवात ने तट पर प्रहार किया", "महाचक्रीवादळ किनाऱ्यावर धडकले")),
        ev("name", 2011, L("2011", "2011", "2011"), L("English name changed from Orissa to Odisha", "अंग्रेज़ी नाम Orissa से Odisha हुआ", "इंग्रजी नाव Orissa वरून Odisha झाले")),
        ev("cm2024", 2024, L("12 June 2024", "12 जून 2024", "12 जून 2024"), L("Mohan Charan Majhi sworn in as Chief Minister", "मोहन चरण माझी ने मुख्यमंत्री पद की शपथ ली", "मोहन चरण माझी यांचा मुख्यमंत्रिपदाचा शपथविधी")),
    ]),
    lst("heritage", [
        it3("konark", "Sun Temple, Konark", "सूर्य मंदिर, कोणार्क", "सूर्य मंदिर, कोणार्क", m=("UNESCO 1984", "यूनेस्को 1984", "युनेस्को 1984"), url=UNESCO, src="unesco-whc"),
        it3("jagannath", "Jagannath Temple, Puri", "जगन्नाथ मंदिर, पुरी", "जगन्नाथ मंदिर, पुरी", m=("12th century; Char Dham", "12वीं सदी; चार धाम", "बारावे शतक; चार धाम")),
        it3("lingaraja", "Lingaraja Temple, Bhubaneswar", "लिंगराज मंदिर, भुवनेश्वर", "लिंगराज मंदिर, भुवनेश्वर", m=("11th century", "11वीं सदी", "अकरावे शतक")),
        it3("udayagiri", "Udayagiri and Khandagiri caves", "उदयगिरि और खंडगिरि गुफाएँ", "उदयगिरी व खंडगिरी लेणी", m=("Jain caves; Hathigumpha", "जैन गुफाएँ; हाथीगुंफा", "जैन लेणी; हाथीगुंफा")),
        it3("dhauli", "Dhauli rock edicts", "धौली शिलालेख", "धौली शिलालेख", m=("Ashokan", "अशोककालीन", "अशोककालीन")),
        it3("ratnagiri", "Ratnagiri, Lalitgiri and Udayagiri (Jajpur)", "रत्नगिरि, ललितगिरि और उदयगिरि (जाजपुर)", "रत्नगिरी, ललितगिरी व उदयगिरी (जाजपूर)", m=("Buddhist sites", "बौद्ध स्थल", "बौद्ध स्थळे")),
        it3("barabati", "Barabati Fort, Cuttack", "बाराबाटी क़िला, कटक", "बाराबाटी किल्ला, कटक", m=("Ruins on the Mahanadi", "महानदी पर अवशेष", "महानदीकाठचे अवशेष")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("or mod1 ok")
