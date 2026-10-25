"""Mizoram modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-MZ"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
mz = read("regions/IN-MZ.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Mizoram, 'the land of the hill people', is a State in the far south of north-eastern India, wedged between Myanmar to the east and south and Bangladesh to the west, with Tripura, Assam and Manipur to the north. Parallel ridges running north to south, cut by deep river valleys and covered with bamboo and forest, fill almost the whole State. Aizawl, built along a ridge, is the capital.\n\nThe Lushai Hills district of Assam became the Union Territory of Mizoram in 1972 and, after the Mizo Accord of 1986 ended two decades of insurgency, India's 23rd State on 20 February 1987. Most Mizos are Christian, and the State is known for its high literacy, close-knit community life, the bamboo dance Cheraw and its love of football.",
        "मिज़ोरम, 'पहाड़ी लोगों की भूमि', उत्तर-पूर्वी भारत के सुदूर दक्षिण में एक राज्य है, जो पूर्व और दक्षिण में म्यांमार और पश्चिम में बांग्लादेश के बीच स्थित है, और उत्तर में त्रिपुरा, असम और मणिपुर हैं। उत्तर से दक्षिण की ओर चलने वाली समानांतर पर्वतमालाएँ, गहरी नदी घाटियों से कटी और बाँस व वनों से ढकी, लगभग पूरे राज्य में फैली हैं। एक पहाड़ी पर बसा आइज़ोल राजधानी है।\n\nअसम का लुशाई हिल्स ज़िला 1972 में मिज़ोरम केंद्र शासित प्रदेश बना और 1986 के मिज़ो समझौते से दो दशक के उग्रवाद के अंत के बाद 20 फ़रवरी 1987 को भारत का 23वाँ राज्य बना। अधिकांश मिज़ो ईसाई हैं, और राज्य अपनी ऊँची साक्षरता, घनिष्ठ सामुदायिक जीवन, बाँस नृत्य चेराव और फ़ुटबॉल प्रेम के लिए जाना जाता है।",
        "मिझोराम, 'डोंगरी लोकांची भूमी', हे ईशान्य भारताच्या अतिदक्षिणेकडील राज्य आहे, ज्याच्या पूर्व व दक्षिणेला म्यानमार आणि पश्चिमेला बांगलादेश आहे, आणि उत्तरेला त्रिपुरा, आसाम व मणिपूर आहेत. उत्तर-दक्षिण धावणाऱ्या समांतर डोंगररांगा, खोल नदीखोऱ्यांनी कापलेल्या व बांबू आणि जंगलाने व्यापलेल्या, जवळपास संपूर्ण राज्य व्यापतात. एका डोंगरकड्यावर वसलेले आयझॉल ही राजधानी आहे.\n\nआसाममधील लुशाई हिल्स जिल्हा 1972 मध्ये मिझोराम केंद्रशासित प्रदेश झाला आणि 1986 च्या मिझो कराराने दोन दशकांची बंडखोरी संपल्यानंतर 20 फेब्रुवारी 1987 रोजी भारताचे 23 वे राज्य झाला. बहुतेक मिझो ख्रिस्ती आहेत, आणि राज्य उच्च साक्षरता, घट्ट सामुदायिक जीवन, बांबू नृत्य चेराव व फुटबॉलप्रेमासाठी ओळखले जाते."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Literacy in Mizoram was 91.3% at the 2011 Census, and about 85% of the State is forest (ISFR 2023). Community life is organised around the village and the church, and voluntary bodies such as the Young Mizo Association (YMA) help with funerals, clean-ups and disaster relief; the custom of tlawmngaihna, putting others first, is a core value. Aizawl is known for orderly traffic and quiet Sundays. The State has its own GI-registered handloom cloths, such as the puanchei and pawndum, and its people are passionate about football and music.",
        "2011 की जनगणना में मिज़ोरम की साक्षरता 91.3% थी, और राज्य का लगभग 85% भाग वन है (आईएसएफ़आर 2023)। सामुदायिक जीवन गाँव और चर्च के इर्द-गिर्द चलता है, और यंग मिज़ो एसोसिएशन (वाईएमए) जैसे स्वैच्छिक संगठन अंत्येष्टि, सफ़ाई और आपदा राहत में मदद करते हैं; त्लॉमङाइहना, दूसरों को पहले रखने की परंपरा, एक मूल मूल्य है। आइज़ोल अपने अनुशासित यातायात और शांत रविवारों के लिए जाना जाता है। राज्य के अपने जीआई-पंजीकृत हथकरघा वस्त्र हैं, जैसे पुआनचेई और पॉनदुम, और इसके लोग फ़ुटबॉल और संगीत के प्रति उत्साही हैं।",
        "2011 च्या जनगणनेत मिझोरामची साक्षरता 91.3% होती, आणि राज्याचा सुमारे 85% भाग वनाच्छादित आहे (आयएसएफआर 2023). सामुदायिक जीवन गाव व चर्चभोवती चालते, आणि यंग मिझो असोसिएशनसारख्या (वायएमए) स्वयंसेवी संघटना अंत्यविधी, स्वच्छता व आपत्ती मदतीत साहाय्य करतात; त्लॉमङाइहना, इतरांना प्रथम स्थान देण्याची परंपरा, हे मूलभूत मूल्य आहे. आयझॉल शिस्तबद्ध वाहतूक व शांत रविवारांसाठी ओळखले जाते. राज्याची स्वतःची जीआय-नोंदणीकृत हातमाग वस्त्रे आहेत, उदा. पुआनचेई व पॉनदुम, आणि तेथील लोक फुटबॉल व संगीताबद्दल उत्साही आहेत."),
        title=L("What makes Mizoram unique?", "मिज़ोरम को ख़ास क्या बनाता है?", "मिझोरामचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Statehood", "राज्य का दर्जा", "राज्याचा दर्जा"), L("20 February 1987 (Union Territory from 21 January 1972)", "20 फ़रवरी 1987 (21 जनवरी 1972 से केंद्र शासित प्रदेश)", "20 फेब्रुवारी 1987 (21 जानेवारी 1972 पासून केंद्रशासित प्रदेश)")],
           [L("Districts", "ज़िले", "जिल्हे"), L("11 (including Hnahthial, Khawzawl and Saitual, created in 2019)", "11 (2019 में बने ह्नाहथियाल, खॉज़ॉल और सैतुआल सहित)", "11 (2019 मध्ये निर्माण झालेल्या ह्नाहथियाल, खॉझॉल व सैतुआलसह)")],
           [L("Capital", "राजधानी", "राजधानी"), L("Aizawl", "आइज़ोल", "आयझॉल")],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Mizo and English", "मिज़ो और अंग्रेज़ी", "मिझो व इंग्रजी")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Gauhati High Court (Aizawl bench)", "गुवाहाटी उच्च न्यायालय (आइज़ोल पीठ)", "गुवाहाटी उच्च न्यायालय (आयझॉल खंडपीठ)")],
           [L("Autonomous District Councils", "स्वायत्त ज़िला परिषदें", "स्वायत्त जिल्हा परिषदा"), L("Chakma, Lai and Mara (Sixth Schedule)", "चकमा, लाई और मारा (छठी अनुसूची)", "चकमा, लाई व मारा (सहावी अनुसूची)")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "MZ"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be checked against the Government of Mizoram's district list.", "संपादकीय; मिज़ोरम सरकार की ज़िला सूची से जाँचा जाएगा।", "संपादकीय; मिझोराम शासनाच्या जिल्हा यादीशी पडताळले जाईल.")),
    gaps("g", [(L("District creation notification, 2019", "ज़िला गठन अधिसूचना, 2019", "जिल्हा निर्मिती अधिसूचना, 2019"), "india-gov", "Government of Mizoram Gazette.")]),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Mizoram's ridges, part of the Lushai (Mizo) Hills, rise to about 2,000 m in the east, where Phawngpui (Blue Mountain) is the highest peak, and fall to under 100 m in the river valleys of the west. The Tlawng (Dhaleswari), Tuirial and Tuivawl flow north into the Barak in Assam, while the Chhimtuipui (Kaladan) and the Tiau, which forms much of the Myanmar border, drain south and east. Bamboo covers large areas, and soft, young rocks make the hills prone to landslides.",
        "मिज़ोरम की पर्वतमालाएँ, लुशाई (मिज़ो) पहाड़ियों का भाग, पूर्व में लगभग 2,000 मीटर तक उठती हैं, जहाँ फ़ॉङपुई (ब्लू माउंटेन) सबसे ऊँची चोटी है, और पश्चिम की नदी घाटियों में 100 मीटर से नीचे उतरती हैं। त्लॉङ (धलेश्वरी), तुइरियाल और तुइवॉल उत्तर में असम की बराक में बहती हैं, जबकि छिमतुइपुई (कलादान) और तियाउ, जो म्यांमार सीमा का बड़ा भाग बनाती है, दक्षिण और पूर्व की ओर बहती हैं। बड़े क्षेत्रों में बाँस है, और नरम, नई चट्टानें पहाड़ियों को भूस्खलन-प्रवण बनाती हैं।",
        "मिझोरामच्या डोंगररांगा, लुशाई (मिझो) टेकड्यांचा भाग, पूर्वेला सुमारे 2,000 मीटरपर्यंत उंचावतात, जिथे फॉङपुई (ब्लू माउंटन) हे सर्वोच्च शिखर आहे, आणि पश्चिमेकडील नदीखोऱ्यांत 100 मीटरखाली उतरतात. त्लॉङ (धलेश्वरी), तुइरियाल व तुइवॉल उत्तरेला आसाममधील बराकला मिळतात, तर छिमतुइपुई (कलादान) व म्यानमार सीमेचा बराचसा भाग असलेली तियाउ दक्षिण व पूर्वेकडे वाहतात. मोठ्या भागावर बांबू आहे, आणि मऊ, नवे खडक टेकड्यांना भूस्खलनप्रवण बनवतात."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), mz["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("mm", "Myanmar (east and south)", "म्यांमार (पूर्व और दक्षिण)", "म्यानमार (पूर्व व दक्षिण)"), it3("bd", "Bangladesh (west)", "बांग्लादेश (पश्चिम)", "बांगलादेश (पश्चिम)"),
        it3("tr", "Tripura (north-west)", "त्रिपुरा (उत्तर-पश्चिम)", "त्रिपुरा (वायव्य)"), it3("as", "Assam (north)", "असम (उत्तर)", "आसाम (उत्तर)"), it3("mn", "Manipur (north-east)", "मणिपुर (उत्तर-पूर्व)", "मणिपूर (ईशान्य)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("tlawng", "Tlawng (Dhaleswari)", "त्लॉङ (धलेश्वरी)", "त्लॉङ (धलेश्वरी)", d=("Main river of the west; flows north to the Barak.", "पश्चिम की मुख्य नदी; उत्तर में बराक तक बहती है।", "पश्चिमेकडील मुख्य नदी; उत्तरेला बराकपर्यंत वाहते.")),
        it3("kaladan", "Chhimtuipui (Kaladan)", "छिमतुइपुई (कलादान)", "छिमतुइपुई (कलादान)", d=("Flows south into Myanmar; route of the Kaladan transit project.", "दक्षिण में म्यांमार जाती है; कलादान परिवहन परियोजना का मार्ग।", "दक्षिणेला म्यानमारमध्ये जाते; कलादान वाहतूक प्रकल्पाचा मार्ग.")),
        it3("tiau", "Tiau", "तियाउ", "तियाउ", d=("Forms part of the border with Myanmar.", "म्यांमार के साथ सीमा का भाग बनाती है।", "म्यानमारशी सीमेचा भाग बनवते.")),
        it3("tuirial", "Tuirial", "तुइरियाल", "तुइरियाल", d=("Site of the Tuirial hydro project.", "तुइरियाल जलविद्युत परियोजना का स्थल।", "तुइरियाल जलविद्युत प्रकल्पाचे स्थळ.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Phawngpui — official elevation", "फ़ॉङपुई — आधिकारिक ऊँचाई", "फॉङपुई — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Length of the Myanmar and Bangladesh borders", "म्यांमार और बांग्लादेश सीमा की लंबाई", "म्यानमार व बांगलादेश सीमांची लांबी"), "india-gov", "Ministry of Home Affairs (Department of Border Management)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Mizoram has a mild, wet climate. Aizawl, at about 1,100 m, is pleasant for most of the year, while the valleys are hot and humid in summer. The south-west monsoon brings heavy rain from May to September, often with landslides that cut roads; winter, from November to February, is cool and dry.",
        "मिज़ोरम की जलवायु सौम्य और नम है। लगभग 1,100 मीटर पर आइज़ोल वर्ष के अधिकांश समय सुहावना रहता है, जबकि घाटियाँ गर्मियों में गर्म और आर्द्र होती हैं। दक्षिण-पश्चिम मानसून मई से सितंबर तक भारी वर्षा लाता है, अक्सर सड़कें काटने वाले भूस्खलनों के साथ; नवंबर से फ़रवरी तक सर्दी ठंडी और सूखी होती है।",
        "मिझोरामचे हवामान सौम्य व ओलसर आहे. सुमारे 1,100 मीटरवरील आयझॉल वर्षाचा बहुतेक काळ सुखद असते, तर खोरी उन्हाळ्यात उष्ण व दमट असतात. नैर्ऋत्य मान्सून मे ते सप्टेंबर मुसळधार पाऊस आणतो, अनेकदा रस्ते तोडणाऱ्या भूस्खलनांसह; नोव्हेंबर ते फेब्रुवारी हिवाळा थंड व कोरडा असतो."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Aizawl", "आइज़ोल", "आयझॉल"), "lat": 23.7271, "lon": 92.7176},
        {"name": L("Lunglei", "लुंगलेई", "लुंगलेई"), "lat": 22.8833, "lon": 92.7333},
        {"name": L("Champhai", "चम्फाई", "चम्फाई"), "lat": 23.4560, "lon": 93.3280},
    ]},
    lst("best", [
        it3("winter", "October to March", "अक्टूबर से मार्च", "ऑक्टोबर ते मार्च", d=("Clear, cool weather; Chapchar Kut in March.", "साफ़, ठंडा मौसम; मार्च में चापचार कुट।", "निरभ्र, थंड हवामान; मार्चमध्ये चापचार कुट.")),
        it3("monsoon", "May to September", "मई से सितंबर", "मे ते सप्टेंबर", d=("Green hills but heavy rain and road closures.", "हरी पहाड़ियाँ, पर भारी वर्षा और सड़कें बंद।", "हिरव्या टेकड्या, पण मुसळधार पाऊस व रस्ते बंद.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [(L("Normal annual rainfall", "सामान्य वार्षिक वर्षा", "सरासरी वार्षिक पाऊस"), "imd", "IMD climatological normals for Aizawl.")]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Aizawl's houses cling to steep slopes, connected by stairways and narrow roads where cars queue in neat lines and horns are rarely heard. Shops close early, and on Sundays the city stops for church. Village councils and the YMA organise community work, and many shops in the countryside run on trust, with goods left out and payment dropped in a box. Music — gospel, rock and Mizo pop — is everywhere.",
        "आइज़ोल के घर खड़ी ढलानों से चिपके हैं, जिन्हें सीढ़ियाँ और संकरी सड़कें जोड़ती हैं, जहाँ कारें साफ़ कतारों में चलती हैं और हॉर्न शायद ही सुनाई देता है। दुकानें जल्दी बंद होती हैं, और रविवार को शहर चर्च के लिए रुक जाता है। ग्राम परिषदें और वाईएमए सामुदायिक कार्य आयोजित करते हैं, और गाँवों में कई दुकानें भरोसे पर चलती हैं, जहाँ सामान बाहर रखा होता है और पैसा एक डिब्बे में डाला जाता है। संगीत — गॉस्पेल, रॉक और मिज़ो पॉप — हर जगह है।",
        "आयझॉलची घरे तीव्र उतारांना बिलगलेली आहेत, जी पायऱ्या व अरुंद रस्त्यांनी जोडलेली आहेत, जिथे गाड्या व्यवस्थित रांगेत चालतात व हॉर्न क्वचितच ऐकू येतो. दुकाने लवकर बंद होतात, आणि रविवारी शहर चर्चसाठी थांबते. ग्रामपरिषदा व वायएमए सामुदायिक कामे आयोजित करतात, आणि ग्रामीण भागातील अनेक दुकाने विश्वासावर चालतात, जिथे माल बाहेर ठेवलेला असतो व पैसे पेटीत टाकले जातात. संगीत — गॉस्पेल, रॉक व मिझो पॉप — सर्वत्र आहे."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Mizoram had 10.97 lakh people at the 2011 Census, about 52 per km². The sex ratio rose from 935 in 2001 to 976 women per 1,000 men, and the child sex ratio from 964 to 970. Literacy was 91.3%. Scheduled Tribes made up 94.4% of the population. The Mizo — a family of related clans and peoples including the Lusei, Hmar, Ralte, Paite and others — form the large majority, and the Chakma, Lai (Pawi), Mara and Bru are other important communities. Mizo, written in the Roman script introduced by Welsh missionaries in the 1890s, is the common language.",
        "2011 की जनगणना में मिज़ोरम की जनसंख्या 10.97 लाख थी, प्रति वर्ग किमी लगभग 52। लिंगानुपात 2001 के 935 से बढ़कर प्रति 1,000 पुरुषों पर 976 महिलाएँ और शिशु लिंगानुपात 964 से बढ़कर 970 हो गया। साक्षरता 91.3% थी। अनुसूचित जनजातियाँ जनसंख्या का 94.4% थीं। मिज़ो — लुसेई, ह्मार, राल्टे, पाइते और अन्य सहित संबंधित कुलों और लोगों का परिवार — बड़ा बहुमत हैं, और चकमा, लाई (पावी), मारा और ब्रू अन्य महत्त्वपूर्ण समुदाय हैं। 1890 के दशक में वेल्श मिशनरियों द्वारा लाई गई रोमन लिपि में लिखी जाने वाली मिज़ो सामान्य भाषा है।",
        "2011 च्या जनगणनेनुसार मिझोरामची लोकसंख्या 10.97 लाख होती, प्रति चौ.किमी सुमारे 52. लिंग गुणोत्तर 2001 मधील 935 वरून वाढून दर 1,000 पुरुषांमागे 976 स्त्रिया आणि बाल लिंग गुणोत्तर 964 वरून 970 झाले. साक्षरता 91.3% होती. अनुसूचित जमाती लोकसंख्येच्या 94.4% होत्या. मिझो — लुसेई, ह्मार, राल्टे, पाइते व इतरांसह संबंधित कुळे व लोकांचे कुटुंब — मोठे बहुमत आहेत, आणि चकमा, लाई (पावी), मारा व ब्रू हे इतर महत्त्वाचे समुदाय आहेत. 1890 च्या दशकात वेल्श मिशनऱ्यांनी आणलेल्या रोमन लिपीत लिहिली जाणारी मिझो ही सामान्य भाषा आहे."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), mz["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), mz["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(935, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), mz["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(964, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), mz["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), mz["density2011"], "number"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(94.4, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 10.36 lakh people. Scheduled Castes were 0.1%."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("mizo", "Mizo", "मिज़ो", "मिझो", m=("Official", "राजभाषा", "राजभाषा")), it3("en", "English", "अंग्रेज़ी", "इंग्रजी", m=("Official", "राजभाषा", "राजभाषा")),
        it3("chakma", "Chakma", "चकमा", "चकमा"), it3("lai", "Lai (Pawi)", "लाई (पावी)", "लाई (पावी)"), it3("mara", "Mara", "मारा", "मारा"), it3("hmar", "Hmar", "ह्मार", "ह्मार"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "The Mizo peoples migrated into the hills from the east, from the Chin Hills of present-day Myanmar, over several centuries, and lived in villages ruled by hereditary chiefs. British expeditions in the 1870s and 1890s brought the Lushai Hills under colonial rule, and Welsh and other missionaries who arrived in 1894 created the Mizo script and spread Christianity and schooling. After independence the hills became a district of Assam. The mautam famine of 1959, which followed the mass flowering of bamboo and a plague of rats, and the Assam government's response led to the rise of the Mizo National Front (MNF) under Laldenga, which began an armed uprising in 1966.\n\nThe area became a Union Territory in 1972. The Mizo Peace Accord, signed on 30 June 1986 by the Government of India and the MNF, ended the insurgency, and Mizoram became a State on 20 February 1987, with Laldenga as its first Chief Minister. Since 2021 Mizoram has sheltered many people who fled conflict in Myanmar, and earlier also from Bangladesh and Manipur.",
        "मिज़ो लोग कई सदियों में पूर्व से, आज के म्यांमार की चिन पहाड़ियों से, इन पहाड़ियों में आए और वंशानुगत मुखियाओं द्वारा शासित गाँवों में रहे। 1870 और 1890 के दशक के ब्रिटिश अभियानों ने लुशाई पहाड़ियों को औपनिवेशिक शासन में ला दिया, और 1894 में आए वेल्श और अन्य मिशनरियों ने मिज़ो लिपि बनाई और ईसाई धर्म व स्कूली शिक्षा फैलाई। स्वतंत्रता के बाद पहाड़ियाँ असम का एक ज़िला बनीं। 1959 का मौतम अकाल, जो बाँस के बड़े पैमाने पर फूलने और चूहों के प्रकोप के बाद आया, और असम सरकार की प्रतिक्रिया से लालडेंगा के नेतृत्व में मिज़ो नेशनल फ़्रंट (एमएनएफ़) उभरा, जिसने 1966 में सशस्त्र विद्रोह शुरू किया।\n\nयह क्षेत्र 1972 में केंद्र शासित प्रदेश बना। 30 जून 1986 को भारत सरकार और एमएनएफ़ द्वारा हस्ताक्षरित मिज़ो शांति समझौते ने उग्रवाद समाप्त किया, और 20 फ़रवरी 1987 को मिज़ोरम राज्य बना, लालडेंगा इसके पहले मुख्यमंत्री बने। 2021 से मिज़ोरम ने म्यांमार में संघर्ष से भागे बहुत से लोगों को, और पहले बांग्लादेश और मणिपुर से आए लोगों को भी शरण दी है।",
        "मिझो लोक अनेक शतकांत पूर्वेकडून, आजच्या म्यानमारमधील चिन टेकड्यांतून, या डोंगरांत आले आणि वंशपरंपरागत प्रमुखांच्या गावांत राहिले. 1870 व 1890 च्या दशकांतील ब्रिटिश मोहिमांनी लुशाई टेकड्या वसाहती राजवटीखाली आणल्या, आणि 1894 मध्ये आलेल्या वेल्श व इतर मिशनऱ्यांनी मिझो लिपी तयार केली व ख्रिस्ती धर्म आणि शालेय शिक्षण पसरवले. स्वातंत्र्यानंतर टेकड्या आसामचा एक जिल्हा झाल्या. 1959 चा मौतम दुष्काळ, जो बांबूच्या मोठ्या प्रमाणावरील फुलोऱ्यानंतर व उंदरांच्या उपद्रवानंतर आला, आणि आसाम सरकारच्या प्रतिसादामुळे लालडेंगा यांच्या नेतृत्वाखाली मिझो नॅशनल फ्रंट (एमएनएफ) उभी राहिली, जिने 1966 मध्ये सशस्त्र उठाव सुरू केला.\n\nहा भाग 1972 मध्ये केंद्रशासित प्रदेश झाला. 30 जून 1986 रोजी भारत सरकार व एमएनएफने स्वाक्षरी केलेल्या मिझो शांतता कराराने बंडखोरी संपली, आणि 20 फेब्रुवारी 1987 रोजी मिझोराम राज्य झाले, लालडेंगा त्याचे पहिले मुख्यमंत्री झाले. 2021 पासून मिझोरामने म्यानमारमधील संघर्षातून पळालेल्या अनेकांना, आणि त्यापूर्वी बांगलादेश व मणिपूरमधून आलेल्यांनाही आश्रय दिला आहे."),
        conf="Editorial"),
    timeline([
        ev("missionaries", 1894, L("1894", "1894", "1894"), L("First missionaries arrive; Mizo script created", "पहले मिशनरी आए; मिज़ो लिपि बनी", "पहिले मिशनरी आले; मिझो लिपी तयार")),
        ev("mautam", 1959, L("1959", "1959", "1959"), L("Mautam famine after bamboo flowering", "बाँस फूलने के बाद मौतम अकाल", "बांबू फुलल्यानंतर मौतम दुष्काळ")),
        ev("uprising", 1966, L("1966", "1966", "1966"), L("MNF uprising begins", "एमएनएफ़ विद्रोह शुरू", "एमएनएफ उठाव सुरू")),
        ev("ut", 1972, L("21 January 1972", "21 जनवरी 1972", "21 जानेवारी 1972"), L("Union Territory of Mizoram", "मिज़ोरम केंद्र शासित प्रदेश", "मिझोराम केंद्रशासित प्रदेश")),
        ev("accord", 1986, L("30 June 1986", "30 जून 1986", "30 जून 1986"), L("Mizo Peace Accord", "मिज़ो शांति समझौता", "मिझो शांतता करार")),
        ev("state", 1987, L("20 February 1987", "20 फ़रवरी 1987", "20 फेब्रुवारी 1987"), L("Mizoram becomes a State", "मिज़ोरम राज्य बना", "मिझोराम राज्य झाले")),
        ev("rail", 2025, L("13 September 2025", "13 सितंबर 2025", "13 सप्टेंबर 2025"), L("Railway reaches Sairang near Aizawl", "आइज़ोल के पास सैरांग तक रेल", "आयझॉलजवळ सैरांगपर्यंत रेल्वे")),
    ]),
    gaps("g", [
        (L("Mizo Peace Accord — official text", "मिज़ो शांति समझौता — आधिकारिक पाठ", "मिझो शांतता करार — अधिकृत मजकूर"), "india-gov", "Ministry of Home Affairs."),
        (L("Refugees from Myanmar — official figures", "म्यांमार से आए शरणार्थी — आधिकारिक आँकड़े", "म्यानमारमधून आलेले निर्वासित — अधिकृत आकडे"), "india-gov", "Government of Mizoram / MHA statements."),
    ]),
])
print("mz mod1 ok")
