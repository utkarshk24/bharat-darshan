"""Assam modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-AS"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
asm = read("regions/IN-AS.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Assam is the gateway to north-east India, linked to the rest of the country through the narrow Siliguri corridor in West Bengal. Most of the State lies in the broad valley of the Brahmaputra, one of the world's great rivers, with the Barak valley in the south and the Karbi Anglong and Dima Hasao hills between them. Its neighbours are Bhutan and Arunachal Pradesh to the north, Nagaland and Manipur to the east, Mizoram, Meghalaya, Tripura and Bangladesh to the south, and West Bengal to the west. It had 3.12 crore people at the 2011 Census. Dispur, within Guwahati, is the capital; Silchar, Dibrugarh, Jorhat, Nagaon and Tezpur are other major towns.\n\nAssamese is the official language, with Bengali used officially in the Barak valley and Bodo in the Bodoland Territorial Region.",
        "असम पूर्वोत्तर भारत का प्रवेश द्वार है, जो पश्चिम बंगाल के संकरे सिलीगुड़ी गलियारे से देश के बाक़ी हिस्से से जुड़ता है। राज्य का अधिकांश भाग विश्व की महान नदियों में से एक ब्रह्मपुत्र की चौड़ी घाटी में है, दक्षिण में बराक घाटी है और दोनों के बीच कार्बी आंगलोंग और दिमा हसाओ की पहाड़ियाँ हैं। इसके उत्तर में भूटान और अरुणाचल प्रदेश, पूर्व में नागालैंड और मणिपुर, दक्षिण में मिज़ोरम, मेघालय, त्रिपुरा और बांग्लादेश, और पश्चिम में पश्चिम बंगाल है। 2011 की जनगणना में इसकी जनसंख्या 3.12 करोड़ थी। गुवाहाटी के भीतर दिसपुर राजधानी है; सिलचर, डिब्रूगढ़, जोरहाट, नगाँव और तेजपुर अन्य प्रमुख नगर हैं।\n\nअसमिया राजभाषा है, और बराक घाटी में बांग्ला तथा बोडोलैंड प्रादेशिक क्षेत्र में बोडो का आधिकारिक उपयोग होता है।",
        "आसाम हे ईशान्य भारताचे प्रवेशद्वार आहे, जे पश्चिम बंगालमधील अरुंद सिलिगुडी मार्गिकेने उर्वरित देशाशी जोडले आहे. राज्याचा बहुतांश भाग जगातील महान नद्यांपैकी एक असलेल्या ब्रह्मपुत्रेच्या रुंद खोऱ्यात आहे, दक्षिणेला बराक खोरे आहे व दोन्हींच्यामध्ये कार्बी आंगलोंग आणि दिमा हसाओचे डोंगर आहेत. त्याच्या उत्तरेला भूतान व अरुणाचल प्रदेश, पूर्वेला नागालँड व मणिपूर, दक्षिणेला मिझोराम, मेघालय, त्रिपुरा व बांगलादेश, आणि पश्चिमेला पश्चिम बंगाल आहे. 2011 च्या जनगणनेनुसार त्याची लोकसंख्या 3.12 कोटी होती. गुवाहाटीतील दिसपूर ही राजधानी आहे; सिलचर, डिब्रुगड, जोरहाट, नगाव व तेजपूर ही इतर प्रमुख शहरे आहेत.\n\nआसामी ही राजभाषा आहे, आणि बराक खोऱ्यात बंगाली व बोडोलँड प्रादेशिक क्षेत्रात बोडोचा अधिकृत वापर होतो."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Assam is famous worldwide for its tea, grown on hundreds of estates across the Brahmaputra valley since the 1830s, and for Kaziranga, home to most of the world's greater one-horned rhinoceroses. Kaziranga, Manas and the Moidams — the royal burial mounds of the Ahom kings at Charaideo — are UNESCO World Heritage Sites. The Ahom kingdom ruled for about six centuries and famously repelled the Mughals at Saraighat in 1671. Assam's culture centres on the three Bihu festivals, the Vaishnava monasteries (satras) founded by Srimanta Sankardeva, Sattriya dance, and golden muga silk woven into mekhela chador. Majuli, in the Brahmaputra, is one of the world's largest river islands, and Digboi has one of the oldest oil refineries still working.",
        "असम अपनी चाय के लिए विश्व प्रसिद्ध है, जो 1830 के दशक से ब्रह्मपुत्र घाटी के सैकड़ों बाग़ानों में उगाई जाती है, और काज़ीरंगा के लिए, जहाँ विश्व के अधिकांश एक सींग वाले गैंडे रहते हैं। काज़ीरंगा, मानस और मोइदाम — चराइदेउ में अहोम राजाओं के शाही समाधि-टीले — यूनेस्को विश्व धरोहर स्थल हैं। अहोम राज्य ने लगभग छह सदियों तक शासन किया और 1671 में सराईघाट में मुग़लों को प्रसिद्ध रूप से खदेड़ा। असम की संस्कृति तीन बिहू त्योहारों, श्रीमंत शंकरदेव द्वारा स्थापित वैष्णव मठों (सत्रों), सत्रीया नृत्य और मेखेला चादर में बुने सुनहरे मूगा रेशम पर केंद्रित है। ब्रह्मपुत्र में माजुली विश्व के सबसे बड़े नदी द्वीपों में से है, और डिगबोई में अब भी चल रही सबसे पुरानी तेल रिफ़ाइनरियों में से एक है।",
        "आसाम आपल्या चहासाठी जगप्रसिद्ध आहे, जो 1830 च्या दशकापासून ब्रह्मपुत्रा खोऱ्यातील शेकडो मळ्यांत पिकवला जातो, आणि काझीरंगासाठी, जिथे जगातील बहुतेक एकशिंगी गेंडे राहतात. काझीरंगा, मानस व मोइदाम — चराइदेव येथील अहोम राजांची राजसमाधी-टेकाडे — ही युनेस्को जागतिक वारसा स्थळे आहेत. अहोम राज्याने सुमारे सहा शतके राज्य केले आणि 1671 मध्ये सराईघाट येथे मुघलांना प्रसिद्धपणे परतवले. आसामची संस्कृती तीन बिहू सण, श्रीमंत शंकरदेवांनी स्थापलेले वैष्णव मठ (सत्र), सत्रिया नृत्य आणि मेखेला चादरमध्ये विणलेल्या सोनेरी मुगा रेशमाभोवती केंद्रित आहे. ब्रह्मपुत्रेतील माजुली हे जगातील सर्वांत मोठ्या नदी-बेटांपैकी एक आहे, आणि डिगबोईत अजूनही चालू असलेल्या सर्वांत जुन्या तेल शुद्धीकरण कारखान्यांपैकी एक आहे."),
        title=L("What makes Assam unique?", "असम को ख़ास क्या बनाता है?", "आसामचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Status", "दर्जा", "दर्जा"), L("Province from 1874; State of the Union from 26 January 1950", "1874 से प्रांत; 26 जनवरी 1950 से संघ का राज्य", "1874 पासून प्रांत; 26 जानेवारी 1950 पासून संघराज्यातील राज्य")],
           [L("Capital", "राजधानी", "राजधानी"), L("Dispur (Guwahati)", "दिसपुर (गुवाहाटी)", "दिसपूर (गुवाहाटी)")],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Assamese; Bengali (Barak valley); Bodo (Bodoland)", "असमिया; बांग्ला (बराक घाटी); बोडो (बोडोलैंड)", "आसामी; बंगाली (बराक खोरे); बोडो (बोडोलँड)")],
           [L("Sixth Schedule councils", "छठी अनुसूची परिषदें", "सहाव्या अनुसूचीतील परिषदा"), L("Bodoland Territorial Council; Karbi Anglong; Dima Hasao", "बोडोलैंड प्रादेशिक परिषद; कार्बी आंगलोंग; दिमा हसाओ", "बोडोलँड प्रादेशिक परिषद; कार्बी आंगलोंग; दिमा हसाओ")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Gauhati High Court, Guwahati (1948)", "गुवाहाटी उच्च न्यायालय, गुवाहाटी (1948)", "गुवाहाटी उच्च न्यायालय, गुवाहाटी (1948)")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "AS"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be linked to the State's notifications in review. The current number of districts is listed as a gap.", "संपादकीय; समीक्षा में राज्य की अधिसूचनाओं से जोड़ा जाएगा। ज़िलों की वर्तमान संख्या अंतराल सूची में है।", "संपादकीय; तपासणीत राज्याच्या अधिसूचनांशी जोडले जाईल. जिल्ह्यांची सध्याची संख्या उणिवांच्या यादीत आहे.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "The Brahmaputra enters Assam from Arunachal Pradesh near Sadiya and flows west for about the length of the State, braided into many channels and dotted with sandbars (chars) and islands, including Majuli. Its valley, built of rich alluvium and fed by tributaries such as the Subansiri, Jia Bharali, Manas, Dhansiri and Kopili, holds most of Assam's people, farms and tea gardens. To the south, the Karbi plateau and the North Cachar hills of Dima Hasao separate it from the Barak valley around Silchar, which drains through Bangladesh. Wetlands called beels, such as Deepor Beel near Guwahati, are common on the floodplains.",
        "ब्रह्मपुत्र सदिया के पास अरुणाचल प्रदेश से असम में प्रवेश करती है और लगभग पूरे राज्य की लंबाई में पश्चिम की ओर बहती है, कई धाराओं में बँटी हुई और रेतीले टापुओं (चर) व माजुली सहित द्वीपों से भरी। इसकी घाटी, जो समृद्ध जलोढ़ से बनी है और सुबनसिरी, जिया भराली, मानस, धनसिरी और कोपिली जैसी सहायक नदियों से सिंचित है, असम के अधिकांश लोगों, खेतों और चाय बाग़ानों का घर है। दक्षिण में कार्बी पठार और दिमा हसाओ की उत्तरी कछार पहाड़ियाँ इसे सिलचर के आसपास की बराक घाटी से अलग करती हैं, जो बांग्लादेश से होकर बहती है। बाढ़ मैदानों में बील कहलाने वाली आर्द्रभूमियाँ, जैसे गुवाहाटी के पास दीपोर बील, आम हैं।",
        "ब्रह्मपुत्रा सदियाजवळ अरुणाचल प्रदेशातून आसाममध्ये प्रवेश करते आणि जवळपास राज्याच्या पूर्ण लांबीत पश्चिमेकडे वाहते, अनेक प्रवाहांत विभागलेली व वाळूच्या बेटांनी (चर) आणि माजुलीसह बेटांनी भरलेली. समृद्ध गाळाचे व सुबनसिरी, जिया भराली, मानस, धनसिरी व कोपिली यांसारख्या उपनद्यांनी भरणारे तिचे खोरे आसामचे बहुतेक लोक, शेती व चहामळे सामावते. दक्षिणेला कार्बी पठार व दिमा हसाओचे उत्तर कछार डोंगर त्याला सिलचरभोवतीच्या बराक खोऱ्यापासून वेगळे करतात, जे बांगलादेशातून वाहते. पूरमैदानांत बील नावाची पाणथळे, जसे गुवाहाटीजवळील दीपोर बील, सामान्य आहेत."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), asm["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("bt", "Bhutan (north)", "भूटान (उत्तर)", "भूतान (उत्तर)"), it3("ar", "Arunachal Pradesh (north and east)", "अरुणाचल प्रदेश (उत्तर और पूर्व)", "अरुणाचल प्रदेश (उत्तर व पूर्व)"),
        it3("nl", "Nagaland (east)", "नागालैंड (पूर्व)", "नागालँड (पूर्व)"), it3("mn", "Manipur (east)", "मणिपुर (पूर्व)", "मणिपूर (पूर्व)"),
        it3("mz", "Mizoram (south)", "मिज़ोरम (दक्षिण)", "मिझोराम (दक्षिण)"), it3("ml", "Meghalaya (south)", "मेघालय (दक्षिण)", "मेघालय (दक्षिण)"),
        it3("tr", "Tripura (south)", "त्रिपुरा (दक्षिण)", "त्रिपुरा (दक्षिण)"), it3("bd", "Bangladesh (south-west)", "बांग्लादेश (दक्षिण-पश्चिम)", "बांगलादेश (नैर्ऋत्य)"),
        it3("wb", "West Bengal (west)", "पश्चिम बंगाल (पश्चिम)", "पश्चिम बंगाल (पश्चिम)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("brahmaputra", "Brahmaputra", "ब्रह्मपुत्र", "ब्रह्मपुत्रा", d=("Braided giant river; National Waterway 2.", "गुँथी धाराओं वाली विशाल नदी; राष्ट्रीय जलमार्ग 2।", "अनेक प्रवाहांची विशाल नदी; राष्ट्रीय जलमार्ग 2.")),
        it3("barak", "Barak", "बराक", "बराक", d=("Southern river through Silchar; National Waterway 16.", "सिलचर से होकर बहने वाली दक्षिणी नदी; राष्ट्रीय जलमार्ग 16।", "सिलचरमधून वाहणारी दक्षिणेकडील नदी; राष्ट्रीय जलमार्ग 16.")),
        it3("subansiri", "Subansiri", "सुबनसिरी", "सुबनसिरी", d=("Largest tributary of the Brahmaputra, from Arunachal.", "अरुणाचल से आने वाली ब्रह्मपुत्र की सबसे बड़ी सहायक नदी।", "अरुणाचलमधून येणारी ब्रह्मपुत्रेची सर्वांत मोठी उपनदी.")),
        it3("manas", "Manas", "मानस", "मानस", d=("From Bhutan; flows through Manas National Park.", "भूटान से; मानस राष्ट्रीय उद्यान से होकर बहती है।", "भूतानमधून; मानस राष्ट्रीय उद्यानातून वाहते.")),
        it3("dhansiri", "Dhansiri", "धनसिरी", "धनसिरी", d=("From Nagaland; flows past Golaghat.", "नागालैंड से; गोलाघाट से होकर।", "नागालँडमधून; गोलाघाटमार्गे.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Highest point — official elevation", "सर्वोच्च बिंदु — आधिकारिक ऊँचाई", "सर्वोच्च शिखर — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Area of Majuli island (latest survey)", "माजुली द्वीप का क्षेत्रफल (नवीनतम सर्वेक्षण)", "माजुली बेटाचे क्षेत्रफळ (नवीनतम सर्वेक्षण)"), "survey-of-india", "Survey of India / Brahmaputra Board."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Assam has a humid subtropical climate with a long, heavy monsoon. Pre-monsoon thunderstorms (bordoicila, 'nor'westers') arrive in March–April, and the south-west monsoon (June–September) brings very heavy rain, especially along the foothills, so floods are common from May to September. Summers are warm and humid rather than extremely hot, and winters (November–February) are cool and dry, with fog in the valley.",
        "असम की जलवायु आर्द्र उपोष्ण है, जिसमें लंबा और भारी मानसून होता है। मार्च–अप्रैल में मानसून-पूर्व आँधियाँ (बरदैसिला, 'नॉर्वेस्टर') आती हैं, और दक्षिण-पश्चिम मानसून (जून–सितंबर) बहुत भारी वर्षा लाता है, विशेषकर तराई के साथ-साथ, इसलिए मई से सितंबर तक बाढ़ आम है। गर्मियाँ बहुत तेज़ गर्म के बजाय उमस भरी होती हैं, और सर्दियाँ (नवंबर–फ़रवरी) ठंडी और सूखी होती हैं, घाटी में कोहरे के साथ।",
        "आसामचे हवामान दमट उपोष्ण असून मान्सून दीर्घ व मुसळधार असतो. मार्च–एप्रिलमध्ये मान्सूनपूर्व वादळे (बरदैसिला, 'नॉर्वेस्टर') येतात, आणि नैर्ऋत्य मान्सून (जून–सप्टेंबर) अतिशय मुसळधार पाऊस आणतो, विशेषतः पायथ्यालगत, त्यामुळे मे ते सप्टेंबरदरम्यान पूर सामान्य आहेत. उन्हाळा अतिउष्ण नसून दमट असतो, आणि हिवाळा (नोव्हेंबर–फेब्रुवारी) थंड व कोरडा असतो, खोऱ्यात धुक्यासह."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Guwahati", "गुवाहाटी", "गुवाहाटी"), "lat": 26.1445, "lon": 91.7362},
        {"name": L("Dibrugarh", "डिब्रूगढ़", "डिब्रुगड"), "lat": 27.4728, "lon": 94.9120},
        {"name": L("Silchar", "सिलचर", "सिलचर"), "lat": 24.8333, "lon": 92.7789},
        {"name": L("Tezpur", "तेजपुर", "तेजपूर"), "lat": 26.6528, "lon": 92.7926},
    ]},
    lst("best", [
        it3("winter", "November to April", "नवंबर से अप्रैल", "नोव्हेंबर ते एप्रिल", d=("Kaziranga and Manas are open (usually from November); Magh Bihu in January; Rongali Bihu in mid-April.", "काज़ीरंगा और मानस खुले रहते हैं (प्रायः नवंबर से); जनवरी में माघ बिहू; मध्य अप्रैल में रोंगाली बिहू।", "काझीरंगा व मानस खुले असतात (सहसा नोव्हेंबरपासून); जानेवारीत माघ बिहू; एप्रिलच्या मध्यात रोंगाली बिहू.")),
        it3("monsoon", "May to September", "मई से सितंबर", "मे ते सप्टेंबर", d=("Floods; national parks closed; Ambubachi Mela at Kamakhya in June.", "बाढ़; राष्ट्रीय उद्यान बंद; जून में कामाख्या में अंबुबाची मेला।", "पूर; राष्ट्रीय उद्याने बंद; जूनमध्ये कामाख्या येथे अंबुबाची मेळा.")),
        it3("autumn", "October", "अक्टूबर", "ऑक्टोबर", d=("Durga Puja and Kati Bihu; tea plucking season continues.", "दुर्गा पूजा और काती बिहू; चाय तोड़ाई का मौसम जारी।", "दुर्गापूजा व काती बिहू; चहा खुडणीचा हंगाम सुरू.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (Assam & Meghalaya sub-division)", "सामान्य वार्षिक वर्षा (असम व मेघालय उप-मंडल)", "सरासरी वार्षिक पाऊस (आसाम व मेघालय उपविभाग)"), "imd", "IMD rainfall statistics."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Assam's year turns with Bihu. In mid-April, Rongali Bihu brings the new year with dhol, pepa (buffalo-horn pipe) and young dancers in muga and red; Magh Bihu in January is a harvest feast around bonfires (meji); and the quiet Kati Bihu in autumn lights lamps in the paddy fields. Every home has a gamosa, the white-and-red woven towel offered as a mark of respect. The Brahmaputra is always present — ferries cross it at Guwahati and Majuli — and life in the tea gardens, with their own Adivasi music and Jhumur dance, has its own rhythm. Fish curry with a sour tenga, khar, rice and pitha, and endless cups of tea are the taste of Assam.",
        "असम का वर्ष बिहू के साथ घूमता है। मध्य अप्रैल में रोंगाली बिहू ढोल, पेपा (भैंस के सींग की बाँसुरी) और मूगा व लाल रंग में सजे युवा नर्तकों के साथ नया वर्ष लाता है; जनवरी में माघ बिहू अलाव (मेजी) के चारों ओर फ़सल का भोज है; और शरद में शांत काती बिहू धान के खेतों में दीप जलाता है। हर घर में गमोसा है, सफ़ेद-लाल बुना अंगोछा जो सम्मान के प्रतीक के रूप में भेंट किया जाता है। ब्रह्मपुत्र हमेशा मौजूद है — गुवाहाटी और माजुली में नौकाएँ इसे पार करती हैं — और अपने आदिवासी संगीत और झुमुर नृत्य के साथ चाय बाग़ानों का जीवन अपनी लय रखता है। खट्टे टेंगा वाली मछली, खार, भात और पीठा, और अनगिनत प्याले चाय असम का स्वाद हैं।",
        "आसामचे वर्ष बिहूसोबत फिरते. एप्रिलच्या मध्यात रोंगाली बिहू ढोल, पेपा (म्हशीच्या शिंगाची पिपाणी) आणि मुगा व लाल रंगात नटलेल्या तरुण नर्तकांसह नववर्ष आणतो; जानेवारीतील माघ बिहू शेकोटीभोवती (मेजी) सुगीची मेजवानी असते; आणि शरदातील शांत काती बिहू भाताच्या शेतांत दिवे लावतो. प्रत्येक घरात गमोसा असतो, सन्मानाचे प्रतीक म्हणून दिला जाणारा पांढरा-लाल विणलेला पंचा. ब्रह्मपुत्रा सदैव सोबत असते — गुवाहाटी व माजुली येथे नौका तिला ओलांडतात — आणि आपल्या आदिवासी संगीत व झुमुर नृत्यासह चहामळ्यांतील जीवनाची स्वतःची लय आहे. आंबट टेंगा असलेली माशांची आमटी, खार, भात व पिठा, आणि असंख्य कप चहा ही आसामची चव आहे."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Assam had 3.12 crore people at the 2011 Census, with about 398 people per km². The sex ratio improved from 935 women per 1,000 men in 2001 to 958 in 2011, while the child sex ratio was 962. Literacy rose from 63.3% to 72.2%, close to the national 73.0%. Scheduled Tribes made up 12.4% of the population and Scheduled Castes 7.2%.\n\nAssam is one of India's most diverse States. Assamese is the main language of the Brahmaputra valley and Bengali of the Barak valley. Bodo, a scheduled language, is spoken in the Bodoland region, and the Mising, Karbi, Dimasa, Rabha, Tiwa, Deori and many other communities have their own languages. The tea-garden communities, descended from workers brought from central and eastern India in the 19th century, speak Sadri and other languages.",
        "2011 की जनगणना में असम की जनसंख्या 3.12 करोड़ थी, और प्रति वर्ग किमी लगभग 398 लोग। लिंगानुपात 2001 में प्रति 1,000 पुरुषों पर 935 महिलाओं से सुधरकर 2011 में 958 हुआ, जबकि शिशु लिंगानुपात 962 था। साक्षरता 63.3% से बढ़कर 72.2% हुई, जो राष्ट्रीय 73.0% के क़रीब है। अनुसूचित जनजातियाँ जनसंख्या का 12.4% और अनुसूचित जातियाँ 7.2% थीं।\n\nअसम भारत के सबसे विविध राज्यों में से है। ब्रह्मपुत्र घाटी की मुख्य भाषा असमिया और बराक घाटी की बांग्ला है। अनुसूचित भाषा बोडो बोडोलैंड क्षेत्र में बोली जाती है, और मिसिंग, कार्बी, दिमासा, राभा, तिवा, देउरी और कई अन्य समुदायों की अपनी भाषाएँ हैं। 19वीं सदी में मध्य और पूर्वी भारत से लाए गए श्रमिकों के वंशज चाय बाग़ान समुदाय सादरी और अन्य भाषाएँ बोलते हैं।",
        "2011 च्या जनगणनेनुसार आसामची लोकसंख्या 3.12 कोटी होती, आणि प्रति चौ.किमी सुमारे 398 लोक. लिंग गुणोत्तर 2001 मधील दर 1,000 पुरुषांमागे 935 स्त्रियांवरून 2011 मध्ये 958 पर्यंत सुधारले, तर बाल लिंग गुणोत्तर 962 होते. साक्षरता 63.3% वरून 72.2% झाली, राष्ट्रीय 73.0% च्या जवळ. अनुसूचित जमाती लोकसंख्येच्या 12.4% व अनुसूचित जाती 7.2% होत्या.\n\nआसाम हे भारतातील सर्वांत वैविध्यपूर्ण राज्यांपैकी एक आहे. ब्रह्मपुत्रा खोऱ्याची मुख्य भाषा आसामी व बराक खोऱ्याची बंगाली आहे. अनुसूचित भाषा बोडो बोडोलँड प्रदेशात बोलली जाते, आणि मिसिंग, कार्बी, दिमासा, राभा, तिवा, देउरी व इतर अनेक समुदायांच्या स्वतःच्या भाषा आहेत. एकोणिसाव्या शतकात मध्य व पूर्व भारतातून आणलेल्या कामगारांचे वंशज असलेले चहामळा समुदाय सादरी व इतर भाषा बोलतात."),
        sources=["census", "es-india", "dl-planning"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), asm["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), asm["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(935, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), asm["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(965, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), asm["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"],
             previous=dp(63.3, "%", "2001", "census", "es-india", ESI_LIT)),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), asm["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(7.2, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 22.31 lakh people."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(12.4, "%", "2011", "census", "dl-planning", SCST, note="Same table: 38.84 lakh people."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("as", "Assamese", "असमिया", "आसामी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("bn", "Bengali", "बांग्ला", "बंगाली", m=("Official in the Barak valley", "बराक घाटी में राजभाषा", "बराक खोऱ्यात राजभाषा")),
        it3("brx", "Bodo", "बोडो", "बोडो", m=("Scheduled language", "अनुसूचित भाषा", "अनुसूचित भाषा")),
        it3("mrg", "Mising", "मिसिंग", "मिसिंग"), it3("mjw", "Karbi", "कार्बी", "कार्बी"), it3("dis", "Dimasa", "दिमासा", "दिमासा"),
        it3("rah", "Rabha", "राभा", "राभा"), it3("sck", "Sadri", "सादरी", "सादरी"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Final Population Totals for Assam."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Ancient Assam was the kingdom of Kamarupa, ruled by the Varman, Mlechchha and Pala dynasties; the Chinese pilgrim Xuanzang visited the court of Bhaskaravarman in the 7th century. In 1228 the Tai prince Sukaphaa crossed the Patkai hills and founded the Ahom kingdom, which ruled the Brahmaputra valley for about six centuries, built capitals at Charaideo, Garhgaon and Rangpur (Sivasagar), and resisted repeated Mughal invasions — most famously under the general Lachit Borphukan at the naval battle of Saraighat in 1671. In the 15th–16th centuries, Srimanta Sankardeva's Ekasarana Vaishnava movement transformed religion, music and theatre.\n\nBurmese invasions from 1817 devastated the kingdom, and the Treaty of Yandabo in 1826 brought Assam under the East India Company. The British established tea plantations from the 1830s and found oil at Digboi in 1889. Assam became a separate province in 1874; Nagaland, Meghalaya and Mizoram were later carved out of it. The great earthquake of 1950 reshaped the eastern valley. The Assam movement of 1979–85 ended with the Assam Accord, and later accords created the Bodoland Territorial Region.",
        "प्राचीन असम कामरूप राज्य था, जिस पर वर्मन, म्लेच्छ और पाल वंशों ने शासन किया; चीनी यात्री ह्वेनसांग 7वीं सदी में भास्करवर्मन के दरबार में आए। 1228 में ताई राजकुमार सुकाफ़ा ने पटकाई पहाड़ियाँ पार कर अहोम राज्य की स्थापना की, जिसने लगभग छह सदियों तक ब्रह्मपुत्र घाटी पर शासन किया, चराइदेउ, गढ़गाँव और रंगपुर (शिवसागर) में राजधानियाँ बनाईं, और बार-बार के मुग़ल आक्रमणों का सामना किया — सबसे प्रसिद्ध रूप से 1671 में सराईघाट के नौसैनिक युद्ध में सेनापति लाचित बरफुकन के नेतृत्व में। 15वीं–16वीं सदी में श्रीमंत शंकरदेव के एकशरण वैष्णव आंदोलन ने धर्म, संगीत और रंगमंच को बदल दिया।\n\n1817 से बर्मी आक्रमणों ने राज्य को तबाह कर दिया, और 1826 की यांडाबू संधि से असम ईस्ट इंडिया कंपनी के अधीन आया। अंग्रेज़ों ने 1830 के दशक से चाय बाग़ान बनाए और 1889 में डिगबोई में तेल पाया। असम 1874 में अलग प्रांत बना; बाद में नागालैंड, मेघालय और मिज़ोरम इससे अलग हुए। 1950 के महान भूकंप ने पूर्वी घाटी का स्वरूप बदल दिया। 1979–85 का असम आंदोलन असम समझौते के साथ समाप्त हुआ, और बाद के समझौतों से बोडोलैंड प्रादेशिक क्षेत्र बना।",
        "प्राचीन आसाम हे कामरूप राज्य होते, ज्यावर वर्मन, म्लेच्छ व पाल घराण्यांनी राज्य केले; चिनी यात्री ह्वेनसांग सातव्या शतकात भास्करवर्मनच्या दरबारात आला. 1228 मध्ये ताई राजपुत्र सुकाफाने पटकाई डोंगर ओलांडून अहोम राज्याची स्थापना केली, ज्याने सुमारे सहा शतके ब्रह्मपुत्रा खोऱ्यावर राज्य केले, चराइदेव, गढगाव व रंगपूर (शिवसागर) येथे राजधान्या उभारल्या, आणि वारंवारच्या मुघल आक्रमणांना तोंड दिले — सर्वांत प्रसिद्ध म्हणजे 1671 मध्ये सराईघाटच्या नौयुद्धात सेनापती लाचित बरफुकन यांच्या नेतृत्वाखाली. पंधराव्या–सोळाव्या शतकात श्रीमंत शंकरदेवांच्या एकशरण वैष्णव चळवळीने धर्म, संगीत व रंगभूमी बदलून टाकली.\n\n1817 पासूनच्या ब्रह्मी आक्रमणांनी राज्य उद्ध्वस्त केले, आणि 1826 च्या यांदाबू तहाने आसाम ईस्ट इंडिया कंपनीच्या अधिपत्याखाली आला. इंग्रजांनी 1830 च्या दशकापासून चहामळे उभारले आणि 1889 मध्ये डिगबोई येथे तेल सापडले. आसाम 1874 मध्ये स्वतंत्र प्रांत झाला; नंतर नागालँड, मेघालय व मिझोराम त्यातून वेगळे झाले. 1950 च्या महाभूकंपाने पूर्वेकडील खोऱ्याचे स्वरूप बदलले. 1979–85 चे आसाम आंदोलन आसाम करारासह संपले, आणि नंतरच्या करारांतून बोडोलँड प्रादेशिक क्षेत्र निर्माण झाले."),
        conf="Editorial"),
    timeline([
        ev("ahom", 1228, L("1228", "1228", "1228"), L("Sukaphaa founds the Ahom kingdom", "सुकाफ़ा ने अहोम राज्य की स्थापना की", "सुकाफाने अहोम राज्याची स्थापना केली")),
        ev("sankardeva", 1449, L("1449", "1449", "1449"), L("Birth of Srimanta Sankardeva", "श्रीमंत शंकरदेव का जन्म", "श्रीमंत शंकरदेवांचा जन्म")),
        ev("saraighat", 1671, L("1671", "1671", "1671"), L("Battle of Saraighat", "सराईघाट का युद्ध", "सराईघाटची लढाई")),
        ev("yandabo", 1826, L("1826", "1826", "1826"), L("Treaty of Yandabo; British rule begins", "यांडाबू संधि; ब्रिटिश शासन आरंभ", "यांदाबूचा तह; ब्रिटिश सत्ता सुरू")),
        ev("province", 1874, L("1874", "1874", "1874"), L("Assam becomes a separate province", "असम अलग प्रांत बना", "आसाम स्वतंत्र प्रांत बनला")),
        ev("digboi", 1889, L("1889", "1889", "1889"), L("Oil struck at Digboi", "डिगबोई में तेल मिला", "डिगबोई येथे तेल सापडले")),
        ev("quake", 1950, L("15 August 1950", "15 अगस्त 1950", "15 ऑगस्ट 1950"), L("Great Assam earthquake", "असम का महान भूकंप", "आसामचा महाभूकंप")),
        ev("accord", 1985, L("15 August 1985", "15 अगस्त 1985", "15 ऑगस्ट 1985"), L("Assam Accord signed", "असम समझौते पर हस्ताक्षर", "आसाम करारावर स्वाक्षरी")),
        ev("moidams", 2024, L("2024", "2024", "2024"), L("Charaideo Moidams inscribed as a World Heritage Site", "चराइदेउ मोइदाम विश्व धरोहर स्थल घोषित", "चराइदेव मोइदाम जागतिक वारसा स्थळ घोषित")),
        ev("cm2026", 2026, L("12 May 2026", "12 मई 2026", "12 मे 2026"), L("Himanta Biswa Sarma sworn in for a second term", "हिमंत बिस्व सरमा ने दूसरी बार शपथ ली", "हिमंत बिस्व सरमा यांचा दुसऱ्यांदा शपथविधी")),
    ]),
    lst("heritage", [
        it3("moidams", "Moidams of Charaideo", "चराइदेउ के मोइदाम", "चराइदेवचे मोइदाम", m=("UNESCO 2024", "यूनेस्को 2024", "युनेस्को 2024"), url=UNESCO, src="unesco-whc"),
        it3("kaziranga", "Kaziranga National Park", "काज़ीरंगा राष्ट्रीय उद्यान", "काझीरंगा राष्ट्रीय उद्यान", m=("UNESCO 1985", "यूनेस्को 1985", "युनेस्को 1985"), url=UNESCO, src="unesco-whc"),
        it3("manas", "Manas Wildlife Sanctuary", "मानस वन्यजीव अभयारण्य", "मानस वन्यजीव अभयारण्य", m=("UNESCO 1985", "यूनेस्को 1985", "युनेस्को 1985"), url=UNESCO, src="unesco-whc"),
        it3("ranghar", "Rang Ghar and Talatal Ghar, Sivasagar", "रंग घर और तलातल घर, शिवसागर", "रंग घर व तलातल घर, शिवसागर", m=("Ahom monuments", "अहोम स्मारक", "अहोम स्मारके")),
        it3("kamakhya", "Kamakhya temple, Guwahati", "कामाख्या मंदिर, गुवाहाटी", "कामाख्या मंदिर, गुवाहाटी", m=("Shakti peetha", "शक्तिपीठ", "शक्तिपीठ")),
        it3("satras", "Satras of Majuli", "माजुली के सत्र", "माजुलीचे सत्र", m=("Vaishnava monasteries", "वैष्णव मठ", "वैष्णव मठ")),
        it3("madan", "Madan Kamdev", "मदन कामदेव", "मदन कामदेव", m=("Ruined temples, 10th–12th century", "मंदिर अवशेष, 10वीं–12वीं सदी", "मंदिरांचे अवशेष, दहावे–बारावे शतक")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("as mod1 ok")
