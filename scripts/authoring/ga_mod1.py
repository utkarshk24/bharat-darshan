"""Goa modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-GA"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
KUSH = "https://www.thegoan.net/goa-news/govt-notifies-creation-of-third-district-‘kushavati’/141285.html"
ga = read("regions/IN-GA.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Goa is India's smallest State by area, a strip of coast on the Konkan shore of the Arabian Sea between Maharashtra to the north and Karnataka to the east and south. Its land rises from beaches, estuaries and paddy fields through laterite plateaus to the forested Western Ghats along the eastern border. It had 14.6 lakh people at the 2011 Census. Panaji (Panjim) on the Mandovi is the capital; Margao, Vasco da Gama, Mapusa and Ponda are the other main towns.\n\nGoa was ruled by Portugal for about 450 years, until it became part of India on 19 December 1961. It was a Union Territory together with Daman and Diu until it became India's 25th State on 30 May 1987. Konkani in the Devanagari script is the official language, and Marathi is also used for official purposes.",
        "गोवा क्षेत्रफल की दृष्टि से भारत का सबसे छोटा राज्य है, अरब सागर के कोंकण तट की एक पट्टी, जिसके उत्तर में महाराष्ट्र और पूर्व व दक्षिण में कर्नाटक है। इसकी भूमि समुद्र तटों, मुहानों और धान के खेतों से लैटेराइट पठारों होते हुए पूर्वी सीमा पर वनाच्छादित पश्चिमी घाट तक उठती है। 2011 की जनगणना में इसकी जनसंख्या 14.6 लाख थी। मांडवी किनारे पणजी राजधानी है; मडगाँव, वास्को द गामा, म्हापसा और फोंडा अन्य मुख्य नगर हैं।\n\nगोवा पर लगभग 450 वर्ष तक पुर्तगाल का शासन रहा, जब तक 19 दिसंबर 1961 को यह भारत का हिस्सा नहीं बना। यह दमन और दीव के साथ केंद्र शासित प्रदेश रहा, जब तक 30 मई 1987 को यह भारत का 25वाँ राज्य नहीं बना। देवनागरी लिपि में कोंकणी राजभाषा है, और मराठी का भी आधिकारिक कार्यों में उपयोग होता है।",
        "गोवा हे क्षेत्रफळाने भारतातील सर्वांत लहान राज्य आहे, अरबी समुद्राच्या कोकण किनाऱ्यावरील एक पट्टी, ज्याच्या उत्तरेला महाराष्ट्र व पूर्व आणि दक्षिणेला कर्नाटक आहे. त्याची जमीन किनारे, खाड्या व भातशेतांपासून जांभ्या दगडाच्या पठारांमधून पूर्व सीमेवरील जंगलांनी झाकलेल्या पश्चिम घाटापर्यंत चढते. 2011 च्या जनगणनेनुसार त्याची लोकसंख्या 14.6 लाख होती. मांडवीकाठचे पणजी ही राजधानी आहे; मडगाव, वास्को द गामा, म्हापसा व फोंडा ही इतर मुख्य शहरे आहेत.\n\nगोव्यावर सुमारे 450 वर्षे पोर्तुगालचे राज्य होते, 19 डिसेंबर 1961 रोजी ते भारताचा भाग होईपर्यंत. दमण व दीवसह ते केंद्रशासित प्रदेश होते, 30 मे 1987 रोजी भारताचे 25 वे राज्य होईपर्यंत. देवनागरी लिपीतील कोकणी ही राजभाषा आहे, आणि मराठीचाही अधिकृत कामकाजात वापर होतो."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Goa's blend of Konkani, Portuguese and wider Indian influences is unlike anywhere else in India. Whitewashed churches and Baroque cathedrals stand near ancient temples of Mangeshi and Shantadurga; villages still have Indo-Portuguese houses with balcões and azulejo tiles; and the Carnival, the Shigmo festival and the feast of St Francis Xavier draw crowds. Its beaches made it one of India's best-known holiday destinations, and its cuisine — fish curry and rice, xacuti, vindaloo, bebinca and cashew feni — is famous. Goa has the second-highest per capita income of any State or UT in the MoSPI series, high literacy, and over 60% forest cover in the Western Ghats.",
        "कोंकणी, पुर्तगाली और व्यापक भारतीय प्रभावों का गोवा का मेल भारत में कहीं और जैसा नहीं है। सफ़ेद चर्च और बारोक कैथेड्रल मंगेशी और शांतादुर्गा के प्राचीन मंदिरों के पास खड़े हैं; गाँवों में आज भी बालकनियों (बालकाओ) और अज़ुलेजो टाइलों वाले भारतीय-पुर्तगाली घर हैं; और कार्निवल, शिगमो उत्सव और संत फ़्रांसिस ज़ेवियर का पर्व भीड़ खींचते हैं। इसके समुद्र तटों ने इसे भारत के सबसे प्रसिद्ध छुट्टियों के गंतव्यों में बनाया, और इसका भोजन — मछली करी और चावल, शाकुती, विंदालू, बेबिंका और काजू फ़ेनी — प्रसिद्ध है। मोस्पी शृंखला में गोवा की प्रति व्यक्ति आय किसी भी राज्य या केंद्र शासित प्रदेश में दूसरी सबसे अधिक है, साक्षरता ऊँची है, और पश्चिमी घाट में 60% से अधिक वन आवरण है।",
        "कोकणी, पोर्तुगीज व व्यापक भारतीय प्रभावांचा गोव्याचा संगम भारतात इतरत्र कुठेही नाही. चुना लावलेली चर्च व बरोक कॅथेड्रल मंगेशी व शांतादुर्गेच्या प्राचीन मंदिरांजवळ उभी आहेत; गावांत आजही बाल्कांव व अझुलेजो फरशांची इंडो-पोर्तुगीज घरे आहेत; आणि कार्निव्हल, शिगमो उत्सव व संत फ्रान्सिस झेविअरचे फेस्त गर्दी खेचतात. त्याच्या किनाऱ्यांमुळे ते भारतातील सर्वांत प्रसिद्ध सुट्टीच्या ठिकाणांपैकी एक बनले, आणि त्याचे खाद्य — माशांची आमटी व भात, शागुती, विंदालू, बेबिंका व काजू फेणी — प्रसिद्ध आहे. मोस्पी मालिकेत गोव्याचे दरडोई उत्पन्न कोणत्याही राज्य वा केंद्रशासित प्रदेशात दुसऱ्या क्रमांकाचे आहे, साक्षरता उच्च आहे, आणि पश्चिम घाटात 60% हून अधिक वनाच्छादन आहे."),
        title=L("What makes Goa unique?", "गोवा को ख़ास क्या बनाता है?", "गोव्याचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Statehood", "राज्य का दर्जा", "राज्याचा दर्जा"), L("30 May 1987 (Goa Statehood Day); Liberation Day 19 December", "30 मई 1987 (गोवा राज्य दिवस); मुक्ति दिवस 19 दिसंबर", "30 मे 1987 (गोवा राज्य दिन); मुक्तिदिन 19 डिसेंबर")],
           [L("Districts / talukas", "ज़िले / तालुका", "जिल्हे / तालुके"), L("3 (North Goa, South Goa, Kushavati) / 12", "3 (उत्तर गोवा, दक्षिण गोवा, कुशावती) / 12", "3 (उत्तर गोवा, दक्षिण गोवा, कुशावती) / 12")],
           [L("Capital", "राजधानी", "राजधानी"), L("Panaji", "पणजी", "पणजी")],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Konkani (Devanagari); Marathi also used for official purposes", "कोंकणी (देवनागरी); मराठी का भी आधिकारिक उपयोग", "कोकणी (देवनागरी); मराठीचाही अधिकृत वापर")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Bombay High Court, bench at Porvorim (Goa)", "बॉम्बे उच्च न्यायालय, पोरवोरिम (गोवा) पीठ", "मुंबई उच्च न्यायालय, पर्वरी (गोवा) खंडपीठ")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "GA"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; Kushavati district (Quepem, Sanguem, Dharbandora and Canacona talukas) was notified at the end of December 2025.", "संपादकीय; कुशावती ज़िला (केपे, सांगे, धारबांदोड़ा और काणकोण तालुके) दिसंबर 2025 के अंत में अधिसूचित हुआ।", "संपादकीय; कुशावती जिल्हा (केपे, सांगे, धारबांदोडा व काणकोण तालुके) डिसेंबर 2025 च्या अखेरीस अधिसूचित झाला.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Goa has about 100 km of coastline, broken by the estuaries of the Terekhol, Chapora, Mandovi, Zuari, Sal, Talpona and Galgibag rivers. Behind the beaches lie khazan lands — reclaimed estuarine fields protected by sluice gates — and paddy and coconut groves, then a midland of laterite plateaus and hills, and finally the Sahyadri (Western Ghats) in the east, where Sonsogor is among the highest points and the Dudhsagar falls plunge down the Mandovi's headwaters. The Mandovi and Zuari, linked by the Cumbarjua canal, make Tiswadi (Ilhas) an island, and Mormugao is one of India's oldest natural harbours.",
        "गोवा की लगभग 100 किमी लंबी तटरेखा तेरेखोल, शापोरा, मांडवी, जुवारी, साल, तळपोणा और गालजीबाग नदियों के मुहानों से कटी है। समुद्र तटों के पीछे खाज़न भूमि है — जलद्वारों (मानसों) से सुरक्षित, मुहाने से प्राप्त खेत — और धान व नारियल के बाग़, फिर लैटेराइट पठारों और पहाड़ियों का मध्य क्षेत्र, और अंत में पूर्व में सह्याद्रि (पश्चिमी घाट), जहाँ सोनसोगोड सबसे ऊँचे स्थानों में है और दूधसागर जलप्रपात मांडवी के उद्गम क्षेत्र में गिरता है। कुंबारजुआ नहर से जुड़ी मांडवी और जुवारी तिसवाड़ी (इल्हास) को द्वीप बनाती हैं, और मुरगाँव भारत के सबसे पुराने प्राकृतिक बंदरगाहों में है।",
        "गोव्याची सुमारे 100 किमी लांबीची किनारपट्टी तेरेखोल, शापोरा, मांडवी, जुवारी, साळ, तळपण व गालजीबाग नद्यांच्या खाड्यांनी तुटलेली आहे. किनाऱ्यांच्या मागे खाजन जमीन आहे — मानशींनी (जलद्वारांनी) संरक्षित, खाडीतून मिळवलेली शेते — आणि भात व माडांच्या बागा, नंतर जांभ्या दगडाच्या पठारांचा व टेकड्यांचा मधला प्रदेश, आणि शेवटी पूर्वेला सह्याद्री (पश्चिम घाट), जिथे सोनसोगड हे सर्वांत उंच ठिकाणांपैकी आहे आणि दूधसागर धबधबा मांडवीच्या उगम प्रदेशात कोसळतो. कुंभारजुवे कालव्याने जोडलेल्या मांडवी व जुवारीमुळे तिसवाडी (इल्हास) बेट बनते, आणि मुरगाव हे भारतातील सर्वांत जुन्या नैसर्गिक बंदरांपैकी एक आहे."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), ga["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("mh", "Maharashtra (north)", "महाराष्ट्र (उत्तर)", "महाराष्ट्र (उत्तर)"), it3("ka", "Karnataka (east and south)", "कर्नाटक (पूर्व और दक्षिण)", "कर्नाटक (पूर्व व दक्षिण)"),
        it3("sea", "Arabian Sea (west)", "अरब सागर (पश्चिम)", "अरबी समुद्र (पश्चिम)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("mandovi", "Mandovi (Mhadei)", "मांडवी (म्हादई)", "मांडवी (म्हादई)", d=("Rises in Karnataka as the Mhadei; flows past Panaji to the sea.", "कर्नाटक में म्हादई के रूप में निकलती है; पणजी से होकर समुद्र में मिलती है।", "कर्नाटकात म्हादई म्हणून उगम; पणजीजवळून समुद्राला मिळते.")),
        it3("zuari", "Zuari", "जुवारी", "जुवारी", d=("Broad estuary between Tiswadi and Mormugao.", "तिसवाड़ी और मुरगाँव के बीच चौड़ा मुहाना।", "तिसवाडी व मुरगावदरम्यानची रुंद खाडी.")),
        it3("chapora", "Chapora", "शापोरा", "शापोरा", d=("North Goa river below Chapora fort.", "शापोरा क़िले के नीचे उत्तर गोवा की नदी।", "शापोरा किल्ल्याखालील उत्तर गोव्याची नदी.")),
        it3("terekhol", "Terekhol", "तेरेखोल", "तेरेखोल", d=("Border river with Maharashtra.", "महाराष्ट्र के साथ सीमा नदी।", "महाराष्ट्रसोबतची सीमानदी.")),
        it3("sal", "Sal", "साल", "साळ", d=("Flows along the Salcete coast to Mobor.", "सासष्टी तट के साथ मोबोर तक बहती है।", "सासष्टी किनाऱ्याने मोबोरपर्यंत वाहते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Coastline length — official figure", "तटरेखा की लंबाई — आधिकारिक आँकड़ा", "किनारपट्टीची लांबी — अधिकृत आकडा"), "survey-of-india", "Survey of India / Goa Coastal Zone Management Authority."),
        (L("Highest point — official elevation", "सर्वोच्च बिंदु — आधिकारिक ऊँचाई", "सर्वोच्च शिखर — अधिकृत उंची"), "survey-of-india", "Survey of India."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Goa has a warm, humid tropical climate. The south-west monsoon, from June to September, brings very heavy rain — more in the Ghats than on the coast — and turns the land a deep green, while the sea is rough and beaches are closed to swimming. October to February is dry and pleasant with sea breezes, and March to May is hot and humid. Cyclones in the Arabian Sea occasionally bring high winds and storm surges.",
        "गोवा की जलवायु गर्म, आर्द्र उष्णकटिबंधीय है। जून से सितंबर तक दक्षिण-पश्चिम मानसून बहुत भारी वर्षा लाता है — तट से अधिक घाटों में — और भूमि को गहरा हरा कर देता है, जबकि समुद्र उग्र रहता है और समुद्र तटों पर तैरना बंद रहता है। अक्टूबर से फ़रवरी सूखा और सुहावना होता है, समुद्री हवाओं के साथ, और मार्च से मई गर्म व उमस भरा। अरब सागर के चक्रवात कभी-कभी तेज़ हवाएँ और तूफ़ानी लहरें लाते हैं।",
        "गोव्याचे हवामान उष्ण, दमट उष्णकटिबंधीय आहे. जून ते सप्टेंबर नैर्ऋत्य मान्सून अतिशय मुसळधार पाऊस आणतो — किनाऱ्यापेक्षा घाटांत अधिक — आणि जमीन गडद हिरवीगार करतो, तर समुद्र खवळलेला असतो व किनाऱ्यांवर पोहणे बंद असते. ऑक्टोबर ते फेब्रुवारी कोरडा व आल्हाददायक काळ असतो, समुद्री वाऱ्यांसह, आणि मार्च ते मे उष्ण व दमट. अरबी समुद्रातील चक्रीवादळे कधीकधी जोरदार वारे व वादळी लाटा आणतात."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Panaji", "पणजी", "पणजी"), "lat": 15.4909, "lon": 73.8278},
        {"name": L("Margao", "मडगाँव", "मडगाव"), "lat": 15.2832, "lon": 73.9862},
        {"name": L("Mapusa", "म्हापसा", "म्हापसा"), "lat": 15.5937, "lon": 73.8142},
        {"name": L("Canacona", "काणकोण", "काणकोण"), "lat": 15.0108, "lon": 74.0444},
    ]},
    lst("best", [
        it3("winter", "November to February", "नवंबर से फ़रवरी", "नोव्हेंबर ते फेब्रुवारी", d=("Beach season; Christmas, New Year and Carnival.", "समुद्र तट का मौसम; क्रिसमस, नव वर्ष और कार्निवल।", "किनाऱ्यांचा हंगाम; नाताळ, नववर्ष व कार्निव्हल.")),
        it3("monsoon", "June to September", "जून से सितंबर", "जून ते सप्टेंबर", d=("Green landscapes, Dudhsagar in full flow and São João; no sea swimming.", "हरे-भरे भूदृश्य, पूरे वेग में दूधसागर और साओ जोआओ; समुद्र में तैरना नहीं।", "हिरवीगार भूदृश्ये, पूर्ण भरलेला दूधसागर व सांजाव; समुद्रात पोहणे नाही.")),
        it3("spring", "March", "मार्च", "मार्च", d=("Shigmo processions; cashew and mango season begins.", "शिगमो शोभायात्राएँ; काजू और आम का मौसम शुरू।", "शिगमो मिरवणुका; काजू व आंब्याचा हंगाम सुरू.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall", "सामान्य वार्षिक वर्षा", "सरासरी वार्षिक पाऊस"), "imd", "IMD Goa meteorological centre."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Goa is relaxed — susegad, as Goans say. Mornings begin with the poder's bicycle horn as he delivers fresh poi and pao, afternoons slow down for a siesta, and evenings fill village taverns and beach shacks. Village feasts, temple zatras and church fests are celebrated by everyone, and Konkani tiatr plays and mando songs remain popular. Markets in Mapusa and Margao sell fish, sausages, spices and seasonal mangoes and cashews; in the hinterland, spice plantations, temples and quiet villages contrast with the busy beaches of the north.",
        "गोवा सहज और आरामपसंद है — जैसा गोवावासी कहते हैं, सुशेगाद। सुबह ताज़ा पोई और पाव पहुँचाने वाले पोदेर की साइकिल के भोंपू से शुरू होती है, दोपहर आराम के लिए धीमी हो जाती है, और शाम को गाँव के मैख़ाने और समुद्र तट के शैक भर जाते हैं। गाँव के उत्सव, मंदिरों की जात्राएँ और चर्च के फ़ेस्त सब मनाते हैं, और कोंकणी तियात्र नाटक और मांडो गीत आज भी लोकप्रिय हैं। म्हापसा और मडगाँव के बाज़ार मछली, सॉसेज, मसाले और मौसमी आम व काजू बेचते हैं; भीतरी इलाक़ों में मसाला बाग़ान, मंदिर और शांत गाँव उत्तर के व्यस्त समुद्र तटों से अलग दिखते हैं।",
        "गोवा निवांत आहे — गोंयकार म्हणतात तसे सुशेगाद. सकाळ ताजे पोई व पाव घेऊन येणाऱ्या पोदेराच्या सायकलच्या भोंग्याने सुरू होते, दुपार विश्रांतीसाठी संथ होते, आणि संध्याकाळी गावच्या ताबरनी व किनाऱ्यावरील शॅक भरतात. गावचे उत्सव, देवळांच्या जत्रा व चर्चचे फेस्त सगळे साजरे करतात, आणि कोकणी तियात्र नाटके व मांडो गीते आजही लोकप्रिय आहेत. म्हापसा व मडगावचे बाजार मासे, सॉसेज, मसाले व हंगामी आंबे आणि काजू विकतात; आतल्या भागात मसाल्यांच्या बागा, देवळे व शांत गावे उत्तरेच्या गजबजलेल्या किनाऱ्यांपेक्षा वेगळी भासतात."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Goa had 14.6 lakh people at the 2011 Census, with about 394 people per km². Its sex ratio was 973 women per 1,000 men and its child sex ratio 942, both up from 2001, and literacy was 88.7% — among the highest in India. Scheduled Castes made up only 1.7% of the population, and Scheduled Tribes 10.2% — mainly the Gawda, Kunbi and Velip communities, who were notified as Scheduled Tribes in 2003.\n\nKonkani is the mother tongue of most Goans, written in Devanagari and, among many Catholics, in the Roman script; Marathi is widely read and spoken, and English, Hindi, Kannada and Urdu are also common. Portuguese is still known by some older Goans.",
        "2011 की जनगणना में गोवा की जनसंख्या 14.6 लाख थी, और प्रति वर्ग किमी लगभग 394 लोग। लिंगानुपात प्रति 1,000 पुरुषों पर 973 महिलाएँ और शिशु लिंगानुपात 942 था, दोनों 2001 से अधिक, और साक्षरता 88.7% थी — भारत में सबसे ऊँची में। अनुसूचित जातियाँ जनसंख्या का केवल 1.7% थीं, और अनुसूचित जनजातियाँ 10.2% — मुख्यतः गावडा, कुणबी और वेळीप समुदाय, जिन्हें 2003 में अनुसूचित जनजाति के रूप में अधिसूचित किया गया।\n\nअधिकांश गोवावासियों की मातृभाषा कोंकणी है, जो देवनागरी में और कई कैथोलिकों में रोमन लिपि में लिखी जाती है; मराठी व्यापक रूप से पढ़ी और बोली जाती है, और अंग्रेज़ी, हिंदी, कन्नड़ और उर्दू भी आम हैं। कुछ बुज़ुर्ग गोवावासी आज भी पुर्तगाली जानते हैं।",
        "2011 च्या जनगणनेनुसार गोव्याची लोकसंख्या 14.6 लाख होती, आणि प्रति चौ.किमी सुमारे 394 लोक. दर 1,000 पुरुषांमागे 973 स्त्रिया होत्या व बाल लिंग गुणोत्तर 942 होते, दोन्ही 2001 पेक्षा अधिक, आणि साक्षरता 88.7% होती — भारतातील सर्वाधिकांपैकी. अनुसूचित जाती लोकसंख्येच्या केवळ 1.7% होत्या, आणि अनुसूचित जमाती 10.2% — मुख्यतः गावडा, कुणबी व वेळीप समुदाय, ज्यांना 2003 मध्ये अनुसूचित जमाती म्हणून अधिसूचित केले गेले.\n\nबहुतेक गोंयकारांची मातृभाषा कोकणी आहे, जी देवनागरीत व अनेक कॅथलिकांमध्ये रोमन लिपीत लिहिली जाते; मराठी मोठ्या प्रमाणावर वाचली व बोलली जाते, आणि इंग्रजी, हिंदी, कन्नड व उर्दूही सामान्य आहेत. काही वयस्क गोंयकारांना आजही पोर्तुगीज येते."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), ga["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), ga["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(961, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), ga["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(938, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), ga["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), ga["density2011"], "number"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(10.2, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 1.49 lakh people. Scheduled Castes were 1.7% (0.25 lakh)."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("kok", "Konkani", "कोंकणी", "कोकणी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("mr", "Marathi", "मराठी", "मराठी", m=("Used for official purposes", "आधिकारिक उपयोग", "अधिकृत वापर")),
        it3("en", "English", "अंग्रेज़ी", "इंग्रजी"), it3("hi", "Hindi", "हिंदी", "हिंदी"),
        it3("kn", "Kannada", "कन्नड़", "कन्नड"), it3("pt", "Portuguese", "पुर्तगाली", "पोर्तुगीज"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("ST notification of 2003 — official copy", "2003 की अनुसूचित जनजाति अधिसूचना — आधिकारिक प्रति", "2003 ची अनुसूचित जमाती अधिसूचना — अधिकृत प्रत"), "tribal-affairs", "Scheduled Tribes Order (Amendment) Act, 2002."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Goa — Gomantak in the Puranas — was ruled by the Bhojas, the Konkan Mauryas, the Chalukyas and the Shilaharas, and from the 10th century by the Kadambas, who made Gopakapattana (near Panaji) and later Chandor their capitals and built the Tambdi Surla temple. It then passed to the Vijayanagara empire, the Bahmani sultans and Adil Shah of Bijapur, who had a palace at Old Goa. In 1510 the Portuguese under Afonso de Albuquerque captured Goa, which became the capital of their Estado da Índia; Old Goa grew into a great city of churches, the Inquisition was introduced in 1560, and the 'New Conquests' of Ponda, Sanguem, Pernem and other talukas were added in the 18th century.\n\nGoans resisted colonial rule through revolts and, in the 20th century, a freedom movement led by figures such as Tristão de Bragança Cunha, and the satyagraha launched by Ram Manohar Lohia at Margao on 18 June 1946 (now Goa Revolution Day). Portugal refused to leave after India's independence, and on 19 December 1961 Indian forces ended Portuguese rule in Operation Vijay. Goa, Daman and Diu became a Union Territory; in the opinion poll of 1967 voters chose to keep Goa separate rather than merge with Maharashtra, and Goa became a State on 30 May 1987, the year Konkani was made its official language.",
        "गोवा — पुराणों का गोमंतक — पर भोजों, कोंकण मौर्यों, चालुक्यों और शिलाहारों ने शासन किया, और 10वीं सदी से कदंबों ने, जिन्होंने गोपकपट्टण (पणजी के पास) और बाद में चांदोर को राजधानी बनाया और ताम्बडी सुर्ला मंदिर बनवाया। फिर यह विजयनगर साम्राज्य, बहमनी सुल्तानों और बीजापुर के आदिलशाह के पास गया, जिनका पुराने गोवा में महल था। 1510 में अफ़ोंसो दे अल्बुकर्क के नेतृत्व में पुर्तगालियों ने गोवा पर क़ब्ज़ा किया, जो उनके एस्तादो दा इंडिया की राजधानी बना; पुराना गोवा चर्चों का बड़ा नगर बना, 1560 में इन्क्विज़िशन लागू हुआ, और 18वीं सदी में फोंडा, सांगे, पेडणे और अन्य तालुकों की 'नई विजयें' जोड़ी गईं।\n\nगोवावासियों ने विद्रोहों से और 20वीं सदी में त्रिस्ताओ ब्रागांसा कुन्हा जैसे नेताओं के नेतृत्व वाले स्वतंत्रता आंदोलन से औपनिवेशिक शासन का विरोध किया, और 18 जून 1946 को राम मनोहर लोहिया ने मडगाँव में सत्याग्रह शुरू किया (जो अब गोवा क्रांति दिवस है)। भारत की स्वतंत्रता के बाद पुर्तगाल ने जाने से इनकार किया, और 19 दिसंबर 1961 को ऑपरेशन विजय में भारतीय सेनाओं ने पुर्तगाली शासन समाप्त किया। गोवा, दमन और दीव केंद्र शासित प्रदेश बने; 1967 के जनमत सर्वेक्षण में मतदाताओं ने महाराष्ट्र में विलय के बजाय गोवा को अलग रखना चुना, और 30 मई 1987 को गोवा राज्य बना — उसी वर्ष कोंकणी इसकी राजभाषा बनी।",
        "गोवा — पुराणांतील गोमंतक — वर भोज, कोकण मौर्य, चालुक्य व शिलाहारांनी राज्य केले, आणि दहाव्या शतकापासून कदंबांनी, ज्यांनी गोपकपट्टण (पणजीजवळ) व नंतर चांदोर ही राजधानी केली आणि तांबडी सुर्ला मंदिर बांधले. नंतर ते विजयनगर साम्राज्य, बहामनी सुलतान व विजापूरच्या आदिलशहाकडे गेले, ज्यांचा जुन्या गोव्यात महाल होता. 1510 मध्ये आफोंसो द आल्बुकेर्कच्या नेतृत्वाखाली पोर्तुगीजांनी गोवा जिंकले, जे त्यांच्या एस्तादो द इंडियाची राजधानी झाले; जुने गोवा चर्चचे मोठे शहर बनले, 1560 मध्ये इन्क्विझिशन लागू झाले, आणि अठराव्या शतकात फोंडा, सांगे, पेडणे व इतर तालुक्यांचे 'नवे काबीज' जोडले गेले.\n\nगोंयकारांनी उठावांद्वारे आणि विसाव्या शतकात त्रिस्तांव ब्रागांस कुन्हा यांसारख्या नेत्यांच्या स्वातंत्र्य चळवळीद्वारे वसाहतवादी राजवटीला विरोध केला, आणि 18 जून 1946 रोजी राम मनोहर लोहियांनी मडगाव येथे सत्याग्रह सुरू केला (आता गोवा क्रांतिदिन). भारताच्या स्वातंत्र्यानंतर पोर्तुगालने जाण्यास नकार दिला, आणि 19 डिसेंबर 1961 रोजी ऑपरेशन विजयमध्ये भारतीय सैन्याने पोर्तुगीज राजवट संपवली. गोवा, दमण व दीव केंद्रशासित प्रदेश झाले; 1967 च्या जनमत कौलात मतदारांनी महाराष्ट्रात विलीन होण्याऐवजी गोवा वेगळा ठेवणे निवडले, आणि 30 मे 1987 रोजी गोवा राज्य झाले — त्याच वर्षी कोकणी त्याची राजभाषा झाली."),
        conf="Editorial"),
    timeline([
        ev("kadamba", 1000, L("10th–14th century", "10वीं–14वीं सदी", "दहावे–चौदावे शतक"), L("Kadamba kings rule Goa", "कदंब राजाओं का गोवा पर शासन", "कदंब राजांचे गोव्यावर राज्य")),
        ev("portuguese", 1510, L("1510", "1510", "1510"), L("Portuguese capture Goa", "पुर्तगालियों ने गोवा पर क़ब्ज़ा किया", "पोर्तुगीजांनी गोवा जिंकले")),
        ev("lohia", 1946, L("18 June 1946", "18 जून 1946", "18 जून 1946"), L("Satyagraha at Margao (Goa Revolution Day)", "मडगाँव में सत्याग्रह (गोवा क्रांति दिवस)", "मडगाव येथे सत्याग्रह (गोवा क्रांतिदिन)")),
        ev("liberation", 1961, L("19 December 1961", "19 दिसंबर 1961", "19 डिसेंबर 1961"), L("End of Portuguese rule (Goa Liberation Day)", "पुर्तगाली शासन का अंत (गोवा मुक्ति दिवस)", "पोर्तुगीज राजवटीचा अंत (गोवा मुक्तिदिन)")),
        ev("poll", 1967, L("16 January 1967", "16 जनवरी 1967", "16 जानेवारी 1967"), L("Opinion poll keeps Goa separate from Maharashtra", "जनमत सर्वेक्षण से गोवा महाराष्ट्र से अलग रहा", "जनमत कौलाने गोवा महाराष्ट्रापासून वेगळा राहिला")),
        ev("state", 1987, L("30 May 1987", "30 मई 1987", "30 मे 1987"), L("Goa becomes India's 25th State", "गोवा भारत का 25वाँ राज्य बना", "गोवा भारताचे 25 वे राज्य")),
        ev("mopa", 2022, L("11 December 2022", "11 दिसंबर 2022", "11 डिसेंबर 2022"), L("Manohar International Airport at Mopa opens", "मोपा में मनोहर अंतरराष्ट्रीय हवाई अड्डा खुला", "मोपा येथील मनोहर आंतरराष्ट्रीय विमानतळ सुरू")),
        ev("kushavati", 2025, L("December 2025", "दिसंबर 2025", "डिसेंबर 2025"), L("Kushavati notified as the third district", "कुशावती तीसरे ज़िले के रूप में अधिसूचित", "कुशावती तिसरा जिल्हा म्हणून अधिसूचित")),
    ]),
    lst("heritage", [
        it3("bom", "Basilica of Bom Jesus, Old Goa", "बेसिलिका ऑफ़ बॉम जीसस, पुराना गोवा", "बॅसिलिका ऑफ बॉम जीझस, जुने गोवा", m=("UNESCO World Heritage (Churches and Convents of Goa)", "यूनेस्को विश्व धरोहर (गोवा के चर्च और कॉन्वेंट)", "युनेस्को जागतिक वारसा (गोव्याची चर्च व कॉन्व्हेंट)")),
        it3("se", "Sé Cathedral, Old Goa", "से कैथेड्रल, पुराना गोवा", "से कॅथेड्रल, जुने गोवा", m=("16th–17th century", "16वीं–17वीं सदी", "सोळावे–सतरावे शतक")),
        it3("tambdi", "Tambdi Surla Mahadev temple", "ताम्बडी सुर्ला महादेव मंदिर", "तांबडी सुर्ला महादेव मंदिर", m=("Kadamba era, basalt", "कदंब काल, बेसाल्ट", "कदंब काळ, बेसॉल्ट")),
        it3("aguada", "Fort Aguada", "अगुआदा क़िला", "आग्वाद किल्ला", m=("Portuguese fort and lighthouse", "पुर्तगाली क़िला और प्रकाशस्तंभ", "पोर्तुगीज किल्ला व दीपस्तंभ")),
        it3("mangeshi", "Shri Mangueshi temple, Ponda", "श्री मंगेशी मंदिर, फोंडा", "श्री मंगेश मंदिर, फोंडा", m=("Goan temple architecture", "गोवा मंदिर स्थापत्य", "गोमंतकीय मंदिर स्थापत्य")),
        it3("fontainhas", "Fontainhas, Panaji", "फ़ॉन्टेनहास, पणजी", "फोंतेनास, पणजी", m=("Latin quarter", "लैटिन क्वार्टर", "लॅटिन क्वार्टर")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
    gaps("g", [
        (L("Kushavati district notification — official copy", "कुशावती ज़िला अधिसूचना — आधिकारिक प्रति", "कुशावती जिल्हा अधिसूचना — अधिकृत प्रत"), "india-gov", f"Reported by The Goan ({KUSH}); link the Revenue Department notification."),
    ]),
])
print("ga mod1 ok")
