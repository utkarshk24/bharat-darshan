"""Jammu and Kashmir (UT) modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-JK"
C = research("census_b5plus.json"); J = C["jk_ut"]; DES = J["url"]
PYD = "https://statistics.py.gov.in/state-wise-population"
jk = read("regions/IN-JK.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Jammu and Kashmir is a Union Territory with a legislature in the far north of India. It has two divisions: the Kashmir valley, an oval basin of the Jhelum ringed by the Pir Panjal and the Great Himalaya, and the Jammu division, which runs from the plains along the Punjab border through the Shivalik and Pir Panjal ranges. Ladakh lies to the east, Himachal Pradesh and Punjab to the south, and the Line of Control and the international border with Pakistan to the west. The present UT had 1.23 crore people at the 2011 Census. Srinagar is the summer capital and Jammu the winter capital; Anantnag, Baramulla, Sopore, Kathua and Udhampur are other major towns.\n\nThe former State of Jammu and Kashmir was reorganised by Parliament in August 2019: from 31 October 2019 it became two Union Territories, Jammu and Kashmir with an elected Assembly and Ladakh without one. Kashmiri, Dogri, Hindi, Urdu and English are the official languages.",
        "जम्मू और कश्मीर भारत के सुदूर उत्तर में विधानमंडल वाला केंद्र शासित प्रदेश है। इसके दो संभाग हैं: कश्मीर घाटी, जो पीर पंजाल और महान हिमालय से घिरी झेलम की अंडाकार द्रोणी है, और जम्मू संभाग, जो पंजाब सीमा के मैदानों से शिवालिक और पीर पंजाल श्रेणियों तक फैला है। इसके पूर्व में लद्दाख, दक्षिण में हिमाचल प्रदेश और पंजाब, और पश्चिम में नियंत्रण रेखा और पाकिस्तान के साथ अंतरराष्ट्रीय सीमा है। 2011 की जनगणना में वर्तमान केंद्र शासित प्रदेश की जनसंख्या 1.23 करोड़ थी। श्रीनगर ग्रीष्मकालीन राजधानी है और जम्मू शीतकालीन राजधानी; अनंतनाग, बारामूला, सोपोर, कठुआ और उधमपुर अन्य प्रमुख नगर हैं।\n\nअगस्त 2019 में संसद ने पूर्ववर्ती जम्मू-कश्मीर राज्य का पुनर्गठन किया: 31 अक्टूबर 2019 से यह दो केंद्र शासित प्रदेश बना — निर्वाचित विधानसभा वाला जम्मू और कश्मीर और बिना विधानसभा वाला लद्दाख। कश्मीरी, डोगरी, हिंदी, उर्दू और अंग्रेज़ी राजभाषाएँ हैं।",
        "जम्मू व काश्मीर हा भारताच्या अगदी उत्तरेकडील विधिमंडळ असलेला केंद्रशासित प्रदेश आहे. त्याचे दोन विभाग आहेत: पीर पंजाल व महान हिमालयाने वेढलेले झेलमचे अंडाकृती खोरे असलेले काश्मीर खोरे, आणि पंजाब सीमेवरील मैदानांपासून शिवालिक व पीर पंजाल रांगांपर्यंत पसरलेला जम्मू विभाग. त्याच्या पूर्वेला लडाख, दक्षिणेला हिमाचल प्रदेश व पंजाब, आणि पश्चिमेला नियंत्रण रेषा व पाकिस्तानसोबतची आंतरराष्ट्रीय सीमा आहे. 2011 च्या जनगणनेनुसार सध्याच्या केंद्रशासित प्रदेशाची लोकसंख्या 1.23 कोटी होती. श्रीनगर ही उन्हाळी व जम्मू ही हिवाळी राजधानी आहे; अनंतनाग, बारामुल्ला, सोपोर, कठुआ व उधमपूर ही इतर प्रमुख शहरे आहेत.\n\nऑगस्ट 2019 मध्ये संसदेने पूर्वीच्या जम्मू-काश्मीर राज्याची पुनर्रचना केली: 31 ऑक्टोबर 2019 पासून ते दोन केंद्रशासित प्रदेश झाले — निवडून आलेल्या विधानसभेसह जम्मू व काश्मीर आणि विधानसभेशिवाय लडाख. काश्मिरी, डोगरी, हिंदी, उर्दू व इंग्रजी या राजभाषा आहेत."),
        sources=["jk-des"], conf="Editorial"),
    prose("intro-unique", L(
        "Kashmir has been celebrated for centuries for its beauty — the Dal lake and its houseboats and shikaras, the Mughal gardens of Srinagar, the meadows of Gulmarg, Pahalgam and Sonamarg, and the chinar trees that turn red in autumn. Its crafts are among the finest in India: pashmina and Kani shawls, hand-knotted carpets, papier-mâché, walnut-wood carving and the willow cricket bat, and Kashmir is India's main source of saffron and a major producer of apples and walnuts. Jammu, the 'city of temples', is the gateway to the shrine of Mata Vaishno Devi, one of India's most visited pilgrimages, and the annual Amarnath Yatra climbs to a cave shrine in the high Himalaya. The region's history has also been marked by conflict since 1947.",
        "कश्मीर सदियों से अपनी सुंदरता के लिए प्रसिद्ध रहा है — डल झील और उसके हाउसबोट और शिकारे, श्रीनगर के मुग़ल बाग़, गुलमर्ग, पहलगाम और सोनमर्ग के घास के मैदान, और शरद ऋतु में लाल होने वाले चिनार के पेड़। इसके शिल्प भारत के सबसे उत्कृष्ट में हैं: पश्मीना और कानी शॉल, हाथ से गाँठे क़ालीन, पेपर माशी, अखरोट की लकड़ी की नक़्क़ाशी और विलो का क्रिकेट बल्ला, और कश्मीर भारत में केसर का मुख्य स्रोत और सेब व अखरोट का बड़ा उत्पादक है। 'मंदिरों का शहर' जम्मू माता वैष्णो देवी के धाम का प्रवेश द्वार है, जो भारत की सबसे अधिक यात्रियों वाली तीर्थयात्राओं में है, और वार्षिक अमरनाथ यात्रा ऊँचे हिमालय की एक गुफा तक जाती है। 1947 से इस क्षेत्र का इतिहास संघर्ष से भी चिह्नित रहा है।",
        "काश्मीर शतकानुशतके आपल्या सौंदर्यासाठी प्रसिद्ध आहे — दल सरोवर व त्यातील हाउसबोट आणि शिकारे, श्रीनगरच्या मुघल बागा, गुलमर्ग, पहलगाम व सोनमर्गची कुरणे, आणि शरद ऋतूत लाल होणारे चिनार वृक्ष. त्याच्या हस्तकला भारतातील सर्वोत्कृष्टांपैकी आहेत: पश्मीना व कानी शाली, हाताने विणलेले गालिचे, पेपर-माशे, अक्रोडाच्या लाकडावरील कोरीवकाम व विलोची क्रिकेट बॅट, आणि काश्मीर हे भारतातील केशराचे मुख्य उगमस्थान व सफरचंद आणि अक्रोडाचे मोठे उत्पादक आहे. 'मंदिरांचे शहर' जम्मू हे माता वैष्णोदेवीच्या धामाचे प्रवेशद्वार आहे, जी भारतातील सर्वाधिक भाविक येणाऱ्या तीर्थयात्रांपैकी एक आहे, आणि वार्षिक अमरनाथ यात्रा उंच हिमालयातील एका गुहेपर्यंत जाते. 1947 पासून या प्रदेशाच्या इतिहासावर संघर्षाचाही ठसा आहे."),
        title=L("What makes Jammu and Kashmir unique?", "जम्मू और कश्मीर को ख़ास क्या बनाता है?", "जम्मू व काश्मीरचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Union Territory since", "केंद्र शासित प्रदेश", "केंद्रशासित प्रदेश"), L("31 October 2019 (Jammu and Kashmir Reorganisation Act, 2019)", "31 अक्टूबर 2019 से (जम्मू और कश्मीर पुनर्गठन अधिनियम, 2019)", "31 ऑक्टोबर 2019 पासून (जम्मू व काश्मीर पुनर्रचना कायदा, 2019)")],
           [L("Districts / divisions", "ज़िले / संभाग", "जिल्हे / विभाग"), L("20 / 2 (Jammu, Kashmir)", "20 / 2 (जम्मू, कश्मीर)", "20 / 2 (जम्मू, काश्मीर)")],
           [L("Capitals", "राजधानियाँ", "राजधान्या"), L("Srinagar (summer); Jammu (winter)", "श्रीनगर (ग्रीष्मकालीन); जम्मू (शीतकालीन)", "श्रीनगर (उन्हाळी); जम्मू (हिवाळी)")],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Kashmiri, Dogri, Hindi, Urdu, English", "कश्मीरी, डोगरी, हिंदी, उर्दू, अंग्रेज़ी", "काश्मिरी, डोगरी, हिंदी, उर्दू, इंग्रजी")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("High Court of Jammu & Kashmir and Ladakh (Srinagar and Jammu)", "जम्मू-कश्मीर और लद्दाख उच्च न्यायालय (श्रीनगर और जम्मू)", "जम्मू-काश्मीर व लडाख उच्च न्यायालय (श्रीनगर व जम्मू)")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "JK"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be linked to the Reorganisation Act and the UT's notifications in review.", "संपादकीय; समीक्षा में पुनर्गठन अधिनियम और केंद्र शासित प्रदेश की अधिसूचनाओं से जोड़ा जाएगा।", "संपादकीय; तपासणीत पुनर्रचना कायदा व केंद्रशासित प्रदेशाच्या अधिसूचनांशी जोडले जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "The Kashmir valley, about 135 km long and 1,600 m above sea level, is the flat floor of an ancient lake, filled with alluvium and karewa terraces where saffron is grown. The Jhelum flows through it past Anantnag, Srinagar and Sopore into the Wular lake and out through Baramulla. The Pir Panjal separates the valley from the Jammu division, crossed by the Banihal pass and the Jawahar and Navyug tunnels, and the Great Himalaya rises to the north and east, with the Zojila pass leading to Ladakh. The Jammu division descends through the hilly districts of Doda, Kishtwar, Ramban, Reasi, Rajouri and Poonch to the Shivaliks and the plains of Jammu, Samba and Kathua, drained by the Chenab, Tawi and Ravi.",
        "लगभग 135 किमी लंबी और समुद्र तल से 1,600 मीटर ऊँची कश्मीर घाटी एक प्राचीन झील का समतल तल है, जो जलोढ़ और करेवा वेदिकाओं से भरी है, जहाँ केसर उगाया जाता है। झेलम इसमें अनंतनाग, श्रीनगर और सोपोर से होकर वुलर झील में बहती है और बारामूला से बाहर निकलती है। पीर पंजाल घाटी को जम्मू संभाग से अलग करता है, जिसे बनिहाल दर्रा और जवाहर व नवयुग सुरंगें पार करती हैं, और उत्तर व पूर्व में महान हिमालय उठता है, जहाँ ज़ोजिला दर्रा लद्दाख की ओर जाता है। जम्मू संभाग डोडा, किश्तवाड़, रामबन, रियासी, राजौरी और पुंछ के पहाड़ी ज़िलों से होकर शिवालिक और जम्मू, सांबा व कठुआ के मैदानों तक उतरता है, जिनका जल चिनाब, तवी और रावी बहाती हैं।",
        "सुमारे 135 किमी लांब व समुद्रसपाटीपासून 1,600 मीटर उंचीवरील काश्मीर खोरे हे एका प्राचीन सरोवराचा सपाट तळ आहे, गाळ व करेवा टप्प्यांनी भरलेला, जिथे केशर पिकवले जाते. झेलम त्यातून अनंतनाग, श्रीनगर व सोपोरमार्गे वुलर सरोवरात वाहते व बारामुल्लाहून बाहेर पडते. पीर पंजाल खोऱ्याला जम्मू विभागापासून वेगळे करतो, जो बनिहाल खिंड व जवाहर आणि नवयुग बोगद्यांनी ओलांडला जातो, आणि उत्तर व पूर्वेला महान हिमालय उठतो, जिथे झोजिला खिंड लडाखकडे जाते. जम्मू विभाग डोडा, किश्तवाड, रामबन, रियासी, राजौरी व पुंछ या डोंगरी जिल्ह्यांमधून शिवालिक व जम्मू, सांबा आणि कठुआच्या मैदानांपर्यंत उतरतो, ज्यांचे पाणी चिनाब, तवी व रावी वाहून नेतात."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area (Census 2011, present UT)", "भौगोलिक क्षेत्रफल (जनगणना 2011, वर्तमान केंद्र शासित प्रदेश)", "भौगोलिक क्षेत्रफळ (जनगणना 2011, सध्याचा केंद्रशासित प्रदेश)"), jk["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("la", "Ladakh (east)", "लद्दाख (पूर्व)", "लडाख (पूर्व)"), it3("hp", "Himachal Pradesh (south-east)", "हिमाचल प्रदेश (दक्षिण-पूर्व)", "हिमाचल प्रदेश (आग्नेय)"),
        it3("pb", "Punjab (south)", "पंजाब (दक्षिण)", "पंजाब (दक्षिण)"), it3("loc", "Line of Control and international border with Pakistan (west)", "नियंत्रण रेखा और पाकिस्तान के साथ अंतरराष्ट्रीय सीमा (पश्चिम)", "नियंत्रण रेषा व पाकिस्तानसोबतची आंतरराष्ट्रीय सीमा (पश्चिम)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("jhelum", "Jhelum", "झेलम", "झेलम", d=("Rises at Verinag; the river of the Kashmir valley.", "वेरीनाग से निकलती है; कश्मीर घाटी की नदी।", "वेरीनाग येथे उगम; काश्मीर खोऱ्याची नदी.")),
        it3("chenab", "Chenab", "चिनाब", "चिनाब", d=("Cuts a deep gorge through Kishtwar, Doda, Ramban and Reasi; Baglihar and Salal dams.", "किश्तवाड़, डोडा, रामबन और रियासी में गहरी घाटी बनाती है; बगलिहार और सलाल बाँध।", "किश्तवाड, डोडा, रामबन व रियासीमधून खोल घळ कोरते; बगलिहार व सलाल धरणे.")),
        it3("tawi", "Tawi", "तवी", "तवी", d=("Flows through Jammu city.", "जम्मू शहर से होकर बहती है।", "जम्मू शहरातून वाहते.")),
        it3("ravi", "Ravi", "रावी", "रावी", d=("Forms the border with Punjab near Kathua; Ranjit Sagar dam.", "कठुआ के पास पंजाब के साथ सीमा बनाती है; रणजीत सागर बाँध।", "कठुआजवळ पंजाबसोबतची सीमा बनवते; रणजित सागर धरण.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point within the UT — official elevation", "केंद्र शासित प्रदेश का सर्वोच्च बिंदु — आधिकारिक ऊँचाई", "केंद्रशासित प्रदेशातील सर्वोच्च शिखर — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Length of the Line of Control and international border in the UT", "केंद्र शासित प्रदेश में नियंत्रण रेखा और अंतरराष्ट्रीय सीमा की लंबाई", "केंद्रशासित प्रदेशातील नियंत्रण रेषा व आंतरराष्ट्रीय सीमेची लांबी"), "india-gov", "Ministry of Home Affairs (Border Management)."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "The Kashmir valley has four distinct seasons: a warm summer (June–August), a crisp, golden autumn, a cold winter with snow and sub-zero nights — the 40 days of harshest cold from late December are called chillai kalan — and a spring of almond and fruit blossom. Most of its precipitation comes from western disturbances in winter and spring rather than the monsoon. The Jammu plains, by contrast, have hot summers with temperatures well above 40 °C, a monsoon from July to September and mild winters, while the high ranges are snowbound for months.",
        "कश्मीर घाटी में चार स्पष्ट ऋतुएँ होती हैं: गर्म गर्मी (जून–अगस्त), खिली हुई सुनहरी शरद ऋतु, बर्फ़ और शून्य से नीचे की रातों वाली ठंडी सर्दी — दिसंबर के अंत से सबसे कड़ी ठंड के 40 दिनों को चिल्लई कलाँ कहा जाता है — और बादाम व फलों के फूलों वाला वसंत। इसकी अधिकांश वर्षा मानसून के बजाय सर्दियों और वसंत में पश्चिमी विक्षोभों से होती है। इसके विपरीत जम्मू के मैदानों में गर्मियाँ गर्म होती हैं, तापमान 40 °C से काफ़ी ऊपर, जुलाई से सितंबर तक मानसून और सर्दियाँ हल्की, जबकि ऊँची श्रेणियाँ महीनों बर्फ़ से ढकी रहती हैं।",
        "काश्मीर खोऱ्यात चार स्पष्ट ऋतू असतात: उबदार उन्हाळा (जून–ऑगस्ट), प्रसन्न सोनेरी शरद, बर्फ व शून्याखालील रात्रींचा थंड हिवाळा — डिसेंबरच्या अखेरीपासूनच्या सर्वांत कडक थंडीच्या 40 दिवसांना चिल्लई कलां म्हणतात — आणि बदाम व फळांच्या बहराचा वसंत. त्याचा बहुतेक पाऊस मान्सूनऐवजी हिवाळा व वसंतातील पश्चिमी विक्षोभांमुळे पडतो. याउलट जम्मूच्या मैदानांत उन्हाळा उष्ण असतो, तापमान 40 °C च्या बरेच वर, जुलै ते सप्टेंबर मान्सून व हिवाळा सौम्य, तर उंच रांगा महिनोन्महिने बर्फाखाली असतात."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Srinagar", "श्रीनगर", "श्रीनगर"), "lat": 34.0837, "lon": 74.7973},
        {"name": L("Jammu", "जम्मू", "जम्मू"), "lat": 32.7266, "lon": 74.8570},
        {"name": L("Gulmarg", "गुलमर्ग", "गुलमर्ग"), "lat": 34.0484, "lon": 74.3805},
        {"name": L("Pahalgam", "पहलगाम", "पहलगाम"), "lat": 34.0161, "lon": 75.3150},
    ]},
    lst("best", [
        it3("spring", "March to May", "मार्च से मई", "मार्च ते मे", d=("Tulip garden and fruit blossom in the valley.", "घाटी में ट्यूलिप उद्यान और फलों के फूल।", "खोऱ्यात ट्युलिप उद्यान व फळांचा बहर.")),
        it3("summer", "June to August", "जून से अगस्त", "जून ते ऑगस्ट", d=("Meadows of Sonamarg and Pahalgam; Amarnath Yatra.", "सोनमर्ग और पहलगाम के घास के मैदान; अमरनाथ यात्रा।", "सोनमर्ग व पहलगामची कुरणे; अमरनाथ यात्रा.")),
        it3("autumn", "September to November", "सितंबर से नवंबर", "सप्टेंबर ते नोव्हेंबर", d=("Red chinars and the saffron harvest.", "लाल चिनार और केसर की फ़सल।", "लाल चिनार व केशराची काढणी.")),
        it3("winter", "December to March", "दिसंबर से मार्च", "डिसेंबर ते मार्च", d=("Skiing at Gulmarg; Jammu is mild and best for temples.", "गुलमर्ग में स्कीइंग; जम्मू सुहावना और मंदिरों के लिए सबसे अच्छा।", "गुलमर्गमध्ये स्कीइंग; जम्मू सौम्य व मंदिरांसाठी उत्तम.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual precipitation, Srinagar and Jammu", "सामान्य वार्षिक वर्षा, श्रीनगर और जम्मू", "सरासरी वार्षिक पर्जन्य, श्रीनगर व जम्मू"), "imd", "IMD Srinagar meteorological centre."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Life in the valley moves around the samovar of noon chai (salt tea) or kahwa, the bakers' kandur shops at dawn, and the shikaras gliding across the Dal at dusk; in winter people keep warm under the pheran with a kangri firepot. Weddings are known for the multi-course wazwan feast cooked by wazas. Sufi shrines such as Hazratbal and Makhdoom Sahib and the Kheer Bhawani temple are places of shared devotion. In Jammu, temple bells ring at the Raghunath and Ranbireshwar temples, Dogra food and folk songs fill the bazaars, and pilgrims to Vaishno Devi fill the town of Katra year-round.",
        "घाटी का जीवन नून चाय (नमकीन चाय) या कहवा के समावार, भोर में कंदूर नानबाइयों की दुकानों, और साँझ को डल पर सरकते शिकारों के इर्द-गिर्द चलता है; सर्दियों में लोग फ़िरन और कांगड़ी (अँगीठी) से गर्म रहते हैं। शादियाँ वाज़ों द्वारा पकाए गए कई व्यंजनों वाले वाज़वान भोज के लिए जानी जाती हैं। हज़रतबल और मख़दूम साहिब जैसी सूफ़ी दरगाहें और खीर भवानी मंदिर साझी श्रद्धा के स्थान हैं। जम्मू में रघुनाथ और रणबीरेश्वर मंदिरों में घंटियाँ बजती हैं, डोगरा भोजन और लोकगीत बाज़ारों में गूँजते हैं, और वैष्णो देवी के तीर्थयात्री वर्ष भर कटरा नगर को भरे रखते हैं।",
        "खोऱ्यातील जीवन नून चाय (खारट चहा) किंवा कहवाच्या समोवार, पहाटे कंदूर नानबाईंची दुकाने आणि संध्याकाळी दलवर सरकणारे शिकारे यांभोवती फिरते; हिवाळ्यात लोक फिरन व कांगडी (शेगडी) यांनी ऊब घेतात. लग्ने वाझांनी शिजवलेल्या अनेक पदार्थांच्या वाझवान मेजवानीसाठी ओळखली जातात. हजरतबल व मखदूम साहिबसारखे सूफी दर्गे आणि खीर भवानी मंदिर ही सामायिक श्रद्धेची ठिकाणे आहेत. जम्मूमध्ये रघुनाथ व रणबीरेश्वर मंदिरांत घंटा वाजतात, डोग्रा खाद्यपदार्थ व लोकगीते बाजारांत गजबजतात, आणि वैष्णोदेवीचे यात्रेकरू वर्षभर कटरा शहर भरून टाकतात."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "The area of the present Union Territory had 1.23 crore people at the 2011 Census, according to the J&K Directorate of Economics and Statistics, with about 290 people per km² and 27.5% living in towns. The sex ratio was 892 women per 1,000 men and the child sex ratio 860 — among the lowest in India. Literacy was 67.0%, higher in the Jammu division (72.0%) than in the Kashmir division (63.0%). Scheduled Castes made up 7.5% of the population, almost all in the Jammu division, and Scheduled Tribes 10.4% — mainly Gujjars and Bakarwals, with Gaddis and Sippis; Paharis were added to the Scheduled Tribes list in 2024.\n\nKashmiri is the main language of the valley, and Dogri of the Jammu plains and hills; Gojri, Pahari, Punjabi and other languages are spoken in the hill districts, and Urdu, Hindi and English are widely used in schools and offices.",
        "जम्मू-कश्मीर अर्थशास्त्र एवं सांख्यिकी निदेशालय के अनुसार 2011 की जनगणना में वर्तमान केंद्र शासित प्रदेश के क्षेत्र की जनसंख्या 1.23 करोड़ थी, प्रति वर्ग किमी लगभग 290 लोग, और 27.5% लोग नगरों में रहते थे। लिंगानुपात प्रति 1,000 पुरुषों पर 892 महिलाएँ और शिशु लिंगानुपात 860 था — भारत में सबसे कम में। साक्षरता 67.0% थी, जो कश्मीर संभाग (63.0%) की तुलना में जम्मू संभाग (72.0%) में अधिक थी। अनुसूचित जातियाँ जनसंख्या का 7.5% थीं, लगभग सभी जम्मू संभाग में, और अनुसूचित जनजातियाँ 10.4% — मुख्यतः गुज्जर और बकरवाल, साथ में गद्दी और सिप्पी; 2024 में पहाड़ियों को अनुसूचित जनजातियों की सूची में जोड़ा गया।\n\nकश्मीरी घाटी की मुख्य भाषा है और डोगरी जम्मू के मैदानों और पहाड़ियों की; पहाड़ी ज़िलों में गोजरी, पहाड़ी, पंजाबी और अन्य भाषाएँ बोली जाती हैं, और विद्यालयों व कार्यालयों में उर्दू, हिंदी और अंग्रेज़ी का व्यापक उपयोग होता है।",
        "जम्मू-काश्मीर अर्थशास्त्र व सांख्यिकी संचालनालयानुसार 2011 च्या जनगणनेत सध्याच्या केंद्रशासित प्रदेशाच्या क्षेत्राची लोकसंख्या 1.23 कोटी होती, प्रति चौ.किमी सुमारे 290 लोक, आणि 27.5% लोक शहरांत राहत होते. दर 1,000 पुरुषांमागे 892 स्त्रिया होत्या व बाल लिंग गुणोत्तर 860 होते — भारतातील सर्वांत कमींपैकी. साक्षरता 67.0% होती, काश्मीर विभागापेक्षा (63.0%) जम्मू विभागात (72.0%) अधिक. अनुसूचित जाती लोकसंख्येच्या 7.5% होत्या, जवळपास सर्व जम्मू विभागात, आणि अनुसूचित जमाती 10.4% — मुख्यतः गुज्जर व बकरवाल, सोबत गद्दी व सिप्पी; 2024 मध्ये पहाडींना अनुसूचित जमातींच्या यादीत समाविष्ट करण्यात आले.\n\nकाश्मिरी ही खोऱ्याची मुख्य भाषा आहे आणि डोगरी जम्मूच्या मैदानांची व डोंगरांची; डोंगरी जिल्ह्यांत गोजरी, पहाडी, पंजाबी व इतर भाषा बोलल्या जातात, आणि शाळा-कार्यालयांत उर्दू, हिंदी व इंग्रजीचा मोठा वापर होतो."),
        sources=["jk-des"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011, present UT)", "जनसंख्या (जनगणना 2011, वर्तमान केंद्र शासित प्रदेश)", "लोकसंख्या (जनगणना 2011, सध्याचा केंद्रशासित प्रदेश)"), jk["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), jk["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"]),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), jk["childSexRatio2011"], "ratio", "higher-is-better", national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), jk["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("urb", L("Urban population share", "शहरी जनसंख्या का हिस्सा", "नागरी लोकसंख्येचा वाटा"), jk["urbanisation2011"], "percent"),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), jk["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(7.54, "%", "2011", "census", "jk-des", DES, note="J&K DES, UT at a Glance 2024-25: 9,24,485 people."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(10.39, "%", "2011", "census", "jk-des", DES, note="J&K DES, UT at a Glance 2024-25: 12,75,106 people (Census 2011 list, before the 2024 additions)."), "percent"),
    ], title=L("Census 2011 at a glance (present UT)", "जनगणना 2011 एक नज़र में (वर्तमान केंद्र शासित प्रदेश)", "जनगणना 2011 दृष्टिक्षेपात (सध्याचा केंद्रशासित प्रदेश)")),
    lst("langs", [
        it3("ks", "Kashmiri", "कश्मीरी", "काश्मिरी", m=("Official language", "राजभाषा", "राजभाषा")), it3("doi", "Dogri", "डोगरी", "डोगरी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("ur", "Urdu", "उर्दू", "उर्दू", m=("Official language", "राजभाषा", "राजभाषा")), it3("hi", "Hindi", "हिंदी", "हिंदी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("en", "English", "अंग्रेज़ी", "इंग्रजी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("gojri", "Gojri", "गोजरी", "गोजरी"), it3("pahari", "Pahari", "पहाड़ी", "पहाडी"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Paharis and other communities added to the ST list in 2024 — official notification", "2024 में अनुसूचित जनजाति सूची में जोड़े गए पहाड़ी और अन्य समुदाय — आधिकारिक अधिसूचना", "2024 मध्ये अनुसूचित जमाती यादीत जोडलेले पहाडी व इतर समुदाय — अधिकृत अधिसूचना"), "tribal-affairs", "Constitution (Jammu and Kashmir) Scheduled Tribes Order (Amendment) Act, 2024."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table for the districts of the present UT; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "jk-planning", "J&K Planning Department gives 133.05 lakh for 2020 (projected)."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Kashmir's history is unusually well recorded. Neolithic people lived at Burzahom near Srinagar, and the valley later became a centre of Buddhist learning under the Kushans. Kalhana's Rajatarangini (12th century) chronicles its Hindu kings, among them Lalitaditya Muktapida, builder of the Martand sun temple in the 8th century, and Kashmir was a home of Shaiva philosophy and Sanskrit scholarship, with thinkers such as Abhinavagupta. The Shah Mir sultans ruled from 1339; Zain-ul-Abidin (Budshah, 15th century) is remembered for tolerance and for bringing crafts such as papier-mâché and carpet-weaving. The Mughals annexed Kashmir in 1586 and laid out its gardens, followed by Afghan (1752) and Sikh (1819) rule.\n\nAfter the first Anglo-Sikh war, the Treaty of Amritsar (1846) made Gulab Singh, the Dogra ruler of Jammu, Maharaja of Jammu and Kashmir. In October 1947, after an invasion by tribesmen from Pakistan, Maharaja Hari Singh signed the Instrument of Accession to India; fighting ended in 1949 with a ceasefire line that later became the Line of Control. Under Article 370 the State had a special constitutional status until August 2019, when Parliament made the provision inoperative and reorganised the State into two Union Territories. An armed insurgency from 1989–90 caused heavy loss of life and the displacement of most Kashmiri Pandits from the valley. The UT's first Assembly elections were held in 2024.",
        "कश्मीर का इतिहास असाधारण रूप से अच्छी तरह दर्ज है। श्रीनगर के पास बुर्ज़होम में नवपाषाण काल के लोग रहते थे, और बाद में कुषाणों के समय घाटी बौद्ध विद्या का केंद्र बनी। कल्हण की राजतरंगिणी (12वीं सदी) इसके हिंदू राजाओं का वृत्तांत देती है, जिनमें 8वीं सदी में मार्तंड सूर्य मंदिर बनवाने वाले ललितादित्य मुक्तापीड हैं, और कश्मीर अभिनवगुप्त जैसे चिंतकों के साथ शैव दर्शन और संस्कृत विद्या का घर था। 1339 से शाह मीर सुल्तानों ने शासन किया; ज़ैनुल आबिदीन (बडशाह, 15वीं सदी) सहिष्णुता के लिए और पेपर माशी व क़ालीन बुनाई जैसे शिल्प लाने के लिए याद किए जाते हैं। मुग़लों ने 1586 में कश्मीर को अपने राज्य में मिलाया और इसके बाग़ बनवाए, जिसके बाद अफ़ग़ान (1752) और सिख (1819) शासन आया।\n\nपहले आंग्ल-सिख युद्ध के बाद अमृतसर की संधि (1846) ने जम्मू के डोगरा शासक गुलाब सिंह को जम्मू और कश्मीर का महाराजा बनाया। अक्टूबर 1947 में पाकिस्तान से आए क़बायलियों के आक्रमण के बाद महाराजा हरि सिंह ने भारत के साथ विलय पत्र पर हस्ताक्षर किए; 1949 में युद्धविराम रेखा के साथ लड़ाई समाप्त हुई, जो बाद में नियंत्रण रेखा बनी। अनुच्छेद 370 के तहत राज्य को अगस्त 2019 तक विशेष संवैधानिक दर्जा प्राप्त था, जब संसद ने इस प्रावधान को निष्क्रिय किया और राज्य को दो केंद्र शासित प्रदेशों में पुनर्गठित किया। 1989–90 से शुरू हुए सशस्त्र उग्रवाद में भारी जनहानि हुई और अधिकांश कश्मीरी पंडितों को घाटी से विस्थापित होना पड़ा। केंद्र शासित प्रदेश के पहले विधानसभा चुनाव 2024 में हुए।",
        "काश्मीरचा इतिहास असामान्यपणे चांगल्या प्रकारे नोंदलेला आहे. श्रीनगरजवळील बुर्झहोम येथे नवाश्मयुगीन लोक राहत होते, आणि नंतर कुषाणांच्या काळात खोरे बौद्ध विद्येचे केंद्र बनले. कल्हणाची राजतरंगिणी (बारावे शतक) तिथल्या हिंदू राजांचा वृत्तांत देते, ज्यांत आठव्या शतकात मार्तंड सूर्यमंदिर बांधणारे ललितादित्य मुक्तापीड आहेत, आणि अभिनवगुप्तांसारख्या विचारवंतांसह काश्मीर हे शैव तत्त्वज्ञान व संस्कृत विद्येचे घर होते. 1339 पासून शाह मीर सुलतानांनी राज्य केले; झैनुल आबिदीन (बडशाह, पंधरावे शतक) सहिष्णुतेसाठी आणि पेपर-माशे व गालिचे विणकामासारख्या हस्तकला आणल्याबद्दल स्मरणात आहेत. मुघलांनी 1586 मध्ये काश्मीर आपल्या राज्यात सामील केले व तिथल्या बागा उभारल्या, त्यानंतर अफगाण (1752) व शीख (1819) राजवट आली.\n\nपहिल्या इंग्रज-शीख युद्धानंतर अमृतसरच्या तहाने (1846) जम्मूचे डोग्रा राज्यकर्ते गुलाबसिंह यांना जम्मू व काश्मीरचे महाराजा बनवले. ऑक्टोबर 1947 मध्ये पाकिस्तानातून आलेल्या टोळीवाल्यांच्या आक्रमणानंतर महाराजा हरिसिंह यांनी भारताशी सामीलनाम्यावर स्वाक्षरी केली; 1949 मध्ये युद्धविराम रेषेसह लढाई संपली, जी नंतर नियंत्रण रेषा बनली. कलम 370 अंतर्गत राज्याला ऑगस्ट 2019 पर्यंत विशेष घटनात्मक दर्जा होता, तेव्हा संसदेने ही तरतूद निष्प्रभ केली व राज्याची दोन केंद्रशासित प्रदेशांत पुनर्रचना केली. 1989–90 पासूनच्या सशस्त्र दहशतवादात मोठी जीवितहानी झाली आणि बहुतेक काश्मिरी पंडितांना खोऱ्यातून विस्थापित व्हावे लागले. केंद्रशासित प्रदेशाच्या पहिल्या विधानसभा निवडणुका 2024 मध्ये झाल्या."),
        conf="Editorial"),
    timeline([
        ev("shahmir", 1339, L("1339", "1339", "1339"), L("Shah Mir dynasty founded", "शाह मीर वंश की स्थापना", "शाह मीर घराण्याची स्थापना")),
        ev("mughal", 1586, L("1586", "1586", "1586"), L("Mughal annexation of Kashmir", "मुग़लों का कश्मीर पर अधिकार", "मुघलांचे काश्मीरवर आधिपत्य")),
        ev("amritsar", 1846, L("16 March 1846", "16 मार्च 1846", "16 मार्च 1846"), L("Treaty of Amritsar; Gulab Singh becomes Maharaja", "अमृतसर की संधि; गुलाब सिंह महाराजा बने", "अमृतसरचा तह; गुलाबसिंह महाराजा")),
        ev("accession", 1947, L("26 October 1947", "26 अक्टूबर 1947", "26 ऑक्टोबर 1947"), L("Instrument of Accession signed", "विलय पत्र पर हस्ताक्षर", "सामीलनाम्यावर स्वाक्षरी")),
        ev("reorg", 2019, L("31 October 2019", "31 अक्टूबर 2019", "31 ऑक्टोबर 2019"), L("Union Territories of J&K and Ladakh formed", "जम्मू-कश्मीर और लद्दाख केंद्र शासित प्रदेश बने", "जम्मू-काश्मीर व लडाख केंद्रशासित प्रदेशांची निर्मिती")),
        ev("cm2024", 2024, L("16 October 2024", "16 अक्टूबर 2024", "16 ऑक्टोबर 2024"), L("Omar Abdullah sworn in as the UT's first Chief Minister", "उमर अब्दुल्ला ने केंद्र शासित प्रदेश के पहले मुख्यमंत्री के रूप में शपथ ली", "उमर अब्दुल्ला केंद्रशासित प्रदेशाचे पहिले मुख्यमंत्री")),
        ev("rail", 2025, L("6 June 2025", "6 जून 2025", "6 जून 2025"), L("Rail link to the valley through the Chenab bridge opened", "चिनाब पुल से होकर घाटी तक रेल संपर्क खुला", "चिनाब पुलामार्गे खोऱ्यापर्यंत रेल्वे जोडणी खुली")),
    ]),
    lst("heritage", [
        it3("martand", "Martand Sun Temple ruins, Anantnag", "मार्तंड सूर्य मंदिर के भग्नावशेष, अनंतनाग", "मार्तंड सूर्यमंदिराचे भग्नावशेष, अनंतनाग", m=("8th century", "8वीं सदी", "आठवे शतक")),
        it3("burzahom", "Burzahom", "बुर्ज़होम", "बुर्झहोम", m=("Neolithic site", "नवपाषाण स्थल", "नवाश्मयुगीन स्थळ")),
        it3("shalimar", "Shalimar Bagh and Nishat Bagh, Srinagar", "शालीमार बाग़ और निशात बाग़, श्रीनगर", "शालिमार बाग व निशात बाग, श्रीनगर", m=("Mughal gardens", "मुग़ल उद्यान", "मुघल उद्याने")),
        it3("jamia", "Jamia Masjid, Srinagar", "जामिया मस्जिद, श्रीनगर", "जामिया मशीद, श्रीनगर", m=("Wooden pillars, 15th century", "लकड़ी के खंभे, 15वीं सदी", "लाकडी खांब, पंधरावे शतक")),
        it3("raghunath", "Raghunath temple, Jammu", "रघुनाथ मंदिर, जम्मू", "रघुनाथ मंदिर, जम्मू", m=("Dogra era", "डोगरा काल", "डोग्रा काळ")),
        it3("bahu", "Bahu Fort, Jammu", "बाहु क़िला, जम्मू", "बाहू किल्ला, जम्मू", m=("Bawe Wali Mata temple", "बावे वाली माता मंदिर", "बावे वाली माता मंदिर")),
        it3("mubarak", "Mubarak Mandi Palace, Jammu", "मुबारक मंडी महल, जम्मू", "मुबारक मंडी राजवाडा, जम्मू", m=("Dogra palace complex", "डोगरा महल परिसर", "डोग्रा राजवाडा संकुल")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
    gaps("g", [
        (L("Article 370 and the Reorganisation Act — official texts", "अनुच्छेद 370 और पुनर्गठन अधिनियम — आधिकारिक पाठ", "कलम 370 व पुनर्रचना कायदा — अधिकृत मजकूर"), "india-gov", "Gazette notifications of 5–9 August 2019; Supreme Court judgment of 11 December 2023."),
    ]),
])
print("jk mod1 ok")
