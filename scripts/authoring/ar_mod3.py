"""Arunachal Pradesh modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-AR"
ar = read("regions/IN-AR.json")["metrics"]; ind = read("india.json")["metrics"]
C = research("census_b5plus.json"); F = C["forest"]["AR"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "About 79% of Arunachal Pradesh is forest (ISFR 2023), ranging from tropical evergreen rainforest in the foothills and the Namdapha valley, through subtropical and temperate broadleaf and pine forests, to fir, rhododendron and alpine meadows in the north. The State lies in the Eastern Himalaya and Indo-Burma biodiversity hotspots and is home to tigers, clouded and snow leopards, red pandas, the Mishmi takin, four hornbill species, hoolock gibbons and hundreds of orchids; the Bugun liocichla, a bird first described in 2006, lives only around Eaglenest. Namdapha, Pakke and Kamlang are tiger reserves, and Mouling and Namdapha are national parks. Pakke's Hornbill Nest Adoption Programme, in which Nyishi villagers protect nests, is a well-known community conservation effort.\n\nThere are no Ramsar sites in Arunachal Pradesh on the list as on 21 April 2026.",
        "अरुणाचल प्रदेश का लगभग 79% भाग वन है (आईएसएफ़आर 2023), जो तलहटी और नामदफा घाटी के उष्णकटिबंधीय सदाबहार वर्षावन से, उपोष्ण और समशीतोष्ण चौड़ी पत्ती और चीड़ के वनों से होते हुए, उत्तर में देवदार (फ़र), बुरांश और अल्पाइन घास के मैदानों तक फैले हैं। राज्य पूर्वी हिमालय और भारत-बर्मा जैव विविधता हॉटस्पॉट में है और बाघों, धूमिल और हिम तेंदुओं, लाल पांडा, मिश्मी ताकिन, धनेश की चार प्रजातियों, हूलॉक गिबन और सैकड़ों ऑर्किड का घर है; 2006 में पहली बार वर्णित पक्षी बुगुन लियोसिकला केवल ईगलनेस्ट के आसपास रहता है। नामदफा, पक्के और कमलांग बाघ अभयारण्य हैं, और मौलिंग और नामदफा राष्ट्रीय उद्यान हैं। पक्के का धनेश घोंसला गोद कार्यक्रम, जिसमें न्यिशी ग्रामीण घोंसलों की रक्षा करते हैं, एक प्रसिद्ध सामुदायिक संरक्षण प्रयास है।\n\n21 अप्रैल 2026 की सूची में अरुणाचल प्रदेश में कोई रामसर स्थल नहीं है।",
        "अरुणाचल प्रदेशचा सुमारे 79% भाग वनाच्छादित आहे (आयएसएफआर 2023), पायथ्याचे डोंगर व नामदफा खोऱ्यातील उष्णकटिबंधीय सदाहरित वर्षावनापासून, उपोष्ण व समशीतोष्ण रुंदपर्णी आणि पाइन जंगलांमधून, उत्तरेकडील फर, ऱ्होडोडेंड्रॉन व अल्पाइन कुरणांपर्यंत. राज्य पूर्व हिमालय व इंडो-बर्मा जैवविविधता हॉटस्पॉटमध्ये आहे आणि वाघ, ढगाळ व हिमबिबटे, लाल पांडा, मिश्मी ताकिन, धनेशाच्या चार प्रजाती, हूलॉक गिबन व शेकडो ऑर्किडचे घर आहे; 2006 मध्ये प्रथम वर्णन झालेला बुगुन लिओसिक्ला पक्षी केवळ ईगलनेस्टभोवती राहतो. नामदफा, पक्के व कमलांग हे व्याघ्र प्रकल्प आहेत, आणि मौलिंग व नामदफा राष्ट्रीय उद्याने आहेत. पक्केचा धनेश घरटे दत्तक कार्यक्रम, ज्यात न्यिशी गावकरी घरट्यांचे रक्षण करतात, हा प्रसिद्ध सामुदायिक संवर्धन उपक्रम आहे.\n\n21 एप्रिल 2026 च्या यादीत अरुणाचल प्रदेशमध्ये कोणतेही रामसर स्थळ नाही."),
        sources=["fsi", "indian-wetlands", "ntca"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), ar["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(0, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: none in Arunachal Pradesh."), "number"),
    ]),
    lst("protected", [
        it3("namdapha", "Namdapha National Park and Tiger Reserve", "नामदफा राष्ट्रीय उद्यान और बाघ अभयारण्य", "नामदफा राष्ट्रीय उद्यान व व्याघ्र प्रकल्प", m=("Changlang", "चांगलांग", "चांगलांग")),
        it3("pakke", "Pakke Tiger Reserve", "पक्के बाघ अभयारण्य", "पक्के व्याघ्र प्रकल्प", m=("Hornbills, Pakke-Kessang", "धनेश, पक्के-केस्सांग", "धनेश, पक्के-केस्सांग")),
        it3("kamlang", "Kamlang Tiger Reserve", "कमलांग बाघ अभयारण्य", "कमलांग व्याघ्र प्रकल्प", m=("Lohit", "लोहित", "लोहित")),
        it3("mouling", "Mouling National Park", "मौलिंग राष्ट्रीय उद्यान", "मौलिंग राष्ट्रीय उद्यान", m=("Upper Siang", "अपर सियांग", "अप्पर सियांग")),
        it3("eaglenest", "Eaglenest Wildlife Sanctuary", "ईगलनेस्ट वन्यजीव अभयारण्य", "ईगलनेस्ट वन्यजीव अभयारण्य", m=("Bugun liocichla", "बुगुन लियोसिकला", "बुगुन लिओसिक्ला")),
        it3("talle", "Talle Valley Wildlife Sanctuary", "ताले घाटी वन्यजीव अभयारण्य", "ताले खोरे वन्यजीव अभयारण्य", m=("Near Ziro", "ज़ीरो के पास", "झिरोजवळ")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("mithun", "Mithun (State animal)", "मिथुन (राज्य पशु)", "मिथुन (राज्यप्राणी)"), it3("hornbill", "Great hornbill (State bird)", "बड़ा धनेश (राज्य पक्षी)", "महाधनेश (राज्यपक्षी)"),
        it3("takin", "Mishmi takin", "मिश्मी ताकिन", "मिश्मी ताकिन"), it3("gibbon", "Hoolock gibbon", "हूलॉक गिबन", "हूलॉक गिबन"),
        it3("redpanda", "Red panda", "लाल पांडा", "लाल पांडा"), it3("orchid", "Foxtail orchid (State flower)", "फ़ॉक्सटेल ऑर्किड (राज्य पुष्प)", "फॉक्सटेल ऑर्किड (राज्यपुष्प)"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Tiger numbers by reserve (All India Tiger Estimation)", "अभयारण्यवार बाघों की संख्या (अखिल भारतीय बाघ आकलन)", "प्रकल्पनिहाय वाघांची संख्या (अखिल भारतीय व्याघ्र गणना)"), "ntca", "NTCA / WII status of tigers report."),
        (L("Number of orchid species — official", "ऑर्किड प्रजातियों की संख्या — आधिकारिक", "ऑर्किड प्रजातींची संख्या — अधिकृत"), "india-gov", "Botanical Survey of India / State Forest Research Institute."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Arunachal Pradesh supplies a large share of the Brahmaputra's water: the Siang, Subansiri, Kameng, Dibang and Lohit carry heavy monsoon rain and Himalayan snowmelt down to Assam. That makes the State central both to hydropower plans and to flood management downstream, and dams on these rivers are debated for their effects on Assam's floods and fisheries. Upstream construction in Tibet on the Yarlung Tsangpo is watched closely. Most villages draw water from springs and streams, and the Apatani of Ziro manage an old system of channels that irrigates their rice fields and fish ponds.",
        "अरुणाचल प्रदेश ब्रह्मपुत्र के जल का बड़ा भाग देता है: सियांग, सुबनसिरी, कामेंग, दिबांग और लोहित भारी मानसूनी वर्षा और हिमालय की पिघली बर्फ़ को असम तक ले जाती हैं। इससे राज्य जलविद्युत योजनाओं और नीचे बाढ़ प्रबंधन दोनों का केंद्र है, और इन नदियों पर बाँध असम की बाढ़ और मत्स्य पालन पर प्रभाव के कारण बहस में हैं। तिब्बत में यारलुंग त्सांगपो पर ऊपर की ओर निर्माण पर क़रीबी नज़र रखी जाती है। अधिकांश गाँव झरनों और धाराओं से पानी लेते हैं, और ज़ीरो के अपातानी नहरों की एक पुरानी व्यवस्था संभालते हैं जो उनके धान के खेतों और मछली तालाबों को सींचती है।",
        "अरुणाचल प्रदेश ब्रह्मपुत्रेच्या पाण्याचा मोठा वाटा देते: सियांग, सुबनसिरी, कामेंग, दिबांग व लोहित मुसळधार मान्सून पाऊस व हिमालयातील वितळलेले बर्फ आसामपर्यंत वाहून नेतात. त्यामुळे राज्य जलविद्युत योजना व खालच्या भागातील पूर व्यवस्थापन या दोन्हींचे केंद्र आहे, आणि या नद्यांवरील धरणे आसामच्या पुरांवर व मत्स्यव्यवसायावरील परिणामांमुळे वादात आहेत. तिबेटमध्ये यारलुंग त्सांगपोवरील वरच्या भागातील बांधकामावर बारकाईने लक्ष ठेवले जाते. बहुतेक गावे झरे व ओढ्यांतून पाणी घेतात, आणि झिरोचे आपातानी कालव्यांची जुनी व्यवस्था सांभाळतात जी त्यांची भातशेते व मत्स्यतळी भिजवते."),
        conf="Editorial"),
    gaps("g", [
        (L("Brahmaputra flow contributed by Arunachal rivers — official estimate", "अरुणाचल की नदियों का ब्रह्मपुत्र प्रवाह में योगदान — आधिकारिक अनुमान", "अरुणाचलच्या नद्यांचा ब्रह्मपुत्रा प्रवाहातील वाटा — अधिकृत अंदाज"), "india-gov", "Central Water Commission / Brahmaputra Board."),
        (L("Household tap-water coverage", "घरेलू नल जल कवरेज", "घरगुती नळजोडणी व्याप्ती"), "india-gov", "Jal Jeevan Mission dashboard."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Arunachal Pradesh lies in the highest earthquake zone; the great Assam earthquake of 1950 had its epicentre near the border. Landslides block roads every monsoon, flash floods are common in the Siang and Lohit valleys, and heavy snow can close the road over Sela and to Bum La. Visitors need an Inner Line Permit (Indian citizens) or a Protected Area Permit (foreigners), should carry identity documents near the border, and should allow for delays on mountain roads.",
        "अरुणाचल प्रदेश सबसे ऊँचे भूकंप क्षेत्र में है; 1950 के महान असम भूकंप का केंद्र सीमा के पास था। हर मानसून में भूस्खलन सड़कें रोकते हैं, सियांग और लोहित घाटियों में अचानक बाढ़ आम है, और भारी बर्फ़ सेला और बुम ला की सड़क बंद कर सकती है। पर्यटकों को इनर लाइन परमिट (भारतीय नागरिक) या संरक्षित क्षेत्र परमिट (विदेशी) चाहिए, सीमा के पास पहचान पत्र साथ रखने चाहिए, और पहाड़ी सड़कों पर देरी का ध्यान रखना चाहिए।",
        "अरुणाचल प्रदेश सर्वोच्च भूकंप क्षेत्रात आहे; 1950 च्या महान आसाम भूकंपाचे केंद्र सीमेजवळ होते. दर पावसाळ्यात भूस्खलन रस्ते अडवते, सियांग व लोहित खोऱ्यांत अचानक पूर सामान्य आहेत, आणि जोरदार बर्फवृष्टीमुळे सेला व बुम लाचा रस्ता बंद होऊ शकतो. पर्यटकांना इनर लाइन परवाना (भारतीय नागरिक) किंवा संरक्षित क्षेत्र परवाना (परदेशी) लागतो, सीमेजवळ ओळखपत्रे जवळ ठेवावीत, आणि डोंगरी रस्त्यांवरील विलंबाचा विचार करावा."),
        conf="Editorial"),
    emergency_table(("Arunachal Pradesh", "अरुणाचल प्रदेश", "अरुणाचल प्रदेश")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official address."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Twenty-one GIs on the GI Registry's list as on 31 December 2025 belong to Arunachal Pradesh, two of them shared with Assam (Singpho phalap tea and Mishing handloom products). Arunachal orange was the first, filed in 2012. Most were filed in 2021–2023 and reflect the State's tribes: the textiles of the Adi, Apatani, Galo, Idu Mishmi, Monpa, Nyishi, Tai Khamti and Tangsa; Wancho wood carving, Monpa handmade paper, handmade carpets and the dao sword; and foods and drinks such as Khamti rice, Adi kekir ginger, yak churpi, angnyat millet, Adi apong and marua apo.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में इक्कीस जीआई अरुणाचल प्रदेश के हैं, जिनमें से दो असम के साथ साझा हैं (सिंगफ़ो फलाप चाय और मिसिंग हथकरघा उत्पाद)। 2012 में दायर अरुणाचल संतरा पहला था। अधिकांश 2021–2023 में दायर हुए और राज्य की जनजातियों को दर्शाते हैं: आदी, अपातानी, गालो, इदु मिश्मी, मोनपा, न्यिशी, ताई खामती और तांगसा के वस्त्र; वांचो काष्ठ नक्काशी, मोनपा हस्तनिर्मित काग़ज़, हस्तनिर्मित क़ालीन और दाओ तलवार; और खामती चावल, आदी केकिर अदरक, याक छुरपी, अंग्न्यात बाजरा, आदी आपोंग और मरुआ आपो जैसे खाद्य और पेय।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीतील एकवीस जीआय अरुणाचल प्रदेशचे आहेत, ज्यांपैकी दोन आसामसोबत सामायिक आहेत (सिंगफो फलाप चहा व मिसिंग हातमाग उत्पादने). 2012 मध्ये दाखल अरुणाचल संत्रे पहिले होते. बहुतेक 2021–2023 मध्ये दाखल झाले आणि राज्यातील जमाती दर्शवतात: आदी, आपातानी, गालो, इदु मिश्मी, मोनपा, न्यिशी, ताई खामती व तांगसा यांची वस्त्रे; वांचो लाकडी कोरीवकाम, मोनपा हातकागद, हाताने बनवलेले गालिचे व दाओ तलवार; आणि खामती तांदूळ, आदी केकिर आले, याक छुरपी, अंग्न्यात भरडधान्य, आदी आपोंग व मरुआ आपो सारखे खाद्य व पेये."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Pending GI applications from Arunachal Pradesh", "अरुणाचल प्रदेश के लंबित जीआई आवेदन", "अरुणाचल प्रदेशचे प्रलंबित जीआय अर्ज"), "gi-registry", "GI Registry application status search."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Tawang, reached over the Sela Pass, is the State's best-known destination, with its great monastery, the Tawang War Memorial, high lakes such as Sangetsar (Madhuri) and, with permits, the Bum La pass on the border. On the way lie Bomdila and the Dirang valley. The Ziro valley of the Apatani, with its pine-ringed rice fields and the Ziro Festival of Music, Mechuka in the far west of Siang, Pasighat on the Siang, and the riverine forests of Namdapha draw travellers seeking quieter places. Itanagar has the Ita Fort and the Jawaharlal Nehru State Museum, and Parshuram Kund on the Lohit draws pilgrims in January.",
        "सेला दर्रे पार कर पहुँचा जाने वाला तवांग राज्य का सबसे प्रसिद्ध गंतव्य है, अपने महान मठ, तवांग युद्ध स्मारक, संगेत्सर (माधुरी) जैसी ऊँची झीलों और, परमिट के साथ, सीमा पर बुम ला दर्रे के साथ। रास्ते में बोमडिला और दिरांग घाटी हैं। अपातानी की ज़ीरो घाटी, चीड़ से घिरे धान के खेतों और ज़ीरो संगीत उत्सव के साथ, सियांग के सुदूर पश्चिम में मेचुका, सियांग किनारे पासीघाट, और नामदफा के नदी तटीय वन शांत स्थानों की तलाश करने वाले यात्रियों को खींचते हैं। ईटानगर में ईटा क़िला और जवाहरलाल नेहरू राज्य संग्रहालय है, और लोहित पर परशुराम कुंड जनवरी में तीर्थयात्रियों को खींचता है।",
        "सेला खिंड ओलांडून पोहोचले जाणारे तवांग हे राज्यातील सर्वांत प्रसिद्ध ठिकाण आहे, त्याचा महान मठ, तवांग युद्ध स्मारक, संगेत्सर (माधुरी) सारखी उंचावरील सरोवरे आणि, परवान्यासह, सीमेवरील बुम ला खिंड यांसह. वाटेत बोमडिला व दिरांग खोरे आहे. आपातानींचे झिरो खोरे, पाइनने वेढलेल्या भातशेतांसह व झिरो संगीत महोत्सवासह, सियांगच्या दूर पश्चिमेकडील मेचुका, सियांगकाठचे पासीघाट, आणि नामदफाची नदीकाठची जंगले शांत ठिकाणे शोधणाऱ्या प्रवाशांना खेचतात. इटानगरमध्ये इटा किल्ला व जवाहरलाल नेहरू राज्य संग्रहालय आहे, आणि लोहितवरील परशुराम कुंड जानेवारीत यात्रेकरूंना खेचते."),
        conf="Editorial"),
    lst("places", [
        it3("tawang", "Tawang", "तवांग", "तवांग", m=("Monastery, war memorial, lakes", "मठ, युद्ध स्मारक, झीलें", "मठ, युद्ध स्मारक, सरोवरे")),
        it3("dirang", "Bomdila and Dirang", "बोमडिला और दिरांग", "बोमडिला व दिरांग", m=("On the road to Tawang", "तवांग के मार्ग पर", "तवांगच्या वाटेवर")),
        it3("ziro", "Ziro valley", "ज़ीरो घाटी", "झिरो खोरे", m=("Apatani villages; music festival", "अपातानी गाँव; संगीत उत्सव", "आपातानी गावे; संगीत महोत्सव")),
        it3("mechuka", "Mechuka", "मेचुका", "मेचुका", m=("Remote valley in Shi Yomi", "शि योमी की सुदूर घाटी", "शि योमीतील दुर्गम खोरे")),
        it3("namdapha", "Namdapha", "नामदफा", "नामदफा", m=("Rainforest and wildlife", "वर्षावन और वन्यजीव", "वर्षावन व वन्यजीव")),
        it3("parshuram", "Parshuram Kund", "परशुराम कुंड", "परशुराम कुंड", m=("Makar Sankranti pilgrimage", "मकर संक्रांति तीर्थ", "मकरसंक्रांत यात्रा")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d6", "6 days (west)", "6 दिन (पश्चिम)", "6 दिवस (पश्चिम)", d=("Bhalukpong, Dirang, Sela and Tawang, returning via Bomdila.", "भालुकपोंग, दिरांग, सेला और तवांग, बोमडिला होकर वापसी।", "भालुकपोंग, दिरांग, सेला व तवांग, बोमडिलामार्गे परत.")),
        it3("d4", "4 days (centre)", "4 दिन (मध्य)", "4 दिवस (मध्य)", d=("Itanagar and the Ziro valley.", "ईटानगर और ज़ीरो घाटी।", "इटानगर व झिरो खोरे.")),
        it3("d5", "5 days (east)", "5 दिन (पूर्व)", "5 दिवस (पूर्व)", d=("Pasighat, Roing and Mayudia, or Namdapha from Miao.", "पासीघाट, रोइंग और मायुडिया, या मियाओ से नामदफा।", "पासीघाट, रोइंग व मायुडिया, किंवा मियाओहून नामदफा.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium / Arunachal Tourism."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "cities", [
    lst("cities", [
        city("itanagar", ("Itanagar", "ईटानगर", "इटानगर"), ("Capital in the Papum Pare foothills.", "पापुम पारे की तलहटी में राजधानी।", "पापुम पारेच्या पायथ्याशी राजधानी."), ("Capital", "राजधानी", "राजधानी")),
        city("naharlagun", ("Naharlagun", "नहारलगुन", "नाहरलगुन"), ("Twin town of Itanagar; railway station.", "ईटानगर का जुड़वाँ नगर; रेलवे स्टेशन।", "इटानगरचे जुळे शहर; रेल्वे स्थानक."), ("Commerce", "वाणिज्य", "व्यापार")),
        city("pasighat", ("Pasighat", "पासीघाट", "पासीघाट"), ("Founded in 1911; gateway to the Siang valley.", "1911 में स्थापित; सियांग घाटी का प्रवेश द्वार।", "1911 मध्ये स्थापन; सियांग खोऱ्याचे प्रवेशद्वार."), ("History", "इतिहास", "इतिहास")),
        city("tawang", ("Tawang", "तवांग", "तवांग"), ("Monastery town at about 3,000 m.", "लगभग 3,000 मीटर पर मठ नगर।", "सुमारे 3,000 मीटरवरील मठांचे शहर."), ("Heritage", "धरोहर", "वारसा")),
        city("ziro", ("Ziro", "ज़ीरो", "झिरो"), ("Apatani plateau town.", "अपातानी पठार का नगर।", "आपातानी पठारावरील शहर."), ("Culture", "संस्कृति", "संस्कृती")),
        city("tezu", ("Tezu", "तेज़ू", "तेझू"), ("Headquarters of Lohit district.", "लोहित ज़िले का मुख्यालय।", "लोहित जिल्ह्याचे मुख्यालय."), ("Administration", "प्रशासन", "प्रशासन")),
    ], title=L("Major towns", "प्रमुख नगर", "प्रमुख शहरे"), conf="Editorial"),
    gaps("g", [
        (L("List of districts — official", "ज़िलों की सूची — आधिकारिक", "जिल्ह्यांची यादी — अधिकृत"), "india-gov", "Government of Arunachal Pradesh; see the district-count note in the overview."),
        (L("Town populations (Census 2011)", "नगरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Mountaineering and adventure sports are a source of pride: Tine Mena became the first woman from Arunachal Pradesh to climb Everest in 2011, and Anshu Jamsenpa of Bomdila has climbed it several times. Weightlifting, archery, wushu, taekwondo and football are popular, and traditional games and indigenous sports are played at festivals. River rafting on the Siang and Kameng and paragliding draw adventure travellers.",
        "पर्वतारोहण और साहसिक खेल गर्व का विषय हैं: तिने मेना 2011 में एवरेस्ट पर चढ़ने वाली अरुणाचल प्रदेश की पहली महिला बनीं, और बोमडिला की अंशु जामसेनपा कई बार इस पर चढ़ चुकी हैं। भारोत्तोलन, तीरंदाज़ी, वुशु, ताइक्वांडो और फ़ुटबॉल लोकप्रिय हैं, और त्योहारों पर पारंपरिक और देशज खेल खेले जाते हैं। सियांग और कामेंग पर रिवर राफ़्टिंग और पैराग्लाइडिंग साहसिक यात्रियों को खींचते हैं।",
        "गिर्यारोहण व साहसी खेळ हा अभिमानाचा विषय आहे: तिने मेना 2011 मध्ये एव्हरेस्ट सर करणाऱ्या अरुणाचल प्रदेशच्या पहिल्या महिला ठरल्या, आणि बोमडिलाच्या अंशु जामसेनपा यांनी तो अनेक वेळा सर केला आहे. भारोत्तोलन, तिरंदाजी, वुशू, तायक्वांदो व फुटबॉल लोकप्रिय आहेत, आणि सणांना पारंपरिक व देशी खेळ खेळले जातात. सियांग व कामेंगवरील राफ्टिंग आणि पॅराग्लायडिंग साहसी प्रवाशांना खेचतात."),
        conf="Editorial"),
    gaps("g", [(L("Major stadiums — official list", "प्रमुख स्टेडियम — आधिकारिक सूची", "प्रमुख स्टेडियम — अधिकृत यादी"), "india-gov", "Department of Sports and Youth Affairs, Arunachal Pradesh.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("tsangyang", ("Tsangyang Gyatso", "त्सांगयांग ग्यात्सो", "त्सांगयांग ग्यात्सो"), ("The sixth Dalai Lama, born near Tawang in the 17th century and remembered for his love poems.", "छठे दलाई लामा, 17वीं सदी में तवांग के पास जन्मे, अपनी प्रेम कविताओं के लिए याद किए जाते हैं।", "सहावे दलाई लामा, सतराव्या शतकात तवांगजवळ जन्मलेले, आपल्या प्रेमकवितांसाठी स्मरणात."), ("Religion and poetry", "धर्म और कविता", "धर्म व काव्य")),
        person("talom", ("Talom Rukbo", "तालोम रुकबो", "तालोम रुकबो"), ("Adi thinker who led the revival of the indigenous Donyi-Polo faith.", "आदी विचारक जिन्होंने देशज दोन्यी-पोलो आस्था के पुनरुद्धार का नेतृत्व किया।", "आदी विचारवंत, ज्यांनी देशी दोन्यी-पोलो श्रद्धेच्या पुनरुज्जीवनाचे नेतृत्व केले."), ("Culture", "संस्कृति", "संस्कृती")),
        person("mamang", ("Mamang Dai", "मामांग दाई", "मामांग दाई"), ("Writer, poet and former journalist; Padma Shri awardee.", "लेखिका, कवयित्री और पूर्व पत्रकार; पद्म श्री सम्मानित।", "लेखिका, कवयित्री व माजी पत्रकार; पद्मश्री सन्मानित."), ("Literature", "साहित्य", "साहित्य")),
        person("thongchi", ("Yeshe Dorjee Thongchi", "येशे दोरजी थोंगची", "येशे दोरजी थोंगची"), ("Novelist writing in Assamese; Sahitya Akademi awardee.", "असमिया में लिखने वाले उपन्यासकार; साहित्य अकादमी पुरस्कार विजेता।", "आसामीत लिहिणारे कादंबरीकार; साहित्य अकादमी पुरस्कार विजेते."), ("Literature", "साहित्य", "साहित्य")),
        person("tinemena", ("Tine Mena", "तिने मेना", "तिने मेना"), ("Mountaineer; first woman from the State to summit Everest (2011).", "पर्वतारोही; एवरेस्ट पर पहुँचने वाली राज्य की पहली महिला (2011)।", "गिर्यारोहक; एव्हरेस्ट सर करणाऱ्या राज्याच्या पहिल्या महिला (2011)."), ("Sport", "खेल", "क्रीडा")),
        person("anshu", ("Anshu Jamsenpa", "अंशु जामसेनपा", "अंशु जामसेनपा"), ("Mountaineer from Bomdila who has climbed Everest several times.", "बोमडिला की पर्वतारोही जो कई बार एवरेस्ट पर चढ़ चुकी हैं।", "बोमडिलाच्या गिर्यारोहक, ज्यांनी एव्हरेस्ट अनेकदा सर केला आहे."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Arunachal Pradesh has a small diaspora. Students and workers from the State live in Guwahati, Shillong, Delhi, Bengaluru and Pune, and the Monpa, Khamti and Singpho share family and religious ties with communities across the borders in Bhutan, Myanmar and Tibet.",
        "अरुणाचल प्रदेश का प्रवासी समुदाय छोटा है। राज्य के छात्र और कामगार गुवाहाटी, शिलांग, दिल्ली, बेंगलुरु और पुणे में रहते हैं, और मोनपा, खामती और सिंगफ़ो भूटान, म्यांमार और तिब्बत की सीमाओं के पार के समुदायों से पारिवारिक और धार्मिक संबंध रखते हैं।",
        "अरुणाचल प्रदेशचा प्रवासी समुदाय लहान आहे. राज्यातील विद्यार्थी व कामगार गुवाहाटी, शिलाँग, दिल्ली, बंगळुरू व पुण्यात राहतात, आणि मोनपा, खामती व सिंगफो भूतान, म्यानमार व तिबेटच्या सीमांपलीकडील समुदायांशी कौटुंबिक व धार्मिक नाते जपतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Out-migration from the State — official estimate", "राज्य से बाहर प्रवास — आधिकारिक अनुमान", "राज्याबाहेर स्थलांतर — अधिकृत अंदाज"), "census", "Census 2011 migration tables (D-series)."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Arunachal Pradesh portal", "अरुणाचल प्रदेश सरकार पोर्टल", "अरुणाचल प्रदेश शासन संकेतस्थळ", url="https://arunachalpradesh.gov.in", src="india-gov"),
        it3("lokbhavan", "Lok Bhavan Arunachal Pradesh", "लोक भवन अरुणाचल प्रदेश", "लोक भवन अरुणाचल प्रदेश", url="https://arunachalgovernor.gov.in", src="ar-governor"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD code", "एसटीडी कोड", "एसटीडी कोड"),
          [col(L("Area", "क्षेत्र", "क्षेत्र")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Itanagar", "ईटानगर", "इटानगर"), "0360"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial; other districts have their own codes. To be checked against the Department of Telecommunications numbering plan.", "संपादकीय; अन्य ज़िलों के अपने कोड हैं। दूरसंचार विभाग की नंबरिंग योजना से जाँचा जाएगा।", "संपादकीय; इतर जिल्ह्यांचे स्वतंत्र कोड आहेत. दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळले जाईल.")),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("area", ("At 83,743 km², Arunachal Pradesh is the largest State in the North-East.", "83,743 वर्ग किमी के साथ अरुणाचल प्रदेश पूर्वोत्तर का सबसे बड़ा राज्य है।", "83,743 चौ.किमीसह अरुणाचल प्रदेश हे ईशान्येतील सर्वांत मोठे राज्य आहे."), LS_FOREST, "fsi"),
        triv("density", ("It is India's most thinly populated State — about 17 people per km² in 2011.", "यह भारत का सबसे विरल आबादी वाला राज्य है — 2011 में प्रति वर्ग किमी लगभग 17 लोग।", "हे भारतातील सर्वांत विरळ लोकवस्तीचे राज्य आहे — 2011 मध्ये प्रति चौ.किमी सुमारे 17 लोक."), "https://statistics.py.gov.in/state-wise-population", "census"),
        triv("csr", ("Its child sex ratio of 972 in 2011 was the highest among the regions profiled here.", "2011 में इसका 972 का शिशु लिंगानुपात यहाँ प्रोफ़ाइल किए गए क्षेत्रों में सबसे ऊँचा था।", "2011 मधील त्याचे 972 बाल लिंग गुणोत्तर येथे प्रोफाइल केलेल्या प्रदेशांत सर्वाधिक होते."), PIB_CSR, "pib"),
        triv("gi", ("Twenty-one GIs are registered for the State, most of them tribal textiles.", "राज्य के लिए इक्कीस जीआई पंजीकृत हैं, जिनमें अधिकांश जनजातीय वस्त्र हैं।", "राज्यासाठी एकवीस जीआय नोंदणीकृत आहेत, ज्यांपैकी बहुतेक आदिवासी वस्त्रे आहेत."), GI_PDF, "gi-registry"),
        triv("english", ("English is the official language of Arunachal Pradesh.", "अंग्रेज़ी अरुणाचल प्रदेश की राजभाषा है।", "इंग्रजी ही अरुणाचल प्रदेशची राजभाषा आहे.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("ar mod3 ok")
