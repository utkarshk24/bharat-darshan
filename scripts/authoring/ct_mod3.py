"""Chhattisgarh modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-CT"
ct = read("regions/IN-CT.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About 41% of Chhattisgarh is forest (ISFR 2023) — sal in the north and centre, mixed teak and bamboo forests in the south. The State has several tiger reserves: Indravati in Bijapur, Udanti–Sitanadi in Gariaband and Dhamtari, Achanakmar in Mungeli and Bilaspur, and Guru Ghasidas–Tamor Pingla in the north. Kanger Valley National Park near Jagdalpur has limestone caves such as Kotumsar, and Barnawapara is a popular sanctuary near Raipur. The wild water buffalo, the State animal, survives in small numbers in Udanti–Sitanadi and Indravati, and the hill myna, the State bird, lives in Bastar's forests. Elephants have moved into the northern forests in recent decades.\n\nKopra Jalashay, a reservoir near Bilaspur, is the State's only Ramsar site, designated in 2025.",
        "छत्तीसगढ़ का लगभग 41% भाग वन है (आईएसएफ़आर 2023) — उत्तर और मध्य में साल, दक्षिण में सागौन और बाँस के मिश्रित वन। राज्य में कई बाघ अभयारण्य हैं: बीजापुर में इंद्रावती, गरियाबंद और धमतरी में उदंती–सीतानदी, मुंगेली और बिलासपुर में अचानकमार, और उत्तर में गुरु घासीदास–तमोर पिंगला। जगदलपुर के पास कांगेर घाटी राष्ट्रीय उद्यान में कोटमसर जैसी चूना-पत्थर की गुफाएँ हैं, और बारनवापारा रायपुर के पास लोकप्रिय अभयारण्य है। राज्य पशु वन भैंसा उदंती–सीतानदी और इंद्रावती में कम संख्या में बचा है, और राज्य पक्षी पहाड़ी मैना बस्तर के वनों में रहती है। पिछले दशकों में हाथी उत्तरी वनों में आ गए हैं।\n\nबिलासपुर के पास कोपरा जलाशय राज्य का एकमात्र रामसर स्थल है, जो 2025 में घोषित हुआ।",
        "छत्तीसगडचा सुमारे 41% भाग वनाच्छादित आहे (आयएसएफआर 2023) — उत्तर व मध्य भागात साल, दक्षिणेत साग व बांबूची मिश्र वने. राज्यात अनेक व्याघ्र प्रकल्प आहेत: बिजापूरमधील इंद्रावती, गरियाबंद व धमतरीतील उदंती–सीतानदी, मुंगेली व बिलासपूरमधील अचानकमार, आणि उत्तरेतील गुरु घासीदास–तमोर पिंगला. जगदलपूरजवळील कांगेर खोरे राष्ट्रीय उद्यानात कोटमसरसारख्या चुनखडीच्या गुहा आहेत, आणि बारनवापारा हे रायपूरजवळील लोकप्रिय अभयारण्य आहे. राज्यप्राणी रानरेडा उदंती–सीतानदी व इंद्रावतीत अल्प संख्येत टिकून आहे, आणि राज्यपक्षी पहाडी मैना बस्तरच्या जंगलांत राहते. गेल्या काही दशकांत हत्ती उत्तरेकडील जंगलांत आले आहेत.\n\nबिलासपूरजवळील कोपरा जलाशय हे राज्यातील एकमेव रामसर स्थळ आहे, जे 2025 मध्ये घोषित झाले."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(55811.75, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(55830.88, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), ct["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(1, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: Kopra Jalashay, 210 ha, designated 8 August 2025."), "number"),
    ]),
    lst("protected", [
        it3("indravati", "Indravati Tiger Reserve", "इंद्रावती बाघ अभयारण्य", "इंद्रावती व्याघ्र प्रकल्प", m=("Bijapur", "बीजापुर", "बिजापूर")),
        it3("udanti", "Udanti–Sitanadi Tiger Reserve", "उदंती–सीतानदी बाघ अभयारण्य", "उदंती–सीतानदी व्याघ्र प्रकल्प", m=("Wild buffalo", "वन भैंसा", "रानरेडा")),
        it3("achanakmar", "Achanakmar Tiger Reserve", "अचानकमार बाघ अभयारण्य", "अचानकमार व्याघ्र प्रकल्प", m=("Biosphere reserve with Amarkantak", "अमरकंटक के साथ जैवमंडल आरक्षित क्षेत्र", "अमरकंटकसह जैवमंडल राखीव")),
        it3("kanger", "Kanger Valley National Park", "कांगेर घाटी राष्ट्रीय उद्यान", "कांगेर खोरे राष्ट्रीय उद्यान", m=("Caves; Tirathgarh falls", "गुफाएँ; तीरथगढ़ जलप्रपात", "गुहा; तीरथगड धबधबा")),
        it3("barnawapara", "Barnawapara Wildlife Sanctuary", "बारनवापारा वन्यजीव अभयारण्य", "बारनवापारा वन्यजीव अभयारण्य", m=("Near Raipur", "रायपुर के पास", "रायपूरजवळ")),
        it3("kopra", "Kopra Jalashay", "कोपरा जलाशय", "कोपरा जलाशय", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("buffalo", "Wild water buffalo (State animal)", "वन भैंसा (राज्य पशु)", "रानरेडा (राज्यप्राणी)"), it3("myna", "Hill myna (State bird)", "पहाड़ी मैना (राज्य पक्षी)", "पहाडी मैना (राज्यपक्षी)"),
        it3("tiger", "Tiger", "बाघ", "वाघ"), it3("elephant", "Asian elephant", "एशियाई हाथी", "आशियाई हत्ती"),
        it3("gaur", "Gaur", "गौर", "गवा"), it3("sloth", "Sloth bear", "भालू", "अस्वल"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger estimate", "बाघों का अनुमान", "वाघांचा अंदाज"), "ntca", "NTCA All India Tiger Estimation."),
        (L("Wild buffalo population", "वन भैंसों की संख्या", "रानरेड्यांची संख्या"), "india-gov", "Chhattisgarh Forest Department."),
        (L("Tiger reserves — notification dates", "बाघ अभयारण्य — अधिसूचना तिथियाँ", "व्याघ्र प्रकल्प — अधिसूचना तारखा"), "ntca", "NTCA list of tiger reserves."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Most of Chhattisgarh lies in the upper Mahanadi basin, with the south draining to the Godavari through the Indravati and Sabari, and the north to the Ganga through the Son. The Gangrel (Ravishankar Sagar) dam on the Mahanadi near Dhamtari, the Hasdeo Bango (Minimata) dam near Korba and older tanks such as Tandula irrigate the plains, but much farmland still depends on the monsoon. The sharing of Mahanadi water with Odisha is disputed and before a tribunal. Industrial use, coal mining and fluoride in some areas affect water quality; ponds (talabs) in every village remain central to daily life.",
        "छत्तीसगढ़ का अधिकांश भाग ऊपरी महानदी बेसिन में है, जबकि दक्षिण इंद्रावती और सबरी के माध्यम से गोदावरी में और उत्तर सोन के माध्यम से गंगा में बहता है। धमतरी के पास महानदी पर गंगरेल (रविशंकर सागर) बाँध, कोरबा के पास हसदेव बांगो (मिनीमाता) बाँध और तांदुला जैसे पुराने जलाशय मैदानों की सिंचाई करते हैं, लेकिन बहुत सी खेती अब भी मानसून पर निर्भर है। ओडिशा के साथ महानदी जल का बँटवारा विवादित है और एक न्यायाधिकरण के समक्ष है। औद्योगिक उपयोग, कोयला खनन और कुछ क्षेत्रों में फ़्लोराइड जल गुणवत्ता को प्रभावित करते हैं; हर गाँव के तालाब दैनिक जीवन के केंद्र में हैं।",
        "छत्तीसगडचा बहुतांश भाग वरच्या महानदी खोऱ्यात आहे, तर दक्षिण भाग इंद्रावती व सबरीमार्गे गोदावरीत आणि उत्तर भाग सोनमार्गे गंगेत वाहतो. धमतरीजवळ महानदीवरील गंगरेल (रविशंकर सागर) धरण, कोरब्याजवळील हसदेव बांगो (मिनीमाता) धरण व तांदुलासारखे जुने जलाशय मैदानांना सिंचन देतात, पण बरीच शेती अजूनही मान्सूनवर अवलंबून आहे. ओडिशासोबत महानदीच्या पाणीवाटपाचा वाद लवादासमोर आहे. औद्योगिक वापर, कोळसा खाणकाम व काही भागांतील फ्लोराइड पाण्याच्या गुणवत्तेवर परिणाम करतात; प्रत्येक गावातील तलाव दैनंदिन जीवनाच्या केंद्रस्थानी आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Irrigated area", "सिंचित क्षेत्र", "सिंचित क्षेत्र"), "india-gov", "Chhattisgarh Economic Survey / Water Resources Department."),
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Heatwaves are the main weather hazard on the plains in April–June, and lightning and occasional floods in the Mahanadi basin occur during the monsoon. Human–elephant conflict causes deaths and crop losses in the northern districts. Left-wing extremist violence has affected parts of the forested southern districts; visitors to the interior of Bastar should travel by day and follow official advisories. Air quality around industrial clusters such as Korba and Raigarh can be poor.",
        "मैदानों में अप्रैल–जून में लू मुख्य मौसमी ख़तरा है, और मानसून में आकाशीय बिजली और कभी-कभी महानदी बेसिन में बाढ़ आती है। उत्तरी ज़िलों में मनुष्य–हाथी संघर्ष से मौतें और फ़सल नुकसान होते हैं। वनाच्छादित दक्षिणी ज़िलों के कुछ भाग वामपंथी उग्रवादी हिंसा से प्रभावित रहे हैं; बस्तर के भीतरी भागों में जाने वाले पर्यटकों को दिन में यात्रा करनी चाहिए और आधिकारिक सलाह माननी चाहिए। कोरबा और रायगढ़ जैसे औद्योगिक क्षेत्रों के आसपास वायु गुणवत्ता ख़राब हो सकती है।",
        "मैदानांत एप्रिल–जूनमध्ये उष्णतेची लाट हा मुख्य हवामान धोका आहे, आणि पावसाळ्यात वीज कोसळणे व कधीकधी महानदी खोऱ्यात पूर येतो. उत्तरेकडील जिल्ह्यांत माणूस–हत्ती संघर्षामुळे मृत्यू व पीकहानी होते. वनाच्छादित दक्षिणेकडील जिल्ह्यांचे काही भाग डाव्या अतिरेकी हिंसाचाराने बाधित राहिले आहेत; बस्तरच्या अंतर्गत भागात जाणाऱ्या पर्यटकांनी दिवसा प्रवास करावा व अधिकृत सूचना पाळाव्यात. कोरबा व रायगडसारख्या औद्योगिक भागांभोवती हवेची गुणवत्ता खराब असू शकते."),
        conf="Editorial"),
    emergency_table(("Chhattisgarh", "छत्तीसगढ़", "छत्तीसगड")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official address."),
        (L("Heatwave and lightning deaths by year", "वर्षवार लू और आकाशीय बिजली से मौतें", "वर्षनिहाय उष्माघात व वीज कोसळून मृत्यू"), "india-gov", "NCRB Accidental Deaths and Suicides in India."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Chhattisgarh has 7 registered Geographical Indications in the GI Registry's list as on 31 December 2025, with no shared entries. Three Bastar crafts were filed together in March 2007 — Bastar iron craft, Bastar Dhokra (with a separate logo registration in 2012) and Bastar wooden craft — and Champa silk sarees and fabrics followed in 2009. Two aromatic rice varieties from the plains, Jeeraphool and Nagri Dubraj, are the State's agricultural GIs.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में छत्तीसगढ़ के 7 पंजीकृत भौगोलिक संकेतक हैं, और कोई साझा प्रविष्टि नहीं है। बस्तर के तीन शिल्प मार्च 2007 में एक साथ दायर हुए — बस्तर लौह शिल्प, बस्तर ढोकरा (2012 में अलग लोगो पंजीकरण सहित) और बस्तर काष्ठ शिल्प — और 2009 में चांपा रेशम साड़ियाँ और वस्त्र आए। मैदानों की दो सुगंधित धान किस्में, जीराफूल और नगरी दुबराज, राज्य के कृषि जीआई हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत छत्तीसगडची 7 नोंदणीकृत भौगोलिक मानांकने आहेत, आणि एकही सामायिक नोंद नाही. बस्तरच्या तीन हस्तकला मार्च 2007 मध्ये एकत्र दाखल झाल्या — बस्तर लोखंडी हस्तकला, बस्तर ढोकरा (2012 मध्ये स्वतंत्र बोधचिन्ह नोंदणीसह) व बस्तर लाकडी हस्तकला — आणि 2009 मध्ये चांपा रेशीम साड्या व वस्त्रे आली. मैदानांतील दोन सुगंधी भात वाण, जीराफूल व नगरी दुबराज, ही राज्याची कृषी जीआय आहेत."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Bastar is Chhattisgarh's great draw: Chitrakote falls on the Indravati, often called India's Niagara for its broad horseshoe shape, Tirathgarh falls and the Kotumsar caves in Kanger Valley, the Danteshwari temple at Dantewada, and the weekly tribal haats and Dussehra of Jagdalpur. Sirpur's brick temples and Buddhist monasteries, the Bhoramdeo temple in Kabirdham, Rajim's temples at the river confluence, Ratanpur and the hilltop Bamleshwari temple at Dongargarh are historic and pilgrimage sites. Mainpat, with its cool plateau and Tibetan settlement, is a hill retreat in the north, and Barnawapara and Achanakmar are wildlife destinations.",
        "बस्तर छत्तीसगढ़ का सबसे बड़ा आकर्षण है: इंद्रावती पर चित्रकोट जलप्रपात, जिसे अपने चौड़े घोड़े की नाल जैसे आकार के कारण अक्सर भारत का नियाग्रा कहा जाता है, कांगेर घाटी में तीरथगढ़ जलप्रपात और कोटमसर गुफाएँ, दंतेवाड़ा का दंतेश्वरी मंदिर, और जगदलपुर के साप्ताहिक आदिवासी हाट व दशहरा। सिरपुर के ईंट मंदिर और बौद्ध विहार, कबीरधाम का भोरमदेव मंदिर, नदी संगम पर राजिम के मंदिर, रतनपुर और डोंगरगढ़ का पहाड़ी बम्लेश्वरी मंदिर ऐतिहासिक और तीर्थ स्थल हैं। ठंडे पठार और तिब्बती बस्ती वाला मैनपाट उत्तर का पहाड़ी विश्राम स्थल है, और बारनवापारा व अचानकमार वन्यजीव गंतव्य हैं।",
        "बस्तर हे छत्तीसगडचे सर्वांत मोठे आकर्षण आहे: इंद्रावतीवरील चित्रकोट धबधबा, ज्याला त्याच्या रुंद नालाकृती आकारामुळे अनेकदा भारताचा नायगारा म्हटले जाते, कांगेर खोऱ्यातील तीरथगड धबधबा व कोटमसर गुहा, दंतेवाड्याचे दंतेश्वरी मंदिर, आणि जगदलपूरचे आठवडी आदिवासी बाजार व दसरा. सिरपूरची विटांची मंदिरे व बौद्ध विहार, कबीरधाममधील भोरमदेव मंदिर, नद्यांच्या संगमावरील राजिमची मंदिरे, रतनपूर आणि डोंगरगडचे डोंगरावरील बम्लेश्वरी मंदिर ही ऐतिहासिक व तीर्थस्थळे आहेत. थंड पठार व तिबेटी वस्ती असलेले मैनपाट हे उत्तरेकडील थंड हवेचे ठिकाण आहे, आणि बारनवापारा व अचानकमार ही वन्यजीव स्थळे आहेत."),
        conf="Editorial"),
    lst("places", [
        it3("chitrakote", "Chitrakote falls", "चित्रकोट जलप्रपात", "चित्रकोट धबधबा", m=("Indravati; Bastar", "इंद्रावती; बस्तर", "इंद्रावती; बस्तर")),
        it3("kanger", "Kanger Valley", "कांगेर घाटी", "कांगेर खोरे", m=("Kotumsar caves; Tirathgarh", "कोटमसर गुफाएँ; तीरथगढ़", "कोटमसर गुहा; तीरथगड")),
        it3("sirpur", "Sirpur", "सिरपुर", "सिरपूर", m=("Temples and monasteries", "मंदिर और विहार", "मंदिरे व विहार")),
        it3("bhoramdeo", "Bhoramdeo", "भोरमदेव", "भोरमदेव", m=("Temple; Kabirdham", "मंदिर; कबीरधाम", "मंदिर; कबीरधाम")),
        it3("mainpat", "Mainpat", "मैनपाट", "मैनपाट", m=("Hill plateau; Tibetan settlement", "पहाड़ी पठार; तिब्बती बस्ती", "डोंगरी पठार; तिबेटी वस्ती")),
        it3("dantewada", "Dantewada", "दंतेवाड़ा", "दंतेवाडा", m=("Danteshwari temple", "दंतेश्वरी मंदिर", "दंतेश्वरी मंदिर")),
        it3("barnawapara", "Barnawapara", "बारनवापारा", "बारनवापारा", m=("Wildlife", "वन्यजीव", "वन्यजीव")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Raipur, Sirpur and Rajim.", "रायपुर, सिरपुर और राजिम।", "रायपूर, सिरपूर व राजिम.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Jagdalpur, Chitrakote, Tirathgarh and Kanger Valley.", "जगदलपुर, चित्रकोट, तीरथगढ़ और कांगेर घाटी।", "जगदलपूर, चित्रकोट, तीरथगड व कांगेर खोरे.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Raipur and Sirpur, then Bastar with Dantewada and a weekly haat.", "रायपुर और सिरपुर, फिर दंतेवाड़ा और साप्ताहिक हाट के साथ बस्तर।", "रायपूर व सिरपूर, नंतर दंतेवाडा व आठवडी बाजारासह बस्तर.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("cgt", "Chhattisgarh Tourism (official)", "छत्तीसगढ़ पर्यटन (आधिकारिक)", "छत्तीसगड पर्यटन (अधिकृत)", url="https://chhattisgarhtourism.co.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Balod", "बालोद", "बालोद"), ("Baloda Bazar", "बलौदाबाज़ार", "बलौदाबाजार"), ("Balrampur", "बलरामपुर", "बलरामपूर"), ("Bastar", "बस्तर", "बस्तर"), ("Bemetara", "बेमेतरा", "बेमेतरा"),
    ("Bijapur", "बीजापुर", "बिजापूर"), ("Bilaspur", "बिलासपुर", "बिलासपूर"), ("Dantewada", "दंतेवाड़ा", "दंतेवाडा"), ("Dhamtari", "धमतरी", "धमतरी"), ("Durg", "दुर्ग", "दुर्ग"),
    ("Gariaband", "गरियाबंद", "गरियाबंद"), ("Gaurela-Pendra-Marwahi", "गौरेला-पेंड्रा-मरवाही", "गौरेला-पेंड्रा-मरवाही"), ("Janjgir-Champa", "जांजगीर-चांपा", "जांजगीर-चांपा"), ("Jashpur", "जशपुर", "जशपूर"), ("Kabirdham", "कबीरधाम", "कबीरधाम"),
    ("Kanker", "कांकेर", "कांकेर"), ("Khairagarh-Chhuikhadan-Gandai", "खैरागढ़-छुईखदान-गंडई", "खैरागड-छुईखदान-गंडई"), ("Kondagaon", "कोंडागाँव", "कोंडागाव"), ("Korba", "कोरबा", "कोरबा"), ("Koriya", "कोरिया", "कोरिया"),
    ("Mahasamund", "महासमुंद", "महासमुंद"), ("Manendragarh-Chirmiri-Bharatpur", "मनेंद्रगढ़-चिरमिरी-भरतपुर", "मनेंद्रगड-चिरमिरी-भरतपूर"), ("Mohla-Manpur-Ambagarh Chowki", "मोहला-मानपुर-अंबागढ़ चौकी", "मोहला-मानपूर-अंबागड चौकी"), ("Mungeli", "मुंगेली", "मुंगेली"), ("Narayanpur", "नारायणपुर", "नारायणपूर"),
    ("Raigarh", "रायगढ़", "रायगड"), ("Raipur", "रायपुर", "रायपूर"), ("Rajnandgaon", "राजनांदगाँव", "राजनांदगाव"), ("Sakti", "सक्ती", "सक्ती"), ("Sarangarh-Bilaigarh", "सारंगढ़-बिलाईगढ़", "सारंगड-बिलाईगड"),
    ("Sukma", "सुकमा", "सुकमा"), ("Surajpur", "सूरजपुर", "सूरजपूर"), ("Surguja", "सरगुजा", "सरगुजा"),
]
assert len(DISTRICTS) == 33, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("raipur", ("Raipur", "रायपुर", "रायपूर"), ("State capital and commercial centre; Nava Raipur Atal Nagar nearby.", "राज्य की राजधानी और वाणिज्यिक केंद्र; पास में नवा रायपुर अटल नगर।", "राज्याची राजधानी व व्यापारी केंद्र; जवळच नवा रायपूर अटल नगर."), ("Capital", "राजधानी", "राजधानी")),
        city("bhilai", ("Bhilai–Durg", "भिलाई–दुर्ग", "भिलाई–दुर्ग"), ("Steel city around the Bhilai Steel Plant; IIT Bhilai.", "भिलाई इस्पात संयंत्र के इर्द-गिर्द इस्पात नगर; आईआईटी भिलाई।", "भिलाई पोलाद कारखान्याभोवतीचे पोलादनगर; आयआयटी भिलाई."), ("Industry", "उद्योग", "उद्योग")),
        city("bilaspur", ("Bilaspur", "बिलासपुर", "बिलासपूर"), ("High Court, railway zone and coal company headquarters.", "उच्च न्यायालय, रेलवे ज़ोन और कोयला कंपनी का मुख्यालय।", "उच्च न्यायालय, रेल्वे विभाग व कोळसा कंपनीचे मुख्यालय."), ("Judicial", "न्यायिक", "न्यायिक")),
        city("korba", ("Korba", "कोरबा", "कोरबा"), ("Power capital with coal mines and thermal stations.", "कोयला खदानों और तापीय केंद्रों वाली ऊर्जा राजधानी।", "कोळसा खाणी व औष्णिक केंद्रांची ऊर्जा राजधानी."), ("Power", "ऊर्जा", "ऊर्जा")),
        city("jagdalpur", ("Jagdalpur", "जगदलपुर", "जगदलपूर"), ("Centre of Bastar; Dussehra and tribal crafts.", "बस्तर का केंद्र; दशहरा और जनजातीय शिल्प।", "बस्तरचे केंद्र; दसरा व आदिवासी हस्तकला."), ("Bastar", "बस्तर", "बस्तर")),
        city("raigarh", ("Raigarh", "रायगढ़", "रायगड"), ("Industrial town of steel and power; Kathak tradition of the Raigarh court.", "इस्पात और बिजली का औद्योगिक नगर; रायगढ़ दरबार की कथक परंपरा।", "पोलाद व विजेचे औद्योगिक शहर; रायगड दरबारची कथक परंपरा."), ("Industry", "उद्योग", "उद्योग")),
        city("ambikapur", ("Ambikapur", "अंबिकापुर", "अंबिकापूर"), ("Centre of Surguja; gateway to Mainpat.", "सरगुजा का केंद्र; मैनपाट का प्रवेश द्वार।", "सरगुजाचे केंद्र; मैनपाटचे प्रवेशद्वार."), ("North", "उत्तर", "उत्तर")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 33 districts (alphabetical)", "33 ज़िले (वर्णानुक्रम)", "33 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Official district list (State notification)", "आधिकारिक ज़िला सूची (राज्य अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य अधिसूचना)"), "india-gov", "Link the State's list of districts; several were created in 2020–22."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Rajnandgaon has a long hockey tradition and hosts an annual all-India tournament, and the State has invested in hockey turf and academies. The Shaheed Veer Narayan Singh International Cricket Stadium at Nava Raipur, one of India's largest, has hosted international matches. Traditional games such as gedi (stilt-walking) at Hareli, kabaddi and archery in tribal areas remain popular, and mallakhamb trainees from the Abujhmarh region have gained national attention.",
        "राजनांदगाँव की हॉकी परंपरा पुरानी है और वहाँ हर वर्ष अखिल भारतीय टूर्नामेंट होता है, और राज्य ने हॉकी टर्फ़ और अकादमियों में निवेश किया है। नवा रायपुर का शहीद वीर नारायण सिंह अंतरराष्ट्रीय क्रिकेट स्टेडियम, भारत के सबसे बड़े स्टेडियमों में से एक, अंतरराष्ट्रीय मैचों की मेज़बानी कर चुका है। हरेली पर गेड़ी, कबड्डी और जनजातीय क्षेत्रों में तीरंदाज़ी जैसे पारंपरिक खेल लोकप्रिय हैं, और अबूझमाड़ क्षेत्र के मलखंब प्रशिक्षुओं ने राष्ट्रीय ध्यान खींचा है।",
        "राजनांदगावची हॉकी परंपरा जुनी आहे व तिथे दरवर्षी अखिल भारतीय स्पर्धा होते, आणि राज्याने हॉकी टर्फ व अकादमींमध्ये गुंतवणूक केली आहे. नवा रायपूरचे शहीद वीर नारायण सिंह आंतरराष्ट्रीय क्रिकेट स्टेडियम, भारतातील सर्वांत मोठ्या स्टेडियमपैकी एक, आंतरराष्ट्रीय सामने आयोजित करून चुकले आहे. हरेलीला गेडी, कबड्डी व आदिवासी भागांत तिरंदाजी यांसारखे पारंपरिक खेळ लोकप्रिय आहेत, आणि अबुझमाड भागातील मल्लखांब प्रशिक्षणार्थींनी राष्ट्रीय लक्ष वेधले आहे."),
        conf="Editorial"),
    lst("venues", [
        it3("svns", "Shaheed Veer Narayan Singh International Cricket Stadium, Nava Raipur", "शहीद वीर नारायण सिंह अंतरराष्ट्रीय क्रिकेट स्टेडियम, नवा रायपुर", "शहीद वीर नारायण सिंह आंतरराष्ट्रीय क्रिकेट स्टेडियम, नवा रायपूर"),
        it3("rjn", "Hockey stadium, Rajnandgaon", "हॉकी स्टेडियम, राजनांदगाँव", "हॉकी स्टेडियम, राजनांदगाव"),
        it3("indoor", "Swami Vivekananda indoor stadium, Raipur", "स्वामी विवेकानंद इनडोर स्टेडियम, रायपुर", "स्वामी विवेकानंद इनडोअर स्टेडियम, रायपूर"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("National and international medallists from Chhattisgarh (official list)", "छत्तीसगढ़ के राष्ट्रीय और अंतरराष्ट्रीय पदक विजेता (आधिकारिक सूची)", "छत्तीसगडचे राष्ट्रीय व आंतरराष्ट्रीय पदकविजेते (अधिकृत यादी)"), "india-gov", "Chhattisgarh Sports and Youth Welfare Department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("ghasidas", ("Guru Ghasidas", "गुरु घासीदास", "गुरु घासीदास"), ("Founder of the Satnami movement, which preached equality and rejected caste discrimination.", "सतनामी आंदोलन के संस्थापक, जिन्होंने समानता का संदेश दिया और जातिगत भेदभाव को नकारा।", "सतनामी चळवळीचे संस्थापक, ज्यांनी समतेचा संदेश दिला व जातिभेद नाकारला."), ("Social reform", "समाज सुधार", "समाजसुधारणा")),
        person("narayan", ("Veer Narayan Singh", "वीर नारायण सिंह", "वीर नारायणसिंह"), ("Zamindar of Sonakhan who distributed grain during a famine and was executed in 1857; the State's first martyr.", "सोनाखान के ज़मींदार, जिन्होंने अकाल में अनाज बाँटा और 1857 में फाँसी पाई; राज्य के पहले शहीद।", "सोनाखानचे जमीनदार, ज्यांनी दुष्काळात धान्य वाटले व 1857 मध्ये फाशी गेले; राज्याचे पहिले हुतात्मा."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("gundadhur", ("Gunda Dhur", "गुंडाधुर", "गुंडाधुर"), ("Leader of the Bhumkal rebellion in Bastar in 1910.", "1910 में बस्तर के भूमकाल विद्रोह के नेता।", "1910 मध्ये बस्तरमधील भूमकाल उठावाचे नेते."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("sundarlal", ("Pandit Sundarlal Sharma", "पंडित सुंदरलाल शर्मा", "पंडित सुंदरलाल शर्मा"), ("Social reformer and freedom fighter who worked against untouchability.", "समाज सुधारक और स्वतंत्रता सेनानी, जिन्होंने छुआछूत के विरुद्ध काम किया।", "समाजसुधारक व स्वातंत्र्यसैनिक, ज्यांनी अस्पृश्यतेविरुद्ध काम केले."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("minimata", ("Minimata", "मिनीमाता", "मिनीमाता"), ("The region's first woman member of Parliament; the Hasdeo Bango dam is named after her.", "क्षेत्र की पहली महिला सांसद; हसदेव बांगो बाँध उनके नाम पर है।", "प्रदेशाच्या पहिल्या महिला खासदार; हसदेव बांगो धरण त्यांच्या नावाने आहे."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("teejan", ("Teejan Bai", "तीजन बाई", "तीजनबाई"), ("Pandavani singer from near Bhilai who took the art to the world; Padma Vibhushan.", "भिलाई के पास की पंडवानी गायिका, जिन्होंने इस कला को विश्व तक पहुँचाया; पद्म विभूषण।", "भिलाईजवळच्या पंडवानी गायिका, ज्यांनी ही कला जगभर पोहोचवली; पद्मविभूषण."), ("Music", "संगीत", "संगीत")),
        person("habib", ("Habib Tanvir", "हबीब तनवीर", "हबीब तनवीर"), ("Playwright and director born in Raipur, whose Naya Theatre worked with Chhattisgarhi folk actors.", "रायपुर में जन्मे नाटककार और निर्देशक, जिनके नया थिएटर ने छत्तीसगढ़ी लोक कलाकारों के साथ काम किया।", "रायपूरमध्ये जन्मलेले नाटककार व दिग्दर्शक, ज्यांच्या नया थिएटरने छत्तीसगढी लोककलाकारांसोबत काम केले."), ("Theatre", "रंगमंच", "रंगभूमी")),
        person("muktibodh", ("Gajanan Madhav Muktibodh", "गजानन माधव मुक्तिबोध", "गजानन माधव मुक्तिबोध"), ("Modern Hindi poet who taught at Rajnandgaon.", "आधुनिक हिंदी कवि, जिन्होंने राजनांदगाँव में अध्यापन किया।", "आधुनिक हिंदी कवी, ज्यांनी राजनांदगाव येथे अध्यापन केले."), ("Literature", "साहित्य", "साहित्य")),
        person("vinod", ("Vinod Kumar Shukla", "विनोद कुमार शुक्ल", "विनोद कुमार शुक्ल"), ("Hindi novelist and poet from Rajnandgaon; Jnanpith Award.", "राजनांदगाँव के हिंदी उपन्यासकार और कवि; ज्ञानपीठ पुरस्कार।", "राजनांदगावचे हिंदी कादंबरीकार व कवी; ज्ञानपीठ पुरस्कार."), ("Literature", "साहित्य", "साहित्य")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Seasonal migration is a long tradition in Chhattisgarh: workers from the plains travel each year to brick kilns, construction sites and farms in Uttar Pradesh, Jammu and Kashmir, Punjab, Telangana and other States after the harvest. In the colonial period, many people from the region were recruited to the tea gardens of Assam. Chhattisgarhi communities in other States keep festivals such as Hareli and Teeja, and the State government runs schemes to register and support migrant workers.",
        "मौसमी प्रवास छत्तीसगढ़ की पुरानी परंपरा है: फ़सल के बाद मैदानों के श्रमिक हर वर्ष उत्तर प्रदेश, जम्मू-कश्मीर, पंजाब, तेलंगाना और अन्य राज्यों के ईंट भट्ठों, निर्माण स्थलों और खेतों में जाते हैं। औपनिवेशिक काल में इस क्षेत्र के बहुत से लोगों को असम के चाय बाग़ानों में भर्ती किया गया। दूसरे राज्यों में छत्तीसगढ़ी समुदाय हरेली और तीजा जैसे त्योहार मनाते हैं, और राज्य सरकार प्रवासी श्रमिकों के पंजीकरण और सहायता के लिए योजनाएँ चलाती है।",
        "हंगामी स्थलांतर ही छत्तीसगडची जुनी परंपरा आहे: सुगीनंतर मैदानांतील कामगार दरवर्षी उत्तर प्रदेश, जम्मू-काश्मीर, पंजाब, तेलंगणा व इतर राज्यांतील वीटभट्ट्या, बांधकामस्थळे व शेतांत जातात. वसाहतकाळात या प्रदेशातील अनेक लोकांना आसामच्या चहाच्या मळ्यांत भरती करण्यात आले. इतर राज्यांतील छत्तीसगढी समुदाय हरेली व तीजासारखे सण साजरे करतात, आणि राज्य सरकार स्थलांतरित कामगारांच्या नोंदणी व मदतीसाठी योजना राबवते."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of seasonal and internal migrants", "मौसमी और आंतरिक प्रवासियों की संख्या", "हंगामी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; State labour department."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Chhattisgarh portal", "छत्तीसगढ़ सरकार पोर्टल", "छत्तीसगड शासन संकेतस्थळ", url="https://cgstate.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Chhattisgarh Tourism", "छत्तीसगढ़ पर्यटन", "छत्तीसगड पर्यटन", url="https://chhattisgarhtourism.co.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Raipur", "रायपुर", "रायपूर"), "0771"], [L("Bhilai–Durg", "भिलाई–दुर्ग", "भिलाई–दुर्ग"), "0788"], [L("Bilaspur", "बिलासपुर", "बिलासपूर"), "07752"],
           [L("Korba", "कोरबा", "कोरबा"), "07759"], [L("Jagdalpur", "जगदलपुर", "जगदलपूर"), "07782"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("State e-services portal — verified link", "राज्य ई-सेवा पोर्टल — सत्यापित लिंक", "राज्य ई-सेवा संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "e-District Chhattisgarh."),
        (L("Official tourism site — verify domain", "आधिकारिक पर्यटन साइट — डोमेन सत्यापन", "अधिकृत पर्यटन संकेतस्थळ — डोमेन पडताळणी"), "india-gov", "Chhattisgarh Tourism Board."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("seven", ("Chhattisgarh shares borders with seven States.", "छत्तीसगढ़ की सीमाएँ सात राज्यों से लगती हैं।", "छत्तीसगडच्या सीमा सात राज्यांना लागतात.")),
        triv("dussehra", ("Bastar Dussehra lasts about 75 days and is devoted to the goddess Danteshwari.", "बस्तर दशहरा लगभग 75 दिन चलता है और देवी दंतेश्वरी को समर्पित है।", "बस्तर दसरा सुमारे 75 दिवस चालतो व देवी दंतेश्वरीला समर्पित आहे.")),
        triv("sexratio", ("Chhattisgarh's sex ratio of 991 in 2011 was among the highest of any State.", "2011 में छत्तीसगढ़ का 991 का लिंगानुपात राज्यों में सबसे ऊँचे में था।", "2011 मधील छत्तीसगडचे 991 लिंग गुणोत्तर राज्यांतील सर्वाधिकांपैकी होते."), "https://statistics.py.gov.in/state-wise-population", "py-des"),
        triv("gi2007", ("Three Bastar crafts — iron, Dhokra and wood — were filed for GI on the same day in 2007.", "बस्तर के तीन शिल्प — लोहा, ढोकरा और लकड़ी — 2007 में एक ही दिन जीआई के लिए दायर हुए।", "बस्तरच्या तीन हस्तकला — लोखंड, ढोकरा व लाकूड — 2007 मध्ये एकाच दिवशी जीआयसाठी दाखल झाल्या."), GI_PDF, "gi-registry"),
        triv("mitanin", ("The State's mitanin community health workers inspired India's national ASHA programme.", "राज्य की मितानिन सामुदायिक स्वास्थ्य कार्यकर्ताओं ने भारत के राष्ट्रीय आशा कार्यक्रम को प्रेरित किया।", "राज्याच्या मितानिन सामुदायिक आरोग्य कार्यकर्त्यांनी भारताच्या राष्ट्रीय आशा कार्यक्रमाला प्रेरणा दिली.")),
        triv("ls", ("The State elects 11 members to the Lok Sabha.", "राज्य से लोकसभा के 11 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 11 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("ct mod3 ok")
