"""Odisha modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-OR"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
CM = "https://newsonair.gov.in/odisha-bjp-to-form-government-as-mohan-charan-majhi-sworn-in-as-cm-ending-24-year-bjd-rule"
NOTE_OR = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 16 Oct 2026. "
           "FY2025-26 is the latest year published for Odisha and may be revised.")
mo = research("mospi_or.json")
NAME = L("Odisha", "ओडिशा", "ओडिशा")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Odisha's culture centres on the worship of Jagannath, whose temple at Puri shaped the State's music, dance, painting and food. Odissi dance grew from the temple dancers (maharis) and the boy dancers (gotipuas), and was revived in the 20th century by gurus such as Kelucharan Mohapatra. Jayadeva's Sanskrit Gita Govinda, sung in the Puri temple, inspired Odissi music. Odia literature runs from Sarala Das's Mahabharata in the 15th century to Fakir Mohan Senapati, the father of modern Odia fiction, and Jnanpith winners such as Gopinath Mohanty and Sitakant Mahapatra.\n\nPattachitra cloth painting and palm-leaf engraving come from Raghurajpur near Puri; Pipli is known for appliqué, Cuttack for silver filigree (tarakasi), and western Odisha for Sambalpuri, Bomkai and other ikat saris. Tribal communities keep their own arts, such as Saura wall paintings (idital) and Dongria Kondh embroidered shawls.",
        "ओडिशा की संस्कृति जगन्नाथ की उपासना पर केंद्रित है, जिनके पुरी मंदिर ने राज्य के संगीत, नृत्य, चित्रकला और भोजन को आकार दिया। ओडिसी नृत्य मंदिर की नर्तकियों (महारी) और बाल नर्तकों (गोटीपुआ) से विकसित हुआ, और 20वीं सदी में केलुचरण महापात्र जैसे गुरुओं ने इसे पुनर्जीवित किया। पुरी मंदिर में गाए जाने वाले जयदेव के संस्कृत गीतगोविंद ने ओडिसी संगीत को प्रेरित किया। ओड़िया साहित्य 15वीं सदी के सारला दास के महाभारत से लेकर आधुनिक ओड़िया कथा के जनक फ़कीर मोहन सेनापति और गोपीनाथ महांती व सीताकांत महापात्र जैसे ज्ञानपीठ विजेताओं तक फैला है।\n\nपट्टचित्र वस्त्र चित्रकला और ताड़पत्र नक्काशी पुरी के पास रघुराजपुर से आती है; पिपली एप्लिक के लिए, कटक चाँदी की तारकशी के लिए, और पश्चिमी ओडिशा संबलपुरी, बोमकाई और अन्य इकत साड़ियों के लिए प्रसिद्ध है। जनजातीय समुदाय अपनी कलाएँ सँजोए हुए हैं, जैसे सौरा भित्ति चित्र (इडिताल) और डोंगरिया कोंध की कढ़ाई वाली शॉल।",
        "ओडिशाची संस्कृती जगन्नाथाच्या उपासनेभोवती केंद्रित आहे, ज्यांच्या पुरीतील मंदिराने राज्याचे संगीत, नृत्य, चित्रकला व खाद्यसंस्कृती घडवली. ओडिसी नृत्य मंदिरातील नर्तकी (महारी) व बाल नर्तक (गोटीपुआ) यांच्यातून विकसित झाले, आणि विसाव्या शतकात केलुचरण महापात्र यांसारख्या गुरूंनी त्याचे पुनरुज्जीवन केले. पुरीच्या मंदिरात गायल्या जाणाऱ्या जयदेवाच्या संस्कृत गीतगोविंदाने ओडिसी संगीताला प्रेरणा दिली. ओडिया साहित्य पंधराव्या शतकातील सारला दासांच्या महाभारतापासून आधुनिक ओडिया कथेचे जनक फकीर मोहन सेनापती आणि गोपीनाथ महांती व सीताकांत महापात्र यांसारख्या ज्ञानपीठ विजेत्यांपर्यंत पसरले आहे.\n\nपट्टचित्र वस्त्रचित्रकला व ताडपत्री कोरीवकाम पुरीजवळील रघुराजपूरमधून येते; पिपली ऍप्लिकसाठी, कटक चांदीच्या जाळीकामासाठी (तारकशी), आणि पश्चिम ओडिशा संबलपुरी, बोमकाई व इतर इकत साड्यांसाठी प्रसिद्ध आहे. आदिवासी समुदाय आपल्या कला जपतात, जसे सौरा भित्तिचित्रे (इडिताल) व डोंगरिया कोंधांच्या भरतकाम केलेल्या शाली."),
        conf="Editorial"),
    lst("festivals", [
        fest("rath", "Rath Yatra", "रथयात्रा", "रथयात्रा", ("June–July (Ashadha)", "जून–जुलाई (आषाढ़)", "जून–जुलै (आषाढ)"),
             ("Jagannath, Balabhadra and Subhadra ride giant wooden chariots from the Puri temple to the Gundicha temple.", "जगन्नाथ, बलभद्र और सुभद्रा विशाल लकड़ी के रथों पर पुरी मंदिर से गुंडिचा मंदिर जाते हैं।", "जगन्नाथ, बलभद्र व सुभद्रा प्रचंड लाकडी रथांतून पुरी मंदिरापासून गुंडिचा मंदिरापर्यंत जातात.")),
        fest("raja", "Raja Parba", "रज पर्व", "रज पर्व", ("Mid-June", "मध्य जून", "जूनच्या मध्यात"),
             ("Three-day festival celebrating the earth and womanhood at the onset of the monsoon; swings and pitha.", "मानसून की शुरुआत में धरती और नारीत्व का तीन दिन का उत्सव; झूले और पीठा।", "मान्सूनच्या प्रारंभी पृथ्वी व स्त्रीत्वाचा तीन दिवसांचा उत्सव; झोके व पिठा.")),
        fest("nuakhai", "Nuakhai", "नुआखाई", "नुआखाई", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Western Odisha's harvest festival of the new rice, offered first to the goddess Samaleswari.", "नए धान का पश्चिमी ओडिशा का फ़सल उत्सव, पहले देवी समलेश्वरी को अर्पित।", "नव्या भाताचा पश्चिम ओडिशाचा सुगीचा सण, प्रथम देवी समलेश्वरीला अर्पण.")),
        fest("durga", "Durga Puja", "दुर्गा पूजा", "दुर्गापूजा", ("September–October", "सितंबर–अक्टूबर", "सप्टेंबर–ऑक्टोबर"),
             ("Cuttack's pandals are famous for silver filigree decorations.", "कटक के पंडाल चाँदी की तारकशी की सजावट के लिए प्रसिद्ध हैं।", "कटकचे मंडप चांदीच्या जाळीकामाच्या सजावटीसाठी प्रसिद्ध आहेत.")),
        fest("bali", "Bali Jatra", "बाली जात्रा", "बाली जात्रा", ("November (Kartik Purnima)", "नवंबर (कार्तिक पूर्णिमा)", "नोव्हेंबर (कार्तिक पौर्णिमा)"),
             ("Cuttack fair recalling Kalinga's sea voyages to Bali and South-East Asia; boats are floated at dawn (boita bandana).", "बाली और दक्षिण-पूर्व एशिया तक कलिंग की समुद्री यात्राओं की याद में कटक का मेला; भोर में नावें बहाई जाती हैं (बोइत बंदाण)।", "बाली व आग्नेय आशियापर्यंतच्या कलिंगच्या सागरी सफरींच्या स्मृतीत कटकची जत्रा; पहाटे होड्या सोडल्या जातात (बोइत बंदाण).")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("odissi", "Odissi dance", "ओडिसी नृत्य", "ओडिसी नृत्य"), it3("gotipua", "Gotipua", "गोटीपुआ", "गोटीपुआ"),
        it3("patta", "Pattachitra", "पट्टचित्र", "पट्टचित्र"), it3("tarakasi", "Silver filigree (tarakasi)", "चाँदी की तारकशी", "चांदीचे जाळीकाम (तारकशी)"),
        it3("applique", "Pipli appliqué", "पिपली एप्लिक", "पिपली ऍप्लिक"), it3("sambalpuri", "Sambalpuri ikat", "संबलपुरी इकत", "संबलपुरी इकत"),
        it3("chhau", "Mayurbhanj Chhau", "मयूरभंज छऊ", "मयूरभंज छाऊ"), it3("dalkhai", "Dalkhai dance", "डालखाई नृत्य", "डालखाई नृत्य"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("pakhala", "Pakhala", "पखाल", "पखाल", d=("Cooked rice soaked in water, often fermented, with fried vegetables and fish; a summer staple.", "पानी में भिगोया पका भात, अक्सर ख़मीरी, तली सब्ज़ियों और मछली के साथ; गर्मियों का मुख्य भोजन।", "पाण्यात भिजवलेला शिजवलेला भात, अनेकदा आंबवलेला, तळलेल्या भाज्या व माशांसह; उन्हाळ्याचे मुख्य अन्न.")),
        it3("dalma", "Dalma", "दालमा", "दालमा", d=("Lentils cooked with vegetables; part of the temple's offerings.", "सब्ज़ियों के साथ पकी दाल; मंदिर के भोग का हिस्सा।", "भाज्यांसह शिजवलेली डाळ; मंदिराच्या नैवेद्याचा भाग.")),
        it3("chhenapoda", "Chhena poda", "छेना पोड़ा", "छेना पोडा", d=("Baked cottage-cheese sweet from Nayagarh.", "नयागढ़ की सेंकी हुई छेना मिठाई।", "नयागडची भाजलेली छेन्याची मिठाई.")),
        it3("rasagola", "Odisha Rasagola", "ओडिशा रसगोला", "ओडिशा रसगोला", d=("Soft cheese balls in syrup; a registered GI.", "चाशनी में नरम छेने के गोले; पंजीकृत जीआई।", "पाकातील मऊ छेन्याचे गोळे; नोंदणीकृत जीआय.")),
        it3("rasabali", "Kendrapara rasabali", "केंद्रापाड़ा रसाबली", "केंद्रापाडा रसाबली", d=("Fried cheese patties in thickened milk; a registered GI.", "गाढ़े दूध में तली छेना टिकिया; पंजीकृत जीआई।", "आटवलेल्या दुधातील तळलेल्या छेन्याच्या चकत्या; नोंदणीकृत जीआय.")),
        it3("machha", "Machha jhola", "माछ झोल", "माछ झोल", d=("Light fish curry eaten along the coast.", "तट पर खाई जाने वाली हल्की मछली करी।", "किनाऱ्यावर खाल्ली जाणारी हलकी माशांची आमटी.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("saree", "Sambalpuri, Bomkai and Khandua saris", "संबलपुरी, बोमकाई और खंडुआ साड़ियाँ", "संबलपुरी, बोमकाई व खंडुआ साड्या", d=("Handwoven ikat saris worn for festivals and weddings.", "त्योहारों और विवाहों में पहनी जाने वाली हाथ से बुनी इकत साड़ियाँ।", "सण व लग्नांत नेसल्या जाणाऱ्या हातमागावरील इकत साड्या.")),
        it3("dhoti", "Dhoti, kurta and gamuchha", "धोती, कुर्ता और गामुछा", "धोतर, कुर्ता व गामुछा", d=("Everyday men's dress in villages.", "गाँवों में पुरुषों की रोज़ की पोशाक।", "गावांत पुरुषांचा रोजचा पोशाख.")),
        it3("kapadaganda", "Kapadaganda shawl", "कपड़गंडा शॉल", "कपडगंडा शाल", d=("Embroidered shawl of the Dongria Kondh of the Niyamgiri hills.", "नियमगिरि पहाड़ियों के डोंगरिया कोंध की कढ़ाईदार शॉल।", "नियमगिरी डोंगरांतील डोंगरिया कोंधांची भरतकाम केलेली शाल.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; mine = 100 * g["mining"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["OR"]; lf = AP["plfs_lfpr_2025"]["OR"]
module(R, "economy", [
    prose("p1", L(
        f"Odisha's GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26 in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2025-26'][0])}. Its economy is unusually dependent on minerals and heavy industry: in FY2024-25 mining made up about {mine:.0f}% of GSVA and manufacturing about {mfg:.0f}%, while agriculture, livestock and fishing contributed about {agri:.0f}%. Odisha has large reserves of iron ore, bauxite, chromite and coal, and the steel plants of Rourkela, Kalinganagar and Angul, the aluminium smelters and refineries of Angul, Jharsuguda and Damanjodi, and the refinery at Paradip process them. Paradip is one of India's busiest ports. Most rural families still farm, mainly paddy, and coastal fisheries and prawn farming are important.\n\nThe PLFS unemployment rate fell from {ur['2022']}% in 2022 to {ur['2025']}% in 2025, and {lf['female']}% of women aged 15 and above were in the labour force in 2025.",
        f"मोस्पी शृंखला में वित्त वर्ष 2025-26 में ओडिशा का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2025-26'][0])}। इसकी अर्थव्यवस्था खनिजों और भारी उद्योग पर असामान्य रूप से निर्भर है: वित्त वर्ष 2024-25 में खनन जीएसवीए का लगभग {mine:.0f}% और विनिर्माण लगभग {mfg:.0f}% था, जबकि कृषि, पशुपालन और मत्स्य पालन का योगदान लगभग {agri:.0f}% था। ओडिशा में लौह अयस्क, बॉक्साइट, क्रोमाइट और कोयले के बड़े भंडार हैं, और राउरकेला, कलिंगनगर और अंगुल के इस्पात संयंत्र, अंगुल, झारसुगुड़ा और दामनजोड़ी के एल्युमिनियम स्मेल्टर व रिफ़ाइनरियाँ और पारादीप की तेल रिफ़ाइनरी इनका प्रसंस्करण करते हैं। पारादीप भारत के सबसे व्यस्त बंदरगाहों में से है। अधिकांश ग्रामीण परिवार अब भी खेती करते हैं, मुख्यतः धान की, और तटीय मत्स्य पालन व झींगा पालन महत्त्वपूर्ण हैं।\n\nपीएलएफ़एस बेरोज़गारी दर 2022 के {ur['2022']}% से घटकर 2025 में {ur['2025']}% रह गई, और 2025 में 15 वर्ष से अधिक आयु की {lf['female']}% महिलाएँ श्रम बल में थीं।",
        f"मोस्पी मालिकेनुसार आ.व. 2025-26 मध्ये ओडिशाचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2025-26'][0])}. त्याची अर्थव्यवस्था खनिजे व अवजड उद्योगांवर असामान्यपणे अवलंबून आहे: आ.व. 2024-25 मध्ये खाणकामाचा जीएसव्हीएमध्ये सुमारे {mine:.0f}% व उत्पादन उद्योगाचा सुमारे {mfg:.0f}% वाटा होता, तर शेती, पशुपालन व मत्स्यव्यवसायाचा सुमारे {agri:.0f}%. ओडिशात लोहखनिज, बॉक्साइट, क्रोमाइट व कोळशाचे मोठे साठे आहेत, आणि राउरकेला, कलिंगनगर व अंगुलचे पोलाद कारखाने, अंगुल, झारसुगुडा व दामनजोडीचे ॲल्युमिनियम स्मेल्टर व शुद्धीकरण कारखाने आणि पारादीपची तेल रिफायनरी त्यांच्यावर प्रक्रिया करतात. पारादीप हे भारतातील सर्वांत व्यस्त बंदरांपैकी एक आहे. बहुतेक ग्रामीण कुटुंबे अजूनही शेती करतात, मुख्यतः भाताची, आणि किनारी मत्स्यव्यवसाय व कोळंबीपालन महत्त्वाचे आहे.\n\nपीएलएफएस बेरोजगारी दर 2022 मधील {ur['2022']}% वरून 2025 मध्ये {ur['2025']}% वर आला, आणि 2025 मध्ये 15 वर्षांवरील {lf['female']}% स्त्रिया श्रमशक्तीत होत्या."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_OR), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_OR), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_OR), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("OR", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    plfs_series("OR", NAME),
    lst("sectors-key", [
        it3("mining", "Mining", "खनन", "खाणकाम", d=("Iron ore in Kendujhar and Sundargarh, bauxite in Koraput, chromite at Sukinda, coal at Talcher and Ib valley.", "केंदुझर और सुंदरगढ़ में लौह अयस्क, कोरापुट में बॉक्साइट, सुकिंदा में क्रोमाइट, तालचेर और ईब घाटी में कोयला।", "केंदुझर व सुंदरगडमध्ये लोहखनिज, कोरापुटमध्ये बॉक्साइट, सुकिंदा येथे क्रोमाइट, तालचेर व ईब खोऱ्यात कोळसा.")),
        it3("steel", "Steel", "इस्पात", "पोलाद", d=("Rourkela, Kalinganagar and Angul.", "राउरकेला, कलिंगनगर और अंगुल।", "राउरकेला, कलिंगनगर व अंगुल.")),
        it3("aluminium", "Aluminium", "एल्युमिनियम", "ॲल्युमिनियम", d=("Refinery at Damanjodi; smelters at Angul and Jharsuguda.", "दामनजोड़ी में रिफ़ाइनरी; अंगुल और झारसुगुड़ा में स्मेल्टर।", "दामनजोडी येथे शुद्धीकरण; अंगुल व झारसुगुडा येथे स्मेल्टर.")),
        it3("port", "Ports and refining", "बंदरगाह और शोधन", "बंदरे व शुद्धीकरण", d=("Paradip port and refinery; Dhamra and Gopalpur ports.", "पारादीप बंदरगाह और रिफ़ाइनरी; धामरा और गोपालपुर बंदरगाह।", "पारादीप बंदर व रिफायनरी; धामरा व गोपाळपूर बंदरे.")),
        it3("agri", "Paddy and fisheries", "धान और मत्स्य पालन", "भात व मत्स्यव्यवसाय", d=("Rice across the State; marine fish and prawns on the coast.", "पूरे राज्य में धान; तट पर समुद्री मछली और झींगे।", "संपूर्ण राज्यात भात; किनाऱ्यावर सागरी मासे व कोळंबी.")),
        it3("handloom", "Handlooms and crafts", "हथकरघा और शिल्प", "हातमाग व हस्तकला", d=("Ikat weaving in western Odisha; Pattachitra, appliqué and filigree.", "पश्चिमी ओडिशा में इकत बुनाई; पट्टचित्र, एप्लिक और तारकशी।", "पश्चिम ओडिशात इकत विणकाम; पट्टचित्र, ऍप्लिक व जाळीकाम.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Mineral production and royalty", "खनिज उत्पादन और रॉयल्टी", "खनिज उत्पादन व स्वामित्वधन"), "india-gov", "Indian Bureau of Mines / Odisha Economic Survey."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("Cargo handled at Paradip port", "पारादीप बंदरगाह पर माल ढुलाई", "पारादीप बंदरातील माल हाताळणी"), "india-gov", "Ministry of Ports, Shipping and Waterways statistics."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Odisha has a unicameral legislature, the 147-member Legislative Assembly in Bhubaneswar. The State elects 21 members to the Lok Sabha and 10 to the Rajya Sabha.\n\nAssembly and Lok Sabha elections were held together in 2024. The BJP formed the government, ending 24 years of rule by the Biju Janata Dal under Naveen Patnaik, and Mohan Charan Majhi, a tribal leader from Kendujhar, was sworn in as Chief Minister on 12 June 2024, with Kanak Vardhan Singh Deo and Pravati Parida as Deputy Chief Ministers (News On AIR). Surama Padhy is Speaker. Dr Hari Babu Kambhampati became Governor in January 2025; the President appointed Braj Mohan Ram as his successor in October 2026.",
        "ओडिशा में एकसदनीय विधानमंडल है, भुवनेश्वर में 147 सदस्यों वाली विधानसभा। राज्य से लोकसभा के 21 और राज्यसभा के 10 सदस्य चुने जाते हैं।\n\n2024 में विधानसभा और लोकसभा चुनाव एक साथ हुए। भाजपा ने सरकार बनाई, जिससे नवीन पटनायक के नेतृत्व में बीजू जनता दल का 24 वर्ष का शासन समाप्त हुआ, और केंदुझर के जनजातीय नेता मोहन चरण माझी ने 12 जून 2024 को मुख्यमंत्री पद की शपथ ली, कनक वर्धन सिंह देव और प्रभाती परिडा उपमुख्यमंत्री बने (न्यूज़ ऑन एआईआर)। सुरमा पाढ़ी अध्यक्ष हैं। डॉ. हरि बाबू कंभमपति जनवरी 2025 में राज्यपाल बने; राष्ट्रपति ने अक्टूबर 2026 में ब्रज मोहन राम को उनका उत्तराधिकारी नियुक्त किया।",
        "ओडिशात एकसदनी विधिमंडळ आहे, भुवनेश्वरमधील 147 सदस्यांची विधानसभा. राज्यातून लोकसभेवर 21 व राज्यसभेवर 10 सदस्य निवडले जातात.\n\n2024 मध्ये विधानसभा व लोकसभा निवडणुका एकत्र झाल्या. भाजपने सरकार स्थापन केले, ज्यामुळे नवीन पटनायक यांच्या नेतृत्वाखालील बिजू जनता दलाची 24 वर्षांची सत्ता संपली, आणि केंदुझरचे आदिवासी नेते मोहन चरण माझी यांनी 12 जून 2024 रोजी मुख्यमंत्रिपदाची शपथ घेतली, कनक वर्धन सिंह देव व प्रभाती परिडा उपमुख्यमंत्री झाले (न्यूज ऑन एआयआर). सुरमा पाढी अध्यक्ष आहेत. डॉ. हरी बाबू कंभमपती जानेवारी 2025 मध्ये राज्यपाल झाले; राष्ट्रपतींनी ऑक्टोबर 2026 मध्ये ब्रज मोहन राम यांची त्यांचे उत्तराधिकारी म्हणून नियुक्ती केली."),
        sources=["newsonair", "odishabytes"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("noa", "News On AIR: Mohan Charan Majhi sworn in (12 Jun 2024)", "न्यूज़ ऑन एआईआर: मोहन चरण माझी ने शपथ ली (12 जून 2024)", "न्यूज ऑन एआयआर: मोहन चरण माझी यांचा शपथविधी (12 जून 2024)", url=CM, src="newsonair"),
        it3("rajbhavan", "Raj Bhavan, Odisha", "राजभवन, ओडिशा", "राजभवन, ओडिशा", url="https://rajbhavanodisha.gov.in", src="india-gov"),
        it3("portal", "Government of Odisha", "ओडिशा सरकार", "ओडिशा शासन", url="https://odisha.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2024 Assembly election — party-wise result", "2024 विधानसभा चुनाव — दलवार परिणाम", "2024 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Odisha 2024."),
        (L("Leader of Opposition — official notice", "नेता प्रतिपक्ष — आधिकारिक सूचना", "विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "Assembly secretariat."),
        (L("Local bodies by type", "प्रकार के अनुसार स्थानीय निकाय", "प्रकारानुसार स्थानिक स्वराज्य संस्था"), "india-gov", "Panchayati Raj and Housing & Urban Development departments."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "In August 2025 the Union Cabinet approved two semiconductor units at Info Valley, Bhubaneswar, under the India Semiconductor Mission. Odisha's other large works include new railway lines in the interior, port and industrial-corridor projects along the coast, and steel and aluminium expansions. Each card shows its source and the date it was checked.",
        "अगस्त 2025 में केंद्रीय मंत्रिमंडल ने भारत सेमीकंडक्टर मिशन के तहत भुवनेश्वर की इन्फ़ो वैली में दो सेमीकंडक्टर इकाइयों को मंज़ूरी दी। ओडिशा के अन्य बड़े कार्यों में भीतरी क्षेत्रों में नई रेल लाइनें, तट पर बंदरगाह और औद्योगिक गलियारा परियोजनाएँ, और इस्पात व एल्युमिनियम विस्तार शामिल हैं। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "ऑगस्ट 2025 मध्ये केंद्रीय मंत्रिमंडळाने भारत सेमीकंडक्टर मिशनअंतर्गत भुवनेश्वरच्या इन्फो व्हॅलीत दोन सेमीकंडक्टर प्रकल्पांना मंजुरी दिली. ओडिशाच्या इतर मोठ्या कामांत अंतर्गत भागांतील नवे रेल्वेमार्ग, किनाऱ्यावरील बंदर व औद्योगिक मार्गिका प्रकल्प आणि पोलाद व ॲल्युमिनियम विस्तार यांचा समावेश आहे. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pmindia"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Khurda Road–Bolangir rail line — status", "खुर्दा रोड–बलांगीर रेल लाइन — स्थिति", "खुर्दा रोड–बलांगीर रेल्वेमार्ग — स्थिती"), "railways", "East Coast Railway / Ministry of Railways."),
        (L("Puri international airport — status", "पुरी अंतरराष्ट्रीय हवाई अड्डा — स्थिति", "पुरी आंतरराष्ट्रीय विमानतळ — स्थिती"), "civil-aviation", "Ministry of Civil Aviation."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Biju Patnaik International Airport at Bhubaneswar is the main airport; Veer Surendra Sai Airport at Jharsuguda serves western Odisha, and smaller airports at Rourkela and Jeypore have regional flights. The East Coast Railway is headquartered at Bhubaneswar, and the Howrah–Chennai main line runs along the coast through Balasore, Cuttack, Bhubaneswar and Berhampur. National Highway 16, part of the Golden Quadrilateral, follows the same route. Paradip is a major port, and Dhamra and Gopalpur are other ports for coal, iron ore and containers.",
        "भुवनेश्वर का बीजू पटनायक अंतरराष्ट्रीय हवाई अड्डा मुख्य हवाई अड्डा है; झारसुगुड़ा का वीर सुरेंद्र साय हवाई अड्डा पश्चिमी ओडिशा को सेवा देता है, और राउरकेला व जयपुर के छोटे हवाई अड्डों से क्षेत्रीय उड़ानें हैं। पूर्व तट रेलवे का मुख्यालय भुवनेश्वर में है, और हावड़ा–चेन्नई मुख्य लाइन तट के साथ बालेश्वर, कटक, भुवनेश्वर और बरहमपुर से होकर जाती है। स्वर्णिम चतुर्भुज का हिस्सा राष्ट्रीय राजमार्ग 16 इसी मार्ग पर है। पारादीप एक प्रमुख बंदरगाह है, और धामरा व गोपालपुर कोयला, लौह अयस्क और कंटेनरों के अन्य बंदरगाह हैं।",
        "भुवनेश्वरचे बिजू पटनायक आंतरराष्ट्रीय विमानतळ हे मुख्य विमानतळ आहे; झारसुगुडाचे वीर सुरेंद्र साय विमानतळ पश्चिम ओडिशाला सेवा देते, आणि राउरकेला व जयपूरच्या लहान विमानतळांवरून प्रादेशिक उड्डाणे आहेत. पूर्व किनारा रेल्वेचे मुख्यालय भुवनेश्वरमध्ये आहे, आणि हावडा–चेन्नई मुख्य मार्ग किनाऱ्यालगत बालेश्वर, कटक, भुवनेश्वर व बेरहमपूरमार्गे जातो. सुवर्ण चतुष्कोनाचा भाग असलेला राष्ट्रीय महामार्ग 16 याच मार्गावर आहे. पारादीप हे प्रमुख बंदर आहे, आणि धामरा व गोपाळपूर ही कोळसा, लोहखनिज व कंटेनरसाठीची इतर बंदरे आहेत."),
        conf="Editorial"),
    lst("airports", [
        it3("bbi", "Biju Patnaik International Airport, Bhubaneswar", "बीजू पटनायक अंतरराष्ट्रीय हवाई अड्डा, भुवनेश्वर", "बिजू पटनायक आंतरराष्ट्रीय विमानतळ, भुवनेश्वर", m=("BBI", "BBI", "BBI")),
        it3("jrg", "Veer Surendra Sai Airport, Jharsuguda", "वीर सुरेंद्र साय हवाई अड्डा, झारसुगुड़ा", "वीर सुरेंद्र साय विमानतळ, झारसुगुडा", m=("JRG", "JRG", "JRG")),
        it3("rrk", "Rourkela", "राउरकेला", "राउरकेला", m=("RRK", "RRK", "RRK")),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Odisha holds some of India's largest coal reserves, in the Talcher and Ib valley coalfields worked by Mahanadi Coalfields Ltd, and much of its power comes from coal stations at Talcher, Angul and Jharsuguda, including captive plants of the aluminium and steel industries. Hydro-electric power comes from Hirakud, Balimela, Upper Kolab, Upper Indravati and Rengali. In the 1990s Odisha became the first State to restructure its electricity board and privatise distribution; the State is now adding solar and pumped-storage capacity.",
        "ओडिशा में भारत के सबसे बड़े कोयला भंडारों में से कुछ हैं, तालचेर और ईब घाटी कोयला क्षेत्रों में, जिनका खनन महानदी कोलफ़ील्ड्स लिमिटेड करता है, और इसकी अधिकांश बिजली तालचेर, अंगुल और झारसुगुड़ा के कोयला संयंत्रों से आती है, जिनमें एल्युमिनियम और इस्पात उद्योगों के कैप्टिव संयंत्र भी हैं। जलविद्युत हीराकुद, बालीमेला, अपर कोलाब, अपर इंद्रावती और रेंगाली से आती है। 1990 के दशक में ओडिशा अपने बिजली बोर्ड का पुनर्गठन कर वितरण का निजीकरण करने वाला पहला राज्य बना; राज्य अब सौर और पंप्ड-स्टोरेज क्षमता जोड़ रहा है।",
        "ओडिशात भारतातील सर्वांत मोठ्या कोळसा साठ्यांपैकी काही आहेत, तालचेर व ईब खोऱ्याच्या कोळसा क्षेत्रांत, जिथे महानदी कोलफिल्ड्स लिमिटेड खाणकाम करते, आणि त्याची बहुतांश वीज तालचेर, अंगुल व झारसुगुडाच्या कोळसा केंद्रांतून येते, ज्यात ॲल्युमिनियम व पोलाद उद्योगांचे स्वतःचे वीज प्रकल्पही आहेत. जलविद्युत हिराकुड, बालीमेला, अपर कोलाब, अपर इंद्रावती व रेंगाली येथून येते. 1990 च्या दशकात आपल्या वीज मंडळाची पुनर्रचना करून वितरणाचे खासगीकरण करणारे ओडिशा हे पहिले राज्य ठरले; राज्य आता सौर व पंप्ड-स्टोरेज क्षमता वाढवत आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
        (L("Coal production (MCL)", "कोयला उत्पादन (एमसीएल)", "कोळसा उत्पादन (एमसीएल)"), "india-gov", "Ministry of Coal annual report."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Bhubaneswar is Odisha's technology hub, with IT parks at Infocity and Info Valley, data centres and a growing start-up scene supported by incubators at IIT Bhubaneswar and KIIT. The 2025 approval of two semiconductor units at Info Valley may add electronics manufacturing. The State delivers many services online, and mobile connectivity has been extended to remote tribal districts.",
        "भुवनेश्वर ओडिशा का प्रौद्योगिकी केंद्र है, जहाँ इन्फ़ोसिटी और इन्फ़ो वैली में आईटी पार्क, डेटा सेंटर और आईआईटी भुवनेश्वर व कीट के इनक्यूबेटरों से समर्थित बढ़ता स्टार्टअप परिदृश्य है। 2025 में इन्फ़ो वैली में दो सेमीकंडक्टर इकाइयों की मंज़ूरी से इलेक्ट्रॉनिक्स विनिर्माण जुड़ सकता है। राज्य कई सेवाएँ ऑनलाइन देता है, और मोबाइल कनेक्टिविटी दूरस्थ जनजातीय ज़िलों तक पहुँचाई गई है।",
        "भुवनेश्वर हे ओडिशाचे तंत्रज्ञान केंद्र आहे, जिथे इन्फोसिटी व इन्फो व्हॅलीत आयटी पार्क, डेटा सेंटर आणि आयआयटी भुवनेश्वर व कीटच्या इन्क्युबेटर्सच्या आधाराने वाढते स्टार्टअप विश्व आहे. 2025 मध्ये इन्फो व्हॅलीतील दोन सेमीकंडक्टर प्रकल्पांच्या मंजुरीमुळे इलेक्ट्रॉनिक्स उत्पादनाची भर पडू शकते. राज्य अनेक सेवा ऑनलाइन देते, आणि मोबाइल जोडणी दुर्गम आदिवासी जिल्ह्यांपर्यंत पोहोचवली गेली आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Odisha circle)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("OR", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["OR"]
module(R, "education", [
    prose("p1", L(
        f"Odisha's higher-education gross enrolment ratio (ages 18–23) was 22.1% in 2021-22 in AISHE, up slightly from 21.1% in 2017-18 and below the national 28.4%; men's GER was {gm}% and women's {gf}%. The State had 37 universities and 1,300 colleges. Literacy at the 2011 Census was 72.9%.\n\nRavenshaw College in Cuttack (1868, now a university) and Utkal University (1943) are the oldest institutions. National institutes include IIT Bhubaneswar, NISER, AIIMS Bhubaneswar, NIT Rourkela, IIM Sambalpur and the National Law University Odisha, and the Odisha University of Agriculture and Technology is a leading farm university.",
        f"एआईएसएचई के अनुसार 2021-22 में ओडिशा का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) 22.1% था, जो 2017-18 के 21.1% से थोड़ा अधिक और राष्ट्रीय 28.4% से कम है; पुरुषों का जीईआर {gm}% और महिलाओं का {gf}% था। राज्य में 37 विश्वविद्यालय और 1,300 कॉलेज थे। 2011 की जनगणना में साक्षरता 72.9% थी।\n\nकटक का रेवेनशॉ कॉलेज (1868, अब विश्वविद्यालय) और उत्कल विश्वविद्यालय (1943) सबसे पुराने संस्थान हैं। राष्ट्रीय संस्थानों में आईआईटी भुवनेश्वर, नाइसर, एम्स भुवनेश्वर, एनआईटी राउरकेला, आईआईएम संबलपुर और राष्ट्रीय विधि विश्वविद्यालय ओडिशा शामिल हैं, और ओडिशा कृषि एवं प्रौद्योगिकी विश्वविद्यालय एक अग्रणी कृषि विश्वविद्यालय है।",
        f"एआयएसएचईनुसार 2021-22 मध्ये ओडिशाचे उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) 22.1% होते, 2017-18 मधील 21.1% पेक्षा किंचित अधिक आणि राष्ट्रीय 28.4% पेक्षा कमी; पुरुषांचे जीईआर {gm}% व स्त्रियांचे {gf}% होते. राज्यात 37 विद्यापीठे व 1,300 महाविद्यालये होती. 2011 च्या जनगणनेत साक्षरता 72.9% होती.\n\nकटकचे रेव्हेनशॉ महाविद्यालय (1868, आता विद्यापीठ) व उत्कल विद्यापीठ (1943) या सर्वांत जुन्या संस्था आहेत. राष्ट्रीय संस्थांत आयआयटी भुवनेश्वर, नायसर, एम्स भुवनेश्वर, एनआयटी राउरकेला, आयआयएम संबलपूर व राष्ट्रीय विधी विद्यापीठ ओडिशा यांचा समावेश आहे, आणि ओडिशा कृषी व तंत्रज्ञान विद्यापीठ हे आघाडीचे कृषी विद्यापीठ आहे."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("ravenshaw", "Ravenshaw University", "रेवेनशॉ विश्वविद्यालय", "रेव्हेनशॉ विद्यापीठ", m=("Cuttack, 1868", "कटक, 1868", "कटक, 1868")),
        it3("utkal", "Utkal University", "उत्कल विश्वविद्यालय", "उत्कल विद्यापीठ", m=("Bhubaneswar, 1943", "भुवनेश्वर, 1943", "भुवनेश्वर, 1943")),
        it3("iitbbs", "IIT Bhubaneswar", "आईआईटी भुवनेश्वर", "आयआयटी भुवनेश्वर", m=("Argul", "अरगुल", "अरगुल")),
        it3("niser", "NISER", "नाइसर", "नायसर", m=("Jatni", "जटनी", "जटनी")),
        it3("nitr", "NIT Rourkela", "एनआईटी राउरकेला", "एनआयटी राउरकेला", m=("Rourkela", "राउरकेला", "राउरकेला")),
        it3("aiimsbbs", "AIIMS Bhubaneswar", "एम्स भुवनेश्वर", "एम्स भुवनेश्वर", m=("Bhubaneswar", "भुवनेश्वर", "भुवनेश्वर")),
        it3("iims", "IIM Sambalpur", "आईआईएम संबलपुर", "आयआयएम संबलपूर", m=("Sambalpur", "संबलपुर", "संबलपूर")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Literacy by sex (Census 2011)", "लिंग के अनुसार साक्षरता (जनगणना 2011)", "लिंगनिहाय साक्षरता (जनगणना 2011)"), "census", "Primary Census Abstract."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["OR"]
module(R, "health", [
    prose("p1", L(
        f"Odisha has cut infant deaths sharply: the infant mortality rate fell from 61 per 1,000 live births in 2010 — among the highest in India — to 36 in 2020, though it was still above the national 28. The birth rate was 17.7 per 1,000 in 2020 and the death rate 7.3. Life expectancy at birth was 69.3 years in 2014-18 (men 68.0, women 70.8). In NFHS-5, {n['stunted'][1]:.1f}% of children under five were stunted, {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight — all lower than in NFHS-4 — and {n['institutional_N5']:.1f}% of births took place in health facilities, above the national 88.6%.\n\nSCB Medical College in Cuttack is the oldest referral hospital; AIIMS Bhubaneswar and the medical colleges at Berhampur (MKCG) and Burla (VIMSAR) are other major centres.",
        f"ओडिशा ने शिशु मृत्यु को तेज़ी से घटाया है: शिशु मृत्यु दर 2010 में प्रति 1,000 जीवित जन्म पर 61 — भारत में सबसे ऊँची दरों में — से घटकर 2020 में 36 हो गई, हालाँकि यह अब भी राष्ट्रीय 28 से ऊपर थी। 2020 में जन्म दर प्रति 1,000 पर 17.7 और मृत्यु दर 7.3 थी। 2014-18 में जन्म के समय जीवन प्रत्याशा 69.3 वर्ष थी (पुरुष 68.0, महिलाएँ 70.8)। एनएफ़एचएस-5 में पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने, {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के थे — सभी एनएफ़एचएस-4 से कम — और {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, जो राष्ट्रीय 88.6% से अधिक है।\n\nकटक का एससीबी मेडिकल कॉलेज सबसे पुराना रेफ़रल अस्पताल है; एम्स भुवनेश्वर और बरहमपुर (एमकेसीजी) व बुर्ला (विमसार) के मेडिकल कॉलेज अन्य प्रमुख केंद्र हैं।",
        f"ओडिशाने अर्भकमृत्यू वेगाने कमी केले आहेत: अर्भक मृत्युदर 2010 मध्ये दर 1,000 जिवंत जन्मांमागे 61 — भारतातील सर्वाधिक दरांपैकी — वरून 2020 मध्ये 36 वर आला, तरी तो राष्ट्रीय 28 पेक्षा अधिक होता. 2020 मध्ये जन्मदर दर 1,000 मागे 17.7 व मृत्युदर 7.3 होता. 2014-18 मध्ये जन्मतः आयुर्मान 69.3 वर्षे होते (पुरुष 68.0, स्त्रिया 70.8). एनएफएचएस-5 मध्ये पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी, {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची होती — सर्व एनएफएचएस-4 पेक्षा कमी — आणि {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, राष्ट्रीय 88.6% पेक्षा अधिक.\n\nकटकचे एससीबी वैद्यकीय महाविद्यालय हे सर्वांत जुने संदर्भ रुग्णालय आहे; एम्स भुवनेश्वर आणि बेरहमपूर (एमकेसीजी) व बुर्ला (विमसार) येथील वैद्यकीय महाविद्यालये ही इतर प्रमुख केंद्रे आहेत."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(36, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(61, "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(17.7, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020 (death rate 7.3); 20.5 in 2010."), "number",
             previous=dp(20.5, "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(69.3, "years", "2014-18", "survey", "srs", ESI_LE, note="SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male 68.0, female 70.8)."), "number", "higher-is-better",
             previous=dp(65.8, "years", "2010-14", "survey", "srs", ESI_LE), national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("OR"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin; the PIB summary used here lists only States that met the SDG target."),
        (L("Under-five mortality rate (SRS 2021)", "पाँच वर्ष से कम आयु की मृत्यु दर (एसआरएस 2021)", "पाच वर्षांखालील मृत्युदर (एसआरएस 2021)"), "srs", "SRS Statistical Report 2021."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("or mod2 ok")
