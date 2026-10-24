"""Uttarakhand modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-UK"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
uk = read("regions/IN-UK.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Uttarakhand lies in the central Himalaya, with Himachal Pradesh to the north-west, Tibet (China) to the north, Nepal to the east across the Kali river, and Uttar Pradesh and a short stretch of Haryana to the south and west. It has two historic regions — Garhwal in the west and Kumaon in the east — and rises from the Terai and Bhabar plains of Haridwar and Udham Singh Nagar through the Shivaliks and middle hills to snow peaks above 7,000 m, including Nanda Devi. The Ganga and the Yamuna both rise here. It had 1.01 crore people at the 2011 Census. Dehradun is the winter capital and Bhararisain (Gairsain) the summer capital; Haridwar, Haldwani, Roorkee, Rudrapur and Rishikesh are other major towns.\n\nThe State was carved out of Uttar Pradesh on 9 November 2000 as Uttaranchal and renamed Uttarakhand in 2007. Hindi is the official language and Sanskrit the second official language.",
        "उत्तराखंड मध्य हिमालय में है; इसके उत्तर-पश्चिम में हिमाचल प्रदेश, उत्तर में तिब्बत (चीन), पूर्व में काली नदी के पार नेपाल, और दक्षिण व पश्चिम में उत्तर प्रदेश व हरियाणा का एक छोटा हिस्सा है। इसके दो ऐतिहासिक क्षेत्र हैं — पश्चिम में गढ़वाल और पूर्व में कुमाऊँ — और यह हरिद्वार और ऊधम सिंह नगर के तराई-भाबर मैदानों से शिवालिक और मध्य पहाड़ियों से होकर नंदा देवी सहित 7,000 मीटर से ऊँची हिम चोटियों तक उठता है। गंगा और यमुना दोनों यहीं से निकलती हैं। 2011 की जनगणना में इसकी जनसंख्या 1.01 करोड़ थी। देहरादून शीतकालीन राजधानी है और भराड़ीसैंण (गैरसैंण) ग्रीष्मकालीन राजधानी; हरिद्वार, हल्द्वानी, रुड़की, रुद्रपुर और ऋषिकेश अन्य प्रमुख नगर हैं।\n\nराज्य 9 नवंबर 2000 को उत्तर प्रदेश से उत्तरांचल के रूप में अलग बना और 2007 में इसका नाम उत्तराखंड हुआ। हिंदी राजभाषा है और संस्कृत द्वितीय राजभाषा।",
        "उत्तराखंड मध्य हिमालयात आहे; त्याच्या वायव्येला हिमाचल प्रदेश, उत्तरेला तिबेट (चीन), पूर्वेला काली नदीपलीकडे नेपाळ, आणि दक्षिण व पश्चिमेला उत्तर प्रदेश व हरियाणाचा थोडासा भाग आहे. त्याचे दोन ऐतिहासिक प्रदेश आहेत — पश्चिमेला गढवाल व पूर्वेला कुमाऊँ — आणि तो हरिद्वार व उधमसिंह नगरच्या तराई-भाबर मैदानांपासून शिवालिक व मधल्या टेकड्यांमधून नंदादेवीसह 7,000 मीटरहून उंच हिमशिखरांपर्यंत चढतो. गंगा व यमुना दोन्ही इथेच उगम पावतात. 2011 च्या जनगणनेनुसार त्याची लोकसंख्या 1.01 कोटी होती. डेहराडून ही हिवाळी राजधानी व भराडीसैंण (गैरसैंण) ही उन्हाळी राजधानी आहे; हरिद्वार, हल्द्वानी, रुडकी, रुद्रपूर व ऋषिकेश ही इतर प्रमुख शहरे आहेत.\n\n9 नोव्हेंबर 2000 रोजी उत्तर प्रदेशमधून उत्तरांचल म्हणून राज्याची निर्मिती झाली आणि 2007 मध्ये त्याचे नाव उत्तराखंड झाले. हिंदी ही राजभाषा व संस्कृत ही द्वितीय राजभाषा आहे."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Uttarakhand is Dev Bhoomi, the 'land of the gods', and one of the holiest landscapes in India. The Char Dham — Yamunotri, Gangotri, Kedarnath and Badrinath — and the Sikh shrine of Hemkund Sahib draw millions of pilgrims each summer, Haridwar is one of the four sites of the Kumbh Mela, and Rishikesh is known worldwide for yoga. The State is also a land of forests and wildlife: nearly half of it is forest, Jim Corbett National Park was India's first national park, and the Valley of Flowers and Nanda Devi national parks are a UNESCO World Heritage site. The Chipko movement, in which village women hugged trees to stop logging in the 1970s, began here, and the hill regiments of Garhwal and Kumaon are famous in the Indian Army.",
        "उत्तराखंड देवभूमि है और भारत के सबसे पवित्र भूदृश्यों में से है। चार धाम — यमुनोत्री, गंगोत्री, केदारनाथ और बद्रीनाथ — और सिख तीर्थ हेमकुंड साहिब हर गर्मी में लाखों तीर्थयात्रियों को खींचते हैं, हरिद्वार कुंभ मेले के चार स्थलों में से है, और ऋषिकेश योग के लिए विश्व भर में जाना जाता है। राज्य वनों और वन्यजीवों की भूमि भी है: इसका लगभग आधा भाग वन है, जिम कॉर्बेट राष्ट्रीय उद्यान भारत का पहला राष्ट्रीय उद्यान था, और फूलों की घाटी व नंदा देवी राष्ट्रीय उद्यान यूनेस्को विश्व धरोहर स्थल हैं। चिपको आंदोलन, जिसमें 1970 के दशक में गाँव की महिलाओं ने कटाई रोकने के लिए पेड़ों से चिपककर विरोध किया, यहीं शुरू हुआ, और गढ़वाल व कुमाऊँ की पहाड़ी रेजिमेंट भारतीय सेना में प्रसिद्ध हैं।",
        "उत्तराखंड ही देवभूमी आहे आणि भारतातील सर्वांत पवित्र भूदृश्यांपैकी एक आहे. चार धाम — यमुनोत्री, गंगोत्री, केदारनाथ व बद्रीनाथ — आणि शीख तीर्थ हेमकुंड साहिब दर उन्हाळ्यात लाखो यात्रेकरूंना आकर्षित करतात, हरिद्वार हे कुंभमेळ्याच्या चार स्थळांपैकी एक आहे, आणि ऋषिकेश योगासाठी जगभर ओळखले जाते. राज्य वने व वन्यजीवांचीही भूमी आहे: त्याचा जवळपास निम्मा भाग वनाच्छादित आहे, जिम कॉर्बेट राष्ट्रीय उद्यान हे भारताचे पहिले राष्ट्रीय उद्यान होते, आणि फुलांचे खोरे व नंदादेवी राष्ट्रीय उद्याने युनेस्को जागतिक वारसा स्थळ आहेत. 1970 च्या दशकात गावच्या स्त्रियांनी वृक्षतोड थांबवण्यासाठी झाडांना मिठी मारली ते चिपको आंदोलन इथेच सुरू झाले, आणि गढवाल व कुमाऊँच्या डोंगरी रेजिमेंट भारतीय सैन्यात प्रसिद्ध आहेत."),
        title=L("What makes Uttarakhand unique?", "उत्तराखंड को ख़ास क्या बनाता है?", "उत्तराखंडचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed", "गठन", "निर्मिती"), L("9 November 2000 (as Uttaranchal; renamed 2007)", "9 नवंबर 2000 (उत्तरांचल के रूप में; 2007 में नाम बदला)", "9 नोव्हेंबर 2000 (उत्तरांचल म्हणून; 2007 मध्ये नाव बदलले)")],
           [L("Districts / divisions", "ज़िले / मंडल", "जिल्हे / विभाग"), L("13 / 2 (Garhwal, Kumaon)", "13 / 2 (गढ़वाल, कुमाऊँ)", "13 / 2 (गढवाल, कुमाऊँ)")],
           [L("Capital", "राजधानी", "राजधानी"), L("Dehradun (winter); Bhararisain, Gairsain (summer)", "देहरादून (शीतकालीन); भराड़ीसैंण, गैरसैंण (ग्रीष्मकालीन)", "डेहराडून (हिवाळी); भराडीसैंण, गैरसैंण (उन्हाळी)")],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Hindi; Sanskrit (second official language)", "हिंदी; संस्कृत (द्वितीय राजभाषा)", "हिंदी; संस्कृत (द्वितीय राजभाषा)")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("High Court of Uttarakhand, Nainital", "उत्तराखंड उच्च न्यायालय, नैनीताल", "उत्तराखंड उच्च न्यायालय, नैनीताल")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "UK"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be linked to the State's notifications in review.", "संपादकीय; समीक्षा में राज्य की अधिसूचनाओं से जोड़ा जाएगा।", "संपादकीय; तपासणीत राज्याच्या अधिसूचनांशी जोडले जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Uttarakhand has five belts from south to north. The Terai and Bhabar — once swampy forest, now fertile farmland — fringe the plains of Haridwar and Udham Singh Nagar. Above them rise the Shivaliks and the Doon valley, then the middle hills (the Lesser Himalaya) with towns such as Mussoorie, Nainital, Almora and Pauri, and then the Great Himalaya, with Nanda Devi (7,816 m), Kamet, Trishul and the Panchachuli peaks and glaciers such as Gangotri, Satopanth and Pindari. In the far north, valleys such as Niti, Mana and Johar lead to passes into Tibet. The Bhagirathi and Alaknanda meet at Devprayag to form the Ganga, the Yamuna rises at Yamunotri, and the Kali (Sharda) forms the border with Nepal.",
        "उत्तराखंड में दक्षिण से उत्तर पाँच पट्टियाँ हैं। तराई और भाबर — कभी दलदली वन, अब उपजाऊ खेत — हरिद्वार और ऊधम सिंह नगर के मैदानों के किनारे हैं। उनके ऊपर शिवालिक और दून घाटी हैं, फिर मसूरी, नैनीताल, अल्मोड़ा और पौड़ी जैसे नगरों वाली मध्य पहाड़ियाँ (लघु हिमालय), और फिर महान हिमालय, जिसमें नंदा देवी (7,816 मीटर), कामेट, त्रिशूल और पंचाचूली चोटियाँ और गंगोत्री, सतोपंथ व पिंडारी जैसे हिमनद हैं। सुदूर उत्तर में नीती, माणा और जोहार जैसी घाटियाँ तिब्बत के दर्रों तक जाती हैं। भागीरथी और अलकनंदा देवप्रयाग में मिलकर गंगा बनाती हैं, यमुना यमुनोत्री से निकलती है, और काली (शारदा) नेपाल के साथ सीमा बनाती है।",
        "उत्तराखंडमध्ये दक्षिणेकडून उत्तरेकडे पाच पट्टे आहेत. तराई व भाबर — एकेकाळी दलदलीचे जंगल, आता सुपीक शेती — हरिद्वार व उधमसिंह नगरच्या मैदानांच्या कडेला आहेत. त्यांच्या वर शिवालिक व डून खोरे, नंतर मसुरी, नैनीताल, अल्मोडा व पौडीसारख्या शहरांच्या मधल्या टेकड्या (लघु हिमालय), आणि नंतर महान हिमालय, ज्यात नंदादेवी (7,816 मीटर), कामेत, त्रिशूल व पंचचुली शिखरे आणि गंगोत्री, सतोपंथ व पिंडारीसारख्या हिमनद्या आहेत. अगदी उत्तरेला नीती, माणा व जोहारसारखी खोरी तिबेटकडील खिंडींकडे जातात. भागीरथी व अलकनंदा देवप्रयाग येथे मिळून गंगा बनते, यमुना यमुनोत्री येथे उगम पावते, आणि काली (शारदा) नेपाळसोबतची सीमा बनवते."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), uk["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("cn", "Tibet, China (north)", "तिब्बत, चीन (उत्तर)", "तिबेट, चीन (उत्तर)"), it3("np", "Nepal (east)", "नेपाल (पूर्व)", "नेपाळ (पूर्व)"),
        it3("up", "Uttar Pradesh (south)", "उत्तर प्रदेश (दक्षिण)", "उत्तर प्रदेश (दक्षिण)"), it3("hr", "Haryana (south-west)", "हरियाणा (दक्षिण-पश्चिम)", "हरियाणा (नैर्ऋत्य)"),
        it3("hp", "Himachal Pradesh (north-west)", "हिमाचल प्रदेश (उत्तर-पश्चिम)", "हिमाचल प्रदेश (वायव्य)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("bhagirathi", "Bhagirathi", "भागीरथी", "भागीरथी", d=("Source stream of the Ganga from the Gangotri glacier at Gaumukh; Tehri dam.", "गौमुख में गंगोत्री हिमनद से निकलने वाली गंगा की स्रोत धारा; टिहरी बाँध।", "गौमुख येथे गंगोत्री हिमनदीतून निघणारा गंगेचा स्रोतप्रवाह; टिहरी धरण.")),
        it3("alaknanda", "Alaknanda", "अलकनंदा", "अलकनंदा", d=("Flows past Badrinath; joined at the five prayags.", "बद्रीनाथ के पास से बहती है; पंच प्रयागों पर सहायक नदियाँ मिलती हैं।", "बद्रीनाथजवळून वाहते; पंचप्रयागांवर उपनद्या मिळतात.")),
        it3("ganga", "Ganga", "गंगा", "गंगा", d=("Formed at Devprayag; enters the plains at Rishikesh and Haridwar.", "देवप्रयाग में बनती है; ऋषिकेश और हरिद्वार में मैदानों में आती है।", "देवप्रयाग येथे तयार होते; ऋषिकेश व हरिद्वार येथे मैदानात येते.")),
        it3("yamuna", "Yamuna", "यमुना", "यमुना", d=("Rises at Yamunotri; forms part of the border with Himachal.", "यमुनोत्री से निकलती है; हिमाचल के साथ सीमा का हिस्सा।", "यमुनोत्री येथे उगम; हिमाचलसोबतच्या सीमेचा भाग.")),
        it3("kali", "Kali (Sharda)", "काली (शारदा)", "काली (शारदा)", d=("Border river with Nepal in Pithoragarh and Champawat.", "पिथौरागढ़ और चंपावत में नेपाल के साथ सीमा नदी।", "पिथौरागड व चंपावतमध्ये नेपाळसोबतची सीमानदी.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Nanda Devi elevation — Survey of India citation", "नंदा देवी की ऊँचाई — सर्वे ऑफ़ इंडिया संदर्भ", "नंदादेवीची उंची — सर्व्हे ऑफ इंडिया संदर्भ"), "survey-of-india", "Cite the Survey of India figure for the elevation used above."),
        (L("Glaciers and glacial lakes", "हिमनद और हिमनदी झीलें", "हिमनद्या व हिमनदी सरोवरे"), "india-gov", "Wadia Institute of Himalayan Geology / NRSC inventory."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "The plains and Doon valley have hot summers, a heavy monsoon and cool winters; the middle hills, around 1,500–2,500 m, have mild summers and cold winters with occasional snow; and the high Himalaya is under snow for much of the year, with the Char Dham shrines open only from about late April or May to November. The monsoon (late June to September) brings intense rain to the outer ranges, and cloudbursts, landslides and flash floods are common. Western disturbances bring winter rain and snow.",
        "मैदानों और दून घाटी में गर्मियाँ गर्म, मानसून भारी और सर्दियाँ ठंडी होती हैं; लगभग 1,500–2,500 मीटर की मध्य पहाड़ियों में गर्मियाँ हल्की और सर्दियाँ ठंडी होती हैं, कभी-कभी बर्फ़ के साथ; और ऊँचा हिमालय वर्ष के अधिकांश समय बर्फ़ से ढका रहता है, जहाँ चार धाम के मंदिर केवल अप्रैल के अंत या मई से नवंबर तक खुलते हैं। मानसून (जून के अंत से सितंबर) बाहरी श्रेणियों में तीव्र वर्षा लाता है, और बादल फटना, भूस्खलन व अचानक बाढ़ आम हैं। पश्चिमी विक्षोभ सर्दियों में वर्षा और बर्फ़ लाते हैं।",
        "मैदाने व डून खोऱ्यात उन्हाळा उष्ण, मान्सून मुसळधार व हिवाळा थंड असतो; सुमारे 1,500–2,500 मीटरवरील मधल्या टेकड्यांत उन्हाळा सौम्य व हिवाळा थंड असतो, कधीकधी बर्फासह; आणि उंच हिमालय वर्षातील बहुतेक काळ बर्फाखाली असतो, जिथे चार धामची मंदिरे केवळ एप्रिलच्या अखेरीपासून किंवा मेपासून नोव्हेंबरपर्यंत उघडी असतात. मान्सून (जूनच्या अखेरीपासून सप्टेंबर) बाहेरच्या रांगांत तीव्र पाऊस आणतो, आणि ढगफुटी, भूस्खलन व आकस्मिक पूर सामान्य आहेत. पश्चिमी विक्षोभ हिवाळ्यात पाऊस व बर्फ आणतात."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Dehradun", "देहरादून", "डेहराडून"), "lat": 30.3165, "lon": 78.0322},
        {"name": L("Nainital", "नैनीताल", "नैनीताल"), "lat": 29.3803, "lon": 79.4636},
        {"name": L("Haridwar", "हरिद्वार", "हरिद्वार"), "lat": 29.9457, "lon": 78.1642},
        {"name": L("Joshimath", "जोशीमठ", "जोशीमठ"), "lat": 30.5560, "lon": 79.5643},
    ]},
    lst("best", [
        it3("summer", "April to June", "अप्रैल से जून", "एप्रिल ते जून", d=("Char Dham season opens; hill stations at their best.", "चार धाम यात्रा शुरू; पर्वतीय स्थल सबसे सुंदर।", "चार धाम यात्रा सुरू; थंड हवेची ठिकाणे सर्वोत्तम.")),
        it3("autumn", "September to November", "सितंबर से नवंबर", "सप्टेंबर ते नोव्हेंबर", d=("Clear Himalayan views after the monsoon; good trekking.", "मानसून के बाद हिमालय के साफ़ दृश्य; ट्रेकिंग के लिए अच्छा।", "मान्सूननंतर हिमालयाचे स्वच्छ दर्शन; ट्रेकिंगसाठी चांगले.")),
        it3("monsoon", "July to August", "जुलाई से अगस्त", "जुलै ते ऑगस्ट", d=("Valley of Flowers in bloom, but landslides often block roads.", "फूलों की घाटी खिली होती है, पर भूस्खलन अक्सर सड़कें रोकते हैं।", "फुलांचे खोरे बहरलेले असते, पण भूस्खलन अनेकदा रस्ते अडवतात.")),
        it3("winter", "December to March", "दिसंबर से मार्च", "डिसेंबर ते मार्च", d=("Skiing at Auli; Corbett safaris; high shrines closed.", "औली में स्कीइंग; कॉर्बेट सफ़ारी; ऊँचे मंदिर बंद।", "औलीत स्कीइंग; कॉर्बेट सफारी; उंचावरील मंदिरे बंद.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall", "सामान्य वार्षिक वर्षा", "सरासरी वार्षिक पाऊस"), "imd", "IMD Dehradun meteorological centre."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Uttarakhand moves to the rhythm of pilgrimage and the seasons. At Haridwar's Har ki Pauri and Rishikesh's ghats, lamps float down the Ganga at the evening aarti, while ashrams, yoga schools and cafés line the river. In the hills, slate-roofed villages sit among terraced fields of millet and red rice, women gather fodder and firewood from the forest, and the sound of the dhol-damau announces a jagar or a wedding. Bal mithai from Almora, aloo ke gutke and bhatt ki churkani are local flavours, and in many villages old houses stand empty as young people have left for jobs in the plains.",
        "उत्तराखंड तीर्थयात्रा और ऋतुओं की लय पर चलता है। हरिद्वार की हर की पैड़ी और ऋषिकेश के घाटों पर शाम की आरती में दीप गंगा में बहते हैं, जबकि नदी किनारे आश्रम, योग विद्यालय और कैफ़े हैं। पहाड़ों में स्लेट की छत वाले गाँव मंडुआ और लाल चावल के सीढ़ीदार खेतों के बीच बसे हैं, महिलाएँ जंगल से चारा और लकड़ी लाती हैं, और ढोल-दमाऊ की ध्वनि जागर या विवाह की घोषणा करती है। अल्मोड़ा की बाल मिठाई, आलू के गुटके और भट्ट की चुड़कानी स्थानीय स्वाद हैं, और कई गाँवों में पुराने घर ख़ाली पड़े हैं क्योंकि युवा मैदानों में नौकरियों के लिए चले गए हैं।",
        "उत्तराखंड तीर्थयात्रा व ऋतूंच्या लयीवर चालतो. हरिद्वारच्या हर की पौडी व ऋषिकेशच्या घाटांवर संध्याकाळच्या आरतीत दिवे गंगेत तरंगतात, तर नदीकाठी आश्रम, योगशाळा व कॅफे आहेत. डोंगरांत स्लेटच्या छपरांची गावे नाचणी व लाल तांदळाच्या पायऱ्यांच्या शेतांमध्ये वसलेली आहेत, स्त्रिया जंगलातून चारा व सरपण आणतात, आणि ढोल-दमाऊचा आवाज जागर किंवा लग्नाची वर्दी देतो. अल्मोड्याची बाल मिठाई, आलू के गुटके व भट्टाची चुडकानी या स्थानिक चवी आहेत, आणि अनेक गावांत तरुण मैदानी भागात नोकरीसाठी गेल्याने जुनी घरे रिकामी पडली आहेत."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Uttarakhand had 1.01 crore people at the 2011 Census, with about 189 people per km² — though most live in the plains districts of Haridwar, Dehradun, Udham Singh Nagar and Nainital, while hill districts are sparsely settled. The sex ratio was 963 women per 1,000 men, but the child sex ratio fell from 908 in 2001 to 890 in 2011. Literacy was 78.8%. Scheduled Castes made up 18.8% of the population and Scheduled Tribes 2.9% — among them the Tharu and Buksa of the Terai, the Jaunsari of Jaunsar-Bawar, and the Bhotia and Raji of the high valleys.\n\nHindi is the official language; Garhwali and Kumaoni are the main mother tongues of the hills, with Jaunsari in the west, and Punjabi, Urdu and Bengali are spoken in the plains, where many families settled after Partition.",
        "2011 की जनगणना में उत्तराखंड की जनसंख्या 1.01 करोड़ थी, और प्रति वर्ग किमी लगभग 189 लोग — हालाँकि अधिकांश लोग हरिद्वार, देहरादून, ऊधम सिंह नगर और नैनीताल के मैदानी ज़िलों में रहते हैं, जबकि पहाड़ी ज़िलों में बसावट कम है। लिंगानुपात प्रति 1,000 पुरुषों पर 963 महिलाएँ था, लेकिन शिशु लिंगानुपात 2001 के 908 से घटकर 2011 में 890 हो गया। साक्षरता 78.8% थी। अनुसूचित जातियाँ जनसंख्या का 18.8% और अनुसूचित जनजातियाँ 2.9% थीं — जिनमें तराई के थारू और बुक्सा, जौनसार-बावर के जौनसारी, और ऊँची घाटियों के भोटिया और राजी शामिल हैं।\n\nहिंदी राजभाषा है; गढ़वाली और कुमाऊँनी पहाड़ों की मुख्य मातृभाषाएँ हैं, पश्चिम में जौनसारी है, और मैदानों में पंजाबी, उर्दू और बांग्ला बोली जाती हैं, जहाँ विभाजन के बाद बहुत से परिवार बसे।",
        "2011 च्या जनगणनेनुसार उत्तराखंडची लोकसंख्या 1.01 कोटी होती, आणि प्रति चौ.किमी सुमारे 189 लोक — तरी बहुतेक लोक हरिद्वार, डेहराडून, उधमसिंह नगर व नैनीतालच्या मैदानी जिल्ह्यांत राहतात, तर डोंगरी जिल्ह्यांत वस्ती विरळ आहे. दर 1,000 पुरुषांमागे 963 स्त्रिया होत्या, पण बाल लिंग गुणोत्तर 2001 मधील 908 वरून 2011 मध्ये 890 वर घसरले. साक्षरता 78.8% होती. अनुसूचित जाती लोकसंख्येच्या 18.8% व अनुसूचित जमाती 2.9% होत्या — ज्यांत तराईचे थारू व बुक्सा, जौनसार-बावरचे जौनसारी आणि उंच खोऱ्यांतील भोटिया व राजी यांचा समावेश आहे.\n\nहिंदी ही राजभाषा आहे; गढवाली व कुमाऊँनी या डोंगरांतील मुख्य मातृभाषा आहेत, पश्चिमेला जौनसारी आहे, आणि मैदानी भागात पंजाबी, उर्दू व बंगाली बोलल्या जातात, जिथे फाळणीनंतर अनेक कुटुंबे स्थायिक झाली."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), uk["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), uk["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(962, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), uk["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(908, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), uk["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), uk["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(18.8, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 18.92 lakh people."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(2.9, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 2.91 lakh people."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("hi", "Hindi", "हिंदी", "हिंदी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("sa", "Sanskrit", "संस्कृत", "संस्कृत", m=("Second official language", "द्वितीय राजभाषा", "द्वितीय राजभाषा")),
        it3("garhwali", "Garhwali", "गढ़वाली", "गढवाली"), it3("kumaoni", "Kumaoni", "कुमाऊँनी", "कुमाऊँनी"),
        it3("jaunsari", "Jaunsari", "जौनसारी", "जौनसारी"), it3("pa", "Punjabi", "पंजाबी", "पंजाबी"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Out-migration from hill villages", "पहाड़ी गाँवों से पलायन", "डोंगरी गावांतून स्थलांतर"), "india-gov", "Uttarakhand Rural Development and Migration Prevention Commission reports."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Uttarakhand appears in the Puranas as Kedarkhand (Garhwal) and Manaskhand (Kumaon), and its shrines at Badrinath and Kedarnath are linked to Adi Shankaracharya, who is said to have revived them in the 8th century. The Katyuri dynasty ruled much of the region from the Katyur valley and Baijnath between about the 7th and 11th centuries, building temples such as those at Jageshwar and Baijnath. Later the Chand kings ruled Kumaon from Champawat and then Almora, and the Panwar (Parmar) dynasty unified Garhwal with its capital at Srinagar on the Alaknanda.\n\nThe Gurkhas of Nepal overran both kingdoms around 1790–1804; after the Anglo-Gurkha war of 1814–16 the British annexed Kumaon and eastern Garhwal, while Tehri Garhwal remained a princely state until 1949. Hill towns such as Mussoorie, Nainital, Lansdowne and Ranikhet grew as resorts and cantonments, and the region's people joined the freedom movement and the coolie begar (forced labour) protests of 1921. After Independence the hills were part of Uttar Pradesh; a long popular movement for a separate hill State led to the creation of Uttaranchal on 9 November 2000.",
        "पुराणों में उत्तराखंड केदारखंड (गढ़वाल) और मानसखंड (कुमाऊँ) के रूप में आता है, और बद्रीनाथ व केदारनाथ के धाम आदि शंकराचार्य से जुड़े हैं, जिनके बारे में माना जाता है कि उन्होंने 8वीं सदी में इनका पुनरुद्धार किया। लगभग 7वीं से 11वीं सदी तक कत्यूरी राजवंश ने कत्यूर घाटी और बैजनाथ से इस क्षेत्र के बड़े भाग पर शासन किया और जागेश्वर व बैजनाथ जैसे मंदिर बनवाए। बाद में चंद राजाओं ने चंपावत और फिर अल्मोड़ा से कुमाऊँ पर शासन किया, और पंवार (परमार) वंश ने अलकनंदा किनारे श्रीनगर को राजधानी बनाकर गढ़वाल को एक किया।\n\nलगभग 1790–1804 में नेपाल के गोरखों ने दोनों राज्यों पर क़ब्ज़ा कर लिया; 1814–16 के आंग्ल-गोरखा युद्ध के बाद अंग्रेज़ों ने कुमाऊँ और पूर्वी गढ़वाल को अपने राज्य में मिला लिया, जबकि टिहरी गढ़वाल 1949 तक रियासत बना रहा। मसूरी, नैनीताल, लैंसडाउन और रानीखेत जैसे पहाड़ी नगर सैरगाहों और छावनियों के रूप में बढ़े, और क्षेत्र के लोग स्वतंत्रता आंदोलन और 1921 के कुली बेगार (बेगार प्रथा) विरोधी आंदोलन में शामिल हुए। स्वतंत्रता के बाद पहाड़ उत्तर प्रदेश का हिस्सा रहे; अलग पर्वतीय राज्य के लिए लंबे जन आंदोलन के बाद 9 नवंबर 2000 को उत्तरांचल बना।",
        "पुराणांत उत्तराखंड केदारखंड (गढवाल) व मानसखंड (कुमाऊँ) म्हणून येतो, आणि बद्रीनाथ व केदारनाथची धामे आदि शंकराचार्यांशी जोडलेली आहेत, ज्यांनी आठव्या शतकात त्यांचे पुनरुज्जीवन केले असे मानले जाते. सुमारे सातव्या ते अकराव्या शतकापर्यंत कत्यूरी राजवंशाने कत्यूर खोरे व बैजनाथहून या प्रदेशाच्या मोठ्या भागावर राज्य केले आणि जागेश्वर व बैजनाथसारखी मंदिरे बांधली. नंतर चंद राजांनी चंपावत व नंतर अल्मोड्याहून कुमाऊँवर राज्य केले, आणि पंवार (परमार) घराण्याने अलकनंदेकाठच्या श्रीनगरला राजधानी करून गढवाल एकत्र केले.\n\nसुमारे 1790–1804 मध्ये नेपाळच्या गुरख्यांनी दोन्ही राज्ये जिंकली; 1814–16 च्या इंग्रज-गुरखा युद्धानंतर इंग्रजांनी कुमाऊँ व पूर्व गढवाल आपल्या राज्यात सामील केले, तर टिहरी गढवाल 1949 पर्यंत संस्थान राहिले. मसुरी, नैनीताल, लॅन्सडाउन व राणीखेतसारखी डोंगरी शहरे विश्रांतिस्थळे व छावण्या म्हणून वाढली, आणि प्रदेशातील लोक स्वातंत्र्यलढ्यात व 1921 च्या कुली बेगार (वेठबिगारी) विरोधी आंदोलनात सहभागी झाले. स्वातंत्र्यानंतर डोंगरी भाग उत्तर प्रदेशचा भाग राहिला; स्वतंत्र डोंगरी राज्यासाठीच्या दीर्घ जनआंदोलनानंतर 9 नोव्हेंबर 2000 रोजी उत्तरांचलची निर्मिती झाली."),
        conf="Editorial"),
    timeline([
        ev("gurkha", 1804, L("1804", "1804", "1804"), L("Gurkhas conquer Garhwal", "गोरखों ने गढ़वाल जीता", "गुरख्यांनी गढवाल जिंकले")),
        ev("sugauli", 1816, L("1816", "1816", "1816"), L("Treaty of Sugauli; British take Kumaon and Garhwal", "सुगौली की संधि; अंग्रेज़ों ने कुमाऊँ और गढ़वाल लिया", "सुगौलीचा तह; इंग्रजांनी कुमाऊँ व गढवाल घेतले")),
        ev("begar", 1921, L("January 1921", "जनवरी 1921", "जानेवारी 1921"), L("Coolie begar movement at Bageshwar", "बागेश्वर में कुली बेगार आंदोलन", "बागेश्वर येथे कुली बेगार आंदोलन")),
        ev("tehri", 1949, L("1949", "1949", "1949"), L("Tehri Garhwal state merges with Uttar Pradesh", "टिहरी गढ़वाल रियासत का उत्तर प्रदेश में विलय", "टिहरी गढवाल संस्थानाचे उत्तर प्रदेशात विलीनीकरण")),
        ev("chipko", 1974, L("March 1974", "मार्च 1974", "मार्च 1974"), L("Women of Reni village protect their forest — the Chipko movement", "रैणी गाँव की महिलाओं ने अपना जंगल बचाया — चिपको आंदोलन", "रैणी गावच्या स्त्रियांनी आपले जंगल वाचवले — चिपको आंदोलन")),
        ev("state", 2000, L("9 November 2000", "9 नवंबर 2000", "9 नोव्हेंबर 2000"), L("Uttaranchal created", "उत्तरांचल का गठन", "उत्तरांचलची निर्मिती")),
        ev("rename", 2007, L("1 January 2007", "1 जनवरी 2007", "1 जानेवारी 2007"), L("Renamed Uttarakhand", "नाम बदलकर उत्तराखंड", "नाव बदलून उत्तराखंड")),
        ev("kedar", 2013, L("June 2013", "जून 2013", "जून 2013"), L("Kedarnath flood disaster", "केदारनाथ बाढ़ आपदा", "केदारनाथ पूर आपत्ती")),
        ev("cm2022", 2022, L("23 March 2022", "23 मार्च 2022", "23 मार्च 2022"), L("Pushkar Singh Dhami sworn in for a second term", "पुष्कर सिंह धामी ने दूसरी बार शपथ ली", "पुष्करसिंह धामी यांचा दुसऱ्यांदा शपथविधी")),
    ]),
    lst("heritage", [
        it3("jageshwar", "Jageshwar temple group, Almora", "जागेश्वर मंदिर समूह, अल्मोड़ा", "जागेश्वर मंदिरसमूह, अल्मोडा", m=("Katyuri and Chand era", "कत्यूरी और चंद काल", "कत्यूरी व चंद काळ")),
        it3("baijnath", "Baijnath temples, Bageshwar", "बैजनाथ मंदिर, बागेश्वर", "बैजनाथ मंदिरे, बागेश्वर", m=("Katyuri capital", "कत्यूरी राजधानी", "कत्यूरी राजधानी")),
        it3("kedarnath", "Kedarnath temple", "केदारनाथ मंदिर", "केदारनाथ मंदिर", m=("Jyotirlinga", "ज्योतिर्लिंग", "ज्योतिर्लिंग")),
        it3("badrinath", "Badrinath temple", "बद्रीनाथ मंदिर", "बद्रीनाथ मंदिर", m=("One of the Char Dham", "चार धाम में से एक", "चार धामांपैकी एक")),
        it3("lakhamandal", "Lakhamandal", "लाखामंडल", "लाखामंडल", m=("Ancient Shiva shrine, Jaunsar", "प्राचीन शिव धाम, जौनसार", "प्राचीन शिवमंदिर, जौनसार")),
        it3("fri", "Forest Research Institute, Dehradun", "वन अनुसंधान संस्थान, देहरादून", "वन संशोधन संस्था, डेहराडून", m=("Colonial-era building", "औपनिवेशिक काल का भवन", "वसाहतकालीन इमारत")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("uk mod1 ok")
