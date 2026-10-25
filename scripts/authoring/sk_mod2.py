"""Sikkim modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-SK"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_SK = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 25 Oct 2026. "
           "FY2024-25 is the latest year published for Sikkim and may be revised.")
mo = research("mospi_sk.json")
C = research("census_b5plus.json")
NAME = L("Sikkim", "सिक्किम", "सिक्कीम")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Sikkim's culture blends the Buddhist traditions of the Lepcha and Bhutia with the Hindu and Kirat traditions of its Nepali communities. Monasteries hold masked cham dances at festivals, and thangka painting, wood carving and the making of choktse (carved folding tables) are traditional crafts. The Lepcha honour Mount Kangchenjunga and nature spirits, and Pang Lhabsol, a festival unique to Sikkim, worships Kangchenjunga as the guardian deity. Nepali folk songs and dances such as the maruni and tamang selo, and Lepcha and Bhutia songs, are performed at festivals across the State.",
        "सिक्किम की संस्कृति लेप्चा और भूटिया की बौद्ध परंपराओं को उसके नेपाली समुदायों की हिंदू और किरात परंपराओं से जोड़ती है। मठों में त्योहारों पर मुखौटे वाले छम नृत्य होते हैं, और थांका चित्रकला, लकड़ी की नक्काशी और छोक्त्से (नक्काशीदार मोड़ने वाली मेज़ें) बनाना पारंपरिक शिल्प हैं। लेप्चा कंचनजंगा पर्वत और प्रकृति की आत्माओं का सम्मान करते हैं, और सिक्किम का अनूठा त्योहार पांग ल्हाबसोल कंचनजंगा को संरक्षक देवता के रूप में पूजता है। नेपाली लोकगीत और मारुनी व तमांग सेलो जैसे नृत्य, और लेप्चा व भूटिया गीत पूरे राज्य में त्योहारों पर प्रस्तुत होते हैं।",
        "सिक्कीमची संस्कृती लेप्चा व भुतियांच्या बौद्ध परंपरांना तेथील नेपाळी समुदायांच्या हिंदू व किरात परंपरांशी जोडते. मठांत सणांना मुखवटे घातलेली छम नृत्ये होतात, आणि थांका चित्रकला, लाकडी कोरीवकाम व छोक्त्से (कोरीव घडीची टेबले) बनवणे या पारंपरिक कला आहेत. लेप्चा कांचनजंगा पर्वत व निसर्गदेवतांचा आदर करतात, आणि सिक्कीमचा वैशिष्ट्यपूर्ण सण पांग ल्हाबसोल कांचनजंगाची रक्षणकर्ती देवता म्हणून पूजा करतो. नेपाळी लोकगीते व मारुनी आणि तमांग सेलोसारखी नृत्ये, तसेच लेप्चा व भुतिया गीते संपूर्ण राज्यात सणांना सादर होतात."),
        conf="Editorial"),
    lst("festivals", [
        fest("losar", "Losar", "लोसार", "लोसार", ("February–March", "फ़रवरी–मार्च", "फेब्रुवारी–मार्च"),
             ("Tibetan New Year, with cham dances at monasteries.", "तिब्बती नव वर्ष, मठों में छम नृत्यों के साथ।", "तिबेटी नववर्ष, मठांत छम नृत्यांसह.")),
        fest("sagadawa", "Saga Dawa", "सागा दावा", "सागा दावा", ("May–June", "मई–जून", "मे–जून"),
             ("Celebrates the Buddha's birth, enlightenment and parinirvana.", "बुद्ध के जन्म, ज्ञान और परिनिर्वाण का उत्सव।", "बुद्धाचा जन्म, ज्ञानप्राप्ती व परिनिर्वाणाचा उत्सव.")),
        fest("panglhabsol", "Pang Lhabsol", "पांग ल्हाबसोल", "पांग ल्हाबसोल", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Worship of Kangchenjunga as Sikkim's guardian deity.", "कंचनजंगा की सिक्किम के संरक्षक देवता के रूप में पूजा।", "कांचनजंगाची सिक्कीमची रक्षणकर्ती देवता म्हणून पूजा.")),
        fest("dasain", "Dasain and Tihar", "दसैं और तिहार", "दसैं व तिहार", ("October–November", "अक्टूबर–नवंबर", "ऑक्टोबर–नोव्हेंबर"),
             ("The main festivals of Sikkim's Nepali Hindus.", "सिक्किम के नेपाली हिंदुओं के मुख्य त्योहार।", "सिक्कीममधील नेपाळी हिंदूंचे मुख्य सण.")),
        fest("bumchu", "Bumchu", "बुमछू", "बुमछू", ("February–March", "फ़रवरी–मार्च", "फेब्रुवारी–मार्च"),
             ("Opening of the sacred water vase at Tashiding.", "ताशिदिंग में पवित्र जल कलश का उद्घाटन।", "ताशिदिंग येथे पवित्र जलकलश उघडणे.")),
        fest("tendong", "Tendong Lho Rum Faat", "तेंदोंग ल्हो रम फात", "तेंदोंग ल्हो रम फात", ("August", "अगस्त", "ऑगस्ट"),
             ("Lepcha festival honouring Mount Tendong.", "तेंदोंग पर्वत के सम्मान में लेप्चा त्योहार।", "तेंदोंग पर्वताच्या सन्मानार्थ लेप्चा सण.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("cham", "Cham masked dances", "छम मुखौटा नृत्य", "छम मुखवटा नृत्य"), it3("thangka", "Thangka painting", "थांका चित्रकला", "थांका चित्रकला"),
        it3("choktse", "Choktse tables", "छोक्त्से मेज़ें", "छोक्त्से टेबले"), it3("maruni", "Maruni dance", "मारुनी नृत्य", "मारुनी नृत्य"),
        it3("carpet", "Hand-woven carpets", "हाथ से बुने क़ालीन", "हाताने विणलेले गालिचे"), it3("pumtong", "Lepcha flute (pumtong pulit)", "लेप्चा बाँसुरी (पुमतोंग पुलित)", "लेप्चा बासरी (पुमतोंग पुलित)"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("momo", "Momos and thukpa", "मोमो और थुकपा", "मोमो व थुकपा", d=("Dumplings and noodle soup, eaten everywhere.", "पकौड़ी जैसे मोमो और नूडल सूप, हर जगह खाए जाते हैं।", "मोमो व नूडल सूप, सर्वत्र खाल्ले जातात.")),
        it3("gundruk", "Gundruk and sinki", "गुंद्रुक और सिंकी", "गुंद्रुक व सिंकी", d=("Fermented leafy greens and radish, made into soups and pickles.", "किण्वित पत्तेदार साग और मूली, जिनसे सूप और अचार बनते हैं।", "आंबवलेल्या पालेभाज्या व मुळा, ज्यांची सूप व लोणची बनतात.")),
        it3("kinema", "Kinema", "किनेमा", "किनेमा", d=("Fermented soya bean dish of the Nepali communities.", "नेपाली समुदायों का किण्वित सोयाबीन व्यंजन।", "नेपाळी समुदायांचा आंबवलेल्या सोयाबीनचा पदार्थ.")),
        it3("churpi", "Churpi", "छुरपी", "छुरपी", d=("Hard cheese of yak or cow milk.", "याक या गाय के दूध का सख़्त पनीर।", "याक किंवा गायीच्या दुधाचे कडक चीज.")),
        it3("selroti", "Sel roti", "सेल रोटी", "सेल रोटी", d=("Ring-shaped rice bread made at festivals.", "त्योहारों पर बनने वाली चावल की गोल रोटी।", "सणांना केली जाणारी तांदळाची गोल भाकरी.")),
        it3("khursani", "Dalle khursani", "डल्ले खुर्सानी", "डल्ले खुर्सानी", d=("Fiery round chilli; a registered GI shared with West Bengal.", "तीखी गोल मिर्च; पश्चिम बंगाल के साथ साझा पंजीकृत जीआई।", "तिखट गोल मिरची; पश्चिम बंगालसोबत सामायिक नोंदणीकृत जीआय.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("bakhu", "Bakhu", "बखू", "बखू", d=("Loose robe worn by Bhutia men and women.", "भूटिया पुरुषों और महिलाओं द्वारा पहना जाने वाला ढीला चोगा।", "भुतिया पुरुष व स्त्रिया घालतात तो सैल झगा.")),
        it3("dumvum", "Dumvum and dumdyam", "दुमवुम और दुमद्याम", "दुमवुम व दुमद्याम", d=("Traditional Lepcha dress for women and men.", "लेप्चा महिलाओं और पुरुषों की पारंपरिक पोशाक।", "लेप्चा स्त्री-पुरुषांचा पारंपरिक पोशाख.")),
        it3("daura", "Daura-suruwal and chaubandi cholo", "दौरा-सुरुवाल और चौबंदी चोलो", "दौरा-सुरुवाल व चौबंदी चोलो", d=("Traditional Nepali dress for men and women.", "नेपाली पुरुषों और महिलाओं की पारंपरिक पोशाक।", "नेपाळी स्त्री-पुरुषांचा पारंपरिक पोशाख.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; util = 100 * g["utilities"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["SK"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["SK"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Sikkim's GSDP at current prices was about ₹{inr(cur['FY2024-25'][0])} crore in FY2024-25, the latest year published for the State in the MoSPI series, and its per capita NSDP of ₹{inr(pc['FY2024-25'][0])} was the highest of any State or UT with a figure for that year. Its economy is unusual for a hill State: manufacturing made up about {mfg:.0f}% of GSVA, mostly pharmaceutical plants set up in the south since the 2000s, and electricity, gas and water about {util:.0f}%, reflecting the hydropower stations on the Teesta. Agriculture, livestock and forestry contributed about {agri:.0f}%; farming is fully organic, and large cardamom, ginger, turmeric, mandarin oranges and flowers such as cymbidium orchids are the main cash crops. Tourism and government services employ many people.\n\nUnemployment is low: the PLFS rate was {ur['2025']}% in 2025, against {ui['2025']}% nationally, and {lf['female']}% of women aged 15 and above were in the labour force, well above the national {lfi['female']}%.",
        f"मोस्पी शृंखला में राज्य के लिए प्रकाशित नवीनतम वर्ष, वित्त वर्ष 2024-25 में सिक्किम का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{inr(cur['FY2024-25'][0])} करोड़ था, और ₹{inr(pc['FY2024-25'][0])} का प्रति व्यक्ति एनएसडीपी उस वर्ष के आँकड़े वाले किसी भी राज्य या केंद्र शासित प्रदेश में सबसे अधिक था। पहाड़ी राज्य के लिए इसकी अर्थव्यवस्था असामान्य है: जीएसवीए में विनिर्माण का हिस्सा लगभग {mfg:.0f}% था, अधिकतर 2000 के दशक से दक्षिण में स्थापित दवा संयंत्र, और बिजली, गैस व जल का लगभग {util:.0f}%, जो तीस्ता पर बने जलविद्युत केंद्रों को दर्शाता है। कृषि, पशुपालन और वानिकी का योगदान लगभग {agri:.0f}% था; खेती पूरी तरह जैविक है, और बड़ी इलायची, अदरक, हल्दी, संतरे और सिंबिडियम ऑर्किड जैसे फूल मुख्य नक़दी फ़सलें हैं। पर्यटन और सरकारी सेवाएँ बहुत लोगों को रोज़गार देती हैं।\n\nबेरोज़गारी कम है: पीएलएफ़एस दर 2025 में {ur['2025']}% थी, जबकि राष्ट्रीय स्तर पर {ui['2025']}%, और 15 वर्ष से अधिक आयु की {lf['female']}% महिलाएँ श्रम बल में थीं, जो राष्ट्रीय {lfi['female']}% से बहुत अधिक है।",
        f"मोस्पी मालिकेत राज्यासाठी प्रकाशित नवीनतम वर्ष, आ.व. 2024-25 मध्ये सिक्कीमचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{inr(cur['FY2024-25'][0])} कोटी होते, आणि ₹{inr(pc['FY2024-25'][0])} चे दरडोई एनएसडीपी त्या वर्षीचा आकडा असलेल्या कोणत्याही राज्य वा केंद्रशासित प्रदेशात सर्वाधिक होते. डोंगरी राज्यासाठी त्याची अर्थव्यवस्था वेगळी आहे: जीएसव्हीएमध्ये उत्पादन उद्योगाचा वाटा सुमारे {mfg:.0f}% होता, बहुतांश 2000 च्या दशकापासून दक्षिणेत उभारलेले औषधनिर्मिती कारखाने, आणि वीज, वायू व पाण्याचा सुमारे {util:.0f}%, जो तिस्तेवरील जलविद्युत केंद्रांमुळे आहे. शेती, पशुपालन व वनीकरणाचा वाटा सुमारे {agri:.0f}% होता; शेती पूर्णतः सेंद्रिय आहे, आणि मोठी वेलची, आले, हळद, संत्री आणि सिंबिडियम ऑर्किडसारखी फुले ही मुख्य नगदी पिके आहेत. पर्यटन व सरकारी सेवा अनेकांना रोजगार देतात.\n\nबेरोजगारी कमी आहे: पीएलएफएस दर 2025 मध्ये {ur['2025']}% होता, तर राष्ट्रीय पातळीवर {ui['2025']}%, आणि 15 वर्षांवरील {lf['female']}% स्त्रिया श्रमशक्तीत होत्या, राष्ट्रीय {lfi['female']}% पेक्षा खूप जास्त."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_SK), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_SK), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_SK), "rupee", "higher-is-better",
             previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("SK", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    plfs_series("SK", NAME),
    lst("sectors-key", [
        it3("pharma", "Pharmaceuticals", "दवा उद्योग", "औषधनिर्मिती", d=("Formulation plants in the south and east of the State.", "राज्य के दक्षिण और पूर्व में दवा निर्माण संयंत्र।", "राज्याच्या दक्षिण व पूर्व भागात औषधनिर्मिती कारखाने.")),
        it3("hydro", "Hydropower", "जलविद्युत", "जलविद्युत", d=("Run-of-river stations on the Teesta and Rangeet.", "तीस्ता और रंगीत पर नदी-प्रवाह जलविद्युत केंद्र।", "तिस्ता व रंगीतवर प्रवाही जलविद्युत केंद्रे.")),
        it3("cardamom", "Large cardamom", "बड़ी इलायची", "मोठी वेलची", d=("Grown under forest shade; a registered GI.", "वन की छाया में उगाई जाती है; पंजीकृत जीआई।", "जंगलाच्या सावलीत घेतली जाते; नोंदणीकृत जीआय.")),
        it3("organic", "Organic farming", "जैविक खेती", "सेंद्रिय शेती", d=("Ginger, turmeric, buckwheat, mandarins and vegetables.", "अदरक, हल्दी, कुट्टू, संतरे और सब्ज़ियाँ।", "आले, हळद, कुट्टू, संत्री व भाज्या.")),
        it3("tourism", "Tourism", "पर्यटन", "पर्यटन", d=("Monasteries, lakes, treks and mountain views.", "मठ, झीलें, ट्रेक और पर्वतीय दृश्य।", "मठ, सरोवरे, ट्रेक व पर्वतदर्शन.")),
        it3("flori", "Floriculture", "पुष्प उत्पादन", "पुष्पशेती", d=("Orchids and cut flowers.", "ऑर्किड और कटे फूल।", "ऑर्किड व कापलेली फुले.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Large cardamom production by year", "वर्षवार बड़ी इलायची उत्पादन", "वर्षनिहाय मोठ्या वेलचीचे उत्पादन"), "india-gov", "Spices Board India."),
        (L("Tourist arrivals by year", "वर्षवार पर्यटक आगमन", "वर्षनिहाय पर्यटक आगमन"), "tourism", "Sikkim Tourism and Civil Aviation Department."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Sikkim has a unicameral legislature, the 32-member Legislative Assembly in Gangtok. Seats are reserved for the Bhutia-Lepcha communities, and one seat, the Sangha seat, is elected only by registered monks and nuns of the State's monasteries. Sikkim elects 1 member to the Lok Sabha and 1 to the Rajya Sabha. Article 371F of the Constitution, added when Sikkim joined India, protects its existing laws and the special features of its legislature.\n\nThe Sikkim Krantikari Morcha won the Assembly election of 2024, and Prem Singh Tamang (Golay), Chief Minister since 2019, was sworn in for a second term on 10 June 2024. Mingma Norbu Sherpa was elected Speaker on 12 June 2024, and Dushyant Kumar Gautam has been Governor since 19 October 2026. The next Assembly election is due by 2029.",
        "सिक्किम में एकसदनीय विधानमंडल है, गंगटोक में 32 सदस्यों वाली विधानसभा। भूटिया-लेप्चा समुदायों के लिए सीटें आरक्षित हैं, और एक सीट, संघ सीट, केवल राज्य के मठों के पंजीकृत भिक्षुओं और भिक्षुणियों द्वारा चुनी जाती है। सिक्किम से लोकसभा का 1 और राज्यसभा का 1 सदस्य चुना जाता है। सिक्किम के भारत में शामिल होने पर संविधान में जोड़ा गया अनुच्छेद 371च इसके मौजूदा क़ानूनों और इसकी विधानसभा की विशेषताओं की रक्षा करता है।\n\n2024 का विधानसभा चुनाव सिक्किम क्रांतिकारी मोर्चा ने जीता, और 2019 से मुख्यमंत्री प्रेम सिंह तमांग (गोले) ने 10 जून 2024 को दूसरे कार्यकाल की शपथ ली। मिंगमा नोर्बु शेर्पा 12 जून 2024 को अध्यक्ष चुने गए, और दुष्यंत कुमार गौतम 19 अक्टूबर 2026 से राज्यपाल हैं। अगला विधानसभा चुनाव 2029 तक होना है।",
        "सिक्कीममध्ये एकसदनी विधिमंडळ आहे, गंगटोकमधील 32 सदस्यांची विधानसभा. भुतिया-लेप्चा समुदायांसाठी जागा राखीव आहेत, आणि एक जागा, संघ जागा, केवळ राज्यातील मठांतील नोंदणीकृत भिक्षू व भिक्षुणी निवडतात. सिक्कीममधून लोकसभेवर 1 व राज्यसभेवर 1 सदस्य निवडला जातो. सिक्कीम भारतात सामील झाले तेव्हा संविधानात जोडलेला अनुच्छेद 371च त्याचे विद्यमान कायदे व विधानसभेची वैशिष्ट्ये जपतो.\n\n2024 ची विधानसभा निवडणूक सिक्कीम क्रांतिकारी मोर्चाने जिंकली, आणि 2019 पासून मुख्यमंत्री असलेल्या प्रेम सिंह तमांग (गोले) यांनी 10 जून 2024 रोजी दुसऱ्या कारकिर्दीची शपथ घेतली. मिंगमा नोर्बु शेर्पा 12 जून 2024 रोजी अध्यक्षपदी निवडले गेले, आणि दुष्यंत कुमार गौतम 19 ऑक्टोबर 2026 पासून राज्यपाल आहेत. पुढील विधानसभा निवडणूक 2029 पर्यंत होणे अपेक्षित आहे."),
        sources=["scroll", "sk-gov", "eastmojo"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("portal", "Government of Sikkim", "सिक्किम सरकार", "सिक्कीम शासन", url="https://sikkim.gov.in", src="sk-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2024 Assembly election — party-wise result", "2024 विधानसभा चुनाव — दलवार परिणाम", "2024 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Sikkim 2024."),
        (L("Governor's swearing-in — official source", "राज्यपाल का शपथ ग्रहण — आधिकारिक स्रोत", "राज्यपालांचा शपथविधी — अधिकृत स्रोत"), "india-gov", "Replace the news report with the Lok Bhavan Sikkim release."),
        (L("Chief Minister's swearing-in — official source", "मुख्यमंत्री का शपथ ग्रहण — आधिकारिक स्रोत", "मुख्यमंत्र्यांचा शपथविधी — अधिकृत स्रोत"), "sk-gov", "Replace the news report with the Government of Sikkim notification."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Sikkim's first airport, at Pakyong, opened in 2018, and its first railway, from Sivok in West Bengal to Rangpo, is under construction, with a later extension to Gangtok planned. Other works include the rebuilding of roads and bridges damaged by the Teesta flood of October 2023 and the widening of NH-10; these will be added as cards once their status is confirmed from official sources. Each card shows its source and the date it was checked.",
        "पाक्योंग में सिक्किम का पहला हवाई अड्डा 2018 में खुला, और इसकी पहली रेल लाइन, पश्चिम बंगाल के सेवक से रंगपो तक, निर्माणाधीन है, जिसे बाद में गंगटोक तक बढ़ाने की योजना है। अन्य कार्यों में अक्टूबर 2023 की तीस्ता बाढ़ में क्षतिग्रस्त सड़कों और पुलों का पुनर्निर्माण और एनएच-10 का चौड़ीकरण शामिल हैं; आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर इन्हें कार्ड के रूप में जोड़ा जाएगा। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "पाकयोंग येथील सिक्कीमचा पहिला विमानतळ 2018 मध्ये सुरू झाला, आणि त्याचा पहिला रेल्वेमार्ग, पश्चिम बंगालमधील सेवक ते रंगपो, बांधकामाधीन आहे, ज्याचा पुढे गंगटोकपर्यंत विस्तार नियोजित आहे. इतर कामांत ऑक्टोबर 2023 च्या तिस्ता पुरात नुकसान झालेल्या रस्ते व पुलांची पुनर्बांधणी आणि एनएच-10 चे रुंदीकरण यांचा समावेश आहे; अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर त्यांची कार्डे जोडली जातील. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pmindia", "morung-express"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Sivok–Rangpo line — sanctioned cost and official progress", "सेवक–रंगपो लाइन — स्वीकृत लागत और आधिकारिक प्रगति", "सेवक–रंगपो मार्ग — मंजूर खर्च व अधिकृत प्रगती"), "railways", "Ministry of Railways / Parliament answer; replace the news report."),
        (L("Pakyong Airport — project cost and flight operations", "पाक्योंग हवाई अड्डा — परियोजना लागत और उड़ान संचालन", "पाकयोंग विमानतळ — प्रकल्प खर्च व उड्डाण संचालन"), "aai", "Airports Authority of India."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "National Highway 10, from Sevoke near Siliguri up the Teesta valley to Gangtok, is Sikkim's lifeline, and it is often cut by landslides in the monsoon. Mountain roads run north to Mangan, Lachen and Lachung and east to Tsomgo and Nathu La, and shared jeeps are the main public transport. Pakyong Airport serves Gangtok, but most visitors fly into Bagdogra in West Bengal; the nearest railway stations are New Jalpaiguri and Siliguri until the Sivok–Rangpo line opens. Gangtok has a short passenger ropeway. Indian visitors need permits for Nathu La, Tsomgo and North Sikkim, and foreign visitors need a Restricted Area Permit to enter the State.",
        "सिलीगुड़ी के पास सेवक से तीस्ता घाटी होते हुए गंगटोक तक राष्ट्रीय राजमार्ग 10 सिक्किम की जीवनरेखा है, और मानसून में अक्सर भूस्खलन से कट जाता है। पहाड़ी सड़कें उत्तर में मंगन, लाचेन और लाचुंग और पूर्व में छांगू और नाथु ला तक जाती हैं, और साझा जीपें मुख्य सार्वजनिक परिवहन हैं। पाक्योंग हवाई अड्डा गंगटोक की सेवा करता है, पर अधिकांश यात्री पश्चिम बंगाल के बागडोगरा उतरते हैं; सेवक–रंगपो लाइन खुलने तक निकटतम रेलवे स्टेशन न्यू जलपाईगुड़ी और सिलीगुड़ी हैं। गंगटोक में एक छोटा यात्री रोपवे है। भारतीय पर्यटकों को नाथु ला, छांगू और उत्तर सिक्किम के लिए परमिट चाहिए, और विदेशी पर्यटकों को राज्य में प्रवेश के लिए प्रतिबंधित क्षेत्र परमिट चाहिए।",
        "सिलिगुडीजवळील सेवकपासून तिस्ता खोऱ्यातून गंगटोकपर्यंत जाणारा राष्ट्रीय महामार्ग 10 ही सिक्कीमची जीवनवाहिनी आहे, आणि पावसाळ्यात तो अनेकदा भूस्खलनाने तुटतो. डोंगरी रस्ते उत्तरेला मंगन, लाचेन व लाचुंग आणि पूर्वेला छांगू व नथु लापर्यंत जातात, आणि सामायिक जीप ही मुख्य सार्वजनिक वाहतूक आहे. पाकयोंग विमानतळ गंगटोकला सेवा देतो, पण बहुतेक पर्यटक पश्चिम बंगालमधील बागडोगरा येथे उतरतात; सेवक–रंगपो मार्ग सुरू होईपर्यंत जवळची रेल्वे स्थानके न्यू जलपाईगुडी व सिलिगुडी आहेत. गंगटोकमध्ये लहान प्रवासी रोपवे आहे. भारतीय पर्यटकांना नथु ला, छांगू व उत्तर सिक्कीमसाठी परवाने लागतात, आणि परदेशी पर्यटकांना राज्यात प्रवेशासाठी प्रतिबंधित क्षेत्र परवाना लागतो."),
        conf="Editorial"),
    lst("airports", [
        it3("pyg", "Pakyong Airport", "पाक्योंग हवाई अड्डा", "पाकयोंग विमानतळ", m=("PYG", "PYG", "PYG")),
        it3("ixb", "Bagdogra (West Bengal)", "बागडोगरा (पश्चिम बंगाल)", "बागडोगरा (पश्चिम बंगाल)", m=("IXB, nearest major airport", "IXB, निकटतम बड़ा हवाई अड्डा", "IXB, जवळचा मोठा विमानतळ")),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("Permit rules for visitors — official notice", "पर्यटकों के लिए परमिट नियम — आधिकारिक सूचना", "पर्यटकांसाठी परवाना नियम — अधिकृत सूचना"), "india-gov", "Sikkim Tourism / Ministry of Home Affairs."),
        (L("Road length and NH-10 closures", "सड़क लंबाई और एनएच-10 बंद होने की घटनाएँ", "रस्त्यांची लांबी व एनएच-10 बंद होण्याच्या घटना"), "morth", "MoRTH / NHIDCL."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Sikkim's steep rivers make it a hydropower State. Run-of-river stations on the Teesta and Rangeet, built by NHPC, the State government and private developers, feed the eastern regional grid as well as the State. The glacial lake outburst flood of 4 October 2023 swept away the dam of the Teesta III project at Chungthang and damaged other stations downstream, raising questions about hydropower in a fragile, earthquake-prone valley.",
        "सिक्किम की तेज़ ढलान वाली नदियाँ इसे जलविद्युत राज्य बनाती हैं। एनएचपीसी, राज्य सरकार और निजी विकासकर्ताओं द्वारा तीस्ता और रंगीत पर बनाए गए नदी-प्रवाह केंद्र राज्य के साथ-साथ पूर्वी क्षेत्रीय ग्रिड को भी बिजली देते हैं। 4 अक्टूबर 2023 की हिमनद झील फटने से आई बाढ़ ने चुंगथांग में तीस्ता III परियोजना का बाँध बहा दिया और नीचे के अन्य केंद्रों को क्षति पहुँचाई, जिससे नाज़ुक, भूकंप-प्रवण घाटी में जलविद्युत पर प्रश्न उठे।",
        "सिक्कीमच्या तीव्र उताराच्या नद्या त्याला जलविद्युत राज्य बनवतात. एनएचपीसी, राज्य सरकार व खासगी विकासकांनी तिस्ता व रंगीतवर बांधलेली प्रवाही केंद्रे राज्याबरोबरच पूर्व प्रादेशिक ग्रिडलाही वीज पुरवतात. 4 ऑक्टोबर 2023 रोजी हिमनदी सरोवर फुटून आलेल्या पुराने चुंगथांग येथील तिस्ता III प्रकल्पाचे धरण वाहून गेले आणि खालच्या इतर केंद्रांचे नुकसान झाले, ज्यामुळे नाजूक, भूकंपप्रवण खोऱ्यातील जलविद्युतबद्दल प्रश्न उपस्थित झाले."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed hydropower capacity by station", "केंद्रवार स्थापित जलविद्युत क्षमता", "केंद्रनिहाय स्थापित जलविद्युत क्षमता"), "cea", "CEA installed capacity report."),
        (L("Teesta III restoration — official status", "तीस्ता III की बहाली — आधिकारिक स्थिति", "तिस्ता III ची पुनर्बांधणी — अधिकृत स्थिती"), "india-gov", "Ministry of Power / Sikkim Urja Ltd."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Mobile coverage reaches most towns and villages, though signal is patchy in the high north and roads and cables are often cut by landslides. Government services are offered online through the State portal, and Sikkim University, NIT Sikkim and Sikkim Manipal University train students in computing and engineering.",
        "मोबाइल कवरेज अधिकांश नगरों और गाँवों तक पहुँचता है, हालाँकि ऊँचे उत्तर में सिग्नल कमज़ोर है और भूस्खलन से अक्सर सड़कें और केबल कट जाते हैं। सरकारी सेवाएँ राज्य पोर्टल से ऑनलाइन दी जाती हैं, और सिक्किम विश्वविद्यालय, एनआईटी सिक्किम और सिक्किम मणिपाल विश्वविद्यालय कंप्यूटिंग और इंजीनियरिंग में छात्रों को प्रशिक्षित करते हैं।",
        "मोबाइल सेवा बहुतेक शहरे व गावांपर्यंत पोहोचते, मात्र उंच उत्तरेत संकेत कमकुवत आहे आणि भूस्खलनामुळे रस्ते व केबल अनेकदा तुटतात. सरकारी सेवा राज्य संकेतस्थळावरून ऑनलाइन दिल्या जातात, आणि सिक्कीम विद्यापीठ, एनआयटी सिक्कीम व सिक्कीम मणिपाल विद्यापीठ संगणन व अभियांत्रिकीचे शिक्षण देतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (North East circle / Sikkim)."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("SK", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["SK"]
ger = AP["aishe_ger"]["SK"]; nu = AP["aishe_universities_2021_22"]["SK"]; nc = AP["aishe_colleges_2021_22"]["SK"]
module(R, "education", [
    prose("p1", L(
        f"Literacy in Sikkim was 81.4% at the 2011 Census. The higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE, above the national 28.4%, and women's GER ({gf}%) was higher than men's ({gm}%). The small State had {nu} universities and {inr(nc)} colleges.\n\nSikkim University, a central university founded in 2007, is in Gangtok; Sikkim Manipal University (1995) runs medical, engineering and management institutes; and NIT Sikkim is at Ravangla. Monastic schools teach Buddhist philosophy, and Nepali, Bhutia, Lepcha and other official languages are taught in State schools.",
        f"2011 की जनगणना में सिक्किम की साक्षरता 81.4% थी। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था, जो राष्ट्रीय 28.4% से अधिक है, और महिलाओं का जीईआर ({gf}%) पुरुषों ({gm}%) से अधिक था। इस छोटे राज्य में {nu} विश्वविद्यालय और {inr(nc)} कॉलेज थे।\n\n2007 में स्थापित केंद्रीय विश्वविद्यालय, सिक्किम विश्वविद्यालय गंगटोक में है; सिक्किम मणिपाल विश्वविद्यालय (1995) चिकित्सा, इंजीनियरिंग और प्रबंधन संस्थान चलाता है; और एनआईटी सिक्किम रावंगला में है। मठ विद्यालय बौद्ध दर्शन पढ़ाते हैं, और राज्य के स्कूलों में नेपाली, भूटिया, लेप्चा और अन्य राजभाषाएँ पढ़ाई जाती हैं।",
        f"2011 च्या जनगणनेत सिक्कीमची साक्षरता 81.4% होती. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा अधिक, आणि स्त्रियांचे जीईआर ({gf}%) पुरुषांपेक्षा ({gm}%) जास्त होते. या लहान राज्यात {nu} विद्यापीठे व {inr(nc)} महाविद्यालये होती.\n\n2007 मध्ये स्थापन झालेले केंद्रीय विद्यापीठ, सिक्कीम विद्यापीठ गंगटोकमध्ये आहे; सिक्कीम मणिपाल विद्यापीठ (1995) वैद्यकीय, अभियांत्रिकी व व्यवस्थापन संस्था चालवते; आणि एनआयटी सिक्कीम रावंगला येथे आहे. मठांतील शाळा बौद्ध तत्त्वज्ञान शिकवतात, आणि राज्याच्या शाळांत नेपाळी, भुतिया, लेप्चा व इतर राजभाषा शिकवल्या जातात."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("su", "Sikkim University", "सिक्किम विश्वविद्यालय", "सिक्कीम विद्यापीठ", m=("Central university, Gangtok, 2007", "केंद्रीय विश्वविद्यालय, गंगटोक, 2007", "केंद्रीय विद्यापीठ, गंगटोक, 2007")),
        it3("smu", "Sikkim Manipal University", "सिक्किम मणिपाल विश्वविद्यालय", "सिक्कीम मणिपाल विद्यापीठ", m=("Gangtok, 1995", "गंगटोक, 1995", "गंगटोक, 1995")),
        it3("nits", "NIT Sikkim", "एनआईटी सिक्किम", "एनआयटी सिक्कीम", m=("Ravangla", "रावंगला", "रावंगला")),
        it3("namgyal", "Namgyal Institute of Tibetology", "नामग्याल तिब्बत विज्ञान संस्थान", "नामग्याल तिबेटविद्या संस्था", m=("Gangtok", "गंगटोक", "गंगटोक")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["SK"]; s = C["srs"]["SK"]
module(R, "health", [
    prose("p1", L(
        f"Sikkim's infant mortality rate was {s[5]:.0f} per 1,000 live births in 2020 in the Sample Registration System, down from {s[4]} in 2010 and among the lowest in India (national 28). The birth rate was {s[1]} and the death rate {s[3]} per 1,000. In NFHS-5, {n['institutional_N5']:.1f}% of births took place in health facilities; {n['stunted'][1]:.1f}% of children under five were stunted, down from {n['stunted'][0]}% in NFHS-4, {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight.\n\nThe STNM multi-speciality hospital at Sochakgang in Gangtok is the main government referral hospital, with district hospitals in each district, and the Central Referral Hospital at Tadong is attached to Sikkim Manipal University. Remote villages in the north depend on primary health centres and on roads that can be blocked for days.",
        f"नमूना पंजीकरण प्रणाली में 2020 में सिक्किम की शिशु मृत्यु दर प्रति 1,000 जीवित जन्म पर {s[5]:.0f} थी, जो 2010 के {s[4]} से कम और भारत में सबसे कम में है (राष्ट्रीय 28)। जन्म दर प्रति 1,000 पर {s[1]} और मृत्यु दर {s[3]} थी। एनएफ़एचएस-5 में {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए; पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने थे, जो एनएफ़एचएस-4 के {n['stunted'][0]}% से कम है, {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के।\n\nगंगटोक में सोचाकगांग का एसटीएनएम बहु-विशेषज्ञता अस्पताल मुख्य सरकारी रेफ़रल अस्पताल है, हर ज़िले में ज़िला अस्पताल हैं, और ताडोंग का सेंट्रल रेफ़रल अस्पताल सिक्किम मणिपाल विश्वविद्यालय से जुड़ा है। उत्तर के दूरस्थ गाँव प्राथमिक स्वास्थ्य केंद्रों और उन सड़कों पर निर्भर हैं जो कई दिनों तक बंद रह सकती हैं।",
        f"नमुना नोंदणी पद्धतीनुसार 2020 मध्ये सिक्कीमचा अर्भक मृत्युदर दर 1,000 जिवंत जन्मांमागे {s[5]:.0f} होता, 2010 मधील {s[4]} वरून कमी आणि भारतातील सर्वांत कमींपैकी (राष्ट्रीय 28). जन्मदर दर 1,000 मागे {s[1]} व मृत्युदर {s[3]} होता. एनएफएचएस-5 मध्ये {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या; पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी होती, एनएफएचएस-4 मधील {n['stunted'][0]}% वरून कमी, {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची.\n\nगंगटोकमधील सोचाकगांगचे एसटीएनएम बहुविशेष रुग्णालय हे मुख्य सरकारी संदर्भ रुग्णालय आहे, प्रत्येक जिल्ह्यात जिल्हा रुग्णालय आहे, आणि ताडोंगचे सेंट्रल रेफरल रुग्णालय सिक्कीम मणिपाल विद्यापीठाशी संलग्न आहे. उत्तरेकडील दुर्गम गावे प्राथमिक आरोग्य केंद्रांवर व अनेक दिवस बंद राहू शकणाऱ्या रस्त्यांवर अवलंबून आहेत."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2. Small States have larger sampling errors."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("SK"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"), "srs", "Sikkim is not in the SRS abridged life table for major States used here."),
        (L("Hospital beds and doctors per lakh population", "प्रति लाख जनसंख्या अस्पताल बिस्तर और डॉक्टर", "दर लाख लोकसंख्येमागे रुग्णालय खाटा व डॉक्टर"), "mohfw", "Rural Health Statistics / National Health Profile."),
    ]),
])
print("sk mod2 ok")
