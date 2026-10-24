"""Himachal Pradesh modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-HP"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
hp = read("regions/IN-HP.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Himachal Pradesh — 'the land of snowy mountains' — lies in the western Himalaya, with Jammu and Kashmir and Ladakh to the north, Tibet (China) to the east, Uttarakhand to the south-east, Haryana to the south and Punjab to the west. Almost all of it is mountainous, rising from the Shivalik foothills at a few hundred metres to peaks above 6,000 m in Kinnaur and Lahaul and Spiti, and it is drained by the Sutlej, Beas, Ravi, Chenab and Yamuna. It had 68.6 lakh people at the 2011 Census, most of them in villages. Shimla is the capital and Dharamshala the second (winter) capital; Mandi, Solan, Kullu, Hamirpur and Una are other important towns.\n\nHimachal became a Union Territory in 1956, gained the hill areas of Punjab in 1966 and became India's 18th State on 25 January 1971. Hindi is the official language and Sanskrit the second official language.",
        "हिमाचल प्रदेश — 'हिम से ढके पर्वतों की भूमि' — पश्चिमी हिमालय में है; इसके उत्तर में जम्मू-कश्मीर और लद्दाख, पूर्व में तिब्बत (चीन), दक्षिण-पूर्व में उत्तराखंड, दक्षिण में हरियाणा और पश्चिम में पंजाब है। इसका लगभग पूरा भाग पहाड़ी है, जो कुछ सौ मीटर की शिवालिक तलहटी से किन्नौर और लाहौल-स्पीति में 6,000 मीटर से ऊँची चोटियों तक उठता है, और सतलुज, ब्यास, रावी, चिनाब और यमुना इसका जल बहाती हैं। 2011 की जनगणना में इसकी जनसंख्या 68.6 लाख थी, जिनमें अधिकांश गाँवों में रहते हैं। शिमला राजधानी है और धर्मशाला दूसरी (शीतकालीन) राजधानी; मंडी, सोलन, कुल्लू, हमीरपुर और ऊना अन्य महत्त्वपूर्ण नगर हैं।\n\nहिमाचल 1956 में केंद्र शासित प्रदेश बना, 1966 में पंजाब के पहाड़ी क्षेत्र इसमें जुड़े और 25 जनवरी 1971 को यह भारत का 18वाँ राज्य बना। हिंदी राजभाषा है और संस्कृत द्वितीय राजभाषा।",
        "हिमाचल प्रदेश — 'बर्फाच्छादित पर्वतांची भूमी' — पश्चिम हिमालयात आहे; त्याच्या उत्तरेला जम्मू-काश्मीर व लडाख, पूर्वेला तिबेट (चीन), आग्नेयेला उत्तराखंड, दक्षिणेला हरियाणा आणि पश्चिमेला पंजाब आहे. त्याचा जवळपास संपूर्ण भाग डोंगराळ आहे, जो काहीशे मीटरच्या शिवालिक पायथ्यापासून किन्नौर व लाहौल-स्पितीमधील 6,000 मीटरहून उंच शिखरांपर्यंत चढतो, आणि सतलज, बियास, रावी, चिनाब व यमुना त्यातील पाणी वाहून नेतात. 2011 च्या जनगणनेनुसार त्याची लोकसंख्या 68.6 लाख होती, ज्यांपैकी बहुतेक गावांत राहतात. शिमला ही राजधानी व धर्मशाला ही दुसरी (हिवाळी) राजधानी आहे; मंडी, सोलन, कुल्लू, हमीरपूर व ऊना ही इतर महत्त्वाची शहरे आहेत.\n\nहिमाचल 1956 मध्ये केंद्रशासित प्रदेश झाला, 1966 मध्ये पंजाबचे डोंगरी भाग त्यात जोडले गेले आणि 25 जानेवारी 1971 रोजी तो भारताचे 18 वे राज्य बनला. हिंदी ही राजभाषा व संस्कृत ही द्वितीय राजभाषा आहे."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Himachal is called Dev Bhoomi, 'the land of the gods': nearly every village has its own deity, carried in palanquins to gatherings such as the Kullu Dussehra and the Mandi Shivratri fair. Its apple orchards in Shimla, Kullu and Kinnaur, its hydro-electric dams on the Sutlej and Beas, and tourism to Shimla, Manali, Dharamshala and Spiti are the pillars of its economy. The State has some of India's best social indicators — high literacy, a high sex ratio and a large share of women in the workforce — despite its difficult terrain. McLeod Ganj above Dharamshala is the seat of the Dalai Lama and the Tibetan government-in-exile, and the Kalka–Shimla railway and the Great Himalayan National Park are UNESCO World Heritage sites.",
        "हिमाचल को देवभूमि कहा जाता है: लगभग हर गाँव के अपने देवता हैं, जिन्हें कुल्लू दशहरा और मंडी शिवरात्रि मेले जैसे समागमों में पालकियों में ले जाया जाता है। शिमला, कुल्लू और किन्नौर के सेब बाग़ान, सतलुज और ब्यास पर बने जलविद्युत बाँध, और शिमला, मनाली, धर्मशाला व स्पीति का पर्यटन इसकी अर्थव्यवस्था के स्तंभ हैं। कठिन भूभाग के बावजूद राज्य के सामाजिक संकेतक भारत में सबसे अच्छे में हैं — ऊँची साक्षरता, ऊँचा लिंगानुपात और श्रम बल में महिलाओं की बड़ी भागीदारी। धर्मशाला के ऊपर मैक्लोडगंज दलाई लामा और निर्वासित तिब्बती सरकार का केंद्र है, और कालका–शिमला रेलवे और ग्रेट हिमालयन राष्ट्रीय उद्यान यूनेस्को विश्व धरोहर स्थल हैं।",
        "हिमाचलला देवभूमी म्हणतात: जवळपास प्रत्येक गावाचे स्वतःचे दैवत आहे, ज्याला कुल्लू दसरा व मंडी शिवरात्री जत्रेसारख्या मेळाव्यांत पालखीतून नेले जाते. शिमला, कुल्लू व किन्नौरच्या सफरचंदबागा, सतलज व बियासवरील जलविद्युत धरणे आणि शिमला, मनाली, धर्मशाला व स्पितीचे पर्यटन हे त्याच्या अर्थव्यवस्थेचे आधारस्तंभ आहेत. कठीण भूप्रदेश असूनही राज्याचे सामाजिक निर्देशक भारतातील सर्वोत्तमांपैकी आहेत — उच्च साक्षरता, उच्च लिंग गुणोत्तर आणि श्रमशक्तीत स्त्रियांचा मोठा सहभाग. धर्मशालेच्या वर मॅक्लिओडगंज हे दलाई लामा व निर्वासित तिबेटी सरकारचे केंद्र आहे, आणि कालका–शिमला रेल्वे व ग्रेट हिमालयन राष्ट्रीय उद्यान ही युनेस्को जागतिक वारसा स्थळे आहेत."),
        title=L("What makes Himachal Pradesh unique?", "हिमाचल प्रदेश को ख़ास क्या बनाता है?", "हिमाचल प्रदेशचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Statehood", "राज्य का दर्जा", "राज्याचा दर्जा"), L("25 January 1971 (Statehood Day); Himachal Day 15 April (1948)", "25 जनवरी 1971 (पूर्ण राज्यत्व दिवस); हिमाचल दिवस 15 अप्रैल (1948)", "25 जानेवारी 1971 (राज्य स्थापना दिन); हिमाचल दिन 15 एप्रिल (1948)")],
           [L("Districts / divisions", "ज़िले / मंडल", "जिल्हे / विभाग"), "12 / 3"],
           [L("Capital", "राजधानी", "राजधानी"), L("Shimla; Dharamshala (second capital)", "शिमला; धर्मशाला (दूसरी राजधानी)", "शिमला; धर्मशाला (दुसरी राजधानी)")],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Hindi; Sanskrit (second official language)", "हिंदी; संस्कृत (द्वितीय राजभाषा)", "हिंदी; संस्कृत (द्वितीय राजभाषा)")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("High Court of Himachal Pradesh, Shimla", "हिमाचल प्रदेश उच्च न्यायालय, शिमला", "हिमाचल प्रदेश उच्च न्यायालय, शिमला")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "HP"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be linked to the State's notifications in review.", "संपादकीय; समीक्षा में राज्य की अधिसूचनाओं से जोड़ा जाएगा।", "संपादकीय; तपासणीत राज्याच्या अधिसूचनांशी जोडले जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Himachal climbs in steps from south-west to north-east. The low Shivalik hills of Una, Hamirpur, Bilaspur and Sirmaur give way to the middle Himalaya — the Dhauladhar range rising sharply behind Dharamshala and Palampur, and the ridges around Shimla — and then to the Great Himalaya and the Pir Panjal, crossed by passes such as Rohtang. Beyond them lie the cold deserts of Lahaul, Spiti and upper Kinnaur, in the rain shadow, which resemble Ladakh and Tibet. Broad valleys — Kangra, Kullu, Chamba, Kinnaur and Spiti — follow the rivers. The Sutlej enters from Tibet near Shipki La, the Beas rises near Rohtang, and the Chandra and Bhaga join in Lahaul to form the Chenab.",
        "हिमाचल दक्षिण-पश्चिम से उत्तर-पूर्व की ओर सीढ़ियों में ऊपर उठता है। ऊना, हमीरपुर, बिलासपुर और सिरमौर की नीची शिवालिक पहाड़ियों के बाद मध्य हिमालय आता है — धर्मशाला और पालमपुर के पीछे तेज़ी से उठती धौलाधार श्रेणी और शिमला के आसपास की पहाड़ियाँ — और फिर महान हिमालय और पीर पंजाल, जिन्हें रोहतांग जैसे दर्रे पार करते हैं। उनके पार वर्षा छाया में लाहौल, स्पीति और ऊपरी किन्नौर के शीत मरुस्थल हैं, जो लद्दाख और तिब्बत जैसे दिखते हैं। चौड़ी घाटियाँ — कांगड़ा, कुल्लू, चंबा, किन्नौर और स्पीति — नदियों के साथ चलती हैं। सतलुज शिपकी ला के पास तिब्बत से प्रवेश करती है, ब्यास रोहतांग के पास निकलती है, और चंद्रा व भागा लाहौल में मिलकर चिनाब बनाती हैं।",
        "हिमाचल नैर्ऋत्येकडून ईशान्येकडे पायऱ्यांनी चढत जातो. ऊना, हमीरपूर, बिलासपूर व सिरमौरच्या कमी उंचीच्या शिवालिक टेकड्यांनंतर मध्य हिमालय येतो — धर्मशाला व पालमपूरच्या मागे झपाट्याने उठणारी धौलाधार रांग आणि शिमल्याभोवतीच्या टेकड्या — आणि नंतर महान हिमालय व पीर पंजाल, ज्या रोहतांगसारख्या खिंडी ओलांडतात. त्यांच्या पलीकडे पर्जन्यछायेत लाहौल, स्पिती व वरच्या किन्नौरची शीत वाळवंटे आहेत, जी लडाख व तिबेटसारखी दिसतात. रुंद खोरी — कांगडा, कुल्लू, चंबा, किन्नौर व स्पिती — नद्यांच्या बाजूने जातात. सतलज शिपकी लाजवळ तिबेटमधून प्रवेश करते, बियास रोहतांगजवळ उगम पावते, आणि चंद्रा व भागा लाहौलमध्ये मिळून चिनाब बनवतात."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), hp["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("jk", "Jammu and Kashmir (north)", "जम्मू और कश्मीर (उत्तर)", "जम्मू व काश्मीर (उत्तर)"), it3("la", "Ladakh (north-east)", "लद्दाख (उत्तर-पूर्व)", "लडाख (ईशान्य)"),
        it3("cn", "Tibet, China (east)", "तिब्बत, चीन (पूर्व)", "तिबेट, चीन (पूर्व)"), it3("uk", "Uttarakhand (south-east)", "उत्तराखंड (दक्षिण-पूर्व)", "उत्तराखंड (आग्नेय)"),
        it3("hr", "Haryana (south)", "हरियाणा (दक्षिण)", "हरियाणा (दक्षिण)"), it3("pb", "Punjab (west and south-west)", "पंजाब (पश्चिम और दक्षिण-पश्चिम)", "पंजाब (पश्चिम व नैर्ऋत्य)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("sutlej", "Sutlej", "सतलुज", "सतलज", d=("Enters from Tibet at Shipki La; dammed at Nathpa Jhakri and Bhakra (Gobind Sagar).", "शिपकी ला से तिब्बत से प्रवेश; नाथपा झाकड़ी और भाखड़ा (गोबिंद सागर) पर बाँध।", "शिपकी लामार्गे तिबेटमधून प्रवेश; नाथपा झाकडी व भाक्रा (गोविंद सागर) येथे धरणे.")),
        it3("beas", "Beas", "ब्यास", "बियास", d=("Rises near Rohtang; flows through Kullu and Mandi to the Pong dam.", "रोहतांग के पास से निकलती है; कुल्लू और मंडी से पौंग बाँध तक बहती है।", "रोहतांगजवळ उगम; कुल्लू व मंडीमार्गे पोंग धरणापर्यंत वाहते.")),
        it3("ravi", "Ravi", "रावी", "रावी", d=("Drains the Chamba valley.", "चंबा घाटी का जल बहाती है।", "चंबा खोऱ्यातील पाणी वाहून नेते.")),
        it3("chenab", "Chenab (Chandra–Bhaga)", "चिनाब (चंद्रा–भागा)", "चिनाब (चंद्रा–भागा)", d=("Formed at Tandi in Lahaul; flows into Jammu and Kashmir.", "लाहौल के तांदी में बनती है; जम्मू-कश्मीर में बहती है।", "लाहौलमधील तांदी येथे तयार होते; जम्मू-काश्मीरमध्ये वाहते.")),
        it3("yamuna", "Yamuna", "यमुना", "यमुना", d=("Forms part of the border with Uttarakhand near Paonta Sahib.", "पांवटा साहिब के पास उत्तराखंड के साथ सीमा का हिस्सा।", "पांवटा साहिबजवळ उत्तराखंडसोबतच्या सीमेचा भाग.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest peak — official elevation", "सर्वोच्च शिखर — आधिकारिक ऊँचाई", "सर्वोच्च शिखर — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Glaciers and glacial lakes", "हिमनद और हिमनदी झीलें", "हिमनद्या व हिमनदी सरोवरे"), "india-gov", "HP State Centre on Climate Change / CWC glacial lake monitoring."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Climate changes with altitude. The Shivalik foothills and low valleys have hot summers and mild winters; the middle hills around Shimla, Dharamshala and Kullu have pleasant summers, a wet monsoon and cold winters with snow on the higher ridges; and Lahaul, Spiti and upper Kinnaur are cold deserts with little rain, very cold winters and passes closed by snow for months. Dharamshala, under the Dhauladhar, is among the wettest places in north-western India. Heavy monsoon rain brings landslides and flash floods, and western disturbances bring winter snow.",
        "जलवायु ऊँचाई के साथ बदलती है। शिवालिक तलहटी और निचली घाटियों में गर्मियाँ गर्म और सर्दियाँ हल्की होती हैं; शिमला, धर्मशाला और कुल्लू के आसपास की मध्य पहाड़ियों में सुहावनी गर्मियाँ, भीगा मानसून और ठंडी सर्दियाँ होती हैं, जब ऊँची पहाड़ियों पर बर्फ़ गिरती है; और लाहौल, स्पीति व ऊपरी किन्नौर कम वर्षा वाले शीत मरुस्थल हैं, जहाँ सर्दियाँ बहुत ठंडी होती हैं और दर्रे महीनों बर्फ़ से बंद रहते हैं। धौलाधार के नीचे बसा धर्मशाला उत्तर-पश्चिमी भारत के सबसे भीगे स्थानों में है। भारी मानसूनी वर्षा भूस्खलन और अचानक बाढ़ लाती है, और पश्चिमी विक्षोभ सर्दियों में बर्फ़ लाते हैं।",
        "हवामान उंचीनुसार बदलते. शिवालिक पायथा व खालच्या खोऱ्यांत उन्हाळा उष्ण व हिवाळा सौम्य असतो; शिमला, धर्मशाला व कुल्लूभोवतीच्या मधल्या टेकड्यांत आल्हाददायक उन्हाळा, ओला मान्सून व थंड हिवाळा असतो, जेव्हा उंच कड्यांवर बर्फ पडतो; आणि लाहौल, स्पिती व वरचे किन्नौर ही कमी पावसाची शीत वाळवंटे आहेत, जिथे हिवाळा अतिशय थंड असतो व खिंडी महिनोन्महिने बर्फाने बंद असतात. धौलाधारखाली वसलेले धर्मशाला हे वायव्य भारतातील सर्वाधिक पावसाच्या ठिकाणांपैकी एक आहे. मुसळधार मान्सून पावसामुळे भूस्खलन व आकस्मिक पूर येतात, आणि पश्चिमी विक्षोभ हिवाळ्यात बर्फ आणतात."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Shimla", "शिमला", "शिमला"), "lat": 31.1048, "lon": 77.1734},
        {"name": L("Dharamshala", "धर्मशाला", "धर्मशाला"), "lat": 32.2190, "lon": 76.3234},
        {"name": L("Manali", "मनाली", "मनाली"), "lat": 32.2432, "lon": 77.1892},
        {"name": L("Kaza (Spiti)", "काज़ा (स्पीति)", "काझा (स्पिती)"), "lat": 32.2276, "lon": 78.0710},
    ]},
    lst("best", [
        it3("summer", "March to June", "मार्च से जून", "मार्च ते जून", d=("Best for Shimla, Manali and Dharamshala; apple blossom in spring.", "शिमला, मनाली और धर्मशाला के लिए सबसे अच्छा; वसंत में सेब के फूल।", "शिमला, मनाली व धर्मशालेसाठी उत्तम; वसंतात सफरचंदाचा बहर.")),
        it3("autumn", "September to November", "सितंबर से नवंबर", "सप्टेंबर ते नोव्हेंबर", d=("Clear skies; Kullu Dussehra; apple harvest.", "साफ़ आसमान; कुल्लू दशहरा; सेब की तुड़ाई।", "निरभ्र आकाश; कुल्लू दसरा; सफरचंदाची तोडणी.")),
        it3("high", "June to September", "जून से सितंबर", "जून ते सप्टेंबर", d=("Lahaul and Spiti are open and dry while the monsoon soaks the lower hills.", "लाहौल और स्पीति खुले और सूखे रहते हैं, जबकि निचली पहाड़ियाँ मानसून में भीगती हैं।", "लाहौल व स्पिती खुले व कोरडे असतात, तर खालच्या टेकड्या मान्सूनमध्ये भिजतात.")),
        it3("winter", "December to February", "दिसंबर से फ़रवरी", "डिसेंबर ते फेब्रुवारी", d=("Snow and skiing at Solang, Narkanda and Kufri; check road closures.", "सोलंग, नारकंडा और कुफ़री में बर्फ़ और स्कीइंग; सड़कें बंद होने की जानकारी लें।", "सोलंग, नारकंडा व कुफरीत बर्फ व स्कीइंग; रस्ते बंद आहेत का ते तपासा.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall and snowfall", "सामान्य वार्षिक वर्षा और हिमपात", "सरासरी वार्षिक पाऊस व हिमवर्षाव"), "imd", "IMD Shimla meteorological centre."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Himachal is quiet, orderly and close to its gods. Slate-roofed houses of wood and stone cling to slopes above terraced fields and apple orchards; women in bright headscarves carry grass and firewood along narrow paths; and the village devta is consulted on everything from harvests to weddings. Shimla's Mall Road and the Ridge still have a colonial air, and toy trains climb from Kalka. Manali and Kasol fill with young travellers, Dharamshala's McLeod Ganj with monks, prayer flags and Tibetan momos, and in Spiti whitewashed monasteries stand above a moonscape. People are known for honesty and hospitality.",
        "हिमाचल शांत, व्यवस्थित और अपने देवताओं के निकट है। लकड़ी और पत्थर के स्लेट की छत वाले घर सीढ़ीदार खेतों और सेब बाग़ानों के ऊपर ढलानों से चिपके रहते हैं; चटक रंग के ढाठू पहनी महिलाएँ संकरे रास्तों पर घास और लकड़ी ढोती हैं; और फ़सल से लेकर शादी तक हर बात में गाँव के देवता से सलाह ली जाती है। शिमला के मॉल रोड और रिज पर अब भी औपनिवेशिक माहौल है, और कालका से टॉय ट्रेन ऊपर चढ़ती है। मनाली और कसोल युवा यात्रियों से, धर्मशाला का मैक्लोडगंज भिक्षुओं, प्रार्थना झंडों और तिब्बती मोमो से भरा रहता है, और स्पीति में सफ़ेदी किए मठ चंद्रमा जैसे भूदृश्य के ऊपर खड़े हैं। लोग ईमानदारी और मेहमाननवाज़ी के लिए जाने जाते हैं।",
        "हिमाचल शांत, शिस्तबद्ध व आपल्या दैवतांच्या जवळचा आहे. लाकूड व दगडाची, स्लेटच्या छपरांची घरे पायऱ्यांच्या शेतांवर व सफरचंदबागांवरील उतारांना चिकटून असतात; रंगीबेरंगी ढाठू बांधलेल्या स्त्रिया अरुंद वाटांवरून गवत व सरपण वाहतात; आणि सुगीपासून लग्नापर्यंत प्रत्येक गोष्टीत गावदेवतेचा सल्ला घेतला जातो. शिमल्याच्या मॉल रोड व रिजवर अजूनही वसाहतकालीन वातावरण आहे, आणि कालकाहून टॉय ट्रेन वर चढते. मनाली व कसोल तरुण प्रवाशांनी, धर्मशालेचे मॅक्लिओडगंज भिक्खू, प्रार्थना ध्वज व तिबेटी मोमोने भरलेले असते, आणि स्पितीत चुना लावलेले मठ चंद्रासारख्या भूदृश्यावर उभे आहेत. लोक प्रामाणिकपणा व पाहुणचारासाठी ओळखले जातात."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Himachal Pradesh had 68.6 lakh people at the 2011 Census and, with 123 people per km², is one of the less densely populated States. Its sex ratio was 972 women per 1,000 men and its child sex ratio 909, both up from 2001, and literacy was 82.8%, well above the national 73.0%. Scheduled Castes made up 25.2% of the population — among the highest shares in India — and Scheduled Tribes 5.7%, mostly the Kinnauras, Lahaulas, Gaddis, Gujjars and the people of Pangi and Bharmour.\n\nHindi is the official language and the language of schools and offices; at home most people speak Pahari languages such as Kangri, Mandeali, Kullui, Mahasui and Chambeali, while Kinnauri and the Tibetan-related languages of Lahaul and Spiti are spoken in the north and east. Most Himachalis live in villages, and Shimla is the only large city.",
        "2011 की जनगणना में हिमाचल प्रदेश की जनसंख्या 68.6 लाख थी, और प्रति वर्ग किमी 123 लोगों के साथ यह कम घनत्व वाले राज्यों में है। लिंगानुपात प्रति 1,000 पुरुषों पर 972 महिलाएँ और शिशु लिंगानुपात 909 था, दोनों 2001 से अधिक, और साक्षरता 82.8% थी, जो राष्ट्रीय 73.0% से काफ़ी अधिक है। अनुसूचित जातियाँ जनसंख्या का 25.2% थीं — भारत में सबसे अधिक हिस्सों में — और अनुसूचित जनजातियाँ 5.7%, जिनमें अधिकतर किन्नौरा, लाहौला, गद्दी, गुज्जर और पांगी व भरमौर के लोग हैं।\n\nहिंदी राजभाषा और विद्यालयों व कार्यालयों की भाषा है; घर में अधिकांश लोग कांगड़ी, मंडियाली, कुल्लुई, महासुई और चंबियाली जैसी पहाड़ी भाषाएँ बोलते हैं, जबकि उत्तर और पूर्व में किन्नौरी और लाहौल व स्पीति की तिब्बती से जुड़ी भाषाएँ बोली जाती हैं। अधिकांश हिमाचली गाँवों में रहते हैं, और शिमला एकमात्र बड़ा शहर है।",
        "2011 च्या जनगणनेनुसार हिमाचल प्रदेशची लोकसंख्या 68.6 लाख होती, आणि प्रति चौ.किमी 123 लोकांसह ते कमी घनतेच्या राज्यांपैकी आहे. दर 1,000 पुरुषांमागे 972 स्त्रिया होत्या व बाल लिंग गुणोत्तर 909 होते, दोन्ही 2001 पेक्षा अधिक, आणि साक्षरता 82.8% होती, राष्ट्रीय 73.0% पेक्षा बरीच अधिक. अनुसूचित जाती लोकसंख्येच्या 25.2% होत्या — भारतातील सर्वाधिक वाट्यांपैकी — आणि अनुसूचित जमाती 5.7%, ज्यांत बहुतांश किन्नौरा, लाहौला, गद्दी, गुज्जर आणि पांगी व भरमौरचे लोक आहेत.\n\nहिंदी ही राजभाषा व शाळा-कार्यालयांची भाषा आहे; घरी बहुतेक लोक कांगडी, मंडियाली, कुल्लुई, महासुई व चंबियाली यांसारख्या पहाडी भाषा बोलतात, तर उत्तर व पूर्वेत किन्नौरी आणि लाहौल व स्पितीच्या तिबेटीशी संबंधित भाषा बोलल्या जातात. बहुतेक हिमाचली गावांत राहतात, आणि शिमला हे एकमेव मोठे शहर आहे."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), hp["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), hp["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(968, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), hp["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(896, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), hp["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), hp["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(25.2, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 17.29 lakh people."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(5.7, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 3.92 lakh people."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("hi", "Hindi", "हिंदी", "हिंदी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("sa", "Sanskrit", "संस्कृत", "संस्कृत", m=("Second official language", "द्वितीय राजभाषा", "द्वितीय राजभाषा")),
        it3("kangri", "Kangri", "कांगड़ी", "कांगडी", m=("Pahari", "पहाड़ी", "पहाडी")), it3("mandeali", "Mandeali", "मंडियाली", "मंडियाली", m=("Pahari", "पहाड़ी", "पहाडी")),
        it3("kullui", "Kullui", "कुल्लुई", "कुल्लुई", m=("Pahari", "पहाड़ी", "पहाडी")), it3("mahasui", "Mahasui", "महासुई", "महासुई", m=("Pahari", "पहाड़ी", "पहाडी")),
        it3("kinnauri", "Kinnauri", "किन्नौरी", "किन्नौरी"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "The hills of Himachal were home to early tribes such as the Kolis, Kinnars and Khasas, and to small republics (janapadas) like the Audumbaras and Trigartas in the Kangra region. Over the centuries the region was divided into many hill kingdoms — Kangra (Trigarta), Chamba, Kullu, Mandi, Suket, Bilaspur (Kahlur), Sirmaur and the Shimla hill states — whose rajas built the temples of Chamba, Bharmour and Masroor and patronised the Pahari schools of miniature painting at Guler and Kangra. Kangra Fort was taken by the Mughals, then by Maharaja Sansar Chand, the Gurkhas and Ranjit Singh, before the British took control after the Anglo-Gurkha (1815–16) and Anglo-Sikh wars.\n\nShimla became the summer capital of British India from 1864, and the Kalka–Shimla railway opened in 1903. After Independence, 30 princely states were merged to form Himachal Pradesh on 15 April 1948. It became a Union Territory in 1956, absorbed the hill districts of Punjab — Kangra, Kullu, Shimla and Lahaul and Spiti — in 1966, and became a full State on 25 January 1971 under its first Chief Minister, Dr Yashwant Singh Parmar.",
        "हिमाचल की पहाड़ियाँ कोली, किन्नर और खश जैसी प्राचीन जनजातियों और कांगड़ा क्षेत्र के औदुंबर व त्रिगर्त जैसे छोटे गणराज्यों (जनपदों) का घर थीं। सदियों तक यह क्षेत्र कई पहाड़ी रियासतों में बँटा रहा — कांगड़ा (त्रिगर्त), चंबा, कुल्लू, मंडी, सुकेत, बिलासपुर (कहलूर), सिरमौर और शिमला की पहाड़ी रियासतें — जिनके राजाओं ने चंबा, भरमौर और मसरूर के मंदिर बनवाए और गुलेर व कांगड़ा में पहाड़ी लघुचित्र शैलियों को संरक्षण दिया। कांगड़ा क़िला मुग़लों ने लिया, फिर महाराजा संसार चंद, गोरखों और रणजीत सिंह ने, और आंग्ल-गोरखा (1815–16) और आंग्ल-सिख युद्धों के बाद अंग्रेज़ों ने नियंत्रण किया।\n\n1864 से शिमला ब्रिटिश भारत की ग्रीष्मकालीन राजधानी बना, और 1903 में कालका–शिमला रेलवे खुली। स्वतंत्रता के बाद 15 अप्रैल 1948 को 30 रियासतों को मिलाकर हिमाचल प्रदेश बना। 1956 में यह केंद्र शासित प्रदेश बना, 1966 में पंजाब के पहाड़ी ज़िले — कांगड़ा, कुल्लू, शिमला और लाहौल-स्पीति — इसमें मिले, और 25 जनवरी 1971 को पहले मुख्यमंत्री डॉ. यशवंत सिंह परमार के नेतृत्व में यह पूर्ण राज्य बना।",
        "हिमाचलच्या टेकड्या कोळी, किन्नर व खश यांसारख्या प्राचीन जमातींचे आणि कांगडा प्रदेशातील औदुंबर व त्रिगर्त यांसारख्या लहान गणराज्यांचे (जनपदांचे) घर होत्या. शतकानुशतके हा प्रदेश अनेक डोंगरी संस्थानांत विभागलेला राहिला — कांगडा (त्रिगर्त), चंबा, कुल्लू, मंडी, सुकेत, बिलासपूर (कहलूर), सिरमौर व शिमल्याची डोंगरी संस्थाने — ज्यांच्या राजांनी चंबा, भरमौर व मसरूरची मंदिरे बांधली आणि गुलेर व कांगडा येथील पहाडी लघुचित्र शैलींना आश्रय दिला. कांगडा किल्ला मुघलांनी घेतला, नंतर महाराजा संसारचंद, गुरखे व रणजितसिंह यांनी, आणि इंग्रज-गुरखा (1815–16) व इंग्रज-शीख युद्धांनंतर इंग्रजांनी नियंत्रण मिळवले.\n\n1864 पासून शिमला ही ब्रिटिश भारताची उन्हाळी राजधानी झाली, आणि 1903 मध्ये कालका–शिमला रेल्वे सुरू झाली. स्वातंत्र्यानंतर 15 एप्रिल 1948 रोजी 30 संस्थाने एकत्र करून हिमाचल प्रदेश बनवण्यात आला. 1956 मध्ये तो केंद्रशासित प्रदेश झाला, 1966 मध्ये पंजाबचे डोंगरी जिल्हे — कांगडा, कुल्लू, शिमला व लाहौल-स्पिती — त्यात मिळाले, आणि 25 जानेवारी 1971 रोजी पहिले मुख्यमंत्री डॉ. यशवंतसिंह परमार यांच्या नेतृत्वाखाली तो पूर्ण राज्य बनला."),
        conf="Editorial"),
    timeline([
        ev("summer", 1864, L("1864", "1864", "1864"), L("Shimla becomes summer capital of British India", "शिमला ब्रिटिश भारत की ग्रीष्मकालीन राजधानी बना", "शिमला ब्रिटिश भारताची उन्हाळी राजधानी")),
        ev("railway", 1903, L("1903", "1903", "1903"), L("Kalka–Shimla railway opens", "कालका–शिमला रेलवे खुली", "कालका–शिमला रेल्वे सुरू")),
        ev("formed", 1948, L("15 April 1948", "15 अप्रैल 1948", "15 एप्रिल 1948"), L("Himachal Pradesh formed from 30 princely states", "30 रियासतों से हिमाचल प्रदेश बना", "30 संस्थानांतून हिमाचल प्रदेशाची निर्मिती")),
        ev("ut", 1956, L("1 November 1956", "1 नवंबर 1956", "1 नोव्हेंबर 1956"), L("Becomes a Union Territory", "केंद्र शासित प्रदेश बना", "केंद्रशासित प्रदेश")),
        ev("merger", 1966, L("1 November 1966", "1 नवंबर 1966", "1 नोव्हेंबर 1966"), L("Hill areas of Punjab added", "पंजाब के पहाड़ी क्षेत्र जुड़े", "पंजाबचे डोंगरी भाग जोडले")),
        ev("state", 1971, L("25 January 1971", "25 जनवरी 1971", "25 जानेवारी 1971"), L("Full statehood — India's 18th State", "पूर्ण राज्य — भारत का 18वाँ राज्य", "पूर्ण राज्य — भारताचे 18 वे राज्य")),
        ev("atal", 2020, L("3 October 2020", "3 अक्टूबर 2020", "3 ऑक्टोबर 2020"), L("Atal Tunnel opened under Rohtang", "रोहतांग के नीचे अटल सुरंग खुली", "रोहतांगखालील अटल बोगदा खुला")),
        ev("cm2022", 2022, L("11 December 2022", "11 दिसंबर 2022", "11 डिसेंबर 2022"), L("Sukhvinder Singh Sukhu sworn in as Chief Minister", "सुखविंदर सिंह सुक्खू ने मुख्यमंत्री पद की शपथ ली", "सुखविंदर सिंह सुक्खू यांचा मुख्यमंत्रिपदाचा शपथविधी")),
    ]),
    lst("heritage", [
        it3("kangra", "Kangra Fort", "कांगड़ा क़िला", "कांगडा किल्ला", m=("Ancient hill fort", "प्राचीन पहाड़ी क़िला", "प्राचीन डोंगरी किल्ला")),
        it3("masroor", "Masroor rock-cut temples", "मसरूर शैलकृत मंदिर", "मसरूर शैलकोरीव मंदिरे", m=("8th century", "8वीं सदी", "आठवे शतक")),
        it3("chamba", "Lakshmi Narayan temples, Chamba", "लक्ष्मी नारायण मंदिर, चंबा", "लक्ष्मी नारायण मंदिरे, चंबा", m=("Shikhara temples", "शिखर शैली मंदिर", "शिखर शैलीची मंदिरे")),
        it3("tabo", "Tabo Monastery, Spiti", "ताबो मठ, स्पीति", "ताबो मठ, स्पिती", m=("Founded 996 CE", "996 ई. में स्थापित", "इ.स. 996 मध्ये स्थापना")),
        it3("hadimba", "Hadimba Devi temple, Manali", "हिडिंबा देवी मंदिर, मनाली", "हिडिंबा देवी मंदिर, मनाली", m=("Pagoda-style wooden temple", "पगोडा शैली का लकड़ी का मंदिर", "पॅगोडा शैलीतील लाकडी मंदिर")),
        it3("viceregal", "Viceregal Lodge (Rashtrapati Niwas), Shimla", "वाइसरीगल लॉज (राष्ट्रपति निवास), शिमला", "व्हाइसरीगल लॉज (राष्ट्रपती निवास), शिमला", m=("Indian Institute of Advanced Study", "भारतीय उच्च अध्ययन संस्थान", "भारतीय प्रगत अध्ययन संस्था")),
        it3("kalka", "Kalka–Shimla Railway", "कालका–शिमला रेलवे", "कालका–शिमला रेल्वे", m=("UNESCO World Heritage (Mountain Railways of India)", "यूनेस्को विश्व धरोहर (भारत की पर्वतीय रेलें)", "युनेस्को जागतिक वारसा (भारताच्या पर्वतीय रेल्वे)")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("hp mod1 ok")
