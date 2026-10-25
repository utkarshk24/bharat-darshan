"""Nagaland modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-NL"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
E = research("econ_nl.json")
C = research("census_b5plus.json")
NAME = L("Nagaland", "नागालैंड", "नागालँड")
nl = read("regions/IN-NL.json")["metrics"]
ES_NOTE = "Nagaland Economic Survey 2025-26, as reported by The Morung Express (9 March 2026). MoSPI's state series has no Nagaland figures."


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Naga culture is rooted in the village and the clan. The morung, a dormitory where young men (and in some tribes young women) learned crafts, songs, history and warfare, was the centre of village life, and log drums carved from single tree trunks still stand in many villages. Each tribe has its own shawl patterns, which once showed a person's status and deeds; the Chakhesang shawl is a registered GI. Wood carving, cane and bamboo work, beadwork and pottery are traditional crafts. Christianity, brought by missionaries from the 19th century, shapes much of modern life, and church choirs and gospel music are popular alongside folk songs and dances.",
        "नागा संस्कृति गाँव और कुल में निहित है। मोरुंग, एक छात्रावास जहाँ युवक (और कुछ जनजातियों में युवतियाँ) शिल्प, गीत, इतिहास और युद्धकला सीखते थे, गाँव के जीवन का केंद्र था, और एक ही पेड़ के तने से तराशे गए लकड़ी के ढोल आज भी कई गाँवों में खड़े हैं। हर जनजाति के अपने शॉल के नमूने हैं, जो कभी व्यक्ति की प्रतिष्ठा और कर्म दर्शाते थे; चाखेसांग शॉल पंजीकृत जीआई है। लकड़ी की नक्काशी, बेंत और बाँस का काम, मनके का काम और मिट्टी के बर्तन पारंपरिक शिल्प हैं। 19वीं सदी से मिशनरियों द्वारा लाया गया ईसाई धर्म आधुनिक जीवन के बड़े भाग को आकार देता है, और लोकगीतों और नृत्यों के साथ चर्च गायक मंडलियाँ और गॉस्पेल संगीत लोकप्रिय हैं।",
        "नागा संस्कृती गाव व कुळात रुजलेली आहे. मोरुंग, एक वसतिगृह जिथे तरुण (व काही जमातींत तरुणी) हस्तकला, गीते, इतिहास व युद्धकला शिकत, हे गावजीवनाचे केंद्र होते, आणि एकाच झाडाच्या खोडातून कोरलेले लाकडी ढोल आजही अनेक गावांत उभे आहेत. प्रत्येक जमातीची स्वतःची शाल-नक्षी आहे, जी एकेकाळी व्यक्तीचा दर्जा व पराक्रम दाखवत असे; चाखेसांग शाल नोंदणीकृत जीआय आहे. लाकडी कोरीवकाम, वेत व बांबूकाम, मण्यांचे काम व मातीची भांडी या पारंपरिक कला आहेत. एकोणिसाव्या शतकापासून मिशनऱ्यांनी आणलेला ख्रिस्ती धर्म आधुनिक जीवनाचा मोठा भाग घडवतो, आणि लोकगीते व नृत्यांबरोबर चर्च गायक वृंद व गॉस्पेल संगीत लोकप्रिय आहेत."),
        conf="Editorial"),
    lst("festivals", [
        fest("hornbill", "Hornbill Festival", "हॉर्नबिल महोत्सव", "हॉर्नबिल महोत्सव", ("1–10 December", "1–10 दिसंबर", "1–10 डिसेंबर"),
             ("All the Naga tribes at Kisama Heritage Village near Kohima.", "कोहिमा के पास किसामा धरोहर गाँव में सभी नागा जनजातियाँ।", "कोहिमाजवळील किसामा वारसा गावात सर्व नागा जमाती.")),
        fest("sekrenyi", "Sekrenyi", "सेक्रेन्यी", "सेक्रेन्यी", ("February", "फ़रवरी", "फेब्रुवारी"),
             ("Angami festival of purification.", "अंगामी शुद्धि त्योहार।", "अंगामी शुद्धीकरणाचा सण.")),
        fest("aoleang", "Aoleang", "आओलियांग", "आओलेआंग", ("April", "अप्रैल", "एप्रिल"),
             ("Konyak spring and new-year festival in Mon.", "मोन में कोन्याक वसंत और नव वर्ष त्योहार।", "मोनमधील कोन्याक वसंत व नववर्ष सण.")),
        fest("moatsu", "Moatsu", "मोआत्सु", "मोआत्सु", ("May", "मई", "मे"),
             ("Ao festival after sowing.", "बुवाई के बाद आओ त्योहार।", "पेरणीनंतरचा आओ सण.")),
        fest("tuluni", "Tuluni", "तुलुनी", "तुलुनी", ("July", "जुलाई", "जुलै"),
             ("Sumi mid-year festival of feasting.", "सुमी मध्य-वर्ष भोज त्योहार।", "सुमींचा मध्यवर्षीय मेजवानीचा सण.")),
        fest("tokhuemong", "Tokhu Emong", "तोखु एमोंग", "तोखु एमोंग", ("November", "नवंबर", "नोव्हेंबर"),
             ("Lotha post-harvest festival.", "लोथा फ़सल-पश्चात त्योहार।", "लोथांचा सुगीनंतरचा सण.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("shawl", "Tribal shawls", "जनजातीय शॉल", "आदिवासी शाली"), it3("logdrum", "Log drums", "लकड़ी के ढोल", "लाकडी ढोल"),
        it3("woodcarving", "Wood carving", "लकड़ी की नक्काशी", "लाकडी कोरीवकाम"), it3("beads", "Beadwork", "मनके का काम", "मण्यांचे काम"),
        it3("cane", "Cane and bamboo", "बेंत और बाँस", "वेत व बांबू"), it3("choir", "Choirs and folk song", "गायक मंडलियाँ और लोकगीत", "गायक वृंद व लोकगीते"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("pork", "Smoked pork with bamboo shoot", "बाँस की कोंपल के साथ धुएँ में पका पोर्क", "बांबूच्या कोंबांसह धुरी दिलेले डुकराचे मांस", d=("The signature Naga dish.", "नागा पहचान वाला व्यंजन।", "नागा ओळखीचा पदार्थ.")),
        it3("axone", "Axone (akhuni)", "अखुनी (अक्सोन)", "अखुनी (अक्सोन)", d=("Fermented soya bean with a strong aroma.", "तेज़ गंध वाला किण्वित सोयाबीन।", "तीव्र गंधाचे आंबवलेले सोयाबीन.")),
        it3("mircha", "Naga mircha (king chilli)", "नागा मिर्च (राजा मिर्च)", "नागा मिरची (राजा मिरची)", d=("Among the hottest chillies; a registered GI since 2008.", "सबसे तीखी मिर्चों में; 2008 से पंजीकृत जीआई।", "सर्वांत तिखट मिरच्यांपैकी; 2008 पासून नोंदणीकृत जीआय.")),
        it3("galho", "Galho", "गाल्हो", "गाल्हो", d=("Rice porridge with vegetables and meat.", "सब्ज़ियों और मांस के साथ चावल का दलिया।", "भाज्या व मांसासह भाताची लापशी.")),
        it3("zutho", "Zutho", "ज़ूथो", "झूथो", d=("Traditional rice beer.", "पारंपरिक चावल की बियर।", "पारंपरिक तांदळाचे मद्य.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("shawl", "Warrior shawls", "योद्धा शॉल", "योद्धा शाली", d=("Patterns earned through deeds, such as the Angami and Ao warrior shawls.", "कर्मों से अर्जित नमूने, जैसे अंगामी और आओ योद्धा शॉल।", "पराक्रमाने मिळणारी नक्षी, जसे अंगामी व आओ योद्धा शाली.")),
        it3("mekhala", "Mekhala", "मेखला", "मेखला", d=("Women's wrap-around skirt woven in tribal colours.", "जनजातीय रंगों में बुनी महिलाओं की लपेटदार स्कर्ट।", "आदिवासी रंगांत विणलेला स्त्रियांचा गुंडाळ स्कर्ट.")),
        it3("headgear", "Feathered headgear", "पंखों वाला शिरोभूषण", "पिसांचे शिरोभूषण", d=("Worn at festivals by Konyak and other warriors.", "त्योहारों पर कोन्याक और अन्य योद्धाओं द्वारा पहना जाता है।", "सणांना कोन्याक व इतर योद्धे घालतात.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
g = E["gsdp_current"]; k = E["gsdp_constant"]; sh = E["sector_shares_2025_26"]; gr = E["growth_2025_26"]
ur = AP["plfs_ur_15plus_psss"]["NL"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["NL"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Nagaland's GSDP at current prices was about ₹{inr(g['FY2025-26'])} crore in FY2025-26 (advance estimate), {gr['nominal']}% higher than the previous year and {gr['real']}% higher in real terms, according to the Nagaland Economic Survey 2025-26; per capita income was ₹{inr(E['per_capita_income']['FY2025-26'])}. Services made up about {sh['tertiary']:.0f}% of the economy — much of it government administration, education, trade and transport — agriculture and allied activities about {sh['primary']:.0f}% and industry about {sh['secondary']:.0f}%. Most rural families grow rice on terraces or jhum (shifting cultivation) fields, along with maize, millets, vegetables, the Naga king chilli and fruit; pigs and mithun are reared widely. The State depends heavily on transfers from the Union government.\n\nThe PLFS unemployment rate was {ur['2025']}% in 2025 (it was {ur['2024']}% in 2024), above the national {ui['2025']}%, while labour-force participation was high: {lf['person']}% of people aged 15 and above and {lf['female']}% of women, against {lfi['female']}% of women nationally.",
        f"नागालैंड आर्थिक सर्वेक्षण 2025-26 के अनुसार वित्त वर्ष 2025-26 (अग्रिम अनुमान) में नागालैंड का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{inr(g['FY2025-26'])} करोड़ था, जो पिछले वर्ष से {gr['nominal']}% और वास्तविक रूप से {gr['real']}% अधिक है; प्रति व्यक्ति आय ₹{inr(E['per_capita_income']['FY2025-26'])} थी। अर्थव्यवस्था में सेवाओं का हिस्सा लगभग {sh['tertiary']:.0f}% था — इसका बड़ा भाग सरकारी प्रशासन, शिक्षा, व्यापार और परिवहन — कृषि और संबद्ध गतिविधियों का लगभग {sh['primary']:.0f}% और उद्योग का लगभग {sh['secondary']:.0f}%। अधिकांश ग्रामीण परिवार सीढ़ीदार या झूम (स्थानांतरित खेती) खेतों में धान उगाते हैं, साथ में मक्का, मोटे अनाज, सब्ज़ियाँ, नागा राजा मिर्च और फल; सूअर और मिथुन व्यापक रूप से पाले जाते हैं। राज्य केंद्र सरकार से मिलने वाले अंतरण पर बहुत निर्भर है।\n\nपीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी (2024 में {ur['2024']}%), जो राष्ट्रीय {ui['2025']}% से अधिक है, जबकि श्रम बल भागीदारी ऊँची थी: 15 वर्ष से अधिक आयु के {lf['person']}% लोग और {lf['female']}% महिलाएँ, जबकि राष्ट्रीय स्तर पर {lfi['female']}% महिलाएँ।",
        f"नागालँड आर्थिक पाहणी 2025-26 नुसार आ.व. 2025-26 (आगाऊ अंदाज) मध्ये नागालँडचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{inr(g['FY2025-26'])} कोटी होते, मागील वर्षापेक्षा {gr['nominal']}% आणि प्रत्यक्ष मूल्यात {gr['real']}% अधिक; दरडोई उत्पन्न ₹{inr(E['per_capita_income']['FY2025-26'])} होते. अर्थव्यवस्थेत सेवांचा वाटा सुमारे {sh['tertiary']:.0f}% होता — त्यातील मोठा भाग सरकारी प्रशासन, शिक्षण, व्यापार व वाहतूक — शेती व संलग्न उपक्रमांचा सुमारे {sh['primary']:.0f}% आणि उद्योगाचा सुमारे {sh['secondary']:.0f}%. बहुतेक ग्रामीण कुटुंबे पायऱ्यांच्या किंवा झूम (स्थलांतरित शेती) शेतांत भात घेतात, सोबत मका, भरडधान्ये, भाज्या, नागा राजा मिरची व फळे; डुकरे व मिथुन मोठ्या प्रमाणावर पाळले जातात. राज्य केंद्र सरकारकडून मिळणाऱ्या निधीवर मोठ्या प्रमाणात अवलंबून आहे.\n\nपीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता (2024 मध्ये {ur['2024']}%), राष्ट्रीय {ui['2025']}% पेक्षा जास्त, तर श्रमशक्ती सहभाग उच्च होता: 15 वर्षांवरील {lf['person']}% लोक व {lf['female']}% स्त्रिया, तर राष्ट्रीय पातळीवर {lfi['female']}% स्त्रिया."),
        sources=["morung-express", "plfs"], conf="Third-party verified"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"), nl["gsdpCurrent"], "rupeeCrore", "higher-is-better",
             previous=dp(g["FY2024-25"], "₹ crore", "FY2024-25", "fy", "morung-express", E["url"], rev="provisional", base=CUR, conf="Third-party verified", note=ES_NOTE + " Provisional estimate.")),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(k["FY2025-26"], "₹ crore", "FY2025-26", "fy", "morung-express", E["url"], rev="provisional", base=CON, conf="Third-party verified", note=ES_NOTE + " Advance estimate."), "rupeeCrore", "higher-is-better",
             previous=dp(k["FY2024-25"], "₹ crore", "FY2024-25", "fy", "morung-express", E["url"], rev="provisional", base=CON, conf="Third-party verified", note=ES_NOTE)),
        fact("pc", L("Per capita income, current prices", "प्रति व्यक्ति आय, प्रचलित मूल्य", "दरडोई उत्पन्न, चालू किमती"), nl["perCapitaNsdpCurrent"], "rupee", "higher-is-better"),
        *plfs_facts("NL", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    table("sectors", L("Sectoral shares of GSDP, FY2025-26 (current prices)", "जीएसडीपी में क्षेत्रवार हिस्सा, वित्त वर्ष 2025-26 (प्रचलित मूल्य)", "जीएसडीपीमधील क्षेत्रनिहाय वाटा, आ.व. 2025-26 (चालू किमती)"),
          [col(L("Sector", "क्षेत्र", "क्षेत्र")), col(L("Share (%)", "हिस्सा (%)", "वाटा (%)"), "right")],
          [[L("Primary (agriculture and allied)", "प्राथमिक (कृषि और संबद्ध)", "प्राथमिक (शेती व संलग्न)"), sh["primary"]],
           [L("Secondary (industry)", "द्वितीयक (उद्योग)", "द्वितीयक (उद्योग)"), sh["secondary"]],
           [L("Tertiary (services)", "तृतीयक (सेवाएँ)", "तृतीयक (सेवा)"), sh["tertiary"]]],
          "morung-express", E["url"], period="FY2025-26", conf="Third-party verified",
          note=L("Nagaland Economic Survey 2025-26 (advance estimates), as reported by The Morung Express.", "नागालैंड आर्थिक सर्वेक्षण 2025-26 (अग्रिम अनुमान), द मोरुंग एक्सप्रेस के अनुसार।", "नागालँड आर्थिक पाहणी 2025-26 (आगाऊ अंदाज), द मोरुंग एक्सप्रेसनुसार.")),
    plfs_series("NL", NAME),
    lst("sectors-key", [
        it3("agri", "Rice, maize and millets", "धान, मक्का और मोटे अनाज", "भात, मका व भरडधान्ये", d=("Terraced and jhum cultivation.", "सीढ़ीदार और झूम खेती।", "पायऱ्यांची व झूम शेती.")),
        it3("horti", "Horticulture and spices", "बाग़वानी और मसाले", "फलोत्पादन व मसाले", d=("King chilli, ginger, pineapple, passion fruit, tree tomato.", "राजा मिर्च, अदरक, अनानास, पैशन फ़्रूट, ट्री टमाटर।", "राजा मिरची, आले, अननस, पॅशन फ्रूट, झाड-टोमॅटो.")),
        it3("livestock", "Pig and mithun rearing", "सूअर और मिथुन पालन", "डुक्कर व मिथुन पालन", d=("Central to rural incomes and feasts.", "ग्रामीण आय और भोज के केंद्र में।", "ग्रामीण उत्पन्न व मेजवान्यांच्या केंद्रस्थानी.")),
        it3("bamboo", "Bamboo", "बाँस", "बांबू", d=("Construction, crafts and food.", "निर्माण, शिल्प और भोजन।", "बांधकाम, हस्तकला व अन्न.")),
        it3("tourism", "Tourism", "पर्यटन", "पर्यटन", d=("Hornbill Festival, Kohima, Dzükou and village tourism.", "हॉर्नबिल महोत्सव, कोहिमा, ज़ुकू और ग्राम पर्यटन।", "हॉर्नबिल महोत्सव, कोहिमा, झुकू व ग्रामपर्यटन.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("GSDP series — official DES Nagaland or MoSPI", "जीएसडीपी शृंखला — आधिकारिक डीईएस नागालैंड या मोस्पी", "जीएसडीपी मालिका — अधिकृत डीईएस नागालँड किंवा मोस्पी"), "mospi", "Replace the news report with the Nagaland Economic Survey PDF or the DES Nagaland GSDP tables."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Nagaland has a unicameral legislature, the 60-member Legislative Assembly at Kohima, and elects 1 member to the Lok Sabha and 1 to the Rajya Sabha. Article 371A of the Constitution provides that no Act of Parliament on Naga religious or social practices, customary law and procedure, or ownership and transfer of land and its resources applies to the State unless the Assembly so decides. Village councils and customary courts handle many local matters, and an Inner Line Permit is required for visitors from other States.\n\nAfter the 2023 Assembly election Neiphiu Rio was sworn in as Chief Minister for a fifth term on 7 March 2023, with T. R. Zeliang and Y. Patton as Deputy Chief Ministers. His party, the NDPP, merged with the Naga People's Front in October 2025. Sharingain Longkumer has been Speaker since 2020 and was re-elected in March 2023, and Nand Kishore Yadav has been Governor since 13 March 2026. The next Assembly election is due by early 2028.",
        "नागालैंड में एकसदनीय विधानमंडल है, कोहिमा में 60 सदस्यों वाली विधानसभा, और राज्य से लोकसभा का 1 और राज्यसभा का 1 सदस्य चुना जाता है। संविधान का अनुच्छेद 371क प्रावधान करता है कि नागा धार्मिक या सामाजिक प्रथाओं, पारंपरिक क़ानून और प्रक्रिया, या भूमि और उसके संसाधनों के स्वामित्व और हस्तांतरण पर संसद का कोई अधिनियम राज्य पर तब तक लागू नहीं होता जब तक विधानसभा ऐसा तय न करे। ग्राम परिषदें और पारंपरिक न्यायालय कई स्थानीय मामले देखते हैं, और अन्य राज्यों से आने वालों को इनर लाइन परमिट चाहिए।\n\n2023 के विधानसभा चुनाव के बाद नेफ़्यू रियो ने 7 मार्च 2023 को पाँचवें कार्यकाल के लिए मुख्यमंत्री पद की शपथ ली, टी. आर. ज़ेलियांग और वाई. पैटन उपमुख्यमंत्री बने। उनकी पार्टी एनडीपीपी का अक्टूबर 2025 में नागा पीपुल्स फ़्रंट में विलय हुआ। शरिंगेन लोंगकुमेर 2020 से अध्यक्ष हैं और मार्च 2023 में फिर चुने गए, और नंद किशोर यादव 13 मार्च 2026 से राज्यपाल हैं। अगला विधानसभा चुनाव 2028 की शुरुआत तक होना है।",
        "नागालँडमध्ये एकसदनी विधिमंडळ आहे, कोहिमा येथील 60 सदस्यांची विधानसभा, आणि राज्यातून लोकसभेवर 1 व राज्यसभेवर 1 सदस्य निवडला जातो. संविधानाचा अनुच्छेद 371क अशी तरतूद करतो की नागा धार्मिक किंवा सामाजिक प्रथा, पारंपरिक कायदा व प्रक्रिया, किंवा जमीन व तिच्या संसाधनांची मालकी आणि हस्तांतरण यांबाबतचा संसदेचा कोणताही कायदा विधानसभेने ठरवल्याशिवाय राज्याला लागू होत नाही. ग्रामपरिषदा व पारंपरिक न्यायालये अनेक स्थानिक प्रकरणे हाताळतात, आणि इतर राज्यांतून येणाऱ्यांना इनर लाइन परवाना लागतो.\n\n2023 च्या विधानसभा निवडणुकीनंतर नेफ्यू रियो यांनी 7 मार्च 2023 रोजी पाचव्या कारकिर्दीसाठी मुख्यमंत्रिपदाची शपथ घेतली, टी. आर. झेलियांग व वाय. पॅटन उपमुख्यमंत्री झाले. त्यांच्या एनडीपीपी पक्षाचे ऑक्टोबर 2025 मध्ये नागा पीपल्स फ्रंटमध्ये विलीनीकरण झाले. शरिंगेन लोंगकुमेर 2020 पासून अध्यक्ष आहेत व मार्च 2023 मध्ये पुन्हा निवडले गेले, आणि नंदकिशोर यादव 13 मार्च 2026 पासून राज्यपाल आहेत. पुढील विधानसभा निवडणूक 2028 च्या सुरुवातीपर्यंत होणे अपेक्षित आहे."),
        sources=["tribune", "newsonair", "eastmojo"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("portal", "Government of Nagaland", "नागालैंड सरकार", "नागालँड शासन", url="https://www.nagaland.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2023 Assembly election — party-wise result", "2023 विधानसभा चुनाव — दलवार परिणाम", "2023 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Nagaland 2023."),
        (L("Chief Minister's swearing-in — official source", "मुख्यमंत्री का शपथ ग्रहण — आधिकारिक स्रोत", "मुख्यमंत्र्यांचा शपथविधी — अधिकृत स्रोत"), "india-gov", "Replace the news report with the Nagaland IPR release of 7 March 2023."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "The railway from Dimapur to Kohima is the State's largest project, with its first two sections already open. Other works include four-laning of the Dimapur–Kohima highway, the Foothill Road along the Assam border, and new medical and engineering colleges; these will be added as cards once their status is confirmed from official sources. Each card shows its source and the date it was checked.",
        "दीमापुर से कोहिमा तक रेलवे राज्य की सबसे बड़ी परियोजना है, जिसके पहले दो खंड खुल चुके हैं। अन्य कार्यों में दीमापुर–कोहिमा राजमार्ग को चार-लेन करना, असम सीमा के साथ फ़ुटहिल रोड, और नए मेडिकल व इंजीनियरिंग कॉलेज शामिल हैं; आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर इन्हें कार्ड के रूप में जोड़ा जाएगा। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "दिमापूर ते कोहिमा रेल्वे हा राज्यातील सर्वांत मोठा प्रकल्प आहे, ज्याचे पहिले दोन टप्पे आधीच सुरू झाले आहेत. इतर कामांत दिमापूर–कोहिमा महामार्गाचे चौपदरीकरण, आसाम सीमेलगतचा फूटहिल रस्ता, आणि नवी वैद्यकीय व अभियांत्रिकी महाविद्यालये यांचा समावेश आहे; अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर त्यांची कार्डे जोडली जातील. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["morung-express"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Dimapur–Kohima line — sanctioned cost and official progress", "दीमापुर–कोहिमा लाइन — स्वीकृत लागत और आधिकारिक प्रगति", "दिमापूर–कोहिमा मार्ग — मंजूर खर्च व अधिकृत प्रगती"), "railways", "Ministry of Railways / NFR release; replace the news report."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Dimapur is Nagaland's gateway: it has the State's only airport and its main railway station, on the line between Guwahati and Dibrugarh. National Highway 29 climbs from Dimapur to Kohima and continues to Imphal in Manipur, and other highways link Mokokchung, Wokha, Zunheboto, Tuensang and Mon. Roads are narrow and often damaged by landslides in the monsoon. The new Dhansiri–Zubza line will bring the railway close to Kohima. Visitors from other States need an Inner Line Permit, which can be obtained online.",
        "दीमापुर नागालैंड का प्रवेश द्वार है: यहाँ राज्य का एकमात्र हवाई अड्डा और गुवाहाटी–डिब्रूगढ़ लाइन पर मुख्य रेलवे स्टेशन है। राष्ट्रीय राजमार्ग 29 दीमापुर से कोहिमा चढ़ता है और मणिपुर के इंफाल तक जाता है, और अन्य राजमार्ग मोकोकचुंग, वोखा, ज़ुन्हेबोटो, त्वेनसांग और मोन को जोड़ते हैं। सड़कें संकरी हैं और मानसून में अक्सर भूस्खलन से क्षतिग्रस्त होती हैं। नई धनसिरी–ज़ुबज़ा लाइन रेलवे को कोहिमा के पास लाएगी। अन्य राज्यों से आने वालों को इनर लाइन परमिट चाहिए, जो ऑनलाइन मिल सकता है।",
        "दिमापूर हे नागालँडचे प्रवेशद्वार आहे: येथे राज्याचा एकमेव विमानतळ व गुवाहाटी–दिब्रुगड मार्गावरील मुख्य रेल्वे स्थानक आहे. राष्ट्रीय महामार्ग 29 दिमापूरहून कोहिमापर्यंत चढतो व मणिपूरच्या इंफाळपर्यंत जातो, आणि इतर महामार्ग मोकोकचुंग, वोखा, झुन्हेबोटो, त्वेनसांग व मोनला जोडतात. रस्ते अरुंद आहेत व पावसाळ्यात अनेकदा भूस्खलनाने खराब होतात. नवा धनसिरी–झुबझा मार्ग रेल्वे कोहिमाजवळ आणेल. इतर राज्यांतून येणाऱ्यांना इनर लाइन परवाना लागतो, जो ऑनलाइन मिळू शकतो."),
        conf="Editorial"),
    lst("airports", [
        it3("dmu", "Dimapur Airport", "दीमापुर हवाई अड्डा", "दिमापूर विमानतळ", m=("DMU", "DMU", "DMU")),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Inner Line Permit rules — official notice", "इनर लाइन परमिट नियम — आधिकारिक सूचना", "इनर लाइन परवाना नियम — अधिकृत सूचना"), "india-gov", "Government of Nagaland ILP portal."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Nagaland generates only a small part of the power it uses — chiefly from the Doyang hydroelectric project in Wokha district and small hydel stations — and buys the rest from central stations through the north-eastern grid. Many villages rely on small hydro and solar schemes, and the State is promoting rooftop solar. Oil exists in the foothills, but production has been suspended for decades over questions of land and resource ownership.",
        "नागालैंड अपनी ज़रूरत की बिजली का छोटा भाग ही बनाता है — मुख्यतः वोखा ज़िले की दोयांग जलविद्युत परियोजना और छोटे जलविद्युत केंद्रों से — और शेष पूर्वोत्तर ग्रिड के माध्यम से केंद्रीय केंद्रों से ख़रीदता है। कई गाँव छोटी जलविद्युत और सौर योजनाओं पर निर्भर हैं, और राज्य छतों पर सौर ऊर्जा को बढ़ावा दे रहा है। तलहटी में तेल है, पर भूमि और संसाधन स्वामित्व के प्रश्नों के कारण उत्पादन दशकों से रुका है।",
        "नागालँड आपल्या गरजेच्या विजेचा लहान भागच निर्माण करतो — मुख्यतः वोखा जिल्ह्यातील दोयांग जलविद्युत प्रकल्प व लहान जलविद्युत केंद्रांतून — आणि उर्वरित वीज ईशान्य ग्रिडमार्फत केंद्रीय केंद्रांकडून विकत घेतो. अनेक गावे लहान जलविद्युत व सौर योजनांवर अवलंबून आहेत, आणि राज्य छतांवरील सौरऊर्जेला प्रोत्साहन देत आहे. पायथ्याच्या भागात तेल आहे, पण जमीन व संसाधन मालकीच्या प्रश्नांमुळे उत्पादन दशकांपासून थांबले आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Power purchase and own generation", "बिजली ख़रीद और स्वयं उत्पादन", "वीजखरेदी व स्वनिर्मिती"), "cea", "CEA / Nagaland Department of Power."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Mobile and internet services reach the towns and most villages, though connectivity is weak in the remote eastern districts. Government services such as the online Inner Line Permit are delivered digitally, and Kohima and Dimapur have growing start-up and creative communities in music, fashion and food.",
        "मोबाइल और इंटरनेट सेवाएँ नगरों और अधिकांश गाँवों तक पहुँचती हैं, हालाँकि दूरस्थ पूर्वी ज़िलों में कनेक्टिविटी कमज़ोर है। ऑनलाइन इनर लाइन परमिट जैसी सरकारी सेवाएँ डिजिटल रूप से दी जाती हैं, और कोहिमा व दीमापुर में संगीत, फ़ैशन और भोजन में बढ़ते स्टार्टअप और रचनात्मक समुदाय हैं।",
        "मोबाइल व इंटरनेट सेवा शहरे व बहुतेक गावांपर्यंत पोहोचते, मात्र दुर्गम पूर्वेकडील जिल्ह्यांत संपर्क कमकुवत आहे. ऑनलाइन इनर लाइन परवान्यासारख्या सरकारी सेवा डिजिटल पद्धतीने दिल्या जातात, आणि कोहिमा व दिमापूरमध्ये संगीत, फॅशन व खाद्यक्षेत्रात वाढते स्टार्टअप व सर्जनशील समुदाय आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (North East circle)."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("NL", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["NL"]
ger = AP["aishe_ger"]["NL"]; nu = AP["aishe_universities_2021_22"]["NL"]; nc = AP["aishe_colleges_2021_22"]["NL"]
module(R, "education", [
    prose("p1", L(
        f"Literacy in Nagaland was 79.6% at the 2011 Census, above the national 73%. The higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE (women {gf}%, men {gm}%), and the State had {nu} universities and {inr(nc)} colleges.\n\nNagaland University, the central university, has its headquarters at Lumami and campuses at Kohima and Medziphema; NIT Nagaland is at Chümoukedima; and Kohima Science College, Patkai Christian College and the State's first medical college at Kohima are other major institutions. Church-run schools have played a large part in education since the 19th century.",
        f"2011 की जनगणना में नागालैंड की साक्षरता 79.6% थी, जो राष्ट्रीय 73% से अधिक है। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था (महिलाएँ {gf}%, पुरुष {gm}%), और राज्य में {nu} विश्वविद्यालय और {inr(nc)} कॉलेज थे।\n\nकेंद्रीय विश्वविद्यालय, नागालैंड विश्वविद्यालय का मुख्यालय लुमामी में है और परिसर कोहिमा और मेज़िफ़ेमा में हैं; एनआईटी नागालैंड चुमौकेदिमा में है; और कोहिमा साइंस कॉलेज, पटकाई क्रिश्चियन कॉलेज और कोहिमा में राज्य का पहला मेडिकल कॉलेज अन्य प्रमुख संस्थान हैं। 19वीं सदी से चर्च द्वारा चलाए जाने वाले स्कूलों ने शिक्षा में बड़ी भूमिका निभाई है।",
        f"2011 च्या जनगणनेत नागालँडची साक्षरता 79.6% होती, राष्ट्रीय 73% पेक्षा अधिक. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते (स्त्रिया {gf}%, पुरुष {gm}%), आणि राज्यात {nu} विद्यापीठे व {inr(nc)} महाविद्यालये होती.\n\nकेंद्रीय विद्यापीठ असलेल्या नागालँड विद्यापीठाचे मुख्यालय लुमामी येथे आहे व संकुले कोहिमा आणि मेझिफेमा येथे आहेत; एनआयटी नागालँड चुमौकेदिमा येथे आहे; आणि कोहिमा सायन्स कॉलेज, पटकाई ख्रिश्चन कॉलेज व कोहिमा येथील राज्याचे पहिले वैद्यकीय महाविद्यालय या इतर प्रमुख संस्था आहेत. एकोणिसाव्या शतकापासून चर्च चालवत असलेल्या शाळांनी शिक्षणात मोठी भूमिका बजावली आहे."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("nu", "Nagaland University", "नागालैंड विश्वविद्यालय", "नागालँड विद्यापीठ", m=("Central university, Lumami", "केंद्रीय विश्वविद्यालय, लुमामी", "केंद्रीय विद्यापीठ, लुमामी")),
        it3("nitn", "NIT Nagaland", "एनआईटी नागालैंड", "एनआयटी नागालँड", m=("Chümoukedima", "चुमौकेदिमा", "चुमौकेदिमा")),
        it3("ksc", "Kohima Science College", "कोहिमा साइंस कॉलेज", "कोहिमा सायन्स कॉलेज", m=("Jotsoma", "जोत्सोमा", "जोत्सोमा")),
        it3("patkai", "Patkai Christian College", "पटकाई क्रिश्चियन कॉलेज", "पटकाई ख्रिश्चन कॉलेज", m=("Chümoukedima", "चुमौकेदिमा", "चुमौकेदिमा")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Nagaland's first medical college — official name and year", "नागालैंड का पहला मेडिकल कॉलेज — आधिकारिक नाम और वर्ष", "नागालँडचे पहिले वैद्यकीय महाविद्यालय — अधिकृत नाव व वर्ष"), "india-gov", "National Medical Commission college list."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["NL"]; s = C["srs"]["NL"]
module(R, "health", [
    prose("p1", L(
        f"The Sample Registration System put Nagaland's infant mortality rate at {s[5]:.0f} per 1,000 live births in 2020, down from {s[4]} in 2010 and among the lowest in India, with a birth rate of {s[1]} and a death rate of {s[3]} per 1,000 — figures for small States have wide margins of error. Other indicators are weaker: in NFHS-5 only {n['institutional_N5']:.1f}% of births took place in health facilities, and child nutrition worsened between NFHS-4 and NFHS-5, with stunting rising from {n['stunted'][0]}% to {n['stunted'][1]:.1f}%, wasting from {n['wasted'][0]}% to {n['wasted'][1]:.1f}% and underweight from {n['underweight'][0]}% to {n['underweight'][1]:.1f}%.\n\nNaga Hospital Authority in Kohima and district hospitals provide government care, with mission and private hospitals in Kohima and Dimapur; serious cases are often referred to Guwahati.",
        f"नमूना पंजीकरण प्रणाली के अनुसार 2020 में नागालैंड की शिशु मृत्यु दर प्रति 1,000 जीवित जन्म पर {s[5]:.0f} थी, जो 2010 के {s[4]} से कम और भारत में सबसे कम में है, जन्म दर प्रति 1,000 पर {s[1]} और मृत्यु दर {s[3]} — छोटे राज्यों के आँकड़ों में त्रुटि की गुंजाइश अधिक होती है। अन्य संकेतक कमज़ोर हैं: एनएफ़एचएस-5 में केवल {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, और एनएफ़एचएस-4 और एनएफ़एचएस-5 के बीच बाल पोषण बिगड़ा, जिसमें ठिगनापन {n['stunted'][0]}% से बढ़कर {n['stunted'][1]:.1f}%, दुबलापन {n['wasted'][0]}% से {n['wasted'][1]:.1f}% और कम वज़न {n['underweight'][0]}% से {n['underweight'][1]:.1f}% हुआ।\n\nकोहिमा का नागा हॉस्पिटल अथॉरिटी और ज़िला अस्पताल सरकारी सेवा देते हैं, साथ में कोहिमा और दीमापुर में मिशन और निजी अस्पताल हैं; गंभीर मामले अक्सर गुवाहाटी भेजे जाते हैं।",
        f"नमुना नोंदणी पद्धतीनुसार 2020 मध्ये नागालँडचा अर्भक मृत्युदर दर 1,000 जिवंत जन्मांमागे {s[5]:.0f} होता, 2010 मधील {s[4]} वरून कमी आणि भारतातील सर्वांत कमींपैकी, जन्मदर दर 1,000 मागे {s[1]} व मृत्युदर {s[3]} — लहान राज्यांच्या आकड्यांत त्रुटीची शक्यता मोठी असते. इतर निर्देशक कमकुवत आहेत: एनएफएचएस-5 मध्ये केवळ {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, आणि एनएफएचएस-4 व एनएफएचएस-5 दरम्यान बालपोषण बिघडले, ज्यात खुजेपणा {n['stunted'][0]}% वरून {n['stunted'][1]:.1f}%, कृशता {n['wasted'][0]}% वरून {n['wasted'][1]:.1f}% व कमी वजन {n['underweight'][0]}% वरून {n['underweight'][1]:.1f}% झाले.\n\nकोहिमाची नागा हॉस्पिटल ऑथॉरिटी व जिल्हा रुग्णालये सरकारी सेवा देतात, सोबत कोहिमा व दिमापूरमध्ये मिशन व खासगी रुग्णालये आहेत; गंभीर रुग्ण अनेकदा गुवाहाटीला पाठवले जातात."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2. Small States have larger sampling errors."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("NL"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"), "srs", "Nagaland is not in the SRS abridged life table for major States used here."),
    ]),
])
print("nl mod2 ok")
