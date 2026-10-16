"""Punjab modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-PB"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
pb = read("regions/IN-PB.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Punjab — 'the land of five rivers' — lies in north-western India on the international border with Pakistan, with Jammu and Kashmir to the north, Himachal Pradesh to the north-east, Haryana to the south and Rajasthan to the south-west. Almost all of it is a flat, fertile alluvial plain watered by the Sutlej, Beas and Ravi, with the Shivalik foothills along the north-east. It had 2.77 crore people at the 2011 Census. Chandigarh, a Union Territory, is the shared capital of Punjab and Haryana; Ludhiana, Amritsar, Jalandhar, Patiala, Bathinda and Mohali are the major cities.\n\nThe present State was formed on 1 November 1966, when the Punjab Reorganisation Act created Haryana and transferred hill areas to Himachal Pradesh. Punjabi, written in Gurmukhi, is the official language.",
        "पंजाब — 'पाँच नदियों की भूमि' — उत्तर-पश्चिमी भारत में पाकिस्तान के साथ अंतरराष्ट्रीय सीमा पर स्थित है; इसके उत्तर में जम्मू और कश्मीर, उत्तर-पूर्व में हिमाचल प्रदेश, दक्षिण में हरियाणा और दक्षिण-पश्चिम में राजस्थान है। इसका लगभग पूरा भाग सतलुज, ब्यास और रावी से सिंचित समतल, उपजाऊ जलोढ़ मैदान है, और उत्तर-पूर्व में शिवालिक की तलहटी है। 2011 की जनगणना में इसकी जनसंख्या 2.77 करोड़ थी। केंद्र शासित प्रदेश चंडीगढ़ पंजाब और हरियाणा की साझा राजधानी है; लुधियाना, अमृतसर, जालंधर, पटियाला, बठिंडा और मोहाली प्रमुख शहर हैं।\n\nवर्तमान राज्य 1 नवंबर 1966 को बना, जब पंजाब पुनर्गठन अधिनियम से हरियाणा बना और पहाड़ी क्षेत्र हिमाचल प्रदेश को दिए गए। गुरमुखी में लिखी जाने वाली पंजाबी राजभाषा है।",
        "पंजाब — 'पाच नद्यांची भूमी' — वायव्य भारतात पाकिस्तानच्या आंतरराष्ट्रीय सीमेवर आहे; त्याच्या उत्तरेला जम्मू व काश्मीर, ईशान्येला हिमाचल प्रदेश, दक्षिणेला हरियाणा व नैर्ऋत्येला राजस्थान आहे. त्याचा जवळपास संपूर्ण भाग सतलज, बियास व रावीने भिजलेले सपाट, सुपीक गाळाचे मैदान आहे, आणि ईशान्येला शिवालिकच्या पायथ्याच्या टेकड्या आहेत. 2011 च्या जनगणनेनुसार त्याची लोकसंख्या 2.77 कोटी होती. केंद्रशासित प्रदेश चंदीगड ही पंजाब व हरियाणाची सामायिक राजधानी आहे; लुधियाना, अमृतसर, जालंधर, पटियाळा, भटिंडा व मोहाली ही प्रमुख शहरे आहेत.\n\nसध्याचे राज्य 1 नोव्हेंबर 1966 रोजी निर्माण झाले, जेव्हा पंजाब पुनर्रचना कायद्याने हरियाणा बनला आणि डोंगरी भाग हिमाचल प्रदेशाला दिले गेले. गुरुमुखी लिपीत लिहिली जाणारी पंजाबी ही राजभाषा आहे."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Punjab is the heartland of Sikhism: Guru Nanak's teachings began here, and the Harmandir Sahib (Golden Temple) in Amritsar, whose langar kitchen feeds tens of thousands every day, draws visitors of every faith. The State was the centre of India's Green Revolution and remains a 'food bowl', supplying large quantities of wheat and rice to the national stock. Bhangra and giddha, Punjabi music and films, phulkari embroidery and hearty food such as sarson da saag and makki di roti are known worldwide, carried by a large Punjabi diaspora in Canada, the United Kingdom, the United States and Australia. Punjab also has the highest share of Scheduled Castes of any State, and has given India many soldiers and sportspeople.",
        "पंजाब सिख धर्म का हृदय है: गुरु नानक की शिक्षाएँ यहीं से शुरू हुईं, और अमृतसर का हरमंदिर साहिब (स्वर्ण मंदिर), जिसकी लंगर रसोई हर दिन हज़ारों लोगों को भोजन कराती है, हर आस्था के आगंतुकों को खींचता है। राज्य भारत की हरित क्रांति का केंद्र था और आज भी 'अन्न का कटोरा' है, जो राष्ट्रीय भंडार को बड़ी मात्रा में गेहूँ और चावल देता है। भांगड़ा और गिद्धा, पंजाबी संगीत और फ़िल्में, फुलकारी कढ़ाई और सरसों का साग व मक्की की रोटी जैसे भोजन विश्व भर में प्रसिद्ध हैं, जिन्हें कनाडा, ब्रिटेन, अमेरिका और ऑस्ट्रेलिया में बड़ा पंजाबी प्रवासी समुदाय आगे ले गया है। पंजाब में किसी भी राज्य से अधिक अनुसूचित जातियों का हिस्सा है, और इसने भारत को बहुत से सैनिक और खिलाड़ी दिए हैं।",
        "पंजाब हे शीख धर्माचे हृदय आहे: गुरु नानकांची शिकवण इथूनच सुरू झाली, आणि अमृतसरचे हरमंदिर साहिब (सुवर्ण मंदिर), ज्याचे लंगर स्वयंपाकघर दररोज हजारो लोकांना जेवू घालते, प्रत्येक श्रद्धेच्या पाहुण्यांना आकर्षित करते. राज्य भारताच्या हरितक्रांतीचे केंद्र होते आणि आजही 'अन्नाचे कोठार' आहे, जे राष्ट्रीय साठ्याला मोठ्या प्रमाणावर गहू व तांदूळ पुरवते. भांगडा व गिद्धा, पंजाबी संगीत व चित्रपट, फुलकारी भरतकाम आणि सरसों दा साग व मक्की दी रोटीसारखे पदार्थ जगभर प्रसिद्ध आहेत, जे कॅनडा, ब्रिटन, अमेरिका व ऑस्ट्रेलियातील मोठ्या पंजाबी प्रवासी समुदायाने पुढे नेले आहेत. पंजाबमध्ये कोणत्याही राज्यापेक्षा अनुसूचित जातींचा वाटा अधिक आहे, आणि त्याने भारताला अनेक सैनिक व खेळाडू दिले आहेत."),
        title=L("What makes Punjab unique?", "पंजाब को ख़ास क्या बनाता है?", "पंजाबचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed (present boundaries)", "गठन (वर्तमान सीमाएँ)", "निर्मिती (सध्याच्या सीमा)"), L("1 November 1966 (Punjab Day)", "1 नवंबर 1966 (पंजाब दिवस)", "1 नोव्हेंबर 1966 (पंजाब दिन)")],
           [L("Districts / divisions", "ज़िले / मंडल", "जिल्हे / विभाग"), "23 / 5"],
           [L("Capital", "राजधानी", "राजधानी"), L("Chandigarh (Union Territory, shared with Haryana)", "चंडीगढ़ (केंद्र शासित प्रदेश, हरियाणा के साथ साझा)", "चंदीगड (केंद्रशासित प्रदेश, हरियाणासोबत सामायिक)")],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Punjabi (Gurmukhi)", "पंजाबी (गुरमुखी)", "पंजाबी (गुरुमुखी)")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Punjab and Haryana High Court, Chandigarh", "पंजाब एवं हरियाणा उच्च न्यायालय, चंडीगढ़", "पंजाब व हरियाणा उच्च न्यायालय, चंदीगड")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "PB"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be linked to the State's notifications in review.", "संपादकीय; समीक्षा में राज्य की अधिसूचनाओं से जोड़ा जाएगा।", "संपादकीय; तपासणीत राज्याच्या अधिसूचनांशी जोडले जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Punjab is traditionally divided into three regions by its rivers: Majha, between the Ravi and the Beas, around Amritsar and Gurdaspur; Doaba, between the Beas and the Sutlej, around Jalandhar and Hoshiarpur; and Malwa, the large area south of the Sutlej, around Ludhiana, Patiala and Bathinda. The land slopes gently from the Shivalik foothills (the kandi belt) in the north-east to the semi-arid south-west near Rajasthan. The Sutlej and Beas meet at Harike, and the seasonal Ghaggar crosses the south-east. Little natural forest remains, and nearly all land is farmed.",
        "पंजाब को उसकी नदियाँ पारंपरिक रूप से तीन क्षेत्रों में बाँटती हैं: रावी और ब्यास के बीच अमृतसर और गुरदासपुर के आसपास माझा; ब्यास और सतलुज के बीच जालंधर और होशियारपुर के आसपास दोआबा; और सतलुज के दक्षिण में लुधियाना, पटियाला और बठिंडा के आसपास का बड़ा क्षेत्र मालवा। भूमि उत्तर-पूर्व में शिवालिक की तलहटी (कंडी पट्टी) से राजस्थान के पास अर्ध-शुष्क दक्षिण-पश्चिम की ओर धीरे-धीरे ढलती है। सतलुज और ब्यास हरिके में मिलती हैं, और मौसमी घग्गर दक्षिण-पूर्व से गुज़रती है। प्राकृतिक वन बहुत कम बचे हैं, और लगभग पूरी भूमि पर खेती होती है।",
        "पंजाब पारंपरिकपणे त्याच्या नद्यांमुळे तीन प्रदेशांत विभागला जातो: रावी व बियासदरम्यान अमृतसर व गुरदासपूरभोवतीचा माझा; बियास व सतलजदरम्यान जालंधर व होशियारपूरभोवतीचा दोआबा; आणि सतलजच्या दक्षिणेला लुधियाना, पटियाळा व भटिंडाभोवतीचा मोठा प्रदेश माळवा. जमीन ईशान्येकडील शिवालिकच्या पायथ्यापासून (कंडी पट्टा) राजस्थानजवळील अर्धशुष्क नैर्ऋत्येकडे हळूहळू उतरत जाते. सतलज व बियास हरिके येथे मिळतात, आणि हंगामी घग्गर आग्नेयेकडून वाहते. नैसर्गिक जंगल फारच थोडे उरले आहे, आणि जवळपास सर्व जमिनीवर शेती होते."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), pb["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("pk", "Pakistan (west)", "पाकिस्तान (पश्चिम)", "पाकिस्तान (पश्चिम)"), it3("jk", "Jammu and Kashmir (north)", "जम्मू और कश्मीर (उत्तर)", "जम्मू व काश्मीर (उत्तर)"),
        it3("hp", "Himachal Pradesh (north-east)", "हिमाचल प्रदेश (उत्तर-पूर्व)", "हिमाचल प्रदेश (ईशान्य)"), it3("ch", "Chandigarh (east)", "चंडीगढ़ (पूर्व)", "चंदीगड (पूर्व)"),
        it3("hr", "Haryana (south and south-east)", "हरियाणा (दक्षिण और दक्षिण-पूर्व)", "हरियाणा (दक्षिण व आग्नेय)"), it3("rj", "Rajasthan (south-west)", "राजस्थान (दक्षिण-पश्चिम)", "राजस्थान (नैर्ऋत्य)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("sutlej", "Sutlej", "सतलुज", "सतलज", d=("Enters from Himachal at Nangal; flows past Ropar and Ludhiana to Harike.", "नंगल में हिमाचल से प्रवेश करती है; रोपड़ और लुधियाना से होकर हरिके तक बहती है।", "नांगल येथे हिमाचलमधून प्रवेश; रोपड व लुधियानामार्गे हरिकेपर्यंत वाहते.")),
        it3("beas", "Beas", "ब्यास", "बियास", d=("Separates Majha from Doaba; joins the Sutlej at Harike.", "माझा को दोआबा से अलग करती है; हरिके में सतलुज से मिलती है।", "माझा व दोआबा वेगळे करते; हरिके येथे सतलजला मिळते.")),
        it3("ravi", "Ravi", "रावी", "रावी", d=("Forms part of the border with Pakistan; Ranjit Sagar dam upstream.", "पाकिस्तान के साथ सीमा का हिस्सा; ऊपर रणजीत सागर बाँध।", "पाकिस्तानसोबतच्या सीमेचा भाग; वरच्या बाजूला रणजित सागर धरण.")),
        it3("ghaggar", "Ghaggar", "घग्गर", "घग्गर", d=("Seasonal river in the south-east; floods in heavy monsoons.", "दक्षिण-पूर्व की मौसमी नदी; भारी मानसून में बाढ़।", "आग्नेयेकडील हंगामी नदी; मुसळधार पावसात पूर.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point — official elevation", "सर्वोच्च बिंदु — आधिकारिक ऊँचाई", "सर्वोच्च शिखर — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Length of the international border", "अंतरराष्ट्रीय सीमा की लंबाई", "आंतरराष्ट्रीय सीमेची लांबी"), "india-gov", "Ministry of Home Affairs (Border Management)."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Punjab has a continental climate with sharp contrasts. Summers (April–June) are very hot and dry, with dust storms and loo winds, especially in the south-west. The monsoon (July–September) brings most of the rain, heavier near the Shivaliks; floods occur when heavy rain in the hills swells the rivers. Winters (December–February) are cold, with frost and dense fog across the plains, and western disturbances bring winter rain that helps the wheat crop.",
        "पंजाब की जलवायु महाद्वीपीय है, जिसमें तीखे अंतर हैं। गर्मियाँ (अप्रैल–जून) बहुत गर्म और सूखी होती हैं, आँधियों और लू के साथ, विशेषकर दक्षिण-पश्चिम में। मानसून (जुलाई–सितंबर) अधिकांश वर्षा लाता है, जो शिवालिक के पास अधिक होती है; पहाड़ों में भारी वर्षा से नदियाँ उफनने पर बाढ़ आती है। सर्दियाँ (दिसंबर–फ़रवरी) ठंडी होती हैं, मैदानों में पाला और घना कोहरा रहता है, और पश्चिमी विक्षोभ सर्दियों की बारिश लाते हैं जो गेहूँ की फ़सल के लिए सहायक है।",
        "पंजाबचे हवामान खंडीय असून त्यात तीव्र विरोधाभास आहेत. उन्हाळा (एप्रिल–जून) अतिशय उष्ण व कोरडा असतो, धुळीची वादळे व लू वाऱ्यांसह, विशेषतः नैर्ऋत्येत. मान्सून (जुलै–सप्टेंबर) बहुतेक पाऊस आणतो, शिवालिकजवळ अधिक; डोंगरांत मुसळधार पावसाने नद्या फुगल्यावर पूर येतात. हिवाळा (डिसेंबर–फेब्रुवारी) थंड असतो, मैदानांत दव गोठते व दाट धुके असते, आणि पश्चिमी विक्षोभ हिवाळी पाऊस आणतात जो गव्हाच्या पिकाला उपयुक्त ठरतो."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Amritsar", "अमृतसर", "अमृतसर"), "lat": 31.6340, "lon": 74.8723},
        {"name": L("Ludhiana", "लुधियाना", "लुधियाना"), "lat": 30.9010, "lon": 75.8573},
        {"name": L("Patiala", "पटियाला", "पटियाळा"), "lat": 30.3398, "lon": 76.3869},
        {"name": L("Bathinda", "बठिंडा", "भटिंडा"), "lat": 30.2110, "lon": 74.9455},
    ]},
    lst("best", [
        it3("winter", "October to March", "अक्टूबर से मार्च", "ऑक्टोबर ते मार्च", d=("Pleasant days; Lohri in January, Hola Mohalla at Anandpur Sahib in March; fog can delay travel.", "सुहावने दिन; जनवरी में लोहड़ी, मार्च में आनंदपुर साहिब में होला मोहल्ला; कोहरे से यात्रा में देरी हो सकती है।", "आल्हाददायक दिवस; जानेवारीत लोहडी, मार्चमध्ये आनंदपूर साहिब येथे होला मोहल्ला; धुक्यामुळे प्रवासाला उशीर होऊ शकतो.")),
        it3("spring", "April", "अप्रैल", "एप्रिल", d=("Baisakhi harvest festival; golden wheat fields.", "बैसाखी फ़सल उत्सव; सुनहरे गेहूँ के खेत।", "बैसाखी सुगीचा सण; सोनेरी गव्हाची शेते.")),
        it3("summer", "May to June", "मई से जून", "मे ते जून", d=("Very hot; visit Amritsar early morning or late evening.", "बहुत गर्म; अमृतसर सुबह जल्दी या देर शाम जाएँ।", "अतिशय उष्ण; अमृतसरला पहाटे किंवा उशिरा संध्याकाळी भेट द्या.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (Punjab sub-division)", "सामान्य वार्षिक वर्षा (पंजाब उप-मंडल)", "सरासरी वार्षिक पाऊस (पंजाब उपविभाग)"), "imd", "IMD rainfall statistics."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Punjab is warm, loud and hospitable. Every gurdwara runs a free langar where anyone can sit on the floor and eat, and the evening palki ceremony at the Golden Temple and the flag-lowering at the Attari–Wagah border draw huge crowds. Villages are surrounded by green wheat in winter and paddy in summer, tubewells hum in the fields, and tractors carry music as much as crops. Weddings are famous for bhangra and dhol, roadside dhabas serve parathas with white butter and tall glasses of lassi, and almost every family has a relative abroad — in Brampton, Southall or Melbourne — whose visits are part of village life.",
        "पंजाब गर्मजोशी भरा, मुखर और मेहमाननवाज़ है। हर गुरुद्वारे में मुफ़्त लंगर चलता है, जहाँ कोई भी ज़मीन पर बैठकर खा सकता है, और स्वर्ण मंदिर की शाम की पालकी सेवा और अटारी–वाघा सीमा पर ध्वज उतारने का समारोह भारी भीड़ खींचते हैं। गाँव सर्दियों में हरे गेहूँ और गर्मियों में धान से घिरे रहते हैं, खेतों में ट्यूबवेल गूँजते हैं, और ट्रैक्टर फ़सल जितना ही संगीत भी ढोते हैं। शादियाँ भांगड़ा और ढोल के लिए प्रसिद्ध हैं, सड़क किनारे के ढाबे सफ़ेद मक्खन के साथ पराठे और लस्सी के बड़े गिलास परोसते हैं, और लगभग हर परिवार का कोई रिश्तेदार विदेश में है — ब्रैम्पटन, साउथहॉल या मेलबर्न में — जिनका आना गाँव के जीवन का हिस्सा है।",
        "पंजाब उबदार, मोकळा व पाहुणचार करणारा आहे. प्रत्येक गुरुद्वाऱ्यात मोफत लंगर चालतो, जिथे कोणीही जमिनीवर बसून जेवू शकतो, आणि सुवर्ण मंदिराचा संध्याकाळचा पालखी सोहळा व अटारी–वाघा सीमेवरील ध्वज उतरवण्याचा समारंभ प्रचंड गर्दी खेचतो. गावे हिवाळ्यात हिरव्या गव्हाने व उन्हाळ्यात भाताने वेढलेली असतात, शेतांत कूपनलिका गुणगुणतात, आणि ट्रॅक्टर पिकांइतकेच संगीतही वाहून नेतात. लग्ने भांगडा व ढोलासाठी प्रसिद्ध आहेत, रस्त्याकडेचे ढाबे पांढऱ्या लोण्यासह पराठे व लस्सीचे मोठे ग्लास देतात, आणि जवळपास प्रत्येक कुटुंबाचा कोणीतरी नातेवाईक परदेशात — ब्रॅम्प्टन, साउथहॉल किंवा मेलबर्नमध्ये — असतो, ज्यांचे येणे हा गावजीवनाचा भाग आहे."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Punjab had 2.77 crore people at the 2011 Census, with about 551 people per km². The sex ratio was 895 women per 1,000 men, among the lowest in India, but the child sex ratio, which had fallen to 798 in 2001, recovered to 846 in 2011. Literacy was 75.8%, above the national 73.0%. Scheduled Castes made up 31.9% of the population — the highest share of any State — and Punjab has no notified Scheduled Tribes.\n\nPunjabi is spoken by the great majority, in the Majhi, Doabi, Malwai and Puadhi dialects. Hindi is widely understood, especially in towns.",
        "2011 की जनगणना में पंजाब की जनसंख्या 2.77 करोड़ थी, और प्रति वर्ग किमी लगभग 551 लोग। लिंगानुपात प्रति 1,000 पुरुषों पर 895 महिलाएँ था, जो भारत में सबसे कम में है, लेकिन 2001 में 798 तक गिरा शिशु लिंगानुपात 2011 में सुधरकर 846 हुआ। साक्षरता 75.8% थी, जो राष्ट्रीय 73.0% से अधिक है। अनुसूचित जातियाँ जनसंख्या का 31.9% थीं — किसी भी राज्य में सबसे अधिक हिस्सा — और पंजाब में कोई अधिसूचित अनुसूचित जनजाति नहीं है।\n\nअधिकांश लोग माझी, दोआबी, मलवई और पुआधी बोलियों में पंजाबी बोलते हैं। हिंदी व्यापक रूप से समझी जाती है, विशेषकर शहरों में।",
        "2011 च्या जनगणनेनुसार पंजाबची लोकसंख्या 2.77 कोटी होती, आणि प्रति चौ.किमी सुमारे 551 लोक. दर 1,000 पुरुषांमागे 895 स्त्रिया होत्या — भारतातील सर्वांत कमींपैकी — पण 2001 मध्ये 798 पर्यंत घसरलेले बाल लिंग गुणोत्तर 2011 मध्ये 846 पर्यंत सुधारले. साक्षरता 75.8% होती, राष्ट्रीय 73.0% पेक्षा अधिक. अनुसूचित जाती लोकसंख्येच्या 31.9% होत्या — कोणत्याही राज्यातील सर्वाधिक वाटा — आणि पंजाबमध्ये एकही अधिसूचित अनुसूचित जमात नाही.\n\nबहुसंख्य लोक माझी, दोआबी, माळवी व पुआधी बोलींत पंजाबी बोलतात. हिंदी मोठ्या प्रमाणावर समजली जाते, विशेषतः शहरांत."),
        sources=["census", "es-india", "dl-planning"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), pb["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), pb["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(876, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), pb["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(798, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), pb["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"],
             previous=dp(69.7, "%", "2001", "census", "es-india", ESI_LIT)),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), pb["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(31.9, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 88.60 lakh people — the highest share among States."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("pa", "Punjabi", "पंजाबी", "पंजाबी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("majhi", "Majhi", "माझी", "माझी", m=("Dialect", "बोली", "बोली")), it3("doabi", "Doabi", "दोआबी", "दोआबी", m=("Dialect", "बोली", "बोली")),
        it3("malwai", "Malwai", "मलवई", "माळवी", m=("Dialect", "बोली", "बोली")), it3("puadhi", "Puadhi", "पुआधी", "पुआधी", m=("Dialect", "बोली", "बोली")),
        it3("hi", "Hindi", "हिंदी", "हिंदी"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Final Population Totals for Punjab."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Punjab's plains were part of the Harappan world — Ropar and Sanghol have important sites — and the setting of much of early Vedic India. Later the region was ruled by the Mauryas, Kushans, Guptas and, from the 11th century, a series of Turkic, Afghan and Mughal powers. Guru Nanak (1469–1539) founded the Sikh faith, and his nine successors built it into a community; Guru Arjan compiled the Adi Granth and completed the Harmandir Sahib, and Guru Gobind Singh created the Khalsa at Anandpur Sahib in 1699. After Banda Singh Bahadur's campaigns and the period of the misls, Maharaja Ranjit Singh united Punjab into a powerful Sikh kingdom ruled from Lahore (1799–1839).\n\nThe British annexed Punjab in 1849 after two Anglo-Sikh wars, built vast canal colonies, and recruited heavily for the army. The Jallianwala Bagh massacre at Amritsar on 13 April 1919 became a turning point in the freedom struggle, and Bhagat Singh, Udham Singh, Kartar Singh Sarabha and Lala Lajpat Rai are among Punjab's heroes. Partition in 1947 divided Punjab between India and Pakistan amid mass migration and violence. PEPSU was merged in 1956, and the 1966 reorganisation gave the State its present shape. The Green Revolution of the late 1960s transformed its farms, and the State went through a period of militancy in the 1980s and early 1990s.",
        "पंजाब के मैदान हड़प्पा सभ्यता का हिस्सा थे — रोपड़ और संघोल में महत्त्वपूर्ण स्थल हैं — और प्रारंभिक वैदिक भारत के बड़े भाग की पृष्ठभूमि रहे। बाद में इस क्षेत्र पर मौर्य, कुषाण, गुप्त और 11वीं सदी से तुर्क, अफ़ग़ान और मुग़ल शक्तियों ने शासन किया। गुरु नानक (1469–1539) ने सिख धर्म की नींव रखी, और उनके नौ उत्तराधिकारियों ने इसे एक समुदाय के रूप में गढ़ा; गुरु अर्जन ने आदि ग्रंथ का संकलन किया और हरमंदिर साहिब पूरा किया, और गुरु गोबिंद सिंह ने 1699 में आनंदपुर साहिब में खालसा की स्थापना की। बंदा सिंह बहादुर के अभियानों और मिसलों के दौर के बाद महाराजा रणजीत सिंह ने पंजाब को लाहौर से शासित एक शक्तिशाली सिख राज्य (1799–1839) में एकजुट किया।\n\nदो आंग्ल-सिख युद्धों के बाद 1849 में अंग्रेज़ों ने पंजाब का विलय किया, विशाल नहर बस्तियाँ बसाईं और सेना के लिए बड़े पैमाने पर भर्ती की। 13 अप्रैल 1919 को अमृतसर का जलियाँवाला बाग़ हत्याकांड स्वतंत्रता संग्राम का निर्णायक मोड़ बना, और भगत सिंह, ऊधम सिंह, करतार सिंह सराभा और लाला लाजपत राय पंजाब के नायकों में हैं। 1947 के विभाजन ने बड़े पैमाने पर पलायन और हिंसा के बीच पंजाब को भारत और पाकिस्तान में बाँट दिया। 1956 में पेप्सू का विलय हुआ, और 1966 के पुनर्गठन ने राज्य को वर्तमान रूप दिया। 1960 के दशक के अंत की हरित क्रांति ने इसकी खेती बदल दी, और राज्य 1980 के दशक और 1990 के दशक की शुरुआत में उग्रवाद के दौर से गुज़रा।",
        "पंजाबची मैदाने हडप्पा संस्कृतीचा भाग होती — रोपड व संघोल येथे महत्त्वाची स्थळे आहेत — आणि प्रारंभीच्या वैदिक भारताच्या मोठ्या भागाची पार्श्वभूमी होती. नंतर या प्रदेशावर मौर्य, कुषाण, गुप्त आणि अकराव्या शतकापासून तुर्की, अफगाण व मुघल सत्तांनी राज्य केले. गुरु नानक (1469–1539) यांनी शीख धर्माची स्थापना केली, आणि त्यांच्या नऊ उत्तराधिकाऱ्यांनी त्याला समुदायाचे रूप दिले; गुरु अर्जन यांनी आदिग्रंथाचे संकलन केले व हरमंदिर साहिब पूर्ण केले, आणि गुरु गोविंदसिंहांनी 1699 मध्ये आनंदपूर साहिब येथे खालशाची स्थापना केली. बंदासिंह बहादूर यांच्या मोहिमा व मिसलींच्या काळानंतर महाराजा रणजितसिंहांनी पंजाबला लाहोरहून चालणाऱ्या बलाढ्य शीख राज्यात (1799–1839) एकत्र केले.\n\nदोन इंग्रज-शीख युद्धांनंतर 1849 मध्ये इंग्रजांनी पंजाब खालसा केला, प्रचंड कालवा वसाहती उभारल्या व सैन्यासाठी मोठी भरती केली. 13 एप्रिल 1919 रोजीचे अमृतसरमधील जालियनवाला बाग हत्याकांड स्वातंत्र्यलढ्यातील निर्णायक वळण ठरले, आणि भगतसिंह, उधमसिंह, कर्तारसिंह सराभा व लाला लजपतराय हे पंजाबच्या नायकांपैकी आहेत. 1947 च्या फाळणीने प्रचंड स्थलांतर व हिंसाचारात पंजाबची भारत व पाकिस्तानात विभागणी केली. 1956 मध्ये पेप्सूचे विलीनीकरण झाले, आणि 1966 च्या पुनर्रचनेने राज्याला सध्याचे स्वरूप दिले. 1960 च्या दशकाच्या अखेरीच्या हरितक्रांतीने त्याची शेती बदलली, आणि राज्य 1980 च्या दशकात व 1990 च्या दशकाच्या सुरुवातीला दहशतवादाच्या काळातून गेले."),
        conf="Editorial"),
    timeline([
        ev("nanak", 1469, L("1469", "1469", "1469"), L("Birth of Guru Nanak", "गुरु नानक का जन्म", "गुरु नानकांचा जन्म")),
        ev("granth", 1604, L("1604", "1604", "1604"), L("Adi Granth installed at the Harmandir Sahib", "हरमंदिर साहिब में आदि ग्रंथ की स्थापना", "हरमंदिर साहिबमध्ये आदिग्रंथाची स्थापना")),
        ev("khalsa", 1699, L("1699", "1699", "1699"), L("Khalsa created at Anandpur Sahib", "आनंदपुर साहिब में खालसा की स्थापना", "आनंदपूर साहिब येथे खालशाची स्थापना")),
        ev("ranjit", 1799, L("1799", "1799", "1799"), L("Ranjit Singh takes Lahore", "रणजीत सिंह ने लाहौर लिया", "रणजितसिंहांनी लाहोर घेतले")),
        ev("annex", 1849, L("1849", "1849", "1849"), L("British annexation of Punjab", "पंजाब का ब्रिटिश विलय", "इंग्रजांनी पंजाब खालसा केला")),
        ev("jallianwala", 1919, L("13 April 1919", "13 अप्रैल 1919", "13 एप्रिल 1919"), L("Jallianwala Bagh massacre", "जलियाँवाला बाग़ हत्याकांड", "जालियनवाला बाग हत्याकांड")),
        ev("partition", 1947, L("August 1947", "अगस्त 1947", "ऑगस्ट 1947"), L("Partition of Punjab", "पंजाब का विभाजन", "पंजाबची फाळणी")),
        ev("reorg", 1966, L("1 November 1966", "1 नवंबर 1966", "1 नोव्हेंबर 1966"), L("Present State formed", "वर्तमान राज्य बना", "सध्याचे राज्य निर्माण")),
        ev("cm2022", 2022, L("16 March 2022", "16 मार्च 2022", "16 मार्च 2022"), L("Bhagwant Mann sworn in as Chief Minister", "भगवंत मान ने मुख्यमंत्री पद की शपथ ली", "भगवंत मान यांचा मुख्यमंत्रिपदाचा शपथविधी")),
    ]),
    lst("heritage", [
        it3("golden", "Harmandir Sahib (Golden Temple), Amritsar", "हरमंदिर साहिब (स्वर्ण मंदिर), अमृतसर", "हरमंदिर साहिब (सुवर्ण मंदिर), अमृतसर", m=("Sikh shrine", "सिख तीर्थ", "शीख तीर्थ")),
        it3("jallianwala", "Jallianwala Bagh, Amritsar", "जलियाँवाला बाग़, अमृतसर", "जालियनवाला बाग, अमृतसर", m=("National memorial", "राष्ट्रीय स्मारक", "राष्ट्रीय स्मारक")),
        it3("anandpur", "Takht Sri Keshgarh Sahib, Anandpur Sahib", "तख़्त श्री केसगढ़ साहिब, आनंदपुर साहिब", "तख्त श्री केसगड साहिब, आनंदपूर साहिब", m=("Birthplace of the Khalsa", "खालसा की जन्मभूमि", "खालशाचे जन्मस्थान")),
        it3("qila", "Qila Mubarak and Sheesh Mahal, Patiala", "क़िला मुबारक और शीश महल, पटियाला", "किला मुबारक व शीश महल, पटियाळा", m=("Patiala state", "पटियाला रियासत", "पटियाळा संस्थान")),
        it3("gobindgarh", "Gobindgarh Fort, Amritsar", "गोबिंदगढ़ क़िला, अमृतसर", "गोविंदगड किल्ला, अमृतसर", m=("Ranjit Singh era", "रणजीत सिंह काल", "रणजितसिंह काळ")),
        it3("sanghol", "Sanghol", "संघोल", "संघोल", m=("Harappan and Kushan site", "हड़प्पा और कुषाण स्थल", "हडप्पा व कुषाण स्थळ")),
        it3("rauza", "Rauza Sharif, Sirhind", "रौज़ा शरीफ़, सरहिंद", "रौजा शरीफ, सरहिंद", m=("Sufi shrine", "सूफ़ी दरगाह", "सूफी दर्गा")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("pb mod1 ok")
