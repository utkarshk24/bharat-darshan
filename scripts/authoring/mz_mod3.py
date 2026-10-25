"""Mizoram modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-MZ"
mz = read("regions/IN-MZ.json")["metrics"]; ind = read("india.json")["metrics"]
C = research("census_b5plus.json"); F = C["forest"]["MZ"]

module(R, "nature", [
    prose("p1", L(
        "About 85% of Mizoram is forest (ISFR 2023), much of it bamboo and regrowing forest on old jhum fields. Dampa Tiger Reserve on the Bangladesh border, Murlen National Park near the Myanmar border and Phawngpui (Blue Mountain) National Park are the main protected areas, with sanctuaries such as Ngengpui, Tawi and Lengteng. Wildlife includes the hoolock gibbon, clouded leopard, serow and many hornbills and pheasants. Pala wetland in Saiha district was designated a Ramsar site on 31 August 2021.",
        "मिज़ोरम का लगभग 85% भाग वन है (आईएसएफ़आर 2023), जिसका बड़ा हिस्सा बाँस और पुराने झूम खेतों पर फिर उगता वन है। बांग्लादेश सीमा पर दम्पा बाघ अभयारण्य, म्यांमार सीमा के पास मुर्लेन राष्ट्रीय उद्यान और फ़ॉङपुई (ब्लू माउंटेन) राष्ट्रीय उद्यान मुख्य संरक्षित क्षेत्र हैं, और ङेंगपुई, तावी और लेंगतेंग जैसे अभयारण्य हैं। वन्यजीवों में हूलॉक गिबन, धूमिल तेंदुआ, सीरो और कई धनेश और तीतर शामिल हैं। साइहा ज़िले की पाला आर्द्रभूमि को 31 अगस्त 2021 को रामसर स्थल घोषित किया गया।",
        "मिझोरामचा सुमारे 85% भाग वनाच्छादित आहे (आयएसएफआर 2023), ज्यातील बराचसा बांबू व जुन्या झूम शेतांवर पुन्हा वाढणारे वन आहे. बांगलादेश सीमेवरील दम्पा व्याघ्र प्रकल्प, म्यानमार सीमेजवळील मुर्लेन राष्ट्रीय उद्यान व फॉङपुई (ब्लू माउंटन) राष्ट्रीय उद्यान ही मुख्य संरक्षित क्षेत्रे आहेत, आणि ङेंगपुई, तावी व लेंगतेंगसारखी अभयारण्ये आहेत. वन्यजीवांत हूलॉक गिबन, ढगाळ बिबट्या, सेरो व अनेक धनेश आणि तितर आहेत. साइहा जिल्ह्यातील पाला पाणथळ भागाला 31 ऑगस्ट 2021 रोजी रामसर स्थळ घोषित केले गेले."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), mz["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(1, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: Pala Wetland (31 Aug 2021, 1,850 ha)."), "number"),
    ]),
    lst("protected", [
        it3("dampa", "Dampa Tiger Reserve", "दम्पा बाघ अभयारण्य", "दम्पा व्याघ्र प्रकल्प", m=("Mamit district", "मामित ज़िला", "मामित जिल्हा")),
        it3("murlen", "Murlen National Park", "मुर्लेन राष्ट्रीय उद्यान", "मुर्लेन राष्ट्रीय उद्यान", m=("Champhai district", "चम्फाई ज़िला", "चम्फाई जिल्हा")),
        it3("phawngpui", "Phawngpui National Park", "फ़ॉङपुई राष्ट्रीय उद्यान", "फॉङपुई राष्ट्रीय उद्यान", m=("Blue Mountain", "ब्लू माउंटेन", "ब्लू माउंटन")),
        it3("pala", "Pala Wetland", "पाला आर्द्रभूमि", "पाला पाणथळ", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    gaps("g", [(L("Tiger presence in Dampa — latest estimate", "दम्पा में बाघ — नवीनतम अनुमान", "दम्पातील वाघ — नवीनतम अंदाज"), "ntca", "NTCA All India Tiger Estimation.")]),
])

module(R, "water", [
    prose("p1", L(
        "Despite heavy rain, Aizawl and other ridge-top towns face water shortages in the dry season, because water must be pumped up from rivers far below; the Greater Aizawl water supply scheme lifts water from the Tlawng. Villages depend on springs and rooftop rainwater tanks.",
        "भारी वर्षा के बावजूद आइज़ोल और पहाड़ी चोटियों पर बसे अन्य नगर सूखे मौसम में पानी की कमी झेलते हैं, क्योंकि पानी बहुत नीचे की नदियों से पंप करके ऊपर लाना पड़ता है; ग्रेटर आइज़ोल जल आपूर्ति योजना त्लॉङ से पानी उठाती है। गाँव झरनों और छत पर वर्षा जल की टंकियों पर निर्भर हैं।",
        "मुसळधार पाऊस असूनही आयझॉल व डोंगरमाथ्यावरील इतर शहरांना कोरड्या ऋतूत पाणीटंचाई जाणवते, कारण पाणी खूप खालच्या नद्यांतून उपसून वर आणावे लागते; ग्रेटर आयझॉल पाणीपुरवठा योजना त्लॉङमधून पाणी उचलते. गावे झरे व छपरावरील पावसाच्या पाण्याच्या टाक्यांवर अवलंबून आहेत."),
        conf="Editorial"),
    gaps("g", [(L("Household tap-water coverage", "घरेलू नल जल कवरेज", "घरगुती नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard.")]),
])

module(R, "safety", [
    prose("p1", L(
        "Mizoram lies in seismic zone V. Landslides during the monsoon are the most frequent hazard — in May 2024, Cyclone Remal's rains caused deadly landslides and a stone-quarry collapse around Aizawl. The bamboo flowering cycle (mautam, about every 48 years) brings rat outbreaks that threaten crops. Visitors need an Inner Line Permit and should check road conditions in the rains.",
        "मिज़ोरम भूकंपीय क्षेत्र V में है। मानसून में भूस्खलन सबसे आम ख़तरा है — मई 2024 में चक्रवात रेमल की वर्षा से आइज़ोल के आसपास घातक भूस्खलन हुए और एक पत्थर खदान ढह गई। बाँस के फूलने का चक्र (मौतम, लगभग हर 48 वर्ष) चूहों का प्रकोप लाता है जो फ़सलों के लिए ख़तरा है। पर्यटकों को इनर लाइन परमिट चाहिए और वर्षा में सड़क की स्थिति देखनी चाहिए।",
        "मिझोराम भूकंप क्षेत्र V मध्ये आहे. पावसाळ्यातील भूस्खलन हा सर्वांत वारंवार येणारा धोका आहे — मे 2024 मध्ये रेमल चक्रीवादळाच्या पावसाने आयझॉलभोवती प्राणघातक भूस्खलन झाले व एक दगडखाण कोसळली. बांबू फुलण्याचे चक्र (मौतम, सुमारे दर 48 वर्षांनी) उंदरांचा उपद्रव आणते, जो पिकांसाठी धोका आहे. पर्यटकांना इनर लाइन परवाना लागतो व पावसात रस्त्यांची स्थिती पाहावी."),
        conf="Editorial"),
    emergency_table(("Mizoram", "मिज़ोरम", "मिझोराम")),
    gaps("g", [(L("Cyclone Remal landslides (May 2024) — official toll", "चक्रवात रेमल भूस्खलन (मई 2024) — आधिकारिक मृतक संख्या", "रेमल चक्रीवादळ भूस्खलन (मे 2024) — अधिकृत मृतसंख्या"), "ndma", "Mizoram State Disaster Management Authority.")]),
])

module(R, "gi", [
    prose("p1", L(
        "Seven GIs belong to Mizoram on the GI Registry's list as on 31 December 2025: Mizo chilli (filed in 2012), Mizo ginger, and five handloom textiles — Tawlhlohpuan, Mizo Puanchei, Pawndum, Ngotekherh and Hmaram — each a traditional puan with its own pattern and use.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में सात जीआई मिज़ोरम के हैं: मिज़ो मिर्च (2012 में दायर), मिज़ो अदरक, और पाँच हथकरघा वस्त्र — तॉल्ह्लोहपुआन, मिज़ो पुआनचेई, पॉनदुम, ङोतेखेर्ह और ह्मारम — हर एक अपने नमूने और उपयोग वाला पारंपरिक पुआन।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत सात जीआय मिझोरामचे आहेत: मिझो मिरची (2012 मध्ये दाखल), मिझो आले, आणि पाच हातमाग वस्त्रे — तॉल्ह्लोहपुआन, मिझो पुआनचेई, पॉनदुम, ङोतेखेर्ह व ह्मारम — प्रत्येक स्वतःच्या नक्षी व उपयोगाचा पारंपरिक पुआन."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
])

module(R, "tourism", [
    prose("p1", L(
        "Aizawl's viewpoints, Bara Bazar and the Mizoram State Museum are a good start. Reiek peak and its model Mizo village are a short drive away. In the east, Champhai looks over rice fields to the hills of Myanmar, and Murlen and Rih Dil lake (across the border) draw visitors; in the south, Lunglei, Phawngpui and the Palak and Pala lakes are quieter. Tam Dil and the Vantawng falls near Thenzawl are popular day trips.",
        "आइज़ोल के दर्शनीय बिंदु, बड़ा बाज़ार और मिज़ोरम राज्य संग्रहालय अच्छी शुरुआत हैं। रेइक चोटी और उसका आदर्श मिज़ो गाँव थोड़ी दूरी पर है। पूर्व में चम्फाई से धान के खेतों के पार म्यांमार की पहाड़ियाँ दिखती हैं, और मुर्लेन तथा (सीमा पार) रिह दिल झील पर्यटकों को खींचते हैं; दक्षिण में लुंगलेई, फ़ॉङपुई और पालक व पाला झीलें शांत हैं। तम दिल और थेनज़ॉल के पास वांतॉङ जलप्रपात लोकप्रिय एक दिन की यात्राएँ हैं।",
        "आयझॉलचे प्रेक्षणीय बिंदू, बडा बाजार व मिझोराम राज्य संग्रहालय ही चांगली सुरुवात आहे. रेइक शिखर व तेथील आदर्श मिझो गाव थोड्या अंतरावर आहे. पूर्वेला चम्फाईहून भातशेतांपलीकडे म्यानमारच्या टेकड्या दिसतात, आणि मुर्लेन व (सीमेपलीकडील) रिह दिल सरोवर पर्यटकांना आकर्षित करतात; दक्षिणेला लुंगलेई, फॉङपुई व पालक आणि पाला सरोवरे शांत आहेत. तम दिल व थेनझॉलजवळील वांतॉङ धबधबा लोकप्रिय एकदिवसीय सहली आहेत."),
        conf="Editorial"),
    lst("places", [
        it3("aizawl", "Aizawl", "आइज़ोल", "आयझॉल", m=("Capital", "राजधानी", "राजधानी")), it3("reiek", "Reiek", "रेइक", "रेइक", m=("Peak and heritage village", "चोटी और धरोहर गाँव", "शिखर व वारसा गाव")),
        it3("champhai", "Champhai", "चम्फाई", "चम्फाई", m=("Rice bowl on the border", "सीमा पर धान का कटोरा", "सीमेवरील भाताचे कोठार")),
        it3("vantawng", "Vantawng falls", "वांतॉङ जलप्रपात", "वांतॉङ धबधबा", m=("Near Thenzawl", "थेनज़ॉल के पास", "थेनझॉलजवळ")),
        it3("phawngpui", "Phawngpui", "फ़ॉङपुई", "फॉङपुई", m=("Blue Mountain", "ब्लू माउंटेन", "ब्लू माउंटन")),
    ], title=L("Top places", "प्रमुख स्थल", "प्रमुख ठिकाणे"), conf="Editorial"),
    gaps("g", [(L("Tourist arrivals by year", "वर्षवार पर्यटक आगमन", "वर्षनिहाय पर्यटक आगमन"), "tourism", "Mizoram Tourism Department.")]),
])


def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "cities", [
    lst("cities", [
        city("aizawl", ("Aizawl", "आइज़ोल", "आयझॉल"), ("Ridge-top capital.", "पहाड़ी पर बसी राजधानी।", "डोंगरकड्यावरील राजधानी."), ("Capital", "राजधानी", "राजधानी")),
        city("lunglei", ("Lunglei", "लुंगलेई", "लुंगलेई"), ("Main town of the south.", "दक्षिण का मुख्य नगर।", "दक्षिणेकडील मुख्य शहर."), ("Administration", "प्रशासन", "प्रशासन")),
        city("champhai", ("Champhai", "चम्फाई", "चम्फाई"), ("Border trade with Myanmar at Zokhawthar.", "ज़ोखॉथार में म्यांमार के साथ सीमा व्यापार।", "झोखॉथार येथे म्यानमारशी सीमाव्यापार."), ("Trade", "व्यापार", "व्यापार")),
        city("kolasib", ("Kolasib", "कोलासिब", "कोलासिब"), ("Gateway from Assam.", "असम से प्रवेश द्वार।", "आसामकडून प्रवेशद्वार."), ("Transport", "परिवहन", "वाहतूक")),
        city("serchhip", ("Serchhip", "सेरछिप", "सेरछिप"), ("District town in central Mizoram.", "मध्य मिज़ोरम का ज़िला नगर।", "मध्य मिझोराममधील जिल्ह्याचे शहर."), ("Administration", "प्रशासन", "प्रशासन")),
    ], title=L("Major towns", "प्रमुख नगर", "प्रमुख शहरे"), conf="Editorial"),
])

module(R, "sports", [
    prose("p1", L(
        "Football is the leading sport: Aizawl FC won the I-League in 2016-17, and players such as Jeje Lalpekhlua and Lalianzuala Chhangte have played for India. Lalrinnunga Jeremy won weightlifting gold at the 2018 Youth Olympics and the 2022 Commonwealth Games. Boxing, volleyball and archery are also popular.",
        "फ़ुटबॉल प्रमुख खेल है: आइज़ोल एफ़सी ने 2016-17 में आई-लीग जीती, और जेजे लालपेखलुआ और लालियानज़ुआला छांगते जैसे खिलाड़ी भारत के लिए खेले हैं। लालरिननुंगा जेरेमी ने 2018 के युवा ओलंपिक और 2022 के राष्ट्रमंडल खेलों में भारोत्तोलन में स्वर्ण जीता। मुक्केबाज़ी, वॉलीबॉल और तीरंदाज़ी भी लोकप्रिय हैं।",
        "फुटबॉल हा प्रमुख खेळ आहे: आयझॉल एफसीने 2016-17 मध्ये आय-लीग जिंकली, आणि जेजे लालपेखलुआ व लालियानझुआला छांगते सारखे खेळाडू भारताकडून खेळले आहेत. लालरिननुंगा जेरेमी यांनी 2018 युवा ऑलिंपिक व 2022 राष्ट्रकुल खेळांत भारोत्तोलनात सुवर्ण जिंकले. मुष्टियुद्ध, व्हॉलीबॉल व धनुर्विद्याही लोकप्रिय आहेत."),
        conf="Editorial"),
])


def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("laldenga", ("Laldenga", "लालडेंगा", "लालडेंगा"), ("MNF leader; signed the 1986 accord and became the first Chief Minister.", "एमएनएफ़ नेता; 1986 का समझौता किया और पहले मुख्यमंत्री बने।", "एमएनएफ नेते; 1986 चा करार केला व पहिले मुख्यमंत्री झाले."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("zoramthanga", ("Zoramthanga", "ज़ोरमथांगा", "झोरमथांगा"), ("Chief Minister for three terms (1998–2008, 2018–2023).", "तीन कार्यकालों के मुख्यमंत्री (1998–2008, 2018–2023)।", "तीन कारकिर्दींचे मुख्यमंत्री (1998–2008, 2018–2023)."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("jeje", ("Jeje Lalpekhlua", "जेजे लालपेखलुआ", "जेजे लालपेखलुआ"), ("Footballer and India striker.", "फ़ुटबॉलर और भारत के स्ट्राइकर।", "फुटबॉलपटू व भारताचे आघाडीपटू."), ("Sport", "खेल", "क्रीडा")),
        person("jeremy", ("Lalrinnunga Jeremy", "लालरिननुंगा जेरेमी", "लालरिननुंगा जेरेमी"), ("Weightlifter; Commonwealth Games gold 2022.", "भारोत्तोलक; 2022 राष्ट्रमंडल खेलों में स्वर्ण।", "भारोत्तोलक; 2022 राष्ट्रकुल खेळांत सुवर्ण."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

module(R, "diaspora", [
    prose("p1", L(
        "Mizo and related Chin–Kuki peoples live across the border in Myanmar's Chin State and in Manipur, Tripura and Bangladesh. Many young Mizos study and work in Delhi, Bengaluru, Shillong and Guwahati, and small communities live abroad.",
        "मिज़ो और संबंधित चिन–कुकी लोग सीमा पार म्यांमार के चिन राज्य और मणिपुर, त्रिपुरा और बांग्लादेश में रहते हैं। बहुत से युवा मिज़ो दिल्ली, बेंगलुरु, शिलांग और गुवाहाटी में पढ़ते और काम करते हैं, और छोटे समुदाय विदेश में रहते हैं।",
        "मिझो व संबंधित चिन–कुकी लोक सीमेपलीकडे म्यानमारच्या चिन राज्यात आणि मणिपूर, त्रिपुरा व बांगलादेशात राहतात. अनेक तरुण मिझो दिल्ली, बंगळुरू, शिलाँग व गुवाहाटीत शिकतात व काम करतात, आणि लहान समुदाय परदेशात राहतात."),
        conf="Editorial"),
])

module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Mizoram portal", "मिज़ोरम सरकार पोर्टल", "मिझोराम शासन संकेतस्थळ", url="https://mizoram.gov.in", src="india-gov"),
        it3("assembly", "Mizoram Legislative Assembly", "मिज़ोरम विधानसभा", "मिझोराम विधानसभा", url="https://mizoramassembly.in", src="mz-assembly"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
])


def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("lit", ("Mizoram's literacy rate was 91.3% at the 2011 Census.", "2011 की जनगणना में मिज़ोरम की साक्षरता दर 91.3% थी।", "2011 च्या जनगणनेत मिझोरामचा साक्षरता दर 91.3% होता."), "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf", "es-india"),
        triv("forest", ("About 85% of the State is forest (ISFR 2023).", "राज्य का लगभग 85% भाग वन है (आईएसएफ़आर 2023)।", "राज्याचा सुमारे 85% भाग वनाच्छादित आहे (आयएसएफआर 2023)."), LS_FOREST, "fsi"),
        triv("rail", ("The railway reached Sairang near Aizawl in September 2025.", "सितंबर 2025 में रेल आइज़ोल के पास सैरांग पहुँची।", "सप्टेंबर 2025 मध्ये रेल्वे आयझॉलजवळ सैरांगला पोहोचली.")),
        triv("script", ("Mizo is written in the Roman alphabet, adapted by missionaries in the 1890s.", "मिज़ो रोमन वर्णमाला में लिखी जाती है, जिसे 1890 के दशक में मिशनरियों ने अपनाया।", "मिझो रोमन वर्णमालेत लिहिली जाते, जी 1890 च्या दशकात मिशनऱ्यांनी स्वीकारली.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("mz mod3 ok")
