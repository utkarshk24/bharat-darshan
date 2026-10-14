"""Gujarat modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-GJ"
ECI = "https://results.eci.gov.in/ResultAcGenDec2022/partywiseresult-S06.htm"
SER = "https://data.opencity.in/dataset/ac23cf45-bf10-4f17-b389-cb49c6c72fc6/resource/1704d67b-ca8d-4231-9540-389f7c8001ae/download/socioeconomicreview202223english27_02_23_10_14_25.pdf"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab82.pdf"
NOTE_GJ = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 14 Oct 2026. "
           "FY2025-26 is the latest year published for Gujarat and may be revised.")
mo = research("mospi_gj.json")
NAME = L("Gujarat", "गुजरात", "गुजरात")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Gujarati culture is shaped by trade, devotion and craft. The 15th-century poet-saint Narsinh Mehta is regarded as the first great poet of Gujarati, and his hymn 'Vaishnav Jan To' was a favourite of Gandhi. Jain, Vaishnava and Swaminarayan traditions are strong, as are Sufi shrines and the Parsi community that first landed at Sanjan. Garba and dandiya raas, danced in circles through the nine nights of Navratri, are the State's signature performing arts; bhavai is a traditional folk theatre.\n\nGujarat's textile crafts are among the richest in India: patola double-ikat silk from Patan, bandhani tie-dye from Jamnagar and Kutch, ajrakh block printing, Kutch and Suf embroidery, and the painted and printed Mata ni Pachhedi temple cloths. Rogan painting, Sankheda lacquered furniture and Pithora wall paintings by the Rathwa community are other well-known traditions.",
        "गुजराती संस्कृति व्यापार, भक्ति और शिल्प से बनी है। 15वीं सदी के संत-कवि नरसिंह मेहता गुजराती के पहले बड़े कवि माने जाते हैं, और उनका भजन 'वैष्णव जन तो' गांधी का प्रिय था। जैन, वैष्णव और स्वामीनारायण परंपराएँ मज़बूत हैं, और सूफ़ी दरगाहें और पारसी समुदाय भी, जो सबसे पहले संजाण में उतरा था। नवरात्रि की नौ रातों में घेरे में नाचे जाने वाले गरबा और डांडिया रास राज्य की पहचान वाली प्रदर्शन कलाएँ हैं; भवाई पारंपरिक लोक रंगमंच है।\n\nगुजरात के वस्त्र शिल्प भारत में सबसे समृद्ध में हैं: पाटन का पटोला डबल-इकत रेशम, जामनगर और कच्छ की बांधनी, अजरख ठप्पा छपाई, कच्छ और सूफ़ कढ़ाई, और चित्रित व छपे हुए माता नी पछेडी मंदिर वस्त्र। रोगन चित्रकला, संखेडा का लाख वाला फ़र्नीचर और राठवा समुदाय की पिथोरा भित्ति चित्रकला अन्य प्रसिद्ध परंपराएँ हैं।",
        "गुजराती संस्कृती व्यापार, भक्ती आणि हस्तकलेतून घडली आहे. पंधराव्या शतकातील संतकवी नरसिंह मेहता हे गुजरातीचे पहिले श्रेष्ठ कवी मानले जातात, आणि त्यांचे 'वैष्णव जन तो' हे भजन गांधींचे आवडते होते. जैन, वैष्णव व स्वामीनारायण परंपरा भक्कम आहेत, तसेच सुफी दर्गे आणि संजाण येथे प्रथम उतरलेला पारशी समुदायही. नवरात्रीच्या नऊ रात्री वर्तुळात खेळले जाणारे गरबा व दांडिया रास हे राज्याचे ओळखचिन्ह असलेले सादरीकरण प्रकार आहेत; भवाई हे पारंपरिक लोकनाट्य आहे.\n\nगुजरातची वस्त्रकला भारतातील सर्वांत समृद्ध कलांपैकी आहे: पाटणचा पटोला दुहेरी-इकत रेशीम, जामनगर व कच्छची बांधणी, अजरख ठसा छपाई, कच्छ व सूफ भरतकाम, आणि रंगवलेली व छापलेली माता नी पछेडी मंदिरवस्त्रे. रोगन चित्रकला, संखेडाचे लाखकाम केलेले फर्निचर आणि राठवा समुदायाची पिथोरा भित्तिचित्रकला या इतर प्रसिद्ध परंपरा आहेत."),
        conf="Editorial"),
    lst("festivals", [
        fest("navratri", "Navratri", "नवरात्रि", "नवरात्र", ("September–October", "सितंबर–अक्टूबर", "सप्टेंबर–ऑक्टोबर"),
             ("Nine nights of garba and dandiya across the State.", "पूरे राज्य में नौ रातों का गरबा और डांडिया।", "राज्यभर नऊ रात्री गरबा व दांडिया.")),
        fest("uttarayan", "Uttarayan (kite festival)", "उत्तरायण (पतंग उत्सव)", "उत्तरायण (पतंग महोत्सव)", ("14–15 January", "14–15 जनवरी", "14–15 जानेवारी"),
             ("Rooftop kite-flying; an international kite festival in Ahmedabad.", "छतों पर पतंगबाज़ी; अहमदाबाद में अंतरराष्ट्रीय पतंग उत्सव।", "गच्चीवरून पतंगबाजी; अहमदाबादमध्ये आंतरराष्ट्रीय पतंग महोत्सव.")),
        fest("rann", "Rann Utsav", "रण उत्सव", "रण उत्सव", ("November–February", "नवंबर–फ़रवरी", "नोव्हेंबर–फेब्रुवारी"),
             ("Tent city and culture on the white salt desert of Kutch.", "कच्छ के सफ़ेद नमक मरुस्थल पर तंबू नगरी और सांस्कृतिक कार्यक्रम।", "कच्छच्या पांढऱ्या मिठाच्या वाळवंटावर तंबूनगरी व सांस्कृतिक कार्यक्रम.")),
        fest("tarnetar", "Tarnetar fair", "तरणेतर मेला", "तरणेतर जत्रा", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Folk fair of Saurashtra with embroidered umbrellas and dances.", "कढ़ाईदार छतरियों और नृत्यों वाला सौराष्ट्र का लोक मेला।", "भरतकाम केलेल्या छत्र्या व नृत्यांसह सौराष्ट्राची लोकजत्रा.")),
        fest("janmashtami", "Janmashtami at Dwarka", "द्वारका में जन्माष्टमी", "द्वारकेत जन्माष्टमी", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Krishna's birth celebrated at the Dwarkadhish temple.", "द्वारकाधीश मंदिर में कृष्ण जन्मोत्सव।", "द्वारकाधीश मंदिरात कृष्णजन्मोत्सव.")),
        fest("eid", "Eid, Christmas and Navroz", "ईद, क्रिसमस और नवरोज़", "ईद, नाताळ व नवरोज", ("Various", "विभिन्न", "विविध"),
             ("Celebrated by Muslim, Christian and Parsi communities.", "मुस्लिम, ईसाई और पारसी समुदायों द्वारा मनाए जाते हैं।", "मुस्लिम, ख्रिश्चन व पारशी समुदाय साजरे करतात.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("garba", "Garba", "गरबा", "गरबा"), it3("dandiya", "Dandiya raas", "डांडिया रास", "दांडिया रास"), it3("bhavai", "Bhavai", "भवाई", "भवाई"),
        it3("patola", "Patola weaving", "पटोला बुनाई", "पटोला विणकाम"), it3("bandhani", "Bandhani", "बांधनी", "बांधणी"), it3("ajrakh", "Ajrakh printing", "अजरख छपाई", "अजरख छपाई"),
        it3("rogan", "Rogan painting", "रोगन चित्रकला", "रोगन चित्रकला"), it3("pithora", "Pithora painting", "पिथोरा चित्रकला", "पिथोरा चित्रकला"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("thali", "Gujarati thali", "गुजराती थाली", "गुजराती थाळी", d=("Dal, kadhi, vegetables, rotli, rice, farsan and a sweet — often lightly sweet overall.", "दाल, कढ़ी, सब्ज़ियाँ, रोटली, चावल, फरसाण और मिठाई — अक्सर हल्की मिठास के साथ।", "डाळ, कढी, भाज्या, पोळी, भात, फरसाण व गोड पदार्थ — अनेकदा किंचित गोडसर.")),
        it3("dhokla", "Dhokla and khandvi", "ढोकला और खांडवी", "ढोकळा व खांडवी", d=("Steamed gram-flour snacks.", "बेसन से बने भाप में पके नाश्ते।", "बेसनाचे वाफवलेले पदार्थ.")),
        it3("undhiyu", "Undhiyu", "उंधियू", "उंधियो", d=("Winter dish of mixed vegetables slow-cooked with spices, especially in Surat.", "मसालों के साथ धीमी आँच पर पकी मिली-जुली सब्ज़ियों का सर्दियों का व्यंजन, ख़ासकर सूरत में।", "मसाल्यांसह मंद आचेवर शिजवलेल्या मिश्र भाज्यांचा हिवाळी पदार्थ, विशेषतः सुरतमध्ये.")),
        it3("thepla", "Thepla and khakhra", "थेपला और खाखरा", "थेपला व खाकरा", d=("Spiced flatbreads that travel well.", "मसालेदार रोटियाँ, जो सफ़र में ख़राब नहीं होतीं।", "प्रवासात टिकणाऱ्या मसालेदार पोळ्या.")),
        it3("fafda", "Fafda–jalebi", "फाफड़ा–जलेबी", "फाफडा–जिलेबी", d=("Crisp gram-flour strips with jalebi, a Sunday and Dussehra favourite.", "जलेबी के साथ कुरकुरे बेसन के फाफड़े, रविवार और दशहरे का पसंदीदा।", "जिलेबीसोबत कुरकुरीत बेसनाचे फाफडे — रविवारी व दसऱ्याला आवडते.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("chaniya", "Chaniya choli", "चणिया चोली", "चणिया चोळी", d=("Flared skirt and blouse, often mirror-worked, worn for garba.", "घेरदार घाघरा और चोली, अक्सर शीशे के काम वाली, गरबा में पहनी जाती है।", "घेरदार घागरा व चोळी, अनेकदा आरसेकाम असलेली, गरब्याला घातली जाते.")),
        it3("kediyu", "Kediyu and chorno", "केडियू और चोरणो", "केडियू व चोरणो", d=("Pleated upper garment and trousers worn by men for dandiya.", "डांडिया में पुरुषों द्वारा पहना जाने वाला चुन्नटदार ऊपरी वस्त्र और पायजामा।", "दांडियाला पुरुष घालतात तो चुण्यांचा अंगरखा व विजार.")),
        it3("patola", "Patola saree", "पटोला साड़ी", "पटोला साडी", d=("Double-ikat silk from Patan, worn at weddings.", "पाटन का डबल-इकत रेशम, शादियों में पहना जाता है।", "पाटणचे दुहेरी-इकत रेशीम, लग्नात परिधान केले जाते.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
mfg = 100 * g["manufacturing"] / g["total"]
crops = table("crops", L("Agricultural production, 2021-22", "कृषि उत्पादन, 2021-22", "कृषी उत्पादन, 2021-22"),
              [col(L("Crop group", "फ़सल समूह", "पीकगट")), col(L("Production", "उत्पादन", "उत्पादन"), "right")],
              [[L("Foodgrains (lakh tonnes)", "खाद्यान्न (लाख टन)", "अन्नधान्य (लाख टन)"), "108.15"],
               [L("Oilseeds (lakh tonnes)", "तिलहन (लाख टन)", "तेलबिया (लाख टन)"), "70.72"],
               [L("Cotton (lakh bales of 170 kg)", "कपास (170 किग्रा की लाख गाँठें)", "कापूस (170 किलोच्या लाख गाठी)"), "73.88"]],
              "gj-des", SER, period="2021-22",
              note=L("Socio-Economic Review, Gujarat State 2022-23 (Directorate of Economics and Statistics).", "सामाजिक-आर्थिक समीक्षा, गुजरात राज्य 2022-23 (अर्थशास्त्र एवं सांख्यिकी निदेशालय)।", "सामाजिक-आर्थिक आढावा, गुजरात राज्य 2022-23 (अर्थशास्त्र व सांख्यिकी संचालनालय)."))
module(R, "economy", [
    prose("p1", L(
        f"Gujarat is one of India's most industrialised States. In the MoSPI series its GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26, and per capita NSDP was ₹{inr(pc['FY2025-26'][0])}. Manufacturing made up about {mfg:.0f}% of GSVA in FY2024-25 — the highest share among the large States — led by petroleum refining at Jamnagar, chemicals and petrochemicals along the 'golden corridor' from Vapi to Ahmedabad, pharmaceuticals, engineering, ceramics at Morbi, textiles, and the diamond-cutting and polishing industry of Surat.\n\nGujarat's ports — Deendayal (Kandla), Mundra, Pipavav, Hazira and others — handle more cargo than those of any other State. Agriculture is also important: the State is a leading producer of cotton, groundnut, castor, cumin and milk, home to the Amul co-operative model. The PLFS unemployment rate was 0.9% in 2025, well below the national level, and women's labour-force participation was 46.2%.",
        f"गुजरात भारत के सबसे औद्योगिक राज्यों में है। मोस्पी शृंखला में वित्त वर्ष 2025-26 में प्रचलित मूल्यों पर इसका जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2025-26'][0])} था। वित्त वर्ष 2024-25 में जीएसवीए में विनिर्माण का हिस्सा लगभग {mfg:.0f}% था — बड़े राज्यों में सबसे अधिक — जिसमें जामनगर में पेट्रोलियम शोधन, वापी से अहमदाबाद तक 'गोल्डन कॉरिडोर' पर रसायन और पेट्रोरसायन, दवाएँ, इंजीनियरिंग, मोरबी में सिरेमिक, कपड़ा, और सूरत का हीरा तराशी व पॉलिश उद्योग प्रमुख हैं।\n\nगुजरात के बंदरगाह — दीनदयाल (कांडला), मुंद्रा, पीपावाव, हज़ीरा और अन्य — किसी भी अन्य राज्य से अधिक माल संभालते हैं। कृषि भी महत्त्वपूर्ण है: राज्य कपास, मूँगफली, अरंडी, जीरा और दूध का प्रमुख उत्पादक है, और अमूल सहकारी मॉडल का घर है। 2025 में पीएलएफ़एस बेरोज़गारी दर 0.9% थी, जो राष्ट्रीय स्तर से काफ़ी कम है, और महिलाओं की श्रम बल भागीदारी 46.2% थी।",
        f"गुजरात हे भारतातील सर्वाधिक औद्योगिक राज्यांपैकी एक आहे. मोस्पी मालिकेनुसार आ.व. 2025-26 मध्ये चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी आणि दरडोई एनएसडीपी ₹{inr(pc['FY2025-26'][0])} होते. आ.व. 2024-25 मध्ये जीएसव्हीएमध्ये उत्पादन उद्योगाचा वाटा सुमारे {mfg:.0f}% होता — मोठ्या राज्यांत सर्वाधिक — ज्यात जामनगरमधील पेट्रोलियम शुद्धीकरण, वापी ते अहमदाबाद 'गोल्डन कॉरिडॉर' वरील रसायने व पेट्रोरसायने, औषधनिर्मिती, अभियांत्रिकी, मोरबीतील सिरॅमिक, कापड, आणि सुरतचा हिरे पैलू पाडणे व पॉलिश उद्योग आघाडीवर आहेत.\n\nगुजरातची बंदरे — दीनदयाळ (कांडला), मुंद्रा, पिपावाव, हजिरा व इतर — इतर कोणत्याही राज्यापेक्षा जास्त माल हाताळतात. शेतीही महत्त्वाची आहे: राज्य कापूस, भुईमूग, एरंड, जिरे व दुधाचे आघाडीचे उत्पादक असून अमूल सहकारी प्रारूपाचे घर आहे. 2025 मध्ये पीएलएफएस बेरोजगारी दर 0.9% होता — राष्ट्रीय पातळीपेक्षा बराच कमी — आणि स्त्रियांचा श्रमशक्ती सहभाग 46.2% होता."),
        sources=["mospi", "plfs", "gj-des"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_GJ), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_GJ), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_GJ), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("GJ", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    crops,
    plfs_series("GJ", NAME),
    lst("sectors-key", [
        it3("refining", "Refining and petrochemicals", "शोधन और पेट्रोरसायन", "तेलशुद्धीकरण व पेट्रोरसायने", d=("Jamnagar, Vadodara (Koyali), Hazira and Dahej.", "जामनगर, वडोदरा (कोयली), हज़ीरा और दहेज।", "जामनगर, वडोदरा (कोयली), हजिरा व दहेज.")),
        it3("chem", "Chemicals and pharmaceuticals", "रसायन और दवाएँ", "रसायने व औषधनिर्मिती", d=("Ankleshwar, Vapi, Bharuch and Ahmedabad.", "अंकलेश्वर, वापी, भरूच और अहमदाबाद।", "अंकलेश्वर, वापी, भरूच व अहमदाबाद.")),
        it3("diamonds", "Diamonds and textiles", "हीरे और कपड़ा", "हिरे व कापड", d=("Surat's diamond-cutting and synthetic-textile clusters.", "सूरत के हीरा तराशी और सिंथेटिक कपड़ा क्लस्टर।", "सुरतचे हिरे पैलू व कृत्रिम कापड समूह.")),
        it3("ceramics", "Ceramics and engineering", "सिरेमिक और इंजीनियरिंग", "सिरॅमिक व अभियांत्रिकी", d=("Morbi tiles; Rajkot engine parts and castings.", "मोरबी की टाइलें; राजकोट के इंजन पुर्ज़े और ढलाई।", "मोरबीच्या टाइल्स; राजकोटचे इंजिन भाग व ओतकाम.")),
        it3("ports", "Ports and logistics", "बंदरगाह और लॉजिस्टिक्स", "बंदरे व लॉजिस्टिक्स", d=("Deendayal (Kandla), Mundra, Pipavav, Hazira.", "दीनदयाल (कांडला), मुंद्रा, पीपावाव, हज़ीरा।", "दीनदयाळ (कांडला), मुंद्रा, पिपावाव, हजिरा.")),
        it3("dairy", "Dairy and agro-processing", "डेयरी और कृषि प्रसंस्करण", "दुग्धव्यवसाय व कृषिप्रक्रिया", d=("Amul and district milk unions; cotton ginning; groundnut oil.", "अमूल और ज़िला दुग्ध संघ; कपास ओटाई; मूँगफली तेल।", "अमूल व जिल्हा दूध संघ; कापूस जिनिंग; शेंगदाणा तेल.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Port cargo handled (latest year)", "बंदरगाहों द्वारा संभाला गया माल (नवीनतम वर्ष)", "बंदरांनी हाताळलेला माल (नवीनतम वर्ष)"), "india-gov", "Gujarat Maritime Board and Indian Ports Association."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("FDI equity inflows", "एफ़डीआई इक्विटी प्रवाह", "एफडीआय समभाग गुंतवणूक"), "dpiit", "DPIIT state-wise FDI factsheet."),
        (L("Milk production", "दुग्ध उत्पादन", "दूध उत्पादन"), "india-gov", "Basic Animal Husbandry Statistics."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Gujarat has a unicameral legislature: the 182-member Legislative Assembly meets in Gandhinagar. The State elects 26 members to the Lok Sabha and 11 to the Rajya Sabha.\n\nIn the December 2022 Assembly election the BJP won 156 seats, and Bhupendra Patel, Chief Minister since September 2021, was sworn in for a second term. Harsh Sanghavi became Deputy Chief Minister in the October 2025 reshuffle, and Shankar Chaudhary is Speaker. Acharya Devvrat has been Governor since July 2019. The next Assembly election is due in late 2027.",
        "गुजरात में एकसदनीय विधानमंडल है: 182 सदस्यों वाली विधानसभा गांधीनगर में बैठती है। राज्य से लोकसभा के 26 और राज्यसभा के 11 सदस्य चुने जाते हैं।\n\nदिसंबर 2022 के विधानसभा चुनाव में भाजपा ने 156 सीटें जीतीं, और सितंबर 2021 से मुख्यमंत्री भूपेंद्र पटेल ने दूसरे कार्यकाल की शपथ ली। अक्टूबर 2025 के फेरबदल में हर्ष संघवी उपमुख्यमंत्री बने, और शंकर चौधरी अध्यक्ष हैं। आचार्य देवव्रत जुलाई 2019 से राज्यपाल हैं। अगला विधानसभा चुनाव 2027 के अंत में होना है।",
        "गुजरातमध्ये एकसदनी विधिमंडळ आहे: 182 सदस्यांची विधानसभा गांधीनगर येथे भरते. राज्यातून लोकसभेवर 26 आणि राज्यसभेवर 11 सदस्य निवडले जातात.\n\nडिसेंबर 2022 च्या विधानसभा निवडणुकीत भाजपने 156 जागा जिंकल्या, आणि सप्टेंबर 2021 पासून मुख्यमंत्री असलेले भूपेंद्र पटेल यांनी दुसऱ्या कार्यकाळाची शपथ घेतली. ऑक्टोबर 2025 च्या फेरबदलात हर्ष संघवी उपमुख्यमंत्री झाले, आणि शंकर चौधरी अध्यक्ष आहेत. आचार्य देवव्रत जुलै 2019 पासून राज्यपाल आहेत. पुढील विधानसभा निवडणूक 2027 च्या अखेरीस होणार आहे."),
        sources=["eci", "newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    table("results", L("Legislative Assembly election, 2022 — seats won", "विधानसभा चुनाव, 2022 — जीती गई सीटें", "विधानसभा निवडणूक, 2022 — जिंकलेल्या जागा"),
          [col(L("Party", "दल", "पक्ष")), col(L("Seats", "सीटें", "जागा"), "right")],
          [["Bharatiya Janata Party (BJP)", 156], ["Indian National Congress (INC)", 17], ["Aam Aadmi Party (AAP)", 5],
           ["Samajwadi Party (SP)", 1], [L("Independents", "निर्दलीय", "अपक्ष"), 3], [L("Total", "कुल", "एकूण"), 182]],
          "eci", ECI, period="2022",
          note=L("Seats won as listed by the Election Commission (results declared 8 December 2022). Parties are shown by seats, without colours or commentary. By-elections and defections since 2022 have changed party strengths in the House.",
                 "चुनाव आयोग की सूची के अनुसार जीती गई सीटें (परिणाम 8 दिसंबर 2022 को घोषित)। दलों को सीटों के क्रम में, बिना रंग या टिप्पणी के दिखाया गया है। 2022 के बाद उपचुनावों और दलबदल से सदन में दलों की संख्या बदली है।",
                 "निवडणूक आयोगाच्या यादीनुसार जिंकलेल्या जागा (निकाल 8 डिसेंबर 2022 रोजी जाहीर). पक्ष जागांच्या क्रमाने, रंग किंवा भाष्याशिवाय दाखवले आहेत. 2022 नंतरच्या पोटनिवडणुका व पक्षांतरांमुळे सभागृहातील पक्षीय बळ बदलले आहे.")),
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("assembly", "Gujarat Legislative Assembly", "गुजरात विधानसभा", "गुजरात विधानसभा", url="https://gujaratassembly.gov.in", src="india-gov"),
        it3("portal", "Government of Gujarat", "गुजरात सरकार", "गुजरात शासन", url="https://gujaratindia.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Leader of Opposition — recognition status", "नेता प्रतिपक्ष — मान्यता की स्थिति", "विरोधी पक्षनेते — मान्यतेची स्थिती"), "india-gov", "Assembly secretariat; no party reached the 10% of seats usually required in 2022."),
        (L("Local bodies by type", "प्रकार के अनुसार स्थानीय निकाय", "प्रकारानुसार स्थानिक स्वराज्य संस्था"), "gj-des", "Panchayat and urban development departments."),
        (L("Current party strength in the Assembly", "विधानसभा में वर्तमान दलीय स्थिति", "विधानसभेतील सध्याचे पक्षीय बळ"), "india-gov", "Assembly secretariat member list."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Gujarat hosts several of India's largest new projects: most of the Mumbai–Ahmedabad high-speed rail line, the country's first commercial semiconductor fab at Dholera, a very large renewable-energy park at Khavda in Kutch, GIFT City's international financial services centre near Gandhinagar, and metro systems in Ahmedabad–Gandhinagar and Surat. Each card shows its source and the date it was checked.",
        "गुजरात में भारत की कई सबसे बड़ी नई परियोजनाएँ हैं: मुंबई–अहमदाबाद हाई-स्पीड रेल लाइन का अधिकांश हिस्सा, धोलेरा में देश का पहला वाणिज्यिक सेमीकंडक्टर फ़ैब, कच्छ के खावड़ा में बहुत बड़ा अक्षय ऊर्जा पार्क, गांधीनगर के पास गिफ़्ट सिटी का अंतरराष्ट्रीय वित्तीय सेवा केंद्र, और अहमदाबाद–गांधीनगर व सूरत में मेट्रो। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "गुजरातमध्ये भारतातील अनेक सर्वांत मोठे नवे प्रकल्प आहेत: मुंबई–अहमदाबाद अतिजलद रेल्वेमार्गाचा बहुतांश भाग, धोलेरा येथील देशातील पहिला व्यावसायिक सेमीकंडक्टर फॅब, कच्छमधील खावडा येथील प्रचंड अक्षय ऊर्जा उद्यान, गांधीनगरजवळील गिफ्ट सिटीचे आंतरराष्ट्रीय वित्तीय सेवा केंद्र, आणि अहमदाबाद–गांधीनगर व सुरत येथील मेट्रो. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pib", "pmindia"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Khavda renewable energy park — capacity commissioned", "खावड़ा अक्षय ऊर्जा पार्क — चालू क्षमता", "खावडा अक्षय ऊर्जा उद्यान — कार्यान्वित क्षमता"), "mnre", "MNRE / SECI status."),
        (L("Ahmedabad and Surat metro — official status", "अहमदाबाद और सूरत मेट्रो — आधिकारिक स्थिति", "अहमदाबाद व सुरत मेट्रो — अधिकृत स्थिती"), "india-gov", "GMRC project pages."),
        (L("Dholera semiconductor fab — production status", "धोलेरा सेमीकंडक्टर फ़ैब — उत्पादन की स्थिति", "धोलेरा सेमीकंडक्टर फॅब — उत्पादनाची स्थिती"), "india-gov", "India Semiconductor Mission update."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Gujarat's ports are its gateways: Deendayal Port at Kandla is a major port under the Union government, and Mundra, Pipavav, Hazira, Dahej and others are run privately or by the Gujarat Maritime Board. Ahmedabad's Sardar Vallabhbhai Patel International Airport is the busiest in the State, and Surat also has international flights; Vadodara, Rajkot, Bhuj, Jamnagar, Bhavnagar and Porbandar have domestic services. The Western Railway runs dense networks across the State, and the Western Dedicated Freight Corridor ends at the ports. Ahmedabad–Gandhinagar and Surat have metro lines, and Ahmedabad's BRTS was one of India's first bus-rapid-transit systems.",
        "गुजरात के बंदरगाह उसके प्रवेश द्वार हैं: कांडला का दीनदयाल पोर्ट केंद्र सरकार के अधीन प्रमुख बंदरगाह है, और मुंद्रा, पीपावाव, हज़ीरा, दहेज और अन्य निजी रूप से या गुजरात मैरीटाइम बोर्ड द्वारा चलाए जाते हैं। अहमदाबाद का सरदार वल्लभभाई पटेल अंतरराष्ट्रीय हवाई अड्डा राज्य का सबसे व्यस्त हवाई अड्डा है, और सूरत से भी अंतरराष्ट्रीय उड़ानें हैं; वडोदरा, राजकोट, भुज, जामनगर, भावनगर और पोरबंदर में घरेलू सेवाएँ हैं। पश्चिम रेलवे का घना नेटवर्क पूरे राज्य में है, और पश्चिमी समर्पित माल गलियारा बंदरगाहों तक जाता है। अहमदाबाद–गांधीनगर और सूरत में मेट्रो लाइनें हैं, और अहमदाबाद की बीआरटीएस भारत की पहली बस रैपिड ट्रांज़िट प्रणालियों में थी।",
        "गुजरातची बंदरे ही त्याची प्रवेशद्वारे आहेत: कांडलाचे दीनदयाळ बंदर हे केंद्र सरकारअंतर्गत प्रमुख बंदर आहे, तर मुंद्रा, पिपावाव, हजिरा, दहेज व इतर खासगी किंवा गुजरात मेरिटाइम बोर्डाकडून चालवली जातात. अहमदाबादचे सरदार वल्लभभाई पटेल आंतरराष्ट्रीय विमानतळ हे राज्यातील सर्वांत व्यस्त असून सुरतहूनही आंतरराष्ट्रीय उड्डाणे आहेत; वडोदरा, राजकोट, भुज, जामनगर, भावनगर व पोरबंदर येथे देशांतर्गत सेवा आहे. पश्चिम रेल्वेचे दाट जाळे राज्यभर आहे, आणि पश्चिम समर्पित मालवाहतूक मार्गिका बंदरांपर्यंत जाते. अहमदाबाद–गांधीनगर व सुरत येथे मेट्रो मार्गिका आहेत, आणि अहमदाबादची बीआरटीएस ही भारतातील पहिल्या बस रॅपिड ट्रान्झिट प्रणालींपैकी होती."),
        conf="Editorial"),
    lst("airports", [
        it3("amd", "Sardar Vallabhbhai Patel International Airport, Ahmedabad", "सरदार वल्लभभाई पटेल अंतरराष्ट्रीय हवाई अड्डा, अहमदाबाद", "सरदार वल्लभभाई पटेल आंतरराष्ट्रीय विमानतळ, अहमदाबाद", m=("AMD", "AMD", "AMD")),
        it3("stv", "Surat International Airport", "सूरत अंतरराष्ट्रीय हवाई अड्डा", "सुरत आंतरराष्ट्रीय विमानतळ", m=("STV", "STV", "STV")),
        it3("bdq", "Vadodara airport", "वडोदरा हवाई अड्डा", "वडोदरा विमानतळ"), it3("raj", "Rajkot (Hirasar) airport", "राजकोट (हीरासर) हवाई अड्डा", "राजकोट (हिरासर) विमानतळ"),
        it3("bhj", "Bhuj airport", "भुज हवाई अड्डा", "भुज विमानतळ"), it3("jga", "Jamnagar airport", "जामनगर हवाई अड्डा", "जामनगर विमानतळ"),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    lst("ports", [
        it3("kandla", "Deendayal Port (Kandla)", "दीनदयाल पोर्ट (कांडला)", "दीनदयाळ बंदर (कांडला)", m=("Major port", "प्रमुख बंदरगाह", "प्रमुख बंदर")),
        it3("mundra", "Mundra", "मुंद्रा", "मुंद्रा"), it3("pipavav", "Pipavav", "पीपावाव", "पिपावाव"), it3("hazira", "Hazira", "हज़ीरा", "हजिरा"), it3("dahej", "Dahej", "दहेज", "दहेज"),
    ], layout="chips", title=L("Ports (selected)", "बंदरगाह (चयनित)", "बंदरे (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Port and airport traffic", "बंदरगाह और हवाई अड्डा यातायात", "बंदर व विमानतळ वाहतूक"), "aai", "AAI statistics; Gujarat Maritime Board."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Gujarat is one of India's largest power producers. The State's Socio-Economic Review put installed capacity at 42,208 MW on 31 March 2022, second among the States, and Gujarat had 15.1% of the country's installed renewable capacity. Large coal and gas stations stand at Mundra, Wanakbori, Ukai and Gandhinagar; the Kakrapar atomic power station is near Surat. Wind farms run along the Kutch and Saurashtra coasts, solar parks include Charanka in Patan district, and the very large Khavda renewable park in the Rann of Kutch is being built in phases. Jamnagar hosts one of the world's largest refinery complexes.",
        "गुजरात भारत के सबसे बड़े बिजली उत्पादकों में है। राज्य की सामाजिक-आर्थिक समीक्षा के अनुसार 31 मार्च 2022 को स्थापित क्षमता 42,208 मेगावाट थी, जो राज्यों में दूसरे स्थान पर है, और देश की स्थापित अक्षय क्षमता का 15.1% गुजरात में था। बड़े कोयला और गैस संयंत्र मुंद्रा, वणाकबोरी, उकाई और गांधीनगर में हैं; काकरापार परमाणु बिजलीघर सूरत के पास है। कच्छ और सौराष्ट्र के तटों पर पवन फ़ार्म हैं, सौर पार्कों में पाटन ज़िले का चारणका शामिल है, और कच्छ के रण में बहुत बड़ा खावड़ा अक्षय पार्क चरणों में बन रहा है। जामनगर में दुनिया के सबसे बड़े रिफ़ाइनरी परिसरों में से एक है।",
        "गुजरात हे भारतातील सर्वांत मोठ्या वीज उत्पादकांपैकी एक आहे. राज्याच्या सामाजिक-आर्थिक आढाव्यानुसार 31 मार्च 2022 रोजी स्थापित क्षमता 42,208 मेगावॉट होती — राज्यांत दुसरी — आणि देशाच्या स्थापित अक्षय क्षमतेपैकी 15.1% गुजरातमध्ये होती. मोठी कोळसा व वायू केंद्रे मुंद्रा, वणाकबोरी, उकाई व गांधीनगर येथे आहेत; काक्रापार अणुऊर्जा केंद्र सुरतजवळ आहे. कच्छ व सौराष्ट्राच्या किनाऱ्यांवर पवनऊर्जा प्रकल्प आहेत, सौर उद्यानांत पाटण जिल्ह्यातील चारणका आहे, आणि कच्छच्या रणात प्रचंड खावडा अक्षय उद्यान टप्प्याटप्प्याने उभारले जात आहे. जामनगरमध्ये जगातील सर्वांत मोठ्या तेलशुद्धीकरण संकुलांपैकी एक आहे."),
        sources=["gj-des"], conf="Official"),
    facts("f", [
        fact("cap", L("Installed power capacity", "स्थापित बिजली क्षमता", "स्थापित वीज क्षमता"),
             dp(42208, "MW", "2022", "calendar", "gj-des", SER, note="As on 31 March 2022 (Socio-Economic Review, Gujarat State 2022-23)."), "number", "higher-is-better"),
        fact("reshare", L("Share of India's installed renewable capacity", "भारत की स्थापित अक्षय क्षमता में हिस्सा", "भारताच्या स्थापित अक्षय क्षमतेतील वाटा"),
             dp(15.10, "%", "2022", "calendar", "gj-des", SER, note="As of March 2022 (Socio-Economic Review, Gujarat State 2022-23)."), "percent"),
    ], title=L("Power capacity", "बिजली क्षमता", "वीज क्षमता")),
    gaps("g", [
        (L("Installed capacity by source, latest (CEA)", "स्रोतवार स्थापित क्षमता, नवीनतम (सीईए)", "स्रोतनिहाय स्थापित क्षमता, नवीनतम (सीईए)"), "cea", "CEA installed capacity report."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "GIFT City (Gujarat International Finance Tec-City) near Gandhinagar is a planned business district and India's international financial services centre (IFSC), with stock exchanges, banks and fund managers operating under a single regulator. Ahmedabad and Gandhinagar have growing IT and start-up clusters, and the State is promoting electronics and semiconductor manufacturing at Dholera and Sanand, where an assembly-and-test plant is being built alongside the fab.",
        "गांधीनगर के पास गिफ़्ट सिटी (गुजरात इंटरनेशनल फ़ाइनेंस टेक-सिटी) एक नियोजित व्यावसायिक क्षेत्र और भारत का अंतरराष्ट्रीय वित्तीय सेवा केंद्र (आईएफ़एससी) है, जहाँ शेयर बाज़ार, बैंक और फ़ंड प्रबंधक एक ही नियामक के अधीन काम करते हैं। अहमदाबाद और गांधीनगर में बढ़ते आईटी और स्टार्टअप केंद्र हैं, और राज्य धोलेरा और साणंद में इलेक्ट्रॉनिक्स और सेमीकंडक्टर विनिर्माण को बढ़ावा दे रहा है, जहाँ फ़ैब के साथ एक असेंबली-एवं-परीक्षण संयंत्र बन रहा है।",
        "गांधीनगरजवळील गिफ्ट सिटी (गुजरात इंटरनॅशनल फायनान्स टेक-सिटी) हे नियोजित व्यावसायिक क्षेत्र आणि भारताचे आंतरराष्ट्रीय वित्तीय सेवा केंद्र (आयएफएससी) आहे, जिथे शेअर बाजार, बँका व फंड व्यवस्थापक एकाच नियामकाखाली काम करतात. अहमदाबाद व गांधीनगरमध्ये वाढती आयटी व स्टार्टअप केंद्रे आहेत, आणि राज्य धोलेरा व साणंद येथे इलेक्ट्रॉनिक्स व सेमीकंडक्टर उत्पादनाला चालना देत आहे, जिथे फॅबसोबत जुळणी-व-चाचणी प्रकल्प उभारला जात आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Gujarat circle)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
        (L("GIFT City IFSC — entities and transactions", "गिफ़्ट सिटी आईएफ़एससी — संस्थाएँ और लेनदेन", "गिफ्ट सिटी आयएफएससी — संस्था व व्यवहार"), "india-gov", "IFSCA annual report."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("GJ", NAME)
module(R, "education", [
    prose("p1", L(
        "Gujarat had 91 universities and 2,395 colleges in the 2021-22 AISHE survey, but its higher-education gross enrolment ratio (ages 18–23) was 24.0%, below the national 28.4%, with a lower figure for women (22.7%) than for men (25.2%). Literacy at the 2011 Census was 78.0%.\n\nThe State has several national institutions: IIM Ahmedabad, IIT Gandhinagar, the National Institute of Design and CEPT University in Ahmedabad, the Physical Research Laboratory and ISRO's Space Applications Centre, SVNIT Surat, and the Maharaja Sayajirao University of Baroda.",
        "2021-22 के एआईएसएचई सर्वेक्षण में गुजरात में 91 विश्वविद्यालय और 2,395 कॉलेज थे, लेकिन उच्च शिक्षा का सकल नामांकन अनुपात (18–23 आयु) 24.0% था, जो राष्ट्रीय 28.4% से कम है, और महिलाओं (22.7%) का पुरुषों (25.2%) से कम। 2011 की जनगणना में साक्षरता 78.0% थी।\n\nराज्य में कई राष्ट्रीय संस्थान हैं: आईआईएम अहमदाबाद, आईआईटी गांधीनगर, अहमदाबाद में राष्ट्रीय डिज़ाइन संस्थान और सेप्ट विश्वविद्यालय, भौतिक अनुसंधान प्रयोगशाला और इसरो का अंतरिक्ष उपयोग केंद्र, एसवीएनआईटी सूरत, और महाराजा सयाजीराव विश्वविद्यालय बड़ौदा।",
        "2021-22 च्या एआयएसएचई सर्वेक्षणात गुजरातमध्ये 91 विद्यापीठे व 2,395 महाविद्यालये होती, पण उच्चशिक्षणाचे एकूण नोंदणी गुणोत्तर (18–23 वय) 24.0% होते — राष्ट्रीय 28.4% पेक्षा कमी — आणि स्त्रियांचे (22.7%) पुरुषांपेक्षा (25.2%) कमी. 2011 च्या जनगणनेत साक्षरता 78.0% होती.\n\nराज्यात अनेक राष्ट्रीय संस्था आहेत: आयआयएम अहमदाबाद, आयआयटी गांधीनगर, अहमदाबादमधील राष्ट्रीय डिझाइन संस्था व सेप्ट विद्यापीठ, भौतिक संशोधन प्रयोगशाळा व इस्रोचे अवकाश उपयोजन केंद्र, एसव्हीएनआयटी सुरत, आणि महाराजा सयाजीराव विद्यापीठ, बडोदा."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("iima", "IIM Ahmedabad", "आईआईएम अहमदाबाद", "आयआयएम अहमदाबाद", m=("Ahmedabad", "अहमदाबाद", "अहमदाबाद")),
        it3("iitgn", "IIT Gandhinagar", "आईआईटी गांधीनगर", "आयआयटी गांधीनगर", m=("Gandhinagar", "गांधीनगर", "गांधीनगर")),
        it3("nid", "National Institute of Design", "राष्ट्रीय डिज़ाइन संस्थान", "राष्ट्रीय डिझाइन संस्था", m=("Ahmedabad", "अहमदाबाद", "अहमदाबाद")),
        it3("prl", "Physical Research Laboratory", "भौतिक अनुसंधान प्रयोगशाला", "भौतिक संशोधन प्रयोगशाळा", m=("Ahmedabad", "अहमदाबाद", "अहमदाबाद")),
        it3("cept", "CEPT University", "सेप्ट विश्वविद्यालय", "सेप्ट विद्यापीठ", m=("Ahmedabad", "अहमदाबाद", "अहमदाबाद")),
        it3("svnit", "SVNIT Surat", "एसवीएनआईटी सूरत", "एसव्हीएनआयटी सुरत", m=("Surat", "सूरत", "सुरत")),
        it3("msu", "Maharaja Sayajirao University of Baroda", "महाराजा सयाजीराव विश्वविद्यालय, बड़ौदा", "महाराजा सयाजीराव विद्यापीठ, बडोदा", m=("Vadodara", "वडोदरा", "वडोदरा")),
    ], title=L("National institutions (selected)", "राष्ट्रीय संस्थान (चयनित)", "राष्ट्रीय संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Dropout rates by level", "स्तरवार ड्रॉपआउट दर", "स्तरनिहाय गळती दर"), "udise", "UDISE+."),
        (L("NIRF-ranked institutions", "एनआईआरएफ़ रैंक वाले संस्थान", "एनआयआरएफ क्रमवारीतील संस्था"), "nirf", "Latest NIRF list filtered to Gujarat."),
    ]),
])

# ---------------- O. Health ----------------
srs = NF["SRS_2021_PIB_PRID2128024"]
def srsdp(v, unit, period, note=None, level="state"):
    return dp(v, unit, period, "survey" if "-" in period else "calendar", "srs", SRS, note=note, level=level)
module(R, "health", [
    prose("p1", L(
        "Gujarat's mortality indicators are better than the national average: maternal mortality was 53 per lakh live births in 2019-21 (India 93) and under-five mortality 24 per 1,000 live births in 2021 (India 31), and about 94% of births took place in health facilities in NFHS-5. Child nutrition is a weak point: 39.0% of children under five were stunted and 25.1% wasted in NFHS-5, both above the national averages and little changed from NFHS-4.\n\nThe public system runs medical colleges in most districts, and Ahmedabad, Surat, Vadodara and Rajkot have large private hospitals. Life expectancy at birth was 69.9 years in 2014-18.",
        "गुजरात के मृत्यु संकेतक राष्ट्रीय औसत से बेहतर हैं: 2019-21 में मातृ मृत्यु अनुपात प्रति लाख जीवित जन्म पर 53 (भारत 93) और 2021 में पाँच वर्ष से कम आयु की मृत्यु दर प्रति 1,000 जीवित जन्म पर 24 (भारत 31) थी, और एनएफ़एचएस-5 में लगभग 94% प्रसव स्वास्थ्य संस्थानों में हुए। बाल पोषण कमज़ोर पक्ष है: एनएफ़एचएस-5 में पाँच वर्ष से कम आयु के 39.0% बच्चे ठिगने और 25.1% दुबले थे, दोनों राष्ट्रीय औसत से अधिक और एनएफ़एचएस-4 से लगभग अपरिवर्तित।\n\nसार्वजनिक व्यवस्था अधिकांश ज़िलों में मेडिकल कॉलेज चलाती है, और अहमदाबाद, सूरत, वडोदरा और राजकोट में बड़े निजी अस्पताल हैं। 2014-18 में जन्म के समय जीवन प्रत्याशा 69.9 वर्ष थी।",
        "गुजरातचे मृत्युदर निर्देशक राष्ट्रीय सरासरीपेक्षा चांगले आहेत: 2019-21 मध्ये मातामृत्यू प्रमाण दर लाख जिवंत जन्मांमागे 53 (भारत 93) आणि 2021 मध्ये पाच वर्षांखालील मृत्युदर दर 1,000 जिवंत जन्मांमागे 24 (भारत 31) होता, आणि एनएफएचएस-5 मध्ये सुमारे 94% प्रसूती आरोग्य संस्थांत झाल्या. बालपोषण ही कमकुवत बाजू आहे: एनएफएचएस-5 मध्ये पाच वर्षांखालील 39.0% मुले खुजी व 25.1% कृश होती — दोन्ही राष्ट्रीय सरासरीपेक्षा जास्त आणि एनएफएचएस-4 पासून जवळपास अपरिवर्तित.\n\nसार्वजनिक व्यवस्था बहुतेक जिल्ह्यांत वैद्यकीय महाविद्यालये चालवते, आणि अहमदाबाद, सुरत, वडोदरा व राजकोट येथे मोठी खासगी रुग्णालये आहेत. 2014-18 मध्ये जन्मतः आयुर्मान 69.9 वर्षे होते."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("mmr", L("Maternal mortality ratio", "मातृ मृत्यु अनुपात", "मातामृत्यू प्रमाण"), srsdp(srs["GJ"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", "SRS special bulletin, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", level="national")),
        fact("u5mr", L("Under-five mortality rate", "पाँच वर्ष से कम आयु की मृत्यु दर", "पाच वर्षांखालील मृत्युदर"), srsdp(srs["GJ"]["U5MR"], "per 1,000 live births", "2021", "SRS 2021, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["U5MR"], "per 1,000 live births", "2021", level="national")),
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(25, "per 1,000 live births", "2019", "calendar", "srs", ESI_VS, note="SRS 2019, Economic Survey 2021-22 Statistical Appendix Table 8.2 (48 in 2009)."), "number", "lower-is-better",
             previous=dp(48, "per 1,000 live births", "2009", "calendar", "srs", ESI_VS)),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(69.9, "years", "2014-18", "survey", "srs", ESI_LE, note="SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male 67.8, female 72.3)."), "number", "higher-is-better",
             national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality (Sample Registration System)", "मृत्यु दर (नमूना पंजीकरण प्रणाली)", "मृत्युदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("GJ"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Infant mortality rate, latest SRS year", "शिशु मृत्यु दर, नवीनतम एसआरएस वर्ष", "अर्भक मृत्युदर, नवीनतम एसआरएस वर्ष"), "srs", "SRS Statistical Report (latest)."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("gj mod2 ok")
