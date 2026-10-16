"""Madhya Pradesh modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-MP"
ECI = "https://results.eci.gov.in/AcResultGenDecNew2023/partywiseresult-S12.htm"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_MP = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 16 Oct 2026. "
           "FY2025-26 is the latest year published for Madhya Pradesh and may be revised.")
mo = research("mospi_mp.json")
NAME = L("Madhya Pradesh", "मध्य प्रदेश", "मध्य प्रदेश")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Madhya Pradesh has deep roots in Indian classical music: Tansen, the legendary singer of Akbar's court, is buried in Gwalior, the home of the oldest khayal gharana, and Ustad Allauddin Khan made Maihar a great centre of instrumental music. The State's tribal art is world-famous — Gond painting, made famous by artists from Patangarh, and the Pithora and dot paintings of the Bhils. Bhopal's Bharat Bhavan and the Tribal Museum showcase modern and tribal art. Folk forms include the Matki dance of Malwa, Rai and Badhai of Bundelkhand, and Bhagoria, the spring festival of the Bhils.\n\nCrafts include Chanderi and Maheshwari saris, Bagh block prints, Gwalior carpets and stone carving, Dokra-like bell-metal from Datia and Tikamgarh, and the wrought-iron craft of Dindori.",
        "मध्य प्रदेश की जड़ें भारतीय शास्त्रीय संगीत में गहरी हैं: अकबर के दरबार के महान गायक तानसेन ग्वालियर में दफ़्न हैं, जो सबसे पुराने ख़याल घराने का घर है, और उस्ताद अलाउद्दीन ख़ाँ ने मैहर को वाद्य संगीत का बड़ा केंद्र बनाया। राज्य की जनजातीय कला विश्व प्रसिद्ध है — पाटनगढ़ के कलाकारों से प्रसिद्ध हुई गोंड चित्रकला, और भीलों की पिथौरा और बिंदु चित्रकला। भोपाल का भारत भवन और जनजातीय संग्रहालय आधुनिक और जनजातीय कला दिखाते हैं। लोक रूपों में मालवा का मटकी नृत्य, बुंदेलखंड के राई और बधाई, और भीलों का वसंत उत्सव भगोरिया शामिल हैं।\n\nशिल्पों में चंदेरी और महेश्वरी साड़ियाँ, बाग़ ठप्पा छपाई, ग्वालियर के कालीन और पत्थर नक्काशी, दतिया और टीकमगढ़ के घंटा-धातु के बर्तन, और डिंडोरी का लौह शिल्प शामिल हैं।",
        "मध्य प्रदेशची मुळे भारतीय अभिजात संगीतात खोलवर आहेत: अकबराच्या दरबारातील महान गायक तानसेन ग्वाल्हेरमध्ये चिरनिद्रा घेत आहेत — सर्वांत जुन्या ख्याल घराण्याचे घर — आणि उस्ताद अल्लाउद्दीन खाँ यांनी मैहरला वाद्यसंगीताचे मोठे केंद्र बनवले. राज्याची आदिवासी कला जगप्रसिद्ध आहे — पाटनगडच्या कलाकारांमुळे प्रसिद्ध झालेली गोंड चित्रकला, आणि भिल्लांची पिठोरा व ठिपक्यांची चित्रकला. भोपाळचे भारत भवन व आदिवासी संग्रहालय आधुनिक व आदिवासी कला मांडतात. लोककलांत माळव्याचे मटकी नृत्य, बुंदेलखंडचे राई व बधाई, आणि भिल्लांचा वसंतोत्सव भगोरिया यांचा समावेश आहे.\n\nहस्तकलेत चंदेरी व महेश्वरी साड्या, बाग ठसे छपाई, ग्वाल्हेरचे गालिचे व दगडी कोरीवकाम, दतिया व टीकमगडची घंटाधातू भांडी, आणि डिंडोरीची लोखंडी हस्तकला यांचा समावेश आहे."),
        conf="Editorial"),
    lst("festivals", [
        fest("simhastha", "Simhastha Kumbh, Ujjain", "सिंहस्थ कुंभ, उज्जैन", "सिंहस्थ कुंभ, उज्जैन", ("Every 12 years", "हर 12 साल", "दर 12 वर्षांनी"),
             ("Great bathing fair on the Kshipra.", "क्षिप्रा पर विशाल स्नान पर्व।", "क्षिप्रेवरील महान स्नानपर्व.")),
        fest("bhagoria", "Bhagoria", "भगोरिया", "भगोरिया", ("Before Holi", "होली से पहले", "होळीपूर्वी"),
             ("Week of tribal haats, music and dance in Jhabua and Alirajpur.", "झाबुआ और अलीराजपुर में आदिवासी हाटों, संगीत और नृत्य का सप्ताह।", "झाबुआ व अलीराजपूरमध्ये आदिवासी बाजार, संगीत व नृत्याचा आठवडा.")),
        fest("khajuraho", "Khajuraho Dance Festival", "खजुराहो नृत्य महोत्सव", "खजुराहो नृत्य महोत्सव", ("February", "फ़रवरी", "फेब्रुवारी"),
             ("Classical dance against the temples.", "मंदिरों की पृष्ठभूमि में शास्त्रीय नृत्य।", "मंदिरांच्या पार्श्वभूमीवर अभिजात नृत्य.")),
        fest("tansen", "Tansen Samaroh, Gwalior", "तानसेन समारोह, ग्वालियर", "तानसेन समारोह, ग्वाल्हेर", ("December", "दिसंबर", "डिसेंबर"),
             ("Classical music festival at Tansen's tomb.", "तानसेन की समाधि पर शास्त्रीय संगीत उत्सव।", "तानसेनांच्या समाधीजवळ अभिजात संगीत महोत्सव.")),
        fest("navratri", "Navratri, Diwali and Holi", "नवरात्रि, दीवाली और होली", "नवरात्र, दिवाळी व होळी", ("Autumn; March", "शरद; मार्च", "शरद; मार्च"),
             ("Garba in Malwa; Rangpanchami processions in Indore.", "मालवा में गरबा; इंदौर में रंगपंचमी की गेर।", "माळव्यात गरबा; इंदूरमध्ये रंगपंचमीची गेर.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("gond", "Gond painting", "गोंड चित्रकला", "गोंड चित्रकला"), it3("pithora", "Pithora painting", "पिथौरा चित्रकला", "पिठोरा चित्रकला"), it3("gwalior", "Gwalior gharana", "ग्वालियर घराना", "ग्वाल्हेर घराणे"),
        it3("maihar", "Maihar gharana", "मैहर घराना", "मैहर घराणे"), it3("matki", "Matki dance", "मटकी नृत्य", "मटकी नृत्य"), it3("rai", "Rai dance", "राई नृत्य", "राई नृत्य"),
        it3("chanderi", "Chanderi weaving", "चंदेरी बुनाई", "चंदेरी विणकाम"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("poha", "Poha and jalebi", "पोहा और जलेबी", "पोहे व जिलेबी", d=("Indore's breakfast, topped with sev.", "इंदौर का नाश्ता, ऊपर सेव के साथ।", "इंदूरची न्याहारी, वर शेव.")),
        it3("dalbafla", "Dal bafla", "दाल बाफला", "दाल बाफला", d=("Malwa's boiled-then-baked wheat cakes with dal and ghee.", "मालवा के उबालकर सेंके गेहूँ के बाफले, दाल और घी के साथ।", "माळव्याचे उकडून भाजलेले गव्हाचे बाफले, डाळ व तुपासह.")),
        it3("bhutte", "Bhutte ka kees", "भुट्टे का कीस", "भुट्ट्याचा कीस", d=("Grated corn cooked with milk and spices.", "दूध और मसालों के साथ पकाया कसा हुआ भुट्टा।", "दूध व मसाल्यांसह शिजवलेला किसलेला मका.")),
        it3("biryani", "Bhopali biryani and korma", "भोपाली बिरयानी और क़ोरमा", "भोपाळी बिर्याणी व कोरमा", d=("Nawabi dishes of old Bhopal.", "पुराने भोपाल के नवाबी व्यंजन।", "जुन्या भोपाळचे नवाबी पदार्थ.")),
        it3("sev", "Ratlami sev", "रतलामी सेव", "रतलामी शेव", d=("Spiced gram-flour snack; a registered GI.", "मसालेदार बेसन का नमकीन; पंजीकृत जीआई।", "मसालेदार बेसनाचा फराळ; नोंदणीकृत जीआय.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("saree", "Chanderi and Maheshwari saris", "चंदेरी और महेश्वरी साड़ियाँ", "चंदेरी व महेश्वरी साड्या", d=("Light handloom silk-cotton saris.", "हल्की हथकरघा रेशम-सूती साड़ियाँ।", "हलक्या हातमाग रेशीम-सुती साड्या.")),
        it3("dhoti", "Dhoti, kurta and safa", "धोती, कुर्ता और साफ़ा", "धोतर, कुर्ता व फेटा", d=("Traditional men's dress in villages.", "गाँवों में पुरुषों की पारंपरिक पोशाक।", "गावांत पुरुषांचा पारंपरिक पोशाख.")),
        it3("tribal", "Tribal dress and silver jewellery", "आदिवासी पोशाक और चाँदी के गहने", "आदिवासी पोशाख व चांदीचे दागिने", d=("Worn by Bhil and Gond women at festivals.", "त्योहारों में भील और गोंड महिलाएँ पहनती हैं।", "सणांत भिल्ल व गोंड स्त्रिया परिधान करतात.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; mining = 100 * g["mining"] / g["total"]
module(R, "economy", [
    prose("p1", L(
        f"Madhya Pradesh's GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26 in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2025-26'][0])}, below the national average. Agriculture, livestock, forestry and fishing made up about {agri:.0f}% of GSVA in FY2024-25 — the highest share among the large States. The State leads India in soybean and grows wheat (including the prized Sharbati of Sehore), gram and other pulses, garlic, oranges and spices; irrigation has expanded fast in the last two decades. Mining and quarrying were about {mining:.1f}% of GSVA — coal at Singrauli, copper at Malanjkhand, manganese at Balaghat and India's only working diamond mine at Panna — and manufacturing about {mfg:.1f}%, in the Pithampur automobile cluster near Indore, Mandideep near Bhopal, cement at Satna and Katni, and food processing.\n\nThe PLFS unemployment rate was 1.5% in 2025, among the lowest in India, and labour-force participation was high (65.1% of persons aged 15 and above; 46.1% of women).",
        f"मोस्पी शृंखला में वित्त वर्ष 2025-26 में मध्य प्रदेश का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2025-26'][0])} था, जो राष्ट्रीय औसत से कम है। वित्त वर्ष 2024-25 में कृषि, पशुपालन, वानिकी और मत्स्य पालन जीएसवीए का लगभग {agri:.0f}% थे — बड़े राज्यों में सबसे ऊँचा हिस्सा। राज्य सोयाबीन में भारत में अग्रणी है और गेहूँ (सीहोर का प्रसिद्ध शरबती सहित), चना और अन्य दलहन, लहसुन, संतरे और मसाले उगाता है; पिछले दो दशकों में सिंचाई तेज़ी से बढ़ी है। खनन जीएसवीए का लगभग {mining:.1f}% था — सिंगरौली में कोयला, मलांजखंड में ताँबा, बालाघाट में मैंगनीज़ और पन्ना में भारत की एकमात्र चालू हीरा खदान — और विनिर्माण लगभग {mfg:.1f}%, इंदौर के पास पीथमपुर ऑटोमोबाइल क्लस्टर, भोपाल के पास मंडीदीप, सतना और कटनी में सीमेंट, और खाद्य प्रसंस्करण में।\n\n2025 में पीएलएफ़एस बेरोज़गारी दर 1.5% थी, जो भारत में सबसे कम में से है, और श्रम बल भागीदारी ऊँची थी (15 वर्ष से अधिक आयु के व्यक्तियों में 65.1%; महिलाओं में 46.1%)।",
        f"मोस्पी मालिकेनुसार आ.व. 2025-26 मध्ये मध्य प्रदेशचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2025-26'][0])} होते — राष्ट्रीय सरासरीपेक्षा कमी. आ.व. 2024-25 मध्ये शेती, पशुपालन, वनीकरण व मत्स्यव्यवसायाचा जीएसव्हीएमध्ये सुमारे {agri:.0f}% वाटा होता — मोठ्या राज्यांत सर्वाधिक. राज्य सोयाबीनमध्ये भारतात आघाडीवर आहे आणि गहू (सिहोरच्या प्रसिद्ध शरबतीसह), हरभरा व इतर कडधान्ये, लसूण, संत्री व मसाले पिकवते; गेल्या दोन दशकांत सिंचन झपाट्याने वाढले आहे. खाणकामाचा वाटा सुमारे {mining:.1f}% होता — सिंगरौलीत कोळसा, मलांजखंडमध्ये तांबे, बालाघाटमध्ये मँगनीज व पन्ना येथे भारतातील एकमेव कार्यरत हिऱ्याची खाण — आणि उत्पादन उद्योगाचा सुमारे {mfg:.1f}%, इंदूरजवळील पिथमपूर वाहन समूह, भोपाळजवळील मंडीदीप, सतना व कटनी येथे सिमेंट, आणि अन्नप्रक्रिया.\n\n2025 मध्ये पीएलएफएस बेरोजगारी दर 1.5% होता — भारतातील सर्वांत कमींपैकी — आणि श्रमशक्ती सहभाग जास्त होता (15 वर्षांवरील व्यक्तींमध्ये 65.1%; स्त्रियांमध्ये 46.1%)."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_MP), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_MP), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_MP), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("MP", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    plfs_series("MP", NAME),
    lst("sectors-key", [
        it3("soy", "Soybean and pulses", "सोयाबीन और दलहन", "सोयाबीन व कडधान्ये", d=("Malwa's black soils; soy processing around Indore.", "मालवा की काली मिट्टी; इंदौर के आसपास सोया प्रसंस्करण।", "माळव्याची काळी माती; इंदूरभोवती सोया प्रक्रिया.")),
        it3("wheat", "Wheat", "गेहूँ", "गहू", d=("Including Sharbati wheat of Sehore and Vidisha, a GI.", "सीहोर और विदिशा के शरबती गेहूँ सहित, जो जीआई है।", "सिहोर व विदिशाच्या शरबती गव्हासह, जे जीआय आहे.")),
        it3("minerals", "Coal, copper, manganese and diamonds", "कोयला, ताँबा, मैंगनीज़ और हीरे", "कोळसा, तांबे, मँगनीज व हिरे", d=("Singrauli, Malanjkhand, Balaghat and Panna.", "सिंगरौली, मलांजखंड, बालाघाट और पन्ना।", "सिंगरौली, मलांजखंड, बालाघाट व पन्ना.")),
        it3("auto", "Automobiles and engineering", "ऑटोमोबाइल और इंजीनियरिंग", "वाहन व अभियांत्रिकी", d=("Pithampur near Indore.", "इंदौर के पास पीथमपुर।", "इंदूरजवळील पिथमपूर.")),
        it3("cement", "Cement", "सीमेंट", "सिमेंट", d=("Satna, Katni and Neemuch.", "सतना, कटनी और नीमच।", "सतना, कटनी व नीमच.")),
        it3("tourism", "Wildlife and heritage tourism", "वन्यजीव और धरोहर पर्यटन", "वन्यजीव व वारसा पर्यटन", d=("Tiger reserves, Khajuraho, Ujjain and Omkareshwar.", "बाघ अभयारण्य, खजुराहो, उज्जैन और ओंकारेश्वर।", "व्याघ्र प्रकल्प, खजुराहो, उज्जैन व ओंकारेश्वर.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Crop production (soybean, wheat, gram)", "फ़सल उत्पादन (सोयाबीन, गेहूँ, चना)", "पीक उत्पादन (सोयाबीन, गहू, हरभरा)"), "india-gov", "State Economic Survey / Ministry of Agriculture."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("FDI equity inflows", "एफ़डीआई इक्विटी प्रवाह", "एफडीआय समभाग गुंतवणूक"), "dpiit", "DPIIT state-wise FDI factsheet."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Madhya Pradesh has a unicameral legislature: the 230-member Legislative Assembly meets in Bhopal. The State elects 29 members to the Lok Sabha and 11 to the Rajya Sabha.\n\nIn the Assembly election of November 2023 the BJP won 163 seats, the Congress 66 and the Bharat Adivasi Party 1 (ECI). Mohan Yadav was sworn in as Chief Minister on 13 December 2023, with Jagdish Devda and Rajendra Shukla as Deputy Chief Ministers, and former Union minister Narendra Singh Tomar was elected Speaker. Mangubhai C. Patel has been Governor since July 2021.",
        "मध्य प्रदेश में एकसदनीय विधानमंडल है: 230 सदस्यों वाली विधानसभा भोपाल में बैठती है। राज्य से लोकसभा के 29 और राज्यसभा के 11 सदस्य चुने जाते हैं।\n\nनवंबर 2023 के विधानसभा चुनाव में भाजपा ने 163, कांग्रेस ने 66 और भारत आदिवासी पार्टी ने 1 सीट जीती (भारत निर्वाचन आयोग)। मोहन यादव ने 13 दिसंबर 2023 को मुख्यमंत्री पद की शपथ ली, जगदीश देवड़ा और राजेंद्र शुक्ल उपमुख्यमंत्री बने, और पूर्व केंद्रीय मंत्री नरेंद्र सिंह तोमर अध्यक्ष चुने गए। मंगुभाई छ. पटेल जुलाई 2021 से राज्यपाल हैं।",
        "मध्य प्रदेशात एकसदनी विधिमंडळ आहे: 230 सदस्यांची विधानसभा भोपाळमध्ये भरते. राज्यातून लोकसभेवर 29 आणि राज्यसभेवर 11 सदस्य निवडले जातात.\n\nनोव्हेंबर 2023 च्या विधानसभा निवडणुकीत भाजपने 163, काँग्रेसने 66 व भारत आदिवासी पक्षाने 1 जागा जिंकली (भारत निवडणूक आयोग). मोहन यादव यांनी 13 डिसेंबर 2023 रोजी मुख्यमंत्रिपदाची शपथ घेतली, जगदीश देवडा व राजेंद्र शुक्ला उपमुख्यमंत्री झाले, आणि माजी केंद्रीय मंत्री नरेंद्रसिंह तोमर अध्यक्षपदी निवडले गेले. मंगूभाई छ. पटेल जुलै 2021 पासून राज्यपाल आहेत."),
        sources=["eci", "scroll", "fpj"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    table("result2023", L("Assembly election 2023 — seats won", "विधानसभा चुनाव 2023 — जीती गई सीटें", "विधानसभा निवडणूक 2023 — जिंकलेल्या जागा"),
          [col(L("Party", "दल", "पक्ष")), col(L("Seats", "सीटें", "जागा"), "right")],
          [[L("Bharatiya Janata Party", "भारतीय जनता पार्टी", "भारतीय जनता पक्ष"), "163"], [L("Indian National Congress", "भारतीय राष्ट्रीय कांग्रेस", "भारतीय राष्ट्रीय काँग्रेस"), "66"],
           [L("Bharat Adivasi Party", "भारत आदिवासी पार्टी", "भारत आदिवासी पक्ष"), "1"], [L("Total", "कुल", "एकूण"), "230"]],
          "eci", ECI, period="2023",
          note=L("ECI results website, December 2023. Later by-elections and defections are not reflected.", "भारत निर्वाचन आयोग की परिणाम वेबसाइट, दिसंबर 2023। बाद के उपचुनाव और दलबदल शामिल नहीं।", "भारत निवडणूक आयोगाचे निकाल संकेतस्थळ, डिसेंबर 2023. नंतरच्या पोटनिवडणुका व पक्षांतरे समाविष्ट नाहीत.")),
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("assembly", "Madhya Pradesh Vidhan Sabha", "मध्य प्रदेश विधानसभा", "मध्य प्रदेश विधानसभा", url="https://mpvidhansabha.nic.in", src="india-gov"),
        it3("portal", "Government of Madhya Pradesh", "मध्य प्रदेश सरकार", "मध्य प्रदेश शासन", url="https://www.mp.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Leader of Opposition — official notice", "नेता प्रतिपक्ष — आधिकारिक सूचना", "विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "Assembly secretariat."),
        (L("Local bodies by type", "प्रकार के अनुसार स्थानीय निकाय", "प्रकारानुसार स्थानिक स्वराज्य संस्था"), "india-gov", "Panchayat and Rural Development and Urban Development departments."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "The Ken–Betwa link, the first project of India's national river-linking plan, is being built to carry water to drought-prone Bundelkhand. Bhopal's metro opened its first stretch in December 2025, joining Indore, whose first metro section opened in May 2025. The Ramjal Setu link with Rajasthan is listed on the Rajasthan page. Each card shows its source and the date it was checked.",
        "भारत की राष्ट्रीय नदी-जोड़ योजना की पहली परियोजना, केन–बेतवा लिंक, सूखाग्रस्त बुंदेलखंड तक पानी पहुँचाने के लिए बन रही है। भोपाल मेट्रो का पहला खंड दिसंबर 2025 में खुला, और इंदौर में पहला मेट्रो खंड मई 2025 में खुला था। राजस्थान के साथ रामजल सेतु लिंक राजस्थान पृष्ठ पर है। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "भारताच्या राष्ट्रीय नदीजोड योजनेतील पहिला प्रकल्प, केन–बेतवा जोड, दुष्काळग्रस्त बुंदेलखंडपर्यंत पाणी पोहोचवण्यासाठी उभारला जात आहे. भोपाळ मेट्रोचा पहिला टप्पा डिसेंबर 2025 मध्ये सुरू झाला, आणि इंदूरमध्ये पहिला मेट्रो टप्पा मे 2025 मध्ये सुरू झाला होता. राजस्थानसोबतचा रामजल सेतू जोड प्रकल्प राजस्थानच्या पानावर आहे. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["newsonair"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Indore Metro — official status", "इंदौर मेट्रो — आधिकारिक स्थिति", "इंदूर मेट्रो — अधिकृत स्थिती"), "india-gov", "Madhya Pradesh Metro Rail Corporation / MoHUA."),
        (L("Ken–Betwa — physical progress", "केन–बेतवा — भौतिक प्रगति", "केन–बेतवा — भौतिक प्रगती"), "india-gov", "Ministry of Jal Shakti."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "At the centre of India, Madhya Pradesh is crossed by the main north–south and east–west rail lines; Itarsi, Bina and Katni are major junctions, and Jabalpur is the headquarters of the West Central Railway. National Highway 44, India's longest, runs north–south through Gwalior and Sagar. Indore's Devi Ahilyabai Holkar Airport is the busiest, followed by Bhopal's Raja Bhoj Airport; Jabalpur, Gwalior, Khajuraho and Rewa also have airports. Bhopal and Indore have new metro lines.",
        "भारत के केंद्र में स्थित मध्य प्रदेश को मुख्य उत्तर–दक्षिण और पूर्व–पश्चिम रेल लाइनें पार करती हैं; इटारसी, बीना और कटनी बड़े जंक्शन हैं, और जबलपुर पश्चिम मध्य रेलवे का मुख्यालय है। भारत का सबसे लंबा राष्ट्रीय राजमार्ग 44 ग्वालियर और सागर से होकर उत्तर–दक्षिण जाता है। इंदौर का देवी अहिल्याबाई होलकर हवाई अड्डा सबसे व्यस्त है, उसके बाद भोपाल का राजा भोज हवाई अड्डा; जबलपुर, ग्वालियर, खजुराहो और रीवा में भी हवाई अड्डे हैं। भोपाल और इंदौर में नई मेट्रो लाइनें हैं।",
        "भारताच्या केंद्रस्थानी असलेल्या मध्य प्रदेशातून मुख्य उत्तर–दक्षिण व पूर्व–पश्चिम रेल्वेमार्ग जातात; इटारसी, बीना व कटनी ही मोठी जंक्शन आहेत, आणि जबलपूर हे पश्चिम मध्य रेल्वेचे मुख्यालय आहे. भारतातील सर्वांत लांब राष्ट्रीय महामार्ग 44 ग्वाल्हेर व सागरमार्गे उत्तर–दक्षिण जातो. इंदूरचे देवी अहिल्याबाई होळकर विमानतळ सर्वांत व्यस्त आहे, त्यानंतर भोपाळचे राजा भोज विमानतळ; जबलपूर, ग्वाल्हेर, खजुराहो व रीवा येथेही विमानतळ आहेत. भोपाळ व इंदूरमध्ये नव्या मेट्रो मार्गिका आहेत."),
        conf="Editorial"),
    lst("airports", [
        it3("idr", "Devi Ahilyabai Holkar Airport, Indore", "देवी अहिल्याबाई होलकर हवाई अड्डा, इंदौर", "देवी अहिल्याबाई होळकर विमानतळ, इंदूर", m=("IDR", "IDR", "IDR")),
        it3("bho", "Raja Bhoj Airport, Bhopal", "राजा भोज हवाई अड्डा, भोपाल", "राजा भोज विमानतळ, भोपाळ", m=("BHO", "BHO", "BHO")),
        it3("jlr", "Jabalpur (Dumna)", "जबलपुर (डुमना)", "जबलपूर (डुमना)", m=("JLR", "JLR", "JLR")),
        it3("gwl", "Gwalior (Rajmata Vijaya Raje Scindia)", "ग्वालियर (राजमाता विजयाराजे सिंधिया)", "ग्वाल्हेर (राजमाता विजयाराजे शिंदे)", m=("GWL", "GWL", "GWL")),
        it3("hjr", "Khajuraho", "खजुराहो", "खजुराहो", m=("HJR", "HJR", "HJR")),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Singrauli, on the border with Uttar Pradesh, is one of India's great power hubs, with NTPC's Vindhyachal station and the Sasan ultra mega power project burning local coal. State plants at Satpura (Sarni), Amarkantak, Birsinghpur and Shree Singaji add more. The Narmada dams at Indira Sagar, Omkareshwar and Bargi generate hydro power, and Omkareshwar also has one of India's largest floating solar plants. The Rewa ultra mega solar park supplies power to the Delhi Metro, and new solar parks are coming up in Agar, Shajapur, Neemuch and Morena.",
        "उत्तर प्रदेश की सीमा पर सिंगरौली भारत के बड़े बिजली केंद्रों में है, जहाँ एनटीपीसी का विंध्याचल संयंत्र और सासन अल्ट्रा मेगा पावर परियोजना स्थानीय कोयले से चलते हैं। सतपुड़ा (सारणी), अमरकंटक, बिरसिंहपुर और श्री सिंगाजी के राज्य संयंत्र और जोड़ते हैं। इंदिरा सागर, ओंकारेश्वर और बरगी पर नर्मदा के बाँध जलविद्युत बनाते हैं, और ओंकारेश्वर में भारत के सबसे बड़े तैरते सौर संयंत्रों में से एक भी है। रीवा अल्ट्रा मेगा सौर पार्क दिल्ली मेट्रो को बिजली देता है, और आगर, शाजापुर, नीमच और मुरैना में नए सौर पार्क बन रहे हैं।",
        "उत्तर प्रदेशच्या सीमेवरील सिंगरौली हे भारतातील मोठ्या वीज केंद्रांपैकी आहे, जिथे एनटीपीसीचे विंध्याचल केंद्र व सासन अल्ट्रा मेगा वीज प्रकल्प स्थानिक कोळशावर चालतात. सातपुडा (सारणी), अमरकंटक, बिरसिंहपूर व श्री सिंगाजी येथील राज्याची केंद्रे भर घालतात. इंदिरा सागर, ओंकारेश्वर व बरगी येथील नर्मदेवरील धरणे जलविद्युत निर्माण करतात, आणि ओंकारेश्वर येथे भारतातील सर्वांत मोठ्या तरंगत्या सौर प्रकल्पांपैकी एकही आहे. रीवा अल्ट्रा मेगा सौर उद्यान दिल्ली मेट्रोला वीज पुरवते, आणि आगर, शाजापूर, नीमच व मुरैना येथे नवी सौर उद्याने उभी राहत आहेत."),
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
        "Indore is the State's IT centre, with special economic zones and campuses of large Indian IT companies along the Super Corridor and at Crystal IT Park. Bhopal and Jabalpur have smaller clusters and growing start-up activity, supported by the State's start-up policy and incubators at IIT Indore, IIM Indore and IISER Bhopal.",
        "इंदौर राज्य का आईटी केंद्र है, जहाँ सुपर कॉरिडोर और क्रिस्टल आईटी पार्क में विशेष आर्थिक क्षेत्र और बड़ी भारतीय आईटी कंपनियों के परिसर हैं। भोपाल और जबलपुर में छोटे क्लस्टर और बढ़ती स्टार्टअप गतिविधि है, जिसे राज्य की स्टार्टअप नीति और आईआईटी इंदौर, आईआईएम इंदौर व आईआईएसईआर भोपाल के इनक्यूबेटर सहारा देते हैं।",
        "इंदूर हे राज्याचे आयटी केंद्र आहे, जिथे सुपर कॉरिडॉर व क्रिस्टल आयटी पार्क येथे विशेष आर्थिक क्षेत्रे व मोठ्या भारतीय आयटी कंपन्यांची संकुले आहेत. भोपाळ व जबलपूरमध्ये लहान समूह व वाढती स्टार्टअप हालचाल आहे, जिला राज्याचे स्टार्टअप धोरण व आयआयटी इंदूर, आयआयएम इंदूर व आयसर भोपाळ येथील इन्क्युबेटर्सचा आधार आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Madhya Pradesh circle, which includes Chhattisgarh)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("MP", NAME)
module(R, "education", [
    prose("p1", L(
        "Madhya Pradesh's higher-education gross enrolment ratio (ages 18–23) was 28.9% in 2021-22 in AISHE, slightly above the national 28.4% and up from 20.2% in 2017-18; men's GER (29.7%) was a little above women's (28.0%). The State had 77 universities and 2,742 colleges. Literacy at the 2011 Census was 69.3%.\n\nNational institutions include IIT Indore, IIM Indore, AIIMS Bhopal, IISER Bhopal, MANIT Bhopal, the National Law Institute University in Bhopal, IIITDM Jabalpur and ABV-IIITM Gwalior. Dr Harisingh Gour University at Sagar (1946) and Rani Durgavati University at Jabalpur are among the older universities.",
        "एआईएसएचई के अनुसार 2021-22 में मध्य प्रदेश का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) 28.9% था, जो राष्ट्रीय 28.4% से थोड़ा अधिक और 2017-18 के 20.2% से ऊपर है; पुरुषों का जीईआर (29.7%) महिलाओं (28.0%) से थोड़ा अधिक था। राज्य में 77 विश्वविद्यालय और 2,742 कॉलेज थे। 2011 की जनगणना में साक्षरता 69.3% थी।\n\nराष्ट्रीय संस्थानों में आईआईटी इंदौर, आईआईएम इंदौर, एम्स भोपाल, आईआईएसईआर भोपाल, मैनिट भोपाल, भोपाल का राष्ट्रीय विधि संस्थान विश्वविद्यालय, आईआईआईटीडीएम जबलपुर और एबीवी-आईआईआईटीएम ग्वालियर शामिल हैं। सागर का डॉ. हरिसिंह गौर विश्वविद्यालय (1946) और जबलपुर का रानी दुर्गावती विश्वविद्यालय पुराने विश्वविद्यालयों में हैं।",
        "एआयएसएचईनुसार 2021-22 मध्ये मध्य प्रदेशचे उच्चशिक्षणातील एकूण नोंदणी गुणोत्तर (18–23 वय) 28.9% होते — राष्ट्रीय 28.4% पेक्षा किंचित जास्त व 2017-18 च्या 20.2% पेक्षा अधिक; पुरुषांचे जीईआर (29.7%) स्त्रियांपेक्षा (28.0%) किंचित जास्त होते. राज्यात 77 विद्यापीठे व 2,742 महाविद्यालये होती. 2011 च्या जनगणनेत साक्षरता 69.3% होती.\n\nराष्ट्रीय संस्थांत आयआयटी इंदूर, आयआयएम इंदूर, एम्स भोपाळ, आयसर भोपाळ, मॅनिट भोपाळ, भोपाळचे राष्ट्रीय विधी संस्था विद्यापीठ, आयआयआयटीडीएम जबलपूर व एबीव्ही-आयआयआयटीएम ग्वाल्हेर यांचा समावेश आहे. सागरचे डॉ. हरिसिंह गौर विद्यापीठ (1946) व जबलपूरचे राणी दुर्गावती विद्यापीठ ही जुन्या विद्यापीठांपैकी आहेत."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("iiti", "IIT Indore", "आईआईटी इंदौर", "आयआयटी इंदूर", m=("Indore", "इंदौर", "इंदूर")),
        it3("iimi", "IIM Indore", "आईआईएम इंदौर", "आयआयएम इंदूर", m=("Indore", "इंदौर", "इंदूर")),
        it3("aiimsb", "AIIMS Bhopal", "एम्स भोपाल", "एम्स भोपाळ", m=("Bhopal", "भोपाल", "भोपाळ")),
        it3("iiserb", "IISER Bhopal", "आईआईएसईआर भोपाल", "आयसर भोपाळ", m=("Bhopal", "भोपाल", "भोपाळ")),
        it3("nliu", "National Law Institute University", "राष्ट्रीय विधि संस्थान विश्वविद्यालय", "राष्ट्रीय विधी संस्था विद्यापीठ", m=("Bhopal", "भोपाल", "भोपाळ")),
        it3("hgu", "Dr Harisingh Gour University", "डॉ. हरिसिंह गौर विश्वविद्यालय", "डॉ. हरिसिंह गौर विद्यापीठ", m=("Sagar, 1946", "सागर, 1946", "सागर, 1946")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("NIRF-ranked institutions", "एनआईआरएफ़ रैंक वाले संस्थान", "एनआयआरएफ क्रमवारीतील संस्था"), "nirf", "Latest NIRF list filtered to Madhya Pradesh."),
    ]),
])

# ---------------- O. Health ----------------
module(R, "health", [
    prose("p1", L(
        "Madhya Pradesh has made progress but still has some of India's weakest mortality indicators. The infant mortality rate fell from 62 per 1,000 live births in 2010 to 43 in 2020, but this was the highest of any State that year (India 28). Life expectancy at birth was 66.5 years in 2014-18 (men 64.8, women 68.5), below the national 69.4. Child nutrition improved between NFHS-4 and NFHS-5 — stunting fell from 42.0% to 35.7% and underweight from 42.8% to 33.0% — and 90.7% of births took place in health facilities.\n\nAIIMS Bhopal and the government medical colleges at Bhopal, Indore (M.Y. Hospital), Jabalpur and Gwalior are the main referral centres.",
        "मध्य प्रदेश ने प्रगति की है, लेकिन यहाँ अब भी भारत के कुछ सबसे कमज़ोर मृत्यु संकेतक हैं। शिशु मृत्यु दर 2010 में प्रति 1,000 जीवित जन्म पर 62 से घटकर 2020 में 43 हो गई, लेकिन उस वर्ष यह किसी भी राज्य में सबसे अधिक थी (भारत 28)। 2014-18 में जन्म के समय जीवन प्रत्याशा 66.5 वर्ष (पुरुष 64.8, महिलाएँ 68.5) थी, जो राष्ट्रीय 69.4 से कम है। एनएफ़एचएस-4 और एनएफ़एचएस-5 के बीच बाल पोषण सुधरा — ठिगनापन 42.0% से 35.7% और कम वज़न 42.8% से 33.0% पर आया — और 90.7% प्रसव स्वास्थ्य संस्थानों में हुए।\n\nएम्स भोपाल और भोपाल, इंदौर (एम.वाई. अस्पताल), जबलपुर और ग्वालियर के सरकारी मेडिकल कॉलेज मुख्य रेफ़रल केंद्र हैं।",
        "मध्य प्रदेशने प्रगती केली आहे, पण इथे अजूनही भारतातील काही सर्वांत कमकुवत मृत्युदर निर्देशक आहेत. अर्भक मृत्युदर 2010 मध्ये दर 1,000 जिवंत जन्मांमागे 62 वरून 2020 मध्ये 43 वर आला, पण त्या वर्षी तो कोणत्याही राज्यात सर्वाधिक होता (भारत 28). 2014-18 मध्ये जन्मतः आयुर्मान 66.5 वर्षे (पुरुष 64.8, स्त्रिया 68.5) होते, राष्ट्रीय 69.4 पेक्षा कमी. एनएफएचएस-4 ते एनएफएचएस-5 दरम्यान बालपोषण सुधारले — खुजेपणा 42.0% वरून 35.7% व कमी वजन 42.8% वरून 33.0% — आणि 90.7% प्रसूती आरोग्य संस्थांत झाल्या.\n\nएम्स भोपाळ आणि भोपाळ, इंदूर (एम.वाय. रुग्णालय), जबलपूर व ग्वाल्हेरची शासकीय वैद्यकीय महाविद्यालये ही मुख्य संदर्भ केंद्रे आहेत."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(43, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(62, "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(24.1, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020 (death rate 6.5); 27.3 in 2010."), "number",
             previous=dp(27.3, "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(66.5, "years", "2014-18", "survey", "srs", ESI_LE, note="SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male 64.8, female 68.5)."), "number", "higher-is-better",
             national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("MP"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin; the PIB summary used here lists only States that met the SDG target."),
        (L("Under-five mortality rate (SRS 2021)", "पाँच वर्ष से कम आयु की मृत्यु दर (एसआरएस 2021)", "पाच वर्षांखालील मृत्युदर (एसआरएस 2021)"), "srs", "SRS Statistical Report 2021."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("mp mod2 ok")
