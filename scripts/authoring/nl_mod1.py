"""Nagaland modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-NL"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
nl = read("regions/IN-NL.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Nagaland is a hill State in the north-east, bordered by Myanmar to the east, Arunachal Pradesh to the north-east, Assam to the north and west, and Manipur to the south. It had 19.8 lakh people at the 2011 Census. Kohima, in the southern hills near the Japfü range, is the capital, and Dimapur in the plains along the Assam border is the main commercial town and transport hub.\n\nNagaland became India's 16th State on 1 December 1963. It is home to the Naga peoples — the Angami, Ao, Chakhesang, Chang, Khiamniungan, Konyak, Lotha, Phom, Pochury, Rengma, Sangtam, Sumi, Yimkhiung, Zeliang and others — each with its own language, customs and village traditions, as well as other communities such as the Kachari and Kuki. English is the official language and Nagamese, a creole, is the common spoken language.",
        "नागालैंड उत्तर-पूर्व का एक पहाड़ी राज्य है, जिसके पूर्व में म्यांमार, उत्तर-पूर्व में अरुणाचल प्रदेश, उत्तर और पश्चिम में असम और दक्षिण में मणिपुर है। 2011 की जनगणना में इसकी जनसंख्या 19.8 लाख थी। जाप्फ़ू पर्वत के पास दक्षिणी पहाड़ियों में बसा कोहिमा राजधानी है, और असम सीमा के मैदानों में दीमापुर मुख्य वाणिज्यिक नगर और परिवहन केंद्र है।\n\nनागालैंड 1 दिसंबर 1963 को भारत का 16वाँ राज्य बना। यह नागा लोगों का घर है — अंगामी, आओ, चाखेसांग, चांग, खियामनियुंगन, कोन्याक, लोथा, फोम, पोचुरी, रेंगमा, सांगताम, सुमी, यिमखियुंग, ज़ेलियांग और अन्य — जिनकी अपनी भाषा, रीति-रिवाज और ग्राम परंपराएँ हैं, साथ ही कचारी और कुकी जैसे अन्य समुदाय भी। अंग्रेज़ी राजभाषा है और नागामीज़, एक मिश्रित भाषा, आम बोलचाल की भाषा है।",
        "नागालँड हे ईशान्येकडील डोंगरी राज्य आहे, ज्याच्या पूर्वेला म्यानमार, ईशान्येला अरुणाचल प्रदेश, उत्तर व पश्चिमेला आसाम आणि दक्षिणेला मणिपूर आहे. 2011 च्या जनगणनेनुसार त्याची लोकसंख्या 19.8 लाख होती. जाप्फू पर्वताजवळील दक्षिणेकडील डोंगरांतील कोहिमा ही राजधानी आहे, आणि आसाम सीमेलगतच्या मैदानातील दिमापूर हे मुख्य व्यापारी शहर व वाहतूक केंद्र आहे.\n\nनागालँड 1 डिसेंबर 1963 रोजी भारताचे 16 वे राज्य झाले. ते नागा लोकांचे घर आहे — अंगामी, आओ, चाखेसांग, चांग, खियामनियुंगन, कोन्याक, लोथा, फोम, पोचुरी, रेंगमा, सांगताम, सुमी, यिमखियुंग, झेलियांग व इतर — प्रत्येकाची स्वतःची भाषा, चालीरीती व ग्रामपरंपरा, तसेच कचारी व कुकी सारखे इतर समुदायही. इंग्रजी ही राजभाषा आहे आणि नागामीज, एक मिश्रभाषा, ही सामान्य बोलीभाषा आहे."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Nagaland is known for its strong village communities, its warrior and morung (youth dormitory) traditions, its colourful shawls and its music. Each December the Hornbill Festival at Kisama near Kohima brings all the Naga tribes together, and the Battle of Kohima in 1944 is remembered at the Kohima War Cemetery. Article 371A of the Constitution protects Naga customary law and ownership of land and its resources, and the village of Khonoma has become known for community conservation. About three-quarters of the State is forest (ISFR 2023).",
        "नागालैंड अपने मज़बूत ग्राम समुदायों, योद्धा और मोरुंग (युवा छात्रावास) परंपराओं, रंगीन शॉलों और संगीत के लिए जाना जाता है। हर दिसंबर कोहिमा के पास किसामा में हॉर्नबिल महोत्सव सभी नागा जनजातियों को एक साथ लाता है, और 1944 के कोहिमा युद्ध को कोहिमा युद्ध समाधि स्थल पर याद किया जाता है। संविधान का अनुच्छेद 371क नागा पारंपरिक क़ानून और भूमि व उसके संसाधनों के स्वामित्व की रक्षा करता है, और खोनोमा गाँव सामुदायिक संरक्षण के लिए जाना जाने लगा है। राज्य का लगभग तीन-चौथाई भाग वन है (आईएसएफ़आर 2023)।",
        "नागालँड आपल्या मजबूत ग्रामसमुदायांसाठी, योद्धा व मोरुंग (तरुणांचे वसतिगृह) परंपरांसाठी, रंगीबेरंगी शालींसाठी व संगीतासाठी ओळखले जाते. दर डिसेंबरमध्ये कोहिमाजवळील किसामा येथील हॉर्नबिल महोत्सव सर्व नागा जमातींना एकत्र आणतो, आणि 1944 च्या कोहिमाच्या लढाईचे कोहिमा युद्धस्मशानात स्मरण केले जाते. संविधानाचा अनुच्छेद 371क नागा पारंपरिक कायदा आणि जमीन व तिच्या संसाधनांच्या मालकीचे संरक्षण करतो, आणि खोनोमा गाव सामुदायिक संवर्धनासाठी ओळखले जाऊ लागले आहे. राज्याचा सुमारे तीन-चतुर्थांश भाग वनाच्छादित आहे (आयएसएफआर 2023)."),
        title=L("What makes Nagaland unique?", "नागालैंड को ख़ास क्या बनाता है?", "नागालँडचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Statehood", "राज्य का दर्जा", "राज्याचा दर्जा"), L("1 December 1963 (Statehood Day)", "1 दिसंबर 1963 (राज्य दिवस)", "1 डिसेंबर 1963 (राज्य दिन)")],
           [L("Districts", "ज़िले", "जिल्हे"), L("Official count to be confirmed (see the gap note); the LGD boundary file of December 2023 shows 16", "आधिकारिक संख्या की पुष्टि होनी है (अंतर-सूचना देखें); दिसंबर 2023 की एलजीडी सीमा फ़ाइल में 16", "अधिकृत संख्येची खात्री व्हायची आहे (त्रुटी-टीप पाहा); डिसेंबर 2023 च्या एलजीडी सीमा फाइलमध्ये 16")],
           [L("Capital", "राजधानी", "राजधानी"), L("Kohima", "कोहिमा", "कोहिमा")],
           [L("Official language", "राजभाषा", "राजभाषा"), L("English", "अंग्रेज़ी", "इंग्रजी")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Gauhati High Court, Kohima bench", "गुवाहाटी उच्च न्यायालय, कोहिमा पीठ", "गुवाहाटी उच्च न्यायालय, कोहिमा खंडपीठ")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "NL"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None),
    gaps("g", [
        (L("Current number of districts — official", "ज़िलों की वर्तमान संख्या — आधिकारिक", "जिल्ह्यांची सद्यःस्थितीतील संख्या — अधिकृत"), "india-gov", "Government of Nagaland notifications on new districts created since 2021."),
    ]),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Nagaland is almost all hills, part of the Naga and Patkai ranges that run along the Myanmar border, with a narrow strip of plains around Dimapur and the foothills bordering Assam. Mount Saramati on the Myanmar border in Kiphire district is the highest peak; Japfü rises above Kohima, and the Dzükou valley on the Nagaland–Manipur border is famous for its seasonal flowers. Rivers such as the Doyang, Dhansiri, Dikhu and Jhanji flow west and north into the Brahmaputra basin, while the Tizu and Zungki drain east towards the Chindwin in Myanmar.",
        "नागालैंड लगभग पूरा पहाड़ी है, जो म्यांमार सीमा के साथ चलने वाली नागा और पटकाई शृंखलाओं का भाग है, और दीमापुर के आसपास मैदानों की एक संकरी पट्टी और असम से लगी तलहटी है। किफ़िरे ज़िले में म्यांमार सीमा पर सारामती पर्वत सबसे ऊँची चोटी है; जाप्फ़ू कोहिमा के ऊपर उठता है, और नागालैंड–मणिपुर सीमा पर ज़ुकू घाटी अपने मौसमी फूलों के लिए प्रसिद्ध है। दोयांग, धनसिरी, दिखू और झांजी जैसी नदियाँ पश्चिम और उत्तर में ब्रह्मपुत्र बेसिन में बहती हैं, जबकि तिज़ू और ज़ुंगकी पूर्व में म्यांमार की चिंदविन की ओर बहती हैं।",
        "नागालँड जवळपास संपूर्ण डोंगराळ आहे, म्यानमार सीमेलगत जाणाऱ्या नागा व पटकाई रांगांचा भाग, दिमापूरभोवती मैदानांची अरुंद पट्टी व आसामलगतचे पायथ्याचे डोंगर वगळता. किफिरे जिल्ह्यात म्यानमार सीमेवरील सारामती पर्वत हे सर्वोच्च शिखर आहे; जाप्फू कोहिमावर उभा आहे, आणि नागालँड–मणिपूर सीमेवरील झुकू खोरे हंगामी फुलांसाठी प्रसिद्ध आहे. दोयांग, धनसिरी, दिखू व झांजीसारख्या नद्या पश्चिम व उत्तरेला ब्रह्मपुत्रा खोऱ्यात वाहतात, तर तिझू व झुंगकी पूर्वेला म्यानमारमधील चिंदविनकडे वाहतात."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), nl["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("mm", "Myanmar (east)", "म्यांमार (पूर्व)", "म्यानमार (पूर्व)"), it3("ar", "Arunachal Pradesh (north-east)", "अरुणाचल प्रदेश (उत्तर-पूर्व)", "अरुणाचल प्रदेश (ईशान्य)"),
        it3("as", "Assam (north and west)", "असम (उत्तर और पश्चिम)", "आसाम (उत्तर व पश्चिम)"), it3("mn", "Manipur (south)", "मणिपुर (दक्षिण)", "मणिपूर (दक्षिण)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("doyang", "Doyang", "दोयांग", "दोयांग", d=("Largest river of the State; Doyang hydro project in Wokha.", "राज्य की सबसे बड़ी नदी; वोखा में दोयांग जलविद्युत परियोजना।", "राज्यातील सर्वांत मोठी नदी; वोखामध्ये दोयांग जलविद्युत प्रकल्प.")),
        it3("dhansiri", "Dhansiri", "धनसिरी", "धनसिरी", d=("Flows past Dimapur into Assam.", "दीमापुर से होकर असम में बहती है।", "दिमापूरवरून आसाममध्ये वाहते.")),
        it3("dikhu", "Dikhu", "दिखू", "दिखू", d=("Drains Mokokchung and Mon districts.", "मोकोकचुंग और मोन ज़िलों का जल बहाती है।", "मोकोकचुंग व मोन जिल्ह्यांचे पाणी वाहते.")),
        it3("tizu", "Tizu", "तिज़ू", "तिझू", d=("Flows east to Myanmar.", "पूर्व में म्यांमार की ओर बहती है।", "पूर्वेला म्यानमारकडे वाहते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Mount Saramati — official elevation", "सारामती पर्वत — आधिकारिक ऊँचाई", "सारामती पर्वत — अधिकृत उंची"), "survey-of-india", "Survey of India."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Nagaland has a monsoon climate that varies with height: Dimapur in the plains is hot and humid, while Kohima at about 1,400 m and other hill towns are mild in summer and cool in winter, with occasional frost on the highest ridges. The south-west monsoon from May to September brings heavy rain and landslides, and October to April is dry, with clear skies from October to December.",
        "नागालैंड की मानसूनी जलवायु ऊँचाई के साथ बदलती है: मैदानों में दीमापुर गर्म और आर्द्र है, जबकि लगभग 1,400 मीटर पर कोहिमा और अन्य पहाड़ी नगर गर्मियों में सुहावने और सर्दियों में ठंडे रहते हैं, और सबसे ऊँची पहाड़ियों पर कभी-कभी पाला पड़ता है। मई से सितंबर तक दक्षिण-पश्चिम मानसून भारी वर्षा और भूस्खलन लाता है, और अक्टूबर से अप्रैल सूखा रहता है, अक्टूबर से दिसंबर साफ़ आसमान के साथ।",
        "नागालँडचे मान्सूनी हवामान उंचीनुसार बदलते: मैदानातील दिमापूर उष्ण व दमट आहे, तर सुमारे 1,400 मीटरवरील कोहिमा व इतर डोंगरी शहरे उन्हाळ्यात सौम्य व हिवाळ्यात थंड असतात, आणि सर्वांत उंच कड्यांवर कधीकधी दव गोठते. मे ते सप्टेंबर नैर्ऋत्य मान्सून मुसळधार पाऊस व भूस्खलन आणतो, आणि ऑक्टोबर ते एप्रिल कोरडा असतो, ऑक्टोबर ते डिसेंबर निरभ्र आकाशासह."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Kohima", "कोहिमा", "कोहिमा"), "lat": 25.6747, "lon": 94.1086},
        {"name": L("Dimapur", "दीमापुर", "दिमापूर"), "lat": 25.9063, "lon": 93.7276},
        {"name": L("Mokokchung", "मोकोकचुंग", "मोकोकचुंग"), "lat": 26.3220, "lon": 94.5130},
        {"name": L("Mon", "मोन", "मोन"), "lat": 26.7350, "lon": 95.0570},
    ]},
    lst("best", [
        it3("dec", "October to December", "अक्टूबर से दिसंबर", "ऑक्टोबर ते डिसेंबर", d=("Clear weather; the Hornbill Festival from 1 December.", "साफ़ मौसम; 1 दिसंबर से हॉर्नबिल महोत्सव।", "निरभ्र हवामान; 1 डिसेंबरपासून हॉर्नबिल महोत्सव.")),
        it3("spring", "February to April", "फ़रवरी से अप्रैल", "फेब्रुवारी ते एप्रिल", d=("Sekrenyi and Aoleang festivals; rhododendrons in bloom.", "सेक्रेन्यी और आओलियांग त्योहार; बुरांश खिलते हैं।", "सेक्रेन्यी व आओलेआंग सण; ऱ्होडोडेंड्रॉन बहरतात.")),
        it3("dzukou", "June to September", "जून से सितंबर", "जून ते सप्टेंबर", d=("Dzükou lilies in bloom, but roads can be blocked by landslides.", "ज़ुकू लिली खिलती हैं, पर भूस्खलन से सड़कें बंद हो सकती हैं।", "झुकू लिली बहरतात, पण भूस्खलनाने रस्ते बंद होऊ शकतात.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall", "सामान्य वार्षिक वर्षा", "सरासरी वार्षिक पाऊस"), "imd", "IMD Kohima / Guwahati regional centre."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Life in Nagaland centres on the village, the clan and the church. Villages sit on ridge tops, each with its own council and gates, and are proud of their histories; Sunday is a quiet day of worship. Food is spicy, smoky and generous, served with rice, and music is everywhere — choirs, folk songs and a lively rock and gospel scene in Kohima and Dimapur. Dimapur's markets are busy and diverse, while Kohima, built across hills, has steep streets lined with shops and churches.",
        "नागालैंड में जीवन गाँव, कुल और चर्च के इर्द-गिर्द घूमता है। गाँव पहाड़ियों की चोटियों पर बसे हैं, हर गाँव की अपनी परिषद और द्वार हैं, और उन्हें अपने इतिहास पर गर्व है; रविवार उपासना का शांत दिन है। भोजन तीखा, धुएँदार और भरपूर होता है, चावल के साथ परोसा जाता है, और संगीत हर जगह है — गायक मंडलियाँ, लोकगीत और कोहिमा व दीमापुर में जीवंत रॉक और गॉस्पेल संगीत। दीमापुर के बाज़ार व्यस्त और विविध हैं, जबकि पहाड़ियों पर बसे कोहिमा की खड़ी गलियाँ दुकानों और चर्चों से भरी हैं।",
        "नागालँडमधील जीवन गाव, कूळ व चर्च यांभोवती फिरते. गावे डोंगरमाथ्यांवर वसलेली आहेत, प्रत्येकाची स्वतःची परिषद व वेशी आहेत, आणि त्यांना आपल्या इतिहासाचा अभिमान आहे; रविवार हा उपासनेचा शांत दिवस असतो. अन्न तिखट, धुरकट व भरपूर असते, भातासोबत वाढले जाते, आणि संगीत सर्वत्र आहे — गायक वृंद, लोकगीते व कोहिमा आणि दिमापूरमधील जिवंत रॉक व गॉस्पेल संगीत. दिमापूरचे बाजार गजबजलेले व वैविध्यपूर्ण आहेत, तर डोंगरांवर वसलेल्या कोहिमाचे उभे रस्ते दुकाने व चर्चनी भरलेले आहेत."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Nagaland had 19.8 lakh people at the 2011 Census, about 119 per km² — fewer than in 2001, as the State's population fell slightly over the decade. Its sex ratio was 931 women per 1,000 men, up from 900, while the child sex ratio fell from 964 to 943; literacy was 79.6%. Scheduled Tribes made up 86.5% of the population, and no Scheduled Castes are listed for the State.\n\nEach Naga tribe speaks its own Tibeto-Burman language — Angami, Ao, Lotha, Sumi, Konyak and others — and villages a few hills apart may speak different dialects. Nagamese, based on Assamese, is the everyday language between communities and in markets, and English is the language of government and schooling.",
        "2011 की जनगणना में नागालैंड की जनसंख्या 19.8 लाख थी, प्रति वर्ग किमी लगभग 119 — 2001 से कम, क्योंकि दशक में राज्य की जनसंख्या थोड़ी घटी। लिंगानुपात प्रति 1,000 पुरुषों पर 931 महिलाएँ था, जो 900 से अधिक है, जबकि शिशु लिंगानुपात 964 से घटकर 943 हुआ; साक्षरता 79.6% थी। अनुसूचित जनजातियाँ जनसंख्या का 86.5% थीं, और राज्य के लिए कोई अनुसूचित जाति सूचीबद्ध नहीं है।\n\nहर नागा जनजाति अपनी तिब्बती-बर्मी भाषा बोलती है — अंगामी, आओ, लोथा, सुमी, कोन्याक और अन्य — और कुछ पहाड़ियों की दूरी पर बसे गाँव भिन्न बोलियाँ बोल सकते हैं। असमिया पर आधारित नागामीज़ समुदायों के बीच और बाज़ारों में रोज़ की भाषा है, और अंग्रेज़ी सरकार और शिक्षा की भाषा है।",
        "2011 च्या जनगणनेनुसार नागालँडची लोकसंख्या 19.8 लाख होती, प्रति चौ.किमी सुमारे 119 — 2001 पेक्षा कमी, कारण दशकात राज्याची लोकसंख्या किंचित घटली. दर 1,000 पुरुषांमागे 931 स्त्रिया होत्या, 900 वरून वाढ, तर बाल लिंग गुणोत्तर 964 वरून 943 पर्यंत घटले; साक्षरता 79.6% होती. अनुसूचित जमाती लोकसंख्येच्या 86.5% होत्या, आणि राज्यासाठी कोणत्याही अनुसूचित जाती सूचीबद्ध नाहीत.\n\nप्रत्येक नागा जमात स्वतःची तिबेटी-बर्मी भाषा बोलते — अंगामी, आओ, लोथा, सुमी, कोन्याक व इतर — आणि काही डोंगरांच्या अंतरावरील गावे वेगवेगळ्या बोली बोलू शकतात. आसामीवर आधारित नागामीज ही समुदायांमधील व बाजारांतील रोजची भाषा आहे, आणि इंग्रजी ही शासन व शिक्षणाची भाषा आहे."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), nl["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), nl["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(900, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), nl["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(964, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), nl["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), nl["density2011"], "number"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(86.5, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 17.1 lakh people. No Scheduled Castes are listed for the State."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("en", "English", "अंग्रेज़ी", "इंग्रजी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("nag", "Nagamese", "नागामीज़", "नागामीज", m=("Link language", "संपर्क भाषा", "संपर्कभाषा")),
        it3("ang", "Angami", "अंगामी", "अंगामी"), it3("ao", "Ao", "आओ", "आओ"), it3("lot", "Lotha", "लोथा", "लोथा"),
        it3("sum", "Sumi", "सुमी", "सुमी"), it3("kon", "Konyak", "कोन्याक", "कोन्याक"), it3("cha", "Chakhesang (Chokri, Khezha)", "चाखेसांग (चोकरी, खेज़ा)", "चाखेसांग (चोकरी, खेझा)"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Tribe-wise population (Census 2011)", "जनजातिवार जनसंख्या (जनगणना 2011)", "जमातनिहाय लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 ST tables (A-11)."),
        (L("Population change 2001–2011 — official explanation", "जनसंख्या परिवर्तन 2001–2011 — आधिकारिक व्याख्या", "लोकसंख्या बदल 2001–2011 — अधिकृत स्पष्टीकरण"), "census", "Census 2011 provisional and final population totals for Nagaland."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "The Naga peoples lived in independent, self-governing villages for centuries, trading with and sometimes raiding the Ahom kingdom of the Brahmaputra valley. The British expanded into the Naga Hills from the 1830s, met long resistance — notably at Khonoma in 1879–80 — and set up the Naga Hills district with Kohima as its headquarters. American Baptist missionaries arrived in the 1870s, and most Nagas became Christian over the following century. In April–June 1944 the Battle of Kohima, fought around the Deputy Commissioner's tennis court, halted the Japanese advance into India.\n\nThe Naga National Council, formed in 1946, sought independence, and a long armed conflict followed. Under the 16-point agreement of 1960 the Naga Hills–Tuensang Area became the State of Nagaland on 1 December 1963. A ceasefire with the NSCN (I-M) was agreed in 1997, and talks between the Government of India and Naga groups, including a framework agreement signed in 2015, have continued since.",
        "नागा लोग सदियों तक स्वतंत्र, स्वशासित गाँवों में रहे, ब्रह्मपुत्र घाटी के अहोम राज्य से व्यापार करते और कभी-कभी धावे बोलते। अंग्रेज़ 1830 के दशक से नागा पहाड़ियों में फैले, उन्हें लंबे प्रतिरोध का सामना करना पड़ा — विशेषकर 1879–80 में खोनोमा में — और उन्होंने कोहिमा मुख्यालय वाला नागा हिल्स ज़िला बनाया। अमेरिकी बैप्टिस्ट मिशनरी 1870 के दशक में आए, और अगली सदी में अधिकांश नागा ईसाई बने। अप्रैल–जून 1944 में डिप्टी कमिश्नर के टेनिस कोर्ट के आसपास लड़े गए कोहिमा युद्ध ने भारत में जापानी बढ़त को रोका।\n\n1946 में बनी नागा नेशनल काउंसिल ने स्वतंत्रता की माँग की, और लंबा सशस्त्र संघर्ष चला। 1960 के 16-सूत्रीय समझौते के तहत नागा हिल्स–त्वेनसांग क्षेत्र 1 दिसंबर 1963 को नागालैंड राज्य बना। 1997 में एनएससीएन (आई-एम) के साथ युद्धविराम हुआ, और 2015 में हस्ताक्षरित एक रूपरेखा समझौते सहित भारत सरकार और नागा समूहों के बीच बातचीत तब से जारी है।",
        "नागा लोक शतकानुशतके स्वतंत्र, स्वशासित गावांत राहिले, ब्रह्मपुत्रा खोऱ्यातील अहोम राज्याशी व्यापार करत व कधीकधी छापे घालत. ब्रिटिश 1830 च्या दशकापासून नागा डोंगरांत पसरले, त्यांना दीर्घ प्रतिकाराला तोंड द्यावे लागले — विशेषतः 1879–80 मध्ये खोनोमा येथे — आणि त्यांनी कोहिमा मुख्यालय असलेला नागा हिल्स जिल्हा स्थापन केला. अमेरिकन बॅप्टिस्ट मिशनरी 1870 च्या दशकात आले, आणि पुढील शतकात बहुतेक नागा ख्रिस्ती झाले. एप्रिल–जून 1944 मध्ये उपायुक्तांच्या टेनिस कोर्टभोवती लढलेल्या कोहिमाच्या लढाईने भारतातील जपानी आगेकूच रोखली.\n\n1946 मध्ये स्थापन झालेल्या नागा नॅशनल कौन्सिलने स्वातंत्र्याची मागणी केली, आणि दीर्घ सशस्त्र संघर्ष झाला. 1960 च्या 16-कलमी कराराअंतर्गत नागा हिल्स–त्वेनसांग क्षेत्र 1 डिसेंबर 1963 रोजी नागालँड राज्य झाले. 1997 मध्ये एनएससीएन (आय-एम) सोबत युद्धविराम झाला, आणि 2015 मध्ये स्वाक्षरी झालेल्या आराखडा करारासह भारत सरकार व नागा गटांमधील चर्चा तेव्हापासून सुरू आहे."),
        conf="Editorial"),
    timeline([
        ev("khonoma", 1879, L("1879–80", "1879–80", "1879–80"), L("Battle of Khonoma against British forces", "ब्रिटिश सेनाओं के विरुद्ध खोनोमा की लड़ाई", "ब्रिटिश सैन्याविरुद्ध खोनोमाची लढाई")),
        ev("kohima", 1944, L("April–June 1944", "अप्रैल–जून 1944", "एप्रिल–जून 1944"), L("Battle of Kohima", "कोहिमा का युद्ध", "कोहिमाची लढाई")),
        ev("nnc", 1946, L("1946", "1946", "1946"), L("Naga National Council formed", "नागा नेशनल काउंसिल का गठन", "नागा नॅशनल कौन्सिलची स्थापना")),
        ev("agreement", 1960, L("1960", "1960", "1960"), L("16-point agreement on statehood", "राज्य के दर्जे पर 16-सूत्रीय समझौता", "राज्य दर्ज्याबाबत 16-कलमी करार")),
        ev("state", 1963, L("1 December 1963", "1 दिसंबर 1963", "1 डिसेंबर 1963"), L("Nagaland becomes India's 16th State", "नागालैंड भारत का 16वाँ राज्य बना", "नागालँड भारताचे 16 वे राज्य")),
        ev("ceasefire", 1997, L("1997", "1997", "1997"), L("Ceasefire with the NSCN (I-M)", "एनएससीएन (आई-एम) के साथ युद्धविराम", "एनएससीएन (आय-एम) सोबत युद्धविराम")),
        ev("hornbill", 2000, L("2000", "2000", "2000"), L("First Hornbill Festival", "पहला हॉर्नबिल महोत्सव", "पहिला हॉर्नबिल महोत्सव")),
        ev("framework", 2015, L("2015", "2015", "2015"), L("Framework agreement signed in the Naga peace talks", "नागा शांति वार्ता में रूपरेखा समझौते पर हस्ताक्षर", "नागा शांतता चर्चेत आराखडा करारावर स्वाक्षरी")),
        ev("rail", 2021, L("October 2021", "अक्टूबर 2021", "ऑक्टोबर 2021"), L("First section of the Dimapur–Kohima railway opens", "दीमापुर–कोहिमा रेल लाइन का पहला खंड खुला", "दिमापूर–कोहिमा रेल्वेचा पहिला टप्पा सुरू")),
    ]),
    lst("heritage", [
        it3("warcemetery", "Kohima War Cemetery", "कोहिमा युद्ध समाधि स्थल", "कोहिमा युद्धस्मशान", m=("1944 battle", "1944 का युद्ध", "1944 ची लढाई")),
        it3("kisama", "Kisama Heritage Village", "किसामा धरोहर गाँव", "किसामा वारसा गाव", m=("Hornbill Festival venue", "हॉर्नबिल महोत्सव स्थल", "हॉर्नबिल महोत्सवाचे ठिकाण")),
        it3("khonoma", "Khonoma village", "खोनोमा गाँव", "खोनोमा गाव", m=("Angami village; community conservation", "अंगामी गाँव; सामुदायिक संरक्षण", "अंगामी गाव; सामुदायिक संवर्धन")),
        it3("ruins", "Kachari ruins, Dimapur", "कचारी खंडहर, दीमापुर", "कचारी अवशेष, दिमापूर", m=("Mushroom-shaped monoliths", "कुकुरमुत्ते जैसे शिलास्तंभ", "भूछत्राच्या आकाराचे शिलास्तंभ")),
        it3("longwa", "Longwa village", "लोंगवा गाँव", "लोंगवा गाव", m=("Konyak village on the Myanmar border", "म्यांमार सीमा पर कोन्याक गाँव", "म्यानमार सीमेवरील कोन्याक गाव")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
    gaps("g", [
        (L("16-point agreement and State of Nagaland Act, 1962 — official text", "16-सूत्रीय समझौता और नागालैंड राज्य अधिनियम, 1962 — आधिकारिक पाठ", "16-कलमी करार व नागालँड राज्य अधिनियम, 1962 — अधिकृत मजकूर"), "india-gov", "India Code / Ministry of Home Affairs."),
    ]),
])
print("nl mod1 ok")
