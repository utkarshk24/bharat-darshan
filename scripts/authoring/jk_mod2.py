"""Jammu and Kashmir (UT) modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-JK"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_JK = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 24 Oct 2026. "
           "FY2025-26 is the latest year published for J&K and may be revised. MoSPI does not say whether years before FY2019-20 are recast for the present UT or relate to the former State including Ladakh.")
mo = research("mospi_jk.json")
C = research("census_b5plus.json")
NAME = L("Jammu and Kashmir", "जम्मू और कश्मीर", "जम्मू व काश्मीर")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Kashmiri culture blends Shaiva, Buddhist and Sufi traditions — often summed up as Kashmiriyat. The 14th-century mystic Lal Ded (Lalleshwari) and the Sufi saint Nund Rishi (Sheikh Noor-ud-din) founded Kashmiri poetry with their vakhs and shruks, and the lyrics of Habba Khatoon are still sung. Sufiana kalam is the valley's classical music, played on the santoor, sitar and saz; chakri and ladishah are folk forms; women dance the rouf at festivals; and bhand pather is a satirical folk theatre. Jammu's Dogra culture has its own songs and dances, such as the kud, and the Pahari schools of painting flourished at Basohli and Jammu. Kashmir's crafts — pashmina, Kani and sozani shawls, hand-knotted carpets, papier-mâché, walnut-wood carving, khatamband ceilings, namda rugs and willow bats — carry registered GIs.",
        "कश्मीरी संस्कृति शैव, बौद्ध और सूफ़ी परंपराओं का मेल है — जिसे अक्सर कश्मीरियत कहा जाता है। 14वीं सदी की संत कवयित्री लल द्यद (ललेश्वरी) और सूफ़ी संत नुंद ऋषि (शेख़ नूरुद्दीन) ने अपने वाखों और श्रुखों से कश्मीरी कविता की नींव रखी, और हब्बा ख़ातून के गीत आज भी गाए जाते हैं। सूफ़ियाना कलाम घाटी का शास्त्रीय संगीत है, जो संतूर, सितार और साज़ पर बजता है; चकरी और लड़ीशाह लोक रूप हैं; महिलाएँ त्योहारों पर रउफ़ नृत्य करती हैं; और भांड पथेर व्यंग्यात्मक लोकनाट्य है। जम्मू की डोगरा संस्कृति के अपने गीत और नृत्य हैं, जैसे कुड, और बसोहली व जम्मू में पहाड़ी चित्र शैलियाँ फली-फूलीं। कश्मीर के शिल्प — पश्मीना, कानी और सोज़नी शॉल, हाथ से गाँठे क़ालीन, पेपर माशी, अखरोट की लकड़ी की नक़्क़ाशी, ख़तमबंद छतें, नमदा और विलो बल्ले — पंजीकृत जीआई हैं।",
        "काश्मिरी संस्कृती शैव, बौद्ध व सूफी परंपरांचा संगम आहे — ज्याला अनेकदा काश्मिरियत म्हणतात. चौदाव्या शतकातील संत कवयित्री लल द्यद (ललेश्वरी) व सूफी संत नुंद ऋषी (शेख नूरुद्दीन) यांनी आपल्या वाख व श्रुखांनी काश्मिरी काव्याचा पाया घातला, आणि हब्बा खातूनची गीते आजही गायली जातात. सूफियाना कलाम हे खोऱ्याचे शास्त्रीय संगीत आहे, जे संतूर, सतार व साझवर वाजते; चकरी व लडीशाह हे लोकप्रकार आहेत; स्त्रिया सणांना रऊफ नृत्य करतात; आणि भांड पथेर हे उपहासात्मक लोकनाट्य आहे. जम्मूच्या डोग्रा संस्कृतीची स्वतःची गाणी व नृत्ये आहेत, जसे कुड, आणि बसोहली व जम्मू येथे पहाडी चित्रशैली बहरल्या. काश्मीरच्या हस्तकला — पश्मीना, कानी व सोझनी शाली, हाताने विणलेले गालिचे, पेपर-माशे, अक्रोडाच्या लाकडावरील कोरीवकाम, खतमबंद छते, नमदा व विलो बॅट — नोंदणीकृत जीआय आहेत."),
        sources=["gi-registry"], conf="Editorial"),
    lst("festivals", [
        fest("eid", "Eid-ul-Fitr and Eid-ul-Adha", "ईद-उल-फ़ितर और ईद-उल-अज़हा", "ईद-उल-फित्र व ईद-उल-अजहा", ("Islamic calendar", "इस्लामी कैलेंडर", "इस्लामी दिनदर्शिका"),
             ("Prayers at the Eidgah and Hazratbal; family feasts.", "ईदगाह और हज़रतबल में नमाज़; पारिवारिक भोज।", "ईदगाह व हजरतबलमध्ये नमाज; कौटुंबिक मेजवान्या.")),
        fest("kheer", "Mela Kheer Bhawani", "मेला खीर भवानी", "मेळा खीर भवानी", ("May–June (Jyeshtha Ashtami)", "मई–जून (ज्येष्ठ अष्टमी)", "मे–जून (ज्येष्ठ अष्टमी)"),
             ("Kashmiri Pandit pilgrimage to the spring temple at Tulmul, Ganderbal.", "गांदरबल के तुलमुल में झरने वाले मंदिर की कश्मीरी पंडित तीर्थयात्रा।", "गांदरबलच्या तुलमुल येथील झऱ्याच्या मंदिराची काश्मिरी पंडित यात्रा.")),
        fest("amarnath", "Amarnath Yatra", "अमरनाथ यात्रा", "अमरनाथ यात्रा", ("July–August", "जुलाई–अगस्त", "जुलै–ऑगस्ट"),
             ("Pilgrimage to the ice lingam in the Amarnath cave.", "अमरनाथ गुफा के हिम लिंग की तीर्थयात्रा।", "अमरनाथ गुहेतील हिमलिंगाची यात्रा.")),
        fest("navratri", "Navratri at Vaishno Devi", "वैष्णो देवी में नवरात्रि", "वैष्णोदेवी येथे नवरात्र", ("March–April and September–October", "मार्च–अप्रैल और सितंबर–अक्टूबर", "मार्च–एप्रिल व सप्टेंबर–ऑक्टोबर"),
             ("Peak pilgrim season at Katra.", "कटरा में तीर्थयात्रियों का चरम मौसम।", "कटरा येथे यात्रेकरूंचा मुख्य हंगाम.")),
        fest("lohri", "Lohri and Baisakhi", "लोहड़ी और बैसाखी", "लोहडी व बैसाखी", ("January and April", "जनवरी और अप्रैल", "जानेवारी व एप्रिल"),
             ("Harvest festivals of the Jammu region.", "जम्मू क्षेत्र के फ़सल उत्सव।", "जम्मू प्रदेशातील सुगीचे सण.")),
        fest("tulip", "Tulip Festival", "ट्यूलिप उत्सव", "ट्युलिप महोत्सव", ("March–April", "मार्च–अप्रैल", "मार्च–एप्रिल"),
             ("At the Indira Gandhi Memorial Tulip Garden, Srinagar.", "श्रीनगर के इंदिरा गांधी स्मारक ट्यूलिप उद्यान में।", "श्रीनगरच्या इंदिरा गांधी स्मारक ट्युलिप उद्यानात.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("sufiana", "Sufiana kalam", "सूफ़ियाना कलाम", "सूफियाना कलाम"), it3("rouf", "Rouf dance", "रउफ़ नृत्य", "रऊफ नृत्य"),
        it3("bhand", "Bhand pather", "भांड पथेर", "भांड पथेर"), it3("kud", "Kud dance (Jammu)", "कुड नृत्य (जम्मू)", "कुड नृत्य (जम्मू)"),
        it3("pashmina", "Pashmina", "पश्मीना", "पश्मीना"), it3("papier", "Papier-mâché", "पेपर माशी", "पेपर-माशे"),
        it3("basohli", "Basohli painting", "बसोहली चित्रकला", "बसोहली चित्रकला"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("wazwan", "Wazwan", "वाज़वान", "वाझवान", d=("Multi-course feast with rista, rogan josh and gushtaba.", "रिस्ता, रोगन जोश और गुश्ताबा वाला कई व्यंजनों का भोज।", "रिस्ता, रोगन जोश व गुश्ताबा असलेली अनेक पदार्थांची मेजवानी.")),
        it3("kahwa", "Kahwa and noon chai", "कहवा और नून चाय", "कहवा व नून चाय", d=("Saffron-almond green tea, and pink salt tea with bread.", "केसर-बादाम वाली हरी चाय, और रोटी के साथ गुलाबी नमकीन चाय।", "केशर-बदामाचा हिरवा चहा, आणि पावासोबत गुलाबी खारट चहा.")),
        it3("dum", "Dum aloo and haak", "दम आलू और हाक", "दम आलू व हाक", d=("Kashmiri potato curry and collard greens.", "कश्मीरी आलू की सब्ज़ी और हाक साग।", "काश्मिरी बटाट्याची भाजी व हाक पालेभाजी.")),
        it3("kalari", "Kalari kulcha", "कलाड़ी कुलचा", "कलाडी कुलचा", d=("Udhampur's ripened cheese, fried, in bread — a registered GI.", "उधमपुर का पका पनीर, तला हुआ, कुलचे में — पंजीकृत जीआई।", "उधमपूरचे मुरवलेले चीज, तळून, कुलच्यात — नोंदणीकृत जीआय.")),
        it3("rajmash", "Rajmash-chawal", "राजमाश-चावल", "राजमा-भात", d=("Bhaderwah and Jammu kidney beans with rice.", "भद्रवाह और जम्मू के राजमा के साथ चावल।", "भद्रवाह व जम्मूचा राजमा भातासोबत.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("pheran", "Pheran", "फ़िरन", "फिरन", d=("Long loose woollen gown worn by men and women in winter.", "सर्दियों में पुरुषों और महिलाओं का लंबा ढीला ऊनी चोगा।", "हिवाळ्यात पुरुष व स्त्रियांचा लांब सैल लोकरी झगा.")),
        it3("dogra", "Dogra kurta-churidar and dupatta", "डोगरा कुर्ता-चूड़ीदार और दुपट्टा", "डोग्रा कुर्ता-चुडीदार व ओढणी", d=("Traditional dress of the Jammu region.", "जम्मू क्षेत्र की पारंपरिक पोशाक।", "जम्मू प्रदेशाचा पारंपरिक पोशाख.")),
        it3("gojri", "Gujjar and Bakarwal dress", "गुज्जर और बकरवाल पोशाक", "गुज्जर व बकरवाल पोशाख", d=("Embroidered caps and turbans of the pastoral communities.", "पशुपालक समुदायों की कढ़ाईदार टोपियाँ और पगड़ियाँ।", "पशुपालक समुदायांच्या भरतकाम केलेल्या टोप्या व पगड्या.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; pa = 100 * g["public_admin"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["JK"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["JK"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Jammu and Kashmir's GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26, the latest year published in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2025-26'][0])}, below the national average. In FY2024-25 agriculture, horticulture and livestock made up about {agri:.0f}% of GSVA and public administration about {pa:.0f}% — an unusually large share that reflects the weight of government employment — while manufacturing was only about {mfg:.0f}%. Apples, walnuts, almonds, cherries and Kashmir saffron are the most valuable crops, and handicrafts, carpets and shawls employ many artisans. Tourism and pilgrimage — to Srinagar, Gulmarg, Pahalgam, Vaishno Devi and Amarnath — are major earners, and hydro-electric stations on the Chenab and Jhelum supply power to the northern grid.\n\nThe PLFS unemployment rate was {ur['2025']}% in 2025 (India {ui['2025']}%), and {lf['female']}% of women aged 15 and above were in the labour force — well above the national {lfi['female']}%.",
        f"मोस्पी शृंखला में प्रकाशित नवीनतम वर्ष, वित्त वर्ष 2025-26 में जम्मू और कश्मीर का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2025-26'][0])} था, जो राष्ट्रीय औसत से कम है। वित्त वर्ष 2024-25 में जीएसवीए में कृषि, बाग़वानी और पशुपालन का हिस्सा लगभग {agri:.0f}% और लोक प्रशासन का लगभग {pa:.0f}% था — एक असामान्य रूप से बड़ा हिस्सा जो सरकारी रोज़गार के महत्त्व को दर्शाता है — जबकि विनिर्माण केवल लगभग {mfg:.0f}% था। सेब, अखरोट, बादाम, चेरी और कश्मीरी केसर सबसे मूल्यवान फ़सलें हैं, और हस्तशिल्प, क़ालीन और शॉलें बहुत से कारीगरों को रोज़गार देते हैं। पर्यटन और तीर्थयात्रा — श्रीनगर, गुलमर्ग, पहलगाम, वैष्णो देवी और अमरनाथ — कमाई के बड़े स्रोत हैं, और चिनाब व झेलम पर बने जलविद्युत केंद्र उत्तरी ग्रिड को बिजली देते हैं।\n\nपीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी (भारत {ui['2025']}%), और 15 वर्ष से अधिक आयु की {lf['female']}% महिलाएँ श्रम बल में थीं — राष्ट्रीय {lfi['female']}% से काफ़ी अधिक।",
        f"मोस्पी मालिकेत प्रकाशित नवीनतम वर्ष, आ.व. 2025-26 मध्ये जम्मू व काश्मीरचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2025-26'][0])} होते, जे राष्ट्रीय सरासरीपेक्षा कमी आहे. आ.व. 2024-25 मध्ये जीएसव्हीएमध्ये शेती, फलोत्पादन व पशुपालनाचा वाटा सुमारे {agri:.0f}% आणि लोकप्रशासनाचा सुमारे {pa:.0f}% होता — असामान्यपणे मोठा वाटा, जो सरकारी रोजगाराचे महत्त्व दाखवतो — तर उत्पादन उद्योग केवळ सुमारे {mfg:.0f}% होता. सफरचंद, अक्रोड, बदाम, चेरी व काश्मिरी केशर ही सर्वांत मौल्यवान पिके आहेत, आणि हस्तकला, गालिचे व शाली अनेक कारागिरांना रोजगार देतात. पर्यटन व तीर्थयात्रा — श्रीनगर, गुलमर्ग, पहलगाम, वैष्णोदेवी व अमरनाथ — हे उत्पन्नाचे मोठे स्रोत आहेत, आणि चिनाब व झेलमवरील जलविद्युत केंद्रे उत्तर ग्रीडला वीज पुरवतात.\n\nपीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता (भारत {ui['2025']}%), आणि 15 वर्षांवरील {lf['female']}% स्त्रिया श्रमशक्तीत होत्या — राष्ट्रीय {lfi['female']}% पेक्षा बऱ्याच अधिक."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_JK), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_JK), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_JK), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("JK", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    plfs_series("JK", NAME),
    lst("sectors-key", [
        it3("horti", "Horticulture", "बाग़वानी", "फलोत्पादन", d=("Apples of Shopian, Sopore and Baramulla; walnuts, almonds and cherries.", "शोपियाँ, सोपोर और बारामूला के सेब; अखरोट, बादाम और चेरी।", "शोपियां, सोपोर व बारामुल्लाची सफरचंदे; अक्रोड, बदाम व चेरी.")),
        it3("saffron", "Saffron", "केसर", "केशर", d=("Grown on the karewas of Pampore; a registered GI.", "पांपोर के करेवों पर उगाया जाता है; पंजीकृत जीआई।", "पांपोरच्या करेवांवर पिकते; नोंदणीकृत जीआय.")),
        it3("crafts", "Handicrafts and carpets", "हस्तशिल्प और क़ालीन", "हस्तकला व गालिचे", d=("Shawls, carpets, papier-mâché and woodwork.", "शॉल, क़ालीन, पेपर माशी और काष्ठ कार्य।", "शाली, गालिचे, पेपर-माशे व काष्ठकाम.")),
        it3("tourism", "Tourism and pilgrimage", "पर्यटन और तीर्थयात्रा", "पर्यटन व तीर्थयात्रा", d=("Srinagar, Gulmarg, Pahalgam, Vaishno Devi, Amarnath.", "श्रीनगर, गुलमर्ग, पहलगाम, वैष्णो देवी, अमरनाथ।", "श्रीनगर, गुलमर्ग, पहलगाम, वैष्णोदेवी, अमरनाथ.")),
        it3("hydro", "Hydro-electricity", "जलविद्युत", "जलविद्युत", d=("Salal, Baglihar, Dulhasti, Uri and Kishanganga stations.", "सलाल, बगलिहार, दुलहस्ती, उड़ी और किशनगंगा केंद्र।", "सलाल, बगलिहार, दुलहस्ती, उरी व किशनगंगा केंद्रे.")),
        it3("bats", "Willow bats", "विलो बल्ले", "विलो बॅट", d=("Made from Kashmir willow in Anantnag and Pulwama.", "अनंतनाग और पुलवामा में कश्मीरी विलो से बने।", "अनंतनाग व पुलवामामध्ये काश्मिरी विलोपासून बनवलेल्या.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Comparable GSDP series for the present UT before FY2019-20", "वित्त वर्ष 2019-20 से पहले वर्तमान केंद्र शासित प्रदेश की तुलनीय जीएसडीपी शृंखला", "आ.व. 2019-20 पूर्वीची सध्याच्या केंद्रशासित प्रदेशाची तुलनीय जीएसडीपी मालिका"), "jk-des", "Confirm with the J&K DES whether the MoSPI back series excludes Ladakh."),
        (L("Apple and saffron production", "सेब और केसर उत्पादन", "सफरचंद व केशर उत्पादन"), "india-gov", "J&K Horticulture and Agriculture Departments."),
        (L("Tourist arrivals by year", "वर्षवार पर्यटक आगमन", "वर्षनिहाय पर्यटक आगमन"), "tourism", "J&K Tourism Department."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Under the Jammu and Kashmir Reorganisation Act, 2019, the Union Territory has a Lieutenant Governor appointed by the President and an elected Legislative Assembly of 90 members, with seats redrawn by the Delimitation Commission in 2022 (43 in the Jammu division and 47 in the Kashmir division); the Lieutenant Governor may also nominate members. Police and public order remain with the Lieutenant Governor. The UT elects 5 members to the Lok Sabha and 4 to the Rajya Sabha.\n\nThe first Assembly election of the UT was held in three phases in September–October 2024. The Jammu & Kashmir National Conference, in alliance with the Congress, formed the government, and Omar Abdullah was sworn in as Chief Minister on 16 October 2024; Abdul Rahim Rather (JKNC) was elected Speaker. Manoj Sinha has been Lieutenant Governor since August 2020. Restoration of statehood remains a major political question.",
        "जम्मू और कश्मीर पुनर्गठन अधिनियम, 2019 के तहत केंद्र शासित प्रदेश में राष्ट्रपति द्वारा नियुक्त उपराज्यपाल और 90 सदस्यों वाली निर्वाचित विधानसभा है, जिसकी सीटें 2022 में परिसीमन आयोग ने नए सिरे से तय कीं (जम्मू संभाग में 43 और कश्मीर संभाग में 47); उपराज्यपाल सदस्य मनोनीत भी कर सकते हैं। पुलिस और लोक व्यवस्था उपराज्यपाल के पास रहती है। केंद्र शासित प्रदेश से लोकसभा के 5 और राज्यसभा के 4 सदस्य चुने जाते हैं।\n\nकेंद्र शासित प्रदेश का पहला विधानसभा चुनाव सितंबर–अक्टूबर 2024 में तीन चरणों में हुआ। जम्मू एंड कश्मीर नेशनल कॉन्फ़्रेंस ने कांग्रेस के साथ गठबंधन में सरकार बनाई, और उमर अब्दुल्ला ने 16 अक्टूबर 2024 को मुख्यमंत्री पद की शपथ ली; अब्दुल रहीम राथर (नेशनल कॉन्फ़्रेंस) अध्यक्ष चुने गए। मनोज सिन्हा अगस्त 2020 से उपराज्यपाल हैं। राज्य का दर्जा बहाल करना एक प्रमुख राजनीतिक प्रश्न बना हुआ है।",
        "जम्मू व काश्मीर पुनर्रचना कायदा, 2019 अंतर्गत केंद्रशासित प्रदेशात राष्ट्रपतींनी नियुक्त केलेले नायब राज्यपाल आणि 90 सदस्यांची निवडून आलेली विधानसभा आहे, जिच्या जागा 2022 मध्ये परिसीमन आयोगाने नव्याने ठरवल्या (जम्मू विभागात 43 व काश्मीर विभागात 47); नायब राज्यपाल सदस्यांचे नामनिर्देशनही करू शकतात. पोलीस व सार्वजनिक सुव्यवस्था नायब राज्यपालांकडे राहते. केंद्रशासित प्रदेशातून लोकसभेवर 5 व राज्यसभेवर 4 सदस्य निवडले जातात.\n\nकेंद्रशासित प्रदेशाची पहिली विधानसभा निवडणूक सप्टेंबर–ऑक्टोबर 2024 मध्ये तीन टप्प्यांत झाली. जम्मू अँड काश्मीर नॅशनल कॉन्फरन्सने काँग्रेससोबत आघाडी करून सरकार स्थापन केले, आणि उमर अब्दुल्ला यांनी 16 ऑक्टोबर 2024 रोजी मुख्यमंत्रिपदाची शपथ घेतली; अब्दुल रहीम राथर (नॅशनल कॉन्फरन्स) अध्यक्षपदी निवडले गेले. मनोज सिन्हा ऑगस्ट 2020 पासून नायब राज्यपाल आहेत. राज्याचा दर्जा पुनर्स्थापित करणे हा प्रमुख राजकीय प्रश्न राहिला आहे."),
        sources=["etv-bharat", "kashmir-reader", "newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("jkla", "J&K Legislative Assembly", "जम्मू-कश्मीर विधानसभा", "जम्मू-काश्मीर विधानसभा", url="https://jkla.nic.in", src="india-gov"),
        it3("portal", "Government of Jammu and Kashmir", "जम्मू और कश्मीर सरकार", "जम्मू व काश्मीर शासन", url="https://jk.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2024 Assembly election — party-wise result", "2024 विधानसभा चुनाव — दलवार परिणाम", "2024 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for J&K 2024."),
        (L("Deputy Chief Minister and Leader of Opposition — official notice", "उपमुख्यमंत्री और नेता प्रतिपक्ष — आधिकारिक सूचना", "उपमुख्यमंत्री व विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "General Administration Department / Assembly secretariat."),
        (L("Delimitation Commission final order (2022)", "परिसीमन आयोग का अंतिम आदेश (2022)", "परिसीमन आयोगाचा अंतिम आदेश (2022)"), "india-gov", "Gazette notification."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "The Udhampur–Srinagar–Baramulla Rail Link, with the Chenab and Anji Khad bridges, was dedicated to the nation in June 2025, giving the Kashmir valley an all-weather rail connection to the rest of India. Other large works include the Zojila and Z-Morh tunnels towards Ladakh, AIIMS Awantipora, and hydro-electric projects on the Chenab such as Pakal Dul, Kiru and Ratle; these will be added as cards once their status is confirmed from official sources. Each card shows its source and the date it was checked.",
        "चिनाब और अंजी खड्ड पुलों सहित उधमपुर–श्रीनगर–बारामूला रेल लिंक जून 2025 में राष्ट्र को समर्पित हुआ, जिससे कश्मीर घाटी को शेष भारत से हर मौसम में रेल संपर्क मिला। अन्य बड़े कार्यों में लद्दाख की ओर ज़ोजिला और ज़ेड-मोड़ सुरंगें, एम्स अवंतीपोरा, और चिनाब पर पाकल दुल, किरु और रतले जैसी जलविद्युत परियोजनाएँ शामिल हैं; आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर इन्हें कार्ड के रूप में जोड़ा जाएगा। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "चिनाब व अंजी खड्ड पुलांसह उधमपूर–श्रीनगर–बारामुल्ला रेल्वे मार्ग जून 2025 मध्ये राष्ट्राला समर्पित झाला, ज्यामुळे काश्मीर खोऱ्याला उर्वरित भारताशी सर्व हवामानातील रेल्वे जोडणी मिळाली. इतर मोठ्या कामांत लडाखकडे जाणारे झोजिला व झेड-मोड बोगदे, एम्स अवंतीपोरा आणि चिनाबवरील पाकल दुल, किरू व रतले यांसारखे जलविद्युत प्रकल्प यांचा समावेश आहे; अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर त्यांची कार्डे जोडली जातील. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["newsonair"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("USBRL length and Chenab bridge height — official figures", "यूएसबीआरएल की लंबाई और चिनाब पुल की ऊँचाई — आधिकारिक आँकड़े", "यूएसबीआरएलची लांबी व चिनाब पुलाची उंची — अधिकृत आकडे"), "railways", "Northern Railway / PIB."),
        (L("Zojila tunnel — status", "ज़ोजिला सुरंग — स्थिति", "झोजिला बोगदा — स्थिती"), "nhai", "NHIDCL project status."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Srinagar's Sheikh ul-Alam International Airport and Jammu airport are the main airports, both civil enclaves at Indian Air Force stations. National Highway 44 crosses the Pir Panjal from Jammu to Srinagar through the Chenani–Nashri and Navyug tunnels, and the Mughal Road links Poonch and Rajouri with Shopian when it is free of snow. Since 2025 trains run from Jammu and Katra across the Chenab bridge and through the Pir Panjal to Srinagar and Baramulla. In Srinagar, shikaras still ferry people across the Dal and Nigeen lakes.",
        "श्रीनगर का शेख़ उल-आलम अंतरराष्ट्रीय हवाई अड्डा और जम्मू हवाई अड्डा मुख्य हवाई अड्डे हैं, दोनों भारतीय वायु सेना के स्टेशनों पर नागरिक परिसर हैं। राष्ट्रीय राजमार्ग 44 चेनानी–नाशरी और नवयुग सुरंगों से होकर जम्मू से श्रीनगर तक पीर पंजाल पार करता है, और मुग़ल रोड बर्फ़ न होने पर पुंछ और राजौरी को शोपियाँ से जोड़ता है। 2025 से रेलगाड़ियाँ जम्मू और कटरा से चिनाब पुल पार कर और पीर पंजाल से होकर श्रीनगर और बारामूला तक चलती हैं। श्रीनगर में शिकारे आज भी लोगों को डल और निगीन झीलों के पार ले जाते हैं।",
        "श्रीनगरचे शेख उल-आलम आंतरराष्ट्रीय विमानतळ व जम्मू विमानतळ हे मुख्य विमानतळ आहेत, दोन्ही भारतीय हवाई दलाच्या तळांवरील नागरी विभाग. राष्ट्रीय महामार्ग 44 चेनानी–नाशरी व नवयुग बोगद्यांमधून जम्मूहून श्रीनगरपर्यंत पीर पंजाल ओलांडतो, आणि मुघल रोड बर्फ नसताना पुंछ व राजौरीला शोपियांशी जोडतो. 2025 पासून रेल्वेगाड्या जम्मू व कटराहून चिनाब पूल ओलांडून व पीर पंजालमधून श्रीनगर व बारामुल्लापर्यंत धावतात. श्रीनगरमध्ये शिकारे आजही लोकांना दल व निगीन सरोवरांपलीकडे नेतात."),
        conf="Editorial"),
    lst("airports", [
        it3("sxr", "Sheikh ul-Alam International Airport, Srinagar", "शेख़ उल-आलम अंतरराष्ट्रीय हवाई अड्डा, श्रीनगर", "शेख उल-आलम आंतरराष्ट्रीय विमानतळ, श्रीनगर", m=("SXR", "SXR", "SXR")),
        it3("ixj", "Jammu Airport", "जम्मू हवाई अड्डा", "जम्मू विमानतळ", m=("IXJ", "IXJ", "IXJ")),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Jammu and Kashmir's power comes mostly from hydro-electricity. NHPC operates large stations on the Chenab (Salal, Dulhasti) and the Jhelum basin (Uri, Kishanganga), the UT's own Baglihar station is on the Chenab, and several more Chenab projects — Pakal Dul, Kiru, Kwar and Ratle — are being built. The rivers run low in winter, when demand for heating peaks, so the UT imports power and winter power cuts are common in the valley.",
        "जम्मू और कश्मीर की बिजली अधिकतर जलविद्युत से आती है। एनएचपीसी चिनाब (सलाल, दुलहस्ती) और झेलम बेसिन (उड़ी, किशनगंगा) पर बड़े केंद्र चलाता है, केंद्र शासित प्रदेश का अपना बगलिहार केंद्र चिनाब पर है, और चिनाब पर कई और परियोजनाएँ — पाकल दुल, किरु, क्वार और रतले — बन रही हैं। सर्दियों में नदियों का प्रवाह कम होता है, जब तापन की माँग चरम पर होती है, इसलिए केंद्र शासित प्रदेश बिजली आयात करता है और घाटी में सर्दियों में बिजली कटौती आम है।",
        "जम्मू व काश्मीरची वीज बहुतांश जलविद्युतमधून येते. एनएचपीसी चिनाब (सलाल, दुलहस्ती) व झेलम खोऱ्यात (उरी, किशनगंगा) मोठी केंद्रे चालवते, केंद्रशासित प्रदेशाचे स्वतःचे बगलिहार केंद्र चिनाबवर आहे, आणि चिनाबवरील आणखी काही प्रकल्प — पाकल दुल, किरू, क्वार व रतले — उभारले जात आहेत. हिवाळ्यात नद्यांचा प्रवाह कमी होतो, तेव्हा उबेची मागणी शिखरावर असते, म्हणून केंद्रशासित प्रदेश वीज आयात करतो आणि खोऱ्यात हिवाळ्यात वीजकपात सामान्य असते."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Chenab projects — status and capacity", "चिनाब परियोजनाएँ — स्थिति और क्षमता", "चिनाब प्रकल्प — स्थिती व क्षमता"), "cea", "NHPC / CVPPL project pages."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Mobile and internet services in Jammu and Kashmir have at times been suspended for security reasons, most extensively after August 2019, and connectivity in remote border areas remains limited. Citizen services are increasingly delivered online, and IT parks have been set up in Srinagar and Jammu, while IIT Jammu and NIT Srinagar train engineers for the region.",
        "जम्मू और कश्मीर में मोबाइल और इंटरनेट सेवाएँ समय-समय पर सुरक्षा कारणों से निलंबित की गई हैं, सबसे व्यापक रूप से अगस्त 2019 के बाद, और दूरस्थ सीमावर्ती क्षेत्रों में संपर्क अब भी सीमित है। नागरिक सेवाएँ अधिकाधिक ऑनलाइन दी जा रही हैं, और श्रीनगर व जम्मू में आईटी पार्क बनाए गए हैं, जबकि आईआईटी जम्मू और एनआईटी श्रीनगर क्षेत्र के लिए इंजीनियर तैयार करते हैं।",
        "जम्मू व काश्मीरमध्ये मोबाइल व इंटरनेट सेवा वेळोवेळी सुरक्षेच्या कारणांनी स्थगित केल्या गेल्या आहेत, सर्वाधिक व्यापकपणे ऑगस्ट 2019 नंतर, आणि दुर्गम सीमावर्ती भागांत जोडणी अजूनही मर्यादित आहे. नागरी सेवा अधिकाधिक ऑनलाइन दिल्या जात आहेत, आणि श्रीनगर व जम्मूमध्ये आयटी पार्क उभारले गेले आहेत, तर आयआयटी जम्मू व एनआयटी श्रीनगर प्रदेशासाठी अभियंते घडवतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (J&K circle)."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("JK", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["JK"]
ger = AP["aishe_ger"]["JK"]; nu = AP["aishe_universities_2021_22"]["JK"]; nc = AP["aishe_colleges_2021_22"]["JK"]
module(R, "education", [
    prose("p1", L(
        f"Literacy in the area of the present UT was 67.0% at the 2011 Census. The higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE, below the national 28.4%; women's GER ({gf}%) was higher than men's ({gm}%). AISHE reported {nu} universities and {inr(nc)} colleges in the UT. Years before 2019-20 relate to the former State, which included Ladakh.\n\nThe University of Kashmir (1948) and the University of Jammu (1969) are the oldest universities, joined by the Central Universities of Kashmir and Jammu, the Islamic University of Science and Technology at Awantipora, Shri Mata Vaishno Devi University at Katra and the agricultural universities (SKUAST) of Kashmir and Jammu. National institutions include IIT Jammu, IIM Jammu, NIT Srinagar and AIIMS Jammu, and the Sher-i-Kashmir Institute of Medical Sciences (SKIMS) at Soura is the main medical institute of the valley.",
        f"2011 की जनगणना में वर्तमान केंद्र शासित प्रदेश के क्षेत्र में साक्षरता 67.0% थी। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था, जो राष्ट्रीय 28.4% से कम है; महिलाओं का जीईआर ({gf}%) पुरुषों ({gm}%) से अधिक था। एआईएसएचई ने केंद्र शासित प्रदेश में {nu} विश्वविद्यालय और {inr(nc)} कॉलेज बताए। 2019-20 से पहले के वर्ष पूर्ववर्ती राज्य के हैं, जिसमें लद्दाख शामिल था।\n\nकश्मीर विश्वविद्यालय (1948) और जम्मू विश्वविद्यालय (1969) सबसे पुराने विश्वविद्यालय हैं, जिनके साथ कश्मीर और जम्मू के केंद्रीय विश्वविद्यालय, अवंतीपोरा का इस्लामिक यूनिवर्सिटी ऑफ़ साइंस एंड टेक्नोलॉजी, कटरा का श्री माता वैष्णो देवी विश्वविद्यालय और कश्मीर व जम्मू के कृषि विश्वविद्यालय (स्कास्ट) हैं। राष्ट्रीय संस्थानों में आईआईटी जम्मू, आईआईएम जम्मू, एनआईटी श्रीनगर और एम्स जम्मू शामिल हैं, और सौरा का शेर-ए-कश्मीर आयुर्विज्ञान संस्थान (स्किम्स) घाटी का मुख्य चिकित्सा संस्थान है।",
        f"2011 च्या जनगणनेत सध्याच्या केंद्रशासित प्रदेशाच्या क्षेत्रात साक्षरता 67.0% होती. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा कमी; स्त्रियांचे जीईआर ({gf}%) पुरुषांपेक्षा ({gm}%) अधिक होते. एआयएसएचईने केंद्रशासित प्रदेशात {nu} विद्यापीठे व {inr(nc)} महाविद्यालये नोंदवली. 2019-20 पूर्वीची वर्षे पूर्वीच्या राज्याची आहेत, ज्यात लडाखचा समावेश होता.\n\nकाश्मीर विद्यापीठ (1948) व जम्मू विद्यापीठ (1969) ही सर्वांत जुनी विद्यापीठे आहेत, सोबत काश्मीर व जम्मूची केंद्रीय विद्यापीठे, अवंतीपोराचे इस्लामिक युनिव्हर्सिटी ऑफ सायन्स अँड टेक्नॉलॉजी, कटराचे श्री माता वैष्णोदेवी विद्यापीठ आणि काश्मीर व जम्मूची कृषी विद्यापीठे (स्कास्ट). राष्ट्रीय संस्थांत आयआयटी जम्मू, आयआयएम जम्मू, एनआयटी श्रीनगर व एम्स जम्मू यांचा समावेश आहे, आणि सौराचे शेर-ए-काश्मीर आयुर्विज्ञान संस्थान (स्किम्स) ही खोऱ्यातील मुख्य वैद्यकीय संस्था आहे."),
        sources=["aishe", "jk-des"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("ku", "University of Kashmir", "कश्मीर विश्वविद्यालय", "काश्मीर विद्यापीठ", m=("Srinagar, 1948", "श्रीनगर, 1948", "श्रीनगर, 1948")),
        it3("ju", "University of Jammu", "जम्मू विश्वविद्यालय", "जम्मू विद्यापीठ", m=("Jammu, 1969", "जम्मू, 1969", "जम्मू, 1969")),
        it3("iitj", "IIT Jammu", "आईआईटी जम्मू", "आयआयटी जम्मू", m=("Jagti, Jammu", "जगती, जम्मू", "जगती, जम्मू")),
        it3("iimj", "IIM Jammu", "आईआईएम जम्मू", "आयआयएम जम्मू", m=("Jammu", "जम्मू", "जम्मू")),
        it3("nits", "NIT Srinagar", "एनआईटी श्रीनगर", "एनआयटी श्रीनगर", m=("Hazratbal, Srinagar", "हज़रतबल, श्रीनगर", "हजरतबल, श्रीनगर")),
        it3("aiimsj", "AIIMS Jammu", "एम्स जम्मू", "एम्स जम्मू", m=("Vijaypur, Samba", "विजयपुर, सांबा", "विजयपूर, सांबा")),
        it3("skims", "SKIMS", "स्किम्स", "स्किम्स", m=("Soura, Srinagar", "सौरा, श्रीनगर", "सौरा, श्रीनगर")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["JK"]; s = C["srs"]["JK"]; le = C["le"]["JK_incl_LA"]
module(R, "health", [
    prose("p1", L(
        f"The Sample Registration System reports an infant mortality rate of {s[5]:.0f} per 1,000 live births in 2020, down from {s[4]:.0f} in 2010 and well below the national 28, a birth rate of {s[1]} and a death rate of {s[3]} per 1,000 — among the lowest death rates in India. Life expectancy at birth was {le[2]} years in 2014-18 (men {le[0]}, women {le[1]}), above the national 69.4; this figure includes Ladakh. In NFHS-5 (2019-21), {n['stunted'][1]:.1f}% of children under five were stunted, {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight, and {n['institutional_N5']:.1f}% of births took place in health facilities; the NFHS-4 figures shown for comparison cover the former State including Ladakh.\n\nSKIMS Soura, the Government Medical Colleges in Srinagar and Jammu, AIIMS Jammu and newer medical colleges in district towns are the main hospitals; AIIMS Awantipora is being built for the valley.",
        f"नमूना पंजीकरण प्रणाली के अनुसार 2020 में शिशु मृत्यु दर प्रति 1,000 जीवित जन्म पर {s[5]:.0f} थी, जो 2010 के {s[4]:.0f} से कम और राष्ट्रीय 28 से काफ़ी नीचे है, जन्म दर {s[1]} और मृत्यु दर प्रति 1,000 पर {s[3]} — भारत में सबसे कम मृत्यु दरों में। 2014-18 में जन्म के समय जीवन प्रत्याशा {le[2]} वर्ष थी (पुरुष {le[0]}, महिलाएँ {le[1]}), जो राष्ट्रीय 69.4 से अधिक है; इस आँकड़े में लद्दाख शामिल है। एनएफ़एचएस-5 (2019-21) में पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने, {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के थे, और {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए; तुलना के लिए दिखाए गए एनएफ़एचएस-4 के आँकड़े लद्दाख सहित पूर्ववर्ती राज्य के हैं।\n\nस्किम्स सौरा, श्रीनगर और जम्मू के सरकारी मेडिकल कॉलेज, एम्स जम्मू और ज़िला नगरों के नए मेडिकल कॉलेज मुख्य अस्पताल हैं; घाटी के लिए एम्स अवंतीपोरा बनाया जा रहा है।",
        f"नमुना नोंदणी पद्धतीनुसार 2020 मध्ये अर्भक मृत्युदर दर 1,000 जिवंत जन्मांमागे {s[5]:.0f} होता, 2010 मधील {s[4]:.0f} पेक्षा कमी व राष्ट्रीय 28 पेक्षा बराच खाली, जन्मदर {s[1]} व मृत्युदर दर 1,000 मागे {s[3]} — भारतातील सर्वांत कमी मृत्युदरांपैकी. 2014-18 मध्ये जन्मतः आयुर्मान {le[2]} वर्षे होते (पुरुष {le[0]}, स्त्रिया {le[1]}), राष्ट्रीय 69.4 पेक्षा अधिक; या आकड्यात लडाखचा समावेश आहे. एनएफएचएस-5 (2019-21) मध्ये पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी, {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची होती, आणि {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या; तुलनेसाठी दाखवलेले एनएफएचएस-4 चे आकडे लडाखसह पूर्वीच्या राज्याचे आहेत.\n\nस्किम्स सौरा, श्रीनगर व जम्मूची शासकीय वैद्यकीय महाविद्यालये, एम्स जम्मू आणि जिल्हा शहरांतील नवी वैद्यकीय महाविद्यालये ही मुख्य रुग्णालये आहेत; खोऱ्यासाठी एम्स अवंतीपोरा उभारले जात आहे."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS, note="Former State including Ladakh."), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(le[2], "years", "2014-18", "survey", "srs", ESI_LE, note=f"SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male {le[0]}, female {le[1]}); includes Ladakh."), "number", "higher-is-better",
             national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("JK"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Whether SRS 2020 figures cover the UT alone", "क्या एसआरएस 2020 के आँकड़े केवल केंद्र शासित प्रदेश के हैं", "एसआरएस 2020 चे आकडे केवळ केंद्रशासित प्रदेशाचे आहेत का"), "srs", "Check the SRS Statistical Report 2020 table notes."),
        (L("AIIMS Awantipora — status", "एम्स अवंतीपोरा — स्थिति", "एम्स अवंतीपोरा — स्थिती"), "mohfw", "PMSSY status."),
    ]),
])
print("jk mod2 ok")
