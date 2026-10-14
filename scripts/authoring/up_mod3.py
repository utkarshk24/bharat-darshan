"""Uttar Pradesh modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-UP"
UPF = "https://updes.up.nic.in/updes/data/upinfigures/up%20in%20figures-%202022.pdf"
TOUR = "https://tourism.gov.in/sites/default/files/2025-03/usq.3180%20for%2027.03.2025.pdf"
GANGA = "https://newsonair.gov.in/pm-modi-inaugurates-594-km-long-ganga-expressway-connecting-meerut-to-prayagraj/"
up = read("regions/IN-UP.json")["metrics"]; ind = read("india.json")["metrics"]

RAMSAR_UP = [
    ("Upper Ganga River (Brijghat to Narora)", "ऊपरी गंगा नदी (बृजघाट से नरौरा)", "वरची गंगा नदी (बृजघाट ते नरौरा)", "8 Nov 2005", "26,590"),
    ("Nawabganj Bird Sanctuary", "नवाबगंज पक्षी अभयारण्य", "नवाबगंज पक्षी अभयारण्य", "19 Sep 2019", "225"),
    ("Sarsai Nawar Jheel", "सरसई नावर झील", "सरसई नावर तलाव", "19 Sep 2019", "161"),
    ("Sandi Bird Sanctuary", "सांडी पक्षी अभयारण्य", "सांडी पक्षी अभयारण्य", "26 Sep 2019", "309"),
    ("Samaspur Bird Sanctuary", "समसपुर पक्षी अभयारण्य", "समसपूर पक्षी अभयारण्य", "3 Oct 2019", "799"),
    ("Parvati Arga Bird Sanctuary", "पार्वती अरगा पक्षी अभयारण्य", "पार्वती अरगा पक्षी अभयारण्य", "2 Dec 2019", "722"),
    ("Saman Bird Sanctuary", "समान पक्षी अभयारण्य", "समान पक्षी अभयारण्य", "2 Dec 2019", "526"),
    ("Sur Sarovar", "सूर सरोवर", "सूर सरोवर", "21 Aug 2020", "431"),
    ("Haiderpur Wetland", "हैदरपुर आर्द्रभूमि", "हैदरपूर पाणथळ", "13 Apr 2021", "6,908"),
    ("Bakhira Wildlife Sanctuary", "बखिरा वन्यजीव अभयारण्य", "बखिरा वन्यजीव अभयारण्य", "29 Jun 2021", "2,894"),
    ("Patna Bird Sanctuary", "पटना पक्षी अभयारण्य", "पटना पक्षी अभयारण्य", "4 Dec 2025", "108.86"),
    ("Sheikha Jheel Bird Sanctuary", "शेखा झील पक्षी अभयारण्य", "शेखा झील पक्षी अभयारण्य", "19 Jan 2026", "40.31"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Uttar Pradesh is one of India's least forested States — forest cover was about 6.2% of its area in ISFR 2023 — because almost all of the Gangetic plain has long been farmed. The richest wild landscape is the Terai along the Nepal border, where Dudhwa and Pilibhit tiger reserves protect tall grasslands and sal forest with tigers, swamp deer (barasingha), the State animal, one-horned rhinoceroses reintroduced into Dudhwa, and the Bengal florican. Amangarh in Bijnor adjoins Corbett, and Ranipur in Chitrakoot protects dry forest in the south.\n\nWetlands matter a great deal: the State has 12 Ramsar sites, from the Upper Ganga stretch, home to the Gangetic dolphin and gharial, to village lakes such as Nawabganj, Sur Sarovar and Bakhira that host migratory waterbirds and the sarus crane, the State bird. The Chambal sanctuary, shared with Madhya Pradesh and Rajasthan, protects one of the last strongholds of the gharial.",
        "उत्तर प्रदेश भारत के सबसे कम वन वाले राज्यों में है — आईएसएफ़आर 2023 में इसके क्षेत्रफल का लगभग 6.2% वनाच्छादित था — क्योंकि गंगा का लगभग पूरा मैदान लंबे समय से खेती में है। सबसे समृद्ध वन्य भूदृश्य नेपाल सीमा पर तराई है, जहाँ दुधवा और पीलीभीत बाघ अभयारण्य ऊँची घास और साल के वनों की रक्षा करते हैं, जिनमें बाघ, राज्य पशु बारहसिंगा, दुधवा में फिर से बसाए गए एक सींग वाले गैंडे और बंगाल फ़्लोरिकन रहते हैं। बिजनौर का अमानगढ़ कॉर्बेट से सटा है, और चित्रकूट का रानीपुर दक्षिण के शुष्क वनों की रक्षा करता है।\n\nआर्द्रभूमियाँ बहुत महत्त्वपूर्ण हैं: राज्य में 12 रामसर स्थल हैं — गंगा डॉल्फ़िन और घड़ियाल के आवास ऊपरी गंगा खंड से लेकर नवाबगंज, सूर सरोवर और बखिरा जैसी गाँव की झीलों तक, जहाँ प्रवासी जलपक्षी और राज्य पक्षी सारस आते हैं। मध्य प्रदेश और राजस्थान के साथ साझा चंबल अभयारण्य घड़ियाल के अंतिम गढ़ों में से एक की रक्षा करता है।",
        "उत्तर प्रदेश हे भारतातील सर्वांत कमी वनक्षेत्र असलेल्या राज्यांपैकी एक आहे — आयएसएफआर 2023 नुसार क्षेत्रफळाच्या सुमारे 6.2% भागावर वनाच्छादन होते — कारण गंगेचे जवळपास संपूर्ण मैदान दीर्घकाळ लागवडीखाली आहे. सर्वांत समृद्ध वन्य प्रदेश नेपाळ सीमेवरील तराई आहे, जिथे दुधवा व पिलीभीत व्याघ्र प्रकल्प उंच गवताळ प्रदेश व सालवनांचे संरक्षण करतात — वाघ, राज्यप्राणी बारशिंगा, दुधवात पुन्हा वसवलेले एकशिंगी गेंडे आणि बंगाल फ्लोरिकन तिथे आहेत. बिजनौरमधील अमानगड कॉर्बेटला लागून आहे, आणि चित्रकूटमधील राणीपूर दक्षिणेकडील कोरड्या वनांचे संरक्षण करते.\n\nपाणथळ जागा फार महत्त्वाच्या आहेत: राज्यात 12 रामसर स्थळे आहेत — गांगेय डॉल्फिन व घडियालचा अधिवास असलेल्या वरच्या गंगा पट्ट्यापासून ते नवाबगंज, सूर सरोवर व बखिरा यांसारख्या गावतलावांपर्यंत, जिथे स्थलांतरित पाणपक्षी आणि राज्यपक्षी सारस येतात. मध्य प्रदेश व राजस्थानसोबत सामायिक चंबळ अभयारण्य घडियालच्या शेवटच्या बालेकिल्ल्यांपैकी एकाचे संरक्षण करते."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(15045.80, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(14927.37, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), up["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(12, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026 (India total 99)."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_UP], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026.", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी.")),
    lst("protected", [
        it3("dudhwa", "Dudhwa Tiger Reserve", "दुधवा बाघ अभयारण्य", "दुधवा व्याघ्र प्रकल्प", m=("Lakhimpur Kheri; rhino, barasingha", "लखीमपुर खीरी; गैंडा, बारहसिंगा", "लखीमपूर खेरी; गेंडा, बारशिंगा")),
        it3("pilibhit", "Pilibhit Tiger Reserve", "पीलीभीत बाघ अभयारण्य", "पिलीभीत व्याघ्र प्रकल्प", m=("Terai", "तराई", "तराई")),
        it3("amangarh", "Amangarh Tiger Reserve", "अमानगढ़ बाघ अभयारण्य", "अमानगड व्याघ्र प्रकल्प", m=("Bijnor, adjoining Corbett", "बिजनौर, कॉर्बेट से सटा", "बिजनौर, कॉर्बेटलगत")),
        it3("ranipur", "Ranipur Tiger Reserve", "रानीपुर बाघ अभयारण्य", "राणीपूर व्याघ्र प्रकल्प", m=("Chitrakoot", "चित्रकूट", "चित्रकूट")),
        it3("chambal", "National Chambal Sanctuary", "राष्ट्रीय चंबल अभयारण्य", "राष्ट्रीय चंबळ अभयारण्य", m=("Gharial; shared with MP and Rajasthan", "घड़ियाल; मध्य प्रदेश और राजस्थान के साथ साझा", "घडियाल; मध्य प्रदेश व राजस्थानसोबत सामायिक")),
        it3("katarniaghat", "Katarniaghat Wildlife Sanctuary", "कतर्नियाघाट वन्यजीव अभयारण्य", "कतर्नियाघाट वन्यजीव अभयारण्य", m=("Bahraich", "बहराइच", "बहराइच")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("barasingha", "Swamp deer (barasingha)", "बारहसिंगा", "बारशिंगा"), it3("sarus", "Sarus crane", "सारस", "सारस क्रौंच"),
        it3("tiger", "Bengal tiger", "बंगाल बाघ", "पट्टेरी वाघ"), it3("rhino", "One-horned rhinoceros", "एक सींग वाला गैंडा", "एकशिंगी गेंडा"),
        it3("dolphin", "Gangetic dolphin", "गंगा डॉल्फ़िन (सूंस)", "गांगेय डॉल्फिन"), it3("gharial", "Gharial", "घड़ियाल", "घडियाल"),
        it3("florican", "Bengal florican", "बंगाल फ़्लोरिकन", "बंगाल फ्लोरिकन"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger reserve areas and tiger estimates", "बाघ अभयारण्य क्षेत्रफल और बाघों का अनुमान", "व्याघ्र प्रकल्प क्षेत्र व वाघांचा अंदाज"), "ntca", "NTCA tiger reserve list."),
        (L("National parks and sanctuaries (count, area)", "राष्ट्रीय उद्यान और अभयारण्य (संख्या, क्षेत्रफल)", "राष्ट्रीय उद्याने व अभयारण्ये (संख्या, क्षेत्र)"), "moefcc", "ENVIS / WII database."),
        (L("Sarus crane count", "सारस गणना", "सारस गणना"), "moefcc", "State Forest Department sarus census."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Uttar Pradesh has abundant rivers but uneven water. The Ganga and its tributaries, the Upper and Lower Ganga canals (opened in the 19th century) and a very large number of tube wells irrigate the plains, making the State a leading producer of wheat, rice and sugarcane. The cost is falling groundwater in the western districts, arsenic and fluoride in parts of the east and the Bundelkhand region, and polluted river stretches near cities, which the national Namami Gange programme targets.\n\nBundelkhand in the south suffers recurrent drought; the Ken–Betwa river link, shared with Madhya Pradesh, is intended to move water into the region. In the east, the Ghaghara, Rapti and Gandak flood large areas most monsoons.",
        "उत्तर प्रदेश में नदियाँ प्रचुर हैं, लेकिन पानी असमान रूप से उपलब्ध है। गंगा और उसकी सहायक नदियाँ, 19वीं सदी में खुली ऊपरी और निचली गंगा नहरें और बहुत बड़ी संख्या में नलकूप मैदानों को सींचते हैं, जिससे राज्य गेहूँ, चावल और गन्ने का प्रमुख उत्पादक है। इसकी क़ीमत पश्चिमी ज़िलों में गिरता भूजल, पूर्व और बुंदेलखंड के कुछ भागों में आर्सेनिक और फ़्लोराइड, और शहरों के पास प्रदूषित नदी खंड हैं, जिन पर राष्ट्रीय नमामि गंगे कार्यक्रम केंद्रित है।\n\nदक्षिण में बुंदेलखंड बार-बार सूखे से जूझता है; मध्य प्रदेश के साथ साझा केन–बेतवा नदी जोड़ परियोजना का उद्देश्य इस क्षेत्र में पानी पहुँचाना है। पूर्व में घाघरा, राप्ती और गंडक लगभग हर मानसून में बड़े क्षेत्र को बाढ़ में डुबो देती हैं।",
        "उत्तर प्रदेशात नद्या भरपूर आहेत, पण पाणी असमान आहे. गंगा व तिच्या उपनद्या, एकोणिसाव्या शतकात सुरू झालेले वरचे व खालचे गंगा कालवे आणि अतिशय मोठ्या संख्येने कूपनलिका मैदानांना पाणी देतात, त्यामुळे राज्य गहू, तांदूळ व उसाचे आघाडीचे उत्पादक आहे. याची किंमत म्हणजे पश्चिमेकडील जिल्ह्यांत घटते भूजल, पूर्व भागात व बुंदेलखंडच्या काही भागांत आर्सेनिक व फ्लोराइड, आणि शहरांजवळील प्रदूषित नदीपट्टे — ज्यांवर राष्ट्रीय नमामि गंगे कार्यक्रम केंद्रित आहे.\n\nदक्षिणेकडील बुंदेलखंड वारंवार दुष्काळ सोसतो; मध्य प्रदेशसोबत सामायिक केन–बेतवा नदीजोड प्रकल्पाचा उद्देश या भागात पाणी पोहोचवणे आहे. पूर्वेकडे घाघरा, राप्ती व गंडक जवळपास दर पावसाळ्यात मोठा भाग पुराखाली आणतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Net irrigated area and sources", "शुद्ध सिंचित क्षेत्र और स्रोत", "निव्वळ सिंचित क्षेत्र व स्रोत"), "up-des", "Land use statistics."),
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Uttar Pradesh's main natural hazards are monsoon floods in the eastern and Terai districts, heatwaves in May and June, cold waves and dense fog in December–January — which cause road and rail accidents — and lightning strikes during pre-monsoon and monsoon storms. Bundelkhand is drought-prone. The western districts lie in a higher seismic zone near the Himalaya.\n\nFor visitors, the main precautions are avoiding midday travel in summer, allowing extra time for fog-related delays in winter, and following crowd-safety instructions at large festivals and melas.",
        "उत्तर प्रदेश के मुख्य प्राकृतिक ख़तरे हैं — पूर्वी और तराई ज़िलों में मानसूनी बाढ़, मई और जून में लू, दिसंबर–जनवरी में शीत लहर और घना कोहरा — जिससे सड़क और रेल दुर्घटनाएँ होती हैं — और मानसून-पूर्व व मानसूनी तूफ़ानों में आकाशीय बिजली। बुंदेलखंड सूखा-प्रवण है। पश्चिमी ज़िले हिमालय के पास ऊँचे भूकंपीय क्षेत्र में हैं।\n\nपर्यटकों के लिए मुख्य सावधानियाँ हैं: गर्मियों में दोपहर की यात्रा से बचना, सर्दियों में कोहरे से होने वाली देरी के लिए अतिरिक्त समय रखना, और बड़े त्योहारों व मेलों में भीड़-सुरक्षा निर्देशों का पालन करना।",
        "उत्तर प्रदेशमधील प्रमुख नैसर्गिक धोके म्हणजे पूर्वेकडील व तराईतील जिल्ह्यांत मोसमी पूर, मे-जूनमध्ये उष्णतेची लाट, डिसेंबर–जानेवारीत थंडीची लाट व दाट धुके — ज्यामुळे रस्ते व रेल्वे अपघात होतात — आणि मान्सूनपूर्व व मोसमी वादळांत वीज कोसळणे. बुंदेलखंड दुष्काळप्रवण आहे. पश्चिमेकडील जिल्हे हिमालयाजवळील अधिक भूकंपप्रवण क्षेत्रात आहेत.\n\nपर्यटकांसाठी मुख्य काळजी: उन्हाळ्यात दुपारचा प्रवास टाळणे, हिवाळ्यात धुक्यामुळे होणाऱ्या विलंबासाठी जास्त वेळ ठेवणे, आणि मोठ्या सणांत व मेळ्यांत गर्दी-सुरक्षा सूचनांचे पालन करणे."),
        conf="Editorial"),
    emergency_table(("Uttar Pradesh", "उत्तर प्रदेश", "उत्तर प्रदेश")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("UP State Disaster Management Authority — verified link", "उत्तर प्रदेश राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "उत्तर प्रदेश राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official UPSDMA address."),
        (L("Flood-prone area", "बाढ़-प्रवण क्षेत्र", "पूरप्रवण क्षेत्र"), "ndma", "UPSDMA flood hazard atlas."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Uttar Pradesh has 78 registered Geographical Indications in the GI Registry's list as on 31 December 2025 — the most of any State in this directory — of which 56 are handicrafts. Varanasi alone accounts for more than twenty, from Banarasi brocades and saris, gulabi meenakari and wooden toys to the tabla, shehnai, langda mango, paan and thandai. Other well-known names are Lucknow chikankari and zardozi, Bhadohi carpets, Moradabad metal craft, Firozabad glass, Khurja pottery, Nizamabad black clay pottery, Kannauj perfume, Agra stone inlay, the Kalanamak rice of Siddharthnagar and Malihabadi Dussehri mangoes.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में उत्तर प्रदेश के 78 पंजीकृत भौगोलिक संकेतक हैं — इस निर्देशिका में किसी भी राज्य से अधिक — जिनमें 56 हस्तशिल्प हैं। अकेले वाराणसी के बीस से अधिक हैं — बनारसी ब्रोकेड और साड़ियों, गुलाबी मीनाकारी और लकड़ी के खिलौनों से लेकर तबला, शहनाई, लंगड़ा आम, पान और ठंडाई तक। अन्य प्रसिद्ध नाम हैं लखनवी चिकनकारी और ज़रदोज़ी, भदोही के क़ालीन, मुरादाबाद का धातु शिल्प, फ़िरोज़ाबाद का काँच, खुर्जा के मृद्भांड, निज़ामाबाद के काले मिट्टी के बर्तन, कन्नौज का इत्र, आगरा की पत्थर पच्चीकारी, सिद्धार्थनगर का कालानमक चावल और मलीहाबादी दशहरी आम।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत उत्तर प्रदेशची 78 नोंदणीकृत भौगोलिक मानांकने आहेत — या सूचीतील कोणत्याही राज्यापेक्षा जास्त — त्यांतील 56 हस्तकला आहेत. एकट्या वाराणसीची वीसहून अधिक आहेत — बनारसी जरीकाम व साड्या, गुलाबी मीनाकारी व लाकडी खेळण्यांपासून तबला, सनई, लंगडा आंबा, पान व थंडाईपर्यंत. इतर प्रसिद्ध नावे म्हणजे लखनवी चिकनकारी व जरदोजी, भदोहीचे गालिचे, मुरादाबादचे धातुकाम, फिरोजाबादची काच, खुर्जाची मातीची भांडी, निजामाबादची काळ्या मातीची भांडी, कनौजचे अत्तर, आग्र्याचे दगडी जडावकाम, सिद्धार्थनगरचा काळानमक तांदूळ आणि मलीहाबादी दशेरी आंबा."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
        (L("One District One Product (ODOP) list", "एक ज़िला एक उत्पाद (ओडीओपी) सूची", "एक जिल्हा एक उत्पादन (ओडीओपी) यादी"), "dpiit", "UP ODOP portal / DPIIT list."),
    ]),
])

# ---------------- T. Tourism ----------------
TV = [("2022", 317913000, 650000), ("2023", 478526000, 1601000), ("2024", 646807000, 2269000)]
tdp = lambda v, y: dp(v, "visits", y, "calendar", "tourism", TOUR, rev="provisional" if y == "2024" else "final",
                      note="Rajya Sabha Unstarred Q. 3180, 27 March 2025 (Ministry of Tourism, from the State Tourism Department). Published in lakh visits (e.g. 6,468.07 lakh); 2024 is provisional." if y == "2024" else "Published in lakh visits.")
module(R, "tourism", [
    prose("p1", L(
        "Uttar Pradesh receives more domestic tourist visits than any State listed by the Ministry of Tourism — about 64.7 crore in 2024 (provisional), up from 31.8 crore in 2022 — driven by pilgrimage to Ayodhya, Varanasi, Prayagraj and Mathura–Vrindavan. Foreign visits were about 22.7 lakh in 2024, centred on Agra's Taj Mahal and the Buddhist circuit of Sarnath, Kushinagar, Kapilvastu and Shravasti. The Maha Kumbh at Prayagraj in early 2025 alone drew several crore pilgrims.",
        "पर्यटन मंत्रालय के आँकड़ों में उत्तर प्रदेश में सबसे अधिक घरेलू पर्यटक यात्राएँ होती हैं — 2024 में लगभग 64.7 करोड़ (अनंतिम), जो 2022 के 31.8 करोड़ से अधिक हैं — जिसका मुख्य कारण अयोध्या, वाराणसी, प्रयागराज और मथुरा–वृंदावन की तीर्थयात्राएँ हैं। 2024 में विदेशी यात्राएँ लगभग 22.7 लाख थीं, जो आगरा के ताजमहल और सारनाथ, कुशीनगर, कपिलवस्तु और श्रावस्ती के बौद्ध परिपथ पर केंद्रित थीं। 2025 की शुरुआत में प्रयागराज के महाकुंभ में ही कई करोड़ श्रद्धालु आए।",
        "पर्यटन मंत्रालयाच्या आकडेवारीनुसार उत्तर प्रदेशला सर्वाधिक देशी पर्यटक भेटी मिळतात — 2024 मध्ये सुमारे 64.7 कोटी (तात्पुरत्या), 2022 मधील 31.8 कोटींपेक्षा जास्त — मुख्यतः अयोध्या, वाराणसी, प्रयागराज व मथुरा–वृंदावन येथील तीर्थयात्रांमुळे. 2024 मध्ये परदेशी भेटी सुमारे 22.7 लाख होत्या, ज्या आग्र्याचा ताजमहाल आणि सारनाथ, कुशीनगर, कपिलवस्तू व श्रावस्तीच्या बौद्ध परिक्रमेवर केंद्रित होत्या. 2025 च्या सुरुवातीच्या प्रयागराज महाकुंभालाच अनेक कोटी भाविक आले."),
        sources=["tourism"], conf="Official"),
    facts("f", [
        fact("dtv", L("Domestic tourist visits", "घरेलू पर्यटक यात्राएँ", "देशी पर्यटक भेटी"), tdp(646807000, "2024"), "count", "neutral", previous=tdp(478526000, "2023")),
        fact("ftv", L("Foreign tourist visits", "विदेशी पर्यटक यात्राएँ", "परदेशी पर्यटक भेटी"), tdp(2269000, "2024"), "count", "neutral", previous=tdp(1601000, "2023")),
    ], title=L("Tourist visits", "पर्यटक यात्राएँ", "पर्यटक भेटी")),
    lst("places", [
        it3("taj", "Taj Mahal and Agra Fort", "ताजमहल और आगरा क़िला", "ताजमहाल व आग्र्याचा किल्ला", m=("UNESCO heritage", "यूनेस्को धरोहर", "युनेस्को वारसा")),
        it3("varanasi", "Varanasi ghats and Sarnath", "वाराणसी के घाट और सारनाथ", "वाराणसीचे घाट व सारनाथ", m=("Pilgrimage, heritage", "तीर्थ, धरोहर", "तीर्थक्षेत्र, वारसा")),
        it3("ayodhya", "Ayodhya", "अयोध्या", "अयोध्या", m=("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        it3("prayagraj", "Prayagraj and the Sangam", "प्रयागराज और संगम", "प्रयागराज व संगम", m=("Pilgrimage, Kumbh", "तीर्थ, कुंभ", "तीर्थक्षेत्र, कुंभ")),
        it3("braj", "Mathura and Vrindavan", "मथुरा और वृंदावन", "मथुरा व वृंदावन", m=("Krishna pilgrimage", "कृष्ण तीर्थ", "कृष्ण तीर्थक्षेत्र")),
        it3("lucknow", "Lucknow", "लखनऊ", "लखनौ", m=("Nawabi heritage, food", "नवाबी धरोहर, व्यंजन", "नवाबी वारसा, खाद्यपदार्थ")),
        it3("sikri", "Fatehpur Sikri", "फ़तेहपुर सीकरी", "फतेहपूर सिक्री", m=("UNESCO heritage", "यूनेस्को धरोहर", "युनेस्को वारसा")),
        it3("dudhwa", "Dudhwa National Park", "दुधवा राष्ट्रीय उद्यान", "दुधवा राष्ट्रीय उद्यान", m=("Wildlife (Nov–Jun)", "वन्यजीव (नवंबर–जून)", "वन्यजीव (नोव्हें.–जून)")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Agra: Taj Mahal at sunrise, Agra Fort, and Fatehpur Sikri.", "आगरा: सूर्योदय पर ताजमहल, आगरा क़िला और फ़तेहपुर सीकरी।", "आग्रा: सूर्योदयाला ताजमहाल, आग्र्याचा किल्ला आणि फतेहपूर सिक्री.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Varanasi: dawn boat on the ghats, Ganga aarti, Sarnath.", "वाराणसी: भोर में घाटों पर नौका, गंगा आरती, सारनाथ।", "वाराणसी: पहाटे घाटांवर नौकाविहार, गंगा आरती, सारनाथ.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Lucknow, Ayodhya and Varanasi by road or rail.", "सड़क या रेल से लखनऊ, अयोध्या और वाराणसी।", "रस्ता किंवा रेल्वेने लखनौ, अयोध्या व वाराणसी.")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Agra and Mathura–Vrindavan, then Lucknow, Prayagraj and Varanasi.", "आगरा और मथुरा–वृंदावन, फिर लखनऊ, प्रयागराज और वाराणसी।", "आग्रा व मथुरा–वृंदावन, नंतर लखनौ, प्रयागराज व वाराणसी.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("upt", "Uttar Pradesh Tourism (official)", "उत्तर प्रदेश पर्यटन (आधिकारिक)", "उत्तर प्रदेश पर्यटन (अधिकृत)", url="https://www.uptourism.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Tourist visits before 2022 and for 2025", "2022 से पहले और 2025 की पर्यटक यात्राएँ", "2022 पूर्वीच्या व 2025 च्या पर्यटक भेटी"), "tourism", "India Tourism Statistics."),
        (L("Earnings from tourism", "पर्यटन से आय", "पर्यटनातून उत्पन्न"), "tourism", "State tourism department."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Agra", "आगरा", "आग्रा"), ("Aligarh", "अलीगढ़", "अलीगढ"), ("Ambedkar Nagar", "अंबेडकर नगर", "आंबेडकर नगर"), ("Amethi", "अमेठी", "अमेठी"),
    ("Amroha", "अमरोहा", "अमरोहा"), ("Auraiya", "औरैया", "औरैया"), ("Ayodhya", "अयोध्या", "अयोध्या"), ("Azamgarh", "आज़मगढ़", "आझमगड"),
    ("Baghpat", "बागपत", "बागपत"), ("Bahraich", "बहराइच", "बहराइच"), ("Ballia", "बलिया", "बलिया"), ("Balrampur", "बलरामपुर", "बलरामपूर"),
    ("Banda", "बाँदा", "बांदा"), ("Barabanki", "बाराबंकी", "बाराबंकी"), ("Bareilly", "बरेली", "बरेली"), ("Basti", "बस्ती", "बस्ती"),
    ("Bhadohi", "भदोही", "भदोही"), ("Bijnor", "बिजनौर", "बिजनौर"), ("Budaun", "बदायूँ", "बदायूं"), ("Bulandshahr", "बुलंदशहर", "बुलंदशहर"),
    ("Chandauli", "चंदौली", "चंदौली"), ("Chitrakoot", "चित्रकूट", "चित्रकूट"), ("Deoria", "देवरिया", "देवरिया"), ("Etah", "एटा", "एटा"),
    ("Etawah", "इटावा", "इटावा"), ("Farrukhabad", "फ़र्रुख़ाबाद", "फर्रुखाबाद"), ("Fatehpur", "फ़तेहपुर", "फतेहपूर"), ("Firozabad", "फ़िरोज़ाबाद", "फिरोजाबाद"),
    ("Gautam Buddh Nagar", "गौतम बुद्ध नगर", "गौतमबुद्धनगर"), ("Ghaziabad", "ग़ाज़ियाबाद", "गाझियाबाद"), ("Ghazipur", "ग़ाज़ीपुर", "गाझीपूर"), ("Gonda", "गोंडा", "गोंडा"),
    ("Gorakhpur", "गोरखपुर", "गोरखपूर"), ("Hamirpur", "हमीरपुर", "हमीरपूर"), ("Hapur", "हापुड़", "हापूड"), ("Hardoi", "हरदोई", "हरदोई"),
    ("Hathras", "हाथरस", "हाथरस"), ("Jalaun", "जालौन", "जालौन"), ("Jaunpur", "जौनपुर", "जौनपूर"), ("Jhansi", "झाँसी", "झाशी"),
    ("Kannauj", "कन्नौज", "कनौज"), ("Kanpur Dehat", "कानपुर देहात", "कानपूर देहात"), ("Kanpur Nagar", "कानपुर नगर", "कानपूर नगर"), ("Kasganj", "कासगंज", "कासगंज"),
    ("Kaushambi", "कौशांबी", "कौशांबी"), ("Kushinagar", "कुशीनगर", "कुशीनगर"), ("Lakhimpur Kheri", "लखीमपुर खीरी", "लखीमपूर खेरी"), ("Lalitpur", "ललितपुर", "ललितपूर"),
    ("Lucknow", "लखनऊ", "लखनौ"), ("Maharajganj", "महराजगंज", "महाराजगंज"), ("Mahoba", "महोबा", "महोबा"), ("Mainpuri", "मैनपुरी", "मैनपुरी"),
    ("Mathura", "मथुरा", "मथुरा"), ("Mau", "मऊ", "मऊ"), ("Meerut", "मेरठ", "मेरठ"), ("Mirzapur", "मिर्ज़ापुर", "मिर्झापूर"),
    ("Moradabad", "मुरादाबाद", "मुरादाबाद"), ("Muzaffarnagar", "मुज़फ़्फ़रनगर", "मुजफ्फरनगर"), ("Pilibhit", "पीलीभीत", "पिलीभीत"), ("Pratapgarh", "प्रतापगढ़", "प्रतापगड"),
    ("Prayagraj", "प्रयागराज", "प्रयागराज"), ("Rae Bareli", "रायबरेली", "रायबरेली"), ("Rampur", "रामपुर", "रामपूर"), ("Saharanpur", "सहारनपुर", "सहारनपूर"),
    ("Sambhal", "संभल", "संभल"), ("Sant Kabir Nagar", "संत कबीर नगर", "संत कबीर नगर"), ("Shahjahanpur", "शाहजहाँपुर", "शाहजहानपूर"), ("Shamli", "शामली", "शामली"),
    ("Shravasti", "श्रावस्ती", "श्रावस्ती"), ("Siddharthnagar", "सिद्धार्थनगर", "सिद्धार्थनगर"), ("Sitapur", "सीतापुर", "सीतापूर"), ("Sonbhadra", "सोनभद्र", "सोनभद्र"),
    ("Sultanpur", "सुल्तानपुर", "सुलतानपूर"), ("Unnao", "उन्नाव", "उन्नाव"), ("Varanasi", "वाराणसी", "वाराणसी"),
]
assert len(DISTRICTS) == 75, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("lucknow", ("Lucknow", "लखनऊ", "लखनौ"), ("State capital; Nawabi architecture, chikankari, Awadhi cuisine; metro.", "राज्य की राजधानी; नवाबी स्थापत्य, चिकनकारी, अवधी व्यंजन; मेट्रो।", "राज्याची राजधानी; नवाबी स्थापत्य, चिकनकारी, अवधी खाद्यपदार्थ; मेट्रो."), ("Capital", "राजधानी", "राजधानी")),
        city("kanpur", ("Kanpur", "कानपुर", "कानपूर"), ("Industrial city on the Ganga; leather, textiles; IIT Kanpur.", "गंगा किनारे औद्योगिक शहर; चमड़ा, कपड़ा; आईआईटी कानपुर।", "गंगाकाठचे औद्योगिक शहर; चामडे, कापड; आयआयटी कानपूर."), ("Industry", "उद्योग", "उद्योग")),
        city("ghaziabad", ("Ghaziabad and Noida", "ग़ाज़ियाबाद और नोएडा", "गाझियाबाद व नोएडा"), ("Delhi-region cities: electronics, IT, media and housing.", "दिल्ली क्षेत्र के शहर: इलेक्ट्रॉनिक्स, आईटी, मीडिया और आवास।", "दिल्ली परिसरातील शहरे: इलेक्ट्रॉनिक्स, आयटी, माध्यमे व गृहनिर्माण."), ("NCR", "एनसीआर", "एनसीआर")),
        city("agra", ("Agra", "आगरा", "आग्रा"), ("Taj Mahal, Agra Fort; leather footwear and marble inlay.", "ताजमहल, आगरा क़िला; चमड़े के जूते और संगमरमर पच्चीकारी।", "ताजमहाल, आग्र्याचा किल्ला; चामडी पादत्राणे व संगमरवरी जडावकाम."), ("Heritage", "धरोहर", "वारसा")),
        city("varanasi", ("Varanasi", "वाराणसी", "वाराणसी"), ("Ancient city of the ghats; BHU; silk and music.", "घाटों का प्राचीन नगर; बीएचयू; रेशम और संगीत।", "घाटांची प्राचीन नगरी; बीएचयू; रेशीम व संगीत."), ("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        city("prayagraj", ("Prayagraj", "प्रयागराज", "प्रयागराज"), ("Sangam and Kumbh; High Court; university town.", "संगम और कुंभ; उच्च न्यायालय; विश्वविद्यालय नगर।", "संगम व कुंभ; उच्च न्यायालय; विद्यापीठ नगरी."), ("Pilgrimage, justice", "तीर्थ, न्याय", "तीर्थक्षेत्र, न्याय")),
        city("meerut", ("Meerut", "मेरठ", "मेरठ"), ("Sports goods, scissors; where the 1857 uprising began.", "खेल का सामान, कैंची; जहाँ 1857 का विद्रोह शुरू हुआ।", "क्रीडासाहित्य, कात्री; 1857 चा उठाव जिथे सुरू झाला."), ("Industry, history", "उद्योग, इतिहास", "उद्योग, इतिहास")),
        city("gorakhpur", ("Gorakhpur", "गोरखपुर", "गोरखपूर"), ("Gorakhnath temple; Gita Press; AIIMS; terracotta craft.", "गोरखनाथ मंदिर; गीता प्रेस; एम्स; टेराकोटा शिल्प।", "गोरखनाथ मंदिर; गीता प्रेस; एम्स; टेराकोटा कला."), ("Purvanchal", "पूर्वांचल", "पूर्वांचल")),
        city("bareilly", ("Bareilly", "बरेली", "बरेली"), ("Zari-zardozi, cane and bamboo crafts.", "ज़री-ज़रदोज़ी, बेंत और बाँस शिल्प।", "जरी-जरदोजी, वेत व बांबू कला."), ("Rohilkhand", "रुहेलखंड", "रोहिलखंड")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 75 districts (alphabetical)", "75 ज़िले (वर्णानुक्रम)", "75 जिल्हे (वर्णक्रमानुसार)"), src="up-des", url=UPF, conf="Official", access=TODAY),
    gaps("g", [
        (L("District populations (Census 2011)", "ज़िलावार जनसंख्या (जनगणना 2011)", "जिल्हानिहाय लोकसंख्या (जनगणना 2011)"), "census", "District Census Handbooks."),
        (L("The 18 divisions and their districts", "18 मंडल और उनके ज़िले", "18 विभाग व त्यांचे जिल्हे"), "up-des", "Revenue Department list."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Uttar Pradesh is the home of Indian hockey's greatest name, Major Dhyan Chand, who grew up in Jhansi; his birthday, 29 August, is India's National Sports Day, and Meerut hosts a sports university named after him. Meerut is also a national centre for cricket bats, balls and other sports goods. Cricket is followed everywhere, with international venues at Green Park in Kanpur and the Ekana stadium in Lucknow. Wrestling in village akharas — especially around Varanasi and the west — and kabaddi have deep roots, and the State has produced Olympic medallists and world-class athletes in hockey, wrestling, shooting and athletics.",
        "उत्तर प्रदेश भारतीय हॉकी के सबसे बड़े नाम, मेजर ध्यानचंद का घर है, जो झाँसी में पले-बढ़े; उनका जन्मदिन, 29 अगस्त, भारत का राष्ट्रीय खेल दिवस है, और मेरठ में उनके नाम पर एक खेल विश्वविद्यालय है। मेरठ क्रिकेट बल्ले, गेंद और अन्य खेल सामग्री का भी राष्ट्रीय केंद्र है। क्रिकेट हर जगह देखा जाता है, और कानपुर के ग्रीन पार्क व लखनऊ के इकाना स्टेडियम में अंतरराष्ट्रीय मैदान हैं। गाँवों के अखाड़ों में कुश्ती — ख़ासकर वाराणसी और पश्चिम में — और कबड्डी की जड़ें गहरी हैं, और राज्य ने हॉकी, कुश्ती, निशानेबाज़ी और एथलेटिक्स में ओलंपिक पदक विजेता और विश्व स्तरीय खिलाड़ी दिए हैं।",
        "उत्तर प्रदेश हे भारतीय हॉकीतील सर्वांत मोठे नाव, मेजर ध्यानचंद यांचे घर आहे; ते झाशीत लहानाचे मोठे झाले. त्यांचा जन्मदिवस, 29 ऑगस्ट, हा भारताचा राष्ट्रीय क्रीडा दिन आहे, आणि मेरठमध्ये त्यांच्या नावाने क्रीडा विद्यापीठ आहे. मेरठ हे क्रिकेट बॅट, चेंडू व इतर क्रीडासाहित्याचे राष्ट्रीय केंद्रही आहे. क्रिकेट सर्वत्र पाहिले जाते, आणि कानपूरचे ग्रीन पार्क व लखनौचे इकाना स्टेडियम ही आंतरराष्ट्रीय मैदाने आहेत. गावातील आखाड्यांतील कुस्ती — विशेषतः वाराणसी व पश्चिम भागात — आणि कबड्डीची मुळे खोल आहेत, आणि राज्याने हॉकी, कुस्ती, नेमबाजी व अॅथलेटिक्समध्ये ऑलिम्पिक पदकविजेते व जागतिक दर्जाचे खेळाडू दिले आहेत."),
        conf="Editorial"),
    lst("venues", [
        it3("ekana", "BRSABV Ekana Cricket Stadium, Lucknow", "बीआरएसएबीवी इकाना क्रिकेट स्टेडियम, लखनऊ", "बीआरएसएबीव्ही इकाना क्रिकेट स्टेडियम, लखनौ"),
        it3("greenpark", "Green Park Stadium, Kanpur", "ग्रीन पार्क स्टेडियम, कानपुर", "ग्रीन पार्क स्टेडियम, कानपूर"),
        it3("dhyanchand", "Major Dhyan Chand Sports University, Meerut", "मेजर ध्यानचंद खेल विश्वविद्यालय, मेरठ", "मेजर ध्यानचंद क्रीडा विद्यापीठ, मेरठ"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from UP (official list)", "उत्तर प्रदेश के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "उत्तर प्रदेशचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Sports Authority of India / State sports department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("kabir", ("Kabir", "कबीर", "कबीर"), ("15th-century poet-saint of Varanasi whose dohas challenged ritual and caste.", "15वीं सदी के वाराणसी के संत-कवि, जिनके दोहों ने कर्मकांड और जाति को चुनौती दी।", "पंधराव्या शतकातील वाराणसीचे संतकवी; त्यांच्या दोह्यांनी कर्मकांड व जातिभेदाला आव्हान दिले."), ("Literature", "साहित्य", "साहित्य")),
        person("tulsidas", ("Tulsidas", "तुलसीदास", "तुलसीदास"), ("Poet of the Ramcharitmanas in Awadhi.", "अवधी में रामचरितमानस के कवि।", "अवधीतील रामचरितमानसाचे कवी."), ("Literature", "साहित्य", "साहित्य")),
        person("ravidas", ("Guru Ravidas", "गुरु रविदास", "गुरू रविदास"), ("Bhakti poet-saint of Varanasi; his hymns are part of the Guru Granth Sahib.", "वाराणसी के भक्ति संत-कवि; उनके पद गुरु ग्रंथ साहिब में शामिल हैं।", "वाराणसीचे भक्ती संतकवी; त्यांची पदे गुरू ग्रंथ साहिबात समाविष्ट आहेत."), ("Spiritual", "आध्यात्मिक", "आध्यात्मिक")),
        person("lakshmibai", ("Rani Lakshmibai", "रानी लक्ष्मीबाई", "राणी लक्ष्मीबाई"), ("Queen of Jhansi and a leader of the 1857 uprising.", "झाँसी की रानी और 1857 के विद्रोह की नेता।", "झाशीची राणी आणि 1857 च्या उठावाची नेता."), ("History", "इतिहास", "इतिहास")),
        person("premchand", ("Munshi Premchand", "मुंशी प्रेमचंद", "मुन्शी प्रेमचंद"), ("Hindi–Urdu novelist of village India: Godaan, Nirmala, Idgah.", "ग्रामीण भारत के हिंदी–उर्दू उपन्यासकार: गोदान, निर्मला, ईदगाह।", "ग्रामीण भारताचे हिंदी–उर्दू कादंबरीकार: गोदान, निर्मला, ईदगाह."), ("Literature", "साहित्य", "साहित्य")),
        person("nehru", ("Jawaharlal Nehru", "जवाहरलाल नेहरू", "जवाहरलाल नेहरू"), ("Born in Allahabad (Prayagraj); first Prime Minister of India (1947–64).", "इलाहाबाद (प्रयागराज) में जन्मे; भारत के पहले प्रधानमंत्री (1947–64)।", "अलाहाबाद (प्रयागराज) येथे जन्म; भारताचे पहिले पंतप्रधान (1947–64)."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("shastri", ("Lal Bahadur Shastri", "लाल बहादुर शास्त्री", "लाल बहादूर शास्त्री"), ("Born at Mughalsarai; Prime Minister (1964–66), 'Jai Jawan, Jai Kisan'.", "मुग़लसराय में जन्मे; प्रधानमंत्री (1964–66), 'जय जवान, जय किसान'।", "मुघलसराय येथे जन्म; पंतप्रधान (1964–66), 'जय जवान, जय किसान'."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("bismillah", ("Ustad Bismillah Khan", "उस्ताद बिस्मिल्लाह ख़ाँ", "उस्ताद बिस्मिल्ला खाँ"), ("Shehnai maestro of Varanasi; Bharat Ratna 2001.", "वाराणसी के शहनाई उस्ताद; भारत रत्न 2001।", "वाराणसीचे सनईवादक उस्ताद; भारतरत्न 2001."), ("Music", "संगीत", "संगीत")),
        person("ravishankar", ("Pandit Ravi Shankar", "पंडित रवि शंकर", "पंडित रविशंकर"), ("Sitar maestro born in Varanasi; Bharat Ratna 1999.", "वाराणसी में जन्मे सितार उस्ताद; भारत रत्न 1999।", "वाराणसीत जन्मलेले सतारवादक; भारतरत्न 1999."), ("Music", "संगीत", "संगीत")),
        person("mahadevi", ("Mahadevi Varma", "महादेवी वर्मा", "महादेवी वर्मा"), ("Chhayavad poet of Prayagraj; Jnanpith Award 1982.", "प्रयागराज की छायावादी कवयित्री; 1982 का ज्ञानपीठ पुरस्कार।", "प्रयागराजच्या छायावादी कवयित्री; 1982 चा ज्ञानपीठ पुरस्कार."), ("Literature", "साहित्य", "साहित्य")),
        person("dhyanchand", ("Major Dhyan Chand", "मेजर ध्यानचंद", "मेजर ध्यानचंद"), ("Hockey legend; three Olympic gold medals (1928, 1932, 1936).", "हॉकी के महानायक; तीन ओलंपिक स्वर्ण पदक (1928, 1932, 1936)।", "हॉकीतील महानायक; तीन ऑलिम्पिक सुवर्णपदके (1928, 1932, 1936)."), ("Sport", "खेल", "क्रीडा")),
        person("birju", ("Pandit Birju Maharaj", "पंडित बिरजू महाराज", "पंडित बिरजू महाराज"), ("Kathak maestro of the Lucknow gharana.", "लखनऊ घराने के कथक उस्ताद।", "लखनौ घराण्याचे कथक नर्तक."), ("Dance", "नृत्य", "नृत्य")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "From the 1830s to 1917, hundreds of thousands of indentured labourers — girmitiyas — sailed from eastern Uttar Pradesh and western Bihar to sugar colonies in Mauritius, Fiji, Trinidad and Tobago, Guyana, Suriname and South Africa. Their descendants form large communities there today, and Bhojpuri and Awadhi-based languages, Ramayana recitation and festivals such as Diwali and Phagwah (Holi) remain part of life. Since the 1970s many workers from the State have migrated to the Gulf countries, and within India people from Uttar Pradesh form some of the largest migrant communities in Delhi, Mumbai, Punjab and Gujarat.",
        "1830 के दशक से 1917 तक लाखों गिरमिटिया मज़दूर पूर्वी उत्तर प्रदेश और पश्चिमी बिहार से मॉरीशस, फ़िजी, त्रिनिदाद और टोबैगो, गयाना, सूरीनाम और दक्षिण अफ़्रीका के गन्ना उपनिवेशों में गए। उनके वंशज आज वहाँ बड़े समुदाय हैं, और भोजपुरी व अवधी आधारित भाषाएँ, रामायण पाठ और दीवाली व फगवा (होली) जैसे त्योहार वहाँ के जीवन का हिस्सा हैं। 1970 के दशक से राज्य के बहुत से श्रमिक खाड़ी देशों में गए हैं, और भारत के भीतर उत्तर प्रदेश के लोग दिल्ली, मुंबई, पंजाब और गुजरात में सबसे बड़े प्रवासी समुदायों में हैं।",
        "1830 च्या दशकापासून 1917 पर्यंत लाखो करारबद्ध मजूर — गिरमिटिया — पूर्व उत्तर प्रदेश व पश्चिम बिहारमधून मॉरिशस, फिजी, त्रिनिदाद व टोबॅगो, गयाना, सुरिनाम व दक्षिण आफ्रिकेतील उसाच्या वसाहतींत गेले. त्यांचे वंशज आज तिथे मोठे समुदाय आहेत, आणि भोजपुरी व अवधी आधारित भाषा, रामायण पठण आणि दिवाळी व फगवा (होळी) यांसारखे सण तिथल्या जीवनाचा भाग आहेत. 1970 च्या दशकापासून राज्यातील अनेक कामगार आखाती देशांत गेले आहेत, आणि भारतातच उत्तर प्रदेशचे लोक दिल्ली, मुंबई, पंजाब व गुजरातमधील सर्वांत मोठ्या स्थलांतरित समुदायांपैकी आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants and internal migrants", "प्रवासियों और आंतरिक प्रवासियों की संख्या", "परदेशी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; MEA."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Uttar Pradesh portal", "उत्तर प्रदेश सरकार पोर्टल", "उत्तर प्रदेश शासन संकेतस्थळ", url="https://up.gov.in", src="india-gov"),
        it3("edistrict", "e-District Uttar Pradesh — certificates and services", "ई-डिस्ट्रिक्ट उत्तर प्रदेश — प्रमाणपत्र और सेवाएँ", "ई-डिस्ट्रिक्ट उत्तर प्रदेश — प्रमाणपत्रे व सेवा", url="https://edistrict.up.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Uttar Pradesh Tourism", "उत्तर प्रदेश पर्यटन", "उत्तर प्रदेश पर्यटन", url="https://www.uptourism.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Lucknow", "लखनऊ", "लखनौ"), "0522"], [L("Kanpur", "कानपुर", "कानपूर"), "0512"], [L("Agra", "आगरा", "आग्रा"), "0562"],
           [L("Varanasi", "वाराणसी", "वाराणसी"), "0542"], [L("Prayagraj", "प्रयागराज", "प्रयागराज"), "0532"], [L("Meerut", "मेरठ", "मेरठ"), "0121"],
           [L("Gorakhpur", "गोरखपुर", "गोरखपूर"), "0551"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [(L("Verified local business directory", "सत्यापित स्थानीय व्यवसाय निर्देशिका", "पडताळलेली स्थानिक उद्योग सूची"), "india-gov", "Udyam Registration, ODOP clusters and co-operative registrars.")]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("pop", ("At the 2011 Census, about one in six Indians lived in Uttar Pradesh — 19.98 crore people.", "2011 की जनगणना में लगभग हर छठा भारतीय उत्तर प्रदेश में रहता था — 19.98 करोड़ लोग।", "2011 च्या जनगणनेत जवळपास दर सहावा भारतीय उत्तर प्रदेशात राहत होता — 19.98 कोटी लोक."), UPF, "up-des"),
        triv("gi", ("With 78 registered GIs, it has the most of any State in this directory; more than twenty are from Varanasi.", "78 पंजीकृत जीआई के साथ इस निर्देशिका में सबसे अधिक इसी राज्य के हैं; बीस से अधिक वाराणसी के हैं।", "78 नोंदणीकृत जीआयसह या सूचीत सर्वाधिक याच राज्याची आहेत; वीसहून अधिक वाराणसीची आहेत."), GI_PDF, "gi-registry"),
        triv("ganga", ("The Ganga Expressway (2026) runs 594 km from Meerut to Prayagraj through 12 districts.", "गंगा एक्सप्रेसवे (2026) मेरठ से प्रयागराज तक 12 ज़िलों से होकर 594 किमी जाता है।", "गंगा द्रुतगती मार्ग (2026) मेरठपासून प्रयागराजपर्यंत 12 जिल्ह्यांतून 594 किमी जातो."), GANGA, "newsonair"),
        triv("ls", ("It elects 80 members to the Lok Sabha — more than any other State.", "यह लोकसभा में 80 सदस्य भेजता है — किसी भी अन्य राज्य से अधिक।", "ते लोकसभेवर 80 सदस्य पाठवते — इतर कोणत्याही राज्यापेक्षा जास्त.")),
        triv("dhyan", ("National Sports Day, 29 August, marks the birthday of hockey legend Major Dhyan Chand.", "राष्ट्रीय खेल दिवस, 29 अगस्त, हॉकी के महानायक मेजर ध्यानचंद का जन्मदिन है।", "राष्ट्रीय क्रीडा दिन, 29 ऑगस्ट, हा हॉकीतील महानायक मेजर ध्यानचंद यांचा जन्मदिवस आहे.")),
        triv("kumbh", ("The Kumbh Mela is on UNESCO's list of the Intangible Cultural Heritage of Humanity (2017).", "कुंभ मेला यूनेस्को की मानवता की अमूर्त सांस्कृतिक धरोहर सूची में है (2017)।", "कुंभमेळा युनेस्कोच्या मानवतेच्या अमूर्त सांस्कृतिक वारसा यादीत आहे (2017).")),
        triv("sarnath", ("Sarnath, where the Buddha gave his first sermon, became a UNESCO World Heritage Site in 2026.", "सारनाथ, जहाँ बुद्ध ने पहला उपदेश दिया, 2026 में यूनेस्को विश्व धरोहर स्थल बना।", "बुद्धांनी जिथे पहिले प्रवचन दिले ते सारनाथ 2026 मध्ये युनेस्को जागतिक वारसा स्थळ झाले."), UNESCO, "unesco-whc"),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("up mod3 ok")
