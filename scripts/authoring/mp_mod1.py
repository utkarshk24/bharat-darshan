"""Madhya Pradesh modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-MP"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
mp = read("regions/IN-MP.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Madhya Pradesh — the 'middle province' — lies at the heart of India. With 3.08 lakh km² it is the second-largest State by area, and it had 7.26 crore people at the 2011 Census. It is a land of plateaus, forests and rivers: the Narmada flows west through a valley between the Vindhya and Satpura ranges, and the Chambal, Betwa, Ken and Son drain the north and east. Bhopal, the City of Lakes, is the capital; Indore is the largest city and commercial centre, and Jabalpur, Gwalior and Ujjain are other major cities.\n\nThe State took its present form on 1 November 2000, when Chhattisgarh was separated from it. Hindi is the official language.",
        "मध्य प्रदेश — 'मध्य का प्रांत' — भारत के हृदय में स्थित है। 3.08 लाख वर्ग किमी के साथ यह क्षेत्रफल में दूसरा सबसे बड़ा राज्य है, और 2011 की जनगणना में यहाँ 7.26 करोड़ लोग थे। यह पठारों, वनों और नदियों की भूमि है: नर्मदा विंध्य और सतपुड़ा पर्वतमालाओं के बीच की घाटी में पश्चिम की ओर बहती है, और चंबल, बेतवा, केन और सोन उत्तर और पूर्व का जल बहाती हैं। झीलों की नगरी भोपाल राजधानी है; इंदौर सबसे बड़ा शहर और वाणिज्यिक केंद्र है, और जबलपुर, ग्वालियर और उज्जैन अन्य प्रमुख शहर हैं।\n\nराज्य ने 1 नवंबर 2000 को, जब छत्तीसगढ़ इससे अलग हुआ, अपना वर्तमान रूप लिया। हिंदी राजभाषा है।",
        "मध्य प्रदेश — 'मधला प्रांत' — भारताच्या हृदयस्थानी आहे. 3.08 लाख चौ.किमीसह ते क्षेत्रफळाने दुसरे सर्वांत मोठे राज्य आहे, आणि 2011 च्या जनगणनेनुसार इथे 7.26 कोटी लोक होते. ही पठारे, जंगले व नद्यांची भूमी आहे: नर्मदा विंध्य व सातपुडा पर्वतरांगांमधील खोऱ्यातून पश्चिमेकडे वाहते, आणि चंबळ, बेतवा, केन व सोन उत्तर व पूर्वेचे पाणी वाहून नेतात. सरोवरांचे शहर भोपाळ ही राजधानी आहे; इंदूर हे सर्वांत मोठे शहर व व्यापारी केंद्र आहे, आणि जबलपूर, ग्वाल्हेर व उज्जैन ही इतर प्रमुख शहरे आहेत.\n\n1 नोव्हेंबर 2000 रोजी छत्तीसगड वेगळे झाल्यावर राज्याला सध्याचे स्वरूप मिळाले. हिंदी ही राजभाषा आहे."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Madhya Pradesh has the largest forest cover of any Indian State and more wild tigers than any other, in reserves such as Kanha, Bandhavgarh, Pench and Panna; Kuno National Park is where cheetahs were brought back to India in 2022. Three UNESCO World Heritage Sites — the temples of Khajuraho, the Buddhist monuments at Sanchi and the rock shelters of Bhimbetka — lie within the State, along with the Mahakaleshwar and Omkareshwar jyotirlingas, the forts of Gwalior and Mandu and the riverside town of Maheshwar. It is India's largest producer of soybean, and Indore is known for its cleanliness and its street food.",
        "मध्य प्रदेश में किसी भी भारतीय राज्य से अधिक वन आवरण है और कान्हा, बांधवगढ़, पेंच और पन्ना जैसे अभयारण्यों में किसी भी अन्य राज्य से अधिक जंगली बाघ हैं; कूनो राष्ट्रीय उद्यान में 2022 में भारत में चीते वापस लाए गए। तीन यूनेस्को विश्व धरोहर स्थल — खजुराहो के मंदिर, साँची के बौद्ध स्मारक और भीमबेटका के शैलाश्रय — राज्य में हैं, साथ में महाकालेश्वर और ओंकारेश्वर ज्योतिर्लिंग, ग्वालियर और मांडू के क़िले और नदी किनारे बसा महेश्वर। यह भारत का सबसे बड़ा सोयाबीन उत्पादक है, और इंदौर अपनी स्वच्छता और सड़क के व्यंजनों के लिए प्रसिद्ध है।",
        "मध्य प्रदेशात कोणत्याही भारतीय राज्यापेक्षा जास्त वनाच्छादन आहे आणि कान्हा, बांधवगड, पेंच व पन्ना यांसारख्या प्रकल्पांत इतर कोणत्याही राज्यापेक्षा जास्त जंगली वाघ आहेत; कुनो राष्ट्रीय उद्यानात 2022 मध्ये भारतात चित्ते परत आणले गेले. तीन युनेस्को जागतिक वारसा स्थळे — खजुराहोची मंदिरे, सांचीची बौद्ध स्मारके व भीमबेटकाची शैलाश्रये — राज्यात आहेत, सोबत महाकालेश्वर व ओंकारेश्वर ज्योतिर्लिंगे, ग्वाल्हेर व मांडूचे किल्ले आणि नदीकाठचे महेश्वर. हे भारतातील सर्वांत मोठे सोयाबीन उत्पादक आहे, आणि इंदूर स्वच्छता व रस्त्यावरील खाद्यपदार्थांसाठी प्रसिद्ध आहे."),
        title=L("What makes Madhya Pradesh unique?", "मध्य प्रदेश को ख़ास क्या बनाता है?", "मध्य प्रदेशचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formed", "गठन", "निर्मिती"), L("1 November 1956; present boundaries from 1 November 2000", "1 नवंबर 1956; वर्तमान सीमाएँ 1 नवंबर 2000 से", "1 नोव्हेंबर 1956; सध्याच्या सीमा 1 नोव्हेंबर 2000 पासून")],
           [L("Districts", "ज़िले", "जिल्हे"), "55"],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Hindi", "हिंदी", "हिंदी")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Madhya Pradesh High Court, Jabalpur, with benches at Indore and Gwalior", "मध्य प्रदेश उच्च न्यायालय, जबलपुर, इंदौर और ग्वालियर में पीठ", "मध्य प्रदेश उच्च न्यायालय, जबलपूर, इंदूर व ग्वाल्हेर येथे खंडपीठ")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-MP / MP"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; the district count (55, after Maihar, Mauganj and Pandhurna were created in 2023) is to be linked to the State's notification.",
                 "संपादकीय; ज़िलों की संख्या (55, 2023 में मैहर, मऊगंज और पांढुर्णा बनने के बाद) राज्य अधिसूचना से जोड़ी जाएगी।",
                 "संपादकीय; जिल्ह्यांची संख्या (55, 2023 मध्ये मैहर, मऊगंज व पांढुर्णा निर्माण झाल्यानंतर) राज्य अधिसूचनेशी जोडली जाईल.")),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Madhya Pradesh is a land-locked State of plateaus and low ranges. In the west the black-soil Malwa plateau surrounds Indore and Ujjain; to the north lie the Gwalior–Chambal ravines and the rocky Bundelkhand upland; in the east Baghelkhand rises towards the Kaimur hills. The Vindhya range runs across the middle of the State, and south of it the Narmada flows west through a long rift valley; beyond the river the Satpura range holds Pachmarhi and Dhupgarh, the State's highest point. The Narmada and the Son both rise at Amarkantak, flowing in opposite directions. The Tapti rises at Multai in Betul district.",
        "मध्य प्रदेश पठारों और नीची पर्वतमालाओं वाला एक भू-आबद्ध राज्य है। पश्चिम में काली मिट्टी वाला मालवा पठार इंदौर और उज्जैन को घेरता है; उत्तर में ग्वालियर–चंबल के बीहड़ और पथरीला बुंदेलखंड क्षेत्र है; पूर्व में बघेलखंड कैमूर पहाड़ियों की ओर उठता है। विंध्य पर्वतमाला राज्य के बीच से गुज़रती है, और उसके दक्षिण में नर्मदा एक लंबी भ्रंश घाटी में पश्चिम की ओर बहती है; नदी के पार सतपुड़ा पर्वतमाला में पचमढ़ी और राज्य का सबसे ऊँचा स्थान धूपगढ़ है। नर्मदा और सोन दोनों अमरकंटक से निकलती हैं और विपरीत दिशाओं में बहती हैं। ताप्ती बैतूल ज़िले के मुलताई से निकलती है।",
        "मध्य प्रदेश हे पठारे व कमी उंचीच्या पर्वतरांगांचे भूवेष्टित राज्य आहे. पश्चिमेला काळ्या मातीचे माळवा पठार इंदूर व उज्जैनला वेढते; उत्तरेला ग्वाल्हेर–चंबळची घळी व खडकाळ बुंदेलखंड आहे; पूर्वेला बघेलखंड कैमूर डोंगरांकडे उंचावतो. विंध्य पर्वतरांग राज्याच्या मधोमध जाते, आणि तिच्या दक्षिणेला नर्मदा एका लांब खचदरीतून पश्चिमेकडे वाहते; नदीपलीकडील सातपुडा रांगेत पचमढी व राज्याचे सर्वोच्च ठिकाण धूपगड आहे. नर्मदा व सोन दोन्ही अमरकंटक येथे उगम पावून विरुद्ध दिशांना वाहतात. तापी बैतूल जिल्ह्यातील मुलताई येथे उगम पावते."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), mp["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("rj", "Rajasthan (north-west)", "राजस्थान (उत्तर-पश्चिम)", "राजस्थान (वायव्य)"), it3("up", "Uttar Pradesh (north)", "उत्तर प्रदेश (उत्तर)", "उत्तर प्रदेश (उत्तर)"),
        it3("ct", "Chhattisgarh (east)", "छत्तीसगढ़ (पूर्व)", "छत्तीसगड (पूर्व)"), it3("mh", "Maharashtra (south)", "महाराष्ट्र (दक्षिण)", "महाराष्ट्र (दक्षिण)"),
        it3("gj", "Gujarat (west)", "गुजरात (पश्चिम)", "गुजरात (पश्चिम)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("narmada", "Narmada", "नर्मदा", "नर्मदा", d=("Rises at Amarkantak and flows west to Gujarat; dams at Bargi, Indira Sagar and Omkareshwar.", "अमरकंटक से निकलकर पश्चिम में गुजरात तक बहती है; बरगी, इंदिरा सागर और ओंकारेश्वर पर बाँध।", "अमरकंटक येथे उगम पावून पश्चिमेकडे गुजरातपर्यंत वाहते; बरगी, इंदिरा सागर व ओंकारेश्वर येथे धरणे.")),
        it3("chambal", "Chambal", "चंबल", "चंबळ", d=("Rises near Mhow and flows north; Gandhi Sagar dam; gharial sanctuary.", "महू के पास से निकलकर उत्तर बहती है; गांधी सागर बाँध; घड़ियाल अभयारण्य।", "महूजवळ उगम पावून उत्तरेकडे वाहते; गांधी सागर धरण; घडियाल अभयारण्य.")),
        it3("betwa", "Betwa", "बेतवा", "बेतवा", d=("Flows past Vidisha and Orchha into Uttar Pradesh.", "विदिशा और ओरछा से होकर उत्तर प्रदेश जाती है।", "विदिशा व ओरछावरून उत्तर प्रदेशात जाते.")),
        it3("son", "Son", "सोन", "सोन", d=("Flows east from Amarkantak to join the Ganga in Bihar; Bansagar dam.", "अमरकंटक से पूर्व बहकर बिहार में गंगा से मिलती है; बाणसागर बाँध।", "अमरकंटकहून पूर्वेकडे वाहत बिहारमध्ये गंगेला मिळते; बाणसागर धरण.")),
        it3("tapti", "Tapti", "ताप्ती", "तापी", d=("Rises at Multai and flows west through Burhanpur.", "मुलताई से निकलकर बुरहानपुर से होकर पश्चिम बहती है।", "मुलताई येथे उगम पावून बुरहानपूरमार्गे पश्चिमेकडे वाहते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Dhupgarh — official elevation", "धूपगढ़ — आधिकारिक ऊँचाई", "धूपगड — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Madhya Pradesh has a subtropical climate with three clear seasons. Summers (March–June) are hot and dry, hottest in the north around Gwalior and in Bundelkhand. The south-west monsoon (mid-June to September) brings most of the year's rain, heaviest in the south-east around Mandla and Balaghat and lighter in the north-west. Winters (November–February) are cool and dry, with cold nights in Gwalior and the north and pleasant days elsewhere; Pachmarhi, in the Satpuras, is the State's hill station.",
        "मध्य प्रदेश में तीन स्पष्ट ऋतुओं वाली उपोष्ण जलवायु है। गर्मियाँ (मार्च–जून) गर्म और सूखी होती हैं, सबसे गर्म उत्तर में ग्वालियर के आसपास और बुंदेलखंड में। दक्षिण-पश्चिम मानसून (मध्य जून से सितंबर) साल की अधिकांश वर्षा लाता है — सबसे अधिक दक्षिण-पूर्व में मंडला और बालाघाट के आसपास और उत्तर-पश्चिम में कम। सर्दियाँ (नवंबर–फ़रवरी) ठंडी और सूखी होती हैं — ग्वालियर और उत्तर में ठंडी रातें और अन्यत्र सुहावने दिन; सतपुड़ा में पचमढ़ी राज्य का पर्वतीय स्थल है।",
        "मध्य प्रदेशात तीन स्पष्ट ऋतूंचे उपोष्ण हवामान आहे. उन्हाळा (मार्च–जून) उष्ण व कोरडा असतो — सर्वाधिक उष्ण उत्तरेत ग्वाल्हेरभोवती व बुंदेलखंडात. नैर्ऋत्य मान्सून (जूनच्या मध्यापासून सप्टेंबरपर्यंत) वर्षाचा बहुतांश पाऊस आणतो — सर्वाधिक आग्नेयेत मंडला व बालाघाटभोवती आणि वायव्येत कमी. हिवाळा (नोव्हेंबर–फेब्रुवारी) थंड व कोरडा असतो — ग्वाल्हेर व उत्तरेत थंड रात्री आणि इतरत्र सुखद दिवस; सातपुड्यातील पचमढी हे राज्याचे थंड हवेचे ठिकाण आहे."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Bhopal", "भोपाल", "भोपाळ"), "lat": 23.2599, "lon": 77.4126},
        {"name": L("Indore", "इंदौर", "इंदूर"), "lat": 22.7196, "lon": 75.8577},
        {"name": L("Gwalior", "ग्वालियर", "ग्वाल्हेर"), "lat": 26.2183, "lon": 78.1828},
        {"name": L("Pachmarhi", "पचमढ़ी", "पचमढी"), "lat": 22.4674, "lon": 78.4346},
    ]},
    lst("best", [
        it3("winter", "October to March", "अक्टूबर से मार्च", "ऑक्टोबर ते मार्च", d=("Best for monuments and wildlife; Khajuraho Dance Festival in February.", "स्मारकों और वन्यजीवों के लिए सबसे अच्छा; फ़रवरी में खजुराहो नृत्य महोत्सव।", "स्मारके व वन्यजीवांसाठी उत्तम; फेब्रुवारीत खजुराहो नृत्य महोत्सव.")),
        it3("summer", "April to June", "अप्रैल से जून", "एप्रिल ते जून", d=("Hot, but the best tiger sightings as animals visit water holes; parks close in the monsoon.", "गर्मी, लेकिन बाघ देखने का सबसे अच्छा समय क्योंकि जानवर जलाशयों पर आते हैं; मानसून में उद्यान बंद।", "उष्ण, पण वाघ दिसण्याचा उत्तम काळ कारण प्राणी पाणवठ्यांवर येतात; पावसाळ्यात उद्याने बंद.")),
        it3("monsoon", "July to September", "जुलाई से सितंबर", "जुलै ते सप्टेंबर", d=("Waterfalls and green hills at Pachmarhi, Mandu and Bhedaghat.", "पचमढ़ी, मांडू और भेड़ाघाट में झरने और हरी पहाड़ियाँ।", "पचमढी, मांडू व भेडाघाट येथे धबधबे व हिरवे डोंगर.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall (East and West Madhya Pradesh)", "सामान्य वार्षिक वर्षा (पूर्वी और पश्चिमी मध्य प्रदेश)", "सरासरी वार्षिक पाऊस (पूर्व व पश्चिम मध्य प्रदेश)"), "imd", "IMD rainfall statistics by sub-division."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Madhya Pradesh moves at an unhurried pace. In Indore the day starts with poha and jalebi and ends at the Sarafa night market; Bhopal's old city of mosques and bazaars wraps around its lakes; Ujjain and Omkareshwar fill with pilgrims at dawn aartis on the riverbanks. Across the countryside, life follows the wheat and soybean seasons, weekly haats bring tribal villages together, and folk songs in Malwi, Bundeli and Nimadi accompany festivals. Forests are never far away, and in the tiger reserves villages and wildlife share the land.",
        "मध्य प्रदेश में जीवन इत्मीनान से चलता है। इंदौर में दिन पोहा-जलेबी से शुरू होकर सराफ़ा के रात्रि बाज़ार में ख़त्म होता है; भोपाल का मस्जिदों और बाज़ारों वाला पुराना शहर उसकी झीलों के चारों ओर फैला है; उज्जैन और ओंकारेश्वर भोर में नदी तटों पर होने वाली आरतियों में तीर्थयात्रियों से भर जाते हैं। गाँवों में जीवन गेहूँ और सोयाबीन के मौसम के साथ चलता है, साप्ताहिक हाट आदिवासी गाँवों को साथ लाते हैं, और त्योहारों में मालवी, बुंदेली और निमाड़ी लोकगीत गूँजते हैं। वन कभी दूर नहीं होते, और बाघ अभयारण्यों में गाँव और वन्यजीव भूमि साझा करते हैं।",
        "मध्य प्रदेशात जीवन निवांत गतीने चालते. इंदूरमध्ये दिवसाची सुरुवात पोहे-जिलेबीने होऊन सराफ्याच्या रात्रीच्या बाजारात शेवट होतो; भोपाळचे मशिदी व बाजारांचे जुने शहर सरोवरांभोवती पसरले आहे; उज्जैन व ओंकारेश्वर पहाटे नदीकाठच्या आरत्यांना यात्रेकरूंनी भरून जातात. गावांत जीवन गहू व सोयाबीनच्या हंगामांनुसार चालते, आठवडी बाजार आदिवासी गावांना एकत्र आणतात, आणि सणांना माळवी, बुंदेली व निमाडी लोकगीते गुंजतात. जंगले कधीच दूर नसतात, आणि व्याघ्र प्रकल्पांत गावे व वन्यजीव भूमी सामायिक करतात."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Madhya Pradesh had 7.26 crore people at the 2011 Census, with a density of about 236 per km². The sex ratio was 931 women per 1,000 men (919 in 2001), and the child sex ratio fell from 932 to 918. Literacy was 69.3%, below the national 73.0%. Scheduled Tribes made up 21.1% of the population — 1.53 crore people, the largest tribal population of any State — mainly Bhils, Gonds, Baigas, Korkus, Bharias and Sahariyas. Scheduled Castes were 15.6%.\n\nHindi is the official language, spoken with regional forms such as Malwi, Bundeli, Bagheli and Nimadi. Bhili and Gondi are the main tribal languages, and Marathi, Urdu and Sindhi are also spoken.",
        "2011 की जनगणना में मध्य प्रदेश की जनसंख्या 7.26 करोड़ थी, और घनत्व लगभग 236 प्रति वर्ग किमी। लिंगानुपात प्रति 1,000 पुरुषों पर 931 महिलाएँ (2001 में 919) था, और शिशु लिंगानुपात 932 से घटकर 918 हो गया। साक्षरता 69.3% थी, जो राष्ट्रीय 73.0% से कम है। अनुसूचित जनजातियाँ जनसंख्या का 21.1% थीं — 1.53 करोड़ लोग, जो किसी भी राज्य की सबसे बड़ी जनजातीय आबादी है — मुख्यतः भील, गोंड, बैगा, कोरकू, भारिया और सहरिया। अनुसूचित जातियाँ 15.6% थीं।\n\nहिंदी राजभाषा है, जो मालवी, बुंदेली, बघेली और निमाड़ी जैसे क्षेत्रीय रूपों में बोली जाती है। भीली और गोंडी मुख्य आदिवासी भाषाएँ हैं, और मराठी, उर्दू और सिंधी भी बोली जाती हैं।",
        "2011 च्या जनगणनेनुसार मध्य प्रदेशची लोकसंख्या 7.26 कोटी होती, आणि घनता सुमारे 236 प्रति चौ.किमी. दर 1,000 पुरुषांमागे 931 स्त्रिया (2001 मध्ये 919) होत्या, आणि बाल लिंग गुणोत्तर 932 वरून 918 वर घसरले. साक्षरता 69.3% होती, राष्ट्रीय 73.0% पेक्षा कमी. अनुसूचित जमाती लोकसंख्येच्या 21.1% होत्या — 1.53 कोटी लोक, कोणत्याही राज्यातील सर्वांत मोठी आदिवासी लोकसंख्या — मुख्यतः भिल्ल, गोंड, बैगा, कोरकू, भारिया व सहरिया. अनुसूचित जाती 15.6% होत्या.\n\nहिंदी ही राजभाषा असून ती माळवी, बुंदेली, बघेली व निमाडी यांसारख्या प्रादेशिक रूपांत बोलली जाते. भिली व गोंडी या मुख्य आदिवासी भाषा आहेत, आणि मराठी, उर्दू व सिंधीही बोलल्या जातात."),
        sources=["census", "es-india", "dl-planning"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), mp["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), mp["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(919, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), mp["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(932, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), mp["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), mp["density2011"], "number"),
        fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
             dp(15.6, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 113.42 lakh people."), "percent"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(21.1, "%", "2011", "census", "dl-planning", SCST, note="Same table: 153.17 lakh people."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("hi", "Hindi", "हिंदी", "हिंदी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("mup", "Malwi", "मालवी", "माळवी"), it3("bns", "Bundeli", "बुंदेली", "बुंदेली"), it3("bfy", "Bagheli", "बघेली", "बघेली"), it3("noe", "Nimadi", "निमाड़ी", "निमाडी"),
        it3("bhb", "Bhili", "भीली", "भिली"), it3("gon", "Gondi", "गोंडी", "गोंडी"), it3("mr", "Marathi", "मराठी", "मराठी"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"), "census", "Census 2011 Final Population Totals for Madhya Pradesh."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "The rock shelters of Bhimbetka hold paintings made over many thousands of years. Avanti, with its capital at Ujjain, was one of the great kingdoms of ancient India; Ashoka governed from Ujjain as a prince and built the great stupa at Sanchi. Ujjain was later a centre of astronomy and learning, linked by tradition with Vikramaditya and the poet Kalidasa. The Paramaras of Malwa — among them Raja Bhoj — the Chandelas, who built the temples of Khajuraho, and the Kachchhapaghatas and Tomars of Gwalior ruled in medieval times, followed by the sultans of Malwa at Mandu and Gond kingdoms such as Garha-Mandla, whose queen Durgavati fell fighting the Mughals in 1564.\n\nIn the 18th century the Marathas took much of the region: the Scindias ruled from Gwalior and the Holkars from Indore, where Ahilyabai Holkar is remembered as a model ruler. In 1857 Rani Lakshmibai of Jhansi fell fighting near Gwalior. After Independence, Madhya Bharat, Vindhya Pradesh, Bhopal State and the Hindi-speaking districts of the Central Provinces were merged to form Madhya Pradesh on 1 November 1956. The Bhopal gas tragedy of December 1984 was among the world's worst industrial disasters. Chhattisgarh was carved out on 1 November 2000.",
        "भीमबेटका के शैलाश्रयों में हज़ारों वर्षों में बने चित्र हैं। उज्जैन राजधानी वाला अवंति प्राचीन भारत के बड़े राज्यों में था; अशोक ने राजकुमार के रूप में उज्जैन से शासन किया और साँची का महान स्तूप बनवाया। उज्जैन बाद में खगोल विज्ञान और विद्या का केंद्र रहा, जो परंपरा में विक्रमादित्य और कवि कालिदास से जुड़ा है। मध्यकाल में मालवा के परमार — जिनमें राजा भोज थे — खजुराहो के मंदिर बनवाने वाले चंदेल, और ग्वालियर के कच्छपघात और तोमरों ने शासन किया, उसके बाद मांडू के मालवा सुल्तान और गढ़ा-मंडला जैसे गोंड राज्य आए, जिनकी रानी दुर्गावती 1564 में मुग़लों से लड़ते हुए वीरगति को प्राप्त हुईं।\n\n18वीं सदी में मराठों ने क्षेत्र का बड़ा भाग जीता: सिंधिया ग्वालियर से और होलकर इंदौर से शासन करते थे, जहाँ अहिल्याबाई होलकर आदर्श शासक के रूप में याद की जाती हैं। 1857 में झाँसी की रानी लक्ष्मीबाई ग्वालियर के पास लड़ते हुए वीरगति को प्राप्त हुईं। आज़ादी के बाद मध्य भारत, विंध्य प्रदेश, भोपाल राज्य और मध्य प्रांत के हिंदी-भाषी ज़िलों को मिलाकर 1 नवंबर 1956 को मध्य प्रदेश बना। दिसंबर 1984 की भोपाल गैस त्रासदी दुनिया की सबसे भीषण औद्योगिक दुर्घटनाओं में थी। 1 नवंबर 2000 को छत्तीसगढ़ अलग हुआ।",
        "भीमबेटकाच्या शैलाश्रयांत हजारो वर्षांत काढलेली चित्रे आहेत. उज्जैन राजधानी असलेले अवंती हे प्राचीन भारतातील मोठ्या राज्यांपैकी होते; अशोकाने राजपुत्र म्हणून उज्जैनहून कारभार केला व सांचीचा महान स्तूप बांधला. उज्जैन नंतर खगोलशास्त्र व विद्येचे केंद्र होते, जे परंपरेने विक्रमादित्य व कवी कालिदासाशी जोडले जाते. मध्ययुगात माळव्याचे परमार — ज्यांत राजा भोज होते — खजुराहोची मंदिरे बांधणारे चंदेल, आणि ग्वाल्हेरचे कच्छपघात व तोमर यांनी राज्य केले, त्यानंतर मांडूचे माळवा सुलतान आणि गढा-मंडलासारखी गोंड राज्ये आली, जिची राणी दुर्गावती 1564 मध्ये मुघलांशी लढताना धारातीर्थी पडली.\n\nअठराव्या शतकात मराठ्यांनी प्रदेशाचा मोठा भाग जिंकला: शिंदे ग्वाल्हेरहून व होळकर इंदूरहून राज्य करत, जिथे अहिल्याबाई होळकर आदर्श शासक म्हणून स्मरणात आहेत. 1857 मध्ये झाशीची राणी लक्ष्मीबाई ग्वाल्हेरजवळ लढताना धारातीर्थी पडली. स्वातंत्र्यानंतर मध्य भारत, विंध्य प्रदेश, भोपाळ राज्य व मध्य प्रांतातील हिंदीभाषक जिल्हे एकत्र करून 1 नोव्हेंबर 1956 रोजी मध्य प्रदेश बनले. डिसेंबर 1984 ची भोपाळ वायू दुर्घटना ही जगातील सर्वांत भीषण औद्योगिक दुर्घटनांपैकी होती. 1 नोव्हेंबर 2000 रोजी छत्तीसगड वेगळे झाले."),
        conf="Editorial"),
    timeline([
        ev("sanchi", -250, L("3rd century BCE", "ई.पू. तीसरी सदी", "इ.स.पू. तिसरे शतक"), L("Great Stupa at Sanchi begun under Ashoka", "अशोक के समय साँची का महान स्तूप आरंभ", "अशोकाच्या काळात सांचीच्या महान स्तूपाची सुरुवात")),
        ev("khajuraho", 1000, L("c. 950–1050", "लगभग 950–1050", "सुमारे 950–1050"), L("Chandela temples of Khajuraho built", "खजुराहो के चंदेल मंदिरों का निर्माण", "खजुराहोच्या चंदेल मंदिरांची उभारणी")),
        ev("durgavati", 1564, L("1564", "1564", "1564"), L("Rani Durgavati falls fighting the Mughals", "रानी दुर्गावती मुग़लों से लड़ते हुए वीरगति को प्राप्त", "राणी दुर्गावती मुघलांशी लढताना धारातीर्थी")),
        ev("ahilya", 1767, L("1767–1795", "1767–1795", "1767–1795"), L("Ahilyabai Holkar rules from Maheshwar", "अहिल्याबाई होलकर का महेश्वर से शासन", "अहिल्याबाई होळकरांचा महेश्वरहून कारभार")),
        ev("lakshmibai", 1858, L("June 1858", "जून 1858", "जून 1858"), L("Rani Lakshmibai falls near Gwalior", "रानी लक्ष्मीबाई ग्वालियर के पास वीरगति को प्राप्त", "राणी लक्ष्मीबाई ग्वाल्हेरजवळ धारातीर्थी")),
        ev("formed", 1956, L("1 November 1956", "1 नवंबर 1956", "1 नोव्हेंबर 1956"), L("Madhya Pradesh formed", "मध्य प्रदेश का गठन", "मध्य प्रदेशची स्थापना")),
        ev("gas", 1984, L("2–3 December 1984", "2–3 दिसंबर 1984", "2–3 डिसेंबर 1984"), L("Bhopal gas tragedy", "भोपाल गैस त्रासदी", "भोपाळ वायू दुर्घटना")),
        ev("ct", 2000, L("1 November 2000", "1 नवंबर 2000", "1 नोव्हेंबर 2000"), L("Chhattisgarh separated", "छत्तीसगढ़ अलग हुआ", "छत्तीसगड वेगळे")),
        ev("cheetah", 2022, L("17 September 2022", "17 सितंबर 2022", "17 सप्टेंबर 2022"), L("Cheetahs released in Kuno National Park", "कूनो राष्ट्रीय उद्यान में चीते छोड़े गए", "कुनो राष्ट्रीय उद्यानात चित्ते सोडले")),
    ]),
    lst("heritage", [
        it3("khajuraho", "Khajuraho Group of Monuments", "खजुराहो स्मारक समूह", "खजुराहो स्मारक समूह", m=("UNESCO 1986", "यूनेस्को 1986", "युनेस्को 1986"), url=UNESCO, src="unesco-whc"),
        it3("sanchi", "Buddhist Monuments at Sanchi", "साँची के बौद्ध स्मारक", "सांचीची बौद्ध स्मारके", m=("UNESCO 1989", "यूनेस्को 1989", "युनेस्को 1989"), url=UNESCO, src="unesco-whc"),
        it3("bhimbetka", "Rock Shelters of Bhimbetka", "भीमबेटका के शैलाश्रय", "भीमबेटकाची शैलाश्रये", m=("UNESCO 2003", "यूनेस्को 2003", "युनेस्को 2003"), url=UNESCO, src="unesco-whc"),
        it3("gwalior", "Gwalior Fort", "ग्वालियर क़िला", "ग्वाल्हेर किल्ला", m=("Man Singh Palace", "मान सिंह महल", "मानसिंह महाल")),
        it3("mandu", "Mandu", "मांडू", "मांडू", m=("Malwa sultanate", "मालवा सल्तनत", "माळवा सुलतानशाही")),
        it3("orchha", "Orchha", "ओरछा", "ओरछा", m=("Bundela palaces and temples", "बुंदेला महल और मंदिर", "बुंदेला राजवाडे व मंदिरे")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("mp mod1 ok")
