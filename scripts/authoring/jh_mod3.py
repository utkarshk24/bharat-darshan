"""Jharkhand modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-JH"
jh = read("regions/IN-JH.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Nearly 30% of Jharkhand — 29.8% in ISFR 2023 — is under forest, mostly moist and dry deciduous sal forest. Saranda in West Singhbhum is one of Asia's largest sal forests. Palamau Tiger Reserve, with Betla National Park at its heart, was among the first nine tiger reserves created under Project Tiger in 1973. Dalma Wildlife Sanctuary near Jamshedpur is known for its elephants, and Hazaribagh, Koderma and Topchanchi are other protected areas. Elephants range widely across the plateau, and conflict between people and elephants is a serious issue.\n\nUdhwa Lake Bird Sanctuary in Sahibganj, an oxbow wetland on the Ganga floodplain, is the State's only Ramsar site.",
        "झारखंड का लगभग 30% भाग — आईएसएफ़आर 2023 में 29.8% — वनों से ढका है, जो अधिकतर नम और शुष्क पर्णपाती साल वन हैं। पश्चिमी सिंहभूम का सारंडा एशिया के सबसे बड़े साल वनों में से एक है। बेतला राष्ट्रीय उद्यान को केंद्र में रखने वाला पलामू बाघ अभयारण्य 1973 में प्रोजेक्ट टाइगर के तहत बने पहले नौ बाघ अभयारण्यों में था। जमशेदपुर के पास दलमा वन्यजीव अभयारण्य अपने हाथियों के लिए जाना जाता है, और हज़ारीबाग, कोडरमा और तोपचांची अन्य संरक्षित क्षेत्र हैं। हाथी पूरे पठार पर दूर-दूर तक घूमते हैं, और मनुष्य–हाथी संघर्ष एक गंभीर समस्या है।\n\nगंगा के बाढ़ मैदान में गोखुर आर्द्रभूमि, साहिबगंज का उधवा झील पक्षी अभयारण्य राज्य का एकमात्र रामसर स्थल है।",
        "झारखंडचा सुमारे 30% भाग — आयएसएफआर 2023 नुसार 29.8% — वनाच्छादित आहे, बहुतांश आर्द्र व शुष्क पानगळीची साल वने. पश्चिम सिंहभूममधील सारंडा हे आशियातील सर्वांत मोठ्या साल वनांपैकी एक आहे. बेतला राष्ट्रीय उद्यान केंद्रस्थानी असलेला पलामू व्याघ्र प्रकल्प 1973 मध्ये प्रोजेक्ट टायगरअंतर्गत निर्माण झालेल्या पहिल्या नऊ व्याघ्र प्रकल्पांपैकी होता. जमशेदपूरजवळील दलमा वन्यजीव अभयारण्य हत्तींसाठी ओळखले जाते, आणि हजारीबाग, कोडरमा व तोपचांची ही इतर संरक्षित क्षेत्रे आहेत. हत्ती संपूर्ण पठारावर दूरवर फिरतात, आणि माणूस–हत्ती संघर्ष ही गंभीर समस्या आहे.\n\nगंगेच्या पूरमैदानातील गोखुर पाणथळ, साहिबगंजचे उधवा सरोवर पक्षी अभयारण्य हे राज्यातील एकमेव रामसर स्थळ आहे."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(23765.78, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(23706.97, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), jh["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(1, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: Udhwa Lake Bird Sanctuary, 935.5 ha; designation date printed as 08-01-2024."), "number"),
    ]),
    lst("protected", [
        it3("palamau", "Palamau Tiger Reserve (Betla National Park)", "पलामू बाघ अभयारण्य (बेतला राष्ट्रीय उद्यान)", "पलामू व्याघ्र प्रकल्प (बेतला राष्ट्रीय उद्यान)", m=("Latehar; Project Tiger 1973", "लातेहार; प्रोजेक्ट टाइगर 1973", "लातेहार; प्रोजेक्ट टायगर 1973")),
        it3("dalma", "Dalma Wildlife Sanctuary", "दलमा वन्यजीव अभयारण्य", "दलमा वन्यजीव अभयारण्य", m=("Elephants; near Jamshedpur", "हाथी; जमशेदपुर के पास", "हत्ती; जमशेदपूरजवळ")),
        it3("hazaribagh", "Hazaribagh Wildlife Sanctuary", "हज़ारीबाग वन्यजीव अभयारण्य", "हजारीबाग वन्यजीव अभयारण्य", m=("Hazaribagh", "हज़ारीबाग", "हजारीबाग")),
        it3("udhwa", "Udhwa Lake Bird Sanctuary", "उधवा झील पक्षी अभयारण्य", "उधवा सरोवर पक्षी अभयारण्य", m=("Ramsar site; Sahibganj", "रामसर स्थल; साहिबगंज", "रामसर स्थळ; साहिबगंज")),
        it3("saranda", "Saranda forest", "सारंडा वन", "सारंडा वन", m=("West Singhbhum; sal", "पश्चिमी सिंहभूम; साल", "पश्चिम सिंहभूम; साल")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("elephant", "Asian elephant (State animal)", "हाथी (राज्य पशु)", "हत्ती (राज्यप्राणी)"), it3("tiger", "Tiger", "बाघ", "वाघ"),
        it3("gaur", "Gaur", "गौर", "गवा"), it3("wolf", "Indian wolf", "भारतीय भेड़िया", "भारतीय लांडगा"),
        it3("koel", "Asian koel (State bird)", "कोयल (राज्य पक्षी)", "कोकिळा (राज्यपक्षी)"), it3("sloth", "Sloth bear", "भालू", "अस्वल"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger estimate (Palamau)", "बाघों का अनुमान (पलामू)", "वाघांचा अंदाज (पलामू)"), "ntca", "NTCA All India Tiger Estimation."),
        (L("Elephant population and conflict deaths", "हाथियों की संख्या और संघर्ष में मौतें", "हत्तींची संख्या व संघर्षातील मृत्यू"), "moefcc", "Project Elephant / Lok Sabha answers."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Jharkhand receives good monsoon rain, but its hard rocks hold little groundwater and its rivers run fast off the plateau, so water scarcity in summer is common. The Damodar Valley Corporation, set up in 1948 as independent India's first multipurpose river valley project, built dams at Tilaiya, Konar, Maithon and Panchet for flood control, power and irrigation; Getalsud near Ranchi and Chandil on the Subarnarekha are other major reservoirs. Mining has polluted the Damodar and other rivers, and fluoride and arsenic affect groundwater in parts of Palamu, Garhwa and Sahibganj. Small check dams and ponds are widely used to store monsoon water.",
        "झारखंड में अच्छी मानसूनी वर्षा होती है, लेकिन इसकी कठोर चट्टानों में भूजल कम रहता है और नदियाँ पठार से तेज़ी से बह जाती हैं, इसलिए गर्मियों में पानी की कमी आम है। 1948 में स्वतंत्र भारत की पहली बहुउद्देशीय नदी घाटी परियोजना के रूप में बने दामोदर घाटी निगम ने बाढ़ नियंत्रण, बिजली और सिंचाई के लिए तिलैया, कोनार, मैथन और पंचेत में बाँध बनाए; रांची के पास गेतलसूद और सुवर्णरेखा पर चांडिल अन्य बड़े जलाशय हैं। खनन ने दामोदर और अन्य नदियों को प्रदूषित किया है, और पलामू, गढ़वा और साहिबगंज के कुछ भागों के भूजल में फ़्लोराइड और आर्सेनिक है। मानसूनी पानी जमा करने के लिए छोटे चेक डैम और तालाब व्यापक रूप से उपयोग होते हैं।",
        "झारखंडमध्ये चांगला मान्सूनी पाऊस पडतो, पण त्याच्या कठीण खडकांत भूजल कमी साठते आणि नद्या पठारावरून वेगाने वाहून जातात, त्यामुळे उन्हाळ्यात पाणीटंचाई सामान्य आहे. 1948 मध्ये स्वतंत्र भारताचा पहिला बहुउद्देशीय नदी खोरे प्रकल्प म्हणून स्थापन झालेल्या दामोदर खोरे महामंडळाने पूरनियंत्रण, वीज व सिंचनासाठी तिलैया, कोनार, मैथन व पंचेत येथे धरणे बांधली; रांचीजवळील गेतलसूद व सुवर्णरेखेवरील चांडिल हे इतर मोठे जलाशय आहेत. खाणकामामुळे दामोदर व इतर नद्या प्रदूषित झाल्या आहेत, आणि पलामू, गढवा व साहिबगंजच्या काही भागांतील भूजलात फ्लोराइड व आर्सेनिक आहे. पावसाचे पाणी साठवण्यासाठी लहान बंधारे व तलाव मोठ्या प्रमाणावर वापरले जातात."),
        conf="Editorial"),
    gaps("g", [
        (L("Irrigated area", "सिंचित क्षेत्र", "सिंचित क्षेत्र"), "india-gov", "Jharkhand Economic Survey / Water Resources Department."),
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Fluoride- and arsenic-affected habitations", "फ़्लोराइड और आर्सेनिक प्रभावित बस्तियाँ", "फ्लोराइड व आर्सेनिकबाधित वस्त्या"), "india-gov", "Jal Jeevan Mission water-quality data."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Lightning is one of the biggest natural killers in Jharkhand, especially during the pre-monsoon and monsoon months, and heatwaves affect the lower districts in May and June. Drought recurs in Palamu and other western districts. In the Jharia coalfield, underground fires that have burned for over a century and land subsidence threaten settlements, and a master plan for relocating residents is under way. Elephant movements cause deaths and crop losses in forest-fringe villages.\n\nVisitors should check weather warnings before visiting waterfalls in the monsoon, when water levels rise suddenly, and follow crowd advisories at the Shravani Mela in Deoghar.",
        "आकाशीय बिजली झारखंड में सबसे अधिक जान लेने वाली प्राकृतिक आपदाओं में से है, विशेषकर मानसून-पूर्व और मानसून के महीनों में, और मई-जून में निचले ज़िलों में लू चलती है। पलामू और अन्य पश्चिमी ज़िलों में सूखा बार-बार पड़ता है। झरिया कोयला क्षेत्र में एक सदी से अधिक समय से जल रही भूमिगत आग और भू-धँसाव बस्तियों के लिए ख़तरा हैं, और निवासियों के पुनर्वास के लिए एक मास्टर प्लान चल रहा है। हाथियों की आवाजाही से वन-सीमा के गाँवों में मौतें और फ़सल नुकसान होते हैं।\n\nपर्यटकों को मानसून में झरनों पर जाने से पहले मौसम चेतावनियाँ देखनी चाहिए, जब पानी अचानक बढ़ जाता है, और देवघर के श्रावणी मेले में भीड़ संबंधी सलाह माननी चाहिए।",
        "वीज कोसळणे हे झारखंडमधील सर्वाधिक बळी घेणाऱ्या नैसर्गिक आपत्तींपैकी एक आहे, विशेषतः मान्सूनपूर्व व मान्सूनच्या महिन्यांत, आणि मे-जूनमध्ये खालच्या जिल्ह्यांत उष्णतेची लाट येते. पलामू व इतर पश्चिमेकडील जिल्ह्यांत वारंवार दुष्काळ पडतो. झरिया कोळसा क्षेत्रात शतकाहून अधिक काळ धुमसणारी भूमिगत आग व जमीन खचणे वस्त्यांसाठी धोकादायक आहे, आणि रहिवाशांच्या पुनर्वसनासाठी बृहत् आराखडा राबवला जात आहे. हत्तींच्या वावरामुळे जंगलालगतच्या गावांत मृत्यू व पीकहानी होते.\n\nपर्यटकांनी पावसाळ्यात धबधब्यांना भेट देण्यापूर्वी हवामान इशारे तपासावेत, जेव्हा पाण्याची पातळी अचानक वाढते, आणि देवघरच्या श्रावणी मेळ्यात गर्दीविषयक सूचना पाळाव्यात."),
        conf="Editorial"),
    emergency_table(("Jharkhand", "झारखंड", "झारखंड")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official JSDMA address."),
        (L("Lightning deaths by year", "वर्षवार आकाशीय बिजली से मौतें", "वर्षनिहाय वीज कोसळून मृत्यू"), "india-gov", "NCRB Accidental Deaths and Suicides in India."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Jharkhand has one registered Geographical Indication in the GI Registry's list as on 31 December 2025: Sohrai–Khovar painting, filed in 2019. Sohrai is painted by women on the mud walls of houses at the harvest festival, and Khovar for weddings, using natural earth colours, in villages of Hazaribagh district. Other crafts of the State — Paitkar painting, Dokra metal casting and tussar silk — are not registered GIs on this list.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में झारखंड का एक पंजीकृत भौगोलिक संकेतक है: 2019 में दायर सोहराय–खोवर चित्रकला। हज़ारीबाग ज़िले के गाँवों में महिलाएँ फ़सल उत्सव पर सोहराय और विवाहों के लिए खोवर चित्र प्राकृतिक मिट्टी के रंगों से घरों की कच्ची दीवारों पर बनाती हैं। राज्य के अन्य शिल्प — पैटकर चित्रकला, ढोकरा धातु ढलाई और तसर रेशम — इस सूची में पंजीकृत जीआई नहीं हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत झारखंडचे एक नोंदणीकृत भौगोलिक मानांकन आहे: 2019 मध्ये दाखल झालेली सोहराय–खोवर चित्रकला. हजारीबाग जिल्ह्यातील गावांत स्त्रिया सुगीच्या सणाला सोहराय व लग्नांसाठी खोवर चित्रे नैसर्गिक मातीच्या रंगांनी घरांच्या मातीच्या भिंतींवर काढतात. राज्यातील इतर हस्तकला — पैटकर चित्रकला, ढोकरा धातू ओतकाम व टसर रेशीम — या यादीत नोंदणीकृत जीआय नाहीत."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Pending GI applications from Jharkhand", "झारखंड के लंबित जीआई आवेदन", "झारखंडचे प्रलंबित जीआय अर्ज"), "gi-registry", "GI Registry application status search."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Ranchi is known as the 'city of waterfalls': Hundru, Dassam, Jonha and Hirni falls are within easy reach, and Patratu valley's winding road and lake are popular. Netarhat, the 'queen of Chota Nagpur', is famed for its sunrises and sunsets, and nearby Lodh falls is the State's highest waterfall. Betla National Park offers jungle drives and the ruins of the Palamu forts. Pilgrims visit the Baidyanath jyotirlinga at Deoghar, the Jain shrines of Shikharji on Parasnath hill, the Chhinnamasta temple at Rajrappa and the Maluti temples. Jamshedpur's Jubilee Park and Dimna lake are city attractions.",
        "रांची को 'झरनों का शहर' कहा जाता है: हुंडरू, दशम, जोन्हा और हिरनी जलप्रपात आसानी से पहुँचे जा सकते हैं, और पतरातू घाटी की घुमावदार सड़क और झील लोकप्रिय हैं। 'छोटा नागपुर की रानी' नेतरहाट अपने सूर्योदय और सूर्यास्त के लिए प्रसिद्ध है, और पास का लोध जलप्रपात राज्य का सबसे ऊँचा झरना है। बेतला राष्ट्रीय उद्यान में जंगल सफ़ारी और पलामू क़िलों के खंडहर हैं। तीर्थयात्री देवघर के बैद्यनाथ ज्योतिर्लिंग, पारसनाथ पहाड़ी पर शिखरजी के जैन तीर्थ, रजरप्पा के छिन्नमस्तिका मंदिर और मलूटी मंदिरों में जाते हैं। जमशेदपुर का जुबली पार्क और डिमना झील शहर के आकर्षण हैं।",
        "रांचीला 'धबधब्यांचे शहर' म्हणतात: हुंडरू, दशम, जोन्हा व हिरनी धबधबे सहज गाठता येतात, आणि पतरातू खोऱ्याचा वळणदार रस्ता व सरोवर लोकप्रिय आहेत. 'छोटा नागपूरची राणी' नेतरहाट सूर्योदय व सूर्यास्तासाठी प्रसिद्ध आहे, आणि जवळचा लोध धबधबा हा राज्यातील सर्वांत उंच धबधबा आहे. बेतला राष्ट्रीय उद्यानात जंगल सफारी व पलामू किल्ल्यांचे अवशेष आहेत. यात्रेकरू देवघरचे बैद्यनाथ ज्योतिर्लिंग, पारसनाथ टेकडीवरील शिखरजीची जैन तीर्थे, रजरप्पाचे छिन्नमस्ता मंदिर व मलूटीची मंदिरे पाहायला जातात. जमशेदपूरचे ज्युबिली पार्क व डिमना सरोवर ही शहरातील आकर्षणे आहेत."),
        conf="Editorial"),
    lst("places", [
        it3("ranchi", "Ranchi waterfalls", "रांची के झरने", "रांचीचे धबधबे", m=("Hundru, Dassam, Jonha", "हुंडरू, दशम, जोन्हा", "हुंडरू, दशम, जोन्हा")),
        it3("netarhat", "Netarhat", "नेतरहाट", "नेतरहाट", m=("Hill station; Lodh falls", "पहाड़ी स्थल; लोध जलप्रपात", "थंड हवेचे ठिकाण; लोध धबधबा")),
        it3("betla", "Betla National Park", "बेतला राष्ट्रीय उद्यान", "बेतला राष्ट्रीय उद्यान", m=("Wildlife; Palamu forts", "वन्यजीव; पलामू क़िले", "वन्यजीव; पलामू किल्ले")),
        it3("deoghar", "Deoghar", "देवघर", "देवघर", m=("Baidyanath jyotirlinga", "बैद्यनाथ ज्योतिर्लिंग", "बैद्यनाथ ज्योतिर्लिंग")),
        it3("parasnath", "Parasnath (Shikharji)", "पारसनाथ (शिखरजी)", "पारसनाथ (शिखरजी)", m=("Jain pilgrimage", "जैन तीर्थ", "जैन तीर्थ")),
        it3("jamshedpur", "Jamshedpur", "जमशेदपुर", "जमशेदपूर", m=("Jubilee Park; Dalma", "जुबली पार्क; दलमा", "ज्युबिली पार्क; दलमा")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Ranchi: Hundru, Dassam and Jonha falls, Patratu valley and Rock Garden.", "रांची: हुंडरू, दशम और जोन्हा जलप्रपात, पतरातू घाटी और रॉक गार्डन।", "रांची: हुंडरू, दशम व जोन्हा धबधबे, पतरातू खोरे व रॉक गार्डन.")),
        it3("d4", "4 days", "4 दिन", "4 दिवस", d=("Ranchi, Netarhat and Betla National Park.", "रांची, नेतरहाट और बेतला राष्ट्रीय उद्यान।", "रांची, नेतरहाट व बेतला राष्ट्रीय उद्यान.")),
        it3("d3p", "3 days (pilgrimage)", "3 दिन (तीर्थयात्रा)", "3 दिवस (तीर्थयात्रा)", d=("Deoghar, Parasnath and Rajrappa.", "देवघर, पारसनाथ और रजरप्पा।", "देवघर, पारसनाथ व रजरप्पा.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("jt", "Jharkhand Tourism (official)", "झारखंड पर्यटन (आधिकारिक)", "झारखंड पर्यटन (अधिकृत)", url="https://tourism.jharkhand.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Bokaro", "बोकारो", "बोकारो"), ("Chatra", "चतरा", "चतरा"), ("Deoghar", "देवघर", "देवघर"), ("Dhanbad", "धनबाद", "धनबाद"), ("Dumka", "दुमका", "दुमका"),
    ("East Singhbhum", "पूर्वी सिंहभूम", "पूर्व सिंहभूम"), ("Garhwa", "गढ़वा", "गढवा"), ("Giridih", "गिरिडीह", "गिरिडीह"), ("Godda", "गोड्डा", "गोड्डा"), ("Gumla", "गुमला", "गुमला"),
    ("Hazaribagh", "हज़ारीबाग", "हजारीबाग"), ("Jamtara", "जामताड़ा", "जामताडा"), ("Khunti", "खूँटी", "खुंटी"), ("Koderma", "कोडरमा", "कोडरमा"), ("Latehar", "लातेहार", "लातेहार"),
    ("Lohardaga", "लोहरदगा", "लोहरदगा"), ("Pakur", "पाकुड़", "पाकुड"), ("Palamu", "पलामू", "पलामू"), ("Ramgarh", "रामगढ़", "रामगड"), ("Ranchi", "रांची", "रांची"),
    ("Sahibganj", "साहिबगंज", "साहिबगंज"), ("Seraikela Kharsawan", "सरायकेला खरसावाँ", "सरायकेला खरसावां"), ("Simdega", "सिमडेगा", "सिमडेगा"), ("West Singhbhum", "पश्चिमी सिंहभूम", "पश्चिम सिंहभूम"),
]
assert len(DISTRICTS) == 24, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("ranchi", ("Ranchi", "रांची", "रांची"), ("State capital on the plateau; city of waterfalls.", "पठार पर राज्य की राजधानी; झरनों का शहर।", "पठारावरील राज्याची राजधानी; धबधब्यांचे शहर."), ("Capital", "राजधानी", "राजधानी")),
        city("jamshedpur", ("Jamshedpur", "जमशेदपुर", "जमशेदपूर"), ("Planned steel city founded around the Tata works.", "टाटा कारख़ाने के इर्द-गिर्द बसा नियोजित इस्पात नगर।", "टाटा कारखान्याभोवती वसलेले नियोजित पोलादनगर."), ("Industry", "उद्योग", "उद्योग")),
        city("dhanbad", ("Dhanbad", "धनबाद", "धनबाद"), ("Coal capital of India; IIT (ISM).", "भारत की कोयला राजधानी; आईआईटी (आईएसएम)।", "भारताची कोळसा राजधानी; आयआयटी (आयएसएम)."), ("Mining", "खनन", "खाणकाम")),
        city("bokaro", ("Bokaro Steel City", "बोकारो स्टील सिटी", "बोकारो स्टील सिटी"), ("Township of SAIL's Bokaro Steel Plant.", "सेल के बोकारो इस्पात संयंत्र की बस्ती।", "सेलच्या बोकारो पोलाद कारखान्याची वसाहत."), ("Industry", "उद्योग", "उद्योग")),
        city("deoghar", ("Deoghar", "देवघर", "देवघर"), ("Temple town of Baidyanath; AIIMS and airport.", "बैद्यनाथ का मंदिर नगर; एम्स और हवाई अड्डा।", "बैद्यनाथाचे मंदिरनगर; एम्स व विमानतळ."), ("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        city("hazaribagh", ("Hazaribagh", "हज़ारीबाग", "हजारीबाग"), ("Plateau town; Sohrai–Khovar painting.", "पठारी नगर; सोहराय–खोवर चित्रकला।", "पठारावरील शहर; सोहराय–खोवर चित्रकला."), ("Culture", "संस्कृति", "संस्कृती")),
        city("dumka", ("Dumka", "दुमका", "दुमका"), ("Sub-capital and centre of Santhal Pargana.", "उपराजधानी और संथाल परगना का केंद्र।", "उपराजधानी व संथाल परगण्याचे केंद्र."), ("Sub-capital", "उपराजधानी", "उपराजधानी")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 24 districts (alphabetical)", "24 ज़िले (वर्णानुक्रम)", "24 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Official district list (State notification)", "आधिकारिक ज़िला सूची (राज्य अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य अधिसूचना)"), "india-gov", "Link the State's list of districts."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Jharkhand punches above its weight in sport. Jaipal Singh Munda captained India to its first Olympic hockey gold in 1928, and the tribal districts of Simdega, Khunti and Gumla continue to produce national hockey players, including women's team stars such as Salima Tete and Nikki Pradhan. Archer Deepika Kumari, from Ranchi, has been world number one, and the Tata Archery Academy in Jamshedpur trains many champions. M. S. Dhoni, who led India to the 2007 T20 and 2011 50-over World Cup titles, grew up in Ranchi, where the JSCA International Stadium hosts international cricket. Jamshedpur is also a football centre, home to the Tata Football Academy and the JRD Tata Sports Complex.",
        "झारखंड खेलों में अपने आकार से बढ़कर प्रदर्शन करता है। जयपाल सिंह मुंडा ने 1928 में भारत को पहला ओलंपिक हॉकी स्वर्ण दिलाने वाली टीम की कप्तानी की, और सिमडेगा, खूँटी और गुमला के जनजातीय ज़िले सलीमा टेटे और निक्की प्रधान जैसी महिला टीम की सितारों सहित राष्ट्रीय हॉकी खिलाड़ी देते रहे हैं। रांची की तीरंदाज़ दीपिका कुमारी विश्व नंबर एक रह चुकी हैं, और जमशेदपुर की टाटा तीरंदाज़ी अकादमी कई चैंपियन तैयार करती है। भारत को 2007 टी20 और 2011 के 50 ओवर विश्व कप ख़िताब दिलाने वाले एम. एस. धोनी रांची में पले-बढ़े, जहाँ जेएससीए अंतरराष्ट्रीय स्टेडियम अंतरराष्ट्रीय क्रिकेट की मेज़बानी करता है। जमशेदपुर फ़ुटबॉल का भी केंद्र है, जहाँ टाटा फ़ुटबॉल अकादमी और जेआरडी टाटा स्पोर्ट्स कॉम्प्लेक्स हैं।",
        "झारखंड क्रीडेत आपल्या आकारापेक्षा मोठी कामगिरी करते. जयपाल सिंह मुंडा यांनी 1928 मध्ये भारताला पहिले ऑलिम्पिक हॉकी सुवर्ण मिळवून देणाऱ्या संघाचे नेतृत्व केले, आणि सिमडेगा, खुंटी व गुमला हे आदिवासी जिल्हे सलीमा टेटे व निक्की प्रधान यांसारख्या महिला संघातील ताऱ्यांसह राष्ट्रीय हॉकी खेळाडू देत आहेत. रांचीची तिरंदाज दीपिका कुमारी जागतिक क्रमवारीत पहिल्या स्थानावर राहिली आहे, आणि जमशेदपूरची टाटा तिरंदाजी अकादमी अनेक विजेते घडवते. भारताला 2007 टी20 व 2011 चा 50 षटकांचा विश्वचषक जिंकून देणारे एम. एस. धोनी रांचीत वाढले, जिथे जेएससीए आंतरराष्ट्रीय स्टेडियममध्ये आंतरराष्ट्रीय क्रिकेट सामने होतात. जमशेदपूर हे फुटबॉलचेही केंद्र आहे, जिथे टाटा फुटबॉल अकादमी व जेआरडी टाटा स्पोर्ट्स कॉम्प्लेक्स आहेत."),
        conf="Editorial"),
    lst("venues", [
        it3("jsca", "JSCA International Stadium, Ranchi", "जेएससीए अंतरराष्ट्रीय स्टेडियम, रांची", "जेएससीए आंतरराष्ट्रीय स्टेडियम, रांची"),
        it3("keenan", "Keenan Stadium, Jamshedpur", "कीनन स्टेडियम, जमशेदपुर", "कीनन स्टेडियम, जमशेदपूर"),
        it3("jrd", "JRD Tata Sports Complex, Jamshedpur", "जेआरडी टाटा स्पोर्ट्स कॉम्प्लेक्स, जमशेदपुर", "जेआरडी टाटा स्पोर्ट्स कॉम्प्लेक्स, जमशेदपूर"),
        it3("astro", "Astroturf hockey stadium, Morhabadi, Ranchi", "एस्ट्रोटर्फ़ हॉकी स्टेडियम, मोरहाबादी, रांची", "ॲस्ट्रोटर्फ हॉकी स्टेडियम, मोरहाबादी, रांची"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from Jharkhand (official list)", "झारखंड के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "झारखंडचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Jharkhand Sports Department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("birsa", ("Birsa Munda", "बिरसा मुंडा", "बिरसा मुंडा"), ("Leader of the 1899–1900 ulgulan against colonial rule and land alienation; revered as 'Dharti Aaba'.", "औपनिवेशिक शासन और भूमि हड़पने के विरुद्ध 1899–1900 के उलगुलान के नेता; 'धरती आबा' के रूप में पूजित।", "वसाहतवादी सत्ता व जमीन बळकावणीविरुद्धच्या 1899–1900 च्या उलगुलानचे नेते; 'धरती आबा' म्हणून पूज्य."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("sidhukanhu", ("Sidhu and Kanhu Murmu", "सिद्धू और कान्हू मुर्मू", "सिद्धू व कान्हू मुर्मू"), ("Brothers who led the Santhal Hul of 1855.", "1855 के संथाल हूल का नेतृत्व करने वाले भाई।", "1855 च्या संथाल हूलचे नेतृत्व करणारे बंधू."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("jaipal", ("Jaipal Singh Munda", "जयपाल सिंह मुंडा", "जयपाल सिंह मुंडा"), ("Captain of India's 1928 Olympic hockey team; Constituent Assembly member and founder of the Jharkhand Party.", "भारत की 1928 ओलंपिक हॉकी टीम के कप्तान; संविधान सभा के सदस्य और झारखंड पार्टी के संस्थापक।", "भारताच्या 1928 च्या ऑलिम्पिक हॉकी संघाचे कर्णधार; संविधान सभेचे सदस्य व झारखंड पक्षाचे संस्थापक."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("albertekka", ("Albert Ekka", "अल्बर्ट एक्का", "अल्बर्ट एक्का"), ("Soldier from Gumla awarded the Param Vir Chakra posthumously for the 1971 war.", "गुमला के सैनिक, 1971 के युद्ध के लिए मरणोपरांत परमवीर चक्र।", "गुमल्याचे सैनिक, 1971 च्या युद्धासाठी मरणोत्तर परमवीर चक्र."), ("Armed forces", "सशस्त्र बल", "सशस्त्र दल")),
        person("ramdayal", ("Ram Dayal Munda", "राम दयाल मुंडा", "राम दयाल मुंडा"), ("Scholar, musician and champion of tribal languages and arts; Padma Shri.", "विद्वान, संगीतकार और जनजातीय भाषाओं व कलाओं के समर्थक; पद्मश्री।", "विद्वान, संगीतकार व आदिवासी भाषा आणि कलांचे पुरस्कर्ते; पद्मश्री."), ("Culture", "संस्कृति", "संस्कृती")),
        person("shibu", ("Shibu Soren", "शिबू सोरेन", "शिबू सोरेन"), ("Founder leader of the Jharkhand Mukti Morcha and a leading figure of the statehood movement.", "झारखंड मुक्ति मोर्चा के संस्थापक नेता और राज्य आंदोलन के प्रमुख व्यक्ति।", "झारखंड मुक्ती मोर्चाचे संस्थापक नेते व राज्य चळवळीतील प्रमुख व्यक्ती."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("dhoni", ("M. S. Dhoni", "एम. एस. धोनी", "एम. एस. धोनी"), ("Cricketer from Ranchi who captained India to the 2007 T20 and 2011 World Cup titles.", "रांची के क्रिकेटर, जिन्होंने भारत को 2007 टी20 और 2011 विश्व कप ख़िताब दिलाए।", "रांचीचे क्रिकेटपटू, ज्यांनी भारताला 2007 टी20 व 2011 विश्वचषक जिंकून दिला."), ("Sport", "खेल", "क्रीडा")),
        person("deepika", ("Deepika Kumari", "दीपिका कुमारी", "दीपिका कुमारी"), ("Recurve archer from Ranchi; former world number one.", "रांची की रिकर्व तीरंदाज़; पूर्व विश्व नंबर एक।", "रांचीची रिकर्व्ह तिरंदाज; माजी जागतिक क्रमांक एक."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "In the 19th century, many Adivasi people from Chota Nagpur were recruited to work on the tea gardens of Assam and north Bengal, where their descendants form large communities today, and some were taken as indentured labourers to Mauritius and the Caribbean. Today workers from Jharkhand migrate seasonally to brick kilns, construction sites and farms in other States, and many young women work in domestic service in Delhi and other cities. Professionals trained at Dhanbad, Mesra and Jamshedpur work across India and abroad.",
        "19वीं सदी में छोटा नागपुर के बहुत से आदिवासी लोगों को असम और उत्तर बंगाल के चाय बाग़ानों में काम के लिए भर्ती किया गया, जहाँ उनके वंशज आज बड़े समुदाय बनाते हैं, और कुछ को गिरमिटिया मज़दूरों के रूप में मॉरीशस और कैरिबियन ले जाया गया। आज झारखंड के श्रमिक मौसमी रूप से दूसरे राज्यों के ईंट भट्ठों, निर्माण स्थलों और खेतों में जाते हैं, और बहुत सी युवा महिलाएँ दिल्ली और अन्य शहरों में घरेलू काम करती हैं। धनबाद, मेसरा और जमशेदपुर में प्रशिक्षित पेशेवर पूरे भारत और विदेश में काम करते हैं।",
        "एकोणिसाव्या शतकात छोटा नागपूरमधील अनेक आदिवासी लोकांना आसाम व उत्तर बंगालच्या चहाच्या मळ्यांत कामासाठी भरती करण्यात आले, जिथे त्यांचे वंशज आज मोठे समुदाय बनवतात, आणि काहींना करारबद्ध मजूर म्हणून मॉरिशस व कॅरिबियनमध्ये नेले गेले. आज झारखंडचे कामगार हंगामी स्वरूपात इतर राज्यांतील वीटभट्ट्या, बांधकामस्थळे व शेतांत जातात, आणि अनेक तरुण स्त्रिया दिल्ली व इतर शहरांत घरकाम करतात. धनबाद, मेसरा व जमशेदपूरमध्ये प्रशिक्षित व्यावसायिक भारतभर व परदेशात काम करतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of internal migrants", "आंतरिक प्रवासियों की संख्या", "देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Jharkhand portal", "झारखंड सरकार पोर्टल", "झारखंड शासन संकेतस्थळ", url="https://www.jharkhand.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Jharkhand Tourism", "झारखंड पर्यटन", "झारखंड पर्यटन", url="https://tourism.jharkhand.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Ranchi", "रांची", "रांची"), "0651"], [L("Jamshedpur", "जमशेदपुर", "जमशेदपूर"), "0657"], [L("Dhanbad", "धनबाद", "धनबाद"), "0326"],
           [L("Bokaro", "बोकारो", "बोकारो"), "06542"], [L("Deoghar", "देवघर", "देवघर"), "06432"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("State e-services portal — verified link", "राज्य ई-सेवा पोर्टल — सत्यापित लिंक", "राज्य ई-सेवा संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "Jharsewa / e-District portal."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("birsa", ("Jharkhand was formed on 15 November 2000, the birth anniversary of Birsa Munda.", "झारखंड 15 नवंबर 2000 को, बिरसा मुंडा की जयंती पर, बना।", "झारखंड 15 नोव्हेंबर 2000 रोजी, बिरसा मुंडांच्या जयंतीदिनी, निर्माण झाले.")),
        triv("palamau", ("Palamau was one of the first nine tiger reserves of Project Tiger in 1973.", "पलामू 1973 में प्रोजेक्ट टाइगर के पहले नौ बाघ अभयारण्यों में से एक था।", "पलामू हा 1973 मध्ये प्रोजेक्ट टायगरच्या पहिल्या नऊ व्याघ्र प्रकल्पांपैकी एक होता.")),
        triv("dvc", ("The Damodar Valley Corporation (1948) was independent India's first multipurpose river valley project.", "दामोदर घाटी निगम (1948) स्वतंत्र भारत की पहली बहुउद्देशीय नदी घाटी परियोजना थी।", "दामोदर खोरे महामंडळ (1948) हा स्वतंत्र भारताचा पहिला बहुउद्देशीय नदी खोरे प्रकल्प होता.")),
        triv("jaipal", ("Jaipal Singh Munda captained India to Olympic hockey gold at Amsterdam in 1928.", "जयपाल सिंह मुंडा ने 1928 में एम्स्टर्डम में भारत को ओलंपिक हॉकी स्वर्ण दिलाने वाली टीम की कप्तानी की।", "जयपाल सिंह मुंडा यांनी 1928 मध्ये ॲमस्टरडॅम येथे भारताला ऑलिम्पिक हॉकी सुवर्ण मिळवून देणाऱ्या संघाचे नेतृत्व केले.")),
        triv("st", ("Scheduled Tribes made up 26.2% of Jharkhand's population in 2011.", "2011 में झारखंड की जनसंख्या में अनुसूचित जनजातियों का हिस्सा 26.2% था।", "2011 मध्ये झारखंडच्या लोकसंख्येत अनुसूचित जमातींचा वाटा 26.2% होता."), "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf", "dl-planning"),
        triv("ls", ("The State elects 14 members to the Lok Sabha.", "राज्य से लोकसभा के 14 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 14 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("jh mod3 ok")
