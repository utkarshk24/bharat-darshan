import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from bd import *

R = "IN-MH"
MOSPI = "https://mospi.gov.in"
SRS = "https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2128024&reg=48&lang=2"
NFHS = "https://rchiips.org/nfhs"
LS_FOREST = "https://eparlib.sansad.in/bitstream/123456789/3021702/1/AU1550_C0eysl.pdf"
NTCA = "https://ntca.gov.in/tiger-reserves/"
RAMSAR = "https://indianwetlands.in/wp-content/uploads/library/1761126102.pdf"
TOUR = "https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2199002&reg=1&lang=1"
GI_PDF = "https://ipindia.gov.in/frontend/pdf/gi/registered/State_wise_Registered_GI_of_India.pdf"
SDB_DIST = "https://mahasdb.maharashtra.gov.in/SDB_Reports/Population_Census/PDF/Districtwise%20population,%20Decadal%20Growth%20rate,%20Sex%20Ratio%20and%20Density%20according%20to%20Census%202011.pdf"
MHT = "https://maharashtratourism.gov.in/districts/dharashiv/"

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Mumbai and Pune are among India's main technology and start-up centres, with IT parks at Hinjawadi and Kharadi in Pune, and Navi Mumbai, Thane and Powai in the Mumbai region. Mumbai is also a hub for fintech, media and data centres, helped by its submarine cable landing stations. Nagpur's MIHAN zone hosts IT and aviation services.",
        "मुंबई और पुणे भारत के प्रमुख प्रौद्योगिकी और स्टार्टअप केंद्रों में हैं; पुणे में हिंजवडी और खराडी, और मुंबई क्षेत्र में नवी मुंबई, ठाणे और पवई में आईटी पार्क हैं। समुद्री केबलों के लैंडिंग स्टेशनों के कारण मुंबई फ़िनटेक, मीडिया और डेटा सेंटरों का भी केंद्र है। नागपुर के मिहान क्षेत्र में आईटी और विमानन सेवाएँ हैं।",
        "मुंबई आणि पुणे ही भारतातील प्रमुख तंत्रज्ञान व स्टार्टअप केंद्रांपैकी आहेत; पुण्यात हिंजवडी आणि खराडी, तर मुंबई परिसरात नवी मुंबई, ठाणे आणि पवई येथे आयटी पार्क आहेत. सागरी केबलच्या लँडिंग स्थानकांमुळे मुंबई फिनटेक, माध्यमे आणि डेटा सेंटरचेही केंद्र आहे. नागपूरच्या मिहान क्षेत्रात आयटी आणि विमानसेवा उद्योग आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI Indian Telecom Services Performance Indicators (Maharashtra + Mumbai circles)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
        (L("BharatNet and 5G coverage", "भारतनेट और 5जी कवरेज", "भारतनेट व 5जी व्याप्ती"), "india-gov", "Department of Telecommunications."),
        (L("Common Service Centres", "कॉमन सर्विस सेंटर", "आपले सरकार सेवा केंद्रे / सीएससी"), "india-gov", "CSC SPV dashboard."),
    ]),
])

# ---------------- N. Education ----------------
AISHE = "https://aishe.gov.in"
module(R, "education", [
    prose("p1", L(
        "Maharashtra has one of India's largest higher-education systems, with 74 universities and 4,692 colleges in the 2021-22 AISHE survey. Its gross enrolment ratio in higher education (ages 18–23) was 35.3%, above the national 28.4%. Pune is known as an education centre, and the State hosts several institutions of national importance, including IIT Bombay, IIM Mumbai, IIM Nagpur, AIIMS Nagpur and VNIT Nagpur.",
        "महाराष्ट्र में भारत की सबसे बड़ी उच्च शिक्षा प्रणालियों में से एक है; 2021-22 के एआईएसएचई सर्वेक्षण में यहाँ 74 विश्वविद्यालय और 4,692 कॉलेज थे। उच्च शिक्षा में सकल नामांकन अनुपात (18–23 वर्ष) 35.3% था, जो राष्ट्रीय 28.4% से अधिक है। पुणे शिक्षा केंद्र के रूप में प्रसिद्ध है, और राज्य में आईआईटी बॉम्बे, आईआईएम मुंबई, आईआईएम नागपुर, एम्स नागपुर और वीएनआईटी नागपुर सहित कई राष्ट्रीय महत्व के संस्थान हैं।",
        "महाराष्ट्रात देशातील सर्वांत मोठ्या उच्चशिक्षण व्यवस्थांपैकी एक आहे; 2021-22 च्या एआयएसएचई सर्वेक्षणानुसार येथे 74 विद्यापीठे आणि 4,692 महाविद्यालये होती. उच्चशिक्षणातील एकूण नोंदणी गुणोत्तर (18–23 वर्षे) 35.3% होते, जे राष्ट्रीय 28.4% पेक्षा जास्त आहे. पुणे हे विद्येचे माहेरघर म्हणून ओळखले जाते, आणि राज्यात आयआयटी मुंबई, आयआयएम मुंबई, आयआयएम नागपूर, एम्स नागपूर आणि व्हीएनआयटी नागपूर यांसह राष्ट्रीय महत्त्वाच्या अनेक संस्था आहेत."),
        sources=["aishe"], conf="Official"),
    facts("f", [
        fact("ger", L("Gross enrolment ratio, higher education (18–23)", "सकल नामांकन अनुपात, उच्च शिक्षा (18–23)", "एकूण नोंदणी गुणोत्तर, उच्चशिक्षण (18–23)"),
             dp(35.30, "%", "2021-22", "survey", "aishe", AISHE, note="AISHE 2021-22, all categories, both sexes (via MoSPI API)."), "percent", "higher-is-better",
             previous=dp(34.92, "%", "2020-21", "survey", "aishe", AISHE), national=dp(28.40, "%", "2021-22", "survey", "aishe", AISHE, level="national")),
        fact("univ", L("Universities", "विश्वविद्यालय", "विद्यापीठे"), dp(74, "count", "2021-22", "survey", "aishe", AISHE), "number"),
        fact("coll", L("Colleges", "कॉलेज", "महाविद्यालये"), dp(4692, "count", "2021-22", "survey", "aishe", AISHE), "number"),
    ]),
    {"type": "series", "id": "ger-series", "title": L("Higher-education GER, 2017-18 to 2021-22", "उच्च शिक्षा जीईआर, 2017-18 से 2021-22", "उच्चशिक्षण जीईआर, 2017-18 ते 2021-22"),
     "kind": "percent", "polarity": "higher-is-better",
     "series": [{"id": "mh", "label": L("Maharashtra", "महाराष्ट्र", "महाराष्ट्र"),
                 "points": [dp(v, "%", y, "survey", "aishe", AISHE) for y, v in [("2017-18", 31.35), ("2018-19", 32.23), ("2019-20", 32.63), ("2020-21", 34.92), ("2021-22", 35.30)]]}]},
    lst("ini", [
        item("iitb", L("IIT Bombay", "आईआईटी बॉम्बे", "आयआयटी मुंबई"), meta=L("Mumbai", "मुंबई", "मुंबई")),
        item("iimm", L("IIM Mumbai", "आईआईएम मुंबई", "आयआयएम मुंबई"), meta=L("Mumbai (formerly NITIE)", "मुंबई (पूर्व में नीटी)", "मुंबई (पूर्वीचे निटी)")),
        item("iimn", L("IIM Nagpur", "आईआईएम नागपुर", "आयआयएम नागपूर"), meta=L("Nagpur", "नागपुर", "नागपूर")),
        item("aiims", L("AIIMS Nagpur", "एम्स नागपुर", "एम्स नागपूर"), meta=L("Nagpur", "नागपुर", "नागपूर")),
        item("vnit", L("VNIT (NIT) Nagpur", "वीएनआईटी (एनआईटी) नागपुर", "व्हीएनआयटी (एनआयटी) नागपूर"), meta=L("Nagpur", "नागपुर", "नागपूर")),
        item("iiitp", L("IIIT Pune", "आईआईआईटी पुणे", "आयआयआयटी पुणे"), meta=L("Pune", "पुणे", "पुणे")),
        item("iiitn", L("IIIT Nagpur", "आईआईआईटी नागपुर", "आयआयआयटी नागपूर"), meta=L("Nagpur", "नागपुर", "नागपूर")),
        item("mnlu", L("Maharashtra National Law Universities", "महाराष्ट्र राष्ट्रीय विधि विश्वविद्यालय", "महाराष्ट्र राष्ट्रीय विधी विद्यापीठे"), meta=L("Mumbai, Nagpur, Chhatrapati Sambhajinagar", "मुंबई, नागपुर, छत्रपति संभाजीनगर", "मुंबई, नागपूर, छत्रपती संभाजीनगर")),
        item("mgahv", L("Mahatma Gandhi Antarrashtriya Hindi Vishwavidyalaya (central university)", "महात्मा गांधी अंतरराष्ट्रीय हिंदी विश्वविद्यालय (केंद्रीय विश्वविद्यालय)", "महात्मा गांधी आंतरराष्ट्रीय हिंदी विश्वविद्यालय (केंद्रीय विद्यापीठ)"), meta=L("Wardha", "वर्धा", "वर्धा")),
    ], title=L("National institutions (selected)", "राष्ट्रीय संस्थान (चयनित)", "राष्ट्रीय संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Dropout rates by level", "स्तरवार ड्रॉपआउट दर", "स्तरनिहाय गळती दर"), "udise", "UDISE+."),
        (L("Literacy by sex", "लिंगवार साक्षरता", "लिंगनिहाय साक्षरता"), "census", "Census 2011 PCA."),
        (L("NIRF-ranked institutions", "एनआईआरएफ़ रैंक वाले संस्थान", "एनआयआरएफ क्रमवारीतील संस्था"), "nirf", "Latest NIRF list filtered to Maharashtra."),
    ]),
])

# ---------------- O. Health ----------------
module(R, "health", [
    prose("p1", L(
        "Maharashtra's mortality indicators are well below the national average. The Sample Registration System put the State's maternal mortality ratio at 38 per lakh live births for 2019-21, against 93 for India, and its under-five mortality at 16 per 1,000 in 2021, against 31 nationally — meeting the SDG targets for both. Almost 95% of births in NFHS-5 took place in health facilities.\n\nChild nutrition remains a concern. In NFHS-5 (2019-21), about 35% of children under five were stunted and about 26% wasted — wasting is notably higher than the national average and showed no improvement since NFHS-4.",
        "महाराष्ट्र के मृत्यु दर संकेतक राष्ट्रीय औसत से काफ़ी कम हैं। नमूना पंजीकरण प्रणाली के अनुसार 2019-21 में राज्य का मातृ मृत्यु अनुपात प्रति लाख जीवित जन्मों पर 38 था, जबकि भारत का 93; और 2021 में पाँच वर्ष से कम आयु की मृत्यु दर प्रति 1,000 पर 16 थी, जबकि राष्ट्रीय दर 31 — यानी दोनों में एसडीजी लक्ष्य पूरे हुए। एनएफ़एचएस-5 में लगभग 95% प्रसव स्वास्थ्य संस्थानों में हुए।\n\nबच्चों का पोषण अब भी चिंता का विषय है। एनएफ़एचएस-5 (2019-21) में पाँच वर्ष से कम आयु के लगभग 35% बच्चे ठिगने (स्टंटेड) और लगभग 26% दुबले (वेस्टेड) थे — दुबलापन राष्ट्रीय औसत से स्पष्ट रूप से अधिक है और एनएफ़एचएस-4 के बाद से इसमें सुधार नहीं हुआ।",
        "महाराष्ट्रातील मृत्युदर निर्देशक राष्ट्रीय सरासरीपेक्षा बरेच कमी आहेत. नमुना नोंदणी पद्धतीनुसार 2019-21 मध्ये राज्याचे माता मृत्यू प्रमाण दर लाख जिवंत जन्मांमागे 38 होते, तर भारताचे 93; आणि 2021 मध्ये पाच वर्षांखालील बालमृत्यू दर दर 1,000 मागे 16 होता, तर राष्ट्रीय दर 31 — म्हणजे दोन्ही बाबतींत एसडीजी उद्दिष्टे गाठली. एनएफएचएस-5 नुसार सुमारे 95% प्रसूती आरोग्य संस्थांमध्ये झाल्या.\n\nबालपोषण अजूनही चिंतेचा विषय आहे. एनएफएचएस-5 (2019-21) मध्ये पाच वर्षांखालील सुमारे 35% मुले खुरटलेली (स्टंटेड) आणि सुमारे 26% कृश (वेस्टेड) होती — कृशतेचे प्रमाण राष्ट्रीय सरासरीपेक्षा लक्षणीयरीत्या जास्त असून एनएफएचएस-4 नंतर त्यात सुधारणा झालेली नाही."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("mort", [
        fact("mmr", L("Maternal mortality ratio", "मातृ मृत्यु अनुपात", "माता मृत्यू प्रमाण"),
             dp(38, "per 1,00,000 live births", "2019-21", "survey", "srs", SRS, note="SRS Special Bulletin on Maternal Mortality 2019-21, as reported by PIB on 10 May 2025."), "number", "lower-is-better",
             national=dp(93, "per 1,00,000 live births", "2019-21", "survey", "srs", SRS, level="national")),
        fact("u5", L("Under-five mortality rate", "पाँच वर्ष से कम आयु मृत्यु दर", "पाच वर्षांखालील मृत्यू दर"),
             dp(16, "per 1,000 live births", "2021", "calendar", "srs", SRS, note="SRS Statistical Report 2021."), "number", "lower-is-better",
             national=dp(31, "per 1,000 live births", "2021", "calendar", "srs", SRS, level="national")),
        fact("nmr", L("Neonatal mortality rate", "नवजात मृत्यु दर", "नवजात मृत्यू दर"),
             dp(11, "per 1,000 live births", "2021", "calendar", "srs", SRS, note="SRS Statistical Report 2021."), "number", "lower-is-better",
             national=dp(19, "per 1,000 live births", "2021", "calendar", "srs", SRS, level="national")),
    ], title=L("Mortality (SRS)", "मृत्यु दर (एसआरएस)", "मृत्युदर (एसआरएस)")),
    facts("nfhs", [
        fact("inst", L("Institutional births", "संस्थागत प्रसव", "संस्थात्मक प्रसूती"),
             dp(94.67, "%", "2019-21", "survey", "nfhs", NFHS, note="NFHS-5, births in the 5 years before the survey (via MoSPI API)."), "percent", "higher-is-better",
             national=dp(88.59, "%", "2019-21", "survey", "nfhs", NFHS, level="national")),
        fact("stunt", L("Children under 5 who are stunted", "पाँच वर्ष से कम आयु के ठिगने बच्चे", "पाच वर्षांखालील खुरटलेली मुले"),
             dp(35.24, "%", "2019-21", "survey", "nfhs", NFHS, note="NFHS-5, height-for-age."), "percent", "lower-is-better",
             previous=dp(34.4, "%", "2015-16", "survey", "nfhs", NFHS), national=dp(35.47, "%", "2019-21", "survey", "nfhs", NFHS, level="national")),
        fact("waste", L("Children under 5 who are wasted", "पाँच वर्ष से कम आयु के दुबले बच्चे", "पाच वर्षांखालील कृश मुले"),
             dp(25.6, "%", "2019-21", "survey", "nfhs", NFHS, note="NFHS-5, weight-for-height."), "percent", "lower-is-better",
             previous=dp(25.6, "%", "2015-16", "survey", "nfhs", NFHS), national=dp(19.26, "%", "2019-21", "survey", "nfhs", NFHS, level="national")),
        fact("under", L("Children under 5 who are underweight", "पाँच वर्ष से कम आयु के कम वज़न वाले बच्चे", "पाच वर्षांखालील कमी वजनाची मुले"),
             dp(36.12, "%", "2019-21", "survey", "nfhs", NFHS, note="NFHS-5, weight-for-age."), "percent", "lower-is-better",
             previous=dp(36.0, "%", "2015-16", "survey", "nfhs", NFHS), national=dp(32.11, "%", "2019-21", "survey", "nfhs", NFHS, level="national")),
    ], title=L("NFHS-5 (2019-21)", "एनएफ़एचएस-5 (2019-21)", "एनएफएचएस-5 (2019-21)")),
    gaps("g", [
        (L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्यू दर"), "srs", "SRS Statistical Report, state table."),
        (L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"), "srs", "SRS abridged life tables."),
        (L("Hospitals, PHCs, CHCs; doctors and beds per 1,000", "अस्पताल, पीएचसी, सीएचसी; प्रति 1,000 डॉक्टर और बिस्तर", "रुग्णालये, प्रा.आ. केंद्रे, ग्रामीण रुग्णालये; दर 1,000 डॉक्टर व खाटा"), "mohfw", "Health Dynamics of India (Rural Health Statistics)."),
        (L("Anaemia and full immunisation (NFHS-5)", "रक्ताल्पता और पूर्ण टीकाकरण (एनएफ़एचएस-5)", "रक्तक्षय व संपूर्ण लसीकरण (एनएफएचएस-5)"), "nfhs", "NFHS-5 state fact sheet."),
        (L("Ayushman Bharat / state insurance coverage", "आयुष्मान भारत / राज्य बीमा कवरेज", "आयुष्मान भारत / राज्य विमा व्याप्ती"), "mohfw", "National Health Authority dashboard."),
    ]),
])

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About 16.5% of Maharashtra's area is under forest cover, below the national 21.8%. Forests are concentrated in two belts: the moist forests of the Sahyadri, part of the Western Ghats biodiversity hotspot, and the dry deciduous teak and bamboo forests of eastern Vidarbha. The coast has mangroves along creeks such as Thane Creek, which draws large flocks of flamingos in winter.\n\nThe State has six tiger reserves and three Ramsar wetlands. The Kaas plateau near Satara is known for its seasonal carpets of wildflowers after the monsoon. Human–wildlife conflict, especially with tigers and leopards near Chandrapur and on the edges of Mumbai, is a recurring challenge.",
        "महाराष्ट्र के लगभग 16.5% क्षेत्र पर वन आवरण है, जो राष्ट्रीय 21.8% से कम है। वन दो पट्टियों में केंद्रित हैं: पश्चिमी घाट जैव-विविधता हॉटस्पॉट का हिस्सा सह्याद्रि के नम वन, और पूर्वी विदर्भ के शुष्क पर्णपाती सागौन व बाँस के वन। तट पर ठाणे खाड़ी जैसी खाड़ियों के किनारे मैंग्रोव हैं, जहाँ सर्दियों में फ़्लेमिंगो के बड़े झुंड आते हैं।\n\nराज्य में छह बाघ अभयारण्य और तीन रामसर आर्द्रभूमियाँ हैं। सातारा के पास कास पठार मानसून के बाद खिलने वाले जंगली फूलों के लिए जाना जाता है। मानव-वन्यजीव संघर्ष, ख़ासकर चंद्रपुर के पास और मुंबई के किनारों पर बाघ और तेंदुओं के साथ, एक बार-बार आने वाली चुनौती है।",
        "महाराष्ट्राच्या सुमारे 16.5% क्षेत्रावर वनाच्छादन आहे, जे राष्ट्रीय 21.8% पेक्षा कमी आहे. वने दोन पट्ट्यांत एकवटलेली आहेत: पश्चिम घाट जैवविविधता केंद्राचा भाग असलेली सह्याद्रीतील आर्द्र वने, आणि पूर्व विदर्भातील शुष्क पानगळीची साग व बांबूची वने. किनाऱ्यावर ठाणे खाडीसारख्या खाड्यांलगत खारफुटी आहे, जिथे हिवाळ्यात रोहित (फ्लेमिंगो) पक्ष्यांचे मोठे थवे येतात.\n\nराज्यात सहा व्याघ्र प्रकल्प आणि तीन रामसर पाणथळ स्थळे आहेत. साताऱ्याजवळचे कास पठार पावसाळ्यानंतर फुलणाऱ्या रानफुलांच्या गालिच्यांसाठी प्रसिद्ध आहे. मानव-वन्यजीव संघर्ष, विशेषतः चंद्रपूरजवळ आणि मुंबईच्या सीमेवर वाघ व बिबट्यांशी, हे सातत्याने समोर येणारे आव्हान आहे."),
        sources=["fsi", "ntca", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(50858.53, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(50913.00, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"),
             read("regions/IN-MH.json")["metrics"]["forestCoverPct"], "percent", "higher-is-better", national=read("india.json")["metrics"]["forestCoverPct"]),
    ]),
    table("tiger", L("Tiger reserves", "बाघ अभयारण्य", "व्याघ्र प्रकल्प"),
          [col(L("Tiger reserve", "बाघ अभयारण्य", "व्याघ्र प्रकल्प")), col(L("Notified", "अधिसूचित", "अधिसूचना"), "right"), col(L("Core (km²)", "कोर (किमी²)", "गाभा (किमी²)"), "right"), col(L("Buffer (km²)", "बफ़र (किमी²)", "बफर (किमी²)"), "right"), col(L("Total (km²)", "कुल (किमी²)", "एकूण (किमी²)"), "right")],
          [[L("Melghat", "मेलघाट", "मेळघाट"), "2007", "1,500.49", "1,268.03", "2,768.52"],
           [L("Nawegaon–Nagzira", "नवेगांव–नागझिरा", "नवेगाव–नागझिरा"), "2013", "653.67", "1,241.27", "1,894.94"],
           [L("Tadoba–Andhari", "ताडोबा–अंधारी", "ताडोबा–अंधारी"), "2007", "625.82", "1,101.77", "1,727.59"],
           [L("Sahyadri", "सह्याद्रि", "सह्याद्री"), "2012", "600.12", "565.45", "1,165.57"],
           [L("Bor", "बोर", "बोर"), "2014", "138.12", "678.15", "816.27"],
           [L("Pench (Maharashtra)", "पेंच (महाराष्ट्र)", "पेंच (महाराष्ट्र)"), "2007", "257.26", "483.96", "741.22"]],
          "ntca", NTCA,
          note=L("Notification year as listed by NTCA (Melghat was among India's first tiger reserves in 1973-74; the year shown is the later notification of its core). India has 58 tiger reserves.",
                 "अधिसूचना वर्ष एनटीसीए की सूची के अनुसार (मेलघाट 1973-74 में भारत के पहले बाघ अभयारण्यों में था; दिखाया गया वर्ष उसके कोर क्षेत्र की बाद की अधिसूचना है)। भारत में 58 बाघ अभयारण्य हैं।",
                 "अधिसूचना वर्ष एनटीसीएच्या यादीनुसार (मेळघाट 1973-74 मध्ये भारतातील पहिल्या व्याघ्र प्रकल्पांपैकी एक होता; दाखवलेले वर्ष त्याच्या गाभा क्षेत्राच्या नंतरच्या अधिसूचनेचे आहे). भारतात 58 व्याघ्र प्रकल्प आहेत.")),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हे.)", "क्षेत्र (हे.)"), "right")],
          [[L("Nandur Madhameshwar (Nashik)", "नांदूर मधमेश्वर (नासिक)", "नांदूर मध्यमेश्वर (नाशिक)"), "21 Jun 2019", 1437],
           [L("Lonar Lake (Buldhana)", "लोणार झील (बुलढाणा)", "लोणार सरोवर (बुलढाणा)"), "22 Jul 2020", 427],
           [L("Thane Creek", "ठाणे खाड़ी", "ठाणे खाडी"), "13 Apr 2022", 6521]],
          "indian-wetlands", RAMSAR, note=L("India has 99 Ramsar sites (list as on 21 April 2026).", "भारत में 99 रामसर स्थल हैं (21 अप्रैल 2026 की सूची)।", "भारतात 99 रामसर स्थळे आहेत (21 एप्रिल 2026 ची यादी).")),
    lst("species", [
        item("tiger", L("Bengal tiger", "बंगाल बाघ", "पट्टेरी वाघ"), meta=L("Tadoba, Melghat, Pench", "ताडोबा, मेलघाट, पेंच", "ताडोबा, मेळघाट, पेंच")),
        item("shekru", L("Indian giant squirrel (Shekru)", "भारतीय विशाल गिलहरी (शेकरू)", "शेकरू"), meta=L("Bhimashankar", "भीमाशंकर", "भीमाशंकर")),
        item("gib", L("Great Indian bustard", "सोन चिरैया (ग्रेट इंडियन बस्टर्ड)", "माळढोक"), meta=L("Critically endangered; Solapur grasslands", "अति संकटग्रस्त; सोलापुर के घास के मैदान", "अतिसंकटग्रस्त; सोलापूरची गवताळ कुरणे")),
        item("flamingo", L("Flamingos", "फ़्लेमिंगो", "रोहित (फ्लेमिंगो)"), meta=L("Thane Creek, winter", "ठाणे खाड़ी, सर्दियाँ", "ठाणे खाडी, हिवाळा")),
        item("leopard", L("Leopard", "तेंदुआ", "बिबट्या"), meta=L("Sanjay Gandhi National Park, Junnar", "संजय गांधी राष्ट्रीय उद्यान, जुन्नर", "संजय गांधी राष्ट्रीय उद्यान, जुन्नर")),
        item("blackbuck", L("Blackbuck", "काला हिरण", "काळवीट"), meta=L("Grasslands of the Deccan", "दक्कन के घास के मैदान", "दख्खनची गवताळ कुरणे")),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("National parks and sanctuaries (count, area)", "राष्ट्रीय उद्यान और अभयारण्य (संख्या, क्षेत्रफल)", "राष्ट्रीय उद्याने व अभयारण्ये (संख्या, क्षेत्र)"), "moefcc", "ENVIS Protected Areas database / Maharashtra Forest Department."),
        (L("Mangrove and tree cover", "मैंग्रोव और वृक्ष आवरण", "खारफुटी व वृक्षाच्छादन"), "fsi", "ISFR 2023, Maharashtra chapter."),
        (L("Biosphere and elephant reserves", "बायोस्फ़ीयर और हाथी रिज़र्व", "जीवावरण व हत्ती राखीव क्षेत्रे"), "moefcc", "MoEFCC lists."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Most of Maharashtra drains east through the Godavari and Krishna basins, with smaller shares in the Tapi–Narmada system and the short west-flowing Konkan rivers. The State has the largest number of large dams in India, but much of the Deccan plateau relies on rain-fed farming and seasonal groundwater, and Marathwada in particular faces recurring drought and drinking-water shortages.\n\nWater sharing with neighbouring States has been settled or contested before tribunals, including the Krishna and Godavari Water Disputes Tribunals and the Mahadayi tribunal shared with Goa and Karnataka. This section presents those matters neutrally, with official sources.",
        "महाराष्ट्र का अधिकांश हिस्सा गोदावरी और कृष्णा घाटियों से होकर पूर्व की ओर बहता है; छोटा हिस्सा तापी–नर्मदा प्रणाली और कोंकण की पश्चिम-वाहिनी छोटी नदियों में जाता है। राज्य में देश के सबसे अधिक बड़े बाँध हैं, फिर भी दक्कन पठार का बड़ा भाग वर्षा-आधारित खेती और मौसमी भूजल पर निर्भर है, और विशेषकर मराठवाड़ा बार-बार सूखे और पेयजल की कमी का सामना करता है।\n\nपड़ोसी राज्यों के साथ जल-बँटवारे के मामले न्यायाधिकरणों में तय या विचाराधीन रहे हैं, जिनमें कृष्णा और गोदावरी जल विवाद न्यायाधिकरण तथा गोवा और कर्नाटक के साथ महादयी न्यायाधिकरण शामिल हैं। यह खंड इन मामलों को आधिकारिक स्रोतों के साथ निष्पक्ष रूप से प्रस्तुत करता है।",
        "महाराष्ट्राचा बहुतांश भाग गोदावरी आणि कृष्णा खोऱ्यांतून पूर्वेकडे वाहतो; थोडा भाग तापी–नर्मदा प्रणालीत आणि कोकणातील पश्चिमवाहिनी लहान नद्यांत जातो. देशात सर्वाधिक मोठी धरणे महाराष्ट्रात आहेत, तरीही दख्खन पठाराचा मोठा भाग पावसावर अवलंबून शेती आणि हंगामी भूजलावर चालतो, आणि विशेषतः मराठवाड्याला वारंवार दुष्काळ व पिण्याच्या पाण्याच्या टंचाईला तोंड द्यावे लागते.\n\nशेजारी राज्यांसोबतचे पाणीवाटपाचे प्रश्न लवादांसमोर निकाली निघाले आहेत किंवा प्रलंबित आहेत, ज्यात कृष्णा आणि गोदावरी पाणीतंटा लवाद तसेच गोवा व कर्नाटकसोबतचा म्हादई लवाद यांचा समावेश आहे. हा विभाग हे प्रश्न अधिकृत स्रोतांसह निःपक्षपणे मांडतो."),
        conf="Editorial"),
    gaps("g", [
        (L("Large dams (count)", "बड़े बाँध (संख्या)", "मोठी धरणे (संख्या)"), "mh-gov", "Central Water Commission National Register of Large Dams."),
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "mh-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
        (L("Net irrigated area", "शुद्ध सिंचित क्षेत्र", "निव्वळ सिंचित क्षेत्र"), "mh-sdb", "State Data Bank lists gross irrigated area as not available; use Land Use Statistics."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Maharashtra faces several natural hazards: cyclones and storm surges on the Konkan coast (Nisarga in 2020, Tauktae in 2021), urban flooding in Mumbai during heavy monsoon rain (as on 26 July 2005), landslides on the ghats, drought on the plateau and heatwaves in Vidarbha. The 1967 Koyna and 1993 Killari (Latur) earthquakes caused major loss of life. The Maharashtra State Disaster Management Authority coordinates preparedness and response.",
        "महाराष्ट्र कई प्राकृतिक आपदाओं का सामना करता है: कोंकण तट पर चक्रवात और तूफ़ानी लहरें (2020 में निसर्ग, 2021 में ताउते), भारी मानसूनी वर्षा में मुंबई में शहरी बाढ़ (जैसे 26 जुलाई 2005 को), घाटों पर भूस्खलन, पठार पर सूखा और विदर्भ में लू। 1967 के कोयना और 1993 के किल्लारी (लातूर) भूकंपों में भारी जनहानि हुई। महाराष्ट्र राज्य आपदा प्रबंधन प्राधिकरण तैयारी और राहत का समन्वय करता है।",
        "महाराष्ट्राला अनेक नैसर्गिक आपत्तींचा सामना करावा लागतो: कोकणकिनाऱ्यावर चक्रीवादळे व वादळी लाटा (2020 मध्ये निसर्ग, 2021 मध्ये तौक्ते), मुसळधार पावसात मुंबईतील शहरी पूर (उदा. 26 जुलै 2005), घाटांवर दरडी कोसळणे, पठारावर दुष्काळ आणि विदर्भात उष्णतेच्या लाटा. 1967 चा कोयना आणि 1993 चा किल्लारी (लातूर) भूकंप यांत मोठी जीवितहानी झाली. महाराष्ट्र राज्य आपत्ती व्यवस्थापन प्राधिकरण पूर्वतयारी आणि मदतकार्याचे समन्वय करते."),
        conf="Editorial"),
    table("numbers", L("Emergency numbers", "आपातकालीन नंबर", "आपत्कालीन क्रमांक"),
          [col(L("Service", "सेवा", "सेवा")), col(L("Number", "नंबर", "क्रमांक"), "right")],
          [[L("Emergency response (police, fire, ambulance)", "आपातकालीन सहायता (पुलिस, अग्निशमन, एंबुलेंस)", "आपत्कालीन मदत (पोलीस, अग्निशमन, रुग्णवाहिका)"), "112"],
           [L("Ambulance", "एंबुलेंस", "रुग्णवाहिका"), "108"],
           [L("Women's helpline", "महिला हेल्पलाइन", "महिला हेल्पलाइन"), "1091 / 181"],
           [L("Child helpline", "चाइल्ड हेल्पलाइन", "चाइल्ड हेल्पलाइन"), "1098"],
           [L("Cybercrime", "साइबर अपराध", "सायबर गुन्हे"), "1930"],
           [L("Tourist helpline (Ministry of Tourism)", "पर्यटक हेल्पलाइन (पर्यटन मंत्रालय)", "पर्यटक हेल्पलाइन (पर्यटन मंत्रालय)"), "1800-11-1363"]],
          "india-gov", "https://www.india.gov.in", conf="Official", access=None,
          note=L("National numbers that work in Maharashtra.", "राष्ट्रीय नंबर जो महाराष्ट्र में काम करते हैं।", "महाराष्ट्रात चालणारे राष्ट्रीय क्रमांक.")),
    lst("links", [
        item("sdma", L("Maharashtra State Disaster Management Authority", "महाराष्ट्र राज्य आपदा प्रबंधन प्राधिकरण", "महाराष्ट्र राज्य आपत्ती व्यवस्थापन प्राधिकरण"), url="https://sdma.maharashtra.gov.in", src="mh-gov"),
        item("imd", L("IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे"), url="https://mausam.imd.gov.in", src="imd"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Police commissionerates (count)", "पुलिस आयुक्तालय (संख्या)", "पोलीस आयुक्तालये (संख्या)"), "mh-gov", "Maharashtra Police website."),
        (L("Hospital locator", "अस्पताल खोजें", "रुग्णालय शोधक"), "mohfw", "Link a national facility registry once integrated."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Maharashtra has 55 registered Geographical Indications, more than most States, as listed by the GI Registry on 31 December 2025. Most are agricultural — from Alphonso mangoes and Nashik grapes to Lasalgaon onions and several regional rice and turmeric varieties — alongside crafts such as Paithani saris, Kolhapuri chappals, Warli painting, Miraj sitars and tanpuras, and Pen's Ganesh idols. Three GIs are shared with neighbouring States.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची के अनुसार महाराष्ट्र के 55 पंजीकृत भौगोलिक संकेतक (जीआई) हैं, जो अधिकांश राज्यों से अधिक है। इनमें ज़्यादातर कृषि उत्पाद हैं — अल्फांसो आम और नासिक के अंगूर से लेकर लासलगांव प्याज़ और चावल व हल्दी की कई क्षेत्रीय किस्में — साथ ही पैठणी साड़ी, कोल्हापुरी चप्पल, वारली चित्रकला, मिरज के सितार और तानपूरे, और पेण की गणेश मूर्तियाँ जैसे शिल्प भी। तीन जीआई पड़ोसी राज्यों के साथ साझा हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीनुसार महाराष्ट्राची 55 नोंदणीकृत भौगोलिक मानांकने (जीआय) आहेत, जी बहुतेक राज्यांपेक्षा अधिक आहेत. यात बहुतांश कृषी उत्पादने आहेत — हापूस आंबा आणि नाशिकच्या द्राक्षांपासून लासलगावचा कांदा आणि तांदूळ व हळदीच्या अनेक प्रादेशिक जातींपर्यंत — सोबतच पैठणी, कोल्हापुरी चप्पल, वारली चित्रकला, मिरजेच्या सतारी व तानपुरे आणि पेणच्या गणेशमूर्ती यांसारख्या हस्तकलाही. तीन जीआय शेजारी राज्यांसोबत सामायिक आहेत."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI Registry application detail pages."),
        (L("One District One Product (ODOP) items", "एक ज़िला एक उत्पाद (ओडीओपी)", "एक जिल्हा एक उत्पादन (ओडीओपी)"), "dpiit", "DPIIT ODOP list for Maharashtra."),
    ]),
])

# ---------------- T. Tourism ----------------
def visits(v, y, note=None):
    return dp(v, "visits", y, "calendar", "tourism", TOUR, note=note)
module(R, "tourism", [
    prose("p1", L(
        "Maharashtra received about 18.94 crore domestic and 37 lakh foreign tourist visits in 2024, according to the Ministry of Tourism. The main draws are the Ajanta and Ellora caves, Mumbai's Victorian and Art Deco architecture, the Maratha forts, pilgrimage centres such as Shirdi, Pandharpur, Trimbakeshwar and the Jyotirlinga at Bhimashankar, hill stations such as Mahabaleshwar, Matheran and Lonavala, the Konkan beaches, and tiger safaris at Tadoba.\n\nNo special permit is needed for Indian or foreign visitors, apart from standard rules in protected areas and defence zones.",
        "पर्यटन मंत्रालय के अनुसार 2024 में महाराष्ट्र में लगभग 18.94 करोड़ घरेलू और 37 लाख विदेशी पर्यटक-यात्राएँ हुईं। मुख्य आकर्षण हैं अजंता और एलोरा की गुफ़ाएँ, मुंबई की विक्टोरियन और आर्ट डेको इमारतें, मराठा क़िले, शिर्डी, पंढरपुर, त्र्यंबकेश्वर और भीमाशंकर ज्योतिर्लिंग जैसे तीर्थ, महाबलेश्वर, माथेरान और लोनावला जैसे हिल स्टेशन, कोंकण के समुद्र तट और ताडोबा में बाघ सफ़ारी।\n\nभारतीय या विदेशी पर्यटकों के लिए कोई विशेष परमिट ज़रूरी नहीं है; केवल संरक्षित क्षेत्रों और रक्षा क्षेत्रों के सामान्य नियम लागू होते हैं।",
        "पर्यटन मंत्रालयानुसार 2024 मध्ये महाराष्ट्राला सुमारे 18.94 कोटी देशी आणि 37 लाख परदेशी पर्यटक भेटी मिळाल्या. अजिंठा-वेरूळ लेणी, मुंबईतील व्हिक्टोरियन व आर्ट डेको इमारती, मराठा किल्ले, शिर्डी, पंढरपूर, त्र्यंबकेश्वर व भीमाशंकर ज्योतिर्लिंग यांसारखी तीर्थक्षेत्रे, महाबळेश्वर, माथेरान, लोणावळा यांसारखी थंड हवेची ठिकाणे, कोकणातील समुद्रकिनारे आणि ताडोब्यातील व्याघ्र सफारी ही प्रमुख आकर्षणे आहेत.\n\nभारतीय किंवा परदेशी पर्यटकांना विशेष परवान्याची गरज नाही; केवळ संरक्षित क्षेत्रे व संरक्षण क्षेत्रांचे नेहमीचे नियम लागू होतात."),
        sources=["tourism"], conf="Official"),
    facts("f", [
        fact("dtv", L("Domestic tourist visits", "घरेलू पर्यटक यात्राएँ", "देशी पर्यटक भेटी"), visits(189371541, "2024", "Ministry of Tourism, via PIB Mumbai (4 Dec 2025)."), "count", "neutral",
             previous=visits(161359527, "2023")),
        fact("ftv", L("Foreign tourist visits", "विदेशी पर्यटक यात्राएँ", "परदेशी पर्यटक भेटी"), visits(3705170, "2024", "Ministry of Tourism, via PIB Mumbai (4 Dec 2025)."), "count", "neutral",
             previous=visits(3387739, "2023")),
    ]),
    {"type": "series", "id": "visits", "title": L("Tourist visits, 2022–2024", "पर्यटक यात्राएँ, 2022–2024", "पर्यटक भेटी, 2022–2024"), "kind": "count", "polarity": "neutral",
     "series": [{"id": "dtv", "label": L("Domestic", "घरेलू", "देशी"), "points": [visits(111297624, "2022"), visits(161359527, "2023"), visits(189371541, "2024")]},
                {"id": "ftv", "label": L("Foreign", "विदेशी", "परदेशी"), "points": [visits(1511623, "2022"), visits(3387739, "2023"), visits(3705170, "2024")]}],
     "note": L("2022 figures reflect the recovery after the pandemic.", "2022 के आँकड़े महामारी के बाद की वापसी दिखाते हैं।", "2022 ची आकडेवारी महामारीनंतरचे सावरणे दर्शवते.")},
    lst("places", [
        item("ajanta", L("Ajanta and Ellora", "अजंता और एलोरा", "अजिंठा आणि वेरूळ"), meta=L("Heritage", "धरोहर", "वारसा")),
        item("mumbai", L("South Mumbai heritage precinct and Elephanta", "दक्षिण मुंबई धरोहर क्षेत्र और एलिफेंटा", "दक्षिण मुंबई वारसा परिसर आणि घारापुरी"), meta=L("Heritage", "धरोहर", "वारसा")),
        item("forts", L("Raigad, Rajgad, Sindhudurg and other Maratha forts", "रायगढ़, राजगढ़, सिंधुदुर्ग और अन्य मराठा क़िले", "रायगड, राजगड, सिंधुदुर्ग व इतर मराठा किल्ले"), meta=L("Heritage, trekking", "धरोहर, ट्रेकिंग", "वारसा, गिर्यारोहण")),
        item("shirdi", L("Shirdi, Pandharpur, Trimbakeshwar, Bhimashankar", "शिर्डी, पंढरपुर, त्र्यंबकेश्वर, भीमाशंकर", "शिर्डी, पंढरपूर, त्र्यंबकेश्वर, भीमाशंकर"), meta=L("Spiritual", "आध्यात्मिक", "धार्मिक")),
        item("hills", L("Mahabaleshwar, Matheran, Lonavala", "महाबलेश्वर, माथेरान, लोनावला", "महाबळेश्वर, माथेरान, लोणावळा"), meta=L("Hill stations", "हिल स्टेशन", "थंड हवेची ठिकाणे")),
        item("tadoba", L("Tadoba–Andhari Tiger Reserve", "ताडोबा–अंधारी बाघ अभयारण्य", "ताडोबा–अंधारी व्याघ्र प्रकल्प"), meta=L("Wildlife", "वन्यजीव", "वन्यजीव")),
        item("konkan", L("Tarkarli, Ganpatipule, Alibag, Diveagar", "तारकर्ली, गणपतिपुळे, अलीबाग, दिवेआगर", "तारकर्ली, गणपतीपुळे, अलिबाग, दिवेआगर"), meta=L("Beaches", "समुद्र तट", "समुद्रकिनारे")),
        item("kaas", L("Kaas plateau and Lonar crater", "कास पठार और लोणार क्रेटर", "कास पठार आणि लोणार विवर"), meta=L("Nature, offbeat", "प्रकृति, कम भीड़ वाले", "निसर्ग, वेगळी ठिकाणे")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        item("d2", L("2 days", "2 दिन", "2 दिवस"), detail=L("Mumbai: Gateway of India, Kala Ghoda and the Fort precinct, CSMT; ferry to Elephanta.", "मुंबई: गेटवे ऑफ़ इंडिया, काला घोड़ा और फ़ोर्ट क्षेत्र, सीएसएमटी; एलिफेंटा तक फ़ेरी।", "मुंबई: गेटवे ऑफ इंडिया, काळा घोडा व फोर्ट परिसर, सीएसएमटी; घारापुरीला फेरी.")),
        item("d3", L("3 days", "3 दिन", "3 दिवस"), detail=L("Chhatrapati Sambhajinagar base: Ellora and Daulatabad, then a full day at Ajanta.", "छत्रपति संभाजीनगर से: एलोरा और दौलताबाद, फिर पूरा दिन अजंता।", "छत्रपती संभाजीनगर मुक्काम: वेरूळ व देवगिरी (दौलताबाद), मग पूर्ण दिवस अजिंठा.")),
        item("d5", L("5 days", "5 दिन", "5 दिवस"), detail=L("Pune's wadas and Shaniwar Wada, Sinhagad, then Mahabaleshwar and Pratapgad, and the Kaas plateau in season.", "पुणे के वाड़े और शनिवारवाड़ा, सिंहगढ़, फिर महाबलेश्वर और प्रतापगढ़, और मौसम में कास पठार।", "पुण्याचे वाडे व शनिवारवाडा, सिंहगड, मग महाबळेश्वर, प्रतापगड आणि हंगामात कास पठार.")),
        item("d7", L("7 days", "7 दिन", "7 दिवस"), detail=L("Konkan coast by road or Konkan Railway: Alibag, Ganpatipule, Ratnagiri, Sindhudurg fort and Tarkarli.", "सड़क या कोंकण रेलवे से कोंकण तट: अलीबाग, गणपतिपुळे, रत्नागिरी, सिंधुदुर्ग क़िला और तारकर्ली।", "रस्त्याने किंवा कोकण रेल्वेने कोकणकिनारा: अलिबाग, गणपतीपुळे, रत्नागिरी, सिंधुदुर्ग किल्ला आणि तारकर्ली.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    table("schemes", L("Ministry of Tourism projects in Maharashtra (selected)", "महाराष्ट्र में पर्यटन मंत्रालय की परियोजनाएँ (चयनित)", "महाराष्ट्रातील पर्यटन मंत्रालयाचे प्रकल्प (निवडक)"),
          [col(L("Project", "परियोजना", "प्रकल्प")), col(L("Scheme", "योजना", "योजना")), col(L("Sanctioned (₹ crore)", "स्वीकृत (₹ करोड़)", "मंजूर (₹ कोटी)"), "right")],
          [[L("Sindhudurg Coastal Circuit (complete)", "सिंधुदुर्ग तटीय सर्किट (पूर्ण)", "सिंधुदुर्ग किनारी सर्किट (पूर्ण)"), "Swadesh Darshan", "19.06"],
           [L("Shivsrushti Historical Theme Park, Phase 3, Pune", "शिवसृष्टि ऐतिहासिक थीम पार्क, चरण 3, पुणे", "शिवसृष्टी ऐतिहासिक थीम पार्क, टप्पा 3, पुणे"), "Swadesh Darshan 2.0", "76.22"],
           [L("Trimbakeshwar, Nashik", "त्र्यंबकेश्वर, नासिक", "त्र्यंबकेश्वर, नाशिक"), "PRASHAD", "45.41"],
           [L("Ram-Kal Path, Nashik", "राम-काल पथ, नासिक", "राम-काल पथ, नाशिक"), "SASCI", "99.14"],
           [L("Ex-INS Guldar underwater museum, Sindhudurg", "पूर्व आईएनएस गुलदार अंडरवॉटर संग्रहालय, सिंधुदुर्ग", "माजी आयएनएस गुलदार पाण्याखालील संग्रहालय, सिंधुदुर्ग"), "SASCI", "46.91"],
           [L("Ahmednagar Fort", "अहमदनगर क़िला", "अहमदनगर किल्ला"), "CBDD", "25.00"]],
          "pib", TOUR, period="2015–2025"),
    gaps("g", [
        (L("Top source markets for foreign visitors", "विदेशी पर्यटकों के प्रमुख स्रोत देश", "परदेशी पर्यटकांचे प्रमुख देश"), "tourism", "India Tourism Statistics."),
        (L("Foreign exchange earnings from tourism", "पर्यटन से विदेशी मुद्रा आय", "पर्यटनातून परकीय चलन उत्पन्न"), "tourism", "Not published state-wise; confirm."),
    ]),
])

# ---------------- U. Cities ----------------
DIST_ROWS = [
    ("Nandurbar", "नंदुरबार", "नंदुरबार", 1646177, 25.5, 972, 276), ("Dhule", "धुले", "धुळे", 2048781, 20.0, 941, 285),
    ("Jalgaon", "जलगांव", "जळगाव", 4224442, 14.7, 922, 359), ("Buldhana", "बुलढाणा", "बुलढाणा", 2588039, 15.9, 928, 268),
    ("Akola", "अकोला", "अकोला", 1818617, 11.6, 942, 321), ("Washim", "वाशिम", "वाशिम", 1196714, 17.2, 926, 244),
    ("Amravati", "अमरावती", "अमरावती", 2887826, 10.8, 947, 237), ("Wardha", "वर्धा", "वर्धा", 1296157, 4.8, 946, 205),
    ("Nagpur", "नागपुर", "नागपूर", 4653171, 14.4, 948, 470), ("Bhandara", "भंडारा", "भंडारा", 1198810, 5.5, 984, 293),
    ("Gondia", "गोंदिया", "गोंदिया", 1322331, 10.1, 996, 253), ("Gadchiroli", "गढ़चिरौली", "गडचिरोली", 1071795, 10.5, 975, 74),
    ("Chandrapur", "चंद्रपुर", "चंद्रपूर", 2194262, 6.0, 959, 192), ("Yavatmal", "यवतमाल", "यवतमाळ", 2775457, 12.9, 947, 204),
    ("Nanded", "नांदेड़", "नांदेड", 3356566, 16.7, 937, 319), ("Hingoli", "हिंगोली", "हिंगोली", 1178973, 19.4, 935, 244),
    ("Parbhani", "परभणी", "परभणी", 1835982, 20.2, 940, 295), ("Jalna", "जालना", "जालना", 1958483, 21.8, 929, 255),
    ("Chhatrapati Sambhajinagar (Aurangabad)", "छत्रपति संभाजीनगर (औरंगाबाद)", "छत्रपती संभाजीनगर (औरंगाबाद)", 3695928, 27.3, 917, 365),
    ("Nashik", "नासिक", "नाशिक", 6109052, 22.3, 931, 393),
    ("Thane (incl. present Palghar)", "ठाणे (वर्तमान पालघर सहित)", "ठाणे (सध्याच्या पालघरसह)", 11054131, 35.9, 880, 1157),
    ("Mumbai Suburban", "मुंबई उपनगर", "मुंबई उपनगर", 9332481, 8.0, 857, 20925), ("Mumbai City", "मुंबई शहर", "मुंबई शहर", 3145966, -5.8, 838, 20038),
    ("Raigad", "रायगढ़", "रायगड", 2635394, 19.4, 955, 368), ("Pune", "पुणे", "पुणे", 9426959, 30.3, 910, 603),
    ("Ahilyanagar (Ahmednagar)", "अहिल्यानगर (अहमदनगर)", "अहिल्यानगर (अहमदनगर)", 4543083, 12.4, 934, 266),
    ("Beed", "बीड", "बीड", 2585962, 19.7, 912, 242), ("Latur", "लातूर", "लातूर", 2455543, 18.0, 924, 343),
    ("Dharashiv (Osmanabad)", "धाराशिव (उस्मानाबाद)", "धाराशिव (उस्मानाबाद)", 1660311, 11.7, 920, 219),
    ("Solapur", "सोलापुर", "सोलापूर", 4315527, 12.1, 932, 290), ("Satara", "सातारा", "सातारा", 3003922, 6.9, 986, 287),
    ("Ratnagiri", "रत्नागिरी", "रत्नागिरी", 1612672, -5.0, 1123, 196), ("Sindhudurg", "सिंधुदुर्ग", "सिंधुदुर्ग", 848868, -2.3, 1037, 163),
    ("Kolhapur", "कोल्हापुर", "कोल्हापूर", 3874015, 10.0, 953, 504), ("Sangli", "सांगली", "सांगली", 2820575, 9.2, 964, 329),
]
def city(id, en, hi, mr, d_en, d_hi, d_mr, b_en, b_hi, b_mr):
    return item(id, L(en, hi, mr), detail=L(d_en, d_hi, d_mr), meta=L(b_en, b_hi, b_mr))
module(R, "cities", [
    lst("cities", [
        city("mumbai", "Mumbai", "मुंबई", "मुंबई", "State capital; India's financial and film capital; ports, Victorian Gothic and Art Deco heritage.", "राज्य की राजधानी; भारत की वित्तीय और फ़िल्म राजधानी; बंदरगाह, विक्टोरियन गॉथिक और आर्ट डेको विरासत।", "राज्याची राजधानी; भारताची आर्थिक व चित्रपट राजधानी; बंदरे, व्हिक्टोरियन गॉथिक व आर्ट डेको वारसा.", "Brihanmumbai Municipal Corporation", "बृहन्मुंबई महानगरपालिका", "बृहन्मुंबई महानगरपालिका"),
        city("pune", "Pune", "पुणे", "पुणे", "Education and IT hub; automotive industry around Chakan and Pimpri-Chinchwad; Peshwa-era heritage.", "शिक्षा और आईटी केंद्र; चाकण और पिंपरी-चिंचवड़ के आसपास ऑटोमोबाइल उद्योग; पेशवा काल की विरासत।", "शिक्षण व आयटी केंद्र; चाकण आणि पिंपरी-चिंचवड परिसरात वाहन उद्योग; पेशवेकालीन वारसा.", "Pune Municipal Corporation", "पुणे महानगरपालिका", "पुणे महानगरपालिका"),
        city("nagpur", "Nagpur", "नागपुर", "नागपूर", "Winter session capital; geographic centre of India; oranges, MIHAN logistics hub.", "शीतकालीन सत्र की राजधानी; भारत का भौगोलिक केंद्र; संतरे, मिहान लॉजिस्टिक्स केंद्र।", "हिवाळी अधिवेशनाची राजधानी; भारताचा भौगोलिक मध्य; संत्री, मिहान लॉजिस्टिक्स केंद्र.", "Nagpur Municipal Corporation", "नागपुर महानगरपालिका", "नागपूर महानगरपालिका"),
        city("thane", "Thane", "ठाणे", "ठाणे", "Lake city and fast-growing residential and industrial centre in the Mumbai region.", "मुंबई क्षेत्र का झीलों वाला शहर और तेज़ी से बढ़ता आवासीय व औद्योगिक केंद्र।", "मुंबई परिसरातील तलावांचे शहर आणि वेगाने वाढणारे निवासी व औद्योगिक केंद्र.", "Thane Municipal Corporation", "ठाणे महानगरपालिका", "ठाणे महानगरपालिका"),
        city("nashik", "Nashik", "नासिक", "नाशिक", "Pilgrimage city on the Godavari, host of the Kumbh Mela; grapes and wine; HAL aircraft plant at Ozar.", "गोदावरी तट का तीर्थ नगर, कुंभ मेले का आयोजक; अंगूर और वाइन; ओझर में एचएएल विमान संयंत्र।", "गोदावरीकाठचे तीर्थक्षेत्र, कुंभमेळ्याचे यजमान; द्राक्षे व वाइन; ओझर येथे एचएएलचा विमान कारखाना.", "Nashik Municipal Corporation", "नासिक महानगरपालिका", "नाशिक महानगरपालिका"),
        city("chs", "Chhatrapati Sambhajinagar", "छत्रपति संभाजीनगर", "छत्रपती संभाजीनगर", "Gateway to Ajanta and Ellora; Bibi-ka-Maqbara; auto industry at Waluj and Shendra.", "अजंता और एलोरा का प्रवेश द्वार; बीबी का मक़बरा; वालुज और शेंद्रा में ऑटो उद्योग।", "अजिंठा-वेरूळचे प्रवेशद्वार; बीबी का मकबरा; वाळूज व शेंद्रा येथे वाहन उद्योग.", "Chhatrapati Sambhajinagar Municipal Corporation", "छत्रपति संभाजीनगर महानगरपालिका", "छत्रपती संभाजीनगर महानगरपालिका"),
        city("solapur", "Solapur", "सोलापुर", "सोलापूर", "Textile city known for chaddars and terry towels; close to Pandharpur and Tuljapur.", "चादरों और टेरी तौलियों के लिए प्रसिद्ध कपड़ा शहर; पंढरपुर और तुलजापुर के पास।", "चादरी आणि टेरी टॉवेलसाठी प्रसिद्ध वस्त्रनगरी; पंढरपूर व तुळजापूरजवळ.", "Solapur Municipal Corporation", "सोलापुर महानगरपालिका", "सोलापूर महानगरपालिका"),
        city("kolhapur", "Kolhapur", "कोल्हापुर", "कोल्हापूर", "Mahalaxmi temple, Kolhapuri chappals and cuisine, wrestling tradition and sugar co-operatives.", "महालक्ष्मी मंदिर, कोल्हापुरी चप्पल और व्यंजन, कुश्ती की परंपरा और चीनी सहकारी संस्थाएँ।", "महालक्ष्मी मंदिर, कोल्हापुरी चप्पल व खाद्यसंस्कृती, कुस्तीची परंपरा आणि साखर सहकारी संस्था.", "Kolhapur Municipal Corporation", "कोल्हापुर महानगरपालिका", "कोल्हापूर महानगरपालिका"),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    table("districts", L("Districts at the 2011 Census", "2011 की जनगणना के अनुसार ज़िले", "2011 च्या जनगणनेनुसार जिल्हे"),
          [col(L("District (current name)", "ज़िला (वर्तमान नाम)", "जिल्हा (सध्याचे नाव)")), col(L("Population", "जनसंख्या", "लोकसंख्या"), "right"),
           col(L("Growth 2001–11 (%)", "वृद्धि 2001–11 (%)", "वाढ 2001–11 (%)"), "right"), col(L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), "right"), col(L("Density (/km²)", "घनत्व (/किमी²)", "घनता (/किमी²)"), "right")],
          [[L(en, hi, mr), pop, f"{g:.1f}", sr, den] for en, hi, mr, pop, g, sr, den in DIST_ROWS],
          "mh-sdb", SDB_DIST, period="2011",
          note=L("Maharashtra had 35 districts in 2011. Palghar was carved out of Thane in 2014, making 36. Former names are shown in brackets.",
                 "2011 में महाराष्ट्र में 35 ज़िले थे। 2014 में ठाणे से पालघर अलग हुआ, जिससे संख्या 36 हुई। पूर्व नाम कोष्ठक में दिए गए हैं।",
                 "2011 मध्ये महाराष्ट्रात 35 जिल्हे होते. 2014 मध्ये ठाण्यातून पालघर वेगळा झाल्याने संख्या 36 झाली. पूर्वीची नावे कंसात दिली आहेत.")),
    gaps("g", [
        (L("Urban agglomeration populations and city tiers", "नगरीय समूह जनसंख्या और शहर श्रेणी", "नागरी समूह लोकसंख्या व शहर श्रेणी"), "census", "Census 2011 UA tables; Ministry of Finance HRA classification."),
        (L("District explorer pages", "ज़िला एक्सप्लोरर पेज", "जिल्हा माहितीपाने"), "mh-gov", "Phase 3."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Cricket dominates popular sport, with Mumbai one of the most successful teams in domestic cricket and Wankhede Stadium a regular international venue. Traditional sports are strong too: kabaddi and kho-kho are played in schools across the State, and mallakhamb — gymnastics on a wooden pole or rope — is a Maharashtrian tradition. Kolhapur's talim (wrestling gyms) keep kushti alive.\n\nKhashaba Jadhav of Satara won India's first individual Olympic medal, a wrestling bronze at Helsinki in 1952. Swapnil Kusale of Kolhapur won bronze in 50 m rifle three positions at Paris 2024.",
        "लोकप्रिय खेलों में क्रिकेट सबसे आगे है; घरेलू क्रिकेट में मुंबई सबसे सफल टीमों में है और वानखेड़े स्टेडियम नियमित अंतरराष्ट्रीय मैदान है। पारंपरिक खेल भी मज़बूत हैं: कबड्डी और खो-खो राज्य भर के स्कूलों में खेले जाते हैं, और मल्लखंब — लकड़ी के खंभे या रस्सी पर जिम्नास्टिक — महाराष्ट्र की परंपरा है। कोल्हापुर की तालीमें (कुश्ती अखाड़े) कुश्ती को जीवित रखती हैं।\n\nसातारा के खाशाबा जाधव ने 1952 के हेलसिंकी ओलंपिक में कुश्ती में कांस्य जीतकर भारत का पहला व्यक्तिगत ओलंपिक पदक दिलाया। कोल्हापुर के स्वप्निल कुसाले ने पेरिस 2024 में 50 मीटर राइफ़ल थ्री पोज़ीशन में कांस्य जीता।",
        "लोकप्रिय खेळांत क्रिकेट आघाडीवर आहे; देशांतर्गत क्रिकेटमध्ये मुंबई सर्वांत यशस्वी संघांपैकी एक आहे आणि वानखेडे स्टेडियम नियमित आंतरराष्ट्रीय मैदान आहे. पारंपरिक खेळही बहरलेले आहेत: कबड्डी व खो-खो राज्यभरातील शाळांत खेळले जातात, आणि मल्लखांब — लाकडी खांबावर किंवा दोरावरील कसरत — ही महाराष्ट्राची परंपरा आहे. कोल्हापूरच्या तालमी कुस्तीची परंपरा जिवंत ठेवतात.\n\nसाताऱ्याचे खाशाबा जाधव यांनी 1952 च्या हेलसिंकी ऑलिंपिकमध्ये कुस्तीत कांस्यपदक जिंकून भारताला पहिले वैयक्तिक ऑलिंपिक पदक मिळवून दिले. कोल्हापूरच्या स्वप्नील कुसाळे यांनी पॅरिस 2024 मध्ये 50 मीटर रायफल थ्री पोझिशनमध्ये कांस्यपदक जिंकले."),
        conf="Editorial"),
    lst("venues", [
        item("wankhede", L("Wankhede Stadium, Mumbai", "वानखेड़े स्टेडियम, मुंबई", "वानखेडे स्टेडियम, मुंबई")),
        item("brabourne", L("Brabourne Stadium, Mumbai", "ब्रेबोर्न स्टेडियम, मुंबई", "ब्रेबॉर्न स्टेडियम, मुंबई")),
        item("dyp", L("DY Patil Stadium, Navi Mumbai", "डी. वाई. पाटिल स्टेडियम, नवी मुंबई", "डी. वाय. पाटील स्टेडियम, नवी मुंबई")),
        item("mca", L("MCA Stadium, Pune", "एमसीए स्टेडियम, पुणे", "एमसीए स्टेडियम, पुणे")),
        item("vca", L("VCA Stadium, Jamtha (Nagpur)", "वीसीए स्टेडियम, जामठा (नागपुर)", "व्हीसीए स्टेडियम, जामठा (नागपूर)")),
        item("balewadi", L("Shree Shiv Chhatrapati Sports Complex, Balewadi (Pune)", "श्री शिव छत्रपति क्रीड़ा संकुल, बालेवाड़ी (पुणे)", "श्री शिवछत्रपती क्रीडा संकुल, बालेवाडी (पुणे)")),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [
        (L("Officially declared State sport", "आधिकारिक राज्य खेल", "अधिकृत राज्य खेळ"), "mh-gov", "Confirm the Government Resolution."),
        (L("Sports academies and Khelo India centres", "खेल अकादमियाँ और खेलो इंडिया केंद्र", "क्रीडा प्रबोधिनी व खेलो इंडिया केंद्रे"), "mh-gov", "Department of Sports & Youth Services."),
    ]),
])

# ---------------- W. Personalities ----------------
def person(id, en, hi, mr, d_en, d_hi, d_mr, m_en, m_hi, m_mr):
    return item(id, L(en, hi, mr), detail=L(d_en, d_hi, d_mr), meta=L(m_en, m_hi, m_mr))
module(R, "personalities", [
    lst("people", [
        person("shivaji", "Chhatrapati Shivaji Maharaj", "छत्रपति शिवाजी महाराज", "छत्रपती शिवाजी महाराज", "Founder of the Maratha state, crowned at Raigad in 1674.", "मराठा राज्य के संस्थापक; 1674 में रायगढ़ में राज्याभिषेक।", "मराठा राज्याचे संस्थापक; 1674 मध्ये रायगडावर राज्याभिषेक.", "Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन"),
        person("dnyaneshwar", "Sant Dnyaneshwar", "संत ज्ञानेश्वर", "संत ज्ञानेश्वर", "13th-century saint-poet; author of the Dnyaneshwari.", "13वीं सदी के संत-कवि; ज्ञानेश्वरी के रचयिता।", "तेराव्या शतकातील संतकवी; ज्ञानेश्वरीचे कर्ते.", "Literature", "साहित्य", "साहित्य"),
        person("tukaram", "Sant Tukaram", "संत तुकाराम", "संत तुकाराम", "17th-century Varkari saint whose abhangs are sung widely today.", "17वीं सदी के वारकरी संत, जिनके अभंग आज भी गाए जाते हैं।", "सतराव्या शतकातील वारकरी संत; त्यांचे अभंग आजही घरोघरी गायले जातात.", "Literature", "साहित्य", "साहित्य"),
        person("jphule", "Jyotirao Phule", "ज्योतिराव फुले", "जोतीराव फुले", "Social reformer; founded the Satyashodhak Samaj in 1873.", "समाज सुधारक; 1873 में सत्यशोधक समाज की स्थापना की।", "समाजसुधारक; 1873 मध्ये सत्यशोधक समाजाची स्थापना.", "Social reform", "समाज सुधार", "समाजसुधारणा"),
        person("sphule", "Savitribai Phule", "सावित्रीबाई फुले", "सावित्रीबाई फुले", "Pioneer of girls' education; opened schools in Pune from 1848 with Jyotirao Phule.", "बालिका शिक्षा की अग्रदूत; 1848 से ज्योतिराव फुले के साथ पुणे में स्कूल खोले।", "स्त्रीशिक्षणाच्या प्रणेत्या; 1848 पासून जोतीराव फुले यांच्यासोबत पुण्यात मुलींच्या शाळा सुरू केल्या.", "Social reform", "समाज सुधार", "समाजसुधारणा"),
        person("ambedkar", "Dr B. R. Ambedkar", "डॉ. बी. आर. आंबेडकर", "डॉ. बाबासाहेब आंबेडकर", "Chairman of the Constitution's Drafting Committee; social reformer and jurist.", "संविधान की प्रारूप समिति के अध्यक्ष; समाज सुधारक और विधिवेत्ता।", "राज्यघटनेच्या मसुदा समितीचे अध्यक्ष; समाजसुधारक आणि कायदेतज्ज्ञ.", "Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन"),
        person("tilak", "Bal Gangadhar Tilak", "बाल गंगाधर तिलक", "बाळ गंगाधर टिळक", "Freedom fighter and editor of Kesari; popularised public Ganeshotsav.", "स्वतंत्रता सेनानी और केसरी के संपादक; सार्वजनिक गणेशोत्सव को लोकप्रिय बनाया।", "स्वातंत्र्यसैनिक आणि केसरीचे संपादक; सार्वजनिक गणेशोत्सवाला लोकप्रियता दिली.", "Freedom movement", "स्वतंत्रता आंदोलन", "स्वातंत्र्यलढा"),
        person("gokhale", "Gopal Krishna Gokhale", "गोपाल कृष्ण गोखले", "गोपाळ कृष्ण गोखले", "Moderate leader of the Congress; founded the Servants of India Society.", "कांग्रेस के नरमपंथी नेता; सर्वेंट्स ऑफ़ इंडिया सोसाइटी के संस्थापक।", "काँग्रेसचे मवाळ नेते; भारत सेवक समाजाचे संस्थापक.", "Freedom movement", "स्वतंत्रता आंदोलन", "स्वातंत्र्यलढा"),
        person("karve", "Dhondo Keshav Karve", "धोंडो केशव कर्वे", "धोंडो केशव कर्वे", "Pioneer of women's education; founded what became SNDT Women's University. Bharat Ratna 1958.", "महिला शिक्षा के अग्रदूत; एसएनडीटी महिला विश्वविद्यालय की नींव रखी। भारत रत्न 1958।", "स्त्रीशिक्षणाचे प्रणेते; एसएनडीटी महिला विद्यापीठाचे संस्थापक. भारतरत्न 1958.", "Social reform", "समाज सुधार", "समाजसुधारणा"),
        person("phalke", "Dadasaheb Phalke", "दादासाहेब फाल्के", "दादासाहेब फाळके", "Made Raja Harishchandra (1913), regarded as India's first feature film.", "राजा हरिश्चंद्र (1913) के निर्माता, जिसे भारत की पहली फ़ीचर फ़िल्म माना जाता है।", "‘राजा हरिश्चंद्र’ (1913) चे निर्माते; हा भारतातील पहिला चित्रपट मानला जातो.", "Arts", "कला", "कला"),
        person("lata", "Lata Mangeshkar", "लता मंगेशकर", "लता मंगेशकर", "Playback singer whose career spanned seven decades. Bharat Ratna 2001.", "पार्श्वगायिका, जिनका करियर सात दशकों तक चला। भारत रत्न 2001।", "सात दशके गाजलेल्या पार्श्वगायिका. भारतरत्न 2001.", "Arts", "कला", "कला"),
        person("pula", "P. L. Deshpande", "पु. ल. देशपांडे", "पु. ल. देशपांडे", "Humorist, writer and performer; one of Marathi's best-loved authors.", "हास्य लेखक, लेखक और कलाकार; मराठी के सबसे प्रिय लेखकों में।", "विनोदी लेखक, साहित्यिक आणि कलावंत; मराठीतील लाडके लेखक.", "Literature", "साहित्य", "साहित्य"),
        person("sachin", "Sachin Tendulkar", "सचिन तेंदुलकर", "सचिन तेंडुलकर", "Cricketer; leading run-scorer in Test and ODI history. Bharat Ratna 2014.", "क्रिकेटर; टेस्ट और वनडे इतिहास में सबसे अधिक रन। भारत रत्न 2014।", "क्रिकेटपटू; कसोटी व एकदिवसीय सामन्यांत सर्वाधिक धावा. भारतरत्न 2014.", "Sports", "खेल", "क्रीडा"),
        person("khashaba", "Khashaba Jadhav", "खाशाबा जाधव", "खाशाबा जाधव", "Wrestler; India's first individual Olympic medallist (1952).", "पहलवान; भारत के पहले व्यक्तिगत ओलंपिक पदक विजेता (1952)।", "कुस्तीपटू; भारताचे पहिले वैयक्तिक ऑलिंपिक पदकविजेते (1952).", "Sports", "खेल", "क्रीडा"),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Maharashtra is one of India's biggest destinations for internal migration. For more than a century, people have moved to Mumbai, Thane and Pune for work from across the State and from Uttar Pradesh, Bihar, Karnataka, Gujarat and other States, making the Mumbai region one of the most diverse in India. Within the State, seasonal migration from drought-prone districts to sugarcane fields and cities is common.\n\nMarathi-speaking communities have long histories outside the State — in Indore, Gwalior, Vadodara and Thanjavur, often linked to Maratha-era settlement — and there are sizeable Maharashtrian communities in the Gulf, North America and the United Kingdom.",
        "महाराष्ट्र देश में आंतरिक प्रवास के सबसे बड़े गंतव्यों में है। सौ से अधिक वर्षों से राज्य भर से तथा उत्तर प्रदेश, बिहार, कर्नाटक, गुजरात और अन्य राज्यों से लोग काम के लिए मुंबई, ठाणे और पुणे आते रहे हैं, जिससे मुंबई क्षेत्र भारत के सबसे विविध क्षेत्रों में है। राज्य के भीतर सूखाग्रस्त ज़िलों से गन्ने के खेतों और शहरों की ओर मौसमी प्रवास आम है।\n\nमराठी भाषी समुदायों का राज्य के बाहर लंबा इतिहास है — इंदौर, ग्वालियर, वडोदरा और तंजावुर में, जो अक्सर मराठा काल की बसावट से जुड़ा है — और खाड़ी देशों, उत्तरी अमेरिका और ब्रिटेन में भी बड़े महाराष्ट्रीय समुदाय हैं।",
        "महाराष्ट्र हे देशांतर्गत स्थलांतराचे सर्वांत मोठे केंद्र आहे. शंभरहून अधिक वर्षे राज्यभरातून तसेच उत्तर प्रदेश, बिहार, कर्नाटक, गुजरात आणि इतर राज्यांतून लोक कामासाठी मुंबई, ठाणे आणि पुण्यात येत आहेत, त्यामुळे मुंबई परिसर भारतातील सर्वांत वैविध्यपूर्ण प्रदेशांपैकी एक आहे. राज्यांतर्गत दुष्काळप्रवण जिल्ह्यांतून ऊसतोडणीसाठी आणि शहरांकडे हंगामी स्थलांतर सामान्य आहे.\n\nमराठी भाषक समुदायांचा राज्याबाहेरही दीर्घ इतिहास आहे — इंदूर, ग्वाल्हेर, बडोदा आणि तंजावर येथे, जो अनेकदा मराठाकालीन वसाहतींशी जोडलेला आहे — आणि आखाती देश, उत्तर अमेरिका व ब्रिटनमध्येही मोठे महाराष्ट्रीय समुदाय आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("In- and out-migration figures", "आप्रवास और उत्प्रवास के आँकड़े", "स्थलांतर (आवक-जावक) आकडेवारी"), "census", "Census 2011 D-series migration tables."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        item("portal", L("Government of Maharashtra portal", "महाराष्ट्र सरकार पोर्टल", "महाराष्ट्र शासन संकेतस्थळ"), url="https://www.maharashtra.gov.in", src="mh-gov"),
        item("aaple", L("Aaple Sarkar — online public services", "आपले सरकार — ऑनलाइन नागरिक सेवाएँ", "आपले सरकार — ऑनलाइन नागरी सेवा"), url="https://aaplesarkar.mahaonline.gov.in", src="mh-gov"),
        item("rti", L("RTI Online, Maharashtra", "आरटीआई ऑनलाइन, महाराष्ट्र", "माहितीचा अधिकार ऑनलाइन, महाराष्ट्र"), url="https://rtionline.maharashtra.gov.in", src="mh-gov"),
        item("lokbhavan", L("Lok Bhavan (Governor's office)", "लोक भवन (राज्यपाल कार्यालय)", "लोकभवन (राज्यपाल कार्यालय)"), url="https://lokbhavan.maharashtra.gov.in", src="mh-lokbhavan"),
        item("tourism", L("Maharashtra Tourism", "महाराष्ट्र पर्यटन", "महाराष्ट्र पर्यटन"), url="https://maharashtratourism.gov.in", src="mh-tourism"),
        item("consumer", L("National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन"), url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Mumbai and Thane", "मुंबई और ठाणे", "मुंबई व ठाणे"), "022"], [L("Pune", "पुणे", "पुणे"), "020"], [L("Nagpur", "नागपुर", "नागपूर"), "0712"],
           [L("Nashik", "नासिक", "नाशिक"), "0253"], [L("Chhatrapati Sambhajinagar", "छत्रपति संभाजीनगर", "छत्रपती संभाजीनगर"), "0240"],
           [L("Kolhapur", "कोल्हापुर", "कोल्हापूर"), "0231"], [L("Solapur", "सोलापुर", "सोलापूर"), "0217"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जानी है।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळायची आहे.")),
    gaps("g", [
        (L("Verified local business directory (MSMEs, co-operatives, FPOs, artisan clusters)", "सत्यापित स्थानीय व्यवसाय निर्देशिका (एमएसएमई, सहकारी, एफ़पीओ, कारीगर क्लस्टर)", "पडताळलेली स्थानिक व्यवसाय सूची (एमएसएमई, सहकारी संस्था, एफपीओ, कारागीर समूह)"), "mh-gov", "Udyam registration data, Registrar of Co-operative Societies, SFAC FPO list."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, en, hi, mr, url, src):
    return item(id, L(en, hi, mr), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("gsdp", "Maharashtra has the largest GSDP of any Indian State (FY2024-25, MoSPI).", "महाराष्ट्र का जीएसडीपी देश के सभी राज्यों में सबसे अधिक है (वित्त वर्ष 2024-25, मोस्पी)।", "महाराष्ट्राचे जीएसडीपी देशातील सर्व राज्यांत सर्वाधिक आहे (आ.व. 2024-25, मोस्पी).", MOSPI, "mospi"),
        triv("whs", "It has seven UNESCO World Heritage properties, including 11 of the 12 forts of the Maratha Military Landscapes (2025).", "यहाँ सात यूनेस्को विश्व धरोहर स्थल हैं, जिनमें मराठा सैन्य परिदृश्य (2025) के 12 में से 11 क़िले शामिल हैं।", "येथे युनेस्कोची सात जागतिक वारसा स्थळे आहेत, ज्यात मराठा लष्करी भूप्रदेशातील (2025) 12 पैकी 11 किल्ले आहेत.", "https://whc.unesco.org/en/list/1739", "unesco-whc"),
        triv("gi", "Its 55 registered GIs range from Alphonso mangoes to Miraj sitars.", "इसके 55 पंजीकृत जीआई में अल्फांसो आम से लेकर मिरज के सितार तक शामिल हैं।", "हापूस आंब्यापासून मिरजेच्या सतारीपर्यंत येथे 55 नोंदणीकृत जीआय आहेत.", GI_PDF, "gi-registry"),
        triv("lonar", "Lonar Lake fills a meteorite impact crater and is a Ramsar wetland (2020).", "लोणार झील उल्कापिंड से बने गड्ढे में है और रामसर आर्द्रभूमि (2020) है।", "लोणार सरोवर उल्कापाताने बनलेल्या विवरात असून ते रामसर पाणथळ स्थळ (2020) आहे.", RAMSAR, "indian-wetlands"),
        triv("rail", "India's first passenger train ran from Bori Bunder (Mumbai) to Thane on 16 April 1853.", "भारत की पहली यात्री रेलगाड़ी 16 अप्रैल 1853 को बोरी बंदर (मुंबई) से ठाणे तक चली।", "भारतातील पहिली प्रवासी रेल्वे 16 एप्रिल 1853 रोजी बोरीबंदर (मुंबई) ते ठाणे धावली.", "https://indianrailways.gov.in", "railways"),
        triv("tarapur", "Tarapur, commissioned in 1969, was India's first nuclear power station.", "1969 में शुरू हुआ तारापुर भारत का पहला परमाणु बिजलीघर था।", "1969 मध्ये सुरू झालेले तारापूर हे भारतातील पहिले अणुऊर्जा केंद्र होते.", "https://www.npcil.nic.in", "npcil"),
        triv("classical", "Marathi was declared a classical language in October 2024.", "अक्टूबर 2024 में मराठी को शास्त्रीय भाषा घोषित किया गया।", "ऑक्टोबर 2024 मध्ये मराठीला अभिजात भाषेचा दर्जा मिळाला.", "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2061660&reg=48&lang=2", "pib"),
        triv("olympic", "Khashaba Jadhav won India's first individual Olympic medal, in wrestling, at Helsinki 1952.", "खाशाबा जाधव ने 1952 हेलसिंकी में कुश्ती में भारत का पहला व्यक्तिगत ओलंपिक पदक जीता।", "खाशाबा जाधव यांनी 1952 च्या हेलसिंकी ऑलिंपिकमध्ये कुस्तीत भारताचे पहिले वैयक्तिक पदक जिंकले.", None, None),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("mod3 ok")
