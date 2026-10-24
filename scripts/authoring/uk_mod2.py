"""Uttarakhand modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-UK"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_UK = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 24 Oct 2026. "
           "FY2025-26 is the latest year published for Uttarakhand and may be revised.")
mo = research("mospi_uk.json")
C = research("census_b5plus.json")
NAME = L("Uttarakhand", "उत्तराखंड", "उत्तराखंड")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Garhwali and Kumaoni folk culture is rich in song, dance and ritual. Jagar ceremonies invoke local deities through the songs of the jagariya and the beat of the dhol and damau; Ramman, the religious festival and ritual theatre of Saloor-Dungra village in Chamoli, is on UNESCO's list of the Intangible Cultural Heritage of Humanity; and the Nanda Devi Raj Jat, a long Himalayan pilgrimage, is held roughly every twelve years. Dances include the langvir nritya, chholiya — a sword dance at Kumaoni weddings — and the circle dances of Jaunsar. Aipan, red-and-white ritual floor and wall art, ringal bamboo work, copperware from Almora and woollen thulma and dann rugs are registered GIs, and the Pahari painting of Garhwal flourished at the Srinagar court.",
        "गढ़वाली और कुमाऊँनी लोक संस्कृति गीत, नृत्य और अनुष्ठानों से समृद्ध है। जागर अनुष्ठान जगरिया के गीतों और ढोल-दमाऊ की थाप से स्थानीय देवताओं का आह्वान करते हैं; चमोली के सलूड़-डुंग्रा गाँव का धार्मिक उत्सव और अनुष्ठानिक रंगमंच रम्माण यूनेस्को की मानवता की अमूर्त सांस्कृतिक विरासत सूची में है; और हिमालय की लंबी तीर्थयात्रा नंदा देवी राजजात लगभग हर बारह वर्ष में होती है। नृत्यों में लांगवीर नृत्य, कुमाऊँनी शादियों का तलवार नृत्य छोलिया और जौनसार के घेरा नृत्य शामिल हैं। ऐपण — लाल-सफ़ेद अनुष्ठानिक भूमि और भित्ति कला — रिंगाल बाँस का काम, अल्मोड़ा के ताँबे के बर्तन और ऊनी थुलमा व दन क़ालीन पंजीकृत जीआई हैं, और गढ़वाल की पहाड़ी चित्रकला श्रीनगर दरबार में फली-फूली।",
        "गढवाली व कुमाऊँनी लोकसंस्कृती गाणी, नृत्य व विधींनी समृद्ध आहे. जागर विधी जगरियाच्या गाण्यांनी व ढोल-दमाऊच्या ठेक्यावर स्थानिक देवतांचे आवाहन करतात; चमोलीतील सलूड-डुंग्रा गावचा धार्मिक उत्सव व विधिनाट्य रम्माण युनेस्कोच्या मानवतेच्या अमूर्त सांस्कृतिक वारसा यादीत आहे; आणि हिमालयातील दीर्घ तीर्थयात्रा नंदादेवी राजजात साधारण दर बारा वर्षांनी होते. नृत्यांत लांगवीर नृत्य, कुमाऊँनी लग्नांतील तलवार नृत्य छोलिया आणि जौनसारची वर्तुळ नृत्ये यांचा समावेश आहे. ऐपण — लाल-पांढरी विधिवत भूमी व भित्तीकला — रिंगाल बांबूकाम, अल्मोड्याची तांब्याची भांडी आणि लोकरी थुलमा व दन गालिचे हे नोंदणीकृत जीआय आहेत, आणि गढवालची पहाडी चित्रकला श्रीनगरच्या दरबारात बहरली."),
        sources=["gi-registry"], conf="Editorial"),
    lst("festivals", [
        fest("harela", "Harela", "हरेला", "हरेला", ("July (Shravan)", "जुलाई (श्रावण)", "जुलै (श्रावण)"),
             ("Kumaoni festival of greenery; seedlings are sown and trees planted.", "हरियाली का कुमाऊँनी पर्व; अंकुर बोए और पेड़ लगाए जाते हैं।", "हिरवाईचा कुमाऊँनी सण; रोपे पेरली व झाडे लावली जातात.")),
        fest("phooldei", "Phool Dei", "फूलदेई", "फूलदेई", ("March (Chaitra)", "मार्च (चैत्र)", "मार्च (चैत्र)"),
             ("Children scatter spring flowers on doorsteps.", "बच्चे दरवाज़ों पर वसंत के फूल बिखेरते हैं।", "मुले उंबऱ्यांवर वसंताची फुले उधळतात.")),
        fest("uttarayani", "Uttarayani fair, Bageshwar", "उत्तरायणी मेला, बागेश्वर", "उत्तरायणी जत्रा, बागेश्वर", ("January (Makar Sankranti)", "जनवरी (मकर संक्रांति)", "जानेवारी (मकर संक्रांती)"),
             ("Fair at the confluence of the Saryu and Gomti.", "सरयू और गोमती के संगम पर मेला।", "सरयू व गोमतीच्या संगमावरील जत्रा.")),
        fest("nandadevi", "Nanda Devi fair and Raj Jat", "नंदा देवी मेला और राजजात", "नंदादेवी जत्रा व राजजात", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Fairs at Almora and Nainital; the Raj Jat pilgrimage roughly every 12 years.", "अल्मोड़ा और नैनीताल में मेले; लगभग हर 12 वर्ष में राजजात यात्रा।", "अल्मोडा व नैनीतालमध्ये जत्रा; साधारण दर 12 वर्षांनी राजजात यात्रा.")),
        fest("kumbh", "Kumbh and Ardh Kumbh, Haridwar", "कुंभ और अर्धकुंभ, हरिद्वार", "कुंभ व अर्धकुंभ, हरिद्वार", ("Every 12 and 6 years", "हर 12 और 6 वर्ष", "दर 12 व 6 वर्षांनी"),
             ("Mass bathing in the Ganga at Har ki Pauri.", "हर की पैड़ी पर गंगा में सामूहिक स्नान।", "हर की पौडी येथे गंगेत सामूहिक स्नान.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("jagar", "Jagar", "जागर", "जागर"), it3("ramman", "Ramman (UNESCO intangible heritage)", "रम्माण (यूनेस्को अमूर्त विरासत)", "रम्माण (युनेस्को अमूर्त वारसा)"),
        it3("chholiya", "Chholiya dance", "छोलिया नृत्य", "छोलिया नृत्य"), it3("aipan", "Aipan", "ऐपण", "ऐपण"),
        it3("ringal", "Ringal craft", "रिंगाल शिल्प", "रिंगाल हस्तकला"), it3("tamta", "Tamta copperware", "ताम्र (टम्टा) बर्तन", "तांब्याची (टमटा) भांडी"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("kafuli", "Kafuli", "काफुली", "काफुली", d=("Thick curry of spinach and fenugreek greens.", "पालक और मेथी के साग की गाढ़ी सब्ज़ी।", "पालक व मेथीची घट्ट भाजी.")),
        it3("bhatt", "Bhatt ki churkani", "भट्ट की चुड़कानी", "भट्टाची चुडकानी", d=("Black soybean (kala bhat) curry — kala bhat is a registered GI.", "काले भट्ट की सब्ज़ी — काला भट पंजीकृत जीआई है।", "काळ्या भट्टाची आमटी — काळा भट नोंदणीकृत जीआय आहे.")),
        it3("mandua", "Mandua roti and jhangora kheer", "मंडुए की रोटी और झंगोरे की खीर", "मंडुआची भाकरी व झंगोऱ्याची खीर", d=("Finger-millet bread and barnyard-millet pudding.", "मंडुए की रोटी और झंगोरे की खीर।", "नाचणीची भाकरी व सावा (झंगोरा) खीर.")),
        it3("balmithai", "Bal mithai", "बाल मिठाई", "बाल मिठाई", d=("Almora's fudge of roasted khoya coated with sugar balls.", "भुने खोए की अल्मोड़ा की मिठाई, चीनी के दानों से ढकी।", "भाजलेल्या खव्याची अल्मोड्याची मिठाई, साखरेच्या दाण्यांनी मढवलेली.")),
        it3("singori", "Singori", "सिंगोड़ी", "सिंगोडी", d=("Khoya sweet wrapped in a maalu leaf cone.", "मालू के पत्ते में लिपटी खोए की मिठाई।", "मालूच्या पानात गुंडाळलेली खव्याची मिठाई.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("pichhoda", "Rangwali pichhoda", "रंगवाली पिछौड़ा", "रंगवाली पिछौडा", d=("Kumaoni women's yellow-and-red ceremonial veil; a registered GI.", "कुमाऊँनी महिलाओं की पीली-लाल अनुष्ठानिक ओढ़नी; पंजीकृत जीआई।", "कुमाऊँनी स्त्रियांची पिवळी-लाल विधिवत ओढणी; नोंदणीकृत जीआय.")),
        it3("ghagra", "Ghagra, angra and pagdi", "घाघरा, अंगरा और पगड़ी", "घागरा, अंगरा व पगडी", d=("Traditional women's skirt and men's coat and turban in the hills.", "पहाड़ों में महिलाओं का पारंपरिक घाघरा और पुरुषों का अंगरखा व पगड़ी।", "डोंगरांत स्त्रियांचा पारंपरिक घागरा व पुरुषांचा अंगरखा आणि पगडी.")),
        it3("nath", "Nath", "नथ", "नथ", d=("Large gold nose ring worn by Garhwali and Kumaoni brides.", "गढ़वाली और कुमाऊँनी दुल्हनों की बड़ी सोने की नथ।", "गढवाली व कुमाऊँनी वधूंची मोठी सोन्याची नथ.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; th = 100 * g["trade_hotels"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["UK"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["UK"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Uttarakhand's GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26, the latest year published for the State in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2025-26'][0])}. In FY2024-25 manufacturing made up about {mfg:.0f}% of GSVA, trade, repair, hotels and restaurants about {th:.0f}%, and agriculture, livestock and forestry about {agri:.0f}%. Industry grew rapidly after the special incentive package that followed statehood, with industrial estates of SIDCUL at Haridwar, Pantnagar and Sitarganj making vehicles, pharmaceuticals, FMCG goods and electronics. Pilgrimage and tourism — the Char Dham, Haridwar and Rishikesh, hill stations and Corbett — are the other mainstay, and hydro-electricity, horticulture and remittances from soldiers and migrants support the hills, where farming on small terraces is often unrewarding.\n\nThe PLFS unemployment rate was {ur['2025']}% in 2025, up from {ur['2024']}% in 2024 (India {ui['2025']}%), and {lf['female']}% of women aged 15 and above were in the labour force, against {lfi['female']}% nationally.",
        f"मोस्पी शृंखला में राज्य के लिए प्रकाशित नवीनतम वर्ष, वित्त वर्ष 2025-26 में उत्तराखंड का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2025-26'][0])}। वित्त वर्ष 2024-25 में जीएसवीए में विनिर्माण का हिस्सा लगभग {mfg:.0f}%, व्यापार, मरम्मत, होटल और रेस्तराँ का लगभग {th:.0f}%, और कृषि, पशुपालन व वानिकी का लगभग {agri:.0f}% था। राज्य बनने के बाद मिले विशेष प्रोत्साहन पैकेज से उद्योग तेज़ी से बढ़े, और हरिद्वार, पंतनगर और सितारगंज के सिडकुल औद्योगिक क्षेत्रों में वाहन, दवाएँ, एफ़एमसीजी सामान और इलेक्ट्रॉनिक्स बनते हैं। तीर्थयात्रा और पर्यटन — चार धाम, हरिद्वार और ऋषिकेश, पर्वतीय स्थल और कॉर्बेट — दूसरा मुख्य आधार हैं, और जलविद्युत, बाग़वानी तथा सैनिकों व प्रवासियों द्वारा भेजी गई रक़म पहाड़ों को सहारा देती है, जहाँ छोटे सीढ़ीदार खेतों पर खेती अक्सर कम लाभ देती है।\n\nपीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी, जो 2024 में {ur['2024']}% थी (भारत {ui['2025']}%), और 15 वर्ष से अधिक आयु की {lf['female']}% महिलाएँ श्रम बल में थीं, जबकि राष्ट्रीय स्तर पर {lfi['female']}%।",
        f"मोस्पी मालिकेत राज्यासाठी प्रकाशित नवीनतम वर्ष, आ.व. 2025-26 मध्ये उत्तराखंडचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2025-26'][0])}. आ.व. 2024-25 मध्ये जीएसव्हीएमध्ये उत्पादन उद्योगाचा वाटा सुमारे {mfg:.0f}%, व्यापार, दुरुस्ती, हॉटेल व उपाहारगृहांचा सुमारे {th:.0f}%, आणि शेती, पशुपालन व वनीकरणाचा सुमारे {agri:.0f}% होता. राज्यनिर्मितीनंतर मिळालेल्या विशेष प्रोत्साहन पॅकेजमुळे उद्योग झपाट्याने वाढले, आणि हरिद्वार, पंतनगर व सितारगंज येथील सिडकुल औद्योगिक वसाहतींत वाहने, औषधे, एफएमसीजी वस्तू व इलेक्ट्रॉनिक्स बनतात. तीर्थयात्रा व पर्यटन — चार धाम, हरिद्वार व ऋषिकेश, थंड हवेची ठिकाणे व कॉर्बेट — हा दुसरा मुख्य आधार आहे, आणि जलविद्युत, फलोत्पादन व सैनिक आणि स्थलांतरितांनी पाठवलेले पैसे डोंगरांना आधार देतात, जिथे लहान पायऱ्यांच्या शेतांवरील शेती अनेकदा फारशी फायदेशीर नसते.\n\nपीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता, 2024 मध्ये {ur['2024']}% होता (भारत {ui['2025']}%), आणि 15 वर्षांवरील {lf['female']}% स्त्रिया श्रमशक्तीत होत्या, तर राष्ट्रीय पातळीवर {lfi['female']}%."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_UK), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_UK), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_UK), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("UK", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    plfs_series("UK", NAME),
    lst("sectors-key", [
        it3("pilgrim", "Pilgrimage and tourism", "तीर्थयात्रा और पर्यटन", "तीर्थयात्रा व पर्यटन", d=("Char Dham, Haridwar, Rishikesh, Nainital, Mussoorie and Corbett.", "चार धाम, हरिद्वार, ऋषिकेश, नैनीताल, मसूरी और कॉर्बेट।", "चार धाम, हरिद्वार, ऋषिकेश, नैनीताल, मसुरी व कॉर्बेट.")),
        it3("auto", "Automobiles and components", "ऑटोमोबाइल और कलपुर्ज़े", "मोटारी व सुटे भाग", d=("Commercial-vehicle and two-wheeler plants at Pantnagar and Haridwar.", "पंतनगर और हरिद्वार में वाणिज्यिक वाहन और दोपहिया संयंत्र।", "पंतनगर व हरिद्वार येथे व्यावसायिक वाहने व दुचाकी कारखाने.")),
        it3("pharma", "Pharmaceuticals and FMCG", "दवाएँ और एफ़एमसीजी", "औषधे व एफएमसीजी", d=("SIDCUL estates at Haridwar and Selaqui.", "हरिद्वार और सेलाकुई के सिडकुल क्षेत्र।", "हरिद्वार व सेलाकुई येथील सिडकुल वसाहती.")),
        it3("hydro", "Hydro-electricity", "जलविद्युत", "जलविद्युत", d=("Tehri, Koteshwar and other projects on the Ganga's headwaters.", "गंगा के उद्गम क्षेत्र पर टिहरी, कोटेश्वर और अन्य परियोजनाएँ।", "गंगेच्या उगम प्रदेशातील टिहरी, कोटेश्वर व इतर प्रकल्प.")),
        it3("horti", "Horticulture and millets", "बाग़वानी और मोटे अनाज", "फलोत्पादन व भरडधान्ये", d=("Apples, malta, litchi, peaches; mandua and jhangora.", "सेब, माल्टा, लीची, आड़ू; मंडुआ और झंगोरा।", "सफरचंद, माल्टा, लिची, पीच; नाचणी व झंगोरा.")),
        it3("edu", "Education and research", "शिक्षा और शोध", "शिक्षण व संशोधन", d=("Dehradun's schools, IIT Roorkee and national institutes.", "देहरादून के विद्यालय, आईआईटी रुड़की और राष्ट्रीय संस्थान।", "डेहराडूनच्या शाळा, आयआयटी रुडकी व राष्ट्रीय संस्था.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Char Dham pilgrim numbers by year", "वर्षवार चार धाम तीर्थयात्री संख्या", "वर्षनिहाय चार धाम यात्रेकरू संख्या"), "india-gov", "Uttarakhand Tourism Development Board / Char Dham registration portal."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("Sectoral GSVA for FY2025-26", "वित्त वर्ष 2025-26 का क्षेत्रवार जीएसवीए", "आ.व. 2025-26 चे क्षेत्रनिहाय जीएसव्हीए"), "mospi", "The sector table uses FY2024-25, the year fetched."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Uttarakhand has a unicameral legislature, the 70-member Vidhan Sabha, which sits in Dehradun and also holds sessions at Bhararisain (Gairsain). The State elects 5 members to the Lok Sabha and 3 to the Rajya Sabha.\n\nThe Bharatiya Janata Party won 47 of the 70 seats in the Assembly election of 2022, and Pushkar Singh Dhami — Chief Minister since July 2021 — was sworn in for a second term on 23 March 2022, although he had lost his own seat; he later won a by-election. Ritu Khanduri Bhushan (BJP), the first woman Speaker, presides over the Assembly. Dr Dhal Singh Bisen was sworn in as Governor on 19 October 2026. The next Assembly election is due by early 2027.",
        "उत्तराखंड में एकसदनीय विधानमंडल है, 70 सदस्यों वाली विधानसभा, जिसकी बैठकें देहरादून में होती हैं और भराड़ीसैंण (गैरसैंण) में भी सत्र होते हैं। राज्य से लोकसभा के 5 और राज्यसभा के 3 सदस्य चुने जाते हैं।\n\n2022 के विधानसभा चुनाव में भारतीय जनता पार्टी ने 70 में से 47 सीटें जीतीं, और जुलाई 2021 से मुख्यमंत्री पुष्कर सिंह धामी ने 23 मार्च 2022 को दूसरे कार्यकाल की शपथ ली, हालाँकि वे अपनी सीट हार गए थे; बाद में उन्होंने उपचुनाव जीता। पहली महिला अध्यक्ष ऋतु खंडूड़ी भूषण (भाजपा) विधानसभा की अध्यक्षता करती हैं। डॉ. ढाल सिंह बिसेन ने 19 अक्टूबर 2026 को राज्यपाल पद की शपथ ली। अगला विधानसभा चुनाव 2027 की शुरुआत तक होना है।",
        "उत्तराखंडमध्ये एकसदनी विधिमंडळ आहे, 70 सदस्यांची विधानसभा, जिच्या बैठका डेहराडूनमध्ये होतात व भराडीसैंण (गैरसैंण) येथेही अधिवेशने होतात. राज्यातून लोकसभेवर 5 व राज्यसभेवर 3 सदस्य निवडले जातात.\n\n2022 च्या विधानसभा निवडणुकीत भारतीय जनता पक्षाने 70 पैकी 47 जागा जिंकल्या, आणि जुलै 2021 पासून मुख्यमंत्री असलेल्या पुष्करसिंह धामी यांनी 23 मार्च 2022 रोजी दुसऱ्या कारकिर्दीची शपथ घेतली, जरी ते स्वतःची जागा हरले होते; नंतर त्यांनी पोटनिवडणूक जिंकली. पहिल्या महिला अध्यक्ष ऋतू खंडुरी भूषण (भाजप) विधानसभेचे अध्यक्षपद भूषवतात. डॉ. ढालसिंह बिसेन यांनी 19 ऑक्टोबर 2026 रोजी राज्यपालपदाची शपथ घेतली. पुढील विधानसभा निवडणूक 2027 च्या सुरुवातीपर्यंत होणे अपेक्षित आहे."),
        sources=["tribune", "deccan-chronicle", "drishti"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("gov", "Lok Bhavan Uttarakhand", "लोक भवन उत्तराखंड", "लोक भवन उत्तराखंड", url="https://governoruk.gov.in", src="india-gov"),
        it3("portal", "Government of Uttarakhand", "उत्तराखंड सरकार", "उत्तराखंड शासन", url="https://uk.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2022 Assembly election — party-wise result", "2022 विधानसभा चुनाव — दलवार परिणाम", "2022 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Uttarakhand 2022."),
        (L("Chief Minister's by-election (Champawat, 2022)", "मुख्यमंत्री का उपचुनाव (चंपावत, 2022)", "मुख्यमंत्र्यांची पोटनिवडणूक (चंपावत, 2022)"), "eci", "ECI bye-election result."),
        (L("Governor's swearing-in — official source", "राज्यपाल का शपथ ग्रहण — आधिकारिक स्रोत", "राज्यपालांचा शपथविधी — अधिकृत स्रोत"), "india-gov", "Lok Bhavan Uttarakhand release."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "The Rishikesh–Karnaprayag railway, most of it in tunnels, is under construction, and ropeways to Kedarnath and Hemkund Sahib were approved in March 2025. Other large works include the all-weather Char Dham road project and the Delhi–Dehradun expressway; these will be added as cards once their status is confirmed from official sources. Each card shows its source and the date it was checked.",
        "ऋषिकेश–कर्णप्रयाग रेलवे, जिसका अधिकांश भाग सुरंगों में है, निर्माणाधीन है, और केदारनाथ व हेमकुंड साहिब के रोपवे मार्च 2025 में स्वीकृत हुए। अन्य बड़े कार्यों में हर मौसम वाली चार धाम सड़क परियोजना और दिल्ली–देहरादून एक्सप्रेसवे शामिल हैं; आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर इन्हें कार्ड के रूप में जोड़ा जाएगा। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "ऋषिकेश–कर्णप्रयाग रेल्वे, जिचा बहुतांश भाग बोगद्यांत आहे, बांधकामाधीन आहे, आणि केदारनाथ व हेमकुंड साहिबचे रोपवे मार्च 2025 मध्ये मंजूर झाले. इतर मोठ्या कामांत सर्व हवामानातील चार धाम रस्ता प्रकल्प व दिल्ली–डेहराडून द्रुतगती मार्ग यांचा समावेश आहे; अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर त्यांची कार्डे जोडली जातील. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["newsonair", "etv-bharat"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Char Dham all-weather road — status", "चार धाम ऑल-वेदर सड़क — स्थिति", "चार धाम सर्व-हवामान रस्ता — स्थिती"), "morth", "MoRTH project status."),
        (L("Rishikesh–Karnaprayag line — official status page", "ऋषिकेश–कर्णप्रयाग लाइन — आधिकारिक स्थिति पृष्ठ", "ऋषिकेश–कर्णप्रयाग मार्गिका — अधिकृत स्थिती पान"), "railways", "Replace the news report with the Lok Sabha answer or RVNL page."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Jolly Grant Airport near Dehradun is the main airport, with Pantnagar serving Kumaon and small airstrips and heliports — including Pithoragarh (Naini Saini) and helipads used for Kedarnath — in the hills. Railways reach only the foothills: Dehradun, Haridwar, Rishikesh (Yog Nagari), Kathgodam, Ramnagar and Tanakpur. Most travel in the hills is by road, on highways that follow the river valleys to Badrinath, Kedarnath, Gangotri, Yamunotri and Pithoragarh, and are being widened under the Char Dham project. Landslides often close these roads in the monsoon.",
        "देहरादून के पास जॉली ग्रांट हवाई अड्डा मुख्य हवाई अड्डा है, पंतनगर कुमाऊँ को सेवा देता है, और पहाड़ों में छोटी हवाई पट्टियाँ और हेलीपोर्ट हैं — जिनमें पिथौरागढ़ (नैनी सैनी) और केदारनाथ के लिए उपयोग होने वाले हेलीपैड शामिल हैं। रेल केवल तलहटी तक पहुँचती है: देहरादून, हरिद्वार, ऋषिकेश (योग नगरी), काठगोदाम, रामनगर और टनकपुर। पहाड़ों में अधिकांश यात्रा सड़क से होती है, उन राजमार्गों पर जो नदी घाटियों के साथ बद्रीनाथ, केदारनाथ, गंगोत्री, यमुनोत्री और पिथौरागढ़ तक जाते हैं और चार धाम परियोजना के तहत चौड़े किए जा रहे हैं। मानसून में भूस्खलन अक्सर इन सड़कों को बंद कर देते हैं।",
        "डेहराडूनजवळील जॉली ग्रांट विमानतळ हा मुख्य विमानतळ आहे, पंतनगर कुमाऊँला सेवा देतो, आणि डोंगरांत लहान धावपट्ट्या व हेलिपोर्ट आहेत — ज्यांत पिथौरागड (नैनी सैनी) व केदारनाथसाठी वापरले जाणारे हेलिपॅड आहेत. रेल्वे केवळ पायथ्यापर्यंत पोहोचते: डेहराडून, हरिद्वार, ऋषिकेश (योगनगरी), काठगोदाम, रामनगर व टनकपूर. डोंगरांत बहुतेक प्रवास रस्त्याने होतो, नदीखोऱ्यांच्या बाजूने बद्रीनाथ, केदारनाथ, गंगोत्री, यमुनोत्री व पिथौरागडपर्यंत जाणाऱ्या महामार्गांवरून, जे चार धाम प्रकल्पाअंतर्गत रुंद केले जात आहेत. मान्सूनमध्ये भूस्खलन अनेकदा हे रस्ते बंद करतात."),
        conf="Editorial"),
    lst("airports", [
        it3("ded", "Jolly Grant Airport, Dehradun", "जॉली ग्रांट हवाई अड्डा, देहरादून", "जॉली ग्रांट विमानतळ, डेहराडून", m=("DED", "DED", "DED")),
        it3("pgh", "Pantnagar Airport", "पंतनगर हवाई अड्डा", "पंतनगर विमानतळ", m=("PGH", "PGH", "PGH")),
        it3("pith", "Pithoragarh (Naini Saini)", "पिथौरागढ़ (नैनी सैनी)", "पिथौरागड (नैनी सैनी)", m=("Regional", "क्षेत्रीय", "प्रादेशिक")),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("Road length and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Hydro-electricity is Uttarakhand's main power source. The Tehri dam on the Bhagirathi, with the Koteshwar project below it, is run by THDC India; NHPC operates the Dhauliganga station; and the State's UJVN runs older projects on the Yamuna, Ganga and their tributaries. Many further projects on the upper Ganga have been delayed or halted over environmental and safety concerns, especially after the floods of 2013 and 2021, when the Rishiganga and Tapovan–Vishnugad projects were badly damaged. Solar power is growing in the plains.",
        "जलविद्युत उत्तराखंड का मुख्य बिजली स्रोत है। भागीरथी पर टिहरी बाँध, उसके नीचे कोटेश्वर परियोजना सहित, टीएचडीसी इंडिया चलाता है; एनएचपीसी धौलीगंगा केंद्र संचालित करता है; और राज्य का यूजेवीएन यमुना, गंगा और उनकी सहायक नदियों पर पुरानी परियोजनाएँ चलाता है। ऊपरी गंगा पर कई और परियोजनाएँ पर्यावरण और सुरक्षा चिंताओं के कारण टल गईं या रुक गईं, विशेषकर 2013 और 2021 की बाढ़ के बाद, जब ऋषिगंगा और तपोवन–विष्णुगाड़ परियोजनाओं को भारी नुकसान हुआ। मैदानों में सौर ऊर्जा बढ़ रही है।",
        "जलविद्युत हा उत्तराखंडचा मुख्य वीजस्रोत आहे. भागीरथीवरील टिहरी धरण, त्याखालील कोटेश्वर प्रकल्पासह, टीएचडीसी इंडिया चालवते; एनएचपीसी धौलीगंगा केंद्र चालवते; आणि राज्याचे यूजेव्हीएन यमुना, गंगा व उपनद्यांवरील जुने प्रकल्प चालवते. वरच्या गंगेवरील अनेक नवे प्रकल्प पर्यावरण व सुरक्षाविषयक चिंतांमुळे लांबले किंवा थांबले, विशेषतः 2013 व 2021 च्या पुरांनंतर, जेव्हा ऋषिगंगा व तपोवन–विष्णुगाड प्रकल्पांचे मोठे नुकसान झाले. मैदानी भागात सौरऊर्जा वाढत आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Status of suspended hydro projects on the upper Ganga", "ऊपरी गंगा पर स्थगित जलविद्युत परियोजनाओं की स्थिति", "वरच्या गंगेवरील स्थगित जलविद्युत प्रकल्पांची स्थिती"), "india-gov", "Ministry of Jal Shakti / Supreme Court orders."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Dehradun is the State's technology and education hub, with an IT park at Sahastradhara Road and national scientific institutions such as the Indian Institute of Remote Sensing (ISRO), the Survey of India headquarters and the Wildlife Institute of India. Citizen services are delivered through the State's e-district portal and common service centres, and mobile coverage is weakest in the remote border valleys.",
        "देहरादून राज्य का प्रौद्योगिकी और शिक्षा केंद्र है, जहाँ सहस्त्रधारा रोड पर आईटी पार्क और भारतीय सुदूर संवेदन संस्थान (इसरो), सर्वे ऑफ़ इंडिया मुख्यालय और भारतीय वन्यजीव संस्थान जैसे राष्ट्रीय वैज्ञानिक संस्थान हैं। नागरिक सेवाएँ राज्य के ई-डिस्ट्रिक्ट पोर्टल और सामान्य सेवा केंद्रों से दी जाती हैं, और दूरस्थ सीमावर्ती घाटियों में मोबाइल कवरेज सबसे कमज़ोर है।",
        "डेहराडून हे राज्याचे तंत्रज्ञान व शिक्षण केंद्र आहे, जिथे सहस्रधारा रोडवर आयटी पार्क आणि भारतीय सुदूर संवेदन संस्था (इस्रो), सर्व्हे ऑफ इंडियाचे मुख्यालय व भारतीय वन्यजीव संस्था यांसारख्या राष्ट्रीय वैज्ञानिक संस्था आहेत. नागरी सेवा राज्याच्या ई-डिस्ट्रिक्ट संकेतस्थळ व सामायिक सेवा केंद्रांमार्फत दिल्या जातात, आणि दुर्गम सीमावर्ती खोऱ्यांत मोबाइल कव्हरेज सर्वांत कमकुवत आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (UP West / Uttarakhand circle)."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("UK", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["UK"]
ger = AP["aishe_ger"]["UK"]; nu = AP["aishe_universities_2021_22"]["UK"]; nc = AP["aishe_colleges_2021_22"]["UK"]
module(R, "education", [
    prose("p1", L(
        f"Uttarakhand's higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE, well above the national 28.4% and up from {ger['2017-18']}% in 2017-18 (it was {ger['2020-21']}% in 2020-21); women's GER ({gf}%) was higher than men's ({gm}%). The State had {nu} universities and {inr(nc)} colleges, and literacy at the 2011 Census was 78.8%.\n\nIIT Roorkee grew from the Thomason College of Civil Engineering, founded in 1847. G. B. Pant University of Agriculture and Technology at Pantnagar (1960) was India's first agricultural university of the land-grant type, and H. N. B. Garhwal University (a Central University) at Srinagar and Kumaun University at Nainital serve the hills. Dehradun hosts the Forest Research Institute, the Wildlife Institute of India, the Indian Military Academy and the Doon School, and Mussoorie the Lal Bahadur Shastri National Academy of Administration, which trains civil servants; IIM Kashipur and AIIMS Rishikesh are newer national institutions.",
        f"एआईएसएचई के अनुसार 2021-22 में उत्तराखंड का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था, जो राष्ट्रीय 28.4% से काफ़ी अधिक और 2017-18 के {ger['2017-18']}% से ऊपर है (2020-21 में यह {ger['2020-21']}% था); महिलाओं का जीईआर ({gf}%) पुरुषों ({gm}%) से अधिक था। राज्य में {nu} विश्वविद्यालय और {inr(nc)} कॉलेज थे, और 2011 की जनगणना में साक्षरता 78.8% थी।\n\nआईआईटी रुड़की 1847 में स्थापित थॉमसन कॉलेज ऑफ़ सिविल इंजीनियरिंग से विकसित हुआ। पंतनगर का गोविंद बल्लभ पंत कृषि एवं प्रौद्योगिकी विश्वविद्यालय (1960) लैंड-ग्रांट प्रकार का भारत का पहला कृषि विश्वविद्यालय था, और श्रीनगर का हेमवती नंदन बहुगुणा गढ़वाल विश्वविद्यालय (केंद्रीय विश्वविद्यालय) और नैनीताल का कुमाऊँ विश्वविद्यालय पहाड़ों को सेवा देते हैं। देहरादून में वन अनुसंधान संस्थान, भारतीय वन्यजीव संस्थान, भारतीय सैन्य अकादमी और दून स्कूल हैं, और मसूरी में सिविल सेवकों को प्रशिक्षण देने वाली लाल बहादुर शास्त्री राष्ट्रीय प्रशासन अकादमी; आईआईएम काशीपुर और एम्स ऋषिकेश नए राष्ट्रीय संस्थान हैं।",
        f"एआयएसएचईनुसार 2021-22 मध्ये उत्तराखंडचे उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा बरेच अधिक व 2017-18 मधील {ger['2017-18']}% पेक्षा जास्त (2020-21 मध्ये ते {ger['2020-21']}% होते); स्त्रियांचे जीईआर ({gf}%) पुरुषांपेक्षा ({gm}%) अधिक होते. राज्यात {nu} विद्यापीठे व {inr(nc)} महाविद्यालये होती, आणि 2011 च्या जनगणनेत साक्षरता 78.8% होती.\n\nआयआयटी रुडकी 1847 मध्ये स्थापन झालेल्या थॉमसन कॉलेज ऑफ सिव्हिल इंजिनिअरिंगमधून विकसित झाली. पंतनगरचे गोविंद वल्लभ पंत कृषी व तंत्रज्ञान विद्यापीठ (1960) हे लँड-ग्रांट प्रकारचे भारतातील पहिले कृषी विद्यापीठ होते, आणि श्रीनगरचे हेमवती नंदन बहुगुणा गढवाल विद्यापीठ (केंद्रीय विद्यापीठ) व नैनीतालचे कुमाऊँ विद्यापीठ डोंगरी भागाला सेवा देतात. डेहराडूनमध्ये वन संशोधन संस्था, भारतीय वन्यजीव संस्था, भारतीय लष्करी अकादमी व डून स्कूल आहेत, आणि मसुरीत नागरी सेवकांना प्रशिक्षण देणारी लालबहादूर शास्त्री राष्ट्रीय प्रशासन अकादमी; आयआयएम काशीपूर व एम्स ऋषिकेश या नव्या राष्ट्रीय संस्था आहेत."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("iitr", "IIT Roorkee", "आईआईटी रुड़की", "आयआयटी रुडकी", m=("Roorkee, 1847 (as Thomason College)", "रुड़की, 1847 (थॉमसन कॉलेज के रूप में)", "रुडकी, 1847 (थॉमसन कॉलेज म्हणून)")),
        it3("gbpuat", "G. B. Pant University of Agriculture and Technology", "गो. ब. पंत कृषि एवं प्रौद्योगिकी विश्वविद्यालय", "गो. व. पंत कृषी व तंत्रज्ञान विद्यापीठ", m=("Pantnagar, 1960", "पंतनगर, 1960", "पंतनगर, 1960")),
        it3("hnbgu", "H. N. B. Garhwal University", "हे. न. ब. गढ़वाल विश्वविद्यालय", "हे. न. ब. गढवाल विद्यापीठ", m=("Srinagar (Garhwal)", "श्रीनगर (गढ़वाल)", "श्रीनगर (गढवाल)")),
        it3("ku", "Kumaun University", "कुमाऊँ विश्वविद्यालय", "कुमाऊँ विद्यापीठ", m=("Nainital", "नैनीताल", "नैनीताल")),
        it3("fri", "Forest Research Institute", "वन अनुसंधान संस्थान", "वन संशोधन संस्था", m=("Dehradun", "देहरादून", "डेहराडून")),
        it3("ima", "Indian Military Academy", "भारतीय सैन्य अकादमी", "भारतीय लष्करी अकादमी", m=("Dehradun", "देहरादून", "डेहराडून")),
        it3("lbsnaa", "LBSNAA", "लाल बहादुर शास्त्री राष्ट्रीय प्रशासन अकादमी", "लालबहादूर शास्त्री राष्ट्रीय प्रशासन अकादमी", m=("Mussoorie", "मसूरी", "मसुरी")),
        it3("aiimsr", "AIIMS Rishikesh", "एम्स ऋषिकेश", "एम्स ऋषिकेश", m=("Rishikesh", "ऋषिकेश", "ऋषिकेश")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["UK"]; s = C["srs"]["UK"]
module(R, "health", [
    prose("p1", L(
        f"Uttarakhand's infant mortality rate fell from {s[4]} per 1,000 live births in 2010 to {s[5]:.0f} in 2020, below the national 28, and the birth rate was {s[1]} per 1,000 (death rate {s[3]}). Child nutrition improved between the two national family health surveys: in NFHS-5, {n['stunted'][1]:.1f}% of children under five were stunted (from {n['stunted'][0]}%), {n['wasted'][1]:.1f}% wasted (from {n['wasted'][0]}%) and {n['underweight'][1]:.1f}% underweight (from {n['underweight'][0]}%). Institutional births rose from 68.6% to {n['institutional_N5']:.1f}%, still lower than in neighbouring Himachal Pradesh and Haryana, partly because of distance and terrain in the hills.\n\nAIIMS Rishikesh, the government medical colleges at Dehradun, Haldwani, Srinagar and Almora, and the Himalayan Institute at Jolly Grant are the main referral hospitals; helicopter and ambulance services link remote areas, and doctor shortages in hill hospitals are a long-standing problem.",
        f"उत्तराखंड की शिशु मृत्यु दर 2010 में प्रति 1,000 जीवित जन्म पर {s[4]} से घटकर 2020 में {s[5]:.0f} हो गई, जो राष्ट्रीय 28 से कम है, और जन्म दर प्रति 1,000 पर {s[1]} थी (मृत्यु दर {s[3]})। दो राष्ट्रीय परिवार स्वास्थ्य सर्वेक्षणों के बीच बाल पोषण में सुधार हुआ: एनएफ़एचएस-5 में पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने थे ({n['stunted'][0]}% से), {n['wasted'][1]:.1f}% दुबले ({n['wasted'][0]}% से) और {n['underweight'][1]:.1f}% कम वज़न के ({n['underweight'][0]}% से)। संस्थागत प्रसव 68.6% से बढ़कर {n['institutional_N5']:.1f}% हुए, जो पड़ोसी हिमाचल प्रदेश और हरियाणा से अब भी कम है, आंशिक रूप से पहाड़ों में दूरी और भूभाग के कारण।\n\nएम्स ऋषिकेश, देहरादून, हल्द्वानी, श्रीनगर और अल्मोड़ा के सरकारी मेडिकल कॉलेज, और जॉली ग्रांट का हिमालयन इंस्टिट्यूट मुख्य रेफ़रल अस्पताल हैं; हेलिकॉप्टर और एंबुलेंस सेवाएँ दूरस्थ क्षेत्रों को जोड़ती हैं, और पहाड़ी अस्पतालों में डॉक्टरों की कमी पुरानी समस्या है।",
        f"उत्तराखंडचा अर्भक मृत्युदर 2010 मध्ये दर 1,000 जिवंत जन्मांमागे {s[4]} वरून 2020 मध्ये {s[5]:.0f} वर आला, राष्ट्रीय 28 पेक्षा कमी, आणि जन्मदर दर 1,000 मागे {s[1]} होता (मृत्युदर {s[3]}). दोन राष्ट्रीय कुटुंब आरोग्य सर्वेक्षणांदरम्यान बालपोषण सुधारले: एनएफएचएस-5 मध्ये पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी होती ({n['stunted'][0]}% वरून), {n['wasted'][1]:.1f}% कृश ({n['wasted'][0]}% वरून) व {n['underweight'][1]:.1f}% कमी वजनाची ({n['underweight'][0]}% वरून). संस्थात्मक प्रसूती 68.6% वरून {n['institutional_N5']:.1f}% झाल्या, जे शेजारच्या हिमाचल प्रदेश व हरियाणापेक्षा अजूनही कमी आहे, अंशतः डोंगरांतील अंतर व भूप्रदेशामुळे.\n\nएम्स ऋषिकेश, डेहराडून, हल्द्वानी, श्रीनगर व अल्मोड्याची शासकीय वैद्यकीय महाविद्यालये आणि जॉली ग्रांटची हिमालयन इन्स्टिट्यूट ही मुख्य संदर्भ रुग्णालये आहेत; हेलिकॉप्टर व रुग्णवाहिका सेवा दुर्गम भाग जोडतात, आणि डोंगरी रुग्णालयांतील डॉक्टरांची कमतरता ही जुनी समस्या आहे."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("UK"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"), "srs", "Not in the SRS abridged life table for major States used here (Economic Survey 2021-22, Table 8.1)."),
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin."),
        (L("Doctor vacancies in hill districts", "पहाड़ी ज़िलों में डॉक्टरों के रिक्त पद", "डोंगरी जिल्ह्यांतील डॉक्टरांची रिक्त पदे"), "mohfw", "Health Dynamics of India / State Health Department."),
    ]),
])
print("uk mod2 ok")
