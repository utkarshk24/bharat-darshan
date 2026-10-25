"""Meghalaya modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-ML"
ml = read("regions/IN-ML.json")["metrics"]; ind = read("india.json")["metrics"]
C = research("census_b5plus.json"); F = C["forest"]["ML"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About 76% of Meghalaya is forest (ISFR 2023), and most of it belongs to clans, villages and the District Councils rather than the State. Sacred groves (law kyntang), protected by custom for centuries, survive around villages such as Mawphlang. Nokrek, the peak of the Garo Hills and home of the wild ancestor of the citrus fruits, is a national park and a UNESCO biosphere reserve; Balpakram's plateau and gorges in South Garo Hills form another national park, and Siju, Nongkhyllem and Baghmara (for pitcher plants) are sanctuaries. Wildlife includes Asian elephants, the clouded leopard (State animal), the western hoolock gibbon, the hill myna (State bird) and many orchids, among them the endemic pitcher plant Nepenthes khasiana.\n\nThere are no Ramsar sites in Meghalaya on the list as on 21 April 2026.",
        "मेघालय का लगभग 76% भाग वन है (आईएसएफ़आर 2023), और इसका अधिकांश भाग राज्य के बजाय कुलों, गाँवों और ज़िला परिषदों का है। सदियों से परंपरा द्वारा संरक्षित पवित्र उपवन (लॉ किंताङ) माफ़लांग जैसे गाँवों के आसपास बचे हैं। गारो पहाड़ियों की चोटी नोकरेक, जो खट्टे फलों के जंगली पूर्वज का घर है, राष्ट्रीय उद्यान और यूनेस्को जैवमंडल आरक्षित क्षेत्र है; दक्षिण गारो हिल्स में बालपाक्रम का पठार और खड्ड एक और राष्ट्रीय उद्यान बनाते हैं, और सिजू, नोंगख्यल्लेम और बाघमारा (घटपर्णी पौधों के लिए) अभयारण्य हैं। वन्यजीवों में एशियाई हाथी, धूमिल तेंदुआ (राज्य पशु), पश्चिमी हूलॉक गिबन, पहाड़ी मैना (राज्य पक्षी) और कई ऑर्किड शामिल हैं, और स्थानिक घटपर्णी पौधा नेपेंथीस खासियाना भी।\n\n21 अप्रैल 2026 की सूची में मेघालय में कोई रामसर स्थल नहीं है।",
        "मेघालयाचा सुमारे 76% भाग वनाच्छादित आहे (आयएसएफआर 2023), आणि त्यातील बहुतांश राज्याऐवजी कुळे, गावे व जिल्हा परिषदांच्या मालकीचा आहे. शतकानुशतके परंपरेने जपलेल्या देवराया (लॉ किंताङ) माफलांगसारख्या गावांभोवती टिकून आहेत. गारो टेकड्यांचे शिखर नोकरेक, लिंबूवर्गीय फळांच्या रानटी पूर्वजाचे घर, राष्ट्रीय उद्यान व युनेस्को जैवमंडल राखीव क्षेत्र आहे; दक्षिण गारो हिल्समधील बालपाक्रमचे पठार व दऱ्या आणखी एक राष्ट्रीय उद्यान बनवतात, आणि सिजू, नोंगख्यल्लेम व बाघमारा (घटपर्णी वनस्पतींसाठी) ही अभयारण्ये आहेत. वन्यजीवांत आशियाई हत्ती, ढगाळ बिबट्या (राज्यप्राणी), पश्चिमी हूलॉक गिबन, डोंगरी मैना (राज्यपक्षी) व अनेक ऑर्किड आहेत, तसेच स्थानिक घटपर्णी वनस्पती नेपेंथिस खासियाना.\n\n21 एप्रिल 2026 च्या यादीत मेघालयात कोणतेही रामसर स्थळ नाही."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), ml["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(0, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: none in Meghalaya."), "number"),
    ]),
    lst("protected", [
        it3("nokrek", "Nokrek National Park and Biosphere Reserve", "नोकरेक राष्ट्रीय उद्यान और जैवमंडल आरक्षित क्षेत्र", "नोकरेक राष्ट्रीय उद्यान व जैवमंडल राखीव क्षेत्र", m=("Garo Hills", "गारो पहाड़ियाँ", "गारो टेकड्या")),
        it3("balpakram", "Balpakram National Park", "बालपाक्रम राष्ट्रीय उद्यान", "बालपाक्रम राष्ट्रीय उद्यान", m=("South Garo Hills", "दक्षिण गारो हिल्स", "दक्षिण गारो हिल्स")),
        it3("nongkhyllem", "Nongkhyllem Wildlife Sanctuary", "नोंगख्यल्लेम वन्यजीव अभयारण्य", "नोंगख्यल्लेम वन्यजीव अभयारण्य", m=("Ri-Bhoi", "री-भोई", "री-भोई")),
        it3("siju", "Siju Wildlife Sanctuary", "सिजू वन्यजीव अभयारण्य", "सिजू वन्यजीव अभयारण्य", m=("Next to Siju caves", "सिजू गुफाओं के पास", "सिजू गुहांजवळ")),
        it3("mawphlang", "Mawphlang sacred forest", "माफ़लांग पवित्र वन", "माफलांग देवराई", m=("Community-protected", "समुदाय द्वारा संरक्षित", "समुदायाने संरक्षित")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("leopard", "Clouded leopard (State animal)", "धूमिल तेंदुआ (राज्य पशु)", "ढगाळ बिबट्या (राज्यप्राणी)"), it3("myna", "Hill myna (State bird)", "पहाड़ी मैना (राज्य पक्षी)", "डोंगरी मैना (राज्यपक्षी)"),
        it3("elephant", "Asian elephant", "एशियाई हाथी", "आशियाई हत्ती"), it3("gibbon", "Western hoolock gibbon", "पश्चिमी हूलॉक गिबन", "पश्चिमी हूलॉक गिबन"),
        it3("pitcher", "Khasi pitcher plant", "खासी घटपर्णी पौधा", "खासी घटपर्णी वनस्पती"), it3("orchid", "Lady's slipper orchid (State flower)", "लेडीज़ स्लिपर ऑर्किड (राज्य पुष्प)", "लेडीज स्लिपर ऑर्किड (राज्यपुष्प)"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Community and clan forests — official area", "सामुदायिक और कुल वन — आधिकारिक क्षेत्रफल", "सामुदायिक व कुळ वने — अधिकृत क्षेत्रफळ"), "fsi", "ISFR State chapter / Meghalaya Forest Department."),
        (L("Nokrek biosphere reserve — UNESCO designation link", "नोकरेक जैवमंडल — यूनेस्को पदनाम लिंक", "नोकरेक जैवमंडल — युनेस्को नियुक्ती दुवा"), "unesco-whc", "UNESCO Man and the Biosphere directory."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Despite its rain, Meghalaya faces dry-season water shortages: water runs off the steep, often deforested slopes quickly, and Sohra itself has struggled for drinking water in winter. Shillong is supplied by the Greater Shillong water supply scheme and springs, and Umiam lake stores water for power and is threatened by silt and pollution. Villages rely on springs, and the State's spring-shed programme maps and protects them. Acid drainage from abandoned coal mines has polluted rivers such as the Lukha and Myntdu in the Jaintia Hills.",
        "वर्षा के बावजूद मेघालय को सूखे मौसम में पानी की कमी झेलनी पड़ती है: खड़ी, अक्सर वनविहीन ढलानों से पानी जल्दी बह जाता है, और स्वयं सोहरा में सर्दियों में पीने के पानी की कठिनाई रही है। शिलांग को ग्रेटर शिलांग जल आपूर्ति योजना और झरनों से पानी मिलता है, और उमियम झील बिजली के लिए पानी संचित करती है और गाद व प्रदूषण से संकट में है। गाँव झरनों पर निर्भर हैं, और राज्य का स्प्रिंग-शेड कार्यक्रम उनका मानचित्रण और संरक्षण करता है। छोड़ी गई कोयला खदानों के अम्लीय बहाव ने जयंतिया पहाड़ियों की लुखा और मिंतदू जैसी नदियों को प्रदूषित किया है।",
        "पाऊस असूनही मेघालयाला कोरड्या ऋतूत पाणीटंचाई जाणवते: तीव्र, अनेकदा वृक्षतोड झालेल्या उतारांवरून पाणी पटकन वाहून जाते, आणि खुद्द सोहराला हिवाळ्यात पिण्याच्या पाण्याची अडचण आली आहे. शिलाँगला ग्रेटर शिलाँग पाणीपुरवठा योजना व झऱ्यांतून पाणी मिळते, आणि उमियम सरोवर विजेसाठी पाणी साठवते व गाळ आणि प्रदूषणाने धोक्यात आहे. गावे झऱ्यांवर अवलंबून आहेत, आणि राज्याचा स्प्रिंग-शेड कार्यक्रम त्यांचे नकाशांकन व संरक्षण करतो. सोडून दिलेल्या कोळसा खाणींतील आम्लयुक्त निचऱ्याने जयंतिया टेकड्यांतील लुखा व मिंतदूसारख्या नद्या प्रदूषित केल्या आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Household tap-water coverage", "घरेलू नल जल कवरेज", "घरगुती नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
        (L("River water quality (Lukha, Myntdu)", "नदी जल गुणवत्ता (लुखा, मिंतदू)", "नदी पाण्याची गुणवत्ता (लुखा, मिंतदू)"), "india-gov", "Meghalaya State Pollution Control Board / CPCB."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Meghalaya lies in seismic zone V; the great Assam earthquake of 1897 had its epicentre under the Shillong plateau. Landslides and flash floods are common in the monsoon, especially on the roads to Sohra and Dawki and on NH-6, and the slopes and caves become dangerous after heavy rain. Visitors should check weather warnings, use registered guides for caving and long treks, and follow local rules at waterfalls, rivers and sacred groves.",
        "मेघालय भूकंपीय क्षेत्र V में है; 1897 के महान असम भूकंप का केंद्र शिलांग पठार के नीचे था। मानसून में भूस्खलन और अचानक बाढ़ आम हैं, विशेषकर सोहरा और दावकी की सड़कों और एनएच-6 पर, और भारी वर्षा के बाद ढलानें और गुफाएँ ख़तरनाक हो जाती हैं। पर्यटकों को मौसम चेतावनियाँ देखनी चाहिए, गुफा यात्रा और लंबे ट्रेक के लिए पंजीकृत गाइड लेने चाहिए, और झरनों, नदियों और पवित्र उपवनों में स्थानीय नियमों का पालन करना चाहिए।",
        "मेघालय भूकंप क्षेत्र V मध्ये आहे; 1897 च्या महान आसाम भूकंपाचे केंद्र शिलाँग पठाराखाली होते. पावसाळ्यात भूस्खलन व अचानक पूर सामान्य आहेत, विशेषतः सोहरा व दावकीच्या रस्त्यांवर आणि एनएच-6 वर, आणि मुसळधार पावसानंतर उतार व गुहा धोकादायक होतात. पर्यटकांनी हवामान इशारे पाहावेत, गुहा भ्रमंती व लांब ट्रेकसाठी नोंदणीकृत मार्गदर्शक घ्यावेत, आणि धबधबे, नद्या व देवरायांमध्ये स्थानिक नियमांचे पालन करावे."),
        conf="Editorial"),
    emergency_table(("Meghalaya", "मेघालय", "मेघालय")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Seismic zone — BIS map reference", "भूकंपीय क्षेत्र — बीआईएस मानचित्र संदर्भ", "भूकंप क्षेत्र — बीआयएस नकाशा संदर्भ"), "bis", "IS 1893 seismic zoning map."),
        (L("Registered tourist guides — official list", "पंजीकृत पर्यटक गाइड — आधिकारिक सूची", "नोंदणीकृत पर्यटक मार्गदर्शक — अधिकृत यादी"), "tourism", "Meghalaya Tourism Department."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Eight GIs belong to Meghalaya on the GI Registry's list as on 31 December 2025. Memong narang, a wild orange of the Garo Hills, and Khasi mandarin were registered in 2013 and Lakadong turmeric in 2021. In 2023 five more followed: Garo textiles, Ryndia (eri silk) textiles, Khasi handloom products, Lyrnai pottery and Chubitchi, the Garo rice drink.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में आठ जीआई मेघालय के हैं। गारो पहाड़ियों का जंगली संतरा मेमोंग नारंग और खासी संतरा 2013 में और लाकाडोंग हल्दी 2021 में पंजीकृत हुए। 2023 में पाँच और आए: गारो वस्त्र, रिंदिया (एरी रेशम) वस्त्र, खासी हथकरघा उत्पाद, लिरनाई मिट्टी के बर्तन और गारो चावल पेय चुबित्ची।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत आठ जीआय मेघालयाचे आहेत. गारो टेकड्यांचे रानटी संत्रे मेमोंग नारंग व खासी संत्रे 2013 मध्ये आणि लाकाडोंग हळद 2021 मध्ये नोंदणीकृत झाली. 2023 मध्ये आणखी पाच आले: गारो वस्त्रे, रिंदिया (एरी रेशीम) वस्त्रे, खासी हातमाग उत्पादने, लिरनाई मातीची भांडी व गारो तांदळाचे पेय चुबित्ची."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Pending GI applications from Meghalaya", "मेघालय के लंबित जीआई आवेदन", "मेघालयाचे प्रलंबित जीआय अर्ज"), "gi-registry", "GI Registry application status search."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Shillong is the base for most visitors: Ward's Lake, the Don Bosco Museum, Shillong Peak, Elephant Falls and the cafés of Police Bazaar and Laitumkhrah. South of the city, Sohra has the Nohkalikai and Seven Sisters falls, the Mawsmai cave and the trek down to the double-decker living root bridge at Nongriat; Laitlum canyons and the Mawphlang sacred forest are close by. Further east, Mawlynnong village and the Umngot river at Dawki and Shnongpdeng draw large crowds, and the Jaintia Hills have the Nartiang monoliths and the Krang Suri falls. In the west, Tura is the gateway to Nokrek, Balpakram and the Siju caves.",
        "अधिकांश पर्यटकों के लिए शिलांग आधार है: वार्ड्स झील, डॉन बॉस्को संग्रहालय, शिलांग पीक, एलिफ़ेंट फ़ॉल्स और पुलिस बाज़ार व लैतुमख्राह के कैफ़े। शहर के दक्षिण में सोहरा में नोहकलिकाई और सेवन सिस्टर्स जलप्रपात, मावस्माई गुफा और नोंग्रियात के दोमंज़िला जीवित जड़ पुल तक नीचे का ट्रेक है; लाइटलुम घाटियाँ और माफ़लांग पवित्र वन पास ही हैं। आगे पूर्व में मावलिननोंग गाँव और दावकी व श्नोंगपदेंग में उमंगोट नदी भारी भीड़ खींचते हैं, और जयंतिया पहाड़ियों में नारतियांग एकाश्म और क्रांग सूरी जलप्रपात हैं। पश्चिम में तुरा नोकरेक, बालपाक्रम और सिजू गुफाओं का प्रवेश द्वार है।",
        "बहुतेक पर्यटकांसाठी शिलाँग हा तळ आहे: वॉर्ड्स सरोवर, डॉन बॉस्को संग्रहालय, शिलाँग पीक, एलिफंट फॉल्स व पोलीस बाजार आणि लैतुमख्राहमधील कॅफे. शहराच्या दक्षिणेला सोहरामध्ये नोहकलिकाई व सेव्हन सिस्टर्स धबधबे, मावस्माई गुहा व नोंग्रियातच्या दुमजली जिवंत मुळांच्या पुलापर्यंत खाली उतरणारा ट्रेक आहे; लाइटलुम दऱ्या व माफलांग देवराई जवळच आहेत. पुढे पूर्वेला मावलिननोंग गाव आणि दावकी व श्नोंगपदेंग येथील उमंगोट नदी मोठी गर्दी खेचतात, आणि जयंतिया टेकड्यांत नारतियांग एकाश्म स्तंभ व क्रांग सूरी धबधबा आहेत. पश्चिमेला तुरा हे नोकरेक, बालपाक्रम व सिजू गुहांचे प्रवेशद्वार आहे."),
        conf="Editorial"),
    lst("places", [
        it3("shillong", "Shillong", "शिलांग", "शिलाँग", m=("Capital; music and cafés", "राजधानी; संगीत और कैफ़े", "राजधानी; संगीत व कॅफे")),
        it3("sohra", "Sohra (Cherrapunji)", "सोहरा (चेरापूंजी)", "सोहरा (चेरापुंजी)", m=("Waterfalls and caves", "जलप्रपात और गुफाएँ", "धबधबे व गुहा")),
        it3("nongriat", "Nongriat", "नोंग्रियात", "नोंग्रियात", m=("Double-decker root bridge", "दोमंज़िला जड़ पुल", "दुमजली मुळांचा पूल")),
        it3("dawki", "Dawki and Shnongpdeng", "दावकी और श्नोंगपदेंग", "दावकी व श्नोंगपदेंग", m=("Umngot river", "उमंगोट नदी", "उमंगोट नदी")),
        it3("mawlynnong", "Mawlynnong", "मावलिननोंग", "मावलिननोंग", m=("Village known for cleanliness", "स्वच्छता के लिए प्रसिद्ध गाँव", "स्वच्छतेसाठी प्रसिद्ध गाव")),
        it3("nokrek", "Tura and Nokrek", "तुरा और नोकरेक", "तुरा व नोकरेक", m=("Garo Hills", "गारो पहाड़ियाँ", "गारो टेकड्या")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Shillong, then a day each at Sohra and at Dawki–Mawlynnong.", "शिलांग, फिर एक-एक दिन सोहरा और दावकी–मावलिननोंग में।", "शिलाँग, मग एक-एक दिवस सोहरा व दावकी–मावलिननोंगमध्ये.")),
        it3("d6", "6 days", "6 दिन", "6 दिवस", d=("Add a night at Nongriat for the root bridges and a day in the Jaintia Hills.", "जड़ पुलों के लिए नोंग्रियात में एक रात और जयंतिया पहाड़ियों में एक दिन जोड़ें।", "मुळांच्या पुलांसाठी नोंग्रियातमध्ये एक रात्र व जयंतिया टेकड्यांत एक दिवस जोडा.")),
        it3("garo", "Garo Hills (4 days)", "गारो पहाड़ियाँ (4 दिन)", "गारो टेकड्या (4 दिवस)", d=("Tura, Nokrek and Balpakram; time a visit with Wangala in November.", "तुरा, नोकरेक और बालपाक्रम; नवंबर में वांगला के समय जाएँ।", "तुरा, नोकरेक व बालपाक्रम; नोव्हेंबरमधील वांगलाच्या वेळी भेट द्या.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    gaps("g", [
        (L("Tourist arrivals by year", "वर्षवार पर्यटक आगमन", "वर्षनिहाय पर्यटक आगमन"), "tourism", "Meghalaya Tourism Department / India Tourism Statistics."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "cities", [
    lst("cities", [
        city("shillong", ("Shillong", "शिलांग", "शिलाँग"), ("Capital on the Khasi Hills plateau.", "खासी पहाड़ियों के पठार पर राजधानी।", "खासी टेकड्यांच्या पठारावरील राजधानी."), ("Capital", "राजधानी", "राजधानी")),
        city("tura", ("Tura", "तुरा", "तुरा"), ("Main town of the Garo Hills.", "गारो पहाड़ियों का मुख्य नगर।", "गारो टेकड्यांचे मुख्य शहर."), ("Administration", "प्रशासन", "प्रशासन")),
        city("jowai", ("Jowai", "जोवाई", "जोवाई"), ("Headquarters of West Jaintia Hills.", "पश्चिम जयंतिया हिल्स का मुख्यालय।", "पश्चिम जयंतिया हिल्सचे मुख्यालय."), ("Culture", "संस्कृति", "संस्कृती")),
        city("nongpoh", ("Nongpoh", "नोंगपोह", "नोंगपोह"), ("Ri-Bhoi town on the Guwahati road.", "गुवाहाटी मार्ग पर री-भोई का नगर।", "गुवाहाटी मार्गावरील री-भोईचे शहर."), ("Trade", "व्यापार", "व्यापार")),
        city("williamnagar", ("Williamnagar", "विलियमनगर", "विल्यमनगर"), ("East Garo Hills headquarters, named after Williamson Sangma.", "पूर्वी गारो हिल्स का मुख्यालय, विलियमसन संगमा के नाम पर।", "पूर्व गारो हिल्सचे मुख्यालय, विल्यमसन संगमांच्या नावाने."), ("Administration", "प्रशासन", "प्रशासन")),
        city("sohra", ("Sohra", "सोहरा", "सोहरा"), ("Escarpment town of waterfalls.", "झरनों वाला ढलान का नगर।", "धबधब्यांचे कड्यावरील शहर."), ("Tourism", "पर्यटन", "पर्यटन")),
    ], title=L("Major towns", "प्रमुख नगर", "प्रमुख शहरे"), conf="Editorial"),
    gaps("g", [
        (L("Town populations (Census 2011)", "नगरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Football is the most popular sport. Shillong Lajong FC won promotion to the I-League in 2009 and has produced many national-team players, and Shillong's Polo Grounds and JN Stadium host league and district matches. Archery has deep roots: teer, a daily lottery based on the number of arrows that hit a target, is shot in Shillong every afternoon except Sunday. Shillong was a co-host, with Guwahati, of the 12th South Asian Games in 2016.",
        "फ़ुटबॉल सबसे लोकप्रिय खेल है। शिलांग लाजोंग एफ़सी 2009 में आई-लीग में पहुँचा और इसने राष्ट्रीय टीम के कई खिलाड़ी दिए हैं, और शिलांग के पोलो ग्राउंड और जेएन स्टेडियम में लीग और ज़िला मैच होते हैं। तीरंदाज़ी की जड़ें गहरी हैं: तीर, लक्ष्य पर लगे तीरों की संख्या पर आधारित दैनिक लॉटरी, रविवार छोड़कर हर दोपहर शिलांग में चलाई जाती है। 2016 के 12वें दक्षिण एशियाई खेलों का गुवाहाटी के साथ शिलांग सह-मेज़बान था।",
        "फुटबॉल हा सर्वांत लोकप्रिय खेळ आहे. शिलाँग लाजोंग एफसी 2009 मध्ये आय-लीगमध्ये पोहोचला व त्याने राष्ट्रीय संघाचे अनेक खेळाडू दिले आहेत, आणि शिलाँगच्या पोलो ग्राउंड व जेएन स्टेडियमवर लीग व जिल्हा सामने होतात. धनुर्विद्येची मुळे खोल आहेत: तीर, लक्ष्यावर लागलेल्या बाणांच्या संख्येवर आधारित रोजची लॉटरी, रविवार वगळता दररोज दुपारी शिलाँगमध्ये खेळली जाते. 2016 च्या 12 व्या दक्षिण आशियाई खेळांचे गुवाहाटीसोबत शिलाँग सह-यजमान होते."),
        conf="Editorial"),
    gaps("g", [(L("Major stadiums — official list", "प्रमुख स्टेडियम — आधिकारिक सूची", "प्रमुख स्टेडियम — अधिकृत यादी"), "india-gov", "Meghalaya Sports and Youth Affairs Department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("tirot", ("U Tirot Sing", "उ तिरोत सिंह", "उ तिरोत सिंह"), ("Syiem of Nongkhlaw who led the Khasi resistance of 1829–33.", "नोंगख्लाव के स्येम जिन्होंने 1829–33 के खासी प्रतिरोध का नेतृत्व किया।", "नोंगख्लावचे स्येम ज्यांनी 1829–33 च्या खासी प्रतिकाराचे नेतृत्व केले."), ("History", "इतिहास", "इतिहास")),
        person("kiang", ("U Kiang Nangbah", "उ कियांग नांगबाह", "उ कियांग नांगबाह"), ("Jaintia leader executed by the British in 1862.", "जयंतिया नेता जिन्हें 1862 में अंग्रेज़ों ने फाँसी दी।", "जयंतिया नेते ज्यांना 1862 मध्ये ब्रिटिशांनी फाशी दिली."), ("History", "इतिहास", "इतिहास")),
        person("togan", ("Pa Togan Nengminza Sangma", "पा तोगन नेंगमिंजा संगमा", "पा तोगन नेंगमिंजा संगमा"), ("Garo warrior who fought British troops in 1872.", "गारो योद्धा जो 1872 में ब्रिटिश सेना से लड़े।", "गारो योद्धा जे 1872 मध्ये ब्रिटिश सैन्याशी लढले."), ("History", "इतिहास", "इतिहास")),
        person("williamson", ("Williamson A. Sangma", "विलियमसन ए. संगमा", "विल्यमसन ए. संगमा"), ("Leader of the hill State movement and first Chief Minister.", "पहाड़ी राज्य आंदोलन के नेता और पहले मुख्यमंत्री।", "डोंगरी राज्य चळवळीचे नेते व पहिले मुख्यमंत्री."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("pasangma", ("P. A. Sangma", "पी. ए. संगमा", "पी. ए. संगमा"), ("Speaker of the Lok Sabha (1996–98) and former Chief Minister.", "लोकसभा अध्यक्ष (1996–98) और पूर्व मुख्यमंत्री।", "लोकसभा अध्यक्ष (1996–98) व माजी मुख्यमंत्री."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("lou", ("Lou Majaw", "लू माजॉ", "लू माजॉ"), ("Shillong rock and blues musician.", "शिलांग के रॉक और ब्लूज़ संगीतकार।", "शिलाँगचे रॉक व ब्लूज संगीतकार."), ("Music", "संगीत", "संगीत")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Khasi and Garo communities also live in neighbouring Assam and across the border in Bangladesh's Sylhet and Mymensingh divisions. Many young people from Meghalaya study and work in Guwahati, Delhi, Bengaluru and other cities, especially in hospitality, aviation and services, and Shillong's musicians and choirs perform in India and abroad.",
        "खासी और गारो समुदाय पड़ोसी असम में और सीमा पार बांग्लादेश के सिलहट और मयमनसिंह मंडलों में भी रहते हैं। मेघालय के बहुत से युवा गुवाहाटी, दिल्ली, बेंगलुरु और अन्य नगरों में पढ़ते और काम करते हैं, विशेषकर आतिथ्य, विमानन और सेवाओं में, और शिलांग के संगीतकार और गायक मंडलियाँ भारत और विदेश में प्रस्तुति देते हैं।",
        "खासी व गारो समुदाय शेजारच्या आसाममध्ये आणि सीमेपलीकडे बांगलादेशच्या सिलहट व मयमनसिंह विभागांतही राहतात. मेघालयातील अनेक तरुण गुवाहाटी, दिल्ली, बंगळुरू व इतर शहरांत शिकतात व काम करतात, विशेषतः आतिथ्य, विमानवाहतूक व सेवा क्षेत्रांत, आणि शिलाँगचे संगीतकार व गायकवृंद भारतात व परदेशात सादरीकरण करतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Out-migration from the State — official estimate", "राज्य से बाहर प्रवास — आधिकारिक अनुमान", "राज्याबाहेर स्थलांतर — अधिकृत अंदाज"), "census", "Census 2011 migration tables (D-series)."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Meghalaya portal", "मेघालय सरकार पोर्टल", "मेघालय शासन संकेतस्थळ", url="https://meghalaya.gov.in", src="ml-gov"),
        it3("governor", "Lok Bhavan (Raj Bhavan), Shillong", "लोक भवन (राजभवन), शिलांग", "लोक भवन (राजभवन), शिलाँग", url="https://meggovernor.gov.in", src="ml-governor"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes", "एसटीडी कोड", "एसटीडी कोड"),
          [col(L("Area", "क्षेत्र", "क्षेत्र")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Shillong", "शिलांग", "शिलाँग"), "0364"], [L("Tura", "तुरा", "तुरा"), "03651"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय; दूरसंचार विभाग की नंबरिंग योजना से जाँचा जाएगा।", "संपादकीय; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळले जाईल.")),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("st", ("Scheduled Tribes made up 86.1% of Meghalaya's population in 2011.", "2011 में मेघालय की जनसंख्या में अनुसूचित जनजातियों का हिस्सा 86.1% था।", "2011 मध्ये मेघालयाच्या लोकसंख्येत अनुसूचित जमातींचा वाटा 86.1% होता."), "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf", "dl-planning"),
        triv("forest", ("About 76% of the State is forest (ISFR 2023).", "राज्य का लगभग 76% भाग वन है (आईएसएफ़आर 2023)।", "राज्याचा सुमारे 76% भाग वनाच्छादित आहे (आयएसएफआर 2023)."), LS_FOREST, "fsi"),
        triv("name", ("The name Meghalaya, 'abode of clouds', was coined from Sanskrit by the geographer S. P. Chatterjee.", "'बादलों का घर' अर्थ वाला नाम मेघालय भूगोलवेत्ता एस. पी. चटर्जी ने संस्कृत से गढ़ा था।", "'ढगांचे निवासस्थान' अर्थाचे मेघालय हे नाव भूगोलतज्ज्ञ एस. पी. चॅटर्जी यांनी संस्कृतमधून घडवले.")),
        triv("lakadong", ("Lakadong turmeric was registered as a GI on an application filed in 2021.", "लाकाडोंग हल्दी 2021 में दायर आवेदन पर जीआई के रूप में पंजीकृत हुई।", "लाकाडोंग हळद 2021 मध्ये दाखल अर्जावर जीआय म्हणून नोंदणीकृत झाली."), GI_PDF, "gi-registry"),
        triv("matrilineal", ("Khasi and Garo children take their mother's clan name.", "खासी और गारो बच्चे माँ का कुल नाम लेते हैं।", "खासी व गारो मुले आईचे कुळनाव घेतात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("ml mod3 ok")
