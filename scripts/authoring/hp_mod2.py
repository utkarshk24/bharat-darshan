"""Himachal Pradesh modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-HP"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_HP = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 24 Oct 2026. "
           "FY2024-25 is the latest year published for Himachal Pradesh and may be revised.")
mo = research("mospi_hp.json")
C = research("census_b5plus.json")
NAME = L("Himachal Pradesh", "हिमाचल प्रदेश", "हिमाचल प्रदेश")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Himachali culture centres on the village deity (devta) and the fairs held in its honour, where devtas arrive in decorated palanquins to the sound of drums, trumpets and the long karnal horn. The nati, a slow circle dance with linked arms, is danced across Kullu, Shimla, Sirmaur and Kinnaur. The Pahari schools of miniature painting that flourished at Guler and Kangra in the 18th and 19th centuries are known for delicate scenes of Krishna and Radha, and Kangra Paintings are a registered GI. Chamba rumals — double-sided embroidered handkerchiefs — Kullu and Kinnauri shawls woven with bright geometric borders, and the woodcarving of temples in Kullu, Mandi and Sarahan are celebrated crafts. Buddhist traditions of Lahaul, Spiti and Kinnaur, and the Tibetan community in Dharamshala, add monasteries, cham masked dances and thangka painting.",
        "हिमाचली संस्कृति गाँव के देवता और उनके सम्मान में लगने वाले मेलों के इर्द-गिर्द है, जहाँ ढोल, नगाड़ों और लंबे करनाल वाद्य की ध्वनि के बीच देवता सजी पालकियों में आते हैं। बाँहों में बाँहें डालकर किया जाने वाला धीमा घेरा नृत्य नाटी कुल्लू, शिमला, सिरमौर और किन्नौर में होता है। 18वीं और 19वीं सदी में गुलेर और कांगड़ा में पनपी पहाड़ी लघुचित्र शैलियाँ कृष्ण और राधा के कोमल चित्रों के लिए जानी जाती हैं, और कांगड़ा चित्रकला पंजीकृत जीआई है। चंबा रूमाल — दोनों ओर कढ़े रूमाल — चटक ज्यामितीय किनारी वाली कुल्लू और किन्नौरी शॉलें, और कुल्लू, मंडी व सराहन के मंदिरों की काष्ठ नक़्क़ाशी प्रसिद्ध शिल्प हैं। लाहौल, स्पीति और किन्नौर की बौद्ध परंपराएँ और धर्मशाला का तिब्बती समुदाय मठ, छम मुखौटा नृत्य और थंका चित्रकला जोड़ते हैं।",
        "हिमाचली संस्कृती गावदेवता व त्याच्या सन्मानार्थ भरणाऱ्या जत्रांभोवती फिरते, जिथे ढोल, नगारे व लांब करनाल वाद्याच्या आवाजात देवता सजवलेल्या पालख्यांतून येतात. हातात हात गुंफून केले जाणारे संथ वर्तुळ नृत्य नाटी कुल्लू, शिमला, सिरमौर व किन्नौरमध्ये होते. अठराव्या व एकोणिसाव्या शतकात गुलेर व कांगडा येथे बहरलेल्या पहाडी लघुचित्र शैली कृष्ण-राधेच्या नाजूक चित्रांसाठी ओळखल्या जातात, आणि कांगडा चित्रकला हे नोंदणीकृत जीआय आहे. चंबा रुमाल — दोन्ही बाजूंनी भरतकाम केलेले रुमाल — रंगीत भौमितिक काठांच्या कुल्लू व किन्नौरी शाली, आणि कुल्लू, मंडी व सराहनच्या मंदिरांचे काष्ठशिल्प या प्रसिद्ध हस्तकला आहेत. लाहौल, स्पिती व किन्नौरच्या बौद्ध परंपरा आणि धर्मशालेचा तिबेटी समुदाय मठ, छम मुखवटा नृत्य व थांका चित्रकलेची भर घालतात."),
        conf="Editorial"),
    lst("festivals", [
        fest("dussehra", "Kullu Dussehra", "कुल्लू दशहरा", "कुल्लू दसरा", ("October (week after Vijayadashami)", "अक्टूबर (विजयादशमी से एक सप्ताह)", "ऑक्टोबर (विजयादशमीपासून आठवडाभर)"),
             ("Hundreds of valley deities gather at Dhalpur maidan around Raghunath ji.", "ढालपुर मैदान में रघुनाथ जी के आसपास घाटी के सैकड़ों देवता इकट्ठा होते हैं।", "ढालपूर मैदानावर रघुनाथजींभोवती खोऱ्यातील शेकडो देवता जमतात.")),
        fest("shivratri", "Mandi Shivratri fair", "मंडी शिवरात्रि मेला", "मंडी शिवरात्री जत्रा", ("February–March", "फ़रवरी–मार्च", "फेब्रुवारी–मार्च"),
             ("Week-long fair of the deities of Mandi around Mahashivratri.", "महाशिवरात्रि पर मंडी के देवताओं का सप्ताह भर का मेला।", "महाशिवरात्रीला मंडीच्या देवतांची आठवडाभराची जत्रा.")),
        fest("minjar", "Minjar fair, Chamba", "मिंजर मेला, चंबा", "मिंजर जत्रा, चंबा", ("July–August", "जुलाई–अगस्त", "जुलै–ऑगस्ट"),
             ("Harvest fair ending with offerings to the Ravi.", "फ़सल मेला, जो रावी को अर्पण के साथ समाप्त होता है।", "सुगीची जत्रा, जी रावीला अर्पणाने संपते.")),
        fest("lavi", "Lavi fair, Rampur", "लवी मेला, रामपुर", "लवी जत्रा, रामपूर", ("November", "नवंबर", "नोव्हेंबर"),
             ("Old trade fair for wool, dry fruit and horses from Kinnaur and Tibet.", "किन्नौर और तिब्बत से ऊन, मेवे और घोड़ों का पुराना व्यापार मेला।", "किन्नौर व तिबेटमधून लोकर, सुकामेवा व घोड्यांची जुनी व्यापारी जत्रा.")),
        fest("losar", "Losar", "लोसर", "लोसर", ("February–March", "फ़रवरी–मार्च", "फेब्रुवारी–मार्च"),
             ("Tibetan New Year in Lahaul, Spiti, Kinnaur and McLeod Ganj.", "लाहौल, स्पीति, किन्नौर और मैक्लोडगंज में तिब्बती नव वर्ष।", "लाहौल, स्पिती, किन्नौर व मॅक्लिओडगंजमध्ये तिबेटी नववर्ष.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("nati", "Nati dance", "नाटी नृत्य", "नाटी नृत्य"), it3("pahari", "Pahari (Kangra) painting", "पहाड़ी (कांगड़ा) चित्रकला", "पहाडी (कांगडा) चित्रकला"),
        it3("rumal", "Chamba rumal", "चंबा रूमाल", "चंबा रुमाल"), it3("shawl", "Kullu and Kinnauri shawls", "कुल्लू और किन्नौरी शॉल", "कुल्लू व किन्नौरी शाली"),
        it3("wood", "Temple woodcarving", "मंदिर काष्ठ नक़्क़ाशी", "मंदिर काष्ठशिल्प"), it3("thangka", "Thangka painting", "थंका चित्रकला", "थांका चित्रकला"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("dham", "Dham", "धाम", "धाम", d=("Festive meal of rice, rajma, madra and sweet rice, cooked by botis and served on leaf plates.", "चावल, राजमा, मदरा और मीठे चावल का उत्सवी भोज, जिसे बोटी बनाते हैं और पत्तल पर परोसा जाता है।", "भात, राजमा, मदरा व गोड भाताची सणाची पंगत, जी बोटी शिजवतात व पत्रावळीवर वाढली जाते.")),
        it3("siddu", "Siddu", "सिड्डू", "सिड्डू", d=("Steamed wheat bun stuffed with walnut or poppy seed, eaten with ghee.", "अखरोट या पोस्ते से भरा भाप में पका गेहूँ का बन, घी के साथ।", "अक्रोड किंवा खसखस भरलेला वाफवलेला गव्हाचा बन, तुपासह.")),
        it3("madra", "Madra", "मदरा", "मदरा", d=("Chickpeas or beans cooked in yoghurt with spices — a Chamba speciality.", "मसालों के साथ दही में पके छोले या राजमा — चंबा की विशेषता।", "मसाल्यांसह दह्यात शिजवलेले छोले किंवा राजमा — चंब्याची खासियत.")),
        it3("babru", "Babru", "बबरू", "बबरू", d=("Deep-fried black-gram bread, a Shimla snack.", "उड़द भरी तली रोटी, शिमला का नाश्ता।", "उडीद भरलेली तळलेली पुरी, शिमल्याचा नाश्ता.")),
        it3("tea", "Kangra tea", "कांगड़ा चाय", "कांगडा चहा", d=("Green and black tea grown around Palampur; a registered GI.", "पालमपुर के आसपास उगाई गई हरी और काली चाय; पंजीकृत जीआई।", "पालमपूरभोवती पिकवला जाणारा हिरवा व काळा चहा; नोंदणीकृत जीआय.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("topi", "Himachali topi", "हिमाचली टोपी", "हिमाचली टोपी", d=("Woollen cap with a coloured velvet band, worn by men and women.", "रंगीन मख़मली पट्टी वाली ऊनी टोपी, जिसे पुरुष और महिलाएँ पहनते हैं।", "रंगीत मखमली पट्टीची लोकरी टोपी, जी पुरुष व स्त्रिया घालतात.")),
        it3("pattu", "Pattu and dhatu", "पट्टू और ढाठू", "पट्टू व ढाठू", d=("Women's woollen wrap pinned at the shoulder, with a headscarf.", "कंधे पर पिन से बँधा महिलाओं का ऊनी वस्त्र और सिर का रूमाल।", "खांद्यावर पिनने बांधलेले स्त्रियांचे लोकरी वस्त्र व डोक्याचा रुमाल.")),
        it3("chola", "Gaddi chola and dora", "गद्दी चोला और डोरा", "गद्दी चोला व डोरा", d=("Shepherds' woollen coat tied with a long black rope.", "चरवाहों का ऊनी कोट, जिसे लंबी काली रस्सी से बाँधा जाता है।", "मेंढपाळांचा लोकरी कोट, जो लांब काळ्या दोरीने बांधला जातो.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; util = 100 * g["utilities"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["HP"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["HP"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Himachal Pradesh's GSDP at current prices was about ₹{cur['FY2024-25'][0]/1e5:.2f} lakh crore in FY2024-25, the latest year published for the State in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2024-25'][0])}. Manufacturing made up about {mfg:.0f}% of GSVA — mostly pharmaceuticals and other factories in the Baddi–Barotiwala–Nalagarh belt of Solan district, which grew after the industrial incentives of the 2000s — agriculture, horticulture, livestock and forestry about {agri:.0f}%, and electricity and other utilities about {util:.0f}%, reflecting the large hydro-electric stations on the Sutlej, Beas and Ravi. Apples from Shimla, Kullu and Kinnaur are the most valuable crop, followed by other fruit, off-season vegetables and Kangra tea, and tourism supports hotels, transport and handicrafts across the State.\n\nThe PLFS unemployment rate was {ur['2025']}% in 2025, against {ui['2025']}% nationally. Women's labour force participation was {lf['female']}% — far above the national {lfi['female']}% — largely because women do much of the farm and orchard work.",
        f"मोस्पी शृंखला में राज्य के लिए प्रकाशित नवीनतम वर्ष, वित्त वर्ष 2024-25 में हिमाचल प्रदेश का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2024-25'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2024-25'][0])}। जीएसवीए में विनिर्माण का हिस्सा लगभग {mfg:.0f}% था — अधिकतर सोलन ज़िले की बद्दी–बरोटीवाला–नालागढ़ पट्टी के दवा और अन्य कारख़ाने, जो 2000 के दशक की औद्योगिक रियायतों के बाद बढ़े — कृषि, बाग़वानी, पशुपालन और वानिकी का लगभग {agri:.0f}%, और बिजली व अन्य उपयोगिताओं का लगभग {util:.0f}%, जो सतलुज, ब्यास और रावी पर बने बड़े जलविद्युत केंद्रों को दर्शाता है। शिमला, कुल्लू और किन्नौर के सेब सबसे मूल्यवान फ़सल हैं, उसके बाद अन्य फल, बेमौसमी सब्ज़ियाँ और कांगड़ा चाय, और पर्यटन पूरे राज्य में होटलों, परिवहन और हस्तशिल्प को सहारा देता है।\n\nपीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी, जबकि राष्ट्रीय {ui['2025']}%। महिलाओं की श्रम बल भागीदारी {lf['female']}% थी — राष्ट्रीय {lfi['female']}% से कहीं अधिक — मुख्यतः इसलिए कि खेतों और बाग़ानों का अधिकांश काम महिलाएँ करती हैं।",
        f"मोस्पी मालिकेत राज्यासाठी प्रकाशित नवीनतम वर्ष, आ.व. 2024-25 मध्ये हिमाचल प्रदेशचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2024-25'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2024-25'][0])}. जीएसव्हीएमध्ये उत्पादन उद्योगाचा वाटा सुमारे {mfg:.0f}% होता — बहुतांश सोलन जिल्ह्यातील बद्दी–बरोटीवाला–नालागड पट्ट्यातील औषधनिर्मिती व इतर कारखाने, जे 2000 च्या दशकातील औद्योगिक सवलतींनंतर वाढले — शेती, फलोत्पादन, पशुपालन व वनीकरणाचा सुमारे {agri:.0f}%, आणि वीज व इतर उपयुक्तता सेवांचा सुमारे {util:.0f}%, जो सतलज, बियास व रावीवरील मोठ्या जलविद्युत केंद्रांचे प्रतिबिंब आहे. शिमला, कुल्लू व किन्नौरची सफरचंदे हे सर्वांत मौल्यवान पीक आहे, त्यानंतर इतर फळे, बिगरहंगामी भाज्या व कांगडा चहा, आणि पर्यटन संपूर्ण राज्यात हॉटेल, वाहतूक व हस्तकलांना आधार देते.\n\nपीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता, तर राष्ट्रीय {ui['2025']}%. स्त्रियांचा श्रमशक्ती सहभाग {lf['female']}% होता — राष्ट्रीय {lfi['female']}% पेक्षा कितीतरी अधिक — मुख्यतः शेती व बागांतील बहुतेक काम स्त्रिया करतात म्हणून."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_HP), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_HP), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_HP), "rupee", "higher-is-better",
             previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("HP", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    plfs_series("HP", NAME),
    lst("sectors-key", [
        it3("apple", "Apples and fruit", "सेब और फल", "सफरचंदे व फळे", d=("Orchards of Shimla, Kullu, Kinnaur and Chamba; plums, cherries and pears too.", "शिमला, कुल्लू, किन्नौर और चंबा के बाग़; आलूबुख़ारा, चेरी और नाशपाती भी।", "शिमला, कुल्लू, किन्नौर व चंब्याच्या बागा; आलुबुखार, चेरी व नासपतीही.")),
        it3("hydro", "Hydro-electricity", "जलविद्युत", "जलविद्युत", d=("Stations on the Sutlej, Beas, Ravi and their tributaries; surplus power sold to other States.", "सतलुज, ब्यास, रावी और उनकी सहायक नदियों पर केंद्र; अतिरिक्त बिजली अन्य राज्यों को बेची जाती है।", "सतलज, बियास, रावी व उपनद्यांवर केंद्रे; जादा वीज इतर राज्यांना विकली जाते.")),
        it3("pharma", "Pharmaceuticals", "दवा उद्योग", "औषधनिर्मिती", d=("Baddi–Barotiwala–Nalagarh industrial belt in Solan.", "सोलन की बद्दी–बरोटीवाला–नालागढ़ औद्योगिक पट्टी।", "सोलनचा बद्दी–बरोटीवाला–नालागड औद्योगिक पट्टा.")),
        it3("tourism", "Tourism", "पर्यटन", "पर्यटन", d=("Shimla, Manali, Dharamshala, Dalhousie and Spiti.", "शिमला, मनाली, धर्मशाला, डलहौज़ी और स्पीति।", "शिमला, मनाली, धर्मशाला, डलहौसी व स्पिती.")),
        it3("veg", "Off-season vegetables", "बेमौसमी सब्ज़ियाँ", "बिगरहंगामी भाज्या", d=("Peas, tomatoes and cauliflower for the plains in summer.", "गर्मियों में मैदानों के लिए मटर, टमाटर और फूलगोभी।", "उन्हाळ्यात मैदानी प्रदेशासाठी वाटाणा, टोमॅटो व फुलकोबी.")),
        it3("cement", "Cement", "सीमेंट", "सिमेंट", d=("Limestone-based plants in Bilaspur, Solan and Sirmaur.", "बिलासपुर, सोलन और सिरमौर में चूना पत्थर आधारित संयंत्र।", "बिलासपूर, सोलन व सिरमौरमध्ये चुनखडीवर आधारित कारखाने.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Apple production and area", "सेब उत्पादन और क्षेत्रफल", "सफरचंद उत्पादन व क्षेत्र"), "india-gov", "HP Horticulture Department."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("GSDP for FY2025-26", "वित्त वर्ष 2025-26 का जीएसडीपी", "आ.व. 2025-26 चे जीएसडीपी"), "mospi", "Not yet published for Himachal Pradesh in the MoSPI series at access time."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Himachal Pradesh has a unicameral legislature, the 68-member Vidhan Sabha, which meets in Shimla and holds its winter session at Tapovan near Dharamshala. The State elects 4 members to the Lok Sabha and 3 to the Rajya Sabha.\n\nThe Indian National Congress won the Assembly election of November 2022, and Sukhvinder Singh Sukhu was sworn in as Chief Minister on 11 December 2022, with Mukesh Agnihotri as Deputy Chief Minister. Kuldeep Singh Pathania (INC) is Speaker. Kavinder Gupta, formerly Lieutenant Governor of Ladakh, has been Governor since 10 March 2026. The next Assembly election is due by late 2027.",
        "हिमाचल प्रदेश में एकसदनीय विधानमंडल है, 68 सदस्यों वाली विधानसभा, जिसकी बैठकें शिमला में होती हैं और शीतकालीन सत्र धर्मशाला के पास तपोवन में होता है। राज्य से लोकसभा के 4 और राज्यसभा के 3 सदस्य चुने जाते हैं।\n\nनवंबर 2022 का विधानसभा चुनाव भारतीय राष्ट्रीय कांग्रेस ने जीता, और सुखविंदर सिंह सुक्खू ने 11 दिसंबर 2022 को मुख्यमंत्री पद की शपथ ली, जबकि मुकेश अग्निहोत्री उपमुख्यमंत्री बने। कुलदीप सिंह पठानिया (कांग्रेस) अध्यक्ष हैं। लद्दाख के पूर्व उपराज्यपाल कविंद्र गुप्ता 10 मार्च 2026 से राज्यपाल हैं। अगला विधानसभा चुनाव 2027 के अंत तक होना है।",
        "हिमाचल प्रदेशमध्ये एकसदनी विधिमंडळ आहे, 68 सदस्यांची विधानसभा, जिच्या बैठका शिमल्यात होतात आणि हिवाळी अधिवेशन धर्मशालेजवळील तपोवन येथे होते. राज्यातून लोकसभेवर 4 व राज्यसभेवर 3 सदस्य निवडले जातात.\n\nनोव्हेंबर 2022 ची विधानसभा निवडणूक भारतीय राष्ट्रीय काँग्रेसने जिंकली, आणि सुखविंदर सिंह सुक्खू यांनी 11 डिसेंबर 2022 रोजी मुख्यमंत्रिपदाची शपथ घेतली, तर मुकेश अग्निहोत्री उपमुख्यमंत्री झाले. कुलदीप सिंह पठानिया (काँग्रेस) अध्यक्ष आहेत. लडाखचे माजी नायब राज्यपाल कविंदर गुप्ता 10 मार्च 2026 पासून राज्यपाल आहेत. पुढील विधानसभा निवडणूक 2027 च्या अखेरीपर्यंत होणे अपेक्षित आहे."),
        sources=["scroll", "kashmir-life", "etv-bharat"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("vs", "Himachal Pradesh Vidhan Sabha", "हिमाचल प्रदेश विधानसभा", "हिमाचल प्रदेश विधानसभा", url="https://hpvidhansabha.nic.in", src="india-gov"),
        it3("portal", "Government of Himachal Pradesh", "हिमाचल प्रदेश सरकार", "हिमाचल प्रदेश शासन", url="https://himachal.nic.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2022 Assembly election — party-wise result", "2022 विधानसभा चुनाव — दलवार परिणाम", "2022 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Himachal Pradesh 2022."),
        (L("Governor's swearing-in — official source", "राज्यपाल का शपथ ग्रहण — आधिकारिक स्रोत", "राज्यपालांचा शपथविधी — अधिकृत स्रोत"), "india-gov", "Replace the news report with the Raj Bhavan (Lok Bhavan) release."),
        (L("Leader of Opposition — official notice", "नेता प्रतिपक्ष — आधिकारिक सूचना", "विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "Vidhan Sabha secretariat."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "The Atal Tunnel under the Rohtang Pass (2020), AIIMS Bilaspur (2022) and the four-lane Kiratpur–Nerchowk highway (2024) are recent completed projects. Other major works include the Bhanupli–Bilaspur–Beri railway line towards Manali and Leh, four-laning of highways to Shimla and Dharamshala, and several large hydro-electric projects; these will be added as cards once their status is confirmed from official sources. Each card shows its source and the date it was checked.",
        "रोहतांग दर्रे के नीचे अटल सुरंग (2020), एम्स बिलासपुर (2022) और चार-लेन कीरतपुर–नेरचौक राजमार्ग (2024) हाल में पूरी हुई परियोजनाएँ हैं। अन्य बड़े कार्यों में मनाली और लेह की ओर भानुपल्ली–बिलासपुर–बेरी रेल लाइन, शिमला और धर्मशाला के राजमार्गों को चार-लेन करना और कई बड़ी जलविद्युत परियोजनाएँ शामिल हैं; आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर इन्हें कार्ड के रूप में जोड़ा जाएगा। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "रोहतांग खिंडीखालील अटल बोगदा (2020), एम्स बिलासपूर (2022) व चौपदरी कीरतपूर–नेरचौक महामार्ग (2024) हे अलीकडे पूर्ण झालेले प्रकल्प आहेत. इतर मोठ्या कामांत मनाली व लेहकडे जाणारी भानुपल्ली–बिलासपूर–बेरी रेल्वे मार्गिका, शिमला व धर्मशालेकडील महामार्गांचे चौपदरीकरण आणि अनेक मोठे जलविद्युत प्रकल्प यांचा समावेश आहे; अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर त्यांची कार्डे जोडली जातील. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pmindia"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Bhanupli–Bilaspur–Beri rail line — status", "भानुपल्ली–बिलासपुर–बेरी रेल लाइन — स्थिति", "भानुपल्ली–बिलासपूर–बेरी रेल्वे मार्गिका — स्थिती"), "railways", "Ministry of Railways / RVNL."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Roads are Himachal's lifeline, and the Himachal Road Transport Corporation's buses reach remote villages. National highways run from Chandigarh to Shimla and on along the old Hindustan–Tibet Road into Kinnaur, from Kiratpur through Mandi and Kullu to Manali and, through the Atal Tunnel, on to Lahaul and Leh, and from Pathankot to Dharamshala. Small airports at Shimla (Jubbarhatti), Kullu–Manali (Bhuntar) and Kangra (Gaggal) have limited flights. The narrow-gauge Kalka–Shimla railway, a UNESCO World Heritage site, and the Pathankot–Jogindernagar line through the Kangra valley are the main railways; a broad-gauge line reaches Una.",
        "सड़कें हिमाचल की जीवन रेखा हैं, और हिमाचल पथ परिवहन निगम की बसें दूरस्थ गाँवों तक पहुँचती हैं। राष्ट्रीय राजमार्ग चंडीगढ़ से शिमला और आगे पुरानी हिंदुस्तान–तिब्बत रोड के साथ किन्नौर तक, कीरतपुर से मंडी और कुल्लू होकर मनाली तक और अटल सुरंग से होकर लाहौल व लेह तक, और पठानकोट से धर्मशाला तक जाते हैं। शिमला (जुब्बड़हट्टी), कुल्लू–मनाली (भुंतर) और कांगड़ा (गग्गल) के छोटे हवाई अड्डों से सीमित उड़ानें हैं। यूनेस्को विश्व धरोहर नैरो गेज कालका–शिमला रेलवे और कांगड़ा घाटी से गुज़रने वाली पठानकोट–जोगिंदरनगर लाइन मुख्य रेलें हैं; एक ब्रॉड गेज लाइन ऊना तक पहुँचती है।",
        "रस्ते ही हिमाचलची जीवनरेखा आहेत, आणि हिमाचल पथ परिवहन महामंडळाच्या बस दुर्गम गावांपर्यंत पोहोचतात. राष्ट्रीय महामार्ग चंदीगडहून शिमल्यापर्यंत व पुढे जुन्या हिंदुस्थान–तिबेट रस्त्याने किन्नौरपर्यंत, कीरतपूरहून मंडी व कुल्लूमार्गे मनालीपर्यंत व अटल बोगद्यातून लाहौल व लेहपर्यंत, आणि पठाणकोटहून धर्मशालेपर्यंत जातात. शिमला (जुब्बडहट्टी), कुल्लू–मनाली (भुंतर) व कांगडा (गग्गल) येथील लहान विमानतळांवरून मर्यादित उड्डाणे आहेत. युनेस्को जागतिक वारसा असलेली नॅरो गेज कालका–शिमला रेल्वे व कांगडा खोऱ्यातून जाणारी पठाणकोट–जोगिंदरनगर मार्गिका या मुख्य रेल्वे आहेत; एक ब्रॉड गेज मार्ग ऊनापर्यंत पोहोचतो."),
        conf="Editorial"),
    lst("airports", [
        it3("sla", "Shimla (Jubbarhatti)", "शिमला (जुब्बड़हट्टी)", "शिमला (जुब्बडहट्टी)", m=("SLV", "SLV", "SLV")),
        it3("kuu", "Kullu–Manali (Bhuntar)", "कुल्लू–मनाली (भुंतर)", "कुल्लू–मनाली (भुंतर)", m=("KUU", "KUU", "KUU")),
        it3("dhm", "Kangra (Gaggal)", "कांगड़ा (गग्गल)", "कांगडा (गग्गल)", m=("DHM", "DHM", "DHM")),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("Road length and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Himachal Pradesh is one of India's main hydro-electric States. Large stations include Nathpa Jhakri and Rampur on the Sutlej, run by SJVN; Karcham Wangtoo, a private project in Kinnaur; the Bhakra and Pong dams managed by the Bhakra Beas Management Board; and the Chamera and Parbati projects of NHPC, alongside the State's own and many small hydro plants. The State receives free power as royalty from many projects and sells surplus electricity to other States, especially in summer when snowmelt swells the rivers. Hydro development has also raised concerns about landslides, tunnelling and river ecology in fragile valleys.",
        "हिमाचल प्रदेश भारत के मुख्य जलविद्युत राज्यों में से है। बड़े केंद्रों में एसजेवीएन द्वारा संचालित सतलुज पर नाथपा झाकड़ी और रामपुर; किन्नौर में निजी परियोजना करछम वांगतू; भाखड़ा ब्यास प्रबंध बोर्ड द्वारा संचालित भाखड़ा और पौंग बाँध; और एनएचपीसी की चमेरा व पार्बती परियोजनाएँ शामिल हैं, साथ में राज्य के अपने और कई छोटे जलविद्युत संयंत्र। राज्य को कई परियोजनाओं से रॉयल्टी के रूप में मुफ़्त बिजली मिलती है और यह अतिरिक्त बिजली अन्य राज्यों को बेचता है, विशेषकर गर्मियों में जब बर्फ़ पिघलने से नदियाँ उफनती हैं। जलविद्युत विकास ने नाज़ुक घाटियों में भूस्खलन, सुरंग निर्माण और नदी पारिस्थितिकी को लेकर चिंताएँ भी उठाई हैं।",
        "हिमाचल प्रदेश हे भारतातील मुख्य जलविद्युत राज्यांपैकी एक आहे. मोठ्या केंद्रांत एसजेव्हीएनद्वारे चालवली जाणारी सतलजवरील नाथपा झाकडी व रामपूर; किन्नौरमधील खासगी प्रकल्प करछम वांगतू; भाक्रा बियास व्यवस्थापन मंडळाकडील भाक्रा व पोंग धरणे; आणि एनएचपीसीचे चमेरा व पार्बती प्रकल्प यांचा समावेश आहे, सोबत राज्याचे स्वतःचे व अनेक लहान जलविद्युत प्रकल्प. राज्याला अनेक प्रकल्पांतून स्वामित्वधन म्हणून मोफत वीज मिळते आणि ते जादा वीज इतर राज्यांना विकते, विशेषतः उन्हाळ्यात जेव्हा बर्फ वितळून नद्या फुगतात. जलविद्युत विकासाने नाजूक खोऱ्यांत भूस्खलन, बोगदे खोदणे व नदी परिसंस्थेबाबत चिंताही निर्माण केल्या आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Identified hydro potential and capacity harnessed", "चिह्नित जलविद्युत क्षमता और उपयोग की गई क्षमता", "निश्चित जलविद्युत क्षमता व वापरलेली क्षमता"), "cea", "CEA hydro potential assessment / HP Directorate of Energy."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Despite its terrain, Himachal has good mobile coverage in most inhabited valleys. Citizen services are delivered online through the State's e-district portal and Lok Mitra Kendras, and the HIMSWAN network links government offices. IIT Mandi and IIIT Una are the main technology institutes, and Shimla and Dharamshala host small IT and data-centre facilities.",
        "भूभाग के बावजूद हिमाचल की अधिकांश बसी घाटियों में मोबाइल कवरेज अच्छा है। राज्य के ई-डिस्ट्रिक्ट पोर्टल और लोक मित्र केंद्रों के माध्यम से नागरिक सेवाएँ ऑनलाइन दी जाती हैं, और हिमस्वान नेटवर्क सरकारी कार्यालयों को जोड़ता है। आईआईटी मंडी और आईआईआईटी ऊना मुख्य प्रौद्योगिकी संस्थान हैं, और शिमला व धर्मशाला में छोटी आईटी और डेटा सेंटर सुविधाएँ हैं।",
        "भूप्रदेश कठीण असूनही हिमाचलच्या बहुतेक वस्ती असलेल्या खोऱ्यांत मोबाइल कव्हरेज चांगले आहे. राज्याच्या ई-डिस्ट्रिक्ट संकेतस्थळ व लोकमित्र केंद्रांमार्फत नागरी सेवा ऑनलाइन दिल्या जातात, आणि हिमस्वान जाळे सरकारी कार्यालये जोडते. आयआयटी मंडी व आयआयआयटी ऊना या मुख्य तंत्रज्ञान संस्था आहेत, आणि शिमला व धर्मशाला येथे लहान आयटी व डेटा सेंटर सुविधा आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Himachal Pradesh circle)."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("HP", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["HP"]
ger = AP["aishe_ger"]["HP"]; nu = AP["aishe_universities_2021_22"]["HP"]; nc = AP["aishe_colleges_2021_22"]["HP"]
module(R, "education", [
    prose("p1", L(
        f"Himachal Pradesh has one of India's best education records. Literacy at the 2011 Census was 82.8%, and the higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE, well above the national 28.4% and up from {ger['2017-18']}% in 2017-18; women's GER ({gf}%) was far higher than men's ({gm}%). The State had {nu} universities and {inr(nc)} colleges.\n\nHimachal Pradesh University in Shimla (1970), Dr Y. S. Parmar University of Horticulture and Forestry at Nauni near Solan, and CSK Himachal Pradesh Krishi Vishvavidyalaya at Palampur are the main State universities, and the Central University of Himachal Pradesh is at Dharamshala. National institutions include IIT Mandi, NIT Hamirpur, IIM Sirmaur, IIIT Una and AIIMS Bilaspur; the Indian Institute of Advanced Study occupies the former Viceregal Lodge in Shimla, and the Lawrence School, Sanawar, is one of India's oldest boarding schools.",
        f"हिमाचल प्रदेश का शिक्षा रिकॉर्ड भारत में सबसे अच्छे में है। 2011 की जनगणना में साक्षरता 82.8% थी, और एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था, जो राष्ट्रीय 28.4% से काफ़ी अधिक और 2017-18 के {ger['2017-18']}% से ऊपर है; महिलाओं का जीईआर ({gf}%) पुरुषों ({gm}%) से कहीं अधिक था। राज्य में {nu} विश्वविद्यालय और {inr(nc)} कॉलेज थे।\n\nशिमला का हिमाचल प्रदेश विश्वविद्यालय (1970), सोलन के पास नौणी का डॉ. यशवंत सिंह परमार औद्यानिकी एवं वानिकी विश्वविद्यालय और पालमपुर का चौधरी सरवण कुमार हिमाचल प्रदेश कृषि विश्वविद्यालय मुख्य राज्य विश्वविद्यालय हैं, और हिमाचल प्रदेश केंद्रीय विश्वविद्यालय धर्मशाला में है। राष्ट्रीय संस्थानों में आईआईटी मंडी, एनआईटी हमीरपुर, आईआईएम सिरमौर, आईआईआईटी ऊना और एम्स बिलासपुर शामिल हैं; भारतीय उच्च अध्ययन संस्थान शिमला के पूर्व वाइसरीगल लॉज में है, और सनावर का लॉरेंस स्कूल भारत के सबसे पुराने आवासीय विद्यालयों में है।",
        f"हिमाचल प्रदेशचा शैक्षणिक विक्रम भारतातील सर्वोत्तमांपैकी आहे. 2011 च्या जनगणनेत साक्षरता 82.8% होती, आणि एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा बरेच अधिक व 2017-18 मधील {ger['2017-18']}% पेक्षा जास्त; स्त्रियांचे जीईआर ({gf}%) पुरुषांपेक्षा ({gm}%) कितीतरी अधिक होते. राज्यात {nu} विद्यापीठे व {inr(nc)} महाविद्यालये होती.\n\nशिमल्याचे हिमाचल प्रदेश विद्यापीठ (1970), सोलनजवळील नौणी येथील डॉ. यशवंतसिंह परमार फलोत्पादन व वनशास्त्र विद्यापीठ आणि पालमपूरचे चौधरी सरवण कुमार हिमाचल प्रदेश कृषी विद्यापीठ ही मुख्य राज्य विद्यापीठे आहेत, आणि हिमाचल प्रदेश केंद्रीय विद्यापीठ धर्मशालेत आहे. राष्ट्रीय संस्थांत आयआयटी मंडी, एनआयटी हमीरपूर, आयआयएम सिरमौर, आयआयआयटी ऊना व एम्स बिलासपूर यांचा समावेश आहे; भारतीय प्रगत अध्ययन संस्था शिमल्याच्या पूर्वीच्या व्हाइसरीगल लॉजमध्ये आहे, आणि सनावरची लॉरेन्स स्कूल ही भारतातील सर्वांत जुन्या निवासी शाळांपैकी एक आहे."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("hpu", "Himachal Pradesh University", "हिमाचल प्रदेश विश्वविद्यालय", "हिमाचल प्रदेश विद्यापीठ", m=("Shimla, 1970", "शिमला, 1970", "शिमला, 1970")),
        it3("nauni", "Dr Y. S. Parmar University of Horticulture and Forestry", "डॉ. वाई. एस. परमार औद्यानिकी एवं वानिकी विश्वविद्यालय", "डॉ. वाय. एस. परमार फलोत्पादन व वनशास्त्र विद्यापीठ", m=("Nauni, Solan", "नौणी, सोलन", "नौणी, सोलन")),
        it3("csk", "CSK HP Krishi Vishvavidyalaya", "सीएसके हिमाचल प्रदेश कृषि विश्वविद्यालय", "सीएसके हिमाचल प्रदेश कृषी विद्यापीठ", m=("Palampur", "पालमपुर", "पालमपूर")),
        it3("iitm", "IIT Mandi", "आईआईटी मंडी", "आयआयटी मंडी", m=("Kamand, Mandi", "कमांद, मंडी", "कमांद, मंडी")),
        it3("nith", "NIT Hamirpur", "एनआईटी हमीरपुर", "एनआयटी हमीरपूर", m=("Hamirpur", "हमीरपुर", "हमीरपूर")),
        it3("cuhp", "Central University of Himachal Pradesh", "हिमाचल प्रदेश केंद्रीय विश्वविद्यालय", "हिमाचल प्रदेश केंद्रीय विद्यापीठ", m=("Dharamshala", "धर्मशाला", "धर्मशाला")),
        it3("iias", "Indian Institute of Advanced Study", "भारतीय उच्च अध्ययन संस्थान", "भारतीय प्रगत अध्ययन संस्था", m=("Shimla", "शिमला", "शिमला")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["HP"]; s = C["srs"]["HP"]; le = C["le"]["HP"]
module(R, "health", [
    prose("p1", L(
        f"Himachal Pradesh's infant mortality rate fell from {s[4]} per 1,000 live births in 2010 to {s[5]:.0f} in 2020, well below the national 28, and the birth rate was {s[1]} per 1,000 (death rate {s[3]}). Life expectancy at birth was {le[2]} years in 2014-18, with women living much longer than men ({le[1]} against {le[0]}), above the national 69.4. Child nutrition is a concern: in NFHS-5, {n['stunted'][1]:.1f}% of children under five were stunted, {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight — all higher than in NFHS-4 — while {n['institutional_N5']:.1f}% of births took place in health facilities, up from 76.4%.\n\nIndira Gandhi Medical College in Shimla, AIIMS Bilaspur, Dr Rajendra Prasad Government Medical College at Tanda (Kangra) and the medical colleges at Nerchowk, Hamirpur, Chamba and Nahan are the main hospitals. Remote valleys depend on primary health centres, and winter snow can cut off access to care.",
        f"हिमाचल प्रदेश की शिशु मृत्यु दर 2010 में प्रति 1,000 जीवित जन्म पर {s[4]} से घटकर 2020 में {s[5]:.0f} हो गई, जो राष्ट्रीय 28 से काफ़ी कम है, और जन्म दर प्रति 1,000 पर {s[1]} थी (मृत्यु दर {s[3]})। 2014-18 में जन्म के समय जीवन प्रत्याशा {le[2]} वर्ष थी, और महिलाएँ पुरुषों से कहीं अधिक जीती हैं ({le[1]} बनाम {le[0]}), जो राष्ट्रीय 69.4 से अधिक है। बाल पोषण चिंता का विषय है: एनएफ़एचएस-5 में पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने, {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के थे — सभी एनएफ़एचएस-4 से अधिक — जबकि {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, जो 76.4% से बढ़े।\n\nशिमला का इंदिरा गांधी मेडिकल कॉलेज, एम्स बिलासपुर, टांडा (कांगड़ा) का डॉ. राजेंद्र प्रसाद राजकीय मेडिकल कॉलेज और नेरचौक, हमीरपुर, चंबा व नाहन के मेडिकल कॉलेज मुख्य अस्पताल हैं। दूरस्थ घाटियाँ प्राथमिक स्वास्थ्य केंद्रों पर निर्भर हैं, और सर्दियों की बर्फ़ इलाज तक पहुँच काट सकती है।",
        f"हिमाचल प्रदेशचा अर्भक मृत्युदर 2010 मध्ये दर 1,000 जिवंत जन्मांमागे {s[4]} वरून 2020 मध्ये {s[5]:.0f} वर आला, राष्ट्रीय 28 पेक्षा बराच कमी, आणि जन्मदर दर 1,000 मागे {s[1]} होता (मृत्युदर {s[3]}). 2014-18 मध्ये जन्मतः आयुर्मान {le[2]} वर्षे होते, आणि स्त्रिया पुरुषांपेक्षा कितीतरी अधिक जगतात ({le[1]} विरुद्ध {le[0]}), राष्ट्रीय 69.4 पेक्षा अधिक. बालपोषण ही चिंतेची बाब आहे: एनएफएचएस-5 मध्ये पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी, {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची होती — सर्व एनएफएचएस-4 पेक्षा अधिक — तर {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, 76.4% वरून वाढून.\n\nशिमल्याचे इंदिरा गांधी वैद्यकीय महाविद्यालय, एम्स बिलासपूर, टांडा (कांगडा) येथील डॉ. राजेंद्र प्रसाद शासकीय वैद्यकीय महाविद्यालय आणि नेरचौक, हमीरपूर, चंबा व नाहनची वैद्यकीय महाविद्यालये ही मुख्य रुग्णालये आहेत. दुर्गम खोरी प्राथमिक आरोग्य केंद्रांवर अवलंबून आहेत, आणि हिवाळ्यातील बर्फामुळे उपचारापर्यंत पोहोचणे बंद होऊ शकते."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(le[2], "years", "2014-18", "survey", "srs", ESI_LE, note=f"SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male {le[0]}, female {le[1]})."), "number", "higher-is-better",
             national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("HP"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("hp mod2 ok")
