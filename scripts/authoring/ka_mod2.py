"""Karnataka modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-KA"
ECI = "https://results.eci.gov.in/ResultAcGenMay2023/partywiseresult-S10.htm"
KAES24 = "https://data.opencity.in/dataset/90aaf1df-999b-4d84-a0d0-443aee3d0bfc/resource/b96f076f-9b1c-48b2-bc1b-f081f1beca84/download/economic_survey_2023-24_finalenglish_compressed.pdf"
KAES26 = "https://data.opencity.in/dataset/699b7b8d-3813-4e44-8d70-cfdf1414ee85/resource/ee584e22-2c78-4a54-9054-74db776a9a53/download/economic_survey_2025-26_english_finalmpdf_1772796504.pdf"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab82.pdf"
NOTE_KA = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 14 Oct 2026. "
           "FY2025-26 is the latest year published for Karnataka and may be revised.")
mo = research("mospi_ka.json")
NAME = L("Karnataka", "कर्नाटक", "कर्नाटक")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Kannada has one of India's longest literary traditions, from the 9th-century Kavirajamarga and the poets Pampa, Ranna and Ponna to the 12th-century vachanas of Basavanna and Akka Mahadevi and the songs of the Haridasas, Purandara Dasa and Kanaka Dasa. Kannada writers have won eight Jnanpith Awards, among the most for any Indian language. Purandara Dasa is called the father of Carnatic music, and the north of the State, around Dharwad, produced some of the greatest Hindustani musicians.\n\nYakshagana, a night-long dance-drama with rich costumes and a sung narrative, is the signature art of the coast, where the bhuta kola spirit rituals and kambala buffalo races are also held. Mysore painting, Channapatna lacquer toys, Bidriware, sandalwood carving, Ilkal and Molakalmuru saris and Mysore silk are among the State's crafts.",
        "कन्नड़ की साहित्यिक परंपरा भारत की सबसे लंबी परंपराओं में है — नौवीं सदी के कविराजमार्ग और कवि पंप, रन्न व पोन्न से लेकर 12वीं सदी के बसवण्णा और अक्क महादेवी के वचनों तथा हरिदासों — पुरंदर दास और कनक दास — के गीतों तक। कन्नड़ लेखकों ने आठ ज्ञानपीठ पुरस्कार जीते हैं, जो किसी भी भारतीय भाषा के लिए सबसे अधिक में से हैं। पुरंदर दास को कर्नाटक संगीत का पितामह कहा जाता है, और राज्य के उत्तर में धारवाड़ के आसपास से कुछ सबसे बड़े हिंदुस्तानी संगीतकार निकले।\n\nयक्षगान — भव्य वेशभूषा और गाए जाने वाले कथानक वाला रात भर चलने वाला नृत्य-नाट्य — तट की पहचान है, जहाँ भूत कोला अनुष्ठान और कंबला भैंसा दौड़ भी होते हैं। मैसूर चित्रकला, चन्नपट्टण के लाख के खिलौने, बिदरी शिल्प, चंदन की नक़्क़ाशी, इलकल और मोलकालमुरु साड़ियाँ और मैसूर सिल्क राज्य के शिल्पों में हैं।",
        "कन्नडची साहित्यपरंपरा भारतातील सर्वांत दीर्घ परंपरांपैकी आहे — नवव्या शतकातील कविराजमार्ग आणि पंप, रन्न व पोन्न या कवींपासून बाराव्या शतकातील बसवण्णा व अक्कमहादेवी यांच्या वचनांपर्यंत आणि हरिदासांच्या — पुरंदरदास व कनकदास — गीतांपर्यंत. कन्नड लेखकांनी आठ ज्ञानपीठ पुरस्कार मिळवले आहेत — कोणत्याही भारतीय भाषेसाठी सर्वाधिकांपैकी. पुरंदरदासांना कर्नाटक संगीताचे पितामह म्हटले जाते, आणि राज्याच्या उत्तरेकडील धारवाड परिसराने काही श्रेष्ठ हिंदुस्तानी गायक दिले.\n\nयक्षगान — भरजरी वेशभूषा आणि गायलेल्या कथानकासह रात्रभर चालणारे नृत्यनाट्य — ही किनारपट्टीची ओळख आहे; तिथे भूत कोला विधी आणि कंबळा म्हशींच्या शर्यतीही होतात. म्हैसूर चित्रशैली, चन्नपट्टणची लाखेची खेळणी, बिदरी कला, चंदनाचे कोरीवकाम, इळकल व मोळकाल्मुरू साड्या आणि म्हैसूर सिल्क ही राज्याची हस्तकला आहे."),
        conf="Editorial"),
    lst("festivals", [
        fest("dasara", "Mysuru Dasara (Nadahabba)", "मैसूरु दशहरा (नाडहब्ब)", "म्हैसूरु दसरा (नाडहब्ब)", ("September–October", "सितंबर–अक्टूबर", "सप्टेंबर–ऑक्टोबर"),
             ("The State festival: ten days of events ending in the Jamboo Savari elephant procession.", "राज्य उत्सव: दस दिनों के आयोजन, जिनका समापन जंबू सवारी हाथी जुलूस से होता है।", "राज्योत्सव: दहा दिवसांचे कार्यक्रम, जंबू सवारी हत्तींच्या मिरवणुकीने सांगता.")),
        fest("ugadi", "Ugadi", "उगादि", "उगादी", ("March–April", "मार्च–अप्रैल", "मार्च–एप्रिल"),
             ("New Year, marked with bevu–bella (neem and jaggery).", "नववर्ष, बेवु–बेल्ला (नीम और गुड़) के साथ।", "नववर्ष, बेवु–बेल्ला (कडुलिंब व गूळ) सह.")),
        fest("rajyotsava", "Kannada Rajyotsava", "कन्नड़ राज्योत्सव", "कन्नड राज्योत्सव", ("1 November", "1 नवंबर", "1 नोव्हेंबर"),
             ("Formation day of the State.", "राज्य का स्थापना दिवस।", "राज्याचा स्थापना दिन.")),
        fest("karaga", "Bengaluru Karaga", "बेंगलूरु करगा", "बंगळूरु करगा", ("March–April", "मार्च–अप्रैल", "मार्च–एप्रिल"),
             ("Night procession of the Dharmaraya temple.", "धर्मराय मंदिर की रात्रिकालीन शोभायात्रा।", "धर्मराय मंदिराची रात्रीची मिरवणूक.")),
        fest("kambala", "Kambala", "कंबला", "कंबळा", ("November–March", "नवंबर–मार्च", "नोव्हेंबर–मार्च"),
             ("Buffalo races in flooded paddy fields of Dakshina Kannada and Udupi.", "दक्षिण कन्नड़ और उडुपी के पानी भरे धान के खेतों में भैंसों की दौड़।", "दक्षिण कन्नड व उडुपीच्या पाण्याने भरलेल्या भातखाचरांत म्हशींच्या शर्यती.")),
        fest("hampi", "Hampi Utsav", "हम्पी उत्सव", "हंपी उत्सव", ("Winter", "सर्दियाँ", "हिवाळा"),
             ("Music and dance among the ruins.", "खंडहरों के बीच संगीत और नृत्य।", "अवशेषांच्या सान्निध्यात संगीत व नृत्य.")),
        fest("ganesha", "Gowri–Ganesha", "गौरी–गणेश", "गौरी–गणेश", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Household and public celebrations across the State.", "पूरे राज्य में घरेलू और सार्वजनिक उत्सव।", "राज्यभर घरगुती व सार्वजनिक उत्सव.")),
        fest("eid", "Eid and Christmas", "ईद और क्रिसमस", "ईद व नाताळ", ("Lunar calendar / 25 December", "चंद्र कैलेंडर / 25 दिसंबर", "चांद्र दिनदर्शिका / 25 डिसेंबर"),
             ("Widely celebrated, especially in Bengaluru, the coast and the north.", "व्यापक रूप से मनाए जाते हैं, ख़ासकर बेंगलूरु, तट और उत्तर में।", "मोठ्या प्रमाणावर साजरे होतात, विशेषतः बंगळूरु, किनारपट्टी व उत्तरेत.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("yakshagana", "Yakshagana", "यक्षगान", "यक्षगान"), it3("dollu", "Dollu Kunitha", "डोल्लु कुनिता", "डोल्लू कुणिता"),
        it3("carnatic", "Carnatic music", "कर्नाटक संगीत", "कर्नाटक संगीत"), it3("hindustani", "Hindustani music (Dharwad)", "हिंदुस्तानी संगीत (धारवाड़)", "हिंदुस्तानी संगीत (धारवाड)"),
        it3("mysorepainting", "Mysore painting", "मैसूर चित्रकला", "म्हैसूर चित्रशैली"), it3("channapatna", "Channapatna toys", "चन्नपट्टण खिलौने", "चन्नपट्टण खेळणी"),
        it3("bidri", "Bidriware", "बिदरी शिल्प", "बिदरी कला"), it3("kasuti", "Kasuti embroidery", "कसूती कढ़ाई", "कसूती भरतकाम"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("bisibele", "Bisi bele bath", "बिसी बेले भात", "बिसी बेळे भात", d=("Rice, lentils and vegetables cooked with a spiced tamarind masala.", "इमली और मसालों के साथ पकाए चावल, दाल और सब्ज़ियाँ।", "चिंच व मसाल्यांसह शिजवलेला भात, डाळ व भाज्या.")),
        it3("masaladosa", "Masala dosa and filter coffee", "मसाला डोसा और फ़िल्टर कॉफ़ी", "मसाला डोसा व फिल्टर कॉफी", d=("Bengaluru and Mysuru breakfast classics.", "बेंगलूरु और मैसूरु का क्लासिक नाश्ता।", "बंगळूरु व म्हैसूरुची खास न्याहारी.")),
        it3("ragi", "Ragi mudde", "रागी मुद्दे", "नाचणी मुद्दे", d=("Finger-millet balls eaten with saaru (curry), staple of the south.", "रागी (मंडुआ) के गोले, सारु (करी) के साथ — दक्षिण का मुख्य भोजन।", "नाचणीचे गोळे, सारू (आमटी) सोबत — दक्षिणेकडील मुख्य अन्न.")),
        it3("jolada", "Jolada rotti meal", "जोलद रोट्टी थाली", "जोळद रोट्टी थाळी", d=("Jowar flatbread with ennegai brinjal and chutneys, from the north.", "उत्तर की ज्वार की रोटी, एन्नेगायी बैंगन और चटनियों के साथ।", "उत्तरेकडील ज्वारीची भाकरी, एण्णेगायी वांगे व चटण्यांसह.")),
        it3("mysorepak", "Mysore pak and Dharwad pedha", "मैसूर पाक और धारवाड़ पेड़ा", "म्हैसूर पाक व धारवाड पेढा", d=("Gram-flour and ghee sweet; caramelised milk sweet.", "बेसन और घी की मिठाई; भुने दूध की मिठाई।", "बेसन-तुपाची मिठाई; आटवलेल्या दुधाची मिठाई.")),
        it3("coastal", "Mangalorean fish curry and neer dosa", "मंगलूरी मछली करी और नीर डोसा", "मंगळुरी माशांची आमटी व नीर डोसा", d=("Coconut-based curries with thin rice crêpes.", "नारियल वाली करी और पतले चावल के डोसे।", "नारळाच्या आमटीसोबत तांदळाचे पातळ डोसे.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("silk", "Mysore silk saree", "मैसूर सिल्क साड़ी", "म्हैसूर सिल्क साडी", d=("Pure silk with gold zari, worn at weddings and festivals.", "सुनहरी ज़री वाली शुद्ध रेशमी साड़ी, शादियों और त्योहारों में पहनी जाती है।", "सोनेरी जरीची शुद्ध रेशमी साडी, लग्नात व सणासुदीला परिधान केली जाते.")),
        it3("peta", "Mysore peta", "मैसूर पेटा", "म्हैसूर पेटा", d=("Ceremonial turban, given as a mark of honour.", "रस्मी पगड़ी, सम्मान के रूप में भेंट की जाती है।", "समारंभातील पगडी, सन्मानाचे प्रतीक म्हणून दिली जाते.")),
        it3("kodava", "Kodava dress", "कोडव पोशाक", "कोडव पोशाख", d=("Kupya–chele for men and the pleated-at-the-back saree for women.", "पुरुषों के लिए कुप्य–चेले और महिलाओं के लिए पीछे प्लीट वाली साड़ी।", "पुरुषांसाठी कुप्य–चेले आणि स्त्रियांसाठी मागे निऱ्या असलेली साडी.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
reprof = 100 * g["realestate_prof"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]
crops = table("crops", L("Foodgrain production", "खाद्यान्न उत्पादन", "अन्नधान्य उत्पादन"),
              [col(L("Year", "वर्ष", "वर्ष")), col(L("Production (lakh tonnes)", "उत्पादन (लाख टन)", "उत्पादन (लाख टन)"), "right"), col(L("Area (lakh ha)", "क्षेत्रफल (लाख हेक्टेयर)", "क्षेत्र (लाख हेक्टर)"), "right")],
              [[L("2022-23 (final estimates)", "2022-23 (अंतिम अनुमान)", "2022-23 (अंतिम अंदाज)"), "143.55", "79.04"],
               [L("2025-26 (second advance estimates)", "2025-26 (द्वितीय अग्रिम अनुमान)", "2025-26 (दुसरे आगाऊ अंदाज)"), "136.22", "78.6"]],
              "ka-des", KAES26,
              note=L("Economic Survey of Karnataka 2023-24 (2022-23 final) and 2025-26 (2025-26 second advance estimates). The two estimates are of different types and are not directly comparable.",
                     "कर्नाटक आर्थिक सर्वेक्षण 2023-24 (2022-23 अंतिम) और 2025-26 (2025-26 द्वितीय अग्रिम अनुमान)। दोनों अनुमान अलग प्रकार के हैं और सीधे तुलनीय नहीं हैं।",
                     "कर्नाटक आर्थिक पाहणी 2023-24 (2022-23 अंतिम) व 2025-26 (2025-26 दुसरे आगाऊ अंदाज). दोन्ही अंदाज वेगळ्या प्रकारचे असून थेट तुलनीय नाहीत."))
module(R, "economy", [
    prose("p1", L(
        f"Karnataka is one of India's largest State economies. In the MoSPI series its GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26, and per capita NSDP, ₹{inr(pc['FY2025-26'][0])}, is among the highest of the large States. The economy leans heavily on services: in FY2024-25 real estate, ownership of dwellings and professional services — the group that includes software and IT services — made up about {reprof:.0f}% of GSVA, far more than in most States, while manufacturing was about {mfg:.0f}%.\n\nBengaluru is India's largest technology cluster, with software, research and development centres, aerospace and defence firms (HAL, ISRO), biotechnology and thousands of start-ups. Elsewhere, Ballari and Hosapete have iron ore and steel, Mangaluru has a port and refinery, Belagavi has foundries and aerospace suppliers, and the Mysuru–Mandya belt has sugar and silk. Karnataka is a leading producer of coffee, raw silk, ragi and areca nut. The PLFS unemployment rate was 2.3% in 2025; women's labour-force participation was 39.8%.",
        f"कर्नाटक भारत की सबसे बड़ी राज्य अर्थव्यवस्थाओं में है। मोस्पी शृंखला में वित्त वर्ष 2025-26 में प्रचलित मूल्यों पर इसका जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी, ₹{inr(pc['FY2025-26'][0])}, बड़े राज्यों में सबसे अधिक में से है। अर्थव्यवस्था सेवाओं पर बहुत निर्भर है: वित्त वर्ष 2024-25 में रियल एस्टेट, आवास स्वामित्व और पेशेवर सेवाएँ — वह समूह जिसमें सॉफ़्टवेयर और आईटी सेवाएँ शामिल हैं — जीएसवीए का लगभग {reprof:.0f}% थीं, जो अधिकांश राज्यों से बहुत अधिक है, जबकि विनिर्माण लगभग {mfg:.0f}% था।\n\nबेंगलूरु भारत का सबसे बड़ा प्रौद्योगिकी केंद्र है — सॉफ़्टवेयर, शोध एवं विकास केंद्र, एयरोस्पेस और रक्षा कंपनियाँ (एचएएल, इसरो), जैव-प्रौद्योगिकी और हज़ारों स्टार्टअप। अन्य जगहों पर, बल्लारी और होसपेटे में लौह अयस्क और इस्पात, मंगलूरु में बंदरगाह और रिफ़ाइनरी, बेलगावी में ढलाईघर और एयरोस्पेस आपूर्तिकर्ता, और मैसूरु–मंड्या पट्टी में चीनी और रेशम है। कर्नाटक कॉफ़ी, कच्चे रेशम, रागी और सुपारी का प्रमुख उत्पादक है। 2025 में पीएलएफ़एस बेरोज़गारी दर 2.3% थी; महिलाओं की श्रम बल भागीदारी 39.8% थी।",
        f"कर्नाटक ही भारतातील सर्वांत मोठ्या राज्य अर्थव्यवस्थांपैकी एक आहे. मोस्पी मालिकेनुसार आ.व. 2025-26 मध्ये चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी, ₹{inr(pc['FY2025-26'][0])}, मोठ्या राज्यांतील सर्वाधिकांपैकी आहे. अर्थव्यवस्था सेवाक्षेत्रावर मोठ्या प्रमाणात अवलंबून आहे: आ.व. 2024-25 मध्ये स्थावर मालमत्ता, घरमालकी व व्यावसायिक सेवा — ज्या गटात सॉफ्टवेअर व आयटी सेवा येतात — यांचा जीएसव्हीएमध्ये सुमारे {reprof:.0f}% वाटा होता, जो बहुतेक राज्यांपेक्षा कितीतरी जास्त आहे, तर उत्पादन उद्योगाचा सुमारे {mfg:.0f}%.\n\nबंगळूरु हे भारतातील सर्वांत मोठे तंत्रज्ञान केंद्र आहे — सॉफ्टवेअर, संशोधन व विकास केंद्रे, एरोस्पेस व संरक्षण कंपन्या (एचएएल, इस्रो), जैवतंत्रज्ञान आणि हजारो स्टार्टअप. इतरत्र, बळ्ळारी व होसपेटे येथे लोहखनिज व पोलाद, मंगळूरु येथे बंदर व तेलशुद्धीकरण कारखाना, बेळगावीत ओतकाम कारखाने व एरोस्पेस पुरवठादार, आणि म्हैसूरु–मंड्या पट्ट्यात साखर व रेशीम आहे. कर्नाटक कॉफी, कच्चे रेशीम, नाचणी व सुपारीचे आघाडीचे उत्पादक आहे. 2025 मध्ये पीएलएफएस बेरोजगारी दर 2.3% होता; स्त्रियांचा श्रमशक्ती सहभाग 39.8% होता."),
        sources=["mospi", "plfs", "ka-des"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_KA), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_KA), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_KA), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("KA", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    crops,
    plfs_series("KA", NAME),
    lst("sectors-key", [
        it3("it", "Software, IT services and R&D centres", "सॉफ़्टवेयर, आईटी सेवाएँ और शोध केंद्र", "सॉफ्टवेअर, आयटी सेवा व संशोधन केंद्रे", d=("Bengaluru, with smaller clusters in Mysuru, Mangaluru and Hubballi.", "बेंगलूरु, और मैसूरु, मंगलूरु व हुब्बल्ली में छोटे केंद्र।", "बंगळूरु, तसेच म्हैसूरु, मंगळूरु व हुबळी येथे लहान केंद्रे.")),
        it3("aero", "Aerospace and defence", "एयरोस्पेस और रक्षा", "एरोस्पेस व संरक्षण", d=("HAL, ISRO centres and suppliers in Bengaluru and Belagavi.", "बेंगलूरु और बेलगावी में एचएएल, इसरो केंद्र और आपूर्तिकर्ता।", "बंगळूरु व बेळगावीत एचएएल, इस्रो केंद्रे व पुरवठादार.")),
        it3("bt", "Biotechnology", "जैव-प्रौद्योगिकी", "जैवतंत्रज्ञान", d=("Bengaluru's biotech and pharma research cluster.", "बेंगलूरु का जैव-प्रौद्योगिकी और फ़ार्मा शोध केंद्र।", "बंगळूरुचे जैवतंत्रज्ञान व औषधनिर्मिती संशोधन केंद्र.")),
        it3("steel", "Iron ore and steel", "लौह अयस्क और इस्पात", "लोहखनिज व पोलाद", d=("Ballari–Hosapete belt.", "बल्लारी–होसपेटे पट्टी।", "बळ्ळारी–होसपेटे पट्टा.")),
        it3("coffee", "Coffee, silk and plantation crops", "कॉफ़ी, रेशम और बागान फ़सलें", "कॉफी, रेशीम व मळ्यातील पिके", d=("Kodagu and Chikkamagaluru coffee; Ramanagara–Mandya silk; areca nut in Malnad.", "कोडगु और चिक्कमगलूरु की कॉफ़ी; रामनगर–मंड्या का रेशम; मलनाड में सुपारी।", "कोडगू व चिक्कमगळूरुची कॉफी; रामनगर–मंड्याचे रेशीम; मलनाडमध्ये सुपारी.")),
        it3("ports", "Port, refinery and petrochemicals", "बंदरगाह, रिफ़ाइनरी और पेट्रोरसायन", "बंदर, तेलशुद्धीकरण व पेट्रोरसायने", d=("New Mangalore Port and the Mangaluru refinery.", "न्यू मंगलौर पोर्ट और मंगलूरु रिफ़ाइनरी।", "न्यू मंगलोर बंदर व मंगळूरु तेलशुद्धीकरण कारखाना.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Software and IT services exports", "सॉफ़्टवेयर और आईटी सेवा निर्यात", "सॉफ्टवेअर व आयटी सेवा निर्यात"), "india-gov", "STPI / State IT department, latest year."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("FDI equity inflows", "एफ़डीआई इक्विटी प्रवाह", "एफडीआय समभाग गुंतवणूक"), "dpiit", "DPIIT state-wise FDI factsheet."),
        (L("Coffee and raw silk production", "कॉफ़ी और कच्चे रेशम का उत्पादन", "कॉफी व कच्च्या रेशमाचे उत्पादन"), "india-gov", "Coffee Board and Central Silk Board statistics."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Karnataka has a bicameral legislature that meets at the Vidhana Soudha in Bengaluru and holds a winter session at the Suvarna Vidhana Soudha in Belagavi. The Legislative Assembly has 224 elected members and the Legislative Council 75. The State elects 28 members to the Lok Sabha and 12 to the Rajya Sabha.\n\nIn the May 2023 Assembly election the Indian National Congress won 135 seats and Siddaramaiah became Chief Minister. On 3 June 2026 D. K. Shivakumar took office as Chief Minister. G. S. Patil was elected Speaker in August 2026, and R. Ashoka of the BJP is Leader of Opposition. Sudha Yadav was sworn in as Governor on 16 October 2026, succeeding Thaawarchand Gehlot, Governor since July 2021. The next Assembly election is due in 2028.",
        "कर्नाटक में द्विसदनीय विधानमंडल है, जो बेंगलूरु के विधान सौध में बैठता है और बेलगावी के सुवर्ण विधान सौध में शीतकालीन सत्र करता है। विधानसभा में 224 निर्वाचित सदस्य और विधान परिषद में 75 सदस्य हैं। राज्य से लोकसभा के 28 और राज्यसभा के 12 सदस्य चुने जाते हैं।\n\nमई 2023 के विधानसभा चुनाव में भारतीय राष्ट्रीय कांग्रेस ने 135 सीटें जीतीं और सिद्धरामय्या मुख्यमंत्री बने। 3 जून 2026 को डी. के. शिवकुमार ने मुख्यमंत्री का पद संभाला। अगस्त 2026 में जी. एस. पाटिल अध्यक्ष चुने गए, और भाजपा के आर. अशोक नेता प्रतिपक्ष हैं। 16 अक्टूबर 2026 को सुधा यादव ने राज्यपाल पद की शपथ ली; वे जुलाई 2021 से राज्यपाल रहे थावरचंद गहलोत के उत्तराधिकारी हैं। अगला विधानसभा चुनाव 2028 में होना है।",
        "कर्नाटकमध्ये द्विसदनी विधिमंडळ आहे; ते बंगळूरुच्या विधानसौधमध्ये भरते आणि बेळगावीच्या सुवर्ण विधानसौधमध्ये हिवाळी अधिवेशन घेते. विधानसभेत 224 निर्वाचित सदस्य आणि विधान परिषदेत 75 सदस्य आहेत. राज्यातून लोकसभेवर 28 आणि राज्यसभेवर 12 सदस्य निवडले जातात.\n\nमे 2023 च्या विधानसभा निवडणुकीत भारतीय राष्ट्रीय काँग्रेसने 135 जागा जिंकल्या आणि सिद्धरामय्या मुख्यमंत्री झाले. 3 जून 2026 रोजी डी. के. शिवकुमार यांनी मुख्यमंत्रिपदाची सूत्रे स्वीकारली. ऑगस्ट 2026 मध्ये जी. एस. पाटील अध्यक्षपदी निवडले गेले, आणि भाजपचे आर. अशोक विरोधी पक्षनेते आहेत. 16 ऑक्टोबर 2026 रोजी सुधा यादव यांनी राज्यपालपदाची शपथ घेतली; जुलै 2021 पासून राज्यपाल असलेल्या थावरचंद गेहलोत यांच्या त्या उत्तराधिकारी आहेत. पुढील विधानसभा निवडणूक 2028 मध्ये होणार आहे."),
        sources=["eci", "newsonair", "uni", "ani"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    table("results", L("Legislative Assembly election, 2023 — seats won", "विधानसभा चुनाव, 2023 — जीती गई सीटें", "विधानसभा निवडणूक, 2023 — जिंकलेल्या जागा"),
          [col(L("Party", "दल", "पक्ष")), col(L("Seats", "सीटें", "जागा"), "right")],
          [["Indian National Congress (INC)", 135], ["Bharatiya Janata Party (BJP)", 66], ["Janata Dal (Secular) (JD(S))", 19],
           ["Kalyana Rajya Pragathi Paksha", 1], ["Sarvodaya Karnataka Paksha", 1], [L("Independents", "निर्दलीय", "अपक्ष"), 2],
           [L("Total", "कुल", "एकूण"), 224]],
          "eci", ECI, period="2023",
          note=L("Seats won as listed by the Election Commission (results declared 13 May 2023). Parties are shown by seats, without colours or commentary. By-elections and changes since 2023 have altered party strengths in the House.",
                 "चुनाव आयोग की सूची के अनुसार जीती गई सीटें (परिणाम 13 मई 2023 को घोषित)। दलों को सीटों के क्रम में, बिना रंग या टिप्पणी के दिखाया गया है। 2023 के बाद उपचुनावों और बदलावों से सदन में दलों की संख्या बदली है।",
                 "निवडणूक आयोगाच्या यादीनुसार जिंकलेल्या जागा (निकाल 13 मे 2023 रोजी जाहीर). पक्ष जागांच्या क्रमाने, रंग किंवा भाष्याशिवाय दाखवले आहेत. 2023 नंतरच्या पोटनिवडणुका व बदलांमुळे सभागृहातील पक्षीय बळ बदलले आहे.")),
    table("local", L("Panchayati Raj institutions", "पंचायती राज संस्थाएँ", "पंचायत राज संस्था"),
          [col(L("Type", "प्रकार", "प्रकार")), col(L("Number", "संख्या", "संख्या"), "right")],
          [[L("Zilla panchayats", "ज़िला पंचायतें", "जिल्हा परिषदा"), 31], [L("Taluk panchayats", "तालुक पंचायतें", "तालुका पंचायती"), 239],
           [L("Gram panchayats", "ग्राम पंचायतें", "ग्रामपंचायती"), "5,946"]],
          "ka-des", KAES26, period="2025-26", note=L("Economic Survey of Karnataka 2025-26.", "कर्नाटक आर्थिक सर्वेक्षण 2025-26।", "कर्नाटक आर्थिक पाहणी 2025-26.")),
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("assembly", "Karnataka Legislative Assembly", "कर्नाटक विधानसभा", "कर्नाटक विधानसभा", url="https://kla.kar.nic.in", src="india-gov"),
        it3("portal", "Government of Karnataka", "कर्नाटक सरकार", "कर्नाटक शासन", url="https://www.karnataka.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Speaker and Leader of Opposition — official confirmation", "अध्यक्ष और नेता प्रतिपक्ष — आधिकारिक पुष्टि", "अध्यक्ष व विरोधी पक्षनेते — अधिकृत पुष्टी"), "india-gov", "Replace the UNI citations with the Assembly secretariat page."),
        (L("Urban local bodies by type", "प्रकार के अनुसार नगरीय निकाय", "प्रकारानुसार नागरी स्वराज्य संस्था"), "ka-des", "Urban Development Department list."),
        (L("Current party strength in the Assembly", "विधानसभा में वर्तमान दलीय स्थिति", "विधानसभेतील सध्याचे पक्षीय बळ"), "india-gov", "Assembly secretariat member list."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Much of Karnataka's large infrastructure spending is in and around Bengaluru: the Namma Metro network, which passed 96 km with the opening of the Yellow Line in August 2025, the Phase 3 metro lines, a suburban rail network and new ring roads. Elsewhere, irrigation projects on the Krishna and the Upper Bhadra, and port and highway works on the coast, are the main programmes. Each card shows its source and the date it was checked.",
        "कर्नाटक का अधिकांश बड़ा बुनियादी ढाँचा ख़र्च बेंगलूरु और उसके आसपास है: नम्मा मेट्रो नेटवर्क, जो अगस्त 2025 में येलो लाइन खुलने के साथ 96 किमी पार कर गया, मेट्रो चरण 3 की लाइनें, उपनगरीय रेल नेटवर्क और नई रिंग रोड। अन्य जगहों पर कृष्णा और अपर भद्रा की सिंचाई परियोजनाएँ, और तट पर बंदरगाह व राजमार्ग कार्य मुख्य कार्यक्रम हैं। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "कर्नाटकचा बहुतांश मोठा पायाभूत खर्च बंगळूरु व परिसरात आहे: नम्मा मेट्रो जाळे — ऑगस्ट 2025 मध्ये यलो लाईन सुरू झाल्याने 96 किमीच्या पुढे — मेट्रो टप्पा 3 च्या मार्गिका, उपनगरी रेल्वे जाळे आणि नवे वर्तुळाकार मार्ग. इतरत्र, कृष्णा व अप्पर भद्रा सिंचन प्रकल्प आणि किनारपट्टीवरील बंदर व महामार्गांची कामे हे मुख्य कार्यक्रम आहेत. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pmindia"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Bengaluru Suburban Rail — official status", "बेंगलूरु उपनगरीय रेल — आधिकारिक स्थिति", "बंगळूरु उपनगरी रेल्वे — अधिकृत स्थिती"), "railways", "K-RIDE project status page."),
        (L("Upper Bhadra and Krishna Stage III irrigation — status", "अपर भद्रा और कृष्णा चरण III सिंचाई — स्थिति", "अप्पर भद्रा व कृष्णा टप्पा III सिंचन — स्थिती"), "india-gov", "Water Resources Department."),
        (L("Bengaluru–Mysuru expressway — completion record", "बेंगलूरु–मैसूरु एक्सप्रेसवे — पूर्णता रिकॉर्ड", "बंगळूरु–म्हैसूरु द्रुतगती मार्ग — पूर्णत्वाची नोंद"), "nhai", "NHAI / PIB release."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Kempegowda International Airport at Devanahalli, north of Bengaluru, is one of India's busiest airports; Mangaluru also has international flights, and Hubballi, Belagavi, Kalaburagi, Mysuru, Shivamogga and Bidar have domestic air services. The South Western Railway is headquartered in Hubballi, and Bengaluru, Mysuru and Hubballi–Dharwad are major rail hubs. New Mangalore Port is the State's major port, with Karwar and smaller ports on the coast. In Bengaluru, the Namma Metro had more than 96 km in operation after August 2025, and the BMTC runs one of India's largest city bus fleets.",
        "बेंगलूरु के उत्तर में देवनहल्ली स्थित केम्पेगौडा अंतरराष्ट्रीय हवाई अड्डा भारत के सबसे व्यस्त हवाई अड्डों में है; मंगलूरु से भी अंतरराष्ट्रीय उड़ानें हैं, और हुब्बल्ली, बेलगावी, कलबुर्गी, मैसूरु, शिवमोग्गा और बीदर में घरेलू हवाई सेवाएँ हैं। दक्षिण पश्चिम रेलवे का मुख्यालय हुब्बल्ली में है, और बेंगलूरु, मैसूरु व हुब्बल्ली–धारवाड़ बड़े रेल केंद्र हैं। न्यू मंगलौर पोर्ट राज्य का प्रमुख बंदरगाह है, और तट पर कारवार व छोटे बंदरगाह हैं। बेंगलूरु में अगस्त 2025 के बाद नम्मा मेट्रो के 96 किमी से अधिक हिस्से चालू थे, और बीएमटीसी भारत के सबसे बड़े शहरी बस बेड़ों में से एक चलाता है।",
        "बंगळूरुच्या उत्तरेला देवनहळ्ळी येथील केम्पेगौडा आंतरराष्ट्रीय विमानतळ भारतातील सर्वांत व्यस्त विमानतळांपैकी आहे; मंगळूरुहूनही आंतरराष्ट्रीय उड्डाणे आहेत, आणि हुबळी, बेळगावी, कलबुर्गी, म्हैसूरु, शिवमोग्गा व बीदर येथे देशांतर्गत विमानसेवा आहे. दक्षिण पश्चिम रेल्वेचे मुख्यालय हुबळीत आहे, आणि बंगळूरु, म्हैसूरु व हुबळी–धारवाड ही मोठी रेल्वे केंद्रे आहेत. न्यू मंगलोर बंदर हे राज्याचे प्रमुख बंदर असून किनारपट्टीवर कारवार व लहान बंदरे आहेत. बंगळूरुमध्ये ऑगस्ट 2025 नंतर नम्मा मेट्रोचे 96 किमीहून अधिक जाळे कार्यरत होते, आणि बीएमटीसी भारतातील सर्वांत मोठ्या शहरी बस ताफ्यांपैकी एक चालवते."),
        conf="Editorial"),
    lst("airports", [
        it3("blr", "Kempegowda International Airport, Bengaluru", "केम्पेगौडा अंतरराष्ट्रीय हवाई अड्डा, बेंगलूरु", "केम्पेगौडा आंतरराष्ट्रीय विमानतळ, बंगळूरु", m=("BLR", "BLR", "BLR")),
        it3("ixe", "Mangaluru International Airport", "मंगलूरु अंतरराष्ट्रीय हवाई अड्डा", "मंगळूरु आंतरराष्ट्रीय विमानतळ", m=("IXE", "IXE", "IXE")),
        it3("hbx", "Hubballi airport", "हुब्बल्ली हवाई अड्डा", "हुबळी विमानतळ"), it3("ixg", "Belagavi airport", "बेलगावी हवाई अड्डा", "बेळगावी विमानतळ"),
        it3("glb", "Kalaburagi airport", "कलबुर्गी हवाई अड्डा", "कलबुर्गी विमानतळ"), it3("myq", "Mysuru airport", "मैसूरु हवाई अड्डा", "म्हैसूरु विमानतळ"),
        it3("rqy", "Shivamogga airport", "शिवमोग्गा हवाई अड्डा", "शिवमोग्गा विमानतळ"),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Railway route length", "रेलवे मार्ग की लंबाई", "रेल्वे मार्गाची लांबी"), "railways", "Indian Railways Year Book."),
        (L("Airport and port traffic", "हवाई अड्डा और बंदरगाह यातायात", "विमानतळ व बंदर वाहतूक"), "aai", "AAI traffic statistics; Indian Ports Association."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Karnataka has one of India's highest shares of renewable power. The Economic Survey of Karnataka 2025-26 puts installed generation capacity at 37,072.95 MW as of December 2025, with renewables making up more than half. The Pavagada solar park in Tumakuru district is among the largest in the world, and wind farms run across the northern and central districts. Hydro stations on the Sharavati, Kali and Kaveri — including Linganamakki and Shivanasamudra, one of Asia's first hydro-electric stations (1902) — and coal plants at Raichur, Ballari (Kudithini) and Yermarus make up much of the rest. The Kaiga nuclear power station is in Uttara Kannada district.",
        "कर्नाटक में अक्षय ऊर्जा का हिस्सा भारत में सबसे अधिक में से है। कर्नाटक आर्थिक सर्वेक्षण 2025-26 के अनुसार दिसंबर 2025 तक स्थापित उत्पादन क्षमता 37,072.95 मेगावाट थी, जिसमें आधे से अधिक अक्षय ऊर्जा है। तुमकूरु ज़िले का पावगडा सौर पार्क दुनिया के सबसे बड़े सौर पार्कों में है, और उत्तरी व मध्य ज़िलों में पवन फ़ार्म हैं। शरावती, काली और कावेरी पर जलविद्युत केंद्र — जिनमें लिंगनमक्की और एशिया के पहले जलविद्युत केंद्रों में से एक शिवनसमुद्र (1902) शामिल हैं — और रायचूर, बल्लारी (कुडितिनी) व येरमरस के कोयला संयंत्र बाकी क्षमता का बड़ा हिस्सा हैं। कैगा परमाणु बिजलीघर उत्तर कन्नड़ ज़िले में है।",
        "अक्षय ऊर्जेचा वाटा असलेल्या भारतातील आघाडीच्या राज्यांपैकी कर्नाटक एक आहे. कर्नाटक आर्थिक पाहणी 2025-26 नुसार डिसेंबर 2025 पर्यंत स्थापित निर्मिती क्षमता 37,072.95 मेगावॉट होती, ज्यात निम्म्याहून अधिक अक्षय ऊर्जा आहे. तुमकूरु जिल्ह्यातील पावगडा सौर उद्यान जगातील सर्वांत मोठ्या सौर उद्यानांपैकी आहे, आणि उत्तर व मध्य जिल्ह्यांत पवनऊर्जा प्रकल्प आहेत. शरावती, काळी व कावेरीवरील जलविद्युत केंद्रे — लिंगनमक्की आणि आशियातील पहिल्या जलविद्युत केंद्रांपैकी एक शिवनसमुद्र (1902) यांसह — आणि रायचूर, बळ्ळारी (कुडितिनी) व येरमरस येथील कोळसा केंद्रे उरलेल्या क्षमतेचा मोठा भाग आहेत. कैगा अणुऊर्जा केंद्र उत्तर कन्नड जिल्ह्यात आहे."),
        sources=["ka-des"], conf="Official"),
    facts("f", [
        fact("cap", L("Installed generation capacity", "स्थापित उत्पादन क्षमता", "स्थापित निर्मिती क्षमता"),
             dp(37072.95, "MW", "2025", "calendar", "ka-des", KAES26, note="As of December 2025: public sector 13,759.78 MW, private sector 23,313.17 MW (Economic Survey of Karnataka 2025-26)."), "number", "higher-is-better"),
        fact("re", L("Renewable share of installed capacity", "स्थापित क्षमता में अक्षय ऊर्जा का हिस्सा", "स्थापित क्षमतेत अक्षय ऊर्जेचा वाटा"),
             dp(53.32, "%", "2025", "calendar", "ka-des", KAES26, note="'Over 53.32%' as of December 2025, excluding IPP thermal and mini-hydro (Economic Survey of Karnataka 2025-26)."), "percent", "higher-is-better"),
    ], title=L("Power capacity", "बिजली क्षमता", "वीज क्षमता")),
    gaps("g", [
        (L("Capacity by source (CEA)", "स्रोतवार क्षमता (सीईए)", "स्रोतनिहाय क्षमता (सीईए)"), "cea", "CEA installed capacity report."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Bengaluru is India's largest technology hub. It hosts the development centres of many global technology companies, the headquarters of major Indian IT services firms, and one of the world's largest start-up ecosystems, together with research institutions such as the Indian Institute of Science. The State was among the first in India to publish an IT policy (1997) and has set up technology parks and incubators in Mysuru, Mangaluru, Hubballi and Kalaburagi to spread the industry beyond the capital.",
        "बेंगलूरु भारत का सबसे बड़ा प्रौद्योगिकी केंद्र है। यहाँ कई वैश्विक प्रौद्योगिकी कंपनियों के विकास केंद्र, प्रमुख भारतीय आईटी सेवा कंपनियों के मुख्यालय और दुनिया के सबसे बड़े स्टार्टअप तंत्रों में से एक है, साथ में भारतीय विज्ञान संस्थान जैसे शोध संस्थान भी। राज्य आईटी नीति (1997) प्रकाशित करने वाले भारत के पहले राज्यों में था और उसने उद्योग को राजधानी से बाहर फैलाने के लिए मैसूरु, मंगलूरु, हुब्बल्ली और कलबुर्गी में टेक्नोलॉजी पार्क और इनक्यूबेटर बनाए हैं।",
        "बंगळूरु हे भारतातील सर्वांत मोठे तंत्रज्ञान केंद्र आहे. इथे अनेक जागतिक तंत्रज्ञान कंपन्यांची विकास केंद्रे, प्रमुख भारतीय आयटी सेवा कंपन्यांची मुख्यालये आणि जगातील सर्वांत मोठ्या स्टार्टअप परिसंस्थांपैकी एक आहे, सोबत भारतीय विज्ञान संस्थेसारख्या संशोधन संस्था. आयटी धोरण (1997) प्रसिद्ध करणाऱ्या भारतातील पहिल्या राज्यांपैकी कर्नाटक एक होते, आणि उद्योग राजधानीबाहेर पसरवण्यासाठी त्याने म्हैसूरु, मंगळूरु, हुबळी व कलबुर्गी येथे तंत्रज्ञान पार्क व इनक्युबेटर उभारले आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Karnataka circle)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
        (L("IT employment", "आईटी रोज़गार", "आयटी रोजगार"), "india-gov", "State IT/BT department or NASSCOM (label third-party)."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("KA", NAME)
module(R, "education", [
    prose("p1", L(
        "Karnataka's higher-education gross enrolment ratio (ages 18–23) was 36.2% in 2021-22 in AISHE, well above the national 28.4%, and almost equal for women (36.3%) and men (36.1%). The State had 75 universities and 4,430 colleges. Literacy at the 2011 Census was 75.4%.\n\nBengaluru is home to several of India's leading institutions — the Indian Institute of Science (1909), IIM Bangalore, the National Law School of India University, NIMHANS and the Raman Research Institute — and the State also has IIT Dharwad, NIT Karnataka at Surathkal and the University of Mysore (1916). Engineering and medical colleges are spread across the State, many of them private.",
        "एआईएसएचई के अनुसार 2021-22 में कर्नाटक का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) 36.2% था, जो राष्ट्रीय 28.4% से काफ़ी अधिक है, और महिलाओं (36.3%) व पुरुषों (36.1%) के लिए लगभग बराबर था। राज्य में 75 विश्वविद्यालय और 4,430 कॉलेज थे। 2011 की जनगणना में साक्षरता 75.4% थी।\n\nबेंगलूरु में भारत के कई प्रमुख संस्थान हैं — भारतीय विज्ञान संस्थान (1909), आईआईएम बैंगलोर, नेशनल लॉ स्कूल ऑफ़ इंडिया यूनिवर्सिटी, निमहांस और रमन शोध संस्थान — और राज्य में आईआईटी धारवाड़, सुरत्कल में एनआईटी कर्नाटक और मैसूर विश्वविद्यालय (1916) भी हैं। इंजीनियरिंग और मेडिकल कॉलेज पूरे राज्य में फैले हैं, जिनमें से कई निजी हैं।",
        "एआयएसएचईनुसार 2021-22 मध्ये कर्नाटकचे उच्चशिक्षणातील एकूण नोंदणी गुणोत्तर (18–23 वय) 36.2% होते — राष्ट्रीय 28.4% पेक्षा बरेच जास्त — आणि स्त्रिया (36.3%) व पुरुष (36.1%) यांच्यासाठी जवळपास समान होते. राज्यात 75 विद्यापीठे व 4,430 महाविद्यालये होती. 2011 च्या जनगणनेत साक्षरता 75.4% होती.\n\nबंगळूरुमध्ये भारतातील अनेक आघाडीच्या संस्था आहेत — भारतीय विज्ञान संस्था (1909), आयआयएम बंगळूर, नॅशनल लॉ स्कूल ऑफ इंडिया युनिव्हर्सिटी, निमहान्स व रामन संशोधन संस्था — आणि राज्यात आयआयटी धारवाड, सुरत्कल येथील एनआयटी कर्नाटक व म्हैसूर विद्यापीठ (1916) देखील आहेत. अभियांत्रिकी व वैद्यकीय महाविद्यालये राज्यभर पसरली असून त्यांपैकी अनेक खासगी आहेत."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("iisc", "Indian Institute of Science", "भारतीय विज्ञान संस्थान", "भारतीय विज्ञान संस्था", m=("Bengaluru, 1909", "बेंगलूरु, 1909", "बंगळूरु, 1909")),
        it3("iimb", "IIM Bangalore", "आईआईएम बैंगलोर", "आयआयएम बंगळूर", m=("Bengaluru", "बेंगलूरु", "बंगळूरु")),
        it3("nls", "National Law School of India University", "नेशनल लॉ स्कूल ऑफ़ इंडिया यूनिवर्सिटी", "नॅशनल लॉ स्कूल ऑफ इंडिया युनिव्हर्सिटी", m=("Bengaluru", "बेंगलूरु", "बंगळूरु")),
        it3("nimhans", "NIMHANS", "निमहांस", "निमहान्स", m=("Bengaluru", "बेंगलूरु", "बंगळूरु")),
        it3("iitdh", "IIT Dharwad", "आईआईटी धारवाड़", "आयआयटी धारवाड", m=("Dharwad", "धारवाड़", "धारवाड")),
        it3("nitk", "NIT Karnataka", "एनआईटी कर्नाटक", "एनआयटी कर्नाटक", m=("Surathkal", "सुरत्कल", "सुरत्कल")),
        it3("uom", "University of Mysore", "मैसूर विश्वविद्यालय", "म्हैसूर विद्यापीठ", m=("Mysuru, 1916", "मैसूरु, 1916", "म्हैसूरु, 1916")),
    ], title=L("National institutions (selected)", "राष्ट्रीय संस्थान (चयनित)", "राष्ट्रीय संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Dropout rates by level", "स्तरवार ड्रॉपआउट दर", "स्तरनिहाय गळती दर"), "udise", "UDISE+."),
        (L("NIRF-ranked institutions", "एनआईआरएफ़ रैंक वाले संस्थान", "एनआयआरएफ क्रमवारीतील संस्था"), "nirf", "Latest NIRF list filtered to Karnataka."),
    ]),
])

# ---------------- O. Health ----------------
srs = NF["SRS_2021_PIB_PRID2128024"]
def srsdp(v, unit, period, note=None, level="state"):
    return dp(v, unit, period, "survey" if "-" in period else "calendar", "srs", SRS, note=note, level=level)
module(R, "health", [
    prose("p1", L(
        "Karnataka's health indicators are better than the national average on most measures. In the Sample Registration System, maternal mortality was 63 per lakh live births in 2019-21 (India 93) and under-five mortality 21 per 1,000 live births in 2021 (India 31). Almost 97% of births took place in health facilities in NFHS-5, but child undernutrition remains a concern: 35.4% of children under five were stunted, close to the national level, though wasting fell from 26.1% to 19.5% between NFHS-4 and NFHS-5.\n\nBengaluru and Mysuru are major centres for specialist and private hospital care, and Mangaluru and Manipal have large medical-college hospitals. Life expectancy at birth was 69.4 years in 2014-18.",
        "अधिकांश मापदंडों पर कर्नाटक के स्वास्थ्य संकेतक राष्ट्रीय औसत से बेहतर हैं। नमूना पंजीकरण प्रणाली में 2019-21 में मातृ मृत्यु अनुपात प्रति लाख जीवित जन्म पर 63 (भारत 93) और 2021 में पाँच वर्ष से कम आयु की मृत्यु दर प्रति 1,000 जीवित जन्म पर 21 (भारत 31) थी। एनएफ़एचएस-5 में लगभग 97% प्रसव स्वास्थ्य संस्थानों में हुए, लेकिन बाल कुपोषण चिंता का विषय है: पाँच वर्ष से कम आयु के 35.4% बच्चे ठिगने थे, जो राष्ट्रीय स्तर के क़रीब है, हालाँकि एनएफ़एचएस-4 और एनएफ़एचएस-5 के बीच दुबलापन 26.1% से घटकर 19.5% रह गया।\n\nबेंगलूरु और मैसूरु विशेषज्ञ और निजी अस्पताल देखभाल के बड़े केंद्र हैं, और मंगलूरु व मणिपाल में बड़े मेडिकल-कॉलेज अस्पताल हैं। 2014-18 में जन्म के समय जीवन प्रत्याशा 69.4 वर्ष थी।",
        "बहुतेक निकषांवर कर्नाटकचे आरोग्य निर्देशक राष्ट्रीय सरासरीपेक्षा चांगले आहेत. नमुना नोंदणी पद्धतीनुसार 2019-21 मध्ये मातामृत्यू प्रमाण दर लाख जिवंत जन्मांमागे 63 (भारत 93) आणि 2021 मध्ये पाच वर्षांखालील मृत्युदर दर 1,000 जिवंत जन्मांमागे 21 (भारत 31) होता. एनएफएचएस-5 मध्ये जवळपास 97% प्रसूती आरोग्य संस्थांत झाल्या, पण बालकुपोषण ही चिंता कायम आहे: पाच वर्षांखालील 35.4% मुले खुजी होती — राष्ट्रीय पातळीच्या जवळ — मात्र एनएफएचएस-4 ते एनएफएचएस-5 दरम्यान कृशता 26.1% वरून 19.5% वर आली.\n\nबंगळूरु व म्हैसूरु ही विशेषज्ञ व खासगी रुग्णालय सेवेची मोठी केंद्रे आहेत, आणि मंगळूरु व मणिपाल येथे मोठी वैद्यकीय महाविद्यालय रुग्णालये आहेत. 2014-18 मध्ये जन्मतः आयुर्मान 69.4 वर्षे होते."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("mmr", L("Maternal mortality ratio", "मातृ मृत्यु अनुपात", "मातामृत्यू प्रमाण"), srsdp(srs["KA"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", "SRS special bulletin, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", level="national")),
        fact("u5mr", L("Under-five mortality rate", "पाँच वर्ष से कम आयु की मृत्यु दर", "पाच वर्षांखालील मृत्युदर"), srsdp(srs["KA"]["U5MR"], "per 1,000 live births", "2021", "SRS 2021, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["U5MR"], "per 1,000 live births", "2021", level="national")),
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(21, "per 1,000 live births", "2019", "calendar", "srs", ESI_VS, note="SRS 2019, Economic Survey 2021-22 Statistical Appendix Table 8.2 (41 in 2009)."), "number", "lower-is-better",
             previous=dp(41, "per 1,000 live births", "2009", "calendar", "srs", ESI_VS)),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, note="SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male 67.9, female 70.9)."), "number", "higher-is-better",
             national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality (Sample Registration System)", "मृत्यु दर (नमूना पंजीकरण प्रणाली)", "मृत्युदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("KA"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Infant mortality rate, latest SRS year", "शिशु मृत्यु दर, नवीनतम एसआरएस वर्ष", "अर्भक मृत्युदर, नवीनतम एसआरएस वर्ष"), "srs", "SRS Statistical Report (latest)."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("ka mod2 ok")
