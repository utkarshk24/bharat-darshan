"""Punjab modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-PB"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
CM = "https://www.deccanherald.com/amp/story/india%2Fpunjab-cm-bhagwant-mann-assumes-office-1091892.html"
NOTE_PB = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 16 Oct 2026. "
           "FY2024-25 is the latest year published for Punjab and may be revised.")
mo = research("mospi_pb.json")
NAME = L("Punjab", "पंजाब", "पंजाब")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Punjabi culture combines Sikh traditions with a rich shared heritage of Sufi poetry, folk song and dance. The Guru Granth Sahib gathers the hymns of the Sikh Gurus alongside those of saints such as Kabir, Ravidas and Sheikh Farid, and gurbani kirtan is sung in gurdwaras every day. The Sufi poets Bulleh Shah and Waris Shah, whose Heer is the best-loved Punjabi romance, belong to the undivided Punjab. Modern Punjabi literature includes Amrita Pritam, Shiv Kumar Batalvi and Gurdial Singh, and Punjabi pop and film music have a worldwide audience.\n\nBhangra, danced by men at harvest, and giddha, performed by women, are the signature dances. Phulkari embroidery — a registered GI shared with Haryana and Rajasthan — juttis, parandis and the woodwork of Hoshiarpur are traditional crafts.",
        "पंजाबी संस्कृति सिख परंपराओं को सूफ़ी कविता, लोकगीत और नृत्य की समृद्ध साझा विरासत से जोड़ती है। गुरु ग्रंथ साहिब में सिख गुरुओं की वाणी के साथ कबीर, रविदास और शेख़ फ़रीद जैसे संतों की वाणी है, और गुरुद्वारों में प्रतिदिन गुरबाणी कीर्तन होता है। सूफ़ी कवि बुल्ले शाह और वारिस शाह, जिनकी 'हीर' सबसे प्रिय पंजाबी प्रेमकथा है, अविभाजित पंजाब के हैं। आधुनिक पंजाबी साहित्य में अमृता प्रीतम, शिव कुमार बटालवी और गुरदयाल सिंह शामिल हैं, और पंजाबी पॉप व फ़िल्म संगीत के श्रोता विश्व भर में हैं।\n\nफ़सल पर पुरुषों द्वारा किया जाने वाला भांगड़ा और महिलाओं का गिद्धा पहचान वाले नृत्य हैं। फुलकारी कढ़ाई — हरियाणा और राजस्थान के साथ साझा पंजीकृत जीआई — जूतियाँ, परांदे और होशियारपुर की लकड़ी का काम पारंपरिक शिल्प हैं।",
        "पंजाबी संस्कृती शीख परंपरांना सूफी काव्य, लोकगीत व नृत्याच्या समृद्ध सामायिक वारशाशी जोडते. गुरु ग्रंथ साहिबमध्ये शीख गुरूंच्या वाणीसोबत कबीर, रविदास व शेख फरीद यांसारख्या संतांची वाणी आहे, आणि गुरुद्वाऱ्यांत दररोज गुरबाणी कीर्तन होते. सूफी कवी बुल्ले शाह व वारिस शाह, ज्यांची 'हीर' ही सर्वांत लाडकी पंजाबी प्रेमकथा आहे, अविभाजित पंजाबचे आहेत. आधुनिक पंजाबी साहित्यात अमृता प्रीतम, शिवकुमार बटालवी व गुरदयाल सिंह यांचा समावेश आहे, आणि पंजाबी पॉप व चित्रपट संगीताचा श्रोतावर्ग जगभर आहे.\n\nसुगीला पुरुषांचे भांगडा व स्त्रियांचे गिद्धा ही ओळख असलेली नृत्ये आहेत. फुलकारी भरतकाम — हरियाणा व राजस्थानसोबत सामायिक नोंदणीकृत जीआय — जुत्ती, परांदे व होशियारपूरचे लाकडी काम या पारंपरिक हस्तकला आहेत."),
        conf="Editorial"),
    lst("festivals", [
        fest("baisakhi", "Baisakhi (Vaisakhi)", "बैसाखी (वैसाखी)", "बैसाखी (वैसाखी)", ("13–14 April", "13–14 अप्रैल", "13–14 एप्रिल"),
             ("Harvest festival and the founding day of the Khalsa; fairs, bhangra and processions.", "फ़सल उत्सव और खालसा का स्थापना दिवस; मेले, भांगड़ा और जुलूस।", "सुगीचा सण व खालशाचा स्थापना दिन; जत्रा, भांगडा व मिरवणुका.")),
        fest("lohri", "Lohri", "लोहड़ी", "लोहडी", ("13 January", "13 जनवरी", "13 जानेवारी"),
             ("Bonfire festival marking the end of winter; rewri, peanuts and folk songs.", "सर्दियों के अंत का अलाव उत्सव; रेवड़ी, मूँगफली और लोकगीत।", "हिवाळ्याच्या शेवटाचा शेकोटी सण; रेवडी, शेंगदाणे व लोकगीते.")),
        fest("gurpurab", "Gurpurab", "गुरपुरब", "गुरपुरब", ("October–November and other dates", "अक्टूबर–नवंबर और अन्य तिथियाँ", "ऑक्टोबर–नोव्हेंबर व इतर तारखा"),
             ("Birth anniversaries of the Gurus, especially Guru Nanak; nagar kirtan processions.", "गुरुओं, विशेषकर गुरु नानक, की जयंती; नगर कीर्तन शोभायात्राएँ।", "गुरूंच्या, विशेषतः गुरु नानकांच्या जयंत्या; नगर कीर्तन मिरवणुका.")),
        fest("hola", "Hola Mohalla", "होला मोहल्ला", "होला मोहल्ला", ("March (day after Holi)", "मार्च (होली के अगले दिन)", "मार्च (होळीच्या दुसऱ्या दिवशी)"),
             ("Martial displays by Nihang Sikhs at Anandpur Sahib.", "आनंदपुर साहिब में निहंग सिखों के युद्ध-कौशल प्रदर्शन।", "आनंदपूर साहिब येथे निहंग शिखांचे युद्धकौशल्य प्रदर्शन.")),
        fest("teeyan", "Teeyan", "तीयाँ", "तीयां", ("July–August (Sawan)", "जुलाई–अगस्त (सावन)", "जुलै–ऑगस्ट (श्रावण)"),
             ("Monsoon festival of women, with swings and giddha.", "महिलाओं का मानसून उत्सव, झूलों और गिद्धे के साथ।", "स्त्रियांचा पावसाळी सण, झोके व गिद्ध्यासह.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("bhangra", "Bhangra", "भांगड़ा", "भांगडा"), it3("giddha", "Giddha", "गिद्धा", "गिद्धा"),
        it3("kirtan", "Gurbani kirtan", "गुरबाणी कीर्तन", "गुरबाणी कीर्तन"), it3("phulkari", "Phulkari", "फुलकारी", "फुलकारी"),
        it3("jutti", "Punjabi jutti", "पंजाबी जूती", "पंजाबी जुत्ती"), it3("gatka", "Gatka (martial art)", "गतका (युद्धकला)", "गतका (युद्धकला)"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("saag", "Sarson da saag and makki di roti", "सरसों का साग और मक्की की रोटी", "सरसों दा साग व मक्की दी रोटी", d=("Mustard greens with maize bread and white butter — a winter classic.", "सफ़ेद मक्खन के साथ सरसों का साग और मक्की की रोटी — सर्दियों का ख़ास भोजन।", "पांढऱ्या लोण्यासह मोहरीची भाजी व मक्याची भाकरी — हिवाळ्याचा खास बेत.")),
        it3("kulcha", "Amritsari kulcha", "अमृतसरी कुलचा", "अमृतसरी कुलचा", d=("Stuffed, tandoor-baked bread with chole.", "छोले के साथ तंदूर में सेंका भरवाँ कुलचा।", "छोल्यांसह तंदूरमध्ये भाजलेला भरलेला कुलचा.")),
        it3("lassi", "Lassi", "लस्सी", "लस्सी", d=("Thick, churned yoghurt drink, sweet or salted.", "गाढ़ी मथी दही का पेय, मीठी या नमकीन।", "घट्ट घुसळलेल्या दह्याचे पेय, गोड किंवा खारट.")),
        it3("langar", "Langar", "लंगर", "लंगर", d=("Free community meal of dal, roti and kheer at every gurdwara.", "हर गुरुद्वारे में दाल, रोटी और खीर का मुफ़्त सामुदायिक भोजन।", "प्रत्येक गुरुद्वाऱ्यात डाळ, रोटी व खिरीचे मोफत सामूहिक भोजन.")),
        it3("pinni", "Pinni", "पिन्नी", "पिन्नी", d=("Winter sweet of wheat flour, ghee and dry fruit.", "गेहूँ के आटे, घी और मेवों की सर्दियों की मिठाई।", "गव्हाचे पीठ, तूप व सुकामेव्याची हिवाळी मिठाई.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("salwar", "Salwar kameez with phulkari dupatta", "फुलकारी दुपट्टे के साथ सलवार क़मीज़", "फुलकारी ओढणीसह सलवार कमीज", d=("Women's dress; parandi tassels in braided hair.", "महिलाओं की पोशाक; चोटी में परांदा।", "स्त्रियांचा पोशाख; वेणीत परांदा.")),
        it3("kurta", "Kurta, tehmat and pagg", "कुर्ता, तहमत और पग", "कुर्ता, तहमत व पग", d=("Men's traditional dress; the turban (pagg) is central to Sikh identity.", "पुरुषों की पारंपरिक पोशाक; पगड़ी (पग) सिख पहचान का केंद्र है।", "पुरुषांचा पारंपरिक पोशाख; पगडी (पग) शीख ओळखीचे केंद्र आहे.")),
        it3("jutti", "Jutti", "जूती", "जुत्ती", d=("Embroidered leather shoes from Patiala and Amritsar.", "पटियाला और अमृतसर की कढ़ाईदार चमड़े की जूतियाँ।", "पटियाळा व अमृतसरच्या भरतकाम केलेल्या चामड्याच्या जुत्त्या.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["PB"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["PB"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Punjab's GSDP at current prices was about ₹{cur['FY2024-25'][0]/1e5:.2f} lakh crore in FY2024-25, the latest year published for the State in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2024-25'][0])}. Agriculture, livestock and fishing made up about {agri:.0f}% of GSVA in FY2024-25 — a large share for a relatively prosperous State — and manufacturing about {mfg:.0f}%. Since the Green Revolution, Punjab's wheat–rice rotation has supplied a large part of India's central food stocks, supported by canals, tubewells, minimum support prices and assured procurement; dairying is also strong. Industry is built on small and medium firms: hosiery, bicycles and auto parts in Ludhiana, sports goods and hand tools in Jalandhar, steel re-rolling at Mandi Gobindgarh, and IT and pharmaceuticals around Mohali, with a refinery at Bathinda.\n\nThe PLFS unemployment rate fell from {ur['2022']}% in 2022 to {ur['2025']}% in 2025 but remained above the national {ui['2025']}%, and only {lf['female']}% of women aged 15 and above were in the labour force, against {lfi['female']}% nationally.",
        f"मोस्पी शृंखला में राज्य के लिए प्रकाशित नवीनतम वर्ष, वित्त वर्ष 2024-25 में पंजाब का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2024-25'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2024-25'][0])}। वित्त वर्ष 2024-25 में कृषि, पशुपालन और मत्स्य पालन जीएसवीए का लगभग {agri:.0f}% थे — अपेक्षाकृत समृद्ध राज्य के लिए बड़ा हिस्सा — और विनिर्माण लगभग {mfg:.0f}%। हरित क्रांति के बाद से पंजाब के गेहूँ–धान चक्र ने भारत के केंद्रीय खाद्य भंडार का बड़ा हिस्सा दिया है, जिसे नहरों, ट्यूबवेलों, न्यूनतम समर्थन मूल्य और सुनिश्चित ख़रीद का सहारा है; डेयरी भी मज़बूत है। उद्योग छोटी और मध्यम इकाइयों पर आधारित है: लुधियाना में होज़री, साइकिलें और ऑटो पुर्ज़े, जालंधर में खेल का सामान और हस्त औज़ार, मंडी गोबिंदगढ़ में इस्पात री-रोलिंग, और मोहाली के आसपास आईटी और दवाएँ, तथा बठिंडा में रिफ़ाइनरी।\n\nपीएलएफ़एस बेरोज़गारी दर 2022 के {ur['2022']}% से घटकर 2025 में {ur['2025']}% हुई लेकिन राष्ट्रीय {ui['2025']}% से ऊपर रही, और 15 वर्ष से अधिक आयु की केवल {lf['female']}% महिलाएँ श्रम बल में थीं, जबकि राष्ट्रीय स्तर पर {lfi['female']}%।",
        f"मोस्पी मालिकेत राज्यासाठी प्रकाशित नवीनतम वर्ष, आ.व. 2024-25 मध्ये पंजाबचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2024-25'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2024-25'][0])}. आ.व. 2024-25 मध्ये शेती, पशुपालन व मत्स्यव्यवसायाचा जीएसव्हीएमध्ये सुमारे {agri:.0f}% वाटा होता — तुलनेने समृद्ध राज्यासाठी मोठा वाटा — आणि उत्पादन उद्योगाचा सुमारे {mfg:.0f}%. हरितक्रांतीपासून पंजाबच्या गहू–भात चक्राने भारताच्या केंद्रीय अन्नसाठ्याचा मोठा भाग पुरवला आहे, ज्याला कालवे, कूपनलिका, किमान आधारभूत किंमत व खात्रीशीर खरेदीचा आधार आहे; दुग्धव्यवसायही मजबूत आहे. उद्योग लहान व मध्यम कंपन्यांवर उभे आहेत: लुधियान्यात होजियरी, सायकली व वाहनांचे सुटे भाग, जालंधरमध्ये क्रीडा साहित्य व हत्यारे, मंडी गोविंदगड येथे पोलाद री-रोलिंग, आणि मोहालीभोवती आयटी व औषधनिर्मिती, तसेच भटिंडा येथे रिफायनरी.\n\nपीएलएफएस बेरोजगारी दर 2022 मधील {ur['2022']}% वरून 2025 मध्ये {ur['2025']}% वर आला, पण तो राष्ट्रीय {ui['2025']}% पेक्षा अधिक राहिला, आणि 15 वर्षांवरील केवळ {lf['female']}% स्त्रिया श्रमशक्तीत होत्या, तर राष्ट्रीय पातळीवर {lfi['female']}%."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_PB), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_PB), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_PB), "rupee", "higher-is-better",
             previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("PB", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    plfs_series("PB", NAME),
    lst("sectors-key", [
        it3("wheat", "Wheat and rice", "गेहूँ और धान", "गहू व भात", d=("Wheat in rabi, paddy in kharif; procured for the central pool.", "रबी में गेहूँ, ख़रीफ़ में धान; केंद्रीय भंडार के लिए ख़रीद।", "रब्बीत गहू, खरिपात भात; केंद्रीय साठ्यासाठी खरेदी.")),
        it3("dairy", "Dairy", "डेयरी", "दुग्धव्यवसाय", d=("Verka co-operative milk brand.", "वेरका सहकारी दुग्ध ब्रांड।", "वेरका सहकारी दूध ब्रँड.")),
        it3("hosiery", "Hosiery and textiles", "होज़री और वस्त्र", "होजियरी व वस्त्रोद्योग", d=("Woollen and cotton knitwear in Ludhiana.", "लुधियाना में ऊनी और सूती बुनाई।", "लुधियान्यात लोकरी व सुती विणलेले कपडे.")),
        it3("cycles", "Bicycles and auto parts", "साइकिलें और ऑटो पुर्ज़े", "सायकली व वाहनांचे सुटे भाग", d=("Ludhiana's engineering cluster.", "लुधियाना का इंजीनियरिंग क्लस्टर।", "लुधियान्याचा अभियांत्रिकी समूह.")),
        it3("sports", "Sports goods and hand tools", "खेल का सामान और हस्त औज़ार", "क्रीडा साहित्य व हत्यारे", d=("Jalandhar's export industries.", "जालंधर के निर्यात उद्योग।", "जालंधरचे निर्यात उद्योग.")),
        it3("it", "IT and pharma", "आईटी और दवाएँ", "आयटी व औषधनिर्मिती", d=("Mohali and the Chandigarh tricity.", "मोहाली और चंडीगढ़ ट्राइसिटी।", "मोहाली व चंदीगड त्रिनगरी.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Wheat and paddy procurement by season", "मौसमवार गेहूँ और धान ख़रीद", "हंगामनिहाय गहू व धानखरेदी"), "india-gov", "Food Corporation of India / Punjab Food Department."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("GSDP for FY2025-26", "वित्त वर्ष 2025-26 का जीएसडीपी", "आ.व. 2025-26 चे जीएसडीपी"), "mospi", "Not yet published for Punjab in the MoSPI series at access time."),
        (L("Remittance inflows", "प्रेषण प्रवाह", "परदेशातून येणारा पैसा"), "rbi-handbook", "RBI remittance survey, state shares."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Punjab has a unicameral legislature, the 117-member Vidhan Sabha in Chandigarh. The State elects 13 members to the Lok Sabha and 7 to the Rajya Sabha.\n\nThe Aam Aadmi Party won the Assembly election of 2022, and Bhagwant Mann was sworn in as Chief Minister on 16 March 2022 at Khatkar Kalan, the ancestral village of Bhagat Singh. Kultar Singh Sandhwan (AAP) is Speaker. Gulab Chand Kataria has been Governor since July 2024 and is also Administrator of Chandigarh. The next Assembly election is due by early 2027.",
        "पंजाब में एकसदनीय विधानमंडल है, चंडीगढ़ में 117 सदस्यों वाली विधानसभा। राज्य से लोकसभा के 13 और राज्यसभा के 7 सदस्य चुने जाते हैं।\n\n2022 का विधानसभा चुनाव आम आदमी पार्टी ने जीता, और भगवंत मान ने 16 मार्च 2022 को भगत सिंह के पैतृक गाँव खटकड़ कलाँ में मुख्यमंत्री पद की शपथ ली। कुलतार सिंह संधवां (आप) अध्यक्ष हैं। गुलाब चंद कटारिया जुलाई 2024 से राज्यपाल हैं और चंडीगढ़ के प्रशासक भी। अगला विधानसभा चुनाव 2027 की शुरुआत तक होना है।",
        "पंजाबमध्ये एकसदनी विधिमंडळ आहे, चंदीगडमधील 117 सदस्यांची विधानसभा. राज्यातून लोकसभेवर 13 व राज्यसभेवर 7 सदस्य निवडले जातात.\n\n2022 ची विधानसभा निवडणूक आम आदमी पक्षाने जिंकली, आणि भगवंत मान यांनी 16 मार्च 2022 रोजी भगतसिंहांच्या मूळ गावी खटकड कलां येथे मुख्यमंत्रिपदाची शपथ घेतली. कुलतार सिंह संधवां (आप) अध्यक्ष आहेत. गुलाबचंद कटारिया जुलै 2024 पासून राज्यपाल आहेत व चंदीगडचे प्रशासकही. पुढील विधानसभा निवडणूक 2027 च्या सुरुवातीपर्यंत होणे अपेक्षित आहे."),
        sources=["deccan-herald", "newsonair", "etv-bharat"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("rajbhavan", "Punjab Raj Bhavan", "पंजाब राजभवन", "पंजाब राजभवन", url="https://punjabrajbhavan.gov.in", src="india-gov"),
        it3("portal", "Government of Punjab", "पंजाब सरकार", "पंजाब शासन", url="https://punjab.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2022 Assembly election — party-wise result", "2022 विधानसभा चुनाव — दलवार परिणाम", "2022 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Punjab 2022."),
        (L("Chief Minister's swearing-in — official source", "मुख्यमंत्री का शपथ ग्रहण — आधिकारिक स्रोत", "मुख्यमंत्र्यांचा शपथविधी — अधिकृत स्रोत"), "india-gov", "Replace the PTI copy with a Raj Bhavan or State release."),
        (L("Leader of Opposition — official notice", "नेता प्रतिपक्ष — आधिकारिक सूचना", "विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "Vidhan Sabha secretariat."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "AIIMS Bathinda was dedicated to the nation in February 2024, and a power-semiconductor expansion at Mohali was approved under the India Semiconductor Mission in August 2025. Other large works include the Punjab stretch of the Delhi–Amritsar–Katra expressway, new airport terminals and canal lining. Each card shows its source and the date it was checked.",
        "एम्स बठिंडा फ़रवरी 2024 में राष्ट्र को समर्पित हुआ, और अगस्त 2025 में भारत सेमीकंडक्टर मिशन के तहत मोहाली में पावर सेमीकंडक्टर विस्तार को मंज़ूरी मिली। अन्य बड़े कार्यों में दिल्ली–अमृतसर–कटरा एक्सप्रेसवे का पंजाब खंड, नए हवाई अड्डा टर्मिनल और नहरों की लाइनिंग शामिल है। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "एम्स भटिंडा फेब्रुवारी 2024 मध्ये राष्ट्राला समर्पित झाले, आणि ऑगस्ट 2025 मध्ये भारत सेमीकंडक्टर मिशनअंतर्गत मोहाली येथील पॉवर सेमीकंडक्टर विस्ताराला मंजुरी मिळाली. इतर मोठ्या कामांत दिल्ली–अमृतसर–कटरा द्रुतगती मार्गाचा पंजाब टप्पा, नवी विमानतळ टर्मिनल व कालव्यांचे अस्तरीकरण यांचा समावेश आहे. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pmindia"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Delhi–Amritsar–Katra expressway (Punjab section) — status", "दिल्ली–अमृतसर–कटरा एक्सप्रेसवे (पंजाब खंड) — स्थिति", "दिल्ली–अमृतसर–कटरा द्रुतगती मार्ग (पंजाब टप्पा) — स्थिती"), "nhai", "NHAI project status; land acquisition has been reported as a constraint."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Sri Guru Ram Dass Jee International Airport at Amritsar and the Shaheed Bhagat Singh International Airport at Mohali (serving Chandigarh) are the main airports, with smaller airports at Bathinda, Adampur (Jalandhar) and Ludhiana. The Grand Trunk Road (National Highway 44) runs through Ludhiana, Jalandhar and Amritsar to the Attari border, and the Northern Railway's Ambala and Ferozepur divisions serve the State. The Eastern Dedicated Freight Corridor begins at Sahnewal near Ludhiana.",
        "अमृतसर का श्री गुरु रामदास जी अंतरराष्ट्रीय हवाई अड्डा और मोहाली का शहीद भगत सिंह अंतरराष्ट्रीय हवाई अड्डा (चंडीगढ़ को सेवा देने वाला) मुख्य हवाई अड्डे हैं, और बठिंडा, आदमपुर (जालंधर) और लुधियाना में छोटे हवाई अड्डे हैं। ग्रैंड ट्रंक रोड (राष्ट्रीय राजमार्ग 44) लुधियाना, जालंधर और अमृतसर से होकर अटारी सीमा तक जाती है, और उत्तर रेलवे के अंबाला और फ़िरोज़पुर मंडल राज्य को सेवा देते हैं। पूर्वी समर्पित माल गलियारा लुधियाना के पास साहनेवाल से शुरू होता है।",
        "अमृतसरचे श्री गुरु रामदास जी आंतरराष्ट्रीय विमानतळ व मोहालीचे शहीद भगतसिंह आंतरराष्ट्रीय विमानतळ (चंदीगडला सेवा देणारे) हे मुख्य विमानतळ आहेत, आणि भटिंडा, आदमपूर (जालंधर) व लुधियाना येथे लहान विमानतळ आहेत. ग्रँड ट्रंक रोड (राष्ट्रीय महामार्ग 44) लुधियाना, जालंधर व अमृतसरमार्गे अटारी सीमेपर्यंत जातो, आणि उत्तर रेल्वेचे अंबाला व फिरोजपूर विभाग राज्याला सेवा देतात. पूर्व समर्पित मालवाहतूक मार्गिका लुधियान्याजवळ साहनेवाल येथून सुरू होते."),
        conf="Editorial"),
    lst("airports", [
        it3("atq", "Sri Guru Ram Dass Jee International Airport, Amritsar", "श्री गुरु रामदास जी अंतरराष्ट्रीय हवाई अड्डा, अमृतसर", "श्री गुरु रामदास जी आंतरराष्ट्रीय विमानतळ, अमृतसर", m=("ATQ", "ATQ", "ATQ")),
        it3("ixc", "Shaheed Bhagat Singh International Airport, Mohali", "शहीद भगत सिंह अंतरराष्ट्रीय हवाई अड्डा, मोहाली", "शहीद भगतसिंह आंतरराष्ट्रीय विमानतळ, मोहाली", m=("IXC", "IXC", "IXC")),
        it3("bup", "Bathinda", "बठिंडा", "भटिंडा", m=("BUP", "BUP", "BUP")),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Punjab draws power from its own coal stations — Ropar, Lehra Mohabbat and the Goindwal Sahib plant — and from private plants at Rajpura and Talwandi Sabo, which burn coal brought from eastern India. It also receives a share of hydro-electric power from the Bhakra–Beas system managed by the Bhakra Beas Management Board, and from its own Ranjit Sagar dam on the Ravi. Demand peaks during the paddy season, when millions of farm tubewells run, and the State supplies free power for agriculture. Rooftop and canal-top solar capacity is growing.",
        "पंजाब अपने कोयला संयंत्रों — रोपड़, लहरा मोहब्बत और गोइंदवाल साहिब संयंत्र — और राजपुरा व तलवंडी साबो के निजी संयंत्रों से बिजली लेता है, जो पूर्वी भारत से लाया गया कोयला जलाते हैं। इसे भाखड़ा ब्यास प्रबंध बोर्ड द्वारा संचालित भाखड़ा–ब्यास प्रणाली और रावी पर अपने रणजीत सागर बाँध से भी जलविद्युत का हिस्सा मिलता है। धान के मौसम में, जब लाखों कृषि ट्यूबवेल चलते हैं, माँग चरम पर होती है, और राज्य कृषि के लिए मुफ़्त बिजली देता है। छतों और नहरों पर सौर क्षमता बढ़ रही है।",
        "पंजाब आपल्या कोळसा केंद्रांतून — रोपड, लहरा मोहब्बत व गोइंदवाल साहिब प्रकल्प — आणि राजपुरा व तलवंडी साबो येथील खासगी प्रकल्पांतून वीज घेतो, जे पूर्व भारतातून आणलेला कोळसा वापरतात. त्याला भाक्रा बियास व्यवस्थापन मंडळाद्वारे चालवल्या जाणाऱ्या भाक्रा–बियास प्रणालीतून व रावीवरील स्वतःच्या रणजित सागर धरणातूनही जलविद्युतचा वाटा मिळतो. भाताच्या हंगामात, जेव्हा लाखो शेती कूपनलिका चालतात, मागणी शिखरावर असते, आणि राज्य शेतीसाठी मोफत वीज देते. छतांवरील व कालव्यांवरील सौरक्षमता वाढत आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Agricultural power subsidy", "कृषि बिजली सब्सिडी", "शेती वीज अनुदान"), "india-gov", "Punjab budget documents / PSERC tariff orders."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Mohali, part of the Chandigarh tricity, is Punjab's technology hub, with IT parks, data centres, a growing start-up scene and research institutions such as IISER Mohali, NIPER and the Indian School of Business campus. The State delivers many citizen services online through its Sewa Kendras, and internet use is high across urban and rural Punjab.",
        "चंडीगढ़ ट्राइसिटी का हिस्सा मोहाली पंजाब का प्रौद्योगिकी केंद्र है, जहाँ आईटी पार्क, डेटा सेंटर, बढ़ता स्टार्टअप परिदृश्य और आईआईएसईआर मोहाली, नाइपर और इंडियन स्कूल ऑफ़ बिज़नेस परिसर जैसे शोध संस्थान हैं। राज्य अपने सेवा केंद्रों के माध्यम से कई नागरिक सेवाएँ ऑनलाइन देता है, और शहरी व ग्रामीण पंजाब में इंटरनेट का उपयोग ऊँचा है।",
        "चंदीगड त्रिनगरीचा भाग असलेले मोहाली हे पंजाबचे तंत्रज्ञान केंद्र आहे, जिथे आयटी पार्क, डेटा सेंटर, वाढते स्टार्टअप विश्व आणि आयसर मोहाली, नायपर व इंडियन स्कूल ऑफ बिझनेस संकुल यांसारख्या संशोधन संस्था आहेत. राज्य आपल्या सेवा केंद्रांमार्फत अनेक नागरी सेवा ऑनलाइन देते, आणि शहरी व ग्रामीण पंजाबमध्ये इंटरनेटचा वापर जास्त आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Punjab circle)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("PB", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["PB"]
module(R, "education", [
    prose("p1", L(
        f"Punjab's higher-education gross enrolment ratio (ages 18–23) was 27.4% in 2021-22 in AISHE, close to the national 28.4% but lower than 29.2% in 2017-18; women's GER ({gf}%) was clearly higher than men's ({gm}%), and many young people go abroad to study. The State had 40 universities and 1,044 colleges. Literacy at the 2011 Census was 75.8%.\n\nPunjabi University, Patiala (1962), Guru Nanak Dev University, Amritsar (1969) and Punjab Agricultural University, Ludhiana (1962) — a centre of the Green Revolution — are major State universities, and Panjab University in Chandigarh serves many colleges in the State. National institutions include IIT Ropar, AIIMS Bathinda, IISER Mohali, IIM Amritsar, NIT Jalandhar, the Central University of Punjab at Bathinda, and the National Institute of Sports at Patiala; Thapar Institute in Patiala is a well-known private engineering institute.",
        f"एआईएसएचई के अनुसार 2021-22 में पंजाब का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) 27.4% था, जो राष्ट्रीय 28.4% के क़रीब लेकिन 2017-18 के 29.2% से कम है; महिलाओं का जीईआर ({gf}%) पुरुषों ({gm}%) से स्पष्ट रूप से अधिक था, और बहुत से युवा पढ़ने विदेश जाते हैं। राज्य में 40 विश्वविद्यालय और 1,044 कॉलेज थे। 2011 की जनगणना में साक्षरता 75.8% थी।\n\nपंजाबी विश्वविद्यालय, पटियाला (1962), गुरु नानक देव विश्वविद्यालय, अमृतसर (1969) और हरित क्रांति का केंद्र रहा पंजाब कृषि विश्वविद्यालय, लुधियाना (1962) प्रमुख राज्य विश्वविद्यालय हैं, और चंडीगढ़ का पंजाब विश्वविद्यालय राज्य के कई कॉलेजों को सेवा देता है। राष्ट्रीय संस्थानों में आईआईटी रोपड़, एम्स बठिंडा, आईआईएसईआर मोहाली, आईआईएम अमृतसर, एनआईटी जालंधर, बठिंडा का पंजाब केंद्रीय विश्वविद्यालय और पटियाला का राष्ट्रीय खेल संस्थान शामिल हैं; पटियाला का थापर संस्थान प्रसिद्ध निजी इंजीनियरिंग संस्थान है।",
        f"एआयएसएचईनुसार 2021-22 मध्ये पंजाबचे उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) 27.4% होते, राष्ट्रीय 28.4% च्या जवळ पण 2017-18 मधील 29.2% पेक्षा कमी; स्त्रियांचे जीईआर ({gf}%) पुरुषांपेक्षा ({gm}%) स्पष्टपणे अधिक होते, आणि अनेक तरुण शिक्षणासाठी परदेशी जातात. राज्यात 40 विद्यापीठे व 1,044 महाविद्यालये होती. 2011 च्या जनगणनेत साक्षरता 75.8% होती.\n\nपंजाबी विद्यापीठ, पटियाळा (1962), गुरु नानक देव विद्यापीठ, अमृतसर (1969) व हरितक्रांतीचे केंद्र राहिलेले पंजाब कृषी विद्यापीठ, लुधियाना (1962) ही प्रमुख राज्य विद्यापीठे आहेत, आणि चंदीगडचे पंजाब विद्यापीठ राज्यातील अनेक महाविद्यालयांना सेवा देते. राष्ट्रीय संस्थांत आयआयटी रोपड, एम्स भटिंडा, आयसर मोहाली, आयआयएम अमृतसर, एनआयटी जालंधर, भटिंडाचे पंजाब केंद्रीय विद्यापीठ व पटियाळाची राष्ट्रीय क्रीडा संस्था यांचा समावेश आहे; पटियाळाची थापर संस्था ही प्रसिद्ध खासगी अभियांत्रिकी संस्था आहे."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("pup", "Punjabi University", "पंजाबी विश्वविद्यालय", "पंजाबी विद्यापीठ", m=("Patiala, 1962", "पटियाला, 1962", "पटियाळा, 1962")),
        it3("gndu", "Guru Nanak Dev University", "गुरु नानक देव विश्वविद्यालय", "गुरु नानक देव विद्यापीठ", m=("Amritsar, 1969", "अमृतसर, 1969", "अमृतसर, 1969")),
        it3("pau", "Punjab Agricultural University", "पंजाब कृषि विश्वविद्यालय", "पंजाब कृषी विद्यापीठ", m=("Ludhiana, 1962", "लुधियाना, 1962", "लुधियाना, 1962")),
        it3("iitr", "IIT Ropar", "आईआईटी रोपड़", "आयआयटी रोपड", m=("Rupnagar", "रूपनगर", "रूपनगर")),
        it3("aiimsb", "AIIMS Bathinda", "एम्स बठिंडा", "एम्स भटिंडा", m=("Bathinda", "बठिंडा", "भटिंडा")),
        it3("iiser", "IISER Mohali", "आईआईएसईआर मोहाली", "आयसर मोहाली", m=("Mohali", "मोहाली", "मोहाली")),
        it3("nis", "Netaji Subhas National Institute of Sports", "नेताजी सुभाष राष्ट्रीय खेल संस्थान", "नेताजी सुभाष राष्ट्रीय क्रीडा संस्था", m=("Patiala", "पटियाला", "पटियाळा")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Students going abroad", "विदेश जाने वाले छात्र", "परदेशी जाणारे विद्यार्थी"), "india-gov", "MEA / Bureau of Immigration data, if published by State."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["PB"]
module(R, "health", [
    prose("p1", L(
        f"Punjab's health indicators are better than the national average. The infant mortality rate fell from 34 per 1,000 live births in 2010 to 18 in 2020, well below the national 28, and the birth rate, 14.3 per 1,000, was among the lowest in India; the death rate was 7.2. Life expectancy at birth was 72.7 years in 2014-18 (men 71.0, women 74.8), above the national 69.4. In NFHS-5, {n['stunted'][1]:.1f}% of children under five were stunted, {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight — all lower than in NFHS-4 and well below the national levels — and {n['institutional_N5']:.1f}% of births took place in health facilities.\n\nAIIMS Bathinda, the government medical colleges at Amritsar, Patiala and Faridkot, and the Christian and Dayanand medical colleges in Ludhiana are major hospitals, and PGIMER in Chandigarh serves many patients from the State. Non-communicable diseases and substance use are recognised public-health challenges.",
        f"पंजाब के स्वास्थ्य संकेतक राष्ट्रीय औसत से बेहतर हैं। शिशु मृत्यु दर 2010 में प्रति 1,000 जीवित जन्म पर 34 से घटकर 2020 में 18 हो गई, जो राष्ट्रीय 28 से काफ़ी कम है, और प्रति 1,000 पर 14.3 की जन्म दर भारत में सबसे कम में थी; मृत्यु दर 7.2 थी। 2014-18 में जन्म के समय जीवन प्रत्याशा 72.7 वर्ष थी (पुरुष 71.0, महिलाएँ 74.8), जो राष्ट्रीय 69.4 से अधिक है। एनएफ़एचएस-5 में पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने, {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के थे — सभी एनएफ़एचएस-4 से कम और राष्ट्रीय स्तर से काफ़ी नीचे — और {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए।\n\nएम्स बठिंडा, अमृतसर, पटियाला और फ़रीदकोट के सरकारी मेडिकल कॉलेज, और लुधियाना के क्रिश्चियन व दयानंद मेडिकल कॉलेज प्रमुख अस्पताल हैं, और चंडीगढ़ का पीजीआईएमईआर राज्य के बहुत से रोगियों को सेवा देता है। ग़ैर-संचारी रोग और नशीले पदार्थों का सेवन मान्य सार्वजनिक स्वास्थ्य चुनौतियाँ हैं।",
        f"पंजाबचे आरोग्य निर्देशक राष्ट्रीय सरासरीपेक्षा चांगले आहेत. अर्भक मृत्युदर 2010 मध्ये दर 1,000 जिवंत जन्मांमागे 34 वरून 2020 मध्ये 18 वर आला, राष्ट्रीय 28 पेक्षा बराच कमी, आणि दर 1,000 मागे 14.3 चा जन्मदर भारतातील सर्वांत कमींपैकी होता; मृत्युदर 7.2 होता. 2014-18 मध्ये जन्मतः आयुर्मान 72.7 वर्षे होते (पुरुष 71.0, स्त्रिया 74.8), राष्ट्रीय 69.4 पेक्षा अधिक. एनएफएचएस-5 मध्ये पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी, {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची होती — सर्व एनएफएचएस-4 पेक्षा कमी व राष्ट्रीय पातळीपेक्षा बरीच खाली — आणि {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या.\n\nएम्स भटिंडा, अमृतसर, पटियाळा व फरीदकोटची शासकीय वैद्यकीय महाविद्यालये, आणि लुधियान्याची ख्रिश्चन व दयानंद वैद्यकीय महाविद्यालये ही प्रमुख रुग्णालये आहेत, आणि चंदीगडचे पीजीआयएमईआर राज्यातील अनेक रुग्णांना सेवा देते. असंसर्गजन्य आजार व अमली पदार्थांचे सेवन ही मान्य सार्वजनिक आरोग्य आव्हाने आहेत."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(18, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(34, "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(14.3, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020 (death rate 7.2); 16.6 in 2010."), "number",
             previous=dp(16.6, "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(72.7, "years", "2014-18", "survey", "srs", ESI_LE, note="SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male 71.0, female 74.8)."), "number", "higher-is-better",
             previous=dp(71.6, "years", "2010-14", "survey", "srs", ESI_LE), national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("PB"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin; the PIB summary used here lists only States that met the SDG target."),
        (L("Cancer incidence (population-based registries)", "कैंसर की घटनाएँ (जनसंख्या-आधारित रजिस्ट्री)", "कर्करोग प्रमाण (लोकसंख्याआधारित नोंदवह्या)"), "india-gov", "ICMR–NCDIR National Cancer Registry Programme."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("pb mod2 ok")
