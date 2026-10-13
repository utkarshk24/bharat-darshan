import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-LA"
LAG = "https://ladakh.gov.in"
KGL = "https://kargil.nic.in/demography/"
LS_ZOJILA = "https://eparlib.nic.in/bitstream/123456789/2980199/1/AU2921_SM4WZv.pdf"
ind = read("india.json")["metrics"]
NAME = L("Ladakh", "लद्दाख", "लडाख")


def fest(id, n, m, d):
    return item(id, L(*n), detail=L(*d), meta=L(*m))


# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Ladakh is a high-altitude Union Territory in India's far north, lying between the Great Himalaya and the Karakoram. It became a separate Union Territory without a legislature on 31 October 2019, when the Jammu and Kashmir Reorganisation Act, 2019 divided the former State. It is administered by a Lieutenant Governor, with elected Autonomous Hill Development Councils for Leh and Kargil.\n\nIt is one of the most thinly populated parts of India: a cold desert of bare mountains, river valleys, high lakes and passes, where villages cluster around irrigated fields of barley and apricot. Leh is the main town and administrative centre; Kargil is the second.",
        "लद्दाख भारत के सुदूर उत्तर में महान हिमालय और काराकोरम के बीच स्थित एक ऊँचाई वाला केंद्र शासित प्रदेश है। 31 अक्टूबर 2019 को जम्मू और कश्मीर पुनर्गठन अधिनियम, 2019 द्वारा पूर्व राज्य के विभाजन के साथ यह बिना विधानसभा वाला अलग केंद्र शासित प्रदेश बना। इसका प्रशासन उपराज्यपाल करते हैं, और लेह व कारगिल के लिए निर्वाचित स्वायत्त पहाड़ी विकास परिषदें हैं।\n\nयह भारत के सबसे विरल आबादी वाले हिस्सों में है: नंगे पहाड़ों, नदी घाटियों, ऊँची झीलों और दर्रों का ठंडा रेगिस्तान, जहाँ गाँव जौ और ख़ुबानी के सिंचित खेतों के आसपास बसे हैं। लेह मुख्य नगर और प्रशासनिक केंद्र है; कारगिल दूसरा।",
        "लडाख हा भारताच्या अतिउत्तरेला महान हिमालय आणि काराकोरम यांच्यामध्ये वसलेला उंचावरील केंद्रशासित प्रदेश आहे. जम्मू आणि काश्मीर पुनर्रचना अधिनियम, 2019 द्वारे पूर्वीच्या राज्याचे विभाजन होऊन 31 ऑक्टोबर 2019 रोजी तो विधिमंडळ नसलेला स्वतंत्र केंद्रशासित प्रदेश बनला. त्याचे प्रशासन नायब राज्यपाल पाहतात, आणि लेह व कारगिलसाठी निवडून आलेल्या स्वायत्त पर्वतीय विकास परिषदा आहेत.\n\nहा भारतातील सर्वांत विरळ लोकवस्तीच्या भागांपैकी एक आहे: उघडे डोंगर, नदीखोरी, उंचावरील सरोवरे आणि खिंडी यांचे थंड वाळवंट, जिथे गावे बार्ली आणि जर्दाळूच्या सिंचित शेतांभोवती वसलेली आहेत. लेह हे मुख्य शहर व प्रशासकीय केंद्र आहे; कारगिल दुसरे."),
        conf="Editorial"),
    prose("intro-unique", L(
        "Ladakh's landscapes — Pangong and Tso Moriri lakes, the sand dunes of Nubra, the gorges of Zanskar — are matched by a living Buddhist and Islamic heritage: cliff-top gompas such as Hemis, Thiksey and Lamayuru, masked cham dances, and the Shia traditions of Kargil and the Suru valley. It is also a place of inventive adaptation to cold and scarcity, from solar-heated homes to artificial glaciers that store winter meltwater for spring sowing.",
        "लद्दाख के भू-दृश्य — पैंगोंग और त्सो मोरीरी झीलें, नुब्रा के रेत के टीले, ज़ांस्कर की घाटियाँ — के साथ-साथ यहाँ जीवित बौद्ध और इस्लामी विरासत भी है: हेमिस, थिकसे और लामायुरु जैसे पहाड़ी चोटियों पर बने गोम्पा, मुखौटों वाले छम नृत्य, और कारगिल व सुरू घाटी की शिया परंपराएँ। यह ठंड और कमी के प्रति रचनात्मक अनुकूलन की जगह भी है — सौर ऊर्जा से गर्म घरों से लेकर कृत्रिम ग्लेशियरों तक, जो वसंत की बुआई के लिए सर्दियों का पानी जमा रखते हैं।",
        "लडाखच्या निसर्गदृश्यांसोबत — पँगाँग आणि त्सो मोरिरी सरोवरे, नुब्राचे वाळूचे ढिगारे, झांस्करच्या घळी — येथे जिवंत बौद्ध व इस्लामी वारसाही आहे: हेमिस, थिकसे आणि लामायुरूसारखे कड्यांवरील गोंपा, मुखवट्यांचे छम नृत्य, आणि कारगिल व सुरू खोऱ्यातील शिया परंपरा. थंडी आणि टंचाईशी कल्पकतेने जुळवून घेण्याचेही हे ठिकाण आहे — सौरऊर्जेने उबदार केलेल्या घरांपासून वसंतातील पेरणीसाठी हिवाळ्यातील पाणी साठवणाऱ्या कृत्रिम हिमनद्यांपर्यंत."),
        title=L("What makes Ladakh unique?", "लद्दाख को ख़ास क्या बनाता है?", "लडाखचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formation", "गठन", "स्थापना"), L("31 October 2019 (Union Territory without legislature)", "31 अक्टूबर 2019 (बिना विधानसभा वाला केंद्र शासित प्रदेश)", "31 ऑक्टोबर 2019 (विधिमंडळ नसलेला केंद्रशासित प्रदेश)")],
           [L("Districts", "ज़िले", "जिल्हे"), L("Leh and Kargil (as listed on the UT portal)", "लेह और कारगिल (केंद्र शासित प्रदेश पोर्टल के अनुसार)", "लेह आणि कारगिल (केंद्रशासित प्रदेश संकेतस्थळानुसार)")],
           [L("Elected local bodies", "निर्वाचित स्थानीय निकाय", "निवडून आलेल्या स्थानिक संस्था"), L("Ladakh Autonomous Hill Development Councils, Leh and Kargil", "लद्दाख स्वायत्त पहाड़ी विकास परिषद, लेह और कारगिल", "लडाख स्वायत्त पर्वतीय विकास परिषद, लेह व कारगिल")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-LA / LA"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          "la-gov", LAG, conf="Editorial",
          note=L("Districts as shown on the UT Administration portal. New districts announced by the Union Government in 2024 are listed as a gap until their notification is linked.",
                 "ज़िले केंद्र शासित प्रदेश प्रशासन के पोर्टल के अनुसार। 2024 में केंद्र सरकार द्वारा घोषित नए ज़िलों को उनकी अधिसूचना जुड़ने तक कमियों में रखा गया है।",
                 "जिल्हे केंद्रशासित प्रदेश प्रशासनाच्या संकेतस्थळानुसार. 2024 मध्ये केंद्र सरकारने जाहीर केलेले नवे जिल्हे त्यांची अधिसूचना जोडली जाईपर्यंत त्रुटींमध्ये दाखवले आहेत.")),
    gaps("g", [
        (L("New districts announced in 2024 — notification and operational status", "2024 में घोषित नए ज़िले — अधिसूचना और कार्य स्थिति", "2024 मध्ये जाहीर नवे जिल्हे — अधिसूचना व कार्यस्थिती"), "la-gov", "Ministry of Home Affairs / UT Administration notifications."),
        (L("Official languages (with notification)", "राजभाषाएँ (अधिसूचना सहित)", "राजभाषा (अधिसूचनेसह)"), "la-gov", "Link the UT's official-languages regulation."),
    ]),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Ladakh lies on the Tibetan plateau's western edge, mostly above 3,000 m. Parallel ranges run north-west to south-east — the Great Himalaya, Zanskar, Ladakh and Karakoram — with the Indus flowing between them past Leh. Its tributaries, the Shyok and Nubra in the north and the Zanskar and Suru in the south and west, carve the main inhabited valleys. The Changthang plateau in the east holds high saline and freshwater lakes, including Pangong Tso, Tso Moriri and Tso Kar.\n\nLadakh borders Jammu & Kashmir to the west and Himachal Pradesh to the south. India's official map shows its boundaries extending to areas under the occupation of Pakistan and China, which is why area figures from different sources do not match.",
        "लद्दाख तिब्बती पठार के पश्चिमी किनारे पर है, जिसका अधिकांश भाग 3,000 मीटर से ऊपर है। समानांतर पर्वत श्रेणियाँ उत्तर-पश्चिम से दक्षिण-पूर्व तक फैली हैं — महान हिमालय, ज़ांस्कर, लद्दाख और काराकोरम — और उनके बीच सिंधु लेह के पास से बहती है। उत्तर में श्योक और नुब्रा तथा दक्षिण व पश्चिम में ज़ांस्कर और सुरू जैसी सहायक नदियाँ मुख्य आबाद घाटियाँ बनाती हैं। पूर्व में चांगथांग पठार पर ऊँची खारी और मीठे पानी की झीलें हैं, जिनमें पैंगोंग त्सो, त्सो मोरीरी और त्सो कार शामिल हैं।\n\nलद्दाख के पश्चिम में जम्मू-कश्मीर और दक्षिण में हिमाचल प्रदेश है। भारत के आधिकारिक मानचित्र में इसकी सीमाएँ पाकिस्तान और चीन के कब्ज़े वाले क्षेत्रों तक दिखाई गई हैं, इसलिए विभिन्न स्रोतों के क्षेत्रफल आँकड़े मेल नहीं खाते।",
        "लडाख तिबेटी पठाराच्या पश्चिम कडेवर असून त्याचा बहुतांश भाग 3,000 मीटरपेक्षा उंच आहे. समांतर पर्वतरांगा वायव्येकडून आग्नेयेकडे पसरल्या आहेत — महान हिमालय, झांस्कर, लडाख आणि काराकोरम — आणि त्यांच्यामधून सिंधू नदी लेहजवळून वाहते. उत्तरेकडील श्योक व नुब्रा आणि दक्षिण-पश्चिमेकडील झांस्कर व सुरू या उपनद्यांनी मुख्य वस्ती असलेली खोरी कोरली आहेत. पूर्वेकडील चांगथांग पठारावर उंचावरील खारी व गोड्या पाण्याची सरोवरे आहेत — पँगाँग त्सो, त्सो मोरिरी आणि त्सो कार.\n\nलडाखच्या पश्चिमेला जम्मू-काश्मीर आणि दक्षिणेला हिमाचल प्रदेश आहे. भारताच्या अधिकृत नकाशात त्याच्या सीमा पाकिस्तान व चीनच्या ताब्यातील प्रदेशांपर्यंत दाखवल्या आहेत, म्हणूनच वेगवेगळ्या स्रोतांतील क्षेत्रफळाचे आकडे जुळत नाहीत."),
        conf="Editorial"),
    lst("neighbours", [
        it3("jk", "Jammu & Kashmir (west)", "जम्मू और कश्मीर (पश्चिम)", "जम्मू आणि काश्मीर (पश्चिम)"),
        it3("hp", "Himachal Pradesh (south)", "हिमाचल प्रदेश (दक्षिण)", "हिमाचल प्रदेश (दक्षिण)"),
    ], layout="chips", title=L("Neighbouring States and UTs", "पड़ोसी राज्य और केंद्र शासित प्रदेश", "शेजारी राज्ये व केंद्रशासित प्रदेश"), conf="Editorial"),
    lst("rivers", [
        it3("indus", "Indus (Sindhu)", "सिंधु", "सिंधू", d=("Enters from Tibet and flows north-west past Leh.", "तिब्बत से प्रवेश कर लेह के पास से उत्तर-पश्चिम की ओर बहती है।", "तिबेटमधून प्रवेश करून लेहजवळून वायव्येकडे वाहते.")),
        it3("shyok", "Shyok and Nubra", "श्योक और नुब्रा", "श्योक व नुब्रा", d=("Northern valleys below the Karakoram.", "काराकोरम के नीचे की उत्तरी घाटियाँ।", "काराकोरमखालील उत्तरेकडील खोरी.")),
        it3("zanskar", "Zanskar", "ज़ांस्कर", "झांस्कर", d=("Flows through deep gorges to join the Indus near Nimmu; frozen in winter.", "गहरी घाटियों से होकर निम्मू के पास सिंधु से मिलती है; सर्दियों में जम जाती है।", "खोल घळींतून वाहत निम्मूजवळ सिंधूला मिळते; हिवाळ्यात गोठते.")),
        it3("suru", "Suru", "सुरू", "सुरू", d=("Flows past Kargil; its valley is the main farming area of Kargil district.", "कारगिल के पास से बहती है; इसकी घाटी कारगिल ज़िले का मुख्य कृषि क्षेत्र है।", "कारगिलजवळून वाहते; तिचे खोरे कारगिल जिल्ह्याचा मुख्य शेती प्रदेश आहे.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Geographical area (administered and as per India's map)", "भौगोलिक क्षेत्रफल (प्रशासित और भारत के मानचित्र के अनुसार)", "भौगोलिक क्षेत्रफळ (प्रशासित व भारताच्या नकाशानुसार)"), "survey-of-india", "Record both with clear labels."),
        (L("Elevation of main settlements and passes", "मुख्य बस्तियों और दर्रों की ऊँचाई", "मुख्य वस्त्या व खिंडींची उंची"), "survey-of-india", "Survey of India."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "IS 1893 (Part 1), current revision."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Ladakh has a cold-desert climate. The Himalaya block most monsoon rain, so the region receives very little precipitation, much of it as winter snow. Winters are long and severe, with night temperatures far below freezing; Drass, on the route from Kashmir, is one of the coldest inhabited places in India. Summers are short, sunny and dry, warm in the day and cool at night. The thin air means strong sunlight and rapid sunburn, and high-altitude sickness is a real risk for visitors arriving by air.",
        "लद्दाख की जलवायु ठंडे रेगिस्तान वाली है। हिमालय अधिकांश मानसूनी वर्षा को रोक देता है, इसलिए यहाँ बहुत कम वर्षा होती है, जिसका बड़ा हिस्सा सर्दियों की बर्फ़ के रूप में होता है। सर्दियाँ लंबी और कड़ी होती हैं, रात का तापमान हिमांक से काफ़ी नीचे चला जाता है; कश्मीर से आने वाले रास्ते पर द्रास भारत के सबसे ठंडे आबाद स्थानों में है। गर्मियाँ छोटी, धूप भरी और सूखी होती हैं — दिन में गर्म, रात में ठंडी। पतली हवा के कारण धूप तेज़ होती है और त्वचा जल्दी झुलसती है, और हवाई मार्ग से आने वाले पर्यटकों के लिए ऊँचाई की बीमारी का वास्तविक ख़तरा है।",
        "लडाखचे हवामान थंड वाळवंटी आहे. हिमालय बहुतांश मोसमी पाऊस अडवतो, त्यामुळे येथे फारच कमी पर्जन्य होते आणि त्याचा मोठा भाग हिवाळ्यातील बर्फाच्या रूपात असतो. हिवाळा दीर्घ आणि कडक असतो, रात्रीचे तापमान गोठणबिंदूच्या खूप खाली जाते; काश्मीरहून येणाऱ्या मार्गावरील द्रास हे भारतातील सर्वांत थंड वस्ती असलेल्या ठिकाणांपैकी एक आहे. उन्हाळा छोटा, सूर्यप्रकाशित आणि कोरडा असतो — दिवसा उबदार, रात्री थंड. विरळ हवेमुळे ऊन प्रखर असते आणि त्वचा लवकर भाजते, तसेच विमानाने येणाऱ्या पर्यटकांना उंचीमुळे होणाऱ्या आजाराचा खरा धोका असतो."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Leh", "लेह", "लेह"), "lat": 34.1526, "lon": 77.5771},
        {"name": L("Kargil", "कारगिल", "कारगिल"), "lat": 34.5539, "lon": 76.1349},
        {"name": L("Diskit (Nubra)", "डिस्किट (नुब्रा)", "डिस्किट (नुब्रा)"), "lat": 34.5426, "lon": 77.5602},
        {"name": L("Drass", "द्रास", "द्रास"), "lat": 34.4290, "lon": 75.7495},
    ]},
    lst("best", [
        it3("summer", "June to September", "जून से सितंबर", "जून ते सप्टेंबर", d=("Main season: all passes and roads usually open.", "मुख्य मौसम: आम तौर पर सभी दर्रे और सड़कें खुली रहती हैं।", "मुख्य हंगाम: सहसा सर्व खिंडी आणि रस्ते खुले असतात.")),
        it3("may", "May and October", "मई और अक्टूबर", "मे आणि ऑक्टोबर", d=("Quieter shoulder months; colder nights and possible road closures.", "कम भीड़ वाले महीने; ठंडी रातें और सड़कें बंद होने की संभावना।", "कमी गर्दीचे महिने; थंड रात्री व रस्ते बंद होण्याची शक्यता.")),
        it3("winter", "January to February", "जनवरी से फ़रवरी", "जानेवारी ते फेब्रुवारी", d=("For experienced travellers: the frozen Zanskar, ice hockey and winter festivals; access mainly by air.", "अनुभवी यात्रियों के लिए: जमी हुई ज़ांस्कर, आइस हॉकी और शीतकालीन उत्सव; पहुँच मुख्यतः हवाई मार्ग से।", "अनुभवी प्रवाशांसाठी: गोठलेली झांस्कर, आइस हॉकी आणि हिवाळी उत्सव; पोहोच मुख्यतः विमानाने.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Monthly temperature and precipitation normals (Leh, Kargil, Drass)", "मासिक तापमान और वर्षा सामान्य (लेह, कारगिल, द्रास)", "मासिक तापमान व पर्जन्य सरासरी (लेह, कारगिल, द्रास)"), "imd", "IMD climatological normals."),
        (L("Glacier retreat and climate vulnerability", "ग्लेशियर पीछे हटना और जलवायु संवेदनशीलता", "हिमनद माघार व हवामान असुरक्षितता"), "ndma", "Ladakh action plan on climate change; GSI glacier studies."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Mornings in Leh are sharp and bright: prayer flags snapping in the wind, the smell of fresh khambir bread from a bakery, and the first jeeps heading out to the passes. People greet each other — and visitors — with \"Julley\". Life slows to the pace of the thin air; climbing a monastery staircase leaves everyone breathless. In the villages, stone-and-mud houses with flat roofs stack firewood and fodder for winter, apricots dry on rooftops, and water channels run beside willow and poplar groves. Kargil's bazaars are busy with traders and travellers, and in Drass the snow lingers late. Then there is the silence of the high plateau, broken only by the wind and a herd of pashmina goats moving across it.",
        "लेह की सुबह तीखी और चमकीली होती है: हवा में फड़फड़ाते प्रार्थना ध्वज, बेकरी से ताज़ी खंबीर रोटी की ख़ुशबू, और दर्रों की ओर निकलती पहली जीपें। लोग एक-दूसरे का — और पर्यटकों का — \"जुले\" कहकर अभिवादन करते हैं। पतली हवा के साथ जीवन की रफ़्तार धीमी हो जाती है; किसी मठ की सीढ़ियाँ चढ़ते ही सबकी साँस फूल जाती है। गाँवों में सपाट छत वाले पत्थर-मिट्टी के घरों पर सर्दियों के लिए लकड़ी और चारा जमा होता है, छतों पर ख़ुबानियाँ सूखती हैं, और विलो व पॉपलर के झुरमुटों के पास पानी की नालियाँ बहती हैं। कारगिल के बाज़ार व्यापारियों और यात्रियों से भरे रहते हैं, और द्रास में बर्फ़ देर तक टिकी रहती है। फिर ऊँचे पठार का सन्नाटा है, जिसे केवल हवा और उसके पार गुज़रता पश्मीना बकरियों का झुंड तोड़ता है।",
        "लेहमधली सकाळ बोचरी आणि लख्ख असते: वाऱ्यावर फडफडणारे प्रार्थनाध्वज, बेकरीतून ताज्या खंबीर भाकरीचा सुगंध, आणि खिंडींकडे निघणाऱ्या पहिल्या जीप. लोक एकमेकांना — आणि पर्यटकांना — \"जुले\" म्हणून अभिवादन करतात. विरळ हवेबरोबर आयुष्याचा वेग मंदावतो; एखाद्या मठाच्या पायऱ्या चढताना सगळ्यांचा दम लागतो. गावांत सपाट छपरांच्या दगड-मातीच्या घरांवर हिवाळ्यासाठी लाकूडफाटा व चारा रचलेला असतो, छपरांवर जर्दाळू वाळत असतात, आणि विलो व पॉप्लरच्या राईंलगत पाण्याचे पाट वाहतात. कारगिलच्या बाजारपेठा व्यापारी व प्रवाशांनी गजबजलेल्या असतात, आणि द्रासमध्ये बर्फ उशिरापर्यंत टिकतो. आणि मग उंच पठाराची शांतता, जी फक्त वारा आणि त्यावरून सरकणारा पश्मिना शेळ्यांचा कळप भंग करतो."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Ladakh's population is small and spread across valleys separated by high passes. Leh district is predominantly Buddhist and Kargil district predominantly Muslim, with smaller Christian, Hindu and Sikh communities; most of the population belongs to Scheduled Tribes. Ladakhi (Bhoti) and Purgi are the main languages, with Balti, Shina (Brokskat), Changskat and Zanskari spoken in particular areas, and Hindi, Urdu and English used in administration and education. The Changpa of the Changthang plateau are pastoral nomads who herd yak, sheep and pashmina goats.",
        "लद्दाख की आबादी कम है और ऊँचे दर्रों से अलग घाटियों में फैली है। लेह ज़िले में बौद्ध और कारगिल ज़िले में मुस्लिम बहुसंख्यक हैं, साथ में छोटे ईसाई, हिंदू और सिख समुदाय हैं; अधिकांश आबादी अनुसूचित जनजातियों की है। लद्दाखी (भोटी) और पुरगी मुख्य भाषाएँ हैं; कुछ क्षेत्रों में बाल्टी, शिना (ब्रोकस्कट), चांगस्कट और ज़ांस्करी बोली जाती हैं, और प्रशासन व शिक्षा में हिंदी, उर्दू और अंग्रेज़ी का प्रयोग होता है। चांगथांग पठार के चांगपा पशुपालक घुमंतू हैं, जो याक, भेड़ और पश्मीना बकरियाँ पालते हैं।",
        "लडाखची लोकसंख्या कमी असून उंच खिंडींनी विभागलेल्या खोऱ्यांत पसरलेली आहे. लेह जिल्ह्यात बौद्ध आणि कारगिल जिल्ह्यात मुस्लिम बहुसंख्य आहेत, सोबत लहान ख्रिस्ती, हिंदू व शीख समुदाय आहेत; बहुतांश लोकसंख्या अनुसूचित जमातींची आहे. लडाखी (भोटी) आणि पुरगी या मुख्य भाषा आहेत; काही भागांत बाल्टी, शिना (ब्रोकस्कट), चांगस्कट व झांस्करी बोलल्या जातात, आणि प्रशासन व शिक्षणात हिंदी, उर्दू व इंग्रजी वापरल्या जातात. चांगथांग पठारावरील चांगपा हे भटके पशुपालक असून ते याक, मेंढ्या आणि पश्मिना शेळ्या पाळतात."),
        conf="Editorial"),
    table("kargil", L("Kargil district at the 2011 Census", "2011 की जनगणना में कारगिल ज़िला", "2011 च्या जनगणनेनुसार कारगिल जिल्हा"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "मान", "मूल्य"), "right")],
          [[L("Population", "जनसंख्या", "लोकसंख्या"), 140802], [L("Rural", "ग्रामीण", "ग्रामीण"), 124464], [L("Urban", "शहरी", "नागरी"), 16338],
           [L("Area (km²)", "क्षेत्रफल (किमी²)", "क्षेत्रफळ (किमी²)"), 14036], [L("Villages", "गाँव", "गावे"), 129]],
          "kargil-nic", KGL, period="2011",
          note=L("As published by the District Administration, Kargil. A matching official table for Leh district was not retrievable at access time, so no UT total is shown.",
                 "कारगिल ज़िला प्रशासन द्वारा प्रकाशित। लेह ज़िले की समान आधिकारिक तालिका उपलब्ध नहीं हो सकी, इसलिए केंद्र शासित प्रदेश का कुल आँकड़ा नहीं दिखाया गया।",
                 "कारगिल जिल्हा प्रशासनाने प्रसिद्ध केल्याप्रमाणे. लेह जिल्ह्याचा तसाच अधिकृत तक्ता मिळू न शकल्याने केंद्रशासित प्रदेशाची एकूण संख्या दाखवलेली नाही.")),
    lst("langs", [
        it3("bhoti", "Ladakhi (Bhoti)", "लद्दाखी (भोटी)", "लडाखी (भोटी)"), it3("purgi", "Purgi", "पुरगी", "पुरगी"), it3("balti", "Balti", "बाल्टी", "बाल्टी"),
        it3("shina", "Shina (Brokskat)", "शिना (ब्रोकस्कट)", "शिना (ब्रोकस्कट)"), it3("hindi", "Hindi", "हिंदी", "हिंदी"), it3("urdu", "Urdu", "उर्दू", "उर्दू"), it3("english", "English", "अंग्रेज़ी", "इंग्रजी"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("UT population, sex ratio, literacy and urban share (Census 2011)", "केंद्र शासित प्रदेश की जनसंख्या, लिंगानुपात, साक्षरता और शहरी हिस्सा (जनगणना 2011)", "केंद्रशासित प्रदेशाची लोकसंख्या, लिंग गुणोत्तर, साक्षरता व नागरी वाटा (जनगणना 2011)"), "census", "Sum Leh and Kargil district PCA; label as recomputed for the new UT."),
        (L("ST share by district", "ज़िलेवार अनुसूचित जनजाति हिस्सा", "जिल्हानिहाय अनुसूचित जमाती वाटा"), "census", "Census 2011 PCA ST tables."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "Check whether the MoHFW projections report Ladakh separately."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Rock carvings along the Indus and Zanskar show that people and traders have crossed Ladakh for thousands of years. Buddhism reached the region early, and from the 10th century a Ladakhi kingdom ruled from bases such as Shey and later Leh. Monasteries founded in this period — Alchi with its early murals, Lamayuru, and later Hemis and Thiksey — made Ladakh a centre of Tibetan Buddhist culture. Under the Namgyal dynasty in the 16th and 17th centuries, the nine-storey Leh Palace was built, and Leh grew as a caravan town on routes linking Punjab, Kashmir, Tibet and Central Asia.\n\nIn the 1830s the Dogra general Zorawar Singh brought Ladakh under the rulers of Jammu, and it became part of the princely State of Jammu and Kashmir. After 1947 it was a division of that State, with Leh and Kargil as districts from 1979, and autonomous hill councils for Leh (1995) and Kargil (2003). On 31 October 2019 Ladakh became a separate Union Territory.",
        "सिंधु और ज़ांस्कर के किनारे की शैल नक़्क़ाशियाँ बताती हैं कि हज़ारों वर्षों से लोग और व्यापारी लद्दाख से गुज़रते रहे हैं। बौद्ध धर्म यहाँ जल्दी पहुँचा, और 10वीं सदी से शे और बाद में लेह जैसे केंद्रों से एक लद्दाखी राज्य का शासन रहा। इस काल में स्थापित मठों — शुरुआती भित्तिचित्रों वाला अलची, लामायुरु, और बाद में हेमिस व थिकसे — ने लद्दाख को तिब्बती बौद्ध संस्कृति का केंद्र बनाया। 16वीं और 17वीं सदी में नामग्याल राजवंश के समय नौ मंज़िला लेह महल बना, और लेह पंजाब, कश्मीर, तिब्बत और मध्य एशिया को जोड़ने वाले कारवाँ मार्गों पर एक व्यापारिक नगर के रूप में बढ़ा।\n\n1830 के दशक में डोगरा सेनापति ज़ोरावर सिंह ने लद्दाख को जम्मू के शासकों के अधीन किया, और यह जम्मू-कश्मीर रियासत का हिस्सा बना। 1947 के बाद यह उस राज्य का एक संभाग रहा; 1979 से लेह और कारगिल ज़िले बने, और लेह (1995) व कारगिल (2003) के लिए स्वायत्त पहाड़ी परिषदें गठित हुईं। 31 अक्टूबर 2019 को लद्दाख अलग केंद्र शासित प्रदेश बना।",
        "सिंधू व झांस्करकाठची शिलाचित्रे दाखवतात की हजारो वर्षांपासून लोक आणि व्यापारी लडाखमधून ये-जा करत आले आहेत. बौद्ध धर्म येथे लवकर पोहोचला, आणि दहाव्या शतकापासून शे आणि नंतर लेहसारख्या केंद्रांवरून लडाखी राज्याचा कारभार चालला. या काळात स्थापन झालेल्या मठांनी — सुरुवातीच्या भित्तिचित्रांचा अलची, लामायुरू, आणि नंतर हेमिस व थिकसे — लडाखला तिबेटी बौद्ध संस्कृतीचे केंद्र बनवले. सोळाव्या-सतराव्या शतकात नामग्याल घराण्याच्या काळात नऊ मजली लेह राजवाडा बांधला गेला, आणि पंजाब, काश्मीर, तिबेट व मध्य आशियाला जोडणाऱ्या काफिला मार्गांवरील व्यापारी शहर म्हणून लेहचा विकास झाला.\n\n1830 च्या दशकात डोग्रा सेनापती जोरावर सिंग यांनी लडाख जम्मूच्या राज्यकर्त्यांच्या अधिपत्याखाली आणला, आणि तो जम्मू-काश्मीर संस्थानाचा भाग बनला. 1947 नंतर तो त्या राज्याचा एक विभाग होता; 1979 पासून लेह व कारगिल जिल्हे झाले, आणि लेह (1995) व कारगिल (2003) साठी स्वायत्त पर्वतीय परिषदा स्थापन झाल्या. 31 ऑक्टोबर 2019 रोजी लडाख स्वतंत्र केंद्रशासित प्रदेश झाला."),
        conf="Editorial"),
    timeline([
        ev("kingdom", 950, L("10th century", "10वीं सदी", "दहावे शतक"), L("Ladakhi kingdom established", "लद्दाखी राज्य की स्थापना", "लडाखी राज्याची स्थापना")),
        ev("alchi", 1050, L("11th century", "11वीं सदी", "अकरावे शतक"), L("Alchi monastery complex and its murals", "अलची मठ परिसर और उसके भित्तिचित्र", "अलची मठसंकुल व त्यातील भित्तिचित्रे")),
        ev("hemis", 1630, L("17th century", "17वीं सदी", "सतरावे शतक"), L("Hemis monastery founded; Leh Palace built under the Namgyals", "हेमिस मठ की स्थापना; नामग्यालों के समय लेह महल बना", "हेमिस मठाची स्थापना; नामग्यालांच्या काळात लेह राजवाडा")),
        ev("dogra", 1834, L("1834–42", "1834–42", "1834–42"), L("Dogra campaigns under Zorawar Singh", "ज़ोरावर सिंह के नेतृत्व में डोगरा अभियान", "जोरावर सिंगांच्या नेतृत्वाखाली डोग्रा मोहिमा")),
        ev("districts", 1979, L("1979", "1979", "1979"), L("Leh and Kargil districts formed", "लेह और कारगिल ज़िले बने", "लेह व कारगिल जिल्हे स्थापन")),
        ev("lahdc", 1995, L("1995", "1995", "1995"), L("Autonomous Hill Development Council, Leh", "स्वायत्त पहाड़ी विकास परिषद, लेह", "स्वायत्त पर्वतीय विकास परिषद, लेह")),
        ev("lahdck", 2003, L("2003", "2003", "2003"), L("Autonomous Hill Development Council, Kargil", "स्वायत्त पहाड़ी विकास परिषद, कारगिल", "स्वायत्त पर्वतीय विकास परिषद, कारगिल")),
        ev("ut", 2019, L("31 October 2019", "31 अक्टूबर 2019", "31 ऑक्टोबर 2019"), L("Ladakh becomes a Union Territory", "लद्दाख केंद्र शासित प्रदेश बना", "लडाख केंद्रशासित प्रदेश")),
    ]),
])

# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Monastery festivals are the high points of Ladakh's calendar. At Hemis, Thiksey, Lamayuru and other gompas, monks in masks and brocade perform cham dances that depict the victory of good over evil. Losar, the Ladakhi new year, falls in winter. In Kargil and the Suru valley, Shia Muslim observances such as Muharram are central to community life. Polo, played on village grounds and in Leh, and archery contests accompany many festivals.\n\nThe food is built for cold and altitude: thukpa and skyu (noodle and dough stews), momos, tsampa (roasted barley flour), khambir bread, butter tea and apricots fresh or dried.",
        "मठों के उत्सव लद्दाख के कैलेंडर के मुख्य आकर्षण हैं। हेमिस, थिकसे, लामायुरु और अन्य गोम्पाओं में मुखौटे और ज़री के वस्त्र पहने भिक्षु छम नृत्य करते हैं, जो बुराई पर अच्छाई की जीत दर्शाते हैं। लद्दाखी नववर्ष लोसर सर्दियों में आता है। कारगिल और सुरू घाटी में मुहर्रम जैसे शिया अनुष्ठान सामुदायिक जीवन के केंद्र में हैं। गाँव के मैदानों और लेह में खेला जाने वाला पोलो और तीरंदाज़ी प्रतियोगिताएँ कई उत्सवों का हिस्सा हैं।\n\nखान-पान ठंड और ऊँचाई के अनुकूल है: थुकपा और स्कयू (नूडल और आटे के शोरबे), मोमो, त्सम्पा (भुने जौ का आटा), खंबीर रोटी, मक्खन वाली चाय और ताज़ी या सूखी ख़ुबानी।",
        "मठांतील उत्सव हे लडाखच्या वर्षातील ठळक प्रसंग आहेत. हेमिस, थिकसे, लामायुरू आणि इतर गोंपांमध्ये मुखवटे व जरीचे पोशाख घातलेले भिक्षू छम नृत्य करतात, जे वाईटावर चांगल्याचा विजय दर्शवते. लडाखी नववर्ष लोसार हिवाळ्यात येते. कारगिल व सुरू खोऱ्यात मोहरमसारखे शिया धार्मिक विधी सामुदायिक जीवनाच्या केंद्रस्थानी आहेत. गावांच्या मैदानांवर व लेहमध्ये खेळला जाणारा पोलो आणि तिरंदाजी स्पर्धा अनेक उत्सवांचा भाग असतात.\n\nखाद्यपदार्थ थंडी आणि उंचीला साजेसे आहेत: थुकपा आणि स्क्यू (नूडल्स व कणकेचे रस्से), मोमो, त्सम्पा (भाजलेल्या बार्लीचे पीठ), खंबीर भाकरी, लोण्याचा चहा आणि ताजे किंवा सुके जर्दाळू."),
        conf="Editorial"),
    lst("festivals", [
        fest("hemis", ("Hemis Tsechu", "हेमिस त्सेचु", "हेमिस त्सेचू"), ("June–July", "जून–जुलाई", "जून–जुलै"), ("Masked cham dances in Hemis monastery's courtyard.", "हेमिस मठ के आँगन में मुखौटा छम नृत्य।", "हेमिस मठाच्या प्रांगणात मुखवटा छम नृत्य.")),
        fest("losar", ("Losar", "लोसर", "लोसार"), ("December–January", "दिसंबर–जनवरी", "डिसेंबर–जानेवारी"), ("Ladakhi new year, with family feasts and rituals.", "पारिवारिक भोज और अनुष्ठानों के साथ लद्दाखी नववर्ष।", "कौटुंबिक मेजवान्या व विधींसह लडाखी नववर्ष.")),
        fest("sindhu", ("Sindhu Darshan", "सिंधु दर्शन", "सिंधू दर्शन"), ("June", "जून", "जून"), ("Celebration on the banks of the Indus near Leh.", "लेह के पास सिंधु के तट पर उत्सव।", "लेहजवळ सिंधूच्या काठी उत्सव.")),
        fest("ladakhfest", ("Ladakh Festival", "लद्दाख महोत्सव", "लडाख महोत्सव"), ("September", "सितंबर", "सप्टेंबर"), ("Cultural parades, music, polo and archery.", "सांस्कृतिक झाँकियाँ, संगीत, पोलो और तीरंदाज़ी।", "सांस्कृतिक मिरवणुका, संगीत, पोलो आणि तिरंदाजी.")),
        fest("muharram", ("Muharram", "मुहर्रम", "मोहरम"), ("Lunar calendar", "चंद्र कैलेंडर", "चांद्र दिनदर्शिका"), ("Major observance in Kargil.", "कारगिल में प्रमुख धार्मिक अनुष्ठान।", "कारगिलमधील प्रमुख धार्मिक विधी.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("food", [
        it3("thukpa", "Thukpa and skyu", "थुकपा और स्कयू", "थुकपा व स्क्यू"), it3("momo", "Momos", "मोमो", "मोमो"),
        it3("tsampa", "Tsampa", "त्सम्पा", "त्सम्पा"), it3("khambir", "Khambir bread", "खंबीर रोटी", "खंबीर भाकरी"),
        it3("tea", "Butter tea (gur gur cha)", "मक्खन वाली चाय (गुड़ गुड़ चा)", "लोण्याचा चहा (गुर गुर चा)"), it3("apricot", "Apricots", "ख़ुबानी", "जर्दाळू"),
    ], layout="chips", title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
module(R, "economy", [
    prose("p1", L(
        "Ladakh's economy rests on government services and the armed forces, tourism, agriculture and livestock. Farming is limited to a short growing season in irrigated valleys — barley, wheat, peas, vegetables and orchards of apricot and apple — while the Changpa herders of Changthang produce the fine pashmina fibre. Tourism has grown fast since the 1970s and supports hotels, homestays, transport and trekking. Solar and geothermal resources are being explored for clean energy.\n\nPLFS data show unusually high participation: 66.2% of people aged 15+ and 61.0% of women were in the labour force in 2025, well above the national 59.3% and 40.0%. The unemployment rate fell from 8.1% in 2022 to 4.0% in 2025. MoSPI does not publish a separate GSDP series for the Union Territory.",
        "लद्दाख की अर्थव्यवस्था सरकारी सेवाओं और सशस्त्र बलों, पर्यटन, कृषि और पशुपालन पर टिकी है। सिंचित घाटियों में खेती का मौसम छोटा है — जौ, गेहूँ, मटर, सब्ज़ियाँ और ख़ुबानी व सेब के बाग़ — जबकि चांगथांग के चांगपा पशुपालक महीन पश्मीना रेशा पैदा करते हैं। 1970 के दशक से पर्यटन तेज़ी से बढ़ा है और होटल, होमस्टे, परिवहन और ट्रेकिंग को सहारा देता है। स्वच्छ ऊर्जा के लिए सौर और भूतापीय संसाधनों की खोज हो रही है।\n\nपीएलएफ़एस आँकड़े असामान्य रूप से ऊँची भागीदारी दिखाते हैं: 2025 में 15+ आयु के 66.2% लोग और 61.0% महिलाएँ श्रम बल में थीं, जो राष्ट्रीय 59.3% और 40.0% से काफ़ी अधिक है। बेरोज़गारी दर 2022 के 8.1% से घटकर 2025 में 4.0% हो गई। मोस्पी इस केंद्र शासित प्रदेश के लिए अलग जीएसडीपी शृंखला प्रकाशित नहीं करता।",
        "लडाखची अर्थव्यवस्था सरकारी सेवा व सशस्त्र दले, पर्यटन, शेती आणि पशुपालनावर आधारित आहे. सिंचित खोऱ्यांत शेतीचा हंगाम छोटा असतो — बार्ली, गहू, वाटाणा, भाज्या आणि जर्दाळू व सफरचंदाच्या बागा — तर चांगथांगमधील चांगपा पशुपालक तलम पश्मिना धागा निर्माण करतात. 1970 च्या दशकापासून पर्यटन झपाट्याने वाढले असून ते हॉटेले, होमस्टे, वाहतूक आणि ट्रेकिंगला आधार देते. स्वच्छ ऊर्जेसाठी सौर व भूऔष्णिक संसाधनांचा शोध सुरू आहे.\n\nपीएलएफएस आकडेवारी असामान्यपणे उच्च सहभाग दाखवते: 2025 मध्ये 15+ वयाच्या 66.2% व्यक्ती आणि 61.0% स्त्रिया श्रमशक्तीत होत्या — राष्ट्रीय 59.3% आणि 40.0% पेक्षा बऱ्याच जास्त. बेरोजगारी दर 2022 मधील 8.1% वरून 2025 मध्ये 4.0% झाला. मोस्पी या केंद्रशासित प्रदेशासाठी स्वतंत्र जीएसडीपी मालिका प्रसिद्ध करत नाही."),
        sources=["plfs"], conf="Official"),
    facts("f", plfs_facts("LA", NAME), title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    plfs_series("LA", NAME),
    gaps("g", [
        (L("GSDP and per capita income", "जीएसडीपी और प्रति व्यक्ति आय", "जीएसडीपी व दरडोई उत्पन्न"), "mospi", "Not in the MoSPI State series; check the UT Directorate of Economics & Statistics."),
        (L("Tourist arrivals", "पर्यटक आगमन", "पर्यटक आगमन"), "la-gov", "Tourism Department, UT Ladakh."),
        (L("Pashmina production", "पश्मीना उत्पादन", "पश्मिना उत्पादन"), "la-gov", "Sheep Husbandry Department."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Ladakh is a Union Territory without a legislature, administered by the President through a Lieutenant Governor, with an Advisor and senior officers of the UT Administration. Elected Ladakh Autonomous Hill Development Councils in Leh and Kargil handle many local development subjects. Ladakh elects one member to the Lok Sabha and has no seat in the Rajya Sabha.\n\nSince 2019, organisations from Leh and Kargil have sought safeguards for land, jobs and culture — including demands for statehood and inclusion under the Sixth Schedule — and have held talks with a committee of the Union Home Ministry. This page records the official position and will be updated as decisions are notified.",
        "लद्दाख बिना विधानसभा वाला केंद्र शासित प्रदेश है, जिसका प्रशासन राष्ट्रपति उपराज्यपाल के माध्यम से करते हैं; उनके साथ एक सलाहकार और केंद्र शासित प्रदेश प्रशासन के वरिष्ठ अधिकारी होते हैं। लेह और कारगिल में निर्वाचित लद्दाख स्वायत्त पहाड़ी विकास परिषदें कई स्थानीय विकास विषय सँभालती हैं। लद्दाख से लोकसभा का एक सदस्य चुना जाता है और राज्यसभा में इसकी कोई सीट नहीं है।\n\n2019 से लेह और कारगिल के संगठन भूमि, नौकरियों और संस्कृति के लिए सुरक्षा की माँग करते रहे हैं — जिसमें राज्य का दर्जा और छठी अनुसूची में शामिल करने की माँग भी है — और केंद्रीय गृह मंत्रालय की एक समिति के साथ बातचीत करते रहे हैं। यह पेज आधिकारिक स्थिति दर्ज करता है और निर्णय अधिसूचित होने पर अद्यतन किया जाएगा।",
        "लडाख हा विधिमंडळ नसलेला केंद्रशासित प्रदेश असून राष्ट्रपती नायब राज्यपालांमार्फत त्याचा कारभार पाहतात; त्यांच्यासोबत एक सल्लागार आणि केंद्रशासित प्रदेश प्रशासनाचे वरिष्ठ अधिकारी असतात. लेह व कारगिलमधील निवडून आलेल्या लडाख स्वायत्त पर्वतीय विकास परिषदा अनेक स्थानिक विकास विषय हाताळतात. लडाखमधून लोकसभेवर एक सदस्य निवडला जातो आणि राज्यसभेत त्याची जागा नाही.\n\n2019 पासून लेह व कारगिलमधील संघटनांनी जमीन, नोकऱ्या व संस्कृतीसाठी संरक्षणाची मागणी केली आहे — राज्याचा दर्जा आणि सहाव्या अनुसूचीत समावेशाच्या मागणीसह — आणि केंद्रीय गृह मंत्रालयाच्या समितीशी चर्चा केली आहे. हे पान अधिकृत भूमिका नोंदवते आणि निर्णय अधिसूचित झाल्यावर अद्ययावत केले जाईल."),
        conf="Editorial"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("portal", "UT Administration of Ladakh", "केंद्र शासित प्रदेश लद्दाख प्रशासन", "केंद्रशासित प्रदेश लडाख प्रशासन", url="https://ladakh.gov.in", src="la-gov"),
        it3("leh", "District Leh", "ज़िला लेह", "लेह जिल्हा", url="https://leh.nic.in", src="la-gov"),
        it3("kargil", "District Kargil", "ज़िला कारगिल", "कारगिल जिल्हा", url="https://kargil.nic.in", src="kargil-nic"),
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Chief Executive Councillors of LAHDC Leh and Kargil", "एलएएचडीसी लेह और कारगिल के मुख्य कार्यकारी पार्षद", "एलएएचडीसी लेह व कारगिलचे मुख्य कार्यकारी नगरसेवक"), "la-gov", "Council websites; record asOf (council terms and elections change)."),
        (L("Advisor to the Lieutenant Governor", "उपराज्यपाल के सलाहकार", "नायब राज्यपालांचे सल्लागार"), "la-gov", "UT Administration portal."),
        (L("Status of the Union Home Ministry's talks on safeguards", "सुरक्षा उपायों पर गृह मंत्रालय की वार्ता की स्थिति", "संरक्षणाबाबत गृह मंत्रालयाच्या चर्चेची स्थिती"), "pib", "Cite only official statements."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Ladakh's priority projects aim at all-weather access and clean energy. The Zojila tunnel will keep the Srinagar–Leh highway open through winter. Other projects announced by the Union Government include a large solar-and-storage park with a transmission line to the national grid, new tunnels on the Manali–Leh route and a geothermal pilot at Puga; these are listed as gaps until an official status page is linked.",
        "लद्दाख की प्राथमिक परियोजनाएँ हर मौसम में पहुँच और स्वच्छ ऊर्जा पर केंद्रित हैं। ज़ोजिला सुरंग श्रीनगर–लेह राजमार्ग को सर्दियों में भी खुला रखेगी। केंद्र सरकार द्वारा घोषित अन्य परियोजनाओं में राष्ट्रीय ग्रिड तक ट्रांसमिशन लाइन वाला बड़ा सौर-और-भंडारण पार्क, मनाली–लेह मार्ग पर नई सुरंगें और पुगा में भूतापीय पायलट परियोजना शामिल हैं; आधिकारिक स्थिति पेज जुड़ने तक इन्हें कमियों में रखा गया है।",
        "लडाखचे प्राधान्याचे प्रकल्प बारमाही संपर्क आणि स्वच्छ ऊर्जेवर केंद्रित आहेत. झोजिला बोगद्यामुळे श्रीनगर–लेह महामार्ग हिवाळ्यातही खुला राहील. केंद्र सरकारने जाहीर केलेल्या इतर प्रकल्पांत राष्ट्रीय ग्रिडपर्यंत पारेषण वाहिनी असलेले मोठे सौर-व-साठवण उद्यान, मनाली–लेह मार्गावरील नवे बोगदे आणि पुगा येथील भूऔष्णिक प्रायोगिक प्रकल्प यांचा समावेश आहे; अधिकृत स्थितीचे पान जोडले जाईपर्यंत ते त्रुटींमध्ये दाखवले आहेत."),
        sources=["sansad"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Ladakh renewable energy park and transmission line — official status", "लद्दाख नवीकरणीय ऊर्जा पार्क और ट्रांसमिशन लाइन — आधिकारिक स्थिति", "लडाख नवीकरणीय ऊर्जा उद्यान व पारेषण वाहिनी — अधिकृत स्थिती"), "mnre", "MNRE / Cabinet approval and progress."),
        (L("Shinku La tunnel (Himachal–Zanskar) — status", "शिंकु ला सुरंग (हिमाचल–ज़ांस्कर) — स्थिति", "शिंकू ला बोगदा (हिमाचल–झांस्कर) — स्थिती"), "morth", "MoRTH / BRO."),
        (L("Zojila tunnel — current completion date", "ज़ोजिला सुरंग — वर्तमान पूर्णता तिथि", "झोजिला बोगदा — सध्याची पूर्णत्व तारीख"), "morth", "Latest MoRTH / NHIDCL statement."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Air is Ladakh's year-round lifeline: Leh's Kushok Bakula Rimpochee Airport has daily flights to Delhi and other cities, and is one of the highest commercial airports in the world. By road, the Srinagar–Kargil–Leh highway crosses Zoji La and the Manali–Leh highway crosses several passes above 5,000 m; both are typically closed for part of winter by snow. Within Ladakh, roads over passes such as Khardung La and Chang La link Leh to Nubra and Pangong. There is no railway yet.",
        "हवाई सेवा लद्दाख की साल भर की जीवनरेखा है: लेह के कुशोक बकुला रिम्पोछे हवाई अड्डे से दिल्ली और अन्य शहरों के लिए रोज़ उड़ानें हैं, और यह दुनिया के सबसे ऊँचे व्यावसायिक हवाई अड्डों में है। सड़क मार्ग से श्रीनगर–कारगिल–लेह राजमार्ग ज़ोजिला पार करता है और मनाली–लेह राजमार्ग 5,000 मीटर से ऊँचे कई दर्रे पार करता है; दोनों आम तौर पर सर्दियों के कुछ हिस्से में बर्फ़ से बंद रहते हैं। लद्दाख के भीतर खारदुंग ला और चांग ला जैसे दर्रों से होकर सड़कें लेह को नुब्रा और पैंगोंग से जोड़ती हैं। अभी कोई रेल लाइन नहीं है।",
        "विमानसेवा ही लडाखची वर्षभराची जीवनरेखा आहे: लेहच्या कुशोक बकुला रिम्पोछे विमानतळावरून दिल्ली व इतर शहरांसाठी दररोज उड्डाणे होतात, आणि हा जगातील सर्वांत उंच व्यावसायिक विमानतळांपैकी एक आहे. रस्त्याने श्रीनगर–कारगिल–लेह महामार्ग झोजिला ओलांडतो आणि मनाली–लेह महामार्ग 5,000 मीटरहून उंच अनेक खिंडी ओलांडतो; दोन्ही सहसा हिवाळ्याच्या काही काळ बर्फामुळे बंद असतात. लडाखमध्ये खारदुंग ला आणि चांग ला सारख्या खिंडींवरून जाणारे रस्ते लेहला नुब्रा व पँगाँगशी जोडतात. अद्याप रेल्वेमार्ग नाही."),
        conf="Editorial"),
    gaps("g", [
        (L("Road length and pass opening dates", "सड़क की लंबाई और दर्रे खुलने की तारीख़ें", "रस्त्यांची लांबी व खिंडी खुल्या होण्याच्या तारखा"), "morth", "BRO / UT Public Works Department."),
        (L("Leh airport passenger traffic", "लेह हवाई अड्डा यात्री यातायात", "लेह विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
        (L("Bilaspur–Manali–Leh railway — status", "बिलासपुर–मनाली–लेह रेल लाइन — स्थिति", "बिलासपूर–मनाली–लेह रेल्वेमार्ग — स्थिती"), "railways", "Ministry of Railways."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Ladakh has some of India's best solar conditions — high altitude, clear skies and cold air — as well as geothermal heat in the Puga valley. Local supply has come from small hydro stations on the Indus and Suru and, in remote areas, diesel generators; the region was connected to the national grid by a high-altitude transmission line in 2019. Large renewable-energy parks have been planned to export power to the rest of India.",
        "लद्दाख में भारत की कुछ सबसे अच्छी सौर परिस्थितियाँ हैं — ऊँचाई, साफ़ आसमान और ठंडी हवा — साथ ही पुगा घाटी में भूतापीय ऊष्मा भी। स्थानीय आपूर्ति सिंधु और सुरू पर छोटे पनबिजली केंद्रों और दूरदराज़ के क्षेत्रों में डीज़ल जनरेटरों से होती रही है; 2019 में ऊँचाई पर बनी ट्रांसमिशन लाइन से यह क्षेत्र राष्ट्रीय ग्रिड से जुड़ा। शेष भारत को बिजली भेजने के लिए बड़े नवीकरणीय ऊर्जा पार्कों की योजना बनाई गई है।",
        "लडाखमध्ये भारतातील काही सर्वोत्तम सौर परिस्थिती आहे — उंची, निरभ्र आकाश आणि थंड हवा — तसेच पुगा खोऱ्यात भूऔष्णिक उष्णताही आहे. स्थानिक पुरवठा सिंधू व सुरूवरील लहान जलविद्युत केंद्रांतून आणि दुर्गम भागांत डिझेल जनित्रांतून होत आला आहे; 2019 मध्ये उंचावरील पारेषण वाहिनीद्वारे हा प्रदेश राष्ट्रीय ग्रिडला जोडला गेला. उर्वरित भारताला वीज पाठवण्यासाठी मोठ्या नवीकरणीय ऊर्जा उद्यानांचे नियोजन झाले आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Solar and geothermal potential (official estimates)", "सौर और भूतापीय क्षमता (आधिकारिक अनुमान)", "सौर व भूऔष्णिक क्षमता (अधिकृत अंदाज)"), "mnre", "MNRE / NIWE."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Mobile and internet coverage has expanded in Leh, Kargil and the main valleys, but many high villages, passes and trekking routes still have little or no signal. Visitors should note that prepaid connections from other States may not work in Ladakh, while postpaid connections generally do.",
        "लेह, कारगिल और मुख्य घाटियों में मोबाइल और इंटरनेट कवरेज बढ़ा है, लेकिन कई ऊँचे गाँवों, दर्रों और ट्रेकिंग मार्गों पर अब भी बहुत कम या कोई सिग्नल नहीं है। पर्यटक ध्यान दें कि दूसरे राज्यों के प्रीपेड कनेक्शन लद्दाख में काम न करें, जबकि पोस्टपेड आम तौर पर काम करते हैं।",
        "लेह, कारगिल आणि मुख्य खोऱ्यांत मोबाइल व इंटरनेट व्याप्ती वाढली आहे, पण अनेक उंचावरील गावे, खिंडी आणि ट्रेकिंग मार्गांवर अजूनही फारसा किंवा अजिबात सिग्नल नसतो. पर्यटकांनी लक्षात ठेवावे की इतर राज्यांतील प्रीपेड जोडण्या लडाखमध्ये चालू शकत नाहीत, तर पोस्टपेड सहसा चालतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Village connectivity (mobile and broadband)", "गाँवों में संपर्क (मोबाइल और ब्रॉडबैंड)", "गावांतील संपर्क (मोबाइल व ब्रॉडबँड)"), "india-gov", "Department of Telecommunications / USOF."),
        (L("Prepaid-SIM rules for visitors", "पर्यटकों के लिए प्रीपेड सिम नियम", "पर्यटकांसाठी प्रीपेड सिम नियम"), "india-gov", "Confirm the current rule with DoT before publishing as fact."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("LA", NAME)
module(R, "education", [
    prose("p1", L(
        "Higher education in Ladakh is young and small. The 2021-22 AISHE survey recorded 2 universities and 6 colleges, and a gross enrolment ratio of 11.5% for ages 18–23, up from 7.9% in 2019-20 but well below the national 28.4%; many students still leave for Jammu, Srinagar, Chandigarh and Delhi. The University of Ladakh, set up in 2018, has campuses in Leh and Kargil. Ladakh is also known for alternative schooling experiments, such as the Students' Educational and Cultural Movement of Ladakh (SECMOL).",
        "लद्दाख में उच्च शिक्षा नई और छोटी है। 2021-22 के एआईएसएचई सर्वेक्षण में 2 विश्वविद्यालय और 6 कॉलेज दर्ज हुए, और 18–23 आयु का सकल नामांकन अनुपात 11.5% था — 2019-20 के 7.9% से अधिक, लेकिन राष्ट्रीय 28.4% से काफ़ी कम; कई छात्र अब भी जम्मू, श्रीनगर, चंडीगढ़ और दिल्ली जाते हैं। 2018 में स्थापित लद्दाख विश्वविद्यालय के परिसर लेह और कारगिल में हैं। लद्दाख वैकल्पिक शिक्षा के प्रयोगों के लिए भी जाना जाता है, जैसे स्टूडेंट्स एजुकेशनल एंड कल्चरल मूवमेंट ऑफ़ लद्दाख (सेकमोल)।",
        "लडाखमधील उच्चशिक्षण नवे आणि लहान आहे. 2021-22 च्या एआयएसएचई सर्वेक्षणात 2 विद्यापीठे आणि 6 महाविद्यालये नोंदली गेली, आणि 18–23 वयोगटाचे एकूण नोंदणी गुणोत्तर 11.5% होते — 2019-20 च्या 7.9% पेक्षा जास्त, पण राष्ट्रीय 28.4% पेक्षा बरेच कमी; अनेक विद्यार्थी अजूनही जम्मू, श्रीनगर, चंदीगड आणि दिल्लीला जातात. 2018 मध्ये स्थापन झालेल्या लडाख विद्यापीठाचे परिसर लेह व कारगिलमध्ये आहेत. स्टुडंट्स एज्युकेशनल अँड कल्चरल मूव्हमेंट ऑफ लडाख (सेकमोल) सारख्या पर्यायी शिक्षण प्रयोगांसाठीही लडाख ओळखला जातो."),
        sources=["aishe"], conf="Official"),
    ef, es,
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Literacy rate (Census 2011, Leh + Kargil)", "साक्षरता दर (जनगणना 2011, लेह + कारगिल)", "साक्षरता दर (जनगणना 2011, लेह + कारगिल)"), "census", "Census 2011 PCA."),
    ]),
])

# ---------------- O. Health ----------------
module(R, "health", [
    prose("p1", L(
        "NFHS-5 (2019-21), the first survey to report Ladakh separately, found that 95.1% of births took place in health facilities, above the national 88.6%, while 30.5% of children under five were stunted, close to the national level. Health services are concentrated in Leh and Kargil, and the distances, altitude and winter road closures make emergency care difficult in remote valleys.\n\nFor visitors, acute mountain sickness is the main health risk. Rest for at least the first day or two after arriving in Leh by air, avoid exertion and alcohol, and descend if symptoms worsen.",
        "एनएफ़एचएस-5 (2019-21), जो लद्दाख के आँकड़े अलग से देने वाला पहला सर्वेक्षण है, के अनुसार 95.1% प्रसव स्वास्थ्य संस्थानों में हुए, जो राष्ट्रीय 88.6% से अधिक है, जबकि पाँच वर्ष से कम आयु के 30.5% बच्चे ठिगने थे — राष्ट्रीय स्तर के क़रीब। स्वास्थ्य सेवाएँ लेह और कारगिल में केंद्रित हैं, और दूरी, ऊँचाई और सर्दियों में सड़कें बंद होने से दूरदराज़ की घाटियों में आपात चिकित्सा कठिन हो जाती है।\n\nपर्यटकों के लिए ऊँचाई की तीव्र बीमारी मुख्य स्वास्थ्य ख़तरा है। हवाई मार्ग से लेह पहुँचने के बाद कम से कम पहले एक-दो दिन आराम करें, मेहनत और शराब से बचें, और लक्षण बढ़ने पर नीचे उतरें।",
        "एनएफएचएस-5 (2019-21) — लडाखची आकडेवारी स्वतंत्रपणे देणारे पहिले सर्वेक्षण — नुसार 95.1% प्रसूती आरोग्य संस्थांत झाल्या, जे राष्ट्रीय 88.6% पेक्षा जास्त आहे, तर पाच वर्षांखालील 30.5% मुले खुजी होती — राष्ट्रीय पातळीच्या जवळ. आरोग्यसेवा लेह व कारगिलमध्ये एकवटलेल्या आहेत, आणि अंतर, उंची व हिवाळ्यात बंद होणारे रस्ते यांमुळे दुर्गम खोऱ्यांत आपत्कालीन उपचार कठीण होतात.\n\nपर्यटकांसाठी उंचीमुळे होणारा तीव्र आजार हा मुख्य आरोग्य धोका आहे. विमानाने लेहला पोहोचल्यावर किमान पहिले एक-दोन दिवस विश्रांती घ्या, श्रम व मद्य टाळा, आणि लक्षणे वाढल्यास खालच्या उंचीवर जा."),
        sources=["nfhs"], conf="Official"),
    facts("nfhs", nfhs_facts("LA"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Infant and under-five mortality", "शिशु और पाँच वर्ष से कम आयु की मृत्यु दर", "अर्भक व पाच वर्षांखालील मृत्युदर"), "srs", "SRS does not yet report Ladakh separately."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India; UT Health Department."),
    ]),
])

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Ladakh's cold desert supports a remarkable range of high-altitude wildlife. Hemis National Park is one of the best places in the world to see the snow leopard, along with Ladakh urial, Tibetan argali and bharal. The Changthang plateau is home to the kiang (Tibetan wild ass) and the black-necked crane, which breeds on its wetlands. Two of those wetlands, Tsomoriri and Tso Kar, are Ramsar sites. Forest cover is very small in a landscape that is mostly rock, scree and alpine steppe — 2,285.92 km² in ISFR 2023.",
        "लद्दाख का ठंडा रेगिस्तान ऊँचाई के वन्यजीवों की उल्लेखनीय विविधता को सहारा देता है। हेमिस राष्ट्रीय उद्यान हिम तेंदुआ देखने के लिए दुनिया की सबसे अच्छी जगहों में है; यहाँ लद्दाख उरियल, तिब्बती अर्गली और भरल भी हैं। चांगथांग पठार कियांग (तिब्बती जंगली गधा) और काली गर्दन वाले सारस का घर है, जो इसकी आर्द्रभूमियों में प्रजनन करता है। इनमें से दो आर्द्रभूमियाँ, त्सोमोरीरी और त्सो कार, रामसर स्थल हैं। चट्टानों, पत्थरों और अल्पाइन स्टेपी वाले इस भू-दृश्य में वन आवरण बहुत कम है — आईएसएफ़आर 2023 में 2,285.92 किमी²।",
        "लडाखचे थंड वाळवंट उंचावरील वन्यजीवांच्या उल्लेखनीय विविधतेला आधार देते. हेमिस राष्ट्रीय उद्यान हे हिमबिबट्या पाहण्यासाठी जगातील सर्वोत्तम ठिकाणांपैकी एक आहे; येथे लडाख उरियल, तिबेटी अर्गली आणि भरलही आहेत. चांगथांग पठारावर कियांग (तिबेटी रानगाढव) आणि काळ्या मानेचा करकोचा आढळतो, जो तेथील पाणथळांत प्रजनन करतो. त्यांपैकी दोन पाणथळे, त्सोमोरिरी आणि त्सो कार, रामसर स्थळे आहेत. खडक, दगडगोटे आणि अल्पाइन गवताळ प्रदेश असलेल्या या भूदृश्यात वनाच्छादन फारच कमी आहे — आयएसएफआर 2023 नुसार 2,285.92 किमी²."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(2285.92, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023. Percentage not shown because the area base is disputed."), "number", "higher-is-better",
             previous=dp(2278.55, "km²", "2021", "calendar", "fsi", LS_FOREST)),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हे.)", "क्षेत्र (हे.)"), "right")],
          [[L("Tsomoriri", "त्सोमोरीरी", "त्सोमोरिरी"), "19 Aug 2002", 12000], [L("Tso Kar Wetland Complex", "त्सो कार आर्द्रभूमि परिसर", "त्सो कार पाणथळ संकुल"), "17 Nov 2020", 9577]],
          "indian-wetlands", RAMSAR, note=L("India has 99 Ramsar sites (list as on 21 April 2026).", "भारत में 99 रामसर स्थल हैं (21 अप्रैल 2026 की सूची)।", "भारतात 99 रामसर स्थळे आहेत (21 एप्रिल 2026 ची यादी).")),
    lst("protected", [
        it3("hemis", "Hemis National Park", "हेमिस राष्ट्रीय उद्यान", "हेमिस राष्ट्रीय उद्यान", m=("Snow leopard", "हिम तेंदुआ", "हिमबिबट्या")),
        it3("changthang", "Changthang Cold Desert Wildlife Sanctuary", "चांगथांग शीत मरुस्थल वन्यजीव अभयारण्य", "चांगथांग शीत वाळवंट वन्यजीव अभयारण्य", m=("Kiang, black-necked crane", "कियांग, काली गर्दन वाला सारस", "कियांग, काळ्या मानेचा करकोचा")),
        it3("karakoram", "Karakoram (Nubra–Shyok) Wildlife Sanctuary", "काराकोरम (नुब्रा–श्योक) वन्यजीव अभयारण्य", "काराकोरम (नुब्रा–श्योक) वन्यजीव अभयारण्य", m=("Northern valleys", "उत्तरी घाटियाँ", "उत्तरेकडील खोरी")),
    ], title=L("Protected areas", "संरक्षित क्षेत्र", "संरक्षित क्षेत्रे"), conf="Editorial"),
    lst("species", [
        it3("snowleopard", "Snow leopard", "हिम तेंदुआ", "हिमबिबट्या"), it3("crane", "Black-necked crane", "काली गर्दन वाला सारस", "काळ्या मानेचा करकोचा"),
        it3("kiang", "Kiang", "कियांग", "कियांग"), it3("urial", "Ladakh urial", "लद्दाख उरियल", "लडाख उरियल"),
        it3("bharal", "Bharal (blue sheep)", "भरल (नीली भेड़)", "भरल (निळी मेंढी)"), it3("marmot", "Himalayan marmot", "हिमालयी मर्मोट", "हिमालयी मार्मोट"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Protected area extents", "संरक्षित क्षेत्रों का विस्तार", "संरक्षित क्षेत्रांचा विस्तार"), "moefcc", "Wildlife Institute of India / UT Wildlife Department."),
        (L("Glacier inventory", "ग्लेशियर सूची", "हिमनद सूची"), "moefcc", "GSI / ISRO glacier atlas."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "With almost no rain, Ladakh's farms depend on snow and glacier melt carried to fields by channels, so water arrives late in spring, when sowing needs it most. Communities have responded with artificial glaciers and \"ice stupas\" — structures that freeze winter streamflow and release it as they melt in April and May. The Indus, Shyok, Zanskar and Suru are the main rivers; their flows are expected to change as glaciers retreat.",
        "लगभग बिना वर्षा वाले लद्दाख के खेत नालियों के ज़रिए खेतों तक पहुँचने वाले बर्फ़ और ग्लेशियर के पिघले पानी पर निर्भर हैं, इसलिए पानी वसंत में देर से आता है, जब बुआई को उसकी सबसे ज़्यादा ज़रूरत होती है। समुदायों ने इसका जवाब कृत्रिम ग्लेशियरों और \"आइस स्तूपों\" से दिया है — ऐसी संरचनाएँ जो सर्दियों के प्रवाह को जमा देती हैं और अप्रैल-मई में पिघलकर पानी देती हैं। सिंधु, श्योक, ज़ांस्कर और सुरू मुख्य नदियाँ हैं; ग्लेशियरों के पीछे हटने से इनके प्रवाह में बदलाव की आशंका है।",
        "जवळपास पाऊस नसलेल्या लडाखमधील शेती पाटांद्वारे शेतांपर्यंत पोहोचणाऱ्या बर्फ व हिमनदीच्या वितळलेल्या पाण्यावर अवलंबून आहे, त्यामुळे पाणी वसंतात उशिरा येते — नेमके पेरणीला सर्वाधिक गरज असताना. यावर समुदायांनी कृत्रिम हिमनद्या आणि \"आइस स्तूप\" यांचा उपाय शोधला आहे — हिवाळ्यातील प्रवाह गोठवून एप्रिल-मेमध्ये वितळताना पाणी देणाऱ्या रचना. सिंधू, श्योक, झांस्कर आणि सुरू या मुख्य नद्या आहेत; हिमनद्या मागे सरकल्याने त्यांच्या प्रवाहात बदल होण्याची अपेक्षा आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Rural tap-water coverage", "ग्रामीण नल जल कवरेज", "ग्रामीण नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
        (L("Irrigated area", "सिंचित क्षेत्र", "सिंचित क्षेत्र"), "la-gov", "UT Agriculture Department."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "The main hazards are those of high mountains: flash floods from cloudbursts (as in Leh in August 2010), avalanches and landslides on the passes, extreme cold and sudden road closures. Visitors must acclimatise, carry warm clothing and enough fuel and cash, and check road status before crossing passes. Several areas near the borders — including Nubra, Pangong, Tso Moriri and parts of Changthang — require a protected-area permit, available through the district administration's online system.",
        "मुख्य ख़तरे ऊँचे पहाड़ों वाले हैं: बादल फटने से अचानक बाढ़ (जैसे अगस्त 2010 में लेह में), दर्रों पर हिमस्खलन और भूस्खलन, कड़ाके की ठंड और अचानक सड़कें बंद होना। पर्यटकों को ऊँचाई के अनुकूल होना चाहिए, गर्म कपड़े और पर्याप्त ईंधन व नक़दी रखनी चाहिए, और दर्रे पार करने से पहले सड़क की स्थिति देखनी चाहिए। सीमा के पास के कई क्षेत्रों — नुब्रा, पैंगोंग, त्सो मोरीरी और चांगथांग के कुछ हिस्सों — के लिए संरक्षित क्षेत्र परमिट ज़रूरी है, जो ज़िला प्रशासन की ऑनलाइन प्रणाली से मिलता है।",
        "मुख्य धोके उंच पर्वतांचे आहेत: ढगफुटीमुळे अचानक येणारे पूर (ऑगस्ट 2010 मध्ये लेहमध्ये आला तसा), खिंडींवरील हिमस्खलन व दरडी, कडाक्याची थंडी आणि अचानक बंद होणारे रस्ते. पर्यटकांनी उंचीशी जुळवून घ्यावे, उबदार कपडे आणि पुरेसे इंधन व रोकड बाळगावी, आणि खिंडी ओलांडण्यापूर्वी रस्त्यांची स्थिती तपासावी. सीमेजवळील अनेक भागांसाठी — नुब्रा, पँगाँग, त्सो मोरिरी आणि चांगथांगचा काही भाग — संरक्षित क्षेत्र परवाना आवश्यक असतो, जो जिल्हा प्रशासनाच्या ऑनलाइन प्रणालीद्वारे मिळतो."),
        conf="Editorial"),
    emergency_table(("Ladakh", "लद्दाख", "लडाख")),
    lst("links", [
        it3("leh", "District Leh (permits, advisories)", "ज़िला लेह (परमिट, परामर्श)", "लेह जिल्हा (परवाने, सूचना)", url="https://leh.nic.in", src="la-gov"),
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Protected-area permit rules and fees (current)", "संरक्षित क्षेत्र परमिट नियम और शुल्क (वर्तमान)", "संरक्षित क्षेत्र परवाना नियम व शुल्क (सध्याचे)"), "la-gov", "District Leh / Kargil notifications."),
        (L("Avalanche and flash-flood hazard maps", "हिमस्खलन और अचानक बाढ़ जोखिम मानचित्र", "हिमस्खलन व आकस्मिक पूर धोका नकाशे"), "ndma", "DGRE / NDMA."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Ladakh has four registered Geographical Indications in the GI Registry's list as on 31 December 2025, all filed after it became a Union Territory: Pashmina wool from the Changthang goats, the white-kernelled Raktsey Karpo apricot, seabuckthorn berries and Shingskos wood carving.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में लद्दाख के चार पंजीकृत भौगोलिक संकेतक हैं, जो सभी केंद्र शासित प्रदेश बनने के बाद दाखिल हुए: चांगथांग की बकरियों का पश्मीना ऊन, सफ़ेद गिरी वाली रक्त्से कार्पो ख़ुबानी, सीबकथॉर्न बेरी और शिंगस्कोस काष्ठ नक़्क़ाशी।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत लडाखची चार नोंदणीकृत भौगोलिक मानांकने आहेत, आणि सर्व केंद्रशासित प्रदेश झाल्यानंतर दाखल झाली: चांगथांगच्या शेळ्यांची पश्मिना लोकर, पांढऱ्या गराचा रक्त्से कार्पो जर्दाळू, सीबकथॉर्न बेरी आणि शिंगस्कोस लाकडी कोरीवकाम."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Most visitors base themselves in Leh and make trips over high passes to the Nubra valley and Pangong Tso, with longer journeys to Tso Moriri, Zanskar and the Kargil–Suru region. Monasteries, trekking, mountaineering, river rafting on the Indus and Zanskar, and winter treks on the frozen Zanskar (the Chadar) are the main draws. The Kargil War Memorial at Drass receives a steady flow of visitors.",
        "अधिकांश पर्यटक लेह में ठहरते हैं और ऊँचे दर्रों के पार नुब्रा घाटी और पैंगोंग त्सो जाते हैं; लंबी यात्राएँ त्सो मोरीरी, ज़ांस्कर और कारगिल–सुरू क्षेत्र तक होती हैं। मठ, ट्रेकिंग, पर्वतारोहण, सिंधु और ज़ांस्कर में रिवर राफ़्टिंग, और जमी हुई ज़ांस्कर पर सर्दियों का ट्रेक (चादर) मुख्य आकर्षण हैं। द्रास के कारगिल युद्ध स्मारक पर लगातार आगंतुक आते हैं।",
        "बहुतेक पर्यटक लेहमध्ये मुक्काम करून उंच खिंडी ओलांडत नुब्रा खोरे आणि पँगाँग त्सोला जातात; त्सो मोरिरी, झांस्कर आणि कारगिल–सुरू भागापर्यंत लांबचे प्रवासही होतात. मठ, ट्रेकिंग, गिर्यारोहण, सिंधू व झांस्करमधील रिव्हर राफ्टिंग, आणि गोठलेल्या झांस्करवरील हिवाळी ट्रेक (चादर) ही मुख्य आकर्षणे आहेत. द्रास येथील कारगिल युद्ध स्मारकाला सतत पर्यटक भेट देतात."),
        conf="Editorial"),
    lst("places", [
        it3("leh", "Leh Palace, Shanti Stupa and the old town", "लेह महल, शांति स्तूप और पुराना शहर", "लेह राजवाडा, शांती स्तूप आणि जुने शहर", m=("Leh", "लेह", "लेह")),
        it3("gompas", "Hemis, Thiksey, Alchi and Lamayuru monasteries", "हेमिस, थिकसे, अलची और लामायुरु मठ", "हेमिस, थिकसे, अलची व लामायुरू मठ", m=("Monasteries", "मठ", "मठ")),
        it3("nubra", "Nubra valley and Diskit", "नुब्रा घाटी और डिस्किट", "नुब्रा खोरे आणि डिस्किट", m=("Valleys, dunes", "घाटियाँ, टीले", "खोरी, ढिगारे")),
        it3("pangong", "Pangong Tso", "पैंगोंग त्सो", "पँगाँग त्सो", m=("High lake; permit needed", "ऊँची झील; परमिट ज़रूरी", "उंचावरील सरोवर; परवाना आवश्यक")),
        it3("tsomoriri", "Tso Moriri and Tso Kar", "त्सो मोरीरी और त्सो कार", "त्सो मोरिरी व त्सो कार", m=("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळे")),
        it3("zanskar", "Zanskar valley", "ज़ांस्कर घाटी", "झांस्कर खोरे", m=("Remote valley, trekking", "दूरस्थ घाटी, ट्रेकिंग", "दुर्गम खोरे, ट्रेकिंग")),
        it3("drass", "Kargil War Memorial, Drass", "कारगिल युद्ध स्मारक, द्रास", "कारगिल युद्ध स्मारक, द्रास", m=("Memorial", "स्मारक", "स्मारक")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Acclimatise in Leh; Leh Palace, Shanti Stupa, then Thiksey, Shey and Hemis.", "लेह में अनुकूलन; लेह महल, शांति स्तूप, फिर थिकसे, शे और हेमिस।", "लेहमध्ये जुळवून घ्या; लेह राजवाडा, शांती स्तूप, नंतर थिकसे, शे व हेमिस.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Add Nubra over Khardung La and a night at Pangong Tso (permits required).", "खारदुंग ला पार नुब्रा और पैंगोंग त्सो पर एक रात जोड़ें (परमिट ज़रूरी)।", "खारदुंग ला ओलांडून नुब्रा आणि पँगाँग त्सोवर एक रात्र जोडा (परवाने आवश्यक).")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Continue west via Lamayuru to Kargil and Drass, or south-east to Tso Moriri.", "लामायुरु होते हुए पश्चिम में कारगिल और द्रास, या दक्षिण-पूर्व में त्सो मोरीरी जाएँ।", "लामायुरूमार्गे पश्चिमेला कारगिल व द्रास, किंवा आग्नेयेला त्सो मोरिरी.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    gaps("g", [
        (L("Tourist arrivals (domestic and foreign)", "पर्यटक आगमन (घरेलू और विदेशी)", "पर्यटक आगमन (देशी व परदेशी)"), "la-gov", "Tourism Department, UT Ladakh."),
        (L("Carrying-capacity and environmental fee rules", "वहन क्षमता और पर्यावरण शुल्क नियम", "वहनक्षमता व पर्यावरण शुल्क नियम"), "la-gov", "District notifications."),
    ]),
])

# ---------------- U. Cities ----------------
module(R, "cities", [
    lst("towns", [
        it3("leh", "Leh", "लेह", "लेह", d=("Administrative centre and main town; old town below the palace, bazaar, monasteries nearby.", "प्रशासनिक केंद्र और मुख्य नगर; महल के नीचे पुराना शहर, बाज़ार, पास में मठ।", "प्रशासकीय केंद्र व मुख्य शहर; राजवाड्याखाली जुने शहर, बाजार, जवळ मठ."), m=("Capital", "राजधानी", "राजधानी")),
        it3("kargil", "Kargil", "कारगिल", "कारगिल", d=("Second town, on the Suru; gateway to Zanskar and the Suru valley.", "सुरू पर दूसरा बड़ा नगर; ज़ांस्कर और सुरू घाटी का प्रवेश द्वार।", "सुरू नदीकाठचे दुसरे शहर; झांस्कर व सुरू खोऱ्याचे प्रवेशद्वार."), m=("District HQ", "ज़िला मुख्यालय", "जिल्हा मुख्यालय")),
        it3("drass", "Drass", "द्रास", "द्रास", d=("On the highway below Zoji La; known for extreme winter cold.", "ज़ोजिला के नीचे राजमार्ग पर; कड़ाके की सर्दी के लिए प्रसिद्ध।", "झोजिलाखालील महामार्गावर; कडाक्याच्या थंडीसाठी प्रसिद्ध."), m=("Town", "कस्बा", "गाव")),
        it3("padum", "Padum", "पदुम", "पदुम", d=("Main settlement of Zanskar.", "ज़ांस्कर की मुख्य बस्ती।", "झांस्करमधील मुख्य वस्ती."), m=("Zanskar", "ज़ांस्कर", "झांस्कर")),
        it3("diskit", "Diskit", "डिस्किट", "डिस्किट", d=("Main village of the Nubra valley, with its hilltop monastery.", "नुब्रा घाटी का मुख्य गाँव, पहाड़ी पर मठ के साथ।", "नुब्रा खोऱ्यातील मुख्य गाव, टेकडीवरील मठासह."), m=("Nubra", "नुब्रा", "नुब्रा")),
    ], title=L("Main towns", "मुख्य नगर", "मुख्य शहरे"), conf="Editorial"),
    gaps("g", [
        (L("Town populations (Census 2011)", "नगरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 town directory."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Ice hockey is Ladakh's signature winter sport, played on frozen ponds and rinks in Leh and its villages, and Ladakhi players make up much of India's national teams; Leh has hosted ice events of the Khelo India Winter Games. Polo, archery and football are the main summer sports, and Ladakh's altitude makes it a training base for endurance athletes and the scene of high-altitude marathons.",
        "आइस हॉकी लद्दाख का पहचान बन चुका शीतकालीन खेल है, जो लेह और उसके गाँवों के जमे तालाबों और रिंकों पर खेला जाता है, और भारत की राष्ट्रीय टीमों में लद्दाखी खिलाड़ियों की बड़ी संख्या होती है; लेह खेलो इंडिया शीतकालीन खेलों की बर्फ़ प्रतियोगिताओं की मेज़बानी कर चुका है। पोलो, तीरंदाज़ी और फ़ुटबॉल गर्मियों के मुख्य खेल हैं, और लद्दाख की ऊँचाई इसे सहनशक्ति एथलीटों के प्रशिक्षण और ऊँचाई वाली मैराथनों का केंद्र बनाती है।",
        "आइस हॉकी हा लडाखचा ओळख बनलेला हिवाळी खेळ असून लेह व आसपासच्या गावांतील गोठलेल्या तलावांवर आणि रिंकवर खेळला जातो; भारताच्या राष्ट्रीय संघांत लडाखी खेळाडूंचा मोठा वाटा असतो, आणि लेहने खेलो इंडिया हिवाळी स्पर्धांतील बर्फावरील स्पर्धांचे यजमानपद भूषवले आहे. पोलो, तिरंदाजी आणि फुटबॉल हे उन्हाळ्यातील मुख्य खेळ आहेत, आणि उंचीमुळे लडाख सहनशक्ती खेळाडूंच्या सरावाचे व उंचावरील मॅरेथॉनचे केंद्र बनले आहे."),
        conf="Editorial"),
    lst("venues", [
        it3("nds", "NDS Sports Complex (ice rink), Leh", "एनडीएस खेल परिसर (आइस रिंक), लेह", "एनडीएस क्रीडा संकुल (आइस रिंक), लेह"),
        it3("polo", "Polo Ground, Leh", "पोलो ग्राउंड, लेह", "पोलो मैदान, लेह"),
    ], layout="chips", title=L("Venues", "मैदान", "मैदाने"), conf="Editorial"),
])

# ---------------- W. Personalities ----------------
module(R, "personalities", [
    lst("people", [
        it3("bakula", "Kushok Bakula Rimpochee", "कुशोक बकुला रिम्पोछे", "कुशोक बकुला रिम्पोछे", d=("Buddhist leader and statesman; Leh's airport is named after him.", "बौद्ध धर्मगुरु और राजनेता; लेह हवाई अड्डा उनके नाम पर है।", "बौद्ध धर्मगुरू व राजनेते; लेह विमानतळाला त्यांचे नाव आहे."), m=("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        it3("rinchen", "Colonel Chewang Rinchen", "कर्नल छेवांग रिनचेन", "कर्नल छेवांग रिनचेन", d=("Soldier twice awarded the Maha Vir Chakra; known as the \"Lion of Ladakh\".", "दो बार महावीर चक्र से सम्मानित सैनिक; \"लद्दाख के शेर\" के रूप में प्रसिद्ध।", "दोनदा महावीर चक्राने सन्मानित सैनिक; \"लडाखचा सिंह\" म्हणून ओळख."), m=("Armed forces", "सशस्त्र बल", "सशस्त्र दले")),
        it3("norphel", "Chewang Norphel", "छेवांग नोरफेल", "छेवांग नोरफेल", d=("Civil engineer who built artificial glaciers for village irrigation.", "सिविल इंजीनियर, जिन्होंने गाँवों की सिंचाई के लिए कृत्रिम ग्लेशियर बनाए।", "गावांच्या सिंचनासाठी कृत्रिम हिमनद्या उभारणारे स्थापत्य अभियंता."), m=("Water, innovation", "जल, नवाचार", "पाणी, नवोन्मेष")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Ladakh's out-migration is mostly of students and young job-seekers moving to Jammu, Srinagar, Chandigarh, Delhi and beyond. In the other direction, seasonal workers from other States arrive each summer for construction and tourism, and the army has a large presence. Historically, Leh was a meeting point for Kashmiri, Tibetan, Central Asian and Punjabi traders.",
        "लद्दाख से बाहर जाने वाले मुख्यतः छात्र और नौकरी तलाशने वाले युवा हैं, जो जम्मू, श्रीनगर, चंडीगढ़, दिल्ली और आगे जाते हैं। दूसरी ओर, हर गर्मी में निर्माण और पर्यटन के लिए दूसरे राज्यों से मौसमी मज़दूर आते हैं, और सेना की बड़ी उपस्थिति है। ऐतिहासिक रूप से लेह कश्मीरी, तिब्बती, मध्य एशियाई और पंजाबी व्यापारियों का मिलन स्थल था।",
        "लडाखमधून बाहेर जाणारे प्रामुख्याने विद्यार्थी आणि नोकरी शोधणारे तरुण असून ते जम्मू, श्रीनगर, चंदीगड, दिल्ली व पुढे जातात. उलट दिशेने, दर उन्हाळ्यात बांधकाम व पर्यटनासाठी इतर राज्यांतून हंगामी कामगार येतात, आणि लष्कराची मोठी उपस्थिती आहे. ऐतिहासिकदृष्ट्या लेह हे काश्मिरी, तिबेटी, मध्य आशियाई आणि पंजाबी व्यापाऱ्यांचे भेटीचे ठिकाण होते."),
        conf="Editorial"),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "UT Administration of Ladakh", "केंद्र शासित प्रदेश लद्दाख प्रशासन", "केंद्रशासित प्रदेश लडाख प्रशासन", url="https://ladakh.gov.in", src="la-gov"),
        it3("leh", "District Leh", "ज़िला लेह", "लेह जिल्हा", url="https://leh.nic.in", src="la-gov"),
        it3("kargil", "District Kargil", "ज़िला कारगिल", "कारगिल जिल्हा", url="https://kargil.nic.in", src="kargil-nic"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes", "एसटीडी कोड", "एसटीडी कोड"), [col(L("Town", "नगर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Leh", "लेह", "लेह"), "01982"], [L("Kargil", "कारगिल", "कारगिल"), "01985"]], None, None, conf="Editorial", access=None,
          note=L("Editorial; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय; दूरसंचार विभाग की नंबरिंग योजना से जाँचा जाएगा।", "संपादकीय; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळले जाईल.")),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("lfpr", ("In PLFS 2025, 61% of Ladakh's women aged 15+ were in the labour force — about one and a half times the national rate.", "पीएलएफ़एस 2025 में लद्दाख की 15+ आयु की 61% महिलाएँ श्रम बल में थीं — राष्ट्रीय दर का लगभग डेढ़ गुना।", "पीएलएफएस 2025 नुसार लडाखमधील 15+ वयाच्या 61% स्त्रिया श्रमशक्तीत होत्या — राष्ट्रीय दराच्या सुमारे दीडपट."), MOSPI, "plfs"),
        triv("tsokar", ("Tso Kar became a Ramsar wetland in November 2020, joining Tsomoriri.", "त्सो कार नवंबर 2020 में रामसर आर्द्रभूमि बना और त्सोमोरीरी के साथ जुड़ गया।", "त्सो कार नोव्हेंबर 2020 मध्ये रामसर पाणथळ बनले आणि त्सोमोरिरीच्या पंक्तीत आले."), RAMSAR, "indian-wetlands"),
        triv("gi", ("All four of Ladakh's GIs were filed in 2020–21, after it became a Union Territory.", "लद्दाख के चारों जीआई 2020–21 में, केंद्र शासित प्रदेश बनने के बाद दाखिल हुए।", "लडाखची चारही जीआय 2020–21 मध्ये, केंद्रशासित प्रदेश झाल्यानंतर दाखल झाली."), GI_PDF, "gi-registry"),
        triv("ut", ("Ladakh became a Union Territory on 31 October 2019.", "लद्दाख 31 अक्टूबर 2019 को केंद्र शासित प्रदेश बना।", "लडाख 31 ऑक्टोबर 2019 रोजी केंद्रशासित प्रदेश झाला.")),
        triv("hockey", ("Many players in India's ice hockey teams come from Ladakh.", "भारत की आइस हॉकी टीमों के कई खिलाड़ी लद्दाख से आते हैं।", "भारताच्या आइस हॉकी संघांतील अनेक खेळाडू लडाखचे आहेत.")),
        triv("stupa", ("\"Ice stupas\" store winter water as towering cones of ice that melt in time for spring sowing.", "\"आइस स्तूप\" सर्दियों का पानी बर्फ़ के ऊँचे शंकुओं के रूप में जमा करते हैं, जो वसंत की बुआई के समय पिघलते हैं।", "\"आइस स्तूप\" हिवाळ्यातील पाणी बर्फाच्या उंच शंकूंच्या रूपात साठवतात, जे वसंतातील पेरणीच्या वेळी वितळतात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("la mod ok")
