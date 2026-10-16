"""Rajasthan modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-RJ"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
DIST = "https://www.newsonair.gov.in/rajasthan-govt-announces-to-dissolve-9-out-of-17-districts-created-by-previous-govt"
PYD = "https://statistics.py.gov.in/state-wise-population"
rj = read("regions/IN-RJ.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Rajasthan, in north-western India, is the country's largest State by area, covering 3.42 lakh km² — about a tenth of India. The Aravalli range runs across it from south-west to north-east, dividing the Thar Desert in the west from the greener plains and plateaus of the east. It had 6.85 crore people at the 2011 Census. Jaipur is the capital; Jodhpur, Kota, Bikaner, Ajmer and Udaipur are the other large cities.\n\nThe State was built between 1948 and 1956 by joining the princely States of Rajputana — Mewar, Marwar, Jaipur, Bikaner and many others — with Ajmer. It shares a long border with Pakistan. Hindi is the official language, and Rajasthani languages such as Marwari, Mewari and Dhundhari are spoken at home.",
        "उत्तर-पश्चिमी भारत में स्थित राजस्थान क्षेत्रफल में देश का सबसे बड़ा राज्य है, जो 3.42 लाख वर्ग किमी — भारत का लगभग दसवाँ हिस्सा — में फैला है। अरावली पर्वतमाला इसे दक्षिण-पश्चिम से उत्तर-पूर्व तक पार करती है और पश्चिम के थार मरुस्थल को पूर्व के अधिक हरे मैदानों और पठारों से अलग करती है। 2011 की जनगणना में यहाँ 6.85 करोड़ लोग थे। जयपुर राजधानी है; जोधपुर, कोटा, बीकानेर, अजमेर और उदयपुर अन्य बड़े शहर हैं।\n\nराज्य 1948 से 1956 के बीच राजपूताना की रियासतों — मेवाड़, मारवाड़, जयपुर, बीकानेर और कई अन्य — को अजमेर के साथ जोड़कर बना। इसकी पाकिस्तान के साथ लंबी सीमा है। हिंदी राजभाषा है, और घरों में मारवाड़ी, मेवाड़ी और ढूँढाड़ी जैसी राजस्थानी भाषाएँ बोली जाती हैं।",
        "वायव्य भारतातील राजस्थान हे क्षेत्रफळाने देशातील सर्वांत मोठे राज्य असून 3.42 लाख चौ.किमी — भारताचा सुमारे दहावा भाग — व्यापते. अरवली पर्वतरांग त्याला नैर्ऋत्येकडून ईशान्येकडे छेदते आणि पश्चिमेकडील थरचे वाळवंट पूर्वेकडील अधिक हिरव्या मैदानांपासून व पठारांपासून वेगळे करते. 2011 च्या जनगणनेनुसार इथे 6.85 कोटी लोक होते. जयपूर ही राजधानी आहे; जोधपूर, कोटा, बिकानेर, अजमेर व उदयपूर ही इतर मोठी शहरे आहेत.\n\nराजपुतान्यातील संस्थाने — मेवाड, मारवाड, जयपूर, बिकानेर व इतर अनेक — अजमेरसोबत जोडून 1948 ते 1956 दरम्यान हे राज्य घडले. त्याची पाकिस्तानसोबत लांब सीमा आहे. हिंदी ही राजभाषा आहे, आणि घरांमध्ये मारवाडी, मेवाडी व ढूंढाडी यांसारख्या राजस्थानी भाषा बोलल्या जातात."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Rajasthan is the land of forts and palaces: six of its hill forts, the walled city of Jaipur, the Jantar Mantar observatory and the Keoladeo bird sanctuary are UNESCO World Heritage Sites. Its desert culture — camel fairs, the music of Manganiyar and Langa singers, Kalbelia dance, puppetry and block-printed textiles — is known around the world. The State is also a leader in solar power, grows much of India's mustard, cumin and pearl millet, and is home to most of India's zinc and marble mining and to the Barmer oil fields.",
        "राजस्थान क़िलों और महलों की भूमि है: इसके छह पहाड़ी क़िले, परकोटे वाला जयपुर शहर, जंतर मंतर वेधशाला और केवलादेव पक्षी अभयारण्य यूनेस्को विश्व धरोहर स्थल हैं। इसकी मरु संस्कृति — ऊँट मेले, मांगणियार और लंगा गायकों का संगीत, कालबेलिया नृत्य, कठपुतली और ठप्पा छपाई वाले वस्त्र — दुनिया भर में प्रसिद्ध है। राज्य सौर ऊर्जा में भी अग्रणी है, भारत की बहुत सी सरसों, जीरा और बाजरा उगाता है, और भारत के अधिकांश जस्ता और संगमरमर खनन तथा बाड़मेर के तेल क्षेत्रों का घर है।",
        "राजस्थान ही किल्ले व राजवाड्यांची भूमी आहे: त्याचे सहा डोंगरी किल्ले, तटबंदीचे जयपूर शहर, जंतर मंतर वेधशाळा व केवलादेव पक्षी अभयारण्य ही युनेस्को जागतिक वारसा स्थळे आहेत. त्याची वाळवंटी संस्कृती — उंटांच्या जत्रा, मांगणियार व लंगा गायकांचे संगीत, कालबेलिया नृत्य, कठपुतळ्या व ठसे छपाईची वस्त्रे — जगभर प्रसिद्ध आहे. राज्य सौरऊर्जेतही आघाडीवर आहे, भारतातील मोठ्या प्रमाणावर मोहरी, जिरे व बाजरी पिकवते, आणि भारतातील बहुतांश जस्त व संगमरवर खाणकाम आणि बाडमेरच्या तेलक्षेत्रांचे घर आहे."),
        title=L("What makes Rajasthan unique?", "राजस्थान को ख़ास क्या बनाता है?", "राजस्थानचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed", "गठन", "निर्मिती"), L("30 March 1949 (Rajasthan Day); completed 1 November 1956", "30 मार्च 1949 (राजस्थान दिवस); 1 नवंबर 1956 को पूर्ण", "30 मार्च 1949 (राजस्थान दिन); 1 नोव्हेंबर 1956 रोजी पूर्ण")],
           [L("Districts / divisions", "ज़िले / संभाग", "जिल्हे / विभाग"), "41 / 7"],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Hindi", "हिंदी", "हिंदी")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Rajasthan High Court, Jodhpur, with a bench at Jaipur", "राजस्थान उच्च न्यायालय, जोधपुर, जयपुर में पीठ", "राजस्थान उच्च न्यायालय, जोधपूर, जयपूर येथे खंडपीठ")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-RJ / RJ"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          "newsonair", DIST, conf="Editorial", access=None,
          note=L("District and division counts after the State cancelled nine new districts in December 2024 (News On AIR, 28 Dec 2024); other rows editorial.",
                 "दिसंबर 2024 में राज्य द्वारा नौ नए ज़िले रद्द करने के बाद ज़िलों और संभागों की संख्या (न्यूज़ ऑन एआईआर, 28 दिसंबर 2024); अन्य पंक्तियाँ संपादकीय।",
                 "डिसेंबर 2024 मध्ये राज्याने नऊ नवे जिल्हे रद्द केल्यानंतरची जिल्हे व विभागांची संख्या (न्यूज ऑन एआयआर, 28 डिसेंबर 2024); इतर ओळी संपादकीय.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "The Aravalli hills, among the oldest mountains on Earth, cross Rajasthan diagonally; Guru Shikhar on Mount Abu is their highest point. West of the Aravallis lies the Thar, or Great Indian Desert — sand dunes, rocky plains and salt lakes such as Sambhar — covering most of Jaisalmer, Barmer, Bikaner and Jodhpur. The Luni is the main river of the west and drains into the Rann of Kutch. East and south-east of the hills, the land is greener: the Banas and Chambal basins, the Hadoti plateau around Kota and the hilly, forested south around Udaipur and Banswara, drained by the Mahi. The Indira Gandhi Canal brings water from Punjab into the northern desert.",
        "पृथ्वी के सबसे पुराने पर्वतों में से अरावली पहाड़ियाँ राजस्थान को तिरछा पार करती हैं; माउंट आबू पर गुरु शिखर इनका सबसे ऊँचा स्थान है। अरावली के पश्चिम में थार या महान भारतीय मरुस्थल है — रेत के टीले, पथरीले मैदान और सांभर जैसी खारी झीलें — जो जैसलमेर, बाड़मेर, बीकानेर और जोधपुर के अधिकांश भाग में फैला है। लूणी पश्चिम की मुख्य नदी है और कच्छ के रण में गिरती है। पहाड़ियों के पूर्व और दक्षिण-पूर्व में भूमि अधिक हरी है: बनास और चंबल बेसिन, कोटा के आसपास हाड़ौती पठार और उदयपुर व बाँसवाड़ा के आसपास पहाड़ी, वनाच्छादित दक्षिण, जिसे माही बहाती है। इंदिरा गांधी नहर पंजाब से उत्तरी मरुस्थल तक पानी लाती है।",
        "पृथ्वीवरील सर्वांत प्राचीन पर्वतांपैकी अरवली डोंगर राजस्थानला तिरपे छेदतात; माउंट अबूवरील गुरुशिखर हे त्यांचे सर्वोच्च ठिकाण आहे. अरवलीच्या पश्चिमेला थर किंवा महान भारतीय वाळवंट आहे — वाळूच्या टेकड्या, खडकाळ मैदाने व सांभरसारखी खारी सरोवरे — जे जैसलमेर, बाडमेर, बिकानेर व जोधपूरचा बहुतांश भाग व्यापते. लुणी ही पश्चिमेची मुख्य नदी असून कच्छच्या रणात जाते. डोंगरांच्या पूर्वेला व आग्नेयेला भूमी अधिक हिरवी आहे: बनास व चंबळ खोरे, कोट्याभोवतीचे हाडोती पठार आणि उदयपूर व बांसवाड्याभोवतीचा डोंगराळ, जंगलव्याप्त दक्षिण भाग, जो माही नदी वाहून नेते. इंदिरा गांधी कालवा पंजाबमधून उत्तरेकडील वाळवंटात पाणी आणतो."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), rj["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("pk", "Pakistan (west and north-west)", "पाकिस्तान (पश्चिम और उत्तर-पश्चिम)", "पाकिस्तान (पश्चिम व वायव्य)"), it3("pb", "Punjab (north)", "पंजाब (उत्तर)", "पंजाब (उत्तर)"),
        it3("hr", "Haryana (north-east)", "हरियाणा (उत्तर-पूर्व)", "हरियाणा (ईशान्य)"), it3("up", "Uttar Pradesh (east)", "उत्तर प्रदेश (पूर्व)", "उत्तर प्रदेश (पूर्व)"),
        it3("mp", "Madhya Pradesh (south-east)", "मध्य प्रदेश (दक्षिण-पूर्व)", "मध्य प्रदेश (आग्नेय)"), it3("gj", "Gujarat (south-west)", "गुजरात (दक्षिण-पश्चिम)", "गुजरात (नैर्ऋत्य)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("chambal", "Chambal", "चंबल", "चंबळ", d=("The State's only large perennial river; dams at Rana Pratap Sagar, Jawahar Sagar and Kota.", "राज्य की एकमात्र बड़ी सदानीरा नदी; राणा प्रताप सागर, जवाहर सागर और कोटा में बाँध।", "राज्यातील एकमेव मोठी बारमाही नदी; राणा प्रताप सागर, जवाहर सागर व कोटा येथे धरणे.")),
        it3("banas", "Banas", "बनास", "बनास", d=("Chambal tributary flowing entirely within Rajasthan.", "चंबल की सहायक नदी, जो पूरी तरह राजस्थान में बहती है।", "चंबळची उपनदी, पूर्णपणे राजस्थानात वाहते.")),
        it3("luni", "Luni", "लूणी", "लुणी", d=("Seasonal river of the west, turning salty downstream.", "पश्चिम की मौसमी नदी, जो आगे चलकर खारी हो जाती है।", "पश्चिमेकडील हंगामी नदी, पुढे खारट होते.")),
        it3("mahi", "Mahi", "माही", "माही", d=("River of the south; Mahi Bajaj Sagar dam at Banswara.", "दक्षिण की नदी; बाँसवाड़ा में माही बजाज सागर बाँध।", "दक्षिणेकडील नदी; बांसवाडा येथे माही बजाज सागर धरण.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Guru Shikhar — official elevation", "गुरु शिखर — आधिकारिक ऊँचाई", "गुरुशिखर — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Length of the international border", "अंतरराष्ट्रीय सीमा की लंबाई", "आंतरराष्ट्रीय सीमेची लांबी"), "india-gov", "Ministry of Home Affairs (Department of Border Management)."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Rajasthan has some of India's harshest weather. Western Rajasthan is arid: summers are fierce, with temperatures near or above 50 °C in places such as Phalodi, Churu and Barmer, dust storms in May and June, and very little rain. Winters are cold at night, with frost in the north and near-freezing nights at Mount Abu and in the Shekhawati towns. The south-west monsoon arrives in late June or July and brings most of the year's rain, heaviest in the south and south-east — Banswara, Jhalawar and Mount Abu — and lightest in Jaisalmer.",
        "राजस्थान में भारत का कुछ सबसे कठोर मौसम है। पश्चिमी राजस्थान शुष्क है: गर्मियाँ भीषण होती हैं, फलोदी, चूरू और बाड़मेर जैसे स्थानों में तापमान 50 °C के आसपास या उससे ऊपर जाता है, मई-जून में आँधियाँ चलती हैं, और वर्षा बहुत कम होती है। सर्दियों में रातें ठंडी होती हैं — उत्तर में पाला पड़ता है, और माउंट आबू व शेखावाटी के कस्बों में रातें शून्य के आसपास पहुँचती हैं। दक्षिण-पश्चिम मानसून जून के अंत या जुलाई में आता है और साल की अधिकांश वर्षा लाता है — सबसे अधिक दक्षिण और दक्षिण-पूर्व में (बाँसवाड़ा, झालावाड़ और माउंट आबू) और सबसे कम जैसलमेर में।",
        "राजस्थानात भारतातील काही सर्वांत कठोर हवामान आहे. पश्चिम राजस्थान शुष्क आहे: उन्हाळा भीषण असतो, फलोदी, चुरू व बाडमेरसारख्या ठिकाणी तापमान 50 °C च्या जवळ किंवा पुढे जाते, मे-जूनमध्ये धुळीची वादळे येतात, आणि पाऊस फारच कमी पडतो. हिवाळ्यात रात्री थंड असतात — उत्तरेत दव गोठते, आणि माउंट अबू व शेखावटीच्या गावांत रात्री शून्याजवळ पोहोचतात. नैर्ऋत्य मान्सून जूनच्या अखेरीस किंवा जुलैमध्ये येतो आणि वर्षाचा बहुतांश पाऊस आणतो — सर्वाधिक दक्षिण व आग्नेयेत (बांसवाडा, झालावाड व माउंट अबू) आणि सर्वांत कमी जैसलमेरमध्ये."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Jaipur", "जयपुर", "जयपूर"), "lat": 26.9124, "lon": 75.7873},
        {"name": L("Jaisalmer", "जैसलमेर", "जैसलमेर"), "lat": 26.9157, "lon": 70.9083},
        {"name": L("Udaipur", "उदयपुर", "उदयपूर"), "lat": 24.5854, "lon": 73.7125},
        {"name": L("Mount Abu", "माउंट आबू", "माउंट अबू"), "lat": 24.5926, "lon": 72.7156},
    ]},
    lst("best", [
        it3("winter", "October to March", "अक्टूबर से मार्च", "ऑक्टोबर ते मार्च", d=("Best season: desert camps, forts, the Pushkar fair (Oct–Nov) and the Jaisalmer desert festival (Feb).", "सबसे अच्छा मौसम: मरु शिविर, क़िले, पुष्कर मेला (अक्टूबर–नवंबर) और जैसलमेर मरु महोत्सव (फ़रवरी)।", "सर्वोत्तम काळ: वाळवंटी शिबिरे, किल्ले, पुष्कर जत्रा (ऑक्टो.–नोव्हें.) व जैसलमेर वाळवंट महोत्सव (फेब्रु.).")),
        it3("summer", "April to June", "अप्रैल से जून", "एप्रिल ते जून", d=("Extreme heat; Mount Abu is the only cool retreat.", "भीषण गर्मी; केवल माउंट आबू ठंडा ठिकाना है।", "प्रचंड उष्णता; फक्त माउंट अबू थंड ठिकाण.")),
        it3("monsoon", "July to September", "जुलाई से सितंबर", "जुलै ते सप्टेंबर", d=("Udaipur's lakes fill; Teej festival; green Aravallis.", "उदयपुर की झीलें भरती हैं; तीज उत्सव; हरी अरावली।", "उदयपूरची सरोवरे भरतात; तीज सण; हिरवी अरवली.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (East and West Rajasthan)", "सामान्य वार्षिक वर्षा (पूर्वी और पश्चिमी राजस्थान)", "सरासरी वार्षिक पाऊस (पूर्व व पश्चिम राजस्थान)"), "imd", "IMD rainfall statistics by sub-division."),
        (L("Highest recorded temperature (official)", "दर्ज सबसे ऊँचा तापमान (आधिकारिक)", "नोंदलेले सर्वोच्च तापमान (अधिकृत)"), "imd", "IMD station records."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Colour is everywhere in Rajasthan: bright turbans and odhnis against the sand, painted havelis in Shekhawati, the pink walls of Jaipur, the blue houses of Jodhpur and the golden sandstone of Jaisalmer. Old city bazaars sell bangles, textiles and silver, and tea stalls and kachori shops fill the mornings. In the villages of the desert, life follows the camel, the well and the rains, with folk musicians singing at weddings and fairs. Hospitality — 'padharo mhare des', welcome to my land — is a point of pride, and food is rich in ghee, millet and spices.",
        "राजस्थान में हर जगह रंग हैं: रेत के बीच चटकीले साफ़े और ओढ़नियाँ, शेखावाटी की चित्रित हवेलियाँ, जयपुर की गुलाबी दीवारें, जोधपुर के नीले घर और जैसलमेर का सुनहरा बलुआ पत्थर। पुराने शहरों के बाज़ार चूड़ियाँ, वस्त्र और चाँदी बेचते हैं, और सुबह चाय की थड़ियों और कचौरी की दुकानों से भरी रहती है। मरुस्थल के गाँवों में जीवन ऊँट, कुएँ और वर्षा के साथ चलता है, और लोक संगीतकार शादियों और मेलों में गाते हैं। मेहमाननवाज़ी — 'पधारो म्हारे देस' — गर्व की बात है, और भोजन घी, बाजरे और मसालों से भरपूर होता है।",
        "राजस्थानात सर्वत्र रंग आहेत: वाळूच्या पार्श्वभूमीवर भडक फेटे व ओढण्या, शेखावटीतील रंगवलेल्या हवेल्या, जयपूरच्या गुलाबी भिंती, जोधपूरची निळी घरे आणि जैसलमेरचा सोनेरी वालुकाश्म. जुन्या शहरांचे बाजार बांगड्या, वस्त्रे व चांदी विकतात, आणि सकाळ चहाच्या टपऱ्या व कचोरीच्या दुकानांनी भरलेली असते. वाळवंटातील गावांत जीवन उंट, विहीर व पावसाच्या लयीत चालते, आणि लोकसंगीतकार लग्नांत व जत्रांत गातात. आदरातिथ्य — 'पधारो म्हारे देस' — अभिमानाची गोष्ट आहे, आणि जेवण तूप, बाजरी व मसाल्यांनी समृद्ध असते."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Rajasthan had 6.85 crore people at the 2011 Census, with a density of about 200 per km² — low, because of the desert west. The sex ratio was 928 women per 1,000 men, below the national 943, and the child sex ratio was 888, among the lowest in India and down from 909 in 2001. Literacy was 66.1%, below the national 73.0%. Scheduled Castes made up 17.8% of the population and Scheduled Tribes 13.5% — Meenas in the east and Bhils, Garasias and others in the southern hills.\n\nHindi is the official language. At home most people speak Rajasthani languages: Marwari in the west, Mewari around Udaipur, Dhundhari around Jaipur, Harauti around Kota, Mewati in the north-east and Wagdi among the Bhils of the south. Sindhi and Punjabi are spoken in parts of the north and west.",
        "2011 की जनगणना में राजस्थान की जनसंख्या 6.85 करोड़ थी, और घनत्व लगभग 200 प्रति वर्ग किमी — पश्चिमी मरुस्थल के कारण कम। लिंगानुपात प्रति 1,000 पुरुषों पर 928 महिलाएँ था, जो राष्ट्रीय 943 से कम है, और शिशु लिंगानुपात 888 था, जो भारत में सबसे कम में से है और 2001 के 909 से घटा। साक्षरता 66.1% थी, जो राष्ट्रीय 73.0% से कम है। अनुसूचित जातियाँ जनसंख्या का 17.8% और अनुसूचित जनजातियाँ 13.5% थीं — पूर्व में मीणा और दक्षिणी पहाड़ियों में भील, गरासिया और अन्य।\n\nहिंदी राजभाषा है। घरों में अधिकांश लोग राजस्थानी भाषाएँ बोलते हैं: पश्चिम में मारवाड़ी, उदयपुर के आसपास मेवाड़ी, जयपुर के आसपास ढूँढाड़ी, कोटा के आसपास हाड़ौती, उत्तर-पूर्व में मेवाती और दक्षिण के भीलों में वागड़ी। उत्तर और पश्चिम के कुछ भागों में सिंधी और पंजाबी बोली जाती हैं।",
        "2011 च्या जनगणनेनुसार राजस्थानची लोकसंख्या 6.85 कोटी होती, आणि घनता सुमारे 200 प्रति चौ.किमी — पश्चिमेकडील वाळवंटामुळे कमी. दर 1,000 पुरुषांमागे 928 स्त्रिया होत्या — राष्ट्रीय 943 पेक्षा कमी — आणि बाल लिंग गुणोत्तर 888 होते, भारतातील सर्वांत कमींपैकी व 2001 च्या 909 वरून घटलेले. साक्षरता 66.1% होती, राष्ट्रीय 73.0% पेक्षा कमी. अनुसूचित जाती लोकसंख्येच्या 17.8% व अनुसूचित जमाती 13.5% होत्या — पूर्वेला मीणा आणि दक्षिणेकडील डोंगरांत भिल्ल, गरासिया व इतर.\n\nहिंदी ही राजभाषा आहे. घरांत बहुतेक लोक राजस्थानी भाषा बोलतात: पश्चिमेत मारवाडी, उदयपूरभोवती मेवाडी, जयपूरभोवती ढूंढाडी, कोट्याभोवती हाडोती, ईशान्येत मेवाती आणि दक्षिणेकडील भिल्लांमध्ये वागडी. उत्तर व पश्चिमेच्या काही भागांत सिंधी व पंजाबी बोलल्या जातात."),
        sources=["census", "es-india", "dl-planning"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), rj["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), rj["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(921, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), rj["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(909, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), rj["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), rj["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(17.8, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 122.21 lakh people."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(13.5, "%", "2011", "census", "dl-planning", SCST, note="Same table: 92.38 lakh people."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("hi", "Hindi", "हिंदी", "हिंदी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("mwr", "Marwari", "मारवाड़ी", "मारवाडी"), it3("mtr", "Mewari", "मेवाड़ी", "मेवाडी"), it3("dhd", "Dhundhari", "ढूँढाड़ी", "ढूंढाडी"),
        it3("hoj", "Harauti", "हाड़ौती", "हाडोती"), it3("wbr", "Wagdi", "वागड़ी", "वागडी"), it3("sd", "Sindhi", "सिंधी", "सिंधी"), it3("pa", "Punjabi", "पंजाबी", "पंजाबी"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Final Population Totals for Rajasthan."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Kalibangan, on the dry bed of the Ghaggar, was a Harappan town, and Bairat near Jaipur was the capital of the ancient Matsya kingdom. From the 7th century Rajput clans rose to power: the Gurjara-Pratiharas, the Chauhans of Ajmer — whose king Prithviraj fought Muhammad of Ghor in 1191–92 — the Sisodias of Mewar at Chittor and later Udaipur, the Rathores of Marwar at Jodhpur and Bikaner, the Kachwahas of Amber and Jaipur, and the Bhatis of Jaisalmer. Mewar's Rana Kumbha, Rana Sanga and Maharana Pratap, who fought the Mughals at Haldighati in 1576, are remembered for resistance, while Amber allied with Akbar. Sawai Jai Singh II founded Jaipur in 1727 and built observatories there and elsewhere.\n\nAfter Maratha raids in the 18th century, the Rajput States signed treaties with the British around 1818 and formed Rajputana. After Independence, 19 princely States and three chiefships were merged in stages: Rajasthan was formed on 30 March 1949, now Rajasthan Day, and took its final shape on 1 November 1956, when Ajmer was added. India's nuclear tests of 1974 and 1998 were carried out at Pokhran in Jaisalmer district.",
        "घग्घर के सूखे तल पर कालीबंगा एक हड़प्पा नगर था, और जयपुर के पास बैराठ प्राचीन मत्स्य राज्य की राजधानी थी। 7वीं सदी से राजपूत कुल शक्तिशाली हुए: गुर्जर-प्रतिहार, अजमेर के चौहान — जिनके राजा पृथ्वीराज ने 1191–92 में मुहम्मद ग़ोरी से युद्ध किया — चित्तौड़ और बाद में उदयपुर के मेवाड़ के सिसोदिया, जोधपुर और बीकानेर के मारवाड़ के राठौड़, आमेर और जयपुर के कछवाहा, और जैसलमेर के भाटी। मेवाड़ के राणा कुंभा, राणा सांगा और 1576 में हल्दीघाटी में मुग़लों से लड़ने वाले महाराणा प्रताप प्रतिरोध के लिए याद किए जाते हैं, जबकि आमेर ने अकबर से संधि की। सवाई जयसिंह द्वितीय ने 1727 में जयपुर बसाया और वहाँ व अन्यत्र वेधशालाएँ बनवाईं।\n\n18वीं सदी में मराठा आक्रमणों के बाद राजपूत रियासतों ने 1818 के आसपास अंग्रेज़ों से संधियाँ कीं और राजपूताना बना। आज़ादी के बाद 19 रियासतों और तीन ठिकानों का चरणों में विलय हुआ: 30 मार्च 1949 को — जो अब राजस्थान दिवस है — राजस्थान बना, और 1 नवंबर 1956 को अजमेर जुड़ने के साथ इसने अंतिम रूप लिया। भारत के 1974 और 1998 के परमाणु परीक्षण जैसलमेर ज़िले के पोकरण में हुए।",
        "घग्गरच्या कोरड्या पात्रावरील कालीबंगा हे हडप्पा नगर होते, आणि जयपूरजवळील बैराठ ही प्राचीन मत्स्य राज्याची राजधानी होती. सातव्या शतकापासून राजपूत कुळे सत्तेवर आली: गुर्जर-प्रतिहार, अजमेरचे चौहान — ज्यांचा राजा पृथ्वीराज 1191–92 मध्ये मुहम्मद घोरीशी लढला — चित्तोड व नंतर उदयपूरचे मेवाडचे सिसोदिया, जोधपूर व बिकानेरचे मारवाडचे राठोड, आमेर व जयपूरचे कछवाह, आणि जैसलमेरचे भाटी. मेवाडचे राणा कुंभा, राणा संग आणि 1576 मध्ये हळदीघाटी येथे मुघलांशी लढलेले महाराणा प्रताप प्रतिकारासाठी स्मरणात आहेत, तर आमेरने अकबराशी सख्य केले. सवाई जयसिंह दुसरे यांनी 1727 मध्ये जयपूर वसवले आणि तिथे व इतरत्र वेधशाळा बांधल्या.\n\nअठराव्या शतकातील मराठा स्वाऱ्यांनंतर राजपूत संस्थानांनी 1818 च्या सुमारास इंग्रजांशी तह केले आणि राजपुताना बनला. स्वातंत्र्यानंतर 19 संस्थाने व तीन ठिकाणे टप्प्याटप्प्याने विलीन झाली: 30 मार्च 1949 रोजी — जो आता राजस्थान दिन आहे — राजस्थान स्थापन झाले, आणि 1 नोव्हेंबर 1956 रोजी अजमेर जोडल्यावर त्याला अंतिम स्वरूप मिळाले. भारताच्या 1974 व 1998 च्या अणुचाचण्या जैसलमेर जिल्ह्यातील पोखरण येथे झाल्या."),
        conf="Editorial"),
    timeline([
        ev("kalibangan", -2500, L("c. 2500 BCE", "लगभग 2500 ई.पू.", "सुमारे इ.स.पू. 2500"), L("Harappan town at Kalibangan", "कालीबंगा में हड़प्पा नगर", "कालीबंगा येथे हडप्पा नगर")),
        ev("tarain", 1192, L("1191–92", "1191–92", "1191–92"), L("Battles of Tarain; Prithviraj Chauhan", "तराइन के युद्ध; पृथ्वीराज चौहान", "तराईनच्या लढाया; पृथ्वीराज चौहान")),
        ev("haldighati", 1576, L("1576", "1576", "1576"), L("Battle of Haldighati", "हल्दीघाटी का युद्ध", "हळदीघाटीची लढाई")),
        ev("jaipur", 1727, L("1727", "1727", "1727"), L("Jaipur founded by Sawai Jai Singh II", "सवाई जयसिंह द्वितीय ने जयपुर बसाया", "सवाई जयसिंह दुसरे यांनी जयपूर वसवले")),
        ev("treaties", 1818, L("1818", "1818", "1818"), L("Rajput States sign treaties with the British", "राजपूत रियासतों की अंग्रेज़ों से संधियाँ", "राजपूत संस्थानांचे इंग्रजांशी तह")),
        ev("formed", 1949, L("30 March 1949", "30 मार्च 1949", "30 मार्च 1949"), L("Greater Rajasthan formed (Rajasthan Day)", "वृहत् राजस्थान बना (राजस्थान दिवस)", "बृहद् राजस्थान स्थापन (राजस्थान दिन)")),
        ev("final", 1956, L("1 November 1956", "1 नवंबर 1956", "1 नोव्हेंबर 1956"), L("Ajmer merged; present boundaries", "अजमेर का विलय; वर्तमान सीमाएँ", "अजमेर विलीन; सध्याच्या सीमा")),
        ev("pokhran", 1998, L("1974 and 1998", "1974 और 1998", "1974 व 1998"), L("Nuclear tests at Pokhran", "पोकरण में परमाणु परीक्षण", "पोखरण येथे अणुचाचण्या")),
        ev("jaipurwhs", 2019, L("2019", "2019", "2019"), L("Jaipur City inscribed as a UNESCO World Heritage Site", "जयपुर शहर यूनेस्को विश्व धरोहर स्थल घोषित", "जयपूर शहर युनेस्को जागतिक वारसा स्थळ घोषित")),
    ]),
    lst("heritage", [
        it3("forts", "Hill Forts of Rajasthan (Chittorgarh, Kumbhalgarh, Ranthambore, Gagron, Amber, Jaisalmer)", "राजस्थान के पहाड़ी क़िले (चित्तौड़गढ़, कुंभलगढ़, रणथंभौर, गागरोन, आमेर, जैसलमेर)", "राजस्थानचे डोंगरी किल्ले (चित्तोडगड, कुंभलगड, रणथंभोर, गागरोन, आमेर, जैसलमेर)", m=("UNESCO 2013", "यूनेस्को 2013", "युनेस्को 2013"), url=UNESCO, src="unesco-whc"),
        it3("jantar", "Jantar Mantar, Jaipur", "जंतर मंतर, जयपुर", "जंतर मंतर, जयपूर", m=("UNESCO 2010", "यूनेस्को 2010", "युनेस्को 2010"), url=UNESCO, src="unesco-whc"),
        it3("jaipurcity", "Jaipur City", "जयपुर शहर", "जयपूर शहर", m=("UNESCO 2019", "यूनेस्को 2019", "युनेस्को 2019"), url=UNESCO, src="unesco-whc"),
        it3("keoladeo", "Keoladeo National Park", "केवलादेव राष्ट्रीय उद्यान", "केवलादेव राष्ट्रीय उद्यान", m=("UNESCO 1985", "यूनेस्को 1985", "युनेस्को 1985"), url=UNESCO, src="unesco-whc"),
        it3("dilwara", "Dilwara temples, Mount Abu", "दिलवाड़ा मंदिर, माउंट आबू", "दिलवाडा मंदिरे, माउंट अबू", m=("Jain marble temples", "जैन संगमरमर मंदिर", "जैन संगमरवरी मंदिरे")),
        it3("mehrangarh", "Mehrangarh Fort, Jodhpur", "मेहरानगढ़ क़िला, जोधपुर", "मेहरानगड किल्ला, जोधपूर", m=("Rathore capital", "राठौड़ राजधानी", "राठोड राजधानी")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("rj mod1 ok")
