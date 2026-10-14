"""Uttar Pradesh modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-UP"
UPF = "https://updes.up.nic.in/updes/data/upinfigures/up%20in%20figures-%202022.pdf"
up = read("regions/IN-UP.json")["metrics"]; ind = read("india.json")["metrics"]
NAME = L("Uttar Pradesh", "उत्तर प्रदेश", "उत्तर प्रदेश")
UD = lambda v, unit, note=None, period="2011", ptype="census": dp(v, unit, period, ptype, "up-des", UPF, note=note)

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Uttar Pradesh is India's most populous State, home to almost 20 crore people at the 2011 Census — about one in six Indians. It spreads across the fertile Ganga–Yamuna plain between the Himalayan foothills in the north and the Vindhya and Bundelkhand uplands in the south. Lucknow is the capital; Prayagraj seats the High Court; and Varanasi, Ayodhya, Mathura and Prayagraj are among the most important pilgrimage centres in the country.\n\nThe area was organised by the British as the North-Western Provinces and later the United Provinces of Agra and Oudh; it took the name Uttar Pradesh in January 1950. In 2000 its Himalayan districts were separated to form Uttarakhand. Hindi is the official language and Urdu the second official language.",
        "उत्तर प्रदेश भारत का सबसे अधिक आबादी वाला राज्य है — 2011 की जनगणना में यहाँ लगभग 20 करोड़ लोग थे, यानी हर छह में से एक भारतीय। यह उत्तर में हिमालय की तलहटी और दक्षिण में विंध्य व बुंदेलखंड के पठार के बीच उपजाऊ गंगा–यमुना मैदान में फैला है। लखनऊ राजधानी है; प्रयागराज में उच्च न्यायालय है; और वाराणसी, अयोध्या, मथुरा और प्रयागराज देश के सबसे महत्त्वपूर्ण तीर्थों में हैं।\n\nअंग्रेज़ों ने इस क्षेत्र को पश्चिमोत्तर प्रांत और बाद में आगरा व अवध के संयुक्त प्रांत के रूप में संगठित किया; जनवरी 1950 में इसका नाम उत्तर प्रदेश पड़ा। 2000 में इसके हिमालयी ज़िलों को अलग कर उत्तराखंड बनाया गया। हिंदी राजभाषा है और उर्दू दूसरी राजभाषा।",
        "उत्तर प्रदेश हे भारतातील सर्वाधिक लोकसंख्येचे राज्य आहे — 2011 च्या जनगणनेनुसार इथे जवळपास 20 कोटी लोक होते, म्हणजे दर सहा भारतीयांमागे एक. उत्तरेला हिमालयाच्या पायथ्यापासून दक्षिणेला विंध्य व बुंदेलखंडच्या पठारापर्यंत सुपीक गंगा–यमुना मैदानात ते पसरले आहे. लखनौ ही राजधानी; प्रयागराज येथे उच्च न्यायालय; आणि वाराणसी, अयोध्या, मथुरा व प्रयागराज ही देशातील सर्वांत महत्त्वाच्या तीर्थक्षेत्रांपैकी आहेत.\n\nइंग्रजांनी हा प्रदेश वायव्य प्रांत आणि नंतर आग्रा व अवधचा संयुक्त प्रांत म्हणून संघटित केला; जानेवारी 1950 मध्ये त्याला उत्तर प्रदेश हे नाव मिळाले. 2000 मध्ये त्याचे हिमालयीन जिल्हे वेगळे करून उत्तराखंड निर्माण झाले. हिंदी ही राजभाषा आणि उर्दू दुसरी राजभाषा आहे."),
        sources=["up-des"], conf="Editorial"),
    prose("intro-unique", L(
        "Few regions hold as much of India's story. The Buddha gave his first sermon at Sarnath and died at Kushinagar; Ayodhya and Mathura are central to the Ramayana and the Krishna traditions; the Mughals built the Taj Mahal, Agra Fort and Fatehpur Sikri; and the 1857 uprising was fought out at Meerut, Kanpur, Lucknow and Jhansi. The Kumbh Mela at Prayagraj, at the meeting of the Ganga and Yamuna, is among the largest gatherings of people anywhere. Lucknow's Awadhi cuisine, chikan embroidery and courtly Urdu, Varanasi's silk brocades and music, and Agra's marble inlay are known across the world.",
        "बहुत कम क्षेत्रों में भारत की कहानी का इतना बड़ा हिस्सा समाया है। बुद्ध ने सारनाथ में पहला उपदेश दिया और कुशीनगर में महापरिनिर्वाण पाया; अयोध्या और मथुरा रामायण और कृष्ण परंपराओं के केंद्र हैं; मुग़लों ने ताजमहल, आगरा क़िला और फ़तेहपुर सीकरी बनवाए; और 1857 का विद्रोह मेरठ, कानपुर, लखनऊ और झाँसी में लड़ा गया। गंगा और यमुना के संगम पर प्रयागराज का कुंभ मेला दुनिया के सबसे बड़े जनसमागमों में है। लखनऊ के अवधी व्यंजन, चिकनकारी और नफ़ीस उर्दू, वाराणसी के रेशमी ब्रोकेड और संगीत, और आगरा की संगमरमर पच्चीकारी दुनिया भर में जाने जाते हैं।",
        "भारताच्या कहाणीचा इतका मोठा भाग सामावलेले प्रदेश फार थोडे आहेत. बुद्धांनी सारनाथ येथे पहिले प्रवचन दिले आणि कुशीनगर येथे महापरिनिर्वाण पावले; अयोध्या आणि मथुरा ही रामायण व कृष्ण परंपरांची केंद्रे आहेत; मुघलांनी ताजमहाल, आग्र्याचा किल्ला आणि फतेहपूर सिक्री उभारले; आणि 1857 चा उठाव मेरठ, कानपूर, लखनौ व झाशी येथे लढला गेला. गंगा-यमुनेच्या संगमावर प्रयागराजचा कुंभमेळा हा जगातील सर्वांत मोठ्या जनसमुदायांपैकी एक आहे. लखनौची अवधी खाद्यसंस्कृती, चिकनकारी आणि नजाकतदार उर्दू, वाराणसीचे रेशमी जरीकाम व संगीत, आणि आग्र्याचे संगमरवरी जडावकाम जगभर ओळखले जातात."),
        title=L("What makes Uttar Pradesh unique?", "उत्तर प्रदेश को ख़ास क्या बनाता है?", "उत्तर प्रदेशचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Named Uttar Pradesh", "उत्तर प्रदेश नाम", "उत्तर प्रदेश नाव"), L("24 January 1950 (UP Diwas)", "24 जनवरी 1950 (यूपी दिवस)", "24 जानेवारी 1950 (यूपी दिवस)")],
           [L("Divisions / districts", "मंडल / ज़िले", "विभाग / जिल्हे"), "18 / 75"],
           [L("Tehsils / development blocks", "तहसीलें / विकास खंड", "तहसीली / विकास गट"), "351 / 826"],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Hindi; Urdu (second official language)", "हिंदी; उर्दू (दूसरी राजभाषा)", "हिंदी; उर्दू (दुसरी राजभाषा)")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Allahabad (Prayagraj), with a bench at Lucknow", "इलाहाबाद (प्रयागराज), लखनऊ में खंडपीठ", "अलाहाबाद (प्रयागराज), लखनौ येथे खंडपीठ")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-UP / UP"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          "up-des", UPF, conf="Editorial",
          note=L("Division, district, tehsil and block counts as on 31 March 2022 (Economics & Statistics Division, Government of Uttar Pradesh). Other rows are editorial and will be linked to notifications in review.",
                 "मंडल, ज़िला, तहसील और विकास खंड की संख्या 31 मार्च 2022 की स्थिति में (अर्थ एवं संख्या प्रभाग, उत्तर प्रदेश सरकार)। बाकी पंक्तियाँ संपादकीय हैं; समीक्षा में अधिसूचनाओं से जोड़ी जाएँगी।",
                 "विभाग, जिल्हे, तहसील व विकास गटांची संख्या 31 मार्च 2022 रोजीची (अर्थ व सांख्यिकी विभाग, उत्तर प्रदेश शासन). इतर ओळी संपादकीय असून तपासणीत अधिसूचनांशी जोडल्या जातील.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Most of Uttar Pradesh is a vast, flat alluvial plain built by the Ganga and its tributaries — one of the most densely farmed landscapes on Earth. Along the northern border with Nepal runs the Terai, a belt of tall grassland, sal forest and swamp at the foot of the Himalaya, now protected in Dudhwa and Pilibhit. In the south the land rises into the rocky Bundelkhand plateau and the Vindhya and Kaimur hills around Mirzapur and Sonbhadra, which are drier and less fertile.\n\nThe Ganga enters the plains near Bijnor and flows south-east past Kanpur, Prayagraj and Varanasi. The Yamuna runs parallel to it past Mathura and Agra and joins it at the Triveni Sangam in Prayagraj. Other major rivers — the Ramganga, Gomti, Ghaghara, Rapti, Gandak, Betwa and Ken — feed the system; floods in the eastern districts and dry spells in Bundelkhand are both recurring problems.",
        "उत्तर प्रदेश का अधिकांश भाग गंगा और उसकी सहायक नदियों से बना विशाल, समतल जलोढ़ मैदान है — धरती के सबसे सघन खेती वाले भूदृश्यों में से एक। नेपाल से लगी उत्तरी सीमा के साथ हिमालय की तलहटी में तराई की पट्टी है, जिसमें ऊँची घास, साल के वन और दलदल हैं, जो अब दुधवा और पीलीभीत में संरक्षित हैं। दक्षिण में भूमि बुंदेलखंड के पथरीले पठार और मिर्ज़ापुर व सोनभद्र के आसपास विंध्य और कैमूर पहाड़ियों में उठती है, जो अधिक सूखी और कम उपजाऊ है।\n\nगंगा बिजनौर के पास मैदान में प्रवेश करती है और कानपुर, प्रयागराज और वाराणसी से होकर दक्षिण-पूर्व की ओर बहती है। यमुना मथुरा और आगरा से होकर इसके समानांतर बहती है और प्रयागराज के त्रिवेणी संगम पर इससे मिलती है। अन्य बड़ी नदियाँ — रामगंगा, गोमती, घाघरा, राप्ती, गंडक, बेतवा और केन — इस तंत्र को जल देती हैं; पूर्वी ज़िलों में बाढ़ और बुंदेलखंड में सूखा, दोनों बार-बार आने वाली समस्याएँ हैं।",
        "उत्तर प्रदेशचा बहुतांश भाग गंगा व तिच्या उपनद्यांनी घडवलेले विशाल, सपाट गाळाचे मैदान आहे — पृथ्वीवरील सर्वांत दाट शेती असलेल्या प्रदेशांपैकी एक. नेपाळलगतच्या उत्तर सीमेवर हिमालयाच्या पायथ्याशी तराईचा पट्टा आहे — उंच गवत, सालवृक्षांची वने आणि दलदल — जो आता दुधवा व पिलीभीत येथे संरक्षित आहे. दक्षिणेकडे जमीन बुंदेलखंडच्या खडकाळ पठारात आणि मिर्झापूर व सोनभद्रभोवतीच्या विंध्य व कैमूर डोंगरांत उंचावते, जो भाग अधिक कोरडा व कमी सुपीक आहे.\n\nगंगा बिजनौरजवळ मैदानात प्रवेश करते आणि कानपूर, प्रयागराज व वाराणसीवरून आग्नेयेकडे वाहते. यमुना मथुरा व आग्र्यावरून तिला समांतर वाहते आणि प्रयागराजच्या त्रिवेणी संगमावर तिला मिळते. इतर मोठ्या नद्या — रामगंगा, गोमती, घाघरा, राप्ती, गंडक, बेतवा आणि केन — या प्रणालीला पाणी पुरवतात; पूर्वेकडील जिल्ह्यांत पूर आणि बुंदेलखंडमध्ये दुष्काळ, या दोन्ही वारंवार येणाऱ्या समस्या आहेत."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), up["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("uk", "Uttarakhand (north-west)", "उत्तराखंड (उत्तर-पश्चिम)", "उत्तराखंड (वायव्य)"), it3("np", "Nepal (north)", "नेपाल (उत्तर)", "नेपाळ (उत्तर)"),
        it3("hp", "Himachal Pradesh (north-west)", "हिमाचल प्रदेश (उत्तर-पश्चिम)", "हिमाचल प्रदेश (वायव्य)"), it3("hr", "Haryana (west)", "हरियाणा (पश्चिम)", "हरियाणा (पश्चिम)"),
        it3("dl", "Delhi (west)", "दिल्ली (पश्चिम)", "दिल्ली (पश्चिम)"), it3("rj", "Rajasthan (west)", "राजस्थान (पश्चिम)", "राजस्थान (पश्चिम)"),
        it3("mp", "Madhya Pradesh (south)", "मध्य प्रदेश (दक्षिण)", "मध्य प्रदेश (दक्षिण)"), it3("ct", "Chhattisgarh (south-east)", "छत्तीसगढ़ (दक्षिण-पूर्व)", "छत्तीसगड (आग्नेय)"),
        it3("jh", "Jharkhand (south-east)", "झारखंड (दक्षिण-पूर्व)", "झारखंड (आग्नेय)"), it3("br", "Bihar (east)", "बिहार (पूर्व)", "बिहार (पूर्व)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("ganga", "Ganga", "गंगा", "गंगा", d=("Flows past Kanpur, Prayagraj and Varanasi; the Upper Ganga stretch is a Ramsar site.", "कानपुर, प्रयागराज और वाराणसी से होकर बहती है; ऊपरी गंगा खंड रामसर स्थल है।", "कानपूर, प्रयागराज व वाराणसीवरून वाहते; वरचा गंगा पट्टा रामसर स्थळ आहे.")),
        it3("yamuna", "Yamuna", "यमुना", "यमुना", d=("Past Mathura and Agra to the Sangam at Prayagraj.", "मथुरा और आगरा से होकर प्रयागराज के संगम तक।", "मथुरा व आग्र्यावरून प्रयागराजच्या संगमापर्यंत.")),
        it3("gomti", "Gomti", "गोमती", "गोमती", d=("Rises in Pilibhit; flows through Lucknow and joins the Ganga near Varanasi.", "पीलीभीत से निकलती है; लखनऊ से होकर वाराणसी के पास गंगा में मिलती है।", "पिलीभीतमध्ये उगम; लखनौतून वाहत वाराणसीजवळ गंगेला मिळते.")),
        it3("ghaghara", "Ghaghara (Saryu)", "घाघरा (सरयू)", "घाघरा (शरयू)", d=("Large Himalayan river; known as the Saryu at Ayodhya.", "बड़ी हिमालयी नदी; अयोध्या में सरयू कहलाती है।", "मोठी हिमालयीन नदी; अयोध्येत शरयू म्हणून ओळखली जाते.")),
        it3("betwa", "Betwa and Ken", "बेतवा और केन", "बेतवा व केन", d=("Rivers of Bundelkhand flowing north to the Yamuna.", "बुंदेलखंड की नदियाँ, जो उत्तर में यमुना तक बहती हैं।", "बुंदेलखंडच्या नद्या, उत्तरेकडे यमुनेला मिळतात.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
        (L("Highest and lowest elevation (official)", "सर्वोच्च और निम्नतम ऊँचाई (आधिकारिक)", "सर्वोच्च व नीचांकी उंची (अधिकृत)"), "survey-of-india", "Survey of India or the State gazetteer."),
        (L("Latitude and longitude extent", "अक्षांश-देशांतर विस्तार", "अक्षांश-रेखांश विस्तार"), "survey-of-india", "Survey of India or the State gazetteer."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Uttar Pradesh has a strongly seasonal, continental monsoon climate. Summers (April–June) are very hot and dry, with dusty westerly winds (loo) and temperatures that often pass 45 °C in the west and Bundelkhand. The south-west monsoon arrives in late June and brings most of the year's rain by September, with more rain in the east and the Terai than in the west. Winters (December–February) are cool to cold, with dense fog across the plains in December and January that disrupts roads, rail and flights, and occasional cold waves.",
        "उत्तर प्रदेश की जलवायु स्पष्ट मौसमी, महाद्वीपीय मानसूनी है। गर्मियाँ (अप्रैल–जून) बहुत गर्म और सूखी होती हैं, धूल भरी पछुआ हवाएँ (लू) चलती हैं और पश्चिम व बुंदेलखंड में तापमान अक्सर 45 °C से ऊपर चला जाता है। दक्षिण-पश्चिम मानसून जून के अंत में आता है और सितंबर तक साल की अधिकांश वर्षा देता है; पश्चिम की तुलना में पूर्व और तराई में अधिक वर्षा होती है। सर्दियाँ (दिसंबर–फ़रवरी) ठंडी होती हैं; दिसंबर और जनवरी में मैदानों पर घना कोहरा सड़क, रेल और उड़ानों को बाधित करता है, और कभी-कभी शीत लहर चलती है।",
        "उत्तर प्रदेशचे हवामान ठळकपणे हंगामी, खंडीय मोसमी आहे. उन्हाळा (एप्रिल–जून) अतिशय उष्ण व कोरडा असतो; धुळीचे पश्चिमी वारे (लू) वाहतात आणि पश्चिम भाग व बुंदेलखंडमध्ये तापमान अनेकदा 45 °C च्या पुढे जाते. नैर्ऋत्य मोसमी पाऊस जूनच्या शेवटी येतो आणि सप्टेंबरपर्यंत वर्षभराचा बहुतांश पाऊस देतो; पश्चिमेपेक्षा पूर्वेला व तराईत जास्त पाऊस पडतो. हिवाळा (डिसेंबर–फेब्रुवारी) थंड असतो; डिसेंबर-जानेवारीत मैदानावर दाट धुके पडून रस्ते, रेल्वे व विमानसेवा विस्कळीत होतात, आणि अधूनमधून थंडीची लाट येते."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Lucknow", "लखनऊ", "लखनौ"), "lat": 26.8467, "lon": 80.9462},
        {"name": L("Varanasi", "वाराणसी", "वाराणसी"), "lat": 25.3176, "lon": 82.9739},
        {"name": L("Agra", "आगरा", "आग्रा"), "lat": 27.1767, "lon": 78.0081},
        {"name": L("Prayagraj", "प्रयागराज", "प्रयागराज"), "lat": 25.4358, "lon": 81.8463},
    ]},
    lst("best", [
        it3("winter", "October to March", "अक्टूबर से मार्च", "ऑक्टोबर ते मार्च", d=("Best for sightseeing in Agra, Lucknow and Varanasi; Dev Deepavali in November; Magh Mela at Prayagraj in January–February. Expect fog in December–January.", "आगरा, लखनऊ और वाराणसी घूमने का सबसे अच्छा समय; नवंबर में देव दीपावली; जनवरी–फ़रवरी में प्रयागराज का माघ मेला। दिसंबर–जनवरी में कोहरे की संभावना।", "आग्रा, लखनौ व वाराणसी पाहण्यासाठी उत्तम; नोव्हेंबरमध्ये देव दीपावली; जानेवारी–फेब्रुवारीत प्रयागराजचा माघमेळा. डिसेंबर–जानेवारीत धुक्याची शक्यता.")),
        it3("summer", "April to June", "अप्रैल से जून", "एप्रिल ते जून", d=("Very hot; plan early-morning visits.", "बहुत गर्मी; सुबह जल्दी घूमने की योजना बनाएँ।", "अतिशय उष्ण; सकाळी लवकर भेटींचे नियोजन करा.")),
        it3("monsoon", "July to September", "जुलाई से सितंबर", "जुलै ते सप्टेंबर", d=("Humid, with flooding risk in the east; Terai parks close for the season.", "उमस भरा, पूर्व में बाढ़ का ख़तरा; तराई के उद्यान इस मौसम में बंद रहते हैं।", "दमट, पूर्वेला पुराचा धोका; तराईतील उद्याने या काळात बंद असतात.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (State)", "सामान्य वार्षिक वर्षा (राज्य)", "सरासरी वार्षिक पाऊस (राज्य)"), "imd", "IMD rainfall statistics for East and West UP sub-divisions."),
        (L("Monthly temperature and rainfall normals", "मासिक तापमान और वर्षा सामान्य", "मासिक तापमान व पर्जन्य सरासरी"), "imd", "IMD climatological normals for Lucknow, Varanasi, Agra."),
        (L("Heatwave and cold-wave days", "लू और शीत लहर के दिन", "उष्णतेची व थंडीची लाट असलेले दिवस"), "imd", "IMD annual climate summary."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Uttar Pradesh moves at many speeds. In Varanasi the day begins before dawn on the ghats, with bathers, boatmen, temple bells and the smoke of the cremation grounds, and ends with the evening Ganga aarti. Lucknow is courteous and unhurried — \"pehle aap\" — with kebab shops in Aminabad and Chowk, chikan workshops and the arches of the Imambaras. In the western districts, sugarcane trolleys queue at the mills, Meerut and Moradabad hum with workshops, and Noida's towers and expressways feel like a different State altogether. Small-town life runs on chai at the corner stall, crowded shared autos, wedding bands and loud debate about cricket and politics. Festivals — Holi in Braj, Diwali in Ayodhya, Dev Deepavali on the Varanasi ghats and the great Kumbh at Prayagraj — draw vast crowds.",
        "उत्तर प्रदेश कई रफ़्तारों पर चलता है। वाराणसी में दिन भोर से पहले घाटों पर शुरू होता है — स्नान करने वाले, नाविक, मंदिर की घंटियाँ और श्मशान घाट का धुआँ — और शाम की गंगा आरती पर ख़त्म होता है। लखनऊ विनम्र और इत्मीनान भरा है — \"पहले आप\" — अमीनाबाद और चौक की कबाब दुकानें, चिकन की कार्यशालाएँ और इमामबाड़ों की मेहराबें। पश्चिमी ज़िलों में गन्ने की ट्रॉलियाँ मिलों पर कतार में खड़ी रहती हैं, मेरठ और मुरादाबाद कार्यशालाओं से गूँजते हैं, और नोएडा की ऊँची इमारतें व एक्सप्रेसवे बिल्कुल दूसरा प्रदेश लगते हैं। छोटे शहरों की ज़िंदगी नुक्कड़ की चाय, ठसाठस भरे शेयर्ड ऑटो, बारात के बैंड और क्रिकेट व राजनीति पर ज़ोरदार बहस से चलती है। त्योहार — ब्रज की होली, अयोध्या की दीवाली, वाराणसी के घाटों पर देव दीपावली और प्रयागराज का महाकुंभ — विशाल भीड़ खींचते हैं।",
        "उत्तर प्रदेश अनेक वेगांनी चालतो. वाराणसीत दिवस पहाटेपूर्वीच घाटांवर सुरू होतो — स्नान करणारे, नावाडी, मंदिरघंटा आणि स्मशानघाटाचा धूर — आणि संध्याकाळच्या गंगा आरतीने संपतो. लखनौ नम्र आणि निवांत आहे — \"पहले आप\" — अमीनाबाद व चौकमधील कबाबची दुकाने, चिकनकारीच्या कार्यशाळा आणि इमामबाड्यांच्या कमानी. पश्चिमेकडील जिल्ह्यांत उसाच्या ट्रॉल्या साखर कारखान्यांवर रांगेत उभ्या असतात, मेरठ व मुरादाबाद कार्यशाळांनी गजबजलेले असतात, आणि नोएडाचे उंच टॉवर व द्रुतगती मार्ग अगदी वेगळेच राज्य वाटतात. लहान शहरांचे जीवन कोपऱ्यावरच्या चहावर, खच्चून भरलेल्या शेअर रिक्षांवर, लग्नाच्या बँडवर आणि क्रिकेट-राजकारणावरील जोरदार वादांवर चालते. सण — ब्रजमधील होळी, अयोध्येतील दिवाळी, वाराणसीच्या घाटांवरील देव दीपावली आणि प्रयागराजचा महाकुंभ — प्रचंड गर्दी खेचतात."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
SC = round(100 * 41357608 / 199812341, 2); ST = round(100 * 1134273 / 199812341, 2)
module(R, "people", [
    prose("p1", L(
        f"At the 2011 Census Uttar Pradesh had 19.98 crore people — more than any other State, and more than most countries. It had 912 women for every 1,000 men, below the national 943, and the child sex ratio was 902. Literacy was 67.7% (men 77.3%, women 57.2%), below the national level, and about 22.3% of people lived in towns, so the State remains largely rural. Population density was 829 per km², among the highest of any large State.\n\nHindi in its regional forms — Awadhi, Braj, Bhojpuri, Bundeli and Khari Boli in the west — is spoken by most people, and Urdu is widely used, especially in Lucknow and the western cities. Scheduled Castes formed about {SC:.1f}% and Scheduled Tribes about {ST:.2f}% of the population in 2011 (calculated from the State's Census counts).",
        f"2011 की जनगणना में उत्तर प्रदेश की जनसंख्या 19.98 करोड़ थी — किसी भी अन्य राज्य से अधिक, और अधिकांश देशों से भी अधिक। यहाँ प्रति 1,000 पुरुषों पर 912 महिलाएँ थीं, जो राष्ट्रीय 943 से कम है, और शिशु लिंगानुपात 902 था। साक्षरता 67.7% थी (पुरुष 77.3%, महिलाएँ 57.2%), जो राष्ट्रीय स्तर से कम है, और लगभग 22.3% लोग शहरों में रहते थे, इसलिए राज्य अब भी मुख्यतः ग्रामीण है। जनसंख्या घनत्व 829 प्रति वर्ग किमी था, जो बड़े राज्यों में सबसे अधिक में से है।\n\nहिंदी अपने क्षेत्रीय रूपों में — अवधी, ब्रज, भोजपुरी, बुंदेली और पश्चिम में खड़ी बोली — अधिकांश लोग बोलते हैं, और उर्दू का भी व्यापक उपयोग है, ख़ासकर लखनऊ और पश्चिमी शहरों में। 2011 में अनुसूचित जातियाँ लगभग {SC:.1f}% और अनुसूचित जनजातियाँ लगभग {ST:.2f}% थीं (राज्य के जनगणना आँकड़ों से गणना)।",
        f"2011 च्या जनगणनेनुसार उत्तर प्रदेशची लोकसंख्या 19.98 कोटी होती — इतर कोणत्याही राज्यापेक्षा आणि बहुतेक देशांपेक्षाही जास्त. दर 1,000 पुरुषांमागे 912 स्त्रिया होत्या, राष्ट्रीय 943 पेक्षा कमी, आणि बाल लिंग गुणोत्तर 902 होते. साक्षरता 67.7% होती (पुरुष 77.3%, स्त्रिया 57.2%), राष्ट्रीय पातळीपेक्षा कमी, आणि सुमारे 22.3% लोक शहरांत राहत होते, त्यामुळे राज्य अजूनही मुख्यतः ग्रामीण आहे. लोकसंख्येची घनता दर चौ.किमी 829 होती — मोठ्या राज्यांतील सर्वाधिकांपैकी एक.\n\nहिंदी तिच्या प्रादेशिक रूपांत — अवधी, ब्रज, भोजपुरी, बुंदेली आणि पश्चिमेला खडी बोली — बहुसंख्य लोक बोलतात, आणि उर्दूचाही व्यापक वापर होतो, विशेषतः लखनौ व पश्चिमेकडील शहरांत. 2011 मध्ये अनुसूचित जाती सुमारे {SC:.1f}% आणि अनुसूचित जमाती सुमारे {ST:.2f}% होत्या (राज्याच्या जनगणना आकड्यांवरून गणना)."),
        sources=["up-des", "census"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), up["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), up["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"]),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), up["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(916, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), up["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("urb", L("Urban population", "शहरी जनसंख्या", "नागरी लोकसंख्या"), up["urbanisation2011"], "percent", national=ind["urbanisation2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), up["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             UD(SC, "%", f"Calculated: SC population {inr(41357608)} ÷ total {inr(199812341)} (UP DES, Census 2011)."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             UD(ST, "%", f"Calculated: ST population {inr(1134273)} ÷ total {inr(199812341)} (UP DES, Census 2011)."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("hi", "Hindi", "हिंदी", "हिंदी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("ur", "Urdu", "उर्दू", "उर्दू", m=("Second official language", "दूसरी राजभाषा", "दुसरी राजभाषा")),
        it3("awa", "Awadhi", "अवधी", "अवधी", m=("Central UP (Awadh)", "मध्य उत्तर प्रदेश (अवध)", "मध्य उत्तर प्रदेश (अवध)")),
        it3("bho", "Bhojpuri", "भोजपुरी", "भोजपुरी", m=("Eastern UP (Purvanchal)", "पूर्वी उत्तर प्रदेश (पूर्वांचल)", "पूर्व उत्तर प्रदेश (पूर्वांचल)")),
        it3("bra", "Braj Bhasha", "ब्रजभाषा", "ब्रजभाषा", m=("Mathura–Agra region", "मथुरा–आगरा क्षेत्र", "मथुरा–आग्रा परिसर")),
        it3("bns", "Bundeli", "बुंदेली", "बुंदेली", m=("Bundelkhand", "बुंदेलखंड", "बुंदेलखंड")),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Provisional/Final Population Totals for Uttar Pradesh."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Mother-tongue shares (Census C-16)", "मातृभाषावार हिस्सा (जनगणना C-16)", "मातृभाषानिहाय वाटा (जनगणना C-16)"), "census", "Census C-16."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "The Ganga plain has been at the centre of Indian history for three thousand years. The later Vedic kingdoms of Kuru-Panchala and Kosala lay here; Kashi (Varanasi) was already an ancient city when the Buddha preached at Sarnath in the 6th–5th century BCE. The Mauryas, the Kushanas at Mathura and the Guptas ruled the region, and Kannauj became the capital of Harsha in the 7th century and the prize fought over by later dynasties.\n\nFrom the 13th century the Delhi Sultanate and then the Mughals ruled. Akbar built Fatehpur Sikri and made Agra a capital; Shah Jahan built the Taj Mahal. After Mughal power declined, the Nawabs of Awadh made Lucknow a centre of culture. The British annexed Awadh in 1856, and the next year the uprising of 1857 spread through Meerut, Kanpur, Lucknow and Jhansi. Prayagraj (then Allahabad) became a hub of the national movement. After Independence, the United Provinces were renamed Uttar Pradesh in 1950, and the hill districts became Uttarakhand in 2000.",
        "गंगा का मैदान तीन हज़ार वर्षों से भारतीय इतिहास के केंद्र में रहा है। उत्तर वैदिक काल के कुरु-पांचाल और कोसल राज्य यहीं थे; जब बुद्ध ने ईसा पूर्व छठी–पाँचवीं सदी में सारनाथ में उपदेश दिया, तब काशी (वाराणसी) पहले से एक प्राचीन नगर थी। मौर्यों, मथुरा में कुषाणों और गुप्तों ने इस क्षेत्र पर शासन किया, और कन्नौज सातवीं सदी में हर्ष की राजधानी बना और बाद के राजवंशों के बीच संघर्ष का केंद्र रहा।\n\n13वीं सदी से दिल्ली सल्तनत और फिर मुग़लों का शासन रहा। अकबर ने फ़तेहपुर सीकरी बनवाया और आगरा को राजधानी बनाया; शाहजहाँ ने ताजमहल बनवाया। मुग़ल सत्ता के कमज़ोर पड़ने के बाद अवध के नवाबों ने लखनऊ को संस्कृति का केंद्र बनाया। अंग्रेज़ों ने 1856 में अवध पर क़ब्ज़ा किया, और अगले वर्ष 1857 का विद्रोह मेरठ, कानपुर, लखनऊ और झाँसी में फैल गया। प्रयागराज (तब इलाहाबाद) राष्ट्रीय आंदोलन का केंद्र बना। आज़ादी के बाद 1950 में संयुक्त प्रांत का नाम उत्तर प्रदेश हुआ, और 2000 में पहाड़ी ज़िले उत्तराखंड बने।",
        "गंगेचे मैदान तीन हजार वर्षे भारतीय इतिहासाच्या केंद्रस्थानी आहे. उत्तर वैदिक काळातील कुरु-पांचाल व कोसल राज्ये इथेच होती; बुद्धांनी इ.स.पू. सहाव्या–पाचव्या शतकात सारनाथ येथे उपदेश दिला तेव्हा काशी (वाराणसी) आधीच प्राचीन नगरी होती. मौर्य, मथुरेतील कुषाण आणि गुप्त यांनी या प्रदेशावर राज्य केले, आणि कनौज सातव्या शतकात हर्षाची राजधानी बनले व नंतरच्या राजघराण्यांच्या संघर्षाचे केंद्र राहिले.\n\nतेराव्या शतकापासून दिल्ली सल्तनत आणि नंतर मुघलांचे राज्य होते. अकबराने फतेहपूर सिक्री बांधली आणि आग्र्याला राजधानी केले; शाहजहानने ताजमहाल बांधला. मुघल सत्ता क्षीण झाल्यावर अवधच्या नवाबांनी लखनौला संस्कृतीचे केंद्र बनवले. इंग्रजांनी 1856 मध्ये अवध खालसा केले, आणि पुढच्याच वर्षी 1857 चा उठाव मेरठ, कानपूर, लखनौ व झाशीत पसरला. प्रयागराज (तेव्हाचे अलाहाबाद) राष्ट्रीय चळवळीचे केंद्र बनले. स्वातंत्र्यानंतर 1950 मध्ये संयुक्त प्रांताचे नाव उत्तर प्रदेश झाले, आणि 2000 मध्ये डोंगरी जिल्ह्यांचे उत्तराखंड झाले."),
        conf="Editorial"),
    timeline([
        ev("sarnath", -528, L("c. 6th–5th century BCE", "लगभग ईसा पूर्व छठी–पाँचवीं सदी", "सुमारे इ.स.पू. सहावे–पाचवे शतक"), L("The Buddha's first sermon at Sarnath", "सारनाथ में बुद्ध का पहला उपदेश", "सारनाथ येथे बुद्धांचे पहिले प्रवचन")),
        ev("harsha", 606, L("7th century", "7वीं सदी", "सातवे शतक"), L("Kannauj becomes Harsha's capital", "कन्नौज हर्ष की राजधानी बना", "कनौज हर्षाची राजधानी")),
        ev("sikri", 1571, L("1571–85", "1571–85", "1571–85"), L("Akbar builds Fatehpur Sikri", "अकबर ने फ़तेहपुर सीकरी बनवाया", "अकबराने फतेहपूर सिक्री बांधली")),
        ev("taj", 1653, L("c. 1632–53", "लगभग 1632–53", "सुमारे 1632–53"), L("Taj Mahal built at Agra", "आगरा में ताजमहल बना", "आग्रा येथे ताजमहाल बांधला")),
        ev("awadh", 1856, L("1856", "1856", "1856"), L("British annex Awadh", "अंग्रेज़ों ने अवध पर क़ब्ज़ा किया", "इंग्रजांनी अवध खालसा केले")),
        ev("1857", 1857, L("10 May 1857", "10 मई 1857", "10 मे 1857"), L("Uprising begins at Meerut", "मेरठ से विद्रोह शुरू", "मेरठ येथून उठावाला सुरुवात")),
        ev("chauri", 1922, L("1922", "1922", "1922"), L("Chauri Chaura incident; Non-Cooperation Movement withdrawn", "चौरी चौरा कांड; असहयोग आंदोलन वापस", "चौरीचौरा घटना; असहकार आंदोलन मागे")),
        ev("up", 1950, L("24 January 1950", "24 जनवरी 1950", "24 जानेवारी 1950"), L("United Provinces renamed Uttar Pradesh", "संयुक्त प्रांत का नाम उत्तर प्रदेश हुआ", "संयुक्त प्रांताचे नाव उत्तर प्रदेश")),
        ev("uk", 2000, L("9 November 2000", "9 नवंबर 2000", "9 नोव्हेंबर 2000"), L("Hill districts form Uttarakhand", "पहाड़ी ज़िलों से उत्तराखंड बना", "डोंगरी जिल्ह्यांतून उत्तराखंड निर्मिती")),
        ev("kumbh", 2025, L("January–February 2025", "जनवरी–फ़रवरी 2025", "जानेवारी–फेब्रुवारी 2025"), L("Maha Kumbh at Prayagraj", "प्रयागराज में महाकुंभ", "प्रयागराज येथे महाकुंभ")),
        ev("sarnathwh", 2026, L("2026", "2026", "2026"), L("Sarnath inscribed as a UNESCO World Heritage Site", "सारनाथ यूनेस्को विश्व धरोहर स्थल घोषित", "सारनाथ युनेस्को जागतिक वारसा स्थळ घोषित")),
    ]),
    lst("heritage", [
        it3("taj", "Taj Mahal", "ताजमहल", "ताजमहाल", m=("UNESCO 1983", "यूनेस्को 1983", "युनेस्को 1983"), url=UNESCO, src="unesco-whc"),
        it3("agrafort", "Agra Fort", "आगरा क़िला", "आग्र्याचा किल्ला", m=("UNESCO 1983", "यूनेस्को 1983", "युनेस्को 1983"), url=UNESCO, src="unesco-whc"),
        it3("sikri", "Fatehpur Sikri", "फ़तेहपुर सीकरी", "फतेहपूर सिक्री", m=("UNESCO 1986", "यूनेस्को 1986", "युनेस्को 1986"), url=UNESCO, src="unesco-whc"),
        it3("sarnath", "Ancient Buddhist site of Sarnath", "सारनाथ का प्राचीन बौद्ध स्थल", "सारनाथचे प्राचीन बौद्ध स्थळ", m=("UNESCO 2026", "यूनेस्को 2026", "युनेस्को 2026"), url=UNESCO, src="unesco-whc"),
        it3("kumbh", "Kumbh Mela", "कुंभ मेला", "कुंभमेळा", m=("UNESCO intangible heritage (2017)", "यूनेस्को अमूर्त धरोहर (2017)", "युनेस्को अमूर्त वारसा (2017)")),
        it3("imambara", "Bara Imambara, Lucknow", "बड़ा इमामबाड़ा, लखनऊ", "बडा इमामबाडा, लखनौ", m=("Nawabi architecture", "नवाबी स्थापत्य", "नवाबी स्थापत्य")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("up mod1 ok")
