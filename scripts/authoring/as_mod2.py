"""Assam modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-AS"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
CAG_AS = "https://www.digitalreports.cag.gov.in/assam/chapter/1"
CM = "https://newsonair.gov.in/senior-bjp-leader-himanta-biswa-sarma-to-be-sworn-in-as-cm-of-assam-in-guwahati-today/"
RES = "https://newsonair.gov.in/assam-cm-himanta-biswa-sarma-tenders-his-resignation-to-governor-in-guwahati/"
NAME = L("Assam", "असम", "आसाम")
asm = read("regions/IN-AS.json")["metrics"]


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Assamese culture was shaped by Srimanta Sankardeva (1449–1568) and his disciple Madhavdeva, whose Ekasarana movement created the satras — Vaishnava monasteries such as those of Majuli and Barpeta — the borgeet devotional songs, the Ankiya Naat plays performed in bhaonas, and Sattriya, recognised as one of India's classical dances. The three Bihus, Bihu dance and song, and the many traditions of the Bodo, Mising, Karbi, Dimasa, Rabha and tea-garden communities add great variety. Jyoti Prasad Agarwala made the first Assamese film, Joymoti, in 1935, and Bhupen Hazarika's songs carried the Brahmaputra's voice across India.\n\nWeaving is part of almost every home: golden muga, white pat and warm eri silk are woven into mekhela chador and the gamosa. Majuli's masks, the bell-metal of Sarthebari, the bamboo-and-palm jaapi hat and Assamese jewellery are registered GIs.",
        "असमिया संस्कृति को श्रीमंत शंकरदेव (1449–1568) और उनके शिष्य माधवदेव ने आकार दिया, जिनके एकशरण आंदोलन ने सत्र — माजुली और बरपेटा जैसे वैष्णव मठ — बरगीत भक्ति गीत, भावना में खेले जाने वाले अंकीया नाट, और भारत के शास्त्रीय नृत्यों में मान्य सत्रीया नृत्य रचे। तीनों बिहू, बिहू नृत्य और गीत, और बोडो, मिसिंग, कार्बी, दिमासा, राभा और चाय बाग़ान समुदायों की अनेक परंपराएँ इसमें बहुत विविधता जोड़ती हैं। ज्योति प्रसाद अग्रवाल ने 1935 में पहली असमिया फ़िल्म 'जयमती' बनाई, और भूपेन हज़ारिका के गीतों ने ब्रह्मपुत्र की आवाज़ पूरे भारत तक पहुँचाई।\n\nबुनाई लगभग हर घर का हिस्सा है: सुनहरा मूगा, सफ़ेद पाट और गर्म एरी रेशम मेखेला चादर और गमोसा में बुना जाता है। माजुली के मुखौटे, सार्थेबाड़ी का काँसा, बाँस और ताड़ की जापी टोपी और असमिया आभूषण पंजीकृत जीआई हैं।",
        "आसामी संस्कृती श्रीमंत शंकरदेव (1449–1568) व त्यांचे शिष्य माधवदेव यांनी घडवली, ज्यांच्या एकशरण चळवळीने सत्र — माजुली व बरपेटासारखे वैष्णव मठ — बरगीत भक्तिगीते, भावनांत सादर होणारी अंकीया नाटके आणि भारताच्या शास्त्रीय नृत्यांत मान्यता असलेले सत्रिया नृत्य निर्माण केले. तिन्ही बिहू, बिहू नृत्य व गाणी, आणि बोडो, मिसिंग, कार्बी, दिमासा, राभा व चहामळा समुदायांच्या अनेक परंपरा यात मोठे वैविध्य आणतात. ज्योती प्रसाद आगरवाला यांनी 1935 मध्ये पहिला आसामी चित्रपट 'जयमती' बनवला, आणि भूपेन हजारिका यांच्या गाण्यांनी ब्रह्मपुत्रेचा आवाज भारतभर पोहोचवला.\n\nविणकाम जवळपास प्रत्येक घराचा भाग आहे: सोनेरी मुगा, पांढरे पाट व उबदार एरी रेशीम मेखेला चादर व गमोशात विणले जाते. माजुलीचे मुखवटे, सार्थेबारीचे काशाचे काम, बांबू व ताडपत्रीची जापी टोपी आणि आसामी दागिने ही नोंदणीकृत जीआय आहेत."),
        conf="Editorial"),
    lst("festivals", [
        fest("rongali", "Rongali (Bohag) Bihu", "रोंगाली (बहाग) बिहू", "रोंगाली (बहाग) बिहू", ("Mid-April", "मध्य अप्रैल", "एप्रिलच्या मध्यात"),
             ("Assamese new year: cattle are bathed, gamosas exchanged, and Bihu dance fills villages and stages.", "असमिया नववर्ष: पशुओं को नहलाया जाता है, गमोसे भेंट होते हैं, और गाँवों व मंचों पर बिहू नृत्य होता है।", "आसामी नववर्ष: गुरांना आंघोळ घातली जाते, गमोसे दिले जातात, आणि गावांत व मंचांवर बिहू नृत्य रंगते.")),
        fest("magh", "Magh (Bhogali) Bihu", "माघ (भोगाली) बिहू", "माघ (भोगाली) बिहू", ("Mid-January", "मध्य जनवरी", "जानेवारीच्या मध्यात"),
             ("Harvest feast; community meals in bamboo huts (bhelaghar) and bonfires (meji) at dawn.", "फ़सल का भोज; बाँस की झोपड़ियों (भेलाघर) में सामूहिक भोज और भोर में अलाव (मेजी)।", "सुगीची मेजवानी; बांबूच्या झोपड्यांत (भेलाघर) सामूहिक भोजन व पहाटे शेकोटी (मेजी).")),
        fest("kati", "Kati (Kongali) Bihu", "काती (कोंगाली) बिहू", "काती (कोंगाली) बिहू", ("Mid-October", "मध्य अक्टूबर", "ऑक्टोबरच्या मध्यात"),
             ("Lamps are lit in paddy fields and at the tulsi plant before the harvest.", "फ़सल से पहले धान के खेतों और तुलसी के पास दीप जलाए जाते हैं।", "सुगीपूर्वी भाताच्या शेतांत व तुळशीजवळ दिवे लावले जातात.")),
        fest("ambubachi", "Ambubachi Mela", "अंबुबाची मेला", "अंबुबाची मेळा", ("June", "जून", "जून"),
             ("Great gathering of pilgrims and sadhus at the Kamakhya temple.", "कामाख्या मंदिर में तीर्थयात्रियों और साधुओं का बड़ा समागम।", "कामाख्या मंदिरात यात्रेकरू व साधूंचा मोठा मेळावा.")),
        fest("raas", "Raas Mahotsav", "रास महोत्सव", "रास महोत्सव", ("November", "नवंबर", "नोव्हेंबर"),
             ("Krishna's raas performed in the satras of Majuli.", "माजुली के सत्रों में कृष्ण की रासलीला।", "माजुलीच्या सत्रांत कृष्णाची रासलीला.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("sattriya", "Sattriya dance", "सत्रीया नृत्य", "सत्रिया नृत्य"), it3("bihu", "Bihu dance", "बिहू नृत्य", "बिहू नृत्य"),
        it3("borgeet", "Borgeet", "बरगीत", "बरगीत"), it3("ankiya", "Ankiya Naat (bhaona)", "अंकीया नाट (भावना)", "अंकीया नाट (भावना)"),
        it3("muga", "Muga silk weaving", "मूगा रेशम बुनाई", "मुगा रेशीम विणकाम"), it3("masks", "Majuli masks", "माजुली मुखौटे", "माजुली मुखवटे"),
        it3("bagurumba", "Bagurumba (Bodo dance)", "बागुरुम्बा (बोडो नृत्य)", "बागुरुम्बा (बोडो नृत्य)"), it3("jhumur", "Jhumur (tea-garden dance)", "झुमुर (चाय बाग़ान नृत्य)", "झुमुर (चहामळ्यांचे नृत्य)"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("tenga", "Masor tenga", "मासोर टेंगा", "मासोर टेंगा", d=("Light, sour fish curry made with tomato, lemon or elephant apple.", "टमाटर, नींबू या ओटेंगा से बनी हल्की खट्टी मछली करी।", "टोमॅटो, लिंबू किंवा ओटेंगा घालून केलेली हलकी आंबट माशांची आमटी.")),
        it3("khar", "Khar", "खार", "खार", d=("Dish made with an alkaline filtrate of burnt banana peel, eaten at the start of a meal.", "जले केले के छिलके के क्षारीय पानी से बना व्यंजन, भोजन की शुरुआत में।", "जाळलेल्या केळ्याच्या सालीच्या क्षारीय पाण्याने बनवलेला पदार्थ, जेवणाच्या सुरुवातीला.")),
        it3("pitha", "Pitha", "पीठा", "पिठा", d=("Rice cakes — til pitha, ghila pitha — made for Bihu.", "बिहू के लिए बनने वाले चावल के पीठे — तिल पीठा, घिला पीठा।", "बिहूसाठी बनवले जाणारे तांदळाचे पिठे — तीळ पिठा, घिला पिठा.")),
        it3("jolpan", "Jolpan", "जलपान", "जलपान", d=("Breakfast of flattened or puffed rice with curd and jaggery.", "दही और गुड़ के साथ चिवड़ा या मुरमुरे का नाश्ता।", "दही व गुळासह पोहे किंवा चुरमुऱ्यांचा न्याहारी.")),
        it3("tea", "Assam tea", "असम चाय", "आसाम चहा", d=("Strong, malty black tea; Assam Orthodox is a registered GI.", "कड़क, माल्टी काली चाय; असम ऑर्थोडॉक्स पंजीकृत जीआई है।", "कडक, माल्टी काळा चहा; आसाम ऑर्थोडॉक्स नोंदणीकृत जीआय आहे.")),
        it3("joha", "Joha rice", "जोहा चावल", "जोहा तांदूळ", d=("Fragrant short-grain rice; a registered GI.", "सुगंधित छोटे दाने का चावल; पंजीकृत जीआई।", "सुगंधी लहान दाण्याचा तांदूळ; नोंदणीकृत जीआय.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("mekhela", "Mekhela chador", "मेखेला चादर", "मेखेला चादर", d=("Two-piece women's dress, often of muga or pat silk.", "महिलाओं की दो-टुकड़ा पोशाक, अक्सर मूगा या पाट रेशम की।", "स्त्रियांचा दोन भागांचा पोशाख, अनेकदा मुगा किंवा पाट रेशमाचा.")),
        it3("dhoti", "Dhoti, gamosa and seleng", "धोती, गमोसा और सेलेंग", "धोतर, गमोसा व सेलेंग", d=("Men's traditional dress for Bihu and ceremonies.", "बिहू और समारोहों के लिए पुरुषों की पारंपरिक पोशाक।", "बिहू व समारंभांसाठी पुरुषांचा पारंपरिक पोशाख.")),
        it3("dokhona", "Dokhona", "दोखोना", "दोखोना", d=("Bodo women's wrap, woven in bright colours; a registered GI.", "बोडो महिलाओं का चटख रंगों में बुना वस्त्र; पंजीकृत जीआई।", "बोडो स्त्रियांचे चमकदार रंगांत विणलेले वस्त्र; नोंदणीकृत जीआय.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
ur = AP["plfs_ur_15plus_psss"]["AS"]; lf = AP["plfs_lfpr_2025"]["AS"]
module(R, "economy", [
    prose("p1", L(
        f"Assam's GSDP at current prices was ₹6,43,667 crore in FY2024-25 and per capita income ₹1,59,185, according to the Comptroller and Auditor General's State Finances Audit Report, which notes that per capita income remained below the national average. The same report puts the tertiary sector at about 38% of GSDP, the primary sector at 33% and the secondary sector at 20% in FY2024-25. Tea is the signature industry — Assam grows a large share of India's tea on hundreds of estates and many small gardens — and the State has oil and gas fields in Upper Assam, with refineries at Digboi, Guwahati, Bongaigaon and Numaligarh and a petrochemical complex at Lepetkata. Rice, fish, silk, bamboo and tourism support many livelihoods, and a semiconductor assembly plant at Jagiroad marks a new industry.\n\nThe PLFS unemployment rate rose from {ur['2022']}% in 2022 to {ur['2024']}% in 2024 before easing to {ur['2025']}% in 2025; {lf['female']}% of women aged 15 and above were in the labour force.",
        f"नियंत्रक एवं महालेखापरीक्षक की राज्य वित्त लेखापरीक्षा रिपोर्ट के अनुसार वित्त वर्ष 2024-25 में असम का प्रचलित मूल्यों पर जीएसडीपी ₹6,43,667 करोड़ और प्रति व्यक्ति आय ₹1,59,185 थी; रिपोर्ट के अनुसार प्रति व्यक्ति आय राष्ट्रीय औसत से कम रही। इसी रिपोर्ट के अनुसार वित्त वर्ष 2024-25 में तृतीयक क्षेत्र जीएसडीपी का लगभग 38%, प्राथमिक क्षेत्र 33% और द्वितीयक क्षेत्र 20% था। चाय पहचान वाला उद्योग है — असम सैकड़ों बाग़ानों और कई छोटे बाग़ों में भारत की चाय का बड़ा हिस्सा उगाता है — और ऊपरी असम में तेल व गैस क्षेत्र हैं, डिगबोई, गुवाहाटी, बोंगाईगाँव और नुमालीगढ़ में रिफ़ाइनरियाँ और लेपेटकाटा में पेट्रोरसायन परिसर। धान, मछली, रेशम, बाँस और पर्यटन बहुत से लोगों की आजीविका हैं, और जागीरोड में सेमीकंडक्टर असेंबली संयंत्र एक नया उद्योग है।\n\nपीएलएफ़एस बेरोज़गारी दर 2022 के {ur['2022']}% से बढ़कर 2024 में {ur['2024']}% हुई और 2025 में घटकर {ur['2025']}% रही; 15 वर्ष से अधिक आयु की {lf['female']}% महिलाएँ श्रम बल में थीं।",
        f"नियंत्रक व महालेखापरीक्षकांच्या राज्य वित्त लेखापरीक्षा अहवालानुसार आ.व. 2024-25 मध्ये आसामचे चालू किमतींनुसार जीएसडीपी ₹6,43,667 कोटी व दरडोई उत्पन्न ₹1,59,185 होते; अहवालानुसार दरडोई उत्पन्न राष्ट्रीय सरासरीपेक्षा कमी राहिले. याच अहवालानुसार आ.व. 2024-25 मध्ये तृतीयक क्षेत्राचा जीएसडीपीत सुमारे 38%, प्राथमिक क्षेत्राचा 33% व द्वितीयक क्षेत्राचा 20% वाटा होता. चहा हा ओळख असलेला उद्योग आहे — आसाम शेकडो मळ्यांत व अनेक लहान बागांत भारतातील चहाचा मोठा वाटा पिकवतो — आणि वरच्या आसाममध्ये तेल व वायूक्षेत्रे आहेत, डिगबोई, गुवाहाटी, बोंगाईगाव व नुमालीगड येथे शुद्धीकरण कारखाने व लेपेटकाटा येथे पेट्रोरसायन संकुल. भात, मासे, रेशीम, बांबू व पर्यटन अनेकांच्या उपजीविकेचा आधार आहेत, आणि जागीरोड येथील सेमीकंडक्टर जोडणी प्रकल्प हा नवा उद्योग आहे.\n\nपीएलएफएस बेरोजगारी दर 2022 मधील {ur['2022']}% वरून 2024 मध्ये {ur['2024']}% पर्यंत वाढला व 2025 मध्ये {ur['2025']}% वर आला; 15 वर्षांवरील {lf['female']}% स्त्रिया श्रमशक्तीत होत्या."),
        sources=["cag", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"), asm["gsdpCurrent"], "rupeeCrore", "higher-is-better",
             previous=dp(339803, "₹ crore", "FY2020-21", "fy", "cag", CAG_AS, rev="revised", base=CUR, note="CAG SFAR 2024-25, Table 1.2.")),
        fact("pc", L("Per capita income, current prices", "प्रति व्यक्ति आय, प्रचलित मूल्य", "दरडोई उत्पन्न, चालू किमती"), asm["perCapitaNsdpCurrent"], "rupee", "higher-is-better",
             previous=dp(86947, "₹", "FY2020-21", "fy", "cag", CAG_AS, rev="revised", base=CUR, note="CAG SFAR 2024-25.")),
        *plfs_facts("AS", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    plfs_series("AS", NAME),
    lst("sectors-key", [
        it3("tea", "Tea", "चाय", "चहा", d=("Estates and small growers across the Brahmaputra valley; Assam Orthodox GI.", "ब्रह्मपुत्र घाटी भर में बाग़ान और छोटे उत्पादक; असम ऑर्थोडॉक्स जीआई।", "ब्रह्मपुत्रा खोऱ्यात मळे व लहान उत्पादक; आसाम ऑर्थोडॉक्स जीआय.")),
        it3("oil", "Oil, gas and refining", "तेल, गैस और शोधन", "तेल, वायू व शुद्धीकरण", d=("Digboi, Duliajan and Sivasagar fields; four refineries.", "डिगबोई, दुलियाजान और शिवसागर क्षेत्र; चार रिफ़ाइनरियाँ।", "डिगबोई, दुलियाजान व शिवसागर क्षेत्रे; चार शुद्धीकरण कारखाने.")),
        it3("rice", "Rice and fisheries", "धान और मत्स्य पालन", "भात व मत्स्यव्यवसाय", d=("Sali, ahu and boro rice; beel and river fisheries.", "शाली, आहू और बोरो धान; बील और नदी मत्स्य पालन।", "शाली, आहू व बोरो भात; बील व नदी मत्स्यव्यवसाय.")),
        it3("silk", "Silk and handloom", "रेशम और हथकरघा", "रेशीम व हातमाग", d=("Muga, eri and pat silk; Sualkuchi weaving town.", "मूगा, एरी और पाट रेशम; सुआलकुची बुनकर नगर।", "मुगा, एरी व पाट रेशीम; सुआलकुची विणकर नगर.")),
        it3("semi", "Electronics", "इलेक्ट्रॉनिक्स", "इलेक्ट्रॉनिक्स", d=("Semiconductor assembly and test plant at Jagiroad.", "जागीरोड में सेमीकंडक्टर असेंबली और परीक्षण संयंत्र।", "जागीरोड येथे सेमीकंडक्टर जोडणी व चाचणी प्रकल्प.")),
        it3("tourism", "Tourism", "पर्यटन", "पर्यटन", d=("Kaziranga, Manas, Majuli and Kamakhya.", "काज़ीरंगा, मानस, माजुली और कामाख्या।", "काझीरंगा, मानस, माजुली व कामाख्या.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("GSDP series and sectoral GSVA (MoSPI)", "जीएसडीपी शृंखला और क्षेत्रवार जीएसवीए (मोस्पी)", "जीएसडीपी मालिका व क्षेत्रनिहाय जीएसव्हीए (मोस्पी)"), "mospi", "MoSPI's state-wise API returned no Assam series at access time; use the Assam Economic Survey or DES Assam."),
        (L("Tea production and share of India", "चाय उत्पादन और भारत में हिस्सा", "चहा उत्पादन व भारतातील वाटा"), "india-gov", "Tea Board of India statistics."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "cag", "CAG SFAR / RBI State Finances."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Assam has a unicameral legislature, the 126-member Legislative Assembly at Dispur. The State elects 14 members to the Lok Sabha and 7 to the Rajya Sabha. Under the Sixth Schedule of the Constitution, the Bodoland Territorial Council, the Karbi Anglong Autonomous Council and the Dima Hasao Autonomous Council have their own legislative and executive powers over many subjects.\n\nIn the Assembly election of 2026, the BJP-led NDA won 102 of the 126 seats — the BJP 82, the Asom Gana Parishad 10 and the Bodoland People's Front 10 (News On AIR). Himanta Biswa Sarma was sworn in for a second consecutive term as Chief Minister on 12 May 2026. Ranjeet Kumar Dass was elected Speaker of the 16th Assembly, and Lakshman Prasad Acharya has been Governor since July 2024.",
        "असम में एकसदनीय विधानमंडल है, दिसपुर में 126 सदस्यों वाली विधानसभा। राज्य से लोकसभा के 14 और राज्यसभा के 7 सदस्य चुने जाते हैं। संविधान की छठी अनुसूची के तहत बोडोलैंड प्रादेशिक परिषद, कार्बी आंगलोंग स्वायत्त परिषद और दिमा हसाओ स्वायत्त परिषद को कई विषयों पर अपनी विधायी और कार्यकारी शक्तियाँ प्राप्त हैं।\n\n2026 के विधानसभा चुनाव में भाजपा के नेतृत्व वाले राजग ने 126 में से 102 सीटें जीतीं — भाजपा 82, असम गण परिषद 10 और बोडोलैंड पीपुल्स फ़्रंट 10 (न्यूज़ ऑन एआईआर)। हिमंत बिस्व सरमा ने 12 मई 2026 को लगातार दूसरी बार मुख्यमंत्री पद की शपथ ली। रंजीत कुमार दास 16वीं विधानसभा के अध्यक्ष चुने गए, और लक्ष्मण प्रसाद आचार्य जुलाई 2024 से राज्यपाल हैं।",
        "आसाममध्ये एकसदनी विधिमंडळ आहे, दिसपूरमधील 126 सदस्यांची विधानसभा. राज्यातून लोकसभेवर 14 व राज्यसभेवर 7 सदस्य निवडले जातात. संविधानाच्या सहाव्या अनुसूचीअंतर्गत बोडोलँड प्रादेशिक परिषद, कार्बी आंगलोंग स्वायत्त परिषद व दिमा हसाओ स्वायत्त परिषदेला अनेक विषयांवर स्वतःचे विधायी व कार्यकारी अधिकार आहेत.\n\n2026 च्या विधानसभा निवडणुकीत भाजपच्या नेतृत्वाखालील रालोआने 126 पैकी 102 जागा जिंकल्या — भाजप 82, आसाम गण परिषद 10 व बोडोलँड पीपल्स फ्रंट 10 (न्यूज ऑन एआयआर). हिमंत बिस्व सरमा यांनी 12 मे 2026 रोजी सलग दुसऱ्यांदा मुख्यमंत्रिपदाची शपथ घेतली. रंजीत कुमार दास 16 व्या विधानसभेचे अध्यक्ष निवडले गेले, आणि लक्ष्मण प्रसाद आचार्य जुलै 2024 पासून राज्यपाल आहेत."),
        sources=["newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("noa", "News On AIR: Himanta Biswa Sarma sworn in (12 May 2026)", "न्यूज़ ऑन एआईआर: हिमंत बिस्व सरमा ने शपथ ली (12 मई 2026)", "न्यूज ऑन एआयआर: हिमंत बिस्व सरमा यांचा शपथविधी (12 मे 2026)", url=CM, src="newsonair"),
        it3("res", "News On AIR: outgoing CM tenders resignation after results (6 May 2026)", "न्यूज़ ऑन एआईआर: परिणामों के बाद निवर्तमान मुख्यमंत्री का इस्तीफ़ा (6 मई 2026)", "न्यूज ऑन एआयआर: निकालांनंतर मावळत्या मुख्यमंत्र्यांचा राजीनामा (6 मे 2026)", url=RES, src="newsonair"),
        it3("portal", "Government of Assam", "असम सरकार", "आसाम शासन", url="https://assam.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2026 Assembly election — full party-wise result and vote shares", "2026 विधानसभा चुनाव — दलवार पूरा परिणाम और मत प्रतिशत", "2026 विधानसभा निवडणूक — पक्षनिहाय संपूर्ण निकाल व मतटक्केवारी"), "eci", "ECI statistical report for Assam 2026."),
        (L("Council of Ministers (full list)", "मंत्रिपरिषद (पूरी सूची)", "मंत्रिमंडळ (संपूर्ण यादी)"), "india-gov", "Government of Assam notification."),
        (L("Leader of Opposition — official notice", "नेता प्रतिपक्ष — आधिकारिक सूचना", "विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "Assembly secretariat."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "The Bogibeel rail-cum-road bridge, opened in December 2018 after two decades of work, transformed travel between the north and south banks of the Brahmaputra in Upper Assam. Tata's ₹27,000 crore chip assembly and test plant at Jagiroad, approved under the India Semiconductor Mission, is the State's largest private investment. Other large works include new Brahmaputra bridges, the expansion of the Numaligarh refinery and highway four-laning. Each card shows its source and the date it was checked.",
        "दो दशक के काम के बाद दिसंबर 2018 में खुले बोगीबील रेल-सह-सड़क पुल ने ऊपरी असम में ब्रह्मपुत्र के उत्तरी और दक्षिणी तटों के बीच यात्रा बदल दी। भारत सेमीकंडक्टर मिशन के तहत स्वीकृत, जागीरोड में टाटा का ₹27,000 करोड़ का चिप असेंबली और परीक्षण संयंत्र राज्य का सबसे बड़ा निजी निवेश है। अन्य बड़े कार्यों में ब्रह्मपुत्र पर नए पुल, नुमालीगढ़ रिफ़ाइनरी का विस्तार और राजमार्गों का चौड़ीकरण शामिल है। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "दोन दशकांच्या कामानंतर डिसेंबर 2018 मध्ये खुल्या झालेल्या बोगीबील रेल्वे-सह-रस्ता पुलाने वरच्या आसाममध्ये ब्रह्मपुत्रेच्या उत्तर व दक्षिण किनाऱ्यांदरम्यानचा प्रवास बदलून टाकला. भारत सेमीकंडक्टर मिशनअंतर्गत मंजूर, जागीरोड येथील टाटांचा ₹27,000 कोटींचा चिप जोडणी व चाचणी प्रकल्प ही राज्यातील सर्वांत मोठी खासगी गुंतवणूक आहे. इतर मोठ्या कामांत ब्रह्मपुत्रेवरील नवे पूल, नुमालीगड रिफायनरीचा विस्तार व महामार्ग चौपदरीकरण यांचा समावेश आहे. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["new-india-samachar", "pib"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Numaligarh refinery expansion — status", "नुमालीगढ़ रिफ़ाइनरी विस्तार — स्थिति", "नुमालीगड रिफायनरी विस्तार — स्थिती"), "india-gov", "Ministry of Petroleum and Natural Gas."),
        (L("Guwahati–North Guwahati and other Brahmaputra bridges — status", "गुवाहाटी–उत्तर गुवाहाटी और अन्य ब्रह्मपुत्र पुल — स्थिति", "गुवाहाटी–उत्तर गुवाहाटी व इतर ब्रह्मपुत्रा पूल — स्थिती"), "india-gov", "Assam PWD / MoRTH."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Lokpriya Gopinath Bordoloi International Airport at Guwahati is the busiest airport in the north-east; Dibrugarh, Jorhat, Tezpur, Silchar and Lakhimpur (Lilabari) have domestic flights. The Northeast Frontier Railway is headquartered at Maligaon in Guwahati, and the main line from West Bengal runs through Guwahati to Dibrugarh, with branches to the Barak valley and the other north-eastern States. Bridges over the Brahmaputra — Saraighat at Guwahati, the Kolia Bhomora Setu at Tezpur, Bogibeel and the Bhupen Hazarika Setu (Dhola–Sadiya) — tie the valley together, and the river itself is National Waterway 2.",
        "गुवाहाटी का लोकप्रिय गोपीनाथ बरदलै अंतरराष्ट्रीय हवाई अड्डा पूर्वोत्तर का सबसे व्यस्त हवाई अड्डा है; डिब्रूगढ़, जोरहाट, तेजपुर, सिलचर और लखीमपुर (लीलाबाड़ी) से घरेलू उड़ानें हैं। पूर्वोत्तर सीमांत रेलवे का मुख्यालय गुवाहाटी के मालीगाँव में है, और पश्चिम बंगाल से मुख्य लाइन गुवाहाटी से डिब्रूगढ़ तक जाती है, जिसकी शाखाएँ बराक घाटी और अन्य पूर्वोत्तर राज्यों तक हैं। ब्रह्मपुत्र पर पुल — गुवाहाटी का सराईघाट, तेजपुर का कलिया भोमरा सेतु, बोगीबील और भूपेन हज़ारिका सेतु (ढोला–सदिया) — घाटी को जोड़ते हैं, और नदी स्वयं राष्ट्रीय जलमार्ग 2 है।",
        "गुवाहाटीचे लोकप्रिय गोपीनाथ बरदलै आंतरराष्ट्रीय विमानतळ हे ईशान्येतील सर्वांत व्यस्त विमानतळ आहे; डिब्रुगड, जोरहाट, तेजपूर, सिलचर व लखीमपूर (लीलाबारी) येथून देशांतर्गत उड्डाणे आहेत. ईशान्य सीमा रेल्वेचे मुख्यालय गुवाहाटीतील मालीगाव येथे आहे, आणि पश्चिम बंगालमधून मुख्य मार्ग गुवाहाटीमार्गे डिब्रुगडपर्यंत जातो, ज्याच्या शाखा बराक खोरे व इतर ईशान्य राज्यांपर्यंत आहेत. ब्रह्मपुत्रेवरील पूल — गुवाहाटीचा सराईघाट, तेजपूरचा कलिया भोमरा सेतू, बोगीबील व भूपेन हजारिका सेतू (ढोला–सदिया) — खोरे जोडतात, आणि नदी स्वतः राष्ट्रीय जलमार्ग 2 आहे."),
        conf="Editorial"),
    lst("airports", [
        it3("gau", "Lokpriya Gopinath Bordoloi International Airport, Guwahati", "लोकप्रिय गोपीनाथ बरदलै अंतरराष्ट्रीय हवाई अड्डा, गुवाहाटी", "लोकप्रिय गोपीनाथ बरदलै आंतरराष्ट्रीय विमानतळ, गुवाहाटी", m=("GAU", "GAU", "GAU")),
        it3("dib", "Dibrugarh", "डिब्रूगढ़", "डिब्रुगड", m=("DIB", "DIB", "DIB")),
        it3("ixs", "Silchar", "सिलचर", "सिलचर", m=("IXS", "IXS", "IXS")),
        it3("jrh", "Jorhat", "जोरहाट", "जोरहाट", m=("JRH", "JRH", "JRH")),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Assam is one of India's oldest oil and gas producers: Oil India Limited is headquartered at Duliajan, and ONGC works fields around Sivasagar. Natural gas fuels power stations at Namrup and elsewhere, and NTPC's coal plant at Bongaigaon adds to supply. The Lower Subansiri hydro-electric project on the Assam–Arunachal border is one of India's largest, and the State is adding solar capacity.",
        "असम भारत के सबसे पुराने तेल और गैस उत्पादकों में से है: ऑयल इंडिया लिमिटेड का मुख्यालय दुलियाजान में है, और ओएनजीसी शिवसागर के आसपास के क्षेत्रों में काम करता है। प्राकृतिक गैस नामरूप और अन्य स्थानों के बिजलीघरों को ईंधन देती है, और बोंगाईगाँव में एनटीपीसी का कोयला संयंत्र आपूर्ति बढ़ाता है। असम–अरुणाचल सीमा पर निचली सुबनसिरी जलविद्युत परियोजना भारत की सबसे बड़ी परियोजनाओं में से है, और राज्य सौर क्षमता जोड़ रहा है।",
        "आसाम हा भारतातील सर्वांत जुन्या तेल व वायू उत्पादकांपैकी एक आहे: ऑइल इंडिया लिमिटेडचे मुख्यालय दुलियाजान येथे आहे, आणि ओएनजीसी शिवसागरभोवतीच्या क्षेत्रांत काम करते. नैसर्गिक वायू नामरूप व इतर ठिकाणच्या वीजकेंद्रांना इंधन पुरवतो, आणि बोंगाईगाव येथील एनटीपीसीचा कोळसा प्रकल्प पुरवठ्यात भर घालतो. आसाम–अरुणाचल सीमेवरील लोअर सुबनसिरी जलविद्युत प्रकल्प हा भारतातील सर्वांत मोठ्या प्रकल्पांपैकी एक आहे, आणि राज्य सौरक्षमता वाढवत आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Crude oil and gas production", "कच्चा तेल और गैस उत्पादन", "कच्चे तेल व वायू उत्पादन"), "india-gov", "Ministry of Petroleum and Natural Gas statistics."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Guwahati is the north-east's main technology and start-up centre, with incubators at IIT Guwahati and an IT park at Amingaon. The Jagiroad semiconductor plant is expected to bring electronics manufacturing to the region. The State runs many services online, and mobile connectivity has expanded across the valleys, though hill and char areas remain less connected.",
        "गुवाहाटी पूर्वोत्तर का मुख्य प्रौद्योगिकी और स्टार्टअप केंद्र है, जहाँ आईआईटी गुवाहाटी में इनक्यूबेटर और अमीनगाँव में आईटी पार्क है। जागीरोड सेमीकंडक्टर संयंत्र से क्षेत्र में इलेक्ट्रॉनिक्स विनिर्माण आने की उम्मीद है। राज्य कई सेवाएँ ऑनलाइन देता है, और घाटियों में मोबाइल कनेक्टिविटी बढ़ी है, हालाँकि पहाड़ी और चर क्षेत्र कम जुड़े हैं।",
        "गुवाहाटी हे ईशान्येचे मुख्य तंत्रज्ञान व स्टार्टअप केंद्र आहे, जिथे आयआयटी गुवाहाटीत इन्क्युबेटर व अमीनगाव येथे आयटी पार्क आहे. जागीरोड सेमीकंडक्टर प्रकल्पामुळे प्रदेशात इलेक्ट्रॉनिक्स उत्पादन येण्याची अपेक्षा आहे. राज्य अनेक सेवा ऑनलाइन देते, आणि खोऱ्यांत मोबाइल जोडणी वाढली आहे, तरी डोंगरी व चर भाग कमी जोडलेले आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Assam circle)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("AS", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["AS"]
module(R, "education", [
    prose("p1", L(
        f"Assam's higher-education gross enrolment ratio (ages 18–23) was 16.9% in 2021-22 in AISHE, slightly lower than the 17.6% of 2017-18 and well below the national 28.4%; women's GER ({gf}%) was higher than men's ({gm}%). The State had 30 universities and 607 colleges. Literacy rose from 63.3% in 2001 to 72.2% in 2011.\n\nCotton College in Guwahati (1901, now Cotton University) and Gauhati University (1948) are the oldest institutions, and Dibrugarh University (1965) serves Upper Assam. IIT Guwahati, AIIMS Guwahati, NIT Silchar, the central universities at Tezpur and Silchar, Assam Agricultural University at Jorhat and the National Law University and Judicial Academy are other major institutions.",
        f"एआईएसएचई के अनुसार 2021-22 में असम का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) 16.9% था, जो 2017-18 के 17.6% से थोड़ा कम और राष्ट्रीय 28.4% से काफ़ी नीचे है; महिलाओं का जीईआर ({gf}%) पुरुषों ({gm}%) से अधिक था। राज्य में 30 विश्वविद्यालय और 607 कॉलेज थे। साक्षरता 2001 के 63.3% से बढ़कर 2011 में 72.2% हुई।\n\nगुवाहाटी का कॉटन कॉलेज (1901, अब कॉटन विश्वविद्यालय) और गुवाहाटी विश्वविद्यालय (1948) सबसे पुराने संस्थान हैं, और डिब्रूगढ़ विश्वविद्यालय (1965) ऊपरी असम को सेवा देता है। आईआईटी गुवाहाटी, एम्स गुवाहाटी, एनआईटी सिलचर, तेजपुर और सिलचर के केंद्रीय विश्वविद्यालय, जोरहाट का असम कृषि विश्वविद्यालय और राष्ट्रीय विधि विश्वविद्यालय एवं न्यायिक अकादमी अन्य प्रमुख संस्थान हैं।",
        f"एआयएसएचईनुसार 2021-22 मध्ये आसामचे उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) 16.9% होते, 2017-18 मधील 17.6% पेक्षा किंचित कमी व राष्ट्रीय 28.4% पेक्षा बरेच कमी; स्त्रियांचे जीईआर ({gf}%) पुरुषांपेक्षा ({gm}%) अधिक होते. राज्यात 30 विद्यापीठे व 607 महाविद्यालये होती. साक्षरता 2001 मधील 63.3% वरून 2011 मध्ये 72.2% झाली.\n\nगुवाहाटीचे कॉटन महाविद्यालय (1901, आता कॉटन विद्यापीठ) व गुवाहाटी विद्यापीठ (1948) या सर्वांत जुन्या संस्था आहेत, आणि डिब्रुगड विद्यापीठ (1965) वरच्या आसामला सेवा देते. आयआयटी गुवाहाटी, एम्स गुवाहाटी, एनआयटी सिलचर, तेजपूर व सिलचरची केंद्रीय विद्यापीठे, जोरहाटचे आसाम कृषी विद्यापीठ व राष्ट्रीय विधी विद्यापीठ आणि न्यायिक अकादमी या इतर प्रमुख संस्था आहेत."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("cotton", "Cotton University", "कॉटन विश्वविद्यालय", "कॉटन विद्यापीठ", m=("Guwahati, 1901", "गुवाहाटी, 1901", "गुवाहाटी, 1901")),
        it3("gu", "Gauhati University", "गुवाहाटी विश्वविद्यालय", "गुवाहाटी विद्यापीठ", m=("Guwahati, 1948", "गुवाहाटी, 1948", "गुवाहाटी, 1948")),
        it3("iitg", "IIT Guwahati", "आईआईटी गुवाहाटी", "आयआयटी गुवाहाटी", m=("North Guwahati", "उत्तर गुवाहाटी", "उत्तर गुवाहाटी")),
        it3("aiimsg", "AIIMS Guwahati", "एम्स गुवाहाटी", "एम्स गुवाहाटी", m=("Changsari", "चांगसारी", "चांगसारी")),
        it3("tu", "Tezpur University", "तेजपुर विश्वविद्यालय", "तेजपूर विद्यापीठ", m=("Central university", "केंद्रीय विश्वविद्यालय", "केंद्रीय विद्यापीठ")),
        it3("nits", "NIT Silchar", "एनआईटी सिलचर", "एनआयटी सिलचर", m=("Silchar", "सिलचर", "सिलचर")),
        it3("aau", "Assam Agricultural University", "असम कृषि विश्वविद्यालय", "आसाम कृषी विद्यापीठ", m=("Jorhat", "जोरहाट", "जोरहाट")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Literacy by sex (Census 2011)", "लिंग के अनुसार साक्षरता (जनगणना 2011)", "लिंगनिहाय साक्षरता (जनगणना 2011)"), "census", "Primary Census Abstract."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["AS"]
module(R, "health", [
    prose("p1", L(
        f"Assam's infant mortality rate fell from 58 per 1,000 live births in 2010 to 36 in 2020, still above the national 28. The birth rate was 20.8 per 1,000 in 2020 and the death rate 6.2. Life expectancy at birth was 66.9 years in 2014-18 (men 66.1, women 67.9), below the national 69.4. Child nutrition is a concern: in NFHS-5, {n['stunted'][1]:.1f}% of children under five were stunted, and wasting ({n['wasted'][1]:.1f}%) and underweight ({n['underweight'][1]:.1f}%) both rose from NFHS-4. About {n['institutional_N5']:.1f}% of births took place in health facilities, below the national 88.6%; tea-garden and char communities face particular gaps in care.\n\nGauhati Medical College and AIIMS Guwahati are the main referral centres, and the Dr B. Borooah Cancer Institute in Guwahati anchors a network of cancer hospitals across the State.",
        f"असम की शिशु मृत्यु दर 2010 में प्रति 1,000 जीवित जन्म पर 58 से घटकर 2020 में 36 हो गई, जो अब भी राष्ट्रीय 28 से ऊपर है। 2020 में जन्म दर प्रति 1,000 पर 20.8 और मृत्यु दर 6.2 थी। 2014-18 में जन्म के समय जीवन प्रत्याशा 66.9 वर्ष थी (पुरुष 66.1, महिलाएँ 67.9), जो राष्ट्रीय 69.4 से कम है। बाल पोषण चिंता का विषय है: एनएफ़एचएस-5 में पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने थे, और दुबलापन ({n['wasted'][1]:.1f}%) और कम वज़न ({n['underweight'][1]:.1f}%) दोनों एनएफ़एचएस-4 से बढ़े। लगभग {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, जो राष्ट्रीय 88.6% से कम है; चाय बाग़ान और चर समुदायों को देखभाल में विशेष कमियों का सामना करना पड़ता है।\n\nगुवाहाटी मेडिकल कॉलेज और एम्स गुवाहाटी मुख्य रेफ़रल केंद्र हैं, और गुवाहाटी का डॉ. बी. बरुआ कैंसर संस्थान राज्य भर के कैंसर अस्पतालों के नेटवर्क का केंद्र है।",
        f"आसामचा अर्भक मृत्युदर 2010 मध्ये दर 1,000 जिवंत जन्मांमागे 58 वरून 2020 मध्ये 36 वर आला, तरी तो राष्ट्रीय 28 पेक्षा अधिक आहे. 2020 मध्ये जन्मदर दर 1,000 मागे 20.8 व मृत्युदर 6.2 होता. 2014-18 मध्ये जन्मतः आयुर्मान 66.9 वर्षे होते (पुरुष 66.1, स्त्रिया 67.9), राष्ट्रीय 69.4 पेक्षा कमी. बालपोषण चिंतेचा विषय आहे: एनएफएचएस-5 मध्ये पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी होती, आणि कृशता ({n['wasted'][1]:.1f}%) व कमी वजन ({n['underweight'][1]:.1f}%) दोन्ही एनएफएचएस-4 पेक्षा वाढले. सुमारे {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, राष्ट्रीय 88.6% पेक्षा कमी; चहामळा व चर समुदायांना आरोग्यसेवेत विशेष उणिवांना तोंड द्यावे लागते.\n\nगुवाहाटी वैद्यकीय महाविद्यालय व एम्स गुवाहाटी ही मुख्य संदर्भ केंद्रे आहेत, आणि गुवाहाटीची डॉ. बी. बरुआ कर्करोग संस्था राज्यभरातील कर्करोग रुग्णालयांच्या जाळ्याचे केंद्र आहे."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(36, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(58, "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(20.8, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020 (death rate 6.2); 23.2 in 2010."), "number",
             previous=dp(23.2, "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(66.9, "years", "2014-18", "survey", "srs", ESI_LE, note="SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male 66.1, female 67.9)."), "number", "higher-is-better",
             previous=dp(63.9, "years", "2010-14", "survey", "srs", ESI_LE), national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("AS"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin; the PIB summary used here lists only States that met the SDG target."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("as mod2 ok")
