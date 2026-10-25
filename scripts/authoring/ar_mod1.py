"""Arunachal Pradesh modules A–F: overview, geography, climate, vibe, people, history."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-AR"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"
BICHOM = "https://www.theweek.in/wire-updates/national/2024/03/08/ces2-ar-new-district.html"
ar = read("regions/IN-AR.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- A. Overview ----------------
module(R, "overview", [
    prose("intro", L(
        "Arunachal Pradesh, 'the land of the dawn-lit mountains', is India's north-easternmost State and the largest in the North-East, covering 83,743 km². It borders Bhutan to the west, the Tibet region of China to the north, Myanmar to the east, and Assam and Nagaland to the south. With 13.8 lakh people at the 2011 Census it is the most thinly populated State in India, about 17 people per km². Most of it is mountain and forest, cut by the deep valleys of the Kameng, Subansiri, Siang, Dibang and Lohit, which flow down to the Brahmaputra. Itanagar is the capital.\n\nThe region was the North-East Frontier Agency (NEFA), administered by the Union, until it became a Union Territory named Arunachal Pradesh on 20 January 1972; it became a State on 20 February 1987. Some 26 major tribes and more than a hundred sub-groups live here, each with its own language, dress and festivals, and English is the State's official language.",
        "अरुणाचल प्रदेश, 'उगते सूरज के पहाड़ों की भूमि', भारत का सबसे उत्तर-पूर्वी राज्य है और 83,743 वर्ग किमी के साथ पूर्वोत्तर का सबसे बड़ा राज्य। इसके पश्चिम में भूटान, उत्तर में चीन का तिब्बत क्षेत्र, पूर्व में म्यांमार और दक्षिण में असम और नागालैंड हैं। 2011 की जनगणना में 13.8 लाख लोगों के साथ यह भारत का सबसे विरल आबादी वाला राज्य है, प्रति वर्ग किमी लगभग 17 लोग। इसका अधिकांश भाग पहाड़ और वन है, जिसे कामेंग, सुबनसिरी, सियांग, दिबांग और लोहित की गहरी घाटियाँ काटती हैं, जो ब्रह्मपुत्र में उतरती हैं। ईटानगर राजधानी है।\n\nयह क्षेत्र संघ द्वारा प्रशासित नॉर्थ-ईस्ट फ़्रंटियर एजेंसी (नेफ़ा) था, जब तक 20 जनवरी 1972 को यह अरुणाचल प्रदेश नाम से केंद्र शासित प्रदेश नहीं बना; 20 फ़रवरी 1987 को यह राज्य बना। यहाँ लगभग 26 प्रमुख जनजातियाँ और सौ से अधिक उप-समूह रहते हैं, जिनकी अपनी भाषा, वेशभूषा और त्योहार हैं, और अंग्रेज़ी राज्य की राजभाषा है।",
        "अरुणाचल प्रदेश, 'उगवत्या सूर्याच्या पर्वतांची भूमी', हे भारतातील सर्वांत ईशान्येकडील राज्य असून 83,743 चौ.किमीसह ईशान्य भारतातील सर्वांत मोठे राज्य आहे. त्याच्या पश्चिमेला भूतान, उत्तरेला चीनचा तिबेट प्रदेश, पूर्वेला म्यानमार आणि दक्षिणेला आसाम व नागालँड आहेत. 2011 च्या जनगणनेनुसार 13.8 लाख लोकसंख्येसह ते भारतातील सर्वांत विरळ लोकवस्तीचे राज्य आहे, प्रति चौ.किमी सुमारे 17 लोक. त्याचा बहुतांश भाग पर्वत व जंगल आहे, ज्याला कामेंग, सुबनसिरी, सियांग, दिबांग व लोहित यांची खोल खोरी छेदतात, ज्या ब्रह्मपुत्रेत उतरतात. इटानगर ही राजधानी आहे.\n\nहा प्रदेश केंद्राद्वारे प्रशासित नॉर्थ-ईस्ट फ्रंटियर एजन्सी (नेफा) होता, 20 जानेवारी 1972 रोजी तो अरुणाचल प्रदेश नावाचा केंद्रशासित प्रदेश होईपर्यंत; 20 फेब्रुवारी 1987 रोजी ते राज्य झाले. येथे सुमारे 26 प्रमुख जमाती व शंभराहून अधिक उपगट राहतात, प्रत्येकाची स्वतःची भाषा, वेशभूषा व सण आहेत, आणि इंग्रजी ही राज्याची राजभाषा आहे."),
        sources=["census", "fsi"], conf="Editorial"),
    prose("intro-unique", L(
        "Arunachal Pradesh is exceptionally rich in plants and animals: nearly four-fifths of it is forest (ISFR 2023), and its parks range from tropical rainforest at Namdapha to alpine meadows below Kangto. Its cultural diversity is just as great — from the Buddhist Monpa of Tawang, with one of India's great monasteries, to the Apatani of the Ziro valley with their wet-rice and fish farming, and the Adi, Nyishi, Galo, Mishmi, Wancho and Khamti peoples. Twenty-one GIs are registered for the State, most of them tribal textiles and crafts.",
        "अरुणाचल प्रदेश पेड़-पौधों और जीव-जंतुओं से असाधारण रूप से समृद्ध है: इसका लगभग चार-पाँचवाँ भाग वन है (आईएसएफ़आर 2023), और इसके उद्यान नामदफा के उष्णकटिबंधीय वर्षावन से कांगतो के नीचे अल्पाइन घास के मैदानों तक फैले हैं। इसकी सांस्कृतिक विविधता भी उतनी ही बड़ी है — भारत के महान मठों में से एक वाले तवांग के बौद्ध मोनपा से लेकर गीली धान और मछली की खेती करने वाले ज़ीरो घाटी के अपातानी, और आदी, न्यिशी, गालो, मिश्मी, वांचो और खामती लोगों तक। राज्य के लिए इक्कीस जीआई पंजीकृत हैं, जिनमें अधिकांश जनजातीय वस्त्र और शिल्प हैं।",
        "अरुणाचल प्रदेश वनस्पती व प्राणिसंपदेने अत्यंत समृद्ध आहे: त्याचा जवळपास चार-पंचमांश भाग वनाच्छादित आहे (आयएसएफआर 2023), आणि त्याची उद्याने नामदफाच्या उष्णकटिबंधीय वर्षावनापासून कांगतोखालील अल्पाइन कुरणांपर्यंत आहेत. त्याची सांस्कृतिक विविधताही तितकीच मोठी आहे — भारतातील महान मठांपैकी एक असलेल्या तवांगच्या बौद्ध मोनपांपासून ओली भातशेती व मत्स्यपालन करणाऱ्या झिरो खोऱ्यातील आपातानींपर्यंत, आणि आदी, न्यिशी, गालो, मिश्मी, वांचो व खामती लोक. राज्यासाठी एकवीस जीआय नोंदणीकृत आहेत, ज्यांपैकी बहुतेक आदिवासी वस्त्रे व हस्तकला आहेत."),
        title=L("What makes Arunachal Pradesh unique?", "अरुणाचल प्रदेश को ख़ास क्या बनाता है?", "अरुणाचल प्रदेशचे वेगळेपण काय?")),
    table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
          [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))],
          [[L("Statehood", "राज्य का दर्जा", "राज्याचा दर्जा"), L("20 February 1987 (Union Territory from 20 January 1972)", "20 फ़रवरी 1987 (20 जनवरी 1972 से केंद्र शासित प्रदेश)", "20 फेब्रुवारी 1987 (20 जानेवारी 1972 पासून केंद्रशासित प्रदेश)")],
           [L("Districts", "ज़िले", "जिल्हे"), L("27 after Bichom district was inaugurated in March 2024, as reported by PTI; see the gap note", "27, मार्च 2024 में बिचोम ज़िले के उद्घाटन के बाद, पीटीआई के अनुसार; अंतर-सूचना देखें", "27, मार्च 2024 मध्ये बिचोम जिल्ह्याच्या उद्घाटनानंतर, पीटीआयनुसार; त्रुटी-टीप पाहा")],
           [L("Capital", "राजधानी", "राजधानी"), L("Itanagar", "ईटानगर", "इटानगर")],
           [L("Official language", "राजभाषा", "राजभाषा"), L("English; Hindi is widely used as a link language", "अंग्रेज़ी; हिंदी संपर्क भाषा के रूप में व्यापक", "इंग्रजी; हिंदी संपर्कभाषा म्हणून व्यापक")],
           [L("High Court", "उच्च न्यायालय", "उच्च न्यायालय"), L("Gauhati High Court, Itanagar permanent bench", "गुवाहाटी उच्च न्यायालय, ईटानगर स्थायी पीठ", "गुवाहाटी उच्च न्यायालय, इटानगर कायम खंडपीठ")],
           [L("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक"), "AR"],
           [L("Time zone", "समय क्षेत्र", "प्रमाणवेळ"), "IST (UTC+05:30)"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; Keyi Panyor and Bichom districts were created by an Act passed in February 2024.", "संपादकीय; केयी पान्योर और बिचोम ज़िले फ़रवरी 2024 में पारित अधिनियम से बने।", "संपादकीय; केयी पान्योर व बिचोम जिल्हे फेब्रुवारी 2024 मध्ये संमत अधिनियमाने निर्माण झाले.")),
    gaps("g", [
        (L("Official number of districts", "ज़िलों की आधिकारिक संख्या", "जिल्ह्यांची अधिकृत संख्या"), "india-gov", f"Reports differ on how the Itanagar Capital Complex is counted; Bichom was reported as the 27th district (PTI via The Week, {BICHOM}). Confirm from the Government of Arunachal Pradesh."),
    ]),
])

# ---------------- B. Geography ----------------
module(R, "geography", [
    prose("p1", L(
        "Arunachal Pradesh rises from the edge of the Assam plains at about 100 m to Himalayan peaks above 7,000 m, Kangto being the highest. The Greater Himalaya runs along the northern border, with passes such as Bum La above Tawang; the Mishmi hills lie in the east and the Patkai hills along the Myanmar border in the south-east. The Siang — the Yarlung Tsangpo of Tibet — cuts a deep gorge through the Himalaya before emerging at Pasighat, where it becomes the Brahmaputra after it meets the Dibang and Lohit in Assam. The Kameng and Subansiri drain the west and centre. Steep, rain-soaked slopes and active earthquakes make landslides frequent.",
        "अरुणाचल प्रदेश असम के मैदानों के किनारे लगभग 100 मीटर से 7,000 मीटर से ऊँची हिमालयी चोटियों तक उठता है, जिनमें कांगतो सबसे ऊँची है। वृहत् हिमालय उत्तरी सीमा के साथ चलता है, जिसमें तवांग के ऊपर बुम ला जैसे दर्रे हैं; पूर्व में मिश्मी पहाड़ियाँ और दक्षिण-पूर्व में म्यांमार सीमा के साथ पटकाई पहाड़ियाँ हैं। सियांग — तिब्बत की यारलुंग त्सांगपो — पासीघाट पर निकलने से पहले हिमालय में गहरा महाखड्ड काटती है, और असम में दिबांग और लोहित से मिलकर ब्रह्मपुत्र बनती है। कामेंग और सुबनसिरी पश्चिम और मध्य भाग का जल बहाती हैं। खड़ी, वर्षा से भीगी ढलानें और सक्रिय भूकंप भूस्खलन को आम बनाते हैं।",
        "अरुणाचल प्रदेश आसामच्या मैदानांच्या कडेला सुमारे 100 मीटरपासून 7,000 मीटरहून उंच हिमालयी शिखरांपर्यंत चढते, ज्यांत कांगतो सर्वोच्च आहे. बृहद् हिमालय उत्तर सीमेलगत जातो, ज्यात तवांगवर बुम लासारख्या खिंडी आहेत; पूर्वेला मिश्मी डोंगर व आग्नेयेला म्यानमार सीमेलगत पटकाई डोंगर आहेत. सियांग — तिबेटची यारलुंग त्सांगपो — पासीघाट येथे बाहेर पडण्यापूर्वी हिमालयात खोल घळ कोरते, आणि आसाममध्ये दिबांग व लोहितला मिळून ब्रह्मपुत्रा बनते. कामेंग व सुबनसिरी पश्चिम व मध्य भागाचे पाणी वाहतात. तीव्र, पावसाने भिजलेले उतार व सक्रिय भूकंप यांमुळे भूस्खलन वारंवार होते."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), ar["area"], "number", national=ind["area"])]),
    lst("neighbours", [
        it3("bt", "Bhutan (west)", "भूटान (पश्चिम)", "भूतान (पश्चिम)"), it3("cn", "Tibet region of China (north)", "चीन का तिब्बत क्षेत्र (उत्तर)", "चीनचा तिबेट प्रदेश (उत्तर)"),
        it3("mm", "Myanmar (east)", "म्यांमार (पूर्व)", "म्यानमार (पूर्व)"), it3("as", "Assam (south)", "असम (दक्षिण)", "आसाम (दक्षिण)"), it3("nl", "Nagaland (south-east)", "नागालैंड (दक्षिण-पूर्व)", "नागालँड (आग्नेय)"),
    ], layout="chips", title=L("Neighbours", "पड़ोसी", "शेजारी"), conf="Editorial"),
    lst("rivers", [
        it3("siang", "Siang (Brahmaputra)", "सियांग (ब्रह्मपुत्र)", "सियांग (ब्रह्मपुत्रा)", d=("Enters from Tibet as the Tsangpo; flows past Tuting, Yingkiong and Pasighat.", "तिब्बत से त्सांगपो के रूप में आती है; तूतिंग, यिंगक्योंग और पासीघाट से बहती है।", "तिबेटमधून त्सांगपो म्हणून येते; तूतिंग, यिंगक्योंग व पासीघाटवरून वाहते.")),
        it3("subansiri", "Subansiri", "सुबनसिरी", "सुबनसिरी", d=("Largest tributary of the Brahmaputra from the Himalaya; Lower Subansiri dam near the Assam border.", "हिमालय से ब्रह्मपुत्र की सबसे बड़ी सहायक नदी; असम सीमा के पास निचला सुबनसिरी बाँध।", "हिमालयातून येणारी ब्रह्मपुत्रेची सर्वांत मोठी उपनदी; आसाम सीमेजवळ खालचे सुबनसिरी धरण.")),
        it3("kameng", "Kameng", "कामेंग", "कामेंग", d=("Drains the west; known as the Jia Bharali in Assam.", "पश्चिमी भाग का जल बहाती है; असम में जिया भराली कहलाती है।", "पश्चिम भागाचे पाणी वाहते; आसाममध्ये जिया भराली म्हणतात.")),
        it3("lohit", "Lohit", "लोहित", "लोहित", d=("Flows past Tezu; Parshuram Kund is on its banks.", "तेज़ू से होकर बहती है; परशुराम कुंड इसके तट पर है।", "तेझूवरून वाहते; परशुराम कुंड तिच्या काठी आहे.")),
        it3("dibang", "Dibang", "दिबांग", "दिबांग", d=("Flows from the Mishmi hills past Roing.", "मिश्मी पहाड़ियों से रोइंग होते हुए बहती है।", "मिश्मी डोंगरांतून रोइंगवरून वाहते.")),
    ], title=L("Major rivers", "प्रमुख नदियाँ", "प्रमुख नद्या"), conf="Editorial"),
    gaps("g", [
        (L("Kangto — official elevation", "कांगतो — आधिकारिक ऊँचाई", "कांगतो — अधिकृत उंची"), "survey-of-india", "Survey of India."),
        (L("Length of international borders by country", "देशवार अंतरराष्ट्रीय सीमा की लंबाई", "देशनिहाय आंतरराष्ट्रीय सीमेची लांबी"), "india-gov", "Ministry of Home Affairs (Department of Border Management)."),
    ]),
])

# ---------------- C. Climate ----------------
module(R, "climate", [
    prose("p1", L(
        "Arunachal Pradesh is one of the wettest parts of India. The foothills and valleys are hot and humid, the middle hills are temperate, and the high north is alpine, with snow from November to March at Tawang, Sela and Mechuka. The south-west monsoon, from May or June to September, brings very heavy rain, floods in the river valleys and landslides that cut roads. October to April is drier and clearer, the best time to travel.",
        "अरुणाचल प्रदेश भारत के सबसे अधिक वर्षा वाले भागों में है। तलहटी और घाटियाँ गर्म और आर्द्र हैं, मध्य पहाड़ियाँ समशीतोष्ण हैं, और ऊँचा उत्तर अल्पाइन है, जहाँ तवांग, सेला और मेचुका में नवंबर से मार्च तक बर्फ़ रहती है। मई या जून से सितंबर तक दक्षिण-पश्चिम मानसून बहुत भारी वर्षा, नदी घाटियों में बाढ़ और सड़कें काटने वाले भूस्खलन लाता है। अक्टूबर से अप्रैल अधिक सूखा और साफ़ रहता है, यात्रा का सबसे अच्छा समय।",
        "अरुणाचल प्रदेश हा भारतातील सर्वाधिक पावसाच्या भागांपैकी आहे. पायथ्याचे डोंगर व खोरी उष्ण व दमट आहेत, मधले डोंगर समशीतोष्ण आहेत, आणि उंच उत्तर भाग अल्पाइन आहे, जिथे तवांग, सेला व मेचुका येथे नोव्हेंबर ते मार्च बर्फ असते. मे किंवा जून ते सप्टेंबर नैर्ऋत्य मान्सून अतिशय मुसळधार पाऊस, नदीखोऱ्यांत पूर व रस्ते तोडणारे भूस्खलन आणतो. ऑक्टोबर ते एप्रिल अधिक कोरडा व निरभ्र असतो, प्रवासासाठी उत्तम काळ."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Itanagar", "ईटानगर", "इटानगर"), "lat": 27.0844, "lon": 93.6053},
        {"name": L("Tawang", "तवांग", "तवांग"), "lat": 27.5860, "lon": 91.8590},
        {"name": L("Pasighat", "पासीघाट", "पासीघाट"), "lat": 28.0660, "lon": 95.3260},
        {"name": L("Ziro", "ज़ीरो", "झिरो"), "lat": 27.5449, "lon": 93.8197},
    ]},
    lst("best", [
        it3("autumn", "October to November", "अक्टूबर से नवंबर", "ऑक्टोबर ते नोव्हेंबर", d=("Clear skies; Torgya preparations and Ziro's music festival season.", "साफ़ आसमान; तोरग्या की तैयारी और ज़ीरो के संगीत उत्सव का मौसम।", "निरभ्र आकाश; तोरग्याची तयारी व झिरोच्या संगीत महोत्सवाचा हंगाम.")),
        it3("spring", "March to April", "मार्च से अप्रैल", "मार्च ते एप्रिल", d=("Rhododendrons in bloom; festivals such as Mopin and Sangken.", "बुरांश खिलते हैं; मोपिन और सांगकेन जैसे त्योहार।", "ऱ्होडोडेंड्रॉन बहरतात; मोपिन व सांगकेनसारखे सण.")),
        it3("winter", "December to February", "दिसंबर से फ़रवरी", "डिसेंबर ते फेब्रुवारी", d=("Snow at Tawang and Sela; Losar in February–March.", "तवांग और सेला में बर्फ़; फ़रवरी–मार्च में लोसार।", "तवांग व सेला येथे बर्फ; फेब्रुवारी–मार्चमध्ये लोसार.")),
    ], title=L("Best time to visit", "घूमने का सबसे अच्छा समय", "भेटीसाठी उत्तम काळ"), conf="Editorial"),
    gaps("g", [
        (L("Normal annual rainfall", "सामान्य वार्षिक वर्षा", "सरासरी वार्षिक पाऊस"), "imd", "IMD Itanagar / Guwahati regional centre."),
    ]),
])

# ---------------- D. Vibe ----------------
module(R, "vibe", [
    prose("p1", L(
        "Arunachal is a land of small towns and scattered villages linked by long mountain roads. Community and clan matter: villages are run by traditional councils such as the Adi kebang, and every tribe marks the farming year with its own festival of dances, prayers and shared feasts with rice beer. Bamboo houses on stilts, longhouses and Buddhist prayer flags tell you which valley you are in. Itanagar and Naharlagun are the busiest places; elsewhere life is quiet and close to the forest.",
        "अरुणाचल छोटे नगरों और बिखरे गाँवों की भूमि है, जो लंबी पहाड़ी सड़कों से जुड़े हैं। समुदाय और कुल महत्त्वपूर्ण हैं: गाँव आदी केबांग जैसी पारंपरिक परिषदों द्वारा चलाए जाते हैं, और हर जनजाति खेती के वर्ष को नृत्य, प्रार्थना और चावल की बियर के साथ सामूहिक भोज वाले अपने त्योहार से मनाती है। खंभों पर बने बाँस के घर, लंबे घर और बौद्ध प्रार्थना झंडे बताते हैं कि आप किस घाटी में हैं। ईटानगर और नहारलगुन सबसे व्यस्त स्थान हैं; अन्यत्र जीवन शांत और वन के निकट है।",
        "अरुणाचल ही लहान शहरे व विखुरलेल्या गावांची भूमी आहे, जी लांब डोंगरी रस्त्यांनी जोडलेली आहेत. समुदाय व कुळाला महत्त्व आहे: गावांचा कारभार आदी केबांगसारख्या पारंपरिक परिषदा चालवतात, आणि प्रत्येक जमात शेतीचे वर्ष नृत्य, प्रार्थना व तांदळाच्या मद्यासह सामूहिक भोजनाच्या आपल्या सणाने साजरे करते. खांबांवरील बांबूची घरे, लांब घरे व बौद्ध प्रार्थना ध्वज सांगतात की तुम्ही कोणत्या खोऱ्यात आहात. इटानगर व नाहरलगुन ही सर्वांत गजबजलेली ठिकाणे आहेत; इतरत्र जीवन शांत व जंगलाच्या जवळ आहे."),
        conf="Editorial"),
])

# ---------------- E. People ----------------
module(R, "people", [
    prose("p1", L(
        "Arunachal Pradesh had 13.8 lakh people at the 2011 Census. Its sex ratio was 938 women per 1,000 men, up sharply from 893 in 2001, and its child sex ratio 972, among the highest in India; literacy was 65.4%, below the national average. Scheduled Tribes made up 68.8% of the population — among them the Nyishi, Adi, Galo, Apatani, Tagin, Monpa, Sherdukpen, Aka, Miji, Mishmi, Khamti, Singpho, Tangsa, Nocte and Wancho — and there are no Scheduled Castes listed for the State.\n\nEach tribe speaks its own language, mostly of the Tibeto-Burman family, so English is the official language and Hindi, in a local form often called Arunachali Hindi, is the everyday link language across the State.",
        "2011 की जनगणना में अरुणाचल प्रदेश की जनसंख्या 13.8 लाख थी। लिंगानुपात प्रति 1,000 पुरुषों पर 938 महिलाएँ था, जो 2001 के 893 से काफ़ी अधिक है, और शिशु लिंगानुपात 972, जो भारत में सबसे ऊँचे में है; साक्षरता 65.4% थी, राष्ट्रीय औसत से कम। अनुसूचित जनजातियाँ जनसंख्या का 68.8% थीं — इनमें न्यिशी, आदी, गालो, अपातानी, तागिन, मोनपा, शेरदुकपेन, आका, मिजी, मिश्मी, खामती, सिंगफ़ो, तांगसा, नोक्टे और वांचो शामिल हैं — और राज्य के लिए कोई अनुसूचित जाति सूचीबद्ध नहीं है।\n\nहर जनजाति अपनी भाषा बोलती है, अधिकतर तिब्बती-बर्मी परिवार की, इसलिए अंग्रेज़ी राजभाषा है और हिंदी, एक स्थानीय रूप में जिसे अक्सर अरुणाचली हिंदी कहा जाता है, पूरे राज्य में रोज़मर्रा की संपर्क भाषा है।",
        "2011 च्या जनगणनेनुसार अरुणाचल प्रदेशची लोकसंख्या 13.8 लाख होती. दर 1,000 पुरुषांमागे 938 स्त्रिया होत्या, 2001 मधील 893 वरून मोठी वाढ, आणि बाल लिंग गुणोत्तर 972 होते, भारतातील सर्वाधिकांपैकी; साक्षरता 65.4% होती, राष्ट्रीय सरासरीपेक्षा कमी. अनुसूचित जमाती लोकसंख्येच्या 68.8% होत्या — त्यांत न्यिशी, आदी, गालो, आपातानी, तागिन, मोनपा, शेरदुकपेन, आका, मिजी, मिश्मी, खामती, सिंगफो, तांगसा, नोक्टे व वांचो — आणि राज्यासाठी कोणत्याही अनुसूचित जाती सूचीबद्ध नाहीत.\n\nप्रत्येक जमात स्वतःची भाषा बोलते, बहुतेक तिबेटी-बर्मी कुळातील, म्हणून इंग्रजी ही राजभाषा आहे आणि हिंदी, स्थानिक रूपात जिला अनेकदा अरुणाचली हिंदी म्हणतात, संपूर्ण राज्यात रोजची संपर्कभाषा आहे."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), ar["population2011"], "count", national=ind["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), ar["sexRatio2011"], "ratio", "higher-is-better", national=ind["sexRatio2011"],
             previous=dp(893, "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), ar["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(964, "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=ind["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), ar["literacyRate2011"], "percent", "higher-is-better", national=ind["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), ar["density2011"], "number"),
        fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
             dp(68.8, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 9.51 lakh people. No Scheduled Castes are listed for the State."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
    lst("langs", [
        it3("en", "English", "अंग्रेज़ी", "इंग्रजी", m=("Official language", "राजभाषा", "राजभाषा")),
        it3("hi", "Hindi (Arunachali Hindi)", "हिंदी (अरुणाचली हिंदी)", "हिंदी (अरुणाचली हिंदी)", m=("Link language", "संपर्क भाषा", "संपर्कभाषा")),
        it3("nyishi", "Nyishi", "न्यिशी", "न्यिशी"), it3("adi", "Adi", "आदी", "आदी"), it3("galo", "Galo", "गालो", "गालो"),
        it3("monpa", "Monpa", "मोनपा", "मोनपा"), it3("apatani", "Apatani", "अपातानी", "आपातानी"), it3("mishmi", "Mishmi (Idu, Digaro, Miju)", "मिश्मी (इदु, दिगारो, मिजु)", "मिश्मी (इदु, दिगारो, मिजु)"),
        it3("wancho", "Wancho", "वांचो", "वांचो"), it3("khamti", "Tai Khamti", "ताई खामती", "ताई खामती"),
    ], layout="chips", title=L("Languages", "भाषाएँ", "भाषा"), conf="Editorial"),
    gaps("g", [
        (L("Tribe-wise population (Census 2011)", "जनजातिवार जनसंख्या (जनगणना 2011)", "जमातनिहाय लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 ST tables (A-11)."),
        (L("Urban population share (Census 2011)", "शहरी जनसंख्या का हिस्सा (जनगणना 2011)", "नागरी लोकसंख्येचा वाटा (जनगणना 2011)"), "census", "Primary Census Abstract."),
        (L("Religion shares (Census 2011, C-01)", "धर्मवार हिस्सा (जनगणना 2011, C-01)", "धर्मनिहाय वाटा (जनगणना 2011, C-01)"), "census", "Census C-01 table; show without commentary."),
    ]),
])

# ---------------- F. History ----------------
module(R, "history", [
    prose("p1", L(
        "The hill peoples of what is now Arunachal Pradesh lived largely by their own customary laws, trading and sometimes fighting with the kingdoms of the Assam plains — the Chutiyas, whose ruins at Bhismaknagar near Roing date from the 12th–16th centuries, and later the Ahoms. Tawang and the Monpa areas of the west had close religious ties with Tibet; the Tawang monastery was founded in the 1680s, and the sixth Dalai Lama was born near Tawang. Under British rule the Inner Line of 1873 restricted entry from the plains, and the McMahon Line agreed at the Simla Conference of 1914 marked the boundary with Tibet.\n\nAfter independence the area was administered from Shillong and then Itanagar as the North-East Frontier Agency (NEFA), with the Governor of Assam acting for the President. During the war with China in 1962, Chinese forces advanced into parts of the region before withdrawing. NEFA became the Union Territory of Arunachal Pradesh on 20 January 1972 and a State on 20 February 1987.",
        "आज के अरुणाचल प्रदेश के पहाड़ी लोग अधिकतर अपने पारंपरिक क़ानूनों से जीते थे, और असम के मैदानों के राज्यों से व्यापार और कभी-कभी युद्ध करते थे — चुटिया, जिनके रोइंग के पास भीष्मकनगर के खंडहर 12वीं–16वीं सदी के हैं, और बाद में अहोम। पश्चिम के तवांग और मोनपा क्षेत्रों के तिब्बत से घनिष्ठ धार्मिक संबंध थे; तवांग मठ की स्थापना 1680 के दशक में हुई, और छठे दलाई लामा का जन्म तवांग के पास हुआ। ब्रिटिश शासन में 1873 की इनर लाइन ने मैदानों से प्रवेश सीमित किया, और 1914 के शिमला सम्मेलन में तय मैकमोहन रेखा ने तिब्बत के साथ सीमा चिह्नित की।\n\nस्वतंत्रता के बाद इस क्षेत्र का प्रशासन शिलांग और फिर ईटानगर से नॉर्थ-ईस्ट फ़्रंटियर एजेंसी (नेफ़ा) के रूप में हुआ, जिसमें असम के राज्यपाल राष्ट्रपति की ओर से कार्य करते थे। 1962 के चीन युद्ध में चीनी सेनाएँ क्षेत्र के कुछ भागों में आगे बढ़ीं और फिर पीछे हट गईं। 20 जनवरी 1972 को नेफ़ा अरुणाचल प्रदेश केंद्र शासित प्रदेश बना और 20 फ़रवरी 1987 को राज्य।",
        "आजच्या अरुणाचल प्रदेशातील डोंगरी लोक मुख्यतः आपल्या पारंपरिक कायद्यांनुसार जगत, आणि आसामच्या मैदानी राज्यांशी व्यापार व कधीकधी संघर्ष करत — चुटिया, ज्यांचे रोइंगजवळील भीष्मकनगरचे अवशेष बारावे–सोळावे शतकातील आहेत, आणि नंतर अहोम. पश्चिमेकडील तवांग व मोनपा भागांचे तिबेटशी जवळचे धार्मिक संबंध होते; तवांग मठाची स्थापना 1680 च्या दशकात झाली, आणि सहाव्या दलाई लामांचा जन्म तवांगजवळ झाला. ब्रिटिश राजवटीत 1873 च्या इनर लाइनने मैदानांतून प्रवेश मर्यादित केला, आणि 1914 च्या शिमला परिषदेत ठरलेल्या मॅकमहॉन रेषेने तिबेटशी सीमा आखली.\n\nस्वातंत्र्यानंतर या प्रदेशाचा कारभार शिलाँग व नंतर इटानगरहून नॉर्थ-ईस्ट फ्रंटियर एजन्सी (नेफा) म्हणून झाला, ज्यात आसामचे राज्यपाल राष्ट्रपतींच्या वतीने काम पाहत. 1962 च्या चीन युद्धात चिनी सैन्य प्रदेशाच्या काही भागांत पुढे आले व नंतर मागे गेले. 20 जानेवारी 1972 रोजी नेफा हा अरुणाचल प्रदेश केंद्रशासित प्रदेश झाला आणि 20 फेब्रुवारी 1987 रोजी राज्य."),
        conf="Editorial"),
    timeline([
        ev("bhismak", 1200, L("12th–16th century", "12वीं–16वीं सदी", "बारावे–सोळावे शतक"), L("Chutiya-era fort and city at Bhismaknagar", "भीष्मकनगर में चुटिया काल का क़िला और नगर", "भीष्मकनगर येथे चुटियाकालीन किल्ला व नगर")),
        ev("tawang", 1680, L("1680s", "1680 का दशक", "1680 चे दशक"), L("Tawang monastery founded", "तवांग मठ की स्थापना", "तवांग मठाची स्थापना")),
        ev("innerline", 1873, L("1873", "1873", "1873"), L("Inner Line Regulation", "इनर लाइन विनियम", "इनर लाइन नियमन")),
        ev("mcmahon", 1914, L("1914", "1914", "1914"), L("McMahon Line agreed at the Simla Conference", "शिमला सम्मेलन में मैकमोहन रेखा तय", "शिमला परिषदेत मॅकमहॉन रेषा ठरली")),
        ev("nefa", 1954, L("1954", "1954", "1954"), L("North-East Frontier Agency (NEFA) named", "नॉर्थ-ईस्ट फ़्रंटियर एजेंसी (नेफ़ा) नामकरण", "नॉर्थ-ईस्ट फ्रंटियर एजन्सी (नेफा) नामकरण")),
        ev("ut", 1972, L("20 January 1972", "20 जनवरी 1972", "20 जानेवारी 1972"), L("Union Territory of Arunachal Pradesh", "अरुणाचल प्रदेश केंद्र शासित प्रदेश", "अरुणाचल प्रदेश केंद्रशासित प्रदेश")),
        ev("state", 1987, L("20 February 1987", "20 फ़रवरी 1987", "20 फेब्रुवारी 1987"), L("Arunachal Pradesh becomes a State", "अरुणाचल प्रदेश राज्य बना", "अरुणाचल प्रदेश राज्य झाले")),
        ev("airport", 2022, L("19 November 2022", "19 नवंबर 2022", "19 नोव्हेंबर 2022"), L("Donyi Polo Airport opens near Itanagar", "ईटानगर के पास दोन्यी पोलो हवाई अड्डा खुला", "इटानगरजवळ दोन्यी पोलो विमानतळ सुरू")),
        ev("sela", 2024, L("9 March 2024", "9 मार्च 2024", "9 मार्च 2024"), L("Sela Tunnel opened", "सेला सुरंग खुली", "सेला बोगदा सुरू")),
    ]),
    lst("heritage", [
        it3("tawangmon", "Tawang Monastery", "तवांग मठ", "तवांग मठ", m=("Gelug monastery, 1680s", "गेलुग मठ, 1680 का दशक", "गेलुग मठ, 1680 चे दशक")),
        it3("bhismak", "Bhismaknagar", "भीष्मकनगर", "भीष्मकनगर", m=("Archaeological site near Roing", "रोइंग के पास पुरातात्विक स्थल", "रोइंगजवळील पुरातत्त्वीय स्थळ")),
        it3("ita", "Ita Fort, Itanagar", "ईटा क़िला, ईटानगर", "इटा किल्ला, इटानगर", m=("Brick fort that gives the capital its name", "ईंटों का क़िला जिससे राजधानी का नाम पड़ा", "विटांचा किल्ला, ज्यावरून राजधानीचे नाव")),
        it3("malinithan", "Malinithan", "मालिनीथान", "मालिनीथान", m=("Temple ruins near Likabali", "लिकाबाली के पास मंदिर के खंडहर", "लिकाबालीजवळील मंदिर अवशेष")),
        it3("urgelling", "Urgelling Monastery", "उरगेलिंग मठ", "उरगेलिंग मठ", m=("Birthplace of the sixth Dalai Lama", "छठे दलाई लामा का जन्मस्थान", "सहाव्या दलाई लामांचे जन्मस्थान")),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
    gaps("g", [
        (L("Ziro valley (Apatani cultural landscape) — UNESCO Tentative List entry", "ज़ीरो घाटी (अपातानी सांस्कृतिक भूदृश्य) — यूनेस्को संभावित सूची", "झिरो खोरे (आपातानी सांस्कृतिक भूदृश्य) — युनेस्को संभाव्य यादी"), "unesco-whc", "Confirm the Tentative List entry on whc.unesco.org."),
    ]),
])
print("ar mod1 ok")
