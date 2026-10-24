"""Haryana modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-HR"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
HANSI = "https://www.theweek.in/wire-updates/national/2025/12/17/des102-hr-new-district-cabinet.html"
hr = read("regions/IN-HR.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Haryana lies in north-western India and wraps around the national capital, Delhi, on three sides. It borders Punjab and Himachal Pradesh to the north, Rajasthan to the south-west and Uttar Pradesh to the east across the Yamuna. Most of the State is a flat alluvial plain between the Yamuna and the Ghaggar, with the Shivalik hills in the north-east and the worn ridges of the Aravallis in the south. It had 2.54 crore people at the 2011 Census. Chandigarh, a Union Territory, is the shared capital of Haryana and Punjab; Faridabad, Gurugram, Panipat, Ambala, Rohtak, Hisar and Karnal are the major cities.\n\nThe State was formed on 1 November 1966, when the Punjab Reorganisation Act separated the Hindi-speaking south-east of Punjab. Hindi is the official language, and Punjabi is the second language.",
        "हरियाणा उत्तर-पश्चिमी भारत में है और राष्ट्रीय राजधानी दिल्ली को तीन ओर से घेरता है। इसके उत्तर में पंजाब और हिमाचल प्रदेश, दक्षिण-पश्चिम में राजस्थान और पूर्व में यमुना के पार उत्तर प्रदेश है। राज्य का अधिकांश भाग यमुना और घग्गर के बीच का समतल जलोढ़ मैदान है, उत्तर-पूर्व में शिवालिक की पहाड़ियाँ हैं और दक्षिण में अरावली की घिसी हुई पहाड़ियाँ। 2011 की जनगणना में इसकी जनसंख्या 2.54 करोड़ थी। केंद्र शासित प्रदेश चंडीगढ़ हरियाणा और पंजाब की साझा राजधानी है; फ़रीदाबाद, गुरुग्राम, पानीपत, अंबाला, रोहतक, हिसार और करनाल प्रमुख शहर हैं।\n\nराज्य 1 नवंबर 1966 को बना, जब पंजाब पुनर्गठन अधिनियम ने पंजाब के हिंदी-भाषी दक्षिण-पूर्वी भाग को अलग किया। हिंदी राजभाषा है और पंजाबी द्वितीय भाषा।",
        "हरियाणा वायव्य भारतात असून राष्ट्रीय राजधानी दिल्लीला तीन बाजूंनी वेढतो. त्याच्या उत्तरेला पंजाब व हिमाचल प्रदेश, नैर्ऋत्येला राजस्थान आणि पूर्वेला यमुनेपलीकडे उत्तर प्रदेश आहे. राज्याचा बहुतांश भाग यमुना व घग्गरदरम्यानचे सपाट गाळाचे मैदान आहे; ईशान्येला शिवालिकच्या टेकड्या आणि दक्षिणेला अरवलीच्या झिजलेल्या टेकड्या आहेत. 2011 च्या जनगणनेनुसार त्याची लोकसंख्या 2.54 कोटी होती. केंद्रशासित प्रदेश चंदीगड ही हरियाणा व पंजाबची सामायिक राजधानी आहे; फरिदाबाद, गुरुग्राम, पानिपत, अंबाला, रोहतक, हिसार व कर्नाल ही प्रमुख शहरे आहेत.\n\nपंजाब पुनर्रचना कायद्याने पंजाबचा हिंदीभाषक आग्नेय भाग वेगळा केल्यावर 1 नोव्हेंबर 1966 रोजी राज्याची निर्मिती झाली. हिंदी ही राजभाषा आहे आणि पंजाबी ही द्वितीय भाषा."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Haryana is a land of farms, wrestlers and fast-growing cities. Its fields of wheat, rice and mustard, and its Murrah buffaloes, make it one of India's most productive farm States, while Gurugram has become a corporate and technology hub and the Faridabad–Gurugram–Manesar belt is a major centre of the car and component industry. Kurukshetra, the battlefield of the Mahabharata where the Bhagavad Gita is said to have been spoken, and Panipat, site of three decisive battles, give it a deep history; Rakhigarhi in Hisar district is one of the largest Harappan sites known. Haryana's village akharas have produced many of India's Olympic wrestlers and boxers, and Neeraj Chopra of Panipat won India's first Olympic gold in athletics.",
        "हरियाणा खेतों, पहलवानों और तेज़ी से बढ़ते शहरों की भूमि है। गेहूँ, धान और सरसों के खेत और मुर्रा भैंसें इसे भारत के सबसे उत्पादक कृषि राज्यों में शामिल करती हैं, जबकि गुरुग्राम एक कॉर्पोरेट और प्रौद्योगिकी केंद्र बन गया है और फ़रीदाबाद–गुरुग्राम–मानेसर पट्टी कार और कलपुर्ज़ा उद्योग का बड़ा केंद्र है। महाभारत की युद्धभूमि कुरुक्षेत्र, जहाँ भगवद्गीता का उपदेश दिया गया माना जाता है, और तीन निर्णायक युद्धों का स्थल पानीपत इसे गहरा इतिहास देते हैं; हिसार ज़िले का राखीगढ़ी ज्ञात सबसे बड़े हड़प्पा स्थलों में से एक है। हरियाणा के गाँवों के अखाड़ों ने भारत के कई ओलंपिक पहलवान और मुक्केबाज़ दिए हैं, और पानीपत के नीरज चोपड़ा ने एथलेटिक्स में भारत का पहला ओलंपिक स्वर्ण जीता।",
        "हरियाणा ही शेती, पैलवान आणि झपाट्याने वाढणाऱ्या शहरांची भूमी आहे. गहू, भात व मोहरीची शेते आणि मुर्रा म्हशी यांमुळे तो भारतातील सर्वाधिक उत्पादक कृषी राज्यांपैकी एक आहे, तर गुरुग्राम हे कॉर्पोरेट व तंत्रज्ञान केंद्र बनले आहे आणि फरिदाबाद–गुरुग्राम–मानेसर पट्टा मोटार व सुटे भाग उद्योगाचे मोठे केंद्र आहे. महाभारताची युद्धभूमी कुरुक्षेत्र, जिथे भगवद्गीता सांगितली गेली असे मानले जाते, आणि तीन निर्णायक युद्धांचे ठिकाण पानिपत यांमुळे त्याला खोल इतिहास आहे; हिसार जिल्ह्यातील राखीगढी हे ज्ञात सर्वांत मोठ्या हडप्पा स्थळांपैकी एक आहे. हरियाणाच्या गावांतील आखाड्यांनी भारताला अनेक ऑलिम्पिक पैलवान व मुष्टियोद्धे दिले आहेत, आणि पानिपतच्या नीरज चोप्राने ॲथलेटिक्समध्ये भारताचे पहिले ऑलिम्पिक सुवर्ण जिंकले."),
        title=L("What makes Haryana unique?", "हरियाणा को ख़ास क्या बनाता है?", "हरियाणाचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed", "गठन", "निर्मिती"), L("1 November 1966 (Haryana Day)", "1 नवंबर 1966 (हरियाणा दिवस)", "1 नोव्हेंबर 1966 (हरियाणा दिन)")],
           [L("Districts / divisions", "ज़िले / मंडल", "जिल्हे / विभाग"), "23 / 6"],
           [L("Capital", "राजधानी", "राजधानी"), L("Chandigarh (Union Territory, shared with Punjab)", "चंडीगढ़ (केंद्र शासित प्रदेश, पंजाब के साथ साझा)", "चंदीगड (केंद्रशासित प्रदेश, पंजाबसोबत सामायिक)")],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Hindi; Punjabi (second language)", "हिंदी; पंजाबी (द्वितीय भाषा)", "हिंदी; पंजाबी (द्वितीय भाषा)")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Punjab and Haryana High Court, Chandigarh", "पंजाब एवं हरियाणा उच्च न्यायालय, चंडीगढ़", "पंजाब व हरियाणा उच्च न्यायालय, चंदीगड")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "HR"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; Hansi became the 23rd district in December 2025. To be linked to the State's notifications in review.",
                 "संपादकीय; हांसी दिसंबर 2025 में 23वाँ ज़िला बना। समीक्षा में राज्य की अधिसूचनाओं से जोड़ा जाएगा।",
                 "संपादकीय; हांसी डिसेंबर 2025 मध्ये 23 वा जिल्हा झाला. तपासणीत राज्याच्या अधिसूचनांशी जोडले जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Haryana has four broad landscapes. The Shivalik hills, with the Morni hills of Panchkula district, rise in the north-east. Below them lies the Yamuna–Ghaggar plain, the fertile heart of the State, drained by the Yamuna along the eastern border and by seasonal streams such as the Ghaggar, Markanda and Tangri. To the south-west the land turns sandy and semi-arid towards the Thar, around Sirsa, Bhiwani and Mahendragarh, and in the south the low ridges of the Aravallis run through Gurugram, Nuh and Faridabad. The State has no perennial river of its own apart from the Yamuna and depends heavily on canals and groundwater.",
        "हरियाणा के चार मोटे भू-दृश्य हैं। उत्तर-पूर्व में शिवालिक की पहाड़ियाँ हैं, जिनमें पंचकूला ज़िले की मोरनी पहाड़ियाँ हैं। उनके नीचे यमुना–घग्गर का मैदान है, जो राज्य का उपजाऊ हृदय है; पूर्वी सीमा पर यमुना और घग्गर, मारकंडा व टांगरी जैसी मौसमी धाराएँ इसका जल बहाती हैं। दक्षिण-पश्चिम में सिरसा, भिवानी और महेंद्रगढ़ के आसपास भूमि थार की ओर रेतीली और अर्ध-शुष्क हो जाती है, और दक्षिण में अरावली की नीची पहाड़ियाँ गुरुग्राम, नूँह और फ़रीदाबाद से गुज़रती हैं। यमुना के अलावा राज्य की अपनी कोई सदानीरा नदी नहीं है, और यह नहरों और भूजल पर बहुत निर्भर है।",
        "हरियाणाचे चार ढोबळ भूप्रदेश आहेत. ईशान्येला शिवालिकच्या टेकड्या आहेत, ज्यांत पंचकुला जिल्ह्यातील मोरनी टेकड्या आहेत. त्यांच्या खाली यमुना–घग्गरचे मैदान आहे, जे राज्याचे सुपीक हृदय आहे; पूर्व सीमेवरील यमुना आणि घग्गर, मारकंडा व टांगरीसारखे हंगामी प्रवाह त्यातील पाणी वाहून नेतात. नैर्ऋत्येला सिरसा, भिवानी व महेंद्रगडभोवती जमीन थारकडे वाळूमय व अर्धशुष्क होते, आणि दक्षिणेला अरवलीच्या कमी उंचीच्या टेकड्या गुरुग्राम, नूह व फरिदाबादमधून जातात. यमुनेशिवाय राज्याची स्वतःची बारमाही नदी नाही, आणि ते कालवे व भूजलावर मोठ्या प्रमाणात अवलंबून आहे."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), hr["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("pb", "Punjab (north-west)", "पंजाब (उत्तर-पश्चिम)", "पंजाब (वायव्य)"), it3("ch", "Chandigarh (north)", "चंडीगढ़ (उत्तर)", "चंदीगड (उत्तर)"),
        it3("hp", "Himachal Pradesh (north)", "हिमाचल प्रदेश (उत्तर)", "हिमाचल प्रदेश (उत्तर)"), it3("up", "Uttar Pradesh (east)", "उत्तर प्रदेश (पूर्व)", "उत्तर प्रदेश (पूर्व)"),
        it3("dl", "Delhi (east, enclosed on three sides)", "दिल्ली (पूर्व, तीन ओर से घिरी)", "दिल्ली (पूर्व, तीन बाजूंनी वेढलेली)"), it3("rj", "Rajasthan (south-west and south)", "राजस्थान (दक्षिण-पश्चिम और दक्षिण)", "राजस्थान (नैर्ऋत्य व दक्षिण)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("yamuna", "Yamuna", "यमुना", "यमुना", d=("Forms the eastern border with Uttar Pradesh; Hathnikund barrage feeds the Western Yamuna Canal.", "उत्तर प्रदेश के साथ पूर्वी सीमा बनाती है; हथिनीकुंड बैराज पश्चिमी यमुना नहर को पानी देता है।", "उत्तर प्रदेशसोबतची पूर्व सीमा बनवते; हथिनीकुंड बंधारा पश्चिम यमुना कालव्याला पाणी देतो.")),
        it3("ghaggar", "Ghaggar", "घग्गर", "घग्गर", d=("Seasonal river from the Shivaliks, crossing Panchkula, Ambala, Kaithal, Fatehabad and Sirsa.", "शिवालिक से निकलने वाली मौसमी नदी, जो पंचकूला, अंबाला, कैथल, फ़तेहाबाद और सिरसा से गुज़रती है।", "शिवालिकमधून निघणारी हंगामी नदी, जी पंचकुला, अंबाला, कैथल, फतेहाबाद व सिरसामधून जाते.")),
        it3("markanda", "Markanda", "मारकंडा", "मारकंडा", d=("Monsoon-fed stream of the north; floods Kurukshetra district in heavy rain.", "उत्तर की मानसूनी धारा; भारी वर्षा में कुरुक्षेत्र ज़िले में बाढ़।", "उत्तरेकडील पावसाळी प्रवाह; मुसळधार पावसात कुरुक्षेत्र जिल्ह्यात पूर.")),
        it3("sahibi", "Sahibi", "साहिबी", "साहिबी", d=("Seasonal stream from the Aravallis in the south.", "दक्षिण में अरावली से आने वाली मौसमी धारा।", "दक्षिणेकडील अरवलीतून येणारा हंगामी प्रवाह.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point — official elevation", "सर्वोच्च बिंदु — आधिकारिक ऊँचाई", "सर्वोच्च शिखर — अधिकृत उंची"), "survey-of-india", "Survey of India (Morni hills)."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
        (L("Area under the National Capital Region", "राष्ट्रीय राजधानी क्षेत्र में शामिल क्षेत्र", "राष्ट्रीय राजधानी क्षेत्रातील भाग"), "india-gov", "NCR Planning Board."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Haryana has a continental, semi-arid climate. Summers (April–June) are very hot, with loo winds and dust storms, especially in the south-west. The monsoon (July–September) brings most of the year's rain, more in the Shivalik foothills of the north-east than in the sandy south-west. Winters (December–February) are cold, with frost and dense fog across the plains, and western disturbances bring light winter rain that helps the wheat and mustard crops.",
        "हरियाणा की जलवायु महाद्वीपीय और अर्ध-शुष्क है। गर्मियाँ (अप्रैल–जून) बहुत गर्म होती हैं, लू और आँधियों के साथ, विशेषकर दक्षिण-पश्चिम में। मानसून (जुलाई–सितंबर) वर्ष की अधिकांश वर्षा लाता है, जो रेतीले दक्षिण-पश्चिम की तुलना में उत्तर-पूर्व की शिवालिक तलहटी में अधिक होती है। सर्दियाँ (दिसंबर–फ़रवरी) ठंडी होती हैं, मैदानों में पाला और घना कोहरा रहता है, और पश्चिमी विक्षोभ सर्दियों की हल्की वर्षा लाते हैं जो गेहूँ और सरसों की फ़सलों के लिए सहायक है।",
        "हरियाणाचे हवामान खंडीय व अर्धशुष्क आहे. उन्हाळा (एप्रिल–जून) अतिशय उष्ण असतो, लू वारे व धुळीच्या वादळांसह, विशेषतः नैर्ऋत्येत. मान्सून (जुलै–सप्टेंबर) वर्षातील बहुतेक पाऊस आणतो, जो वाळूमय नैर्ऋत्येपेक्षा ईशान्येकडील शिवालिक पायथ्याशी अधिक पडतो. हिवाळा (डिसेंबर–फेब्रुवारी) थंड असतो, मैदानांत दव गोठते व दाट धुके असते, आणि पश्चिमी विक्षोभ हलका हिवाळी पाऊस आणतात जो गहू व मोहरीच्या पिकांना उपयुक्त ठरतो."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Gurugram", "गुरुग्राम", "गुरुग्राम"), "lat": 28.4595, "lon": 77.0266},
        {"name": L("Hisar", "हिसार", "हिसार"), "lat": 29.1492, "lon": 75.7217},
        {"name": L("Ambala", "अंबाला", "अंबाला"), "lat": 30.3782, "lon": 76.7767},
        {"name": L("Kurukshetra", "कुरुक्षेत्र", "कुरुक्षेत्र"), "lat": 29.9695, "lon": 76.8783},
    ]},
    lst("best", [
        it3("winter", "October to March", "अक्टूबर से मार्च", "ऑक्टोबर ते मार्च", d=("Pleasant days; the Gita Mahotsav at Kurukshetra and the Surajkund crafts fair in February; fog can delay travel.", "सुहावने दिन; कुरुक्षेत्र में गीता महोत्सव और फ़रवरी में सूरजकुंड शिल्प मेला; कोहरे से यात्रा में देरी हो सकती है।", "आल्हाददायक दिवस; कुरुक्षेत्र येथील गीता महोत्सव व फेब्रुवारीतील सूरजकुंड हस्तकला मेळा; धुक्यामुळे प्रवासाला उशीर होऊ शकतो.")),
        it3("spring", "March to April", "मार्च से अप्रैल", "मार्च ते एप्रिल", d=("Mustard in flower, then the wheat harvest and Baisakhi.", "सरसों फूलती है, फिर गेहूँ की कटाई और बैसाखी।", "मोहरी फुलते, नंतर गव्हाची कापणी व बैसाखी.")),
        it3("summer", "May to June", "मई से जून", "मे ते जून", d=("Very hot; Morni hills are the cooler escape.", "बहुत गर्म; मोरनी पहाड़ियाँ ठंडी जगह हैं।", "अतिशय उष्ण; मोरनी टेकड्या हे थंड ठिकाण.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (Haryana, Chandigarh and Delhi sub-division)", "सामान्य वार्षिक वर्षा (हरियाणा, चंडीगढ़ और दिल्ली उप-मंडल)", "सरासरी वार्षिक पाऊस (हरियाणा, चंदीगड व दिल्ली उपविभाग)"), "imd", "IMD rainfall statistics."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Haryana is plain-spoken and proud. Village life revolves around fields, cattle and the chaupal where elders gather, and the hookah, the akhara and the evening game of kabaddi are part of the rhythm. Milk, curd, ghee and buttermilk are everyday staples — 'desaan mein des Haryana, jit doodh dahi ka khaana' runs a popular saying. Along the highways, dhabas at Murthal serve parathas with white butter through the night. A short drive away, Gurugram's glass towers, malls and metro show the other Haryana — young, corporate and connected to the world.",
        "हरियाणा सीधा-सादा और स्वाभिमानी है। गाँव का जीवन खेतों, पशुओं और उस चौपाल के चारों ओर घूमता है जहाँ बड़े-बुज़ुर्ग बैठते हैं, और हुक्का, अखाड़ा और शाम का कबड्डी का खेल इसकी लय का हिस्सा हैं। दूध, दही, घी और छाछ रोज़ का भोजन हैं — 'देसां में देस हरियाणा, जित दूध दही का खाणा' एक लोकप्रिय कहावत है। राजमार्गों पर मुरथल के ढाबे रात भर सफ़ेद मक्खन के साथ पराठे परोसते हैं। कुछ ही दूरी पर गुरुग्राम के शीशे के टावर, मॉल और मेट्रो दूसरा हरियाणा दिखाते हैं — युवा, कॉर्पोरेट और दुनिया से जुड़ा।",
        "हरियाणा सरळ बोलणारा व स्वाभिमानी आहे. गावजीवन शेती, गुरेढोरे आणि वडीलधारी मंडळी जमतात त्या चौपालभोवती फिरते, आणि हुक्का, आखाडा व संध्याकाळचा कबड्डीचा खेळ हा त्याच्या लयीचा भाग आहे. दूध, दही, तूप व ताक हे रोजचे अन्न आहे — 'देसां में देस हरियाणा, जित दूध दही का खाणा' ही लोकप्रिय म्हण आहे. महामार्गांवर मुरथलचे ढाबे रात्रभर पांढऱ्या लोण्यासह पराठे देतात. थोड्याच अंतरावर गुरुग्रामचे काचेचे मनोरे, मॉल व मेट्रो दुसरा हरियाणा दाखवतात — तरुण, कॉर्पोरेट व जगाशी जोडलेला."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Haryana had 2.54 crore people at the 2011 Census, with about 573 people per km². Its sex ratio was 879 women per 1,000 men, and its child sex ratio, 834 girls per 1,000 boys, was the lowest of any State or Union Territory, though up from 819 in 2001. Literacy was 75.6%. Scheduled Castes made up 20.2% of the population; the State has no notified Scheduled Tribes.\n\nHindi is the official language and Haryanvi — in forms such as Bangru, Ahirwati, Mewati and Bagri — is the everyday speech of most villages. Punjabi is widely spoken, especially among families who came from western Punjab at Partition.",
        "2011 की जनगणना में हरियाणा की जनसंख्या 2.54 करोड़ थी, और प्रति वर्ग किमी लगभग 573 लोग। लिंगानुपात प्रति 1,000 पुरुषों पर 879 महिलाएँ था, और शिशु लिंगानुपात, प्रति 1,000 लड़कों पर 834 लड़कियाँ, किसी भी राज्य या केंद्र शासित प्रदेश में सबसे कम था, हालाँकि 2001 के 819 से ऊपर। साक्षरता 75.6% थी। अनुसूचित जातियाँ जनसंख्या का 20.2% थीं; राज्य में कोई अधिसूचित अनुसूचित जनजाति नहीं है।\n\nहिंदी राजभाषा है और हरियाणवी — बांगरू, अहीरवाटी, मेवाती और बागड़ी जैसे रूपों में — अधिकांश गाँवों की रोज़ की बोली है। पंजाबी व्यापक रूप से बोली जाती है, विशेषकर उन परिवारों में जो विभाजन के समय पश्चिमी पंजाब से आए।",
        "2011 च्या जनगणनेनुसार हरियाणाची लोकसंख्या 2.54 कोटी होती, आणि प्रति चौ.किमी सुमारे 573 लोक. दर 1,000 पुरुषांमागे 879 स्त्रिया होत्या, आणि बाल लिंग गुणोत्तर, दर 1,000 मुलांमागे 834 मुली, हे कोणत्याही राज्य वा केंद्रशासित प्रदेशात सर्वांत कमी होते, जरी 2001 मधील 819 पेक्षा अधिक. साक्षरता 75.6% होती. अनुसूचित जाती लोकसंख्येच्या 20.2% होत्या; राज्यात एकही अधिसूचित अनुसूचित जमात नाही.\n\nहिंदी ही राजभाषा आहे आणि हरियाणवी — बांगरू, अहिरवाटी, मेवाती व बागडी अशा रूपांत — ही बहुतेक गावांची रोजची बोली आहे. पंजाबी मोठ्या प्रमाणावर बोलली जाते, विशेषतः फाळणीच्या वेळी पश्चिम पंजाबमधून आलेल्या कुटुंबांत."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), hr["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), hr["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(861, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), hr["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(819, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), hr["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), hr["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(20.2, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 51.13 lakh people. No Scheduled Tribes are notified in Haryana."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("hi", "Hindi", "हिंदी", "हिंदी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("pa", "Punjabi", "पंजाबी", "पंजाबी", m=("Second language", "द्वितीय भाषा", "द्वितीय भाषा")),
        it3("bangru", "Haryanvi (Bangru)", "हरियाणवी (बांगरू)", "हरियाणवी (बांगरू)", m=("Dialect", "बोली", "बोली")),
        it3("ahirwati", "Ahirwati", "अहीरवाटी", "अहिरवाटी", m=("Dialect", "बोली", "बोली")),
        it3("mewati", "Mewati", "मेवाती", "मेवाती", m=("Dialect", "बोली", "बोली")),
        it3("bagri", "Bagri", "बागड़ी", "बागडी", m=("Dialect", "बोली", "बोली")),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Literacy rate in 2001", "2001 में साक्षरता दर", "2001 मधील साक्षरता दर"), "census", "Census 2001 / Economic Survey Table 8.5."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Haryana's plains were home to the Harappan civilisation: Rakhigarhi in Hisar district, Banawali in Fatehabad and Bhirrana are among its important sites. In the epics this is the land of Kurukshetra, where the Mahabharata war was fought, and the region later lay at the heart of the kingdoms that ruled northern India — Thanesar was the capital of Harshavardhana in the 7th century, and the Tomar and Chauhan rulers held Delhi and its hinterland. Because the road to Delhi ran through it, Haryana saw some of India's most decisive battles: at Tarain in 1191–92, and at Panipat in 1526, 1556 and 1761.\n\nIn 1857 the region rose against the Company, and Rao Tula Ram of Rewari was among the leaders; the British then attached it to the Punjab province. In the 20th century Sir Chhotu Ram championed the rights of peasants. After Independence the demand for a Hindi-speaking State grew, and Haryana was carved out of Punjab on 1 November 1966. The Green Revolution, canal building and later the growth of Gurugram and Faridabad transformed its economy.",
        "हरियाणा के मैदान हड़प्पा सभ्यता के घर थे: हिसार ज़िले का राखीगढ़ी, फ़तेहाबाद का बनावली और भिरड़ाना इसके महत्त्वपूर्ण स्थलों में हैं। महाकाव्यों में यह कुरुक्षेत्र की भूमि है, जहाँ महाभारत का युद्ध हुआ, और बाद में यह क्षेत्र उत्तर भारत पर शासन करने वाले राज्यों के केंद्र में रहा — 7वीं सदी में थानेसर हर्षवर्धन की राजधानी था, और तोमर व चौहान शासकों के पास दिल्ली और उसका पृष्ठ प्रदेश था। क्योंकि दिल्ली का मार्ग यहीं से जाता था, हरियाणा ने भारत के कुछ सबसे निर्णायक युद्ध देखे: 1191–92 में तराइन में, और 1526, 1556 व 1761 में पानीपत में।\n\n1857 में इस क्षेत्र ने कंपनी के विरुद्ध विद्रोह किया, और रेवाड़ी के राव तुलाराम इसके नेताओं में थे; इसके बाद अंग्रेज़ों ने इसे पंजाब प्रांत से जोड़ दिया। 20वीं सदी में सर छोटूराम ने किसानों के अधिकारों की लड़ाई लड़ी। स्वतंत्रता के बाद हिंदी-भाषी राज्य की माँग बढ़ी, और 1 नवंबर 1966 को हरियाणा पंजाब से अलग बना। हरित क्रांति, नहर निर्माण और बाद में गुरुग्राम व फ़रीदाबाद के विकास ने इसकी अर्थव्यवस्था बदल दी।",
        "हरियाणाची मैदाने हडप्पा संस्कृतीचे घर होती: हिसार जिल्ह्यातील राखीगढी, फतेहाबादचे बनावली व भिरडाणा ही तिची महत्त्वाची स्थळे आहेत. महाकाव्यांत ही कुरुक्षेत्राची भूमी आहे, जिथे महाभारताचे युद्ध झाले, आणि नंतर हा प्रदेश उत्तर भारतावर राज्य करणाऱ्या राज्यांच्या केंद्रस्थानी राहिला — सातव्या शतकात ठाणेसर ही हर्षवर्धनाची राजधानी होती, आणि तोमर व चौहान राज्यकर्त्यांकडे दिल्ली व तिचा परिसर होता. दिल्लीचा मार्ग इथूनच जात असल्याने हरियाणाने भारतातील काही अत्यंत निर्णायक लढाया पाहिल्या: 1191–92 मध्ये तराईन येथे, आणि 1526, 1556 व 1761 मध्ये पानिपत येथे.\n\n1857 मध्ये या प्रदेशाने कंपनीविरुद्ध उठाव केला, आणि रेवाडीचे राव तुलाराम त्याच्या नेत्यांपैकी होते; त्यानंतर इंग्रजांनी तो पंजाब प्रांताला जोडला. विसाव्या शतकात सर छोटूराम यांनी शेतकऱ्यांच्या हक्कांसाठी लढा दिला. स्वातंत्र्यानंतर हिंदीभाषक राज्याची मागणी वाढली, आणि 1 नोव्हेंबर 1966 रोजी हरियाणा पंजाबमधून वेगळा झाला. हरितक्रांती, कालव्यांची बांधणी आणि नंतर गुरुग्राम व फरिदाबादच्या वाढीने त्याची अर्थव्यवस्था बदलली."),
        conf="Editorial"),
    timeline([
        ev("rakhi", -2600, L("c. 2600 BCE", "लगभग 2600 ई.पू.", "सुमारे इ.स.पू. 2600"), L("Mature Harappan phase at Rakhigarhi", "राखीगढ़ी में परिपक्व हड़प्पा चरण", "राखीगढी येथे परिपक्व हडप्पा टप्पा")),
        ev("harsha", 606, L("606 CE", "606 ई.", "इ.स. 606"), L("Harshavardhana rules from Thanesar", "थानेसर से हर्षवर्धन का शासन", "ठाणेसरहून हर्षवर्धनाचे राज्य")),
        ev("panipat1", 1526, L("1526", "1526", "1526"), L("First Battle of Panipat", "पानीपत का पहला युद्ध", "पानिपतची पहिली लढाई")),
        ev("panipat3", 1761, L("1761", "1761", "1761"), L("Third Battle of Panipat", "पानीपत का तीसरा युद्ध", "पानिपतची तिसरी लढाई")),
        ev("revolt", 1857, L("1857", "1857", "1857"), L("Uprising; Rao Tula Ram of Rewari among its leaders", "विद्रोह; रेवाड़ी के राव तुलाराम इसके नेताओं में", "उठाव; रेवाडीचे राव तुलाराम त्याच्या नेत्यांपैकी")),
        ev("formed", 1966, L("1 November 1966", "1 नवंबर 1966", "1 नोव्हेंबर 1966"), L("Haryana formed", "हरियाणा का गठन", "हरियाणाची निर्मिती")),
        ev("cm2024", 2024, L("17 October 2024", "17 अक्टूबर 2024", "17 ऑक्टोबर 2024"), L("Nayab Singh Saini sworn in for a second term", "नायब सिंह सैनी ने दूसरी बार शपथ ली", "नायबसिंह सैनी यांचा दुसऱ्यांदा शपथविधी")),
        ev("hansi", 2025, L("December 2025", "दिसंबर 2025", "डिसेंबर 2025"), L("Hansi becomes the 23rd district", "हांसी 23वाँ ज़िला बना", "हांसी 23 वा जिल्हा")),
    ]),
    lst("heritage", [
        it3("rakhigarhi", "Rakhigarhi, Hisar", "राखीगढ़ी, हिसार", "राखीगढी, हिसार", m=("Harappan site", "हड़प्पा स्थल", "हडप्पा स्थळ")),
        it3("brahma", "Brahma Sarovar and Jyotisar, Kurukshetra", "ब्रह्म सरोवर और ज्योतिसर, कुरुक्षेत्र", "ब्रह्म सरोवर व ज्योतिसर, कुरुक्षेत्र", m=("Mahabharata tradition", "महाभारत परंपरा", "महाभारत परंपरा")),
        it3("sheikh", "Sheikh Chehli's tomb, Thanesar", "शेख़ चेहली का मक़बरा, थानेसर", "शेख चेहलीची कबर, ठाणेसर", m=("Mughal era", "मुग़ल काल", "मुघल काळ")),
        it3("pinjore", "Yadavindra Gardens, Pinjore", "यादविंद्र उद्यान, पिंजौर", "यादविंद्र उद्यान, पिंजोर", m=("Mughal-style garden", "मुग़ल शैली का उद्यान", "मुघल शैलीतील उद्यान")),
        it3("panipat", "Kala Amb and Panipat Museum", "काला अंब और पानीपत संग्रहालय", "काला अंब व पानिपत संग्रहालय", m=("Battle of 1761", "1761 का युद्ध", "1761 ची लढाई")),
        it3("agroha", "Agroha Dham, Hisar", "अग्रोहा धाम, हिसार", "अग्रोहा धाम, हिसार", m=("Archaeological site and temple", "पुरातात्विक स्थल और मंदिर", "पुरातत्त्वीय स्थळ व मंदिर")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
    gaps("g", [
        (L("Hansi district notification — official copy", "हांसी ज़िला अधिसूचना — आधिकारिक प्रति", "हांसी जिल्हा अधिसूचना — अधिकृत प्रत"), "india-gov", f"Cabinet approval reported by PTI ({HANSI}); link the Revenue Department notification."),
    ]),
])
print("hr mod1 ok")
