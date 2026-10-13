import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-DL"
ESD = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/chapter_19_0.pdf"
ECI = "https://results.eci.gov.in/ResultAcGenFeb2025/"
mo = research("mospi_dl.json")
dl = read("regions/IN-DL.json")["metrics"]; ind = read("india.json")["metrics"]
NAME = L("Delhi", "दिल्ली", "दिल्ली")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Delhi is India's National Capital Territory: a Union Territory with its own elected Legislative Assembly and Council of Ministers, headed by a Chief Minister, alongside a Lieutenant Governor who represents the President. New Delhi, the seat of the Union Government, lies within it. The territory sits on the Yamuna between Haryana and Uttar Pradesh and is the core of a much larger National Capital Region.\n\nDelhi's special status comes from Article 239AA of the Constitution, added in 1991. The elected government handles most State subjects, while public order, police and land remain with the Union.",
        "दिल्ली भारत का राष्ट्रीय राजधानी क्षेत्र है: अपनी निर्वाचित विधानसभा और मुख्यमंत्री के नेतृत्व वाली मंत्रिपरिषद वाला केंद्र शासित प्रदेश, जहाँ राष्ट्रपति का प्रतिनिधित्व करने वाले उपराज्यपाल भी होते हैं। केंद्र सरकार का मुख्यालय नई दिल्ली इसी के भीतर है। यह क्षेत्र हरियाणा और उत्तर प्रदेश के बीच यमुना के किनारे बसा है और कहीं बड़े राष्ट्रीय राजधानी क्षेत्र (एनसीआर) का केंद्र है।\n\nदिल्ली का विशेष दर्जा संविधान के अनुच्छेद 239कक से आता है, जो 1991 में जोड़ा गया। निर्वाचित सरकार अधिकांश राज्य विषय सँभालती है, जबकि लोक व्यवस्था, पुलिस और भूमि केंद्र के पास रहते हैं।",
        "दिल्ली हा भारताचा राष्ट्रीय राजधानी प्रदेश आहे: स्वतःची निवडून आलेली विधानसभा आणि मुख्यमंत्र्यांच्या नेतृत्वाखालील मंत्रिमंडळ असलेला केंद्रशासित प्रदेश, जिथे राष्ट्रपतींचे प्रतिनिधी म्हणून नायब राज्यपालही असतात. केंद्र सरकारचे मुख्यालय असलेली नवी दिल्ली याच प्रदेशात आहे. हरियाणा आणि उत्तर प्रदेश यांच्यामध्ये यमुनेकाठी वसलेला हा प्रदेश त्याहून कितीतरी मोठ्या राष्ट्रीय राजधानी क्षेत्राचा (एनसीआर) गाभा आहे.\n\nदिल्लीचा विशेष दर्जा राज्यघटनेच्या 1991 मध्ये समाविष्ट झालेल्या अनुच्छेद 239कक मधून येतो. निवडून आलेले सरकार बहुतांश राज्य विषय हाताळते, तर सार्वजनिक सुव्यवस्था, पोलीस आणि जमीन हे विषय केंद्राकडे राहतात."),
        conf="Editorial"),
    prose("intro-unique", L(
        "Few cities hold as many capitals in one place. Delhi's ruins and monuments span the Tomar and Chauhan forts, the Delhi Sultanate's Qutb Minar and Tughlaqabad, Mughal Shahjahanabad with its Red Fort and Jama Masjid, and Lutyens' imperial New Delhi — three of them UNESCO World Heritage Sites. Today it is also India's most densely populated State or UT, a magnet for migrants from across the country, and a city of street food, Sufi music, markets and ministries.",
        "बहुत कम शहरों में एक ही जगह इतनी राजधानियाँ समाई हैं। दिल्ली के खंडहर और स्मारक तोमर और चौहान क़िलों, दिल्ली सल्तनत के क़ुतुब मीनार और तुग़लक़ाबाद, लाल क़िले व जामा मस्जिद वाले मुग़ल शाहजहानाबाद और लुटियंस की शाही नई दिल्ली तक फैले हैं — इनमें से तीन यूनेस्को विश्व धरोहर स्थल हैं। आज यह भारत का सबसे घनी आबादी वाला राज्य या केंद्र शासित प्रदेश भी है, देश भर से आने वाले प्रवासियों का केंद्र, और स्ट्रीट फ़ूड, सूफ़ी संगीत, बाज़ारों और मंत्रालयों का शहर।",
        "इतक्या राजधान्या एकाच ठिकाणी सामावलेली शहरे फार थोडी आहेत. दिल्लीतील अवशेष आणि स्मारके तोमर व चौहान किल्ल्यांपासून, दिल्ली सल्तनतीच्या कुतुबमिनार व तुघलकाबादपासून, लाल किल्ला व जामा मशीद असलेल्या मुघल शाहजहानाबादपर्यंत आणि लुटियन्सच्या साम्राज्यकालीन नव्या दिल्लीपर्यंत पसरली आहेत — त्यापैकी तीन युनेस्को जागतिक वारसा स्थळे आहेत. आज हा भारतातील सर्वाधिक दाट लोकवस्तीचा राज्य किंवा केंद्रशासित प्रदेश आहे, देशभरातील स्थलांतरितांचे आकर्षण केंद्र आहे, आणि स्ट्रीट फूड, सूफी संगीत, बाजारपेठा व मंत्रालयांचे शहर आहे."),
        title=L("What makes Delhi unique?", "दिल्ली को ख़ास क्या बनाता है?", "दिल्लीचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Status", "दर्जा", "दर्जा"), L("National Capital Territory — Union Territory with legislature (Article 239AA)", "राष्ट्रीय राजधानी क्षेत्र — विधानसभा वाला केंद्र शासित प्रदेश (अनुच्छेद 239कक)", "राष्ट्रीय राजधानी प्रदेश — विधिमंडळ असलेला केंद्रशासित प्रदेश (अनुच्छेद 239कक)")],
           [L("Districts / sub-divisions", "ज़िले / उप-मंडल", "जिल्हे / उपविभाग"), L("11 / 33 (Economic Survey of Delhi 2023-24)", "11 / 33 (दिल्ली आर्थिक सर्वेक्षण 2023-24)", "11 / 33 (दिल्ली आर्थिक पाहणी 2023-24)")],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Hindi; Punjabi and Urdu as second official languages", "हिंदी; पंजाबी और उर्दू द्वितीय राजभाषाएँ", "हिंदी; पंजाबी व उर्दू दुसऱ्या राजभाषा")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-DL / DL"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          "dl-planning", ESD, conf="Editorial",
          note=L("District count from the Economic Survey of Delhi 2023-24; district boundaries have been under revision, so confirm the current list. Other rows are editorial and will each be linked to a notification in review.",
                 "ज़िलों की संख्या दिल्ली आर्थिक सर्वेक्षण 2023-24 से; ज़िला सीमाओं में संशोधन होता रहा है, इसलिए वर्तमान सूची की पुष्टि करें। बाकी पंक्तियाँ संपादकीय हैं; समीक्षा में हर एक को अधिसूचना से जोड़ा जाएगा।",
                 "जिल्ह्यांची संख्या दिल्ली आर्थिक पाहणी 2023-24 मधून; जिल्ह्यांच्या सीमांत फेरबदल होत आले आहेत, त्यामुळे सध्याची यादी तपासा. इतर ओळी संपादकीय असून तपासणीदरम्यान प्रत्येकीला अधिसूचनेचा दुवा जोडला जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Delhi covers 1,483 km² on the Indo-Gangetic plain. Two features shape it. The Yamuna flows north to south along the eastern side, with a broad floodplain that floods in heavy monsoons. To the west and south runs the Delhi Ridge, the rocky northern tail of the Aravalli hills, now largely protected as forest. Between them the plain is almost entirely built up; only about 2.5% of residents were classed as rural in 2011.\n\nThe territory borders Haryana on three sides and Uttar Pradesh on the east, and its suburbs — Gurugram, Faridabad, Noida, Ghaziabad — form one continuous urban region across State lines.",
        "दिल्ली सिंधु-गंगा के मैदान में 1,483 किमी² में फैली है। दो विशेषताएँ इसकी बनावट तय करती हैं। यमुना पूर्वी हिस्से में उत्तर से दक्षिण बहती है, जिसका चौड़ा बाढ़ क्षेत्र भारी मानसून में डूब जाता है। पश्चिम और दक्षिण में दिल्ली रिज है — अरावली पहाड़ियों का पथरीला उत्तरी छोर — जो अब बड़े हिस्से में संरक्षित वन है। इनके बीच का मैदान लगभग पूरी तरह बसा हुआ है; 2011 में केवल लगभग 2.5% निवासी ग्रामीण माने गए।\n\nयह क्षेत्र तीन ओर से हरियाणा और पूर्व में उत्तर प्रदेश से घिरा है, और इसके उपनगर — गुरुग्राम, फ़रीदाबाद, नोएडा, ग़ाज़ियाबाद — राज्य सीमाओं के पार एक लगातार शहरी क्षेत्र बनाते हैं।",
        "दिल्ली सिंधू-गंगा मैदानात 1,483 किमी² क्षेत्रावर पसरली आहे. दोन वैशिष्ट्ये तिची रचना ठरवतात. यमुना पूर्व भागात उत्तरेकडून दक्षिणेकडे वाहते आणि तिचा रुंद पूरमैदान मुसळधार पावसाळ्यात पाण्याखाली जातो. पश्चिम व दक्षिणेला दिल्ली रिज आहे — अरवली डोंगररांगेचे खडकाळ उत्तरेकडील टोक — जे आता मोठ्या प्रमाणात संरक्षित वन आहे. या दोघांमधील मैदान जवळपास पूर्णपणे वस्तीने व्यापले आहे; 2011 मध्ये केवळ सुमारे 2.5% रहिवासी ग्रामीण गणले गेले.\n\nया प्रदेशाच्या तीन बाजूंना हरियाणा आणि पूर्वेला उत्तर प्रदेश आहे, आणि त्याची उपनगरे — गुरुग्राम, फरीदाबाद, नोएडा, गाझियाबाद — राज्यसीमांपलीकडे एक सलग नागरी प्रदेश बनवतात."),
        sources=["dl-planning"], conf="Official"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), dl["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("hr", "Haryana (north, west, south)", "हरियाणा (उत्तर, पश्चिम, दक्षिण)", "हरियाणा (उत्तर, पश्चिम, दक्षिण)"),
        it3("up", "Uttar Pradesh (east)", "उत्तर प्रदेश (पूर्व)", "उत्तर प्रदेश (पूर्व)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    gaps("g", [
        (L("Yamuna length within Delhi and floodplain area", "दिल्ली में यमुना की लंबाई और बाढ़ क्षेत्र", "दिल्लीतील यमुनेची लांबी व पूरमैदान क्षेत्र"), "dl-gov", "Irrigation & Flood Control Department."),
        (L("Ridge area (notified)", "रिज क्षेत्र (अधिसूचित)", "रिज क्षेत्र (अधिसूचित)"), "dl-gov", "Forest Department notification."),
        (L("Seismic zone (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Delhi has a climate of extremes. Summers from April to June are very hot and dry, with dust storms and heatwaves that can push temperatures above 45 °C. The monsoon, from about late June to September, brings most of the year's rain and humid heat. Winters from December to February are cool to cold, with foggy mornings that disrupt flights and trains.\n\nAir quality is a serious seasonal problem. From October to January, still winter air traps emissions from vehicles, industry, construction dust and biomass burning in the region, and the Air Quality Index regularly reaches \"very poor\" or \"severe\" levels, triggering the Graded Response Action Plan.",
        "दिल्ली की जलवायु चरम सीमाओं वाली है। अप्रैल से जून तक गर्मियाँ बहुत गर्म और सूखी होती हैं, धूल भरी आँधियाँ और लू तापमान को 45 °C से ऊपर ले जा सकती हैं। लगभग जून के अंत से सितंबर तक मानसून साल की अधिकांश वर्षा और उमस भरी गर्मी लाता है। दिसंबर से फ़रवरी तक सर्दियाँ ठंडी होती हैं, और सुबह का कोहरा उड़ानों और ट्रेनों को बाधित करता है।\n\nवायु गुणवत्ता गंभीर मौसमी समस्या है। अक्टूबर से जनवरी तक सर्दियों की ठहरी हवा वाहनों, उद्योगों, निर्माण की धूल और क्षेत्र में जलाए जाने वाले जैव-ईंधन के उत्सर्जन को रोक लेती है, और वायु गुणवत्ता सूचकांक अक्सर \"बहुत ख़राब\" या \"गंभीर\" स्तर तक पहुँचता है, जिससे ग्रेडेड रिस्पॉन्स एक्शन प्लान लागू होता है।",
        "दिल्लीचे हवामान टोकाचे आहे. एप्रिल ते जून उन्हाळा अतिशय उष्ण व कोरडा असतो; धुळीची वादळे आणि उष्णतेच्या लाटा तापमान 45 °C च्या पुढे नेऊ शकतात. साधारण जूनच्या अखेरीपासून सप्टेंबरपर्यंतचा पावसाळा वर्षभराचा बहुतांश पाऊस आणि दमट उकाडा घेऊन येतो. डिसेंबर ते फेब्रुवारी हिवाळा थंड असतो आणि सकाळचे दाट धुके विमाने व रेल्वेगाड्या विस्कळीत करते.\n\nहवेची गुणवत्ता ही गंभीर हंगामी समस्या आहे. ऑक्टोबर ते जानेवारी हिवाळ्यातील स्थिर हवा वाहने, उद्योग, बांधकामाची धूळ आणि परिसरात जाळल्या जाणाऱ्या जैवइंधनाचे उत्सर्जन अडकवून ठेवते, आणि हवा गुणवत्ता निर्देशांक वारंवार \"अतिशय वाईट\" किंवा \"गंभीर\" पातळी गाठतो; त्यामुळे श्रेणीबद्ध प्रतिसाद कृती आराखडा लागू होतो."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("New Delhi", "नई दिल्ली", "नवी दिल्ली"), "lat": 28.6139, "lon": 77.2090},
        {"name": L("Civil Lines (North Delhi)", "सिविल लाइंस (उत्तरी दिल्ली)", "सिव्हिल लाइन्स (उत्तर दिल्ली)"), "lat": 28.6814, "lon": 77.2226},
        {"name": L("Dwarka (South-West Delhi)", "द्वारका (दक्षिण-पश्चिमी दिल्ली)", "द्वारका (नैर्ऋत्य दिल्ली)"), "lat": 28.5921, "lon": 77.0460},
    ]},
    lst("best", [
        it3("feb", "February to March", "फ़रवरी से मार्च", "फेब्रुवारी ते मार्च", d=("Mild days and cleaner air; gardens in bloom.", "सुहावने दिन और अपेक्षाकृत साफ़ हवा; बाग़ों में बहार।", "आल्हाददायक दिवस आणि तुलनेने स्वच्छ हवा; बागा बहरलेल्या.")),
        it3("oct", "October to November", "अक्टूबर से नवंबर", "ऑक्टोबर ते नोव्हेंबर", d=("Pleasant temperatures and festivals, but check air-quality alerts.", "सुहावना तापमान और त्योहार, लेकिन वायु गुणवत्ता अलर्ट देखें।", "सुखद तापमान आणि सण, पण हवा गुणवत्तेचे इशारे तपासा.")),
        it3("winter", "December to January", "दिसंबर से जनवरी", "डिसेंबर ते जानेवारी", d=("Cold, foggy mornings; Republic Day events in January.", "ठंडी, कोहरे वाली सुबहें; जनवरी में गणतंत्र दिवस समारोह।", "थंड, धुक्याच्या सकाळी; जानेवारीत प्रजासत्ताक दिनाचे कार्यक्रम.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Monthly temperature and rainfall normals (Safdarjung)", "मासिक तापमान और वर्षा सामान्य (सफ़दरजंग)", "मासिक तापमान व पर्जन्य सरासरी (सफदरजंग)"), "imd", "IMD climatological normals."),
        (L("Annual AQI statistics", "वार्षिक एक्यूआई आँकड़े", "वार्षिक एक्यूआय आकडेवारी"), "moefcc", "CPCB daily AQI bulletins / CAQM annual report."),
        (L("Heat action plan", "ऊष्मा कार्य योजना", "उष्णता कृती आराखडा"), "ndma", "Delhi Disaster Management Authority."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Delhi wakes to joggers in Lodhi Garden, pigeons wheeling over Jama Masjid and the clatter of shutters going up in Chandni Chowk. By mid-morning the roads are a river of buses, autos, e-rickshaws and SUVs, and the metro carries the city underneath. Old Delhi is all lanes and noise — paratha shops, wholesale spice markets, cycle-rickshaws squeezing past each other. South Delhi is leafier and quieter, with markets of cafés and boutiques. Evenings bring qawwali at the Nizamuddin dargah on Thursdays, families around India Gate and Kartavya Path, and kebab smoke in the lanes near Jama Masjid. Winters are for sweaters, peanuts and book fairs; summers for nimbu-paani and early starts. Delhi is loud, impatient and generous, a city of arrivals where almost everyone's family came from somewhere else.",
        "दिल्ली की सुबह लोधी गार्डन में दौड़ते लोगों, जामा मस्जिद के ऊपर उड़ते कबूतरों और चाँदनी चौक में खुलते शटरों की खड़खड़ाहट से होती है। दोपहर से पहले सड़कें बसों, ऑटो, ई-रिक्शा और एसयूवी की नदी बन जाती हैं, और नीचे मेट्रो शहर को ढोती है। पुरानी दिल्ली गलियों और शोर से भरी है — परांठे की दुकानें, मसालों की थोक मंडियाँ, एक-दूसरे से सटकर निकलते साइकिल-रिक्शा। दक्षिणी दिल्ली ज़्यादा हरी-भरी और शांत है, जहाँ कैफ़े और बुटीक वाले बाज़ार हैं। शाम को गुरुवार के दिन निज़ामुद्दीन दरगाह पर क़व्वाली होती है, इंडिया गेट और कर्तव्य पथ पर परिवार जुटते हैं, और जामा मस्जिद के पास की गलियों में कबाब का धुआँ उठता है। सर्दियाँ स्वेटर, मूँगफली और पुस्तक मेलों की होती हैं; गर्मियाँ नींबू-पानी और जल्दी शुरू होने वाले दिनों की। दिल्ली शोरगुल वाली, बेसब्र और दरियादिल है — आने वालों का शहर, जहाँ लगभग हर किसी का परिवार कहीं और से आया है।",
        "दिल्लीची सकाळ लोधी गार्डनमध्ये धावणारे लोक, जामा मशिदीवर घिरट्या घालणारी कबुतरे आणि चांदनी चौकात उघडणाऱ्या शटरांच्या खडखडाटाने होते. दुपारपूर्वीच रस्ते बसगाड्या, रिक्षा, ई-रिक्षा आणि एसयूव्हींची नदी बनतात, आणि खालून मेट्रो शहराला वाहून नेते. जुनी दिल्ली म्हणजे गल्ल्या आणि गोंगाट — पराठ्यांची दुकाने, मसाल्यांच्या घाऊक बाजारपेठा, एकमेकांना घासत जाणाऱ्या सायकल-रिक्षा. दक्षिण दिल्ली अधिक हिरवीगार आणि शांत आहे, जिथे कॅफे आणि बुटिकांच्या बाजारपेठा आहेत. संध्याकाळी गुरुवारी निजामुद्दीन दर्ग्यावर कव्वाली होते, इंडिया गेट आणि कर्तव्य पथावर कुटुंबे जमतात, आणि जामा मशिदीजवळच्या गल्ल्यांत कबाबांचा धूर दरवळतो. हिवाळा म्हणजे स्वेटर, शेंगदाणे आणि पुस्तक मेळे; उन्हाळा म्हणजे लिंबूपाणी आणि लवकर सुरू होणारे दिवस. दिल्ली गोंगाटी, उतावीळ आणि दिलदार आहे — येणाऱ्यांचे शहर, जिथे जवळपास प्रत्येकाचे कुटुंब कुठून तरी आलेले असते."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
POP = [("1951", 17.44), ("1961", 26.59), ("1971", 40.66), ("1981", 62.20), ("1991", 94.21), ("2001", 138.51), ("2011", 167.88)]
module(R, "people", [
    prose("p1", L(
        "At the 2011 Census, Delhi had 1.68 crore residents, up 21.2% in a decade, and a density of 11,320 people per km² — the highest of any State or UT, against 382 for India. Its population has grown almost tenfold since 1951, driven largely by migration. It is overwhelmingly urban (97.5%). The sex ratio, 868 women per 1,000 men in 2011, is low but rose from 821 in 2001; literacy was 86.2% (men 90.9%, women 80.8%). The MoHFW Technical Group projects Delhi's population at about 2.25 crore in 2026.\n\nHindi is the main language, with Punjabi and Urdu recognised as second official languages; Delhi's population also speaks almost every language of India, from Bengali in Chittaranjan Park to Malayalam, Tamil and the languages of the North-East.",
        "2011 की जनगणना में दिल्ली की जनसंख्या 1.68 करोड़ थी, जो एक दशक में 21.2% बढ़ी, और घनत्व 11,320 व्यक्ति प्रति किमी² था — किसी भी राज्य या केंद्र शासित प्रदेश में सबसे अधिक, जबकि भारत का 382 है। 1951 से इसकी आबादी लगभग दस गुना हो चुकी है, जिसका मुख्य कारण प्रवास है। यह लगभग पूरी तरह शहरी (97.5%) है। 2011 में लिंगानुपात प्रति 1,000 पुरुषों पर 868 महिलाएँ था — कम, पर 2001 के 821 से अधिक; साक्षरता 86.2% (पुरुष 90.9%, महिलाएँ 80.8%) थी। स्वास्थ्य मंत्रालय के तकनीकी समूह के अनुमान के अनुसार 2026 में दिल्ली की आबादी लगभग 2.25 करोड़ है।\n\nहिंदी मुख्य भाषा है, और पंजाबी व उर्दू द्वितीय राजभाषाएँ हैं; दिल्ली में भारत की लगभग हर भाषा बोली जाती है — चितरंजन पार्क की बांग्ला से लेकर मलयालम, तमिल और पूर्वोत्तर की भाषाओं तक।",
        "2011 च्या जनगणनेनुसार दिल्लीची लोकसंख्या 1.68 कोटी होती, दशकभरात 21.2% वाढ, आणि घनता दर किमी² ला 11,320 — सर्व राज्ये व केंद्रशासित प्रदेशांत सर्वाधिक, तर भारताची 382. 1951 पासून लोकसंख्या जवळपास दहापट वाढली आहे, आणि त्याचे मुख्य कारण स्थलांतर आहे. प्रदेश जवळपास पूर्णपणे नागरी (97.5%) आहे. 2011 मध्ये लिंग गुणोत्तर दर 1,000 पुरुषांमागे 868 स्त्रिया होते — कमी, पण 2001 च्या 821 पेक्षा जास्त; साक्षरता 86.2% (पुरुष 90.9%, स्त्रिया 80.8%) होती. आरोग्य मंत्रालयाच्या तांत्रिक गटाच्या प्रक्षेपणानुसार 2026 मध्ये दिल्लीची लोकसंख्या सुमारे 2.25 कोटी आहे.\n\nहिंदी ही मुख्य भाषा असून पंजाबी व उर्दू दुसऱ्या राजभाषा आहेत; दिल्लीत भारतातील जवळपास प्रत्येक भाषा बोलली जाते — चित्तरंजन पार्कमधील बंगालीपासून मल्याळम, तमिळ आणि ईशान्येकडील भाषांपर्यंत."),
        sources=["dl-planning", "mohfw-projections"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), dl["population2011"], "count", national=ind["population2011"]),
        fact("proj", L("Population, 2026 (projected)", "जनसंख्या, 2026 (अनुमानित)", "लोकसंख्या, 2026 (प्रक्षेपित)"),
             dp(22540000, "persons", "2026", "calendar", "mohfw-projections", ESD, rev="projected", conf="Official estimate/projection",
                note="MoHFW Technical Group on Population Projections (July 2020): 22,540 thousand, as reproduced in the Economic Survey of Delhi 2023-24. A projection, not a count."), "count"),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), dl["density2011"], "number"),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), dl["sexRatio2011"], "ratio", "higher-is-better",
             previous=dp(821, "females per 1000 males", "2001", "census", "census", ESD), national=ind["sexRatio2011"]),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), dl["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(868, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), dl["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("litf", L("Female literacy", "महिला साक्षरता", "स्त्री साक्षरता"), dp(80.8, "%", "2011", "census", "census", ESD), "percent", "higher-is-better"),
        fact("urb", L("Urban population", "शहरी जनसंख्या", "नागरी लोकसंख्या"), dl["urbanisation2011"], "percent", national=ind["urbanisation2011"]),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    {"type": "series", "id": "pop-series", "title": L("Population at each Census, 1951–2011", "हर जनगणना में जनसंख्या, 1951–2011", "प्रत्येक जनगणनेतील लोकसंख्या, 1951–2011"),
     "kind": "number", "polarity": "neutral",
     "series": [{"id": "dl", "label": NAME, "points": [dp(v, "lakh persons", y, "census", "census", ESD,
                                                       note="Economic Survey of Delhi 2023-24, Statement 19.2; earlier censuses adjusted to the 2011 jurisdiction." if y == "2011" else None) for y, v in POP]}],
     "note": L("Values in lakh. Census years only; projections are shown separately above.", "आँकड़े लाख में। केवल जनगणना वर्ष; अनुमान ऊपर अलग दिखाए गए हैं।", "आकडे लाखांत. फक्त जनगणना वर्षे; प्रक्षेपण वर वेगळे दाखवले आहे.")},
    gaps("g", [
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("SC share (Delhi has no notified STs)", "अनुसूचित जाति का हिस्सा (दिल्ली में कोई अधिसूचित जनजाति नहीं)", "अनुसूचित जातींचा वाटा (दिल्लीत अधिसूचित जमाती नाहीत)"), "census", "Census 2011 PCA."),
        (L("Mother-tongue shares (Census C-16)", "मातृभाषावार हिस्सा (जनगणना C-16)", "मातृभाषानिहाय वाटा (जनगणना C-16)"), "census", "Census C-16."),
        (L("Migrant share of population", "जनसंख्या में प्रवासियों का हिस्सा", "लोकसंख्येतील स्थलांतरितांचा वाटा"), "census", "Census 2011 D-series."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Delhi's story is told in its many \"cities\". Legend links the area to Indraprastha of the Mahabharata. The Tomar Rajputs built Lal Kot in the 11th century, and the Chauhans extended it as Qila Rai Pithora. After 1192 Delhi became the seat of the Delhi Sultanate, whose dynasties — Mamluk, Khalji, Tughlaq, Sayyid and Lodi — raised the Qutb Minar, Siri, Tughlaqabad and Firozabad. Babur's victory at Panipat in 1526 began Mughal rule; Humayun's Tomb set a template for Mughal architecture, and Shah Jahan built Shahjahanabad, with the Red Fort and Jama Masjid, in the 1640s.\n\nAs Mughal power faded, Delhi passed to the Marathas and then, in 1803, to the British. It was a centre of the 1857 uprising, after which the last Mughal emperor was exiled. In 1911 the British announced the move of their capital from Calcutta, and Edwin Lutyens and Herbert Baker's New Delhi was inaugurated in 1931. At independence in 1947, the national flag was raised at the Red Fort. Delhi became a Union Territory in 1956 and gained its elected Assembly under the 69th Amendment of 1991, with the first Assembly elected in 1993.",
        "दिल्ली की कहानी इसके कई \"शहरों\" में कही जाती है। किंवदंती इस क्षेत्र को महाभारत के इंद्रप्रस्थ से जोड़ती है। 11वीं सदी में तोमर राजपूतों ने लाल कोट बनाया और चौहानों ने उसे क़िला राय पिथौरा के रूप में बढ़ाया। 1192 के बाद दिल्ली, दिल्ली सल्तनत की राजधानी बनी, जिसके राजवंशों — मामलुक, ख़िलजी, तुग़लक़, सैयद और लोदी — ने क़ुतुब मीनार, सीरी, तुग़लक़ाबाद और फ़िरोज़ाबाद बनाए। 1526 में पानीपत में बाबर की जीत से मुग़ल शासन शुरू हुआ; हुमायूँ के मक़बरे ने मुग़ल वास्तुकला का ढाँचा तय किया, और शाहजहाँ ने 1640 के दशक में लाल क़िले और जामा मस्जिद सहित शाहजहानाबाद बसाया।\n\nमुग़ल शक्ति कमज़ोर होने पर दिल्ली मराठों और फिर 1803 में अंग्रेज़ों के हाथ में गई। यह 1857 के विद्रोह का केंद्र रही, जिसके बाद अंतिम मुग़ल बादशाह को निर्वासित किया गया। 1911 में अंग्रेज़ों ने कलकत्ता से राजधानी हटाने की घोषणा की, और एडविन लुटियंस व हर्बर्ट बेकर की नई दिल्ली का 1931 में उद्घाटन हुआ। 1947 में स्वतंत्रता पर लाल क़िले पर राष्ट्रीय ध्वज फहराया गया। दिल्ली 1956 में केंद्र शासित प्रदेश बनी और 1991 के 69वें संशोधन से इसे निर्वाचित विधानसभा मिली; पहली विधानसभा 1993 में चुनी गई।",
        "दिल्लीची कहाणी तिच्या अनेक \"शहरांतून\" सांगितली जाते. आख्यायिका हा परिसर महाभारतातील इंद्रप्रस्थाशी जोडतात. अकराव्या शतकात तोमर राजपुतांनी लाल कोट बांधला आणि चौहानांनी त्याचा विस्तार किल्ला राय पिथौरा म्हणून केला. 1192 नंतर दिल्ली ही दिल्ली सल्तनतीची राजधानी झाली; मामलुक, खिलजी, तुघलक, सय्यद आणि लोदी घराण्यांनी कुतुबमिनार, सिरी, तुघलकाबाद आणि फिरोजाबाद उभारले. 1526 मध्ये पानिपत येथे बाबराच्या विजयाने मुघल सत्ता सुरू झाली; हुमायूनच्या कबरीने मुघल स्थापत्याचा आदर्श घालून दिला, आणि शाहजहानने 1640 च्या दशकात लाल किल्ला व जामा मशिदीसह शाहजहानाबाद वसवले.\n\nमुघल सत्ता क्षीण झाल्यावर दिल्ली मराठ्यांकडे आणि नंतर 1803 मध्ये ब्रिटिशांकडे गेली. 1857 च्या उठावाचे ते केंद्र होते, त्यानंतर शेवटच्या मुघल बादशहाला हद्दपार करण्यात आले. 1911 मध्ये ब्रिटिशांनी राजधानी कलकत्त्याहून हलवण्याची घोषणा केली, आणि एडविन लुटियन्स व हर्बर्ट बेकर यांच्या नव्या दिल्लीचे 1931 मध्ये उद्घाटन झाले. 1947 मध्ये स्वातंत्र्यदिनी लाल किल्ल्यावर राष्ट्रध्वज फडकला. दिल्ली 1956 मध्ये केंद्रशासित प्रदेश झाली आणि 1991 च्या 69 व्या घटनादुरुस्तीने तिला निवडून आलेली विधानसभा मिळाली; पहिली विधानसभा 1993 मध्ये निवडली गेली."),
        conf="Editorial"),
    timeline([
        ev("lalkot", 1060, L("11th century", "11वीं सदी", "अकरावे शतक"), L("Tomars build Lal Kot", "तोमरों ने लाल कोट बनाया", "तोमरांनी लाल कोट बांधला")),
        ev("sultanate", 1192, L("1192–1206", "1192–1206", "1192–1206"), L("Delhi becomes the seat of the Delhi Sultanate", "दिल्ली, दिल्ली सल्तनत की राजधानी बनी", "दिल्ली ही दिल्ली सल्तनतीची राजधानी")),
        ev("qutb", 1199, L("c. 1199", "लगभग 1199", "सुमारे 1199"), L("Qutb Minar begun", "क़ुतुब मीनार का निर्माण शुरू", "कुतुबमिनारचे बांधकाम सुरू")),
        ev("tughlaq", 1321, L("1320s", "1320 का दशक", "1320 चे दशक"), L("Tughlaqabad fort built", "तुग़लक़ाबाद क़िला बना", "तुघलकाबाद किल्ला बांधला")),
        ev("panipat", 1526, L("1526", "1526", "1526"), L("Babur's victory at Panipat; Mughal rule begins", "पानीपत में बाबर की जीत; मुग़ल शासन की शुरुआत", "पानिपत येथे बाबराचा विजय; मुघल सत्तेची सुरुवात")),
        ev("humayun", 1570, L("1570", "1570", "1570"), L("Humayun's Tomb completed", "हुमायूँ का मक़बरा पूरा", "हुमायूनची कबर पूर्ण")),
        ev("shahjahanabad", 1648, L("1639–48", "1639–48", "1639–48"), L("Shahjahanabad and the Red Fort built", "शाहजहानाबाद और लाल क़िला बने", "शाहजहानाबाद आणि लाल किल्ला उभारले")),
        ev("british", 1803, L("1803", "1803", "1803"), L("British take control after the Battle of Delhi", "दिल्ली की लड़ाई के बाद अंग्रेज़ों का नियंत्रण", "दिल्लीच्या लढाईनंतर ब्रिटिशांचा ताबा")),
        ev("1857", 1857, L("1857", "1857", "1857"), L("Uprising; Bahadur Shah Zafar exiled afterwards", "विद्रोह; बाद में बहादुर शाह ज़फ़र का निर्वासन", "उठाव; नंतर बहादूरशाह जफरची हद्दपारी")),
        ev("capital", 1911, L("1911", "1911", "1911"), L("Capital moved from Calcutta to Delhi", "राजधानी कलकत्ता से दिल्ली स्थानांतरित", "राजधानी कलकत्त्याहून दिल्लीला")),
        ev("newdelhi", 1931, L("1931", "1931", "1931"), L("New Delhi inaugurated", "नई दिल्ली का उद्घाटन", "नव्या दिल्लीचे उद्घाटन")),
        ev("ind", 1947, L("15 August 1947", "15 अगस्त 1947", "15 ऑगस्ट 1947"), L("Independence; flag raised at the Red Fort", "स्वतंत्रता; लाल क़िले पर ध्वजारोहण", "स्वातंत्र्य; लाल किल्ल्यावर ध्वजारोहण")),
        ev("ut", 1956, L("1956", "1956", "1956"), L("Delhi becomes a Union Territory", "दिल्ली केंद्र शासित प्रदेश बनी", "दिल्ली केंद्रशासित प्रदेश")),
        ev("nct", 1991, L("1991", "1991", "1991"), L("69th Amendment creates the National Capital Territory with a legislature", "69वें संशोधन से विधानसभा वाला राष्ट्रीय राजधानी क्षेत्र बना", "69 व्या घटनादुरुस्तीने विधिमंडळासह राष्ट्रीय राजधानी प्रदेश")),
        ev("metro", 2002, L("2002", "2002", "2002"), L("First Delhi Metro line opens", "दिल्ली मेट्रो की पहली लाइन शुरू", "दिल्ली मेट्रोची पहिली मार्गिका सुरू")),
        ev("namo", 2026, L("February 2026", "फ़रवरी 2026", "फेब्रुवारी 2026"), L("Full Delhi–Meerut Namo Bharat corridor opens", "पूरा दिल्ली–मेरठ नमो भारत कॉरिडोर शुरू", "संपूर्ण दिल्ली–मेरठ नमो भारत मार्गिका सुरू")),
    ]),
    lst("heritage", [
        it3("qutb", "Qutb Minar and its Monuments", "क़ुतुब मीनार और उसके स्मारक", "कुतुबमिनार व परिसरातील स्मारके", m=("UNESCO 1993", "यूनेस्को 1993", "युनेस्को 1993"), url=UNESCO, src="unesco-whc"),
        it3("humayun", "Humayun's Tomb", "हुमायूँ का मक़बरा", "हुमायूनची कबर", m=("UNESCO 1993", "यूनेस्को 1993", "युनेस्को 1993"), url=UNESCO, src="unesco-whc"),
        it3("redfort", "Red Fort Complex", "लाल क़िला परिसर", "लाल किल्ला परिसर", m=("UNESCO 2007", "यूनेस्को 2007", "युनेस्को 2007"), url=UNESCO, src="unesco-whc"),
    ], title=L("World Heritage Sites", "विश्व धरोहर स्थल", "जागतिक वारसा स्थळे"), src="unesco-whc", url=UNESCO, conf="Official", access=TODAY),
])

# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Delhi's culture is a layering of court, bazaar and migrant traditions. The Sufi music of the Nizamuddin and Mehrauli shrines, Urdu poetry and the mushaira, and the crafts of zardozi embroidery and attar perfumery come from its Mughal past. Partition brought a large Punjabi population in 1947, reshaping food, festivals and neighbourhoods. Today the city also hosts national institutions of the arts — the National School of Drama, Sangeet Natak Akademi, Lalit Kala Akademi and Sahitya Akademi — and a dense calendar of festivals, book fairs and concerts.\n\nThe food scene ranges from Old Delhi's kebabs, nihari and jalebis to Punjabi chole bhature, butter-rich tandoori dishes and the chaat of every market.",
        "दिल्ली की संस्कृति दरबार, बाज़ार और प्रवासियों की परंपराओं की परतों से बनी है। निज़ामुद्दीन और महरौली की दरगाहों का सूफ़ी संगीत, उर्दू शायरी और मुशायरा, और ज़रदोज़ी कढ़ाई व इत्र बनाने के हुनर इसके मुग़ल अतीत से आते हैं। 1947 के विभाजन के बाद बड़ी पंजाबी आबादी आई, जिसने खान-पान, त्योहारों और मोहल्लों को नया रूप दिया। आज शहर में कला के राष्ट्रीय संस्थान — राष्ट्रीय नाट्य विद्यालय, संगीत नाटक अकादमी, ललित कला अकादमी और साहित्य अकादमी — भी हैं, और उत्सवों, पुस्तक मेलों और संगीत समारोहों का भरा-पूरा कैलेंडर है।\n\nखाने में पुरानी दिल्ली के कबाब, निहारी और जलेबी से लेकर पंजाबी छोले भटूरे, मक्खन भरे तंदूरी व्यंजन और हर बाज़ार की चाट तक सब कुछ है।",
        "दिल्लीची संस्कृती दरबार, बाजार आणि स्थलांतरितांच्या परंपरांच्या थरांनी बनलेली आहे. निजामुद्दीन व मेहरौलीच्या दर्ग्यांचे सूफी संगीत, उर्दू शायरी आणि मुशायरा, तसेच जरदोजी भरतकाम आणि अत्तर बनवण्याची कला मुघल भूतकाळातून आली आहे. 1947 च्या फाळणीनंतर मोठी पंजाबी लोकसंख्या आली आणि तिने खाद्यसंस्कृती, सण आणि मोहल्ल्यांना नवे रूप दिले. आज शहरात कलांच्या राष्ट्रीय संस्था — राष्ट्रीय नाट्य विद्यालय, संगीत नाटक अकादमी, ललित कला अकादमी आणि साहित्य अकादमी — आहेत, आणि उत्सव, पुस्तक मेळे व मैफलींचे भरगच्च वेळापत्रक असते.\n\nखाद्यपदार्थांत जुन्या दिल्लीतील कबाब, निहारी आणि जिलेबीपासून पंजाबी छोले भटुरे, लोण्याने समृद्ध तंदूरी पदार्थ आणि प्रत्येक बाजारपेठेतील चाटपर्यंत सर्व काही आहे."),
        conf="Editorial"),
    lst("festivals", [
        fest("rday", "Republic Day parade", "गणतंत्र दिवस परेड", "प्रजासत्ताक दिन संचलन", ("26 January", "26 जनवरी", "26 जानेवारी"), ("National parade on Kartavya Path, followed by Beating Retreat at Vijay Chowk.", "कर्तव्य पथ पर राष्ट्रीय परेड, उसके बाद विजय चौक पर बीटिंग रिट्रीट।", "कर्तव्य पथावर राष्ट्रीय संचलन, त्यानंतर विजय चौकात बीटिंग रिट्रीट.")),
        fest("diwali", "Diwali", "दिवाली", "दिवाळी", ("October–November", "अक्टूबर–नवंबर", "ऑक्टोबर–नोव्हेंबर"), ("Markets in Chandni Chowk and across the city light up for weeks.", "चाँदनी चौक और पूरे शहर के बाज़ार हफ़्तों तक जगमगाते हैं।", "चांदनी चौक आणि शहरभरच्या बाजारपेठा आठवडाभर उजळून निघतात.")),
        fest("eid", "Eid", "ईद", "ईद", ("Lunar calendar", "चंद्र कैलेंडर", "चांद्र दिनदर्शिका"), ("Prayers at Jama Masjid and festive food in Old Delhi.", "जामा मस्जिद में नमाज़ और पुरानी दिल्ली में त्योहारी पकवान।", "जामा मशिदीत नमाज आणि जुन्या दिल्लीत सणाचे पदार्थ.")),
        fest("gurpurab", "Guru Nanak Gurpurab", "गुरु नानक गुरुपर्व", "गुरू नानक गुरुपुरब", ("October–November", "अक्टूबर–नवंबर", "ऑक्टोबर–नोव्हेंबर"), ("Processions and langar at Bangla Sahib and Sis Ganj gurdwaras.", "बंगला साहिब और शीशगंज गुरुद्वारों में नगर कीर्तन और लंगर।", "बंगला साहिब आणि शीशगंज गुरुद्वारांत नगरकीर्तन व लंगर.")),
        fest("puja", "Durga Puja", "दुर्गा पूजा", "दुर्गापूजा", ("September–October", "सितंबर–अक्टूबर", "सप्टेंबर–ऑक्टोबर"), ("Pandals in Chittaranjan Park and other Bengali neighbourhoods.", "चितरंजन पार्क और अन्य बंगाली इलाक़ों में पंडाल।", "चित्तरंजन पार्क व इतर बंगाली वस्त्यांमध्ये पंडाल.")),
        fest("phoolwalon", "Phool Walon Ki Sair", "फूल वालों की सैर", "फूलवालों की सैर", ("Autumn", "शरद ऋतु", "शरद ऋतू"), ("Mehrauli festival shared by a Sufi shrine and the Yogmaya temple.", "महरौली का उत्सव, जिसे एक सूफ़ी दरगाह और योगमाया मंदिर साथ मनाते हैं।", "सूफी दर्गा आणि योगमाया मंदिर मिळून साजरा करतात असा मेहरौलीचा उत्सव.")),
        fest("holi", "Holi", "होली", "होळी", ("March", "मार्च", "मार्च"), ("Colours and music across neighbourhoods.", "मोहल्लों में रंग और संगीत।", "वस्त्यावस्त्यांत रंग आणि संगीत.")),
    ], title=L("Festivals and events", "त्योहार और आयोजन", "सण व कार्यक्रम"), conf="Editorial"),
    lst("food", [
        it3("chaat", "Chaat", "चाट", "चाट", d=("Papdi chaat, golgappe and aloo tikki in every market.", "हर बाज़ार में पापड़ी चाट, गोलगप्पे और आलू टिक्की।", "प्रत्येक बाजारात पापडी चाट, गोलगप्पे आणि आलू टिक्की.")),
        it3("paratha", "Stuffed parathas", "भरवाँ परांठे", "भरलेले पराठे", d=("Fried in ghee in Old Delhi's Paranthe Wali Gali.", "पुरानी दिल्ली की परांठे वाली गली में घी में तले हुए।", "जुन्या दिल्लीच्या पराठेवाली गल्लीत तुपात तळलेले.")),
        it3("nihari", "Nihari and kebabs", "निहारी और कबाब", "निहारी आणि कबाब", d=("Slow-cooked breakfast stew and grilled meats near Jama Masjid.", "जामा मस्जिद के पास धीमी आँच पर पका नाश्ते का शोरबा और सिके कबाब।", "जामा मशिदीजवळ मंद आचेवर शिजवलेला न्याहारीचा रस्सा आणि भाजलेले कबाब.")),
        it3("chole", "Chole bhature", "छोले भटूरे", "छोले भटुरे", d=("Punjabi chickpea curry with fried bread.", "तली हुई रोटी के साथ पंजाबी छोले।", "तळलेल्या भटुऱ्यासोबत पंजाबी छोले.")),
        it3("sweets", "Jalebi, daulat ki chaat and kulfi", "जलेबी, दौलत की चाट और कुल्फ़ी", "जिलेबी, दौलत की चाट आणि कुल्फी", d=("Old Delhi sweets; daulat ki chaat is a winter-only milk froth.", "पुरानी दिल्ली की मिठाइयाँ; दौलत की चाट केवल सर्दियों में मिलने वाला दूध का झाग है।", "जुन्या दिल्लीतील मिठाया; दौलत की चाट हा केवळ हिवाळ्यात मिळणारा दुधाचा फेस.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("arts", [
        it3("qawwali", "Qawwali", "क़व्वाली", "कव्वाली"), it3("theatre", "Theatre (NSD, Mandi House)", "रंगमंच (एनएसडी, मंडी हाउस)", "रंगभूमी (एनएसडी, मंडी हाउस)"),
        it3("mushaira", "Mushaira (Urdu poetry)", "मुशायरा (उर्दू शायरी)", "मुशायरा (उर्दू शायरी)"), it3("zardozi", "Zardozi embroidery", "ज़रदोज़ी कढ़ाई", "जरदोजी भरतकाम"),
        it3("kathak", "Kathak", "कथक", "कथक"), it3("ramlila", "Ramlila", "रामलीला", "रामलीला"),
    ], layout="chips", title=L("Arts and crafts", "कला और शिल्प", "कला व हस्तकला"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
sect, (prim, sec, serv) = sector_table(mo["gsva2024_25_current_lakh"])
module(R, "economy", [
    prose("p1", L(
        f"Delhi's GSDP at current prices was about ₹{cur['FY2024-25'][0]/1e5:.2f} lakh crore in FY2024-25 (MoSPI), and its per capita NSDP of ₹{inr(pc['FY2024-25'][0])} is among the highest of any State or UT. It is almost entirely a services economy — services make up about {serv:.0f}% of GSVA — dominated by real estate and professional services, trade, finance, transport and communication, and public administration. Agriculture is negligible. The wider National Capital Region adds large manufacturing and IT clusters just across the borders, in Gurugram, Noida and Faridabad.\n\nThe labour market is distinctive: in PLFS 2025 only 13.1% of women aged 15+ were in the labour force, against 40.0% for India. The unemployment rate rose to 5.9% in 2025, from 2.2% in 2024.",
        f"मोस्पी के अनुसार वित्त वर्ष 2024-25 में दिल्ली का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2024-25'][0]/1e5:.2f} लाख करोड़ था, और इसका प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2024-25'][0])} किसी भी राज्य या केंद्र शासित प्रदेश में सबसे अधिक में से है। यह लगभग पूरी तरह सेवा अर्थव्यवस्था है — जीएसवीए में सेवाओं का हिस्सा लगभग {serv:.0f}% है — जिसमें रियल एस्टेट और पेशेवर सेवाएँ, व्यापार, वित्त, परिवहन व संचार, और लोक प्रशासन प्रमुख हैं। कृषि नगण्य है। बड़े राष्ट्रीय राजधानी क्षेत्र में सीमा के ठीक पार गुरुग्राम, नोएडा और फ़रीदाबाद में बड़े विनिर्माण और आईटी क्लस्टर हैं।\n\nश्रम बाज़ार की स्थिति अलग है: पीएलएफ़एस 2025 में 15+ आयु की केवल 13.1% महिलाएँ श्रम बल में थीं, जबकि भारत में 40.0%। बेरोज़गारी दर 2024 के 2.2% से बढ़कर 2025 में 5.9% हो गई।",
        f"मोस्पीनुसार आर्थिक वर्ष 2024-25 मध्ये दिल्लीचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2024-25'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2024-25'][0])} हे सर्व राज्ये व केंद्रशासित प्रदेशांतील सर्वाधिकांपैकी आहे. ही जवळपास पूर्णपणे सेवा अर्थव्यवस्था आहे — जीएसव्हीएमध्ये सेवांचा वाटा सुमारे {serv:.0f}% — ज्यात स्थावर मालमत्ता व व्यावसायिक सेवा, व्यापार, वित्त, वाहतूक व दळणवळण आणि लोकप्रशासन आघाडीवर आहेत. शेती नगण्य आहे. व्यापक राष्ट्रीय राजधानी क्षेत्रात सीमेपलीकडे गुरुग्राम, नोएडा आणि फरीदाबाद येथे मोठे उत्पादन व आयटी समूह आहेत.\n\nश्रमबाजाराचे चित्र वेगळे आहे: पीएलएफएस 2025 नुसार 15+ वयाच्या केवळ 13.1% स्त्रिया श्रमशक्तीत होत्या, तर भारतात 40.0%. बेरोजगारी दर 2024 मधील 2.2% वरून 2025 मध्ये 5.9% झाला."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_NAS), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_NAS), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_NAS), "rupee", "higher-is-better",
             previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("DL", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    plfs_series("DL", NAME),
    gaps("g", [
        (L("Delhi's own GSDP estimates (Directorate of Economics & Statistics)", "दिल्ली के अपने जीएसडीपी अनुमान (अर्थ एवं सांख्यिकी निदेशालय)", "दिल्लीचे स्वतःचे जीएसडीपी अंदाज (अर्थ व सांख्यिकी संचालनालय)"), "dl-planning", "Economic Survey of Delhi; may differ in vintage from MoSPI."),
        (L("Share of India's GDP", "भारत के जीडीपी में हिस्सा", "भारताच्या जीडीपीतील वाटा"), "mospi", "Needs the matching all-India GDP in the same base and vintage."),
        (L("FDI equity inflows (Delhi including parts of NCR)", "एफ़डीआई इक्विटी प्रवाह (दिल्ली व एनसीआर के कुछ भाग)", "एफडीआय समभाग गुंतवणूक (दिल्ली व एनसीआरचा काही भाग)"), "dpiit", "DPIIT reports Delhi with parts of UP and Haryana."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Delhi has a 70-member Legislative Assembly and a Council of Ministers led by the Chief Minister, under Article 239AA and the Government of National Capital Territory of Delhi Act, 1991. The Lieutenant Governor, appointed by the President, is the administrator. Public order, police and land are Union subjects in Delhi, and Parliament can legislate on any matter; the division of powers over services has been the subject of Supreme Court judgments and later legislation. Delhi elects 7 members to the Lok Sabha and 3 to the Rajya Sabha.\n\nLocal government is split between the Municipal Corporation of Delhi (reunified in 2022), the New Delhi Municipal Council and the Delhi Cantonment Board. In the February 2025 Assembly election, the BJP won 48 of 70 seats and Rekha Gupta became Chief Minister.",
        "अनुच्छेद 239कक और राष्ट्रीय राजधानी क्षेत्र दिल्ली शासन अधिनियम, 1991 के तहत दिल्ली में 70 सदस्यों की विधानसभा और मुख्यमंत्री के नेतृत्व वाली मंत्रिपरिषद है। राष्ट्रपति द्वारा नियुक्त उपराज्यपाल प्रशासक हैं। दिल्ली में लोक व्यवस्था, पुलिस और भूमि केंद्र के विषय हैं, और संसद किसी भी विषय पर क़ानून बना सकती है; सेवाओं पर अधिकारों का बँटवारा सर्वोच्च न्यायालय के निर्णयों और बाद के क़ानूनों का विषय रहा है। दिल्ली से लोकसभा के 7 और राज्यसभा के 3 सदस्य चुने जाते हैं।\n\nस्थानीय शासन दिल्ली नगर निगम (2022 में पुनः एकीकृत), नई दिल्ली नगरपालिका परिषद और दिल्ली छावनी बोर्ड में बँटा है। फ़रवरी 2025 के विधानसभा चुनाव में भाजपा ने 70 में से 48 सीटें जीतीं और रेखा गुप्ता मुख्यमंत्री बनीं।",
        "अनुच्छेद 239कक आणि राष्ट्रीय राजधानी प्रदेश दिल्ली शासन अधिनियम, 1991 नुसार दिल्लीत 70 सदस्यांची विधानसभा आणि मुख्यमंत्र्यांच्या नेतृत्वाखाली मंत्रिमंडळ आहे. राष्ट्रपतींनी नेमलेले नायब राज्यपाल हे प्रशासक आहेत. दिल्लीत सार्वजनिक सुव्यवस्था, पोलीस आणि जमीन हे केंद्राचे विषय आहेत, आणि संसद कोणत्याही विषयावर कायदा करू शकते; सेवांवरील अधिकारांचे वाटप सर्वोच्च न्यायालयाचे निकाल आणि नंतरच्या कायद्यांचा विषय राहिले आहे. दिल्लीतून लोकसभेवर 7 आणि राज्यसभेवर 3 सदस्य निवडले जातात.\n\nस्थानिक प्रशासन दिल्ली महानगरपालिका (2022 मध्ये पुन्हा एकत्रित), नवी दिल्ली नगरपालिका परिषद आणि दिल्ली छावणी मंडळ यांत विभागलेले आहे. फेब्रुवारी 2025 च्या विधानसभा निवडणुकीत भाजपने 70 पैकी 48 जागा जिंकल्या आणि रेखा गुप्ता मुख्यमंत्री झाल्या."),
        sources=["eci", "newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    table("results", L("Legislative Assembly election, February 2025 — seats won", "विधानसभा चुनाव, फ़रवरी 2025 — जीती गई सीटें", "विधानसभा निवडणूक, फेब्रुवारी 2025 — जिंकलेल्या जागा"),
          [col(L("Party", "दल", "पक्ष")), col(L("Seats", "सीटें", "जागा"), "right")],
          [["Bharatiya Janata Party (BJP)", 48], ["Aam Aadmi Party (AAAP)", 22], [L("Total", "कुल", "एकूण"), 70]],
          "eci", ECI, period="2025",
          note=L("Party names and abbreviations as listed by the Election Commission. No other party won a seat. Parties are shown in order of seats, without colours or commentary.",
                 "दलों के नाम और संक्षिप्त रूप चुनाव आयोग की सूची के अनुसार। किसी अन्य दल को सीट नहीं मिली। दलों को सीटों के क्रम में, बिना रंग या टिप्पणी के दिखाया गया है।",
                 "पक्षांची नावे व संक्षेप निवडणूक आयोगाच्या यादीनुसार. इतर कोणत्याही पक्षाला जागा मिळाली नाही. पक्ष जागांच्या क्रमाने, रंग किंवा भाष्याशिवाय दाखवले आहेत.")),
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("assembly", "Legislative Assembly of Delhi", "दिल्ली विधानसभा", "दिल्ली विधानसभा", url="https://delhiassembly.delhi.gov.in", src="dl-gov"),
        it3("lg", "Lok Niwas (Lieutenant Governor)", "लोक निवास (उपराज्यपाल)", "लोकनिवास (नायब राज्यपाल)", url="https://lg.delhi.gov.in", src="dl-lg"),
        it3("mcd", "Municipal Corporation of Delhi", "दिल्ली नगर निगम", "दिल्ली महानगरपालिका", url="https://mcdonline.nic.in", src="dl-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Official page for the Leader of Opposition", "नेता प्रतिपक्ष का आधिकारिक पेज", "विरोधी पक्षनेत्यांचे अधिकृत पान"), "dl-gov", "Legislative Assembly members' list."),
        (L("MCD wards and current Mayor", "एमसीडी वार्ड और वर्तमान महापौर", "एमसीडी प्रभाग व सध्याचे महापौर"), "dl-gov", "MCD website; Mayor's term is annual."),
        (L("Flagship welfare schemes", "प्रमुख कल्याण योजनाएँ", "प्रमुख कल्याणकारी योजना"), "dl-gov", "List with official scheme pages and current status."),
    ]),
])
print("dl mod1 ok")
