"""Madhya Pradesh modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-MP"
mp = read("regions/IN-MP.json")["metrics"]; ind = read("india.json")["metrics"]

RAMSAR_MP = [
    ("Bhoj Wetland, Bhopal", "भोज आर्द्रभूमि, भोपाल", "भोज पाणथळ, भोपाळ", "2002", "3,201"),
    ("Sirpur Wetland, Indore", "सिरपुर आर्द्रभूमि, इंदौर", "सिरपूर पाणथळ, इंदूर", "2022", "161"),
    ("Sakhya Sagar, Shivpuri", "सख्य सागर, शिवपुरी", "सख्य सागर, शिवपुरी", "2022", "248"),
    ("Yashwant Sagar, Indore", "यशवंत सागर, इंदौर", "यशवंत सागर, इंदूर", "2022", "823"),
    ("Tawa Reservoir", "तवा जलाशय", "तवा जलाशय", "2024", "20,050"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "A quarter of Madhya Pradesh — 77,073 km² — is forest (ISFR 2023), the largest forest area of any Indian State: teak in the west and centre, sal in the east, and dry mixed forest in the north. The State's tiger reserves — Kanha, Bandhavgarh, Pench, Panna, Satpura, Sanjay–Dubri, Veerangana Durgavati and the newer Ratapani and Madhav — hold the largest wild tiger population in India. Kanha saved the hard-ground barasingha, the State animal, from extinction; Kuno National Park became home to cheetahs brought from Africa from 2022; and the National Chambal Sanctuary, shared with Rajasthan and Uttar Pradesh, protects gharials and river dolphins. Pachmarhi is a UNESCO biosphere reserve.\n\nThe State has five Ramsar sites: the Bhoj Wetland of Bhopal's lakes, Sirpur and Yashwant Sagar near Indore, Sakhya Sagar at Shivpuri and the Tawa reservoir.",
        "मध्य प्रदेश का एक-चौथाई भाग — 77,073 वर्ग किमी — वन है (आईएसएफ़आर 2023), जो किसी भी भारतीय राज्य का सबसे बड़ा वन क्षेत्र है: पश्चिम और मध्य में सागौन, पूर्व में साल, और उत्तर में शुष्क मिश्रित वन। राज्य के बाघ अभयारण्य — कान्हा, बांधवगढ़, पेंच, पन्ना, सतपुड़ा, संजय–दुबरी, वीरांगना दुर्गावती और नए रातापानी व माधव — भारत में जंगली बाघों की सबसे बड़ी आबादी रखते हैं। कान्हा ने राज्य पशु, कठोर भूमि के बारहसिंगा को विलुप्ति से बचाया; कूनो राष्ट्रीय उद्यान 2022 से अफ़्रीका से लाए गए चीतों का घर बना; और राजस्थान व उत्तर प्रदेश के साथ साझा राष्ट्रीय चंबल अभयारण्य घड़ियालों और नदी डॉल्फ़िनों की रक्षा करता है। पचमढ़ी यूनेस्को जैवमंडल आरक्षित क्षेत्र है।\n\nराज्य में पाँच रामसर स्थल हैं: भोपाल की झीलों वाली भोज आर्द्रभूमि, इंदौर के पास सिरपुर और यशवंत सागर, शिवपुरी का सख्य सागर और तवा जलाशय।",
        "मध्य प्रदेशचा एक-चतुर्थांश भाग — 77,073 चौ.किमी — वनाच्छादित आहे (आयएसएफआर 2023), कोणत्याही भारतीय राज्यातील सर्वांत मोठे वनक्षेत्र: पश्चिम व मध्य भागात सागवान, पूर्वेला साल, आणि उत्तरेत कोरडे मिश्र जंगल. राज्याचे व्याघ्र प्रकल्प — कान्हा, बांधवगड, पेंच, पन्ना, सातपुडा, संजय–दुबरी, वीरांगना दुर्गावती आणि नवे रातापानी व माधव — भारतातील सर्वांत मोठी जंगली वाघसंख्या राखतात. कान्हाने राज्यप्राणी, कठीण जमिनीवरील बाराशिंग्याला विलुप्त होण्यापासून वाचवले; कुनो राष्ट्रीय उद्यान 2022 पासून आफ्रिकेतून आणलेल्या चित्त्यांचे घर झाले; आणि राजस्थान व उत्तर प्रदेशसोबत सामायिक राष्ट्रीय चंबळ अभयारण्य घडियाल व नदी डॉल्फिनचे रक्षण करते. पचमढी हे युनेस्को जीवावरण राखीव क्षेत्र आहे.\n\nराज्यात पाच रामसर स्थळे आहेत: भोपाळच्या सरोवरांचे भोज पाणथळ, इंदूरजवळील सिरपूर व यशवंत सागर, शिवपुरीचा सख्य सागर आणि तवा जलाशय."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(77073.44, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(77444.98, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), mp["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(5, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_MP], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026 (year of designation).", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची (घोषणा वर्ष)।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी (घोषणा वर्ष).")),
    lst("protected", [
        it3("kanha", "Kanha Tiger Reserve", "कान्हा बाघ अभयारण्य", "कान्हा व्याघ्र प्रकल्प", m=("Barasingha", "बारहसिंगा", "बाराशिंगा")),
        it3("bandhavgarh", "Bandhavgarh Tiger Reserve", "बांधवगढ़ बाघ अभयारण्य", "बांधवगड व्याघ्र प्रकल्प", m=("Umaria", "उमरिया", "उमरिया")),
        it3("pench", "Pench Tiger Reserve", "पेंच बाघ अभयारण्य", "पेंच व्याघ्र प्रकल्प", m=("Seoni", "सिवनी", "सिवनी")),
        it3("panna", "Panna Tiger Reserve", "पन्ना बाघ अभयारण्य", "पन्ना व्याघ्र प्रकल्प", m=("Ken river", "केन नदी", "केन नदी")),
        it3("satpura", "Satpura Tiger Reserve", "सतपुड़ा बाघ अभयारण्य", "सातपुडा व्याघ्र प्रकल्प", m=("Pachmarhi", "पचमढ़ी", "पचमढी")),
        it3("kuno", "Kuno National Park", "कूनो राष्ट्रीय उद्यान", "कुनो राष्ट्रीय उद्यान", m=("Cheetahs", "चीते", "चित्ते")),
        it3("chambal", "National Chambal Sanctuary", "राष्ट्रीय चंबल अभयारण्य", "राष्ट्रीय चंबळ अभयारण्य", m=("Gharial", "घड़ियाल", "घडियाल")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("barasingha", "Barasingha (State animal)", "बारहसिंगा (राज्य पशु)", "बाराशिंगा (राज्यप्राणी)"), it3("tiger", "Tiger", "बाघ", "वाघ"),
        it3("cheetah", "Cheetah", "चीता", "चित्ता"), it3("gharial", "Gharial", "घड़ियाल", "घडियाल"),
        it3("vulture", "Vultures", "गिद्ध", "गिधाडे"), it3("dudhraj", "Indian paradise flycatcher (State bird)", "दूधराज (राज्य पक्षी)", "स्वर्गीय नर्तक (राज्यपक्षी)"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger estimate (All India Tiger Estimation)", "बाघों का अनुमान (अखिल भारतीय बाघ आकलन)", "वाघांचा अंदाज (अखिल भारतीय व्याघ्र गणना)"), "ntca", "NTCA All India Tiger Estimation, State figure."),
        (L("Cheetah population at Kuno and Gandhi Sagar", "कूनो और गांधी सागर में चीतों की संख्या", "कुनो व गांधी सागर येथील चित्त्यांची संख्या"), "ntca", "Project Cheetah official updates."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "The Narmada is the lifeline of central Madhya Pradesh. The Narmada Valley Development Authority has built dams at Bargi, Indira Sagar, Omkareshwar and elsewhere, and the Narmada–Kshipra and Narmada–Gambhir links lift Narmada water to the Malwa plateau around Ujjain and Indore. The Chambal's Gandhi Sagar dam is shared with Rajasthan, and the Betwa, Ken and Son are dammed for irrigation. Groundwater-fed wheat farming has grown fast, and parts of Malwa and Bundelkhand face falling water tables; Bundelkhand in particular suffers repeated drought, which the Ken–Betwa link is meant to ease. Bhopal draws its water from the Upper Lake, built under Raja Bhoj in the 11th century.",
        "नर्मदा मध्य मध्य प्रदेश की जीवनरेखा है। नर्मदा घाटी विकास प्राधिकरण ने बरगी, इंदिरा सागर, ओंकारेश्वर और अन्य स्थानों पर बाँध बनाए हैं, और नर्मदा–क्षिप्रा और नर्मदा–गंभीर लिंक नर्मदा का पानी उठाकर उज्जैन और इंदौर के आसपास मालवा पठार तक पहुँचाते हैं। चंबल का गांधी सागर बाँध राजस्थान के साथ साझा है, और बेतवा, केन और सोन पर सिंचाई के लिए बाँध हैं। भूजल पर आधारित गेहूँ की खेती तेज़ी से बढ़ी है, और मालवा व बुंदेलखंड के कुछ भागों में जल स्तर गिर रहा है; विशेषकर बुंदेलखंड बार-बार सूखे से पीड़ित है, जिसे केन–बेतवा लिंक से राहत मिलने की उम्मीद है। भोपाल अपना पानी ऊपरी झील से लेता है, जो 11वीं सदी में राजा भोज के समय बनी।",
        "नर्मदा ही मध्य प्रदेशाच्या मध्य भागाची जीवनरेखा आहे. नर्मदा खोरे विकास प्राधिकरणाने बरगी, इंदिरा सागर, ओंकारेश्वर व इतरत्र धरणे बांधली आहेत, आणि नर्मदा–क्षिप्रा व नर्मदा–गंभीर जोड प्रकल्प नर्मदेचे पाणी उचलून उज्जैन व इंदूरभोवतीच्या माळवा पठारापर्यंत नेतात. चंबळवरील गांधी सागर धरण राजस्थानसोबत सामायिक आहे, आणि बेतवा, केन व सोनवर सिंचनासाठी धरणे आहेत. भूजलावर आधारित गहू शेती झपाट्याने वाढली आहे, आणि माळवा व बुंदेलखंडच्या काही भागांत भूजलपातळी घसरत आहे; विशेषतः बुंदेलखंड वारंवार दुष्काळ सोसतो, जो केन–बेतवा जोडामुळे कमी होईल अशी अपेक्षा आहे. भोपाळ आपले पाणी वरच्या सरोवरातून घेते, जे अकराव्या शतकात राजा भोजाच्या काळात बांधले गेले."),
        conf="Editorial"),
    gaps("g", [
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
        (L("Net irrigated area", "शुद्ध सिंचित क्षेत्र", "निव्वळ सिंचित क्षेत्र"), "india-gov", "Land-use statistics, Ministry of Agriculture."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Floods along the Narmada, Chambal and their tributaries occur in heavy monsoons, and lightning causes many deaths during the rains. Bundelkhand and parts of Malwa face recurring drought, and summer heatwaves are severe in the north. The Bhopal gas tragedy of 1984 remains a reminder of industrial risk, and the cleanup of the Union Carbide site continued for decades.\n\nVisitors to tiger reserves should book safaris only through official portals and follow park rules; pilgrims at large gatherings such as the Simhastha in Ujjain should follow crowd-management advisories.",
        "भारी मानसून में नर्मदा, चंबल और उनकी सहायक नदियों में बाढ़ आती है, और वर्षा में आकाशीय बिजली से बहुत मौतें होती हैं। बुंदेलखंड और मालवा के कुछ भाग बार-बार सूखे का सामना करते हैं, और उत्तर में गर्मियों की लू तीव्र होती है। 1984 की भोपाल गैस त्रासदी औद्योगिक जोखिम की याद दिलाती है, और यूनियन कार्बाइड स्थल की सफ़ाई दशकों तक चली।\n\nबाघ अभयारण्यों में जाने वाले पर्यटकों को केवल आधिकारिक पोर्टल से सफ़ारी बुक करनी चाहिए और उद्यान के नियमों का पालन करना चाहिए; उज्जैन के सिंहस्थ जैसे बड़े समागमों में तीर्थयात्रियों को भीड़ प्रबंधन सलाह माननी चाहिए।",
        "मुसळधार पावसाळ्यात नर्मदा, चंबळ व त्यांच्या उपनद्यांना पूर येतात, आणि पावसाळ्यात वीज कोसळून अनेक मृत्यू होतात. बुंदेलखंड व माळव्याचे काही भाग वारंवार दुष्काळाला तोंड देतात, आणि उत्तरेत उन्हाळ्यातील उष्णतेच्या लाटा तीव्र असतात. 1984 ची भोपाळ वायू दुर्घटना औद्योगिक धोक्याची आठवण आहे, आणि युनियन कार्बाइड स्थळाची स्वच्छता दशकानुदशके चालली.\n\nव्याघ्र प्रकल्पांत जाणाऱ्या पर्यटकांनी फक्त अधिकृत संकेतस्थळांवरून सफारी आरक्षित करावी व उद्यानाचे नियम पाळावेत; उज्जैनच्या सिंहस्थासारख्या मोठ्या मेळाव्यांत यात्रेकरूंनी गर्दी व्यवस्थापन सूचना पाळाव्यात."),
        conf="Editorial"),
    emergency_table(("Madhya Pradesh", "मध्य प्रदेश", "मध्य प्रदेश")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official MPSDMA address."),
        (L("Lightning deaths by year", "वर्षवार आकाशीय बिजली से मौतें", "वर्षनिहाय वीज कोसळून मृत्यू"), "india-gov", "NCRB Accidental Deaths and Suicides in India."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Madhya Pradesh has 27 registered Geographical Indications of its own in the GI Registry's list as on 31 December 2025, and shares three more: Nagpur oranges with Maharashtra, and Mahoba Desawari pan and Bundelkhand Kathiya wheat with Uttar Pradesh. Chanderi saris, filed in 2004, were among the earliest. Crafts form the largest group — Maheshwar saris, Bagh prints, Gond painting, leather toys of Indore, bell-metal ware of Datia and Tikamgarh, Ujjain batik, Gwalior carpets, papier-mâché and stone craft, Jabalpur and Khajuraho stone craft, Dindori wrought iron, Betul Bharewa metal craft and Chhatarpur furniture. Food GIs include Ratlami sev, Morena gajak and Jhabua Kadaknath chicken; agricultural GIs include Sharbati wheat, Balaghat Chinnor rice, Rewa Sunderja mango and Riyawan garlic. Panna diamonds are a manufactured-goods GI.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में मध्य प्रदेश के अपने 27 पंजीकृत भौगोलिक संकेतक हैं, और तीन और साझा हैं: नागपुर संतरा महाराष्ट्र के साथ, और महोबा देशावरी पान व बुंदेलखंड कठिया गेहूँ उत्तर प्रदेश के साथ। 2004 में दायर चंदेरी साड़ियाँ सबसे पहले जीआई में थीं। शिल्प सबसे बड़ा समूह हैं — महेश्वर साड़ियाँ, बाग़ छपाई, गोंड चित्रकला, इंदौर के चमड़े के खिलौने, दतिया और टीकमगढ़ के घंटा-धातु बर्तन, उज्जैन बाटिक, ग्वालियर के कालीन, पेपर माशे और पत्थर शिल्प, जबलपुर और खजुराहो पत्थर शिल्प, डिंडोरी लौह शिल्प, बैतूल भरेवा धातु शिल्प और छतरपुर फ़र्नीचर। खाद्य जीआई में रतलामी सेव, मुरैना गजक और झाबुआ कड़कनाथ मुर्गा हैं; कृषि जीआई में शरबती गेहूँ, बालाघाट चिन्नौर चावल, रीवा सुंदरजा आम और रियावन लहसुन। पन्ना हीरा विनिर्मित वस्तु जीआई है।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत मध्य प्रदेशची स्वतःची 27 नोंदणीकृत भौगोलिक मानांकने आहेत, आणि आणखी तीन सामायिक आहेत: नागपुरी संत्री महाराष्ट्रासोबत, आणि महोबा देशावरी पान व बुंदेलखंड कठिया गहू उत्तर प्रदेशसोबत. 2004 मध्ये दाखल झालेल्या चंदेरी साड्या सर्वांत सुरुवातीच्या जीआयपैकी होत्या. हस्तकला हा सर्वांत मोठा गट आहे — महेश्वरी साड्या, बाग छपाई, गोंड चित्रकला, इंदूरची चामडी खेळणी, दतिया व टीकमगडची घंटाधातू भांडी, उज्जैन बाटिक, ग्वाल्हेरचे गालिचे, पेपर माशे व दगडी हस्तकला, जबलपूर व खजुराहो दगडी हस्तकला, डिंडोरीची लोखंडी हस्तकला, बैतूल भरेवा धातुकला व छतरपूर फर्निचर. खाद्य जीआयमध्ये रतलामी शेव, मुरैना गजक व झाबुआ कडकनाथ कोंबडी; कृषी जीआयमध्ये शरबती गहू, बालाघाट चिन्नोर तांदूळ, रीवा सुंदरजा आंबा व रियावन लसूण. पन्ना हिरा हे उत्पादित वस्तू जीआय आहे."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Madhya Pradesh combines temples, forts and forests. The temples of Khajuraho, the stupas of Sanchi and the painted rock shelters of Bhimbetka are World Heritage Sites. Ujjain's Mahakaleshwar temple and its new Mahakal Lok corridor, Omkareshwar on its island in the Narmada and Maheshwar's ghats draw pilgrims. Gwalior fort, the Afghan-era palaces of Mandu, the Bundela town of Orchha and the weaving town of Chanderi are heritage highlights. Wildlife lovers head to Kanha, Bandhavgarh, Pench and Panna, and Pachmarhi and the marble rocks of Bhedaghat near Jabalpur offer scenery.",
        "मध्य प्रदेश मंदिरों, क़िलों और वनों का संगम है। खजुराहो के मंदिर, साँची के स्तूप और भीमबेटका के चित्रित शैलाश्रय विश्व धरोहर स्थल हैं। उज्जैन का महाकालेश्वर मंदिर और उसका नया महाकाल लोक गलियारा, नर्मदा के द्वीप पर ओंकारेश्वर और महेश्वर के घाट तीर्थयात्रियों को खींचते हैं। ग्वालियर क़िला, मांडू के अफ़ग़ान काल के महल, बुंदेला नगर ओरछा और बुनकरों का नगर चंदेरी धरोहर के मुख्य आकर्षण हैं। वन्यजीव प्रेमी कान्हा, बांधवगढ़, पेंच और पन्ना जाते हैं, और पचमढ़ी व जबलपुर के पास भेड़ाघाट की संगमरमरी चट्टानें प्राकृतिक दृश्य देती हैं।",
        "मध्य प्रदेश हे मंदिरे, किल्ले व जंगलांचा संगम आहे. खजुराहोची मंदिरे, सांचीचे स्तूप व भीमबेटकाची रंगवलेली शैलाश्रये ही जागतिक वारसा स्थळे आहेत. उज्जैनचे महाकालेश्वर मंदिर व नवा महाकाल लोक मार्ग, नर्मदेतील बेटावरील ओंकारेश्वर आणि महेश्वरचे घाट यात्रेकरूंना खेचतात. ग्वाल्हेरचा किल्ला, मांडूचे अफगाणकालीन महाल, बुंदेला नगर ओरछा व विणकरांचे गाव चंदेरी ही वारशाची मुख्य आकर्षणे आहेत. वन्यजीवप्रेमी कान्हा, बांधवगड, पेंच व पन्नाला जातात, आणि पचमढी व जबलपूरजवळील भेडाघाटचे संगमरवरी कडे निसर्गदृश्ये देतात."),
        conf="Editorial"),
    lst("places", [
        it3("khajuraho", "Khajuraho", "खजुराहो", "खजुराहो", m=("UNESCO temples", "यूनेस्को मंदिर", "युनेस्को मंदिरे")),
        it3("sanchi", "Sanchi and Bhimbetka", "साँची और भीमबेटका", "सांची व भीमबेटका", m=("UNESCO sites", "यूनेस्को स्थल", "युनेस्को स्थळे")),
        it3("ujjain", "Ujjain and Omkareshwar", "उज्जैन और ओंकारेश्वर", "उज्जैन व ओंकारेश्वर", m=("Jyotirlingas", "ज्योतिर्लिंग", "ज्योतिर्लिंगे")),
        it3("kanha", "Kanha and Bandhavgarh", "कान्हा और बांधवगढ़", "कान्हा व बांधवगड", m=("Tiger safaris", "बाघ सफ़ारी", "वाघ सफारी")),
        it3("gwalior", "Gwalior and Orchha", "ग्वालियर और ओरछा", "ग्वाल्हेर व ओरछा", m=("Forts, palaces", "क़िले, महल", "किल्ले, राजवाडे")),
        it3("mandu", "Mandu and Maheshwar", "मांडू और महेश्वर", "मांडू व महेश्वर", m=("Heritage, weaving", "धरोहर, बुनाई", "वारसा, विणकाम")),
        it3("pachmarhi", "Pachmarhi", "पचमढ़ी", "पचमढी", m=("Hill station", "पर्वतीय स्थल", "थंड हवेचे ठिकाण")),
        it3("bhedaghat", "Bhedaghat marble rocks", "भेड़ाघाट संगमरमरी चट्टानें", "भेडाघाट संगमरवरी कडे", m=("Narmada gorge", "नर्मदा घाटी", "नर्मदा घळ")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Bhopal, Sanchi and Bhimbetka.", "भोपाल, साँची और भीमबेटका।", "भोपाळ, सांची व भीमबेटका.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Indore, Ujjain, Omkareshwar and Maheshwar.", "इंदौर, उज्जैन, ओंकारेश्वर और महेश्वर।", "इंदूर, उज्जैन, ओंकारेश्वर व महेश्वर.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Khajuraho, Panna and Orchha.", "खजुराहो, पन्ना और ओरछा।", "खजुराहो, पन्ना व ओरछा.")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Jabalpur and Bhedaghat, then Kanha and Bandhavgarh.", "जबलपुर और भेड़ाघाट, फिर कान्हा और बांधवगढ़।", "जबलपूर व भेडाघाट, नंतर कान्हा व बांधवगड.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("mpt", "Madhya Pradesh Tourism (official)", "मध्य प्रदेश पर्यटन (आधिकारिक)", "मध्य प्रदेश पर्यटन (अधिकृत)", url="https://www.mptourism.com", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Agar Malwa", "आगर मालवा", "आगर माळवा"), ("Alirajpur", "अलीराजपुर", "अलीराजपूर"), ("Anuppur", "अनूपपुर", "अनूपपूर"), ("Ashoknagar", "अशोकनगर", "अशोकनगर"),
    ("Balaghat", "बालाघाट", "बालाघाट"), ("Barwani", "बड़वानी", "बडवानी"), ("Betul", "बैतूल", "बैतूल"), ("Bhind", "भिंड", "भिंड"), ("Bhopal", "भोपाल", "भोपाळ"),
    ("Burhanpur", "बुरहानपुर", "बुरहानपूर"), ("Chhatarpur", "छतरपुर", "छतरपूर"), ("Chhindwara", "छिंदवाड़ा", "छिंदवाडा"), ("Damoh", "दमोह", "दमोह"), ("Datia", "दतिया", "दतिया"),
    ("Dewas", "देवास", "देवास"), ("Dhar", "धार", "धार"), ("Dindori", "डिंडोरी", "डिंडोरी"), ("Guna", "गुना", "गुना"), ("Gwalior", "ग्वालियर", "ग्वाल्हेर"),
    ("Harda", "हरदा", "हरदा"), ("Indore", "इंदौर", "इंदूर"), ("Jabalpur", "जबलपुर", "जबलपूर"), ("Jhabua", "झाबुआ", "झाबुआ"), ("Katni", "कटनी", "कटनी"),
    ("Khandwa", "खंडवा", "खंडवा"), ("Khargone", "खरगोन", "खरगोन"), ("Maihar", "मैहर", "मैहर"), ("Mandla", "मंडला", "मंडला"), ("Mandsaur", "मंदसौर", "मंदसौर"),
    ("Mauganj", "मऊगंज", "मऊगंज"), ("Morena", "मुरैना", "मुरैना"), ("Narmadapuram", "नर्मदापुरम", "नर्मदापुरम"), ("Narsinghpur", "नरसिंहपुर", "नरसिंहपूर"),
    ("Neemuch", "नीमच", "नीमच"), ("Niwari", "निवाड़ी", "निवाडी"), ("Pandhurna", "पांढुर्णा", "पांढुर्णा"), ("Panna", "पन्ना", "पन्ना"), ("Raisen", "रायसेन", "रायसेन"),
    ("Rajgarh", "राजगढ़", "राजगड"), ("Ratlam", "रतलाम", "रतलाम"), ("Rewa", "रीवा", "रीवा"), ("Sagar", "सागर", "सागर"), ("Satna", "सतना", "सतना"),
    ("Sehore", "सीहोर", "सिहोर"), ("Seoni", "सिवनी", "सिवनी"), ("Shahdol", "शहडोल", "शहडोल"), ("Shajapur", "शाजापुर", "शाजापूर"), ("Sheopur", "श्योपुर", "श्योपूर"),
    ("Shivpuri", "शिवपुरी", "शिवपुरी"), ("Sidhi", "सीधी", "सीधी"), ("Singrauli", "सिंगरौली", "सिंगरौली"), ("Tikamgarh", "टीकमगढ़", "टीकमगड"),
    ("Ujjain", "उज्जैन", "उज्जैन"), ("Umaria", "उमरिया", "उमरिया"), ("Vidisha", "विदिशा", "विदिशा"),
]
assert len(DISTRICTS) == 55, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("bhopal", ("Bhopal", "भोपाल", "भोपाळ"), ("State capital; city of lakes; BHEL and research institutes.", "राज्य की राजधानी; झीलों का शहर; भेल और शोध संस्थान।", "राज्याची राजधानी; सरोवरांचे शहर; भेल व संशोधन संस्था."), ("Capital", "राजधानी", "राजधानी")),
        city("indore", ("Indore", "इंदौर", "इंदूर"), ("Largest city and commercial capital; repeatedly ranked India's cleanest city.", "सबसे बड़ा शहर और वाणिज्यिक राजधानी; बार-बार भारत का सबसे स्वच्छ शहर।", "सर्वांत मोठे शहर व व्यापारी राजधानी; वारंवार भारतातील सर्वांत स्वच्छ शहर."), ("Commerce", "वाणिज्य", "व्यापार")),
        city("jabalpur", ("Jabalpur", "जबलपुर", "जबलपूर"), ("High Court seat; defence factories; Bhedaghat.", "उच्च न्यायालय का स्थान; रक्षा कारख़ाने; भेड़ाघाट।", "उच्च न्यायालयाचे ठिकाण; संरक्षण कारखाने; भेडाघाट."), ("Mahakoshal", "महाकोशल", "महाकोशल")),
        city("gwalior", ("Gwalior", "ग्वालियर", "ग्वाल्हेर"), ("Hilltop fort, Scindia palaces and music.", "पहाड़ी क़िला, सिंधिया महल और संगीत।", "डोंगरी किल्ला, शिंदे राजवाडे व संगीत."), ("Heritage", "धरोहर", "वारसा")),
        city("ujjain", ("Ujjain", "उज्जैन", "उज्जैन"), ("Ancient city of Mahakal on the Kshipra; Simhastha.", "क्षिप्रा पर महाकाल का प्राचीन नगर; सिंहस्थ।", "क्षिप्रेवरील महाकालाचे प्राचीन नगर; सिंहस्थ."), ("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        city("sagar", ("Sagar", "सागर", "सागर"), ("University town of Bundelkhand.", "बुंदेलखंड का विश्वविद्यालय नगर।", "बुंदेलखंडचे विद्यापीठ नगर."), ("Education", "शिक्षा", "शिक्षण")),
        city("singrauli", ("Singrauli", "सिंगरौली", "सिंगरौली"), ("Coal mines and power stations.", "कोयला खदानें और बिजलीघर।", "कोळसा खाणी व वीज केंद्रे."), ("Energy", "ऊर्जा", "ऊर्जा")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 55 districts (alphabetical)", "55 ज़िले (वर्णानुक्रम)", "55 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Official district list (State notification)", "आधिकारिक ज़िला सूची (राज्य अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य अधिसूचना)"), "india-gov", "Link the State's list of districts."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Bhopal has long been called a nursery of Indian hockey, producing Olympians and the 1975 World Cup winner Aslam Sher Khan, and the State runs residential academies for hockey, shooting, rowing and other sports. Cricket is popular: Indore's Holkar Stadium and Gwalior's Captain Roop Singh Stadium have hosted international matches, and Madhya Pradesh won its first Ranji Trophy in 2022. Water sports and sailing are practised on Bhopal's Upper Lake.",
        "भोपाल को लंबे समय से भारतीय हॉकी की नर्सरी कहा जाता है, जिसने ओलंपियन और 1975 विश्व कप विजेता असलम शेर ख़ान दिए, और राज्य हॉकी, निशानेबाज़ी, नौकायन और अन्य खेलों के आवासीय अकादमियाँ चलाता है। क्रिकेट लोकप्रिय है: इंदौर के होलकर स्टेडियम और ग्वालियर के कैप्टन रूप सिंह स्टेडियम ने अंतरराष्ट्रीय मैचों की मेज़बानी की है, और मध्य प्रदेश ने 2022 में अपनी पहली रणजी ट्रॉफी जीती। भोपाल की ऊपरी झील पर जल क्रीड़ा और नौकायन होता है।",
        "भोपाळला दीर्घकाळापासून भारतीय हॉकीची रोपवाटिका म्हटले जाते, ज्याने ऑलिम्पियन व 1975 विश्वचषक विजेते असलम शेर खान दिले, आणि राज्य हॉकी, नेमबाजी, नौकानयन व इतर खेळांसाठी निवासी अकादमी चालवते. क्रिकेट लोकप्रिय आहे: इंदूरचे होळकर स्टेडियम व ग्वाल्हेरचे कॅप्टन रूपसिंह स्टेडियम येथे आंतरराष्ट्रीय सामने झाले आहेत, आणि मध्य प्रदेशने 2022 मध्ये पहिली रणजी करंडक जिंकली. भोपाळच्या वरच्या सरोवरावर जलक्रीडा व नौकानयन होते."),
        conf="Editorial"),
    lst("venues", [
        it3("holkar", "Holkar Stadium, Indore", "होलकर स्टेडियम, इंदौर", "होळकर स्टेडियम, इंदूर"),
        it3("roopsingh", "Captain Roop Singh Stadium, Gwalior", "कैप्टन रूप सिंह स्टेडियम, ग्वालियर", "कॅप्टन रूपसिंह स्टेडियम, ग्वाल्हेर"),
        it3("tatya", "TT Nagar Stadium, Bhopal", "टीटी नगर स्टेडियम, भोपाल", "टीटी नगर स्टेडियम, भोपाळ"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from Madhya Pradesh (official list)", "मध्य प्रदेश के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "मध्य प्रदेशचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "MP Sports and Youth Welfare Department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("tansen", ("Tansen", "तानसेन", "तानसेन"), ("Legendary singer of Akbar's court, linked with Gwalior.", "अकबर के दरबार के महान गायक, ग्वालियर से जुड़े।", "अकबराच्या दरबारातील महान गायक, ग्वाल्हेरशी संबंधित."), ("Music", "संगीत", "संगीत")),
        person("durgavati", ("Rani Durgavati", "रानी दुर्गावती", "राणी दुर्गावती"), ("Gond queen of Garha-Mandla who fought the Mughals (1564).", "गढ़ा-मंडला की गोंड रानी, जिन्होंने मुग़लों से युद्ध किया (1564)।", "गढा-मंडलाची गोंड राणी, जी मुघलांशी लढली (1564)."), ("History", "इतिहास", "इतिहास")),
        person("ahilya", ("Ahilyabai Holkar", "अहिल्याबाई होलकर", "अहिल्याबाई होळकर"), ("Holkar queen who ruled from Maheshwar and rebuilt temples across India.", "होलकर रानी, जिन्होंने महेश्वर से शासन किया और पूरे भारत में मंदिरों का जीर्णोद्धार किया।", "होळकर राणी, ज्यांनी महेश्वरहून कारभार केला व भारतभर मंदिरांचा जीर्णोद्धार केला."), ("History", "इतिहास", "इतिहास")),
        person("azad", ("Chandra Shekhar Azad", "चंद्रशेखर आज़ाद", "चंद्रशेखर आझाद"), ("Revolutionary born at Bhabhra in Alirajpur district.", "अलीराजपुर ज़िले के भाबरा में जन्मे क्रांतिकारी।", "अलीराजपूर जिल्ह्यातील भाबरा येथे जन्मलेले क्रांतिकारक."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("tantya", ("Tantya Bhil", "टंट्या भील", "तंट्या भिल्ल"), ("Bhil hero who resisted British rule in Nimar in the 1880s.", "भील नायक, जिन्होंने 1880 के दशक में निमाड़ में ब्रिटिश शासन का प्रतिरोध किया।", "भिल्ल नायक, ज्यांनी 1880 च्या दशकात निमाडमध्ये इंग्रजी राजवटीला विरोध केला."), ("Tribal history", "आदिवासी इतिहास", "आदिवासी इतिहास")),
        person("makhanlal", ("Makhanlal Chaturvedi", "माखनलाल चतुर्वेदी", "माखनलाल चतुर्वेदी"), ("Hindi poet and journalist of the freedom movement.", "स्वतंत्रता आंदोलन के हिंदी कवि और पत्रकार।", "स्वातंत्र्य चळवळीतील हिंदी कवी व पत्रकार."), ("Literature", "साहित्य", "साहित्य")),
        person("vajpayee", ("Atal Bihari Vajpayee", "अटल बिहारी वाजपेयी", "अटलबिहारी वाजपेयी"), ("Prime Minister of India, born in Gwalior; Bharat Ratna.", "भारत के प्रधानमंत्री, ग्वालियर में जन्मे; भारत रत्न।", "भारताचे पंतप्रधान, ग्वाल्हेरमध्ये जन्म; भारतरत्न."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("lata", ("Lata Mangeshkar", "लता मंगेशकर", "लता मंगेशकर"), ("Playback singer born in Indore; Bharat Ratna.", "इंदौर में जन्मी पार्श्वगायिका; भारत रत्न।", "इंदूरमध्ये जन्मलेल्या पार्श्वगायिका; भारतरत्न."), ("Music", "संगीत", "संगीत")),
        person("kishore", ("Kishore Kumar", "किशोर कुमार", "किशोर कुमार"), ("Singer and actor from Khandwa.", "खंडवा के गायक और अभिनेता।", "खंडव्याचे गायक व अभिनेते."), ("Cinema, music", "सिनेमा, संगीत", "चित्रपट, संगीत")),
        person("bhuribai", ("Bhuri Bai", "भूरी बाई", "भूरी बाई"), ("Bhil artist from Jhabua; Padma Shri.", "झाबुआ की भील कलाकार; पद्मश्री।", "झाबुआच्या भिल्ल कलाकार; पद्मश्री."), ("Art", "कला", "कला")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Migration from Madhya Pradesh is mostly within India: workers from Bundelkhand, the tribal districts of the west and the Vindhya region go to Delhi, Gujarat, Maharashtra and Punjab for construction and farm work, often seasonally. Professionals from Indore, Bhopal and Jabalpur have moved to India's metros and abroad, especially to the United States. The Sindhi community of Bhopal and Indore, which arrived after Partition, and the Marathi-speaking families of Indore and Gwalior from the Maratha era, are among the State's own migrant communities.",
        "मध्य प्रदेश से प्रवास अधिकतर भारत के भीतर होता है: बुंदेलखंड, पश्चिम के आदिवासी ज़िलों और विंध्य क्षेत्र के श्रमिक निर्माण और खेती के काम के लिए, अक्सर मौसमी रूप से, दिल्ली, गुजरात, महाराष्ट्र और पंजाब जाते हैं। इंदौर, भोपाल और जबलपुर के पेशेवर भारत के महानगरों और विदेश, विशेषकर अमेरिका, गए हैं। विभाजन के बाद आया भोपाल और इंदौर का सिंधी समुदाय, और मराठा काल से इंदौर और ग्वालियर के मराठी-भाषी परिवार राज्य के अपने प्रवासी समुदायों में हैं।",
        "मध्य प्रदेशातून होणारे स्थलांतर बहुतांश देशांतर्गत आहे: बुंदेलखंड, पश्चिमेकडील आदिवासी जिल्हे व विंध्य प्रदेशातील कामगार बांधकाम व शेतीकामासाठी, अनेकदा हंगामी, दिल्ली, गुजरात, महाराष्ट्र व पंजाबमध्ये जातात. इंदूर, भोपाळ व जबलपूरचे व्यावसायिक भारतातील महानगरांत व परदेशात, विशेषतः अमेरिकेत गेले आहेत. फाळणीनंतर आलेला भोपाळ व इंदूरचा सिंधी समुदाय, आणि मराठा काळापासूनची इंदूर व ग्वाल्हेरची मराठीभाषक कुटुंबे हे राज्यातील स्वतःचे स्थलांतरित समुदाय आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants and internal migrants", "प्रवासियों और आंतरिक प्रवासियों की संख्या", "परदेशी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; MEA."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Madhya Pradesh portal", "मध्य प्रदेश सरकार पोर्टल", "मध्य प्रदेश शासन संकेतस्थळ", url="https://www.mp.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Madhya Pradesh Tourism", "मध्य प्रदेश पर्यटन", "मध्य प्रदेश पर्यटन", url="https://www.mptourism.com", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Bhopal", "भोपाल", "भोपाळ"), "0755"], [L("Indore", "इंदौर", "इंदूर"), "0731"], [L("Jabalpur", "जबलपुर", "जबलपूर"), "0761"],
           [L("Gwalior", "ग्वालियर", "ग्वाल्हेर"), "0751"], [L("Ujjain", "उज्जैन", "उज्जैन"), "0734"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("State e-services portal — verified link", "राज्य ई-सेवा पोर्टल — सत्यापित लिंक", "राज्य ई-सेवा संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "MP e-District / services portal."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("forest", ("Madhya Pradesh has the largest forest cover of any Indian State — about 77,073 km² in ISFR 2023.", "मध्य प्रदेश में किसी भी भारतीय राज्य से अधिक वन आवरण है — आईएसएफ़आर 2023 में लगभग 77,073 वर्ग किमी।", "मध्य प्रदेशात कोणत्याही भारतीय राज्यापेक्षा जास्त वनाच्छादन आहे — आयएसएफआर 2023 मध्ये सुमारे 77,073 चौ.किमी."), LS_FOREST, "fsi"),
        triv("panna", ("Panna Diamond is a registered Geographical Indication, and Panna has India's only working diamond mine.", "पन्ना हीरा पंजीकृत भौगोलिक संकेतक है, और पन्ना में भारत की एकमात्र चालू हीरा खदान है।", "पन्ना हिरा हे नोंदणीकृत भौगोलिक मानांकन आहे, आणि पन्ना येथे भारतातील एकमेव कार्यरत हिऱ्याची खाण आहे."), GI_PDF, "gi-registry"),
        triv("amarkantak", ("The Narmada and the Son both rise at Amarkantak but flow in opposite directions.", "नर्मदा और सोन दोनों अमरकंटक से निकलती हैं, पर विपरीत दिशाओं में बहती हैं।", "नर्मदा व सोन दोन्ही अमरकंटक येथे उगम पावतात, पण विरुद्ध दिशांना वाहतात.")),
        triv("tribal", ("The State has India's largest Scheduled Tribe population — about 1.53 crore people in 2011.", "राज्य में भारत की सबसे बड़ी अनुसूचित जनजाति आबादी है — 2011 में लगभग 1.53 करोड़ लोग।", "राज्यात भारतातील सर्वांत मोठी अनुसूचित जमाती लोकसंख्या आहे — 2011 मध्ये सुमारे 1.53 कोटी लोक.")),
        triv("cheetah", ("Kuno National Park received India's first reintroduced cheetahs in September 2022.", "सितंबर 2022 में कूनो राष्ट्रीय उद्यान में भारत में फिर से लाए गए पहले चीते छोड़े गए।", "सप्टेंबर 2022 मध्ये कुनो राष्ट्रीय उद्यानात भारतात पुन्हा आणलेले पहिले चित्ते सोडले गेले.")),
        triv("ls", ("The State elects 29 members to the Lok Sabha.", "राज्य से लोकसभा के 29 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 29 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("mp mod3 ok")
