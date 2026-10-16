"""Chhattisgarh modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-CT"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
CAB = "https://www.newsonair.gov.in/chhattisgarh-cabinet-expanded-gajendra-yadav-rajesh-agrawal-and-guru-khushwant-saheb-sworn-in-as-ministers"
NOTE_CT = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 16 Oct 2026. "
           "FY2025-26 is the latest year published for Chhattisgarh and may be revised.")
mo = research("mospi_ct.json")
NAME = L("Chhattisgarh", "छत्तीसगढ़", "छत्तीसगड")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Chhattisgarh's culture blends the folk traditions of the plains with the rich tribal life of Bastar and Surguja. Pandavani, the sung and acted retelling of the Mahabharata with a tambura, was taken to the world by Teejan Bai. Nacha, the folk theatre of the plains, inspired Habib Tanvir's Naya Theatre, and dances include Panthi of the Satnami community, Raut Nacha of the cowherds at Diwali, Sua by women around a parrot figure, and Karma. In Bastar, Gond and Muria communities have their ghotul youth dormitories, Madai fairs and the long Bastar Dussehra.\n\nBastar's crafts — Dhokra bell-metal casting, wrought-iron figures and wood carving — are registered GIs, as is Champa's kosa (tussar) silk. Hindi writers Gajanan Madhav Muktibodh and Vinod Kumar Shukla are closely linked with the State, and Indira Kala Sangeet Vishwavidyalaya in Khairagarh is a pioneering university of music and fine arts.",
        "छत्तीसगढ़ की संस्कृति मैदानों की लोक परंपराओं को बस्तर और सरगुजा के समृद्ध जनजातीय जीवन से जोड़ती है। तंबूरे के साथ गाकर और अभिनय कर महाभारत सुनाने वाली पंडवानी को तीजन बाई ने विश्व तक पहुँचाया। मैदानों के लोक रंगमंच नाचा ने हबीब तनवीर के नया थिएटर को प्रेरित किया, और नृत्यों में सतनामी समुदाय का पंथी, दिवाली पर यादवों का राउत नाचा, तोते की आकृति के चारों ओर महिलाओं का सुआ, और करमा शामिल हैं। बस्तर में गोंड और मुरिया समुदायों के घोटुल युवागृह, मड़ई मेले और लंबा बस्तर दशहरा हैं।\n\nबस्तर के शिल्प — ढोकरा घंटा-धातु ढलाई, लोहे की आकृतियाँ और काष्ठ नक्काशी — पंजीकृत जीआई हैं, और चांपा का कोसा (तसर) रेशम भी। हिंदी लेखक गजानन माधव मुक्तिबोध और विनोद कुमार शुक्ल राज्य से गहराई से जुड़े हैं, और खैरागढ़ का इंदिरा कला संगीत विश्वविद्यालय संगीत और ललित कलाओं का अग्रणी विश्वविद्यालय है।",
        "छत्तीसगडची संस्कृती मैदानी लोकपरंपरांना बस्तर व सरगुजाच्या समृद्ध आदिवासी जीवनाशी जोडते. तंबोऱ्यासह गाऊन व अभिनय करून महाभारत सांगणारी पंडवानी तीजनबाईंनी जगभर पोहोचवली. मैदानी लोकरंगभूमी नाचाने हबीब तनवीर यांच्या नया थिएटरला प्रेरणा दिली, आणि नृत्यांत सतनामी समुदायाचे पंथी, दिवाळीत गवळ्यांचे राउत नाचा, पोपटाच्या प्रतिमेभोवती स्त्रियांचे सुआ व करमा यांचा समावेश आहे. बस्तरमध्ये गोंड व मुरिया समुदायांची घोटुल युवागृहे, मडई जत्रा व दीर्घ बस्तर दसरा आहे.\n\nबस्तरच्या हस्तकला — ढोकरा घंटाधातू ओतकाम, लोखंडी आकृत्या व लाकडी कोरीवकाम — नोंदणीकृत जीआय आहेत, तसेच चांपाचे कोसा (टसर) रेशीमही. हिंदी लेखक गजानन माधव मुक्तिबोध व विनोद कुमार शुक्ल राज्याशी जवळून जोडलेले आहेत, आणि खैरागडचे इंदिरा कला संगीत विश्वविद्यालय हे संगीत व ललित कलांचे अग्रणी विद्यापीठ आहे."),
        conf="Editorial"),
    lst("festivals", [
        fest("dussehra", "Bastar Dussehra", "बस्तर दशहरा", "बस्तर दसरा", ("About 75 days, July–October", "लगभग 75 दिन, जुलाई–अक्टूबर", "सुमारे 75 दिवस, जुलै–ऑक्टोबर"),
             ("Devoted to the goddess Danteshwari rather than Rama; a huge wooden chariot is pulled through Jagdalpur.", "राम के बजाय देवी दंतेश्वरी को समर्पित; जगदलपुर में विशाल लकड़ी का रथ खींचा जाता है।", "रामाऐवजी देवी दंतेश्वरीला समर्पित; जगदलपूरमध्ये प्रचंड लाकडी रथ ओढला जातो.")),
        fest("hareli", "Hareli", "हरेली", "हरेली", ("July–August (Shravan Amavasya)", "जुलाई–अगस्त (श्रावण अमावस्या)", "जुलै–ऑगस्ट (श्रावण अमावस्या)"),
             ("First festival of the farming year; farm tools are worshipped and children walk on stilts (gedi).", "कृषि वर्ष का पहला त्योहार; कृषि औज़ारों की पूजा होती है और बच्चे गेड़ी चढ़ते हैं।", "शेती वर्षाचा पहिला सण; शेतीच्या अवजारांची पूजा होते आणि मुले गेडीवर चालतात.")),
        fest("pola", "Pola and Teeja", "पोला और तीजा", "पोळा व तीजा", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Bullocks are honoured; married women return to their parents' homes for Teeja.", "बैलों का सम्मान; विवाहित महिलाएँ तीजा के लिए मायके लौटती हैं।", "बैलांचा सन्मान; विवाहित स्त्रिया तीजासाठी माहेरी परततात.")),
        fest("rajim", "Rajim Punni Mela", "राजिम पुन्नी मेला", "राजिम पुन्नी मेळा", ("February–March (Magh Purnima to Mahashivratri)", "फ़रवरी–मार्च (माघ पूर्णिमा से महाशिवरात्रि)", "फेब्रुवारी–मार्च (माघ पौर्णिमा ते महाशिवरात्री)"),
             ("Fair at the confluence of the Mahanadi, Pairi and Sondur.", "महानदी, पैरी और सोंढूर के संगम पर मेला।", "महानदी, पैरी व सोंढूरच्या संगमावर जत्रा.")),
        fest("cherchera", "Cherchera", "छेरछेरा", "छेरछेरा", ("December–January (Paush Purnima)", "दिसंबर–जनवरी (पौष पूर्णिमा)", "डिसेंबर–जानेवारी (पौष पौर्णिमा)"),
             ("Harvest festival; children collect new rice from house to house.", "फ़सल उत्सव; बच्चे घर-घर से नया धान इकट्ठा करते हैं।", "सुगीचा सण; मुले घरोघरी नवे धान्य गोळा करतात.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("pandavani", "Pandavani", "पंडवानी", "पंडवानी"), it3("panthi", "Panthi dance", "पंथी नृत्य", "पंथी नृत्य"),
        it3("raut", "Raut Nacha", "राउत नाचा", "राउत नाचा"), it3("nacha", "Nacha theatre", "नाचा रंगमंच", "नाचा रंगभूमी"),
        it3("dhokra", "Bastar Dhokra", "बस्तर ढोकरा", "बस्तर ढोकरा"), it3("iron", "Bastar wrought iron", "बस्तर लौह शिल्प", "बस्तर लोखंडी हस्तकला"),
        it3("kosa", "Kosa silk", "कोसा रेशम", "कोसा रेशीम"), it3("godna", "Godna art", "गोदना कला", "गोंदण कला"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("chila", "Chila and fara", "चीला और फरा", "चिला व फरा", d=("Rice-flour pancakes and steamed rice dumplings.", "चावल के आटे के चीले और भाप में पके चावल के फरे।", "तांदळाच्या पिठाचे चिले व वाफवलेले तांदळाचे फरे.")),
        it3("bore", "Bore basi", "बोरे बासी", "बोरे बासी", d=("Cooked rice soaked overnight in water, eaten with onion and chutney in summer.", "रात भर पानी में भिगोया भात, गर्मियों में प्याज़ और चटनी के साथ।", "रात्रभर पाण्यात भिजवलेला भात, उन्हाळ्यात कांदा व चटणीसह.")),
        it3("chapra", "Chapra (red-ant chutney)", "चापड़ा (लाल चींटी की चटनी)", "चापडा (लाल मुंग्यांची चटणी)", d=("Bastar's tangy chutney of red weaver ants and eggs.", "लाल बुनकर चींटियों और अंडों की बस्तर की खट्टी चटनी।", "लाल विणकर मुंग्या व अंड्यांची बस्तरची आंबट चटणी.")),
        it3("dubraj", "Dubraj and Jeeraphool rice", "दुबराज और जीराफूल चावल", "दुबराज व जीराफूल तांदूळ", d=("Aromatic rice varieties; both registered GIs.", "सुगंधित धान किस्में; दोनों पंजीकृत जीआई।", "सुगंधी तांदळाचे वाण; दोन्ही नोंदणीकृत जीआय.")),
        it3("thethri", "Thethri and khurmi", "ठेठरी और खुरमी", "ठेठरी व खुरमी", d=("Savoury and sweet fried snacks made for Teeja and festivals.", "तीजा और त्योहारों के लिए बनने वाले नमकीन और मीठे तले पकवान।", "तीजा व सणांसाठी बनवले जाणारे खारे व गोड तळलेले पदार्थ.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("lugra", "Lugra saree", "लुगरा साड़ी", "लुगरा साडी", d=("Cotton or kosa saree worn in the Chhattisgarhi style, often with silver jewellery.", "छत्तीसगढ़ी ढंग से पहनी जाने वाली सूती या कोसा साड़ी, अक्सर चाँदी के गहनों के साथ।", "छत्तीसगढी पद्धतीने नेसली जाणारी सुती किंवा कोसा साडी, अनेकदा चांदीच्या दागिन्यांसह.")),
        it3("dhoti", "Dhoti, kurta and pagri", "धोती, कुर्ता और पगड़ी", "धोतर, कुर्ता व पगडी", d=("Men's festive dress; Raut dancers wear colourful costumes with peacock feathers.", "पुरुषों की उत्सव पोशाक; राउत नर्तक मोर पंखों वाली रंगीन वेशभूषा पहनते हैं।", "पुरुषांचा सणासुदीचा पोशाख; राउत नर्तक मोरपिसांच्या रंगीत वेशभूषेत असतात.")),
        it3("tribal", "Bastar tribal ornaments", "बस्तर के जनजातीय आभूषण", "बस्तरचे आदिवासी दागिने", d=("Bead, brass and cowrie ornaments worn at festivals.", "त्योहारों में पहने जाने वाले मोती, पीतल और कौड़ी के आभूषण।", "सणांत घातले जाणारे मणी, पितळ व कवड्यांचे दागिने.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]; mine = 100 * g["mining"] / g["total"]
util = 100 * g["utilities"] / g["total"]; cons = 100 * g["construction"] / g["total"]
ur = AP["plfs_ur_15plus_psss"]["CT"]; lf = AP["plfs_lfpr_2025"]["CT"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Chhattisgarh's GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26 in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2025-26'][0])}. In FY2024-25 agriculture, livestock, forestry and fishing made up about {agri:.0f}% of GSVA, construction about {cons:.0f}%, manufacturing about {mfg:.0f}%, mining about {mine:.0f}% and electricity, gas and water about {util:.0f}% — a large share that reflects the coal-fired power stations of Korba, Raigarh and Bilaspur. The Bhilai Steel Plant, NMDC's Bailadila iron-ore mines, the coal mines of South Eastern Coalfields (headquartered at Bilaspur), BALCO's aluminium smelter at Korba, cement plants and sponge-iron units form the industrial base. Paddy dominates farming, with State procurement of rice a major support to farm incomes, and forest produce such as tendu leaves, sal seed and lac is important in tribal areas.\n\nLabour-force participation is high: in 2025, {lf['person']}% of people aged 15 and above and {lf['female']}% of women were in the labour force, well above the national {lfi['person']}% and {lfi['female']}%. The PLFS unemployment rate was {ur['2025']}%.",
        f"मोस्पी शृंखला में वित्त वर्ष 2025-26 में छत्तीसगढ़ का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2025-26'][0])}। वित्त वर्ष 2024-25 में कृषि, पशुपालन, वानिकी और मत्स्य पालन जीएसवीए का लगभग {agri:.0f}%, निर्माण लगभग {cons:.0f}%, विनिर्माण लगभग {mfg:.0f}%, खनन लगभग {mine:.0f}% और बिजली, गैस व जल लगभग {util:.0f}% थे — यह बड़ा हिस्सा कोरबा, रायगढ़ और बिलासपुर के कोयला-आधारित बिजलीघरों को दर्शाता है। भिलाई इस्पात संयंत्र, एनएमडीसी की बैलाडीला लौह अयस्क खदानें, साउथ ईस्टर्न कोलफ़ील्ड्स (मुख्यालय बिलासपुर) की कोयला खदानें, कोरबा में बाल्को का एल्युमिनियम स्मेल्टर, सीमेंट संयंत्र और स्पंज आयरन इकाइयाँ औद्योगिक आधार हैं। खेती में धान प्रमुख है, और राज्य द्वारा धान की ख़रीद कृषि आय का बड़ा सहारा है, जबकि जनजातीय क्षेत्रों में तेंदूपत्ता, साल बीज और लाख जैसी वनोपज महत्त्वपूर्ण है।\n\nश्रम बल भागीदारी ऊँची है: 2025 में 15 वर्ष से अधिक आयु के {lf['person']}% लोग और {lf['female']}% महिलाएँ श्रम बल में थीं, जो राष्ट्रीय {lfi['person']}% और {lfi['female']}% से काफ़ी अधिक है। पीएलएफ़एस बेरोज़गारी दर {ur['2025']}% थी।",
        f"मोस्पी मालिकेनुसार आ.व. 2025-26 मध्ये छत्तीसगडचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2025-26'][0])}. आ.व. 2024-25 मध्ये शेती, पशुपालन, वनीकरण व मत्स्यव्यवसाय जीएसव्हीएच्या सुमारे {agri:.0f}%, बांधकाम सुमारे {cons:.0f}%, उत्पादन उद्योग सुमारे {mfg:.0f}%, खाणकाम सुमारे {mine:.0f}% आणि वीज, वायू व पाणी सुमारे {util:.0f}% होते — हा मोठा वाटा कोरबा, रायगड व बिलासपूरच्या कोळसाआधारित वीजकेंद्रांचे प्रतिबिंब आहे. भिलाई पोलाद कारखाना, एनएमडीसीच्या बैलाडिला लोहखनिज खाणी, साउथ ईस्टर्न कोलफिल्ड्सच्या (मुख्यालय बिलासपूर) कोळसा खाणी, कोरब्यातील बाल्कोचा ॲल्युमिनियम स्मेल्टर, सिमेंट कारखाने व स्पंज आयर्न उद्योग हा औद्योगिक पाया आहे. शेतीत भात प्रमुख असून राज्याकडून होणारी धानखरेदी शेती उत्पन्नाचा मोठा आधार आहे, तर आदिवासी भागांत तेंदूपत्ता, साल बी व लाख यांसारखे वनोपज महत्त्वाचे आहे.\n\nश्रमशक्ती सहभाग जास्त आहे: 2025 मध्ये 15 वर्षांवरील {lf['person']}% लोक व {lf['female']}% स्त्रिया श्रमशक्तीत होत्या, राष्ट्रीय {lfi['person']}% व {lfi['female']}% पेक्षा बरेच अधिक. पीएलएफएस बेरोजगारी दर {ur['2025']}% होता."),
        sources=["mospi", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_CT), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_CT), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_CT), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("CT", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    plfs_series("CT", NAME),
    lst("sectors-key", [
        it3("steel", "Steel and sponge iron", "इस्पात और स्पंज आयरन", "पोलाद व स्पंज आयर्न", d=("Bhilai Steel Plant; Nagarnar; sponge-iron units around Raipur and Raigarh.", "भिलाई इस्पात संयंत्र; नगरनार; रायपुर और रायगढ़ के आसपास स्पंज आयरन इकाइयाँ।", "भिलाई पोलाद कारखाना; नगरनार; रायपूर व रायगडभोवती स्पंज आयर्न उद्योग.")),
        it3("coal", "Coal and power", "कोयला और बिजली", "कोळसा व वीज", d=("Korba, Raigarh and Mand–Raigarh coalfields; large thermal stations.", "कोरबा, रायगढ़ और मांड–रायगढ़ कोयला क्षेत्र; बड़े तापीय केंद्र।", "कोरबा, रायगड व मांड–रायगड कोळसा क्षेत्रे; मोठी औष्णिक केंद्रे.")),
        it3("iron", "Iron ore", "लौह अयस्क", "लोहखनिज", d=("Bailadila range in Dantewada; Dalli Rajhara.", "दंतेवाड़ा में बैलाडीला श्रेणी; दल्ली राजहरा।", "दंतेवाड्यातील बैलाडिला रांग; दल्ली राजहरा.")),
        it3("aluminium", "Aluminium and cement", "एल्युमिनियम और सीमेंट", "ॲल्युमिनियम व सिमेंट", d=("BALCO at Korba; cement belt around Raipur and Baloda Bazar.", "कोरबा में बाल्को; रायपुर और बलौदाबाज़ार के आसपास सीमेंट पट्टी।", "कोरब्यात बाल्को; रायपूर व बलौदाबाजारभोवती सिमेंट पट्टा.")),
        it3("paddy", "Paddy", "धान", "भात", d=("Main crop of the plains; State procurement.", "मैदानों की मुख्य फ़सल; राज्य द्वारा ख़रीद।", "मैदानांचे मुख्य पीक; राज्याकडून खरेदी.")),
        it3("forest", "Forest produce", "वनोपज", "वनोपज", d=("Tendu leaves, sal seed, lac, mahua and tamarind.", "तेंदूपत्ता, साल बीज, लाख, महुआ और इमली।", "तेंदूपत्ता, साल बी, लाख, मोह व चिंच.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Paddy procurement by season", "मौसमवार धान ख़रीद", "हंगामनिहाय धानखरेदी"), "india-gov", "Chhattisgarh Food Department / FCI."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("Mineral production and royalty", "खनिज उत्पादन और रॉयल्टी", "खनिज उत्पादन व स्वामित्वधन"), "india-gov", "Indian Bureau of Mines."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Chhattisgarh has a unicameral legislature, the 90-member Legislative Assembly at Raipur. The State elects 11 members to the Lok Sabha and 5 to the Rajya Sabha. Much of the north and south are Fifth Schedule areas with special protections for Scheduled Tribes.\n\nThe BJP won the Assembly election of November 2023, and Vishnu Deo Sai, a tribal leader from Jashpur district, was sworn in as Chief Minister on 13 December 2023, with Arun Sao and Vijay Sharma as Deputy Chief Ministers. Former Chief Minister Raman Singh is Speaker, and Ramen Deka has been Governor since July 2024.",
        "छत्तीसगढ़ में एकसदनीय विधानमंडल है, रायपुर में 90 सदस्यों वाली विधानसभा। राज्य से लोकसभा के 11 और राज्यसभा के 5 सदस्य चुने जाते हैं। उत्तर और दक्षिण का अधिकांश भाग पाँचवीं अनुसूची का क्षेत्र है, जहाँ अनुसूचित जनजातियों को विशेष संरक्षण है।\n\nनवंबर 2023 का विधानसभा चुनाव भाजपा ने जीता, और जशपुर ज़िले के जनजातीय नेता विष्णु देव साय ने 13 दिसंबर 2023 को मुख्यमंत्री पद की शपथ ली, अरुण साव और विजय शर्मा उपमुख्यमंत्री बने। पूर्व मुख्यमंत्री रमन सिंह अध्यक्ष हैं, और रमेन डेका जुलाई 2024 से राज्यपाल हैं।",
        "छत्तीसगडमध्ये एकसदनी विधिमंडळ आहे, रायपूरमधील 90 सदस्यांची विधानसभा. राज्यातून लोकसभेवर 11 व राज्यसभेवर 5 सदस्य निवडले जातात. उत्तर व दक्षिणेचा बहुतांश भाग पाचव्या अनुसूचीतील क्षेत्र आहे, जिथे अनुसूचित जमातींना विशेष संरक्षण आहे.\n\nनोव्हेंबर 2023 ची विधानसभा निवडणूक भाजपने जिंकली, आणि जशपूर जिल्ह्यातील आदिवासी नेते विष्णुदेव साय यांनी 13 डिसेंबर 2023 रोजी मुख्यमंत्रिपदाची शपथ घेतली, अरुण साव व विजय शर्मा उपमुख्यमंत्री झाले. माजी मुख्यमंत्री रमण सिंह अध्यक्ष आहेत, आणि रमेन डेका जुलै 2024 पासून राज्यपाल आहेत."),
        sources=["deccan-herald", "newsonair", "thestatesman"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("noa", "News On AIR: Chhattisgarh cabinet expanded (20 Aug 2025)", "न्यूज़ ऑन एआईआर: छत्तीसगढ़ मंत्रिमंडल विस्तार (20 अगस्त 2025)", "न्यूज ऑन एआयआर: छत्तीसगड मंत्रिमंडळ विस्तार (20 ऑगस्ट 2025)", url=CAB, src="newsonair"),
        it3("portal", "Government of Chhattisgarh", "छत्तीसगढ़ सरकार", "छत्तीसगड शासन", url="https://cgstate.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2023 Assembly election — party-wise result", "2023 विधानसभा चुनाव — दलवार परिणाम", "2023 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Chhattisgarh 2023."),
        (L("Leader of Opposition — official notice", "नेता प्रतिपक्ष — आधिकारिक सूचना", "विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "Assembly secretariat."),
        (L("Chief Minister's swearing-in — official source", "मुख्यमंत्री का शपथ ग्रहण — आधिकारिक स्रोत", "मुख्यमंत्र्यांचा शपथविधी — अधिकृत स्रोत"), "india-gov", "Replace the PTI copy with a Raj Bhavan or State release."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "On 3 October 2023 the Prime Minister dedicated NMDC's new steel plant at Nagarnar in Bastar and the Antagarh–Taroki section of the new rail line into north Bastar. The Raipur–Visakhapatnam economic corridor, new rail lines to Rowghat and Jagdalpur, and power and mining projects are other large works. Each card shows its source and the date it was checked.",
        "3 अक्टूबर 2023 को प्रधानमंत्री ने बस्तर के नगरनार में एनएमडीसी का नया इस्पात संयंत्र और उत्तर बस्तर में नई रेल लाइन का अंतागढ़–तारोकी खंड राष्ट्र को समर्पित किया। रायपुर–विशाखापत्तनम आर्थिक गलियारा, रावघाट और जगदलपुर तक नई रेल लाइनें, और बिजली व खनन परियोजनाएँ अन्य बड़े कार्य हैं। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "3 ऑक्टोबर 2023 रोजी पंतप्रधानांनी बस्तरमधील नगरनार येथील एनएमडीसीचा नवा पोलाद कारखाना आणि उत्तर बस्तरमधील नव्या रेल्वेमार्गाचा अंतागड–तारोकी टप्पा राष्ट्राला समर्पित केला. रायपूर–विशाखापट्टणम आर्थिक मार्गिका, रावघाट व जगदलपूरपर्यंत नवे रेल्वेमार्ग आणि वीज व खाण प्रकल्प ही इतर मोठी कामे आहेत. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["newsonair"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Raipur–Visakhapatnam economic corridor — status", "रायपुर–विशाखापत्तनम आर्थिक गलियारा — स्थिति", "रायपूर–विशाखापट्टणम आर्थिक मार्गिका — स्थिती"), "nhai", "NHAI project status."),
        (L("Rowghat–Jagdalpur rail line — status", "रावघाट–जगदलपुर रेल लाइन — स्थिति", "रावघाट–जगदलपूर रेल्वेमार्ग — स्थिती"), "railways", "Ministry of Railways."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Swami Vivekananda Airport at Raipur is the State's main airport; Bilaspur, Jagdalpur and Ambikapur have smaller airports with regional flights. The South East Central Railway is headquartered at Bilaspur, and the Howrah–Mumbai main line crosses the State through Bilaspur, Raipur and Durg; mineral lines run to Korba, Raigarh, Dalli Rajhara and the Bailadila mines, from where iron ore is carried by rail to Visakhapatnam. National highways link Raipur with Nagpur, Sambalpur, Bilaspur and Jagdalpur.",
        "रायपुर का स्वामी विवेकानंद हवाई अड्डा राज्य का मुख्य हवाई अड्डा है; बिलासपुर, जगदलपुर और अंबिकापुर में क्षेत्रीय उड़ानों वाले छोटे हवाई अड्डे हैं। दक्षिण पूर्व मध्य रेलवे का मुख्यालय बिलासपुर में है, और हावड़ा–मुंबई मुख्य लाइन बिलासपुर, रायपुर और दुर्ग से होकर राज्य को पार करती है; खनिज लाइनें कोरबा, रायगढ़, दल्ली राजहरा और बैलाडीला खदानों तक जाती हैं, जहाँ से लौह अयस्क रेल से विशाखापत्तनम जाता है। राष्ट्रीय राजमार्ग रायपुर को नागपुर, संबलपुर, बिलासपुर और जगदलपुर से जोड़ते हैं।",
        "रायपूरचे स्वामी विवेकानंद विमानतळ हे राज्याचे मुख्य विमानतळ आहे; बिलासपूर, जगदलपूर व अंबिकापूर येथे प्रादेशिक उड्डाणांचे लहान विमानतळ आहेत. दक्षिण पूर्व मध्य रेल्वेचे मुख्यालय बिलासपूरमध्ये आहे, आणि हावडा–मुंबई मुख्य मार्ग बिलासपूर, रायपूर व दुर्गमार्गे राज्य ओलांडतो; खनिज मार्ग कोरबा, रायगड, दल्ली राजहरा व बैलाडिला खाणींपर्यंत जातात, जिथून लोहखनिज रेल्वेने विशाखापट्टणमला नेले जाते. राष्ट्रीय महामार्ग रायपूरला नागपूर, संबलपूर, बिलासपूर व जगदलपूरशी जोडतात."),
        conf="Editorial"),
    lst("airports", [
        it3("rpr", "Swami Vivekananda Airport, Raipur", "स्वामी विवेकानंद हवाई अड्डा, रायपुर", "स्वामी विवेकानंद विमानतळ, रायपूर", m=("RPR", "RPR", "RPR")),
        it3("pab", "Bilasa Devi Kevat Airport, Bilaspur", "बिलासा देवी केवट हवाई अड्डा, बिलासपुर", "बिलासा देवी केवट विमानतळ, बिलासपूर", m=("PAB", "PAB", "PAB")),
        it3("jgb", "Jagdalpur", "जगदलपुर", "जगदलपूर", m=("JGB", "JGB", "JGB")),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Chhattisgarh is one of India's major power producers. Korba, the 'power capital', has NTPC's super thermal power station and State plants side by side with the coal mines that feed them, and NTPC's Sipat and Lara stations and many private plants around Raigarh and Janjgir–Champa add to the output. Much of the power is sent to other States. Hydro-electric power comes mainly from the Hasdeo Bango (Minimata) dam, and solar capacity is growing.",
        "छत्तीसगढ़ भारत के प्रमुख बिजली उत्पादकों में से है। 'ऊर्जा राजधानी' कोरबा में एनटीपीसी का सुपर तापीय बिजलीघर और राज्य के संयंत्र उन्हें ईंधन देने वाली कोयला खदानों के साथ-साथ हैं, और एनटीपीसी के सीपत व लारा केंद्र तथा रायगढ़ और जांजगीर–चांपा के आसपास कई निजी संयंत्र उत्पादन बढ़ाते हैं। बिजली का बड़ा भाग दूसरे राज्यों को भेजा जाता है। जलविद्युत मुख्यतः हसदेव बांगो (मिनीमाता) बाँध से आती है, और सौर क्षमता बढ़ रही है।",
        "छत्तीसगड हे भारतातील प्रमुख वीज उत्पादकांपैकी एक आहे. 'ऊर्जा राजधानी' कोरब्यात एनटीपीसीचे सुपर औष्णिक वीजकेंद्र व राज्याचे प्रकल्प त्यांना कोळसा पुरवणाऱ्या खाणींच्या शेजारीच आहेत, आणि एनटीपीसीची सीपत व लारा केंद्रे आणि रायगड व जांजगीर–चांपाभोवतीचे अनेक खासगी प्रकल्प उत्पादनात भर घालतात. विजेचा मोठा भाग इतर राज्यांना पाठवला जातो. जलविद्युत मुख्यतः हसदेव बांगो (मिनीमाता) धरणातून येते, आणि सौरक्षमता वाढत आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Chhattisgarh's technology sector is small and concentrated in Raipur and Nava Raipur, where the State has planned IT and electronics zones. Public services such as land records, ration cards and paddy procurement payments are handled online, and mobile and banking networks have been extended into the forested south, though connectivity in remote Bastar remains patchy.",
        "छत्तीसगढ़ का प्रौद्योगिकी क्षेत्र छोटा है और रायपुर व नवा रायपुर में केंद्रित है, जहाँ राज्य ने आईटी और इलेक्ट्रॉनिक्स क्षेत्र नियोजित किए हैं। भूमि अभिलेख, राशन कार्ड और धान ख़रीद भुगतान जैसी सार्वजनिक सेवाएँ ऑनलाइन चलती हैं, और मोबाइल व बैंकिंग नेटवर्क वनाच्छादित दक्षिण तक पहुँचाए गए हैं, हालाँकि दूरस्थ बस्तर में कनेक्टिविटी अब भी अधूरी है।",
        "छत्तीसगडचे तंत्रज्ञान क्षेत्र लहान असून रायपूर व नवा रायपूरमध्ये केंद्रित आहे, जिथे राज्याने आयटी व इलेक्ट्रॉनिक्स क्षेत्रे नियोजित केली आहेत. जमिनीच्या नोंदी, शिधापत्रिका व धानखरेदीचे पैसे यांसारख्या सार्वजनिक सेवा ऑनलाइन चालतात, आणि मोबाइल व बँकिंग जाळे वनाच्छादित दक्षिणेपर्यंत पोहोचवले आहे, तरी दुर्गम बस्तरमध्ये जोडणी अजूनही अपुरी आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Madhya Pradesh circle, which includes Chhattisgarh)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("CT", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["CT"]
module(R, "education", [
    prose("p1", L(
        f"Chhattisgarh's higher-education gross enrolment ratio (ages 18–23) was 19.6% in 2021-22 in AISHE, up from 17.7% in 2017-18 but well below the national 28.4%. Notably, women's GER ({gf}%) was clearly higher than men's ({gm}%). The State had 34 universities and 917 colleges. Literacy at the 2011 Census was 70.3%.\n\nPt. Ravishankar Shukla University in Raipur (1964) is the oldest general university, and Guru Ghasidas Vishwavidyalaya in Bilaspur is a central university. National institutes include IIT Bhilai, IIM Raipur, NIT Raipur, AIIMS Raipur and Hidayatullah National Law University. Indira Gandhi Krishi Vishwavidyalaya is the State farm university, and Indira Kala Sangeet Vishwavidyalaya in Khairagarh (1956) teaches music, dance and fine arts.",
        f"एआईएसएचई के अनुसार 2021-22 में छत्तीसगढ़ का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) 19.6% था, जो 2017-18 के 17.7% से अधिक लेकिन राष्ट्रीय 28.4% से काफ़ी कम है। उल्लेखनीय है कि महिलाओं का जीईआर ({gf}%) पुरुषों ({gm}%) से स्पष्ट रूप से अधिक था। राज्य में 34 विश्वविद्यालय और 917 कॉलेज थे। 2011 की जनगणना में साक्षरता 70.3% थी।\n\nरायपुर का पं. रविशंकर शुक्ल विश्वविद्यालय (1964) सबसे पुराना सामान्य विश्वविद्यालय है, और बिलासपुर का गुरु घासीदास विश्वविद्यालय केंद्रीय विश्वविद्यालय है। राष्ट्रीय संस्थानों में आईआईटी भिलाई, आईआईएम रायपुर, एनआईटी रायपुर, एम्स रायपुर और हिदायतुल्लाह राष्ट्रीय विधि विश्वविद्यालय शामिल हैं। इंदिरा गांधी कृषि विश्वविद्यालय राज्य का कृषि विश्वविद्यालय है, और खैरागढ़ का इंदिरा कला संगीत विश्वविद्यालय (1956) संगीत, नृत्य और ललित कलाएँ सिखाता है।",
        f"एआयएसएचईनुसार 2021-22 मध्ये छत्तीसगडचे उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) 19.6% होते, 2017-18 मधील 17.7% पेक्षा अधिक पण राष्ट्रीय 28.4% पेक्षा बरेच कमी. विशेष म्हणजे स्त्रियांचे जीईआर ({gf}%) पुरुषांपेक्षा ({gm}%) स्पष्टपणे अधिक होते. राज्यात 34 विद्यापीठे व 917 महाविद्यालये होती. 2011 च्या जनगणनेत साक्षरता 70.3% होती.\n\nरायपूरचे पं. रविशंकर शुक्ल विद्यापीठ (1964) हे सर्वांत जुने सर्वसाधारण विद्यापीठ आहे, आणि बिलासपूरचे गुरु घासीदास विश्वविद्यालय केंद्रीय विद्यापीठ आहे. राष्ट्रीय संस्थांत आयआयटी भिलाई, आयआयएम रायपूर, एनआयटी रायपूर, एम्स रायपूर व हिदायतुल्ला राष्ट्रीय विधी विद्यापीठ यांचा समावेश आहे. इंदिरा गांधी कृषी विश्वविद्यालय हे राज्याचे कृषी विद्यापीठ आहे, आणि खैरागडचे इंदिरा कला संगीत विश्वविद्यालय (1956) संगीत, नृत्य व ललित कला शिकवते."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("prsu", "Pt. Ravishankar Shukla University", "पं. रविशंकर शुक्ल विश्वविद्यालय", "पं. रविशंकर शुक्ल विद्यापीठ", m=("Raipur, 1964", "रायपुर, 1964", "रायपूर, 1964")),
        it3("ggv", "Guru Ghasidas Vishwavidyalaya", "गुरु घासीदास विश्वविद्यालय", "गुरु घासीदास विश्वविद्यालय", m=("Bilaspur; central university", "बिलासपुर; केंद्रीय विश्वविद्यालय", "बिलासपूर; केंद्रीय विद्यापीठ")),
        it3("iitbh", "IIT Bhilai", "आईआईटी भिलाई", "आयआयटी भिलाई", m=("Durg", "दुर्ग", "दुर्ग")),
        it3("iimr", "IIM Raipur", "आईआईएम रायपुर", "आयआयएम रायपूर", m=("Nava Raipur", "नवा रायपुर", "नवा रायपूर")),
        it3("nitr", "NIT Raipur", "एनआईटी रायपुर", "एनआयटी रायपूर", m=("Raipur", "रायपुर", "रायपूर")),
        it3("aiims", "AIIMS Raipur", "एम्स रायपुर", "एम्स रायपूर", m=("Raipur", "रायपुर", "रायपूर")),
        it3("iksv", "Indira Kala Sangeet Vishwavidyalaya", "इंदिरा कला संगीत विश्वविद्यालय", "इंदिरा कला संगीत विश्वविद्यालय", m=("Khairagarh, 1956", "खैरागढ़, 1956", "खैरागड, 1956")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Literacy by sex (Census 2011)", "लिंग के अनुसार साक्षरता (जनगणना 2011)", "लिंगनिहाय साक्षरता (जनगणना 2011)"), "census", "Primary Census Abstract."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["CT"]
module(R, "health", [
    prose("p1", L(
        f"Chhattisgarh's infant mortality rate fell from 51 per 1,000 live births in 2010 to 38 in 2020, but remained among the higher rates in India and above the national 28. The birth rate was 22.0 per 1,000 in 2020 and the death rate 7.9. In NFHS-5, {n['stunted'][1]:.1f}% of children under five were stunted, {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight — all lower than in NFHS-4 — and {n['institutional_N5']:.1f}% of births took place in health facilities, below the national 88.6%. Malaria, sickle-cell disease and anaemia are particular concerns in tribal areas, and the State's network of mitanin community health workers became a model for India's ASHA programme.\n\nAIIMS Raipur and the Dr B. R. Ambedkar Memorial Hospital with Pt. J. N. M. Medical College in Raipur are the main referral centres.",
        f"छत्तीसगढ़ की शिशु मृत्यु दर 2010 में प्रति 1,000 जीवित जन्म पर 51 से घटकर 2020 में 38 हो गई, लेकिन भारत की ऊँची दरों में और राष्ट्रीय 28 से ऊपर रही। 2020 में जन्म दर प्रति 1,000 पर 22.0 और मृत्यु दर 7.9 थी। एनएफ़एचएस-5 में पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने, {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के थे — सभी एनएफ़एचएस-4 से कम — और {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, जो राष्ट्रीय 88.6% से कम है। जनजातीय क्षेत्रों में मलेरिया, सिकल-सेल रोग और एनीमिया विशेष चिंताएँ हैं, और राज्य का मितानिन सामुदायिक स्वास्थ्य कार्यकर्ता नेटवर्क भारत के आशा कार्यक्रम का आदर्श बना।\n\nएम्स रायपुर और रायपुर का डॉ. भीमराव आंबेडकर स्मृति चिकित्सालय व पं. जवाहरलाल नेहरू स्मृति चिकित्सा महाविद्यालय मुख्य रेफ़रल केंद्र हैं।",
        f"छत्तीसगडचा अर्भक मृत्युदर 2010 मध्ये दर 1,000 जिवंत जन्मांमागे 51 वरून 2020 मध्ये 38 वर आला, पण तो भारतातील अधिक दरांपैकी व राष्ट्रीय 28 पेक्षा अधिक राहिला. 2020 मध्ये जन्मदर दर 1,000 मागे 22.0 व मृत्युदर 7.9 होता. एनएफएचएस-5 मध्ये पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी, {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची होती — सर्व एनएफएचएस-4 पेक्षा कमी — आणि {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, राष्ट्रीय 88.6% पेक्षा कमी. आदिवासी भागांत हिवताप, सिकलसेल आजार व रक्तक्षय या विशेष चिंता आहेत, आणि राज्याचे मितानिन सामुदायिक आरोग्य कार्यकर्त्यांचे जाळे भारताच्या आशा कार्यक्रमाचा आदर्श ठरले.\n\nएम्स रायपूर आणि रायपूरचे डॉ. भीमराव आंबेडकर स्मृती रुग्णालय व पं. जवाहरलाल नेहरू स्मृती वैद्यकीय महाविद्यालय ही मुख्य संदर्भ केंद्रे आहेत."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(38, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(51, "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(22.0, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020 (death rate 7.9); 25.3 in 2010."), "number",
             previous=dp(25.3, "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("dr", L("Death rate", "मृत्यु दर", "मृत्युदर"), dp(7.9, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020."), "number", "lower-is-better",
             previous=dp(8.0, "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(6.0, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("CT"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"), "srs", "SRS abridged life tables; Chhattisgarh is not listed separately in Economic Survey Table 8.1."),
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin; Chhattisgarh is reported within a combined group."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("ct mod2 ok")
