"""Telangana modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-TG"
ECI = "https://results.eci.gov.in/AcResultGenDecNew2023/partywiseresult-S29.htm"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_TG = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 16 Oct 2026. "
           "FY2025-26 is the latest year published for Telangana and may be revised.")
mo = research("mospi_tg.json")
NAME = L("Telangana", "तेलंगाना", "तेलंगणा")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Telangana's culture blends the Telugu traditions of the Deccan villages with the Persian- and Urdu-influenced court culture of Golconda and the Nizams. Bathukamma, the floral festival celebrated by women, and Bonalu, offerings to the goddess Mahankali in Hyderabad and Secunderabad, are State festivals. Perini Sivatandavam, a vigorous warrior dance revived from Kakatiya temple sculpture, and Oggu Katha and Burra Katha storytelling are folk forms. Hyderabad has a strong tradition of Urdu poetry, qawwali and Deccani painting, and a large Telugu film industry.\n\nCrafts include Pochampally ikat, Gadwal and Narayanpet saris and the Telia rumal, Cheriyal scroll paintings, Nirmal paintings and toys, Pembarthi brassware, Adilabad dokra and the silver filigree of Karimnagar.",
        "तेलंगाना की संस्कृति दक्कन के गाँवों की तेलुगु परंपराओं को गोलकुंडा और निज़ामों की फ़ारसी और उर्दू प्रभावित दरबारी संस्कृति के साथ मिलाती है। महिलाओं द्वारा मनाया जाने वाला फूलों का पर्व बतुकम्मा, और हैदराबाद व सिकंदराबाद में देवी महांकाली को भोग अर्पित करने का पर्व बोनालु राज्य उत्सव हैं। काकतीय मंदिर मूर्तियों से पुनर्जीवित ओजस्वी योद्धा नृत्य पेरिणी शिवतांडवम, और ओग्गु कथा व बुर्रा कथा लोक रूप हैं। हैदराबाद में उर्दू शायरी, क़व्वाली और दक्कनी चित्रकला की समृद्ध परंपरा है, और एक बड़ा तेलुगु फ़िल्म उद्योग भी।\n\nशिल्पों में पोचमपल्ली इकत, गदवाल और नारायणपेट साड़ियाँ और तेलिया रुमाल, चेरियाल पट-चित्र, निर्मल चित्र और खिलौने, पेम्बर्थी पीतल शिल्प, आदिलाबाद डोकरा और करीमनगर की चाँदी की तारकशी शामिल हैं।",
        "तेलंगणाची संस्कृती दख्खनी गावांच्या तेलुगु परंपरांना गोवळकोंडा व निजामांच्या फारसी व उर्दू प्रभावित दरबारी संस्कृतीशी जोडते. स्त्रिया साजरा करतात तो फुलांचा सण बतुकम्मा, आणि हैदराबाद व सिकंदराबादमध्ये देवी महांकालीला नैवेद्य अर्पण करण्याचा सण बोनालू हे राज्याचे सण आहेत. काकतीय मंदिरशिल्पांवरून पुनरुज्जीवित झालेले जोशपूर्ण योद्धा नृत्य पेरिणी शिवतांडवम, आणि ओग्गू कथा व बुर्रा कथा हे लोककलाप्रकार आहेत. हैदराबादमध्ये उर्दू शायरी, कव्वाली व दख्खनी चित्रकलेची समृद्ध परंपरा आहे, आणि मोठा तेलुगु चित्रपट उद्योगही.\n\nहस्तकलेत पोचमपल्ली इकत, गदवाल व नारायणपेठ साड्या व तेलिया रुमाल, चेरियाल पटचित्रे, निर्मल चित्रे व खेळणी, पेम्बर्थी पितळकाम, आदिलाबाद डोकरा आणि करीमनगरचे चांदीचे तारकाम यांचा समावेश आहे."),
        conf="Editorial"),
    lst("festivals", [
        fest("bathukamma", "Bathukamma", "बतुकम्मा", "बतुकम्मा", ("September–October", "सितंबर–अक्टूबर", "सप्टेंबर–ऑक्टोबर"),
             ("Nine days of flower stacks, songs and circle dances by women, ending before Dasara.", "महिलाओं द्वारा नौ दिन फूलों के ढेर, गीत और वृत्त नृत्य, दशहरे से पहले समाप्त।", "स्त्रियांचे नऊ दिवस फुलांचे मनोरे, गाणी व फेर, दसऱ्यापूर्वी समाप्त.")),
        fest("bonalu", "Bonalu", "बोनालु", "बोनालू", ("July–August", "जुलाई–अगस्त", "जुलै–ऑगस्ट"),
             ("Offerings of cooked rice to Mahankali in Hyderabad's temples.", "हैदराबाद के मंदिरों में महांकाली को पके चावल का भोग।", "हैदराबादच्या मंदिरांत महांकालीला शिजवलेल्या भाताचा नैवेद्य.")),
        fest("medaram", "Sammakka–Saralamma Jatara, Medaram", "सम्मक्का–सारलम्मा जातरा, मेडारम", "सम्मक्का–सारलम्मा जत्रा, मेडारम", ("February, every two years", "फ़रवरी, हर दो साल", "फेब्रुवारी, दर दोन वर्षांनी"),
             ("Tribal festival in Mulugu district drawing very large crowds.", "मुलुगु ज़िले का आदिवासी उत्सव, जिसमें बहुत बड़ी भीड़ आती है।", "मुलुगू जिल्ह्यातील आदिवासी उत्सव, प्रचंड गर्दी.")),
        fest("ramzan", "Ramzan and Eid", "रमज़ान और ईद", "रमजान व ईद", ("Varies", "बदलता है", "बदलते"),
             ("Night markets around the Charminar; haleem everywhere.", "चारमीनार के आसपास रात के बाज़ार; हर जगह हलीम।", "चारमिनारभोवती रात्रीचे बाजार; सर्वत्र हलीम.")),
        fest("sankranti", "Sankranti", "संक्रांति", "संक्रांत", ("January", "जनवरी", "जानेवारी"),
             ("Harvest festival with kites over Hyderabad.", "फ़सल उत्सव, हैदराबाद के आसमान में पतंगें।", "कापणीचा सण, हैदराबादच्या आकाशात पतंग.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("perini", "Perini Sivatandavam", "पेरिणी शिवतांडवम", "पेरिणी शिवतांडवम"), it3("oggu", "Oggu Katha", "ओग्गु कथा", "ओग्गू कथा"),
        it3("cheriyal", "Cheriyal scroll painting", "चेरियाल पट-चित्र", "चेरियाल पटचित्र"), it3("ikat", "Pochampally ikat", "पोचमपल्ली इकत", "पोचमपल्ली इकत"),
        it3("nirmal", "Nirmal painting", "निर्मल चित्रकला", "निर्मल चित्रकला"), it3("qawwali", "Qawwali and Urdu poetry", "क़व्वाली और उर्दू शायरी", "कव्वाली व उर्दू शायरी"),
        it3("filigree", "Silver filigree", "चाँदी की तारकशी", "चांदीचे तारकाम"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("biryani", "Hyderabadi biryani", "हैदराबादी बिरयानी", "हैदराबादी बिर्याणी", d=("Rice and meat cooked together in the dum style.", "दम शैली में साथ पकाए गए चावल और मांस।", "दम पद्धतीने एकत्र शिजवलेला भात व मांस.")),
        it3("haleem", "Haleem", "हलीम", "हलीम", d=("Slow-cooked wheat and meat, a Ramzan speciality; Hyderabad Haleem is a registered GI.", "धीमी आँच पर पका गेहूँ और मांस, रमज़ान की ख़ासियत; हैदराबाद हलीम पंजीकृत जीआई है।", "मंद आचेवर शिजवलेले गहू व मांस, रमजानची खासियत; हैदराबाद हलीम नोंदणीकृत जीआय आहे.")),
        it3("sarva", "Sarva pindi and sakinalu", "सर्व पिंडी और सकिनालु", "सर्व पिंडी व सकिनालू", d=("Rice-flour pancake and crisp sesame rings of Telangana villages.", "तेलंगाना के गाँवों का चावल-आटे का पैनकेक और कुरकुरे तिल के छल्ले।", "तेलंगणाच्या गावांतील तांदळाच्या पिठाचे धिरडे व कुरकुरीत तिळाची वलये.")),
        it3("irani", "Irani chai and Osmania biscuits", "ईरानी चाय और उस्मानिया बिस्कुट", "इराणी चहा व उस्मानिया बिस्किटे", d=("Café staples of old Hyderabad.", "पुराने हैदराबाद के कैफ़े की पहचान।", "जुन्या हैदराबादच्या कॅफेंची ओळख.")),
        it3("qubani", "Double ka meetha and qubani ka meetha", "डबल का मीठा और क़ुबानी का मीठा", "डबल का मीठा व कुबानी का मीठा", d=("Bread pudding and apricot dessert at weddings.", "शादियों में ब्रेड पुडिंग और ख़ुबानी की मिठाई।", "लग्नसमारंभात ब्रेड पुडिंग व जर्दाळूचे पक्वान्न.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("saree", "Pochampally, Gadwal and Narayanpet saris", "पोचमपल्ली, गदवाल और नारायणपेट साड़ियाँ", "पोचमपल्ली, गदवाल व नारायणपेठ साड्या", d=("Handloom saris for daily and festive wear.", "रोज़ और उत्सव के लिए हथकरघा साड़ियाँ।", "रोजच्या व सणासुदीच्या हातमाग साड्या.")),
        it3("sherwani", "Sherwani and khada dupatta", "शेरवानी और खड़ा दुपट्टा", "शेरवानी व खडा दुपट्टा", d=("Hyderabadi wedding dress.", "हैदराबादी विवाह पोशाक।", "हैदराबादी लग्नपोशाख.")),
        it3("lambadi", "Lambadi mirror-work dress", "लंबाडी शीशा-कढ़ाई पोशाक", "लंबाडी आरसेकाम पोशाख", d=("Colourful embroidered skirts and headwear of Lambada women.", "लंबाडा महिलाओं के रंगीन कढ़ाई वाले घाघरे और सिर-पोशाक।", "लंबाडा स्त्रियांचे रंगीबेरंगी भरतकामाचे घागरे व शिरोभूषणे.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]
re_prof = 100 * g["realestate_prof"] / g["total"]; trade = 100 * g["trade_hotels"] / g["total"]
module(R, "economy", [
    prose("p1", L(
        f"Telangana's GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26 in the MoSPI series, and its per capita NSDP — ₹{inr(pc['FY2025-26'][0])} — is among the highest of the larger States. The economy leans heavily on services: real estate, IT and professional services made up about {re_prof:.0f}% of GSVA in FY2024-25, and trade, repair, hotels and restaurants about {trade:.0f}%. Hyderabad hosts the Indian offices and global capability centres of many technology companies, and its Genome Valley and pharmaceutical industry make vaccines and bulk drugs for the world. Agriculture, livestock and fishing were about {agri:.0f}% of GSVA — rice, cotton, maize, red gram and chillies are the main crops — and manufacturing about {mfg:.0f}%, including pharmaceuticals, defence and aerospace components, and coal mining by the Singareni Collieries.\n\nThe PLFS unemployment rate was 5.0% in 2025, above the national 3.1%, and women's labour-force participation was 46.4%.",
        f"मोस्पी शृंखला में वित्त वर्ष 2025-26 में तेलंगाना का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ था, और इसका प्रति व्यक्ति एनएसडीपी — ₹{inr(pc['FY2025-26'][0])} — बड़े राज्यों में सबसे ऊँचे में से है। अर्थव्यवस्था सेवाओं पर बहुत निर्भर है: वित्त वर्ष 2024-25 में रियल एस्टेट, आईटी और पेशेवर सेवाएँ जीएसवीए का लगभग {re_prof:.0f}% थीं, और व्यापार, मरम्मत, होटल व रेस्तराँ लगभग {trade:.0f}%। हैदराबाद में कई प्रौद्योगिकी कंपनियों के भारतीय दफ़्तर और वैश्विक क्षमता केंद्र हैं, और इसकी जीनोम वैली व दवा उद्योग दुनिया के लिए टीके और बल्क दवाएँ बनाते हैं। कृषि, पशुपालन और मत्स्य पालन जीएसवीए का लगभग {agri:.0f}% थे — धान, कपास, मक्का, अरहर और मिर्च मुख्य फ़सलें हैं — और विनिर्माण लगभग {mfg:.0f}%, जिसमें दवाएँ, रक्षा और एयरोस्पेस पुर्ज़े, और सिंगरेणी कोलियरीज़ का कोयला खनन शामिल है।\n\n2025 में पीएलएफ़एस बेरोज़गारी दर 5.0% थी, जो राष्ट्रीय 3.1% से अधिक है, और महिलाओं की श्रम बल भागीदारी 46.4% थी।",
        f"मोस्पी मालिकेनुसार आ.व. 2025-26 मध्ये तेलंगणाचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी होते, आणि त्याचे दरडोई एनएसडीपी — ₹{inr(pc['FY2025-26'][0])} — मोठ्या राज्यांतील सर्वाधिकांपैकी आहे. अर्थव्यवस्था सेवाक्षेत्रावर मोठ्या प्रमाणावर अवलंबून आहे: आ.व. 2024-25 मध्ये स्थावर मालमत्ता, आयटी व व्यावसायिक सेवांचा जीएसव्हीएमध्ये सुमारे {re_prof:.0f}% वाटा होता, आणि व्यापार, दुरुस्ती, हॉटेल व उपाहारगृहांचा सुमारे {trade:.0f}%. हैदराबादमध्ये अनेक तंत्रज्ञान कंपन्यांची भारतीय कार्यालये व जागतिक क्षमता केंद्रे आहेत, आणि तिथली जीनोम व्हॅली व औषध उद्योग जगासाठी लसी व बल्क औषधे बनवतात. शेती, पशुपालन व मत्स्यव्यवसायाचा वाटा सुमारे {agri:.0f}% होता — भात, कापूस, मका, तूर व मिरची ही मुख्य पिके — आणि उत्पादन उद्योगाचा सुमारे {mfg:.0f}%, ज्यात औषधे, संरक्षण व हवाई-अवकाश सुटे भाग, आणि सिंगरेणी कोलियरीजचे कोळसा खाणकाम यांचा समावेश आहे.\n\n2025 मध्ये पीएलएफएस बेरोजगारी दर 5.0% होता, राष्ट्रीय 3.1% पेक्षा जास्त, आणि स्त्रियांचा श्रमशक्ती सहभाग 46.4% होता."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_TG), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_TG), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_TG), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("TG", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    plfs_series("TG", NAME),
    lst("sectors-key", [
        it3("it", "IT and global capability centres", "आईटी और वैश्विक क्षमता केंद्र", "आयटी व जागतिक क्षमता केंद्रे", d=("HITEC City, Gachibowli and the Financial District, Hyderabad.", "हाईटेक सिटी, गच्चीबौली और फ़ाइनेंशियल डिस्ट्रिक्ट, हैदराबाद।", "हायटेक सिटी, गच्चीबावली व फायनान्शियल डिस्ट्रिक्ट, हैदराबाद.")),
        it3("pharma", "Pharmaceuticals and life sciences", "दवा और जीवन विज्ञान", "औषधनिर्मिती व जीवनविज्ञान", d=("Genome Valley and bulk-drug units around Hyderabad.", "जीनोम वैली और हैदराबाद के आसपास बल्क ड्रग इकाइयाँ।", "जीनोम व्हॅली व हैदराबादभोवती बल्क ड्रग कारखाने.")),
        it3("defence", "Defence and aerospace", "रक्षा और एयरोस्पेस", "संरक्षण व हवाई-अवकाश", d=("DRDO laboratories, public-sector units and private suppliers.", "डीआरडीओ प्रयोगशालाएँ, सार्वजनिक क्षेत्र इकाइयाँ और निजी आपूर्तिकर्ता।", "डीआरडीओ प्रयोगशाळा, सार्वजनिक उपक्रम व खासगी पुरवठादार.")),
        it3("coal", "Coal", "कोयला", "कोळसा", d=("Singareni Collieries in the Godavari valley coalfield.", "गोदावरी घाटी कोयला क्षेत्र में सिंगरेणी कोलियरीज़।", "गोदावरी खोरे कोळसा क्षेत्रातील सिंगरेणी कोलियरीज.")),
        it3("agri", "Rice, cotton and chillies", "धान, कपास और मिर्च", "भात, कापूस व मिरची", d=("Canal and tank-fed farming across the plateau.", "पूरे पठार पर नहर और तालाब से सिंचित खेती।", "पठारभर कालवा व तलावाधारित शेती.")),
        it3("textile", "Textiles and handlooms", "वस्त्र और हथकरघा", "वस्त्र व हातमाग", d=("PM MITRA park at Warangal; Pochampally and Gadwal weavers.", "वारंगल में पीएम मित्र पार्क; पोचमपल्ली और गदवाल के बुनकर।", "वरंगळ येथील पीएम मित्र पार्क; पोचमपल्ली व गदवालचे विणकर.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("IT/ITeS exports from Telangana", "तेलंगाना से आईटी/आईटीईएस निर्यात", "तेलंगणातून आयटी/आयटीईएस निर्यात"), "india-gov", "State ITE&C department annual report."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("FDI equity inflows", "एफ़डीआई इक्विटी प्रवाह", "एफडीआय समभाग गुंतवणूक"), "dpiit", "DPIIT state-wise FDI factsheet."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Telangana has a bicameral legislature: a 119-member Legislative Assembly and a 40-member Legislative Council, both in Hyderabad. The State elects 17 members to the Lok Sabha and 7 to the Rajya Sabha.\n\nIn the Assembly election of November 2023 the Congress won 64 seats, the Bharat Rashtra Samithi (formerly the Telangana Rashtra Samithi, which governed from 2014) 39, the BJP 8, the AIMIM 7 and the CPI 1 (ECI). A. Revanth Reddy was sworn in as Chief Minister on 7 December 2023, with Mallu Bhatti Vikramarka as Deputy Chief Minister. Shiv Pratap Shukla became Governor in March 2026.",
        "तेलंगाना में द्विसदनीय विधानमंडल है: 119 सदस्यों वाली विधानसभा और 40 सदस्यों वाली विधान परिषद, दोनों हैदराबाद में। राज्य से लोकसभा के 17 और राज्यसभा के 7 सदस्य चुने जाते हैं।\n\nनवंबर 2023 के विधानसभा चुनाव में कांग्रेस ने 64, भारत राष्ट्र समिति (पूर्व में तेलंगाना राष्ट्र समिति, जिसने 2014 से शासन किया) ने 39, भाजपा ने 8, एआईएमआईएम ने 7 और भाकपा ने 1 सीट जीती (भारत निर्वाचन आयोग)। ए. रेवंत रेड्डी ने 7 दिसंबर 2023 को मुख्यमंत्री पद की शपथ ली, और मल्लु भट्टि विक्रमार्क उपमुख्यमंत्री बने। मार्च 2026 में शिव प्रताप शुक्ल राज्यपाल बने।",
        "तेलंगणात द्विसदनी विधिमंडळ आहे: 119 सदस्यांची विधानसभा व 40 सदस्यांची विधान परिषद, दोन्ही हैदराबादमध्ये. राज्यातून लोकसभेवर 17 आणि राज्यसभेवर 7 सदस्य निवडले जातात.\n\nनोव्हेंबर 2023 च्या विधानसभा निवडणुकीत काँग्रेसने 64, भारत राष्ट्र समितीने (पूर्वीची तेलंगणा राष्ट्र समिती, जिने 2014 पासून राज्य केले) 39, भाजपने 8, एआयएमआयएमने 7 व भाकपने 1 जागा जिंकली (भारत निवडणूक आयोग). ए. रेवंत रेड्डी यांनी 7 डिसेंबर 2023 रोजी मुख्यमंत्रिपदाची शपथ घेतली, आणि मल्लू भट्टी विक्रमार्क उपमुख्यमंत्री झाले. मार्च 2026 मध्ये शिव प्रताप शुक्ला राज्यपाल झाले."),
        sources=["eci", "tribune", "ians"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    table("result2023", L("Assembly election 2023 — seats won", "विधानसभा चुनाव 2023 — जीती गई सीटें", "विधानसभा निवडणूक 2023 — जिंकलेल्या जागा"),
          [col(L("Party", "दल", "पक्ष")), col(L("Seats", "सीटें", "जागा"), "right")],
          [[L("Indian National Congress", "भारतीय राष्ट्रीय कांग्रेस", "भारतीय राष्ट्रीय काँग्रेस"), "64"], [L("Bharat Rashtra Samithi", "भारत राष्ट्र समिति", "भारत राष्ट्र समिती"), "39"],
           [L("Bharatiya Janata Party", "भारतीय जनता पार्टी", "भारतीय जनता पक्ष"), "8"], [L("All India Majlis-e-Ittehadul Muslimeen", "ऑल इंडिया मजलिस-ए-इत्तेहादुल मुस्लिमीन", "ऑल इंडिया मजलिस-ए-इत्तेहादुल मुस्लिमीन"), "7"],
           [L("Communist Party of India", "भारतीय कम्युनिस्ट पार्टी", "भारतीय कम्युनिस्ट पक्ष"), "1"], [L("Total", "कुल", "एकूण"), "119"]],
          "eci", ECI, period="2023",
          note=L("ECI results website, December 2023. Later by-elections and defections are not reflected.", "भारत निर्वाचन आयोग की परिणाम वेबसाइट, दिसंबर 2023। बाद के उपचुनाव और दलबदल शामिल नहीं।", "भारत निवडणूक आयोगाचे निकाल संकेतस्थळ, डिसेंबर 2023. नंतरच्या पोटनिवडणुका व पक्षांतरे समाविष्ट नाहीत.")),
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("portal", "Government of Telangana", "तेलंगाना सरकार", "तेलंगणा शासन", url="https://www.telangana.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Leader of Opposition — official recognition", "नेता प्रतिपक्ष — आधिकारिक मान्यता", "विरोधी पक्षनेते — अधिकृत मान्यता"), "india-gov", "Legislature secretariat notice."),
        (L("Local bodies by type", "प्रकार के अनुसार स्थानीय निकाय", "प्रकारानुसार स्थानिक स्वराज्य संस्था"), "india-gov", "Panchayat Raj and Municipal Administration departments."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "On 10 May 2026 the Prime Minister inaugurated or laid foundation stones for projects worth about ₹9,400 crore in Telangana, including the PM MITRA textile park at Warangal, the Zaheerabad industrial area and a four-lane section of NH-167. Each card shows its source and the date it was checked.",
        "10 मई 2026 को प्रधानमंत्री ने तेलंगाना में लगभग ₹9,400 करोड़ की परियोजनाओं का उद्घाटन या शिलान्यास किया, जिनमें वारंगल का पीएम मित्र वस्त्र पार्क, ज़हीराबाद औद्योगिक क्षेत्र और एनएच-167 का चार-लेन खंड शामिल हैं। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "10 मे 2026 रोजी पंतप्रधानांनी तेलंगणातील सुमारे ₹9,400 कोटींच्या प्रकल्पांचे उद्घाटन किंवा पायाभरणी केली, ज्यात वरंगळचे पीएम मित्र वस्त्र उद्यान, झहीराबाद औद्योगिक क्षेत्र व एनएच-167 चा चौपदरी टप्पा यांचा समावेश आहे. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pmindia"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Kaleshwaram Lift Irrigation Project — official status", "कालेश्वरम लिफ़्ट सिंचाई परियोजना — आधिकारिक स्थिति", "कालेश्वरम उपसा सिंचन प्रकल्प — अधिकृत स्थिती"), "india-gov", "National Dam Safety Authority report and State irrigation department."),
        (L("Hyderabad Metro Phase II — approval status", "हैदराबाद मेट्रो चरण II — स्वीकृति स्थिति", "हैदराबाद मेट्रो टप्पा II — मंजुरी स्थिती"), "india-gov", "Ministry of Housing and Urban Affairs."),
        (L("Regional Ring Road — status", "क्षेत्रीय रिंग रोड — स्थिति", "प्रादेशिक रिंग रोड — स्थिती"), "nhai", "NHAI / MoRTH."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Rajiv Gandhi International Airport at Shamshabad is Hyderabad's airport and one of India's busiest. Secunderabad is the headquarters of the South Central Railway, and Kacheguda, Secunderabad and the new Charlapalli terminal handle long-distance trains. Hyderabad's Outer Ring Road circles the city, and its elevated metro, built in public–private partnership, links the old and new cities. National highways radiate to Bengaluru, Nagpur, Mumbai, Vijayawada and Visakhapatnam. As a land-locked State, Telangana's trade uses the ports of Andhra Pradesh and Maharashtra.",
        "शमशाबाद का राजीव गांधी अंतरराष्ट्रीय हवाई अड्डा हैदराबाद का हवाई अड्डा है और भारत के सबसे व्यस्त हवाई अड्डों में है। सिकंदराबाद दक्षिण मध्य रेलवे का मुख्यालय है, और काचीगुडा, सिकंदराबाद और नया चर्लापल्ली टर्मिनल लंबी दूरी की रेलें संभालते हैं। हैदराबाद की आउटर रिंग रोड शहर को घेरती है, और सार्वजनिक–निजी भागीदारी से बनी इसकी एलिवेटेड मेट्रो पुराने और नए शहर को जोड़ती है। राष्ट्रीय राजमार्ग बेंगलूरु, नागपुर, मुंबई, विजयवाड़ा और विशाखापत्तनम की ओर जाते हैं। भू-आबद्ध राज्य होने से तेलंगाना का व्यापार आंध्र प्रदेश और महाराष्ट्र के बंदरगाहों से होता है।",
        "शमशाबाद येथील राजीव गांधी आंतरराष्ट्रीय विमानतळ हे हैदराबादचे विमानतळ असून भारतातील सर्वांत व्यस्त विमानतळांपैकी एक आहे. सिकंदराबाद हे दक्षिण मध्य रेल्वेचे मुख्यालय आहे, आणि काचीगुडा, सिकंदराबाद व नवे चर्लापल्ली टर्मिनल लांब पल्ल्याच्या गाड्या हाताळतात. हैदराबादचा आउटर रिंग रोड शहराला वेढतो, आणि सार्वजनिक–खासगी भागीदारीतून बांधलेली उन्नत मेट्रो जुने व नवे शहर जोडते. राष्ट्रीय महामार्ग बंगळूरु, नागपूर, मुंबई, विजयवाडा व विशाखापट्टणमकडे जातात. भूवेष्टित राज्य असल्याने तेलंगणाचा व्यापार आंध्र प्रदेश व महाराष्ट्राच्या बंदरांमार्फत होतो."),
        conf="Editorial"),
    lst("airports", [
        it3("hyd", "Rajiv Gandhi International Airport, Hyderabad", "राजीव गांधी अंतरराष्ट्रीय हवाई अड्डा, हैदराबाद", "राजीव गांधी आंतरराष्ट्रीय विमानतळ, हैदराबाद", m=("HYD", "HYD", "HYD")),
        it3("bpm", "Begumpet (business aviation)", "बेगमपेट (व्यावसायिक विमानन)", "बेगमपेट (व्यावसायिक विमानसेवा)"),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Hyderabad Metro operational length and ridership", "हैदराबाद मेट्रो की चालू लंबाई और यात्री संख्या", "हैदराबाद मेट्रोची कार्यरत लांबी व प्रवासी संख्या"), "india-gov", "Hyderabad Metro Rail Ltd."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Telangana's power comes mainly from coal mined by the Singareni Collieries in the Godavari valley. NTPC's Ramagundam station and the State's plants at Kothagudem, Bhupalpally and the new Yadadri station at Damaracherla are the largest generators, and hydro stations at Nagarjuna Sagar, Srisailam (left bank) and on the Godavari add peaking power. Solar parks have been built in the south and west of the State, and the State supplies free power for farm pumps.",
        "तेलंगाना की बिजली मुख्यतः गोदावरी घाटी में सिंगरेणी कोलियरीज़ द्वारा निकाले गए कोयले से आती है। एनटीपीसी का रामागुंडम संयंत्र और कोठागुडेम, भूपालपल्ली व दामरचर्ला के नए यादाद्रि संयंत्र जैसे राज्य के संयंत्र सबसे बड़े उत्पादक हैं, और नागार्जुन सागर, श्रीशैलम (बायाँ किनारा) और गोदावरी के जलविद्युत केंद्र पीक बिजली जोड़ते हैं। राज्य के दक्षिण और पश्चिम में सौर पार्क बने हैं, और राज्य खेतों के पंपों के लिए मुफ़्त बिजली देता है।",
        "तेलंगणाची वीज मुख्यतः गोदावरी खोऱ्यात सिंगरेणी कोलियरीजने खणलेल्या कोळशापासून येते. एनटीपीसीचे रामगुंडम केंद्र आणि कोठागुडेम, भूपालपल्ली व दामरचर्ला येथील नवे यादाद्री केंद्र ही राज्याची केंद्रे सर्वांत मोठी उत्पादक आहेत, आणि नागार्जुन सागर, श्रीशैलम (डावा किनारा) व गोदावरीवरील जलविद्युत केंद्रे कमाल मागणीसाठी वीज देतात. राज्याच्या दक्षिण व पश्चिम भागात सौर उद्याने उभारली आहेत, आणि राज्य शेतीपंपांसाठी मोफत वीज देते."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
        (L("Coal production (Singareni)", "कोयला उत्पादन (सिंगरेणी)", "कोळसा उत्पादन (सिंगरेणी)"), "india-gov", "Ministry of Coal statistics."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Hyderabad is one of India's leading technology cities. HITEC City, opened in 1998, grew into the Cyberabad district of Madhapur, Gachibowli and the Financial District, home to large campuses of global technology firms and a growing number of global capability centres. T-Hub, the State-backed start-up incubator, and T-Works, a prototyping centre, support new companies, and research institutions such as IIIT Hyderabad, IIT Hyderabad and the University of Hyderabad feed the industry.",
        "हैदराबाद भारत के अग्रणी प्रौद्योगिकी शहरों में है। 1998 में खुली हाईटेक सिटी माधापुर, गच्चीबौली और फ़ाइनेंशियल डिस्ट्रिक्ट के साइबराबाद क्षेत्र में बढ़ी, जहाँ वैश्विक प्रौद्योगिकी कंपनियों के बड़े परिसर और बढ़ती संख्या में वैश्विक क्षमता केंद्र हैं। राज्य समर्थित स्टार्टअप इनक्यूबेटर टी-हब और प्रोटोटाइपिंग केंद्र टी-वर्क्स नई कंपनियों की मदद करते हैं, और आईआईआईटी हैदराबाद, आईआईटी हैदराबाद और हैदराबाद विश्वविद्यालय जैसे शोध संस्थान उद्योग को प्रतिभा देते हैं।",
        "हैदराबाद हे भारतातील आघाडीच्या तंत्रज्ञान शहरांपैकी आहे. 1998 मध्ये सुरू झालेली हायटेक सिटी माधापूर, गच्चीबावली व फायनान्शियल डिस्ट्रिक्टच्या सायबराबाद भागात विस्तारली, जिथे जागतिक तंत्रज्ञान कंपन्यांची मोठी संकुले व वाढत्या संख्येने जागतिक क्षमता केंद्रे आहेत. राज्य-पुरस्कृत स्टार्टअप इन्क्युबेटर टी-हब व प्रोटोटायपिंग केंद्र टी-वर्क्स नव्या कंपन्यांना मदत करतात, आणि आयआयआयटी हैदराबाद, आयआयटी हैदराबाद व हैदराबाद विद्यापीठ यांसारख्या संशोधन संस्था उद्योगाला मनुष्यबळ पुरवतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Andhra Pradesh circle, which includes Telangana)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("TG", NAME)
module(R, "education", [
    prose("p1", L(
        "Telangana's higher-education gross enrolment ratio (ages 18–23) was 40.0% in 2021-22 in AISHE, among the highest of the larger States and well above the national 28.4%; women's GER (41.6%) was higher than men's (38.5%). The State had 31 universities and 2,083 colleges. Literacy at the 2011 Census was 66.5%.\n\nOsmania University (1918), the first university to teach in Urdu, is the oldest. Hyderabad also has the University of Hyderabad, the English and Foreign Languages University, Maulana Azad National Urdu University, IIT Hyderabad, IIIT Hyderabad, the Indian School of Business, NALSAR University of Law and national laboratories such as CCMB, IICT and NGRI; NIT Warangal (1959) is one of the oldest NITs.",
        "एआईएसएचई के अनुसार 2021-22 में तेलंगाना का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) 40.0% था, जो बड़े राज्यों में सबसे ऊँचे में से है और राष्ट्रीय 28.4% से काफ़ी अधिक; महिलाओं का जीईआर (41.6%) पुरुषों (38.5%) से अधिक था। राज्य में 31 विश्वविद्यालय और 2,083 कॉलेज थे। 2011 की जनगणना में साक्षरता 66.5% थी।\n\nउर्दू में पढ़ाने वाला पहला विश्वविद्यालय उस्मानिया विश्वविद्यालय (1918) सबसे पुराना है। हैदराबाद में हैदराबाद विश्वविद्यालय, अंग्रेज़ी एवं विदेशी भाषा विश्वविद्यालय, मौलाना आज़ाद राष्ट्रीय उर्दू विश्वविद्यालय, आईआईटी हैदराबाद, आईआईआईटी हैदराबाद, इंडियन स्कूल ऑफ़ बिज़नेस, नालसार विधि विश्वविद्यालय और सीसीएमबी, आईआईसीटी व एनजीआरआई जैसी राष्ट्रीय प्रयोगशालाएँ भी हैं; एनआईटी वारंगल (1959) सबसे पुराने एनआईटी में से है।",
        "एआयएसएचईनुसार 2021-22 मध्ये तेलंगणाचे उच्चशिक्षणातील एकूण नोंदणी गुणोत्तर (18–23 वय) 40.0% होते — मोठ्या राज्यांतील सर्वाधिकांपैकी व राष्ट्रीय 28.4% पेक्षा बरेच जास्त; स्त्रियांचे जीईआर (41.6%) पुरुषांपेक्षा (38.5%) जास्त होते. राज्यात 31 विद्यापीठे व 2,083 महाविद्यालये होती. 2011 च्या जनगणनेत साक्षरता 66.5% होती.\n\nउर्दूतून शिकवणारे पहिले विद्यापीठ, उस्मानिया विद्यापीठ (1918), सर्वांत जुने आहे. हैदराबादमध्ये हैदराबाद विद्यापीठ, इंग्रजी व परदेशी भाषा विद्यापीठ, मौलाना आझाद राष्ट्रीय उर्दू विद्यापीठ, आयआयटी हैदराबाद, आयआयआयटी हैदराबाद, इंडियन स्कूल ऑफ बिझनेस, नालसार विधी विद्यापीठ आणि सीसीएमबी, आयआयसीटी व एनजीआरआय यांसारख्या राष्ट्रीय प्रयोगशाळा आहेत; एनआयटी वरंगळ (1959) हे सर्वांत जुन्या एनआयटींपैकी आहे."),
        sources=["aishe", "msme-di"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("ou", "Osmania University", "उस्मानिया विश्वविद्यालय", "उस्मानिया विद्यापीठ", m=("Hyderabad, 1918", "हैदराबाद, 1918", "हैदराबाद, 1918")),
        it3("uoh", "University of Hyderabad", "हैदराबाद विश्वविद्यालय", "हैदराबाद विद्यापीठ", m=("Gachibowli", "गच्चीबौली", "गच्चीबावली")),
        it3("iith", "IIT Hyderabad", "आईआईटी हैदराबाद", "आयआयटी हैदराबाद", m=("Kandi, Sangareddy", "कंदी, संगारेड्डी", "कंदी, संगारेड्डी")),
        it3("iiith", "IIIT Hyderabad", "आईआईआईटी हैदराबाद", "आयआयआयटी हैदराबाद", m=("Gachibowli", "गच्चीबौली", "गच्चीबावली")),
        it3("nitw", "NIT Warangal", "एनआईटी वारंगल", "एनआयटी वरंगळ", m=("Warangal, 1959", "वारंगल, 1959", "वरंगळ, 1959")),
        it3("nalsar", "NALSAR University of Law", "नालसार विधि विश्वविद्यालय", "नालसार विधी विद्यापीठ", m=("Hyderabad", "हैदराबाद", "हैदराबाद")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("NIRF-ranked institutions", "एनआईआरएफ़ रैंक वाले संस्थान", "एनआयआरएफ क्रमवारीतील संस्था"), "nirf", "Latest NIRF list filtered to Telangana."),
    ]),
])

# ---------------- O. Health ----------------
srs = NF["SRS_2021_PIB_PRID2128024"]
def srsdp(v, unit, period, note=None, level="state"):
    return dp(v, unit, period, "survey" if "-" in period else "calendar", "srs", SRS, note=note, level=level)
module(R, "health", [
    prose("p1", L(
        "Telangana has met the national goal for maternal mortality: the maternal mortality ratio was 45 per 1,00,000 live births in 2019-21, against 93 for India. Under-five mortality was 22 per 1,000 live births in 2021 (India 31), and the infant mortality rate was 21 in 2020. Nearly all births (97.0%) took place in health facilities in NFHS-5. Child nutrition worsened between NFHS-4 and NFHS-5, however: the share of stunted children under five rose from 28.1% to 33.1% and wasted children from 18.0% to 21.7%.\n\nHyderabad is a large medical centre, with Osmania and Gandhi general hospitals, NIMS, the MNJ cancer institute and many private hospitals that draw patients from across India and abroad.",
        "तेलंगाना ने मातृ मृत्यु का राष्ट्रीय लक्ष्य पूरा कर लिया है: 2019-21 में मातृ मृत्यु अनुपात प्रति 1,00,000 जीवित जन्म पर 45 था, जबकि भारत का 93। 2021 में पाँच वर्ष से कम आयु की मृत्यु दर प्रति 1,000 जीवित जन्म पर 22 (भारत 31) थी, और 2020 में शिशु मृत्यु दर 21 थी। एनएफ़एचएस-5 में लगभग सभी प्रसव (97.0%) स्वास्थ्य संस्थानों में हुए। लेकिन एनएफ़एचएस-4 और एनएफ़एचएस-5 के बीच बाल पोषण बिगड़ा: पाँच वर्ष से कम आयु के ठिगने बच्चों का हिस्सा 28.1% से बढ़कर 33.1% और दुबले बच्चों का 18.0% से 21.7% हो गया।\n\nहैदराबाद एक बड़ा चिकित्सा केंद्र है, जहाँ उस्मानिया और गांधी सामान्य अस्पताल, निम्स, एमएनजे कैंसर संस्थान और कई निजी अस्पताल हैं, जो पूरे भारत और विदेश से मरीज़ों को आकर्षित करते हैं।",
        "तेलंगणाने मातामृत्यूचे राष्ट्रीय उद्दिष्ट गाठले आहे: 2019-21 मध्ये मातामृत्यू प्रमाण दर 1,00,000 जिवंत जन्मांमागे 45 होते, तर भारताचे 93. 2021 मध्ये पाच वर्षांखालील मृत्युदर दर 1,000 जिवंत जन्मांमागे 22 (भारत 31) होता, आणि 2020 मध्ये अर्भक मृत्युदर 21 होता. एनएफएचएस-5 मध्ये जवळपास सर्व प्रसूती (97.0%) आरोग्य संस्थांत झाल्या. मात्र एनएफएचएस-4 ते एनएफएचएस-5 दरम्यान बालपोषण खालावले: पाच वर्षांखालील खुज्या मुलांचा वाटा 28.1% वरून 33.1% आणि कृश मुलांचा 18.0% वरून 21.7% झाला.\n\nहैदराबाद हे मोठे वैद्यकीय केंद्र आहे — उस्मानिया व गांधी सामान्य रुग्णालये, निम्स, एमएनजे कर्करोग संस्था आणि अनेक खासगी रुग्णालये, जी संपूर्ण भारतातून व परदेशातून रुग्ण आकर्षित करतात."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("mmr", L("Maternal mortality ratio", "मातृ मृत्यु अनुपात", "मातामृत्यू प्रमाण"), srsdp(srs["TG"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", "SRS 2019-21, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", level="national")),
        fact("u5mr", L("Under-five mortality rate", "पाँच वर्ष से कम आयु की मृत्यु दर", "पाच वर्षांखालील मृत्युदर"), srsdp(srs["TG"]["U5MR"], "per 1,000 live births", "2021", "SRS 2021, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["U5MR"], "per 1,000 live births", "2021", level="national")),
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(21, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(16.4, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020 (death rate 6.0)."), "number",
             national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("TG"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Life expectancy at birth (Telangana)", "जन्म के समय जीवन प्रत्याशा (तेलंगाना)", "जन्मतः आयुर्मान (तेलंगणा)"), "srs", "SRS abridged life tables; the 2014-18 table gives Andhra Pradesh including Telangana only."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("tg mod2 ok")
