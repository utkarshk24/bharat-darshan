"""Karnataka modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-KA"
KGIS = "https://kgis.ksrsac.in/kag/"
ka = read("regions/IN-KA.json")["metrics"]; ind = read("india.json")["metrics"]

RAMSAR_KA = [
    ("Ranganathittu Bird Sanctuary", "रंगनथिट्टु पक्षी अभयारण्य", "रंगनथिट्टू पक्षी अभयारण्य", "15 Feb 2022", "518"),
    ("Aghanashini Estuary", "अघनाशिनी मुहाना", "अघनाशिनी खाडी", "14 Feb 2023", "4,801"),
    ("Magadi Kere Conservation Reserve", "मागडी केरे संरक्षण रिज़र्व", "मागडी केरे संवर्धन राखीव क्षेत्र", "14 Feb 2023", "54.38"),
    ("Ankasamudra Bird Conservation Reserve", "अंकसमुद्र पक्षी संरक्षण रिज़र्व", "अंकसमुद्र पक्षी संवर्धन राखीव क्षेत्र", "10 Mar 2023", "98.76"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About a fifth of Karnataka is forest — 20.5% in ISFR 2023 — most of it in the Western Ghats and the hills of the south. The State has the largest wild Asian elephant population in India and one of the largest tiger populations, protected in a connected belt of reserves: Bandipur and Nagarahole on the border with Tamil Nadu and Keralam, BRT Hills, Bhadra and Kali (Dandeli–Anshi). The Ghats' evergreen forests hold lion-tailed macaques, Malabar giant squirrels, hornbills and many endemic frogs and plants, and the river Kaveri is home to the mahseer.\n\nKarnataka has four Ramsar wetlands — Ranganathittu, a riverine bird sanctuary near Srirangapatna, the Aghanashini estuary on the coast, and the Magadi Kere and Ankasamudra tanks in the north, which host bar-headed geese, painted storks and other water-birds.",
        "कर्नाटक का लगभग पाँचवाँ हिस्सा वन है — आईएसएफ़आर 2023 में 20.5% — जिसका अधिकांश पश्चिमी घाट और दक्षिण की पहाड़ियों में है। राज्य में भारत की सबसे बड़ी जंगली एशियाई हाथी आबादी और बाघों की सबसे बड़ी आबादियों में से एक है, जो जुड़े हुए अभयारण्यों की पट्टी में संरक्षित है: तमिलनाडु और केरलम की सीमा पर बांदीपुर और नागरहोले, बीआरटी पहाड़ियाँ, भद्रा और काली (दांडेली–अंशी)। घाटों के सदाबहार वनों में शेरपूँछ मकाक, मालाबार विशाल गिलहरी, धनेश और अनेक स्थानिक मेंढक व पौधे हैं, और कावेरी नदी में महसीर मछली रहती है।\n\nकर्नाटक में चार रामसर आर्द्रभूमियाँ हैं — श्रीरंगपट्टण के पास नदी किनारे का पक्षी अभयारण्य रंगनथिट्टु, तट पर अघनाशिनी मुहाना, और उत्तर में मागडी केरे व अंकसमुद्र तालाब, जहाँ बार-हेडेड हंस, पेंटेड स्टॉर्क और अन्य जलपक्षी आते हैं।",
        "कर्नाटकचा सुमारे पाचवा भाग वनाच्छादित आहे — आयएसएफआर 2023 नुसार 20.5% — त्यातील बहुतांश पश्चिम घाट व दक्षिणेकडील डोंगरांत आहे. राज्यात भारतातील सर्वांत मोठी वन्य आशियाई हत्तींची संख्या आणि वाघांच्या सर्वांत मोठ्या संख्यांपैकी एक आहे, जी परस्परजोडलेल्या अभयारण्यांच्या पट्ट्यात संरक्षित आहे: तमिळनाडू व केरळमच्या सीमेवरील बांदीपूर व नागरहोळे, बीआरटी टेकड्या, भद्रा आणि काळी (दांडेली–अंशी). घाटांच्या सदाहरित जंगलांत सिंहपुच्छ माकड, मलबारी शेकरू, धनेश आणि अनेक प्रदेशनिष्ठ बेडूक व वनस्पती आहेत, आणि कावेरी नदीत महसीर मासा आढळतो.\n\nकर्नाटकात चार रामसर पाणथळ स्थळे आहेत — श्रीरंगपट्टणजवळील नदीकाठचे पक्षी अभयारण्य रंगनथिट्टू, किनारपट्टीवरील अघनाशिनी खाडी, आणि उत्तरेकडील मागडी केरे व अंकसमुद्र तलाव, जिथे पट्टकादंब, चित्रबलाक व इतर पाणपक्षी येतात."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(39254.27, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(39106.57, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), ka["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(4, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026 (India total 99)."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_KA], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026.", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी.")),
    lst("protected", [
        it3("bandipur", "Bandipur Tiger Reserve", "बांदीपुर बाघ अभयारण्य", "बांदीपूर व्याघ्र प्रकल्प", m=("Chamarajanagar–Mysuru", "चामराजनगर–मैसूरु", "चामराजनगर–म्हैसूरु")),
        it3("nagarahole", "Nagarahole Tiger Reserve", "नागरहोले बाघ अभयारण्य", "नागरहोळे व्याघ्र प्रकल्प", m=("Kodagu–Mysuru", "कोडगु–मैसूरु", "कोडगू–म्हैसूरु")),
        it3("bhadra", "Bhadra Tiger Reserve", "भद्रा बाघ अभयारण्य", "भद्रा व्याघ्र प्रकल्प", m=("Chikkamagaluru", "चिक्कमगलूरु", "चिक्कमगळूरु")),
        it3("kali", "Kali Tiger Reserve (Dandeli–Anshi)", "काली बाघ अभयारण्य (दांडेली–अंशी)", "काळी व्याघ्र प्रकल्प (दांडेली–अंशी)", m=("Uttara Kannada", "उत्तर कन्नड़", "उत्तर कन्नड")),
        it3("brt", "BRT Tiger Reserve", "बीआरटी बाघ अभयारण्य", "बीआरटी व्याघ्र प्रकल्प", m=("Biligiri Rangaswamy Temple hills", "बिलिगिरि रंगस्वामी मंदिर पहाड़ियाँ", "बिळिगिरी रंगस्वामी मंदिर टेकड्या")),
        it3("kudremukh", "Kudremukh National Park", "कुद्रेमुख राष्ट्रीय उद्यान", "कुद्रेमुख राष्ट्रीय उद्यान", m=("Shola grasslands", "शोला घासभूमि", "शोला गवताळ प्रदेश")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("elephant", "Asian elephant", "एशियाई हाथी", "आशियाई हत्ती"), it3("tiger", "Bengal tiger", "बंगाल बाघ", "पट्टेरी वाघ"),
        it3("ltm", "Lion-tailed macaque", "शेरपूँछ मकाक", "सिंहपुच्छ माकड"), it3("hornbill", "Great hornbill", "महा धनेश", "महाधनेश"),
        it3("roller", "Indian roller (State bird)", "नीलकंठ (राज्य पक्षी)", "नीलकंठ (राज्यपक्षी)"), it3("mahseer", "Mahseer", "महसीर", "महसीर"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger and elephant population estimates", "बाघ और हाथी आबादी के अनुमान", "वाघ व हत्तींच्या संख्येचे अंदाज"), "ntca", "NTCA All India Tiger Estimation; MoEFCC elephant census."),
        (L("National parks and sanctuaries (count, area)", "राष्ट्रीय उद्यान और अभयारण्य (संख्या, क्षेत्रफल)", "राष्ट्रीय उद्याने व अभयारण्ये (संख्या, क्षेत्र)"), "moefcc", "ENVIS / WII database."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Water is one of Karnataka's biggest issues. Large parts of the north and the interior plateau are dry, and the State has a long history of tank irrigation — thousands of village keres built over centuries. Big dams on the Krishna (Almatti, Narayanpur), Tungabhadra and Kaveri (Krishna Raja Sagara, Kabini, Harangi) irrigate the plains and supply cities. Sharing the Kaveri with Tamil Nadu, Keralam and Puducherry, and the Krishna with Maharashtra, Telangana and Andhra Pradesh, has been the subject of long inter-State disputes settled by tribunals and the Supreme Court. Bengaluru draws most of its drinking water from the Kaveri, about 100 km away, and relies heavily on groundwater; its lakes have shrunk and many have been polluted.",
        "पानी कर्नाटक के सबसे बड़े मुद्दों में से है। उत्तर और भीतरी पठार के बड़े हिस्से सूखे हैं, और राज्य में तालाब सिंचाई का लंबा इतिहास है — सदियों में बने हज़ारों गाँव के केरे। कृष्णा (अलमट्टी, नारायणपुर), तुंगभद्रा और कावेरी (कृष्णराज सागर, काबिनी, हारंगी) पर बड़े बाँध मैदानों को सींचते और शहरों को पानी देते हैं। कावेरी का तमिलनाडु, केरलम और पुदुच्चेरी के साथ, और कृष्णा का महाराष्ट्र, तेलंगाना और आंध्र प्रदेश के साथ बँटवारा लंबे अंतरराज्यीय विवादों का विषय रहा है, जिन्हें न्यायाधिकरणों और सर्वोच्च न्यायालय ने सुलझाया। बेंगलूरु अपना अधिकांश पेयजल लगभग 100 किमी दूर कावेरी से लेता है और भूजल पर बहुत निर्भर है; इसकी झीलें सिकुड़ी हैं और कई प्रदूषित हुई हैं।",
        "पाणी हा कर्नाटकातील सर्वांत मोठ्या प्रश्नांपैकी एक आहे. उत्तर भाग व अंतर्गत पठाराचा मोठा भाग कोरडा आहे, आणि राज्याला तलाव-सिंचनाचा दीर्घ इतिहास आहे — शतकानुशतके बांधलेले हजारो गावतलाव (केरे). कृष्णा (आलमट्टी, नारायणपूर), तुंगभद्रा व कावेरी (कृष्णराजसागर, काबिनी, हारंगी) वरील मोठी धरणे मैदाने सिंचतात आणि शहरांना पाणी पुरवतात. कावेरीचे तमिळनाडू, केरळम व पुदुच्चेरीसोबत, आणि कृष्णेचे महाराष्ट्र, तेलंगणा व आंध्र प्रदेशसोबत वाटप हा दीर्घ आंतरराज्यीय वादांचा विषय राहिला असून न्यायाधिकरणे व सर्वोच्च न्यायालयाने ते निकाली काढले. बंगळूरु आपले बहुतांश पिण्याचे पाणी सुमारे 100 किमी दूरच्या कावेरीतून घेते आणि भूजलावर मोठ्या प्रमाणात अवलंबून आहे; त्याचे तलाव आकसले असून अनेक प्रदूषित झाले आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Net irrigated area and sources", "शुद्ध सिंचित क्षेत्र और स्रोत", "निव्वळ सिंचित क्षेत्र व स्रोत"), "ka-des", "Land use statistics."),
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Drought is Karnataka's most frequent hazard: many northern and interior districts are declared drought-hit in years of weak monsoon. In heavy-rain years the opposite happens — floods along the Krishna and its tributaries in the north, and landslides in Kodagu, Chikkamagaluru and on the Ghat roads, as in 2018 and 2019. The coast is exposed to cyclones from the Arabian Sea and rough seas in the monsoon. Bengaluru faces urban flooding in intense storms.\n\nFor visitors, the main precautions are checking ghat-road and weather advisories in the monsoon, staying out of the sea when red flags are up, and avoiding forest roads after dark, when elephants cross.",
        "सूखा कर्नाटक का सबसे आम ख़तरा है: कमज़ोर मानसून वाले वर्षों में कई उत्तरी और भीतरी ज़िले सूखा-ग्रस्त घोषित होते हैं। भारी वर्षा वाले वर्षों में इसका उलटा होता है — उत्तर में कृष्णा और उसकी सहायक नदियों में बाढ़, और कोडगु, चिक्कमगलूरु व घाट मार्गों पर भूस्खलन, जैसा 2018 और 2019 में हुआ। तट अरब सागर के चक्रवातों और मानसून में उग्र समुद्र के प्रति संवेदनशील है। तेज़ तूफ़ानों में बेंगलूरु में शहरी बाढ़ आती है।\n\nपर्यटकों के लिए मुख्य सावधानियाँ हैं: मानसून में घाट मार्ग और मौसम चेतावनियाँ देखना, लाल झंडे लगे होने पर समुद्र से दूर रहना, और अँधेरे के बाद वन मार्गों से बचना, जब हाथी सड़क पार करते हैं।",
        "दुष्काळ हा कर्नाटकातील सर्वांत वारंवार येणारा धोका आहे: कमकुवत मान्सूनच्या वर्षांत अनेक उत्तर व अंतर्गत जिल्हे दुष्काळग्रस्त घोषित होतात. मुसळधार पावसाच्या वर्षांत उलट घडते — उत्तरेकडे कृष्णा व तिच्या उपनद्यांना पूर, आणि कोडगू, चिक्कमगळूरु व घाटरस्त्यांवर दरडी कोसळणे, जसे 2018 व 2019 मध्ये झाले. किनारपट्टी अरबी समुद्रातील चक्रीवादळे व पावसाळ्यातील खवळलेल्या समुद्राला उघडी आहे. तीव्र वादळांत बंगळूरुमध्ये नागरी पूर येतात.\n\nपर्यटकांसाठी मुख्य काळजी: पावसाळ्यात घाटरस्ते व हवामान इशारे तपासणे, लाल झेंडे असताना समुद्रात न उतरणे, आणि अंधार पडल्यावर जंगलातील रस्ते टाळणे, जेव्हा हत्ती रस्ता ओलांडतात."),
        conf="Editorial"),
    emergency_table(("Karnataka", "कर्नाटक", "कर्नाटक")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Karnataka State Disaster Management Authority — verified link", "कर्नाटक राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "कर्नाटक राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official KSDMA / KSNDMC address."),
        (L("Drought-declared taluks by year", "वर्षवार सूखा-घोषित तालुक", "वर्षनिहाय दुष्काळग्रस्त तालुके"), "india-gov", "Revenue Department drought notifications."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Karnataka has 45 registered Geographical Indications in the GI Registry's list as on 31 December 2025, and shares four more — Malabar pepper, Monsooned Malabar Arabica and Robusta coffee, and Kolhapuri chappals — with neighbouring States. Mysore silk was among the earliest Indian GI applications (2004), and the State has a cluster of 'Mysore' GIs: sandalwood oil, sandal soap, agarbathi, rosewood inlay, traditional paintings and Ganjifa cards. Other names include Channapatna toys, Bidriware, Ilkal and Molakalmuru saris, Kasuti embroidery, Dharwad pedha, Byadagi chilli, the coffees of Coorg, Chikmagalur and Bababudangiri, and the jasmines of Mysuru, Udupi and Hadagali.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में कर्नाटक के 45 पंजीकृत भौगोलिक संकेतक हैं, और चार और — मालाबार काली मिर्च, मॉनसून्ड मालाबार अरेबिका और रोबस्टा कॉफ़ी, और कोल्हापुरी चप्पल — पड़ोसी राज्यों के साथ साझा हैं। मैसूर सिल्क भारत के सबसे शुरुआती जीआई आवेदनों में था (2004), और राज्य के कई 'मैसूर' जीआई हैं: चंदन तेल, चंदन साबुन, अगरबत्ती, शीशम पच्चीकारी, पारंपरिक चित्रकला और गंजीफ़ा पत्ते। अन्य नामों में चन्नपट्टण के खिलौने, बिदरी शिल्प, इलकल और मोलकालमुरु साड़ियाँ, कसूती कढ़ाई, धारवाड़ पेड़ा, ब्याडगी मिर्च, कुर्ग, चिकमगलूर और बाबाबुदनगिरि की कॉफ़ी, और मैसूरु, उडुपी व हडगली की चमेली शामिल हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत कर्नाटकची 45 नोंदणीकृत भौगोलिक मानांकने आहेत, आणि आणखी चार — मलबारी मिरी, मॉन्सून्ड मलबार अरेबिका व रोबस्टा कॉफी, आणि कोल्हापुरी चप्पल — शेजारी राज्यांसोबत सामायिक आहेत. म्हैसूर सिल्क हा भारतातील सर्वांत सुरुवातीच्या जीआय अर्जांपैकी एक होता (2004), आणि राज्याची अनेक 'म्हैसूर' मानांकने आहेत: चंदनाचे तेल, चंदनी साबण, अगरबत्ती, शिसवी जडावकाम, पारंपरिक चित्रकला आणि गंजिफा पत्ते. इतर नावांत चन्नपट्टणची खेळणी, बिदरी कला, इळकल व मोळकाल्मुरू साड्या, कसूती भरतकाम, धारवाड पेढा, ब्याडगी मिरची, कूर्ग, चिकमगळूर व बाबाबुदनगिरीची कॉफी, आणि म्हैसूरु, उडुपी व हडगलीचा मोगरा यांचा समावेश आहे."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Karnataka's attractions cover a wide range: the World Heritage ruins of Hampi and the temples of Badami, Aihole, Pattadakal, Belur and Halebidu; Mysuru's palace and Dasara; the coffee hills of Kodagu and Chikkamagaluru; wildlife safaris at Bandipur, Nagarahole and Kabini; the beaches and temple towns of the coast — Gokarna, Murudeshwar, Udupi; Jog Falls; and Shravanabelagola, where the 57-foot statue of Gommateshwara draws Jain pilgrims for the Mahamastakabhisheka every twelve years.",
        "कर्नाटक के आकर्षण बहुत विविध हैं: हम्पी के विश्व धरोहर खंडहर और बादामी, ऐहोले, पट्टदकल, बेलूर व हलेबीडु के मंदिर; मैसूरु का महल और दशहरा; कोडगु और चिक्कमगलूरु की कॉफ़ी पहाड़ियाँ; बांदीपुर, नागरहोले और काबिनी में वन्यजीव सफ़ारी; तट के समुद्र तट और मंदिर नगर — गोकर्ण, मुरुडेश्वर, उडुपी; जोग जलप्रपात; और श्रवणबेलगोला, जहाँ गोम्मटेश्वर की 57 फ़ुट ऊँची प्रतिमा का हर बारह वर्ष में होने वाला महामस्तकाभिषेक जैन तीर्थयात्रियों को आकर्षित करता है।",
        "कर्नाटकातील आकर्षणे अतिशय वैविध्यपूर्ण आहेत: हंपीचे जागतिक वारसा अवशेष आणि बदामी, ऐहोळे, पट्टदकल, बेलूर व हळेबीडूची मंदिरे; म्हैसूरुचा राजवाडा व दसरा; कोडगू व चिक्कमगळूरुचे कॉफीचे डोंगर; बांदीपूर, नागरहोळे व काबिनी येथील वन्यजीव सफारी; किनारपट्टीवरील समुद्रकिनारे व मंदिरनगरी — गोकर्ण, मुरुडेश्वर, उडुपी; जोग धबधबा; आणि श्रवणबेळगोळ, जिथे गोमटेश्वराच्या 57 फूट उंच मूर्तीचा दर बारा वर्षांनी होणारा महामस्तकाभिषेक जैन यात्रेकरूंना आकर्षित करतो."),
        conf="Editorial"),
    lst("places", [
        it3("hampi", "Hampi", "हम्पी", "हंपी", m=("UNESCO heritage", "यूनेस्को धरोहर", "युनेस्को वारसा")),
        it3("mysuru", "Mysuru Palace and Chamundi Hill", "मैसूरु महल और चामुंडी पहाड़ी", "म्हैसूरु राजवाडा व चामुंडी टेकडी", m=("Heritage", "धरोहर", "वारसा")),
        it3("belur", "Belur and Halebidu", "बेलूर और हलेबीडु", "बेलूर व हळेबीडू", m=("UNESCO heritage", "यूनेस्को धरोहर", "युनेस्को वारसा")),
        it3("badami", "Badami, Aihole and Pattadakal", "बादामी, ऐहोले और पट्टदकल", "बदामी, ऐहोळे व पट्टदकल", m=("Chalukya temples", "चालुक्य मंदिर", "चालुक्य मंदिरे")),
        it3("kodagu", "Kodagu (Coorg)", "कोडगु (कुर्ग)", "कोडगू (कूर्ग)", m=("Hills and coffee", "पहाड़ियाँ और कॉफ़ी", "डोंगर व कॉफी")),
        it3("kabini", "Kabini and Nagarahole", "काबिनी और नागरहोले", "काबिनी व नागरहोळे", m=("Wildlife", "वन्यजीव", "वन्यजीव")),
        it3("gokarna", "Gokarna and Murudeshwar", "गोकर्ण और मुरुडेश्वर", "गोकर्ण व मुरुडेश्वर", m=("Beaches, temples", "समुद्र तट, मंदिर", "समुद्रकिनारे, मंदिरे")),
        it3("jog", "Jog Falls", "जोग जलप्रपात", "जोग धबधबा", m=("Best in monsoon", "मानसून में सबसे सुंदर", "पावसाळ्यात सर्वोत्तम")),
        it3("shravanabelagola", "Shravanabelagola", "श्रवणबेलगोला", "श्रवणबेळगोळ", m=("Jain pilgrimage", "जैन तीर्थ", "जैन तीर्थक्षेत्र")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Mysuru: palace, Chamundi Hill, Srirangapatna and Ranganathittu.", "मैसूरु: महल, चामुंडी पहाड़ी, श्रीरंगपट्टण और रंगनथिट्टु।", "म्हैसूरु: राजवाडा, चामुंडी टेकडी, श्रीरंगपट्टण व रंगनथिट्टू.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Hampi and the Tungabhadra, with a day trip to Badami or Pattadakal.", "हम्पी और तुंगभद्रा, बादामी या पट्टदकल की एक दिन की यात्रा के साथ।", "हंपी व तुंगभद्रा, बदामी किंवा पट्टदकलच्या एकदिवसीय सहलीसह.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Bengaluru, Mysuru and Kodagu, or Belur–Halebidu–Chikkamagaluru.", "बेंगलूरु, मैसूरु और कोडगु, या बेलूर–हलेबीडु–चिक्कमगलूरु।", "बंगळूरु, म्हैसूरु व कोडगू, किंवा बेलूर–हळेबीडू–चिक्कमगळूरु.")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Coastal Karnataka from Mangaluru to Udupi, Murudeshwar, Gokarna and Jog Falls.", "मंगलूरु से उडुपी, मुरुडेश्वर, गोकर्ण और जोग जलप्रपात तक तटीय कर्नाटक।", "मंगळूरुपासून उडुपी, मुरुडेश्वर, गोकर्ण व जोग धबधब्यापर्यंत किनारी कर्नाटक.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("kst", "Karnataka Tourism (official)", "कर्नाटक पर्यटन (आधिकारिक)", "कर्नाटक पर्यटन (अधिकृत)", url="https://karnatakatourism.org", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by calendar year", "कैलेंडर वर्ष के अनुसार घरेलू और विदेशी पर्यटक यात्राएँ", "कॅलेंडर वर्षानुसार देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table; the Economic Survey of Karnataka 2025-26 gives only a part-year figure, so it is not shown."),
        (L("Earnings from tourism", "पर्यटन से आय", "पर्यटनातून उत्पन्न"), "tourism", "State tourism department."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Bagalkot", "बागलकोट", "बागलकोट"), ("Ballari", "बल्लारी", "बळ्ळारी"), ("Belagavi", "बेलगावी", "बेळगावी"), ("Bengaluru Rural", "बेंगलूरु ग्रामीण", "बंगळूरु ग्रामीण"),
    ("Bengaluru Urban", "बेंगलूरु शहरी", "बंगळूरु शहरी"), ("Bidar", "बीदर", "बीदर"), ("Chamarajanagar", "चामराजनगर", "चामराजनगर"), ("Chikkaballapura", "चिक्कबल्लापुर", "चिक्कबळ्ळापूर"),
    ("Chikkamagaluru", "चिक्कमगलूरु", "चिक्कमगळूरु"), ("Chitradurga", "चित्रदुर्ग", "चित्रदुर्ग"), ("Dakshina Kannada", "दक्षिण कन्नड़", "दक्षिण कन्नड"), ("Davanagere", "दावणगेरे", "दावणगेरे"),
    ("Dharwad", "धारवाड़", "धारवाड"), ("Gadag", "गदग", "गदग"), ("Hassan", "हासन", "हासन"), ("Haveri", "हावेरी", "हावेरी"),
    ("Kalaburagi", "कलबुर्गी", "कलबुर्गी"), ("Kodagu", "कोडगु", "कोडगू"), ("Kolar", "कोलार", "कोलार"), ("Koppal", "कोप्पल", "कोप्पळ"),
    ("Mandya", "मंड्या", "मंड्या"), ("Mysuru", "मैसूरु", "म्हैसूरु"), ("Raichur", "रायचूर", "रायचूर"), ("Ramanagara", "रामनगर", "रामनगर"),
    ("Shivamogga", "शिवमोग्गा", "शिवमोग्गा"), ("Tumakuru", "तुमकूरु", "तुमकूरु"), ("Udupi", "उडुपी", "उडुपी"), ("Uttara Kannada", "उत्तर कन्नड़", "उत्तर कन्नड"),
    ("Vijayanagara", "विजयनगर", "विजयनगर"), ("Vijayapura", "विजयपुरा", "विजयपुरा"), ("Yadgir", "यादगीर", "यादगीर"),
]
assert len(DISTRICTS) == 31, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("bengaluru", ("Bengaluru", "बेंगलूरु", "बंगळूरु"), ("State capital; India's technology and start-up hub; gardens, research institutes, metro.", "राज्य की राजधानी; भारत का प्रौद्योगिकी और स्टार्टअप केंद्र; उद्यान, शोध संस्थान, मेट्रो।", "राज्याची राजधानी; भारताचे तंत्रज्ञान व स्टार्टअप केंद्र; उद्याने, संशोधन संस्था, मेट्रो."), ("Capital", "राजधानी", "राजधानी")),
        city("mysuru", ("Mysuru", "मैसूरु", "म्हैसूरु"), ("Former royal capital; palace, Dasara, silk and sandalwood.", "पूर्व राजधानी; महल, दशहरा, रेशम और चंदन।", "पूर्वीची राजधानी; राजवाडा, दसरा, रेशीम व चंदन."), ("Heritage", "धरोहर", "वारसा")),
        city("hubballi", ("Hubballi–Dharwad", "हुब्बल्ली–धारवाड़", "हुबळी–धारवाड"), ("Twin cities; railway zone headquarters, trade, universities and music.", "जुड़वाँ शहर; रेलवे ज़ोन मुख्यालय, व्यापार, विश्वविद्यालय और संगीत।", "जुळी शहरे; रेल्वे विभागीय मुख्यालय, व्यापार, विद्यापीठे व संगीत."), ("North Karnataka", "उत्तर कर्नाटक", "उत्तर कर्नाटक")),
        city("mangaluru", ("Mangaluru", "मंगलूरु", "मंगळूरु"), ("Port city; refinery, banking, education and coastal cuisine.", "बंदरगाह नगर; रिफ़ाइनरी, बैंकिंग, शिक्षा और तटीय व्यंजन।", "बंदराचे शहर; तेलशुद्धीकरण, बँकिंग, शिक्षण व किनारी खाद्यपदार्थ."), ("Coast", "तट", "किनारपट्टी")),
        city("belagavi", ("Belagavi", "बेलगावी", "बेळगावी"), ("Foundries, aerospace parts; Suvarna Vidhana Soudha.", "ढलाईघर, एयरोस्पेस पुर्ज़े; सुवर्ण विधान सौध।", "ओतकाम कारखाने, एरोस्पेस भाग; सुवर्ण विधानसौध."), ("Industry", "उद्योग", "उद्योग")),
        city("kalaburagi", ("Kalaburagi", "कलबुर्गी", "कलबुर्गी"), ("Bahmani-era monuments; tur dal; High Court bench.", "बहमनी काल के स्मारक; अरहर दाल; उच्च न्यायालय खंडपीठ।", "बहमनीकालीन स्मारके; तूरडाळ; उच्च न्यायालय खंडपीठ."), ("Kalyana Karnataka", "कल्याण कर्नाटक", "कल्याण कर्नाटक")),
        city("vijayapura", ("Vijayapura", "विजयपुरा", "विजयपुरा"), ("Adil Shahi capital; Gol Gumbaz.", "आदिलशाही राजधानी; गोल गुंबज़।", "आदिलशाही राजधानी; गोलघुमट."), ("Heritage", "धरोहर", "वारसा")),
        city("shivamogga", ("Shivamogga", "शिवमोग्गा", "शिवमोग्गा"), ("Gateway to the Malnad and Jog Falls.", "मलनाड और जोग जलप्रपात का प्रवेश द्वार।", "मलनाड व जोग धबधब्याचे प्रवेशद्वार."), ("Malnad", "मलनाड", "मलनाड")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 31 districts (alphabetical)", "31 ज़िले (वर्णानुक्रम)", "31 जिल्हे (वर्णक्रमानुसार)"), src="ka-gis", url=KGIS, conf="Editorial", access=TODAY),
    gaps("g", [
        (L("District populations (Census 2011)", "ज़िलावार जनसंख्या (जनगणना 2011)", "जिल्हानिहाय लोकसंख्या (जनगणना 2011)"), "census", "District Census Handbooks."),
        (L("District names — official list after recent renamings", "ज़िलों के नाम — हाल के नाम-परिवर्तनों के बाद आधिकारिक सूची", "जिल्ह्यांची नावे — अलीकडील नामांतरांनंतरची अधिकृत यादी"), "india-gov", "Revenue Department notification; check Ramanagara's renaming."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Cricket is the most followed sport, and the M. Chinnaswamy Stadium in Bengaluru is one of India's best-known Test and IPL venues. Karnataka has produced many India captains and stars, including Rahul Dravid, Anil Kumble and G. R. Viswanath. The State is also a centre for badminton — Prakash Padukone, India's first All England champion, built his academy in Bengaluru — and for hockey in Kodagu, where the annual Kodava family hockey festival is among the largest field-hockey tournaments in the world. Bengaluru hosts national training centres of the Sports Authority of India and professional football and kabaddi teams.",
        "क्रिकेट सबसे अधिक देखा जाने वाला खेल है, और बेंगलूरु का एम. चिन्नास्वामी स्टेडियम भारत के सबसे प्रसिद्ध टेस्ट और आईपीएल मैदानों में है। कर्नाटक ने राहुल द्रविड़, अनिल कुंबले और जी. आर. विश्वनाथ सहित कई भारतीय कप्तान और सितारे दिए हैं। राज्य बैडमिंटन का भी केंद्र है — भारत के पहले ऑल इंग्लैंड चैंपियन प्रकाश पादुकोण ने बेंगलूरु में अपनी अकादमी बनाई — और कोडगु में हॉकी का, जहाँ वार्षिक कोडव पारिवारिक हॉकी उत्सव दुनिया के सबसे बड़े फ़ील्ड हॉकी टूर्नामेंटों में है। बेंगलूरु में भारतीय खेल प्राधिकरण के राष्ट्रीय प्रशिक्षण केंद्र और पेशेवर फ़ुटबॉल व कबड्डी टीमें हैं।",
        "क्रिकेट हा सर्वाधिक पाहिला जाणारा खेळ आहे, आणि बंगळूरुचे एम. चिन्नास्वामी स्टेडियम भारतातील सर्वांत प्रसिद्ध कसोटी व आयपीएल मैदानांपैकी आहे. कर्नाटकने राहुल द्रविड, अनिल कुंबळे व जी. आर. विश्वनाथ यांच्यासह अनेक भारतीय कर्णधार व तारे दिले आहेत. राज्य बॅडमिंटनचेही केंद्र आहे — भारताचे पहिले ऑल इंग्लंड विजेते प्रकाश पडुकोण यांनी बंगळूरुत आपली अकादमी उभारली — आणि कोडगूमध्ये हॉकीचे, जिथे वार्षिक कोडव कौटुंबिक हॉकी महोत्सव जगातील सर्वांत मोठ्या मैदानी हॉकी स्पर्धांपैकी आहे. बंगळूरुमध्ये भारतीय क्रीडा प्राधिकरणाची राष्ट्रीय प्रशिक्षण केंद्रे आणि व्यावसायिक फुटबॉल व कबड्डी संघ आहेत."),
        conf="Editorial"),
    lst("venues", [
        it3("chinnaswamy", "M. Chinnaswamy Stadium, Bengaluru", "एम. चिन्नास्वामी स्टेडियम, बेंगलूरु", "एम. चिन्नास्वामी स्टेडियम, बंगळूरु"),
        it3("kanteerava", "Sree Kanteerava Stadium, Bengaluru", "श्री कंठीरव स्टेडियम, बेंगलूरु", "श्री कंठीरव स्टेडियम, बंगळूरु"),
        it3("sai", "SAI Southern Centre, Bengaluru", "साई दक्षिणी केंद्र, बेंगलूरु", "साई दक्षिण केंद्र, बंगळूरु"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from Karnataka (official list)", "कर्नाटक के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "कर्नाटकचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Sports Authority of India / State sports department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("basavanna", ("Basavanna", "बसवण्णा", "बसवण्णा"), ("12th-century poet-reformer of Kalyana whose vachanas challenged caste and ritual.", "कल्याण के 12वीं सदी के कवि-सुधारक, जिनके वचनों ने जाति और कर्मकांड को चुनौती दी।", "कल्याणचे बाराव्या शतकातील कवी-सुधारक; त्यांच्या वचनांनी जातिभेद व कर्मकांडाला आव्हान दिले."), ("Reform", "सुधार", "सुधारणा")),
        person("akka", ("Akka Mahadevi", "अक्क महादेवी", "अक्कमहादेवी"), ("12th-century vachana poet and mystic.", "12वीं सदी की वचन कवयित्री और संत।", "बाराव्या शतकातील वचनकवयित्री व संत."), ("Literature", "साहित्य", "साहित्य")),
        person("purandara", ("Purandara Dasa", "पुरंदर दास", "पुरंदरदास"), ("16th-century composer called the father of Carnatic music.", "16वीं सदी के रचनाकार, जिन्हें कर्नाटक संगीत का पितामह कहा जाता है।", "सोळाव्या शतकातील रचनाकार, ज्यांना कर्नाटक संगीताचे पितामह म्हणतात."), ("Music", "संगीत", "संगीत")),
        person("chennamma", ("Kittur Chennamma", "कित्तूर चेन्नम्मा", "कित्तूर चन्नम्मा"), ("Queen of Kittur who led an armed revolt against the East India Company in 1824.", "कित्तूर की रानी, जिन्होंने 1824 में ईस्ट इंडिया कंपनी के विरुद्ध सशस्त्र विद्रोह किया।", "कित्तूरची राणी, जिने 1824 मध्ये ईस्ट इंडिया कंपनीविरुद्ध सशस्त्र उठाव केला."), ("History", "इतिहास", "इतिहास")),
        person("visvesvaraya", ("Sir M. Visvesvaraya", "सर एम. विश्वेश्वरय्या", "सर एम. विश्वेश्वरय्या"), ("Engineer and Diwan of Mysore; built the KRS dam; Bharat Ratna 1955. Engineers' Day marks his birthday.", "इंजीनियर और मैसूर के दीवान; केआरएस बाँध बनवाया; भारत रत्न 1955। इंजीनियर दिवस उनके जन्मदिन पर मनाया जाता है।", "अभियंता व म्हैसूरचे दिवाण; केआरएस धरण उभारले; भारतरत्न 1955. अभियंता दिन त्यांच्या जन्मदिवशी साजरा होतो."), ("Engineering", "इंजीनियरिंग", "अभियांत्रिकी")),
        person("kuvempu", ("Kuvempu", "कुवेम्पु", "कुवेंपू"), ("Poet and novelist; author of the State anthem; Jnanpith Award 1967.", "कवि और उपन्यासकार; राज्य गीत के रचयिता; ज्ञानपीठ पुरस्कार 1967।", "कवी व कादंबरीकार; राज्यगीताचे रचनाकार; ज्ञानपीठ पुरस्कार 1967."), ("Literature", "साहित्य", "साहित्य")),
        person("cariappa", ("Field Marshal K. M. Cariappa", "फ़ील्ड मार्शल के. एम. करिअप्पा", "फील्ड मार्शल के. एम. करिअप्पा"), ("From Kodagu; first Indian Commander-in-Chief of the Indian Army.", "कोडगु के; भारतीय सेना के पहले भारतीय कमांडर-इन-चीफ़।", "कोडगूचे; भारतीय लष्कराचे पहिले भारतीय सरसेनापती."), ("Military", "सेना", "लष्कर")),
        person("bhimsen", ("Pandit Bhimsen Joshi", "पंडित भीमसेन जोशी", "पंडित भीमसेन जोशी"), ("Hindustani vocalist from Gadag of the Kirana gharana; Bharat Ratna 2009.", "गदग के किराना घराने के हिंदुस्तानी गायक; भारत रत्न 2009।", "गदगचे किराणा घराण्याचे हिंदुस्तानी गायक; भारतरत्न 2009."), ("Music", "संगीत", "संगीत")),
        person("gangubai", ("Gangubai Hangal", "गंगूबाई हंगल", "गंगूबाई हनगल"), ("Hindustani vocalist of Hubballi–Dharwad.", "हुब्बल्ली–धारवाड़ की हिंदुस्तानी गायिका।", "हुबळी–धारवाडच्या हिंदुस्तानी गायिका."), ("Music", "संगीत", "संगीत")),
        person("rajkumar", ("Dr. Rajkumar", "डॉ. राजकुमार", "डॉ. राजकुमार"), ("Kannada cinema's most celebrated actor and singer.", "कन्नड़ सिनेमा के सबसे प्रसिद्ध अभिनेता और गायक।", "कन्नड चित्रपटसृष्टीतील सर्वांत लोकप्रिय अभिनेते व गायक."), ("Cinema", "सिनेमा", "चित्रपट")),
        person("karnad", ("Girish Karnad", "गिरीश कर्नाड", "गिरीश कर्नाड"), ("Playwright, actor and director; Jnanpith Award 1998.", "नाटककार, अभिनेता और निर्देशक; ज्ञानपीठ पुरस्कार 1998।", "नाटककार, अभिनेते व दिग्दर्शक; ज्ञानपीठ पुरस्कार 1998."), ("Theatre", "रंगमंच", "रंगभूमी")),
        person("padukone", ("Prakash Padukone", "प्रकाश पादुकोण", "प्रकाश पडुकोण"), ("Badminton player; first Indian to win the All England Championships (1980).", "बैडमिंटन खिलाड़ी; ऑल इंग्लैंड चैंपियनशिप जीतने वाले पहले भारतीय (1980)।", "बॅडमिंटनपटू; ऑल इंग्लंड स्पर्धा जिंकणारे पहिले भारतीय (1980)."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Coastal Karnataka — Dakshina Kannada, Udupi and Uttara Kannada — has sent many workers and professionals to the Gulf countries since the 1970s, and Mangalorean Catholic, Konkani and Tuluva communities are found in Mumbai, the Gulf and beyond. Since the 1990s Bengaluru's technology industry has created large numbers of Kannadiga professionals in the United States, the United Kingdom and Australia. At the same time Bengaluru is itself a city of migrants, drawing people from every part of India.",
        "तटीय कर्नाटक — दक्षिण कन्नड़, उडुपी और उत्तर कन्नड़ — से 1970 के दशक से बहुत से श्रमिक और पेशेवर खाड़ी देशों में गए हैं, और मंगलूरी कैथोलिक, कोंकणी और तुलुव समुदाय मुंबई, खाड़ी और उससे आगे बसे हैं। 1990 के दशक से बेंगलूरु के प्रौद्योगिकी उद्योग के कारण बड़ी संख्या में कन्नड़ पेशेवर संयुक्त राज्य अमेरिका, ब्रिटेन और ऑस्ट्रेलिया में हैं। साथ ही बेंगलूरु स्वयं प्रवासियों का शहर है, जो भारत के हर हिस्से से लोगों को आकर्षित करता है।",
        "किनारी कर्नाटकातून — दक्षिण कन्नड, उडुपी व उत्तर कन्नड — 1970 च्या दशकापासून अनेक कामगार व व्यावसायिक आखाती देशांत गेले आहेत, आणि मंगळुरी कॅथलिक, कोकणी व तुळुव समुदाय मुंबई, आखाती देश व त्यापलीकडे वसले आहेत. 1990 च्या दशकापासून बंगळूरुच्या तंत्रज्ञान उद्योगामुळे मोठ्या संख्येने कन्नड व्यावसायिक अमेरिका, ब्रिटन व ऑस्ट्रेलियात आहेत. त्याच वेळी बंगळूरु स्वतः स्थलांतरितांचे शहर आहे, जे भारताच्या प्रत्येक भागातून लोकांना आकर्षित करते."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants and internal migrants", "प्रवासियों और आंतरिक प्रवासियों की संख्या", "परदेशी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; MEA."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Karnataka portal", "कर्नाटक सरकार पोर्टल", "कर्नाटक शासन संकेतस्थळ", url="https://www.karnataka.gov.in", src="india-gov"),
        it3("sevasindhu", "Seva Sindhu — State government services", "सेवा सिंधु — राज्य सरकार की सेवाएँ", "सेवा सिंधू — राज्य शासनाच्या सेवा", url="https://sevasindhu.karnataka.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Karnataka Tourism", "कर्नाटक पर्यटन", "कर्नाटक पर्यटन", url="https://karnatakatourism.org", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Bengaluru", "बेंगलूरु", "बंगळूरु"), "080"], [L("Mysuru", "मैसूरु", "म्हैसूरु"), "0821"], [L("Mangaluru", "मंगलूरु", "मंगळूरु"), "0824"],
           [L("Hubballi", "हुब्बल्ली", "हुबळी"), "0836"], [L("Belagavi", "बेलगावी", "बेळगावी"), "0831"], [L("Kalaburagi", "कलबुर्गी", "कलबुर्गी"), "08472"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [(L("Verified local business directory", "सत्यापित स्थानीय व्यवसाय निर्देशिका", "पडताळलेली स्थानिक उद्योग सूची"), "india-gov", "Udyam Registration and co-operative registrars.")]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("gi", ("Karnataka has 45 registered GIs of its own, including several 'Mysore' products — silk, sandal soap, sandalwood oil and agarbathi.", "कर्नाटक के अपने 45 पंजीकृत जीआई हैं, जिनमें कई 'मैसूर' उत्पाद हैं — सिल्क, चंदन साबुन, चंदन तेल और अगरबत्ती।", "कर्नाटकची स्वतःची 45 नोंदणीकृत जीआय आहेत, त्यांत अनेक 'म्हैसूर' उत्पादने आहेत — सिल्क, चंदनी साबण, चंदनाचे तेल व अगरबत्ती."), GI_PDF, "gi-registry"),
        triv("hoysala", ("The Hoysala temples of Belur, Halebidu and Somanathapura became a UNESCO World Heritage Site in 2023.", "बेलूर, हलेबीडु और सोमनाथपुर के होयसल मंदिर 2023 में यूनेस्को विश्व धरोहर स्थल बने।", "बेलूर, हळेबीडू व सोमनाथपूरची होयसळ मंदिरे 2023 मध्ये युनेस्को जागतिक वारसा स्थळ झाली."), UNESCO, "unesco-whc"),
        triv("renewable", ("More than half of the State's installed power capacity was renewable in December 2025.", "दिसंबर 2025 में राज्य की स्थापित बिजली क्षमता का आधे से अधिक हिस्सा अक्षय था।", "डिसेंबर 2025 मध्ये राज्याच्या स्थापित वीजक्षमतेपैकी निम्म्याहून अधिक अक्षय होती.")),
        triv("shivanasamudra", ("The Shivanasamudra hydro-electric station on the Kaveri began supplying power in 1902, among the first in Asia.", "कावेरी पर शिवनसमुद्र जलविद्युत केंद्र ने 1902 में बिजली देना शुरू किया, जो एशिया के पहले केंद्रों में था।", "कावेरीवरील शिवनसमुद्र जलविद्युत केंद्राने 1902 मध्ये वीजपुरवठा सुरू केला — आशियातील पहिल्या केंद्रांपैकी एक.")),
        triv("visvesvaraya", ("India's Engineers' Day, 15 September, marks the birthday of Sir M. Visvesvaraya.", "भारत का इंजीनियर दिवस, 15 सितंबर, सर एम. विश्वेश्वरय्या का जन्मदिन है।", "भारताचा अभियंता दिन, 15 सप्टेंबर, हा सर एम. विश्वेश्वरय्या यांचा जन्मदिवस आहे.")),
        triv("golgumbaz", ("The Gol Gumbaz at Vijayapura has one of the largest domes of its era and a famous whispering gallery.", "विजयपुरा का गोल गुंबज़ अपने युग के सबसे बड़े गुंबदों में है और इसकी 'फुसफुसाहट दीर्घा' प्रसिद्ध है।", "विजयपुराचा गोलघुमट त्याच्या काळातील सर्वांत मोठ्या घुमटांपैकी असून त्याची 'कुजबुज दालन' प्रसिद्ध आहे.")),
        triv("ls", ("The State elects 28 members to the Lok Sabha.", "राज्य से लोकसभा के 28 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 28 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("ka mod3 ok")
