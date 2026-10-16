"""Chhattisgarh modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-CT"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
ct = read("regions/IN-CT.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Chhattisgarh lies in central-eastern India, bordered by seven States: Madhya Pradesh, Uttar Pradesh, Jharkhand, Odisha, Andhra Pradesh, Telangana and Maharashtra. Its heart is the fertile Chhattisgarh plain of the upper Mahanadi, ringed by forested hills — the Maikal range to the west, the Surguja highlands to the north and the Bastar plateau to the south. Over two-fifths of the State is forest. It had 2.55 crore people at the 2011 Census. Raipur is the capital, with the planned new capital Nava Raipur Atal Nagar nearby; Bhilai–Durg, Bilaspur, Korba and Jagdalpur are other major cities.\n\nChhattisgarh was carved out of Madhya Pradesh on 1 November 2000. Hindi is the official language, and Chhattisgarhi, the language of the plains, also has official status.",
        "छत्तीसगढ़ मध्य-पूर्वी भारत में स्थित है, और इसकी सीमाएँ सात राज्यों से लगती हैं: मध्य प्रदेश, उत्तर प्रदेश, झारखंड, ओडिशा, आंध्र प्रदेश, तेलंगाना और महाराष्ट्र। इसका हृदय ऊपरी महानदी का उपजाऊ छत्तीसगढ़ मैदान है, जो वनाच्छादित पहाड़ियों से घिरा है — पश्चिम में मैकल श्रेणी, उत्तर में सरगुजा के ऊँचे क्षेत्र और दक्षिण में बस्तर पठार। राज्य का दो-पाँचवें से अधिक भाग वन है। 2011 की जनगणना में इसकी जनसंख्या 2.55 करोड़ थी। रायपुर राजधानी है, और पास में नियोजित नई राजधानी नवा रायपुर अटल नगर है; भिलाई–दुर्ग, बिलासपुर, कोरबा और जगदलपुर अन्य प्रमुख शहर हैं।\n\nछत्तीसगढ़ 1 नवंबर 2000 को मध्य प्रदेश से अलग होकर बना। हिंदी राजभाषा है, और मैदानी क्षेत्र की भाषा छत्तीसगढ़ी को भी राजभाषा का दर्जा प्राप्त है।",
        "छत्तीसगड मध्य-पूर्व भारतात असून त्याच्या सीमा सात राज्यांना लागतात: मध्य प्रदेश, उत्तर प्रदेश, झारखंड, ओडिशा, आंध्र प्रदेश, तेलंगणा व महाराष्ट्र. त्याचे हृदय म्हणजे वरच्या महानदीचे सुपीक छत्तीसगड मैदान, जे वनाच्छादित डोंगरांनी वेढलेले आहे — पश्चिमेला मैकल रांग, उत्तरेला सरगुजाचा उंचवटा व दक्षिणेला बस्तर पठार. राज्याचा दोन-पंचमांशांहून अधिक भाग वनाच्छादित आहे. 2011 च्या जनगणनेनुसार त्याची लोकसंख्या 2.55 कोटी होती. रायपूर ही राजधानी असून जवळच नियोजित नवी राजधानी नवा रायपूर अटल नगर आहे; भिलाई–दुर्ग, बिलासपूर, कोरबा व जगदलपूर ही इतर प्रमुख शहरे आहेत.\n\nछत्तीसगड 1 नोव्हेंबर 2000 रोजी मध्य प्रदेशातून वेगळे होऊन निर्माण झाले. हिंदी ही राजभाषा आहे, आणि मैदानी प्रदेशाची भाषा छत्तीसगढीलाही राजभाषेचा दर्जा आहे."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Chhattisgarh is often called the 'rice bowl' of central India, for the paddy fields of its plains and the many traditional rice varieties grown by its farmers, two of which — Jeeraphool and Nagri Dubraj — are registered GIs. It is also a mineral and power State: the Bhilai Steel Plant, the iron-ore mines of Bailadila and the coal and power stations of Korba drive its industry. Bastar in the south is known for Dhokra bell-metal, wrought-iron and wood crafts, for its weekly haats, and for Bastar Dussehra, a festival lasting about 75 days devoted to the goddess Danteshwari. Chitrakote falls on the Indravati, the ancient brick temples of Sirpur and the Pandavani ballads made famous by Teejan Bai are among its treasures.",
        "छत्तीसगढ़ को अक्सर मध्य भारत का 'धान का कटोरा' कहा जाता है, अपने मैदानों के धान के खेतों और किसानों द्वारा उगाई जाने वाली अनेक पारंपरिक धान किस्मों के कारण, जिनमें से दो — जीराफूल और नगरी दुबराज — पंजीकृत जीआई हैं। यह खनिज और बिजली का राज्य भी है: भिलाई इस्पात संयंत्र, बैलाडीला की लौह अयस्क खदानें और कोरबा के कोयला व बिजली संयंत्र इसके उद्योग को चलाते हैं। दक्षिण का बस्तर ढोकरा घंटा-धातु, लोहे और लकड़ी के शिल्प, साप्ताहिक हाटों, और देवी दंतेश्वरी को समर्पित लगभग 75 दिन चलने वाले बस्तर दशहरे के लिए जाना जाता है। इंद्रावती पर चित्रकोट जलप्रपात, सिरपुर के प्राचीन ईंट मंदिर और तीजन बाई द्वारा प्रसिद्ध की गई पंडवानी गाथाएँ इसकी धरोहरों में हैं।",
        "छत्तीसगडला अनेकदा मध्य भारताचे 'भाताचे कोठार' म्हटले जाते, त्याच्या मैदानांतील भातशेतीमुळे व शेतकऱ्यांनी जपलेल्या अनेक पारंपरिक भात वाणांमुळे, ज्यांपैकी दोन — जीराफूल व नगरी दुबराज — नोंदणीकृत जीआय आहेत. हे खनिज व विजेचे राज्यही आहे: भिलाई पोलाद कारखाना, बैलाडिलाच्या लोहखनिज खाणी आणि कोरब्याचे कोळसा व वीज प्रकल्प त्याचे उद्योग चालवतात. दक्षिणेकडील बस्तर ढोकरा घंटाधातू, लोखंड व लाकडी हस्तकला, आठवडी बाजार आणि देवी दंतेश्वरीला समर्पित सुमारे 75 दिवस चालणाऱ्या बस्तर दसऱ्यासाठी ओळखले जाते. इंद्रावतीवरील चित्रकोट धबधबा, सिरपूरची प्राचीन विटांची मंदिरे व तीजनबाईंनी प्रसिद्ध केलेल्या पंडवानी गाथा हा त्याचा ठेवा आहे."),
        title=L("What makes Chhattisgarh unique?", "छत्तीसगढ़ को ख़ास क्या बनाता है?", "छत्तीसगडचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed", "गठन", "निर्मिती"), L("1 November 2000 (from Madhya Pradesh)", "1 नवंबर 2000 (मध्य प्रदेश से)", "1 नोव्हेंबर 2000 (मध्य प्रदेशातून)")],
           [L("Districts / divisions", "ज़िले / संभाग", "जिल्हे / विभाग"), "33 / 5"],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Hindi; Chhattisgarhi", "हिंदी; छत्तीसगढ़ी", "हिंदी; छत्तीसगढी")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("High Court of Chhattisgarh, Bilaspur (2000)", "छत्तीसगढ़ उच्च न्यायालय, बिलासपुर (2000)", "छत्तीसगड उच्च न्यायालय, बिलासपूर (2000)")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "CG"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be linked to the State's notifications in review.", "संपादकीय; समीक्षा में राज्य की अधिसूचनाओं से जोड़ा जाएगा।", "संपादकीय; तपासणीत राज्याच्या अधिसूचनांशी जोडले जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Chhattisgarh has three natural regions. The northern hills of Surguja, Koriya and Jashpur, including the Mainpat plateau, are part of the Chota Nagpur and Baghelkhand uplands and drain to the Son and Ganga. The central Chhattisgarh plain, drained by the Mahanadi and its tributaries the Shivnath, Hasdeo, Arpa and Jonk, is the State's agricultural and industrial core, with Raipur, Bilaspur and Durg. The southern Bastar plateau, densely forested and cut by the Indravati and Sabari, rises to the Abujhmarh hills and the Bailadila iron-ore range; the Indravati plunges over Chitrakote falls before flowing into the Godavari.",
        "छत्तीसगढ़ के तीन प्राकृतिक क्षेत्र हैं। सरगुजा, कोरिया और जशपुर की उत्तरी पहाड़ियाँ, मैनपाट पठार सहित, छोटा नागपुर और बघेलखंड के ऊँचे क्षेत्रों का हिस्सा हैं और सोन व गंगा की ओर बहती हैं। महानदी और उसकी सहायक शिवनाथ, हसदेव, अरपा और जोंक से सिंचित मध्य छत्तीसगढ़ मैदान रायपुर, बिलासपुर और दुर्ग सहित राज्य का कृषि और औद्योगिक केंद्र है। घने वनों वाला और इंद्रावती व सबरी से कटा दक्षिणी बस्तर पठार अबूझमाड़ पहाड़ियों और बैलाडीला लौह अयस्क श्रेणी तक उठता है; इंद्रावती गोदावरी में मिलने से पहले चित्रकोट जलप्रपात से गिरती है।",
        "छत्तीसगडचे तीन नैसर्गिक प्रदेश आहेत. सरगुजा, कोरिया व जशपूरचे उत्तरेकडील डोंगर, मैनपाट पठारासह, छोटा नागपूर व बघेलखंडच्या उंचवट्याचा भाग असून सोन व गंगेकडे वाहतात. महानदी व तिच्या शिवनाथ, हसदेव, अरपा व जोंक या उपनद्यांनी भिजलेले मध्य छत्तीसगड मैदान रायपूर, बिलासपूर व दुर्गसह राज्याचे कृषी व औद्योगिक केंद्र आहे. घनदाट वनांचे व इंद्रावती आणि सबरीने कापलेले दक्षिणेकडील बस्तर पठार अबुझमाड डोंगर व बैलाडिला लोहखनिज रांगेपर्यंत उंचावते; इंद्रावती गोदावरीला मिळण्यापूर्वी चित्रकोट धबधब्यातून कोसळते."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), ct["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("mp", "Madhya Pradesh (north-west)", "मध्य प्रदेश (उत्तर-पश्चिम)", "मध्य प्रदेश (वायव्य)"), it3("up", "Uttar Pradesh (north)", "उत्तर प्रदेश (उत्तर)", "उत्तर प्रदेश (उत्तर)"),
        it3("jh", "Jharkhand (north-east)", "झारखंड (उत्तर-पूर्व)", "झारखंड (ईशान्य)"), it3("or", "Odisha (east)", "ओडिशा (पूर्व)", "ओडिशा (पूर्व)"),
        it3("ap", "Andhra Pradesh (south)", "आंध्र प्रदेश (दक्षिण)", "आंध्र प्रदेश (दक्षिण)"), it3("tg", "Telangana (south)", "तेलंगाना (दक्षिण)", "तेलंगणा (दक्षिण)"),
        it3("mh", "Maharashtra (west)", "महाराष्ट्र (पश्चिम)", "महाराष्ट्र (पश्चिम)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("mahanadi", "Mahanadi", "महानदी", "महानदी", d=("Rises near Sihawa in Dhamtari; dammed at Gangrel; flows east into Odisha.", "धमतरी में सिहावा के पास से निकलती है; गंगरेल पर बाँधी गई; पूर्व में ओडिशा जाती है।", "धमतरीत सिहावाजवळ उगम; गंगरेल येथे धरण; पूर्वेकडे ओडिशात जाते.")),
        it3("shivnath", "Shivnath", "शिवनाथ", "शिवनाथ", d=("Main tributary of the Mahanadi, past Durg.", "महानदी की मुख्य सहायक नदी, दुर्ग से होकर।", "महानदीची मुख्य उपनदी, दुर्गमार्गे.")),
        it3("hasdeo", "Hasdeo", "हसदेव", "हसदेव", d=("Flows through the Korba coalfield; Hasdeo Bango dam.", "कोरबा कोयला क्षेत्र से होकर बहती है; हसदेव बांगो बाँध।", "कोरबा कोळसा क्षेत्रातून वाहते; हसदेव बांगो धरण.")),
        it3("indravati", "Indravati", "इंद्रावती", "इंद्रावती", d=("Bastar's river; Chitrakote falls; joins the Godavari.", "बस्तर की नदी; चित्रकोट जलप्रपात; गोदावरी से मिलती है।", "बस्तरची नदी; चित्रकोट धबधबा; गोदावरीला मिळते.")),
        it3("arpa", "Arpa", "अरपा", "अरपा", d=("Flows through Bilaspur.", "बिलासपुर से होकर बहती है।", "बिलासपूरमधून वाहते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point — official elevation", "सर्वोच्च बिंदु — आधिकारिक ऊँचाई", "सर्वोच्च शिखर — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Mineral reserves by mineral", "खनिजवार भंडार", "खनिजनिहाय साठे"), "india-gov", "Indian Bureau of Mines, Indian Minerals Yearbook."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Chhattisgarh has a tropical climate. Summers (March–June) are very hot on the plains — Raipur, Bilaspur and Durg are among the hottest cities of central India in May — while Mainpat and the Bastar hills are milder. The south-west monsoon (mid-June to September) brings most of the year's rain, heavier in Bastar and the northern hills than on the plains. Winters (November–February) are pleasant, with cold nights in Surguja and Mainpat.",
        "छत्तीसगढ़ की जलवायु उष्णकटिबंधीय है। गर्मियाँ (मार्च–जून) मैदानों में बहुत गर्म होती हैं — मई में रायपुर, बिलासपुर और दुर्ग मध्य भारत के सबसे गर्म शहरों में होते हैं — जबकि मैनपाट और बस्तर की पहाड़ियाँ अपेक्षाकृत ठंडी रहती हैं। दक्षिण-पश्चिम मानसून (मध्य जून से सितंबर) वर्ष की अधिकांश वर्षा लाता है, जो मैदानों की तुलना में बस्तर और उत्तरी पहाड़ियों में अधिक होती है। सर्दियाँ (नवंबर–फ़रवरी) सुहावनी होती हैं, और सरगुजा व मैनपाट में रातें ठंडी।",
        "छत्तीसगडचे हवामान उष्णकटिबंधीय आहे. उन्हाळा (मार्च–जून) मैदानांत अतिशय उष्ण असतो — मे महिन्यात रायपूर, बिलासपूर व दुर्ग ही मध्य भारतातील सर्वांत उष्ण शहरांपैकी असतात — तर मैनपाट व बस्तरचे डोंगर तुलनेने सौम्य असतात. नैर्ऋत्य मान्सून (जूनच्या मध्यापासून सप्टेंबरपर्यंत) वर्षाचा बहुतेक पाऊस आणतो, जो मैदानांपेक्षा बस्तर व उत्तरेकडील डोंगरांत अधिक असतो. हिवाळा (नोव्हेंबर–फेब्रुवारी) आल्हाददायक असतो, आणि सरगुजा व मैनपाटमध्ये रात्री थंड असतात."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Raipur", "रायपुर", "रायपूर"), "lat": 21.2514, "lon": 81.6296},
        {"name": L("Bilaspur", "बिलासपुर", "बिलासपूर"), "lat": 22.0797, "lon": 82.1409},
        {"name": L("Jagdalpur", "जगदलपुर", "जगदलपूर"), "lat": 19.0748, "lon": 82.0080},
        {"name": L("Ambikapur", "अंबिकापुर", "अंबिकापूर"), "lat": 23.1186, "lon": 83.1950},
    ]},
    lst("best", [
        it3("winter", "October to February", "अक्टूबर से फ़रवरी", "ऑक्टोबर ते फेब्रुवारी", d=("Best for Bastar, Sirpur and wildlife; Bastar Dussehra in October.", "बस्तर, सिरपुर और वन्यजीवों के लिए सबसे अच्छा; अक्टूबर में बस्तर दशहरा।", "बस्तर, सिरपूर व वन्यजीवांसाठी उत्तम; ऑक्टोबरमध्ये बस्तर दसरा.")),
        it3("monsoon", "July to September", "जुलाई से सितंबर", "जुलै ते सप्टेंबर", d=("Chitrakote and Tirathgarh falls at their fullest; Hareli festival.", "चित्रकोट और तीरथगढ़ जलप्रपात पूरे वेग पर; हरेली त्योहार।", "चित्रकोट व तीरथगड धबधबे पूर्ण भरात; हरेली सण.")),
        it3("spring", "February–March", "फ़रवरी–मार्च", "फेब्रुवारी–मार्च", d=("Rajim Punni Mela and Madai fairs in Bastar.", "राजिम पुन्नी मेला और बस्तर में मड़ई मेले।", "राजिम पुन्नी मेळा व बस्तरमधील मडई जत्रा.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (Chhattisgarh sub-division)", "सामान्य वार्षिक वर्षा (छत्तीसगढ़ उप-मंडल)", "सरासरी वार्षिक पाऊस (छत्तीसगड उपविभाग)"), "imd", "IMD rainfall statistics."),
        (L("Record temperatures", "रिकॉर्ड तापमान", "विक्रमी तापमान"), "imd", "IMD station climatology for Raipur and Bilaspur."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Chhattisgarh moves to the rhythm of paddy. In the plains, villages wake to the lowing of cattle and the smell of wood fires, and festivals mark each stage of the rice year — Hareli at sowing, Pola for the bullocks, and Cherchera after harvest, when children go from house to house collecting new rice. Chhattisgarhi songs, Raut Nacha dancers and Pandavani storytellers enliven fairs. In Bastar, weekly haats under the mahua trees are the great social events, where tribal families trade forest produce, buy cloth and meet friends. In Bhilai and Korba, the steel plant and the power stations set a different, industrial pace.",
        "छत्तीसगढ़ धान की लय पर चलता है। मैदानों में गाँव मवेशियों की आवाज़ और लकड़ी के चूल्हों की गंध के साथ जागते हैं, और त्योहार धान के वर्ष के हर चरण को चिह्नित करते हैं — बुवाई पर हरेली, बैलों के लिए पोला, और फ़सल के बाद छेरछेरा, जब बच्चे घर-घर जाकर नया धान माँगते हैं। छत्तीसगढ़ी गीत, राउत नाचा के नर्तक और पंडवानी गायक मेलों में जान डालते हैं। बस्तर में महुआ के पेड़ों के नीचे लगने वाले साप्ताहिक हाट बड़े सामाजिक आयोजन हैं, जहाँ आदिवासी परिवार वनोपज बेचते, कपड़ा ख़रीदते और मित्रों से मिलते हैं। भिलाई और कोरबा में इस्पात संयंत्र और बिजलीघर एक अलग, औद्योगिक गति तय करते हैं।",
        "छत्तीसगड भाताच्या लयीवर चालते. मैदानांत गावे गुरांच्या हंबरण्याने व चुलीच्या धुराच्या वासाने जागी होतात, आणि सण भाताच्या वर्षातील प्रत्येक टप्पा साजरा करतात — पेरणीला हरेली, बैलांसाठी पोळा, आणि सुगीनंतर छेरछेरा, जेव्हा मुले घरोघरी जाऊन नवे धान्य मागतात. छत्तीसगढी गाणी, राउत नाचाचे नर्तक व पंडवानी गायक जत्रांत रंगत आणतात. बस्तरमध्ये मोहाच्या झाडांखाली भरणारे आठवडी बाजार हे मोठे सामाजिक प्रसंग असतात, जिथे आदिवासी कुटुंबे वनोपज विकतात, कापड घेतात व मित्रांना भेटतात. भिलाई व कोरब्यात पोलाद कारखाना व वीजकेंद्रे वेगळी, औद्योगिक गती ठरवतात."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Chhattisgarh had 2.55 crore people at the 2011 Census, with about 189 people per km². Its sex ratio, 991 women per 1,000 men, was among the highest in India, and the child sex ratio was 969. Literacy rose from 64.7% in 2001 to 70.3% in 2011. Scheduled Tribes made up 30.6% of the population — one of the highest shares among the larger States — and Scheduled Castes 12.8%.\n\nThe Gond are the largest tribal community, and the State is also home to the Oraon, Kanwar, Halba, Bhatra, Baiga, Muria, Maria and others, including particularly vulnerable groups such as the Abujhmaria, Baiga, Birhor, Kamar and Pahadi Korwa. Hindi and Chhattisgarhi are the main languages; Gondi, Halbi, Kurukh and Sadri are widely spoken in tribal areas, and Odia and Telugu near the borders.",
        "2011 की जनगणना में छत्तीसगढ़ की जनसंख्या 2.55 करोड़ थी, और प्रति वर्ग किमी लगभग 189 लोग। प्रति 1,000 पुरुषों पर 991 महिलाओं का इसका लिंगानुपात भारत में सबसे ऊँचे में था, और शिशु लिंगानुपात 969 था। साक्षरता 2001 के 64.7% से बढ़कर 2011 में 70.3% हुई। अनुसूचित जनजातियाँ जनसंख्या का 30.6% थीं — बड़े राज्यों में सबसे ऊँचे हिस्सों में से एक — और अनुसूचित जातियाँ 12.8%।\n\nगोंड सबसे बड़ा जनजातीय समुदाय है, और राज्य में उरांव, कंवर, हल्बा, भतरा, बैगा, मुरिया, माड़िया और अन्य समुदाय भी रहते हैं, जिनमें अबूझमाड़िया, बैगा, बिरहोर, कमार और पहाड़ी कोरवा जैसे विशेष रूप से कमज़ोर समूह शामिल हैं। हिंदी और छत्तीसगढ़ी मुख्य भाषाएँ हैं; जनजातीय क्षेत्रों में गोंडी, हल्बी, कुड़ुख और सादरी, और सीमाओं के पास ओड़िया व तेलुगु व्यापक रूप से बोली जाती हैं।",
        "2011 च्या जनगणनेनुसार छत्तीसगडची लोकसंख्या 2.55 कोटी होती, आणि प्रति चौ.किमी सुमारे 189 लोक. दर 1,000 पुरुषांमागे 991 स्त्रिया हे त्याचे लिंग गुणोत्तर भारतातील सर्वाधिकांपैकी होते, आणि बाल लिंग गुणोत्तर 969 होते. साक्षरता 2001 मधील 64.7% वरून 2011 मध्ये 70.3% झाली. अनुसूचित जमाती लोकसंख्येच्या 30.6% होत्या — मोठ्या राज्यांतील सर्वाधिक वाट्यांपैकी एक — आणि अनुसूचित जाती 12.8%.\n\nगोंड हा सर्वांत मोठा आदिवासी समुदाय आहे, आणि राज्यात ओराव, कंवर, हल्बा, भतरा, बैगा, मुरिया, माडिया व इतर समुदायही राहतात, ज्यांत अबुझमाडिया, बैगा, बिरहोर, कमार व पहाडी कोरवा यांसारखे विशेष असुरक्षित गट आहेत. हिंदी व छत्तीसगढी या मुख्य भाषा आहेत; आदिवासी भागांत गोंडी, हल्बी, कुडुख व सादरी, आणि सीमांजवळ ओडिया व तेलुगू मोठ्या प्रमाणावर बोलल्या जातात."),
        sources=["census", "es-india", "dl-planning"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), ct["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), ct["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(989, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), ct["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(975, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), ct["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"],
             previous=dp(64.7, "%", "2001", "census", "es-india", ESI_LIT)),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), ct["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(12.8, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 32.74 lakh people."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(30.6, "%", "2011", "census", "dl-planning", SCST, note="Same table: 78.23 lakh people."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("hi", "Hindi", "हिंदी", "हिंदी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("hne", "Chhattisgarhi", "छत्तीसगढ़ी", "छत्तीसगढी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("gon", "Gondi", "गोंडी", "गोंडी"), it3("hlb", "Halbi", "हल्बी", "हल्बी"), it3("kru", "Kurukh", "कुड़ुख", "कुडुख"),
        it3("sck", "Sadri", "सादरी", "सादरी"), it3("or", "Odia", "ओड़िया", "ओडिया"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Final Population Totals for Chhattisgarh."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "In ancient times the region was known as Dakshina Kosala, and the forests of Bastar are linked with the Dandakaranya of the Ramayana. Sirpur on the Mahanadi was a capital of the Panduvamshi and Somavamshi kings, whose 7th-century brick Lakshmana temple and Buddhist monasteries survive. From around the 11th century the Kalachuri (Haihaya) kings ruled from Ratanpur and later Raipur — the name Chhattisgarh, 'thirty-six forts', is usually traced to their domains — while the Kakatiya-descended kings of Bastar ruled the south. The Bhonsle Marathas of Nagpur took over in the 18th century, and the region passed to the British with Nagpur in 1854, becoming a division of the Central Provinces.\n\nVeer Narayan Singh of Sonakhan was executed in 1857 and is remembered as the State's first martyr, and Gunda Dhur led the Bhumkal rebellion in Bastar in 1910. Guru Ghasidas founded the Satnami movement against caste discrimination in the early 19th century. After independence the region was part of Madhya Pradesh until the State of Chhattisgarh was formed on 1 November 2000.",
        "प्राचीन काल में यह क्षेत्र दक्षिण कोसल कहलाता था, और बस्तर के वन रामायण के दंडकारण्य से जोड़े जाते हैं। महानदी पर सिरपुर पांडुवंशी और सोमवंशी राजाओं की राजधानी था, जिनका 7वीं सदी का ईंटों का लक्ष्मण मंदिर और बौद्ध विहार आज भी बचे हैं। लगभग 11वीं सदी से कलचुरि (हैहय) राजाओं ने रतनपुर और बाद में रायपुर से शासन किया — 'छत्तीसगढ़' यानी 'छत्तीस किले' नाम सामान्यतः उनके राज्य से जोड़ा जाता है — जबकि काकतीय वंश से जुड़े बस्तर के राजाओं ने दक्षिण पर शासन किया। 18वीं सदी में नागपुर के भोंसले मराठों ने अधिकार किया, और 1854 में नागपुर के साथ यह क्षेत्र अंग्रेज़ों के पास गया और मध्य प्रांत का एक संभाग बना।\n\nसोनाखान के वीर नारायण सिंह को 1857 में फाँसी दी गई और उन्हें राज्य का पहला शहीद माना जाता है, और गुंडाधुर ने 1910 में बस्तर में भूमकाल विद्रोह का नेतृत्व किया। गुरु घासीदास ने 19वीं सदी के आरंभ में जातिगत भेदभाव के विरुद्ध सतनामी आंदोलन की नींव रखी। स्वतंत्रता के बाद यह क्षेत्र 1 नवंबर 2000 को छत्तीसगढ़ राज्य बनने तक मध्य प्रदेश का हिस्सा रहा।",
        "प्राचीन काळी हा प्रदेश दक्षिण कोसल म्हणून ओळखला जाई, आणि बस्तरची जंगले रामायणातील दंडकारण्याशी जोडली जातात. महानदीकाठचे सिरपूर ही पांडुवंशी व सोमवंशी राजांची राजधानी होती, ज्यांचे सातव्या शतकातील विटांचे लक्ष्मण मंदिर व बौद्ध विहार आजही टिकून आहेत. सुमारे अकराव्या शतकापासून कलचुरी (हैहय) राजांनी रतनपूर व नंतर रायपूरहून राज्य केले — 'छत्तीसगड' म्हणजे 'छत्तीस किल्ले' हे नाव सामान्यतः त्यांच्या राज्याशी जोडले जाते — तर काकतीय घराण्याशी नाते सांगणाऱ्या बस्तरच्या राजांनी दक्षिणेवर राज्य केले. अठराव्या शतकात नागपूरच्या भोसले मराठ्यांनी ताबा घेतला, आणि 1854 मध्ये नागपूरसोबत हा प्रदेश इंग्रजांकडे गेला व मध्य प्रांताचा एक विभाग बनला.\n\nसोनाखानच्या वीर नारायणसिंहांना 1857 मध्ये फाशी देण्यात आली व त्यांना राज्याचे पहिले हुतात्मा मानले जाते, आणि गुंडाधुर यांनी 1910 मध्ये बस्तरमध्ये भूमकाल उठावाचे नेतृत्व केले. गुरु घासीदास यांनी एकोणिसाव्या शतकाच्या प्रारंभी जातिभेदाविरुद्ध सतनामी चळवळ सुरू केली. स्वातंत्र्यानंतर 1 नोव्हेंबर 2000 रोजी छत्तीसगड राज्य निर्माण होईपर्यंत हा प्रदेश मध्य प्रदेशाचा भाग होता."),
        conf="Editorial"),
    timeline([
        ev("sirpur", 650, L("7th century", "7वीं सदी", "सातवे शतक"), L("Lakshmana temple built at Sirpur", "सिरपुर में लक्ष्मण मंदिर बना", "सिरपूर येथे लक्ष्मण मंदिर बांधले")),
        ev("kalachuri", 1050, L("c. 11th century", "लगभग 11वीं सदी", "सुमारे अकरावे शतक"), L("Kalachuris rule from Ratanpur", "रतनपुर से कलचुरियों का शासन", "रतनपूरहून कलचुरींचे राज्य")),
        ev("maratha", 1758, L("18th century", "18वीं सदी", "अठरावे शतक"), L("Bhonsle Marathas of Nagpur take control", "नागपुर के भोंसले मराठों का अधिकार", "नागपूरच्या भोसले मराठ्यांचा ताबा")),
        ev("british", 1854, L("1854", "1854", "1854"), L("Passes to British rule with Nagpur", "नागपुर के साथ ब्रिटिश शासन में", "नागपूरसोबत ब्रिटिश सत्तेखाली")),
        ev("narayan", 1857, L("1857", "1857", "1857"), L("Veer Narayan Singh executed at Raipur", "रायपुर में वीर नारायण सिंह को फाँसी", "रायपूर येथे वीर नारायणसिंहांना फाशी")),
        ev("bhumkal", 1910, L("1910", "1910", "1910"), L("Bhumkal rebellion in Bastar", "बस्तर में भूमकाल विद्रोह", "बस्तरमध्ये भूमकाल उठाव")),
        ev("bhilai", 1959, L("1959", "1959", "1959"), L("Bhilai Steel Plant begins production", "भिलाई इस्पात संयंत्र में उत्पादन शुरू", "भिलाई पोलाद कारखान्यात उत्पादन सुरू")),
        ev("state", 2000, L("1 November 2000", "1 नवंबर 2000", "1 नोव्हेंबर 2000"), L("Chhattisgarh State formed", "छत्तीसगढ़ राज्य बना", "छत्तीसगड राज्याची निर्मिती")),
        ev("cm2023", 2023, L("13 December 2023", "13 दिसंबर 2023", "13 डिसेंबर 2023"), L("Vishnu Deo Sai sworn in as Chief Minister", "विष्णु देव साय ने मुख्यमंत्री पद की शपथ ली", "विष्णुदेव साय यांचा मुख्यमंत्रिपदाचा शपथविधी")),
    ]),
    lst("heritage", [
        it3("sirpur", "Sirpur", "सिरपुर", "सिरपूर", m=("Lakshmana temple; Buddhist viharas", "लक्ष्मण मंदिर; बौद्ध विहार", "लक्ष्मण मंदिर; बौद्ध विहार")),
        it3("bhoramdeo", "Bhoramdeo temple", "भोरमदेव मंदिर", "भोरमदेव मंदिर", m=("Kabirdham; 11th century", "कबीरधाम; 11वीं सदी", "कबीरधाम; अकरावे शतक")),
        it3("rajim", "Rajim", "राजिम", "राजिम", m=("Rajiv Lochan temple; triveni sangam", "राजीव लोचन मंदिर; त्रिवेणी संगम", "राजीव लोचन मंदिर; त्रिवेणी संगम")),
        it3("ratanpur", "Ratanpur", "रतनपुर", "रतनपूर", m=("Kalachuri capital; Mahamaya temple", "कलचुरि राजधानी; महामाया मंदिर", "कलचुरी राजधानी; महामाया मंदिर")),
        it3("danteshwari", "Danteshwari temple, Dantewada", "दंतेश्वरी मंदिर, दंतेवाड़ा", "दंतेश्वरी मंदिर, दंतेवाडा", m=("Shakti peetha of Bastar", "बस्तर का शक्तिपीठ", "बस्तरचे शक्तिपीठ")),
        it3("tala", "Tala (Devrani–Jethani temples)", "ताला (देवरानी–जेठानी मंदिर)", "ताला (देवराणी–जेठाणी मंदिरे)", m=("Bilaspur; early temples", "बिलासपुर; प्रारंभिक मंदिर", "बिलासपूर; प्रारंभीची मंदिरे")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("ct mod1 ok")
