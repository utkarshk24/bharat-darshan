"""Jharkhand modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-JH"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
jh = read("regions/IN-JH.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Jharkhand — 'the land of forests' — covers most of the Chota Nagpur plateau in eastern India, with Bihar to the north, West Bengal to the east, Odisha to the south, Chhattisgarh to the west and Uttar Pradesh to the north-west. Its rolling uplands, sal forests, waterfalls and rivers sit on some of India's richest deposits of coal, iron ore, copper, mica and uranium. It had 3.30 crore people at the 2011 Census. Ranchi is the capital and Dumka the sub-capital; Jamshedpur, Dhanbad, Bokaro and Deoghar are other major cities.\n\nJharkhand was carved out of southern Bihar on 15 November 2000, the birth anniversary of the tribal hero Birsa Munda, after a long movement for a State for the region's Adivasi and other communities. Hindi is the official language, and several others, including Santali, Urdu, Bengali, Mundari, Ho, Kurukh and Nagpuri, have been given second-official-language status.",
        "झारखंड — 'वनों की भूमि' — पूर्वी भारत के छोटा नागपुर पठार के अधिकांश भाग में फैला है; इसके उत्तर में बिहार, पूर्व में पश्चिम बंगाल, दक्षिण में ओडिशा, पश्चिम में छत्तीसगढ़ और उत्तर-पश्चिम में उत्तर प्रदेश है। इसके लहरदार ऊँचे क्षेत्र, साल वन, झरने और नदियाँ भारत के कोयला, लौह अयस्क, ताँबा, अभ्रक और यूरेनियम के सबसे समृद्ध भंडारों पर स्थित हैं। 2011 की जनगणना में इसकी जनसंख्या 3.30 करोड़ थी। रांची राजधानी और दुमका उपराजधानी है; जमशेदपुर, धनबाद, बोकारो और देवघर अन्य प्रमुख शहर हैं।\n\nक्षेत्र के आदिवासी और अन्य समुदायों के लिए राज्य के लंबे आंदोलन के बाद 15 नवंबर 2000 को, जनजातीय नायक बिरसा मुंडा की जयंती पर, दक्षिणी बिहार से झारखंड बना। हिंदी राजभाषा है, और संताली, उर्दू, बांग्ला, मुंडारी, हो, कुड़ुख और नागपुरी सहित कई भाषाओं को द्वितीय राजभाषा का दर्जा दिया गया है।",
        "झारखंड — 'वनांची भूमी' — पूर्व भारतातील छोटा नागपूर पठाराचा बहुतांश भाग व्यापतो; त्याच्या उत्तरेला बिहार, पूर्वेला पश्चिम बंगाल, दक्षिणेला ओडिशा, पश्चिमेला छत्तीसगड व वायव्येला उत्तर प्रदेश आहे. त्याचे लाटांसारखे उंचवटे, साल वने, धबधबे व नद्या भारतातील कोळसा, लोहखनिज, तांबे, अभ्रक व युरेनियमच्या सर्वांत समृद्ध साठ्यांवर वसलेल्या आहेत. 2011 च्या जनगणनेनुसार त्याची लोकसंख्या 3.30 कोटी होती. रांची ही राजधानी व दुमका उपराजधानी आहे; जमशेदपूर, धनबाद, बोकारो व देवघर ही इतर प्रमुख शहरे आहेत.\n\nप्रदेशातील आदिवासी व इतर समुदायांसाठी स्वतंत्र राज्याच्या दीर्घ चळवळीनंतर 15 नोव्हेंबर 2000 रोजी, आदिवासी नायक बिरसा मुंडा यांच्या जयंतीदिनी, दक्षिण बिहारमधून झारखंड निर्माण झाले. हिंदी ही राजभाषा आहे, आणि संताली, उर्दू, बंगाली, मुंडारी, हो, कुडुख व नागपुरी यांसह अनेक भाषांना द्वितीय राजभाषेचा दर्जा देण्यात आला आहे."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Jharkhand is the heartland of Adivasi India: Santhal, Munda, Ho, Oraon and many other communities make up about a quarter of its people, and their festivals — Sarhul, Karma and Sohrai — set the year's rhythm. The region gave India some of its great anti-colonial uprisings, from the Santhal Hul of 1855 to Birsa Munda's ulgulan. It is also the cradle of Indian heavy industry: Jamshedpur grew around India's first large private steel works in 1907, and Dhanbad's Jharia coalfield fuelled the country's furnaces. Today the State is known for its waterfalls around Ranchi, the Baidyanath temple at Deoghar, Sohrai–Khovar wall painting and Chhau dance — and for cricket's M. S. Dhoni and archer Deepika Kumari.",
        "झारखंड आदिवासी भारत का हृदय है: संथाल, मुंडा, हो, उरांव और कई अन्य समुदाय इसकी लगभग एक-चौथाई आबादी हैं, और उनके त्योहार — सरहुल, करमा और सोहराय — वर्ष की लय तय करते हैं। इस क्षेत्र ने भारत को उपनिवेशवाद-विरोधी कुछ महान विद्रोह दिए, 1855 के संथाल हूल से लेकर बिरसा मुंडा के उलगुलान तक। यह भारतीय भारी उद्योग का पालना भी है: जमशेदपुर 1907 में भारत के पहले बड़े निजी इस्पात कारख़ाने के इर्द-गिर्द बसा, और धनबाद के झरिया कोयला क्षेत्र ने देश की भट्ठियों को ईंधन दिया। आज राज्य रांची के आसपास के झरनों, देवघर के बैद्यनाथ मंदिर, सोहराय–खोवर भित्ति चित्रकला और छऊ नृत्य के लिए — और क्रिकेट के एम. एस. धोनी और तीरंदाज़ दीपिका कुमारी के लिए — जाना जाता है।",
        "झारखंड हे आदिवासी भारताचे हृदय आहे: संथाल, मुंडा, हो, ओराव व इतर अनेक समुदाय त्याच्या लोकसंख्येचा सुमारे एक-चतुर्थांश भाग आहेत, आणि त्यांचे सण — सरहुल, करमा व सोहराय — वर्षाची लय ठरवतात. या प्रदेशाने भारताला काही महान वसाहतवादविरोधी उठाव दिले, 1855 च्या संथाल हूलपासून बिरसा मुंडांच्या उलगुलानपर्यंत. हे भारतीय अवजड उद्योगाचे पाळणाघरही आहे: जमशेदपूर 1907 मध्ये भारतातील पहिल्या मोठ्या खासगी पोलाद कारखान्याभोवती वसले, आणि धनबादच्या झरिया कोळसा क्षेत्राने देशाच्या भट्ट्यांना इंधन पुरवले. आज राज्य रांचीभोवतीचे धबधबे, देवघरचे बैद्यनाथ मंदिर, सोहराय–खोवर भित्तिचित्रकला व छाऊ नृत्यासाठी — आणि क्रिकेटचे एम. एस. धोनी व तिरंदाज दीपिका कुमारी यांच्यासाठी — ओळखले जाते."),
        title=L("What makes Jharkhand unique?", "झारखंड को ख़ास क्या बनाता है?", "झारखंडचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed", "गठन", "निर्मिती"), L("15 November 2000 (from Bihar)", "15 नवंबर 2000 (बिहार से)", "15 नोव्हेंबर 2000 (बिहारमधून)")],
           [L("Districts / divisions", "ज़िले / प्रमंडल", "जिल्हे / विभाग"), "24 / 5"],
           [L("Capital / sub-capital", "राजधानी / उपराजधानी", "राजधानी / उपराजधानी"), L("Ranchi / Dumka", "रांची / दुमका", "रांची / दुमका")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Jharkhand High Court, Ranchi (2000)", "झारखंड उच्च न्यायालय, रांची (2000)", "झारखंड उच्च न्यायालय, रांची (2000)")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "JH"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be linked to the State's notifications in review.", "संपादकीय; समीक्षा में राज्य की अधिसूचनाओं से जोड़ा जाएगा।", "संपादकीय; तपासणीत राज्याच्या अधिसूचनांशी जोडले जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Most of Jharkhand lies on the Chota Nagpur plateau, a series of ancient, eroded tablelands and hills. The Ranchi plateau in the centre is edged by steep scarps where rivers plunge over waterfalls such as Hundru, Dassam and Jonha; the higher pat lands of Netarhat lie to the west; Parasnath hill in Giridih, sacred to Jains, is the highest point; and the Rajmahal hills rise in the north-east near the Ganga, which touches the State only at Sahibganj. The Damodar flows east through the coal belt of Bokaro and Dhanbad, the Subarnarekha drains Ranchi and Jamshedpur, and the North and South Koel, Barakar and Mayurakshi are other important rivers.",
        "झारखंड का अधिकांश भाग छोटा नागपुर पठार पर है, जो प्राचीन, घिसे हुए पठारों और पहाड़ियों की श्रृंखला है। मध्य का रांची पठार खड़ी ढलानों से घिरा है, जहाँ नदियाँ हुंडरू, दशम और जोन्हा जैसे झरनों से गिरती हैं; पश्चिम में नेतरहाट के ऊँचे पाट क्षेत्र हैं; जैनों के लिए पवित्र गिरिडीह की पारसनाथ पहाड़ी सबसे ऊँचा बिंदु है; और उत्तर-पूर्व में गंगा के पास राजमहल पहाड़ियाँ उठती हैं, जो राज्य को केवल साहिबगंज में छूती है। दामोदर बोकारो और धनबाद की कोयला पट्टी से होकर पूर्व की ओर बहती है, सुवर्णरेखा रांची और जमशेदपुर को सिंचित करती है, और उत्तरी व दक्षिणी कोयल, बराकर और मयूराक्षी अन्य महत्त्वपूर्ण नदियाँ हैं।",
        "झारखंडचा बहुतांश भाग छोटा नागपूर पठारावर आहे, जो प्राचीन, झिजलेल्या पठारांची व डोंगरांची मालिका आहे. मध्यभागातील रांची पठार तीव्र कड्यांनी वेढलेले आहे, जिथे नद्या हुंडरू, दशम व जोन्हासारख्या धबधब्यांतून कोसळतात; पश्चिमेला नेतरहाटचे उंच पाट प्रदेश आहेत; जैनांसाठी पवित्र असलेली गिरिडीहची पारसनाथ टेकडी हे सर्वोच्च ठिकाण आहे; आणि ईशान्येला गंगेजवळ राजमहल डोंगर उभे आहेत — गंगा राज्याला फक्त साहिबगंज येथे स्पर्श करते. दामोदर बोकारो व धनबादच्या कोळसा पट्ट्यातून पूर्वेकडे वाहते, सुवर्णरेखा रांची व जमशेदपूरला भिजवते, आणि उत्तर व दक्षिण कोयल, बराकर व मयूराक्षी या इतर महत्त्वाच्या नद्या आहेत."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), jh["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("br", "Bihar (north)", "बिहार (उत्तर)", "बिहार (उत्तर)"), it3("wb", "West Bengal (east)", "पश्चिम बंगाल (पूर्व)", "पश्चिम बंगाल (पूर्व)"),
        it3("or", "Odisha (south)", "ओडिशा (दक्षिण)", "ओडिशा (दक्षिण)"), it3("ct", "Chhattisgarh (west)", "छत्तीसगढ़ (पश्चिम)", "छत्तीसगड (पश्चिम)"),
        it3("up", "Uttar Pradesh (north-west)", "उत्तर प्रदेश (उत्तर-पश्चिम)", "उत्तर प्रदेश (वायव्य)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("damodar", "Damodar", "दामोदर", "दामोदर", d=("Flows through the coal belt; dammed by the Damodar Valley Corporation.", "कोयला पट्टी से होकर बहती है; दामोदर घाटी निगम ने इस पर बाँध बनाए हैं।", "कोळसा पट्ट्यातून वाहते; दामोदर खोरे महामंडळाने त्यावर धरणे बांधली आहेत.")),
        it3("subarnarekha", "Subarnarekha", "सुवर्णरेखा", "सुवर्णरेखा", d=("Rises near Ranchi; flows past Jamshedpur to Odisha and the sea.", "रांची के पास से निकलती है; जमशेदपुर से होकर ओडिशा और समुद्र तक बहती है।", "रांचीजवळ उगम; जमशेदपूरमार्गे ओडिशा व समुद्रापर्यंत वाहते.")),
        it3("koel", "North and South Koel", "उत्तरी और दक्षिणी कोयल", "उत्तर व दक्षिण कोयल", d=("North Koel drains Palamu to the Son; South Koel joins the Brahmani.", "उत्तरी कोयल पलामू से सोन तक बहती है; दक्षिणी कोयल ब्राह्मणी से मिलती है।", "उत्तर कोयल पलामूतून सोनला मिळते; दक्षिण कोयल ब्राह्मणीला मिळते.")),
        it3("barakar", "Barakar", "बराकर", "बराकर", d=("Tributary of the Damodar; Tilaiya and Maithon dams.", "दामोदर की सहायक नदी; तिलैया और मैथन बाँध।", "दामोदरची उपनदी; तिलैया व मैथन धरणे.")),
        it3("ganga", "Ganga", "गंगा", "गंगा", d=("Touches the State only in Sahibganj district.", "राज्य को केवल साहिबगंज ज़िले में छूती है।", "राज्याला फक्त साहिबगंज जिल्ह्यात स्पर्श करते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point — official elevation (Parasnath)", "सर्वोच्च बिंदु — आधिकारिक ऊँचाई (पारसनाथ)", "सर्वोच्च शिखर — अधिकृत उंची (पारसनाथ)"), "survey-of-india", "Survey of India."),
        (L("Mineral reserves by mineral", "खनिजवार भंडार", "खनिजनिहाय साठे"), "india-gov", "Indian Bureau of Mines, Indian Minerals Yearbook."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Jharkhand has a tropical monsoon climate, moderated by the plateau's height. Summers (March–June) are hot, especially in the lower north and in Jamshedpur and Dhanbad, while Ranchi and Netarhat stay a little cooler — Ranchi was once the summer capital of Bihar. The south-west monsoon (mid-June to September) brings most of the rain, and thunderstorms with lightning are frequent. Winters (November–February) are pleasant and dry, with cold nights on the plateau.",
        "झारखंड की जलवायु उष्णकटिबंधीय मानसूनी है, जिसे पठार की ऊँचाई कुछ नरम बनाती है। गर्मियाँ (मार्च–जून) गर्म होती हैं, विशेषकर निचले उत्तर और जमशेदपुर व धनबाद में, जबकि रांची और नेतरहाट थोड़े ठंडे रहते हैं — रांची कभी बिहार की ग्रीष्मकालीन राजधानी थी। दक्षिण-पश्चिम मानसून (मध्य जून से सितंबर) अधिकांश वर्षा लाता है, और आकाशीय बिजली के साथ आँधी-तूफ़ान आम हैं। सर्दियाँ (नवंबर–फ़रवरी) सुहावनी और सूखी होती हैं, और पठार पर रातें ठंडी।",
        "झारखंडचे हवामान उष्णकटिबंधीय मान्सूनचे आहे, जे पठाराच्या उंचीमुळे काहीसे सौम्य होते. उन्हाळा (मार्च–जून) उष्ण असतो, विशेषतः खालच्या उत्तर भागात व जमशेदपूर-धनबादमध्ये, तर रांची व नेतरहाट थोडे थंड राहतात — रांची एकेकाळी बिहारची उन्हाळी राजधानी होती. नैर्ऋत्य मान्सून (जूनच्या मध्यापासून सप्टेंबरपर्यंत) बहुतेक पाऊस आणतो, आणि विजांसह वादळे वारंवार होतात. हिवाळा (नोव्हेंबर–फेब्रुवारी) आल्हाददायक व कोरडा असतो, आणि पठारावर रात्री थंड असतात."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Ranchi", "रांची", "रांची"), "lat": 23.3441, "lon": 85.3096},
        {"name": L("Jamshedpur", "जमशेदपुर", "जमशेदपूर"), "lat": 22.8046, "lon": 86.2029},
        {"name": L("Dhanbad", "धनबाद", "धनबाद"), "lat": 23.7957, "lon": 86.4304},
        {"name": L("Deoghar", "देवघर", "देवघर"), "lat": 24.4852, "lon": 86.6948},
    ]},
    lst("best", [
        it3("winter", "October to March", "अक्टूबर से मार्च", "ऑक्टोबर ते मार्च", d=("Best for waterfalls after the rains, Netarhat sunrises and Betla; Sohrai and Tusu festivals.", "बारिश के बाद झरनों, नेतरहाट के सूर्योदय और बेतला के लिए सबसे अच्छा; सोहराय और टुसू त्योहार।", "पावसानंतरचे धबधबे, नेतरहाटचा सूर्योदय व बेतलासाठी उत्तम; सोहराय व टुसू सण.")),
        it3("spring", "March to April", "मार्च से अप्रैल", "मार्च ते एप्रिल", d=("Sarhul and the flowering of sal and palash.", "सरहुल और साल व पलाश का फूलना।", "सरहुल आणि साल व पळसाचा बहर.")),
        it3("monsoon", "July to August", "जुलाई से अगस्त", "जुलै ते ऑगस्ट", d=("Shravani Mela at Deoghar; lush green plateau.", "देवघर में श्रावणी मेला; हरा-भरा पठार।", "देवघर येथे श्रावणी मेळा; हिरवेगार पठार.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (Jharkhand sub-division)", "सामान्य वार्षिक वर्षा (झारखंड उप-मंडल)", "सरासरी वार्षिक पाऊस (झारखंड उपविभाग)"), "imd", "IMD rainfall statistics."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Life in Jharkhand moves between the village and the mine. In Adivasi villages, the akhra — the dancing ground — fills with drums and dancers at Sarhul and Karma, weekly haats bring together farmers, forest produce and craftspeople, and the sacred grove (sarna) is at the heart of community life. In the industrial towns, shift whistles at the steel plants of Jamshedpur and Bokaro and the collieries of Dhanbad mark the day, and Jamshedpur's tree-lined planned streets are a contrast to the busy coal towns. Dhuska with curry, litti, and seasonal mushrooms (rugra) and bamboo shoots are local favourites, and the language of the street mixes Hindi with Nagpuri, Khortha and Santali.",
        "झारखंड का जीवन गाँव और खदान के बीच चलता है। आदिवासी गाँवों में अखड़ा — नृत्य का मैदान — सरहुल और करमा पर ढोल और नर्तकों से भर जाता है, साप्ताहिक हाट किसानों, वनोपज और कारीगरों को एक साथ लाते हैं, और पवित्र उपवन (सरना) सामुदायिक जीवन का केंद्र है। औद्योगिक नगरों में जमशेदपुर और बोकारो के इस्पात संयंत्रों और धनबाद की कोलियरियों की पाली की सीटियाँ दिन तय करती हैं, और जमशेदपुर की पेड़ों से घिरी नियोजित सड़कें व्यस्त कोयला नगरों से अलग हैं। करी के साथ धुस्का, लिट्टी, और मौसमी मशरूम (रुगड़ा) व बाँस की कोंपलें स्थानीय पसंद हैं, और गली की बोली में हिंदी के साथ नागपुरी, खोरठा और संताली घुली-मिली है।",
        "झारखंडचे जीवन गाव व खाण यांच्यामध्ये चालते. आदिवासी गावांत अखडा — नृत्याचे मैदान — सरहुल व करमाला ढोल व नर्तकांनी भरून जाते, आठवडी बाजार शेतकरी, वनोपज व कारागिरांना एकत्र आणतात, आणि पवित्र देवराई (सरना) सामुदायिक जीवनाचे केंद्र आहे. औद्योगिक शहरांत जमशेदपूर व बोकारोच्या पोलाद कारखान्यांच्या आणि धनबादच्या कोळसा खाणींच्या पाळीच्या शिट्ट्या दिवस ठरवतात, आणि जमशेदपूरचे झाडांनी वेढलेले नियोजित रस्ते गजबजलेल्या कोळसा शहरांपेक्षा वेगळे आहेत. करीसोबत धुस्का, लिट्टी, आणि हंगामी अळंबी (रुगडा) व बांबूचे कोंब हे स्थानिक आवडीचे पदार्थ आहेत, आणि रस्त्यावरच्या बोलीत हिंदीसोबत नागपुरी, खोरठा व संताली मिसळलेल्या असतात."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Jharkhand had 3.30 crore people at the 2011 Census, with about 414 people per km². The sex ratio was 948 women per 1,000 men, and the child sex ratio fell from 965 in 2001 to 948. Literacy rose sharply, from 53.6% in 2001 to 66.4% in 2011, but was still below the national 73.0%. Scheduled Tribes made up 26.2% of the population — among the highest shares outside the north-east — and Scheduled Castes 12.1%.\n\nThe largest tribal communities are the Santhal, Oraon, Munda and Ho, and the State also has several particularly vulnerable tribal groups such as the Asur, Birhor and Sauria Paharia. Santali is a scheduled language, and Mundari, Ho, Kurukh, Kharia, Nagpuri, Khortha, Kurmali and Panchpargania are widely spoken alongside Hindi, Urdu, Bengali and Odia.",
        "2011 की जनगणना में झारखंड की जनसंख्या 3.30 करोड़ थी, और प्रति वर्ग किमी लगभग 414 लोग। लिंगानुपात प्रति 1,000 पुरुषों पर 948 महिलाएँ था, और शिशु लिंगानुपात 2001 के 965 से घटकर 948 हो गया। साक्षरता 2001 के 53.6% से तेज़ी से बढ़कर 2011 में 66.4% हुई, लेकिन फिर भी राष्ट्रीय 73.0% से कम थी। अनुसूचित जनजातियाँ जनसंख्या का 26.2% थीं — पूर्वोत्तर के बाहर सबसे ऊँचे हिस्सों में — और अनुसूचित जातियाँ 12.1%।\n\nसबसे बड़े जनजातीय समुदाय संथाल, उरांव, मुंडा और हो हैं, और राज्य में असुर, बिरहोर और सौरिया पहाड़िया जैसे कई विशेष रूप से कमज़ोर जनजातीय समूह भी हैं। संताली अनुसूचित भाषा है, और हिंदी, उर्दू, बांग्ला और ओड़िया के साथ मुंडारी, हो, कुड़ुख, खड़िया, नागपुरी, खोरठा, कुरमाली और पंचपरगनिया व्यापक रूप से बोली जाती हैं।",
        "2011 च्या जनगणनेनुसार झारखंडची लोकसंख्या 3.30 कोटी होती, आणि प्रति चौ.किमी सुमारे 414 लोक. दर 1,000 पुरुषांमागे 948 स्त्रिया होत्या, आणि बाल लिंग गुणोत्तर 2001 मधील 965 वरून 948 वर घसरले. साक्षरता 2001 मधील 53.6% वरून 2011 मध्ये 66.4% पर्यंत वेगाने वाढली, पण तरीही राष्ट्रीय 73.0% पेक्षा कमी होती. अनुसूचित जमाती लोकसंख्येच्या 26.2% होत्या — ईशान्येबाहेरील सर्वाधिक वाट्यांपैकी — आणि अनुसूचित जाती 12.1%.\n\nसंथाल, ओराव, मुंडा व हो हे सर्वांत मोठे आदिवासी समुदाय आहेत, आणि राज्यात असुर, बिरहोर व सौरिया पहाडिया यांसारखे अनेक विशेष असुरक्षित आदिवासी गटही आहेत. संताली ही अनुसूचित भाषा आहे, आणि हिंदी, उर्दू, बंगाली व ओडियासोबत मुंडारी, हो, कुडुख, खडिया, नागपुरी, खोरठा, कुरमाली व पंचपरगनिया मोठ्या प्रमाणावर बोलल्या जातात."),
        sources=["census", "es-india", "dl-planning"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), jh["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), jh["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(941, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), jh["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(965, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), jh["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"],
             previous=dp(53.6, "%", "2001", "census", "es-india", "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf")),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), jh["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(12.1, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 39.86 lakh people."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(26.2, "%", "2011", "census", "dl-planning", SCST, note="Same table: 86.45 lakh people."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("hi", "Hindi", "हिंदी", "हिंदी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("sat", "Santali", "संताली", "संताली", m=("Scheduled language", "अनुसूचित भाषा", "अनुसूचित भाषा")),
        it3("ur", "Urdu", "उर्दू", "उर्दू"), it3("bn", "Bengali", "बांग्ला", "बंगाली"),
        it3("unr", "Mundari", "मुंडारी", "मुंडारी"), it3("hoc", "Ho", "हो", "हो"), it3("kru", "Kurukh", "कुड़ुख", "कुडुख"),
        it3("sck", "Nagpuri (Sadri)", "नागपुरी (सादरी)", "नागपुरी (सादरी)"), it3("kho", "Khortha", "खोरठा", "खोरठा"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Final Population Totals for Jharkhand."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Second official languages — notification", "द्वितीय राजभाषाएँ — अधिसूचना", "द्वितीय राजभाषा — अधिसूचना"), "india-gov", "Jharkhand Official Language (Amendment) Acts; list the languages as notified."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "The Chota Nagpur plateau has been home to Munda, Oraon, Ho, Santhal and other peoples for millennia, and its forests long sheltered them from outside rule; the Nagvanshi rulers of Chota Nagpur and the Cheros of Palamu were among the local dynasties. The East India Company gained control in the late 18th century, and the region's history under British rule is marked by resistance to land-grabbing by outside landlords and moneylenders: the Kol uprising of 1831–32, the Santhal Hul of 1855 led by Sidhu and Kanhu Murmu, and Birsa Munda's ulgulan of 1899–1900. These led to protective laws such as the Chota Nagpur Tenancy Act of 1908.\n\nIndustry arrived early: Jharia's coal was mined from the 1890s, and Jamsetji Tata's vision led to the Tata steel works at Sakchi, later Jamshedpur, in 1907. After independence, the region remained part of Bihar. The Jharkhand Party of Jaipal Singh Munda and later the Jharkhand Mukti Morcha led a long movement for a separate State, achieved on 15 November 2000.",
        "छोटा नागपुर पठार हज़ारों वर्षों से मुंडा, उरांव, हो, संथाल और अन्य लोगों का घर रहा है, और इसके वनों ने लंबे समय तक उन्हें बाहरी शासन से बचाए रखा; छोटा नागपुर के नागवंशी शासक और पलामू के चेरो स्थानीय राजवंशों में थे। ईस्ट इंडिया कंपनी ने 18वीं सदी के अंत में नियंत्रण पाया, और ब्रिटिश शासन में इस क्षेत्र का इतिहास बाहरी ज़मींदारों और महाजनों द्वारा भूमि हड़पने के प्रतिरोध से भरा है: 1831–32 का कोल विद्रोह, सिद्धू और कान्हू मुर्मू के नेतृत्व में 1855 का संथाल हूल, और 1899–1900 में बिरसा मुंडा का उलगुलान। इनसे 1908 के छोटा नागपुर काश्तकारी अधिनियम जैसे संरक्षणकारी क़ानून बने।\n\nउद्योग जल्दी आया: झरिया का कोयला 1890 के दशक से निकाला गया, और जमशेदजी टाटा की दूरदृष्टि से 1907 में साकची, बाद के जमशेदपुर, में टाटा इस्पात कारख़ाना बना। स्वतंत्रता के बाद यह क्षेत्र बिहार का हिस्सा रहा। जयपाल सिंह मुंडा की झारखंड पार्टी और बाद में झारखंड मुक्ति मोर्चा ने अलग राज्य के लिए लंबा आंदोलन चलाया, जो 15 नवंबर 2000 को साकार हुआ।",
        "छोटा नागपूर पठार हजारो वर्षांपासून मुंडा, ओराव, हो, संथाल व इतर लोकांचे घर आहे, आणि त्याच्या जंगलांनी त्यांना दीर्घकाळ बाहेरच्या सत्तेपासून सुरक्षित ठेवले; छोटा नागपूरचे नागवंशी राजे व पलामूचे चेरो हे स्थानिक राजघराण्यांपैकी होते. ईस्ट इंडिया कंपनीने अठराव्या शतकाच्या अखेरीस नियंत्रण मिळवले, आणि ब्रिटिश राजवटीतील या प्रदेशाचा इतिहास बाहेरच्या जमीनदार व सावकारांनी केलेल्या जमीन बळकावणीविरुद्धच्या प्रतिकाराने भरलेला आहे: 1831–32 चा कोल उठाव, सिद्धू व कान्हू मुर्मू यांच्या नेतृत्वाखालील 1855 चा संथाल हूल, आणि 1899–1900 मधील बिरसा मुंडांचे उलगुलान. यांतून 1908 च्या छोटा नागपूर कूळ कायद्यासारखे संरक्षक कायदे झाले.\n\nउद्योग लवकर आले: झरियाचा कोळसा 1890 च्या दशकापासून काढला गेला, आणि जमशेदजी टाटांच्या दूरदृष्टीतून 1907 मध्ये साकची — नंतरचे जमशेदपूर — येथे टाटांचा पोलाद कारखाना उभा राहिला. स्वातंत्र्यानंतर हा प्रदेश बिहारचा भाग राहिला. जयपाल सिंह मुंडांच्या झारखंड पक्षाने व नंतर झारखंड मुक्ती मोर्चाने स्वतंत्र राज्यासाठी दीर्घ चळवळ चालवली, जी 15 नोव्हेंबर 2000 रोजी साकार झाली."),
        conf="Editorial"),
    timeline([
        ev("kol", 1831, L("1831–32", "1831–32", "1831–32"), L("Kol uprising", "कोल विद्रोह", "कोल उठाव")),
        ev("hul", 1855, L("30 June 1855", "30 जून 1855", "30 जून 1855"), L("Santhal Hul led by Sidhu and Kanhu", "सिद्धू और कान्हू के नेतृत्व में संथाल हूल", "सिद्धू व कान्हू यांच्या नेतृत्वाखाली संथाल हूल")),
        ev("ulgulan", 1899, L("1899–1900", "1899–1900", "1899–1900"), L("Birsa Munda's ulgulan", "बिरसा मुंडा का उलगुलान", "बिरसा मुंडांचे उलगुलान")),
        ev("tata", 1907, L("1907", "1907", "1907"), L("Tata steel works founded at Sakchi (Jamshedpur)", "साकची (जमशेदपुर) में टाटा इस्पात कारख़ाने की स्थापना", "साकची (जमशेदपूर) येथे टाटा पोलाद कारखान्याची स्थापना")),
        ev("cnt", 1908, L("1908", "1908", "1908"), L("Chota Nagpur Tenancy Act", "छोटा नागपुर काश्तकारी अधिनियम", "छोटा नागपूर कूळ कायदा")),
        ev("dvc", 1948, L("1948", "1948", "1948"), L("Damodar Valley Corporation set up", "दामोदर घाटी निगम की स्थापना", "दामोदर खोरे महामंडळाची स्थापना")),
        ev("state", 2000, L("15 November 2000", "15 नवंबर 2000", "15 नोव्हेंबर 2000"), L("Jharkhand State formed", "झारखंड राज्य बना", "झारखंड राज्याची निर्मिती")),
        ev("cm2024", 2024, L("28 November 2024", "28 नवंबर 2024", "28 नोव्हेंबर 2024"), L("Hemant Soren sworn in for a fourth term", "हेमंत सोरेन ने चौथी बार शपथ ली", "हेमंत सोरेन यांचा चौथ्यांदा शपथविधी")),
    ]),
    lst("heritage", [
        it3("baidyanath", "Baidyanath Dham, Deoghar", "बैद्यनाथ धाम, देवघर", "बैद्यनाथ धाम, देवघर", m=("Jyotirlinga", "ज्योतिर्लिंग", "ज्योतिर्लिंग")),
        it3("parasnath", "Shikharji, Parasnath hill", "शिखरजी, पारसनाथ पहाड़ी", "शिखरजी, पारसनाथ टेकडी", m=("Jain pilgrimage", "जैन तीर्थ", "जैन तीर्थ")),
        it3("maluti", "Maluti temples", "मलूटी मंदिर", "मलूटी मंदिरे", m=("Terracotta temples, Dumka", "टेराकोटा मंदिर, दुमका", "टेराकोटा मंदिरे, दुमका")),
        it3("palamu", "Palamu forts", "पलामू क़िले", "पलामू किल्ले", m=("Chero dynasty", "चेरो राजवंश", "चेरो राजघराणे")),
        it3("rajrappa", "Chhinnamasta temple, Rajrappa", "छिन्नमस्तिका मंदिर, रजरप्पा", "छिन्नमस्ता मंदिर, रजरप्पा", m=("Damodar–Bhairavi confluence", "दामोदर–भैरवी संगम", "दामोदर–भैरवी संगम")),
        it3("ulihatu", "Ulihatu", "उलिहातु", "उलिहातू", m=("Birthplace of Birsa Munda", "बिरसा मुंडा का जन्मस्थान", "बिरसा मुंडांचे जन्मस्थान")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("jh mod1 ok")
