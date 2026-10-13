import sys, json
sys.path.insert(0, __import__("os").path.dirname(__file__))
from bd import *

R = "IN-MH"
SDB = "https://mahasdb.maharashtra.gov.in/maagCmpIndia.do"
MOSPI = "https://mospi.gov.in"
ECI = "https://results.eci.gov.in/ResultAcGenNov2024/partywiseresult-S13.htm"
mo = json.load(open(__import__("os").path.join(__import__("os").path.dirname(__file__), "research") + "/mospi.json"))

def fy_points(key, idx, unit, base, kind_note):
    pts = []
    years = sorted(mo[key].keys())
    for y in years:
        v = mo[key][y][idx]
        rev = "provisional" if y in ("FY2024-25", "FY2025-26") else "final"
        pts.append(dp(v, unit, y, "fy", "mospi", MOSPI, rev=rev, base=base,
                      note=kind_note if y == years[-1] else None))
    return pts

CUR = {"type": "current"}
CON = {"type": "constant", "baseYear": "2011-12"}
NOTE = "MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API. FY2024-25 and FY2025-26 are recent estimates and may be revised."

# ---------------- G. Culture ----------------
def fest(id, en, hi, mr, m_en, m_hi, m_mr, d_en, d_hi, d_mr):
    return item(id, L(en, hi, mr), detail=L(d_en, d_hi, d_mr), meta=L(m_en, m_hi, m_mr))

module(R, "culture", [
    prose("p1", L(
        "Maharashtrian culture mixes devotional and secular traditions. The Varkari movement of saint-poets such as Dnyaneshwar, Namdev, Eknath and Tukaram shaped Marathi language and music, and its abhangs are still sung on the annual Wari. Folk forms include Lavani, a fast song-and-dance form performed to the dholki; Tamasha, a travelling folk theatre; the Powada ballad celebrating heroes; and Koli dances of the fishing communities. Marathi theatre has a strong tradition of sangeet natak (musical drama).\n\nCrafts range from Paithani silk saris with peacock motifs to Warli painting from the tribal belt of Palghar and Thane, Kolhapuri leather chappals, and silverwork from Hupari. Mumbai is home to the Hindi film industry, and Marathi cinema traces its roots to Dadasaheb Phalke, whose Raja Harishchandra (1913) is regarded as India's first full-length feature film.",
        "महाराष्ट्र की संस्कृति में भक्ति और लौकिक परंपराएँ घुली-मिली हैं। ज्ञानेश्वर, नामदेव, एकनाथ और तुकाराम जैसे संत-कवियों के वारकरी आंदोलन ने मराठी भाषा और संगीत को आकार दिया, और उनके अभंग आज भी वार्षिक वारी में गाए जाते हैं। लोक कलाओं में ढोलकी की थाप पर तेज़ गीत-नृत्य लावणी, घूमने वाला लोक-रंगमंच तमाशा, वीरों का गुणगान करने वाला पोवाड़ा और मछुआरा समुदायों का कोली नृत्य शामिल हैं। मराठी रंगमंच में संगीत नाटक की समृद्ध परंपरा है।\n\nशिल्पों में मोर की आकृतियों वाली पैठणी रेशमी साड़ियाँ, पालघर और ठाणे के जनजातीय क्षेत्र की वारली चित्रकला, कोल्हापुरी चमड़े की चप्पलें और हुपरी का चाँदी का काम आते हैं। मुंबई हिंदी फ़िल्म उद्योग का घर है, और मराठी सिनेमा की जड़ें दादासाहेब फाल्के तक जाती हैं, जिनकी राजा हरिश्चंद्र (1913) को भारत की पहली पूर्ण-लंबाई फ़ीचर फ़िल्म माना जाता है।",
        "महाराष्ट्राच्या संस्कृतीत भक्ती आणि लौकिक परंपरा एकरूप झाल्या आहेत. ज्ञानेश्वर, नामदेव, एकनाथ आणि तुकाराम यांसारख्या संतकवींच्या वारकरी संप्रदायाने मराठी भाषा व संगीताला आकार दिला, आणि त्यांचे अभंग आजही वारीत गायले जातात. लोककलांमध्ये ढोलकीच्या ठेक्यावरची ठसकेबाज लावणी, फिरता लोकनाट्य प्रकार तमाशा, वीरांचे गुणगान करणारा पोवाडा आणि कोळी समाजाचे कोळीनृत्य यांचा समावेश होतो. मराठी रंगभूमीला संगीत नाटकाची समृद्ध परंपरा आहे.\n\nहस्तकलांमध्ये मोराच्या नक्षीच्या पैठणी साड्या, पालघर-ठाणे भागातील आदिवासी वारली चित्रकला, कोल्हापुरी चपला आणि हुपरीचे चांदीकाम येते. मुंबई हिंदी चित्रपटसृष्टीचे घर आहे, तर मराठी चित्रपटाची मुळे दादासाहेब फाळके यांच्यापर्यंत जातात; त्यांचा ‘राजा हरिश्चंद्र’ (1913) हा भारतातील पहिला पूर्ण लांबीचा चित्रपट मानला जातो."),
        conf="Editorial"),
    lst("festivals", [
        fest("gudi", "Gudi Padwa", "गुड़ी पड़वा", "गुढीपाडवा", "March–April", "मार्च–अप्रैल", "मार्च–एप्रिल",
             "Marathi New Year; households raise a gudi at the doorway.", "मराठी नववर्ष; घर-घर के द्वार पर गुड़ी खड़ी की जाती है।", "मराठी नववर्ष; घरोघरी दारात गुढी उभारली जाते."),
        fest("wari", "Ashadhi Ekadashi Wari", "आषाढ़ी एकादशी वारी", "आषाढी एकादशी वारी", "June–July", "जून–जुलाई", "जून–जुलै",
             "Lakhs of warkaris walk with the palkhis of the saints to Pandharpur.", "लाखों वारकरी संतों की पालकियों के साथ पंढरपुर तक पैदल जाते हैं।", "लाखो वारकरी संतांच्या पालख्यांसोबत पंढरपूरपर्यंत पायी जातात."),
        fest("pola", "Bail Pola", "बैल पोळा", "बैलपोळा", "August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर",
             "Farmers decorate and honour their bullocks.", "किसान अपने बैलों को सजाकर उनका सम्मान करते हैं।", "शेतकरी आपल्या बैलांना सजवून त्यांची पूजा करतात."),
        fest("ganesh", "Ganeshotsav", "गणेशोत्सव", "गणेशोत्सव", "August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर",
             "Ten days of public and household Ganesh worship, popularised as a public festival by Lokmanya Tilak.", "दस दिन तक सार्वजनिक और घरेलू गणेश पूजा; लोकमान्य तिलक ने इसे सार्वजनिक उत्सव के रूप में लोकप्रिय बनाया।", "दहा दिवसांचा सार्वजनिक व घरगुती गणेशोत्सव; लोकमान्य टिळकांनी त्याला सार्वजनिक स्वरूप दिले."),
        fest("navratri", "Navratri and Dasara", "नवरात्रि और दशहरा", "नवरात्र आणि दसरा", "September–October", "सितंबर–अक्टूबर", "सप्टेंबर–ऑक्टोबर",
             "Goddess worship at shrines such as Tuljapur and Kolhapur; apta leaves exchanged as 'gold' on Dasara.", "तुलजापुर और कोल्हापुर जैसे शक्तिपीठों पर देवी पूजा; दशहरे पर आपटे के पत्ते 'सोने' के रूप में बाँटे जाते हैं।", "तुळजापूर, कोल्हापूर यांसारख्या शक्तिपीठांत देवीची उपासना; दसऱ्याला आपट्याची पाने 'सोने' म्हणून वाटली जातात."),
        fest("diwali", "Diwali", "दिवाली", "दिवाळी", "October–November", "अक्टूबर–नवंबर", "ऑक्टोबर–नोव्हेंबर",
             "Akashkandil lanterns, rangoli and faral sweets; Diwali Ank magazines are a Marathi tradition.", "आकाशकंदील, रंगोली और फराळ की मिठाइयाँ; दिवाली अंक पत्रिकाएँ मराठी परंपरा हैं।", "आकाशकंदील, रांगोळी आणि फराळ; दिवाळी अंक ही खास मराठी परंपरा आहे."),
        fest("sankranti", "Makar Sankranti", "मकर संक्रांति", "मकरसंक्रांत", "January", "जनवरी", "जानेवारी",
             "Til-gul sweets shared with 'tilgul ghya, god god bola'.", "'तिळगुळ घ्या, गोड गोड बोला' कहते हुए तिल-गुड़ बाँटा जाता है।", "'तिळगूळ घ्या, गोड गोड बोला' म्हणत तिळगूळ वाटला जातो."),
        fest("mhday", "Maharashtra Day", "महाराष्ट्र दिवस", "महाराष्ट्र दिन", "1 May", "1 मई", "1 मे",
             "State formation day.", "राज्य स्थापना दिवस।", "राज्य स्थापना दिन."),
    ], title=L("Festival calendar", "त्योहार कैलेंडर", "सण-उत्सव दिनदर्शिका"), conf="Editorial"),
    lst("food", [
        item("vadapav", L("Vada pav", "वड़ा पाव", "वडापाव"), detail=L("Spiced potato fritter in a bun — Mumbai's street staple.", "बन में मसालेदार आलू वड़ा — मुंबई का सबसे आम स्ट्रीट फ़ूड।", "पावात मसालेदार बटाटेवडा — मुंबईचा रोजचा रस्त्यावरचा खाऊ.")),
        item("misal", L("Misal pav", "मिसळ पाव", "मिसळपाव"), detail=L("Fiery sprouted-moth curry topped with farsan; Kolhapur, Pune and Nashik have rival styles.", "तीखी अंकुरित मटकी की तरी, ऊपर फरसाण; कोल्हापुर, पुणे और नासिक की अपनी-अपनी शैली।", "झणझणीत मोड आलेल्या मटकीची उसळ आणि वर फरसाण; कोल्हापुरी, पुणेरी, नाशिकची आपापली शैली.")),
        item("puranpoli", L("Puran poli", "पूरन पोली", "पुरणपोळी"), detail=L("Flatbread stuffed with sweet chana dal and jaggery, made on festivals.", "मीठी चना दाल और गुड़ भरी रोटी, त्योहारों पर बनती है।", "हरभरा डाळ आणि गुळाचे पुरण भरलेली पोळी, सणावारी केली जाते.")),
        item("modak", L("Ukadiche modak", "उकडीचे मोदक", "उकडीचे मोदक"), detail=L("Steamed rice dumplings with coconut-jaggery filling, offered at Ganeshotsav.", "नारियल-गुड़ भरे भाप में पके चावल के मोदक, गणेशोत्सव में चढ़ाए जाते हैं।", "ओल्या नारळाचे सारण भरलेले उकडीचे मोदक, गणेशोत्सवात नैवेद्य.")),
        item("thalipeeth", L("Thalipeeth", "थालीपीठ", "थालीपीठ"), detail=L("Savoury multigrain flatbread, eaten with butter or curd.", "कई अनाजों की नमकीन रोटी, मक्खन या दही के साथ।", "भाजणीचे खमंग थालीपीठ, लोणी किंवा दह्यासोबत.")),
        item("bhakri", L("Jowar bhakri with pithla or zunka", "ज्वार भाकरी के साथ पिठला या झुणका", "ज्वारीची भाकरी आणि पिठलं किंवा झुणका"), detail=L("The everyday meal of rural Maharashtra.", "ग्रामीण महाराष्ट्र का रोज़ का भोजन।", "ग्रामीण महाराष्ट्राचे रोजचे जेवण.")),
        item("kolhapuri", L("Kolhapuri tambda and pandhra rassa", "कोल्हापुरी तांबडा और पांढरा रस्सा", "कोल्हापुरी तांबडा-पांढरा रस्सा"), detail=L("Red and white mutton broths from Kolhapur.", "कोल्हापुर के लाल और सफ़ेद मटन शोरबे।", "कोल्हापूरचा लाल आणि पांढरा मटणाचा रस्सा.")),
        item("malvani", L("Malvani fish curry and sol kadhi", "मालवणी मछली करी और सोल कढ़ी", "मालवणी माशांचे कालवण आणि सोलकढी"), detail=L("Coconut-based Konkan seafood with a kokum and coconut-milk drink.", "नारियल वाली कोंकणी समुद्री मछली, साथ में कोकम और नारियल दूध का पेय।", "नारळाच्या वाटणातले कोकणी मासे आणि कोकम-नारळाच्या दुधाची सोलकढी.")),
        item("saoji", L("Saoji cuisine", "सावजी व्यंजन", "सावजी पदार्थ"), detail=L("Intensely spiced curries from Nagpur and Vidarbha.", "नागपुर और विदर्भ की बेहद मसालेदार तरी।", "नागपूर-विदर्भातील झणझणीत सावजी रस्सा.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("jnanpith", [
        item("khandekar", L("V. S. Khandekar", "वि. स. खांडेकर", "वि. स. खांडेकर"), meta=L("Jnanpith 1974", "ज्ञानपीठ 1974", "ज्ञानपीठ 1974")),
        item("kusumagraj", L("Kusumagraj (V. V. Shirwadkar)", "कुसुमाग्रज (वि. वा. शिरवाडकर)", "कुसुमाग्रज (वि. वा. शिरवाडकर)"), meta=L("Jnanpith 1987", "ज्ञानपीठ 1987", "ज्ञानपीठ 1987")),
        item("vinda", L("Vinda Karandikar", "विंदा करंदीकर", "विंदा करंदीकर"), meta=L("Jnanpith 2003", "ज्ञानपीठ 2003", "ज्ञानपीठ 2003")),
        item("nemade", L("Bhalchandra Nemade", "भालचंद्र नेमाडे", "भालचंद्र नेमाडे"), meta=L("Jnanpith 2014", "ज्ञानपीठ 2014", "ज्ञानपीठ 2014")),
    ], layout="chips", title=L("Marathi Jnanpith laureates", "मराठी के ज्ञानपीठ पुरस्कार विजेता", "मराठी ज्ञानपीठ विजेते"), conf="Editorial"),
    prose("etiquette", L(
        "Remove footwear before entering homes and temples. Many forts and caves are protected monuments — do not climb on carvings or leave litter. During the Wari and Ganeshotsav, expect road closures and follow police directions.",
        "घरों और मंदिरों में जाने से पहले जूते-चप्पल उतारें। कई क़िले और गुफ़ाएँ संरक्षित स्मारक हैं — नक़्क़ाशी पर न चढ़ें और कचरा न छोड़ें। वारी और गणेशोत्सव के दौरान सड़कें बंद रह सकती हैं; पुलिस के निर्देशों का पालन करें।",
        "घरात आणि देवळात जाण्यापूर्वी पादत्राणे काढा. अनेक किल्ले आणि लेणी संरक्षित स्मारके आहेत — कोरीवकामावर चढू नका, कचरा टाकू नका. वारी आणि गणेशोत्सवाच्या काळात रस्ते बंद असू शकतात; पोलिसांच्या सूचनांचे पालन करा."),
        conf="Editorial", title=L("Responsible cultural tourism", "ज़िम्मेदार सांस्कृतिक पर्यटन", "जबाबदार सांस्कृतिक पर्यटन")),
])

# ---------------- H. Economy ----------------
g = mo["gsva2024_25_current_lakh"]; T = g["total"]
pct = lambda v: round(v / T * 100, 2)
GSVA_URL = MOSPI
cur_last = mo["gsdp"]["FY2025-26"][0]; cur_prev = mo["gsdp"]["FY2024-25"][0]
con_last = mo["gsdp"]["FY2025-26"][1]; con_prev = mo["gsdp"]["FY2024-25"][1]
module(R, "economy", [
    prose("p1", L(
        "Maharashtra has the largest economy of any Indian State. In the MoSPI series for FY2024-25, its GSDP at current prices was about ₹46.2 lakh crore, well ahead of the next States, Tamil Nadu and Uttar Pradesh. Services dominate: finance, real estate and professional services together make up the single largest block of output, reflecting Mumbai's role as the home of the Reserve Bank of India, SEBI and the BSE and NSE stock exchanges.\n\nManufacturing is concentrated in the Mumbai–Thane–Pune belt, Nashik, Chhatrapati Sambhajinagar and Nagpur, with strong automotive, engineering, chemicals, pharmaceuticals and IT industries. Agriculture employs a large share of the workforce; the State is a major producer of sugarcane, cotton, soybean, onions, grapes and pomegranates, but large parts depend on rain-fed farming.",
        "महाराष्ट्र की अर्थव्यवस्था देश के सभी राज्यों में सबसे बड़ी है। मोस्पी (MoSPI) शृंखला के अनुसार वित्त वर्ष 2024-25 में प्रचलित मूल्यों पर इसका जीएसडीपी लगभग ₹46.2 लाख करोड़ था, जो अगले राज्यों तमिलनाडु और उत्तर प्रदेश से काफ़ी आगे है। सेवा क्षेत्र का दबदबा है: वित्त, रियल एस्टेट और पेशेवर सेवाएँ मिलकर उत्पादन का सबसे बड़ा हिस्सा हैं, क्योंकि मुंबई में भारतीय रिज़र्व बैंक, सेबी तथा बीएसई और एनएसई शेयर बाज़ार हैं।\n\nविनिर्माण मुख्यतः मुंबई–ठाणे–पुणे पट्टी, नासिक, छत्रपति संभाजीनगर और नागपुर में केंद्रित है, जहाँ ऑटोमोबाइल, इंजीनियरिंग, रसायन, दवा और आईटी उद्योग मज़बूत हैं। खेती में कार्यबल का बड़ा हिस्सा लगा है; राज्य गन्ना, कपास, सोयाबीन, प्याज़, अंगूर और अनार का प्रमुख उत्पादक है, पर बड़ा हिस्सा वर्षा पर निर्भर खेती पर टिका है।",
        "महाराष्ट्राची अर्थव्यवस्था देशातील सर्व राज्यांत सर्वांत मोठी आहे. मोस्पी (MoSPI) मालिकेनुसार आर्थिक वर्ष 2024-25 मध्ये चालू किमतींनुसार राज्याचे जीएसडीपी सुमारे ₹46.2 लाख कोटी होते, जे पुढील राज्यांपेक्षा — तमिळनाडू आणि उत्तर प्रदेश — बरेच अधिक आहे. सेवा क्षेत्राचे वर्चस्व आहे: वित्त, स्थावर मालमत्ता आणि व्यावसायिक सेवा मिळून उत्पादनाचा सर्वांत मोठा वाटा आहेत, कारण मुंबईत भारतीय रिझर्व्ह बँक, सेबी आणि बीएसई व एनएसई शेअर बाजार आहेत.\n\nउत्पादन उद्योग प्रामुख्याने मुंबई–ठाणे–पुणे पट्टा, नाशिक, छत्रपती संभाजीनगर आणि नागपूर येथे केंद्रित असून वाहन, अभियांत्रिकी, रसायने, औषधनिर्मिती आणि आयटी उद्योग प्रबळ आहेत. शेतीत कार्यबलाचा मोठा भाग गुंतलेला आहे; ऊस, कापूस, सोयाबीन, कांदा, द्राक्षे आणि डाळिंब यांचे राज्य मोठे उत्पादक आहे, मात्र मोठा भाग पावसावर अवलंबून असलेल्या शेतीवर चालतो."),
        sources=["mospi"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur_last, "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE), "rupeeCrore", "higher-is-better",
             previous=dp(cur_prev, "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(con_last, "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE), "rupeeCrore", "higher-is-better",
             previous=dp(con_prev, "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(mo["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE), "rupee", "higher-is-better",
             previous=dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("rank", L("GSDP rank among States/UTs (FY2024-25)", "राज्यों/केंद्र शासित प्रदेशों में जीएसडीपी रैंक (वित्त वर्ष 2024-25)", "राज्ये/केंद्रशासित प्रदेशांत जीएसडीपी क्रमांक (आ.व. 2024-25)"),
             dp(1, "rank (current prices)", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
                note="Rank among the 29 States/UTs with FY2024-25 figures in the MoSPI series at access time. Absolute ranking, not per capita."), "number"),
        fact("ur", L("Unemployment rate, 15+ (PS+SS)", "बेरोज़गारी दर, 15+ (पीएस+एसएस)", "बेरोजगारी दर, 15+ (पीएस+एसएस)"),
             dp(2.4, "%", "2025", "calendar", "plfs", MOSPI, note="PLFS annual, calendar year, usual status (PS+SS), persons 15 years and above."), "percent", "lower-is-better",
             previous=dp(2.9, "%", "2024", "calendar", "plfs", MOSPI), national=dp(3.1, "%", "2025", "calendar", "plfs", MOSPI, level="national")),
        fact("lfpr", L("Labour force participation, women 15+", "श्रम बल भागीदारी, महिलाएँ 15+", "श्रमशक्ती सहभाग, महिला 15+"),
             dp(39.9, "%", "2025", "calendar", "plfs", MOSPI, note="PLFS annual 2025, PS+SS. All persons: 59.5% (India 59.3%)."), "percent", "higher-is-better",
             national=dp(40.0, "%", "2025", "calendar", "plfs", MOSPI, level="national")),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    {"type": "series", "id": "gsdp-series", "title": L("GSDP, FY2011-12 to FY2025-26", "जीएसडीपी, वित्त वर्ष 2011-12 से 2025-26", "जीएसडीपी, आ.व. 2011-12 ते 2025-26"),
     "kind": "rupeeCrore", "polarity": "higher-is-better",
     "series": [
         {"id": "current", "label": L("Current prices", "प्रचलित मूल्य", "चालू किमती"), "points": fy_points("gsdp", 0, "₹ crore", CUR, NOTE)},
         {"id": "constant", "label": L("Constant 2011-12 prices", "स्थिर 2011-12 मूल्य", "स्थिर 2011-12 किमती"), "points": fy_points("gsdp", 1, "₹ crore", CON, NOTE)},
     ],
     "note": L("Current prices include inflation; constant prices show real growth. The dip in FY2020-21 reflects the pandemic year. MoSPI has released a new 2022-23 base for national accounts; State series in that base were not yet available at access time.",
               "प्रचलित मूल्यों में महँगाई शामिल है; स्थिर मूल्य वास्तविक वृद्धि दिखाते हैं। वित्त वर्ष 2020-21 की गिरावट महामारी वर्ष को दर्शाती है। मोस्पी ने राष्ट्रीय लेखों के लिए नया 2022-23 आधार जारी किया है; उस आधार पर राज्य शृंखला देखे जाने के समय उपलब्ध नहीं थी।",
               "चालू किमतींमध्ये महागाई समाविष्ट असते; स्थिर किमती प्रत्यक्ष वाढ दाखवतात. आ.व. 2020-21 मधील घसरण महामारीच्या वर्षामुळे आहे. मोस्पीने राष्ट्रीय लेख्यांसाठी नवे 2022-23 आधारवर्ष जाहीर केले आहे; त्या आधारावरची राज्य मालिका पाहिली तेव्हा उपलब्ध नव्हती.")},
    {"type": "series", "id": "pc-series", "title": L("Per capita NSDP", "प्रति व्यक्ति एनएसडीपी", "दरडोई एनएसडीपी"),
     "kind": "rupee", "polarity": "higher-is-better",
     "series": [
         {"id": "current", "label": L("Current prices", "प्रचलित मूल्य", "चालू किमती"), "points": fy_points("pcnsdp", 0, "₹", CUR, NOTE)},
         {"id": "constant", "label": L("Constant 2011-12 prices", "स्थिर 2011-12 मूल्य", "स्थिर 2011-12 किमती"), "points": fy_points("pcnsdp", 1, "₹", CON, NOTE)},
     ]},
    table("sectors", L("Sectoral shares of GSVA, FY2024-25 (current prices)", "जीएसवीए में क्षेत्रवार हिस्सा, वित्त वर्ष 2024-25 (प्रचलित मूल्य)", "जीएसव्हीएमधील क्षेत्रनिहाय वाटा, आ.व. 2024-25 (चालू किमती)"),
          [col(L("Sector", "क्षेत्र", "क्षेत्र")), col(L("Share of GSVA (%)", "जीएसवीए में हिस्सा (%)", "जीएसव्हीएमधील वाटा (%)"), "right")],
          [[L("Agriculture, livestock, forestry & fishing", "कृषि, पशुपालन, वानिकी और मत्स्य", "कृषी, पशुपालन, वनीकरण व मत्स्य"), f"{pct(g['agri']):.2f}"],
           [L("Mining & quarrying", "खनन और उत्खनन", "खाणकाम व उत्खनन"), f"{pct(g['mining']):.2f}"],
           [L("Manufacturing", "विनिर्माण", "उत्पादन उद्योग"), f"{pct(g['manufacturing']):.2f}"],
           [L("Electricity, gas, water & utilities", "बिजली, गैस, जल और उपयोगिताएँ", "वीज, वायू, पाणी व उपयुक्त सेवा"), f"{pct(g['utilities']):.2f}"],
           [L("Construction", "निर्माण", "बांधकाम"), f"{pct(g['construction']):.2f}"],
           [L("Trade, repair, hotels & restaurants", "व्यापार, मरम्मत, होटल और रेस्तराँ", "व्यापार, दुरुस्ती, हॉटेल व उपाहारगृहे"), f"{pct(g['trade_hotels']):.2f}"],
           [L("Transport, storage & communication", "परिवहन, भंडारण और संचार", "वाहतूक, साठवण व दळणवळण"), f"{pct(g['transport_comm']):.2f}"],
           [L("Financial services", "वित्तीय सेवाएँ", "वित्तीय सेवा"), f"{pct(g['financial']):.2f}"],
           [L("Real estate, dwellings & professional services", "रियल एस्टेट, आवास और पेशेवर सेवाएँ", "स्थावर मालमत्ता, निवास व व्यावसायिक सेवा"), f"{pct(g['realestate_prof']):.2f}"],
           [L("Public administration", "लोक प्रशासन", "लोकप्रशासन"), f"{pct(g['public_admin']):.2f}"],
           [L("Other services", "अन्य सेवाएँ", "इतर सेवा"), f"{pct(g['other']):.2f}"]],
          "mospi", MOSPI, period="FY2024-25",
          note=L(f"Computed from MoSPI GSVA by industry (₹ lakh). Primary sector {pct(g['agri']+g['mining']):.1f}%, secondary {pct(g['manufacturing']+g['utilities']+g['construction']):.1f}%, services {pct(g['trade_hotels']+g['transport_comm']+g['financial']+g['realestate_prof']+g['public_admin']+g['other']):.1f}%.",
                 f"मोस्पी के उद्योगवार जीएसवीए (₹ लाख) से गणना। प्राथमिक क्षेत्र {pct(g['agri']+g['mining']):.1f}%, द्वितीयक {pct(g['manufacturing']+g['utilities']+g['construction']):.1f}%, सेवाएँ {pct(g['trade_hotels']+g['transport_comm']+g['financial']+g['realestate_prof']+g['public_admin']+g['other']):.1f}%।",
                 f"मोस्पीच्या उद्योगनिहाय जीएसव्हीए (₹ लाख) वरून गणना. प्राथमिक क्षेत्र {pct(g['agri']+g['mining']):.1f}%, द्वितीयक {pct(g['manufacturing']+g['utilities']+g['construction']):.1f}%, सेवा {pct(g['trade_hotels']+g['transport_comm']+g['financial']+g['realestate_prof']+g['public_admin']+g['other']):.1f}%.")),
    {"type": "series", "id": "ur-series", "title": L("Unemployment rate, persons 15+ (PLFS)", "बेरोज़गारी दर, 15+ आयु (पीएलएफ़एस)", "बेरोजगारी दर, 15+ वय (पीएलएफएस)"),
     "kind": "percent", "polarity": "lower-is-better",
     "series": [
         {"id": "mh", "label": L("Maharashtra", "महाराष्ट्र", "महाराष्ट्र"), "points": [dp(v, "%", y, "calendar", "plfs", MOSPI, note="PS+SS, calendar year.") for y, v in [("2022", 3.4), ("2023", 3.1), ("2024", 2.9), ("2025", 2.4)]]},
         {"id": "in", "label": L("India", "भारत", "भारत"), "points": [dp(v, "%", y, "calendar", "plfs", MOSPI, level="national") for y, v in [("2022", 3.6), ("2023", 3.1), ("2024", 3.2), ("2025", 3.1)]]},
     ]},
    table("crops", L("Principal crops by area (average of 2018-19 to 2020-21)", "क्षेत्रफल के अनुसार प्रमुख फ़सलें (2018-19 से 2020-21 का औसत)", "क्षेत्रानुसार प्रमुख पिके (2018-19 ते 2020-21 सरासरी)"),
          [col(L("Crop", "फ़सल", "पीक")), col(L("Area ('000 ha)", "क्षेत्रफल ('000 हे.)", "क्षेत्र ('000 हे.)"), "right")],
          [[L("Cotton", "कपास", "कापूस"), 4418], [L("Jowar", "ज्वार", "ज्वारी"), 2000], [L("Rice", "धान", "भात"), 1526],
           [L("Sugarcane (harvested)", "गन्ना (कटाई)", "ऊस (तोडणी)"), 1043], [L("Wheat", "गेहूँ", "गहू"), 1006], [L("Bajra", "बाजरा", "बाजरी"), 657], [L("Groundnut", "मूँगफली", "भुईमूग"), 281]],
          "mh-sdb", SDB, period="2018-21",
          note=L("Net area sown 1,67,22 thousand ha and gross cropped area 2,35,70 thousand ha in 2019-20 (State Data Bank).", "2019-20 में शुद्ध बोया गया क्षेत्र 1,67,22 हज़ार हे. और सकल फ़सली क्षेत्र 2,35,70 हज़ार हे. (राज्य डेटा बैंक)।", "2019-20 मध्ये निव्वळ पेरणी क्षेत्र 1,67,22 हजार हे. आणि एकूण पीक क्षेत्र 2,35,70 हजार हे. (राज्य डेटा बँक).")),
    gaps("g", [
        (L("Share of India's GDP", "भारत के जीडीपी में हिस्सा", "भारताच्या जीडीपीतील वाटा"), "mospi", "Needs the matching all-India GDP in the same base and vintage."),
        (L("FDI equity inflows", "एफ़डीआई इक्विटी प्रवाह", "एफडीआय समभाग गुंतवणूक"), "dpiit", "DPIIT state-wise FDI factsheet (from Oct 2019)."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("Exports and export clusters", "निर्यात और निर्यात क्लस्टर", "निर्यात व निर्यात समूह"), "dpiit", "DGCI&S state-wise exports."),
        (L("Ease of Doing Business (BRAP) ranking", "कारोबार सुगमता (बीआरएपी) रैंकिंग", "व्यवसाय सुलभता (बीआरएपी) क्रमवारी"), "dpiit", "Latest BRAP assessment."),
    ]),
])

# ---------------- I. Government ----------------
P = lambda en, hi, mr: L(en, hi, mr)
module(R, "government", [
    prose("p1", L(
        "Maharashtra has a bicameral legislature: a 288-member Legislative Assembly (Vidhan Sabha) and a 78-member Legislative Council (Vidhan Parishad). The legislature meets in Mumbai and holds its winter session in Nagpur, under the 1953 Nagpur Agreement. The State sends 48 members to the Lok Sabha and 19 to the Rajya Sabha.\n\nArticle 371(2) of the Constitution lets the Governor set up separate development boards for Vidarbha, Marathwada and the rest of Maharashtra, to ensure a fair share of spending. The Bombay High Court is seated in Mumbai, with benches at Nagpur, Chhatrapati Sambhajinagar and Panaji (Goa), and a bench at Kolhapur that began sitting in August 2025.",
        "महाराष्ट्र में द्विसदनीय विधानमंडल है: 288 सदस्यों वाली विधानसभा और 78 सदस्यों वाली विधान परिषद। विधानमंडल मुंबई में बैठता है और 1953 के नागपुर समझौते के तहत अपना शीतकालीन सत्र नागपुर में करता है। राज्य से लोकसभा में 48 और राज्यसभा में 19 सदस्य जाते हैं।\n\nसंविधान का अनुच्छेद 371(2) राज्यपाल को विदर्भ, मराठवाड़ा और शेष महाराष्ट्र के लिए अलग विकास बोर्ड बनाने का अधिकार देता है, ताकि खर्च में न्यायसंगत हिस्सा सुनिश्चित हो। बॉम्बे उच्च न्यायालय मुंबई में है, जिसकी पीठें नागपुर, छत्रपति संभाजीनगर और पणजी (गोवा) में हैं, और कोल्हापुर पीठ अगस्त 2025 से बैठने लगी।",
        "महाराष्ट्रात द्विसदनी विधिमंडळ आहे: 288 सदस्यांची विधानसभा आणि 78 सदस्यांची विधान परिषद. विधिमंडळाचे कामकाज मुंबईत चालते आणि 1953 च्या नागपूर करारानुसार हिवाळी अधिवेशन नागपुरात भरते. राज्यातून लोकसभेवर 48 आणि राज्यसभेवर 19 सदस्य जातात.\n\nराज्यघटनेच्या अनुच्छेद 371(2) नुसार राज्यपाल विदर्भ, मराठवाडा आणि उर्वरित महाराष्ट्रासाठी स्वतंत्र विकास मंडळे स्थापन करू शकतात, जेणेकरून निधीचे न्याय्य वाटप व्हावे. मुंबई उच्च न्यायालय मुंबईत असून त्याची खंडपीठे नागपूर, छत्रपती संभाजीनगर आणि पणजी (गोवा) येथे आहेत, तर कोल्हापूर खंडपीठाचे कामकाज ऑगस्ट 2025 पासून सुरू झाले."),
        sources=["eci", "sansad", "bar-and-bench"], conf="Third-party verified"),
    {"type": "officeholders", "id": "officeholders"},
    table("results", L("Legislative Assembly election, November 2024 — seats won", "विधानसभा चुनाव, नवंबर 2024 — जीती गई सीटें", "विधानसभा निवडणूक, नोव्हेंबर 2024 — जिंकलेल्या जागा"),
          [col(L("Party", "दल", "पक्ष")), col(L("Seats", "सीटें", "जागा"), "right")],
          [["Bharatiya Janata Party (BJP)", 132], ["Shiv Sena (SHS)", 57], ["Nationalist Congress Party (NCP)", 41],
           ["Shiv Sena (Uddhav Balasaheb Thackeray) (SHSUBT)", 20], ["Indian National Congress (INC)", 16],
           ["Nationalist Congress Party – Sharadchandra Pawar (NCPSP)", 10], ["Samajwadi Party (SP)", 2], ["Jan Surajya Shakti (JSS)", 2],
           [L("Other parties (one seat each: RSHYVSWBHM, RSPS, AIMIM, CPI(M), PWPI, RSVA)", "अन्य दल (एक-एक सीट: RSHYVSWBHM, RSPS, AIMIM, CPI(M), PWPI, RSVA)", "इतर पक्ष (प्रत्येकी एक जागा: RSHYVSWBHM, RSPS, AIMIM, CPI(M), PWPI, RSVA)"), 6],
           [L("Independents", "निर्दलीय", "अपक्ष"), 2],
           [L("Total", "कुल", "एकूण"), 288]],
          "eci", ECI, period="2024",
          note=L("Party names as listed by the Election Commission. Parties are shown in order of seats, without colours or commentary. The next general election to the Assembly is due by late 2029.",
                 "दलों के नाम चुनाव आयोग की सूची के अनुसार। दलों को सीटों के क्रम में दिखाया गया है, बिना रंग या टिप्पणी के। विधानसभा का अगला आम चुनाव 2029 के अंत तक होना है।",
                 "पक्षांची नावे निवडणूक आयोगाच्या यादीनुसार. पक्ष जागांच्या क्रमाने, रंग किंवा भाष्याशिवाय दाखवले आहेत. विधानसभेची पुढील सार्वत्रिक निवडणूक 2029 च्या अखेरीस अपेक्षित आहे.")),
    lst("links", [
        item("eci", L("Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग"), url="https://www.eci.gov.in", src="eci"),
        item("sec", L("State Election Commission, Maharashtra", "राज्य निर्वाचन आयोग, महाराष्ट्र", "राज्य निवडणूक आयोग, महाराष्ट्र"), url="https://mahasec.maharashtra.gov.in", src="mh-gov"),
        item("leg", L("Maharashtra Legislature", "महाराष्ट्र विधानमंडल", "महाराष्ट्र विधिमंडळ"), url="https://mls.org.in", src="mh-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Speaker and Leader of Opposition", "विधानसभा अध्यक्ष और नेता प्रतिपक्ष", "विधानसभा अध्यक्ष व विरोधी पक्षनेते"), "mh-gov", "Verify on mls.org.in with asOf."),
        (L("Municipal corporations and councils (count)", "नगर निगम और नगर परिषदें (संख्या)", "महानगरपालिका व नगरपरिषदा (संख्या)"), "mh-gov", "Urban Development Department."),
        (L("Zilla parishads and gram panchayats (count)", "ज़िला परिषदें और ग्राम पंचायतें (संख्या)", "जिल्हा परिषदा व ग्रामपंचायती (संख्या)"), "mh-gov", "Rural Development Department."),
        (L("Flagship welfare schemes", "प्रमुख कल्याण योजनाएँ", "प्रमुख कल्याणकारी योजना"), "mh-gov", "List with official scheme pages and current status."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Maharashtra is in the middle of a large transport build-out, much of it around the Mumbai Metropolitan Region. Recent completions include the Atal Setu sea bridge, the full Samruddhi expressway from Nagpur, Mumbai Metro Line 3 and the first phase of Navi Mumbai International Airport. Major works still under way include the Mumbai–Ahmedabad high-speed rail line and the Vadhavan deep-sea port in Palghar.\n\nEach project below shows its status only as stated by an official source, with the date it was checked.",
        "महाराष्ट्र में परिवहन ढाँचे का बड़ा निर्माण चल रहा है, जिसका बड़ा हिस्सा मुंबई महानगर क्षेत्र के आसपास है। हाल में पूरे हुए कामों में अटल सेतु समुद्री पुल, नागपुर से पूरा समृद्धि एक्सप्रेसवे, मुंबई मेट्रो लाइन 3 और नवी मुंबई अंतरराष्ट्रीय हवाई अड्डे का पहला चरण शामिल हैं। मुंबई–अहमदाबाद हाई-स्पीड रेल और पालघर का वाढवण गहरे समुद्र का बंदरगाह अभी निर्माणाधीन हैं।\n\nनीचे हर परियोजना की स्थिति केवल आधिकारिक स्रोत के अनुसार, जाँच की तारीख़ के साथ दिखाई गई है।",
        "महाराष्ट्रात वाहतूक पायाभूत सुविधांची मोठी उभारणी सुरू असून तिचा मोठा भाग मुंबई महानगर प्रदेशाभोवती आहे. नुकत्याच पूर्ण झालेल्या कामांत अटल सेतू सागरी पूल, नागपूरपासूनचा संपूर्ण समृद्धी महामार्ग, मुंबई मेट्रो मार्गिका 3 आणि नवी मुंबई आंतरराष्ट्रीय विमानतळाचा पहिला टप्पा यांचा समावेश आहे. मुंबई–अहमदाबाद अतिजलद रेल्वे आणि पालघरमधील वाढवण खोल समुद्री बंदर यांचे काम अद्याप सुरू आहे.\n\nखालील प्रत्येक प्रकल्पाची स्थिती केवळ अधिकृत स्रोतानुसार, तपासणीच्या दिनांकासह दाखवली आहे."),
        sources=["pib", "newsonair"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("State vision document (e.g. Viksit Maharashtra 2047)", "राज्य विज़न दस्तावेज़ (जैसे विकसित महाराष्ट्र 2047)", "राज्य दृष्टी दस्तऐवज (उदा. विकसित महाराष्ट्र 2047)"), "mh-gov", "Link the officially published document, if released."),
        (L("Smart Cities and AMRUT cities", "स्मार्ट सिटी और अमृत शहर", "स्मार्ट सिटी व अमृत शहरे"), "mh-gov", "MoHUA lists for Maharashtra."),
        (L("Other metro, coastal road and irrigation projects", "अन्य मेट्रो, तटीय सड़क और सिंचाई परियोजनाएँ", "इतर मेट्रो, सागरी किनारा मार्ग व सिंचन प्रकल्प"), "mh-gov", "Add each with an official status source."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Mumbai is the hub of western India's transport network. Chhatrapati Shivaji Maharaj International Airport and the new Navi Mumbai International Airport serve the region, and Pune, Nagpur, Chhatrapati Sambhajinagar, Shirdi and Kolhapur have commercial flights. Two railway zones are headquartered in Mumbai — Central Railway at CSMT and Western Railway at Churchgate — and the Konkan Railway runs south along the coast. The Mumbai suburban network carries millions of passengers a day.\n\nMetro systems run in Mumbai, Pune and Nagpur. The Mumbai–Pune Expressway, opened in the early 2000s, was India's first access-controlled six-lane expressway, and the 701 km Samruddhi Mahamarg now links Nagpur with the Mumbai region. Jawaharlal Nehru Port at Nhava Sheva and Mumbai Port handle a large share of India's container and bulk trade. The Maharashtra State Road Transport Corporation (MSRTC) runs intercity and rural buses across the State.",
        "मुंबई पश्चिम भारत के परिवहन नेटवर्क का केंद्र है। छत्रपति शिवाजी महाराज अंतरराष्ट्रीय हवाई अड्डा और नया नवी मुंबई अंतरराष्ट्रीय हवाई अड्डा इस क्षेत्र को सेवा देते हैं, और पुणे, नागपुर, छत्रपति संभाजीनगर, शिर्डी और कोल्हापुर से व्यावसायिक उड़ानें हैं। दो रेलवे ज़ोन का मुख्यालय मुंबई में है — मध्य रेलवे सीएसएमटी में और पश्चिम रेलवे चर्चगेट में — और कोंकण रेलवे तट के साथ दक्षिण की ओर जाती है। मुंबई का उपनगरीय रेल नेटवर्क रोज़ लाखों यात्रियों को ले जाता है।\n\nमुंबई, पुणे और नागपुर में मेट्रो चलती है। 2000 के दशक की शुरुआत में खुला मुंबई–पुणे एक्सप्रेसवे भारत का पहला प्रवेश-नियंत्रित छह लेन एक्सप्रेसवे था, और 701 किमी लंबा समृद्धि महामार्ग अब नागपुर को मुंबई क्षेत्र से जोड़ता है। न्हावा शेवा का जवाहरलाल नेहरू बंदरगाह और मुंबई बंदरगाह भारत के कंटेनर और थोक व्यापार का बड़ा हिस्सा संभालते हैं। महाराष्ट्र राज्य सड़क परिवहन निगम (एमएसआरटीसी) पूरे राज्य में अंतर-शहरी और ग्रामीण बसें चलाता है।",
        "मुंबई हे पश्चिम भारताच्या वाहतूक जाळ्याचे केंद्र आहे. छत्रपती शिवाजी महाराज आंतरराष्ट्रीय विमानतळ आणि नवा नवी मुंबई आंतरराष्ट्रीय विमानतळ या प्रदेशाला सेवा देतात, तर पुणे, नागपूर, छत्रपती संभाजीनगर, शिर्डी आणि कोल्हापूर येथून व्यावसायिक उड्डाणे होतात. दोन रेल्वे विभागांची मुख्यालये मुंबईत आहेत — मध्य रेल्वे सीएसएमटी येथे आणि पश्चिम रेल्वे चर्चगेट येथे — आणि कोकण रेल्वे किनाऱ्याने दक्षिणेकडे जाते. मुंबईची उपनगरी रेल्वे दररोज लाखो प्रवाशांची ने-आण करते.\n\nमुंबई, पुणे आणि नागपूर येथे मेट्रो धावते. 2000 च्या दशकाच्या सुरुवातीला खुला झालेला मुंबई–पुणे द्रुतगती मार्ग हा भारतातील पहिला प्रवेश-नियंत्रित सहापदरी द्रुतगती मार्ग होता, आणि 701 किमीचा समृद्धी महामार्ग आता नागपूरला मुंबई परिसराशी जोडतो. न्हावा शेवा येथील जवाहरलाल नेहरू बंदर आणि मुंबई बंदर भारताच्या कंटेनर व मोठ्या मालवाहतुकीचा मोठा भाग हाताळतात. महाराष्ट्र राज्य मार्ग परिवहन महामंडळ (एसटी) संपूर्ण राज्यात आंतरशहरी व ग्रामीण बससेवा चालवते."),
        conf="Editorial"),
    lst("airports", [
        item("bom", L("Mumbai — Chhatrapati Shivaji Maharaj Intl (BOM)", "मुंबई — छत्रपति शिवाजी महाराज अंतरराष्ट्रीय (BOM)", "मुंबई — छत्रपती शिवाजी महाराज आंतरराष्ट्रीय (BOM)")),
        item("nmi", L("Navi Mumbai International (NMI)", "नवी मुंबई अंतरराष्ट्रीय (NMI)", "नवी मुंबई आंतरराष्ट्रीय (NMI)")),
        item("pnq", L("Pune (PNQ)", "पुणे (PNQ)", "पुणे (PNQ)")),
        item("nag", L("Nagpur — Dr Babasaheb Ambedkar Intl (NAG)", "नागपुर — डॉ. बाबासाहेब आंबेडकर अंतरराष्ट्रीय (NAG)", "नागपूर — डॉ. बाबासाहेब आंबेडकर आंतरराष्ट्रीय (NAG)")),
        item("ixu", L("Chhatrapati Sambhajinagar (IXU)", "छत्रपति संभाजीनगर (IXU)", "छत्रपती संभाजीनगर (IXU)")),
        item("sag", L("Shirdi (SAG)", "शिर्डी (SAG)", "शिर्डी (SAG)")),
        item("klh", L("Kolhapur (KLH)", "कोल्हापुर (KLH)", "कोल्हापूर (KLH)")),
        item("isk", L("Nashik (ISK)", "नासिक (ISK)", "नाशिक (ISK)")),
        item("ndc", L("Nanded (NDC)", "नांदेड़ (NDC)", "नांदेड (NDC)")),
        item("sdw", L("Sindhudurg (SDW)", "सिंधुदुर्ग (SDW)", "सिंधुदुर्ग (SDW)")),
    ], layout="chips", title=L("Airports with scheduled flights (selected)", "नियमित उड़ानों वाले हवाई अड्डे (चयनित)", "नियमित उड्डाणे असलेले विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("National highway length (km)", "राष्ट्रीय राजमार्ग लंबाई (किमी)", "राष्ट्रीय महामार्ग लांबी (किमी)"), "morth", "MoRTH Basic Road Statistics."),
        (L("Rail route km and stations", "रेल मार्ग किमी और स्टेशन", "रेल्वे मार्ग किमी व स्थानके"), "railways", "Indian Railways Year Book, state-wise."),
        (L("Operational metro km by city", "शहरवार चालू मेट्रो किमी", "शहरनिहाय कार्यरत मेट्रो किमी"), "mh-gov", "MMRDA, MMRCL, Maha-Metro."),
        (L("MSRTC fleet size and e-buses", "एमएसआरटीसी बेड़ा और ई-बसें", "एसटी ताफा व ई-बस"), "mh-gov", "MSRTC annual report."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Maharashtra is one of India's largest electricity producers and consumers. Coal-fired plants at Chandrapur and Koradi in Vidarbha, and at Nashik, provide much of the base load. The Koyna hydroelectric project in Satara district is among the largest in the country, and the Tarapur Atomic Power Station in Palghar, commissioned in 1969, was India's first nuclear power station. Solar and wind capacity has grown quickly, particularly in the drier districts of Marathwada and western Maharashtra.",
        "महाराष्ट्र देश के सबसे बड़े बिजली उत्पादक और उपभोक्ता राज्यों में है। विदर्भ में चंद्रपुर और कोराडी तथा नासिक के कोयला संयंत्र आधार भार का बड़ा हिस्सा देते हैं। सातारा ज़िले की कोयना जलविद्युत परियोजना देश की सबसे बड़ी परियोजनाओं में है, और पालघर का तारापुर परमाणु बिजलीघर, जो 1969 में शुरू हुआ, भारत का पहला परमाणु बिजलीघर था। सौर और पवन क्षमता तेज़ी से बढ़ी है, ख़ासकर मराठवाड़ा और पश्चिमी महाराष्ट्र के सूखे ज़िलों में।",
        "महाराष्ट्र हे देशातील सर्वांत मोठ्या वीज उत्पादक व वापरकर्त्या राज्यांपैकी एक आहे. विदर्भातील चंद्रपूर व कोराडी आणि नाशिक येथील कोळसा प्रकल्प पायाभूत भाराचा मोठा भाग पुरवतात. सातारा जिल्ह्यातील कोयना जलविद्युत प्रकल्प हा देशातील सर्वांत मोठ्या प्रकल्पांपैकी एक आहे, आणि 1969 मध्ये सुरू झालेले पालघरमधील तारापूर अणुऊर्जा केंद्र हे भारतातील पहिले अणुऊर्जा केंद्र होते. सौर व पवन क्षमता वेगाने वाढली आहे, विशेषतः मराठवाडा आणि पश्चिम महाराष्ट्रातील कोरड्या जिल्ह्यांत."),
        conf="Editorial"),
    facts("f", [
        fact("gen", L("Electricity generation (2021-22)", "बिजली उत्पादन (2021-22)", "वीजनिर्मिती (2021-22)"),
             dp(131682, "million kWh", "FY2021-22", "fy", "mh-sdb", SDB, note="Maharashtra State Data Bank."), "number"),
        fact("cons", L("Electricity consumption (2021-22)", "बिजली खपत (2021-22)", "वीज वापर (2021-22)"),
             dp(138779, "million kWh", "FY2021-22", "fy", "mh-sdb", SDB, note="Energy sold to ultimate consumers through distribution licensees."), "number"),
        fact("ind", L("Industrial share of consumption (2021-22)", "खपत में उद्योग का हिस्सा (2021-22)", "वापरातील उद्योगांचा वाटा (2021-22)"),
             dp(38.5, "%", "FY2021-22", "fy", "mh-sdb", SDB), "percent",
             national=dp(33.1, "%", "FY2021-22", "fy", "mh-sdb", SDB, level="national")),
    ]),
    gaps("g", [
        (L("Installed capacity by source (MW)", "स्रोतवार स्थापित क्षमता (मेगावाट)", "स्रोतनिहाय स्थापित क्षमता (मेगावॉट)"), "cea", "CEA monthly installed capacity report, Maharashtra rows."),
        (L("Renewable energy share", "नवीकरणीय ऊर्जा का हिस्सा", "अक्षय ऊर्जेचा वाटा"), "mnre", "MNRE state-wise RE capacity."),
        (L("Per capita consumption", "प्रति व्यक्ति खपत", "दरडोई वापर"), "cea", "CEA General Review."),
    ]),
])
print("mod2 ok")
