"""Sikkim modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-SK"
sk = read("regions/IN-SK.json")["metrics"]; ind = read("india.json")["metrics"]
C = research("census_b5plus.json"); F = C["forest"]["SK"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Forests cover about 47% of Sikkim (ISFR 2023); above them lie alpine meadows, rock and permanent snow. Within a few kilometres the vegetation changes from tropical sal and bamboo in the lower Teesta valley to oak, magnolia and some 40 kinds of rhododendron, then fir, juniper and alpine flowers. Sikkim is famous for its orchids — the noble dendrobium is the State flower — and its wildlife includes the red panda (the State animal), snow leopard, Himalayan black bear, blue sheep and the blood pheasant (the State bird).\n\nKhangchendzonga National Park, covering much of the north-west around Kangchenjunga, was inscribed in 2016 as India's first mixed World Heritage Site, and the wider Khangchendzonga Biosphere Reserve is part of UNESCO's network. Sanctuaries include Fambong Lho, Kyongnosla, Maenam, Barsey and Shingba (rhododendron) and Pangolakha. Khecheopalri Lake, sacred to Buddhists and Hindus, is Sikkim's Ramsar site.",
        "सिक्किम का लगभग 47% भाग वनाच्छादित है (आईएसएफ़आर 2023); उनके ऊपर अल्पाइन घास के मैदान, चट्टानें और स्थायी बर्फ़ है। कुछ किलोमीटर के भीतर वनस्पति निचली तीस्ता घाटी के उष्णकटिबंधीय साल और बाँस से बदलकर बलूत, मैगनोलिया और बुरांश की लगभग 40 किस्मों, फिर देवदार (फ़र), जुनिपर और अल्पाइन फूलों में बदल जाती है। सिक्किम अपने ऑर्किड के लिए प्रसिद्ध है — नोबल डेंड्रोबियम राज्य पुष्प है — और इसके वन्यजीवों में लाल पांडा (राज्य पशु), हिम तेंदुआ, हिमालयी काला भालू, भरल और रक्त तीतर (राज्य पक्षी) शामिल हैं।\n\nकंचनजंगा के आसपास उत्तर-पश्चिम के बड़े भाग में फैले खांगचेंदज़ोंगा राष्ट्रीय उद्यान को 2016 में भारत के पहले मिश्रित विश्व धरोहर स्थल के रूप में अंकित किया गया, और व्यापक खांगचेंदज़ोंगा जैवमंडल आरक्षित क्षेत्र यूनेस्को नेटवर्क का भाग है। अभयारण्यों में फ़ंबोंग ल्हो, क्योंगनोसला, मैनम, बरसे और शिंगबा (बुरांश) और पांगोलाखा शामिल हैं। बौद्धों और हिंदुओं के लिए पवित्र खेचियोपलरी झील सिक्किम का रामसर स्थल है।",
        "सिक्कीमचा सुमारे 47% भाग वनाच्छादित आहे (आयएसएफआर 2023); त्यांच्या वर अल्पाइन कुरणे, खडक व कायमचे बर्फ आहे. काही किलोमीटरमध्येच वनस्पती खालच्या तिस्ता खोऱ्यातील उष्णकटिबंधीय साल व बांबूपासून ओक, मॅग्नोलिया व ऱ्होडोडेंड्रॉनच्या सुमारे 40 प्रकारांत, नंतर फर, ज्युनिपर व अल्पाइन फुलांत बदलते. सिक्कीम त्याच्या ऑर्किडसाठी प्रसिद्ध आहे — नोबल डेंड्रोबियम हे राज्यपुष्प आहे — आणि त्याच्या वन्यजीवांत लाल पांडा (राज्यप्राणी), हिमबिबट्या, हिमालयी काळे अस्वल, भरल व रक्त तितर (राज्यपक्षी) यांचा समावेश आहे.\n\nकांचनजंगाभोवती वायव्येचा मोठा भाग व्यापणाऱ्या खांगचेंदझोंगा राष्ट्रीय उद्यानाची 2016 मध्ये भारतातील पहिले मिश्र जागतिक वारसा स्थळ म्हणून नोंद झाली, आणि व्यापक खांगचेंदझोंगा जीवावरण राखीव क्षेत्र युनेस्कोच्या जाळ्याचा भाग आहे. अभयारण्यांत फांबोंग ल्हो, क्योंगनोसला, मैनम, बरसे व शिंगबा (ऱ्होडोडेंड्रॉन) आणि पांगोलाखा यांचा समावेश आहे. बौद्ध व हिंदूंसाठी पवित्र खेचिओपलरी सरोवर हे सिक्कीमचे रामसर स्थळ आहे."),
        sources=["fsi", "indian-wetlands", "unesco-whc"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), sk["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(1, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: Khecheopalri (listed as Khachoedpalri) wetland, 172 ha."), "number"),
    ]),
    lst("protected", [
        it3("knp", "Khangchendzonga National Park", "खांगचेंदज़ोंगा राष्ट्रीय उद्यान", "खांगचेंदझोंगा राष्ट्रीय उद्यान", m=("UNESCO World Heritage (mixed), 2016", "यूनेस्को विश्व धरोहर (मिश्रित), 2016", "युनेस्को जागतिक वारसा (मिश्र), 2016")),
        it3("fambong", "Fambong Lho Wildlife Sanctuary", "फ़ंबोंग ल्हो वन्यजीव अभयारण्य", "फांबोंग ल्हो वन्यजीव अभयारण्य", m=("Near Gangtok", "गंगटोक के पास", "गंगटोकजवळ")),
        it3("kyongnosla", "Kyongnosla Alpine Sanctuary", "क्योंगनोसला अल्पाइन अभयारण्य", "क्योंगनोसला अल्पाइन अभयारण्य", m=("On the road to Tsomgo", "छांगू के मार्ग पर", "छांगूच्या रस्त्यावर")),
        it3("barsey", "Barsey Rhododendron Sanctuary", "बरसे बुरांश अभयारण्य", "बरसे ऱ्होडोडेंड्रॉन अभयारण्य", m=("West Sikkim", "पश्चिम सिक्किम", "पश्चिम सिक्कीम")),
        it3("shingba", "Shingba Rhododendron Sanctuary", "शिंगबा बुरांश अभयारण्य", "शिंगबा ऱ्होडोडेंड्रॉन अभयारण्य", m=("Yumthang valley", "युमथांग घाटी", "युमथांग खोरे")),
        it3("khecheopalri", "Khecheopalri Lake", "खेचियोपलरी झील", "खेचिओपलरी सरोवर", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("redpanda", "Red panda (State animal)", "लाल पांडा (राज्य पशु)", "लाल पांडा (राज्यप्राणी)"), it3("pheasant", "Blood pheasant (State bird)", "रक्त तीतर (राज्य पक्षी)", "रक्त तितर (राज्यपक्षी)"),
        it3("snowleopard", "Snow leopard", "हिम तेंदुआ", "हिमबिबट्या"), it3("bharal", "Blue sheep (bharal)", "भरल (नीली भेड़)", "भरल (निळी मेंढी)"),
        it3("rhodo", "Rhododendrons", "बुरांश", "ऱ्होडोडेंड्रॉन"), it3("orchid", "Orchids", "ऑर्किड", "ऑर्किड"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Number of rhododendron and orchid species — official", "बुरांश और ऑर्किड की प्रजातियों की संख्या — आधिकारिक", "ऱ्होडोडेंड्रॉन व ऑर्किड प्रजातींची संख्या — अधिकृत"), "india-gov", "Botanical Survey of India / Sikkim Forest Department."),
        (L("Khecheopalri Ramsar designation date", "खेचियोपलरी रामसर घोषणा की तिथि", "खेचिओपलरी रामसर घोषणेची तारीख"), "ramsar", "Confirm against the Ramsar Sites Information Service."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Sikkim's water comes from glaciers, snowmelt, monsoon rain and countless hill springs (dhara), which most villages depend on for drinking water. As springs have dried up with changing rainfall and land use, the State has run spring-recharge programmes on the hillsides. The Teesta, fed by glaciers and glacial lakes, is also the source of a long-standing water-sharing question between India and Bangladesh downstream. High glacial lakes such as South Lhonak are monitored because they can burst, as South Lhonak did in October 2023.",
        "सिक्किम का पानी हिमनदों, बर्फ़ पिघलने, मानसूनी वर्षा और अनगिनत पहाड़ी झरनों (धारा) से आता है, जिन पर अधिकांश गाँव पेयजल के लिए निर्भर हैं। बदलती वर्षा और भूमि उपयोग से झरने सूखने पर राज्य ने पहाड़ी ढलानों पर झरना पुनर्भरण कार्यक्रम चलाए हैं। हिमनदों और हिमनद झीलों से पोषित तीस्ता नीचे भारत और बांग्लादेश के बीच जल बँटवारे के लंबे प्रश्न का स्रोत भी है। दक्षिण ल्होनक जैसी ऊँची हिमनद झीलों की निगरानी की जाती है क्योंकि वे फट सकती हैं, जैसा अक्टूबर 2023 में दक्षिण ल्होनक के साथ हुआ।",
        "सिक्कीमचे पाणी हिमनद्या, वितळणारे बर्फ, मान्सूनचा पाऊस व असंख्य डोंगरी झरे (धारा) यांतून येते, ज्यांवर बहुतेक गावे पिण्याच्या पाण्यासाठी अवलंबून आहेत. बदलत्या पावसामुळे व जमीनवापरामुळे झरे आटू लागल्यावर राज्याने डोंगरउतारांवर झरा पुनर्भरण कार्यक्रम राबवले आहेत. हिमनद्या व हिमनदी सरोवरांनी पोसलेली तिस्ता खालच्या बाजूस भारत व बांगलादेशमधील दीर्घकालीन पाणीवाटप प्रश्नाचा स्रोतही आहे. दक्षिण ल्होनकसारख्या उंचावरील हिमनदी सरोवरांवर लक्ष ठेवले जाते कारण ती फुटू शकतात, जसे ऑक्टोबर 2023 मध्ये दक्षिण ल्होनकचे झाले."),
        conf="Editorial"),
    gaps("g", [
        (L("Spring-recharge programme — area and springs revived", "झरना पुनर्भरण कार्यक्रम — क्षेत्र और पुनर्जीवित झरने", "झरा पुनर्भरण कार्यक्रम — क्षेत्र व पुनरुज्जीवित झरे"), "india-gov", "Sikkim Rural Development Department (Dhara Vikas)."),
        (L("Household tap-water coverage", "घरेलू नल जल कवरेज", "घरगुती नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Sikkim lies in a highly earthquake-prone zone — an earthquake on 18 September 2011 caused deaths and heavy damage — and landslides close roads every monsoon. On 4 October 2023 South Lhonak glacial lake burst, sending a flood down the Teesta that destroyed the Chungthang dam, bridges and parts of NH-10 and towns downstream. At Gurudongmar, Nathu La and other high places visitors can suffer altitude sickness, and roads to the north and east can close suddenly because of snow. Visitors should carry permits, follow police and army advisories, and avoid travel on mountain roads during heavy rain.",
        "सिक्किम अत्यधिक भूकंप-प्रवण क्षेत्र में है — 18 सितंबर 2011 के भूकंप से मौतें और भारी क्षति हुई — और हर मानसून में भूस्खलन सड़कें बंद कर देते हैं। 4 अक्टूबर 2023 को दक्षिण ल्होनक हिमनद झील फटी, जिससे तीस्ता में आई बाढ़ ने चुंगथांग बाँध, पुलों और एनएच-10 के हिस्सों व नीचे के नगरों को नष्ट कर दिया। गुरुडोंगमार, नाथु ला और अन्य ऊँचे स्थानों पर पर्यटकों को ऊँचाई की बीमारी हो सकती है, और बर्फ़ के कारण उत्तर और पूर्व की सड़कें अचानक बंद हो सकती हैं। पर्यटकों को परमिट साथ रखने चाहिए, पुलिस और सेना के परामर्श मानने चाहिए, और भारी वर्षा में पहाड़ी सड़कों पर यात्रा से बचना चाहिए।",
        "सिक्कीम अतिशय भूकंपप्रवण क्षेत्रात आहे — 18 सप्टेंबर 2011 च्या भूकंपात मृत्यू व मोठे नुकसान झाले — आणि दर पावसाळ्यात भूस्खलन रस्ते बंद करते. 4 ऑक्टोबर 2023 रोजी दक्षिण ल्होनक हिमनदी सरोवर फुटले, आणि तिस्तेत आलेल्या पुराने चुंगथांग धरण, पूल व एनएच-10 चे भाग आणि खालची शहरे उद्ध्वस्त केली. गुरुडोंगमार, नथु ला व इतर उंच ठिकाणी पर्यटकांना उंचीचा त्रास होऊ शकतो, आणि बर्फामुळे उत्तर व पूर्वेकडील रस्ते अचानक बंद होऊ शकतात. पर्यटकांनी परवाने जवळ ठेवावेत, पोलीस व लष्कराच्या सूचना पाळाव्यात, आणि मुसळधार पावसात डोंगरी रस्त्यांवर प्रवास टाळावा."),
        conf="Editorial"),
    emergency_table(("Sikkim", "सिक्किम", "सिक्कीम")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Teesta flood of October 2023 — official toll and damage", "अक्टूबर 2023 की तीस्ता बाढ़ — आधिकारिक मृत्यु संख्या और क्षति", "ऑक्टोबर 2023 चा तिस्ता पूर — अधिकृत मृत्यू व नुकसान"), "ndma", "Sikkim State Disaster Management Authority / NDMA report."),
        (L("2011 earthquake — official toll", "2011 का भूकंप — आधिकारिक मृत्यु संख्या", "2011 चा भूकंप — अधिकृत मृत्यूसंख्या"), "ndma", "NDMA / Government of Sikkim."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Sikkim has four GIs on the GI Registry's list as on 31 December 2025. Sikkim large cardamom (filed in 2012) is the State's signature crop, grown under the forest canopy; Dalle khursani, the round, fiery chilli, is shared with West Bengal's Darjeeling hills; and two Lepcha crafts were registered in 2022: the tungbuk, a stringed instrument, and the pumtong pulit, a bamboo flute.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में सिक्किम के चार जीआई हैं। सिक्किम बड़ी इलायची (2012 में दायर) राज्य की पहचान वाली फ़सल है, जो वन की छाया में उगती है; गोल, तीखी मिर्च डल्ले खुर्सानी पश्चिम बंगाल की दार्जिलिंग पहाड़ियों के साथ साझा है; और 2022 में दो लेप्चा शिल्प पंजीकृत हुए: तारों वाला वाद्य तुंगबुक, और बाँस की बाँसुरी पुमतोंग पुलित।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत सिक्कीमचे चार जीआय आहेत. सिक्कीम मोठी वेलची (2012 मध्ये दाखल) हे राज्याचे ओळखपीक आहे, जे जंगलाच्या सावलीत घेतले जाते; गोल, तिखट मिरची डल्ले खुर्सानी पश्चिम बंगालच्या दार्जिलिंग डोंगरांशी सामायिक आहे; आणि 2022 मध्ये दोन लेप्चा कलावस्तूंची नोंदणी झाली: तंतुवाद्य तुंगबुक, आणि बांबूची बासरी पुमतोंग पुलित."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Pending GI applications from Sikkim", "सिक्किम के लंबित जीआई आवेदन", "सिक्कीमचे प्रलंबित जीआय अर्ज"), "gi-registry", "GI Registry application status search."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Gangtok, with MG Marg, Rumtek and Enchey monasteries and views of Kangchenjunga, is the base for trips east to Tsomgo (Changu) Lake, Baba Mandir and Nathu La on the China border. North Sikkim's Lachung, the Yumthang valley of rhododendrons and hot springs, and Gurudongmar Lake at about 5,400 m need permits and a night or two in Lachen or Lachung. In the west, Pelling looks across to Kangchenjunga and the Pemayangtse monastery, Yuksom is the starting point of the trek to Dzongri and Goecha La, and Khecheopalri is a sacred lake. In the south, Namchi has a giant statue of Guru Padmasambhava at Samdruptse and the Char Dham complex, and Ravangla has the Buddha Park.",
        "एमजी मार्ग, रुमटेक और एंचे मठों और कंचनजंगा के दृश्यों वाला गंगटोक पूर्व में छांगू (त्सोमगो) झील, बाबा मंदिर और चीन सीमा पर नाथु ला की यात्राओं का आधार है। उत्तर सिक्किम का लाचुंग, बुरांश और गर्म झरनों की युमथांग घाटी, और लगभग 5,400 मीटर पर गुरुडोंगमार झील के लिए परमिट और लाचेन या लाचुंग में एक-दो रातें चाहिए। पश्चिम में पेलिंग से कंचनजंगा और पेमायांग्त्से मठ दिखते हैं, युकसोम ज़ोंगरी और गोएचा ला ट्रेक का आरंभ बिंदु है, और खेचियोपलरी एक पवित्र झील है। दक्षिण में नामची के सामद्रुप्त्से में गुरु पद्मसंभव की विशाल प्रतिमा और चार धाम परिसर है, और रावंगला में बुद्ध पार्क है।",
        "एमजी मार्ग, रुमटेक व एंचे मठ आणि कांचनजंगाचे दर्शन असलेले गंगटोक हे पूर्वेकडील छांगू (त्सोमगो) सरोवर, बाबा मंदिर व चीन सीमेवरील नथु लाच्या सहलींसाठी तळ आहे. उत्तर सिक्कीममधील लाचुंग, ऱ्होडोडेंड्रॉन व गरम पाण्याच्या झऱ्यांचे युमथांग खोरे, आणि सुमारे 5,400 मीटरवरील गुरुडोंगमार सरोवरासाठी परवाने व लाचेन किंवा लाचुंग येथे एक-दोन रात्री लागतात. पश्चिमेला पेलिंगहून कांचनजंगा व पेमायांगत्से मठ दिसतात, युकसोम हे झोंगरी व गोएचा ला ट्रेकचे सुरुवातीचे ठिकाण आहे, आणि खेचिओपलरी हे पवित्र सरोवर आहे. दक्षिणेत नामचीच्या सामद्रुप्त्से येथे गुरु पद्मसंभवांची भव्य मूर्ती व चारधाम संकुल आहे, आणि रावंगला येथे बुद्ध उद्यान आहे."),
        conf="Editorial"),
    lst("places", [
        it3("gangtok", "Gangtok", "गंगटोक", "गंगटोक", m=("MG Marg, monasteries, ropeway", "एमजी मार्ग, मठ, रोपवे", "एमजी मार्ग, मठ, रोपवे")),
        it3("tsomgo", "Tsomgo Lake and Nathu La", "छांगू झील और नाथु ला", "छांगू सरोवर व नथु ला", m=("Permit needed", "परमिट आवश्यक", "परवाना आवश्यक")),
        it3("yumthang", "Lachung and Yumthang", "लाचुंग और युमथांग", "लाचुंग व युमथांग", m=("Valley of flowers", "फूलों की घाटी", "फुलांचे खोरे")),
        it3("gurudongmar", "Gurudongmar Lake", "गुरुडोंगमार झील", "गुरुडोंगमार सरोवर", m=("High-altitude lake", "ऊँचाई की झील", "उंचावरील सरोवर")),
        it3("pelling", "Pelling and Yuksom", "पेलिंग और युकसोम", "पेलिंग व युकसोम", m=("Kangchenjunga views; trekking", "कंचनजंगा दृश्य; ट्रेकिंग", "कांचनजंगा दर्शन; ट्रेकिंग")),
        it3("namchi", "Namchi and Ravangla", "नामची और रावंगला", "नामची व रावंगला", m=("Samdruptse, Char Dham, Buddha Park", "सामद्रुप्त्से, चार धाम, बुद्ध पार्क", "सामद्रुप्त्से, चारधाम, बुद्ध उद्यान")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Gangtok, Rumtek, and a day trip to Tsomgo Lake and Nathu La.", "गंगटोक, रुमटेक, और छांगू झील व नाथु ला की एक दिन की यात्रा।", "गंगटोक, रुमटेक, आणि छांगू सरोवर व नथु लाची एकदिवसीय सहल.")),
        it3("d6", "6 days", "6 दिन", "6 दिवस", d=("Add Lachung, Yumthang and Gurudongmar (two nights in the north).", "लाचुंग, युमथांग और गुरुडोंगमार जोड़ें (उत्तर में दो रातें)।", "लाचुंग, युमथांग व गुरुडोंगमार जोडा (उत्तरेत दोन रात्री).")),
        it3("d4w", "4 days (west and south)", "4 दिन (पश्चिम और दक्षिण)", "4 दिवस (पश्चिम व दक्षिण)", d=("Ravangla, Pelling, Pemayangtse, Khecheopalri and Yuksom.", "रावंगला, पेलिंग, पेमायांग्त्से, खेचियोपलरी और युकसोम।", "रावंगला, पेलिंग, पेमायांगत्से, खेचिओपलरी व युकसोम.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium / Sikkim Tourism."),
        (L("Gurudongmar Lake — official elevation", "गुरुडोंगमार झील — आधिकारिक ऊँचाई", "गुरुडोंगमार सरोवर — अधिकृत उंची"), "survey-of-india", "Survey of India."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [("Gangtok", "गंगटोक", "गंगटोक"), ("Gyalshing", "ग्यालशिंग", "ग्यालशिंग"), ("Mangan", "मंगन", "मंगन"),
             ("Namchi", "नामची", "नामची"), ("Pakyong", "पाक्योंग", "पाकयोंग"), ("Soreng", "सोरेंग", "सोरेंग")]
module(R, "cities", [
    lst("cities", [
        city("gangtok", ("Gangtok", "गंगटोक", "गंगटोक"), ("Capital on a ridge at about 1,600 m.", "लगभग 1,600 मीटर पर एक पहाड़ी पर राजधानी।", "सुमारे 1,600 मीटरवरील कड्यावरील राजधानी."), ("Capital", "राजधानी", "राजधानी")),
        city("namchi", ("Namchi", "नामची", "नामची"), ("Headquarters of the south; pilgrimage centre.", "दक्षिण का मुख्यालय; तीर्थ केंद्र।", "दक्षिणेचे मुख्यालय; तीर्थक्षेत्र."), ("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        city("gyalshing", ("Gyalshing (Geyzing)", "ग्यालशिंग (गेज़िंग)", "ग्यालशिंग (गेझिंग)"), ("Headquarters of the west, near Pelling.", "पश्चिम का मुख्यालय, पेलिंग के पास।", "पश्चिमेचे मुख्यालय, पेलिंगजवळ."), ("Administration", "प्रशासन", "प्रशासन")),
        city("mangan", ("Mangan", "मंगन", "मंगन"), ("Headquarters of the north; large-cardamom country.", "उत्तर का मुख्यालय; बड़ी इलायची का क्षेत्र।", "उत्तरेचे मुख्यालय; मोठ्या वेलचीचा प्रदेश."), ("Administration", "प्रशासन", "प्रशासन")),
        city("rangpo", ("Rangpo", "रंगपो", "रंगपो"), ("Border town on NH-10; future railhead.", "एनएच-10 पर सीमावर्ती नगर; भावी रेल टर्मिनल।", "एनएच-10 वरील सीमाशहर; भावी रेल्वेस्थानक."), ("Gateway", "प्रवेशद्वार", "प्रवेशद्वार")),
        city("singtam", ("Singtam", "सिंगताम", "सिंगताम"), ("Market town on the Teesta.", "तीस्ता किनारे बाज़ार नगर।", "तिस्ताकाठचे बाजारशहर."), ("Market", "बाज़ार", "बाजार")),
    ], title=L("Major towns", "प्रमुख नगर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 6 districts (alphabetical)", "6 ज़िले (वर्णानुक्रम)", "6 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Town populations (Census 2011)", "नगरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Football is Sikkim's most popular sport. Baichung Bhutia from Tinkitam captained India and became one of its best-known footballers, and the Paljor Stadium in Gangtok hosts the Sikkim Governor's Gold Cup football tournament. Archery has a strong following too: Tarundeep Rai has represented India at several Olympic Games. The mountains draw climbers, trekkers, paragliders and river-rafters on the Teesta and Rangeet.",
        "फ़ुटबॉल सिक्किम का सबसे लोकप्रिय खेल है। तिनकिताम के बाईचुंग भूटिया ने भारत की कप्तानी की और देश के सबसे प्रसिद्ध फ़ुटबॉलरों में बने, और गंगटोक का पलजोर स्टेडियम सिक्किम गवर्नर्स गोल्ड कप फ़ुटबॉल टूर्नामेंट की मेज़बानी करता है। तीरंदाज़ी भी लोकप्रिय है: तरुणदीप राय कई ओलंपिक खेलों में भारत का प्रतिनिधित्व कर चुके हैं। पहाड़ पर्वतारोहियों, ट्रेकरों, पैराग्लाइडरों और तीस्ता व रंगीत पर रिवर-राफ़्टिंग करने वालों को खींचते हैं।",
        "फुटबॉल हा सिक्कीमचा सर्वांत लोकप्रिय खेळ आहे. तिनकितामचे बायचुंग भुतिया यांनी भारताचे कर्णधारपद भूषवले व ते देशातील सर्वांत प्रसिद्ध फुटबॉलपटूंपैकी झाले, आणि गंगटोकचे पलजोर स्टेडियम सिक्कीम गव्हर्नर्स गोल्ड कप फुटबॉल स्पर्धेचे यजमान आहे. तिरंदाजीचीही मोठी आवड आहे: तरुणदीप राय यांनी अनेक ऑलिंपिक स्पर्धांत भारताचे प्रतिनिधित्व केले आहे. पर्वत गिर्यारोहक, ट्रेकर, पॅराग्लायडर व तिस्ता आणि रंगीतवर राफ्टिंग करणाऱ्यांना आकर्षित करतात."),
        conf="Editorial"),
    lst("venues", [
        it3("paljor", "Paljor Stadium, Gangtok", "पलजोर स्टेडियम, गंगटोक", "पलजोर स्टेडियम, गंगटोक"),
        it3("namchi", "Bhaichung Stadium, Namchi", "बाईचुंग स्टेडियम, नामची", "बायचुंग स्टेडियम, नामची"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Gold Cup history — official record", "गोल्ड कप इतिहास — आधिकारिक रिकॉर्ड", "गोल्ड कप इतिहास — अधिकृत नोंद"), "india-gov", "Sikkim Football Association.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("palden", ("Palden Thondup Namgyal", "पाल्देन थोंडुप नामग्याल", "पाल्देन थोंडुप नामग्याल"), ("The twelfth and last Chogyal of Sikkim, who reigned from 1963 to 1975.", "सिक्किम के बारहवें और अंतिम चोग्याल, जिन्होंने 1963 से 1975 तक शासन किया।", "सिक्कीमचे बारावे व शेवटचे चोग्याल, ज्यांनी 1963 ते 1975 राज्य केले."), ("History", "इतिहास", "इतिहास")),
        person("lhendup", ("Kazi Lhendup Dorjee", "काज़ी ल्हेंडुप दोरजी", "काझी ल्हेंडुप दोरजी"), ("Leader of the democracy movement and the State's first Chief Minister (1974–1979).", "लोकतंत्र आंदोलन के नेता और राज्य के पहले मुख्यमंत्री (1974–1979)।", "लोकशाही चळवळीचे नेते व राज्याचे पहिले मुख्यमंत्री (1974–1979)."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("chamling", ("Pawan Kumar Chamling", "पवन कुमार चामलिंग", "पवन कुमार चामलिंग"), ("Founder of the Sikkim Democratic Front and Chief Minister for five consecutive terms, from 1994 to 2019.", "सिक्किम डेमोक्रेटिक फ़्रंट के संस्थापक और 1994 से 2019 तक लगातार पाँच कार्यकालों तक मुख्यमंत्री।", "सिक्कीम डेमोक्रॅटिक फ्रंटचे संस्थापक व 1994 ते 2019 सलग पाच कारकिर्दींसाठी मुख्यमंत्री."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("bhaichung", ("Baichung Bhutia", "बाईचुंग भूटिया", "बायचुंग भुतिया"), ("Former India football captain from Tinkitam, Padma Shri awardee.", "तिनकिताम के भारत के पूर्व फ़ुटबॉल कप्तान, पद्म श्री सम्मानित।", "तिनकितामचे भारताचे माजी फुटबॉल कर्णधार, पद्मश्री सन्मानित."), ("Sport", "खेल", "क्रीडा")),
        person("tarundeep", ("Tarundeep Rai", "तरुणदीप राय", "तरुणदीप राय"), ("Archer who has competed for India at several Olympic Games.", "तीरंदाज़ जिन्होंने कई ओलंपिक खेलों में भारत के लिए भाग लिया।", "तिरंदाज, ज्यांनी अनेक ऑलिंपिक स्पर्धांत भारतासाठी भाग घेतला."), ("Sport", "खेल", "क्रीडा")),
        person("danny", ("Danny Denzongpa", "डैनी डेन्ज़ोंग्पा", "डॅनी डेंझोंग्पा"), ("Actor in Hindi and Nepali films, born in Sikkim.", "हिंदी और नेपाली फ़िल्मों के अभिनेता, सिक्किम में जन्मे।", "हिंदी व नेपाळी चित्रपटांतील अभिनेते, सिक्कीममध्ये जन्मलेले."), ("Cinema", "सिनेमा", "चित्रपट")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Sikkim has a small diaspora. Many young people study and work in Bengaluru, Delhi, Kolkata and other cities, especially in hospitality, nursing, aviation and IT, and others serve in the armed forces. There are close family and cultural ties with Darjeeling and Kalimpong in West Bengal, Nepal and Bhutan.",
        "सिक्किम का प्रवासी समुदाय छोटा है। बहुत से युवा बेंगलुरु, दिल्ली, कोलकाता और अन्य नगरों में पढ़ते और काम करते हैं, विशेषकर आतिथ्य, नर्सिंग, विमानन और आईटी में, और अन्य सशस्त्र बलों में सेवा करते हैं। पश्चिम बंगाल के दार्जिलिंग और कालिम्पोंग, नेपाल और भूटान के साथ घनिष्ठ पारिवारिक और सांस्कृतिक संबंध हैं।",
        "सिक्कीमचा प्रवासी समुदाय लहान आहे. अनेक तरुण बंगळुरू, दिल्ली, कोलकाता व इतर शहरांत शिकतात व काम करतात, विशेषतः आतिथ्य, परिचर्या, विमानवाहतूक व आयटी क्षेत्रांत, आणि काही सशस्त्र दलांत सेवा करतात. पश्चिम बंगालमधील दार्जिलिंग व कालिम्पोंग, नेपाळ आणि भूतानशी जवळचे कौटुंबिक व सांस्कृतिक नाते आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Out-migration from Sikkim — official estimate", "सिक्किम से बाहर प्रवास — आधिकारिक अनुमान", "सिक्कीममधून बाहेर स्थलांतर — अधिकृत अंदाज"), "census", "Census 2011 migration tables (D-series)."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Sikkim portal", "सिक्किम सरकार पोर्टल", "सिक्कीम शासन संकेतस्थळ", url="https://sikkim.gov.in", src="sk-gov"),
        it3("lokbhavan", "Lok Bhavan Sikkim", "लोक भवन सिक्किम", "लोक भवन सिक्कीम", url="https://rajbhavansikkim.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD code", "एसटीडी कोड", "एसटीडी कोड"),
          [col(L("Area", "क्षेत्र", "क्षेत्र")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Gangtok", "गंगटोक", "गंगटोक"), "03592"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; other towns have their own codes. To be checked against the Department of Telecommunications numbering plan.", "संपादकीय; अन्य नगरों के अपने कोड हैं। दूरसंचार विभाग की नंबरिंग योजना से जाँचा जाएगा।", "संपादकीय; इतर शहरांचे स्वतंत्र कोड आहेत. दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळले जाईल.")),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("pop", ("Sikkim is India's least populous State — 6.1 lakh people in 2011.", "सिक्किम भारत का सबसे कम आबादी वाला राज्य है — 2011 में 6.1 लाख लोग।", "सिक्कीम हे भारतातील सर्वांत कमी लोकसंख्येचे राज्य आहे — 2011 मध्ये 6.1 लाख लोक."), "https://statistics.py.gov.in/state-wise-population", "census"),
        triv("pc", ("Sikkim's per capita NSDP in FY2024-25 was the highest of any State or UT in the MoSPI series.", "वित्त वर्ष 2024-25 में सिक्किम का प्रति व्यक्ति एनएसडीपी मोस्पी शृंखला में किसी भी राज्य या केंद्र शासित प्रदेश में सबसे अधिक था।", "आ.व. 2024-25 मध्ये सिक्कीमचे दरडोई एनएसडीपी मोस्पी मालिकेत कोणत्याही राज्य वा केंद्रशासित प्रदेशात सर्वाधिक होते."), MOSPI, "mospi"),
        triv("knp", ("Khangchendzonga National Park was India's first 'mixed' World Heritage Site (2016).", "खांगचेंदज़ोंगा राष्ट्रीय उद्यान भारत का पहला 'मिश्रित' विश्व धरोहर स्थल था (2016)।", "खांगचेंदझोंगा राष्ट्रीय उद्यान हे भारतातील पहिले 'मिश्र' जागतिक वारसा स्थळ होते (2016)."), UNESCO, "unesco-whc"),
        triv("organic", ("Sikkim was declared India's first fully organic State in 2016.", "सिक्किम को 2016 में भारत का पहला पूर्णतः जैविक राज्य घोषित किया गया।", "सिक्कीमला 2016 मध्ये भारताचे पहिले पूर्णतः सेंद्रिय राज्य घोषित केले गेले.")),
        triv("sangha", ("One Assembly seat, the Sangha seat, is elected only by monks and nuns.", "विधानसभा की एक सीट, संघ सीट, केवल भिक्षुओं और भिक्षुणियों द्वारा चुनी जाती है।", "विधानसभेची एक जागा, संघ जागा, केवळ भिक्षू व भिक्षुणी निवडतात.")),
        triv("langs", ("Sikkim has eleven official languages.", "सिक्किम की ग्यारह राजभाषाएँ हैं।", "सिक्कीमच्या अकरा राजभाषा आहेत.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("sk mod3 ok")
