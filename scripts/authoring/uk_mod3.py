"""Uttarakhand modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-UK"
uk = read("regions/IN-UK.json")["metrics"]; ind = read("india.json")["metrics"]
C = research("census_b5plus.json"); F = C["forest"]["UK"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Forests cover about 45% of Uttarakhand (ISFR 2023) — sal in the Terai and Bhabar, chir pine and banj oak in the middle hills, and deodar, fir, birch and rhododendron higher up, giving way to alpine bugyals (meadows) below the snow line. Jim Corbett National Park, established in 1936 as Hailey National Park, was India's first national park and is a major tiger reserve, and Rajaji National Park around Haridwar protects elephants and tigers. The Nanda Devi and Valley of Flowers national parks together form a UNESCO World Heritage site, famous for snow leopards, Himalayan musk deer and alpine flowers. The Askot and Kedarnath sanctuaries, Gangotri National Park and Govind Pashu Vihar protect the high Himalaya.\n\nThe State has one Ramsar site: the Asan Conservation Reserve near Dehradun, where the Asan river meets the Yamuna, a wintering ground for waterbirds.",
        "उत्तराखंड का लगभग 45% भाग वन है (आईएसएफ़आर 2023) — तराई और भाबर में साल, मध्य पहाड़ियों में चीड़ और बाँज, और ऊपर देवदार, फ़र, भोजपत्र और बुरांस, जो हिम रेखा के नीचे अल्पाइन बुग्यालों (घास के मैदानों) में बदल जाते हैं। 1936 में हेली राष्ट्रीय उद्यान के रूप में स्थापित जिम कॉर्बेट राष्ट्रीय उद्यान भारत का पहला राष्ट्रीय उद्यान था और एक प्रमुख बाघ अभयारण्य है, और हरिद्वार के आसपास का राजाजी राष्ट्रीय उद्यान हाथियों और बाघों को संरक्षण देता है। नंदा देवी और फूलों की घाटी राष्ट्रीय उद्यान मिलकर यूनेस्को विश्व धरोहर स्थल हैं, जो हिम तेंदुओं, हिमालयी कस्तूरी मृग और अल्पाइन फूलों के लिए प्रसिद्ध हैं। अस्कोट और केदारनाथ अभयारण्य, गंगोत्री राष्ट्रीय उद्यान और गोविंद पशु विहार ऊँचे हिमालय को संरक्षित करते हैं।\n\nराज्य में एक रामसर स्थल है: देहरादून के पास आसन संरक्षण आरक्षित क्षेत्र, जहाँ आसन नदी यमुना से मिलती है और जो जलपक्षियों का शीतकालीन ठिकाना है।",
        "उत्तराखंडचा सुमारे 45% भाग वनाच्छादित आहे (आयएसएफआर 2023) — तराई व भाबरमध्ये साल, मधल्या टेकड्यांत चीड पाइन व बांज ओक, आणि वर देवदार, फर, भूर्जपत्र व र्‍होडोडेंड्रॉन, जे हिमरेषेखाली अल्पाइन बुग्यालांत (कुरणांत) रूपांतरित होतात. 1936 मध्ये हेली राष्ट्रीय उद्यान म्हणून स्थापन झालेले जिम कॉर्बेट राष्ट्रीय उद्यान हे भारताचे पहिले राष्ट्रीय उद्यान होते आणि प्रमुख व्याघ्र प्रकल्प आहे, आणि हरिद्वारभोवतीचे राजाजी राष्ट्रीय उद्यान हत्ती व वाघांचे संरक्षण करते. नंदादेवी व फुलांचे खोरे राष्ट्रीय उद्याने मिळून युनेस्को जागतिक वारसा स्थळ आहेत, जे हिमबिबटे, हिमालयीन कस्तुरी मृग व अल्पाइन फुलांसाठी प्रसिद्ध आहे. अस्कोट व केदारनाथ अभयारण्ये, गंगोत्री राष्ट्रीय उद्यान व गोविंद पशुविहार उंच हिमालयाचे संरक्षण करतात.\n\nराज्यात एक रामसर स्थळ आहे: डेहराडूनजवळील आसन संवर्धन राखीव क्षेत्र, जिथे आसन नदी यमुनेला मिळते आणि जे पाणपक्ष्यांचे हिवाळी ठिकाण आहे."),
        sources=["fsi", "indian-wetlands", "unesco-whc"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), uk["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(1, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: Asan Conservation Reserve, designated 21 July 2020, 444 ha."), "number"),
    ]),
    lst("protected", [
        it3("corbett", "Jim Corbett National Park", "जिम कॉर्बेट राष्ट्रीय उद्यान", "जिम कॉर्बेट राष्ट्रीय उद्यान", m=("India's first national park (1936); tiger reserve", "भारत का पहला राष्ट्रीय उद्यान (1936); बाघ अभयारण्य", "भारताचे पहिले राष्ट्रीय उद्यान (1936); व्याघ्र प्रकल्प")),
        it3("rajaji", "Rajaji National Park", "राजाजी राष्ट्रीय उद्यान", "राजाजी राष्ट्रीय उद्यान", m=("Elephants and tigers", "हाथी और बाघ", "हत्ती व वाघ")),
        it3("nandadevi", "Nanda Devi and Valley of Flowers National Parks", "नंदा देवी और फूलों की घाटी राष्ट्रीय उद्यान", "नंदादेवी व फुलांचे खोरे राष्ट्रीय उद्याने", m=("UNESCO World Heritage", "यूनेस्को विश्व धरोहर", "युनेस्को जागतिक वारसा")),
        it3("gangotri", "Gangotri National Park", "गंगोत्री राष्ट्रीय उद्यान", "गंगोत्री राष्ट्रीय उद्यान", m=("Snow leopard, bharal", "हिम तेंदुआ, भरल", "हिमबिबट्या, भरल")),
        it3("askot", "Askot Wildlife Sanctuary", "अस्कोट वन्यजीव अभयारण्य", "अस्कोट वन्यजीव अभयारण्य", m=("Musk deer", "कस्तूरी मृग", "कस्तुरी मृग")),
        it3("asan", "Asan Conservation Reserve", "आसन संरक्षण आरक्षित क्षेत्र", "आसन संवर्धन राखीव क्षेत्र", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("musk", "Alpine musk deer (State animal)", "कस्तूरी मृग (राज्य पशु)", "कस्तुरी मृग (राज्यप्राणी)"), it3("monal", "Himalayan monal (State bird)", "मोनाल (राज्य पक्षी)", "मोनाल (राज्यपक्षी)"),
        it3("tiger", "Bengal tiger", "बाघ", "वाघ"), it3("elephant", "Asian elephant", "एशियाई हाथी", "आशियाई हत्ती"),
        it3("snowleopard", "Snow leopard", "हिम तेंदुआ", "हिमबिबट्या"), it3("brahmakamal", "Brahma kamal (State flower)", "ब्रह्म कमल (राज्य पुष्प)", "ब्रह्मकमळ (राज्यपुष्प)"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger count (All India Tiger Estimation)", "बाघों की संख्या (अखिल भारतीय बाघ आकलन)", "वाघांची संख्या (अखिल भारतीय व्याघ्र गणना)"), "ntca", "NTCA Status of Tigers report, Uttarakhand chapter."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Uttarakhand holds the headwaters of the Ganga and the Yamuna. The Gangotri glacier at Gaumukh feeds the Bhagirathi, the Alaknanda rises below Satopanth, and their tributaries meet at the five prayags — Vishnuprayag, Nandprayag, Karnaprayag, Rudraprayag and Devprayag. The Tehri dam on the Bhagirathi, one of the tallest in India, stores water for power, irrigation and drinking water for Delhi and Uttar Pradesh, and barrages at Pashulok and Haridwar divert water into the Upper Ganga canal. Hill villages depend on springs (naula and dhara), many of which are reported to be drying. Disasters linked to water have been severe: the Kedarnath flood of June 2013, the Chamoli flood of February 2021 after a rock and ice avalanche, and the land subsidence at Joshimath in 2023.",
        "उत्तराखंड में गंगा और यमुना के उद्गम हैं। गौमुख में गंगोत्री हिमनद भागीरथी को पानी देता है, अलकनंदा सतोपंथ के नीचे से निकलती है, और उनकी सहायक नदियाँ पाँच प्रयागों — विष्णुप्रयाग, नंदप्रयाग, कर्णप्रयाग, रुद्रप्रयाग और देवप्रयाग — पर मिलती हैं। भागीरथी पर भारत के सबसे ऊँचे बाँधों में से एक टिहरी बाँध बिजली, सिंचाई और दिल्ली व उत्तर प्रदेश के पेयजल के लिए पानी जमा करता है, और पशुलोक और हरिद्वार के बैराज ऊपरी गंगा नहर में पानी मोड़ते हैं। पहाड़ी गाँव नौलों और धारों (झरनों) पर निर्भर हैं, जिनमें से बहुतों के सूखने की ख़बरें हैं। पानी से जुड़ी आपदाएँ गंभीर रही हैं: जून 2013 की केदारनाथ बाढ़, फ़रवरी 2021 में चट्टान और बर्फ़ के हिमस्खलन के बाद चमोली की बाढ़, और 2023 में जोशीमठ में भू-धँसाव।",
        "उत्तराखंडमध्ये गंगा व यमुनेचे उगम आहेत. गौमुख येथील गंगोत्री हिमनदी भागीरथीला पाणी देते, अलकनंदा सतोपंथखाली उगम पावते, आणि त्यांच्या उपनद्या पाच प्रयागांवर — विष्णुप्रयाग, नंदप्रयाग, कर्णप्रयाग, रुद्रप्रयाग व देवप्रयाग — मिळतात. भागीरथीवरील भारतातील सर्वांत उंच धरणांपैकी एक टिहरी धरण वीज, सिंचन व दिल्ली आणि उत्तर प्रदेशच्या पिण्याच्या पाण्यासाठी पाणी साठवते, आणि पशुलोक व हरिद्वार येथील बंधारे वरच्या गंगा कालव्यात पाणी वळवतात. डोंगरी गावे नौले व धारे (झरे) यांवर अवलंबून आहेत, ज्यांपैकी अनेक आटत असल्याचे सांगितले जाते. पाण्याशी संबंधित आपत्ती गंभीर राहिल्या आहेत: जून 2013 चा केदारनाथ पूर, फेब्रुवारी 2021 मध्ये खडक व बर्फाच्या हिमस्खलनानंतरचा चमोली पूर, आणि 2023 मध्ये जोशीमठ येथील भूस्खलनसदृश जमीन खचणे."),
        conf="Editorial"),
    gaps("g", [
        (L("Deaths and damage in the 2013 Kedarnath flood — official figures", "2013 केदारनाथ बाढ़ में मृत्यु और नुकसान — आधिकारिक आँकड़े", "2013 केदारनाथ पुरातील मृत्यू व नुकसान — अधिकृत आकडे"), "ndma", "NDMA / Uttarakhand Disaster Management Authority reports."),
        (L("Spring rejuvenation and drinking-water coverage", "झरना पुनर्जीवन और पेयजल कवरेज", "झरा पुनरुज्जीवन व पेयजल व्याप्ती"), "india-gov", "SARRA / Jal Jeevan Mission dashboard."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Uttarakhand is highly exposed to natural hazards. Much of it lies in the highest earthquake zones — the Uttarkashi (1991) and Chamoli (1999) earthquakes caused heavy loss of life — and the monsoon brings cloudbursts, landslides and flash floods that block roads and sweep away riverside buildings. Forest fires are common in the dry months of April–June, glacial lake outbursts and avalanches are risks in the high valleys, and human–wildlife conflict with leopards and elephants occurs near forests. Pilgrims to the Char Dham must register with the State before travel, should check weather and road advisories, and should allow time to acclimatise at Kedarnath, Hemkund Sahib and other high shrines.",
        "उत्तराखंड प्राकृतिक आपदाओं के प्रति अत्यधिक संवेदनशील है। इसका अधिकांश भाग सबसे ऊँचे भूकंपीय क्षेत्रों में है — उत्तरकाशी (1991) और चमोली (1999) के भूकंपों में भारी जनहानि हुई — और मानसून बादल फटना, भूस्खलन और अचानक बाढ़ लाता है जो सड़कें रोकते हैं और नदी किनारे की इमारतें बहा ले जाते हैं। अप्रैल–जून के सूखे महीनों में जंगल की आग आम है, ऊँची घाटियों में हिमनदी झीलों का फटना और हिमस्खलन ख़तरे हैं, और जंगलों के पास तेंदुओं व हाथियों के साथ मानव–वन्यजीव संघर्ष होता है। चार धाम तीर्थयात्रियों को यात्रा से पहले राज्य में पंजीकरण कराना होता है, मौसम और सड़क परामर्श देखने चाहिए, और केदारनाथ, हेमकुंड साहिब व अन्य ऊँचे धामों में शरीर को ढलने का समय देना चाहिए।",
        "उत्तराखंड नैसर्गिक आपत्तींना अतिशय प्रवण आहे. त्याचा बहुतांश भाग सर्वाधिक भूकंपप्रवण क्षेत्रांत आहे — उत्तरकाशी (1991) व चमोली (1999) भूकंपांत मोठी जीवितहानी झाली — आणि मान्सून ढगफुटी, भूस्खलन व आकस्मिक पूर आणतो जे रस्ते अडवतात व नदीकाठच्या इमारती वाहून नेतात. एप्रिल–जूनच्या कोरड्या महिन्यांत वणवे सामान्य आहेत, उंच खोऱ्यांत हिमनदी सरोवरे फुटणे व हिमस्खलन हे धोके आहेत, आणि जंगलांजवळ बिबटे व हत्तींसोबत मानव–वन्यजीव संघर्ष होतो. चार धाम यात्रेकरूंनी प्रवासापूर्वी राज्याकडे नोंदणी करणे आवश्यक आहे, हवामान व रस्ता सूचना तपासाव्यात, आणि केदारनाथ, हेमकुंड साहिब व इतर उंच धामांवर शरीराला जुळवून घेण्यास वेळ द्यावा."),
        conf="Editorial"),
    emergency_table(("Uttarakhand", "उत्तराखंड", "उत्तराखंड")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Char Dham registration portal — verified link", "चार धाम पंजीकरण पोर्टल — सत्यापित लिंक", "चार धाम नोंदणी संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "Uttarakhand Tourism Development Board."),
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official address."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Uttarakhand has 28 GIs registered for the State alone on the GI Registry's list as on 31 December 2025, plus Basmati rice, which it shares with six other States and Union Territories. Many were filed in 2022 in a single drive: hill crops such as mandua (finger millet), jhangora (barnyard millet), gahat, red rice, kala bhat, pahari toor dal, Munsyari rajma and Almora lakhori chilli; fruit such as the malta, Ramnagar litchi and Ramgarh peach; and crafts such as aipan, ringal, Almora copperware, thulma and Bhotia dann rugs, nettle fabrics, the rangwali pichhoda veil, wood carving and the wooden masks of Ramman. Badri cow ghee was filed in December 2024.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में केवल उत्तराखंड के लिए 28 जीआई पंजीकृत हैं, साथ में बासमती चावल, जिसे यह छह अन्य राज्यों और केंद्र शासित प्रदेशों के साथ साझा करता है। बहुत से 2022 में एक ही अभियान में दायर हुए: मंडुआ, झंगोरा, गहत, लाल चावल, काला भट, पहाड़ी तूर दाल, मुनस्यारी राजमा और अल्मोड़ा लखोरी मिर्च जैसी पहाड़ी फ़सलें; माल्टा, रामनगर लीची और रामगढ़ आड़ू जैसे फल; और ऐपण, रिंगाल, अल्मोड़ा के ताँबे के बर्तन, थुलमा और भोटिया दन क़ालीन, बिच्छू बूटी वस्त्र, रंगवाली पिछौड़ा, काष्ठ नक़्क़ाशी और रम्माण के लकड़ी के मुखौटे जैसे शिल्प। बद्री गाय का घी दिसंबर 2024 में दायर हुआ।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत केवळ उत्तराखंडसाठी 28 जीआय नोंदणीकृत आहेत, सोबत बासमती तांदूळ, जो तो इतर सहा राज्ये व केंद्रशासित प्रदेशांसोबत सामायिक करतो. अनेक 2022 मध्ये एकाच मोहिमेत दाखल झाले: नाचणी (मंडुआ), झंगोरा, गहत, लाल तांदूळ, काळा भट, पहाडी तूरडाळ, मुनस्यारी राजमा व अल्मोडा लखोरी मिरची यांसारखी डोंगरी पिके; माल्टा, रामनगर लिची व रामगड पीच यांसारखी फळे; आणि ऐपण, रिंगाल, अल्मोड्याची तांब्याची भांडी, थुलमा व भोटिया दन गालिचे, बिच्छू बुटी वस्त्रे, रंगवाली पिछौडा, काष्ठकोरीव काम व रम्माणचे लाकडी मुखवटे यांसारख्या हस्तकला. बद्री गायीचे तूप डिसेंबर 2024 मध्ये दाखल झाले."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Filing date of Uttarakhand Bedu (application 1188)", "उत्तराखंड बेड़ू की दायर तिथि (आवेदन 1188)", "उत्तराखंड बेडूची दाखल तारीख (अर्ज 1188)"), "gi-registry", "The registry list prints 27.02.2027, which cannot be correct; confirm from the GI Journal."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "The Char Dham yatra — Yamunotri, Gangotri, Kedarnath and Badrinath — is the State's great pilgrimage, together with Hemkund Sahib, and Haridwar and Rishikesh draw pilgrims and yoga students all year; the evening Ganga aarti at Har ki Pauri is unforgettable. Hill stations include Mussoorie, Nainital with its lake, Ranikhet, Almora, Kausani with its view of the Himalaya, Lansdowne and Chakrata. Corbett and Rajaji offer jungle safaris, the Valley of Flowers blooms in July and August, Auli has skiing in winter, and treks such as Roopkund, Har ki Dun, Kedarkantha and Pindari glacier, and the climb to Tungnath — the highest Shiva temple — attract walkers from across India.",
        "चार धाम यात्रा — यमुनोत्री, गंगोत्री, केदारनाथ और बद्रीनाथ — हेमकुंड साहिब के साथ राज्य की सबसे बड़ी तीर्थयात्रा है, और हरिद्वार व ऋषिकेश वर्ष भर तीर्थयात्रियों और योग विद्यार्थियों को खींचते हैं; हर की पैड़ी पर शाम की गंगा आरती अविस्मरणीय है। पर्वतीय स्थलों में मसूरी, अपनी झील वाला नैनीताल, रानीखेत, अल्मोड़ा, हिमालय के दृश्य वाला कौसानी, लैंसडाउन और चकराता शामिल हैं। कॉर्बेट और राजाजी जंगल सफ़ारी कराते हैं, फूलों की घाटी जुलाई और अगस्त में खिलती है, औली में सर्दियों में स्कीइंग होती है, और रूपकुंड, हर की दून, केदारकांठा और पिंडारी हिमनद जैसे ट्रेक और सबसे ऊँचे शिव मंदिर तुंगनाथ की चढ़ाई पूरे भारत से पैदल यात्रियों को आकर्षित करती है।",
        "चार धाम यात्रा — यमुनोत्री, गंगोत्री, केदारनाथ व बद्रीनाथ — हेमकुंड साहिबसह राज्याची सर्वांत मोठी तीर्थयात्रा आहे, आणि हरिद्वार व ऋषिकेश वर्षभर यात्रेकरू व योगविद्यार्थ्यांना आकर्षित करतात; हर की पौडी येथील संध्याकाळची गंगा आरती अविस्मरणीय असते. थंड हवेच्या ठिकाणांत मसुरी, सरोवर असलेले नैनीताल, राणीखेत, अल्मोडा, हिमालयाचे दर्शन देणारे कौसानी, लॅन्सडाउन व चकराता यांचा समावेश आहे. कॉर्बेट व राजाजी जंगल सफारी देतात, फुलांचे खोरे जुलै व ऑगस्टमध्ये बहरते, औलीत हिवाळ्यात स्कीइंग होते, आणि रूपकुंड, हर की दून, केदारकांठा व पिंडारी हिमनदीसारखे ट्रेक आणि सर्वांत उंच शिवमंदिर तुंगनाथची चढाई भारतभरातून पदयात्रींना आकर्षित करते."),
        conf="Editorial"),
    lst("places", [
        it3("chardham", "Char Dham", "चार धाम", "चार धाम", m=("Yamunotri, Gangotri, Kedarnath, Badrinath", "यमुनोत्री, गंगोत्री, केदारनाथ, बद्रीनाथ", "यमुनोत्री, गंगोत्री, केदारनाथ, बद्रीनाथ")),
        it3("haridwar", "Haridwar and Rishikesh", "हरिद्वार और ऋषिकेश", "हरिद्वार व ऋषिकेश", m=("Ganga aarti; yoga", "गंगा आरती; योग", "गंगा आरती; योग")),
        it3("nainital", "Nainital", "नैनीताल", "नैनीताल", m=("Lake town", "झील नगरी", "सरोवरनगरी")),
        it3("mussoorie", "Mussoorie", "मसूरी", "मसुरी", m=("'Queen of the hills'", "'पहाड़ों की रानी'", "'डोंगरांची राणी'")),
        it3("corbett", "Jim Corbett National Park", "जिम कॉर्बेट राष्ट्रीय उद्यान", "जिम कॉर्बेट राष्ट्रीय उद्यान", m=("Tiger safaris", "बाघ सफ़ारी", "व्याघ्र सफारी")),
        it3("vof", "Valley of Flowers and Hemkund Sahib", "फूलों की घाटी और हेमकुंड साहिब", "फुलांचे खोरे व हेमकुंड साहिब", m=("July–August", "जुलाई–अगस्त", "जुलै–ऑगस्ट")),
        it3("auli", "Auli", "औली", "औली", m=("Skiing", "स्कीइंग", "स्कीइंग")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Haridwar's aarti, Rishikesh's ashrams and a day in Rajaji.", "हरिद्वार की आरती, ऋषिकेश के आश्रम और राजाजी में एक दिन।", "हरिद्वारची आरती, ऋषिकेशचे आश्रम व राजाजीत एक दिवस.")),
        it3("d5", "5 days", "5 दिन", "5 दिवस", d=("Nainital, Bhimtal, Almora and Kausani in Kumaon.", "कुमाऊँ में नैनीताल, भीमताल, अल्मोड़ा और कौसानी।", "कुमाऊँमध्ये नैनीताल, भीमताल, अल्मोडा व कौसानी.")),
        it3("d10", "10–12 days (May–October)", "10–12 दिन (मई–अक्टूबर)", "10–12 दिवस (मे–ऑक्टोबर)", d=("The Char Dham circuit from Rishikesh, after registering online.", "ऑनलाइन पंजीकरण के बाद ऋषिकेश से चार धाम परिक्रमा।", "ऑनलाइन नोंदणीनंतर ऋषिकेशहून चार धाम परिक्रमा.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("ut", "Uttarakhand Tourism (official)", "उत्तराखंड पर्यटन (आधिकारिक)", "उत्तराखंड पर्यटन (अधिकृत)", url="https://uttarakhandtourism.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Almora", "अल्मोड़ा", "अल्मोडा"), ("Bageshwar", "बागेश्वर", "बागेश्वर"), ("Chamoli", "चमोली", "चमोली"), ("Champawat", "चंपावत", "चंपावत"), ("Dehradun", "देहरादून", "डेहराडून"),
    ("Haridwar", "हरिद्वार", "हरिद्वार"), ("Nainital", "नैनीताल", "नैनीताल"), ("Pauri Garhwal", "पौड़ी गढ़वाल", "पौडी गढवाल"), ("Pithoragarh", "पिथौरागढ़", "पिथौरागड"),
    ("Rudraprayag", "रुद्रप्रयाग", "रुद्रप्रयाग"), ("Tehri Garhwal", "टिहरी गढ़वाल", "टिहरी गढवाल"), ("Udham Singh Nagar", "ऊधम सिंह नगर", "उधमसिंह नगर"), ("Uttarkashi", "उत्तरकाशी", "उत्तरकाशी"),
]
assert len(DISTRICTS) == 13, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("dehradun", ("Dehradun", "देहरादून", "डेहराडून"), ("Capital and largest city; schools and national institutes.", "राजधानी और सबसे बड़ा शहर; विद्यालय और राष्ट्रीय संस्थान।", "राजधानी व सर्वांत मोठे शहर; शाळा व राष्ट्रीय संस्था."), ("Capital", "राजधानी", "राजधानी")),
        city("haridwar", ("Haridwar", "हरिद्वार", "हरिद्वार"), ("Pilgrimage city on the Ganga; BHEL and SIDCUL industries.", "गंगा किनारे तीर्थ नगरी; भेल और सिडकुल उद्योग।", "गंगाकाठचे तीर्थनगर; भेल व सिडकुल उद्योग."), ("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        city("haldwani", ("Haldwani", "हल्द्वानी", "हल्द्वानी"), ("Gateway to Kumaon and its main trading town.", "कुमाऊँ का प्रवेश द्वार और मुख्य व्यापारिक नगर।", "कुमाऊँचे प्रवेशद्वार व मुख्य व्यापारी शहर."), ("Trade", "व्यापार", "व्यापार")),
        city("roorkee", ("Roorkee", "रुड़की", "रुडकी"), ("IIT Roorkee and the Ganga canal.", "आईआईटी रुड़की और गंगा नहर।", "आयआयटी रुडकी व गंगा कालवा."), ("Education", "शिक्षा", "शिक्षण")),
        city("rudrapur", ("Rudrapur", "रुद्रपुर", "रुद्रपूर"), ("Industrial town near Pantnagar.", "पंतनगर के पास औद्योगिक नगर।", "पंतनगरजवळील औद्योगिक शहर."), ("Industry", "उद्योग", "उद्योग")),
        city("rishikesh", ("Rishikesh", "ऋषिकेश", "ऋषिकेश"), ("Yoga capital; gateway to the Char Dham.", "योग राजधानी; चार धाम का प्रवेश द्वार।", "योगाची राजधानी; चार धामचे प्रवेशद्वार."), ("Pilgrimage", "तीर्थ", "तीर्थक्षेत्र")),
        city("nainital", ("Nainital", "नैनीताल", "नैनीताल"), ("Lake town; seat of the High Court.", "झील नगरी; उच्च न्यायालय का मुख्यालय।", "सरोवरनगरी; उच्च न्यायालयाचे ठिकाण."), ("Tourism", "पर्यटन", "पर्यटन")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 13 districts (alphabetical)", "13 ज़िले (वर्णानुक्रम)", "13 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Official district list (State notification)", "आधिकारिक ज़िला सूची (राज्य अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य अधिसूचना)"), "india-gov", "Link the State's list of districts."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Uttarakhand is a centre of mountaineering and adventure sport: Bachendri Pal of Uttarkashi became the first Indian woman to climb Everest in 1984, the Nehru Institute of Mountaineering in Uttarkashi trains climbers, Auli hosts skiing, and Rishikesh is India's best-known white-water rafting centre. The State has produced Olympians and international players such as the badminton player Lakshya Sen of Almora, a Commonwealth Games gold medallist and member of India's Thomas Cup-winning team in 2022, and the hockey forward Vandana Katariya of Haridwar, who scored a hat-trick at the Tokyo Olympics. Uttarakhand hosted the 38th National Games in early 2025.",
        "उत्तराखंड पर्वतारोहण और साहसिक खेलों का केंद्र है: उत्तरकाशी की बछेंद्री पाल 1984 में एवरेस्ट पर चढ़ने वाली पहली भारतीय महिला बनीं, उत्तरकाशी का नेहरू पर्वतारोहण संस्थान पर्वतारोहियों को प्रशिक्षण देता है, औली में स्कीइंग होती है, और ऋषिकेश भारत का सबसे प्रसिद्ध व्हाइट-वॉटर राफ्टिंग केंद्र है। राज्य ने ओलंपियन और अंतरराष्ट्रीय खिलाड़ी दिए हैं, जैसे अल्मोड़ा के बैडमिंटन खिलाड़ी लक्ष्य सेन, जो राष्ट्रमंडल खेलों के स्वर्ण पदक विजेता और 2022 में थॉमस कप जीतने वाली भारतीय टीम के सदस्य हैं, और हरिद्वार की हॉकी फ़ॉरवर्ड वंदना कटारिया, जिन्होंने टोक्यो ओलंपिक में हैट्रिक लगाई। उत्तराखंड ने 2025 की शुरुआत में 38वें राष्ट्रीय खेलों की मेज़बानी की।",
        "उत्तराखंड हे गिर्यारोहण व साहसी खेळांचे केंद्र आहे: उत्तरकाशीच्या बचेंद्री पाल 1984 मध्ये एव्हरेस्टवर चढणाऱ्या पहिल्या भारतीय महिला ठरल्या, उत्तरकाशीची नेहरू गिर्यारोहण संस्था गिर्यारोहकांना प्रशिक्षण देते, औलीत स्कीइंग होते, आणि ऋषिकेश हे भारतातील सर्वांत प्रसिद्ध व्हाइट-वॉटर राफ्टिंग केंद्र आहे. राज्याने ऑलिम्पियन व आंतरराष्ट्रीय खेळाडू दिले आहेत, जसे अल्मोड्याचा बॅडमिंटनपटू लक्ष्य सेन, जो राष्ट्रकुल स्पर्धेतील सुवर्णपदकविजेता व 2022 मध्ये थॉमस कप जिंकणाऱ्या भारतीय संघाचा सदस्य आहे, आणि हरिद्वारची हॉकी फॉरवर्ड वंदना कटारिया, जिने टोकियो ऑलिम्पिकमध्ये हॅटट्रिक केली. उत्तराखंडने 2025 च्या सुरुवातीला 38 व्या राष्ट्रीय क्रीडा स्पर्धांचे यजमानपद भूषवले."),
        conf="Editorial"),
    lst("venues", [
        it3("nim", "Nehru Institute of Mountaineering, Uttarkashi", "नेहरू पर्वतारोहण संस्थान, उत्तरकाशी", "नेहरू गिर्यारोहण संस्था, उत्तरकाशी"),
        it3("auli", "Auli ski slopes", "औली स्की ढलान", "औली स्की उतार"),
        it3("rajiv", "Rajiv Gandhi International Cricket Stadium, Dehradun", "राजीव गांधी अंतरराष्ट्रीय क्रिकेट स्टेडियम, देहरादून", "राजीव गांधी आंतरराष्ट्रीय क्रिकेट स्टेडियम, डेहराडून"),
        it3("rafting", "Rishikesh rafting stretch", "ऋषिकेश राफ्टिंग खंड", "ऋषिकेश राफ्टिंग टप्पा"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("38th National Games — official medal table", "38वें राष्ट्रीय खेल — आधिकारिक पदक तालिका", "38 व्या राष्ट्रीय क्रीडा स्पर्धा — अधिकृत पदकतालिका"), "india-gov", "Indian Olympic Association / Uttarakhand Sports Department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("gbpant", ("Govind Ballabh Pant", "गोविंद बल्लभ पंत", "गोविंद वल्लभ पंत"), ("Freedom fighter from Almora district, first Chief Minister of Uttar Pradesh and Union Home Minister; Bharat Ratna.", "अल्मोड़ा ज़िले के स्वतंत्रता सेनानी, उत्तर प्रदेश के पहले मुख्यमंत्री और केंद्रीय गृह मंत्री; भारत रत्न।", "अल्मोडा जिल्ह्यातील स्वातंत्र्यसैनिक, उत्तर प्रदेशचे पहिले मुख्यमंत्री व केंद्रीय गृहमंत्री; भारतरत्न."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("garhwali", ("Chandra Singh Garhwali", "चंद्र सिंह गढ़वाली", "चंद्रसिंह गढवाली"), ("Soldier who refused to fire on unarmed protesters at Peshawar in 1930.", "सैनिक, जिन्होंने 1930 में पेशावर में निहत्थे प्रदर्शनकारियों पर गोली चलाने से इनकार किया।", "सैनिक, ज्यांनी 1930 मध्ये पेशावर येथे निःशस्त्र आंदोलकांवर गोळीबार करण्यास नकार दिला."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("sridev", ("Sri Dev Suman", "श्रीदेव सुमन", "श्रीदेव सुमन"), ("Activist against the rule of Tehri state who died on hunger strike in jail in 1944.", "टिहरी रियासत के शासन के विरुद्ध आंदोलनकारी, जिनकी 1944 में जेल में अनशन के दौरान मृत्यु हुई।", "टिहरी संस्थानाच्या राजवटीविरुद्धचे आंदोलक, ज्यांचा 1944 मध्ये तुरुंगात उपोषणादरम्यान मृत्यू झाला."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("sumitra", ("Sumitranandan Pant", "सुमित्रानंदन पंत", "सुमित्रानंदन पंत"), ("Hindi poet of the Chhayavad school from Kausani; Jnanpith Award.", "कौसानी के छायावादी हिंदी कवि; ज्ञानपीठ पुरस्कार।", "कौसानीचे छायावादी हिंदी कवी; ज्ञानपीठ पुरस्कार."), ("Literature", "साहित्य", "साहित्य")),
        person("gaura", ("Gaura Devi", "गौरा देवी", "गौरा देवी"), ("Leader of the women of Reni village whose 1974 protest became the Chipko movement.", "रैणी गाँव की महिलाओं की नेता, जिनका 1974 का विरोध चिपको आंदोलन बना।", "रैणी गावच्या स्त्रियांच्या नेत्या, ज्यांचे 1974 चे आंदोलन चिपको आंदोलन बनले."), ("Environment", "पर्यावरण", "पर्यावरण")),
        person("bahuguna", ("Sunderlal Bahuguna", "सुंदरलाल बहुगुणा", "सुंदरलाल बहुगुणा"), ("Environmentalist of the Chipko movement and opponent of the Tehri dam.", "चिपको आंदोलन के पर्यावरणविद और टिहरी बाँध के विरोधी।", "चिपको आंदोलनाचे पर्यावरणवादी व टिहरी धरणाचे विरोधक."), ("Environment", "पर्यावरण", "पर्यावरण")),
        person("bachendri", ("Bachendri Pal", "बछेंद्री पाल", "बचेंद्री पाल"), ("First Indian woman to climb Mount Everest, in 1984.", "1984 में माउंट एवरेस्ट पर चढ़ने वाली पहली भारतीय महिला।", "1984 मध्ये माउंट एव्हरेस्ट सर करणाऱ्या पहिल्या भारतीय महिला."), ("Sport", "खेल", "क्रीडा")),
        person("corbett", ("Jim Corbett", "जिम कॉर्बेट", "जिम कॉर्बेट"), ("Hunter-turned-conservationist and author from Nainital; the national park is named after him.", "नैनीताल के शिकारी से संरक्षणवादी बने लेखक; राष्ट्रीय उद्यान उनके नाम पर है।", "नैनीतालचे शिकारी ते संवर्धनवादी झालेले लेखक; राष्ट्रीय उद्यान त्यांच्या नावाने आहे."), ("Conservation", "संरक्षण", "संवर्धन")),
        person("lakshya", ("Lakshya Sen", "लक्ष्य सेन", "लक्ष्य सेन"), ("Badminton player from Almora; Commonwealth Games gold, 2022.", "अल्मोड़ा के बैडमिंटन खिलाड़ी; राष्ट्रमंडल खेल स्वर्ण, 2022।", "अल्मोड्याचा बॅडमिंटनपटू; राष्ट्रकुल स्पर्धा सुवर्ण, 2022."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Out-migration from the hills is one of Uttarakhand's defining issues: many young people leave for jobs in Dehradun, Haldwani, Delhi, Mumbai and the Gulf, and some villages have been left almost empty. The Garhwal Rifles and the Kumaon Regiment recruit heavily from the hills, and ex-servicemen form a large share of the population. Large Uttarakhandi communities in Delhi and the National Capital Region keep up the festivals, music and food of Garhwal and Kumaon.",
        "पहाड़ों से पलायन उत्तराखंड के प्रमुख मुद्दों में से है: बहुत से युवा देहरादून, हल्द्वानी, दिल्ली, मुंबई और खाड़ी देशों में नौकरियों के लिए जाते हैं, और कुछ गाँव लगभग ख़ाली हो गए हैं। गढ़वाल राइफ़ल्स और कुमाऊँ रेजिमेंट पहाड़ों से बड़ी संख्या में भर्ती करती हैं, और पूर्व सैनिक जनसंख्या का बड़ा हिस्सा हैं। दिल्ली और राष्ट्रीय राजधानी क्षेत्र में बड़े उत्तराखंडी समुदाय गढ़वाल और कुमाऊँ के त्योहार, संगीत और खान-पान जीवित रखते हैं।",
        "डोंगरांतून होणारे स्थलांतर हा उत्तराखंडचा एक मुख्य प्रश्न आहे: अनेक तरुण डेहराडून, हल्द्वानी, दिल्ली, मुंबई व आखाती देशांत नोकरीसाठी जातात, आणि काही गावे जवळपास रिकामी झाली आहेत. गढवाल रायफल्स व कुमाऊँ रेजिमेंट डोंगरांतून मोठ्या संख्येने भरती करतात, आणि माजी सैनिक लोकसंख्येचा मोठा भाग आहेत. दिल्ली व राष्ट्रीय राजधानी क्षेत्रातील मोठे उत्तराखंडी समुदाय गढवाल व कुमाऊँचे सण, संगीत व खाद्यसंस्कृती जिवंत ठेवतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Villages depopulated by migration", "पलायन से ख़ाली हुए गाँव", "स्थलांतरामुळे ओस पडलेली गावे"), "india-gov", "Uttarakhand Rural Development and Migration Prevention Commission."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Uttarakhand portal", "उत्तराखंड सरकार पोर्टल", "उत्तराखंड शासन संकेतस्थळ", url="https://uk.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Uttarakhand Tourism", "उत्तराखंड पर्यटन", "उत्तराखंड पर्यटन", url="https://uttarakhandtourism.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Dehradun", "देहरादून", "डेहराडून"), "0135"], [L("Haridwar", "हरिद्वार", "हरिद्वार"), "01334"], [L("Haldwani", "हल्द्वानी", "हल्द्वानी"), "05946"],
           [L("Nainital", "नैनीताल", "नैनीताल"), "05942"], [L("Roorkee", "रुड़की", "रुडकी"), "01332"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("corbett", ("Jim Corbett National Park, founded in 1936 as Hailey National Park, was India's first national park.", "1936 में हेली राष्ट्रीय उद्यान के रूप में स्थापित जिम कॉर्बेट राष्ट्रीय उद्यान भारत का पहला राष्ट्रीय उद्यान था।", "1936 मध्ये हेली राष्ट्रीय उद्यान म्हणून स्थापन झालेले जिम कॉर्बेट राष्ट्रीय उद्यान हे भारताचे पहिले राष्ट्रीय उद्यान होते.")),
        triv("ramman", ("Ramman, the ritual theatre of Saloor-Dungra in Chamoli, is on UNESCO's list of Intangible Cultural Heritage.", "चमोली के सलूड़-डुंग्रा का अनुष्ठानिक रंगमंच रम्माण यूनेस्को की अमूर्त सांस्कृतिक विरासत सूची में है।", "चमोलीतील सलूड-डुंग्राचे विधिनाट्य रम्माण युनेस्कोच्या अमूर्त सांस्कृतिक वारसा यादीत आहे.")),
        triv("gi", ("Uttarakhand has 28 GIs registered for the State alone — and filed most of them in 2022.", "उत्तराखंड में केवल राज्य के लिए 28 जीआई पंजीकृत हैं — और इनमें से अधिकांश 2022 में दायर हुए।", "उत्तराखंडमध्ये केवळ राज्यासाठी 28 जीआय नोंदणीकृत आहेत — आणि त्यांपैकी बहुतेक 2022 मध्ये दाखल झाले."), GI_PDF, "gi-registry"),
        triv("speaker", ("Ritu Khanduri Bhushan, elected in 2022, is the first woman Speaker of the Uttarakhand Assembly.", "2022 में चुनी गईं ऋतु खंडूड़ी भूषण उत्तराखंड विधानसभा की पहली महिला अध्यक्ष हैं।", "2022 मध्ये निवडलेल्या ऋतू खंडुरी भूषण या उत्तराखंड विधानसभेच्या पहिल्या महिला अध्यक्ष आहेत.")),
        triv("roorkee", ("IIT Roorkee traces its origin to the Thomason College of Civil Engineering, founded in 1847.", "आईआईटी रुड़की का मूल 1847 में स्थापित थॉमसन कॉलेज ऑफ़ सिविल इंजीनियरिंग है।", "आयआयटी रुडकीचे मूळ 1847 मध्ये स्थापन झालेल्या थॉमसन कॉलेज ऑफ सिव्हिल इंजिनिअरिंगमध्ये आहे.")),
        triv("ls", ("The State elects 5 members to the Lok Sabha.", "राज्य से लोकसभा के 5 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 5 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("uk mod3 ok")
