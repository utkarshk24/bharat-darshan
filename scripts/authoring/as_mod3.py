"""Assam modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-AS"
asm = read("regions/IN-AS.json")["metrics"]; ind = read("india.json")["metrics"]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Assam lies in one of the world's biodiversity hotspots, and about 36% of the State is forest (ISFR 2023). Kaziranga National Park, a mosaic of tall grassland, beels and forest on the Brahmaputra floodplain, shelters most of the world's greater one-horned rhinoceroses as well as tigers, wild water buffalo, swamp deer and elephants. Manas, on the Bhutan border, is a tiger and elephant reserve and a home of the golden langur and the pygmy hog. Pobitora has one of the densest rhino populations anywhere, Orang and Nameri are other tiger reserves, Dibru-Saikhowa protects feral horses and riverine forests, and the Hoollongapar Gibbon Sanctuary is named for India's only ape. The Gangetic dolphin lives in the Brahmaputra.\n\nDeepor Beel, a large wetland on the edge of Guwahati, is the State's only Ramsar site, designated in 2002.",
        "असम विश्व के जैव विविधता हॉटस्पॉट में से एक में स्थित है, और राज्य का लगभग 36% भाग वन है (आईएसएफ़आर 2023)। ब्रह्मपुत्र के बाढ़ मैदान पर ऊँची घास, बील और वनों का मिश्रण काज़ीरंगा राष्ट्रीय उद्यान विश्व के अधिकांश एक सींग वाले गैंडों के साथ बाघों, जंगली भैंसों, बारहसिंगा और हाथियों को आश्रय देता है। भूटान सीमा पर मानस बाघ और हाथी अभयारण्य है और सुनहरे लंगूर व पिग्मी हॉग का घर है। पबितरा में दुनिया में सबसे घनी गैंडा आबादियों में से एक है, ओरंग और नामेरी अन्य बाघ अभयारण्य हैं, डिब्रू-सैखोवा जंगली घोड़ों और नदी-तटीय वनों की रक्षा करता है, और होलोंगापार गिब्बन अभयारण्य भारत के एकमात्र कपि के नाम पर है। ब्रह्मपुत्र में गंगा डॉल्फ़िन रहती है।\n\nगुवाहाटी के किनारे की बड़ी आर्द्रभूमि दीपोर बील राज्य का एकमात्र रामसर स्थल है, जो 2002 में घोषित हुआ।",
        "आसाम जगातील जैवविविधता हॉटस्पॉटपैकी एकात आहे, आणि राज्याचा सुमारे 36% भाग वनाच्छादित आहे (आयएसएफआर 2023). ब्रह्मपुत्रेच्या पूरमैदानावरील उंच गवताळ प्रदेश, बील व जंगलांचे मिश्रण असलेले काझीरंगा राष्ट्रीय उद्यान जगातील बहुतेक एकशिंगी गेंड्यांसह वाघ, रानरेडे, बाराशिंगे व हत्तींना आश्रय देते. भूतान सीमेवरील मानस हा व्याघ्र व हत्ती प्रकल्प असून सोनेरी वानर व पिग्मी हॉगचे घर आहे. पोबितोरामध्ये जगातील सर्वाधिक घनतेच्या गेंडा लोकसंख्येपैकी एक आहे, ओरांग व नामेरी हे इतर व्याघ्र प्रकल्प आहेत, डिब्रू-सैखोवा रानटी घोडे व नदीकाठच्या जंगलांचे रक्षण करते, आणि होलोंगापार गिबन अभयारण्य भारतातील एकमेव कपीच्या नावाने आहे. ब्रह्मपुत्रेत गंगा डॉल्फिन राहते.\n\nगुवाहाटीच्या कडेला असलेले मोठे पाणथळ दीपोर बील हे राज्यातील एकमेव रामसर स्थळ आहे, जे 2002 मध्ये घोषित झाले."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(28313.55, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(28325.31, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), asm["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(1, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026: Deepor Beel, 4,000 ha, designated 19 August 2002."), "number"),
    ]),
    lst("protected", [
        it3("kaziranga", "Kaziranga National Park and Tiger Reserve", "काज़ीरंगा राष्ट्रीय उद्यान और बाघ अभयारण्य", "काझीरंगा राष्ट्रीय उद्यान व व्याघ्र प्रकल्प", m=("UNESCO; one-horned rhino", "यूनेस्को; एक सींग वाला गैंडा", "युनेस्को; एकशिंगी गेंडा")),
        it3("manas", "Manas National Park and Tiger Reserve", "मानस राष्ट्रीय उद्यान और बाघ अभयारण्य", "मानस राष्ट्रीय उद्यान व व्याघ्र प्रकल्प", m=("UNESCO; golden langur", "यूनेस्को; सुनहरा लंगूर", "युनेस्को; सोनेरी वानर")),
        it3("orang", "Orang National Park", "ओरंग राष्ट्रीय उद्यान", "ओरांग राष्ट्रीय उद्यान", m=("Tiger reserve", "बाघ अभयारण्य", "व्याघ्र प्रकल्प")),
        it3("nameri", "Nameri National Park", "नामेरी राष्ट्रीय उद्यान", "नामेरी राष्ट्रीय उद्यान", m=("Tiger reserve", "बाघ अभयारण्य", "व्याघ्र प्रकल्प")),
        it3("pobitora", "Pobitora Wildlife Sanctuary", "पबितरा वन्यजीव अभयारण्य", "पोबितोरा वन्यजीव अभयारण्य", m=("Rhinos near Guwahati", "गुवाहाटी के पास गैंडे", "गुवाहाटीजवळ गेंडे")),
        it3("dibru", "Dibru-Saikhowa National Park", "डिब्रू-सैखोवा राष्ट्रीय उद्यान", "डिब्रू-सैखोवा राष्ट्रीय उद्यान", m=("Feral horses; riverine forest", "जंगली घोड़े; नदी-तटीय वन", "रानटी घोडे; नदीकाठची जंगले")),
        it3("hoollongapar", "Hoollongapar Gibbon Sanctuary", "होलोंगापार गिब्बन अभयारण्य", "होलोंगापार गिबन अभयारण्य", m=("Hoolock gibbon", "हूलॉक गिब्बन", "हुलॉक गिबन")),
        it3("deepor", "Deepor Beel", "दीपोर बील", "दीपोर बील", m=("Ramsar site", "रामसर स्थल", "रामसर स्थळ")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("rhino", "Greater one-horned rhinoceros (State animal)", "एक सींग वाला गैंडा (राज्य पशु)", "एकशिंगी गेंडा (राज्यप्राणी)"), it3("tiger", "Tiger", "बाघ", "वाघ"),
        it3("langur", "Golden langur", "सुनहरा लंगूर", "सोनेरी वानर"), it3("pygmyhog", "Pygmy hog", "पिग्मी हॉग", "पिग्मी हॉग"),
        it3("gibbon", "Hoolock gibbon", "हूलॉक गिब्बन", "हुलॉक गिबन"), it3("woodduck", "White-winged wood duck (State bird)", "सफ़ेद पंखों वाली वन बत्तख़ (राज्य पक्षी)", "पांढऱ्या पंखांचे वनबदक (राज्यपक्षी)"),
        it3("dolphin", "Gangetic dolphin", "गंगा डॉल्फ़िन", "गंगा डॉल्फिन"), it3("adjutant", "Greater adjutant stork", "गरुड़ (बड़ा गरुड़ बगुला)", "मोठा करकोचा (हाडगिला)"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Rhino census (Kaziranga and State)", "गैंडा गणना (काज़ीरंगा और राज्य)", "गेंडा गणना (काझीरंगा व राज्य)"), "india-gov", "Assam Forest Department rhino estimation."),
        (L("Tiger estimate", "बाघों का अनुमान", "वाघांचा अंदाज"), "ntca", "NTCA All India Tiger Estimation."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Water defines Assam. The Brahmaputra carries one of the heaviest sediment loads of any large river, and its channels shift constantly; together with its tributaries from the Himalaya, it floods large parts of the valley almost every year, while bank erosion has destroyed villages and steadily shrunk Majuli island. The Barak valley also suffers severe floods. Embankments line much of the river, and the Brahmaputra Board plans flood control and drainage. Beels and wetlands store floodwater and support fisheries. Groundwater is plentiful but affected in places by arsenic, fluoride and iron, and piped drinking water under the Jal Jeevan Mission has been expanding.",
        "पानी असम की पहचान है। ब्रह्मपुत्र किसी भी बड़ी नदी में सबसे भारी गाद ले जाने वाली नदियों में से है, और इसकी धाराएँ लगातार बदलती हैं; हिमालय से आने वाली सहायक नदियों के साथ यह लगभग हर वर्ष घाटी के बड़े भागों में बाढ़ लाती है, जबकि तट कटाव ने गाँवों को नष्ट किया है और माजुली द्वीप को लगातार सिकोड़ा है। बराक घाटी भी भीषण बाढ़ झेलती है। नदी के बड़े भाग पर तटबंध हैं, और ब्रह्मपुत्र बोर्ड बाढ़ नियंत्रण और जल-निकासी की योजना बनाता है। बील और आर्द्रभूमियाँ बाढ़ का पानी रोकती हैं और मत्स्य पालन का आधार हैं। भूजल प्रचुर है लेकिन कुछ स्थानों पर आर्सेनिक, फ़्लोराइड और लौह से प्रभावित है, और जल जीवन मिशन के तहत नल से पेयजल का विस्तार हो रहा है।",
        "पाणी ही आसामची ओळख आहे. ब्रह्मपुत्रा ही कोणत्याही मोठ्या नदीपैकी सर्वाधिक गाळ वाहून नेणाऱ्या नद्यांपैकी एक असून तिचे प्रवाह सतत बदलतात; हिमालयातून येणाऱ्या उपनद्यांसह ती जवळपास दरवर्षी खोऱ्याच्या मोठ्या भागात पूर आणते, तर किनारा-धूपीने गावे उद्ध्वस्त केली आहेत व माजुली बेट सतत आकुंचित केले आहे. बराक खोरेही तीव्र पूर सोसते. नदीच्या बऱ्याच भागावर बांध आहेत, आणि ब्रह्मपुत्रा मंडळ पूरनियंत्रण व निचऱ्याचे नियोजन करते. बील व पाणथळे पुराचे पाणी साठवतात व मत्स्यव्यवसायाला आधार देतात. भूजल मुबलक आहे पण काही ठिकाणी आर्सेनिक, फ्लोराइड व लोहाने बाधित आहे, आणि जलजीवन मिशनअंतर्गत नळाद्वारे पिण्याच्या पाण्याचा विस्तार होत आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Flood-affected population and area by year", "वर्षवार बाढ़ प्रभावित जनसंख्या और क्षेत्र", "वर्षनिहाय पूरग्रस्त लोकसंख्या व क्षेत्र"), "india-gov", "ASDMA flood reports."),
        (L("Land lost to erosion", "कटाव से नष्ट भूमि", "धूपीने गेलेली जमीन"), "india-gov", "Assam Water Resources Department / Brahmaputra Board."),
        (L("Arsenic- and fluoride-affected habitations", "आर्सेनिक और फ़्लोराइड प्रभावित बस्तियाँ", "आर्सेनिक व फ्लोराइडबाधित वस्त्या"), "india-gov", "Jal Jeevan Mission water-quality data."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Floods and erosion affect Assam in most years, displacing people and damaging crops, roads and the national parks. The State lies in one of India's most earthquake-prone regions: the great earthquakes of 1897 and 1950 caused widespread destruction, and moderate quakes are frequent. Landslides strike Guwahati's hills and Dima Hasao in heavy rain, lightning and storms are common in spring, and urban flooding affects Guwahati.\n\nVisitors should check ASDMA and IMD advisories during the monsoon; Kaziranga and Manas usually close from about May to October.",
        "बाढ़ और कटाव अधिकांश वर्षों में असम को प्रभावित करते हैं, लोगों को विस्थापित करते हैं और फ़सलों, सड़कों और राष्ट्रीय उद्यानों को नुकसान पहुँचाते हैं। राज्य भारत के सबसे भूकंप-प्रवण क्षेत्रों में है: 1897 और 1950 के महान भूकंपों ने व्यापक विनाश किया, और मध्यम भूकंप अक्सर आते हैं। भारी वर्षा में गुवाहाटी की पहाड़ियों और दिमा हसाओ में भूस्खलन होते हैं, वसंत में आकाशीय बिजली और आँधियाँ आम हैं, और गुवाहाटी में शहरी जलभराव होता है।\n\nपर्यटकों को मानसून में एएसडीएमए और आईएमडी की सलाह देखनी चाहिए; काज़ीरंगा और मानस प्रायः मई से अक्टूबर के आसपास तक बंद रहते हैं।",
        "पूर व धूप बहुतेक वर्षी आसामला बाधित करतात, लोकांना विस्थापित करतात आणि पिके, रस्ते व राष्ट्रीय उद्यानांचे नुकसान करतात. राज्य भारतातील सर्वाधिक भूकंपप्रवण प्रदेशांपैकी एकात आहे: 1897 व 1950 च्या महाभूकंपांनी मोठा विध्वंस केला, आणि मध्यम भूकंप वारंवार होतात. मुसळधार पावसात गुवाहाटीच्या डोंगरांत व दिमा हसाओत भूस्खलन होते, वसंतात वीज व वादळे सामान्य आहेत, आणि गुवाहाटीत शहरी पूर येतो.\n\nपर्यटकांनी पावसाळ्यात एएसडीएमए व आयएमडीच्या सूचना तपासाव्यात; काझीरंगा व मानस सहसा मे ते ऑक्टोबरच्या सुमारास बंद असतात."),
        conf="Editorial"),
    emergency_table(("Assam", "असम", "आसाम")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("asdma", "Assam State Disaster Management Authority", "असम राज्य आपदा प्रबंधन प्राधिकरण", "आसाम राज्य आपत्ती व्यवस्थापन प्राधिकरण", url="https://asdma.assam.gov.in", src="india-gov"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Flood deaths and damage by year", "वर्षवार बाढ़ से मौतें और नुकसान", "वर्षनिहाय पुरातील मृत्यू व नुकसान"), "india-gov", "ASDMA."),
        (L("Park opening and closing dates", "उद्यान खुलने और बंद होने की तिथियाँ", "उद्याने उघडण्या-बंद होण्याच्या तारखा"), "india-gov", "Assam Forest Department notices."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Assam has 42 entries in the GI Registry's list as on 31 December 2025 — more than most States — including two shared with Arunachal Pradesh: Singpho phalap (Singpho tea) and Mising handloom products. Assam Orthodox tea and muga silk were among the early registrations. In 2022 a large group of Bodo products was registered together: textiles such as the aronai scarf, dokhona and eri silk; foods such as napham fermented fish and ondla; musical instruments such as the kham drum and sifung flute; and traditional rice beers. Other GIs include Joha, Boka and Chokuwa rice, Karbi Anglong ginger, Tezpur litchi, Kaji nemu lemon, the gamosa, Majuli masks and manuscript painting, the jaapi, Bihu dhol, Sarthebari bell-metal, Asharikandi terracotta, Pani Meteka craft and Assamese jewellery.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में असम की 42 प्रविष्टियाँ हैं — अधिकांश राज्यों से अधिक — जिनमें अरुणाचल प्रदेश के साथ साझा दो हैं: सिंगफो फलाप (सिंगफो चाय) और मिसिंग हथकरघा उत्पाद। असम ऑर्थोडॉक्स चाय और मूगा रेशम शुरुआती पंजीकरणों में थे। 2022 में बोडो उत्पादों का एक बड़ा समूह एक साथ पंजीकृत हुआ: अरोनाई दुपट्टा, दोखोना और एरी रेशम जैसे वस्त्र; नाफाम ख़मीरी मछली और ओंदला जैसे खाद्य; खाम ढोल और सिफुंग बाँसुरी जैसे वाद्य; और पारंपरिक चावल की शराब। अन्य जीआई में जोहा, बोका और चोकुवा चावल, कार्बी आंगलोंग अदरक, तेजपुर लीची, काजी नेमू नींबू, गमोसा, माजुली मुखौटे और पांडुलिपि चित्रकला, जापी, बिहू ढोल, सार्थेबाड़ी काँसा, आशारीकांदी टेराकोटा, पानी मेटेका शिल्प और असमिया आभूषण शामिल हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत आसामच्या 42 नोंदी आहेत — बहुतेक राज्यांपेक्षा अधिक — ज्यांत अरुणाचल प्रदेशासोबत सामायिक दोन आहेत: सिंगफो फलाप (सिंगफो चहा) व मिसिंग हातमाग उत्पादने. आसाम ऑर्थोडॉक्स चहा व मुगा रेशीम या सुरुवातीच्या नोंदण्यांपैकी होत्या. 2022 मध्ये बोडो उत्पादनांचा एक मोठा गट एकत्र नोंदला गेला: अरोनाई ओढणी, दोखोना व एरी रेशीम यांसारखी वस्त्रे; नाफाम आंबवलेला मासा व ओंदला यांसारखे खाद्यपदार्थ; खाम ढोल व सिफुंग बासरी यांसारखी वाद्ये; आणि पारंपरिक तांदळाची मद्ये. इतर जीआयमध्ये जोहा, बोका व चोकुवा तांदूळ, कार्बी आंगलोंग आले, तेजपूर लिची, काजी नेमू लिंबू, गमोसा, माजुली मुखवटे व हस्तलिखित चित्रकला, जापी, बिहू ढोल, सार्थेबारीचे काशाचे काम, आशारीकांदी टेराकोटा, पानी मेटेका हस्तकला व आसामी दागिने यांचा समावेश आहे."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Registration year and producing region for each GI", "हर जीआई का पंजीकरण वर्ष और उत्पादन क्षेत्र", "प्रत्येक जीआयचे नोंदणी वर्ष व उत्पादन क्षेत्र"), "gi-registry", "GI public search, certificate details."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Kaziranga, with jeep and elephant safaris among rhinos, is Assam's best-known destination, and Manas, Pobitora, Nameri and Dibru-Saikhowa offer quieter wildlife experiences. Guwahati has the Kamakhya temple on Nilachal hill, Umananda island in the Brahmaputra and river cruises. Majuli's satras, mask-makers and Mising villages, Sivasagar's Ahom monuments and the Charaideo Moidams tell Assam's history, and tea-estate bungalows around Jorhat and Dibrugarh offer stays among the gardens. Hajo is a meeting point of Hindu, Buddhist and Muslim pilgrimage, and Haflong in Dima Hasao is the State's only hill station.",
        "गैंडों के बीच जीप और हाथी सफ़ारी वाला काज़ीरंगा असम का सबसे प्रसिद्ध गंतव्य है, और मानस, पबितरा, नामेरी और डिब्रू-सैखोवा शांत वन्यजीव अनुभव देते हैं। गुवाहाटी में नीलाचल पहाड़ी पर कामाख्या मंदिर, ब्रह्मपुत्र में उमानंद द्वीप और नदी क्रूज़ हैं। माजुली के सत्र, मुखौटा बनाने वाले और मिसिंग गाँव, शिवसागर के अहोम स्मारक और चराइदेउ मोइदाम असम का इतिहास बताते हैं, और जोरहाट व डिब्रूगढ़ के आसपास चाय बाग़ानों के बंगले बाग़ों के बीच रहने का अवसर देते हैं। हाजो हिंदू, बौद्ध और मुस्लिम तीर्थों का संगम है, और दिमा हसाओ का हाफ़लोंग राज्य का एकमात्र पहाड़ी स्थल है।",
        "गेंड्यांमध्ये जीप व हत्ती सफारी असलेले काझीरंगा हे आसामचे सर्वांत प्रसिद्ध ठिकाण आहे, आणि मानस, पोबितोरा, नामेरी व डिब्रू-सैखोवा शांत वन्यजीव अनुभव देतात. गुवाहाटीत नीलाचल टेकडीवर कामाख्या मंदिर, ब्रह्मपुत्रेत उमानंद बेट व नदीसफरी आहेत. माजुलीचे सत्र, मुखवटे घडवणारे कारागीर व मिसिंग गावे, शिवसागरची अहोम स्मारके व चराइदेव मोइदाम आसामचा इतिहास सांगतात, आणि जोरहाट व डिब्रुगडभोवतीचे चहामळ्यांतील बंगले बागांमध्ये राहण्याची संधी देतात. हाजो हे हिंदू, बौद्ध व मुस्लिम तीर्थांचा संगम आहे, आणि दिमा हसाओतील हाफलोंग हे राज्यातील एकमेव थंड हवेचे ठिकाण आहे."),
        conf="Editorial"),
    lst("places", [
        it3("kaziranga", "Kaziranga", "काज़ीरंगा", "काझीरंगा", m=("UNESCO; rhinos", "यूनेस्को; गैंडे", "युनेस्को; गेंडे")),
        it3("kamakhya", "Guwahati and Kamakhya", "गुवाहाटी और कामाख्या", "गुवाहाटी व कामाख्या", m=("Temple; river cruises", "मंदिर; नदी क्रूज़", "मंदिर; नदीसफर")),
        it3("majuli", "Majuli", "माजुली", "माजुली", m=("River island; satras", "नदी द्वीप; सत्र", "नदी-बेट; सत्र")),
        it3("sivasagar", "Sivasagar and Charaideo", "शिवसागर और चराइदेउ", "शिवसागर व चराइदेव", m=("Ahom heritage", "अहोम धरोहर", "अहोम वारसा")),
        it3("manas", "Manas", "मानस", "मानस", m=("UNESCO; wildlife", "यूनेस्को; वन्यजीव", "युनेस्को; वन्यजीव")),
        it3("tea", "Jorhat and Dibrugarh tea estates", "जोरहाट और डिब्रूगढ़ के चाय बाग़ान", "जोरहाट व डिब्रुगडचे चहामळे", m=("Tea tourism", "चाय पर्यटन", "चहा पर्यटन")),
        it3("haflong", "Haflong", "हाफ़लोंग", "हाफलोंग", m=("Hill station", "पहाड़ी स्थल", "थंड हवेचे ठिकाण")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Guwahati: Kamakhya, Umananda, a Brahmaputra cruise and Pobitora.", "गुवाहाटी: कामाख्या, उमानंद, ब्रह्मपुत्र क्रूज़ और पबितरा।", "गुवाहाटी: कामाख्या, उमानंद, ब्रह्मपुत्रा सफर व पोबितोरा.")),
        it3("d4", "4 days", "4 दिन", "4 दिवस", d=("Guwahati and two days in Kaziranga.", "गुवाहाटी और काज़ीरंगा में दो दिन।", "गुवाहाटी व काझीरंग्यात दोन दिवस.")),
        it3("d7", "7 days", "7 दिन", "7 दिवस", d=("Guwahati, Kaziranga, Majuli, Sivasagar and a tea-estate stay near Jorhat.", "गुवाहाटी, काज़ीरंगा, माजुली, शिवसागर और जोरहाट के पास चाय बाग़ान में ठहराव।", "गुवाहाटी, काझीरंगा, माजुली, शिवसागर व जोरहाटजवळ चहामळ्यात मुक्काम.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("at", "Assam Tourism (official)", "असम पर्यटन (आधिकारिक)", "आसाम पर्यटन (अधिकृत)", url="https://tourism.assam.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "cities", [
    lst("cities", [
        city("guwahati", ("Guwahati", "गुवाहाटी", "गुवाहाटी"), ("Largest city of the north-east; Dispur, the capital, lies within it.", "पूर्वोत्तर का सबसे बड़ा शहर; राजधानी दिसपुर इसके भीतर है।", "ईशान्येतील सर्वांत मोठे शहर; राजधानी दिसपूर त्यातच आहे."), ("Capital region", "राजधानी क्षेत्र", "राजधानी क्षेत्र")),
        city("silchar", ("Silchar", "सिलचर", "सिलचर"), ("Main town of the Barak valley.", "बराक घाटी का मुख्य नगर।", "बराक खोऱ्याचे मुख्य शहर."), ("Barak valley", "बराक घाटी", "बराक खोरे")),
        city("dibrugarh", ("Dibrugarh", "डिब्रूगढ़", "डिब्रुगड"), ("Tea city of Upper Assam on the Brahmaputra.", "ब्रह्मपुत्र पर ऊपरी असम का चाय नगर।", "ब्रह्मपुत्रेकाठचे वरच्या आसामचे चहानगर."), ("Tea", "चाय", "चहा")),
        city("jorhat", ("Jorhat", "जोरहाट", "जोरहाट"), ("Cultural and educational centre; gateway to Majuli.", "सांस्कृतिक और शैक्षिक केंद्र; माजुली का प्रवेश द्वार।", "सांस्कृतिक व शैक्षणिक केंद्र; माजुलीचे प्रवेशद्वार."), ("Culture", "संस्कृति", "संस्कृती")),
        city("nagaon", ("Nagaon", "नगाँव", "नगाव"), ("Central Assam town; birthplace region of Sankardeva.", "मध्य असम का नगर; शंकरदेव की जन्मभूमि का क्षेत्र।", "मध्य आसामचे शहर; शंकरदेवांच्या जन्मभूमीचा प्रदेश."), ("Central", "मध्य", "मध्य")),
        city("tezpur", ("Tezpur", "तेजपुर", "तेजपूर"), ("Historic town on the north bank; Tezpur litchi.", "उत्तरी तट पर ऐतिहासिक नगर; तेजपुर लीची।", "उत्तर किनाऱ्यावरील ऐतिहासिक शहर; तेजपूर लिची."), ("North bank", "उत्तरी तट", "उत्तर किनारा")),
        city("tinsukia", ("Tinsukia and Digboi", "तिनसुकिया और डिगबोई", "तिनसुकिया व डिगबोई"), ("Oil and tea towns of the far east.", "सुदूर पूर्व के तेल और चाय नगर।", "अगदी पूर्वेकडील तेल व चहा शहरे."), ("Oil", "तेल", "तेल")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    gaps("g", [
        (L("Current number and list of districts", "ज़िलों की वर्तमान संख्या और सूची", "जिल्ह्यांची सध्याची संख्या व यादी"), "india-gov", "Assam's districts were merged and re-formed in 2022–24; link the State's current notification before listing them."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Football is hugely popular in Assam, and Guwahati is home to the NorthEast United club. Boxer Lovlina Borgohain won an Olympic bronze medal at Tokyo, sprinter Hima Das became the first Indian to win a track gold at the World U20 Championships in 2018, and Shiva Thapa is a multiple Asian medallist in boxing. Bhogeswar Baruah won Asian Games gold in athletics in 1966. Guwahati's Barsapara cricket stadium hosts international matches, and the Indira Gandhi Athletic Stadium at Sarusajai hosted the 2016 South Asian Games. Traditional sports include buffalo and bulbul contests at Bihu (now regulated), boat races and the indigenous martial art of the Bodo.",
        "असम में फ़ुटबॉल बहुत लोकप्रिय है, और गुवाहाटी नॉर्थईस्ट यूनाइटेड क्लब का घर है। मुक्केबाज़ लवलीना बोरगोहेन ने टोक्यो में ओलंपिक कांस्य पदक जीता, धाविका हिमा दास 2018 में विश्व अंडर-20 चैंपियनशिप में ट्रैक स्वर्ण जीतने वाली पहली भारतीय बनीं, और शिव थापा मुक्केबाज़ी में कई बार एशियाई पदक विजेता हैं। भोगेश्वर बरुआ ने 1966 में एथलेटिक्स में एशियाई खेलों का स्वर्ण जीता। गुवाहाटी का बरसापारा क्रिकेट स्टेडियम अंतरराष्ट्रीय मैचों की मेज़बानी करता है, और सरुसजाई के इंदिरा गांधी एथलेटिक स्टेडियम ने 2016 के दक्षिण एशियाई खेलों की मेज़बानी की। पारंपरिक खेलों में बिहू पर भैंस और बुलबुल की लड़ाइयाँ (अब नियंत्रित), नौका दौड़ और बोडो समुदाय की देशी युद्धकला शामिल हैं।",
        "आसाममध्ये फुटबॉल अत्यंत लोकप्रिय आहे, आणि गुवाहाटी हे नॉर्थईस्ट युनायटेड क्लबचे घर आहे. मुष्टियोद्धा लवलिना बोरगोहेन यांनी टोकियोत ऑलिम्पिक कांस्य जिंकले, धावपटू हिमा दास 2018 मध्ये जागतिक 20 वर्षांखालील स्पर्धेत ट्रॅकवर सुवर्ण जिंकणाऱ्या पहिल्या भारतीय ठरल्या, आणि शिवा थापा मुष्टियुद्धात अनेकदा आशियाई पदकविजेते आहेत. भोगेश्वर बरुआ यांनी 1966 मध्ये ॲथलेटिक्समध्ये आशियाई स्पर्धेचे सुवर्ण जिंकले. गुवाहाटीचे बरसापारा क्रिकेट स्टेडियम आंतरराष्ट्रीय सामने आयोजित करते, आणि सरुसजाई येथील इंदिरा गांधी ॲथलेटिक स्टेडियमने 2016 च्या दक्षिण आशियाई स्पर्धा आयोजित केल्या. पारंपरिक खेळांत बिहूला म्हशी व बुलबुलांच्या झुंजी (आता नियमित), नौकाशर्यती व बोडो समुदायाची देशी युद्धकला यांचा समावेश आहे."),
        conf="Editorial"),
    lst("venues", [
        it3("barsapara", "Barsapara Cricket Stadium, Guwahati", "बरसापारा क्रिकेट स्टेडियम, गुवाहाटी", "बरसापारा क्रिकेट स्टेडियम, गुवाहाटी"),
        it3("sarusajai", "Indira Gandhi Athletic Stadium, Sarusajai", "इंदिरा गांधी एथलेटिक स्टेडियम, सरुसजाई", "इंदिरा गांधी ॲथलेटिक स्टेडियम, सरुसजाई"),
        it3("nehru", "Nehru Stadium, Guwahati", "नेहरू स्टेडियम, गुवाहाटी", "नेहरू स्टेडियम, गुवाहाटी"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic and Asian Games medallists from Assam (official list)", "असम के ओलंपिक और एशियाई खेल पदक विजेता (आधिकारिक सूची)", "आसामचे ऑलिम्पिक व आशियाई स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Assam Sports and Youth Welfare Department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("sukaphaa", ("Sukaphaa", "सुकाफ़ा", "सुकाफा"), ("Founder of the Ahom kingdom in 1228; 2 December is observed as Asom Divas in his memory.", "1228 में अहोम राज्य के संस्थापक; उनकी स्मृति में 2 दिसंबर को असम दिवस मनाया जाता है।", "1228 मध्ये अहोम राज्याचे संस्थापक; त्यांच्या स्मृतीत 2 डिसेंबरला आसाम दिवस पाळला जातो."), ("History", "इतिहास", "इतिहास")),
        person("sankardeva", ("Srimanta Sankardeva", "श्रीमंत शंकरदेव", "श्रीमंत शंकरदेव"), ("Saint, poet, playwright and reformer who founded the Ekasarana movement and the satras.", "संत, कवि, नाटककार और सुधारक, जिन्होंने एकशरण आंदोलन और सत्रों की स्थापना की।", "संत, कवी, नाटककार व सुधारक, ज्यांनी एकशरण चळवळ व सत्रांची स्थापना केली."), ("Religion and arts", "धर्म और कला", "धर्म व कला")),
        person("lachit", ("Lachit Borphukan", "लाचित बरफुकन", "लाचित बरफुकन"), ("Ahom general who defeated the Mughal fleet at Saraighat in 1671.", "अहोम सेनापति, जिन्होंने 1671 में सराईघाट में मुग़ल बेड़े को हराया।", "अहोम सेनापती, ज्यांनी 1671 मध्ये सराईघाट येथे मुघल आरमाराचा पराभव केला."), ("History", "इतिहास", "इतिहास")),
        person("maniram", ("Maniram Dewan", "मणिराम दीवान", "मणिराम दिवाण"), ("Early Indian tea planter, hanged for his role in the 1857 uprising.", "आरंभिक भारतीय चाय बाग़ान मालिक, 1857 के विद्रोह में भूमिका के लिए फाँसी दी गई।", "सुरुवातीचे भारतीय चहामळेवाले, 1857 च्या उठावातील भूमिकेसाठी फाशी देण्यात आली."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("kanaklata", ("Kanaklata Barua", "कनकलता बरुआ", "कनकलता बरुआ"), ("Teenage freedom fighter killed while carrying the national flag in 1942.", "किशोर स्वतंत्रता सेनानी, जो 1942 में राष्ट्रध्वज लेकर चलते हुए शहीद हुईं।", "किशोरवयीन स्वातंत्र्यसैनिक, 1942 मध्ये राष्ट्रध्वज घेऊन जाताना हुतात्मा झाल्या."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("bordoloi", ("Gopinath Bordoloi", "गोपीनाथ बरदलै", "गोपीनाथ बरदलै"), ("First Chief Minister of Assam; Bharat Ratna.", "असम के पहले मुख्यमंत्री; भारत रत्न।", "आसामचे पहिले मुख्यमंत्री; भारतरत्न."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("jyotiprasad", ("Jyoti Prasad Agarwala", "ज्योति प्रसाद अग्रवाल", "ज्योती प्रसाद आगरवाला"), ("Poet, playwright and maker of the first Assamese film, Joymoti (1935).", "कवि, नाटककार और पहली असमिया फ़िल्म 'जयमती' (1935) के निर्माता।", "कवी, नाटककार व पहिल्या आसामी चित्रपट 'जयमती' (1935) चे निर्माते."), ("Arts", "कला", "कला")),
        person("bhupen", ("Bhupen Hazarika", "भूपेन हज़ारिका", "भूपेन हजारिका"), ("Singer, composer and film-maker; Dadasaheb Phalke Award and Bharat Ratna.", "गायक, संगीतकार और फ़िल्मकार; दादासाहेब फाल्के पुरस्कार और भारत रत्न।", "गायक, संगीतकार व चित्रपटकर्ते; दादासाहेब फाळके पुरस्कार व भारतरत्न."), ("Music", "संगीत", "संगीत")),
        person("mamoni", ("Mamoni Raisom Goswami", "मामोनी रायसम गोस्वामी", "मामोनी रायसम गोस्वामी"), ("Assamese novelist; Jnanpith Award.", "असमिया उपन्यासकार; ज्ञानपीठ पुरस्कार।", "आसामी कादंबरीकार; ज्ञानपीठ पुरस्कार."), ("Literature", "साहित्य", "साहित्य")),
        person("lovlina", ("Lovlina Borgohain", "लवलीना बोरगोहेन", "लवलिना बोरगोहेन"), ("Boxer from Golaghat; Olympic bronze medallist.", "गोलाघाट की मुक्केबाज़; ओलंपिक कांस्य पदक विजेता।", "गोलाघाटची मुष्टियोद्धा; ऑलिम्पिक कांस्यपदक विजेती."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Assamese communities live across India — in Delhi, Bengaluru, Mumbai and Kolkata — and abroad, especially in the United States and the United Kingdom, where they celebrate Bihu each spring. Many young people from Assam now work in other States' service industries. Assam itself has long received migrants: the tea-garden communities descend from workers brought from central and eastern India in the 19th century.",
        "असमिया समुदाय पूरे भारत में — दिल्ली, बेंगलुरु, मुंबई और कोलकाता में — और विदेश में, विशेषकर संयुक्त राज्य अमेरिका और ब्रिटेन में रहते हैं, जहाँ वे हर वसंत में बिहू मनाते हैं। असम के बहुत से युवा अब दूसरे राज्यों के सेवा उद्योगों में काम करते हैं। असम स्वयं लंबे समय से प्रवासियों का गंतव्य रहा है: चाय बाग़ान समुदाय 19वीं सदी में मध्य और पूर्वी भारत से लाए गए श्रमिकों के वंशज हैं।",
        "आसामी समुदाय संपूर्ण भारतात — दिल्ली, बंगळुरू, मुंबई व कोलकात्यात — आणि परदेशात, विशेषतः अमेरिका व ब्रिटनमध्ये राहतात, जिथे ते दर वसंतात बिहू साजरा करतात. आसाममधील अनेक तरुण आता इतर राज्यांतील सेवा उद्योगांत काम करतात. आसाम स्वतः दीर्घकाळ स्थलांतरितांचे गंतव्य राहिले आहे: चहामळा समुदाय एकोणिसाव्या शतकात मध्य व पूर्व भारतातून आणलेल्या कामगारांचे वंशज आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Number of emigrants and internal migrants", "प्रवासियों और आंतरिक प्रवासियों की संख्या", "परदेशी व देशांतर्गत स्थलांतरितांची संख्या"), "census", "Census 2011 D-series migration tables; MEA."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Assam portal", "असम सरकार पोर्टल", "आसाम शासन संकेतस्थळ", url="https://assam.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("tourism", "Assam Tourism", "असम पर्यटन", "आसाम पर्यटन", url="https://tourism.assam.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Guwahati", "गुवाहाटी", "गुवाहाटी"), "0361"], [L("Dibrugarh", "डिब्रूगढ़", "डिब्रुगड"), "0373"], [L("Jorhat", "जोरहाट", "जोरहाट"), "0376"],
           [L("Silchar", "सिलचर", "सिलचर"), "03842"], [L("Tezpur", "तेजपुर", "तेजपूर"), "03712"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
    gaps("g", [
        (L("State e-services portal — verified link", "राज्य ई-सेवा पोर्टल — सत्यापित लिंक", "राज्य ई-सेवा संकेतस्थळ — पडताळलेला दुवा"), "india-gov", "Sewa Setu portal of the State."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("unesco", ("Assam has three UNESCO World Heritage Sites: Kaziranga, Manas and the Moidams of Charaideo.", "असम में तीन यूनेस्को विश्व धरोहर स्थल हैं: काज़ीरंगा, मानस और चराइदेउ के मोइदाम।", "आसाममध्ये तीन युनेस्को जागतिक वारसा स्थळे आहेत: काझीरंगा, मानस व चराइदेवचे मोइदाम."), UNESCO, "unesco-whc"),
        triv("bogibeel", ("Bogibeel, at 4.94 km, is India's longest rail-cum-road bridge.", "4.94 किमी लंबा बोगीबील भारत का सबसे लंबा रेल-सह-सड़क पुल है।", "4.94 किमी लांबीचा बोगीबील हा भारतातील सर्वांत लांब रेल्वे-सह-रस्ता पूल आहे."), "https://newindiasamachar.pib.gov.in/WriteReadData/flipbook/2026/Mar/1st/English/files/basic-html/page22.html", "new-india-samachar"),
        triv("digboi", ("Oil was struck at Digboi in 1889, and its refinery is among the oldest still operating.", "1889 में डिगबोई में तेल मिला, और इसकी रिफ़ाइनरी अब भी चल रही सबसे पुरानी रिफ़ाइनरियों में है।", "1889 मध्ये डिगबोई येथे तेल सापडले, आणि तिथली रिफायनरी अजूनही चालू असलेल्या सर्वांत जुन्या रिफायनरींपैकी आहे.")),
        triv("gi42", ("Assam has 42 entries in the GI Registry's list, including a large group of Bodo products registered in 2022.", "जीआई रजिस्ट्री की सूची में असम की 42 प्रविष्टियाँ हैं, जिनमें 2022 में पंजीकृत बोडो उत्पादों का बड़ा समूह शामिल है।", "जीआय रजिस्ट्रीच्या यादीत आसामच्या 42 नोंदी आहेत, ज्यांत 2022 मध्ये नोंदलेल्या बोडो उत्पादनांचा मोठा गट आहे."), GI_PDF, "gi-registry"),
        triv("saraighat", ("Lachit Borphukan, victor of Saraighat in 1671, is remembered on Lachit Divas, his birth anniversary on 24 November.", "1671 में सराईघाट के विजेता लाचित बरफुकन को 24 नवंबर को उनकी जयंती, लाचित दिवस, पर याद किया जाता है।", "1671 मधील सराईघाटचे विजेते लाचित बरफुकन यांचे स्मरण 24 नोव्हेंबरला, त्यांच्या जयंतीदिनी, लाचित दिवस म्हणून केले जाते.")),
        triv("ls", ("The State elects 14 members to the Lok Sabha.", "राज्य से लोकसभा के 14 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 14 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("as mod3 ok")
