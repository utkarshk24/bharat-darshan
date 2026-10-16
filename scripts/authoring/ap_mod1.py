"""Andhra Pradesh modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-AP"
CSE = "https://cse.ap.gov.in/MISdownload/MIS_REPORT_NOTIFICATION/Educational%20Statistics%202017-18.pdf"
SES = "https://s3.ap-south-1.amazonaws.com/apfinance.gov.in/uploads/index-docs/AP_Socio_Economic_Survey_2024_25.pdf"
DIST = "https://www.etvbharat.com/en/state/andhra-pradesh-cabinet-approves-formation-of-two-new-districts-enn25123002492"
ap = read("regions/IN-AP.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Andhra Pradesh lies on India's south-eastern coast, between the Bay of Bengal and the Eastern Ghats. In its present form it was created on 2 June 2014, when Telangana was separated from it; it had 4.96 crore people at the 2011 Census (counted for its present area) on about 1.63 lakh km². The fertile deltas of the Godavari and the Krishna form its rice bowl, while the drier upland region of Rayalaseema lies to the south-west. Amaravati, on the Krishna, is the capital; Visakhapatnam, Vijayawada, Guntur, Nellore and Tirupati are the largest cities.\n\nAndhra State, formed in 1953 after the death of Potti Sriramulu, who fasted for a Telugu-speaking State, was the first State created on linguistic lines. It merged with the Telugu-speaking districts of Hyderabad State in 1956 to form Andhra Pradesh. Telugu is the official language.",
        "आंध्र प्रदेश भारत के दक्षिण-पूर्वी तट पर, बंगाल की खाड़ी और पूर्वी घाट के बीच स्थित है। अपने वर्तमान रूप में यह 2 जून 2014 को बना, जब तेलंगाना इससे अलग हुआ; 2011 की जनगणना में (वर्तमान क्षेत्र के अनुसार) यहाँ लगभग 1.63 लाख वर्ग किमी पर 4.96 करोड़ लोग थे। गोदावरी और कृष्णा के उपजाऊ डेल्टा इसका धान का कटोरा हैं, जबकि दक्षिण-पश्चिम में अपेक्षाकृत सूखा ऊपरी क्षेत्र रायलसीमा है। कृष्णा के किनारे अमरावती राजधानी है; विशाखापत्तनम, विजयवाड़ा, गुंटूर, नेल्लोर और तिरुपति सबसे बड़े शहर हैं।\n\nतेलुगु-भाषी राज्य के लिए अनशन करने वाले पोट्टि श्रीरामुलु की मृत्यु के बाद 1953 में बना आंध्र राज्य भाषाई आधार पर बना पहला राज्य था। 1956 में यह हैदराबाद राज्य के तेलुगु-भाषी ज़िलों के साथ मिलकर आंध्र प्रदेश बना। तेलुगु राजभाषा है।",
        "आंध्र प्रदेश भारताच्या आग्नेय किनाऱ्यावर, बंगालचा उपसागर व पूर्व घाट यांच्या दरम्यान आहे. सध्याच्या स्वरूपात ते 2 जून 2014 रोजी तेलंगणा वेगळे झाल्यावर अस्तित्वात आले; 2011 च्या जनगणनेनुसार (सध्याच्या क्षेत्रानुसार) सुमारे 1.63 लाख चौ.किमी क्षेत्रावर 4.96 कोटी लोक होते. गोदावरी व कृष्णेचे सुपीक त्रिभुज प्रदेश हे त्याचे भाताचे कोठार आहेत, तर नैर्ऋत्येला तुलनेने कोरडा उंचावरील रायलसीमा प्रदेश आहे. कृष्णेकाठची अमरावती ही राजधानी आहे; विशाखापट्टणम, विजयवाडा, गुंटूर, नेल्लोर व तिरुपती ही सर्वांत मोठी शहरे आहेत.\n\nतेलुगुभाषक राज्यासाठी उपोषण करणारे पोट्टी श्रीरामुलू यांच्या मृत्यूनंतर 1953 मध्ये स्थापन झालेले आंध्र राज्य हे भाषिक आधारावर बनलेले पहिले राज्य होते. 1956 मध्ये ते हैदराबाद राज्यातील तेलुगुभाषक जिल्ह्यांसोबत एकत्र होऊन आंध्र प्रदेश बनले. तेलुगु ही राजभाषा आहे."),
        sources=["ap-cse", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Andhra Pradesh is home to the hill shrine of Tirumala at Tirupati, one of the most visited places of pilgrimage in the world, and to India's spaceport at Sriharikota, from where ISRO launches its rockets. The Buddhist stupa at Amaravati and the remains at Nagarjunakonda recall a time when the Krishna valley was a centre of Buddhist learning. The State is known for Kuchipudi dance, Kalamkari painted textiles, Kondapalli and Etikoppaka toys, fiery Guntur chillies and the coffee of the Araku hills.",
        "आंध्र प्रदेश में तिरुपति का पहाड़ी तीर्थ तिरुमला है, जो दुनिया के सबसे अधिक देखे जाने वाले तीर्थस्थलों में है, और श्रीहरिकोटा में भारत का अंतरिक्ष प्रक्षेपण केंद्र, जहाँ से इसरो अपने रॉकेट छोड़ता है। अमरावती का बौद्ध स्तूप और नागार्जुनकोंडा के अवशेष उस समय की याद दिलाते हैं जब कृष्णा घाटी बौद्ध शिक्षा का केंद्र थी। राज्य कुचिपुड़ी नृत्य, कलमकारी चित्रित वस्त्रों, कोंडापल्ली और एटिकोप्पाका खिलौनों, तीखी गुंटूर मिर्च और अराकू पहाड़ियों की कॉफ़ी के लिए जाना जाता है।",
        "आंध्र प्रदेशात तिरुपतीचे डोंगरावरील तीर्थक्षेत्र तिरुमला आहे — जगातील सर्वाधिक भेट दिल्या जाणाऱ्या तीर्थस्थळांपैकी एक — आणि श्रीहरिकोटा येथे भारताचे अंतराळ प्रक्षेपण केंद्र, जिथून इस्रो आपली रॉकेट सोडते. अमरावतीचा बौद्ध स्तूप व नागार्जुनकोंडाचे अवशेष त्या काळाची आठवण करून देतात जेव्हा कृष्णा खोरे बौद्ध विद्येचे केंद्र होते. राज्य कुचिपुडी नृत्य, कलमकारी रंगवलेली वस्त्रे, कोंडापल्ली व एटिकोप्पाकाची खेळणी, तिखट गुंटूर मिरची आणि अराकू डोंगरांची कॉफी यांसाठी ओळखले जाते."),
        title=L("What makes Andhra Pradesh unique?", "आंध्र प्रदेश को ख़ास क्या बनाता है?", "आंध्र प्रदेशचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed", "गठन", "निर्मिती"), L("1 November 1956; present boundaries from 2 June 2014", "1 नवंबर 1956; वर्तमान सीमाएँ 2 जून 2014 से", "1 नोव्हेंबर 1956; सध्याच्या सीमा 2 जून 2014 पासून")],
           [L("Districts", "ज़िले", "जिल्हे"), L("28 (Markapuram and Polavaram added with effect from 31 December 2025)", "28 (मार्कापुरम और पोलावरम 31 दिसंबर 2025 से जोड़े गए)", "28 (मार्कापुरम व पोलावरम 31 डिसेंबर 2025 पासून जोडले)")],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Telugu; Urdu is the second official language", "तेलुगु; उर्दू दूसरी राजभाषा है", "तेलुगु; उर्दू ही दुसरी राजभाषा")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("High Court of Andhra Pradesh, Amaravati (2019)", "आंध्र प्रदेश उच्च न्यायालय, अमरावती (2019)", "आंध्र प्रदेश उच्च न्यायालय, अमरावती (2019)")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-AP / AP"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          "etv-bharat", DIST, conf="Editorial", access=None,
          note=L("District count from ETV Bharat's report of the State Cabinet decision (30 Dec 2025); the State's Socio Economic Survey 2024-25 gives 26 before the change. Other rows are editorial.",
                 "ज़िलों की संख्या ईटीवी भारत की राज्य मंत्रिमंडल निर्णय (30 दिसंबर 2025) की रिपोर्ट से; राज्य का सामाजिक-आर्थिक सर्वेक्षण 2024-25 बदलाव से पहले 26 बताता है। अन्य पंक्तियाँ संपादकीय हैं।",
                 "जिल्ह्यांची संख्या ईटीव्ही भारतच्या राज्य मंत्रिमंडळ निर्णयाच्या (30 डिसेंबर 2025) वृत्तावरून; राज्याचे सामाजिक-आर्थिक सर्वेक्षण 2024-25 बदलापूर्वी 26 सांगते. इतर ओळी संपादकीय आहेत.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Andhra Pradesh has three broad regions. North Coastal Andhra, around Visakhapatnam and Srikakulam, rises inland into the forested Eastern Ghats and the Araku hills. Central and South Coastal Andhra hold the deltas of the Godavari and the Krishna — two of India's largest rivers, which reach the sea here — and the coastal plains down to Nellore and the Pulicat lagoon. Rayalaseema, in the south-west, is a dry plateau of red soils, granite hills and the Nallamala and Seshachalam forests, drained by the Penna (Pennar).\n\nThe coastline runs for 974 km along the Bay of Bengal, according to the State's Socio Economic Survey 2024-25. Kolleru, between the two deltas, is one of India's largest freshwater lakes.",
        "आंध्र प्रदेश के तीन बड़े क्षेत्र हैं। विशाखापत्तनम और श्रीकाकुलम के आसपास का उत्तरी तटीय आंध्र भीतर की ओर वनाच्छादित पूर्वी घाट और अराकू पहाड़ियों में उठता है। मध्य और दक्षिणी तटीय आंध्र में गोदावरी और कृष्णा — भारत की दो सबसे बड़ी नदियाँ, जो यहीं समुद्र में मिलती हैं — के डेल्टा और नेल्लोर व पुलिकट लैगून तक तटीय मैदान हैं। दक्षिण-पश्चिम में रायलसीमा लाल मिट्टी, ग्रेनाइट पहाड़ियों और नल्लमला व शेषाचलम वनों का सूखा पठार है, जिसे पेन्ना (पेन्नार) बहाती है।\n\nराज्य के सामाजिक-आर्थिक सर्वेक्षण 2024-25 के अनुसार तटरेखा बंगाल की खाड़ी के साथ 974 किमी लंबी है। दोनों डेल्टाओं के बीच कोल्लेरु भारत की सबसे बड़ी मीठे पानी की झीलों में से है।",
        "आंध्र प्रदेशचे तीन मोठे प्रदेश आहेत. विशाखापट्टणम व श्रीकाकुलमभोवतीचा उत्तर किनारी आंध्र आतल्या बाजूला जंगलव्याप्त पूर्व घाट व अराकू डोंगरांत उंचावतो. मध्य व दक्षिण किनारी आंध्रमध्ये गोदावरी व कृष्णा — भारतातील दोन सर्वांत मोठ्या नद्या, ज्या इथेच समुद्राला मिळतात — यांचे त्रिभुज प्रदेश आणि नेल्लोर व पुलिकत खाजणापर्यंत किनारी मैदाने आहेत. नैर्ऋत्येला रायलसीमा हे तांबडी माती, ग्रॅनाइटचे डोंगर आणि नल्लमला व शेषाचलम जंगलांचे कोरडे पठार आहे, जे पेन्ना (पेन्नार) नदी वाहून नेते.\n\nराज्याच्या सामाजिक-आर्थिक सर्वेक्षण 2024-25 नुसार किनारपट्टी बंगालच्या उपसागराकाठी 974 किमी लांब आहे. दोन्ही त्रिभुज प्रदेशांदरम्यानचे कोल्लेरू हे भारतातील सर्वांत मोठ्या गोड्या पाण्याच्या सरोवरांपैकी आहे."),
        sources=["ap-fin"], conf="Editorial"),
    facts("f", [
        fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), ap["area"], "number", national=ind["area"]),
        fact("coast", L("Coastline", "तटरेखा", "किनारपट्टी"), dp(974, "km", "FY2024-25", "fy", "ap-fin", SES, note="Socio Economic Survey 2024-25, Government of Andhra Pradesh."), "number"),
    ]),
    lst("neighbours", [
        it3("tg", "Telangana (north-west)", "तेलंगाना (उत्तर-पश्चिम)", "तेलंगणा (वायव्य)"), it3("ct", "Chhattisgarh (north)", "छत्तीसगढ़ (उत्तर)", "छत्तीसगड (उत्तर)"),
        it3("or", "Odisha (north-east)", "ओडिशा (उत्तर-पूर्व)", "ओडिशा (ईशान्य)"), it3("ka", "Karnataka (west)", "कर्नाटक (पश्चिम)", "कर्नाटक (पश्चिम)"),
        it3("tn", "Tamil Nadu (south)", "तमिलनाडु (दक्षिण)", "तमिळनाडू (दक्षिण)"), it3("sea", "Bay of Bengal (east)", "बंगाल की खाड़ी (पूर्व)", "बंगालचा उपसागर (पूर्व)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("godavari", "Godavari", "गोदावरी", "गोदावरी", d=("Enters from Telangana and forms a wide delta below Rajamahendravaram.", "तेलंगाना से आती है और राजमहेंद्रवरम के नीचे चौड़ा डेल्टा बनाती है।", "तेलंगणातून येते आणि राजमहेंद्रवरमच्या खाली रुंद त्रिभुज प्रदेश बनवते.")),
        it3("krishna", "Krishna", "कृष्णा", "कृष्णा", d=("Dammed at Srisailam and Nagarjuna Sagar; the Prakasam Barrage stands at Vijayawada.", "श्रीशैलम और नागार्जुन सागर पर बाँध; विजयवाड़ा में प्रकाशम बराज।", "श्रीशैलम व नागार्जुन सागर येथे धरणे; विजयवाड्यात प्रकाशम बंधारा.")),
        it3("penna", "Penna (Pennar)", "पेन्ना (पेन्नार)", "पेन्ना (पेन्नार)", d=("River of Rayalaseema and Nellore.", "रायलसीमा और नेल्लोर की नदी।", "रायलसीमा व नेल्लोरची नदी.")),
        it3("vamsadhara", "Vamsadhara and Nagavali", "वंशधारा और नागावली", "वंशधारा व नागावली", d=("Rivers of the far north-east, flowing from Odisha.", "सुदूर उत्तर-पूर्व की नदियाँ, जो ओडिशा से आती हैं।", "अगदी ईशान्येकडील नद्या, ओडिशातून येणाऱ्या.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point — official elevation", "सर्वोच्च बिंदु — आधिकारिक ऊँचाई", "सर्वोच्च शिखर — अधिकृत उंची"), "survey-of-india", "Survey of India or the State gazetteer."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Andhra Pradesh is hot for much of the year. April and May are the hottest months, and heatwaves are common in coastal and Rayalaseema districts alike. The south-west monsoon (June–September) brings most of the rain to the north and the deltas, while the south — Nellore, Chittoor and parts of Rayalaseema — also gets important rain from the north-east monsoon in October and November. Rayalaseema, in the rain shadow of the Western Ghats, is among the driest parts of southern India. Cyclones from the Bay of Bengal strike the coast mainly in May and from October to December.",
        "आंध्र प्रदेश साल के अधिकांश समय गर्म रहता है। अप्रैल और मई सबसे गर्म महीने हैं, और तटीय व रायलसीमा दोनों ज़िलों में लू आम है। दक्षिण-पश्चिम मानसून (जून–सितंबर) उत्तर और डेल्टाओं में अधिकांश वर्षा लाता है, जबकि दक्षिण — नेल्लोर, चित्तूर और रायलसीमा के कुछ भाग — को अक्टूबर और नवंबर में उत्तर-पूर्वी मानसून से भी महत्त्वपूर्ण वर्षा मिलती है। पश्चिमी घाट की वृष्टि-छाया में स्थित रायलसीमा दक्षिण भारत के सबसे सूखे हिस्सों में है। बंगाल की खाड़ी के चक्रवात मुख्यतः मई में और अक्टूबर से दिसंबर तक तट से टकराते हैं।",
        "आंध्र प्रदेश वर्षातील बहुतांश काळ उष्ण असते. एप्रिल व मे हे सर्वांत उष्ण महिने आहेत, आणि किनारी व रायलसीमा दोन्ही जिल्ह्यांत उष्णतेच्या लाटा नेहमीच्या आहेत. नैर्ऋत्य मान्सून (जून–सप्टेंबर) उत्तरेत व त्रिभुज प्रदेशांत बहुतांश पाऊस आणतो, तर दक्षिणेला — नेल्लोर, चित्तूर व रायलसीमाचे काही भाग — ऑक्टोबर-नोव्हेंबरमध्ये ईशान्य मान्सूनपासूनही महत्त्वाचा पाऊस मिळतो. पश्चिम घाटाच्या पर्जन्यछायेतील रायलसीमा हा दक्षिण भारतातील सर्वांत कोरड्या भागांपैकी आहे. बंगालच्या उपसागरातील चक्रीवादळे मुख्यतः मे महिन्यात आणि ऑक्टोबर ते डिसेंबरदरम्यान किनाऱ्याला धडकतात."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Amaravati", "अमरावती", "अमरावती"), "lat": 16.5131, "lon": 80.5165},
        {"name": L("Visakhapatnam", "विशाखापत्तनम", "विशाखापट्टणम"), "lat": 17.6868, "lon": 83.2185},
        {"name": L("Tirupati", "तिरुपति", "तिरुपती"), "lat": 13.6288, "lon": 79.4192},
        {"name": L("Araku Valley", "अराकू घाटी", "अराकू खोरे"), "lat": 18.3273, "lon": 82.8775},
    ]},
    lst("best", [
        it3("winter", "October to February", "अक्टूबर से फ़रवरी", "ऑक्टोबर ते फेब्रुवारी", d=("Pleasant weather for the coast, temples and the Araku hills; Sankranti in January.", "तट, मंदिरों और अराकू पहाड़ियों के लिए सुहावना मौसम; जनवरी में संक्रांति।", "किनारा, मंदिरे व अराकू डोंगरांसाठी सुखद हवामान; जानेवारीत संक्रांती.")),
        it3("summer", "March to June", "मार्च से जून", "मार्च ते जून", d=("Very hot; plan travel for early mornings.", "बहुत गर्म; यात्रा सुबह जल्दी करें।", "खूप उष्ण; प्रवास पहाटे करा.")),
        it3("monsoon", "July to September", "जुलाई से सितंबर", "जुलै ते सप्टेंबर", d=("Green landscapes and waterfalls in the Eastern Ghats; heavy rain at times.", "पूर्वी घाट में हरियाली और झरने; कभी-कभी भारी वर्षा।", "पूर्व घाटात हिरवाई व धबधबे; कधीकधी मुसळधार पाऊस.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (Coastal Andhra Pradesh and Rayalaseema)", "सामान्य वार्षिक वर्षा (तटीय आंध्र प्रदेश और रायलसीमा)", "सरासरी वार्षिक पाऊस (किनारी आंध्र प्रदेश व रायलसीमा)"), "imd", "IMD rainfall statistics by sub-division."),
        (L("Cyclone landfalls by year", "वर्षवार चक्रवात का तट पर पहुँचना", "वर्षनिहाय चक्रीवादळांचे किनाऱ्यावर येणे"), "imd", "IMD cyclone e-Atlas."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Life in coastal Andhra moves with the rice and the river: green paddy and coconut groves in the Godavari delta, fishing harbours along the shore, and busy market towns linked by buses and trains. Vijayawada sits at a great road and rail junction on the Krishna, Visakhapatnam is a port and naval city between hills and sea, and Tirupati fills with pilgrims at every hour. Meals are generous and spicy — rice with pickles, podis and ghee — and filter coffee and tiffin stalls start the day. Telugu cinema is followed with passion, and new releases are celebrated in packed theatres.",
        "तटीय आंध्र का जीवन धान और नदी के साथ चलता है: गोदावरी डेल्टा में हरे धान के खेत और नारियल के बाग़, तट पर मछली बंदरगाह, और बसों व रेलों से जुड़े व्यस्त बाज़ार कस्बे। विजयवाड़ा कृष्णा पर एक बड़े सड़क और रेल जंक्शन पर बसा है, विशाखापत्तनम पहाड़ियों और समुद्र के बीच बंदरगाह व नौसेना शहर है, और तिरुपति हर समय तीर्थयात्रियों से भरा रहता है। भोजन भरपूर और तीखा होता है — अचार, पोडी और घी के साथ चावल — और दिन की शुरुआत फ़िल्टर कॉफ़ी और टिफ़िन की दुकानों से होती है। तेलुगु सिनेमा को जुनून से देखा जाता है, और नई फ़िल्मों की रिलीज़ भरे सिनेमाघरों में उत्सव की तरह मनाई जाती है।",
        "किनारी आंध्रमधील जीवन भात व नदीच्या लयीत चालते: गोदावरीच्या त्रिभुज प्रदेशात हिरवी भातशेती व नारळाच्या बागा, किनाऱ्यावर मासेमारी बंदरे, आणि बस व रेल्वेने जोडलेली गजबजलेली बाजारपेठेची गावे. विजयवाडा कृष्णेवरील मोठ्या रस्ते व रेल्वे जंक्शनवर वसले आहे, विशाखापट्टणम हे डोंगर व समुद्राच्या मधले बंदर व नौदल शहर आहे, आणि तिरुपती सदैव यात्रेकरूंनी भरलेले असते. जेवण भरपूर व तिखट असते — लोणची, पोडी व तुपासह भात — आणि दिवसाची सुरुवात फिल्टर कॉफी व टिफिनच्या टपऱ्यांवर होते. तेलुगु चित्रपट उत्कटतेने पाहिले जातात, आणि नवे चित्रपट भरलेल्या चित्रपटगृहांत उत्सवासारखे साजरे होतात."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Counted for its present area, Andhra Pradesh had 4.96 crore people at the 2011 Census, with a density of about 304 per km². The sex ratio was 997 women per 1,000 men — far above the national 943 — and literacy was 67.4% (men 74.8%, women 60.0%), below the national 73.0%. About 29.5% of people lived in towns and cities. Scheduled Castes made up about 17.1% of the population and Scheduled Tribes about 5.5%, the latter mainly in the Eastern Ghats agency areas of the north.\n\nTelugu is spoken by the great majority. Urdu is spoken by many Muslims, and tribal languages such as Koya, Savara and Konda are spoken in the hills; Tamil, Kannada and Odia are heard along the borders.",
        "वर्तमान क्षेत्र के अनुसार गिनने पर, 2011 की जनगणना में आंध्र प्रदेश की जनसंख्या 4.96 करोड़ थी, और घनत्व लगभग 304 प्रति वर्ग किमी। लिंगानुपात प्रति 1,000 पुरुषों पर 997 महिलाएँ था — राष्ट्रीय 943 से बहुत अधिक — और साक्षरता 67.4% (पुरुष 74.8%, महिलाएँ 60.0%) थी, जो राष्ट्रीय 73.0% से कम है। लगभग 29.5% लोग कस्बों और शहरों में रहते थे। अनुसूचित जातियाँ जनसंख्या का लगभग 17.1% और अनुसूचित जनजातियाँ लगभग 5.5% थीं; जनजातियाँ मुख्यतः उत्तर के पूर्वी घाट के एजेंसी क्षेत्रों में हैं।\n\nअधिकांश लोग तेलुगु बोलते हैं। बहुत से मुसलमान उर्दू बोलते हैं, और पहाड़ों में कोया, सवरा और कोंडा जैसी आदिवासी भाषाएँ बोली जाती हैं; सीमाओं पर तमिल, कन्नड़ और ओड़िया भी सुनाई देती हैं।",
        "सध्याच्या क्षेत्रानुसार मोजल्यास, 2011 च्या जनगणनेत आंध्र प्रदेशची लोकसंख्या 4.96 कोटी होती, आणि घनता सुमारे 304 प्रति चौ.किमी. दर 1,000 पुरुषांमागे 997 स्त्रिया होत्या — राष्ट्रीय 943 पेक्षा बरेच जास्त — आणि साक्षरता 67.4% (पुरुष 74.8%, स्त्रिया 60.0%) होती, राष्ट्रीय 73.0% पेक्षा कमी. सुमारे 29.5% लोक शहरांत राहत होते. अनुसूचित जाती लोकसंख्येच्या सुमारे 17.1% व अनुसूचित जमाती सुमारे 5.5% होत्या; जमाती मुख्यतः उत्तरेकडील पूर्व घाटातील एजन्सी भागांत आहेत.\n\nबहुसंख्य लोक तेलुगु बोलतात. अनेक मुस्लीम उर्दू बोलतात, आणि डोंगराळ भागात कोया, सवरा व कोंडा यांसारख्या आदिवासी भाषा बोलल्या जातात; सीमाभागांत तमिळ, कन्नड व ओडियाही ऐकू येतात."),
        sources=["ap-cse", "census"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), ap["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), ap["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), ap["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("urb", L("Urban population share", "शहरी जनसंख्या का हिस्सा", "नागरी लोकसंख्येचा वाटा"), ap["urbanisation2011"], "percent"),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), ap["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(17.08, "%", "2011", "census", "ap-cse", CSE, note="Calculated: 84,69,278 SC persons ÷ 4,95,77,103 (residual State, Census 2011)."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(5.53, "%", "2011", "census", "ap-cse", CSE, note="Calculated: 27,40,133 ST persons ÷ 4,95,77,103 (residual State, Census 2011)."), "percent"),
        fact("growth", L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"),
             dp(9.21, "%", "2011", "census", "ap-cse", CSE, note="Growth between the 2001 and 2011 Censuses for the residual State, as given in Educational Statistics 2017-18."), "percent"),
    ], title=L("Census 2011 at a glance (present area)", "जनगणना 2011 एक नज़र में (वर्तमान क्षेत्र)", "जनगणना 2011 दृष्टिक्षेपात (सध्याचे क्षेत्र)")),
    lst("langs", [
        it3("te", "Telugu", "तेलुगु", "तेलुगु", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("ur", "Urdu", "उर्दू", "उर्दू"), it3("koya", "Koya", "कोया", "कोया", m=("Godavari agency areas", "गोदावरी एजेंसी क्षेत्र", "गोदावरी एजन्सी भाग")),
        it3("savara", "Savara", "सवरा", "सवरा", m=("Srikakulam and Parvathipuram Manyam hills", "श्रीकाकुलम और पार्वतीपुरम मन्यम पहाड़ियाँ", "श्रीकाकुलम व पार्वतीपुरम मन्यम डोंगर")),
        it3("ta", "Tamil", "तमिल", "तमिळ"), it3("kn", "Kannada", "कन्नड़", "कन्नड"), it3("or", "Odia", "ओड़िया", "ओडिया"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Child sex ratio (0–6) for the present State", "वर्तमान राज्य का शिशु लिंगानुपात (0–6)", "सध्याच्या राज्याचे बाल लिंग गुणोत्तर (0–6)"), "census", "Census 2011 Primary Census Abstract, recast for the 13 residual districts."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "The Satavahanas, who ruled much of the Deccan from around the 1st century BCE, had an important centre at Dhanyakataka near Amaravati, where a great Buddhist stupa stood; the Ikshvakus later built monasteries at Nagarjunakonda. The Eastern Chalukyas of Vengi (7th–11th centuries) saw the beginnings of Telugu literature with Nannaya's Mahabharata. The Kakatiyas of Warangal and then the Vijayanagara empire — whose king Krishnadevaraya was himself a Telugu poet — ruled the region, followed by the Qutb Shahis of Golconda and the Nizams. Coastal Andhra and Rayalaseema passed to the British and became part of the Madras Presidency.\n\nAfter Independence the demand for a Telugu State grew. Potti Sriramulu died in December 1952 after a fast of 58 days, and Andhra State was formed on 1 October 1953 with Kurnool as capital. On 1 November 1956 it was joined with the Telugu-speaking districts of Hyderabad State to form Andhra Pradesh, with Hyderabad as capital. After a long movement for a separate Telangana, the State was divided on 2 June 2014; Andhra Pradesh kept 13 districts and began building a new capital at Amaravati.",
        "लगभग पहली सदी ईसा पूर्व से दक्कन के बड़े भाग पर शासन करने वाले सातवाहनों का अमरावती के पास धान्यकटक में एक महत्त्वपूर्ण केंद्र था, जहाँ एक विशाल बौद्ध स्तूप था; बाद में इक्ष्वाकुओं ने नागार्जुनकोंडा में विहार बनवाए। वेंगी के पूर्वी चालुक्यों (7वीं–11वीं सदी) के काल में नन्नय के महाभारत से तेलुगु साहित्य की शुरुआत हुई। वारंगल के काकतीयों और फिर विजयनगर साम्राज्य — जिसके राजा कृष्णदेवराय स्वयं तेलुगु कवि थे — ने इस क्षेत्र पर शासन किया, उसके बाद गोलकुंडा के क़ुतुबशाही और निज़ाम आए। तटीय आंध्र और रायलसीमा अंग्रेज़ों के अधीन होकर मद्रास प्रेसीडेंसी का हिस्सा बने।\n\nआज़ादी के बाद तेलुगु राज्य की माँग बढ़ी। दिसंबर 1952 में 58 दिनों के अनशन के बाद पोट्टि श्रीरामुलु का निधन हुआ, और 1 अक्टूबर 1953 को कुरनूल राजधानी के साथ आंध्र राज्य बना। 1 नवंबर 1956 को इसे हैदराबाद राज्य के तेलुगु-भाषी ज़िलों से जोड़कर हैदराबाद राजधानी के साथ आंध्र प्रदेश बनाया गया। अलग तेलंगाना के लंबे आंदोलन के बाद 2 जून 2014 को राज्य का विभाजन हुआ; आंध्र प्रदेश के पास 13 ज़िले रहे और उसने अमरावती में नई राजधानी बनाना शुरू किया।",
        "सुमारे इसवी सनपूर्व पहिल्या शतकापासून दख्खनच्या मोठ्या भागावर राज्य करणाऱ्या सातवाहनांचे अमरावतीजवळील धान्यकटक येथे महत्त्वाचे केंद्र होते, जिथे एक भव्य बौद्ध स्तूप होता; नंतर इक्ष्वाकूंनी नागार्जुनकोंडा येथे विहार बांधले. वेंगीच्या पूर्व चालुक्यांच्या काळात (सातवे–अकरावे शतक) नन्नयाच्या महाभारतातून तेलुगु साहित्याची सुरुवात झाली. वरंगळचे काकतीय आणि नंतर विजयनगर साम्राज्य — ज्याचा राजा कृष्णदेवराय स्वतः तेलुगु कवी होता — यांनी या प्रदेशावर राज्य केले, त्यानंतर गोवळकोंड्याचे कुतुबशाही व निजाम आले. किनारी आंध्र व रायलसीमा इंग्रजांकडे जाऊन मद्रास प्रांताचा भाग बनले.\n\nस्वातंत्र्यानंतर तेलुगु राज्याची मागणी वाढली. डिसेंबर 1952 मध्ये 58 दिवसांच्या उपोषणानंतर पोट्टी श्रीरामुलू यांचे निधन झाले, आणि 1 ऑक्टोबर 1953 रोजी कर्नूल राजधानीसह आंध्र राज्य स्थापन झाले. 1 नोव्हेंबर 1956 रोजी त्याला हैदराबाद राज्यातील तेलुगुभाषक जिल्हे जोडून हैदराबाद राजधानीसह आंध्र प्रदेश बनवले गेले. स्वतंत्र तेलंगणासाठीच्या दीर्घ आंदोलनानंतर 2 जून 2014 रोजी राज्याचे विभाजन झाले; आंध्र प्रदेशकडे 13 जिल्हे राहिले आणि त्याने अमरावती येथे नवी राजधानी उभारण्यास सुरुवात केली."),
        conf="Editorial"),
    timeline([
        ev("satavahana", -100, L("c. 1st century BCE", "लगभग पहली सदी ई.पू.", "सुमारे इ.स.पू. पहिले शतक"), L("Satavahana rule; Amaravati stupa flourishes", "सातवाहन शासन; अमरावती स्तूप का उत्कर्ष", "सातवाहन राजवट; अमरावती स्तूपाचा उत्कर्ष")),
        ev("nannaya", 1050, L("11th century", "11वीं सदी", "अकरावे शतक"), L("Nannaya begins the Telugu Mahabharata", "नन्नय ने तेलुगु महाभारत आरंभ किया", "नन्नयाने तेलुगु महाभारताचा प्रारंभ केला")),
        ev("krishnadevaraya", 1509, L("1509–1529", "1509–1529", "1509–1529"), L("Reign of Krishnadevaraya of Vijayanagara", "विजयनगर के कृष्णदेवराय का शासन", "विजयनगरच्या कृष्णदेवरायाची राजवट")),
        ev("sriramulu", 1952, L("15 December 1952", "15 दिसंबर 1952", "15 डिसेंबर 1952"), L("Potti Sriramulu dies after a 58-day fast", "58 दिन के अनशन के बाद पोट्टि श्रीरामुलु का निधन", "58 दिवसांच्या उपोषणानंतर पोट्टी श्रीरामुलू यांचे निधन")),
        ev("andhra", 1953, L("1 October 1953", "1 अक्टूबर 1953", "1 ऑक्टोबर 1953"), L("Andhra State formed, capital Kurnool", "आंध्र राज्य बना, राजधानी कुरनूल", "आंध्र राज्य स्थापन, राजधानी कर्नूल")),
        ev("ap", 1956, L("1 November 1956", "1 नवंबर 1956", "1 नोव्हेंबर 1956"), L("Andhra Pradesh formed", "आंध्र प्रदेश का गठन", "आंध्र प्रदेशची स्थापना")),
        ev("sriharikota", 1971, L("1971", "1971", "1971"), L("First rocket launch from Sriharikota", "श्रीहरिकोटा से पहला रॉकेट प्रक्षेपण", "श्रीहरिकोट्याहून पहिले रॉकेट प्रक्षेपण")),
        ev("bifurcation", 2014, L("2 June 2014", "2 जून 2014", "2 जून 2014"), L("Telangana separated; Andhra Pradesh in its present form", "तेलंगाना अलग; आंध्र प्रदेश अपने वर्तमान रूप में", "तेलंगणा वेगळे; आंध्र प्रदेश सध्याच्या स्वरूपात")),
        ev("amaravati", 2026, L("2026", "2026", "2026"), L("Parliament passes Bill naming Amaravati as capital", "संसद ने अमरावती को राजधानी घोषित करने वाला विधेयक पारित किया", "अमरावतीला राजधानी ठरवणारे विधेयक संसदेत मंजूर")),
    ]),
    lst("heritage", [
        it3("amaravati", "Amaravati stupa site", "अमरावती स्तूप स्थल", "अमरावती स्तूप स्थळ", m=("Satavahana era", "सातवाहन काल", "सातवाहन काळ")),
        it3("nagarjunakonda", "Nagarjunakonda", "नागार्जुनकोंडा", "नागार्जुनकोंडा", m=("Ikshvaku Buddhist remains", "इक्ष्वाकु बौद्ध अवशेष", "इक्ष्वाकू बौद्ध अवशेष")),
        it3("lepakshi", "Veerabhadra temple, Lepakshi", "वीरभद्र मंदिर, लेपाक्षी", "वीरभद्र मंदिर, लेपाक्षी", m=("Vijayanagara murals", "विजयनगर भित्तिचित्र", "विजयनगर भित्तिचित्रे")),
        it3("tirumala", "Sri Venkateswara temple, Tirumala", "श्री वेंकटेश्वर मंदिर, तिरुमला", "श्री वेंकटेश्वर मंदिर, तिरुमला", m=("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        it3("srisailam", "Srisailam (Mallikarjuna Jyotirlinga)", "श्रीशैलम (मल्लिकार्जुन ज्योतिर्लिंग)", "श्रीशैलम (मल्लिकार्जुन ज्योतिर्लिंग)", m=("Nallamala hills", "नल्लमला पहाड़ियाँ", "नल्लमला डोंगर")),
        it3("gandikota", "Gandikota fort and gorge", "गंडिकोटा क़िला और घाटी", "गंडिकोटा किल्ला व घळ", m=("Penna river", "पेन्ना नदी", "पेन्ना नदी")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("ap mod1 ok")
