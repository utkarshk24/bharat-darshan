"""Karnataka modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-KA"
KAES26 = "https://data.opencity.in/dataset/699b7b8d-3813-4e44-8d70-cfdf1414ee85/resource/ee584e22-2c78-4a54-9054-74db776a9a53/download/economic_survey_2025-26_english_finalmpdf_1772796504.pdf"
KGIS = "https://kgis.ksrsac.in/kag/"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
ka = read("regions/IN-KA.json")["metrics"]; ind = read("india.json")["metrics"]
NAME = L("Karnataka", "कर्नाटक", "कर्नाटक")

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Karnataka lies on India's south-western Deccan plateau, between the Arabian Sea coast and the Western Ghats in the west and the dry interior plains that run east towards Andhra Pradesh and Tamil Nadu. It had 6.11 crore people at the 2011 Census. Bengaluru, the capital, is India's best-known technology city; Mysuru is the old royal capital; and Hubballi–Dharwad, Mangaluru, Belagavi and Kalaburagi are the main regional centres.\n\nThe State was formed on 1 November 1956 as the enlarged Mysore State, bringing together the Kannada-speaking areas of the old princely state of Mysore and of the Bombay, Madras and Hyderabad regions. It was renamed Karnataka on 1 November 1973. Kannada is the official language.",
        "कर्नाटक भारत के दक्षिण-पश्चिमी दक्कन पठार पर स्थित है — पश्चिम में अरब सागर तट और पश्चिमी घाट, और पूर्व की ओर आंध्र प्रदेश व तमिलनाडु तक फैले सूखे भीतरी मैदान। 2011 की जनगणना में यहाँ 6.11 करोड़ लोग थे। राजधानी बेंगलूरु भारत का सबसे प्रसिद्ध प्रौद्योगिकी नगर है; मैसूरु पुरानी राजधानी है; और हुब्बल्ली–धारवाड़, मंगलूरु, बेलगावी और कलबुर्गी प्रमुख क्षेत्रीय केंद्र हैं।\n\nयह राज्य 1 नवंबर 1956 को विस्तारित मैसूर राज्य के रूप में बना, जिसमें पुरानी मैसूर रियासत और बॉम्बे, मद्रास व हैदराबाद क्षेत्रों के कन्नड़-भाषी इलाक़े मिलाए गए। 1 नवंबर 1973 को इसका नाम कर्नाटक रखा गया। कन्नड़ राजभाषा है।",
        "कर्नाटक भारताच्या नैर्ऋत्य दख्खन पठारावर वसले आहे — पश्चिमेला अरबी समुद्राचा किनारा व पश्चिम घाट, आणि पूर्वेकडे आंध्र प्रदेश व तमिळनाडूपर्यंत पसरलेली कोरडी अंतर्गत मैदाने. 2011 च्या जनगणनेनुसार इथे 6.11 कोटी लोक होते. राजधानी बंगळूरु हे भारतातील सर्वांत प्रसिद्ध तंत्रज्ञान शहर आहे; म्हैसूरु ही जुनी राजधानी; आणि हुबळी–धारवाड, मंगळूरु, बेळगावी व कलबुर्गी ही प्रमुख प्रादेशिक केंद्रे आहेत.\n\nहे राज्य 1 नोव्हेंबर 1956 रोजी विस्तारित म्हैसूर राज्य म्हणून निर्माण झाले — जुन्या म्हैसूर संस्थानासोबत मुंबई, मद्रास व हैदराबाद प्रदेशांतील कन्नडभाषिक भाग जोडले गेले. 1 नोव्हेंबर 1973 रोजी त्याचे नाव कर्नाटक झाले. कन्नड ही राजभाषा आहे."),
        sources=["ka-des", "census"], conf="Editorial"),
    prose("intro-unique", L(
        "Karnataka joins some of India's oldest stone architecture to one of its newest economies. The ruins of Vijayanagara at Hampi, the Chalukya temples of Badami, Aihole and Pattadakal and the intricately carved Hoysala temples of Belur, Halebidu and Somanathapura sit a few hours from Bengaluru's software parks, research institutes and start-ups. The coffee estates of Kodagu and Chikkamagaluru, the tiger and elephant forests of Nagarahole and Bandipur, Yakshagana theatre on the coast and the Mysuru Dasara add to a State with a remarkable range.",
        "कर्नाटक भारत की सबसे पुरानी पाषाण वास्तुकला को उसकी सबसे नई अर्थव्यवस्थाओं में से एक से जोड़ता है। हम्पी में विजयनगर के खंडहर, बादामी, ऐहोले और पट्टदकल के चालुक्य मंदिर और बेलूर, हलेबीडु व सोमनाथपुर के बारीक नक़्क़ाशी वाले होयसल मंदिर बेंगलूरु के सॉफ़्टवेयर पार्कों, शोध संस्थानों और स्टार्टअप से कुछ ही घंटों की दूरी पर हैं। कोडगु और चिक्कमगलूरु के कॉफ़ी बागान, नागरहोले और बांदीपुर के बाघ व हाथी वाले वन, तट का यक्षगान रंगमंच और मैसूरु दशहरा इस राज्य की विविधता को और समृद्ध करते हैं।",
        "कर्नाटक भारतातील सर्वांत जुन्या पाषाण स्थापत्याला सर्वांत नव्या अर्थव्यवस्थांपैकी एकाशी जोडतो. हंपी येथील विजयनगरचे अवशेष, बदामी, ऐहोळे व पट्टदकल येथील चालुक्य मंदिरे आणि बेलूर, हळेबीडू व सोमनाथपूर येथील बारीक कोरीव होयसळ मंदिरे बंगळूरुच्या सॉफ्टवेअर पार्क, संशोधन संस्था व स्टार्टअपपासून काही तासांच्या अंतरावर आहेत. कोडगू व चिक्कमगळूरुचे कॉफीचे मळे, नागरहोळे व बांदीपूरची वाघ-हत्तींची जंगले, किनारपट्टीवरील यक्षगान रंगभूमी आणि म्हैसूरु दसरा या राज्याच्या वैविध्यात भर घालतात."),
        title=L("What makes Karnataka unique?", "कर्नाटक को ख़ास क्या बनाता है?", "कर्नाटकचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("State formed", "राज्य गठन", "राज्यनिर्मिती"), L("1 November 1956 (as Mysore State)", "1 नवंबर 1956 (मैसूर राज्य के रूप में)", "1 नोव्हेंबर 1956 (म्हैसूर राज्य म्हणून)")],
           [L("Renamed Karnataka", "कर्नाटक नाम", "कर्नाटक नाव"), L("1 November 1973", "1 नवंबर 1973", "1 नोव्हेंबर 1973")],
           [L("Districts", "ज़िले", "जिल्हे"), "31"],
           [L("Zilla / taluk / gram panchayats", "ज़िला / तालुक / ग्राम पंचायतें", "जिल्हा / तालुका / ग्रामपंचायती"), "31 / 239 / 5,946"],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Kannada", "कन्नड़", "कन्नड")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Bengaluru, with benches at Dharwad and Kalaburagi", "बेंगलूरु, धारवाड़ और कलबुर्गी में खंडपीठ", "बंगळूरु, धारवाड व कलबुर्गी येथे खंडपीठ")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-KA / KA"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          "ka-des", KAES26, conf="Editorial",
          note=L("Panchayat counts from the Economic Survey of Karnataka 2025-26; 31 districts as listed by Karnataka-GIS (KSRSAC). Other rows are editorial and will be linked to notifications in review.",
                 "पंचायतों की संख्या कर्नाटक आर्थिक सर्वेक्षण 2025-26 से; 31 ज़िले कर्नाटक-जीआईएस (केएसआरएसएसी) की सूची के अनुसार। बाकी पंक्तियाँ संपादकीय हैं; समीक्षा में अधिसूचनाओं से जोड़ी जाएँगी।",
                 "पंचायतींची संख्या कर्नाटक आर्थिक पाहणी 2025-26 मधून; 31 जिल्हे कर्नाटक-जीआयएस (केएसआरएसएसी) यादीनुसार. इतर ओळी संपादकीय असून तपासणीत अधिसूचनांशी जोडल्या जातील.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Karnataka has three broad regions. The narrow coastal strip (Karavali) runs about 300 km along the Arabian Sea from Karwar to Mangaluru, with estuaries, beaches and coconut and areca gardens. Behind it rise the forested Western Ghats (Malnad), among the wettest places in India, where most of the State's big rivers begin and the coffee, pepper and cardamom estates of Kodagu, Chikkamagaluru and Hassan lie. East of the Ghats the Deccan plateau (Bayaluseeme) slopes gently towards the east: the southern Maidan around Bengaluru and Mysuru is red-soil country dotted with tanks, and the north — Vijayapura, Kalaburagi, Raichur and Ballari — has black cotton soils and a hot, semi-arid climate.\n\nThe Krishna and its tributaries, the Tungabhadra, Ghataprabha, Malaprabha and Bhima, drain the north; the Kaveri, with the Hemavati and Kabini, drains the south. Westward rivers such as the Sharavati, Kali and Netravati are short and fast; the Sharavati falls 253 m at Jog Falls.",
        "कर्नाटक के तीन मुख्य क्षेत्र हैं। संकरी तटीय पट्टी (करावली) अरब सागर के साथ कारवार से मंगलूरु तक लगभग 300 किमी फैली है, जिसमें मुहाने, समुद्र तट और नारियल व सुपारी के बाग़ हैं। इसके पीछे वनाच्छादित पश्चिमी घाट (मलनाड) उठते हैं — भारत के सबसे अधिक वर्षा वाले स्थानों में से — जहाँ राज्य की अधिकांश बड़ी नदियाँ निकलती हैं और कोडगु, चिक्कमगलूरु व हासन के कॉफ़ी, काली मिर्च और इलायची के बागान हैं। घाटों के पूर्व में दक्कन पठार (बयलुसीमे) धीरे-धीरे पूर्व की ओर ढलता है: बेंगलूरु और मैसूरु के आसपास का दक्षिणी मैदान लाल मिट्टी का क्षेत्र है जिसमें जगह-जगह तालाब (केरे) हैं, और उत्तर — विजयपुरा, कलबुर्गी, रायचूर और बल्लारी — में काली कपास मिट्टी और गर्म, अर्ध-शुष्क जलवायु है।\n\nकृष्णा और उसकी सहायक नदियाँ — तुंगभद्रा, घटप्रभा, मलप्रभा और भीमा — उत्तर को सींचती हैं; कावेरी, हेमावती और काबिनी के साथ, दक्षिण को। पश्चिम की ओर बहने वाली शरावती, काली और नेत्रावती जैसी नदियाँ छोटी और तेज़ हैं; शरावती जोग जलप्रपात पर 253 मीटर नीचे गिरती है।",
        "कर्नाटकचे तीन मुख्य प्रदेश आहेत. अरुंद किनारपट्टी (करावळी) अरबी समुद्रालगत कारवारपासून मंगळूरुपर्यंत सुमारे 300 किमी पसरली आहे — खाड्या, समुद्रकिनारे आणि नारळ व सुपारीच्या बागा. तिच्यामागे वनाच्छादित पश्चिम घाट (मलनाड) उभे आहेत — भारतातील सर्वाधिक पावसाच्या ठिकाणांपैकी — जिथे राज्यातील बहुतेक मोठ्या नद्यांचा उगम होतो आणि कोडगू, चिक्कमगळूरु व हासनचे कॉफी, मिरी व वेलचीचे मळे आहेत. घाटांच्या पूर्वेला दख्खन पठार (बयलुसीमे) हळूहळू पूर्वेकडे उतरते: बंगळूरु व म्हैसूरुभोवतीचे दक्षिणी मैदान तांबड्या मातीचे असून जागोजागी तलाव (केरे) आहेत, तर उत्तरेकडे — विजयपुरा, कलबुर्गी, रायचूर व बळ्ळारी — काळी कापसाची माती आणि उष्ण, अर्धशुष्क हवामान आहे.\n\nकृष्णा व तिच्या उपनद्या — तुंगभद्रा, घटप्रभा, मलप्रभा व भीमा — उत्तरेकडील भाग, तर कावेरी, हेमावती व काबिनीसह, दक्षिणेकडील भाग सिंचतात. पश्चिमवाहिनी शरावती, काळी व नेत्रावती यांसारख्या नद्या लहान व वेगवान आहेत; शरावती जोग धबधब्यावर 253 मीटर खाली कोसळते."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), ka["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("ga", "Goa (north-west)", "गोवा (उत्तर-पश्चिम)", "गोवा (वायव्य)"), it3("mh", "Maharashtra (north)", "महाराष्ट्र (उत्तर)", "महाराष्ट्र (उत्तर)"),
        it3("tg", "Telangana (north-east)", "तेलंगाना (उत्तर-पूर्व)", "तेलंगणा (ईशान्य)"), it3("ap", "Andhra Pradesh (east)", "आंध्र प्रदेश (पूर्व)", "आंध्र प्रदेश (पूर्व)"),
        it3("tn", "Tamil Nadu (south-east)", "तमिलनाडु (दक्षिण-पूर्व)", "तमिळनाडू (आग्नेय)"), it3("kl", "Keralam (south-west)", "केरलम (दक्षिण-पश्चिम)", "केरळम (नैर्ऋत्य)"),
        it3("sea", "Arabian Sea (west)", "अरब सागर (पश्चिम)", "अरबी समुद्र (पश्चिम)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("kaveri", "Kaveri", "कावेरी", "कावेरी", d=("Rises at Talakaveri in Kodagu; KRS dam near Mysuru; flows on into Tamil Nadu.", "कोडगु के तलकावेरी से निकलती है; मैसूरु के पास केआरएस बाँध; आगे तमिलनाडु जाती है।", "कोडगूमधील तलकावेरी येथे उगम; म्हैसूरुजवळ केआरएस धरण; पुढे तमिळनाडूत जाते.")),
        it3("krishna", "Krishna", "कृष्णा", "कृष्णा", d=("Crosses the north; Almatti and Narayanpur dams.", "उत्तर से होकर बहती है; अलमट्टी और नारायणपुर बाँध।", "उत्तरेकडून वाहते; आलमट्टी व नारायणपूर धरणे.")),
        it3("tungabhadra", "Tungabhadra", "तुंगभद्रा", "तुंगभद्रा", d=("Formed by the Tunga and Bhadra; flows past Hampi; Tungabhadra dam at Hosapete.", "तुंगा और भद्रा से बनती है; हम्पी के पास से बहती है; होसपेटे में तुंगभद्रा बाँध।", "तुंगा व भद्रा यांच्या संगमाने बनते; हंपीजवळून वाहते; होसपेटे येथे तुंगभद्रा धरण.")),
        it3("sharavati", "Sharavati", "शरावती", "शरावती", d=("West-flowing; Jog Falls and the Linganamakki reservoir.", "पश्चिम की ओर बहती है; जोग जलप्रपात और लिंगनमक्की जलाशय।", "पश्चिमवाहिनी; जोग धबधबा व लिंगनमक्की जलाशय.")),
        it3("netravati", "Netravati", "नेत्रावती", "नेत्रावती", d=("Reaches the sea at Mangaluru.", "मंगलूरु में समुद्र से मिलती है।", "मंगळूरु येथे समुद्राला मिळते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Coastline length (official)", "तटरेखा की लंबाई (आधिकारिक)", "किनारपट्टीची लांबी (अधिकृत)"), "survey-of-india", "Survey of India / NHO figure for Karnataka."),
        (L("Highest point (Mullayanagiri) — official elevation", "सर्वोच्च बिंदु (मुल्लयनगिरि) — आधिकारिक ऊँचाई", "सर्वोच्च शिखर (मुल्लयनगिरी) — अधिकृत उंची"), "survey-of-india", "Survey of India or the State gazetteer."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Karnataka's climate changes sharply from west to east. The coast and the Western Ghats get very heavy south-west monsoon rain from June to September — Agumbe and parts of Uttara Kannada and Kodagu are among the wettest places in peninsular India — while the plateau in the rain shadow is much drier, and the northern districts are hot and semi-arid. Bengaluru's elevation of about 900 m keeps it mild through most of the year. Summers (March–May) are hot in the north, with temperatures above 40 °C around Kalaburagi and Raichur. The south-east of the State also gets rain from the north-east monsoon in October–November.",
        "कर्नाटक की जलवायु पश्चिम से पूर्व तेज़ी से बदलती है। तट और पश्चिमी घाट में जून से सितंबर तक दक्षिण-पश्चिम मानसून की बहुत भारी वर्षा होती है — आगुम्बे और उत्तर कन्नड़ व कोडगु के कुछ हिस्से प्रायद्वीपीय भारत के सबसे अधिक वर्षा वाले स्थानों में हैं — जबकि वृष्टि-छाया में स्थित पठार कहीं अधिक सूखा है, और उत्तरी ज़िले गर्म और अर्ध-शुष्क हैं। लगभग 900 मीटर की ऊँचाई के कारण बेंगलूरु साल के अधिकांश समय सुहावना रहता है। गर्मियाँ (मार्च–मई) उत्तर में तीखी होती हैं, और कलबुर्गी व रायचूर के आसपास तापमान 40 °C से ऊपर जाता है। राज्य के दक्षिण-पूर्व में अक्टूबर–नवंबर में उत्तर-पूर्व मानसून से भी वर्षा होती है।",
        "कर्नाटकचे हवामान पश्चिमेकडून पूर्वेकडे झपाट्याने बदलते. किनारपट्टी व पश्चिम घाटात जून ते सप्टेंबर नैर्ऋत्य मोसमी पाऊस अतिशय जोरदार पडतो — आगुंबे आणि उत्तर कन्नड व कोडगूचे काही भाग द्वीपकल्पीय भारतातील सर्वाधिक पावसाच्या ठिकाणांपैकी आहेत — तर पर्जन्यछायेतील पठार बरेच कोरडे आहे, आणि उत्तरेकडील जिल्हे उष्ण व अर्धशुष्क आहेत. सुमारे 900 मीटर उंचीमुळे बंगळूरु वर्षाच्या बहुतांश काळ सुखद राहते. उन्हाळा (मार्च–मे) उत्तरेकडे कडक असतो, आणि कलबुर्गी व रायचूरभोवती तापमान 40 °C च्या पुढे जाते. राज्याच्या आग्नेय भागात ऑक्टोबर–नोव्हेंबरमध्ये ईशान्य मोसमी पाऊसही पडतो."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Bengaluru", "बेंगलूरु", "बंगळूरु"), "lat": 12.9716, "lon": 77.5946},
        {"name": L("Mysuru", "मैसूरु", "म्हैसूरु"), "lat": 12.2958, "lon": 76.6394},
        {"name": L("Mangaluru", "मंगलूरु", "मंगळूरु"), "lat": 12.9141, "lon": 74.8560},
        {"name": L("Kalaburagi", "कलबुर्गी", "कलबुर्गी"), "lat": 17.3297, "lon": 76.8343},
    ]},
    lst("best", [
        it3("winter", "October to February", "अक्टूबर से फ़रवरी", "ऑक्टोबर ते फेब्रुवारी", d=("Best for Hampi, Badami and the north; Mysuru Dasara in September–October.", "हम्पी, बादामी और उत्तर के लिए सबसे अच्छा; सितंबर–अक्टूबर में मैसूरु दशहरा।", "हंपी, बदामी व उत्तर भागासाठी उत्तम; सप्टेंबर–ऑक्टोबरमध्ये म्हैसूरु दसरा.")),
        it3("summer", "March to May", "मार्च से मई", "मार्च ते मे", d=("Hot in the north; a good time for the hills of Kodagu and Chikkamagaluru.", "उत्तर में गर्मी; कोडगु और चिक्कमगलूरु की पहाड़ियों के लिए अच्छा समय।", "उत्तरेकडे उष्ण; कोडगू व चिक्कमगळूरुच्या डोंगरांसाठी चांगला काळ.")),
        it3("monsoon", "June to September", "जून से सितंबर", "जून ते सप्टेंबर", d=("Heavy rain on the coast and Ghats; Jog Falls at its fullest; landslide risk on ghat roads.", "तट और घाटों पर भारी वर्षा; जोग जलप्रपात पूरे वेग पर; घाट मार्गों पर भूस्खलन का ख़तरा।", "किनारपट्टी व घाटांत मुसळधार पाऊस; जोग धबधबा पूर्ण भरात; घाटरस्त्यांवर दरडींचा धोका.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (State and sub-divisions)", "सामान्य वार्षिक वर्षा (राज्य और उप-मंडल)", "सरासरी वार्षिक पाऊस (राज्य व उपविभाग)"), "imd", "IMD rainfall statistics for Coastal, North Interior and South Interior Karnataka."),
        (L("Monthly temperature and rainfall normals", "मासिक तापमान और वर्षा सामान्य", "मासिक तापमान व पर्जन्य सरासरी"), "imd", "IMD climatological normals for Bengaluru, Mangaluru, Kalaburagi."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Bengaluru sets much of Karnataka's modern pace: tech parks on the Outer Ring Road, start-up meet-ups, craft breweries and a famous traffic jam, alongside old neighbourhoods like Basavanagudi and Malleswaram where the day begins with filter coffee and idli at a darshini. Mysuru is calmer and more ceremonial, its palace lit up on Sundays and through Dasara. On the coast, Udupi and Mangaluru are known for temple food, fish curry, Yakshagana performances that run through the night and a strong tradition of banking and education. In the north, life follows the farming year, with jowar rotti, jolada rotti meals, wrestling and the music of the Dharwad gharana. Kannada film, cricket and the State's many festivals bring all these regions together.",
        "बेंगलूरु कर्नाटक की आधुनिक रफ़्तार तय करता है: आउटर रिंग रोड पर टेक पार्क, स्टार्टअप बैठकें, क्राफ़्ट ब्रूअरी और मशहूर ट्रैफ़िक जाम — और साथ ही बसवनगुडी और मल्लेश्वरम जैसे पुराने मोहल्ले, जहाँ दिन किसी दर्शिनी पर फ़िल्टर कॉफ़ी और इडली से शुरू होता है। मैसूरु शांत और अधिक रस्मी है; उसका महल रविवार को और दशहरा भर रोशनी से जगमगाता है। तट पर उडुपी और मंगलूरु मंदिर के भोजन, मछली करी, रात भर चलने वाले यक्षगान प्रदर्शन और बैंकिंग व शिक्षा की मज़बूत परंपरा के लिए जाने जाते हैं। उत्तर में जीवन खेती के साल के साथ चलता है — ज्वार की रोटी (जोलद रोट्टी) वाले भोजन, कुश्ती और धारवाड़ घराने का संगीत। कन्नड़ सिनेमा, क्रिकेट और राज्य के अनेक त्योहार इन सभी क्षेत्रों को जोड़ते हैं।",
        "बंगळूरु कर्नाटकचा आधुनिक वेग ठरवते: आउटर रिंग रोडवरील टेक पार्क, स्टार्टअप बैठका, क्राफ्ट ब्रुअरी आणि प्रसिद्ध वाहतूक कोंडी — आणि सोबतच बसवनगुडी व मल्लेश्वरमसारखे जुने भाग, जिथे दिवस एखाद्या दर्शिनीवर फिल्टर कॉफी व इडलीने सुरू होतो. म्हैसूरु शांत व अधिक समारंभप्रिय आहे; त्याचा राजवाडा रविवारी आणि दसऱ्यात दिव्यांनी उजळतो. किनारपट्टीवर उडुपी व मंगळूरु मंदिरातील भोजन, माशांची आमटी, रात्रभर चालणारे यक्षगान प्रयोग आणि बँकिंग व शिक्षणाच्या भक्कम परंपरेसाठी ओळखले जातात. उत्तरेकडे जीवन शेतीच्या वर्षचक्रानुसार चालते — ज्वारीची भाकरी (जोळद रोट्टी), कुस्ती आणि धारवाड घराण्याचे संगीत. कन्नड चित्रपट, क्रिकेट आणि राज्यातील अनेक सण या सर्व प्रदेशांना एकत्र आणतात."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "At the 2011 Census Karnataka had 6.11 crore people. The sex ratio was 973 women per 1,000 men, above the national 943, and the child sex ratio was 948. Literacy was 75.4%, above the national 73.0%, and 38.67% of people lived in towns — Bengaluru alone accounts for a large part of the urban population. Scheduled Castes made up 17.1% and Scheduled Tribes 7.0% of the population.\n\nKannada is the language of most people and the official language. Tulu and Konkani are widely spoken on the coast, Kodava in Kodagu, and Urdu, Telugu, Tamil, Marathi and Hindi in different parts of the State and especially in Bengaluru, one of India's most linguistically mixed cities.",
        "2011 की जनगणना में कर्नाटक की जनसंख्या 6.11 करोड़ थी। लिंगानुपात प्रति 1,000 पुरुषों पर 973 महिलाएँ था, जो राष्ट्रीय 943 से अधिक है, और शिशु लिंगानुपात 948 था। साक्षरता 75.4% थी, जो राष्ट्रीय 73.0% से अधिक है, और 38.67% लोग शहरों में रहते थे — अकेले बेंगलूरु शहरी आबादी का बड़ा हिस्सा है। अनुसूचित जातियाँ जनसंख्या का 17.1% और अनुसूचित जनजातियाँ 7.0% थीं।\n\nअधिकांश लोगों की भाषा और राजभाषा कन्नड़ है। तट पर तुलु और कोंकणी, कोडगु में कोडव, और राज्य के अलग-अलग हिस्सों में — ख़ासकर बेंगलूरु में, जो भारत के सबसे बहुभाषी शहरों में है — उर्दू, तेलुगु, तमिल, मराठी और हिंदी व्यापक रूप से बोली जाती हैं।",
        "2011 च्या जनगणनेनुसार कर्नाटकची लोकसंख्या 6.11 कोटी होती. दर 1,000 पुरुषांमागे 973 स्त्रिया होत्या — राष्ट्रीय 943 पेक्षा जास्त — आणि बाल लिंग गुणोत्तर 948 होते. साक्षरता 75.4% होती, राष्ट्रीय 73.0% पेक्षा जास्त, आणि 38.67% लोक शहरांत राहत होते — एकट्या बंगळूरुचा नागरी लोकसंख्येत मोठा वाटा आहे. अनुसूचित जाती लोकसंख्येच्या 17.1% आणि अनुसूचित जमाती 7.0% होत्या.\n\nबहुसंख्य लोकांची भाषा व राजभाषा कन्नड आहे. किनारपट्टीवर तुळू व कोकणी, कोडगूमध्ये कोडव, आणि राज्याच्या वेगवेगळ्या भागांत — विशेषतः भारतातील सर्वांत बहुभाषिक शहरांपैकी एक असलेल्या बंगळूरुत — उर्दू, तेलुगू, तमिळ, मराठी व हिंदी मोठ्या प्रमाणावर बोलल्या जातात."),
        sources=["census", "es-india", "ka-des"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), ka["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), ka["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"]),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), ka["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(946, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), ka["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("urb", L("Urban population", "शहरी जनसंख्या", "नागरी लोकसंख्या"), ka["urbanisation2011"], "percent", national=ind["urbanisation2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), ka["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(17.1, "%", "2011", "census", "dl-planning", SCST, note="Census 2011 SC population 104.75 lakh, as tabulated in Table 17.2 of the Delhi Planning Department's statistical annex."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(7.0, "%", "2011", "census", "dl-planning", SCST, note="Census 2011 ST population 42.49 lakh (same table)."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("kn", "Kannada", "कन्नड़", "कन्नड", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("tcy", "Tulu", "तुलु", "तुळू", m=("Dakshina Kannada and Udupi", "दक्षिण कन्नड़ और उडुपी", "दक्षिण कन्नड व उडुपी")),
        it3("kok", "Konkani", "कोंकणी", "कोकणी", m=("Coast and Uttara Kannada", "तट और उत्तर कन्नड़", "किनारपट्टी व उत्तर कन्नड")),
        it3("kodava", "Kodava", "कोडव", "कोडव", m=("Kodagu", "कोडगु", "कोडगू")),
        it3("ur", "Urdu", "उर्दू", "उर्दू"), it3("te", "Telugu", "तेलुगु", "तेलुगू"), it3("ta", "Tamil", "तमिल", "तमिळ"), it3("mr", "Marathi", "मराठी", "मराठी"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Final Population Totals for Karnataka."),
        (L("Literacy by sex", "लिंगवार साक्षरता", "लिंगनिहाय साक्षरता"), "census", "Census 2011 Primary Census Abstract."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Mother-tongue shares (Census C-16)", "मातृभाषावार हिस्सा (जनगणना C-16)", "मातृभाषानिहाय वाटा (जनगणना C-16)"), "census", "Census C-16."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Rock art and Neolithic ash mounds in the north show settlement going back thousands of years, and Ashoka's edicts at Brahmagiri and Maski mark the Mauryan frontier in the 3rd century BCE. The Kadambas of Banavasi (4th century CE) were the first major dynasty to use Kannada in administration; the Western Gangas ruled the south, and the Chalukyas of Badami (6th–8th centuries) built the rock-cut caves of Badami and the temples of Aihole and Pattadakal. The Rashtrakutas, the Chalukyas of Kalyani and the Hoysalas followed; the Hoysalas' star-shaped temples at Belur and Halebidu are high points of Indian sculpture. In the 12th century Basavanna and the Vachana poets led a social and religious reform movement at Kalyana.\n\nThe Vijayanagara empire (1336–1565), with its capital at Hampi, dominated the south until its defeat at Talikota. The Bahmani and Adil Shahi sultanates ruled the north from Gulbarga, Bidar and Bijapur, where the Gol Gumbaz stands. Mysore rose under the Wodeyars and then Hyder Ali and Tipu Sultan, who fought four wars with the British until Tipu's death at Srirangapatna in 1799. Under the restored Wodeyars, Mysore became a well-run princely state, with early hydro-electricity and the Krishna Raja Sagara dam. Kittur Chennamma's revolt of 1824 is remembered as an early challenge to British rule. The Kannada unification (Ekikarana) movement led to the creation of the State in 1956.",
        "उत्तर के शैल चित्र और नवपाषाणकालीन राख के टीले हज़ारों वर्ष पुरानी बसावट दिखाते हैं, और ब्रह्मगिरि व मस्की में अशोक के शिलालेख ईसा पूर्व तीसरी सदी में मौर्य सीमा के चिह्न हैं। बनवासी के कदंब (चौथी सदी ई.) प्रशासन में कन्नड़ का उपयोग करने वाला पहला बड़ा राजवंश थे; पश्चिमी गंगों ने दक्षिण पर शासन किया, और बादामी के चालुक्यों (छठी–आठवीं सदी) ने बादामी की गुफाएँ और ऐहोले व पट्टदकल के मंदिर बनवाए। इसके बाद राष्ट्रकूट, कल्याणी के चालुक्य और होयसल आए; बेलूर और हलेबीडु के होयसलों के तारा-आकार के मंदिर भारतीय मूर्तिकला के शिखर हैं। 12वीं सदी में बसवण्णा और वचन कवियों ने कल्याण में एक सामाजिक-धार्मिक सुधार आंदोलन चलाया।\n\nहम्पी को राजधानी बनाकर विजयनगर साम्राज्य (1336–1565) ने तालीकोटा की हार तक दक्षिण पर प्रभुत्व रखा। बहमनी और आदिलशाही सल्तनतों ने गुलबर्गा, बीदर और बीजापुर से उत्तर पर शासन किया, जहाँ गोल गुंबज़ है। मैसूर वोडेयारों और फिर हैदर अली व टीपू सुल्तान के अधीन उभरा, जिन्होंने अंग्रेज़ों से चार युद्ध लड़े, जब तक 1799 में श्रीरंगपट्टण में टीपू की मृत्यु नहीं हुई। पुनर्स्थापित वोडेयारों के अधीन मैसूर एक सुशासित रियासत बना, जहाँ शुरुआती पनबिजली और कृष्णराज सागर बाँध बने। 1824 में कित्तूर चेन्नम्मा का विद्रोह अंग्रेज़ी शासन को शुरुआती चुनौती के रूप में याद किया जाता है। कन्नड़ एकीकरण आंदोलन से 1956 में राज्य का निर्माण हुआ।",
        "उत्तरेकडील शैलचित्रे व नवाश्मयुगीन राखेचे ढिगारे हजारो वर्षांपूर्वीची वस्ती दाखवतात, आणि ब्रह्मगिरी व मस्की येथील अशोकाचे शिलालेख इ.स.पू. तिसऱ्या शतकातील मौर्य सीमेची खूण आहेत. बनवासीचे कदंब (इ.स. चौथे शतक) प्रशासनात कन्नडचा वापर करणारे पहिले मोठे राजघराणे होते; पश्चिम गंगांनी दक्षिणेवर राज्य केले, आणि बदामीच्या चालुक्यांनी (सहावे–आठवे शतक) बदामीची लेणी व ऐहोळे-पट्टदकलची मंदिरे उभारली. त्यानंतर राष्ट्रकूट, कल्याणीचे चालुक्य व होयसळ आले; बेलूर व हळेबीडूची होयसळांची ताराकृती मंदिरे भारतीय शिल्पकलेचा कळस आहेत. बाराव्या शतकात बसवण्णा व वचनकवींनी कल्याण येथे सामाजिक-धार्मिक सुधारणा चळवळ चालवली.\n\nहंपी राजधानी असलेल्या विजयनगर साम्राज्याने (1336–1565) तालिकोटच्या पराभवापर्यंत दक्षिणेवर वर्चस्व ठेवले. बहमनी व आदिलशाही सल्तनतींनी गुलबर्गा, बीदर व विजापूरहून उत्तरेवर राज्य केले, जिथे गोलघुमट आहे. म्हैसूर वोडेयार आणि नंतर हैदर अली व टिपू सुलतान यांच्या काळात उदयास आले; त्यांनी इंग्रजांशी चार युद्धे केली, 1799 मध्ये श्रीरंगपट्टण येथे टिपूचा मृत्यू होईपर्यंत. पुनर्स्थापित वोडेयारांच्या काळात म्हैसूर एक सुव्यवस्थित संस्थान बनले — सुरुवातीची जलविद्युत व कृष्णराजसागर धरण तिथेच झाले. 1824 चा कित्तूर चन्नम्मांचा उठाव इंग्रजी सत्तेला दिलेले सुरुवातीचे आव्हान म्हणून स्मरणात आहे. कन्नड एकीकरण चळवळीतून 1956 मध्ये राज्याची निर्मिती झाली."),
        conf="Editorial"),
    timeline([
        ev("ashoka", -250, L("3rd century BCE", "ईसा पूर्व तीसरी सदी", "इ.स.पू. तिसरे शतक"), L("Ashoka's edicts at Brahmagiri and Maski", "ब्रह्मगिरि और मस्की में अशोक के शिलालेख", "ब्रह्मगिरी व मस्की येथे अशोकाचे शिलालेख")),
        ev("kadamba", 345, L("c. 345 CE", "लगभग 345 ई.", "सुमारे इ.स. 345"), L("Kadamba dynasty founded at Banavasi", "बनवासी में कदंब वंश की स्थापना", "बनवासी येथे कदंब घराण्याची स्थापना")),
        ev("chalukya", 543, L("6th–8th century", "छठी–आठवीं सदी", "सहावे–आठवे शतक"), L("Chalukyas of Badami; temples of Aihole and Pattadakal", "बादामी के चालुक्य; ऐहोले और पट्टदकल के मंदिर", "बदामीचे चालुक्य; ऐहोळे व पट्टदकलची मंदिरे")),
        ev("hoysala", 1117, L("12th century", "12वीं सदी", "बारावे शतक"), L("Hoysala temple at Belur", "बेलूर में होयसल मंदिर", "बेलूर येथे होयसळ मंदिर")),
        ev("vijayanagara", 1336, L("1336", "1336", "1336"), L("Vijayanagara empire founded; capital at Hampi", "विजयनगर साम्राज्य की स्थापना; राजधानी हम्पी", "विजयनगर साम्राज्याची स्थापना; राजधानी हंपी")),
        ev("talikota", 1565, L("1565", "1565", "1565"), L("Battle of Talikota; Hampi sacked", "तालीकोटा का युद्ध; हम्पी का विनाश", "तालिकोटची लढाई; हंपीचा विध्वंस")),
        ev("tipu", 1799, L("1799", "1799", "1799"), L("Tipu Sultan killed at Srirangapatna", "श्रीरंगपट्टण में टीपू सुल्तान की मृत्यु", "श्रीरंगपट्टण येथे टिपू सुलतानचा मृत्यू")),
        ev("kittur", 1824, L("1824", "1824", "1824"), L("Kittur Chennamma's revolt", "कित्तूर चेन्नम्मा का विद्रोह", "कित्तूर चन्नम्मांचा उठाव")),
        ev("state", 1956, L("1 November 1956", "1 नवंबर 1956", "1 नोव्हेंबर 1956"), L("Unified Mysore State formed", "एकीकृत मैसूर राज्य का गठन", "एकीकृत म्हैसूर राज्याची निर्मिती")),
        ev("rename", 1973, L("1 November 1973", "1 नवंबर 1973", "1 नोव्हेंबर 1973"), L("Renamed Karnataka", "नाम कर्नाटक हुआ", "नाव कर्नाटक झाले")),
        ev("hoysalawh", 2023, L("2023", "2023", "2023"), L("Hoysala temples inscribed as a UNESCO World Heritage Site", "होयसल मंदिर यूनेस्को विश्व धरोहर स्थल घोषित", "होयसळ मंदिरे युनेस्को जागतिक वारसा स्थळ घोषित")),
    ]),
    lst("heritage", [
        it3("hampi", "Group of Monuments at Hampi", "हम्पी के स्मारक समूह", "हंपी येथील स्मारकसमूह", m=("UNESCO 1986", "यूनेस्को 1986", "युनेस्को 1986"), url=UNESCO, src="unesco-whc"),
        it3("pattadakal", "Group of Monuments at Pattadakal", "पट्टदकल के स्मारक समूह", "पट्टदकल येथील स्मारकसमूह", m=("UNESCO 1987", "यूनेस्को 1987", "युनेस्को 1987"), url=UNESCO, src="unesco-whc"),
        it3("hoysala", "Sacred Ensembles of the Hoysalas (Belur, Halebidu, Somanathapura)", "होयसलों के पवित्र मंदिर समूह (बेलूर, हलेबीडु, सोमनाथपुर)", "होयसळांचे पवित्र मंदिरसमूह (बेलूर, हळेबीडू, सोमनाथपूर)", m=("UNESCO 2023", "यूनेस्को 2023", "युनेस्को 2023"), url=UNESCO, src="unesco-whc"),
        it3("ghats", "Western Ghats (serial site, shared)", "पश्चिमी घाट (क्रमिक स्थल, साझा)", "पश्चिम घाट (मालिका स्थळ, सामायिक)", m=("UNESCO 2012", "यूनेस्को 2012", "युनेस्को 2012"), url=UNESCO, src="unesco-whc"),
        it3("golgumbaz", "Gol Gumbaz, Vijayapura", "गोल गुंबज़, विजयपुरा", "गोलघुमट, विजयपुरा", m=("Adil Shahi architecture", "आदिलशाही स्थापत्य", "आदिलशाही स्थापत्य")),
        it3("palace", "Mysuru Palace", "मैसूरु महल", "म्हैसूरु राजवाडा", m=("Wodeyar seat", "वोडेयारों का आसन", "वोडेयारांचे निवासस्थान")),
        it3("badami", "Badami cave temples", "बादामी गुफा मंदिर", "बदामी लेणी मंदिरे", m=("Chalukya", "चालुक्य", "चालुक्य")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("ka mod1 ok")
