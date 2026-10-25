"""Chandigarh — Phase 3 profile (core + all modules). Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from ut_kit import *

R = "IN-CH"
NAME = L("Chandigarh", "चंडीगढ़", "चंदीगड")
ADM = "https://www.newsonair.gov.in/gulab-chand-kataria-takes-oath-as-governor-of-punjab/"
ADM2 = "https://www.newsonair.gov.in/punjab-governor-gulab-chand-kataria-congratulates-contributors-to-chandigarhs-growth"
mo = research("mospi_ch.json")

r = read("regions/IN-CH.json"); m = r["metrics"]
census_metrics(m, "CH", 114, "Males 5,80,663; females 4,74,787.", 9258, 21.93,
               "Computed from ISFR 2023 forest cover 25.0 km² ÷ geographical area 114 km².")
mospi_metrics(m, mo, "Chandigarh")
r["officialPortal"] = "https://chandigarh.gov.in"
r["symbols"] = {"animal": sym("Indian grey mongoose", "भारतीय भूरा नेवला", "भारतीय मुंगूस", "Urva edwardsii"),
                "bird": sym("Indian grey hornbill", "भारतीय भूरा धनेश", "भारतीय राखी धनेश", "Ocyceros birostris"),
                "tree": sym("Mango", "आम", "आंबा", "Mangifera indica")}
r["government"] = {
    "headOfState": office("administrator", L("Gulab Chand Kataria", "गुलाब चंद कटारिया", "गुलाबचंद कटारिया"), None, "2024-07-31", "newsonair", ADM, "https://chandigarh.gov.in", conf="Official",
                          note=f"Governor of Punjab since 31 July 2024, and by convention Administrator of the Union Territory of Chandigarh (All India Radio News). A March 2026 News On AIR report ({ADM2}) still describes him in this role."),
    "headOfGovernment": None, "others": [],
}
r["projects"] = []
r["giProducts"] = []
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-CH.json", r)
m = r["metrics"]

module(R, "overview", [
    prose("intro", L(
        "Chandigarh is a planned city at the foot of the Shivalik hills that serves as the capital of both Punjab and Haryana while itself being a Union Territory, administered directly by the Union. It was designed in the 1950s by the Swiss-French architect Le Corbusier with Pierre Jeanneret, Maxwell Fry and Jane Drew, to replace Lahore as Punjab's capital after Partition. The city is laid out in a grid of self-contained sectors, with wide green belts, the Capitol Complex in the north and Sukhna Lake to the east.\n\nWith Mohali in Punjab and Panchkula in Haryana it forms the Chandigarh Tricity. The Capitol Complex is part of the transnational UNESCO World Heritage Site 'The Architectural Work of Le Corbusier', inscribed in 2016.",
        "चंडीगढ़ शिवालिक पहाड़ियों की तलहटी में एक नियोजित नगर है, जो पंजाब और हरियाणा दोनों की राजधानी है और स्वयं एक केंद्र शासित प्रदेश है, जिसका प्रशासन सीधे केंद्र करता है। इसे 1950 के दशक में स्विस-फ़्रांसीसी वास्तुकार ले कॉर्बुज़िए ने पियरे जेनरे, मैक्सवेल फ़्राई और जेन ड्रू के साथ डिज़ाइन किया, ताकि विभाजन के बाद लाहौर के स्थान पर पंजाब की राजधानी बने। नगर आत्मनिर्भर सेक्टरों के ग्रिड में बसा है, चौड़ी हरित पट्टियों, उत्तर में कैपिटल कॉम्प्लेक्स और पूर्व में सुखना झील के साथ।\n\nपंजाब के मोहाली और हरियाणा के पंचकूला के साथ यह चंडीगढ़ ट्राइसिटी बनाता है। कैपिटल कॉम्प्लेक्स 2016 में अंकित अंतरराष्ट्रीय यूनेस्को विश्व धरोहर स्थल 'ले कॉर्बुज़िए का वास्तु कार्य' का भाग है।",
        "चंदीगड हे शिवालिक टेकड्यांच्या पायथ्याशी वसलेले नियोजित शहर आहे, जे पंजाब व हरियाणा दोघांची राजधानी असून स्वतः केंद्रशासित प्रदेश आहे, ज्याचा कारभार थेट केंद्र पाहते. फाळणीनंतर लाहोरऐवजी पंजाबची राजधानी म्हणून 1950 च्या दशकात स्विस-फ्रेंच वास्तुविशारद ले कॉर्बुझिए यांनी पियरे जेनरे, मॅक्सवेल फ्राय व जेन ड्रू यांच्यासोबत त्याची रचना केली. शहर स्वयंपूर्ण सेक्टरांच्या जाळीत वसलेले आहे, रुंद हरित पट्टे, उत्तरेला कॅपिटल कॉम्प्लेक्स व पूर्वेला सुखना सरोवरासह.\n\nपंजाबमधील मोहाली व हरियाणातील पंचकुलासह ते चंदीगड ट्रायसिटी बनवते. कॅपिटल कॉम्प्लेक्स हे 2016 मध्ये कोरलेल्या आंतरराष्ट्रीय युनेस्को जागतिक वारसा स्थळ 'ले कॉर्बुझिए यांचे वास्तुकार्य' याचा भाग आहे."),
        sources=["census", "unesco-whc"], conf="Editorial"),
    admin_table([
        row("Status", "दर्जा", "दर्जा", ("Union Territory without a legislature (since 1 November 1966)", "बिना विधानसभा वाला केंद्र शासित प्रदेश (1 नवंबर 1966 से)", "विधिमंडळ नसलेला केंद्रशासित प्रदेश (1 नोव्हेंबर 1966 पासून)")),
        row("Districts", "ज़िले", "जिल्हे", ("1 (Chandigarh)", "1 (चंडीगढ़)", "1 (चंदीगड)")),
        row("Capital of", "राजधानी", "राजधानी", ("Punjab and Haryana", "पंजाब और हरियाणा", "पंजाब व हरियाणा")),
        row("High Court", "उच्च न्यायालय", "उच्च न्यायालय", ("Punjab and Haryana High Court, Chandigarh", "पंजाब और हरियाणा उच्च न्यायालय, चंडीगढ़", "पंजाब व हरियाणा उच्च न्यायालय, चंदीगड")),
        row("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक", "CH"),
        row("Time zone", "समय क्षेत्र", "प्रमाणवेळ", "IST (UTC+05:30)"),
    ]),
])

module(R, "geography", [
    prose("p1", L(
        "Chandigarh lies on the gently sloping plain below the Shivalik foothills, between two seasonal streams, the Sukhna Choe and the Patiali Ki Rao. Sukhna Lake was created in 1958 by damming the Sukhna Choe. The UT covers 114 km² and borders Punjab on the west and south and Haryana on the east.",
        "चंडीगढ़ शिवालिक तलहटी के नीचे धीरे-धीरे ढलते मैदान पर, दो मौसमी नालों, सुखना चो और पटियाली की राव, के बीच स्थित है। सुखना झील 1958 में सुखना चो को बाँधकर बनाई गई। केंद्र शासित प्रदेश 114 वर्ग किमी में फैला है और पश्चिम व दक्षिण में पंजाब तथा पूर्व में हरियाणा से घिरा है।",
        "चंदीगड शिवालिक पायथ्याखालील हळूहळू उतरत्या मैदानावर, सुखना चो व पटियाली की राव या दोन हंगामी ओढ्यांच्या दरम्यान आहे. सुखना सरोवर 1958 मध्ये सुखना चो अडवून तयार केले गेले. केंद्रशासित प्रदेश 114 चौ.किमी व्यापतो आणि पश्चिम व दक्षिणेला पंजाब व पूर्वेला हरियाणा आहे."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), m["area"], "number", national=IND["area"])]),
])

module(R, "climate", [
    prose("p1", L(
        "Chandigarh has a humid subtropical climate: hot summers from April to June, monsoon rain from July to September, and cool, foggy winters from December to February. October–November and February–March are the most pleasant months.",
        "चंडीगढ़ की जलवायु आर्द्र उपोष्ण है: अप्रैल से जून तक गर्म गर्मियाँ, जुलाई से सितंबर तक मानसूनी वर्षा, और दिसंबर से फ़रवरी तक ठंडी, कोहरे वाली सर्दियाँ। अक्टूबर–नवंबर और फ़रवरी–मार्च सबसे सुहावने महीने हैं।",
        "चंदीगडचे हवामान दमट उपोष्ण आहे: एप्रिल ते जून उष्ण उन्हाळा, जुलै ते सप्टेंबर मान्सूनी पाऊस, आणि डिसेंबर ते फेब्रुवारी थंड, धुक्याचा हिवाळा. ऑक्टोबर–नोव्हेंबर व फेब्रुवारी–मार्च हे सर्वांत सुखद महिने आहेत."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [{"name": L("Chandigarh", "चंडीगढ़", "चंदीगड"), "lat": 30.7333, "lon": 76.7794}]},
])

module(R, "vibe", [
    prose("p1", L(
        "Chandigarh is known for its tree-lined avenues, roundabouts and orderly sectors, each with its own market. Evenings are spent walking at Sukhna Lake or shopping in Sector 17, and the city has a large student and government-employee population, which gives it a relaxed, middle-class feel.",
        "चंडीगढ़ अपने पेड़ों से घिरे मार्गों, गोल चक्करों और व्यवस्थित सेक्टरों के लिए जाना जाता है, जिनमें से हर एक का अपना बाज़ार है। शामें सुखना झील पर टहलते या सेक्टर 17 में ख़रीदारी करते बीतती हैं, और शहर में छात्रों और सरकारी कर्मचारियों की बड़ी आबादी है, जो इसे सहज, मध्यमवर्गीय माहौल देती है।",
        "चंदीगड झाडांनी वेढलेले रस्ते, गोलचक्कर व शिस्तबद्ध सेक्टरांसाठी ओळखले जाते, ज्यांपैकी प्रत्येकाचा स्वतःचा बाजार आहे. संध्याकाळ सुखना सरोवरावर फिरण्यात किंवा सेक्टर 17 मध्ये खरेदीत जाते, आणि शहरात विद्यार्थी व सरकारी कर्मचाऱ्यांची मोठी लोकसंख्या आहे, जी त्याला निवांत, मध्यमवर्गीय वातावरण देते."),
        conf="Editorial"),
])

module(R, "people", [
    prose("p1", L(
        "Chandigarh had 10.55 lakh people at the 2011 Census, at a density of about 9,258 per km². Its sex ratio was 818 women per 1,000 men, up from 777 in 2001, reflecting male migrant workers, and the child sex ratio rose from 845 to 880. Literacy was 86.0%, and Scheduled Castes made up 18.9% of the population. Hindi and Punjabi are the main languages, and English is the language of administration.",
        "2011 की जनगणना में चंडीगढ़ की जनसंख्या 10.55 लाख थी, लगभग 9,258 प्रति वर्ग किमी के घनत्व पर। लिंगानुपात प्रति 1,000 पुरुषों पर 818 महिलाएँ था, जो 2001 के 777 से अधिक है और पुरुष प्रवासी मज़दूरों को दर्शाता है, और शिशु लिंगानुपात 845 से बढ़कर 880 हुआ। साक्षरता 86.0% थी, और अनुसूचित जातियाँ जनसंख्या का 18.9% थीं। हिंदी और पंजाबी मुख्य भाषाएँ हैं, और प्रशासन की भाषा अंग्रेज़ी है।",
        "2011 च्या जनगणनेनुसार चंदीगडची लोकसंख्या 10.55 लाख होती, सुमारे 9,258 प्रति चौ.किमी घनतेसह. दर 1,000 पुरुषांमागे 818 स्त्रिया होत्या, 2001 मधील 777 वरून वाढ, जी पुरुष स्थलांतरित मजुरांमुळे आहे, आणि बाल लिंग गुणोत्तर 845 वरून 880 झाले. साक्षरता 86.0% होती, आणि अनुसूचित जाती लोकसंख्येच्या 18.9% होत्या. हिंदी व पंजाबी मुख्य भाषा आहेत, आणि प्रशासनाची भाषा इंग्रजी आहे."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", people_facts("CH", m, "CH", fact("sc", L("Scheduled Castes, share of population", "अनुसूचित जातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जाती, लोकसंख्येतील वाटा"),
        dp(18.9, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 1.99 lakh people. No Scheduled Tribes are notified for the UT."), "percent")),
        title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
])

module(R, "history", [
    prose("p1", L(
        "After Partition left Lahore in Pakistan, Punjab needed a new capital. The site near the Shivalik foothills was chosen in 1948, and after the death of the first planner, Matthew Nowicki, Le Corbusier was appointed in 1951. Jawaharlal Nehru described the city as 'unfettered by the traditions of the past, a symbol of the nation's faith in the future'. When Punjab was reorganised on 1 November 1966 and Haryana created, Chandigarh became a Union Territory and the shared capital of both States. Its final status has been the subject of political claims by Punjab and Haryana.",
        "विभाजन के बाद लाहौर पाकिस्तान में चले जाने पर पंजाब को नई राजधानी की ज़रूरत थी। शिवालिक तलहटी के पास स्थल 1948 में चुना गया, और पहले योजनाकार मैथ्यू नोविकी की मृत्यु के बाद 1951 में ले कॉर्बुज़िए नियुक्त हुए। जवाहरलाल नेहरू ने इस नगर को 'अतीत की परंपराओं से मुक्त, भविष्य में राष्ट्र के विश्वास का प्रतीक' कहा। 1 नवंबर 1966 को पंजाब के पुनर्गठन और हरियाणा के गठन पर चंडीगढ़ केंद्र शासित प्रदेश और दोनों राज्यों की साझा राजधानी बना। इसकी अंतिम स्थिति पर पंजाब और हरियाणा के राजनीतिक दावे रहे हैं।",
        "फाळणीनंतर लाहोर पाकिस्तानात गेल्यामुळे पंजाबला नव्या राजधानीची गरज होती. शिवालिक पायथ्याजवळील जागा 1948 मध्ये निवडली गेली, आणि पहिले नियोजक मॅथ्यू नोविकी यांच्या निधनानंतर 1951 मध्ये ले कॉर्बुझिए यांची नेमणूक झाली. जवाहरलाल नेहरूंनी या शहराला 'भूतकाळाच्या परंपरांपासून मुक्त, राष्ट्राच्या भविष्यावरील श्रद्धेचे प्रतीक' म्हटले. 1 नोव्हेंबर 1966 रोजी पंजाबच्या पुनर्रचनेनंतर व हरियाणाच्या निर्मितीनंतर चंदीगड केंद्रशासित प्रदेश व दोन्ही राज्यांची सामायिक राजधानी झाले. त्याच्या अंतिम दर्जाबाबत पंजाब व हरियाणाचे राजकीय दावे राहिले आहेत."),
        conf="Editorial"),
    timeline([
        ev("site", 1948, L("1948", "1948", "1948"), L("Site chosen for Punjab's new capital", "पंजाब की नई राजधानी के लिए स्थल चुना गया", "पंजाबच्या नव्या राजधानीसाठी जागा निवडली")),
        ev("corbu", 1951, L("1951", "1951", "1951"), L("Le Corbusier appointed", "ले कॉर्बुज़िए नियुक्त", "ले कॉर्बुझिए यांची नेमणूक")),
        ev("ut", 1966, L("1 November 1966", "1 नवंबर 1966", "1 नोव्हेंबर 1966"), L("Union Territory; capital of Punjab and Haryana", "केंद्र शासित प्रदेश; पंजाब और हरियाणा की राजधानी", "केंद्रशासित प्रदेश; पंजाब व हरियाणाची राजधानी")),
        ev("unesco", 2016, L("2016", "2016", "2016"), L("Capitol Complex inscribed as World Heritage", "कैपिटल कॉम्प्लेक्स विश्व धरोहर में अंकित", "कॅपिटल कॉम्प्लेक्स जागतिक वारसा म्हणून कोरले")),
    ]),
])

module(R, "culture", [
    prose("p1", L(
        "Chandigarh's culture blends Punjabi and Haryanvi traditions with a cosmopolitan student life. Lohri, Baisakhi, Diwali and Gurpurab are widely celebrated, the Rose Festival in the Zakir Hussain Rose Garden is held every February, and the Teej festival and Chandigarh Carnival draw crowds. Nek Chand's Rock Garden, made from waste materials, is a celebrated work of outsider art.",
        "चंडीगढ़ की संस्कृति पंजाबी और हरियाणवी परंपराओं को महानगरीय छात्र जीवन से मिलाती है। लोहड़ी, बैसाखी, दीवाली और गुरपुरब व्यापक रूप से मनाए जाते हैं, ज़ाकिर हुसैन रोज़ गार्डन में हर फ़रवरी गुलाब महोत्सव होता है, और तीज उत्सव व चंडीगढ़ कार्निवल भीड़ खींचते हैं। कचरे से बना नेक चंद का रॉक गार्डन बाहरी कला की प्रसिद्ध कृति है।",
        "चंदीगडची संस्कृती पंजाबी व हरियाणवी परंपरांना महानगरी विद्यार्थी जीवनाशी जोडते. लोहडी, बैसाखी, दिवाळी व गुरपुरब मोठ्या प्रमाणावर साजरे होतात, झाकीर हुसेन रोझ गार्डनमध्ये दर फेब्रुवारीला गुलाब महोत्सव भरतो, आणि तीज उत्सव व चंदीगड कार्निव्हल गर्दी खेचतात. टाकाऊ वस्तूंतून बनवलेले नेक चंद यांचे रॉक गार्डन हे बाह्य कलेचे प्रसिद्ध उदाहरण आहे."),
        conf="Editorial"),
])

ur = AP["plfs_ur_15plus_psss"]["CH"]; lf = AP["plfs_lfpr_2025"]["CH"]; g = mo["gsva2024_25_current_lakh"]; sh = {k: 100 * v / g["total"] for k, v in g.items()}
module(R, "economy", [
    prose("p1", L(
        f"Chandigarh's GSDP at current prices was about ₹{inr(mo['gsdp']['FY2024-25'][0])} crore in FY2024-25 in the MoSPI series, and its per capita NSDP of ₹{inr(mo['pcnsdp']['FY2024-25'][0])} was the fourth highest of the 30 regions with a FY2024-25 figure in that series, after Sikkim, Goa and Delhi. Services dominate: trade, hotels and restaurants made up about {sh['trade_hotels']:.0f}% of GSVA, real estate and professional services {sh['realestate_prof']:.0f}% and financial services {sh['financial']:.0f}%, while agriculture was under 1%. Government offices of the UT, Punjab and Haryana, education and health institutions, and IT firms in the IT Park are major employers. The PLFS unemployment rate was {ur['2025']}% in 2025, and {lf['female']}% of women aged 15+ were in the labour force.",
        f"मोस्पी शृंखला में वित्त वर्ष 2024-25 में चंडीगढ़ का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{inr(mo['gsdp']['FY2024-25'][0])} करोड़ था, और ₹{inr(mo['pcnsdp']['FY2024-25'][0])} का प्रति व्यक्ति एनएसडीपी उस शृंखला में वित्त वर्ष 2024-25 के आँकड़े वाले 30 क्षेत्रों में सिक्किम, गोवा और दिल्ली के बाद चौथा सबसे ऊँचा था। सेवाएँ प्रमुख हैं: व्यापार, होटल और रेस्तराँ जीएसवीए का लगभग {sh['trade_hotels']:.0f}%, अचल संपत्ति और व्यावसायिक सेवाएँ {sh['realestate_prof']:.0f}% और वित्तीय सेवाएँ {sh['financial']:.0f}% थीं, जबकि कृषि 1% से कम। केंद्र शासित प्रदेश, पंजाब और हरियाणा के सरकारी कार्यालय, शिक्षा और स्वास्थ्य संस्थान, और आईटी पार्क की आईटी कंपनियाँ बड़े नियोक्ता हैं। पीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी, और 15+ आयु की {lf['female']}% महिलाएँ श्रम बल में थीं।",
        f"मोस्पी मालिकेनुसार आ.व. 2024-25 मध्ये चंदीगडचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{inr(mo['gsdp']['FY2024-25'][0])} कोटी होते, आणि ₹{inr(mo['pcnsdp']['FY2024-25'][0])} चे दरडोई एनएसडीपी त्या मालिकेत आ.व. 2024-25 चा आकडा असलेल्या 30 प्रदेशांत सिक्कीम, गोवा व दिल्लीनंतर चौथ्या क्रमांकाचे होते. सेवा प्रमुख आहेत: व्यापार, हॉटेल व उपाहारगृहे जीएसव्हीएच्या सुमारे {sh['trade_hotels']:.0f}%, स्थावर मालमत्ता व व्यावसायिक सेवा {sh['realestate_prof']:.0f}% व वित्तीय सेवा {sh['financial']:.0f}% होत्या, तर शेती 1% पेक्षा कमी. केंद्रशासित प्रदेश, पंजाब व हरियाणाची सरकारी कार्यालये, शिक्षण व आरोग्य संस्था, आणि आयटी पार्कमधील आयटी कंपन्या मोठे रोजगारदाते आहेत. पीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता, आणि 15+ वयाच्या {lf['female']}% स्त्रिया श्रमशक्तीत होत्या."),
        sources=["mospi", "plfs"], conf="Official"),
    *econ_blocks("CH", NAME, mo),
])

module(R, "government", [
    prose("p1", L(
        "Chandigarh is a Union Territory without a legislature. Since 1984 the Governor of Punjab has also served as its Administrator, assisted by an Adviser and UT officers. The elected Municipal Corporation of Chandigarh, headed by a Mayor, runs civic services, and the UT elects one member to the Lok Sabha. The Punjab and Haryana legislatures and secretariats sit in the Capitol Complex.",
        "चंडीगढ़ बिना विधानसभा वाला केंद्र शासित प्रदेश है। 1984 से पंजाब के राज्यपाल इसके प्रशासक भी हैं, जिनकी सहायता एक सलाहकार और केंद्र शासित प्रदेश के अधिकारी करते हैं। महापौर के नेतृत्व वाला निर्वाचित चंडीगढ़ नगर निगम नागरिक सेवाएँ चलाता है, और केंद्र शासित प्रदेश से लोकसभा का एक सदस्य चुना जाता है। पंजाब और हरियाणा की विधानसभाएँ और सचिवालय कैपिटल कॉम्प्लेक्स में हैं।",
        "चंदीगड हा विधिमंडळ नसलेला केंद्रशासित प्रदेश आहे. 1984 पासून पंजाबचे राज्यपाल त्याचे प्रशासकही आहेत, ज्यांना एक सल्लागार व केंद्रशासित प्रदेशाचे अधिकारी मदत करतात. महापौरांच्या नेतृत्वाखालील निवडून आलेली चंदीगड महानगरपालिका नागरी सेवा चालवते, आणि केंद्रशासित प्रदेशातून लोकसभेवर एक सदस्य निवडला जातो. पंजाब व हरियाणाच्या विधानसभा व सचिवालये कॅपिटल कॉम्प्लेक्समध्ये आहेत."),
        sources=["newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    gaps("g", [(L("Mayor of Chandigarh — current", "चंडीगढ़ के महापौर — वर्तमान", "चंदीगडचे महापौर — सध्याचे"), "india-gov", "Municipal Corporation Chandigarh; record the date of election.")]),
])

module(R, "projects", [
    prose("p1", L(
        "Planned works include a metro or mass rapid transit system for the Tricity and the expansion of Chandigarh International Airport, which lies just across the border in Mohali. They will be added as cards once their status is confirmed from official sources.",
        "नियोजित कार्यों में ट्राइसिटी के लिए मेट्रो या मास रैपिड ट्रांज़िट प्रणाली और मोहाली में सीमा के ठीक पार स्थित चंडीगढ़ अंतरराष्ट्रीय हवाई अड्डे का विस्तार शामिल हैं। आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर इन्हें कार्ड के रूप में जोड़ा जाएगा।",
        "नियोजित कामांत ट्रायसिटीसाठी मेट्रो किंवा मास रॅपिड ट्रान्झिट प्रणाली आणि मोहालीत सीमेपलीकडेच असलेल्या चंदीगड आंतरराष्ट्रीय विमानतळाचा विस्तार यांचा समावेश आहे. अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर त्यांची कार्डे जोडली जातील."),
        conf="Editorial"),
    {"type": "projects", "id": "projects"},
    gaps("g", [(L("Tricity metro — official status", "ट्राइसिटी मेट्रो — आधिकारिक स्थिति", "ट्रायसिटी मेट्रो — अधिकृत स्थिती"), "india-gov", "Chandigarh Administration / MoHUA.")]),
])

module(R, "transport", [
    prose("p1", L(
        "Chandigarh is a junction on the railway to Kalka and Shimla, and Shaheed Bhagat Singh International Airport (Chandigarh International Airport) serves the Tricity. The city's grid of 'V' roads separates fast traffic from local streets, and it has an extensive cycle-track network and local bus service.",
        "चंडीगढ़ कालका और शिमला की रेल लाइन पर एक जंक्शन है, और शहीद भगत सिंह अंतरराष्ट्रीय हवाई अड्डा (चंडीगढ़ अंतरराष्ट्रीय हवाई अड्डा) ट्राइसिटी की सेवा करता है। शहर का 'वी' सड़कों का ग्रिड तेज़ यातायात को स्थानीय गलियों से अलग करता है, और इसमें साइकिल ट्रैक का व्यापक जाल और स्थानीय बस सेवा है।",
        "चंदीगड हे कालका व शिमलाकडील रेल्वेमार्गावरील जंक्शन आहे, आणि शहीद भगतसिंग आंतरराष्ट्रीय विमानतळ (चंदीगड आंतरराष्ट्रीय विमानतळ) ट्रायसिटीला सेवा देतो. शहराचे 'व्ही' रस्त्यांचे जाळे जलद वाहतूक स्थानिक रस्त्यांपासून वेगळी ठेवते, आणि येथे सायकल मार्गांचे विस्तृत जाळे व स्थानिक बससेवा आहे."),
        conf="Editorial"),
])

module(R, "energy", [
    prose("p1", L(
        "Chandigarh has no large power stations and draws electricity from the northern grid through central allocations. Rooftop solar is mandatory on larger buildings, and government buildings have been fitted with solar panels.",
        "चंडीगढ़ में बड़े बिजलीघर नहीं हैं और यह केंद्रीय आवंटन से उत्तरी ग्रिड से बिजली लेता है। बड़े भवनों पर रूफ़टॉप सौर अनिवार्य है, और सरकारी भवनों पर सौर पैनल लगाए गए हैं।",
        "चंदीगडमध्ये मोठी वीजकेंद्रे नाहीत आणि ते केंद्रीय वाटपातून उत्तर ग्रिडमधून वीज घेते. मोठ्या इमारतींवर छतावरील सौरऊर्जा बंधनकारक आहे, आणि सरकारी इमारतींवर सौर पॅनेल बसवले गेले आहेत."),
        conf="Editorial"),
    gaps("g", [(L("Rooftop solar capacity", "रूफ़टॉप सौर क्षमता", "छतावरील सौर क्षमता"), "mnre", "MNRE / CREST Chandigarh.")]),
])

module(R, "digital", [
    prose("p1", L(
        "Chandigarh has good mobile and fibre broadband coverage. The Rajiv Gandhi Chandigarh Technology Park hosts IT and IT-enabled service companies, and the city offers many civic services online through the UT and municipal portals.",
        "चंडीगढ़ में अच्छा मोबाइल और फ़ाइबर ब्रॉडबैंड कवरेज है। राजीव गांधी चंडीगढ़ टेक्नोलॉजी पार्क में आईटी और आईटी-सक्षम सेवा कंपनियाँ हैं, और शहर केंद्र शासित प्रदेश और नगर निगम पोर्टलों से कई नागरिक सेवाएँ ऑनलाइन देता है।",
        "चंदीगडमध्ये चांगली मोबाइल व फायबर ब्रॉडबँड व्याप्ती आहे. राजीव गांधी चंदीगड तंत्रज्ञान उद्यानात आयटी व आयटी-आधारित सेवा कंपन्या आहेत, आणि शहर केंद्रशासित प्रदेश व महानगरपालिकेच्या संकेतस्थळांवरून अनेक नागरी सेवा ऑनलाइन देते."),
        conf="Editorial"),
])

ef, es = aishe_block("CH", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["CH"]
module(R, "education", [
    prose("p1", L(
        f"Chandigarh is an education hub for the region. The higher-education gross enrolment ratio was {AP['aishe_ger']['CH']['2021-22']}% in 2021-22 in AISHE, far above the national 28.4% because students come from neighbouring States, with women at {gf}% and men at {gm}%. Panjab University, the Postgraduate Institute of Medical Education and Research (PGIMER), Punjab Engineering College and the Government Medical College are the main institutions.",
        f"चंडीगढ़ क्षेत्र का शैक्षिक केंद्र है। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात {AP['aishe_ger']['CH']['2021-22']}% था, जो राष्ट्रीय 28.4% से बहुत अधिक है क्योंकि छात्र पड़ोसी राज्यों से आते हैं, महिलाएँ {gf}% और पुरुष {gm}%। पंजाब विश्वविद्यालय, स्नातकोत्तर चिकित्सा शिक्षा एवं अनुसंधान संस्थान (पीजीआईएमईआर), पंजाब इंजीनियरिंग कॉलेज और गवर्नमेंट मेडिकल कॉलेज मुख्य संस्थान हैं।",
        f"चंदीगड हे प्रदेशाचे शैक्षणिक केंद्र आहे. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर {AP['aishe_ger']['CH']['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा खूप जास्त, कारण विद्यार्थी शेजारच्या राज्यांतून येतात, स्त्रिया {gf}% व पुरुष {gm}%. पंजाब विद्यापीठ, पदव्युत्तर वैद्यकीय शिक्षण व संशोधन संस्था (पीजीआयएमईआर), पंजाब अभियांत्रिकी महाविद्यालय व शासकीय वैद्यकीय महाविद्यालय या मुख्य संस्था आहेत."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
])

n = NF["CH"]
module(R, "health", [
    prose("p1", L(
        f"PGIMER, an institute of national importance, and the Government Medical College and Hospital in Sector 32 serve patients from Punjab, Haryana, Himachal Pradesh and Jammu and Kashmir as well as the city. In NFHS-5, {n['institutional_N5']:.1f}% of births were in health facilities and {n['stunted'][1]:.1f}% of children under five were stunted, down from {n['stunted'][0]}% in NFHS-4.",
        f"राष्ट्रीय महत्व का संस्थान पीजीआईएमईआर और सेक्टर 32 का गवर्नमेंट मेडिकल कॉलेज एवं अस्पताल शहर के साथ-साथ पंजाब, हरियाणा, हिमाचल प्रदेश और जम्मू-कश्मीर के मरीज़ों की सेवा करते हैं। एनएफ़एचएस-5 में {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए और पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने थे, जो एनएफ़एचएस-4 के {n['stunted'][0]}% से कम है।",
        f"राष्ट्रीय महत्त्वाची संस्था पीजीआयएमईआर व सेक्टर 32 मधील शासकीय वैद्यकीय महाविद्यालय व रुग्णालय शहराबरोबरच पंजाब, हरियाणा, हिमाचल प्रदेश व जम्मू-काश्मीरमधील रुग्णांना सेवा देतात. एनएफएचएस-5 मध्ये {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या आणि पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी होती, एनएफएचएस-4 मधील {n['stunted'][0]}% वरून कमी."),
        sources=["srs", "nfhs"], conf="Official"),
    srs_facts("CH"), nfhs_block("CH"),
])

module(R, "nature", [
    prose("p1", L(
        "Despite its small size, about 22% of Chandigarh is forest (ISFR 2023), mainly in the Sukhna Wildlife Sanctuary in the Shivalik foothills and the city's green belts. Sukhna Lake attracts migratory birds in winter, and the city has many parks and gardens. There is no Ramsar site in Chandigarh on the list as on 21 April 2026.",
        "छोटे आकार के बावजूद चंडीगढ़ का लगभग 22% भाग वन है (आईएसएफ़आर 2023), मुख्यतः शिवालिक तलहटी के सुखना वन्यजीव अभयारण्य और शहर की हरित पट्टियों में। सुखना झील सर्दियों में प्रवासी पक्षियों को आकर्षित करती है, और शहर में कई पार्क और उद्यान हैं। 21 अप्रैल 2026 की सूची में चंडीगढ़ में कोई रामसर स्थल नहीं है।",
        "लहान आकार असूनही चंदीगडचा सुमारे 22% भाग वनाच्छादित आहे (आयएसएफआर 2023), मुख्यतः शिवालिक पायथ्याचे सुखना वन्यजीव अभयारण्य व शहरातील हरित पट्ट्यांत. सुखना सरोवर हिवाळ्यात स्थलांतरित पक्ष्यांना आकर्षित करते, आणि शहरात अनेक उद्याने व बागा आहेत. 21 एप्रिल 2026 च्या यादीत चंदीगडमध्ये कोणतेही रामसर स्थळ नाही."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    forest_facts("CH", m["forestCoverPct"], 0, "MoEFCC list of Ramsar sites as on 21 April 2026: none in Chandigarh."),
])

module(R, "water", [
    prose("p1", L(
        "Chandigarh's drinking water comes mainly from the Bhakra main canal at Kajauli, supplemented by tube wells. Sukhna Lake depends on rain and has been affected by silt from the Shivalik hills.",
        "चंडीगढ़ का पेयजल मुख्यतः काजौली में भाखड़ा मुख्य नहर से आता है, जिसे नलकूप पूरा करते हैं। सुखना झील वर्षा पर निर्भर है और शिवालिक पहाड़ियों की गाद से प्रभावित हुई है।",
        "चंदीगडचे पिण्याचे पाणी मुख्यतः काजौली येथील भाक्रा मुख्य कालव्यातून येते, ज्याला कूपनलिकांची जोड आहे. सुखना सरोवर पावसावर अवलंबून आहे व शिवालिक टेकड्यांतील गाळाने प्रभावित झाले आहे."),
        conf="Editorial"),
])

module(R, "safety", [
    prose("p1", L(
        "Chandigarh lies in seismic zone IV. Winter fog disrupts road, rail and air travel, and the city's roads have a large number of vehicles for its size. Emergency services are coordinated by the UT Administration.",
        "चंडीगढ़ भूकंपीय क्षेत्र IV में है। सर्दियों का कोहरा सड़क, रेल और हवाई यात्रा बाधित करता है, और शहर की सड़कों पर उसके आकार की तुलना में बहुत वाहन हैं। आपात सेवाओं का समन्वय केंद्र शासित प्रदेश प्रशासन करता है।",
        "चंदीगड भूकंप क्षेत्र IV मध्ये आहे. हिवाळ्यातील धुके रस्ता, रेल्वे व हवाई प्रवास विस्कळीत करते, आणि शहराच्या आकाराच्या मानाने रस्त्यांवर वाहने जास्त आहेत. आपत्कालीन सेवांचा समन्वय केंद्रशासित प्रदेश प्रशासन करते."),
        conf="Editorial"),
    emergency_table(("Chandigarh", "चंडीगढ़", "चंदीगड")),
])

module(R, "gi", [
    prose("p1", L(
        "No GI on the GI Registry's list as on 31 December 2025 is registered for Chandigarh.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में चंडीगढ़ के लिए कोई जीआई पंजीकृत नहीं है।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत चंदीगडसाठी कोणताही जीआय नोंदणीकृत नाही."),
        sources=["gi-registry"], conf="Official"),
])

module(R, "tourism", [
    prose("p1", L(
        "The Capitol Complex — the Secretariat, the Legislative Assembly building, the High Court and the Open Hand monument — can be visited on guided tours. Nek Chand's Rock Garden, Sukhna Lake, the Zakir Hussain Rose Garden, the Government Museum and Art Gallery and the Le Corbusier Centre are other highlights, and the hill towns of Kasauli and Shimla are a short drive away.",
        "कैपिटल कॉम्प्लेक्स — सचिवालय, विधानसभा भवन, उच्च न्यायालय और ओपन हैंड स्मारक — निर्देशित भ्रमण पर देखा जा सकता है। नेक चंद का रॉक गार्डन, सुखना झील, ज़ाकिर हुसैन रोज़ गार्डन, राजकीय संग्रहालय एवं कला वीथिका और ले कॉर्बुज़िए केंद्र अन्य आकर्षण हैं, और कसौली और शिमला जैसे पहाड़ी नगर थोड़ी दूरी पर हैं।",
        "कॅपिटल कॉम्प्लेक्स — सचिवालय, विधानसभा इमारत, उच्च न्यायालय व ओपन हँड स्मारक — मार्गदर्शित सहलीत पाहता येते. नेक चंद यांचे रॉक गार्डन, सुखना सरोवर, झाकीर हुसेन रोझ गार्डन, शासकीय संग्रहालय व कलादालन आणि ले कॉर्बुझिए केंद्र ही इतर आकर्षणे आहेत, आणि कसौली व शिमलासारखी डोंगरी शहरे जवळच आहेत."),
        conf="Editorial"),
])

module(R, "cities", [
    lst("cities", [
        item("ch", L("Chandigarh", "चंडीगढ़", "चंदीगड"), detail=L("Planned city of sectors; the whole UT is one district.", "सेक्टरों वाला नियोजित नगर; पूरा केंद्र शासित प्रदेश एक ज़िला है।", "सेक्टरांचे नियोजित शहर; संपूर्ण केंद्रशासित प्रदेश एकच जिल्हा आहे."), meta=L("Capital", "राजधानी", "राजधानी")),
        item("manimajra", L("Manimajra", "मनीमाजरा", "मनीमाजरा"), detail=L("Older town within the UT.", "केंद्र शासित प्रदेश के भीतर पुराना नगर।", "केंद्रशासित प्रदेशातील जुने गाव."), meta=L("Heritage", "धरोहर", "वारसा")),
    ], title=L("Main settlements", "मुख्य बस्तियाँ", "मुख्य वस्त्या"), conf="Editorial"),
])

module(R, "sports", [
    prose("p1", L(
        "Chandigarh has produced many international athletes, among them the cricketers Kapil Dev and Yuvraj Singh and the shooter Abhinav Bindra, India's first individual Olympic gold medallist (Beijing 2008). The Sector 16 cricket stadium and the Lake Sports Complex are major venues.",
        "चंडीगढ़ ने कई अंतरराष्ट्रीय खिलाड़ी दिए हैं, जिनमें क्रिकेटर कपिल देव और युवराज सिंह और भारत के पहले व्यक्तिगत ओलंपिक स्वर्ण पदक विजेता (बीजिंग 2008) निशानेबाज़ अभिनव बिंद्रा शामिल हैं। सेक्टर 16 क्रिकेट स्टेडियम और लेक स्पोर्ट्स कॉम्प्लेक्स प्रमुख स्थल हैं।",
        "चंदीगडने अनेक आंतरराष्ट्रीय खेळाडू दिले आहेत, ज्यांत क्रिकेटपटू कपिल देव व युवराज सिंग आणि भारताचे पहिले वैयक्तिक ऑलिंपिक सुवर्णपदकविजेते (बीजिंग 2008) नेमबाज अभिनव बिंद्रा यांचा समावेश आहे. सेक्टर 16 क्रिकेट स्टेडियम व लेक स्पोर्ट्स कॉम्प्लेक्स ही प्रमुख ठिकाणे आहेत."),
        conf="Editorial"),
])

module(R, "personalities", [
    lst("people", [
        person("corbusier", ("Le Corbusier", "ले कॉर्बुज़िए", "ले कॉर्बुझिए"), ("Architect and planner of the city.", "नगर के वास्तुकार और योजनाकार।", "शहराचे वास्तुविशारद व नियोजक."), ("Architecture", "वास्तुकला", "वास्तुकला")),
        person("nekchand", ("Nek Chand", "नेक चंद", "नेक चंद"), ("Creator of the Rock Garden.", "रॉक गार्डन के निर्माता।", "रॉक गार्डनचे निर्माते."), ("Art", "कला", "कला")),
        person("bindra", ("Abhinav Bindra", "अभिनव बिंद्रा", "अभिनव बिंद्रा"), ("Shooter; Olympic gold at Beijing 2008.", "निशानेबाज़; बीजिंग 2008 में ओलंपिक स्वर्ण।", "नेमबाज; बीजिंग 2008 मध्ये ऑलिंपिक सुवर्ण."), ("Sport", "खेल", "क्रीडा")),
        person("kapil", ("Kapil Dev", "कपिल देव", "कपिल देव"), ("Captain of India's 1983 World Cup-winning cricket team.", "1983 विश्व कप विजेता भारतीय क्रिकेट टीम के कप्तान।", "1983 विश्वचषक विजेत्या भारतीय क्रिकेट संघाचे कर्णधार."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

module(R, "diaspora", [
    prose("p1", L(
        "Like much of Punjab, Chandigarh has strong links with Punjabi communities in Canada, the United Kingdom, Australia and the United States, and many young people go abroad to study.",
        "पंजाब के बड़े भाग की तरह चंडीगढ़ के कनाडा, ब्रिटेन, ऑस्ट्रेलिया और अमेरिका के पंजाबी समुदायों से मज़बूत संबंध हैं, और बहुत से युवा पढ़ने विदेश जाते हैं।",
        "पंजाबच्या बऱ्याच भागाप्रमाणे चंदीगडचे कॅनडा, ब्रिटन, ऑस्ट्रेलिया व अमेरिकेतील पंजाबी समुदायांशी घट्ट संबंध आहेत, आणि अनेक तरुण शिक्षणासाठी परदेशी जातात."),
        conf="Editorial"),
])

module(R, "civic", [links([
    it3("portal", "Chandigarh Administration", "चंडीगढ़ प्रशासन", "चंदीगड प्रशासन", url="https://chandigarh.gov.in", src="india-gov"), RTI])])

module(R, "trivia", [
    lst("facts", [
        triv("capital", ("Chandigarh is the capital of two States, Punjab and Haryana.", "चंडीगढ़ दो राज्यों, पंजाब और हरियाणा, की राजधानी है।", "चंदीगड ही दोन राज्यांची, पंजाब व हरियाणाची, राजधानी आहे.")),
        triv("unesco", ("The Capitol Complex is part of a World Heritage Site spread over seven countries.", "कैपिटल कॉम्प्लेक्स सात देशों में फैले एक विश्व धरोहर स्थल का भाग है।", "कॅपिटल कॉम्प्लेक्स सात देशांत पसरलेल्या जागतिक वारसा स्थळाचा भाग आहे."), UNESCO, "unesco-whc"),
        triv("density", ("Chandigarh had about 9,258 people per km² in 2011.", "2011 में चंडीगढ़ में प्रति वर्ग किमी लगभग 9,258 लोग थे।", "2011 मध्ये चंदीगडमध्ये प्रति चौ.किमी सुमारे 9,258 लोक होते."), PYD, "census"),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("ch ok")
