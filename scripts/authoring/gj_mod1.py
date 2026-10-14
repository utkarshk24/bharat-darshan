"""Gujarat modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-GJ"
SER = "https://data.opencity.in/dataset/ac23cf45-bf10-4f17-b389-cb49c6c72fc6/resource/1704d67b-ca8d-4231-9540-389f7c8001ae/download/socioeconomicreview202223english27_02_23_10_14_25.pdf"
NITI = "https://www.niti.gov.in/sites/default/files/2025-03/Macro-and-Fiscal-Landscape-of-the-State-of-Gujarat-1.pdf"
VAV = "https://newsonair.gov.in/gujarat-govt-approves-creation-of-new-district-named-vav-tharad"
gj = read("regions/IN-GJ.json")["metrics"]; ind = read("india.json")["metrics"]
NAME = L("Gujarat", "गुजरात", "गुजरात")

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Gujarat is India's westernmost State, with the country's longest coastline — about 1,600 km along the Arabian Sea, the Gulf of Kutch and the Gulf of Khambhat. It had 6.04 crore people at the 2011 Census. Gandhinagar is the capital; Ahmedabad is the largest city, and Surat, Vadodara and Rajkot are the other major centres. The State is one of India's main industrial and trading economies, with large ports, refineries, chemical and pharmaceutical plants, textiles and diamond polishing.\n\nGujarat was formed on 1 May 1960, when the bilingual Bombay State was divided into Gujarat and Maharashtra. Gujarati is the official language.",
        "गुजरात भारत का सबसे पश्चिमी राज्य है, जिसकी तटरेखा देश में सबसे लंबी है — अरब सागर, कच्छ की खाड़ी और खंभात की खाड़ी के साथ लगभग 1,600 किमी। 2011 की जनगणना में यहाँ 6.04 करोड़ लोग थे। गांधीनगर राजधानी है; अहमदाबाद सबसे बड़ा शहर है, और सूरत, वडोदरा और राजकोट अन्य बड़े केंद्र हैं। राज्य भारत की प्रमुख औद्योगिक और व्यापारिक अर्थव्यवस्थाओं में है, जहाँ बड़े बंदरगाह, रिफ़ाइनरियाँ, रसायन और दवा संयंत्र, कपड़ा उद्योग और हीरा तराशी है।\n\nगुजरात 1 मई 1960 को बना, जब द्विभाषी बॉम्बे राज्य को गुजरात और महाराष्ट्र में बाँटा गया। गुजराती राजभाषा है।",
        "गुजरात हे भारताचे सर्वांत पश्चिमेकडील राज्य असून त्याची किनारपट्टी देशात सर्वांत लांब आहे — अरबी समुद्र, कच्छचे आखात व खंबायतच्या आखातालगत सुमारे 1,600 किमी. 2011 च्या जनगणनेनुसार इथे 6.04 कोटी लोक होते. गांधीनगर ही राजधानी; अहमदाबाद हे सर्वांत मोठे शहर, आणि सुरत, वडोदरा व राजकोट ही इतर मोठी केंद्रे आहेत. राज्य भारताच्या प्रमुख औद्योगिक व व्यापारी अर्थव्यवस्थांपैकी एक आहे — मोठी बंदरे, तेलशुद्धीकरण कारखाने, रसायन व औषध प्रकल्प, कापड उद्योग आणि हिरे पैलू पाडणे.\n\nद्विभाषिक मुंबई राज्याचे गुजरात व महाराष्ट्र असे विभाजन होऊन 1 मे 1960 रोजी गुजरातची निर्मिती झाली. गुजराती ही राजभाषा आहे."),
        sources=["gj-des", "census"], conf="Editorial"),
    prose("intro-unique", L(
        "Gujarat holds some of the oldest and newest chapters of Indian history. Dholavira and Lothal are major cities of the Harappan civilisation; Somnath and Dwarka are ancient pilgrimage sites; Ahmedabad was the first Indian city listed by UNESCO as a World Heritage City. Mahatma Gandhi was born at Porbandar and led the Salt March from Ahmedabad's Sabarmati Ashram, and Sardar Vallabhbhai Patel, who united the princely states, came from Kheda. The Gir forest is the last wild home of the Asiatic lion, and the salt desert of the Rann of Kutch turns into a white plain each winter. Navratri garba, now on UNESCO's intangible heritage list, is the State's best-known festival.",
        "गुजरात में भारतीय इतिहास के सबसे पुराने और सबसे नए, दोनों अध्याय हैं। धोलावीरा और लोथल हड़प्पा सभ्यता के बड़े नगर हैं; सोमनाथ और द्वारका प्राचीन तीर्थ हैं; अहमदाबाद यूनेस्को द्वारा विश्व धरोहर नगर घोषित होने वाला पहला भारतीय शहर है। महात्मा गांधी का जन्म पोरबंदर में हुआ और उन्होंने अहमदाबाद के साबरमती आश्रम से दांडी यात्रा शुरू की, और रियासतों का एकीकरण करने वाले सरदार वल्लभभाई पटेल खेड़ा से थे। गिर का वन एशियाई सिंह का अंतिम प्राकृतिक आवास है, और कच्छ के रण का नमक मरुस्थल हर सर्दी में सफ़ेद मैदान बन जाता है। नवरात्रि का गरबा, जो अब यूनेस्को की अमूर्त धरोहर सूची में है, राज्य का सबसे प्रसिद्ध उत्सव है।",
        "गुजरातमध्ये भारतीय इतिहासाची सर्वांत जुनी आणि सर्वांत नवी, दोन्ही प्रकरणे आहेत. धोलावीरा व लोथल ही हडप्पा संस्कृतीची मोठी नगरे आहेत; सोमनाथ व द्वारका ही प्राचीन तीर्थक्षेत्रे आहेत; युनेस्कोने जागतिक वारसा शहर म्हणून घोषित केलेले अहमदाबाद हे पहिले भारतीय शहर आहे. महात्मा गांधींचा जन्म पोरबंदर येथे झाला आणि त्यांनी अहमदाबादच्या साबरमती आश्रमातून दांडी यात्रा सुरू केली, तर संस्थानांचे विलीनीकरण घडवणारे सरदार वल्लभभाई पटेल खेडा जिल्ह्याचे होते. गीरचे जंगल हे आशियाई सिंहाचे शेवटचे नैसर्गिक निवासस्थान आहे, आणि कच्छच्या रणातील मिठाचे वाळवंट दर हिवाळ्यात पांढरे मैदान बनते. नवरात्रीचा गरबा — आता युनेस्कोच्या अमूर्त वारसा यादीत — हा राज्याचा सर्वांत प्रसिद्ध उत्सव आहे."),
        title=L("What makes Gujarat unique?", "गुजरात को ख़ास क्या बनाता है?", "गुजरातचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("State formed", "राज्य गठन", "राज्यनिर्मिती"), L("1 May 1960 (Gujarat Day)", "1 मई 1960 (गुजरात दिवस)", "1 मे 1960 (गुजरात दिन)")],
           [L("Districts", "ज़िले", "जिल्हे"), "34"],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Gujarati", "गुजराती", "गुजराती")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Ahmedabad", "अहमदाबाद", "अहमदाबाद")],
           [L("Coastline", "तटरेखा", "किनारपट्टी"), L("About 1,600 km", "लगभग 1,600 किमी", "सुमारे 1,600 किमी")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-GJ / GJ"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          "newsonair", VAV, conf="Editorial",
          note=L("34 districts after Vav-Tharad was carved out of Banaskantha in January 2025 (News On AIR). Coastline as given in the State's Socio-Economic Review 2022-23. Other rows are editorial and will be linked to notifications in review.",
                 "जनवरी 2025 में बनासकांठा से वाव-थराद ज़िला बनने के बाद 34 ज़िले (न्यूज़ ऑन एआईआर)। तटरेखा राज्य की सामाजिक-आर्थिक समीक्षा 2022-23 के अनुसार। बाकी पंक्तियाँ संपादकीय हैं; समीक्षा में अधिसूचनाओं से जोड़ी जाएँगी।",
                 "जानेवारी 2025 मध्ये बनासकांठातून वाव-थराद जिल्हा निर्माण झाल्यानंतर 34 जिल्हे (न्यूज ऑन एआयआर). किनारपट्टी राज्याच्या सामाजिक-आर्थिक आढावा 2022-23 नुसार. इतर ओळी संपादकीय असून तपासणीत अधिसूचनांशी जोडल्या जातील.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Gujarat has three main regions. Kutch in the north-west is a largely arid district bounded by the Great and Little Rann — vast salt flats that flood in the monsoon and dry into white crust in winter — and the Gulf of Kutch, with its coral reefs and mangroves. Saurashtra (Kathiawar) is a broad peninsula of low plateau and hills, including the Gir forest and the Girnar hills near Junagadh, with a long coastline from Dwarka to Bhavnagar. Mainland Gujarat, east of the Gulf of Khambhat, runs from the Banaskantha and Mehsana plains in the north through the fertile Charotar region around Anand to the wetter south, where the Western Ghats begin in the Dang forests.\n\nThe major rivers — the Narmada, Tapi, Mahi and Sabarmati — flow west to the sea through the mainland. The Sardar Sarovar dam on the Narmada carries water by canal across much of the State, as far as Kutch and Saurashtra.",
        "गुजरात के तीन मुख्य क्षेत्र हैं। उत्तर-पश्चिम में कच्छ एक अधिकतर शुष्क ज़िला है, जिसके किनारे बड़ा और छोटा रण हैं — विशाल नमक के मैदान, जो मानसून में जलमग्न हो जाते हैं और सर्दियों में सूखकर सफ़ेद परत बन जाते हैं — और कच्छ की खाड़ी, जहाँ प्रवाल भित्तियाँ और मैंग्रोव हैं। सौराष्ट्र (काठियावाड़) निचले पठार और पहाड़ियों वाला चौड़ा प्रायद्वीप है, जिसमें गिर वन और जूनागढ़ के पास गिरनार पहाड़ियाँ हैं, और द्वारका से भावनगर तक लंबी तटरेखा है। खंभात की खाड़ी के पूर्व में मुख्य भूमि गुजरात उत्तर में बनासकांठा और मेहसाणा के मैदानों से आणंद के आसपास के उपजाऊ चरोतर क्षेत्र होते हुए अधिक वर्षा वाले दक्षिण तक फैला है, जहाँ डांग के वनों में पश्चिमी घाट शुरू होते हैं।\n\nप्रमुख नदियाँ — नर्मदा, तापी, माही और साबरमती — मुख्य भूमि से होकर पश्चिम में समुद्र तक बहती हैं। नर्मदा पर सरदार सरोवर बाँध नहरों से राज्य के बड़े हिस्से में, कच्छ और सौराष्ट्र तक, पानी पहुँचाता है।",
        "गुजरातचे तीन मुख्य प्रदेश आहेत. वायव्येकडील कच्छ हा मुख्यतः शुष्क जिल्हा असून त्याच्या कडेला मोठे व छोटे रण आहे — मिठाची विस्तीर्ण मैदाने, जी पावसाळ्यात पाण्याखाली जातात आणि हिवाळ्यात सुकून पांढरा थर बनतात — आणि प्रवाळभित्ती व खारफुटी असलेले कच्छचे आखात. सौराष्ट्र (काठियावाड) हे सखल पठार व टेकड्यांचे विस्तीर्ण द्वीपकल्प असून त्यात गीरचे जंगल व जुनागडजवळील गिरनार डोंगर आहेत, आणि द्वारकेपासून भावनगरपर्यंत लांब किनारा आहे. खंबायतच्या आखाताच्या पूर्वेकडील मुख्य भूमीचा गुजरात उत्तरेकडील बनासकांठा व मेहसाणाच्या मैदानांपासून आणंदभोवतीच्या सुपीक चरोतर प्रदेशामार्गे अधिक पावसाच्या दक्षिण भागापर्यंत पसरला आहे, जिथे डांगच्या जंगलांत पश्चिम घाट सुरू होतात.\n\nप्रमुख नद्या — नर्मदा, तापी, मही व साबरमती — मुख्य भूमीतून पश्चिमेकडे समुद्राला मिळतात. नर्मदेवरील सरदार सरोवर धरण कालव्यांद्वारे राज्याच्या मोठ्या भागात, कच्छ व सौराष्ट्रापर्यंत, पाणी पोहोचवते."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), gj["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("pk", "Pakistan (north-west)", "पाकिस्तान (उत्तर-पश्चिम)", "पाकिस्तान (वायव्य)"), it3("rj", "Rajasthan (north-east)", "राजस्थान (उत्तर-पूर्व)", "राजस्थान (ईशान्य)"),
        it3("mp", "Madhya Pradesh (east)", "मध्य प्रदेश (पूर्व)", "मध्य प्रदेश (पूर्व)"), it3("mh", "Maharashtra (south-east)", "महाराष्ट्र (दक्षिण-पूर्व)", "महाराष्ट्र (आग्नेय)"),
        it3("dh", "Dadra & Nagar Haveli and Daman & Diu", "दादरा और नगर हवेली तथा दमन और दीव", "दादरा व नगर हवेली आणि दमण व दीव"),
        it3("sea", "Arabian Sea (west and south)", "अरब सागर (पश्चिम और दक्षिण)", "अरबी समुद्र (पश्चिम व दक्षिण)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("narmada", "Narmada", "नर्मदा", "नर्मदा", d=("Sardar Sarovar dam and the Statue of Unity at Kevadia; reaches the sea near Bharuch.", "केवड़िया में सरदार सरोवर बाँध और स्टैच्यू ऑफ़ यूनिटी; भरूच के पास समुद्र से मिलती है।", "केवडिया येथे सरदार सरोवर धरण व स्टॅच्यू ऑफ युनिटी; भरूचजवळ समुद्राला मिळते.")),
        it3("tapi", "Tapi", "तापी", "तापी", d=("Flows through Surat to the sea; Ukai dam.", "सूरत से होकर समुद्र तक; उकाई बाँध।", "सुरतमधून समुद्रापर्यंत; उकाई धरण.")),
        it3("mahi", "Mahi", "माही", "मही", d=("Enters the Gulf of Khambhat; Kadana and Wanakbori dams.", "खंभात की खाड़ी में मिलती है; कडाणा और वणाकबोरी बाँध।", "खंबायतच्या आखाताला मिळते; कडाणा व वणाकबोरी धरणे.")),
        it3("sabarmati", "Sabarmati", "साबरमती", "साबरमती", d=("Flows through Ahmedabad; riverfront and Gandhi's ashram.", "अहमदाबाद से होकर बहती है; रिवरफ़्रंट और गांधी आश्रम।", "अहमदाबादमधून वाहते; रिव्हरफ्रंट व गांधी आश्रम.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point (Girnar) — official elevation", "सर्वोच्च बिंदु (गिरनार) — आधिकारिक ऊँचाई", "सर्वोच्च शिखर (गिरनार) — अधिकृत उंची"), "survey-of-india", "Survey of India or the State gazetteer."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1); Kutch is in the highest zone."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Most of Gujarat has a hot, semi-arid climate. Summers (March–June) are very hot, with temperatures often above 42 °C in Ahmedabad and Kutch. The south-west monsoon, from late June to September, brings heavy rain to the south — Valsad, Navsari and the Dangs — and much less to the north and Kutch, which are prone to drought. Winters (November–February) are mild and dry, though the Rann and northern districts can be cold at night. Coastal Saurashtra and Kutch are exposed to Arabian Sea cyclones in May–June and October–November.",
        "गुजरात के अधिकांश भाग की जलवायु गर्म, अर्ध-शुष्क है। गर्मियाँ (मार्च–जून) बहुत गर्म होती हैं, और अहमदाबाद व कच्छ में तापमान अक्सर 42 °C से ऊपर रहता है। जून के अंत से सितंबर तक दक्षिण-पश्चिम मानसून दक्षिण — वलसाड, नवसारी और डांग — में भारी वर्षा लाता है, जबकि उत्तर और कच्छ में बहुत कम, जो सूखा-प्रवण हैं। सर्दियाँ (नवंबर–फ़रवरी) सुहावनी और सूखी होती हैं, हालाँकि रण और उत्तरी ज़िलों में रातें ठंडी हो सकती हैं। तटीय सौराष्ट्र और कच्छ मई–जून और अक्टूबर–नवंबर में अरब सागर के चक्रवातों की चपेट में आते हैं।",
        "गुजरातच्या बहुतांश भागाचे हवामान उष्ण, अर्धशुष्क आहे. उन्हाळा (मार्च–जून) अतिशय उष्ण असतो, आणि अहमदाबाद व कच्छमध्ये तापमान अनेकदा 42 °C च्या पुढे जाते. जूनच्या अखेरीपासून सप्टेंबरपर्यंत नैर्ऋत्य मान्सून दक्षिणेत — वलसाड, नवसारी व डांग — मुसळधार पाऊस आणतो, तर उत्तर भाग व कच्छमध्ये फार कमी, जे दुष्काळप्रवण आहेत. हिवाळा (नोव्हेंबर–फेब्रुवारी) सौम्य व कोरडा असतो, मात्र रण व उत्तरेकडील जिल्ह्यांत रात्री थंड असू शकतात. किनारी सौराष्ट्र व कच्छ मे–जून आणि ऑक्टोबर–नोव्हेंबरमध्ये अरबी समुद्रातील चक्रीवादळांच्या तडाख्यात येतात."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Ahmedabad", "अहमदाबाद", "अहमदाबाद"), "lat": 23.0225, "lon": 72.5714},
        {"name": L("Surat", "सूरत", "सुरत"), "lat": 21.1702, "lon": 72.8311},
        {"name": L("Rajkot", "राजकोट", "राजकोट"), "lat": 22.3039, "lon": 70.8022},
        {"name": L("Bhuj", "भुज", "भुज"), "lat": 23.2420, "lon": 69.6669},
    ]},
    lst("best", [
        it3("winter", "November to February", "नवंबर से फ़रवरी", "नोव्हेंबर ते फेब्रुवारी", d=("Best overall; the Rann Utsav in Kutch and Gir safaris (park open mid-October to mid-June).", "सबसे अच्छा समय; कच्छ में रण उत्सव और गिर सफ़ारी (उद्यान मध्य-अक्टूबर से मध्य-जून तक खुला)।", "सर्वोत्तम काळ; कच्छमधील रण उत्सव आणि गीर सफारी (उद्यान ऑक्टोबरच्या मध्यापासून जूनच्या मध्यापर्यंत खुले).")),
        it3("navratri", "September–October (Navratri)", "सितंबर–अक्टूबर (नवरात्रि)", "सप्टेंबर–ऑक्टोबर (नवरात्र)", d=("Nine nights of garba across the State.", "पूरे राज्य में नौ रातों का गरबा।", "राज्यभर नऊ रात्री गरबा.")),
        it3("summer", "March to June", "मार्च से जून", "मार्च ते जून", d=("Very hot; plan early mornings.", "बहुत गर्मी; सुबह जल्दी की योजना बनाएँ।", "अतिशय उष्ण; सकाळी लवकर नियोजन करा.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (State and sub-divisions)", "सामान्य वार्षिक वर्षा (राज्य और उप-मंडल)", "सरासरी वार्षिक पाऊस (राज्य व उपविभाग)"), "imd", "IMD rainfall statistics for Gujarat Region and Saurashtra & Kutch."),
        (L("Cyclone landfalls by year", "वर्षवार चक्रवात का तट पर पहुँचना", "वर्षनिहाय चक्रीवादळांचे किनाऱ्यावर येणे"), "imd", "IMD cyclone e-Atlas."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Gujarat is a State of traders and early risers. Ahmedabad's old city is a maze of pols — gated neighbourhoods of carved wooden houses — with the Manek Chowk night food market opening as the jewellers close. Surat hums with diamond-cutting units and textile markets, and Rajkot and Morbi with small factories making engine parts and ceramics. Food is mostly vegetarian and often a little sweet: dhokla, thepla and khakhra for breakfast, and a full thali at lunch. Kite-flying fills the skies at Uttarayan in January, and during Navratri entire towns stay up dancing garba and dandiya until late at night. In Kutch, village crafts — embroidery, bandhani, ajrakh printing — are part of daily life.",
        "गुजरात व्यापारियों और जल्दी उठने वालों का राज्य है। अहमदाबाद का पुराना शहर पोलों की भूलभुलैया है — नक़्क़ाशीदार लकड़ी के घरों वाले बंद मोहल्ले — और जौहरियों की दुकानें बंद होते ही माणेक चौक का रात्रि खाद्य बाज़ार खुल जाता है। सूरत हीरा तराशी इकाइयों और कपड़ा बाज़ारों से, और राजकोट व मोरबी इंजन पुर्ज़े और सिरेमिक बनाने वाले छोटे कारख़ानों से गूँजते हैं। भोजन अधिकतर शाकाहारी और अक्सर हल्का मीठा होता है: नाश्ते में ढोकला, थेपला और खाखरा, और दोपहर में पूरी थाली। जनवरी में उत्तरायण पर पतंगें आसमान भर देती हैं, और नवरात्रि में पूरे-पूरे शहर देर रात तक गरबा और डांडिया करते हैं। कच्छ में गाँवों के शिल्प — कढ़ाई, बांधनी, अजरख छपाई — रोज़मर्रा के जीवन का हिस्सा हैं।",
        "गुजरात हे व्यापाऱ्यांचे आणि लवकर उठणाऱ्यांचे राज्य आहे. अहमदाबादचे जुने शहर पोळांचा चक्रव्यूह आहे — कोरीव लाकडी घरांच्या बंदिस्त वस्त्या — आणि सराफांची दुकाने बंद होताच माणेक चौकचा रात्रीचा खाऊ बाजार सुरू होतो. सुरत हिरे पैलू पाडणाऱ्या युनिट्स व कापडबाजारांनी, तर राजकोट व मोरबी इंजिनचे सुटे भाग व सिरॅमिक बनवणाऱ्या लहान कारखान्यांनी गजबजलेले असतात. जेवण मुख्यतः शाकाहारी आणि अनेकदा किंचित गोड असते: न्याहारीला ढोकळा, थेपला व खाकरा, आणि दुपारी पूर्ण थाळी. जानेवारीत उत्तरायणाला पतंगांनी आकाश भरून जाते, आणि नवरात्रीत अख्खी शहरे रात्री उशिरापर्यंत गरबा व दांडिया खेळतात. कच्छमध्ये गावांतील हस्तकला — भरतकाम, बांधणी, अजरख छपाई — रोजच्या जीवनाचा भाग आहे."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "At the 2011 Census Gujarat had 6.04 crore people. The sex ratio was 919 women per 1,000 men, below the national 943, and the child sex ratio was 890, among the lower figures in India. Literacy was 78.0%, above the national 73.0%. The State is relatively urbanised — the Socio-Economic Review puts the urban population at about 2.57 crore of 6.04 crore — with Ahmedabad, Surat, Vadodara and Rajkot the largest cities. Scheduled Castes made up 6.7% and Scheduled Tribes 14.8% of the population; the tribal belt runs along the eastern hills from Banaskantha to the Dangs.\n\nGujarati is spoken by most people. Kutchi is spoken in Kutch, Bhili and other tribal languages in the east, and Hindi, Sindhi, Marathi and Urdu by large communities in the cities.",
        "2011 की जनगणना में गुजरात की जनसंख्या 6.04 करोड़ थी। लिंगानुपात प्रति 1,000 पुरुषों पर 919 महिलाएँ था, जो राष्ट्रीय 943 से कम है, और शिशु लिंगानुपात 890 था, जो भारत में निचले आँकड़ों में है। साक्षरता 78.0% थी, जो राष्ट्रीय 73.0% से अधिक है। राज्य अपेक्षाकृत शहरीकृत है — सामाजिक-आर्थिक समीक्षा के अनुसार 6.04 करोड़ में से लगभग 2.57 करोड़ लोग शहरों में थे — और अहमदाबाद, सूरत, वडोदरा और राजकोट सबसे बड़े शहर हैं। अनुसूचित जातियाँ जनसंख्या का 6.7% और अनुसूचित जनजातियाँ 14.8% थीं; आदिवासी पट्टी बनासकांठा से डांग तक पूर्वी पहाड़ियों के साथ फैली है।\n\nअधिकांश लोग गुजराती बोलते हैं। कच्छ में कच्छी, पूर्व में भीली और अन्य आदिवासी भाषाएँ, और शहरों में बड़े समुदाय हिंदी, सिंधी, मराठी और उर्दू बोलते हैं।",
        "2011 च्या जनगणनेनुसार गुजरातची लोकसंख्या 6.04 कोटी होती. दर 1,000 पुरुषांमागे 919 स्त्रिया होत्या — राष्ट्रीय 943 पेक्षा कमी — आणि बाल लिंग गुणोत्तर 890 होते, जे भारतातील कमी आकड्यांपैकी आहे. साक्षरता 78.0% होती, राष्ट्रीय 73.0% पेक्षा जास्त. राज्य तुलनेने नागरीकृत आहे — सामाजिक-आर्थिक आढाव्यानुसार 6.04 कोटींपैकी सुमारे 2.57 कोटी लोक शहरांत होते — आणि अहमदाबाद, सुरत, वडोदरा व राजकोट ही सर्वांत मोठी शहरे आहेत. अनुसूचित जाती लोकसंख्येच्या 6.7% आणि अनुसूचित जमाती 14.8% होत्या; आदिवासी पट्टा बनासकांठापासून डांगपर्यंत पूर्वेकडील डोंगररांगांलगत पसरला आहे.\n\nबहुसंख्य लोक गुजराती बोलतात. कच्छमध्ये कच्छी, पूर्वेकडे भिल्ली व इतर आदिवासी भाषा, आणि शहरांत मोठे समुदाय हिंदी, सिंधी, मराठी व उर्दू बोलतात."),
        sources=["census", "es-india", "niti", "gj-des"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), gj["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), gj["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"]),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), gj["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(883, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), gj["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), gj["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(6.7, "%", "2011", "census", "niti", NITI, note="NITI Aayog, 'Macro and Fiscal Landscape of the State of Gujarat' (2025), citing Census 2011."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(14.8, "%", "2011", "census", "niti", NITI, note="Same report, citing Census 2011."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("gu", "Gujarati", "गुजराती", "गुजराती", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("kfr", "Kutchi", "कच्छी", "कच्छी", m=("Kutch", "कच्छ", "कच्छ")),
        it3("bhb", "Bhili and other tribal languages", "भीली और अन्य आदिवासी भाषाएँ", "भिल्ली व इतर आदिवासी भाषा", m=("Eastern hills", "पूर्वी पहाड़ियाँ", "पूर्वेकडील डोंगर")),
        it3("hi", "Hindi", "हिंदी", "हिंदी"), it3("sd", "Sindhi", "सिंधी", "सिंधी"), it3("mr", "Marathi", "मराठी", "मराठी"), it3("ur", "Urdu", "उर्दू", "उर्दू"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract; the State review gives only rounded crore figures."),
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Final Population Totals for Gujarat."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Gujarat has some of the most important sites of the Harappan civilisation: Lothal, with its dockyard, and Dholavira in the Rann of Kutch, with its reservoirs and planned city, flourished in the third millennium BCE. Ashoka's edicts are carved on a rock at Junagadh, which also bears inscriptions of the Western Kshatrapas and the Guptas. The Maitrakas of Vallabhi and then the Chaulukyas (Solankis) of Anhilwad Patan ruled the region; the Solankis built the Rani ki Vav stepwell at Patan and the Sun Temple at Modhera, and Jain merchants and patrons raised the temples of Palitana and Girnar. Somnath, on the Saurashtra coast, was raided by Mahmud of Ghazni in 1026 and rebuilt many times.\n\nThe Gujarat Sultanate founded Ahmedabad in 1411 and built its mosques and stepwells; the Mughals took Gujarat in 1573, and the Marathas followed in the 18th century. Surat became a great port, where the English East India Company set up one of its first factories in 1613. Under British rule much of Gujarat was divided among hundreds of princely states. Gandhi's Sabarmati Ashram and the Salt March of 1930, and Sardar Patel's Bardoli satyagraha of 1928, made Gujarat central to the national movement. After Independence the region was part of Bombay State until Gujarat was formed in 1960.",
        "गुजरात में हड़प्पा सभ्यता के कुछ सबसे महत्त्वपूर्ण स्थल हैं: गोदी वाला लोथल और जलाशयों व नियोजित नगर वाला कच्छ के रण का धोलावीरा, जो ईसा पूर्व तीसरी सहस्राब्दी में फले-फूले। जूनागढ़ की एक चट्टान पर अशोक के शिलालेख हैं, जिस पर पश्चिमी क्षत्रपों और गुप्तों के लेख भी हैं। वल्लभी के मैत्रकों और फिर अणहिलवाड़ पाटन के चौलुक्यों (सोलंकियों) ने इस क्षेत्र पर शासन किया; सोलंकियों ने पाटन की रानी की वाव और मोढेरा का सूर्य मंदिर बनवाया, और जैन व्यापारियों और संरक्षकों ने पालीताणा और गिरनार के मंदिर बनवाए। सौराष्ट्र तट पर सोमनाथ पर 1026 में महमूद ग़ज़नवी ने आक्रमण किया, और यह कई बार फिर से बना।\n\nगुजरात सल्तनत ने 1411 में अहमदाबाद बसाया और उसकी मस्जिदें व बावड़ियाँ बनवाईं; मुग़लों ने 1573 में गुजरात लिया, और 18वीं सदी में मराठा आए। सूरत एक बड़ा बंदरगाह बना, जहाँ अंग्रेज़ी ईस्ट इंडिया कंपनी ने 1613 में अपनी पहली कोठियों में से एक बनाई। अंग्रेज़ी शासन में गुजरात का बड़ा हिस्सा सैकड़ों रियासतों में बँटा था। गांधी के साबरमती आश्रम और 1930 की दांडी यात्रा, और सरदार पटेल के 1928 के बारडोली सत्याग्रह ने गुजरात को राष्ट्रीय आंदोलन का केंद्र बनाया। आज़ादी के बाद यह क्षेत्र बॉम्बे राज्य का हिस्सा रहा, जब तक 1960 में गुजरात नहीं बना।",
        "गुजरातमध्ये हडप्पा संस्कृतीची काही सर्वांत महत्त्वाची स्थळे आहेत: गोदी असलेले लोथल आणि जलाशय व नियोजित नगर असलेले कच्छच्या रणातील धोलावीरा, जी इ.स.पू. तिसऱ्या सहस्रकात भरभराटीला आली. जुनागड येथील एका खडकावर अशोकाचे शिलालेख आहेत, आणि त्याच खडकावर पश्चिम क्षत्रप व गुप्त यांचेही लेख आहेत. वल्लभीचे मैत्रक आणि नंतर अणहिलवाड पाटणचे चौलुक्य (सोळंकी) यांनी या प्रदेशावर राज्य केले; सोळंकींनी पाटणची राणी की वाव व मोढेराचे सूर्यमंदिर उभारले, आणि जैन व्यापारी व आश्रयदात्यांनी पालीताणा व गिरनारची मंदिरे बांधली. सौराष्ट्र किनाऱ्यावरील सोमनाथवर 1026 मध्ये महमूद गझनवीने आक्रमण केले, आणि ते अनेकदा पुन्हा उभारले गेले.\n\nगुजरात सल्तनतीने 1411 मध्ये अहमदाबाद वसवले आणि तिथल्या मशिदी व बारवा बांधल्या; मुघलांनी 1573 मध्ये गुजरात घेतले, आणि अठराव्या शतकात मराठे आले. सुरत मोठे बंदर बनले, जिथे इंग्रजी ईस्ट इंडिया कंपनीने 1613 मध्ये आपल्या पहिल्या वखारींपैकी एक उभारली. इंग्रजी अमलात गुजरातचा मोठा भाग शेकडो संस्थानांत विभागलेला होता. गांधींचा साबरमती आश्रम व 1930 ची दांडी यात्रा, आणि सरदार पटेलांचा 1928 चा बारडोली सत्याग्रह यांमुळे गुजरात राष्ट्रीय चळवळीचे केंद्र बनले. स्वातंत्र्यानंतर हा प्रदेश मुंबई राज्याचा भाग होता, 1960 मध्ये गुजरातची निर्मिती होईपर्यंत."),
        conf="Editorial"),
    timeline([
        ev("dholavira", -2600, L("c. 3rd millennium BCE", "लगभग ईसा पूर्व तीसरी सहस्राब्दी", "सुमारे इ.स.पू. तिसरे सहस्रक"), L("Harappan cities of Dholavira and Lothal", "धोलावीरा और लोथल के हड़प्पा नगर", "धोलावीरा व लोथलची हडप्पा नगरे")),
        ev("junagadh", -250, L("3rd century BCE", "ईसा पूर्व तीसरी सदी", "इ.स.पू. तिसरे शतक"), L("Ashoka's rock edicts at Junagadh", "जूनागढ़ में अशोक के शिलालेख", "जुनागड येथे अशोकाचे शिलालेख")),
        ev("ranikivav", 1063, L("11th century", "11वीं सदी", "अकरावे शतक"), L("Rani ki Vav stepwell built at Patan", "पाटन में रानी की वाव बनी", "पाटण येथे राणी की वाव बांधली")),
        ev("ahmedabad", 1411, L("1411", "1411", "1411"), L("Ahmedabad founded by Sultan Ahmad Shah", "सुल्तान अहमद शाह ने अहमदाबाद बसाया", "सुलतान अहमदशहाने अहमदाबाद वसवले")),
        ev("surat", 1613, L("1613", "1613", "1613"), L("English factory at Surat", "सूरत में अंग्रेज़ी कोठी", "सुरत येथे इंग्रजी वखार")),
        ev("bardoli", 1928, L("1928", "1928", "1928"), L("Bardoli satyagraha led by Vallabhbhai Patel", "वल्लभभाई पटेल के नेतृत्व में बारडोली सत्याग्रह", "वल्लभभाई पटेलांच्या नेतृत्वाखाली बारडोली सत्याग्रह")),
        ev("dandi", 1930, L("12 March 1930", "12 मार्च 1930", "12 मार्च 1930"), L("Gandhi begins the Salt March from Sabarmati", "गांधी ने साबरमती से दांडी यात्रा शुरू की", "गांधींनी साबरमतीहून दांडी यात्रा सुरू केली")),
        ev("state", 1960, L("1 May 1960", "1 मई 1960", "1 मे 1960"), L("Gujarat State formed", "गुजरात राज्य का गठन", "गुजरात राज्याची निर्मिती")),
        ev("quake", 2001, L("26 January 2001", "26 जनवरी 2001", "26 जानेवारी 2001"), L("Bhuj earthquake", "भुज भूकंप", "भुज भूकंप")),
        ev("dholaviraWH", 2021, L("2021", "2021", "2021"), L("Dholavira inscribed as a UNESCO World Heritage Site", "धोलावीरा यूनेस्को विश्व धरोहर स्थल घोषित", "धोलावीरा युनेस्को जागतिक वारसा स्थळ घोषित")),
        ev("garba", 2023, L("2023", "2023", "2023"), L("Garba added to UNESCO's intangible heritage list", "गरबा यूनेस्को की अमूर्त धरोहर सूची में शामिल", "गरबा युनेस्कोच्या अमूर्त वारसा यादीत समाविष्ट")),
    ]),
    lst("heritage", [
        it3("champaner", "Champaner-Pavagadh Archaeological Park", "चंपानेर-पावागढ़ पुरातात्विक उद्यान", "चंपानेर-पावागड पुरातत्त्व उद्यान", m=("UNESCO 2004", "यूनेस्को 2004", "युनेस्को 2004"), url=UNESCO, src="unesco-whc"),
        it3("ranikivav", "Rani-ki-Vav, Patan", "रानी की वाव, पाटन", "राणी की वाव, पाटण", m=("UNESCO 2014", "यूनेस्को 2014", "युनेस्को 2014"), url=UNESCO, src="unesco-whc"),
        it3("ahmedabad", "Historic City of Ahmadabad", "ऐतिहासिक नगर अहमदाबाद", "ऐतिहासिक शहर अहमदाबाद", m=("UNESCO 2017", "यूनेस्को 2017", "युनेस्को 2017"), url=UNESCO, src="unesco-whc"),
        it3("dholavira", "Dholavira: a Harappan City", "धोलावीरा: एक हड़प्पा नगर", "धोलावीरा: एक हडप्पा नगर", m=("UNESCO 2021", "यूनेस्को 2021", "युनेस्को 2021"), url=UNESCO, src="unesco-whc"),
        it3("garba", "Garba of Gujarat", "गुजरात का गरबा", "गुजरातचा गरबा", m=("UNESCO intangible heritage (2023)", "यूनेस्को अमूर्त धरोहर (2023)", "युनेस्को अमूर्त वारसा (2023)")),
        it3("modhera", "Sun Temple, Modhera", "सूर्य मंदिर, मोढेरा", "सूर्यमंदिर, मोढेरा", m=("Solanki architecture", "सोलंकी स्थापत्य", "सोळंकी स्थापत्य")),
        it3("lothal", "Lothal", "लोथल", "लोथल", m=("Harappan port", "हड़प्पा बंदरगाह", "हडप्पा बंदर")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("gj mod1 ok")
