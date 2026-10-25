"""Manipur modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-MN"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_MN = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 25 Oct 2026. "
           "FY2024-25 is the latest year published for Manipur and may be revised.")
mo = research("mospi_mn.json")
C = research("census_b5plus.json")
NAME = L("Manipur", "मणिपुर", "मणिपूर")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Manipuri dance (Jagoi), one of India's classical dance forms, grew out of the Ras Lila of the Vaishnava tradition and the much older Lai Haraoba, a festival in which priestesses (maibis) re-enact the creation of the world in honour of the umang lai, the forest deities. Nata sankirtana, devotional singing and drumming with the pung, is on UNESCO's list of the Intangible Cultural Heritage of Humanity. Thang-ta, the martial art of sword and spear, and sagol kangjei (polo) are traditional, and Shumang Leela, a travelling theatre, is popular across the valley. Naga and Kuki-Zo tribes have their own song, dance and festivals, such as Lui-Ngai-Ni, Chumpha and Kut, and every community is known for its handloom.",
        "मणिपुरी नृत्य (जगोई), भारत के शास्त्रीय नृत्यों में से एक, वैष्णव परंपरा की रास लीला और कहीं पुराने लाई हराओबा से विकसित हुआ, जिस त्योहार में पुजारिनें (माइबी) वन देवताओं, उमंग लाई, के सम्मान में सृष्टि की रचना का अभिनय करती हैं। पुंग (ढोल) के साथ भक्ति गायन और वादन, नट संकीर्तन, यूनेस्को की मानवता की अमूर्त सांस्कृतिक धरोहर की सूची में है। तलवार और भाले की युद्ध कला थांग-ता और सगोल कांगजेई (पोलो) पारंपरिक हैं, और घूमने वाला रंगमंच शुमांग लीला पूरी घाटी में लोकप्रिय है। नागा और कुकी-ज़ो जनजातियों के अपने गीत, नृत्य और लुई-ङाई-नी, चुम्फा और कुट जैसे त्योहार हैं, और हर समुदाय अपने हथकरघे के लिए जाना जाता है।",
        "मणिपुरी नृत्य (जगोई), भारताच्या शास्त्रीय नृत्यप्रकारांपैकी एक, वैष्णव परंपरेतील रासलीला व त्याहूनही जुन्या लाई हराओबातून विकसित झाले, ज्या सणात पुजारिणी (माइबी) वनदेवता, उमंग लाई, यांच्या सन्मानार्थ सृष्टिनिर्मितीचे सादरीकरण करतात. पुंग (ढोल) सह भक्तिगायन व वादन, नट संकीर्तन, युनेस्कोच्या मानवतेच्या अमूर्त सांस्कृतिक वारसा यादीत आहे. तलवार व भाल्याची युद्धकला थांग-ता आणि सगोल कांगजेई (पोलो) पारंपरिक आहेत, आणि फिरते रंगभूमी शुमांग लीला संपूर्ण खोऱ्यात लोकप्रिय आहे. नागा व कुकी-झो जमातींची स्वतःची गीते, नृत्ये आणि लुई-ङाई-नी, चुम्फा व कुटसारखे सण आहेत, आणि प्रत्येक समुदाय आपल्या हातमागासाठी ओळखला जातो."),
        conf="Editorial"),
    lst("festivals", [
        fest("laiharaoba", "Lai Haraoba", "लाई हराओबा", "लाई हराओबा", ("April–May", "अप्रैल–मई", "एप्रिल–मे"),
             ("Ritual festival of the forest deities, with dance by maibis.", "वन देवताओं का अनुष्ठानिक त्योहार, माइबियों के नृत्य के साथ।", "वनदेवतांचा विधिपर सण, माइबींच्या नृत्यासह.")),
        fest("yaoshang", "Yaoshang", "याओशांग", "याओशांग", ("February–March", "फ़रवरी–मार्च", "फेब्रुवारी–मार्च"),
             ("Five-day spring festival at the time of Holi, with sports and the thabal chongba dance.", "होली के समय पाँच दिन का वसंत उत्सव, खेलों और थाबल चोंगबा नृत्य के साथ।", "होळीच्या वेळी पाच दिवसांचा वसंतोत्सव, खेळ व थाबल चोंगबा नृत्यासह.")),
        fest("ningol", "Ningol Chakouba", "निंगोल चाकौबा", "निंगोल चाकौबा", ("October–November", "अक्टूबर–नवंबर", "ऑक्टोबर–नोव्हेंबर"),
             ("Married daughters are invited home for a feast.", "विवाहित बेटियों को भोज के लिए मायके बुलाया जाता है।", "विवाहित मुलींना माहेरी मेजवानीसाठी बोलावले जाते.")),
        fest("kut", "Kut", "कुट", "कुट", ("1 November", "1 नवंबर", "1 नोव्हेंबर"),
             ("Post-harvest festival of the Kuki-Zo tribes.", "कुकी-ज़ो जनजातियों का फ़सल कटाई के बाद का त्योहार।", "कुकी-झो जमातींचा सुगीनंतरचा सण.")),
        fest("luingai", "Lui-Ngai-Ni", "लुई-ङाई-नी", "लुई-ङाई-नी", ("15 February", "15 फ़रवरी", "15 फेब्रुवारी"),
             ("Seed-sowing festival of the Naga tribes.", "नागा जनजातियों का बीज-बुवाई त्योहार।", "नागा जमातींचा बीजपेरणीचा सण.")),
        fest("sangai", "Sangai Festival", "संगाई महोत्सव", "संगाई महोत्सव", ("November", "नवंबर", "नोव्हेंबर"),
             ("State tourism festival named after the sangai deer.", "संगाई हिरण के नाम पर राज्य का पर्यटन महोत्सव।", "संगाई हरिणाच्या नावाचा राज्याचा पर्यटन महोत्सव.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("jagoi", "Manipuri dance (Ras Lila)", "मणिपुरी नृत्य (रास लीला)", "मणिपुरी नृत्य (रासलीला)"), it3("sankirtana", "Nata sankirtana", "नट संकीर्तन", "नट संकीर्तन"),
        it3("thangta", "Thang-ta", "थांग-ता", "थांग-ता"), it3("shumang", "Shumang Leela", "शुमांग लीला", "शुमांग लीला"),
        it3("pottery", "Longpi black pottery", "लोंगपी काली मिट्टी के बर्तन", "लोंगपी काळी मातीची भांडी"), it3("weaving", "Handloom weaving", "हथकरघा बुनाई", "हातमाग विणकाम"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("eromba", "Eromba", "एरोम्बा", "एरोम्बा", d=("Mashed vegetables with fermented fish (ngari) and chilli.", "किण्वित मछली (ङारी) और मिर्च के साथ मसली सब्ज़ियाँ।", "आंबवलेला मासा (ङारी) व मिरचीसह कुस्करलेल्या भाज्या.")),
        it3("singju", "Singju", "सिंगजू", "सिंगजू", d=("Salad of shredded greens, lotus stem and roasted gram flour.", "कटे साग, कमल ककड़ी और भुने बेसन का सलाद।", "चिरलेल्या पालेभाज्या, कमळकाकडी व भाजलेल्या बेसनाची कोशिंबीर.")),
        it3("chakhao", "Chak-hao kheer", "चाक-हाओ खीर", "चाक-हाओ खीर", d=("Purple-black rice pudding; chak-hao is a registered GI.", "बैंगनी-काले चावल की खीर; चाक-हाओ पंजीकृत जीआई है।", "जांभळ्या-काळ्या तांदळाची खीर; चाक-हाओ नोंदणीकृत जीआय आहे.")),
        it3("kangshoi", "Kangshoi", "कांगशोई", "कांगशोई", d=("Light vegetable stew.", "हल्का सब्ज़ी का शोरबा।", "हलका भाज्यांचा रस्सा.")),
        it3("chamthong", "Chamthong", "चामथोंग", "चामथोंग", d=("Clear vegetable and fish broth.", "सब्ज़ी और मछली का पतला शोरबा।", "भाज्या व माशांचा पातळ रस्सा.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("phanek", "Phanek and innaphi", "फ़ानेक और इन्नाफ़ी", "फानेक व इन्नाफी", d=("Wrap-around skirt and shawl worn by Meitei women.", "मैतेई महिलाओं की लपेटने वाली घाघरी और शॉल।", "मैतेई स्त्रियांचा गुंडाळून नेसायचा परकर व शाल.")),
        it3("potloi", "Potloi", "पोटलोई", "पोटलोई", d=("Stiff cylindrical skirt worn in Ras Lila and by brides.", "रास लीला में और दुल्हनों द्वारा पहनी जाने वाली कड़ी बेलनाकार घाघरी।", "रासलीलेत व वधू परिधान करतात तो कडक दंडगोलाकार परकर.")),
        it3("shawls", "Tribal shawls", "जनजातीय शॉल", "आदिवासी शाली", d=("Each Naga and Kuki-Zo tribe has its own patterns, such as the Tangkhul kashan.", "हर नागा और कुकी-ज़ो जनजाति के अपने नमूने हैं, जैसे तांगखुल काशान।", "प्रत्येक नागा व कुकी-झो जमातीची स्वतःची नक्षी आहे, उदा. तांगखुल काशान.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
    gaps("g", [(L("UNESCO inscription of sankirtana — link", "संकीर्तन का यूनेस्को अंकन — लिंक", "संकीर्तनाची युनेस्को नोंद — दुवा"), "unesco-whc", "UNESCO Intangible Cultural Heritage list (2013).")]),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; pa = 100 * g["public_admin"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["MN"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["MN"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Manipur's GSDP at current prices was about ₹{inr(cur['FY2024-25'][0])} crore in FY2024-25, the latest year in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2024-25'][0])}. Agriculture, livestock, forestry and fishing contributed about {agri:.0f}% of GSVA — rice in the valley, terraced and jhum farming in the hills, fruit such as pineapple, orange and Kachai lemon, and fish from Loktak and the wetlands. Public administration made up about {pa:.0f}%, while manufacturing was only about {mfg:.1f}%; handloom and handicrafts are the main industries and employ many women. Border trade with Myanmar passes through Moreh.\n\nThe PLFS unemployment rate was {ur['2025']}% in 2025 (national {ui['2025']}%), and {lf['female']}% of women aged 15 and above were in the labour force, against {lfi['female']}% nationally. The violence since 2023 disrupted trade, transport and farming, and displaced many families from their land.",
        f"मोस्पी शृंखला के नवीनतम वर्ष, वित्त वर्ष 2024-25 में मणिपुर का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{inr(cur['FY2024-25'][0])} करोड़ और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2024-25'][0])} था। कृषि, पशुपालन, वानिकी और मत्स्य पालन का जीएसवीए में योगदान लगभग {agri:.0f}% था — घाटी में धान, पहाड़ियों में सीढ़ीदार और झूम खेती, अनानास, संतरा और काचाई नींबू जैसे फल, और लोकटक व आर्द्रभूमियों से मछली। लोक प्रशासन का हिस्सा लगभग {pa:.0f}% था, जबकि विनिर्माण केवल लगभग {mfg:.1f}% था; हथकरघा और हस्तशिल्प मुख्य उद्योग हैं और बहुत सी महिलाओं को रोज़गार देते हैं। म्यांमार के साथ सीमा व्यापार मोरेह से होता है।\n\nपीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी (राष्ट्रीय {ui['2025']}%), और 15 वर्ष से अधिक आयु की {lf['female']}% महिलाएँ श्रम बल में थीं, जबकि राष्ट्रीय स्तर पर {lfi['female']}%। 2023 से चली हिंसा ने व्यापार, परिवहन और खेती को बाधित किया, और बहुत से परिवारों को उनकी भूमि से विस्थापित किया।",
        f"मोस्पी मालिकेतील नवीनतम वर्ष, आ.व. 2024-25 मध्ये मणिपूरचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{inr(cur['FY2024-25'][0])} कोटी व दरडोई एनएसडीपी ₹{inr(pc['FY2024-25'][0])} होते. शेती, पशुपालन, वनीकरण व मासेमारीचा जीएसव्हीएमध्ये वाटा सुमारे {agri:.0f}% होता — खोऱ्यात भात, डोंगरांत पायऱ्यांची व झूम शेती, अननस, संत्री व काचाई लिंबूसारखी फळे, आणि लोकटक व पाणथळींतील मासे. लोकप्रशासनाचा वाटा सुमारे {pa:.0f}% होता, तर उत्पादन उद्योग केवळ सुमारे {mfg:.1f}% होता; हातमाग व हस्तकला हे मुख्य उद्योग आहेत आणि अनेक स्त्रियांना रोजगार देतात. म्यानमारशी सीमाव्यापार मोरेहमार्गे होतो.\n\nपीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता (राष्ट्रीय {ui['2025']}%), आणि 15 वर्षांवरील {lf['female']}% स्त्रिया श्रमशक्तीत होत्या, तर राष्ट्रीय पातळीवर {lfi['female']}%. 2023 पासूनच्या हिंसाचाराने व्यापार, वाहतूक व शेती विस्कळीत झाली, आणि अनेक कुटुंबे आपल्या जमिनींवरून विस्थापित झाली."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_MN), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_MN), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_MN), "rupee", "higher-is-better",
             previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("MN", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    plfs_series("MN", NAME),
    lst("sectors-key", [
        it3("handloom", "Handloom and handicrafts", "हथकरघा और हस्तशिल्प", "हातमाग व हस्तकला", d=("Phanek, shawls, Moirang phee and Longpi pottery.", "फ़ानेक, शॉल, मोइरांग फ़ी और लोंगपी के बर्तन।", "फानेक, शाली, मोइरांग फी व लोंगपी भांडी.")),
        it3("rice", "Rice and horticulture", "धान और बाग़वानी", "भात व फलोत्पादन", d=("Black rice, pineapple, orange, Kachai lemon.", "काला चावल, अनानास, संतरा, काचाई नींबू।", "काळा तांदूळ, अननस, संत्री, काचाई लिंबू.")),
        it3("fish", "Fisheries", "मत्स्य पालन", "मत्स्यव्यवसाय", d=("Loktak and valley wetlands.", "लोकटक और घाटी की आर्द्रभूमियाँ।", "लोकटक व खोऱ्यातील पाणथळी.")),
        it3("border", "Border trade", "सीमा व्यापार", "सीमाव्यापार", d=("Through Moreh–Tamu with Myanmar.", "म्यांमार के साथ मोरेह–तामू से।", "म्यानमारशी मोरेह–तामूमार्गे.")),
        it3("sericulture", "Sericulture", "रेशम उत्पादन", "रेशीम उद्योग", d=("Mulberry, eri, muga and oak tasar silk.", "शहतूत, एरी, मूगा और ओक तसर रेशम।", "तुती, एरी, मुगा व ओक टसर रेशीम.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Economic impact of the conflict since 2023 — official estimate", "2023 से संघर्ष का आर्थिक प्रभाव — आधिकारिक अनुमान", "2023 पासूनच्या संघर्षाचा आर्थिक परिणाम — अधिकृत अंदाज"), "state-economic-survey", "Economic Survey of Manipur."),
        (L("Border trade through Moreh by year", "मोरेह से वर्षवार सीमा व्यापार", "मोरेहमार्गे वर्षनिहाय सीमाव्यापार"), "india-gov", "Department of Commerce / Land Ports Authority of India."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Manipur has a unicameral, 60-member Legislative Assembly in Imphal, 40 of whose seats are in the valley and 20 in the hills. Under Article 371C of the Constitution, a Hill Areas Committee of the Assembly's hill members has a special role in laws and budgets for the hill areas. The State elects 2 members to the Lok Sabha (Inner and Outer Manipur) and 1 to the Rajya Sabha.\n\nThe Assembly elected in 2022 was kept in suspended animation during President's Rule, imposed on 13 February 2025 after Chief Minister N. Biren Singh resigned. The proclamation was revoked on 4 February 2026, and Yumnam Khemchand Singh of the BJP was sworn in as Chief Minister the same day, with Nemcha Kipgen and L. Dikho as Deputy Chief Ministers. Thokchom Satyabrata Singh has been Speaker since March 2022 and Ajay Kumar Bhalla Governor since January 2025. The next Assembly election is due by early 2027.",
        "मणिपुर में इंफाल में 60 सदस्यों वाली एकसदनीय विधानसभा है, जिसकी 40 सीटें घाटी में और 20 पहाड़ियों में हैं। संविधान के अनुच्छेद 371ग के तहत विधानसभा के पहाड़ी सदस्यों की पहाड़ी क्षेत्र समिति की पहाड़ी क्षेत्रों के क़ानूनों और बजट में विशेष भूमिका है। राज्य से लोकसभा के 2 (आंतरिक और बाहरी मणिपुर) और राज्यसभा का 1 सदस्य चुना जाता है।\n\nमुख्यमंत्री एन. बीरेन सिंह के इस्तीफ़े के बाद 13 फ़रवरी 2025 को लगे राष्ट्रपति शासन में 2022 में चुनी गई विधानसभा निलंबित अवस्था में रखी गई। 4 फ़रवरी 2026 को उद्घोषणा वापस ली गई, और उसी दिन भाजपा के युमनाम खेमचंद सिंह ने मुख्यमंत्री पद की शपथ ली, नेमचा किपगेन और एल. दिखो उपमुख्यमंत्री बने। थोकचोम सत्यव्रत सिंह मार्च 2022 से अध्यक्ष और अजय कुमार भल्ला जनवरी 2025 से राज्यपाल हैं। अगला विधानसभा चुनाव 2027 की शुरुआत तक होना है।",
        "मणिपूरमध्ये इंफाळ येथे 60 सदस्यांची एकसदनी विधानसभा आहे, जिच्या 40 जागा खोऱ्यात व 20 डोंगरी भागात आहेत. संविधानाच्या अनुच्छेद 371ग अन्वये विधानसभेच्या डोंगरी सदस्यांच्या डोंगरी क्षेत्र समितीला डोंगरी भागांच्या कायदे व अर्थसंकल्पात विशेष भूमिका आहे. राज्यातून लोकसभेवर 2 (अंतर्गत व बाह्य मणिपूर) आणि राज्यसभेवर 1 सदस्य निवडला जातो.\n\nमुख्यमंत्री एन. बीरेन सिंह यांच्या राजीनाम्यानंतर 13 फेब्रुवारी 2025 रोजी लागू झालेल्या राष्ट्रपती राजवटीत 2022 मध्ये निवडलेली विधानसभा निलंबित अवस्थेत ठेवली गेली. 4 फेब्रुवारी 2026 रोजी घोषणा मागे घेतली गेली, आणि त्याच दिवशी भाजपचे युमनाम खेमचंद सिंह यांनी मुख्यमंत्रिपदाची शपथ घेतली, नेमचा किपगेन व एल. दिखो उपमुख्यमंत्री झाले. थोकचोम सत्यव्रत सिंह मार्च 2022 पासून अध्यक्ष आणि अजय कुमार भल्ला जानेवारी 2025 पासून राज्यपाल आहेत. पुढील विधानसभा निवडणूक 2027 च्या सुरुवातीपर्यंत होणे अपेक्षित आहे."),
        sources=["hitavada", "mn-assembly", "newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("assembly", "Manipur Legislative Assembly", "मणिपुर विधानसभा", "मणिपूर विधानसभा", url="https://assembly.mn.gov.in", src="mn-assembly"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2022 Assembly election — party-wise result", "2022 विधानसभा चुनाव — दलवार परिणाम", "2022 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Manipur 2022."),
        (L("Chief Minister's swearing-in — official source", "मुख्यमंत्री का शपथ ग्रहण — आधिकारिक स्रोत", "मुख्यमंत्र्यांचा शपथविधी — अधिकृत स्रोत"), "india-gov", "Replace the news report with the Government of Manipur notification."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "The Jiribam–Imphal railway, built through steep, earthquake-prone hills, will bring broad-gauge trains to Imphal. Other works — the four-laning of the Imphal–Moreh road on the India–Myanmar–Thailand Trilateral Highway corridor and the restoration of roads and houses damaged since 2023 — will be added as cards once their status is confirmed from official sources. Each card shows its source and the date it was checked.",
        "खड़ी, भूकंप-प्रवण पहाड़ियों से होकर बन रही जिरीबाम–इंफाल रेलवे इंफाल तक बड़ी लाइन की ट्रेनें लाएगी। अन्य कार्य — भारत–म्यांमार–थाईलैंड त्रिपक्षीय राजमार्ग गलियारे पर इंफाल–मोरेह सड़क का चार-लेन विस्तार और 2023 से क्षतिग्रस्त सड़कों और घरों की मरम्मत — आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर कार्ड के रूप में जोड़े जाएँगे। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "तीव्र, भूकंपप्रवण डोंगरांतून बांधली जाणारी जिरीबाम–इंफाळ रेल्वे इंफाळपर्यंत ब्रॉडगेज गाड्या आणेल. इतर कामे — भारत–म्यानमार–थायलंड त्रिपक्षीय महामार्ग मार्गिकेवरील इंफाळ–मोरेह रस्त्याचे चौपदरीकरण आणि 2023 पासून नुकसान झालेल्या रस्ते व घरांची दुरुस्ती — अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर कार्डे म्हणून जोडली जातील. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["morung-express"], conf="Third-party verified"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Jiribam–Imphal line — sanctioned cost and official progress", "जिरीबाम–इंफाल लाइन — स्वीकृत लागत और आधिकारिक प्रगति", "जिरीबाम–इंफाळ मार्ग — मंजूर खर्च व अधिकृत प्रगती"), "railways", "Ministry of Railways / Parliament answer; replace the news report."),
        (L("Imphal–Moreh highway — status", "इंफाल–मोरेह राजमार्ग — स्थिति", "इंफाळ–मोरेह महामार्ग — स्थिती"), "morth", "MoRTH / NHIDCL."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Manipur depends on two highways: NH-2 north through Kohima to Dimapur, and NH-37 west through Jiribam to Silchar in Assam. Both cross long stretches of hill road and are often hit by landslides and blockades, so supplies of fuel and food are easily disrupted. NH-102 (part of Asian Highway 1) runs south-east to Moreh on the Myanmar border. Bir Tikendrajit International Airport at Imphal has flights to Guwahati, Kolkata, Delhi and other cities and is the State's main link with the rest of India. The railway reaches Jiribam and Khongsang; the line to Imphal is under construction.",
        "मणिपुर दो राजमार्गों पर निर्भर है: उत्तर में कोहिमा होकर दीमापुर तक एनएच-2, और पश्चिम में जिरीबाम होकर असम के सिलचर तक एनएच-37। दोनों लंबी पहाड़ी सड़कों से गुज़रते हैं और अक्सर भूस्खलन और नाकेबंदी से प्रभावित होते हैं, इसलिए ईंधन और खाद्य की आपूर्ति आसानी से बाधित होती है। एनएच-102 (एशियाई राजमार्ग 1 का भाग) दक्षिण-पूर्व में म्यांमार सीमा पर मोरेह तक जाता है। इंफाल का बीर टिकेंद्रजीत अंतरराष्ट्रीय हवाई अड्डा गुवाहाटी, कोलकाता, दिल्ली और अन्य नगरों से जुड़ा है और शेष भारत से राज्य की मुख्य कड़ी है। रेलवे जिरीबाम और खोंगसांग तक पहुँचती है; इंफाल तक लाइन निर्माणाधीन है।",
        "मणिपूर दोन महामार्गांवर अवलंबून आहे: उत्तरेला कोहिमामार्गे दिमापूरपर्यंत एनएच-2, आणि पश्चिमेला जिरीबाममार्गे आसाममधील सिलचरपर्यंत एनएच-37. दोन्ही लांब डोंगरी रस्त्यांतून जातात आणि अनेकदा भूस्खलन व अडवणुकीने प्रभावित होतात, त्यामुळे इंधन व अन्नपुरवठा सहज विस्कळीत होतो. एनएच-102 (आशियाई महामार्ग 1 चा भाग) आग्नेयेला म्यानमार सीमेवरील मोरेहपर्यंत जातो. इंफाळचा बीर टिकेंद्रजीत आंतरराष्ट्रीय विमानतळ गुवाहाटी, कोलकाता, दिल्ली व इतर शहरांशी जोडलेला आहे आणि उर्वरित भारताशी राज्याचा मुख्य दुवा आहे. रेल्वे जिरीबाम व खोंगसांगपर्यंत पोहोचते; इंफाळपर्यंतचा मार्ग बांधकामाधीन आहे."),
        conf="Editorial"),
    lst("airports", [
        it3("imf", "Bir Tikendrajit International Airport, Imphal", "बीर टिकेंद्रजीत अंतरराष्ट्रीय हवाई अड्डा, इंफाल", "बीर टिकेंद्रजीत आंतरराष्ट्रीय विमानतळ, इंफाळ", m=("IMF", "IMF", "IMF")),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("Inner Line Permit rules (since 2019)", "इनर लाइन परमिट नियम (2019 से)", "इनर लाइन परवाना नियम (2019 पासून)"), "india-gov", "Government of Manipur ILP portal."),
        (L("Passenger traffic at Imphal airport", "इंफाल हवाई अड्डे पर यात्री यातायात", "इंफाळ विमानतळावरील प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Manipur produces little of its own electricity. The Loktak hydroelectric project of NHPC, commissioned in 1983, uses water diverted from Loktak lake through a tunnel to a power house at Leimatak, and its barrage at Ithai changed the lake's water levels and the life of its phumdis. Most power comes from central stations in the North-East through the regional grid, and solar power and pre-paid smart meters are being expanded.",
        "मणिपुर अपनी बहुत कम बिजली स्वयं बनाता है। एनएचपीसी की लोकटक जलविद्युत परियोजना, जो 1983 में चालू हुई, लोकटक झील से सुरंग के ज़रिए लेइमाताक के बिजलीघर तक मोड़े गए पानी का उपयोग करती है, और इथाई के बैराज ने झील के जलस्तर और उसकी फुमदियों के जीवन को बदल दिया। अधिकांश बिजली क्षेत्रीय ग्रिड के माध्यम से पूर्वोत्तर के केंद्रीय बिजलीघरों से आती है, और सौर ऊर्जा और प्रीपेड स्मार्ट मीटरों का विस्तार हो रहा है।",
        "मणिपूर स्वतःची फार थोडी वीज निर्माण करते. एनएचपीसीचा लोकटक जलविद्युत प्रकल्प, 1983 मध्ये कार्यान्वित, लोकटक सरोवरातून बोगद्याने लेइमाताक येथील वीजघरापर्यंत वळवलेले पाणी वापरतो, आणि इथाई येथील बंधाऱ्याने सरोवराची पाणीपातळी व फुमदींचे जीवन बदलले. बहुतांश वीज प्रादेशिक ग्रिडद्वारे ईशान्येतील केंद्रीय वीजकेंद्रांतून येते, आणि सौरऊर्जा व प्रीपेड स्मार्ट मीटरांचा विस्तार होत आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity and peak demand", "स्थापित क्षमता और अधिकतम माँग", "स्थापित क्षमता व कमाल मागणी"), "cea", "CEA installed capacity report / load generation balance report."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Mobile and broadband networks cover Imphal and most district headquarters, but connectivity in hill villages is patchy. Mobile internet was suspended across the State for long periods after May 2023 under government orders, affecting business, banking and education. IIIT Manipur, NIT Manipur and Manipur University train students in computing and electronics.",
        "मोबाइल और ब्रॉडबैंड नेटवर्क इंफाल और अधिकांश ज़िला मुख्यालयों को कवर करते हैं, पर पहाड़ी गाँवों में संपर्क कमज़ोर है। मई 2023 के बाद सरकारी आदेशों के तहत लंबे समय तक पूरे राज्य में मोबाइल इंटरनेट बंद रहा, जिससे व्यापार, बैंकिंग और शिक्षा प्रभावित हुए। आईआईआईटी मणिपुर, एनआईटी मणिपुर और मणिपुर विश्वविद्यालय कंप्यूटिंग और इलेक्ट्रॉनिक्स में छात्रों को प्रशिक्षित करते हैं।",
        "मोबाइल व ब्रॉडबँड जाळे इंफाळ व बहुतेक जिल्हा मुख्यालयांना व्यापते, पण डोंगरी गावांत संपर्क कमकुवत आहे. मे 2023 नंतर सरकारी आदेशांनुसार दीर्घ काळ संपूर्ण राज्यात मोबाइल इंटरनेट बंद होते, ज्याचा व्यापार, बँकिंग व शिक्षणावर परिणाम झाला. आयआयआयटी मणिपूर, एनआयटी मणिपूर व मणिपूर विद्यापीठ संगणन व इलेक्ट्रॉनिक्सचे शिक्षण देतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (North East circle)."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("MN", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["MN"]
ger = AP["aishe_ger"]["MN"]; nu = AP["aishe_universities_2021_22"]["MN"]; nc = AP["aishe_colleges_2021_22"]["MN"]
module(R, "education", [
    prose("p1", L(
        f"Literacy in Manipur was 76.9% at the 2011 Census. The higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE, well above the national 28.4%, with women ({gf}%) and men ({gm}%) at similar levels. The State had {nu} universities and {inr(nc)} colleges.\n\nManipur University at Canchipur is a central university; Imphal also has NIT Manipur, IIIT Manipur, the Central Agricultural University, the National Sports University (2018), Dhanamanjuri University and two medical colleges, RIMS and JNIMS. Schools and colleges were disrupted by the violence from 2023, and many displaced students had to change schools.",
        f"2011 की जनगणना में मणिपुर की साक्षरता 76.9% थी। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था, जो राष्ट्रीय 28.4% से काफ़ी अधिक है, और महिलाएँ ({gf}%) और पुरुष ({gm}%) लगभग बराबर स्तर पर थे। राज्य में {nu} विश्वविद्यालय और {inr(nc)} कॉलेज थे।\n\nकांचीपुर का मणिपुर विश्वविद्यालय केंद्रीय विश्वविद्यालय है; इंफाल में एनआईटी मणिपुर, आईआईआईटी मणिपुर, केंद्रीय कृषि विश्वविद्यालय, राष्ट्रीय खेल विश्वविद्यालय (2018), धनमंजुरी विश्वविद्यालय और दो मेडिकल कॉलेज, रिम्स और जेएनआईएमएस, भी हैं। 2023 से हिंसा के कारण स्कूल और कॉलेज बाधित हुए, और बहुत से विस्थापित छात्रों को स्कूल बदलने पड़े।",
        f"2011 च्या जनगणनेत मणिपूरची साक्षरता 76.9% होती. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा बरेच अधिक, आणि स्त्रिया ({gf}%) व पुरुष ({gm}%) जवळपास समान पातळीवर होते. राज्यात {nu} विद्यापीठे व {inr(nc)} महाविद्यालये होती.\n\nकांचीपूर येथील मणिपूर विद्यापीठ हे केंद्रीय विद्यापीठ आहे; इंफाळमध्ये एनआयटी मणिपूर, आयआयआयटी मणिपूर, केंद्रीय कृषी विद्यापीठ, राष्ट्रीय क्रीडा विद्यापीठ (2018), धनमंजुरी विद्यापीठ आणि रिम्स व जेएनआयएमएस ही दोन वैद्यकीय महाविद्यालयेही आहेत. 2023 पासूनच्या हिंसाचारामुळे शाळा व महाविद्यालये विस्कळीत झाली, आणि अनेक विस्थापित विद्यार्थ्यांना शाळा बदलाव्या लागल्या."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("mu", "Manipur University", "मणिपुर विश्वविद्यालय", "मणिपूर विद्यापीठ", m=("Central university, Canchipur", "केंद्रीय विश्वविद्यालय, कांचीपुर", "केंद्रीय विद्यापीठ, कांचीपूर")),
        it3("nsu", "National Sports University", "राष्ट्रीय खेल विश्वविद्यालय", "राष्ट्रीय क्रीडा विद्यापीठ", m=("Imphal, 2018", "इंफाल, 2018", "इंफाळ, 2018")),
        it3("cau", "Central Agricultural University", "केंद्रीय कृषि विश्वविद्यालय", "केंद्रीय कृषी विद्यापीठ", m=("Imphal", "इंफाल", "इंफाळ")),
        it3("nitm", "NIT Manipur", "एनआईटी मणिपुर", "एनआयटी मणिपूर", m=("Langol", "लांगोल", "लांगोल")),
        it3("rims", "Regional Institute of Medical Sciences (RIMS)", "क्षेत्रीय आयुर्विज्ञान संस्थान (रिम्स)", "प्रादेशिक वैद्यकशास्त्र संस्था (रिम्स)", m=("Imphal", "इंफाल", "इंफाळ")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Displaced students — official count", "विस्थापित छात्र — आधिकारिक संख्या", "विस्थापित विद्यार्थी — अधिकृत संख्या"), "india-gov", "Government of Manipur Education Department."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["MN"]; s = C["srs"]["MN"]
module(R, "health", [
    prose("p1", L(
        f"Manipur's infant mortality rate was {s[5]:.0f} per 1,000 live births in 2020 in the Sample Registration System, down from {s[4]} in 2010 and far below the national 28, although small States have large sampling errors. The birth rate was {s[1]} and the death rate {s[3]} per 1,000. In NFHS-5, {n['institutional_N5']:.1f}% of births took place in health facilities; {n['stunted'][1]:.1f}% of children under five were stunted, down from {n['stunted'][0]}% in NFHS-4, but wasting rose from {n['wasted'][0]}% to {n['wasted'][1]:.1f}%, and {n['underweight'][1]:.1f}% were underweight.\n\nRIMS and JNIMS in Imphal are the main referral hospitals, with district hospitals elsewhere. Hill districts have fewer facilities, and since 2023 many displaced people have depended on health camps in relief centres.",
        f"नमूना पंजीकरण प्रणाली में 2020 में मणिपुर की शिशु मृत्यु दर प्रति 1,000 जीवित जन्म पर {s[5]:.0f} थी, जो 2010 के {s[4]} से कम और राष्ट्रीय 28 से बहुत नीचे है, हालाँकि छोटे राज्यों में नमूना त्रुटियाँ बड़ी होती हैं। जन्म दर प्रति 1,000 पर {s[1]} और मृत्यु दर {s[3]} थी। एनएफ़एचएस-5 में {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए; पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने थे, जो एनएफ़एचएस-4 के {n['stunted'][0]}% से कम है, पर दुबलापन {n['wasted'][0]}% से बढ़कर {n['wasted'][1]:.1f}% हो गया, और {n['underweight'][1]:.1f}% कम वज़न के थे।\n\nइंफाल के रिम्स और जेएनआईएमएस मुख्य रेफ़रल अस्पताल हैं, और अन्य जगहों पर ज़िला अस्पताल हैं। पहाड़ी ज़िलों में सुविधाएँ कम हैं, और 2023 से बहुत से विस्थापित लोग राहत शिविरों में स्वास्थ्य शिविरों पर निर्भर रहे हैं।",
        f"नमुना नोंदणी पद्धतीनुसार 2020 मध्ये मणिपूरचा अर्भक मृत्युदर दर 1,000 जिवंत जन्मांमागे {s[5]:.0f} होता, 2010 मधील {s[4]} वरून कमी व राष्ट्रीय 28 पेक्षा खूप कमी, मात्र लहान राज्यांत नमुना त्रुटी मोठ्या असतात. जन्मदर दर 1,000 मागे {s[1]} व मृत्युदर {s[3]} होता. एनएफएचएस-5 मध्ये {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या; पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी होती, एनएफएचएस-4 मधील {n['stunted'][0]}% वरून कमी, पण कृशता {n['wasted'][0]}% वरून वाढून {n['wasted'][1]:.1f}% झाली, आणि {n['underweight'][1]:.1f}% कमी वजनाची होती.\n\nइंफाळमधील रिम्स व जेएनआयएमएस ही मुख्य संदर्भ रुग्णालये आहेत, आणि इतरत्र जिल्हा रुग्णालये आहेत. डोंगरी जिल्ह्यांत सुविधा कमी आहेत, आणि 2023 पासून अनेक विस्थापित लोक मदत छावण्यांतील आरोग्य शिबिरांवर अवलंबून राहिले आहेत."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2. Small States have larger sampling errors."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("MN"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"), "srs", "Manipur is not in the SRS abridged life table for major States used here."),
        (L("Hospital beds and doctors per lakh population", "प्रति लाख जनसंख्या अस्पताल बिस्तर और डॉक्टर", "दर लाख लोकसंख्येमागे रुग्णालय खाटा व डॉक्टर"), "mohfw", "Rural Health Statistics / National Health Profile."),
    ]),
])
print("mn mod2 ok")
