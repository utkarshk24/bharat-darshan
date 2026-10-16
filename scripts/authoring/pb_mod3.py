"""Punjab modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-PB"
pb = read("regions/IN-PB.json")["metrics"]; ind = read("india.json")["metrics"]

RAMSAR_PB = [
    ("Harike Lake", "हरिके झील", "हरिके सरोवर", "1990", "4,100"),
    ("Kanjli Lake", "कांजली झील", "कांजली सरोवर", "2002", "183"),
    ("Ropar Lake", "रोपड़ झील", "रोपड सरोवर", "2002", "1,365"),
    ("Beas Conservation Reserve", "ब्यास संरक्षण आरक्षित क्षेत्र", "बियास संवर्धन राखीव क्षेत्र", "2019", "6,429"),
    ("Keshopur-Miani Community Reserve", "केशोपुर-मियानी सामुदायिक आरक्षित क्षेत्र", "केशोपूर-मियानी सामुदायिक राखीव क्षेत्र", "2019", "344"),
    ("Nangal Wildlife Sanctuary", "नंगल वन्यजीव अभयारण्य", "नांगल वन्यजीव अभयारण्य", "2019", "116"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Only about 3.7% of Punjab is forest (ISFR 2023) — among the lowest shares of any State — mostly in the Shivalik foothills of Hoshiarpur, Ropar and Pathankot. Its wetlands are its natural treasures: Harike, where the Sutlej and Beas meet, is one of the largest wetlands of northern India and a winter home for migratory waterbirds, and the Beas Conservation Reserve shelters a small population of the Indus river dolphin and reintroduced gharials. The blackbuck, the State animal, survives in the Abohar Wildlife Sanctuary, protected by the Bishnoi community.\n\nPunjab has six Ramsar sites: Harike, Kanjli, Ropar, the Beas Conservation Reserve, the Keshopur-Miani Community Reserve and Nangal.",
        "पंजाब का केवल लगभग 3.7% भाग वन है (आईएसएफ़आर 2023) — राज्यों में सबसे कम हिस्सों में — जो अधिकतर होशियारपुर, रोपड़ और पठानकोट की शिवालिक तलहटी में है। इसकी आर्द्रभूमियाँ इसकी प्राकृतिक धरोहर हैं: हरिके, जहाँ सतलुज और ब्यास मिलती हैं, उत्तर भारत की सबसे बड़ी आर्द्रभूमियों में से एक है और प्रवासी जलपक्षियों का शीतकालीन घर है, और ब्यास संरक्षण आरक्षित क्षेत्र में सिंधु नदी डॉल्फ़िन की छोटी आबादी और फिर से बसाए गए घड़ियाल हैं। राज्य पशु काला हिरण बिश्नोई समुदाय द्वारा संरक्षित अबोहर वन्यजीव अभयारण्य में बचा है।\n\nपंजाब में छह रामसर स्थल हैं: हरिके, कांजली, रोपड़, ब्यास संरक्षण आरक्षित क्षेत्र, केशोपुर-मियानी सामुदायिक आरक्षित क्षेत्र और नंगल।",
        "पंजाबचा केवळ सुमारे 3.7% भाग वनाच्छादित आहे (आयएसएफआर 2023) — राज्यांतील सर्वांत कमी वाट्यांपैकी — बहुतांश होशियारपूर, रोपड व पठाणकोटच्या शिवालिक पायथ्याशी. त्याची पाणथळे हा त्याचा नैसर्गिक ठेवा आहे: सतलज व बियास जिथे मिळतात ते हरिके हे उत्तर भारतातील सर्वांत मोठ्या पाणथळांपैकी एक असून स्थलांतरित पाणपक्ष्यांचे हिवाळी घर आहे, आणि बियास संवर्धन राखीव क्षेत्रात सिंधू नदी डॉल्फिनची लहान संख्या व पुन्हा सोडलेले घडियाल आहेत. राज्यप्राणी काळवीट बिश्नोई समुदायाने जपलेल्या अबोहर वन्यजीव अभयारण्यात टिकून आहे.\n\nपंजाबमध्ये सहा रामसर स्थळे आहेत: हरिके, कांजली, रोपड, बियास संवर्धन राखीव क्षेत्र, केशोपूर-मियानी सामुदायिक राखीव क्षेत्र व नांगल."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(1846.09, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(1846.54, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), pb["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(6, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_PB], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026 (year of designation).", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची (घोषणा वर्ष)।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी (घोषणा वर्ष).")),
    lst("protected", [
        it3("harike", "Harike Wildlife Sanctuary", "हरिके वन्यजीव अभयारण्य", "हरिके वन्यजीव अभयारण्य", m=("Sutlej–Beas confluence", "सतलुज–ब्यास संगम", "सतलज–बियास संगम")),
        it3("beas", "Beas Conservation Reserve", "ब्यास संरक्षण आरक्षित क्षेत्र", "बियास संवर्धन राखीव क्षेत्र", m=("Indus river dolphin", "सिंधु नदी डॉल्फ़िन", "सिंधू नदी डॉल्फिन")),
        it3("abohar", "Abohar Wildlife Sanctuary", "अबोहर वन्यजीव अभयारण्य", "अबोहर वन्यजीव अभयारण्य", m=("Blackbuck", "काला हिरण", "काळवीट")),
        it3("bir", "Bir Moti Bagh and Bir Bhunerheri", "बीड़ मोती बाग़ और बीड़ भुनेरहेड़ी", "बीड मोती बाग व बीड भुनेरहेडी", m=("Patiala", "पटियाला", "पटियाळा")),
        it3("takhni", "Takhni–Rehmapur Wildlife Sanctuary", "तख़्नी–रहमापुर वन्यजीव अभयारण्य", "तख्नी–रहमापूर वन्यजीव अभयारण्य", m=("Shivalik foothills", "शिवालिक तलहटी", "शिवालिक पायथा")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("blackbuck", "Blackbuck (State animal)", "काला हिरण (राज्य पशु)", "काळवीट (राज्यप्राणी)"), it3("dolphin", "Indus river dolphin", "सिंधु नदी डॉल्फ़िन", "सिंधू नदी डॉल्फिन"),
        it3("gharial", "Gharial (reintroduced)", "घड़ियाल (फिर से बसाया गया)", "घडियाल (पुन्हा सोडलेला)"), it3("baaz", "Northern goshawk (baaz, State bird)", "बाज़ (राज्य पक्षी)", "ससाणा (बाज, राज्यपक्षी)"),
        it3("sambar", "Sambar", "सांभर", "सांबर"), it3("waterbirds", "Migratory waterbirds", "प्रवासी जलपक्षी", "स्थलांतरित पाणपक्षी"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Indus river dolphin count", "सिंधु नदी डॉल्फ़िन की संख्या", "सिंधू नदी डॉल्फिनची संख्या"), "moefcc", "Punjab Forest and Wildlife Department / WWF-India survey."),
        (L("Waterbird census at Harike", "हरिके में जलपक्षी गणना", "हरिके येथील पाणपक्षी गणना"), "india-gov", "Punjab Forest Department annual census."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Punjab's farms are watered by an extensive canal network fed by the Sutlej, Beas and Ravi — including canals from the Ropar and Harike headworks and the Bhakra main line — and, above all, by groundwater pumped by well over a million tubewells. The intensive wheat–paddy rotation has drawn the water table down sharply across most of the State, and most of its groundwater blocks are classed as over-exploited; the State has promoted direct-seeded rice and crop diversification in response. Sharing of river waters with neighbouring States, including the long-pending Sutlej–Yamuna Link canal, remains a political and legal issue. Floods from the rivers and the Ghaggar caused heavy damage in 2023 and 2025.",
        "पंजाब के खेत सतलुज, ब्यास और रावी से निकली व्यापक नहर प्रणाली से सींचे जाते हैं — जिसमें रोपड़ और हरिके हेडवर्क्स की नहरें और भाखड़ा मुख्य नहर शामिल हैं — और सबसे बढ़कर दस लाख से कहीं अधिक ट्यूबवेलों से खींचे गए भूजल से। सघन गेहूँ–धान चक्र ने राज्य के अधिकांश भाग में जल स्तर तेज़ी से नीचे गिराया है, और इसके अधिकांश भूजल ब्लॉक अति-दोहित श्रेणी में हैं; जवाब में राज्य ने धान की सीधी बुवाई और फ़सल विविधीकरण को बढ़ावा दिया है। पड़ोसी राज्यों के साथ नदी जल बँटवारा, जिसमें लंबे समय से लंबित सतलुज–यमुना लिंक नहर भी है, एक राजनीतिक और क़ानूनी मुद्दा बना हुआ है। नदियों और घग्गर की बाढ़ ने 2023 और 2025 में भारी नुकसान किया।",
        "पंजाबची शेती सतलज, बियास व रावीतून निघणाऱ्या विस्तृत कालवा जाळ्याने — ज्यात रोपड व हरिके हेडवर्क्सचे कालवे व भाक्रा मुख्य कालवा आहेत — आणि सर्वांत मुख्य म्हणजे दहा लाखांहून बऱ्याच अधिक कूपनलिकांनी उपसलेल्या भूजलाने भिजते. सघन गहू–भात चक्राने राज्याच्या बहुतांश भागात भूजल पातळी वेगाने खाली नेली आहे, आणि त्याचे बहुतेक भूजल गट अतिउपसा श्रेणीत आहेत; प्रत्युत्तरादाखल राज्याने भाताची थेट पेरणी व पीक वैविध्याला प्रोत्साहन दिले आहे. शेजारी राज्यांसोबतचे नदी पाणीवाटप, ज्यात दीर्घकाळ प्रलंबित सतलज–यमुना जोड कालवाही आहे, हा राजकीय व कायदेशीर मुद्दा राहिला आहे. नद्या व घग्गरच्या पुरांनी 2023 व 2025 मध्ये मोठे नुकसान केले."),
        conf="Editorial"),
    gaps("g", [
        (L("Groundwater stage of extraction and over-exploited blocks", "भूजल दोहन का स्तर और अति-दोहित ब्लॉक", "भूजल उपशाचा टप्पा व अतिउपसा गट"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Number of agricultural tubewells", "कृषि ट्यूबवेलों की संख्या", "शेती कूपनलिकांची संख्या"), "india-gov", "Minor Irrigation Census / PSPCL."),
        (L("Flood damage, 2023 and 2025", "बाढ़ से नुकसान, 2023 और 2025", "पुरामुळे नुकसान, 2023 व 2025"), "india-gov", "Punjab Revenue and Disaster Management Department."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Floods are Punjab's main natural hazard in the monsoon, when heavy rain in the hills and dam releases swell the Sutlej, Beas, Ravi and Ghaggar. In winter, dense fog makes road and rail travel dangerous, and in October–November smoke from burning paddy stubble worsens air quality across the region. Summers bring heatwaves and dust storms. The north-east of the State lies in a moderately high earthquake zone.\n\nAreas along the international border have security restrictions; visitors to the Attari–Wagah ceremony should follow the instructions of the Border Security Force.",
        "मानसून में बाढ़ पंजाब का मुख्य प्राकृतिक ख़तरा है, जब पहाड़ों में भारी वर्षा और बाँधों से छोड़ा गया पानी सतलुज, ब्यास, रावी और घग्गर को उफना देता है। सर्दियों में घना कोहरा सड़क और रेल यात्रा को ख़तरनाक बनाता है, और अक्टूबर–नवंबर में धान की पराली जलाने का धुआँ पूरे क्षेत्र की वायु गुणवत्ता बिगाड़ता है। गर्मियों में लू और आँधियाँ आती हैं। राज्य का उत्तर-पूर्व अपेक्षाकृत ऊँचे भूकंपीय क्षेत्र में है।\n\nअंतरराष्ट्रीय सीमा के साथ के क्षेत्रों में सुरक्षा प्रतिबंध हैं; अटारी–वाघा समारोह में जाने वाले पर्यटकों को सीमा सुरक्षा बल के निर्देश मानने चाहिए।",
        "मान्सूनमध्ये पूर हा पंजाबवरील मुख्य नैसर्गिक धोका आहे, जेव्हा डोंगरांतील मुसळधार पाऊस व धरणांतून सोडलेले पाणी सतलज, बियास, रावी व घग्गरला फुगवते. हिवाळ्यात दाट धुके रस्ते व रेल्वे प्रवास धोकादायक करते, आणि ऑक्टोबर–नोव्हेंबरमध्ये भाताचे तण जाळण्याचा धूर संपूर्ण प्रदेशातील हवेची गुणवत्ता खालावतो. उन्हाळ्यात उष्णतेच्या लाटा व धुळीची वादळे येतात. राज्याचा ईशान्य भाग तुलनेने अधिक भूकंपप्रवण क्षेत्रात आहे.\n\nआंतरराष्ट्रीय सीमेलगतच्या भागांत सुरक्षाविषयक निर्बंध आहेत; अटारी–वाघा सोहळ्याला जाणाऱ्या पर्यटकांनी सीमा सुरक्षा दलाच्या सूचना पाळाव्यात."),
        conf="Editorial"),
    emergency_table(("Punjab", "पंजाब", "पंजाब")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official address."),
        (L("Stubble-burning incidents by season", "मौसमवार पराली जलाने की घटनाएँ", "हंगामनिहाय तण जाळण्याच्या घटना"), "india-gov", "Punjab Remote Sensing Centre / CAQM."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Punjab appears in two entries of the GI Registry's list as on 31 December 2025, both shared with neighbouring States. Phulkari, the 'flower work' embroidery of Punjabi women, was filed in 2005 for Punjab, Haryana and Rajasthan. Basmati rice, filed in 2008, is registered for the Indo-Gangetic plain of Punjab, Haryana, Himachal Pradesh, Delhi, Uttarakhand, western Uttar Pradesh and Jammu and Kashmir. No GI is registered for Punjab alone on this list.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची की दो प्रविष्टियों में पंजाब है, और दोनों पड़ोसी राज्यों के साथ साझा हैं। पंजाबी महिलाओं की 'फूलों का काम' कढ़ाई फुलकारी 2005 में पंजाब, हरियाणा और राजस्थान के लिए दायर हुई। 2008 में दायर बासमती चावल पंजाब, हरियाणा, हिमाचल प्रदेश, दिल्ली, उत्तराखंड, पश्चिमी उत्तर प्रदेश और जम्मू-कश्मीर के सिंधु-गंगा मैदान के लिए पंजीकृत है। इस सूची में केवल पंजाब के लिए कोई जीआई पंजीकृत नहीं है।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीतील दोन नोंदींत पंजाब आहे, आणि दोन्ही शेजारी राज्यांसोबत सामायिक आहेत. पंजाबी स्त्रियांचे 'फुलांचे काम' भरतकाम फुलकारी 2005 मध्ये पंजाब, हरियाणा व राजस्थानसाठी दाखल झाले. 2008 मध्ये दाखल बासमती तांदूळ पंजाब, हरियाणा, हिमाचल प्रदेश, दिल्ली, उत्तराखंड, पश्चिम उत्तर प्रदेश व जम्मू-काश्मीरच्या सिंधू-गंगा मैदानासाठी नोंदणीकृत आहे. या यादीत केवळ पंजाबसाठी एकही जीआय नोंदणीकृत नाही."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Pending GI applications from Punjab", "पंजाब के लंबित जीआई आवेदन", "पंजाबचे प्रलंबित जीआय अर्ज"), "gi-registry", "GI Registry application status search."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Amritsar is Punjab's great destination: the Harmandir Sahib, best seen at dawn or lit up at night, with its langar; Jallianwala Bagh; the Partition Museum; Gobindgarh Fort; and the evening ceremony at the Attari–Wagah border. Anandpur Sahib, with Takht Keshgarh Sahib and the Virasat-e-Khalsa museum, and Talwandi Sabo's Takht Damdama Sahib are major Sikh pilgrimage centres. Patiala's Qila Mubarak and Sheesh Mahal, Kapurthala's palaces, the Harike wetland, the Sufi shrine at Sirhind and the Shivalik foothills around Ropar and the Ranjit Sagar dam offer variety, and farm stays let visitors experience village life.",
        "अमृतसर पंजाब का सबसे बड़ा गंतव्य है: हरमंदिर साहिब, जिसे भोर में या रात की रोशनी में देखना सबसे अच्छा है, अपने लंगर के साथ; जलियाँवाला बाग़; विभाजन संग्रहालय; गोबिंदगढ़ क़िला; और अटारी–वाघा सीमा पर शाम का समारोह। तख़्त केसगढ़ साहिब और विरासत-ए-ख़ालसा संग्रहालय वाला आनंदपुर साहिब और तलवंडी साबो का तख़्त दमदमा साहिब प्रमुख सिख तीर्थ केंद्र हैं। पटियाला का क़िला मुबारक और शीश महल, कपूरथला के महल, हरिके आर्द्रभूमि, सरहिंद की सूफ़ी दरगाह और रोपड़ व रणजीत सागर बाँध के आसपास की शिवालिक तलहटी विविधता देती हैं, और फ़ार्म स्टे पर्यटकों को गाँव का जीवन अनुभव कराते हैं।",
        "अमृतसर हे पंजाबचे सर्वांत मोठे पर्यटनस्थळ आहे: हरमंदिर साहिब, जे पहाटे किंवा रात्रीच्या रोषणाईत पाहणे उत्तम, त्याच्या लंगरसह; जालियनवाला बाग; फाळणी संग्रहालय; गोविंदगड किल्ला; आणि अटारी–वाघा सीमेवरील संध्याकाळचा सोहळा. तख्त केसगड साहिब व विरासत-ए-खालसा संग्रहालय असलेले आनंदपूर साहिब आणि तलवंडी साबोचे तख्त दमदमा साहिब ही प्रमुख शीख तीर्थक्षेत्रे आहेत. पटियाळाचा किला मुबारक व शीश महल, कपूरथळ्याचे राजवाडे, हरिके पाणथळ, सरहिंदचा सूफी दर्गा आणि रोपड व रणजित सागर धरणाभोवतीचा शिवालिक पायथा वैविध्य देतात, आणि शेतमुक्काम पर्यटकांना गावजीवनाचा अनुभव देतात."),
        conf="Editorial"),
    lst("places", [
        it3("amritsar", "Amritsar", "अमृतसर", "अमृतसर", m=("Golden Temple; Jallianwala Bagh", "स्वर्ण मंदिर; जलियाँवाला बाग़", "सुवर्ण मंदिर; जालियनवाला बाग")),
        it3("wagah", "Attari–Wagah border", "अटारी–वाघा सीमा", "अटारी–वाघा सीमा", m=("Beating retreat ceremony", "बीटिंग रिट्रीट समारोह", "बीटिंग रिट्रीट सोहळा")),
        it3("anandpur", "Anandpur Sahib", "आनंदपुर साहिब", "आनंदपूर साहिब", m=("Virasat-e-Khalsa; Hola Mohalla", "विरासत-ए-ख़ालसा; होला मोहल्ला", "विरासत-ए-खालसा; होला मोहल्ला")),
        it3("patiala", "Patiala", "पटियाला", "पटियाळा", m=("Qila Mubarak; Sheesh Mahal", "क़िला मुबारक; शीश महल", "किला मुबारक; शीश महल")),
        it3("kapurthala", "Kapurthala", "कपूरथला", "कपूरथळा", m=("Palaces and gardens", "महल और उद्यान", "राजवाडे व उद्याने")),
        it3("harike", "Harike wetland", "हरिके आर्द्रभूमि", "हरिके पाणथळ", m=("Birdwatching in winter", "सर्दियों में पक्षी दर्शन", "हिवाळ्यात पक्षीनिरीक्षण")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Amritsar: Golden Temple at dawn and night, Jallianwala Bagh, Partition Museum and Attari–Wagah.", "अमृतसर: भोर और रात में स्वर्ण मंदिर, जलियाँवाला बाग़, विभाजन संग्रहालय और अटारी–वाघा।", "अमृतसर: पहाटे व रात्री सुवर्ण मंदिर, जालियनवाला बाग, फाळणी संग्रहालय व अटारी–वाघा.")),
        it3("d4", "4 days", "4 दिन", "4 दिवस", d=("Amritsar and Kapurthala, then Anandpur Sahib.", "अमृतसर और कपूरथला, फिर आनंदपुर साहिब।", "अमृतसर व कपूरथळा, नंतर आनंदपूर साहिब.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Amritsar, Harike, Patiala and a village farm stay.", "अमृतसर, हरिके, पटियाला और गाँव में फ़ार्म स्टे।", "अमृतसर, हरिके, पटियाळा व गावात शेतमुक्काम.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("pt", "Punjab Tourism (official)", "पंजाब पर्यटन (आधिकारिक)", "पंजाब पर्यटन (अधिकृत)", url="https://punjabtourism.punjab.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Amritsar", "अमृतसर", "अमृतसर"), ("Barnala", "बरनाला", "बरनाला"), ("Bathinda", "बठिंडा", "भटिंडा"), ("Faridkot", "फ़रीदकोट", "फरीदकोट"), ("Fatehgarh Sahib", "फ़तेहगढ़ साहिब", "फतेहगड साहिब"),
    ("Fazilka", "फ़ाज़िल्का", "फाजिल्का"), ("Ferozepur", "फ़िरोज़पुर", "फिरोजपूर"), ("Gurdaspur", "गुरदासपुर", "गुरदासपूर"), ("Hoshiarpur", "होशियारपुर", "होशियारपूर"), ("Jalandhar", "जालंधर", "जालंधर"),
    ("Kapurthala", "कपूरथला", "कपूरथळा"), ("Ludhiana", "लुधियाना", "लुधियाना"), ("Malerkotla", "मलेरकोटला", "मलेरकोटला"), ("Mansa", "मानसा", "मानसा"), ("Moga", "मोगा", "मोगा"),
    ("Pathankot", "पठानकोट", "पठाणकोट"), ("Patiala", "पटियाला", "पटियाळा"), ("Rupnagar", "रूपनगर", "रूपनगर"), ("Sahibzada Ajit Singh Nagar (Mohali)", "साहिबज़ादा अजीत सिंह नगर (मोहाली)", "साहिबजादा अजितसिंह नगर (मोहाली)"), ("Sangrur", "संगरूर", "संगरूर"),
    ("Shaheed Bhagat Singh Nagar", "शहीद भगत सिंह नगर", "शहीद भगतसिंह नगर"), ("Sri Muktsar Sahib", "श्री मुक्तसर साहिब", "श्री मुक्तसर साहिब"), ("Tarn Taran", "तरनतारन", "तरनतारन"),
]
assert len(DISTRICTS) == 23, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("ludhiana", ("Ludhiana", "लुधियाना", "लुधियाना"), ("Largest city; industrial hub of hosiery, bicycles and auto parts.", "सबसे बड़ा शहर; होज़री, साइकिलों और ऑटो पुर्ज़ों का औद्योगिक केंद्र।", "सर्वांत मोठे शहर; होजियरी, सायकली व वाहनांच्या सुट्या भागांचे औद्योगिक केंद्र."), ("Industry", "उद्योग", "उद्योग")),
        city("amritsar", ("Amritsar", "अमृतसर", "अमृतसर"), ("Holy city of the Sikhs; Golden Temple.", "सिखों का पवित्र नगर; स्वर्ण मंदिर।", "शिखांचे पवित्र नगर; सुवर्ण मंदिर."), ("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        city("jalandhar", ("Jalandhar", "जालंधर", "जालंधर"), ("Sports goods and hand tools; centre of the Doaba.", "खेल का सामान और हस्त औज़ार; दोआबा का केंद्र।", "क्रीडा साहित्य व हत्यारे; दोआब्याचे केंद्र."), ("Industry", "उद्योग", "उद्योग")),
        city("patiala", ("Patiala", "पटियाला", "पटियाळा"), ("Former princely capital; Punjabi University and NIS.", "पूर्व रियासत की राजधानी; पंजाबी विश्वविद्यालय और एनआईएस।", "पूर्वीची संस्थानी राजधानी; पंजाबी विद्यापीठ व एनआयएस."), ("Heritage", "धरोहर", "वारसा")),
        city("bathinda", ("Bathinda", "बठिंडा", "भटिंडा"), ("Malwa's main town; refinery and AIIMS.", "मालवा का मुख्य नगर; रिफ़ाइनरी और एम्स।", "माळव्याचे मुख्य शहर; रिफायनरी व एम्स."), ("Malwa", "मालवा", "माळवा")),
        city("mohali", ("Mohali (SAS Nagar)", "मोहाली (एसएएस नगर)", "मोहाली (एसएएस नगर)"), ("IT and research city next to Chandigarh.", "चंडीगढ़ से सटा आईटी और शोध नगर।", "चंदीगडलगतचे आयटी व संशोधन शहर."), ("IT", "आईटी", "आयटी")),
        city("pathankot", ("Pathankot", "पठानकोट", "पठाणकोट"), ("Gateway to Jammu and Himachal.", "जम्मू और हिमाचल का प्रवेश द्वार।", "जम्मू व हिमाचलचे प्रवेशद्वार."), ("Transport", "परिवहन", "वाहतूक")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 23 districts (alphabetical)", "23 ज़िले (वर्णानुक्रम)", "23 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Official district list (State notification)", "आधिकारिक ज़िला सूची (राज्य अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य अधिसूचना)"), "india-gov", "Link the State's list of districts; Malerkotla was created in 2021."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Punjab is one of India's great sporting States. Hockey runs deep — the village of Sansarpur near Jalandhar produced many Olympians, Balbir Singh Senior won three Olympic gold medals, and Harmanpreet Singh of Amritsar has captained the men's team. Milkha Singh, the 'Flying Sikh', made athletics popular, and Harmanpreet Kaur of Moga has captained India's women's cricket team. Wrestling, weightlifting and circle-style kabaddi are hugely popular in villages, and Jalandhar's sports-goods industry supplies equipment worldwide. The Netaji Subhas National Institute of Sports in Patiala is India's premier training centre, and Mohali's cricket stadiums host international matches.",
        "पंजाब भारत के महान खेल राज्यों में से है। हॉकी की जड़ें गहरी हैं — जालंधर के पास संसारपुर गाँव ने कई ओलंपियन दिए, बलबीर सिंह सीनियर ने तीन ओलंपिक स्वर्ण पदक जीते, और अमृतसर के हरमनप्रीत सिंह पुरुष टीम के कप्तान रहे हैं। 'फ़्लाइंग सिख' मिल्खा सिंह ने एथलेटिक्स को लोकप्रिय बनाया, और मोगा की हरमनप्रीत कौर भारतीय महिला क्रिकेट टीम की कप्तान रही हैं। गाँवों में कुश्ती, भारोत्तोलन और सर्कल कबड्डी बहुत लोकप्रिय हैं, और जालंधर का खेल सामान उद्योग दुनिया भर में उपकरण भेजता है। पटियाला का नेताजी सुभाष राष्ट्रीय खेल संस्थान भारत का प्रमुख प्रशिक्षण केंद्र है, और मोहाली के क्रिकेट स्टेडियम अंतरराष्ट्रीय मैचों की मेज़बानी करते हैं।",
        "पंजाब हे भारतातील महान क्रीडा राज्यांपैकी एक आहे. हॉकीची मुळे खोलवर आहेत — जालंधरजवळील संसारपूर गावाने अनेक ऑलिम्पियन दिले, बलबीरसिंह सीनियर यांनी तीन ऑलिम्पिक सुवर्णपदके जिंकली, आणि अमृतसरचे हरमनप्रीत सिंह पुरुष संघाचे कर्णधार राहिले आहेत. 'फ्लाइंग सिख' मिल्खासिंहांनी ॲथलेटिक्स लोकप्रिय केले, आणि मोग्याची हरमनप्रीत कौर भारतीय महिला क्रिकेट संघाची कर्णधार राहिली आहे. गावांत कुस्ती, भारोत्तोलन व सर्कल कबड्डी अतिशय लोकप्रिय आहेत, आणि जालंधरचा क्रीडा साहित्य उद्योग जगभर साहित्य पुरवतो. पटियाळाची नेताजी सुभाष राष्ट्रीय क्रीडा संस्था हे भारताचे प्रमुख प्रशिक्षण केंद्र आहे, आणि मोहालीची क्रिकेट स्टेडियम आंतरराष्ट्रीय सामने आयोजित करतात."),
        conf="Editorial"),
    lst("venues", [
        it3("nis", "NIS Patiala", "एनआईएस पटियाला", "एनआयएस पटियाळा"),
        it3("surjit", "Surjit Hockey Stadium, Jalandhar", "सुरजीत हॉकी स्टेडियम, जालंधर", "सुरजित हॉकी स्टेडियम, जालंधर"),
        it3("pca", "Punjab Cricket Association stadiums, Mohali and Mullanpur", "पंजाब क्रिकेट एसोसिएशन स्टेडियम, मोहाली और मुल्लांपुर", "पंजाब क्रिकेट असोसिएशन स्टेडियम, मोहाली व मुल्लांपूर"),
        it3("guru", "Guru Nanak Stadium, Ludhiana", "गुरु नानक स्टेडियम, लुधियाना", "गुरु नानक स्टेडियम, लुधियाना"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from Punjab (official list)", "पंजाब के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "पंजाबचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Punjab Sports Department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("nanak", ("Guru Nanak", "गुरु नानक", "गुरु नानक"), ("Founder of Sikhism (1469–1539), who taught devotion to one God, equality and honest work.", "सिख धर्म के संस्थापक (1469–1539), जिन्होंने एक ईश्वर की भक्ति, समानता और ईमानदार श्रम की शिक्षा दी।", "शीख धर्माचे संस्थापक (1469–1539), ज्यांनी एका ईश्वराची भक्ती, समता व प्रामाणिक श्रमाची शिकवण दिली."), ("Religion", "धर्म", "धर्म")),
        person("gobind", ("Guru Gobind Singh", "गुरु गोबिंद सिंह", "गुरु गोविंदसिंह"), ("Tenth Sikh Guru, who created the Khalsa at Anandpur Sahib in 1699.", "दसवें सिख गुरु, जिन्होंने 1699 में आनंदपुर साहिब में खालसा की स्थापना की।", "दहावे शीख गुरू, ज्यांनी 1699 मध्ये आनंदपूर साहिब येथे खालशाची स्थापना केली."), ("Religion", "धर्म", "धर्म")),
        person("ranjit", ("Maharaja Ranjit Singh", "महाराजा रणजीत सिंह", "महाराजा रणजितसिंह"), ("Founder of the Sikh empire, ruling from Lahore (1799–1839).", "लाहौर से शासन करने वाले सिख साम्राज्य के संस्थापक (1799–1839)।", "लाहोरहून राज्य करणाऱ्या शीख साम्राज्याचे संस्थापक (1799–1839)."), ("History", "इतिहास", "इतिहास")),
        person("bhagat", ("Bhagat Singh", "भगत सिंह", "भगतसिंह"), ("Revolutionary executed in 1931; his ancestral village is Khatkar Kalan.", "1931 में फाँसी पाने वाले क्रांतिकारी; उनका पैतृक गाँव खटकड़ कलाँ है।", "1931 मध्ये फाशी गेलेले क्रांतिकारक; त्यांचे मूळ गाव खटकड कलां आहे."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("udham", ("Udham Singh", "ऊधम सिंह", "उधमसिंह"), ("Revolutionary from Sunam who avenged the Jallianwala Bagh massacre in London in 1940.", "सुनाम के क्रांतिकारी, जिन्होंने 1940 में लंदन में जलियाँवाला बाग़ हत्याकांड का प्रतिशोध लिया।", "सुनामचे क्रांतिकारक, ज्यांनी 1940 मध्ये लंडनमध्ये जालियनवाला बाग हत्याकांडाचा बदला घेतला."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("lajpat", ("Lala Lajpat Rai", "लाला लाजपत राय", "लाला लजपतराय"), ("'Punjab Kesari'; nationalist leader who died after a police lathi charge in 1928.", "'पंजाब केसरी'; राष्ट्रवादी नेता, जिनकी 1928 में पुलिस लाठीचार्ज के बाद मृत्यु हुई।", "'पंजाब केसरी'; राष्ट्रवादी नेते, ज्यांचा 1928 मध्ये पोलिसांच्या लाठीमारानंतर मृत्यू झाला."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("amrita", ("Amrita Pritam", "अमृता प्रीतम", "अमृता प्रीतम"), ("Poet and novelist; the first woman to win the Sahitya Akademi Award for Punjabi.", "कवयित्री और उपन्यासकार; पंजाबी के लिए साहित्य अकादमी पुरस्कार पाने वाली पहली महिला।", "कवयित्री व कादंबरीकार; पंजाबीसाठी साहित्य अकादमी पुरस्कार मिळवणाऱ्या पहिल्या महिला."), ("Literature", "साहित्य", "साहित्य")),
        person("batalvi", ("Shiv Kumar Batalvi", "शिव कुमार बटालवी", "शिवकुमार बटालवी"), ("Romantic Punjabi poet; Sahitya Akademi Award for Loona.", "पंजाबी के रूमानी कवि; 'लूणा' के लिए साहित्य अकादमी पुरस्कार।", "पंजाबीचे स्वच्छंदतावादी कवी; 'लूणा'साठी साहित्य अकादमी पुरस्कार."), ("Literature", "साहित्य", "साहित्य")),
        person("balbir", ("Balbir Singh Senior", "बलबीर सिंह सीनियर", "बलबीरसिंह सीनियर"), ("Hockey centre-forward; Olympic gold in 1948, 1952 and 1956.", "हॉकी सेंटर-फ़ॉरवर्ड; 1948, 1952 और 1956 में ओलंपिक स्वर्ण।", "हॉकी सेंटर-फॉरवर्ड; 1948, 1952 व 1956 मध्ये ऑलिम्पिक सुवर्ण."), ("Sport", "खेल", "क्रीडा")),
        person("milkha", ("Milkha Singh", "मिल्खा सिंह", "मिल्खासिंह"), ("The 'Flying Sikh', Asian Games and Commonwealth Games champion sprinter.", "'फ़्लाइंग सिख', एशियाई और राष्ट्रमंडल खेलों के चैंपियन धावक।", "'फ्लाइंग सिख', आशियाई व राष्ट्रकुल स्पर्धांचे विजेते धावपटू."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Punjab has one of India's largest and most visible diasporas. Sikh soldiers and labourers reached Canada, the United States and East Africa at the start of the 20th century; after the Second World War, large numbers settled in Britain, and from the 1970s in Canada, the United States, Australia, New Zealand and Italy. Today Punjabi is among the most widely spoken languages in Canada, and towns such as Brampton, Surrey and Southall have large Punjabi communities. Money sent home has built houses and gurdwaras across the Doaba, and many young people still seek to study and work abroad.",
        "पंजाब में भारत के सबसे बड़े और सबसे दृश्यमान प्रवासी समुदायों में से एक है। सिख सैनिक और श्रमिक 20वीं सदी की शुरुआत में कनाडा, अमेरिका और पूर्वी अफ़्रीका पहुँचे; द्वितीय विश्व युद्ध के बाद बड़ी संख्या में लोग ब्रिटेन में बसे, और 1970 के दशक से कनाडा, अमेरिका, ऑस्ट्रेलिया, न्यूज़ीलैंड और इटली में। आज पंजाबी कनाडा की सबसे अधिक बोली जाने वाली भाषाओं में से है, और ब्रैम्पटन, सरे और साउथहॉल जैसे नगरों में बड़े पंजाबी समुदाय हैं। घर भेजे गए धन से दोआबा भर में घर और गुरुद्वारे बने हैं, और बहुत से युवा आज भी विदेश में पढ़ने और काम करने का प्रयास करते हैं।",
        "पंजाबमध्ये भारतातील सर्वांत मोठ्या व ठळक प्रवासी समुदायांपैकी एक आहे. शीख सैनिक व कामगार विसाव्या शतकाच्या सुरुवातीला कॅनडा, अमेरिका व पूर्व आफ्रिकेत पोहोचले; दुसऱ्या महायुद्धानंतर मोठ्या संख्येने लोक ब्रिटनमध्ये स्थायिक झाले, आणि 1970 च्या दशकापासून कॅनडा, अमेरिका, ऑस्ट्रेलिया, न्यूझीलंड व इटलीत. आज पंजाबी ही कॅनडातील सर्वाधिक बोलल्या जाणाऱ्या भाषांपैकी एक आहे, आणि ब्रॅम्प्टन, सरे व साउथहॉलसारख्या शहरांत मोठे पंजाबी समुदाय आहेत. घरी पाठवलेल्या पैशांतून दोआबाभर घरे व गुरुद्वारे उभे राहिले आहेत, आणि अनेक तरुण आजही परदेशात शिकण्याचा व काम करण्याचा प्रयत्न करतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Size of the Punjabi diaspora by country", "देशवार पंजाबी प्रवासी समुदाय का आकार", "देशनिहाय पंजाबी प्रवासी समुदायाचा आकार"), "india-gov", "MEA estimates; national censuses of host countries."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Punjab portal", "पंजाब सरकार पोर्टल", "पंजाब शासन संकेतस्थळ", url="https://punjab.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Punjab Tourism", "पंजाब पर्यटन", "पंजाब पर्यटन", url="https://punjabtourism.punjab.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Ludhiana", "लुधियाना", "लुधियाना"), "0161"], [L("Amritsar", "अमृतसर", "अमृतसर"), "0183"], [L("Jalandhar", "जालंधर", "जालंधर"), "0181"],
           [L("Patiala", "पटियाला", "पटियाळा"), "0175"], [L("Bathinda", "बठिंडा", "भटिंडा"), "0164"], [L("Mohali", "मोहाली", "मोहाली"), "0172"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("State e-services portal — verified link", "राज्य ई-सेवा पोर्टल — सत्यापित लिंक", "राज्य ई-सेवा संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "Sewa Kendra / Connect portal of the State."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("sc", ("Punjab has the highest share of Scheduled Castes of any State — 31.9% in 2011.", "पंजाब में किसी भी राज्य से अधिक अनुसूचित जातियों का हिस्सा है — 2011 में 31.9%।", "पंजाबमध्ये कोणत्याही राज्यापेक्षा अनुसूचित जातींचा वाटा अधिक आहे — 2011 मध्ये 31.9%."), "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf", "dl-planning"),
        triv("csr", ("Punjab's child sex ratio rose from 798 in 2001 to 846 in 2011 — an improvement, though still low.", "पंजाब का शिशु लिंगानुपात 2001 के 798 से बढ़कर 2011 में 846 हुआ — फिर भी कम।", "पंजाबचे बाल लिंग गुणोत्तर 2001 मधील 798 वरून 2011 मध्ये 846 झाले — तरीही कमी."), PIB_CSR, "pib"),
        triv("ramsar", ("Punjab has six Ramsar wetlands despite having only about 3.7% forest cover.", "केवल लगभग 3.7% वन आवरण के बावजूद पंजाब में छह रामसर आर्द्रभूमियाँ हैं।", "केवळ सुमारे 3.7% वनाच्छादन असूनही पंजाबमध्ये सहा रामसर पाणथळे आहेत."), RAMSAR, "indian-wetlands"),
        triv("capital", ("Chandigarh, a Union Territory, is the capital of both Punjab and Haryana.", "केंद्र शासित प्रदेश चंडीगढ़ पंजाब और हरियाणा दोनों की राजधानी है।", "केंद्रशासित प्रदेश चंदीगड ही पंजाब व हरियाणा दोघांची राजधानी आहे.")),
        triv("dfc", ("The Eastern Dedicated Freight Corridor begins at Sahnewal near Ludhiana.", "पूर्वी समर्पित माल गलियारा लुधियाना के पास साहनेवाल से शुरू होता है।", "पूर्व समर्पित मालवाहतूक मार्गिका लुधियान्याजवळ साहनेवाल येथून सुरू होते.")),
        triv("ls", ("The State elects 13 members to the Lok Sabha.", "राज्य से लोकसभा के 13 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 13 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("pb mod3 ok")
