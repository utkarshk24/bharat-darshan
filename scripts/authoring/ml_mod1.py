"""Meghalaya modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-ML"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
ml = read("regions/IN-ML.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Meghalaya, 'the abode of clouds', is a hill State in north-eastern India, bordered by Assam to the north and east and by Bangladesh to the south and west. It covers the Shillong plateau — the Garo Hills in the west, the Khasi Hills in the centre and the Jaintia Hills in the east — and the steep southern escarpment that drops to the plains of Bangladesh. Shillong is the capital.\n\nCarved out of Assam, Meghalaya became an autonomous State in 1970 and a full State on 21 January 1972. Most of its people belong to the Khasi, Jaintia (Pnar) and Garo communities, which follow matrilineal traditions in which family names and property pass through women. It is known for its heavy rain, waterfalls, caves, living root bridges and music.",
        "मेघालय, 'बादलों का घर', उत्तर-पूर्वी भारत का एक पहाड़ी राज्य है, जिसकी सीमाएँ उत्तर और पूर्व में असम और दक्षिण और पश्चिम में बांग्लादेश से मिलती हैं। यह शिलांग पठार पर फैला है — पश्चिम में गारो पहाड़ियाँ, मध्य में खासी पहाड़ियाँ और पूर्व में जयंतिया पहाड़ियाँ — और उस खड़ी दक्षिणी ढलान पर जो बांग्लादेश के मैदानों तक उतरती है। शिलांग राजधानी है।\n\nअसम से अलग होकर मेघालय 1970 में स्वायत्त राज्य और 21 जनवरी 1972 को पूर्ण राज्य बना। इसके अधिकांश लोग खासी, जयंतिया (प्नार) और गारो समुदायों के हैं, जो मातृवंशीय परंपराओं का पालन करते हैं जिनमें कुल नाम और संपत्ति स्त्रियों के माध्यम से आगे बढ़ते हैं। यह अपनी भारी वर्षा, झरनों, गुफाओं, जीवित जड़ पुलों और संगीत के लिए जाना जाता है।",
        "मेघालय, 'ढगांचे निवासस्थान', हे ईशान्य भारतातील डोंगरी राज्य आहे, ज्याच्या उत्तर व पूर्वेला आसाम आणि दक्षिण व पश्चिमेला बांगलादेश आहे. ते शिलाँग पठारावर पसरलेले आहे — पश्चिमेला गारो टेकड्या, मध्यभागी खासी टेकड्या व पूर्वेला जयंतिया टेकड्या — आणि बांगलादेशच्या मैदानांपर्यंत उतरणाऱ्या तीव्र दक्षिणी कड्यावर. शिलाँग ही राजधानी आहे.\n\nआसाममधून वेगळे होऊन मेघालय 1970 मध्ये स्वायत्त राज्य व 21 जानेवारी 1972 रोजी पूर्ण राज्य झाले. तेथील बहुतेक लोक खासी, जयंतिया (प्नार) व गारो समुदायांचे आहेत, जे मातृवंशीय परंपरा पाळतात, ज्यांत कुळनाव व संपत्ती स्त्रियांमार्फत पुढे जाते. ते मुसळधार पाऊस, धबधबे, गुहा, जिवंत मुळांचे पूल व संगीतासाठी ओळखले जाते."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Moist winds from the Bay of Bengal strike the southern face of the plateau and drop enormous amounts of rain on Sohra (Cherrapunji) and Mawsynram. Khasi villages have trained the roots of rubber fig trees across streams to make living root bridges, which are on India's tentative list for UNESCO World Heritage. The limestone hills hide long cave systems, the Umngot river at Dawki is famous for its clear water, and Mawlynnong is known for its cleanliness. Shillong has a long tradition of rock, blues and choral music, and football is followed passionately.",
        "बंगाल की खाड़ी से आने वाली नम हवाएँ पठार के दक्षिणी मुख से टकराती हैं और सोहरा (चेरापूंजी) और मौसिनराम पर भारी मात्रा में वर्षा करती हैं। खासी गाँवों ने रबर अंजीर के पेड़ों की जड़ों को धाराओं के पार मोड़कर जीवित जड़ पुल बनाए हैं, जो यूनेस्को विश्व धरोहर के लिए भारत की अस्थायी सूची में हैं। चूना पत्थर की पहाड़ियों में लंबी गुफा प्रणालियाँ छिपी हैं, दावकी में उमंगोट नदी अपने साफ़ पानी के लिए प्रसिद्ध है, और मावलिननोंग अपनी स्वच्छता के लिए जाना जाता है। शिलांग में रॉक, ब्लूज़ और कोरल संगीत की लंबी परंपरा है, और फ़ुटबॉल के प्रति गहरा लगाव है।",
        "बंगालच्या उपसागरावरून येणारे दमट वारे पठाराच्या दक्षिण बाजूवर आदळतात आणि सोहरा (चेरापुंजी) व मौसिनरामवर प्रचंड पाऊस पाडतात. खासी गावांनी रबर अंजिराच्या झाडांची मुळे ओढ्यांपलीकडे वळवून जिवंत मुळांचे पूल बनवले आहेत, जे युनेस्को जागतिक वारशासाठी भारताच्या तात्पुरत्या यादीत आहेत. चुनखडीच्या टेकड्यांत लांब गुहा प्रणाली दडल्या आहेत, दावकी येथील उमंगोट नदी स्वच्छ पाण्यासाठी प्रसिद्ध आहे, आणि मावलिननोंग स्वच्छतेसाठी ओळखले जाते. शिलाँगमध्ये रॉक, ब्लूज व समूहगान संगीताची दीर्घ परंपरा आहे, आणि फुटबॉलची प्रचंड आवड आहे."),
        title=L("What makes Meghalaya unique?", "मेघालय को ख़ास क्या बनाता है?", "मेघालयाचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Statehood", "राज्य का दर्जा", "राज्याचा दर्जा"), L("21 January 1972 (autonomous State within Assam from 2 April 1970)", "21 जनवरी 1972 (2 अप्रैल 1970 से असम के भीतर स्वायत्त राज्य)", "21 जानेवारी 1972 (2 एप्रिल 1970 पासून आसाममधील स्वायत्त राज्य)")],
           [L("Districts", "ज़िले", "जिल्हे"), L("12 (five in the Garo Hills, five in the Khasi Hills including Ri-Bhoi, and two in the Jaintia Hills)", "12 (पाँच गारो पहाड़ियों में, री-भोई सहित पाँच खासी पहाड़ियों में, और दो जयंतिया पहाड़ियों में)", "12 (पाच गारो टेकड्यांत, री-भोईसह पाच खासी टेकड्यांत, आणि दोन जयंतिया टेकड्यांत)")],
           [L("Capital", "राजधानी", "राजधानी"), L("Shillong", "शिलांग", "शिलाँग")],
           [L("Languages", "भाषाएँ", "भाषा"), L("English is the official language; Khasi and Garo are associate official languages", "अंग्रेज़ी राजभाषा है; खासी और गारो सहायक राजभाषाएँ हैं", "इंग्रजी ही राजभाषा; खासी व गारो सहयोगी राजभाषा")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("High Court of Meghalaya, Shillong (since 2013)", "मेघालय उच्च न्यायालय, शिलांग (2013 से)", "मेघालय उच्च न्यायालय, शिलाँग (2013 पासून)")],
           [L("Autonomous District Councils", "स्वायत्त ज़िला परिषदें", "स्वायत्त जिल्हा परिषदा"), L("Khasi Hills, Jaintia Hills and Garo Hills (Sixth Schedule)", "खासी हिल्स, जयंतिया हिल्स और गारो हिल्स (छठी अनुसूची)", "खासी हिल्स, जयंतिया हिल्स व गारो हिल्स (सहावी अनुसूची)")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "ML"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; the newest district, Eastern West Khasi Hills, was created in 2021.", "संपादकीय; सबसे नया ज़िला, ईस्टर्न वेस्ट खासी हिल्स, 2021 में बना।", "संपादकीय; सर्वांत नवा जिल्हा, ईस्टर्न वेस्ट खासी हिल्स, 2021 मध्ये निर्माण झाला.")),
    gaps("g", [
        (L("District list — official notification", "ज़िलों की सूची — आधिकारिक अधिसूचना", "जिल्ह्यांची यादी — अधिकृत अधिसूचना"), "ml-gov", "Government of Meghalaya / Local Government Directory."),
        (L("Living root bridges — UNESCO tentative list entry", "जीवित जड़ पुल — यूनेस्को अस्थायी सूची प्रविष्टि", "जिवंत मुळांचे पूल — युनेस्को तात्पुरती यादी नोंद"), "unesco-whc", "UNESCO World Heritage Centre tentative lists (India)."),
    ]),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "The Shillong plateau is an ancient block of rock, uplifted and separated from the Indian peninsula by the Garo–Rajmahal gap. Its highest point is Shillong Peak, close to the capital. The north slopes gently to the Brahmaputra valley in Assam, while the south ends in a steep escarpment of deep gorges and waterfalls — Nohkalikai, Nohsngithiang (Seven Sisters) and Kynrem near Sohra — that fall towards the Surma plains of Bangladesh. Limestone, coal and uranium deposits lie in the southern hills, and rivers such as the Umiam, Umngot, Myntdu, Kynshi and Simsang (Someshwari) cut through the plateau.",
        "शिलांग पठार चट्टान का एक प्राचीन खंड है, जो ऊपर उठा और गारो–राजमहल अंतराल से भारतीय प्रायद्वीप से अलग हुआ। इसका सबसे ऊँचा बिंदु राजधानी के पास शिलांग पीक है। उत्तर धीरे-धीरे असम की ब्रह्मपुत्र घाटी की ओर ढलता है, जबकि दक्षिण गहरे खड्डों और झरनों की खड़ी ढलान में समाप्त होता है — सोहरा के पास नोहकलिकाई, नोहस्ङिथियांग (सेवन सिस्टर्स) और किनरेम — जो बांग्लादेश के सुरमा मैदानों की ओर गिरते हैं। दक्षिणी पहाड़ियों में चूना पत्थर, कोयला और यूरेनियम के भंडार हैं, और उमियम, उमंगोट, मिंतदू, किन्शी और सिमसांग (सोमेश्वरी) जैसी नदियाँ पठार को काटती हैं।",
        "शिलाँग पठार हा खडकाचा एक प्राचीन खंड आहे, जो उंचावला व गारो–राजमहाल खिंडीने भारतीय द्वीपकल्पापासून वेगळा झाला. त्याचे सर्वोच्च ठिकाण राजधानीजवळील शिलाँग पीक आहे. उत्तर भाग हळूहळू आसाममधील ब्रह्मपुत्रा खोऱ्याकडे उतरतो, तर दक्षिण भाग खोल दऱ्या व धबधब्यांच्या तीव्र कड्यात संपतो — सोहराजवळील नोहकलिकाई, नोहस्ङिथियांग (सेव्हन सिस्टर्स) व किनरेम — जे बांगलादेशच्या सुरमा मैदानांकडे कोसळतात. दक्षिणेकडील टेकड्यांत चुनखडी, कोळसा व युरेनियमचे साठे आहेत, आणि उमियम, उमंगोट, मिंतदू, किन्शी व सिमसांग (सोमेश्वरी) सारख्या नद्या पठार कापतात."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), ml["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("as", "Assam (north and east)", "असम (उत्तर और पूर्व)", "आसाम (उत्तर व पूर्व)"), it3("bd", "Bangladesh (south and west)", "बांग्लादेश (दक्षिण और पश्चिम)", "बांगलादेश (दक्षिण व पश्चिम)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("umiam", "Umiam", "उमियम", "उमियम", d=("Dammed to form Umiam lake (Barapani) north of Shillong.", "शिलांग के उत्तर में बाँध से उमियम झील (बड़ापानी) बनी।", "शिलाँगच्या उत्तरेला धरणाने उमियम सरोवर (बडापानी) तयार झाले.")),
        it3("umngot", "Umngot", "उमंगोट", "उमंगोट", d=("Clear river at Dawki on the Bangladesh border.", "बांग्लादेश सीमा पर दावकी में साफ़ पानी की नदी।", "बांगलादेश सीमेवरील दावकी येथील स्वच्छ पाण्याची नदी.")),
        it3("simsang", "Simsang (Someshwari)", "सिमसांग (सोमेश्वरी)", "सिमसांग (सोमेश्वरी)", d=("Main river of the Garo Hills.", "गारो पहाड़ियों की मुख्य नदी।", "गारो टेकड्यांतील मुख्य नदी.")),
        it3("myntdu", "Myntdu", "मिंतदू", "मिंतदू", d=("Flows past Jowai; used for hydropower.", "जोवाई के पास से बहती है; जलविद्युत के लिए उपयोग।", "जोवाईजवळून वाहते; जलविद्युतसाठी वापर.")),
        it3("kynshi", "Kynshi (Jadukata)", "किन्शी (जादुकाटा)", "किन्शी (जादुकाटा)", d=("Drains the West Khasi Hills.", "पश्चिमी खासी पहाड़ियों का जल बहाती है।", "पश्चिम खासी टेकड्यांचे पाणी वाहते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    lst("features", [
        it3("peak", "Shillong Peak", "शिलांग पीक", "शिलाँग पीक"), it3("nohkalikai", "Nohkalikai falls", "नोहकलिकाई जलप्रपात", "नोहकलिकाई धबधबा"),
        it3("caves", "Limestone caves of the Jaintia and Khasi Hills", "जयंतिया और खासी पहाड़ियों की चूना पत्थर गुफाएँ", "जयंतिया व खासी टेकड्यांतील चुनखडी गुहा"),
        it3("laitlum", "Laitlum canyons", "लाइटलुम घाटियाँ", "लाइटलुम दऱ्या"), it3("balpakram", "Balpakram plateau", "बालपाक्रम पठार", "बालपाक्रम पठार"),
    ], layout="chips", title=L("Landscapes", "भूदृश्य", "भूदृश्ये"), conf="Editorial"),
    gaps("g", [
        (L("Shillong Peak — official elevation", "शिलांग पीक — आधिकारिक ऊँचाई", "शिलाँग पीक — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Length of the Bangladesh border", "बांग्लादेश सीमा की लंबाई", "बांगलादेश सीमेची लांबी"), "india-gov", "Ministry of Home Affairs (Department of Border Management)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Meghalaya is cool for its latitude because of its height: Shillong, at about 1,500 m, has mild summers and chilly winters. The south-west monsoon from May to September is extremely wet on the southern escarpment, where Sohra and Mawsynram receive very heavy rainfall; the northern slopes and Ri-Bhoi are in a rain shadow and much drier. Winters, from November to February, are dry and clear, with fog in the valleys. The Garo Hills, lower and warmer, have a more tropical climate.",
        "ऊँचाई के कारण मेघालय अपने अक्षांश के हिसाब से ठंडा है: लगभग 1,500 मीटर पर शिलांग में गर्मियाँ सुहावनी और सर्दियाँ ठंडी होती हैं। मई से सितंबर तक दक्षिण-पश्चिम मानसून दक्षिणी ढलान पर अत्यधिक वर्षा लाता है, जहाँ सोहरा और मौसिनराम में बहुत भारी वर्षा होती है; उत्तरी ढलानें और री-भोई वृष्टि छाया में हैं और बहुत सूखे हैं। नवंबर से फ़रवरी तक सर्दियाँ सूखी और साफ़ होती हैं, घाटियों में कोहरे के साथ। नीची और गर्म गारो पहाड़ियों की जलवायु अधिक उष्णकटिबंधीय है।",
        "उंचीमुळे मेघालय त्याच्या अक्षांशाच्या मानाने थंड आहे: सुमारे 1,500 मीटरवरील शिलाँगमध्ये उन्हाळे सौम्य व हिवाळे गारठलेले असतात. मे ते सप्टेंबर नैर्ऋत्य मान्सून दक्षिणी कड्यावर अतिशय पाऊस आणतो, जिथे सोहरा व मौसिनरामला अतिशय मुसळधार पाऊस पडतो; उत्तरेकडील उतार व री-भोई पर्जन्यछायेत असून बरेच कोरडे आहेत. नोव्हेंबर ते फेब्रुवारी हिवाळा कोरडा व निरभ्र असतो, खोऱ्यांत धुक्यासह. कमी उंचीच्या व उबदार गारो टेकड्यांचे हवामान अधिक उष्णकटिबंधीय आहे."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Shillong", "शिलांग", "शिलाँग"), "lat": 25.5788, "lon": 91.8933},
        {"name": L("Sohra (Cherrapunji)", "सोहरा (चेरापूंजी)", "सोहरा (चेरापुंजी)"), "lat": 25.2702, "lon": 91.7323},
        {"name": L("Tura", "तुरा", "तुरा"), "lat": 25.5138, "lon": 90.2036},
        {"name": L("Jowai", "जोवाई", "जोवाई"), "lat": 25.4500, "lon": 92.2000},
    ]},
    lst("best", [
        it3("autumn", "October to November", "अक्टूबर से नवंबर", "ऑक्टोबर ते नोव्हेंबर", d=("Clear skies after the rains; Shad Nongkrem and Wangala festivals.", "वर्षा के बाद साफ़ आसमान; शाद नोंगक्रेम और वांगला उत्सव।", "पावसानंतर निरभ्र आकाश; शाद नोंगक्रेम व वांगला उत्सव.")),
        it3("spring", "March to May", "मार्च से मई", "मार्च ते मे", d=("Pleasant weather; Shad Suk Mynsiem in April.", "सुहावना मौसम; अप्रैल में शाद सुक मिनसिएम।", "सुखद हवामान; एप्रिलमध्ये शाद सुक मिनसिएम.")),
        it3("monsoon", "June to September", "जून से सितंबर", "जून ते सप्टेंबर", d=("Waterfalls at their fullest; expect heavy rain, slippery treks and road delays.", "झरने पूरे उफान पर; भारी वर्षा, फिसलन भरे ट्रेक और सड़क पर देरी की संभावना।", "धबधबे पूर्ण भरात; मुसळधार पाऊस, निसरडे ट्रेक व रस्त्यांवर उशीर अपेक्षित.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall at Sohra and Mawsynram", "सोहरा और मौसिनराम में सामान्य वार्षिक वर्षा", "सोहरा व मौसिनराम येथील सरासरी वार्षिक पाऊस"), "imd", "IMD climatological normals."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Shillong mixes hill-station calm with a lively youth culture: cafés and live music, church choirs, football on the Polo Grounds and the daily teer archery lottery. Police Bazaar is the busy centre, and Iewduh (Bara Bazar) is the large traditional market. Village life is organised around clans and the traditional institutions of chiefs (syiem, doloi, nokma) and councils, and community rules on forests, water and cleanliness are widely respected. Sunday is quiet in much of the State, as most people are Christian and go to church.",
        "शिलांग पहाड़ी नगर की शांति और जीवंत युवा संस्कृति का मेल है: कैफ़े और लाइव संगीत, चर्च गायक मंडलियाँ, पोलो ग्राउंड पर फ़ुटबॉल और रोज़ होने वाली तीर तीरंदाज़ी लॉटरी। पुलिस बाज़ार व्यस्त केंद्र है, और इवदुह (बड़ा बाज़ार) बड़ा पारंपरिक बाज़ार है। गाँव का जीवन कुलों और मुखियाओं (स्येम, दोलोई, नोकमा) और परिषदों की पारंपरिक संस्थाओं के इर्द-गिर्द चलता है, और वनों, पानी और स्वच्छता पर सामुदायिक नियमों का व्यापक सम्मान होता है। राज्य के अधिकांश भाग में रविवार शांत रहता है, क्योंकि अधिकांश लोग ईसाई हैं और चर्च जाते हैं।",
        "शिलाँगमध्ये डोंगरी शहराची शांतता व चैतन्यशील तरुण संस्कृती यांचा मेळ आहे: कॅफे व थेट संगीत, चर्चमधील गायकवृंद, पोलो ग्राउंडवर फुटबॉल आणि रोजची तीर धनुर्विद्या लॉटरी. पोलीस बाजार हे गजबजलेले केंद्र आहे, आणि इवदुह (बडा बाजार) हा मोठा पारंपरिक बाजार आहे. गावजीवन कुळे आणि प्रमुख (स्येम, दोलोई, नोकमा) व परिषदांच्या पारंपरिक संस्थांभोवती चालते, आणि जंगल, पाणी व स्वच्छतेबाबतचे सामुदायिक नियम मोठ्या प्रमाणावर पाळले जातात. राज्याच्या बहुतांश भागात रविवार शांत असतो, कारण बहुतेक लोक ख्रिस्ती आहेत व चर्चला जातात."),
        conf="Editorial"),
    gaps("g", [
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
    ]),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Meghalaya had 29.7 lakh people at the 2011 Census, about 132 per km². The sex ratio was 989 women per 1,000 men, up from 972 in 2001, and the child sex ratio 970. Literacy was 74.4%. Scheduled Tribes made up 86.1% of the population — mainly the Khasi, the Jaintia (Pnar, War and others, often counted with the Khasi) and the Garo, with smaller groups such as the Hajong, Koch, Rabha and Biate — and Scheduled Castes 0.6%.\n\nKhasi and Garo are the main languages, and English is the official language. Among the Khasi and Jaintia the youngest daughter (ka khadduh) traditionally inherits the ancestral home, and among the Garo a chosen daughter (nokna) inherits; children take their mother's clan name.",
        "2011 की जनगणना में मेघालय की जनसंख्या 29.7 लाख थी, प्रति वर्ग किमी लगभग 132। लिंगानुपात प्रति 1,000 पुरुषों पर 989 महिलाएँ था, जो 2001 के 972 से अधिक है, और शिशु लिंगानुपात 970 था। साक्षरता 74.4% थी। अनुसूचित जनजातियाँ जनसंख्या का 86.1% थीं — मुख्यतः खासी, जयंतिया (प्नार, वार और अन्य, जिन्हें अक्सर खासी के साथ गिना जाता है) और गारो, और हाजोंग, कोच, राभा और बियाते जैसे छोटे समूह — और अनुसूचित जातियाँ 0.6%।\n\nखासी और गारो मुख्य भाषाएँ हैं, और अंग्रेज़ी राजभाषा है। खासी और जयंतिया में परंपरागत रूप से सबसे छोटी बेटी (का खद्दुह) पैतृक घर की उत्तराधिकारी होती है, और गारो में एक चुनी हुई बेटी (नोकना); बच्चे माँ का कुल नाम लेते हैं।",
        "2011 च्या जनगणनेनुसार मेघालयाची लोकसंख्या 29.7 लाख होती, प्रति चौ.किमी सुमारे 132. दर 1,000 पुरुषांमागे 989 स्त्रिया होत्या, 2001 मधील 972 वरून वाढ, आणि बाल लिंग गुणोत्तर 970 होते. साक्षरता 74.4% होती. अनुसूचित जमाती लोकसंख्येच्या 86.1% होत्या — मुख्यतः खासी, जयंतिया (प्नार, वार व इतर, ज्यांची अनेकदा खासींसोबत गणना होते) व गारो, आणि हाजोंग, कोच, राभा व बियाते सारखे लहान गट — आणि अनुसूचित जाती 0.6%.\n\nखासी व गारो या मुख्य भाषा आहेत, आणि इंग्रजी राजभाषा आहे. खासी व जयंतियांमध्ये परंपरेने सर्वांत धाकटी मुलगी (का खद्दुह) वडिलोपार्जित घराची वारस असते, आणि गारोंमध्ये निवडलेली मुलगी (नोकना); मुले आईचे कुळनाव घेतात."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), ml["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), ml["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(972, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), ml["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(973, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), ml["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), ml["density2011"], "number"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(86.1, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 25.56 lakh people. Scheduled Castes were 0.6% (0.17 lakh)."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("kha", "Khasi", "खासी", "खासी", m=("Associate official language", "सहायक राजभाषा", "सहयोगी राजभाषा")),
        it3("garo", "Garo (A·chik)", "गारो (आ·चिक)", "गारो (आ·चिक)", m=("Associate official language", "सहायक राजभाषा", "सहयोगी राजभाषा")),
        it3("pnar", "Pnar (Jaintia)", "प्नार (जयंतिया)", "प्नार (जयंतिया)"), it3("war", "War", "वार", "वार"),
        it3("hajong", "Hajong", "हाजोंग", "हाजोंग"), it3("bn", "Bengali", "बांग्ला", "बंगाली"), it3("ne", "Nepali", "नेपाली", "नेपाळी"),
        it3("en", "English", "अंग्रेज़ी", "इंग्रजी", m=("Official language", "राजभाषा", "राजभाषा")),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Population by tribe — official figures", "जनजातिवार जनसंख्या — आधिकारिक आँकड़े", "जमातिनिहाय लोकसंख्या — अधिकृत आकडे"), "census", "Census 2011 ST-wise tables (A-11)."),
        (L("Meghalaya State Language Act — official text", "मेघालय राज्य भाषा अधिनियम — आधिकारिक पाठ", "मेघालय राज्य भाषा अधिनियम — अधिकृत मजकूर"), "ml-gov", "Meghalaya State Language Act, 2005."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Before British rule the Khasi Hills were divided among small states (hima) ruled by syiems chosen within royal clans, the Jaintia kingdom stretched from its hill capital at Nartiang to the plains of Sylhet, and Garo villages were governed by their nokmas. The great stone monoliths at Nartiang and across the Khasi and Jaintia Hills mark clan memorials. The British entered the hills after the Treaty of Yandabo (1826); U Tirot Sing, syiem of Nongkhlaw, led the Khasi resistance of 1829–33, the Jaintia kingdom was annexed in 1835, and U Kiang Nangbah was executed at Jowai in 1862 after a Jaintia uprising. In the Garo Hills, Pa Togan Nengminza Sangma fought British forces in 1872. Shillong became the capital of the Province of Assam in 1874 and grew into a hill station.\n\nAfter independence the hills were part of Assam, with Autonomous District Councils under the Sixth Schedule. A movement for a separate hill State, led by the All Party Hill Leaders' Conference under Captain Williamson A. Sangma, led to the Assam Reorganisation (Meghalaya) Act of 1969; Meghalaya became an autonomous State within Assam on 2 April 1970 and a full State on 21 January 1972, with Williamson Sangma as its first Chief Minister. Boundary differences with Assam remain in some areas, and a 2022 agreement settled six of twelve disputed sectors.",
        "ब्रिटिश शासन से पहले खासी पहाड़ियाँ छोटे राज्यों (हिमा) में बँटी थीं, जिन पर राजकुलों में से चुने गए स्येम शासन करते थे, जयंतिया राज्य अपनी पहाड़ी राजधानी नारतियांग से सिलहट के मैदानों तक फैला था, और गारो गाँवों का शासन उनके नोकमा करते थे। नारतियांग और पूरे खासी व जयंतिया पहाड़ियों में बड़े पत्थर के एकाश्म स्तंभ कुलों के स्मारक हैं। यांडाबू की संधि (1826) के बाद अंग्रेज़ पहाड़ियों में आए; नोंगख्लाव के स्येम उ तिरोत सिंह ने 1829–33 के खासी प्रतिरोध का नेतृत्व किया, 1835 में जयंतिया राज्य का विलय हुआ, और जयंतिया विद्रोह के बाद 1862 में जोवाई में उ कियांग नांगबाह को फाँसी दी गई। गारो पहाड़ियों में पा तोगन नेंगमिंजा संगमा 1872 में ब्रिटिश सेना से लड़े। 1874 में शिलांग असम प्रांत की राजधानी बना और एक पहाड़ी नगर के रूप में विकसित हुआ।\n\nस्वतंत्रता के बाद पहाड़ियाँ असम का भाग थीं, छठी अनुसूची के तहत स्वायत्त ज़िला परिषदों के साथ। कैप्टन विलियमसन ए. संगमा के नेतृत्व में ऑल पार्टी हिल लीडर्स कॉन्फ़्रेंस के अलग पहाड़ी राज्य के आंदोलन से 1969 का असम पुनर्गठन (मेघालय) अधिनियम बना; मेघालय 2 अप्रैल 1970 को असम के भीतर स्वायत्त राज्य और 21 जनवरी 1972 को पूर्ण राज्य बना, और विलियमसन संगमा इसके पहले मुख्यमंत्री बने। असम के साथ कुछ क्षेत्रों में सीमा मतभेद बने हुए हैं, और 2022 के एक समझौते से बारह विवादित क्षेत्रों में से छह का निपटारा हुआ।",
        "ब्रिटिश राजवटीपूर्वी खासी टेकड्या लहान राज्यांत (हिमा) विभागलेल्या होत्या, ज्यांवर राजकुळांतून निवडलेले स्येम राज्य करत, जयंतिया राज्य त्याच्या डोंगरी राजधानी नारतियांगपासून सिलहटच्या मैदानांपर्यंत पसरले होते, आणि गारो गावांचा कारभार त्यांचे नोकमा पाहत. नारतियांग व संपूर्ण खासी आणि जयंतिया टेकड्यांतील मोठे दगडी एकाश्म स्तंभ कुळांची स्मारके आहेत. यांडाबूच्या तहानंतर (1826) ब्रिटिश टेकड्यांत आले; नोंगख्लावचे स्येम उ तिरोत सिंह यांनी 1829–33 च्या खासी प्रतिकाराचे नेतृत्व केले, 1835 मध्ये जयंतिया राज्य खालसा झाले, आणि जयंतिया उठावानंतर 1862 मध्ये जोवाई येथे उ कियांग नांगबाह यांना फाशी देण्यात आली. गारो टेकड्यांत पा तोगन नेंगमिंजा संगमा 1872 मध्ये ब्रिटिश सैन्याशी लढले. 1874 मध्ये शिलाँग आसाम प्रांताची राजधानी झाली व डोंगरी शहर म्हणून विकसित झाली.\n\nस्वातंत्र्यानंतर टेकड्या आसामचा भाग होत्या, सहाव्या अनुसूचीतील स्वायत्त जिल्हा परिषदांसह. कॅप्टन विल्यमसन ए. संगमा यांच्या नेतृत्वाखालील ऑल पार्टी हिल लीडर्स कॉन्फरन्सच्या स्वतंत्र डोंगरी राज्याच्या चळवळीतून 1969 चा आसाम पुनर्रचना (मेघालय) अधिनियम आला; मेघालय 2 एप्रिल 1970 रोजी आसाममधील स्वायत्त राज्य व 21 जानेवारी 1972 रोजी पूर्ण राज्य झाले, आणि विल्यमसन संगमा त्याचे पहिले मुख्यमंत्री झाले. आसामशी काही भागांत सीमावाद कायम आहेत, आणि 2022 च्या करारामुळे बारा वादग्रस्त भागांपैकी सहांचा निपटारा झाला."),
        conf="Editorial"),
    timeline([
        ev("tirot", 1829, L("1829–1833", "1829–1833", "1829–1833"), L("Anglo-Khasi war led by U Tirot Sing", "उ तिरोत सिंह के नेतृत्व में आंग्ल-खासी युद्ध", "उ तिरोत सिंह यांच्या नेतृत्वाखाली आंग्ल-खासी युद्ध")),
        ev("jaintia", 1835, L("1835", "1835", "1835"), L("Jaintia kingdom annexed", "जयंतिया राज्य का विलय", "जयंतिया राज्य खालसा")),
        ev("kiang", 1862, L("1862", "1862", "1862"), L("U Kiang Nangbah executed at Jowai", "जोवाई में उ कियांग नांगबाह को फाँसी", "जोवाई येथे उ कियांग नांगबाह यांना फाशी")),
        ev("shillong", 1874, L("1874", "1874", "1874"), L("Shillong becomes capital of Assam province", "शिलांग असम प्रांत की राजधानी बना", "शिलाँग आसाम प्रांताची राजधानी")),
        ev("act", 1969, L("1969", "1969", "1969"), L("Assam Reorganisation (Meghalaya) Act", "असम पुनर्गठन (मेघालय) अधिनियम", "आसाम पुनर्रचना (मेघालय) अधिनियम")),
        ev("auto", 1970, L("2 April 1970", "2 अप्रैल 1970", "2 एप्रिल 1970"), L("Autonomous State within Assam", "असम के भीतर स्वायत्त राज्य", "आसाममधील स्वायत्त राज्य")),
        ev("state", 1972, L("21 January 1972", "21 जनवरी 1972", "21 जानेवारी 1972"), L("Meghalaya becomes a full State", "मेघालय पूर्ण राज्य बना", "मेघालय पूर्ण राज्य झाले")),
        ev("ngt", 2014, L("2014", "2014", "2014"), L("National Green Tribunal bans unregulated coal mining", "राष्ट्रीय हरित अधिकरण ने अनियमित कोयला खनन पर रोक लगाई", "राष्ट्रीय हरित लवादाची अनियंत्रित कोळसा खाणकामावर बंदी")),
        ev("border", 2022, L("29 March 2022", "29 मार्च 2022", "29 मार्च 2022"), L("Assam–Meghalaya agreement on six border sectors", "छह सीमा क्षेत्रों पर असम–मेघालय समझौता", "सहा सीमा भागांवर आसाम–मेघालय करार")),
    ]),
    lst("heritage", [
        it3("nartiang", "Nartiang monoliths", "नारतियांग एकाश्म", "नारतियांग एकाश्म स्तंभ", m=("Jaintia summer capital", "जयंतिया ग्रीष्म राजधानी", "जयंतियांची उन्हाळी राजधानी")),
        it3("rootbridges", "Living root bridges, Nongriat and elsewhere", "जीवित जड़ पुल, नोंग्रियात और अन्य स्थान", "जिवंत मुळांचे पूल, नोंग्रियात व इतरत्र", m=("Khasi and Jaintia villages", "खासी और जयंतिया गाँव", "खासी व जयंतिया गावे")),
        it3("tirot", "U Tirot Sing memorial, Mairang", "उ तिरोत सिंह स्मारक, मैरांग", "उ तिरोत सिंह स्मारक, मैरांग"),
        it3("cathedral", "Cathedral of Mary Help of Christians, Shillong", "मेरी हेल्प ऑफ़ क्रिश्चियन्स कैथेड्रल, शिलांग", "मेरी हेल्प ऑफ ख्रिश्चन्स कॅथेड्रल, शिलाँग"),
        it3("donbosco", "Don Bosco Museum of Indigenous Cultures, Shillong", "डॉन बॉस्को देशज संस्कृति संग्रहालय, शिलांग", "डॉन बॉस्को देशी संस्कृती संग्रहालय, शिलाँग"),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
    gaps("g", [
        (L("Assam–Meghalaya boundary agreement, 2022 — official text", "असम–मेघालय सीमा समझौता, 2022 — आधिकारिक पाठ", "आसाम–मेघालय सीमा करार, 2022 — अधिकृत मजकूर"), "india-gov", "Ministry of Home Affairs release of 29 March 2022."),
        (L("NGT coal-mining order — official text", "एनजीटी कोयला खनन आदेश — आधिकारिक पाठ", "एनजीटी कोळसा खाणकाम आदेश — अधिकृत मजकूर"), "india-gov", "National Green Tribunal order of April 2014 and later Supreme Court rulings."),
    ]),
])
print("ml mod1 ok")
