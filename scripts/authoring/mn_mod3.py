"""Manipur modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-MN"
mn = read("regions/IN-MN.json")["metrics"]; ind = read("india.json")["metrics"]
C = research("census_b5plus.json"); F = C["forest"]["MN"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About 74% of Manipur is forest (ISFR 2023), much of it bamboo and secondary forest regrowing on old jhum fields. Loktak lake, a Ramsar site since 1990, is the heart of the valley's wetlands; its phumdis, floating mats of vegetation, carry Keibul Lamjao National Park, a park that floats on the lake and the last natural home of the sangai. Siroi hill in Ukhrul is the only known home of the Shirui lily, the State flower. Other wildlife includes the hoolock gibbon, the Mrs Hume's pheasant, clouded leopards and many hornbills, and the State has the Yangoupokpi-Lokchao and Bunning sanctuaries as well as the Zeilad and Shiroi community areas.",
        "मणिपुर का लगभग 74% भाग वन है (आईएसएफ़आर 2023), जिसका बड़ा हिस्सा बाँस और पुराने झूम खेतों पर फिर से उगता द्वितीयक वन है। 1990 से रामसर स्थल लोकटक झील घाटी की आर्द्रभूमियों का हृदय है; इसकी फुमदियाँ, वनस्पति के तैरते गद्दे, कैबुल लामजाओ राष्ट्रीय उद्यान को धारण करती हैं, जो झील पर तैरता उद्यान और संगाई का अंतिम प्राकृतिक आवास है। उखरुल की शिरुई पहाड़ी राज्य पुष्प शिरुई लिली का एकमात्र ज्ञात आवास है। अन्य वन्यजीवों में हूलॉक गिबन, मिसेज़ ह्यूम्स फ़ेज़ेंट, धूमिल तेंदुआ और कई धनेश शामिल हैं, और राज्य में यांगौपोकपी-लोकचाओ और बुनिंग अभयारण्य तथा ज़ेइलाद और शिरुई सामुदायिक क्षेत्र हैं।",
        "मणिपूरचा सुमारे 74% भाग वनाच्छादित आहे (आयएसएफआर 2023), ज्यातील बराचसा भाग बांबू व जुन्या झूम शेतांवर पुन्हा वाढणारे दुय्यम वन आहे. 1990 पासून रामसर स्थळ असलेले लोकटक सरोवर हे खोऱ्यातील पाणथळींचे हृदय आहे; त्याच्या फुमदी, वनस्पतींचे तरंगते थर, कैबुल लामजाओ राष्ट्रीय उद्यान धारण करतात, जे सरोवरावर तरंगणारे उद्यान व संगाईचे शेवटचे नैसर्गिक अधिवास आहे. उखरुलमधील शिरुई टेकडी हे राज्यपुष्प शिरुई लिलीचे एकमेव ज्ञात अधिवास आहे. इतर वन्यजीवांत हूलॉक गिबन, मिसेस ह्यूम्स फेझंट, ढगाळ बिबट्या व अनेक धनेश यांचा समावेश आहे, आणि राज्यात यांगौपोकपी-लोकचाओ व बुनिंग अभयारण्ये तसेच झेइलाद व शिरुई सामुदायिक क्षेत्रे आहेत."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), mn["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(1, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: Loktak Lake (designated 23 March 1990)."), "number"),
    ]),
    lst("protected", [
        it3("keibul", "Keibul Lamjao National Park", "कैबुल लामजाओ राष्ट्रीय उद्यान", "कैबुल लामजाओ राष्ट्रीय उद्यान", m=("Floating park; sangai", "तैरता उद्यान; संगाई", "तरंगते उद्यान; संगाई")),
        it3("loktak", "Loktak Lake", "लोकटक झील", "लोकटक सरोवर", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
        it3("sirohi", "Shirui (Siroi) National Park", "शिरुई (सिरोई) राष्ट्रीय उद्यान", "शिरुई (सिरोई) राष्ट्रीय उद्यान", m=("Shirui lily, Ukhrul", "शिरुई लिली, उखरुल", "शिरुई लिली, उखरुल")),
        it3("yangoupokpi", "Yangoupokpi-Lokchao Wildlife Sanctuary", "यांगौपोकपी-लोकचाओ वन्यजीव अभयारण्य", "यांगौपोकपी-लोकचाओ वन्यजीव अभयारण्य", m=("Myanmar border", "म्यांमार सीमा", "म्यानमार सीमा")),
        it3("bunning", "Bunning Wildlife Sanctuary", "बुनिंग वन्यजीव अभयारण्य", "बुनिंग वन्यजीव अभयारण्य", m=("Tamenglong", "तामेंगलोंग", "तामेंगलोंग")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("sangai", "Sangai (State animal)", "संगाई (राज्य पशु)", "संगाई (राज्यप्राणी)"), it3("pheasant", "Mrs Hume's pheasant (State bird)", "मिसेज़ ह्यूम्स फ़ेज़ेंट (राज्य पक्षी)", "मिसेस ह्यूम्स फेझंट (राज्यपक्षी)"),
        it3("lily", "Shirui lily (State flower)", "शिरुई लिली (राज्य पुष्प)", "शिरुई लिली (राज्यपुष्प)"), it3("gibbon", "Hoolock gibbon", "हूलॉक गिबन", "हूलॉक गिबन"),
        it3("leopard", "Clouded leopard", "धूमिल तेंदुआ", "ढगाळ बिबट्या"), it3("pengba", "Pengba (Manipur osteobrama, a fish)", "पेंगबा (एक मछली)", "पेंगबा (एक मासा)"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Sangai population — latest official census", "संगाई की संख्या — नवीनतम आधिकारिक गणना", "संगाईची संख्या — नवीनतम अधिकृत गणना"), "india-gov", "Manipur Forest Department / Wildlife Institute of India."),
        (L("Phumdi thickness and Loktak water quality", "फुमदी की मोटाई और लोकटक जल गुणवत्ता", "फुमदीची जाडी व लोकटक पाण्याची गुणवत्ता"), "india-gov", "Loktak Development Authority."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Loktak and the smaller lakes and marshes of the valley store water, support fisheries and feed the Loktak hydroelectric project, but the Ithai barrage, silt from the deforested hills and the spread of phumdis have changed the lake. Imphal's piped water comes from the Singda and Maphou dams and river intakes, and dry-season shortages are common. Hill villages depend on springs and streams, and the Khuga and Thoubal multipurpose projects irrigate parts of the valley.",
        "लोकटक और घाटी की छोटी झीलें और दलदल पानी संचित करते हैं, मत्स्य पालन को सहारा देते हैं और लोकटक जलविद्युत परियोजना को पानी देते हैं, पर इथाई बैराज, वनविहीन पहाड़ियों की गाद और फुमदियों के फैलाव ने झील को बदल दिया है। इंफाल को पाइप से पानी सिंगदा और माफ़ौ बाँधों और नदी के इनटेक से मिलता है, और सूखे मौसम में कमी आम है। पहाड़ी गाँव झरनों और धाराओं पर निर्भर हैं, और खुगा और थौबाल बहुउद्देशीय परियोजनाएँ घाटी के कुछ भागों की सिंचाई करती हैं।",
        "लोकटक व खोऱ्यातील लहान सरोवरे व दलदली पाणी साठवतात, मासेमारीला आधार देतात व लोकटक जलविद्युत प्रकल्पाला पाणी पुरवतात, पण इथाई बंधारा, वृक्षतोड झालेल्या डोंगरांतील गाळ व फुमदींचा प्रसार यांनी सरोवर बदलले आहे. इंफाळला नळाचे पाणी सिंगदा व माफौ धरणे व नदीतील उद्भवांतून मिळते, आणि कोरड्या ऋतूत टंचाई सामान्य आहे. डोंगरी गावे झरे व ओढ्यांवर अवलंबून आहेत, आणि खुगा व थौबाल बहुउद्देशीय प्रकल्प खोऱ्याच्या काही भागांना सिंचन देतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Household tap-water coverage", "घरेलू नल जल कवरेज", "घरगुती नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
        (L("Irrigated area", "सिंचित क्षेत्र", "सिंचित क्षेत्र"), "india-gov", "Land Use Statistics, Ministry of Agriculture."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Manipur lies in seismic zone V, the highest earthquake zone; the Imphal earthquake of January 2016 damaged buildings across the valley. Floods in the valley and landslides on NH-2 and NH-37 are frequent in the monsoon — a landslide at Noney in June 2022 killed dozens of people at a railway construction camp. Since 2023 the security situation has varied by area, with curfews and restrictions at times; visitors need an Inner Line Permit, should check the latest advisories of the State government before travel and follow local instructions.",
        "मणिपुर भूकंपीय क्षेत्र V में है, जो सबसे ऊँचा भूकंप क्षेत्र है; जनवरी 2016 के इंफाल भूकंप ने पूरी घाटी में इमारतों को क्षति पहुँचाई। मानसून में घाटी में बाढ़ और एनएच-2 और एनएच-37 पर भूस्खलन आम हैं — जून 2022 में नोनी में एक भूस्खलन में रेलवे निर्माण शिविर में दर्जनों लोग मारे गए। 2023 से सुरक्षा स्थिति क्षेत्र के अनुसार अलग रही है, कभी कर्फ़्यू और प्रतिबंधों के साथ; पर्यटकों को इनर लाइन परमिट चाहिए, यात्रा से पहले राज्य सरकार की नवीनतम सलाह देखनी चाहिए और स्थानीय निर्देशों का पालन करना चाहिए।",
        "मणिपूर भूकंप क्षेत्र V मध्ये आहे, जे सर्वोच्च भूकंप क्षेत्र आहे; जानेवारी 2016 च्या इंफाळ भूकंपाने संपूर्ण खोऱ्यातील इमारतींचे नुकसान केले. पावसाळ्यात खोऱ्यात पूर व एनएच-2 आणि एनएच-37 वर भूस्खलन वारंवार होतात — जून 2022 मध्ये नोनी येथे झालेल्या भूस्खलनात रेल्वे बांधकाम छावणीतील डझनावारी लोक मृत्युमुखी पडले. 2023 पासून सुरक्षा स्थिती भागानुसार वेगवेगळी राहिली आहे, कधी संचारबंदी व निर्बंधांसह; पर्यटकांना इनर लाइन परवाना लागतो, प्रवासापूर्वी राज्य सरकारचे नवीनतम मार्गदर्शन पाहावे आणि स्थानिक सूचनांचे पालन करावे."),
        conf="Editorial"),
    emergency_table(("Manipur", "मणिपुर", "मणिपूर")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Seismic zone — BIS map reference", "भूकंपीय क्षेत्र — बीआईएस मानचित्र संदर्भ", "भूकंप क्षेत्र — बीआयएस नकाशा संदर्भ"), "bis", "IS 1893 seismic zoning map."),
        (L("Noney landslide (2022) — official toll", "नोनी भूस्खलन (2022) — आधिकारिक मृतक संख्या", "नोनी भूस्खलन (2022) — अधिकृत मृतसंख्या"), "ndma", "Government of Manipur / NDMA report."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Seven GIs belong to Manipur on the GI Registry's list as on 31 December 2025. Three are handloom textiles registered in 2011 — Shaphee Lanphee, a warrior's shawl once given as a royal honour, the fine Wangkhei Phee and the bordered Moirang Phee. The rest are farm products: Kachai lemon from Ukhrul, Tamenglong orange, Sirarakhong hathei chilli and Chak-hao black rice, which is shared with Nagaland.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में सात जीआई मणिपुर के हैं। तीन 2011 में पंजीकृत हथकरघा वस्त्र हैं — शफ़ी लानफ़ी, एक योद्धा की शॉल जो कभी राजकीय सम्मान के रूप में दी जाती थी, महीन वांगखेई फ़ी और किनारीदार मोइरांग फ़ी। शेष कृषि उत्पाद हैं: उखरुल का काचाई नींबू, तामेंगलोंग संतरा, सिरारखोंग हथेई मिर्च और चाक-हाओ काला चावल, जो नागालैंड के साथ साझा है।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत सात जीआय मणिपूरचे आहेत. तीन 2011 मध्ये नोंदणीकृत हातमाग वस्त्रे आहेत — शफी लानफी, एकेकाळी राजसन्मान म्हणून दिली जाणारी योद्ध्याची शाल, बारीक वांगखेई फी आणि काठाची मोइरांग फी. उरलेली कृषी उत्पादने आहेत: उखरुलचा काचाई लिंबू, तामेंगलोंग संत्रे, सिरारखोंग हथेई मिरची आणि चाक-हाओ काळा तांदूळ, जो नागालँडसोबत सामायिक आहे."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Pending GI applications from Manipur", "मणिपुर के लंबित जीआई आवेदन", "मणिपूरचे प्रलंबित जीआय अर्ज"), "gi-registry", "GI Registry application status search."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "In Imphal, Kangla Fort, the Shri Govindajee temple, Ima Keithel, the State Museum, the Imphal War Cemetery and the polo ground at Mapal Kangjeibung can be seen in a day or two. South of the capital, Moirang has the INA Memorial, and Sendra island and Keibul Lamjao look out over Loktak's phumdis, where the sangai may be spotted. In the hills, Ukhrul has the Shirui hills and Longpi pottery villages, and Dzükou valley can be reached from the Manipur side. Visitors need an Inner Line Permit, and travel plans should follow the latest official advice on which areas are open.",
        "इंफाल में कांगला क़िला, श्री गोविंदजी मंदिर, इमा कैथेल, राज्य संग्रहालय, इंफाल युद्ध समाधि स्थल और मापाल कांगजेइबुंग का पोलो मैदान एक-दो दिन में देखे जा सकते हैं। राजधानी के दक्षिण में मोइरांग में आईएनए स्मारक है, और सेंद्रा द्वीप और कैबुल लामजाओ से लोकटक की फुमदियाँ दिखती हैं, जहाँ संगाई दिख सकता है। पहाड़ियों में उखरुल में शिरुई पहाड़ियाँ और लोंगपी के मिट्टी के बर्तनों वाले गाँव हैं, और मणिपुर की ओर से ज़ुकू घाटी पहुँचा जा सकता है। पर्यटकों को इनर लाइन परमिट चाहिए, और यात्रा योजना इस बारे में नवीनतम आधिकारिक सलाह के अनुसार होनी चाहिए कि कौन से क्षेत्र खुले हैं।",
        "इंफाळमध्ये कांगला किल्ला, श्री गोविंदजी मंदिर, इमा कैथेल, राज्य संग्रहालय, इंफाळ युद्धस्मशान व मापाल कांगजेइबुंगचे पोलो मैदान एक-दोन दिवसांत पाहता येतात. राजधानीच्या दक्षिणेला मोइरांगमध्ये आयएनए स्मारक आहे, आणि सेंद्रा बेट व कैबुल लामजाओवरून लोकटकच्या फुमदी दिसतात, जिथे संगाई दिसू शकतो. डोंगरांत उखरुलमध्ये शिरुई टेकड्या व लोंगपी मातीकामाची गावे आहेत, आणि मणिपूरच्या बाजूने झुकू खोऱ्यात जाता येते. पर्यटकांना इनर लाइन परवाना लागतो, आणि कोणते भाग खुले आहेत याबाबत नवीनतम अधिकृत सल्ल्यानुसार प्रवास आखावा."),
        conf="Editorial"),
    lst("places", [
        it3("kangla", "Kangla Fort, Imphal", "कांगला क़िला, इंफाल", "कांगला किल्ला, इंफाळ", m=("History", "इतिहास", "इतिहास")),
        it3("ima", "Ima Keithel", "इमा कैथेल", "इमा कैथेल", m=("Women's market", "महिलाओं का बाज़ार", "स्त्रियांचा बाजार")),
        it3("loktak", "Loktak and Sendra", "लोकटक और सेंद्रा", "लोकटक व सेंद्रा", m=("Lake and phumdis", "झील और फुमदियाँ", "सरोवर व फुमदी")),
        it3("keibul", "Keibul Lamjao", "कैबुल लामजाओ", "कैबुल लामजाओ", m=("Sangai deer", "संगाई हिरण", "संगाई हरिण")),
        it3("moirang", "Moirang", "मोइरांग", "मोइरांग", m=("INA Memorial", "आईएनए स्मारक", "आयएनए स्मारक")),
        it3("ukhrul", "Ukhrul and Shirui", "उखरुल और शिरुई", "उखरुल व शिरुई", m=("Hills; lily in May–June", "पहाड़ियाँ; मई–जून में लिली", "टेकड्या; मे–जूनमध्ये लिली")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Imphal sights, then a day at Moirang, Loktak and Keibul Lamjao.", "इंफाल के दर्शनीय स्थल, फिर मोइरांग, लोकटक और कैबुल लामजाओ में एक दिन।", "इंफाळमधील प्रेक्षणीय स्थळे, मग मोइरांग, लोकटक व कैबुल लामजाओत एक दिवस.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Add Ukhrul and the Shirui hills, if the route is open.", "मार्ग खुला हो तो उखरुल और शिरुई पहाड़ियाँ जोड़ें।", "मार्ग खुला असल्यास उखरुल व शिरुई टेकड्या जोडा.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    gaps("g", [
        (L("Tourist arrivals by year", "वर्षवार पर्यटक आगमन", "वर्षनिहाय पर्यटक आगमन"), "tourism", "Lok Sabha USQ 3834 (16 March 2026) lists Manipur separately; figures to be added."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "cities", [
    lst("cities", [
        city("imphal", ("Imphal", "इंफाल", "इंफाळ"), ("Capital in the centre of the valley.", "घाटी के केंद्र में राजधानी।", "खोऱ्याच्या मध्यभागी राजधानी."), ("Capital", "राजधानी", "राजधानी")),
        city("thoubal", ("Thoubal", "थौबाल", "थौबाल"), ("Valley town south-east of Imphal.", "इंफाल के दक्षिण-पूर्व में घाटी का नगर।", "इंफाळच्या आग्नेयेकडील खोऱ्यातील शहर."), ("Trade", "व्यापार", "व्यापार")),
        city("kakching", ("Kakching", "काकचिंग", "काकचिंग"), ("Market town and district headquarters.", "बाज़ार नगर और ज़िला मुख्यालय।", "बाजारपेठेचे शहर व जिल्हा मुख्यालय."), ("Trade", "व्यापार", "व्यापार")),
        city("churachandpur", ("Churachandpur (Lamka)", "चुराचांदपुर (लमका)", "चुराचांदपूर (लमका)"), ("Main town of the southern hills.", "दक्षिणी पहाड़ियों का मुख्य नगर।", "दक्षिणेकडील डोंगरांचे मुख्य शहर."), ("Administration", "प्रशासन", "प्रशासन")),
        city("ukhrul", ("Ukhrul", "उखरुल", "उखरुल"), ("Tangkhul Naga hill town.", "तांगखुल नागा पहाड़ी नगर।", "तांगखुल नागा डोंगरी शहर."), ("Culture", "संस्कृति", "संस्कृती")),
        city("moreh", ("Moreh", "मोरेह", "मोरेह"), ("Border town opposite Tamu in Myanmar.", "म्यांमार के तामू के सामने सीमावर्ती नगर।", "म्यानमारमधील तामूसमोरील सीमावर्ती शहर."), ("Border trade", "सीमा व्यापार", "सीमाव्यापार")),
    ], title=L("Major towns", "प्रमुख नगर", "प्रमुख शहरे"), conf="Editorial"),
    gaps("g", [
        (L("Town populations (Census 2011)", "नगरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Sport is central to Manipur's identity. M. C. Mary Kom won Olympic bronze in boxing at London 2012 and six world titles; Saikhom Mirabai Chanu won weightlifting silver at Tokyo 2020; Ngangom Dingko Singh won boxing gold at the 1998 Asian Games; and the State has supplied many players to India's football and hockey teams. Traditional sports include sagol kangjei (polo), mukna (wrestling), yubi lakpi (a team game played with a greased coconut) and hiyang tannaba (boat racing). The National Sports University was set up in Imphal in 2018.",
        "खेल मणिपुर की पहचान के केंद्र में हैं। एम. सी. मैरी कॉम ने लंदन 2012 में मुक्केबाज़ी में ओलंपिक कांस्य और छह विश्व ख़िताब जीते; सैखोम मीराबाई चानू ने टोक्यो 2020 में भारोत्तोलन में रजत जीता; न्गांगोम डिंको सिंह ने 1998 के एशियाई खेलों में मुक्केबाज़ी में स्वर्ण जीता; और राज्य ने भारत की फ़ुटबॉल और हॉकी टीमों को बहुत से खिलाड़ी दिए हैं। पारंपरिक खेलों में सगोल कांगजेई (पोलो), मुकना (कुश्ती), युबी लाकपी (तेल लगे नारियल से खेला जाने वाला टीम खेल) और हियांग तान्नबा (नौका दौड़) शामिल हैं। 2018 में इंफाल में राष्ट्रीय खेल विश्वविद्यालय स्थापित हुआ।",
        "खेळ हा मणिपूरच्या ओळखीचा गाभा आहे. एम. सी. मेरी कोम यांनी लंडन 2012 मध्ये मुष्टियुद्धात ऑलिंपिक कांस्य व सहा जागतिक विजेतेपदे जिंकली; सैखोम मीराबाई चानू यांनी टोकियो 2020 मध्ये भारोत्तोलनात रौप्य जिंकले; न्गांगोम डिंको सिंह यांनी 1998 च्या आशियाई खेळांत मुष्टियुद्धात सुवर्ण जिंकले; आणि राज्याने भारताच्या फुटबॉल व हॉकी संघांना अनेक खेळाडू दिले आहेत. पारंपरिक खेळांत सगोल कांगजेई (पोलो), मुकना (कुस्ती), युबी लाकपी (तेल लावलेल्या नारळाने खेळला जाणारा सांघिक खेळ) व हियांग तान्नबा (नौकाशर्यत) यांचा समावेश आहे. 2018 मध्ये इंफाळमध्ये राष्ट्रीय क्रीडा विद्यापीठ स्थापन झाले."),
        conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from Manipur — official list", "मणिपुर के ओलंपिक और एशियाई खेल पदक विजेता — आधिकारिक सूची", "मणिपूरचे ऑलिंपिक व आशियाई खेळ पदकविजेते — अधिकृत यादी"), "india-gov", "Sports Authority of India / Manipur Youth Affairs and Sports.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("marykom", ("M. C. Mary Kom", "एम. सी. मैरी कॉम", "एम. सी. मेरी कोम"), ("Boxer; Olympic bronze 2012 and six-time world champion.", "मुक्केबाज़; 2012 ओलंपिक कांस्य और छह बार विश्व विजेता।", "मुष्टियोद्धा; 2012 ऑलिंपिक कांस्य व सहा वेळा जगज्जेत्या."), ("Sport", "खेल", "क्रीडा")),
        person("mirabai", ("Saikhom Mirabai Chanu", "सैखोम मीराबाई चानू", "सैखोम मीराबाई चानू"), ("Weightlifter; Olympic silver at Tokyo 2020.", "भारोत्तोलक; टोक्यो 2020 में ओलंपिक रजत।", "भारोत्तोलक; टोकियो 2020 मध्ये ऑलिंपिक रौप्य."), ("Sport", "खेल", "क्रीडा")),
        person("tikendrajit", ("Bir Tikendrajit Singh", "बीर टिकेंद्रजीत सिंह", "बीर टिकेंद्रजीत सिंह"), ("Prince and commander in the Anglo-Manipur War of 1891.", "1891 के आंग्ल-मणिपुर युद्ध में राजकुमार और सेनापति।", "1891 च्या आंग्ल-मणिपूर युद्धातील राजकुमार व सेनापती."), ("History", "इतिहास", "इतिहास")),
        person("gaidinliu", ("Rani Gaidinliu", "रानी गाइदिन्ल्यू", "राणी गाइदिन्ल्यू"), ("Rongmei Naga freedom fighter from Tamenglong.", "तामेंगलोंग की रोंगमेई नागा स्वतंत्रता सेनानी।", "तामेंगलोंगच्या रोंगमेई नागा स्वातंत्र्यसैनिक."), ("Freedom movement", "स्वतंत्रता आंदोलन", "स्वातंत्र्यलढा")),
        person("ratan", ("Ratan Thiyam", "रतन थियाम", "रतन थियाम"), ("Theatre director; founder of the Chorus Repertory Theatre.", "रंगमंच निर्देशक; कोरस रिपर्टरी थिएटर के संस्थापक।", "रंगभूमी दिग्दर्शक; कोरस रिपर्टरी थिएटरचे संस्थापक."), ("Theatre", "रंगमंच", "रंगभूमी")),
        person("guru", ("Guru Bipin Singh", "गुरु बिपिन सिंह", "गुरु बिपिन सिंह"), ("Dancer and teacher who spread Manipuri dance across India.", "नर्तक और गुरु जिन्होंने मणिपुरी नृत्य को पूरे भारत में फैलाया।", "नर्तक व गुरू ज्यांनी मणिपुरी नृत्य संपूर्ण भारतात पोहोचवले."), ("Dance", "नृत्य", "नृत्य")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Manipuri communities live in Assam's Barak valley, Tripura and Bangladesh, descendants of people who left during the Burmese wars of the 19th century, and in Myanmar. Today many young people from all communities study and work in Delhi, Bengaluru, Pune, Guwahati and other cities, and the displacement since 2023 has sent more families to Mizoram, Assam and beyond.",
        "मणिपुरी समुदाय असम की बराक घाटी, त्रिपुरा और बांग्लादेश में रहते हैं, जो 19वीं सदी के बर्मी युद्धों में यहाँ से गए लोगों के वंशज हैं, और म्यांमार में भी। आज सभी समुदायों के बहुत से युवा दिल्ली, बेंगलुरु, पुणे, गुवाहाटी और अन्य नगरों में पढ़ते और काम करते हैं, और 2023 से विस्थापन ने और परिवारों को मिज़ोरम, असम और उससे आगे भेजा है।",
        "मणिपुरी समुदाय आसामच्या बराक खोऱ्यात, त्रिपुरा व बांगलादेशात राहतात, जे एकोणिसाव्या शतकातील ब्रह्मी युद्धांच्या काळात येथून गेलेल्या लोकांचे वंशज आहेत, आणि म्यानमारमध्येही. आज सर्व समुदायांतील अनेक तरुण दिल्ली, बंगळुरू, पुणे, गुवाहाटी व इतर शहरांत शिकतात व काम करतात, आणि 2023 पासूनच्या विस्थापनाने आणखी कुटुंबे मिझोराम, आसाम व त्यापलीकडे गेली आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Out-migration from the State — official estimate", "राज्य से बाहर प्रवास — आधिकारिक अनुमान", "राज्याबाहेर स्थलांतर — अधिकृत अंदाज"), "census", "Census 2011 migration tables (D-series)."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Manipur portal", "मणिपुर सरकार पोर्टल", "मणिपूर शासन संकेतस्थळ", url="https://manipur.gov.in", src="india-gov"),
        it3("assembly", "Manipur Legislative Assembly", "मणिपुर विधानसभा", "मणिपूर विधानसभा", url="https://assembly.mn.gov.in", src="mn-assembly"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes", "एसटीडी कोड", "एसटीडी कोड"),
          [col(L("Area", "क्षेत्र", "क्षेत्र")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Imphal", "इंफाल", "इंफाळ"), "0385"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय; दूरसंचार विभाग की नंबरिंग योजना से जाँचा जाएगा।", "संपादकीय; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळले जाईल.")),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("loktak", ("Loktak lake was designated a Ramsar site on 23 March 1990.", "लोकटक झील को 23 मार्च 1990 को रामसर स्थल घोषित किया गया।", "लोकटक सरोवराला 23 मार्च 1990 रोजी रामसर स्थळ घोषित केले गेले."), RAMSAR, "indian-wetlands"),
        triv("forest", ("About 74% of the State is forest (ISFR 2023).", "राज्य का लगभग 74% भाग वन है (आईएसएफ़आर 2023)।", "राज्याचा सुमारे 74% भाग वनाच्छादित आहे (आयएसएफआर 2023)."), LS_FOREST, "fsi"),
        triv("textiles", ("Three Manipuri textiles — Shaphee Lanphee, Wangkhei Phee and Moirang Phee — were registered as GIs on the same day in December 2011.", "तीन मणिपुरी वस्त्र — शफ़ी लानफ़ी, वांगखेई फ़ी और मोइरांग फ़ी — दिसंबर 2011 में एक ही दिन जीआई के रूप में पंजीकृत हुए।", "तीन मणिपुरी वस्त्रे — शफी लानफी, वांगखेई फी व मोइरांग फी — डिसेंबर 2011 मध्ये एकाच दिवशी जीआय म्हणून नोंदणीकृत झाली."), GI_PDF, "gi-registry"),
        triv("polo", ("British planters and officers took polo from Manipur to Cachar and then to England in the 19th century.", "19वीं सदी में ब्रिटिश बागान मालिक और अधिकारी पोलो को मणिपुर से कछार और फिर इंग्लैंड ले गए।", "एकोणिसाव्या शतकात ब्रिटिश मळेवाले व अधिकारी पोलो मणिपूरहून कछार व पुढे इंग्लंडला घेऊन गेले.")),
        triv("ima", ("Only married women may hold a stall at Ima Keithel.", "इमा कैथेल में केवल विवाहित महिलाएँ ही दुकान लगा सकती हैं।", "इमा कैथेलमध्ये केवळ विवाहित स्त्रियाच दुकान लावू शकतात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("mn mod3 ok")
