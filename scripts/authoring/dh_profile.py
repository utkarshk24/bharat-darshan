"""Dadra and Nagar Haveli and Daman and Diu — Phase 3 profile (core + all modules). Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from ut_kit import *

R = "IN-DH"
NAME = L("Dadra and Nagar Haveli and Daman and Diu", "दादरा और नगर हवेली और दमन और दीव", "दादरा आणि नगर हवेली आणि दमण आणि दीव")
ADM = "https://lakshadweep.gov.in/about-lakshadweep/profile-administrator/"
NAMO = "https://www.deccanherald.com/amp/story/india%2Fdaman-and-diu%2Fpm-modi-inaugurates-namo-hospital-in-silvassa-3436729"
dnh, dd = C["pop"]["DNH"], C["pop"]["DD"]
POP = dnh[0] + dd[0]; MALE = dnh[1] + dd[1]; FEM = dnh[2] + dd[2]
SR = round(1000 * FEM / MALE)

r = read("regions/IN-DH.json"); m = r["metrics"]
SEP = "Census 2011 was taken for the two former UTs separately; the combined figure is computed here."
m["population2011"] = dp(POP, "persons", "2011", "census", "census", PYD,
    note=f"{SEP} Dadra and Nagar Haveli {inr(dnh[0])}; Daman and Diu {inr(dd[0])} (Puducherry DES table citing ORGI).")
m["area"] = dp(602, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(round(POP / 602), "persons per km²", "2011", "census", "census", PYD, note=f"Calculated: combined Census 2011 population {inr(POP)} ÷ 602 km².")
m["sexRatio2011"] = dp(SR, "females per 1000 males", "2011", "census", "census", PYD,
    note=f"Computed from combined males {inr(MALE)} and females {inr(FEM)}. Separately: Dadra and Nagar Haveli {dnh[4]}, Daman and Diu {dd[4]}.")
m["childSexRatio2011"] = dp(None, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR,
    note=f"Not combined: the two former UTs had {C['csr']['DNH'][1]} (Dadra and Nagar Haveli) and {C['csr']['DD'][1]} (Daman and Diu) in 2011 (PIB, 11 Feb 2014). A combined figure needs the 0–6 population.")
m["literacyRate2011"] = dp(None, "%", "2011", "census", "es-india", ESI_LIT,
    note=f"Not combined: Dadra and Nagar Haveli {C['lit']['DNH']}%, Daman and Diu {C['lit']['DD']}% (Economic Survey 2021-22, Table 8.5). A combined rate needs the population aged 7+.")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None, note="Needs the Census 2011 Primary Census Abstract for both former UTs.")
m["gsdpCurrent"] = todo("₹ crore", "FY2024-25", "fy", "mospi", "MoSPI's state series returned no rows for Dadra and Nagar Haveli and Daman and Diu.", base=CUR)
m["perCapitaNsdpCurrent"] = todo("₹", "FY2024-25", "fy", "mospi", "Not published by MoSPI for this UT.", base=CUR)
m["forestCoverPct"] = dp(37.48, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST, note="Computed from ISFR 2023 forest cover 225.62 km² ÷ geographical area 602 km².")
r["officialPortal"] = "https://ddd.gov.in"
r["government"] = {
    "headOfState": office("administrator", L("Praful Khoda Patel", "प्रफुल्ल खोड़ा पटेल", "प्रफुल्ल खोडा पटेल"), None, None, "ld-gov", ADM, "https://ddd.gov.in", conf="Official",
                          note="Administrator of Dadra and Nagar Haveli and Daman and Diu (also Administrator of Lakshadweep since 5 December 2020), as stated on the Lakshadweep Administration's profile page. He became Administrator of the merged UT when it was formed on 26 January 2020; the start date is to be confirmed from an official notification."),
    "headOfGovernment": None, "others": [],
}
r["projects"] = [
    proj("namo-hospital", L("NAMO Hospital (Phase I), Silvassa", "नमो अस्पताल (चरण I), सिलवासा", "नमो रुग्णालय (टप्पा I), सिलवासा"),
         L("A 450-bed hospital in Silvassa, built at a cost of about ₹460 crore and inaugurated by the Prime Minister on 7 March 2025, to give the UT and nearby tribal areas of Gujarat and Maharashtra specialist care close to home. It is attached to the NAMO Medical Education and Research Institute.",
           "सिलवासा में 450 बिस्तरों वाला अस्पताल, जो लगभग ₹460 करोड़ की लागत से बना और जिसका प्रधानमंत्री ने 7 मार्च 2025 को उद्घाटन किया, ताकि केंद्र शासित प्रदेश और गुजरात व महाराष्ट्र के पास के जनजातीय क्षेत्रों को घर के पास विशेषज्ञ उपचार मिले। यह नमो चिकित्सा शिक्षा एवं अनुसंधान संस्थान से जुड़ा है।",
           "सिलवासा येथील 450 खाटांचे रुग्णालय, जे सुमारे ₹460 कोटी खर्चून बांधले गेले व ज्याचे पंतप्रधानांनी 7 मार्च 2025 रोजी उद्घाटन केले, जेणेकरून केंद्रशासित प्रदेश व गुजरात आणि महाराष्ट्रातील जवळच्या आदिवासी भागांना घराजवळ विशेषज्ञ उपचार मिळावेत. ते नमो वैद्यकीय शिक्षण व संशोधन संस्थेशी संलग्न आहे."),
         "health", "UT Administration of DNH and DD", 460, "About ₹460 crore (Deccan Herald/PTI, 7 Mar 2025).", "2025", None, "7 March 2025", "Completed", "deccan-herald", NAMO, conf="Third-party verified"),
]
r["giProducts"] = gi_list("gi_dh.tsv", {"Warli Painting": ("वारली चित्रकला", "वारली चित्रकला")}, {"MH,GJ,DNH,DD": ["Maharashtra", "Gujarat"]}, set())
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-DH.json", r)
m = r["metrics"]

module(R, "overview", [
    prose("intro", L(
        "Dadra and Nagar Haveli and Daman and Diu is a Union Territory on India's west coast formed on 26 January 2020 by merging two former UTs. It has three separate parts: Dadra and Nagar Haveli, an inland, forested area between Gujarat and Maharashtra; Daman, on the Gujarat coast at the mouth of the Damanganga; and Diu, an island off the southern tip of Saurashtra. Daman is the capital, and Silvassa is the largest town.\n\nAll three were Portuguese territories for centuries — Daman and Diu until 1961 — and their forts, churches and old quarters still show that past. Today Silvassa and Daman are important manufacturing centres, while Diu is known for its beaches and fort.",
        "दादरा और नगर हवेली और दमन और दीव भारत के पश्चिमी तट पर एक केंद्र शासित प्रदेश है, जो 26 जनवरी 2020 को दो पूर्व केंद्र शासित प्रदेशों के विलय से बना। इसके तीन अलग भाग हैं: दादरा और नगर हवेली, गुजरात और महाराष्ट्र के बीच एक भीतरी, वनाच्छादित क्षेत्र; दमन, दमनगंगा के मुहाने पर गुजरात तट पर; और दीव, सौराष्ट्र के दक्षिणी सिरे के पास एक द्वीप। दमन राजधानी है, और सिलवासा सबसे बड़ा नगर।\n\nतीनों सदियों तक पुर्तगाली क्षेत्र रहे — दमन और दीव 1961 तक — और उनके क़िले, चर्च और पुराने मोहल्ले अब भी वह अतीत दिखाते हैं। आज सिलवासा और दमन महत्त्वपूर्ण विनिर्माण केंद्र हैं, जबकि दीव अपने तटों और क़िले के लिए जाना जाता है।",
        "दादरा आणि नगर हवेली आणि दमण आणि दीव हा भारताच्या पश्चिम किनाऱ्यावरील केंद्रशासित प्रदेश असून 26 जानेवारी 2020 रोजी दोन पूर्वीच्या केंद्रशासित प्रदेशांच्या विलीनीकरणाने तयार झाला. त्याचे तीन वेगळे भाग आहेत: दादरा आणि नगर हवेली, गुजरात व महाराष्ट्रादरम्यानचा अंतर्गत, वनाच्छादित प्रदेश; दमण, दमणगंगेच्या मुखाशी गुजरात किनाऱ्यावर; आणि दीव, सौराष्ट्राच्या दक्षिण टोकाजवळील बेट. दमण ही राजधानी आहे, आणि सिलवासा हे सर्वांत मोठे शहर.\n\nतिन्ही भाग शतकानुशतके पोर्तुगीज प्रदेश होते — दमण व दीव 1961 पर्यंत — आणि त्यांचे किल्ले, चर्च व जुन्या वस्त्या अजूनही तो भूतकाळ दाखवतात. आज सिलवासा व दमण महत्त्वाची उत्पादन केंद्रे आहेत, तर दीव किनारे व किल्ल्यासाठी ओळखले जाते."),
        sources=["census", "fsi"], conf="Editorial"),
    admin_table([
        row("Status", "दर्जा", "दर्जा", ("Union Territory without a legislature (merged UT since 26 January 2020)", "बिना विधानसभा वाला केंद्र शासित प्रदेश (26 जनवरी 2020 से संयुक्त)", "विधिमंडळ नसलेला केंद्रशासित प्रदेश (26 जानेवारी 2020 पासून संयुक्त)")),
        row("Districts", "ज़िले", "जिल्हे", ("3 (Dadra and Nagar Haveli, Daman, Diu)", "3 (दादरा और नगर हवेली, दमन, दीव)", "3 (दादरा आणि नगर हवेली, दमण, दीव)")),
        row("Capital", "राजधानी", "राजधानी", ("Daman", "दमन", "दमण")),
        row("High Court", "उच्च न्यायालय", "उच्च न्यायालय", ("Bombay High Court", "बॉम्बे उच्च न्यायालय", "मुंबई उच्च न्यायालय")),
        row("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक", "DD"),
        row("Time zone", "समय क्षेत्र", "प्रमाणवेळ", "IST (UTC+05:30)"),
    ]),
])

module(R, "geography", [
    prose("p1", L(
        "Dadra and Nagar Haveli lies in the foothills of the Western Ghats, crossed by the Damanganga river and its tributaries, with forests, hills and the Madhuban reservoir. Daman, about 30 km to the west, is a flat coastal strip split by the Damanganga into Nani Daman and Moti Daman. Diu, more than 600 km away by road, is a small limestone island separated from Gujarat by a tidal creek.",
        "दादरा और नगर हवेली पश्चिमी घाट की तलहटी में है, जिसे दमनगंगा नदी और उसकी सहायक नदियाँ पार करती हैं, जहाँ वन, पहाड़ियाँ और मधुबन जलाशय हैं। लगभग 30 किमी पश्चिम में दमन एक समतल तटीय पट्टी है, जिसे दमनगंगा नानी दमन और मोटी दमन में बाँटती है। सड़क से 600 किमी से अधिक दूर दीव एक छोटा चूना पत्थर द्वीप है, जो एक ज्वारीय खाड़ी से गुजरात से अलग है।",
        "दादरा आणि नगर हवेली पश्चिम घाटाच्या पायथ्याशी आहे, जिथून दमणगंगा नदी व तिच्या उपनद्या वाहतात, जंगले, टेकड्या व मधुबन जलाशयासह. सुमारे 30 किमी पश्चिमेला दमण ही सपाट किनारपट्टी आहे, जिला दमणगंगा नानी दमण व मोटी दमणमध्ये विभागते. रस्त्याने 600 किमीहून अधिक दूर दीव हे लहान चुनखडीचे बेट असून भरतीच्या खाडीने गुजरातपासून वेगळे आहे."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), m["area"], "number", national=IND["area"])]),
])

module(R, "climate", [
    prose("p1", L(
        "All three parts have a tropical climate. Dadra and Nagar Haveli and Daman receive heavy south-west monsoon rain from June to September; Diu is drier. Winters from November to February are pleasant.",
        "तीनों भागों की जलवायु उष्णकटिबंधीय है। दादरा और नगर हवेली और दमन में जून से सितंबर तक भारी दक्षिण-पश्चिम मानसूनी वर्षा होती है; दीव अधिक सूखा है। नवंबर से फ़रवरी तक सर्दियाँ सुहावनी होती हैं।",
        "तिन्ही भागांचे हवामान उष्णकटिबंधीय आहे. दादरा आणि नगर हवेली व दमणमध्ये जून ते सप्टेंबर मुसळधार नैर्ऋत्य मान्सूनी पाऊस पडतो; दीव अधिक कोरडे आहे. नोव्हेंबर ते फेब्रुवारी हिवाळा सुखद असतो."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Daman", "दमन", "दमण"), "lat": 20.3974, "lon": 72.8328},
        {"name": L("Silvassa", "सिलवासा", "सिलवासा"), "lat": 20.2766, "lon": 73.0083},
        {"name": L("Diu", "दीव", "दीव"), "lat": 20.7144, "lon": 70.9874},
    ]},
])

module(R, "vibe", [
    prose("p1", L(
        "Silvassa is a busy industrial town surrounded by tribal villages and forest; Daman mixes fishing villages, Portuguese-era churches and factories; and Diu is quiet, with whitewashed lanes, churches and a slow pace. Many visitors come from Gujarat for the beaches.",
        "सिलवासा जनजातीय गाँवों और वनों से घिरा एक व्यस्त औद्योगिक नगर है; दमन मछुआरों के गाँवों, पुर्तगाली काल के चर्चों और कारख़ानों का मेल है; और दीव शांत है, सफ़ेद पुती गलियों, चर्चों और धीमी गति के साथ। बहुत से पर्यटक तटों के लिए गुजरात से आते हैं।",
        "सिलवासा हे आदिवासी गावे व जंगलांनी वेढलेले गजबजलेले औद्योगिक शहर आहे; दमण मच्छीमार गावे, पोर्तुगीजकालीन चर्च व कारखाने यांचा मेळ आहे; आणि दीव शांत आहे, पांढऱ्या रंगवलेल्या गल्ल्या, चर्च व संथ गतीसह. अनेक पर्यटक किनाऱ्यांसाठी गुजरातमधून येतात."),
        conf="Editorial"),
])

module(R, "people", [
    prose("p1", L(
        f"The two former UTs together had about {inr(POP)} people at the 2011 Census. Their sex ratios were unusually low — {dnh[4]} women per 1,000 men in Dadra and Nagar Haveli and {dd[4]} in Daman and Diu — because of the many male workers who came for factory jobs. Literacy was {C['lit']['DNH']}% in Dadra and Nagar Haveli and {C['lit']['DD']}% in Daman and Diu. Scheduled Tribes, mainly the Warli, Kokna, Dhodia and Dubla, made up 52% of the population of Dadra and Nagar Haveli. Gujarati, Hindi and Marathi are widely spoken, and Portuguese is still heard among older residents of Daman and Diu.",
        f"2011 की जनगणना में दोनों पूर्व केंद्र शासित प्रदेशों की कुल जनसंख्या लगभग {inr(POP)} थी। उनके लिंगानुपात असामान्य रूप से कम थे — दादरा और नगर हवेली में प्रति 1,000 पुरुषों पर {dnh[4]} महिलाएँ और दमन और दीव में {dd[4]} — कारख़ानों में नौकरी के लिए आए बहुत से पुरुष मज़दूरों के कारण। साक्षरता दादरा और नगर हवेली में {C['lit']['DNH']}% और दमन और दीव में {C['lit']['DD']}% थी। अनुसूचित जनजातियाँ, मुख्यतः वारली, कोकना, धोडिया और दुबला, दादरा और नगर हवेली की जनसंख्या का 52% थीं। गुजराती, हिंदी और मराठी व्यापक रूप से बोली जाती हैं, और दमन और दीव के पुराने निवासियों में पुर्तगाली अब भी सुनाई देती है।",
        f"2011 च्या जनगणनेनुसार दोन्ही पूर्वीच्या केंद्रशासित प्रदेशांची एकूण लोकसंख्या सुमारे {inr(POP)} होती. त्यांचे लिंग गुणोत्तर असामान्यपणे कमी होते — दादरा आणि नगर हवेलीत दर 1,000 पुरुषांमागे {dnh[4]} स्त्रिया व दमण आणि दीवमध्ये {dd[4]} — कारखान्यांतील नोकऱ्यांसाठी आलेल्या अनेक पुरुष कामगारांमुळे. साक्षरता दादरा आणि नगर हवेलीत {C['lit']['DNH']}% व दमण आणि दीवमध्ये {C['lit']['DD']}% होती. अनुसूचित जमाती, मुख्यतः वारली, कोकणा, धोडिया व दुबळा, दादरा आणि नगर हवेलीच्या लोकसंख्येच्या 52% होत्या. गुजराती, हिंदी व मराठी मोठ्या प्रमाणावर बोलल्या जातात, आणि दमण व दीवच्या जुन्या रहिवाशांत पोर्तुगीज अजूनही ऐकू येते."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", people_facts("DH", m, "DNH", None)[:1] + [
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), m["sexRatio2011"], "ratio", "higher-is-better", national=IND["sexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), m["literacyRate2011"], "percent", "higher-is-better", national=IND["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), m["density2011"], "number"),
        fact("st", L("Scheduled Tribes, Dadra and Nagar Haveli", "अनुसूचित जनजातियाँ, दादरा और नगर हवेली", "अनुसूचित जमाती, दादरा आणि नगर हवेली"),
             dp(52.0, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011 for the former UT of Dadra and Nagar Haveli (1.78 lakh). Daman and Diu: 6.3%."), "percent"),
    ], title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
])

module(R, "history", [
    prose("p1", L(
        "Diu was taken by the Portuguese in 1535 and fortified, and Daman in 1559; Dadra and Nagar Haveli came under Portuguese control in 1779–1783 through a treaty with the Marathas. In 1954 volunteers ended Portuguese rule in Dadra and Nagar Haveli, which ran itself as the Free Dadra and Nagar Haveli until it was merged with India on 11 August 1961. Indian forces ended Portuguese rule in Goa, Daman and Diu on 19 December 1961. Daman and Diu were part of the UT of Goa, Daman and Diu until Goa became a State in 1987, and the two UTs were merged on 26 January 2020 under the Dadra and Nagar Haveli and Daman and Diu (Merger of Union Territories) Act, 2019.",
        "पुर्तगालियों ने 1535 में दीव और 1559 में दमन पर अधिकार कर क़िलेबंदी की; दादरा और नगर हवेली 1779–1783 में मराठों के साथ संधि से पुर्तगाली नियंत्रण में आया। 1954 में स्वयंसेवकों ने दादरा और नगर हवेली में पुर्तगाली शासन समाप्त किया, जो 11 अगस्त 1961 को भारत में विलय तक स्वतंत्र दादरा और नगर हवेली के रूप में स्वयं शासित रहा। 19 दिसंबर 1961 को भारतीय सेना ने गोवा, दमन और दीव में पुर्तगाली शासन समाप्त किया। 1987 में गोवा के राज्य बनने तक दमन और दीव गोवा, दमन और दीव केंद्र शासित प्रदेश का भाग थे, और दादरा और नगर हवेली और दमन और दीव (केंद्र शासित प्रदेशों का विलय) अधिनियम, 2019 के तहत 26 जनवरी 2020 को दोनों केंद्र शासित प्रदेश विलीन हुए।",
        "पोर्तुगीजांनी 1535 मध्ये दीव व 1559 मध्ये दमण ताब्यात घेऊन तटबंदी केली; दादरा आणि नगर हवेली 1779–1783 मध्ये मराठ्यांसोबतच्या तहाने पोर्तुगीज ताब्यात आले. 1954 मध्ये स्वयंसेवकांनी दादरा आणि नगर हवेलीतील पोर्तुगीज राजवट संपवली, जे 11 ऑगस्ट 1961 रोजी भारतात विलीन होईपर्यंत स्वतंत्र दादरा आणि नगर हवेली म्हणून स्वशासित राहिले. 19 डिसेंबर 1961 रोजी भारतीय सैन्याने गोवा, दमण व दीवमधील पोर्तुगीज राजवट संपवली. 1987 मध्ये गोवा राज्य होईपर्यंत दमण व दीव गोवा, दमण आणि दीव केंद्रशासित प्रदेशाचा भाग होते, आणि दादरा आणि नगर हवेली आणि दमण आणि दीव (केंद्रशासित प्रदेशांचे विलीनीकरण) अधिनियम, 2019 अन्वये 26 जानेवारी 2020 रोजी दोन्ही केंद्रशासित प्रदेश विलीन झाले."),
        conf="Editorial"),
    timeline([
        ev("diu", 1535, L("1535", "1535", "1535"), L("Portuguese take Diu", "पुर्तगालियों ने दीव लिया", "पोर्तुगीजांनी दीव घेतले")),
        ev("daman", 1559, L("1559", "1559", "1559"), L("Portuguese take Daman", "पुर्तगालियों ने दमन लिया", "पोर्तुगीजांनी दमण घेतले")),
        ev("free", 1954, L("1954", "1954", "1954"), L("Dadra and Nagar Haveli freed from Portuguese rule", "दादरा और नगर हवेली पुर्तगाली शासन से मुक्त", "दादरा आणि नगर हवेली पोर्तुगीज राजवटीतून मुक्त")),
        ev("merge61", 1961, L("1961", "1961", "1961"), L("Merger with India; Daman and Diu liberated", "भारत में विलय; दमन और दीव मुक्त", "भारतात विलीनीकरण; दमण व दीव मुक्त")),
        ev("ut87", 1987, L("1987", "1987", "1987"), L("Daman and Diu a separate UT", "दमन और दीव अलग केंद्र शासित प्रदेश", "दमण व दीव स्वतंत्र केंद्रशासित प्रदेश")),
        ev("merge20", 2020, L("26 January 2020", "26 जनवरी 2020", "26 जानेवारी 2020"), L("The two UTs merged", "दोनों केंद्र शासित प्रदेश विलीन", "दोन्ही केंद्रशासित प्रदेश विलीन")),
    ]),
    lst("heritage", [
        it3("diufort", "Diu Fort", "दीव क़िला", "दीव किल्ला", m=("16th century", "16वीं सदी", "सोळावे शतक")),
        it3("motidaman", "Moti Daman Fort and Bom Jesus Church", "मोटी दमन क़िला और बॉम जीसस चर्च", "मोटी दमण किल्ला व बॉम जीझस चर्च"),
        it3("stpaul", "St Paul's Church, Diu", "सेंट पॉल चर्च, दीव", "सेंट पॉल चर्च, दीव"),
        it3("khukri", "INS Khukri Memorial, Diu", "आईएनएस खुकरी स्मारक, दीव", "आयएनएस खुकरी स्मारक, दीव"),
    ], title=L("Heritage", "धरोहर", "वारसा"), conf="Editorial"),
])

module(R, "culture", [
    prose("p1", L(
        "Warli painting, with its stick figures of daily life and festivals, belongs to the Warli tribe of Dadra and Nagar Haveli and neighbouring Gujarat and Maharashtra, and is a GI shared by these regions. Tribal dances such as the tarpa dance are performed at festivals and at the annual Tarpa Festival in Silvassa. Daman and Diu keep Portuguese-era church feasts alongside Gujarati festivals such as Navratri, and fishing communities celebrate Nariyal Purnima.",
        "दैनिक जीवन और त्योहारों की रेखा-आकृतियों वाली वारली चित्रकला दादरा और नगर हवेली और पड़ोसी गुजरात व महाराष्ट्र की वारली जनजाति की है, और इन क्षेत्रों का साझा जीआई है। तारपा नृत्य जैसे जनजातीय नृत्य त्योहारों पर और सिलवासा के वार्षिक तारपा महोत्सव में किए जाते हैं। दमन और दीव पुर्तगाली काल के चर्च उत्सवों के साथ नवरात्रि जैसे गुजराती त्योहार मनाते हैं, और मछुआरा समुदाय नारियल पूर्णिमा मनाते हैं।",
        "दैनंदिन जीवन व सणांच्या रेषाकृती असलेली वारली चित्रकला दादरा आणि नगर हवेली व शेजारच्या गुजरात आणि महाराष्ट्रातील वारली जमातीची आहे, आणि या प्रदेशांचा सामायिक जीआय आहे. तारपा नृत्यासारखी आदिवासी नृत्ये सणांना व सिलवासाच्या वार्षिक तारपा महोत्सवात सादर होतात. दमण व दीव पोर्तुगीजकालीन चर्च उत्सवांसोबत नवरात्रीसारखे गुजराती सण साजरे करतात, आणि मच्छीमार समुदाय नारळी पौर्णिमा साजरी करतात."),
        conf="Editorial"),
])

ur = AP["plfs_ur_15plus_psss"]["DH"]; lf = AP["plfs_lfpr_2025"]["DH"]
module(R, "economy", [
    prose("p1", L(
        f"Tax incentives from the 1980s turned Silvassa and Daman into manufacturing centres for textiles and yarn, plastics, pharmaceuticals, electrical goods and packaging, drawing workers from across India. Fishing is important in Daman and Diu, and tourism in Diu and Daman. MoSPI does not publish a GSDP series for the UT. The PLFS unemployment rate was low at {ur['2025']}% in 2025, and {lf['person']}% of people aged 15+ were in the labour force.",
        f"1980 के दशक के कर प्रोत्साहनों ने सिलवासा और दमन को वस्त्र और धागा, प्लास्टिक, दवा, विद्युत सामान और पैकेजिंग के विनिर्माण केंद्र बना दिया, जो पूरे भारत से मज़दूरों को खींचते हैं। दमन और दीव में मछली पकड़ना और दीव व दमन में पर्यटन महत्त्वपूर्ण है। मोस्पी इस केंद्र शासित प्रदेश के लिए जीएसडीपी शृंखला प्रकाशित नहीं करता। पीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% पर कम थी, और 15+ आयु के {lf['person']}% लोग श्रम बल में थे।",
        f"1980 च्या दशकातील कर सवलतींमुळे सिलवासा व दमण वस्त्र व धागा, प्लास्टिक, औषधे, विद्युत साहित्य व पॅकेजिंगची उत्पादन केंद्रे बनली, जी संपूर्ण भारतातून कामगार आकर्षित करतात. दमण व दीवमध्ये मासेमारी व दीव आणि दमणमध्ये पर्यटन महत्त्वाचे आहे. मोस्पी या केंद्रशासित प्रदेशासाठी जीएसडीपी मालिका प्रसिद्ध करत नाही. पीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% इतका कमी होता, आणि 15+ वयाच्या {lf['person']}% व्यक्ती श्रमशक्तीत होत्या."),
        sources=["plfs"], conf="Official"),
    facts("f", plfs_facts("DH", NAME), title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    plfs_series("DH", NAME),
    gaps("g", [(L("GSDP and per capita income", "जीएसडीपी और प्रति व्यक्ति आय", "जीएसडीपी व दरडोई उत्पन्न"), "mospi", "Not in the MoSPI State series; check the UT Planning and Statistics Department.")]),
])

module(R, "government", [
    prose("p1", L(
        "The UT has no legislature and is run by an Administrator appointed by the President, with district administrations at Silvassa, Daman and Diu. Each part has elected municipal and panchayat bodies, and the UT elects two members to the Lok Sabha — one for Dadra and Nagar Haveli and one for Daman and Diu. Courts come under the Bombay High Court. Praful Khoda Patel has been Administrator since the merger.",
        "केंद्र शासित प्रदेश में विधानसभा नहीं है और इसे राष्ट्रपति द्वारा नियुक्त प्रशासक चलाते हैं, सिलवासा, दमन और दीव में ज़िला प्रशासनों के साथ। हर भाग में निर्वाचित नगर और पंचायत निकाय हैं, और केंद्र शासित प्रदेश से लोकसभा के दो सदस्य चुने जाते हैं — एक दादरा और नगर हवेली से और एक दमन और दीव से। न्यायालय बॉम्बे उच्च न्यायालय के अंतर्गत हैं। प्रफुल्ल खोड़ा पटेल विलय से प्रशासक हैं।",
        "केंद्रशासित प्रदेशात विधिमंडळ नाही आणि राष्ट्रपतींनी नेमलेले प्रशासक त्याचा कारभार पाहतात, सिलवासा, दमण व दीव येथील जिल्हा प्रशासनांसह. प्रत्येक भागात निवडून आलेल्या नगर व पंचायत संस्था आहेत, आणि केंद्रशासित प्रदेशातून लोकसभेवर दोन सदस्य निवडले जातात — एक दादरा आणि नगर हवेलीतून व एक दमण आणि दीवमधून. न्यायालये मुंबई उच्च न्यायालयाच्या अखत्यारीत आहेत. प्रफुल्ल खोडा पटेल विलीनीकरणापासून प्रशासक आहेत."),
        sources=["ld-gov"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
])

module(R, "projects", [
    prose("p1", L(
        "The NAMO Hospital and the NAMO Medical Education and Research Institute in Silvassa have expanded health care in the UT. Other works, such as roads and smart-city projects in Silvassa, Daman and Diu, will be added once their status is confirmed from official sources.",
        "सिलवासा के नमो अस्पताल और नमो चिकित्सा शिक्षा एवं अनुसंधान संस्थान ने केंद्र शासित प्रदेश में स्वास्थ्य सेवा का विस्तार किया है। सिलवासा, दमन और दीव में सड़क और स्मार्ट सिटी परियोजनाओं जैसे अन्य कार्य आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर जोड़े जाएँगे।",
        "सिलवासा येथील नमो रुग्णालय व नमो वैद्यकीय शिक्षण व संशोधन संस्थेने केंद्रशासित प्रदेशातील आरोग्यसेवेचा विस्तार केला आहे. सिलवासा, दमण व दीवमधील रस्ते व स्मार्ट सिटी प्रकल्पांसारखी इतर कामे अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर जोडली जातील."),
        sources=["deccan-herald"], conf="Third-party verified"),
    {"type": "projects", "id": "projects"},
])

module(R, "transport", [
    prose("p1", L(
        "Vapi, on the Mumbai–Ahmedabad railway in Gujarat, is the nearest station for both Silvassa and Daman, and NH-48 runs close by. Daman has a small airport used mainly by the Coast Guard, and Diu has an airport with flights to Mumbai and Ahmedabad; Diu is also reached by road from Una in Gujarat.",
        "गुजरात में मुंबई–अहमदाबाद रेल लाइन पर वापी सिलवासा और दमन दोनों का निकटतम स्टेशन है, और एनएच-48 पास से गुज़रता है। दमन में एक छोटा हवाई अड्डा है जिसका उपयोग मुख्यतः तटरक्षक बल करता है, और दीव में मुंबई और अहमदाबाद की उड़ानों वाला हवाई अड्डा है; दीव गुजरात के ऊना से सड़क द्वारा भी पहुँचा जाता है।",
        "गुजरातमधील मुंबई–अहमदाबाद रेल्वेमार्गावरील वापी हे सिलवासा व दमण दोन्हींसाठी जवळचे स्थानक आहे, आणि एनएच-48 जवळून जातो. दमणमध्ये प्रामुख्याने तटरक्षक दल वापरत असलेला लहान विमानतळ आहे, आणि दीवमध्ये मुंबई व अहमदाबादसाठी उड्डाणे असलेला विमानतळ आहे; दीवला गुजरातमधील उनाहून रस्त्यानेही जाता येते."),
        conf="Editorial"),
])

module(R, "energy", [
    prose("p1", L(
        "The UT buys almost all its electricity from central power stations through the western grid; demand is dominated by industry in Silvassa and Daman. Diu has solar plants that supply much of its daytime demand.",
        "केंद्र शासित प्रदेश अपनी लगभग पूरी बिजली पश्चिमी ग्रिड से केंद्रीय बिजलीघरों से ख़रीदता है; माँग में सिलवासा और दमन के उद्योग प्रमुख हैं। दीव में सौर संयंत्र हैं जो दिन की माँग का बड़ा भाग पूरा करते हैं।",
        "केंद्रशासित प्रदेश जवळपास सर्व वीज पश्चिम ग्रिडमार्फत केंद्रीय वीजकेंद्रांकडून खरेदी करतो; मागणीत सिलवासा व दमणमधील उद्योग प्रमुख आहेत. दीवमध्ये सौर प्रकल्प आहेत जे दिवसाच्या मागणीचा मोठा भाग पुरवतात."),
        conf="Editorial"),
    gaps("g", [(L("Diu solar — official record", "दीव सौर — आधिकारिक अभिलेख", "दीव सौर — अधिकृत नोंद"), "mnre", "UT Electricity Department / MNRE.")]),
])

module(R, "digital", [
    prose("p1", L(
        "Mobile and broadband networks cover the towns and most villages, and the UT offers many services online through its portal.",
        "मोबाइल और ब्रॉडबैंड नेटवर्क नगरों और अधिकांश गाँवों को कवर करते हैं, और केंद्र शासित प्रदेश अपने पोर्टल से कई सेवाएँ ऑनलाइन देता है।",
        "मोबाइल व ब्रॉडबँड जाळे शहरे व बहुतेक गावांना व्यापते, आणि केंद्रशासित प्रदेश आपल्या संकेतस्थळावरून अनेक सेवा ऑनलाइन देतो."),
        conf="Editorial"),
])

ef, es = aishe_block("DH", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["DH"]
module(R, "education", [
    prose("p1", L(
        f"The higher-education gross enrolment ratio was {AP['aishe_ger']['DH']['2021-22']}% in 2021-22 in AISHE, far below the national 28.4%, with women at {gf}% and men at {gm}%; many students study in Gujarat and Maharashtra. The NAMO Medical Education and Research Institute in Silvassa, engineering and polytechnic colleges and government colleges in Silvassa, Daman and Diu are the main institutions.",
        f"एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात {AP['aishe_ger']['DH']['2021-22']}% था, जो राष्ट्रीय 28.4% से बहुत कम है, महिलाएँ {gf}% और पुरुष {gm}%; बहुत से छात्र गुजरात और महाराष्ट्र में पढ़ते हैं। सिलवासा का नमो चिकित्सा शिक्षा एवं अनुसंधान संस्थान, इंजीनियरिंग और पॉलिटेक्निक कॉलेज और सिलवासा, दमन और दीव के सरकारी कॉलेज मुख्य संस्थान हैं।",
        f"एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर {AP['aishe_ger']['DH']['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा खूप कमी, स्त्रिया {gf}% व पुरुष {gm}%; अनेक विद्यार्थी गुजरात व महाराष्ट्रात शिकतात. सिलवासा येथील नमो वैद्यकीय शिक्षण व संशोधन संस्था, अभियांत्रिकी व पॉलिटेक्निक महाविद्यालये आणि सिलवासा, दमण व दीवमधील शासकीय महाविद्यालये या मुख्य संस्था आहेत."),
        sources=["aishe"], conf="Official"),
    ef, es,
])

n = NF["DH"]
module(R, "health", [
    prose("p1", L(
        f"In NFHS-5 — the first survey of the merged UT — {n['institutional_N5']:.1f}% of births took place in health facilities, but child nutrition was poor: {n['stunted'][1]:.1f}% of children under five were stunted, {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight, all well above the national averages. The NAMO Hospital and the Vinoba Bhave Civil Hospital in Silvassa and the government hospitals in Daman and Diu are the main centres.",
        f"एनएफ़एचएस-5 में — संयुक्त केंद्र शासित प्रदेश का पहला सर्वेक्षण — {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, पर बाल पोषण ख़राब था: पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने, {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के थे, सभी राष्ट्रीय औसत से काफ़ी ऊपर। सिलवासा का नमो अस्पताल और विनोबा भावे सिविल अस्पताल और दमन व दीव के सरकारी अस्पताल मुख्य केंद्र हैं।",
        f"एनएफएचएस-5 मध्ये — संयुक्त केंद्रशासित प्रदेशाचे पहिले सर्वेक्षण — {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, पण बालपोषण वाईट होते: पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी, {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची होती, सर्व राष्ट्रीय सरासरीपेक्षा बरीच जास्त. सिलवासा येथील नमो रुग्णालय व विनोबा भावे सिव्हिल रुग्णालय आणि दमण व दीवमधील शासकीय रुग्णालये ही मुख्य केंद्रे आहेत."),
        sources=["nfhs"], conf="Official"),
    nfhs_block("DH"),
    gaps("g", [(L("Infant mortality (SRS) for the merged UT", "संयुक्त केंद्र शासित प्रदेश की शिशु मृत्यु दर (एसआरएस)", "संयुक्त केंद्रशासित प्रदेशाचा अर्भक मृत्युदर (एसआरएस)"), "srs", "Not in the SRS table used here.")]),
])

module(R, "nature", [
    prose("p1", L(
        "About 37% of the UT is forest (ISFR 2023), almost all of it in Dadra and Nagar Haveli, where moist and dry deciduous forests with teak cover the hills. The Dadra and Nagar Haveli Wildlife Sanctuary and the Vasona lion safari are here. Daman and Diu have coastal ecosystems and mangroves. There is no Ramsar site in the UT on the list as on 21 April 2026.",
        "केंद्र शासित प्रदेश का लगभग 37% भाग वन है (आईएसएफ़आर 2023), जो लगभग पूरा दादरा और नगर हवेली में है, जहाँ सागौन वाले नम और शुष्क पर्णपाती वन पहाड़ियों को ढकते हैं। दादरा और नगर हवेली वन्यजीव अभयारण्य और वासोणा लायन सफ़ारी यहीं हैं। दमन और दीव में तटीय पारितंत्र और मैंग्रोव हैं। 21 अप्रैल 2026 की सूची में केंद्र शासित प्रदेश में कोई रामसर स्थल नहीं है।",
        "केंद्रशासित प्रदेशाचा सुमारे 37% भाग वनाच्छादित आहे (आयएसएफआर 2023), जवळपास सर्व दादरा आणि नगर हवेलीत, जिथे सागवानाची आर्द्र व शुष्क पानगळी जंगले टेकड्या व्यापतात. दादरा आणि नगर हवेली वन्यजीव अभयारण्य व वासोणा लायन सफारी येथे आहेत. दमण व दीवमध्ये किनारी परिसंस्था व खारफुटी आहेत. 21 एप्रिल 2026 च्या यादीत केंद्रशासित प्रदेशात कोणतेही रामसर स्थळ नाही."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    forest_facts("DH", m["forestCoverPct"], 0, "MoEFCC list of Ramsar sites as on 21 April 2026: none in the UT."),
])

module(R, "water", [
    prose("p1", L(
        "The Madhuban dam on the Damanganga, built jointly with Gujarat, supplies water for drinking, industry and irrigation in Dadra and Nagar Haveli and Daman. Diu depends on groundwater, rainwater and supply from Gujarat.",
        "गुजरात के साथ मिलकर दमनगंगा पर बना मधुबन बाँध दादरा और नगर हवेली और दमन में पीने, उद्योग और सिंचाई के लिए पानी देता है। दीव भूजल, वर्षा जल और गुजरात से आपूर्ति पर निर्भर है।",
        "गुजरातसोबत दमणगंगेवर बांधलेले मधुबन धरण दादरा आणि नगर हवेली व दमणमध्ये पिण्यासाठी, उद्योग व सिंचनासाठी पाणी पुरवते. दीव भूजल, पावसाचे पाणी व गुजरातमधील पुरवठ्यावर अवलंबून आहे."),
        conf="Editorial"),
])

module(R, "safety", [
    prose("p1", L(
        "Daman and Diu face cyclones from the Arabian Sea — Cyclone Tauktae struck Diu in May 2021 — and Dadra and Nagar Haveli sees monsoon floods along the Damanganga. Industrial safety is a concern in Silvassa's factory areas.",
        "दमन और दीव अरब सागर के चक्रवातों का सामना करते हैं — मई 2021 में चक्रवात तौकते दीव से टकराया — और दादरा और नगर हवेली में दमनगंगा के किनारे मानसूनी बाढ़ आती है। सिलवासा के कारख़ाना क्षेत्रों में औद्योगिक सुरक्षा चिंता का विषय है।",
        "दमण व दीवला अरबी समुद्रातील चक्रीवादळांचा सामना करावा लागतो — मे 2021 मध्ये तौक्ते चक्रीवादळ दीवला धडकले — आणि दादरा आणि नगर हवेलीत दमणगंगेकाठी मान्सूनी पूर येतात. सिलवासाच्या कारखाना भागांत औद्योगिक सुरक्षा हा चिंतेचा विषय आहे."),
        conf="Editorial"),
    emergency_table(("Dadra and Nagar Haveli and Daman and Diu", "दादरा और नगर हवेली और दमन और दीव", "दादरा आणि नगर हवेली आणि दमण आणि दीव")),
])

module(R, "gi", [
    prose("p1", L(
        "The GI Registry's list as on 31 December 2025 has no GI of the UT's own, but Warli painting (filed in 2011) is registered for Maharashtra, Gujarat, Dadra and Nagar Haveli and Daman and Diu together.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में केंद्र शासित प्रदेश का अपना कोई जीआई नहीं है, पर वारली चित्रकला (2011 में दायर) महाराष्ट्र, गुजरात, दादरा और नगर हवेली और दमन और दीव के लिए संयुक्त रूप से पंजीकृत है।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत केंद्रशासित प्रदेशाचा स्वतःचा जीआय नाही, पण वारली चित्रकला (2011 मध्ये दाखल) महाराष्ट्र, गुजरात, दादरा आणि नगर हवेली आणि दमण आणि दीव यांच्यासाठी संयुक्तपणे नोंदणीकृत आहे."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
])

module(R, "tourism", [
    prose("p1", L(
        "Diu's fort, St Paul's Church, Naida caves, Nagoa and Ghoghla beaches and the INS Khukri memorial draw most visitors. Daman has Moti Daman fort, Devka and Jampore beaches and a seafront promenade. In Dadra and Nagar Haveli, the Vanganga garden, the tribal museum in Silvassa, the Dudhni reservoir and the Vasona lion safari are popular.",
        "दीव का क़िला, सेंट पॉल चर्च, नायडा गुफाएँ, नागोआ और घोघला तट और आईएनएस खुकरी स्मारक अधिकांश पर्यटकों को खींचते हैं। दमन में मोटी दमन क़िला, देवका और जम्पोर तट और समुद्र तटीय सैरगाह हैं। दादरा और नगर हवेली में वनगंगा उद्यान, सिलवासा का जनजातीय संग्रहालय, दूधनी जलाशय और वासोणा लायन सफ़ारी लोकप्रिय हैं।",
        "दीवचा किल्ला, सेंट पॉल चर्च, नायडा गुहा, नागोआ व घोघला किनारे आणि आयएनएस खुकरी स्मारक बहुतेक पर्यटकांना आकर्षित करतात. दमणमध्ये मोटी दमण किल्ला, देवका व जम्पोर किनारे आणि सागरी पदपथ आहे. दादरा आणि नगर हवेलीत वनगंगा उद्यान, सिलवासाचे आदिवासी संग्रहालय, दूधनी जलाशय व वासोणा लायन सफारी लोकप्रिय आहेत."),
        conf="Editorial"),
])

module(R, "cities", [
    lst("cities", [
        item("daman", L("Daman", "दमन", "दमण"), detail=L("Capital on the Gujarat coast.", "गुजरात तट पर राजधानी।", "गुजरात किनाऱ्यावरील राजधानी."), meta=L("Capital", "राजधानी", "राजधानी")),
        item("silvassa", L("Silvassa", "सिलवासा", "सिलवासा"), detail=L("Largest town; industrial centre.", "सबसे बड़ा नगर; औद्योगिक केंद्र।", "सर्वांत मोठे शहर; औद्योगिक केंद्र."), meta=L("Industry", "उद्योग", "उद्योग")),
        item("diu", L("Diu", "दीव", "दीव"), detail=L("Island town with fort and beaches.", "क़िले और तटों वाला द्वीप नगर।", "किल्ला व किनारे असलेले बेटावरील शहर."), meta=L("Tourism", "पर्यटन", "पर्यटन")),
    ], title=L("Main towns", "मुख्य नगर", "मुख्य शहरे"), conf="Editorial"),
])

module(R, "sports", [
    prose("p1", L(
        "Football, cricket and beach sports are popular, and Diu has hosted beach games events. Tribal archery is a traditional skill in Dadra and Nagar Haveli.",
        "फ़ुटबॉल, क्रिकेट और तटीय खेल लोकप्रिय हैं, और दीव ने बीच गेम्स आयोजनों की मेज़बानी की है। दादरा और नगर हवेली में जनजातीय तीरंदाज़ी पारंपरिक कौशल है।",
        "फुटबॉल, क्रिकेट व किनारी खेळ लोकप्रिय आहेत, आणि दीवने बीच गेम्स स्पर्धांचे आयोजन केले आहे. दादरा आणि नगर हवेलीत आदिवासी धनुर्विद्या हे पारंपरिक कौशल्य आहे."),
        conf="Editorial"),
])

module(R, "personalities", [
    lst("people", [
        person("delkar", ("Mohan Delkar", "मोहन डेलकर", "मोहन डेलकर"), ("Tribal leader and seven-time MP for Dadra and Nagar Haveli.", "जनजातीय नेता और दादरा और नगर हवेली से सात बार सांसद।", "आदिवासी नेते व दादरा आणि नगर हवेलीचे सात वेळा खासदार."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

module(R, "diaspora", [
    prose("p1", L(
        "Many families from Diu and Daman, often holding Portuguese citizenship through birth before 1961 or descent, have settled in Portugal and the United Kingdom, and keep close ties with their home towns.",
        "दीव और दमन के बहुत से परिवार, जिनके पास अक्सर 1961 से पहले जन्म या वंश के आधार पर पुर्तगाली नागरिकता है, पुर्तगाल और ब्रिटेन में बसे हैं और अपने गृह नगरों से निकट संबंध रखते हैं।",
        "दीव व दमणमधील अनेक कुटुंबे, ज्यांच्याकडे अनेकदा 1961 पूर्वीच्या जन्मामुळे किंवा वंशामुळे पोर्तुगीज नागरिकत्व आहे, पोर्तुगाल व ब्रिटनमध्ये स्थायिक झाली आहेत आणि आपल्या मूळ गावांशी घट्ट नाते ठेवतात."),
        conf="Editorial"),
])

module(R, "civic", [links([
    it3("portal", "UT Administration of DNH and DD", "दादरा और नगर हवेली और दमन और दीव प्रशासन", "दादरा आणि नगर हवेली आणि दमण आणि दीव प्रशासन", url="https://ddd.gov.in", src="india-gov"), RTI])])

module(R, "trivia", [
    lst("facts", [
        triv("merge", ("The UT was created on 26 January 2020 by merging two UTs.", "यह केंद्र शासित प्रदेश 26 जनवरी 2020 को दो केंद्र शासित प्रदेशों के विलय से बना।", "हा केंद्रशासित प्रदेश 26 जानेवारी 2020 रोजी दोन केंद्रशासित प्रदेशांच्या विलीनीकरणाने तयार झाला.")),
        triv("warli", ("Warli painting is a GI shared with Maharashtra and Gujarat.", "वारली चित्रकला महाराष्ट्र और गुजरात के साथ साझा जीआई है।", "वारली चित्रकला महाराष्ट्र व गुजरातसोबत सामायिक जीआय आहे."), GI_PDF, "gi-registry"),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("dh ok", POP, SR)
