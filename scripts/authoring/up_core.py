"""Uttar Pradesh — Phase 3 profile: identity, officeholders, projects, GIs.
Core Census/MoSPI metrics are written by tn_up_core.py (run it first)."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

GOV = "https://www.newsonair.gov.in/budget-session-of-up-legislative-assembly-begins-with-address-of-governor-anandiben-patel"
LOP = "https://www.newsonair.gov.in/uttar-pradesh-assembly-monsoon-session-begins-today"
CM = "https://www.newsonair.gov.in/tag/up-cm-yogi-adityanath"
CM_OATH = "https://onmanorama.com/news/india/2022/03/25/yogi-adityanath-uttar-pradesh-government.html"
NIA = "https://www.pmindia.gov.in/?p=16818806"
GANGA = "https://newsonair.gov.in/pm-modi-inaugurates-594-km-long-ganga-expressway-connecting-meerut-to-prayagraj/"

r = read("regions/IN-UP.json")
r["officialPortal"] = "https://up.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Swamp deer (barasingha)", "बारहसिंगा", "बारशिंगा", "Rucervus duvaucelii"),
    "bird": sym("Sarus crane", "सारस", "सारस क्रौंच", "Antigone antigone"),
    "flower": sym("Palash (flame of the forest)", "पलाश (टेसू)", "पळस", "Butea monosperma"),
    "tree": sym("Ashoka", "अशोक", "अशोक", "Saraca asoca"),
    "fish": sym("Chital (clown knifefish)", "चीतल मछली", "चितळ मासा", "Chitala chitala"),
}

r["government"] = {
    "headOfState": office("governor", L("Anandiben Patel", "आनंदीबेन पटेल", "आनंदीबेन पटेल"), None, "2019-07-29",
                          "newsonair", GOV, "https://up.gov.in",
                          note="Governor since 29 July 2019; she addressed the Legislature's budget session on 9 February 2026 (News On AIR). Still named as Chancellor of State universities in August 2026. Confirm on the Lok Bhavan, Uttar Pradesh website."),
    "headOfGovernment": office("chief-minister", L("Yogi Adityanath", "योगी आदित्यनाथ", "योगी आदित्यनाथ"), "BJP", "2022-03-25",
                               "newsonair", CM, "https://up.gov.in",
                               note="Second consecutive term; sworn in on 25 March 2022 (first term from 19 March 2017). Referred to as Chief Minister in News On AIR reports through 2026."),
    "others": [
        office("speaker", L("Satish Mahana", "सतीश महाना", "सतीश महाना"), "BJP", "2022-03-29", "newsonair", LOP, "https://uplegisassembly.gov.in",
               note="Speaker of the 18th Legislative Assembly; named in News On AIR's report of 29 July 2024."),
        office("leader-of-opposition", L("Mata Prasad Pandey", "माता प्रसाद पांडेय", "माता प्रसाद पांडे"), "SP", "2024-07-28", "newsonair", LOP, "https://uplegisassembly.gov.in",
               note="Samajwadi Party; introduced as Leader of Opposition at the start of the monsoon session on 29 July 2024 (News On AIR)."),
    ],
}

r["projects"] = [
    proj("noida-airport", L("Noida International Airport, Jewar (Phase I)", "नोएडा अंतरराष्ट्रीय हवाई अड्डा, जेवर (चरण I)", "नोएडा आंतरराष्ट्रीय विमानतळ, जेवर (टप्पा I)"),
         L("A second airport for the Delhi region, at Jewar in Gautam Buddh Nagar district, built under a public–private partnership. Phase I has a 3,900 m runway for wide-body aircraft and a capacity of 12 million passengers a year, expandable to 70 million. Inaugurated on 28 March 2026.",
           "दिल्ली क्षेत्र के लिए दूसरा हवाई अड्डा, गौतम बुद्ध नगर ज़िले के जेवर में, सार्वजनिक–निजी भागीदारी से बना। चरण I में चौड़े विमानों के लिए 3,900 मीटर का रनवे है और क्षमता सालाना 1.2 करोड़ यात्रियों की है, जिसे 7 करोड़ तक बढ़ाया जा सकता है। 28 मार्च 2026 को उद्घाटन।",
           "दिल्ली परिसरासाठी दुसरे विमानतळ, गौतमबुद्धनगर जिल्ह्यातील जेवर येथे, सार्वजनिक–खासगी भागीदारीतून उभारलेले. टप्पा I मध्ये रुंद विमानांसाठी 3,900 मीटरची धावपट्टी असून वार्षिक क्षमता 1.2 कोटी प्रवासी आहे, जी 7 कोटींपर्यंत वाढवता येईल. 28 मार्च 2026 रोजी उद्घाटन."),
         "transport", None, 11200, "About ₹11,200 crore for Phase I (PMO).", "2026",
         None, "March 2026", "Completed", "pmindia", NIA),
    proj("ganga-expressway", L("Ganga Expressway (Meerut–Prayagraj)", "गंगा एक्सप्रेसवे (मेरठ–प्रयागराज)", "गंगा द्रुतगती मार्ग (मेरठ–प्रयागराज)"),
         L("A 594 km access-controlled expressway through 12 districts from Meerut to Prayagraj, cutting the journey from about 12 hours to about 6. Built by the Uttar Pradesh Expressways Industrial Development Authority; inaugurated on 29 April 2026.",
           "मेरठ से प्रयागराज तक 12 ज़िलों से गुज़रने वाला 594 किमी का एक्सेस-नियंत्रित एक्सप्रेसवे, जिससे यात्रा लगभग 12 घंटे से घटकर लगभग 6 घंटे रह जाती है। उत्तर प्रदेश एक्सप्रेसवे औद्योगिक विकास प्राधिकरण द्वारा निर्मित; 29 अप्रैल 2026 को उद्घाटन।",
           "मेरठपासून प्रयागराजपर्यंत 12 जिल्ह्यांतून जाणारा 594 किमीचा प्रवेश-नियंत्रित द्रुतगती मार्ग; प्रवास सुमारे 12 तासांवरून सुमारे 6 तासांवर येतो. उत्तर प्रदेश द्रुतगती मार्ग औद्योगिक विकास प्राधिकरणाने बांधला; 29 एप्रिल 2026 रोजी उद्घाटन."),
         "transport", "Uttar Pradesh Expressways Industrial Development Authority (UPEIDA)", None, None, None,
         None, "April 2026", "Completed", "newsonair", GANGA),
]

GI_NAMES = {
 "Allahabad Surkha Guava": ("इलाहाबादी सुर्ख़ा अमरूद", "अलाहाबादी सुरखा पेरू"),
 "Mango Malihabadi Dusseheri": ("मलीहाबादी दशहरी आम", "मलीहाबादी दशेरी आंबा"),
 "Kalanamak Rice": ("कालानमक चावल", "काळानमक तांदूळ"),
 "Rataul Mango": ("रटौल आम", "रटौल आंबा"),
 "Adamchini Chawal": ("आदमचीनी चावल", "आदमचिनी तांदूळ"),
 "Pratapgarh Aonla": ("प्रतापगढ़ आँवला", "प्रतापगढ आवळा"),
 "Banaras Langda Aam (Mango)": ("बनारसी लंगड़ा आम", "बनारसी लंगडा आंबा"),
 "Ramnagar Bhanta (Brinjal)": ("रामनगर भंटा (बैंगन)", "रामनगर भांटा (वांगे)"),
 "Banaras Pan (Betel Leaf)": ("बनारसी पान", "बनारसी विड्याचे पान"),
 "Banaras Lal Bharwamirch": ("बनारसी लाल भरवा मिर्च", "बनारसी लाल भरली मिरची"),
 "Chiraigaon Karonda of Varanasi": ("वाराणसी का चिरईगाँव करौंदा", "वाराणसीचे चिरईगाव करवंद"),
 "Hathras Hing": ("हाथरस हींग", "हाथरस हिंग"),
 "Muzaffarnagar Gur (Jaggery)": ("मुज़फ़्फ़रनगर गुड़", "मुजफ्फरनगर गूळ"),
 "Banaras Lal Peda": ("बनारसी लाल पेड़ा", "बनारसी लाल पेढा"),
 "Jaunpur Imarti": ("जौनपुर इमरती", "जौनपूर इमरती"),
 "Banaras Thandai": ("बनारसी ठंडाई", "बनारसी थंडाई"),
 "Banaras Tirangi Barfi": ("बनारसी तिरंगी बर्फ़ी", "बनारसी तिरंगी बर्फी"),
 "Banaras Brocades And Sarees": ("बनारसी ब्रोकेड और साड़ियाँ", "बनारसी जरीकाम व साड्या"),
 "Lucknow Chikan Craft": ("लखनवी चिकनकारी", "लखनवी चिकनकारी"),
 "Hand Made Carpet of Bhadohi": ("भदोही का हस्तनिर्मित क़ालीन", "भदोहीचा हाताने विणलेला गालिचा"),
 "Firozabad Glass (Logo)": ("फ़िरोज़ाबाद काँच (लोगो)", "फिरोजाबाद काच (बोधचिन्ह)"),
 "Kanpur Saddlery (Logo)": ("कानपुर ज़ीनसाज़ी (लोगो)", "कानपूर खोगीर (बोधचिन्ह)"),
 "Moradabad Metal Craft (Logo)": ("मुरादाबाद धातु शिल्प (लोगो)", "मुरादाबाद धातुकाम (बोधचिन्ह)"),
 "Varanasi Glass Beads": ("वाराणसी काँच के मनके", "वाराणसी काचेचे मणी"),
 "Khurja Pottery": ("खुर्जा मृद्भांड", "खुर्जा मातीची भांडी"),
 "Saharanpur Wood Craft": ("सहारनपुर काष्ठ शिल्प", "सहारनपूर काष्ठकला"),
 "Agra Durrie": ("आगरा दरी", "आग्रा सतरंजी"),
 "Farrukhabad Prints": ("फ़र्रुख़ाबाद छपाई", "फर्रुखाबाद छपाई"),
 "Lucknow Zardozi": ("लखनऊ ज़रदोज़ी", "लखनौ जरदोजी"),
 "Banaras Brocades And Sarees (Logo)": ("बनारसी ब्रोकेड और साड़ियाँ (लोगो)", "बनारसी जरीकाम व साड्या (बोधचिन्ह)"),
 "Banaras Gulabi Meenakari Craft": ("बनारसी गुलाबी मीनाकारी", "बनारसी गुलाबी मीनाकारी"),
 "Banaras Metal Repouse Craft": ("बनारसी धातु उभार (रिपूसे) शिल्प", "बनारसी धातू उठाव (रिपूसे) काम"),
 "Varanasi Wooden Lacquerware & Toys": ("वाराणसी लकड़ी के लाख के बर्तन और खिलौने", "वाराणसी लाखेची लाकडी भांडी व खेळणी"),
 "Mirzapur Handmade Dari": ("मिर्ज़ापुर हस्तनिर्मित दरी", "मिर्झापूर हाताने विणलेली सतरंजी"),
 "Nizamabad Black Clay Pottery": ("निज़ामाबाद काली मिट्टी के बर्तन", "निजामाबाद काळ्या मातीची भांडी"),
 "Ghazipur Wall Hanging": ("ग़ाज़ीपुर दीवार सज्जा", "गाझीपूर भिंत सजावट"),
 "Varanasi Soft Stone Jali Work": ("वाराणसी मुलायम पत्थर जाली काम", "वाराणसी मऊ दगडी जाळीकाम"),
 "Gorakhpur Terracotta": ("गोरखपुर टेराकोटा", "गोरखपूर टेराकोटा"),
 "Banaras Zardozi": ("बनारसी ज़रदोज़ी", "बनारसी जरदोजी"),
 "Chunar Glaze Pottery": ("चुनार चमकदार मृद्भांड", "चुनार चकाकी मातीची भांडी"),
 "Mirzapur Pital Bartan": ("मिर्ज़ापुर पीतल बर्तन", "मिर्झापूर पितळी भांडी"),
 "Banaras Wood Carving": ("बनारसी काष्ठ नक़्क़ाशी", "बनारसी काष्ठ कोरीवकाम"),
 "Banaras Hand Block Print": ("बनारसी हस्त ठप्पा छपाई", "बनारसी हातठसा छपाई"),
 "Mau Saree": ("मऊ साड़ी", "मऊ साडी"),
 "Aligarh Tala": ("अलीगढ़ ताला", "अलीगढ कुलूप"),
 "Bakhira Brassware": ("बखिरा पीतल के बर्तन", "बखिरा पितळी भांडी"),
 "Banda Shazar Patthar craft": ("बाँदा शजर पत्थर शिल्प", "बांदा शजर दगड कलाकुसर"),
 "Nagina Wood Craft": ("नगीना काष्ठ शिल्प", "नगीना काष्ठकला"),
 "Mahoba Gaura Patthar Hastashlip": ("महोबा गौरा पत्थर हस्तशिल्प", "महोबा गौरा दगड हस्तकला"),
 "Mainpuri Tarkashi": ("मैनपुरी तारकशी", "मैनपुरी तारकशी"),
 "Sambhal Horn Craft": ("संभल सींग शिल्प", "संभल शिंगकाम"),
 "Amroha Dholak": ("अमरोहा ढोलक", "अमरोहा ढोलक"),
 "Baghpat Home Furnishings": ("बागपत गृह सज्जा वस्त्र", "बागपत गृहसजावट वस्त्रे"),
 "Barabanki Handloom Product": ("बाराबंकी हथकरघा उत्पाद", "बाराबंकी हातमाग उत्पादने"),
 "Kalpi Handmade Paper": ("कालपी हस्तनिर्मित काग़ज़", "काल्पी हातकागद"),
 "Jalesar Dhatu Shilp (Metal Craft)": ("जलेसर धातु शिल्प", "जलेसर धातुकाम"),
 "Patchwork of Rampur": ("रामपुर का पैचवर्क", "रामपूरचे ठिगळकाम (पॅचवर्क)"),
 "Mathura Sanjhi Craft": ("मथुरा साँझी शिल्प", "मथुरा सांझी कला"),
 "Banaras Tabla": ("बनारसी तबला", "बनारसी तबला"),
 "Pilibhit Bansuri": ("पीलीभीत बाँसुरी", "पिलीभीत बासरी"),
 "Banaras Shehnai": ("बनारसी शहनाई", "बनारसी सनई"),
 "Sambhal Bone Craft": ("संभल अस्थि शिल्प", "संभल हाडकाम कला"),
 "Moonj Craft of Uttar Pradesh": ("उत्तर प्रदेश का मूँज शिल्प", "उत्तर प्रदेशची मुंज गवत कला"),
 "Chitrakoot Wooden Craft & Toys": ("चित्रकूट काष्ठ शिल्प और खिलौने", "चित्रकूट काष्ठकला व खेळणी"),
 "Banaras Mural Painting": ("बनारसी भित्ति चित्रकला", "बनारसी भित्तिचित्रकला"),
 "Pilkhuwa Hand Block Print Textile": ("पिलखुवा हस्त ठप्पा छपाई वस्त्र", "पिलखुवा हातठसा छपाई वस्त्र"),
 "Banaras Metal Casting Craft": ("बनारसी धातु ढलाई शिल्प", "बनारसी धातू ओतकाम"),
 "Bareilly Cane & Bamboo Craft": ("बरेली बेंत और बाँस शिल्प", "बरेली वेत व बांबू कला"),
 "Tharu Embroidery of Uttar Pradesh": ("उत्तर प्रदेश की थारू कढ़ाई", "उत्तर प्रदेशचे थारू भरतकाम"),
 "Bareilly Zari Zardoji": ("बरेली ज़री ज़रदोज़ी", "बरेली जरी जरदोजी"),
 "Mathura Zari Poshak": ("मथुरा ज़री पोशाक", "मथुरा जरी पोशाख"),
 "Kannauj Perfume (Logo)": ("कन्नौज इत्र (लोगो)", "कन्नौज अत्तर (बोधचिन्ह)"),
 "Meerut Scissors": ("मेरठ कैंची", "मेरठ कात्री"),
 "Agra Leather Footwear": ("आगरा चमड़े के जूते", "आग्रा चामडी पादत्राणे"),
 "Meerut Bugle": ("मेरठ बिगुल", "मेरठ बिगुल"),
 "Chunar Balua Patthar": ("चुनार बलुआ पत्थर", "चुनार वालुकाश्म"),
 "Agra Stone Inlay Work": ("आगरा पत्थर पच्चीकारी", "आग्रा दगडी जडावकाम"),
 "Bareilly Terracotta": ("बरेली टेराकोटा", "बरेली टेराकोटा"),
}
TEXTILE = {"Banaras Brocades And Sarees", "Lucknow Chikan Craft", "Hand Made Carpet of Bhadohi", "Agra Durrie", "Farrukhabad Prints", "Lucknow Zardozi",
           "Banaras Brocades And Sarees (Logo)", "Mirzapur Handmade Dari", "Banaras Zardozi", "Banaras Hand Block Print", "Mau Saree",
           "Baghpat Home Furnishings", "Barabanki Handloom Product", "Pilkhuwa Hand Block Print Textile", "Tharu Embroidery of Uttar Pradesh",
           "Bareilly Zari Zardoji", "Mathura Zari Poshak", "Patchwork of Rampur"}
r["giProducts"] = gi_list("gi_up.tsv", GI_NAMES, {}, TEXTILE)
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-UP.json", r)
print("up core ok", len(r["giProducts"]), "GIs")
