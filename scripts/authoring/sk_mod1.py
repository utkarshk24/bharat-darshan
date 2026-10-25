"""Sikkim modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-SK"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
sk = read("regions/IN-SK.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Sikkim is a small Himalayan State in the north-east, wedged between Nepal to the west, the Tibet region of China to the north and east, Bhutan to the south-east and West Bengal to the south. It is India's least populous State, with 6.1 lakh people at the 2011 Census, and the second smallest by area after Goa. Within about 100 km it rises from subtropical valleys of the Teesta at a few hundred metres to Kangchenjunga, India's highest peak. Gangtok is the capital.\n\nSikkim was a kingdom ruled by the Namgyal dynasty (the Chogyals) for more than three centuries, a British protectorate and then an Indian protectorate, until it became India's 22nd State on 16 May 1975. It is known for its Buddhist monasteries, its mix of Lepcha, Bhutia and Nepali communities, and for being the first State in India to farm entirely organically.",
        "सिक्किम उत्तर-पूर्व का एक छोटा हिमालयी राज्य है, जो पश्चिम में नेपाल, उत्तर और पूर्व में चीन के तिब्बत क्षेत्र, दक्षिण-पूर्व में भूटान और दक्षिण में पश्चिम बंगाल के बीच स्थित है। 2011 की जनगणना में 6.1 लाख लोगों के साथ यह भारत का सबसे कम आबादी वाला राज्य है, और क्षेत्रफल में गोवा के बाद दूसरा सबसे छोटा। लगभग 100 किमी के भीतर यह कुछ सौ मीटर पर तीस्ता की उपोष्ण घाटियों से भारत की सबसे ऊँची चोटी कंचनजंगा तक उठता है। गंगटोक राजधानी है।\n\nसिक्किम तीन सदियों से अधिक समय तक नामग्याल वंश (चोग्याल) द्वारा शासित राज्य रहा, फिर ब्रिटिश संरक्षित राज्य और फिर भारतीय संरक्षित राज्य, जब तक 16 मई 1975 को यह भारत का 22वाँ राज्य नहीं बना। यह अपने बौद्ध मठों, लेप्चा, भूटिया और नेपाली समुदायों के मेल, और भारत का पहला पूर्णतः जैविक खेती वाला राज्य होने के लिए जाना जाता है।",
        "सिक्कीम हे ईशान्येकडील एक लहान हिमालयी राज्य आहे, ज्याच्या पश्चिमेला नेपाळ, उत्तर व पूर्वेला चीनचा तिबेट प्रदेश, आग्नेयेला भूतान आणि दक्षिणेला पश्चिम बंगाल आहे. 2011 च्या जनगणनेनुसार 6.1 लाख लोकसंख्येसह ते भारतातील सर्वांत कमी लोकसंख्येचे राज्य आहे, आणि क्षेत्रफळाने गोव्यानंतर दुसरे सर्वांत लहान. सुमारे 100 किमीच्या आत ते काही शे मीटर उंचीवरील तिस्तेच्या उपोष्ण खोऱ्यांपासून भारतातील सर्वोच्च शिखर कांचनजंगापर्यंत चढते. गंगटोक ही राजधानी आहे.\n\nसिक्कीम हे तीनशेहून अधिक वर्षे नामग्याल घराण्याचे (चोग्याल) राज्य होते, नंतर ब्रिटिश संरक्षित राज्य व पुढे भारतीय संरक्षित राज्य, 16 मे 1975 रोजी ते भारताचे 22 वे राज्य होईपर्यंत. ते बौद्ध मठ, लेप्चा, भुतिया व नेपाळी समुदायांचा मेळ, आणि पूर्णतः सेंद्रिय शेती करणारे भारतातील पहिले राज्य म्हणून ओळखले जाते."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Few places pack so much into so little land. Sikkim has glaciers and high-altitude lakes such as Gurudongmar and Tsomgo, rhododendron forests, terraced cardamom fields and orchid-filled valleys, and Khangchendzonga National Park is India's first 'mixed' UNESCO World Heritage Site, listed for both its nature and its sacred landscape. It has eleven official languages, monasteries such as Rumtek and Pemayangtse, and festivals such as Losar, Saga Dawa and Pang Lhabsol. In the MoSPI series it has the highest per capita income of any State or UT, and its infant mortality rate is among the lowest in India.",
        "बहुत कम जगहें इतनी छोटी भूमि में इतना कुछ समेटे हैं। सिक्किम में हिमनद और गुरुडोंगमार व छांगू (त्सोमगो) जैसी ऊँची झीलें, बुरांश के वन, सीढ़ीदार इलायची के खेत और ऑर्किड से भरी घाटियाँ हैं, और खांगचेंदज़ोंगा राष्ट्रीय उद्यान भारत का पहला 'मिश्रित' यूनेस्को विश्व धरोहर स्थल है, जो अपनी प्रकृति और पवित्र भूदृश्य दोनों के लिए सूचीबद्ध है। इसकी ग्यारह राजभाषाएँ हैं, रुमटेक और पेमायांग्त्से जैसे मठ हैं, और लोसार, सागा दावा और पांग ल्हाबसोल जैसे त्योहार हैं। मोस्पी शृंखला में इसकी प्रति व्यक्ति आय किसी भी राज्य या केंद्र शासित प्रदेश में सबसे अधिक है, और इसकी शिशु मृत्यु दर भारत में सबसे कम में है।",
        "इतक्या लहान भूमीत इतके काही असलेली ठिकाणे फार थोडी आहेत. सिक्कीममध्ये हिमनद्या व गुरुडोंगमार आणि छांगू (त्सोमगो) सारखी उंचावरील सरोवरे, ऱ्होडोडेंड्रॉनची जंगले, पायऱ्यांची वेलचीची शेते व ऑर्किडांनी भरलेली खोरी आहेत, आणि खांगचेंदझोंगा राष्ट्रीय उद्यान हे भारतातील पहिले 'मिश्र' युनेस्को जागतिक वारसा स्थळ आहे, जे निसर्ग व पवित्र भूदृश्य दोन्हींसाठी सूचीबद्ध आहे. त्याच्या अकरा राजभाषा आहेत, रुमटेक व पेमायांगत्सेसारखे मठ आहेत, आणि लोसार, सागा दावा व पांग ल्हाबसोलसारखे सण आहेत. मोस्पी मालिकेत त्याचे दरडोई उत्पन्न कोणत्याही राज्य वा केंद्रशासित प्रदेशात सर्वाधिक आहे, आणि त्याचा अर्भक मृत्युदर भारतातील सर्वांत कमींपैकी आहे."),
        title=L("What makes Sikkim unique?", "सिक्किम को ख़ास क्या बनाता है?", "सिक्कीमचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Statehood", "राज्य का दर्जा", "राज्याचा दर्जा"), L("16 May 1975 (Sikkim State Day)", "16 मई 1975 (सिक्किम राज्य दिवस)", "16 मे 1975 (सिक्कीम राज्य दिन)")],
           [L("Districts", "ज़िले", "जिल्हे"), L("6 (Gangtok, Gyalshing, Mangan, Namchi, Pakyong, Soreng)", "6 (गंगटोक, ग्यालशिंग, मंगन, नामची, पाक्योंग, सोरेंग)", "6 (गंगटोक, ग्यालशिंग, मंगन, नामची, पाकयोंग, सोरेंग)")],
           [L("Capital", "राजधानी", "राजधानी"), L("Gangtok", "गंगटोक", "गंगटोक")],
           [L("Official languages", "राजभाषाएँ", "राजभाषा"), L("Eleven, including Nepali, Bhutia, Lepcha and Limbu; English is used for official work", "ग्यारह, जिनमें नेपाली, भूटिया, लेप्चा और लिम्बू शामिल हैं; आधिकारिक कार्य में अंग्रेज़ी", "अकरा, ज्यांत नेपाळी, भुतिया, लेप्चा व लिंबू; अधिकृत कामकाजात इंग्रजी")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("High Court of Sikkim, Gangtok", "सिक्किम उच्च न्यायालय, गंगटोक", "सिक्कीम उच्च न्यायालय, गंगटोक")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "SK"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; Pakyong and Soreng districts were created in 2021, and the four older districts were renamed after their headquarters.", "संपादकीय; पाक्योंग और सोरेंग ज़िले 2021 में बने, और चार पुराने ज़िलों के नाम उनके मुख्यालयों पर रखे गए।", "संपादकीय; पाकयोंग व सोरेंग जिल्हे 2021 मध्ये निर्माण झाले, आणि चार जुन्या जिल्ह्यांना त्यांच्या मुख्यालयांची नावे दिली गेली.")),
    gaps("g", [
        (L("District reorganisation of 2021 — official notification", "2021 का ज़िला पुनर्गठन — आधिकारिक अधिसूचना", "2021 ची जिल्हा पुनर्रचना — अधिकृत अधिसूचना"), "india-gov", "Government of Sikkim Gazette."),
    ]),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Sikkim is the basin of the Teesta and its main tributary the Rangeet, enclosed by mountain ranges on three sides: the Singalila range along the Nepal border to the west, with Kangchenjunga at its northern end, and the Chola and Dongkya ranges along the Tibet and Bhutan borders to the east, crossed by passes such as Nathu La and Jelep La. The north is high and cold, with glaciers such as the Zemu, alpine pastures and lakes such as Gurudongmar and Cholamu at over 5,000 m; the south falls to warm, forested valleys where the Teesta leaves for West Bengal at Melli and Rangpo. Steep slopes, heavy rain and young rocks make landslides common.",
        "सिक्किम तीस्ता और उसकी मुख्य सहायक नदी रंगीत का बेसिन है, जो तीन ओर पर्वत शृंखलाओं से घिरा है: पश्चिम में नेपाल सीमा के साथ सिंगालीला शृंखला, जिसके उत्तरी छोर पर कंचनजंगा है, और पूर्व में तिब्बत और भूटान सीमाओं के साथ चोला और डोंक्या शृंखलाएँ, जिन्हें नाथु ला और जेलेप ला जैसे दर्रे पार करते हैं। उत्तर ऊँचा और ठंडा है, जहाँ ज़ेमू जैसे हिमनद, अल्पाइन चरागाह और 5,000 मीटर से ऊपर गुरुडोंगमार और छोलामु जैसी झीलें हैं; दक्षिण गर्म, वनाच्छादित घाटियों में उतरता है, जहाँ तीस्ता मेल्ली और रंगपो पर पश्चिम बंगाल में जाती है। खड़ी ढलानें, भारी वर्षा और नई चट्टानें भूस्खलन को आम बनाती हैं।",
        "सिक्कीम हे तिस्ता व तिची मुख्य उपनदी रंगीत यांचे खोरे आहे, जे तीन बाजूंनी पर्वतरांगांनी वेढलेले आहे: पश्चिमेला नेपाळ सीमेलगत सिंगालीला रांग, जिच्या उत्तर टोकाला कांचनजंगा आहे, आणि पूर्वेला तिबेट व भूतान सीमांलगत चोला व डोंक्या रांगा, ज्या नथु ला व जेलेप ला सारख्या खिंडींनी ओलांडल्या जातात. उत्तरेकडील भाग उंच व थंड आहे, जिथे झेमूसारख्या हिमनद्या, अल्पाइन कुरणे आणि 5,000 मीटरहून अधिक उंचीवर गुरुडोंगमार व छोलामुसारखी सरोवरे आहेत; दक्षिण भाग उबदार, वनाच्छादित खोऱ्यांत उतरतो, जिथे तिस्ता मेल्ली व रंगपो येथे पश्चिम बंगालमध्ये जाते. तीव्र उतार, मुसळधार पाऊस व नवे खडक यांमुळे भूस्खलन सामान्य आहे."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), sk["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("np", "Nepal (west)", "नेपाल (पश्चिम)", "नेपाळ (पश्चिम)"), it3("cn", "Tibet region of China (north and east)", "चीन का तिब्बत क्षेत्र (उत्तर और पूर्व)", "चीनचा तिबेट प्रदेश (उत्तर व पूर्व)"),
        it3("bt", "Bhutan (south-east)", "भूटान (दक्षिण-पूर्व)", "भूतान (आग्नेय)"), it3("wb", "West Bengal (south)", "पश्चिम बंगाल (दक्षिण)", "पश्चिम बंगाल (दक्षिण)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("teesta", "Teesta", "तीस्ता", "तिस्ता", d=("Rises in the glaciers of the north; flows south through Chungthang, Mangan and Singtam into West Bengal.", "उत्तर के हिमनदों से निकलती है; चुंगथांग, मंगन और सिंगताम से होकर दक्षिण में पश्चिम बंगाल जाती है।", "उत्तरेकडील हिमनद्यांतून उगम; चुंगथांग, मंगन व सिंगतामवरून दक्षिणेला पश्चिम बंगालमध्ये जाते.")),
        it3("rangeet", "Rangeet", "रंगीत", "रंगीत", d=("Drains the west; joins the Teesta at Melli.", "पश्चिमी भाग का जल बहाती है; मेल्ली में तीस्ता से मिलती है।", "पश्चिम भागाचे पाणी वाहते; मेल्ली येथे तिस्तेला मिळते.")),
        it3("lachung", "Lachung and Lachen chu", "लाचुंग और लाचेन छू", "लाचुंग व लाचेन छू", d=("Headstreams of the Teesta that meet at Chungthang.", "तीस्ता की उद्गम धाराएँ जो चुंगथांग में मिलती हैं।", "तिस्तेचे उगम प्रवाह, जे चुंगथांग येथे मिळतात.")),
        it3("rangpo", "Rangpo chu", "रंगपो छू", "रंगपो छू", d=("Eastern tributary; the border town of Rangpo stands on it.", "पूर्वी सहायक नदी; सीमावर्ती नगर रंगपो इसके किनारे है।", "पूर्वेकडील उपनदी; सीमेवरील रंगपो शहर तिच्या काठी आहे.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    lst("peaks", [
        it3("kanchenjunga", "Kangchenjunga", "कंचनजंगा", "कांचनजंगा", m=("India's highest peak", "भारत की सबसे ऊँची चोटी", "भारतातील सर्वोच्च शिखर")),
        it3("siniolchu", "Siniolchu", "सिनिओल्चू", "सिनिओल्चू"), it3("pandim", "Pandim", "पांडिम", "पांडिम"),
        it3("kabru", "Kabru", "काबरू", "काब्रू"), it3("nathula", "Nathu La pass", "नाथु ला दर्रा", "नथु ला खिंड"),
    ], layout="chips", title=L("Peaks and passes", "चोटियाँ और दर्रे", "शिखरे व खिंडी"), conf="Editorial"),
    gaps("g", [
        (L("Kangchenjunga — official elevation", "कंचनजंगा — आधिकारिक ऊँचाई", "कांचनजंगा — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Length of international borders by country", "देशवार अंतरराष्ट्रीय सीमा की लंबाई", "देशनिहाय आंतरराष्ट्रीय सीमेची लांबी"), "india-gov", "Ministry of Home Affairs (Department of Border Management)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Sikkim's climate changes with height more than with season. The southern valleys are warm and humid, Gangtok at about 1,600 m is mild, and the north above 4,000 m is alpine, with snow for much of the year. The south-west monsoon from June to September brings very heavy rain, landslides and road closures; October to December is clear, with the best mountain views; and January and February are cold, with snow on the higher roads to Tsomgo, Nathu La and Lachung.",
        "सिक्किम की जलवायु मौसम से अधिक ऊँचाई के साथ बदलती है। दक्षिणी घाटियाँ गर्म और आर्द्र हैं, लगभग 1,600 मीटर पर गंगटोक सुहावना है, और 4,000 मीटर से ऊपर का उत्तर अल्पाइन है, जहाँ वर्ष के बड़े भाग में बर्फ़ रहती है। जून से सितंबर तक दक्षिण-पश्चिम मानसून बहुत भारी वर्षा, भूस्खलन और सड़कें बंद होना लाता है; अक्टूबर से दिसंबर साफ़ रहता है, पहाड़ों के सबसे अच्छे दृश्यों के साथ; और जनवरी-फ़रवरी ठंडे होते हैं, जब छांगू, नाथु ला और लाचुंग की ऊँची सड़कों पर बर्फ़ होती है।",
        "सिक्कीमचे हवामान ऋतूपेक्षा उंचीनुसार अधिक बदलते. दक्षिणेकडील खोरी उबदार व दमट आहेत, सुमारे 1,600 मीटरवरील गंगटोक सौम्य आहे, आणि 4,000 मीटरवरील उत्तर भाग अल्पाइन आहे, जिथे वर्षाचा बराच काळ बर्फ असते. जून ते सप्टेंबर नैर्ऋत्य मान्सून अतिशय मुसळधार पाऊस, भूस्खलन व रस्ते बंद होणे आणतो; ऑक्टोबर ते डिसेंबर निरभ्र असतो, पर्वतांच्या सर्वोत्तम दर्शनासह; आणि जानेवारी-फेब्रुवारी थंड असतात, जेव्हा छांगू, नथु ला व लाचुंगच्या उंच रस्त्यांवर बर्फ असते."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Gangtok", "गंगटोक", "गंगटोक"), "lat": 27.3314, "lon": 88.6138},
        {"name": L("Namchi", "नामची", "नामची"), "lat": 27.1667, "lon": 88.3500},
        {"name": L("Mangan", "मंगन", "मंगन"), "lat": 27.5066, "lon": 88.5297},
        {"name": L("Lachung", "लाचुंग", "लाचुंग"), "lat": 27.6890, "lon": 88.7436},
    ]},
    lst("best", [
        it3("spring", "March to May", "मार्च से मई", "मार्च ते मे", d=("Rhododendrons and orchids in bloom; trekking season.", "बुरांश और ऑर्किड खिलते हैं; ट्रेकिंग का मौसम।", "ऱ्होडोडेंड्रॉन व ऑर्किड बहरतात; ट्रेकिंगचा हंगाम.")),
        it3("autumn", "October to December", "अक्टूबर से दिसंबर", "ऑक्टोबर ते डिसेंबर", d=("Clear skies and views of Kangchenjunga.", "साफ़ आसमान और कंचनजंगा के दृश्य।", "निरभ्र आकाश व कांचनजंगाचे दर्शन.")),
        it3("winter", "January to February", "जनवरी से फ़रवरी", "जानेवारी ते फेब्रुवारी", d=("Snow at Tsomgo and Lachung; Losar celebrations. Some high roads close.", "छांगू और लाचुंग में बर्फ़; लोसार उत्सव। कुछ ऊँची सड़कें बंद होती हैं।", "छांगू व लाचुंगला बर्फ; लोसार उत्सव. काही उंच रस्ते बंद होतात.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall", "सामान्य वार्षिक वर्षा", "सरासरी वार्षिक पाऊस"), "imd", "IMD Gangtok meteorological centre."),
        (L("Glacier retreat and glacial lakes — official assessment", "हिमनदों का पीछे हटना और हिमनद झीलें — आधिकारिक आकलन", "हिमनद्यांचे मागे हटणे व हिमनदी सरोवरे — अधिकृत मूल्यांकन"), "isro", "ISRO / NRSC glacial lake atlas; Sikkim State Disaster Management Authority."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Sikkim feels calm and orderly. Gangtok's MG Marg is a car-free, litter-free promenade where people stroll in the evening; prayer flags flutter on ridges and bridges, and monks in maroon robes walk to monasteries above the town. Plastic bags and packaged drinking water in plastic bottles are restricted, and towns are known for their cleanliness. Life follows the farming year and a dense calendar of Buddhist, Hindu and Lepcha festivals, and a cup of butter tea or a plate of momos is never far away.",
        "सिक्किम शांत और व्यवस्थित लगता है। गंगटोक का एमजी मार्ग वाहन-मुक्त, कूड़ा-मुक्त सैरगाह है जहाँ लोग शाम को टहलते हैं; पहाड़ियों और पुलों पर प्रार्थना झंडे लहराते हैं, और मरून वस्त्रों में भिक्षु नगर के ऊपर के मठों की ओर जाते हैं। प्लास्टिक की थैलियों और प्लास्टिक की बोतलों में बंद पेयजल पर रोक है, और नगर अपनी स्वच्छता के लिए जाने जाते हैं। जीवन खेती के वर्ष और बौद्ध, हिंदू और लेप्चा त्योहारों के घने कैलेंडर के साथ चलता है, और मक्खन वाली चाय या मोमो की प्लेट कभी दूर नहीं होती।",
        "सिक्कीम शांत व शिस्तबद्ध वाटते. गंगटोकचा एमजी मार्ग वाहनमुक्त, कचरामुक्त पदपथ आहे जिथे लोक संध्याकाळी फिरतात; डोंगरकडांवर व पुलांवर प्रार्थना ध्वज फडकतात, आणि लालसर वस्त्रांतील भिक्षू शहरावरच्या मठांकडे जातात. प्लास्टिक पिशव्या व प्लास्टिक बाटल्यांतील पॅकबंद पाण्यावर निर्बंध आहेत, आणि शहरे स्वच्छतेसाठी ओळखली जातात. जीवन शेतीच्या वर्षाप्रमाणे आणि बौद्ध, हिंदू व लेप्चा सणांच्या भरगच्च दिनदर्शिकेप्रमाणे चालते, आणि लोण्याचा चहा किंवा मोमोची प्लेट कधीच दूर नसते."),
        conf="Editorial"),
    gaps("g", [
        (L("Plastic and packaged-water restrictions — official orders", "प्लास्टिक और बोतलबंद पानी पर रोक — आधिकारिक आदेश", "प्लास्टिक व पॅकबंद पाण्यावरील निर्बंध — अधिकृत आदेश"), "india-gov", "Sikkim Forest and Environment / Urban Development department notifications."),
    ]),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Sikkim had 6.1 lakh people at the 2011 Census, about 86 per km². Its sex ratio was 890 women per 1,000 men, up from 875 in 2001, while the child sex ratio fell slightly from 963 to 957, and literacy was 81.4%. Scheduled Tribes made up 33.8% of the population — the Lepcha, regarded as the original inhabitants, the Bhutia and, since 2003, the Limboo and Tamang — and Scheduled Castes 4.6%.\n\nNepali, spoken by the Nepali-origin majority, is the common language of the State; Bhutia (Sikkimese), Lepcha, Limbu, Newari, Rai, Gurung, Mangar, Sherpa, Tamang and Sunwar are also official languages, and English is the language of administration and schooling.",
        "2011 की जनगणना में सिक्किम की जनसंख्या 6.1 लाख थी, प्रति वर्ग किमी लगभग 86। लिंगानुपात प्रति 1,000 पुरुषों पर 890 महिलाएँ था, जो 2001 के 875 से अधिक है, जबकि शिशु लिंगानुपात 963 से थोड़ा घटकर 957 हुआ, और साक्षरता 81.4% थी। अनुसूचित जनजातियाँ जनसंख्या का 33.8% थीं — लेप्चा, जिन्हें मूल निवासी माना जाता है, भूटिया और 2003 से लिम्बू और तमांग — और अनुसूचित जातियाँ 4.6%।\n\nनेपाली मूल के बहुसंख्यकों द्वारा बोली जाने वाली नेपाली राज्य की सामान्य भाषा है; भूटिया (सिक्किमी), लेप्चा, लिम्बू, नेवारी, राई, गुरुंग, मगर, शेर्पा, तमांग और सुनुवार भी राजभाषाएँ हैं, और प्रशासन व शिक्षा की भाषा अंग्रेज़ी है।",
        "2011 च्या जनगणनेनुसार सिक्कीमची लोकसंख्या 6.1 लाख होती, प्रति चौ.किमी सुमारे 86. दर 1,000 पुरुषांमागे 890 स्त्रिया होत्या, 2001 मधील 875 वरून वाढ, तर बाल लिंग गुणोत्तर 963 वरून किंचित घटून 957 झाले, आणि साक्षरता 81.4% होती. अनुसूचित जमाती लोकसंख्येच्या 33.8% होत्या — मूळ रहिवासी मानले जाणारे लेप्चा, भुतिया व 2003 पासून लिंबू आणि तमांग — आणि अनुसूचित जाती 4.6%.\n\nनेपाळी वंशाच्या बहुसंख्याकांची नेपाळी ही राज्याची सामान्य भाषा आहे; भुतिया (सिक्कीमी), लेप्चा, लिंबू, नेवारी, राई, गुरुंग, मगर, शेर्पा, तमांग व सुनुवार याही राजभाषा आहेत, आणि प्रशासन व शिक्षणाची भाषा इंग्रजी आहे."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), sk["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), sk["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(875, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), sk["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(963, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), sk["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), sk["density2011"], "number"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(33.8, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 2.06 lakh people. Scheduled Castes were 4.6% (0.28 lakh)."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("ne", "Nepali", "नेपाली", "नेपाळी", m=("Official; in the Eighth Schedule", "राजभाषा; आठवीं अनुसूची में", "राजभाषा; आठव्या अनुसूचीत")),
        it3("bhu", "Bhutia (Sikkimese)", "भूटिया (सिक्किमी)", "भुतिया (सिक्कीमी)", m=("Official", "राजभाषा", "राजभाषा")),
        it3("lep", "Lepcha", "लेप्चा", "लेप्चा", m=("Official", "राजभाषा", "राजभाषा")),
        it3("lim", "Limbu", "लिम्बू", "लिंबू", m=("Official", "राजभाषा", "राजभाषा")),
        it3("new", "Newari", "नेवारी", "नेवारी"), it3("rai", "Rai", "राई", "राई"), it3("gur", "Gurung", "गुरुंग", "गुरुंग"),
        it3("mag", "Mangar", "मगर", "मगर"), it3("she", "Sherpa", "शेर्पा", "शेर्पा"), it3("tam", "Tamang", "तमांग", "तमांग"), it3("sun", "Sunwar", "सुनुवार", "सुनुवार"),
        it3("en", "English", "अंग्रेज़ी", "इंग्रजी", m=("Language of administration", "प्रशासन की भाषा", "प्रशासनाची भाषा")),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Official Languages Act — list and amendments", "राजभाषा अधिनियम — सूची और संशोधन", "राजभाषा अधिनियम — यादी व सुधारणा"), "india-gov", "Sikkim Official Languages Act, 1977 and later amendments."),
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "The Lepcha were Sikkim's earliest known inhabitants. In 1642 Phuntsog Namgyal was consecrated the first Chogyal (king) at Yuksom by three Tibetan lamas, founding the Namgyal dynasty that ruled Sikkim until 1975; the capital later moved to Rabdentse and, in the 19th century, to Tumlong and then Gangtok. Wars with Nepal and Bhutan cost Sikkim territory, and the Darjeeling hills were ceded to the British East India Company in 1835. The Treaty of Tumlong (1861) and the Anglo-Chinese Convention of 1890 made Sikkim a British protectorate, and the road through Nathu La and Jelep La became a major trade route to Tibet.\n\nAfter India's independence a treaty in 1950 made Sikkim an Indian protectorate, with India responsible for defence, external affairs and communications. Political movements for democracy grew in the 1970s, and after an Assembly election in 1974 and a referendum on 14 April 1975 that voted to abolish the monarchy, Sikkim became the 22nd State of India on 16 May 1975 under the Constitution (Thirty-sixth Amendment) Act. Kazi Lhendup Dorjee was its first Chief Minister.",
        "लेप्चा सिक्किम के सबसे पहले ज्ञात निवासी थे। 1642 में तीन तिब्बती लामाओं ने युकसोम में फुन्त्सोग नामग्याल को पहला चोग्याल (राजा) अभिषिक्त किया, जिससे नामग्याल वंश की स्थापना हुई जिसने 1975 तक सिक्किम पर शासन किया; राजधानी बाद में राबदेन्त्से और 19वीं सदी में तुमलोंग और फिर गंगटोक आई। नेपाल और भूटान से युद्धों में सिक्किम ने भूभाग खोया, और 1835 में दार्जिलिंग की पहाड़ियाँ ब्रिटिश ईस्ट इंडिया कंपनी को सौंपी गईं। तुमलोंग की संधि (1861) और 1890 के आंग्ल-चीनी अभिसमय ने सिक्किम को ब्रिटिश संरक्षित राज्य बनाया, और नाथु ला व जेलेप ला से होकर जाने वाला मार्ग तिब्बत का प्रमुख व्यापार मार्ग बना।\n\nभारत की स्वतंत्रता के बाद 1950 की एक संधि ने सिक्किम को भारतीय संरक्षित राज्य बनाया, जिसमें रक्षा, विदेश मामले और संचार भारत के ज़िम्मे थे। 1970 के दशक में लोकतंत्र के लिए राजनीतिक आंदोलन बढ़े, और 1974 के विधानसभा चुनाव और 14 अप्रैल 1975 के जनमत संग्रह के बाद, जिसमें राजतंत्र समाप्त करने के पक्ष में मत पड़े, संविधान (छत्तीसवाँ संशोधन) अधिनियम के तहत 16 मई 1975 को सिक्किम भारत का 22वाँ राज्य बना। काज़ी ल्हेंडुप दोरजी इसके पहले मुख्यमंत्री थे।",
        "लेप्चा हे सिक्कीमचे सर्वांत जुने ज्ञात रहिवासी होते. 1642 मध्ये तीन तिबेटी लामांनी युकसोम येथे फुंत्सोग नामग्याल यांना पहिले चोग्याल (राजा) म्हणून अभिषेक केला, आणि नामग्याल घराण्याची स्थापना झाली ज्याने 1975 पर्यंत सिक्कीमवर राज्य केले; राजधानी नंतर राबदेंत्से व एकोणिसाव्या शतकात तुमलोंग व पुढे गंगटोकला आली. नेपाळ व भूतानशी झालेल्या युद्धांत सिक्कीमने भूभाग गमावला, आणि 1835 मध्ये दार्जिलिंगचे डोंगर ब्रिटिश ईस्ट इंडिया कंपनीला दिले गेले. तुमलोंगचा तह (1861) व 1890 च्या आंग्ल-चिनी करारामुळे सिक्कीम ब्रिटिश संरक्षित राज्य झाले, आणि नथु ला व जेलेप ला मार्गे जाणारा रस्ता तिबेटकडील प्रमुख व्यापारी मार्ग बनला.\n\nभारताच्या स्वातंत्र्यानंतर 1950 च्या तहाने सिक्कीम भारतीय संरक्षित राज्य झाले, ज्यात संरक्षण, परराष्ट्र व्यवहार व दळणवळण भारताकडे होते. 1970 च्या दशकात लोकशाहीसाठीच्या राजकीय चळवळी वाढल्या, आणि 1974 ची विधानसभा निवडणूक व 14 एप्रिल 1975 च्या सार्वमतानंतर, ज्यात राजेशाही रद्द करण्याच्या बाजूने कौल मिळाला, संविधान (छत्तिसावी सुधारणा) अधिनियमान्वये 16 मे 1975 रोजी सिक्कीम भारताचे 22 वे राज्य झाले. काझी ल्हेंडुप दोरजी हे त्याचे पहिले मुख्यमंत्री होते."),
        conf="Editorial"),
    timeline([
        ev("yuksom", 1642, L("1642", "1642", "1642"), L("Phuntsog Namgyal consecrated first Chogyal at Yuksom", "युकसोम में फुन्त्सोग नामग्याल पहले चोग्याल अभिषिक्त", "युकसोम येथे फुंत्सोग नामग्याल पहिले चोग्याल")),
        ev("darjeeling", 1835, L("1835", "1835", "1835"), L("Darjeeling hills ceded to the British", "दार्जिलिंग की पहाड़ियाँ अंग्रेज़ों को सौंपी गईं", "दार्जिलिंगचे डोंगर ब्रिटिशांना दिले")),
        ev("tumlong", 1861, L("1861", "1861", "1861"), L("Treaty of Tumlong; Sikkim becomes a British protectorate", "तुमलोंग की संधि; सिक्किम ब्रिटिश संरक्षित राज्य", "तुमलोंगचा तह; सिक्कीम ब्रिटिश संरक्षित राज्य")),
        ev("treaty1950", 1950, L("1950", "1950", "1950"), L("Indo-Sikkim treaty; Indian protectorate", "भारत-सिक्किम संधि; भारतीय संरक्षित राज्य", "भारत-सिक्कीम तह; भारतीय संरक्षित राज्य")),
        ev("referendum", 1975, L("14 April 1975", "14 अप्रैल 1975", "14 एप्रिल 1975"), L("Referendum votes to abolish the monarchy", "जनमत संग्रह में राजतंत्र समाप्त करने के पक्ष में मत", "सार्वमतात राजेशाही रद्द करण्याचा कौल")),
        ev("state", 1975, L("16 May 1975", "16 मई 1975", "16 मे 1975"), L("Sikkim becomes India's 22nd State", "सिक्किम भारत का 22वाँ राज्य बना", "सिक्कीम भारताचे 22 वे राज्य")),
        ev("nathula", 2006, L("2006", "2006", "2006"), L("Border trade through Nathu La reopens", "नाथु ला से सीमा व्यापार फिर शुरू", "नथु ला मार्गे सीमा व्यापार पुन्हा सुरू")),
        ev("organic", 2016, L("January 2016", "जनवरी 2016", "जानेवारी 2016"), L("Declared India's first fully organic State", "भारत का पहला पूर्णतः जैविक राज्य घोषित", "भारताचे पहिले पूर्णतः सेंद्रिय राज्य घोषित")),
        ev("glof", 2023, L("4 October 2023", "4 अक्टूबर 2023", "4 ऑक्टोबर 2023"), L("Glacial lake outburst flood on the Teesta", "तीस्ता पर हिमनद झील फटने से बाढ़", "तिस्तेवर हिमनदी सरोवर फुटून पूर")),
    ]),
    lst("heritage", [
        it3("rumtek", "Rumtek Monastery", "रुमटेक मठ", "रुमटेक मठ", m=("Seat of the Karma Kagyu order in exile", "निर्वासन में कर्म काग्यू परंपरा का पीठ", "निर्वासनातील कर्म काग्यू परंपरेचे पीठ")),
        it3("pemayangtse", "Pemayangtse Monastery", "पेमायांग्त्से मठ", "पेमायांगत्से मठ", m=("17th century, near Pelling", "17वीं सदी, पेलिंग के पास", "सतरावे शतक, पेलिंगजवळ")),
        it3("tashiding", "Tashiding Monastery", "ताशिदिंग मठ", "ताशिदिंग मठ", m=("Bumchu festival", "बुमछू उत्सव", "बुमछू उत्सव")),
        it3("rabdentse", "Rabdentse ruins", "राबदेन्त्से के खंडहर", "राबदेंत्से अवशेष", m=("Second capital of the Chogyals", "चोग्यालों की दूसरी राजधानी", "चोग्यालांची दुसरी राजधानी")),
        it3("dubdi", "Dubdi Monastery, Yuksom", "दुबदी मठ, युकसोम", "दुबदी मठ, युकसोम", m=("Among the oldest in Sikkim", "सिक्किम के सबसे पुराने में", "सिक्कीममधील सर्वांत जुन्यांपैकी")),
        it3("enchey", "Enchey Monastery, Gangtok", "एंचे मठ, गंगटोक", "एंचे मठ, गंगटोक"),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
    gaps("g", [
        (L("Referendum of 1975 — official result", "1975 का जनमत संग्रह — आधिकारिक परिणाम", "1975 चे सार्वमत — अधिकृत निकाल"), "eci", "Official record of the 14 April 1975 referendum."),
        (L("Constitution (36th Amendment) Act, 1975 — official text", "संविधान (36वाँ संशोधन) अधिनियम, 1975 — आधिकारिक पाठ", "संविधान (36 वी सुधारणा) अधिनियम, 1975 — अधिकृत मजकूर"), "india-gov", "India Code / Legislative Department."),
    ]),
])
print("sk mod1 ok")
