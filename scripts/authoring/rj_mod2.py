"""Rajasthan modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-RJ"
ECI = "https://results.eci.gov.in/AcResultGenDecNew2023/partywiseresult-S20.htm"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_RJ = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 16 Oct 2026. "
           "FY2025-26 is the latest year published for Rajasthan and may be revised.")
mo = research("mospi_rj.json")
NAME = L("Rajasthan", "राजस्थान", "राजस्थान")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Rajasthan's culture grew from its courts and its desert villages. Rajput painting flourished in schools such as Mewar, Marwar, Bundi, Kota and Kishangarh, and Nathdwara is known for its pichhwai cloth paintings; phad scrolls tell the epics of folk heroes like Pabuji and Devnarayan. The hereditary Manganiyar and Langa musicians of the Thar sing to the kamaicha and sarangi, the Kalbelia dance — inscribed by UNESCO in 2010 — and Ghoomar are performed across the world, and puppeteers stage kathputli shows. The devotional songs of Meera Bai remain popular.\n\nCrafts include blue pottery of Jaipur, block printing at Sanganer and Bagru, bandhej tie-dye, Kota doria weaving, lac bangles, Thewa gold-on-glass work of Pratapgarh, Molela terracotta, and the marble of Makrana, used in the Taj Mahal.",
        "राजस्थान की संस्कृति उसके दरबारों और मरु गाँवों से पनपी। मेवाड़, मारवाड़, बूँदी, कोटा और किशनगढ़ जैसी शैलियों में राजपूत चित्रकला फली-फूली, और नाथद्वारा अपनी पिछवाई कपड़ा चित्रकला के लिए जाना जाता है; फड़ पट पाबूजी और देवनारायण जैसे लोकनायकों की गाथाएँ कहते हैं। थार के वंशानुगत मांगणियार और लंगा संगीतकार कमायचा और सारंगी पर गाते हैं, कालबेलिया नृत्य — जिसे यूनेस्को ने 2010 में सूचीबद्ध किया — और घूमर दुनिया भर में प्रस्तुत होते हैं, और कठपुतली कलाकार कठपुतली के खेल दिखाते हैं। मीराबाई के भक्ति पद आज भी लोकप्रिय हैं।\n\nशिल्पों में जयपुर की ब्लू पॉटरी, सांगानेर और बगरू की ठप्पा छपाई, बंधेज, कोटा डोरिया बुनाई, लाख की चूड़ियाँ, प्रतापगढ़ का कांच पर सोने का थेवा काम, मोलेला की मृण्मूर्तियाँ, और ताजमहल में प्रयुक्त मकराना का संगमरमर शामिल हैं।",
        "राजस्थानची संस्कृती त्याच्या दरबारांतून व वाळवंटी गावांतून वाढली. मेवाड, मारवाड, बुंदी, कोटा व किशनगड यांसारख्या शैलींत राजपूत चित्रकला बहरली, आणि नाथद्वारा पिछवाई कापडी चित्रांसाठी ओळखले जाते; फड पट पाबूजी व देवनारायण यांसारख्या लोकनायकांच्या गाथा सांगतात. थरमधील वंशपरंपरागत मांगणियार व लंगा संगीतकार कमायचा व सारंगीवर गातात, कालबेलिया नृत्य — युनेस्कोने 2010 मध्ये नोंदवलेले — आणि घूमर जगभर सादर होतात, आणि कठपुतळी कलाकार कठपुतळीचे खेळ करतात. मीराबाईंची भक्तिपदे आजही लोकप्रिय आहेत.\n\nहस्तकलेत जयपूरची निळी मृद्भांडी, सांगानेर व बगरूची ठसे छपाई, बांधणी, कोटा डोरिया विणकाम, लाखेच्या बांगड्या, प्रतापगडचे काचेवरील सोन्याचे थेवा काम, मोलेलाची मृण्मूर्ती आणि ताजमहालात वापरलेला मकरानाचा संगमरवर यांचा समावेश आहे."),
        conf="Editorial"),
    lst("festivals", [
        fest("gangaur", "Gangaur", "गणगौर", "गणगौर", ("March–April", "मार्च–अप्रैल", "मार्च–एप्रिल"),
             ("Women worship Gauri for marital happiness; processions in Jaipur and Udaipur.", "महिलाएँ सौभाग्य के लिए गौरी की पूजा करती हैं; जयपुर और उदयपुर में शोभायात्राएँ।", "स्त्रिया सौभाग्यासाठी गौरीची पूजा करतात; जयपूर व उदयपूरमध्ये मिरवणुका.")),
        fest("teej", "Teej", "तीज", "तीज", ("July–August", "जुलाई–अगस्त", "जुलै–ऑगस्ट"),
             ("Monsoon festival of swings, songs and green clothes.", "झूलों, गीतों और हरे वस्त्रों का मानसूनी उत्सव।", "झोके, गाणी व हिरव्या वस्त्रांचा पावसाळी सण.")),
        fest("pushkar", "Pushkar Fair", "पुष्कर मेला", "पुष्कर जत्रा", ("October–November (Kartik)", "अक्टूबर–नवंबर (कार्तिक)", "ऑक्टोबर–नोव्हेंबर (कार्तिक)"),
             ("Camel and livestock fair and holy dip at Pushkar lake.", "ऊँट और पशु मेला तथा पुष्कर सरोवर में पवित्र स्नान।", "उंट व पशुंची जत्रा आणि पुष्कर सरोवरात पवित्र स्नान.")),
        fest("desert", "Desert Festival, Jaisalmer", "मरु महोत्सव, जैसलमेर", "वाळवंट महोत्सव, जैसलमेर", ("February", "फ़रवरी", "फेब्रुवारी"),
             ("Folk music, camel races and dune events.", "लोक संगीत, ऊँट दौड़ और टीलों पर कार्यक्रम।", "लोकसंगीत, उंटांच्या शर्यती व वाळूच्या टेकड्यांवरील कार्यक्रम.")),
        fest("urs", "Urs of Khwaja Moinuddin Chishti, Ajmer", "ख़्वाजा मोइनुद्दीन चिश्ती का उर्स, अजमेर", "ख्वाजा मोईनुद्दीन चिश्ती यांचा उरूस, अजमेर", ("Rajab (Islamic calendar)", "रजब (हिजरी पंचांग)", "रजब (हिजरी पंचांग)"),
             ("Six-day gathering at the Ajmer Sharif dargah.", "अजमेर शरीफ़ दरगाह पर छह दिन का समागम।", "अजमेर शरीफ दर्ग्यावर सहा दिवसांचा मेळा.")),
        fest("diwali", "Diwali and Holi", "दीवाली और होली", "दिवाळी व होळी", ("Oct–Nov; March", "अक्टूबर–नवंबर; मार्च", "ऑक्टो.–नोव्हें.; मार्च"),
             ("Celebrated across the State; lit-up bazaars of Jaipur at Diwali.", "पूरे राज्य में मनाए जाते हैं; दीवाली पर जयपुर के रोशन बाज़ार।", "राज्यभर साजरे; दिवाळीत जयपूरचे उजळलेले बाजार.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("ghoomar", "Ghoomar", "घूमर", "घूमर"), it3("kalbelia", "Kalbelia", "कालबेलिया", "कालबेलिया"), it3("manganiyar", "Manganiyar and Langa music", "मांगणियार और लंगा संगीत", "मांगणियार व लंगा संगीत"),
        it3("phad", "Phad painting", "फड़ चित्रकला", "फड चित्रकला"), it3("miniature", "Rajput miniature painting", "राजपूत लघु चित्रकला", "राजपूत लघुचित्रकला"),
        it3("kathputli", "Kathputli puppetry", "कठपुतली", "कठपुतळी"), it3("bandhej", "Bandhej tie-dye", "बंधेज", "बांधणी"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("dalbaati", "Dal baati churma", "दाल बाटी चूरमा", "दाल बाटी चुरमा", d=("Baked wheat balls with lentils and sweet crushed wheat.", "दाल और मीठे चूरमे के साथ सेंकी गई गेहूँ की बाटियाँ।", "डाळ व गोड चुरम्यासोबत भाजलेल्या गव्हाच्या बाट्या.")),
        it3("kersangri", "Ker sangri", "केर सांगरी", "केर सांगरी", d=("Desert berries and khejri beans, cooked dry with spices.", "मरुस्थलीय बेर और खेजड़ी की फलियाँ, मसालों के साथ सूखी पकाई गईं।", "वाळवंटी बेरे व खेजडीच्या शेंगा, मसाल्यांसह सुक्या शिजवलेल्या.")),
        it3("gatte", "Gatte ki sabzi", "गट्टे की सब्ज़ी", "गट्ट्याची भाजी", d=("Gram-flour dumplings in yoghurt curry.", "दही की करी में बेसन के गट्टे।", "दह्याच्या आमटीत बेसनाचे गट्टे.")),
        it3("laalmaas", "Laal maas", "लाल मांस", "लाल मांस", d=("Fiery mutton curry with Mathania chillies.", "मथानिया मिर्च के साथ तीखी मटन करी।", "मथानिया मिरचीसह तिखट मटण.")),
        it3("ghevar", "Ghevar and pyaaz kachori", "घेवर और प्याज़ कचौरी", "घेवर व कांदा कचोरी", d=("Teej sweet and Jodhpur's favourite snack.", "तीज की मिठाई और जोधपुर का प्रिय नाश्ता।", "तीजची मिठाई व जोधपूरचा आवडता नाश्ता.")),
        it3("bhujia", "Bikaneri bhujia", "बीकानेरी भुजिया", "बिकानेरी भुजिया", d=("Spiced gram-flour snack; a registered GI.", "मसालेदार बेसन का नमकीन; पंजीकृत जीआई।", "मसालेदार बेसनाचा फराळ; नोंदणीकृत जीआय.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("poshak", "Ghagra, kurti and odhni", "घाघरा, कुर्ती और ओढ़नी", "घागरा, कुर्ती व ओढणी", d=("Women's dress, often in leheriya or bandhej.", "महिलाओं की पोशाक, अक्सर लहरिया या बंधेज में।", "स्त्रियांचा पोशाख, अनेकदा लहरिया किंवा बांधणीत.")),
        it3("safa", "Safa (turban), angrakha and dhoti", "साफ़ा, अंगरखा और धोती", "साफा (फेटा), अंगरखा व धोतर", d=("Turban styles and colours vary by region and occasion.", "साफ़े की शैली और रंग क्षेत्र और अवसर के अनुसार बदलते हैं।", "फेट्याची पद्धत व रंग प्रदेश व प्रसंगानुसार बदलतात.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; mining = 100 * g["mining"] / g["total"]
module(R, "economy", [
    prose("p1", L(
        f"Rajasthan's GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26 in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2025-26'][0])}. Agriculture, livestock and fishing made up about {agri:.0f}% of GSVA in FY2024-25. Farmers grow pearl millet (bajra), mustard, guar, cumin, wheat and pulses, and the State's camels, goats, sheep and cattle make livestock a major source of income. Mining and quarrying were about {mining:.1f}% of GSVA — zinc and lead at Zawar and Rampura Agucha, marble, granite and sandstone, limestone for cement, and crude oil from the Barmer basin — and manufacturing about {mfg:.0f}%, including textiles at Bhilwara, cement, automobiles and engineering in the Neemrana–Bhiwadi belt near Delhi, and the new refinery at Pachpadra.\n\nTourism, trade and handicrafts are important in the services sector. The PLFS unemployment rate was 4.3% in 2025, and women's labour-force participation, at 52.3%, was well above the national 40.0%.",
        f"मोस्पी शृंखला में वित्त वर्ष 2025-26 में राजस्थान का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2025-26'][0])} था। वित्त वर्ष 2024-25 में कृषि, पशुपालन और मत्स्य पालन जीएसवीए का लगभग {agri:.0f}% थे। किसान बाजरा, सरसों, ग्वार, जीरा, गेहूँ और दलहन उगाते हैं, और राज्य के ऊँट, बकरियाँ, भेड़ें और गाय-भैंस पशुपालन को आय का बड़ा स्रोत बनाते हैं। खनन जीएसवीए का लगभग {mining:.1f}% था — ज़ावर और रामपुरा आगुचा में जस्ता और सीसा, संगमरमर, ग्रेनाइट और बलुआ पत्थर, सीमेंट के लिए चूना पत्थर, और बाड़मेर बेसिन से कच्चा तेल — और विनिर्माण लगभग {mfg:.0f}%, जिसमें भीलवाड़ा के वस्त्र, सीमेंट, दिल्ली के पास नीमराना–भिवाड़ी पट्टी में ऑटोमोबाइल और इंजीनियरिंग, और पचपदरा की नई रिफ़ाइनरी शामिल हैं।\n\nसेवा क्षेत्र में पर्यटन, व्यापार और हस्तशिल्प महत्त्वपूर्ण हैं। 2025 में पीएलएफ़एस बेरोज़गारी दर 4.3% थी, और महिलाओं की श्रम बल भागीदारी 52.3% थी, जो राष्ट्रीय 40.0% से काफ़ी अधिक है।",
        f"मोस्पी मालिकेनुसार आ.व. 2025-26 मध्ये राजस्थानचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2025-26'][0])} होते. आ.व. 2024-25 मध्ये शेती, पशुपालन व मत्स्यव्यवसायाचा जीएसव्हीएमध्ये सुमारे {agri:.0f}% वाटा होता. शेतकरी बाजरी, मोहरी, गवार, जिरे, गहू व कडधान्ये पिकवतात, आणि राज्यातील उंट, शेळ्या, मेंढ्या व गायी-म्हशींमुळे पशुपालन हे उत्पन्नाचे मोठे साधन आहे. खाणकामाचा वाटा सुमारे {mining:.1f}% होता — झावर व रामपुरा आगुचा येथे जस्त व शिसे, संगमरवर, ग्रॅनाइट व वालुकाश्म, सिमेंटसाठी चुनखडी, आणि बाडमेर खोऱ्यातून कच्चे तेल — आणि उत्पादन उद्योगाचा सुमारे {mfg:.0f}%, ज्यात भीलवाड्याची वस्त्रे, सिमेंट, दिल्लीजवळील नीमराणा–भिवाडी पट्ट्यातील वाहन व अभियांत्रिकी उद्योग, आणि पचपदरा येथील नवी रिफायनरी यांचा समावेश आहे.\n\nसेवाक्षेत्रात पर्यटन, व्यापार व हस्तकला महत्त्वाच्या आहेत. 2025 मध्ये पीएलएफएस बेरोजगारी दर 4.3% होता, आणि स्त्रियांचा श्रमशक्ती सहभाग 52.3% होता — राष्ट्रीय 40.0% पेक्षा बराच जास्त."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_RJ), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_RJ), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_RJ), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("RJ", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    plfs_series("RJ", NAME),
    lst("sectors-key", [
        it3("agri", "Millets, mustard and spices", "बाजरा, सरसों और मसाले", "बाजरी, मोहरी व मसाले", d=("Bajra, mustard, guar, cumin and coriander across the State.", "पूरे राज्य में बाजरा, सरसों, ग्वार, जीरा और धनिया।", "राज्यभर बाजरी, मोहरी, गवार, जिरे व धणे.")),
        it3("livestock", "Livestock and dairy", "पशुपालन और डेयरी", "पशुपालन व दुग्धव्यवसाय", d=("Camels, goats, sheep and cattle; milk co-operatives.", "ऊँट, बकरियाँ, भेड़ें और गाय-भैंस; दुग्ध सहकारी।", "उंट, शेळ्या, मेंढ्या व गायी-म्हशी; दूध सहकारी संस्था.")),
        it3("mining", "Minerals and stone", "खनिज और पत्थर", "खनिजे व दगड", d=("Zinc–lead, marble, sandstone, granite, limestone and gypsum.", "जस्ता–सीसा, संगमरमर, बलुआ पत्थर, ग्रेनाइट, चूना पत्थर और जिप्सम।", "जस्त–शिसे, संगमरवर, वालुकाश्म, ग्रॅनाइट, चुनखडी व जिप्सम.")),
        it3("oil", "Oil, gas and refining", "तेल, गैस और शोधन", "तेल, वायू व शुद्धीकरण", d=("Barmer basin oil fields and the Pachpadra refinery.", "बाड़मेर बेसिन के तेल क्षेत्र और पचपदरा रिफ़ाइनरी।", "बाडमेर खोऱ्यातील तेलक्षेत्रे व पचपदरा रिफायनरी.")),
        it3("solar", "Solar and wind energy", "सौर और पवन ऊर्जा", "सौर व पवन ऊर्जा", d=("Large solar parks at Bhadla and in western districts.", "भड़ला और पश्चिमी ज़िलों में बड़े सौर पार्क।", "भडला व पश्चिमेकडील जिल्ह्यांत मोठी सौर उद्याने.")),
        it3("tourism", "Tourism and handicrafts", "पर्यटन और हस्तशिल्प", "पर्यटन व हस्तकला", d=("Heritage hotels, forts and craft exports.", "हेरिटेज होटल, क़िले और शिल्प निर्यात।", "हेरिटेज हॉटेल, किल्ले व हस्तकला निर्यात.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Crop production (mustard, bajra, cumin)", "फ़सल उत्पादन (सरसों, बाजरा, जीरा)", "पीक उत्पादन (मोहरी, बाजरी, जिरे)"), "india-gov", "State Economic Review / Ministry of Agriculture."),
        (L("Crude oil production (Barmer basin)", "कच्चा तेल उत्पादन (बाड़मेर बेसिन)", "कच्च्या तेलाचे उत्पादन (बाडमेर खोरे)"), "india-gov", "Ministry of Petroleum and Natural Gas statistics."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Rajasthan has a unicameral legislature: the 200-member Legislative Assembly meets in Jaipur. The State elects 25 members to the Lok Sabha and 10 to the Rajya Sabha.\n\nIn the Assembly election of November 2023, results for 199 seats were declared on 3 December: the BJP won 115, the Congress 69, the Bharat Adivasi Party 3, the BSP 2, the RLD and RLP one each, and independents 8 (ECI); polling in the remaining seat was held later. Bhajan Lal Sharma, a first-time MLA, was sworn in as Chief Minister on 15 December 2023, with Diya Kumari and Prem Chand Bairwa as Deputy Chief Ministers. Haribhau Kisanrao Bagde has been Governor since July 2024.",
        "राजस्थान में एकसदनीय विधानमंडल है: 200 सदस्यों वाली विधानसभा जयपुर में बैठती है। राज्य से लोकसभा के 25 और राज्यसभा के 10 सदस्य चुने जाते हैं।\n\nनवंबर 2023 के विधानसभा चुनाव में 3 दिसंबर को 199 सीटों के परिणाम घोषित हुए: भाजपा ने 115, कांग्रेस ने 69, भारत आदिवासी पार्टी ने 3, बसपा ने 2, रालोद और रालोपा ने एक-एक, और निर्दलीयों ने 8 सीटें जीतीं (भारत निर्वाचन आयोग); शेष एक सीट पर मतदान बाद में हुआ। पहली बार विधायक बने भजनलाल शर्मा ने 15 दिसंबर 2023 को मुख्यमंत्री पद की शपथ ली, और दीया कुमारी व प्रेमचंद बैरवा उपमुख्यमंत्री बने। हरिभाऊ किसनराव बागडे जुलाई 2024 से राज्यपाल हैं।",
        "राजस्थानात एकसदनी विधिमंडळ आहे: 200 सदस्यांची विधानसभा जयपूरमध्ये भरते. राज्यातून लोकसभेवर 25 आणि राज्यसभेवर 10 सदस्य निवडले जातात.\n\nनोव्हेंबर 2023 च्या विधानसभा निवडणुकीत 3 डिसेंबर रोजी 199 जागांचे निकाल जाहीर झाले: भाजपने 115, काँग्रेसने 69, भारत आदिवासी पक्षाने 3, बसपने 2, रालोद व रालोपने प्रत्येकी एक, आणि अपक्षांनी 8 जागा जिंकल्या (भारत निवडणूक आयोग); उर्वरित एका जागेचे मतदान नंतर झाले. प्रथमच आमदार झालेले भजनलाल शर्मा यांनी 15 डिसेंबर 2023 रोजी मुख्यमंत्रिपदाची शपथ घेतली, आणि दिया कुमारी व प्रेमचंद बैरवा उपमुख्यमंत्री झाले. हरिभाऊ किसनराव बागडे जुलै 2024 पासून राज्यपाल आहेत."),
        sources=["eci", "tribune", "newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    table("result2023", L("Assembly election 2023 — seats won (199 seats declared)", "विधानसभा चुनाव 2023 — जीती गई सीटें (199 सीटें घोषित)", "विधानसभा निवडणूक 2023 — जिंकलेल्या जागा (199 जागा जाहीर)"),
          [col(L("Party", "दल", "पक्ष")), col(L("Seats", "सीटें", "जागा"), "right")],
          [[L("Bharatiya Janata Party", "भारतीय जनता पार्टी", "भारतीय जनता पक्ष"), "115"], [L("Indian National Congress", "भारतीय राष्ट्रीय कांग्रेस", "भारतीय राष्ट्रीय काँग्रेस"), "69"],
           [L("Bharat Adivasi Party", "भारत आदिवासी पार्टी", "भारत आदिवासी पक्ष"), "3"], [L("Bahujan Samaj Party", "बहुजन समाज पार्टी", "बहुजन समाज पक्ष"), "2"],
           [L("Rashtriya Lok Dal", "राष्ट्रीय लोक दल", "राष्ट्रीय लोक दल"), "1"], [L("Rashtriya Loktantrik Party", "राष्ट्रीय लोकतांत्रिक पार्टी", "राष्ट्रीय लोकतांत्रिक पक्ष"), "1"],
           [L("Independents", "निर्दलीय", "अपक्ष"), "8"], [L("Total", "कुल", "एकूण"), "199"]],
          "eci", ECI, period="2023",
          note=L("ECI results website, December 2023. Polling in one constituency was held later; later by-elections are not reflected.", "भारत निर्वाचन आयोग की परिणाम वेबसाइट, दिसंबर 2023। एक क्षेत्र में मतदान बाद में हुआ; बाद के उपचुनाव शामिल नहीं।", "भारत निवडणूक आयोगाचे निकाल संकेतस्थळ, डिसेंबर 2023. एका मतदारसंघात मतदान नंतर झाले; नंतरच्या पोटनिवडणुका समाविष्ट नाहीत.")),
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("assembly", "Rajasthan Legislative Assembly", "राजस्थान विधानसभा", "राजस्थान विधानसभा", url="https://assembly.rajasthan.gov.in", src="india-gov"),
        it3("portal", "Government of Rajasthan", "राजस्थान सरकार", "राजस्थान शासन", url="https://rajasthan.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Leader of Opposition — official notice", "नेता प्रतिपक्ष — आधिकारिक सूचना", "विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "Assembly secretariat."),
        (L("Local bodies by type", "प्रकार के अनुसार स्थानीय निकाय", "प्रकारानुसार स्थानिक स्वराज्य संस्था"), "india-gov", "Panchayati Raj and Local Self Government departments."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "On 4 July 2026 the Prime Minister dedicated the Rajasthan Refinery at Pachpadra, inaugurated a new terminal at Jodhpur airport and laid the foundation stone of Jaipur Metro Phase 2, part of projects worth about ₹1.06 lakh crore. The Ramjal Setu river-link project, agreed with Madhya Pradesh in December 2024, is meant to bring water to the eastern districts. Each card shows its source and the date it was checked.",
        "4 जुलाई 2026 को प्रधानमंत्री ने पचपदरा की राजस्थान रिफ़ाइनरी राष्ट्र को समर्पित की, जोधपुर हवाई अड्डे के नए टर्मिनल का उद्घाटन किया और जयपुर मेट्रो चरण 2 की आधारशिला रखी — लगभग ₹1.06 लाख करोड़ की परियोजनाओं का हिस्सा। दिसंबर 2024 में मध्य प्रदेश के साथ सहमत रामजल सेतु नदी-जोड़ परियोजना का उद्देश्य पूर्वी ज़िलों तक पानी लाना है। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "4 जुलै 2026 रोजी पंतप्रधानांनी पचपदरा येथील राजस्थान रिफायनरी राष्ट्राला समर्पित केली, जोधपूर विमानतळाच्या नव्या टर्मिनलचे उद्घाटन केले आणि जयपूर मेट्रो टप्पा 2 ची पायाभरणी केली — सुमारे ₹1.06 लाख कोटींच्या प्रकल्पांचा भाग. डिसेंबर 2024 मध्ये मध्य प्रदेशसोबत मान्य झालेल्या रामजल सेतू नदीजोड प्रकल्पाचा उद्देश पूर्वेकडील जिल्ह्यांपर्यंत पाणी पोहोचवणे हा आहे. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pmindia", "newsonair"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Delhi–Mumbai Expressway — Rajasthan sections status", "दिल्ली–मुंबई एक्सप्रेसवे — राजस्थान खंडों की स्थिति", "दिल्ली–मुंबई द्रुतगती मार्ग — राजस्थानातील टप्प्यांची स्थिती"), "nhai", "NHAI project status."),
        (L("Shekhawati water pipeline (Hathnikund) — approvals", "शेखावाटी जल पाइपलाइन (हथिनीकुंड) — स्वीकृतियाँ", "शेखावटी जलवाहिनी (हथनीकुंड) — मंजुऱ्या"), "india-gov", "State Water Resources Department."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Jaipur International Airport is the main air gateway, with airports also at Udaipur, Jodhpur, Jaisalmer, Bikaner and Kishangarh. Jaipur is the headquarters of the North Western Railway, and the Western Dedicated Freight Corridor crosses the State on its way from Delhi to the Gujarat ports. The Delhi–Mumbai Expressway runs through eastern Rajasthan, and national highways link Jaipur with Delhi, Agra, Ahmedabad and the west. Jaipur has a metro line, with a second phase begun in 2026. Tourist trains such as the Palace on Wheels have long been a Rajasthan speciality.",
        "जयपुर अंतरराष्ट्रीय हवाई अड्डा मुख्य हवाई द्वार है, और उदयपुर, जोधपुर, जैसलमेर, बीकानेर और किशनगढ़ में भी हवाई अड्डे हैं। जयपुर उत्तर पश्चिम रेलवे का मुख्यालय है, और पश्चिमी समर्पित माल गलियारा दिल्ली से गुजरात के बंदरगाहों तक जाते हुए राज्य को पार करता है। दिल्ली–मुंबई एक्सप्रेसवे पूर्वी राजस्थान से होकर जाता है, और राष्ट्रीय राजमार्ग जयपुर को दिल्ली, आगरा, अहमदाबाद और पश्चिम से जोड़ते हैं। जयपुर में एक मेट्रो लाइन है, और 2026 में दूसरा चरण शुरू हुआ। पैलेस ऑन व्हील्स जैसी पर्यटक रेलें लंबे समय से राजस्थान की विशेषता हैं।",
        "जयपूर आंतरराष्ट्रीय विमानतळ हे मुख्य हवाई प्रवेशद्वार आहे, आणि उदयपूर, जोधपूर, जैसलमेर, बिकानेर व किशनगड येथेही विमानतळ आहेत. जयपूर हे उत्तर पश्चिम रेल्वेचे मुख्यालय आहे, आणि पश्चिम समर्पित मालवाहतूक मार्गिका दिल्लीहून गुजरातच्या बंदरांकडे जाताना राज्य ओलांडते. दिल्ली–मुंबई द्रुतगती मार्ग पूर्व राजस्थानातून जातो, आणि राष्ट्रीय महामार्ग जयपूरला दिल्ली, आग्रा, अहमदाबाद व पश्चिमेशी जोडतात. जयपूरमध्ये एक मेट्रो मार्गिका आहे, आणि 2026 मध्ये दुसरा टप्पा सुरू झाला. पॅलेस ऑन व्हील्ससारख्या पर्यटक गाड्या दीर्घकाळापासून राजस्थानची खासियत आहेत."),
        conf="Editorial"),
    lst("airports", [
        it3("jai", "Jaipur International Airport", "जयपुर अंतरराष्ट्रीय हवाई अड्डा", "जयपूर आंतरराष्ट्रीय विमानतळ", m=("JAI", "JAI", "JAI")),
        it3("udr", "Udaipur (Maharana Pratap Airport)", "उदयपुर (महाराणा प्रताप हवाई अड्डा)", "उदयपूर (महाराणा प्रताप विमानतळ)", m=("UDR", "UDR", "UDR")),
        it3("jdh", "Jodhpur", "जोधपुर", "जोधपूर", m=("JDH", "JDH", "JDH")),
        it3("jsa", "Jaisalmer", "जैसलमेर", "जैसलमेर", m=("JSA", "JSA", "JSA")),
        it3("bkb", "Bikaner (Nal)", "बीकानेर (नाल)", "बिकानेर (नाल)", m=("BKB", "BKB", "BKB")),
        it3("kqh", "Kishangarh (Ajmer)", "किशनगढ़ (अजमेर)", "किशनगड (अजमेर)", m=("KQH", "KQH", "KQH")),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Sunny, open and lightly populated, western Rajasthan has become one of India's main centres of renewable energy: the Bhadla solar park in Jodhpur district is among the largest in the world, and wind farms stand in Jaisalmer and Barmer. Coal and lignite stations at Suratgarh, Kota, Chhabra, Kalisindh, Barsingsar and Giral, and the Rajasthan Atomic Power Station at Rawatbhata, supply firm power. Transmission corridors (Green Energy Corridors) carry renewable power to other States.",
        "धूप वाला, खुला और कम आबादी वाला पश्चिमी राजस्थान भारत में अक्षय ऊर्जा के मुख्य केंद्रों में बन गया है: जोधपुर ज़िले का भड़ला सौर पार्क दुनिया के सबसे बड़े सौर पार्कों में है, और जैसलमेर और बाड़मेर में पवन फ़ार्म हैं। सूरतगढ़, कोटा, छबड़ा, कालीसिंध, बरसिंगसर और गिरल के कोयला व लिग्नाइट संयंत्र, और रावतभाटा का राजस्थान परमाणु बिजलीघर स्थिर बिजली देते हैं। पारेषण गलियारे (ग्रीन एनर्जी कॉरिडोर) अक्षय बिजली को दूसरे राज्यों तक ले जाते हैं।",
        "भरपूर ऊन, मोकळा व विरळ लोकवस्तीचा पश्चिम राजस्थान भारतातील अक्षय ऊर्जेच्या मुख्य केंद्रांपैकी एक बनला आहे: जोधपूर जिल्ह्यातील भडला सौर उद्यान जगातील सर्वांत मोठ्या सौर उद्यानांपैकी आहे, आणि जैसलमेर व बाडमेरमध्ये पवन प्रकल्प आहेत. सुरतगड, कोटा, छबडा, कालीसिंध, बरसिंगसर व गिरल येथील कोळसा व लिग्नाइट केंद्रे, आणि रावतभाटा येथील राजस्थान अणुऊर्जा केंद्र स्थिर वीज देतात. पारेषण मार्गिका (ग्रीन एनर्जी कॉरिडॉर) अक्षय वीज इतर राज्यांपर्यंत नेतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Solar and wind capacity", "सौर और पवन क्षमता", "सौर व पवन क्षमता"), "mnre", "MNRE state-wise RE capacity."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Jaipur is the State's main centre for IT and start-ups, with a technology park at Sitapura and a growing number of software and BPO firms; the Bhiwadi–Neemrana belt near Delhi hosts electronics and manufacturing companies. The State has used digital platforms for public services, and Kota — known across India for coaching students for entrance examinations — has a large online-education industry.",
        "जयपुर राज्य में आईटी और स्टार्टअप का मुख्य केंद्र है, जहाँ सीतापुरा में प्रौद्योगिकी पार्क और बढ़ती संख्या में सॉफ़्टवेयर व बीपीओ कंपनियाँ हैं; दिल्ली के पास भिवाड़ी–नीमराना पट्टी में इलेक्ट्रॉनिक्स और विनिर्माण कंपनियाँ हैं। राज्य ने सार्वजनिक सेवाओं के लिए डिजिटल मंचों का उपयोग किया है, और प्रवेश परीक्षाओं की कोचिंग के लिए देश भर में प्रसिद्ध कोटा में बड़ा ऑनलाइन-शिक्षा उद्योग है।",
        "जयपूर हे राज्यातील आयटी व स्टार्टअपचे मुख्य केंद्र आहे — सीतापुरा येथे तंत्रज्ञान पार्क आणि वाढत्या संख्येने सॉफ्टवेअर व बीपीओ कंपन्या; दिल्लीजवळील भिवाडी–नीमराणा पट्ट्यात इलेक्ट्रॉनिक्स व उत्पादन कंपन्या आहेत. राज्याने सार्वजनिक सेवांसाठी डिजिटल व्यासपीठांचा वापर केला आहे, आणि प्रवेश परीक्षांच्या शिकवणीसाठी देशभर प्रसिद्ध असलेल्या कोट्यात मोठा ऑनलाइन-शिक्षण उद्योग आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Rajasthan circle)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("RJ", NAME)
module(R, "education", [
    prose("p1", L(
        "Rajasthan's higher-education gross enrolment ratio (ages 18–23) was 28.6% in 2021-22 in AISHE, close to the national 28.4%; men's GER (29.0%) was a little above women's (28.1%). With 90 universities and 3,934 colleges, the State has one of the largest higher-education systems in India. Literacy at the 2011 Census was 66.1%, with a wide gap between men and women.\n\nKota is India's best-known centre for coaching students for engineering and medical entrance examinations. National institutions include IIT Jodhpur, MNIT Jaipur, IIM Udaipur, BITS Pilani, AIIMS Jodhpur, the Central University of Rajasthan at Kishangarh and NLU Jodhpur; the University of Rajasthan in Jaipur dates from 1947.",
        "एआईएसएचई के अनुसार 2021-22 में राजस्थान का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) 28.6% था, जो राष्ट्रीय 28.4% के क़रीब है; पुरुषों का जीईआर (29.0%) महिलाओं (28.1%) से थोड़ा अधिक था। 90 विश्वविद्यालयों और 3,934 कॉलेजों के साथ राज्य की उच्च शिक्षा प्रणाली भारत की सबसे बड़ी प्रणालियों में है। 2011 की जनगणना में साक्षरता 66.1% थी, और पुरुषों व महिलाओं के बीच बड़ा अंतर था।\n\nकोटा इंजीनियरिंग और मेडिकल प्रवेश परीक्षाओं की कोचिंग का भारत का सबसे प्रसिद्ध केंद्र है। राष्ट्रीय संस्थानों में आईआईटी जोधपुर, एमएनआईटी जयपुर, आईआईएम उदयपुर, बिट्स पिलानी, एम्स जोधपुर, किशनगढ़ में राजस्थान केंद्रीय विश्वविद्यालय और एनएलयू जोधपुर हैं; जयपुर का राजस्थान विश्वविद्यालय 1947 का है।",
        "एआयएसएचईनुसार 2021-22 मध्ये राजस्थानचे उच्चशिक्षणातील एकूण नोंदणी गुणोत्तर (18–23 वय) 28.6% होते — राष्ट्रीय 28.4% च्या जवळ; पुरुषांचे जीईआर (29.0%) स्त्रियांपेक्षा (28.1%) किंचित जास्त होते. 90 विद्यापीठे व 3,934 महाविद्यालयांसह राज्याची उच्चशिक्षण व्यवस्था भारतातील सर्वांत मोठ्यांपैकी आहे. 2011 च्या जनगणनेत साक्षरता 66.1% होती, आणि पुरुष व स्त्रियांमध्ये मोठी तफावत होती.\n\nकोटा हे अभियांत्रिकी व वैद्यकीय प्रवेश परीक्षांच्या शिकवणीचे भारतातील सर्वांत प्रसिद्ध केंद्र आहे. राष्ट्रीय संस्थांत आयआयटी जोधपूर, एमएनआयटी जयपूर, आयआयएम उदयपूर, बिट्स पिलानी, एम्स जोधपूर, किशनगड येथील राजस्थान केंद्रीय विद्यापीठ व एनएलयू जोधपूर यांचा समावेश आहे; जयपूरचे राजस्थान विद्यापीठ 1947 चे आहे."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("iitj", "IIT Jodhpur", "आईआईटी जोधपुर", "आयआयटी जोधपूर", m=("Jodhpur", "जोधपुर", "जोधपूर")),
        it3("bits", "BITS Pilani", "बिट्स पिलानी", "बिट्स पिलानी", m=("Pilani, Jhunjhunu", "पिलानी, झुंझुनूँ", "पिलानी, झुंझुनू")),
        it3("mnit", "MNIT Jaipur", "एमएनआईटी जयपुर", "एमएनआयटी जयपूर", m=("Jaipur", "जयपुर", "जयपूर")),
        it3("iimu", "IIM Udaipur", "आईआईएम उदयपुर", "आयआयएम उदयपूर", m=("Udaipur", "उदयपुर", "उदयपूर")),
        it3("aiimsj", "AIIMS Jodhpur", "एम्स जोधपुर", "एम्स जोधपूर", m=("Jodhpur", "जोधपुर", "जोधपूर")),
        it3("uor", "University of Rajasthan", "राजस्थान विश्वविद्यालय", "राजस्थान विद्यापीठ", m=("Jaipur, 1947", "जयपुर, 1947", "जयपूर, 1947")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Literacy by sex (Census 2011)", "लिंग के अनुसार साक्षरता (जनगणना 2011)", "लिंगनिहाय साक्षरता (जनगणना 2011)"), "census", "Primary Census Abstract."),
    ]),
])

# ---------------- O. Health ----------------
module(R, "health", [
    prose("p1", L(
        "Rajasthan's health indicators have improved steadily but remain below the national average in places. The infant mortality rate fell from 55 per 1,000 live births in 2010 to 32 in 2020 (India 28), and the birth rate from 26.7 to 23.5 per 1,000. Life expectancy at birth was 68.7 years in 2014-18 — 71.6 for women and 66.5 for men. Institutional births reached 94.9% in NFHS-5, and the share of stunted children under five fell from 39.1% to 31.8% between NFHS-4 and NFHS-5.\n\nThe State runs large public health insurance and free-medicine schemes. SMS Medical College and Hospital in Jaipur is the largest public hospital, and AIIMS Jodhpur is a national institute.",
        "राजस्थान के स्वास्थ्य संकेतकों में लगातार सुधार हुआ है, लेकिन कुछ जगह वे राष्ट्रीय औसत से नीचे हैं। शिशु मृत्यु दर 2010 में प्रति 1,000 जीवित जन्म पर 55 से घटकर 2020 में 32 हो गई (भारत 28), और जन्म दर प्रति 1,000 पर 26.7 से 23.5। 2014-18 में जन्म के समय जीवन प्रत्याशा 68.7 वर्ष थी — महिलाओं की 71.6 और पुरुषों की 66.5। एनएफ़एचएस-5 में संस्थागत प्रसव 94.9% तक पहुँचे, और एनएफ़एचएस-4 से एनएफ़एचएस-5 के बीच पाँच वर्ष से कम आयु के ठिगने बच्चों का हिस्सा 39.1% से घटकर 31.8% हो गया।\n\nराज्य बड़ी सार्वजनिक स्वास्थ्य बीमा और मुफ़्त दवा योजनाएँ चलाता है। जयपुर का एसएमएस मेडिकल कॉलेज और अस्पताल सबसे बड़ा सार्वजनिक अस्पताल है, और एम्स जोधपुर राष्ट्रीय संस्थान है।",
        "राजस्थानच्या आरोग्य निर्देशकांत सातत्याने सुधारणा झाली आहे, पण काही ठिकाणी ते राष्ट्रीय सरासरीपेक्षा खाली आहेत. अर्भक मृत्युदर 2010 मध्ये दर 1,000 जिवंत जन्मांमागे 55 वरून 2020 मध्ये 32 (भारत 28) झाला, आणि जन्मदर दर 1,000 मागे 26.7 वरून 23.5. 2014-18 मध्ये जन्मतः आयुर्मान 68.7 वर्षे होते — स्त्रियांचे 71.6 व पुरुषांचे 66.5. एनएफएचएस-5 मध्ये संस्थात्मक प्रसूती 94.9% पर्यंत पोहोचल्या, आणि एनएफएचएस-4 ते एनएफएचएस-5 दरम्यान पाच वर्षांखालील खुज्या मुलांचा वाटा 39.1% वरून 31.8% झाला.\n\nराज्य मोठ्या सार्वजनिक आरोग्य विमा व मोफत औषध योजना चालवते. जयपूरचे एसएमएस वैद्यकीय महाविद्यालय व रुग्णालय हे सर्वांत मोठे सार्वजनिक रुग्णालय आहे, आणि एम्स जोधपूर ही राष्ट्रीय संस्था आहे."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(32, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(55, "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(23.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020 (death rate 5.6); 26.7 in 2010."), "number",
             previous=dp(26.7, "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(68.7, "years", "2014-18", "survey", "srs", ESI_LE, note="SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male 66.5, female 71.6)."), "number", "higher-is-better",
             national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("RJ"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin; the PIB summary used here lists only States that met the SDG target."),
        (L("Under-five mortality rate (SRS 2021)", "पाँच वर्ष से कम आयु की मृत्यु दर (एसआरएस 2021)", "पाच वर्षांखालील मृत्युदर (एसआरएस 2021)"), "srs", "SRS Statistical Report 2021."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("rj mod2 ok")
