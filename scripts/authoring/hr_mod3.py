"""Haryana modules P–Z."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-HR"
hr = read("regions/IN-HR.json")["metrics"]; ind = read("india.json")["metrics"]
C = research("census_b5plus.json"); F = C["forest"]["HR"]

RAMSAR_HR = [
    ("Sultanpur National Park", "सुल्तानपुर राष्ट्रीय उद्यान", "सुलतानपूर राष्ट्रीय उद्यान", "2021", "143"),
    ("Bhindawas Wildlife Sanctuary", "भिंडावास वन्यजीव अभयारण्य", "भिंडावास वन्यजीव अभयारण्य", "2021", "412"),
]

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "Only about 3.7% of Haryana is forest (ISFR 2023), one of the lowest shares of any State, found mainly in the Shivalik and Morni hills of Panchkula and Yamunanagar — where Kalesar National Park protects sal forest — and in the scrub and dry deciduous woods of the Aravallis in Gurugram, Faridabad, Nuh and Mahendragarh, which shelter leopards, striped hyenas and nilgai close to the capital region. The blackbuck, the State animal, survives in community-protected areas of the south-west.\n\nHaryana has two Ramsar wetlands, both designated in May 2021: Sultanpur National Park in Gurugram district and Bhindawas Wildlife Sanctuary in Jhajjar, winter homes for migratory waterbirds such as bar-headed geese, ruddy shelducks and flamingos.",
        "हरियाणा का केवल लगभग 3.7% भाग वन है (आईएसएफ़आर 2023), जो किसी भी राज्य में सबसे कम हिस्सों में है; ये वन मुख्यतः पंचकूला और यमुनानगर की शिवालिक व मोरनी पहाड़ियों में हैं — जहाँ कलेसर राष्ट्रीय उद्यान साल के वन को संरक्षित करता है — और गुरुग्राम, फ़रीदाबाद, नूँह और महेंद्रगढ़ में अरावली के झाड़ीदार और शुष्क पर्णपाती वनों में, जो राजधानी क्षेत्र के पास तेंदुओं, धारीदार लकड़बग्घों और नीलगायों को आश्रय देते हैं। राज्य पशु काला हिरण दक्षिण-पश्चिम के समुदाय-संरक्षित क्षेत्रों में बचा है।\n\nहरियाणा में दो रामसर आर्द्रभूमियाँ हैं, दोनों मई 2021 में घोषित: गुरुग्राम ज़िले का सुल्तानपुर राष्ट्रीय उद्यान और झज्जर का भिंडावास वन्यजीव अभयारण्य, जो धारीदार सिर वाले हंस, सुर्ख़ाब और राजहंस जैसे प्रवासी जलपक्षियों के शीतकालीन घर हैं।",
        "हरियाणाचा केवळ सुमारे 3.7% भाग वनाच्छादित आहे (आयएसएफआर 2023), जो कोणत्याही राज्यातील सर्वांत कमी वाट्यांपैकी आहे; ही वने मुख्यतः पंचकुला व यमुनानगरच्या शिवालिक व मोरनी टेकड्यांत आहेत — जिथे कलेसर राष्ट्रीय उद्यान सालवृक्षांचे वन जपते — आणि गुरुग्राम, फरिदाबाद, नूह व महेंद्रगडमधील अरवलीच्या झुडपी व शुष्क पानगळी वनांत, जी राजधानी प्रदेशाजवळ बिबटे, पट्टेरी तरस व नीलगायींना आश्रय देतात. राज्यप्राणी काळवीट नैर्ऋत्येतील समुदायाने जपलेल्या भागांत टिकून आहे.\n\nहरियाणात दोन रामसर पाणथळे आहेत, दोन्ही मे 2021 मध्ये घोषित: गुरुग्राम जिल्ह्यातील सुलतानपूर राष्ट्रीय उद्यान व झज्जरचे भिंडावास वन्यजीव अभयारण्य, जी पट्टेरी डोक्याचे हंस, चक्रवाक व रोहित (फ्लेमिंगो) यांसारख्या स्थलांतरित पाणपक्ष्यांची हिवाळी घरे आहेत."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), hr["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(2, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list of Ramsar sites as on 21 April 2026."), "number"),
    ]),
    table("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
          [col(L("Site", "स्थल", "स्थळ")), col(L("Designated", "घोषित", "घोषणा"), "right"), col(L("Area (ha)", "क्षेत्रफल (हेक्टेयर)", "क्षेत्रफळ (हेक्टर)"), "right")],
          [[L(e, h, m), d, a] for e, h, m, d, a in RAMSAR_HR], "indian-wetlands", RAMSAR,
          note=L("MoEFCC list as on 21 April 2026 (year of designation).", "21 अप्रैल 2026 की पर्यावरण मंत्रालय सूची (घोषणा वर्ष)।", "21 एप्रिल 2026 ची पर्यावरण मंत्रालयाची यादी (घोषणा वर्ष).")),
    lst("protected", [
        it3("kalesar", "Kalesar National Park", "कलेसर राष्ट्रीय उद्यान", "कलेसर राष्ट्रीय उद्यान", m=("Shivalik sal forest, Yamunanagar", "शिवालिक साल वन, यमुनानगर", "शिवालिक साल वन, यमुनानगर")),
        it3("sultanpur", "Sultanpur National Park", "सुल्तानपुर राष्ट्रीय उद्यान", "सुलतानपूर राष्ट्रीय उद्यान", m=("Wetland birds, Gurugram", "आर्द्रभूमि पक्षी, गुरुग्राम", "पाणथळ पक्षी, गुरुग्राम")),
        it3("bhindawas", "Bhindawas Wildlife Sanctuary", "भिंडावास वन्यजीव अभयारण्य", "भिंडावास वन्यजीव अभयारण्य", m=("Jhajjar", "झज्जर", "झज्जर")),
        it3("bir", "Bir Shikargah Wildlife Sanctuary", "बीड़ शिकारगाह वन्यजीव अभयारण्य", "बीड शिकारगाह वन्यजीव अभयारण्य", m=("Panchkula", "पंचकूला", "पंचकुला")),
        it3("khol", "Khol Hi-Raitan Wildlife Sanctuary", "खोल ही-रैतान वन्यजीव अभयारण्य", "खोल ही-रैतान वन्यजीव अभयारण्य", m=("Morni hills", "मोरनी पहाड़ियाँ", "मोरनी टेकड्या")),
    ], title=L("Protected areas (selected)", "संरक्षित क्षेत्र (चयनित)", "संरक्षित क्षेत्रे (निवडक)"), conf="Editorial"),
    lst("species", [
        it3("blackbuck", "Blackbuck (State animal)", "काला हिरण (राज्य पशु)", "काळवीट (राज्यप्राणी)"), it3("francolin", "Black francolin (State bird)", "काला तीतर (राज्य पक्षी)", "काळा तित्तर (राज्यपक्षी)"),
        it3("leopard", "Leopard (Aravallis)", "तेंदुआ (अरावली)", "बिबट्या (अरवली)"), it3("nilgai", "Nilgai", "नीलगाय", "नीलगाय"),
        it3("hyena", "Striped hyena", "धारीदार लकड़बग्घा", "पट्टेरी तरस"), it3("waterbirds", "Migratory waterbirds", "प्रवासी जलपक्षी", "स्थलांतरित पाणपक्षी"),
    ], layout="chips", title=L("Key species", "प्रमुख प्रजातियाँ", "प्रमुख प्रजाती"), conf="Editorial"),
    gaps("g", [
        (L("Aravalli forest area protected under the Punjab Land Preservation Act", "पंजाब भूमि संरक्षण अधिनियम के तहत संरक्षित अरावली वन क्षेत्र", "पंजाब भूमी संरक्षण कायद्यांतर्गत संरक्षित अरवली वनक्षेत्र"), "moefcc", "Haryana Forest Department."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Haryana has little surface water of its own and depends on canals and groundwater. The Western Yamuna Canal, one of the oldest canal systems in India, draws water at the Hathnikund barrage on the Yamuna, and the Bhakra main line brings Sutlej water from the Bhakra–Nangal system; lift canals carry water up to the dry south. Groundwater is heavily used for wheat and paddy, and many blocks in the north and centre are over-exploited, while parts of the south-west have saline groundwater. Sharing of river waters with Punjab — including the long-pending Sutlej–Yamuna Link canal — and Delhi's dependence on Yamuna flows through Haryana remain contested issues. The Yamuna, Ghaggar and Markanda flooded parts of the State in July 2023.",
        "हरियाणा के पास अपना सतही जल कम है और यह नहरों व भूजल पर निर्भर है। भारत की सबसे पुरानी नहर प्रणालियों में से एक, पश्चिमी यमुना नहर, यमुना पर हथिनीकुंड बैराज से पानी लेती है, और भाखड़ा मुख्य नहर भाखड़ा–नंगल प्रणाली से सतलुज का पानी लाती है; उठान नहरें पानी को सूखे दक्षिण तक पहुँचाती हैं। गेहूँ और धान के लिए भूजल का भारी उपयोग होता है, और उत्तर व मध्य के कई ब्लॉक अति-दोहित हैं, जबकि दक्षिण-पश्चिम के कुछ भागों में भूजल खारा है। पंजाब के साथ नदी जल बँटवारा — जिसमें लंबे समय से लंबित सतलुज–यमुना लिंक नहर भी है — और हरियाणा से आने वाले यमुना प्रवाह पर दिल्ली की निर्भरता विवादित मुद्दे बने हुए हैं। जुलाई 2023 में यमुना, घग्गर और मारकंडा ने राज्य के कई भागों में बाढ़ ला दी।",
        "हरियाणाकडे स्वतःचे पृष्ठजल कमी आहे आणि ते कालवे व भूजलावर अवलंबून आहे. भारतातील सर्वांत जुन्या कालवा प्रणालींपैकी एक, पश्चिम यमुना कालवा, यमुनेवरील हथिनीकुंड बंधाऱ्यातून पाणी घेतो, आणि भाक्रा मुख्य कालवा भाक्रा–नांगल प्रणालीतून सतलजचे पाणी आणतो; उपसा कालवे पाणी कोरड्या दक्षिणेपर्यंत पोहोचवतात. गहू व भातासाठी भूजलाचा प्रचंड वापर होतो, आणि उत्तर व मध्य भागातील अनेक गट अतिउपसा श्रेणीत आहेत, तर नैर्ऋत्येच्या काही भागांत भूजल खारे आहे. पंजाबसोबतचे नदी पाणीवाटप — ज्यात दीर्घकाळ प्रलंबित सतलज–यमुना जोड कालवाही आहे — आणि हरियाणातून येणाऱ्या यमुनेच्या प्रवाहावरील दिल्लीचे अवलंबित्व हे वादग्रस्त मुद्दे राहिले आहेत. जुलै 2023 मध्ये यमुना, घग्गर व मारकंडाने राज्याच्या अनेक भागांत पूर आणला."),
        conf="Editorial"),
    gaps("g", [
        (L("Groundwater stage of extraction and over-exploited blocks", "भूजल दोहन का स्तर और अति-दोहित ब्लॉक", "भूजल उपशाचा टप्पा व अतिउपसा गट"), "india-gov", "CGWB Dynamic Ground Water Resources assessment."),
        (L("Canal command area", "नहर कमान क्षेत्र", "कालवा लाभक्षेत्र"), "india-gov", "Haryana Irrigation and Water Resources Department."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Haryana's main hazards are heatwaves and dust storms in summer, floods along the Yamuna, Ghaggar and Markanda in heavy monsoons, and dense fog in winter, which causes road and rail accidents on the busy highways. The districts around Delhi are in a moderately high earthquake zone. In October–November, smoke from crop-residue burning and urban pollution often push air quality in Gurugram, Faridabad and the rest of the National Capital Region into the 'very poor' or 'severe' range, when restrictions under the Graded Response Action Plan apply.",
        "हरियाणा के मुख्य ख़तरे गर्मियों में लू और आँधियाँ, भारी मानसून में यमुना, घग्गर और मारकंडा की बाढ़, और सर्दियों में घना कोहरा हैं, जो व्यस्त राजमार्गों पर सड़क और रेल दुर्घटनाओं का कारण बनता है। दिल्ली के आसपास के ज़िले अपेक्षाकृत ऊँचे भूकंपीय क्षेत्र में हैं। अक्टूबर–नवंबर में फ़सल अवशेष जलाने का धुआँ और शहरी प्रदूषण अक्सर गुरुग्राम, फ़रीदाबाद और बाक़ी राष्ट्रीय राजधानी क्षेत्र की वायु गुणवत्ता को 'बहुत ख़राब' या 'गंभीर' श्रेणी में पहुँचा देते हैं, जब ग्रेडेड रिस्पॉन्स एक्शन प्लान के तहत प्रतिबंध लागू होते हैं।",
        "हरियाणावरील मुख्य धोके म्हणजे उन्हाळ्यातील उष्णतेच्या लाटा व धुळीची वादळे, मुसळधार पावसात यमुना, घग्गर व मारकंडाचे पूर, आणि हिवाळ्यातील दाट धुके, ज्यामुळे वर्दळीच्या महामार्गांवर रस्ते व रेल्वे अपघात होतात. दिल्लीभोवतीचे जिल्हे तुलनेने अधिक भूकंपप्रवण क्षेत्रात आहेत. ऑक्टोबर–नोव्हेंबरमध्ये पिकांचे अवशेष जाळण्याचा धूर व शहरी प्रदूषण अनेकदा गुरुग्राम, फरिदाबाद व उर्वरित राष्ट्रीय राजधानी क्षेत्रातील हवेची गुणवत्ता 'अतिशय वाईट' किंवा 'गंभीर' श्रेणीत नेतात, तेव्हा श्रेणीबद्ध प्रतिसाद कृती आराखड्याअंतर्गत निर्बंध लागू होतात."),
        conf="Editorial"),
    emergency_table(("Haryana", "हरियाणा", "हरियाणा")),
    lst("links", [
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
        it3("ndma", "National Disaster Management Authority", "राष्ट्रीय आपदा प्रबंधन प्राधिकरण", "राष्ट्रीय आपत्ती व्यवस्थापन प्राधिकरण", url="https://ndma.gov.in", src="ndma"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("State Disaster Management Authority — verified link", "राज्य आपदा प्रबंधन प्राधिकरण — सत्यापित लिंक", "राज्य आपत्ती व्यवस्थापन प्राधिकरण — पडताळलेला दुवा"), "ndma", "Add the official address."),
        (L("Air quality — days in each AQI category", "वायु गुणवत्ता — प्रत्येक एक्यूआई श्रेणी के दिन", "हवेची गुणवत्ता — प्रत्येक एक्यूआय श्रेणीतील दिवस"), "india-gov", "CPCB / CAQM annual data for Haryana cities."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Haryana appears in two entries of the GI Registry's list as on 31 December 2025, both shared with neighbouring States. Phulkari embroidery was filed in 2005 for Punjab, Haryana and Rajasthan, and Basmati rice, filed in 2008, is registered for the Indo-Gangetic plain of Punjab, Haryana, Himachal Pradesh, Delhi, Uttarakhand, western Uttar Pradesh and Jammu and Kashmir. No GI is registered for Haryana alone on this list.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची की दो प्रविष्टियों में हरियाणा है, और दोनों पड़ोसी राज्यों के साथ साझा हैं। फुलकारी कढ़ाई 2005 में पंजाब, हरियाणा और राजस्थान के लिए दायर हुई, और 2008 में दायर बासमती चावल पंजाब, हरियाणा, हिमाचल प्रदेश, दिल्ली, उत्तराखंड, पश्चिमी उत्तर प्रदेश और जम्मू-कश्मीर के सिंधु-गंगा मैदान के लिए पंजीकृत है। इस सूची में केवल हरियाणा के लिए कोई जीआई पंजीकृत नहीं है।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीतील दोन नोंदींत हरियाणा आहे, आणि दोन्ही शेजारी राज्यांसोबत सामायिक आहेत. फुलकारी भरतकाम 2005 मध्ये पंजाब, हरियाणा व राजस्थानसाठी दाखल झाले, आणि 2008 मध्ये दाखल बासमती तांदूळ पंजाब, हरियाणा, हिमाचल प्रदेश, दिल्ली, उत्तराखंड, पश्चिम उत्तर प्रदेश व जम्मू-काश्मीरच्या सिंधू-गंगा मैदानासाठी नोंदणीकृत आहे. या यादीत केवळ हरियाणासाठी एकही जीआय नोंदणीकृत नाही."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("Pending GI applications from Haryana", "हरियाणा के लंबित जीआई आवेदन", "हरियाणाचे प्रलंबित जीआय अर्ज"), "gi-registry", "GI Registry application status search."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Kurukshetra is Haryana's best-known destination, with the Brahma Sarovar tank, Jyotisar — where the Gita is said to have been spoken — the Sri Krishna Museum and the panorama of the Mahabharata war, and it fills with pilgrims during the Gita Mahotsav and solar eclipses. Pinjore's terraced Yadavindra Gardens and the Morni hills, Haryana's only hill station, lie near Panchkula. Panipat's museum tells the story of its three battles, and Rakhigarhi and Agroha attract those interested in archaeology. Close to Delhi, the Surajkund crafts fair, the Sultanpur bird sanctuary, Damdama lake and the highway dhabas of Murthal are popular weekend trips, and the State's tourist complexes named after birds — such as Blue Jay at Samalkha and Skylark at Panipat — line the highways.",
        "कुरुक्षेत्र हरियाणा का सबसे प्रसिद्ध गंतव्य है, जहाँ ब्रह्म सरोवर, ज्योतिसर — जहाँ गीता का उपदेश दिया गया माना जाता है — श्रीकृष्ण संग्रहालय और महाभारत युद्ध का पैनोरमा है, और गीता महोत्सव व सूर्य ग्रहण के समय यह तीर्थयात्रियों से भर जाता है। पिंजौर के सीढ़ीदार यादविंद्र उद्यान और हरियाणा का एकमात्र पर्वतीय स्थल मोरनी पहाड़ियाँ पंचकूला के पास हैं। पानीपत का संग्रहालय उसके तीन युद्धों की कहानी बताता है, और राखीगढ़ी व अग्रोहा पुरातत्व में रुचि रखने वालों को आकर्षित करते हैं। दिल्ली के पास सूरजकुंड शिल्प मेला, सुल्तानपुर पक्षी अभयारण्य, दमदमा झील और मुरथल के राजमार्ग ढाबे लोकप्रिय सप्ताहांत यात्राएँ हैं, और राजमार्गों पर पक्षियों के नाम वाले राज्य के पर्यटक परिसर — जैसे समालखा का ब्लू जे और पानीपत का स्काईलार्क — मिलते हैं।",
        "कुरुक्षेत्र हे हरियाणाचे सर्वांत प्रसिद्ध पर्यटनस्थळ आहे, जिथे ब्रह्म सरोवर, ज्योतिसर — जिथे गीता सांगितली गेली असे मानले जाते — श्रीकृष्ण संग्रहालय व महाभारत युद्धाचे पॅनोरमा आहे, आणि गीता महोत्सव व सूर्यग्रहणाच्या वेळी ते यात्रेकरूंनी गजबजते. पिंजोरचे पायऱ्यांचे यादविंद्र उद्यान व हरियाणाचे एकमेव थंड हवेचे ठिकाण मोरनी टेकड्या पंचकुलाजवळ आहेत. पानिपतचे संग्रहालय तिथल्या तीन लढायांची कहाणी सांगते, आणि राखीगढी व अग्रोहा पुरातत्त्वात रस असणाऱ्यांना आकर्षित करतात. दिल्लीजवळ सूरजकुंड हस्तकला मेळा, सुलतानपूर पक्षी अभयारण्य, दमदमा तलाव व मुरथलचे महामार्ग ढाबे हे लोकप्रिय शनिवार-रविवार सहलींचे ठिकाण आहेत, आणि महामार्गांवर पक्ष्यांची नावे असलेली राज्याची पर्यटक संकुले — जसे समालखाचे ब्लू जे व पानिपतचे स्कायलार्क — आढळतात."),
        conf="Editorial"),
    lst("places", [
        it3("kurukshetra", "Kurukshetra", "कुरुक्षेत्र", "कुरुक्षेत्र", m=("Brahma Sarovar; Jyotisar", "ब्रह्म सरोवर; ज्योतिसर", "ब्रह्म सरोवर; ज्योतिसर")),
        it3("pinjore", "Pinjore and Morni hills", "पिंजौर और मोरनी पहाड़ियाँ", "पिंजोर व मोरनी टेकड्या", m=("Gardens and hills near Panchkula", "पंचकूला के पास उद्यान और पहाड़ियाँ", "पंचकुलाजवळील उद्याने व टेकड्या")),
        it3("surajkund", "Surajkund", "सूरजकुंड", "सूरजकुंड", m=("Crafts fair in February", "फ़रवरी में शिल्प मेला", "फेब्रुवारीत हस्तकला मेळा")),
        it3("sultanpur", "Sultanpur National Park", "सुल्तानपुर राष्ट्रीय उद्यान", "सुलतानपूर राष्ट्रीय उद्यान", m=("Winter birdwatching", "सर्दियों में पक्षी दर्शन", "हिवाळ्यात पक्षीनिरीक्षण")),
        it3("panipat", "Panipat", "पानीपत", "पानिपत", m=("Battlefield museum; textiles", "युद्धभूमि संग्रहालय; वस्त्र", "युद्धभूमी संग्रहालय; वस्त्रोद्योग")),
        it3("rakhigarhi", "Rakhigarhi", "राखीगढ़ी", "राखीगढी", m=("Harappan site and museum", "हड़प्पा स्थल और संग्रहालय", "हडप्पा स्थळ व संग्रहालय")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Kurukshetra's sarovars and museums, with a stop at Panipat on the way from Delhi.", "दिल्ली से रास्ते में पानीपत रुकते हुए कुरुक्षेत्र के सरोवर और संग्रहालय।", "दिल्लीहून वाटेत पानिपतला थांबत कुरुक्षेत्राचे सरोवर व संग्रहालये.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Pinjore gardens, Morni hills and the Chandigarh tricity.", "पिंजौर उद्यान, मोरनी पहाड़ियाँ और चंडीगढ़ ट्राइसिटी।", "पिंजोर उद्यान, मोरनी टेकड्या व चंदीगड त्रिनगरी.")),
        it3("d1", "1 day from Delhi", "दिल्ली से 1 दिन", "दिल्लीहून 1 दिवस", d=("Sultanpur at dawn, then Surajkund or Damdama lake.", "भोर में सुल्तानपुर, फिर सूरजकुंड या दमदमा झील।", "पहाटे सुलतानपूर, नंतर सूरजकुंड किंवा दमदमा तलाव.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [
        it3("ht", "Haryana Tourism (official)", "हरियाणा पर्यटन (आधिकारिक)", "हरियाणा पर्यटन (अधिकृत)", url="https://haryanatourism.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits, by year", "वर्षवार घरेलू और विदेशी पर्यटक यात्राएँ", "वर्षनिहाय देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Data Compendium state table."),
    ]),
])

# ---------------- U. Cities ----------------
def city(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
DISTRICTS = [
    ("Ambala", "अंबाला", "अंबाला"), ("Bhiwani", "भिवानी", "भिवानी"), ("Charkhi Dadri", "चरखी दादरी", "चरखी दादरी"), ("Faridabad", "फ़रीदाबाद", "फरिदाबाद"), ("Fatehabad", "फ़तेहाबाद", "फतेहाबाद"),
    ("Gurugram", "गुरुग्राम", "गुरुग्राम"), ("Hansi", "हांसी", "हांसी"), ("Hisar", "हिसार", "हिसार"), ("Jhajjar", "झज्जर", "झज्जर"), ("Jind", "जींद", "जिंद"),
    ("Kaithal", "कैथल", "कैथल"), ("Karnal", "करनाल", "कर्नाल"), ("Kurukshetra", "कुरुक्षेत्र", "कुरुक्षेत्र"), ("Mahendragarh", "महेंद्रगढ़", "महेंद्रगड"), ("Nuh", "नूँह", "नूह"),
    ("Palwal", "पलवल", "पलवल"), ("Panchkula", "पंचकूला", "पंचकुला"), ("Panipat", "पानीपत", "पानिपत"), ("Rewari", "रेवाड़ी", "रेवाडी"), ("Rohtak", "रोहतक", "रोहतक"),
    ("Sirsa", "सिरसा", "सिरसा"), ("Sonipat", "सोनीपत", "सोनीपत"), ("Yamunanagar", "यमुनानगर", "यमुनानगर"),
]
assert len(DISTRICTS) == 23, len(DISTRICTS)
module(R, "cities", [
    lst("cities", [
        city("faridabad", ("Faridabad", "फ़रीदाबाद", "फरिदाबाद"), ("Largest city; engineering and manufacturing hub next to Delhi.", "सबसे बड़ा शहर; दिल्ली से सटा इंजीनियरिंग और विनिर्माण केंद्र।", "सर्वांत मोठे शहर; दिल्लीलगतचे अभियांत्रिकी व उत्पादन केंद्र."), ("Industry", "उद्योग", "उद्योग")),
        city("gurugram", ("Gurugram", "गुरुग्राम", "गुरुग्राम"), ("Corporate, IT and automobile city.", "कॉर्पोरेट, आईटी और ऑटोमोबाइल शहर।", "कॉर्पोरेट, आयटी व मोटार उद्योगाचे शहर."), ("Services", "सेवाएँ", "सेवा")),
        city("panipat", ("Panipat", "पानीपत", "पानिपत"), ("Textiles, handloom and refinery; three historic battles.", "वस्त्र, हथकरघा और रिफ़ाइनरी; तीन ऐतिहासिक युद्ध।", "वस्त्रोद्योग, हातमाग व रिफायनरी; तीन ऐतिहासिक लढाया."), ("Industry", "उद्योग", "उद्योग")),
        city("ambala", ("Ambala", "अंबाला", "अंबाला"), ("Cantonment and railway junction; scientific instruments.", "छावनी और रेलवे जंक्शन; वैज्ञानिक उपकरण।", "छावणी व रेल्वे जंक्शन; वैज्ञानिक उपकरणे."), ("Transport", "परिवहन", "वाहतूक")),
        city("rohtak", ("Rohtak", "रोहतक", "रोहतक"), ("Education centre: MDU, PGIMS and IIM.", "शिक्षा केंद्र: एमडीयू, पीजीआईएमएस और आईआईएम।", "शिक्षण केंद्र: एमडीयू, पीजीआयएमएस व आयआयएम."), ("Education", "शिक्षा", "शिक्षण")),
        city("hisar", ("Hisar", "हिसार", "हिसार"), ("Agricultural university, livestock research and steel.", "कृषि विश्वविद्यालय, पशुधन अनुसंधान और इस्पात।", "कृषी विद्यापीठ, पशुधन संशोधन व पोलाद."), ("Agriculture", "कृषि", "शेती")),
        city("karnal", ("Karnal", "करनाल", "कर्नाल"), ("Rice and dairy research institutes.", "धान और डेयरी अनुसंधान संस्थान।", "भात व दुग्ध संशोधन संस्था."), ("Agriculture", "कृषि", "शेती")),
        city("panchkula", ("Panchkula", "पंचकूला", "पंचकुला"), ("Planned city in the Chandigarh tricity.", "चंडीगढ़ ट्राइसिटी का नियोजित शहर।", "चंदीगड त्रिनगरीतील नियोजित शहर."), ("Administration", "प्रशासन", "प्रशासन")),
    ], title=L("Major cities", "प्रमुख शहर", "प्रमुख शहरे"), conf="Editorial"),
    lst("districts", [it3(re.sub(r"[^a-z0-9]", "", e.lower()), e, h, m) for e, h, m in DISTRICTS],
        layout="chips", title=L("The 23 districts (alphabetical)", "23 ज़िले (वर्णानुक्रम)", "23 जिल्हे (वर्णक्रमानुसार)"), conf="Editorial"),
    gaps("g", [
        (L("Official district list (State notification)", "आधिकारिक ज़िला सूची (राज्य अधिसूचना)", "अधिकृत जिल्हा यादी (राज्य अधिसूचना)"), "india-gov", "Link the State's list of districts; Hansi was carved out of Hisar in December 2025."),
        (L("City populations (Census 2011)", "शहरों की जनसंख्या (जनगणना 2011)", "शहरांची लोकसंख्या (जनगणना 2011)"), "census", "Census 2011 urban agglomeration tables."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Haryana punches far above its size in sport. Its village akharas and the Bhiwani Boxing Club have made it the home of Indian wrestling and boxing: Vijender Singh won India's first Olympic boxing medal at Beijing in 2008, and wrestlers including Yogeshwar Dutt, Sakshi Malik — India's first woman Olympic wrestling medallist, at Rio 2016 — Ravi Kumar Dahiya, Bajrang Punia and Aman Sehrawat have won Olympic medals. Neeraj Chopra from Khandra village near Panipat won the javelin gold at Tokyo 2020 — India's first Olympic gold in athletics — and silver at Paris 2024, where Manu Bhaker of Jhajjar won two shooting bronzes. Kabaddi and hockey are also popular, and the State's policy of large cash awards for medallists has encouraged young athletes.",
        "खेलों में हरियाणा अपने आकार से कहीं आगे है। इसके गाँवों के अखाड़ों और भिवानी बॉक्सिंग क्लब ने इसे भारतीय कुश्ती और मुक्केबाज़ी का घर बना दिया है: विजेंद्र सिंह ने 2008 में बीजिंग में भारत का पहला ओलंपिक मुक्केबाज़ी पदक जीता, और योगेश्वर दत्त, साक्षी मलिक — रियो 2016 में ओलंपिक कुश्ती पदक जीतने वाली पहली भारतीय महिला — रवि कुमार दहिया, बजरंग पूनिया और अमन सहरावत सहित पहलवानों ने ओलंपिक पदक जीते हैं। पानीपत के पास खंडरा गाँव के नीरज चोपड़ा ने टोक्यो 2020 में भाला फेंक में स्वर्ण — एथलेटिक्स में भारत का पहला ओलंपिक स्वर्ण — और पेरिस 2024 में रजत जीता, जहाँ झज्जर की मनु भाकर ने निशानेबाज़ी में दो कांस्य जीते। कबड्डी और हॉकी भी लोकप्रिय हैं, और पदक विजेताओं को बड़े नक़द पुरस्कार देने की राज्य की नीति ने युवा खिलाड़ियों को प्रोत्साहित किया है।",
        "खेळांत हरियाणा आपल्या आकारापेक्षा कितीतरी पुढे आहे. त्याच्या गावांतील आखाडे व भिवानी बॉक्सिंग क्लबमुळे तो भारतीय कुस्ती व मुष्टियुद्धाचे घर बनला आहे: विजेंदरसिंहांनी 2008 मध्ये बीजिंगमध्ये भारताचे पहिले ऑलिम्पिक मुष्टियुद्ध पदक जिंकले, आणि योगेश्वर दत्त, साक्षी मलिक — रिओ 2016 मध्ये ऑलिम्पिक कुस्ती पदक जिंकणारी पहिली भारतीय महिला — रवी कुमार दहिया, बजरंग पुनिया व अमन सहरावत यांच्यासह पैलवानांनी ऑलिम्पिक पदके जिंकली आहेत. पानिपतजवळील खांडरा गावच्या नीरज चोप्राने टोकियो 2020 मध्ये भालाफेकीत सुवर्ण — ॲथलेटिक्समधील भारताचे पहिले ऑलिम्पिक सुवर्ण — आणि पॅरिस 2024 मध्ये रौप्य जिंकले, जिथे झज्जरच्या मनू भाकरने नेमबाजीत दोन कांस्यपदके जिंकली. कबड्डी व हॉकीही लोकप्रिय आहेत, आणि पदकविजेत्यांना मोठी रोख बक्षिसे देण्याच्या राज्याच्या धोरणाने तरुण खेळाडूंना प्रोत्साहन मिळाले आहे."),
        conf="Editorial"),
    lst("venues", [
        it3("tau", "Tau Devi Lal Stadium, Panchkula", "ताऊ देवीलाल स्टेडियम, पंचकूला", "ताऊ देवीलाल स्टेडियम, पंचकुला"),
        it3("bbc", "Bhiwani Boxing Club", "भिवानी बॉक्सिंग क्लब", "भिवानी बॉक्सिंग क्लब"),
        it3("rajiv", "Rajiv Gandhi Sports Complex, Rohtak", "राजीव गांधी खेल परिसर, रोहतक", "राजीव गांधी क्रीडा संकुल, रोहतक"),
        it3("motilal", "Motilal Nehru School of Sports, Rai", "मोतीलाल नेहरू खेल विद्यालय, राई", "मोतीलाल नेहरू क्रीडा विद्यालय, राई"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
    gaps("g", [(L("Olympic, Asian and Commonwealth Games medallists from Haryana (official list)", "हरियाणा के ओलंपिक, एशियाई और राष्ट्रमंडल खेल पदक विजेता (आधिकारिक सूची)", "हरियाणाचे ऑलिम्पिक, आशियाई व राष्ट्रकुल स्पर्धा पदकविजेते (अधिकृत यादी)"), "india-gov", "Haryana Sports Department.")]),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("harsha", ("Harshavardhana", "हर्षवर्धन", "हर्षवर्धन"), ("7th-century emperor who ruled northern India from Thanesar and later Kannauj.", "7वीं सदी के सम्राट, जिन्होंने थानेसर और बाद में कन्नौज से उत्तर भारत पर शासन किया।", "सातव्या शतकातील सम्राट, ज्यांनी ठाणेसर व नंतर कनौजहून उत्तर भारतावर राज्य केले."), ("History", "इतिहास", "इतिहास")),
        person("hemu", ("Hem Chandra Vikramaditya (Hemu)", "हेमचंद्र विक्रमादित्य (हेमू)", "हेमचंद्र विक्रमादित्य (हेमू)"), ("16th-century ruler from Rewari, defeated at the Second Battle of Panipat in 1556.", "रेवाड़ी के 16वीं सदी के शासक, जो 1556 में पानीपत के दूसरे युद्ध में पराजित हुए।", "रेवाडीचे सोळाव्या शतकातील राज्यकर्ते, ज्यांचा 1556 मध्ये पानिपतच्या दुसऱ्या लढाईत पराभव झाला."), ("History", "इतिहास", "इतिहास")),
        person("tularam", ("Rao Tula Ram", "राव तुलाराम", "राव तुलाराम"), ("Leader of the 1857 uprising in the Rewari region.", "रेवाड़ी क्षेत्र में 1857 के विद्रोह के नेता।", "रेवाडी परिसरातील 1857 च्या उठावाचे नेते."), ("Freedom struggle", "स्वतंत्रता संग्राम", "स्वातंत्र्यलढा")),
        person("chhoturam", ("Sir Chhotu Ram", "सर छोटूराम", "सर छोटूराम"), ("Peasant leader and minister in undivided Punjab who championed farmers' rights.", "अविभाजित पंजाब के किसान नेता और मंत्री, जिन्होंने किसानों के अधिकारों की लड़ाई लड़ी।", "अविभाजित पंजाबचे शेतकरी नेते व मंत्री, ज्यांनी शेतकऱ्यांच्या हक्कांसाठी लढा दिला."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
        person("lakhmichand", ("Pandit Lakhmi Chand", "पंडित लखमीचंद", "पंडित लखमीचंद"), ("Poet and performer of saang, called the 'Kalidas of Haryana'.", "सांग के कवि और कलाकार, जिन्हें 'हरियाणा का कालिदास' कहा जाता है।", "सांगचे कवी व कलाकार, ज्यांना 'हरियाणाचे कालिदास' म्हणतात."), ("Folk arts", "लोक कला", "लोककला")),
        person("jasraj", ("Pandit Jasraj", "पंडित जसराज", "पंडित जसराज"), ("Hindustani vocalist of the Mewati gharana.", "मेवाती घराने के हिंदुस्तानी गायक।", "मेवाती घराण्याचे हिंदुस्तानी गायक."), ("Music", "संगीत", "संगीत")),
        person("kalpana", ("Kalpana Chawla", "कल्पना चावला", "कल्पना चावला"), ("Astronaut from Karnal, the first woman of Indian origin in space; died in the Columbia disaster in 2003.", "करनाल की अंतरिक्ष यात्री, अंतरिक्ष में जाने वाली भारतीय मूल की पहली महिला; 2003 में कोलंबिया दुर्घटना में निधन।", "कर्नालच्या अंतराळवीर, अंतराळात जाणाऱ्या भारतीय वंशाच्या पहिल्या महिला; 2003 मध्ये कोलंबिया दुर्घटनेत निधन."), ("Science", "विज्ञान", "विज्ञान")),
        person("neeraj", ("Neeraj Chopra", "नीरज चोपड़ा", "नीरज चोप्रा"), ("Javelin thrower; Olympic gold at Tokyo 2020 and silver at Paris 2024.", "भाला फेंक खिलाड़ी; टोक्यो 2020 में ओलंपिक स्वर्ण और पेरिस 2024 में रजत।", "भालाफेकपटू; टोकियो 2020 मध्ये ऑलिम्पिक सुवर्ण व पॅरिस 2024 मध्ये रौप्य."), ("Sport", "खेल", "क्रीडा")),
        person("sakshi", ("Sakshi Malik", "साक्षी मलिक", "साक्षी मलिक"), ("Wrestler; bronze at Rio 2016.", "पहलवान; रियो 2016 में कांस्य।", "पैलवान; रिओ 2016 मध्ये कांस्य."), ("Sport", "खेल", "क्रीडा")),
        person("manu", ("Manu Bhaker", "मनु भाकर", "मनू भाकर"), ("Shooter; two bronze medals at Paris 2024.", "निशानेबाज़; पेरिस 2024 में दो कांस्य पदक।", "नेमबाज; पॅरिस 2024 मध्ये दोन कांस्यपदके."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Haryana's migration story is mostly within India — to Delhi, the armed forces and government service — and the State in turn draws large numbers of workers from Uttar Pradesh, Bihar and other States to the factories and offices of Gurugram, Faridabad and Panipat. Families from Haryana have also settled in Australia, Canada, the United States and the United Kingdom, often through study, and the Haryanvi community abroad celebrates Haryana Day and Teej.",
        "हरियाणा की प्रवास कहानी अधिकतर भारत के भीतर है — दिल्ली, सशस्त्र बलों और सरकारी सेवा की ओर — और बदले में राज्य उत्तर प्रदेश, बिहार और अन्य राज्यों से बड़ी संख्या में श्रमिकों को गुरुग्राम, फ़रीदाबाद और पानीपत के कारख़ानों और कार्यालयों में खींचता है। हरियाणा के परिवार ऑस्ट्रेलिया, कनाडा, अमेरिका और ब्रिटेन में भी बसे हैं, अक्सर पढ़ाई के माध्यम से, और विदेश में हरियाणवी समुदाय हरियाणा दिवस और तीज मनाता है।",
        "हरियाणाची स्थलांतर कथा बहुतांश भारतांतर्गत आहे — दिल्ली, सशस्त्र दले व सरकारी सेवेकडे — आणि त्याबदल्यात राज्य उत्तर प्रदेश, बिहार व इतर राज्यांतून मोठ्या संख्येने कामगारांना गुरुग्राम, फरिदाबाद व पानिपतच्या कारखाने व कार्यालयांकडे खेचते. हरियाणातील कुटुंबे ऑस्ट्रेलिया, कॅनडा, अमेरिका व ब्रिटनमध्येही स्थायिक झाली आहेत, अनेकदा शिक्षणाच्या माध्यमातून, आणि परदेशातील हरियाणवी समुदाय हरियाणा दिन व तीज साजरी करतो."),
        conf="Editorial"),
    gaps("g", [
        (L("Migration in and out of Haryana (Census 2011 D-series)", "हरियाणा में आने-जाने वाला प्रवास (जनगणना 2011 डी-शृंखला)", "हरियाणात येणारे-जाणारे स्थलांतर (जनगणना 2011 डी-मालिका)"), "census", "Census 2011 migration tables."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of Haryana portal", "हरियाणा सरकार पोर्टल", "हरियाणा शासन संकेतस्थळ", url="https://haryana.gov.in", src="india-gov"),
        it3("saral", "Saral Haryana (citizen services)", "सरल हरियाणा (नागरिक सेवाएँ)", "सरल हरियाणा (नागरी सेवा)", url="https://saralharyana.gov.in", src="india-gov"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD codes of major cities", "प्रमुख शहरों के एसटीडी कोड", "प्रमुख शहरांचे एसटीडी कोड"),
          [col(L("City", "शहर", "शहर")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("Gurugram", "गुरुग्राम", "गुरुग्राम"), "0124"], [L("Faridabad", "फ़रीदाबाद", "फरिदाबाद"), "0129"], [L("Panipat", "पानीपत", "पानिपत"), "0180"],
           [L("Ambala", "अंबाला", "अंबाला"), "0171"], [L("Karnal", "करनाल", "कर्नाल"), "0184"], [L("Hisar", "हिसार", "हिसार"), "01662"]],
          None, None, conf="Editorial", access=None,
          note=L("Editorial list; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय सूची; दूरसंचार विभाग की नंबरिंग योजना से जाँची जाएगी।", "संपादकीय यादी; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळली जाईल.")),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("csr", ("Haryana's child sex ratio in 2011 — 834 girls per 1,000 boys — was the lowest of any State or Union Territory.", "2011 में हरियाणा का शिशु लिंगानुपात — प्रति 1,000 लड़कों पर 834 लड़कियाँ — किसी भी राज्य या केंद्र शासित प्रदेश में सबसे कम था।", "2011 मध्ये हरियाणाचे बाल लिंग गुणोत्तर — दर 1,000 मुलांमागे 834 मुली — कोणत्याही राज्य वा केंद्रशासित प्रदेशात सर्वांत कमी होते."), PIB_CSR, "pib"),
        triv("delhi", ("Haryana surrounds Delhi on three sides; Uttar Pradesh is on the fourth.", "हरियाणा दिल्ली को तीन ओर से घेरता है; चौथी ओर उत्तर प्रदेश है।", "हरियाणा दिल्लीला तीन बाजूंनी वेढतो; चौथ्या बाजूला उत्तर प्रदेश आहे.")),
        triv("ramsar", ("Both of Haryana's Ramsar sites — Sultanpur and Bhindawas — were designated on the same day, 25 May 2021.", "हरियाणा के दोनों रामसर स्थल — सुल्तानपुर और भिंडावास — एक ही दिन, 25 मई 2021 को घोषित हुए।", "हरियाणाची दोन्ही रामसर स्थळे — सुलतानपूर व भिंडावास — एकाच दिवशी, 25 मे 2021 रोजी घोषित झाली."), RAMSAR, "indian-wetlands"),
        triv("capital", ("Haryana shares its capital, Chandigarh, with Punjab; the city is a Union Territory.", "हरियाणा अपनी राजधानी चंडीगढ़ पंजाब के साथ साझा करता है; यह शहर केंद्र शासित प्रदेश है।", "हरियाणा आपली राजधानी चंदीगड पंजाबसोबत सामायिक करतो; हे शहर केंद्रशासित प्रदेश आहे.")),
        triv("neeraj", ("Neeraj Chopra's javelin gold at Tokyo 2020 was India's first Olympic gold in athletics.", "टोक्यो 2020 में नीरज चोपड़ा का भाला फेंक स्वर्ण एथलेटिक्स में भारत का पहला ओलंपिक स्वर्ण था।", "टोकियो 2020 मधील नीरज चोप्राचे भालाफेकीतील सुवर्ण हे ॲथलेटिक्समधील भारताचे पहिले ऑलिम्पिक सुवर्ण होते.")),
        triv("ls", ("The State elects 10 members to the Lok Sabha.", "राज्य से लोकसभा के 10 सदस्य चुने जाते हैं।", "राज्यातून लोकसभेवर 10 सदस्य निवडले जातात.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("hr mod3 ok")
