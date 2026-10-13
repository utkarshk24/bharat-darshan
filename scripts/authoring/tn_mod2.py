"""Tamil Nadu modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-TN"
TN23 = "https://des.tn.gov.in/sites/default/files/2024-01/At_a_glance_%2029_12_2023.pdf"
ECI = "https://results.eci.gov.in/ResultAcGenMay2026/partywiseresult-S22.htm"
mo = research("mospi_tn.json")
NAME = L("Tamil Nadu", "तमिलनाडु", "तमिळनाडू")
NOTE_TN = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API. "
           "FY2025-26 is the latest year published for Tamil Nadu and may be revised.")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Tamil culture is built on a literary tradition more than two thousand years old — from the Sangam anthologies and the Thirukkural, a book of ethics in 1,330 couplets, to the devotional hymns of the Nayanmars and Alvars and the modern poetry of Subramania Bharati. Temples are the other pillar: the towering gopurams of Madurai, Srirangam, Thanjavur and Chidambaram are still the centres of festival life, music and craft.\n\nBharatanatyam, the classical dance, grew from temple and court traditions, and Carnatic music has its creative heart in the works of the 18th–19th-century Trinity of Thyagaraja, Muthuswami Dikshitar and Syama Sastri. Folk forms — therukoothu street theatre, karagattam, villu paattu ballads and the silambam staff art — remain popular in villages, and Tamil cinema, based in Chennai's Kodambakkam, is one of India's largest film industries.",
        "तमिल संस्कृति दो हज़ार साल से अधिक पुरानी साहित्यिक परंपरा पर टिकी है — संगम संकलनों और 1,330 दोहों में नीति-ग्रंथ तिरुक्कुरल से लेकर नायनमारों और आलवारों के भक्ति भजनों और सुब्रमण्य भारती की आधुनिक कविता तक। मंदिर दूसरा स्तंभ हैं: मदुरै, श्रीरंगम, तंजावुर और चिदंबरम के ऊँचे गोपुरम आज भी उत्सव, संगीत और शिल्प के केंद्र हैं।\n\nशास्त्रीय नृत्य भरतनाट्यम मंदिर और दरबार की परंपराओं से विकसित हुआ, और कर्नाटक संगीत का रचनात्मक केंद्र 18वीं–19वीं सदी की त्रिमूर्ति — त्यागराज, मुत्तुस्वामी दीक्षितर और श्यामा शास्त्री — की रचनाएँ हैं। लोक रूप — तेरुक्कूत्तु सड़क रंगमंच, करगाट्टम, विल्लु पाट्टु गाथाएँ और सिलंबम लाठी कला — गाँवों में आज भी लोकप्रिय हैं, और चेन्नई के कोडंबक्कम में स्थित तमिल सिनेमा भारत के सबसे बड़े फ़िल्म उद्योगों में से एक है।",
        "तमिळ संस्कृती दोन हजार वर्षांहून जुन्या साहित्यपरंपरेवर उभी आहे — संगम संकलने आणि 1,330 द्विपदींमधील नीतिग्रंथ तिरुक्कुरळपासून नायनमार व आळवार संतांच्या भक्तिस्तोत्रांपर्यंत आणि सुब्रमण्य भारती यांच्या आधुनिक कवितेपर्यंत. मंदिरे हा दुसरा आधारस्तंभ: मदुराई, श्रीरंगम, तंजावूर आणि चिदंबरमची उत्तुंग गोपुरे आजही उत्सव, संगीत आणि कलाकुसरीची केंद्रे आहेत.\n\nभरतनाट्यम हे अभिजात नृत्य मंदिर व दरबारी परंपरांतून विकसित झाले, आणि कर्नाटक संगीताचा सर्जनशील गाभा अठराव्या–एकोणिसाव्या शतकातील त्रयी — त्यागराज, मुत्तुस्वामी दीक्षितर आणि श्यामा शास्त्री — यांच्या रचनांत आहे. लोककला — तेरुक्कूत्तू रस्त्यावरील नाट्य, करगाट्टम, विल्लू पाट्टू कथागीते आणि सिलंबम काठीकला — गावांत आजही लोकप्रिय आहेत, आणि चेन्नईच्या कोडंबक्कममधील तमिळ चित्रपटसृष्टी भारतातील सर्वांत मोठ्या चित्रपट उद्योगांपैकी एक आहे."),
        conf="Editorial"),
    lst("festivals", [
        fest("pongal", "Pongal", "पोंगल", "पोंगल", ("Mid-January", "जनवरी के मध्य", "जानेवारीच्या मध्यात"),
             ("Four-day harvest festival: new rice boiled with milk and jaggery until it overflows, kolam, and Mattu Pongal honouring cattle.", "चार दिन का फ़सल उत्सव: नए चावल को दूध और गुड़ के साथ उफान आने तक पकाया जाता है, कोलम बनते हैं, और मट्टु पोंगल पर पशुओं का सम्मान होता है।", "चार दिवसांचा सुगीचा सण: नवा तांदूळ दूध-गुळासह उतू जाईपर्यंत शिजवला जातो, कोलम रेखाटले जातात, आणि मट्टू पोंगलला गुराढोरांचा सन्मान होतो.")),
        fest("puthandu", "Puthandu (Tamil New Year)", "पुत्तांडु (तमिल नववर्ष)", "पुत्तांडू (तमिळ नववर्ष)", ("Mid-April", "अप्रैल के मध्य", "एप्रिलच्या मध्यात"),
             ("First day of the month of Chithirai, with a meal of six tastes.", "चित्तिरै महीने का पहला दिन, छह स्वादों वाले भोजन के साथ।", "चित्तिरै महिन्याचा पहिला दिवस, सहा चवींच्या जेवणासह.")),
        fest("chithirai", "Chithirai festival, Madurai", "चित्तिरै उत्सव, मदुरै", "चित्तिरै उत्सव, मदुराई", ("April–May", "अप्रैल–मई", "एप्रिल–मे"),
             ("Celebrates the wedding of Meenakshi and Sundareswarar; huge crowds for the temple car and Kallazhagar's entry into the Vaigai.", "मीनाक्षी और सुंदरेश्वर के विवाह का उत्सव; मंदिर रथ और कल्लझगर के वैगै प्रवेश पर भारी भीड़।", "मीनाक्षी व सुंदरेश्वर यांच्या विवाहाचा उत्सव; मंदिररथ आणि कल्लळगरच्या वैगै प्रवेशाला प्रचंड गर्दी.")),
        fest("thaipusam", "Thaipusam", "तैपूसम", "तैपूसम", ("January–February", "जनवरी–फ़रवरी", "जानेवारी–फेब्रुवारी"),
             ("Festival of Murugan, with pilgrims carrying kavadi to Palani and other hill shrines.", "मुरुगन का उत्सव, जिसमें श्रद्धालु पलनी और अन्य पहाड़ी मंदिरों तक कावड़ी ले जाते हैं।", "मुरुगनचा उत्सव; भाविक पळनी व इतर डोंगरमंदिरांपर्यंत कावडी नेतात.")),
        fest("karthigai", "Karthigai Deepam", "कार्तिगै दीपम", "कार्तिगै दीपम", ("November–December", "नवंबर–दिसंबर", "नोव्हेंबर–डिसेंबर"),
             ("Festival of lamps; a great beacon is lit on the Arunachala hill at Tiruvannamalai.", "दीपों का उत्सव; तिरुवण्णामलै में अरुणाचल पहाड़ी पर विशाल दीप जलाया जाता है।", "दिव्यांचा उत्सव; तिरुवण्णामलै येथे अरुणाचल डोंगरावर प्रचंड दीप प्रज्वलित केला जातो.")),
        fest("margazhi", "Margazhi music and dance season", "मार्गऴि संगीत और नृत्य सीज़न", "मार्गळी संगीत व नृत्य हंगाम", ("December–January", "दिसंबर–जनवरी", "डिसेंबर–जानेवारी"),
             ("Chennai's sabhas host hundreds of Carnatic music and Bharatanatyam performances.", "चेन्नई की सभाएँ कर्नाटक संगीत और भरतनाट्यम के सैकड़ों कार्यक्रम आयोजित करती हैं।", "चेन्नईतील सभा कर्नाटक संगीत व भरतनाट्यमचे शेकडो कार्यक्रम भरवतात.")),
        fest("velankanni", "Feast of Our Lady of Velankanni", "वेलांकन्नी माता का पर्व", "वेलांकण्णी मातेचा उत्सव", ("Late August – 8 September", "अगस्त के अंत से 8 सितंबर", "ऑगस्टअखेर ते 8 सप्टेंबर"),
             ("Pilgrims of many faiths gather at the basilica on the Nagapattinam coast.", "नागपट्टिनम तट पर स्थित बेसिलिका में अनेक धर्मों के तीर्थयात्री जुटते हैं।", "नागपट्टिनम किनाऱ्यावरील बॅसिलिकात अनेक धर्मांचे यात्रेकरू जमतात.")),
        fest("eid", "Eid al-Fitr and Eid al-Adha", "ईद-उल-फ़ित्र और ईद-उल-अज़हा", "ईद-उल-फित्र आणि ईद-उल-अजहा", ("Lunar calendar", "चंद्र कैलेंडर", "चांद्र दिनदर्शिका"),
             ("Celebrated with biryani feasts in Chennai, Vellore, Ambur and the coastal towns.", "चेन्नई, वेल्लोर, आम्बूर और तटीय कस्बों में बिरयानी की दावतों के साथ।", "चेन्नई, वेल्लोर, आंबूर आणि किनारी गावांत बिर्याणीच्या मेजवान्यांसह.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("bharatanatyam", "Bharatanatyam", "भरतनाट्यम", "भरतनाट्यम"), it3("carnatic", "Carnatic music", "कर्नाटक संगीत", "कर्नाटक संगीत"),
        it3("therukoothu", "Therukoothu", "तेरुक्कूत्तु", "तेरुक्कूत्तू"), it3("karagattam", "Karagattam", "करगाट्टम", "करगाट्टम"),
        it3("villu", "Villu paattu", "विल्लु पाट्टु", "विल्लू पाट्टू"), it3("silambam", "Silambam", "सिलंबम", "सिलंबम"),
        it3("parai", "Parai drumming", "पऱै ढोल वादन", "पऱै ढोलवादन"), it3("kolam", "Kolam", "कोलम", "कोलम"),
        it3("bronze", "Bronze casting (Swamimalai)", "कांस्य ढलाई (स्वामीमलै)", "कांस्य ओतकाम (स्वामीमलै)"), it3("tanjore", "Thanjavur painting", "तंजावुर चित्रकला", "तंजावूर चित्रकला"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("tiffin", "Idli, dosa and vada", "इडली, डोसा और वड़ा", "इडली, डोसा आणि वडा", d=("Breakfast staples served with sambar and coconut chutney.", "सांभर और नारियल चटनी के साथ परोसे जाने वाले नाश्ते के मुख्य व्यंजन।", "सांबार व नारळाच्या चटणीसह दिले जाणारे न्याहारीचे मुख्य पदार्थ.")),
        it3("meals", "Banana-leaf meals", "केले के पत्ते पर भोजन", "केळीच्या पानावरचे जेवण", d=("Rice with sambar, rasam, kootu, poriyal, curd and payasam.", "चावल के साथ सांभर, रसम, कूट्टु, पोरियल, दही और पायसम।", "भातासोबत सांबार, रसम, कूट्टू, पोरियल, दही आणि पायसम.")),
        it3("chettinad", "Chettinad cuisine", "चेट्टिनाड व्यंजन", "चेट्टिनाड खाद्यपदार्थ", d=("Richly spiced meat and vegetable dishes from the Karaikudi region.", "कराइकुडी क्षेत्र के तेज़ मसालेदार मांसाहारी और शाकाहारी व्यंजन।", "कराइकुडी परिसरातील झणझणीत मांसाहारी व शाकाहारी पदार्थ.")),
        it3("pongal", "Ven pongal and sakkarai pongal", "वेन पोंगल और सक्करै पोंगल", "वेण पोंगल आणि सक्करै पोंगल", d=("Savoury rice-and-lentil dish with pepper and ghee, and its jaggery-sweet twin.", "काली मिर्च और घी वाला नमकीन चावल-दाल व्यंजन, और गुड़ वाला उसका मीठा रूप।", "मिरी व तुपासह खारट तांदूळ-डाळ पदार्थ, आणि गुळाचे त्याचे गोड रूप.")),
        it3("biryani", "Ambur and Dindigul biryani", "आम्बूर और डिंडीगुल बिरयानी", "आंबूर व दिंडीगुल बिर्याणी", d=("Two distinct local styles, often made with short-grain seeraga samba rice.", "दो अलग स्थानीय शैलियाँ, अक्सर छोटे दाने वाले सीरगा सांबा चावल से।", "दोन वेगळ्या स्थानिक शैली, अनेकदा लहान दाण्याच्या सीरगा सांबा तांदळापासून.")),
        it3("coffee", "Filter coffee", "फ़िल्टर कॉफ़ी", "फिल्टर कॉफी", d=("Decoction with boiled milk, frothed between tumbler and dabarah.", "उबले दूध के साथ डिकॉक्शन, गिलास और डबरा के बीच झाग बनाकर।", "उकळत्या दुधासह डिकॉक्शन, पेला व डबरा यांत ओतून फेसाळलेली.")),
        it3("jigarthanda", "Jigarthanda (Madurai)", "जिगरठंडा (मदुरै)", "जिगरठंडा (मदुराई)", d=("Cold drink of milk, almond gum, sarsaparilla syrup and ice cream.", "दूध, बादाम गोंद, सारसपरिला शरबत और आइसक्रीम का ठंडा पेय।", "दूध, बदामाचा डिंक, सारसापरिला सरबत व आइसक्रीमचे थंड पेय.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("veshti", "Veshti", "वेष्टि", "वेष्टी", d=("White cotton wrap worn by men, often with a gold or coloured border.", "पुरुषों द्वारा पहना जाने वाला सफ़ेद सूती वस्त्र, अक्सर सुनहरी या रंगीन किनारी वाला।", "पुरुषांचे पांढरे सुती वस्त्र, अनेकदा सोनेरी किंवा रंगीत काठाचे.")),
        it3("pattu", "Kanchipuram silk saree", "कांचीपुरम रेशमी साड़ी", "कांचीपुरम रेशमी साडी", d=("Heavy mulberry-silk saree with contrasting zari borders, worn at weddings.", "विपरीत रंग की ज़री किनारी वाली भारी शहतूत रेशम की साड़ी, शादियों में पहनी जाती है।", "विरोधी रंगाच्या जरी काठाची जड तुती-रेशमी साडी, लग्नसमारंभात परिधान केली जाते.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
sect, (prim, sec, serv) = sector_table(mo["gsva2024_25_current_lakh"])
mfg = 100 * mo["gsva2024_25_current_lakh"]["manufacturing"] / mo["gsva2024_25_current_lakh"]["total"]
rows = [["Paddy", "धान", "भात", "2,158.9", "7,556.6"], ["Maize", "मक्का", "मका", "426.7", "2,989.9"], ["Black gram", "उड़द", "उडीद", "396.5", "267.8"],
        ["Jowar (cholam)", "ज्वार (चोलम)", "ज्वारी (चोलम)", "360.2", "292.7"], ["Groundnut", "मूंगफली", "भुईमूग", "351.1", "912.2"],
        ["Sugarcane", "गन्ना", "ऊस", "159.0", "17,658.1"], ["Banana", "केला", "केळी", "109.4", "4,303.9"], ["Mango", "आम", "आंबा", "145.9", "673.1"]]
crops = table("crops", L("Major crops, 2022-23", "प्रमुख फ़सलें, 2022-23", "प्रमुख पिके, 2022-23"),
              [col(L("Crop", "फ़सल", "पीक")), col(L("Area ('000 ha)", "क्षेत्र ('000 हेक्टेयर)", "क्षेत्र ('000 हेक्टर)"), "right"),
               col(L("Production ('000 tonnes)", "उत्पादन ('000 टन)", "उत्पादन ('000 टन)"), "right")],
              [[L(e, h, m), a, p] for e, h, m, a, p in rows], "tn-des", TN23, period="2022-23",
              note=L("Tamil Nadu DES, 'Tamil Nadu at a Glance'. Coconut is also grown on about 4.73 lakh ha.", "तमिलनाडु अर्थशास्त्र एवं सांख्यिकी विभाग, 'तमिलनाडु एक नज़र में'। नारियल भी लगभग 4.73 लाख हेक्टेयर में उगाया जाता है।", "तमिळनाडू अर्थशास्त्र व सांख्यिकी विभाग, 'तमिळनाडू एका दृष्टिक्षेपात'. नारळ सुमारे 4.73 लाख हेक्टरवर घेतला जातो."))
module(R, "economy", [
    prose("p1", L(
        f"Tamil Nadu is one of India's largest and most diversified State economies. In the MoSPI series its GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26, and per capita NSDP was ₹{inr(pc['FY2025-26'][0])}. Manufacturing made up about {mfg:.0f}% of GSVA in FY2024-25 — a large share by Indian standards — with cars and components around Chennai, textiles and garments in Coimbatore, Tiruppur and Erode, electronics and mobile phones at Sriperumbudur, leather at Vellore and Ambur, and matches and fireworks at Sivakasi.\n\nServices — software and IT-enabled services along Chennai's Old Mahabalipuram Road, healthcare, trade, finance and logistics through three major ports — make up about {serv:.0f}% of GSVA. Agriculture is smaller in output but employs many people; paddy dominates the Kaveri delta, and the State is a large producer of bananas, sugarcane, coconut and turmeric. The PLFS unemployment rate was 3.4% in 2025, close to the national figure, and women's labour-force participation (47.3%) was well above it.",
        f"तमिलनाडु भारत की सबसे बड़ी और सबसे विविध राज्य अर्थव्यवस्थाओं में है। मोस्पी शृंखला में वित्त वर्ष 2025-26 में इसका प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2025-26'][0])} था। वित्त वर्ष 2024-25 में जीएसवीए में विनिर्माण का हिस्सा लगभग {mfg:.0f}% था — भारतीय मानकों पर बड़ा हिस्सा — जिसमें चेन्नई के आसपास कार और पुर्ज़े, कोयंबटूर, तिरुप्पुर और इरोड में कपड़ा और परिधान, श्रीपेरुंबुदूर में इलेक्ट्रॉनिक्स और मोबाइल फ़ोन, वेल्लोर व आम्बूर में चमड़ा, और शिवकाशी में माचिस व पटाखे शामिल हैं।\n\nसेवाएँ — चेन्नई के ओल्ड महाबलीपुरम रोड पर सॉफ़्टवेयर और आईटी सेवाएँ, स्वास्थ्य, व्यापार, वित्त और तीन बड़े बंदरगाहों से लॉजिस्टिक्स — जीएसवीए का लगभग {serv:.0f}% हैं। कृषि का उत्पादन में हिस्सा छोटा है पर यह बहुत लोगों को रोज़गार देती है; कावेरी डेल्टा में धान प्रमुख है, और राज्य केला, गन्ना, नारियल और हल्दी का बड़ा उत्पादक है। 2025 में पीएलएफ़एस बेरोज़गारी दर 3.4% थी, राष्ट्रीय स्तर के क़रीब, और महिलाओं की श्रम बल भागीदारी (47.3%) उससे काफ़ी अधिक थी।",
        f"तमिळनाडू ही भारतातील सर्वांत मोठ्या आणि वैविध्यपूर्ण राज्य अर्थव्यवस्थांपैकी एक आहे. मोस्पी मालिकेनुसार आर्थिक वर्ष 2025-26 मध्ये चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी आणि दरडोई एनएसडीपी ₹{inr(pc['FY2025-26'][0])} होते. आ.व. 2024-25 मध्ये जीएसव्हीएमध्ये उत्पादन उद्योगाचा वाटा सुमारे {mfg:.0f}% होता — भारतीय मानाने मोठा — ज्यात चेन्नईभोवती मोटारी व सुटे भाग, कोइंबतूर, तिरुप्पूर व इरोडमध्ये कापड व तयार कपडे, श्रीपेरुंबुदूर येथे इलेक्ट्रॉनिक्स व मोबाइल फोन, वेल्लोर व आंबूरमध्ये चामडे, आणि शिवकाशीत काडेपेट्या व फटाके यांचा समावेश आहे.\n\nसेवाक्षेत्र — चेन्नईच्या ओल्ड महाबलीपुरम रोडवरील सॉफ्टवेअर व आयटी सेवा, आरोग्यसेवा, व्यापार, वित्त आणि तीन मोठ्या बंदरांतून होणारी लॉजिस्टिक्स — जीएसव्हीएच्या सुमारे {serv:.0f}% आहे. उत्पादनात शेतीचा वाटा लहान असला तरी ती अनेकांना रोजगार देते; कावेरी त्रिभुज प्रदेशात भात प्रमुख आहे, आणि राज्य केळी, ऊस, नारळ आणि हळदीचे मोठे उत्पादक आहे. 2025 मध्ये पीएलएफएस बेरोजगारी दर 3.4% होता — राष्ट्रीय पातळीच्या जवळ — तर स्त्रियांचा श्रमशक्ती सहभाग (47.3%) त्यापेक्षा बराच जास्त होता."),
        sources=["mospi", "plfs", "tn-des"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_TN), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_TN), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_TN), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("TN", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    crops,
    plfs_series("TN", NAME),
    lst("sectors-key", [
        it3("auto", "Automobiles and components", "ऑटोमोबाइल और पुर्ज़े", "मोटारी व सुटे भाग", d=("Chennai–Sriperumbudur–Oragadam belt.", "चेन्नई–श्रीपेरुंबुदूर–ओरगडम पट्टी।", "चेन्नई–श्रीपेरुंबुदूर–ओरगडम पट्टा.")),
        it3("textiles", "Textiles and knitwear", "कपड़ा और निटवियर", "कापड व विणलेले कपडे", d=("Spinning in Coimbatore; knitwear exports from Tiruppur; handloom silk in Kancheepuram.", "कोयंबटूर में कताई; तिरुप्पुर से निटवियर निर्यात; कांचीपुरम में हथकरघा रेशम।", "कोइंबतूरमध्ये सूतकताई; तिरुप्पूरहून विणलेल्या कपड्यांची निर्यात; कांचीपुरममध्ये हातमाग रेशीम.")),
        it3("electronics", "Electronics and mobile phones", "इलेक्ट्रॉनिक्स और मोबाइल फ़ोन", "इलेक्ट्रॉनिक्स व मोबाइल फोन", d=("Sriperumbudur and Hosur.", "श्रीपेरुंबुदूर और होसूर।", "श्रीपेरुंबुदूर व होसूर.")),
        it3("it", "Software and IT-enabled services", "सॉफ़्टवेयर और आईटी सेवाएँ", "सॉफ्टवेअर व आयटी सेवा", d=("Chennai's Old Mahabalipuram Road (IT Corridor), Coimbatore.", "चेन्नई का ओल्ड महाबलीपुरम रोड (आईटी कॉरिडोर), कोयंबटूर।", "चेन्नईचा ओल्ड महाबलीपुरम रोड (आयटी कॉरिडॉर), कोइंबतूर.")),
        it3("leather", "Leather and footwear", "चमड़ा और जूते", "चामडे व पादत्राणे", d=("Vellore, Ambur, Ranipet and Chennai.", "वेल्लोर, आम्बूर, रानीपेट और चेन्नई।", "वेल्लोर, आंबूर, राणीपेट व चेन्नई.")),
        it3("engineering", "Pumps, motors and engineering", "पंप, मोटर और इंजीनियरिंग", "पंप, मोटर व अभियांत्रिकी", d=("Coimbatore's foundries and workshops.", "कोयंबटूर की ढलाईशालाएँ और कार्यशालाएँ।", "कोइंबतूरच्या ओतशाळा व कार्यशाळा.")),
        it3("sivakasi", "Fireworks, matches and printing", "पटाखे, माचिस और छपाई", "फटाके, काडेपेट्या व छपाई", d=("Sivakasi, Virudhunagar district.", "शिवकाशी, विरुधुनगर ज़िला।", "शिवकाशी, विरुधुनगर जिल्हा.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Share of India's GDP, FY2025-26", "भारत के जीडीपी में हिस्सा, वित्त वर्ष 2025-26", "भारताच्या जीडीपीतील वाटा, आ.व. 2025-26"), "mospi", "Needs the matching all-India GDP in the same base and vintage; the comparison page shows FY2024-25."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("FDI equity inflows", "एफ़डीआई इक्विटी प्रवाह", "एफडीआय समभाग गुंतवणूक"), "dpiit", "DPIIT state-wise FDI factsheet."),
        (L("Exports by product", "उत्पादवार निर्यात", "उत्पादननिहाय निर्यात"), "dpiit", "DGCI&S state-wise export data."),
        (L("Number of factories and factory employment", "कारख़ानों की संख्या और रोज़गार", "कारखान्यांची संख्या व रोजगार"), "mospi", "Annual Survey of Industries, State tables."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Tamil Nadu has a unicameral legislature — the Legislative Council was abolished in 1986 — with a 234-member Legislative Assembly that meets at Fort St George, Chennai. The State elects 39 members to the Lok Sabha and 18 to the Rajya Sabha.\n\nFrom 1967 to 2026 the State was governed by one of two Dravidian parties, the DMK or the AIADMK. In the Assembly election held on 23 April 2026, with results on 4 May, the newly formed Tamilaga Vettri Kazhagam (TVK) won 108 seats and became the largest party, short of a majority. Its founder, C. Joseph Vijay, was sworn in as Chief Minister on 10 May 2026 with the support of the INC, CPI, CPI(M), VCK and IUML. The Governor, Rajendra Vishwanath Arlekar, has held additional charge of Tamil Nadu since 12 March 2026.",
        "तमिलनाडु में एकसदनीय विधानमंडल है — विधान परिषद 1986 में समाप्त कर दी गई — जिसमें 234 सदस्यों वाली विधानसभा है, जो चेन्नई के फ़ोर्ट सेंट जॉर्ज में बैठती है। राज्य से लोकसभा के 39 और राज्यसभा के 18 सदस्य चुने जाते हैं।\n\n1967 से 2026 तक राज्य में दो द्रविड़ दलों — द्रमुक या अन्नाद्रमुक — में से किसी एक का शासन रहा। 23 अप्रैल 2026 को हुए विधानसभा चुनाव में, जिसके परिणाम 4 मई को आए, नवगठित तमिलगा वेट्री कड़गम (टीवीके) ने 108 सीटें जीतीं और बहुमत से कुछ दूर सबसे बड़ा दल बना। इसके संस्थापक सी. जोसेफ़ विजय ने कांग्रेस, भाकपा, माकपा, वीसीके और आईयूएमएल के समर्थन से 10 मई 2026 को मुख्यमंत्री पद की शपथ ली। राज्यपाल राजेंद्र विश्वनाथ आर्लेकर 12 मार्च 2026 से तमिलनाडु का अतिरिक्त प्रभार सँभाल रहे हैं।",
        "तमिळनाडूमध्ये एकसदनी विधिमंडळ आहे — विधान परिषद 1986 मध्ये रद्द करण्यात आली — आणि 234 सदस्यांची विधानसभा चेन्नईच्या फोर्ट सेंट जॉर्जमध्ये भरते. राज्यातून लोकसभेवर 39 आणि राज्यसभेवर 18 सदस्य निवडले जातात.\n\n1967 ते 2026 या काळात राज्यात द्रमुक किंवा अण्णाद्रमुक या दोनपैकी एका द्रविड पक्षाचे सरकार होते. 23 एप्रिल 2026 रोजी झालेल्या विधानसभा निवडणुकीत, ज्याचे निकाल 4 मे रोजी लागले, नव्याने स्थापन झालेल्या तमिळगा वेट्री कळगमने (टीव्हीके) 108 जागा जिंकल्या आणि बहुमतापासून थोडा दूर राहिलेला सर्वांत मोठा पक्ष ठरला. त्याचे संस्थापक सी. जोसेफ विजय यांनी काँग्रेस, भाकप, माकप, व्हीसीके आणि आययूएमएल यांच्या पाठिंब्याने 10 मे 2026 रोजी मुख्यमंत्रिपदाची शपथ घेतली. राज्यपाल राजेंद्र विश्वनाथ आर्लेकर 12 मार्च 2026 पासून तमिळनाडूचा अतिरिक्त कार्यभार सांभाळत आहेत."),
        sources=["eci", "newsonair", "tn-lokbhavan"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    table("results", L("Legislative Assembly election, 2026 — seats won", "विधानसभा चुनाव, 2026 — जीती गई सीटें", "विधानसभा निवडणूक, 2026 — जिंकलेल्या जागा"),
          [col(L("Party", "दल", "पक्ष")), col(L("Seats", "सीटें", "जागा"), "right")],
          [["Tamilaga Vettri Kazhagam (TVK)", 108], ["Dravida Munnetra Kazhagam (DMK)", 59], ["All India Anna Dravida Munnetra Kazhagam (AIADMK)", 47],
           ["Indian National Congress (INC)", 5], ["Pattali Makkal Katchi (PMK)", 4],
           [L("Two seats each: VCK, CPI, CPI(M), IUML", "दो-दो सीटें: VCK, CPI, CPI(M), IUML", "प्रत्येकी दोन जागा: VCK, CPI, CPI(M), IUML"), 8],
           [L("One seat each: DMDK, BJP, AMMK", "एक-एक सीट: DMDK, BJP, AMMK", "प्रत्येकी एक जागा: DMDK, BJP, AMMK"), 3],
           [L("Total", "कुल", "एकूण"), 234]],
          "eci", ECI, period="2026", conf="Third-party verified",
          note=L("Seats won as declared on 4 May 2026. The Election Commission's results page loads its table dynamically and could not be read when this was compiled, so the tally was taken from news and reference compilations of the ECI result and is marked for verification. Parties are shown by seats, without colours or commentary. Several seats have since fallen vacant after resignations.",
                 "4 मई 2026 को घोषित जीती गई सीटें। चुनाव आयोग का परिणाम पेज अपनी तालिका गतिशील रूप से लोड करता है और संकलन के समय पढ़ा नहीं जा सका, इसलिए आँकड़े ईसीआई परिणाम के समाचार और संदर्भ संकलनों से लिए गए हैं और सत्यापन के लिए चिह्नित हैं। दलों को सीटों के क्रम में, बिना रंग या टिप्पणी के दिखाया गया है। इस्तीफ़ों के बाद कई सीटें खाली हुई हैं।",
                 "4 मे 2026 रोजी जाहीर झालेल्या जिंकलेल्या जागा. निवडणूक आयोगाचे निकाल पान आपली तालिका गतिमानपणे लोड करते आणि संकलनाच्या वेळी ते वाचता आले नाही, त्यामुळे आकडे ईसीआय निकालाच्या वृत्त व संदर्भ संकलनांतून घेतले असून पडताळणीसाठी चिन्हांकित आहेत. पक्ष जागांच्या क्रमाने, रंग किंवा भाष्याशिवाय दाखवले आहेत. राजीनाम्यांनंतर काही जागा रिक्त झाल्या आहेत.")),
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("assembly", "Tamil Nadu Legislative Assembly", "तमिलनाडु विधानसभा", "तमिळनाडू विधानसभा", url="https://www.assembly.tn.gov.in", src="tn-gov"),
        it3("lokbhavan", "Lok Bhavan, Tamil Nadu (Governor)", "लोक भवन, तमिलनाडु (राज्यपाल)", "लोकभवन, तमिळनाडू (राज्यपाल)", url="https://lokbhavan.tn.gov.in", src="tn-lokbhavan"),
        it3("sec", "Tamil Nadu State Election Commission", "तमिलनाडु राज्य निर्वाचन आयोग", "तमिळनाडू राज्य निवडणूक आयोग", url="https://tnsec.tn.gov.in", src="tn-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    table("local", L("Local bodies, 2022-23", "स्थानीय निकाय, 2022-23", "स्थानिक स्वराज्य संस्था, 2022-23"),
          [col(L("Type", "प्रकार", "प्रकार")), col(L("Number", "संख्या", "संख्या"), "right")],
          [[L("Municipal corporations", "नगर निगम", "महानगरपालिका"), 21], [L("Municipalities", "नगरपालिकाएँ", "नगरपालिका"), 142],
           [L("Town panchayats", "नगर पंचायतें", "नगर पंचायती"), 528], [L("Village panchayats", "ग्राम पंचायतें", "ग्रामपंचायती"), "12,525"]],
          "tn-des", TN23, period="2022-23"),
    gaps("g", [
        (L("Official 2026 results table (ECI Form-20)", "2026 का आधिकारिक परिणाम (ईसीआई फ़ॉर्म-20)", "2026 चा अधिकृत निकाल (ईसीआय फॉर्म-20)"), "eci", "Replace the compiled tally with the ECI statistical report once published."),
        (L("Leader of Opposition — formal recognition", "विपक्ष के नेता — औपचारिक मान्यता", "विरोधी पक्षनेते — औपचारिक मान्यता"), "tn-gov", "Assembly website or Gazette notification."),
        (L("Flagship welfare schemes", "प्रमुख कल्याण योजनाएँ", "प्रमुख कल्याणकारी योजना"), "tn-gov", "List with official scheme pages and current status."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Recent and ongoing infrastructure in Tamil Nadu includes Chennai Metro Phase II, the largest urban transit project in the State, whose first stretch opened in October 2026; the New Pamban rail bridge to Rameswaram, India's first vertical-lift sea bridge, opened in April 2025; ISRO's second spaceport at Kulasekarapattinam; and four more reactors at the Kudankulam nuclear plant. Each card shows its source and the date it was checked; status labels follow that source.",
        "तमिलनाडु में हालिया और जारी बुनियादी ढाँचे में चेन्नई मेट्रो चरण II शामिल है — राज्य की सबसे बड़ी शहरी परिवहन परियोजना, जिसका पहला खंड अक्टूबर 2026 में शुरू हुआ; रामेश्वरम तक नया पंबन रेल पुल, भारत का पहला वर्टिकल-लिफ़्ट समुद्री पुल, जो अप्रैल 2025 में खुला; कुलशेखरपट्टिनम में इसरो का दूसरा अंतरिक्ष प्रक्षेपण केंद्र; और कुडनकुलम परमाणु संयंत्र में चार और रिएक्टर। हर कार्ड पर उसका स्रोत और जाँच की तारीख़ है; स्थिति उसी स्रोत के अनुसार है।",
        "तमिळनाडूतील अलीकडच्या व चालू पायाभूत प्रकल्पांत चेन्नई मेट्रो टप्पा II — राज्यातील सर्वांत मोठा नागरी वाहतूक प्रकल्प, ज्याचा पहिला भाग ऑक्टोबर 2026 मध्ये सुरू झाला; रामेश्वरमपर्यंतचा नवा पंबन रेल्वे पूल, भारतातील पहिला उभा उचलला जाणारा सागरी पूल, जो एप्रिल 2025 मध्ये खुला झाला; कुलशेखरपट्टिनम येथील इस्रोचे दुसरे अंतराळ प्रक्षेपण केंद्र; आणि कुडनकुलम अणुऊर्जा प्रकल्पातील आणखी चार अणुभट्ट्या यांचा समावेश आहे. प्रत्येक कार्डावर स्रोत आणि तपासणीची तारीख आहे; स्थिती त्याच स्रोतानुसार आहे."),
        sources=["pmindia", "newsonair", "isro"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Chennai Metro Phase II — corridor-wise progress", "चेन्नई मेट्रो चरण II — कॉरिडोरवार प्रगति", "चेन्नई मेट्रो टप्पा II — मार्गिकानिहाय प्रगती"), "tn-gov", "CMRL project status page."),
        (L("Kudankulam Units 3–6 — official status", "कुडनकुलम इकाइयाँ 3–6 — आधिकारिक स्थिति", "कुडनकुलम युनिट 3–6 — अधिकृत स्थिती"), "npcil", "NPCIL or DAE status page to replace the news citation."),
        (L("Parandur greenfield airport — official status", "परंदूर ग्रीनफ़ील्ड हवाई अड्डा — आधिकारिक स्थिति", "परंदूर ग्रीनफिल्ड विमानतळ — अधिकृत स्थिती"), "civil-aviation", "MoCA / TIDCO page."),
        (L("State vision document", "राज्य दृष्टि दस्तावेज़", "राज्य दृष्टी दस्तऐवज"), "tn-gov", "State Planning Commission."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Chennai is the hub: its international airport is one of the busiest in India, and the city has a metro, suburban rail and the elevated MRTS line. Other airports serve Coimbatore, Madurai, Tiruchirappalli, Thoothukudi and Salem. Three major ports — Chennai, Kamarajar (Ennore) and V. O. Chidambaranar (Thoothukudi) — handle containers, coal, cars and bulk cargo.\n\nThe rail network links every district headquarters, and the Nilgiri Mountain Railway, a UNESCO World Heritage line, climbs from Mettupalayam to Ooty on a rack-and-pinion track. The State-owned transport corporations run one of India's largest public bus fleets, and the East Coast Road runs along the shore from Chennai to Puducherry and beyond.",
        "चेन्नई केंद्र है: इसका अंतरराष्ट्रीय हवाई अड्डा भारत के सबसे व्यस्त हवाई अड्डों में है, और शहर में मेट्रो, उपनगरीय रेल और ऊँची एमआरटीएस लाइन है। अन्य हवाई अड्डे कोयंबटूर, मदुरै, तिरुचिरापल्ली, थूथुकुडी और सेलम में हैं। तीन बड़े बंदरगाह — चेन्नई, कामराजर (एन्नोर) और वी. ओ. चिदंबरनार (थूथुकुडी) — कंटेनर, कोयला, कारें और थोक माल संभालते हैं।\n\nरेल नेटवर्क हर ज़िला मुख्यालय को जोड़ता है, और यूनेस्को विश्व धरोहर नीलगिरि पर्वतीय रेल रैक-एंड-पिनियन पटरी पर मेट्टुपालयम से ऊटी तक चढ़ती है। राज्य की परिवहन निगमें भारत के सबसे बड़े सार्वजनिक बस बेड़ों में से एक चलाती हैं, और ईस्ट कोस्ट रोड तट के साथ चेन्नई से पुदुच्चेरी और आगे तक जाती है।",
        "चेन्नई हे केंद्र आहे: इथले आंतरराष्ट्रीय विमानतळ भारतातील सर्वांत गजबजलेल्या विमानतळांपैकी एक आहे, आणि शहरात मेट्रो, उपनगरी रेल्वे व उन्नत एमआरटीएस मार्ग आहे. इतर विमानतळ कोइंबतूर, मदुराई, तिरुचिरापल्ली, थुथुकुडी आणि सेलम येथे आहेत. तीन मोठी बंदरे — चेन्नई, कामराजर (एन्नोर) आणि व्ही. ओ. चिदंबरनार (थुथुकुडी) — कंटेनर, कोळसा, मोटारी आणि घाऊक माल हाताळतात.\n\nरेल्वे जाळे प्रत्येक जिल्हा मुख्यालय जोडते, आणि युनेस्को जागतिक वारसा असलेली निलगिरी पर्वतीय रेल्वे दातेरी रुळांवरून मेट्टुपालयमपासून ऊटीपर्यंत चढते. राज्याच्या परिवहन महामंडळांचा सार्वजनिक बसताफा भारतातील सर्वांत मोठ्यांपैकी एक आहे, आणि ईस्ट कोस्ट रोड किनाऱ्यालगत चेन्नईपासून पुदुच्चेरी व पुढे जातो."),
        conf="Editorial"),
    lst("airports", [
        it3("maa", "Chennai International Airport", "चेन्नई अंतरराष्ट्रीय हवाई अड्डा", "चेन्नई आंतरराष्ट्रीय विमानतळ", m=("MAA", "MAA", "MAA")),
        it3("cjb", "Coimbatore International Airport", "कोयंबटूर अंतरराष्ट्रीय हवाई अड्डा", "कोइंबतूर आंतरराष्ट्रीय विमानतळ", m=("CJB", "CJB", "CJB")),
        it3("ixm", "Madurai Airport", "मदुरै हवाई अड्डा", "मदुराई विमानतळ", m=("IXM", "IXM", "IXM")),
        it3("trz", "Tiruchirappalli International Airport", "तिरुचिरापल्ली अंतरराष्ट्रीय हवाई अड्डा", "तिरुचिरापल्ली आंतरराष्ट्रीय विमानतळ", m=("TRZ", "TRZ", "TRZ")),
        it3("tcr", "Thoothukudi Airport", "थूथुकुडी हवाई अड्डा", "थुथुकुडी विमानतळ", m=("TCR", "TCR", "TCR")),
        it3("sxv", "Salem Airport", "सेलम हवाई अड्डा", "सेलम विमानतळ", m=("SXV", "SXV", "SXV")),
    ], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
    lst("ports", [
        it3("chennai", "Chennai Port", "चेन्नई बंदरगाह", "चेन्नई बंदर"), it3("kamarajar", "Kamarajar Port (Ennore)", "कामराजर बंदरगाह (एन्नोर)", "कामराजर बंदर (एन्नोर)"),
        it3("voc", "V. O. Chidambaranar Port (Thoothukudi)", "वी. ओ. चिदंबरनार बंदरगाह (थूथुकुडी)", "व्ही. ओ. चिदंबरनार बंदर (थुथुकुडी)"),
    ], layout="chips", title=L("Major ports", "बड़े बंदरगाह", "मोठी बंदरे"), conf="Editorial"),
    gaps("g", [
        (L("National highway length", "राष्ट्रीय राजमार्ग की लंबाई", "राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Railway route length", "रेलवे मार्ग की लंबाई", "रेल्वे मार्गाची लांबी"), "railways", "Indian Railways Year Book."),
        (L("Port cargo traffic", "बंदरगाह माल यातायात", "बंदर मालवाहतूक"), "india-gov", "Ministry of Ports, Shipping and Waterways statistics."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Tamil Nadu has one of India's most varied power systems. Wind farms line the passes at Muppandal near Kanniyakumari and around Palakkad Gap and Theni, where the winds funnel through the Western Ghats, and large solar parks have been built in the southern districts such as Ramanathapuram. Coal-fired stations run at Ennore, North Chennai, Mettur and Thoothukudi, the Kudankulam nuclear plant has two 1,000 MW units in operation with four more under construction, and the Kalpakkam site near Chennai hosts nuclear reactors and research facilities. Hydropower comes from the Nilgiris and the Kaveri. State-owned companies under TNEB Limited generate and distribute much of the State's power.",
        "तमिलनाडु की बिजली व्यवस्था भारत में सबसे विविध व्यवस्थाओं में है। कन्याकुमारी के पास मुप्पंदल और पालक्काड गैप व थेनी के आसपास के दर्रों में, जहाँ हवाएँ पश्चिमी घाट से होकर तेज़ होती हैं, पवन फ़ार्मों की कतारें हैं, और रामनाथपुरम जैसे दक्षिणी ज़िलों में बड़े सौर पार्क बने हैं। कोयला आधारित संयंत्र एन्नोर, उत्तर चेन्नई, मेट्टूर और थूथुकुडी में हैं; कुडनकुलम परमाणु संयंत्र में 1,000 मेगावाट की दो इकाइयाँ चल रही हैं और चार और बन रही हैं; और चेन्नई के पास कल्पक्कम में परमाणु रिएक्टर और शोध सुविधाएँ हैं। जलविद्युत नीलगिरि और कावेरी से आती है। टीएनईबी लिमिटेड के अधीन राज्य की कंपनियाँ राज्य की बिजली का बड़ा हिस्सा बनाती और वितरित करती हैं।",
        "तमिळनाडूची वीजव्यवस्था भारतातील सर्वांत वैविध्यपूर्ण व्यवस्थांपैकी एक आहे. कन्याकुमारीजवळील मुप्पंदल आणि पालक्काड गॅप व थेनीच्या खिंडींत — जिथे पश्चिम घाटातून वारे वेगाने वाहतात — पवनचक्क्यांच्या रांगा आहेत, आणि रामनाथपुरमसारख्या दक्षिणेकडील जिल्ह्यांत मोठी सौर उद्याने उभी राहिली आहेत. कोळशावरील केंद्रे एन्नोर, उत्तर चेन्नई, मेट्टूर आणि थुथुकुडी येथे आहेत; कुडनकुलम अणुऊर्जा प्रकल्पात 1,000 मेगावॉटची दोन युनिट्स चालू असून आणखी चार उभारली जात आहेत; आणि चेन्नईजवळील कल्पक्कम येथे अणुभट्ट्या व संशोधन सुविधा आहेत. जलविद्युत निलगिरी व कावेरीतून मिळते. टीएनईबी लिमिटेडअंतर्गत राज्याच्या मालकीच्या कंपन्या राज्यातील विजेचा मोठा भाग निर्माण करतात व वितरित करतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report (portal blocked automated access)."),
        (L("Wind and solar capacity", "पवन और सौर क्षमता", "पवन व सौर क्षमता"), "mnre", "MNRE state-wise RE capacity."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Chennai is one of India's main software and IT-services centres. TIDEL Park, opened in 2000, anchored the IT Corridor along Old Mahabalipuram Road, which now runs past campuses of large Indian and multinational firms; Coimbatore, Madurai and Tiruchirappalli have smaller IT parks. Electronics manufacturing — including mobile-phone assembly at Sriperumbudur and Hosur — has grown quickly. Chennai is also a landing point for international submarine data cables. The Tamil Nadu e-Governance Agency and the State's Tamil Nadu Startup and Innovation Mission (StartupTN) support digital services and young companies.",
        "चेन्नई भारत के प्रमुख सॉफ़्टवेयर और आईटी सेवा केंद्रों में है। 2000 में खुले टाइडल पार्क ने ओल्ड महाबलीपुरम रोड पर आईटी कॉरिडोर की नींव रखी, जहाँ अब बड़ी भारतीय और बहुराष्ट्रीय कंपनियों के परिसर हैं; कोयंबटूर, मदुरै और तिरुचिरापल्ली में छोटे आईटी पार्क हैं। इलेक्ट्रॉनिक्स विनिर्माण — श्रीपेरुंबुदूर और होसूर में मोबाइल फ़ोन असेंबली सहित — तेज़ी से बढ़ा है। चेन्नई अंतरराष्ट्रीय समुद्री डेटा केबलों का लैंडिंग बिंदु भी है। तमिलनाडु ई-गवर्नेंस एजेंसी और राज्य का तमिलनाडु स्टार्टअप एवं इनोवेशन मिशन (स्टार्टअपटीएन) डिजिटल सेवाओं और नई कंपनियों को सहायता देते हैं।",
        "चेन्नई हे भारतातील प्रमुख सॉफ्टवेअर व आयटी सेवा केंद्रांपैकी एक आहे. 2000 मध्ये सुरू झालेल्या टायडल पार्कने ओल्ड महाबलीपुरम रोडवरील आयटी कॉरिडॉरचा पाया घातला, जिथे आता मोठ्या भारतीय व बहुराष्ट्रीय कंपन्यांची संकुले आहेत; कोइंबतूर, मदुराई व तिरुचिरापल्लीत लहान आयटी पार्क आहेत. इलेक्ट्रॉनिक्स उत्पादन — श्रीपेरुंबुदूर व होसूर येथील मोबाइल फोन जुळणीसह — झपाट्याने वाढले आहे. चेन्नई हे आंतरराष्ट्रीय समुद्राखालील डेटा केबल्सचे किनारी स्थानकही आहे. तमिळनाडू ई-गव्हर्नन्स एजन्सी आणि राज्याचे तमिळनाडू स्टार्टअप व इनोव्हेशन मिशन (स्टार्टअपटीएन) डिजिटल सेवा व नव्या कंपन्यांना पाठबळ देतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI Indian Telecom Services Performance Indicators (Tamil Nadu circle)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
        (L("Software and electronics exports", "सॉफ़्टवेयर और इलेक्ट्रॉनिक्स निर्यात", "सॉफ्टवेअर व इलेक्ट्रॉनिक्स निर्यात"), "india-gov", "STPI / MeitY state data."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("TN", NAME)
module(R, "education", [
    prose("p1", L(
        "Tamil Nadu has one of the highest higher-education enrolment rates among the large States. The 2021-22 AISHE survey counted 62 universities and 2,829 colleges, and a gross enrolment ratio (ages 18–23) of 47.0%, against 28.4% nationally; women's GER (47.3%) was slightly higher than men's (46.8%). The State is known for engineering and medical colleges and for its long-running school meal programme, which began in Madras city schools in the 1920s and was extended State-wide as the noon-meal scheme in 1982; a breakfast scheme for primary pupils was added in 2022.\n\nNational institutions include IIT Madras, NIT Tiruchirappalli and IIM Tiruchirappalli; the University of Madras, founded in 1857, is among the oldest modern universities in India.",
        "बड़े राज्यों में तमिलनाडु की उच्च शिक्षा नामांकन दर सबसे अधिक में है। 2021-22 के एआईएसएचई सर्वेक्षण में 62 विश्वविद्यालय और 2,829 कॉलेज गिने गए, और सकल नामांकन अनुपात (18–23 आयु) 47.0% था, जबकि राष्ट्रीय स्तर 28.4% है; महिलाओं का जीईआर (47.3%) पुरुषों (46.8%) से थोड़ा अधिक था। राज्य इंजीनियरिंग और मेडिकल कॉलेजों और अपने लंबे स्कूली भोजन कार्यक्रम के लिए जाना जाता है, जो 1920 के दशक में मद्रास शहर के स्कूलों में शुरू हुआ और 1982 में दोपहर भोजन योजना के रूप में पूरे राज्य में फैला; 2022 में प्राथमिक कक्षाओं के लिए नाश्ता योजना जोड़ी गई।\n\nराष्ट्रीय संस्थानों में आईआईटी मद्रास, एनआईटी तिरुचिरापल्ली और आईआईएम तिरुचिरापल्ली हैं; 1857 में स्थापित मद्रास विश्वविद्यालय भारत के सबसे पुराने आधुनिक विश्वविद्यालयों में है।",
        "मोठ्या राज्यांमध्ये तमिळनाडूचा उच्चशिक्षण नोंदणी दर सर्वाधिक दरांपैकी आहे. 2021-22 च्या एआयएसएचई सर्वेक्षणात 62 विद्यापीठे आणि 2,829 महाविद्यालये नोंदली गेली, आणि एकूण नोंदणी गुणोत्तर (18–23 वय) 47.0% होते, तर राष्ट्रीय प्रमाण 28.4%; स्त्रियांचे जीईआर (47.3%) पुरुषांपेक्षा (46.8%) किंचित जास्त होते. अभियांत्रिकी व वैद्यकीय महाविद्यालये आणि दीर्घकाळ चालणारी शालेय आहार योजना यांसाठी राज्य ओळखले जाते — ती 1920 च्या दशकात मद्रास शहरातील शाळांत सुरू झाली आणि 1982 मध्ये माध्यान्ह भोजन योजना म्हणून राज्यभर विस्तारली; 2022 मध्ये प्राथमिक विद्यार्थ्यांसाठी न्याहारी योजना जोडली गेली.\n\nराष्ट्रीय संस्थांत आयआयटी मद्रास, एनआयटी तिरुचिरापल्ली आणि आयआयएम तिरुचिरापल्ली यांचा समावेश आहे; 1857 मध्ये स्थापन झालेले मद्रास विद्यापीठ हे भारतातील सर्वांत जुन्या आधुनिक विद्यापीठांपैकी एक आहे."),
        sources=["aishe"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("iitm", "IIT Madras", "आईआईटी मद्रास", "आयआयटी मद्रास", m=("Chennai", "चेन्नई", "चेन्नई")),
        it3("nitt", "NIT Tiruchirappalli", "एनआईटी तिरुचिरापल्ली", "एनआयटी तिरुचिरापल्ली", m=("Tiruchirappalli", "तिरुचिरापल्ली", "तिरुचिरापल्ली")),
        it3("iimt", "IIM Tiruchirappalli", "आईआईएम तिरुचिरापल्ली", "आयआयएम तिरुचिरापल्ली", m=("Tiruchirappalli", "तिरुचिरापल्ली", "तिरुचिरापल्ली")),
        it3("unom", "University of Madras", "मद्रास विश्वविद्यालय", "मद्रास विद्यापीठ", m=("Chennai, 1857", "चेन्नई, 1857", "चेन्नई, 1857")),
        it3("anna", "Anna University", "अन्ना विश्वविद्यालय", "अण्णा विद्यापीठ", m=("Chennai", "चेन्नई", "चेन्नई")),
        it3("cutn", "Central University of Tamil Nadu", "तमिलनाडु केंद्रीय विश्वविद्यालय", "तमिळनाडू केंद्रीय विद्यापीठ", m=("Thiruvarur", "तिरुवारूर", "तिरुवारूर")),
        it3("kalakshetra", "Kalakshetra Foundation", "कलाक्षेत्र फ़ाउंडेशन", "कलाक्षेत्र फाउंडेशन", m=("Chennai; arts", "चेन्नई; कलाएँ", "चेन्नई; कला")),
    ], title=L("National institutions (selected)", "राष्ट्रीय संस्थान (चयनित)", "राष्ट्रीय संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Dropout rates by level", "स्तरवार ड्रॉपआउट दर", "स्तरनिहाय गळती दर"), "udise", "UDISE+."),
        (L("Noon-meal and breakfast scheme coverage", "दोपहर भोजन और नाश्ता योजना कवरेज", "माध्यान्ह भोजन व न्याहारी योजना व्याप्ती"), "tn-gov", "School Education Department; link the scheme notifications."),
        (L("NIRF-ranked institutions", "एनआईआरएफ़ रैंक वाले संस्थान", "एनआयआरएफ क्रमवारीतील संस्था"), "nirf", "Latest NIRF list filtered to Tamil Nadu."),
    ]),
])

# ---------------- O. Health ----------------
srs = NF["SRS_2021_PIB_PRID2128024"]
def srsdp(v, unit, period, note=None, level="state"):
    return dp(v, unit, period, "survey" if "-" in period else "calendar", "srs", SRS, note=note, level=level)
module(R, "health", [
    prose("p1", L(
        "Tamil Nadu has strong public health outcomes. In the Sample Registration System, its maternal mortality was 49 per lakh live births in 2019-21 (India 93) and under-five mortality 14 per 1,000 live births in 2021 (India 31); it was one of only six States and UTs that had already met the SDG target for neonatal mortality. Almost all births (99.6% in NFHS-5) take place in health facilities, and child stunting fell from 27.1% in NFHS-4 to 25.0% in NFHS-5.\n\nThe public system is built around primary health centres and district hospitals, with a large network of government medical colleges; Chennai and Vellore are major destinations for specialist care, including for patients from other States and countries. Life expectancy at birth was 73.2 years in 2016-20.",
        "तमिलनाडु के सार्वजनिक स्वास्थ्य परिणाम मज़बूत हैं। नमूना पंजीकरण प्रणाली में यहाँ 2019-21 में मातृ मृत्यु अनुपात प्रति लाख जीवित जन्म पर 49 (भारत 93) और 2021 में पाँच वर्ष से कम आयु की मृत्यु दर प्रति 1,000 जीवित जन्म पर 14 (भारत 31) थी; यह उन केवल छह राज्यों/केंद्र शासित प्रदेशों में था जो नवजात मृत्यु दर का एसडीजी लक्ष्य पहले ही पा चुके थे। लगभग सभी प्रसव (एनएफ़एचएस-5 में 99.6%) स्वास्थ्य संस्थानों में होते हैं, और बच्चों में ठिगनापन एनएफ़एचएस-4 के 27.1% से घटकर एनएफ़एचएस-5 में 25.0% रह गया।\n\nसार्वजनिक व्यवस्था प्राथमिक स्वास्थ्य केंद्रों और ज़िला अस्पतालों पर आधारित है, साथ में सरकारी मेडिकल कॉलेजों का बड़ा नेटवर्क है; चेन्नई और वेल्लोर विशेषज्ञ इलाज के बड़े केंद्र हैं, जहाँ दूसरे राज्यों और देशों से भी मरीज़ आते हैं। 2016-20 में जन्म के समय जीवन प्रत्याशा 73.2 वर्ष थी।",
        "तमिळनाडूचे सार्वजनिक आरोग्य परिणाम भक्कम आहेत. नमुना नोंदणी पद्धतीनुसार येथे 2019-21 मध्ये मातामृत्यू प्रमाण दर लाख जिवंत जन्मांमागे 49 (भारत 93) आणि 2021 मध्ये पाच वर्षांखालील मृत्युदर दर 1,000 जिवंत जन्मांमागे 14 (भारत 31) होता; नवजात मृत्युदराचे एसडीजी उद्दिष्ट आधीच गाठलेल्या केवळ सहा राज्य/केंद्रशासित प्रदेशांपैकी हे एक होते. जवळपास सर्व प्रसूती (एनएफएचएस-5 मध्ये 99.6%) आरोग्य संस्थांत होतात, आणि मुलांमधील खुजेपणा एनएफएचएस-4 मधील 27.1% वरून एनएफएचएस-5 मध्ये 25.0% वर आला.\n\nसार्वजनिक व्यवस्था प्राथमिक आरोग्य केंद्रे आणि जिल्हा रुग्णालयांवर उभी आहे, सोबत सरकारी वैद्यकीय महाविद्यालयांचे मोठे जाळे आहे; चेन्नई व वेल्लोर ही विशेषज्ञ उपचारांची मोठी केंद्रे असून इतर राज्ये व देशांतूनही रुग्ण येतात. 2016-20 मध्ये जन्मतः आयुर्मान 73.2 वर्षे होते."),
        sources=["srs", "nfhs", "tn-des"], conf="Official"),
    facts("srs", [
        fact("mmr", L("Maternal mortality ratio", "मातृ मृत्यु अनुपात", "मातामृत्यू प्रमाण"), srsdp(srs["TN"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", "SRS special bulletin, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", level="national")),
        fact("u5mr", L("Under-five mortality rate", "पाँच वर्ष से कम आयु की मृत्यु दर", "पाच वर्षांखालील मृत्युदर"), srsdp(srs["TN"]["U5MR"], "per 1,000 live births", "2021", "SRS 2021, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["U5MR"], "per 1,000 live births", "2021", level="national")),
        fact("nmr", L("Neonatal mortality rate", "नवजात मृत्यु दर", "नवजात मृत्युदर"), srsdp(srs["TN"]["NMR"], "per 1,000 live births", "2021"), "number", "lower-is-better",
             national=srsdp(srs["IN"]["NMR"], "per 1,000 live births", "2021", level="national")),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(73.2, "years", "2016-20", "survey", "srs", TN23, note="SRS abridged life table 2016-20, as published by Tamil Nadu DES (male 71.0, female 75.5)."), "number", "higher-is-better"),
    ], title=L("Mortality (Sample Registration System)", "मृत्यु दर (नमूना पंजीकरण प्रणाली)", "मृत्युदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("TN"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Infant mortality rate (State)", "शिशु मृत्यु दर (राज्य)", "अर्भक मृत्युदर (राज्य)"), "srs", "SRS Statistical Report; the State's two published figures for 2020 (12.5 and 13) differ, so neither is shown."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
        (L("Anaemia and immunisation", "एनीमिया और टीकाकरण", "रक्तक्षय व लसीकरण"), "nfhs", "NFHS-5 State fact sheet."),
    ]),
])
print("tn mod2 ok")
