"""Tripura modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-TR"
tr = read("regions/IN-TR.json")["metrics"]; ind = read("india.json")["metrics"]
C = research("census_b5plus.json"); F = C["forest"]["TR"]

module(R, "nature", [
    prose("p1", L(
        "About 72% of Tripura is forest (ISFR 2023), much of it mixed moist deciduous forest with bamboo. Sepahijala Wildlife Sanctuary, known for its spectacled (Phayre's) leaf monkeys and clouded leopard enclosure, Trishna Wildlife Sanctuary with its gaur (bison), and the Rowa and Gumti sanctuaries are the main protected areas. Rudrasagar lake, home to Neermahal palace, was designated a Ramsar site on 8 November 2005.",
        "त्रिपुरा का लगभग 72% भाग वन है (आईएसएफ़आर 2023), जिसका बड़ा हिस्सा बाँस वाले मिश्रित नम पर्णपाती वन हैं। फ़ेयर के पत्ती बंदरों और धूमिल तेंदुआ बाड़े के लिए प्रसिद्ध सिपाहीजला वन्यजीव अभयारण्य, गौर (बाइसन) वाला तृष्णा वन्यजीव अभयारण्य, और रोवा व गुमती अभयारण्य मुख्य संरक्षित क्षेत्र हैं। नीरमहल महल वाली रुद्रसागर झील को 8 नवंबर 2005 को रामसर स्थल घोषित किया गया।",
        "त्रिपुराचा सुमारे 72% भाग वनाच्छादित आहे (आयएसएफआर 2023), ज्यातील बराचसा बांबू असलेले मिश्र आर्द्र पानगळी वन आहे. फेअरची पानमाकडे व ढगाळ बिबट्याच्या कुंपणासाठी प्रसिद्ध सिपाहीजला वन्यजीव अभयारण्य, गवा असलेले तृष्णा वन्यजीव अभयारण्य, आणि रोवा व गुमती अभयारण्ये ही मुख्य संरक्षित क्षेत्रे आहेत. नीरमहाल असलेल्या रुद्रसागर सरोवराला 8 नोव्हेंबर 2005 रोजी रामसर स्थळ घोषित केले गेले."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), tr["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(1, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: Rudrasagar Lake (8 Nov 2005, 240 ha)."), "number"),
    ]),
    lst("protected", [
        it3("sepahijala", "Sepahijala Wildlife Sanctuary", "सिपाहीजला वन्यजीव अभयारण्य", "सिपाहीजला वन्यजीव अभयारण्य"),
        it3("trishna", "Trishna Wildlife Sanctuary", "तृष्णा वन्यजीव अभयारण्य", "तृष्णा वन्यजीव अभयारण्य", m=("Gaur", "गौर", "गवा")),
        it3("rudrasagar", "Rudrasagar Lake", "रुद्रसागर झील", "रुद्रसागर सरोवर", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
        it3("gumti", "Gumti Wildlife Sanctuary", "गुमती वन्यजीव अभयारण्य", "गुमती वन्यजीव अभयारण्य", m=("Dumbur reservoir", "डुम्बुर जलाशय", "डुम्बुर जलाशय")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
])

module(R, "water", [
    prose("p1", L(
        "Tripura's rivers are short and rain-fed, and most flow into Bangladesh, so sharing river water — especially of the Feni and the Manu — is a matter for India–Bangladesh talks. Ponds and lakes are used for fish farming across the State, and groundwater supplies most drinking water; iron content is high in many areas.",
        "त्रिपुरा की नदियाँ छोटी और वर्षा पर आधारित हैं, और अधिकांश बांग्लादेश में बहती हैं, इसलिए नदी जल का बँटवारा — विशेषकर फेनी और मनु का — भारत–बांग्लादेश वार्ता का विषय है। पूरे राज्य में तालाबों और झीलों में मछली पालन होता है, और अधिकांश पेयजल भूजल से आता है; कई क्षेत्रों में लौह की मात्रा अधिक है।",
        "त्रिपुराच्या नद्या लहान व पावसावर अवलंबून आहेत, आणि बहुतेक बांगलादेशात वाहतात, त्यामुळे नदीपाण्याची वाटणी — विशेषतः फेनी व मनूची — भारत–बांगलादेश चर्चेचा विषय आहे. संपूर्ण राज्यात तलाव व सरोवरांत मत्स्यपालन होते, आणि बहुतांश पिण्याचे पाणी भूजलातून येते; अनेक भागांत लोहाचे प्रमाण जास्त आहे."),
        conf="Editorial"),
    gaps("g", [(L("Household tap-water coverage", "घरेलू नल जल कवरेज", "घरगुती नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard.")]),
])

module(R, "safety", [
    prose("p1", L(
        "Tripura lies in seismic zone V. Heavy monsoon rain causes floods in the Gomati, Haora and Khowai valleys — severe floods in August 2024 affected large parts of the State — and landslides in the hills. Visitors should check weather warnings in the rains.",
        "त्रिपुरा भूकंपीय क्षेत्र V में है। भारी मानसूनी वर्षा गोमती, हावड़ा और खोवाई घाटियों में बाढ़ — अगस्त 2024 की भीषण बाढ़ ने राज्य के बड़े भागों को प्रभावित किया — और पहाड़ियों में भूस्खलन लाती है। पर्यटकों को वर्षा में मौसम चेतावनियाँ देखनी चाहिए।",
        "त्रिपुरा भूकंप क्षेत्र V मध्ये आहे. मुसळधार मान्सूनी पाऊस गोमती, हावडा व खोवाई खोऱ्यांत पूर — ऑगस्ट 2024 च्या भीषण पुराने राज्याच्या मोठ्या भागाला फटका बसला — आणि डोंगरांत भूस्खलन आणतो. पर्यटकांनी पावसाळ्यात हवामान इशारे पाहावेत."),
        conf="Editorial"),
    emergency_table(("Tripura", "त्रिपुरा", "त्रिपुरा")),
    gaps("g", [(L("August 2024 floods — official damage assessment", "अगस्त 2024 बाढ़ — आधिकारिक क्षति आकलन", "ऑगस्ट 2024 पूर — अधिकृत नुकसान मूल्यांकन"), "ndma", "Tripura State Disaster Management Authority.")]),
])

module(R, "gi", [
    prose("p1", L(
        "Four GIs belong to Tripura on the GI Registry's list as on 31 December 2025: the Queen pineapple (filed in 2013), the Risa textile, the Pachra-Rignai textile and the Matabari peda, the milk sweet offered at the Tripura Sundari temple.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में चार जीआई त्रिपुरा के हैं: क्वीन अनानास (2013 में दायर), रिसा वस्त्र, पाछरा-रिग्नाई वस्त्र और त्रिपुरा सुंदरी मंदिर में चढ़ाई जाने वाली दूध की मिठाई माताबाड़ी पेड़ा।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत चार जीआय त्रिपुराचे आहेत: क्वीन अननस (2013 मध्ये दाखल), रिसा वस्त्र, पाछरा-रिग्नाई वस्त्र आणि त्रिपुरा सुंदरी मंदिरात अर्पण केली जाणारी दुधाची मिठाई माताबाडी पेढा."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
])

module(R, "tourism", [
    prose("p1", L(
        "Agartala's Ujjayanta Palace (now the State Museum), the Jagannath and Ummaneshwar temples and the Heritage Park are the city's highlights. South of the capital, Neermahal rises from Rudrasagar lake, and Udaipur has the Tripura Sundari temple and the Bhuvaneshwari temple described in Tagore's writings. In the north, Unakoti's rock carvings and the Jampui hills, with orange orchards and views over Bangladesh and Mizoram, are worth the journey; Pilak, Chabimura's river-cliff carvings and Dumbur lake are other attractions.",
        "अगरतला का उज्जयंत महल (अब राज्य संग्रहालय), जगन्नाथ और उम्मनेश्वर मंदिर और हेरिटेज पार्क शहर के प्रमुख आकर्षण हैं। राजधानी के दक्षिण में नीरमहल रुद्रसागर झील से उठता है, और उदयपुर में त्रिपुरा सुंदरी मंदिर और टैगोर की रचनाओं में वर्णित भुवनेश्वरी मंदिर हैं। उत्तर में उनाकोटी की शैल नक्काशी और संतरे के बाग़ों व बांग्लादेश और मिज़ोरम के दृश्यों वाली जामपुई पहाड़ियाँ यात्रा योग्य हैं; पिलाक, छबिमुड़ा की नदी किनारे की चट्टानी नक्काशी और डुम्बुर झील अन्य आकर्षण हैं।",
        "आगरतळ्यातील उज्जयंत राजवाडा (आता राज्य संग्रहालय), जगन्नाथ व उम्मनेश्वर मंदिरे आणि हेरिटेज पार्क ही शहराची वैशिष्ट्ये आहेत. राजधानीच्या दक्षिणेला नीरमहाल रुद्रसागर सरोवरातून उभा आहे, आणि उदयपूरमध्ये त्रिपुरा सुंदरी मंदिर व टागोरांच्या लेखनात वर्णन केलेले भुवनेश्वरी मंदिर आहे. उत्तरेला उनाकोटीची खडकावरील कोरीवकामे आणि संत्र्यांच्या बागा व बांगलादेश आणि मिझोरामचे दृश्य असलेल्या जामपुई टेकड्या पाहण्याजोग्या आहेत; पिलाक, छबिमुडाची नदीकाठच्या कड्यावरील कोरीवकामे व डुम्बुर सरोवर ही इतर आकर्षणे आहेत."),
        conf="Editorial"),
    lst("places", [
        it3("ujjayanta", "Ujjayanta Palace", "उज्जयंत महल", "उज्जयंत राजवाडा", m=("Agartala", "अगरतला", "आगरतळा")),
        it3("neermahal", "Neermahal", "नीरमहल", "नीरमहाल", m=("Melaghar", "मेलाघर", "मेलाघर")),
        it3("udaipur", "Tripura Sundari, Udaipur", "त्रिपुरा सुंदरी, उदयपुर", "त्रिपुरा सुंदरी, उदयपूर", m=("Temple", "मंदिर", "मंदिर")),
        it3("unakoti", "Unakoti", "उनाकोटी", "उनाकोटी", m=("Rock carvings", "शैल नक्काशी", "खडकावरील कोरीवकाम")),
        it3("jampui", "Jampui hills", "जामपुई पहाड़ियाँ", "जामपुई टेकड्या", m=("Orange festival in November", "नवंबर में संतरा उत्सव", "नोव्हेंबरमध्ये संत्रा महोत्सव")),
    ], title=L("Top places", "प्रमुख स्थल", "प्रमुख ठिकाणे"), conf="Editorial"),
    gaps("g", [(L("Tourist arrivals by year", "वर्षवार पर्यटक आगमन", "वर्षनिहाय पर्यटक आगमन"), "tourism", "Tripura Tourism Development Corporation.")]),
])


def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "cities", [
    lst("cities", [
        city("agartala", ("Agartala", "अगरतला", "आगरतळा"), ("Capital near the Bangladesh border.", "बांग्लादेश सीमा के पास राजधानी।", "बांगलादेश सीमेजवळील राजधानी."), ("Capital", "राजधानी", "राजधानी")),
        city("udaipur", ("Udaipur", "उदयपुर", "उदयपूर"), ("Old royal capital and temple town.", "पुरानी राजधानी और मंदिर नगर।", "जुनी राजधानी व मंदिरनगरी."), ("Heritage", "धरोहर", "वारसा")),
        city("dharmanagar", ("Dharmanagar", "धर्मनगर", "धर्मनगर"), ("Main town of North Tripura.", "उत्तर त्रिपुरा का मुख्य नगर।", "उत्तर त्रिपुराचे मुख्य शहर."), ("Trade", "व्यापार", "व्यापार")),
        city("kailashahar", ("Kailashahar", "कैलाशहर", "कैलाशहर"), ("Unakoti district headquarters.", "उनाकोटी ज़िला मुख्यालय।", "उनाकोटी जिल्हा मुख्यालय."), ("Administration", "प्रशासन", "प्रशासन")),
        city("sabroom", ("Sabroom", "सबरूम", "सबरूम"), ("Southern border town at Maitri Setu.", "मैत्री सेतु पर दक्षिणी सीमावर्ती नगर।", "मैत्री सेतूवरील दक्षिणेकडील सीमावर्ती शहर."), ("Trade", "व्यापार", "व्यापार")),
    ], title=L("Major towns", "प्रमुख नगर", "प्रमुख शहरे"), conf="Editorial"),
])

module(R, "sports", [
    prose("p1", L(
        "Gymnast Dipa Karmakar of Agartala finished fourth in the vault at the Rio 2016 Olympics, the first Indian woman gymnast to compete at the Olympics, and later won the Asian championship vault title in 2024. Football, cricket and kho-kho are widely played, and traditional sports such as boat races are held at festivals.",
        "अगरतला की जिमनास्ट दीपा करमाकर रियो 2016 ओलंपिक में वॉल्ट में चौथे स्थान पर रहीं, ओलंपिक में भाग लेने वाली पहली भारतीय महिला जिमनास्ट, और बाद में 2024 में एशियाई चैंपियनशिप वॉल्ट ख़िताब जीता। फ़ुटबॉल, क्रिकेट और खो-खो व्यापक रूप से खेले जाते हैं, और त्योहारों पर नौका दौड़ जैसे पारंपरिक खेल होते हैं।",
        "आगरतळ्याच्या जिम्नॅस्ट दीपा कर्माकर रिओ 2016 ऑलिंपिकमध्ये व्हॉल्टमध्ये चौथ्या आल्या, ऑलिंपिकमध्ये सहभागी झालेल्या पहिल्या भारतीय महिला जिम्नॅस्ट, आणि नंतर 2024 मध्ये आशियाई अजिंक्यपद व्हॉल्ट जिंकले. फुटबॉल, क्रिकेट व खो-खो मोठ्या प्रमाणावर खेळले जातात, आणि सणांना नौकाशर्यतीसारखे पारंपरिक खेळ होतात."),
        conf="Editorial"),
])


def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("sdburman", ("S. D. Burman", "एस. डी. बर्मन", "एस. डी. बर्मन"), ("Composer and singer, born into the Tripura royal family.", "संगीतकार और गायक, त्रिपुरा राजपरिवार में जन्मे।", "संगीतकार व गायक, त्रिपुरा राजघराण्यात जन्मलेले."), ("Music", "संगीत", "संगीत")),
        person("birchandra", ("Bir Chandra Manikya", "बीर चंद्र माणिक्य", "बीर चंद्र माणिक्य"), ("Maharaja (1862–1896), moderniser and patron of Tagore.", "महाराजा (1862–1896), आधुनिकीकरण करने वाले और टैगोर के संरक्षक।", "महाराजा (1862–1896), आधुनिकीकरण करणारे व टागोरांचे आश्रयदाते."), ("History", "इतिहास", "इतिहास")),
        person("dasarath", ("Dasarath Deb", "दशरथ देब", "दशरथ देब"), ("Tribal leader and Chief Minister (1993–98).", "जनजातीय नेता और मुख्यमंत्री (1993–98)।", "आदिवासी नेते व मुख्यमंत्री (1993–98)."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("dipa", ("Dipa Karmakar", "दीपा करमाकर", "दीपा कर्माकर"), ("Artistic gymnast; fourth in the vault at Rio 2016.", "कलात्मक जिमनास्ट; रियो 2016 में वॉल्ट में चौथी।", "कलात्मक जिम्नॅस्ट; रिओ 2016 मध्ये व्हॉल्टमध्ये चौथ्या."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

module(R, "diaspora", [
    prose("p1", L(
        "Tripura's Bengali families have close ties with Bangladesh, and Kokborok-speaking communities also live in Bangladesh's Chittagong Hill Tracts. Many young people move to Kolkata, Guwahati, Bengaluru and Delhi for study and work.",
        "त्रिपुरा के बंगाली परिवारों के बांग्लादेश से निकट संबंध हैं, और कोकबोरोक भाषी समुदाय बांग्लादेश के चटगाँव पहाड़ी क्षेत्रों में भी रहते हैं। बहुत से युवा पढ़ाई और काम के लिए कोलकाता, गुवाहाटी, बेंगलुरु और दिल्ली जाते हैं।",
        "त्रिपुरातील बंगाली कुटुंबांचे बांगलादेशशी जवळचे नाते आहे, आणि कोकबोरोक भाषक समुदाय बांगलादेशातील चितगाव डोंगरी भागांतही राहतात. अनेक तरुण शिक्षण व कामासाठी कोलकाता, गुवाहाटी, बंगळुरू व दिल्लीला जातात."),
        conf="Editorial"),
])

module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Tripura portal", "त्रिपुरा सरकार पोर्टल", "त्रिपुरा शासन संकेतस्थळ", url="https://tripura.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
])


def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("st", ("Scheduled Tribes made up 31.8% of Tripura's population in 2011.", "2011 में त्रिपुरा की जनसंख्या में अनुसूचित जनजातियों का हिस्सा 31.8% था।", "2011 मध्ये त्रिपुराच्या लोकसंख्येत अनुसूचित जमातींचा वाटा 31.8% होता."), "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf", "dl-planning"),
        triv("ramsar", ("Rudrasagar Lake was designated a Ramsar site on 8 November 2005.", "रुद्रसागर झील को 8 नवंबर 2005 को रामसर स्थल घोषित किया गया।", "रुद्रसागर सरोवराला 8 नोव्हेंबर 2005 रोजी रामसर स्थळ घोषित केले गेले."), RAMSAR, "indian-wetlands"),
        triv("tagore", ("Rabindranath Tagore visited Agartala several times as a guest of the Manikya kings.", "रवींद्रनाथ टैगोर माणिक्य राजाओं के अतिथि के रूप में कई बार अगरतला आए।", "रवींद्रनाथ टागोर माणिक्य राजांचे पाहुणे म्हणून अनेकदा आगरतळ्याला आले.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("tr mod3 ok")
