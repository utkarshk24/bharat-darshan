"""Himachal Pradesh modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-HP"
hp = read("regions/IN-HP.json")["metrics"]; ind = read("india.json")["metrics"]
C = research("census_b5plus.json"); F = C["forest"]["HP"]

RAMSAR_HP = [
    ("Pong Dam Lake", "पौंग बाँध झील", "पोंग धरण सरोवर", "2002", "15,662"),
    ("Chandertal Wetland", "चंद्रताल आर्द्रभूमि", "चंद्रताल पाणथळ", "2005", "49"),
    ("Renuka Wetland", "रेणुका आर्द्रभूमि", "रेणुका पाणथळ", "2005", "20"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Forests cover about 28% of Himachal Pradesh (ISFR 2023); much of the rest is alpine meadow, rock, glacier and the cold desert of Lahaul and Spiti, above the tree line. Chir pine covers the lower hills, and higher up there are forests of oak, deodar, blue pine, fir and spruce, with rhododendron and birch near the tree line. The Great Himalayan National Park in Kullu, with the adjoining Sainj and Tirthan valleys, is a UNESCO World Heritage site, and Pin Valley National Park in Spiti protects the snow leopard and Himalayan ibex. The western tragopan, the State bird, is one of the world's rarest pheasants.\n\nThe State has three Ramsar wetlands: the Pong Dam Lake on the Beas, a major wintering ground for waterbirds; the high-altitude Chandertal in Lahaul; and Renuka lake in Sirmaur.",
        "हिमाचल प्रदेश का लगभग 28% भाग वन है (आईएसएफ़आर 2023); बाक़ी का अधिकांश भाग वृक्ष रेखा से ऊपर अल्पाइन घास के मैदान, चट्टान, हिमनद और लाहौल-स्पीति का शीत मरुस्थल है। निचली पहाड़ियों पर चीड़ है, और ऊपर बान, देवदार, कैल, फ़र और स्प्रूस के वन हैं, तथा वृक्ष रेखा के पास बुरांस और भोजपत्र। कुल्लू का ग्रेट हिमालयन राष्ट्रीय उद्यान, सैंज और तीर्थन घाटियों सहित, यूनेस्को विश्व धरोहर स्थल है, और स्पीति का पिन घाटी राष्ट्रीय उद्यान हिम तेंदुए और हिमालयी आइबेक्स को संरक्षण देता है। राज्य पक्षी जाजुराना (पश्चिमी ट्रैगोपैन) दुनिया के सबसे दुर्लभ तीतरों में है।\n\nराज्य में तीन रामसर आर्द्रभूमियाँ हैं: ब्यास पर पौंग बाँध झील, जो जलपक्षियों का बड़ा शीतकालीन ठिकाना है; लाहौल का ऊँचाई पर स्थित चंद्रताल; और सिरमौर की रेणुका झील।",
        "हिमाचल प्रदेशचा सुमारे 28% भाग वनाच्छादित आहे (आयएसएफआर 2023); उरलेल्या भागापैकी बराचसा वृक्षरेषेवरील अल्पाइन कुरणे, खडक, हिमनद्या व लाहौल-स्पितीचे शीत वाळवंट आहे. खालच्या टेकड्यांवर चीड पाइन आहे, आणि वर ओक, देवदार, ब्लू पाइन, फर व स्प्रूसची जंगले आहेत, तसेच वृक्षरेषेजवळ र्‍होडोडेंड्रॉन व भूर्जपत्र. कुल्लूमधील ग्रेट हिमालयन राष्ट्रीय उद्यान, सैंज व तीर्थन खोऱ्यांसह, युनेस्को जागतिक वारसा स्थळ आहे, आणि स्पितीतील पिन खोरे राष्ट्रीय उद्यान हिमबिबट्या व हिमालयीन आयबेक्सचे संरक्षण करते. राज्यपक्षी जुजुराना (पश्चिमी ट्रॅगोपॅन) हा जगातील सर्वांत दुर्मीळ तितरांपैकी एक आहे.\n\nराज्यात तीन रामसर पाणथळे आहेत: बियासवरील पोंग धरण सरोवर, जे पाणपक्ष्यांचे मोठे हिवाळी ठिकाण आहे; लाहौलमधील उंचावरील चंद्रताल; आणि सिरमौरचे रेणुका सरोवर."),
        sources=["fsi", "indian-wetlands", "unesco-whc"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), hp["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(3, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_HP], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026 (year of designation).", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची (घोषणा वर्ष)।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी (घोषणा वर्ष).")),
    lst("protected", [
        it3("ghnp", "Great Himalayan National Park Conservation Area", "ग्रेट हिमालयन राष्ट्रीय उद्यान संरक्षण क्षेत्र", "ग्रेट हिमालयन राष्ट्रीय उद्यान संवर्धन क्षेत्र", m=("UNESCO World Heritage, 2014", "यूनेस्को विश्व धरोहर, 2014", "युनेस्को जागतिक वारसा, 2014")),
        it3("pin", "Pin Valley National Park", "पिन घाटी राष्ट्रीय उद्यान", "पिन खोरे राष्ट्रीय उद्यान", m=("Snow leopard, ibex — Spiti", "हिम तेंदुआ, आइबेक्स — स्पीति", "हिमबिबट्या, आयबेक्स — स्पिती")),
        it3("kibber", "Kibber Wildlife Sanctuary", "किब्बर वन्यजीव अभयारण्य", "किब्बर वन्यजीव अभयारण्य", m=("Cold desert", "शीत मरुस्थल", "शीत वाळवंट")),
        it3("pong", "Pong Dam Lake Wildlife Sanctuary", "पौंग बाँध झील वन्यजीव अभयारण्य", "पोंग धरण सरोवर वन्यजीव अभयारण्य", m=("Wintering waterbirds", "शीतकालीन जलपक्षी", "हिवाळी पाणपक्षी")),
        it3("chail", "Chail Wildlife Sanctuary", "चैल वन्यजीव अभयारण्य", "चैल वन्यजीव अभयारण्य", m=("Cheer pheasant", "चीर तीतर", "चीर तित्तर")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("snowleopard", "Snow leopard (State animal)", "हिम तेंदुआ (राज्य पशु)", "हिमबिबट्या (राज्यप्राणी)"), it3("tragopan", "Western tragopan (State bird)", "जाजुराना (राज्य पक्षी)", "जुजुराना (राज्यपक्षी)"),
        it3("ibex", "Himalayan ibex", "हिमालयी आइबेक्स", "हिमालयीन आयबेक्स"), it3("musk", "Musk deer", "कस्तूरी मृग", "कस्तुरी मृग"),
        it3("monal", "Himalayan monal", "मोनाल", "मोनाल"), it3("goral", "Goral", "घोरल", "घोरल"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Snow leopard population estimate", "हिम तेंदुए की अनुमानित संख्या", "हिमबिबट्यांची अंदाजित संख्या"), "moefcc", "SPAI (Snow Leopard Population Assessment in India) / HP Wildlife Wing."),
        (L("Glacier retreat and glacial lake risk", "हिमनदों का पीछे हटना और हिमनदी झीलों का ख़तरा", "हिमनद्यांची माघार व हिमनदी सरोवरांचा धोका"), "india-gov", "HP State Centre on Climate Change."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Himachal is a water tower for northern India: its snow and glaciers feed the Sutlej, Beas, Ravi, Chenab and Yamuna, which irrigate Punjab, Haryana and Rajasthan downstream. The Bhakra dam's Gobind Sagar and the Pong dam's Maharana Pratap Sagar are among India's largest reservoirs, and the Beas–Sutlej link carries Beas water through a tunnel to the Sutlej. Within the State, most villages rely on springs, streams (khuds) and gravity-fed water schemes rather than groundwater, and traditional irrigation channels (kuhls) water the Kangra valley. Many springs are reported to be drying, and cloudbursts and flash floods — especially in the monsoons of 2023 and 2025 — have repeatedly damaged roads, houses and water schemes.",
        "हिमाचल उत्तर भारत का जल भंडार है: इसकी बर्फ़ और हिमनद सतलुज, ब्यास, रावी, चिनाब और यमुना को पानी देते हैं, जो नीचे पंजाब, हरियाणा और राजस्थान को सींचती हैं। भाखड़ा बाँध का गोबिंद सागर और पौंग बाँध का महाराणा प्रताप सागर भारत के सबसे बड़े जलाशयों में हैं, और ब्यास–सतलुज लिंक सुरंग के माध्यम से ब्यास का पानी सतलुज तक ले जाता है। राज्य के भीतर अधिकांश गाँव भूजल के बजाय झरनों, खड्डों और गुरुत्व-आधारित जल योजनाओं पर निर्भर हैं, और पारंपरिक सिंचाई नालियाँ (कूहलें) कांगड़ा घाटी को सींचती हैं। बहुत से झरनों के सूखने की ख़बरें हैं, और बादल फटने व अचानक बाढ़ — विशेषकर 2023 और 2025 के मानसून में — ने बार-बार सड़कों, घरों और जल योजनाओं को नुकसान पहुँचाया है।",
        "हिमाचल हा उत्तर भारताचा जलसाठा आहे: त्याचा बर्फ व हिमनद्या सतलज, बियास, रावी, चिनाब व यमुनेला पाणी पुरवतात, ज्या खाली पंजाब, हरियाणा व राजस्थानला भिजवतात. भाक्रा धरणाचा गोविंद सागर व पोंग धरणाचा महाराणा प्रताप सागर हे भारतातील सर्वांत मोठ्या जलाशयांपैकी आहेत, आणि बियास–सतलज जोड बोगद्यातून बियासचे पाणी सतलजपर्यंत नेतो. राज्यात बहुतेक गावे भूजलाऐवजी झरे, खड्ड (ओढे) व गुरुत्वाकर्षणावर चालणाऱ्या पाणी योजनांवर अवलंबून आहेत, आणि पारंपरिक सिंचन पाट (कूहल) कांगडा खोरे भिजवतात. अनेक झरे आटत असल्याचे सांगितले जाते, आणि ढगफुटी व आकस्मिक पूर — विशेषतः 2023 व 2025 च्या मान्सूनमध्ये — यांनी वारंवार रस्ते, घरे व पाणी योजनांचे नुकसान केले आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Spring-shed and drinking-water scheme coverage", "झरना क्षेत्र और पेयजल योजना कवरेज", "झरा क्षेत्र व पेयजल योजना व्याप्ती"), "india-gov", "Jal Shakti Vibhag, Himachal Pradesh / Jal Jeevan Mission dashboard."),
        (L("Monsoon damage, 2023 and 2025", "मानसून से नुकसान, 2023 और 2025", "मान्सूनमुळे नुकसान, 2023 व 2025"), "india-gov", "HP State Disaster Management Authority."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Landslides, cloudbursts and flash floods in the monsoon are Himachal's most frequent hazards, and roads to Kullu, Manali, Kinnaur and Chamba are often blocked for days. Much of the State lies in high earthquake zones — the Kangra earthquake of 1905 killed about 20,000 people — and avalanches and heavy snow close high passes in winter. Travellers to Lahaul, Spiti and the high passes should allow for altitude sickness and check road status before setting out, and river banks are dangerous when dams release water.",
        "मानसून में भूस्खलन, बादल फटना और अचानक बाढ़ हिमाचल के सबसे अधिक होने वाले ख़तरे हैं, और कुल्लू, मनाली, किन्नौर व चंबा की सड़कें अक्सर कई दिनों तक बंद रहती हैं। राज्य का अधिकांश भाग ऊँचे भूकंपीय क्षेत्रों में है — 1905 के कांगड़ा भूकंप में लगभग 20,000 लोग मारे गए थे — और सर्दियों में हिमस्खलन व भारी बर्फ़ ऊँचे दर्रे बंद कर देते हैं। लाहौल, स्पीति और ऊँचे दर्रों पर जाने वाले यात्रियों को ऊँचाई की बीमारी का ध्यान रखना चाहिए और निकलने से पहले सड़कों की स्थिति जाँचनी चाहिए, और बाँधों से पानी छोड़े जाने पर नदी किनारे ख़तरनाक होते हैं।",
        "मान्सूनमधील भूस्खलन, ढगफुटी व आकस्मिक पूर हे हिमाचलवरील सर्वाधिक वारंवार येणारे धोके आहेत, आणि कुल्लू, मनाली, किन्नौर व चंब्याचे रस्ते अनेकदा दिवसेंदिवस बंद असतात. राज्याचा बहुतांश भाग उच्च भूकंपप्रवण क्षेत्रात आहे — 1905 च्या कांगडा भूकंपात सुमारे 20,000 लोक मरण पावले — आणि हिवाळ्यात हिमस्खलन व मुसळधार बर्फवृष्टी उंच खिंडी बंद करतात. लाहौल, स्पिती व उंच खिंडींकडे जाणाऱ्या प्रवाशांनी उंचीमुळे होणाऱ्या आजाराची काळजी घ्यावी व निघण्यापूर्वी रस्त्यांची स्थिती तपासावी, आणि धरणांतून पाणी सोडले जाते तेव्हा नदीकाठ धोकादायक असतात."),
        conf="Editorial"),
    emergency_table(("Himachal Pradesh", "हिमाचल प्रदेश", "हिमाचल प्रदेश")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Kangra earthquake of 1905 — official casualty figure", "1905 का कांगड़ा भूकंप — आधिकारिक मृतक संख्या", "1905 चा कांगडा भूकंप — अधिकृत मृतसंख्या"), "india-gov", "Geological Survey of India memoir; the figure above is the commonly cited estimate."),
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official address."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Ten GIs are registered for Himachal Pradesh alone on the GI Registry's list as on 31 December 2025, plus Basmati rice, which it shares with six other States and Union Territories. Most are hill crafts: Kullu and Kinnauri shawls, the Chamba rumal, Kangra paintings, Chamba chappals and the knitted socks and gloves of Lahaul. Kangra tea, Himachali kala zeera (black cumin) and chulli oil from wild apricot kernels are its agricultural and manufactured GIs. Kangra tea, filed in 2005, and Kullu shawl, filed in 2004, are among India's earliest GIs.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में केवल हिमाचल प्रदेश के लिए दस जीआई पंजीकृत हैं, साथ में बासमती चावल, जिसे यह छह अन्य राज्यों और केंद्र शासित प्रदेशों के साथ साझा करता है। अधिकांश पहाड़ी शिल्प हैं: कुल्लू और किन्नौरी शॉल, चंबा रूमाल, कांगड़ा चित्रकला, चंबा चप्पल और लाहौल के बुने मोज़े व दस्ताने। कांगड़ा चाय, हिमाचली काला ज़ीरा और जंगली ख़ुबानी की गुठली से बना चुल्ली तेल इसके कृषि और विनिर्मित जीआई हैं। 2005 में दायर कांगड़ा चाय और 2004 में दायर कुल्लू शॉल भारत के सबसे शुरुआती जीआई में हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत केवळ हिमाचल प्रदेशसाठी दहा जीआय नोंदणीकृत आहेत, सोबत बासमती तांदूळ, जो तो इतर सहा राज्ये व केंद्रशासित प्रदेशांसोबत सामायिक करतो. बहुतेक डोंगरी हस्तकला आहेत: कुल्लू व किन्नौरी शाली, चंबा रुमाल, कांगडा चित्रकला, चंबा चप्पल आणि लाहौलचे विणलेले मोजे व हातमोजे. कांगडा चहा, हिमाचली काळे जिरे व रानटी जर्दाळूच्या बियांपासून बनणारे चुल्ली तेल हे त्याचे कृषी व उत्पादित जीआय आहेत. 2005 मध्ये दाखल कांगडा चहा व 2004 मध्ये दाखल कुल्लू शाल हे भारतातील सर्वांत सुरुवातीच्या जीआयपैकी आहेत."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Pending GI applications from Himachal Pradesh", "हिमाचल प्रदेश के लंबित जीआई आवेदन", "हिमाचल प्रदेशचे प्रलंबित जीआय अर्ज"), "gi-registry", "GI Registry application status search."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Shimla, the old summer capital, with its Mall Road, Ridge, Christ Church and Viceregal Lodge, is reached by the Kalka–Shimla toy train. Manali and the Kullu valley offer orchards, the Hadimba temple, the Solang valley for snow sports and the road through the Atal Tunnel to Lahaul. Dharamshala and McLeod Ganj, home of the Dalai Lama, combine Tibetan monasteries with treks on the Dhauladhar; Bir Billing is a well-known paragliding site; and Dalhousie, Khajjiar and Chamba are quieter hill stations. Spiti and Kinnaur draw travellers to Key and Tabo monasteries, Chandratal lake and villages such as Kalpa and Chitkul. Temples at Jwalamukhi, Chintpurni, Naina Devi and Baijnath are major pilgrimage sites.",
        "पुरानी ग्रीष्मकालीन राजधानी शिमला, अपने मॉल रोड, रिज, क्राइस्ट चर्च और वाइसरीगल लॉज के साथ, कालका–शिमला टॉय ट्रेन से पहुँचा जाता है। मनाली और कुल्लू घाटी में बाग़, हिडिंबा मंदिर, बर्फ़ीले खेलों के लिए सोलंग घाटी और अटल सुरंग से लाहौल जाने वाली सड़क है। दलाई लामा का निवास धर्मशाला और मैक्लोडगंज तिब्बती मठों को धौलाधार के ट्रेक से जोड़ते हैं; बीड़ बिलिंग प्रसिद्ध पैराग्लाइडिंग स्थल है; और डलहौज़ी, खज्जियार और चंबा शांत पर्वतीय स्थल हैं। स्पीति और किन्नौर यात्रियों को की और ताबो मठों, चंद्रताल झील और कल्पा व छितकुल जैसे गाँवों की ओर खींचते हैं। ज्वालामुखी, चिंतपूर्णी, नैना देवी और बैजनाथ के मंदिर प्रमुख तीर्थस्थल हैं।",
        "जुनी उन्हाळी राजधानी शिमला, तिच्या मॉल रोड, रिज, क्राइस्ट चर्च व व्हाइसरीगल लॉजसह, कालका–शिमला टॉय ट्रेनने गाठता येते. मनाली व कुल्लू खोऱ्यात बागा, हिडिंबा मंदिर, बर्फातील खेळांसाठी सोलंग खोरे आणि अटल बोगद्यातून लाहौलकडे जाणारा रस्ता आहे. दलाई लामांचे निवासस्थान धर्मशाला व मॅक्लिओडगंज तिबेटी मठांना धौलाधारवरील ट्रेकशी जोडतात; बीड बिलिंग हे प्रसिद्ध पॅराग्लायडिंग ठिकाण आहे; आणि डलहौसी, खज्जियार व चंबा ही शांत थंड हवेची ठिकाणे आहेत. स्पिती व किन्नौर प्रवाशांना की व ताबो मठ, चंद्रताल सरोवर आणि कल्पा व छितकुलसारख्या गावांकडे आकर्षित करतात. ज्वालामुखी, चिंतपूर्णी, नैना देवी व बैजनाथची मंदिरे प्रमुख तीर्थक्षेत्रे आहेत."),
        conf="Editorial"),
    lst("places", [
        it3("shimla", "Shimla", "शिमला", "शिमला", m=("Mall Road; toy train", "मॉल रोड; टॉय ट्रेन", "मॉल रोड; टॉय ट्रेन")),
        it3("manali", "Manali and Kullu", "मनाली और कुल्लू", "मनाली व कुल्लू", m=("Orchards; Solang; Atal Tunnel", "बाग़; सोलंग; अटल सुरंग", "बागा; सोलंग; अटल बोगदा")),
        it3("dharamshala", "Dharamshala and McLeod Ganj", "धर्मशाला और मैक्लोडगंज", "धर्मशाला व मॅक्लिओडगंज", m=("Tibetan culture; treks", "तिब्बती संस्कृति; ट्रेक", "तिबेटी संस्कृती; ट्रेक")),
        it3("spiti", "Spiti valley", "स्पीति घाटी", "स्पिती खोरे", m=("Key and Tabo monasteries", "की और ताबो मठ", "की व ताबो मठ")),
        it3("kinnaur", "Kinnaur", "किन्नौर", "किन्नौर", m=("Kalpa, Sangla, Chitkul", "कल्पा, सांगला, छितकुल", "कल्पा, सांगला, छितकुल")),
        it3("dalhousie", "Dalhousie and Khajjiar", "डलहौज़ी और खज्जियार", "डलहौसी व खज्जियार", m=("Meadows and forests", "घास के मैदान और वन", "कुरणे व वने")),
        it3("bir", "Bir Billing", "बीड़ बिलिंग", "बीड बिलिंग", m=("Paragliding", "पैराग्लाइडिंग", "पॅराग्लायडिंग")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Shimla by the toy train from Kalka, with Kufri and Naldehra.", "कालका से टॉय ट्रेन द्वारा शिमला, साथ में कुफ़री और नालदेहरा।", "कालकाहून टॉय ट्रेनने शिमला, सोबत कुफरी व नालदेहरा.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Dharamshala, McLeod Ganj, Palampur tea gardens and Bir.", "धर्मशाला, मैक्लोडगंज, पालमपुर के चाय बाग़ान और बीड़।", "धर्मशाला, मॅक्लिओडगंज, पालमपूरचे चहाचे मळे व बीड.")),
        it3("d8", "8 days (June–September)", "8 दिन (जून–सितंबर)", "8 दिवस (जून–सप्टेंबर)", d=("Shimla to Kinnaur and Spiti, returning via Kunzum Pass and the Atal Tunnel to Manali.", "शिमला से किन्नौर और स्पीति, लौटते समय कुंज़ुम दर्रे और अटल सुरंग से मनाली।", "शिमल्याहून किन्नौर व स्पिती, परतीच्या वाटेवर कुंजुम खिंड व अटल बोगद्यामार्गे मनाली.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("hpt", "Himachal Tourism (official)", "हिमाचल पर्यटन (आधिकारिक)", "हिमाचल पर्यटन (अधिकृत)", url="https://himachaltourism.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
        (L("Permit rules for areas near the international border", "अंतरराष्ट्रीय सीमा के पास के क्षेत्रों के परमिट नियम", "आंतरराष्ट्रीय सीमेजवळील भागांचे परवाना नियम"), "india-gov", "District administrations of Kinnaur and Lahaul and Spiti."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Bilaspur", "बिलासपुर", "बिलासपूर"), ("Chamba", "चंबा", "चंबा"), ("Hamirpur", "हमीरपुर", "हमीरपूर"), ("Kangra", "कांगड़ा", "कांगडा"),
    ("Kinnaur", "किन्नौर", "किन्नौर"), ("Kullu", "कुल्लू", "कुल्लू"), ("Lahaul and Spiti", "लाहौल और स्पीति", "लाहौल व स्पिती"), ("Mandi", "मंडी", "मंडी"),
    ("Shimla", "शिमला", "शिमला"), ("Sirmaur", "सिरमौर", "सिरमौर"), ("Solan", "सोलन", "सोलन"), ("Una", "ऊना", "ऊना"),
]
assert len(DISTRICTS) == 12, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("shimla", ("Shimla", "शिमला", "शिमला"), ("Capital and largest city; colonial-era summer capital.", "राजधानी और सबसे बड़ा शहर; औपनिवेशिक काल की ग्रीष्मकालीन राजधानी।", "राजधानी व सर्वांत मोठे शहर; वसाहतकालीन उन्हाळी राजधानी."), ("Capital", "राजधानी", "राजधानी")),
        city("dharamshala", ("Dharamshala", "धर्मशाला", "धर्मशाला"), ("Second capital; seat of the Dalai Lama at McLeod Ganj.", "दूसरी राजधानी; मैक्लोडगंज में दलाई लामा का निवास।", "दुसरी राजधानी; मॅक्लिओडगंज येथे दलाई लामांचे निवासस्थान."), ("Capital", "राजधानी", "राजधानी")),
        city("solan", ("Solan", "सोलन", "सोलन"), ("'Mushroom city'; gateway to the Baddi industrial belt.", "'मशरूम नगरी'; बद्दी औद्योगिक पट्टी का प्रवेश द्वार।", "'मशरूमनगरी'; बद्दी औद्योगिक पट्ट्याचे प्रवेशद्वार."), ("Industry", "उद्योग", "उद्योग")),
        city("mandi", ("Mandi", "मंडी", "मंडी"), ("Temple town on the Beas; Shivratri fair.", "ब्यास किनारे मंदिरों का नगर; शिवरात्रि मेला।", "बियासकाठचे मंदिरनगर; शिवरात्री जत्रा."), ("Heritage", "धरोहर", "वारसा")),
        city("kullu", ("Kullu and Manali", "कुल्लू और मनाली", "कुल्लू व मनाली"), ("Valley towns of orchards and tourism.", "बाग़ों और पर्यटन के घाटी नगर।", "बागा व पर्यटनाची खोऱ्यातील शहरे."), ("Tourism", "पर्यटन", "पर्यटन")),
        city("baddi", ("Baddi", "बद्दी", "बद्दी"), ("Pharmaceutical manufacturing hub.", "दवा विनिर्माण केंद्र।", "औषधनिर्मितीचे केंद्र."), ("Industry", "उद्योग", "उद्योग")),
        city("hamirpur", ("Hamirpur", "हमीरपुर", "हमीरपूर"), ("Education town; NIT Hamirpur.", "शिक्षा नगर; एनआईटी हमीरपुर।", "शिक्षणनगर; एनआयटी हमीरपूर."), ("Education", "शिक्षा", "शिक्षण")),
    ], title=L("Major towns", "प्रमुख नगर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 12 districts (alphabetical)", "12 ज़िले (वर्णानुक्रम)", "12 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Official district list (State notification)", "आधिकारिक ज़िला सूची (राज्य अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य अधिसूचना)"), "india-gov", "Link the State's list of districts."),
        (L("Town populations (Census 2011)", "नगरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Himachal's terrain makes it India's adventure-sports playground: skiing at Solang, Narkanda and Kufri, paragliding at Bir Billing, which hosted the Paragliding World Cup in 2015, river rafting on the Beas and Sutlej, mountaineering from Manali's Atal Bihari Vajpayee Institute of Mountaineering, and mountain-bike and trail races through the high valleys. Kabaddi is hugely popular — Ajay Thakur of Bilaspur was a star of India's 2016 Kabaddi World Cup win — and the HPCA cricket stadium at Dharamshala, set against the Dhauladhar, hosts international matches. Charanjit Singh of Una captained India's hockey team to Olympic gold at Tokyo in 1964.",
        "हिमाचल का भूभाग इसे भारत का साहसिक खेलों का मैदान बनाता है: सोलंग, नारकंडा और कुफ़री में स्कीइंग, बीड़ बिलिंग में पैराग्लाइडिंग, जहाँ 2015 में पैराग्लाइडिंग विश्व कप हुआ, ब्यास और सतलुज पर रिवर राफ्टिंग, मनाली के अटल बिहारी वाजपेयी पर्वतारोहण संस्थान से पर्वतारोहण, और ऊँची घाटियों में माउंटेन बाइक व ट्रेल दौड़। कबड्डी बहुत लोकप्रिय है — बिलासपुर के अजय ठाकुर 2016 कबड्डी विश्व कप में भारत की जीत के सितारे थे — और धौलाधार की पृष्ठभूमि में धर्मशाला का एचपीसीए क्रिकेट स्टेडियम अंतरराष्ट्रीय मैचों की मेज़बानी करता है। ऊना के चरणजीत सिंह ने 1964 में टोक्यो में भारतीय हॉकी टीम को ओलंपिक स्वर्ण दिलाया।",
        "हिमाचलचा भूप्रदेश त्याला भारताचे साहसी खेळांचे मैदान बनवतो: सोलंग, नारकंडा व कुफरीत स्कीइंग, बीड बिलिंग येथे पॅराग्लायडिंग, जिथे 2015 मध्ये पॅराग्लायडिंग विश्वचषक झाला, बियास व सतलजवर रिव्हर राफ्टिंग, मनालीच्या अटल बिहारी वाजपेयी गिर्यारोहण संस्थेतून गिर्यारोहण, आणि उंच खोऱ्यांतून माउंटन बाइक व ट्रेल शर्यती. कबड्डी अतिशय लोकप्रिय आहे — बिलासपूरचा अजय ठाकूर 2016 कबड्डी विश्वचषकातील भारताच्या विजयाचा तारा होता — आणि धौलाधारच्या पार्श्वभूमीवरील धर्मशालेचे एचपीसीए क्रिकेट स्टेडियम आंतरराष्ट्रीय सामने आयोजित करते. ऊनाच्या चरणजीत सिंह यांनी 1964 मध्ये टोकियोत भारतीय हॉकी संघाला ऑलिम्पिक सुवर्ण मिळवून दिले."),
        conf="Editorial"),
    lst("venues", [
        it3("hpca", "HPCA Stadium, Dharamshala", "एचपीसीए स्टेडियम, धर्मशाला", "एचपीसीए स्टेडियम, धर्मशाला"),
        it3("abvimas", "Atal Bihari Vajpayee Institute of Mountaineering, Manali", "अटल बिहारी वाजपेयी पर्वतारोहण संस्थान, मनाली", "अटल बिहारी वाजपेयी गिर्यारोहण संस्था, मनाली"),
        it3("solang", "Solang valley (skiing)", "सोलंग घाटी (स्कीइंग)", "सोलंग खोरे (स्कीइंग)"),
        it3("bir", "Bir Billing (paragliding)", "बीड़ बिलिंग (पैराग्लाइडिंग)", "बीड बिलिंग (पॅराग्लायडिंग)"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("National and international medallists from Himachal (official list)", "हिमाचल के राष्ट्रीय और अंतरराष्ट्रीय पदक विजेता (आधिकारिक सूची)", "हिमाचलचे राष्ट्रीय व आंतरराष्ट्रीय पदकविजेते (अधिकृत यादी)"), "india-gov", "HP Youth Services and Sports Department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("parmar", ("Dr Yashwant Singh Parmar", "डॉ. यशवंत सिंह परमार", "डॉ. यशवंतसिंह परमार"), ("First Chief Minister, regarded as the architect of Himachal Pradesh.", "पहले मुख्यमंत्री, जिन्हें हिमाचल प्रदेश का निर्माता माना जाता है।", "पहिले मुख्यमंत्री, ज्यांना हिमाचल प्रदेशचे शिल्पकार मानले जाते."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("somnath", ("Major Somnath Sharma", "मेजर सोमनाथ शर्मा", "मेजर सोमनाथ शर्मा"), ("First recipient of the Param Vir Chakra, for the defence of Srinagar in 1947; his family was from Kangra.", "परमवीर चक्र के पहले विजेता, 1947 में श्रीनगर की रक्षा के लिए; उनका परिवार कांगड़ा से था।", "परमवीर चक्राचे पहिले मानकरी, 1947 मध्ये श्रीनगरच्या संरक्षणासाठी; त्यांचे कुटुंब कांगड्याचे होते."), ("Armed forces", "सशस्त्र बल", "सशस्त्र दले")),
        person("batra", ("Captain Vikram Batra", "कैप्टन विक्रम बत्रा", "कॅप्टन विक्रम बत्रा"), ("Param Vir Chakra (posthumous) in the Kargil war of 1999; from Palampur.", "1999 के कारगिल युद्ध में परमवीर चक्र (मरणोपरांत); पालमपुर से।", "1999 च्या कारगिल युद्धात परमवीर चक्र (मरणोत्तर); पालमपूरचे."), ("Armed forces", "सशस्त्र बल", "सशस्त्र दले")),
        person("sansar", ("Maharaja Sansar Chand", "महाराजा संसार चंद", "महाराजा संसारचंद"), ("Katoch ruler of Kangra and great patron of Kangra painting.", "कांगड़ा के कटोच शासक और कांगड़ा चित्रकला के महान संरक्षक।", "कांगड्याचे कटोच राज्यकर्ते व कांगडा चित्रकलेचे मोठे आश्रयदाते."), ("History", "इतिहास", "इतिहास")),
        person("nirmal", ("Nirmal Verma", "निर्मल वर्मा", "निर्मल वर्मा"), ("Hindi novelist and Jnanpith laureate, born in Shimla.", "हिंदी उपन्यासकार और ज्ञानपीठ पुरस्कार विजेता, शिमला में जन्मे।", "हिंदी कादंबरीकार व ज्ञानपीठ पुरस्कारविजेते, शिमल्यात जन्मलेले."), ("Literature", "साहित्य", "साहित्य")),
        person("charanjit", ("Charanjit Singh", "चरणजीत सिंह", "चरणजीत सिंह"), ("Captain of India's hockey team at the 1964 Olympic gold; from Una.", "1964 ओलंपिक स्वर्ण विजेता भारतीय हॉकी टीम के कप्तान; ऊना से।", "1964 ऑलिम्पिक सुवर्णविजेत्या भारतीय हॉकी संघाचे कर्णधार; ऊनाचे."), ("Sport", "खेल", "क्रीडा")),
        person("ajay", ("Ajay Thakur", "अजय ठाकुर", "अजय ठाकूर"), ("Kabaddi raider who starred in India's 2016 World Cup win.", "कबड्डी रेडर, जो 2016 विश्व कप में भारत की जीत के सितारे रहे।", "कबड्डी रेडर, जो 2016 विश्वचषकातील भारताच्या विजयाचा तारा ठरला."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Many Himachalis work outside the State — in the armed forces, in which the Dogra and other regiments recruit heavily from Kangra, Hamirpur and Mandi, and in government and private jobs in Chandigarh, Delhi and beyond — and their pensions and remittances are important to hill households. The State in turn hosts a large Tibetan refugee community around Dharamshala, as well as Nepali and other migrant workers in orchards and construction.",
        "बहुत से हिमाचली राज्य से बाहर काम करते हैं — सशस्त्र बलों में, जिनमें डोगरा और अन्य रेजिमेंट कांगड़ा, हमीरपुर और मंडी से बड़ी संख्या में भर्ती करती हैं, और चंडीगढ़, दिल्ली व अन्य जगहों पर सरकारी व निजी नौकरियों में — और उनकी पेंशन व भेजी गई रक़म पहाड़ी परिवारों के लिए महत्त्वपूर्ण है। बदले में राज्य धर्मशाला के आसपास एक बड़े तिब्बती शरणार्थी समुदाय को, और बाग़ानों व निर्माण में नेपाली व अन्य प्रवासी श्रमिकों को आश्रय देता है।",
        "अनेक हिमाचली राज्याबाहेर काम करतात — सशस्त्र दलांत, ज्यांत डोग्रा व इतर रेजिमेंट कांगडा, हमीरपूर व मंडीतून मोठ्या संख्येने भरती करतात, आणि चंदीगड, दिल्ली व इतरत्र सरकारी व खासगी नोकऱ्यांत — आणि त्यांचे निवृत्तिवेतन व पाठवलेले पैसे डोंगरी कुटुंबांसाठी महत्त्वाचे आहेत. त्याबदल्यात राज्य धर्मशालेभोवती मोठ्या तिबेटी निर्वासित समुदायाला, आणि बागा व बांधकामात नेपाळी व इतर स्थलांतरित कामगारांना आश्रय देते."),
        conf="Editorial"),
    gaps("g", [
        (L("Serving and ex-servicemen from Himachal", "हिमाचल के सेवारत और पूर्व सैनिक", "हिमाचलचे सेवारत व माजी सैनिक"), "india-gov", "Department of Sainik Welfare, Himachal Pradesh."),
        (L("Tibetan population in Himachal", "हिमाचल में तिब्बती जनसंख्या", "हिमाचलमधील तिबेटी लोकसंख्या"), "india-gov", "Central Tibetan Administration demographic survey."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Himachal Pradesh portal", "हिमाचल प्रदेश सरकार पोर्टल", "हिमाचल प्रदेश शासन संकेतस्थळ", url="https://himachal.nic.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Himachal Tourism", "हिमाचल पर्यटन", "हिमाचल पर्यटन", url="https://himachaltourism.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major towns", "प्रमुख नगरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("Town", "नगर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Shimla", "शिमला", "शिमला"), "0177"], [L("Dharamshala", "धर्मशाला", "धर्मशाला"), "01892"], [L("Mandi", "मंडी", "मंडी"), "01905"],
           [L("Kullu and Manali", "कुल्लू और मनाली", "कुल्लू व मनाली"), "01902"], [L("Solan", "सोलन", "सोलन"), "01792"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("atal", ("The Atal Tunnel under Rohtang is 9.02 km long and lies at about 3,000 m above sea level.", "रोहतांग के नीचे अटल सुरंग 9.02 किमी लंबी है और समुद्र तल से लगभग 3,000 मीटर पर है।", "रोहतांगखालील अटल बोगदा 9.02 किमी लांब असून समुद्रसपाटीपासून सुमारे 3,000 मीटर उंचीवर आहे."), "https://pmindia.gov.in/?p=8160111", "pmindia"),
        triv("sanskrit", ("Sanskrit is Himachal's second official language.", "संस्कृत हिमाचल की द्वितीय राजभाषा है।", "संस्कृत ही हिमाचलची द्वितीय राजभाषा आहे.")),
        triv("lfpr", (f"{AP['plfs_lfpr_2025']['HP']['female']}% of Himachali women aged 15 and above were in the labour force in 2025, against {AP['plfs_lfpr_2025']['IN']['female']}% nationally.", f"2025 में 15 वर्ष से अधिक आयु की {AP['plfs_lfpr_2025']['HP']['female']}% हिमाचली महिलाएँ श्रम बल में थीं, जबकि राष्ट्रीय स्तर पर {AP['plfs_lfpr_2025']['IN']['female']}%।", f"2025 मध्ये 15 वर्षांवरील {AP['plfs_lfpr_2025']['HP']['female']}% हिमाचली स्त्रिया श्रमशक्तीत होत्या, तर राष्ट्रीय पातळीवर {AP['plfs_lfpr_2025']['IN']['female']}%."), MOSPI, "plfs"),
        triv("kalka", ("The Kalka–Shimla railway, opened in 1903, is part of the UNESCO World Heritage site 'Mountain Railways of India'.", "1903 में खुली कालका–शिमला रेलवे यूनेस्को विश्व धरोहर स्थल 'भारत की पर्वतीय रेलें' का हिस्सा है।", "1903 मध्ये सुरू झालेली कालका–शिमला रेल्वे युनेस्को जागतिक वारसा स्थळ 'भारताच्या पर्वतीय रेल्वे'चा भाग आहे."), UNESCO, "unesco-whc"),
        triv("summer", ("Shimla was the summer capital of British India from 1864.", "1864 से शिमला ब्रिटिश भारत की ग्रीष्मकालीन राजधानी था।", "1864 पासून शिमला ही ब्रिटिश भारताची उन्हाळी राजधानी होती.")),
        triv("ls", ("The State elects 4 members to the Lok Sabha.", "राज्य से लोकसभा के 4 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 4 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("hp mod3 ok")
