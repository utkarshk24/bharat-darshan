"""Tripura modules A–F."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-TR"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
tr = read("regions/IN-TR.json")["metrics"]; ind = read("india.json")["metrics"]

module(R, "overview", [
    prose("intro", L(
        "Tripura is a small State in north-eastern India, surrounded on three sides — north, west and south — by Bangladesh, with Assam and Mizoram to the east. Low hill ranges running north to south alternate with broad valleys and plains where most people live and farm. Agartala, close to the Bangladesh border, is the capital.\n\nFor centuries Tripura was a princely kingdom ruled by the Manikya dynasty. It merged with India on 15 October 1949, became a Union Territory in 1956 and a full State on 21 January 1972. Its people are a mix of Bengali-speaking communities and nineteen Scheduled Tribes, of whom the Tripuri are the largest group. It is known for its palaces and temples, bamboo and cane crafts, the Queen pineapple and rubber plantations.",
        "त्रिपुरा उत्तर-पूर्वी भारत का एक छोटा राज्य है, जो तीन ओर — उत्तर, पश्चिम और दक्षिण — से बांग्लादेश से घिरा है, और पूर्व में असम और मिज़ोरम हैं। उत्तर से दक्षिण चलने वाली नीची पहाड़ी शृंखलाएँ चौड़ी घाटियों और मैदानों के साथ बारी-बारी आती हैं, जहाँ अधिकांश लोग रहते और खेती करते हैं। बांग्लादेश सीमा के पास अगरतला राजधानी है।\n\nसदियों तक त्रिपुरा माणिक्य वंश द्वारा शासित एक रियासत थी। यह 15 अक्टूबर 1949 को भारत में विलीन हुई, 1956 में केंद्र शासित प्रदेश और 21 जनवरी 1972 को पूर्ण राज्य बनी। इसके लोग बांग्ला भाषी समुदायों और उन्नीस अनुसूचित जनजातियों का मेल हैं, जिनमें त्रिपुरी सबसे बड़ा समूह है। यह अपने महलों और मंदिरों, बाँस और बेंत शिल्प, क्वीन अनानास और रबर बाग़ानों के लिए जाना जाता है।",
        "त्रिपुरा हे ईशान्य भारतातील लहान राज्य आहे, जे तीन बाजूंनी — उत्तर, पश्चिम व दक्षिण — बांगलादेशाने वेढलेले आहे, आणि पूर्वेला आसाम व मिझोराम आहेत. उत्तर-दक्षिण धावणाऱ्या कमी उंचीच्या टेकड्यांच्या रांगा रुंद खोरी व मैदानांसोबत आलटून-पालटून येतात, जिथे बहुतेक लोक राहतात व शेती करतात. बांगलादेश सीमेजवळील आगरतळा ही राजधानी आहे.\n\nशतकानुशतके त्रिपुरा माणिक्य घराण्याचे संस्थान होते. ते 15 ऑक्टोबर 1949 रोजी भारतात विलीन झाले, 1956 मध्ये केंद्रशासित प्रदेश व 21 जानेवारी 1972 रोजी पूर्ण राज्य झाले. तेथील लोक बंगाली भाषक समुदाय व एकोणीस अनुसूचित जमातींचा मेळ आहेत, ज्यांत त्रिपुरी हा सर्वांत मोठा गट आहे. ते राजवाडे व मंदिरे, बांबू व वेत हस्तकला, क्वीन अननस व रबराच्या मळ्यांसाठी ओळखले जाते."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Ujjayanta Palace in Agartala, built by the Manikya kings in 1901, and Neermahal, a water palace in Rudrasagar lake, recall the royal past. Unakoti has huge rock-cut faces of Shiva and other deities carved into a hillside, and the Tripura Sundari temple at Udaipur is one of the Shakti peethas. Literacy rose to 87.2% at the 2011 Census. The Tripura Tribal Areas Autonomous District Council governs about two-thirds of the State's area under the Sixth Schedule.",
        "अगरतला का उज्जयंत महल, जिसे माणिक्य राजाओं ने 1901 में बनवाया, और रुद्रसागर झील में जल महल नीरमहल, राजसी अतीत की याद दिलाते हैं। उनाकोटी में एक पहाड़ी पर शिव और अन्य देवताओं के विशाल शैल-उत्कीर्ण चेहरे हैं, और उदयपुर का त्रिपुरा सुंदरी मंदिर शक्तिपीठों में से एक है। 2011 की जनगणना में साक्षरता बढ़कर 87.2% हो गई। त्रिपुरा जनजातीय क्षेत्र स्वायत्त ज़िला परिषद छठी अनुसूची के तहत राज्य के लगभग दो-तिहाई क्षेत्र का शासन करती है।",
        "आगरतळ्यातील उज्जयंत राजवाडा, जो माणिक्य राजांनी 1901 मध्ये बांधला, आणि रुद्रसागर सरोवरातील जलमहाल नीरमहाल राजेशाही भूतकाळाची आठवण करून देतात. उनाकोटी येथे एका टेकडीवर शिव व इतर देवतांचे प्रचंड खडकात कोरलेले चेहरे आहेत, आणि उदयपूरचे त्रिपुरा सुंदरी मंदिर शक्तिपीठांपैकी एक आहे. 2011 च्या जनगणनेत साक्षरता वाढून 87.2% झाली. त्रिपुरा आदिवासी क्षेत्र स्वायत्त जिल्हा परिषद सहाव्या अनुसूचीखाली राज्याच्या सुमारे दोन-तृतीयांश क्षेत्राचा कारभार पाहते."),
        title=L("What makes Tripura unique?", "त्रिपुरा को ख़ास क्या बनाता है?", "त्रिपुराचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Statehood", "राज्य का दर्जा", "राज्याचा दर्जा"), L("21 January 1972", "21 जनवरी 1972", "21 जानेवारी 1972")],
           [L("Districts", "ज़िले", "जिल्हे"), L("8 (Dhalai, Gomati, Khowai, North Tripura, Sepahijala, South Tripura, Unakoti, West Tripura)", "8 (धलाई, गोमती, खोवाई, उत्तर त्रिपुरा, सिपाहीजला, दक्षिण त्रिपुरा, उनाकोटी, पश्चिम त्रिपुरा)", "8 (धलाई, गोमती, खोवाई, उत्तर त्रिपुरा, सिपाहीजला, दक्षिण त्रिपुरा, उनाकोटी, पश्चिम त्रिपुरा)")],
           [L("Capital", "राजधानी", "राजधानी"), L("Agartala", "अगरतला", "आगरतळा")],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Bengali, Kokborok and English", "बांग्ला, कोकबोरोक और अंग्रेज़ी", "बंगाली, कोकबोरोक व इंग्रजी")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("High Court of Tripura, Agartala (since 2013)", "त्रिपुरा उच्च न्यायालय, अगरतला (2013 से)", "त्रिपुरा उच्च न्यायालय, आगरतळा (2013 पासून)")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "TR"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None),
])

module(R, "geography", [
    prose("p1", L(
        "Six main hill ranges — Jampui, Sakhan, Longtharai, Atharamura, Baramura and Deotamura — run north to south, rising to about 900 m at Betlingchhip in the Jampui hills on the Mizoram border. Between them lie valleys drained by the Gomati, Khowai, Haora, Manu, Dhalai and Juri rivers, most of which flow west into Bangladesh. The Gomati, dammed at Dumbur, feeds a large reservoir. Much of the land is covered by forest, bamboo and rubber plantations.",
        "छह मुख्य पहाड़ी शृंखलाएँ — जामपुई, साखन, लोंगथराई, अठारमुड़ा, बड़मुड़ा और देवतामुड़ा — उत्तर से दक्षिण चलती हैं, जो मिज़ोरम सीमा पर जामपुई पहाड़ियों में बेटलिंगछिप पर लगभग 900 मीटर तक उठती हैं। इनके बीच गोमती, खोवाई, हावड़ा, मनु, धलाई और जूरी नदियों की घाटियाँ हैं, जिनमें से अधिकांश पश्चिम में बांग्लादेश की ओर बहती हैं। डुम्बुर में बाँधी गई गोमती एक बड़ा जलाशय बनाती है। भूमि का बड़ा भाग वन, बाँस और रबर बाग़ानों से ढका है।",
        "सहा मुख्य डोंगररांगा — जामपुई, साखन, लोंगथराई, अठारमुडा, बडमुडा व देवतामुडा — उत्तर-दक्षिण धावतात, ज्या मिझोराम सीमेवरील जामपुई टेकड्यांत बेटलिंगछिप येथे सुमारे 900 मीटरपर्यंत उंचावतात. त्यांच्यामध्ये गोमती, खोवाई, हावडा, मनू, धलाई व जुरी नद्यांची खोरी आहेत, ज्यांतील बहुतेक पश्चिमेला बांगलादेशकडे वाहतात. डुम्बुर येथे बांधलेली गोमती मोठा जलाशय तयार करते. जमिनीचा बराचसा भाग जंगल, बांबू व रबराच्या मळ्यांनी व्यापलेला आहे."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), tr["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("bd", "Bangladesh (north, west and south)", "बांग्लादेश (उत्तर, पश्चिम और दक्षिण)", "बांगलादेश (उत्तर, पश्चिम व दक्षिण)"),
        it3("as", "Assam (north-east)", "असम (उत्तर-पूर्व)", "आसाम (ईशान्य)"), it3("mz", "Mizoram (east)", "मिज़ोरम (पूर्व)", "मिझोराम (पूर्व)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("gomati", "Gomati", "गोमती", "गोमती", d=("Dammed at Dumbur; flows west past Udaipur.", "डुम्बुर में बाँधी गई; उदयपुर से पश्चिम बहती है।", "डुम्बुर येथे धरण; उदयपूरवरून पश्चिमेला वाहते.")),
        it3("haora", "Haora", "हावड़ा", "हावडा", d=("Flows through Agartala into Bangladesh.", "अगरतला से होकर बांग्लादेश जाती है।", "आगरतळ्यातून बांगलादेशात जाते.")),
        it3("manu", "Manu", "मनु", "मनू", d=("Drains the north.", "उत्तरी भाग का जल बहाती है।", "उत्तरेकडील भागाचे पाणी वाहते.")),
        it3("khowai", "Khowai", "खोवाई", "खोवाई", d=("Flows north-west into Bangladesh.", "उत्तर-पश्चिम में बांग्लादेश जाती है।", "वायव्येला बांगलादेशात जाते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [(L("Length of the Bangladesh border", "बांग्लादेश सीमा की लंबाई", "बांगलादेश सीमेची लांबी"), "india-gov", "Ministry of Home Affairs (Department of Border Management).")]),
])

module(R, "climate", [
    prose("p1", L(
        "Tripura has a warm, humid tropical climate. Summers from March to May are hot, with thunderstorms; the monsoon from June to September brings heavy rain and floods in low-lying areas; and winters from November to February are mild and pleasant.",
        "त्रिपुरा की जलवायु गर्म, आर्द्र उष्णकटिबंधीय है। मार्च से मई तक गर्मियाँ गर्म होती हैं, गरज के साथ तूफ़ानों के साथ; जून से सितंबर तक मानसून भारी वर्षा और निचले क्षेत्रों में बाढ़ लाता है; और नवंबर से फ़रवरी तक सर्दियाँ सौम्य और सुहावनी होती हैं।",
        "त्रिपुराचे हवामान उष्ण, दमट उष्णकटिबंधीय आहे. मार्च ते मे उन्हाळा उष्ण असतो, वादळी पावसासह; जून ते सप्टेंबर मान्सून मुसळधार पाऊस व सखल भागांत पूर आणतो; आणि नोव्हेंबर ते फेब्रुवारी हिवाळा सौम्य व सुखद असतो."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Agartala", "अगरतला", "आगरतळा"), "lat": 23.8315, "lon": 91.2868},
        {"name": L("Udaipur", "उदयपुर", "उदयपूर"), "lat": 23.5333, "lon": 91.4833},
        {"name": L("Dharmanagar", "धर्मनगर", "धर्मनगर"), "lat": 24.3667, "lon": 92.1667},
    ]},
    lst("best", [it3("winter", "October to March", "अक्टूबर से मार्च", "ऑक्टोबर ते मार्च", d=("Pleasant weather; Durga Puja and Diwali at Tripura Sundari.", "सुहावना मौसम; दुर्गा पूजा और त्रिपुरा सुंदरी में दीवाली।", "सुखद हवामान; दुर्गापूजा व त्रिपुरा सुंदरी येथे दिवाळी."))],
        title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [(L("Normal annual rainfall", "सामान्य वार्षिक वर्षा", "सरासरी वार्षिक पाऊस"), "imd", "IMD climatological normals for Agartala.")]),
])

module(R, "vibe", [
    prose("p1", L(
        "Agartala is an easy-going city of ponds, palaces and markets, with a strong Bengali cultural life — adda over tea, Durga Puja pandals and Rabindra Sangeet — and close links to Bangladesh, whose border is a few kilometres away. In the hills, tribal villages keep their own rhythms of jhum farming, weaving and festivals.",
        "अगरतला तालाबों, महलों और बाज़ारों का एक सहज शहर है, जहाँ गहरा बंगाली सांस्कृतिक जीवन है — चाय पर अड्डा, दुर्गा पूजा पंडाल और रवींद्र संगीत — और बांग्लादेश से निकट संबंध हैं, जिसकी सीमा कुछ किलोमीटर दूर है। पहाड़ियों में जनजातीय गाँव झूम खेती, बुनाई और त्योहारों की अपनी लय बनाए रखते हैं।",
        "आगरतळा तलाव, राजवाडे व बाजारांचे शांत शहर आहे, जिथे सशक्त बंगाली सांस्कृतिक जीवन आहे — चहावर अड्डा, दुर्गापूजा मंडप व रवींद्रसंगीत — आणि बांगलादेशशी जवळचे नाते आहे, ज्याची सीमा काही किलोमीटरवर आहे. डोंगरांत आदिवासी गावे झूम शेती, विणकाम व सणांची स्वतःची लय जपतात."),
        conf="Editorial"),
])

module(R, "people", [
    prose("p1", L(
        "Tripura had 36.7 lakh people at the 2011 Census, about 350 per km². The sex ratio was 960 women per 1,000 men, up from 948 in 2001, and literacy 87.2%. Scheduled Tribes made up 31.8% of the population and Scheduled Castes 17.8%. Bengali-speaking people, many of whose families came from present-day Bangladesh before and after Partition, form the majority; the tribes include the Tripuri, Reang (Bru), Jamatia, Chakma, Halam, Noatia, Mog and others. Bengali and Kokborok, the language of the Tripuri, are the main languages.",
        "2011 की जनगणना में त्रिपुरा की जनसंख्या 36.7 लाख थी, प्रति वर्ग किमी लगभग 350। लिंगानुपात प्रति 1,000 पुरुषों पर 960 महिलाएँ था, जो 2001 के 948 से अधिक है, और साक्षरता 87.2%। अनुसूचित जनजातियाँ जनसंख्या का 31.8% और अनुसूचित जातियाँ 17.8% थीं। बांग्ला भाषी लोग, जिनमें से बहुतों के परिवार विभाजन से पहले और बाद आज के बांग्लादेश से आए, बहुमत हैं; जनजातियों में त्रिपुरी, रियांग (ब्रू), जमातिया, चकमा, हलाम, नोआतिया, मोग और अन्य शामिल हैं। बांग्ला और त्रिपुरी लोगों की भाषा कोकबोरोक मुख्य भाषाएँ हैं।",
        "2011 च्या जनगणनेनुसार त्रिपुराची लोकसंख्या 36.7 लाख होती, प्रति चौ.किमी सुमारे 350. दर 1,000 पुरुषांमागे 960 स्त्रिया होत्या, 2001 मधील 948 वरून वाढ, आणि साक्षरता 87.2%. अनुसूचित जमाती लोकसंख्येच्या 31.8% व अनुसूचित जाती 17.8% होत्या. बंगाली भाषक लोक, ज्यांच्यापैकी अनेकांची कुटुंबे फाळणीपूर्वी व नंतर आजच्या बांगलादेशातून आली, बहुसंख्य आहेत; जमातींत त्रिपुरी, रियांग (ब्रू), जमातिया, चकमा, हलाम, नोआतिया, मोग व इतर आहेत. बंगाली व त्रिपुरी लोकांची भाषा कोकबोरोक या मुख्य भाषा आहेत."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), tr["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), tr["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"], previous=dp(948, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), tr["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(966, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), tr["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), tr["density2011"], "number"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(31.8, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 11.67 lakh people. Scheduled Castes were 17.8% (6.55 lakh)."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("bn", "Bengali", "बांग्ला", "बंगाली", m=("Official", "राजभाषा", "राजभाषा")), it3("kok", "Kokborok", "कोकबोरोक", "कोकबोरोक", m=("Official", "राजभाषा", "राजभाषा")),
        it3("en", "English", "अंग्रेज़ी", "इंग्रजी", m=("Official", "राजभाषा", "राजभाषा")), it3("chakma", "Chakma", "चकमा", "चकमा"), it3("bru", "Kau Bru", "काउ ब्रू", "काउ ब्रू"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [(L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary.")]),
])

module(R, "history", [
    prose("p1", L(
        "The Rajmala, the royal chronicle of Tripura, traces the Manikya dynasty over many centuries; under kings such as Dhanya Manikya in the 15th–16th centuries the kingdom extended into the plains of present-day Bangladesh. The capital moved from Udaipur (Rangamati) to Old Agartala and in 1849 to the present Agartala. Under British rule Tripura remained a princely state, while its plains estate of Chakla Roshnabad was British territory. The Manikya rulers were patrons of Bengali literature and music, and Rabindranath Tagore visited Agartala several times as a guest of Maharaja Birchandra and his successors.\n\nAfter the death of Maharaja Bir Bikram Kishore Manikya in 1947, Maharani Kanchan Prabha Devi, as regent, signed the merger agreement, and Tripura joined India on 15 October 1949. It became a Union Territory in 1956 and a State in 1972. The arrival of refugees after Partition changed the population balance, and tribal unrest and insurgency followed from the late 1970s; the Tripura Tribal Areas Autonomous District Council was set up in 1979–82 and brought under the Sixth Schedule in 1985, and accords with armed groups (1988, 1993, 2019 and 2024) helped restore peace.",
        "त्रिपुरा का राजकीय इतिहास-ग्रंथ राजमाला कई सदियों तक माणिक्य वंश का वर्णन करता है; 15वीं–16वीं सदी में धन्य माणिक्य जैसे राजाओं के समय राज्य आज के बांग्लादेश के मैदानों तक फैला। राजधानी उदयपुर (रंगामाटी) से पुराने अगरतला और 1849 में वर्तमान अगरतला आई। ब्रिटिश शासन में त्रिपुरा एक रियासत बनी रही, जबकि इसकी मैदानी जागीर चाकला रोशनाबाद ब्रिटिश क्षेत्र थी। माणिक्य शासक बांग्ला साहित्य और संगीत के संरक्षक थे, और रवींद्रनाथ टैगोर महाराजा बीरचंद्र और उनके उत्तराधिकारियों के अतिथि के रूप में कई बार अगरतला आए।\n\n1947 में महाराजा बीर बिक्रम किशोर माणिक्य की मृत्यु के बाद रीजेंट महारानी कंचन प्रभा देवी ने विलय समझौते पर हस्ताक्षर किए, और 15 अक्टूबर 1949 को त्रिपुरा भारत में शामिल हुई। यह 1956 में केंद्र शासित प्रदेश और 1972 में राज्य बनी। विभाजन के बाद शरणार्थियों के आगमन से जनसंख्या संतुलन बदला, और 1970 के दशक के अंत से जनजातीय असंतोष और उग्रवाद हुआ; 1979–82 में त्रिपुरा जनजातीय क्षेत्र स्वायत्त ज़िला परिषद बनी और 1985 में छठी अनुसूची में लाई गई, और सशस्त्र समूहों के साथ समझौतों (1988, 1993, 2019 और 2024) ने शांति बहाल करने में मदद की।",
        "त्रिपुराचा राजवंशीय इतिहासग्रंथ राजमाला अनेक शतकांतील माणिक्य घराण्याचे वर्णन करतो; पंधराव्या–सोळाव्या शतकात धन्य माणिक्यसारख्या राजांच्या काळात राज्य आजच्या बांगलादेशच्या मैदानांपर्यंत पसरले. राजधानी उदयपूर (रंगामाटी) हून जुन्या आगरतळ्याला व 1849 मध्ये सध्याच्या आगरतळ्याला आली. ब्रिटिश राजवटीत त्रिपुरा संस्थान राहिले, तर त्याची मैदानी जहागीर चाकला रोशनाबाद ब्रिटिश प्रदेश होती. माणिक्य राज्यकर्ते बंगाली साहित्य व संगीताचे आश्रयदाते होते, आणि रवींद्रनाथ टागोर महाराजा बीरचंद्र व त्यांच्या वारसांचे पाहुणे म्हणून अनेकदा आगरतळ्याला आले.\n\n1947 मध्ये महाराजा बीर बिक्रम किशोर माणिक्य यांच्या निधनानंतर रीजंट महाराणी कांचनप्रभा देवी यांनी विलीनीकरण करारावर स्वाक्षरी केली, आणि 15 ऑक्टोबर 1949 रोजी त्रिपुरा भारतात सामील झाले. ते 1956 मध्ये केंद्रशासित प्रदेश व 1972 मध्ये राज्य झाले. फाळणीनंतर निर्वासितांच्या आगमनाने लोकसंख्येचा समतोल बदलला, आणि 1970 च्या दशकाच्या अखेरीपासून आदिवासी असंतोष व बंडखोरी झाली; 1979–82 मध्ये त्रिपुरा आदिवासी क्षेत्र स्वायत्त जिल्हा परिषद स्थापन झाली व 1985 मध्ये सहाव्या अनुसूचीत आणली गेली, आणि सशस्त्र गटांसोबतच्या करारांनी (1988, 1993, 2019 व 2024) शांतता प्रस्थापित करण्यास मदत केली."),
        conf="Editorial"),
    timeline([
        ev("agartala", 1849, L("1849", "1849", "1849"), L("Capital moves to present Agartala", "राजधानी वर्तमान अगरतला आई", "राजधानी सध्याच्या आगरतळ्याला")),
        ev("ujjayanta", 1901, L("1901", "1901", "1901"), L("Ujjayanta Palace completed", "उज्जयंत महल पूर्ण", "उज्जयंत राजवाडा पूर्ण")),
        ev("merger", 1949, L("15 October 1949", "15 अक्टूबर 1949", "15 ऑक्टोबर 1949"), L("Merger with India", "भारत में विलय", "भारतात विलीनीकरण")),
        ev("ut", 1956, L("1956", "1956", "1956"), L("Union Territory", "केंद्र शासित प्रदेश", "केंद्रशासित प्रदेश")),
        ev("state", 1972, L("21 January 1972", "21 जनवरी 1972", "21 जानेवारी 1972"), L("Tripura becomes a State", "त्रिपुरा राज्य बना", "त्रिपुरा राज्य झाले")),
        ev("adc", 1985, L("1985", "1985", "1985"), L("TTAADC brought under the Sixth Schedule", "टीटीएएडीसी छठी अनुसूची में", "टीटीएएडीसी सहाव्या अनुसूचीत")),
    ]),
    lst("heritage", [
        it3("ujjayanta", "Ujjayanta Palace, Agartala", "उज्जयंत महल, अगरतला", "उज्जयंत राजवाडा, आगरतळा", m=("State Museum", "राज्य संग्रहालय", "राज्य संग्रहालय")),
        it3("neermahal", "Neermahal", "नीरमहल", "नीरमहाल", m=("Lake palace, 1930s", "झील महल, 1930 का दशक", "सरोवरातील महाल, 1930 चे दशक")),
        it3("unakoti", "Unakoti", "उनाकोटी", "उनाकोटी", m=("Rock-cut sculptures", "शैल-उत्कीर्ण मूर्तियाँ", "खडकात कोरलेली शिल्पे")),
        it3("tripurasundari", "Tripura Sundari temple, Udaipur", "त्रिपुरा सुंदरी मंदिर, उदयपुर", "त्रिपुरा सुंदरी मंदिर, उदयपूर"),
        it3("pilak", "Pilak", "पिलाक", "पिलाक", m=("Buddhist and Hindu ruins", "बौद्ध और हिंदू अवशेष", "बौद्ध व हिंदू अवशेष")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
    gaps("g", [(L("Tripura Merger Agreement, 1949 — official text", "त्रिपुरा विलय समझौता, 1949 — आधिकारिक पाठ", "त्रिपुरा विलीनीकरण करार, 1949 — अधिकृत मजकूर"), "india-gov", "National Archives of India.")]),
])
print("tr mod1 ok")
