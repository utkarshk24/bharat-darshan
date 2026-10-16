"""Bihar modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-BR"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
br = read("regions/IN-BR.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Bihar lies in the eastern Gangetic plain, with Nepal to the north and Jharkhand to the south. The Ganga flows through it from west to east, dividing the flood-prone plains of north Bihar, watered by Himalayan rivers such as the Gandak and the Kosi, from the drier south. With 10.41 crore people at the 2011 Census on just 94,163 km², it is the most densely populated State. Patna, the capital, stands on the site of ancient Pataliputra; Gaya, Bhagalpur, Muzaffarpur and Darbhanga are other large cities.\n\nBihar became a separate province in 1912, when it was carved out of the Bengal Presidency, and took its present shape on 15 November 2000, when Jharkhand was formed from its southern districts. Hindi is the official language and Urdu the second official language; Bhojpuri, Maithili and Magahi are widely spoken.",
        "बिहार पूर्वी गंगा के मैदान में स्थित है, जिसके उत्तर में नेपाल और दक्षिण में झारखंड है। गंगा इसमें पश्चिम से पूर्व बहती है और गंडक व कोसी जैसी हिमालयी नदियों से सिंचित उत्तर बिहार के बाढ़-प्रवण मैदानों को अपेक्षाकृत सूखे दक्षिण से अलग करती है। 2011 की जनगणना में केवल 94,163 वर्ग किमी पर 10.41 करोड़ लोगों के साथ यह सबसे घनी आबादी वाला राज्य है। राजधानी पटना प्राचीन पाटलिपुत्र के स्थान पर बसी है; गया, भागलपुर, मुज़फ़्फ़रपुर और दरभंगा अन्य बड़े शहर हैं।\n\nबिहार 1912 में बंगाल प्रेसीडेंसी से अलग होकर एक अलग प्रांत बना, और 15 नवंबर 2000 को, जब इसके दक्षिणी ज़िलों से झारखंड बना, इसने अपना वर्तमान रूप लिया। हिंदी राजभाषा और उर्दू दूसरी राजभाषा है; भोजपुरी, मैथिली और मगही व्यापक रूप से बोली जाती हैं।",
        "बिहार पूर्व गंगेच्या मैदानात असून त्याच्या उत्तरेला नेपाळ व दक्षिणेला झारखंड आहे. गंगा त्यातून पश्चिमेकडून पूर्वेकडे वाहते आणि गंडक व कोसीसारख्या हिमालयीन नद्यांनी भिजलेल्या उत्तर बिहारच्या पूरप्रवण मैदानांना तुलनेने कोरड्या दक्षिणेपासून वेगळे करते. 2011 च्या जनगणनेनुसार केवळ 94,163 चौ.किमी क्षेत्रावर 10.41 कोटी लोकांसह हे सर्वाधिक दाट लोकवस्तीचे राज्य आहे. राजधानी पाटणा प्राचीन पाटलिपुत्राच्या जागी वसली आहे; गया, भागलपूर, मुझफ्फरपूर व दरभंगा ही इतर मोठी शहरे आहेत.\n\n1912 मध्ये बंगाल प्रांतातून वेगळे होऊन बिहार स्वतंत्र प्रांत बनला, आणि 15 नोव्हेंबर 2000 रोजी त्याच्या दक्षिणेकडील जिल्ह्यांतून झारखंड बनल्यावर त्याला सध्याचे स्वरूप मिळाले. हिंदी ही राजभाषा व उर्दू दुसरी राजभाषा आहे; भोजपुरी, मैथिली व मगही मोठ्या प्रमाणावर बोलल्या जातात."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Bihar is where much of early Indian history was made. The Buddha attained enlightenment at Bodh Gaya, Mahavira was born near Vaishali, and the Magadha empires of the Mauryas and Guptas ruled from Pataliputra. The ruins of Nalanda, one of the world's oldest universities, and the Mahabodhi temple are UNESCO World Heritage Sites, and Patna Sahib is the birthplace of Guru Gobind Singh. Chhath, the festival of the setting and rising sun, is Bihar's great celebration, and Madhubani painting, Bhagalpur silk, Mithila makhana and Shahi litchi are known across India.",
        "बिहार वह भूमि है जहाँ प्रारंभिक भारतीय इतिहास का बड़ा भाग रचा गया। बुद्ध को बोधगया में ज्ञान प्राप्त हुआ, महावीर का जन्म वैशाली के पास हुआ, और मौर्य व गुप्त साम्राज्यों ने पाटलिपुत्र से शासन किया। दुनिया के सबसे पुराने विश्वविद्यालयों में से एक नालंदा के खंडहर और महाबोधि मंदिर यूनेस्को विश्व धरोहर स्थल हैं, और पटना साहिब गुरु गोविंद सिंह का जन्मस्थान है। डूबते और उगते सूर्य का पर्व छठ बिहार का महान उत्सव है, और मधुबनी चित्रकला, भागलपुरी रेशम, मिथिला मखाना और शाही लीची पूरे भारत में प्रसिद्ध हैं।",
        "बिहार ही अशी भूमी आहे जिथे प्राचीन भारतीय इतिहासाचा मोठा भाग घडला. बुद्धांना बोधगया येथे ज्ञानप्राप्ती झाली, महावीरांचा जन्म वैशालीजवळ झाला, आणि मौर्य व गुप्त साम्राज्यांनी पाटलिपुत्राहून राज्य केले. जगातील सर्वांत जुन्या विद्यापीठांपैकी नालंदाचे अवशेष आणि महाबोधी मंदिर ही युनेस्को जागतिक वारसा स्थळे आहेत, आणि पाटणा साहिब हे गुरु गोविंदसिंहांचे जन्मस्थान आहे. मावळत्या व उगवत्या सूर्याचा सण छठ हा बिहारचा मोठा उत्सव आहे, आणि मधुबनी चित्रकला, भागलपुरी रेशीम, मिथिला मखाणा व शाही लिची भारतभर प्रसिद्ध आहेत."),
        title=L("What makes Bihar unique?", "बिहार को ख़ास क्या बनाता है?", "बिहारचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed", "गठन", "निर्मिती"), L("22 March 1912 (Bihar Day); present boundaries from 15 November 2000", "22 मार्च 1912 (बिहार दिवस); वर्तमान सीमाएँ 15 नवंबर 2000 से", "22 मार्च 1912 (बिहार दिन); सध्याच्या सीमा 15 नोव्हेंबर 2000 पासून")],
           [L("Districts / divisions", "ज़िले / प्रमंडल", "जिल्हे / विभाग"), "38 / 9"],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Hindi; Urdu as second official language", "हिंदी; उर्दू दूसरी राजभाषा", "हिंदी; उर्दू दुसरी राजभाषा")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Patna High Court (1916)", "पटना उच्च न्यायालय (1916)", "पाटणा उच्च न्यायालय (1916)")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-BR / BR"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be linked to the State's notifications in review.", "संपादकीय; समीक्षा में राज्य की अधिसूचनाओं से जोड़ा जाएगा।", "संपादकीय; तपासणीत राज्याच्या अधिसूचनांशी जोडले जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Almost all of Bihar is flat alluvial plain. North of the Ganga, rivers from Nepal — the Ghaghara, Gandak, Burhi Gandak, Bagmati, Kamla, Kosi and Mahananda — cross the plain and often shift their courses; the Kosi, which has moved more than 100 km westward over the past two centuries, was long called the 'sorrow of Bihar'. In the far north-west the Someshwar hills, an outlier of the Shivaliks, hold the Valmiki forests. South of the Ganga, the Son, Punpun and Phalgu flow from the Chota Nagpur plateau, and low rocky hills rise at Rajgir, Gaya and Kaimur. Bihar is land-locked; the Ganga is National Waterway 1, with a terminal at Patna.",
        "बिहार का लगभग पूरा भाग समतल जलोढ़ मैदान है। गंगा के उत्तर में नेपाल से आने वाली नदियाँ — घाघरा, गंडक, बूढ़ी गंडक, बागमती, कमला, कोसी और महानंदा — मैदान को पार करती हैं और अक्सर अपना मार्ग बदलती हैं; पिछली दो सदियों में 100 किमी से अधिक पश्चिम खिसक चुकी कोसी को लंबे समय तक 'बिहार का शोक' कहा गया। सुदूर उत्तर-पश्चिम में शिवालिक की एक शाखा सोमेश्वर पहाड़ियों में वाल्मीकि के वन हैं। गंगा के दक्षिण में सोन, पुनपुन और फल्गु छोटा नागपुर पठार से आती हैं, और राजगीर, गया और कैमूर में नीची पथरीली पहाड़ियाँ हैं। बिहार भू-आबद्ध है; गंगा राष्ट्रीय जलमार्ग 1 है, जिसका एक टर्मिनल पटना में है।",
        "बिहारचा जवळपास संपूर्ण भाग सपाट गाळाचे मैदान आहे. गंगेच्या उत्तरेला नेपाळमधून येणाऱ्या नद्या — घागरा, गंडक, बूढी गंडक, बागमती, कमला, कोसी व महानंदा — मैदान ओलांडतात आणि अनेकदा आपले पात्र बदलतात; गेल्या दोन शतकांत 100 किमीहून अधिक पश्चिमेकडे सरकलेल्या कोसीला दीर्घकाळ 'बिहारचे दुःख' म्हटले गेले. अगदी वायव्येला शिवालिकची एक शाखा असलेल्या सोमेश्वर डोंगरांत वाल्मीकीची जंगले आहेत. गंगेच्या दक्षिणेला सोन, पुनपुन व फल्गू छोटा नागपूर पठारावरून येतात, आणि राजगीर, गया व कैमूर येथे कमी उंचीचे खडकाळ डोंगर आहेत. बिहार भूवेष्टित आहे; गंगा हा राष्ट्रीय जलमार्ग 1 असून त्याचे एक टर्मिनल पाटण्यात आहे."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), br["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("np", "Nepal (north)", "नेपाल (उत्तर)", "नेपाळ (उत्तर)"), it3("wb", "West Bengal (east)", "पश्चिम बंगाल (पूर्व)", "पश्चिम बंगाल (पूर्व)"),
        it3("jh", "Jharkhand (south)", "झारखंड (दक्षिण)", "झारखंड (दक्षिण)"), it3("up", "Uttar Pradesh (west)", "उत्तर प्रदेश (पश्चिम)", "उत्तर प्रदेश (पश्चिम)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("ganga", "Ganga", "गंगा", "गंगा", d=("Flows west to east past Buxar, Patna, Munger and Bhagalpur.", "बक्सर, पटना, मुंगेर और भागलपुर से होकर पश्चिम से पूर्व बहती है।", "बक्सर, पाटणा, मुंगेर व भागलपूरवरून पश्चिमेकडून पूर्वेकडे वाहते.")),
        it3("kosi", "Kosi", "कोसी", "कोसी", d=("Himalayan river notorious for floods and shifting courses.", "बाढ़ और बदलते मार्ग के लिए कुख्यात हिमालयी नदी।", "पूर व बदलत्या पात्रासाठी कुप्रसिद्ध हिमालयीन नदी.")),
        it3("gandak", "Gandak", "गंडक", "गंडक", d=("Joins the Ganga opposite Patna at Hajipur.", "पटना के सामने हाजीपुर में गंगा से मिलती है।", "पाटण्यासमोर हाजीपूर येथे गंगेला मिळते.")),
        it3("son", "Son", "सोन", "सोन", d=("Southern tributary from Madhya Pradesh.", "मध्य प्रदेश से आने वाली दक्षिणी सहायक नदी।", "मध्य प्रदेशातून येणारी दक्षिणेकडील उपनदी.")),
        it3("bagmati", "Bagmati", "बागमती", "बागमती", d=("Flows from the Kathmandu valley across Mithila.", "काठमांडू घाटी से मिथिला होकर बहती है।", "काठमांडू खोऱ्यातून मिथिलामार्गे वाहते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point — official elevation", "सर्वोच्च बिंदु — आधिकारिक ऊँचाई", "सर्वोच्च शिखर — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Flood-prone area", "बाढ़-प्रवण क्षेत्र", "पूरप्रवण क्षेत्र"), "india-gov", "Bihar Water Resources / Disaster Management Department."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Bihar has a humid subtropical climate. Summers (April–June) are hot, with the dry west wind called loo in the south and west; the south-west monsoon (mid-June to September) brings heavy rain, especially in the north-east near Kishanganj and the foothills, and often floods. Winters (December–February) are cool, with dense fog and occasional cold waves across the plains.",
        "बिहार में आर्द्र उपोष्ण जलवायु है। गर्मियाँ (अप्रैल–जून) गर्म होती हैं, और दक्षिण व पश्चिम में लू चलती है; दक्षिण-पश्चिम मानसून (मध्य जून से सितंबर) भारी वर्षा लाता है, विशेषकर उत्तर-पूर्व में किशनगंज और तराई के पास, और अक्सर बाढ़ भी। सर्दियाँ (दिसंबर–फ़रवरी) ठंडी होती हैं, मैदानों में घना कोहरा और कभी-कभी शीतलहर रहती है।",
        "बिहारमध्ये दमट उपोष्ण हवामान आहे. उन्हाळा (एप्रिल–जून) उष्ण असतो, आणि दक्षिण व पश्चिमेत लू नावाचा कोरडा पश्चिमी वारा वाहतो; नैर्ऋत्य मान्सून (जूनच्या मध्यापासून सप्टेंबरपर्यंत) मुसळधार पाऊस आणतो, विशेषतः ईशान्येला किशनगंज व पायथ्याच्या प्रदेशात, आणि अनेकदा पूरही. हिवाळा (डिसेंबर–फेब्रुवारी) थंड असतो, मैदानांत दाट धुके व कधीकधी थंडीची लाट असते."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Patna", "पटना", "पाटणा"), "lat": 25.5941, "lon": 85.1376},
        {"name": L("Gaya", "गया", "गया"), "lat": 24.7955, "lon": 85.0002},
        {"name": L("Bhagalpur", "भागलपुर", "भागलपूर"), "lat": 25.2425, "lon": 86.9842},
        {"name": L("Darbhanga", "दरभंगा", "दरभंगा"), "lat": 26.1542, "lon": 85.8918},
    ]},
    lst("best", [
        it3("winter", "October to March", "अक्टूबर से मार्च", "ऑक्टोबर ते मार्च", d=("Best for Bodh Gaya, Nalanda and Rajgir; Chhath in Oct–Nov; Sonepur fair in November.", "बोधगया, नालंदा और राजगीर के लिए सबसे अच्छा; अक्टूबर–नवंबर में छठ; नवंबर में सोनपुर मेला।", "बोधगया, नालंदा व राजगीरसाठी उत्तम; ऑक्टो.–नोव्हें.मध्ये छठ; नोव्हेंबरमध्ये सोनपूर जत्रा.")),
        it3("summer", "April to June", "अप्रैल से जून", "एप्रिल ते जून", d=("Hot; litchi season in Muzaffarpur in May–June.", "गर्मी; मई–जून में मुज़फ़्फ़रपुर में लीची का मौसम।", "उष्ण; मे–जूनमध्ये मुझफ्फरपूरमध्ये लिचीचा हंगाम.")),
        it3("monsoon", "July to September", "जुलाई से सितंबर", "जुलै ते सप्टेंबर", d=("Floods in the north; Shravani Mela pilgrimage from Sultanganj.", "उत्तर में बाढ़; सुल्तानगंज से श्रावणी मेला यात्रा।", "उत्तरेत पूर; सुलतानगंजहून श्रावणी मेळा यात्रा.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (Bihar sub-division)", "सामान्य वार्षिक वर्षा (बिहार उप-मंडल)", "सरासरी वार्षिक पाऊस (बिहार उपविभाग)"), "imd", "IMD rainfall statistics."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Bihar's life follows the river and the seasons. Ghats along the Ganga in Patna and Bhagalpur fill at dawn, and at Chhath millions stand in rivers and ponds to offer prayers to the sun. Villages of north Bihar are green with paddy, maize and mango and litchi orchards, ponds full of fish and makhana; the south has stony hills, Buddhist and Jain pilgrimage towns and busy market towns. Litti chokha and sattu are everyday fare, and Bhojpuri, Maithili and Magahi songs fill weddings and festivals. Many families have members working in other States or abroad, and homecomings at Chhath and Holi are a big part of the year.",
        "बिहार का जीवन नदी और मौसमों के साथ चलता है। पटना और भागलपुर में गंगा के घाट भोर में भर जाते हैं, और छठ पर लाखों लोग नदियों और तालाबों में खड़े होकर सूर्य को अर्घ्य देते हैं। उत्तर बिहार के गाँव धान, मक्का, आम और लीची के बाग़ों, मछली और मखाने से भरे तालाबों से हरे-भरे हैं; दक्षिण में पथरीली पहाड़ियाँ, बौद्ध और जैन तीर्थ नगर और व्यस्त बाज़ार कस्बे हैं। लिट्टी चोखा और सत्तू रोज़ का भोजन हैं, और शादियों और त्योहारों में भोजपुरी, मैथिली और मगही गीत गूँजते हैं। बहुत से परिवारों के सदस्य दूसरे राज्यों या विदेश में काम करते हैं, और छठ और होली पर घर लौटना साल का बड़ा हिस्सा है।",
        "बिहारचे जीवन नदी व ऋतूंनुसार चालते. पाटणा व भागलपूरमधील गंगेचे घाट पहाटे भरून जातात, आणि छठला लाखो लोक नद्या व तलावांत उभे राहून सूर्याला अर्घ्य देतात. उत्तर बिहारची गावे भात, मका, आंबा व लिचीच्या बागा, मासे व मखाण्याने भरलेल्या तलावांनी हिरवीगार आहेत; दक्षिणेला खडकाळ डोंगर, बौद्ध व जैन तीर्थनगरे आणि गजबजलेली बाजारपेठेची गावे आहेत. लिट्टी चोखा व सत्तू हे रोजचे अन्न आहे, आणि लग्ने व सणांत भोजपुरी, मैथिली व मगही गाणी गुंजतात. अनेक कुटुंबांचे सदस्य इतर राज्यांत किंवा परदेशात काम करतात, आणि छठ व होळीला घरी परतणे हा वर्षाचा मोठा भाग आहे."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Bihar had 10.41 crore people at the 2011 Census — the third-largest population among the States — and, at about 1,106 per km², the highest density. The sex ratio was 918 women per 1,000 men and the child sex ratio 935. Literacy was 61.8%, the lowest of any State, with a large gap between men and women. Scheduled Castes made up 15.9% of the population; Scheduled Tribes, most of whom live in present-day Jharkhand, were only 1.3%.\n\nHindi is the official language and Urdu the second official language. At home, most people speak Bhojpuri in the west, Maithili in Mithila in the north, Magahi around Patna and Gaya, and Angika and Bajjika in other regions; Maithili is one of India's 22 scheduled languages.",
        "2011 की जनगणना में बिहार की जनसंख्या 10.41 करोड़ थी — राज्यों में तीसरी सबसे बड़ी — और लगभग 1,106 प्रति वर्ग किमी के साथ घनत्व सबसे अधिक। लिंगानुपात प्रति 1,000 पुरुषों पर 918 महिलाएँ और शिशु लिंगानुपात 935 था। साक्षरता 61.8% थी, जो किसी भी राज्य में सबसे कम है, और पुरुषों व महिलाओं के बीच बड़ा अंतर था। अनुसूचित जातियाँ जनसंख्या का 15.9% थीं; अनुसूचित जनजातियाँ, जिनमें से अधिकांश अब झारखंड में रहती हैं, केवल 1.3% थीं।\n\nहिंदी राजभाषा और उर्दू दूसरी राजभाषा है। घरों में अधिकांश लोग पश्चिम में भोजपुरी, उत्तर के मिथिला में मैथिली, पटना और गया के आसपास मगही, और अन्य क्षेत्रों में अंगिका व बज्जिका बोलते हैं; मैथिली भारत की 22 अनुसूचित भाषाओं में से एक है।",
        "2011 च्या जनगणनेनुसार बिहारची लोकसंख्या 10.41 कोटी होती — राज्यांमध्ये तिसरी सर्वांत मोठी — आणि सुमारे 1,106 प्रति चौ.किमीसह घनता सर्वाधिक. दर 1,000 पुरुषांमागे 918 स्त्रिया व बाल लिंग गुणोत्तर 935 होते. साक्षरता 61.8% होती — कोणत्याही राज्यातील सर्वांत कमी — आणि पुरुष व स्त्रियांमध्ये मोठी तफावत होती. अनुसूचित जाती लोकसंख्येच्या 15.9% होत्या; अनुसूचित जमाती, ज्यांपैकी बहुतेक आता झारखंडमध्ये राहतात, केवळ 1.3% होत्या.\n\nहिंदी ही राजभाषा व उर्दू दुसरी राजभाषा आहे. घरांत बहुतेक लोक पश्चिमेत भोजपुरी, उत्तरेकडील मिथिलेत मैथिली, पाटणा व गयाभोवती मगही, आणि इतर भागांत अंगिका व बज्जिका बोलतात; मैथिली ही भारताच्या 22 अनुसूचित भाषांपैकी एक आहे."),
        sources=["census", "es-india", "dl-planning"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), br["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), br["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(919, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), br["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(942, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), br["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), br["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(15.9, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 165.67 lakh people."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(1.3, "%", "2011", "census", "dl-planning", SCST, note="Same table: 13.36 lakh people."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("hi", "Hindi", "हिंदी", "हिंदी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("ur", "Urdu", "उर्दू", "उर्दू", m=("Second official language", "दूसरी राजभाषा", "दुसरी राजभाषा")),
        it3("bho", "Bhojpuri", "भोजपुरी", "भोजपुरी"), it3("mai", "Maithili", "मैथिली", "मैथिली", m=("Scheduled language", "अनुसूचित भाषा", "अनुसूचित भाषा")),
        it3("mag", "Magahi", "मगही", "मगही"), it3("anp", "Angika", "अंगिका", "अंगिका"), it3("vjj", "Bajjika", "बज्जिका", "बज्जिका"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Final Population Totals for Bihar."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Caste-based survey 2022-23 (State)", "जाति आधारित सर्वेक्षण 2022-23 (राज्य)", "जातिनिहाय सर्वेक्षण 2022-23 (राज्य)"), "india-gov", "State government report; to be shown without commentary if linked."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Bihar was the heart of ancient Magadha. From Rajgir and later Pataliputra (Patna), the Haryanka, Nanda, Maurya and Gupta dynasties built India's first great empires; Chandragupta Maurya, guided by Chanakya, and Ashoka ruled from here. Vaishali was home to one of the earliest known republics, the Licchavi confederacy. Siddhartha Gautama became the Buddha at Bodh Gaya, and Mahavira, born near Vaishali, attained nirvana at Pawapuri. Nalanda and Vikramashila were great Buddhist universities until the 12th–13th centuries, and Aryabhata worked at Kusumapura near Pataliputra.\n\nSher Shah Suri, from Sasaram, briefly drove out the Mughals in the 16th century, and Guru Gobind Singh was born in Patna in 1666. The Battle of Buxar (1764) confirmed East India Company control of Bihar and Bengal. In 1857 Kunwar Singh of Jagdishpur led the revolt, and in 1917 Gandhi's Champaran Satyagraha was his first in India. Bihar became a province in 1912; Orissa separated in 1936 and Jharkhand in 2000. The JP movement of 1974, led by Jayaprakash Narayan, shook national politics.",
        "बिहार प्राचीन मगध का हृदय था। राजगीर और बाद में पाटलिपुत्र (पटना) से हर्यंक, नंद, मौर्य और गुप्त वंशों ने भारत के पहले महान साम्राज्य बनाए; चाणक्य के मार्गदर्शन में चंद्रगुप्त मौर्य और अशोक ने यहीं से शासन किया। वैशाली सबसे प्रारंभिक ज्ञात गणराज्यों में से एक, लिच्छवि संघ का घर थी। सिद्धार्थ गौतम बोधगया में बुद्ध बने, और वैशाली के पास जन्मे महावीर ने पावापुरी में निर्वाण प्राप्त किया। नालंदा और विक्रमशिला 12वीं–13वीं सदी तक महान बौद्ध विश्वविद्यालय रहे, और आर्यभट ने पाटलिपुत्र के पास कुसुमपुर में काम किया।\n\nसासाराम के शेरशाह सूरी ने 16वीं सदी में कुछ समय के लिए मुग़लों को खदेड़ दिया, और 1666 में पटना में गुरु गोविंद सिंह का जन्म हुआ। बक्सर के युद्ध (1764) ने बिहार और बंगाल पर ईस्ट इंडिया कंपनी का नियंत्रण पक्का किया। 1857 में जगदीशपुर के कुंवर सिंह ने विद्रोह का नेतृत्व किया, और 1917 में गांधी का चंपारण सत्याग्रह भारत में उनका पहला सत्याग्रह था। बिहार 1912 में प्रांत बना; 1936 में उड़ीसा और 2000 में झारखंड अलग हुए। 1974 में जयप्रकाश नारायण के नेतृत्व वाले जेपी आंदोलन ने राष्ट्रीय राजनीति को हिला दिया।",
        "बिहार हे प्राचीन मगधाचे हृदय होते. राजगीर व नंतर पाटलिपुत्र (पाटणा) येथून हर्यंक, नंद, मौर्य व गुप्त घराण्यांनी भारतातील पहिली महान साम्राज्ये उभारली; चाणक्याच्या मार्गदर्शनाखाली चंद्रगुप्त मौर्य व अशोकाने इथूनच राज्य केले. वैशाली हे सर्वांत प्रारंभीच्या ज्ञात गणराज्यांपैकी एक, लिच्छवी संघाचे घर होते. सिद्धार्थ गौतम बोधगया येथे बुद्ध झाले, आणि वैशालीजवळ जन्मलेल्या महावीरांना पावापुरी येथे निर्वाण प्राप्त झाले. नालंदा व विक्रमशिला ही बाराव्या–तेराव्या शतकापर्यंत महान बौद्ध विद्यापीठे होती, आणि आर्यभटाने पाटलिपुत्राजवळील कुसुमपुर येथे कार्य केले.\n\nसासारामच्या शेरशहा सुरीने सोळाव्या शतकात काही काळ मुघलांना हुसकावून लावले, आणि 1666 मध्ये पाटण्यात गुरु गोविंदसिंहांचा जन्म झाला. बक्सरच्या लढाईने (1764) बिहार व बंगालवर ईस्ट इंडिया कंपनीचे नियंत्रण पक्के केले. 1857 मध्ये जगदीशपूरच्या कुंवरसिंहांनी उठावाचे नेतृत्व केले, आणि 1917 चा गांधीजींचा चंपारण सत्याग्रह हा भारतातील त्यांचा पहिला सत्याग्रह होता. बिहार 1912 मध्ये प्रांत बनला; 1936 मध्ये ओरिसा व 2000 मध्ये झारखंड वेगळे झाले. 1974 मध्ये जयप्रकाश नारायण यांच्या नेतृत्वाखालील जेपी आंदोलनाने राष्ट्रीय राजकारण हादरवले."),
        conf="Editorial"),
    timeline([
        ev("buddha", -528, L("c. 5th century BCE", "लगभग ई.पू. 5वीं सदी", "सुमारे इ.स.पू. पाचवे शतक"), L("The Buddha's enlightenment at Bodh Gaya", "बोधगया में बुद्ध को ज्ञान प्राप्ति", "बोधगया येथे बुद्धांना ज्ञानप्राप्ती")),
        ev("maurya", -321, L("c. 321 BCE", "लगभग 321 ई.पू.", "सुमारे इ.स.पू. 321"), L("Maurya empire founded at Pataliputra", "पाटलिपुत्र में मौर्य साम्राज्य की स्थापना", "पाटलिपुत्र येथे मौर्य साम्राज्याची स्थापना")),
        ev("nalanda", 427, L("5th century CE", "5वीं सदी ई.", "इसवी सन पाचवे शतक"), L("Nalanda mahavihara flourishes", "नालंदा महाविहार का उत्कर्ष", "नालंदा महाविहाराचा उत्कर्ष")),
        ev("gobind", 1666, L("1666", "1666", "1666"), L("Guru Gobind Singh born in Patna", "पटना में गुरु गोविंद सिंह का जन्म", "पाटण्यात गुरु गोविंदसिंहांचा जन्म")),
        ev("buxar", 1764, L("1764", "1764", "1764"), L("Battle of Buxar", "बक्सर का युद्ध", "बक्सरची लढाई")),
        ev("province", 1912, L("22 March 1912", "22 मार्च 1912", "22 मार्च 1912"), L("Bihar separated from Bengal (Bihar Day)", "बिहार बंगाल से अलग (बिहार दिवस)", "बिहार बंगालपासून वेगळा (बिहार दिन)")),
        ev("champaran", 1917, L("1917", "1917", "1917"), L("Champaran Satyagraha", "चंपारण सत्याग्रह", "चंपारण सत्याग्रह")),
        ev("quake", 1934, L("15 January 1934", "15 जनवरी 1934", "15 जानेवारी 1934"), L("Great Bihar–Nepal earthquake", "बिहार–नेपाल का महान भूकंप", "बिहार–नेपाळचा महाभूकंप")),
        ev("jharkhand", 2000, L("15 November 2000", "15 नवंबर 2000", "15 नोव्हेंबर 2000"), L("Jharkhand separated", "झारखंड अलग हुआ", "झारखंड वेगळे")),
        ev("cm2026", 2026, L("15 April 2026", "15 अप्रैल 2026", "15 एप्रिल 2026"), L("Samrat Choudhary sworn in as Chief Minister", "सम्राट चौधरी ने मुख्यमंत्री पद की शपथ ली", "सम्राट चौधरी यांचा मुख्यमंत्रिपदाचा शपथविधी")),
    ]),
    lst("heritage", [
        it3("mahabodhi", "Mahabodhi Temple Complex, Bodh Gaya", "महाबोधि मंदिर परिसर, बोधगया", "महाबोधी मंदिर संकुल, बोधगया", m=("UNESCO 2002", "यूनेस्को 2002", "युनेस्को 2002"), url=UNESCO, src="unesco-whc"),
        it3("nalanda", "Archaeological Site of Nalanda Mahavihara", "नालंदा महाविहार पुरातात्विक स्थल", "नालंदा महाविहार पुरातत्त्व स्थळ", m=("UNESCO 2016", "यूनेस्को 2016", "युनेस्को 2016"), url=UNESCO, src="unesco-whc"),
        it3("vikramshila", "Vikramashila ruins", "विक्रमशिला के अवशेष", "विक्रमशिलेचे अवशेष", m=("Bhagalpur", "भागलपुर", "भागलपूर")),
        it3("vaishali", "Vaishali (Ashokan pillar)", "वैशाली (अशोक स्तंभ)", "वैशाली (अशोक स्तंभ)", m=("Licchavi republic", "लिच्छवि गणराज्य", "लिच्छवी गणराज्य")),
        it3("shershah", "Sher Shah Suri's tomb, Sasaram", "शेरशाह सूरी का मक़बरा, सासाराम", "शेरशहा सुरीची कबर, सासाराम", m=("16th century", "16वीं सदी", "सोळावे शतक")),
        it3("patnasahib", "Takht Sri Harmandir Sahib, Patna", "तख़्त श्री हरमंदिर साहिब, पटना", "तख्त श्री हरमंदिर साहिब, पाटणा", m=("Birthplace of Guru Gobind Singh", "गुरु गोविंद सिंह का जन्मस्थान", "गुरु गोविंदसिंहांचे जन्मस्थान")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("br mod1 ok")
