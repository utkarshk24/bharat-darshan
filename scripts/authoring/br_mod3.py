"""Bihar modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-BR"
br = read("regions/IN-BR.json")["metrics"]; ind = read("india.json")["metrics"]

RAMSAR_BR = [
    ("Kanwar Lake (Kabartal)", "कांवर झील (काबरताल)", "कांवर सरोवर (काबरताल)", "2020", "2,620"),
    ("Nagi Bird Sanctuary", "नागी पक्षी अभयारण्य", "नागी पक्षी अभयारण्य", "2023", "205.82"),
    ("Nakti Bird Sanctuary", "नकटी पक्षी अभयारण्य", "नकटी पक्षी अभयारण्य", "2023", "332.61"),
    ("Gokul Jalashay", "गोकुल जलाशय", "गोकुळ जलाशय", "2025", "448"),
    ("Udaipur Jheel", "उदयपुर झील", "उदयपूर सरोवर", "2025", "319"),
    ("Gogabil", "गोगाबील", "गोगाबील", "2025", "86.63"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Only about 8% of Bihar is forest (ISFR 2023), mostly in the Valmiki Tiger Reserve in the far north-west — the State's only tiger reserve, adjoining Nepal's Chitwan National Park — and in the Kaimur hills and the Rajgir–Gaya hills of the south. The rivers are Bihar's richest wildlife habitat: the Vikramshila Gangetic Dolphin Sanctuary near Bhagalpur protects the endangered Ganges river dolphin, India's national aquatic animal, and the oxbow lakes, chaurs and ponds of the north are winter homes for migratory birds.\n\nBihar has six Ramsar sites: Kanwar Lake (Kabartal) in Begusarai, the Nagi and Nakti bird sanctuaries in Jamui, and, from 2025, Gokul Jalashay, Udaipur Jheel and Gogabil.",
        "बिहार का केवल लगभग 8% भाग वन है (आईएसएफ़आर 2023), जो अधिकतर सुदूर उत्तर-पश्चिम के वाल्मीकि बाघ अभयारण्य में — राज्य का एकमात्र बाघ अभयारण्य, जो नेपाल के चितवन राष्ट्रीय उद्यान से सटा है — और दक्षिण की कैमूर और राजगीर–गया पहाड़ियों में है। नदियाँ बिहार के सबसे समृद्ध वन्यजीव आवास हैं: भागलपुर के पास विक्रमशिला गंगा डॉल्फ़िन अभयारण्य भारत के राष्ट्रीय जलीय जीव, संकटग्रस्त गंगा डॉल्फ़िन की रक्षा करता है, और उत्तर की गोखुर झीलें, चौर और तालाब प्रवासी पक्षियों के शीतकालीन घर हैं।\n\nबिहार में छह रामसर स्थल हैं: बेगूसराय की कांवर झील (काबरताल), जमुई के नागी और नकटी पक्षी अभयारण्य, और 2025 से गोकुल जलाशय, उदयपुर झील और गोगाबील।",
        "बिहारचा केवळ सुमारे 8% भाग वनाच्छादित आहे (आयएसएफआर 2023), बहुतांश अगदी वायव्येकडील वाल्मीकी व्याघ्र प्रकल्पात — राज्यातील एकमेव व्याघ्र प्रकल्प, नेपाळच्या चितवन राष्ट्रीय उद्यानाला लागून — आणि दक्षिणेकडील कैमूर व राजगीर–गया डोंगरांत. नद्या हा बिहारचा सर्वांत समृद्ध वन्यजीव अधिवास आहे: भागलपूरजवळील विक्रमशिला गांगेय डॉल्फिन अभयारण्य भारताचा राष्ट्रीय जलचर, संकटग्रस्त गंगा डॉल्फिनचे रक्षण करते, आणि उत्तरेकडील गोखुर सरोवरे, चौर व तलाव स्थलांतरित पक्ष्यांची हिवाळी घरे आहेत.\n\nबिहारमध्ये सहा रामसर स्थळे आहेत: बेगुसरायचे कांवर सरोवर (काबरताल), जमुईची नागी व नकटी पक्षी अभयारण्ये, आणि 2025 पासून गोकुळ जलाशय, उदयपूर सरोवर व गोगाबील."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(7532.45, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(7403.26, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), br["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(6, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_BR], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026 (year of designation).", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची (घोषणा वर्ष)।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी (घोषणा वर्ष).")),
    lst("protected", [
        it3("valmiki", "Valmiki Tiger Reserve", "वाल्मीकि बाघ अभयारण्य", "वाल्मीकी व्याघ्र प्रकल्प", m=("West Champaran", "पश्चिमी चंपारण", "पश्चिम चंपारण")),
        it3("vikramshila", "Vikramshila Gangetic Dolphin Sanctuary", "विक्रमशिला गंगा डॉल्फ़िन अभयारण्य", "विक्रमशिला गांगेय डॉल्फिन अभयारण्य", m=("Bhagalpur", "भागलपुर", "भागलपूर")),
        it3("kaimur", "Kaimur Wildlife Sanctuary", "कैमूर वन्यजीव अभयारण्य", "कैमूर वन्यजीव अभयारण्य", m=("Kaimur plateau", "कैमूर पठार", "कैमूर पठार")),
        it3("bhimbandh", "Bhimbandh Wildlife Sanctuary", "भीमबांध वन्यजीव अभयारण्य", "भीमबांध वन्यजीव अभयारण्य", m=("Hot springs", "गर्म जलकुंड", "गरम पाण्याचे झरे")),
        it3("kabartal", "Kanwar Lake (Kabartal)", "कांवर झील (काबरताल)", "कांवर सरोवर (काबरताल)", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("dolphin", "Ganges river dolphin", "गंगा डॉल्फ़िन", "गंगा डॉल्फिन"), it3("tiger", "Tiger", "बाघ", "वाघ"),
        it3("gaur", "Gaur (State animal)", "गौर (राज्य पशु)", "गवा (राज्यप्राणी)"), it3("sparrow", "House sparrow (State bird)", "गौरैया (राज्य पक्षी)", "चिमणी (राज्यपक्षी)"),
        it3("gharial", "Gharial (Gandak)", "घड़ियाल (गंडक)", "घडियाल (गंडक)"), it3("adjutant", "Greater adjutant stork", "गरुड़ (बड़ा गरुड़ बगुला)", "मोठा करकोचा (गरुड)"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger estimate (Valmiki)", "बाघों का अनुमान (वाल्मीकि)", "वाघांचा अंदाज (वाल्मीकी)"), "ntca", "NTCA All India Tiger Estimation."),
        (L("Gangetic dolphin count in Bihar", "बिहार में गंगा डॉल्फ़िन की संख्या", "बिहारमधील गंगा डॉल्फिनची संख्या"), "moefcc", "Project Dolphin population estimate."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "North Bihar has too much water and south Bihar too little. The Kosi, Gandak, Bagmati and other rivers from Nepal carry heavy silt and flood large parts of the north almost every monsoon; thousands of kilometres of embankments have been built, but breaches — like the Kosi breach at Kusaha in Nepal in August 2008, which displaced millions — remain a threat. Many north Bihar districts also face waterlogging. South Bihar, drained by the Son, Punpun and Phalgu, depends on canals from the Son barrage at Indrapuri and on groundwater, and suffers droughts. Arsenic in groundwater affects districts along the Ganga, and fluoride some southern areas; the State's 'Har Ghar Nal Ka Jal' scheme aims to give every household piped water.",
        "उत्तर बिहार में पानी बहुत अधिक है और दक्षिण बिहार में बहुत कम। नेपाल से आने वाली कोसी, गंडक, बागमती और अन्य नदियाँ भारी गाद लाती हैं और लगभग हर मानसून में उत्तर के बड़े हिस्सों में बाढ़ लाती हैं; हज़ारों किलोमीटर तटबंध बनाए गए हैं, लेकिन टूटन — जैसे अगस्त 2008 में नेपाल के कुसहा में कोसी तटबंध का टूटना, जिससे लाखों लोग विस्थापित हुए — अब भी ख़तरा है। उत्तर बिहार के कई ज़िलों में जलजमाव भी है। सोन, पुनपुन और फल्गु द्वारा जल-निकासी वाला दक्षिण बिहार इंद्रपुरी के सोन बराज की नहरों और भूजल पर निर्भर है, और सूखे से पीड़ित होता है। गंगा किनारे के ज़िलों में भूजल में आर्सेनिक और कुछ दक्षिणी क्षेत्रों में फ़्लोराइड है; राज्य की 'हर घर नल का जल' योजना का लक्ष्य हर घर को नल से पानी देना है।",
        "उत्तर बिहारमध्ये पाणी फार जास्त आहे आणि दक्षिण बिहारमध्ये फार कमी. नेपाळमधून येणाऱ्या कोसी, गंडक, बागमती व इतर नद्या प्रचंड गाळ आणतात आणि जवळपास दर पावसाळ्यात उत्तरेच्या मोठ्या भागात पूर आणतात; हजारो किलोमीटर बांध बांधले गेले आहेत, पण भगदाडे — जसे ऑगस्ट 2008 मध्ये नेपाळमधील कुसहा येथे कोसीचा बांध फुटला, ज्यामुळे लाखो लोक विस्थापित झाले — अजूनही धोका आहेत. उत्तर बिहारच्या अनेक जिल्ह्यांत पाणी साचण्याची समस्याही आहे. सोन, पुनपुन व फल्गूने वाहून नेलेला दक्षिण बिहार इंद्रपुरी येथील सोन बंधाऱ्याच्या कालव्यांवर व भूजलावर अवलंबून आहे, आणि दुष्काळ सोसतो. गंगेकाठच्या जिल्ह्यांत भूजलात आर्सेनिक व काही दक्षिणेकडील भागांत फ्लोराइड आहे; राज्याची 'हर घर नल का जल' योजना प्रत्येक घराला नळाने पाणी देण्याचे उद्दिष्ट ठेवते."),
        conf="Editorial"),
    gaps("g", [
        (L("Flood-affected population and area by year", "वर्षवार बाढ़ प्रभावित जनसंख्या और क्षेत्र", "वर्षनिहाय पूरग्रस्त लोकसंख्या व क्षेत्र"), "india-gov", "Bihar Disaster Management Department annual flood reports."),
        (L("Arsenic-affected habitations", "आर्सेनिक प्रभावित बस्तियाँ", "आर्सेनिकबाधित वस्त्या"), "india-gov", "Jal Jeevan Mission water-quality data."),
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Floods are Bihar's biggest hazard, affecting the north Bihar plain in most years. North Bihar lies in a high seismic zone close to the Himalayan front: the earthquake of 15 January 1934 devastated Munger, Darbhanga and much of north Bihar and Nepal, and the 2015 Nepal earthquake was felt strongly. Lightning kills many people during the monsoon, heatwaves strike the south in May and June, and cold waves and dense fog affect the plains in winter.\n\nVisitors should check flood advisories in the monsoon, and follow crowd advisories at large gatherings such as Chhath on the Ganga ghats and the Pitru Paksha fair at Gaya.",
        "बाढ़ बिहार का सबसे बड़ा ख़तरा है, जो अधिकांश वर्षों में उत्तर बिहार के मैदान को प्रभावित करती है। उत्तर बिहार हिमालय के अग्रभाग के पास ऊँचे भूकंपीय क्षेत्र में है: 15 जनवरी 1934 के भूकंप ने मुंगेर, दरभंगा और उत्तर बिहार व नेपाल के बड़े हिस्से को तबाह किया, और 2015 का नेपाल भूकंप तेज़ी से महसूस हुआ। मानसून में आकाशीय बिजली से बहुत लोग मरते हैं, मई-जून में दक्षिण में लू चलती है, और सर्दियों में मैदानों में शीतलहर और घना कोहरा रहता है।\n\nपर्यटकों को मानसून में बाढ़ संबंधी सलाह देखनी चाहिए, और गंगा घाटों पर छठ और गया में पितृपक्ष मेले जैसे बड़े समागमों में भीड़ संबंधी सलाह माननी चाहिए।",
        "पूर हा बिहारवरील सर्वांत मोठा धोका आहे, जो बहुतेक वर्षी उत्तर बिहारच्या मैदानाला बाधित करतो. उत्तर बिहार हिमालयाच्या आघाडीजवळ अधिक भूकंपप्रवण क्षेत्रात आहे: 15 जानेवारी 1934 च्या भूकंपाने मुंगेर, दरभंगा व उत्तर बिहार आणि नेपाळचा मोठा भाग उद्ध्वस्त केला, आणि 2015 चा नेपाळ भूकंप तीव्रतेने जाणवला. पावसाळ्यात वीज कोसळून अनेक लोक मरण पावतात, मे-जूनमध्ये दक्षिणेत उष्णतेची लाट येते, आणि हिवाळ्यात मैदानांत थंडीची लाट व दाट धुके असते.\n\nपर्यटकांनी पावसाळ्यात पूरविषयक सूचना तपासाव्यात, आणि गंगाघाटांवरील छठ व गया येथील पितृपक्ष मेळ्यासारख्या मोठ्या मेळाव्यांत गर्दीविषयक सूचना पाळाव्यात."),
        conf="Editorial"),
    emergency_table(("Bihar", "बिहार", "बिहार")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official BSDMA address."),
        (L("Lightning deaths by year", "वर्षवार आकाशीय बिजली से मौतें", "वर्षनिहाय वीज कोसळून मृत्यू"), "india-gov", "NCRB Accidental Deaths and Suicides in India."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Bihar has 16 registered Geographical Indications in the GI Registry's list as on 31 December 2025, with no shared entries. Madhubani painting, filed in 2005, is the best known. Applique (khatwa) work, Sujini embroidery and Sikki grass products each appear twice — the original registration of 2006 and a second filed in December 2015 alongside other logo marks. Bhagalpur silk and Manjusha art complete the crafts, while the agricultural and food GIs include Shahi litchi, Mithila makhana, Magahi paan, Bhagalpuri zardalu mango, Katarni and Marcha rice, and Silao khaja.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में बिहार के 16 पंजीकृत भौगोलिक संकेतक हैं, और कोई साझा प्रविष्टि नहीं है। 2005 में दायर मधुबनी चित्रकला सबसे प्रसिद्ध है। एप्लिक (खटवा) काम, सुजनी कढ़ाई और सिक्की घास उत्पाद दो-दो बार आते हैं — 2006 का मूल पंजीकरण और दिसंबर 2015 में अन्य लोगो चिह्नों के साथ दायर दूसरा। भागलपुरी रेशम और मंजूषा कला शिल्पों को पूरा करते हैं, जबकि कृषि और खाद्य जीआई में शाही लीची, मिथिला मखाना, मगही पान, भागलपुरी ज़र्दालू आम, कतरनी और मर्चा चावल, और सिलाव खाजा शामिल हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत बिहारची 16 नोंदणीकृत भौगोलिक मानांकने आहेत, आणि एकही सामायिक नोंद नाही. 2005 मध्ये दाखल झालेली मधुबनी चित्रकला सर्वांत प्रसिद्ध आहे. ऍप्लिक (खटवा) काम, सुजनी भरतकाम व सिक्की गवत उत्पादने प्रत्येकी दोनदा येतात — 2006 ची मूळ नोंदणी आणि डिसेंबर 2015 मध्ये इतर बोधचिन्हांसोबत दाखल झालेली दुसरी. भागलपुरी रेशीम व मंजूषा कला हस्तकला पूर्ण करतात, तर कृषी व खाद्य जीआयमध्ये शाही लिची, मिथिला मखाणा, मगही पान, भागलपुरी जर्दाळू आंबा, कतरनी व मर्चा तांदूळ आणि सिलाव खाजा यांचा समावेश आहे."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Bihar is at the centre of the Buddhist circuit: Bodh Gaya, where the Buddha attained enlightenment, draws pilgrims from across Asia, and Rajgir, Nalanda, Vaishali and Kesariya are linked to his life. Jain pilgrims visit Pawapuri, where Mahavira attained nirvana, and Vaishali, near his birthplace; Sikh pilgrims come to Takht Sri Harmandir Sahib in Patna. Patna's Bihar Museum, Golghar and riverfront, Sher Shah's tomb at Sasaram, the Vikramshila ruins and the forests of Valmiki are other attractions, and the Sonepur fair and Chhath are memorable experiences.",
        "बिहार बौद्ध परिपथ के केंद्र में है: बोधगया, जहाँ बुद्ध को ज्ञान प्राप्त हुआ, पूरे एशिया से तीर्थयात्रियों को खींचता है, और राजगीर, नालंदा, वैशाली और केसरिया उनके जीवन से जुड़े हैं। जैन तीर्थयात्री पावापुरी जाते हैं, जहाँ महावीर ने निर्वाण प्राप्त किया, और उनके जन्मस्थान के पास वैशाली; सिख तीर्थयात्री पटना के तख़्त श्री हरमंदिर साहिब आते हैं। पटना का बिहार संग्रहालय, गोलघर और नदी तट, सासाराम में शेरशाह का मक़बरा, विक्रमशिला के खंडहर और वाल्मीकि के वन अन्य आकर्षण हैं, और सोनपुर मेला और छठ यादगार अनुभव हैं।",
        "बिहार बौद्ध परिक्रमेच्या केंद्रस्थानी आहे: बोधगया, जिथे बुद्धांना ज्ञानप्राप्ती झाली, आशियाभरातून यात्रेकरू खेचते, आणि राजगीर, नालंदा, वैशाली व केसरिया त्यांच्या जीवनाशी जोडलेली आहेत. जैन यात्रेकरू पावापुरीला, जिथे महावीरांना निर्वाण प्राप्त झाले, आणि त्यांच्या जन्मस्थानाजवळील वैशालीला जातात; शीख यात्रेकरू पाटण्यातील तख्त श्री हरमंदिर साहिबला येतात. पाटण्याचे बिहार संग्रहालय, गोलघर व नदीकाठ, सासारामची शेरशहाची कबर, विक्रमशिलेचे अवशेष व वाल्मीकीची जंगले ही इतर आकर्षणे आहेत, आणि सोनपूर जत्रा व छठ हे संस्मरणीय अनुभव आहेत."),
        conf="Editorial"),
    lst("places", [
        it3("bodhgaya", "Bodh Gaya", "बोधगया", "बोधगया", m=("UNESCO; Buddhist pilgrimage", "यूनेस्को; बौद्ध तीर्थ", "युनेस्को; बौद्ध तीर्थ")),
        it3("nalanda", "Nalanda and Rajgir", "नालंदा और राजगीर", "नालंदा व राजगीर", m=("UNESCO; ancient university", "यूनेस्को; प्राचीन विश्वविद्यालय", "युनेस्को; प्राचीन विद्यापीठ")),
        it3("vaishali", "Vaishali and Kesariya", "वैशाली और केसरिया", "वैशाली व केसरिया", m=("Buddhist and Jain sites", "बौद्ध और जैन स्थल", "बौद्ध व जैन स्थळे")),
        it3("patna", "Patna: Bihar Museum, Golghar, Patna Sahib", "पटना: बिहार संग्रहालय, गोलघर, पटना साहिब", "पाटणा: बिहार संग्रहालय, गोलघर, पाटणा साहिब", m=("Capital", "राजधानी", "राजधानी")),
        it3("pawapuri", "Pawapuri", "पावापुरी", "पावापुरी", m=("Jain pilgrimage", "जैन तीर्थ", "जैन तीर्थ")),
        it3("sasaram", "Sasaram", "सासाराम", "सासाराम", m=("Sher Shah's tomb", "शेरशाह का मक़बरा", "शेरशहाची कबर")),
        it3("valmiki", "Valmiki Tiger Reserve", "वाल्मीकि बाघ अभयारण्य", "वाल्मीकी व्याघ्र प्रकल्प", m=("Wildlife", "वन्यजीव", "वन्यजीव")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Patna: Bihar Museum, Golghar, Patna Sahib and the Ganga ghats.", "पटना: बिहार संग्रहालय, गोलघर, पटना साहिब और गंगा घाट।", "पाटणा: बिहार संग्रहालय, गोलघर, पाटणा साहिब व गंगाघाट.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Bodh Gaya and Gaya, with Rajgir.", "बोधगया और गया, साथ में राजगीर।", "बोधगया व गया, सोबत राजगीर.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("The Buddhist circuit: Bodh Gaya, Rajgir, Nalanda, Pawapuri, Vaishali and Kesariya.", "बौद्ध परिपथ: बोधगया, राजगीर, नालंदा, पावापुरी, वैशाली और केसरिया।", "बौद्ध परिक्रमा: बोधगया, राजगीर, नालंदा, पावापुरी, वैशाली व केसरिया.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("brt", "Bihar Tourism (official)", "बिहार पर्यटन (आधिकारिक)", "बिहार पर्यटन (अधिकृत)", url="https://tourism.bihar.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Araria", "अररिया", "अररिया"), ("Arwal", "अरवल", "अरवल"), ("Aurangabad", "औरंगाबाद", "औरंगाबाद"), ("Banka", "बांका", "बांका"), ("Begusarai", "बेगूसराय", "बेगुसराय"),
    ("Bhagalpur", "भागलपुर", "भागलपूर"), ("Bhojpur", "भोजपुर", "भोजपूर"), ("Buxar", "बक्सर", "बक्सर"), ("Darbhanga", "दरभंगा", "दरभंगा"), ("East Champaran", "पूर्वी चंपारण", "पूर्व चंपारण"),
    ("Gaya", "गया", "गया"), ("Gopalganj", "गोपालगंज", "गोपालगंज"), ("Jamui", "जमुई", "जमुई"), ("Jehanabad", "जहानाबाद", "जहानाबाद"), ("Kaimur", "कैमूर", "कैमूर"),
    ("Katihar", "कटिहार", "कटिहार"), ("Khagaria", "खगड़िया", "खगडिया"), ("Kishanganj", "किशनगंज", "किशनगंज"), ("Lakhisarai", "लखीसराय", "लखीसराय"), ("Madhepura", "मधेपुरा", "मधेपुरा"),
    ("Madhubani", "मधुबनी", "मधुबनी"), ("Munger", "मुंगेर", "मुंगेर"), ("Muzaffarpur", "मुज़फ़्फ़रपुर", "मुझफ्फरपूर"), ("Nalanda", "नालंदा", "नालंदा"), ("Nawada", "नवादा", "नवादा"),
    ("Patna", "पटना", "पाटणा"), ("Purnia", "पूर्णिया", "पूर्णिया"), ("Rohtas", "रोहतास", "रोहतास"), ("Saharsa", "सहरसा", "सहरसा"), ("Samastipur", "समस्तीपुर", "समस्तीपूर"),
    ("Saran", "सारण", "सारण"), ("Sheikhpura", "शेखपुरा", "शेखपुरा"), ("Sheohar", "शिवहर", "शिवहर"), ("Sitamarhi", "सीतामढ़ी", "सीतामढी"), ("Siwan", "सिवान", "सिवान"),
    ("Supaul", "सुपौल", "सुपौल"), ("Vaishali", "वैशाली", "वैशाली"), ("West Champaran", "पश्चिमी चंपारण", "पश्चिम चंपारण"),
]
assert len(DISTRICTS) == 38, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("patna", ("Patna", "पटना", "पाटणा"), ("State capital on the Ganga; ancient Pataliputra.", "गंगा पर राज्य की राजधानी; प्राचीन पाटलिपुत्र।", "गंगेकाठची राज्याची राजधानी; प्राचीन पाटलिपुत्र."), ("Capital", "राजधानी", "राजधानी")),
        city("gaya", ("Gaya and Bodh Gaya", "गया और बोधगया", "गया व बोधगया"), ("Pilgrimage city of the Phalgu; Buddhist centre nearby.", "फल्गु पर तीर्थ नगर; पास में बौद्ध केंद्र।", "फल्गूकाठचे तीर्थनगर; जवळच बौद्ध केंद्र."), ("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        city("bhagalpur", ("Bhagalpur", "भागलपुर", "भागलपूर"), ("Silk city; Vikramshila nearby.", "रेशम नगरी; पास में विक्रमशिला।", "रेशीम नगरी; जवळच विक्रमशिला."), ("Silk", "रेशम", "रेशीम")),
        city("muzaffarpur", ("Muzaffarpur", "मुज़फ़्फ़रपुर", "मुझफ्फरपूर"), ("Litchi capital of north Bihar.", "उत्तर बिहार की लीची राजधानी।", "उत्तर बिहारची लिची राजधानी."), ("Agri-trade", "कृषि व्यापार", "कृषी व्यापार")),
        city("darbhanga", ("Darbhanga", "दरभंगा", "दरभंगा"), ("Cultural capital of Mithila; makhana and AIIMS.", "मिथिला की सांस्कृतिक राजधानी; मखाना और एम्स।", "मिथिलेची सांस्कृतिक राजधानी; मखाणा व एम्स."), ("Mithila", "मिथिला", "मिथिला")),
        city("purnia", ("Purnia", "पूर्णिया", "पूर्णिया"), ("Commercial centre of the Kosi–Seemanchal region.", "कोसी–सीमांचल क्षेत्र का वाणिज्यिक केंद्र।", "कोसी–सीमांचल प्रदेशाचे व्यापारी केंद्र."), ("Commerce", "वाणिज्य", "व्यापार")),
        city("begusarai", ("Begusarai", "बेगूसराय", "बेगुसराय"), ("Barauni refinery and fertiliser plant.", "बरौनी रिफ़ाइनरी और उर्वरक संयंत्र।", "बरौनी रिफायनरी व खत कारखाना."), ("Industry", "उद्योग", "उद्योग")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 38 districts (alphabetical)", "38 ज़िले (वर्णानुक्रम)", "38 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Official district list (State notification)", "आधिकारिक ज़िला सूची (राज्य अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य अधिसूचना)"), "india-gov", "Link the State's list of districts."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Bihar has invested in sport in recent years. The Rajgir Sports Complex and the Bihar Sports University at Rajgir hosted the Women's Asian Champions Trophy in hockey in 2024 and the men's Hockey Asia Cup in 2025. Shooter Shreyasi Singh of Jamui won Commonwealth Games gold in 2018. Cricket is widely followed, with the Moin-ul-Haq Stadium in Patna, and the Bihar team returned to the Ranji Trophy in 2018. Traditional rural sports include kabaddi and wrestling in village akharas.",
        "बिहार ने हाल के वर्षों में खेलों में निवेश किया है। राजगीर खेल परिसर और राजगीर के बिहार खेल विश्वविद्यालय ने 2024 में महिला एशियाई चैंपियंस ट्रॉफ़ी हॉकी और 2025 में पुरुष हॉकी एशिया कप की मेज़बानी की। जमुई की निशानेबाज़ श्रेयसी सिंह ने 2018 में राष्ट्रमंडल खेलों में स्वर्ण जीता। क्रिकेट व्यापक रूप से देखा जाता है, पटना में मोइनुल हक़ स्टेडियम है, और बिहार की टीम 2018 में रणजी ट्रॉफ़ी में लौटी। पारंपरिक ग्रामीण खेलों में कबड्डी और गाँव के अखाड़ों में कुश्ती शामिल हैं।",
        "बिहारने अलीकडच्या वर्षांत क्रीडांत गुंतवणूक केली आहे. राजगीर क्रीडा संकुल व राजगीर येथील बिहार क्रीडा विद्यापीठाने 2024 मध्ये महिला आशियाई चॅम्पियन्स करंडक हॉकी व 2025 मध्ये पुरुष हॉकी आशिया चषक आयोजित केला. जमुईच्या नेमबाज श्रेयसी सिंह यांनी 2018 मध्ये राष्ट्रकुल स्पर्धेत सुवर्ण जिंकले. क्रिकेट मोठ्या प्रमाणावर पाहिले जाते, पाटण्यात मोईनुल हक स्टेडियम आहे, आणि बिहारचा संघ 2018 मध्ये रणजी करंडकात परतला. पारंपरिक ग्रामीण खेळांत कबड्डी व गावच्या आखाड्यांतील कुस्ती यांचा समावेश आहे."),
        conf="Editorial"),
    lst("venues", [
        it3("rajgir", "Rajgir Sports Complex", "राजगीर खेल परिसर", "राजगीर क्रीडा संकुल"),
        it3("moinulhaq", "Moin-ul-Haq Stadium, Patna", "मोइनुल हक़ स्टेडियम, पटना", "मोईनुल हक स्टेडियम, पाटणा"),
        it3("patliputra", "Patliputra Sports Complex, Patna", "पाटलिपुत्र खेल परिसर, पटना", "पाटलिपुत्र क्रीडा संकुल, पाटणा"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from Bihar (official list)", "बिहार के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "बिहारचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Bihar State Sports Authority.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("chanakya", ("Chanakya", "चाणक्य", "चाणक्य"), ("Teacher and strategist who helped Chandragupta Maurya found the Maurya empire; associated with the Arthashastra.", "शिक्षक और रणनीतिकार, जिन्होंने चंद्रगुप्त मौर्य को मौर्य साम्राज्य की स्थापना में मदद की; अर्थशास्त्र से जुड़े।", "शिक्षक व रणनीतीकार, ज्यांनी चंद्रगुप्त मौर्यांना मौर्य साम्राज्य स्थापन करण्यास मदत केली; अर्थशास्त्राशी संबंधित."), ("History", "इतिहास", "इतिहास")),
        person("ashoka", ("Ashoka", "अशोक", "अशोक"), ("Maurya emperor who ruled from Pataliputra and spread Buddhism across Asia.", "पाटलिपुत्र से शासन करने वाले मौर्य सम्राट, जिन्होंने एशिया भर में बौद्ध धर्म फैलाया।", "पाटलिपुत्राहून राज्य करणारे मौर्य सम्राट, ज्यांनी आशियाभर बौद्ध धर्म पसरवला."), ("History", "इतिहास", "इतिहास")),
        person("aryabhata", ("Aryabhata", "आर्यभट", "आर्यभट"), ("Mathematician-astronomer who worked at Kusumapura near Pataliputra.", "गणितज्ञ-खगोलविद, जिन्होंने पाटलिपुत्र के पास कुसुमपुर में काम किया।", "गणितज्ञ-खगोलशास्त्रज्ञ, ज्यांनी पाटलिपुत्राजवळील कुसुमपूर येथे कार्य केले."), ("Science", "विज्ञान", "विज्ञान")),
        person("vidyapati", ("Vidyapati", "विद्यापति", "विद्यापती"), ("14th–15th-century Maithili poet of love and devotion.", "14वीं–15वीं सदी के प्रेम और भक्ति के मैथिली कवि।", "चौदाव्या–पंधराव्या शतकातील प्रेम व भक्तीचे मैथिली कवी."), ("Literature", "साहित्य", "साहित्य")),
        person("kunwar", ("Veer Kunwar Singh", "वीर कुंवर सिंह", "वीर कुंवरसिंह"), ("Elderly zamindar of Jagdishpur who led the 1857 revolt in Bihar.", "जगदीशपुर के वृद्ध ज़मींदार, जिन्होंने बिहार में 1857 के विद्रोह का नेतृत्व किया।", "जगदीशपूरचे वयोवृद्ध जमीनदार, ज्यांनी बिहारमध्ये 1857 च्या उठावाचे नेतृत्व केले."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("rajendra", ("Dr Rajendra Prasad", "डॉ. राजेंद्र प्रसाद", "डॉ. राजेंद्र प्रसाद"), ("First President of India, born at Ziradei in Siwan district.", "भारत के पहले राष्ट्रपति, सिवान ज़िले के ज़ीरादेई में जन्मे।", "भारताचे पहिले राष्ट्रपती, सिवान जिल्ह्यातील झिरादेई येथे जन्म."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("jp", ("Jayaprakash Narayan", "जयप्रकाश नारायण", "जयप्रकाश नारायण"), ("Leader of the 1974 'total revolution' movement; Bharat Ratna.", "1974 के 'संपूर्ण क्रांति' आंदोलन के नेता; भारत रत्न।", "1974 च्या 'संपूर्ण क्रांती' आंदोलनाचे नेते; भारतरत्न."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("dinkar", ("Ramdhari Singh 'Dinkar'", "रामधारी सिंह 'दिनकर'", "रामधारी सिंह 'दिनकर'"), ("Hindi poet of national awakening; Jnanpith Award.", "राष्ट्रीय जागरण के हिंदी कवि; ज्ञानपीठ पुरस्कार।", "राष्ट्रीय जागृतीचे हिंदी कवी; ज्ञानपीठ पुरस्कार."), ("Literature", "साहित्य", "साहित्य")),
        person("bhikhari", ("Bhikhari Thakur", "भिखारी ठाकुर", "भिखारी ठाकूर"), ("Bhojpuri playwright and folk artist, creator of Bidesia.", "भोजपुरी नाटककार और लोक कलाकार, बिदेसिया के रचयिता।", "भोजपुरी नाटककार व लोककलाकार, बिदेसियाचे जनक."), ("Theatre", "रंगमंच", "रंगभूमी")),
        person("bismillah", ("Ustad Bismillah Khan", "उस्ताद बिस्मिल्लाह ख़ाँ", "उस्ताद बिस्मिल्ला खाँ"), ("Shehnai maestro born at Dumraon in Buxar district; Bharat Ratna.", "बक्सर ज़िले के डुमराँव में जन्मे शहनाई वादक; भारत रत्न।", "बक्सर जिल्ह्यातील डुमराव येथे जन्मलेले सनईवादक; भारतरत्न."), ("Music", "संगीत", "संगीत")),
        person("karpoori", ("Karpoori Thakur", "कर्पूरी ठाकुर", "कर्पूरी ठाकूर"), ("Former Chief Minister and social-justice leader; Bharat Ratna (2024).", "पूर्व मुख्यमंत्री और सामाजिक न्याय के नेता; भारत रत्न (2024)।", "माजी मुख्यमंत्री व सामाजिक न्यायाचे नेते; भारतरत्न (2024)."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("sharda", ("Sharda Sinha", "शारदा सिन्हा", "शारदा सिन्हा"), ("Folk singer whose Chhath and Maithili–Bhojpuri songs are loved across India.", "लोकगायिका, जिनके छठ और मैथिली–भोजपुरी गीत पूरे भारत में प्रिय हैं।", "लोकगायिका, जिनची छठ व मैथिली–भोजपुरी गाणी भारतभर लोकप्रिय आहेत."), ("Music", "संगीत", "संगीत")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Bihar has one of the largest migrant populations in India. In the 19th century, indentured labourers from the Bhojpuri-speaking districts of Bihar and eastern Uttar Pradesh were taken to Mauritius, Fiji, Trinidad and Tobago, Guyana and Suriname; their descendants keep Bhojpuri songs and festivals alive there. Today millions of workers from Bihar live in Delhi, Punjab, Haryana, Maharashtra, Gujarat and the south, and many go to the Gulf. Students and professionals from Bihar are prominent in the civil services, medicine and engineering across India, and Chhath is now celebrated wherever Biharis live.",
        "बिहार में भारत की सबसे बड़ी प्रवासी आबादियों में से एक है। 19वीं सदी में बिहार और पूर्वी उत्तर प्रदेश के भोजपुरी-भाषी ज़िलों के गिरमिटिया श्रमिकों को मॉरीशस, फ़िजी, त्रिनिदाद और टोबैगो, गयाना और सूरीनाम ले जाया गया; उनके वंशज वहाँ भोजपुरी गीतों और त्योहारों को जीवित रखते हैं। आज बिहार के लाखों श्रमिक दिल्ली, पंजाब, हरियाणा, महाराष्ट्र, गुजरात और दक्षिण में रहते हैं, और बहुत से खाड़ी देशों में जाते हैं। बिहार के छात्र और पेशेवर पूरे भारत में सिविल सेवाओं, चिकित्सा और इंजीनियरिंग में प्रमुख हैं, और छठ अब जहाँ भी बिहारी रहते हैं वहाँ मनाया जाता है।",
        "बिहारमध्ये भारतातील सर्वांत मोठ्या स्थलांतरित लोकसंख्यांपैकी एक आहे. एकोणिसाव्या शतकात बिहार व पूर्व उत्तर प्रदेशच्या भोजपुरीभाषक जिल्ह्यांतील करारबद्ध (गिरमिटिया) कामगारांना मॉरिशस, फिजी, त्रिनिदाद व टोबॅगो, गयाना व सुरिनाम येथे नेले गेले; त्यांचे वंशज तिथे भोजपुरी गाणी व सण जिवंत ठेवतात. आज बिहारचे लाखो कामगार दिल्ली, पंजाब, हरियाणा, महाराष्ट्र, गुजरात व दक्षिणेत राहतात, आणि अनेक जण आखाती देशांत जातात. बिहारचे विद्यार्थी व व्यावसायिक भारतभर नागरी सेवा, वैद्यकशास्त्र व अभियांत्रिकीत आघाडीवर आहेत, आणि छठ आता जिथे जिथे बिहारी राहतात तिथे साजरी होते."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants and internal migrants", "प्रवासियों और आंतरिक प्रवासियों की संख्या", "परदेशी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; MEA."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Bihar portal", "बिहार सरकार पोर्टल", "बिहार शासन संकेतस्थळ", url="https://state.bihar.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Bihar Tourism", "बिहार पर्यटन", "बिहार पर्यटन", url="https://tourism.bihar.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Patna", "पटना", "पाटणा"), "0612"], [L("Gaya", "गया", "गया"), "0631"], [L("Bhagalpur", "भागलपुर", "भागलपूर"), "0641"],
           [L("Muzaffarpur", "मुज़फ़्फ़रपुर", "मुझफ्फरपूर"), "0621"], [L("Darbhanga", "दरभंगा", "दरभंगा"), "06272"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("State e-services portal — verified link", "राज्य ई-सेवा पोर्टल — सत्यापित लिंक", "राज्य ई-सेवा संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "RTPS services portal of the State."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("density", ("Bihar is the most densely populated State, with about 1,106 people per km² in 2011.", "2011 में लगभग 1,106 लोग प्रति वर्ग किमी के साथ बिहार सबसे घनी आबादी वाला राज्य है।", "2011 मध्ये सुमारे 1,106 लोक प्रति चौ.किमीसह बिहार हे सर्वाधिक दाट लोकवस्तीचे राज्य आहे.")),
        triv("unesco", ("Two UNESCO World Heritage Sites — the Mahabodhi temple and Nalanda Mahavihara — are in Bihar.", "दो यूनेस्को विश्व धरोहर स्थल — महाबोधि मंदिर और नालंदा महाविहार — बिहार में हैं।", "दोन युनेस्को जागतिक वारसा स्थळे — महाबोधी मंदिर व नालंदा महाविहार — बिहारमध्ये आहेत."), UNESCO, "unesco-whc"),
        triv("champaran", ("Gandhi's first satyagraha in India was in Champaran, in 1917.", "भारत में गांधी का पहला सत्याग्रह 1917 में चंपारण में हुआ।", "भारतातील गांधीजींचा पहिला सत्याग्रह 1917 मध्ये चंपारणमध्ये झाला.")),
        triv("dolphin", ("The Vikramshila sanctuary near Bhagalpur protects the Ganges river dolphin, India's national aquatic animal.", "भागलपुर के पास विक्रमशिला अभयारण्य भारत के राष्ट्रीय जलीय जीव गंगा डॉल्फ़िन की रक्षा करता है।", "भागलपूरजवळील विक्रमशिला अभयारण्य भारताचा राष्ट्रीय जलचर गंगा डॉल्फिनचे रक्षण करते.")),
        triv("makhana", ("Mithila Makhana is a registered Geographical Indication (filed 2020).", "मिथिला मखाना पंजीकृत भौगोलिक संकेतक है (2020 में दायर)।", "मिथिला मखाणा हे नोंदणीकृत भौगोलिक मानांकन आहे (2020 मध्ये दाखल)."), GI_PDF, "gi-registry"),
        triv("ls", ("The State elects 40 members to the Lok Sabha.", "राज्य से लोकसभा के 40 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 40 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("br mod3 ok")
