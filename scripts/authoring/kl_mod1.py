import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-KL"
KL_SPB = "https://spb.kerala.gov.in/economic-review/ER2015/Chapter1/chapter01.html"
PRS = "https://prsindia.org/billtrack/the-kerala-alteration-of-name-bill-2026"
ONM = "https://www.onmanorama.com/news/kerala/2026/08/26/its-official-kerala-is-now-keralam-as-centre-notifies-name-change.html"
ECI = "https://results.eci.gov.in/ResultAcGenMay2026/partywiseresult-S11.htm"
mo = research("mospi_kl.json")
kl = read("regions/IN-KL.json")["metrics"]; ind = read("india.json")["metrics"]
NAME = L("Keralam", "केरलम", "केरळम")

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Keralam, known until August 2026 as Kerala, is a narrow State on India's south-western coast, squeezed between the Arabian Sea and the Western Ghats. Lagoons and backwaters line the coast, rice fields and coconut groves fill the midlands, and tea, cardamom and rubber estates climb the hills. Thiruvananthapuram is the capital; Kochi is the main port and commercial city.\n\nThe State was formed on 1 November 1956, when Travancore-Cochin was joined with the Malabar district of Madras State on linguistic lines. Malayalam is the official language. Parliament passed the Kerala (Alteration of Name) Bill in August 2026, and the new name, Keralam, came into force on 25 August 2026.",
        "केरलम, जिसे अगस्त 2026 तक केरल कहा जाता था, भारत के दक्षिण-पश्चिमी तट पर अरब सागर और पश्चिमी घाट के बीच बसा एक संकरा राज्य है। तट के साथ लैगून और बैकवाटर फैले हैं, बीच के भाग में धान के खेत और नारियल के बाग़ हैं, और पहाड़ियों पर चाय, इलायची और रबर के बागान हैं। तिरुवनंतपुरम राजधानी है; कोच्चि प्रमुख बंदरगाह और व्यावसायिक शहर है।\n\nराज्य का गठन 1 नवंबर 1956 को हुआ, जब भाषाई आधार पर त्रावणकोर-कोचीन को मद्रास राज्य के मलबार ज़िले के साथ जोड़ा गया। मलयालम राजभाषा है। संसद ने अगस्त 2026 में केरल (नाम परिवर्तन) विधेयक पारित किया और नया नाम केरलम 25 अगस्त 2026 से लागू हुआ।",
        "केरळम — ऑगस्ट 2026 पर्यंत केरळ म्हणून ओळखले जाणारे — भारताच्या नैर्ऋत्य किनाऱ्यावर अरबी समुद्र आणि पश्चिम घाट यांच्यामध्ये वसलेले चिंचोळे राज्य आहे. किनाऱ्यालगत खारकच्छ आणि बॅकवॉटर्स पसरले आहेत, मधल्या पट्ट्यात भातशेती आणि नारळाच्या बागा आहेत, तर डोंगरउतारांवर चहा, वेलची आणि रबराचे मळे आहेत. तिरुवनंतपुरम ही राजधानी असून कोची हे प्रमुख बंदर आणि व्यापारी शहर आहे.\n\nभाषिक आधारावर त्रावणकोर-कोचीन संस्थान मद्रास राज्याच्या मलबार जिल्ह्याशी जोडून 1 नोव्हेंबर 1956 रोजी राज्याची स्थापना झाली. मल्याळम ही राजभाषा आहे. संसदेने ऑगस्ट 2026 मध्ये केरळ (नावबदल) विधेयक मंजूर केले आणि केरळम हे नवे नाव 25 ऑगस्ट 2026 पासून लागू झाले."),
        sources=["prs", "onmanorama"], conf="Editorial"),
    prose("intro-unique", L(
        "Keralam stands out for its human-development record: the highest sex ratio of any State at the 2011 Census, near-universal literacy, and maternal and child mortality close to developed-country levels. Its culture is just as distinctive — Kathakali and Kutiyattam, temple festivals with caparisoned elephants, snake-boat races on the backwaters, and a cuisine built on coconut, rice, fish and spice. Centuries of sea trade brought Arab, Jewish, Syrian Christian, Portuguese and Dutch influences that are still visible in Kochi.",
        "केरलम अपने मानव विकास के रिकॉर्ड के लिए अलग दिखता है: 2011 की जनगणना में किसी भी राज्य से अधिक लिंगानुपात, लगभग सार्वभौमिक साक्षरता, और विकसित देशों के क़रीब मातृ एवं शिशु मृत्यु दर। इसकी संस्कृति भी उतनी ही विशिष्ट है — कथकली और कूडियाट्टम, सजे-धजे हाथियों वाले मंदिर उत्सव, बैकवाटर में सर्प-नौका दौड़, और नारियल, चावल, मछली व मसालों पर आधारित खान-पान। सदियों के समुद्री व्यापार से आए अरब, यहूदी, सीरियाई ईसाई, पुर्तगाली और डच प्रभाव आज भी कोच्चि में दिखते हैं।",
        "मानव विकासाच्या कामगिरीमुळे केरळम वेगळे ठरते: 2011 च्या जनगणनेत सर्व राज्यांत सर्वाधिक लिंग गुणोत्तर, जवळपास सार्वत्रिक साक्षरता आणि विकसित देशांच्या जवळ जाणारे माता व बालमृत्यूचे प्रमाण. इथली संस्कृतीही तितकीच वैशिष्ट्यपूर्ण आहे — कथकली आणि कूडियाट्टम, सजवलेल्या हत्तींचे मंदिरोत्सव, बॅकवॉटर्समधील सर्प-नौका शर्यती, आणि नारळ, भात, मासे व मसाल्यांवर आधारित खाद्यसंस्कृती. शतकानुशतकांच्या सागरी व्यापारामुळे आलेले अरब, ज्यू, सिरियन ख्रिश्चन, पोर्तुगीज आणि डच प्रभाव आजही कोचीत दिसतात."),
        title=L("What makes Keralam unique?", "केरलम को ख़ास क्या बनाता है?", "केरळमचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Formation", "गठन", "स्थापना"), L("1 November 1956 (Kerala Piravi)", "1 नवंबर 1956 (केरल पिरवी)", "1 नोव्हेंबर 1956 (केरळ पिरवी)")],
           [L("Name", "नाम", "नाव"), L("Keralam, in force from 25 August 2026 (formerly Kerala)", "केरलम, 25 अगस्त 2026 से लागू (पूर्व नाम केरल)", "केरळम, 25 ऑगस्ट 2026 पासून लागू (पूर्वीचे नाव केरळ)")],
           [L("Districts", "ज़िले", "जिल्हे"), "14"],
           [L("Official language", "राजभाषा", "राजभाषा"), L("Malayalam (classical language status, 2013)", "मलयालम (2013 में शास्त्रीय भाषा का दर्जा)", "मल्याळम (2013 मध्ये अभिजात भाषेचा दर्जा)")],
           [L("ISO 3166-2 / vehicle code", "आईएसओ 3166-2 / वाहन कोड", "आयएसओ 3166-2 / वाहन संकेतांक"), "IN-KL / KL"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          "kl-spb", KL_SPB, conf="Editorial",
          note=L("District count from the Kerala State Planning Board's Economic Review. The ISO 3166-2 code IN-KL is unchanged by the renaming. Other rows are editorial and will each be linked to a notification in review.",
                 "ज़िलों की संख्या केरल राज्य योजना बोर्ड की आर्थिक समीक्षा से। नाम बदलने से आईएसओ 3166-2 कोड IN-KL नहीं बदला है। बाकी पंक्तियाँ संपादकीय हैं; समीक्षा में हर एक को अधिसूचना से जोड़ा जाएगा।",
                 "जिल्ह्यांची संख्या केरळ राज्य नियोजन मंडळाच्या आर्थिक आढाव्यातून. नावबदलामुळे आयएसओ 3166-2 संकेत IN-KL बदललेला नाही. इतर ओळी संपादकीय असून तपासणीदरम्यान प्रत्येकीला अधिसूचनेचा दुवा जोडला जाईल.")),
    lst("rename", [
        it3("res", "Assembly resolution", "विधानसभा का प्रस्ताव", "विधानसभेचा ठराव", m=("June 2024", "जून 2024", "जून 2024"),
            d=("The Kerala Legislative Assembly asked the Union to change the name in the Constitution.", "केरल विधानसभा ने संविधान में नाम बदलने का अनुरोध केंद्र से किया।", "केरळ विधानसभेने राज्यघटनेतील नाव बदलण्याची विनंती केंद्राकडे केली."),
            url=PRS, src="prs"),
        it3("ls", "Bill introduced and passed in the Lok Sabha", "लोकसभा में विधेयक पेश और पारित", "लोकसभेत विधेयक सादर व मंजूर", m=("10 and 11 August 2026", "10 और 11 अगस्त 2026", "10 व 11 ऑगस्ट 2026"), url=PRS, src="prs"),
        it3("rs", "Passed by the Rajya Sabha", "राज्यसभा से पारित", "राज्यसभेत मंजूर", m=("12 August 2026", "12 अगस्त 2026", "12 ऑगस्ट 2026"), url=PRS, src="prs"),
        it3("force", "New name in force (MHA notification)", "नया नाम लागू (गृह मंत्रालय की अधिसूचना)", "नवे नाव लागू (गृह मंत्रालयाची अधिसूचना)", m=("25 August 2026", "25 अगस्त 2026", "25 ऑगस्ट 2026"),
            d=("Reported by Onmanorama; link to the Gazette of India pending.", "ओणमनोरमा की रिपोर्ट के अनुसार; भारत के राजपत्र का लिंक जोड़ा जाना बाकी।", "ओणमनोरमाच्या वृत्तानुसार; भारताच्या राजपत्राचा दुवा जोडणे बाकी."),
            url=ONM, src="onmanorama"),
    ], layout="bullets", title=L("From Kerala to Keralam", "केरल से केरलम तक", "केरळ ते केरळम"), src="prs", url=PRS, conf="Official", access=TODAY),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Keralam is long and thin: roughly 550 km from north to south but never much more than about 120 km wide. It falls into three natural belts running parallel to the coast. The lowland is a sandy coastal strip with lagoons, estuaries and the backwaters — a linked network of lakes and canals, of which Vembanad is the largest. The midland is rolling laterite country of rice paddies, coconut, rubber and spice gardens. The highland is the Western Ghats, rising to Anamudi in the Idukki hills, the highest peak in peninsular India.\n\nMore than forty short, fast rivers rise in the Ghats; most flow west to the sea, and a few flow east into Tamil Nadu and Karnataka. The Periyar is the longest and feeds the Idukki reservoir. The Palakkad Gap, a broad break in the Ghats, has long been the main land route to Tamil Nadu and funnels dry winds into the plains around it.",
        "केरलम लंबा और पतला है: उत्तर से दक्षिण लगभग 550 किमी, लेकिन चौड़ाई कहीं भी लगभग 120 किमी से अधिक नहीं। यह तट के समानांतर तीन प्राकृतिक पट्टियों में बँटा है। निचली पट्टी रेतीला तटीय क्षेत्र है, जिसमें लैगून, मुहाने और बैकवाटर हैं — झीलों और नहरों का जुड़ा हुआ जाल, जिसमें वेम्बनाड सबसे बड़ी झील है। मध्य पट्टी लैटेराइट की लहरदार भूमि है, जहाँ धान, नारियल, रबर और मसालों के बाग़ हैं। ऊँची पट्टी पश्चिमी घाट है, जो इडुक्की की पहाड़ियों में आनामुडी तक उठती है — प्रायद्वीपीय भारत की सबसे ऊँची चोटी।\n\nघाट से चालीस से अधिक छोटी, तेज़ नदियाँ निकलती हैं; अधिकांश पश्चिम में समुद्र की ओर बहती हैं और कुछ पूर्व में तमिलनाडु व कर्नाटक की ओर। पेरियार सबसे लंबी नदी है और इडुक्की जलाशय को भरती है। घाट में एक चौड़ा दर्रा, पालक्काड गैप, लंबे समय से तमिलनाडु जाने का मुख्य थल मार्ग रहा है और आसपास के मैदानों में सूखी हवाएँ लाता है।",
        "केरळम लांब आणि अरुंद आहे: उत्तर-दक्षिण सुमारे 550 किमी, पण रुंदी कुठेही सुमारे 120 किमीपेक्षा फारशी जास्त नाही. किनाऱ्याला समांतर असे तीन नैसर्गिक पट्टे आहेत. सखल पट्टा वाळूचा किनारी भाग असून त्यात खारकच्छ, नदीमुखे आणि बॅकवॉटर्स आहेत — सरोवरे आणि कालव्यांचे जोडलेले जाळे, ज्यात वेंबनाड हे सर्वांत मोठे सरोवर आहे. मधला पट्टा जांभ्या दगडाचा उंच-सखल प्रदेश असून तिथे भातखाचरे, नारळ, रबर आणि मसाल्यांच्या बागा आहेत. उंच पट्टा म्हणजे पश्चिम घाट, जो इडुक्कीच्या डोंगररांगांत आनामुडीपर्यंत चढतो — द्वीपकल्पीय भारतातील सर्वोच्च शिखर.\n\nघाटात चाळीसहून अधिक लहान, वेगवान नद्या उगम पावतात; बहुतेक पश्चिमेकडे समुद्राला मिळतात आणि काही पूर्वेकडे तमिळनाडू व कर्नाटकात जातात. पेरियार ही सर्वांत लांब नदी असून ती इडुक्की जलाशयाला पाणी पुरवते. घाटातील रुंद खिंड, पालक्काड गॅप, हा फार पूर्वीपासून तमिळनाडूकडे जाणारा मुख्य भूमार्ग आहे आणि त्यातून आसपासच्या मैदानात कोरडे वारे येतात."),
        conf="Editorial"),
    facts("f", [
        fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), kl["area"], "number", national=ind["area"]),
    ]),
    lst("neighbours", [
        it3("ka", "Karnataka (north)", "कर्नाटक (उत्तर)", "कर्नाटक (उत्तर)"), it3("tn", "Tamil Nadu (east)", "तमिलनाडु (पूर्व)", "तमिळनाडू (पूर्व)"),
        it3("py", "Puducherry (Mahe enclave)", "पुदुच्चेरी (माहे अंतःक्षेत्र)", "पुदुच्चेरी (माहे परिक्षेत्र)"),
        it3("sea", "Arabian Sea (west)", "अरब सागर (पश्चिम)", "अरबी समुद्र (पश्चिम)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("periyar", "Periyar", "पेरियार", "पेरियार", d=("Longest river; feeds the Idukki and Mullaperiyar reservoirs and reaches the sea near Kochi.", "सबसे लंबी नदी; इडुक्की और मुल्लपेरियार जलाशयों को भरती है और कोच्चि के पास समुद्र में मिलती है।", "सर्वांत लांब नदी; इडुक्की आणि मुल्लपेरियार जलाशयांना पाणी देते आणि कोचीजवळ समुद्राला मिळते.")),
        it3("bharathapuzha", "Bharathapuzha (Nila)", "भारतपुझा (निला)", "भारतपुझा (निळा)", d=("Flows west through the Palakkad Gap; closely tied to Malayalam literature and the arts.", "पालक्काड गैप से पश्चिम की ओर बहती है; मलयालम साहित्य और कलाओं से गहराई से जुड़ी।", "पालक्काड गॅपमधून पश्चिमेकडे वाहते; मल्याळम साहित्य व कलांशी घट्ट नाते.")),
        it3("pamba", "Pamba", "पंबा", "पंबा", d=("Flows past Sabarimala and Aranmula into Vembanad Lake.", "सबरीमला और आरनमुला से होकर वेम्बनाड झील में मिलती है।", "शबरीमला व आरनमुळा जवळून वाहत वेंबनाड सरोवरात मिळते.")),
        it3("chaliyar", "Chaliyar", "चालियार", "चालियार", d=("Northern river reaching the sea near Kozhikode; Nilambur's teak forests lie in its basin.", "उत्तरी नदी, जो कोझिकोड के पास समुद्र में मिलती है; निलांबुर के सागौन वन इसी घाटी में हैं।", "कोझिकोडजवळ समुद्राला मिळणारी उत्तरेकडील नदी; निलांबूरची सागवने याच खोऱ्यात आहेत.")),
        it3("kabini", "Kabini", "काबिनी", "काबिनी", d=("One of the few east-flowing rivers; rises in Wayanad and joins the Kaveri in Karnataka.", "पूर्व की ओर बहने वाली गिनी-चुनी नदियों में; वायनाड से निकलकर कर्नाटक में कावेरी से मिलती है।", "पूर्वेकडे वाहणाऱ्या मोजक्या नद्यांपैकी एक; वायनाडमध्ये उगम पावून कर्नाटकात कावेरीला मिळते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Official coastline length and highest-point elevation", "आधिकारिक तटरेखा लंबाई और सर्वोच्च बिंदु की ऊँचाई", "अधिकृत किनारपट्टी लांबी व सर्वोच्च बिंदूची उंची"), "survey-of-india", "Editorial text avoids exact figures until an official one is linked."),
        (L("Number of rivers (official list)", "नदियों की संख्या (आधिकारिक सूची)", "नद्यांची संख्या (अधिकृत यादी)"), "kl-spb", "Water Resources Department list."),
        (L("Seismic zones (latest BIS map)", "भूकंपीय क्षेत्र (नवीनतम बीआईएस मानचित्र)", "भूकंप क्षेत्र (नवीनतम बीआयएस नकाशा)"), "bis", "Use the current revision of IS 1893 (Part 1)."),
        (L("Latitude and longitude extent", "अक्षांश-देशांतर विस्तार", "अक्षांश-रेखांश विस्तार"), "survey-of-india", "Survey of India or the State gazetteer."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Keralam has a humid tropical climate with little seasonal change in temperature, but rainfall dominates the calendar. The south-west monsoon usually reaches the Indian mainland here first, around the start of June, and brings most of the year's rain by September. A second, smaller season of rain — the north-east monsoon, locally called Thulavarsham — follows in October and November. December to February is the driest and most comfortable stretch; March to May is hot and sticky, broken by pre-monsoon thunderstorms.\n\nThe hills are much cooler. Munnar, Wayanad and the Idukki highlands can be chilly on winter nights, while the coast stays warm all year.",
        "केरलम की जलवायु आर्द्र उष्णकटिबंधीय है; तापमान में मौसमी बदलाव कम है, लेकिन साल का कैलेंडर वर्षा तय करती है। दक्षिण-पश्चिम मानसून आम तौर पर भारत की मुख्य भूमि पर सबसे पहले यहीं, जून की शुरुआत के आसपास पहुँचता है और सितंबर तक साल की अधिकांश वर्षा दे जाता है। इसके बाद अक्टूबर और नवंबर में दूसरा, छोटा वर्षा काल आता है — उत्तर-पूर्व मानसून, जिसे यहाँ तुलावर्षम कहते हैं। दिसंबर से फ़रवरी सबसे सूखा और सुहावना समय है; मार्च से मई गर्म और उमस भरा रहता है, बीच-बीच में मानसून-पूर्व आँधी-बारिश होती है।\n\nपहाड़ियाँ काफ़ी ठंडी हैं। मुन्नार, वायनाड और इडुक्की के ऊँचे इलाक़ों में सर्दियों की रातें ठिठुरन भरी हो सकती हैं, जबकि तट साल भर गर्म रहता है।",
        "केरळमचे हवामान दमट उष्णकटिबंधीय आहे; तापमानात ऋतूनुसार फारसा फरक पडत नाही, पण वर्षाचे वेळापत्रक पाऊस ठरवतो. नैर्ऋत्य मोसमी पाऊस साधारणपणे जूनच्या सुरुवातीला भारताच्या मुख्य भूमीवर सर्वप्रथम इथेच दाखल होतो आणि सप्टेंबरपर्यंत वर्षभराचा बहुतांश पाऊस देतो. त्यानंतर ऑक्टोबर-नोव्हेंबरमध्ये दुसरा, लहान पावसाळा येतो — ईशान्य मोसमी पाऊस, ज्याला स्थानिक भाषेत तुलावर्षम म्हणतात. डिसेंबर ते फेब्रुवारी हा सर्वांत कोरडा आणि आल्हाददायक काळ; मार्च ते मे उष्ण व दमट असतो, अधूनमधून मान्सूनपूर्व वादळी पाऊस पडतो.\n\nडोंगराळ भाग बराच थंड असतो. मुन्नार, वायनाड आणि इडुक्कीच्या उंच भागात हिवाळ्यातील रात्री गारठा जाणवतो, तर किनारपट्टी वर्षभर उबदार राहते."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Thiruvananthapuram", "तिरुवनंतपुरम", "तिरुवनंतपुरम"), "lat": 8.5241, "lon": 76.9366},
        {"name": L("Kochi", "कोच्चि", "कोची"), "lat": 9.9312, "lon": 76.2673},
        {"name": L("Kozhikode", "कोझिकोड", "कोझिकोड"), "lat": 11.2588, "lon": 75.7804},
        {"name": L("Munnar", "मुन्नार", "मुन्नार"), "lat": 10.0889, "lon": 77.0595},
    ]},
    lst("best", [
        it3("winter", "December to February", "दिसंबर से फ़रवरी", "डिसेंबर ते फेब्रुवारी", d=("Driest and most comfortable: backwaters, beaches, hill stations and festivals.", "सबसे सूखा और सुहावना: बैकवाटर, समुद्र तट, हिल स्टेशन और उत्सव।", "सर्वांत कोरडा आणि आल्हाददायक: बॅकवॉटर्स, समुद्रकिनारे, थंड हवेची ठिकाणे आणि उत्सव.")),
        it3("monsoon", "June to September", "जून से सितंबर", "जून ते सप्टेंबर", d=("Green and dramatic; season for Ayurveda treatments and the August boat races, with flood and landslide risk.", "हरियाली और नाटकीय नज़ारे; आयुर्वेदिक उपचार और अगस्त की नौका दौड़ का मौसम, पर बाढ़ और भूस्खलन का ख़तरा।", "हिरवाई आणि नाट्यमय निसर्ग; आयुर्वेदिक उपचार आणि ऑगस्टमधील नौका शर्यतींचा काळ, मात्र पूर व दरडींचा धोका.")),
        it3("onam", "August–September (Onam)", "अगस्त–सितंबर (ओणम)", "ऑगस्ट–सप्टेंबर (ओणम)", d=("Harvest festival season with flower carpets, feasts and cultural events.", "फूलों की रंगोली, भोज और सांस्कृतिक कार्यक्रमों वाला फ़सल उत्सव का मौसम।", "फुलांच्या रांगोळ्या, मेजवान्या आणि सांस्कृतिक कार्यक्रमांचा सुगीचा सणासुदीचा काळ.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Monthly temperature and rainfall normals", "मासिक तापमान और वर्षा सामान्य", "मासिक तापमान व पर्जन्य सरासरी"), "imd", "IMD climatological normals for Thiruvananthapuram, Kochi, Kozhikode."),
        (L("Annual rainfall (State average)", "वार्षिक वर्षा (राज्य औसत)", "वार्षिक पर्जन्य (राज्य सरासरी)"), "imd", "IMD rainfall statistics."),
        (L("Climate-change vulnerability", "जलवायु परिवर्तन संवेदनशीलता", "हवामान बदल असुरक्षितता"), "ndma", "Kerala State Action Plan on Climate Change."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Days in Keralam start early, with temple loudspeakers, church bells and the azaan overlapping in the half-light, and the smell of filter coffee and steaming puttu from a tea shop. Newspapers are read closely — on buses, at the barber, outside the reading room — and conversations about politics and football run long. Along the backwaters, life moves at the speed of a country boat: ducks herded across paddy canals, toddy shops on the bank, a kettuvallam drifting past coconut palms. Kochi feels cosmopolitan and layered, with Chinese fishing nets at Fort Kochi, old warehouses turned into galleries and a busy metro. In the hills the air smells of tea and cardamom and the mist rolls in by afternoon. Then the festivals arrive and everything gets loud: chenda drums, elephants in gold caparisons, fireworks at Thrissur Pooram, and the floral pookkalam at every doorstep during Onam.",
        "केरलम में दिन जल्दी शुरू होता है — धुँधली रोशनी में मंदिर के लाउडस्पीकर, चर्च की घंटियाँ और अज़ान एक साथ सुनाई देते हैं, और चाय की दुकान से फ़िल्टर कॉफ़ी और भाप में बने पुट्टु की ख़ुशबू आती है। अख़बार ध्यान से पढ़े जाते हैं — बस में, नाई की दुकान पर, वाचनालय के बाहर — और राजनीति व फ़ुटबॉल पर बहसें लंबी चलती हैं। बैकवाटर के किनारे ज़िंदगी देसी नाव की रफ़्तार से चलती है: धान की नहरों में बत्तखों के झुंड, किनारे पर ताड़ी की दुकानें, और नारियल के पेड़ों के बीच से धीरे-धीरे गुज़रता केट्टुवल्लम। कोच्चि में महानगरीय और परतदार अनुभव है — फ़ोर्ट कोच्चि के चीनी मछली जाल, गैलरी में बदले पुराने गोदाम और व्यस्त मेट्रो। पहाड़ियों की हवा में चाय और इलायची की गंध है और दोपहर तक धुंध छा जाती है। फिर उत्सव आते हैं और सब कुछ गूँज उठता है: चेंडा ढोल, सुनहरे नेट्टिपट्टम में सजे हाथी, त्रिशूर पूरम की आतिशबाज़ी, और ओणम में हर दरवाज़े पर फूलों का पूक्कलम।",
        "केरळममध्ये दिवस लवकर सुरू होतो — पहाटेच्या अंधुक उजेडात देवळाचे ध्वनिक्षेपक, चर्चच्या घंटा आणि अजान एकाच वेळी कानावर पडतात, आणि चहाच्या टपरीतून फिल्टर कॉफी व वाफवलेल्या पुट्टूचा दरवळ येतो. वर्तमानपत्रे बारकाईने वाचली जातात — बसमध्ये, केशकर्तनालयात, वाचनालयाबाहेर — आणि राजकारण व फुटबॉलवरच्या गप्पा लांबत जातात. बॅकवॉटर्सच्या काठी आयुष्य देशी होडीच्या वेगाने चालते: भातखाचरांच्या कालव्यांतून हाकलले जाणारे बदकांचे थवे, काठावर ताडीची दुकाने, आणि नारळीच्या झाडांमधून हळूच सरकणारा केट्टुवल्लम. कोचीत बहुसांस्कृतिक, अनेक थरांचा अनुभव येतो — फोर्ट कोचीची चिनी मासेमारी जाळी, कलादालनांत रूपांतरित जुनी गोदामे आणि गजबजलेली मेट्रो. डोंगरांत हवेला चहा-वेलचीचा सुगंध असतो आणि दुपारपर्यंत धुके दाटते. मग उत्सव येतात आणि सगळे दुमदुमून जाते: चेंडा वाद्याचा नाद, सोनेरी नेट्टिपट्टम घातलेले हत्ती, त्रिशूर पूरमची आतषबाजी, आणि ओणमला प्रत्येक दारात फुलांची पूक्कळम रांगोळी."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "At the 2011 Census, Keralam had 3.34 crore people. Its population grew by only 4.9% in the decade to 2011, one of the slowest rates of any State, reflecting low fertility and heavy emigration. It had 1,084 women for every 1,000 men, the highest sex ratio of any State, and an effective literacy rate of about 94%. Nearly half the population (47.7%) was classed as urban, though towns and villages merge into one another along the coast, giving the State a distinctive \"rurban\" settlement pattern.\n\nMalayalam is the official language and the mother tongue of the great majority. Tamil is spoken along the eastern border and in Thiruvananthapuram and Palakkad; Kannada and Tulu in Kasaragod. Keralam is also home to one of India's oldest Christian communities, a large Muslim population concentrated in Malabar, and a historic Jewish community in Kochi.",
        "2011 की जनगणना में केरलम की जनसंख्या 3.34 करोड़ थी। 2011 तक के दशक में जनसंख्या केवल 4.9% बढ़ी, जो राज्यों में सबसे धीमी दरों में से एक थी; इसके पीछे कम प्रजनन दर और बड़े पैमाने पर विदेश प्रवास है। यहाँ प्रति 1,000 पुरुषों पर 1,084 महिलाएँ थीं — किसी भी राज्य में सबसे अधिक लिंगानुपात — और प्रभावी साक्षरता दर लगभग 94% थी। लगभग आधी आबादी (47.7%) शहरी मानी गई, हालाँकि तट के साथ कस्बे और गाँव एक-दूसरे में घुल-मिल जाते हैं, जिससे राज्य का बसावट पैटर्न \"ग्रामीण-शहरी\" जैसा अनोखा है।\n\nमलयालम राजभाषा है और अधिकांश लोगों की मातृभाषा। पूर्वी सीमा पर तथा तिरुवनंतपुरम और पालक्काड में तमिल, और कासरगोड में कन्नड़ व तुलु बोली जाती है। केरलम भारत के सबसे पुराने ईसाई समुदायों में से एक, मलबार में केंद्रित बड़ी मुस्लिम आबादी और कोच्चि के ऐतिहासिक यहूदी समुदाय का भी घर है।",
        "2011 च्या जनगणनेनुसार केरळमची लोकसंख्या 3.34 कोटी होती. 2011 पर्यंतच्या दशकात लोकसंख्या केवळ 4.9% ने वाढली — राज्यांमधील सर्वांत कमी दरांपैकी एक — कारण जननदर कमी आहे आणि परदेशी स्थलांतर मोठ्या प्रमाणात होते. दर 1,000 पुरुषांमागे 1,084 स्त्रिया होत्या, हे सर्व राज्यांत सर्वाधिक लिंग गुणोत्तर, आणि प्रभावी साक्षरता सुमारे 94% होती. जवळपास निम्मी लोकसंख्या (47.7%) नागरी गणली गेली; मात्र किनाऱ्यालगत गावे आणि शहरे एकमेकांत मिसळून जातात, त्यामुळे राज्याची वस्तीरचना \"ग्रामीण-नागरी\" अशी वेगळी आहे.\n\nमल्याळम ही राजभाषा आणि बहुसंख्य लोकांची मातृभाषा आहे. पूर्व सीमेवर तसेच तिरुवनंतपुरम व पालक्काडमध्ये तमिळ, तर कासारगोडमध्ये कन्नड व तुळू बोलली जाते. भारतातील सर्वांत जुन्या ख्रिस्ती समुदायांपैकी एक, मलबारमध्ये एकवटलेली मोठी मुस्लिम लोकसंख्या आणि कोचीतील ऐतिहासिक ज्यू समुदाय यांचेही केरळम हे घर आहे."),
        sources=["kl-spb"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), kl["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), kl["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"]),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), kl["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(960, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), kl["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("urb", L("Urban population", "शहरी जनसंख्या", "नागरी लोकसंख्या"), kl["urbanisation2011"], "percent", national=ind["urbanisation2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), kl["density2011"], "number"),
        fact("growth", L("Decadal growth, 2001–2011", "दशकीय वृद्धि, 2001–2011", "दशकातील वाढ, 2001–2011"),
             dp(4.9, "%", "2011", "census", "census", KL_SPB, note="Kerala State Planning Board, Economic Review."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("ml", "Malayalam", "मलयालम", "मल्याळम", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("ta", "Tamil", "तमिल", "तमिळ", m=("Eastern border, Thiruvananthapuram, Palakkad", "पूर्वी सीमा, तिरुवनंतपुरम, पालक्काड", "पूर्व सीमा, तिरुवनंतपुरम, पालक्काड")),
        it3("kn", "Kannada", "कन्नड़", "कन्नड", m=("Kasaragod", "कासरगोड", "कासारगोड")),
        it3("tcy", "Tulu", "तुलु", "तुळू", m=("Kasaragod", "कासरगोड", "कासारगोड")),
        it3("kok", "Konkani", "कोंकणी", "कोकणी", m=("Kochi and coastal towns", "कोच्चि और तटीय कस्बे", "कोची व किनारी गावे")),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
        (L("SC and ST shares", "अनुसूचित जाति और जनजाति का हिस्सा", "अनुसूचित जाती व जमातींचा वाटा"), "census", "Census 2011 PCA; earlier source link was not retrievable at access time."),
        (L("Literacy by sex", "लिंगवार साक्षरता", "लिंगनिहाय साक्षरता"), "census", "Census 2011 PCA."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projections; label as Projected."),
        (L("Mother-tongue shares (Census C-16)", "मातृभाषावार हिस्सा (जनगणना C-16)", "मातृभाषानिहाय वाटा (जनगणना C-16)"), "census", "Census C-16."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "Keralam's coast has traded with the wider world for over two thousand years. Muziris, near today's Kodungallur, shipped pepper to Roman and West Asian merchants in the early centuries CE, when the Cheras ruled much of the region. Christianity, Judaism and Islam arrived early by sea, and the later Chera (Kulasekhara) kingdom of Mahodayapuram gave way to smaller principalities — Venad (later Travancore), Kochi, and the Zamorin's Kozhikode.\n\nVasco da Gama landed near Kozhikode in 1498, beginning centuries of Portuguese, Dutch and British competition for the spice trade. In the 18th century Marthanda Varma built Travancore into a strong state and defeated the Dutch at Colachel in 1741. Malabar passed to the British after the Mysore wars, while Travancore and Kochi remained princely states.\n\nThe late 19th and 20th centuries brought powerful social reform movements led by Sree Narayana Guru, Ayyankali, Chattampi Swamikal and others, along with the Vaikom Satyagraha (1924–25) and the Temple Entry Proclamation (1936). Travancore and Kochi merged in 1949; Keralam was formed in 1956, and in 1957 elected one of the world's first communist governments through the ballot box. The State has since been known for land reform, mass literacy and public health — and for some of India's worst recent floods, in 2018.",
        "केरलम का तट दो हज़ार वर्षों से भी अधिक समय से दुनिया से व्यापार करता रहा है। आज के कोडुंगल्लूर के पास स्थित मुज़िरिस से ईसवी सन् की शुरुआती सदियों में रोमन और पश्चिम एशियाई व्यापारियों को काली मिर्च भेजी जाती थी; तब इस क्षेत्र के बड़े हिस्से पर चेरों का शासन था। ईसाई, यहूदी और इस्लाम धर्म समुद्र के रास्ते जल्दी पहुँचे, और बाद का महोदयपुरम का चेर (कुलशेखर) राज्य छोटी रियासतों में बँट गया — वेणाड (बाद में त्रावणकोर), कोच्चि और ज़मोरिन का कोझिकोड।\n\n1498 में वास्को डी गामा कोझिकोड के पास उतरा और मसाला व्यापार के लिए पुर्तगालियों, डचों और अंग्रेज़ों की सदियों लंबी होड़ शुरू हुई। 18वीं सदी में मार्तंड वर्मा ने त्रावणकोर को मज़बूत राज्य बनाया और 1741 में कोलाचेल में डचों को हराया। मैसूर युद्धों के बाद मलबार अंग्रेज़ों के अधीन चला गया, जबकि त्रावणकोर और कोच्चि रियासतें बनी रहीं।\n\n19वीं सदी के अंत और 20वीं सदी में श्री नारायण गुरु, अय्यंकाली, चट्टंपी स्वामिकल और अन्य लोगों के नेतृत्व में शक्तिशाली समाज सुधार आंदोलन हुए, साथ ही वैकम सत्याग्रह (1924–25) और मंदिर प्रवेश उद्घोषणा (1936) भी। 1949 में त्रावणकोर और कोच्चि का विलय हुआ; 1956 में केरलम बना, और 1957 में यहाँ मतपेटी के ज़रिए दुनिया की पहली कम्युनिस्ट सरकारों में से एक चुनी गई। तब से राज्य भूमि सुधार, जन साक्षरता और सार्वजनिक स्वास्थ्य के लिए जाना जाता है — और 2018 में आई हाल के वर्षों की भारत की सबसे भीषण बाढ़ों में से एक के लिए भी।",
        "केरळमचा किनारा दोन हजार वर्षांहून अधिक काळ जगाशी व्यापार करत आला आहे. आजच्या कोडुंगल्लूरजवळील मुझिरिस बंदरातून इसवी सनाच्या सुरुवातीच्या शतकांत रोमन व पश्चिम आशियाई व्यापाऱ्यांना मिरी पाठवली जात असे; तेव्हा या प्रदेशाच्या मोठ्या भागावर चेरांचे राज्य होते. ख्रिस्ती, ज्यू आणि इस्लाम धर्म सागरी मार्गाने लवकरच पोहोचले, आणि नंतरचे महोदयपुरमचे चेर (कुलशेखर) राज्य लहान संस्थानांत विभागले गेले — वेणाड (पुढे त्रावणकोर), कोची आणि झामोरिनचे कोझिकोड.\n\n1498 मध्ये वास्को द गामा कोझिकोडजवळ उतरला आणि मसाल्यांच्या व्यापारासाठी पोर्तुगीज, डच आणि ब्रिटिशांची शतकानुशतकांची स्पर्धा सुरू झाली. अठराव्या शतकात मार्तंड वर्मा यांनी त्रावणकोरला बलवान राज्य बनवले आणि 1741 मध्ये कोलाचेल येथे डचांचा पराभव केला. म्हैसूर युद्धांनंतर मलबार ब्रिटिशांकडे गेले, तर त्रावणकोर आणि कोची संस्थाने राहिली.\n\nएकोणिसाव्या शतकाच्या अखेरीस आणि विसाव्या शतकात श्री नारायण गुरू, अय्यंकाळी, चट्टंपी स्वामिकळ आणि इतरांच्या नेतृत्वाखाली प्रभावी समाजसुधारणा चळवळी झाल्या; वैकम सत्याग्रह (1924–25) आणि मंदिरप्रवेश घोषणा (1936) हेही याच काळातले. 1949 मध्ये त्रावणकोर आणि कोची यांचे विलीनीकरण झाले; 1956 मध्ये केरळम राज्य बनले आणि 1957 मध्ये मतपेटीद्वारे जगातील पहिल्या कम्युनिस्ट सरकारांपैकी एक येथे निवडून आले. तेव्हापासून राज्य जमीन सुधारणा, सार्वत्रिक साक्षरता आणि सार्वजनिक आरोग्यासाठी ओळखले जाते — तसेच 2018 मधील अलीकडच्या काळातील भारतातील सर्वांत भीषण पुरांपैकी एकासाठीही."),
        conf="Editorial"),
    timeline([
        ev("muziris", 100, L("c. 1st century CE", "लगभग पहली सदी ईसवी", "सुमारे इ.स. पहिले शतक"), L("Muziris trades pepper with Rome and West Asia", "मुज़िरिस से रोम और पश्चिम एशिया के साथ काली मिर्च का व्यापार", "मुझिरिसमधून रोम व पश्चिम आशियाशी मिरीचा व्यापार")),
        ev("kulasekhara", 800, L("9th century", "9वीं सदी", "नववे शतक"), L("Chera (Kulasekhara) kingdom of Mahodayapuram", "महोदयपुरम का चेर (कुलशेखर) राज्य", "महोदयपुरमचे चेर (कुलशेखर) राज्य")),
        ev("gama", 1498, L("1498", "1498", "1498"), L("Vasco da Gama lands near Kozhikode", "वास्को डी गामा कोझिकोड के पास उतरा", "वास्को द गामा कोझिकोडजवळ उतरला")),
        ev("dutch", 1663, L("1663", "1663", "1663"), L("Dutch take Kochi from the Portuguese", "डचों ने पुर्तगालियों से कोच्चि छीना", "डचांनी पोर्तुगीजांकडून कोची घेतले")),
        ev("colachel", 1741, L("1741", "1741", "1741"), L("Travancore defeats the Dutch at Colachel", "कोलाचेल में त्रावणकोर ने डचों को हराया", "कोलाचेल येथे त्रावणकोरने डचांचा पराभव केला")),
        ev("malabar", 1792, L("1792", "1792", "1792"), L("Malabar ceded to the British after the Third Anglo-Mysore War", "तीसरे आंग्ल-मैसूर युद्ध के बाद मलबार अंग्रेज़ों को सौंपा गया", "तिसऱ्या इंग्रज-म्हैसूर युद्धानंतर मलबार ब्रिटिशांकडे")),
        ev("aruvippuram", 1888, L("1888", "1888", "1888"), L("Sree Narayana Guru consecrates the Aruvippuram temple", "श्री नारायण गुरु ने अरुविप्पुरम में मंदिर प्रतिष्ठा की", "श्री नारायण गुरूंनी अरुविप्पुरम येथे मंदिराची प्रतिष्ठापना केली")),
        ev("vaikom", 1924, L("1924–25", "1924–25", "1924–25"), L("Vaikom Satyagraha for access to temple roads", "मंदिर के रास्तों पर आवाजाही के लिए वैकम सत्याग्रह", "मंदिराच्या रस्त्यांवरील प्रवेशासाठी वैकम सत्याग्रह")),
        ev("entry", 1936, L("1936", "1936", "1936"), L("Temple Entry Proclamation in Travancore", "त्रावणकोर में मंदिर प्रवेश उद्घोषणा", "त्रावणकोरमध्ये मंदिरप्रवेश घोषणा")),
        ev("tc", 1949, L("1949", "1949", "1949"), L("Travancore and Kochi merge as Travancore-Cochin", "त्रावणकोर और कोच्चि का विलय होकर त्रावणकोर-कोचीन बना", "त्रावणकोर व कोची यांचे विलीनीकरण होऊन त्रावणकोर-कोचीन")),
        ev("formation", 1956, L("1 November 1956", "1 नवंबर 1956", "1 नोव्हेंबर 1956"), L("State formed under the States Reorganisation Act", "राज्य पुनर्गठन अधिनियम के तहत राज्य बना", "राज्य पुनर्रचना कायद्यानुसार राज्याची स्थापना")),
        ev("ems", 1957, L("1957", "1957", "1957"), L("First elected State government takes office", "पहली निर्वाचित राज्य सरकार ने पदभार सँभाला", "पहिले निर्वाचित राज्य सरकार सत्तेवर")),
        ev("floods", 2018, L("August 2018", "अगस्त 2018", "ऑगस्ट 2018"), L("Severe monsoon floods across the State", "पूरे राज्य में भीषण मानसूनी बाढ़", "राज्यभर भीषण मोसमी पूर")),
        ev("keralam", 2026, L("25 August 2026", "25 अगस्त 2026", "25 ऑगस्ट 2026"), L("Name changed to Keralam", "नाम बदलकर केरलम हुआ", "नाव बदलून केरळम")),
    ]),
    lst("heritage", [
        it3("wg", "Western Ghats (natural World Heritage, serial)", "पश्चिमी घाट (प्राकृतिक विश्व धरोहर, शृंखला)", "पश्चिम घाट (नैसर्गिक जागतिक वारसा, मालिका)", m=("UNESCO 2012", "यूनेस्को 2012", "युनेस्को 2012"), url=UNESCO, src="unesco-whc"),
        it3("kutiyattam", "Kutiyattam, Sanskrit theatre", "कूडियाट्टम, संस्कृत रंगमंच", "कूडियाट्टम, संस्कृत रंगभूमी", m=("UNESCO intangible heritage", "यूनेस्को अमूर्त धरोहर", "युनेस्को अमूर्त वारसा")),
        it3("mudiyettu", "Mudiyettu, ritual theatre and dance drama", "मुडियेट्टु, अनुष्ठानिक रंगमंच और नृत्य-नाटिका", "मुडियेट्टू, विधीनाट्य व नृत्यनाट्य", m=("UNESCO intangible heritage", "यूनेस्को अमूर्त धरोहर", "युनेस्को अमूर्त वारसा")),
        it3("muziris", "Muziris Heritage Project (Kodungallur–North Paravur)", "मुज़िरिस धरोहर परियोजना (कोडुंगल्लूर–उत्तर परवूर)", "मुझिरिस वारसा प्रकल्प (कोडुंगल्लूर–उत्तर परवूर)", m=("Archaeology and museums", "पुरातत्व और संग्रहालय", "पुरातत्त्व व संग्रहालये")),
        it3("padmanabhapuram", "Padmanabhapuram Palace", "पद्मनाभपुरम महल", "पद्मनाभपुरम राजवाडा", m=("Travancore-era wooden palace (in Tamil Nadu, maintained by Keralam)", "त्रावणकोर कालीन लकड़ी का महल (तमिलनाडु में, केरलम द्वारा संरक्षित)", "त्रावणकोरकालीन लाकडी राजवाडा (तमिळनाडूत, केरळमकडून देखभाल)")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])
print("kl mod1 ok")
