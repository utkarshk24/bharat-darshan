"""Andaman and Nicobar Islands — Phase 3 profile (core + all modules). Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from ut_kit import *

R = "IN-AN"
NAME = L("Andaman and Nicobar Islands", "अंडमान और निकोबार द्वीपसमूह", "अंदमान आणि निकोबार बेटे")
LG = "https://theprint.in/india/dinesh-sharma-sworn-in-as-lieutenant-governor-of-andaman-and-nicobar/3042960/"
APT = "https://www.newsonair.gov.in/pm-narendra-modi-inaugurates-integrated-terminal-building-of-veer-savarkar-international-airport-port-blair"
mo = research("mospi_an.json")

# ---------------- core ----------------
r = read("regions/IN-AN.json"); m = r["metrics"]
census_metrics(m, "AN", 8249, "Males 2,02,871; females 1,77,710.", 46, 81.62,
               "Computed from ISFR 2023 forest cover 6,732.92 km² ÷ geographical area 8,249 km².")
mospi_metrics(m, mo, "the Andaman and Nicobar Islands")
r["officialPortal"] = "https://andaman.gov.in"
r["symbols"] = {"animal": sym("Dugong", "डुगोंग", "डुगाँग", "Dugong dugon"),
                "bird": sym("Andaman wood pigeon", "अंडमान वन कबूतर", "अंदमान वन कबूतर", "Columba palumboides"),
                "tree": sym("Andaman padauk", "अंडमान पडौक", "अंदमान पडौक", "Pterocarpus dalbergioides")}
r["government"] = {
    "headOfState": office('lieutenant-governor', L('Dinesh Sharma', 'दिनेश शर्मा', 'दिनेश शर्मा'), None, '2026-09-15', 'president-of-india', 'https://presidentofindia.nic.in/press_releases/press-communique-36', 'https://andaman.gov.in', note='Official confirmation: Rashtrapati Bhavan communique 5 Sep 2026: President appoints Dr Dinesh Sharma LG of A&N, effective from assuming charge. Sworn in as Lieutenant Governor on 15 September 2026 at Lok Niwas, Sri Vijaya Puram, by Chief Justice Ravindra Vithalrao Ghuge of the Calcutta High Court, succeeding Admiral D. K. Joshi (Retd), LG since October 2017. Former Deputy Chief Minister of Uttar Pradesh (ThePrint/PTI).', as_of='2026-10-27'),
    "headOfGovernment": None, "others": [],
}
r["projects"] = [
    proj("port-blair-terminal", L("New integrated terminal, Veer Savarkar International Airport", "वीर सावरकर अंतरराष्ट्रीय हवाई अड्डे का नया एकीकृत टर्मिनल", "वीर सावरकर आंतरराष्ट्रीय विमानतळाचे नवे एकात्मिक टर्मिनल"),
         L("A new terminal of about 40,800 m² at Sri Vijaya Puram (Port Blair), built at a cost of about ₹710 crore and able to handle about 50 lakh passengers a year, inaugurated by the Prime Minister on 18 July 2023. The airport is the islands' main link with the mainland.",
           "श्री विजयपुरम (पोर्ट ब्लेयर) में लगभग 40,800 वर्ग मीटर का नया टर्मिनल, जो लगभग ₹710 करोड़ की लागत से बना और वर्ष में लगभग 50 लाख यात्रियों को सँभाल सकता है; प्रधानमंत्री ने 18 जुलाई 2023 को इसका उद्घाटन किया। यह हवाई अड्डा द्वीपों का मुख्य भूमि से मुख्य संपर्क है।",
           "श्री विजयपुरम (पोर्ट ब्लेअर) येथील सुमारे 40,800 चौ.मी.चे नवे टर्मिनल, जे सुमारे ₹710 कोटी खर्चून बांधले गेले व वर्षाला सुमारे 50 लाख प्रवासी हाताळू शकते; पंतप्रधानांनी 18 जुलै 2023 रोजी त्याचे उद्घाटन केले. हा विमानतळ बेटांचा मुख्य भूमीशी मुख्य दुवा आहे."),
         "aviation", "Airports Authority of India", 710, "About ₹710 crore (All India Radio News, 18 Jul 2023).", "2023", None, "18 July 2023", "Completed", "newsonair", APT),
]
GI_NAMES = {
 "Andaman Karen Musley Rice": ("अंडमान करेन मुसली चावल", "अंदमान करेन मुसली तांदूळ"),
 "Nguat-Kuk-Khawtha Coconut of Andaman & Nicobar": ("अंडमान और निकोबार का ङुआत-कुक-ख़ॉथा नारियल", "अंदमान व निकोबारचा ङुआत-कुक-खॉथा नारळ"),
 "Nicobari Canoe - Hodi Craft of Andaman & Nicobar": ("निकोबारी डोंगी — होडी शिल्प", "निकोबारी होडी शिल्प"),
 "Nicobari Mat (Chatrai / Hileuoi) of Andaman & Nicobar": ("निकोबारी चटाई (चटराई / हिलेउओई)", "निकोबारी चटई (चटराई / हिलेउओई)"),
 "Padauk Wood Craft of Andaman & Nicobar": ("अंडमान और निकोबार का पडौक काष्ठ शिल्प", "अंदमान व निकोबारचे पडौक काष्ठशिल्प"),
 "Nicobari Hut of Andaman & Nicobar": ("निकोबारी झोंपड़ी", "निकोबारी झोपडी"),
 "Nicobari Tavi-i-Ngaich (Virgin Coconut Oil) of Andaman & Nicobar": ("निकोबारी तावी-इ-ङाइच (वर्जिन नारियल तेल)", "निकोबारी तावी-इ-ङाइच (व्हर्जिन नारळ तेल)"),
}
r["giProducts"] = gi_list("gi_an.tsv", GI_NAMES, {}, set())
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-AN.json", r)
m = r["metrics"]

# ---------------- modules ----------------
module(R, "overview", [
    prose("intro", L(
        "The Andaman and Nicobar Islands are a Union Territory of several hundred islands in the Bay of Bengal, stretching about 800 km from north to south and lying closer to Myanmar, Thailand and Indonesia than to mainland India. The Andaman group in the north and the Nicobar group in the south are separated by the Ten Degree Channel. Sri Vijaya Puram (Port Blair until 2024), on South Andaman, is the capital.\n\nThe islands are known for their tropical forests, coral reefs and beaches, the Cellular Jail where freedom fighters were imprisoned, and their indigenous peoples — among them the Great Andamanese, Onge, Jarawa, Sentinelese, Shompen and Nicobarese. Indira Point on Great Nicobar is the southernmost point of India.",
        "अंडमान और निकोबार द्वीपसमूह बंगाल की खाड़ी में कई सौ द्वीपों का एक केंद्र शासित प्रदेश है, जो उत्तर से दक्षिण लगभग 800 किमी तक फैला है और मुख्य भूमि भारत की तुलना में म्यांमार, थाईलैंड और इंडोनेशिया के अधिक निकट है। उत्तर में अंडमान समूह और दक्षिण में निकोबार समूह दस डिग्री चैनल से अलग हैं। दक्षिण अंडमान पर श्री विजयपुरम (2024 तक पोर्ट ब्लेयर) राजधानी है।\n\nये द्वीप अपने उष्णकटिबंधीय वनों, प्रवाल भित्तियों और तटों, उस सेल्युलर जेल जहाँ स्वतंत्रता सेनानी क़ैद रहे, और अपने मूल निवासियों के लिए जाने जाते हैं — जिनमें ग्रेट अंडमानी, ओंगे, जारवा, सेंटिनली, शोम्पेन और निकोबारी शामिल हैं। ग्रेट निकोबार पर इंदिरा पॉइंट भारत का सबसे दक्षिणी बिंदु है।",
        "अंदमान आणि निकोबार बेटे हा बंगालच्या उपसागरातील शेकडो बेटांचा केंद्रशासित प्रदेश आहे, जो उत्तर-दक्षिण सुमारे 800 किमी पसरलेला आहे आणि मुख्य भारतापेक्षा म्यानमार, थायलंड व इंडोनेशियाच्या अधिक जवळ आहे. उत्तरेकडील अंदमान समूह व दक्षिणेकडील निकोबार समूह दहा अंश खाडीने वेगळे आहेत. दक्षिण अंदमानवरील श्री विजयपुरम (2024 पर्यंत पोर्ट ब्लेअर) ही राजधानी आहे.\n\nही बेटे उष्णकटिबंधीय जंगले, प्रवाळ भित्ती व किनारे, स्वातंत्र्यसैनिकांना डांबलेला सेल्युलर तुरुंग, आणि तेथील मूळ रहिवाशांसाठी ओळखली जातात — ज्यांत ग्रेट अंदमानी, ओंगे, जारवा, सेंटिनली, शोम्पेन व निकोबारी आहेत. ग्रेट निकोबारवरील इंदिरा पॉइंट हे भारताचे दक्षिणेकडील टोक आहे."),
        sources=["census", "fsi"], conf="Editorial"),
    admin_table([
        row("Status", "दर्जा", "दर्जा", ("Union Territory without a legislature (since 1 November 1956)", "बिना विधानसभा वाला केंद्र शासित प्रदेश (1 नवंबर 1956 से)", "विधिमंडळ नसलेला केंद्रशासित प्रदेश (1 नोव्हेंबर 1956 पासून)")),
        row("Districts", "ज़िले", "जिल्हे", ("3 (South Andaman, North and Middle Andaman, Nicobar)", "3 (दक्षिण अंडमान, उत्तर और मध्य अंडमान, निकोबार)", "3 (दक्षिण अंदमान, उत्तर व मध्य अंदमान, निकोबार)")),
        row("Capital", "राजधानी", "राजधानी", ("Sri Vijaya Puram (formerly Port Blair)", "श्री विजयपुरम (पूर्व में पोर्ट ब्लेयर)", "श्री विजयपुरम (पूर्वीचे पोर्ट ब्लेअर)")),
        row("High Court", "उच्च न्यायालय", "उच्च न्यायालय", ("Calcutta High Court (circuit bench at Sri Vijaya Puram)", "कलकत्ता उच्च न्यायालय (श्री विजयपुरम में सर्किट पीठ)", "कलकत्ता उच्च न्यायालय (श्री विजयपुरम येथे सर्किट खंडपीठ)")),
        row("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक", "AN"),
        row("Time zone", "समय क्षेत्र", "प्रमाणवेळ", "IST (UTC+05:30)"),
    ]),
    gaps("g", [(L("Official count of islands", "द्वीपों की आधिकारिक संख्या", "बेटांची अधिकृत संख्या"), "survey-of-india", "Survey of India / A&N Administration.")]),
])

module(R, "geography", [
    prose("p1", L(
        "The islands are the peaks of a submerged mountain chain that continues the Arakan Yoma of Myanmar southwards towards Sumatra. Most are hilly and covered with forest, fringed by mangroves, beaches and coral reefs. Saddle Peak on North Andaman is the highest point of the Andamans, and Mount Thuillier the highest on Great Nicobar. Barren Island, east of the main Andaman chain, is an active volcano, and Narcondam is a dormant one.",
        "ये द्वीप एक जलमग्न पर्वत शृंखला की चोटियाँ हैं, जो म्यांमार की अराकान योमा को दक्षिण में सुमात्रा की ओर आगे बढ़ाती है। अधिकांश पहाड़ी और वनाच्छादित हैं, जिनके किनारे मैंग्रोव, तट और प्रवाल भित्तियाँ हैं। उत्तरी अंडमान पर सैडल पीक अंडमान का सबसे ऊँचा बिंदु है, और माउंट थुइलियर ग्रेट निकोबार का। मुख्य अंडमान शृंखला के पूर्व में बैरन द्वीप एक सक्रिय ज्वालामुखी है, और नारकोंडम सुप्त।",
        "ही बेटे एका बुडालेल्या पर्वतरांगेची शिखरे आहेत, जी म्यानमारच्या अराकान योमाला दक्षिणेकडे सुमात्राकडे पुढे नेते. बहुतेक डोंगराळ व वनाच्छादित असून त्यांच्या कडेला खारफुटी, किनारे व प्रवाळ भित्ती आहेत. उत्तर अंदमानवरील सॅडल पीक हे अंदमानचे सर्वोच्च ठिकाण आहे, आणि माउंट थुइलियर ग्रेट निकोबारचे. मुख्य अंदमान रांगेच्या पूर्वेला बॅरन बेट हा जागृत ज्वालामुखी आहे, आणि नारकोंडम सुप्त."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), m["area"], "number", national=IND["area"])]),
])

module(R, "climate", [
    prose("p1", L(
        "The islands have a warm, humid tropical climate all year, with temperatures mostly between 23 and 31 °C. Both the south-west monsoon (May to September) and the north-east monsoon (October to December) bring rain, and cyclones can form in the Bay of Bengal. December to April is the dry, calm season for travel and diving.",
        "द्वीपों की जलवायु पूरे वर्ष गर्म, आर्द्र उष्णकटिबंधीय है, तापमान अधिकतर 23 से 31 °C के बीच रहता है। दक्षिण-पश्चिम मानसून (मई से सितंबर) और उत्तर-पूर्व मानसून (अक्टूबर से दिसंबर) दोनों वर्षा लाते हैं, और बंगाल की खाड़ी में चक्रवात बन सकते हैं। दिसंबर से अप्रैल यात्रा और गोताख़ोरी का सूखा, शांत मौसम है।",
        "बेटांचे हवामान वर्षभर उष्ण, दमट उष्णकटिबंधीय असते, तापमान बहुधा 23 ते 31 °C दरम्यान. नैर्ऋत्य मान्सून (मे ते सप्टेंबर) व ईशान्य मान्सून (ऑक्टोबर ते डिसेंबर) दोन्ही पाऊस आणतात, आणि बंगालच्या उपसागरात चक्रीवादळे तयार होऊ शकतात. डिसेंबर ते एप्रिल प्रवास व डायव्हिंगसाठी कोरडा, शांत काळ असतो."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Sri Vijaya Puram", "श्री विजयपुरम", "श्री विजयपुरम"), "lat": 11.6234, "lon": 92.7265},
        {"name": L("Car Nicobar", "कार निकोबार", "कार निकोबार"), "lat": 9.1650, "lon": 92.8170},
        {"name": L("Mayabunder", "मायाबंदर", "मायाबंदर"), "lat": 12.9200, "lon": 92.9000},
    ]},
])

module(R, "vibe", [
    prose("p1", L(
        "Life in Sri Vijaya Puram is unhurried, shaped by ferry and flight timetables and the sea. Because settlers came from many parts of India — Bengal, Tamil Nadu, Kerala, Andhra Pradesh, Bihar and elsewhere — Hindi serves as a common language and festivals of every region are celebrated. On the outer islands, small fishing and farming villages depend on inter-island ships.",
        "श्री विजयपुरम का जीवन धीमा है, जो फ़ेरी और उड़ानों की समय-सारणी और समुद्र से तय होता है। क्योंकि बसने वाले भारत के कई भागों — बंगाल, तमिलनाडु, केरल, आंध्र प्रदेश, बिहार और अन्य — से आए, हिंदी सामान्य भाषा का काम करती है और हर क्षेत्र के त्योहार मनाए जाते हैं। बाहरी द्वीपों पर मछली पकड़ने और खेती वाले छोटे गाँव अंतर-द्वीप जहाज़ों पर निर्भर हैं।",
        "श्री विजयपुरममधील जीवन संथ आहे, जे फेरी व उड्डाणांच्या वेळापत्रकाने व समुद्राने ठरते. स्थायिक भारताच्या अनेक भागांतून — बंगाल, तमिळनाडू, केरळ, आंध्र प्रदेश, बिहार व इतरत्र — आल्यामुळे हिंदी सामान्य भाषा म्हणून वापरली जाते आणि प्रत्येक प्रदेशाचे सण साजरे होतात. बाहेरील बेटांवर मासेमारी व शेतीची लहान गावे आंतर-बेट जहाजांवर अवलंबून आहेत."),
        conf="Editorial"),
])

module(R, "people", [
    prose("p1", L(
        "The islands had 3.81 lakh people at the 2011 Census, about 46 per km². The sex ratio was 876 women per 1,000 men, up from 846 in 2001, and literacy 86.6%. Scheduled Tribes — the Nicobarese and the much smaller Andamanese, Onge, Jarawa, Sentinelese and Shompen communities — made up 7.5%. Most people descend from settlers, convicts and workers brought from the mainland in the 19th and 20th centuries, and from families resettled after 1947. Contact with the Sentinelese and Jarawa is restricted by law to protect them.",
        "2011 की जनगणना में द्वीपसमूह की जनसंख्या 3.81 लाख थी, प्रति वर्ग किमी लगभग 46। लिंगानुपात प्रति 1,000 पुरुषों पर 876 महिलाएँ था, जो 2001 के 846 से अधिक है, और साक्षरता 86.6%। अनुसूचित जनजातियाँ — निकोबारी और बहुत छोटे अंडमानी, ओंगे, जारवा, सेंटिनली और शोम्पेन समुदाय — 7.5% थीं। अधिकांश लोग 19वीं और 20वीं सदी में मुख्य भूमि से लाए गए बसने वालों, क़ैदियों और मज़दूरों के, और 1947 के बाद पुनर्वासित परिवारों के वंशज हैं। सेंटिनली और जारवा की रक्षा के लिए उनसे संपर्क क़ानूनन प्रतिबंधित है।",
        "2011 च्या जनगणनेनुसार बेटांची लोकसंख्या 3.81 लाख होती, प्रति चौ.किमी सुमारे 46. दर 1,000 पुरुषांमागे 876 स्त्रिया होत्या, 2001 मधील 846 वरून वाढ, आणि साक्षरता 86.6%. अनुसूचित जमाती — निकोबारी व खूप लहान अंदमानी, ओंगे, जारवा, सेंटिनली व शोम्पेन समुदाय — 7.5% होत्या. बहुतेक लोक एकोणिसाव्या व विसाव्या शतकात मुख्य भूमीतून आणलेल्या स्थायिक, कैदी व मजुरांचे, आणि 1947 नंतर पुनर्वसित कुटुंबांचे वंशज आहेत. सेंटिनली व जारवा यांच्या संरक्षणासाठी त्यांच्याशी संपर्काला कायद्याने बंदी आहे."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", people_facts("AN", m, "AN", fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
        dp(7.5, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 0.28 lakh people. No Scheduled Castes are notified for the UT."), "percent")),
        title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    gaps("g", [(L("Population of each indigenous community — official figures", "प्रत्येक मूल निवासी समुदाय की जनसंख्या — आधिकारिक आँकड़े", "प्रत्येक मूळ समुदायाची लोकसंख्या — अधिकृत आकडे"), "tribal-affairs", "Census 2011 ST tables / Andaman Adim Janjati Vikas Samiti.")]),
])

module(R, "history", [
    prose("p1", L(
        "Indigenous peoples have lived on the islands for many thousands of years. The Chola navy reached the Nicobars in the 11th century. The Danish East India Company held the Nicobars from the 18th century, and the British set up a settlement at Port Blair in 1789 and, after the uprising of 1857, a penal colony to which thousands of Indian prisoners were sent. The Cellular Jail, completed in 1906, held many freedom fighters, among them V. D. Savarkar and his brother. Japan occupied the islands from 1942 to 1945, and on 30 December 1943 Subhas Chandra Bose raised the national flag at Port Blair.\n\nThe islands became a Union Territory in 1956. The tsunami of 26 December 2004 devastated the Nicobars and parts of the Andamans. In 2018 three islands were renamed Netaji Subhas Chandra Bose Dweep (Ross), Shaheed Dweep (Neil) and Swaraj Dweep (Havelock), and in September 2024 Port Blair was renamed Sri Vijaya Puram.",
        "मूल निवासी हज़ारों वर्षों से इन द्वीपों पर रहते आए हैं। 11वीं सदी में चोल नौसेना निकोबार पहुँची। 18वीं सदी से डेनिश ईस्ट इंडिया कंपनी के पास निकोबार रहा, और अंग्रेज़ों ने 1789 में पोर्ट ब्लेयर में बस्ती बसाई और 1857 के विद्रोह के बाद एक दंड उपनिवेश बनाया, जहाँ हज़ारों भारतीय क़ैदी भेजे गए। 1906 में पूरी हुई सेल्युलर जेल में वी. डी. सावरकर और उनके भाई सहित कई स्वतंत्रता सेनानी क़ैद रहे। 1942 से 1945 तक जापान ने द्वीपों पर क़ब्ज़ा किया, और 30 दिसंबर 1943 को सुभाष चंद्र बोस ने पोर्ट ब्लेयर में राष्ट्रीय ध्वज फहराया।\n\n1956 में द्वीप केंद्र शासित प्रदेश बने। 26 दिसंबर 2004 की सुनामी ने निकोबार और अंडमान के कुछ भागों को तबाह कर दिया। 2018 में तीन द्वीपों के नाम नेताजी सुभाष चंद्र बोस द्वीप (रॉस), शहीद द्वीप (नील) और स्वराज द्वीप (हैवलॉक) रखे गए, और सितंबर 2024 में पोर्ट ब्लेयर का नाम श्री विजयपुरम किया गया।",
        "मूळ रहिवासी हजारो वर्षांपासून या बेटांवर राहत आहेत. अकराव्या शतकात चोल आरमार निकोबारला पोहोचले. अठराव्या शतकापासून डॅनिश ईस्ट इंडिया कंपनीकडे निकोबार होते, आणि ब्रिटिशांनी 1789 मध्ये पोर्ट ब्लेअर येथे वसाहत वसवली व 1857 च्या उठावानंतर दंडवसाहत उभारली, जिथे हजारो भारतीय कैदी पाठवले गेले. 1906 मध्ये पूर्ण झालेल्या सेल्युलर तुरुंगात वि. दा. सावरकर व त्यांच्या बंधूंसह अनेक स्वातंत्र्यसैनिक डांबले गेले. 1942 ते 1945 जपानने बेटे ताब्यात घेतली, आणि 30 डिसेंबर 1943 रोजी सुभाषचंद्र बोस यांनी पोर्ट ब्लेअर येथे राष्ट्रध्वज फडकवला.\n\n1956 मध्ये बेटे केंद्रशासित प्रदेश झाली. 26 डिसेंबर 2004 च्या त्सुनामीने निकोबार व अंदमानचे काही भाग उद्ध्वस्त केले. 2018 मध्ये तीन बेटांची नावे नेताजी सुभाषचंद्र बोस द्वीप (रॉस), शहीद द्वीप (नील) व स्वराज द्वीप (हॅवलॉक) ठेवली गेली, आणि सप्टेंबर 2024 मध्ये पोर्ट ब्लेअरचे नाव श्री विजयपुरम करण्यात आले."),
        conf="Editorial"),
    timeline([
        ev("settlement", 1789, L("1789", "1789", "1789"), L("British settlement at Port Blair", "पोर्ट ब्लेयर में ब्रिटिश बस्ती", "पोर्ट ब्लेअर येथे ब्रिटिश वसाहत")),
        ev("penal", 1858, L("1858", "1858", "1858"), L("Penal settlement founded", "दंड बस्ती की स्थापना", "दंडवसाहतीची स्थापना")),
        ev("cellular", 1906, L("1906", "1906", "1906"), L("Cellular Jail completed", "सेल्युलर जेल पूर्ण", "सेल्युलर तुरुंग पूर्ण")),
        ev("bose", 1943, L("30 December 1943", "30 दिसंबर 1943", "30 डिसेंबर 1943"), L("Netaji raises the national flag at Port Blair", "नेताजी ने पोर्ट ब्लेयर में ध्वज फहराया", "नेताजींनी पोर्ट ब्लेअर येथे ध्वज फडकवला")),
        ev("ut", 1956, L("1 November 1956", "1 नवंबर 1956", "1 नोव्हेंबर 1956"), L("Union Territory", "केंद्र शासित प्रदेश", "केंद्रशासित प्रदेश")),
        ev("tsunami", 2004, L("26 December 2004", "26 दिसंबर 2004", "26 डिसेंबर 2004"), L("Indian Ocean tsunami", "हिंद महासागर सुनामी", "हिंदी महासागर त्सुनामी")),
        ev("rename", 2024, L("September 2024", "सितंबर 2024", "सप्टेंबर 2024"), L("Port Blair renamed Sri Vijaya Puram", "पोर्ट ब्लेयर का नाम श्री विजयपुरम", "पोर्ट ब्लेअरचे नाव श्री विजयपुरम")),
    ]),
    lst("heritage", [
        it3("cellular", "Cellular Jail National Memorial", "सेल्युलर जेल राष्ट्रीय स्मारक", "सेल्युलर तुरुंग राष्ट्रीय स्मारक", m=("Sri Vijaya Puram", "श्री विजयपुरम", "श्री विजयपुरम")),
        it3("ross", "Netaji Subhas Chandra Bose Dweep (Ross Island)", "नेताजी सुभाष चंद्र बोस द्वीप (रॉस द्वीप)", "नेताजी सुभाषचंद्र बोस द्वीप (रॉस बेट)", m=("Ruins of the British headquarters", "ब्रिटिश मुख्यालय के खंडहर", "ब्रिटिश मुख्यालयाचे अवशेष")),
        it3("viper", "Viper Island", "वाइपर द्वीप", "वायपर बेट"),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])

module(R, "culture", [
    prose("p1", L(
        "Settler communities brought the festivals, food and languages of their home regions, so Durga Puja, Pongal, Onam, Diwali, Christmas and Eid are all celebrated. The Island Tourism Festival in Sri Vijaya Puram showcases performers from the islands and the mainland. Nicobarese culture is organised around villages and tuhets (joint families), with canoe races, pig festivals and ossuary feasts, and crafts such as the hodi canoe, mats and huts, now registered GIs.",
        "बसने वाले समुदाय अपने मूल क्षेत्रों के त्योहार, भोजन और भाषाएँ लाए, इसलिए दुर्गा पूजा, पोंगल, ओणम, दीवाली, क्रिसमस और ईद सभी मनाए जाते हैं। श्री विजयपुरम का द्वीप पर्यटन महोत्सव द्वीपों और मुख्य भूमि के कलाकारों को प्रस्तुत करता है। निकोबारी संस्कृति गाँवों और तुहेत (संयुक्त परिवारों) के इर्द-गिर्द है, नौका दौड़, सूअर उत्सव और अस्थि-भोज के साथ, और होडी डोंगी, चटाई और झोंपड़ी जैसे शिल्प अब पंजीकृत जीआई हैं।",
        "स्थायिक समुदायांनी आपल्या मूळ प्रदेशांचे सण, खाद्य व भाषा आणल्या, त्यामुळे दुर्गापूजा, पोंगल, ओणम, दिवाळी, नाताळ व ईद सर्व साजरे होतात. श्री विजयपुरममधील बेट पर्यटन महोत्सव बेटे व मुख्य भूमीतील कलाकारांना सादर करतो. निकोबारी संस्कृती गावे व तुहेत (संयुक्त कुटुंबे) भोवती आहे, नौकाशर्यती, डुक्कर उत्सव व अस्थिभोजांसह, आणि होडी नाव, चटया व झोपड्यांसारख्या हस्तकला आता नोंदणीकृत जीआय आहेत."),
        conf="Editorial"),
])

ur = AP["plfs_ur_15plus_psss"]["AN"]; lf = AP["plfs_lfpr_2025"]["AN"]; g = mo["gsva2024_25_current_lakh"]; sh = {k: 100 * v / g["total"] for k, v in g.items()}
module(R, "economy", [
    prose("p1", L(
        f"The islands' GSDP at current prices was about ₹{inr(mo['gsdp']['FY2024-25'][0])} crore in FY2024-25 in the MoSPI series, and per capita NSDP ₹{inr(mo['pcnsdp']['FY2024-25'][0])}. Government and defence dominate: public administration was about {sh['public_admin']:.0f}% of GSVA, construction {sh['construction']:.0f}% and transport and communication {sh['transport_comm']:.0f}%. Tourism, fishing, coconut and arecanut farming and spices are the main private activities; timber extraction was largely stopped by a Supreme Court order in 2002. The PLFS unemployment rate was high at {ur['2025']}% in 2025, while {lf['female']}% of women aged 15+ were in the labour force.",
        f"मोस्पी शृंखला में वित्त वर्ष 2024-25 में द्वीपसमूह का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{inr(mo['gsdp']['FY2024-25'][0])} करोड़ और प्रति व्यक्ति एनएसडीपी ₹{inr(mo['pcnsdp']['FY2024-25'][0])} था। सरकार और रक्षा प्रमुख हैं: लोक प्रशासन जीएसवीए का लगभग {sh['public_admin']:.0f}%, निर्माण {sh['construction']:.0f}% और परिवहन व संचार {sh['transport_comm']:.0f}% था। पर्यटन, मछली पकड़ना, नारियल और सुपारी की खेती और मसाले मुख्य निजी गतिविधियाँ हैं; 2002 में सर्वोच्च न्यायालय के आदेश से लकड़ी की कटाई काफ़ी हद तक बंद हो गई। पीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% पर ऊँची थी, जबकि 15+ आयु की {lf['female']}% महिलाएँ श्रम बल में थीं।",
        f"मोस्पी मालिकेनुसार आ.व. 2024-25 मध्ये बेटांचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{inr(mo['gsdp']['FY2024-25'][0])} कोटी व दरडोई एनएसडीपी ₹{inr(mo['pcnsdp']['FY2024-25'][0])} होते. सरकार व संरक्षण प्रमुख आहेत: लोकप्रशासन जीएसव्हीएच्या सुमारे {sh['public_admin']:.0f}%, बांधकाम {sh['construction']:.0f}% व वाहतूक आणि दळणवळण {sh['transport_comm']:.0f}% होते. पर्यटन, मासेमारी, नारळ व सुपारी शेती आणि मसाले या मुख्य खासगी क्रिया आहेत; 2002 च्या सर्वोच्च न्यायालयाच्या आदेशाने लाकूडतोड बहुतांश थांबली. पीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% इतका जास्त होता, तर 15+ वयाच्या {lf['female']}% स्त्रिया श्रमशक्तीत होत्या."),
        sources=["mospi", "plfs"], conf="Official"),
    *econ_blocks("AN", NAME, mo),
])

module(R, "government", [
    prose("p1", L(
        "The islands are a Union Territory without a legislature, administered by a Lieutenant Governor appointed by the President, with a Chief Secretary and UT departments. Elected panchayats and the Sri Vijaya Puram Municipal Council handle local matters, and the Andaman and Nicobar Command, the country's first tri-service command (2001), is based at Sri Vijaya Puram. The UT elects one member to the Lok Sabha. Dinesh Sharma has been Lieutenant Governor since 15 September 2026.",
        "द्वीपसमूह बिना विधानसभा वाला केंद्र शासित प्रदेश है, जिसका प्रशासन राष्ट्रपति द्वारा नियुक्त उपराज्यपाल मुख्य सचिव और केंद्र शासित प्रदेश के विभागों के साथ करते हैं। निर्वाचित पंचायतें और श्री विजयपुरम नगर परिषद स्थानीय विषय सँभालती हैं, और देश की पहली त्रि-सेवा कमान, अंडमान और निकोबार कमान (2001), श्री विजयपुरम में है। केंद्र शासित प्रदेश से लोकसभा का एक सदस्य चुना जाता है। दिनेश शर्मा 15 सितंबर 2026 से उपराज्यपाल हैं।",
        "बेटे हा विधिमंडळ नसलेला केंद्रशासित प्रदेश आहे, ज्याचा कारभार राष्ट्रपतींनी नेमलेले नायब राज्यपाल मुख्य सचिव व केंद्रशासित प्रदेशाच्या विभागांसह पाहतात. निवडून आलेल्या पंचायती व श्री विजयपुरम नगर परिषद स्थानिक विषय हाताळतात, आणि देशातील पहिले त्रिसेवा कमांड, अंदमान व निकोबार कमांड (2001), श्री विजयपुरम येथे आहे. केंद्रशासित प्रदेशातून लोकसभेवर एक सदस्य निवडला जातो. दिनेश शर्मा 15 सप्टेंबर 2026 पासून नायब राज्यपाल आहेत."),
        sources=["theprint"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    gaps("g", [(L("Lieutenant Governor's swearing-in — official source", "उपराज्यपाल का शपथ ग्रहण — आधिकारिक स्रोत", "नायब राज्यपालांचा शपथविधी — अधिकृत स्रोत"), "india-gov", "Replace the news report with the A&N Administration release.")]),
])

module(R, "projects", [
    prose("p1", L(
        "The new airport terminal at Sri Vijaya Puram opened in 2023. The proposed Great Nicobar development — a transshipment port at Galathea Bay, an airport, a township and a power plant — has been approved by the Union Government but has drawn concerns over forests, coral reefs and the rights of the Shompen and Nicobarese; its status will be shown from official sources only. A submarine optical-fibre cable from Chennai has linked the islands since 2020.",
        "श्री विजयपुरम में हवाई अड्डे का नया टर्मिनल 2023 में खुला। प्रस्तावित ग्रेट निकोबार विकास — गैलाथिया खाड़ी में ट्रांसशिपमेंट बंदरगाह, हवाई अड्डा, नगर और बिजलीघर — को केंद्र सरकार ने स्वीकृति दी है, पर वनों, प्रवाल भित्तियों और शोम्पेन व निकोबारी लोगों के अधिकारों को लेकर चिंताएँ उठी हैं; इसकी स्थिति केवल आधिकारिक स्रोतों से दिखाई जाएगी। 2020 से चेन्नई से समुद्री ऑप्टिकल फ़ाइबर केबल द्वीपों को जोड़ती है।",
        "श्री विजयपुरम येथील विमानतळाचे नवे टर्मिनल 2023 मध्ये सुरू झाले. प्रस्तावित ग्रेट निकोबार विकास — गॅलाथिया खाडीतील ट्रान्सशिपमेंट बंदर, विमानतळ, नगर व वीजकेंद्र — याला केंद्र सरकारने मंजुरी दिली आहे, पण जंगले, प्रवाळ भित्ती व शोम्पेन आणि निकोबारी लोकांच्या हक्कांबाबत चिंता व्यक्त झाल्या आहेत; त्याची स्थिती केवळ अधिकृत स्रोतांतून दाखवली जाईल. 2020 पासून चेन्नईहून सागरी ऑप्टिकल फायबर केबल बेटांना जोडते."),
        sources=["newsonair"], conf="Editorial"),
    {"type": "projects", "id": "projects"},
    gaps("g", [(L("Great Nicobar project — official status and clearances", "ग्रेट निकोबार परियोजना — आधिकारिक स्थिति और मंज़ूरियाँ", "ग्रेट निकोबार प्रकल्प — अधिकृत स्थिती व मंजुऱ्या"), "india-gov", "NITI Aayog / MoEFCC / ANIIDCO; cite official documents only.")]),
])

module(R, "transport", [
    prose("p1", L(
        "Flights from Chennai, Kolkata, Delhi and other cities land at Veer Savarkar International Airport. Passenger ships link Sri Vijaya Puram with Chennai, Kolkata and Visakhapatnam in about three days, and government and private ferries connect the islands. The Andaman Trunk Road runs north from the capital to Diglipur, with sections through the Jarawa reserve where stopping and photography are banned.",
        "चेन्नई, कोलकाता, दिल्ली और अन्य नगरों की उड़ानें वीर सावरकर अंतरराष्ट्रीय हवाई अड्डे पर उतरती हैं। यात्री जहाज़ श्री विजयपुरम को लगभग तीन दिन में चेन्नई, कोलकाता और विशाखापत्तनम से जोड़ते हैं, और सरकारी व निजी फ़ेरी द्वीपों को जोड़ती हैं। अंडमान ट्रंक रोड राजधानी से उत्तर में दिगलीपुर तक जाती है, जिसके कुछ भाग जारवा आरक्षित क्षेत्र से गुज़रते हैं जहाँ रुकना और फ़ोटो लेना प्रतिबंधित है।",
        "चेन्नई, कोलकाता, दिल्ली व इतर शहरांतील उड्डाणे वीर सावरकर आंतरराष्ट्रीय विमानतळावर उतरतात. प्रवासी जहाजे श्री विजयपुरमला सुमारे तीन दिवसांत चेन्नई, कोलकाता व विशाखापट्टणमशी जोडतात, आणि सरकारी व खासगी फेरी बेटे जोडतात. अंदमान ट्रंक रोड राजधानीपासून उत्तरेला दिगलीपूरपर्यंत जातो, ज्याचे काही भाग जारवा राखीव क्षेत्रातून जातात जिथे थांबणे व छायाचित्रण बंदी आहे."),
        conf="Editorial"),
])

module(R, "energy", [
    prose("p1", L(
        "The islands are not connected to the national grid, so most electricity comes from diesel generators, which is costly and polluting. Solar plants, including battery-backed projects in South Andaman, are being added to cut diesel use.",
        "द्वीप राष्ट्रीय ग्रिड से जुड़े नहीं हैं, इसलिए अधिकांश बिजली डीज़ल जनरेटरों से आती है, जो महँगी और प्रदूषणकारी है। डीज़ल का उपयोग घटाने के लिए दक्षिण अंडमान में बैटरी-समर्थित परियोजनाओं सहित सौर संयंत्र जोड़े जा रहे हैं।",
        "बेटे राष्ट्रीय ग्रिडशी जोडलेली नाहीत, त्यामुळे बहुतांश वीज डिझेल जनरेटरमधून येते, जी महाग व प्रदूषणकारी आहे. डिझेलचा वापर कमी करण्यासाठी दक्षिण अंदमानमध्ये बॅटरी-आधारित प्रकल्पांसह सौर प्रकल्प वाढवले जात आहेत."),
        conf="Editorial"),
    gaps("g", [(L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA / A&N Electricity Department.")]),
])

module(R, "digital", [
    prose("p1", L(
        "Until 2020 the islands depended on satellite links for internet. The Chennai–Andaman and Nicobar Islands submarine optical-fibre cable, inaugurated in August 2020, now connects Sri Vijaya Puram and several other islands, greatly improving mobile and broadband speeds.",
        "2020 तक द्वीप इंटरनेट के लिए उपग्रह संपर्क पर निर्भर थे। अगस्त 2020 में शुरू हुई चेन्नई–अंडमान और निकोबार द्वीपसमूह समुद्री ऑप्टिकल फ़ाइबर केबल अब श्री विजयपुरम और कई अन्य द्वीपों को जोड़ती है, जिससे मोबाइल और ब्रॉडबैंड की गति काफ़ी सुधरी है।",
        "2020 पर्यंत बेटे इंटरनेटसाठी उपग्रह जोडणीवर अवलंबून होती. ऑगस्ट 2020 मध्ये सुरू झालेली चेन्नई–अंदमान व निकोबार बेटे सागरी ऑप्टिकल फायबर केबल आता श्री विजयपुरम व इतर अनेक बेटांना जोडते, ज्यामुळे मोबाइल व ब्रॉडबँडचा वेग बराच सुधारला."),
        conf="Editorial"),
    gaps("g", [(L("Chennai–A&N submarine cable — official record", "चेन्नई–अंडमान समुद्री केबल — आधिकारिक अभिलेख", "चेन्नई–अंदमान सागरी केबल — अधिकृत नोंद"), "pib", "PIB release of 10 August 2020.")]),
])

ef, es = aishe_block("AN", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["AN"]
module(R, "education", [
    prose("p1", L(
        f"Literacy was 86.6% at the 2011 Census. The higher-education gross enrolment ratio was {AP['aishe_ger']['AN']['2021-22']}% in 2021-22 in AISHE, with women ({gf}%) ahead of men ({gm}%). Higher education is offered through colleges such as Jawaharlal Nehru Rajkeeya Mahavidyalaya and the Andaman and Nicobar Islands Institute of Medical Sciences, and the Dr. B. R. Ambedkar Institute of Technology; many students go to the mainland for degrees.",
        f"2011 की जनगणना में साक्षरता 86.6% थी। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात {AP['aishe_ger']['AN']['2021-22']}% था, महिलाएँ ({gf}%) पुरुषों ({gm}%) से आगे। उच्च शिक्षा जवाहरलाल नेहरू राजकीय महाविद्यालय, अंडमान और निकोबार द्वीपसमूह आयुर्विज्ञान संस्थान और डॉ. बी. आर. आंबेडकर प्रौद्योगिकी संस्थान जैसे संस्थानों में मिलती है; बहुत से छात्र डिग्री के लिए मुख्य भूमि जाते हैं।",
        f"2011 च्या जनगणनेत साक्षरता 86.6% होती. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर {AP['aishe_ger']['AN']['2021-22']}% होते, स्त्रिया ({gf}%) पुरुषांच्या ({gm}%) पुढे. उच्चशिक्षण जवाहरलाल नेहरू राजकीय महाविद्यालय, अंदमान व निकोबार बेटे वैद्यकीय विज्ञान संस्था व डॉ. बी. आर. आंबेडकर तंत्रज्ञान संस्था यांसारख्या संस्थांतून मिळते; अनेक विद्यार्थी पदवीसाठी मुख्य भूमीवर जातात."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
])

n = NF["AN"]
module(R, "health", [
    prose("p1", L(
        f"In NFHS-5, {n['institutional_N5']:.1f}% of births took place in health facilities; {n['stunted'][1]:.1f}% of children under five were stunted, {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight. G. B. Pant Hospital in Sri Vijaya Puram, attached to the UT's medical college, is the main referral hospital; patients from remote islands are moved by ship or helicopter, and serious cases are often referred to Chennai or Kolkata.",
        f"एनएफ़एचएस-5 में {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए; पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने, {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के थे। केंद्र शासित प्रदेश के मेडिकल कॉलेज से जुड़ा श्री विजयपुरम का जी. बी. पंत अस्पताल मुख्य रेफ़रल अस्पताल है; दूरस्थ द्वीपों के मरीज़ जहाज़ या हेलीकॉप्टर से लाए जाते हैं, और गंभीर मामले अक्सर चेन्नई या कोलकाता भेजे जाते हैं।",
        f"एनएफएचएस-5 मध्ये {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या; पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी, {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची होती. केंद्रशासित प्रदेशाच्या वैद्यकीय महाविद्यालयाशी संलग्न श्री विजयपुरमचे जी. बी. पंत रुग्णालय हे मुख्य संदर्भ रुग्णालय आहे; दुर्गम बेटांवरील रुग्ण जहाज किंवा हेलिकॉप्टरने आणले जातात, आणि गंभीर रुग्ण अनेकदा चेन्नई किंवा कोलकात्याला पाठवले जातात."),
        sources=["srs", "nfhs"], conf="Official"),
    srs_facts("AN"), nfhs_block("AN"),
])

module(R, "nature", [
    prose("p1", L(
        "About 82% of the islands is forest (ISFR 2023) — evergreen rainforest, mangroves and littoral forest — with coral reefs around most islands. Many species are found nowhere else, such as the Andaman wood pigeon, Narcondam hornbill and Nicobar megapode, and dugongs, sea turtles and saltwater crocodiles live in the surrounding waters. Mahatma Gandhi Marine National Park at Wandoor, Rani Jhansi Marine National Park and the Campbell Bay and Galathea national parks are among the islands' many protected areas, and the Great Nicobar Biosphere Reserve is part of UNESCO's network. The islands have no Ramsar site on the list as on 21 April 2026.",
        "द्वीपों का लगभग 82% भाग वन है (आईएसएफ़आर 2023) — सदाबहार वर्षावन, मैंग्रोव और तटीय वन — और अधिकांश द्वीपों के चारों ओर प्रवाल भित्तियाँ हैं। कई प्रजातियाँ कहीं और नहीं मिलतीं, जैसे अंडमान वन कबूतर, नारकोंडम धनेश और निकोबार मेगापोड, और आसपास के जल में डुगोंग, समुद्री कछुए और खारे पानी के मगरमच्छ रहते हैं। वांडूर का महात्मा गांधी समुद्री राष्ट्रीय उद्यान, रानी झाँसी समुद्री राष्ट्रीय उद्यान और कैंपबेल बे व गैलाथिया राष्ट्रीय उद्यान द्वीपों के अनेक संरक्षित क्षेत्रों में हैं, और ग्रेट निकोबार जैवमंडल आरक्षित क्षेत्र यूनेस्को नेटवर्क का भाग है। 21 अप्रैल 2026 की सूची में द्वीपों में कोई रामसर स्थल नहीं है।",
        "बेटांचा सुमारे 82% भाग वनाच्छादित आहे (आयएसएफआर 2023) — सदाहरित वर्षावन, खारफुटी व किनारी वने — आणि बहुतेक बेटांभोवती प्रवाळ भित्ती आहेत. अनेक प्रजाती इतरत्र कुठेच आढळत नाहीत, उदा. अंदमान वन कबूतर, नारकोंडम धनेश व निकोबार मेगापोड, आणि सभोवतालच्या पाण्यात डुगाँग, सागरी कासवे व खाऱ्या पाण्यातील मगरी राहतात. वांडूर येथील महात्मा गांधी सागरी राष्ट्रीय उद्यान, राणी झाशी सागरी राष्ट्रीय उद्यान आणि कॅम्पबेल बे व गॅलाथिया राष्ट्रीय उद्याने ही बेटांवरील अनेक संरक्षित क्षेत्रांपैकी आहेत, आणि ग्रेट निकोबार जैवमंडल राखीव क्षेत्र युनेस्को जाळ्याचा भाग आहे. 21 एप्रिल 2026 च्या यादीत बेटांवर कोणतेही रामसर स्थळ नाही."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    forest_facts("AN", m["forestCoverPct"], 0, "MoEFCC list of Ramsar sites as on 21 April 2026: none in the Andaman and Nicobar Islands."),
    gaps("g", [(L("Number of protected areas — official list", "संरक्षित क्षेत्रों की संख्या — आधिकारिक सूची", "संरक्षित क्षेत्रांची संख्या — अधिकृत यादी"), "india-gov", "ENVIS / Wildlife Institute of India protected-area database.")]),
])

module(R, "water", [
    prose("p1", L(
        "Despite heavy rain, the islands face water shortages in the dry season because there are no large rivers and little storage. Dhanikhari dam supplies Sri Vijaya Puram, and smaller islands depend on wells, rainwater and, increasingly, desalination.",
        "भारी वर्षा के बावजूद द्वीपों में सूखे मौसम में पानी की कमी रहती है, क्योंकि बड़ी नदियाँ नहीं हैं और भंडारण कम है। धनीखाड़ी बाँध श्री विजयपुरम को पानी देता है, और छोटे द्वीप कुओं, वर्षा जल और बढ़ते रूप से विलवणीकरण पर निर्भर हैं।",
        "मुसळधार पाऊस असूनही बेटांना कोरड्या ऋतूत पाणीटंचाई जाणवते, कारण मोठ्या नद्या नाहीत व साठवण कमी आहे. धनीखाडी धरण श्री विजयपुरमला पाणी पुरवते, आणि लहान बेटे विहिरी, पावसाचे पाणी व वाढत्या प्रमाणात निःक्षारीकरणावर अवलंबून आहेत."),
        conf="Editorial"),
])

module(R, "safety", [
    prose("p1", L(
        "The islands lie in seismic zone V on an active plate boundary; the earthquake and tsunami of December 2004 killed thousands here. Cyclones and heavy rain are other hazards. Entry to tribal reserves is prohibited, and foreign visitors need permits for some islands. Swim only at guarded beaches, and follow advice on crocodiles at creeks and mangroves.",
        "द्वीप एक सक्रिय प्लेट सीमा पर भूकंपीय क्षेत्र V में हैं; दिसंबर 2004 के भूकंप और सुनामी में यहाँ हज़ारों लोग मारे गए। चक्रवात और भारी वर्षा अन्य ख़तरे हैं। जनजातीय आरक्षित क्षेत्रों में प्रवेश प्रतिबंधित है, और विदेशी पर्यटकों को कुछ द्वीपों के लिए परमिट चाहिए। केवल सुरक्षित तटों पर तैरें, और खाड़ियों और मैंग्रोव में मगरमच्छों के बारे में सलाह मानें।",
        "बेटे सक्रिय प्लेट सीमेवर भूकंप क्षेत्र V मध्ये आहेत; डिसेंबर 2004 च्या भूकंप व त्सुनामीत येथे हजारो लोक मृत्युमुखी पडले. चक्रीवादळे व मुसळधार पाऊस हे इतर धोके आहेत. आदिवासी राखीव क्षेत्रांत प्रवेश बंदी आहे, आणि परदेशी पर्यटकांना काही बेटांसाठी परवाने लागतात. फक्त सुरक्षित किनाऱ्यांवर पोहा, आणि खाड्या व खारफुटीत मगरींबाबतचा सल्ला पाळा."),
        conf="Editorial"),
    emergency_table(("Andaman and Nicobar Islands", "अंडमान और निकोबार द्वीपसमूह", "अंदमान आणि निकोबार बेटे")),
    gaps("g", [(L("2004 tsunami — official toll for the islands", "2004 सुनामी — द्वीपों के लिए आधिकारिक मृतक संख्या", "2004 त्सुनामी — बेटांसाठी अधिकृत मृतसंख्या"), "ndma", "MHA / A&N Administration reports.")]),
])

module(R, "gi", [
    prose("p1", L(
        "Seven GIs belong to the islands on the GI Registry's list as on 31 December 2025, all filed in 2022–23: Andaman Karen Musley rice, grown by the Karen community of Middle Andaman; the Nguat-Kuk-Khawtha coconut; Nicobari virgin coconut oil (tavi-i-ngaich); and four crafts — the Nicobari hodi canoe, Nicobari mat, Nicobari hut and Padauk wood craft.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में सात जीआई द्वीपसमूह के हैं, सभी 2022–23 में दायर: मध्य अंडमान के करेन समुदाय द्वारा उगाया जाने वाला अंडमान करेन मुसली चावल; ङुआत-कुक-ख़ॉथा नारियल; निकोबारी वर्जिन नारियल तेल (तावी-इ-ङाइच); और चार शिल्प — निकोबारी होडी डोंगी, निकोबारी चटाई, निकोबारी झोंपड़ी और पडौक काष्ठ शिल्प।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत सात जीआय बेटांचे आहेत, सर्व 2022–23 मध्ये दाखल: मध्य अंदमानमधील करेन समुदायाने घेतलेला अंदमान करेन मुसली तांदूळ; ङुआत-कुक-खॉथा नारळ; निकोबारी व्हर्जिन नारळ तेल (तावी-इ-ङाइच); आणि चार हस्तकला — निकोबारी होडी नाव, निकोबारी चटई, निकोबारी झोपडी व पडौक काष्ठशिल्प."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
])

module(R, "tourism", [
    prose("p1", L(
        "Most visitors begin at Sri Vijaya Puram with the Cellular Jail and its light-and-sound show, Netaji Subhas Chandra Bose Dweep and Corbyn's Cove, then take ferries to Swaraj Dweep (Havelock) for Radhanagar beach and diving, and to Shaheed Dweep (Neil). Baratang's limestone caves and mud volcano, the Mahatma Gandhi Marine National Park at Wandoor, and Diglipur and Ross & Smith islands in the north are other highlights. The Nicobar group is closed to most tourists.",
        "अधिकांश पर्यटक श्री विजयपुरम से शुरुआत करते हैं — सेल्युलर जेल और उसका ध्वनि-प्रकाश कार्यक्रम, नेताजी सुभाष चंद्र बोस द्वीप और कॉर्बिन्स कोव — फिर फ़ेरी से राधानगर तट और गोताख़ोरी के लिए स्वराज द्वीप (हैवलॉक) और शहीद द्वीप (नील) जाते हैं। बाराटांग की चूना पत्थर गुफाएँ और मिट्टी का ज्वालामुखी, वांडूर का महात्मा गांधी समुद्री राष्ट्रीय उद्यान, और उत्तर में दिगलीपुर और रॉस व स्मिथ द्वीप अन्य आकर्षण हैं। निकोबार समूह अधिकांश पर्यटकों के लिए बंद है।",
        "बहुतेक पर्यटक श्री विजयपुरमपासून सुरुवात करतात — सेल्युलर तुरुंग व त्याचा ध्वनी-प्रकाश कार्यक्रम, नेताजी सुभाषचंद्र बोस द्वीप व कॉर्बिन्स कोव — मग फेरीने राधानगर किनारा व डायव्हिंगसाठी स्वराज द्वीप (हॅवलॉक) व शहीद द्वीप (नील) येथे जातात. बाराटांगच्या चुनखडी गुहा व चिखलाचा ज्वालामुखी, वांडूरचे महात्मा गांधी सागरी राष्ट्रीय उद्यान, आणि उत्तरेकडील दिगलीपूर व रॉस आणि स्मिथ बेटे ही इतर आकर्षणे आहेत. निकोबार समूह बहुतेक पर्यटकांसाठी बंद आहे."),
        conf="Editorial"),
    gaps("g", [(L("Tourist arrivals by year", "वर्षवार पर्यटक आगमन", "वर्षनिहाय पर्यटक आगमन"), "tourism", "A&N Tourism Department.")]),
])

module(R, "cities", [
    lst("cities", [
        item("svp", L("Sri Vijaya Puram", "श्री विजयपुरम", "श्री विजयपुरम"), detail=L("Capital and main port (Port Blair until 2024).", "राजधानी और मुख्य बंदरगाह (2024 तक पोर्ट ब्लेयर)।", "राजधानी व मुख्य बंदर (2024 पर्यंत पोर्ट ब्लेअर)."), meta=L("Capital", "राजधानी", "राजधानी")),
        item("mayabunder", L("Mayabunder", "मायाबंदर", "मायाबंदर"), detail=L("Headquarters of North and Middle Andaman.", "उत्तर और मध्य अंडमान का मुख्यालय।", "उत्तर व मध्य अंदमानचे मुख्यालय."), meta=L("Administration", "प्रशासन", "प्रशासन")),
        item("carnic", L("Car Nicobar", "कार निकोबार", "कार निकोबार"), detail=L("Headquarters of Nicobar district.", "निकोबार ज़िले का मुख्यालय।", "निकोबार जिल्ह्याचे मुख्यालय."), meta=L("Administration", "प्रशासन", "प्रशासन")),
        item("diglipur", L("Diglipur", "दिगलीपुर", "दिगलीपूर"), detail=L("Main town of North Andaman.", "उत्तरी अंडमान का मुख्य नगर।", "उत्तर अंदमानचे मुख्य शहर."), meta=L("Tourism", "पर्यटन", "पर्यटन")),
    ], title=L("Main towns", "मुख्य नगर", "मुख्य शहरे"), conf="Editorial"),
])

module(R, "sports", [
    prose("p1", L(
        "Football and volleyball are popular, and water sports — scuba diving, snorkelling, kayaking and sea-walking — are central to tourism. Canoe racing is a traditional sport of the Nicobarese.",
        "फ़ुटबॉल और वॉलीबॉल लोकप्रिय हैं, और जल क्रीड़ाएँ — स्कूबा डाइविंग, स्नॉर्कलिंग, कयाकिंग और सी-वॉकिंग — पर्यटन के केंद्र में हैं। नौका दौड़ निकोबारी लोगों का पारंपरिक खेल है।",
        "फुटबॉल व व्हॉलीबॉल लोकप्रिय आहेत, आणि जलक्रीडा — स्कूबा डायव्हिंग, स्नॉर्केलिंग, कयाकिंग व सी-वॉकिंग — पर्यटनाचा गाभा आहेत. नौकाशर्यत हा निकोबारी लोकांचा पारंपरिक खेळ आहे."),
        conf="Editorial"),
])

module(R, "personalities", [
    lst("people", [
        person("savarkar", ("V. D. Savarkar", "वी. डी. सावरकर", "वि. दा. सावरकर"), ("Imprisoned in the Cellular Jail, 1911–1921.", "1911–1921 तक सेल्युलर जेल में क़ैद।", "1911–1921 सेल्युलर तुरुंगात कैद."), ("History", "इतिहास", "इतिहास")),
        person("bose", ("Subhas Chandra Bose", "सुभाष चंद्र बोस", "सुभाषचंद्र बोस"), ("Raised the national flag at Port Blair on 30 December 1943.", "30 दिसंबर 1943 को पोर्ट ब्लेयर में राष्ट्रीय ध्वज फहराया।", "30 डिसेंबर 1943 रोजी पोर्ट ब्लेअर येथे राष्ट्रध्वज फडकवला."), ("History", "इतिहास", "इतिहास")),
        person("pandit", ("T. N. Pandit", "टी. एन. पंडित", "टी. एन. पंडित"), ("Anthropologist who led the first friendly contact with the Sentinelese in 1991.", "मानवविज्ञानी जिन्होंने 1991 में सेंटिनली लोगों से पहला मैत्रीपूर्ण संपर्क किया।", "मानववंशशास्त्रज्ञ ज्यांनी 1991 मध्ये सेंटिनली लोकांशी पहिला मैत्रीपूर्ण संपर्क केला."), ("Science", "विज्ञान", "विज्ञान")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

module(R, "diaspora", [
    prose("p1", L(
        "Many islanders keep close family ties with Tamil Nadu, West Bengal, Kerala, Andhra Pradesh and Ranchi (the home region of many forest workers' families), and students and workers move to Chennai and Kolkata. The Karen community of Middle Andaman came from Myanmar in the 1920s.",
        "बहुत से द्वीपवासी तमिलनाडु, पश्चिम बंगाल, केरल, आंध्र प्रदेश और राँची (कई वन मज़दूर परिवारों का मूल क्षेत्र) से निकट पारिवारिक संबंध रखते हैं, और छात्र व कामगार चेन्नई और कोलकाता जाते हैं। मध्य अंडमान का करेन समुदाय 1920 के दशक में म्यांमार से आया।",
        "अनेक बेटवासी तमिळनाडू, पश्चिम बंगाल, केरळ, आंध्र प्रदेश व रांची (अनेक वनमजूर कुटुंबांचा मूळ प्रदेश) येथे जवळचे कौटुंबिक संबंध ठेवतात, आणि विद्यार्थी व कामगार चेन्नई व कोलकात्याला जातात. मध्य अंदमानमधील करेन समुदाय 1920 च्या दशकात म्यानमारहून आला."),
        conf="Editorial"),
])

module(R, "civic", [links([
    it3("portal", "Andaman and Nicobar Administration", "अंडमान और निकोबार प्रशासन", "अंदमान व निकोबार प्रशासन", url="https://andaman.gov.in", src="india-gov"), RTI])])

module(R, "trivia", [
    lst("facts", [
        triv("indira", ("Indira Point on Great Nicobar is the southernmost point of India.", "ग्रेट निकोबार पर इंदिरा पॉइंट भारत का सबसे दक्षिणी बिंदु है।", "ग्रेट निकोबारवरील इंदिरा पॉइंट हे भारताचे दक्षिणेकडील टोक आहे.")),
        triv("barren", ("Barren Island is an active volcano.", "बैरन द्वीप एक सक्रिय ज्वालामुखी है।", "बॅरन बेट हा जागृत ज्वालामुखी आहे.")),
        triv("forest", ("About 82% of the islands is forest (ISFR 2023).", "द्वीपों का लगभग 82% भाग वन है (आईएसएफ़आर 2023)।", "बेटांचा सुमारे 82% भाग वनाच्छादित आहे (आयएसएफआर 2023)."), LS_FOREST, "fsi"),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("an ok", len(r["giProducts"]), "GIs")
