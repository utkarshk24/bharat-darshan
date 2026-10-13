import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-DL"
ESD = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/chapter_19_0.pdf"
NOA_RRTS = "https://www.newsonair.gov.in/pm-modi-flags-off-meerut-metro-namo-bharat-train-in-uttar-pradesh"
dl = read("regions/IN-DL.json")["metrics"]; ind = read("india.json")["metrics"]
NAME = L("Delhi", "दिल्ली", "दिल्ली")

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Delhi's recent infrastructure is mostly about moving people across a sprawling region. The 82 km Delhi–Meerut Namo Bharat corridor, India's first regional rapid transit line, was fully opened in February 2026. Delhi Metro's fourth phase is adding new corridors and ring connections. Other works — expressway links, Yamuna riverfront restoration and landfill clearance — are listed as gaps until an official status page is linked.",
        "दिल्ली का हालिया बुनियादी ढाँचा मुख्यतः एक फैले हुए क्षेत्र में लोगों की आवाजाही पर केंद्रित है। भारत की पहली क्षेत्रीय रैपिड ट्रांज़िट लाइन, 82 किमी लंबा दिल्ली–मेरठ नमो भारत कॉरिडोर, फ़रवरी 2026 में पूरी तरह खुल गया। दिल्ली मेट्रो का चौथा चरण नए कॉरिडोर और रिंग कनेक्शन जोड़ रहा है। अन्य काम — एक्सप्रेसवे संपर्क, यमुना तट का पुनर्स्थापन और लैंडफ़िल हटाना — आधिकारिक स्थिति पेज जुड़ने तक कमियों में रखे गए हैं।",
        "दिल्लीतील अलीकडच्या पायाभूत सुविधा मुख्यतः विस्तीर्ण प्रदेशात लोकांच्या ये-जा सुलभ करण्याबद्दल आहेत. भारतातील पहिली प्रादेशिक जलद परिवहन मार्गिका, 82 किमीची दिल्ली–मेरठ नमो भारत मार्गिका, फेब्रुवारी 2026 मध्ये पूर्णपणे खुली झाली. दिल्ली मेट्रोचा चौथा टप्पा नव्या मार्गिका आणि वर्तुळाकार जोडण्या वाढवत आहे. इतर कामे — द्रुतगती मार्गांच्या जोडण्या, यमुना किनाऱ्याचे पुनरुज्जीवन आणि कचराभूमी हटवणे — अधिकृत स्थितीचे पान जोडले जाईपर्यंत त्रुटींमध्ये दाखवली आहेत."),
        sources=["newsonair", "pmindia"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Delhi Metro Phase IV — current progress by corridor", "दिल्ली मेट्रो चरण IV — कॉरिडोरवार वर्तमान प्रगति", "दिल्ली मेट्रो टप्पा IV — मार्गिकानिहाय सद्यस्थिती"), "dmrc", "DMRC project updates."),
        (L("Urban Extension Road-II and Dwarka Expressway (Delhi section)", "अर्बन एक्सटेंशन रोड-II और द्वारका एक्सप्रेसवे (दिल्ली खंड)", "अर्बन एक्स्टेन्शन रोड-II व द्वारका द्रुतगती मार्ग (दिल्ली भाग)"), "nhai", "NHAI / MoRTH status."),
        (L("Yamuna cleaning and riverfront projects", "यमुना सफ़ाई और रिवरफ़्रंट परियोजनाएँ", "यमुना स्वच्छता व नदीकिनारा प्रकल्प"), "dl-gov", "Delhi Jal Board / DDA."),
        (L("Legacy landfill remediation (Ghazipur, Bhalswa, Okhla)", "पुराने लैंडफ़िल का निपटान (ग़ाज़ीपुर, भलस्वा, ओखला)", "जुन्या कचराभूमींचे निराकरण (गाझीपूर, भलस्वा, ओखला)"), "dl-gov", "MCD status reports."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Indira Gandhi International Airport is one of the busiest airports in South Asia. Delhi Metro, opened in 2002, has grown into one of the world's largest metro networks and carries millions of trips a day across Delhi and neighbouring NCR towns; the Namo Bharat RRTS now links Sarai Kale Khan to Meerut. New Delhi, Old Delhi (Delhi Junction), Hazrat Nizamuddin and Anand Vihar are the main railway terminals. Delhi Transport Corporation runs a large and increasingly electric bus fleet, and the Ring Road and Outer Ring Road connect to expressways towards Gurugram, Jaipur, Meerut and Mumbai.",
        "इंदिरा गांधी अंतरराष्ट्रीय हवाई अड्डा दक्षिण एशिया के सबसे व्यस्त हवाई अड्डों में है। 2002 में शुरू हुई दिल्ली मेट्रो दुनिया के सबसे बड़े मेट्रो नेटवर्कों में से एक बन गई है और दिल्ली व पड़ोसी एनसीआर शहरों में रोज़ लाखों यात्राएँ कराती है; नमो भारत आरआरटीएस अब सराय काले ख़ाँ को मेरठ से जोड़ता है। नई दिल्ली, पुरानी दिल्ली (दिल्ली जंक्शन), हज़रत निज़ामुद्दीन और आनंद विहार मुख्य रेलवे टर्मिनल हैं। दिल्ली परिवहन निगम की बड़ी और बढ़ती इलेक्ट्रिक बस सेवा है, और रिंग रोड व आउटर रिंग रोड गुरुग्राम, जयपुर, मेरठ और मुंबई की ओर जाने वाले एक्सप्रेसवे से जुड़ते हैं।",
        "इंदिरा गांधी आंतरराष्ट्रीय विमानतळ हा दक्षिण आशियातील सर्वांत गजबजलेल्या विमानतळांपैकी एक आहे. 2002 मध्ये सुरू झालेली दिल्ली मेट्रो जगातील सर्वांत मोठ्या मेट्रो जाळ्यांपैकी एक झाली असून दिल्ली व शेजारच्या एनसीआर शहरांत दररोज लाखो प्रवास घडवते; नमो भारत आरआरटीएस आता सराय काले खाँला मेरठशी जोडते. नवी दिल्ली, जुनी दिल्ली (दिल्ली जंक्शन), हजरत निजामुद्दीन आणि आनंद विहार ही प्रमुख रेल्वे टर्मिनस आहेत. दिल्ली परिवहन महामंडळाचा मोठा आणि वाढत्या प्रमाणात विजेवर चालणारा बसताफा आहे, आणि रिंग रोड व आऊटर रिंग रोड गुरुग्राम, जयपूर, मेरठ व मुंबईकडे जाणाऱ्या द्रुतगती मार्गांना जोडतात."),
        conf="Editorial"),
    lst("hubs", [
        it3("del", "Indira Gandhi International Airport", "इंदिरा गांधी अंतरराष्ट्रीय हवाई अड्डा", "इंदिरा गांधी आंतरराष्ट्रीय विमानतळ", m=("DEL", "DEL", "DEL")),
        it3("ndls", "New Delhi railway station", "नई दिल्ली रेलवे स्टेशन", "नवी दिल्ली रेल्वे स्थानक", m=("NDLS", "NDLS", "NDLS")),
        it3("dli", "Delhi Junction (Old Delhi)", "दिल्ली जंक्शन (पुरानी दिल्ली)", "दिल्ली जंक्शन (जुनी दिल्ली)", m=("DLI", "DLI", "DLI")),
        it3("nzm", "Hazrat Nizamuddin", "हज़रत निज़ामुद्दीन", "हजरत निजामुद्दीन", m=("NZM", "NZM", "NZM")),
        it3("anvt", "Anand Vihar Terminal", "आनंद विहार टर्मिनल", "आनंद विहार टर्मिनल", m=("ANVT", "ANVT", "ANVT")),
        it3("skk", "Sarai Kale Khan (Namo Bharat)", "सराय काले ख़ाँ (नमो भारत)", "सराय काले खाँ (नमो भारत)", m=("RRTS", "RRTS", "RRTS")),
    ], layout="chips", title=L("Main transport hubs", "मुख्य परिवहन केंद्र", "प्रमुख वाहतूक केंद्रे"), conf="Editorial"),
    gaps("g", [
        (L("Delhi Metro network length and daily ridership", "दिल्ली मेट्रो नेटवर्क लंबाई और दैनिक यात्री", "दिल्ली मेट्रो जाळ्याची लांबी व दैनिक प्रवासी"), "dmrc", "DMRC annual report."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
        (L("Registered vehicles and electric buses", "पंजीकृत वाहन और इलेक्ट्रिक बसें", "नोंदणीकृत वाहने व विजेवरील बसगाड्या"), "dl-planning", "Economic Survey of Delhi, transport chapter."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Delhi generates only a small part of the electricity it uses and buys most of it from power stations elsewhere, through long-term contracts and the market. Its coal-fired plants inside the city, such as Badarpur, have been closed to cut pollution; the remaining local generation is gas-based, plus waste-to-energy and rooftop solar. Electricity is distributed by private–public joint-venture companies and, in the New Delhi area, by the NDMC. Summer peak demand has repeatedly set new records as air-conditioning spreads.",
        "दिल्ली अपनी खपत की बिजली का छोटा हिस्सा ही बनाती है और अधिकांश बिजली दीर्घकालिक अनुबंधों और बाज़ार के ज़रिए बाहर के बिजलीघरों से ख़रीदती है। प्रदूषण कम करने के लिए शहर के भीतर बदरपुर जैसे कोयला बिजलीघर बंद किए गए हैं; बची हुई स्थानीय बिजली गैस आधारित है, साथ में कचरे से ऊर्जा और छत पर सौर ऊर्जा। बिजली का वितरण निजी–सार्वजनिक संयुक्त उपक्रम कंपनियाँ और नई दिल्ली क्षेत्र में एनडीएमसी करती है। एयर-कंडीशनिंग बढ़ने के साथ गर्मियों की अधिकतम माँग बार-बार नए रिकॉर्ड बनाती रही है।",
        "दिल्ली आपल्या वापराच्या विजेपैकी थोडाच भाग स्वतः निर्माण करते आणि बहुतांश वीज दीर्घकालीन करार व बाजारामार्फत बाहेरील वीजकेंद्रांकडून विकत घेते. प्रदूषण कमी करण्यासाठी शहरातील बदरपूरसारखी कोळशावरील वीजकेंद्रे बंद करण्यात आली; उरलेली स्थानिक वीजनिर्मिती वायू-आधारित आहे, सोबत कचऱ्यापासून ऊर्जा आणि छतावरील सौरऊर्जा. वीजवितरण खासगी–सार्वजनिक संयुक्त कंपन्या आणि नवी दिल्ली परिसरात एनडीएमसी करते. वातानुकूलन वाढत असल्याने उन्हाळ्यातील कमाल मागणी वारंवार नवे विक्रम करत आली आहे."),
        conf="Editorial"),
    gaps("g", [
        (L("Peak demand (latest record)", "अधिकतम माँग (नवीनतम रिकॉर्ड)", "कमाल मागणी (नवीनतम विक्रम)"), "cea", "Delhi SLDC / CEA."),
        (L("Rooftop solar capacity", "छत सौर क्षमता", "छतावरील सौर क्षमता"), "mnre", "MNRE state-wise RE capacity."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Delhi and its NCR neighbours form one of India's largest start-up and technology clusters, with consumer internet, fintech, logistics and software companies spread between Delhi, Gurugram and Noida. Many government services are delivered online through the e-District portal, and the city hosts the headquarters of national digital agencies.",
        "दिल्ली और उसके एनसीआर पड़ोसी भारत के सबसे बड़े स्टार्टअप और प्रौद्योगिकी क्लस्टरों में से एक बनाते हैं; उपभोक्ता इंटरनेट, फ़िनटेक, लॉजिस्टिक्स और सॉफ़्टवेयर कंपनियाँ दिल्ली, गुरुग्राम और नोएडा में फैली हैं। कई सरकारी सेवाएँ ई-डिस्ट्रिक्ट पोर्टल के ज़रिए ऑनलाइन मिलती हैं, और शहर में राष्ट्रीय डिजिटल एजेंसियों के मुख्यालय हैं।",
        "दिल्ली आणि तिचे एनसीआरमधील शेजारी मिळून भारतातील सर्वांत मोठ्या स्टार्टअप व तंत्रज्ञान समूहांपैकी एक बनवतात; ग्राहक इंटरनेट, फिनटेक, लॉजिस्टिक्स आणि सॉफ्टवेअर कंपन्या दिल्ली, गुरुग्राम व नोएडामध्ये पसरलेल्या आहेत. अनेक सरकारी सेवा ई-डिस्ट्रिक्ट पोर्टलवरून ऑनलाइन मिळतात, आणि राष्ट्रीय डिजिटल संस्थांची मुख्यालये शहरात आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI Indian Telecom Services Performance Indicators (Delhi circle)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("DL", NAME)
module(R, "education", [
    prose("p1", L(
        "Delhi is one of India's leading education centres. The 2021-22 AISHE survey counted 30 universities and 188 colleges, and a higher-education gross enrolment ratio of 49.0%, well above the national 28.4% — partly because students from across India come to study here. The University of Delhi, Jawaharlal Nehru University, Jamia Millia Islamia, IIT Delhi and AIIMS New Delhi are among the country's best-known institutions.",
        "दिल्ली भारत के प्रमुख शिक्षा केंद्रों में है। 2021-22 के एआईएसएचई सर्वेक्षण में 30 विश्वविद्यालय और 188 कॉलेज गिने गए, और उच्च शिक्षा में सकल नामांकन अनुपात 49.0% था, जो राष्ट्रीय 28.4% से काफ़ी अधिक है — आंशिक रूप से इसलिए कि पूरे भारत से छात्र यहाँ पढ़ने आते हैं। दिल्ली विश्वविद्यालय, जवाहरलाल नेहरू विश्वविद्यालय, जामिया मिल्लिया इस्लामिया, आईआईटी दिल्ली और एम्स नई दिल्ली देश के सबसे प्रसिद्ध संस्थानों में हैं।",
        "दिल्ली हे भारतातील आघाडीच्या शैक्षणिक केंद्रांपैकी एक आहे. 2021-22 च्या एआयएसएचई सर्वेक्षणात 30 विद्यापीठे आणि 188 महाविद्यालये नोंदली गेली, आणि उच्चशिक्षणातील एकूण नोंदणी गुणोत्तर 49.0% होते — राष्ट्रीय 28.4% पेक्षा बरेच जास्त — याचे एक कारण म्हणजे देशभरातून विद्यार्थी येथे शिकायला येतात. दिल्ली विद्यापीठ, जवाहरलाल नेहरू विद्यापीठ, जामिया मिल्लिया इस्लामिया, आयआयटी दिल्ली आणि एम्स नवी दिल्ली या देशातील सर्वांत प्रसिद्ध संस्थांपैकी आहेत."),
        sources=["aishe"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("du", "University of Delhi", "दिल्ली विश्वविद्यालय", "दिल्ली विद्यापीठ"), it3("jnu", "Jawaharlal Nehru University", "जवाहरलाल नेहरू विश्वविद्यालय", "जवाहरलाल नेहरू विद्यापीठ"),
        it3("jmi", "Jamia Millia Islamia", "जामिया मिल्लिया इस्लामिया", "जामिया मिल्लिया इस्लामिया"), it3("iitd", "IIT Delhi", "आईआईटी दिल्ली", "आयआयटी दिल्ली"),
        it3("aiims", "AIIMS New Delhi", "एम्स नई दिल्ली", "एम्स नवी दिल्ली"), it3("iiitd", "IIIT-Delhi", "आईआईआईटी-दिल्ली", "आयआयआयटी-दिल्ली"),
        it3("nlu", "National Law University Delhi", "राष्ट्रीय विधि विश्वविद्यालय दिल्ली", "राष्ट्रीय विधी विद्यापीठ दिल्ली"), it3("spa", "School of Planning and Architecture", "योजना एवं वास्तुकला विद्यालय", "नियोजन व वास्तुकला विद्यालय"),
        it3("iari", "Indian Agricultural Research Institute (Pusa)", "भारतीय कृषि अनुसंधान संस्थान (पूसा)", "भारतीय कृषी संशोधन संस्था (पुसा)"), it3("nsd", "National School of Drama", "राष्ट्रीय नाट्य विद्यालय", "राष्ट्रीय नाट्य विद्यालय"),
    ], layout="chips", title=L("National institutions (selected)", "राष्ट्रीय संस्थान (चयनित)", "राष्ट्रीय संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Board examination pass rates", "बोर्ड परीक्षा उत्तीर्ण दर", "मंडळ परीक्षा उत्तीर्ण दर"), "dl-planning", "Economic Survey of Delhi, education chapter."),
    ]),
])

# ---------------- O. Health ----------------
srs = NF["SRS_2021_PIB_PRID2128024"]
def srsdp(v, unit, period, note=None, level="state"):
    return dp(v, unit, period, "calendar", "srs", SRS, note=note, level=level)
module(R, "health", [
    prose("p1", L(
        "Delhi has some of India's largest public and private hospitals, including AIIMS, Safdarjung and other central institutions that serve patients from across North India. In the Sample Registration System for 2021, its under-five mortality was 14 per 1,000 live births and neonatal mortality 8, against 31 and 19 nationally. NFHS-5 showed falls in child stunting, wasting and underweight compared with NFHS-4. Air pollution is the city's most widespread public-health concern, especially in winter.",
        "दिल्ली में भारत के कुछ सबसे बड़े सरकारी और निजी अस्पताल हैं, जिनमें एम्स, सफ़दरजंग और अन्य केंद्रीय संस्थान शामिल हैं, जो पूरे उत्तर भारत के मरीज़ों की सेवा करते हैं। 2021 की नमूना पंजीकरण प्रणाली में यहाँ पाँच वर्ष से कम आयु की मृत्यु दर प्रति 1,000 जीवित जन्म पर 14 और नवजात मृत्यु दर 8 थी, जबकि राष्ट्रीय स्तर पर 31 और 19। एनएफ़एचएस-5 में एनएफ़एचएस-4 की तुलना में बच्चों के ठिगनेपन, दुबलेपन और कम वज़न में कमी दिखी। वायु प्रदूषण शहर की सबसे व्यापक सार्वजनिक स्वास्थ्य चिंता है, ख़ासकर सर्दियों में।",
        "दिल्लीत भारतातील काही सर्वांत मोठी सरकारी व खासगी रुग्णालये आहेत — एम्स, सफदरजंग आणि इतर केंद्रीय संस्था — जी संपूर्ण उत्तर भारतातील रुग्णांना सेवा देतात. 2021 च्या नमुना नोंदणी पद्धतीनुसार येथे पाच वर्षांखालील मृत्युदर दर 1,000 जिवंत जन्मांमागे 14 आणि नवजात मृत्युदर 8 होता, तर राष्ट्रीय पातळीवर 31 आणि 19. एनएफएचएस-4 च्या तुलनेत एनएफएचएस-5 मध्ये मुलांमधील खुजेपणा, कृशता आणि कमी वजनाचे प्रमाण घटले. वायुप्रदूषण ही शहरातील सर्वांत व्यापक सार्वजनिक आरोग्य चिंता आहे, विशेषतः हिवाळ्यात."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("srs", [
        fact("u5mr", L("Under-five mortality rate", "पाँच वर्ष से कम आयु की मृत्यु दर", "पाच वर्षांखालील मृत्युदर"), srsdp(srs["DL"]["U5MR"], "per 1,000 live births", "2021", "SRS 2021, via PIB (10 May 2025)."), "number", "lower-is-better",
             national=srsdp(srs["IN"]["U5MR"], "per 1,000 live births", "2021", level="national")),
        fact("nmr", L("Neonatal mortality rate", "नवजात मृत्यु दर", "नवजात मृत्युदर"), srsdp(srs["DL"]["NMR"], "per 1,000 live births", "2021"), "number", "lower-is-better",
             national=srsdp(srs["IN"]["NMR"], "per 1,000 live births", "2021", level="national")),
    ], title=L("Mortality (Sample Registration System)", "मृत्यु दर (नमूना पंजीकरण प्रणाली)", "मृत्युदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("DL"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Maternal mortality ratio", "मातृ मृत्यु अनुपात", "मातामृत्यू प्रमाण"), "srs", "SRS publishes MMR for larger States only; check the special bulletin."),
        (L("Infant mortality rate and life expectancy", "शिशु मृत्यु दर और जीवन प्रत्याशा", "अर्भक मृत्युदर व आयुर्मान"), "srs", "SRS Statistical Report; abridged life tables."),
        (L("Hospitals and beds", "अस्पताल और बिस्तर", "रुग्णालये व खाटा"), "dl-planning", "Economic Survey of Delhi, health chapter."),
    ]),
])

# ---------------- P. Nature ----------------
module(R, "nature", [
    prose("p1", L(
        "For a megacity, Delhi has a surprising amount of green. Forest cover was 195.28 km² in ISFR 2023, about 13.2% of its area, much of it on the Ridge — the Northern, Central, South-Central and Southern Ridge forests that act as the city's lungs. The Asola Bhatti Wildlife Sanctuary protects the Southern Ridge on the Haryana border, and the Yamuna and Aravalli Biodiversity Parks restore native habitats. Okhla Bird Sanctuary on the Yamuna draws winter waterbirds, and the Lodhi Garden, Sunder Nursery and Mehrauli Archaeological Park mix monuments with old trees.",
        "एक महानगर के हिसाब से दिल्ली में आश्चर्यजनक रूप से काफ़ी हरियाली है। आईएसएफ़आर 2023 में वन आवरण 195.28 किमी² था, यानी क्षेत्रफल का लगभग 13.2%, जिसका बड़ा हिस्सा रिज पर है — उत्तरी, मध्य, दक्षिण-मध्य और दक्षिणी रिज के वन, जो शहर के फेफड़ों का काम करते हैं। असोला भाटी वन्यजीव अभयारण्य हरियाणा सीमा पर दक्षिणी रिज की रक्षा करता है, और यमुना व अरावली जैव विविधता पार्क देशी आवासों को पुनर्जीवित करते हैं। यमुना पर ओखला पक्षी अभयारण्य सर्दियों में जल पक्षियों को आकर्षित करता है, और लोधी गार्डन, सुंदर नर्सरी और महरौली पुरातत्व पार्क में स्मारक और पुराने पेड़ साथ-साथ हैं।",
        "महानगराच्या मानाने दिल्लीत आश्चर्यकारकरीत्या बरीच हिरवाई आहे. आयएसएफआर 2023 नुसार वनाच्छादन 195.28 किमी² होते, म्हणजे क्षेत्रफळाच्या सुमारे 13.2%, आणि त्याचा मोठा भाग रिजवर आहे — उत्तर, मध्य, दक्षिण-मध्य आणि दक्षिण रिजमधील वने, जी शहराची फुफ्फुसे आहेत. असोला भाटी वन्यजीव अभयारण्य हरियाणा सीमेवरील दक्षिण रिजचे संरक्षण करते, तर यमुना व अरवली जैवविविधता उद्याने स्थानिक अधिवासांचे पुनरुज्जीवन करतात. यमुनेवरील ओखला पक्षी अभयारण्यात हिवाळ्यात पाणपक्षी येतात, आणि लोधी गार्डन, सुंदर नर्सरी व मेहरौली पुरातत्त्व उद्यानात स्मारके आणि जुने वृक्ष एकत्र आहेत."),
        sources=["fsi"], conf="Official"),
    facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(195.28, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(195.36, "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), dl["forestCoverPct"], "percent", "higher-is-better", national=ind["forestCoverPct"]),
    ]),
    lst("green", [
        it3("asola", "Asola Bhatti Wildlife Sanctuary", "असोला भाटी वन्यजीव अभयारण्य", "असोला भाटी वन्यजीव अभयारण्य", m=("Southern Ridge", "दक्षिणी रिज", "दक्षिण रिज")),
        it3("okhla", "Okhla Bird Sanctuary", "ओखला पक्षी अभयारण्य", "ओखला पक्षी अभयारण्य", m=("Yamuna, winter birds", "यमुना, शीतकालीन पक्षी", "यमुना, हिवाळी पक्षी")),
        it3("ybp", "Yamuna Biodiversity Park", "यमुना जैव विविधता पार्क", "यमुना जैवविविधता उद्यान", m=("Floodplain restoration", "बाढ़ क्षेत्र पुनर्स्थापन", "पूरमैदान पुनरुज्जीवन")),
        it3("abp", "Aravalli Biodiversity Park", "अरावली जैव विविधता पार्क", "अरवली जैवविविधता उद्यान", m=("Ridge restoration", "रिज पुनर्स्थापन", "रिज पुनरुज्जीवन")),
        it3("ridge", "Central Ridge Reserve Forest", "मध्य रिज आरक्षित वन", "मध्य रिज राखीव वन", m=("Near the President's Estate", "राष्ट्रपति भवन के पास", "राष्ट्रपती भवनाजवळ")),
        it3("sunder", "Sunder Nursery", "सुंदर नर्सरी", "सुंदर नर्सरी", m=("Heritage park beside Humayun's Tomb", "हुमायूँ के मक़बरे के पास धरोहर उद्यान", "हुमायूनच्या कबरीजवळ वारसा उद्यान")),
    ], title=L("Green spaces and protected areas", "हरित क्षेत्र और संरक्षित क्षेत्र", "हरित क्षेत्रे व संरक्षित क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("Tree cover", "वृक्ष आवरण", "वृक्षाच्छादन"), "fsi", "ISFR 2023 Delhi chapter."),
        (L("Annual average PM2.5", "वार्षिक औसत पीएम2.5", "वार्षिक सरासरी पीएम2.5"), "moefcc", "CPCB / NCAP city data."),
    ]),
])

# ---------------- Q. Water ----------------
module(R, "water", [
    prose("p1", L(
        "Delhi depends heavily on water from outside its borders: the Yamuna, canals from Haryana, and the Upper Ganga Canal system through Uttar Pradesh, under inter-State agreements. Groundwater supplies much of the rest and has been heavily drawn down in many areas. Within the city, the Yamuna carries a large load of untreated sewage, and its cleaning has been a long-running programme. Delhi Jal Board supplies water and manages sewage. In July 2023 the Yamuna rose to a record level and flooded low-lying areas.",
        "दिल्ली अपनी सीमाओं के बाहर से आने वाले पानी पर बहुत निर्भर है: अंतर-राज्यीय समझौतों के तहत यमुना, हरियाणा की नहरें और उत्तर प्रदेश से होकर आने वाली ऊपरी गंगा नहर प्रणाली। बाक़ी का बड़ा हिस्सा भूजल से आता है, जिसका कई इलाक़ों में भारी दोहन हुआ है। शहर के भीतर यमुना में बड़ी मात्रा में बिना साफ़ किया सीवेज बहता है, और इसकी सफ़ाई लंबे समय से चल रहा कार्यक्रम है। दिल्ली जल बोर्ड पानी की आपूर्ति और सीवेज का प्रबंधन करता है। जुलाई 2023 में यमुना रिकॉर्ड स्तर तक चढ़ी और निचले इलाक़ों में बाढ़ आई।",
        "दिल्ली आपल्या सीमांबाहेरून येणाऱ्या पाण्यावर मोठ्या प्रमाणात अवलंबून आहे: आंतरराज्य करारांनुसार यमुना, हरियाणातील कालवे आणि उत्तर प्रदेशातून येणारी अप्पर गंगा कालवा प्रणाली. उरलेल्यापैकी मोठा भाग भूजलातून येतो आणि अनेक भागांत त्याचा प्रचंड उपसा झाला आहे. शहरात यमुनेतून मोठ्या प्रमाणात प्रक्रिया न केलेले सांडपाणी वाहते, आणि तिची स्वच्छता हा दीर्घकाळ चाललेला कार्यक्रम आहे. दिल्ली जल बोर्ड पाणीपुरवठा व सांडपाणी व्यवस्थापन करते. जुलै 2023 मध्ये यमुनेने विक्रमी पातळी गाठली आणि सखल भागांत पूर आला."),
        conf="Editorial"),
    gaps("g", [
        (L("Water demand and supply (MGD)", "जल माँग और आपूर्ति (एमजीडी)", "पाण्याची मागणी व पुरवठा (एमजीडी)"), "dl-planning", "Economic Survey of Delhi, water chapter."),
        (L("Groundwater stage of extraction", "भूजल दोहन का स्तर", "भूजल उपशाचा टप्पा"), "dl-gov", "CGWB assessment."),
        (L("Sewage treatment capacity and utilisation", "सीवेज उपचार क्षमता और उपयोग", "सांडपाणी प्रक्रिया क्षमता व वापर"), "dl-gov", "Delhi Jal Board."),
    ]),
])

# ---------------- R. Safety ----------------
module(R, "safety", [
    prose("p1", L(
        "Delhi lies in a seismically active zone and has dense, old construction in places, so earthquake preparedness is a priority. Other hazards include heatwaves, Yamuna floods, fires in crowded markets and, above all, winter air pollution. The Delhi Disaster Management Authority coordinates preparedness, and the Commission for Air Quality Management enforces the graded response plan for pollution episodes.\n\nVisitors should check AQI and heat advisories, use licensed taxis or app cabs at night, and keep valuables close in crowded markets and on the metro.",
        "दिल्ली भूकंपीय रूप से सक्रिय क्षेत्र में है और कई जगह घनी, पुरानी इमारतें हैं, इसलिए भूकंप की तैयारी प्राथमिकता है। अन्य ख़तरों में लू, यमुना की बाढ़, भीड़भाड़ वाले बाज़ारों में आग और सबसे बढ़कर सर्दियों का वायु प्रदूषण शामिल हैं। दिल्ली आपदा प्रबंधन प्राधिकरण तैयारी का समन्वय करता है, और वायु गुणवत्ता प्रबंधन आयोग प्रदूषण की घटनाओं के लिए ग्रेडेड रिस्पॉन्स प्लान लागू करता है।\n\nपर्यटकों को एक्यूआई और लू संबंधी सलाह देखनी चाहिए, रात में लाइसेंसशुदा टैक्सी या ऐप कैब लेनी चाहिए, और भीड़ वाले बाज़ारों व मेट्रो में क़ीमती सामान सँभालकर रखना चाहिए।",
        "दिल्ली भूकंपप्रवण क्षेत्रात आहे आणि काही ठिकाणी दाट, जुनी बांधकामे आहेत, त्यामुळे भूकंपाची पूर्वतयारी प्राधान्याची आहे. इतर धोक्यांमध्ये उष्णतेच्या लाटा, यमुनेचे पूर, गर्दीच्या बाजारपेठांतील आगी आणि सर्वांत मोठा म्हणजे हिवाळ्यातील वायुप्रदूषण यांचा समावेश आहे. दिल्ली आपत्ती व्यवस्थापन प्राधिकरण पूर्वतयारीचे समन्वयन करते, आणि हवा गुणवत्ता व्यवस्थापन आयोग प्रदूषणाच्या काळात श्रेणीबद्ध प्रतिसाद आराखडा राबवतो.\n\nपर्यटकांनी एक्यूआय व उष्णतेचे इशारे तपासावेत, रात्री परवानाधारक टॅक्सी किंवा ॲप कॅब वापरावी, आणि गर्दीच्या बाजारांत व मेट्रोत मौल्यवान वस्तू सांभाळाव्यात."),
        conf="Editorial"),
    emergency_table(("Delhi", "दिल्ली", "दिल्ली")),
    lst("links", [
        it3("ddma", "Delhi Disaster Management Authority", "दिल्ली आपदा प्रबंधन प्राधिकरण", "दिल्ली आपत्ती व्यवस्थापन प्राधिकरण", url="https://ddma.delhi.gov.in", src="dl-gov"),
        it3("police", "Delhi Police", "दिल्ली पुलिस", "दिल्ली पोलीस", url="https://delhipolice.gov.in", src="dl-gov"),
        it3("imd", "IMD weather warnings", "आईएमडी मौसम चेतावनियाँ", "आयएमडी हवामान इशारे", url="https://mausam.imd.gov.in", src="imd"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Seismic microzonation", "भूकंपीय सूक्ष्म-क्षेत्रीकरण", "भूकंपीय सूक्ष्म-क्षेत्रीकरण"), "ndma", "NCS / DDMA microzonation report."),
        (L("Yamuna danger level and flood records", "यमुना का ख़तरे का निशान और बाढ़ रिकॉर्ड", "यमुनेची धोका पातळी व पुराच्या नोंदी"), "dl-gov", "Irrigation & Flood Control Department."),
    ]),
])

# ---------------- S. GI ----------------
module(R, "gi", [
    prose("p1", L(
        "Delhi has no Geographical Indication of its own in the GI Registry's list as on 31 December 2025. It shares one: Basmati rice, registered for the Indo-Gangetic plain across Punjab, Haryana, Himachal Pradesh, Delhi, Uttarakhand, western Uttar Pradesh and Jammu & Kashmir. The city's crafts — zardozi embroidery, attar, Old Delhi's kite-making and miniature painting — are not yet registered GIs.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में दिल्ली का अपना कोई भौगोलिक संकेतक नहीं है। यह एक जीआई साझा करती है: बासमती चावल, जो पंजाब, हरियाणा, हिमाचल प्रदेश, दिल्ली, उत्तराखंड, पश्चिमी उत्तर प्रदेश और जम्मू-कश्मीर के सिंधु-गंगा मैदान के लिए पंजीकृत है। शहर के शिल्प — ज़रदोज़ी कढ़ाई, इत्र, पुरानी दिल्ली की पतंगसाज़ी और लघु चित्रकला — अभी पंजीकृत जीआई नहीं हैं।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत दिल्लीचे स्वतःचे कोणतेही भौगोलिक मानांकन नाही. ती एक जीआय सामायिक करते: बासमती तांदूळ, जो पंजाब, हरियाणा, हिमाचल प्रदेश, दिल्ली, उत्तराखंड, पश्चिम उत्तर प्रदेश आणि जम्मू-काश्मीरच्या सिंधू-गंगा मैदानासाठी नोंदणीकृत आहे. शहरातील हस्तकला — जरदोजी भरतकाम, अत्तर, जुन्या दिल्लीतील पतंगनिर्मिती आणि लघुचित्रकला — अद्याप नोंदणीकृत जीआय नाहीत."),
        sources=["gi-registry"], conf="Official"),
    {"type": "gi", "id": "gi"},
    gaps("g", [
        (L("One District One Product (ODOP) items", "एक ज़िला एक उत्पाद (ओडीओपी)", "एक जिल्हा एक उत्पादन (ओडीओपी)"), "dpiit", "DPIIT ODOP list for Delhi."),
    ]),
])

# ---------------- T. Tourism ----------------
module(R, "tourism", [
    prose("p1", L(
        "Delhi is the main gateway for international visitors to North India and the start of the classic Golden Triangle with Agra and Jaipur. Its sights span three World Heritage Sites, Mughal and Sultanate monuments in almost every neighbourhood, major museums, Old Delhi's bazaars and the ceremonial axis of Kartavya Path from Rashtrapati Bhavan to India Gate.",
        "दिल्ली उत्तर भारत आने वाले अंतरराष्ट्रीय पर्यटकों का मुख्य प्रवेश द्वार है और आगरा व जयपुर के साथ प्रसिद्ध स्वर्णिम त्रिभुज की शुरुआत भी। इसके दर्शनीय स्थलों में तीन विश्व धरोहर स्थल, लगभग हर मोहल्ले में मुग़ल और सल्तनत कालीन स्मारक, बड़े संग्रहालय, पुरानी दिल्ली के बाज़ार और राष्ट्रपति भवन से इंडिया गेट तक कर्तव्य पथ की औपचारिक धुरी शामिल हैं।",
        "उत्तर भारतात येणाऱ्या आंतरराष्ट्रीय पर्यटकांचे दिल्ली हे मुख्य प्रवेशद्वार आहे आणि आग्रा व जयपूरसह प्रसिद्ध सुवर्ण त्रिकोणाची सुरुवातही. येथील प्रेक्षणीय स्थळांत तीन जागतिक वारसा स्थळे, जवळपास प्रत्येक वस्तीत मुघल व सल्तनतकालीन स्मारके, मोठी संग्रहालये, जुन्या दिल्लीतील बाजारपेठा आणि राष्ट्रपती भवनापासून इंडिया गेटपर्यंतचा कर्तव्य पथ हा औपचारिक अक्ष यांचा समावेश आहे."),
        conf="Editorial"),
    lst("places", [
        it3("redfort", "Red Fort, Jama Masjid and Chandni Chowk", "लाल क़िला, जामा मस्जिद और चाँदनी चौक", "लाल किल्ला, जामा मशीद आणि चांदनी चौक", m=("Mughal Delhi", "मुग़ल दिल्ली", "मुघल दिल्ली")),
        it3("qutb", "Qutb Minar and Mehrauli", "क़ुतुब मीनार और महरौली", "कुतुबमिनार आणि मेहरौली", m=("Sultanate Delhi", "सल्तनत कालीन दिल्ली", "सल्तनतकालीन दिल्ली")),
        it3("humayun", "Humayun's Tomb, Sunder Nursery and Nizamuddin", "हुमायूँ का मक़बरा, सुंदर नर्सरी और निज़ामुद्दीन", "हुमायूनची कबर, सुंदर नर्सरी आणि निजामुद्दीन", m=("Heritage, Sufi", "धरोहर, सूफ़ी", "वारसा, सूफी")),
        it3("kartavya", "Kartavya Path, India Gate and the National War Memorial", "कर्तव्य पथ, इंडिया गेट और राष्ट्रीय युद्ध स्मारक", "कर्तव्य पथ, इंडिया गेट आणि राष्ट्रीय युद्ध स्मारक", m=("Capital complex", "राजधानी परिसर", "राजधानी परिसर")),
        it3("museums", "National Museum and National Gallery of Modern Art", "राष्ट्रीय संग्रहालय और राष्ट्रीय आधुनिक कला संग्रहालय", "राष्ट्रीय संग्रहालय आणि राष्ट्रीय आधुनिक कला संग्रहालय", m=("Museums", "संग्रहालय", "संग्रहालये")),
        it3("lotus", "Lotus Temple, Akshardham and Bangla Sahib", "लोटस टेंपल, अक्षरधाम और बंगला साहिब", "लोटस टेंपल, अक्षरधाम आणि बंगला साहिब", m=("Places of worship", "पूजा स्थल", "प्रार्थनास्थळे")),
        it3("lodhi", "Lodhi Garden and Hauz Khas", "लोधी गार्डन और हौज़ ख़ास", "लोधी गार्डन आणि हौज खास", m=("Gardens, ruins", "उद्यान, खंडहर", "उद्याने, अवशेष")),
    ], title=L("Top places by category", "श्रेणी के अनुसार प्रमुख स्थल", "प्रकारानुसार प्रमुख ठिकाणे"), conf="Editorial"),
    lst("itin", [
        it3("d1", "1 day", "1 दिन", "1 दिवस", d=("Old Delhi by cycle-rickshaw, the Red Fort and Jama Masjid; evening at India Gate.", "साइकिल-रिक्शा से पुरानी दिल्ली, लाल क़िला और जामा मस्जिद; शाम इंडिया गेट पर।", "सायकल-रिक्षाने जुनी दिल्ली, लाल किल्ला आणि जामा मशीद; संध्याकाळ इंडिया गेटला.")),
        it3("d2", "2 days", "2 दिन", "2 दिवस", d=("Add Humayun's Tomb, Sunder Nursery, Nizamuddin (Thursday qawwali) and Qutb Minar.", "हुमायूँ का मक़बरा, सुंदर नर्सरी, निज़ामुद्दीन (गुरुवार की क़व्वाली) और क़ुतुब मीनार जोड़ें।", "हुमायूनची कबर, सुंदर नर्सरी, निजामुद्दीन (गुरुवारची कव्वाली) आणि कुतुबमिनार जोडा.")),
        it3("d3", "3 days", "3 दिन", "3 दिवस", d=("Museums, Mehrauli Archaeological Park and Hauz Khas; a day trip to Agra by train.", "संग्रहालय, महरौली पुरातत्व पार्क और हौज़ ख़ास; ट्रेन से आगरा की एक दिन की यात्रा।", "संग्रहालये, मेहरौली पुरातत्त्व उद्यान आणि हौज खास; रेल्वेने आग्र्याची एकदिवसीय सहल.")),
    ], layout="bullets", title=L("Sample itineraries", "नमूना यात्रा कार्यक्रम", "नमुना प्रवास आराखडे"), conf="Editorial"),
    lst("links", [it3("dt", "Delhi Tourism (official)", "दिल्ली पर्यटन (आधिकारिक)", "दिल्ली पर्यटन (अधिकृत)", url="https://delhitourism.gov.in", src="dl-gov")],
        title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Domestic and foreign tourist visits", "घरेलू और विदेशी पर्यटक यात्राएँ", "देशी व परदेशी पर्यटक भेटी"), "tourism", "India Tourism Statistics (latest year)."),
        (L("Visitors to ASI-ticketed monuments", "एएसआई टिकट वाले स्मारकों पर आगंतुक", "एएसआय तिकीट असलेल्या स्मारकांना भेटी"), "asi", "ASI annual figures."),
    ]),
])

# ---------------- U. Cities (areas) ----------------
module(R, "cities", [
    prose("p1", L(
        "Delhi is a single city-territory rather than a State of many cities. Its historic and planned parts each have a distinct character: Old Delhi (Shahjahanabad) inside the Mughal walls; Lutyens' New Delhi, the capital complex of wide avenues and bungalows; the post-Partition colonies of the west and south; DDA's planned sub-cities such as Dwarka and Rohini; and the dense, fast-growing settlements of the east and north-east across the Yamuna.",
        "दिल्ली कई शहरों वाला राज्य नहीं, बल्कि एक ही शहर-क्षेत्र है। इसके ऐतिहासिक और नियोजित हिस्सों की अपनी अलग पहचान है: मुग़ल दीवारों के भीतर पुरानी दिल्ली (शाहजहानाबाद); चौड़ी सड़कों और बंगलों वाला लुटियंस की नई दिल्ली का राजधानी परिसर; पश्चिम और दक्षिण की विभाजन के बाद बसी कॉलोनियाँ; द्वारका और रोहिणी जैसे डीडीए के नियोजित उप-नगर; और यमुना पार पूर्वी व उत्तर-पूर्वी दिल्ली की घनी, तेज़ी से बढ़ती बस्तियाँ।",
        "दिल्ली हे अनेक शहरांचे राज्य नसून एकच शहर-प्रदेश आहे. तिच्या ऐतिहासिक आणि नियोजित भागांची स्वतंत्र ओळख आहे: मुघल तटबंदीतील जुनी दिल्ली (शाहजहानाबाद); रुंद रस्ते व बंगल्यांचा लुटियन्सच्या नव्या दिल्लीचा राजधानी परिसर; पश्चिम व दक्षिणेकडील फाळणीनंतर वसलेल्या वसाहती; द्वारका आणि रोहिणीसारखी डीडीएची नियोजित उपनगरे; आणि यमुनेपलीकडील पूर्व व ईशान्य दिल्लीतील दाट, झपाट्याने वाढणाऱ्या वस्त्या."),
        conf="Editorial"),
    lst("areas", [
        it3("old", "Old Delhi (Shahjahanabad)", "पुरानी दिल्ली (शाहजहानाबाद)", "जुनी दिल्ली (शाहजहानाबाद)", d=("Walled Mughal city: Chandni Chowk, Red Fort, Jama Masjid, wholesale markets.", "मुग़ल परकोटा शहर: चाँदनी चौक, लाल क़िला, जामा मस्जिद, थोक बाज़ार।", "मुघल तटबंदीचे शहर: चांदनी चौक, लाल किल्ला, जामा मशीद, घाऊक बाजारपेठा.")),
        it3("new", "New Delhi (NDMC area)", "नई दिल्ली (एनडीएमसी क्षेत्र)", "नवी दिल्ली (एनडीएमसी क्षेत्र)", d=("Seat of the Union Government; Rashtrapati Bhavan, Parliament, Connaught Place.", "केंद्र सरकार का मुख्यालय; राष्ट्रपति भवन, संसद, कनॉट प्लेस।", "केंद्र सरकारचे मुख्यालय; राष्ट्रपती भवन, संसद, कॅनॉट प्लेस.")),
        it3("south", "South Delhi", "दक्षिणी दिल्ली", "दक्षिण दिल्ली", d=("Mehrauli, Hauz Khas, Saket; markets, malls and Sultanate ruins.", "महरौली, हौज़ ख़ास, साकेत; बाज़ार, मॉल और सल्तनत कालीन खंडहर।", "मेहरौली, हौज खास, साकेत; बाजारपेठा, मॉल आणि सल्तनतकालीन अवशेष.")),
        it3("dwarka", "Dwarka and Rohini", "द्वारका और रोहिणी", "द्वारका आणि रोहिणी", d=("Large planned residential sub-cities in the south-west and north-west.", "दक्षिण-पश्चिम और उत्तर-पश्चिम में बड़े नियोजित आवासीय उप-नगर।", "नैर्ऋत्य व वायव्येकडील मोठी नियोजित निवासी उपनगरे.")),
        it3("east", "East and North-East Delhi", "पूर्वी और उत्तर-पूर्वी दिल्ली", "पूर्व व ईशान्य दिल्ली", d=("Dense neighbourhoods across the Yamuna, linked by metro to Noida and Ghaziabad.", "यमुना पार की घनी बस्तियाँ, मेट्रो से नोएडा और ग़ाज़ियाबाद से जुड़ी।", "यमुनेपलीकडील दाट वस्त्या, मेट्रोने नोएडा व गाझियाबादशी जोडलेल्या.")),
    ], title=L("Parts of the city", "शहर के हिस्से", "शहराचे भाग"), conf="Editorial"),
    gaps("g", [
        (L("Current list of revenue districts and populations", "राजस्व ज़िलों की वर्तमान सूची और जनसंख्या", "महसूल जिल्ह्यांची सध्याची यादी व लोकसंख्या"), "dl-gov", "Revenue Department notification; Census 2011 district tables."),
        (L("Unauthorised colonies and JJ clusters (count)", "अनधिकृत कॉलोनियाँ और झुग्गी बस्तियाँ (संख्या)", "अनधिकृत वसाहती व झोपडपट्ट्या (संख्या)"), "dl-planning", "Economic Survey of Delhi, housing chapter."),
    ]),
])

# ---------------- V. Sports ----------------
module(R, "sports", [
    prose("p1", L(
        "Delhi hosted the first Asian Games in 1951, the 1982 Asian Games and the 2010 Commonwealth Games, which left it with major stadiums. Cricket is the most followed sport, and the city has produced many international players. Wrestling has deep roots in Delhi's akharas, and the Chhatrasal Stadium has trained Olympic medallists. Hockey, football and athletics are played at the Major Dhyan Chand National Stadium and Jawaharlal Nehru Stadium.",
        "दिल्ली ने 1951 में पहले एशियाई खेल, 1982 के एशियाई खेल और 2010 के राष्ट्रमंडल खेलों की मेज़बानी की, जिनसे इसे बड़े स्टेडियम मिले। क्रिकेट सबसे लोकप्रिय खेल है, और शहर ने कई अंतरराष्ट्रीय खिलाड़ी दिए हैं। कुश्ती की दिल्ली के अखाड़ों में गहरी जड़ें हैं, और छत्रसाल स्टेडियम ने ओलंपिक पदक विजेताओं को तैयार किया है। हॉकी, फ़ुटबॉल और एथलेटिक्स मेजर ध्यानचंद राष्ट्रीय स्टेडियम और जवाहरलाल नेहरू स्टेडियम में खेले जाते हैं।",
        "दिल्लीने 1951 मधील पहिल्या आशियाई क्रीडा स्पर्धा, 1982 च्या आशियाई स्पर्धा आणि 2010 च्या राष्ट्रकुल स्पर्धांचे यजमानपद भूषवले, त्यामुळे शहराला मोठी स्टेडियम मिळाली. क्रिकेट हा सर्वाधिक लोकप्रिय खेळ असून शहराने अनेक आंतरराष्ट्रीय खेळाडू दिले आहेत. कुस्तीची दिल्लीतील आखाड्यांत खोल मुळे आहेत, आणि छत्रसाल स्टेडियमने ऑलिम्पिक पदकविजेते घडवले आहेत. हॉकी, फुटबॉल आणि अॅथलेटिक्स मेजर ध्यानचंद राष्ट्रीय स्टेडियम व जवाहरलाल नेहरू स्टेडियममध्ये खेळले जातात."),
        conf="Editorial"),
    lst("venues", [
        it3("jaitley", "Arun Jaitley Stadium (Feroz Shah Kotla)", "अरुण जेटली स्टेडियम (फ़िरोज़शाह कोटला)", "अरुण जेटली स्टेडियम (फिरोजशाह कोटला)"),
        it3("jln", "Jawaharlal Nehru Stadium", "जवाहरलाल नेहरू स्टेडियम", "जवाहरलाल नेहरू स्टेडियम"),
        it3("dhyanchand", "Major Dhyan Chand National Stadium", "मेजर ध्यानचंद राष्ट्रीय स्टेडियम", "मेजर ध्यानचंद राष्ट्रीय स्टेडियम"),
        it3("igi", "Indira Gandhi Arena", "इंदिरा गांधी एरीना", "इंदिरा गांधी एरिना"),
        it3("chhatrasal", "Chhatrasal Stadium", "छत्रसाल स्टेडियम", "छत्रसाल स्टेडियम"),
    ], layout="chips", title=L("Major venues", "प्रमुख मैदान", "प्रमुख मैदाने"), conf="Editorial"),
])

# ---------------- W. Personalities ----------------
def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
module(R, "personalities", [
    lst("people", [
        person("nizamuddin", ("Nizamuddin Auliya", "निज़ामुद्दीन औलिया", "निजामुद्दीन औलिया"), ("14th-century Chishti Sufi saint whose dargah is one of Delhi's great shrines.", "14वीं सदी के चिश्ती सूफ़ी संत, जिनकी दरगाह दिल्ली के प्रमुख तीर्थों में है।", "चौदाव्या शतकातील चिश्ती सूफी संत; त्यांचा दर्गा दिल्लीतील प्रमुख तीर्थस्थळांपैकी एक."), ("Sufism", "सूफ़ीवाद", "सूफी परंपरा")),
        person("khusrau", ("Amir Khusrau", "अमीर ख़ुसरो", "अमीर खुसरो"), ("Poet and musician of the Delhi Sultanate; disciple of Nizamuddin Auliya.", "दिल्ली सल्तनत के कवि और संगीतकार; निज़ामुद्दीन औलिया के शिष्य।", "दिल्ली सल्तनतीतील कवी व संगीतकार; निजामुद्दीन औलियांचे शिष्य."), ("Poetry, music", "काव्य, संगीत", "काव्य, संगीत")),
        person("ghalib", ("Mirza Ghalib", "मिर्ज़ा ग़ालिब", "मिर्झा गालिब"), ("Urdu and Persian poet who lived most of his life in Delhi's Ballimaran.", "उर्दू और फ़ारसी के कवि, जिन्होंने जीवन का अधिकांश समय दिल्ली के बल्लीमारान में बिताया।", "उर्दू व फारसी कवी; आयुष्याचा बहुतांश काळ दिल्लीच्या बल्लीमारानमध्ये."), ("Poetry", "काव्य", "काव्य")),
        person("zafar", ("Bahadur Shah Zafar", "बहादुर शाह ज़फ़र", "बहादूरशाह जफर"), ("Last Mughal emperor and poet; exiled to Rangoon after 1857.", "अंतिम मुग़ल बादशाह और कवि; 1857 के बाद रंगून निर्वासित।", "शेवटचा मुघल बादशहा व कवी; 1857 नंतर रंगूनला हद्दपार."), ("History", "इतिहास", "इतिहास")),
        person("syed", ("Syed Ahmad Khan", "सैयद अहमद ख़ान", "सय्यद अहमद खान"), ("Born in Delhi; educationist and founder of what became Aligarh Muslim University.", "दिल्ली में जन्मे; शिक्षाविद् और बाद में अलीगढ़ मुस्लिम विश्वविद्यालय बनी संस्था के संस्थापक।", "दिल्लीत जन्म; शिक्षणतज्ज्ञ आणि पुढे अलिगढ मुस्लिम विद्यापीठ बनलेल्या संस्थेचे संस्थापक."), ("Education", "शिक्षा", "शिक्षण")),
        person("ajmal", ("Hakim Ajmal Khan", "हकीम अजमल ख़ान", "हकीम अजमल खान"), ("Physician of Unani medicine and a founder of Jamia Millia Islamia.", "यूनानी चिकित्सक और जामिया मिल्लिया इस्लामिया के संस्थापकों में।", "युनानी वैद्य आणि जामिया मिल्लिया इस्लामियाच्या संस्थापकांपैकी एक."), ("Medicine, education", "चिकित्सा, शिक्षा", "वैद्यक, शिक्षण")),
        person("kohli", ("Virat Kohli", "विराट कोहली", "विराट कोहली"), ("Delhi-born cricketer and former India captain.", "दिल्ली में जन्मे क्रिकेटर और भारत के पूर्व कप्तान।", "दिल्लीत जन्मलेले क्रिकेटपटू आणि भारताचे माजी कर्णधार."), ("Sport", "खेल", "क्रीडा")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

# ---------------- X. Diaspora ----------------
module(R, "diaspora", [
    prose("p1", L(
        "Delhi is a city of migrants. Refugees from West Punjab and Sindh rebuilt much of the city after 1947, and since then people from Uttar Pradesh, Bihar, Uttarakhand, Haryana, Rajasthan, West Bengal, the North-East and South India have arrived for work and study. Neighbourhoods often reflect these origins — Bengali Chittaranjan Park, Tibetan Majnu-ka-Tilla, Malayali and Tamil enclaves — and Delhi's diaspora abroad is equally varied.",
        "दिल्ली प्रवासियों का शहर है। 1947 के बाद पश्चिमी पंजाब और सिंध के शरणार्थियों ने शहर का बड़ा हिस्सा फिर से बसाया, और तब से उत्तर प्रदेश, बिहार, उत्तराखंड, हरियाणा, राजस्थान, पश्चिम बंगाल, पूर्वोत्तर और दक्षिण भारत से लोग काम और पढ़ाई के लिए आते रहे हैं। मोहल्ले अक्सर इन जड़ों को दर्शाते हैं — बंगाली चितरंजन पार्क, तिब्बती मजनूँ का टीला, मलयाली और तमिल बस्तियाँ — और विदेश में बसे दिल्लीवासी भी उतने ही विविध हैं।",
        "दिल्ली हे स्थलांतरितांचे शहर आहे. 1947 नंतर पश्चिम पंजाब आणि सिंधमधील निर्वासितांनी शहराचा मोठा भाग पुन्हा वसवला, आणि तेव्हापासून उत्तर प्रदेश, बिहार, उत्तराखंड, हरियाणा, राजस्थान, पश्चिम बंगाल, ईशान्य भारत आणि दक्षिण भारतातून लोक कामासाठी व शिक्षणासाठी येत राहिले आहेत. वस्त्या अनेकदा ही मुळे दाखवतात — बंगाली चित्तरंजन पार्क, तिबेटी मजनू-का-टिला, मल्याळी व तमिळ वस्त्या — आणि परदेशस्थ दिल्लीकरही तितकेच वैविध्यपूर्ण आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("In-migration by State of origin", "मूल राज्य के अनुसार आप्रवास", "मूळ राज्यानुसार स्थलांतर"), "census", "Census 2011 D-series migration tables."),
    ]),
])

# ---------------- Y. Civic ----------------
module(R, "civic", [
    lst("links", [
        it3("portal", "Government of NCT of Delhi portal", "दिल्ली सरकार पोर्टल", "दिल्ली सरकार संकेतस्थळ", url="https://delhi.gov.in", src="dl-gov"),
        it3("edistrict", "e-District Delhi — certificates and services", "ई-डिस्ट्रिक्ट दिल्ली — प्रमाणपत्र और सेवाएँ", "ई-डिस्ट्रिक्ट दिल्ली — प्रमाणपत्रे व सेवा", url="https://edistrict.delhigovt.nic.in", src="dl-gov"),
        it3("djb", "Delhi Jal Board", "दिल्ली जल बोर्ड", "दिल्ली जल बोर्ड", url="https://delhijalboard.delhi.gov.in", src="dl-gov"),
        it3("dmrc", "Delhi Metro Rail Corporation", "दिल्ली मेट्रो रेल निगम", "दिल्ली मेट्रो रेल महामंडळ", url="https://www.delhimetrorail.com", src="dmrc"),
        it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov"),
        it3("consumer", "National Consumer Helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन", "राष्ट्रीय ग्राहक हेल्पलाइन", url="https://consumerhelpline.gov.in", src="india-gov"),
    ], title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official"),
    table("std", L("STD code", "एसटीडी कोड", "एसटीडी कोड"), [col(L("Area", "क्षेत्र", "क्षेत्र")), col(L("Code", "कोड", "कोड"), "right")],
          [[L("All of Delhi", "पूरी दिल्ली", "संपूर्ण दिल्ली"), "011"]], None, None, conf="Editorial", access=None,
          note=L("Editorial; to be checked against the Department of Telecommunications numbering plan.", "संपादकीय; दूरसंचार विभाग की नंबरिंग योजना से जाँचा जाएगा।", "संपादकीय; दूरसंचार विभागाच्या क्रमांक योजनेशी पडताळले जाईल.")),
    gaps("g", [
        (L("Verified local business directory (MSMEs, co-operatives, artisan clusters)", "सत्यापित स्थानीय व्यवसाय निर्देशिका (एमएसएमई, सहकारी, कारीगर क्लस्टर)", "पडताळलेली स्थानिक उद्योग सूची (एमएसएमई, सहकारी संस्था, कारागीर समूह)"), "india-gov", "Udyam Registration and co-operative registrar."),
    ]),
])

# ---------------- Z. Trivia ----------------
def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)
module(R, "trivia", [
    lst("facts", [
        triv("density", ("At 11,320 people per km² in 2011, Delhi was the most densely populated State or UT.", "2011 में 11,320 व्यक्ति प्रति किमी² के साथ दिल्ली सबसे घनी आबादी वाला राज्य या केंद्र शासित प्रदेश थी।", "2011 मध्ये दर किमी² ला 11,320 लोकांसह दिल्ली हा सर्वाधिक दाट लोकवस्तीचा राज्य किंवा केंद्रशासित प्रदेश होता."), ESD, "dl-planning"),
        triv("grow", ("Its population grew from 17.44 lakh in 1951 to 167.88 lakh in 2011 — almost tenfold.", "इसकी आबादी 1951 के 17.44 लाख से 2011 में 167.88 लाख हो गई — लगभग दस गुना।", "तिची लोकसंख्या 1951 मधील 17.44 लाखांवरून 2011 मध्ये 167.88 लाख झाली — जवळपास दहापट."), ESD, "dl-planning"),
        triv("whs", ("Delhi has three UNESCO World Heritage Sites: Qutb Minar, Humayun's Tomb and the Red Fort.", "दिल्ली में तीन यूनेस्को विश्व धरोहर स्थल हैं: क़ुतुब मीनार, हुमायूँ का मक़बरा और लाल क़िला।", "दिल्लीत तीन युनेस्को जागतिक वारसा स्थळे आहेत: कुतुबमिनार, हुमायूनची कबर आणि लाल किल्ला."), UNESCO, "unesco-whc"),
        triv("rrts", ("The 82 km Delhi–Meerut Namo Bharat is India's first regional rapid transit corridor.", "82 किमी लंबा दिल्ली–मेरठ नमो भारत भारत का पहला क्षेत्रीय रैपिड ट्रांज़िट कॉरिडोर है।", "82 किमीची दिल्ली–मेरठ नमो भारत ही भारतातील पहिली प्रादेशिक जलद परिवहन मार्गिका आहे."), NOA_RRTS, "newsonair"),
        triv("asiad", ("Delhi hosted the first Asian Games, in 1951.", "दिल्ली ने 1951 में पहले एशियाई खेलों की मेज़बानी की।", "दिल्लीने 1951 मध्ये पहिल्या आशियाई क्रीडा स्पर्धांचे यजमानपद भूषवले.")),
        triv("capital", ("The decision to move the capital from Calcutta was announced at the Delhi Durbar of 1911.", "कलकत्ता से राजधानी हटाने का निर्णय 1911 के दिल्ली दरबार में घोषित हुआ।", "कलकत्त्याहून राजधानी हलवण्याचा निर्णय 1911 च्या दिल्ली दरबारात जाहीर झाला.")),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("dl mod2 ok")
