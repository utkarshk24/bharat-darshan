"""Meghalaya modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-ML"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_ML = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 25 Oct 2026. "
           "FY2024-25 is the latest year published for Meghalaya and may be revised.")
mo = research("mospi_ml.json")
C = research("census_b5plus.json")
NAME = L("Meghalaya", "मेघालय", "मेघालय")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Each of Meghalaya's main communities has its own traditions. The Khasi faith, Niam Khasi (Seng Khasi), and the Jaintia Niamtre honour a creator god and ancestral clans, and festivals such as Shad Suk Mynsiem and Ka Pomblang Nongkrem are danced in traditional dress and gold and silver ornaments. The Garo celebrate Wangala, a harvest thanksgiving to the sun god Saljong, with long rows of dancers and the beat of the dama drum. Most people are now Christian, and church choirs and gospel music are part of public life alongside Shillong's rock and blues scene. Cane and bamboo work, weaving and wooden crafts are made across the hills.",
        "मेघालय के प्रत्येक मुख्य समुदाय की अपनी परंपराएँ हैं। खासी धर्म, नियाम खासी (सेंग खासी), और जयंतिया नियामत्रे एक सृष्टिकर्ता ईश्वर और पूर्वज कुलों का सम्मान करते हैं, और शाद सुक मिनसिएम और का पोम्ब्लांग नोंगक्रेम जैसे त्योहारों में पारंपरिक वेशभूषा और सोने-चाँदी के आभूषणों में नृत्य होता है। गारो वांगला मनाते हैं, सूर्य देवता सलजोंग के प्रति फ़सल का धन्यवाद पर्व, नर्तकों की लंबी पंक्तियों और दामा ढोल की थाप के साथ। अधिकांश लोग अब ईसाई हैं, और चर्च गायक मंडलियाँ और गॉस्पेल संगीत शिलांग के रॉक और ब्लूज़ के साथ सार्वजनिक जीवन का हिस्सा हैं। बेंत और बाँस का काम, बुनाई और लकड़ी के शिल्प पूरी पहाड़ियों में बनते हैं।",
        "मेघालयातील प्रत्येक मुख्य समुदायाच्या स्वतःच्या परंपरा आहेत. खासी धर्म, नियाम खासी (सेंग खासी), व जयंतिया नियामत्रे एका सृष्टिकर्त्या देवाचा व पूर्वज कुळांचा आदर करतात, आणि शाद सुक मिनसिएम व का पोम्ब्लांग नोंगक्रेमसारख्या सणांत पारंपरिक पोशाख व सोन्या-चांदीच्या दागिन्यांत नृत्य होते. गारो वांगला साजरा करतात, सूर्यदेव सलजोंगप्रती सुगीचा कृतज्ञता सण, नर्तकांच्या लांब रांगा व दामा ढोलाच्या तालासह. बहुतेक लोक आता ख्रिस्ती आहेत, आणि चर्चमधील गायकवृंद व गॉस्पेल संगीत शिलाँगच्या रॉक व ब्लूजसोबत सार्वजनिक जीवनाचा भाग आहेत. वेत व बांबूकाम, विणकाम व लाकडी हस्तकला संपूर्ण टेकड्यांत बनतात."),
        conf="Editorial"),
    lst("festivals", [
        fest("suk", "Shad Suk Mynsiem", "शाद सुक मिनसिएम", "शाद सुक मिनसिएम", ("April", "अप्रैल", "एप्रिल"),
             ("Khasi 'dance of the joyful heart' at Weiking, Shillong.", "शिलांग के वाइकिंग में खासी 'प्रसन्न हृदय का नृत्य'।", "शिलाँगच्या वाइकिंग येथे खासी 'आनंदी हृदयाचे नृत्य'.")),
        fest("nongkrem", "Ka Pomblang Nongkrem", "का पोम्ब्लांग नोंगक्रेम", "का पोम्ब्लांग नोंगक्रेम", ("October–November", "अक्टूबर–नवंबर", "ऑक्टोबर–नोव्हेंबर"),
             ("Five-day festival of the Hima Khyrim at Smit.", "स्मित में हिमा ख्रिम का पाँच दिवसीय उत्सव।", "स्मित येथे हिमा ख्रिमचा पाच दिवसांचा उत्सव.")),
        fest("wangala", "Wangala", "वांगला", "वांगला", ("November", "नवंबर", "नोव्हेंबर"),
             ("Garo harvest festival; the '100 drums' gathering near Tura.", "गारो फ़सल उत्सव; तुरा के पास '100 ढोल' का आयोजन।", "गारो सुगीचा सण; तुराजवळ '100 ढोल' मेळावा.")),
        fest("behdienkhlam", "Behdienkhlam", "बेहदिएनख्लाम", "बेहदिएनख्लाम", ("July", "जुलाई", "जुलै"),
             ("Jaintia festival at Jowai to drive away disease.", "रोग दूर भगाने का जोवाई में जयंतिया त्योहार।", "रोगराई दूर करण्यासाठी जोवाई येथील जयंतिया सण.")),
        fest("christmas", "Christmas", "क्रिसमस", "नाताळ", ("December", "दिसंबर", "डिसेंबर"),
             ("Celebrated across the State with carols and lights.", "पूरे राज्य में कैरल और रोशनी के साथ मनाया जाता है।", "संपूर्ण राज्यात कॅरल व दिव्यांसह साजरा होतो.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("dama", "Dama and nagra drums", "दामा और नगाड़ा ढोल", "दामा व नगारा ढोल"), it3("duitara", "Duitara (Khasi string instrument)", "दुइतारा (खासी तंतु वाद्य)", "दुइतारा (खासी तंतुवाद्य)"),
        it3("cane", "Cane and bamboo work", "बेंत और बाँस का काम", "वेत व बांबूकाम"), it3("ryndia", "Ryndia (eri silk) weaving", "रिंदिया (एरी रेशम) बुनाई", "रिंदिया (एरी रेशीम) विणकाम"),
        it3("choir", "Choral and gospel music", "कोरल और गॉस्पेल संगीत", "समूहगान व गॉस्पेल संगीत"), it3("lyrnai", "Lyrnai pottery", "लिरनाई मिट्टी के बर्तन", "लिरनाई मातीची भांडी"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("jadoh", "Jadoh", "जादोह", "जादोह", d=("Khasi rice cooked with pork or chicken.", "सूअर या मुर्ग़े के मांस के साथ पका खासी चावल।", "डुकराचे किंवा कोंबडीचे मांस घालून शिजवलेला खासी भात.")),
        it3("dohneiiong", "Doh neiiong", "दोह नेइयोंग", "दोह नेइयोंग", d=("Pork cooked with black sesame.", "काले तिल के साथ पका सूअर का मांस।", "काळ्या तिळासह शिजवलेले डुकराचे मांस.")),
        it3("tungrymbai", "Tungrymbai", "तुंगरिम्बाई", "तुंगरिम्बाई", d=("Fermented soya bean paste.", "किण्वित सोयाबीन का पेस्ट।", "आंबवलेल्या सोयाबीनची चटणी.")),
        it3("nakham", "Nakham bitchi", "नाखाम बित्ची", "नाखाम बित्ची", d=("Garo soup of dried fish.", "सूखी मछली का गारो सूप।", "सुक्या माशांचे गारो सूप.")),
        it3("pukhlein", "Pukhlein", "पुखलेइन", "पुखलेइन", d=("Sweet fried rice-flour cake.", "चावल के आटे का मीठा तला केक।", "तांदळाच्या पिठाचा गोड तळलेला केक.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("jainsem", "Jainsem and dhara", "जैनसेम और धारा", "जैनसेम व धारा", d=("Draped dress worn by Khasi women.", "खासी महिलाओं द्वारा पहनी जाने वाली लिपटी पोशाक।", "खासी स्त्रिया परिधान करतात तो गुंडाळलेला पोशाख.")),
        it3("jymphong", "Jymphong", "जिम्फोंग", "जिम्फोंग", d=("Sleeveless coat of Khasi men.", "खासी पुरुषों का बिना आस्तीन का कोट।", "खासी पुरुषांचा बिनबाह्यांचा कोट.")),
        it3("dakmanda", "Dakmanda", "दकमांडा", "दकमांडा", d=("Woven wrap-around of Garo women.", "गारो महिलाओं का बुना लपेटने वाला वस्त्र।", "गारो स्त्रियांचे विणलेले गुंडाळायचे वस्त्र.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; trade = 100 * g["trade_hotels"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; mine = 100 * g["mining"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["ML"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["ML"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Meghalaya's GSDP at current prices was about ₹{inr(cur['FY2024-25'][0])} crore in FY2024-25, the latest year in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2024-25'][0])}. Agriculture, livestock and forestry contributed about {agri:.0f}% of GSVA — rice, potatoes, Khasi mandarins, pineapples, areca nut, black pepper, broom grass and the Lakadong turmeric of the Jaintia Hills, known for its high curcumin. Trade, hotels and restaurants made up about {trade:.0f}%, helped by tourism and cross-border trade with Bangladesh. Manufacturing was about {mfg:.0f}%, mainly cement plants in the Jaintia Hills and ferro-alloy and other units at Byrnihat on the Assam border; mining and quarrying, mostly limestone and coal, was about {mine:.0f}%, much reduced since unregulated coal mining was banned in 2014.\n\nThe PLFS unemployment rate was {ur['2025']}% in 2025 (national {ui['2025']}%), and {lf['female']}% of women aged 15 and above were in the labour force, far above the national {lfi['female']}%.",
        f"मोस्पी शृंखला के नवीनतम वर्ष, वित्त वर्ष 2024-25 में मेघालय का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{inr(cur['FY2024-25'][0])} करोड़ और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2024-25'][0])} था। कृषि, पशुपालन और वानिकी का जीएसवीए में योगदान लगभग {agri:.0f}% था — धान, आलू, खासी संतरे, अनानास, सुपारी, काली मिर्च, झाड़ू घास और जयंतिया पहाड़ियों की लाकाडोंग हल्दी, जो अपने उच्च करक्यूमिन के लिए जानी जाती है। व्यापार, होटल और रेस्तराँ का हिस्सा लगभग {trade:.0f}% था, जिसमें पर्यटन और बांग्लादेश के साथ सीमा पार व्यापार का योगदान है। विनिर्माण लगभग {mfg:.0f}% था, मुख्यतः जयंतिया पहाड़ियों के सीमेंट संयंत्र और असम सीमा पर बर्नीहाट की फ़ेरो-एलॉय और अन्य इकाइयाँ; खनन और उत्खनन, अधिकतर चूना पत्थर और कोयला, लगभग {mine:.0f}% था, जो 2014 में अनियमित कोयला खनन पर रोक के बाद बहुत घट गया।\n\nपीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी (राष्ट्रीय {ui['2025']}%), और 15 वर्ष से अधिक आयु की {lf['female']}% महिलाएँ श्रम बल में थीं, जो राष्ट्रीय {lfi['female']}% से बहुत अधिक है।",
        f"मोस्पी मालिकेतील नवीनतम वर्ष, आ.व. 2024-25 मध्ये मेघालयाचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{inr(cur['FY2024-25'][0])} कोटी व दरडोई एनएसडीपी ₹{inr(pc['FY2024-25'][0])} होते. शेती, पशुपालन व वनीकरणाचा जीएसव्हीएमध्ये वाटा सुमारे {agri:.0f}% होता — भात, बटाटे, खासी संत्री, अननस, सुपारी, काळी मिरी, झाडूचे गवत आणि जयंतिया टेकड्यांची लाकाडोंग हळद, जी उच्च कर्क्युमिनसाठी ओळखली जाते. व्यापार, हॉटेल व उपाहारगृहांचा वाटा सुमारे {trade:.0f}% होता, ज्यात पर्यटन व बांगलादेशशी सीमापार व्यापाराचा हातभार आहे. उत्पादन उद्योग सुमारे {mfg:.0f}% होता, मुख्यतः जयंतिया टेकड्यांतील सिमेंट कारखाने व आसाम सीमेवरील बर्नीहाट येथील फेरो-अलॉय व इतर उद्योग; खाणकाम व उत्खनन, बहुतांश चुनखडी व कोळसा, सुमारे {mine:.0f}% होते, जे 2014 मध्ये अनियंत्रित कोळसा खाणकामावर बंदी आल्यानंतर बरेच घटले.\n\nपीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता (राष्ट्रीय {ui['2025']}%), आणि 15 वर्षांवरील {lf['female']}% स्त्रिया श्रमशक्तीत होत्या, राष्ट्रीय {lfi['female']}% पेक्षा खूप जास्त."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_ML), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_ML), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_ML), "rupee", "higher-is-better",
             previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("ML", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    plfs_series("ML", NAME),
    lst("sectors-key", [
        it3("horti", "Horticulture and spices", "बाग़वानी और मसाले", "फलोत्पादन व मसाले", d=("Lakadong turmeric, Khasi mandarin, pineapple, ginger, pepper.", "लाकाडोंग हल्दी, खासी संतरा, अनानास, अदरक, काली मिर्च।", "लाकाडोंग हळद, खासी संत्रे, अननस, आले, मिरी.")),
        it3("cement", "Cement and minerals", "सीमेंट और खनिज", "सिमेंट व खनिजे", d=("Limestone-based cement plants in the Jaintia Hills.", "जयंतिया पहाड़ियों में चूना पत्थर आधारित सीमेंट संयंत्र।", "जयंतिया टेकड्यांतील चुनखडीवर आधारित सिमेंट कारखाने.")),
        it3("tourism", "Tourism", "पर्यटन", "पर्यटन", d=("Shillong, Sohra, Dawki, caves and root bridges.", "शिलांग, सोहरा, दावकी, गुफाएँ और जड़ पुल।", "शिलाँग, सोहरा, दावकी, गुहा व मुळांचे पूल.")),
        it3("trade", "Border trade", "सीमा व्यापार", "सीमाव्यापार", d=("Land customs stations and border haats with Bangladesh.", "बांग्लादेश के साथ भू-सीमा शुल्क केंद्र और सीमा हाट।", "बांगलादेशसोबत भू-सीमाशुल्क केंद्रे व सीमा हाट.")),
        it3("broom", "Broom grass and forest produce", "झाड़ू घास और वनोपज", "झाडूचे गवत व वनोपज", d=("Collected and sold from village forests.", "गाँव के वनों से एकत्र कर बेचा जाता है।", "गावांच्या जंगलांतून गोळा करून विकले जाते.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Lakadong turmeric curcumin content — official test data", "लाकाडोंग हल्दी में करक्यूमिन — आधिकारिक परीक्षण आँकड़े", "लाकाडोंग हळदीतील कर्क्युमिन — अधिकृत चाचणी आकडे"), "gi-registry", "GI application No. 741 / Spices Board."),
        (L("Tourist arrivals by year", "वर्षवार पर्यटक आगमन", "वर्षनिहाय पर्यटक आगमन"), "tourism", "Meghalaya Tourism Department."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Meghalaya has a unicameral, 60-member Legislative Assembly in Shillong, 55 of whose seats are reserved for Scheduled Tribes. Most of the State is under the Sixth Schedule of the Constitution, and three Autonomous District Councils — the Khasi Hills, Jaintia Hills and Garo Hills councils — make laws on land, forests, clan matters and the appointment of traditional chiefs. Meghalaya elects 2 members to the Lok Sabha (Shillong and Tura) and 1 to the Rajya Sabha.\n\nAfter the 2023 Assembly election, Conrad K. Sangma of the National People's Party was sworn in for a second term as Chief Minister on 7 March 2023, heading the Meghalaya Democratic Alliance coalition, with Prestone Tynsong and Sniawbhalang Dhar as Deputy Chief Ministers. Thomas A. Sangma was elected Speaker on 9 March 2023, and C. H. Vijayashankar has been Governor since 30 July 2024. The next Assembly election is due by early 2028.",
        "मेघालय में शिलांग में 60 सदस्यों वाली एकसदनीय विधानसभा है, जिसकी 55 सीटें अनुसूचित जनजातियों के लिए आरक्षित हैं। राज्य का अधिकांश भाग संविधान की छठी अनुसूची के अंतर्गत है, और तीन स्वायत्त ज़िला परिषदें — खासी हिल्स, जयंतिया हिल्स और गारो हिल्स परिषदें — भूमि, वन, कुल संबंधी मामलों और पारंपरिक मुखियाओं की नियुक्ति पर क़ानून बनाती हैं। मेघालय से लोकसभा के 2 (शिलांग और तुरा) और राज्यसभा का 1 सदस्य चुना जाता है।\n\n2023 के विधानसभा चुनाव के बाद नेशनल पीपुल्स पार्टी के कॉनराड के. संगमा ने 7 मार्च 2023 को मेघालय डेमोक्रेटिक अलायंस गठबंधन का नेतृत्व करते हुए दूसरी बार मुख्यमंत्री पद की शपथ ली, प्रेस्टोन तिनसोंग और स्नियावभलांग धर उपमुख्यमंत्री बने। थॉमस ए. संगमा 9 मार्च 2023 को अध्यक्ष चुने गए, और सी. एच. विजयशंकर 30 जुलाई 2024 से राज्यपाल हैं। अगला विधानसभा चुनाव 2028 की शुरुआत तक होना है।",
        "मेघालयात शिलाँग येथे 60 सदस्यांची एकसदनी विधानसभा आहे, जिच्या 55 जागा अनुसूचित जमातींसाठी राखीव आहेत. राज्याचा बहुतांश भाग संविधानाच्या सहाव्या अनुसूचीखाली आहे, आणि तीन स्वायत्त जिल्हा परिषदा — खासी हिल्स, जयंतिया हिल्स व गारो हिल्स परिषदा — जमीन, जंगल, कुळविषयक बाबी व पारंपरिक प्रमुखांच्या नेमणुकीवर कायदे करतात. मेघालयातून लोकसभेवर 2 (शिलाँग व तुरा) व राज्यसभेवर 1 सदस्य निवडला जातो.\n\n2023 च्या विधानसभा निवडणुकीनंतर नॅशनल पीपल्स पार्टीचे कॉनराड के. संगमा यांनी 7 मार्च 2023 रोजी मेघालय डेमोक्रॅटिक अलायन्स आघाडीचे नेतृत्व करत दुसऱ्यांदा मुख्यमंत्रिपदाची शपथ घेतली, प्रेस्टोन तिनसोंग व स्नियावभलांग धर उपमुख्यमंत्री झाले. थॉमस ए. संगमा 9 मार्च 2023 रोजी अध्यक्षपदी निवडले गेले, आणि सी. एच. विजयशंकर 30 जुलै 2024 पासून राज्यपाल आहेत. पुढील विधानसभा निवडणूक 2028 च्या सुरुवातीपर्यंत होणे अपेक्षित आहे."),
        sources=["morung-express", "ml-gov", "ml-governor"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("portal", "Government of Meghalaya", "मेघालय सरकार", "मेघालय शासन", url="https://meghalaya.gov.in", src="ml-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2023 Assembly election — party-wise result", "2023 विधानसभा चुनाव — दलवार परिणाम", "2023 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Meghalaya 2023."),
        (L("Chief Minister's swearing-in — official source", "मुख्यमंत्री का शपथ ग्रहण — आधिकारिक स्रोत", "मुख्यमंत्र्यांचा शपथविधी — अधिकृत स्रोत"), "ml-gov", "Replace the news report with the Government of Meghalaya notification."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "The Shillong–Silchar greenfield corridor, approved in April 2025 at ₹22,864 crore, is meant to cut travel time between Shillong and the Barak valley of Assam. Railway lines to Byrnihat and Shillong have been held up for years by local opposition and land issues; these and other works will be added as cards once their status is confirmed from official sources. Each card shows its source and the date it was checked.",
        "शिलांग–सिलचर ग्रीनफ़ील्ड कॉरिडोर, जिसे अप्रैल 2025 में ₹22,864 करोड़ की लागत पर स्वीकृति मिली, का उद्देश्य शिलांग और असम की बराक घाटी के बीच यात्रा समय घटाना है। बर्नीहाट और शिलांग तक रेल लाइनें स्थानीय विरोध और भूमि संबंधी मुद्दों के कारण वर्षों से रुकी हैं; आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर इन्हें और अन्य कार्यों को कार्ड के रूप में जोड़ा जाएगा। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "शिलाँग–सिलचर ग्रीनफिल्ड कॉरिडॉर, ज्याला एप्रिल 2025 मध्ये ₹22,864 कोटी खर्चास मंजुरी मिळाली, याचा उद्देश शिलाँग व आसाममधील बराक खोऱ्यातील प्रवासाचा वेळ कमी करणे हा आहे. बर्नीहाट व शिलाँगपर्यंतचे रेल्वेमार्ग स्थानिक विरोध व जमिनीच्या प्रश्नांमुळे वर्षानुवर्षे रखडले आहेत; अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर हे व इतर प्रकल्प कार्डे म्हणून जोडले जातील. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["swarajya", "the-week"], conf="Third-party verified"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Shillong–Silchar corridor — CCEA release and award status", "शिलांग–सिलचर कॉरिडोर — सीसीईए विज्ञप्ति और अनुबंध स्थिति", "शिलाँग–सिलचर कॉरिडॉर — सीसीईए प्रसिद्धिपत्रक व कंत्राट स्थिती"), "pib", "PIB release of 30 April 2025; NHIDCL award notices."),
        (L("Tetelia–Byrnihat railway — official status", "तेतेलिया–बर्नीहाट रेलवे — आधिकारिक स्थिति", "तेतेलिया–बर्नीहाट रेल्वे — अधिकृत स्थिती"), "railways", "Ministry of Railways / Parliament answer."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Roads carry almost all of Meghalaya's traffic. NH-6 (formerly NH-40 and NH-44) climbs from Guwahati to Shillong and continues through the Jaintia Hills to Silchar, and NH-62 and NH-217 serve the Garo Hills. Shillong airport at Umroi, about 30 km from the city, has small-aircraft flights, while most travellers use Guwahati airport, about three hours away; Tura has an airstrip at Baljek. The only railway station is Mendipathar in North Garo Hills, linked to Assam since 2014. Shared taxis and buses connect towns, and land ports at Dawki and elsewhere handle trade with Bangladesh.",
        "मेघालय का लगभग सारा यातायात सड़कों से होता है। एनएच-6 (पहले एनएच-40 और एनएच-44) गुवाहाटी से शिलांग चढ़ता है और जयंतिया पहाड़ियों से होकर सिलचर तक जाता है, और एनएच-62 व एनएच-217 गारो पहाड़ियों को जोड़ते हैं। शहर से लगभग 30 किमी दूर उमरोई का शिलांग हवाई अड्डा छोटे विमानों की उड़ानें देता है, जबकि अधिकांश यात्री लगभग तीन घंटे दूर गुवाहाटी हवाई अड्डे का उपयोग करते हैं; तुरा में बालजेक में हवाई पट्टी है। एकमात्र रेलवे स्टेशन उत्तरी गारो हिल्स का मेंदीपाथर है, जो 2014 से असम से जुड़ा है। साझा टैक्सियाँ और बसें नगरों को जोड़ती हैं, और दावकी व अन्य जगहों के भू-बंदरगाह बांग्लादेश के साथ व्यापार संभालते हैं।",
        "मेघालयातील जवळपास सर्व वाहतूक रस्त्यांनी होते. एनएच-6 (पूर्वीचे एनएच-40 व एनएच-44) गुवाहाटीहून शिलाँगपर्यंत चढतो व जयंतिया टेकड्यांतून सिलचरपर्यंत जातो, आणि एनएच-62 व एनएच-217 गारो टेकड्यांना सेवा देतात. शहरापासून सुमारे 30 किमीवरील उमरोई येथील शिलाँग विमानतळावरून लहान विमानांची उड्डाणे होतात, तर बहुतेक प्रवासी सुमारे तीन तासांवरील गुवाहाटी विमानतळ वापरतात; तुराला बालजेक येथे धावपट्टी आहे. एकमेव रेल्वे स्थानक उत्तर गारो हिल्समधील मेंदीपाथर आहे, जे 2014 पासून आसामशी जोडलेले आहे. सामायिक टॅक्सी व बस शहरे जोडतात, आणि दावकी व इतर ठिकाणची भू-बंदरे बांगलादेशशी व्यापार हाताळतात."),
        conf="Editorial"),
    lst("airports", [
        it3("shl", "Shillong Airport, Umroi", "शिलांग हवाई अड्डा, उमरोई", "शिलाँग विमानतळ, उमरोई", m=("SHL", "SHL", "SHL")),
        it3("gau", "Guwahati (Assam)", "गुवाहाटी (असम)", "गुवाहाटी (आसाम)", m=("GAU, nearest major airport", "GAU, निकटतम बड़ा हवाई अड्डा", "GAU, जवळचा मोठा विमानतळ")),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("Road length by category", "श्रेणीवार सड़क लंबाई", "प्रकारनिहाय रस्त्यांची लांबी"), "morth", "Basic Road Statistics of India."),
        (L("Mendipathar rail link — opening date", "मेंदीपाथर रेल लिंक — उद्घाटन तिथि", "मेंदीपाथर रेल्वे जोड — उद्घाटन तारीख"), "railways", "Northeast Frontier Railway."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Hydropower is Meghalaya's main source of electricity. The Umiam–Umtru stations, begun in the 1960s around Umiam lake, the Myntdu-Leshka project in the Jaintia Hills and the New Umtru station are run by the State-owned Meghalaya Energy Corporation, and the State also draws power from central stations through the North-Eastern grid. Coal from the Jaintia and Garo Hills was once a major output, but unscientific 'rat-hole' mining was banned by the National Green Tribunal in 2014, and scientific mining under approved plans has resumed only slowly.",
        "जलविद्युत मेघालय की बिजली का मुख्य स्रोत है। उमियम झील के आसपास 1960 के दशक में शुरू हुए उमियम–उमत्रू केंद्र, जयंतिया पहाड़ियों में मिंतदू-लेश्का परियोजना और न्यू उमत्रू केंद्र राज्य के स्वामित्व वाले मेघालय ऊर्जा निगम द्वारा चलाए जाते हैं, और राज्य पूर्वोत्तर ग्रिड के माध्यम से केंद्रीय बिजलीघरों से भी बिजली लेता है। जयंतिया और गारो पहाड़ियों का कोयला कभी बड़ा उत्पादन था, पर अवैज्ञानिक 'रैट-होल' खनन पर 2014 में राष्ट्रीय हरित अधिकरण ने रोक लगाई, और स्वीकृत योजनाओं के तहत वैज्ञानिक खनन धीरे-धीरे ही फिर शुरू हुआ है।",
        "जलविद्युत हा मेघालयाच्या विजेचा मुख्य स्रोत आहे. उमियम सरोवराभोवती 1960 च्या दशकात सुरू झालेली उमियम–उमत्रू केंद्रे, जयंतिया टेकड्यांतील मिंतदू-लेश्का प्रकल्प व न्यू उमत्रू केंद्र राज्याच्या मालकीचे मेघालय ऊर्जा महामंडळ चालवते, आणि राज्य ईशान्य ग्रिडद्वारे केंद्रीय वीजकेंद्रांतूनही वीज घेते. जयंतिया व गारो टेकड्यांतील कोळसा एकेकाळी मोठे उत्पादन होते, पण अशास्त्रीय 'रॅट-होल' खाणकामावर 2014 मध्ये राष्ट्रीय हरित लवादाने बंदी घातली, आणि मंजूर आराखड्यांनुसार शास्त्रीय खाणकाम हळूहळूच पुन्हा सुरू झाले आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by station", "केंद्रवार स्थापित क्षमता", "केंद्रनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report / MePGCL."),
        (L("Coal production since the resumption of mining", "खनन फिर शुरू होने के बाद कोयला उत्पादन", "खाणकाम पुन्हा सुरू झाल्यापासून कोळसा उत्पादन"), "india-gov", "Ministry of Coal / Meghalaya Mining and Geology Department."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Mobile networks cover Shillong, Tura and most towns, but many villages in the deep valleys and border areas have weak signals. The State has built online services for land records, certificates and payments, and IIM Shillong, NEHU and NIT Meghalaya, with a growing number of software and design start-ups in Shillong, form a small technology community.",
        "मोबाइल नेटवर्क शिलांग, तुरा और अधिकांश नगरों को कवर करते हैं, पर गहरी घाटियों और सीमावर्ती क्षेत्रों के बहुत से गाँवों में सिग्नल कमज़ोर हैं। राज्य ने भूमि अभिलेख, प्रमाणपत्र और भुगतान की ऑनलाइन सेवाएँ बनाई हैं, और आईआईएम शिलांग, नेहू और एनआईटी मेघालय, शिलांग के बढ़ते सॉफ़्टवेयर और डिज़ाइन स्टार्ट-अप के साथ, एक छोटा प्रौद्योगिकी समुदाय बनाते हैं।",
        "मोबाइल जाळे शिलाँग, तुरा व बहुतेक शहरांना व्यापते, पण खोल दऱ्या व सीमाभागांतील अनेक गावांत संकेत कमकुवत आहेत. राज्याने भूमी अभिलेख, दाखले व देयकांसाठी ऑनलाइन सेवा उभारल्या आहेत, आणि आयआयएम शिलाँग, नेहू व एनआयटी मेघालय, शिलाँगमधील वाढत्या सॉफ्टवेअर व डिझाइन स्टार्ट-अपसह, एक लहान तंत्रज्ञान समुदाय घडवतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (North East circle)."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("ML", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["ML"]
ger = AP["aishe_ger"]["ML"]; nu = AP["aishe_universities_2021_22"]["ML"]; nc = AP["aishe_colleges_2021_22"]["ML"]
module(R, "education", [
    prose("p1", L(
        f"Literacy in Meghalaya was 74.4% at the 2011 Census. The higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE, below the national 28.4%, and women's GER ({gf}%) was well above men's ({gm}%). The State had {nu} universities, many of them private, and {inr(nc)} colleges.\n\nShillong has long been an educational centre for the North-East, with mission schools and colleges such as St. Edmund's and St. Anthony's. North-Eastern Hill University (NEHU), a central university founded in 1973, has campuses in Shillong and Tura; IIM Shillong was set up in 2007, and NIT Meghalaya is at Sohra. Khasi and Garo are taught in schools, and NEHU offers degrees in both languages.",
        f"2011 की जनगणना में मेघालय की साक्षरता 74.4% थी। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था, जो राष्ट्रीय 28.4% से कम है, और महिलाओं का जीईआर ({gf}%) पुरुषों ({gm}%) से काफ़ी अधिक था। राज्य में {nu} विश्वविद्यालय थे, जिनमें से कई निजी हैं, और {inr(nc)} कॉलेज।\n\nशिलांग लंबे समय से पूर्वोत्तर का शैक्षिक केंद्र रहा है, जहाँ सेंट एडमंड्स और सेंट एंथनीज़ जैसे मिशन स्कूल और कॉलेज हैं। 1973 में स्थापित केंद्रीय विश्वविद्यालय, नॉर्थ-ईस्टर्न हिल यूनिवर्सिटी (नेहू), के परिसर शिलांग और तुरा में हैं; आईआईएम शिलांग 2007 में स्थापित हुआ, और एनआईटी मेघालय सोहरा में है। स्कूलों में खासी और गारो पढ़ाई जाती हैं, और नेहू दोनों भाषाओं में डिग्री देता है।",
        f"2011 च्या जनगणनेत मेघालयाची साक्षरता 74.4% होती. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा कमी, आणि स्त्रियांचे जीईआर ({gf}%) पुरुषांपेक्षा ({gm}%) बरेच जास्त होते. राज्यात {nu} विद्यापीठे होती, त्यांपैकी अनेक खासगी, आणि {inr(nc)} महाविद्यालये.\n\nशिलाँग दीर्घ काळापासून ईशान्येचे शैक्षणिक केंद्र आहे, जिथे सेंट एडमंड्स व सेंट अँथनीजसारख्या मिशन शाळा व महाविद्यालये आहेत. 1973 मध्ये स्थापन झालेल्या केंद्रीय विद्यापीठाचे, नॉर्थ-ईस्टर्न हिल युनिव्हर्सिटी (नेहू), परिसर शिलाँग व तुरा येथे आहेत; आयआयएम शिलाँग 2007 मध्ये स्थापन झाले, आणि एनआयटी मेघालय सोहरा येथे आहे. शाळांत खासी व गारो शिकवल्या जातात, आणि नेहू दोन्ही भाषांत पदव्या देते."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("nehu", "North-Eastern Hill University", "नॉर्थ-ईस्टर्न हिल यूनिवर्सिटी", "नॉर्थ-ईस्टर्न हिल युनिव्हर्सिटी", m=("Central university, Shillong, 1973", "केंद्रीय विश्वविद्यालय, शिलांग, 1973", "केंद्रीय विद्यापीठ, शिलाँग, 1973")),
        it3("iims", "IIM Shillong", "आईआईएम शिलांग", "आयआयएम शिलाँग", m=("2007", "2007", "2007")),
        it3("nitm", "NIT Meghalaya", "एनआईटी मेघालय", "एनआयटी मेघालय", m=("Sohra", "सोहरा", "सोहरा")),
        it3("neigrihms", "NEIGRIHMS", "नेग्रिम्स", "नेग्रिम्स", m=("Medical institute, Shillong", "चिकित्सा संस्थान, शिलांग", "वैद्यकीय संस्था, शिलाँग")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["ML"]; s = C["srs"]["ML"]
module(R, "health", [
    prose("p1", L(
        f"Meghalaya's infant mortality rate was {s[5]:.0f} per 1,000 live births in 2020 in the Sample Registration System, down from {s[4]:.0f} in 2010 and close to the national 28. The birth rate was {s[1]} and the death rate {s[3]} per 1,000. Maternal and child health remain the main challenges: in NFHS-5 only {n['institutional_N5']:.1f}% of births took place in health facilities, and {n['stunted'][1]:.1f}% of children under five were stunted, up from {n['stunted'][0]}% in NFHS-4, while {n['wasted'][1]:.1f}% were wasted and {n['underweight'][1]:.1f}% underweight.\n\nNEIGRIHMS, a central institute in Shillong, and the Civil Hospital and Ganesh Das Hospital are the main referral centres, with district hospitals elsewhere. Many villages are far from roads, and the State runs programmes to bring mothers to hospitals for delivery and to track pregnancies.",
        f"नमूना पंजीकरण प्रणाली में 2020 में मेघालय की शिशु मृत्यु दर प्रति 1,000 जीवित जन्म पर {s[5]:.0f} थी, जो 2010 के {s[4]:.0f} से कम और राष्ट्रीय 28 के क़रीब है। जन्म दर प्रति 1,000 पर {s[1]} और मृत्यु दर {s[3]} थी। मातृ और शिशु स्वास्थ्य मुख्य चुनौतियाँ बनी हुई हैं: एनएफ़एचएस-5 में केवल {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, और पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने थे, जो एनएफ़एचएस-4 के {n['stunted'][0]}% से अधिक है, जबकि {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के थे।\n\nशिलांग का केंद्रीय संस्थान नेग्रिम्स, और सिविल अस्पताल व गणेश दास अस्पताल मुख्य रेफ़रल केंद्र हैं, और अन्य जगहों पर ज़िला अस्पताल हैं। बहुत से गाँव सड़कों से दूर हैं, और राज्य माताओं को प्रसव के लिए अस्पताल लाने और गर्भावस्था पर नज़र रखने के कार्यक्रम चलाता है।",
        f"नमुना नोंदणी पद्धतीनुसार 2020 मध्ये मेघालयाचा अर्भक मृत्युदर दर 1,000 जिवंत जन्मांमागे {s[5]:.0f} होता, 2010 मधील {s[4]:.0f} वरून कमी व राष्ट्रीय 28 च्या जवळ. जन्मदर दर 1,000 मागे {s[1]} व मृत्युदर {s[3]} होता. माता व बाल आरोग्य ही मुख्य आव्हाने कायम आहेत: एनएफएचएस-5 मध्ये केवळ {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, आणि पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी होती, एनएफएचएस-4 मधील {n['stunted'][0]}% पेक्षा जास्त, तर {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची होती.\n\nशिलाँगमधील केंद्रीय संस्था नेग्रिम्स, आणि सिव्हिल रुग्णालय व गणेश दास रुग्णालय ही मुख्य संदर्भ केंद्रे आहेत, आणि इतरत्र जिल्हा रुग्णालये आहेत. अनेक गावे रस्त्यांपासून दूर आहेत, आणि राज्य मातांना प्रसूतीसाठी रुग्णालयात आणण्याचे व गर्भारपणाचा मागोवा घेण्याचे कार्यक्रम राबवते."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("ML"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Maternal mortality ratio", "मातृ मृत्यु अनुपात", "माता मृत्यू गुणोत्तर"), "srs", "SRS special bulletin on MMR (Meghalaya is reported within 'Other States')."),
        (L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"), "srs", "Meghalaya is not in the SRS abridged life table for major States used here."),
        (L("Hospital beds and doctors per lakh population", "प्रति लाख जनसंख्या अस्पताल बिस्तर और डॉक्टर", "दर लाख लोकसंख्येमागे रुग्णालय खाटा व डॉक्टर"), "mohfw", "Rural Health Statistics / National Health Profile."),
    ]),
])
print("ml mod2 ok")
