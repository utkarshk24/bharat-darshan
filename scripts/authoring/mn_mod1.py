"""Manipur modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-MN"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
mn = read("regions/IN-MN.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Manipur is a State in the far north-east of India, bordered by Nagaland to the north, Assam to the west, Mizoram to the south and Myanmar to the east. At its centre is the oval Imphal valley, about a tenth of the State's area but home to most of its people, ringed by forested hills where the rest of the population lives in hundreds of villages. Imphal is the capital.\n\nManipur was for centuries an independent kingdom ruled by Meitei kings from the Kangla fort in Imphal. It became part of India in 1949 and a full State on 21 January 1972. It is known for Loktak lake and its floating islands, the classical Manipuri dance, polo, handloom weaving and a strong sporting culture. Since May 2023 the State has been affected by ethnic violence, and it was under President's Rule from February 2025 to February 2026.",
        "मणिपुर भारत के सुदूर उत्तर-पूर्व का एक राज्य है, जिसकी सीमाएँ उत्तर में नागालैंड, पश्चिम में असम, दक्षिण में मिज़ोरम और पूर्व में म्यांमार से मिलती हैं। इसके केंद्र में अंडाकार इंफाल घाटी है, जो राज्य के क्षेत्रफल का लगभग दसवाँ भाग है पर अधिकांश लोग यहीं रहते हैं, और उसके चारों ओर वनाच्छादित पहाड़ियाँ हैं जहाँ बाकी जनसंख्या सैकड़ों गाँवों में बसती है। इंफाल राजधानी है।\n\nमणिपुर सदियों तक एक स्वतंत्र राज्य रहा, जिस पर मैतेई राजा इंफाल के कांगला क़िले से शासन करते थे। यह 1949 में भारत का भाग बना और 21 जनवरी 1972 को पूर्ण राज्य बना। यह लोकटक झील और उसके तैरते द्वीपों, शास्त्रीय मणिपुरी नृत्य, पोलो, हथकरघा बुनाई और मज़बूत खेल संस्कृति के लिए जाना जाता है। मई 2023 से राज्य जातीय हिंसा से प्रभावित है, और फ़रवरी 2025 से फ़रवरी 2026 तक यहाँ राष्ट्रपति शासन रहा।",
        "मणिपूर हे भारताच्या अतिपूर्व ईशान्येकडील राज्य आहे, ज्याच्या उत्तरेला नागालँड, पश्चिमेला आसाम, दक्षिणेला मिझोराम आणि पूर्वेला म्यानमार आहे. त्याच्या मध्यभागी अंडाकृती इंफाळ खोरे आहे, जे राज्याच्या क्षेत्रफळाचा सुमारे दहावा भाग असले तरी बहुतेक लोक येथे राहतात, आणि त्याभोवती वनाच्छादित डोंगर आहेत जिथे उरलेली लोकसंख्या शेकडो गावांत राहते. इंफाळ ही राजधानी आहे.\n\nमणिपूर शतकानुशतके स्वतंत्र राज्य होते, ज्यावर मैतेई राजे इंफाळमधील कांगला किल्ल्यातून राज्य करत. ते 1949 मध्ये भारताचा भाग झाले आणि 21 जानेवारी 1972 रोजी पूर्ण राज्य झाले. ते लोकटक सरोवर व त्यावरील तरंगती बेटे, शास्त्रीय मणिपुरी नृत्य, पोलो, हातमाग विणकाम व सशक्त क्रीडासंस्कृतीसाठी ओळखले जाते. मे 2023 पासून राज्य वांशिक हिंसाचाराने प्रभावित आहे, आणि फेब्रुवारी 2025 ते फेब्रुवारी 2026 या काळात तेथे राष्ट्रपती राजवट होती."),
        sources=["census", "fsi", "newsonair"], conf="Editorial"),
    prose("intro-unique", L(
        "Loktak lake, a Ramsar site, is covered with phumdis — floating mats of vegetation and soil — and on its south-eastern side is Keibul Lamjao, a floating national park and the last natural home of the sangai, the brow-antlered deer that is the State animal. Modern polo developed from sagol kangjei, the game British officers learned in Manipur in the 19th century, and the Mapal Kangjeibung in Imphal is a historic polo ground. Ima Keithel, the mothers' market in Imphal, is run entirely by women. Manipur has produced a long line of national and Olympic athletes, among them the boxer M. C. Mary Kom and the weightlifter Mirabai Chanu.",
        "रामसर स्थल लोकटक झील फुमदियों से ढकी है — वनस्पति और मिट्टी के तैरते गद्दे — और इसके दक्षिण-पूर्वी किनारे पर कैबुल लामजाओ है, एक तैरता राष्ट्रीय उद्यान और राज्य पशु, भौंह-सींग वाले हिरण संगाई का अंतिम प्राकृतिक आवास। आधुनिक पोलो सगोल कांगजेई से विकसित हुआ, वह खेल जो ब्रिटिश अधिकारियों ने 19वीं सदी में मणिपुर में सीखा, और इंफाल का मापाल कांगजेइबुंग एक ऐतिहासिक पोलो मैदान है। इंफाल का इमा कैथेल, माताओं का बाज़ार, पूरी तरह महिलाएँ चलाती हैं। मणिपुर ने राष्ट्रीय और ओलंपिक खिलाड़ियों की लंबी शृंखला दी है, जिनमें मुक्केबाज़ एम. सी. मैरी कॉम और भारोत्तोलक मीराबाई चानू शामिल हैं।",
        "रामसर स्थळ असलेले लोकटक सरोवर फुमदींनी झाकलेले आहे — वनस्पती व मातीचे तरंगते थर — आणि त्याच्या आग्नेय बाजूला कैबुल लामजाओ आहे, एक तरंगते राष्ट्रीय उद्यान व राज्यप्राणी, भुवई-शिंगी हरिण संगाईचे शेवटचे नैसर्गिक अधिवास. आधुनिक पोलो सगोल कांगजेईतून विकसित झाला, जो खेळ ब्रिटिश अधिकारी एकोणिसाव्या शतकात मणिपूरमध्ये शिकले, आणि इंफाळमधील मापाल कांगजेइबुंग हे ऐतिहासिक पोलो मैदान आहे. इंफाळमधील इमा कैथेल, मातांचा बाजार, संपूर्णपणे स्त्रिया चालवतात. मणिपूरने राष्ट्रीय व ऑलिंपिक खेळाडूंची दीर्घ परंपरा दिली आहे, ज्यात मुष्टियोद्धा एम. सी. मेरी कोम व भारोत्तोलक मीराबाई चानू यांचा समावेश आहे."),
        title=L("What makes Manipur unique?", "मणिपुर को ख़ास क्या बनाता है?", "मणिपूरचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Statehood", "राज्य का दर्जा", "राज्याचा दर्जा"), L("21 January 1972 (Statehood Day)", "21 जनवरी 1972 (राज्य स्थापना दिवस)", "21 जानेवारी 1972 (राज्य स्थापना दिन)")],
           [L("Districts", "ज़िले", "जिल्हे"), L("16 (seven of them — Jiribam, Kakching, Kamjong, Kangpokpi, Noney, Pherzawl and Tengnoupal — created in December 2016)", "16 (जिनमें से सात — जिरीबाम, काकचिंग, कामजोंग, कांगपोकपी, नोनी, फ़ेरज़ॉल और तेंगनौपाल — दिसंबर 2016 में बने)", "16 (त्यांपैकी सात — जिरीबाम, काकचिंग, कामजोंग, कांगपोकपी, नोनी, फेरझॉल व तेंगनौपाल — डिसेंबर 2016 मध्ये निर्माण झाले)")],
           [L("Capital", "राजधानी", "राजधानी"), L("Imphal", "इंफाल", "इंफाळ")],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Manipuri (Meiteilon), written in the Meitei Mayek and Bengali scripts; English is also used", "मणिपुरी (मैतेईलोन), मैतेई मयेक और बांग्ला लिपियों में; अंग्रेज़ी का भी प्रयोग", "मणिपुरी (मैतेईलोन), मैतेई मयेक व बांगला लिपींत; इंग्रजीचाही वापर")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("High Court of Manipur, Imphal (since 2013)", "मणिपुर उच्च न्यायालय, इंफाल (2013 से)", "मणिपूर उच्च न्यायालय, इंफाळ (2013 पासून)")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "MN"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; the seven districts created in December 2016 were carved out of older hill and valley districts.", "संपादकीय; दिसंबर 2016 में बने सात ज़िले पुराने पहाड़ी और घाटी ज़िलों से अलग किए गए।", "संपादकीय; डिसेंबर 2016 मध्ये निर्माण झालेले सात जिल्हे जुन्या डोंगरी व खोऱ्यातील जिल्ह्यांतून वेगळे केले गेले.")),
    gaps("g", [
        (L("District list and dates of creation — official notification", "ज़िलों की सूची और गठन की तिथियाँ — आधिकारिक अधिसूचना", "जिल्ह्यांची यादी व निर्मितीच्या तारखा — अधिकृत अधिसूचना"), "india-gov", "Government of Manipur Gazette / Local Government Directory."),
    ]),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Manipur is shaped like a bowl: the flat Imphal valley, at about 790 m, is surrounded by ranges of the Patkai–Naga–Lushai hills that rise to Mount Iso (Tenipu) on the Nagaland border. The valley is drained by the Imphal, Iril, Thoubal and Sekmai rivers, which flow south into Loktak and the wetlands around it and leave the State as the Manipur river towards Myanmar. In the west, the Barak river flows through the Jiribam plain into Assam. About nine-tenths of the State is hill country, much of it covered with bamboo and forest, and the region lies in a high earthquake zone.",
        "मणिपुर का आकार कटोरे जैसा है: लगभग 790 मीटर पर समतल इंफाल घाटी पटकाई–नागा–लुशाई पहाड़ियों की शृंखलाओं से घिरी है, जो नागालैंड सीमा पर माउंट ईसो (तेनिपु) तक उठती हैं। घाटी का जल इंफाल, इरिल, थौबाल और सेकमाई नदियाँ बहाती हैं, जो दक्षिण में लोकटक और उसके आसपास की आर्द्रभूमियों में बहती हैं और मणिपुर नदी के रूप में म्यांमार की ओर राज्य से बाहर जाती हैं। पश्चिम में बराक नदी जिरीबाम के मैदान से होकर असम जाती है। राज्य का लगभग नौ-दसवाँ भाग पहाड़ी है, जिसका बड़ा हिस्सा बाँस और वन से ढका है, और यह क्षेत्र उच्च भूकंप क्षेत्र में है।",
        "मणिपूरचा आकार वाटीसारखा आहे: सुमारे 790 मीटरवरील सपाट इंफाळ खोरे पटकाई–नागा–लुशाई डोंगरांच्या रांगांनी वेढलेले आहे, ज्या नागालँड सीमेवरील माउंट ईसो (तेनिपु) पर्यंत उंचावतात. खोऱ्याचे पाणी इंफाळ, इरिल, थौबाल व सेकमाई नद्या वाहतात, ज्या दक्षिणेला लोकटक व त्याभोवतीच्या पाणथळ प्रदेशात वाहतात आणि मणिपूर नदी म्हणून म्यानमारकडे राज्याबाहेर जातात. पश्चिमेला बराक नदी जिरीबामच्या मैदानातून आसाममध्ये जाते. राज्याचा सुमारे नऊ-दशांश भाग डोंगराळ आहे, ज्याचा बराचसा भाग बांबू व जंगलाने व्यापलेला आहे, आणि हा प्रदेश उच्च भूकंप क्षेत्रात आहे."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), mn["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("nl", "Nagaland (north)", "नागालैंड (उत्तर)", "नागालँड (उत्तर)"), it3("as", "Assam (west)", "असम (पश्चिम)", "आसाम (पश्चिम)"),
        it3("mz", "Mizoram (south-west)", "मिज़ोरम (दक्षिण-पश्चिम)", "मिझोराम (नैर्ऋत्य)"), it3("mm", "Myanmar (east and south)", "म्यांमार (पूर्व और दक्षिण)", "म्यानमार (पूर्व व दक्षिण)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("imphal", "Imphal river", "इंफाल नदी", "इंफाळ नदी", d=("Flows south through the valley and becomes the Manipur river.", "घाटी से दक्षिण की ओर बहती है और मणिपुर नदी बन जाती है।", "खोऱ्यातून दक्षिणेला वाहते व मणिपूर नदी बनते.")),
        it3("barak", "Barak", "बराक", "बराक", d=("Rises in the Senapati hills and flows west into Assam.", "सेनापति की पहाड़ियों से निकलती है और पश्चिम में असम जाती है।", "सेनापतीच्या डोंगरांत उगम पावते व पश्चिमेला आसाममध्ये जाते.")),
        it3("iril", "Iril", "इरिल", "इरिल", d=("Joins the Imphal river south of the capital.", "राजधानी के दक्षिण में इंफाल नदी से मिलती है।", "राजधानीच्या दक्षिणेला इंफाळ नदीला मिळते.")),
        it3("thoubal", "Thoubal", "थौबाल", "थौबाल", d=("Dammed at Maphou for irrigation and water supply.", "सिंचाई और जल आपूर्ति के लिए माफ़ौ में बाँधी गई।", "सिंचन व पाणीपुरवठ्यासाठी माफौ येथे धरण.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    lst("features", [
        it3("loktak", "Loktak lake", "लोकटक झील", "लोकटक सरोवर", m=("Ramsar site with phumdis", "फुमदियों वाला रामसर स्थल", "फुमदी असलेले रामसर स्थळ")),
        it3("iso", "Mount Iso (Tenipu)", "माउंट ईसो (तेनिपु)", "माउंट ईसो (तेनिपु)"), it3("shirui", "Shirui Kashung hills", "शिरुई काशुंग पहाड़ियाँ", "शिरुई काशुंग डोंगर"),
        it3("dzukou", "Dzükou valley (shared with Nagaland)", "ज़ुकू घाटी (नागालैंड के साथ)", "झुकू खोरे (नागालँडसोबत)"),
    ], layout="chips", title=L("Landscapes", "भूदृश्य", "भूदृश्ये"), conf="Editorial"),
    gaps("g", [
        (L("Highest point — official elevation", "सबसे ऊँचा बिंदु — आधिकारिक ऊँचाई", "सर्वोच्च बिंदू — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Length of the Myanmar border", "म्यांमार सीमा की लंबाई", "म्यानमार सीमेची लांबी"), "india-gov", "Ministry of Home Affairs (Department of Border Management)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "The Imphal valley has a mild climate, with warm, wet summers and cool, dry winters in which nights can be near freezing and mornings foggy. The south-west monsoon brings most of the rain from May to September, often with floods in the valley and landslides on the hill roads. The hills are cooler and wetter, and the high ridges of Ukhrul and Senapati can see frost in winter. October to March is the pleasant season for travel.",
        "इंफाल घाटी की जलवायु सौम्य है, जहाँ गर्मियाँ गर्म और नम और सर्दियाँ ठंडी और सूखी होती हैं, जिनमें रातें लगभग जमाव बिंदु तक और सुबहें कोहरे वाली हो सकती हैं। दक्षिण-पश्चिम मानसून मई से सितंबर तक अधिकांश वर्षा लाता है, अक्सर घाटी में बाढ़ और पहाड़ी सड़कों पर भूस्खलन के साथ। पहाड़ियाँ अधिक ठंडी और नम हैं, और उखरुल और सेनापति की ऊँची पहाड़ियों पर सर्दियों में पाला पड़ सकता है। अक्टूबर से मार्च यात्रा का सुहावना मौसम है।",
        "इंफाळ खोऱ्याचे हवामान सौम्य आहे, उबदार व दमट उन्हाळे आणि थंड व कोरडे हिवाळे, ज्यांत रात्री जवळपास गोठणबिंदूपर्यंत व सकाळी धुक्याच्या असू शकतात. नैर्ऋत्य मान्सून मे ते सप्टेंबरमध्ये बहुतांश पाऊस आणतो, अनेकदा खोऱ्यात पूर व डोंगरी रस्त्यांवर भूस्खलनासह. डोंगर अधिक थंड व ओलसर आहेत, आणि उखरुल व सेनापतीच्या उंच कड्यांवर हिवाळ्यात दव गोठू शकते. ऑक्टोबर ते मार्च हा प्रवासासाठी सुखद काळ आहे."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Imphal", "इंफाल", "इंफाळ"), "lat": 24.8170, "lon": 93.9368},
        {"name": L("Churachandpur", "चुराचांदपुर", "चुराचांदपूर"), "lat": 24.3333, "lon": 93.6833},
        {"name": L("Ukhrul", "उखरुल", "उखरुल"), "lat": 25.0960, "lon": 94.3600},
        {"name": L("Moirang", "मोइरांग", "मोइरांग"), "lat": 24.4990, "lon": 93.7720},
    ]},
    lst("best", [
        it3("autumn", "October to December", "अक्टूबर से दिसंबर", "ऑक्टोबर ते डिसेंबर", d=("Clear weather; Ningol Chakouba and the Sangai Festival in November.", "साफ़ मौसम; नवंबर में निंगोल चाकौबा और संगाई महोत्सव।", "निरभ्र हवामान; नोव्हेंबरमध्ये निंगोल चाकौबा व संगाई महोत्सव.")),
        it3("spring", "February to April", "फ़रवरी से अप्रैल", "फेब्रुवारी ते एप्रिल", d=("Yaoshang (Holi) and Cheiraoba (Meitei New Year).", "याओशांग (होली) और चेइराओबा (मैतेई नव वर्ष)।", "याओशांग (होळी) व चेइराओबा (मैतेई नववर्ष).")),
        it3("may", "May to June", "मई से जून", "मे ते जून", d=("Shirui lilies bloom in Ukhrul; the monsoon begins.", "उखरुल में शिरुई लिली खिलती है; मानसून शुरू होता है।", "उखरुलमध्ये शिरुई लिली फुलते; मान्सून सुरू होतो.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall", "सामान्य वार्षिक वर्षा", "सरासरी वार्षिक पाऊस"), "imd", "IMD Imphal meteorological centre."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Imphal's day starts early and ends early, and its centre is Ima Keithel, where thousands of women traders sell fish, vegetables, cloth and crafts. Sport is part of daily life — football on village grounds, boxing and weightlifting clubs, polo at Mapal Kangjeibung — and so are music and dance, from the devotional sankirtana to Lai Haraoba. Civil society is strong and vocal: women's groups such as the Meira Paibis, student bodies and village councils play a large public role. Life in recent years has been shaped by the conflict that began in 2023, with curfews, internet shutdowns and road blockades at times.",
        "इंफाल का दिन जल्दी शुरू होता है और जल्दी ख़त्म होता है, और उसका केंद्र इमा कैथेल है, जहाँ हज़ारों महिला व्यापारी मछली, सब्ज़ी, कपड़ा और शिल्प बेचती हैं। खेल दैनिक जीवन का हिस्सा है — गाँव के मैदानों पर फ़ुटबॉल, मुक्केबाज़ी और भारोत्तोलन क्लब, मापाल कांगजेइबुंग पर पोलो — और संगीत और नृत्य भी, भक्तिमय संकीर्तन से लाई हराओबा तक। नागरिक समाज मज़बूत और मुखर है: मीरा पाइबी जैसे महिला समूह, छात्र संगठन और ग्राम परिषदें बड़ी सार्वजनिक भूमिका निभाते हैं। हाल के वर्षों में जीवन 2023 में शुरू हुए संघर्ष से प्रभावित रहा है, कभी कर्फ़्यू, इंटरनेट बंदी और सड़क नाकेबंदी के साथ।",
        "इंफाळचा दिवस लवकर सुरू होतो व लवकर संपतो, आणि त्याचे केंद्र इमा कैथेल आहे, जिथे हजारो महिला व्यापारी मासे, भाज्या, कापड व हस्तकला विकतात. खेळ हा रोजच्या जीवनाचा भाग आहे — गावांच्या मैदानांवर फुटबॉल, मुष्टियुद्ध व भारोत्तोलन क्लब, मापाल कांगजेइबुंगवर पोलो — आणि संगीत व नृत्यही, भक्तिपर संकीर्तनापासून लाई हराओबापर्यंत. नागरी समाज सशक्त व बोलका आहे: मीरा पाइबीसारखे महिला गट, विद्यार्थी संघटना व ग्रामपरिषदा मोठी सार्वजनिक भूमिका बजावतात. अलीकडच्या वर्षांत जीवनावर 2023 मध्ये सुरू झालेल्या संघर्षाचा प्रभाव राहिला आहे, कधी संचारबंदी, इंटरनेट बंदी व रस्ते अडवणुकीसह."),
        conf="Editorial"),
    gaps("g", [
        (L("Internet shutdown orders — official record", "इंटरनेट बंदी आदेश — आधिकारिक अभिलेख", "इंटरनेट बंदी आदेश — अधिकृत नोंद"), "india-gov", "Government of Manipur Home Department orders."),
    ]),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Manipur had 25.7 lakh people at the 2011 Census, about 115 per km² — figures that exclude three sub-divisions of Senapati district where the results were not used. The sex ratio was 992 women per 1,000 men, but the child sex ratio fell from 957 in 2001 to 936. Literacy was 76.9%. Scheduled Tribes made up 35.1% of the counted population and Scheduled Castes 3.8%.\n\nThe Meitei, who live mainly in the valley and speak Manipuri (Meiteilon), are the largest community; Meitei Pangals (Manipuri Muslims) also live in the valley. The hills are home to many Naga tribes, such as the Tangkhul, Mao, Maram, Zeliangrong and Poumai, and to the Kuki-Zo tribes, such as the Thadou, Hmar, Paite, Vaiphei and Zou. Manipuri is in the Eighth Schedule of the Constitution, and dozens of tribal languages are spoken.",
        "2011 की जनगणना में मणिपुर की जनसंख्या 25.7 लाख थी, प्रति वर्ग किमी लगभग 115 — ये आँकड़े सेनापति ज़िले के उन तीन उपखंडों को छोड़कर हैं जहाँ परिणाम उपयोग नहीं किए गए। लिंगानुपात प्रति 1,000 पुरुषों पर 992 महिलाएँ था, पर शिशु लिंगानुपात 2001 के 957 से घटकर 936 हो गया। साक्षरता 76.9% थी। गिनी गई जनसंख्या में अनुसूचित जनजातियाँ 35.1% और अनुसूचित जातियाँ 3.8% थीं।\n\nमुख्यतः घाटी में रहने वाले और मणिपुरी (मैतेईलोन) बोलने वाले मैतेई सबसे बड़ा समुदाय हैं; मैतेई पांगल (मणिपुरी मुसलमान) भी घाटी में रहते हैं। पहाड़ियों में तांगखुल, माओ, मराम, ज़ेलियांगरोंग और पौमाई जैसी कई नागा जनजातियाँ और थाडू, ह्मार, पाइते, वाइफ़ेई और ज़ो जैसी कुकी-ज़ो जनजातियाँ रहती हैं। मणिपुरी संविधान की आठवीं अनुसूची में है, और दर्जनों जनजातीय भाषाएँ बोली जाती हैं।",
        "2011 च्या जनगणनेनुसार मणिपूरची लोकसंख्या 25.7 लाख होती, प्रति चौ.किमी सुमारे 115 — हे आकडे सेनापती जिल्ह्यातील त्या तीन उपविभागांना वगळून आहेत जिथले निकाल वापरले गेले नाहीत. दर 1,000 पुरुषांमागे 992 स्त्रिया होत्या, पण बाल लिंग गुणोत्तर 2001 मधील 957 वरून घटून 936 झाले. साक्षरता 76.9% होती. मोजलेल्या लोकसंख्येत अनुसूचित जमाती 35.1% व अनुसूचित जाती 3.8% होत्या.\n\nमुख्यतः खोऱ्यात राहणारे व मणिपुरी (मैतेईलोन) बोलणारे मैतेई हा सर्वांत मोठा समुदाय आहे; मैतेई पांगल (मणिपुरी मुस्लिम) देखील खोऱ्यात राहतात. डोंगरांत तांगखुल, माओ, मराम, झेलियांगरोंग व पौमाईसारख्या अनेक नागा जमाती आणि थाडू, ह्मार, पाइते, वाइफेई व झोसारख्या कुकी-झो जमाती राहतात. मणिपुरी संविधानाच्या आठव्या अनुसूचीत आहे, आणि डझनावारी आदिवासी भाषा बोलल्या जातात."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), mn["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), mn["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(978, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), mn["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(957, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), mn["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), mn["density2011"], "number"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(35.1, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 9.02 lakh people. Scheduled Castes were 3.8% (0.97 lakh). Excludes three sub-divisions of Senapati district."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("mni", "Manipuri (Meiteilon)", "मणिपुरी (मैतेईलोन)", "मणिपुरी (मैतेईलोन)", m=("Official; in the Eighth Schedule", "राजभाषा; आठवीं अनुसूची में", "राजभाषा; आठव्या अनुसूचीत")),
        it3("tangkhul", "Tangkhul", "तांगखुल", "तांगखुल"), it3("thadou", "Thadou", "थाडू", "थाडू"), it3("mao", "Mao", "माओ", "माओ"),
        it3("paite", "Paite", "पाइते", "पाइते"), it3("hmar", "Hmar", "ह्मार", "ह्मार"), it3("kabui", "Rongmei (Kabui)", "रोंगमेई (काबुई)", "रोंगमेई (काबुई)"),
        it3("en", "English", "अंग्रेज़ी", "इंग्रजी", m=("Used in administration and education", "प्रशासन और शिक्षा में प्रयोग", "प्रशासन व शिक्षणात वापर")),
    ], layout="chips", title=L("Languages (selected)", "भाषाएँ (चयनित)", "भाषा (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Population of the excluded Senapati sub-divisions", "छोड़े गए सेनापति उपखंडों की जनसंख्या", "वगळलेल्या सेनापती उपविभागांची लोकसंख्या"), "census", "Census 2011 Primary Census Abstract notes for Manipur."),
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Population by community — official figures", "समुदायवार जनसंख्या — आधिकारिक आँकड़े", "समुदायनिहाय लोकसंख्या — अधिकृत आकडे"), "census", "Census 2011 ST-wise tables (A-11)."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Manipur's royal chronicle, the Cheitharol Kumbaba, traces a line of Meitei kings back to Nongda Lairen Pakhangba, traditionally dated to 33 CE, ruling from Kangla in Imphal. Hinduism of the Gaudiya Vaishnava school became the court religion in the 18th century under kings such as Garib Niwaz and Bhagyachandra (Rajarshi Bhagyachandra), who is credited with the Ras Lila tradition of Manipuri dance. A Burmese invasion in 1819 began the 'Seven Years' Devastation'; with British help Gambhir Singh drove the Burmese out, and the Treaty of Yandabo (1826) confirmed Manipur's independence. After the Anglo-Manipur War of 1891 the kingdom became a princely state under British paramountcy. Women led the Nupi Lan ('women's war') protests of 1904 and 1939, and in 1944 the Battles of Imphal and Kohima stopped the Japanese advance into India.\n\nIn 1947 Manipur adopted a constitution and held elections; on 21 September 1949 Maharaja Bodhchandra signed the merger agreement, effective 15 October 1949. Manipur was administered by the Union, became a Union Territory in 1956 and a State on 21 January 1972. Insurgency and the Armed Forces (Special Powers) Act shaped later decades. Ethnic violence that began on 3 May 2023, mainly between Meitei and Kuki-Zo groups, led to many deaths, mass displacement and the separation of valley and hill areas; Chief Minister N. Biren Singh resigned in February 2025, President's Rule was imposed on 13 February 2025, and an elected government returned on 4 February 2026.",
        "मणिपुर का राजकीय इतिहास-ग्रंथ, चेइथारोल कुम्बाबा, मैतेई राजाओं की वंशावली को नोंगदा लाइरेन पाखंगबा तक ले जाता है, जिनका पारंपरिक काल 33 ई. माना जाता है और जो इंफाल के कांगला से शासन करते थे। 18वीं सदी में गरीब निवाज़ और भाग्यचंद्र (राजर्षि भाग्यचंद्र) जैसे राजाओं के समय गौड़ीय वैष्णव परंपरा का हिंदू धर्म दरबार का धर्म बना; भाग्यचंद्र को मणिपुरी नृत्य की रास लीला परंपरा का श्रेय दिया जाता है। 1819 में बर्मी आक्रमण से 'सात वर्षों का विनाश' शुरू हुआ; ब्रिटिश सहायता से गंभीर सिंह ने बर्मियों को खदेड़ा, और यांडाबू की संधि (1826) ने मणिपुर की स्वतंत्रता की पुष्टि की। 1891 के आंग्ल-मणिपुर युद्ध के बाद यह राज्य ब्रिटिश सर्वोच्चता के अधीन रियासत बन गया। 1904 और 1939 के नुपी लान ('महिलाओं का युद्ध') आंदोलनों का नेतृत्व महिलाओं ने किया, और 1944 में इंफाल और कोहिमा की लड़ाइयों ने भारत में जापानी बढ़त रोकी।\n\n1947 में मणिपुर ने संविधान अपनाया और चुनाव कराए; 21 सितंबर 1949 को महाराजा बोधचंद्र ने विलय समझौते पर हस्ताक्षर किए, जो 15 अक्टूबर 1949 से प्रभावी हुआ। मणिपुर का प्रशासन केंद्र ने चलाया, यह 1956 में केंद्र शासित प्रदेश और 21 जनवरी 1972 को राज्य बना। उग्रवाद और सशस्त्र बल (विशेष शक्तियाँ) अधिनियम ने बाद के दशकों को प्रभावित किया। 3 मई 2023 को शुरू हुई जातीय हिंसा, मुख्यतः मैतेई और कुकी-ज़ो समूहों के बीच, से अनेक मौतें हुईं, बड़े पैमाने पर विस्थापन हुआ और घाटी व पहाड़ी क्षेत्र अलग हो गए; मुख्यमंत्री एन. बीरेन सिंह ने फ़रवरी 2025 में इस्तीफ़ा दिया, 13 फ़रवरी 2025 को राष्ट्रपति शासन लगा, और 4 फ़रवरी 2026 को निर्वाचित सरकार लौटी।",
        "मणिपूरचा राजवंशीय इतिहासग्रंथ, चेइथारोल कुम्बाबा, मैतेई राजांची वंशावळ नोंगदा लाइरेन पाखंगबा यांच्यापर्यंत नेतो, ज्यांचा पारंपरिक काळ इ.स. 33 मानला जातो आणि जे इंफाळमधील कांगला येथून राज्य करत. अठराव्या शतकात गरीब निवाज व भाग्यचंद्र (राजर्षी भाग्यचंद्र) सारख्या राजांच्या काळात गौडीय वैष्णव परंपरेचा हिंदू धर्म दरबाराचा धर्म झाला; भाग्यचंद्रांना मणिपुरी नृत्याच्या रासलीला परंपरेचे श्रेय दिले जाते. 1819 मध्ये ब्रह्मी आक्रमणाने 'सात वर्षांचा विध्वंस' सुरू झाला; ब्रिटिश मदतीने गंभीर सिंह यांनी ब्रह्मींना हुसकावले, आणि यांडाबूच्या तहाने (1826) मणिपूरच्या स्वातंत्र्याला पुष्टी दिली. 1891 च्या आंग्ल-मणिपूर युद्धानंतर हे राज्य ब्रिटिश सार्वभौमत्वाखालील संस्थान झाले. 1904 व 1939 च्या नुपी लान ('स्त्रियांचे युद्ध') आंदोलनांचे नेतृत्व स्त्रियांनी केले, आणि 1944 मध्ये इंफाळ व कोहिमाच्या लढायांनी भारतातील जपानी आगेकूच थांबवली.\n\n1947 मध्ये मणिपूरने संविधान स्वीकारले व निवडणुका घेतल्या; 21 सप्टेंबर 1949 रोजी महाराजा बोधचंद्र यांनी विलीनीकरण करारावर स्वाक्षरी केली, जो 15 ऑक्टोबर 1949 पासून लागू झाला. मणिपूरचा कारभार केंद्राने चालवला, ते 1956 मध्ये केंद्रशासित प्रदेश व 21 जानेवारी 1972 रोजी राज्य झाले. बंडखोरी व सशस्त्र दल (विशेषाधिकार) अधिनियमाने पुढील दशकांवर प्रभाव टाकला. 3 मे 2023 रोजी सुरू झालेल्या वांशिक हिंसाचारात, मुख्यतः मैतेई व कुकी-झो गटांदरम्यान, अनेकांचा मृत्यू झाला, मोठ्या प्रमाणावर विस्थापन झाले आणि खोरे व डोंगरी भाग विभागले गेले; मुख्यमंत्री एन. बीरेन सिंह यांनी फेब्रुवारी 2025 मध्ये राजीनामा दिला, 13 फेब्रुवारी 2025 रोजी राष्ट्रपती राजवट लागू झाली, आणि 4 फेब्रुवारी 2026 रोजी निर्वाचित सरकार परतले."),
        sources=["newsonair", "hitavada"], conf="Editorial"),
    timeline([
        ev("seven", 1819, L("1819–1826", "1819–1826", "1819–1826"), L("Burmese occupation ('Seven Years' Devastation')", "बर्मी कब्ज़ा ('सात वर्षों का विनाश')", "ब्रह्मी ताबा ('सात वर्षांचा विध्वंस')")),
        ev("yandabo", 1826, L("1826", "1826", "1826"), L("Treaty of Yandabo", "यांडाबू की संधि", "यांडाबूचा तह")),
        ev("war1891", 1891, L("1891", "1891", "1891"), L("Anglo-Manipur War; princely state under the British", "आंग्ल-मणिपुर युद्ध; ब्रिटिश अधीन रियासत", "आंग्ल-मणिपूर युद्ध; ब्रिटिशांखालील संस्थान")),
        ev("nupilan", 1939, L("1904 and 1939", "1904 और 1939", "1904 व 1939"), L("Nupi Lan, the women's wars", "नुपी लान, महिलाओं के युद्ध", "नुपी लान, स्त्रियांची युद्धे")),
        ev("imphal44", 1944, L("1944", "1944", "1944"), L("Battle of Imphal", "इंफाल की लड़ाई", "इंफाळची लढाई")),
        ev("merger", 1949, L("15 October 1949", "15 अक्टूबर 1949", "15 ऑक्टोबर 1949"), L("Merger with India takes effect", "भारत में विलय प्रभावी", "भारतात विलीनीकरण लागू")),
        ev("ut", 1956, L("1956", "1956", "1956"), L("Union Territory", "केंद्र शासित प्रदेश", "केंद्रशासित प्रदेश")),
        ev("state", 1972, L("21 January 1972", "21 जनवरी 1972", "21 जानेवारी 1972"), L("Manipur becomes a State", "मणिपुर राज्य बना", "मणिपूर राज्य झाले")),
        ev("violence", 2023, L("3 May 2023", "3 मई 2023", "3 मे 2023"), L("Ethnic violence begins", "जातीय हिंसा शुरू", "वांशिक हिंसाचार सुरू")),
        ev("pr", 2025, L("13 February 2025", "13 फ़रवरी 2025", "13 फेब्रुवारी 2025"), L("President's Rule imposed", "राष्ट्रपति शासन लागू", "राष्ट्रपती राजवट लागू")),
        ev("govt", 2026, L("4 February 2026", "4 फ़रवरी 2026", "4 फेब्रुवारी 2026"), L("President's Rule revoked; new government sworn in", "राष्ट्रपति शासन हटा; नई सरकार ने शपथ ली", "राष्ट्रपती राजवट उठवली; नव्या सरकारचा शपथविधी")),
    ]),
    lst("heritage", [
        it3("kangla", "Kangla Fort", "कांगला क़िला", "कांगला किल्ला", m=("Seat of the Meitei kings, Imphal", "मैतेई राजाओं का आसन, इंफाल", "मैतेई राजांचे आसन, इंफाळ")),
        it3("govindaji", "Shri Govindajee temple", "श्री गोविंदजी मंदिर", "श्री गोविंदजी मंदिर", m=("Royal Vaishnava temple, Imphal", "राजकीय वैष्णव मंदिर, इंफाल", "राजवैष्णव मंदिर, इंफाळ")),
        it3("ina", "INA Memorial, Moirang", "आईएनए स्मारक, मोइरांग", "आयएनए स्मारक, मोइरांग", m=("Where the INA flag was raised in 1944", "जहाँ 1944 में आईएनए का झंडा फहराया गया", "जिथे 1944 मध्ये आयएनएचा ध्वज फडकवला गेला")),
        it3("war", "Imphal War Cemetery", "इंफाल युद्ध समाधि स्थल", "इंफाळ युद्धस्मशान", m=("Second World War", "द्वितीय विश्व युद्ध", "दुसरे महायुद्ध")),
        it3("khongjom", "Khongjom War Memorial", "खोंगजोम युद्ध स्मारक", "खोंगजोम युद्धस्मारक", m=("Anglo-Manipur War of 1891", "1891 का आंग्ल-मणिपुर युद्ध", "1891 चे आंग्ल-मणिपूर युद्ध")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
    gaps("g", [
        (L("Deaths and displacement since May 2023 — official figures", "मई 2023 से मौतें और विस्थापन — आधिकारिक आँकड़े", "मे 2023 पासून मृत्यू व विस्थापन — अधिकृत आकडे"), "india-gov", "Ministry of Home Affairs / Government of Manipur statements to Parliament."),
        (L("Proclamation and revocation of President's Rule — official text", "राष्ट्रपति शासन की उद्घोषणा और प्रतिसंहरण — आधिकारिक पाठ", "राष्ट्रपती राजवटीची घोषणा व मागे घेणे — अधिकृत मजकूर"), "india-gov", "Gazette of India notifications, Feb 2025 and Feb 2026."),
        (L("Merger Agreement, 1949 — official text", "विलय समझौता, 1949 — आधिकारिक पाठ", "विलीनीकरण करार, 1949 — अधिकृत मजकूर"), "india-gov", "National Archives of India."),
    ]),
])
print("mn mod1 ok")
