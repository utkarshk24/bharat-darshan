import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from bd import *

R = "IN-MH"
SDB = "https://mahasdb.maharashtra.gov.in/maagCmpIndia.do"
SW = "https://socialwelfare.maharashtra.gov.in/en/general-and-scheduled-caste-population-census-2011/"
TRTI = "https://trti.maharashtra.gov.in/statewiseTotalTribal"
PIB_CSR = "https://www.pib.gov.in/newsite/printrelease.aspx?relid=103437&reg=48&lang=2"
UNESCO = "https://whc.unesco.org/en/statesparties/in"
MHT = "https://maharashtratourism.gov.in/districts/dharashiv/"
LANG = "https://cdnbbsr.s3waas.gov.in/s3f55cadb97eaff2ba1980e001b0bd9842/uploads/2025/02/20250202779031828.pdf"
PIB_CL = "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2061660&reg=48&lang=2"
SDB_DIST = "https://mahasdb.maharashtra.gov.in/SDB_Reports/Population_Census/PDF/Districtwise%20population,%20Decadal%20Growth%20rate,%20Sex%20Ratio%20and%20Density%20according%20to%20Census%202011.pdf"

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Maharashtra is India's third-largest State by area and second-largest by population. It stretches from the Arabian Sea coast across the Sahyadri (Western Ghats) to the Deccan plateau and the forests of Vidarbha in the east. Mumbai, the capital, is the country's main financial centre; Nagpur hosts the legislature's winter session.\n\nThe State was formed on 1 May 1960, when the bilingual Bombay State was divided on linguistic lines into Maharashtra and Gujarat after the Samyukta Maharashtra movement. Marathi is the official language.",
        "महाराष्ट्र क्षेत्रफल की दृष्टि से भारत का तीसरा और जनसंख्या की दृष्टि से दूसरा सबसे बड़ा राज्य है। यह अरब सागर के तट से सह्याद्रि (पश्चिमी घाट) होते हुए दक्कन के पठार और पूर्व में विदर्भ के जंगलों तक फैला है। राजधानी मुंबई देश का प्रमुख वित्तीय केंद्र है, जबकि नागपुर में विधानमंडल का शीतकालीन सत्र होता है।\n\nराज्य का गठन 1 मई 1960 को हुआ, जब संयुक्त महाराष्ट्र आंदोलन के बाद द्विभाषी बंबई राज्य को भाषाई आधार पर महाराष्ट्र और गुजरात में बाँटा गया। मराठी राज्य की राजभाषा है।",
        "महाराष्ट्र हे क्षेत्रफळाने भारतातील तिसरे आणि लोकसंख्येने दुसरे मोठे राज्य आहे. अरबी समुद्राच्या किनाऱ्यापासून सह्याद्री (पश्चिम घाट) ओलांडून दख्खनच्या पठारापर्यंत आणि पूर्वेकडील विदर्भातील जंगलांपर्यंत ते पसरलेले आहे. राजधानी मुंबई ही देशाची प्रमुख आर्थिक राजधानी आहे, तर नागपूर येथे विधिमंडळाचे हिवाळी अधिवेशन भरते.\n\nसंयुक्त महाराष्ट्र चळवळीनंतर द्विभाषिक मुंबई राज्याचे भाषिक आधारावर महाराष्ट्र आणि गुजरात असे विभाजन होऊन 1 मे 1960 रोजी राज्याची स्थापना झाली. मराठी ही राज्याची राजभाषा आहे."),
        conf="Editorial"),
    prose("intro-unique", L(
        "Few States combine so many layers in one place: rock-cut cave art at Ajanta and Ellora, a chain of hill and sea forts built by the Marathas, a 19th-century Victorian Gothic and Art Deco city, and India's largest state economy. The annual Wari pilgrimage to Pandharpur and the ten-day Ganeshotsav show how public festivals remain central to everyday life.",
        "बहुत कम राज्यों में इतनी परतें एक साथ मिलती हैं: अजंता और एलोरा की शैलकृत गुफ़ा-कला, मराठों द्वारा बनवाए गए पहाड़ी और समुद्री क़िलों की शृंखला, 19वीं सदी की विक्टोरियन गॉथिक और आर्ट डेको शैली वाला महानगर, और देश की सबसे बड़ी राज्य अर्थव्यवस्था। पंढरपुर की वार्षिक वारी और दस दिन का गणेशोत्सव दिखाते हैं कि सार्वजनिक उत्सव आज भी रोज़मर्रा के जीवन के केंद्र में हैं।",
        "इतके थर एकाच ठिकाणी असलेली राज्ये थोडीच आहेत: अजिंठा-वेरूळची शिल्पलेणी, मराठ्यांनी बांधलेली डोंगरी व सागरी किल्ल्यांची साखळी, एकोणिसाव्या शतकातील व्हिक्टोरियन गॉथिक आणि आर्ट डेको शैलीचे महानगर, आणि देशातील सर्वांत मोठी राज्य अर्थव्यवस्था. पंढरपूरची वार्षिक वारी आणि दहा दिवसांचा गणेशोत्सव यांतून सार्वजनिक उत्सव आजही दैनंदिन जीवनाच्या केंद्रस्थानी असल्याचे दिसते."),
        title=L("What makes Maharashtra unique?", "महाराष्ट्र को ख़ास क्या बनाता है?", "महाराष्ट्राचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formation", "गठन", "स्थापना"), L("1 May 1960 (Maharashtra Day)", "1 मई 1960 (महाराष्ट्र दिवस)", "1 मे 1960 (महाराष्ट्र दिन)")],
           [L("Districts", "ज़िले", "जिल्हे"), "36"],
           [L("Revenue divisions", "राजस्व संभाग", "महसूल विभाग"), L("6 — Konkan, Pune, Nashik, Chhatrapati Sambhajinagar, Amravati, Nagpur", "6 — कोंकण, पुणे, नासिक, छत्रपति संभाजीनगर, अमरावती, नागपुर", "6 — कोकण, पुणे, नाशिक, छत्रपती संभाजीनगर, अमरावती, नागपूर")],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Marathi (classical language status, October 2024)", "मराठी (अक्टूबर 2024 में शास्त्रीय भाषा का दर्जा)", "मराठी (ऑक्टोबर 2024 मध्ये अभिजात भाषेचा दर्जा)")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-MH / MH"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"],
           [L("State song", "राज्य गीत", "राज्यगीत"), L("“Jai Jai Maharashtra Maza” (title only)", "“जय जय महाराष्ट्र माझा” (केवल शीर्षक)", "“जय जय महाराष्ट्र माझा” (केवळ शीर्षक)")]],
          "mh-tourism", MHT, conf="Editorial",
          note=L("District count from the Department of Tourism's district list. Other rows are editorial and will each be linked to a notification in review.",
                 "ज़िलों की संख्या पर्यटन विभाग की ज़िला सूची से। बाकी पंक्तियाँ संपादकीय हैं; समीक्षा में हर एक को अधिसूचना से जोड़ा जाएगा।",
                 "जिल्ह्यांची संख्या पर्यटन विभागाच्या जिल्हा यादीतून. इतर ओळी संपादकीय असून तपासणीदरम्यान प्रत्येकीला अधिसूचनेचा दुवा जोडला जाईल.")),
    lst("renamed", [
        item("chs", L("Chhatrapati Sambhajinagar", "छत्रपति संभाजीनगर", "छत्रपती संभाजीनगर"), meta=L("formerly Aurangabad", "पूर्व नाम औरंगाबाद", "पूर्वीचे नाव औरंगाबाद")),
        item("dharashiv", L("Dharashiv", "धाराशिव", "धाराशिव"), meta=L("formerly Osmanabad", "पूर्व नाम उस्मानाबाद", "पूर्वीचे नाव उस्मानाबाद"), url="https://rdd.maharashtra.gov.in/en/document/notification-regarding-changing-the-name-of-osmanabad-to-dharashiv/"),
        item("ahilyanagar", L("Ahilyanagar", "अहिल्यानगर", "अहिल्यानगर"), meta=L("formerly Ahmednagar", "पूर्व नाम अहमदनगर", "पूर्वीचे नाव अहमदनगर"), url="https://rdd.maharashtra.gov.in/en/document/notification-regarding-changing-the-name-of-ahmednagar-to-ahilyanagar/"),
    ], layout="chips", title=L("Renamed districts", "नए नाम वाले ज़िले", "नामांतर झालेले जिल्हे"),
       src="mh-gov", url="https://rdd.maharashtra.gov.in/en/document/notification-regarding-changing-the-name-of-ahmednagar-to-ahilyanagar/", conf="Official", access=TODAY),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Maharashtra has three broad belts. The narrow Konkan coast runs about 720 km along the Arabian Sea, cut by creeks and estuaries. Behind it the Sahyadri rise steeply; Kalsubai (about 1,646 m) is the highest point. East of the crest lies the Deccan plateau, built of layered basalt from ancient lava flows, which slopes gently towards the Wainganga basin in Vidarbha.\n\nMost large rivers rise in the Sahyadri and flow east to the Bay of Bengal: the Godavari from Trimbakeshwar near Nashik, and the Krishna from Mahabaleshwar, with the Bhima as a major tributary. The Tapi and Narmada system drains the north-west towards the Arabian Sea. Lonar Lake in Buldhana district fills a crater formed by a meteorite impact.",
        "महाराष्ट्र तीन मुख्य पट्टियों में बँटा है। संकरी कोंकण पट्टी अरब सागर के साथ लगभग 720 किमी तक फैली है, जिसे खाड़ियाँ और मुहाने काटते हैं। उसके पीछे सह्याद्रि की खड़ी ढलानें उठती हैं; कळसूबाई (लगभग 1,646 मीटर) सबसे ऊँची चोटी है। चोटी के पूर्व में दक्कन का पठार है, जो प्राचीन लावा प्रवाहों से बनी बेसाल्ट की परतों से बना है और विदर्भ में वैनगंगा घाटी की ओर धीरे-धीरे ढलता है।\n\nअधिकांश बड़ी नदियाँ सह्याद्रि से निकलकर पूर्व की ओर बंगाल की खाड़ी में जाती हैं: गोदावरी नासिक के पास त्र्यंबकेश्वर से और कृष्णा महाबलेश्वर से, जिसकी प्रमुख सहायक नदी भीमा है। उत्तर-पश्चिम का जल तापी के रास्ते अरब सागर में जाता है। बुलढाणा ज़िले की लोणार झील उल्कापिंड के टकराने से बने गड्ढे में भरी है।",
        "महाराष्ट्राचे तीन प्रमुख पट्टे आहेत. चिंचोळी कोकणपट्टी अरबी समुद्राच्या काठाने सुमारे 720 किमी पसरली असून खाड्या आणि नदीमुखांनी ती छेदलेली आहे. तिच्या मागे सह्याद्री उभा चढतो; कळसूबाई (सुमारे 1,646 मीटर) हे सर्वोच्च शिखर आहे. माथ्याच्या पूर्वेला प्राचीन लाव्हारसाच्या थरांनी बनलेले बेसॉल्टचे दख्खन पठार असून ते विदर्भातील वैनगंगेच्या खोऱ्याकडे हळूहळू उतरत जाते.\n\nबहुतेक मोठ्या नद्या सह्याद्रीत उगम पावून पूर्वेकडे बंगालच्या उपसागराकडे वाहतात: गोदावरी नाशिकजवळ त्र्यंबकेश्वर येथून आणि कृष्णा महाबळेश्वर येथून; भीमा ही कृष्णेची प्रमुख उपनदी आहे. वायव्य भागाचे पाणी तापीमार्गे अरबी समुद्राला मिळते. बुलढाणा जिल्ह्यातील लोणार सरोवर उल्कापाताने तयार झालेल्या विवरात साचले आहे."),
        conf="Editorial"),
    facts("f", [
        fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), read("regions/IN-MH.json")["metrics"]["area"], "number",
             national=read("india.json")["metrics"]["area"]),
    ]),
    lst("neighbours", [
        item("gj", L("Gujarat", "गुजरात", "गुजरात")), item("dh", L("Dadra & Nagar Haveli and Daman & Diu", "दादरा और नगर हवेली और दमन और दीव", "दादरा आणि नगर हवेली आणि दमण आणि दीव")),
        item("mp", L("Madhya Pradesh", "मध्य प्रदेश", "मध्य प्रदेश")), item("ct", L("Chhattisgarh", "छत्तीसगढ़", "छत्तीसगड")),
        item("tg", L("Telangana", "तेलंगाना", "तेलंगणा")), item("ka", L("Karnataka", "कर्नाटक", "कर्नाटक")),
        item("ga", L("Goa", "गोवा", "गोवा")), item("sea", L("Arabian Sea (west)", "अरब सागर (पश्चिम)", "अरबी समुद्र (पश्चिम)")),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        item("godavari", L("Godavari", "गोदावरी", "गोदावरी"), detail=L("Rises at Trimbakeshwar (Nashik district); flows east across Marathwada.", "त्र्यंबकेश्वर (नासिक ज़िला) से उद्गम; मराठवाड़ा से होकर पूर्व की ओर।", "त्र्यंबकेश्वर (नाशिक जिल्हा) येथे उगम; मराठवाड्यातून पूर्वेकडे वाहते.")),
        item("krishna", L("Krishna", "कृष्णा", "कृष्णा"), detail=L("Rises near Mahabaleshwar; flows south-east into Karnataka.", "महाबलेश्वर के पास से उद्गम; दक्षिण-पूर्व में कर्नाटक की ओर।", "महाबळेश्वरजवळ उगम; आग्नेयेकडे कर्नाटकात जाते.")),
        item("bhima", L("Bhima", "भीमा", "भीमा"), detail=L("Krishna tributary; Pandharpur stands on its banks.", "कृष्णा की सहायक नदी; पंढरपुर इसी के तट पर है।", "कृष्णेची उपनदी; पंढरपूर हिच्या काठी आहे.")),
        item("tapi", L("Tapi", "तापी", "तापी"), detail=L("Flows west through Khandesh to the Arabian Sea.", "खानदेश से होकर पश्चिम में अरब सागर तक।", "खानदेशातून पश्चिमेकडे अरबी समुद्राकडे वाहते.")),
        item("wainganga", L("Wainganga", "वैनगंगा", "वैनगंगा"), detail=L("Main river of eastern Vidarbha, part of the Godavari basin.", "पूर्वी विदर्भ की मुख्य नदी, गोदावरी घाटी का भाग।", "पूर्व विदर्भातील प्रमुख नदी, गोदावरी खोऱ्याचा भाग.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Latitude and longitude extent", "अक्षांश-देशांतर विस्तार", "अक्षांश-रेखांश विस्तार"), "survey-of-india", "Take from Survey of India or the State gazetteer."),
        (L("Coastline length (official)", "तटरेखा की लंबाई (आधिकारिक)", "किनारपट्टीची लांबी (अधिकृत)"), "survey-of-india", "Editorial text uses about 720 km; confirm against an official figure."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
        (L("Soils and mineral output", "मिट्टी और खनिज उत्पादन", "माती व खनिज उत्पादन"), "mh-sdb", "Indian Bureau of Mines / State Economic Survey."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Maharashtra has a tropical monsoon climate with three clear seasons: a hot summer from March to May, the south-west monsoon from June to September, and a mild, dry winter from November to February.\n\nRainfall varies sharply across short distances. The Konkan coast and the Sahyadri crest receive very heavy monsoon rain, while the plateau just east of the ghats lies in a rain shadow, which is why parts of Marathwada and western Maharashtra are drought-prone. Vidarbha has the hottest summers, with peak temperatures that often cross 45 °C.",
        "महाराष्ट्र की जलवायु उष्णकटिबंधीय मानसूनी है, जिसमें तीन स्पष्ट ऋतुएँ हैं: मार्च से मई तक गर्मी, जून से सितंबर तक दक्षिण-पश्चिम मानसून, और नवंबर से फ़रवरी तक हल्की, सूखी सर्दी।\n\nकम दूरी में ही वर्षा में बड़ा अंतर दिखता है। कोंकण तट और सह्याद्रि की चोटियों पर मानसून में बहुत भारी वर्षा होती है, जबकि घाट के ठीक पूर्व का पठार वृष्टि-छाया में आता है; इसी कारण मराठवाड़ा और पश्चिमी महाराष्ट्र के कुछ हिस्से सूखाग्रस्त रहते हैं। विदर्भ में सबसे तेज़ गर्मी पड़ती है, जहाँ तापमान अक्सर 45 °C से ऊपर चला जाता है।",
        "महाराष्ट्राचे हवामान उष्णकटिबंधीय मोसमी आहे आणि त्यात तीन स्पष्ट ऋतू आहेत: मार्च ते मे उन्हाळा, जून ते सप्टेंबर नैर्ऋत्य मोसमी पाऊस, आणि नोव्हेंबर ते फेब्रुवारी सौम्य, कोरडा हिवाळा.\n\nकमी अंतरातच पावसात मोठा फरक दिसतो. कोकणकिनारा आणि सह्याद्रीच्या माथ्यावर पावसाळ्यात अतिवृष्टी होते, तर घाटाच्या लगेच पूर्वेकडील पठार पर्जन्यछायेत येते; म्हणूनच मराठवाडा आणि पश्चिम महाराष्ट्राचा काही भाग दुष्काळप्रवण आहे. विदर्भात सर्वांत तीव्र उन्हाळा असतो आणि तापमान अनेकदा 45 °C च्या पुढे जाते."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Mumbai", "मुंबई", "मुंबई"), "lat": 19.076, "lon": 72.8777},
        {"name": L("Pune", "पुणे", "पुणे"), "lat": 18.5204, "lon": 73.8567},
        {"name": L("Nagpur", "नागपुर", "नागपूर"), "lat": 21.1458, "lon": 79.0882},
        {"name": L("Chhatrapati Sambhajinagar", "छत्रपति संभाजीनगर", "छत्रपती संभाजीनगर"), "lat": 19.8762, "lon": 75.3433},
    ]},
    lst("best", [
        item("winter", L("October to February", "अक्टूबर से फ़रवरी", "ऑक्टोबर ते फेब्रुवारी"), detail=L("Best for most travel: forts, caves, cities and wildlife.", "अधिकांश यात्राओं के लिए सबसे अच्छा: क़िले, गुफ़ाएँ, शहर और वन्यजीव।", "बहुतेक प्रवासासाठी उत्तम: किल्ले, लेणी, शहरे आणि वन्यजीव.")),
        item("monsoon", L("July to September", "जुलाई से सितंबर", "जुलै ते सप्टेंबर"), detail=L("Waterfalls and green ghats; landslide and flood risk on ghat roads.", "झरने और हरे-भरे घाट; घाट सड़कों पर भूस्खलन और बाढ़ का ख़तरा।", "धबधबे आणि हिरवेगार घाट; घाटरस्त्यांवर दरडी व पुराचा धोका.")),
        item("summer", L("March to May", "मार्च से मई", "मार्च ते मे"), detail=L("Hot inland; tiger sightings peak in Vidarbha reserves.", "भीतरी इलाक़ों में तेज़ गर्मी; विदर्भ के अभयारण्यों में बाघ दिखने की संभावना सबसे अधिक।", "अंतर्गत भागात कडक उन्हाळा; विदर्भातील व्याघ्र प्रकल्पांत वाघ दिसण्याची शक्यता सर्वाधिक.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Monthly temperature and rainfall normals", "मासिक तापमान और वर्षा सामान्य", "मासिक तापमान व पर्जन्य सरासरी"), "imd", "IMD climatological normals for Mumbai, Pune, Nagpur, Chh. Sambhajinagar."),
        (L("Köppen climate zones (sourced)", "कोपेन जलवायु क्षेत्र (स्रोत सहित)", "कोपेन हवामान विभाग (स्रोतासह)"), "imd", "Cite IMD or a peer-reviewed Köppen map."),
        (L("Climate-change vulnerability", "जलवायु परिवर्तन संवेदनशीलता", "हवामान बदल असुरक्षितता"), "ndma", "Maharashtra State Action Plan on Climate Change; DST vulnerability index."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Mornings in Maharashtra often begin with a local train horn or a temple bell, and the smell of poha and cutting chai from a roadside stall. Mumbai moves at a run: crowded suburban platforms, Bollywood billboards, sea breeze along Marine Drive. Pune is younger and greener, a mix of old wadas, college crowds and IT parks. Inland, the pace slows. Sugarcane carts creak along village roads, weekly markets fill with onions and chillies, and evening aartis drift from riverside ghats. In the monsoon the ghats turn startling green and every hill fort seems to hold a waterfall. Through the year, festivals pull everyone outdoors — dhol-tasha troupes during Ganeshotsav, kandils at Diwali, and the long, singing procession of warkaris walking to Pandharpur.",
        "महाराष्ट्र की सुबह अक्सर लोकल ट्रेन के हॉर्न या मंदिर की घंटी से शुरू होती है, साथ में सड़क किनारे ठेले से पोहे और कटिंग चाय की ख़ुशबू। मुंबई दौड़ती है: भीड़ भरे उपनगरीय प्लेटफ़ॉर्म, फ़िल्मों के होर्डिंग और मरीन ड्राइव की समुद्री हवा। पुणे युवा और हरा-भरा है, जहाँ पुराने वाड़े, कॉलेजों की रौनक और आईटी पार्क साथ-साथ हैं। भीतरी इलाक़ों में रफ़्तार धीमी हो जाती है। गाँव की सड़कों पर गन्ने से लदी बैलगाड़ियाँ चरमराती हैं, साप्ताहिक बाज़ार प्याज़ और मिर्च से भर जाते हैं, और नदी घाटों से शाम की आरती गूँजती है। मानसून में घाट गहरे हरे हो जाते हैं और हर पहाड़ी क़िले पर कोई झरना दिखता है। साल भर त्योहार सबको बाहर ले आते हैं — गणेशोत्सव में ढोल-ताशा, दिवाली में आकाशकंदील, और पंढरपुर की ओर गाते-चलते वारकरियों की लंबी पंक्ति।",
        "महाराष्ट्रातली सकाळ अनेकदा लोकलच्या भोंग्याने किंवा देवळातल्या घंटेने सुरू होते, सोबत रस्त्याकडेच्या टपरीवरच्या पोह्यांचा आणि कटिंग चहाचा दरवळ. मुंबई धावत असते: गर्दीचे उपनगरी फलाट, चित्रपटांचे फलक आणि मरीन ड्राइव्हवरचा खारा वारा. पुणे तरुण आणि हिरवेगार आहे — जुने वाडे, महाविद्यालयांची वर्दळ आणि आयटी पार्क एकत्र नांदतात. आतल्या भागात वेग मंदावतो. गावरस्त्यांवर उसाच्या बैलगाड्या करकरत जातात, आठवडी बाजार कांदे-मिरच्यांनी भरतो, आणि नदीकाठच्या घाटांवरून संध्याकाळची आरती ऐकू येते. पावसाळ्यात घाट गर्द हिरवे होतात आणि प्रत्येक गडावर एखादा धबधबा कोसळताना दिसतो. वर्षभर सण सगळ्यांना रस्त्यावर आणतात — गणेशोत्सवात ढोल-ताशा, दिवाळीत आकाशकंदील, आणि पंढरपूरकडे गात चालणाऱ्या वारकऱ्यांची लांबच लांब दिंडी."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
mh = read("regions/IN-MH.json")["metrics"]; ind = read("india.json")["metrics"]
module(R, "people", [
    prose("p1", L(
        "At the 2011 Census, Maharashtra had 11.24 crore people, the second-largest population of any State after Uttar Pradesh. It is also one of India's most urbanised large States: 45.2% of residents lived in towns and cities, compared with 31.1% nationally, with the Mumbai, Pune and Nagpur regions as the main urban centres.\n\nMarathi is the official language and the mother tongue of most residents. Marathi was granted classical language status by the Union Government in October 2024. Large numbers also speak Hindi, Urdu, Gujarati and tribal languages such as Bhili, Gondi and Korku.",
        "2011 की जनगणना में महाराष्ट्र की जनसंख्या 11.24 करोड़ थी, जो उत्तर प्रदेश के बाद किसी भी राज्य में दूसरी सबसे अधिक है। यह देश के सबसे शहरीकृत बड़े राज्यों में भी है: यहाँ 45.2% लोग कस्बों और शहरों में रहते थे, जबकि राष्ट्रीय औसत 31.1% था; मुंबई, पुणे और नागपुर क्षेत्र प्रमुख शहरी केंद्र हैं।\n\nमराठी राज्य की राजभाषा और अधिकांश निवासियों की मातृभाषा है। अक्टूबर 2024 में केंद्र सरकार ने मराठी को शास्त्रीय भाषा का दर्जा दिया। बड़ी संख्या में लोग हिंदी, उर्दू, गुजराती और भीली, गोंडी, कोरकू जैसी जनजातीय भाषाएँ भी बोलते हैं।",
        "2011 च्या जनगणनेनुसार महाराष्ट्राची लोकसंख्या 11.24 कोटी होती, जी उत्तर प्रदेशानंतर कोणत्याही राज्यात दुसऱ्या क्रमांकाची आहे. हे देशातील सर्वाधिक नागरीकरण झालेल्या मोठ्या राज्यांपैकीही एक आहे: येथे 45.2% लोक शहरांत राहत होते, तर राष्ट्रीय सरासरी 31.1% होती; मुंबई, पुणे आणि नागपूर परिसर ही प्रमुख नागरी केंद्रे आहेत.\n\nमराठी ही राज्याची राजभाषा आणि बहुसंख्य रहिवाशांची मातृभाषा आहे. ऑक्टोबर 2024 मध्ये केंद्र सरकारने मराठीला अभिजात भाषेचा दर्जा दिला. मोठ्या संख्येने लोक हिंदी, उर्दू, गुजराती आणि भिली, गोंडी, कोरकू यांसारख्या आदिवासी भाषाही बोलतात."),
        sources=["census", "mh-sdb", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (2011)", "जनसंख्या (2011)", "लोकसंख्या (2011)"), mh["population2011"], "count", national=ind["population2011"]),
        fact("growth", L("Decadal growth 2001–2011", "दशकीय वृद्धि 2001–2011", "दशवार्षिक वाढ 2001–2011"),
             dp(16.0, "%", "2011", "census", "census", SDB, note="Via Maharashtra State Data Bank."), "percent",
             national=dp(17.7, "%", "2011", "census", "census", SDB, level="national")),
        fact("sr", L("Sex ratio (2011)", "लिंगानुपात (2011)", "लिंग गुणोत्तर (2011)"), mh["sexRatio2011"], "number", "higher-is-better", national=ind["sexRatio2011"]),
        fact("csr", L("Child sex ratio, 0–6 (2011)", "शिशु लिंगानुपात, 0–6 (2011)", "बाल लिंग गुणोत्तर, 0–6 (2011)"), mh["childSexRatio2011"], "number", "higher-is-better",
             previous=dp(913, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate (2011)", "साक्षरता दर (2011)", "साक्षरता दर (2011)"), mh["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("urb", L("Urban population share (2011)", "शहरी जनसंख्या का हिस्सा (2011)", "नागरी लोकसंख्येचे प्रमाण (2011)"), mh["urbanisation2011"], "percent", national=ind["urbanisation2011"]),
        fact("sc", L("Scheduled Castes (2011)", "अनुसूचित जातियाँ (2011)", "अनुसूचित जाती (2011)"),
             dp(11.81, "% of population", "2011", "census", "census", SW, note="1,32,75,898 persons (Social Welfare Department, GoM)."), "percent"),
        fact("st", L("Scheduled Tribes (2011)", "अनुसूचित जनजातियाँ (2011)", "अनुसूचित जमाती (2011)"),
             dp(9.35, "% of population", "2011", "census", "census", TRTI, note="1,05,10 thousand persons (Tribal Research & Training Institute, GoM)."), "percent",
             national=dp(8.61, "% of population", "2011", "census", "census", TRTI, level="national")),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 एका दृष्टिक्षेपात")),
    table("lang", L("Other major mother tongues (Census 2011)", "अन्य प्रमुख मातृभाषाएँ (जनगणना 2011)", "इतर प्रमुख मातृभाषा (जनगणना 2011)"),
          [col(L("Language", "भाषा", "भाषा")), col(L("Speakers", "बोलने वाले", "भाषक"), "right"), col(L("% of population", "जनसंख्या का %", "लोकसंख्येच्या %"), "right")],
          [[L("Hindi", "हिंदी", "हिंदी"), 14481513, "12.88"], [L("Urdu", "उर्दू", "उर्दू"), 7540324, "6.71"], [L("Gujarati", "गुजराती", "गुजराती"), 2371743, "2.11"],
           [L("Bhili", "भीली", "भिली"), 2247678, "2.00"], [L("Khandeshi", "खानदेशी", "खानदेशी"), 1616730, "1.43"], [L("Telugu", "तेलुगु", "तेलुगू"), 1320880, "1.17"],
           [L("Kannada", "कन्नड़", "कन्नड"), 1000463, "0.89"], [L("Sindhi", "सिंधी", "सिंधी"), 723748, "0.64"]],
          "census", LANG, period="2011",
          note=L("From the Government of Maharashtra's table of linguistic minorities, which does not list Marathi. Marathi's Census 2011 share is still to be added.",
                 "महाराष्ट्र सरकार की भाषाई अल्पसंख्यक तालिका से, जिसमें मराठी शामिल नहीं है। जनगणना 2011 में मराठी का हिस्सा अभी जोड़ा जाना है।",
                 "महाराष्ट्र शासनाच्या भाषिक अल्पसंख्याक तक्त्यातून, ज्यात मराठीचा समावेश नाही. जनगणना 2011 मधील मराठीचे प्रमाण अद्याप जोडायचे आहे.")),
    prose("tribal", L(
        "Maharashtra's Scheduled Tribes live mainly along the Sahyadri in the north-west (Nashik, Palghar, Thane, Nandurbar) and in the forested east (Gadchiroli, Chandrapur, Gondia, Yavatmal), with Melghat in Amravati district. Major communities include the Bhil, Gond, Warli, Kokna, Thakur and Korku. Three groups are listed as Particularly Vulnerable Tribal Groups: the Katkari (Kathodi), Kolam and Madia Gond. Parts of the State are notified Scheduled Areas under the Fifth Schedule of the Constitution.",
        "महाराष्ट्र की अनुसूचित जनजातियाँ मुख्यतः उत्तर-पश्चिम में सह्याद्रि के साथ (नासिक, पालघर, ठाणे, नंदुरबार) और पूर्व के वन क्षेत्रों (गढ़चिरौली, चंद्रपुर, गोंदिया, यवतमाल) में तथा अमरावती ज़िले के मेलघाट में रहती हैं। प्रमुख समुदायों में भील, गोंड, वारली, कोकणा, ठाकुर और कोरकू शामिल हैं। तीन समूह विशेष रूप से कमज़ोर जनजातीय समूह (पीवीटीजी) के रूप में सूचीबद्ध हैं: कातकरी (कातोडी), कोलाम और माडिया गोंड। राज्य के कुछ हिस्से संविधान की पाँचवीं अनुसूची के तहत अधिसूचित अनुसूचित क्षेत्र हैं।",
        "महाराष्ट्रातील अनुसूचित जमाती प्रामुख्याने वायव्येकडे सह्याद्रीलगत (नाशिक, पालघर, ठाणे, नंदुरबार), पूर्वेकडील वनक्षेत्रात (गडचिरोली, चंद्रपूर, गोंदिया, यवतमाळ) आणि अमरावती जिल्ह्यातील मेळघाटात राहतात. भिल्ल, गोंड, वारली, कोकणा, ठाकूर आणि कोरकू हे प्रमुख समुदाय आहेत. कातकरी (काथोडी), कोलाम आणि माडिया गोंड हे तीन गट विशेष असुरक्षित आदिवासी गट (पीव्हीटीजी) म्हणून सूचीबद्ध आहेत. राज्याचा काही भाग राज्यघटनेच्या पाचव्या अनुसूचीनुसार अधिसूचित अनुसूचित क्षेत्र आहे."),
        conf="Editorial", title=L("Tribal communities", "जनजातीय समुदाय", "आदिवासी समुदाय")),
    gaps("g", [
        (L("Religion (Census 2011 shares)", "धर्म (जनगणना 2011 हिस्सेदारी)", "धर्म (जनगणना 2011 प्रमाण)"), "census", "Table C-01, Maharashtra 2011 (censusindia.gov.in/nada catalog 11382)."),
        (L("Marathi speakers (Census 2011)", "मराठी भाषी (जनगणना 2011)", "मराठी भाषक (जनगणना 2011)"), "census", "Table C-16, Maharashtra 2011."),
        (L("Literacy by sex, 2001 and 2011", "लिंग के अनुसार साक्षरता, 2001 और 2011", "लिंगनिहाय साक्षरता, 2001 व 2011"), "census", "Census PCA / State Data Bank."),
        (L("Current population projection", "वर्तमान जनसंख्या प्रक्षेपण", "सध्याचे लोकसंख्या प्रक्षेपण"), "mohfw-projections", "Technical Group on Population Projections 2011–2036; label Projected."),
        (L("SDG India Index score", "एसडीजी इंडिया इंडेक्स स्कोर", "एसडीजी इंडिया इंडेक्स गुण"), "niti", "SDG India Index 2023-24 (India: 71)."),
        (L("Multidimensional Poverty Index", "बहुआयामी गरीबी सूचकांक", "बहुआयामी दारिद्र्य निर्देशांक"), "niti", "NITI Aayog National MPI 2023."),
    ]),
])

# ---------------- F. History ----------------
def ev(id, year, when, label, detail=None):
    e = {"id": id, "year": year, "when": when, "label": label}
    if detail: e["detail"] = detail
    return e

module(R, "history", [
    prose("p1", L(
        "The region's recorded history begins with the Satavahanas, who ruled much of the Deccan from Pratishthana (today's Paithan) around the turn of the common era. Successive dynasties — Vakatakas, Chalukyas, Rashtrakutas and the Yadavas of Devagiri — left behind the cave temples of Ajanta and Ellora. From the 14th century the Deccan sultanates held power until Chhatrapati Shivaji Maharaj founded the Maratha state in the 17th century. Maratha power later spread across much of India under the Peshwas, before British victory in 1818.\n\nUnder British rule, Bombay grew into a port and textile city and a centre of social reform and the freedom movement. After independence, the Samyukta Maharashtra movement led to the creation of a Marathi-speaking State on 1 May 1960.",
        "इस क्षेत्र का दर्ज इतिहास सातवाहनों से शुरू होता है, जिन्होंने ईसवी सन् के आसपास प्रतिष्ठान (आज का पैठण) से दक्कन के बड़े हिस्से पर शासन किया। बाद के राजवंशों — वाकाटक, चालुक्य, राष्ट्रकूट और देवगिरि के यादव — ने अजंता और एलोरा के गुफ़ा मंदिर छोड़े। 14वीं सदी से दक्कन की सल्तनतें सत्ता में रहीं, जब तक कि 17वीं सदी में छत्रपति शिवाजी महाराज ने मराठा राज्य की स्थापना नहीं की। बाद में पेशवाओं के नेतृत्व में मराठा शक्ति भारत के बड़े हिस्से तक फैली, और 1818 में अंग्रेज़ों की जीत हुई।\n\nब्रिटिश शासन में बंबई बंदरगाह और कपड़ा उद्योग का शहर बना, और समाज सुधार तथा स्वतंत्रता आंदोलन का केंद्र भी। आज़ादी के बाद संयुक्त महाराष्ट्र आंदोलन के फलस्वरूप 1 मई 1960 को मराठी भाषी राज्य बना।",
        "या प्रदेशाचा लिखित इतिहास सातवाहनांपासून सुरू होतो; इसवी सनाच्या आसपास त्यांनी प्रतिष्ठान (आजचे पैठण) येथून दख्खनच्या मोठ्या भागावर राज्य केले. त्यानंतरच्या राजघराण्यांनी — वाकाटक, चालुक्य, राष्ट्रकूट आणि देवगिरीचे यादव — अजिंठा-वेरूळची लेणी मागे ठेवली. चौदाव्या शतकापासून दख्खनच्या सुलतानशाह्या सत्तेवर होत्या; सतराव्या शतकात छत्रपती शिवाजी महाराजांनी मराठा राज्याची स्थापना केली. पुढे पेशव्यांच्या काळात मराठा सत्ता भारताच्या मोठ्या भागात पसरली, आणि 1818 मध्ये इंग्रजांचा विजय झाला.\n\nब्रिटिश राजवटीत मुंबई बंदर आणि कापडगिरण्यांचे शहर बनली, तसेच समाजसुधारणा आणि स्वातंत्र्यलढ्याचे केंद्रही. स्वातंत्र्यानंतर संयुक्त महाराष्ट्र चळवळीतून 1 मे 1960 रोजी मराठी भाषिक राज्य निर्माण झाले."),
        conf="Editorial"),
    {"type": "timeline", "id": "t", "title": L("Timeline", "समयरेखा", "कालरेषा"), "sourceId": None, "url": None, "accessDate": None, "confidence": "Editorial", "events": [
        ev("satavahana", -100, L("c. 1st century BCE", "लगभग पहली सदी ईसा पूर्व", "सुमारे इ.स.पू. पहिले शतक"), L("Satavahanas rule from Pratishthana (Paithan)", "प्रतिष्ठान (पैठण) से सातवाहनों का शासन", "प्रतिष्ठान (पैठण) येथून सातवाहनांची राजवट")),
        ev("ajanta", 460, L("5th century CE", "5वीं सदी ईसवी", "इ.स. पाचवे शतक"), L("Major phase of the Ajanta caves under the Vakatakas", "वाकाटकों के समय अजंता गुफ़ाओं का प्रमुख चरण", "वाकाटकांच्या काळात अजिंठा लेण्यांचा प्रमुख टप्पा")),
        ev("kailasa", 760, L("8th century", "8वीं सदी", "आठवे शतक"), L("Kailasa temple carved at Ellora under the Rashtrakutas", "राष्ट्रकूटों के समय एलोरा में कैलास मंदिर की खुदाई", "राष्ट्रकूटांच्या काळात वेरूळ येथे कैलास मंदिराचे कोरीवकाम")),
        ev("dnyaneshwari", 1290, L("1290", "1290", "1290"), L("Sant Dnyaneshwar completes the Dnyaneshwari", "संत ज्ञानेश्वर ने ज्ञानेश्वरी पूरी की", "संत ज्ञानेश्वरांनी ज्ञानेश्वरी पूर्ण केली")),
        ev("bahmani", 1347, L("1347", "1347", "1347"), L("Bahmani Sultanate founded in the Deccan", "दक्कन में बहमनी सल्तनत की स्थापना", "दख्खनमध्ये बहमनी सुलतानशाहीची स्थापना")),
        ev("shivaji", 1674, L("1674", "1674", "1674"), L("Coronation of Chhatrapati Shivaji Maharaj at Raigad", "रायगढ़ में छत्रपति शिवाजी महाराज का राज्याभिषेक", "रायगडावर छत्रपती शिवाजी महाराजांचा राज्याभिषेक")),
        ev("1818", 1818, L("1818", "1818", "1818"), L("End of Peshwa rule after the Third Anglo-Maratha War", "तीसरे आंग्ल-मराठा युद्ध के बाद पेशवा शासन का अंत", "तिसऱ्या इंग्रज-मराठा युद्धानंतर पेशवाईचा अस्त")),
        ev("rail", 1853, L("16 April 1853", "16 अप्रैल 1853", "16 एप्रिल 1853"), L("India's first passenger train runs from Bori Bunder to Thane", "बोरी बंदर से ठाणे तक भारत की पहली यात्री रेलगाड़ी चली", "बोरीबंदर ते ठाणे अशी भारतातील पहिली प्रवासी रेल्वे धावली")),
        ev("satyashodhak", 1873, L("1873", "1873", "1873"), L("Jyotirao Phule founds the Satyashodhak Samaj", "ज्योतिराव फुले ने सत्यशोधक समाज की स्थापना की", "जोतीराव फुले यांनी सत्यशोधक समाजाची स्थापना केली")),
        ev("inc", 1885, L("1885", "1885", "1885"), L("Indian National Congress holds its first session in Bombay", "बंबई में भारतीय राष्ट्रीय कांग्रेस का पहला अधिवेशन", "मुंबईत भारतीय राष्ट्रीय काँग्रेसचे पहिले अधिवेशन")),
        ev("mahad", 1927, L("1927", "1927", "1927"), L("Dr B. R. Ambedkar leads the Mahad Satyagraha", "डॉ. बी. आर. आंबेडकर के नेतृत्व में महाड सत्याग्रह", "डॉ. बाबासाहेब आंबेडकरांच्या नेतृत्वाखाली महाडचा सत्याग्रह")),
        ev("quit", 1942, L("8 August 1942", "8 अगस्त 1942", "8 ऑगस्ट 1942"), L("Quit India resolution adopted at Gowalia Tank, Bombay", "बंबई के गोवालिया टैंक मैदान में भारत छोड़ो प्रस्ताव पारित", "मुंबईतील गोवालिया टँक मैदानावर ‘चले जाव’ ठराव मंजूर")),
        ev("1960", 1960, L("1 May 1960", "1 मई 1960", "1 मे 1960"), L("Maharashtra State formed", "महाराष्ट्र राज्य का गठन", "महाराष्ट्र राज्याची स्थापना"), L("Bombay Reorganisation Act, 1960, after the Samyukta Maharashtra movement.", "संयुक्त महाराष्ट्र आंदोलन के बाद बंबई पुनर्गठन अधिनियम, 1960।", "संयुक्त महाराष्ट्र चळवळीनंतर मुंबई पुनर्रचना अधिनियम, 1960.")),
    ]},
    table("whs", L("UNESCO World Heritage properties", "यूनेस्को विश्व धरोहर स्थल", "युनेस्को जागतिक वारसा स्थळे"),
          [col(L("Property", "स्थल", "स्थळ")), col(L("Inscribed", "सूची में शामिल", "समावेश"), "right"), col(L("Type", "प्रकार", "प्रकार"))],
          [[L("Ajanta Caves", "अजंता गुफ़ाएँ", "अजिंठा लेणी"), "1983", L("Cultural", "सांस्कृतिक", "सांस्कृतिक")],
           [L("Ellora Caves", "एलोरा गुफ़ाएँ", "वेरूळ लेणी"), "1983", L("Cultural", "सांस्कृतिक", "सांस्कृतिक")],
           [L("Elephanta Caves", "एलिफेंटा गुफ़ाएँ", "घारापुरी (एलिफंटा) लेणी"), "1987", L("Cultural", "सांस्कृतिक", "सांस्कृतिक")],
           [L("Chhatrapati Shivaji Terminus", "छत्रपति शिवाजी टर्मिनस", "छत्रपती शिवाजी टर्मिनस"), "2004", L("Cultural", "सांस्कृतिक", "सांस्कृतिक")],
           [L("Western Ghats (serial, shared with other States)", "पश्चिमी घाट (कई राज्यों में फैली शृंखला)", "पश्चिम घाट (अनेक राज्यांत विखुरलेली मालिका)"), "2012", L("Natural", "प्राकृतिक", "नैसर्गिक")],
           [L("Victorian Gothic and Art Deco Ensembles of Mumbai", "मुंबई के विक्टोरियन गॉथिक और आर्ट डेको समूह", "मुंबईतील व्हिक्टोरियन गॉथिक व आर्ट डेको वास्तुसमूह"), "2018", L("Cultural", "सांस्कृतिक", "सांस्कृतिक")],
           [L("Maratha Military Landscapes of India (11 of 12 forts are in Maharashtra)", "भारत के मराठा सैन्य परिदृश्य (12 में से 11 क़िले महाराष्ट्र में)", "भारतातील मराठा लष्करी भूप्रदेश (12 पैकी 11 किल्ले महाराष्ट्रात)"), "2025", L("Cultural", "सांस्कृतिक", "सांस्कृतिक")]],
          "unesco-whc", UNESCO,
          note=L("The Maratha forts are Shivneri, Lohagad, Raigad, Suvarnadurg, Panhala, Vijaydurg, Sindhudurg, Salher, Rajgad, Khanderi and Pratapgad; the twelfth, Gingee, is in Tamil Nadu. On the Tentative List: coastal fortifications of the Konkan (2024) and the Deccan Traps at Panchgani and Mahabaleshwar (2025).",
                 "मराठा क़िले हैं: शिवनेरी, लोहगढ़, रायगढ़, सुवर्णदुर्ग, पन्हाला, विजयदुर्ग, सिंधुदुर्ग, साल्हेर, राजगढ़, खांदेरी और प्रतापगढ़; बारहवाँ, जिंजी, तमिलनाडु में है। संभावित सूची में: कोंकण के तटीय क़िले (2024) और पंचगनी व महाबलेश्वर के दक्कन ट्रैप (2025)।",
                 "मराठा किल्ले: शिवनेरी, लोहगड, रायगड, सुवर्णदुर्ग, पन्हाळा, विजयदुर्ग, सिंधुदुर्ग, साल्हेर, राजगड, खांदेरी आणि प्रतापगड; बारावा, जिंजी, तमिळनाडूमध्ये आहे. संभाव्य यादीत: कोकणातील सागरी तटबंदी (2024) आणि पाचगणी-महाबळेश्वरचे दख्खन ट्रॅप (2025).")),
])
print("mod1 ok")
