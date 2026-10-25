"""Arunachal Pradesh modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-AR"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_AR = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 25 Oct 2026. "
           "FY2025-26 is the latest year published for Arunachal Pradesh and may be revised.")
mo = research("mospi_ar.json")
C = research("census_b5plus.json")
NAME = L("Arunachal Pradesh", "अरुणाचल प्रदेश", "अरुणाचल प्रदेश")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Arunachal Pradesh's culture is the sum of many tribal cultures. Most communities follow indigenous faiths centred on nature, the sun and the moon — Donyi-Polo among the Adi, Galo and others, and Rangfrah among the Tangsa and Nocte — while the Monpa, Sherdukpen, Khamti and Singpho are Buddhist, and Christianity and Hinduism are also widely followed. Each festival follows the farming cycle and is celebrated with dances, priests' chants, sacrifices and rice beer (apong). Weaving is done on loin looms by women, and each tribe's textiles carry its own patterns; cane and bamboo work, wood carving (notably by the Wancho), Monpa handmade paper and thangka painting in Tawang are other crafts.",
        "अरुणाचल प्रदेश की संस्कृति कई जनजातीय संस्कृतियों का योग है। अधिकांश समुदाय प्रकृति, सूर्य और चंद्रमा पर केंद्रित देशज आस्थाओं का पालन करते हैं — आदी, गालो और अन्य में दोन्यी-पोलो, और तांगसा व नोक्टे में रंगफ़्रा — जबकि मोनपा, शेरदुकपेन, खामती और सिंगफ़ो बौद्ध हैं, और ईसाई और हिंदू धर्म भी व्यापक रूप से माने जाते हैं। हर त्योहार खेती के चक्र के अनुसार होता है और नृत्य, पुजारियों के मंत्र, बलि और चावल की बियर (आपोंग) के साथ मनाया जाता है। महिलाएँ कमर-करघे पर बुनाई करती हैं, और हर जनजाति के वस्त्रों के अपने नमूने हैं; बेंत और बाँस का काम, लकड़ी की नक्काशी (विशेषकर वांचो द्वारा), मोनपा हस्तनिर्मित काग़ज़ और तवांग में थांका चित्रकला अन्य शिल्प हैं।",
        "अरुणाचल प्रदेशची संस्कृती अनेक आदिवासी संस्कृतींची बेरीज आहे. बहुतेक समुदाय निसर्ग, सूर्य व चंद्र यांवर केंद्रित देशी श्रद्धा पाळतात — आदी, गालो व इतरांत दोन्यी-पोलो, आणि तांगसा व नोक्टेंमध्ये रंगफ्रा — तर मोनपा, शेरदुकपेन, खामती व सिंगफो बौद्ध आहेत, आणि ख्रिस्ती व हिंदू धर्मही मोठ्या प्रमाणावर पाळले जातात. प्रत्येक सण शेतीच्या चक्राप्रमाणे असतो आणि नृत्ये, पुजाऱ्यांचे मंत्र, बळी व तांदळाचे मद्य (आपोंग) यांसह साजरा होतो. स्त्रिया कंबर-मागावर विणकाम करतात, आणि प्रत्येक जमातीच्या वस्त्रांवर स्वतःची नक्षी असते; वेत व बांबूकाम, लाकडी कोरीवकाम (विशेषतः वांचोंचे), मोनपा हातकागद व तवांगमधील थांका चित्रकला या इतर कला आहेत."),
        conf="Editorial"),
    lst("festivals", [
        fest("losar", "Losar", "लोसार", "लोसार", ("February–March", "फ़रवरी–मार्च", "फेब्रुवारी–मार्च"),
             ("Monpa New Year in Tawang and West Kameng.", "तवांग और पश्चिम कामेंग में मोनपा नव वर्ष।", "तवांग व पश्चिम कामेंगमधील मोनपा नववर्ष.")),
        fest("nyokum", "Nyokum", "न्योकुम", "न्योकुम", ("February", "फ़रवरी", "फेब्रुवारी"),
             ("Nyishi festival for good harvests.", "अच्छी फ़सल के लिए न्यिशी त्योहार।", "चांगल्या पिकासाठी न्यिशी सण.")),
        fest("mopin", "Mopin", "मोपिन", "मोपिन", ("April", "अप्रैल", "एप्रिल"),
             ("Galo festival of prosperity; rice-powder blessings.", "गालो का समृद्धि का त्योहार; चावल के आटे से आशीर्वाद।", "गालोंचा समृद्धीचा सण; तांदळाच्या पिठाने आशीर्वाद.")),
        fest("dree", "Dree", "द्री", "द्री", ("July", "जुलाई", "जुलै"),
             ("Apatani agricultural festival in the Ziro valley.", "ज़ीरो घाटी में अपातानी कृषि त्योहार।", "झिरो खोऱ्यातील आपातानी कृषी सण.")),
        fest("solung", "Solung", "सोलुंग", "सोलुंग", ("September", "सितंबर", "सप्टेंबर"),
             ("Adi harvest festival with ponung dances.", "पोनुंग नृत्यों के साथ आदी फ़सल त्योहार।", "पोनुंग नृत्यांसह आदी सुगीचा सण.")),
        fest("sangken", "Sangken", "सांगकेन", "सांगकेन", ("April", "अप्रैल", "एप्रिल"),
             ("Khamti water festival, the Buddhist New Year.", "खामती जल उत्सव, बौद्ध नव वर्ष।", "खामतींचा जलोत्सव, बौद्ध नववर्ष.")),
        fest("torgya", "Torgya", "तोरग्या", "तोरग्या", ("January", "जनवरी", "जानेवारी"),
             ("Masked dances at Tawang Monastery.", "तवांग मठ में मुखौटा नृत्य।", "तवांग मठातील मुखवटा नृत्ये.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("loinloom", "Loin-loom weaving", "कमर-करघा बुनाई", "कंबर-माग विणकाम"), it3("cane", "Cane and bamboo work", "बेंत और बाँस का काम", "वेत व बांबूकाम"),
        it3("wancho", "Wancho wood carving", "वांचो काष्ठ नक्काशी", "वांचो लाकडी कोरीवकाम"), it3("paper", "Monpa handmade paper", "मोनपा हस्तनिर्मित काग़ज़", "मोनपा हातकागद"),
        it3("thangka", "Thangka painting", "थांका चित्रकला", "थांका चित्रकला"), it3("dao", "Dao (sword) making", "दाओ (तलवार) निर्माण", "दाओ (तलवार) निर्मिती"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("apong", "Apong", "आपोंग", "आपोंग", d=("Rice beer central to hospitality and rituals; Adi apong is a registered GI.", "आतिथ्य और अनुष्ठानों के केंद्र में चावल की बियर; आदी आपोंग पंजीकृत जीआई है।", "आदरातिथ्य व विधींच्या केंद्रस्थानी तांदळाचे मद्य; आदी आपोंग नोंदणीकृत जीआय आहे.")),
        it3("bambooshoot", "Bamboo shoot dishes", "बाँस की कोंपल के व्यंजन", "बांबूच्या कोंबांचे पदार्थ", d=("Fresh and fermented shoots cooked with meat or fish.", "ताज़ी और किण्वित कोंपलें मांस या मछली के साथ पकाई जाती हैं।", "ताजे व आंबवलेले कोंब मांस किंवा माशांसह शिजवले जातात.")),
        it3("pikapila", "Pika pila", "पिका पिला", "पिका पिला", d=("Apatani pickle of bamboo shoot and pork fat.", "बाँस की कोंपल और सूअर की चर्बी का अपातानी अचार।", "बांबूचे कोंब व डुकराच्या चरबीचे आपातानी लोणचे.")),
        it3("smoked", "Smoked meat and fish", "धुएँ में सुखाया मांस और मछली", "धुरी दिलेले मांस व मासे", d=("Preserved over the hearth in bamboo houses.", "बाँस के घरों में चूल्हे के ऊपर सुरक्षित किया जाता है।", "बांबूच्या घरांत चुलीवर टिकवले जाते.")),
        it3("thukpa", "Thukpa and momos", "थुकपा और मोमो", "थुकपा व मोमो", d=("Everyday food in Tawang and the Monpa areas.", "तवांग और मोनपा क्षेत्रों का रोज़ का भोजन।", "तवांग व मोनपा भागांतील रोजचे अन्न.")),
        it3("churpi", "Yak churpi", "याक छुरपी", "याक छुरपी", d=("Hard yak-milk cheese of the high valleys; a registered GI.", "ऊँची घाटियों का याक के दूध का सख़्त पनीर; पंजीकृत जीआई।", "उंच खोऱ्यांतील याकच्या दुधाचे कडक चीज; नोंदणीकृत जीआय.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("galuk", "Galuk and gale", "गालुक और गाले", "गालुक व गाले", d=("Adi and Galo men's jackets and women's wrap-around skirts.", "आदी और गालो पुरुषों की जैकेट और महिलाओं की लपेटदार स्कर्ट।", "आदी व गालो पुरुषांची जाकिटे व स्त्रियांचे गुंडाळ स्कर्ट.")),
        it3("monpa", "Monpa chuba", "मोनपा चुबा", "मोनपा चुबा", d=("Woollen robe with a cap of yak felt in Tawang.", "तवांग में याक के नमदे की टोपी के साथ ऊनी चोगा।", "तवांगमध्ये याकच्या नमद्याच्या टोपीसह लोकरी झगा.")),
        it3("nyishi", "Nyishi headgear", "न्यिशी शिरोभूषण", "न्यिशी शिरोभूषण", d=("Cane cap with hornbill-beak replicas, now made without real beaks.", "धनेश की चोंच की प्रतिकृति वाली बेंत की टोपी, अब असली चोंच के बिना।", "धनेशाच्या चोचीच्या प्रतिकृतीची वेताची टोपी, आता खऱ्या चोचीशिवाय.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; util = 100 * g["utilities"] / g["total"]; pub = 100 * g["public_admin"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["AR"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["AR"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Arunachal Pradesh's GSDP at current prices was about ₹{inr(cur['FY2025-26'][0])} crore in FY2025-26, up from ₹{inr(cur['FY2024-25'][0])} crore in FY2024-25, and per capita NSDP was ₹{inr(pc['FY2025-26'][0])} (MoSPI). In FY2024-25 agriculture, livestock and forestry made up about {agri:.0f}% of GSVA — shifting (jhum) and terraced rice cultivation, oranges, kiwi fruit, large cardamom and ginger, with forestry a large part — while public administration accounted for about {pub:.0f}% and electricity, gas and water about {util:.0f}%, reflecting new hydropower stations. Manufacturing is small. The State has a very large hydropower potential, and tourism and border-area road building are growing.\n\nThe PLFS unemployment rate was {ur['2025']}% in 2025, above the national {ui['2025']}%, but labour-force participation was high: {lf['person']}% of people aged 15 and above, and {lf['female']}% of women, against {lfi['female']}% of women nationally.",
        f"मोस्पी के अनुसार वित्त वर्ष 2025-26 में अरुणाचल प्रदेश का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{inr(cur['FY2025-26'][0])} करोड़ था, जो वित्त वर्ष 2024-25 के ₹{inr(cur['FY2024-25'][0])} करोड़ से अधिक है, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2025-26'][0])} था। वित्त वर्ष 2024-25 में जीएसवीए में कृषि, पशुपालन और वानिकी का हिस्सा लगभग {agri:.0f}% था — झूम और सीढ़ीदार धान की खेती, संतरे, कीवी, बड़ी इलायची और अदरक, जिसमें वानिकी बड़ा भाग है — जबकि लोक प्रशासन का लगभग {pub:.0f}% और बिजली, गैस व जल का लगभग {util:.0f}%, जो नए जलविद्युत केंद्रों को दर्शाता है। विनिर्माण छोटा है। राज्य में जलविद्युत की बहुत बड़ी क्षमता है, और पर्यटन व सीमावर्ती सड़क निर्माण बढ़ रहे हैं।\n\nपीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी, जो राष्ट्रीय {ui['2025']}% से अधिक है, पर श्रम बल भागीदारी ऊँची थी: 15 वर्ष से अधिक आयु के {lf['person']}% लोग, और {lf['female']}% महिलाएँ, जबकि राष्ट्रीय स्तर पर {lfi['female']}% महिलाएँ।",
        f"मोस्पीनुसार आ.व. 2025-26 मध्ये अरुणाचल प्रदेशचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{inr(cur['FY2025-26'][0])} कोटी होते, आ.व. 2024-25 मधील ₹{inr(cur['FY2024-25'][0])} कोटींवरून वाढ, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2025-26'][0])} होते. आ.व. 2024-25 मध्ये जीएसव्हीएमध्ये शेती, पशुपालन व वनीकरणाचा वाटा सुमारे {agri:.0f}% होता — झूम व पायऱ्यांची भातशेती, संत्री, किवी, मोठी वेलची व आले, ज्यात वनीकरणाचा मोठा भाग — तर लोकप्रशासनाचा सुमारे {pub:.0f}% आणि वीज, वायू व पाण्याचा सुमारे {util:.0f}%, जो नव्या जलविद्युत केंद्रांमुळे आहे. उत्पादन उद्योग लहान आहे. राज्यात जलविद्युतची फार मोठी क्षमता आहे, आणि पर्यटन व सीमाभागातील रस्तेबांधणी वाढत आहेत.\n\nपीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता, राष्ट्रीय {ui['2025']}% पेक्षा जास्त, पण श्रमशक्ती सहभाग उच्च होता: 15 वर्षांवरील {lf['person']}% लोक, आणि {lf['female']}% स्त्रिया, तर राष्ट्रीय पातळीवर {lfi['female']}% स्त्रिया."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_AR), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_AR), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_AR), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("AR", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    plfs_series("AR", NAME),
    lst("sectors-key", [
        it3("hydro", "Hydropower", "जलविद्युत", "जलविद्युत", d=("Kameng, Ranganadi, Pare and the Lower Subansiri project on the Assam border.", "कामेंग, रंगानदी, पारे और असम सीमा पर निचली सुबनसिरी परियोजना।", "कामेंग, रंगानदी, पारे व आसाम सीमेवरील खालचा सुबनसिरी प्रकल्प.")),
        it3("horti", "Horticulture", "बाग़वानी", "फलोत्पादन", d=("Oranges, kiwi, apples, pineapple and large cardamom.", "संतरे, कीवी, सेब, अनानास और बड़ी इलायची।", "संत्री, किवी, सफरचंद, अननस व मोठी वेलची.")),
        it3("forest", "Forestry", "वानिकी", "वनीकरण", d=("Timber, cane and bamboo; regulated by the Supreme Court since the 1990s.", "लकड़ी, बेंत और बाँस; 1990 के दशक से सर्वोच्च न्यायालय द्वारा विनियमित।", "लाकूड, वेत व बांबू; 1990 च्या दशकापासून सर्वोच्च न्यायालयाकडून नियंत्रित.")),
        it3("tourism", "Tourism", "पर्यटन", "पर्यटन", d=("Tawang, Ziro, Namdapha and adventure travel.", "तवांग, ज़ीरो, नामदफा और साहसिक यात्रा।", "तवांग, झिरो, नामदफा व साहसी पर्यटन.")),
        it3("oil", "Oil and coal (small)", "तेल और कोयला (छोटे)", "तेल व कोळसा (लहान)", d=("Small oil fields and coal near the Assam border in the south-east.", "दक्षिण-पूर्व में असम सीमा के पास छोटे तेल क्षेत्र और कोयला।", "आग्नेयेला आसाम सीमेजवळ लहान तेलक्षेत्रे व कोळसा.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Hydropower potential — official estimate", "जलविद्युत क्षमता — आधिकारिक अनुमान", "जलविद्युत क्षमता — अधिकृत अंदाज"), "cea", "CEA reassessment of hydro potential."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Arunachal Pradesh has a unicameral legislature, the 60-member Legislative Assembly at Itanagar, and elects 2 members to the Lok Sabha and 1 to the Rajya Sabha. Article 371H of the Constitution gives the Governor special responsibility for law and order, and traditional village councils still settle many local disputes under customary law. Visitors from other States need an Inner Line Permit under the Bengal Eastern Frontier Regulation of 1873.\n\nThe Bharatiya Janata Party won the Assembly election held with the Lok Sabha election in 2024, and Pema Khandu was sworn in as Chief Minister for a third consecutive term on 13 June 2024, with Chowna Mein as Deputy Chief Minister. Tesam Pongte was elected Speaker on 15 June 2024, and Lt Gen K. T. Parnaik (Retd) has been Governor since 16 February 2023. The next Assembly election is due by 2029.",
        "अरुणाचल प्रदेश में एकसदनीय विधानमंडल है, ईटानगर में 60 सदस्यों वाली विधानसभा, और राज्य से लोकसभा के 2 और राज्यसभा का 1 सदस्य चुना जाता है। संविधान का अनुच्छेद 371ज राज्यपाल को क़ानून-व्यवस्था की विशेष ज़िम्मेदारी देता है, और पारंपरिक ग्राम परिषदें आज भी पारंपरिक क़ानून के तहत कई स्थानीय विवाद सुलझाती हैं। अन्य राज्यों से आने वाले पर्यटकों को 1873 के बंगाल ईस्टर्न फ़्रंटियर विनियम के तहत इनर लाइन परमिट चाहिए।\n\n2024 में लोकसभा चुनाव के साथ हुए विधानसभा चुनाव में भारतीय जनता पार्टी जीती, और पेमा खांडू ने 13 जून 2024 को लगातार तीसरे कार्यकाल के लिए मुख्यमंत्री पद की शपथ ली, चौना मेन उपमुख्यमंत्री बने। तेसाम पोंग्ते 15 जून 2024 को अध्यक्ष चुने गए, और लेफ़्टिनेंट जनरल के. टी. परनाइक (सेवानिवृत्त) 16 फ़रवरी 2023 से राज्यपाल हैं। अगला विधानसभा चुनाव 2029 तक होना है।",
        "अरुणाचल प्रदेशमध्ये एकसदनी विधिमंडळ आहे, इटानगर येथील 60 सदस्यांची विधानसभा, आणि राज्यातून लोकसभेवर 2 व राज्यसभेवर 1 सदस्य निवडला जातो. संविधानाचा अनुच्छेद 371ज राज्यपालांना कायदा व सुव्यवस्थेची विशेष जबाबदारी देतो, आणि पारंपरिक ग्रामपरिषदा आजही पारंपरिक कायद्यानुसार अनेक स्थानिक वाद सोडवतात. इतर राज्यांतून येणाऱ्या पर्यटकांना 1873 च्या बंगाल ईस्टर्न फ्रंटियर नियमनाखाली इनर लाइन परवाना लागतो.\n\n2024 मध्ये लोकसभा निवडणुकीसोबत झालेली विधानसभा निवडणूक भारतीय जनता पक्षाने जिंकली, आणि पेमा खांडू यांनी 13 जून 2024 रोजी सलग तिसऱ्या कारकिर्दीसाठी मुख्यमंत्रिपदाची शपथ घेतली, चौना मेन उपमुख्यमंत्री झाले. तेसाम पोंग्ते 15 जून 2024 रोजी अध्यक्षपदी निवडले गेले, आणि लेफ्टनंट जनरल के. टी. परनाईक (निवृत्त) 16 फेब्रुवारी 2023 पासून राज्यपाल आहेत. पुढील विधानसभा निवडणूक 2029 पर्यंत होणे अपेक्षित आहे."),
        sources=["etv-bharat", "ar-governor", "newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("lokbhavan", "Lok Bhavan Arunachal Pradesh", "लोक भवन अरुणाचल प्रदेश", "लोक भवन अरुणाचल प्रदेश", url="https://arunachalgovernor.gov.in", src="ar-governor"),
        it3("portal", "Government of Arunachal Pradesh", "अरुणाचल प्रदेश सरकार", "अरुणाचल प्रदेश शासन", url="https://arunachalpradesh.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2024 Assembly election — party-wise result", "2024 विधानसभा चुनाव — दलवार परिणाम", "2024 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Arunachal Pradesh 2024."),
        (L("Chief Minister's swearing-in — official source", "मुख्यमंत्री का शपथ ग्रहण — आधिकारिक स्रोत", "मुख्यमंत्र्यांचा शपथविधी — अधिकृत स्रोत"), "ar-governor", "Replace the news report with the Lok Bhavan release of 13 June 2024."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Road and air links dominate Arunachal's projects. The Sela Tunnel on the road to Tawang opened in March 2024, and Donyi Polo Airport gave Itanagar an airport in 2022. Other works include the Frontier Highway along the northern border, the Trans-Arunachal Highway, new railway lines, and large hydropower projects such as Lower Subansiri and Dibang; these will be added as cards once their status is confirmed from official sources. Each card shows its source and the date it was checked.",
        "सड़क और हवाई संपर्क अरुणाचल की परियोजनाओं में प्रमुख हैं। तवांग जाने वाली सड़क पर सेला सुरंग मार्च 2024 में खुली, और दोन्यी पोलो हवाई अड्डे ने 2022 में ईटानगर को हवाई अड्डा दिया। अन्य कार्यों में उत्तरी सीमा के साथ फ़्रंटियर हाईवे, ट्रांस-अरुणाचल हाईवे, नई रेल लाइनें और निचली सुबनसिरी व दिबांग जैसी बड़ी जलविद्युत परियोजनाएँ शामिल हैं; आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर इन्हें कार्ड के रूप में जोड़ा जाएगा। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "रस्ते व हवाई संपर्क हे अरुणाचलच्या प्रकल्पांत प्रमुख आहेत. तवांगच्या रस्त्यावरील सेला बोगदा मार्च 2024 मध्ये सुरू झाला, आणि दोन्यी पोलो विमानतळाने 2022 मध्ये इटानगरला विमानतळ दिला. इतर कामांत उत्तर सीमेलगतचा फ्रंटियर महामार्ग, ट्रान्स-अरुणाचल महामार्ग, नवे रेल्वेमार्ग, आणि खालचा सुबनसिरी व दिबांगसारखे मोठे जलविद्युत प्रकल्प यांचा समावेश आहे; अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर त्यांची कार्डे जोडली जातील. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["new-india-samachar", "morung-express"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Sela Tunnel — official PIB release", "सेला सुरंग — आधिकारिक पीआईबी विज्ञप्ति", "सेला बोगदा — अधिकृत पीआयबी प्रसिद्धिपत्रक"), "pib", "Replace the IANS report with the PIB release of 9 March 2024."),
        (L("Lower Subansiri and Dibang projects — official status", "निचली सुबनसिरी और दिबांग परियोजनाएँ — आधिकारिक स्थिति", "खालचा सुबनसिरी व दिबांग प्रकल्प — अधिकृत स्थिती"), "india-gov", "NHPC / Ministry of Power."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Arunachal Pradesh is reached mostly by road from Assam. NH-13 (the Trans-Arunachal Highway) and other national highways climb from the Brahmaputra plains to Tawang, Ziro, Aalo, Pasighat, Tezu and Roing, and the Sela Tunnel keeps Tawang open in winter. Donyi Polo Airport at Hollongi serves Itanagar, and smaller airports at Pasighat, Tezu and Ziro have regional flights; helicopter services link remote districts. Naharlagun near Itanagar has had a railway station since 2014, and the Bogibeel bridge across the Brahmaputra in Assam shortened the trip to the eastern districts.",
        "अरुणाचल प्रदेश तक अधिकतर असम से सड़क मार्ग से पहुँचा जाता है। एनएच-13 (ट्रांस-अरुणाचल हाईवे) और अन्य राष्ट्रीय राजमार्ग ब्रह्मपुत्र के मैदानों से तवांग, ज़ीरो, आलो, पासीघाट, तेज़ू और रोइंग तक चढ़ते हैं, और सेला सुरंग सर्दियों में तवांग को खुला रखती है। होल्लोंगी का दोन्यी पोलो हवाई अड्डा ईटानगर की सेवा करता है, और पासीघाट, तेज़ू और ज़ीरो के छोटे हवाई अड्डों से क्षेत्रीय उड़ानें हैं; हेलिकॉप्टर सेवाएँ दूरस्थ ज़िलों को जोड़ती हैं। ईटानगर के पास नहारलगुन में 2014 से रेलवे स्टेशन है, और असम में ब्रह्मपुत्र पर बोगीबील पुल ने पूर्वी ज़िलों की यात्रा छोटी की।",
        "अरुणाचल प्रदेशला बहुतेक आसाममधून रस्त्याने पोहोचले जाते. एनएच-13 (ट्रान्स-अरुणाचल महामार्ग) व इतर राष्ट्रीय महामार्ग ब्रह्मपुत्रेच्या मैदानांतून तवांग, झिरो, आलो, पासीघाट, तेझू व रोइंगपर्यंत चढतात, आणि सेला बोगदा हिवाळ्यात तवांग खुले ठेवतो. होल्लोंगीचा दोन्यी पोलो विमानतळ इटानगरला सेवा देतो, आणि पासीघाट, तेझू व झिरोच्या लहान विमानतळांवरून प्रादेशिक उड्डाणे आहेत; हेलिकॉप्टर सेवा दुर्गम जिल्ह्यांना जोडतात. इटानगरजवळील नाहरलगुन येथे 2014 पासून रेल्वे स्थानक आहे, आणि आसाममधील ब्रह्मपुत्रेवरील बोगीबील पुलाने पूर्वेकडील जिल्ह्यांचा प्रवास कमी केला."),
        conf="Editorial"),
    lst("airports", [
        it3("hgi", "Donyi Polo Airport, Itanagar", "दोन्यी पोलो हवाई अड्डा, ईटानगर", "दोन्यी पोलो विमानतळ, इटानगर", m=("Hollongi", "होल्लोंगी", "होल्लोंगी")),
        it3("ixt", "Pasighat Airport", "पासीघाट हवाई अड्डा", "पासीघाट विमानतळ"), it3("tezu", "Tezu Airport", "तेज़ू हवाई अड्डा", "तेझू विमानतळ"),
        it3("ziro", "Ziro Airport", "ज़ीरो हवाई अड्डा", "झिरो विमानतळ"),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("Inner Line Permit rules — official notice", "इनर लाइन परमिट नियम — आधिकारिक सूचना", "इनर लाइन परवाना नियम — अधिकृत सूचना"), "india-gov", "Government of Arunachal Pradesh e-ILP portal."),
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Arunachal Pradesh's steep, rain-fed rivers give it a very large untapped hydropower potential. Operating stations include Ranganadi, Pare and Kameng, the last dedicated to the nation with Donyi Polo Airport in November 2022, and the Lower Subansiri project on the Assam border has been commissioning its units. Larger projects such as Dibang have been approved, and proposals on the Siang are debated because of their impact on forests, fisheries, downstream Assam and local communities. Remote villages rely on small hydel plants and solar power.",
        "अरुणाचल प्रदेश की तेज़ ढलान वाली, वर्षा-पोषित नदियाँ इसे बहुत बड़ी अप्रयुक्त जलविद्युत क्षमता देती हैं। चालू केंद्रों में रंगानदी, पारे और कामेंग शामिल हैं, जिनमें कामेंग को नवंबर 2022 में दोन्यी पोलो हवाई अड्डे के साथ राष्ट्र को समर्पित किया गया, और असम सीमा पर निचली सुबनसिरी परियोजना अपनी इकाइयाँ चालू कर रही है। दिबांग जैसी बड़ी परियोजनाएँ स्वीकृत हुई हैं, और सियांग पर प्रस्ताव वनों, मत्स्य पालन, निचले असम और स्थानीय समुदायों पर प्रभाव के कारण बहस में हैं। दूरस्थ गाँव छोटे जलविद्युत संयंत्रों और सौर ऊर्जा पर निर्भर हैं।",
        "अरुणाचल प्रदेशच्या तीव्र उताराच्या, पावसावर पोसलेल्या नद्या त्याला फार मोठी न वापरलेली जलविद्युत क्षमता देतात. चालू केंद्रांत रंगानदी, पारे व कामेंग यांचा समावेश आहे, ज्यांपैकी कामेंग नोव्हेंबर 2022 मध्ये दोन्यी पोलो विमानतळासह राष्ट्राला समर्पित झाले, आणि आसाम सीमेवरील खालचा सुबनसिरी प्रकल्प आपली युनिट्स सुरू करत आहे. दिबांगसारखे मोठे प्रकल्प मंजूर झाले आहेत, आणि सियांगवरील प्रस्ताव जंगले, मत्स्यव्यवसाय, खालचा आसाम व स्थानिक समुदायांवरील परिणामांमुळे वादात आहेत. दुर्गम गावे लहान जलविद्युत प्रकल्प व सौरऊर्जेवर अवलंबून आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed hydropower capacity by station", "केंद्रवार स्थापित जलविद्युत क्षमता", "केंद्रनिहाय स्थापित जलविद्युत क्षमता"), "cea", "CEA installed capacity report."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Mobile and internet coverage is still limited in many remote and border villages, and the Union government's schemes for 4G towers in the North-East have been extending it. Government services, including the e-Inner Line Permit, are offered online, and NERIST and NIT Arunachal Pradesh train engineers.",
        "कई दूरस्थ और सीमावर्ती गाँवों में मोबाइल और इंटरनेट कवरेज अब भी सीमित है, और पूर्वोत्तर में 4जी टावरों की केंद्र सरकार की योजनाएँ इसे बढ़ा रही हैं। ई-इनर लाइन परमिट सहित सरकारी सेवाएँ ऑनलाइन दी जाती हैं, और नेरिस्ट और एनआईटी अरुणाचल प्रदेश इंजीनियर तैयार करते हैं।",
        "अनेक दुर्गम व सीमावर्ती गावांत मोबाइल व इंटरनेट सेवा अजूनही मर्यादित आहे, आणि ईशान्येत 4जी मनोऱ्यांच्या केंद्र सरकारच्या योजना ती वाढवत आहेत. ई-इनर लाइन परवान्यासह सरकारी सेवा ऑनलाइन दिल्या जातात, आणि नेरिस्ट व एनआयटी अरुणाचल प्रदेश अभियंते घडवतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Villages without mobile coverage", "बिना मोबाइल कवरेज वाले गाँव", "मोबाइल सेवा नसलेली गावे"), "india-gov", "Department of Telecommunications / USOF."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("AR", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["AR"]
ger = AP["aishe_ger"]["AR"]; nu = AP["aishe_universities_2021_22"]["AR"]; nc = AP["aishe_colleges_2021_22"]["AR"]
module(R, "education", [
    prose("p1", L(
        f"Literacy in Arunachal Pradesh was 65.4% at the 2011 Census, below the national 73%. The higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE (women {gf}%, men {gm}%), and the State had {nu} universities and {inr(nc)} colleges.\n\nRajiv Gandhi University at Rono Hills, Doimukh, is the central university; the North Eastern Regional Institute of Science and Technology (NERIST) at Nirjuli and NIT Arunachal Pradesh train engineers; and the Tomo Riba Institute of Health and Medical Sciences at Naharlagun is the State's medical college. Many students still study in Assam, Shillong or further away.",
        f"2011 की जनगणना में अरुणाचल प्रदेश की साक्षरता 65.4% थी, जो राष्ट्रीय 73% से कम है। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था (महिलाएँ {gf}%, पुरुष {gm}%), और राज्य में {nu} विश्वविद्यालय और {inr(nc)} कॉलेज थे।\n\nदोईमुख की रोनो पहाड़ियों पर राजीव गांधी विश्वविद्यालय केंद्रीय विश्वविद्यालय है; निर्जुली का नॉर्थ ईस्टर्न रीजनल इंस्टीट्यूट ऑफ़ साइंस एंड टेक्नोलॉजी (नेरिस्ट) और एनआईटी अरुणाचल प्रदेश इंजीनियर तैयार करते हैं; और नहारलगुन का तोमो रिबा स्वास्थ्य एवं चिकित्सा विज्ञान संस्थान राज्य का मेडिकल कॉलेज है। बहुत से छात्र अब भी असम, शिलांग या और दूर पढ़ते हैं।",
        f"2011 च्या जनगणनेत अरुणाचल प्रदेशची साक्षरता 65.4% होती, राष्ट्रीय 73% पेक्षा कमी. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते (स्त्रिया {gf}%, पुरुष {gm}%), आणि राज्यात {nu} विद्यापीठे व {inr(nc)} महाविद्यालये होती.\n\nदोईमुखच्या रोनो टेकड्यांवरील राजीव गांधी विद्यापीठ हे केंद्रीय विद्यापीठ आहे; निर्जुलीची नॉर्थ ईस्टर्न रीजनल इन्स्टिट्यूट ऑफ सायन्स अँड टेक्नॉलॉजी (नेरिस्ट) व एनआयटी अरुणाचल प्रदेश अभियंते घडवतात; आणि नाहरलगुनची तोमो रिबा आरोग्य व वैद्यकीय विज्ञान संस्था हे राज्याचे वैद्यकीय महाविद्यालय आहे. अनेक विद्यार्थी अजूनही आसाम, शिलाँग किंवा आणखी दूर शिकतात."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("rgu", "Rajiv Gandhi University", "राजीव गांधी विश्वविद्यालय", "राजीव गांधी विद्यापीठ", m=("Central university, Doimukh", "केंद्रीय विश्वविद्यालय, दोईमुख", "केंद्रीय विद्यापीठ, दोईमुख")),
        it3("nerist", "NERIST", "नेरिस्ट", "नेरिस्ट", m=("Nirjuli", "निर्जुली", "निर्जुली")),
        it3("nitap", "NIT Arunachal Pradesh", "एनआईटी अरुणाचल प्रदेश", "एनआयटी अरुणाचल प्रदेश", m=("Jote", "जोते", "जोते")),
        it3("trihms", "Tomo Riba Institute of Health and Medical Sciences", "तोमो रिबा स्वास्थ्य एवं चिकित्सा विज्ञान संस्थान", "तोमो रिबा आरोग्य व वैद्यकीय विज्ञान संस्था", m=("Naharlagun", "नहारलगुन", "नाहरलगुन")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["AR"]; s = C["srs"]["AR"]
module(R, "health", [
    prose("p1", L(
        f"Arunachal Pradesh's infant mortality rate was {s[5]:.0f} per 1,000 live births in 2020 in the Sample Registration System, down from {s[4]} in 2010 and below the national 28; the birth rate was {s[1]} and the death rate {s[3]} per 1,000. In NFHS-5, {n['institutional_N5']:.1f}% of births took place in health facilities; {n['stunted'][1]:.1f}% of children under five were stunted (down from {n['stunted'][0]}%), {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight.\n\nThe Tomo Riba Institute of Health and Medical Sciences at Naharlagun is the main referral hospital, with district hospitals across the State. Distance is the biggest challenge: many villages are days' walk or a helicopter ride from a hospital, and serious cases are often referred to Assam.",
        f"नमूना पंजीकरण प्रणाली में 2020 में अरुणाचल प्रदेश की शिशु मृत्यु दर प्रति 1,000 जीवित जन्म पर {s[5]:.0f} थी, जो 2010 के {s[4]} से कम और राष्ट्रीय 28 से कम है; जन्म दर प्रति 1,000 पर {s[1]} और मृत्यु दर {s[3]} थी। एनएफ़एचएस-5 में {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए; पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने थे ({n['stunted'][0]}% से कम), {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के।\n\nनहारलगुन का तोमो रिबा स्वास्थ्य एवं चिकित्सा विज्ञान संस्थान मुख्य रेफ़रल अस्पताल है, और पूरे राज्य में ज़िला अस्पताल हैं। दूरी सबसे बड़ी चुनौती है: कई गाँव अस्पताल से कई दिनों की पैदल दूरी या हेलिकॉप्टर यात्रा पर हैं, और गंभीर मामले अक्सर असम भेजे जाते हैं।",
        f"नमुना नोंदणी पद्धतीनुसार 2020 मध्ये अरुणाचल प्रदेशचा अर्भक मृत्युदर दर 1,000 जिवंत जन्मांमागे {s[5]:.0f} होता, 2010 मधील {s[4]} वरून कमी आणि राष्ट्रीय 28 पेक्षा कमी; जन्मदर दर 1,000 मागे {s[1]} व मृत्युदर {s[3]} होता. एनएफएचएस-5 मध्ये {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या; पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी होती ({n['stunted'][0]}% वरून कमी), {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची.\n\nनाहरलगुनची तोमो रिबा आरोग्य व वैद्यकीय विज्ञान संस्था हे मुख्य संदर्भ रुग्णालय आहे, आणि संपूर्ण राज्यात जिल्हा रुग्णालये आहेत. अंतर हे सर्वांत मोठे आव्हान आहे: अनेक गावे रुग्णालयापासून अनेक दिवसांच्या पायपिटीवर किंवा हेलिकॉप्टर प्रवासावर आहेत, आणि गंभीर रुग्ण अनेकदा आसामला पाठवले जातात."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("AR"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"), "srs", "Arunachal Pradesh is not in the SRS abridged life table for major States used here."),
    ]),
])
print("ar mod2 ok")
