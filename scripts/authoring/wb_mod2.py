"""West Bengal modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-WB"
NOA_CM = "https://newsonair.gov.in/suvendu-adhikari-takes-oath-as-first-bjp-cm-of-west-bengal/"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab82.pdf"
NOTE_WB = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 14 Oct 2026. "
           "FY2025-26 is the latest year published for West Bengal and may be revised.")
mo = research("mospi_wb.json")
NAME = L("West Bengal", "पश्चिम बंगाल", "पश्चिम बंगाल")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Bengali literature, music and film have shaped modern Indian culture. Rabindranath Tagore's poems, songs (Rabindra Sangeet), plays and paintings are part of everyday life, and his songs are the national anthems of both India and Bangladesh. Kazi Nazrul Islam, Bankim Chandra, Sarat Chandra and Jibanananda Das are other great names. Kolkata was the birthplace of Indian cinema's art-film tradition through Satyajit Ray, Ritwik Ghatak and Mrinal Sen, and its theatre, little magazines and the annual Kolkata Book Fair remain lively.\n\nFolk traditions include the wandering Baul singers of Birbhum, the Chhau masked dance of Purulia, Gambhira of Malda and patachitra scroll painting with sung stories. Bishnupur's terracotta temples and baluchari silks, Shantipur and Dhaniakhali handloom saris, Krishnanagar clay dolls and the dokra metal casting of Bankura are well-known crafts.",
        "बांग्ला साहित्य, संगीत और सिनेमा ने आधुनिक भारतीय संस्कृति को आकार दिया है। रवींद्रनाथ टैगोर की कविताएँ, गीत (रवींद्र संगीत), नाटक और चित्र रोज़मर्रा के जीवन का हिस्सा हैं, और उनके गीत भारत और बांग्लादेश दोनों के राष्ट्रगान हैं। काज़ी नज़रुल इस्लाम, बंकिमचंद्र, शरतचंद्र और जीवनानंद दास अन्य बड़े नाम हैं। सत्यजीत राय, ऋत्विक घटक और मृणाल सेन के माध्यम से कोलकाता भारतीय सिनेमा की कला-फ़िल्म परंपरा का जन्मस्थान रहा, और इसका रंगमंच, लघु पत्रिकाएँ और वार्षिक कोलकाता पुस्तक मेला आज भी जीवंत हैं।\n\nलोक परंपराओं में बीरभूम के घुमंतू बाउल गायक, पुरुलिया का छऊ मुखौटा नृत्य, मालदा का गंभीरा और गाई जाने वाली कथाओं के साथ पटचित्र स्क्रॉल चित्रकला शामिल हैं। बिष्णुपुर के टेराकोटा मंदिर और बालूचरी रेशम, शांतिपुर और धनियाखाली की हथकरघा साड़ियाँ, कृष्णनगर की मिट्टी की गुड़ियाँ और बाँकुड़ा की डोकरा धातु ढलाई प्रसिद्ध शिल्प हैं।",
        "बांगला साहित्य, संगीत व चित्रपटांनी आधुनिक भारतीय संस्कृतीला आकार दिला आहे. रवींद्रनाथ टागोरांच्या कविता, गाणी (रवींद्र संगीत), नाटके व चित्रे रोजच्या जीवनाचा भाग आहेत, आणि त्यांची गाणी भारत व बांगलादेश दोघांची राष्ट्रगीते आहेत. काझी नजरुल इस्लाम, बंकिमचंद्र, शरच्चंद्र व जीवनानंद दास ही इतर मोठी नावे आहेत. सत्यजित राय, ऋत्विक घटक व मृणाल सेन यांच्यामुळे कोलकाता भारतीय चित्रपटसृष्टीतील कलात्मक चित्रपट परंपरेचे जन्मस्थान ठरले, आणि तिथली रंगभूमी, अनियतकालिके व वार्षिक कोलकाता पुस्तक मेळा आजही चैतन्यपूर्ण आहेत.\n\nलोकपरंपरांत बीरभूमचे भटके बाऊल गायक, पुरुलियाचे छाऊ मुखवटा नृत्य, मालदाचे गंभीरा आणि गायलेल्या कथांसह पटचित्र गुंडाळी चित्रकला यांचा समावेश आहे. बिष्णुपूरची टेराकोटा मंदिरे व बालुचरी रेशीम, शांतिपूर व धनियाखालीच्या हातमाग साड्या, कृष्णनगरच्या मातीच्या बाहुल्या आणि बांकुडाचे डोकरा धातू ओतकाम ही प्रसिद्ध हस्तकला आहे."),
        conf="Editorial"),
    lst("festivals", [
        fest("durgapuja", "Durga Puja", "दुर्गा पूजा", "दुर्गापूजा", ("September–October", "सितंबर–अक्टूबर", "सप्टेंबर–ऑक्टोबर"),
             ("The biggest festival: themed pandals, art and food across Kolkata and the State.", "सबसे बड़ा उत्सव: कोलकाता और पूरे राज्य में थीम वाले पंडाल, कला और भोजन।", "सर्वांत मोठा सण: कोलकाता व राज्यभर संकल्पनाधारित मंडप, कला व खाद्यपदार्थ.")),
        fest("kalipuja", "Kali Puja and Diwali", "काली पूजा और दीवाली", "कालीपूजा व दिवाळी", ("October–November", "अक्टूबर–नवंबर", "ऑक्टोबर–नोव्हेंबर"),
             ("Night worship of Kali with lamps and fireworks.", "दीपों और आतिशबाज़ी के साथ काली की रात्रि पूजा।", "दिवे व आतषबाजीसह कालीची रात्रीची पूजा.")),
        fest("poilabaisakh", "Poila Baisakh", "पोइला बैसाख", "पोइला बैशाख", ("14–15 April", "14–15 अप्रैल", "14–15 एप्रिल"),
             ("Bengali New Year; traders open new account books (haal khata).", "बांग्ला नववर्ष; व्यापारी नई बही (हाल खाता) खोलते हैं।", "बांगला नववर्ष; व्यापारी नवी खातेवही (हाल खाता) उघडतात.")),
        fest("saraswati", "Saraswati Puja", "सरस्वती पूजा", "सरस्वती पूजा", ("January–February", "जनवरी–फ़रवरी", "जानेवारी–फेब्रुवारी"),
             ("Worship of the goddess of learning in schools and homes.", "स्कूलों और घरों में विद्या की देवी की पूजा।", "शाळा व घरांत विद्येच्या देवतेची पूजा.")),
        fest("poushmela", "Poush Mela, Santiniketan", "पौष मेला, शांतिनिकेतन", "पौष मेळा, शांतिनिकेतन", ("December", "दिसंबर", "डिसेंबर"),
             ("Fair of folk music, Baul songs and crafts.", "लोक संगीत, बाउल गीतों और शिल्प का मेला।", "लोकसंगीत, बाऊल गीते व हस्तकलेची जत्रा.")),
        fest("eid", "Eid, Christmas and Buddha Purnima", "ईद, क्रिसमस और बुद्ध पूर्णिमा", "ईद, नाताळ व बुद्धपौर्णिमा", ("Various", "विभिन्न", "विविध"),
             ("Widely celebrated; Christmas lights on Park Street are a Kolkata tradition.", "व्यापक रूप से मनाए जाते हैं; पार्क स्ट्रीट की क्रिसमस रोशनी कोलकाता की परंपरा है।", "मोठ्या प्रमाणावर साजरे; पार्क स्ट्रीटवरील नाताळची रोषणाई ही कोलकात्याची परंपरा.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("rabindra", "Rabindra Sangeet", "रवींद्र संगीत", "रवींद्र संगीत"), it3("baul", "Baul", "बाउल", "बाऊल"), it3("chhau", "Purulia Chhau", "पुरुलिया छऊ", "पुरुलिया छाऊ"),
        it3("patachitra", "Patachitra", "पटचित्र", "पटचित्र"), it3("terracotta", "Terracotta", "टेराकोटा", "टेराकोटा"), it3("kantha", "Kantha embroidery", "कांथा कढ़ाई", "कांथा भरतकाम"),
        it3("dokra", "Dokra metal casting", "डोकरा धातु ढलाई", "डोकरा धातू ओतकाम"), it3("jatra", "Jatra theatre", "जात्रा रंगमंच", "जात्रा रंगभूमी"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("machh", "Machher jhol and rice", "माछेर झोल और भात", "माछेर झोल व भात", d=("Light fish curry, the everyday meal; hilsa (ilish) in mustard in the monsoon.", "हल्की मछली करी, रोज़ का भोजन; मानसून में सरसों वाली हिलसा (इलिश)।", "हलकी माशांची आमटी, रोजचे जेवण; पावसाळ्यात मोहरीतील हिलसा (इलिश).")),
        it3("rasgulla", "Rosogolla and sandesh", "रसगुल्ला और संदेश", "रसगुल्ला व संदेश", d=("Chhena sweets; Banglar Rasogolla is a registered GI.", "छेने की मिठाइयाँ; बंगाल का रसगुल्ला पंजीकृत जीआई है।", "छेन्याच्या मिठाया; बंगालचा रसगुल्ला नोंदणीकृत जीआय आहे.")),
        it3("mishtidoi", "Mishti doi", "मिष्टि दोई", "मिष्टी दोई", d=("Sweetened, caramelised yoghurt.", "मीठा, कैरामलाइज़्ड दही।", "गोड, करपवलेले दही.")),
        it3("kathi", "Kathi roll and phuchka", "काठी रोल और फुचका", "काठी रोल व फुचका", d=("Kolkata street food.", "कोलकाता का सड़क भोजन।", "कोलकात्याचे रस्त्यावरील खाद्य.")),
        it3("luchi", "Luchi and alur dom", "लुचि और आलूर दम", "लुची व आलूर दम", d=("Fried flatbreads with spiced potatoes, a festive breakfast.", "तली पूरियाँ मसालेदार आलू के साथ, त्योहार का नाश्ता।", "तळलेल्या पुऱ्या व मसालेदार बटाटे — सणाची न्याहारी.")),
        it3("momo", "Momos and thukpa", "मोमो और थुकपा", "मोमो व थुकपा", d=("Staples of the Darjeeling hills.", "दार्जिलिंग पहाड़ियों का मुख्य भोजन।", "दार्जिलिंगच्या डोंगराळ भागातील मुख्य पदार्थ.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("taant", "Taant and baluchari saris", "तांत और बालूचरी साड़ियाँ", "तांत व बालुचरी साड्या", d=("Cotton handloom for everyday wear; silk baluchari with woven scenes for occasions.", "रोज़ पहनने के लिए सूती हथकरघा; अवसरों के लिए बुने दृश्यों वाली रेशमी बालूचरी।", "रोजच्या वापरासाठी सुती हातमाग; समारंभासाठी विणलेल्या दृश्यांची रेशमी बालुचरी.")),
        it3("dhoti", "Dhoti and panjabi", "धोती और पंजाबी", "धोतर व पंजाबी", d=("Traditional men's dress for festivals.", "त्योहारों में पुरुषों की पारंपरिक पोशाक।", "सणासुदीला पुरुषांचा पारंपरिक पोशाख.")),
        it3("laalpaar", "Red-bordered white sari", "लाल किनारी वाली सफ़ेद साड़ी", "लाल काठाची पांढरी साडी", d=("Worn by women at Durga Puja.", "दुर्गा पूजा में महिलाएँ पहनती हैं।", "दुर्गापूजेला स्त्रिया परिधान करतात.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]
module(R, "economy", [
    prose("p1", L(
        f"West Bengal's GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26 in the MoSPI series, among the larger State economies, but per capita NSDP — ₹{inr(pc['FY2025-26'][0])} — is below the national average because of the State's large population. Agriculture, livestock and fishing made up about {agri:.0f}% of GSVA in FY2024-25, a large share: the State is one of India's leading producers of rice, jute, potatoes, vegetables and inland fish, and Darjeeling and the Dooars grow tea. Manufacturing was about {mfg:.0f}% — steel at Durgapur and Burnpur, engineering and jute mills along the Hooghly, petrochemicals at Haldia, and leather, gems and jewellery around Kolkata.\n\nServices dominate, led by trade, transport, finance and IT around Kolkata's Salt Lake and New Town. MSMEs and handicrafts employ many people. The PLFS unemployment rate was 2.8% in 2025, and women's labour-force participation was 37.5%.",
        f"मोस्पी शृंखला में वित्त वर्ष 2025-26 में पश्चिम बंगाल का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ था, जो बड़ी राज्य अर्थव्यवस्थाओं में है, लेकिन बड़ी आबादी के कारण प्रति व्यक्ति एनएसडीपी — ₹{inr(pc['FY2025-26'][0])} — राष्ट्रीय औसत से कम है। वित्त वर्ष 2024-25 में कृषि, पशुपालन और मत्स्य पालन जीएसवीए का लगभग {agri:.0f}% थे, जो बड़ा हिस्सा है: राज्य चावल, जूट, आलू, सब्ज़ियों और अंतर्देशीय मछली के भारत के प्रमुख उत्पादकों में है, और दार्जिलिंग व डुआर्स में चाय उगती है। विनिर्माण लगभग {mfg:.0f}% था — दुर्गापुर और बर्नपुर में इस्पात, हुगली के किनारे इंजीनियरिंग और जूट मिलें, हल्दिया में पेट्रोरसायन, और कोलकाता के आसपास चमड़ा, रत्न और आभूषण।\n\nसेवाएँ प्रमुख हैं — व्यापार, परिवहन, वित्त और कोलकाता के साल्ट लेक व न्यू टाउन में आईटी। एमएसएमई और हस्तशिल्प बहुत लोगों को रोज़गार देते हैं। 2025 में पीएलएफ़एस बेरोज़गारी दर 2.8% थी, और महिलाओं की श्रम बल भागीदारी 37.5% थी।",
        f"मोस्पी मालिकेनुसार आ.व. 2025-26 मध्ये पश्चिम बंगालचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी होते — मोठ्या राज्य अर्थव्यवस्थांपैकी — पण मोठ्या लोकसंख्येमुळे दरडोई एनएसडीपी — ₹{inr(pc['FY2025-26'][0])} — राष्ट्रीय सरासरीपेक्षा कमी आहे. आ.व. 2024-25 मध्ये शेती, पशुपालन व मत्स्यव्यवसायाचा जीएसव्हीएमध्ये सुमारे {agri:.0f}% वाटा होता, जो मोठा आहे: राज्य तांदूळ, ताग, बटाटे, भाज्या व गोड्या पाण्यातील माशांच्या आघाडीच्या उत्पादकांपैकी आहे, आणि दार्जिलिंग व डुआर्समध्ये चहा पिकतो. उत्पादन उद्योगाचा वाटा सुमारे {mfg:.0f}% होता — दुर्गापूर व बर्नपूरमध्ये पोलाद, हुगळीकाठी अभियांत्रिकी व तागाच्या गिरण्या, हल्दियात पेट्रोरसायने, आणि कोलकात्याभोवती चामडे, रत्ने व दागिने.\n\nसेवाक्षेत्राचे वर्चस्व आहे — व्यापार, वाहतूक, वित्त आणि कोलकात्याच्या सॉल्ट लेक व न्यू टाउनमधील आयटी. एमएसएमई व हस्तकला अनेकांना रोजगार देतात. 2025 मध्ये पीएलएफएस बेरोजगारी दर 2.8% होता, आणि स्त्रियांचा श्रमशक्ती सहभाग 37.5% होता."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_WB), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_WB), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_WB), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("WB", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    plfs_series("WB", NAME),
    lst("sectors-key", [
        it3("agri", "Rice, jute, potatoes and fish", "चावल, जूट, आलू और मछली", "तांदूळ, ताग, बटाटे व मासे", d=("Across the delta; jute in Nadia, Murshidabad and North 24 Parganas.", "पूरे डेल्टा में; नदिया, मुर्शिदाबाद और उत्तर 24 परगना में जूट।", "संपूर्ण त्रिभुज प्रदेशात; नदिया, मुर्शिदाबाद व उत्तर 24 परगण्यात ताग.")),
        it3("tea", "Tea", "चाय", "चहा", d=("Darjeeling, the Terai and the Dooars.", "दार्जिलिंग, तराई और डुआर्स।", "दार्जिलिंग, तराई व डुआर्स.")),
        it3("steel", "Steel and engineering", "इस्पात और इंजीनियरिंग", "पोलाद व अभियांत्रिकी", d=("Durgapur, Burnpur–Asansol and the Hooghly industrial belt.", "दुर्गापुर, बर्नपुर–आसनसोल और हुगली औद्योगिक पट्टी।", "दुर्गापूर, बर्नपूर–आसनसोल व हुगळी औद्योगिक पट्टा.")),
        it3("petro", "Petrochemicals and port", "पेट्रोरसायन और बंदरगाह", "पेट्रोरसायने व बंदर", d=("Haldia.", "हल्दिया।", "हल्दिया.")),
        it3("it", "IT and services", "आईटी और सेवाएँ", "आयटी व सेवा", d=("Salt Lake Sector V and New Town, Kolkata.", "साल्ट लेक सेक्टर V और न्यू टाउन, कोलकाता।", "सॉल्ट लेक सेक्टर V व न्यू टाउन, कोलकाता.")),
        it3("leather", "Leather, gems and jewellery", "चमड़ा, रत्न और आभूषण", "चामडे, रत्ने व दागिने", d=("Kolkata Leather Complex at Bantala; jewellery workshops.", "बानतला में कोलकाता लेदर कॉम्प्लेक्स; आभूषण कार्यशालाएँ।", "बानतला येथील कोलकाता लेदर कॉम्प्लेक्स; दागिन्यांच्या कार्यशाळा.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Crop production (rice, jute, potato)", "फ़सल उत्पादन (चावल, जूट, आलू)", "पीक उत्पादन (तांदूळ, ताग, बटाटा)"), "india-gov", "State agriculture department / Economic Review of West Bengal."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("FDI equity inflows", "एफ़डीआई इक्विटी प्रवाह", "एफडीआय समभाग गुंतवणूक"), "dpiit", "DPIIT state-wise FDI factsheet."),
        (L("Tea production", "चाय उत्पादन", "चहा उत्पादन"), "india-gov", "Tea Board of India statistics."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "West Bengal has a unicameral legislature: the 294-member Legislative Assembly meets in Kolkata. The State elects 42 members to the Lok Sabha and 16 to the Rajya Sabha.\n\nIn the Assembly election held in April 2026, the BJP won a majority — 207 of 294 seats as reported by News On AIR on 9 May, with the Trinamool Congress at 80. Suvendu Adhikari was sworn in as Chief Minister on 9 May 2026 by Governor R. N. Ravi, who had moved to the State from Tamil Nadu in March 2026. Rathindra Bose of the BJP was elected Speaker. The Trinamool legislature party later split, and the recognition of the Leader of Opposition should be checked against the Assembly's records.",
        "पश्चिम बंगाल में एकसदनीय विधानमंडल है: 294 सदस्यों वाली विधानसभा कोलकाता में बैठती है। राज्य से लोकसभा के 42 और राज्यसभा के 16 सदस्य चुने जाते हैं।\n\nअप्रैल 2026 में हुए विधानसभा चुनाव में भाजपा को बहुमत मिला — न्यूज़ ऑन एआईआर की 9 मई की रिपोर्ट के अनुसार 294 में से 207 सीटें, और तृणमूल कांग्रेस को 80। राज्यपाल आर. एन. रवि ने, जो मार्च 2026 में तमिलनाडु से इस राज्य में आए थे, 9 मई 2026 को शुभेंदु अधिकारी को मुख्यमंत्री पद की शपथ दिलाई। भाजपा के रथींद्र बोस अध्यक्ष चुने गए। बाद में तृणमूल विधायक दल में विभाजन हुआ, और नेता प्रतिपक्ष की मान्यता विधानसभा के अभिलेखों से जाँची जानी चाहिए।",
        "पश्चिम बंगालमध्ये एकसदनी विधिमंडळ आहे: 294 सदस्यांची विधानसभा कोलकात्यात भरते. राज्यातून लोकसभेवर 42 आणि राज्यसभेवर 16 सदस्य निवडले जातात.\n\nएप्रिल 2026 मध्ये झालेल्या विधानसभा निवडणुकीत भाजपला बहुमत मिळाले — न्यूज ऑन एआयआरच्या 9 मेच्या वृत्तानुसार 294 पैकी 207 जागा, तर तृणमूल काँग्रेसला 80. मार्च 2026 मध्ये तमिळनाडूहून या राज्यात आलेले राज्यपाल आर. एन. रवी यांनी 9 मे 2026 रोजी शुभेंदू अधिकारी यांना मुख्यमंत्रिपदाची शपथ दिली. भाजपचे रथींद्र बोस अध्यक्षपदी निवडले गेले. नंतर तृणमूल विधिमंडळ पक्षात फूट पडली, आणि विरोधी पक्षनेत्यांची मान्यता विधानसभेच्या नोंदींवरून तपासली पाहिजे."),
        sources=["newsonair", "pioneer"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("assembly", "West Bengal Legislative Assembly", "पश्चिम बंगाल विधानसभा", "पश्चिम बंगाल विधानसभा", url="https://wbassembly.gov.in", src="india-gov"),
        it3("portal", "Government of West Bengal", "पश्चिम बंगाल सरकार", "पश्चिम बंगाल शासन", url="https://wb.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2026 Assembly election — full party-wise result", "2026 विधानसभा चुनाव — दलवार पूरा परिणाम", "2026 विधानसभा निवडणूक — पक्षनिहाय संपूर्ण निकाल"), "eci", "ECI statistical report or Form-20; the results website builds its table in the browser and could not be read here."),
        (L("Leader of Opposition — official recognition", "नेता प्रतिपक्ष — आधिकारिक मान्यता", "विरोधी पक्षनेते — अधिकृत मान्यता"), "india-gov", "Assembly secretariat notice (the Trinamool legislature party split in 2026)."),
        (L("Local bodies by type", "प्रकार के अनुसार स्थानीय निकाय", "प्रकारानुसार स्थानिक स्वराज्य संस्था"), "india-gov", "Panchayats and Municipal Affairs departments."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Kolkata had India's first metro (1984) and its first under-river metro tunnel, below the Hooghly between Howrah and Esplanade, opened in 2024. New metro stretches to the airport and in the east of the city opened in August 2025, and the Kona Expressway elevated corridor linking Howrah and Kolkata is under way. Each card shows its source and the date it was checked.",
        "कोलकाता में भारत की पहली मेट्रो (1984) थी, और हावड़ा व एस्प्लेनेड के बीच हुगली के नीचे उसकी पहली नदी-तल मेट्रो सुरंग 2024 में खुली। हवाई अड्डे तक और शहर के पूर्व में नए मेट्रो खंड अगस्त 2025 में खुले, और हावड़ा व कोलकाता को जोड़ने वाले कोना एक्सप्रेसवे एलिवेटेड कॉरिडोर का काम चल रहा है। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "कोलकात्यात भारतातील पहिली मेट्रो (1984) होती, आणि हावडा व एस्प्लनेडदरम्यान हुगळीखालचा पहिला नदीतळ मेट्रो बोगदा 2024 मध्ये सुरू झाला. विमानतळापर्यंत व शहराच्या पूर्व भागात नवे मेट्रो टप्पे ऑगस्ट 2025 मध्ये सुरू झाले, आणि हावडा व कोलकात्याला जोडणाऱ्या कोना द्रुतगती मार्गावरील उन्नत मार्गिकेचे काम सुरू आहे. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pib"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Tajpur deep-sea port — status", "ताजपुर गहरे समुद्र का बंदरगाह — स्थिति", "ताजपूर खोल समुद्री बंदर — स्थिती"), "india-gov", "Official status from the State or the Ministry of Ports."),
        (L("Purulia pumped-storage and new power projects", "पुरुलिया पंप्ड-स्टोरेज और नई बिजली परियोजनाएँ", "पुरुलिया पंप्ड-स्टोरेज व नवे वीज प्रकल्प"), "cea", "CEA / State power department."),
        (L("New State government's flagship programmes", "नई राज्य सरकार के प्रमुख कार्यक्रम", "नव्या राज्य सरकारचे प्रमुख कार्यक्रम"), "india-gov", "List with official scheme pages once published."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Kolkata is the transport hub of eastern India. Netaji Subhas Chandra Bose International Airport links the city to South-East Asia and the Gulf, and Bagdogra near Siliguri serves the hills, Sikkim and the North-East; Durgapur (Kazi Nazrul Islam Airport) and Cooch Behar have smaller airports. Howrah and Sealdah are among the busiest railway stations in India, and Kolkata is the headquarters of the Eastern and South Eastern Railways and of the Metro Railway. The Syama Prasad Mookerjee Port has docks at Kolkata and Haldia. Siliguri, on the narrow 'Chicken's Neck' corridor, links mainland India with the North-East. The Darjeeling Himalayan Railway's toy train still climbs to Darjeeling.",
        "कोलकाता पूर्वी भारत का परिवहन केंद्र है। नेताजी सुभाष चंद्र बोस अंतरराष्ट्रीय हवाई अड्डा शहर को दक्षिण-पूर्व एशिया और खाड़ी से जोड़ता है, और सिलीगुड़ी के पास बागडोगरा पहाड़ियों, सिक्किम और पूर्वोत्तर को सेवा देता है; दुर्गापुर (काज़ी नज़रुल इस्लाम हवाई अड्डा) और कूचबिहार में छोटे हवाई अड्डे हैं। हावड़ा और सियालदह भारत के सबसे व्यस्त रेलवे स्टेशनों में हैं, और कोलकाता पूर्व रेलवे, दक्षिण पूर्व रेलवे और मेट्रो रेलवे का मुख्यालय है। श्यामा प्रसाद मुखर्जी पोर्ट की गोदियाँ कोलकाता और हल्दिया में हैं। संकरे 'चिकन्स नेक' गलियारे पर स्थित सिलीगुड़ी मुख्य भूमि भारत को पूर्वोत्तर से जोड़ता है। दार्जिलिंग हिमालयन रेलवे की टॉय ट्रेन आज भी दार्जिलिंग तक चढ़ती है।",
        "कोलकाता हे पूर्व भारताचे वाहतूक केंद्र आहे. नेताजी सुभाषचंद्र बोस आंतरराष्ट्रीय विमानतळ शहराला आग्नेय आशिया व आखाती देशांशी जोडते, आणि सिलिगुडीजवळील बागडोगरा डोंगराळ भाग, सिक्कीम व ईशान्य भारताला सेवा देते; दुर्गापूर (काझी नजरुल इस्लाम विमानतळ) व कूचबिहार येथे लहान विमानतळ आहेत. हावडा व सियालदह ही भारतातील सर्वांत व्यस्त रेल्वे स्थानकांपैकी आहेत, आणि कोलकाता पूर्व रेल्वे, दक्षिण पूर्व रेल्वे व मेट्रो रेल्वेचे मुख्यालय आहे. श्यामाप्रसाद मुखर्जी बंदराच्या गोद्या कोलकाता व हल्दिया येथे आहेत. अरुंद 'चिकन्स नेक' मार्गिकेवरील सिलिगुडी मुख्य भारताला ईशान्येशी जोडते. दार्जिलिंग हिमालयन रेल्वेची टॉय ट्रेन आजही दार्जिलिंगपर्यंत चढते."),
        conf="Editorial"),
    lst("airports", [
        it3("ccu", "Netaji Subhas Chandra Bose International Airport, Kolkata", "नेताजी सुभाष चंद्र बोस अंतरराष्ट्रीय हवाई अड्डा, कोलकाता", "नेताजी सुभाषचंद्र बोस आंतरराष्ट्रीय विमानतळ, कोलकाता", m=("CCU", "CCU", "CCU")),
        it3("ixb", "Bagdogra airport", "बागडोगरा हवाई अड्डा", "बागडोगरा विमानतळ", m=("IXB", "IXB", "IXB")),
        it3("rdp", "Kazi Nazrul Islam Airport, Durgapur", "काज़ी नज़रुल इस्लाम हवाई अड्डा, दुर्गापुर", "काझी नजरुल इस्लाम विमानतळ, दुर्गापूर"),
        it3("coh", "Cooch Behar airport", "कूचबिहार हवाई अड्डा", "कूचबिहार विमानतळ"),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Kolkata Metro operational length (official)", "कोलकाता मेट्रो की चालू लंबाई (आधिकारिक)", "कोलकाता मेट्रोची कार्यरत लांबी (अधिकृत)"), "railways", "Metro Railway Kolkata."),
        (L("Port and airport traffic", "बंदरगाह और हवाई अड्डा यातायात", "बंदर व विमानतळ वाहतूक"), "aai", "AAI statistics; Indian Ports Association."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Most of West Bengal's electricity comes from coal, mined in the Raniganj coalfield and brought from neighbouring Jharkhand. Major stations include NTPC Farakka, the State's Kolaghat, Bakreshwar, Sagardighi and Santaldih plants, the Damodar Valley Corporation's stations at Mejia and Durgapur, and private plants serving Kolkata. Hydro-electric stations in the Darjeeling hills and on the Teesta, and the Purulia pumped-storage project, provide peaking power, and rooftop and canal-top solar are growing.",
        "पश्चिम बंगाल की अधिकांश बिजली कोयले से आती है, जो रानीगंज कोयला क्षेत्र से निकाला जाता है और पड़ोसी झारखंड से आता है। प्रमुख संयंत्रों में एनटीपीसी फ़रक्का, राज्य के कोलाघाट, बक्रेश्वर, सागरदीघी और संतालडीह संयंत्र, मेजिया और दुर्गापुर में दामोदर घाटी निगम के संयंत्र, और कोलकाता को बिजली देने वाले निजी संयंत्र शामिल हैं। दार्जिलिंग पहाड़ियों और तीस्ता पर जलविद्युत केंद्र और पुरुलिया पंप्ड-स्टोरेज परियोजना पीक समय की बिजली देते हैं, और छतों और नहरों पर सौर ऊर्जा बढ़ रही है।",
        "पश्चिम बंगालची बहुतांश वीज कोळशापासून येते — राणीगंज कोळसा क्षेत्रातून खणलेला व शेजारच्या झारखंडमधून येणारा. प्रमुख केंद्रांत एनटीपीसी फरक्का, राज्याची कोलाघाट, बक्रेश्वर, सागरदिघी व संतालडीह केंद्रे, मेजिया व दुर्गापूर येथील दामोदर खोरे महामंडळाची केंद्रे, आणि कोलकात्याला वीज पुरवणारी खासगी केंद्रे यांचा समावेश आहे. दार्जिलिंगच्या डोंगरांतील व तिस्तावरील जलविद्युत केंद्रे आणि पुरुलिया पंप्ड-स्टोरेज प्रकल्प कमाल मागणीच्या वेळी वीज देतात, आणि छतावरील व कालव्यावरील सौरऊर्जा वाढत आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Renewable capacity", "अक्षय ऊर्जा क्षमता", "अक्षय ऊर्जा क्षमता"), "mnre", "MNRE state-wise RE capacity."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Kolkata's IT industry is concentrated in Salt Lake Sector V and New Town (Rajarhat), where major Indian and global IT services firms have large campuses. The city also has a growing start-up and fintech community, research institutions such as the Indian Statistical Institute, and an undersea-cable landing and data-centre cluster serving eastern India.",
        "कोलकाता का आईटी उद्योग साल्ट लेक सेक्टर V और न्यू टाउन (राजारहाट) में केंद्रित है, जहाँ बड़ी भारतीय और वैश्विक आईटी सेवा कंपनियों के बड़े परिसर हैं। शहर में बढ़ता स्टार्टअप और फ़िनटेक समुदाय, भारतीय सांख्यिकी संस्थान जैसे शोध संस्थान, और पूर्वी भारत को सेवा देने वाला समुद्री केबल लैंडिंग और डेटा सेंटर क्लस्टर भी है।",
        "कोलकात्याचा आयटी उद्योग सॉल्ट लेक सेक्टर V व न्यू टाउन (राजारहाट) येथे एकवटला आहे, जिथे मोठ्या भारतीय व जागतिक आयटी सेवा कंपन्यांची मोठी संकुले आहेत. शहरात वाढता स्टार्टअप व फिनटेक समुदाय, भारतीय सांख्यिकी संस्थेसारख्या संशोधन संस्था, आणि पूर्व भारताला सेवा देणारे समुद्री केबल लँडिंग व डेटा सेंटर समूहही आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Kolkata and West Bengal circles)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
        (L("IT/ITeS exports", "आईटी/आईटीईएस निर्यात", "आयटी/आयटीईएस निर्यात"), "india-gov", "STPI Kolkata."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("WB", NAME)
module(R, "education", [
    prose("p1", L(
        "West Bengal's higher-education gross enrolment ratio (ages 18–23) was 26.3% in 2021-22 in AISHE, up from 21.3% the year before but below the national 28.4%; women's GER (26.8%) was slightly above men's (25.9%). The State had 58 universities and 1,514 colleges. Literacy at the 2011 Census was 76.3%.\n\nKolkata has some of India's oldest modern institutions — the University of Calcutta (1857), Presidency University (founded as Hindu College in 1817), Jadavpur University and the Asiatic Society — together with the Indian Statistical Institute, IIM Calcutta, IISER Kolkata, the Bose Institute and the Saha Institute of Nuclear Physics. IIT Kharagpur, the first IIT (1951), and Tagore's Visva-Bharati at Santiniketan are elsewhere in the State.",
        "एआईएसएचई के अनुसार 2021-22 में पश्चिम बंगाल का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) 26.3% था, जो पिछले वर्ष के 21.3% से अधिक पर राष्ट्रीय 28.4% से कम है; महिलाओं का जीईआर (26.8%) पुरुषों (25.9%) से थोड़ा अधिक था। राज्य में 58 विश्वविद्यालय और 1,514 कॉलेज थे। 2011 की जनगणना में साक्षरता 76.3% थी।\n\nकोलकाता में भारत के कुछ सबसे पुराने आधुनिक संस्थान हैं — कलकत्ता विश्वविद्यालय (1857), प्रेसिडेंसी विश्वविद्यालय (1817 में हिंदू कॉलेज के रूप में स्थापित), जादवपुर विश्वविद्यालय और एशियाटिक सोसाइटी — साथ में भारतीय सांख्यिकी संस्थान, आईआईएम कलकत्ता, आईआईएसईआर कोलकाता, बोस संस्थान और साहा परमाणु भौतिकी संस्थान। पहला आईआईटी (1951), आईआईटी खड़गपुर, और शांतिनिकेतन में टैगोर का विश्व-भारती राज्य के अन्य हिस्सों में हैं।",
        "एआयएसएचईनुसार 2021-22 मध्ये पश्चिम बंगालचे उच्चशिक्षणातील एकूण नोंदणी गुणोत्तर (18–23 वय) 26.3% होते — मागील वर्षीच्या 21.3% पेक्षा जास्त पण राष्ट्रीय 28.4% पेक्षा कमी; स्त्रियांचे जीईआर (26.8%) पुरुषांपेक्षा (25.9%) किंचित जास्त होते. राज्यात 58 विद्यापीठे व 1,514 महाविद्यालये होती. 2011 च्या जनगणनेत साक्षरता 76.3% होती.\n\nकोलकात्यात भारतातील काही सर्वांत जुन्या आधुनिक संस्था आहेत — कलकत्ता विद्यापीठ (1857), प्रेसिडेन्सी विद्यापीठ (1817 मध्ये हिंदू कॉलेज म्हणून स्थापन), जादवपूर विद्यापीठ व एशियाटिक सोसायटी — सोबत भारतीय सांख्यिकी संस्था, आयआयएम कलकत्ता, आयसर कोलकाता, बोस संस्था व साहा अणुभौतिकी संस्था. पहिले आयआयटी (1951), आयआयटी खरगपूर, आणि शांतिनिकेतनमधील टागोरांचे विश्वभारती राज्याच्या इतर भागांत आहेत."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("iitkgp", "IIT Kharagpur", "आईआईटी खड़गपुर", "आयआयटी खरगपूर", m=("Kharagpur, 1951", "खड़गपुर, 1951", "खरगपूर, 1951")),
        it3("cu", "University of Calcutta", "कलकत्ता विश्वविद्यालय", "कलकत्ता विद्यापीठ", m=("Kolkata, 1857", "कोलकाता, 1857", "कोलकाता, 1857")),
        it3("isi", "Indian Statistical Institute", "भारतीय सांख्यिकी संस्थान", "भारतीय सांख्यिकी संस्था", m=("Kolkata", "कोलकाता", "कोलकाता")),
        it3("iimc", "IIM Calcutta", "आईआईएम कलकत्ता", "आयआयएम कलकत्ता", m=("Kolkata", "कोलकाता", "कोलकाता")),
        it3("ju", "Jadavpur University", "जादवपुर विश्वविद्यालय", "जादवपूर विद्यापीठ", m=("Kolkata", "कोलकाता", "कोलकाता")),
        it3("iiserk", "IISER Kolkata", "आईआईएसईआर कोलकाता", "आयसर कोलकाता", m=("Mohanpur", "मोहनपुर", "मोहनपूर")),
        it3("vb", "Visva-Bharati", "विश्व-भारती", "विश्वभारती", m=("Santiniketan", "शांतिनिकेतन", "शांतिनिकेतन")),
    ], title=L("National institutions (selected)", "राष्ट्रीय संस्थान (चयनित)", "राष्ट्रीय संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Dropout rates by level", "स्तरवार ड्रॉपआउट दर", "स्तरनिहाय गळती दर"), "udise", "UDISE+."),
        (L("NIRF-ranked institutions", "एनआईआरएफ़ रैंक वाले संस्थान", "एनआयआरएफ क्रमवारीतील संस्था"), "nirf", "Latest NIRF list filtered to West Bengal."),
    ]),
])

# ---------------- O. Health ----------------
srs = NF["SRS_2021_PIB_PRID2128024"]
def srsdp(v, unit, period, note=None, level="state"):
    return dp(v, unit, period, "survey" if "-" in period else "calendar", "srs", SRS, note=note, level=level)
module(R, "health", [
    prose("p1", L(
        "West Bengal has relatively low mortality: under-five mortality was 20 per 1,000 live births in 2021 (India 31), and the infant mortality rate was 20 in 2019. Life expectancy at birth was 71.6 years in 2014-18, above the national 69.4, and the birth rate (14.9 per 1,000 in 2019) is among the lowest of the large States. About 92% of births took place in health facilities in NFHS-5. Child undernutrition remains significant, with 33.8% of children under five stunted and 20.3% wasted, little changed from NFHS-4.\n\nKolkata is a major medical centre for eastern India, Bangladesh, Nepal and Bhutan, with old public institutions such as Medical College Kolkata (1835), the School of Tropical Medicine and SSKM Hospital, and many private hospitals.",
        "पश्चिम बंगाल में मृत्यु दर अपेक्षाकृत कम है: 2021 में पाँच वर्ष से कम आयु की मृत्यु दर प्रति 1,000 जीवित जन्म पर 20 (भारत 31) थी, और 2019 में शिशु मृत्यु दर 20 थी। 2014-18 में जन्म के समय जीवन प्रत्याशा 71.6 वर्ष थी, जो राष्ट्रीय 69.4 से अधिक है, और जन्म दर (2019 में प्रति 1,000 पर 14.9) बड़े राज्यों में सबसे कम में से है। एनएफ़एचएस-5 में लगभग 92% प्रसव स्वास्थ्य संस्थानों में हुए। बाल कुपोषण अब भी महत्त्वपूर्ण है: पाँच वर्ष से कम आयु के 33.8% बच्चे ठिगने और 20.3% दुबले थे, जो एनएफ़एचएस-4 से लगभग अपरिवर्तित है।\n\nकोलकाता पूर्वी भारत, बांग्लादेश, नेपाल और भूटान के लिए बड़ा चिकित्सा केंद्र है, जहाँ मेडिकल कॉलेज कोलकाता (1835), स्कूल ऑफ़ ट्रॉपिकल मेडिसिन और एसएसकेएम अस्पताल जैसे पुराने सार्वजनिक संस्थान और कई निजी अस्पताल हैं।",
        "पश्चिम बंगालमध्ये मृत्युदर तुलनेने कमी आहे: 2021 मध्ये पाच वर्षांखालील मृत्युदर दर 1,000 जिवंत जन्मांमागे 20 (भारत 31) होता, आणि 2019 मध्ये अर्भक मृत्युदर 20 होता. 2014-18 मध्ये जन्मतः आयुर्मान 71.6 वर्षे होते — राष्ट्रीय 69.4 पेक्षा जास्त — आणि जन्मदर (2019 मध्ये दर 1,000 मागे 14.9) मोठ्या राज्यांतील सर्वांत कमींपैकी आहे. एनएफएचएस-5 मध्ये सुमारे 92% प्रसूती आरोग्य संस्थांत झाल्या. बालकुपोषण अजूनही लक्षणीय आहे: पाच वर्षांखालील 33.8% मुले खुजी व 20.3% कृश होती, एनएफएचएस-4 पासून जवळपास अपरिवर्तित.\n\nकोलकाता हे पूर्व भारत, बांगलादेश, नेपाळ व भूतानसाठी मोठे वैद्यकीय केंद्र आहे — मेडिकल कॉलेज कोलकाता (1835), स्कूल ऑफ ट्रॉपिकल मेडिसिन व एसएसकेएम रुग्णालय यांसारख्या जुन्या सार्वजनिक संस्था आणि अनेक खासगी रुग्णालये."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("u5mr", L("Under-five mortality rate", "पाँच वर्ष से कम आयु की मृत्यु दर", "पाच वर्षांखालील मृत्युदर"), srsdp(srs["WB"]["U5MR"], "per 1,000 live births", "2021", "SRS 2021, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["U5MR"], "per 1,000 live births", "2021", level="national")),
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(20, "per 1,000 live births", "2019", "calendar", "srs", ESI_VS, note="SRS 2019, Economic Survey 2021-22 Statistical Appendix Table 8.2 (33 in 2009)."), "number", "lower-is-better",
             previous=dp(33, "per 1,000 live births", "2009", "calendar", "srs", ESI_VS)),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(14.9, "per 1,000 population", "2019", "calendar", "srs", ESI_VS, note="SRS 2019 (17.2 in 2009)."), "number"),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(71.6, "years", "2014-18", "survey", "srs", ESI_LE, note="SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male 70.7, female 72.6)."), "number", "higher-is-better",
             national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("WB"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin; the PIB summary used here lists only States that met the SDG target."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("wb mod2 ok")
