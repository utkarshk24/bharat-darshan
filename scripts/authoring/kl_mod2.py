import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-KL"
ECI = "https://results.eci.gov.in/ResultAcGenMay2026/partywiseresult-S11.htm"
mo = research("mospi_kl.json")
NAME = L("Keralam", "केरलम", "केरळम")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Keralam's performing arts are among India's most elaborate. Kathakali tells stories from the epics through painted faces, huge skirts and a precise language of hand gestures; Kutiyattam, the Sanskrit theatre performed in temple theatres, is recognised by UNESCO; Mohiniyattam is the State's graceful solo dance. In the north, Theyyam turns performers into deities for a night in village shrines. Kalaripayattu, the martial art, is still taught in traditional kalaris, and chenda drumming drives temple festivals.\n\nFood is built on rice, coconut, fish and spice. The Onam sadya, a vegetarian feast of more than a dozen dishes on a banana leaf, is the best-known meal; everyday staples include puttu with kadala curry, appam with stew, and fish curries soured with kudampuli. Malabar adds biryanis and snacks with Arab and Persian echoes.",
        "केरलम की प्रदर्शन कलाएँ भारत की सबसे विस्तृत कलाओं में हैं। कथकली रंगे चेहरों, बड़े घेरदार परिधानों और हस्त-मुद्राओं की सटीक भाषा के ज़रिए महाकाव्यों की कथाएँ कहती है; मंदिरों के रंगमंडपों में होने वाला संस्कृत रंगमंच कूडियाट्टम यूनेस्को द्वारा मान्य है; मोहिनीअट्टम राज्य का कोमल एकल नृत्य है। उत्तर में थेय्यम के दौरान कलाकार गाँव के देवस्थानों में एक रात के लिए देवता का रूप लेते हैं। युद्धकला कलरीपयट्टु आज भी पारंपरिक कलरियों में सिखाई जाती है, और चेंडा वादन मंदिर उत्सवों की धड़कन है।\n\nखान-पान चावल, नारियल, मछली और मसालों पर टिका है। केले के पत्ते पर परोसा जाने वाला ओणम सद्या — दर्जन भर से अधिक व्यंजनों वाला शाकाहारी भोज — सबसे प्रसिद्ध है; रोज़मर्रा में कडला करी के साथ पुट्टु, स्टू के साथ अप्पम और कुडमपुली से खट्टी की गई मछली करी आम हैं। मलबार की बिरयानी और नाश्तों में अरब और फ़ारसी प्रभाव झलकता है।",
        "केरळमच्या सादरीकरण कला भारतातील सर्वांत तपशीलवार कलांपैकी आहेत. रंगवलेले चेहरे, मोठे घेरदार पोशाख आणि हस्तमुद्रांची नेमकी भाषा वापरून कथकली महाकाव्यांतील कथा सांगते; मंदिरांच्या रंगमंडपांत सादर होणारे संस्कृत नाट्य कूडियाट्टम युनेस्कोमान्य आहे; मोहिनीअट्टम हे राज्याचे लालित्यपूर्ण एकल नृत्य आहे. उत्तरेत थेय्यममध्ये कलाकार गावातील देवस्थानांत एका रात्रीसाठी देवतेचे रूप घेतात. कळरीपयट्टू ही युद्धकला आजही पारंपरिक कळरींत शिकवली जाते, आणि चेंडा वादन मंदिरोत्सवांचा प्राण आहे.\n\nखाद्यसंस्कृती भात, नारळ, मासे आणि मसाल्यांवर उभी आहे. केळीच्या पानावर वाढली जाणारी ओणम सद्या — डझनाहून अधिक पदार्थांची शाकाहारी मेजवानी — सर्वांत प्रसिद्ध आहे; रोजच्या जेवणात कडला करीसोबत पुट्टू, स्ट्यूसोबत अप्पम आणि कुडमपुळीने आंबट केलेली माशांची आमटी असते. मलबारच्या बिर्याणी आणि खाद्यपदार्थांत अरब व पर्शियन प्रभाव दिसतो."),
        conf="Editorial"),
    lst("festivals", [
        fest("onam", "Onam", "ओणम", "ओणम", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("The State festival: flower carpets (pookkalam), the sadya feast, boat races and folk games.", "राज्य का मुख्य उत्सव: फूलों का पूक्कलम, सद्या भोज, नौका दौड़ और लोक खेल।", "राज्याचा मुख्य सण: फुलांची पूक्कळम रांगोळी, सद्या मेजवानी, नौका शर्यती आणि लोकखेळ.")),
        fest("vishu", "Vishu", "विषु", "विषु", ("April", "अप्रैल", "एप्रिल"),
             ("Malayalam new year, begun by viewing the auspicious vishukkani arrangement at dawn.", "मलयालम नववर्ष, जो भोर में शुभ विषुक्कणि के दर्शन से शुरू होता है।", "मल्याळम नववर्ष; पहाटे शुभ विषुक्कणीच्या दर्शनाने सुरुवात.")),
        fest("pooram", "Thrissur Pooram", "त्रिशूर पूरम", "त्रिशूर पूरम", ("April–May", "अप्रैल–मई", "एप्रिल–मे"),
             ("Temple festival with rows of caparisoned elephants, percussion ensembles and fireworks.", "सजे-धजे हाथियों की कतारों, ताल-वाद्य मंडलियों और आतिशबाज़ी वाला मंदिर उत्सव।", "सजवलेल्या हत्तींच्या रांगा, तालवाद्य वृंद आणि आतषबाजी असलेला मंदिरोत्सव.")),
        fest("pongala", "Attukal Pongala", "आट्टुकाल पोंगाला", "आट्टुकाल पोंगाला", ("February–March", "फ़रवरी–मार्च", "फेब्रुवारी–मार्च"),
             ("Women cook offerings of sweet rice in clay pots along the streets of Thiruvananthapuram.", "तिरुवनंतपुरम की सड़कों पर महिलाएँ मिट्टी के बर्तनों में मीठे चावल का प्रसाद पकाती हैं।", "तिरुवनंतपुरमच्या रस्त्यांवर स्त्रिया मातीच्या भांड्यांत गोड भाताचा नैवेद्य शिजवतात.")),
        fest("boat", "Snake-boat races (Nehru Trophy, Aranmula)", "सर्प-नौका दौड़ (नेहरू ट्रॉफ़ी, आरनमुला)", "सर्प-नौका शर्यती (नेहरू ट्रॉफी, आरनमुळा)", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Long chundan vallam boats rowed by teams of a hundred or more.", "सौ या उससे अधिक नाविकों की टीमों द्वारा खेई जाने वाली लंबी चुंडन वल्लम नावें।", "शंभर किंवा अधिक वल्हेकऱ्यांच्या संघांनी वल्हवलेल्या लांबलचक चुंडन वल्लम नौका.")),
        fest("christmas", "Christmas and Easter", "क्रिसमस और ईस्टर", "नाताळ आणि ईस्टर", ("December; March–April", "दिसंबर; मार्च–अप्रैल", "डिसेंबर; मार्च–एप्रिल"),
             ("Star lanterns, church feasts and plum cakes across central Keralam.", "मध्य केरलम में तारे के आकार की लालटेनें, चर्च उत्सव और प्लम केक।", "मध्य केरळममध्ये ताऱ्याच्या आकाराचे कंदील, चर्चमधील उत्सव आणि प्लम केक.")),
        fest("eid", "Eid al-Fitr and Eid al-Adha", "ईद-उल-फ़ित्र और ईद-उल-अज़हा", "ईद-उल-फित्र आणि ईद-उल-अजहा", ("Lunar calendar", "चंद्र कैलेंडर", "चांद्र दिनदर्शिका"),
             ("Celebrated widely in Malabar with feasts and mappila songs.", "मलबार में भोज और माप्पिला गीतों के साथ धूमधाम से मनाई जाती हैं।", "मलबारमध्ये मेजवान्या आणि माप्पिळा गीतांसह उत्साहात साजरी होते.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("kathakali", "Kathakali", "कथकली", "कथकली"), it3("kutiyattam", "Kutiyattam", "कूडियाट्टम", "कूडियाट्टम"),
        it3("mohiniyattam", "Mohiniyattam", "मोहिनीअट्टम", "मोहिनीअट्टम"), it3("theyyam", "Theyyam", "थेय्यम", "थेय्यम"),
        it3("kalari", "Kalaripayattu", "कलरीपयट्टु", "कळरीपयट्टू"), it3("ottan", "Ottamthullal", "ओट्टमतुल्लल", "ओट्टमतुल्लल"),
        it3("chenda", "Chenda melam (percussion)", "चेंडा मेलम (ताल-वाद्य)", "चेंडा मेळम (तालवाद्य)"), it3("margam", "Margamkali", "मार्गमकली", "मार्गमकळी"),
        it3("oppana", "Oppana", "ओप्पना", "ओप्पना"), it3("thiruvathira", "Thiruvathirakali", "तिरुवातिराकली", "तिरुवातिराकळी"),
    ], layout="chips", title=L("Performing arts", "प्रदर्शन कलाएँ", "सादरीकरण कला"), conf="Editorial"),
    lst("food", [
        it3("sadya", "Sadya", "सद्या", "सद्या", d=("Festive vegetarian meal on a banana leaf: avial, olan, thoran, sambar, payasam and more.", "केले के पत्ते पर उत्सवी शाकाहारी भोजन: अवियल, ओलन, तोरन, सांभर, पायसम आदि।", "केळीच्या पानावर सणाचे शाकाहारी जेवण: अवियल, ओलन, तोरन, सांबार, पायसम इत्यादी.")),
        it3("puttu", "Puttu and kadala curry", "पुट्टु और कडला करी", "पुट्टू आणि कडला करी", d=("Steamed rice-and-coconut cylinders with black-chickpea curry.", "चावल और नारियल के भाप में पके बेलन, काले चने की करी के साथ।", "तांदूळ-नारळाचे वाफवलेले उभे गोळे, काळ्या हरभऱ्याच्या करीसोबत.")),
        it3("appam", "Appam and stew", "अप्पम और स्टू", "अप्पम आणि स्ट्यू", d=("Lacy fermented rice pancakes with a mild coconut-milk stew.", "जालीदार किण्वित चावल के पैनकेक, नारियल के दूध के हल्के स्टू के साथ।", "जाळीदार आंबवलेल्या तांदळाचे अप्पम, नारळाच्या दुधातील सौम्य स्ट्यूसोबत.")),
        it3("karimeen", "Karimeen pollichathu", "करिमीन पोल्लिचतु", "करिमीन पोल्लिचतू", d=("Pearl-spot fish marinated in spice and baked in banana leaf.", "मसाले में लिपटी पर्ल-स्पॉट मछली, केले के पत्ते में पकाई हुई।", "मसाल्यात मुरवलेला पर्ल-स्पॉट मासा, केळीच्या पानात भाजलेला.")),
        it3("biryani", "Thalassery biryani", "तलश्शेरी बिरयानी", "तलश्शेरी बिर्याणी", d=("Malabar biryani made with short-grain kaima rice.", "छोटे दाने वाले कैमा चावल से बनी मलबारी बिरयानी।", "लहान दाण्याच्या कैमा तांदळाची मलबारी बिर्याणी.")),
        it3("payasam", "Payasam", "पायसम", "पायसम", d=("Sweet puddings of rice, lentils or vermicelli with jaggery or milk.", "गुड़ या दूध के साथ चावल, दाल या सेवइयों की खीर।", "गूळ किंवा दुधासह तांदूळ, डाळ किंवा शेवयांची खीर.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("mundu", "Mundu and kasavu", "मुंडु और कसवु", "मुंडू आणि कसवू", d=("White or cream cotton wrap with a gold (kasavu) border, worn by men and women.", "सुनहरी (कसवु) किनारी वाला सफ़ेद या क्रीम रंग का सूती वस्त्र, जिसे पुरुष और महिलाएँ पहनते हैं।", "सोनेरी (कसवू) काठ असलेले पांढरे किंवा क्रीम रंगाचे सुती वस्त्र; स्त्री-पुरुष दोघेही नेसतात.")),
        it3("settu", "Set-mundu and set-saree", "सेट-मुंडु और सेट-साड़ी", "सेट-मुंडू आणि सेट-साडी", d=("Two-piece festive wear for women, typical at Onam and weddings.", "महिलाओं का दो हिस्सों वाला उत्सवी पहनावा, ओणम और विवाहों में आम।", "स्त्रियांचा दोन भागांचा सणासुदीचा पेहराव; ओणम आणि लग्नांत सामान्य.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
sect, (prim, sec, serv) = sector_table(mo["gsva2024_25_current_lakh"])
module(R, "economy", [
    prose("p1", L(
        f"Keralam's GSDP at current prices was about ₹{cur['FY2024-25'][0]/1e5:.2f} lakh crore in FY2024-25 in the MoSPI series, and its per capita NSDP of ₹{inr(pc['FY2024-25'][0])} is well above the national level. The economy leans heavily on services — trade, hotels and restaurants, real estate, transport and public services — which make up about {serv:.0f}% of GSVA. Remittances from Keralites working abroad, especially in the Gulf, have long supported household spending and construction.\n\nAgriculture is small in output but distinctive: coconut, rubber, pepper, cardamom, tea, coffee and cashew, alongside fisheries. Tourism, information technology around Thiruvananthapuram and Kochi, and the new Vizhinjam transshipment port are key growth areas. Unemployment, especially among educated young people, has been above the national average; the PLFS rate fell from 8.1% in 2022 to 4.4% in 2025.",
        f"मोस्पी शृंखला के अनुसार वित्त वर्ष 2024-25 में केरलम का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2024-25'][0]/1e5:.2f} लाख करोड़ था, और इसका प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2024-25'][0])} राष्ट्रीय स्तर से काफ़ी ऊपर है। अर्थव्यवस्था सेवाओं पर बहुत निर्भर है — व्यापार, होटल और रेस्तराँ, रियल एस्टेट, परिवहन और सार्वजनिक सेवाएँ — जो जीएसवीए का लगभग {serv:.0f}% हैं। विदेश में, ख़ासकर खाड़ी देशों में काम करने वाले केरलवासियों के भेजे पैसे लंबे समय से घरेलू खर्च और निर्माण को सहारा देते रहे हैं।\n\nकृषि का उत्पादन में हिस्सा छोटा है लेकिन विशिष्ट है: नारियल, रबर, काली मिर्च, इलायची, चाय, कॉफ़ी और काजू, साथ में मत्स्य पालन। पर्यटन, तिरुवनंतपुरम और कोच्चि के आसपास सूचना प्रौद्योगिकी, और नया विझिंजम ट्रांसशिपमेंट बंदरगाह विकास के प्रमुख क्षेत्र हैं। बेरोज़गारी, ख़ासकर पढ़े-लिखे युवाओं में, राष्ट्रीय औसत से अधिक रही है; पीएलएफ़एस दर 2022 के 8.1% से घटकर 2025 में 4.4% हो गई।",
        f"मोस्पी मालिकेनुसार आर्थिक वर्ष 2024-25 मध्ये केरळमचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2024-25'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2024-25'][0])} राष्ट्रीय पातळीपेक्षा बरेच जास्त आहे. अर्थव्यवस्था सेवाक्षेत्रावर मोठ्या प्रमाणात अवलंबून आहे — व्यापार, हॉटेल व उपाहारगृहे, स्थावर मालमत्ता, वाहतूक आणि सार्वजनिक सेवा — ज्यांचा जीएसव्हीएमध्ये सुमारे {serv:.0f}% वाटा आहे. परदेशात, विशेषतः आखाती देशांत काम करणाऱ्या केरळीयांनी पाठवलेल्या पैशांनी दीर्घकाळ घरगुती खर्च आणि बांधकामाला आधार दिला आहे.\n\nउत्पादनात शेतीचा वाटा लहान पण वैशिष्ट्यपूर्ण आहे: नारळ, रबर, मिरी, वेलची, चहा, कॉफी आणि काजू, सोबत मत्स्यव्यवसाय. पर्यटन, तिरुवनंतपुरम व कोचीभोवतीचे माहिती-तंत्रज्ञान आणि नवे विझिंजम ट्रान्सशिपमेंट बंदर ही वाढीची प्रमुख क्षेत्रे आहेत. बेरोजगारी, विशेषतः शिक्षित तरुणांतील, राष्ट्रीय सरासरीपेक्षा जास्त राहिली आहे; पीएलएफएस दर 2022 मधील 8.1% वरून 2025 मध्ये 4.4% पर्यंत घटला."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_NAS), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_NAS), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_NAS), "rupee", "higher-is-better",
             previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("KL", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    plfs_series("KL", NAME),
    lst("sectors-key", [
        it3("spices", "Spices", "मसाले", "मसाले", d=("Pepper, cardamom, nutmeg, clove and ginger; Kochi is a historic spice-trading port.", "काली मिर्च, इलायची, जायफल, लौंग और अदरक; कोच्चि ऐतिहासिक मसाला व्यापार बंदरगाह है।", "मिरी, वेलची, जायफळ, लवंग आणि आले; कोची हे ऐतिहासिक मसाला-व्यापार बंदर आहे.")),
        it3("plantation", "Rubber, coconut, tea and coffee", "रबर, नारियल, चाय और कॉफ़ी", "रबर, नारळ, चहा आणि कॉफी"),
        it3("cashew", "Cashew processing", "काजू प्रसंस्करण", "काजू प्रक्रिया", d=("Concentrated around Kollam.", "मुख्यतः कोल्लम के आसपास।", "मुख्यतः कोल्लमभोवती.")),
        it3("fish", "Marine fisheries and seafood exports", "समुद्री मत्स्य और समुद्री खाद्य निर्यात", "सागरी मासेमारी व सागरी अन्न निर्यात"),
        it3("it", "IT and start-ups", "आईटी और स्टार्टअप", "आयटी व स्टार्टअप", d=("Technopark (Thiruvananthapuram), Infopark (Kochi), Cyberpark (Kozhikode).", "टेक्नोपार्क (तिरुवनंतपुरम), इन्फ़ोपार्क (कोच्चि), साइबरपार्क (कोझिकोड)।", "टेक्नोपार्क (तिरुवनंतपुरम), इन्फोपार्क (कोची), सायबरपार्क (कोझिकोड).")),
        it3("tourism", "Tourism and Ayurveda", "पर्यटन और आयुर्वेद", "पर्यटन व आयुर्वेद"),
        it3("ports", "Ports and shipbuilding", "बंदरगाह और जहाज़ निर्माण", "बंदरे व जहाजबांधणी", d=("Cochin Port, Cochin Shipyard and Vizhinjam.", "कोचीन बंदरगाह, कोचीन शिपयार्ड और विझिंजम।", "कोचीन बंदर, कोचीन शिपयार्ड आणि विझिंजम.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey state shares; Kerala Migration Survey."),
        (L("Share of India's GDP", "भारत के जीडीपी में हिस्सा", "भारताच्या जीडीपीतील वाटा"), "mospi", "Needs the matching all-India GDP in the same base and vintage."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("FDI equity inflows", "एफ़डीआई इक्विटी प्रवाह", "एफडीआय समभाग गुंतवणूक"), "dpiit", "DPIIT state-wise FDI factsheet."),
        (L("Principal crops by area and output", "क्षेत्रफल और उत्पादन के अनुसार प्रमुख फ़सलें", "क्षेत्र व उत्पादनानुसार प्रमुख पिके"), "kl-spb", "Economic Review, agriculture chapter."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Keralam has a unicameral legislature: the 140-member Legislative Assembly (Niyamasabha) in Thiruvananthapuram. The State elects 20 members to the Lok Sabha and 9 to the Rajya Sabha. Elections have for decades been contested mainly between two broad fronts — the United Democratic Front (UDF), led by the Indian National Congress, and the Left Democratic Front (LDF), led by the CPI(M) — with the National Democratic Alliance (NDA) as a third front.\n\nIn the 2026 Assembly election, the UDF won a majority and V. D. Satheesan was sworn in as Chief Minister on 18 May 2026. Local government is strong: since the 1990s a large share of the State's plan funds has been devolved to panchayats and municipalities under the People's Plan Campaign.",
        "केरलम में एकसदनीय विधानमंडल है: तिरुवनंतपुरम में 140 सदस्यों वाली विधानसभा (नियमसभा)। राज्य से लोकसभा के 20 और राज्यसभा के 9 सदस्य चुने जाते हैं। दशकों से चुनाव मुख्यतः दो बड़े मोर्चों के बीच होते रहे हैं — भारतीय राष्ट्रीय कांग्रेस के नेतृत्व वाला संयुक्त लोकतांत्रिक मोर्चा (यूडीएफ़) और भाकपा (मार्क्सवादी) के नेतृत्व वाला वाम लोकतांत्रिक मोर्चा (एलडीएफ़) — और राष्ट्रीय जनतांत्रिक गठबंधन (एनडीए) तीसरा मोर्चा है।\n\n2026 के विधानसभा चुनाव में यूडीएफ़ को बहुमत मिला और वी. डी. सतीशन ने 18 मई 2026 को मुख्यमंत्री पद की शपथ ली। स्थानीय शासन मज़बूत है: 1990 के दशक से जन योजना अभियान के तहत राज्य की योजना निधि का बड़ा हिस्सा पंचायतों और नगरपालिकाओं को सौंपा गया है।",
        "केरळममध्ये एकसदनी विधिमंडळ आहे: तिरुवनंतपुरममधील 140 सदस्यांची विधानसभा (नियमसभा). राज्यातून लोकसभेवर 20 आणि राज्यसभेवर 9 सदस्य निवडले जातात. अनेक दशके निवडणुका प्रामुख्याने दोन मोठ्या आघाड्यांमध्ये होत आल्या आहेत — भारतीय राष्ट्रीय काँग्रेसच्या नेतृत्वाखालील संयुक्त लोकशाही आघाडी (यूडीएफ) आणि माकपच्या नेतृत्वाखालील डावी लोकशाही आघाडी (एलडीएफ) — तर राष्ट्रीय लोकशाही आघाडी (एनडीए) ही तिसरी आघाडी आहे.\n\n2026 च्या विधानसभा निवडणुकीत यूडीएफला बहुमत मिळाले आणि व्ही. डी. सतीशन यांनी 18 मे 2026 रोजी मुख्यमंत्रिपदाची शपथ घेतली. स्थानिक स्वराज्य संस्था सक्षम आहेत: 1990 च्या दशकापासून लोकनियोजन मोहिमेअंतर्गत राज्याच्या योजना निधीचा मोठा वाटा पंचायती व नगरपालिकांकडे सोपवला गेला आहे."),
        sources=["eci", "newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    table("results", L("Legislative Assembly election, 2026 — seats won", "विधानसभा चुनाव, 2026 — जीती गई सीटें", "विधानसभा निवडणूक, 2026 — जिंकलेल्या जागा"),
          [col(L("Party", "दल", "पक्ष")), col(L("Seats", "सीटें", "जागा"), "right")],
          [["Indian National Congress (INC)", 63], ["Communist Party of India (Marxist) (CPI(M))", 26], ["Indian Union Muslim League (IUML)", 22],
           ["Communist Party of India (CPI)", 8], ["KEC", 7], ["Revolutionary Socialist Party (RSP)", 3], ["Bharatiya Janata Party (BJP)", 3],
           [L("Other parties (one seat each: RJD, RMPOI, KEC(J), CMPKSC)", "अन्य दल (एक-एक सीट: RJD, RMPOI, KEC(J), CMPKSC)", "इतर पक्ष (प्रत्येकी एक जागा: RJD, RMPOI, KEC(J), CMPKSC)"), 4],
           [L("Independents", "निर्दलीय", "अपक्ष"), 4],
           [L("Total", "कुल", "एकूण"), 140]],
          "eci", ECI, period="2026",
          note=L("Party names and abbreviations as listed by the Election Commission (results declared May 2026). Parties are shown in order of seats, without colours or commentary. Seats are shown by party, not by front.",
                 "दलों के नाम और संक्षिप्त रूप चुनाव आयोग की सूची के अनुसार (परिणाम मई 2026 में घोषित)। दलों को सीटों के क्रम में, बिना रंग या टिप्पणी के दिखाया गया है। सीटें दलवार हैं, मोर्चावार नहीं।",
                 "पक्षांची नावे व संक्षेप निवडणूक आयोगाच्या यादीनुसार (निकाल मे 2026 मध्ये जाहीर). पक्ष जागांच्या क्रमाने, रंग किंवा भाष्याशिवाय दाखवले आहेत. जागा पक्षनिहाय आहेत, आघाडीनिहाय नाहीत.")),
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("sec", "State Election Commission, Keralam", "राज्य निर्वाचन आयोग, केरलम", "राज्य निवडणूक आयोग, केरळम", url="https://www.sec.kerala.gov.in", src="kl-gov"),
        it3("leg", "Kerala Legislative Assembly (Niyamasabha)", "केरल विधानसभा (नियमसभा)", "केरळ विधानसभा (नियमसभा)", url="https://www.niyamasabha.org", src="kl-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Governor's official page (Lok Bhavan)", "राज्यपाल का आधिकारिक पेज (लोक भवन)", "राज्यपालांचे अधिकृत पान (लोकभवन)"), "kl-gov", "Replace the news citations for the Governor and Leader of Opposition with official pages."),
        (L("Local bodies (grama panchayats, municipalities, corporations)", "स्थानीय निकाय (ग्राम पंचायतें, नगरपालिकाएँ, निगम)", "स्थानिक स्वराज्य संस्था (ग्रामपंचायती, नगरपालिका, महानगरपालिका)"), "kl-gov", "Local Self Government Department."),
        (L("Flagship welfare schemes", "प्रमुख कल्याण योजनाएँ", "प्रमुख कल्याणकारी योजना"), "kl-gov", "List with official scheme pages and current status."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Keralam's flagship recent project is the Vizhinjam International Deepwater Multipurpose Seaport near Thiruvananthapuram, dedicated to the nation in May 2025 as India's first dedicated container transshipment port. Other works in the pipeline include the extension of Kochi Metro and road widening along the national highway corridor; these are listed as gaps below until an official status page is linked.",
        "केरलम की हाल की प्रमुख परियोजना तिरुवनंतपुरम के पास विझिंजम अंतरराष्ट्रीय डीपवाटर बहुउद्देशीय बंदरगाह है, जिसे मई 2025 में भारत के पहले समर्पित कंटेनर ट्रांसशिपमेंट बंदरगाह के रूप में राष्ट्र को समर्पित किया गया। कोच्चि मेट्रो का विस्तार और राष्ट्रीय राजमार्ग गलियारे का चौड़ीकरण भी प्रगति में हैं; आधिकारिक स्थिति पेज जुड़ने तक इन्हें नीचे कमियों में रखा गया है।",
        "तिरुवनंतपुरमजवळील विझिंजम आंतरराष्ट्रीय खोल पाण्याचे बहुउद्देशीय बंदर हा केरळमचा अलीकडचा प्रमुख प्रकल्प असून मे 2025 मध्ये भारतातील पहिले समर्पित कंटेनर ट्रान्सशिपमेंट बंदर म्हणून ते राष्ट्राला समर्पित झाले. कोची मेट्रोचा विस्तार आणि राष्ट्रीय महामार्ग मार्गिकेचे रुंदीकरण हेही प्रगतिपथावर आहेत; अधिकृत स्थितीचे पान जोडले जाईपर्यंत ते खाली त्रुटींमध्ये दाखवले आहेत."),
        sources=["newsonair"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Kochi Metro Phase 2 (Kakkanad line) — official status and cost", "कोच्चि मेट्रो चरण 2 (काक्कनाड लाइन) — आधिकारिक स्थिति और लागत", "कोची मेट्रो टप्पा 2 (काक्कनाड मार्गिका) — अधिकृत स्थिती व खर्च"), "kl-gov", "KMRL or MoHUA page."),
        (L("NH 66 six-laning — official progress", "एनएच 66 छह-लेन — आधिकारिक प्रगति", "एनएच 66 सहापदरीकरण — अधिकृत प्रगती"), "morth", "MoRTH / NHAI project status."),
        (L("Vizhinjam port Phase 2 and developer details", "विझिंजम बंदरगाह चरण 2 और विकासकर्ता विवरण", "विझिंजम बंदर टप्पा 2 व विकासक तपशील"), "kl-gov", "Vizhinjam International Seaport Ltd."),
        (L("State vision document", "राज्य दृष्टि दस्तावेज़", "राज्य दृष्टी दस्तऐवज"), "kl-spb", "State Planning Board."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Keralam has four international airports — Thiruvananthapuram, Kochi, Kozhikode (Karipur) and Kannur — an unusually high number for its size, driven by Gulf travel. Kochi's airport was developed as a public–private company and runs on solar power. The railway runs the length of the coast from Kasaragod to Thiruvananthapuram, and NH 66 is the main road spine.\n\nKochi has a metro and, since 2023, a Water Metro using electric boats to link the islands of the harbour. The West Coast Canal (National Waterway 3) and the backwaters carry ferries and houseboats. Cochin Port and the new Vizhinjam port handle sea freight.",
        "केरलम में चार अंतरराष्ट्रीय हवाई अड्डे हैं — तिरुवनंतपुरम, कोच्चि, कोझिकोड (करिपुर) और कण्णूर — जो इसके आकार के हिसाब से असामान्य रूप से अधिक हैं; इसका कारण खाड़ी देशों की यात्रा है। कोच्चि हवाई अड्डा सार्वजनिक–निजी कंपनी के रूप में विकसित हुआ और सौर ऊर्जा से चलता है। रेल लाइन कासरगोड से तिरुवनंतपुरम तक पूरे तट के साथ चलती है, और एनएच 66 मुख्य सड़क धुरी है।\n\nकोच्चि में मेट्रो है और 2023 से वाटर मेट्रो भी, जो इलेक्ट्रिक नौकाओं से बंदरगाह के द्वीपों को जोड़ती है। पश्चिमी तट नहर (राष्ट्रीय जलमार्ग 3) और बैकवाटर में फ़ेरी और हाउसबोट चलती हैं। कोचीन बंदरगाह और नया विझिंजम बंदरगाह समुद्री माल संभालते हैं।",
        "केरळममध्ये चार आंतरराष्ट्रीय विमानतळ आहेत — तिरुवनंतपुरम, कोची, कोझिकोड (करिपूर) आणि कण्णूर — राज्याच्या आकाराच्या मानाने ही संख्या असामान्यपणे जास्त आहे, आणि त्यामागे आखाती देशांचा प्रवास आहे. कोची विमानतळ सार्वजनिक–खासगी कंपनी म्हणून विकसित झाले असून ते सौरऊर्जेवर चालते. रेल्वेमार्ग कासारगोडपासून तिरुवनंतपुरमपर्यंत संपूर्ण किनाऱ्यालगत जातो आणि एनएच 66 हा मुख्य रस्ता आहे.\n\nकोचीत मेट्रो आहे आणि 2023 पासून वॉटर मेट्रोही, जी विजेवरील नौकांद्वारे बंदरातील बेटे जोडते. पश्चिम किनारा कालवा (राष्ट्रीय जलमार्ग 3) आणि बॅकवॉटर्समध्ये फेरीबोटी व हाऊसबोटी चालतात. कोचीन बंदर आणि नवे विझिंजम बंदर सागरी मालवाहतूक हाताळतात."),
        conf="Editorial"),
    lst("airports", [
        it3("trv", "Thiruvananthapuram International Airport", "तिरुवनंतपुरम अंतरराष्ट्रीय हवाई अड्डा", "तिरुवनंतपुरम आंतरराष्ट्रीय विमानतळ", m=("TRV", "TRV", "TRV")),
        it3("cok", "Cochin International Airport", "कोचीन अंतरराष्ट्रीय हवाई अड्डा", "कोचीन आंतरराष्ट्रीय विमानतळ", m=("COK", "COK", "COK")),
        it3("ccj", "Calicut International Airport (Karipur)", "कालीकट अंतरराष्ट्रीय हवाई अड्डा (करिपुर)", "कालिकत आंतरराष्ट्रीय विमानतळ (करिपूर)", m=("CCJ", "CCJ", "CCJ")),
        it3("cnn", "Kannur International Airport", "कण्णूर अंतरराष्ट्रीय हवाई अड्डा", "कण्णूर आंतरराष्ट्रीय विमानतळ", m=("CNN", "CNN", "CNN")),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("National highway length", "राष्ट्रीय राजमार्ग की लंबाई", "राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Railway route length", "रेलवे मार्ग की लंबाई", "रेल्वे मार्गाची लांबी"), "railways", "Indian Railways Year Book."),
        (L("Metro and Water Metro network length and ridership", "मेट्रो और वाटर मेट्रो नेटवर्क लंबाई और यात्री संख्या", "मेट्रो व वॉटर मेट्रो जाळ्याची लांबी व प्रवासी संख्या"), "kl-gov", "KMRL annual report."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics (CIAL publishes its own)."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Keralam's own electricity generation has historically come mostly from hydropower, with the Idukki arch dam scheme the largest. Because rainfall varies from year to year and demand has grown, the State buys a large share of its power from central generating stations and the market. Rooftop solar has grown quickly, helped by high household electrification and the Kochi airport's example; the Kerala State Electricity Board (KSEB) is the main utility.",
        "केरलम की अपनी बिजली का अधिकांश हिस्सा ऐतिहासिक रूप से जलविद्युत से आता रहा है, जिसमें इडुक्की आर्च बाँध योजना सबसे बड़ी है। वर्षा साल-दर-साल बदलती है और माँग बढ़ी है, इसलिए राज्य अपनी बिजली का बड़ा हिस्सा केंद्रीय उत्पादन केंद्रों और बाज़ार से ख़रीदता है। छत पर सौर ऊर्जा तेज़ी से बढ़ी है, जिसमें घरों के व्यापक विद्युतीकरण और कोच्चि हवाई अड्डे के उदाहरण ने मदद की; केरल राज्य विद्युत बोर्ड (केएसईबी) मुख्य वितरक है।",
        "केरळमची स्वतःची वीजनिर्मिती पूर्वीपासून मुख्यतः जलविद्युतवर आधारित आहे; इडुक्की कमान धरण योजना सर्वांत मोठी. पाऊस वर्षागणिक बदलतो आणि मागणी वाढली आहे, त्यामुळे राज्य आपल्या विजेचा मोठा भाग केंद्रीय वीजनिर्मिती केंद्रांकडून आणि बाजारातून खरेदी करते. घरांचे व्यापक विद्युतीकरण आणि कोची विमानतळाच्या उदाहरणामुळे छतावरील सौरऊर्जा झपाट्याने वाढली आहे; केरळ राज्य वीज मंडळ (केएसईबी) ही मुख्य वितरण संस्था आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report (portal blocked automated access)."),
        (L("Renewable share and rooftop solar capacity", "नवीकरणीय हिस्सा और छत सौर क्षमता", "नवीकरणीय वाटा व छतावरील सौर क्षमता"), "mnre", "MNRE state-wise RE capacity."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Technopark in Thiruvananthapuram, opened in 1990, was one of India's first IT parks; Infopark in Kochi and Cyberpark in Kozhikode followed. The Kerala Startup Mission supports young companies, and the State-owned K-FON network aims to bring broadband to households and public offices. Digital University Kerala, in Thiruvananthapuram, focuses on digital technology education and research.",
        "1990 में खुला तिरुवनंतपुरम का टेक्नोपार्क भारत के पहले आईटी पार्कों में था; बाद में कोच्चि में इन्फ़ोपार्क और कोझिकोड में साइबरपार्क बने। केरल स्टार्टअप मिशन नई कंपनियों को सहायता देता है, और राज्य के स्वामित्व वाला के-फ़ोन नेटवर्क घरों और सरकारी दफ़्तरों तक ब्रॉडबैंड पहुँचाने का लक्ष्य रखता है। तिरुवनंतपुरम का डिजिटल विश्वविद्यालय केरल डिजिटल प्रौद्योगिकी की शिक्षा और शोध पर केंद्रित है।",
        "1990 मध्ये सुरू झालेले तिरुवनंतपुरमचे टेक्नोपार्क हे भारतातील पहिल्या आयटी पार्कांपैकी एक होते; त्यानंतर कोचीत इन्फोपार्क आणि कोझिकोडमध्ये सायबरपार्क उभे राहिले. केरळ स्टार्टअप मिशन नव्या कंपन्यांना पाठबळ देते, तर राज्याच्या मालकीचे के-फोन जाळे घरे आणि सरकारी कार्यालयांपर्यंत ब्रॉडबँड पोहोचवण्याचे उद्दिष्ट ठेवते. तिरुवनंतपुरममधील डिजिटल युनिव्हर्सिटी केरळ डिजिटल तंत्रज्ञानातील शिक्षण व संशोधनावर भर देते."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI Indian Telecom Services Performance Indicators (Kerala circle)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
        (L("K-FON connections", "के-फ़ोन कनेक्शन", "के-फोन जोडण्या"), "kl-gov", "K-FON official dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("KL", NAME)
module(R, "education", [
    prose("p1", L(
        "Keralam was the first State to approach universal literacy, and schooling is near-universal. In higher education, the 2021-22 AISHE survey counted 25 universities and 1,463 colleges, and a gross enrolment ratio (ages 18–23) of 41.3%, well above the national 28.4%. Women outnumber men in many colleges. The State hosts IIM Kozhikode, NIT Calicut, IIT Palakkad, IISER Thiruvananthapuram and the Indian Institute of Space Science and Technology.",
        "केरलम सार्वभौमिक साक्षरता के क़रीब पहुँचने वाला पहला राज्य था, और स्कूली शिक्षा लगभग सार्वभौमिक है। उच्च शिक्षा में 2021-22 के एआईएसएचई सर्वेक्षण में 25 विश्वविद्यालय और 1,463 कॉलेज गिने गए, और सकल नामांकन अनुपात (18–23 आयु) 41.3% था, जो राष्ट्रीय 28.4% से काफ़ी अधिक है। कई कॉलेजों में छात्राओं की संख्या छात्रों से अधिक है। राज्य में आईआईएम कोझिकोड, एनआईटी कालीकट, आईआईटी पालक्काड, आईसर तिरुवनंतपुरम और भारतीय अंतरिक्ष विज्ञान एवं प्रौद्योगिकी संस्थान हैं।",
        "सार्वत्रिक साक्षरतेच्या जवळ पोहोचणारे केरळम हे पहिले राज्य होते आणि शालेय शिक्षण जवळपास सार्वत्रिक आहे. उच्चशिक्षणात 2021-22 च्या एआयएसएचई सर्वेक्षणात 25 विद्यापीठे आणि 1,463 महाविद्यालये नोंदली गेली, आणि एकूण नोंदणी गुणोत्तर (18–23 वय) 41.3% होते — राष्ट्रीय 28.4% पेक्षा बरेच जास्त. अनेक महाविद्यालयांत विद्यार्थिनींची संख्या विद्यार्थ्यांपेक्षा जास्त आहे. राज्यात आयआयएम कोझिकोड, एनआयटी कालिकत, आयआयटी पालक्काड, आयसर तिरुवनंतपुरम आणि भारतीय अंतराळ विज्ञान व तंत्रज्ञान संस्था आहेत."),
        sources=["aishe"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("iimk", "IIM Kozhikode", "आईआईएम कोझिकोड", "आयआयएम कोझिकोड", m=("Kozhikode", "कोझिकोड", "कोझिकोड")),
        it3("nitc", "NIT Calicut", "एनआईटी कालीकट", "एनआयटी कालिकत", m=("Kozhikode", "कोझिकोड", "कोझिकोड")),
        it3("iitpkd", "IIT Palakkad", "आईआईटी पालक्काड", "आयआयटी पालक्काड", m=("Palakkad", "पालक्काड", "पालक्काड")),
        it3("iisertvm", "IISER Thiruvananthapuram", "आईसर तिरुवनंतपुरम", "आयसर तिरुवनंतपुरम", m=("Thiruvananthapuram", "तिरुवनंतपुरम", "तिरुवनंतपुरम")),
        it3("iist", "Indian Institute of Space Science and Technology", "भारतीय अंतरिक्ष विज्ञान एवं प्रौद्योगिकी संस्थान", "भारतीय अंतराळ विज्ञान व तंत्रज्ञान संस्था", m=("Thiruvananthapuram", "तिरुवनंतपुरम", "तिरुवनंतपुरम")),
        it3("cuk", "Central University of Kerala", "केरल केंद्रीय विश्वविद्यालय", "केरळ केंद्रीय विद्यापीठ", m=("Kasaragod", "कासरगोड", "कासारगोड")),
        it3("cusat", "Cochin University of Science and Technology", "कोचीन विज्ञान एवं प्रौद्योगिकी विश्वविद्यालय", "कोचीन विज्ञान व तंत्रज्ञान विद्यापीठ", m=("Kochi", "कोच्चि", "कोची")),
        it3("nuals", "National University of Advanced Legal Studies", "राष्ट्रीय उन्नत विधि अध्ययन विश्वविद्यालय", "राष्ट्रीय प्रगत विधी अभ्यास विद्यापीठ", m=("Kochi", "कोच्चि", "कोची")),
    ], title=L("National institutions (selected)", "राष्ट्रीय संस्थान (चयनित)", "राष्ट्रीय संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Dropout rates by level", "स्तरवार ड्रॉपआउट दर", "स्तरनिहाय गळती दर"), "udise", "UDISE+."),
        (L("Literacy by sex", "लिंगवार साक्षरता", "लिंगनिहाय साक्षरता"), "census", "Census 2011 PCA."),
        (L("NIRF-ranked institutions", "एनआईआरएफ़ रैंक वाले संस्थान", "एनआयआरएफ क्रमवारीतील संस्था"), "nirf", "Latest NIRF list filtered to Keralam."),
    ]),
])

# ---------------- O. Health ----------------
srs = NF["SRS_2021_PIB_PRID2128024"]
def srsdp(v, unit, period, note=None, level="state"):
    return dp(v, unit, period, "survey" if "-" in period else "calendar", "srs", SRS, note=note, level=level)
module(R, "health", [
    prose("p1", L(
        "Keralam has India's best mortality indicators. In the Sample Registration System for 2021, its under-five mortality was 8 per 1,000 live births and neonatal mortality 4, against 31 and 19 for India; maternal mortality was 20 per lakh live births in 2019-21, against 93 nationally. Almost all births (99.8% in NFHS-5) take place in health facilities.\n\nThe challenges now are those of an ageing, longer-living population: diabetes, hypertension, cancer and the cost of chronic care. NFHS-5 also recorded a rise in child stunting and underweight compared with NFHS-4, which the State will need to track.",
        "केरलम के मृत्यु दर संकेतक भारत में सबसे अच्छे हैं। 2021 की नमूना पंजीकरण प्रणाली में यहाँ पाँच वर्ष से कम आयु की मृत्यु दर प्रति 1,000 जीवित जन्म पर 8 और नवजात मृत्यु दर 4 थी, जबकि भारत में यह 31 और 19 थी; 2019-21 में मातृ मृत्यु अनुपात प्रति लाख जीवित जन्म पर 20 था, जबकि राष्ट्रीय स्तर पर 93। लगभग सभी प्रसव (एनएफ़एचएस-5 में 99.8%) स्वास्थ्य संस्थानों में होते हैं।\n\nअब चुनौतियाँ एक बुज़ुर्ग होती, लंबी उम्र वाली आबादी की हैं: मधुमेह, उच्च रक्तचाप, कैंसर और दीर्घकालिक देखभाल का खर्च। एनएफ़एचएस-5 में एनएफ़एचएस-4 की तुलना में बच्चों में ठिगनापन और कम वज़न भी बढ़ा दर्ज हुआ, जिस पर राज्य को नज़र रखनी होगी।",
        "भारतातील सर्वोत्तम मृत्युदर निर्देशक केरळमचे आहेत. 2021 च्या नमुना नोंदणी पद्धतीनुसार येथे पाच वर्षांखालील मृत्युदर दर 1,000 जिवंत जन्मांमागे 8 आणि नवजात मृत्युदर 4 होता, तर भारतासाठी तो 31 आणि 19 होता; 2019-21 मध्ये मातामृत्यू प्रमाण दर लाख जिवंत जन्मांमागे 20 होते, तर राष्ट्रीय प्रमाण 93. जवळपास सर्व प्रसूती (एनएफएचएस-5 मध्ये 99.8%) आरोग्य संस्थांत होतात.\n\nआता आव्हाने वृद्ध होत जाणाऱ्या, दीर्घायुषी लोकसंख्येची आहेत: मधुमेह, उच्च रक्तदाब, कर्करोग आणि दीर्घकालीन उपचारांचा खर्च. एनएफएचएस-4 च्या तुलनेत एनएफएचएस-5 मध्ये मुलांमधील खुजेपणा आणि कमी वजनाचे प्रमाण वाढल्याचेही नोंदले गेले, यावर राज्याला लक्ष ठेवावे लागेल."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("srs", [
        fact("mmr", L("Maternal mortality ratio", "मातृ मृत्यु अनुपात", "मातामृत्यू प्रमाण"), srsdp(srs["KL"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", "SRS special bulletin, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", level="national")),
        fact("u5mr", L("Under-five mortality rate", "पाँच वर्ष से कम आयु की मृत्यु दर", "पाच वर्षांखालील मृत्युदर"), srsdp(srs["KL"]["U5MR"], "per 1,000 live births", "2021", "SRS 2021, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["U5MR"], "per 1,000 live births", "2021", level="national")),
        fact("nmr", L("Neonatal mortality rate", "नवजात मृत्यु दर", "नवजात मृत्युदर"), srsdp(srs["KL"]["NMR"], "per 1,000 live births", "2021"), "number", "lower-is-better",
             national=srsdp(srs["IN"]["NMR"], "per 1,000 live births", "2021", level="national")),
    ], title=L("Mortality (Sample Registration System)", "मृत्यु दर (नमूना पंजीकरण प्रणाली)", "मृत्युदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("KL"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Infant mortality rate (State)", "शिशु मृत्यु दर (राज्य)", "अर्भक मृत्युदर (राज्य)"), "srs", "SRS Statistical Report 2021, Table on IMR by State."),
        (L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"), "srs", "SRS abridged life tables."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
        (L("Anaemia and immunisation", "एनीमिया और टीकाकरण", "रक्तक्षय व लसीकरण"), "nfhs", "NFHS-5 State fact sheet."),
    ]),
])
print("kl mod2 ok")
