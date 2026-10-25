"""Nagaland modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-NL"
nl = read("regions/IN-NL.json")["metrics"]; ind = read("india.json")["metrics"]
C = research("census_b5plus.json"); F = C["forest"]["NL"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About 74% of Nagaland is forest (ISFR 2023), much of it owned by villages and clans rather than the State, which makes community conservation especially important. Forests range from tropical evergreen in the foothills to subtropical and temperate broadleaf forest and rhododendron on the high ridges. Wildlife includes the hoolock gibbon, the Blyth's tragopan (the State bird), the mithun (the State animal), hornbills and the Amur falcon, which stops over in huge numbers at Doyang reservoir in Wokha every autumn — once hunted, now protected by the villages. Ntangki National Park and the Fakim, Pulie Badze and Rangapahar sanctuaries are the main protected areas, and Khonoma has a community-run sanctuary.\n\nThere are no Ramsar sites in Nagaland on the list as on 21 April 2026.",
        "नागालैंड का लगभग 74% भाग वन है (आईएसएफ़आर 2023), जिसका अधिकांश भाग राज्य के बजाय गाँवों और कुलों के स्वामित्व में है, इसलिए सामुदायिक संरक्षण विशेष रूप से महत्त्वपूर्ण है। वन तलहटी के उष्णकटिबंधीय सदाबहार से ऊँची पहाड़ियों पर उपोष्ण और समशीतोष्ण चौड़ी पत्ती वाले वन और बुरांश तक फैले हैं। वन्यजीवों में हूलॉक गिबन, ब्लाइथ ट्रैगोपैन (राज्य पक्षी), मिथुन (राज्य पशु), धनेश और अमूर बाज़ शामिल हैं, जो हर शरद में वोखा के दोयांग जलाशय पर भारी संख्या में रुकते हैं — कभी इनका शिकार होता था, अब गाँव इनकी रक्षा करते हैं। नटांगकी राष्ट्रीय उद्यान और फ़ाकिम, पुलिए बाद्ज़े और रंगापहाड़ अभयारण्य मुख्य संरक्षित क्षेत्र हैं, और खोनोमा में समुदाय द्वारा चलाया जाने वाला अभयारण्य है।\n\n21 अप्रैल 2026 की सूची में नागालैंड में कोई रामसर स्थल नहीं है।",
        "नागालँडचा सुमारे 74% भाग वनाच्छादित आहे (आयएसएफआर 2023), ज्यातील बहुतांश राज्याऐवजी गावे व कुळांच्या मालकीचे आहे, त्यामुळे सामुदायिक संवर्धन विशेष महत्त्वाचे आहे. जंगले पायथ्याच्या उष्णकटिबंधीय सदाहरितांपासून उंच कड्यांवरील उपोष्ण व समशीतोष्ण रुंदपर्णी जंगले व ऱ्होडोडेंड्रॉनपर्यंत आहेत. वन्यजीवांत हूलॉक गिबन, ब्लायथ ट्रॅगोपॅन (राज्यपक्षी), मिथुन (राज्यप्राणी), धनेश व अमूर ससाणा यांचा समावेश आहे, जो दर शरद ऋतूत वोखाच्या दोयांग जलाशयावर प्रचंड संख्येने थांबतो — एकेकाळी त्याची शिकार होई, आता गावे त्याचे रक्षण करतात. नटांगकी राष्ट्रीय उद्यान व फाकिम, पुलिए बाद्झे आणि रंगापहाड अभयारण्ये ही मुख्य संरक्षित क्षेत्रे आहेत, आणि खोनोमामध्ये समुदायचालित अभयारण्य आहे.\n\n21 एप्रिल 2026 च्या यादीत नागालँडमध्ये कोणतेही रामसर स्थळ नाही."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), nl["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(0, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: none in Nagaland."), "number"),
    ]),
    lst("protected", [
        it3("ntangki", "Ntangki National Park", "नटांगकी राष्ट्रीय उद्यान", "नटांगकी राष्ट्रीय उद्यान", m=("Peren district", "पेरेन ज़िला", "पेरेन जिल्हा")),
        it3("fakim", "Fakim Wildlife Sanctuary", "फ़ाकिम वन्यजीव अभयारण्य", "फाकिम वन्यजीव अभयारण्य", m=("Near Saramati", "सारामती के पास", "सारामतीजवळ")),
        it3("puliebadze", "Pulie Badze Wildlife Sanctuary", "पुलिए बाद्ज़े वन्यजीव अभयारण्य", "पुलिए बाद्झे वन्यजीव अभयारण्य", m=("Above Kohima", "कोहिमा के ऊपर", "कोहिमावर")),
        it3("khonoma", "Khonoma Nature Conservation and Tragopan Sanctuary", "खोनोमा प्रकृति संरक्षण और ट्रैगोपैन अभयारण्य", "खोनोमा निसर्ग संवर्धन व ट्रॅगोपॅन अभयारण्य", m=("Community-run", "समुदाय द्वारा संचालित", "समुदायचालित")),
        it3("doyang", "Doyang reservoir", "दोयांग जलाशय", "दोयांग जलाशय", m=("Amur falcon roost", "अमूर बाज़ का बसेरा", "अमूर ससाण्याचा थांबा")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("mithun", "Mithun (State animal)", "मिथुन (राज्य पशु)", "मिथुन (राज्यप्राणी)"), it3("tragopan", "Blyth's tragopan (State bird)", "ब्लाइथ ट्रैगोपैन (राज्य पक्षी)", "ब्लायथ ट्रॅगोपॅन (राज्यपक्षी)"),
        it3("falcon", "Amur falcon", "अमूर बाज़", "अमूर ससाणा"), it3("gibbon", "Hoolock gibbon", "हूलॉक गिबन", "हूलॉक गिबन"),
        it3("hornbill", "Hornbills", "धनेश", "धनेश"), it3("lily", "Dzükou lily", "ज़ुकू लिली", "झुकू लिली"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Amur falcon counts at Doyang", "दोयांग में अमूर बाज़ों की संख्या", "दोयांग येथील अमूर ससाण्यांची संख्या"), "india-gov", "Nagaland Forest Department / WII."),
        (L("Community-conserved areas — official list", "सामुदायिक संरक्षित क्षेत्र — आधिकारिक सूची", "सामुदायिक संवर्धित क्षेत्रे — अधिकृत यादी"), "india-gov", "Nagaland Forest Department."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Most of Nagaland's villages and towns depend on springs, streams and rainwater, collected from roofs into tanks. Kohima in particular faces dry-season water shortages, and water is often delivered by tanker. The Doyang reservoir is the State's largest water body. Terraced rice fields in the Angami and Chakhesang areas are irrigated by channels that carry stream water along the hillsides, a centuries-old system.",
        "नागालैंड के अधिकांश गाँव और नगर झरनों, धाराओं और वर्षा जल पर निर्भर हैं, जिसे छतों से टंकियों में इकट्ठा किया जाता है। विशेषकर कोहिमा में सूखे मौसम में पानी की कमी होती है, और पानी अक्सर टैंकर से पहुँचाया जाता है। दोयांग जलाशय राज्य का सबसे बड़ा जलाशय है। अंगामी और चाखेसांग क्षेत्रों के सीढ़ीदार धान के खेत उन नहरों से सींचे जाते हैं जो पहाड़ी ढलानों के साथ धारा का पानी ले जाती हैं, जो सदियों पुरानी व्यवस्था है।",
        "नागालँडमधील बहुतेक गावे व शहरे झरे, ओढे व पावसाच्या पाण्यावर अवलंबून आहेत, जे छपरांवरून टाक्यांत साठवले जाते. विशेषतः कोहिमाला कोरड्या ऋतूत पाणीटंचाई जाणवते, आणि पाणी अनेकदा टँकरने पुरवले जाते. दोयांग जलाशय हा राज्यातील सर्वांत मोठा जलसाठा आहे. अंगामी व चाखेसांग भागांतील पायऱ्यांच्या भातशेतांना डोंगरउतारांवरून ओढ्यांचे पाणी वाहून नेणाऱ्या कालव्यांनी पाणी दिले जाते, ही शतकानुशतकांची पद्धत आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Household tap-water coverage", "घरेलू नल जल कवरेज", "घरगुती नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Nagaland lies in a high earthquake zone, and landslides on the hill roads are the most common hazard in the monsoon, sometimes cutting NH-29 between Dimapur and Kohima. Visitors need an Inner Line Permit and should carry identity documents, check road conditions before travel, and follow local advice when visiting remote villages and border areas.",
        "नागालैंड उच्च भूकंप क्षेत्र में है, और पहाड़ी सड़कों पर भूस्खलन मानसून का सबसे आम ख़तरा है, जो कभी-कभी दीमापुर और कोहिमा के बीच एनएच-29 को काट देता है। पर्यटकों को इनर लाइन परमिट चाहिए, पहचान पत्र साथ रखने चाहिए, यात्रा से पहले सड़क की स्थिति देखनी चाहिए, और दूरस्थ गाँवों और सीमावर्ती क्षेत्रों में जाते समय स्थानीय सलाह माननी चाहिए।",
        "नागालँड उच्च भूकंप क्षेत्रात आहे, आणि डोंगरी रस्त्यांवरील भूस्खलन हा पावसाळ्यातील सर्वांत सामान्य धोका आहे, जो कधीकधी दिमापूर व कोहिमादरम्यान एनएच-29 तोडतो. पर्यटकांना इनर लाइन परवाना लागतो, त्यांनी ओळखपत्रे जवळ ठेवावीत, प्रवासापूर्वी रस्त्यांची स्थिती तपासावी, आणि दुर्गम गावे व सीमाभागांना भेट देताना स्थानिक सल्ला पाळावा."),
        conf="Editorial"),
    emergency_table(("Nagaland", "नागालैंड", "नागालँड")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official address."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Five GIs belong to Nagaland on the GI Registry's list as on 31 December 2025. Naga mircha, the king chilli filed in 2007, was among the earliest GIs from the North-East; Naga tree tomato, Naga cucumber and the Chakhesang shawl followed, and Chak-hao, the aromatic black rice, is shared with Manipur.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में पाँच जीआई नागालैंड के हैं। 2007 में दायर राजा मिर्च, नागा मिर्च, पूर्वोत्तर के सबसे पहले जीआई में थी; इसके बाद नागा ट्री टमाटर, नागा खीरा और चाखेसांग शॉल आए, और सुगंधित काला चावल चाक-हाओ मणिपुर के साथ साझा है।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत पाच जीआय नागालँडचे आहेत. 2007 मध्ये दाखल राजा मिरची, नागा मिरची, ईशान्येतील सर्वांत पहिल्या जीआयपैकी होती; त्यानंतर नागा झाड-टोमॅटो, नागा काकडी व चाखेसांग शाल आले, आणि सुगंधी काळा तांदूळ चाक-हाओ मणिपूरसोबत सामायिक आहे."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Pending GI applications from Nagaland", "नागालैंड के लंबित जीआई आवेदन", "नागालँडचे प्रलंबित जीआय अर्ज"), "gi-registry", "GI Registry application status search."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Kohima is the starting point for most visitors: the Kohima War Cemetery on the old battlefield, the State Museum, Kisama Heritage Village where the Hornbill Festival is held each December, and nearby Angami villages such as Khonoma, Jotsoma and Touphema. A trek from Viswema or Zakhama leads to the Dzükou valley, famous for its rolling green hills and summer lilies, and Japfü peak above it. Further north, Mokokchung is the heart of Ao country; Wokha has Doyang lake and the Amur falcons; and in Mon, Konyak villages such as Longwa straddle the Myanmar border. Dimapur has the Kachari ruins and the Chümoukedima heritage area.",
        "अधिकांश पर्यटकों के लिए कोहिमा आरंभ बिंदु है: पुराने युद्धक्षेत्र पर कोहिमा युद्ध समाधि स्थल, राज्य संग्रहालय, किसामा धरोहर गाँव जहाँ हर दिसंबर हॉर्नबिल महोत्सव होता है, और पास के खोनोमा, जोत्सोमा और तौफ़ेमा जैसे अंगामी गाँव। विस्वेमा या ज़ाखामा से एक ट्रेक ज़ुकू घाटी ले जाता है, जो हरी-भरी लहरदार पहाड़ियों और गर्मियों की लिली के लिए प्रसिद्ध है, और उसके ऊपर जाप्फ़ू चोटी। आगे उत्तर में मोकोकचुंग आओ क्षेत्र का हृदय है; वोखा में दोयांग झील और अमूर बाज़ हैं; और मोन में लोंगवा जैसे कोन्याक गाँव म्यांमार सीमा पर फैले हैं। दीमापुर में कचारी खंडहर और चुमौकेदिमा धरोहर क्षेत्र हैं।",
        "बहुतेक पर्यटकांसाठी कोहिमा हे सुरुवातीचे ठिकाण आहे: जुन्या रणभूमीवरील कोहिमा युद्धस्मशान, राज्य संग्रहालय, दर डिसेंबरला हॉर्नबिल महोत्सव भरतो ते किसामा वारसा गाव, आणि जवळची खोनोमा, जोत्सोमा व तौफेमा सारखी अंगामी गावे. विस्वेमा किंवा झाखामाहून ट्रेक झुकू खोऱ्याकडे जातो, जे हिरव्यागार लहरदार टेकड्या व उन्हाळी लिलींसाठी प्रसिद्ध आहे, आणि त्यावरील जाप्फू शिखर. पुढे उत्तरेला मोकोकचुंग हे आओ प्रदेशाचे हृदय आहे; वोखामध्ये दोयांग सरोवर व अमूर ससाणे आहेत; आणि मोनमध्ये लोंगवासारखी कोन्याक गावे म्यानमार सीमेवर पसरलेली आहेत. दिमापूरमध्ये कचारी अवशेष व चुमौकेदिमा वारसा क्षेत्र आहे."),
        conf="Editorial"),
    lst("places", [
        it3("kohima", "Kohima", "कोहिमा", "कोहिमा", m=("War cemetery, museum", "युद्ध समाधि स्थल, संग्रहालय", "युद्धस्मशान, संग्रहालय")),
        it3("kisama", "Kisama", "किसामा", "किसामा", m=("Hornbill Festival", "हॉर्नबिल महोत्सव", "हॉर्नबिल महोत्सव")),
        it3("dzukou", "Dzükou valley", "ज़ुकू घाटी", "झुकू खोरे", m=("Trek; summer lilies", "ट्रेक; गर्मियों की लिली", "ट्रेक; उन्हाळी लिली")),
        it3("khonoma", "Khonoma", "खोनोमा", "खोनोमा", m=("Angami village", "अंगामी गाँव", "अंगामी गाव")),
        it3("mokokchung", "Mokokchung", "मोकोकचुंग", "मोकोकचुंग", m=("Ao heartland", "आओ क्षेत्र का हृदय", "आओ प्रदेशाचे हृदय")),
        it3("longwa", "Longwa, Mon", "लोंगवा, मोन", "लोंगवा, मोन", m=("Konyak village on the border", "सीमा पर कोन्याक गाँव", "सीमेवरील कोन्याक गाव")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d4", "4 days", "4 दिन", "4 दिवस", d=("Kohima, Khonoma and Kisama, with a day trek to Dzükou.", "कोहिमा, खोनोमा और किसामा, ज़ुकू के एक दिन के ट्रेक के साथ।", "कोहिमा, खोनोमा व किसामा, झुकूच्या एकदिवसीय ट्रेकसह.")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Add Mokokchung, Wokha and Mon (Longwa).", "मोकोकचुंग, वोखा और मोन (लोंगवा) जोड़ें।", "मोकोकचुंग, वोखा व मोन (लोंगवा) जोडा.")),
        it3("hornbill", "Hornbill Festival (3 days)", "हॉर्नबिल महोत्सव (3 दिन)", "हॉर्नबिल महोत्सव (3 दिवस)", d=("Book early for stays in Kohima in early December.", "दिसंबर की शुरुआत में कोहिमा में ठहरने के लिए पहले से बुक करें।", "डिसेंबरच्या सुरुवातीला कोहिमात राहण्यासाठी आधीच नोंदणी करा.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    gaps("g", [
        (L("Hornbill Festival visitor numbers", "हॉर्नबिल महोत्सव में आगंतुकों की संख्या", "हॉर्नबिल महोत्सवातील पर्यटकसंख्या"), "tourism", "Nagaland Department of Tourism."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "cities", [
    lst("cities", [
        city("kohima", ("Kohima", "कोहिमा", "कोहिमा"), ("Hill capital at about 1,400 m.", "लगभग 1,400 मीटर पर पहाड़ी राजधानी।", "सुमारे 1,400 मीटरवरील डोंगरी राजधानी."), ("Capital", "राजधानी", "राजधानी")),
        city("dimapur", ("Dimapur", "दीमापुर", "दिमापूर"), ("Commercial hub with the airport and railway.", "हवाई अड्डे और रेलवे वाला वाणिज्यिक केंद्र।", "विमानतळ व रेल्वे असलेले व्यापारी केंद्र."), ("Commerce", "वाणिज्य", "व्यापार")),
        city("mokokchung", ("Mokokchung", "मोकोकचुंग", "मोकोकचुंग"), ("Cultural centre of the Ao.", "आओ लोगों का सांस्कृतिक केंद्र।", "आओ लोकांचे सांस्कृतिक केंद्र."), ("Culture", "संस्कृति", "संस्कृती")),
        city("tuensang", ("Tuensang", "त्वेनसांग", "त्वेनसांग"), ("Largest town of eastern Nagaland.", "पूर्वी नागालैंड का सबसे बड़ा नगर।", "पूर्व नागालँडमधील सर्वांत मोठे शहर."), ("Administration", "प्रशासन", "प्रशासन")),
        city("wokha", ("Wokha", "वोखा", "वोखा"), ("Lotha country; Doyang lake.", "लोथा क्षेत्र; दोयांग झील।", "लोथा प्रदेश; दोयांग सरोवर."), ("Nature", "प्रकृति", "निसर्ग")),
        city("mon", ("Mon", "मोन", "मोन"), ("Konyak heartland.", "कोन्याक क्षेत्र का हृदय।", "कोन्याक प्रदेशाचे हृदय."), ("Culture", "संस्कृति", "संस्कृती")),
    ], title=L("Major towns", "प्रमुख नगर", "प्रमुख शहरे"), conf="Editorial"),
    gaps("g", [
        (L("List of districts — official", "ज़िलों की सूची — आधिकारिक", "जिल्ह्यांची यादी — अधिकृत"), "india-gov", "Government of Nagaland; see the district-count note in the overview."),
        (L("Town populations (Census 2011)", "नगरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Football is the most popular game, and Nagaland has a long football history: Dr Talimeren Ao captained India at the 1948 London Olympics. Naga wrestling, a traditional sport, is held at festivals and State championships, and the Hornbill Festival hosts traditional games. Hokato Hotozhe Sema, a former soldier who lost a leg to a landmine, won a Paralympic bronze medal in shot put at Paris in 2024.",
        "फ़ुटबॉल सबसे लोकप्रिय खेल है, और नागालैंड का फ़ुटबॉल इतिहास लंबा है: डॉ. तालिमेरेन आओ ने 1948 के लंदन ओलंपिक में भारत की कप्तानी की। पारंपरिक खेल नागा कुश्ती त्योहारों और राज्य प्रतियोगिताओं में होती है, और हॉर्नबिल महोत्सव में पारंपरिक खेल होते हैं। बारूदी सुरंग में एक पैर गँवाने वाले पूर्व सैनिक होकातो होतोझे सेमा ने 2024 के पेरिस पैरालंपिक में गोला फेंक में कांस्य पदक जीता।",
        "फुटबॉल हा सर्वांत लोकप्रिय खेळ आहे, आणि नागालँडचा फुटबॉल इतिहास दीर्घ आहे: डॉ. तालिमेरेन आओ यांनी 1948 च्या लंडन ऑलिंपिकमध्ये भारताचे कर्णधारपद भूषवले. पारंपरिक खेळ नागा कुस्ती सण व राज्य स्पर्धांत होते, आणि हॉर्नबिल महोत्सवात पारंपरिक खेळ होतात. भूसुरुंगात पाय गमावलेले माजी सैनिक होकातो होतोझे सेमा यांनी 2024 च्या पॅरिस पॅरालिंपिकमध्ये गोळाफेकीत कांस्यपदक जिंकले."),
        conf="Editorial"),
    gaps("g", [(L("Major stadiums — official list", "प्रमुख स्टेडियम — आधिकारिक सूची", "प्रमुख स्टेडियम — अधिकृत यादी"), "india-gov", "Nagaland Department of Youth Resources and Sports.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("talimeren", ("Talimeren Ao", "तालिमेरेन आओ", "तालिमेरेन आओ"), ("Footballer and doctor who captained India at the 1948 Olympics.", "फ़ुटबॉलर और डॉक्टर जिन्होंने 1948 ओलंपिक में भारत की कप्तानी की।", "फुटबॉलपटू व डॉक्टर, ज्यांनी 1948 ऑलिंपिकमध्ये भारताचे कर्णधारपद भूषवले."), ("Sport", "खेल", "क्रीडा")),
        person("temsula", ("Temsula Ao", "तेमसुला आओ", "तेमसुला आओ"), ("Poet, short-story writer and scholar; Padma Shri and Sahitya Akademi awardee.", "कवयित्री, कहानीकार और विद्वान; पद्म श्री और साहित्य अकादमी पुरस्कार विजेता।", "कवयित्री, कथाकार व विदुषी; पद्मश्री व साहित्य अकादमी पुरस्कार विजेत्या."), ("Literature", "साहित्य", "साहित्य")),
        person("easterine", ("Easterine Kire", "ईस्टरिन किरे", "ईस्टरिन किरे"), ("Novelist and poet whose books tell Angami and Naga history.", "उपन्यासकार और कवयित्री जिनकी पुस्तकें अंगामी और नागा इतिहास कहती हैं।", "कादंबरीकार व कवयित्री, ज्यांची पुस्तके अंगामी व नागा इतिहास सांगतात."), ("Literature", "साहित्य", "साहित्य")),
        person("hokato", ("Hokato Hotozhe Sema", "होकातो होतोझे सेमा", "होकातो होतोझे सेमा"), ("Para athlete; bronze medal in shot put at the Paris 2024 Paralympics.", "पैरा एथलीट; पेरिस 2024 पैरालंपिक में गोला फेंक में कांस्य पदक।", "पॅरा खेळाडू; पॅरिस 2024 पॅरालिंपिकमध्ये गोळाफेकीत कांस्यपदक."), ("Sport", "खेल", "क्रीडा")),
        person("sccjamir", ("S. C. Jamir", "एस. सी. जमीर", "एस. सी. जमीर"), ("Former Chief Minister and Governor of several States.", "पूर्व मुख्यमंत्री और कई राज्यों के राज्यपाल।", "माजी मुख्यमंत्री व अनेक राज्यांचे राज्यपाल."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Many young Nagas study and work outside the State — in Delhi, Bengaluru, Pune, Guwahati and Shillong — especially in hospitality, aviation, healthcare and IT, and Naga students' unions are active in these cities. Naga communities also live across the border in Myanmar and in neighbouring Manipur, Assam and Arunachal Pradesh.",
        "बहुत से युवा नागा राज्य के बाहर पढ़ते और काम करते हैं — दिल्ली, बेंगलुरु, पुणे, गुवाहाटी और शिलांग में — विशेषकर आतिथ्य, विमानन, स्वास्थ्य सेवा और आईटी में, और इन नगरों में नागा छात्र संघ सक्रिय हैं। नागा समुदाय सीमा पार म्यांमार और पड़ोसी मणिपुर, असम और अरुणाचल प्रदेश में भी रहते हैं।",
        "अनेक तरुण नागा राज्याबाहेर शिकतात व काम करतात — दिल्ली, बंगळुरू, पुणे, गुवाहाटी व शिलाँगमध्ये — विशेषतः आतिथ्य, विमानवाहतूक, आरोग्यसेवा व आयटीत, आणि या शहरांत नागा विद्यार्थी संघटना सक्रिय आहेत. नागा समुदाय सीमेपलीकडे म्यानमारमध्ये व शेजारच्या मणिपूर, आसाम आणि अरुणाचल प्रदेशातही राहतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Out-migration from the State — official estimate", "राज्य से बाहर प्रवास — आधिकारिक अनुमान", "राज्याबाहेर स्थलांतर — अधिकृत अंदाज"), "census", "Census 2011 migration tables (D-series)."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Nagaland portal", "नागालैंड सरकार पोर्टल", "नागालँड शासन संकेतस्थळ", url="https://www.nagaland.gov.in", src="india-gov"),
        it3("ipr", "Department of Information and Public Relations", "सूचना एवं जनसंपर्क विभाग", "माहिती व जनसंपर्क विभाग", url="https://ipr.nagaland.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes", "एसटीडी कोड", "एसटीडी कोड"),
          [col(L("Area", "क्षेत्र", "क्षेत्र")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Kohima", "कोहिमा", "कोहिमा"), "0370"], [L("Dimapur", "दीमापुर", "दिमापूर"), "03862"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय; दूरसंचार विभाग की नंबरिंग योजना से जाँचा जाएगा।", "संपादकीय; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळले जाईल.")),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("st", ("Scheduled Tribes made up 86.5% of Nagaland's population in 2011.", "2011 में नागालैंड की जनसंख्या में अनुसूचित जनजातियों का हिस्सा 86.5% था।", "2011 मध्ये नागालँडच्या लोकसंख्येत अनुसूचित जमातींचा वाटा 86.5% होता."), "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf", "dl-planning"),
        triv("forest", ("About 74% of the State is forest (ISFR 2023).", "राज्य का लगभग 74% भाग वन है (आईएसएफ़आर 2023)।", "राज्याचा सुमारे 74% भाग वनाच्छादित आहे (आयएसएफआर 2023)."), LS_FOREST, "fsi"),
        triv("mircha", ("Naga mircha was registered as a GI on an application filed in 2007.", "नागा मिर्च 2007 में दायर आवेदन पर जीआई के रूप में पंजीकृत हुई।", "नागा मिरची 2007 मध्ये दाखल अर्जावर जीआय म्हणून नोंदणीकृत झाली."), GI_PDF, "gi-registry"),
        triv("hornbill", ("The Hornbill Festival is named after the bird revered in Naga folklore.", "हॉर्नबिल महोत्सव का नाम नागा लोककथाओं में पूजनीय पक्षी पर रखा गया है।", "हॉर्नबिल महोत्सवाचे नाव नागा लोककथांत पूजनीय पक्ष्यावरून ठेवले आहे.")),
        triv("english", ("English is the official language of Nagaland.", "अंग्रेज़ी नागालैंड की राजभाषा है।", "इंग्रजी ही नागालँडची राजभाषा आहे.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("nl mod3 ok")
