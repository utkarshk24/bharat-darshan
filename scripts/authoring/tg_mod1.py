"""Telangana modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-TG"
MSME = "https://dcmsme.gov.in/old/dips/state_wise_dips/TS-Profile.pdf"
SEO = "https://data.opencity.in/dataset/349ae865-f062-43bb-8495-07e47dbe797e/resource/38798379-3ef3-4d14-a359-24618bc06fdf/download/telangana-socio-economic-outlook-2024.pdf"
tg = read("regions/IN-TG.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Telangana, India's youngest State, was formed on 2 June 2014 from the north-western districts of Andhra Pradesh. It lies on the Deccan plateau, crossed by the Godavari and the Krishna, and had 3.50 crore people at the 2011 Census on about 1.12 lakh km². Hyderabad, the capital, is one of India's largest cities and a centre of information technology, pharmaceuticals and research; Warangal, Karimnagar, Nizamabad and Khammam are the other main towns.\n\nMost of the region was part of the princely State of Hyderabad, ruled by the Nizams until 1948. It joined Andhra State in 1956 to form Andhra Pradesh, and a long movement for a separate State led to the creation of Telangana. Telugu is the main language, and Urdu is widely spoken.",
        "भारत का सबसे नया राज्य तेलंगाना 2 जून 2014 को आंध्र प्रदेश के उत्तर-पश्चिमी ज़िलों से बना। यह दक्कन के पठार पर है, जिसे गोदावरी और कृष्णा पार करती हैं, और 2011 की जनगणना में लगभग 1.12 लाख वर्ग किमी पर यहाँ 3.50 करोड़ लोग थे। राजधानी हैदराबाद भारत के सबसे बड़े शहरों में है और सूचना प्रौद्योगिकी, दवा उद्योग और शोध का केंद्र है; वारंगल, करीमनगर, निज़ामाबाद और खम्मम अन्य प्रमुख नगर हैं।\n\nइस क्षेत्र का अधिकांश भाग हैदराबाद रियासत का हिस्सा था, जिस पर 1948 तक निज़ामों का शासन रहा। 1956 में यह आंध्र राज्य के साथ मिलकर आंध्र प्रदेश बना, और अलग राज्य के लंबे आंदोलन से तेलंगाना का गठन हुआ। तेलुगु मुख्य भाषा है, और उर्दू व्यापक रूप से बोली जाती है।",
        "भारतातील सर्वांत नवे राज्य तेलंगणा 2 जून 2014 रोजी आंध्र प्रदेशच्या वायव्येकडील जिल्ह्यांतून स्थापन झाले. ते दख्खनच्या पठारावर असून त्यातून गोदावरी व कृष्णा वाहतात, आणि 2011 च्या जनगणनेनुसार सुमारे 1.12 लाख चौ.किमी क्षेत्रावर 3.50 कोटी लोक होते. राजधानी हैदराबाद हे भारतातील सर्वांत मोठ्या शहरांपैकी एक असून माहिती तंत्रज्ञान, औषधनिर्मिती व संशोधनाचे केंद्र आहे; वरंगळ, करीमनगर, निजामाबाद व खम्मम ही इतर प्रमुख शहरे आहेत.\n\nया प्रदेशाचा बहुतांश भाग हैदराबाद संस्थानाचा होता, ज्यावर 1948 पर्यंत निजामांचे राज्य होते. 1956 मध्ये तो आंध्र राज्यासोबत एकत्र होऊन आंध्र प्रदेश बनला, आणि स्वतंत्र राज्यासाठीच्या दीर्घ आंदोलनातून तेलंगणाची निर्मिती झाली. तेलुगु ही मुख्य भाषा आहे, आणि उर्दू मोठ्या प्रमाणावर बोलली जाते."),
        sources=["msme-di", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Telangana combines the old city of Hyderabad — the Charminar, the Golconda fort, the Qutb Shahi tombs, biryani and haleem — with one of India's biggest technology hubs at HITEC City and Gachibowli. The Kakatiya temple at Ramappa is a UNESCO World Heritage Site. The State's own festivals, Bathukamma and Bonalu, and the Sammakka–Saralamma jatara at Medaram, one of the largest tribal gatherings in India, are celebrated with great energy. Pochampally ikat, Gadwal and Narayanpet saris, Cheriyal scroll paintings and Karimnagar silver filigree are well-known crafts.",
        "तेलंगाना हैदराबाद के पुराने शहर — चारमीनार, गोलकुंडा क़िला, क़ुतुबशाही मक़बरे, बिरयानी और हलीम — को हाईटेक सिटी और गच्चीबौली में भारत के सबसे बड़े प्रौद्योगिकी केंद्रों में से एक के साथ जोड़ता है। रामप्पा का काकतीय मंदिर यूनेस्को विश्व धरोहर स्थल है। राज्य के अपने त्योहार बतुकम्मा और बोनालु, और मेडारम का सम्मक्का–सारलम्मा जातरा, जो भारत के सबसे बड़े आदिवासी समागमों में है, बड़े उत्साह से मनाए जाते हैं। पोचमपल्ली इकत, गदवाल और नारायणपेट साड़ियाँ, चेरियाल पट-चित्र और करीमनगर की चाँदी की तारकशी प्रसिद्ध शिल्प हैं।",
        "तेलंगणा हैदराबादच्या जुन्या शहराला — चारमिनार, गोवळकोंडा किल्ला, कुतुबशाही कबरी, बिर्याणी व हलीम — हायटेक सिटी व गच्चीबावली येथील भारतातील सर्वांत मोठ्या तंत्रज्ञान केंद्रांपैकी एकाशी जोडते. रामप्पा येथील काकतीय मंदिर युनेस्को जागतिक वारसा स्थळ आहे. राज्याचे स्वतःचे सण बतुकम्मा व बोनालू, आणि मेडारमची सम्मक्का–सारलम्मा जत्रा — भारतातील सर्वांत मोठ्या आदिवासी मेळाव्यांपैकी एक — मोठ्या उत्साहाने साजरे होतात. पोचमपल्ली इकत, गदवाल व नारायणपेठ साड्या, चेरियाल पटचित्रे व करीमनगरचे चांदीचे तारकाम ही प्रसिद्ध हस्तकला आहे."),
        title=L("What makes Telangana unique?", "तेलंगाना को ख़ास क्या बनाता है?", "तेलंगणाचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed", "गठन", "निर्मिती"), L("2 June 2014 (Andhra Pradesh Reorganisation Act, 2014)", "2 जून 2014 (आंध्र प्रदेश पुनर्गठन अधिनियम, 2014)", "2 जून 2014 (आंध्र प्रदेश पुनर्रचना अधिनियम, 2014)")],
           [L("Districts / mandals", "ज़िले / मंडल", "जिल्हे / मंडळे"), "33 / 620"],
           [L("Gram panchayats", "ग्राम पंचायतें", "ग्रामपंचायती"), "12,769"],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Telugu; Urdu as second official language", "तेलुगु; उर्दू दूसरी राजभाषा", "तेलुगु; उर्दू दुसरी राजभाषा")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("High Court for the State of Telangana, Hyderabad", "तेलंगाना राज्य उच्च न्यायालय, हैदराबाद", "तेलंगणा राज्य उच्च न्यायालय, हैदराबाद")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-TG / TG"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          "tg-plan", SEO, conf="Official",
          note=L("Districts, mandals and gram panchayats from the Telangana Socio Economic Outlook 2024; other rows editorial.",
                 "ज़िले, मंडल और ग्राम पंचायतें तेलंगाना सामाजिक-आर्थिक परिदृश्य 2024 से; अन्य पंक्तियाँ संपादकीय।",
                 "जिल्हे, मंडळे व ग्रामपंचायती तेलंगणा सामाजिक-आर्थिक आढावा 2024 मधून; इतर ओळी संपादकीय.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Telangana is a land-locked State on the Deccan plateau, mostly between 300 and 700 m above sea level, with rolling granite country, thousands of man-made tanks and scattered hills. The Godavari enters from Maharashtra in the north and flows south-east past Bhadrachalam; the Krishna forms much of the southern boundary with Andhra Pradesh. Their tributaries — the Manjira, Pranhita, Musi and others — drain the plateau. Dense forests cover the north and east, in Adilabad, Kumuram Bheem Asifabad, Mulugu and Bhadradri Kothagudem, and the Nallamala hills in the south. Hyderabad stands on the Musi, around the lakes of Hussain Sagar, Osman Sagar and Himayat Sagar.",
        "तेलंगाना दक्कन के पठार पर एक भू-आबद्ध राज्य है, जो अधिकतर समुद्र तल से 300 से 700 मीटर ऊँचा है, जहाँ लहरदार ग्रेनाइट भूमि, हज़ारों मानव-निर्मित तालाब और बिखरी पहाड़ियाँ हैं। गोदावरी उत्तर में महाराष्ट्र से आती है और भद्राचलम से होकर दक्षिण-पूर्व बहती है; कृष्णा आंध्र प्रदेश के साथ दक्षिणी सीमा का बड़ा भाग बनाती है। इनकी सहायक नदियाँ — मंजीरा, प्राणहिता, मूसी और अन्य — पठार का जल बहाती हैं। उत्तर और पूर्व में आदिलाबाद, कुमुरम भीम आसिफ़ाबाद, मुलुगु और भद्राद्रि कोठागुडेम में, और दक्षिण में नल्लमला पहाड़ियों में घने वन हैं। हैदराबाद मूसी के किनारे हुसैन सागर, उस्मान सागर और हिमायत सागर झीलों के आसपास बसा है।",
        "तेलंगणा हे दख्खनच्या पठारावरील भूवेष्टित राज्य असून बहुतांश समुद्रसपाटीपासून 300 ते 700 मीटर उंचीवर आहे — लहरी ग्रॅनाइटचा प्रदेश, हजारो मानवनिर्मित तलाव व विखुरलेले डोंगर. गोदावरी उत्तरेला महाराष्ट्रातून येते आणि भद्राचलमवरून आग्नेयेकडे वाहते; कृष्णा आंध्र प्रदेशसोबतच्या दक्षिण सीमेचा मोठा भाग बनवते. त्यांच्या उपनद्या — मांजरा, प्राणहिता, मुसी व इतर — पठाराचे पाणी वाहून नेतात. उत्तर व पूर्वेला आदिलाबाद, कुमुरम भीम आसिफाबाद, मुलुगू व भद्राद्री कोठागुडेममध्ये, आणि दक्षिणेला नल्लमला डोंगरांत घनदाट जंगले आहेत. हैदराबाद मुसीकाठी हुसेन सागर, उस्मान सागर व हिमायत सागर तलावांभोवती वसले आहे."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), tg["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("mh", "Maharashtra (north and north-west)", "महाराष्ट्र (उत्तर और उत्तर-पश्चिम)", "महाराष्ट्र (उत्तर व वायव्य)"), it3("ct", "Chhattisgarh (north-east)", "छत्तीसगढ़ (उत्तर-पूर्व)", "छत्तीसगड (ईशान्य)"),
        it3("ap", "Andhra Pradesh (east and south)", "आंध्र प्रदेश (पूर्व और दक्षिण)", "आंध्र प्रदेश (पूर्व व दक्षिण)"), it3("ka", "Karnataka (west)", "कर्नाटक (पश्चिम)", "कर्नाटक (पश्चिम)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("godavari", "Godavari", "गोदावरी", "गोदावरी", d=("Flows across the north past Basar, Kaleshwaram and Bhadrachalam.", "उत्तर में बासर, कालेश्वरम और भद्राचलम से होकर बहती है।", "उत्तरेत बासर, कालेश्वरम व भद्राचलमवरून वाहते.")),
        it3("krishna", "Krishna", "कृष्णा", "कृष्णा", d=("Southern border river; Nagarjuna Sagar and Srisailam dams.", "दक्षिणी सीमा की नदी; नागार्जुन सागर और श्रीशैलम बाँध।", "दक्षिण सीमेवरील नदी; नागार्जुन सागर व श्रीशैलम धरणे.")),
        it3("manjira", "Manjira", "मंजीरा", "मांजरा", d=("Godavari tributary supplying water to Hyderabad.", "गोदावरी की सहायक नदी, जो हैदराबाद को पानी देती है।", "गोदावरीची उपनदी, हैदराबादला पाणी देते.")),
        it3("musi", "Musi", "मूसी", "मुसी", d=("Krishna tributary flowing through Hyderabad.", "कृष्णा की सहायक नदी, जो हैदराबाद से होकर बहती है।", "कृष्णेची उपनदी, हैदराबादमधून वाहते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point — official elevation", "सर्वोच्च बिंदु — आधिकारिक ऊँचाई", "सर्वोच्च शिखर — अधिकृत उंची"), "survey-of-india", "Survey of India or the State gazetteer."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Telangana has a semi-arid tropical climate. Summers from March to early June are very hot — the northern districts such as Adilabad, Ramagundam and Bhadrachalam often pass 45 °C — while Hyderabad, on higher ground, is a little milder. The south-west monsoon brings most of the year's rain between June and September, heavier in the north and east and lighter in the south-west. Winters from November to February are dry and pleasant, with cool nights.",
        "तेलंगाना में अर्ध-शुष्क उष्णकटिबंधीय जलवायु है। मार्च से जून की शुरुआत तक गर्मियाँ बहुत गर्म होती हैं — आदिलाबाद, रामागुंडम और भद्राचलम जैसे उत्तरी ज़िलों में तापमान अक्सर 45 °C पार कर जाता है — जबकि ऊँचाई पर बसा हैदराबाद थोड़ा कम गर्म है। दक्षिण-पश्चिम मानसून जून से सितंबर के बीच साल की अधिकांश वर्षा लाता है, जो उत्तर और पूर्व में अधिक और दक्षिण-पश्चिम में कम होती है। नवंबर से फ़रवरी तक सर्दियाँ सूखी और सुहावनी होती हैं, और रातें ठंडी।",
        "तेलंगणात अर्ध-शुष्क उष्णकटिबंधीय हवामान आहे. मार्च ते जूनच्या सुरुवातीपर्यंत उन्हाळा अतिशय उष्ण असतो — आदिलाबाद, रामगुंडम व भद्राचलमसारख्या उत्तरेकडील जिल्ह्यांत तापमान अनेकदा 45 °C ओलांडते — तर उंचावरील हैदराबाद थोडे सौम्य असते. नैर्ऋत्य मान्सून जून ते सप्टेंबरदरम्यान वर्षाचा बहुतांश पाऊस आणतो — उत्तर व पूर्वेत जास्त, नैर्ऋत्येत कमी. नोव्हेंबर ते फेब्रुवारी हिवाळा कोरडा व सुखद असतो, आणि रात्री थंड."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Hyderabad", "हैदराबाद", "हैदराबाद"), "lat": 17.3850, "lon": 78.4867},
        {"name": L("Warangal", "वारंगल", "वरंगळ"), "lat": 17.9689, "lon": 79.5941},
        {"name": L("Adilabad", "आदिलाबाद", "आदिलाबाद"), "lat": 19.6641, "lon": 78.5320},
        {"name": L("Bhadrachalam", "भद्राचलम", "भद्राचलम"), "lat": 17.6688, "lon": 80.8936},
    ]},
    lst("best", [
        it3("winter", "October to February", "अक्टूबर से फ़रवरी", "ऑक्टोबर ते फेब्रुवारी", d=("Best for Hyderabad's monuments and Warangal; Bathukamma and Dasara in autumn.", "हैदराबाद के स्मारकों और वारंगल के लिए सबसे अच्छा; शरद में बतुकम्मा और दशहरा।", "हैदराबादची स्मारके व वरंगळसाठी उत्तम; शरद ऋतूत बतुकम्मा व दसरा.")),
        it3("summer", "March to May", "मार्च से मई", "मार्च ते मे", d=("Very hot; Hyderabad's mango season.", "बहुत गर्म; हैदराबाद में आम का मौसम।", "अतिशय उष्ण; हैदराबादमध्ये आंब्यांचा हंगाम.")),
        it3("monsoon", "June to September", "जून से सितंबर", "जून ते सप्टेंबर", d=("Waterfalls in Adilabad (Kuntala, Pochera); Bonalu in July–August.", "आदिलाबाद में झरने (कुंटाला, पोचेरा); जुलाई–अगस्त में बोनालु।", "आदिलाबादमध्ये धबधबे (कुंटाला, पोचेरा); जुलै–ऑगस्टमध्ये बोनालू.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (Telangana sub-division)", "सामान्य वार्षिक वर्षा (तेलंगाना उप-मंडल)", "सरासरी वार्षिक पाऊस (तेलंगणा उपविभाग)"), "imd", "IMD rainfall statistics."),
        (L("Heatwave days by year", "वर्षवार लू के दिन", "वर्षनिहाय उष्णतेच्या लाटेचे दिवस"), "imd", "IMD heatwave records."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Hyderabad has two faces. The old city around the Charminar is a place of bazaars selling bangles, pearls and attar, Irani cafés serving chai and Osmania biscuits, and long evenings of biryani and, in Ramzan, haleem. The new city to the west — HITEC City, Gachibowli and the Financial District — is a world of glass towers, start-ups and global technology offices. Dakhni, the local mix of Urdu and Telugu, is heard everywhere. Outside the capital, life follows the tanks, paddy and cotton fields of the plateau, and villages come alive for Bathukamma, when women build towers of flowers and dance around them.",
        "हैदराबाद के दो चेहरे हैं। चारमीनार के आसपास का पुराना शहर चूड़ियों, मोतियों और इत्र के बाज़ारों, चाय और उस्मानिया बिस्कुट परोसने वाले ईरानी कैफ़े, और बिरयानी की — और रमज़ान में हलीम की — लंबी शामों की जगह है। पश्चिम का नया शहर — हाईटेक सिटी, गच्चीबौली और फ़ाइनेंशियल डिस्ट्रिक्ट — काँच की इमारतों, स्टार्टअप और वैश्विक प्रौद्योगिकी दफ़्तरों की दुनिया है। उर्दू और तेलुगु का स्थानीय मेल दक्खिनी हर जगह सुनाई देता है। राजधानी से बाहर जीवन पठार के तालाबों, धान और कपास के खेतों के साथ चलता है, और बतुकम्मा पर गाँव जीवंत हो उठते हैं, जब महिलाएँ फूलों के गोपुर बनाकर उनके चारों ओर नाचती हैं।",
        "हैदराबादचे दोन चेहरे आहेत. चारमिनारभोवतीचे जुने शहर बांगड्या, मोती व अत्तराचे बाजार, चहा व उस्मानिया बिस्किटे देणारे इराणी कॅफे, आणि बिर्याणीच्या — व रमजानमध्ये हलीमच्या — लांब संध्याकाळींचे ठिकाण आहे. पश्चिमेकडील नवे शहर — हायटेक सिटी, गच्चीबावली व फायनान्शियल डिस्ट्रिक्ट — काचेच्या इमारती, स्टार्टअप व जागतिक तंत्रज्ञान कार्यालयांचे जग आहे. उर्दू व तेलुगुचे स्थानिक मिश्रण दख्खनी सर्वत्र ऐकू येते. राजधानीबाहेर जीवन पठारावरील तलाव, भात व कापसाच्या शेतांच्या लयीत चालते, आणि बतुकम्माला गावे जिवंत होतात, जेव्हा स्त्रिया फुलांचे मनोरे रचून त्यांच्याभोवती नाचतात."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Counted for its present area, Telangana had 3.50 crore people at the 2011 Census, with a density of about 312 per km². The sex ratio was 988 women per 1,000 men and the child sex ratio 932. Literacy was 66.5% (men 75.0%, women 58.0%), below the national 73.0%. About 38.9% of people lived in towns and cities — a high share, owing to Hyderabad. Scheduled Castes made up about 15.5% of the population and Scheduled Tribes about 9.1%, among them Lambadas, Koyas and Gonds.\n\nTelugu is the language of most people, and Urdu — especially the Dakhni of Hyderabad — is spoken by many. Lambadi, Gondi and Koya are spoken in tribal areas, and Marathi and Kannada along the western borders.",
        "वर्तमान क्षेत्र के अनुसार गिनने पर, 2011 की जनगणना में तेलंगाना की जनसंख्या 3.50 करोड़ थी, और घनत्व लगभग 312 प्रति वर्ग किमी। लिंगानुपात प्रति 1,000 पुरुषों पर 988 महिलाएँ और शिशु लिंगानुपात 932 था। साक्षरता 66.5% (पुरुष 75.0%, महिलाएँ 58.0%) थी, जो राष्ट्रीय 73.0% से कम है। लगभग 38.9% लोग कस्बों और शहरों में रहते थे — हैदराबाद के कारण ऊँचा हिस्सा। अनुसूचित जातियाँ जनसंख्या का लगभग 15.5% और अनुसूचित जनजातियाँ लगभग 9.1% थीं, जिनमें लंबाडा, कोया और गोंड शामिल हैं।\n\nअधिकांश लोग तेलुगु बोलते हैं, और बहुत से लोग उर्दू — विशेषकर हैदराबाद की दक्खिनी — बोलते हैं। आदिवासी क्षेत्रों में लंबाडी, गोंडी और कोया, और पश्चिमी सीमाओं पर मराठी और कन्नड़ बोली जाती हैं।",
        "सध्याच्या क्षेत्रानुसार मोजल्यास, 2011 च्या जनगणनेत तेलंगणाची लोकसंख्या 3.50 कोटी होती, आणि घनता सुमारे 312 प्रति चौ.किमी. दर 1,000 पुरुषांमागे 988 स्त्रिया व बाल लिंग गुणोत्तर 932 होते. साक्षरता 66.5% (पुरुष 75.0%, स्त्रिया 58.0%) होती, राष्ट्रीय 73.0% पेक्षा कमी. सुमारे 38.9% लोक शहरांत राहत होते — हैदराबादमुळे मोठा वाटा. अनुसूचित जाती लोकसंख्येच्या सुमारे 15.5% व अनुसूचित जमाती सुमारे 9.1% होत्या, ज्यांत लंबाडा, कोया व गोंड यांचा समावेश आहे.\n\nबहुसंख्य लोक तेलुगु बोलतात, आणि अनेक जण उर्दू — विशेषतः हैदराबादची दख्खनी — बोलतात. आदिवासी भागांत लंबाडी, गोंडी व कोया, आणि पश्चिम सीमेवर मराठी व कन्नड बोलल्या जातात."),
        sources=["msme-di", "census"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), tg["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), tg["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"]),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), tg["childSexRatio2011"], "ratio", "higher-is-better", national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), tg["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("urb", L("Urban population share", "शहरी जनसंख्या का हिस्सा", "नागरी लोकसंख्येचा वाटा"), tg["urbanisation2011"], "percent"),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), tg["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(15.45, "%", "2011", "census", "msme-di", MSME, note="Calculated: 54,08,800 SC persons ÷ 3,50,03,674 (Census 2011)."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(9.08, "%", "2011", "census", "msme-di", MSME, note="Calculated: 31,77,940 ST persons ÷ 3,50,03,674 (Census 2011)."), "percent"),
        fact("growth", L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"),
             dp(13.58, "%", "2011", "census", "msme-di", MSME, note="Growth between the 2001 and 2011 Censuses, as given in the MSME-DI State Profile."), "percent"),
    ], title=L("Census 2011 at a glance (present area)", "जनगणना 2011 एक नज़र में (वर्तमान क्षेत्र)", "जनगणना 2011 दृष्टिक्षेपात (सध्याचे क्षेत्र)")),
    lst("langs", [
        it3("te", "Telugu", "तेलुगु", "तेलुगु", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("ur", "Urdu (Dakhni)", "उर्दू (दक्खिनी)", "उर्दू (दख्खनी)", m=("Second official language", "दूसरी राजभाषा", "दुसरी राजभाषा")),
        it3("lmn", "Lambadi", "लंबाडी", "लंबाडी"), it3("gon", "Gondi", "गोंडी", "गोंडी"), it3("koya", "Koya", "कोया", "कोया"),
        it3("mr", "Marathi", "मराठी", "मराठी"), it3("kn", "Kannada", "कन्नड़", "कन्नड"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table recast for Telangana; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "The Satavahanas ruled the region in early centuries; Kotilingala on the Godavari is among their oldest sites. The Kakatiya dynasty (12th–14th centuries) made Warangal its capital and built the Thousand Pillar temple, the Ramappa temple and thousands of irrigation tanks. After the Bahmani sultanate, the Qutb Shahi dynasty ruled from Golconda and founded Hyderabad in 1591, building the Charminar. The Mughals took Golconda in 1687, and from 1724 the Asaf Jahi Nizams ruled Hyderabad State, the most populous princely State in India.\n\nThe Telangana armed struggle of the 1940s rose against feudal landlords. Hyderabad State was integrated into India after a police action in September 1948. In 1956 its Telugu-speaking districts were joined with Andhra State to form Andhra Pradesh. Demands for a separate Telangana — strong in 1969 and revived from 2001 under the Telangana Rashtra Samithi led by K. Chandrashekar Rao — led Parliament to pass the Andhra Pradesh Reorganisation Act, and Telangana became a State on 2 June 2014. Hyderabad served as a common capital of both States until 2024.",
        "आरंभिक सदियों में इस क्षेत्र पर सातवाहनों का शासन था; गोदावरी पर कोटिलिंगाला उनके सबसे पुराने स्थलों में है। काकतीय वंश (12वीं–14वीं सदी) ने वारंगल को राजधानी बनाया और हज़ार स्तंभ मंदिर, रामप्पा मंदिर और हज़ारों सिंचाई तालाब बनवाए। बहमनी सल्तनत के बाद क़ुतुबशाही वंश ने गोलकुंडा से शासन किया और 1591 में हैदराबाद बसाकर चारमीनार बनवाई। 1687 में मुग़लों ने गोलकुंडा जीता, और 1724 से आसफ़जाही निज़ामों ने हैदराबाद रियासत पर शासन किया, जो भारत की सबसे अधिक आबादी वाली रियासत थी।\n\n1940 के दशक का तेलंगाना सशस्त्र संघर्ष सामंती ज़मींदारों के विरुद्ध उठा। सितंबर 1948 में पुलिस कार्रवाई के बाद हैदराबाद रियासत का भारत में विलय हुआ। 1956 में इसके तेलुगु-भाषी ज़िलों को आंध्र राज्य से जोड़कर आंध्र प्रदेश बनाया गया। अलग तेलंगाना की माँग — 1969 में प्रबल, और 2001 से के. चंद्रशेखर राव के नेतृत्व वाली तेलंगाना राष्ट्र समिति के साथ फिर उभरी — के बाद संसद ने आंध्र प्रदेश पुनर्गठन अधिनियम पारित किया, और 2 जून 2014 को तेलंगाना राज्य बना। हैदराबाद 2024 तक दोनों राज्यों की साझा राजधानी रहा।",
        "सुरुवातीच्या शतकांत या प्रदेशावर सातवाहनांचे राज्य होते; गोदावरीवरील कोटिलिंगाला हे त्यांच्या सर्वांत जुन्या स्थळांपैकी आहे. काकतीय घराण्याने (बारावे–चौदावे शतक) वरंगळला राजधानी केले आणि हजार खांबी मंदिर, रामप्पा मंदिर व हजारो सिंचन तलाव बांधले. बहमनी सुलतानशाहीनंतर कुतुबशाही घराण्याने गोवळकोंड्याहून राज्य केले आणि 1591 मध्ये हैदराबाद वसवून चारमिनार बांधला. 1687 मध्ये मुघलांनी गोवळकोंडा जिंकला, आणि 1724 पासून आसफजाही निजामांनी हैदराबाद संस्थानावर राज्य केले — भारतातील सर्वाधिक लोकसंख्येचे संस्थान.\n\n1940 च्या दशकातील तेलंगणा सशस्त्र लढा सरंजामी जमीनदारांविरुद्ध उभा राहिला. सप्टेंबर 1948 मध्ये पोलीस कारवाईनंतर हैदराबाद संस्थान भारतात विलीन झाले. 1956 मध्ये त्याचे तेलुगुभाषक जिल्हे आंध्र राज्याला जोडून आंध्र प्रदेश बनवले गेले. स्वतंत्र तेलंगणाची मागणी — 1969 मध्ये प्रबळ, आणि 2001 पासून के. चंद्रशेखर राव यांच्या नेतृत्वाखालील तेलंगणा राष्ट्र समितीसह पुन्हा उभी — यानंतर संसदेने आंध्र प्रदेश पुनर्रचना अधिनियम मंजूर केला, आणि 2 जून 2014 रोजी तेलंगणा राज्य बनले. हैदराबाद 2024 पर्यंत दोन्ही राज्यांची सामायिक राजधानी होती."),
        conf="Editorial"),
    timeline([
        ev("kakatiya", 1163, L("c. 1163", "लगभग 1163", "सुमारे 1163"), L("Kakatiya rule from Warangal (Hanamkonda)", "वारंगल (हनमकोंडा) से काकतीय शासन", "वरंगळ (हनमकोंडा) येथून काकतीय राजवट")),
        ev("ramappa", 1213, L("1213", "1213", "1213"), L("Ramappa (Rudreshwara) temple built", "रामप्पा (रुद्रेश्वर) मंदिर का निर्माण", "रामप्पा (रुद्रेश्वर) मंदिराची उभारणी")),
        ev("hyderabad", 1591, L("1591", "1591", "1591"), L("Hyderabad founded; Charminar built", "हैदराबाद की स्थापना; चारमीनार का निर्माण", "हैदराबादची स्थापना; चारमिनारची उभारणी")),
        ev("nizam", 1724, L("1724", "1724", "1724"), L("Asaf Jahi Nizams begin to rule Hyderabad State", "आसफ़जाही निज़ामों का हैदराबाद रियासत पर शासन आरंभ", "आसफजाही निजामांची हैदराबाद संस्थानावर राजवट सुरू")),
        ev("polo", 1948, L("September 1948", "सितंबर 1948", "सप्टेंबर 1948"), L("Hyderabad State integrated into India", "हैदराबाद रियासत का भारत में विलय", "हैदराबाद संस्थान भारतात विलीन")),
        ev("ap", 1956, L("1 November 1956", "1 नवंबर 1956", "1 नोव्हेंबर 1956"), L("Merged into Andhra Pradesh", "आंध्र प्रदेश में विलय", "आंध्र प्रदेशात विलीनीकरण")),
        ev("agitation", 1969, L("1969", "1969", "1969"), L("Movement for a separate Telangana", "अलग तेलंगाना का आंदोलन", "स्वतंत्र तेलंगणाचे आंदोलन")),
        ev("state", 2014, L("2 June 2014", "2 जून 2014", "2 जून 2014"), L("Telangana becomes India's 29th State", "तेलंगाना भारत का 29वाँ राज्य बना", "तेलंगणा भारताचे 29 वे राज्य")),
        ev("unesco", 2021, L("2021", "2021", "2021"), L("Ramappa temple inscribed as a UNESCO World Heritage Site", "रामप्पा मंदिर यूनेस्को विश्व धरोहर स्थल घोषित", "रामप्पा मंदिर युनेस्को जागतिक वारसा स्थळ घोषित")),
    ]),
    lst("heritage", [
        it3("ramappa", "Kakatiya Rudreshwara (Ramappa) Temple", "काकतीय रुद्रेश्वर (रामप्पा) मंदिर", "काकतीय रुद्रेश्वर (रामप्पा) मंदिर", m=("UNESCO 2021", "यूनेस्को 2021", "युनेस्को 2021"), url=UNESCO, src="unesco-whc"),
        it3("charminar", "Charminar", "चारमीनार", "चारमिनार", m=("1591", "1591", "1591")),
        it3("golconda", "Golconda Fort", "गोलकुंडा क़िला", "गोवळकोंडा किल्ला", m=("Qutb Shahi capital", "क़ुतुबशाही राजधानी", "कुतुबशाही राजधानी")),
        it3("tombs", "Qutb Shahi tombs", "क़ुतुबशाही मक़बरे", "कुतुबशाही कबरी", m=("Hyderabad", "हैदराबाद", "हैदराबाद")),
        it3("thousand", "Thousand Pillar Temple and Warangal Fort", "हज़ार स्तंभ मंदिर और वारंगल क़िला", "हजार खांबी मंदिर व वरंगळ किल्ला", m=("Kakatiya", "काकतीय", "काकतीय")),
        it3("chowmahalla", "Chowmahalla Palace", "चौमहल्ला पैलेस", "चौमहल्ला राजवाडा", m=("Nizams' palace", "निज़ामों का महल", "निजामांचा राजवाडा")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("tg mod1 ok")
