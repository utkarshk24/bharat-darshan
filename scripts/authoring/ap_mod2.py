"""Andhra Pradesh modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-AP"
SES = "https://s3.ap-south-1.amazonaws.com/apfinance.gov.in/uploads/index-docs/AP_Socio_Economic_Survey_2024_25.pdf"
ECI = "https://results.eci.gov.in/AcResultGenJune2024/partywiseresult-S01.htm"
AMR_BILL = "https://newsonair.gov.in/cm-n-chandrababu-naidu-welcomes-unanimous-passage-of-andhra-pradesh-reorganisation-bill-2026/"
ESI_LE = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab81.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE_AP = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 16 Oct 2026. "
           "FY2025-26 is the latest year published for Andhra Pradesh and may be revised.")
mo = research("mospi_ap.json")
NAME = L("Andhra Pradesh", "आंध्र प्रदेश", "आंध्र प्रदेश")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Telugu culture has deep roots in Andhra Pradesh. Telugu literature runs from Nannaya, Tikkana and Pothana to the moral verses of Vemana and the modern reformist writing of Gurajada Apparao. Annamacharya of Tallapaka composed thousands of songs to Lord Venkateswara, and Carnatic music is widely learnt. Kuchipudi, one of India's classical dances, takes its name from a village in Krishna district; Burrakatha storytelling, Tholu Bommalata leather puppetry and Veedhi Natakam street theatre are folk forms. Telugu cinema, made largely in Hyderabad, has a huge following in the State.\n\nCrafts include the hand-painted and block-printed Kalamkari of Srikalahasti and Machilipatnam, Kondapalli and Etikoppaka wooden toys, the Bobbili veena, and handloom saris from Uppada, Venkatagiri, Mangalagiri and Dharmavaram.",
        "आंध्र प्रदेश में तेलुगु संस्कृति की जड़ें गहरी हैं। तेलुगु साहित्य नन्नय, तिक्कन और पोतन से लेकर वेमना की नीति-कविताओं और गुरजाड अप्पाराव के आधुनिक सुधारवादी लेखन तक फैला है। ताल्लपाका के अन्नमाचार्य ने भगवान वेंकटेश्वर के लिए हज़ारों गीत रचे, और कर्नाटक संगीत व्यापक रूप से सीखा जाता है। भारत के शास्त्रीय नृत्यों में से एक कुचिपुड़ी का नाम कृष्णा ज़िले के एक गाँव से है; बुर्रकथा कथा-वाचन, तोलु बोम्मलाटा चमड़ा कठपुतली और वीधि नाटकम लोक रूप हैं। अधिकांशतः हैदराबाद में बनने वाले तेलुगु सिनेमा के राज्य में बहुत बड़े प्रशंसक हैं।\n\nशिल्पों में श्रीकालहस्ती और मछलीपट्टनम की हाथ से चित्रित और ठप्पा छपाई वाली कलमकारी, कोंडापल्ली और एटिकोप्पाका के लकड़ी के खिलौने, बोब्बिली वीणा, और उप्पाडा, वेंकटगिरि, मंगलगिरि और धर्मावरम की हथकरघा साड़ियाँ शामिल हैं।",
        "आंध्र प्रदेशात तेलुगु संस्कृतीची मुळे खोल आहेत. तेलुगु साहित्य नन्नय, तिक्कन व पोतनापासून वेमनाच्या नीतिपर कवितांपर्यंत आणि गुरजाड अप्पाराव यांच्या आधुनिक सुधारणावादी लेखनापर्यंत पसरले आहे. ताळ्ळपाकाच्या अन्नमाचार्यांनी भगवान वेंकटेश्वरासाठी हजारो पदे रचली, आणि कर्नाटक संगीत मोठ्या प्रमाणावर शिकले जाते. भारतातील अभिजात नृत्यांपैकी कुचिपुडीचे नाव कृष्णा जिल्ह्यातील एका गावावरून आहे; बुर्रकथा कथाकथन, तोलू बोम्मलाटा चामडी कठपुतळी व वीधी नाटकम हे लोककलाप्रकार आहेत. मुख्यतः हैदराबादमध्ये बनणाऱ्या तेलुगु चित्रपटांचे राज्यात प्रचंड चाहते आहेत.\n\nहस्तकलेत श्रीकालहस्ती व मछलीपट्टणमची हाताने रंगवलेली व ठसे छपाईची कलमकारी, कोंडापल्ली व एटिकोप्पाकाची लाकडी खेळणी, बोब्बिली वीणा, आणि उप्पाडा, वेंकटगिरी, मंगळगिरी व धर्मावरमच्या हातमाग साड्या यांचा समावेश आहे."),
        conf="Editorial"),
    lst("festivals", [
        fest("sankranti", "Sankranti", "संक्रांति", "संक्रांत", ("January", "जनवरी", "जानेवारी"),
             ("The biggest festival of the coast: rangoli (muggulu), kites, new harvest, family reunions.", "तट का सबसे बड़ा त्योहार: रंगोली (मुग्गुलु), पतंगें, नई फ़सल, परिवार का मिलन।", "किनारपट्टीचा सर्वांत मोठा सण: रांगोळी (मुग्गुलू), पतंग, नवी कापणी, कुटुंबांचे एकत्र येणे.")),
        fest("ugadi", "Ugadi", "उगादि", "उगादी", ("March–April", "मार्च–अप्रैल", "मार्च–एप्रिल"),
             ("Telugu New Year, marked with ugadi pachadi of six tastes.", "तेलुगु नववर्ष, छह स्वादों वाली उगादि पचड़ी के साथ।", "तेलुगु नववर्ष, सहा चवींच्या उगादी पचडीसह.")),
        fest("brahmotsavam", "Tirumala Brahmotsavam", "तिरुमला ब्रह्मोत्सवम", "तिरुमला ब्रह्मोत्सवम", ("September–October", "सितंबर–अक्टूबर", "सप्टेंबर–ऑक्टोबर"),
             ("Nine-day festival of Lord Venkateswara with processions of the deity.", "भगवान वेंकटेश्वर का नौ दिन का उत्सव, देवता की शोभायात्राओं के साथ।", "भगवान वेंकटेश्वराचा नऊ दिवसांचा उत्सव, देवतेच्या मिरवणुकांसह.")),
        fest("dasara", "Dasara at Vijayawada", "विजयवाड़ा में दशहरा", "विजयवाड्यातील दसरा", ("September–October", "सितंबर–अक्टूबर", "सप्टेंबर–ऑक्टोबर"),
             ("Worship of Kanaka Durga on Indrakeeladri hill.", "इंद्रकीलाद्री पहाड़ी पर कनक दुर्गा की पूजा।", "इंद्रकीलाद्री टेकडीवर कनकदुर्गेची पूजा.")),
        fest("vinayaka", "Vinayaka Chavithi", "विनायक चविथि", "विनायक चवथी", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Ganesha festival with clay idols in homes and streets.", "घरों और गलियों में मिट्टी की मूर्तियों के साथ गणेश उत्सव।", "घरोघरी व रस्त्यांवर मातीच्या मूर्तींसह गणेशोत्सव.")),
        fest("eid", "Eid, Christmas and Muharram", "ईद, क्रिसमस और मुहर्रम", "ईद, नाताळ व मोहरम", ("Various", "विभिन्न", "विविध"),
             ("Widely observed across the State.", "पूरे राज्य में व्यापक रूप से मनाए जाते हैं।", "राज्यभर मोठ्या प्रमाणावर पाळले जातात.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("kuchipudi", "Kuchipudi", "कुचिपुड़ी", "कुचिपुडी"), it3("burrakatha", "Burrakatha", "बुर्रकथा", "बुर्रकथा"),
        it3("tholu", "Tholu Bommalata (leather puppetry)", "तोलु बोम्मलाटा (चमड़ा कठपुतली)", "तोलू बोम्मलाटा (चामडी कठपुतळी)"),
        it3("kalamkari", "Kalamkari", "कलमकारी", "कलमकारी"), it3("kondapalli", "Kondapalli toys", "कोंडापल्ली खिलौने", "कोंडापल्ली खेळणी"),
        it3("etikoppaka", "Etikoppaka lacquerware", "एटिकोप्पाका लाख के खिलौने", "एटिकोप्पाका लाखेची खेळणी"), it3("veena", "Bobbili veena", "बोब्बिली वीणा", "बोब्बिली वीणा"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("meals", "Andhra meals", "आंध्र भोजन", "आंध्र जेवण", d=("Rice with dal, pappu, rasam, curd and fiery pickles such as gongura and avakaya mango.", "दाल, पप्पु, रसम, दही और गोंगुरा व आवकाया आम जैसे तीखे अचारों के साथ चावल।", "डाळ, पप्पू, रसम, दही आणि गोंगुरा व आवकाया आंबा यांसारख्या तिखट लोणच्यांसह भात.")),
        it3("pesarattu", "Pesarattu", "पेसरट्टु", "पेसरट्टू", d=("Green-gram dosa, often with upma inside.", "मूँग का डोसा, अक्सर अंदर उपमा के साथ।", "मुगाचा डोसा, अनेकदा आत उपम्यासह.")),
        it3("pulihora", "Pulihora", "पुलिहोरा", "पुलिहोरा", d=("Tamarind rice, a temple and festival favourite.", "इमली वाले चावल, मंदिरों और त्योहारों में प्रिय।", "चिंचेचा भात, मंदिरांत व सणांत आवडता.")),
        it3("ragi", "Ragi sangati", "रागी संगटि", "नाचणी संगटी", d=("Finger-millet balls eaten with curries in Rayalaseema.", "रायलसीमा में करी के साथ खाए जाने वाले रागी के गोले।", "रायलसीमामध्ये आमटीसोबत खाल्ले जाणारे नाचणीचे गोळे.")),
        it3("sweets", "Pootharekulu, Bandar laddu and Tirupati laddu", "पूतरेकुलु, बंदर लड्डू और तिरुपति लड्डू", "पूतरेकुलू, बंदर लाडू व तिरुपती लाडू", d=("Three sweets with registered GIs.", "पंजीकृत जीआई वाली तीन मिठाइयाँ।", "नोंदणीकृत जीआय असलेल्या तीन मिठाया.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("saree", "Handloom saris with half-saree (langa voni) for girls", "हथकरघा साड़ियाँ, और लड़कियों के लिए हाफ़-साड़ी (लंगा वोणी)", "हातमाग साड्या, आणि मुलींसाठी हाफ-साडी (लंगा वोणी)", d=("Uppada, Venkatagiri, Mangalagiri and Dharmavaram weaves.", "उप्पाडा, वेंकटगिरि, मंगलगिरि और धर्मावरम की बुनाई।", "उप्पाडा, वेंकटगिरी, मंगळगिरी व धर्मावरमचे विणकाम.")),
        it3("pancha", "Pancha (dhoti) and kanduva", "पंचा (धोती) और कंडुवा", "पंचा (धोतर) व कंडुवा", d=("Traditional men's dress for festivals and temples.", "त्योहारों और मंदिरों के लिए पुरुषों की पारंपरिक पोशाक।", "सण व मंदिरांसाठी पुरुषांचा पारंपरिक पोशाख.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]; mfg = 100 * g["manufacturing"] / g["total"]
module(R, "economy", [
    prose("p1", L(
        f"Andhra Pradesh's GSDP at current prices was about ₹{cur['FY2025-26'][0]/1e5:.2f} lakh crore in FY2025-26 in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2025-26'][0])}. Agriculture, livestock and fishing made up about {agri:.0f}% of GSVA in FY2024-25 — one of the highest shares among the larger States. The deltas grow rice, Guntur is a major chilli market, and Rayalaseema grows groundnut and horticultural crops; the State's Socio Economic Survey 2024-25 puts foodgrain output at 161.86 lakh tonnes (second advance estimates) and fish production at 41.38 lakh tonnes, much of it farmed shrimp and fish exported from the coast. Manufacturing was about {mfg:.0f}% of GSVA — steel, pharmaceuticals and petrochemicals at Visakhapatnam, automobiles near Anantapur, and electronics and other industry at Sri City near Tirupati.\n\nServices, led by trade, transport, real estate and public services, make up the rest. The PLFS unemployment rate was 4.2% in 2025, and women's labour-force participation was 44.8%.",
        f"मोस्पी शृंखला में वित्त वर्ष 2025-26 में आंध्र प्रदेश का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{cur['FY2025-26'][0]/1e5:.2f} लाख करोड़ था, और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2025-26'][0])} था। वित्त वर्ष 2024-25 में कृषि, पशुपालन और मत्स्य पालन जीएसवीए का लगभग {agri:.0f}% थे — बड़े राज्यों में सबसे ऊँचे हिस्सों में से। डेल्टा में धान उगता है, गुंटूर मिर्च का बड़ा बाज़ार है, और रायलसीमा में मूँगफली और बागवानी फ़सलें होती हैं; राज्य का सामाजिक-आर्थिक सर्वेक्षण 2024-25 खाद्यान्न उत्पादन 161.86 लाख टन (दूसरा अग्रिम अनुमान) और मछली उत्पादन 41.38 लाख टन बताता है, जिसका बड़ा हिस्सा तट से निर्यात होने वाली पाली गई झींगा और मछली है। विनिर्माण जीएसवीए का लगभग {mfg:.0f}% था — विशाखापत्तनम में इस्पात, दवाएँ और पेट्रोरसायन, अनंतपुर के पास ऑटोमोबाइल, और तिरुपति के पास श्री सिटी में इलेक्ट्रॉनिक्स व अन्य उद्योग।\n\nबाक़ी हिस्सा सेवाओं का है — व्यापार, परिवहन, रियल एस्टेट और सार्वजनिक सेवाएँ। 2025 में पीएलएफ़एस बेरोज़गारी दर 4.2% थी, और महिलाओं की श्रम बल भागीदारी 44.8% थी।",
        f"मोस्पी मालिकेनुसार आ.व. 2025-26 मध्ये आंध्र प्रदेशचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{cur['FY2025-26'][0]/1e5:.2f} लाख कोटी होते, आणि दरडोई एनएसडीपी ₹{inr(pc['FY2025-26'][0])} होते. आ.व. 2024-25 मध्ये शेती, पशुपालन व मत्स्यव्यवसायाचा जीएसव्हीएमध्ये सुमारे {agri:.0f}% वाटा होता — मोठ्या राज्यांतील सर्वाधिक वाट्यांपैकी. त्रिभुज प्रदेशात भात पिकतो, गुंटूर ही मिरचीची मोठी बाजारपेठ आहे, आणि रायलसीमात भुईमूग व फलोत्पादन पिके होतात; राज्याचे सामाजिक-आर्थिक सर्वेक्षण 2024-25 अन्नधान्य उत्पादन 161.86 लाख टन (दुसरा आगाऊ अंदाज) आणि मत्स्योत्पादन 41.38 लाख टन सांगते, ज्यातील मोठा भाग किनाऱ्यावरून निर्यात होणारी पाळलेली कोळंबी व मासे आहेत. उत्पादन उद्योगाचा वाटा सुमारे {mfg:.0f}% होता — विशाखापट्टणममध्ये पोलाद, औषधे व पेट्रोरसायने, अनंतपूरजवळ वाहननिर्मिती, आणि तिरुपतीजवळील श्री सिटीमध्ये इलेक्ट्रॉनिक्स व इतर उद्योग.\n\nउर्वरित वाटा सेवाक्षेत्राचा आहे — व्यापार, वाहतूक, स्थावर मालमत्ता व सार्वजनिक सेवा. 2025 मध्ये पीएलएफएस बेरोजगारी दर 4.2% होता, आणि स्त्रियांचा श्रमशक्ती सहभाग 44.8% होता."),
        sources=["mospi", "plfs", "ap-fin"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_AP), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2025-26"][1], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_AP), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_AP), "rupee", "higher-is-better",
             previous=dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("fg", L("Foodgrain production", "खाद्यान्न उत्पादन", "अन्नधान्य उत्पादन"),
             dp(161.86, "lakh tonnes", "FY2024-25", "fy", "ap-fin", SES, rev="provisional", note="Second advance estimates, Socio Economic Survey 2024-25 (paddy 127.15 lakh tonnes)."), "number"),
        fact("fish", L("Fish production", "मछली उत्पादन", "मत्स्योत्पादन"),
             dp(41.38, "lakh tonnes", "FY2024-25", "fy", "ap-fin", SES, rev="provisional", note="As reported in the Socio Economic Survey 2024-25."), "number"),
        *plfs_facts("AP", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2025-26"),
    sect,
    plfs_series("AP", NAME),
    lst("sectors-key", [
        it3("aqua", "Aquaculture and fisheries", "जलकृषि और मत्स्य पालन", "जलशेती व मत्स्यव्यवसाय", d=("Shrimp and fish farms of the Godavari and Krishna deltas; seafood exports.", "गोदावरी और कृष्णा डेल्टा के झींगा व मछली फ़ार्म; समुद्री खाद्य निर्यात।", "गोदावरी व कृष्णा त्रिभुज प्रदेशातील कोळंबी व मत्स्यशेती; सागरी अन्न निर्यात.")),
        it3("agri", "Rice, chillies and horticulture", "धान, मिर्च और बागवानी", "भात, मिरची व फलोत्पादन", d=("Rice in the deltas; chillies around Guntur; mangoes, bananas and other fruit in Rayalaseema.", "डेल्टा में धान; गुंटूर के आसपास मिर्च; रायलसीमा में आम, केले और अन्य फल।", "त्रिभुज प्रदेशात भात; गुंटूरभोवती मिरची; रायलसीमात आंबे, केळी व इतर फळे.")),
        it3("steel", "Steel and heavy industry", "इस्पात और भारी उद्योग", "पोलाद व अवजड उद्योग", d=("Visakhapatnam Steel Plant and the port-based industries of Visakhapatnam.", "विशाखापत्तनम इस्पात संयंत्र और विशाखापत्तनम के बंदरगाह-आधारित उद्योग।", "विशाखापट्टणम पोलाद प्रकल्प व विशाखापट्टणमचे बंदराधारित उद्योग.")),
        it3("pharma", "Pharmaceuticals", "दवा उद्योग", "औषधनिर्मिती", d=("Bulk drug and pharma units around Visakhapatnam.", "विशाखापत्तनम के आसपास बल्क ड्रग और फ़ार्मा इकाइयाँ।", "विशाखापट्टणमभोवती बल्क ड्रग व फार्मा कारखाने.")),
        it3("srcity", "Sri City and electronics", "श्री सिटी और इलेक्ट्रॉनिक्स", "श्री सिटी व इलेक्ट्रॉनिक्स", d=("Multi-product industrial zone on the Tamil Nadu border.", "तमिलनाडु सीमा पर बहु-उत्पाद औद्योगिक क्षेत्र।", "तमिळनाडू सीमेवरील बहुउत्पादन औद्योगिक क्षेत्र.")),
        it3("auto", "Automobiles", "ऑटोमोबाइल", "वाहन उद्योग", d=("Car manufacturing near Penukonda, Sri Sathya Sai district.", "पेनुकोंडा, श्री सत्य साईं ज़िले के पास कार निर्माण।", "पेनुकोंडा, श्री सत्य साई जिल्ह्याजवळ मोटारनिर्मिती.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("FDI equity inflows", "एफ़डीआई इक्विटी प्रवाह", "एफडीआय समभाग गुंतवणूक"), "dpiit", "DPIIT state-wise FDI factsheet."),
        (L("Marine exports from the State", "राज्य से समुद्री निर्यात", "राज्यातून सागरी निर्यात"), "india-gov", "MPEDA state-wise export statistics."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Andhra Pradesh has a bicameral legislature: a 175-member Legislative Assembly and a Legislative Council of 58 members, which meet at Amaravati. The State elects 25 members to the Lok Sabha and 11 to the Rajya Sabha.\n\nIn the Assembly election of 2024 the Telugu Desam Party won 135 seats, the Jana Sena Party 21 and the BJP 8, together forming the government; the YSR Congress Party won 11 (ECI). N. Chandrababu Naidu was sworn in as Chief Minister on 12 June 2024, with Pawan Kalyan of the Jana Sena Party as Deputy Chief Minister. No party in opposition has the one-tenth of seats usually needed for recognition as the official opposition. In 2026 Parliament passed the Andhra Pradesh Reorganisation (Amendment) Bill, confirming Amaravati as the capital.",
        "आंध्र प्रदेश में द्विसदनीय विधानमंडल है: 175 सदस्यों वाली विधानसभा और 58 सदस्यों वाली विधान परिषद, जो अमरावती में बैठती हैं। राज्य से लोकसभा के 25 और राज्यसभा के 11 सदस्य चुने जाते हैं।\n\n2024 के विधानसभा चुनाव में तेलुगु देशम पार्टी ने 135, जन सेना पार्टी ने 21 और भाजपा ने 8 सीटें जीतकर मिलकर सरकार बनाई; वाईएसआर कांग्रेस पार्टी को 11 सीटें मिलीं (भारत निर्वाचन आयोग)। एन. चंद्रबाबू नायडू ने 12 जून 2024 को मुख्यमंत्री पद की शपथ ली, और जन सेना पार्टी के पवन कल्याण उपमुख्यमंत्री बने। विपक्ष के किसी दल के पास आधिकारिक विपक्ष की मान्यता के लिए सामान्यतः आवश्यक दसवाँ हिस्सा सीटें नहीं हैं। 2026 में संसद ने अमरावती को राजधानी के रूप में पुष्ट करने वाला आंध्र प्रदेश पुनर्गठन (संशोधन) विधेयक पारित किया।",
        "आंध्र प्रदेशात द्विसदनी विधिमंडळ आहे: 175 सदस्यांची विधानसभा व 58 सदस्यांची विधान परिषद, जी अमरावती येथे भरते. राज्यातून लोकसभेवर 25 आणि राज्यसभेवर 11 सदस्य निवडले जातात.\n\n2024 च्या विधानसभा निवडणुकीत तेलुगु देसम पक्षाने 135, जनसेना पक्षाने 21 व भाजपने 8 जागा जिंकून एकत्र सरकार स्थापन केले; वायएसआर काँग्रेस पक्षाला 11 जागा मिळाल्या (भारत निवडणूक आयोग). एन. चंद्राबाबू नायडू यांनी 12 जून 2024 रोजी मुख्यमंत्रिपदाची शपथ घेतली, आणि जनसेनेचे पवन कल्याण उपमुख्यमंत्री झाले. अधिकृत विरोधी पक्ष म्हणून मान्यतेसाठी साधारणपणे लागणाऱ्या एक-दशांश जागा विरोधातील कोणत्याही पक्षाकडे नाहीत. 2026 मध्ये संसदेने अमरावतीला राजधानी म्हणून निश्चित करणारे आंध्र प्रदेश पुनर्रचना (सुधारणा) विधेयक मंजूर केले."),
        sources=["eci", "newsonair", "ani"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    table("result2024", L("Assembly election 2024 — seats won", "विधानसभा चुनाव 2024 — जीती गई सीटें", "विधानसभा निवडणूक 2024 — जिंकलेल्या जागा"),
          [col(L("Party", "दल", "पक्ष")), col(L("Seats", "सीटें", "जागा"), "right")],
          [[L("Telugu Desam Party", "तेलुगु देशम पार्टी", "तेलुगु देसम पक्ष"), "135"], [L("Jana Sena Party", "जन सेना पार्टी", "जनसेना पक्ष"), "21"],
           [L("YSR Congress Party", "वाईएसआर कांग्रेस पार्टी", "वायएसआर काँग्रेस पक्ष"), "11"], [L("Bharatiya Janata Party", "भारतीय जनता पार्टी", "भारतीय जनता पक्ष"), "8"],
           [L("Total", "कुल", "एकूण"), "175"]],
          "eci", ECI, period="2024",
          note=L("ECI results website, June 2024.", "भारत निर्वाचन आयोग की परिणाम वेबसाइट, जून 2024।", "भारत निवडणूक आयोगाचे निकाल संकेतस्थळ, जून 2024.")),
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("bill", "News On AIR: Reorganisation (Amendment) Bill passed", "न्यूज़ ऑन एआईआर: पुनर्गठन (संशोधन) विधेयक पारित", "न्यूज ऑन एआयआर: पुनर्रचना (सुधारणा) विधेयक मंजूर", url=AMR_BILL, src="newsonair"),
        it3("portal", "Government of Andhra Pradesh", "आंध्र प्रदेश सरकार", "आंध्र प्रदेश शासन", url="https://www.ap.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Leader of Opposition — official status", "नेता प्रतिपक्ष — आधिकारिक स्थिति", "विरोधी पक्षनेते — अधिकृत स्थिती"), "india-gov", "Assembly secretariat; no party has been recognised as the official opposition."),
        (L("Local bodies by type", "प्रकार के अनुसार स्थानीय निकाय", "प्रकारानुसार स्थानिक स्वराज्य संस्था"), "india-gov", "Panchayat Raj and Municipal Administration departments."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Three projects shape the State's plans: building the capital at Amaravati, completing the Polavaram dam on the Godavari, and the new international airport at Bhogapuram for Visakhapatnam. Each card shows its source and the date it was checked.",
        "तीन परियोजनाएँ राज्य की योजनाओं को आकार देती हैं: अमरावती में राजधानी का निर्माण, गोदावरी पर पोलावरम बाँध को पूरा करना, और विशाखापत्तनम के लिए भोगापुरम में नया अंतरराष्ट्रीय हवाई अड्डा। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "तीन प्रकल्प राज्याच्या योजनांना आकार देतात: अमरावती येथे राजधानीचे बांधकाम, गोदावरीवरील पोलावरम धरण पूर्ण करणे, आणि विशाखापट्टणमसाठी भोगापुरम येथे नवे आंतरराष्ट्रीय विमानतळ. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pmindia", "newsonair", "sansad"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Polavaram — current physical progress", "पोलावरम — वर्तमान भौतिक प्रगति", "पोलावरम — सध्याची भौतिक प्रगती"), "india-gov", "Ministry of Jal Shakti / Polavaram Project Authority."),
        (L("Amaravati — approved cost and timeline", "अमरावती — स्वीकृत लागत और समय-सीमा", "अमरावती — मंजूर खर्च व कालमर्यादा"), "india-gov", "APCRDA official project list."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Visakhapatnam is one of India's major ports and the base of the Eastern Naval Command; non-major ports at Gangavaram, Kakinada and Krishnapatnam handle coal, fertiliser and container cargo, and the State's Socio Economic Survey counts six operational ports. Vijayawada is one of the busiest railway junctions in southern India, on the main lines between Chennai, Kolkata and Delhi. Airports serve Visakhapatnam, Vijayawada (Gannavaram), Tirupati (Renigunta), Rajahmundry, Kadapa and Kurnool, and the new Alluri Sitarama Raju International Airport at Bhogapuram was inaugurated in August 2026. National highways along the coast form part of the Golden Quadrilateral between Chennai and Kolkata.",
        "विशाखापत्तनम भारत के बड़े बंदरगाहों में से है और पूर्वी नौसेना कमान का मुख्यालय है; गंगावरम, काकीनाडा और कृष्णापट्टनम के गैर-प्रमुख बंदरगाह कोयला, उर्वरक और कंटेनर माल संभालते हैं, और राज्य का सामाजिक-आर्थिक सर्वेक्षण छह चालू बंदरगाह गिनता है। विजयवाड़ा चेन्नई, कोलकाता और दिल्ली के बीच मुख्य रेल लाइनों पर दक्षिण भारत के सबसे व्यस्त रेलवे जंक्शनों में है। विशाखापत्तनम, विजयवाड़ा (गन्नवरम), तिरुपति (रेणिगुंटा), राजमहेंद्रवरम, कडपा और कुरनूल में हवाई अड्डे हैं, और भोगापुरम में नए अल्लूरी सीताराम राजू अंतरराष्ट्रीय हवाई अड्डे का उद्घाटन अगस्त 2026 में हुआ। तट के साथ राष्ट्रीय राजमार्ग चेन्नई और कोलकाता के बीच स्वर्णिम चतुर्भुज का हिस्सा हैं।",
        "विशाखापट्टणम हे भारतातील प्रमुख बंदरांपैकी एक असून पूर्व नौदल कमांडचे मुख्यालय आहे; गंगावरम, काकिनाडा व कृष्णापट्टणम ही बिगर-प्रमुख बंदरे कोळसा, खते व कंटेनर माल हाताळतात, आणि राज्याचे सामाजिक-आर्थिक सर्वेक्षण सहा कार्यरत बंदरे मोजते. विजयवाडा हे चेन्नई, कोलकाता व दिल्लीदरम्यानच्या मुख्य रेल्वे मार्गांवरील दक्षिण भारतातील सर्वांत व्यस्त जंक्शनपैकी एक आहे. विशाखापट्टणम, विजयवाडा (गन्नवरम), तिरुपती (रेणिगुंटा), राजमहेंद्रवरम, कडपा व कर्नूल येथे विमानतळ आहेत, आणि भोगापुरम येथील नव्या अल्लुरी सीताराम राजू आंतरराष्ट्रीय विमानतळाचे उद्घाटन ऑगस्ट 2026 मध्ये झाले. किनाऱ्यालगतचे राष्ट्रीय महामार्ग चेन्नई–कोलकातादरम्यानच्या सुवर्ण चतुष्कोनाचा भाग आहेत."),
        sources=["ap-fin", "pmindia"], conf="Editorial"),
    lst("airports", [
        it3("vtz", "Visakhapatnam", "विशाखापत्तनम", "विशाखापट्टणम", m=("VTZ", "VTZ", "VTZ")),
        it3("bhog", "Alluri Sitarama Raju International Airport, Bhogapuram", "अल्लूरी सीताराम राजू अंतरराष्ट्रीय हवाई अड्डा, भोगापुरम", "अल्लुरी सीताराम राजू आंतरराष्ट्रीय विमानतळ, भोगापुरम"),
        it3("vga", "Vijayawada (Gannavaram)", "विजयवाड़ा (गन्नवरम)", "विजयवाडा (गन्नवरम)", m=("VGA", "VGA", "VGA")),
        it3("tir", "Tirupati (Renigunta)", "तिरुपति (रेणिगुंटा)", "तिरुपती (रेणिगुंटा)", m=("TIR", "TIR", "TIR")),
        it3("rja", "Rajahmundry", "राजमहेंद्रवरम", "राजमहेंद्रवरम", m=("RJA", "RJA", "RJA")),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Road and national highway length", "सड़क और राष्ट्रीय राजमार्ग की लंबाई", "रस्ते व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics."),
        (L("Port cargo handled", "बंदरगाहों द्वारा संभाला गया माल", "बंदरांनी हाताळलेला माल"), "india-gov", "Indian Ports Association; AP Maritime Board."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Andhra Pradesh's installed power capacity was 27,392 MW according to the State's Socio Economic Survey 2024-25. Coal-fired stations — NTPC Simhadri near Visakhapatnam, and State plants at Vijayawada, Krishnapatnam and Muddanur — supply much of the power, and the Srisailam and other hydro stations add more. The State has built large solar parks in Kurnool and Ananthapuramu districts and wind farms in Rayalaseema, and new transmission lines are being laid to carry renewable power from renewable energy zones in Kurnool.",
        "राज्य के सामाजिक-आर्थिक सर्वेक्षण 2024-25 के अनुसार आंध्र प्रदेश की स्थापित बिजली क्षमता 27,392 मेगावाट थी। कोयला आधारित संयंत्र — विशाखापत्तनम के पास एनटीपीसी सिंहाद्रि, और विजयवाड़ा, कृष्णापट्टनम व मुद्दनूर के राज्य संयंत्र — अधिकांश बिजली देते हैं, और श्रीशैलम व अन्य जलविद्युत केंद्र और जोड़ते हैं। राज्य ने कुरनूल और अनंतपुरमु ज़िलों में बड़े सौर पार्क और रायलसीमा में पवन फ़ार्म बनाए हैं, और कुरनूल के अक्षय ऊर्जा क्षेत्रों से बिजली ले जाने के लिए नई पारेषण लाइनें बिछाई जा रही हैं।",
        "राज्याच्या सामाजिक-आर्थिक सर्वेक्षण 2024-25 नुसार आंध्र प्रदेशची स्थापित वीजक्षमता 27,392 मेगावॅट होती. कोळशावरील केंद्रे — विशाखापट्टणमजवळील एनटीपीसी सिंहाद्री, आणि विजयवाडा, कृष्णापट्टणम व मुद्दनूर येथील राज्याची केंद्रे — बहुतांश वीज देतात, आणि श्रीशैलम व इतर जलविद्युत केंद्रे त्यात भर घालतात. राज्याने कर्नूल व अनंतपुरमू जिल्ह्यांत मोठी सौर उद्याने आणि रायलसीमात पवन प्रकल्प उभारले आहेत, आणि कर्नूलमधील अक्षय ऊर्जा क्षेत्रांतून वीज वाहून नेण्यासाठी नव्या पारेषण वाहिन्या टाकल्या जात आहेत."),
        sources=["ap-fin", "pmindia"], conf="Editorial"),
    facts("f", [fact("cap", L("Installed power capacity", "स्थापित बिजली क्षमता", "स्थापित वीजक्षमता"),
                     dp(27392, "MW", "FY2024-25", "fy", "ap-fin", SES, note="Socio Economic Survey 2024-25, Government of Andhra Pradesh."), "number", "higher-is-better")]),
    gaps("g", [
        (L("Capacity by source (coal, solar, wind, hydro)", "स्रोतवार क्षमता (कोयला, सौर, पवन, जल)", "स्रोतनिहाय क्षमता (कोळसा, सौर, पवन, जल)"), "cea", "CEA installed capacity report."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Visakhapatnam is the State's main IT centre, with software parks on the Rushikonda hills, and Vijayawada–Guntur and Tirupati have smaller clusters. Electronics manufacturing is concentrated at Sri City and around Tirupati. The State runs many citizen services through its village and ward secretariats, and the Satish Dhawan Space Centre at Sriharikota makes Andhra Pradesh the home of India's rocket launches.",
        "विशाखापत्तनम राज्य का मुख्य आईटी केंद्र है, जहाँ ऋषिकोंडा पहाड़ियों पर सॉफ़्टवेयर पार्क हैं, और विजयवाड़ा–गुंटूर और तिरुपति में छोटे क्लस्टर हैं। इलेक्ट्रॉनिक्स विनिर्माण श्री सिटी और तिरुपति के आसपास केंद्रित है। राज्य अपने ग्राम और वार्ड सचिवालयों के माध्यम से कई नागरिक सेवाएँ चलाता है, और श्रीहरिकोटा का सतीश धवन अंतरिक्ष केंद्र आंध्र प्रदेश को भारत के रॉकेट प्रक्षेपणों का घर बनाता है।",
        "विशाखापट्टणम हे राज्याचे मुख्य आयटी केंद्र आहे, जिथे ऋषिकोंडा टेकड्यांवर सॉफ्टवेअर पार्क आहेत, आणि विजयवाडा–गुंटूर व तिरुपती येथे लहान समूह आहेत. इलेक्ट्रॉनिक्स उत्पादन श्री सिटी व तिरुपतीभोवती एकवटले आहे. राज्य आपल्या ग्राम व वॉर्ड सचिवालयांमार्फत अनेक नागरी सेवा चालवते, आणि श्रीहरिकोटा येथील सतीश धवन अंतराळ केंद्रामुळे आंध्र प्रदेश हे भारताच्या रॉकेट प्रक्षेपणांचे घर आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (Andhra Pradesh circle, which also covers Telangana)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("AP", NAME)
module(R, "education", [
    prose("p1", L(
        "Andhra Pradesh's higher-education gross enrolment ratio (ages 18–23) was 36.5% in 2021-22 in AISHE, well above the national 28.4%; men's GER (37.7%) was a little above women's (35.2%). The State had 47 universities and 2,602 colleges. School literacy has risen fast since 2011, when it was 67.4% for the present State.\n\nAndhra University at Visakhapatnam (1926) and Sri Venkateswara University at Tirupati are the oldest large universities. National institutions set up after 2014 include IIT Tirupati, IIM Visakhapatnam, IISER Tirupati, NIT Andhra Pradesh at Tadepalligudem and AIIMS Mangalagiri.",
        "एआईएसएचई के अनुसार 2021-22 में आंध्र प्रदेश का उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) 36.5% था, जो राष्ट्रीय 28.4% से काफ़ी अधिक है; पुरुषों का जीईआर (37.7%) महिलाओं (35.2%) से थोड़ा अधिक था। राज्य में 47 विश्वविद्यालय और 2,602 कॉलेज थे। 2011 के बाद से साक्षरता तेज़ी से बढ़ी है, जब वर्तमान राज्य में यह 67.4% थी।\n\nविशाखापत्तनम का आंध्र विश्वविद्यालय (1926) और तिरुपति का श्री वेंकटेश्वर विश्वविद्यालय सबसे पुराने बड़े विश्वविद्यालय हैं। 2014 के बाद बने राष्ट्रीय संस्थानों में आईआईटी तिरुपति, आईआईएम विशाखापत्तनम, आईआईएसईआर तिरुपति, ताडेपल्लीगुडेम में एनआईटी आंध्र प्रदेश और एम्स मंगलगिरि शामिल हैं।",
        "एआयएसएचईनुसार 2021-22 मध्ये आंध्र प्रदेशचे उच्चशिक्षणातील एकूण नोंदणी गुणोत्तर (18–23 वय) 36.5% होते — राष्ट्रीय 28.4% पेक्षा बरेच जास्त; पुरुषांचे जीईआर (37.7%) स्त्रियांपेक्षा (35.2%) किंचित जास्त होते. राज्यात 47 विद्यापीठे व 2,602 महाविद्यालये होती. 2011 नंतर साक्षरता झपाट्याने वाढली आहे; तेव्हा सध्याच्या राज्यात ती 67.4% होती.\n\nविशाखापट्टणमचे आंध्र विद्यापीठ (1926) व तिरुपतीचे श्री वेंकटेश्वर विद्यापीठ ही सर्वांत जुनी मोठी विद्यापीठे आहेत. 2014 नंतर स्थापन झालेल्या राष्ट्रीय संस्थांत आयआयटी तिरुपती, आयआयएम विशाखापट्टणम, आयसर तिरुपती, ताडेपल्लीगुडेम येथील एनआयटी आंध्र प्रदेश व एम्स मंगळगिरी यांचा समावेश आहे."),
        sources=["aishe", "ap-cse"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("au", "Andhra University", "आंध्र विश्वविद्यालय", "आंध्र विद्यापीठ", m=("Visakhapatnam, 1926", "विशाखापत्तनम, 1926", "विशाखापट्टणम, 1926")),
        it3("svu", "Sri Venkateswara University", "श्री वेंकटेश्वर विश्वविद्यालय", "श्री वेंकटेश्वर विद्यापीठ", m=("Tirupati", "तिरुपति", "तिरुपती")),
        it3("iitt", "IIT Tirupati", "आईआईटी तिरुपति", "आयआयटी तिरुपती", m=("Tirupati", "तिरुपति", "तिरुपती")),
        it3("iimv", "IIM Visakhapatnam", "आईआईएम विशाखापत्तनम", "आयआयएम विशाखापट्टणम", m=("Visakhapatnam", "विशाखापत्तनम", "विशाखापट्टणम")),
        it3("iisert", "IISER Tirupati", "आईआईएसईआर तिरुपति", "आयसर तिरुपती", m=("Tirupati", "तिरुपति", "तिरुपती")),
        it3("aiims", "AIIMS Mangalagiri", "एम्स मंगलगिरि", "एम्स मंगळगिरी", m=("Guntur district", "गुंटूर ज़िला", "गुंटूर जिल्हा")),
    ], title=L("Institutions (selected)", "संस्थान (चयनित)", "संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("NIRF-ranked institutions", "एनआईआरएफ़ रैंक वाले संस्थान", "एनआयआरएफ क्रमवारीतील संस्था"), "nirf", "Latest NIRF list filtered to Andhra Pradesh."),
    ]),
])

# ---------------- O. Health ----------------
srs = NF["SRS_2021_PIB_PRID2128024"]
def srsdp(v, unit, period, note=None, level="state"):
    return dp(v, unit, period, "survey" if "-" in period else "calendar", "srs", SRS, note=note, level=level)
module(R, "health", [
    prose("p1", L(
        "Andhra Pradesh has met the national goal for maternal mortality: the maternal mortality ratio was 46 per 1,00,000 live births in 2019-21, against 93 for India. Under-five mortality was 24 per 1,000 live births in 2021 (India 31), and the infant mortality rate fell to 24 in 2020. The birth rate (15.7 per 1,000 in 2020) is among the lowest in India. Life expectancy at birth was 70.0 years in 2014-18 (a figure that includes Telangana for the years before 2014). Almost all births (96.5%) took place in health facilities in NFHS-5, but 31.2% of children under five were stunted.\n\nThe State's main public hospitals include King George Hospital in Visakhapatnam, the Government General Hospitals at Guntur and Vijayawada, SVIMS and the Tirumala Tirupati Devasthanams hospitals at Tirupati, and AIIMS Mangalagiri.",
        "आंध्र प्रदेश ने मातृ मृत्यु का राष्ट्रीय लक्ष्य पूरा कर लिया है: 2019-21 में मातृ मृत्यु अनुपात प्रति 1,00,000 जीवित जन्म पर 46 था, जबकि भारत का 93। 2021 में पाँच वर्ष से कम आयु की मृत्यु दर प्रति 1,000 जीवित जन्म पर 24 (भारत 31) थी, और 2020 में शिशु मृत्यु दर घटकर 24 रह गई। जन्म दर (2020 में प्रति 1,000 पर 15.7) भारत में सबसे कम में से है। 2014-18 में जन्म के समय जीवन प्रत्याशा 70.0 वर्ष थी (यह आँकड़ा 2014 से पहले के वर्षों के लिए तेलंगाना सहित है)। एनएफ़एचएस-5 में लगभग सभी प्रसव (96.5%) स्वास्थ्य संस्थानों में हुए, लेकिन पाँच वर्ष से कम आयु के 31.2% बच्चे ठिगने थे।\n\nराज्य के मुख्य सार्वजनिक अस्पतालों में विशाखापत्तनम का किंग जॉर्ज अस्पताल, गुंटूर और विजयवाड़ा के सरकारी सामान्य अस्पताल, तिरुपति में स्विम्स और तिरुमला तिरुपति देवस्थानम के अस्पताल, और एम्स मंगलगिरि शामिल हैं।",
        "आंध्र प्रदेशने मातामृत्यूचे राष्ट्रीय उद्दिष्ट गाठले आहे: 2019-21 मध्ये मातामृत्यू प्रमाण दर 1,00,000 जिवंत जन्मांमागे 46 होते, तर भारताचे 93. 2021 मध्ये पाच वर्षांखालील मृत्युदर दर 1,000 जिवंत जन्मांमागे 24 (भारत 31) होता, आणि 2020 मध्ये अर्भक मृत्युदर घटून 24 झाला. जन्मदर (2020 मध्ये दर 1,000 मागे 15.7) भारतातील सर्वांत कमींपैकी आहे. 2014-18 मध्ये जन्मतः आयुर्मान 70.0 वर्षे होते (हा आकडा 2014 पूर्वीच्या वर्षांसाठी तेलंगणासह आहे). एनएफएचएस-5 मध्ये जवळपास सर्व प्रसूती (96.5%) आरोग्य संस्थांत झाल्या, पण पाच वर्षांखालील 31.2% मुले खुजी होती.\n\nराज्यातील प्रमुख सार्वजनिक रुग्णालयांत विशाखापट्टणमचे किंग जॉर्ज रुग्णालय, गुंटूर व विजयवाड्याची शासकीय सामान्य रुग्णालये, तिरुपतीमधील स्विम्स व तिरुमला तिरुपती देवस्थानमची रुग्णालये, आणि एम्स मंगळगिरी यांचा समावेश आहे."),
        sources=["srs", "nfhs", "es-india"], conf="Official"),
    facts("srs", [
        fact("mmr", L("Maternal mortality ratio", "मातृ मृत्यु अनुपात", "मातामृत्यू प्रमाण"), srsdp(srs["AP"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", "SRS 2019-21, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", level="national")),
        fact("u5mr", L("Under-five mortality rate", "पाँच वर्ष से कम आयु की मृत्यु दर", "पाच वर्षांखालील मृत्युदर"), srsdp(srs["AP"]["U5MR"], "per 1,000 live births", "2021", "SRS 2021, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["U5MR"], "per 1,000 live births", "2021", level="national")),
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(24, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2. The 2010 figure of 46 is for undivided Andhra Pradesh."), "number", "lower-is-better",
             national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(15.7, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note="SRS 2020 (death rate 6.3)."), "number",
             national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("le", L("Life expectancy at birth", "जन्म के समय जीवन प्रत्याशा", "जन्मतः आयुर्मान"),
             dp(70.0, "years", "2014-18", "survey", "srs", ESI_LE, note="SRS abridged life tables, Economic Survey 2021-22 Statistical Appendix Table 8.1 (male 68.7, female 71.4). Includes Telangana for years before 2014."), "number", "higher-is-better",
             national=dp(69.4, "years", "2014-18", "survey", "srs", ESI_LE, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("AP"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India (Infrastructure & Human Resources)."),
    ]),
])
print("ap mod2 ok")
