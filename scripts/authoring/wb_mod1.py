"""West Bengal modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-WB"
NITI = "https://www.niti.gov.in/sites/default/files/2025-07/Macro-and-Fiscal-Landscape-of-the-State-of-West-Bengal-1.pdf"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
wb = read("regions/IN-WB.json")["metrics"]; ind = read("india.json")["metrics"]
NAME = L("West Bengal", "पश्चिम बंगाल", "पश्चिम बंगाल")

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "West Bengal stretches from the Himalaya at Darjeeling to the Bay of Bengal at the Sundarbans, the largest mangrove forest in the world. It had 9.13 crore people at the 2011 Census — the fourth-largest population among the States — on just 2.7% of India's area, making it one of the most densely populated. Kolkata, the capital and former capital of British India, is the largest city of eastern India; Howrah, Durgapur, Asansol, Siliguri and Haldia are the other main urban and industrial centres.\n\nThe State took shape at the partition of Bengal in 1947, when the eastern districts became East Pakistan (now Bangladesh). Purulia and part of Purnea were added from Bihar in 1956, and the former French enclave of Chandannagar in 1954. Bengali is the official language.",
        "पश्चिम बंगाल दार्जिलिंग में हिमालय से लेकर सुंदरबन में बंगाल की खाड़ी तक फैला है, जो दुनिया का सबसे बड़ा मैंग्रोव वन है। 2011 की जनगणना में यहाँ 9.13 करोड़ लोग थे — राज्यों में चौथी सबसे बड़ी आबादी — और यह भारत के केवल 2.7% क्षेत्रफल पर है, इसलिए यह सबसे घनी आबादी वाले राज्यों में है। राजधानी कोलकाता, जो ब्रिटिश भारत की भी राजधानी रही, पूर्वी भारत का सबसे बड़ा शहर है; हावड़ा, दुर्गापुर, आसनसोल, सिलीगुड़ी और हल्दिया अन्य प्रमुख शहरी और औद्योगिक केंद्र हैं।\n\nराज्य 1947 में बंगाल के विभाजन के साथ बना, जब पूर्वी ज़िले पूर्वी पाकिस्तान (अब बांग्लादेश) बने। 1956 में बिहार से पुरुलिया और पूर्णिया का कुछ हिस्सा जोड़ा गया, और 1954 में पूर्व फ़्रांसीसी बस्ती चंदननगर। बांग्ला राजभाषा है।",
        "पश्चिम बंगाल दार्जिलिंगमधील हिमालयापासून सुंदरबनमधील बंगालच्या उपसागरापर्यंत पसरले आहे — सुंदरबन हे जगातील सर्वांत मोठे खारफुटीचे जंगल आहे. 2011 च्या जनगणनेनुसार इथे 9.13 कोटी लोक होते — राज्यांमध्ये चौथी सर्वांत मोठी लोकसंख्या — आणि तेही भारताच्या केवळ 2.7% क्षेत्रावर, त्यामुळे ते सर्वाधिक दाट लोकवस्तीच्या राज्यांपैकी आहे. राजधानी कोलकाता, जी ब्रिटिश भारताचीही राजधानी होती, हे पूर्व भारतातील सर्वांत मोठे शहर आहे; हावडा, दुर्गापूर, आसनसोल, सिलिगुडी व हल्दिया ही इतर प्रमुख नागरी व औद्योगिक केंद्रे आहेत.\n\n1947 मध्ये बंगालच्या फाळणीसोबत हे राज्य आकाराला आले, जेव्हा पूर्वेकडील जिल्हे पूर्व पाकिस्तान (आता बांगलादेश) बनले. 1956 मध्ये बिहारमधून पुरुलिया व पूर्णियाचा काही भाग, आणि 1954 मध्ये पूर्वीची फ्रेंच वसाहत चंदननगर जोडली गेली. बांगला ही राजभाषा आहे."),
        sources=["census", "niti"], conf="Editorial"),
    prose("intro-unique", L(
        "Bengal has given India much of its modern intellectual and artistic life. The Bengal Renaissance of the 19th century — Raja Ram Mohan Roy, Ishwar Chandra Vidyasagar, Bankim Chandra Chattopadhyay, Ramakrishna and Vivekananda — and later Rabindranath Tagore, Asia's first Nobel laureate, Satyajit Ray and Subhas Chandra Bose all came from here. Durga Puja in Kolkata, recognised by UNESCO, transforms the city every autumn. The State also holds the tea gardens and toy train of Darjeeling, the Royal Bengal tigers of the Sundarbans, the terracotta temples of Bishnupur and Tagore's Santiniketan.",
        "बंगाल ने भारत को उसके आधुनिक बौद्धिक और कलात्मक जीवन का बड़ा हिस्सा दिया है। 19वीं सदी का बंगाल पुनर्जागरण — राजा राममोहन राय, ईश्वरचंद्र विद्यासागर, बंकिमचंद्र चट्टोपाध्याय, रामकृष्ण और विवेकानंद — और बाद में एशिया के पहले नोबेल विजेता रवींद्रनाथ टैगोर, सत्यजीत राय और सुभाष चंद्र बोस, सभी यहीं से थे। यूनेस्को से मान्यता प्राप्त कोलकाता की दुर्गा पूजा हर शरद ऋतु में शहर का रूप बदल देती है। राज्य में दार्जिलिंग के चाय बागान और टॉय ट्रेन, सुंदरबन के रॉयल बंगाल टाइगर, बिष्णुपुर के टेराकोटा मंदिर और टैगोर का शांतिनिकेतन भी हैं।",
        "बंगालने भारताला त्याच्या आधुनिक बौद्धिक व कलात्मक जीवनाचा मोठा भाग दिला आहे. एकोणिसाव्या शतकातील बंगाल प्रबोधन — राजा राममोहन रॉय, ईश्वरचंद्र विद्यासागर, बंकिमचंद्र चट्टोपाध्याय, रामकृष्ण व विवेकानंद — आणि नंतर आशियातील पहिले नोबेल विजेते रवींद्रनाथ टागोर, सत्यजित राय व सुभाषचंद्र बोस हे सर्व इथलेच. युनेस्कोची मान्यता असलेली कोलकात्याची दुर्गापूजा दर शरद ऋतूत शहराचे रूप पालटते. राज्यात दार्जिलिंगचे चहामळे व टॉय ट्रेन, सुंदरबनचे रॉयल बंगाल वाघ, बिष्णुपूरची टेराकोटा मंदिरे आणि टागोरांचे शांतिनिकेतनही आहे."),
        title=L("What makes West Bengal unique?", "पश्चिम बंगाल को ख़ास क्या बनाता है?", "पश्चिम बंगालचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed", "गठन", "निर्मिती"), L("15 August 1947, at the partition of Bengal", "15 अगस्त 1947, बंगाल विभाजन के समय", "15 ऑगस्ट 1947, बंगालच्या फाळणीसोबत")],
           [L("Districts", "ज़िले", "जिल्हे"), "23"],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Bengali; Nepali in the Darjeeling hills, with other languages in specified areas", "बांग्ला; दार्जिलिंग पहाड़ियों में नेपाली, और निर्दिष्ट क्षेत्रों में अन्य भाषाएँ", "बांगला; दार्जिलिंग डोंगराळ भागात नेपाळी, आणि निर्दिष्ट क्षेत्रांत इतर भाषा")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Calcutta (1862), with circuit benches at Jalpaiguri and Port Blair", "कलकत्ता (1862), जलपाईगुड़ी और पोर्ट ब्लेयर में सर्किट बेंच", "कलकत्ता (1862), जलपाईगुडी व पोर्ट ब्लेअर येथे सर्किट खंडपीठ")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-WB / WB"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be linked to the State's notifications in review.", "संपादकीय; समीक्षा में राज्य की अधिसूचनाओं से जोड़ा जाएगा।", "संपादकीय; तपासणीत राज्याच्या अधिसूचनांशी जोडले जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "West Bengal is long and narrow, running about 600 km from north to south. In the far north the Darjeeling and Kalimpong hills rise into the Himalaya, with Sandakphu on the Nepal border the State's highest point. Below them lie the Terai and the Dooars, a belt of forest, tea gardens and rivers at the foot of the hills. Most of the State is the flat, fertile Gangetic delta — among the most intensively farmed land in the world — crossed by the Bhagirathi–Hooghly, the main distributary of the Ganga, on which Kolkata stands. The western districts of Purulia, Bankura and Paschim Medinipur rise onto the red, rolling edge of the Chota Nagpur plateau. In the south, the Sundarbans delta of tidal creeks and mangrove islands meets the Bay of Bengal.\n\nThe Ganga enters the State at Farakka, where a barrage diverts water into the Hooghly before the main river flows on into Bangladesh as the Padma. The Teesta, Mahananda, Damodar, Rupnarayan and Subarnarekha are other major rivers; the Damodar Valley dams were built to control floods.",
        "पश्चिम बंगाल लंबा और संकरा है, जो उत्तर से दक्षिण लगभग 600 किमी फैला है। सुदूर उत्तर में दार्जिलिंग और कालिम्पोंग की पहाड़ियाँ हिमालय में उठती हैं, और नेपाल सीमा पर संदकफू राज्य का सबसे ऊँचा स्थान है। इनके नीचे तराई और डुआर्स हैं — पहाड़ियों की तलहटी में वन, चाय बागानों और नदियों की पट्टी। राज्य का अधिकांश भाग समतल, उपजाऊ गंगा डेल्टा है — दुनिया की सबसे सघन खेती वाली भूमि में से — जिसे गंगा की मुख्य वितरिका भागीरथी–हुगली पार करती है, जिसके किनारे कोलकाता बसा है। पश्चिम के पुरुलिया, बाँकुड़ा और पश्चिम मेदिनीपुर ज़िले छोटा नागपुर पठार के लाल, लहरदार किनारे पर हैं। दक्षिण में ज्वारीय खाड़ियों और मैंग्रोव द्वीपों वाला सुंदरबन डेल्टा बंगाल की खाड़ी से मिलता है।\n\nगंगा फ़रक्का में राज्य में प्रवेश करती है, जहाँ एक बराज पानी को हुगली में मोड़ता है और मुख्य नदी आगे पद्मा के रूप में बांग्लादेश जाती है। तीस्ता, महानंदा, दामोदर, रूपनारायण और सुवर्णरेखा अन्य बड़ी नदियाँ हैं; बाढ़ नियंत्रण के लिए दामोदर घाटी के बाँध बनाए गए।",
        "पश्चिम बंगाल लांब व अरुंद असून उत्तर-दक्षिण सुमारे 600 किमी पसरले आहे. अगदी उत्तरेला दार्जिलिंग व कालिम्पोंगचे डोंगर हिमालयात उंचावतात, आणि नेपाळ सीमेवरील संदकफू हे राज्यातील सर्वोच्च ठिकाण आहे. त्यांच्या खाली तराई व डुआर्स आहेत — डोंगरपायथ्याशी जंगल, चहामळे व नद्यांचा पट्टा. राज्याचा बहुतांश भाग सपाट, सुपीक गंगा त्रिभुज प्रदेश आहे — जगातील सर्वाधिक सघन शेती असलेल्या भूमीपैकी — ज्यातून गंगेची मुख्य उपशाखा भागीरथी–हुगळी वाहते, जिच्या काठावर कोलकाता वसले आहे. पश्चिमेकडील पुरुलिया, बांकुडा व पश्चिम मेदिनीपूर जिल्हे छोटा नागपूर पठाराच्या तांबड्या, लहरी कडेवर आहेत. दक्षिणेला भरती-ओहोटीच्या खाड्या व खारफुटी बेटांचा सुंदरबन त्रिभुज प्रदेश बंगालच्या उपसागराला मिळतो.\n\nगंगा फरक्का येथे राज्यात प्रवेश करते, जिथे एक बंधारा पाणी हुगळीत वळवतो आणि मुख्य नदी पुढे पद्मा म्हणून बांगलादेशात जाते. तिस्ता, महानंदा, दामोदर, रूपनारायण व सुवर्णरेखा या इतर मोठ्या नद्या आहेत; पूरनियंत्रणासाठी दामोदर खोऱ्यातील धरणे बांधली गेली."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), wb["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("sk", "Sikkim (north)", "सिक्किम (उत्तर)", "सिक्कीम (उत्तर)"), it3("np", "Nepal (north-west)", "नेपाल (उत्तर-पश्चिम)", "नेपाळ (वायव्य)"),
        it3("bt", "Bhutan (north-east)", "भूटान (उत्तर-पूर्व)", "भूतान (ईशान्य)"), it3("as", "Assam (north-east)", "असम (उत्तर-पूर्व)", "आसाम (ईशान्य)"),
        it3("bd", "Bangladesh (east)", "बांग्लादेश (पूर्व)", "बांगलादेश (पूर्व)"), it3("br", "Bihar (west)", "बिहार (पश्चिम)", "बिहार (पश्चिम)"),
        it3("jh", "Jharkhand (west)", "झारखंड (पश्चिम)", "झारखंड (पश्चिम)"), it3("or", "Odisha (south-west)", "ओडिशा (दक्षिण-पश्चिम)", "ओडिशा (नैर्ऋत्य)"),
        it3("sea", "Bay of Bengal (south)", "बंगाल की खाड़ी (दक्षिण)", "बंगालचा उपसागर (दक्षिण)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("hooghly", "Bhagirathi–Hooghly", "भागीरथी–हुगली", "भागीरथी–हुगळी", d=("Ganga distributary flowing past Kolkata and Howrah to the sea.", "गंगा की वितरिका, जो कोलकाता और हावड़ा से होकर समुद्र तक बहती है।", "गंगेची उपशाखा, कोलकाता व हावड्यावरून समुद्रापर्यंत वाहते.")),
        it3("teesta", "Teesta", "तीस्ता", "तिस्ता", d=("Himalayan river of the north, flowing on into Bangladesh.", "उत्तर की हिमालयी नदी, जो आगे बांग्लादेश जाती है।", "उत्तरेकडील हिमालयीन नदी, पुढे बांगलादेशात जाते.")),
        it3("damodar", "Damodar", "दामोदर", "दामोदर", d=("Once 'the sorrow of Bengal'; dams of the Damodar Valley Corporation.", "कभी 'बंगाल का शोक'; दामोदर घाटी निगम के बाँध।", "एकेकाळी 'बंगालचे दुःख'; दामोदर खोरे महामंडळाची धरणे.")),
        it3("mahananda", "Mahananda", "महानंदा", "महानंदा", d=("Flows past Siliguri and Malda.", "सिलीगुड़ी और मालदा से होकर बहती है।", "सिलिगुडी व मालदावरून वाहते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point (Sandakphu) — official elevation", "सर्वोच्च बिंदु (संदकफू) — आधिकारिक ऊँचाई", "सर्वोच्च शिखर (संदकफू) — अधिकृत उंची"), "survey-of-india", "Survey of India or the State gazetteer."),
        (L("Coastline length (official)", "तटरेखा की लंबाई (आधिकारिक)", "किनारपट्टीची लांबी (अधिकृत)"), "survey-of-india", "Survey of India / NHO figure."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Most of West Bengal has a hot, humid tropical climate. Summers (March–May) are hot and sticky, broken by violent pre-monsoon thunderstorms called kalbaishakhi (nor'westers). The south-west monsoon, from June to September, brings heavy rain — heaviest in the Dooars and the sub-Himalayan north. Winters (December–February) are mild and pleasant in Kolkata and the plains, and cold in Darjeeling, where snow occasionally falls. Cyclones from the Bay of Bengal strike the coast and the Sundarbans before and after the monsoon.",
        "पश्चिम बंगाल के अधिकांश भाग में गर्म, आर्द्र उष्णकटिबंधीय जलवायु है। गर्मियाँ (मार्च–मई) गर्म और उमस भरी होती हैं, जिन्हें कालबैसाखी (नॉरवेस्टर) नामक तेज़ मानसून-पूर्व आँधी-तूफ़ान तोड़ते हैं। जून से सितंबर तक दक्षिण-पश्चिम मानसून भारी वर्षा लाता है — सबसे अधिक डुआर्स और उप-हिमालयी उत्तर में। सर्दियाँ (दिसंबर–फ़रवरी) कोलकाता और मैदानों में सुहावनी होती हैं, और दार्जिलिंग में ठंडी, जहाँ कभी-कभी बर्फ़ भी गिरती है। बंगाल की खाड़ी के चक्रवात मानसून से पहले और बाद में तट और सुंदरबन से टकराते हैं।",
        "पश्चिम बंगालच्या बहुतांश भागात उष्ण, दमट उष्णकटिबंधीय हवामान आहे. उन्हाळा (मार्च–मे) उष्ण व चिकट असतो, आणि त्यात कालबैसाखी (नॉरवेस्टर) नावाची जोरदार मान्सूनपूर्व वादळे येतात. जून ते सप्टेंबर नैर्ऋत्य मान्सून मुसळधार पाऊस आणतो — सर्वाधिक डुआर्स व उप-हिमालयीन उत्तरेत. हिवाळा (डिसेंबर–फेब्रुवारी) कोलकाता व मैदानी भागात सुखद, तर दार्जिलिंगमध्ये थंड असतो, जिथे कधीकधी बर्फही पडतो. बंगालच्या उपसागरातील चक्रीवादळे मान्सूनपूर्वी व नंतर किनारपट्टी व सुंदरबनला धडकतात."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Kolkata", "कोलकाता", "कोलकाता"), "lat": 22.5726, "lon": 88.3639},
        {"name": L("Darjeeling", "दार्जिलिंग", "दार्जिलिंग"), "lat": 27.0410, "lon": 88.2663},
        {"name": L("Siliguri", "सिलीगुड़ी", "सिलिगुडी"), "lat": 26.7271, "lon": 88.3953},
        {"name": L("Digha", "दीघा", "दिघा"), "lat": 21.6266, "lon": 87.5074},
    ]},
    lst("best", [
        it3("winter", "October to February", "अक्टूबर से फ़रवरी", "ऑक्टोबर ते फेब्रुवारी", d=("Best for Kolkata and the Sundarbans; Durga Puja in October; clear Himalayan views from Darjeeling.", "कोलकाता और सुंदरबन के लिए सबसे अच्छा; अक्टूबर में दुर्गा पूजा; दार्जिलिंग से हिमालय के साफ़ दृश्य।", "कोलकाता व सुंदरबनसाठी उत्तम; ऑक्टोबरमध्ये दुर्गापूजा; दार्जिलिंगहून हिमालयाचे स्वच्छ दर्शन.")),
        it3("spring", "March to May", "मार्च से मई", "मार्च ते मे", d=("Hot in the plains; a good time for the Darjeeling hills.", "मैदानों में गर्मी; दार्जिलिंग की पहाड़ियों के लिए अच्छा समय।", "मैदानी भागात उष्ण; दार्जिलिंगच्या डोंगरांसाठी चांगला काळ.")),
        it3("monsoon", "June to September", "जून से सितंबर", "जून ते सप्टेंबर", d=("Heavy rain; landslides on hill roads; forests of the Dooars close mid-June to mid-September.", "भारी वर्षा; पहाड़ी सड़कों पर भूस्खलन; डुआर्स के वन मध्य-जून से मध्य-सितंबर तक बंद।", "मुसळधार पाऊस; डोंगरी रस्त्यांवर दरडी; डुआर्सची जंगले जूनच्या मध्यापासून सप्टेंबरच्या मध्यापर्यंत बंद.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (State and sub-divisions)", "सामान्य वार्षिक वर्षा (राज्य और उप-मंडल)", "सरासरी वार्षिक पाऊस (राज्य व उपविभाग)"), "imd", "IMD rainfall statistics for Gangetic West Bengal and Sub-Himalayan West Bengal & Sikkim."),
        (L("Cyclone landfalls by year", "वर्षवार चक्रवात का तट पर पहुँचना", "वर्षनिहाय चक्रीवादळांचे किनाऱ्यावर येणे"), "imd", "IMD cyclone e-Atlas."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Kolkata runs on conversation — adda over tea in roadside stalls and coffee houses, arguments about football, film and politics, and the second-hand bookstalls of College Street. Yellow taxis and hand-pulled rickshaws share old streets with the metro, while the riverfront ghats and the Victoria Memorial lawns fill up in the evenings. Food is central: fish and rice, sweets from the neighbourhood mishti shop, and street rolls and phuchka. Each autumn, Durga Puja turns the city into a vast open-air exhibition of themed pandals. Beyond the capital, life varies from the tea gardens and Buddhist monasteries of the hills to the paddy fields and village fairs of the delta and the Baul singers of Birbhum.",
        "कोलकाता बातचीत पर चलता है — सड़क किनारे की चाय की दुकानों और कॉफ़ी हाउस में अड्डा, फ़ुटबॉल, फ़िल्म और राजनीति पर बहस, और कॉलेज स्ट्रीट की पुरानी किताबों की दुकानें। पीली टैक्सियाँ और हाथ-रिक्शा पुरानी सड़कों पर मेट्रो के साथ चलते हैं, और शाम को नदी किनारे के घाट और विक्टोरिया मेमोरियल के लॉन भर जाते हैं। भोजन केंद्र में है: माछ-भात, मोहल्ले की मिष्टि की दुकान की मिठाइयाँ, और सड़क के रोल और फुचका। हर शरद ऋतु में दुर्गा पूजा शहर को थीम वाले पंडालों की विशाल खुली प्रदर्शनी में बदल देती है। राजधानी से बाहर, जीवन पहाड़ियों के चाय बागानों और बौद्ध मठों से लेकर डेल्टा के धान के खेतों और गाँव के मेलों और बीरभूम के बाउल गायकों तक बदलता है।",
        "कोलकाता गप्पांवर चालते — रस्त्याकडेच्या चहाच्या टपऱ्यांवर व कॉफी हाउसमध्ये अड्डा, फुटबॉल, चित्रपट व राजकारणावर वाद, आणि कॉलेज स्ट्रीटवरील जुन्या पुस्तकांची दुकाने. पिवळ्या टॅक्सी व हातरिक्षा जुन्या रस्त्यांवर मेट्रोसोबत धावतात, आणि संध्याकाळी नदीकाठचे घाट व व्हिक्टोरिया मेमोरियलची हिरवळ गजबजते. खाद्यपदार्थ केंद्रस्थानी आहेत: मासे-भात, शेजारच्या मिष्टी दुकानातील मिठाया, आणि रस्त्यावरचे रोल व फुचका. दर शरद ऋतूत दुर्गापूजा शहराला संकल्पनाधारित मंडपांच्या प्रचंड खुल्या प्रदर्शनात बदलते. राजधानीबाहेर जीवन डोंगरांतील चहामळे व बौद्ध मठांपासून त्रिभुज प्रदेशातील भातखाचरे व गावजत्रा आणि बीरभूमच्या बाऊल गायकांपर्यंत बदलते."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "At the 2011 Census West Bengal had 9.13 crore people, with a density of about 1,028 per km² — among the highest of any State. The sex ratio was 950 women per 1,000 men, above the national 943, and the child sex ratio was 956. Literacy was 76.3%, above the national 73.0%. Scheduled Castes made up 23.5% of the population, one of the highest shares in India, and Scheduled Tribes 5.8%, mainly Santal, Oraon and Munda communities in the west and north.\n\nBengali is spoken by most people. Nepali is the main language of the Darjeeling and Kalimpong hills; Hindi and Urdu are widely spoken in Kolkata and the industrial belt; and Santali (written in Ol Chiki), Kurmali and other tribal languages are spoken in the western districts.",
        "2011 की जनगणना में पश्चिम बंगाल की जनसंख्या 9.13 करोड़ थी, और घनत्व लगभग 1,028 प्रति वर्ग किमी — किसी भी राज्य में सबसे अधिक में से। लिंगानुपात प्रति 1,000 पुरुषों पर 950 महिलाएँ था, जो राष्ट्रीय 943 से अधिक है, और शिशु लिंगानुपात 956 था। साक्षरता 76.3% थी, जो राष्ट्रीय 73.0% से अधिक है। अनुसूचित जातियाँ जनसंख्या का 23.5% थीं, जो भारत में सबसे अधिक हिस्सों में है, और अनुसूचित जनजातियाँ 5.8%, मुख्यतः पश्चिम और उत्तर के संथाल, उराँव और मुंडा समुदाय।\n\nअधिकांश लोग बांग्ला बोलते हैं। दार्जिलिंग और कालिम्पोंग पहाड़ियों की मुख्य भाषा नेपाली है; कोलकाता और औद्योगिक पट्टी में हिंदी और उर्दू व्यापक रूप से बोली जाती हैं; और पश्चिमी ज़िलों में संथाली (ओल चिकी लिपि में), कुड़मालि और अन्य आदिवासी भाषाएँ बोली जाती हैं।",
        "2011 च्या जनगणनेनुसार पश्चिम बंगालची लोकसंख्या 9.13 कोटी होती, आणि घनता सुमारे 1,028 प्रति चौ.किमी — कोणत्याही राज्यातील सर्वाधिकांपैकी. दर 1,000 पुरुषांमागे 950 स्त्रिया होत्या — राष्ट्रीय 943 पेक्षा जास्त — आणि बाल लिंग गुणोत्तर 956 होते. साक्षरता 76.3% होती, राष्ट्रीय 73.0% पेक्षा जास्त. अनुसूचित जाती लोकसंख्येच्या 23.5% होत्या — भारतातील सर्वाधिक वाट्यांपैकी — आणि अनुसूचित जमाती 5.8%, मुख्यतः पश्चिम व उत्तरेकडील संथाल, ओराँव व मुंडा समुदाय.\n\nबहुसंख्य लोक बांगला बोलतात. दार्जिलिंग व कालिम्पोंगच्या डोंगराळ भागाची मुख्य भाषा नेपाळी आहे; कोलकाता व औद्योगिक पट्ट्यात हिंदी व उर्दू मोठ्या प्रमाणावर बोलल्या जातात; आणि पश्चिमेकडील जिल्ह्यांत संथाली (ओल चिकी लिपीत), कुडमाली व इतर आदिवासी भाषा बोलल्या जातात."),
        sources=["census", "es-india", "niti"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), wb["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), wb["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"]),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), wb["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(960, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), wb["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), wb["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(23.5, "%", "2011", "census", "niti", NITI, note="NITI Aayog, 'Macro and Fiscal Landscape of the State of West Bengal' (2025), citing Census 2011; the Delhi Planning Department's table gives 214.63 lakh people."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(5.8, "%", "2011", "census", "niti", NITI, note="Same report; 52.97 lakh people (Delhi Planning Department table 17.2)."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("bn", "Bengali", "बांग्ला", "बांगला", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("ne", "Nepali", "नेपाली", "नेपाळी", m=("Darjeeling and Kalimpong hills", "दार्जिलिंग और कालिम्पोंग पहाड़ियाँ", "दार्जिलिंग व कालिम्पोंग डोंगर")),
        it3("hi", "Hindi", "हिंदी", "हिंदी"), it3("ur", "Urdu", "उर्दू", "उर्दू"),
        it3("sat", "Santali", "संथाली", "संथाली", m=("Western districts", "पश्चिमी ज़िले", "पश्चिमेकडील जिल्हे")),
        it3("kyw", "Kurmali", "कुड़मालि", "कुडमाली"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Final Population Totals for West Bengal."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Bengal's early kingdoms included Vanga and Gauda; the Mauryas and Guptas ruled parts of it, and in the 7th century Shashanka made Gauda a power. The Pala dynasty (8th–12th centuries) patronised Buddhism and the great monastery-universities, and the Senas followed. From the 13th century Bengal was ruled by sultans, and from the late 16th century by the Mughals; Murshidabad became the capital of the Nawabs of Bengal. The Battle of Plassey in 1757 gave the East India Company control of Bengal, and Calcutta (Kolkata) became the capital of British India until 1911.\n\nThe 19th-century Bengal Renaissance brought social reform, new literature and education. The first partition of Bengal in 1905 sparked the Swadeshi movement and was reversed in 1911. The Bengal famine of 1943 killed millions. At Independence in 1947 Bengal was partitioned again, with West Bengal joining India; millions of refugees crossed the new border then and in 1971. Since then the State has been governed by the Congress, a Left Front government for 34 years (1977–2011), the Trinamool Congress (2011–2026) and, from May 2026, the BJP.",
        "बंगाल के प्रारंभिक राज्यों में वंग और गौड़ थे; मौर्यों और गुप्तों ने इसके हिस्सों पर शासन किया, और सातवीं सदी में शशांक ने गौड़ को शक्ति बनाया। पाल वंश (8वीं–12वीं सदी) ने बौद्ध धर्म और बड़े महाविहार-विश्वविद्यालयों को संरक्षण दिया, और उसके बाद सेन आए। 13वीं सदी से बंगाल पर सुल्तानों का, और 16वीं सदी के अंत से मुग़लों का शासन रहा; मुर्शिदाबाद बंगाल के नवाबों की राजधानी बना। 1757 के प्लासी के युद्ध से ईस्ट इंडिया कंपनी को बंगाल पर नियंत्रण मिला, और कलकत्ता (कोलकाता) 1911 तक ब्रिटिश भारत की राजधानी रहा।\n\n19वीं सदी के बंगाल पुनर्जागरण से सामाजिक सुधार, नया साहित्य और शिक्षा आई। 1905 के पहले बंगाल विभाजन से स्वदेशी आंदोलन भड़का और 1911 में विभाजन रद्द हुआ। 1943 के बंगाल अकाल में लाखों लोग मारे गए। 1947 में आज़ादी के समय बंगाल का फिर विभाजन हुआ, और पश्चिम बंगाल भारत में शामिल हुआ; तब और 1971 में लाखों शरणार्थी नई सीमा पार कर आए। तब से राज्य में कांग्रेस, 34 वर्ष तक (1977–2011) वाम मोर्चा, तृणमूल कांग्रेस (2011–2026) और मई 2026 से भाजपा की सरकार रही है।",
        "बंगालच्या प्रारंभीच्या राज्यांत वंग व गौड होते; मौर्य व गुप्त यांनी त्याच्या काही भागांवर राज्य केले, आणि सातव्या शतकात शशांकाने गौडला सत्ताकेंद्र बनवले. पाल घराण्याने (आठवे–बारावे शतक) बौद्ध धर्म व मोठ्या महाविहार-विद्यापीठांना आश्रय दिला, आणि त्यानंतर सेन आले. तेराव्या शतकापासून बंगालवर सुलतानांचे, आणि सोळाव्या शतकाच्या अखेरीपासून मुघलांचे राज्य होते; मुर्शिदाबाद ही बंगालच्या नवाबांची राजधानी बनली. 1757 च्या प्लासीच्या लढाईने ईस्ट इंडिया कंपनीला बंगालचे नियंत्रण मिळाले, आणि कलकत्ता (कोलकाता) 1911 पर्यंत ब्रिटिश भारताची राजधानी होते.\n\nएकोणिसाव्या शतकातील बंगाल प्रबोधनाने सामाजिक सुधारणा, नवे साहित्य व शिक्षण आणले. 1905 च्या पहिल्या बंगाल फाळणीने स्वदेशी चळवळ पेटली आणि 1911 मध्ये फाळणी रद्द झाली. 1943 च्या बंगालच्या दुष्काळात लाखो लोक मरण पावले. 1947 मध्ये स्वातंत्र्याच्या वेळी बंगालची पुन्हा फाळणी झाली आणि पश्चिम बंगाल भारतात सामील झाले; तेव्हा व 1971 मध्ये लाखो निर्वासितांनी नवी सीमा ओलांडली. तेव्हापासून राज्यात काँग्रेस, 34 वर्षे (1977–2011) डावी आघाडी, तृणमूल काँग्रेस (2011–2026) आणि मे 2026 पासून भाजपचे सरकार राहिले आहे."),
        conf="Editorial"),
    timeline([
        ev("pala", 750, L("c. 750", "लगभग 750", "सुमारे 750"), L("Pala dynasty founded", "पाल वंश की स्थापना", "पाल घराण्याची स्थापना")),
        ev("plassey", 1757, L("23 June 1757", "23 जून 1757", "23 जून 1757"), L("Battle of Plassey", "प्लासी का युद्ध", "प्लासीची लढाई")),
        ev("capital", 1772, L("1772–1911", "1772–1911", "1772–1911"), L("Calcutta the capital of British India", "कलकत्ता ब्रिटिश भारत की राजधानी", "कलकत्ता ब्रिटिश भारताची राजधानी")),
        ev("partition1905", 1905, L("1905", "1905", "1905"), L("First partition of Bengal; Swadeshi movement", "बंगाल का पहला विभाजन; स्वदेशी आंदोलन", "बंगालची पहिली फाळणी; स्वदेशी चळवळ")),
        ev("nobel", 1913, L("1913", "1913", "1913"), L("Rabindranath Tagore awarded the Nobel Prize in Literature", "रवींद्रनाथ टैगोर को साहित्य का नोबेल पुरस्कार", "रवींद्रनाथ टागोरांना साहित्याचे नोबेल पारितोषिक")),
        ev("famine", 1943, L("1943", "1943", "1943"), L("Bengal famine", "बंगाल का अकाल", "बंगालचा दुष्काळ")),
        ev("partition1947", 1947, L("15 August 1947", "15 अगस्त 1947", "15 ऑगस्ट 1947"), L("Partition; West Bengal becomes part of India", "विभाजन; पश्चिम बंगाल भारत का हिस्सा बना", "फाळणी; पश्चिम बंगाल भारताचा भाग")),
        ev("leftfront", 1977, L("1977", "1977", "1977"), L("Left Front government begins (to 2011)", "वाम मोर्चा सरकार शुरू (2011 तक)", "डाव्या आघाडीचे सरकार सुरू (2011 पर्यंत)")),
        ev("santiniketan", 2023, L("2023", "2023", "2023"), L("Santiniketan inscribed as a UNESCO World Heritage Site", "शांतिनिकेतन यूनेस्को विश्व धरोहर स्थल घोषित", "शांतिनिकेतन युनेस्को जागतिक वारसा स्थळ घोषित")),
        ev("election2026", 2026, L("May 2026", "मई 2026", "मे 2026"), L("Assembly election; new government sworn in on 9 May", "विधानसभा चुनाव; 9 मई को नई सरकार ने शपथ ली", "विधानसभा निवडणूक; 9 मे रोजी नव्या सरकारचा शपथविधी")),
    ]),
    lst("heritage", [
        it3("sundarbans", "Sundarbans National Park", "सुंदरबन राष्ट्रीय उद्यान", "सुंदरबन राष्ट्रीय उद्यान", m=("UNESCO 1987", "यूनेस्को 1987", "युनेस्को 1987"), url=UNESCO, src="unesco-whc"),
        it3("dhr", "Darjeeling Himalayan Railway (Mountain Railways of India)", "दार्जिलिंग हिमालयन रेलवे (भारत की पर्वतीय रेलें)", "दार्जिलिंग हिमालयन रेल्वे (भारतातील पर्वतीय रेल्वे)", m=("UNESCO 1999", "यूनेस्को 1999", "युनेस्को 1999"), url=UNESCO, src="unesco-whc"),
        it3("santiniketan", "Santiniketan", "शांतिनिकेतन", "शांतिनिकेतन", m=("UNESCO 2023", "यूनेस्को 2023", "युनेस्को 2023"), url=UNESCO, src="unesco-whc"),
        it3("durgapuja", "Durga Puja in Kolkata", "कोलकाता की दुर्गा पूजा", "कोलकात्याची दुर्गापूजा", m=("UNESCO intangible heritage (2021)", "यूनेस्को अमूर्त धरोहर (2021)", "युनेस्को अमूर्त वारसा (2021)")),
        it3("bishnupur", "Terracotta temples of Bishnupur", "बिष्णुपुर के टेराकोटा मंदिर", "बिष्णुपूरची टेराकोटा मंदिरे", m=("Malla period", "मल्ल काल", "मल्ल काळ")),
        it3("victoria", "Victoria Memorial, Kolkata", "विक्टोरिया मेमोरियल, कोलकाता", "व्हिक्टोरिया मेमोरियल, कोलकाता", m=("Colonial-era museum", "औपनिवेशिक काल का संग्रहालय", "वसाहतकालीन संग्रहालय")),
        it3("murshidabad", "Murshidabad", "मुर्शिदाबाद", "मुर्शिदाबाद", m=("Nawabi capital", "नवाबी राजधानी", "नवाबी राजधानी")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("wb mod1 ok")
