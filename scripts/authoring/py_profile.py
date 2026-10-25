"""Puducherry — Phase 3 profile (core + all modules). Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from ut_kit import *

R = "IN-PY"
NAME = L("Puducherry", "पुडुचेरी", "पुदुच्चेरी")
LG = "https://www.newsonair.gov.in/k-kailashnathan-takes-oath-as-lt-governor-of-puducherry"
CM = "https://organiser.org/2026/05/13/353307/bharat/puducherry-n-rangasamy-sworn-in-as-cm-for-record-fifth-term/"
SPK = "https://puddu.neva.gov.in/"
mo = research("mospi_py.json")

r = read("regions/IN-PY.json"); m = r["metrics"]
census_metrics(m, "PY", 490, "Males 6,12,511; females 6,35,442.", 2547, 9.04,
               "Computed from ISFR 2023 forest cover 44.31 km² ÷ geographical area 490 km².")
mospi_metrics(m, mo, "Puducherry")
r["officialPortal"] = "https://py.gov.in"
r["symbols"] = {"animal": sym("Indian palm squirrel", "भारतीय गिलहरी", "भारतीय खार", "Funambulus palmarum"),
                "bird": sym("Asian koel", "कोयल", "कोकिळ", "Eudynamys scolopaceus"),
                "flower": sym("Cannonball tree flower (nagalingam)", "नागलिंगम पुष्प", "नागलिंग फूल", "Couroupita guianensis"),
                "tree": sym("Bael", "बेल", "बेल", "Aegle marmelos")}
r["government"] = {
    "headOfState": office("lieutenant-governor", L("K. Kailashnathan", "के. कैलाशनाथन", "के. कैलाशनाथन"), None, "2024-08-07", "newsonair", LG, "https://lg.py.gov.in", conf="Official",
                          note="Retired IAS officer of the Gujarat cadre; sworn in as Lieutenant Governor of Puducherry on 7 August 2024 (All India Radio News)."),
    "headOfGovernment": office("chief-minister", L("N. Rangasamy", "एन. रंगासामी", "एन. रंगासामी"), "AINRC", "2026-05-13", "organiser", CM, "https://py.gov.in", conf="Third-party verified",
                               note="Sworn in for a fifth term on 13 May 2026 at Lok Nivas by Lt Governor K. Kailashnathan, after the NDA (AINRC 12, BJP 4, AIADMK 1, LJK 1) won 18 of the 30 elected seats in the 2026 Assembly election; A. Namassivayam (BJP) and Malladi Krishna Rao (AINRC) were sworn in as ministers (Organiser)."),
    "others": [
        office("speaker", L("A. Anbalagan", "ए. अनबलगन", "ए. अनबलगन"), "AIADMK", None, "py-assembly", SPK, "https://puddu.neva.gov.in", conf="Official",
               note="Listed as Speaker on the Puducherry Legislative Assembly's NeVA portal (accessed 25 Oct 2026). He was earlier pro tem Speaker of the 16th Assembly (May 2026); the date of his election as Speaker is to be confirmed."),
    ],
}
r["projects"] = []
r["giProducts"] = gi_list("gi_py.tsv", {"Villianur Terracotta Works": ("विल्लियनूर टेराकोटा शिल्प", "विल्लियनूर टेराकोटा शिल्प"),
                                         "Tirukanur Papier Mache Craft": ("तिरुकानूर पेपर मैशे शिल्प", "तिरुकानूर पेपर मॅशे शिल्प")}, {}, set())
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-PY.json", r)
m = r["metrics"]

module(R, "overview", [
    prose("intro", L(
        "Puducherry is a Union Territory with an elected legislature, made up of four former French settlements far apart from one another: Puducherry and Karaikal on the Tamil Nadu coast, Mahe on the Kerala coast and Yanam on the Andhra Pradesh coast. Puducherry town, on the Bay of Bengal south of Chennai, is the capital.\n\nThe French ruled these enclaves until 1954, and Puducherry's French Quarter of mustard-yellow villas, tree-lined streets and seafront promenade still reflects that heritage. The town is also known for the Sri Aurobindo Ashram and, next door in Tamil Nadu, the international township of Auroville.",
        "पुडुचेरी निर्वाचित विधानसभा वाला केंद्र शासित प्रदेश है, जो एक-दूसरे से बहुत दूर स्थित चार पूर्व फ़्रांसीसी बस्तियों से बना है: तमिलनाडु तट पर पुडुचेरी और कराईकल, केरल तट पर माहे और आंध्र प्रदेश तट पर यनम। चेन्नई के दक्षिण में बंगाल की खाड़ी पर बसा पुडुचेरी नगर राजधानी है।\n\nफ़्रांसीसियों ने 1954 तक इन अंतःक्षेत्रों पर शासन किया, और पुडुचेरी का फ़्रांसीसी मोहल्ला — सरसों-पीले बंगले, पेड़ों से घिरी गलियाँ और समुद्र तटीय सैरगाह — अब भी वह विरासत दिखाता है। नगर श्री अरबिंदो आश्रम और तमिलनाडु में इसके पड़ोस की अंतरराष्ट्रीय नगरी ऑरोविल के लिए भी जाना जाता है।",
        "पुदुच्चेरी हा निवडून आलेले विधिमंडळ असलेला केंद्रशासित प्रदेश असून एकमेकांपासून दूर असलेल्या चार पूर्वीच्या फ्रेंच वसाहतींचा बनलेला आहे: तमिळनाडू किनाऱ्यावरील पुदुच्चेरी व कराईकल, केरळ किनाऱ्यावरील माहे आणि आंध्र प्रदेश किनाऱ्यावरील यानम. चेन्नईच्या दक्षिणेला बंगालच्या उपसागरावरील पुदुच्चेरी शहर ही राजधानी आहे.\n\nफ्रेंचांनी 1954 पर्यंत या भूभागांवर राज्य केले, आणि पुदुच्चेरीचा फ्रेंच भाग — मोहरी-पिवळे बंगले, झाडांनी वेढलेले रस्ते व सागरी पदपथ — अजूनही तो वारसा दाखवतो. शहर श्री अरविंद आश्रम व तमिळनाडूतील शेजारच्या ऑरोव्हिल या आंतरराष्ट्रीय नगरीसाठीही ओळखले जाते."),
        sources=["census", "fsi"], conf="Editorial"),
    admin_table([
        row("Status", "दर्जा", "दर्जा", ("Union Territory with a legislature (since 1963)", "विधानसभा वाला केंद्र शासित प्रदेश (1963 से)", "विधिमंडळ असलेला केंद्रशासित प्रदेश (1963 पासून)")),
        row("Districts", "ज़िले", "जिल्हे", ("4 (Puducherry, Karaikal, Mahe, Yanam)", "4 (पुडुचेरी, कराईकल, माहे, यनम)", "4 (पुदुच्चेरी, कराईकल, माहे, यानम)")),
        row("Capital", "राजधानी", "राजधानी", ("Puducherry", "पुडुचेरी", "पुदुच्चेरी")),
        row("Languages", "भाषाएँ", "भाषा", ("Tamil, Malayalam (Mahe) and Telugu (Yanam); English and French are also official", "तमिल, मलयालम (माहे) और तेलुगु (यनम); अंग्रेज़ी और फ़्रांसीसी भी आधिकारिक", "तमिळ, मल्याळम (माहे) व तेलुगू (यानम); इंग्रजी व फ्रेंचही अधिकृत")),
        row("High Court", "उच्च न्यायालय", "उच्च न्यायालय", ("Madras High Court", "मद्रास उच्च न्यायालय", "मद्रास उच्च न्यायालय")),
        row("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक", "PY"),
        row("Time zone", "समय क्षेत्र", "प्रमाणवेळ", "IST (UTC+05:30)"),
    ]),
])

module(R, "geography", [
    prose("p1", L(
        "Puducherry region is a flat coastal plain crossed by the Gingee and Chunnambar rivers, with Ousteri (Oussudu) lake on its western edge. Karaikal lies in the Kaveri delta about 135 km to the south, Mahe is a small enclave on the Malabar coast in Kerala, and Yanam sits on the Godavari delta in Andhra Pradesh. All four are surrounded by the neighbouring States.",
        "पुडुचेरी क्षेत्र एक समतल तटीय मैदान है, जिसे गिंगी और चुन्नाम्बर नदियाँ पार करती हैं, और इसके पश्चिमी किनारे पर उस्तेरी (उसुडु) झील है। कराईकल लगभग 135 किमी दक्षिण में कावेरी डेल्टा में है, माहे केरल के मालाबार तट पर एक छोटा अंतःक्षेत्र है, और यनम आंध्र प्रदेश में गोदावरी डेल्टा पर है। चारों पड़ोसी राज्यों से घिरे हैं।",
        "पुदुच्चेरी प्रदेश हे सपाट किनारी मैदान असून गिंगी व चुन्नांबर नद्या त्यातून वाहतात, आणि त्याच्या पश्चिम कडेला उस्तेरी (उसुडू) सरोवर आहे. कराईकल सुमारे 135 किमी दक्षिणेला कावेरी त्रिभुज प्रदेशात आहे, माहे केरळच्या मलबार किनाऱ्यावरील लहान भूभाग आहे, आणि यानम आंध्र प्रदेशात गोदावरी त्रिभुज प्रदेशावर आहे. चारही भाग शेजारच्या राज्यांनी वेढलेले आहेत."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), m["area"], "number", national=IND["area"])]),
])

module(R, "climate", [
    prose("p1", L(
        "Puducherry and Karaikal have a hot, humid coastal climate, with most rain from the north-east monsoon in October–December and frequent cyclones; Mahe gets heavy south-west monsoon rain; and Yanam is hot in summer. December to March is the most pleasant time to visit.",
        "पुडुचेरी और कराईकल की जलवायु गर्म, आर्द्र तटीय है, जहाँ अधिकांश वर्षा अक्टूबर–दिसंबर में उत्तर-पूर्व मानसून से होती है और चक्रवात बार-बार आते हैं; माहे में भारी दक्षिण-पश्चिम मानसूनी वर्षा होती है; और यनम गर्मियों में गर्म रहता है। दिसंबर से मार्च घूमने का सबसे सुहावना समय है।",
        "पुदुच्चेरी व कराईकलचे हवामान उष्ण, दमट किनारी आहे, जिथे बहुतांश पाऊस ऑक्टोबर–डिसेंबरमध्ये ईशान्य मान्सूनमुळे पडतो व चक्रीवादळे वारंवार येतात; माहेमध्ये मुसळधार नैर्ऋत्य मान्सूनी पाऊस पडतो; आणि यानम उन्हाळ्यात उष्ण असते. डिसेंबर ते मार्च भेटीसाठी सर्वांत सुखद काळ आहे."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Puducherry", "पुडुचेरी", "पुदुच्चेरी"), "lat": 11.9416, "lon": 79.8083},
        {"name": L("Karaikal", "कराईकल", "कराईकल"), "lat": 10.9254, "lon": 79.8380},
        {"name": L("Mahe", "माहे", "माहे"), "lat": 11.7010, "lon": 75.5365},
        {"name": L("Yanam", "यनम", "यानम"), "lat": 16.7333, "lon": 82.2167},
    ]},
])

module(R, "vibe", [
    prose("p1", L(
        "Puducherry's White Town, with its French street names, cafés and bakeries, contrasts with the busy Tamil town across the old canal. Early morning walks on the Promenade, the calm of the Ashram, and the international community of Auroville give the town a relaxed, cosmopolitan feel that draws many visitors at weekends.",
        "फ़्रांसीसी गली-नामों, कैफ़े और बेकरियों वाला पुडुचेरी का व्हाइट टाउन पुरानी नहर के पार व्यस्त तमिल नगर से अलग है। प्रोमेनेड पर सुबह की सैर, आश्रम की शांति और ऑरोविल का अंतरराष्ट्रीय समुदाय नगर को सहज, महानगरीय माहौल देते हैं, जो सप्ताहांत पर बहुत से पर्यटकों को खींचता है।",
        "फ्रेंच रस्त्यांची नावे, कॅफे व बेकऱ्या असलेले पुदुच्चेरीचे व्हाइट टाउन जुन्या कालव्यापलीकडील गजबजलेल्या तमिळ शहराहून वेगळे आहे. प्रोमेनेडवरील पहाटेची फेरी, आश्रमाची शांतता व ऑरोव्हिलचा आंतरराष्ट्रीय समुदाय शहराला निवांत, महानगरी वातावरण देतात, जे आठवड्याच्या शेवटी अनेक पर्यटकांना आकर्षित करते."),
        conf="Editorial"),
])

module(R, "people", [
    prose("p1", L(
        "Puducherry had 12.48 lakh people at the 2011 Census, about 2,547 per km². It was one of the few regions with more women than men: 1,037 per 1,000 men, up from 1,001 in 2001. The child sex ratio was 967 and literacy 85.8%. Scheduled Castes made up 15.7% of the population. Tamil is spoken by most people, Malayalam in Mahe and Telugu in Yanam, and some families, especially those with links to France, speak French.",
        "2011 की जनगणना में पुडुचेरी की जनसंख्या 12.48 लाख थी, प्रति वर्ग किमी लगभग 2,547। यह उन कुछ क्षेत्रों में था जहाँ महिलाएँ पुरुषों से अधिक थीं: प्रति 1,000 पुरुषों पर 1,037, जो 2001 के 1,001 से अधिक है। शिशु लिंगानुपात 967 और साक्षरता 85.8% थी। अनुसूचित जातियाँ जनसंख्या का 15.7% थीं। अधिकांश लोग तमिल बोलते हैं, माहे में मलयालम और यनम में तेलुगु, और कुछ परिवार, विशेषकर फ़्रांस से संबंध वाले, फ़्रांसीसी बोलते हैं।",
        "2011 च्या जनगणनेनुसार पुदुच्चेरीची लोकसंख्या 12.48 लाख होती, प्रति चौ.किमी सुमारे 2,547. स्त्रिया पुरुषांपेक्षा जास्त असलेल्या मोजक्या प्रदेशांपैकी ते एक होते: दर 1,000 पुरुषांमागे 1,037, 2001 मधील 1,001 वरून वाढ. बाल लिंग गुणोत्तर 967 व साक्षरता 85.8% होती. अनुसूचित जाती लोकसंख्येच्या 15.7% होत्या. बहुतेक लोक तमिळ बोलतात, माहेमध्ये मल्याळम व यानममध्ये तेलुगू, आणि काही कुटुंबे, विशेषतः फ्रान्सशी संबंध असलेली, फ्रेंच बोलतात."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", people_facts("PY", m, "PY", fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
        dp(15.7, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 1.96 lakh people. No Scheduled Tribes are notified for the UT."), "percent")),
        title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
])

module(R, "history", [
    prose("p1", L(
        "Arikamedu, just south of Puducherry town, was a trading port with links to Rome around the 1st century BCE–1st century CE. The French East India Company founded Pondichéry in 1674, and it became the capital of French India; Mahe, Yanam and Karaikal were added in the 18th century, and the town changed hands several times between the French, Dutch and British. On 1 November 1954 the four settlements were transferred to India, and the treaty of cession took legal effect on 16 August 1962. The Government of Union Territories Act, 1963 gave Puducherry an elected legislature, and the name Pondicherry was officially changed to Puducherry in 2006.",
        "पुडुचेरी नगर के ठीक दक्षिण में अरिकामेडु लगभग पहली सदी ईसा पूर्व–पहली सदी ईस्वी में रोम से संबंध वाला व्यापारिक बंदरगाह था। फ़्रांसीसी ईस्ट इंडिया कंपनी ने 1674 में पोंडिशेरी की स्थापना की, और यह फ़्रांसीसी भारत की राजधानी बना; 18वीं सदी में माहे, यनम और कराईकल जुड़े, और नगर कई बार फ़्रांसीसियों, डचों और अंग्रेज़ों के बीच हाथ बदलता रहा। 1 नवंबर 1954 को चारों बस्तियाँ भारत को सौंपी गईं, और हस्तांतरण संधि 16 अगस्त 1962 को क़ानूनी रूप से प्रभावी हुई। केंद्र शासित प्रदेश शासन अधिनियम, 1963 ने पुडुचेरी को निर्वाचित विधानसभा दी, और 2006 में पॉन्डिचेरी का आधिकारिक नाम पुडुचेरी किया गया।",
        "पुदुच्चेरी शहराच्या अगदी दक्षिणेला अरिकामेडू हे सुमारे इ.स.पू. पहिले शतक–इ.स. पहिले शतक या काळात रोमशी संबंध असलेले व्यापारी बंदर होते. फ्रेंच ईस्ट इंडिया कंपनीने 1674 मध्ये पाँडिचेरीची स्थापना केली, आणि ते फ्रेंच भारताची राजधानी झाले; अठराव्या शतकात माहे, यानम व कराईकल जोडले गेले, आणि शहर फ्रेंच, डच व ब्रिटिशांमध्ये अनेकदा हस्तांतरित झाले. 1 नोव्हेंबर 1954 रोजी चारही वसाहती भारताकडे सोपवल्या गेल्या, आणि हस्तांतरण तह 16 ऑगस्ट 1962 रोजी कायदेशीररीत्या लागू झाला. केंद्रशासित प्रदेश शासन अधिनियम, 1963 ने पुदुच्चेरीला निवडून आलेले विधिमंडळ दिले, आणि 2006 मध्ये पाँडिचेरीचे अधिकृत नाव पुदुच्चेरी करण्यात आले."),
        conf="Editorial"),
    timeline([
        ev("found", 1674, L("1674", "1674", "1674"), L("French found Pondichéry", "फ़्रांसीसियों ने पोंडिशेरी बसाया", "फ्रेंचांनी पाँडिचेरी वसवले")),
        ev("transfer", 1954, L("1 November 1954", "1 नवंबर 1954", "1 नोव्हेंबर 1954"), L("De facto transfer to India", "भारत को वास्तविक हस्तांतरण", "भारताकडे प्रत्यक्ष हस्तांतरण")),
        ev("dejure", 1962, L("16 August 1962", "16 अगस्त 1962", "16 ऑगस्ट 1962"), L("Treaty of cession in force", "हस्तांतरण संधि प्रभावी", "हस्तांतरण तह लागू")),
        ev("leg", 1963, L("1963", "1963", "1963"), L("Elected legislature", "निर्वाचित विधानसभा", "निवडून आलेले विधिमंडळ")),
        ev("name", 2006, L("2006", "2006", "2006"), L("Renamed Puducherry", "नाम पुडुचेरी", "पुदुच्चेरी नामकरण")),
    ]),
    lst("heritage", [
        it3("whitetown", "French Quarter (White Town)", "फ़्रांसीसी मोहल्ला (व्हाइट टाउन)", "फ्रेंच भाग (व्हाइट टाउन)"),
        it3("ashram", "Sri Aurobindo Ashram", "श्री अरबिंदो आश्रम", "श्री अरविंद आश्रम"),
        it3("arikamedu", "Arikamedu", "अरिकामेडु", "अरिकामेडू", m=("Indo-Roman port site", "भारत-रोमन बंदरगाह स्थल", "भारत-रोमन बंदर स्थळ")),
        it3("basilica", "Basilica of the Sacred Heart of Jesus", "सेक्रेड हार्ट ऑफ़ जीसस बेसिलिका", "सेक्रेड हार्ट ऑफ जीझस बॅसिलिका"),
        it3("manakula", "Manakula Vinayagar temple", "मनकुला विनायगर मंदिर", "मनकुला विनायगर मंदिर"),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])

module(R, "culture", [
    prose("p1", L(
        "Puducherry's culture is mainly Tamil, with French, Malayali and Telugu strands. Pongal, Masi Magam (when temple deities are taken to the sea), Bastille Day on 14 July and the Fête de Pondichéry on 15 August are celebrated, and the Villianur terracotta and Tirukanur papier-mâché crafts are registered GIs. French bakeries and Creole dishes sit alongside Tamil and Chettinad cooking.",
        "पुडुचेरी की संस्कृति मुख्यतः तमिल है, जिसमें फ़्रांसीसी, मलयाली और तेलुगु धाराएँ हैं। पोंगल, मासी मगम (जब मंदिर के देवता समुद्र तक ले जाए जाते हैं), 14 जुलाई का बैस्टील दिवस और 15 अगस्त का फ़ेत द पोंडिशेरी मनाए जाते हैं, और विल्लियनूर टेराकोटा और तिरुकानूर पेपर मैशे शिल्प पंजीकृत जीआई हैं। फ़्रांसीसी बेकरियाँ और क्रियोल व्यंजन तमिल और चेट्टिनाड पाक कला के साथ मिलते हैं।",
        "पुदुच्चेरीची संस्कृती मुख्यतः तमिळ आहे, फ्रेंच, मल्याळी व तेलुगू धाग्यांसह. पोंगल, मासी मगम (जेव्हा मंदिरातील देवता समुद्रापर्यंत नेल्या जातात), 14 जुलैचा बॅस्टिल दिन व 15 ऑगस्टचा फेत द पाँडिचेरी साजरे होतात, आणि विल्लियनूर टेराकोटा व तिरुकानूर पेपर मॅशे हस्तकला नोंदणीकृत जीआय आहेत. फ्रेंच बेकऱ्या व क्रिओल पदार्थ तमिळ व चेट्टिनाड पाककलेसोबत आहेत."),
        conf="Editorial"),
])

ur = AP["plfs_ur_15plus_psss"]["PY"]; lf = AP["plfs_lfpr_2025"]["PY"]; g = mo["gsva2024_25_current_lakh"]; sh = {k: 100 * v / g["total"] for k, v in g.items()}
module(R, "economy", [
    prose("p1", L(
        f"Puducherry's GSDP at current prices was about ₹{inr(mo['gsdp']['FY2024-25'][0])} crore in FY2024-25 in the MoSPI series, and per capita NSDP ₹{inr(mo['pcnsdp']['FY2024-25'][0])}. Manufacturing — textiles, pharmaceuticals, electrical goods and auto parts in industrial estates around Puducherry and Karaikal — was about {sh['manufacturing']:.0f}% of GSVA, construction {sh['construction']:.0f}% and real estate and professional services {sh['realestate_prof']:.0f}%. Tourism, fishing and rice farming in Karaikal are other mainstays, and Karaikal has a port. The PLFS unemployment rate was {ur['2025']}% in 2025, and {lf['female']}% of women aged 15+ were in the labour force.",
        f"मोस्पी शृंखला में वित्त वर्ष 2024-25 में पुडुचेरी का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{inr(mo['gsdp']['FY2024-25'][0])} करोड़ और प्रति व्यक्ति एनएसडीपी ₹{inr(mo['pcnsdp']['FY2024-25'][0])} था। विनिर्माण — पुडुचेरी और कराईकल के आसपास औद्योगिक क्षेत्रों में वस्त्र, दवा, विद्युत सामान और ऑटो पुर्ज़े — जीएसवीए का लगभग {sh['manufacturing']:.0f}%, निर्माण {sh['construction']:.0f}% और अचल संपत्ति व व्यावसायिक सेवाएँ {sh['realestate_prof']:.0f}% थीं। पर्यटन, मछली पकड़ना और कराईकल में धान की खेती अन्य आधार हैं, और कराईकल में बंदरगाह है। पीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी, और 15+ आयु की {lf['female']}% महिलाएँ श्रम बल में थीं।",
        f"मोस्पी मालिकेनुसार आ.व. 2024-25 मध्ये पुदुच्चेरीचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{inr(mo['gsdp']['FY2024-25'][0])} कोटी व दरडोई एनएसडीपी ₹{inr(mo['pcnsdp']['FY2024-25'][0])} होते. उत्पादन उद्योग — पुदुच्चेरी व कराईकलभोवतीच्या औद्योगिक वसाहतींतील वस्त्र, औषधे, विद्युत साहित्य व वाहनांचे सुटे भाग — जीएसव्हीएच्या सुमारे {sh['manufacturing']:.0f}%, बांधकाम {sh['construction']:.0f}% व स्थावर मालमत्ता आणि व्यावसायिक सेवा {sh['realestate_prof']:.0f}% होते. पर्यटन, मासेमारी व कराईकलमधील भातशेती हे इतर आधार आहेत, आणि कराईकलमध्ये बंदर आहे. पीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता, आणि 15+ वयाच्या {lf['female']}% स्त्रिया श्रमशक्तीत होत्या."),
        sources=["mospi", "plfs"], conf="Official"),
    *econ_blocks("PY", NAME, mo),
])

module(R, "government", [
    prose("p1", L(
        "Puducherry has a 33-member Legislative Assembly — 30 elected and up to 3 nominated by the Union Government — and a Council of Ministers headed by a Chief Minister, but the Lieutenant Governor has wider powers than a State Governor, and many subjects need Union approval. It elects one member each to the Lok Sabha and the Rajya Sabha.\n\nIn the 2026 Assembly election the NDA, led by the All India N. R. Congress, won 18 of the 30 elected seats, and N. Rangasamy was sworn in as Chief Minister for a fifth term on 13 May 2026. A. Anbalagan is listed as Speaker, and K. Kailashnathan has been Lieutenant Governor since August 2024.",
        "पुडुचेरी में 33 सदस्यों की विधानसभा है — 30 निर्वाचित और केंद्र सरकार द्वारा मनोनीत अधिकतम 3 — और मुख्यमंत्री के नेतृत्व में मंत्रिपरिषद, पर उपराज्यपाल के अधिकार राज्य के राज्यपाल से अधिक व्यापक हैं, और कई विषयों के लिए केंद्र की स्वीकृति चाहिए। इससे लोकसभा और राज्यसभा में एक-एक सदस्य चुना जाता है।\n\n2026 के विधानसभा चुनाव में ऑल इंडिया एन. आर. कांग्रेस के नेतृत्व वाले एनडीए ने 30 में से 18 निर्वाचित सीटें जीतीं, और एन. रंगासामी ने 13 मई 2026 को पाँचवीं बार मुख्यमंत्री पद की शपथ ली। ए. अनबलगन अध्यक्ष के रूप में सूचीबद्ध हैं, और के. कैलाशनाथन अगस्त 2024 से उपराज्यपाल हैं।",
        "पुदुच्चेरीमध्ये 33 सदस्यांची विधानसभा आहे — 30 निवडून आलेले व केंद्र सरकारने नामनिर्देशित केलेले जास्तीत जास्त 3 — आणि मुख्यमंत्र्यांच्या नेतृत्वाखाली मंत्रिपरिषद, पण नायब राज्यपालांचे अधिकार राज्याच्या राज्यपालांपेक्षा व्यापक आहेत, आणि अनेक विषयांसाठी केंद्राची मंजुरी लागते. येथून लोकसभा व राज्यसभेवर प्रत्येकी एक सदस्य निवडला जातो.\n\n2026 च्या विधानसभा निवडणुकीत ऑल इंडिया एन. आर. काँग्रेसच्या नेतृत्वाखालील एनडीएने 30 पैकी 18 निवडून आलेल्या जागा जिंकल्या, आणि एन. रंगासामी यांनी 13 मे 2026 रोजी पाचव्यांदा मुख्यमंत्रिपदाची शपथ घेतली. ए. अनबलगन अध्यक्ष म्हणून नोंदलेले आहेत, आणि के. कैलाशनाथन ऑगस्ट 2024 पासून नायब राज्यपाल आहेत."),
        sources=["organiser", "py-assembly", "newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    gaps("g", [
        (L("2026 Assembly election — party-wise result", "2026 विधानसभा चुनाव — दलवार परिणाम", "2026 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Puducherry 2026."),
        (L("Speaker's election date — official bulletin", "अध्यक्ष के चुनाव की तिथि — आधिकारिक बुलेटिन", "अध्यक्ष निवडीची तारीख — अधिकृत बुलेटिन"), "py-assembly", "Puducherry Legislative Assembly bulletin."),
    ]),
])

module(R, "projects", [
    prose("p1", L(
        "Projects under discussion include a new airport or runway extension for Puducherry, a new integrated bus terminal and development of Karaikal port. They will be added as cards once their status is confirmed from official sources.",
        "चर्चा में परियोजनाओं में पुडुचेरी के लिए नया हवाई अड्डा या रनवे विस्तार, नया एकीकृत बस टर्मिनल और कराईकल बंदरगाह का विकास शामिल हैं। आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर इन्हें कार्ड के रूप में जोड़ा जाएगा।",
        "चर्चेतील प्रकल्पांत पुदुच्चेरीसाठी नवा विमानतळ किंवा धावपट्टी विस्तार, नवे एकात्मिक बसस्थानक व कराईकल बंदराचा विकास यांचा समावेश आहे. अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर त्यांची कार्डे जोडली जातील."),
        conf="Editorial"),
    {"type": "projects", "id": "projects"},
])

module(R, "transport", [
    prose("p1", L(
        "Puducherry is about three hours by road from Chennai along the East Coast Road, and a branch railway connects it with Villupuram on the main Chennai line. Puducherry airport has limited domestic flights. Karaikal, Mahe and Yanam are reached through the road and rail networks of Tamil Nadu, Kerala and Andhra Pradesh.",
        "पुडुचेरी ईस्ट कोस्ट रोड से चेन्नई से लगभग तीन घंटे की दूरी पर है, और एक शाखा रेल लाइन इसे मुख्य चेन्नई लाइन पर विल्लुपुरम से जोड़ती है। पुडुचेरी हवाई अड्डे से सीमित घरेलू उड़ानें हैं। कराईकल, माहे और यनम तमिलनाडु, केरल और आंध्र प्रदेश के सड़क और रेल नेटवर्क से पहुँचे जाते हैं।",
        "पुदुच्चेरी ईस्ट कोस्ट रोडने चेन्नईपासून सुमारे तीन तासांवर आहे, आणि एक शाखा रेल्वेमार्ग त्याला मुख्य चेन्नई मार्गावरील विल्लुपुरमशी जोडतो. पुदुच्चेरी विमानतळावरून मर्यादित देशांतर्गत उड्डाणे आहेत. कराईकल, माहे व यानमला तमिळनाडू, केरळ व आंध्र प्रदेशच्या रस्ते व रेल्वे जाळ्यांतून जाता येते."),
        conf="Editorial"),
])

module(R, "energy", [
    prose("p1", L(
        "Puducherry draws most of its electricity from central generating stations through the southern grid, with a small gas-based plant at Karaikal. Rooftop solar is being promoted.",
        "पुडुचेरी अपनी अधिकांश बिजली दक्षिणी ग्रिड से केंद्रीय उत्पादन केंद्रों से लेता है, कराईकल में एक छोटे गैस आधारित संयंत्र के साथ। रूफ़टॉप सौर को बढ़ावा दिया जा रहा है।",
        "पुदुच्चेरी बहुतांश वीज दक्षिण ग्रिडमार्फत केंद्रीय निर्मिती केंद्रांकडून घेते, कराईकल येथील लहान वायू-आधारित प्रकल्पासह. छतावरील सौरऊर्जेला प्रोत्साहन दिले जात आहे."),
        conf="Editorial"),
])

module(R, "digital", [
    prose("p1", L(
        "Mobile and broadband coverage is good in all four regions. Pondicherry University and engineering colleges offer computing programmes, and the UT provides many services online.",
        "चारों क्षेत्रों में मोबाइल और ब्रॉडबैंड कवरेज अच्छा है। पांडिचेरी विश्वविद्यालय और इंजीनियरिंग कॉलेज कंप्यूटिंग कार्यक्रम चलाते हैं, और केंद्र शासित प्रदेश कई सेवाएँ ऑनलाइन देता है।",
        "चारही प्रदेशांत मोबाइल व ब्रॉडबँड व्याप्ती चांगली आहे. पाँडिचेरी विद्यापीठ व अभियांत्रिकी महाविद्यालये संगणन अभ्यासक्रम चालवतात, आणि केंद्रशासित प्रदेश अनेक सेवा ऑनलाइन देतो."),
        conf="Editorial"),
])

ef, es = aishe_block("PY", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["PY"]
module(R, "education", [
    prose("p1", L(
        f"Literacy was 85.8% at the 2011 Census. The higher-education gross enrolment ratio was {AP['aishe_ger']['PY']['2021-22']}% in 2021-22 in AISHE, more than twice the national 28.4%, with women at {gf}% and men at {gm}%, helped by students from neighbouring Tamil Nadu. Pondicherry University (central), JIPMER, an institute of national importance in medicine, NIT Puducherry at Karaikal and the Lycée Français are notable institutions.",
        f"2011 की जनगणना में साक्षरता 85.8% थी। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात {AP['aishe_ger']['PY']['2021-22']}% था, जो राष्ट्रीय 28.4% के दोगुने से अधिक है, महिलाएँ {gf}% और पुरुष {gm}%, जिसमें पड़ोसी तमिलनाडु के छात्रों का योगदान है। पांडिचेरी विश्वविद्यालय (केंद्रीय), चिकित्सा में राष्ट्रीय महत्व का संस्थान जिपमर, कराईकल में एनआईटी पुडुचेरी और लिसे फ़्रांसे उल्लेखनीय संस्थान हैं।",
        f"2011 च्या जनगणनेत साक्षरता 85.8% होती. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर {AP['aishe_ger']['PY']['2021-22']}% होते, राष्ट्रीय 28.4% च्या दुपटीहून अधिक, स्त्रिया {gf}% व पुरुष {gm}%, ज्यात शेजारच्या तमिळनाडूतील विद्यार्थ्यांचा वाटा आहे. पाँडिचेरी विद्यापीठ (केंद्रीय), वैद्यकातील राष्ट्रीय महत्त्वाची संस्था जिपमर, कराईकल येथील एनआयटी पुदुच्चेरी व लिसे फ्रान्से या उल्लेखनीय संस्था आहेत."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
])

n = NF["PY"]
module(R, "health", [
    prose("p1", L(
        f"Puducherry's infant mortality rate was 6 per 1,000 live births in 2020 in the Sample Registration System, far below the national 28. In NFHS-5, {n['institutional_N5']:.1f}% of births took place in health facilities, and child stunting fell from {n['stunted'][0]}% to {n['stunted'][1]:.1f}% and wasting from {n['wasted'][0]}% to {n['wasted'][1]:.1f}%. JIPMER and the Indira Gandhi Government General Hospital serve patients from Puducherry and neighbouring Tamil Nadu.",
        f"नमूना पंजीकरण प्रणाली में 2020 में पुडुचेरी की शिशु मृत्यु दर प्रति 1,000 जीवित जन्म पर 6 थी, जो राष्ट्रीय 28 से बहुत कम है। एनएफ़एचएस-5 में {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, और बच्चों का ठिगनापन {n['stunted'][0]}% से घटकर {n['stunted'][1]:.1f}% और दुबलापन {n['wasted'][0]}% से घटकर {n['wasted'][1]:.1f}% हुआ। जिपमर और इंदिरा गांधी सरकारी सामान्य अस्पताल पुडुचेरी और पड़ोसी तमिलनाडु के मरीज़ों की सेवा करते हैं।",
        f"नमुना नोंदणी पद्धतीनुसार 2020 मध्ये पुदुच्चेरीचा अर्भक मृत्युदर दर 1,000 जिवंत जन्मांमागे 6 होता, राष्ट्रीय 28 पेक्षा खूप कमी. एनएफएचएस-5 मध्ये {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, आणि मुलांचा खुजेपणा {n['stunted'][0]}% वरून {n['stunted'][1]:.1f}% व कृशता {n['wasted'][0]}% वरून {n['wasted'][1]:.1f}% पर्यंत घटली. जिपमर व इंदिरा गांधी शासकीय सामान्य रुग्णालय पुदुच्चेरी व शेजारच्या तमिळनाडूतील रुग्णांना सेवा देतात."),
        sources=["srs", "nfhs"], conf="Official"),
    srs_facts("PY"), nfhs_block("PY"),
])

module(R, "nature", [
    prose("p1", L(
        "Forest covers only about 9% of the UT (ISFR 2023). Ousteri (Oussudu) lake, shared with Tamil Nadu, is an important wetland for migratory birds and a bird sanctuary, and mangroves line the backwaters of Puducherry and Karaikal. Coastal erosion and the loss of beaches are major concerns. There is no Ramsar site in Puducherry on the list as on 21 April 2026.",
        "केंद्र शासित प्रदेश का केवल लगभग 9% भाग वन है (आईएसएफ़आर 2023)। तमिलनाडु के साथ साझा उस्तेरी (उसुडु) झील प्रवासी पक्षियों के लिए महत्त्वपूर्ण आर्द्रभूमि और पक्षी अभयारण्य है, और पुडुचेरी और कराईकल के पश्च-जल के किनारे मैंग्रोव हैं। तटीय कटाव और तटों का नुकसान बड़ी चिंताएँ हैं। 21 अप्रैल 2026 की सूची में पुडुचेरी में कोई रामसर स्थल नहीं है।",
        "केंद्रशासित प्रदेशाचा केवळ सुमारे 9% भाग वनाच्छादित आहे (आयएसएफआर 2023). तमिळनाडूसोबत सामायिक उस्तेरी (उसुडू) सरोवर स्थलांतरित पक्ष्यांसाठी महत्त्वाचे पाणथळ व पक्षी अभयारण्य आहे, आणि पुदुच्चेरी व कराईकलच्या खाड्यांकाठी खारफुटी आहे. किनारी धूप व किनारे नष्ट होणे या मोठ्या चिंता आहेत. 21 एप्रिल 2026 च्या यादीत पुदुच्चेरीमध्ये कोणतेही रामसर स्थळ नाही."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    forest_facts("PY", m["forestCoverPct"], 0, "MoEFCC list of Ramsar sites as on 21 April 2026: none in Puducherry."),
])

module(R, "water", [
    prose("p1", L(
        "Puducherry depends almost entirely on groundwater, which has been over-pumped and is affected by seawater intrusion along the coast. Restoring old tanks and lakes, such as Bahour and Ousteri, and recharging aquifers are priorities.",
        "पुडुचेरी लगभग पूरी तरह भूजल पर निर्भर है, जिसका अत्यधिक दोहन हुआ है और तट के साथ समुद्री जल के प्रवेश से प्रभावित है। बाहूर और उस्तेरी जैसे पुराने तालाबों और झीलों का जीर्णोद्धार और भूजल पुनर्भरण प्राथमिकताएँ हैं।",
        "पुदुच्चेरी जवळपास पूर्णपणे भूजलावर अवलंबून आहे, ज्याचा अतिउपसा झाला आहे व किनाऱ्यालगत समुद्राचे पाणी घुसल्याने तो प्रभावित आहे. बाहूर व उस्तेरीसारख्या जुन्या तलाव व सरोवरांचे पुनरुज्जीवन व भूजल पुनर्भरण ही प्राधान्ये आहेत."),
        conf="Editorial"),
])

module(R, "safety", [
    prose("p1", L(
        "Puducherry and Karaikal are exposed to cyclones and storm surges from the Bay of Bengal — Cyclone Thane in 2011 and Cyclone Fengal in 2024 caused heavy damage — and the 2004 tsunami struck Karaikal hard. Mahe faces monsoon floods. Swimming at the town's rocky seafront is dangerous.",
        "पुडुचेरी और कराईकल बंगाल की खाड़ी के चक्रवातों और तूफ़ानी लहरों के प्रति संवेदनशील हैं — 2011 में चक्रवात थाने और 2024 में चक्रवात फ़ेंगल ने भारी क्षति की — और 2004 की सुनामी ने कराईकल पर भारी प्रहार किया। माहे में मानसूनी बाढ़ आती है। नगर के चट्टानी समुद्र तट पर तैरना ख़तरनाक है।",
        "पुदुच्चेरी व कराईकलला बंगालच्या उपसागरातील चक्रीवादळे व वादळी लाटांचा धोका आहे — 2011 मध्ये थाने व 2024 मध्ये फेंगल चक्रीवादळाने मोठे नुकसान केले — आणि 2004 च्या त्सुनामीचा कराईकलला मोठा फटका बसला. माहेमध्ये मान्सूनी पूर येतात. शहराच्या खडकाळ किनाऱ्यावर पोहणे धोकादायक आहे."),
        conf="Editorial"),
    emergency_table(("Puducherry", "पुडुचेरी", "पुदुच्चेरी")),
])

module(R, "gi", [
    prose("p1", L(
        "Two GIs belong to Puducherry on the GI Registry's list as on 31 December 2025, both handicrafts filed in 2010: Villianur terracotta works and Tirukanur papier-mâché craft.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में दो जीआई पुडुचेरी के हैं, दोनों 2010 में दायर हस्तशिल्प: विल्लियनूर टेराकोटा शिल्प और तिरुकानूर पेपर मैशे शिल्प।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत दोन जीआय पुदुच्चेरीचे आहेत, दोन्ही 2010 मध्ये दाखल हस्तकला: विल्लियनूर टेराकोटा शिल्प व तिरुकानूर पेपर मॅशे शिल्प."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
])

module(R, "tourism", [
    prose("p1", L(
        "Visitors walk the French Quarter and the Promenade, visit the Sri Aurobindo Ashram, the Basilica of the Sacred Heart and the Manakula Vinayagar temple, and spend time at Paradise, Serenity and Auroville beaches. Auroville's Matrimandir, the Chunnambar backwaters and Arikamedu are nearby; Karaikal has the Thirunallar Saneeswaran temple, and Mahe has a riverside promenade.",
        "पर्यटक फ़्रांसीसी मोहल्ले और प्रोमेनेड पर घूमते हैं, श्री अरबिंदो आश्रम, सेक्रेड हार्ट बेसिलिका और मनकुला विनायगर मंदिर देखते हैं, और पैराडाइज़, सेरेनिटी और ऑरोविल तटों पर समय बिताते हैं। ऑरोविल का मातृमंदिर, चुन्नाम्बर पश्च-जल और अरिकामेडु पास हैं; कराईकल में तिरुनल्लार शनीश्वरन मंदिर है, और माहे में नदी किनारे सैरगाह है।",
        "पर्यटक फ्रेंच भाग व प्रोमेनेडवर फिरतात, श्री अरविंद आश्रम, सेक्रेड हार्ट बॅसिलिका व मनकुला विनायगर मंदिर पाहतात, आणि पॅराडाइज, सेरेनिटी व ऑरोव्हिल किनाऱ्यांवर वेळ घालवतात. ऑरोव्हिलचे मातृमंदिर, चुन्नांबर खाडी व अरिकामेडू जवळ आहेत; कराईकलमध्ये तिरुनल्लार शनीश्वरन मंदिर आहे, आणि माहेमध्ये नदीकाठचा पदपथ आहे."),
        conf="Editorial"),
])

module(R, "cities", [
    lst("cities", [
        item("puducherry", L("Puducherry", "पुडुचेरी", "पुदुच्चेरी"), detail=L("Capital on the Bay of Bengal.", "बंगाल की खाड़ी पर राजधानी।", "बंगालच्या उपसागरावरील राजधानी."), meta=L("Capital", "राजधानी", "राजधानी")),
        item("karaikal", L("Karaikal", "कराईकल", "कराईकल"), detail=L("Port town in the Kaveri delta.", "कावेरी डेल्टा में बंदरगाह नगर।", "कावेरी त्रिभुज प्रदेशातील बंदर शहर."), meta=L("Port", "बंदरगाह", "बंदर")),
        item("mahe", L("Mahe", "माहे", "माहे"), detail=L("Enclave on the Kerala coast.", "केरल तट पर अंतःक्षेत्र।", "केरळ किनाऱ्यावरील भूभाग."), meta=L("Heritage", "धरोहर", "वारसा")),
        item("yanam", L("Yanam", "यनम", "यानम"), detail=L("Enclave on the Godavari in Andhra Pradesh.", "आंध्र प्रदेश में गोदावरी पर अंतःक्षेत्र।", "आंध्र प्रदेशात गोदावरीवरील भूभाग."), meta=L("Heritage", "धरोहर", "वारसा")),
    ], title=L("The four regions", "चार क्षेत्र", "चार प्रदेश"), conf="Editorial"),
])

module(R, "sports", [
    prose("p1", L(
        "Cricket, football and volleyball are popular, and the Promenade and beaches are used for running, cycling and surfing. Puducherry has had its own team in the Ranji Trophy since 2018-19.",
        "क्रिकेट, फ़ुटबॉल और वॉलीबॉल लोकप्रिय हैं, और प्रोमेनेड व तटों का उपयोग दौड़, साइकिलिंग और सर्फ़िंग के लिए होता है। 2018-19 से रणजी ट्रॉफ़ी में पुडुचेरी की अपनी टीम है।",
        "क्रिकेट, फुटबॉल व व्हॉलीबॉल लोकप्रिय आहेत, आणि प्रोमेनेड व किनारे धावणे, सायकलिंग व सर्फिंगसाठी वापरले जातात. 2018-19 पासून रणजी करंडकात पुदुच्चेरीचा स्वतःचा संघ आहे."),
        conf="Editorial"),
])

module(R, "personalities", [
    lst("people", [
        person("aurobindo", ("Sri Aurobindo", "श्री अरबिंदो", "श्री अरविंद"), ("Philosopher and yogi who settled in Puducherry in 1910.", "दार्शनिक और योगी जो 1910 में पुडुचेरी में बसे।", "तत्त्वज्ञ व योगी जे 1910 मध्ये पुदुच्चेरीत स्थायिक झाले."), ("Philosophy", "दर्शन", "तत्त्वज्ञान")),
        person("mother", ("The Mother (Mirra Alfassa)", "श्री माँ (मीरा अल्फ़ासा)", "श्री माताजी (मीरा अल्फासा)"), ("Collaborator of Sri Aurobindo and founder of Auroville.", "श्री अरबिंदो की सहयोगी और ऑरोविल की संस्थापक।", "श्री अरविंदांच्या सहकारी व ऑरोव्हिलच्या संस्थापक."), ("Spirituality", "आध्यात्म", "अध्यात्म")),
        person("bharathi", ("Subramania Bharati", "सुब्रमण्य भारती", "सुब्रह्मण्य भारती"), ("Tamil poet who lived in Puducherry in exile, 1908–1918.", "तमिल कवि जो 1908–1918 में निर्वासन में पुडुचेरी में रहे।", "तमिळ कवी जे 1908–1918 निर्वासनात पुदुच्चेरीत राहिले."), ("Literature", "साहित्य", "साहित्य")),
        person("bharathidasan", ("Bharathidasan", "भारतीदासन", "भारतीदासन"), ("Tamil poet, born in Puducherry.", "तमिल कवि, पुडुचेरी में जन्मे।", "तमिळ कवी, पुदुच्चेरीत जन्मलेले."), ("Literature", "साहित्य", "साहित्य")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

module(R, "diaspora", [
    prose("p1", L(
        "Thousands of people from Puducherry, Karaikal and Mahe hold French citizenship, many through families who opted for it in 1962, and there are sizeable communities in France and its overseas territories such as Réunion. Mahe's families also have strong links with the Gulf.",
        "पुडुचेरी, कराईकल और माहे के हज़ारों लोगों के पास फ़्रांसीसी नागरिकता है, बहुतों के परिवारों ने 1962 में इसे चुना था, और फ़्रांस और रीयूनियन जैसे उसके समुद्रपारीय क्षेत्रों में बड़े समुदाय हैं। माहे के परिवारों के खाड़ी देशों से भी मज़बूत संबंध हैं।",
        "पुदुच्चेरी, कराईकल व माहेमधील हजारो लोकांकडे फ्रेंच नागरिकत्व आहे, अनेकांच्या कुटुंबांनी 1962 मध्ये ते निवडले होते, आणि फ्रान्स व रियुनियनसारख्या त्याच्या सागरपार प्रदेशांत मोठे समुदाय आहेत. माहेच्या कुटुंबांचे आखाती देशांशीही घट्ट संबंध आहेत."),
        conf="Editorial"),
])

module(R, "civic", [links([
    it3("portal", "Government of Puducherry", "पुडुचेरी सरकार", "पुदुच्चेरी शासन", url="https://py.gov.in", src="india-gov"),
    it3("assembly", "Puducherry Legislative Assembly (NeVA)", "पुडुचेरी विधानसभा (नेवा)", "पुदुच्चेरी विधानसभा (नेवा)", url="https://puddu.neva.gov.in", src="py-assembly"), RTI])])

module(R, "trivia", [
    lst("facts", [
        triv("sr", ("Puducherry had 1,037 women per 1,000 men in 2011.", "2011 में पुडुचेरी में प्रति 1,000 पुरुषों पर 1,037 महिलाएँ थीं।", "2011 मध्ये पुदुच्चेरीत दर 1,000 पुरुषांमागे 1,037 स्त्रिया होत्या."), PYD, "census"),
        triv("four", ("The UT's four regions lie on three different coasts and in three neighbouring States.", "केंद्र शासित प्रदेश के चार क्षेत्र तीन अलग तटों और तीन पड़ोसी राज्यों में हैं।", "केंद्रशासित प्रदेशाचे चार प्रदेश तीन वेगवेगळ्या किनाऱ्यांवर व तीन शेजारच्या राज्यांत आहेत.")),
        triv("gi", ("Villianur terracotta and Tirukanur papier-mâché are registered GIs.", "विल्लियनूर टेराकोटा और तिरुकानूर पेपर मैशे पंजीकृत जीआई हैं।", "विल्लियनूर टेराकोटा व तिरुकानूर पेपर मॅशे नोंदणीकृत जीआय आहेत."), GI_PDF, "gi-registry"),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("py ok")
