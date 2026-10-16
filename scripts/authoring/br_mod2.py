"""Bihar modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-BR"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
CM_PRE = "https://www.newsonair.gov.in/bihar-samrat-choudhary-elected-as-bjp-legislature-party-leader/"
NOTE_BR = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 16 Oct 2026. "
           "FY2025-26 is the latest year published for Bihar and may be revised.")
mo = research("mospi_br.json")
NAME = L("Bihar", "बिहार", "बिहार")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Bihar's culture is shaped by its languages and its rivers. Maithili literature goes back to the 14th-century poet Vidyapati, whose songs are still sung; Bhojpuri has a vast folk-song tradition and a popular film and music industry, and Bhikhari Thakur, the 'Shakespeare of Bhojpuri', created the Bidesia theatre about migrant life. Hindi writers Ramdhari Singh 'Dinkar', Phanishwar Nath 'Renu' and Nagarjun came from Bihar. Madhubani (Mithila) painting, once made on the walls of homes by women, is now known worldwide, and Manjusha art of Bhagalpur tells the legend of Bihula. Folk singers such as Sharda Sinha made Chhath songs loved across India.\n\nCrafts include Bhagalpur tussar silk, Sujini embroidery, applique (khatwa) work, Sikki grass products, and stone carving at Gaya.",
        "बिहार की संस्कृति उसकी भाषाओं और नदियों से बनी है। मैथिली साहित्य 14वीं सदी के कवि विद्यापति तक जाता है, जिनके गीत आज भी गाए जाते हैं; भोजपुरी में लोकगीतों की विशाल परंपरा और लोकप्रिय फ़िल्म व संगीत उद्योग है, और 'भोजपुरी के शेक्सपियर' भिखारी ठाकुर ने प्रवासी जीवन पर बिदेसिया रंगमंच रचा। हिंदी लेखक रामधारी सिंह 'दिनकर', फणीश्वरनाथ 'रेणु' और नागार्जुन बिहार से थे। मधुबनी (मिथिला) चित्रकला, जो कभी महिलाएँ घरों की दीवारों पर बनाती थीं, अब विश्व प्रसिद्ध है, और भागलपुर की मंजूषा कला बिहुला की कथा कहती है। शारदा सिन्हा जैसी लोकगायिकाओं ने छठ के गीतों को पूरे भारत में प्रिय बनाया।\n\nशिल्पों में भागलपुरी तसर रेशम, सुजनी कढ़ाई, एप्लिक (खटवा) काम, सिक्की घास उत्पाद और गया की पत्थर नक्काशी शामिल हैं।",
        "बिहारची संस्कृती त्याच्या भाषा व नद्यांनी घडली आहे. मैथिली साहित्य चौदाव्या शतकातील कवी विद्यापतींपर्यंत जाते, ज्यांची गाणी आजही गायली जातात; भोजपुरीत लोकगीतांची विशाल परंपरा व लोकप्रिय चित्रपट व संगीत उद्योग आहे, आणि 'भोजपुरीचे शेक्सपिअर' भिखारी ठाकूर यांनी स्थलांतरितांच्या जीवनावर बिदेसिया रंगभूमी रचली. हिंदी लेखक रामधारी सिंह 'दिनकर', फणीश्वरनाथ 'रेणू' व नागार्जुन बिहारचे होते. मधुबनी (मिथिला) चित्रकला, जी पूर्वी स्त्रिया घरांच्या भिंतींवर काढत, आता जगप्रसिद्ध आहे, आणि भागलपूरची मंजूषा कला बिहुलेची कथा सांगते. शारदा सिन्हा यांसारख्या लोकगायिकांनी छठची गाणी भारतभर लोकप्रिय केली.\n\nहस्तकलेत भागलपुरी टसर रेशीम, सुजनी भरतकाम, ऍप्लिक (खटवा) काम, सिक्की गवत उत्पादने व गयाचे दगडी कोरीवकाम यांचा समावेश आहे."),
        conf="Editorial"),
    lst("festivals", [
        fest("chhath", "Chhath", "छठ", "छठ", ("October–November; also in spring", "अक्टूबर–नवंबर; वसंत में भी", "ऑक्टोबर–नोव्हेंबर; वसंतातही"),
             ("Four days of fasting and prayers to the setting and rising sun at rivers and ponds.", "नदियों और तालाबों पर डूबते और उगते सूर्य की उपासना और चार दिन का व्रत।", "नद्या व तलावांवर मावळत्या व उगवत्या सूर्याची उपासना व चार दिवसांचे व्रत.")),
        fest("sonepur", "Sonepur Mela", "सोनपुर मेला", "सोनपूर जत्रा", ("November (Kartik Purnima)", "नवंबर (कार्तिक पूर्णिमा)", "नोव्हेंबर (कार्तिक पौर्णिमा)"),
             ("Great livestock and trade fair where the Gandak meets the Ganga.", "गंडक और गंगा के संगम पर विशाल पशु और व्यापार मेला।", "गंडक व गंगेच्या संगमावर मोठी पशू व व्यापारी जत्रा.")),
        fest("shravani", "Shravani Mela", "श्रावणी मेला", "श्रावणी मेळा", ("July–August", "जुलाई–अगस्त", "जुलै–ऑगस्ट"),
             ("Pilgrims carry Ganga water from Sultanganj to Deoghar.", "तीर्थयात्री सुल्तानगंज से देवघर तक गंगाजल ले जाते हैं।", "यात्रेकरू सुलतानगंजहून देवघरपर्यंत गंगाजल नेतात.")),
        fest("pitrapaksha", "Pitru Paksha at Gaya", "गया में पितृपक्ष", "गया येथे पितृपक्ष", ("September", "सितंबर", "सप्टेंबर"),
             ("Ancestral rites on the Phalgu draw pilgrims from across India.", "फल्गु पर पितरों के श्राद्ध के लिए पूरे भारत से तीर्थयात्री आते हैं।", "फल्गूवरील श्राद्धविधींसाठी भारतभरातून यात्रेकरू येतात.")),
        fest("buddha", "Buddha Purnima and Eid", "बुद्ध पूर्णिमा और ईद", "बुद्धपौर्णिमा व ईद", ("Various", "विभिन्न", "विविध"),
             ("Celebrated widely; Bodh Gaya draws pilgrims from Asia.", "व्यापक रूप से मनाए जाते हैं; बोधगया में एशिया भर से तीर्थयात्री आते हैं।", "मोठ्या प्रमाणावर साजरे; बोधगयेला आशियाभरातून यात्रेकरू येतात.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("madhubani", "Madhubani painting", "मधुबनी चित्रकला", "मधुबनी चित्रकला"), it3("manjusha", "Manjusha art", "मंजूषा कला", "मंजूषा कला"),
        it3("bidesia", "Bidesia theatre", "बिदेसिया रंगमंच", "बिदेसिया रंगभूमी"), it3("sujini", "Sujini embroidery", "सुजनी कढ़ाई", "सुजनी भरतकाम"),
        it3("sikki", "Sikki grass craft", "सिक्की घास शिल्प", "सिक्की गवत हस्तकला"), it3("jatjatin", "Jat-Jatin dance", "जट-जटिन नृत्य", "जट-जटिन नृत्य"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("litti", "Litti chokha", "लिट्टी चोखा", "लिट्टी चोखा", d=("Sattu-stuffed wheat balls roasted on coals, with mashed brinjal, tomato and potato.", "सत्तू भरी गेहूँ की लिट्टी अंगारों पर सेंकी, भुने बैंगन, टमाटर और आलू के चोखे के साथ।", "सत्तू भरलेल्या गव्हाच्या लिट्ट्या निखाऱ्यावर भाजलेल्या, वांगे, टोमॅटो व बटाट्याच्या चोख्यासह.")),
        it3("sattu", "Sattu", "सत्तू", "सत्तू", d=("Roasted gram flour, drunk as a summer cooler or eaten with onion and chilli.", "भुने चने का आटा, गर्मियों में शरबत के रूप में पिया जाता है या प्याज़ और मिर्च के साथ खाया जाता है।", "भाजलेल्या हरभऱ्याचे पीठ, उन्हाळ्यात सरबत म्हणून प्यायले जाते किंवा कांदा-मिरचीसोबत खाल्ले जाते.")),
        it3("thekua", "Thekua", "ठेकुआ", "ठेकुआ", d=("Jaggery-wheat cookies made for Chhath.", "छठ के लिए बनने वाले गुड़-गेहूँ के ठेकुए।", "छठसाठी बनवले जाणारे गूळ-गव्हाचे ठेकुए.")),
        it3("makhana", "Makhana", "मखाना", "मखाणा", d=("Fox nuts from the ponds of Mithila; a registered GI.", "मिथिला के तालाबों के मखाने; पंजीकृत जीआई।", "मिथिलेच्या तलावांतील मखाणे; नोंदणीकृत जीआय.")),
        it3("khaja", "Silao khaja", "सिलाव खाजा", "सिलाव खाजा", d=("Flaky layered sweet from Nalanda district; a registered GI.", "नालंदा ज़िले की परतदार मिठाई; पंजीकृत जीआई।", "नालंदा जिल्ह्याची पापुद्र्यांची मिठाई; नोंदणीकृत जीआय.")),
        it3("chura", "Chura-dahi", "चूड़ा-दही", "पोहे-दही", d=("Flattened rice with curd and jaggery, eaten on Makar Sankranti.", "दही और गुड़ के साथ चूड़ा, मकर संक्रांति पर।", "दही व गुळासह पोहे, मकर संक्रांतीला.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("saree", "Saree with sindoor and lahathi bangles", "सिंदूर और लहठी चूड़ियों के साथ साड़ी", "सिंदूर व लहठी बांगड्यांसह साडी", d=("Married women's festive dress; Bhagalpur silk for occasions.", "विवाहित महिलाओं की उत्सव पोशाक; अवसरों पर भागलपुरी रेशम।", "विवाहित स्त्रियांचा सणासुदीचा पोशाख; प्रसंगी भागलपुरी रेशीम.")),
        it3("dhoti", "Dhoti-kurta and gamchha", "धोती-कुर्ता और गमछा", "धोतर-कुर्ता व गमछा", d=("Everyday men's dress in villages.", "गाँवों में पुरुषों की रोज़ की पोशाक।", "गावांत पुरुषांचा रोजचा पोशाख.")),
        it3("paag", "Mithila paag", "मिथिला पाग", "मिथिला पाग", d=("Traditional headgear of Mithila, worn at ceremonies.", "मिथिला की पारंपरिक पगड़ी, समारोहों में पहनी जाती है।", "मिथिलेचे पारंपरिक शिरोभूषण, समारंभात परिधान केले जाते.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; cons = 100 * g["construction"] / g["total"]
module(R, "economy", [
    prose("p1", L(
        f"Bihar's GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26 in the MoSPI series, but per capita NSDP, at ₹{inr(pc['FY2025-26'][0])}, is the lowest of any State — less than half the national average. Agriculture, livestock and fishing made up about {agri:.0f}% of GSVA in FY2024-25. Farmers grow rice, wheat and maize, and Bihar is the leading producer of makhana and litchi; vegetables, fish and dairy (through the COMFED 'Sudha' co-operatives) matter too. Construction, at about {cons:.0f}% of GSVA, is unusually large, reflecting road, bridge and housing works, while manufacturing is small at about {mfg:.0f}% — the Barauni refinery and fertiliser plant, sugar mills, food processing and handlooms. Money sent home by workers in other States and abroad is an important source of income.\n\nThe PLFS unemployment rate was 3.8% in 2025, and labour-force participation was low — 49.3% of persons aged 15 and above, and 24.7% of women.",
        f"मोस्पी शृंखला में वित्त वर्ष 2025-26 में बिहार का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ था, लेकिन ₹{inr(pc['FY2025-26'][0])} का प्रति व्यक्ति एनएसडीपी किसी भी राज्य में सबसे कम है — राष्ट्रीय औसत के आधे से भी कम। वित्त वर्ष 2024-25 में कृषि, पशुपालन और मत्स्य पालन जीएसवीए का लगभग {agri:.0f}% थे। किसान धान, गेहूँ और मक्का उगाते हैं, और बिहार मखाना और लीची का अग्रणी उत्पादक है; सब्ज़ियाँ, मछली और डेयरी (कॉम्फ़ेड 'सुधा' सहकारी समितियों के माध्यम से) भी महत्त्वपूर्ण हैं। लगभग {cons:.0f}% के साथ निर्माण का हिस्सा असामान्य रूप से बड़ा है, जो सड़क, पुल और आवास कार्यों को दर्शाता है, जबकि विनिर्माण लगभग {mfg:.0f}% पर छोटा है — बरौनी रिफ़ाइनरी और उर्वरक संयंत्र, चीनी मिलें, खाद्य प्रसंस्करण और हथकरघा। दूसरे राज्यों और विदेश में काम करने वाले श्रमिकों द्वारा घर भेजा गया पैसा आय का महत्त्वपूर्ण स्रोत है।\n\n2025 में पीएलएफ़एस बेरोज़गारी दर 3.8% थी, और श्रम बल भागीदारी कम थी — 15 वर्ष से अधिक आयु के व्यक्तियों में 49.3% और महिलाओं में 24.7%।",
        f"मोस्पी मालिकेनुसार आ.व. 2025-26 मध्ये बिहारचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी होते, पण ₹{inr(pc['FY2025-26'][0])} चे दरडोई एनएसडीपी कोणत्याही राज्यातील सर्वांत कमी आहे — राष्ट्रीय सरासरीच्या निम्म्याहूनही कमी. आ.व. 2024-25 मध्ये शेती, पशुपालन व मत्स्यव्यवसायाचा जीएसव्हीएमध्ये सुमारे {agri:.0f}% वाटा होता. शेतकरी भात, गहू व मका पिकवतात, आणि बिहार मखाणा व लिचीचा आघाडीचा उत्पादक आहे; भाज्या, मासे व दुग्धव्यवसाय (कॉम्फेड 'सुधा' सहकारी संस्थांमार्फत) हेही महत्त्वाचे आहेत. सुमारे {cons:.0f}% सह बांधकामाचा वाटा असामान्यपणे मोठा आहे, जो रस्ते, पूल व गृहनिर्माणाची कामे दर्शवतो, तर उत्पादन उद्योग सुमारे {mfg:.0f}% वर लहान आहे — बरौनी रिफायनरी व खत कारखाना, साखर कारखाने, अन्नप्रक्रिया व हातमाग. इतर राज्यांत व परदेशात काम करणाऱ्या कामगारांनी घरी पाठवलेला पैसा हा उत्पन्नाचा महत्त्वाचा स्रोत आहे.\n\n2025 मध्ये पीएलएफएस बेरोजगारी दर 3.8% होता, आणि श्रमशक्ती सहभाग कमी होता — 15 वर्षांवरील व्यक्तींमध्ये 49.3% व स्त्रियांमध्ये 24.7%."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_BR), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_BR), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_BR), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("BR", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    plfs_series("BR", NAME),
    lst("sectors-key", [
        it3("agri", "Rice, wheat and maize", "धान, गेहूँ और मक्का", "भात, गहू व मका", d=("Across the Gangetic plain; maize in the Kosi region.", "पूरे गंगा मैदान में; कोसी क्षेत्र में मक्का।", "संपूर्ण गंगा मैदानात; कोसी प्रदेशात मका.")),
        it3("makhana", "Makhana and litchi", "मखाना और लीची", "मखाणा व लिची", d=("Mithila ponds; Muzaffarpur orchards.", "मिथिला के तालाब; मुज़फ़्फ़रपुर के बाग़।", "मिथिलेचे तलाव; मुझफ्फरपूरच्या बागा.")),
        it3("dairy", "Dairy and fisheries", "डेयरी और मत्स्य पालन", "दुग्धव्यवसाय व मत्स्यव्यवसाय", d=("COMFED (Sudha) co-operatives; pond and river fisheries.", "कॉम्फ़ेड (सुधा) सहकारी समितियाँ; तालाब और नदी मत्स्य पालन।", "कॉम्फेड (सुधा) सहकारी संस्था; तलाव व नदी मत्स्यव्यवसाय.")),
        it3("refinery", "Refining and fertiliser", "शोधन और उर्वरक", "शुद्धीकरण व खते", d=("Barauni refinery and fertiliser plant.", "बरौनी रिफ़ाइनरी और उर्वरक संयंत्र।", "बरौनी रिफायनरी व खत कारखाना.")),
        it3("silk", "Silk and handlooms", "रेशम और हथकरघा", "रेशीम व हातमाग", d=("Bhagalpur tussar silk.", "भागलपुरी तसर रेशम।", "भागलपुरी टसर रेशीम.")),
        it3("construction", "Construction", "निर्माण", "बांधकाम", d=("Roads, bridges and housing.", "सड़कें, पुल और आवास।", "रस्ते, पूल व गृहनिर्माण.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Makhana and litchi production", "मखाना और लीची उत्पादन", "मखाणा व लिची उत्पादन"), "india-gov", "Bihar Economic Survey / Ministry of Agriculture horticulture statistics."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Bihar has a bicameral legislature: a 243-member Legislative Assembly and a 75-member Legislative Council in Patna. The State elects 40 members to the Lok Sabha and 16 to the Rajya Sabha.\n\nIn the Assembly election of November 2025 the National Democratic Alliance won a majority, with the BJP the single largest party at 89 seats (News On AIR), and Nitish Kumar of the JD(U), who had led most governments since 2005, continued as Chief Minister. In April 2026 he resigned on his election to the Rajya Sabha. Samrat Choudhary of the BJP was elected leader of the NDA legislature party and sworn in on 15 April 2026 — the first Chief Minister from the BJP in Bihar — with Vijay Kumar Chaudhary and Bijendra Prasad Yadav of the JD(U) as Deputy Chief Ministers. Prem Kumar (BJP) is Speaker, and Lt Gen (Retd) Syed Ata Hasnain became Governor in March 2026.",
        "बिहार में द्विसदनीय विधानमंडल है: पटना में 243 सदस्यों वाली विधानसभा और 75 सदस्यों वाली विधान परिषद। राज्य से लोकसभा के 40 और राज्यसभा के 16 सदस्य चुने जाते हैं।\n\nनवंबर 2025 के विधानसभा चुनाव में राष्ट्रीय जनतांत्रिक गठबंधन को बहुमत मिला, और भाजपा 89 सीटों के साथ सबसे बड़ा दल बनी (न्यूज़ ऑन एआईआर); 2005 से अधिकांश सरकारों का नेतृत्व करने वाले जदयू के नीतीश कुमार मुख्यमंत्री बने रहे। अप्रैल 2026 में राज्यसभा के लिए चुने जाने पर उन्होंने इस्तीफ़ा दिया। भाजपा के सम्राट चौधरी राजग विधायक दल के नेता चुने गए और 15 अप्रैल 2026 को शपथ ली — बिहार में भाजपा के पहले मुख्यमंत्री — और जदयू के विजय कुमार चौधरी व बिजेंद्र प्रसाद यादव उपमुख्यमंत्री बने। प्रेम कुमार (भाजपा) अध्यक्ष हैं, और लेफ़्टिनेंट जनरल (से.नि.) सैयद अता हसनैन मार्च 2026 में राज्यपाल बने।",
        "बिहारमध्ये द्विसदनी विधिमंडळ आहे: पाटण्यात 243 सदस्यांची विधानसभा व 75 सदस्यांची विधान परिषद. राज्यातून लोकसभेवर 40 आणि राज्यसभेवर 16 सदस्य निवडले जातात.\n\nनोव्हेंबर 2025 च्या विधानसभा निवडणुकीत राष्ट्रीय लोकशाही आघाडीला बहुमत मिळाले, आणि भाजप 89 जागांसह सर्वांत मोठा पक्ष ठरला (न्यूज ऑन एआयआर); 2005 पासून बहुतेक सरकारांचे नेतृत्व करणारे जदयूचे नितीश कुमार मुख्यमंत्रिपदी राहिले. एप्रिल 2026 मध्ये राज्यसभेवर निवड झाल्यावर त्यांनी राजीनामा दिला. भाजपचे सम्राट चौधरी रालोआ विधिमंडळ पक्षाचे नेते निवडले गेले आणि 15 एप्रिल 2026 रोजी शपथ घेतली — बिहारमधील भाजपचे पहिले मुख्यमंत्री — आणि जदयूचे विजय कुमार चौधरी व बिजेंद्र प्रसाद यादव उपमुख्यमंत्री झाले. प्रेम कुमार (भाजप) अध्यक्ष आहेत, आणि लेफ्टनंट जनरल (निवृत्त) सय्यद अता हसनैन मार्च 2026 मध्ये राज्यपाल झाले."),
        sources=["newsonair", "bihar-lokbhavan"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("noa", "News On AIR: NDA legislature party elects new leader (14 Apr 2026)", "न्यूज़ ऑन एआईआर: राजग विधायक दल ने नया नेता चुना (14 अप्रैल 2026)", "न्यूज ऑन एआयआर: रालोआ विधिमंडळ पक्षाने नवा नेता निवडला (14 एप्रिल 2026)", url=CM_PRE, src="newsonair"),
        it3("lokbhavan", "Lok Bhavan, Bihar", "लोक भवन, बिहार", "लोक भवन, बिहार", url="https://governor.bih.nic.in", src="bihar-lokbhavan"),
        it3("portal", "Government of Bihar", "बिहार सरकार", "बिहार शासन", url="https://state.bihar.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2025 Assembly election — full party-wise result", "2025 विधानसभा चुनाव — दलवार पूरा परिणाम", "2025 विधानसभा निवडणूक — पक्षनिहाय संपूर्ण निकाल"), "eci", "ECI statistical report or Form-20; the results website could not be read as a final table here."),
        (L("Leader of Opposition — official notice", "नेता प्रतिपक्ष — आधिकारिक सूचना", "विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "Assembly secretariat."),
        (L("Local bodies by type", "प्रकार के अनुसार स्थानीय निकाय", "प्रकारानुसार स्थानिक स्वराज्य संस्था"), "india-gov", "Panchayati Raj and Urban Development departments."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Patna's first metro stretch opened in October 2025, and work on AIIMS Darbhanga, the State's second AIIMS, began in November 2024. Bihar's other large works include new bridges over the Ganga and Kosi, expressways and flood-control embankments. Each card shows its source and the date it was checked.",
        "पटना का पहला मेट्रो खंड अक्टूबर 2025 में खुला, और राज्य के दूसरे एम्स, एम्स दरभंगा, का काम नवंबर 2024 में शुरू हुआ। बिहार के अन्य बड़े कार्यों में गंगा और कोसी पर नए पुल, एक्सप्रेसवे और बाढ़ नियंत्रण तटबंध शामिल हैं। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "पाटण्याचा पहिला मेट्रो टप्पा ऑक्टोबर 2025 मध्ये सुरू झाला, आणि राज्याच्या दुसऱ्या एम्सचे, एम्स दरभंगाचे काम नोव्हेंबर 2024 मध्ये सुरू झाले. बिहारच्या इतर मोठ्या कामांत गंगा व कोसीवरील नवे पूल, द्रुतगती मार्ग व पूरनियंत्रण बांध यांचा समावेश आहे. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["newsonair"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("New Ganga bridges (Aguwani Ghat–Sultanganj and others) — status", "गंगा के नए पुल (अगुवानी घाट–सुल्तानगंज आदि) — स्थिति", "गंगेवरील नवे पूल (अगुवानी घाट–सुलतानगंज इ.) — स्थिती"), "india-gov", "Bihar Rajya Pul Nirman Nigam / NHAI."),
        (L("Bihta airport — status", "बिहटा हवाई अड्डा — स्थिति", "बिहटा विमानतळ — स्थिती"), "aai", "Airports Authority of India."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Patna's Jay Prakash Narayan Airport is the busiest in the State; Gaya has an international airport used by Buddhist pilgrims, and Darbhanga has an airport serving north Bihar. Hajipur is the headquarters of the East Central Railway, and lines from Delhi to Kolkata pass through Patna, Gaya and Bhagalpur. Bridges are vital in a State split by the Ganga: the Mahatma Gandhi Setu at Patna was long among India's longest river bridges, and newer rail-cum-road bridges link Patna with Sonepur and Munger with the north bank. The Ganga is National Waterway 1, with a cargo terminal at Patna, and Patna has a new metro.",
        "पटना का जयप्रकाश नारायण हवाई अड्डा राज्य का सबसे व्यस्त हवाई अड्डा है; गया में बौद्ध तीर्थयात्रियों के लिए अंतरराष्ट्रीय हवाई अड्डा है, और दरभंगा का हवाई अड्डा उत्तर बिहार को सेवा देता है। हाजीपुर पूर्व मध्य रेलवे का मुख्यालय है, और दिल्ली से कोलकाता की लाइनें पटना, गया और भागलपुर से होकर जाती हैं। गंगा से बँटे राज्य में पुल अहम हैं: पटना का महात्मा गांधी सेतु लंबे समय तक भारत के सबसे लंबे नदी पुलों में था, और नए रेल-सह-सड़क पुल पटना को सोनपुर से और मुंगेर को उत्तरी तट से जोड़ते हैं। गंगा राष्ट्रीय जलमार्ग 1 है, जिसका माल टर्मिनल पटना में है, और पटना में नई मेट्रो है।",
        "पाटण्याचे जयप्रकाश नारायण विमानतळ हे राज्यातील सर्वांत व्यस्त विमानतळ आहे; गया येथे बौद्ध यात्रेकरूंसाठी आंतरराष्ट्रीय विमानतळ आहे, आणि दरभंग्याचे विमानतळ उत्तर बिहारला सेवा देते. हाजीपूर हे पूर्व मध्य रेल्वेचे मुख्यालय आहे, आणि दिल्ली ते कोलकाता मार्ग पाटणा, गया व भागलपूरवरून जातात. गंगेने विभागलेल्या राज्यात पूल महत्त्वाचे आहेत: पाटण्याचा महात्मा गांधी सेतू दीर्घकाळ भारतातील सर्वांत लांब नदीपुलांपैकी होता, आणि नवे रेल्वे-सह-रस्ते पूल पाटण्याला सोनपूरशी व मुंगेरला उत्तर किनाऱ्याशी जोडतात. गंगा हा राष्ट्रीय जलमार्ग 1 असून त्याचे मालवाहतूक टर्मिनल पाटण्यात आहे, आणि पाटण्यात नवी मेट्रो आहे."),
        conf="Editorial"),
    lst("airports", [
        it3("pat", "Jay Prakash Narayan Airport, Patna", "जयप्रकाश नारायण हवाई अड्डा, पटना", "जयप्रकाश नारायण विमानतळ, पाटणा", m=("PAT", "PAT", "PAT")),
        it3("gay", "Gaya International Airport", "गया अंतरराष्ट्रीय हवाई अड्डा", "गया आंतरराष्ट्रीय विमानतळ", m=("GAY", "GAY", "GAY")),
        it3("dbr", "Darbhanga", "दरभंगा", "दरभंगा", m=("DBR", "DBR", "DBR")),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Bihar has no coal mines of its own after the separation of Jharkhand, and depends largely on central-sector coal stations — NTPC's Barh, Kahalgaon, Nabinagar and Kanti plants and Barauni — and on power bought from other States. Electricity supply has expanded greatly in the last decade, reaching nearly every village. The State is adding solar capacity, including canal-top and floating plants, and the Barauni refinery is being expanded.",
        "झारखंड के अलग होने के बाद बिहार के पास अपनी कोयला खदानें नहीं हैं, और यह मुख्यतः केंद्रीय क्षेत्र के कोयला संयंत्रों — एनटीपीसी के बाढ़, कहलगाँव, नबीनगर और कांटी संयंत्र और बरौनी — और दूसरे राज्यों से ख़रीदी गई बिजली पर निर्भर है। पिछले दशक में बिजली आपूर्ति बहुत बढ़ी है और लगभग हर गाँव तक पहुँची है। राज्य नहरों पर और तैरते संयंत्रों सहित सौर क्षमता जोड़ रहा है, और बरौनी रिफ़ाइनरी का विस्तार हो रहा है।",
        "झारखंड वेगळे झाल्यानंतर बिहारकडे स्वतःच्या कोळसा खाणी नाहीत, आणि ते मुख्यतः केंद्रीय क्षेत्रातील कोळसा केंद्रांवर — एनटीपीसीची बाढ, कहलगाव, नबीनगर व कांटी केंद्रे आणि बरौनी — आणि इतर राज्यांकडून विकत घेतलेल्या विजेवर अवलंबून आहे. गेल्या दशकात वीजपुरवठा मोठ्या प्रमाणावर वाढला असून जवळपास प्रत्येक गावात पोहोचला आहे. राज्य कालव्यांवरील व तरंगत्या प्रकल्पांसह सौरक्षमता वाढवत आहे, आणि बरौनी रिफायनरीचा विस्तार होत आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Bihar's technology sector is small but growing, centred on Patna, where the State has set up an IT tower and start-up incubators, and on institutions such as IIT Patna. The State runs many services online, from land records to certificates, and mobile phones and digital payments have spread quickly in rural areas.",
        "बिहार का प्रौद्योगिकी क्षेत्र छोटा लेकिन बढ़ता हुआ है, जो पटना पर केंद्रित है, जहाँ राज्य ने आईटी टावर और स्टार्टअप इनक्यूबेटर बनाए हैं, और आईआईटी पटना जैसे संस्थानों पर। राज्य भूमि अभिलेखों से लेकर प्रमाणपत्रों तक कई सेवाएँ ऑनलाइन चलाता है, और ग्रामीण क्षेत्रों में मोबाइल फ़ोन और डिजिटल भुगतान तेज़ी से फैले हैं।",
        "बिहारचे तंत्रज्ञान क्षेत्र लहान पण वाढते आहे, पाटण्यावर केंद्रित, जिथे राज्याने आयटी टॉवर व स्टार्टअप इन्क्युबेटर्स उभारले आहेत, आणि आयआयटी पाटणासारख्या संस्थांवर. राज्य जमिनीच्या नोंदींपासून प्रमाणपत्रांपर्यंत अनेक सेवा ऑनलाइन चालवते, आणि ग्रामीण भागात मोबाइल फोन व डिजिटल पेमेंट झपाट्याने पसरले आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Bihar circle, which includes Jharkhand)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("BR", NAME)
module(R, "education", [
    prose("p1", L(
        "Higher education in Bihar has grown from a low base: the gross enrolment ratio (ages 18–23) rose from 11.4% in 2017-18 to 17.1% in 2021-22 in AISHE, but remained among the lowest in India and well below the national 28.4%; men's GER was 17.8% and women's 16.3%. With 37 universities and 1,092 colleges for a very large young population, colleges are crowded and many students study in other States. Literacy at the 2011 Census was 61.8%, the lowest of any State.\n\nPatna University (1917) and the NIT at Patna, which traces its origins to 1886, are among the oldest institutions. Newer national institutions include IIT Patna, AIIMS Patna, IIM Bodh Gaya, Chanakya National Law University, the Central University of South Bihar and the revived Nalanda University at Rajgir.",
        "बिहार में उच्च शिक्षा कम आधार से बढ़ी है: एआईएसएचई के अनुसार सकल नामांकन अनुपात (18–23 आयु) 2017-18 के 11.4% से बढ़कर 2021-22 में 17.1% हुआ, लेकिन भारत में सबसे कम में रहा और राष्ट्रीय 28.4% से काफ़ी नीचे; पुरुषों का जीईआर 17.8% और महिलाओं का 16.3% था। बहुत बड़ी युवा आबादी के लिए 37 विश्वविद्यालयों और 1,092 कॉलेजों के कारण कॉलेजों में भीड़ है और बहुत से छात्र दूसरे राज्यों में पढ़ते हैं। 2011 की जनगणना में साक्षरता 61.8% थी, जो किसी भी राज्य में सबसे कम है।\n\nपटना विश्वविद्यालय (1917) और 1886 से अपनी शुरुआत मानने वाला पटना का एनआईटी सबसे पुराने संस्थानों में हैं। नए राष्ट्रीय संस्थानों में आईआईटी पटना, एम्स पटना, आईआईएम बोधगया, चाणक्य राष्ट्रीय विधि विश्वविद्यालय, दक्षिण बिहार केंद्रीय विश्वविद्यालय और राजगीर में पुनर्जीवित नालंदा विश्वविद्यालय शामिल हैं।",
        "बिहारमध्ये उच्चशिक्षण कमी पायापासून वाढले आहे: एआयएसएचईनुसार एकूण नोंदणी गुणोत्तर (18–23 वय) 2017-18 मधील 11.4% वरून 2021-22 मध्ये 17.1% झाले, पण ते भारतातील सर्वांत कमींपैकी आणि राष्ट्रीय 28.4% पेक्षा बरेच खाली राहिले; पुरुषांचे जीईआर 17.8% व स्त्रियांचे 16.3% होते. खूप मोठ्या तरुण लोकसंख्येसाठी 37 विद्यापीठे व 1,092 महाविद्यालये असल्याने महाविद्यालयांत गर्दी असते आणि अनेक विद्यार्थी इतर राज्यांत शिकतात. 2011 च्या जनगणनेत साक्षरता 61.8% होती — कोणत्याही राज्यातील सर्वांत कमी.\n\nपाटणा विद्यापीठ (1917) व 1886 पासून आपली सुरुवात मानणारे पाटण्याचे एनआयटी या सर्वांत जुन्या संस्थांपैकी आहेत. नव्या राष्ट्रीय संस्थांत आयआयटी पाटणा, एम्स पाटणा, आयआयएम बोधगया, चाणक्य राष्ट्रीय विधी विद्यापीठ, दक्षिण बिहार केंद्रीय विद्यापीठ व राजगीर येथील पुनरुज्जीवित नालंदा विद्यापीठ यांचा समावेश आहे."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("pu", "Patna University", "पटना विश्वविद्यालय", "पाटणा विद्यापीठ", m=("Patna, 1917", "पटना, 1917", "पाटणा, 1917")),
        it3("iitp", "IIT Patna", "आईआईटी पटना", "आयआयटी पाटणा", m=("Bihta", "बिहटा", "बिहटा")),
        it3("aiimsp", "AIIMS Patna", "एम्स पटना", "एम्स पाटणा", m=("Phulwari Sharif", "फुलवारी शरीफ़", "फुलवारी शरीफ")),
        it3("iimbg", "IIM Bodh Gaya", "आईआईएम बोधगया", "आयआयएम बोधगया", m=("Bodh Gaya", "बोधगया", "बोधगया")),
        it3("nalanda", "Nalanda University", "नालंदा विश्वविद्यालय", "नालंदा विद्यापीठ", m=("Rajgir", "राजगीर", "राजगीर")),
        it3("cnlu", "Chanakya National Law University", "चाणक्य राष्ट्रीय विधि विश्वविद्यालय", "चाणक्य राष्ट्रीय विधी विद्यापीठ", m=("Patna", "पटना", "पाटणा")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Literacy by sex (Census 2011)", "लिंग के अनुसार साक्षरता (जनगणना 2011)", "लिंगनिहाय साक्षरता (जनगणना 2011)"), "census", "Primary Census Abstract."),
    ]),
])

# ---------------- O. Health ----------------
module(R, "health", [
    prose("p1", L(
        "Bihar's infant mortality rate fell from 48 per 1,000 live births in 2010 to 27 in 2020, just below the national 28, but its birth rate — 25.5 per 1,000 in 2020 — was the highest of any State. Life expectancy at birth was 69.1 years in 2014-18, and unusually men (69.4) lived slightly longer than women (68.7). Child undernutrition is among the most severe in India: in NFHS-5, 42.9% of children under five were stunted, 22.9% wasted and 41.0% underweight, though stunting fell from 48.3% in NFHS-4. About 76.2% of births took place in health facilities, below the national 88.6%.\n\nAIIMS Patna, the Indira Gandhi Institute of Medical Sciences and Patna Medical College are the main referral hospitals, and AIIMS Darbhanga is being built.",
        "बिहार की शिशु मृत्यु दर 2010 में प्रति 1,000 जीवित जन्म पर 48 से घटकर 2020 में 27 हो गई, जो राष्ट्रीय 28 से थोड़ी कम है, लेकिन इसकी जन्म दर — 2020 में प्रति 1,000 पर 25.5 — किसी भी राज्य में सबसे अधिक थी। 2014-18 में जन्म के समय जीवन प्रत्याशा 69.1 वर्ष थी, और असामान्य रूप से पुरुष (69.4) महिलाओं (68.7) से थोड़ा अधिक जीते थे। बाल कुपोषण भारत में सबसे गंभीर स्थितियों में है: एनएफ़एचएस-5 में पाँच वर्ष से कम आयु के 42.9% बच्चे ठिगने, 22.9% दुबले और 41.0% कम वज़न के थे, हालाँकि ठिगनापन एनएफ़एचएस-4 के 48.3% से घटा। लगभग 76.2% प्रसव स्वास्थ्य संस्थानों में हुए, जो राष्ट्रीय 88.6% से कम है।\n\nएम्स पटना, इंदिरा गांधी आयुर्विज्ञान संस्थान और पटना मेडिकल कॉलेज मुख्य रेफ़रल अस्पताल हैं, और एम्स दरभंगा बन रहा है।",
        "बिहारचा अर्भक मृत्युदर 2010 मध्ये दर 1,000 जिवंत जन्मांमागे 48 वरून 2020 मध्ये 27 वर आला — राष्ट्रीय 28 पेक्षा किंचित कमी — पण त्याचा जन्मदर — 2020 मध्ये दर 1,000 मागे 25.5 — कोणत्याही राज्यात सर्वाधिक होता. 2014-18 मध्ये जन्मतः आयुर्मान 69.1 वर्षे होते, आणि असामान्यपणे पुरुष (69.4) स्त्रियांपेक्षा (68.7) किंचित जास्त जगत होते. बालकुपोषण भारतातील सर्वाधिक गंभीर स्थितींपैकी आहे: एनएफएचएस-5 मध्ये पाच वर्षांखालील 42.9% मुले खुजी, 22.9% कृश व 41.0% कमी वजनाची होती, तरीही खुजेपणा एनएफएचएस-4 मधील 48.3% वरून घटला. सुमारे 76.2% प्रसूती आरोग्य संस्थांत झाल्या, राष्ट्रीय 88.6% पेक्षा कमी.\n\nएम्स पाटणा, इंदिरा गांधी आयुर्विज्ञान संस्था व पाटणा वैद्यकीय महाविद्यालय ही मुख्य संदर्भ रुग्णालये आहेत, आणि एम्स दरभंगा उभारले जात आहे."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(27, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(48, "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(25.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020 (death rate 5.4); 28.1 in 2010."), "number",
             previous=dp(28.1, "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(69.1, "years", "2014-18", "survey", "srs", ESI_LE, note="SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male 69.4, female 68.7)."), "number", "higher-is-better",
             national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("BR"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin; the PIB summary used here lists only States that met the SDG target."),
        (L("Under-five mortality rate (SRS 2021)", "पाँच वर्ष से कम आयु की मृत्यु दर (एसआरएस 2021)", "पाच वर्षांखालील मृत्युदर (एसआरएस 2021)"), "srs", "SRS Statistical Report 2021."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("br mod2 ok")
