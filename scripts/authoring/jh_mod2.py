"""Jharkhand modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-JH"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
CM = "https://www.newsonair.gov.in/hemant-soren-to-be-sworn-in-as-jharkhand-cm-tomorrow"
NOTE_JH = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 16 Oct 2026. "
           "FY2024-25 is the latest year published for Jharkhand and may be revised.")
mo = research("mospi_jh.json")
NAME = L("Jharkhand", "झारखंड", "झारखंड")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Jharkhand's culture is rooted in Adivasi traditions of nature worship, community dance and song. At Sarhul, villages honour the sal tree and the sacred grove; at Karma, young people dance around a branch of the karam tree; and at Sohrai, after the harvest, women paint houses with earth colours and cattle are worshipped. Group dances such as jhumar, domkach and paika, accompanied by the mandar drum and nagara, are performed at every festival. The Seraikela style of Chhau, a masked martial dance, is part of the Chhau tradition inscribed by UNESCO as intangible heritage. Sohrai and Khovar wall painting from Hazaribagh is a registered GI, and Paitkar scroll painting, Dokra metal casting and bamboo work are other crafts.\n\nWriters and scholars such as Ram Dayal Munda revived interest in tribal languages and music, and Nagpuri songs and films have a growing audience.",
        "झारखंड की संस्कृति प्रकृति पूजा, सामुदायिक नृत्य और गीत की आदिवासी परंपराओं में रची-बसी है। सरहुल पर गाँव साल वृक्ष और पवित्र उपवन का सम्मान करते हैं; करमा पर युवा करम वृक्ष की डाली के चारों ओर नाचते हैं; और फ़सल के बाद सोहराय पर महिलाएँ मिट्टी के रंगों से घर रंगती हैं और पशुओं की पूजा होती है। मांदर और नगाड़े के साथ झूमर, डोमकच और पाइका जैसे सामूहिक नृत्य हर त्योहार पर होते हैं। मुखौटा युक्त युद्ध-नृत्य छऊ की सरायकेला शैली यूनेस्को की अमूर्त धरोहर सूची में दर्ज छऊ परंपरा का हिस्सा है। हज़ारीबाग की सोहराय और खोवर भित्ति चित्रकला पंजीकृत जीआई है, और पैटकर पट-चित्रकला, ढोकरा धातु ढलाई और बाँस का काम अन्य शिल्प हैं।\n\nराम दयाल मुंडा जैसे लेखकों और विद्वानों ने जनजातीय भाषाओं और संगीत में रुचि को पुनर्जीवित किया, और नागपुरी गीतों और फ़िल्मों के श्रोता बढ़ रहे हैं।",
        "झारखंडची संस्कृती निसर्गपूजा, सामूहिक नृत्य व गाण्यांच्या आदिवासी परंपरांत रुजलेली आहे. सरहुलला गावे साल वृक्ष व पवित्र देवराईचा सन्मान करतात; करमाला तरुण करम वृक्षाच्या फांदीभोवती नाचतात; आणि सुगीनंतर सोहरायला स्त्रिया मातीच्या रंगांनी घरे रंगवतात व गुरांची पूजा होते. मांदर व नगाऱ्याच्या साथीने झुमर, डोमकच व पाईका यांसारखी सामूहिक नृत्ये प्रत्येक सणाला होतात. मुखवटाधारी युद्धनृत्य छाऊची सरायकेला शैली युनेस्कोच्या अमूर्त वारसा यादीत नोंदलेल्या छाऊ परंपरेचा भाग आहे. हजारीबागची सोहराय व खोवर भित्तिचित्रकला नोंदणीकृत जीआय आहे, आणि पैटकर पट-चित्रकला, ढोकरा धातू ओतकाम व बांबूकाम या इतर हस्तकला आहेत.\n\nराम दयाल मुंडा यांसारख्या लेखक व विद्वानांनी आदिवासी भाषा व संगीतातील रुची पुन्हा जागवली, आणि नागपुरी गाणी व चित्रपटांचा प्रेक्षकवर्ग वाढत आहे."),
        conf="Editorial"),
    lst("festivals", [
        fest("sarhul", "Sarhul", "सरहुल", "सरहुल", ("March–April", "मार्च–अप्रैल", "मार्च–एप्रिल"),
             ("Spring festival of the sal blossom and the sacred grove; processions in Ranchi.", "साल के फूल और पवित्र उपवन का वसंत उत्सव; रांची में शोभायात्राएँ।", "सालच्या बहराचा व पवित्र देवराईचा वसंतोत्सव; रांचीत मिरवणुका.")),
        fest("karma", "Karma", "करमा", "करमा", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Night-long dancing around a karam branch, for prosperity and siblings' well-being.", "समृद्धि और भाई-बहनों के कल्याण के लिए करम की डाली के चारों ओर रात भर नृत्य।", "समृद्धी व भावंडांच्या कल्याणासाठी करमच्या फांदीभोवती रात्रभर नृत्य.")),
        fest("sohrai", "Sohrai", "सोहराय", "सोहराय", ("October–November", "अक्टूबर–नवंबर", "ऑक्टोबर–नोव्हेंबर"),
             ("Harvest and cattle festival; houses are painted with Sohrai art.", "फ़सल और पशुओं का त्योहार; घरों पर सोहराय चित्र बनते हैं।", "सुगी व गुरांचा सण; घरांवर सोहराय चित्रे काढली जातात.")),
        fest("tusu", "Tusu Parab", "टुसू परब", "टुसू परब", ("Mid-January", "मध्य जनवरी", "जानेवारीच्या मध्यात"),
             ("Harvest festival of the south-east, with songs and colourful chaudals floated in rivers.", "दक्षिण-पूर्व का फ़सल उत्सव, गीतों और नदियों में बहाए जाने वाले रंगीन चौड़लों के साथ।", "आग्नेयेकडील सुगीचा सण, गाणी व नद्यांत सोडल्या जाणाऱ्या रंगीत चौडलांसह.")),
        fest("shravani", "Shravani Mela", "श्रावणी मेला", "श्रावणी मेळा", ("July–August", "जुलाई–अगस्त", "जुलै–ऑगस्ट"),
             ("Kanwariyas carry Ganga water from Sultanganj to Baidyanath Dham, Deoghar.", "कांवड़िये सुल्तानगंज से बैद्यनाथ धाम, देवघर तक गंगाजल लाते हैं।", "कावडिये सुलतानगंजहून बैद्यनाथ धाम, देवघरपर्यंत गंगाजल आणतात.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("chhau", "Seraikela Chhau", "सरायकेला छऊ", "सरायकेला छाऊ"), it3("sohrai", "Sohrai–Khovar painting", "सोहराय–खोवर चित्रकला", "सोहराय–खोवर चित्रकला"),
        it3("paitkar", "Paitkar painting", "पैटकर चित्रकला", "पैटकर चित्रकला"), it3("jhumar", "Jhumar dance", "झूमर नृत्य", "झुमर नृत्य"),
        it3("dokra", "Dokra metal craft", "ढोकरा धातु शिल्प", "ढोकरा धातू हस्तकला"), it3("mandar", "Mandar and nagara drums", "मांदर और नगाड़ा", "मांदर व नगारा"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("dhuska", "Dhuska", "धुस्का", "धुस्का", d=("Deep-fried rice-and-lentil bread, eaten with potato or chickpea curry.", "चावल-दाल की तली रोटी, आलू या चने की करी के साथ।", "तांदूळ-डाळीची तळलेली भाकरी, बटाटा किंवा हरभऱ्याच्या रश्श्यासह.")),
        it3("pitha", "Pitha", "पीठा", "पिठा", d=("Steamed rice dumplings made at festivals.", "त्योहारों पर बनने वाले भाप में पके चावल के पीठे।", "सणांना बनवले जाणारे वाफवलेले तांदळाचे पिठे.")),
        it3("rugra", "Rugra", "रुगड़ा", "रुगडा", d=("Wild monsoon mushrooms cooked as a curry.", "मानसूनी जंगली मशरूम की सब्ज़ी।", "पावसाळी रानअळंबीची भाजी.")),
        it3("bamboo", "Bamboo shoots (karil)", "बाँस की कोंपलें (करील)", "बांबूचे कोंब (करील)", d=("Pickled or cooked in the monsoon.", "मानसून में अचार या सब्ज़ी के रूप में।", "पावसाळ्यात लोणचे किंवा भाजी म्हणून.")),
        it3("litti", "Litti chokha", "लिट्टी चोखा", "लिट्टी चोखा", d=("Shared with Bihar; roasted sattu-stuffed balls.", "बिहार के साथ साझा; सत्तू भरी सेंकी लिट्टी।", "बिहारसोबत सामायिक; सत्तू भरलेल्या भाजलेल्या लिट्ट्या.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("panchi", "Panchi and parhan", "पंछी और परहान", "पंछी व परहान", d=("Handwoven cotton wraps of Santhal and other women, often with red borders.", "संथाल और अन्य महिलाओं के हाथ से बुने सूती वस्त्र, अक्सर लाल किनारी वाले।", "संथाल व इतर स्त्रियांची हातमागावरील सुती वस्त्रे, अनेकदा लाल काठाची.")),
        it3("karya", "Karya and bhagwan", "करया और भगवान", "करया व भगवान", d=("Traditional men's loincloth and wrap in villages.", "गाँवों में पुरुषों का पारंपरिक वस्त्र।", "गावांत पुरुषांचे पारंपरिक वस्त्र.")),
        it3("tussar", "Tussar silk", "तसर रेशम", "टसर रेशीम", d=("Jharkhand is a leading producer of tussar silk.", "झारखंड तसर रेशम का अग्रणी उत्पादक है।", "झारखंड हा टसर रेशमाचा आघाडीचा उत्पादक आहे.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; mine = 100 * g["mining"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["JH"]; lf = AP["plfs_lfpr_2025"]["JH"]
module(R, "economy", [
    prose("p1", L(
        f"Jharkhand's GSDP at current prices was about ₹{cur['FY2024-25'][0]/1e5:.2f} lakh crore in FY2024-25, the latest year published for the State in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2024-25'][0])}. Manufacturing — led by steel at Jamshedpur and Bokaro, and by metals, cement and engineering — made up about {mfg:.0f}% of GSVA in FY2024-25, mining about {mine:.0f}%, and agriculture, livestock, forestry and fishing about {agri:.0f}%. The State holds a large share of India's coal, much of its iron ore, and deposits of copper, mica, bauxite and uranium; Coal India's subsidiaries Central Coalfields and Bharat Coking Coal are headquartered in Ranchi and Dhanbad. Most rural households still depend on rain-fed paddy and on forest produce such as lac, tussar silk and mahua.\n\nThe PLFS unemployment rate was {ur['2025']}% in 2025, and {lf['female']}% of women aged 15 and above were in the labour force.",
        f"मोस्पी शृंखला में राज्य के लिए प्रकाशित नवीनतम वर्ष, वित्त वर्ष 2024-25 में झारखंड का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2024-25'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2024-25'][0])}। वित्त वर्ष 2024-25 में विनिर्माण — जमशेदपुर और बोकारो के इस्पात तथा धातुओं, सीमेंट और इंजीनियरिंग के नेतृत्व में — जीएसवीए का लगभग {mfg:.0f}%, खनन लगभग {mine:.0f}%, और कृषि, पशुपालन, वानिकी व मत्स्य पालन लगभग {agri:.0f}% था। राज्य में भारत के कोयले का बड़ा हिस्सा, लौह अयस्क का बहुत बड़ा भाग, और ताँबा, अभ्रक, बॉक्साइट व यूरेनियम के भंडार हैं; कोल इंडिया की सहायक कंपनियों सेंट्रल कोलफ़ील्ड्स और भारत कोकिंग कोल के मुख्यालय रांची और धनबाद में हैं। अधिकांश ग्रामीण परिवार अब भी वर्षा-आधारित धान और लाख, तसर रेशम और महुआ जैसी वनोपज पर निर्भर हैं।\n\n2025 में पीएलएफ़एस बेरोज़गारी दर {ur['2025']}% थी, और 15 वर्ष से अधिक आयु की {lf['female']}% महिलाएँ श्रम बल में थीं।",
        f"मोस्पी मालिकेत राज्यासाठी प्रकाशित नवीनतम वर्ष, आ.व. 2024-25 मध्ये झारखंडचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2024-25'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2024-25'][0])}. आ.व. 2024-25 मध्ये उत्पादन उद्योग — जमशेदपूर व बोकारोचे पोलाद आणि धातू, सिमेंट व अभियांत्रिकी यांच्या नेतृत्वाखाली — जीएसव्हीएच्या सुमारे {mfg:.0f}%, खाणकाम सुमारे {mine:.0f}%, आणि शेती, पशुपालन, वनीकरण व मत्स्यव्यवसाय सुमारे {agri:.0f}% होते. राज्यात भारतातील कोळशाचा मोठा वाटा, लोहखनिजाचा बराच भाग, आणि तांबे, अभ्रक, बॉक्साइट व युरेनियमचे साठे आहेत; कोल इंडियाच्या उपकंपन्या सेंट्रल कोलफिल्ड्स व भारत कोकिंग कोल यांची मुख्यालये रांची व धनबाद येथे आहेत. बहुतेक ग्रामीण कुटुंबे अजूनही पावसावर अवलंबून भातशेती आणि लाख, टसर रेशीम व मोह यांसारख्या वनोपजावर अवलंबून आहेत.\n\n2025 मध्ये पीएलएफएस बेरोजगारी दर {ur['2025']}% होता, आणि 15 वर्षांवरील {lf['female']}% स्त्रिया श्रमशक्तीत होत्या."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_JH), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_JH), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_JH), "rupee", "higher-is-better",
             previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("JH", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    plfs_series("JH", NAME),
    lst("sectors-key", [
        it3("coal", "Coal", "कोयला", "कोळसा", d=("Jharia, Bokaro, Karanpura and Rajmahal coalfields.", "झरिया, बोकारो, कर्णपुरा और राजमहल कोयला क्षेत्र।", "झरिया, बोकारो, करणपुरा व राजमहल कोळसा क्षेत्रे.")),
        it3("steel", "Steel and metals", "इस्पात और धातु", "पोलाद व धातू", d=("Tata Steel at Jamshedpur; SAIL's Bokaro Steel Plant; copper at Ghatsila.", "जमशेदपुर में टाटा स्टील; सेल का बोकारो इस्पात संयंत्र; घाटशिला में ताँबा।", "जमशेदपूर येथे टाटा स्टील; सेलचा बोकारो पोलाद कारखाना; घाटशिला येथे तांबे.")),
        it3("ores", "Iron ore, mica and uranium", "लौह अयस्क, अभ्रक और यूरेनियम", "लोहखनिज, अभ्रक व युरेनियम", d=("Iron ore in West Singhbhum, mica in Koderma, uranium at Jaduguda.", "पश्चिमी सिंहभूम में लौह अयस्क, कोडरमा में अभ्रक, जादूगोड़ा में यूरेनियम।", "पश्चिम सिंहभूममध्ये लोहखनिज, कोडरमात अभ्रक, जादूगोडा येथे युरेनियम.")),
        it3("engineering", "Engineering and automobiles", "इंजीनियरिंग और ऑटोमोबाइल", "अभियांत्रिकी व वाहन उद्योग", d=("Heavy Engineering Corporation, Ranchi; vehicle plants and suppliers around Jamshedpur.", "हेवी इंजीनियरिंग कॉर्पोरेशन, रांची; जमशेदपुर के आसपास वाहन संयंत्र और आपूर्तिकर्ता।", "हेवी इंजिनिअरिंग कॉर्पोरेशन, रांची; जमशेदपूरभोवती वाहन कारखाने व पुरवठादार.")),
        it3("forest", "Forest produce", "वनोपज", "वनोपज", d=("Lac, tussar silk, mahua and kendu leaves.", "लाख, तसर रेशम, महुआ और केंदू पत्ते।", "लाख, टसर रेशीम, मोह व तेंदूपत्ता.")),
        it3("agri", "Paddy and vegetables", "धान और सब्ज़ियाँ", "भात व भाज्या", d=("Mostly rain-fed; vegetables around Ranchi.", "अधिकतर वर्षा-आधारित; रांची के आसपास सब्ज़ियाँ।", "बहुतांश पावसावर अवलंबून; रांचीभोवती भाजीपाला.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Coal production and share of India", "कोयला उत्पादन और भारत में हिस्सा", "कोळसा उत्पादन व भारतातील वाटा"), "india-gov", "Ministry of Coal, Provisional Coal Statistics."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("GSDP for FY2025-26", "वित्त वर्ष 2025-26 का जीएसडीपी", "आ.व. 2025-26 चे जीएसडीपी"), "mospi", "Not yet published for Jharkhand in the MoSPI series at access time."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Jharkhand has a unicameral legislature, the 81-member Legislative Assembly in Ranchi. The State elects 14 members to the Lok Sabha and 6 to the Rajya Sabha. Large parts of the State are Fifth Schedule areas, where the Constitution gives special protection to Scheduled Tribes, and a Tribes Advisory Council advises the government.\n\nIn the Assembly election of November 2024, the INDIA bloc led by the Jharkhand Mukti Morcha won 56 of the 81 seats and the BJP-led NDA 24 (News On AIR). Hemant Soren of the JMM was sworn in as Chief Minister on 28 November 2024 — his fourth term. Rabindra Nath Mahato (JMM) was re-elected Speaker, and Santosh Kumar Gangwar has been Governor since July 2024.",
        "झारखंड में एकसदनीय विधानमंडल है, रांची में 81 सदस्यों वाली विधानसभा। राज्य से लोकसभा के 14 और राज्यसभा के 6 सदस्य चुने जाते हैं। राज्य के बड़े भाग पाँचवीं अनुसूची के क्षेत्र हैं, जहाँ संविधान अनुसूचित जनजातियों को विशेष संरक्षण देता है, और एक जनजाति सलाहकार परिषद सरकार को सलाह देती है।\n\nनवंबर 2024 के विधानसभा चुनाव में झारखंड मुक्ति मोर्चा के नेतृत्व वाले इंडिया गठबंधन ने 81 में से 56 सीटें और भाजपा के नेतृत्व वाले राजग ने 24 सीटें जीतीं (न्यूज़ ऑन एआईआर)। झामुमो के हेमंत सोरेन ने 28 नवंबर 2024 को मुख्यमंत्री पद की शपथ ली — उनका चौथा कार्यकाल। रवींद्र नाथ महतो (झामुमो) फिर से अध्यक्ष चुने गए, और संतोष कुमार गंगवार जुलाई 2024 से राज्यपाल हैं।",
        "झारखंडमध्ये एकसदनी विधिमंडळ आहे, रांचीतील 81 सदस्यांची विधानसभा. राज्यातून लोकसभेवर 14 व राज्यसभेवर 6 सदस्य निवडले जातात. राज्याचे मोठे भाग पाचव्या अनुसूचीतील क्षेत्रे आहेत, जिथे संविधान अनुसूचित जमातींना विशेष संरक्षण देते, आणि जमाती सल्लागार परिषद सरकारला सल्ला देते.\n\nनोव्हेंबर 2024 च्या विधानसभा निवडणुकीत झारखंड मुक्ती मोर्चाच्या नेतृत्वाखालील इंडिया आघाडीने 81 पैकी 56 जागा व भाजपच्या नेतृत्वाखालील रालोआने 24 जागा जिंकल्या (न्यूज ऑन एआयआर). झामुमोचे हेमंत सोरेन यांनी 28 नोव्हेंबर 2024 रोजी मुख्यमंत्रिपदाची शपथ घेतली — त्यांची चौथी कारकीर्द. रवींद्र नाथ महतो (झामुमो) पुन्हा अध्यक्ष निवडले गेले, आणि संतोष कुमार गंगवार जुलै 2024 पासून राज्यपाल आहेत."),
        sources=["newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("noa", "News On AIR: Hemant Soren sworn in (28 Nov 2024)", "न्यूज़ ऑन एआईआर: हेमंत सोरेन ने शपथ ली (28 नवंबर 2024)", "न्यूज ऑन एआयआर: हेमंत सोरेन यांचा शपथविधी (28 नोव्हेंबर 2024)", url=CM, src="newsonair"),
        it3("portal", "Government of Jharkhand", "झारखंड सरकार", "झारखंड शासन", url="https://www.jharkhand.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2024 Assembly election — full party-wise result", "2024 विधानसभा चुनाव — दलवार पूरा परिणाम", "2024 विधानसभा निवडणूक — पक्षनिहाय संपूर्ण निकाल"), "eci", "ECI statistical report for Jharkhand 2024."),
        (L("Leader of Opposition — official notice", "नेता प्रतिपक्ष — आधिकारिक सूचना", "विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "Assembly secretariat."),
        (L("Fifth Schedule areas — list of districts and blocks", "पाँचवीं अनुसूची क्षेत्र — ज़िलों और प्रखंडों की सूची", "पाचवी अनुसूची क्षेत्रे — जिल्हे व तालुक्यांची यादी"), "tribal-affairs", "Ministry of Tribal Affairs."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Deoghar's airport, opened in July 2022 under the UDAN scheme, connected the pilgrimage town to Kolkata and other cities. Other large works in the State include new railway lines, expressways and highways across the plateau, and expansion of coal mining and power plants. Each card shows its source and the date it was checked.",
        "उड़ान योजना के तहत जुलाई 2022 में खुले देवघर हवाई अड्डे ने तीर्थ नगर को कोलकाता और अन्य शहरों से जोड़ा। राज्य के अन्य बड़े कार्यों में पठार भर में नई रेल लाइनें, एक्सप्रेसवे और राजमार्ग, और कोयला खनन व बिजली संयंत्रों का विस्तार शामिल है। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "उडान योजनेअंतर्गत जुलै 2022 मध्ये सुरू झालेल्या देवघर विमानतळाने तीर्थनगराला कोलकाता व इतर शहरांशी जोडले. राज्यातील इतर मोठ्या कामांत पठारभर नवे रेल्वेमार्ग, द्रुतगती मार्ग व महामार्ग आणि कोळसा खाणकाम व वीज प्रकल्पांचा विस्तार यांचा समावेश आहे. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["new-india-samachar"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("AIIMS Deoghar — completion date and cost", "एम्स देवघर — पूर्णता तिथि और लागत", "एम्स देवघर — पूर्णत्वाची तारीख व खर्च"), "mohfw", "Ministry of Health and Family Welfare."),
        (L("Jharia Master Plan (fire and subsidence) — status", "झरिया मास्टर प्लान (आग और धँसान) — स्थिति", "झरिया बृहत् आराखडा (आग व भूस्खलन) — स्थिती"), "india-gov", "Ministry of Coal."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Birsa Munda Airport at Ranchi is the State's main airport, and Deoghar has had commercial flights since 2022. Jharkhand's railways are among India's busiest for freight: the Dhanbad division carries vast quantities of coal, and lines from Howrah to Delhi and Mumbai cross the State through Dhanbad, Bokaro, Ranchi and Tatanagar (Jamshedpur). National highways link Ranchi with Jamshedpur, Hazaribagh and Patna, and the Grand Trunk Road crosses the north through Dhanbad and Hazaribagh district.",
        "रांची का बिरसा मुंडा हवाई अड्डा राज्य का मुख्य हवाई अड्डा है, और देवघर से 2022 से व्यावसायिक उड़ानें हैं। झारखंड की रेलें माल ढुलाई के लिए भारत की सबसे व्यस्त रेलों में हैं: धनबाद मंडल भारी मात्रा में कोयला ढोता है, और हावड़ा से दिल्ली और मुंबई की लाइनें धनबाद, बोकारो, रांची और टाटानगर (जमशेदपुर) से होकर राज्य को पार करती हैं। राष्ट्रीय राजमार्ग रांची को जमशेदपुर, हज़ारीबाग और पटना से जोड़ते हैं, और ग्रैंड ट्रंक रोड उत्तर में धनबाद और हज़ारीबाग ज़िले से होकर गुज़रती है।",
        "रांचीचे बिरसा मुंडा विमानतळ हे राज्याचे मुख्य विमानतळ आहे, आणि देवघरहून 2022 पासून व्यावसायिक उड्डाणे आहेत. झारखंडचे रेल्वेमार्ग मालवाहतुकीसाठी भारतातील सर्वांत व्यस्त मार्गांपैकी आहेत: धनबाद विभाग प्रचंड प्रमाणात कोळसा वाहून नेतो, आणि हावडा ते दिल्ली व मुंबई मार्ग धनबाद, बोकारो, रांची व टाटानगर (जमशेदपूर) मार्गे राज्य ओलांडतात. राष्ट्रीय महामार्ग रांचीला जमशेदपूर, हजारीबाग व पाटण्याशी जोडतात, आणि ग्रँड ट्रंक रोड उत्तरेत धनबाद व हजारीबाग जिल्ह्यातून जातो."),
        conf="Editorial"),
    lst("airports", [
        it3("ixr", "Birsa Munda Airport, Ranchi", "बिरसा मुंडा हवाई अड्डा, रांची", "बिरसा मुंडा विमानतळ, रांची", m=("IXR", "IXR", "IXR")),
        it3("dgh", "Deoghar Airport", "देवघर हवाई अड्डा", "देवघर विमानतळ", m=("DGH", "DGH", "DGH")),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Coal is the base of Jharkhand's energy. Thermal stations of the Damodar Valley Corporation at Bokaro, Chandrapura and Koderma, the Maithon plant, Tenughat, Tata Power's Jojobera plant and the Patratu plant being rebuilt as a joint venture of NTPC and the State supply power both within the State and to the eastern grid. The DVC also built hydro-electric dams at Tilaiya, Maithon and Panchet. Solar capacity is small but growing, including floating solar on reservoirs.",
        "कोयला झारखंड की ऊर्जा का आधार है। बोकारो, चंद्रपुरा और कोडरमा में दामोदर घाटी निगम के तापीय केंद्र, मैथन संयंत्र, तेनुघाट, टाटा पावर का जोजोबेरा संयंत्र और एनटीपीसी व राज्य के संयुक्त उद्यम के रूप में पुनर्निर्मित हो रहा पतरातू संयंत्र राज्य के भीतर और पूर्वी ग्रिड दोनों को बिजली देते हैं। डीवीसी ने तिलैया, मैथन और पंचेत में जलविद्युत बाँध भी बनाए। सौर क्षमता छोटी लेकिन बढ़ रही है, जिसमें जलाशयों पर तैरते सौर संयंत्र भी हैं।",
        "कोळसा हा झारखंडच्या ऊर्जेचा पाया आहे. बोकारो, चंद्रपुरा व कोडरमा येथील दामोदर खोरे महामंडळाची औष्णिक केंद्रे, मैथन प्रकल्प, तेनुघाट, टाटा पॉवरचा जोजोबेरा प्रकल्प आणि एनटीपीसी व राज्याच्या संयुक्त उपक्रमातून पुन्हा उभारला जाणारा पतरातू प्रकल्प राज्यांतर्गत व पूर्व ग्रिडला वीज पुरवतात. डीव्हीसीने तिलैया, मैथन व पंचेत येथे जलविद्युत धरणेही बांधली. सौरक्षमता लहान पण वाढती आहे, ज्यात जलाशयांवरील तरंगते सौर प्रकल्पही आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Jharkhand's technology sector is modest, centred on Ranchi and Jamshedpur, where engineering colleges and industrial companies employ IT staff. The State runs land records, certificates and welfare schemes online, and common service centres help people in villages use digital services.",
        "झारखंड का प्रौद्योगिकी क्षेत्र साधारण है, जो रांची और जमशेदपुर पर केंद्रित है, जहाँ इंजीनियरिंग कॉलेज और औद्योगिक कंपनियाँ आईटी कर्मचारी रखती हैं। राज्य भूमि अभिलेख, प्रमाणपत्र और कल्याणकारी योजनाएँ ऑनलाइन चलाता है, और सामान्य सेवा केंद्र गाँवों में लोगों को डिजिटल सेवाओं के उपयोग में मदद करते हैं।",
        "झारखंडचे तंत्रज्ञान क्षेत्र मर्यादित आहे, रांची व जमशेदपूरवर केंद्रित, जिथे अभियांत्रिकी महाविद्यालये व औद्योगिक कंपन्या आयटी कर्मचारी नेमतात. राज्य जमिनीच्या नोंदी, प्रमाणपत्रे व कल्याणकारी योजना ऑनलाइन चालवते, आणि सामायिक सेवा केंद्रे गावांतील लोकांना डिजिटल सेवा वापरण्यास मदत करतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Bihar circle, which includes Jharkhand)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("JH", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["JH"]
module(R, "education", [
    prose("p1", L(
        f"Jharkhand's higher-education gross enrolment ratio (ages 18–23) rose from 15.9% in 2017-18 to 18.6% in 2021-22 in AISHE, still well below the national 28.4%; women's GER ({gf}%) was slightly above men's ({gm}%). The State had 33 universities but only 366 colleges — few for its population. Literacy rose from 53.6% in 2001 to 66.4% in 2011.\n\nJharkhand has several old and well-known institutions: the Indian School of Mines at Dhanbad (1926, now IIT (ISM) Dhanbad), BIT Mesra (1955), XLRI Jamshedpur (1949) and Ranchi University (1960). IIM Ranchi, NIT Jamshedpur, the Central University of Jharkhand, Birsa Agricultural University and the National University of Study and Research in Law are others.",
        f"एआईएसएचई के अनुसार झारखंड का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) 2017-18 के 15.9% से बढ़कर 2021-22 में 18.6% हुआ, जो अब भी राष्ट्रीय 28.4% से काफ़ी कम है; महिलाओं का जीईआर ({gf}%) पुरुषों ({gm}%) से थोड़ा अधिक था। राज्य में 33 विश्वविद्यालय थे लेकिन केवल 366 कॉलेज — इसकी जनसंख्या के हिसाब से कम। साक्षरता 2001 के 53.6% से बढ़कर 2011 में 66.4% हुई।\n\nझारखंड में कई पुराने और प्रसिद्ध संस्थान हैं: धनबाद का इंडियन स्कूल ऑफ़ माइंस (1926, अब आईआईटी (आईएसएम) धनबाद), बीआईटी मेसरा (1955), एक्सएलआरआई जमशेदपुर (1949) और रांची विश्वविद्यालय (1960)। आईआईएम रांची, एनआईटी जमशेदपुर, झारखंड केंद्रीय विश्वविद्यालय, बिरसा कृषि विश्वविद्यालय और राष्ट्रीय विधि अध्ययन एवं अनुसंधान विश्वविद्यालय अन्य संस्थान हैं।",
        f"एआयएसएचईनुसार झारखंडचे उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) 2017-18 मधील 15.9% वरून 2021-22 मध्ये 18.6% झाले, जे अजूनही राष्ट्रीय 28.4% पेक्षा बरेच कमी आहे; स्त्रियांचे जीईआर ({gf}%) पुरुषांपेक्षा ({gm}%) किंचित अधिक होते. राज्यात 33 विद्यापीठे होती पण केवळ 366 महाविद्यालये — लोकसंख्येच्या मानाने कमी. साक्षरता 2001 मधील 53.6% वरून 2011 मध्ये 66.4% झाली.\n\nझारखंडमध्ये अनेक जुन्या व प्रसिद्ध संस्था आहेत: धनबादचे इंडियन स्कूल ऑफ माइन्स (1926, आता आयआयटी (आयएसएम) धनबाद), बीआयटी मेसरा (1955), एक्सएलआरआय जमशेदपूर (1949) व रांची विद्यापीठ (1960). आयआयएम रांची, एनआयटी जमशेदपूर, झारखंड केंद्रीय विद्यापीठ, बिरसा कृषी विद्यापीठ व राष्ट्रीय विधी अध्ययन व संशोधन विद्यापीठ या इतर संस्था आहेत."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("ism", "IIT (ISM) Dhanbad", "आईआईटी (आईएसएम) धनबाद", "आयआयटी (आयएसएम) धनबाद", m=("Dhanbad, 1926", "धनबाद, 1926", "धनबाद, 1926")),
        it3("bit", "BIT Mesra", "बीआईटी मेसरा", "बीआयटी मेसरा", m=("Ranchi, 1955", "रांची, 1955", "रांची, 1955")),
        it3("xlri", "XLRI", "एक्सएलआरआई", "एक्सएलआरआय", m=("Jamshedpur, 1949", "जमशेदपुर, 1949", "जमशेदपूर, 1949")),
        it3("ru", "Ranchi University", "रांची विश्वविद्यालय", "रांची विद्यापीठ", m=("Ranchi, 1960", "रांची, 1960", "रांची, 1960")),
        it3("iimr", "IIM Ranchi", "आईआईएम रांची", "आयआयएम रांची", m=("Ranchi", "रांची", "रांची")),
        it3("nitj", "NIT Jamshedpur", "एनआईटी जमशेदपुर", "एनआयटी जमशेदपूर", m=("Jamshedpur", "जमशेदपुर", "जमशेदपूर")),
        it3("cuj", "Central University of Jharkhand", "झारखंड केंद्रीय विश्वविद्यालय", "झारखंड केंद्रीय विद्यापीठ", m=("Ranchi", "रांची", "रांची")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Literacy by sex (Census 2011)", "लिंग के अनुसार साक्षरता (जनगणना 2011)", "लिंगनिहाय साक्षरता (जनगणना 2011)"), "census", "Primary Census Abstract."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["JH"]
module(R, "health", [
    prose("p1", L(
        f"Jharkhand's infant mortality rate fell from 42 per 1,000 live births in 2010 to 25 in 2020, below the national 28. The birth rate was 22.0 per 1,000 in 2020, among the higher rates in India, and the death rate 5.2. Child undernutrition remains severe: in NFHS-5, {n['stunted'][1]:.1f}% of children under five were stunted, {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight, though all three fell from NFHS-4. About {n['institutional_N5']:.1f}% of births took place in health facilities, well below the national 88.6%. Anaemia and diseases such as malaria in forest areas are continuing challenges.\n\nThe Rajendra Institute of Medical Sciences (RIMS) in Ranchi is the main referral hospital; AIIMS Deoghar, the Tata Main Hospital in Jamshedpur and the medical colleges at Dhanbad and Jamshedpur are other important centres.",
        f"झारखंड की शिशु मृत्यु दर 2010 में प्रति 1,000 जीवित जन्म पर 42 से घटकर 2020 में 25 हो गई, जो राष्ट्रीय 28 से कम है। 2020 में जन्म दर प्रति 1,000 पर 22.0 थी, जो भारत की ऊँची दरों में है, और मृत्यु दर 5.2। बाल कुपोषण अब भी गंभीर है: एनएफ़एचएस-5 में पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने, {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के थे, हालाँकि तीनों एनएफ़एचएस-4 से घटे। लगभग {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, जो राष्ट्रीय 88.6% से काफ़ी कम है। एनीमिया और वन क्षेत्रों में मलेरिया जैसी बीमारियाँ लगातार चुनौतियाँ हैं।\n\nरांची का राजेंद्र आयुर्विज्ञान संस्थान (रिम्स) मुख्य रेफ़रल अस्पताल है; एम्स देवघर, जमशेदपुर का टाटा मेन हॉस्पिटल और धनबाद व जमशेदपुर के मेडिकल कॉलेज अन्य महत्त्वपूर्ण केंद्र हैं।",
        f"झारखंडचा अर्भक मृत्युदर 2010 मध्ये दर 1,000 जिवंत जन्मांमागे 42 वरून 2020 मध्ये 25 वर आला, राष्ट्रीय 28 पेक्षा कमी. 2020 मध्ये जन्मदर दर 1,000 मागे 22.0 होता, भारतातील अधिक दरांपैकी, आणि मृत्युदर 5.2. बालकुपोषण अजूनही गंभीर आहे: एनएफएचएस-5 मध्ये पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी, {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची होती, तरी तिन्ही एनएफएचएस-4 पेक्षा घटले. सुमारे {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, राष्ट्रीय 88.6% पेक्षा बरेच कमी. रक्तक्षय व वनक्षेत्रांतील हिवतापासारखे आजार ही सततची आव्हाने आहेत.\n\nरांचीचे राजेंद्र आयुर्विज्ञान संस्थान (रिम्स) हे मुख्य संदर्भ रुग्णालय आहे; एम्स देवघर, जमशेदपूरचे टाटा मेन हॉस्पिटल आणि धनबाद व जमशेदपूरची वैद्यकीय महाविद्यालये ही इतर महत्त्वाची केंद्रे आहेत."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(25, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(42, "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(22.0, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020 (death rate 5.2); 25.3 in 2010."), "number",
             previous=dp(25.3, "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("dr", L("Death rate", "मृत्यु दर", "मृत्युदर"), dp(5.2, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020."), "number", "lower-is-better",
             previous=dp(7.0, "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(6.0, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("JH"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"), "srs", "SRS abridged life tables; Jharkhand is not listed separately in Economic Survey Table 8.1."),
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin; Jharkhand is reported within a combined group."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("jh mod2 ok")
