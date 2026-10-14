"""Gujarat modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-GJ"
VAV = "https://newsonair.gov.in/gujarat-govt-approves-creation-of-new-district-named-vav-tharad"
gj = read("regions/IN-GJ.json")["metrics"]; ind = read("india.json")["metrics"]

RAMSAR_GJ = [
    ("Nalsarovar Bird Sanctuary", "नलसरोवर पक्षी अभयारण्य", "नळसरोवर पक्षी अभयारण्य", "24 Sep 2012", "12,000"),
    ("Thol Lake Wildlife Sanctuary", "थोल झील वन्यजीव अभयारण्य", "थोळ तलाव वन्यजीव अभयारण्य", "5 Apr 2021", "699"),
    ("Wadhvana Wetland", "वढवाणा आर्द्रभूमि", "वढवाणा पाणथळ", "5 Apr 2021", "630"),
    ("Khijadia Wildlife Sanctuary", "खिजड़िया वन्यजीव अभयारण्य", "खिजडिया वन्यजीव अभयारण्य", "13 Apr 2021", "512"),
    ("Chhari Dhand Conservation Reserve", "छारी ढंढ संरक्षण रिज़र्व", "छारी ढंढ संवर्धन राखीव क्षेत्र", "16 Jun 2025", "22,700"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Gujarat has relatively little forest — 7.7% of its area in ISFR 2023 — but very varied wildlife. Gir National Park and the surrounding forests of Saurashtra are the only wild home of the Asiatic lion, whose population has grown steadily under protection. The Little Rann of Kutch shelters the Indian wild ass; Velavadar near Bhavnagar protects blackbuck on open grassland; and Banni in Kutch is one of Asia's largest grasslands. The Marine National Park in the Gulf of Kutch has coral reefs and mangroves.\n\nGujarat's wetlands are major wintering grounds for migratory birds, especially flamingos, which breed in the Rann. The State has five Ramsar sites, including Nalsarovar near Ahmedabad and Chhari Dhand in Kutch.",
        "गुजरात में वन अपेक्षाकृत कम हैं — आईएसएफ़आर 2023 में क्षेत्रफल का 7.7% — लेकिन वन्यजीव बहुत विविध हैं। गिर राष्ट्रीय उद्यान और सौराष्ट्र के आसपास के वन एशियाई सिंह का एकमात्र प्राकृतिक आवास हैं, जिसकी आबादी संरक्षण में लगातार बढ़ी है। कच्छ का छोटा रण भारतीय जंगली गधे (घुड़खर) का आश्रय है; भावनगर के पास वेलावदर खुले घासभूमि में काले हिरण की रक्षा करता है; और कच्छ का बन्नी एशिया की सबसे बड़ी घासभूमियों में से एक है। कच्छ की खाड़ी के समुद्री राष्ट्रीय उद्यान में प्रवाल भित्तियाँ और मैंग्रोव हैं।\n\nगुजरात की आर्द्रभूमियाँ प्रवासी पक्षियों, ख़ासकर फ़्लेमिंगो, के लिए सर्दियों के प्रमुख ठिकाने हैं, जो रण में प्रजनन करते हैं। राज्य में पाँच रामसर स्थल हैं, जिनमें अहमदाबाद के पास नलसरोवर और कच्छ का छारी ढंढ शामिल हैं।",
        "गुजरातमध्ये वनक्षेत्र तुलनेने कमी आहे — आयएसएफआर 2023 नुसार क्षेत्रफळाच्या 7.7% — पण वन्यजीव अतिशय वैविध्यपूर्ण आहेत. गीर राष्ट्रीय उद्यान व सौराष्ट्रातील आसपासची जंगले हे आशियाई सिंहाचे एकमेव नैसर्गिक निवासस्थान आहे, आणि संरक्षणामुळे त्यांची संख्या सातत्याने वाढली आहे. कच्छचे छोटे रण भारतीय रानगाढवाचे (घुडखर) आश्रयस्थान आहे; भावनगरजवळील वेळावदर मोकळ्या गवताळ प्रदेशात काळविटांचे संरक्षण करते; आणि कच्छमधील बन्नी हे आशियातील सर्वांत मोठ्या गवताळ प्रदेशांपैकी एक आहे. कच्छच्या आखातातील सागरी राष्ट्रीय उद्यानात प्रवाळभित्ती व खारफुटी आहे.\n\nगुजरातमधील पाणथळ जागा स्थलांतरित पक्ष्यांची, विशेषतः रणात प्रजनन करणाऱ्या रोहित पक्ष्यांची (फ्लेमिंगो), प्रमुख हिवाळी ठिकाणे आहेत. राज्यात पाच रामसर स्थळे आहेत, त्यांत अहमदाबादजवळील नळसरोवर व कच्छमधील छारी ढंढ यांचा समावेश आहे."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(15016.64, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(14836.57, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), gj["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(5, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026 (India total 99)."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_GJ], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026.", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी.")),
    lst("protected", [
        it3("gir", "Gir National Park and Sanctuary", "गिर राष्ट्रीय उद्यान और अभयारण्य", "गीर राष्ट्रीय उद्यान व अभयारण्य", m=("Asiatic lion", "एशियाई सिंह", "आशियाई सिंह")),
        it3("lrk", "Indian Wild Ass Sanctuary, Little Rann of Kutch", "भारतीय जंगली गधा अभयारण्य, कच्छ का छोटा रण", "भारतीय रानगाढव अभयारण्य, कच्छचे छोटे रण", m=("Wild ass", "घुड़खर", "घुडखर")),
        it3("velavadar", "Blackbuck National Park, Velavadar", "काला हिरण राष्ट्रीय उद्यान, वेलावदर", "काळवीट राष्ट्रीय उद्यान, वेळावदर", m=("Blackbuck", "काला हिरण", "काळवीट")),
        it3("marine", "Marine National Park, Gulf of Kutch", "समुद्री राष्ट्रीय उद्यान, कच्छ की खाड़ी", "सागरी राष्ट्रीय उद्यान, कच्छचे आखात", m=("Coral reefs", "प्रवाल भित्तियाँ", "प्रवाळभित्ती")),
        it3("vansda", "Vansda National Park", "वांसदा राष्ट्रीय उद्यान", "वांसदा राष्ट्रीय उद्यान", m=("Southern forests", "दक्षिणी वन", "दक्षिणेकडील जंगले")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("lion", "Asiatic lion (State animal)", "एशियाई सिंह (राज्य पशु)", "आशियाई सिंह (राज्यप्राणी)"), it3("wildass", "Indian wild ass", "भारतीय जंगली गधा", "भारतीय रानगाढव"),
        it3("flamingo", "Greater flamingo (State bird)", "बड़ा राजहंस (राज्य पक्षी)", "मोठा रोहित (राज्यपक्षी)"), it3("blackbuck", "Blackbuck", "काला हिरण", "काळवीट"),
        it3("bustard", "Great Indian bustard", "सोन चिरैया (गोडावण)", "माळढोक"), it3("dugong", "Dugong", "डुगोंग", "डुगाँग"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Asiatic lion population (latest count)", "एशियाई सिंह आबादी (नवीनतम गणना)", "आशियाई सिंहांची संख्या (नवीनतम गणना)"), "moefcc", "Gujarat Forest Department lion population estimation."),
        (L("National parks and sanctuaries (count, area)", "राष्ट्रीय उद्यान और अभयारण्य (संख्या, क्षेत्रफल)", "राष्ट्रीय उद्याने व अभयारण्ये (संख्या, क्षेत्र)"), "moefcc", "ENVIS / WII database."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Water scarcity has shaped Gujarat's development. North Gujarat, Kutch and much of Saurashtra receive little rain, groundwater has fallen sharply in the north, and sea-water intrusion has made wells salty along parts of the Saurashtra coast. The Sardar Sarovar dam on the Narmada, completed in 2017, feeds a canal network that carries water to central and north Gujarat and, through pipelines and the SAUNI scheme, to reservoirs in Saurashtra and Kutch. Check dams, farm ponds and drip irrigation are widely used. The south, with heavy monsoon rain and the Tapi and Narmada, has more water.",
        "पानी की कमी ने गुजरात के विकास को आकार दिया है। उत्तर गुजरात, कच्छ और सौराष्ट्र के बड़े हिस्से में कम वर्षा होती है, उत्तर में भूजल तेज़ी से गिरा है, और सौराष्ट्र तट के कुछ हिस्सों में समुद्री पानी घुसने से कुएँ खारे हो गए हैं। 2017 में पूरा हुआ नर्मदा का सरदार सरोवर बाँध नहर नेटवर्क को पानी देता है, जो मध्य और उत्तर गुजरात तक, और पाइपलाइनों व सौनी योजना के माध्यम से सौराष्ट्र और कच्छ के जलाशयों तक पानी पहुँचाता है। चेक डैम, खेत तालाब और ड्रिप सिंचाई का व्यापक उपयोग होता है। भारी मानसूनी वर्षा और तापी व नर्मदा के कारण दक्षिण में अधिक पानी है।",
        "पाणीटंचाईने गुजरातच्या विकासाला आकार दिला आहे. उत्तर गुजरात, कच्छ व सौराष्ट्राच्या बहुतांश भागात पाऊस कमी पडतो, उत्तरेकडे भूजल झपाट्याने खालावले आहे, आणि सौराष्ट्र किनाऱ्याच्या काही भागांत समुद्राचे पाणी शिरल्याने विहिरी खाऱ्या झाल्या आहेत. 2017 मध्ये पूर्ण झालेले नर्मदेवरील सरदार सरोवर धरण कालव्यांच्या जाळ्याला पाणी पुरवते, जे मध्य व उत्तर गुजरातपर्यंत, तसेच जलवाहिन्या व सौनी योजनेद्वारे सौराष्ट्र व कच्छमधील जलाशयांपर्यंत पाणी नेते. बंधारे, शेततळी व ठिबक सिंचनाचा मोठ्या प्रमाणावर वापर होतो. मुसळधार मोसमी पाऊस आणि तापी व नर्मदेमुळे दक्षिण भागात अधिक पाणी आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Narmada canal command area irrigated", "नर्मदा नहर कमान क्षेत्र में सिंचाई", "नर्मदा कालवा लाभक्षेत्रातील सिंचन"), "india-gov", "Sardar Sarovar Narmada Nigam Ltd."),
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Kutch lies in India's highest seismic zone: the Bhuj earthquake of 26 January 2001 killed thousands and led to the creation of the Gujarat State Disaster Management Authority, the first in India. Cyclones from the Arabian Sea regularly strike Saurashtra and Kutch — Tauktae in 2021 and Biparjoy in 2023 were recent examples. Floods affect the south and the Narmada, Tapi and Vishwamitri basins in heavy monsoons, and droughts and heatwaves affect the north and Kutch.\n\nFor visitors, the main precautions are following cyclone warnings on the coast in May–June and October–November, avoiding midday travel in the summer, and staying on marked tracks in the Rann, where the salt flats flood after rain.",
        "कच्छ भारत के सबसे ऊँचे भूकंपीय क्षेत्र में है: 26 जनवरी 2001 के भुज भूकंप में हज़ारों लोग मारे गए, और इसके बाद भारत का पहला राज्य आपदा प्रबंधन प्राधिकरण — गुजरात राज्य आपदा प्रबंधन प्राधिकरण — बना। अरब सागर के चक्रवात नियमित रूप से सौराष्ट्र और कच्छ से टकराते हैं — 2021 में तौकते और 2023 में बिपरजॉय हाल के उदाहरण हैं। भारी मानसून में दक्षिण और नर्मदा, तापी व विश्वामित्री बेसिन में बाढ़ आती है, और उत्तर व कच्छ में सूखा और लू का असर होता है।\n\nपर्यटकों के लिए मुख्य सावधानियाँ हैं: मई–जून और अक्टूबर–नवंबर में तट पर चक्रवात चेतावनियों का पालन, गर्मियों में दोपहर की यात्रा से बचना, और रण में चिह्नित रास्तों पर ही रहना, जहाँ बारिश के बाद नमक के मैदान जलमग्न हो जाते हैं।",
        "कच्छ भारतातील सर्वाधिक भूकंपप्रवण क्षेत्रात आहे: 26 जानेवारी 2001 च्या भुज भूकंपात हजारो लोकांचा मृत्यू झाला, आणि त्यानंतर भारतातील पहिले राज्य आपत्ती व्यवस्थापन प्राधिकरण — गुजरात राज्य आपत्ती व्यवस्थापन प्राधिकरण — स्थापन झाले. अरबी समुद्रातील चक्रीवादळे नियमितपणे सौराष्ट्र व कच्छला धडकतात — 2021 मधील तौक्ते व 2023 मधील बिपरजॉय ही अलीकडील उदाहरणे. मुसळधार पावसाळ्यात दक्षिण भाग आणि नर्मदा, तापी व विश्वामित्री खोऱ्यांत पूर येतात, तर उत्तर भाग व कच्छमध्ये दुष्काळ व उष्णतेची लाट येते.\n\nपर्यटकांसाठी मुख्य काळजी: मे–जून व ऑक्टोबर–नोव्हेंबरमध्ये किनाऱ्यावर चक्रीवादळ इशाऱ्यांचे पालन, उन्हाळ्यात दुपारचा प्रवास टाळणे, आणि रणात खुणा केलेल्या मार्गांवरच राहणे, कारण पावसानंतर मिठाची मैदाने पाण्याखाली जातात."),
        conf="Editorial"),
    emergency_table(("Gujarat", "गुजरात", "गुजरात")),
    lst("links", [
        it3("imd", "IMD weather and cyclone warnings", "आईएमडी मौसम और चक्रवात चेतावनियाँ", "आयएमडी हवामान व चक्रीवादळ इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Gujarat State Disaster Management Authority — verified link", "गुजरात राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "गुजरात राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official GSDMA address."),
        (L("Bhuj earthquake casualty and damage figures (official)", "भुज भूकंप में जन-धन हानि के आधिकारिक आँकड़े", "भुज भूकंपातील जीवित व वित्तहानीचे अधिकृत आकडे"), "ndma", "GSDMA / Government of Gujarat report."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Gujarat has 29 registered Geographical Indications in the GI Registry's list as on 31 December 2025, and shares Warli painting with Maharashtra and Dadra & Nagar Haveli and Daman & Diu. Most are textiles and crafts: Patan patola, Jamnagari and Kutch bandhani, Kutch embroidery and shawls, Kutch ajrakh and rogan craft, Tangaliya shawls, Surat zari, Ahmedabad's Sodagari block prints, Mata ni Pachhedi and Pithora paintings, Sankheda furniture and the agates of Cambay (Khambhat). Food and farm GIs include Gir kesar mangoes, Bhalia wheat, Kachchhi kharek (dates) and Amalsad chikoo, and the most recent additions are Ambaji white marble and Surat cut diamonds.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में गुजरात के 29 पंजीकृत भौगोलिक संकेतक हैं, और वार्ली चित्रकला महाराष्ट्र तथा दादरा और नगर हवेली व दमन और दीव के साथ साझा है। अधिकांश वस्त्र और शिल्प हैं: पाटन पटोला, जामनगरी और कच्छ बांधनी, कच्छ कढ़ाई और शॉल, कच्छ अजरख और रोगन कला, तंगलिया शॉल, सूरत ज़री, अहमदाबाद की सोदागरी छपाई, माता नी पछेडी और पिथोरा चित्रकला, संखेडा फ़र्नीचर और खंभात के अकीक। खाद्य और कृषि जीआई में गिर केसर आम, भालिया गेहूँ, कच्छी खारेक और अमलसाड चीकू हैं, और सबसे नए जुड़े हैं अंबाजी सफ़ेद संगमरमर और सूरत तराशा हीरा।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत गुजरातची 29 नोंदणीकृत भौगोलिक मानांकने आहेत, आणि वारली चित्रकला महाराष्ट्र तसेच दादरा व नगर हवेली आणि दमण व दीवसोबत सामायिक आहे. बहुतेक वस्त्रे व हस्तकला आहेत: पाटण पटोला, जामनगरी व कच्छ बांधणी, कच्छ भरतकाम व शाली, कच्छ अजरख व रोगन कला, तंगलिया शाल, सुरत जरी, अहमदाबादची सोदागरी छपाई, माता नी पछेडी व पिथोरा चित्रकला, संखेडा फर्निचर आणि खंबायतचे अकीक. खाद्य व कृषी मानांकनांत गीर केशर आंबा, भालिया गहू, कच्छी खारीक व अमलसाड चिकू आहेत, आणि सर्वांत अलीकडची भर म्हणजे अंबाजी पांढरा संगमरवर व सुरतचा पैलू पाडलेला हिरा."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Gujarat's attractions range from heritage and pilgrimage to wildlife and desert. Ahmedabad's old city and Sabarmati Ashram, the stepwells of Patan and Adalaj, Champaner-Pavagadh and Dholavira are among its historic sites; Somnath, Dwarka, Ambaji and the Jain hill temples of Palitana draw large numbers of pilgrims. Gir's lions, the white Rann of Kutch during the Rann Utsav, the beaches of Diu nearby and Saurashtra, and the Statue of Unity — at 182 m the world's tallest statue — near the Sardar Sarovar dam are the other main draws.",
        "गुजरात के आकर्षण धरोहर और तीर्थ से लेकर वन्यजीव और मरुस्थल तक हैं। अहमदाबाद का पुराना शहर और साबरमती आश्रम, पाटन और अडालज की बावड़ियाँ, चंपानेर-पावागढ़ और धोलावीरा इसके ऐतिहासिक स्थलों में हैं; सोमनाथ, द्वारका, अंबाजी और पालीताणा के जैन पर्वतीय मंदिर बड़ी संख्या में तीर्थयात्रियों को आकर्षित करते हैं। गिर के सिंह, रण उत्सव के दौरान कच्छ का सफ़ेद रण, पास के दीव और सौराष्ट्र के समुद्र तट, और सरदार सरोवर बाँध के पास 182 मीटर ऊँची — दुनिया की सबसे ऊँची — स्टैच्यू ऑफ़ यूनिटी अन्य मुख्य आकर्षण हैं।",
        "गुजरातमधील आकर्षणे वारसा व तीर्थक्षेत्रांपासून वन्यजीव व वाळवंटापर्यंत आहेत. अहमदाबादचे जुने शहर व साबरमती आश्रम, पाटण व अडालजच्या बारवा, चंपानेर-पावागड व धोलावीरा ही ऐतिहासिक स्थळे आहेत; सोमनाथ, द्वारका, अंबाजी व पालीताणाची जैन डोंगरमंदिरे मोठ्या संख्येने भाविकांना आकर्षित करतात. गीरचे सिंह, रण उत्सवादरम्यान कच्छचे पांढरे रण, जवळच्या दीव व सौराष्ट्राचे समुद्रकिनारे, आणि सरदार सरोवर धरणाजवळील 182 मीटर उंच — जगातील सर्वांत उंच — स्टॅच्यू ऑफ युनिटी ही इतर प्रमुख आकर्षणे आहेत."),
        conf="Editorial"),
    lst("places", [
        it3("ahmedabad", "Old Ahmedabad and Sabarmati Ashram", "पुराना अहमदाबाद और साबरमती आश्रम", "जुने अहमदाबाद व साबरमती आश्रम", m=("UNESCO heritage city", "यूनेस्को धरोहर नगर", "युनेस्को वारसा शहर")),
        it3("gir", "Gir National Park", "गिर राष्ट्रीय उद्यान", "गीर राष्ट्रीय उद्यान", m=("Lions (mid-Oct–mid-Jun)", "सिंह (मध्य-अक्टूबर–मध्य-जून)", "सिंह (ऑक्टो. मध्य–जून मध्य)")),
        it3("rann", "White Rann, Kutch", "सफ़ेद रण, कच्छ", "पांढरे रण, कच्छ", m=("Rann Utsav", "रण उत्सव", "रण उत्सव")),
        it3("somnath", "Somnath and Dwarka", "सोमनाथ और द्वारका", "सोमनाथ व द्वारका", m=("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        it3("ranikivav", "Rani ki Vav, Patan", "रानी की वाव, पाटन", "राणी की वाव, पाटण", m=("UNESCO heritage", "यूनेस्को धरोहर", "युनेस्को वारसा")),
        it3("champaner", "Champaner-Pavagadh", "चंपानेर-पावागढ़", "चंपानेर-पावागड", m=("UNESCO heritage", "यूनेस्को धरोहर", "युनेस्को वारसा")),
        it3("dholavira", "Dholavira", "धोलावीरा", "धोलावीरा", m=("Harappan city", "हड़प्पा नगर", "हडप्पा नगर")),
        it3("palitana", "Palitana (Shatrunjaya hill)", "पालीताणा (शत्रुंजय पर्वत)", "पालीताणा (शत्रुंजय डोंगर)", m=("Jain pilgrimage", "जैन तीर्थ", "जैन तीर्थक्षेत्र")),
        it3("unity", "Statue of Unity, Ekta Nagar", "स्टैच्यू ऑफ़ यूनिटी, एकता नगर", "स्टॅच्यू ऑफ युनिटी, एकता नगर", m=("182 m statue", "182 मीटर प्रतिमा", "182 मीटर पुतळा")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Ahmedabad heritage walk, Sabarmati Ashram, Adalaj stepwell and Modhera.", "अहमदाबाद धरोहर पदयात्रा, साबरमती आश्रम, अडालज बावड़ी और मोढेरा।", "अहमदाबाद वारसा फेरी, साबरमती आश्रम, अडालज बारव व मोढेरा.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Bhuj and the White Rann, with Kutch craft villages.", "भुज और सफ़ेद रण, कच्छ के शिल्प गाँवों के साथ।", "भुज व पांढरे रण, कच्छच्या हस्तकला गावांसह.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Saurashtra: Gir, Somnath, Diu and Junagadh's Girnar.", "सौराष्ट्र: गिर, सोमनाथ, दीव और जूनागढ़ का गिरनार।", "सौराष्ट्र: गीर, सोमनाथ, दीव व जुनागडचा गिरनार.")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Ahmedabad, Patan, Kutch and Dholavira, then Dwarka and Somnath.", "अहमदाबाद, पाटन, कच्छ और धोलावीरा, फिर द्वारका और सोमनाथ।", "अहमदाबाद, पाटण, कच्छ व धोलावीरा, नंतर द्वारका व सोमनाथ.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("gt", "Gujarat Tourism (official)", "गुजरात पर्यटन (आधिकारिक)", "गुजरात पर्यटन (अधिकृत)", url="https://www.gujarattourism.com", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
        (L("Earnings from tourism", "पर्यटन से आय", "पर्यटनातून उत्पन्न"), "tourism", "State tourism department."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Ahmedabad", "अहमदाबाद", "अहमदाबाद"), ("Amreli", "अमरेली", "अमरेली"), ("Anand", "आणंद", "आणंद"), ("Aravalli", "अरवल्ली", "अरवल्ली"),
    ("Banaskantha", "बनासकांठा", "बनासकांठा"), ("Bharuch", "भरूच", "भरूच"), ("Bhavnagar", "भावनगर", "भावनगर"), ("Botad", "बोटाद", "बोटाद"),
    ("Chhota Udaipur", "छोटा उदयपुर", "छोटा उदयपूर"), ("Dahod", "दाहोद", "दाहोद"), ("Dang", "डांग", "डांग"), ("Devbhoomi Dwarka", "देवभूमि द्वारका", "देवभूमी द्वारका"),
    ("Gandhinagar", "गांधीनगर", "गांधीनगर"), ("Gir Somnath", "गिर सोमनाथ", "गीर सोमनाथ"), ("Jamnagar", "जामनगर", "जामनगर"), ("Junagadh", "जूनागढ़", "जुनागड"),
    ("Kheda", "खेड़ा", "खेडा"), ("Kutch", "कच्छ", "कच्छ"), ("Mahisagar", "महीसागर", "महीसागर"), ("Mehsana", "मेहसाणा", "मेहसाणा"),
    ("Morbi", "मोरबी", "मोरबी"), ("Narmada", "नर्मदा", "नर्मदा"), ("Navsari", "नवसारी", "नवसारी"), ("Panchmahal", "पंचमहाल", "पंचमहाल"),
    ("Patan", "पाटन", "पाटण"), ("Porbandar", "पोरबंदर", "पोरबंदर"), ("Rajkot", "राजकोट", "राजकोट"), ("Sabarkantha", "साबरकांठा", "साबरकांठा"),
    ("Surat", "सूरत", "सुरत"), ("Surendranagar", "सुरेंद्रनगर", "सुरेंद्रनगर"), ("Tapi", "तापी", "तापी"), ("Vadodara", "वडोदरा", "वडोदरा"),
    ("Valsad", "वलसाड", "वलसाड"), ("Vav-Tharad", "वाव-थराद", "वाव-थराद"),
]
assert len(DISTRICTS) == 34, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("gandhinagar", ("Gandhinagar", "गांधीनगर", "गांधीनगर"), ("Planned State capital; GIFT City; Akshardham.", "नियोजित राजधानी; गिफ़्ट सिटी; अक्षरधाम।", "नियोजित राजधानी; गिफ्ट सिटी; अक्षरधाम."), ("Capital", "राजधानी", "राजधानी")),
        city("ahmedabad", ("Ahmedabad", "अहमदाबाद", "अहमदाबाद"), ("Largest city; UNESCO heritage city; textiles, pharmaceuticals, IIM.", "सबसे बड़ा शहर; यूनेस्को धरोहर नगर; कपड़ा, दवाएँ, आईआईएम।", "सर्वांत मोठे शहर; युनेस्को वारसा शहर; कापड, औषधे, आयआयएम."), ("Commerce", "वाणिज्य", "वाणिज्य")),
        city("surat", ("Surat", "सूरत", "सुरत"), ("Diamond cutting and polishing; synthetic textiles; port at Hazira.", "हीरा तराशी और पॉलिश; सिंथेटिक कपड़ा; हज़ीरा बंदरगाह।", "हिरे पैलू व पॉलिश; कृत्रिम कापड; हजिरा बंदर."), ("Industry", "उद्योग", "उद्योग")),
        city("vadodara", ("Vadodara", "वडोदरा", "वडोदरा"), ("Former Gaekwad capital; Laxmi Vilas Palace; refinery and engineering; MS University.", "पूर्व गायकवाड़ राजधानी; लक्ष्मी विलास महल; रिफ़ाइनरी और इंजीनियरिंग; एमएस विश्वविद्यालय।", "पूर्वीची गायकवाड राजधानी; लक्ष्मी विलास राजवाडा; तेलशुद्धीकरण व अभियांत्रिकी; एमएस विद्यापीठ."), ("Culture, industry", "संस्कृति, उद्योग", "संस्कृती, उद्योग")),
        city("rajkot", ("Rajkot", "राजकोट", "राजकोट"), ("Saurashtra's commercial hub; engineering, castings, jewellery.", "सौराष्ट्र का वाणिज्यिक केंद्र; इंजीनियरिंग, ढलाई, आभूषण।", "सौराष्ट्राचे व्यापारी केंद्र; अभियांत्रिकी, ओतकाम, दागिने."), ("Saurashtra", "सौराष्ट्र", "सौराष्ट्र")),
        city("jamnagar", ("Jamnagar", "जामनगर", "जामनगर"), ("Refinery complex; brass parts; bandhani.", "रिफ़ाइनरी परिसर; पीतल के पुर्ज़े; बांधनी।", "तेलशुद्धीकरण संकुल; पितळी भाग; बांधणी."), ("Industry", "उद्योग", "उद्योग")),
        city("bhavnagar", ("Bhavnagar", "भावनगर", "भावनगर"), ("Port city; ship-breaking at nearby Alang; Velavadar.", "बंदरगाह नगर; पास के अलंग में जहाज़ तोड़ने का उद्योग; वेलावदर।", "बंदराचे शहर; जवळच्या अलंगमध्ये जहाजतोड उद्योग; वेळावदर."), ("Coast", "तट", "किनारपट्टी")),
        city("bhuj", ("Bhuj", "भुज", "भुज"), ("Kutch's main town; crafts; gateway to the Rann.", "कच्छ का मुख्य नगर; शिल्प; रण का प्रवेश द्वार।", "कच्छचे मुख्य शहर; हस्तकला; रणाचे प्रवेशद्वार."), ("Kutch", "कच्छ", "कच्छ")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 34 districts (alphabetical)", "34 ज़िले (वर्णानुक्रम)", "34 जिल्हे (वर्णक्रमानुसार)"), src="newsonair", url=VAV, conf="Editorial", access=TODAY),
    gaps("g", [
        (L("District populations (Census 2011)", "ज़िलावार जनसंख्या (जनगणना 2011)", "जिल्हानिहाय लोकसंख्या (जनगणना 2011)"), "census", "District Census Handbooks."),
        (L("Official district list (Revenue Department)", "आधिकारिक ज़िला सूची (राजस्व विभाग)", "अधिकृत जिल्हा यादी (महसूल विभाग)"), "india-gov", "Replace the news citation with the State notification."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Cricket dominates. The Narendra Modi Stadium in Ahmedabad (formerly Motera), rebuilt in 2020, is the largest cricket stadium in the world by seating capacity, and Saurashtra and Baroda are among the strongest domestic teams; Cheteshwar Pujara, Ravindra Jadeja, Jasprit Bumrah and Irfan and Yusuf Pathan are among India players from the State. Gujarat also has a strong tradition in chess and table tennis, and the State is preparing infrastructure in Ahmedabad for large multi-sport events.",
        "क्रिकेट सबसे लोकप्रिय है। अहमदाबाद का नरेंद्र मोदी स्टेडियम (पहले मोटेरा), जो 2020 में फिर से बना, बैठने की क्षमता के हिसाब से दुनिया का सबसे बड़ा क्रिकेट स्टेडियम है, और सौराष्ट्र व बड़ौदा सबसे मज़बूत घरेलू टीमों में हैं; चेतेश्वर पुजारा, रवींद्र जडेजा, जसप्रीत बुमराह और इरफ़ान व यूसुफ़ पठान राज्य से भारत के लिए खेलने वाले खिलाड़ियों में हैं। गुजरात में शतरंज और टेबल टेनिस की भी मज़बूत परंपरा है, और राज्य अहमदाबाद में बड़े बहु-खेल आयोजनों के लिए बुनियादी ढाँचा तैयार कर रहा है।",
        "क्रिकेटचे वर्चस्व आहे. अहमदाबादचे नरेंद्र मोदी स्टेडियम (पूर्वीचे मोटेरा), 2020 मध्ये पुन्हा उभारलेले, आसनक्षमतेनुसार जगातील सर्वांत मोठे क्रिकेट मैदान आहे, आणि सौराष्ट्र व बडोदा हे सर्वांत बलाढ्य देशांतर्गत संघांपैकी आहेत; चेतेश्वर पुजारा, रवींद्र जडेजा, जसप्रीत बुमराह आणि इरफान व युसूफ पठाण हे राज्यातून भारतासाठी खेळलेल्या खेळाडूंपैकी आहेत. गुजरातमध्ये बुद्धिबळ व टेबल टेनिसचीही भक्कम परंपरा आहे, आणि राज्य अहमदाबादमध्ये मोठ्या बहुक्रीडा स्पर्धांसाठी पायाभूत सुविधा उभारत आहे."),
        conf="Editorial"),
    lst("venues", [
        it3("motera", "Narendra Modi Stadium, Ahmedabad", "नरेंद्र मोदी स्टेडियम, अहमदाबाद", "नरेंद्र मोदी स्टेडियम, अहमदाबाद"),
        it3("sardarpatel", "Sardar Vallabhbhai Patel Sports Enclave, Ahmedabad", "सरदार वल्लभभाई पटेल स्पोर्ट्स एन्क्लेव, अहमदाबाद", "सरदार वल्लभभाई पटेल स्पोर्ट्स एन्क्लेव्ह, अहमदाबाद"),
        it3("rajkot", "Saurashtra Cricket Association Stadium, Rajkot", "सौराष्ट्र क्रिकेट एसोसिएशन स्टेडियम, राजकोट", "सौराष्ट्र क्रिकेट असोसिएशन स्टेडियम, राजकोट"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from Gujarat (official list)", "गुजरात के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "गुजरातचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Sports Authority of Gujarat.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("narsinh", ("Narsinh Mehta", "नरसिंह मेहता", "नरसिंह मेहता"), ("15th-century poet-saint of Junagadh, author of 'Vaishnav Jan To'.", "जूनागढ़ के 15वीं सदी के संत-कवि, 'वैष्णव जन तो' के रचयिता।", "जुनागडचे पंधराव्या शतकातील संतकवी, 'वैष्णव जन तो' चे रचनाकार."), ("Literature", "साहित्य", "साहित्य")),
        person("gandhi", ("Mahatma Gandhi", "महात्मा गांधी", "महात्मा गांधी"), ("Born at Porbandar in 1869; led the national movement from Sabarmati Ashram.", "1869 में पोरबंदर में जन्मे; साबरमती आश्रम से राष्ट्रीय आंदोलन का नेतृत्व किया।", "1869 मध्ये पोरबंदर येथे जन्म; साबरमती आश्रमातून राष्ट्रीय चळवळीचे नेतृत्व केले."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("patel", ("Sardar Vallabhbhai Patel", "सरदार वल्लभभाई पटेल", "सरदार वल्लभभाई पटेल"), ("Led the Bardoli satyagraha; as India's first Home Minister integrated the princely states.", "बारडोली सत्याग्रह का नेतृत्व किया; भारत के पहले गृह मंत्री के रूप में रियासतों का एकीकरण किया।", "बारडोली सत्याग्रहाचे नेतृत्व; भारताचे पहिले गृहमंत्री म्हणून संस्थानांचे विलीनीकरण केले."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("dayananda", ("Swami Dayananda Saraswati", "स्वामी दयानंद सरस्वती", "स्वामी दयानंद सरस्वती"), ("Born at Tankara; founded the Arya Samaj (1875).", "टंकारा में जन्मे; आर्य समाज के संस्थापक (1875)।", "टंकारा येथे जन्म; आर्य समाजाचे संस्थापक (1875)."), ("Reform", "सुधार", "सुधारणा")),
        person("jamsetji", ("Jamsetji Tata", "जमशेदजी टाटा", "जमशेदजी टाटा"), ("Born at Navsari; founder of the Tata group.", "नवसारी में जन्मे; टाटा समूह के संस्थापक।", "नवसारी येथे जन्म; टाटा समूहाचे संस्थापक."), ("Industry", "उद्योग", "उद्योग")),
        person("sarabhai", ("Vikram Sarabhai", "विक्रम साराभाई", "विक्रम साराभाई"), ("Ahmedabad-born physicist; founded the Physical Research Laboratory and India's space programme.", "अहमदाबाद में जन्मे भौतिक विज्ञानी; भौतिक अनुसंधान प्रयोगशाला और भारत के अंतरिक्ष कार्यक्रम के संस्थापक।", "अहमदाबादमध्ये जन्मलेले भौतिकशास्त्रज्ञ; भौतिक संशोधन प्रयोगशाळा व भारताच्या अवकाश कार्यक्रमाचे संस्थापक."), ("Science", "विज्ञान", "विज्ञान")),
        person("meghani", ("Zaverchand Meghani", "झवेरचंद मेघाणी", "झवेरचंद मेघाणी"), ("Poet and collector of Saurashtra's folk literature, called 'Rashtriya Shayar' by Gandhi.", "कवि और सौराष्ट्र के लोक साहित्य के संग्राहक, जिन्हें गांधी ने 'राष्ट्रीय शायर' कहा।", "कवी व सौराष्ट्राच्या लोकसाहित्याचे संग्राहक; गांधींनी त्यांना 'राष्ट्रीय शायर' म्हटले."), ("Literature", "साहित्य", "साहित्य")),
        person("kurien", ("Verghese Kurien", "वर्गीज़ कुरियन", "व्हर्गीस कुरियन"), ("Built the Amul co-operative at Anand and led India's White Revolution.", "आणंद में अमूल सहकारी संस्था बनाई और भारत की श्वेत क्रांति का नेतृत्व किया।", "आणंद येथे अमूल सहकारी संस्था उभारली आणि भारताच्या धवलक्रांतीचे नेतृत्व केले."), ("Co-operatives", "सहकारिता", "सहकार")),
        person("dhirubhai", ("Dhirubhai Ambani", "धीरूभाई अंबानी", "धीरूभाई अंबानी"), ("From Chorwad; founder of Reliance Industries.", "चोरवाड़ के; रिलायंस इंडस्ट्रीज़ के संस्थापक।", "चोरवाडचे; रिलायन्स इंडस्ट्रीजचे संस्थापक."), ("Industry", "उद्योग", "उद्योग")),
        person("morarji", ("Morarji Desai", "मोरारजी देसाई", "मोरारजी देसाई"), ("Born at Bhadeli (Valsad); Prime Minister of India (1977–79).", "भदेली (वलसाड) में जन्मे; भारत के प्रधानमंत्री (1977–79)।", "भदेली (वलसाड) येथे जन्म; भारताचे पंतप्रधान (1977–79)."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Gujaratis are among the most widespread of Indian communities. Traders from Kutch and Saurashtra sailed to Oman, Zanzibar and the East African coast for centuries; in the colonial period many settled in Kenya, Uganda and Tanzania, and after the expulsions of the 1970s large numbers moved to the United Kingdom, where Leicester and north-west London have large Gujarati populations. Since the 1960s many have settled in the United States, Canada and Australia, often in business. Within India, Gujarati communities are prominent in Mumbai and in trading towns across the country.",
        "गुजराती भारत के सबसे व्यापक रूप से फैले समुदायों में हैं। कच्छ और सौराष्ट्र के व्यापारी सदियों से ओमान, ज़ांज़ीबार और पूर्वी अफ़्रीकी तट तक जाते रहे; औपनिवेशिक काल में बहुत से लोग केन्या, युगांडा और तंज़ानिया में बसे, और 1970 के दशक के निष्कासनों के बाद बड़ी संख्या में लोग ब्रिटेन गए, जहाँ लेस्टर और उत्तर-पश्चिम लंदन में बड़ी गुजराती आबादी है। 1960 के दशक से बहुत से लोग संयुक्त राज्य अमेरिका, कनाडा और ऑस्ट्रेलिया में बसे हैं, अक्सर व्यापार में। भारत के भीतर, मुंबई और देश भर के व्यापारिक नगरों में गुजराती समुदाय प्रमुख हैं।",
        "गुजराती हे भारतातील सर्वांत दूरवर पसरलेल्या समुदायांपैकी आहेत. कच्छ व सौराष्ट्रातील व्यापारी शतकानुशतके ओमान, झांझिबार व पूर्व आफ्रिकेच्या किनाऱ्यापर्यंत जात असत; वसाहतकाळात अनेक जण केनिया, युगांडा व टांझानियात स्थायिक झाले, आणि 1970 च्या दशकातील हकालपट्टीनंतर मोठ्या संख्येने लोक ब्रिटनमध्ये गेले, जिथे लेस्टर व वायव्य लंडनमध्ये मोठी गुजराती लोकसंख्या आहे. 1960 च्या दशकापासून अनेक जण अमेरिका, कॅनडा व ऑस्ट्रेलियात, बहुतेकदा व्यवसायात, स्थायिक झाले आहेत. भारतात मुंबई व देशभरातील व्यापारी शहरांत गुजराती समुदाय ठळकपणे आढळतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants and internal migrants", "प्रवासियों और आंतरिक प्रवासियों की संख्या", "परदेशी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; MEA."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Gujarat portal", "गुजरात सरकार पोर्टल", "गुजरात शासन संकेतस्थळ", url="https://gujaratindia.gov.in", src="india-gov"),
        it3("digitalgujarat", "Digital Gujarat — certificates and services", "डिजिटल गुजरात — प्रमाणपत्र और सेवाएँ", "डिजिटल गुजरात — प्रमाणपत्रे व सेवा", url="https://www.digitalgujarat.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Gujarat Tourism", "गुजरात पर्यटन", "गुजरात पर्यटन", url="https://www.gujarattourism.com", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Ahmedabad", "अहमदाबाद", "अहमदाबाद"), "079"], [L("Surat", "सूरत", "सुरत"), "0261"], [L("Vadodara", "वडोदरा", "वडोदरा"), "0265"],
           [L("Rajkot", "राजकोट", "राजकोट"), "0281"], [L("Bhavnagar", "भावनगर", "भावनगर"), "0278"], [L("Jamnagar", "जामनगर", "जामनगर"), "0288"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [(L("Verified local business directory", "सत्यापित स्थानीय व्यवसाय निर्देशिका", "पडताळलेली स्थानिक उद्योग सूची"), "india-gov", "Udyam Registration and co-operative registrars.")]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("coast", ("Gujarat has India's longest coastline among the States, about 1,600 km.", "राज्यों में गुजरात की तटरेखा सबसे लंबी है, लगभग 1,600 किमी।", "राज्यांमध्ये गुजरातची किनारपट्टी सर्वांत लांब आहे, सुमारे 1,600 किमी.")),
        triv("lion", ("The forests of Gir and Saurashtra are the only place in the world where Asiatic lions live in the wild.", "गिर और सौराष्ट्र के वन दुनिया में एकमात्र स्थान हैं जहाँ एशियाई सिंह प्राकृतिक रूप से रहते हैं।", "गीर व सौराष्ट्राची जंगले हे जगातील एकमेव ठिकाण आहे जिथे आशियाई सिंह नैसर्गिकरीत्या राहतात.")),
        triv("ahmedabad", ("Ahmedabad was the first Indian city to be inscribed as a UNESCO World Heritage City (2017).", "अहमदाबाद यूनेस्को विश्व धरोहर नगर घोषित होने वाला पहला भारतीय शहर था (2017)।", "युनेस्को जागतिक वारसा शहर म्हणून घोषित झालेले अहमदाबाद हे पहिले भारतीय शहर (2017)."), UNESCO, "unesco-whc"),
        triv("garba", ("Garba of Gujarat was added to UNESCO's list of the Intangible Cultural Heritage of Humanity in 2023.", "गुजरात का गरबा 2023 में यूनेस्को की मानवता की अमूर्त सांस्कृतिक धरोहर सूची में शामिल हुआ।", "गुजरातचा गरबा 2023 मध्ये युनेस्कोच्या मानवतेच्या अमूर्त सांस्कृतिक वारसा यादीत समाविष्ट झाला.")),
        triv("diamond", ("Surat cut diamonds became a registered GI — one of the newest in the list.", "सूरत के तराशे हीरे पंजीकृत जीआई बने — सूची के सबसे नए जीआई में से एक।", "सुरतचे पैलू पाडलेले हिरे नोंदणीकृत जीआय झाले — यादीतील सर्वांत नव्यांपैकी एक."), GI_PDF, "gi-registry"),
        triv("unity", ("The Statue of Unity of Sardar Patel, at 182 m, is the tallest statue in the world.", "182 मीटर ऊँची सरदार पटेल की स्टैच्यू ऑफ़ यूनिटी दुनिया की सबसे ऊँची प्रतिमा है।", "सरदार पटेलांचा 182 मीटर उंच स्टॅच्यू ऑफ युनिटी हा जगातील सर्वांत उंच पुतळा आहे.")),
        triv("ls", ("The State elects 26 members to the Lok Sabha.", "राज्य से लोकसभा के 26 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 26 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("gj mod3 ok")
