"""Rajasthan modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-RJ"
DIST = "https://www.newsonair.gov.in/rajasthan-govt-announces-to-dissolve-9-out-of-17-districts-created-by-previous-govt"
rj = read("regions/IN-RJ.json")["metrics"]; ind = read("india.json")["metrics"]

RAMSAR_RJ = [
    ("Keoladeo National Park", "केवलादेव राष्ट्रीय उद्यान", "केवलादेव राष्ट्रीय उद्यान", "1981", "2,873"),
    ("Sambhar Lake", "सांभर झील", "सांभर सरोवर", "1990", "24,000"),
    ("Menar wetland complex", "मेनार आर्द्रभूमि परिसर", "मेनार पाणथळ संकुल", "2025", "463.41"),
    ("Khichan wetland", "खीचन आर्द्रभूमि", "खीचन पाणथळ", "2025", "54.19"),
    ("Siliserh Lake", "सिलीसेढ़ झील", "सिलीसेढ सरोवर", "2025", "315.97"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Only about 4.8% of Rajasthan is forest (ISFR 2023), mostly in the Aravallis and the south-east, yet the State is rich in wildlife adapted to dry country. Ranthambore, Sariska, Mukundra Hills, Ramgarh Vishdhari and Dholpur–Karauli are tiger reserves. The Desert National Park near Jaisalmer protects the great Indian bustard, the critically endangered State bird, along with chinkara, desert foxes and many raptors. Keoladeo at Bharatpur, a UNESCO World Heritage Site, is a famous winter home of water birds, and Tal Chhapar protects blackbuck. Bishnoi villages are known for protecting blackbuck, chinkara and khejri trees.\n\nThe State has five Ramsar sites: Keoladeo, Sambhar — India's largest inland saline lake — and, from 2025, Menar, Khichan, where thousands of demoiselle cranes winter, and Siliserh near Alwar.",
        "राजस्थान का केवल लगभग 4.8% भाग वन है (आईएसएफ़आर 2023), जो अधिकतर अरावली और दक्षिण-पूर्व में है, फिर भी राज्य शुष्क भूमि के अनुकूल वन्यजीवों से समृद्ध है। रणथंभौर, सरिस्का, मुकुंदरा हिल्स, रामगढ़ विषधारी और धौलपुर–करौली बाघ अभयारण्य हैं। जैसलमेर के पास मरु राष्ट्रीय उद्यान गंभीर रूप से संकटग्रस्त राज्य पक्षी गोडावण के साथ चिंकारा, मरु लोमड़ी और कई शिकारी पक्षियों की रक्षा करता है। भरतपुर का केवलादेव, जो यूनेस्को विश्व धरोहर स्थल है, जल पक्षियों का प्रसिद्ध शीतकालीन घर है, और ताल छापर काले हिरणों की रक्षा करता है। बिश्नोई गाँव काले हिरण, चिंकारा और खेजड़ी के पेड़ों की रक्षा के लिए जाने जाते हैं।\n\nराज्य में पाँच रामसर स्थल हैं: केवलादेव, सांभर — भारत की सबसे बड़ी अंतर्देशीय खारी झील — और 2025 से मेनार, खीचन, जहाँ हज़ारों कुरजाँ सर्दियाँ बिताती हैं, और अलवर के पास सिलीसेढ़।",
        "राजस्थानचा केवळ सुमारे 4.8% भाग वनाच्छादित आहे (आयएसएफआर 2023), बहुतांश अरवली व आग्नेय भागात, तरीही राज्य कोरड्या प्रदेशाशी जुळवून घेतलेल्या वन्यजीवांनी समृद्ध आहे. रणथंभोर, सरिस्का, मुकुंदरा हिल्स, रामगड विषधारी व धौलपूर–करौली हे व्याघ्र प्रकल्प आहेत. जैसलमेरजवळील वाळवंट राष्ट्रीय उद्यान अतिसंकटग्रस्त राज्यपक्षी माळढोकसह चिंकारा, वाळवंटी कोल्हे व अनेक शिकारी पक्ष्यांचे रक्षण करते. भरतपूरचे केवलादेव — युनेस्को जागतिक वारसा स्थळ — पाणपक्ष्यांचे प्रसिद्ध हिवाळी घर आहे, आणि ताल छापर काळविटांचे रक्षण करते. बिश्नोई गावे काळवीट, चिंकारा व खेजडीच्या झाडांच्या रक्षणासाठी ओळखली जातात.\n\nराज्यात पाच रामसर स्थळे आहेत: केवलादेव, सांभर — भारतातील सर्वांत मोठे अंतर्गत खारे सरोवर — आणि 2025 पासून मेनार, खीचन, जिथे हजारो कुरकरू क्रौंच हिवाळा घालवतात, आणि अलवरजवळील सिलीसेढ."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(16548.21, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(16632.01, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), rj["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(5, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_RJ], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026 (year of designation).", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची (घोषणा वर्ष)।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी (घोषणा वर्ष).")),
    lst("protected", [
        it3("ranthambore", "Ranthambore Tiger Reserve", "रणथंभौर बाघ अभयारण्य", "रणथंभोर व्याघ्र प्रकल्प", m=("Sawai Madhopur", "सवाई माधोपुर", "सवाई माधोपूर")),
        it3("sariska", "Sariska Tiger Reserve", "सरिस्का बाघ अभयारण्य", "सरिस्का व्याघ्र प्रकल्प", m=("Alwar", "अलवर", "अलवर")),
        it3("mukundra", "Mukundra Hills Tiger Reserve", "मुकुंदरा हिल्स बाघ अभयारण्य", "मुकुंदरा हिल्स व्याघ्र प्रकल्प", m=("Kota", "कोटा", "कोटा")),
        it3("dnp", "Desert National Park", "मरु राष्ट्रीय उद्यान", "वाळवंट राष्ट्रीय उद्यान", m=("Great Indian bustard", "गोडावण", "माळढोक")),
        it3("keoladeo", "Keoladeo National Park", "केवलादेव राष्ट्रीय उद्यान", "केवलादेव राष्ट्रीय उद्यान", m=("UNESCO; birds", "यूनेस्को; पक्षी", "युनेस्को; पक्षी")),
        it3("talchhapar", "Tal Chhapar Sanctuary", "ताल छापर अभयारण्य", "ताल छापर अभयारण्य", m=("Blackbuck", "काला हिरण", "काळवीट")),
        it3("kumbhalgarh", "Kumbhalgarh Wildlife Sanctuary", "कुंभलगढ़ वन्यजीव अभयारण्य", "कुंभलगड वन्यजीव अभयारण्य", m=("Aravallis", "अरावली", "अरवली")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("gib", "Great Indian bustard (State bird)", "गोडावण (राज्य पक्षी)", "माळढोक (राज्यपक्षी)"), it3("chinkara", "Chinkara (State animal)", "चिंकारा (राज्य पशु)", "चिंकारा (राज्यप्राणी)"),
        it3("tiger", "Tiger", "बाघ", "वाघ"), it3("blackbuck", "Blackbuck", "काला हिरण", "काळवीट"),
        it3("crane", "Demoiselle crane", "कुरजाँ", "कुरकरू क्रौंच"), it3("camel", "Dromedary camel", "ऊँट", "उंट"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger estimates by reserve", "अभयारण्यवार बाघों का अनुमान", "प्रकल्पनिहाय वाघांचा अंदाज"), "ntca", "NTCA All India Tiger Estimation."),
        (L("Great Indian bustard population", "गोडावण की संख्या", "माळढोकांची संख्या"), "moefcc", "MoEFCC / Wildlife Institute of India estimates."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Water is Rajasthan's oldest challenge. The State has about a tenth of India's land but very little of its surface water, and much of its groundwater is over-used. Traditional structures — stepwells (baoris), tanks, johads and village ponds — stored rain for centuries, and community groups have revived many of them. The Indira Gandhi Canal, fed from the Harike barrage in Punjab, carries Sutlej and Beas water deep into the northern desert and has turned parts of Sri Ganganagar, Hanumangarh and Bikaner into farmland. The Chambal dams supply the Kota region, and the Ramjal Setu link project aims to move water to the eastern districts. Fluoride and salinity in groundwater are common in the west.",
        "पानी राजस्थान की सबसे पुरानी चुनौती है। राज्य के पास भारत की लगभग दसवीं भूमि है, लेकिन सतही जल बहुत कम है, और भूजल का बड़ा हिस्सा अति-दोहित है। पारंपरिक संरचनाएँ — बावड़ियाँ, तालाब, जोहड़ और गाँव के कुंड — सदियों से वर्षा का पानी संजोती रहीं, और सामुदायिक समूहों ने उनमें से कई को फिर जीवित किया है। पंजाब के हरिके बराज से निकलने वाली इंदिरा गांधी नहर सतलुज और ब्यास का पानी उत्तरी मरुस्थल में दूर तक ले जाती है और श्रीगंगानगर, हनुमानगढ़ और बीकानेर के कुछ हिस्सों को खेती योग्य बना चुकी है। चंबल के बाँध कोटा क्षेत्र को पानी देते हैं, और रामजल सेतु लिंक परियोजना का उद्देश्य पूर्वी ज़िलों तक पानी पहुँचाना है। पश्चिम में भूजल में फ़्लोराइड और खारापन आम है।",
        "पाणी हे राजस्थानचे सर्वांत जुने आव्हान आहे. राज्याकडे भारताची सुमारे दहावी जमीन आहे, पण भूपृष्ठजल फारच कमी, आणि भूजलाचा मोठा भाग अतिउपसा झालेला आहे. पारंपरिक रचना — पायविहिरी (बावडी), तलाव, जोहड व गावतळी — शतकानुशतके पावसाचे पाणी साठवत आल्या, आणि सामुदायिक गटांनी त्यांपैकी अनेकांचे पुनरुज्जीवन केले आहे. पंजाबमधील हरिके बंधाऱ्यातून निघणारा इंदिरा गांधी कालवा सतलज व बियासचे पाणी उत्तरेकडील वाळवंटात खोलवर नेतो आणि त्याने श्रीगंगानगर, हनुमानगड व बिकानेरचे काही भाग शेतीयोग्य केले आहेत. चंबळवरील धरणे कोटा प्रदेशाला पाणी देतात, आणि रामजल सेतू जोड प्रकल्पाचा उद्देश पूर्वेकडील जिल्ह्यांपर्यंत पाणी पोहोचवणे हा आहे. पश्चिमेत भूजलात फ्लोराइड व क्षारता सामान्य आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
        (L("Fluoride-affected habitations", "फ़्लोराइड प्रभावित बस्तियाँ", "फ्लोराइडबाधित वस्त्या"), "india-gov", "Jal Jeevan Mission water-quality data."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Extreme heat is the main hazard: in May and June, temperatures in the western and northern districts can approach or exceed 50 °C, and heatstroke is a real danger. Droughts are frequent, dust storms sweep the desert before the monsoon, and occasional heavy rain causes flash floods in normally dry areas, as in Barmer in 2006. Desert locust swarms reached the State in 2019–20.\n\nVisitors should travel in the cooler months where possible, drink plenty of water, avoid midday exposure in summer and follow official advice on desert safaris.",
        "भीषण गर्मी मुख्य ख़तरा है: मई और जून में पश्चिमी और उत्तरी ज़िलों में तापमान 50 °C के क़रीब या उससे ऊपर पहुँच सकता है, और लू लगना वास्तविक ख़तरा है। सूखा अक्सर पड़ता है, मानसून से पहले मरुस्थल में आँधियाँ चलती हैं, और कभी-कभी भारी वर्षा सामान्यतः सूखे क्षेत्रों में अचानक बाढ़ लाती है, जैसे 2006 में बाड़मेर में। 2019–20 में टिड्डी दल राज्य तक पहुँचे।\n\nपर्यटकों को जहाँ तक हो सके ठंडे महीनों में यात्रा करनी चाहिए, ख़ूब पानी पीना चाहिए, गर्मियों में दोपहर की धूप से बचना चाहिए और मरु सफ़ारी पर आधिकारिक सलाह माननी चाहिए।",
        "प्रचंड उष्णता हा मुख्य धोका आहे: मे-जूनमध्ये पश्चिम व उत्तरेकडील जिल्ह्यांत तापमान 50 °C च्या जवळ किंवा पुढे जाऊ शकते, आणि उष्माघात हा खरा धोका आहे. दुष्काळ वारंवार पडतो, मान्सूनपूर्वी वाळवंटात धुळीची वादळे येतात, आणि कधीकधी मुसळधार पावसाने सामान्यतः कोरड्या भागांत अचानक पूर येतो, जसे 2006 मध्ये बाडमेरमध्ये. 2019–20 मध्ये टोळधाड राज्यात पोहोचली.\n\nपर्यटकांनी शक्य तिथे थंड महिन्यांत प्रवास करावा, भरपूर पाणी प्यावे, उन्हाळ्यात दुपारचे ऊन टाळावे आणि वाळवंटी सफारीसाठी अधिकृत सूचना पाळाव्यात."),
        conf="Editorial"),
    emergency_table(("Rajasthan", "राजस्थान", "राजस्थान")),
    lst("links", [
        it3("imd", "IMD heatwave and weather warnings", "आईएमडी लू और मौसम चेतावनियाँ", "आयएमडी उष्णतेची लाट व हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official Rajasthan disaster management address."),
        (L("Drought-declared districts by year", "वर्षवार सूखाग्रस्त घोषित ज़िले", "वर्षनिहाय दुष्काळग्रस्त जाहीर जिल्हे"), "india-gov", "State Disaster Management and Relief Department."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Rajasthan has 21 registered Geographical Indications of its own in the GI Registry's list as on 31 December 2025, and shares Phulkari embroidery with Punjab and Haryana. Several appear twice, as a word mark and as a logo — Kota Doria, Blue Pottery of Jaipur, Molela clay work and the Kathputlis of Rajasthan. Other crafts include Sanganeri and Bagru block printing, Thewa work, Pokaran pottery, Nathdwara pichhwai painting, Udaipur koftgari, Bikaner kashidakari and usta kala, and Jodhpur bandhej. Makrana marble is a natural-goods GI, and Bikaneri bhujia, Sojat mehndi and Nagori ashwagandha are food and agricultural GIs.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में राजस्थान के अपने 21 पंजीकृत भौगोलिक संकेतक हैं, और फुलकारी कढ़ाई पंजाब और हरियाणा के साथ साझा है। कई दो बार आते हैं, शब्द चिह्न और लोगो के रूप में — कोटा डोरिया, जयपुर की ब्लू पॉटरी, मोलेला मृण्मूर्ति शिल्प और राजस्थान की कठपुतलियाँ। अन्य शिल्पों में सांगानेरी और बगरू ठप्पा छपाई, थेवा कला, पोकरण के मिट्टी के बर्तन, नाथद्वारा पिछवाई चित्रकला, उदयपुर कोफ़्तगरी, बीकानेर कशीदाकारी और उस्ता कला, और जोधपुर बंधेज शामिल हैं। मकराना संगमरमर प्राकृतिक वस्तु जीआई है, और बीकानेरी भुजिया, सोजत मेहंदी और नागौरी अश्वगंधा खाद्य और कृषि जीआई हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत राजस्थानची स्वतःची 21 नोंदणीकृत भौगोलिक मानांकने आहेत, आणि फुलकारी भरतकाम पंजाब व हरियाणासोबत सामायिक आहे. अनेक मानांकने दोनदा येतात, शब्दचिन्ह व बोधचिन्ह म्हणून — कोटा डोरिया, जयपूरची निळी मृद्भांडी, मोलेला मातीकाम व राजस्थानच्या कठपुतळ्या. इतर हस्तकलेत सांगानेरी व बगरू ठसे छपाई, थेवा कला, पोखरणची मृद्भांडी, नाथद्वारा पिछवाई चित्रकला, उदयपूर कोफ्तगरी, बिकानेर कशिदाकारी व उस्ता कला आणि जोधपूर बांधणी यांचा समावेश आहे. मकराना संगमरवर हे नैसर्गिक वस्तू जीआय आहे, आणि बिकानेरी भुजिया, सोजत मेंदी व नागौरी अश्वगंधा ही खाद्य व कृषी जीआय आहेत."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Rajasthan is one of India's most visited States. Jaipur — with Amber Fort, the City Palace, Hawa Mahal and Jantar Mantar — forms the 'Golden Triangle' with Delhi and Agra. Udaipur's lakes and palaces, Jodhpur's Mehrangarh fort and blue city, and Jaisalmer's living fort and dunes draw visitors west. Pushkar and the Ajmer Sharif dargah are major pilgrimage centres; Ranthambore and Sariska offer tiger safaris; Chittorgarh and Kumbhalgarh are great hill forts; Mount Abu has the Dilwara temples; and Shekhawati's painted havelis and Bundi's stepwells reward slower travel.",
        "राजस्थान भारत के सबसे अधिक देखे जाने वाले राज्यों में है। जयपुर — आमेर क़िला, सिटी पैलेस, हवा महल और जंतर मंतर के साथ — दिल्ली और आगरा के साथ 'स्वर्णिम त्रिभुज' बनाता है। उदयपुर की झीलें और महल, जोधपुर का मेहरानगढ़ क़िला और नीला शहर, और जैसलमेर का बसा हुआ क़िला और टीले पर्यटकों को पश्चिम खींचते हैं। पुष्कर और अजमेर शरीफ़ दरगाह बड़े तीर्थ केंद्र हैं; रणथंभौर और सरिस्का में बाघ सफ़ारी है; चित्तौड़गढ़ और कुंभलगढ़ महान पहाड़ी क़िले हैं; माउंट आबू में दिलवाड़ा मंदिर हैं; और शेखावाटी की चित्रित हवेलियाँ और बूँदी की बावड़ियाँ धीमी यात्रा का आनंद देती हैं।",
        "राजस्थान हे भारतातील सर्वाधिक भेट दिल्या जाणाऱ्या राज्यांपैकी आहे. जयपूर — आमेर किल्ला, सिटी पॅलेस, हवा महल व जंतर मंतरसह — दिल्ली व आग्र्यासोबत 'सुवर्ण त्रिकोण' बनवते. उदयपूरची सरोवरे व राजवाडे, जोधपूरचा मेहरानगड किल्ला व निळे शहर, आणि जैसलमेरचा वस्ती असलेला किल्ला व वाळूच्या टेकड्या पर्यटकांना पश्चिमेकडे खेचतात. पुष्कर व अजमेर शरीफ दर्गा ही मोठी तीर्थक्षेत्रे आहेत; रणथंभोर व सरिस्का येथे वाघ सफारी आहे; चित्तोडगड व कुंभलगड हे महान डोंगरी किल्ले आहेत; माउंट अबूवर दिलवाडा मंदिरे आहेत; आणि शेखावटीच्या रंगवलेल्या हवेल्या व बुंदीच्या पायविहिरी निवांत प्रवासाचा आनंद देतात."),
        conf="Editorial"),
    lst("places", [
        it3("jaipur", "Jaipur: Amber, City Palace, Hawa Mahal", "जयपुर: आमेर, सिटी पैलेस, हवा महल", "जयपूर: आमेर, सिटी पॅलेस, हवा महल", m=("UNESCO city", "यूनेस्को शहर", "युनेस्को शहर")),
        it3("udaipur", "Udaipur", "उदयपुर", "उदयपूर", m=("Lakes, palaces", "झीलें, महल", "सरोवरे, राजवाडे")),
        it3("jodhpur", "Jodhpur and Mehrangarh", "जोधपुर और मेहरानगढ़", "जोधपूर व मेहरानगड", m=("Fort, blue city", "क़िला, नीला शहर", "किल्ला, निळे शहर")),
        it3("jaisalmer", "Jaisalmer and the Sam dunes", "जैसलमेर और सम के टीले", "जैसलमेर व सम वाळूच्या टेकड्या", m=("Desert", "मरुस्थल", "वाळवंट")),
        it3("ranthambore", "Ranthambore", "रणथंभौर", "रणथंभोर", m=("Tiger safari", "बाघ सफ़ारी", "वाघ सफारी")),
        it3("pushkar", "Pushkar and Ajmer", "पुष्कर और अजमेर", "पुष्कर व अजमेर", m=("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        it3("chittor", "Chittorgarh and Kumbhalgarh", "चित्तौड़गढ़ और कुंभलगढ़", "चित्तोडगड व कुंभलगड", m=("Hill forts", "पहाड़ी क़िले", "डोंगरी किल्ले")),
        it3("shekhawati", "Shekhawati havelis", "शेखावाटी हवेलियाँ", "शेखावटी हवेल्या", m=("Painted mansions", "चित्रित हवेलियाँ", "रंगवलेल्या हवेल्या")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Jaipur and Amber, with a day trip to Ranthambore or Pushkar.", "जयपुर और आमेर, साथ में रणथंभौर या पुष्कर की एक दिन की यात्रा।", "जयपूर व आमेर, सोबत रणथंभोर किंवा पुष्करची एक दिवसाची सहल.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Udaipur, Kumbhalgarh, Ranakpur and Chittorgarh.", "उदयपुर, कुंभलगढ़, रणकपुर और चित्तौड़गढ़।", "उदयपूर, कुंभलगड, रणकपूर व चित्तोडगड.")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Jodhpur, Jaisalmer and a desert camp, then Bikaner.", "जोधपुर, जैसलमेर और मरु शिविर, फिर बीकानेर।", "जोधपूर, जैसलमेर व वाळवंटी शिबिर, नंतर बिकानेर.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("rjt", "Rajasthan Tourism (official)", "राजस्थान पर्यटन (आधिकारिक)", "राजस्थान पर्यटन (अधिकृत)", url="https://www.tourism.rajasthan.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Ajmer", "अजमेर", "अजमेर"), ("Alwar", "अलवर", "अलवर"), ("Balotra", "बालोतरा", "बालोतरा"), ("Banswara", "बाँसवाड़ा", "बांसवाडा"), ("Baran", "बाराँ", "बारां"),
    ("Barmer", "बाड़मेर", "बाडमेर"), ("Beawar", "ब्यावर", "ब्यावर"), ("Bharatpur", "भरतपुर", "भरतपूर"), ("Bhilwara", "भीलवाड़ा", "भीलवाडा"), ("Bikaner", "बीकानेर", "बिकानेर"),
    ("Bundi", "बूँदी", "बुंदी"), ("Chittorgarh", "चित्तौड़गढ़", "चित्तोडगड"), ("Churu", "चूरू", "चुरू"), ("Dausa", "दौसा", "दौसा"), ("Deeg", "डीग", "डीग"),
    ("Dholpur", "धौलपुर", "धौलपूर"), ("Didwana-Kuchaman", "डीडवाना-कुचामन", "डीडवाना-कुचामन"), ("Dungarpur", "डूँगरपुर", "डुंगरपूर"), ("Hanumangarh", "हनुमानगढ़", "हनुमानगड"),
    ("Jaipur", "जयपुर", "जयपूर"), ("Jaisalmer", "जैसलमेर", "जैसलमेर"), ("Jalore", "जालोर", "जालोर"), ("Jhalawar", "झालावाड़", "झालावाड"), ("Jhunjhunu", "झुंझुनूँ", "झुंझुनू"),
    ("Jodhpur", "जोधपुर", "जोधपूर"), ("Karauli", "करौली", "करौली"), ("Khairthal-Tijara", "खैरथल-तिजारा", "खैरथल-तिजारा"), ("Kota", "कोटा", "कोटा"),
    ("Kotputli-Behror", "कोटपूतली-बहरोड़", "कोटपुतली-बहरोड"), ("Nagaur", "नागौर", "नागौर"), ("Pali", "पाली", "पाली"), ("Phalodi", "फलोदी", "फलोदी"),
    ("Pratapgarh", "प्रतापगढ़", "प्रतापगड"), ("Rajsamand", "राजसमंद", "राजसमंद"), ("Salumbar", "सलूंबर", "सलुंबर"), ("Sawai Madhopur", "सवाई माधोपुर", "सवाई माधोपूर"),
    ("Sikar", "सीकर", "सीकर"), ("Sirohi", "सिरोही", "सिरोही"), ("Sri Ganganagar", "श्रीगंगानगर", "श्रीगंगानगर"), ("Tonk", "टोंक", "टोंक"), ("Udaipur", "उदयपुर", "उदयपूर"),
]
assert len(DISTRICTS) == 41, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("jaipur", ("Jaipur", "जयपुर", "जयपूर"), ("State capital; the 'Pink City', planned in 1727; gems, crafts, IT.", "राज्य की राजधानी; 'गुलाबी नगरी', 1727 में नियोजित; रत्न, शिल्प, आईटी।", "राज्याची राजधानी; 'गुलाबी शहर', 1727 मध्ये नियोजित; रत्ने, हस्तकला, आयटी."), ("Capital", "राजधानी", "राजधानी")),
        city("jodhpur", ("Jodhpur", "जोधपुर", "जोधपूर"), ("Seat of the High Court; handicrafts and furniture; air base.", "उच्च न्यायालय का स्थान; हस्तशिल्प और फ़र्नीचर; वायुसेना अड्डा।", "उच्च न्यायालयाचे ठिकाण; हस्तकला व फर्निचर; हवाई तळ."), ("Marwar", "मारवाड़", "मारवाड")),
        city("kota", ("Kota", "कोटा", "कोटा"), ("Coaching hub on the Chambal; power and chemical industries.", "चंबल पर कोचिंग केंद्र; बिजली और रसायन उद्योग।", "चंबळकाठचे शिकवणी केंद्र; वीज व रसायन उद्योग."), ("Education", "शिक्षा", "शिक्षण")),
        city("udaipur", ("Udaipur", "उदयपुर", "उदयपूर"), ("City of lakes; capital of Mewar; zinc mining nearby.", "झीलों का शहर; मेवाड़ की राजधानी; पास में जस्ता खनन।", "सरोवरांचे शहर; मेवाडची राजधानी; जवळ जस्त खाणी."), ("Tourism", "पर्यटन", "पर्यटन")),
        city("bikaner", ("Bikaner", "बीकानेर", "बिकानेर"), ("Desert city of Junagarh fort, bhujia and camel research.", "जूनागढ़ क़िले, भुजिया और ऊँट अनुसंधान का मरु शहर।", "जुनागड किल्ला, भुजिया व उंट संशोधनाचे वाळवंटी शहर."), ("Desert", "मरुस्थल", "वाळवंट")),
        city("ajmer", ("Ajmer", "अजमेर", "अजमेर"), ("Dargah of Khwaja Moinuddin Chishti; gateway to Pushkar.", "ख़्वाजा मोइनुद्दीन चिश्ती की दरगाह; पुष्कर का प्रवेश द्वार।", "ख्वाजा मोईनुद्दीन चिश्ती यांचा दर्गा; पुष्करचे प्रवेशद्वार."), ("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        city("bhilwara", ("Bhilwara", "भीलवाड़ा", "भीलवाडा"), ("Textile city known for suiting fabric.", "सूटिंग कपड़े के लिए प्रसिद्ध वस्त्र नगर।", "सूटिंग कापडासाठी प्रसिद्ध वस्त्रनगरी."), ("Industry", "उद्योग", "उद्योग")),
        city("jaisalmer", ("Jaisalmer", "जैसलमेर", "जैसलमेर"), ("Golden fort city of the Thar.", "थार का स्वर्णिम क़िला नगर।", "थरचे सोनेरी किल्ल्याचे शहर."), ("Desert", "मरुस्थल", "वाळवंट")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 41 districts (alphabetical)", "41 ज़िले (वर्णानुक्रम)", "41 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    lst("dsrc", [it3("noa", "News On AIR: nine districts dissolved, 41 remain (28 Dec 2024)", "न्यूज़ ऑन एआईआर: नौ ज़िले भंग, 41 शेष (28 दिसंबर 2024)", "न्यूज ऑन एआयआर: नऊ जिल्हे बरखास्त, 41 उरले (28 डिसेंबर 2024)", url=DIST, src="newsonair")],
        title=L("Source for the district count", "ज़िलों की संख्या का स्रोत", "जिल्हा संख्येचा स्रोत"), conf="Official"),
    gaps("g", [
        (L("Official district list (State notification)", "आधिकारिक ज़िला सूची (राज्य अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य अधिसूचना)"), "india-gov", "Link the State's notification of December 2024."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Rajasthan has a strong record in shooting and para sport. Rajyavardhan Singh Rathore, born in Jaisalmer, won India's first individual Olympic silver medal in double trap shooting at Athens in 2004. Javelin thrower Devendra Jhajharia of Churu won Paralympic gold in 2004 and 2016, and shooter Avani Lekhara of Jaipur won Paralympic gold at Tokyo 2020 and Paris 2024. Polo has a long royal tradition in Jaipur and Jodhpur, and the Sawai Mansingh Stadium in Jaipur hosts international and IPL cricket. Traditional rural sports include camel races at desert fairs.",
        "राजस्थान का निशानेबाज़ी और पैरा खेलों में मज़बूत रिकॉर्ड है। जैसलमेर में जन्मे राज्यवर्धन सिंह राठौड़ ने 2004 में एथेंस में डबल ट्रैप निशानेबाज़ी में भारत का पहला व्यक्तिगत ओलंपिक रजत पदक जीता। चूरू के भाला फेंक खिलाड़ी देवेंद्र झाझरिया ने 2004 और 2016 में पैरालंपिक स्वर्ण जीते, और जयपुर की निशानेबाज़ अवनि लेखरा ने टोक्यो 2020 और पेरिस 2024 में पैरालंपिक स्वर्ण जीते। जयपुर और जोधपुर में पोलो की लंबी शाही परंपरा है, और जयपुर का सवाई मानसिंह स्टेडियम अंतरराष्ट्रीय और आईपीएल क्रिकेट की मेज़बानी करता है। पारंपरिक ग्रामीण खेलों में मरु मेलों की ऊँट दौड़ शामिल है।",
        "राजस्थानचा नेमबाजी व पॅरा क्रीडांत भक्कम विक्रम आहे. जैसलमेरमध्ये जन्मलेल्या राज्यवर्धन सिंह राठोड यांनी 2004 मध्ये अथेन्स येथे डबल ट्रॅप नेमबाजीत भारताचे पहिले वैयक्तिक ऑलिम्पिक रौप्यपदक जिंकले. चुरूचे भालाफेकपटू देवेंद्र झाझरिया यांनी 2004 व 2016 मध्ये पॅरालिंपिक सुवर्ण जिंकले, आणि जयपूरच्या नेमबाज अवनी लेखरा यांनी टोकियो 2020 व पॅरिस 2024 मध्ये पॅरालिंपिक सुवर्ण जिंकले. जयपूर व जोधपूरमध्ये पोलोची दीर्घ राजेशाही परंपरा आहे, आणि जयपूरचे सवाई मानसिंह स्टेडियम आंतरराष्ट्रीय व आयपीएल क्रिकेट आयोजित करते. पारंपरिक ग्रामीण खेळांत वाळवंटी जत्रांमधील उंटांच्या शर्यती आहेत."),
        conf="Editorial"),
    lst("venues", [
        it3("sms", "Sawai Mansingh Stadium, Jaipur", "सवाई मानसिंह स्टेडियम, जयपुर", "सवाई मानसिंह स्टेडियम, जयपूर"),
        it3("polo", "Rambagh Polo Ground, Jaipur", "रामबाग पोलो ग्राउंड, जयपुर", "रामबाग पोलो मैदान, जयपूर"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic, Paralympic and Asian Games medallists from Rajasthan (official list)", "राजस्थान के ओलंपिक, पैरालंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "राजस्थानचे ऑलिम्पिक, पॅरालिंपिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Rajasthan State Sports Council.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("prithviraj", ("Prithviraj Chauhan", "पृथ्वीराज चौहान", "पृथ्वीराज चौहान"), ("Chauhan king of Ajmer and Delhi who fought at Tarain (1191–92).", "अजमेर और दिल्ली के चौहान राजा, जिन्होंने तराइन (1191–92) में युद्ध किया।", "अजमेर व दिल्लीचे चौहान राजे, जे तराईन (1191–92) येथे लढले."), ("History", "इतिहास", "इतिहास")),
        person("kumbha", ("Rana Kumbha", "राणा कुंभा", "राणा कुंभा"), ("15th-century ruler of Mewar who built Kumbhalgarh and the Vijay Stambh.", "15वीं सदी के मेवाड़ शासक, जिन्होंने कुंभलगढ़ और विजय स्तंभ बनवाए।", "पंधराव्या शतकातील मेवाडचे शासक, ज्यांनी कुंभलगड व विजयस्तंभ बांधले."), ("History", "इतिहास", "इतिहास")),
        person("pratap", ("Maharana Pratap", "महाराणा प्रताप", "महाराणा प्रताप"), ("Ruler of Mewar who fought Akbar's army at Haldighati (1576).", "मेवाड़ के शासक, जिन्होंने हल्दीघाटी (1576) में अकबर की सेना से युद्ध किया।", "मेवाडचे शासक, जे हळदीघाटी (1576) येथे अकबराच्या सैन्याशी लढले."), ("History", "इतिहास", "इतिहास")),
        person("meera", ("Meera Bai", "मीराबाई", "मीराबाई"), ("16th-century poet-saint devoted to Krishna.", "कृष्ण भक्त 16वीं सदी की संत-कवयित्री।", "कृष्णभक्त सोळाव्या शतकातील संतकवयित्री."), ("Literature", "साहित्य", "साहित्य")),
        person("jaisingh", ("Sawai Jai Singh II", "सवाई जयसिंह द्वितीय", "सवाई जयसिंह दुसरे"), ("Founded Jaipur and built Jantar Mantar observatories.", "जयपुर बसाया और जंतर मंतर वेधशालाएँ बनवाईं।", "जयपूर वसवले व जंतर मंतर वेधशाळा बांधल्या."), ("Science, history", "विज्ञान, इतिहास", "विज्ञान, इतिहास")),
        person("amrita", ("Amrita Devi Bishnoi", "अमृता देवी बिश्नोई", "अमृता देवी बिश्नोई"), ("Gave her life with hundreds of villagers at Khejarli (1730) to protect khejri trees.", "खेजड़ी के पेड़ों की रक्षा के लिए खेजड़ली (1730) में सैकड़ों ग्रामीणों के साथ प्राण दिए।", "खेजडीच्या झाडांच्या रक्षणासाठी खेजडली (1730) येथे शेकडो ग्रामस्थांसह प्राण दिले."), ("Environment", "पर्यावरण", "पर्यावरण")),
        person("shekhawat", ("Bhairon Singh Shekhawat", "भैरों सिंह शेखावत", "भैरोसिंह शेखावत"), ("Three-time Chief Minister and Vice-President of India (2002–07).", "तीन बार मुख्यमंत्री और भारत के उपराष्ट्रपति (2002–07)।", "तीनदा मुख्यमंत्री व भारताचे उपराष्ट्रपती (2002–07)."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("kothari", ("Komal Kothari", "कोमल कोठारी", "कोमल कोठारी"), ("Folklorist who documented the music and oral traditions of Rajasthan.", "लोकविद, जिन्होंने राजस्थान के संगीत और मौखिक परंपराओं का दस्तावेज़ीकरण किया।", "लोकसाहित्य अभ्यासक, ज्यांनी राजस्थानचे संगीत व मौखिक परंपरांचे दस्तऐवजीकरण केले."), ("Culture", "संस्कृति", "संस्कृती")),
        person("gavri", ("Gavri Devi", "गवरी देवी", "गवरी देवी"), ("Celebrated singer of the Maand style of Rajasthani folk music.", "राजस्थानी लोक संगीत की मांड शैली की प्रसिद्ध गायिका।", "राजस्थानी लोकसंगीतातील मांड शैलीच्या प्रसिद्ध गायिका."), ("Music", "संगीत", "संगीत")),
        person("avani", ("Avani Lekhara", "अवनि लेखरा", "अवनी लेखरा"), ("Shooter; Paralympic gold medallist at Tokyo 2020 and Paris 2024.", "निशानेबाज़; टोक्यो 2020 और पेरिस 2024 में पैरालंपिक स्वर्ण पदक विजेता।", "नेमबाज; टोकियो 2020 व पॅरिस 2024 मध्ये पॅरालिंपिक सुवर्णपदक विजेत्या."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Marwari merchants from Shekhawati and Marwar spread across India from the 18th and 19th centuries, founding trading and industrial houses in Kolkata, Mumbai, Assam, Hyderabad and the south; many of India's best-known business families trace their roots to small Rajasthan towns, where their painted havelis still stand. Today large numbers of workers from Shekhawati, Nagaur and other districts go to the Gulf countries, and Rajasthani communities are active in the United States, the United Kingdom and East Africa.",
        "शेखावाटी और मारवाड़ के मारवाड़ी व्यापारी 18वीं और 19वीं सदी से पूरे भारत में फैले और कोलकाता, मुंबई, असम, हैदराबाद और दक्षिण में व्यापारिक और औद्योगिक घराने बनाए; भारत के कई सबसे प्रसिद्ध व्यावसायिक परिवार राजस्थान के छोटे कस्बों से जुड़े हैं, जहाँ उनकी चित्रित हवेलियाँ आज भी खड़ी हैं। आज शेखावाटी, नागौर और अन्य ज़िलों से बड़ी संख्या में श्रमिक खाड़ी देशों में जाते हैं, और राजस्थानी समुदाय अमेरिका, ब्रिटेन और पूर्वी अफ़्रीका में सक्रिय हैं।",
        "शेखावटी व मारवाडमधील मारवाडी व्यापारी अठराव्या-एकोणिसाव्या शतकापासून भारतभर पसरले आणि त्यांनी कोलकाता, मुंबई, आसाम, हैदराबाद व दक्षिणेत व्यापारी व औद्योगिक घराणी उभारली; भारतातील अनेक प्रसिद्ध व्यावसायिक कुटुंबांची मुळे राजस्थानच्या लहान गावांत आहेत, जिथे त्यांच्या रंगवलेल्या हवेल्या आजही उभ्या आहेत. आज शेखावटी, नागौर व इतर जिल्ह्यांतून मोठ्या संख्येने कामगार आखाती देशांत जातात, आणि राजस्थानी समुदाय अमेरिका, ब्रिटन व पूर्व आफ्रिकेत सक्रिय आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants and internal migrants", "प्रवासियों और आंतरिक प्रवासियों की संख्या", "परदेशी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; MEA."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Rajasthan portal", "राजस्थान सरकार पोर्टल", "राजस्थान शासन संकेतस्थळ", url="https://rajasthan.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Rajasthan Tourism", "राजस्थान पर्यटन", "राजस्थान पर्यटन", url="https://www.tourism.rajasthan.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Jaipur", "जयपुर", "जयपूर"), "0141"], [L("Jodhpur", "जोधपुर", "जोधपूर"), "0291"], [L("Udaipur", "उदयपुर", "उदयपूर"), "0294"],
           [L("Kota", "कोटा", "कोटा"), "0744"], [L("Bikaner", "बीकानेर", "बिकानेर"), "0151"], [L("Ajmer", "अजमेर", "अजमेर"), "0145"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("State e-services portal — verified link", "राज्य ई-सेवा पोर्टल — सत्यापित लिंक", "राज्य ई-सेवा संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "SSO / e-Mitra portal of the State."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("largest", ("Rajasthan is India's largest State by area — about a tenth of the country.", "राजस्थान क्षेत्रफल में भारत का सबसे बड़ा राज्य है — देश का लगभग दसवाँ भाग।", "राजस्थान हे क्षेत्रफळाने भारतातील सर्वांत मोठे राज्य आहे — देशाचा सुमारे दहावा भाग."), LS_FOREST, "fsi"),
        triv("unesco", ("Six of its hill forts are inscribed together as one UNESCO World Heritage Site.", "इसके छह पहाड़ी क़िले मिलकर एक यूनेस्को विश्व धरोहर स्थल के रूप में अंकित हैं।", "त्याचे सहा डोंगरी किल्ले मिळून एक युनेस्को जागतिक वारसा स्थळ म्हणून नोंदलेले आहेत."), UNESCO, "unesco-whc"),
        triv("makrana", ("Makrana marble, a registered GI, was used to build the Taj Mahal.", "पंजीकृत जीआई मकराना संगमरमर से ताजमहल बना।", "नोंदणीकृत जीआय मकराना संगमरवराचा वापर ताजमहाल बांधण्यासाठी झाला."), GI_PDF, "gi-registry"),
        triv("sambhar", ("Sambhar is India's largest inland saline lake and a Ramsar site.", "सांभर भारत की सबसे बड़ी अंतर्देशीय खारी झील और रामसर स्थल है।", "सांभर हे भारतातील सर्वांत मोठे अंतर्गत खारे सरोवर व रामसर स्थळ आहे."), RAMSAR, "indian-wetlands"),
        triv("khejarli", ("The Khejarli sacrifice of 1730, when Bishnoi villagers died protecting trees, is remembered as an early environmental movement.", "1730 का खेजड़ली बलिदान, जब बिश्नोई ग्रामीणों ने पेड़ों की रक्षा में प्राण दिए, एक आरंभिक पर्यावरण आंदोलन के रूप में याद किया जाता है।", "1730 चे खेजडली बलिदान, जेव्हा बिश्नोई ग्रामस्थांनी झाडांच्या रक्षणासाठी प्राण दिले, ही सुरुवातीची पर्यावरण चळवळ म्हणून स्मरणात आहे.")),
        triv("ls", ("The State elects 25 members to the Lok Sabha.", "राज्य से लोकसभा के 25 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 25 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("rj mod3 ok")
