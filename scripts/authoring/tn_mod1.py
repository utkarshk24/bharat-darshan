"""Tamil Nadu modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-TN"
TN23 = "https://des.tn.gov.in/sites/default/files/2024-01/At_a_glance_%2029_12_2023.pdf"
tn = read("regions/IN-TN.json")["metrics"]; ind = read("india.json")["metrics"]
NAME = L("Tamil Nadu", "तमिलनाडु", "तमिळनाडू")
TND = lambda v, unit, note=None, period="2011", ptype="census", src="census": dp(v, unit, period, ptype, src, TN23, note=note)

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Tamil Nadu occupies the south-eastern tip of the Indian peninsula, facing the Bay of Bengal on the east and the Indian Ocean at Kanniyakumari. The fertile Kaveri delta, dry interior plains, the Nilgiri and Palani hills of the Western Ghats and a coastline of 1,076 km give it unusual variety. Chennai, the capital, is one of India's largest metropolitan areas and a centre for cars, electronics, software and healthcare.\n\nThe State took its present boundaries in 1956, when Telugu- and Malayalam-speaking areas of Madras State were reorganised on linguistic lines, and was renamed Tamil Nadu — \"the land of the Tamils\" — in 1969. Tamil, one of the world's oldest living classical languages, is the official language.",
        "तमिलनाडु भारतीय प्रायद्वीप के दक्षिण-पूर्वी छोर पर है — पूर्व में बंगाल की खाड़ी और कन्याकुमारी पर हिंद महासागर। उपजाऊ कावेरी डेल्टा, सूखे भीतरी मैदान, पश्चिमी घाट की नीलगिरि और पलनी पहाड़ियाँ और 1,076 किमी की तटरेखा इसे असाधारण विविधता देती हैं। राजधानी चेन्नई भारत के सबसे बड़े महानगरीय क्षेत्रों में है और कार, इलेक्ट्रॉनिक्स, सॉफ़्टवेयर और स्वास्थ्य सेवाओं का केंद्र है।\n\nराज्य को अपनी वर्तमान सीमाएँ 1956 में मिलीं, जब मद्रास राज्य के तेलुगु और मलयालम भाषी क्षेत्रों का भाषाई आधार पर पुनर्गठन हुआ, और 1969 में इसका नाम तमिलनाडु — \"तमिलों की भूमि\" — रखा गया। विश्व की सबसे पुरानी जीवित शास्त्रीय भाषाओं में से एक, तमिल, राजभाषा है।",
        "तमिळनाडू भारतीय द्वीपकल्पाच्या आग्नेय टोकावर आहे — पूर्वेला बंगालचा उपसागर आणि कन्याकुमारीला हिंदी महासागर. सुपीक कावेरी त्रिभुज प्रदेश, कोरडी अंतर्गत मैदाने, पश्चिम घाटातील निलगिरी व पळनी डोंगर आणि 1,076 किमीची किनारपट्टी यांमुळे राज्यात विलक्षण विविधता आहे. राजधानी चेन्नई हे भारतातील सर्वांत मोठ्या महानगरांपैकी एक असून मोटारी, इलेक्ट्रॉनिक्स, सॉफ्टवेअर आणि आरोग्यसेवांचे केंद्र आहे.\n\n1956 मध्ये मद्रास राज्यातील तेलुगू व मल्याळम भाषिक प्रदेशांची भाषिक आधारावर पुनर्रचना झाल्यावर राज्याला सध्याच्या सीमा मिळाल्या, आणि 1969 मध्ये त्याचे नाव तमिळनाडू — \"तमिळांची भूमी\" — ठेवण्यात आले. जगातील सर्वांत प्राचीन जिवंत अभिजात भाषांपैकी एक असलेली तमिळ ही राजभाषा आहे."),
        sources=["tn-des"], conf="Editorial"),
    prose("intro-unique", L(
        "Few places hold so much continuous history in daily use. Temples built by the Pallavas, Cholas and Pandyas a thousand years ago still hold festivals; Sangam poetry composed some two thousand years ago is taught in schools; and Bharatanatyam and Carnatic music are performed in Chennai's December season much as they were a century ago. Tamil Nadu is also one of India's most industrialised and urbanised States, with strong public health and school-meal programmes that other States have copied. It has more Ramsar wetlands (20) than any other State.",
        "बहुत कम जगहों पर इतना निरंतर इतिहास रोज़मर्रा के जीवन में दिखता है। पल्लव, चोल और पांड्य राजाओं के हज़ार साल पहले बनाए मंदिरों में आज भी उत्सव होते हैं; लगभग दो हज़ार वर्ष पहले रचा गया संगम काव्य स्कूलों में पढ़ाया जाता है; और भरतनाट्यम व कर्नाटक संगीत चेन्नई के दिसंबर सीज़न में लगभग वैसे ही प्रस्तुत होते हैं जैसे एक सदी पहले। तमिलनाडु भारत के सबसे औद्योगिक और शहरीकृत राज्यों में भी है, जिसके सार्वजनिक स्वास्थ्य और स्कूली भोजन कार्यक्रमों को दूसरे राज्यों ने अपनाया है। यहाँ किसी भी अन्य राज्य से अधिक रामसर आर्द्रभूमियाँ (20) हैं।",
        "इतका सलग इतिहास रोजच्या जीवनात वापरात असलेली ठिकाणे फार थोडी आहेत. पल्लव, चोळ आणि पांड्य राजांनी हजार वर्षांपूर्वी बांधलेल्या मंदिरांत आजही उत्सव होतात; सुमारे दोन हजार वर्षांपूर्वी रचलेले संगम काव्य शाळांत शिकवले जाते; आणि चेन्नईच्या डिसेंबर हंगामात भरतनाट्यम व कर्नाटक संगीत जवळपास शतकापूर्वीसारखेच सादर होते. तमिळनाडू हे भारतातील सर्वाधिक औद्योगिक व नागरीकरण झालेल्या राज्यांपैकीही आहे; इथल्या सार्वजनिक आरोग्य व शालेय पोषण आहार योजनांचे अनुकरण इतर राज्यांनी केले आहे. इतर कोणत्याही राज्यापेक्षा जास्त रामसर पाणथळ स्थळे (20) इथे आहेत."),
        title=L("What makes Tamil Nadu unique?", "तमिलनाडु को ख़ास क्या बनाता है?", "तमिळनाडूचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formation (present boundaries)", "गठन (वर्तमान सीमाएँ)", "स्थापना (सध्याच्या सीमा)"), L("1 November 1956, as Madras State", "1 नवंबर 1956, मद्रास राज्य के रूप में", "1 नोव्हेंबर 1956, मद्रास राज्य म्हणून")],
           [L("Renamed", "नाम परिवर्तन", "नावबदल"), L("Tamil Nadu, 14 January 1969", "तमिलनाडु, 14 जनवरी 1969", "तमिळनाडू, 14 जानेवारी 1969")],
           [L("Districts / taluks", "ज़िले / तालुक", "जिल्हे / तालुके"), "38 / 314"],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Tamil (classical language, 2004)", "तमिल (शास्त्रीय भाषा, 2004)", "तमिळ (अभिजात भाषा, 2004)")],
           [L("Coastline", "तटरेखा", "किनारपट्टी"), "1,076 km"],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-TN / TN"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          "tn-des", TN23, conf="Editorial",
          note=L("District, taluk and coastline figures from the Tamil Nadu Department of Economics and Statistics (2022-23). Formation and renaming dates are editorial and will be linked to the notifications in review. Tamil was the first language declared classical by the Government of India (2004).",
                 "ज़िला, तालुक और तटरेखा के आँकड़े तमिलनाडु अर्थशास्त्र एवं सांख्यिकी विभाग (2022-23) से। गठन और नाम परिवर्तन की तिथियाँ संपादकीय हैं; समीक्षा में अधिसूचनाओं से जोड़ी जाएँगी। तमिल भारत सरकार द्वारा शास्त्रीय घोषित पहली भाषा थी (2004)।",
                 "जिल्हे, तालुके व किनारपट्टीचे आकडे तमिळनाडू अर्थशास्त्र व सांख्यिकी विभागाकडून (2022-23). स्थापना व नावबदलाच्या तारखा संपादकीय असून तपासणीत अधिसूचनांशी जोडल्या जातील. भारत सरकारने अभिजात घोषित केलेली तमिळ ही पहिली भाषा होती (2004).")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Tamil Nadu falls into a few broad landscapes. Along the east runs a long, low coastal plain — the Coromandel Coast — with lagoons such as Pulicat, beaches and mangroves at Pichavaram. Inland, a dry, rolling plateau of red soils and scattered rocky hills stretches to the Western Ghats, which rise along the western border into the Nilgiris, the Anamalai and the Palani hills; Doddabetta in the Nilgiris is the highest point in the State. The Eastern Ghats appear as isolated ranges — the Javadhu, Shevaroy (Yercaud) and Kolli hills.\n\nThe Kaveri is the lifeline. It enters from Karnataka, is held by the Mettur dam and fans out into a broad delta around Thanjavur, the State's historic rice bowl. Other rivers — the Vaigai, Thamirabarani, Palar and Pennaiyar — are shorter and more seasonal. At Rameswaram a chain of shoals runs towards Sri Lanka across the Palk Strait, and at Kanniyakumari three seas meet.",
        "तमिलनाडु कुछ बड़े भूदृश्यों में बँटा है। पूर्व में एक लंबा, निचला तटीय मैदान — कोरोमंडल तट — है, जिसमें पुलिकट जैसे लैगून, समुद्र तट और पिच्चावरम के मैंग्रोव हैं। भीतर की ओर लाल मिट्टी और बिखरी चट्टानी पहाड़ियों वाला सूखा, लहरदार पठार पश्चिमी घाट तक फैला है, जो पश्चिमी सीमा पर नीलगिरि, अनामलै और पलनी पहाड़ियों के रूप में उठते हैं; नीलगिरि का दोड्डाबेट्टा राज्य का सबसे ऊँचा बिंदु है। पूर्वी घाट अलग-अलग पहाड़ियों के रूप में दिखते हैं — जव्वादु, शेवरॉय (येरकॉड) और कोल्ली पहाड़ियाँ।\n\nकावेरी जीवनरेखा है। यह कर्नाटक से आती है, मेट्टूर बाँध में रोकी जाती है और तंजावुर के आसपास एक चौड़े डेल्टा में फैल जाती है, जो राज्य का ऐतिहासिक धान का कटोरा है। अन्य नदियाँ — वैगै, ताम्रपर्णी, पालार और पेन्नैयार — छोटी और अधिक मौसमी हैं। रामेश्वरम से पाक जलडमरूमध्य के पार श्रीलंका की ओर रेतीले टीलों की एक शृंखला जाती है, और कन्याकुमारी में तीन समुद्र मिलते हैं।",
        "तमिळनाडूचे काही ठळक भूप्रदेश आहेत. पूर्वेकडे लांब, सखल किनारी मैदान — कोरोमंडल किनारा — असून त्यात पुलिकतसारखे खारकच्छ, समुद्रकिनारे आणि पिच्चावरमची खारफुटी आहे. आतल्या भागात तांबड्या मातीचे, विखुरलेल्या खडकाळ टेकड्यांचे कोरडे, उंचसखल पठार पश्चिम घाटापर्यंत पसरले आहे; पश्चिम सीमेवर घाट निलगिरी, अनामलै आणि पळनी डोंगररांगांच्या रूपाने उंचावतो, आणि निलगिरीतील दोड्डाबेट्टा हे राज्यातील सर्वोच्च ठिकाण आहे. पूर्व घाट सुट्या डोंगररांगांच्या रूपात दिसतो — जव्वादू, शेवरॉय (येरकॉड) आणि कोल्ली डोंगर.\n\nकावेरी ही जीवनरेखा आहे. ती कर्नाटकातून येते, मेट्टूर धरणात अडवली जाते आणि तंजावूरभोवती विस्तीर्ण त्रिभुज प्रदेशात पसरते — राज्याचे ऐतिहासिक भाताचे कोठार. इतर नद्या — वैगै, ताम्रपर्णी, पालार आणि पेन्नैयार — लहान आणि अधिक हंगामी आहेत. रामेश्वरमपासून पाल्क सामुद्रधुनी ओलांडून श्रीलंकेकडे वाळूच्या उथळ पट्ट्यांची मालिका जाते, आणि कन्याकुमारीला तीन समुद्र मिळतात."),
        conf="Editorial"),
    facts("f", [
        fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), tn["area"], "number", national=ind["area"]),
        fact("coast", L("Coastline", "तटरेखा", "किनारपट्टी"), TND(1076, "km", "Tamil Nadu DES, 'Tamil Nadu at a Glance' (2022-23).", "FY2022-23", "fy", "tn-des"), "number"),
    ]),
    lst("neighbours", [
        it3("ap", "Andhra Pradesh (north)", "आंध्र प्रदेश (उत्तर)", "आंध्र प्रदेश (उत्तर)"), it3("ka", "Karnataka (north-west)", "कर्नाटक (उत्तर-पश्चिम)", "कर्नाटक (वायव्य)"),
        it3("kl", "Keralam (west)", "केरलम (पश्चिम)", "केरळम (पश्चिम)"), it3("py", "Puducherry (enclaves)", "पुदुच्चेरी (अंतःक्षेत्र)", "पुदुच्चेरी (परिक्षेत्रे)"),
        it3("bay", "Bay of Bengal (east)", "बंगाल की खाड़ी (पूर्व)", "बंगालचा उपसागर (पूर्व)"), it3("lk", "Sri Lanka, across the Palk Strait", "पाक जलडमरूमध्य के पार श्रीलंका", "पाल्क सामुद्रधुनीपलीकडे श्रीलंका"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("kaveri", "Kaveri (Cauvery)", "कावेरी", "कावेरी", d=("Enters from Karnataka; Mettur dam; Grand Anicut (Kallanai) near Thanjavur; feeds the delta.", "कर्नाटक से आती है; मेट्टूर बाँध; तंजावुर के पास ग्रैंड अनिकट (कल्लणै); डेल्टा को सींचती है।", "कर्नाटकातून येते; मेट्टूर धरण; तंजावूरजवळील ग्रँड अनिकट (कल्लणै); त्रिभुज प्रदेशाला पाणी देते.")),
        it3("vaigai", "Vaigai", "वैगै", "वैगै", d=("Flows past Madurai to the Palk Bay; seasonal in its lower course.", "मदुरै से होकर पाक खाड़ी तक बहती है; निचले भाग में मौसमी।", "मदुराईजवळून पाल्क उपसागराकडे वाहते; खालच्या भागात हंगामी.")),
        it3("thamirabarani", "Thamirabarani", "ताम्रपर्णी", "ताम्रपर्णी", d=("Perennial river of the far south, through Tirunelveli to the Gulf of Mannar.", "सुदूर दक्षिण की बारहमासी नदी, तिरुनेलवेली से होकर मन्नार की खाड़ी तक।", "दक्षिण टोकाची बारमाही नदी, तिरुनेलवेलीतून मन्नारच्या आखाताकडे.")),
        it3("palar", "Palar", "पालार", "पालार", d=("Northern river through Vellore and Kancheepuram; largely dry outside the monsoon.", "वेल्लोर और कांचीपुरम से होकर बहने वाली उत्तरी नदी; मानसून के बाहर अधिकतर सूखी।", "वेल्लोर व कांचीपुरममधून वाहणारी उत्तरेकडील नदी; पावसाळ्याबाहेर बहुतांश कोरडी.")),
        it3("bhavani", "Bhavani", "भवानी", "भवानी", d=("Rises in the Nilgiris; Bhavanisagar dam; joins the Kaveri at Bhavani.", "नीलगिरि से निकलती है; भवानीसागर बाँध; भवानी में कावेरी से मिलती है।", "निलगिरीत उगम; भवानीसागर धरण; भवानी येथे कावेरीला मिळते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest-point elevation (official)", "सर्वोच्च बिंदु की ऊँचाई (आधिकारिक)", "सर्वोच्च बिंदूची उंची (अधिकृत)"), "survey-of-india", "Editorial text avoids an exact figure until an official one is linked."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
        (L("Latitude and longitude extent", "अक्षांश-देशांतर विस्तार", "अक्षांश-रेखांश विस्तार"), "survey-of-india", "Survey of India or the State gazetteer."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Tamil Nadu's rainfall calendar is the reverse of most of India. The Western Ghats block much of the south-west monsoon (June–September), so the coast gets most of its rain from the north-east monsoon in October to December, often with cyclones from the Bay of Bengal. The interior gets a share of both seasons. The State's normal annual rainfall was 966.8 mm in the 2022-23 reference year of the Tamil Nadu statistics department.\n\nThe plains are hot for most of the year — April to June is the peak, with Chennai's humidity making it feel hotter — while December to February is mild and pleasant. The hill stations of Ooty (Udhagamandalam), Kodaikanal and Yercaud stay cool, with frost on some winter nights in the Nilgiris.",
        "तमिलनाडु का वर्षा कैलेंडर अधिकांश भारत से उल्टा है। पश्चिमी घाट दक्षिण-पश्चिम मानसून (जून–सितंबर) का बड़ा हिस्सा रोक लेते हैं, इसलिए तट को अधिकतर वर्षा अक्टूबर से दिसंबर में उत्तर-पूर्व मानसून से मिलती है, अक्सर बंगाल की खाड़ी के चक्रवातों के साथ। भीतरी भाग को दोनों मौसमों का हिस्सा मिलता है। तमिलनाडु सांख्यिकी विभाग के 2022-23 संदर्भ वर्ष में राज्य की सामान्य वार्षिक वर्षा 966.8 मिमी थी।\n\nमैदान साल के अधिकांश समय गर्म रहते हैं — अप्रैल से जून चरम होता है, और चेन्नई की उमस इसे और गर्म महसूस कराती है — जबकि दिसंबर से फ़रवरी हल्का और सुहावना रहता है। ऊटी (उदगमंडलम), कोडैकनाल और येरकॉड के हिल स्टेशन ठंडे रहते हैं; नीलगिरि में सर्दियों की कुछ रातों में पाला भी पड़ता है।",
        "तमिळनाडूचे पावसाचे वेळापत्रक बहुतांश भारताच्या उलट आहे. पश्चिम घाट नैर्ऋत्य मोसमी पावसाचा (जून–सप्टेंबर) मोठा भाग अडवतो, त्यामुळे किनारपट्टीला बहुतेक पाऊस ऑक्टोबर ते डिसेंबरदरम्यान ईशान्य मोसमी वाऱ्यांपासून मिळतो — अनेकदा बंगालच्या उपसागरातील चक्रीवादळांसह. अंतर्गत भागाला दोन्ही हंगामांचा वाटा मिळतो. तमिळनाडू सांख्यिकी विभागाच्या 2022-23 संदर्भ वर्षात राज्याचा सरासरी वार्षिक पाऊस 966.8 मिमी होता.\n\nमैदानी भाग वर्षातील बहुतेक काळ उष्ण असतो — एप्रिल ते जून हा कळस, आणि चेन्नईची आर्द्रता उष्मा अधिक जाणवायला लावते — तर डिसेंबर ते फेब्रुवारी सौम्य आणि आल्हाददायक असतो. ऊटी (उदगमंडलम), कोडैकनाल आणि येरकॉड ही थंड हवेची ठिकाणे गार राहतात; निलगिरीत हिवाळ्यातील काही रात्री दवबिंदू गोठतात."),
        sources=["tn-des"], conf="Editorial"),
    facts("f", [
        fact("rain", L("Normal annual rainfall (State)", "सामान्य वार्षिक वर्षा (राज्य)", "सरासरी वार्षिक पाऊस (राज्य)"),
             TND(966.8, "mm", "Tamil Nadu DES, 'Tamil Nadu at a Glance', for June 2022–May 2023 (actual that year: 1,170.6 mm).", "FY2022-23", "fy", "tn-des"), "number"),
    ]),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Chennai", "चेन्नई", "चेन्नई"), "lat": 13.0827, "lon": 80.2707},
        {"name": L("Madurai", "मदुरै", "मदुराई"), "lat": 9.9252, "lon": 78.1198},
        {"name": L("Coimbatore", "कोयंबटूर", "कोइंबतूर"), "lat": 11.0168, "lon": 76.9558},
        {"name": L("Ooty (Udhagamandalam)", "ऊटी (उदगमंडलम)", "ऊटी (उदगमंडलम)"), "lat": 11.4102, "lon": 76.6950},
    ]},
    lst("best", [
        it3("winter", "November to February", "नवंबर से फ़रवरी", "नोव्हेंबर ते फेब्रुवारी", d=("Most comfortable on the plains; temple towns, Chennai's music season and Pongal in mid-January.", "मैदानों में सबसे सुहावना; मंदिर नगर, चेन्नई का संगीत सीज़न और जनवरी के मध्य में पोंगल।", "मैदानी भागात सर्वांत आल्हाददायक; मंदिरनगरे, चेन्नईचा संगीत हंगाम आणि जानेवारीच्या मध्यात पोंगल.")),
        it3("summer", "April to June", "अप्रैल से जून", "एप्रिल ते जून", d=("Hot on the plains; the season for the Nilgiris, Kodaikanal and Yercaud.", "मैदानों में गर्मी; नीलगिरि, कोडैकनाल और येरकॉड का मौसम।", "मैदानांत उष्मा; निलगिरी, कोडैकनाल व येरकॉडचा हंगाम.")),
        it3("ne", "October to December", "अक्टूबर से दिसंबर", "ऑक्टोबर ते डिसेंबर", d=("North-east monsoon: heavy rain and cyclone risk on the coast; check IMD alerts.", "उत्तर-पूर्व मानसून: तट पर भारी वर्षा और चक्रवात का ख़तरा; आईएमडी अलर्ट देखें।", "ईशान्य मोसमी पाऊस: किनाऱ्यावर मुसळधार पाऊस व चक्रीवादळाचा धोका; आयएमडी इशारे पाहा.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Monthly temperature and rainfall normals", "मासिक तापमान और वर्षा सामान्य", "मासिक तापमान व पर्जन्य सरासरी"), "imd", "IMD climatological normals for Chennai, Madurai, Coimbatore, Ooty."),
        (L("Seasonal rainfall split (south-west vs north-east monsoon)", "मौसमी वर्षा विभाजन (दक्षिण-पश्चिम बनाम उत्तर-पूर्व मानसून)", "हंगामनिहाय पाऊस (नैर्ऋत्य विरुद्ध ईशान्य मोसमी)"), "imd", "IMD Tamil Nadu sub-division statistics."),
        (L("Climate-change vulnerability", "जलवायु परिवर्तन संवेदनशीलता", "हवामान बदल असुरक्षितता"), "ndma", "Tamil Nadu State Action Plan on Climate Change."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Mornings in Tamil Nadu begin at the threshold: women draw kolam patterns in rice flour outside front doors, temple bells and nadaswaram drift from the gopurams, and the first tumbler of filter coffee is poured from a height to froth it. Streets fill with jasmine sellers, autorickshaws and buses painted in their routes' colours. In Chennai, the Marina beach fills at dusk with families, kites and sundal sellers, and in December the city's sabhas run hundreds of Carnatic music and dance recitals. Madurai never quite sleeps around the Meenakshi temple; the Kaveri delta towns move to the rhythm of temple cars and harvest; Coimbatore and Tiruppur hum with workshops and textile mills. Cinema is everywhere — on hoardings, in conversation and in politics — and the language itself, spoken with pride, is part of the identity.",
        "तमिलनाडु में सुबह दहलीज़ से शुरू होती है: महिलाएँ घर के दरवाज़े के बाहर चावल के आटे से कोलम बनाती हैं, गोपुरमों से मंदिर की घंटियाँ और नागस्वरम की धुन आती है, और फ़िल्टर कॉफ़ी का पहला गिलास झाग बनाने के लिए ऊँचाई से उड़ेला जाता है। गलियाँ चमेली बेचने वालों, ऑटो-रिक्शा और अपने रूट के रंगों में रँगी बसों से भर जाती हैं। चेन्नई में शाम को मरीना बीच परिवारों, पतंगों और सुंडल बेचने वालों से भर जाता है, और दिसंबर में शहर की सभाएँ कर्नाटक संगीत और नृत्य के सैकड़ों कार्यक्रम करती हैं। मदुरै मीनाक्षी मंदिर के आसपास कभी पूरी तरह सोता नहीं; कावेरी डेल्टा के कस्बे मंदिर रथों और फ़सल की लय पर चलते हैं; कोयंबटूर और तिरुप्पुर कार्यशालाओं और कपड़ा मिलों से गूँजते हैं। सिनेमा हर जगह है — होर्डिंग पर, बातचीत में और राजनीति में — और गर्व से बोली जाने वाली भाषा स्वयं पहचान का हिस्सा है।",
        "तमिळनाडूत सकाळची सुरुवात उंबरठ्यापासून होते: स्त्रिया दारासमोर तांदळाच्या पिठाने कोलम रेखाटतात, गोपुरांतून मंदिरघंटा आणि नागस्वरमचे सूर येतात, आणि फेस यावा म्हणून फिल्टर कॉफीचा पहिला पेला उंचावरून ओतला जातो. रस्ते मोगऱ्याचे गजरे विकणारे, रिक्षा आणि मार्गानुसार रंगवलेल्या बसगाड्यांनी भरून जातात. चेन्नईत संध्याकाळी मरीना किनारा कुटुंबे, पतंग आणि सुंडल विकणाऱ्यांनी फुलून जातो, आणि डिसेंबरमध्ये शहरातील सभा कर्नाटक संगीत व नृत्याचे शेकडो कार्यक्रम भरवतात. मीनाक्षी मंदिराभोवतीचे मदुराई कधीच पूर्ण झोपत नाही; कावेरी त्रिभुज प्रदेशातील गावे मंदिररथ आणि सुगीच्या तालावर चालतात; कोइंबतूर आणि तिरुप्पूर कार्यशाळा व कापड गिरण्यांनी गजबजलेले असतात. चित्रपट सर्वत्र आहे — फलकांवर, गप्पांत आणि राजकारणात — आणि अभिमानाने बोलली जाणारी भाषा हीच ओळखीचा भाग आहे."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
SC = round(100 * 14438445 / 72147030, 2); ST = round(100 * 794697 / 72147030, 2)
module(R, "people", [
    prose("p1", L(
        f"At the 2011 Census Tamil Nadu had 7.21 crore people. It grew by 15.6% in the decade to 2011 and had 996 women for every 1,000 men, well above the national 943. Literacy was 80.1% (men 86.8%, women 73.1%). Almost half the population (48.4%) lived in towns and cities — among the highest shares of any large State — and the Chennai, Coimbatore and Madurai regions are heavily urbanised.\n\nTamil is the official language and the mother tongue of the large majority. Telugu, Kannada, Urdu, Malayalam and Saurashtra are spoken by significant communities, and the Nilgiris are home to Toda, Kota, Irula and Badaga communities. Scheduled Castes formed about {SC:.1f}% and Scheduled Tribes about {ST:.1f}% of the population in 2011 (calculated from the State's Census counts).",
        f"2011 की जनगणना में तमिलनाडु की जनसंख्या 7.21 करोड़ थी, । 2011 तक के दशक में यह 15.6% बढ़ी और यहाँ प्रति 1,000 पुरुषों पर 996 महिलाएँ थीं, जो राष्ट्रीय 943 से काफ़ी ऊपर है। साक्षरता 80.1% थी (पुरुष 86.8%, महिलाएँ 73.1%)। लगभग आधी आबादी (48.4%) कस्बों और शहरों में रहती थी — बड़े राज्यों में सबसे अधिक हिस्सों में से एक — और चेन्नई, कोयंबटूर और मदुरै क्षेत्र अत्यधिक शहरीकृत हैं।\n\nतमिल राजभाषा है और अधिकांश लोगों की मातृभाषा। तेलुगु, कन्नड़, उर्दू, मलयालम और सौराष्ट्र बोलने वाले बड़े समुदाय हैं, और नीलगिरि टोडा, कोटा, इरुला और बडगा समुदायों का घर है। 2011 में अनुसूचित जातियाँ लगभग {SC:.1f}% और अनुसूचित जनजातियाँ लगभग {ST:.1f}% थीं (राज्य के जनगणना आँकड़ों से गणना)।",
        f"2011 च्या जनगणनेनुसार तमिळनाडूची लोकसंख्या 7.21 कोटी होती. 2011 पर्यंतच्या दशकात ती 15.6% ने वाढली, आणि दर 1,000 पुरुषांमागे 996 स्त्रिया होत्या — राष्ट्रीय 943 पेक्षा बरेच जास्त. साक्षरता 80.1% होती (पुरुष 86.8%, स्त्रिया 73.1%). जवळपास निम्मी लोकसंख्या (48.4%) गावे-शहरांत राहत होती — मोठ्या राज्यांतील सर्वाधिक प्रमाणांपैकी एक — आणि चेन्नई, कोइंबतूर व मदुराई परिसर मोठ्या प्रमाणात नागरी आहेत.\n\nतमिळ ही राजभाषा आणि बहुसंख्यांची मातृभाषा आहे. तेलुगू, कन्नड, उर्दू, मल्याळम आणि सौराष्ट्र भाषिकांचे मोठे समुदाय आहेत, आणि निलगिरी हे तोडा, कोटा, इरुळा व बडगा समुदायांचे घर आहे. 2011 मध्ये अनुसूचित जाती सुमारे {SC:.1f}% आणि अनुसूचित जमाती सुमारे {ST:.1f}% होत्या (राज्याच्या जनगणना आकड्यांवरून गणना)."),
        sources=["tn-des", "census"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), tn["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), tn["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"]),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), tn["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(942, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), tn["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("urb", L("Urban population", "शहरी जनसंख्या", "नागरी लोकसंख्या"), tn["urbanisation2011"], "percent", national=ind["urbanisation2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), tn["density2011"], "number"),
        fact("growth", L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), TND(15.61, "%", "Tamil Nadu DES."), "percent"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             TND(SC, "%", f"Calculated: SC population {inr(14438445)} ÷ total {inr(72147030)} (Tamil Nadu DES, Census 2011)."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             TND(ST, "%", f"Calculated: ST population {inr(794697)} ÷ total {inr(72147030)} (Tamil Nadu DES, Census 2011)."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("ta", "Tamil", "तमिल", "तमिळ", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("te", "Telugu", "तेलुगु", "तेलुगू", m=("Northern districts and cities", "उत्तरी ज़िले और शहर", "उत्तरेकडील जिल्हे व शहरे")),
        it3("kn", "Kannada", "कन्नड़", "कन्नड", m=("Krishnagiri, Erode, Nilgiris", "कृष्णगिरि, इरोड, नीलगिरि", "कृष्णगिरी, इरोड, निलगिरी")),
        it3("ur", "Urdu", "उर्दू", "उर्दू", m=("Vellore, Chennai, Ambur", "वेल्लोर, चेन्नई, आम्बूर", "वेल्लोर, चेन्नई, आंबूर")),
        it3("ml", "Malayalam", "मलयालम", "मल्याळम", m=("Kanniyakumari, Coimbatore, Nilgiris", "कन्याकुमारी, कोयंबटूर, नीलगिरि", "कन्याकुमारी, कोइंबतूर, निलगिरी")),
        it3("saz", "Saurashtra", "सौराष्ट्र", "सौराष्ट्र", m=("Madurai and the Kaveri delta", "मदुरै और कावेरी डेल्टा", "मदुराई व कावेरी त्रिभुज प्रदेश")),
        it3("bfq", "Badaga", "बडगा", "बडगा", m=("Nilgiris", "नीलगिरि", "निलगिरी")),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Mother-tongue shares (Census C-16)", "मातृभाषावार हिस्सा (जनगणना C-16)", "मातृभाषानिहाय वाटा (जनगणना C-16)"), "census", "Census C-16."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
        (L("Particularly vulnerable tribal groups", "विशेष रूप से कमज़ोर जनजातीय समूह", "विशेष असुरक्षित आदिवासी गट"), "tribal-affairs", "Ministry of Tribal Affairs PVTG list for Tamil Nadu."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "The Tamil country has one of the longest literary and archaeological records in India. Sangam poetry, composed in the early centuries BCE and CE, describes three ruling houses — the Cheras, Cholas and Pandyas — and a busy maritime trade; excavations at sites such as Keezhadi, Adichanallur and Arikamedu have pushed the picture of early urban life further back. From the 6th to 9th centuries the Pallavas of Kanchipuram built the rock-cut shrines and Shore Temple of Mamallapuram, while devotional Tamil hymns of the Nayanmars and Alvars reshaped religion across the south.\n\nThe imperial Cholas (9th–13th centuries) built the great temples of Thanjavur, Gangaikonda Cholapuram and Darasuram and sent naval expeditions to Sri Lanka and Southeast Asia. The later Pandyas, the Vijayanagara empire and the Nayaks of Madurai and Thanjavur followed. European trading companies arrived from the 16th century; the British founded Fort St George at Madras in 1639–40, and the Madras Presidency became one of the three great provinces of British India.\n\nIn the 20th century Tamil Nadu was a centre of both the national movement and the Self-Respect movement led by E. V. Ramasamy (Periyar), which challenged caste hierarchy. After Independence, Madras State took its present form in 1956 and was renamed Tamil Nadu in 1969. Since 1967 the State has been governed by Dravidian parties, until a new party, Tamilaga Vettri Kazhagam, formed the government in May 2026.",
        "तमिल देश का साहित्यिक और पुरातात्विक इतिहास भारत में सबसे लंबे इतिहासों में से है। ईसा पूर्व और ईसवी की शुरुआती सदियों में रचा गया संगम काव्य तीन शासक वंशों — चेर, चोल और पांड्य — और व्यस्त समुद्री व्यापार का वर्णन करता है; कीझडी, आदिचनल्लूर और अरिकमेडु जैसे स्थलों की खुदाई ने आरंभिक नगरीय जीवन की तस्वीर को और पीछे तक पहुँचाया है। छठी से नौवीं सदी तक कांचीपुरम के पल्लवों ने मामल्लपुरम के शैलकृत मंदिर और तट मंदिर बनवाए, जबकि नायनमारों और आलवारों के भक्ति भजनों ने पूरे दक्षिण में धर्म को नया रूप दिया।\n\nसाम्राज्यवादी चोलों (9वीं–13वीं सदी) ने तंजावुर, गंगैकोंड चोलपुरम और दारासुरम के महान मंदिर बनवाए और श्रीलंका व दक्षिण-पूर्व एशिया तक नौसैनिक अभियान भेजे। इसके बाद परवर्ती पांड्य, विजयनगर साम्राज्य और मदुरै व तंजावुर के नायक आए। 16वीं सदी से यूरोपीय व्यापारिक कंपनियाँ आईं; अंग्रेज़ों ने 1639–40 में मद्रास में फ़ोर्ट सेंट जॉर्ज की स्थापना की, और मद्रास प्रेसीडेंसी ब्रिटिश भारत के तीन बड़े प्रांतों में से एक बनी।\n\n20वीं सदी में तमिलनाडु राष्ट्रीय आंदोलन और ई. वी. रामासामी (पेरियार) के नेतृत्व वाले आत्मसम्मान आंदोलन — दोनों का केंद्र रहा, जिसने जाति-पदानुक्रम को चुनौती दी। आज़ादी के बाद मद्रास राज्य ने 1956 में अपना वर्तमान रूप लिया और 1969 में इसका नाम तमिलनाडु हुआ। 1967 से राज्य में द्रविड़ दलों का शासन रहा, जब तक कि मई 2026 में एक नए दल, तमिलगा वेट्री कड़गम, ने सरकार नहीं बनाई।",
        "तमिळ प्रदेशाचा साहित्यिक व पुरातत्त्वीय इतिहास भारतातील सर्वांत दीर्घ इतिहासांपैकी आहे. इसवी सनपूर्व व इसवी सनाच्या सुरुवातीच्या शतकांत रचलेले संगम काव्य चेर, चोळ आणि पांड्य या तीन राजघराण्यांचे आणि गजबजलेल्या सागरी व्यापाराचे वर्णन करते; कीळडी, आदिचनल्लूर आणि अरिकमेडू यांसारख्या स्थळांवरील उत्खननांनी प्रारंभिक नागरी जीवनाचे चित्र आणखी मागे नेले आहे. सहाव्या ते नवव्या शतकात कांचीपुरमच्या पल्लवांनी मामल्लपुरमची शैलमंदिरे आणि किनारी मंदिर उभारले, तर नायनमार व आळवार संतांच्या भक्तिस्तोत्रांनी संपूर्ण दक्षिणेत धर्माला नवे रूप दिले.\n\nसाम्राज्यवादी चोळांनी (9वे–13वे शतक) तंजावूर, गंगैकोंड चोळपुरम आणि दारासुरमची भव्य मंदिरे बांधली आणि श्रीलंका व आग्नेय आशियापर्यंत आरमारी मोहिमा धाडल्या. त्यानंतर उत्तरकालीन पांड्य, विजयनगर साम्राज्य आणि मदुराई व तंजावूरचे नायक आले. सोळाव्या शतकापासून युरोपीय व्यापारी कंपन्या आल्या; इंग्रजांनी 1639–40 मध्ये मद्रास येथे फोर्ट सेंट जॉर्जची स्थापना केली, आणि मद्रास इलाखा ब्रिटिश भारतातील तीन मोठ्या प्रांतांपैकी एक बनला.\n\nविसाव्या शतकात तमिळनाडू राष्ट्रीय चळवळ आणि ई. व्ही. रामासामी (पेरियार) यांच्या नेतृत्वाखालील स्वाभिमान चळवळ — ज्याने जातिव्यवस्थेला आव्हान दिले — या दोन्हींचे केंद्र होते. स्वातंत्र्यानंतर मद्रास राज्याने 1956 मध्ये सध्याचे रूप घेतले आणि 1969 मध्ये त्याचे नाव तमिळनाडू झाले. 1967 पासून राज्यात द्रविड पक्षांचे सरकार राहिले, ते मे 2026 मध्ये तमिळगा वेट्री कळगम या नव्या पक्षाने सरकार स्थापन करेपर्यंत."),
        conf="Editorial"),
    timeline([
        ev("sangam", -300, L("c. 3rd century BCE – 3rd century CE", "लगभग तीसरी सदी ईसा पूर्व – तीसरी सदी ईसवी", "सुमारे इ.स.पू. तिसरे शतक – इ.स. तिसरे शतक"), L("Sangam age: Chera, Chola and Pandya kingdoms; Sangam poetry", "संगम युग: चेर, चोल और पांड्य राज्य; संगम काव्य", "संगम युग: चेर, चोळ व पांड्य राज्ये; संगम काव्य")),
        ev("pallava", 630, L("7th–8th centuries", "7वीं–8वीं सदी", "सातवे–आठवे शतक"), L("Pallava monuments at Mamallapuram", "मामल्लपुरम में पल्लव स्मारक", "मामल्लपुरम येथील पल्लव स्मारके")),
        ev("brihadisvara", 1010, L("c. 1010", "लगभग 1010", "सुमारे 1010"), L("Rajaraja Chola completes the Brihadisvara temple, Thanjavur", "राजराज चोल ने तंजावुर का बृहदीश्वर मंदिर पूरा कराया", "राजराज चोळाने तंजावूरचे बृहदीश्वर मंदिर पूर्ण केले")),
        ev("vijayanagara", 1529, L("16th century", "16वीं सदी", "सोळावे शतक"), L("Nayak rule at Madurai and Thanjavur under Vijayanagara", "विजयनगर के अधीन मदुरै और तंजावुर में नायक शासन", "विजयनगरच्या अधिपत्याखाली मदुराई व तंजावूर येथे नायक राजवट")),
        ev("fortstgeorge", 1640, L("1639–40", "1639–40", "1639–40"), L("English East India Company builds Fort St George, Madras", "ईस्ट इंडिया कंपनी ने मद्रास में फ़ोर्ट सेंट जॉर्ज बनाया", "ईस्ट इंडिया कंपनीने मद्रास येथे फोर्ट सेंट जॉर्ज बांधला")),
        ev("vellore", 1806, L("1806", "1806", "1806"), L("Vellore mutiny", "वेल्लोर विद्रोह", "वेल्लोर उठाव")),
        ev("selfrespect", 1925, L("1925", "1925", "1925"), L("Periyar launches the Self-Respect Movement", "पेरियार ने आत्मसम्मान आंदोलन शुरू किया", "पेरियार यांनी स्वाभिमान चळवळ सुरू केली")),
        ev("reorg", 1956, L("1 November 1956", "1 नवंबर 1956", "1 नोव्हेंबर 1956"), L("Madras State reorganised on linguistic lines", "मद्रास राज्य का भाषाई आधार पर पुनर्गठन", "मद्रास राज्याची भाषिक आधारावर पुनर्रचना")),
        ev("rename", 1969, L("14 January 1969", "14 जनवरी 1969", "14 जानेवारी 1969"), L("Madras State renamed Tamil Nadu", "मद्रास राज्य का नाम तमिलनाडु हुआ", "मद्रास राज्याचे नाव तमिळनाडू झाले")),
        ev("chennai", 1996, L("1996", "1996", "1996"), L("Madras city renamed Chennai", "मद्रास शहर का नाम चेन्नई हुआ", "मद्रास शहराचे नाव चेन्नई झाले")),
        ev("classical", 2004, L("2004", "2004", "2004"), L("Tamil becomes India's first classical language", "तमिल भारत की पहली शास्त्रीय भाषा बनी", "तमिळ ही भारताची पहिली अभिजात भाषा ठरली")),
        ev("tsunami", 2004, L("26 December 2004", "26 दिसंबर 2004", "26 डिसेंबर 2004"), L("Indian Ocean tsunami strikes the coast", "हिंद महासागर की सुनामी तट से टकराई", "हिंदी महासागरातील त्सुनामी किनाऱ्यावर आदळली")),
        ev("tvk", 2026, L("10 May 2026", "10 मई 2026", "10 मे 2026"), L("TVK forms the government; C. Joseph Vijay becomes Chief Minister", "टीवीके ने सरकार बनाई; सी. जोसेफ़ विजय मुख्यमंत्री बने", "टीव्हीकेने सरकार स्थापन केले; सी. जोसेफ विजय मुख्यमंत्री")),
    ]),
    lst("heritage", [
        it3("mahabalipuram", "Group of Monuments at Mahabalipuram", "महाबलीपुरम के स्मारक समूह", "महाबलीपुरम स्मारक समूह", m=("UNESCO 1984", "यूनेस्को 1984", "युनेस्को 1984"), url=UNESCO, src="unesco-whc"),
        it3("chola", "Great Living Chola Temples (Thanjavur, Gangaikonda Cholapuram, Darasuram)", "महान जीवित चोल मंदिर (तंजावुर, गंगैकोंड चोलपुरम, दारासुरम)", "महान जिवंत चोळ मंदिरे (तंजावूर, गंगैकोंड चोळपुरम, दारासुरम)", m=("UNESCO 1987, extended 2004", "यूनेस्को 1987, विस्तार 2004", "युनेस्को 1987, विस्तार 2004"), url=UNESCO, src="unesco-whc"),
        it3("nilgiri", "Nilgiri Mountain Railway (part of the Mountain Railways of India)", "नीलगिरि पर्वतीय रेल (भारत की पर्वतीय रेल का भाग)", "निलगिरी पर्वतीय रेल्वे (भारतातील पर्वतीय रेल्वेंचा भाग)", m=("UNESCO 1999, extended 2005", "यूनेस्को 1999, विस्तार 2005", "युनेस्को 1999, विस्तार 2005"), url=UNESCO, src="unesco-whc"),
        it3("wg", "Western Ghats (natural, serial)", "पश्चिमी घाट (प्राकृतिक, शृंखला)", "पश्चिम घाट (नैसर्गिक, मालिका)", m=("UNESCO 2012", "यूनेस्को 2012", "युनेस्को 2012"), url=UNESCO, src="unesco-whc"),
        it3("gingee", "Gingee Fort (part of the Maratha Military Landscapes)", "जिंजी क़िला (मराठा सैन्य परिदृश्य का भाग)", "जिंजी किल्ला (मराठा लष्करी भूप्रदेशांचा भाग)", m=("UNESCO 2025", "यूनेस्को 2025", "युनेस्को 2025"), url=UNESCO, src="unesco-whc"),
        it3("keezhadi", "Keezhadi excavations (Sivaganga)", "कीझडी उत्खनन (शिवगंगा)", "कीळडी उत्खनन (शिवगंगा)", m=("Sangam-era urban settlement", "संगम काल की नगरीय बस्ती", "संगम काळातील नागरी वस्ती")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("tn mod1 ok")
