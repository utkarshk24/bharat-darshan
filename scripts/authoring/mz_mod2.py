"""Mizoram modules G–O."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-MZ"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 25 Oct 2026. "
        "FY2024-25 is the latest year published for Mizoram and may be revised.")
mo = research("mospi_mz.json")
C = research("census_b5plus.json")
NAME = L("Mizoram", "मिज़ोरम", "मिझोराम")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Mizo culture centres on the village community, the church and the three traditional kut (festivals) tied to the farming year. Cheraw, the bamboo dance in which dancers step between clapping bamboo poles, is performed at festivals, along with Khuallam and Chheih Lam. Women weave puan, the wrap-around cloth worn on every occasion, in patterns that mark clan and occasion. Choir singing and Christian music are part of everyday life, alongside a lively rock and pop scene.",
        "मिज़ो संस्कृति गाँव के समुदाय, चर्च और खेती के वर्ष से जुड़े तीन पारंपरिक कुट (त्योहारों) पर केंद्रित है। चेराव, बाँस नृत्य जिसमें नर्तक ताली बजाते बाँसों के बीच कदम रखते हैं, ख़ुआललाम और छेइह लाम के साथ त्योहारों पर किया जाता है। महिलाएँ पुआन बुनती हैं, हर अवसर पर पहना जाने वाला लपेटने का वस्त्र, जिनके नमूने कुल और अवसर बताते हैं। गायक मंडलियाँ और ईसाई संगीत दैनिक जीवन का हिस्सा हैं, जीवंत रॉक और पॉप के साथ।",
        "मिझो संस्कृती गावसमुदाय, चर्च आणि शेतीच्या वर्षाशी जोडलेल्या तीन पारंपरिक कुट (सणां) भोवती केंद्रित आहे. चेराव, बांबू नृत्य ज्यात नर्तक टाळ्या वाजवणाऱ्या बांबूंमध्ये पावले टाकतात, ख्वाललाम व छेइह लामसह सणांना सादर होते. स्त्रिया पुआन विणतात, प्रत्येक प्रसंगी परिधान केले जाणारे गुंडाळायचे वस्त्र, ज्यांची नक्षी कुळ व प्रसंग दर्शवते. गायकवृंद व ख्रिस्ती संगीत रोजच्या जीवनाचा भाग आहेत, चैतन्यशील रॉक व पॉपसह."),
        conf="Editorial"),
    lst("festivals", [
        fest("chapchar", "Chapchar Kut", "चापचार कुट", "चापचार कुट", ("March", "मार्च", "मार्च"), ("Spring festival after the jhum fields are cleared.", "झूम खेत साफ़ होने के बाद वसंत उत्सव।", "झूम शेते साफ केल्यानंतरचा वसंतोत्सव.")),
        fest("mimkut", "Mim Kut", "मिम कुट", "मिम कुट", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"), ("Festival in memory of the dead, after the maize harvest.", "मक्के की फ़सल के बाद मृतकों की स्मृति का त्योहार।", "मक्याच्या सुगीनंतर मृतांच्या स्मृतीचा सण.")),
        fest("pawlkut", "Pawl Kut", "पॉल कुट", "पॉल कुट", ("December", "दिसंबर", "डिसेंबर"), ("Harvest thanksgiving festival.", "फ़सल कटाई का धन्यवाद पर्व।", "सुगीचा कृतज्ञता सण.")),
        fest("christmas", "Christmas", "क्रिसमस", "नाताळ", ("December", "दिसंबर", "डिसेंबर"), ("The biggest celebration of the year in most homes.", "अधिकांश घरों में वर्ष का सबसे बड़ा उत्सव।", "बहुतेक घरांत वर्षातील सर्वांत मोठा उत्सव.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("cheraw", "Cheraw bamboo dance", "चेराव बाँस नृत्य", "चेराव बांबू नृत्य"), it3("puan", "Puan weaving", "पुआन बुनाई", "पुआन विणकाम"),
        it3("khuang", "Khuang drum", "ख़ुआंग ढोल", "ख्वांग ढोल"), it3("bamboo", "Bamboo and cane craft", "बाँस और बेंत शिल्प", "बांबू व वेत हस्तकला"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("bai", "Bai", "बाई", "बाई", d=("Stew of greens, bamboo shoot and often pork.", "साग, बाँस की कोंपल और अक्सर सूअर के मांस का शोरबा।", "पालेभाज्या, बांबूचे कोंब व अनेकदा डुकराचे मांस घालून रस्सा.")),
        it3("sawhchiar", "Sawhchiar", "सॉहचियार", "सॉहचियार", d=("Rice cooked with meat.", "मांस के साथ पका चावल।", "मांसासह शिजवलेला भात.")),
        it3("chilli", "Mizo chilli", "मिज़ो मिर्च", "मिझो मिरची", d=("Small, very hot chilli; a registered GI.", "छोटी, बहुत तीखी मिर्च; पंजीकृत जीआई।", "लहान, अतिशय तिखट मिरची; नोंदणीकृत जीआय.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]; g = mo["gsva2024_25_current_lakh"]
sect, _ = sector_table(g)
sh = {k: 100 * v / g["total"] for k, v in g.items()}
ur = AP["plfs_ur_15plus_psss"]["MZ"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["MZ"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Mizoram's GSDP at current prices was about ₹{inr(cur['FY2024-25'][0])} crore in FY2024-25, the latest year in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2024-25'][0])}. Agriculture, livestock, forestry and fishing contributed about {sh['agri']:.0f}% of GSVA, much of it from forestry and logging; farmers grow rice, maize, ginger, chillies, oranges, bananas and anthurium flowers, and many still practise jhum (shifting) cultivation. In the MoSPI figures electricity, gas and water supply made up about {sh['utilities']:.0f}% of GSVA, reflecting the Tuirial and other hydro stations, while public administration was about {sh['public_admin']:.0f}% and manufacturing under 1%. Bamboo is a major resource.\n\nThe PLFS unemployment rate was {ur['2025']}% in 2025 (national {ui['2025']}%), and {lf['female']}% of women aged 15 and above were in the labour force, against {lfi['female']}% nationally.",
        f"मोस्पी शृंखला के नवीनतम वर्ष, वित्त वर्ष 2024-25 में मिज़ोरम का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{inr(cur['FY2024-25'][0])} करोड़ और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2024-25'][0])} था। कृषि, पशुपालन, वानिकी और मत्स्य पालन का जीएसवीए में योगदान लगभग {sh['agri']:.0f}% था, जिसका बड़ा हिस्सा वानिकी और लकड़ी कटाई से है; किसान धान, मक्का, अदरक, मिर्च, संतरे, केले और एंथुरियम फूल उगाते हैं, और बहुत से अब भी झूम (स्थानांतरी) खेती करते हैं। मोस्पी आँकड़ों में बिजली, गैस और जल आपूर्ति का हिस्सा लगभग {sh['utilities']:.0f}% था, जो तुइरियाल और अन्य जलविद्युत केंद्रों को दर्शाता है, जबकि लोक प्रशासन लगभग {sh['public_admin']:.0f}% और विनिर्माण 1% से कम था। बाँस एक बड़ा संसाधन है।\n\nपीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी (राष्ट्रीय {ui['2025']}%), और 15 वर्ष से अधिक आयु की {lf['female']}% महिलाएँ श्रम बल में थीं, जबकि राष्ट्रीय स्तर पर {lfi['female']}%।",
        f"मोस्पी मालिकेतील नवीनतम वर्ष, आ.व. 2024-25 मध्ये मिझोरामचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{inr(cur['FY2024-25'][0])} कोटी व दरडोई एनएसडीपी ₹{inr(pc['FY2024-25'][0])} होते. शेती, पशुपालन, वनीकरण व मासेमारीचा जीएसव्हीएमध्ये वाटा सुमारे {sh['agri']:.0f}% होता, ज्यातील बराचसा वनीकरण व लाकूडतोडीतून; शेतकरी भात, मका, आले, मिरची, संत्री, केळी व अँथुरियम फुले घेतात, आणि अनेक जण अजूनही झूम (स्थलांतरित) शेती करतात. मोस्पी आकड्यांत वीज, वायू व पाणीपुरवठ्याचा वाटा सुमारे {sh['utilities']:.0f}% होता, जो तुइरियाल व इतर जलविद्युत केंद्रांमुळे आहे, तर लोकप्रशासन सुमारे {sh['public_admin']:.0f}% व उत्पादन उद्योग 1% पेक्षा कमी होता. बांबू हे मोठे संसाधन आहे.\n\nपीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता (राष्ट्रीय {ui['2025']}%), आणि 15 वर्षांवरील {lf['female']}% स्त्रिया श्रमशक्तीत होत्या, तर राष्ट्रीय पातळीवर {lfi['female']}%."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE), "rupee", "higher-is-better",
             previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("MZ", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    plfs_series("MZ", NAME),
    gaps("g", [
        (L("Hydropower share of GSVA — explanation from the State DES", "जीएसवीए में जलविद्युत का हिस्सा — राज्य डीईएस से स्पष्टीकरण", "जीएसव्हीएमधील जलविद्युतचा वाटा — राज्य डीईएसकडून स्पष्टीकरण"), "state-economic-survey", "Mizoram Economic Survey."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Mizoram has a unicameral, 40-member Legislative Assembly in Aizawl. Three Autonomous District Councils under the Sixth Schedule — for the Chakma, Lai and Mara peoples — govern parts of the south, and Article 371G of the Constitution protects Mizo religious and social practices, customary law and land ownership. The State elects 1 member to the Lok Sabha and 1 to the Rajya Sabha.\n\nThe Zoram People's Movement won 27 seats in the 2023 election, the first time a party other than the Congress or the MNF formed the government, and Lalduhoma was sworn in as Chief Minister on 8 December 2023. Lalbiakzama was elected Speaker on 12 December 2023, and Gen. V. K. Singh (Retd) has been Governor since 16 January 2025. The next Assembly election is due by late 2028.",
        "मिज़ोरम में आइज़ोल में 40 सदस्यों वाली एकसदनीय विधानसभा है। छठी अनुसूची के तहत तीन स्वायत्त ज़िला परिषदें — चकमा, लाई और मारा लोगों के लिए — दक्षिण के भागों का शासन करती हैं, और संविधान का अनुच्छेद 371छ मिज़ो धार्मिक और सामाजिक प्रथाओं, प्रथागत क़ानून और भूमि स्वामित्व की रक्षा करता है। राज्य से लोकसभा का 1 और राज्यसभा का 1 सदस्य चुना जाता है।\n\n2023 के चुनाव में ज़ोरम पीपुल्स मूवमेंट ने 27 सीटें जीतीं, पहली बार कांग्रेस या एमएनएफ़ के अलावा किसी दल ने सरकार बनाई, और लालदुहोमा ने 8 दिसंबर 2023 को मुख्यमंत्री पद की शपथ ली। लालबियाकज़ामा 12 दिसंबर 2023 को अध्यक्ष चुने गए, और जनरल वी. के. सिंह (सेवानिवृत्त) 16 जनवरी 2025 से राज्यपाल हैं। अगला विधानसभा चुनाव 2028 के अंत तक होना है।",
        "मिझोराममध्ये आयझॉल येथे 40 सदस्यांची एकसदनी विधानसभा आहे. सहाव्या अनुसूचीखालील तीन स्वायत्त जिल्हा परिषदा — चकमा, लाई व मारा लोकांसाठी — दक्षिणेकडील भागांचा कारभार पाहतात, आणि संविधानाचा अनुच्छेद 371छ मिझो धार्मिक व सामाजिक प्रथा, रूढी कायदा व जमीन मालकीचे संरक्षण करतो. राज्यातून लोकसभेवर 1 व राज्यसभेवर 1 सदस्य निवडला जातो.\n\n2023 च्या निवडणुकीत झोरम पीपल्स मूव्हमेंटने 27 जागा जिंकल्या, प्रथमच काँग्रेस किंवा एमएनएफव्यतिरिक्त पक्षाने सरकार स्थापन केले, आणि लालदुहोमा यांनी 8 डिसेंबर 2023 रोजी मुख्यमंत्रिपदाची शपथ घेतली. लालबियाकझामा 12 डिसेंबर 2023 रोजी अध्यक्षपदी निवडले गेले, आणि जनरल व्ही. के. सिंह (निवृत्त) 16 जानेवारी 2025 पासून राज्यपाल आहेत. पुढील विधानसभा निवडणूक 2028 च्या अखेरीपर्यंत होणे अपेक्षित आहे."),
        sources=["udayavani", "mz-assembly", "newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("assembly", "Mizoram Legislative Assembly", "मिज़ोरम विधानसभा", "मिझोराम विधानसभा", url="https://mizoramassembly.in", src="mz-assembly"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [(L("2023 Assembly election — party-wise result", "2023 विधानसभा चुनाव — दलवार परिणाम", "2023 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Mizoram 2023.")]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "The Bairabi–Sairang railway brought trains close to Aizawl in 2025. The Kaladan Multi-Modal Transit Transport Project, which will link Mizoram by road and river to the port of Sittwe in Myanmar, and the Aizawl bypass road will be added as cards once their status is confirmed from official sources.",
        "बइराबी–सैरांग रेलवे 2025 में आइज़ोल के पास तक ट्रेनें ले आई। कलादान बहु-मॉडल पारगमन परिवहन परियोजना, जो मिज़ोरम को सड़क और नदी से म्यांमार के सित्तवे बंदरगाह से जोड़ेगी, और आइज़ोल बाईपास सड़क आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर कार्ड के रूप में जोड़ी जाएँगी।",
        "बइराबी–सैरांग रेल्वेने 2025 मध्ये आयझॉलजवळ गाड्या आणल्या. कलादान बहुविध पारगमन वाहतूक प्रकल्प, जो मिझोरामला रस्ता व नदीमार्गे म्यानमारमधील सित्तवे बंदराशी जोडेल, आणि आयझॉल बाह्यवळण रस्ता अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर कार्डे म्हणून जोडले जातील."),
        sources=["newsonair"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [(L("Kaladan Multi-Modal Transit Transport Project — status", "कलादान बहु-मॉडल परियोजना — स्थिति", "कलादान बहुविध प्रकल्प — स्थिती"), "india-gov", "Ministry of External Affairs / Parliament answers.")]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Mizoram's main road link is NH-306 from Silchar in Assam to Aizawl; NH-54 runs south to Lunglei and Tuipang. Lengpui Airport, about 30 km from Aizawl, has flights to Kolkata, Guwahati, Delhi and Imphal, and the new railway terminus at Sairang connects to the national network. Roads are winding and often blocked by landslides in the monsoon. Visitors from other States need an Inner Line Permit.",
        "मिज़ोरम का मुख्य सड़क संपर्क असम के सिलचर से आइज़ोल तक एनएच-306 है; एनएच-54 दक्षिण में लुंगलेई और तुइपांग तक जाता है। आइज़ोल से लगभग 30 किमी दूर लेंगपुई हवाई अड्डे से कोलकाता, गुवाहाटी, दिल्ली और इंफाल की उड़ानें हैं, और सैरांग का नया रेलवे टर्मिनल राष्ट्रीय नेटवर्क से जुड़ता है। सड़कें घुमावदार हैं और मानसून में अक्सर भूस्खलन से बंद हो जाती हैं। दूसरे राज्यों के पर्यटकों को इनर लाइन परमिट चाहिए।",
        "मिझोरामचा मुख्य रस्ते संपर्क आसाममधील सिलचर ते आयझॉल एनएच-306 आहे; एनएच-54 दक्षिणेला लुंगलेई व तुइपांगपर्यंत जातो. आयझॉलपासून सुमारे 30 किमीवरील लेंगपुई विमानतळावरून कोलकाता, गुवाहाटी, दिल्ली व इंफाळसाठी उड्डाणे आहेत, आणि सैरांग येथील नवे रेल्वे स्थानक राष्ट्रीय जाळ्याशी जोडते. रस्ते वळणावळणाचे आहेत व पावसाळ्यात अनेकदा भूस्खलनाने बंद होतात. इतर राज्यांतील पर्यटकांना इनर लाइन परवाना लागतो."),
        conf="Editorial"),
    lst("airports", [it3("ajl", "Lengpui Airport", "लेंगपुई हवाई अड्डा", "लेंगपुई विमानतळ", m=("AJL", "AJL", "AJL"))], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [(L("Road length by category", "श्रेणीवार सड़क लंबाई", "प्रकारनिहाय रस्त्यांची लांबी"), "morth", "Basic Road Statistics of India.")]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Mizoram's fast rivers give it hydropower potential. NEEPCO's Tuirial project near Aizawl and the State's small hydro stations supply part of the demand, the Serlui B project serves the north, and the State also buys power through the North-Eastern grid. Solar power is being added in villages and towns.",
        "मिज़ोरम की तेज़ नदियाँ इसे जलविद्युत क्षमता देती हैं। आइज़ोल के पास नीपको की तुइरियाल परियोजना और राज्य के छोटे जलविद्युत केंद्र माँग का एक भाग पूरा करते हैं, सेरलुई बी परियोजना उत्तर की सेवा करती है, और राज्य पूर्वोत्तर ग्रिड से भी बिजली ख़रीदता है। गाँवों और नगरों में सौर ऊर्जा जोड़ी जा रही है।",
        "मिझोरामच्या वेगवान नद्या त्याला जलविद्युत क्षमता देतात. आयझॉलजवळील नीपकोचा तुइरियाल प्रकल्प व राज्याची लहान जलविद्युत केंद्रे मागणीचा काही भाग पुरवतात, सेरलुई बी प्रकल्प उत्तरेला सेवा देतो, आणि राज्य ईशान्य ग्रिडमार्फतही वीज खरेदी करते. गावे व शहरांत सौरऊर्जा वाढवली जात आहे."),
        conf="Editorial"),
    gaps("g", [(L("Installed capacity by station", "केंद्रवार स्थापित क्षमता", "केंद्रनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report.")]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Mobile networks cover Aizawl and most towns; villages in deep valleys and along the borders have weaker coverage. The State offers many services online, and Mizoram University, NIT Mizoram and ICFAI University train students in computing.",
        "मोबाइल नेटवर्क आइज़ोल और अधिकांश नगरों को कवर करते हैं; गहरी घाटियों और सीमाओं के गाँवों में कवरेज कमज़ोर है। राज्य कई सेवाएँ ऑनलाइन देता है, और मिज़ोरम विश्वविद्यालय, एनआईटी मिज़ोरम और आईसीएफ़एआई विश्वविद्यालय कंप्यूटिंग में छात्रों को प्रशिक्षित करते हैं।",
        "मोबाइल जाळे आयझॉल व बहुतेक शहरांना व्यापते; खोल दऱ्या व सीमांलगतच्या गावांत संपर्क कमकुवत आहे. राज्य अनेक सेवा ऑनलाइन देते, आणि मिझोराम विद्यापीठ, एनआयटी मिझोराम व आयसीएफएआय विद्यापीठ संगणनाचे शिक्षण देतात."),
        conf="Editorial"),
    gaps("g", [(L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (North East circle).")]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("MZ", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["MZ"]; ger = AP["aishe_ger"]["MZ"]
module(R, "education", [
    prose("p1", L(
        f"Literacy in Mizoram was 91.3% at the 2011 Census, a result of the mission schools that spread across the hills from the 1890s. The higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE, above the national 28.4%, with women at {gf}% and men at {gm}%. Mizoram University, a central university at Tanhril, NIT Mizoram and the Mizoram Institute of Medical Education and Research are the main institutions.",
        f"2011 की जनगणना में मिज़ोरम की साक्षरता 91.3% थी, जो 1890 के दशक से पहाड़ियों में फैले मिशन स्कूलों का परिणाम है। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था, जो राष्ट्रीय 28.4% से अधिक है, महिलाएँ {gf}% और पुरुष {gm}%। तानहरिल का मिज़ोरम विश्वविद्यालय (केंद्रीय), एनआईटी मिज़ोरम और मिज़ोरम आयुर्विज्ञान शिक्षा एवं अनुसंधान संस्थान मुख्य संस्थान हैं।",
        f"2011 च्या जनगणनेत मिझोरामची साक्षरता 91.3% होती, जी 1890 च्या दशकापासून टेकड्यांत पसरलेल्या मिशन शाळांचा परिणाम आहे. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा अधिक, स्त्रिया {gf}% व पुरुष {gm}%. तानह्रिल येथील मिझोराम विद्यापीठ (केंद्रीय), एनआयटी मिझोराम व मिझोराम वैद्यकीय शिक्षण व संशोधन संस्था या मुख्य संस्था आहेत."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    gaps("g", [(L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year.")]),
])

# ---------------- O. Health ----------------
n = NF["MZ"]; s = C["srs"]["MZ"]
module(R, "health", [
    prose("p1", L(
        f"Mizoram's infant mortality rate was {s[5]:.0f} per 1,000 live births in 2020 in the Sample Registration System, down from {s[4]} in 2010; small States have large sampling errors. The birth rate was {s[1]} and the death rate {s[3]} per 1,000. In NFHS-5, {n['institutional_N5']:.1f}% of births took place in health facilities; {n['stunted'][1]:.1f}% of children under five were stunted, {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight, with wasting up from {n['wasted'][0]}% in NFHS-4. The Civil Hospital in Aizawl and the Zoram Medical College at Falkawn are the main referral centres.",
        f"नमूना पंजीकरण प्रणाली में 2020 में मिज़ोरम की शिशु मृत्यु दर प्रति 1,000 जीवित जन्म पर {s[5]:.0f} थी, जो 2010 के {s[4]} से कम है; छोटे राज्यों में नमूना त्रुटियाँ बड़ी होती हैं। जन्म दर प्रति 1,000 पर {s[1]} और मृत्यु दर {s[3]} थी। एनएफ़एचएस-5 में {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए; पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने, {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के थे, और दुबलापन एनएफ़एचएस-4 के {n['wasted'][0]}% से बढ़ा। आइज़ोल का सिविल अस्पताल और फ़ालकॉन का ज़ोरम मेडिकल कॉलेज मुख्य रेफ़रल केंद्र हैं।",
        f"नमुना नोंदणी पद्धतीनुसार 2020 मध्ये मिझोरामचा अर्भक मृत्युदर दर 1,000 जिवंत जन्मांमागे {s[5]:.0f} होता, 2010 मधील {s[4]} वरून कमी; लहान राज्यांत नमुना त्रुटी मोठ्या असतात. जन्मदर दर 1,000 मागे {s[1]} व मृत्युदर {s[3]} होता. एनएफएचएस-5 मध्ये {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या; पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी, {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची होती, आणि कृशता एनएफएचएस-4 मधील {n['wasted'][0]}% वरून वाढली. आयझॉलचे सिव्हिल रुग्णालय व फालकॉन येथील झोरम वैद्यकीय महाविद्यालय ही मुख्य संदर्भ केंद्रे आहेत."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2. Small States have larger sampling errors."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("MZ"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [(L("Hospital beds and doctors per lakh population", "प्रति लाख जनसंख्या अस्पताल बिस्तर और डॉक्टर", "दर लाख लोकसंख्येमागे रुग्णालय खाटा व डॉक्टर"), "mohfw", "Rural Health Statistics / National Health Profile.")]),
])
print("mz mod2 ok")
