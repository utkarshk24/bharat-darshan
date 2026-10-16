"""Telangana modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-TG"
SEO = "https://data.opencity.in/dataset/349ae865-f062-43bb-8495-07e47dbe797e/resource/38798379-3ef3-4d14-a359-24618bc06fdf/download/telangana-socio-economic-outlook-2024.pdf"
tg = read("regions/IN-TG.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About 18.9% of Telangana is forest (ISFR 2023), mostly dry deciduous teak and mixed forest in the Godavari valley and the Nallamala hills. Two tiger reserves protect the largest blocks: Kawal in the north, in Nirmal and Mancherial districts, and Amrabad in the Nallamala hills, adjoining Andhra Pradesh's Nagarjunasagar–Srisailam reserve. Eturnagaram, Pakhal and Kinnerasani sanctuaries cover the forests of the east, where Koya and Gond communities live, and the Godavari and Pranhita rivers shelter crocodiles and many birds. Hyderabad keeps green patches in the KBR National Park and the Mrugavani and Mahavir Harina Vanasthali parks, the last protecting blackbuck on the city's edge. The State has no Ramsar site.",
        "तेलंगाना का लगभग 18.9% भाग वन है (आईएसएफ़आर 2023), जो अधिकतर गोदावरी घाटी और नल्लमला पहाड़ियों में शुष्क पर्णपाती सागौन और मिश्रित वन है। दो बाघ अभयारण्य सबसे बड़े वन खंडों की रक्षा करते हैं: उत्तर में निर्मल और मंचेरियल ज़िलों में कवाल, और नल्लमला पहाड़ियों में अमराबाद, जो आंध्र प्रदेश के नागार्जुनसागर–श्रीशैलम अभयारण्य से सटा है। एटुरनागरम, पाखाल और किन्नेरसानी अभयारण्य पूर्व के वनों को समेटते हैं, जहाँ कोया और गोंड समुदाय रहते हैं, और गोदावरी व प्राणहिता नदियाँ मगरमच्छों और अनेक पक्षियों को आश्रय देती हैं। हैदराबाद में केबीआर राष्ट्रीय उद्यान, मृगवनी और महावीर हरिण वनस्थली उद्यान हरित क्षेत्र हैं; अंतिम उद्यान शहर के किनारे काले हिरणों की रक्षा करता है। राज्य में कोई रामसर स्थल नहीं है।",
        "तेलंगणाचा सुमारे 18.9% भाग वनाच्छादित आहे (आयएसएफआर 2023), बहुतांश गोदावरी खोरे व नल्लमला डोंगरांतील कोरडे पानगळीचे सागवान व मिश्र जंगल. दोन व्याघ्र प्रकल्प सर्वांत मोठ्या वनक्षेत्रांचे रक्षण करतात: उत्तरेत निर्मल व मंचेरियल जिल्ह्यांतील कवाल, आणि नल्लमला डोंगरांतील अमराबाद, जो आंध्र प्रदेशच्या नागार्जुनसागर–श्रीशैलम प्रकल्पाला लागून आहे. एटुरनागरम, पाखाल व किन्नेरसानी अभयारण्ये पूर्वेकडील जंगले व्यापतात, जिथे कोया व गोंड समुदाय राहतात, आणि गोदावरी व प्राणहिता नद्या मगरी व अनेक पक्ष्यांना आश्रय देतात. हैदराबादमध्ये केबीआर राष्ट्रीय उद्यान, मृगवनी व महावीर हरिण वनस्थली उद्याने हरित पट्टे आहेत; शेवटचे उद्यान शहराच्या कडेला काळविटांचे रक्षण करते. राज्यात एकही रामसर स्थळ नाही."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(21179.04, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(21279.46, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), tg["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(0, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="None listed for Telangana in the MoEFCC list as on 21 April 2026."), "number"),
    ]),
    lst("protected", [
        it3("kawal", "Kawal Tiger Reserve", "कवाल बाघ अभयारण्य", "कवाल व्याघ्र प्रकल्प", m=("Nirmal and Mancherial", "निर्मल और मंचेरियल", "निर्मल व मंचेरियल")),
        it3("amrabad", "Amrabad Tiger Reserve", "अमराबाद बाघ अभयारण्य", "अमराबाद व्याघ्र प्रकल्प", m=("Nallamala hills", "नल्लमला पहाड़ियाँ", "नल्लमला डोंगर")),
        it3("eturnagaram", "Eturnagaram Wildlife Sanctuary", "एटुरनागरम वन्यजीव अभयारण्य", "एटुरनागरम वन्यजीव अभयारण्य", m=("Mulugu", "मुलुगु", "मुलुगू")),
        it3("pakhal", "Pakhal Wildlife Sanctuary", "पाखाल वन्यजीव अभयारण्य", "पाखाल वन्यजीव अभयारण्य", m=("Lake and forest", "झील और वन", "तलाव व जंगल")),
        it3("kbr", "KBR National Park", "केबीआर राष्ट्रीय उद्यान", "केबीआर राष्ट्रीय उद्यान", m=("Hyderabad", "हैदराबाद", "हैदराबाद")),
        it3("harina", "Mahavir Harina Vanasthali National Park", "महावीर हरिण वनस्थली राष्ट्रीय उद्यान", "महावीर हरिण वनस्थली राष्ट्रीय उद्यान", m=("Blackbuck", "काला हिरण", "काळवीट")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("chital", "Spotted deer (State animal)", "चीतल (राज्य पशु)", "चितळ (राज्यप्राणी)"), it3("roller", "Indian roller (State bird)", "नीलकंठ (राज्य पक्षी)", "नीलकंठ (राज्यपक्षी)"),
        it3("tiger", "Tiger", "बाघ", "वाघ"), it3("blackbuck", "Blackbuck", "काला हिरण", "काळवीट"),
        it3("gaur", "Gaur", "गौर", "गवा"), it3("mugger", "Mugger crocodile", "मगर", "मगर"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger estimates (Kawal, Amrabad)", "बाघों का अनुमान (कवाल, अमराबाद)", "वाघांचा अंदाज (कवाल, अमराबाद)"), "ntca", "NTCA All India Tiger Estimation."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Telangana lies higher than the river beds of the Godavari and the Krishna, so much of its irrigation depends on lifting water and on its thousands of tanks, many dating from the Kakatiya period. Mission Kakatiya restored tanks across the State, and Mission Bhagiratha supplies treated drinking water to towns and villages by pipeline. The Kaleshwaram lift scheme on the Godavari was built to pump river water uphill to reservoirs across the north and centre; damage to its Medigadda barrage in 2023 led to an inquiry by the National Dam Safety Authority. Nagarjuna Sagar and Srisailam on the Krishna are shared with Andhra Pradesh. Hyderabad draws water from the Krishna, the Godavari, the Manjira and its old reservoirs, Osman Sagar and Himayat Sagar.",
        "तेलंगाना गोदावरी और कृष्णा की नदी तलहटी से ऊँचाई पर है, इसलिए इसकी सिंचाई का बड़ा भाग पानी उठाने और हज़ारों तालाबों पर निर्भर है, जिनमें से कई काकतीय काल के हैं। मिशन काकतीय ने पूरे राज्य में तालाबों का जीर्णोद्धार किया, और मिशन भगीरथ पाइपलाइन से कस्बों और गाँवों को शोधित पेयजल देता है। गोदावरी पर कालेश्वरम लिफ़्ट योजना नदी का पानी ऊपर उठाकर उत्तर और मध्य के जलाशयों तक पहुँचाने के लिए बनी; 2023 में इसके मेडिगड्डा बराज को हुए नुक़सान के बाद राष्ट्रीय बाँध सुरक्षा प्राधिकरण ने जाँच की। कृष्णा पर नागार्जुन सागर और श्रीशैलम आंध्र प्रदेश के साथ साझा हैं। हैदराबाद कृष्णा, गोदावरी, मंजीरा और अपने पुराने जलाशयों उस्मान सागर और हिमायत सागर से पानी लेता है।",
        "तेलंगणा गोदावरी व कृष्णेच्या पात्रांपेक्षा उंचावर आहे, त्यामुळे त्याचे बहुतांश सिंचन पाणी उपसण्यावर व हजारो तलावांवर अवलंबून आहे, ज्यांपैकी अनेक काकतीय काळातील आहेत. मिशन काकतीयने राज्यभर तलावांचे पुनरुज्जीवन केले, आणि मिशन भगीरथ जलवाहिन्यांद्वारे शहरे व गावांना प्रक्रिया केलेले पिण्याचे पाणी पुरवते. गोदावरीवरील कालेश्वरम उपसा योजना नदीचे पाणी उंचावर उचलून उत्तर व मध्य भागातील जलाशयांपर्यंत नेण्यासाठी बांधली गेली; 2023 मध्ये तिच्या मेडिगड्डा बंधाऱ्याचे नुकसान झाल्यावर राष्ट्रीय धरण सुरक्षा प्राधिकरणाने चौकशी केली. कृष्णेवरील नागार्जुन सागर व श्रीशैलम आंध्र प्रदेशसोबत सामायिक आहेत. हैदराबाद कृष्णा, गोदावरी, मांजरा व उस्मान सागर आणि हिमायत सागर या जुन्या जलाशयांतून पाणी घेते."),
        conf="Editorial"),
    gaps("g", [
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
        (L("Kaleshwaram — NDSA findings and repair status", "कालेश्वरम — एनडीएसए निष्कर्ष और मरम्मत स्थिति", "कालेश्वरम — एनडीएसए निष्कर्ष व दुरुस्ती स्थिती"), "india-gov", "National Dam Safety Authority report."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Heatwaves are Telangana's most frequent hazard, with temperatures above 45 °C in the northern districts in May. Heavy monsoon rain causes urban flooding in Hyderabad — severely in October 2020 — and floods along the Godavari at Bhadrachalam. Parts of the State face drought and groundwater stress in poor monsoon years. Seismic risk is relatively low.\n\nVisitors should carry water and avoid outdoor sightseeing at midday in summer, and check traffic and weather alerts during heavy rain in Hyderabad.",
        "लू तेलंगाना का सबसे आम ख़तरा है, और मई में उत्तरी ज़िलों में तापमान 45 °C से ऊपर चला जाता है। भारी मानसूनी वर्षा से हैदराबाद में शहरी बाढ़ आती है — अक्टूबर 2020 में गंभीर — और भद्राचलम में गोदावरी में बाढ़ आती है। ख़राब मानसून के वर्षों में राज्य के कुछ भागों को सूखे और भूजल संकट का सामना करना पड़ता है। भूकंप का जोखिम अपेक्षाकृत कम है।\n\nपर्यटकों को गर्मियों में पानी साथ रखना चाहिए और दोपहर में बाहर घूमने से बचना चाहिए, और हैदराबाद में भारी वर्षा के दौरान यातायात और मौसम चेतावनियाँ देखनी चाहिए।",
        "उष्णतेच्या लाटा हा तेलंगणावरील सर्वांत वारंवार येणारा धोका आहे; मेमध्ये उत्तरेकडील जिल्ह्यांत तापमान 45 °C च्या वर जाते. मुसळधार पावसामुळे हैदराबादमध्ये शहरी पूर येतात — ऑक्टोबर 2020 मध्ये गंभीर — आणि भद्राचलम येथे गोदावरीला पूर येतो. कमकुवत मान्सूनच्या वर्षांत राज्याच्या काही भागांना दुष्काळ व भूजल ताणाचा सामना करावा लागतो. भूकंपाचा धोका तुलनेने कमी आहे.\n\nपर्यटकांनी उन्हाळ्यात पाणी सोबत ठेवावे व दुपारी बाहेर फिरणे टाळावे, आणि हैदराबादमध्ये मुसळधार पावसात वाहतूक व हवामान इशारे तपासावेत."),
        conf="Editorial"),
    emergency_table(("Telangana", "तेलंगाना", "तेलंगणा")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official Telangana disaster management address."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Telangana has 18 registered Geographical Indications of its own in the GI Registry's list as on 31 December 2025, and shares Banaganapalle mangoes with Andhra Pradesh. Pochampally Ikat, filed in 2003, was among the earliest GIs in India. Handlooms and crafts dominate — Gadwal and Narayanpet saris, Siddipet Gollabama, the Telia rumal, Warangal durries, Nirmal paintings, toys and furniture, Cheriyal paintings, Pembarthi metal craft, Adilabad dokra, Hyderabad lac bangles and Karimnagar silver filigree. Food GIs include Hyderabad haleem, Tandur red gram and Warangal chapata chilli.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में तेलंगाना के अपने 18 पंजीकृत भौगोलिक संकेतक हैं, और बंगनपल्ले आम आंध्र प्रदेश के साथ साझा है। 2003 में दायर पोचमपल्ली इकत भारत के सबसे पहले जीआई में से था। हथकरघा और शिल्प प्रमुख हैं — गदवाल और नारायणपेट साड़ियाँ, सिद्दिपेट गोल्लभामा, तेलिया रुमाल, वारंगल दरियाँ, निर्मल चित्र, खिलौने और फ़र्नीचर, चेरियाल चित्र, पेम्बर्थी धातु शिल्प, आदिलाबाद डोकरा, हैदराबाद की लाख की चूड़ियाँ और करीमनगर की चाँदी की तारकशी। खाद्य जीआई में हैदराबाद हलीम, तांडूर अरहर और वारंगल चपाटा मिर्च शामिल हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत तेलंगणाची स्वतःची 18 नोंदणीकृत भौगोलिक मानांकने आहेत, आणि बंगनपल्ले आंबे आंध्र प्रदेशसोबत सामायिक आहेत. 2003 मध्ये दाखल झालेले पोचमपल्ली इकत हे भारतातील सर्वांत सुरुवातीच्या जीआयपैकी होते. हातमाग व हस्तकलेचे वर्चस्व आहे — गदवाल व नारायणपेठ साड्या, सिद्दिपेट गोल्लभामा, तेलिया रुमाल, वरंगळच्या सतरंज्या, निर्मल चित्रे, खेळणी व फर्निचर, चेरियाल चित्रे, पेम्बर्थी धातुकला, आदिलाबाद डोकरा, हैदराबादच्या लाखेच्या बांगड्या व करीमनगरचे चांदीचे तारकाम. खाद्य जीआयमध्ये हैदराबाद हलीम, तांडूर तूर व वरंगळ चपाटा मिरची यांचा समावेश आहे."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Hyderabad is the main attraction: the Charminar and its bazaars, the Golconda fort and its sound-and-light show, the Qutb Shahi tombs, the Chowmahalla and Falaknuma palaces, the Salar Jung Museum and the lakeside Hussain Sagar with its Buddha statue. Warangal has the Kakatiya fort and Thousand Pillar temple, and the UNESCO-listed Ramappa temple and Laknavaram lake lie nearby in Mulugu district. Pilgrims visit Yadagirigutta, Bhadrachalam, Vemulawada and the Saraswati temple at Basar, and nature lovers the Kuntala and Pochera waterfalls, Nagarjuna Sagar and the forests of Amrabad.",
        "हैदराबाद मुख्य आकर्षण है: चारमीनार और उसके बाज़ार, गोलकुंडा क़िला और उसका ध्वनि-प्रकाश कार्यक्रम, क़ुतुबशाही मक़बरे, चौमहल्ला और फ़लकनुमा महल, सालारजंग संग्रहालय और बुद्ध प्रतिमा वाला हुसैन सागर। वारंगल में काकतीय क़िला और हज़ार स्तंभ मंदिर हैं, और पास के मुलुगु ज़िले में यूनेस्को सूचीबद्ध रामप्पा मंदिर और लकनावरम झील हैं। तीर्थयात्री यादगिरिगुट्टा, भद्राचलम, वेमुलवाड़ा और बासर के सरस्वती मंदिर जाते हैं, और प्रकृति प्रेमी कुंटाला व पोचेरा झरने, नागार्जुन सागर और अमराबाद के वन।",
        "हैदराबाद हे मुख्य आकर्षण आहे: चारमिनार व त्याचे बाजार, गोवळकोंडा किल्ला व तिथला ध्वनि-प्रकाश कार्यक्रम, कुतुबशाही कबरी, चौमहल्ला व फलकनुमा राजवाडे, सालारजंग संग्रहालय आणि बुद्धमूर्ती असलेला हुसेन सागर. वरंगळमध्ये काकतीय किल्ला व हजार खांबी मंदिर आहे, आणि जवळच्या मुलुगू जिल्ह्यात युनेस्को यादीतील रामप्पा मंदिर व लकनावरम तलाव आहे. यात्रेकरू यादगिरीगुट्टा, भद्राचलम, वेमुलवाडा व बासरचे सरस्वती मंदिर येथे जातात, आणि निसर्गप्रेमी कुंटाला व पोचेरा धबधबे, नागार्जुन सागर व अमराबादची जंगले."),
        conf="Editorial"),
    lst("places", [
        it3("charminar", "Charminar and the old city", "चारमीनार और पुराना शहर", "चारमिनार व जुने शहर", m=("Heritage, food", "धरोहर, भोजन", "वारसा, खाद्य")),
        it3("golconda", "Golconda Fort and Qutb Shahi tombs", "गोलकुंडा क़िला और क़ुतुबशाही मक़बरे", "गोवळकोंडा किल्ला व कुतुबशाही कबरी", m=("Heritage", "धरोहर", "वारसा")),
        it3("salarjung", "Salar Jung Museum", "सालारजंग संग्रहालय", "सालारजंग संग्रहालय", m=("Museum", "संग्रहालय", "संग्रहालय")),
        it3("ramappa", "Ramappa Temple and Laknavaram", "रामप्पा मंदिर और लकनावरम", "रामप्पा मंदिर व लकनावरम", m=("UNESCO site", "यूनेस्को स्थल", "युनेस्को स्थळ")),
        it3("warangal", "Warangal Fort and Thousand Pillar Temple", "वारंगल क़िला और हज़ार स्तंभ मंदिर", "वरंगळ किल्ला व हजार खांबी मंदिर", m=("Kakatiya heritage", "काकतीय धरोहर", "काकतीय वारसा")),
        it3("bhadrachalam", "Bhadrachalam", "भद्राचलम", "भद्राचलम", m=("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        it3("kuntala", "Kuntala waterfall", "कुंटाला झरना", "कुंटाला धबधबा", m=("Nature (monsoon)", "प्रकृति (मानसून)", "निसर्ग (पावसाळा)")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Hyderabad: Charminar, Chowmahalla, Salar Jung Museum; Golconda and the Qutb Shahi tombs.", "हैदराबाद: चारमीनार, चौमहल्ला, सालारजंग संग्रहालय; गोलकुंडा और क़ुतुबशाही मक़बरे।", "हैदराबाद: चारमिनार, चौमहल्ला, सालारजंग संग्रहालय; गोवळकोंडा व कुतुबशाही कबरी.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Add Warangal, Ramappa and Laknavaram.", "वारंगल, रामप्पा और लकनावरम जोड़ें।", "वरंगळ, रामप्पा व लकनावरम जोडा.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Hyderabad, Pochampally weavers' village, Yadagirigutta and Nagarjuna Sagar.", "हैदराबाद, पोचमपल्ली बुनकर गाँव, यादगिरिगुट्टा और नागार्जुन सागर।", "हैदराबाद, पोचमपल्ली विणकर गाव, यादगिरीगुट्टा व नागार्जुन सागर.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("tgt", "Telangana Tourism (official)", "तेलंगाना पर्यटन (आधिकारिक)", "तेलंगणा पर्यटन (अधिकृत)", url="https://tourism.telangana.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Adilabad", "आदिलाबाद", "आदिलाबाद"), ("Bhadradri Kothagudem", "भद्राद्रि कोठागुडेम", "भद्राद्री कोठागुडेम"), ("Hanumakonda", "हनुमकोंडा", "हनुमकोंडा"),
    ("Hyderabad", "हैदराबाद", "हैदराबाद"), ("Jagtial", "जगतियाल", "जगतियाल"), ("Jangaon", "जनगांव", "जनगाव"), ("Jayashankar Bhupalpally", "जयशंकर भूपालपल्ली", "जयशंकर भूपालपल्ली"),
    ("Jogulamba Gadwal", "जोगुलांबा गदवाल", "जोगुलांबा गदवाल"), ("Kamareddy", "कामारेड्डी", "कामारेड्डी"), ("Karimnagar", "करीमनगर", "करीमनगर"), ("Khammam", "खम्मम", "खम्मम"),
    ("Kumuram Bheem Asifabad", "कुमुरम भीम आसिफ़ाबाद", "कुमुरम भीम आसिफाबाद"), ("Mahabubabad", "महबूबाबाद", "महबूबाबाद"), ("Mahabubnagar", "महबूबनगर", "महबूबनगर"),
    ("Mancherial", "मंचेरियल", "मंचेरियल"), ("Medak", "मेदक", "मेदक"), ("Medchal–Malkajgiri", "मेडचल–मलकाजगिरि", "मेडचल–मलकाजगिरी"), ("Mulugu", "मुलुगु", "मुलुगू"),
    ("Nagarkurnool", "नागरकर्नूल", "नागरकर्नूल"), ("Nalgonda", "नलगोंडा", "नलगोंडा"), ("Narayanpet", "नारायणपेट", "नारायणपेठ"), ("Nirmal", "निर्मल", "निर्मल"),
    ("Nizamabad", "निज़ामाबाद", "निजामाबाद"), ("Peddapalli", "पेद्दापल्ली", "पेद्दापल्ली"), ("Rajanna Sircilla", "राजन्ना सिरसिल्ला", "राजन्ना सिरसिल्ला"), ("Ranga Reddy", "रंगारेड्डी", "रंगारेड्डी"),
    ("Sangareddy", "संगारेड्डी", "संगारेड्डी"), ("Siddipet", "सिद्दिपेट", "सिद्दिपेट"), ("Suryapet", "सूर्यापेट", "सूर्यापेट"), ("Vikarabad", "विकाराबाद", "विकाराबाद"),
    ("Wanaparthy", "वनपर्ती", "वनपर्ती"), ("Warangal", "वारंगल", "वरंगळ"), ("Yadadri Bhuvanagiri", "यादाद्रि भुवनगिरि", "यादाद्री भुवनगिरी"),
]
assert len(DISTRICTS) == 33, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("hyderabad", ("Hyderabad", "हैदराबाद", "हैदराबाद"), ("State capital; IT, pharma, research; historic old city.", "राज्य की राजधानी; आईटी, दवा, शोध; ऐतिहासिक पुराना शहर।", "राज्याची राजधानी; आयटी, औषधनिर्मिती, संशोधन; ऐतिहासिक जुने शहर."), ("Capital", "राजधानी", "राजधानी")),
        city("secunderabad", ("Secunderabad", "सिकंदराबाद", "सिकंदराबाद"), ("Twin city; cantonment and railway headquarters.", "जुड़वाँ शहर; छावनी और रेलवे मुख्यालय।", "जुळे शहर; छावणी व रेल्वे मुख्यालय."), ("Twin city", "जुड़वाँ शहर", "जुळे शहर")),
        city("warangal", ("Warangal", "वारंगल", "वरंगळ"), ("Kakatiya capital; NIT; textile park.", "काकतीय राजधानी; एनआईटी; वस्त्र पार्क।", "काकतीय राजधानी; एनआयटी; वस्त्र उद्यान."), ("Heritage", "धरोहर", "वारसा")),
        city("karimnagar", ("Karimnagar", "करीमनगर", "करीमनगर"), ("Silver filigree; granite.", "चाँदी की तारकशी; ग्रेनाइट।", "चांदीचे तारकाम; ग्रॅनाइट."), ("Crafts", "शिल्प", "हस्तकला")),
        city("nizamabad", ("Nizamabad", "निज़ामाबाद", "निजामाबाद"), ("Turmeric and agricultural trade.", "हल्दी और कृषि व्यापार।", "हळद व कृषी व्यापार."), ("Agri-trade", "कृषि व्यापार", "कृषी व्यापार")),
        city("khammam", ("Khammam", "खम्मम", "खम्मम"), ("Granite, chillies; gateway to Bhadrachalam.", "ग्रेनाइट, मिर्च; भद्राचलम का प्रवेश द्वार।", "ग्रॅनाइट, मिरची; भद्राचलमचे प्रवेशद्वार."), ("East", "पूर्व", "पूर्व")),
        city("ramagundam", ("Ramagundam", "रामागुंडम", "रामगुंडम"), ("Power, coal and fertiliser.", "बिजली, कोयला और उर्वरक।", "वीज, कोळसा व खते."), ("Industry", "उद्योग", "उद्योग")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 33 districts (alphabetical)", "33 ज़िले (वर्णानुक्रम)", "33 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    lst("dsrc", [it3("seo", "Telangana Socio Economic Outlook 2024 (33 districts, 620 mandals)", "तेलंगाना सामाजिक-आर्थिक परिदृश्य 2024 (33 ज़िले, 620 मंडल)", "तेलंगणा सामाजिक-आर्थिक आढावा 2024 (33 जिल्हे, 620 मंडळे)", url=SEO, src="tg-plan")],
        title=L("Source for the district count", "ज़िलों की संख्या का स्रोत", "जिल्हा संख्येचा स्रोत"), conf="Official"),
    gaps("g", [
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Hyderabad is one of India's great sporting cities, especially for badminton. P. V. Sindhu won Olympic silver in 2016 and bronze in 2020 and became world champion in 2019; Saina Nehwal, who trained in Hyderabad, won bronze at London 2012; both came through the Pullela Gopichand Badminton Academy at Gachibowli. Sania Mirza won six Grand Slam titles in doubles and mixed doubles, and Nizamabad's Nikhat Zareen became world boxing champion in 2022 and 2023. Hyderabad cricketers include Mohammed Azharuddin and V. V. S. Laxman, and the Rajiv Gandhi International Cricket Stadium at Uppal hosts international and IPL matches.",
        "हैदराबाद भारत के महान खेल शहरों में है, विशेषकर बैडमिंटन के लिए। पी. वी. सिंधु ने 2016 में ओलंपिक रजत और 2020 में कांस्य जीता और 2019 में विश्व चैंपियन बनीं; हैदराबाद में प्रशिक्षित साइना नेहवाल ने लंदन 2012 में कांस्य जीता; दोनों गच्चीबौली की पुल्लेला गोपीचंद बैडमिंटन अकादमी से निकलीं। सानिया मिर्ज़ा ने युगल और मिश्रित युगल में छह ग्रैंड स्लैम ख़िताब जीते, और निज़ामाबाद की निकहत ज़रीन 2022 और 2023 में विश्व मुक्केबाज़ी चैंपियन बनीं। हैदराबाद के क्रिकेटरों में मोहम्मद अज़हरुद्दीन और वी. वी. एस. लक्ष्मण हैं, और उप्पल का राजीव गांधी अंतरराष्ट्रीय क्रिकेट स्टेडियम अंतरराष्ट्रीय और आईपीएल मैचों की मेज़बानी करता है।",
        "हैदराबाद हे भारतातील महान क्रीडा शहरांपैकी आहे, विशेषतः बॅडमिंटनसाठी. पी. व्ही. सिंधू यांनी 2016 मध्ये ऑलिम्पिक रौप्य व 2020 मध्ये कांस्यपदक जिंकले आणि 2019 मध्ये त्या जगज्जेत्या झाल्या; हैदराबादमध्ये प्रशिक्षण घेतलेल्या सायना नेहवाल यांनी लंडन 2012 मध्ये कांस्य जिंकले; दोघीही गच्चीबावलीतील पुल्लेला गोपीचंद बॅडमिंटन अकादमीतून घडल्या. सानिया मिर्झा यांनी दुहेरी व मिश्र दुहेरीत सहा ग्रँड स्लॅम विजेतेपदे जिंकली, आणि निजामाबादच्या निखत झरीन 2022 व 2023 मध्ये जागतिक मुष्टियुद्ध विजेत्या झाल्या. हैदराबादच्या क्रिकेटपटूंत मोहम्मद अझरुद्दीन व व्ही. व्ही. एस. लक्ष्मण आहेत, आणि उप्पलचे राजीव गांधी आंतरराष्ट्रीय क्रिकेट स्टेडियम आंतरराष्ट्रीय व आयपीएल सामने आयोजित करते."),
        conf="Editorial"),
    lst("venues", [
        it3("uppal", "Rajiv Gandhi International Cricket Stadium, Uppal", "राजीव गांधी अंतरराष्ट्रीय क्रिकेट स्टेडियम, उप्पल", "राजीव गांधी आंतरराष्ट्रीय क्रिकेट स्टेडियम, उप्पल"),
        it3("gachibowli", "G. M. C. Balayogi Athletic Stadium, Gachibowli", "जी. एम. सी. बालयोगी एथलेटिक स्टेडियम, गच्चीबौली", "जी. एम. सी. बालयोगी ऍथलेटिक स्टेडियम, गच्चीबावली"),
        it3("gopichand", "Pullela Gopichand Badminton Academy", "पुल्लेला गोपीचंद बैडमिंटन अकादमी", "पुल्लेला गोपीचंद बॅडमिंटन अकादमी"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from Telangana (official list)", "तेलंगाना के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "तेलंगणाचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Sports Authority of Telangana.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("quli", ("Muhammad Quli Qutb Shah", "मुहम्मद क़ुली क़ुतुबशाह", "मुहम्मद कुली कुतुबशहा"), ("Sultan of Golconda who founded Hyderabad; a poet in Dakhni and Telugu.", "गोलकुंडा के सुल्तान जिन्होंने हैदराबाद बसाया; दक्खिनी और तेलुगु के कवि।", "गोवळकोंड्याचे सुलतान ज्यांनी हैदराबाद वसवले; दख्खनी व तेलुगुचे कवी."), ("History", "इतिहास", "इतिहास")),
        person("rudrama", ("Rudrama Devi", "रुद्रमा देवी", "रुद्रमा देवी"), ("Kakatiya queen who ruled from Warangal in the 13th century.", "13वीं सदी में वारंगल से शासन करने वाली काकतीय रानी।", "तेराव्या शतकात वरंगळहून राज्य करणारी काकतीय राणी."), ("History", "इतिहास", "इतिहास")),
        person("komaram", ("Komaram Bheem", "कोमरम भीम", "कोमरम भीम"), ("Gond leader who fought for tribal land and forest rights against the Nizam's rule.", "गोंड नेता जिन्होंने निज़ाम शासन के विरुद्ध आदिवासी भूमि और वन अधिकारों के लिए संघर्ष किया।", "गोंड नेते ज्यांनी निजामी राजवटीविरुद्ध आदिवासी जमीन व वन अधिकारांसाठी लढा दिला."), ("Tribal movement", "आदिवासी आंदोलन", "आदिवासी चळवळ")),
        person("sarojini", ("Sarojini Naidu", "सरोजिनी नायडू", "सरोजिनी नायडू"), ("Poet and freedom fighter born in Hyderabad; first woman Governor in independent India.", "हैदराबाद में जन्मी कवयित्री और स्वतंत्रता सेनानी; स्वतंत्र भारत की पहली महिला राज्यपाल।", "हैदराबादमध्ये जन्मलेल्या कवयित्री व स्वातंत्र्यसैनिक; स्वतंत्र भारतातील पहिल्या महिला राज्यपाल."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("pvnr", ("P. V. Narasimha Rao", "पी. वी. नरसिम्हा राव", "पी. व्ही. नरसिंह राव"), ("Prime Minister of India (1991–96), born in Warangal district; Bharat Ratna.", "भारत के प्रधानमंत्री (1991–96), वारंगल ज़िले में जन्मे; भारत रत्न।", "भारताचे पंतप्रधान (1991–96), वरंगळ जिल्ह्यात जन्म; भारतरत्न."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("kaloji", ("Kaloji Narayana Rao", "कालोजी नारायण राव", "कालोजी नारायण राव"), ("Poet of the people and voice of Telangana's identity.", "जनकवि और तेलंगाना की पहचान की आवाज़।", "जनकवी व तेलंगणाच्या अस्मितेचा आवाज."), ("Literature", "साहित्य", "साहित्य")),
        person("makhdoom", ("Makhdoom Mohiuddin", "मख़दूम मोहिउद्दीन", "मखदूम मोहिउद्दीन"), ("Urdu poet and leader of the Telangana peasant struggle.", "उर्दू कवि और तेलंगाना किसान संघर्ष के नेता।", "उर्दू कवी व तेलंगणा शेतकरी लढ्याचे नेते."), ("Literature", "साहित्य", "साहित्य")),
        person("jayashankar", ("K. Jayashankar", "के. जयशंकर", "के. जयशंकर"), ("Economist and ideologue of the Telangana movement.", "अर्थशास्त्री और तेलंगाना आंदोलन के विचारक।", "अर्थशास्त्रज्ञ व तेलंगणा आंदोलनाचे विचारवंत."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("benegal", ("Shyam Benegal", "श्याम बेनेगल", "श्याम बेनेगल"), ("Film-maker of Indian parallel cinema, born in Hyderabad.", "भारतीय समानांतर सिनेमा के फ़िल्मकार, हैदराबाद में जन्मे।", "भारतीय समांतर चित्रपटांचे दिग्दर्शक, हैदराबादमध्ये जन्म."), ("Cinema", "सिनेमा", "चित्रपट")),
        person("sindhu", ("P. V. Sindhu", "पी. वी. सिंधु", "पी. व्ही. सिंधू"), ("Two-time Olympic medallist and 2019 world badminton champion.", "दो बार की ओलंपिक पदक विजेता और 2019 की विश्व बैडमिंटन चैंपियन।", "दोनदा ऑलिम्पिक पदकविजेत्या व 2019 च्या जागतिक बॅडमिंटन विजेत्या."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Telangana has a long history of migration to the Gulf: workers from Karimnagar, Nizamabad, Jagtial and nearby districts have gone to the UAE, Saudi Arabia, Oman and other Gulf countries for decades. Hyderabad's professionals have settled in large numbers in the United States, and its old families have links with Pakistan, the Gulf and the United Kingdom. The State is also a destination for migrants from across India who work in Hyderabad's construction, services and technology industries.",
        "तेलंगाना का खाड़ी देशों में प्रवास का लंबा इतिहास है: करीमनगर, निज़ामाबाद, जगतियाल और आसपास के ज़िलों के श्रमिक दशकों से यूएई, सऊदी अरब, ओमान और अन्य खाड़ी देशों में जाते रहे हैं। हैदराबाद के पेशेवर बड़ी संख्या में अमेरिका में बसे हैं, और इसके पुराने परिवारों के पाकिस्तान, खाड़ी और ब्रिटेन से संबंध हैं। राज्य पूरे भारत के उन प्रवासियों का गंतव्य भी है जो हैदराबाद के निर्माण, सेवा और प्रौद्योगिकी उद्योगों में काम करते हैं।",
        "तेलंगणाला आखाती देशांत स्थलांतराचा दीर्घ इतिहास आहे: करीमनगर, निजामाबाद, जगतियाल व आसपासच्या जिल्ह्यांतील कामगार दशकांपासून यूएई, सौदी अरेबिया, ओमान व इतर आखाती देशांत जात आहेत. हैदराबादचे व्यावसायिक मोठ्या संख्येने अमेरिकेत स्थायिक झाले आहेत, आणि तिथल्या जुन्या कुटुंबांचे पाकिस्तान, आखाती देश व ब्रिटनशी संबंध आहेत. हैदराबादच्या बांधकाम, सेवा व तंत्रज्ञान उद्योगांत काम करणाऱ्या भारतभरातील स्थलांतरितांचेही हे राज्य गंतव्य आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants and internal migrants", "प्रवासियों और आंतरिक प्रवासियों की संख्या", "परदेशी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; MEA."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Telangana portal", "तेलंगाना सरकार पोर्टल", "तेलंगणा शासन संकेतस्थळ", url="https://www.telangana.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Telangana Tourism", "तेलंगाना पर्यटन", "तेलंगणा पर्यटन", url="https://tourism.telangana.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Hyderabad", "हैदराबाद", "हैदराबाद"), "040"], [L("Warangal", "वारंगल", "वरंगळ"), "0870"], [L("Karimnagar", "करीमनगर", "करीमनगर"), "0878"],
           [L("Nizamabad", "निज़ामाबाद", "निजामाबाद"), "08462"], [L("Khammam", "खम्मम", "खम्मम"), "08742"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("State e-services portal — verified link", "राज्य ई-सेवा पोर्टल — सत्यापित लिंक", "राज्य ई-सेवा संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "MeeSeva / State services portal."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("young", ("Telangana, formed on 2 June 2014, is India's youngest State.", "2 जून 2014 को बना तेलंगाना भारत का सबसे नया राज्य है।", "2 जून 2014 रोजी स्थापन झालेले तेलंगणा हे भारतातील सर्वांत नवे राज्य आहे.")),
        triv("ramappa", ("The Ramappa temple is named after its sculptor, Ramappa — rare for an Indian temple.", "रामप्पा मंदिर का नाम उसके शिल्पी रामप्पा के नाम पर है — भारतीय मंदिर के लिए दुर्लभ।", "रामप्पा मंदिराचे नाव त्याच्या शिल्पकार रामप्पाच्या नावावरून आहे — भारतीय मंदिरासाठी दुर्मीळ."), UNESCO, "unesco-whc"),
        triv("haleem", ("Hyderabad Haleem is a registered Geographical Indication (filed 2009).", "हैदराबाद हलीम पंजीकृत भौगोलिक संकेतक है (2009 में दायर)।", "हैदराबाद हलीम हे नोंदणीकृत भौगोलिक मानांकन आहे (2009 मध्ये दाखल)."), GI_PDF, "gi-registry"),
        triv("pochampally", ("Pochampally Ikat was filed as GI application number 4 in 2003.", "पोचमपल्ली इकत 2003 में जीआई आवेदन संख्या 4 के रूप में दायर हुआ।", "पोचमपल्ली इकत 2003 मध्ये जीआय अर्ज क्रमांक 4 म्हणून दाखल झाले."), GI_PDF, "gi-registry"),
        triv("osmania", ("Osmania University (1918) was the first Indian university to teach in Urdu.", "उस्मानिया विश्वविद्यालय (1918) उर्दू में पढ़ाने वाला पहला भारतीय विश्वविद्यालय था।", "उस्मानिया विद्यापीठ (1918) हे उर्दूतून शिकवणारे पहिले भारतीय विद्यापीठ होते.")),
        triv("ls", ("The State elects 17 members to the Lok Sabha.", "राज्य से लोकसभा के 17 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 17 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("tg mod3 ok")
