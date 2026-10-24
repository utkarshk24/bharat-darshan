"""Goa modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-GA"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_GA = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 24 Oct 2026. "
           "FY2024-25 is the latest year published for Goa and may be revised.")
mo = research("mospi_ga.json")
C = research("census_b5plus.json")
NAME = L("Goa", "गोवा", "गोवा")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Goan culture mixes Konkani traditions with four and a half centuries of Portuguese influence. Music is everywhere: the mando, a slow, graceful song-dance of Catholic Goa, the dulpod and the dekhni; the fugdi and dhalo dances of Hindu women; the ghumot, a clay drum covered with monitor-lizard skin and now made with goatskin, which is the State heritage instrument; and the brass bands of village fests. Tiatr, popular Konkani musical theatre that began in 1892, draws packed audiences. Konkani literature has produced two Jnanpith laureates from Goa, Ravindra Kelekar and Damodar Mauzo. Crafts include azulejo tiles, terracotta, brass-ware and coconut-shell work, and the International Film Festival of India has been held in Panaji every year since 2004.",
        "गोवा की संस्कृति कोंकणी परंपराओं को साढ़े चार सदियों के पुर्तगाली प्रभाव से जोड़ती है। संगीत हर जगह है: कैथोलिक गोवा का धीमा, सुंदर गीत-नृत्य मांडो, दुलपोद और देखणी; हिंदू महिलाओं के फुगडी और धालो नृत्य; घुमट, मिट्टी का ढोल जो पहले घोरपड़ की खाल से और अब बकरी की खाल से बनता है और राज्य का धरोहर वाद्य है; और गाँव के फ़ेस्त के ब्रास बैंड। 1892 में शुरू हुआ लोकप्रिय कोंकणी संगीत नाट्य तियात्र खचाखच भरे दर्शकों को खींचता है। कोंकणी साहित्य ने गोवा से दो ज्ञानपीठ विजेता दिए हैं, रवींद्र केळेकर और दामोदर मावजो। शिल्पों में अज़ुलेजो टाइलें, टेराकोटा, पीतल के बर्तन और नारियल के खोल का काम शामिल हैं, और भारत का अंतरराष्ट्रीय फ़िल्म महोत्सव 2004 से हर वर्ष पणजी में होता है।",
        "गोमंतकीय संस्कृती कोकणी परंपरांना साडेचार शतकांच्या पोर्तुगीज प्रभावाशी जोडते. संगीत सर्वत्र आहे: कॅथलिक गोव्याचे संथ, डौलदार गीत-नृत्य मांडो, दुलपद व देखणी; हिंदू स्त्रियांची फुगडी व धालो नृत्ये; घुमट, मातीचे वाद्य जे पूर्वी घोरपडीच्या कातड्याने व आता बकरीच्या कातड्याने बनते आणि जे राज्याचे वारसा वाद्य आहे; आणि गावच्या फेस्तांचे ब्रास बँड. 1892 मध्ये सुरू झालेले लोकप्रिय कोकणी संगीत नाट्य तियात्र खच्चून भरलेल्या प्रेक्षकांना खेचते. कोकणी साहित्याने गोव्यातून दोन ज्ञानपीठ विजेते दिले आहेत, रवींद्र केळेकर व दामोदर मावजो. हस्तकलांत अझुलेजो फरशा, टेराकोटा, पितळी भांडी व करवंटीकाम यांचा समावेश आहे, आणि भारतीय आंतरराष्ट्रीय चित्रपट महोत्सव 2004 पासून दरवर्षी पणजीत भरतो."),
        conf="Editorial"),
    lst("festivals", [
        fest("carnival", "Carnival", "कार्निवल", "कार्निव्हल", ("February (before Lent)", "फ़रवरी (लेंट से पहले)", "फेब्रुवारी (लेंटपूर्वी)"),
             ("Float parades led by King Momo through Panaji, Margao and Mapusa.", "किंग मोमो के नेतृत्व में पणजी, मडगाँव और म्हापसा में झाँकियों की परेड।", "किंग मोमोच्या नेतृत्वाखाली पणजी, मडगाव व म्हापशात चित्ररथांची मिरवणूक.")),
        fest("shigmo", "Shigmo", "शिगमो", "शिगमो", ("March (Phalgun)", "मार्च (फाल्गुन)", "मार्च (फाल्गुन)"),
             ("Spring festival with folk dances and float processions.", "लोकनृत्यों और झाँकियों वाला वसंत उत्सव।", "लोकनृत्ये व चित्ररथ मिरवणुकांचा वसंतोत्सव.")),
        fest("saojoao", "São João", "साओ जोआओ", "सांजाव", ("24 June", "24 जून", "24 जून"),
             ("Monsoon feast of St John; young men leap into wells and streams.", "संत जॉन का मानसूनी पर्व; युवक कुओं और नालों में कूदते हैं।", "संत जॉनचे पावसाळी फेस्त; तरुण विहिरी व ओढ्यांत उड्या मारतात.")),
        fest("xavier", "Feast of St Francis Xavier", "संत फ़्रांसिस ज़ेवियर का पर्व", "संत फ्रान्सिस झेविअरचे फेस्त", ("3 December", "3 दिसंबर", "3 डिसेंबर"),
             ("Pilgrimage to the Basilica of Bom Jesus in Old Goa.", "पुराने गोवा के बेसिलिका ऑफ़ बॉम जीसस की तीर्थयात्रा।", "जुन्या गोव्यातील बॅसिलिका ऑफ बॉम जीझसची यात्रा.")),
        fest("chavath", "Chavath (Ganesh Chaturthi)", "चवथ (गणेश चतुर्थी)", "चवथ (गणेश चतुर्थी)", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Goa's biggest Hindu festival, with matoli canopies of forest fruit.", "गोवा का सबसे बड़ा हिंदू त्योहार, जंगली फलों की माटोळी के साथ।", "गोव्याचा सर्वांत मोठा हिंदू सण, रानफळांच्या माटोळीसह.")),
        fest("zatra", "Temple zatras", "मंदिर जात्राएँ", "देवळांच्या जत्रा", ("Varies", "भिन्न", "वेगवेगळे"),
             ("Annual temple fairs at Mangeshi, Shantadurga and Shirgao.", "मंगेशी, शांतादुर्गा और शिरगाँव में वार्षिक मंदिर मेले।", "मंगेशी, शांतादुर्गा व शिरगाव येथील वार्षिक जत्रा.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("mando", "Mando", "मांडो", "मांडो"), it3("tiatr", "Tiatr", "तियात्र", "तियात्र"),
        it3("fugdi", "Fugdi and dhalo", "फुगडी और धालो", "फुगडी व धालो"), it3("ghumot", "Ghumot", "घुमट", "घुमट"),
        it3("azulejo", "Azulejo tiles", "अज़ुलेजो टाइलें", "अझुलेजो फरशा"), it3("terracotta", "Terracotta", "टेराकोटा", "टेराकोटा"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("xitkodi", "Xitt-kodi (fish curry and rice)", "शीत-कोडी (मछली करी और चावल)", "शीत-कोडी (माशांची आमटी व भात)", d=("The everyday meal, with coconut and kokum.", "रोज़ का भोजन, नारियल और कोकम के साथ।", "रोजचे जेवण, नारळ व कोकमसह.")),
        it3("xacuti", "Xacuti and cafreal", "शाकुती और कैफ़्रियल", "शागुती व कफ्रियाल", d=("Roasted-spice and green-masala chicken curries.", "भुने मसालों और हरे मसालों वाली चिकन करी।", "भाजलेल्या मसाल्यांची व हिरव्या मसाल्याची कोंबडी.")),
        it3("vindaloo", "Vindaloo and sorpotel", "विंदालू और सोरपोतेल", "विंदालू व सोरपोतेल", d=("Tangy pork dishes of Portuguese origin.", "पुर्तगाली मूल के खट्टे पोर्क व्यंजन।", "पोर्तुगीज मूळचे आंबट डुकराच्या मांसाचे पदार्थ.")),
        it3("bebinca", "Bebinca", "बेबिंका", "बेबिंका", d=("Layered coconut-milk and egg dessert; a registered GI.", "नारियल के दूध और अंडे की परतदार मिठाई; पंजीकृत जीआई।", "नारळाचे दूध व अंड्याची थरांची मिठाई; नोंदणीकृत जीआय.")),
        it3("feni", "Feni", "फ़ेनी", "फेणी", d=("Spirit distilled from cashew apples or coconut toddy; a registered GI.", "काजू फल या नारियल ताड़ी से बनी मदिरा; पंजीकृत जीआई।", "काजूबोंड किंवा माडाच्या माडीपासून गाळलेले मद्य; नोंदणीकृत जीआय.")),
        it3("poi", "Poi and pao", "पोई और पाव", "पोई व पाव", d=("Wheat breads from the village poder.", "गाँव के पोदेर की गेहूँ की रोटियाँ।", "गावच्या पोदेराचे गव्हाचे पाव.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("kunbi", "Kunbi saree", "कुणबी साड़ी", "कुणबी साडी", d=("Red-and-white checked cotton saree of the Kunbi and Gawda women.", "कुणबी और गावडा महिलाओं की लाल-सफ़ेद चेक वाली सूती साड़ी।", "कुणबी व गावडा स्त्रियांची लाल-पांढऱ्या चौकड्यांची सुती साडी.")),
        it3("pano", "Pano bhaju", "पानो भाजू", "पानो भाजू", d=("Traditional dress of Catholic Goan women, now worn for mando performances.", "कैथोलिक गोवा की महिलाओं की पारंपरिक पोशाक, अब मांडो प्रस्तुतियों में पहनी जाती है।", "कॅथलिक गोमंतकीय स्त्रियांचा पारंपरिक पोशाख, आता मांडो सादरीकरणात परिधान केला जातो.")),
        it3("nauvari", "Nauvari saree", "नौवारी साड़ी", "नऊवारी साडी", d=("Nine-yard saree worn by Hindu women at festivals.", "त्योहारों पर हिंदू महिलाओं द्वारा पहनी जाने वाली नौ गज़ की साड़ी।", "सणांना हिंदू स्त्रिया नेसतात ती नऊवारी साडी.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; util = 100 * g["utilities"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["GA"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["GA"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Goa's GSDP at current prices was about ₹{cur['FY2024-25'][0]/1e5:.2f} lakh crore in FY2024-25, the latest year published for the State in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2024-25'][0])} — second only to Sikkim among the 30 States and UTs with a figure for that year. Manufacturing made up about {mfg:.0f}% of GSVA, largely pharmaceuticals, chemicals, food processing and electronics in industrial estates such as Verna, Kundaim and Pilerne; electricity, gas and water supply about {util:.0f}%; and agriculture, fishing and forestry about {agri:.0f}%. Tourism is a mainstay, supporting hotels, restaurants, transport and trade, and fishing, cashew, coconut, rice and mangoes remain important in villages. Iron-ore mining, once a major export industry, was halted by a Supreme Court order in 2018; mining contributed less than 1% of GSVA in FY2024-25.\n\nGoa has a high unemployment rate for its income level: the PLFS rate was {ur['2025']}% in 2025 (down from {ur['2022']}% in 2022), against {ui['2025']}% nationally, and {lf['female']}% of women aged 15 and above were in the labour force, against {lfi['female']}% in India.",
        f"मोस्पी शृंखला में राज्य के लिए प्रकाशित नवीनतम वर्ष, वित्त वर्ष 2024-25 में गोवा का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2024-25'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2024-25'][0])} — उस वर्ष के आँकड़े वाले 30 राज्यों और केंद्र शासित प्रदेशों में केवल सिक्किम से कम। जीएसवीए में विनिर्माण का हिस्सा लगभग {mfg:.0f}% था, अधिकतर वेर्णा, कुंडई और पिलेर्ण जैसे औद्योगिक क्षेत्रों में दवाएँ, रसायन, खाद्य प्रसंस्करण और इलेक्ट्रॉनिक्स; बिजली, गैस और जल आपूर्ति का लगभग {util:.0f}%; और कृषि, मत्स्य पालन और वानिकी का लगभग {agri:.0f}%। पर्यटन मुख्य आधार है, जो होटलों, रेस्तराँओं, परिवहन और व्यापार को सहारा देता है, और गाँवों में मछली पकड़ना, काजू, नारियल, धान और आम आज भी महत्त्वपूर्ण हैं। कभी बड़ा निर्यात उद्योग रहा लौह अयस्क खनन 2018 में सर्वोच्च न्यायालय के आदेश से रुका; वित्त वर्ष 2024-25 में खनन का जीएसवीए में योगदान 1% से कम था।\n\nअपनी आय के स्तर के हिसाब से गोवा में बेरोज़गारी दर ऊँची है: पीएलएफ़एस दर 2025 में {ur['2025']}% थी (2022 के {ur['2022']}% से कम), जबकि राष्ट्रीय स्तर पर {ui['2025']}%, और 15 वर्ष से अधिक आयु की {lf['female']}% महिलाएँ श्रम बल में थीं, जबकि भारत में {lfi['female']}%।",
        f"मोस्पी मालिकेत राज्यासाठी प्रकाशित नवीनतम वर्ष, आ.व. 2024-25 मध्ये गोव्याचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2024-25'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2024-25'][0])} — त्या वर्षीचा आकडा असलेल्या 30 राज्ये व केंद्रशासित प्रदेशांत केवळ सिक्कीमखालोखाल. जीएसव्हीएमध्ये उत्पादन उद्योगाचा वाटा सुमारे {mfg:.0f}% होता, बहुतांश वेर्णा, कुंडई व पिळर्णसारख्या औद्योगिक वसाहतींतील औषधे, रसायने, अन्नप्रक्रिया व इलेक्ट्रॉनिक्स; वीज, वायू व पाणीपुरवठ्याचा सुमारे {util:.0f}%; आणि शेती, मासेमारी व वनीकरणाचा सुमारे {agri:.0f}%. पर्यटन हा मुख्य आधार आहे, जो हॉटेल, उपाहारगृहे, वाहतूक व व्यापाराला आधार देतो, आणि गावांत मासेमारी, काजू, नारळ, भात व आंबे आजही महत्त्वाचे आहेत. एकेकाळी मोठा निर्यात उद्योग असलेले लोहखनिज खाणकाम 2018 मध्ये सर्वोच्च न्यायालयाच्या आदेशाने थांबले; आ.व. 2024-25 मध्ये खाणकामाचा जीएसव्हीएमधील वाटा 1% पेक्षा कमी होता.\n\nउत्पन्नाच्या पातळीच्या मानाने गोव्यात बेरोजगारी दर जास्त आहे: पीएलएफएस दर 2025 मध्ये {ur['2025']}% होता (2022 मधील {ur['2022']}% वरून कमी), तर राष्ट्रीय पातळीवर {ui['2025']}%, आणि 15 वर्षांवरील {lf['female']}% स्त्रिया श्रमशक्तीत होत्या, तर भारतात {lfi['female']}%."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_GA), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_GA), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_GA), "rupee", "higher-is-better",
             previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("GA", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    plfs_series("GA", NAME),
    lst("sectors-key", [
        it3("tourism", "Tourism", "पर्यटन", "पर्यटन", d=("Beaches, heritage and events; hotels, shacks and taxis.", "समुद्र तट, धरोहर और आयोजन; होटल, शैक और टैक्सियाँ।", "किनारे, वारसा व कार्यक्रम; हॉटेल, शॅक व टॅक्सी.")),
        it3("pharma", "Pharmaceuticals", "दवा उद्योग", "औषधनिर्मिती", d=("Plants in Verna, Kundaim and other estates.", "वेर्णा, कुंडई और अन्य क्षेत्रों में संयंत्र।", "वेर्णा, कुंडई व इतर वसाहतींत कारखाने.")),
        it3("mining", "Iron-ore mining", "लौह अयस्क खनन", "लोहखनिज खाणकाम", d=("Once the main export; halted in 2018 and being restarted through auctions.", "कभी मुख्य निर्यात; 2018 में रुका और नीलामी से फिर शुरू हो रहा है।", "एकेकाळी मुख्य निर्यात; 2018 मध्ये थांबले व लिलावांद्वारे पुन्हा सुरू होत आहे.")),
        it3("fish", "Fisheries", "मत्स्य पालन", "मत्स्यव्यवसाय", d=("Mackerel, sardines and prawns; Malim and Cutbona jetties.", "बांगड़ा, तारले और झींगे; मालीम और कुटबोणा जेटी।", "बांगडा, तारले व कोळंबी; मालीम व कुटबोणा जेटी.")),
        it3("cashew", "Cashew and feni", "काजू और फ़ेनी", "काजू व फेणी", d=("Cashew processing and distilling; Goa cashew is a registered GI.", "काजू प्रसंस्करण और आसवन; गोवा काजू पंजीकृत जीआई है।", "काजूप्रक्रिया व गाळप; गोवा काजू नोंदणीकृत जीआय आहे.")),
        it3("port", "Port and shipbuilding", "बंदरगाह और जहाज़ निर्माण", "बंदर व जहाजबांधणी", d=("Mormugao port; Goa Shipyard at Vasco.", "मुरगाँव बंदरगाह; वास्को में गोवा शिपयार्ड।", "मुरगाव बंदर; वास्को येथील गोवा शिपयार्ड.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Tourist arrivals by year", "वर्षवार पर्यटक आगमन", "वर्षनिहाय पर्यटक आगमन"), "tourism", "Goa Department of Tourism."),
        (L("Iron-ore mining restart — leases and output", "लौह अयस्क खनन की पुनः शुरुआत — पट्टे और उत्पादन", "लोहखनिज खाणकाम पुन्हा सुरू — भाडेपट्टे व उत्पादन"), "india-gov", "Goa Directorate of Mines and Geology / Indian Bureau of Mines."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Goa has a unicameral legislature, the 40-member Legislative Assembly, which sits at Porvorim across the Mandovi from Panaji. The State elects 2 members to the Lok Sabha and 1 to the Rajya Sabha.\n\nAfter the Assembly election of February 2022 the Bharatiya Janata Party formed the government, and Pramod Sawant — Chief Minister since March 2019 — was sworn in for a second term on 28 March 2022. Ganesh Gaonkar (BJP) was elected Speaker in September 2025, after Ramesh Tawadkar joined the Cabinet. Pusapati Ashok Gajapathi Raju has been Governor since 26 July 2025. The next Assembly election is due by early 2027.",
        "गोवा में एकसदनीय विधानमंडल है, 40 सदस्यों वाली विधानसभा, जिसकी बैठकें पणजी के सामने मांडवी के पार पोरवोरिम में होती हैं। राज्य से लोकसभा के 2 और राज्यसभा का 1 सदस्य चुना जाता है।\n\nफ़रवरी 2022 के विधानसभा चुनाव के बाद भारतीय जनता पार्टी ने सरकार बनाई, और मार्च 2019 से मुख्यमंत्री प्रमोद सावंत ने 28 मार्च 2022 को दूसरे कार्यकाल की शपथ ली। रमेश तावडकर के मंत्रिमंडल में शामिल होने के बाद सितंबर 2025 में गणेश गावकर (भाजपा) अध्यक्ष चुने गए। पुसपति अशोक गजपति राजू 26 जुलाई 2025 से राज्यपाल हैं। अगला विधानसभा चुनाव 2027 की शुरुआत तक होना है।",
        "गोव्यात एकसदनी विधिमंडळ आहे, 40 सदस्यांची विधानसभा, जिच्या बैठका पणजीसमोर मांडवीपलीकडील पर्वरी येथे होतात. राज्यातून लोकसभेवर 2 व राज्यसभेवर 1 सदस्य निवडला जातो.\n\nफेब्रुवारी 2022 च्या विधानसभा निवडणुकीनंतर भारतीय जनता पक्षाने सरकार स्थापन केले, आणि मार्च 2019 पासून मुख्यमंत्री असलेल्या प्रमोद सावंत यांनी 28 मार्च 2022 रोजी दुसऱ्या कारकिर्दीची शपथ घेतली. रमेश तवडकर मंत्रिमंडळात गेल्यावर सप्टेंबर 2025 मध्ये गणेश गावकर (भाजप) अध्यक्षपदी निवडले गेले. पुसपती अशोक गजपती राजू 26 जुलै 2025 पासून राज्यपाल आहेत. पुढील विधानसभा निवडणूक 2027 च्या सुरुवातीपर्यंत होणे अपेक्षित आहे."),
        sources=["the-week", "goa-dip", "newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("lokbhavan", "Lok Bhavan Goa", "लोक भवन गोवा", "लोक भवन गोवा", url="https://lokbhavan.goa.gov.in", src="india-gov"),
        it3("portal", "Government of Goa", "गोवा सरकार", "गोवा शासन", url="https://www.goa.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2022 Assembly election — party-wise result", "2022 विधानसभा चुनाव — दलवार परिणाम", "2022 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Goa 2022."),
        (L("Chief Minister's swearing-in — official source", "मुख्यमंत्री का शपथ ग्रहण — आधिकारिक स्रोत", "मुख्यमंत्र्यांचा शपथविधी — अधिकृत स्रोत"), "goa-dip", "Replace the PTI copy with the DIP Goa release."),
        (L("Leader of Opposition — official notice", "नेता प्रतिपक्ष — आधिकारिक सूचना", "विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "Goa Legislative Assembly secretariat."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Goa's new Manohar International Airport at Mopa opened in December 2022. Other recent and ongoing works include the new Zuari bridge, the four-laning of the Mumbai–Goa and Panaji–Margao highways, the doubling of the South Western Railway line through the Ghats, and the restart of iron-ore mining through auctioned blocks; these will be added as cards once their status is confirmed from official sources. Each card shows its source and the date it was checked.",
        "मोपा में गोवा का नया मनोहर अंतरराष्ट्रीय हवाई अड्डा दिसंबर 2022 में खुला। अन्य हाल के और चल रहे कार्यों में नया जुवारी पुल, मुंबई–गोवा और पणजी–मडगाँव राजमार्गों को चार-लेन करना, घाटों से गुज़रने वाली दक्षिण पश्चिम रेलवे लाइन का दोहरीकरण, और नीलाम किए गए ब्लॉकों से लौह अयस्क खनन की पुनः शुरुआत शामिल हैं; आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर इन्हें कार्ड के रूप में जोड़ा जाएगा। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "मोपा येथील गोव्याचा नवा मनोहर आंतरराष्ट्रीय विमानतळ डिसेंबर 2022 मध्ये सुरू झाला. इतर अलीकडील व चालू कामांत नवा जुवारी पूल, मुंबई–गोवा व पणजी–मडगाव महामार्गांचे चौपदरीकरण, घाटांतून जाणाऱ्या दक्षिण पश्चिम रेल्वे मार्गाचे दुहेरीकरण, आणि लिलाव केलेल्या गटांद्वारे लोहखनिज खाणकाम पुन्हा सुरू करणे यांचा समावेश आहे; अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर त्यांची कार्डे जोडली जातील. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["deccan-herald"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Mopa airport — official source and project cost", "मोपा हवाई अड्डा — आधिकारिक स्रोत और परियोजना लागत", "मोपा विमानतळ — अधिकृत स्रोत व प्रकल्प खर्च"), "civil-aviation", "Replace the news report with the PIB or Ministry of Civil Aviation release."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Goa has two airports: Dabolim near Vasco, a civil enclave at the Indian Navy's INS Hansa air station, and the new Manohar International Airport at Mopa in the north. The Konkan Railway runs along the State through Pernem, Thivim, Karmali, Madgaon and Canacona, and the South Western Railway links Vasco and Madgaon with Karnataka over the Ghats past Dudhsagar. National Highway 66 runs along the coast, and NH 748 links Panaji with Belagavi. River ferries still carry people and vehicles across the Mandovi, Zuari and other estuaries, and motorcycle taxis ('pilots') are a Goan speciality.",
        "गोवा में दो हवाई अड्डे हैं: वास्को के पास डाबोलिम, जो भारतीय नौसेना के आईएनएस हंसा हवाई स्टेशन पर नागरिक परिसर है, और उत्तर में मोपा का नया मनोहर अंतरराष्ट्रीय हवाई अड्डा। कोंकण रेलवे राज्य में पेरनेम, थिविम, करमली, मडगाँव और काणकोण से होकर चलती है, और दक्षिण पश्चिम रेलवे दूधसागर के पास से घाट पार कर वास्को और मडगाँव को कर्नाटक से जोड़ती है। राष्ट्रीय राजमार्ग 66 तट के साथ चलता है, और एनएच 748 पणजी को बेलगावी से जोड़ता है। नदी फ़ेरियाँ आज भी लोगों और वाहनों को मांडवी, जुवारी और अन्य मुहानों के पार ले जाती हैं, और मोटरसाइकिल टैक्सियाँ ('पायलट') गोवा की विशेषता हैं।",
        "गोव्यात दोन विमानतळ आहेत: वास्कोजवळील दाबोळी, जो भारतीय नौदलाच्या आयएनएस हंसा हवाई तळावरील नागरी विभाग आहे, आणि उत्तरेकडील मोपा येथील नवा मनोहर आंतरराष्ट्रीय विमानतळ. कोकण रेल्वे राज्यातून पेडणे, थिवी, करमळी, मडगाव व काणकोणमार्गे धावते, आणि दक्षिण पश्चिम रेल्वे दूधसागरजवळून घाट ओलांडून वास्को व मडगावला कर्नाटकशी जोडते. राष्ट्रीय महामार्ग 66 किनाऱ्याने जातो, आणि एनएच 748 पणजीला बेळगावीशी जोडतो. नदीतील फेरीबोटी आजही लोक व वाहनांना मांडवी, जुवारी व इतर खाड्यांपलीकडे नेतात, आणि मोटारसायकल टॅक्सी ('पायलट') ही गोव्याची खासियत आहे."),
        conf="Editorial"),
    lst("airports", [
        it3("goi", "Dabolim Airport", "डाबोलिम हवाई अड्डा", "दाबोळी विमानतळ", m=("GOI", "GOI", "GOI")),
        it3("gox", "Manohar International Airport, Mopa", "मनोहर अंतरराष्ट्रीय हवाई अड्डा, मोपा", "मनोहर आंतरराष्ट्रीय विमानतळ, मोपा", m=("GOX", "GOX", "GOX")),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics (Dabolim) and GGIAL (Mopa)."),
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Goa generates very little electricity of its own and buys most of its power from central generating stations — chiefly NTPC's coal plants in the western region — through its Electricity Department. Demand is driven by households, hotels and industry, and the State is promoting rooftop solar under national schemes. Power lines across the Western Ghats from Karnataka and Maharashtra have been debated because they pass through protected forests.",
        "गोवा स्वयं बहुत कम बिजली बनाता है और अपनी अधिकांश बिजली विद्युत विभाग के माध्यम से केंद्रीय उत्पादन केंद्रों — मुख्यतः पश्चिमी क्षेत्र में एनटीपीसी के कोयला संयंत्रों — से ख़रीदता है। माँग घरों, होटलों और उद्योगों से आती है, और राज्य राष्ट्रीय योजनाओं के तहत छतों पर सौर ऊर्जा को बढ़ावा दे रहा है। कर्नाटक और महाराष्ट्र से पश्चिमी घाट पार करने वाली बिजली लाइनें संरक्षित वनों से गुज़रने के कारण बहस का विषय रही हैं।",
        "गोवा स्वतः फारच थोडी वीज निर्माण करतो आणि आपली बहुतेक वीज वीज खात्यामार्फत केंद्रीय निर्मिती केंद्रांकडून — मुख्यतः पश्चिम विभागातील एनटीपीसीच्या कोळसा प्रकल्पांकडून — विकत घेतो. मागणी घरे, हॉटेल व उद्योगांकडून येते, आणि राज्य राष्ट्रीय योजनांअंतर्गत छतांवरील सौरऊर्जेला प्रोत्साहन देत आहे. कर्नाटक व महाराष्ट्रातून पश्चिम घाट ओलांडणाऱ्या वीजवाहिन्या संरक्षित वनांतून जात असल्याने वादाचा विषय ठरल्या आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Power purchase and own generation by source", "स्रोतवार बिजली ख़रीद और स्वयं उत्पादन", "स्रोतनिहाय वीजखरेदी व स्वनिर्मिती"), "cea", "CEA / Goa Electricity Department."),
        (L("Why utilities have a large share of GSVA", "जीएसवीए में उपयोगिताओं का बड़ा हिस्सा क्यों है", "जीएसव्हीएमध्ये उपयुक्तता सेवांचा वाटा मोठा का"), "mospi", "Check the MoSPI/DES Goa sub-sector breakdown for electricity, gas and water supply."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Goa has high mobile and internet penetration and a growing community of remote workers and start-ups, encouraged by the State's IT and start-up policies. Citizen services are delivered online through the Goa Online portal, and institutions such as IIT Goa, NIT Goa and the BITS Pilani K. K. Birla Goa campus train engineers.",
        "गोवा में मोबाइल और इंटरनेट की पहुँच ऊँची है और दूर से काम करने वालों और स्टार्टअप का बढ़ता समुदाय है, जिसे राज्य की आईटी और स्टार्टअप नीतियों से प्रोत्साहन मिला है। नागरिक सेवाएँ गोवा ऑनलाइन पोर्टल से ऑनलाइन दी जाती हैं, और आईआईटी गोवा, एनआईटी गोवा और बिट्स पिलानी के के. के. बिड़ला गोवा परिसर जैसे संस्थान इंजीनियर तैयार करते हैं।",
        "गोव्यात मोबाइल व इंटरनेटचा प्रसार जास्त आहे आणि दूरस्थ काम करणाऱ्यांचा व स्टार्टअपचा वाढता समुदाय आहे, ज्याला राज्याच्या आयटी व स्टार्टअप धोरणांनी प्रोत्साहन दिले आहे. नागरी सेवा गोवा ऑनलाइन संकेतस्थळावरून दिल्या जातात, आणि आयआयटी गोवा, एनआयटी गोवा व बिट्स पिलानीचे के. के. बिर्ला गोवा संकुल यांसारख्या संस्था अभियंते घडवतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Maharashtra & Goa circle)."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("GA", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["GA"]
ger = AP["aishe_ger"]["GA"]; nu = AP["aishe_universities_2021_22"]["GA"]; nc = AP["aishe_colleges_2021_22"]["GA"]
module(R, "education", [
    prose("p1", L(
        f"Literacy in Goa was 88.7% at the 2011 Census, among the highest in India. The higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE, above the national 28.4% and up from {ger['2017-18']}% in 2017-18, with little difference between women ({gf}%) and men ({gm}%). The State had {nu} universities and {inr(nc)} colleges.\n\nGoa University at Taleigao (1985) is the State university, and Goa Medical College at Bambolim traces its origin to a medical school founded in 1842, one of the oldest in Asia. National institutions include IIT Goa, NIT Goa, the BITS Pilani K. K. Birla Goa campus, the CSIR–National Institute of Oceanography at Dona Paula and the National Centre for Polar and Ocean Research at Vasco, which runs India's Antarctic and Arctic stations.",
        f"2011 की जनगणना में गोवा की साक्षरता 88.7% थी, जो भारत में सबसे ऊँची में है। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था, जो राष्ट्रीय 28.4% से अधिक और 2017-18 के {ger['2017-18']}% से ऊपर है, और महिलाओं ({gf}%) व पुरुषों ({gm}%) में बहुत कम अंतर था। राज्य में {nu} विश्वविद्यालय और {inr(nc)} कॉलेज थे।\n\nताळगाँव का गोवा विश्वविद्यालय (1985) राज्य विश्वविद्यालय है, और बांबोलिम का गोवा मेडिकल कॉलेज 1842 में स्थापित एक चिकित्सा विद्यालय से अपना मूल बताता है, जो एशिया के सबसे पुराने में है। राष्ट्रीय संस्थानों में आईआईटी गोवा, एनआईटी गोवा, बिट्स पिलानी का के. के. बिड़ला गोवा परिसर, डोना पाउला का सीएसआईआर–राष्ट्रीय समुद्र विज्ञान संस्थान और वास्को का राष्ट्रीय ध्रुवीय एवं समुद्री अनुसंधान केंद्र शामिल हैं, जो भारत के अंटार्कटिक और आर्कटिक केंद्र चलाता है।",
        f"2011 च्या जनगणनेत गोव्याची साक्षरता 88.7% होती, भारतातील सर्वाधिकांपैकी. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा अधिक व 2017-18 मधील {ger['2017-18']}% पेक्षा जास्त, आणि स्त्रिया ({gf}%) व पुरुष ({gm}%) यांत फारसा फरक नव्हता. राज्यात {nu} विद्यापीठे व {inr(nc)} महाविद्यालये होती.\n\nताळगावचे गोवा विद्यापीठ (1985) हे राज्य विद्यापीठ आहे, आणि बांबोळीचे गोवा वैद्यकीय महाविद्यालय 1842 मध्ये स्थापन झालेल्या वैद्यकीय शाळेपासून आपले मूळ सांगते, जी आशियातील सर्वांत जुन्यांपैकी आहे. राष्ट्रीय संस्थांत आयआयटी गोवा, एनआयटी गोवा, बिट्स पिलानीचे के. के. बिर्ला गोवा संकुल, दोना पावलची सीएसआयआर–राष्ट्रीय समुद्रविज्ञान संस्था व वास्कोचे राष्ट्रीय ध्रुवीय व सागरी संशोधन केंद्र यांचा समावेश आहे, जे भारताची अंटार्क्टिक व आर्क्टिक केंद्रे चालवते."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("gu", "Goa University", "गोवा विश्वविद्यालय", "गोवा विद्यापीठ", m=("Taleigao, 1985", "ताळगाँव, 1985", "ताळगाव, 1985")),
        it3("gmc", "Goa Medical College", "गोवा मेडिकल कॉलेज", "गोवा वैद्यकीय महाविद्यालय", m=("Bambolim (origin 1842)", "बांबोलिम (मूल 1842)", "बांबोळी (मूळ 1842)")),
        it3("iitg", "IIT Goa", "आईआईटी गोवा", "आयआयटी गोवा", m=("Goa", "गोवा", "गोवा")),
        it3("nitg", "NIT Goa", "एनआईटी गोवा", "एनआयटी गोवा", m=("Cuncolim", "कुंकळ्ळी", "कुंकळ्ळी")),
        it3("bits", "BITS Pilani K. K. Birla Goa Campus", "बिट्स पिलानी के. के. बिड़ला गोवा परिसर", "बिट्स पिलानी के. के. बिर्ला गोवा संकुल", m=("Zuarinagar", "ज़ुआरीनगर", "झुआरीनगर")),
        it3("nio", "CSIR–National Institute of Oceanography", "सीएसआईआर–राष्ट्रीय समुद्र विज्ञान संस्थान", "सीएसआयआर–राष्ट्रीय समुद्रविज्ञान संस्था", m=("Dona Paula", "डोना पाउला", "दोना पावल")),
        it3("ncpor", "National Centre for Polar and Ocean Research", "राष्ट्रीय ध्रुवीय एवं समुद्री अनुसंधान केंद्र", "राष्ट्रीय ध्रुवीय व सागरी संशोधन केंद्र", m=("Vasco", "वास्को", "वास्को")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["GA"]; s = C["srs"]["GA"]
module(R, "health", [
    prose("p1", L(
        f"Goa has some of India's best health indicators. The infant mortality rate was {s[5]:.0f} per 1,000 live births in 2020 (down from {s[4]} in 2010), far below the national 28, the birth rate was {s[1]} per 1,000 — among the lowest in India — and the death rate {s[3]}. Almost all births ({n['institutional_N5']:.1f}%) took place in health facilities in NFHS-5. Child nutrition is the weak spot: {n['stunted'][1]:.1f}% of children under five were stunted (up from {n['stunted'][0]}% in NFHS-4), {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight. Lifestyle diseases such as diabetes and hypertension are a growing concern.\n\nGoa Medical College at Bambolim is the main referral hospital, with district hospitals at Mapusa (North Goa) and Margao (South Goa) and private hospitals in Panaji, Margao and Vasco.",
        f"गोवा के स्वास्थ्य संकेतक भारत में सबसे अच्छे में हैं। 2020 में शिशु मृत्यु दर प्रति 1,000 जीवित जन्म पर {s[5]:.0f} थी (2010 के {s[4]} से कम), जो राष्ट्रीय 28 से बहुत कम है, जन्म दर प्रति 1,000 पर {s[1]} — भारत में सबसे कम में — और मृत्यु दर {s[3]} थी। एनएफ़एचएस-5 में लगभग सभी प्रसव ({n['institutional_N5']:.1f}%) स्वास्थ्य संस्थानों में हुए। बाल पोषण कमज़ोर पक्ष है: पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने थे (एनएफ़एचएस-4 के {n['stunted'][0]}% से अधिक), {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के। मधुमेह और उच्च रक्तचाप जैसे जीवनशैली रोग बढ़ती चिंता हैं।\n\nबांबोलिम का गोवा मेडिकल कॉलेज मुख्य रेफ़रल अस्पताल है, साथ में म्हापसा (उत्तर गोवा) और मडगाँव (दक्षिण गोवा) के ज़िला अस्पताल और पणजी, मडगाँव व वास्को के निजी अस्पताल।",
        f"गोव्याचे आरोग्य निर्देशक भारतातील सर्वोत्तमांपैकी आहेत. 2020 मध्ये अर्भक मृत्युदर दर 1,000 जिवंत जन्मांमागे {s[5]:.0f} होता (2010 मधील {s[4]} वरून कमी), राष्ट्रीय 28 पेक्षा खूपच कमी, जन्मदर दर 1,000 मागे {s[1]} — भारतातील सर्वांत कमींपैकी — व मृत्युदर {s[3]} होता. एनएफएचएस-5 मध्ये जवळपास सर्व प्रसूती ({n['institutional_N5']:.1f}%) आरोग्य संस्थांत झाल्या. बालपोषण ही कमकुवत बाजू आहे: पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी होती (एनएफएचएस-4 मधील {n['stunted'][0]}% वरून वाढ), {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची. मधुमेह व उच्च रक्तदाबासारखे जीवनशैलीचे आजार वाढती चिंता आहेत.\n\nबांबोळीचे गोवा वैद्यकीय महाविद्यालय हे मुख्य संदर्भ रुग्णालय आहे, सोबत म्हापसा (उत्तर गोवा) व मडगाव (दक्षिण गोवा) येथील जिल्हा रुग्णालये आणि पणजी, मडगाव व वास्कोतील खासगी रुग्णालये."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("GA"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"), "srs", "Goa is not in the SRS abridged life table for major States used here."),
        (L("Diabetes and hypertension prevalence (NFHS-5)", "मधुमेह और उच्च रक्तचाप की व्यापकता (एनएफ़एचएस-5)", "मधुमेह व उच्च रक्तदाबाचे प्रमाण (एनएफएचएस-5)"), "nfhs", "NFHS-5 State fact sheet."),
    ]),
])
print("ga mod2 ok")
