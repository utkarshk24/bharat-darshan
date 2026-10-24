"""Haryana modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-HR"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
CAG_HR = "https://cag.gov.in/uploads/download_audit_report/2026/Chapter-1-Overview-of-Finances-of-the-State-06a97fa816bb794.11409406.pdf"
FRBM_HR = "https://cms.neva.gov.in/NeVA/HR/FileStructure/PaperLaid/14/18/14_18_O_1413_V1.pdf"
NAME = L("Haryana", "हरियाणा", "हरियाणा")
hr = read("regions/IN-HR.json")["metrics"]
C = research("census_b5plus.json")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Haryana's culture is rooted in its villages. Saang (swang), the open-air folk theatre of song and dialogue, was made famous by Pandit Lakhmi Chand, the 'Kalidas of Haryana', and ragini singing remains popular at fairs and weddings. Folk dances include the phag, danced by women and men at Holi after the harvest, the loor of the Bangar women, and the dhamal of Mahendragarh and Gurugram. The State also has a classical connection: the Mewati gharana singer Pandit Jasraj was born in Haryana. Phulkari embroidery, a registered GI shared with Punjab and Rajasthan, is still made in villages, and the Surajkund International Crafts Mela near Faridabad has showcased Indian and foreign crafts every February since 1987.",
        "हरियाणा की संस्कृति उसके गाँवों में रची-बसी है। गीत और संवाद का खुला लोकनाट्य सांग (स्वांग) 'हरियाणा के कालिदास' पंडित लखमीचंद ने प्रसिद्ध किया, और रागिनी गायन आज भी मेलों और शादियों में लोकप्रिय है। लोकनृत्यों में फ़सल के बाद होली पर स्त्री-पुरुषों का फाग, बांगर की महिलाओं का लूर और महेंद्रगढ़ व गुरुग्राम का धमाल शामिल हैं। राज्य का शास्त्रीय संगीत से भी नाता है: मेवाती घराने के गायक पंडित जसराज का जन्म हरियाणा में हुआ। हरियाणा, पंजाब और राजस्थान का साझा पंजीकृत जीआई फुलकारी कढ़ाई आज भी गाँवों में बनती है, और फ़रीदाबाद के पास सूरजकुंड अंतरराष्ट्रीय शिल्प मेला 1987 से हर फ़रवरी भारतीय और विदेशी शिल्प प्रदर्शित करता है।",
        "हरियाणाची संस्कृती त्याच्या गावांत रुजलेली आहे. गाणे व संवादाचे खुले लोकनाट्य सांग (स्वांग) 'हरियाणाचे कालिदास' पंडित लखमीचंद यांनी प्रसिद्ध केले, आणि रागिणी गायन आजही जत्रा व लग्नांत लोकप्रिय आहे. लोकनृत्यांत सुगीनंतर होळीला स्त्री-पुरुषांचे फाग, बांगरच्या स्त्रियांचे लूर आणि महेंद्रगड व गुरुग्रामचे धमाल यांचा समावेश आहे. राज्याचा शास्त्रीय संगीताशीही संबंध आहे: मेवाती घराण्याचे गायक पंडित जसराज यांचा जन्म हरियाणात झाला. हरियाणा, पंजाब व राजस्थानचे सामायिक नोंदणीकृत जीआय फुलकारी भरतकाम आजही गावांत होते, आणि फरिदाबादजवळील सूरजकुंड आंतरराष्ट्रीय हस्तकला मेळा 1987 पासून दर फेब्रुवारीत भारतीय व परदेशी हस्तकला मांडतो."),
        conf="Editorial"),
    lst("festivals", [
        fest("teej", "Haryali Teej", "हरियाली तीज", "हरियाली तीज", ("July–August (Sawan)", "जुलाई–अगस्त (सावन)", "जुलै–ऑगस्ट (श्रावण)"),
             ("Monsoon festival of women, with swings, songs and ghevar.", "महिलाओं का मानसून उत्सव, झूलों, गीतों और घेवर के साथ।", "स्त्रियांचा पावसाळी सण, झोके, गाणी व घेवरसह.")),
        fest("gita", "International Gita Mahotsav", "अंतरराष्ट्रीय गीता महोत्सव", "आंतरराष्ट्रीय गीता महोत्सव", ("November–December", "नवंबर–दिसंबर", "नोव्हेंबर–डिसेंबर"),
             ("Celebrated at Kurukshetra around Gita Jayanti, with aarti at Brahma Sarovar.", "गीता जयंती के आसपास कुरुक्षेत्र में, ब्रह्म सरोवर पर आरती के साथ।", "गीता जयंतीच्या सुमारास कुरुक्षेत्र येथे, ब्रह्म सरोवरावरील आरतीसह.")),
        fest("surajkund", "Surajkund Crafts Mela", "सूरजकुंड शिल्प मेला", "सूरजकुंड हस्तकला मेळा", ("February", "फ़रवरी", "फेब्रुवारी"),
             ("International crafts fair near Faridabad.", "फ़रीदाबाद के पास अंतरराष्ट्रीय शिल्प मेला।", "फरिदाबादजवळील आंतरराष्ट्रीय हस्तकला मेळा.")),
        fest("baisakhi", "Baisakhi", "बैसाखी", "बैसाखी", ("13–14 April", "13–14 अप्रैल", "13–14 एप्रिल"),
             ("Harvest festival; fairs at Pinjore and village melas.", "फ़सल उत्सव; पिंजौर और गाँवों में मेले।", "सुगीचा सण; पिंजोर व गावांत जत्रा.")),
        fest("gugga", "Gugga Naumi", "गुग्गा नौमी", "गुग्गा नवमी", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Folk festival of Gugga Pir, with processions and fairs.", "गुग्गा पीर का लोक उत्सव, शोभायात्राओं और मेलों के साथ।", "गुग्गा पीराचा लोकसण, मिरवणुका व जत्रांसह.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("saang", "Saang (folk theatre)", "सांग (लोकनाट्य)", "सांग (लोकनाट्य)"), it3("ragini", "Ragini", "रागिनी", "रागिणी"),
        it3("phag", "Phag dance", "फाग नृत्य", "फाग नृत्य"), it3("loor", "Loor dance", "लूर नृत्य", "लूर नृत्य"),
        it3("phulkari", "Phulkari", "फुलकारी", "फुलकारी"), it3("durrie", "Panja durrie weaving", "पंजा दरी बुनाई", "पंजा दरी विणकाम"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("bajra", "Bajra roti and kadhi", "बाजरे की रोटी और कढ़ी", "बाजरीची भाकरी व कढी", d=("Millet bread with yoghurt curry, often with white butter and jaggery.", "दही की कढ़ी के साथ बाजरे की रोटी, अक्सर सफ़ेद मक्खन और गुड़ के साथ।", "दह्याच्या कढीसह बाजरीची भाकरी, अनेकदा पांढरे लोणी व गुळासह.")),
        it3("kachri", "Kachri ki sabzi", "कचरी की सब्ज़ी", "कचरीची भाजी", d=("Wild desert melon cooked as a tangy vegetable in the south-west.", "दक्षिण-पश्चिम में खट्टी सब्ज़ी के रूप में पकाई जाने वाली जंगली कचरी।", "नैर्ऋत्येत आंबट भाजी म्हणून शिजवली जाणारी रानटी कचरी.")),
        it3("paratha", "Murthal parathas", "मुरथल के पराठे", "मुरथलचे पराठे", d=("Stuffed parathas with white butter at the highway dhabas.", "राजमार्ग के ढाबों पर सफ़ेद मक्खन के साथ भरवाँ पराठे।", "महामार्गावरील ढाब्यांवर पांढऱ्या लोण्यासह भरलेले पराठे.")),
        it3("lassi", "Lassi and chhach", "लस्सी और छाछ", "लस्सी व ताक", d=("Churned curd drinks at every meal.", "हर भोजन के साथ मथी दही के पेय।", "प्रत्येक जेवणासोबत घुसळलेल्या दह्याची पेये.")),
        it3("churma", "Churma", "चूरमा", "चुरमा", d=("Crushed wheat bread with ghee and sugar.", "घी और चीनी के साथ चूरी गई रोटी।", "तूप व साखरेसह कुस्करलेली पोळी.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("daaman", "Daaman, kurti and chunder", "दामण, कुर्ती और चूंदड़", "दामण, कुर्ती व चुंदडी", d=("Women's traditional ankle-length skirt, blouse and long veil.", "महिलाओं का पारंपरिक टखनों तक का घाघरा, कुर्ती और लंबी ओढ़नी।", "स्त्रियांचा पारंपरिक घोट्यापर्यंतचा घागरा, कुर्ती व लांब ओढणी.")),
        it3("kurta", "Kurta, dhoti and pagdi", "कुर्ता, धोती और पगड़ी", "कुर्ता, धोतर व पगडी", d=("Men's village dress, often in white.", "पुरुषों की ग्रामीण पोशाक, प्रायः सफ़ेद।", "पुरुषांचा ग्रामीण पोशाख, बहुधा पांढरा.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
CAG_SERIES = [("FY2020-21", 730442), ("FY2021-22", 877269), ("FY2022-23", 974732), ("FY2023-24", 1085510), ("FY2024-25", 1213951)]
ur = AP["plfs_ur_15plus_psss"]["HR"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["HR"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Haryana's GSDP at current prices was ₹12,13,951 crore in FY2024-25, 11.8% higher than a year earlier, according to the Comptroller and Auditor General's State Finances Audit Report; it was about 3.7% of India's GDP. The State Finance Department put per capita income at ₹3,25,759 in FY2023-24. At constant prices, services made up about 51% of GSVA in FY2023-24, industry 33% and agriculture and allied sectors 16%.\n\nGurugram is a hub for corporate offices, IT and financial services, and the Gurugram–Manesar–Faridabad belt makes a large share of India's cars, two-wheelers and components. Panipat is known for textiles and handloom furnishings and has an oil refinery; Yamunanagar for plywood; Ambala for scientific instruments; and Sonipat and Bahadurgarh for footwear and light industry. Farming — wheat, basmati and other rice, mustard, cotton, bajra and sugarcane — and dairying with Murrah buffaloes remain central to rural incomes. The PLFS unemployment rate was {ur['2025']}% in 2025 (India {ui['2025']}%), and only {lf['female']}% of women aged 15 and above were in the labour force, against {lfi['female']}% nationally.",
        f"नियंत्रक एवं महालेखापरीक्षक की राज्य वित्त लेखापरीक्षा रिपोर्ट के अनुसार वित्त वर्ष 2024-25 में हरियाणा का प्रचलित मूल्यों पर जीएसडीपी ₹12,13,951 करोड़ था, जो एक वर्ष पहले से 11.8% अधिक है; यह भारत के जीडीपी का लगभग 3.7% था। राज्य वित्त विभाग ने वित्त वर्ष 2023-24 में प्रति व्यक्ति आय ₹3,25,759 बताई। स्थिर मूल्यों पर वित्त वर्ष 2023-24 में जीएसवीए में सेवाओं का हिस्सा लगभग 51%, उद्योग का 33% और कृषि व संबद्ध क्षेत्रों का 16% था।\n\nगुरुग्राम कॉर्पोरेट कार्यालयों, आईटी और वित्तीय सेवाओं का केंद्र है, और गुरुग्राम–मानेसर–फ़रीदाबाद पट्टी भारत की कारों, दोपहिया वाहनों और कलपुर्ज़ों का बड़ा हिस्सा बनाती है। पानीपत वस्त्र और हथकरघा फ़र्निशिंग के लिए जाना जाता है और यहाँ तेल रिफ़ाइनरी है; यमुनानगर प्लाइवुड के लिए; अंबाला वैज्ञानिक उपकरणों के लिए; और सोनीपत व बहादुरगढ़ जूतों और हल्के उद्योगों के लिए। खेती — गेहूँ, बासमती व अन्य धान, सरसों, कपास, बाजरा और गन्ना — और मुर्रा भैंसों के साथ डेयरी ग्रामीण आय के केंद्र में हैं। पीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी (भारत {ui['2025']}%), और 15 वर्ष से अधिक आयु की केवल {lf['female']}% महिलाएँ श्रम बल में थीं, जबकि राष्ट्रीय स्तर पर {lfi['female']}%।",
        f"नियंत्रक व महालेखापरीक्षकांच्या राज्य वित्त लेखापरीक्षा अहवालानुसार आ.व. 2024-25 मध्ये हरियाणाचे चालू किमतींनुसार जीएसडीपी ₹12,13,951 कोटी होते, जे वर्षभरापूर्वीपेक्षा 11.8% अधिक आहे; ते भारताच्या जीडीपीच्या सुमारे 3.7% होते. राज्य वित्त विभागाने आ.व. 2023-24 मध्ये दरडोई उत्पन्न ₹3,25,759 सांगितले. स्थिर किमतींनुसार आ.व. 2023-24 मध्ये जीएसव्हीएमध्ये सेवांचा वाटा सुमारे 51%, उद्योगाचा 33% व शेती आणि संलग्न क्षेत्रांचा 16% होता.\n\nगुरुग्राम हे कॉर्पोरेट कार्यालये, आयटी व वित्तीय सेवांचे केंद्र आहे, आणि गुरुग्राम–मानेसर–फरिदाबाद पट्टा भारतातील मोटारी, दुचाकी व सुट्या भागांचा मोठा वाटा बनवतो. पानिपत वस्त्रोद्योग व हातमाग फर्निशिंगसाठी ओळखले जाते आणि तेथे तेलशुद्धीकरण कारखाना आहे; यमुनानगर प्लायवूडसाठी; अंबाला वैज्ञानिक उपकरणांसाठी; आणि सोनीपत व बहादुरगड पादत्राणे व हलक्या उद्योगांसाठी. शेती — गहू, बासमती व इतर भात, मोहरी, कापूस, बाजरी व ऊस — आणि मुर्रा म्हशींसह दुग्धव्यवसाय ग्रामीण उत्पन्नाच्या केंद्रस्थानी आहेत. पीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता (भारत {ui['2025']}%), आणि 15 वर्षांवरील केवळ {lf['female']}% स्त्रिया श्रमशक्तीत होत्या, तर राष्ट्रीय पातळीवर {lfi['female']}%."),
        sources=["cag", "hr-finance", "plfs"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"), hr["gsdpCurrent"], "rupeeCrore", "higher-is-better",
             previous=dp(1085510, "₹ crore", "FY2023-24", "fy", "cag", CAG_HR, rev="provisional", base=CUR, note="CAG SFAR Haryana 2024-25, Table 1.2.")),
        fact("pc", L("Per capita income, current prices", "प्रति व्यक्ति आय, प्रचलित मूल्य", "दरडोई उत्पन्न, चालू किमती"), hr["perCapitaNsdpCurrent"], "rupee", "higher-is-better",
             previous=dp(296592, "₹", "FY2022-23", "fy", "hr-finance", FRBM_HR, rev="provisional", base=CUR, note="Quick estimate.")),
        *plfs_facts("HR", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    {"type": "series", "id": "gsdp-series", "title": L("GSDP at current prices, FY2020-21 to FY2024-25", "प्रचलित मूल्यों पर जीएसडीपी, वित्त वर्ष 2020-21 से 2024-25", "चालू किमतींनुसार जीएसडीपी, आ.व. 2020-21 ते 2024-25"),
     "kind": "rupeeCrore", "polarity": "higher-is-better",
     "series": [{"id": "current", "label": L("Current prices", "प्रचलित मूल्य", "चालू किमती"),
                 "points": [dp(v, "₹ crore", y, "fy", "cag", CAG_HR, rev="provisional", base=CUR) for y, v in CAG_SERIES]}],
     "note": L("CAG, State Finances Audit Report of Haryana 2024-25, Table 1.2. A constant-price series and sectoral GSVA by industry were not available from MoSPI for Haryana at access time.",
               "सीएजी, हरियाणा राज्य वित्त लेखापरीक्षा रिपोर्ट 2024-25, तालिका 1.2। स्थिर मूल्य शृंखला और उद्योगवार क्षेत्रीय जीएसवीए उस समय मोस्पी से हरियाणा के लिए उपलब्ध नहीं थे।",
               "कॅग, हरियाणा राज्य वित्त लेखापरीक्षा अहवाल 2024-25, तक्ता 1.2. स्थिर किंमत मालिका व उद्योगनिहाय क्षेत्रीय जीएसव्हीए त्या वेळी मोस्पीकडून हरियाणासाठी उपलब्ध नव्हते.")},
    table("sectors", L("Sectoral shares of GSVA, FY2023-24 (constant 2011-12 prices)", "जीएसवीए में क्षेत्रवार हिस्सा, वित्त वर्ष 2023-24 (स्थिर 2011-12 मूल्य)", "जीएसव्हीएमधील क्षेत्रनिहाय वाटा, आ.व. 2023-24 (स्थिर 2011-12 किमती)"),
          [col(L("Sector", "क्षेत्र", "क्षेत्र")), col(L("Share of GSVA (%)", "जीएसवीए में हिस्सा (%)", "जीएसव्हीएमधील वाटा (%)"), "right")],
          [[L("Primary (agriculture, livestock, forestry, fishing, mining)", "प्राथमिक (कृषि, पशुपालन, वानिकी, मत्स्य, खनन)", "प्राथमिक (शेती, पशुपालन, वनीकरण, मत्स्य, खाणकाम)"), 16.3],
           [L("Secondary (manufacturing, construction, utilities)", "द्वितीयक (विनिर्माण, निर्माण, उपयोगिताएँ)", "द्वितीयक (उत्पादन, बांधकाम, उपयुक्तता सेवा)"), 33.0],
           [L("Tertiary (services)", "तृतीयक (सेवाएँ)", "तृतीयक (सेवा)"), 50.7]],
          "hr-finance", FRBM_HR, period="FY2023-24",
          note=L("Haryana Finance Department, Statements of Fiscal Policy (Budget 2024-25), advance estimates. Growth in 2023-24: primary 4.5%, secondary 7.2%, tertiary 9.0%.",
                 "हरियाणा वित्त विभाग, राजकोषीय नीति विवरण (बजट 2024-25), अग्रिम अनुमान। 2023-24 में वृद्धि: प्राथमिक 4.5%, द्वितीयक 7.2%, तृतीयक 9.0%।",
                 "हरियाणा वित्त विभाग, राजकोषीय धोरण निवेदने (अर्थसंकल्प 2024-25), आगाऊ अंदाज. 2023-24 मधील वाढ: प्राथमिक 4.5%, द्वितीयक 7.2%, तृतीयक 9.0%.")),
    plfs_series("HR", NAME),
    lst("sectors-key", [
        it3("auto", "Automobiles and components", "ऑटोमोबाइल और कलपुर्ज़े", "मोटारी व सुटे भाग", d=("Car and two-wheeler plants in Gurugram, Manesar, Dharuhera and Kharkhoda.", "गुरुग्राम, मानेसर, धारूहेड़ा और खरखौदा में कार और दोपहिया संयंत्र।", "गुरुग्राम, मानेसर, धारुहेडा व खरखोदा येथे मोटार व दुचाकी कारखाने.")),
        it3("it", "IT and business services", "आईटी और व्यावसायिक सेवाएँ", "आयटी व व्यावसायिक सेवा", d=("Gurugram's offices, start-ups and global capability centres.", "गुरुग्राम के कार्यालय, स्टार्टअप और वैश्विक क्षमता केंद्र।", "गुरुग्रामची कार्यालये, स्टार्टअप व जागतिक क्षमता केंद्रे.")),
        it3("textile", "Textiles and handloom", "वस्त्र और हथकरघा", "वस्त्रोद्योग व हातमाग", d=("Panipat's home furnishings, blankets and recycled yarn.", "पानीपत की गृह-सज्जा, कंबल और पुनर्चक्रित धागा।", "पानिपतचे गृहसजावट साहित्य, घोंगड्या व पुनर्वापरित धागा.")),
        it3("agri", "Wheat, rice and mustard", "गेहूँ, धान और सरसों", "गहू, भात व मोहरी", d=("Basmati in the north; mustard and bajra in the south-west.", "उत्तर में बासमती; दक्षिण-पश्चिम में सरसों और बाजरा।", "उत्तरेत बासमती; नैर्ऋत्येत मोहरी व बाजरी.")),
        it3("dairy", "Dairy", "डेयरी", "दुग्धव्यवसाय", d=("Murrah buffalo, bred around Rohtak, Jind and Hisar; NDRI Karnal.", "रोहतक, जींद और हिसार के आसपास पाली जाने वाली मुर्रा भैंस; एनडीआरआई करनाल।", "रोहतक, जिंद व हिसारभोवती पाळली जाणारी मुर्रा म्हैस; एनडीआरआय कर्नाल.")),
        it3("ply", "Plywood and instruments", "प्लाइवुड और उपकरण", "प्लायवूड व उपकरणे", d=("Yamunanagar plywood; Ambala scientific instruments.", "यमुनानगर का प्लाइवुड; अंबाला के वैज्ञानिक उपकरण।", "यमुनानगरचे प्लायवूड; अंबालाची वैज्ञानिक उपकरणे.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("GSDP at constant prices and GSVA by industry (MoSPI)", "स्थिर मूल्यों पर जीएसडीपी और उद्योगवार जीएसवीए (मोस्पी)", "स्थिर किमतींनुसार जीएसडीपी व उद्योगनिहाय जीएसव्हीए (मोस्पी)"), "mospi", "MoSPI's state-wise API returned no Haryana series at access time; use the Haryana Economic Survey or DESA Haryana."),
        (L("Per capita income for FY2024-25", "वित्त वर्ष 2024-25 की प्रति व्यक्ति आय", "आ.व. 2024-25 चे दरडोई उत्पन्न"), "state-economic-survey", "Haryana Economic Survey 2024-25."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "cag", "CAG SFAR / RBI State Finances."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Haryana has a unicameral legislature, the 90-member Vidhan Sabha, which sits in Chandigarh. The State elects 10 members to the Lok Sabha and 5 to the Rajya Sabha.\n\nIn the Assembly election of October 2024 the Bharatiya Janata Party won 48 of the 90 seats, a third consecutive term, and Nayab Singh Saini — Chief Minister since March 2024 — was sworn in again on 17 October 2024 at Panchkula. Harvinder Kalyan (BJP) is Speaker. Ashim Kumar Ghosh has been Governor since 21 July 2025. The next Assembly election is due by late 2029.",
        "हरियाणा में एकसदनीय विधानमंडल है, 90 सदस्यों वाली विधानसभा, जिसकी बैठकें चंडीगढ़ में होती हैं। राज्य से लोकसभा के 10 और राज्यसभा के 5 सदस्य चुने जाते हैं।\n\nअक्टूबर 2024 के विधानसभा चुनाव में भारतीय जनता पार्टी ने 90 में से 48 सीटें जीतीं, जो लगातार तीसरा कार्यकाल है, और मार्च 2024 से मुख्यमंत्री नायब सिंह सैनी ने 17 अक्टूबर 2024 को पंचकूला में फिर से शपथ ली। हरविंद्र कल्याण (भाजपा) अध्यक्ष हैं। असीम कुमार घोष 21 जुलाई 2025 से राज्यपाल हैं। अगला विधानसभा चुनाव 2029 के अंत तक होना है।",
        "हरियाणामध्ये एकसदनी विधिमंडळ आहे, 90 सदस्यांची विधानसभा, जिच्या बैठका चंदीगडमध्ये होतात. राज्यातून लोकसभेवर 10 व राज्यसभेवर 5 सदस्य निवडले जातात.\n\nऑक्टोबर 2024 च्या विधानसभा निवडणुकीत भारतीय जनता पक्षाने 90 पैकी 48 जागा जिंकल्या, ही सलग तिसरी कारकीर्द आहे, आणि मार्च 2024 पासून मुख्यमंत्री असलेल्या नायबसिंह सैनी यांनी 17 ऑक्टोबर 2024 रोजी पंचकुला येथे पुन्हा शपथ घेतली. हरविंदर कल्याण (भाजप) अध्यक्ष आहेत. असीम कुमार घोष 21 जुलै 2025 पासून राज्यपाल आहेत. पुढील विधानसभा निवडणूक 2029 च्या अखेरीपर्यंत होणे अपेक्षित आहे."),
        sources=["the-week", "hr-lokbhavan", "tribune"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("lokbhavan", "Lok Bhavan Haryana", "लोक भवन हरियाणा", "लोक भवन हरियाणा", url="https://lokbhavan.haryana.gov.in", src="hr-lokbhavan"),
        it3("portal", "Government of Haryana", "हरियाणा सरकार", "हरियाणा शासन", url="https://haryana.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("2024 Assembly election — party-wise result", "2024 विधानसभा चुनाव — दलवार परिणाम", "2024 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Haryana 2024."),
        (L("Chief Minister's swearing-in — official source", "मुख्यमंत्री का शपथ ग्रहण — आधिकारिक स्रोत", "मुख्यमंत्र्यांचा शपथविधी — अधिकृत स्रोत"), "hr-lokbhavan", "Replace the PTI copy with the Lok Bhavan release."),
        (L("Leader of Opposition — official notice", "नेता प्रतिपक्ष — आधिकारिक सूचना", "विरोधी पक्षनेते — अधिकृत सूचना"), "india-gov", "Vidhan Sabha secretariat."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "The 19-km Haryana section of the Dwarka Expressway, linking Gurugram with IGI Airport, was inaugurated in March 2024. Other large works in the State include the Delhi–Mumbai Expressway through Sohna and Nuh, the Western Dedicated Freight Corridor through Rewari, the nuclear power project at Gorakhpur in Fatehabad district and the AIIMS at Majra in Rewari; these will be added as cards once their status is confirmed from official sources. Each card shows its source and the date it was checked.",
        "गुरुग्राम को आईजीआई हवाई अड्डे से जोड़ने वाले द्वारका एक्सप्रेसवे के 19 किमी हरियाणा खंड का उद्घाटन मार्च 2024 में हुआ। राज्य के अन्य बड़े कार्यों में सोहना और नूँह से होकर दिल्ली–मुंबई एक्सप्रेसवे, रेवाड़ी से होकर पश्चिमी समर्पित माल गलियारा, फ़तेहाबाद ज़िले के गोरखपुर में परमाणु बिजली परियोजना और रेवाड़ी के माजरा में एम्स शामिल हैं; आधिकारिक स्रोतों से स्थिति की पुष्टि होने पर इन्हें कार्ड के रूप में जोड़ा जाएगा। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "गुरुग्रामला आयजीआय विमानतळाशी जोडणाऱ्या द्वारका द्रुतगती मार्गाच्या 19 किमी हरियाणा टप्प्याचे उद्घाटन मार्च 2024 मध्ये झाले. राज्यातील इतर मोठ्या कामांत सोहना व नूहमार्गे दिल्ली–मुंबई द्रुतगती मार्ग, रेवाडीमार्गे पश्चिम समर्पित मालवाहतूक मार्गिका, फतेहाबाद जिल्ह्यातील गोरखपूर येथील अणुऊर्जा प्रकल्प आणि रेवाडीच्या माजरा येथील एम्स यांचा समावेश आहे; अधिकृत स्रोतांतून स्थितीची खात्री झाल्यावर त्यांची कार्डे जोडली जातील. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pmindia"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Gorakhpur Haryana Anu Vidyut Pariyojana — status", "गोरखपुर हरियाणा अणु विद्युत परियोजना — स्थिति", "गोरखपूर हरियाणा अणुविद्युत प्रकल्प — स्थिती"), "npcil", "NPCIL project status."),
        (L("AIIMS Rewari (Majra) — status", "एम्स रेवाड़ी (माजरा) — स्थिति", "एम्स रेवाडी (माजरा) — स्थिती"), "mohfw", "MoHFW / PMSSY status."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Most air travellers from Haryana use Delhi's Indira Gandhi International Airport, next to Gurugram; the State's own Maharaja Agrasen Airport at Hisar has begun scheduled flights. National Highway 44 (the old Grand Trunk Road) runs north from Delhi through Sonipat, Panipat, Karnal and Ambala, and the Delhi–Mumbai Expressway, the Kundli–Manesar–Palwal Expressway and the Dwarka Expressway serve the south. The Delhi Metro reaches Gurugram, Faridabad, Ballabgarh and Bahadurgarh, and Gurugram has its own Rapid Metro. Ambala Cantonment is a major railway junction of the Northern Railway, and the Western Dedicated Freight Corridor passes through Rewari.",
        "हरियाणा के अधिकांश हवाई यात्री गुरुग्राम से सटे दिल्ली के इंदिरा गांधी अंतरराष्ट्रीय हवाई अड्डे का उपयोग करते हैं; राज्य के अपने हिसार स्थित महाराजा अग्रसेन हवाई अड्डे से नियमित उड़ानें शुरू हो चुकी हैं। राष्ट्रीय राजमार्ग 44 (पुरानी ग्रैंड ट्रंक रोड) दिल्ली से उत्तर की ओर सोनीपत, पानीपत, करनाल और अंबाला से होकर जाता है, और दिल्ली–मुंबई एक्सप्रेसवे, कुंडली–मानेसर–पलवल एक्सप्रेसवे और द्वारका एक्सप्रेसवे दक्षिण को सेवा देते हैं। दिल्ली मेट्रो गुरुग्राम, फ़रीदाबाद, बल्लभगढ़ और बहादुरगढ़ तक पहुँचती है, और गुरुग्राम की अपनी रैपिड मेट्रो है। अंबाला छावनी उत्तर रेलवे का प्रमुख जंक्शन है, और पश्चिमी समर्पित माल गलियारा रेवाड़ी से गुज़रता है।",
        "हरियाणातील बहुतेक हवाई प्रवासी गुरुग्रामलगतच्या दिल्लीच्या इंदिरा गांधी आंतरराष्ट्रीय विमानतळाचा वापर करतात; राज्याच्या स्वतःच्या हिसार येथील महाराजा अग्रसेन विमानतळावरून नियमित उड्डाणे सुरू झाली आहेत. राष्ट्रीय महामार्ग 44 (जुना ग्रँड ट्रंक रोड) दिल्लीहून उत्तरेकडे सोनीपत, पानिपत, कर्नाल व अंबालामार्गे जातो, आणि दिल्ली–मुंबई द्रुतगती मार्ग, कुंडली–मानेसर–पलवल द्रुतगती मार्ग व द्वारका द्रुतगती मार्ग दक्षिणेला सेवा देतात. दिल्ली मेट्रो गुरुग्राम, फरिदाबाद, बल्लभगड व बहादुरगडपर्यंत पोहोचते, आणि गुरुग्रामची स्वतःची रॅपिड मेट्रो आहे. अंबाला छावणी हे उत्तर रेल्वेचे प्रमुख जंक्शन आहे, आणि पश्चिम समर्पित मालवाहतूक मार्गिका रेवाडीमधून जाते."),
        conf="Editorial"),
    lst("airports", [
        it3("del", "Indira Gandhi International Airport, Delhi (nearest hub)", "इंदिरा गांधी अंतरराष्ट्रीय हवाई अड्डा, दिल्ली (निकटतम केंद्र)", "इंदिरा गांधी आंतरराष्ट्रीय विमानतळ, दिल्ली (जवळचे केंद्र)", m=("DEL", "DEL", "DEL")),
        it3("hss", "Maharaja Agrasen Airport, Hisar", "महाराजा अग्रसेन हवाई अड्डा, हिसार", "महाराजा अग्रसेन विमानतळ, हिसार", m=("Hisar", "हिसार", "हिसार")),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Hisar airport — flights and traffic", "हिसार हवाई अड्डा — उड़ानें और यातायात", "हिसार विमानतळ — उड्डाणे व वाहतूक"), "aai", "AAI / State Civil Aviation Department."),
        (L("Delhi–Gurugram–SNB RRTS corridor — status", "दिल्ली–गुरुग्राम–एसएनबी आरआरटीएस गलियारा — स्थिति", "दिल्ली–गुरुग्राम–एसएनबी आरआरटीएस मार्गिका — स्थिती"), "ncrtc", "NCRTC project page."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Haryana's electricity comes mainly from coal-fired plants — the State's own stations at Panipat, Khedar (Hisar) and Yamunanagar, the Indira Gandhi plant at Jhajjar run with NTPC, and a private plant at Jhajjar — together with its share of hydro-electric power from the Bhakra–Beas system and long-term purchases from central and other States' plants. A nuclear power project is being built at Gorakhpur in Fatehabad district by the Nuclear Power Corporation of India. Demand peaks in summer and during paddy transplanting, and rooftop and farm solar pumps are being promoted.",
        "हरियाणा की बिजली मुख्यतः कोयला संयंत्रों से आती है — पानीपत, खेदड़ (हिसार) और यमुनानगर के राज्य के अपने संयंत्र, एनटीपीसी के साथ चलने वाला झज्जर का इंदिरा गांधी संयंत्र और झज्जर का एक निजी संयंत्र — साथ में भाखड़ा–ब्यास प्रणाली की जलविद्युत में इसका हिस्सा और केंद्रीय व अन्य राज्यों के संयंत्रों से दीर्घकालिक ख़रीद। फ़तेहाबाद ज़िले के गोरखपुर में न्यूक्लियर पावर कॉर्पोरेशन ऑफ़ इंडिया एक परमाणु बिजली परियोजना बना रहा है। गर्मियों और धान रोपाई के दौरान माँग चरम पर होती है, और छतों पर सौर ऊर्जा और खेतों के लिए सौर पंपों को बढ़ावा दिया जा रहा है।",
        "हरियाणाची वीज मुख्यतः कोळसा प्रकल्पांतून येते — पानिपत, खेदड (हिसार) व यमुनानगर येथील राज्याचे स्वतःचे प्रकल्प, एनटीपीसीसोबत चालवला जाणारा झज्जरचा इंदिरा गांधी प्रकल्प व झज्जरचा एक खासगी प्रकल्प — सोबत भाक्रा–बियास प्रणालीतील जलविद्युतचा वाटा आणि केंद्रीय व इतर राज्यांच्या प्रकल्पांतून दीर्घकालीन खरेदी. फतेहाबाद जिल्ह्यातील गोरखपूर येथे न्यूक्लियर पॉवर कॉर्पोरेशन ऑफ इंडिया अणुऊर्जा प्रकल्प उभारत आहे. उन्हाळ्यात व भातलावणीच्या काळात मागणी शिखरावर असते, आणि छतांवरील सौरऊर्जा व शेतीसाठी सौरपंपांना प्रोत्साहन दिले जात आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Gorakhpur nuclear project — capacity and progress", "गोरखपुर परमाणु परियोजना — क्षमता और प्रगति", "गोरखपूर अणुप्रकल्प — क्षमता व प्रगती"), "npcil", "NPCIL."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Gurugram is one of India's leading technology and business-services cities, home to offices of many multinational companies, global capability centres and start-ups; Faridabad, Manesar and Panchkula's IT park add to the cluster. The State delivers citizen services online through the Saral portal and Antyodaya Saral centres, and runs the Parivar Pehchan Patra family-ID system used for welfare schemes.",
        "गुरुग्राम भारत के अग्रणी प्रौद्योगिकी और व्यावसायिक सेवा शहरों में से है, जहाँ अनेक बहुराष्ट्रीय कंपनियों के कार्यालय, वैश्विक क्षमता केंद्र और स्टार्टअप हैं; फ़रीदाबाद, मानेसर और पंचकूला का आईटी पार्क इस क्लस्टर को बढ़ाते हैं। राज्य सरल पोर्टल और अंत्योदय सरल केंद्रों के माध्यम से नागरिक सेवाएँ ऑनलाइन देता है, और कल्याणकारी योजनाओं के लिए परिवार पहचान पत्र प्रणाली चलाता है।",
        "गुरुग्राम हे भारतातील आघाडीच्या तंत्रज्ञान व व्यावसायिक सेवा शहरांपैकी एक आहे, जिथे अनेक बहुराष्ट्रीय कंपन्यांची कार्यालये, जागतिक क्षमता केंद्रे व स्टार्टअप आहेत; फरिदाबाद, मानेसर व पंचकुलाचे आयटी पार्क या समूहात भर घालतात. राज्य सरल पोर्टल व अंत्योदय सरल केंद्रांमार्फत नागरी सेवा ऑनलाइन देते, आणि कल्याणकारी योजनांसाठी परिवार पहचान पत्र ही कुटुंब ओळख प्रणाली चालवते."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Haryana circle)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("HR", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["HR"]
ger = AP["aishe_ger"]["HR"]; nu = AP["aishe_universities_2021_22"]["HR"]; nc = AP["aishe_colleges_2021_22"]["HR"]
module(R, "education", [
    prose("p1", L(
        f"Haryana's higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE, above the national 28.4% and up from {ger['2017-18']}% in 2017-18; women's GER ({gf}%) was well above men's ({gm}%). The State had {nu} universities and {inr(nc)} colleges. Literacy at the 2011 Census was 75.6%.\n\nKurukshetra University (1956), Maharshi Dayanand University in Rohtak (1976) and Chaudhary Charan Singh Haryana Agricultural University in Hisar (1970) are the oldest State universities, and the Lala Lajpat Rai University of Veterinary and Animal Sciences is also in Hisar. National institutions include IIM Rohtak, NIT Kurukshetra, the National Dairy Research Institute in Karnal, the Central University of Haryana at Mahendragarh, and the National Cancer Institute of AIIMS at Badsa in Jhajjar; Pt. B. D. Sharma PGIMS in Rohtak is the main State medical institute. Private universities in Sonipat and Gurugram have grown rapidly.",
        f"एआईएसएचई के अनुसार 2021-22 में हरियाणा का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था, जो राष्ट्रीय 28.4% से अधिक और 2017-18 के {ger['2017-18']}% से ऊपर है; महिलाओं का जीईआर ({gf}%) पुरुषों ({gm}%) से काफ़ी अधिक था। राज्य में {nu} विश्वविद्यालय और {inr(nc)} कॉलेज थे। 2011 की जनगणना में साक्षरता 75.6% थी।\n\nकुरुक्षेत्र विश्वविद्यालय (1956), रोहतक का महर्षि दयानंद विश्वविद्यालय (1976) और हिसार का चौधरी चरण सिंह हरियाणा कृषि विश्वविद्यालय (1970) सबसे पुराने राज्य विश्वविद्यालय हैं, और लाला लाजपत राय पशु चिकित्सा एवं पशु विज्ञान विश्वविद्यालय भी हिसार में है। राष्ट्रीय संस्थानों में आईआईएम रोहतक, एनआईटी कुरुक्षेत्र, करनाल का राष्ट्रीय डेयरी अनुसंधान संस्थान, महेंद्रगढ़ का हरियाणा केंद्रीय विश्वविद्यालय और झज्जर के बाढ़सा में एम्स का राष्ट्रीय कैंसर संस्थान शामिल हैं; रोहतक का पं. बी. डी. शर्मा पीजीआईएमएस राज्य का मुख्य चिकित्सा संस्थान है। सोनीपत और गुरुग्राम में निजी विश्वविद्यालय तेज़ी से बढ़े हैं।",
        f"एआयएसएचईनुसार 2021-22 मध्ये हरियाणाचे उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा अधिक व 2017-18 मधील {ger['2017-18']}% पेक्षा जास्त; स्त्रियांचे जीईआर ({gf}%) पुरुषांपेक्षा ({gm}%) बरेच अधिक होते. राज्यात {nu} विद्यापीठे व {inr(nc)} महाविद्यालये होती. 2011 च्या जनगणनेत साक्षरता 75.6% होती.\n\nकुरुक्षेत्र विद्यापीठ (1956), रोहतकचे महर्षी दयानंद विद्यापीठ (1976) व हिसारचे चौधरी चरणसिंह हरियाणा कृषी विद्यापीठ (1970) ही सर्वांत जुनी राज्य विद्यापीठे आहेत, आणि लाला लजपतराय पशुवैद्यकीय व पशुविज्ञान विद्यापीठही हिसारमध्ये आहे. राष्ट्रीय संस्थांत आयआयएम रोहतक, एनआयटी कुरुक्षेत्र, कर्नालची राष्ट्रीय दुग्ध संशोधन संस्था, महेंद्रगडचे हरियाणा केंद्रीय विद्यापीठ आणि झज्जरच्या बाढसा येथील एम्सची राष्ट्रीय कर्करोग संस्था यांचा समावेश आहे; रोहतकचे पं. बी. डी. शर्मा पीजीआयएमएस ही राज्याची मुख्य वैद्यकीय संस्था आहे. सोनीपत व गुरुग्राममध्ये खासगी विद्यापीठे झपाट्याने वाढली आहेत."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("kuk", "Kurukshetra University", "कुरुक्षेत्र विश्वविद्यालय", "कुरुक्षेत्र विद्यापीठ", m=("Kurukshetra, 1956", "कुरुक्षेत्र, 1956", "कुरुक्षेत्र, 1956")),
        it3("mdu", "Maharshi Dayanand University", "महर्षि दयानंद विश्वविद्यालय", "महर्षी दयानंद विद्यापीठ", m=("Rohtak, 1976", "रोहतक, 1976", "रोहतक, 1976")),
        it3("hau", "CCS Haryana Agricultural University", "चौ. चरण सिंह हरियाणा कृषि विश्वविद्यालय", "चौ. चरणसिंह हरियाणा कृषी विद्यापीठ", m=("Hisar, 1970", "हिसार, 1970", "हिसार, 1970")),
        it3("iimr", "IIM Rohtak", "आईआईएम रोहतक", "आयआयएम रोहतक", m=("Rohtak", "रोहतक", "रोहतक")),
        it3("nitk", "NIT Kurukshetra", "एनआईटी कुरुक्षेत्र", "एनआयटी कुरुक्षेत्र", m=("Kurukshetra", "कुरुक्षेत्र", "कुरुक्षेत्र")),
        it3("ndri", "National Dairy Research Institute", "राष्ट्रीय डेयरी अनुसंधान संस्थान", "राष्ट्रीय दुग्ध संशोधन संस्था", m=("Karnal", "करनाल", "कर्नाल")),
        it3("cuh", "Central University of Haryana", "हरियाणा केंद्रीय विश्वविद्यालय", "हरियाणा केंद्रीय विद्यापीठ", m=("Mahendragarh", "महेंद्रगढ़", "महेंद्रगड")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
    ]),
])

# ---------------- O. Health ----------------
n = NF["HR"]; s = C["srs"]["HR"]; le = C["le"]["HR"]
module(R, "health", [
    prose("p1", L(
        f"Haryana's infant mortality rate fell from {s[4]:.0f} per 1,000 live births in 2010 to {s[5]:.0f} in 2020, equal to the national rate, and the birth rate was {s[1]} per 1,000 (death rate {s[3]}). Life expectancy at birth was {le[2]} years in 2014-18 (men {le[0]}, women {le[1]}), close to the national 69.4. Child nutrition improved markedly between the two national family health surveys: in NFHS-5, {n['stunted'][1]:.1f}% of children under five were stunted (down from {n['stunted'][0]}%), {n['wasted'][1]:.1f}% wasted (from {n['wasted'][0]}%) and {n['underweight'][1]:.1f}% underweight (from {n['underweight'][0]}%), and {n['institutional_N5']:.1f}% of births took place in health facilities, up from 80.5% in NFHS-4.\n\nPGIMS Rohtak, the government medical colleges at Khanpur Kalan, Nalhar (Nuh) and Agroha, the National Cancer Institute at Badsa and large private hospitals in Gurugram and Faridabad are the main referral centres. Low sex ratios at birth have been a long-standing concern, addressed by campaigns such as Beti Bachao Beti Padhao, which was launched at Panipat in 2015.",
        f"हरियाणा की शिशु मृत्यु दर 2010 में प्रति 1,000 जीवित जन्म पर {s[4]:.0f} से घटकर 2020 में {s[5]:.0f} हो गई, जो राष्ट्रीय दर के बराबर है, और जन्म दर प्रति 1,000 पर {s[1]} थी (मृत्यु दर {s[3]})। 2014-18 में जन्म के समय जीवन प्रत्याशा {le[2]} वर्ष थी (पुरुष {le[0]}, महिलाएँ {le[1]}), जो राष्ट्रीय 69.4 के क़रीब है। दो राष्ट्रीय परिवार स्वास्थ्य सर्वेक्षणों के बीच बाल पोषण में उल्लेखनीय सुधार हुआ: एनएफ़एचएस-5 में पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने थे ({n['stunted'][0]}% से कम), {n['wasted'][1]:.1f}% दुबले ({n['wasted'][0]}% से) और {n['underweight'][1]:.1f}% कम वज़न के ({n['underweight'][0]}% से), और {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, जो एनएफ़एचएस-4 में 80.5% थे।\n\nपीजीआईएमएस रोहतक, खानपुर कलाँ, नल्हड़ (नूँह) और अग्रोहा के सरकारी मेडिकल कॉलेज, बाढ़सा का राष्ट्रीय कैंसर संस्थान और गुरुग्राम व फ़रीदाबाद के बड़े निजी अस्पताल मुख्य रेफ़रल केंद्र हैं। जन्म के समय कम लिंगानुपात लंबे समय से चिंता का विषय रहा है, जिसके लिए बेटी बचाओ बेटी पढ़ाओ जैसे अभियान चलाए गए, जो 2015 में पानीपत से शुरू हुआ।",
        f"हरियाणाचा अर्भक मृत्युदर 2010 मध्ये दर 1,000 जिवंत जन्मांमागे {s[4]:.0f} वरून 2020 मध्ये {s[5]:.0f} वर आला, जो राष्ट्रीय दराइतका आहे, आणि जन्मदर दर 1,000 मागे {s[1]} होता (मृत्युदर {s[3]}). 2014-18 मध्ये जन्मतः आयुर्मान {le[2]} वर्षे होते (पुरुष {le[0]}, स्त्रिया {le[1]}), राष्ट्रीय 69.4 च्या जवळ. दोन राष्ट्रीय कुटुंब आरोग्य सर्वेक्षणांदरम्यान बालपोषणात लक्षणीय सुधारणा झाली: एनएफएचएस-5 मध्ये पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी होती ({n['stunted'][0]}% वरून कमी), {n['wasted'][1]:.1f}% कृश ({n['wasted'][0]}% वरून) व {n['underweight'][1]:.1f}% कमी वजनाची ({n['underweight'][0]}% वरून), आणि {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, एनएफएचएस-4 मध्ये 80.5% होत्या.\n\nपीजीआयएमएस रोहतक, खानपूर कलां, नल्हड (नूह) व अग्रोहाची शासकीय वैद्यकीय महाविद्यालये, बाढसाची राष्ट्रीय कर्करोग संस्था आणि गुरुग्राम व फरिदाबादची मोठी खासगी रुग्णालये ही मुख्य संदर्भ केंद्रे आहेत. जन्मावेळचे कमी लिंग गुणोत्तर ही दीर्घकाळची चिंता राहिली आहे, ज्यासाठी बेटी बचाओ बेटी पढाओसारखी अभियाने राबवली गेली; हे अभियान 2015 मध्ये पानिपत येथून सुरू झाले."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(le[2], "years", "2014-18", "survey", "srs", ESI_LE, note=f"SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male {le[0]}, female {le[1]})."), "number", "higher-is-better",
             national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("HR"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Sex ratio at birth (SRS / CRS)", "जन्म के समय लिंगानुपात (एसआरएस / सीआरएस)", "जन्मावेळचे लिंग गुणोत्तर (एसआरएस / सीआरएस)"), "srs", "SRS statistical report; Civil Registration System."),
        (L("Maternal mortality ratio (SRS 2019-21)", "मातृ मृत्यु अनुपात (एसआरएस 2019-21)", "मातामृत्यू प्रमाण (एसआरएस 2019-21)"), "srs", "SRS special bulletin."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("hr mod2 ok")
