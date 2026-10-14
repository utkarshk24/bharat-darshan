"""Uttar Pradesh modules G–O: culture, economy, government, projects, transport, energy, digital, education, health."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-UP"
UPF = "https://updes.up.nic.in/updes/data/upinfigures/up%20in%20figures-%202022.pdf"
ECI = "https://results.eci.gov.in/ResultAcGenMar2022/partywiseresult-S24.htm"
mo = research("mospi_up.json")
NAME = L("Uttar Pradesh", "उत्तर प्रदेश", "उत्तर प्रदेश")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


# ---------------- G. Culture ----------------
module(R, "culture", [
    prose("p1", L(
        "Uttar Pradesh is a heartland of Hindustani culture. Kathak grew in the courts and temples of Lucknow and Varanasi, which also gave their names to great schools (gharanas) of Hindustani music — Varanasi for thumri, tabla and the shehnai of Bismillah Khan. The Ramlila, staged across towns every autumn and most famously at Ramnagar near Varanasi, is recognised by UNESCO; nautanki, birha and qawwali are popular stage and song forms. Hindi and Urdu literature owe much to the region — from the devotional poetry of Kabir, Tulsidas and Surdas to Premchand's stories of village life and the Urdu poetry of Lucknow.\n\nCraft is everywhere: Banarasi silk brocade, Lucknow chikankari, Bhadohi carpets, Moradabad brass, Firozabad glass bangles, Agra marble inlay and Kannauj perfume. The State has the largest number of registered GIs of any State in this directory.",
        "उत्तर प्रदेश हिंदुस्तानी संस्कृति का हृदय-स्थल है। कथक लखनऊ और वाराणसी के दरबारों और मंदिरों में विकसित हुआ, जिनके नाम पर हिंदुस्तानी संगीत के बड़े घराने भी हैं — ठुमरी, तबला और बिस्मिल्लाह ख़ाँ की शहनाई के लिए वाराणसी। हर शरद ऋतु में नगरों में, और सबसे प्रसिद्ध रूप में वाराणसी के पास रामनगर में, होने वाली रामलीला को यूनेस्को की मान्यता है; नौटंकी, बिरहा और क़व्वाली लोकप्रिय मंच और गीत रूप हैं। हिंदी और उर्दू साहित्य इस क्षेत्र का बहुत ऋणी है — कबीर, तुलसीदास और सूरदास की भक्ति कविता से लेकर प्रेमचंद की ग्रामीण कहानियों और लखनऊ की उर्दू शायरी तक।\n\nशिल्प हर जगह है: बनारसी रेशमी ब्रोकेड, लखनवी चिकनकारी, भदोही के क़ालीन, मुरादाबाद का पीतल, फ़िरोज़ाबाद की काँच की चूड़ियाँ, आगरा की संगमरमर पच्चीकारी और कन्नौज का इत्र। इस निर्देशिका में किसी भी राज्य से अधिक पंजीकृत जीआई इसी राज्य के हैं।",
        "उत्तर प्रदेश हे हिंदुस्तानी संस्कृतीचे हृदयस्थान आहे. कथक लखनौ आणि वाराणसीच्या दरबारांत व मंदिरांत विकसित झाले, आणि याच शहरांच्या नावाने हिंदुस्तानी संगीताची मोठी घराणी आहेत — ठुमरी, तबला आणि बिस्मिल्ला खाँ यांच्या सनईसाठी वाराणसी. दर शरद ऋतूत शहरोशहरी, आणि सर्वांत प्रसिद्ध म्हणजे वाराणसीजवळील रामनगर येथे होणाऱ्या रामलीलेला युनेस्कोची मान्यता आहे; नौटंकी, बिरहा आणि कव्वाली हे लोकप्रिय रंगमंच व गीतप्रकार आहेत. हिंदी आणि उर्दू साहित्य या प्रदेशाचे मोठे ऋणी आहे — कबीर, तुलसीदास व सूरदास यांच्या भक्तिकाव्यापासून प्रेमचंदांच्या ग्रामीण कथांपर्यंत आणि लखनौच्या उर्दू शायरीपर्यंत.\n\nकलाकुसर सर्वत्र आहे: बनारसी रेशमी जरीकाम, लखनवी चिकनकारी, भदोहीचे गालिचे, मुरादाबादचे पितळ, फिरोजाबादच्या काचेच्या बांगड्या, आग्र्याचे संगमरवरी जडावकाम आणि कनौजचे अत्तर. या सूचीत इतर कोणत्याही राज्यापेक्षा जास्त नोंदणीकृत जीआय याच राज्याचे आहेत."),
        conf="Editorial"),
    lst("festivals", [
        fest("holi", "Holi in Braj", "ब्रज की होली", "ब्रजमधील होळी", ("February–March", "फ़रवरी–मार्च", "फेब्रुवारी–मार्च"),
             ("A week of celebration in Mathura, Vrindavan, Barsana and Nandgaon, including Lathmar Holi.", "मथुरा, वृंदावन, बरसाना और नंदगाँव में सप्ताह भर का उत्सव, जिसमें लठमार होली भी शामिल है।", "मथुरा, वृंदावन, बरसाना व नंदगाव येथे आठवडाभर उत्सव, लठमार होळीसह.")),
        fest("kumbh", "Kumbh and Magh Mela, Prayagraj", "कुंभ और माघ मेला, प्रयागराज", "कुंभ व माघमेळा, प्रयागराज", ("January–February", "जनवरी–फ़रवरी", "जानेवारी–फेब्रुवारी"),
             ("Ritual bathing at the Sangam; the Magh Mela is annual and the Kumbh returns in a twelve-year cycle.", "संगम पर स्नान; माघ मेला हर साल होता है और कुंभ बारह वर्ष के चक्र में।", "संगमावर स्नान; माघमेळा दरवर्षी भरतो आणि कुंभ बारा वर्षांच्या चक्राने.")),
        fest("devdeepavali", "Dev Deepavali, Varanasi", "देव दीपावली, वाराणसी", "देव दीपावली, वाराणसी", ("November (Kartik Purnima)", "नवंबर (कार्तिक पूर्णिमा)", "नोव्हेंबर (कार्तिक पौर्णिमा)"),
             ("The ghats are lit with lakhs of lamps.", "घाट लाखों दीयों से जगमगाते हैं।", "घाट लाखो दिव्यांनी उजळतात.")),
        fest("deepotsav", "Diwali and Deepotsav, Ayodhya", "दीवाली और दीपोत्सव, अयोध्या", "दिवाळी व दीपोत्सव, अयोध्या", ("October–November", "अक्टूबर–नवंबर", "ऑक्टोबर–नोव्हेंबर"),
             ("Lamps along the Saryu ghats.", "सरयू घाटों पर दीपों की कतारें।", "शरयू घाटांवर दिव्यांच्या रांगा.")),
        fest("janmashtami", "Janmashtami, Mathura–Vrindavan", "जन्माष्टमी, मथुरा–वृंदावन", "जन्माष्टमी, मथुरा–वृंदावन", ("August–September", "अगस्त–सितंबर", "ऑगस्ट–सप्टेंबर"),
             ("Midnight celebration of Krishna's birth.", "कृष्ण जन्म का आधी रात का उत्सव।", "मध्यरात्री कृष्णजन्माचा उत्सव.")),
        fest("ramlila", "Ramlila and Dussehra", "रामलीला और दशहरा", "रामलीला व दसरा", ("September–October", "सितंबर–अक्टूबर", "सप्टेंबर–ऑक्टोबर"),
             ("Month-long Ramlila at Ramnagar; staged performances in towns and villages.", "रामनगर में महीने भर की रामलीला; कस्बों और गाँवों में मंचन।", "रामनगर येथे महिनाभर रामलीला; गावोगावी सादरीकरण.")),
        fest("eid", "Eid al-Fitr and Eid al-Adha", "ईद-उल-फ़ित्र और ईद-उल-अज़हा", "ईद-उल-फित्र आणि ईद-उल-अजहा", ("Lunar calendar", "चंद्र कैलेंडर", "चांद्र दिनदर्शिका"),
             ("Celebrated with sewaiyan, biryani and family gatherings, especially in Lucknow and the western cities.", "सेवइयों, बिरयानी और पारिवारिक मेल-मिलाप के साथ, ख़ासकर लखनऊ और पश्चिमी शहरों में।", "शेवया, बिर्याणी आणि कौटुंबिक मेळाव्यांसह, विशेषतः लखनौ व पश्चिमेकडील शहरांत.")),
        fest("chhath", "Chhath Puja", "छठ पूजा", "छठ पूजा", ("October–November", "अक्टूबर–नवंबर", "ऑक्टोबर–नोव्हेंबर"),
             ("Offerings to the setting and rising sun at riverbanks in eastern UP.", "पूर्वी उत्तर प्रदेश में नदी तटों पर डूबते और उगते सूर्य को अर्घ्य।", "पूर्व उत्तर प्रदेशात नदीकाठी मावळत्या व उगवत्या सूर्याला अर्घ्य.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("arts", [
        it3("kathak", "Kathak", "कथक", "कथक"), it3("thumri", "Thumri and dadra", "ठुमरी और दादरा", "ठुमरी व दादरा"),
        it3("ramlila", "Ramlila", "रामलीला", "रामलीला"), it3("nautanki", "Nautanki", "नौटंकी", "नौटंकी"),
        it3("birha", "Birha", "बिरहा", "बिरहा"), it3("qawwali", "Qawwali", "क़व्वाली", "कव्वाली"),
        it3("chikan", "Chikankari", "चिकनकारी", "चिकनकारी"), it3("brocade", "Banarasi brocade weaving", "बनारसी ब्रोकेड बुनाई", "बनारसी जरी विणकाम"),
    ], layout="chips", title=L("Arts and crafts", "कलाएँ और शिल्प", "कला व हस्तकला"), conf="Editorial"),
    lst("food", [
        it3("kebab", "Awadhi kebabs and biryani", "अवधी कबाब और बिरयानी", "अवधी कबाब व बिर्याणी", d=("Galouti and kakori kebabs, dum-cooked biryani and nihari from Lucknow.", "लखनऊ के गलौटी और काकोरी कबाब, दम पुख़्त बिरयानी और निहारी।", "लखनौचे गलौटी व काकोरी कबाब, दम बिर्याणी आणि निहारी.")),
        it3("chaat", "Banarasi chaat and kachori", "बनारसी चाट और कचौड़ी", "बनारसी चाट व कचोरी", d=("Tamatar chaat, kachori-sabzi and jalebi for breakfast.", "टमाटर चाट, कचौड़ी-सब्ज़ी और नाश्ते में जलेबी।", "टोमॅटो चाट, कचोरी-भाजी आणि न्याहारीला जिलेबी.")),
        it3("petha", "Agra petha", "आगरा का पेठा", "आग्र्याचा पेठा", d=("Translucent candy made from ash gourd.", "पेठा कद्दू से बनी पारदर्शी मिठाई।", "कोहळ्यापासून बनणारी पारदर्शक मिठाई.")),
        it3("malaiyo", "Malaiyo (makhan malai)", "मलइयो (मक्खन मलाई)", "मलइयो (मक्खन मलई)", d=("Saffron-flavoured milk froth sold on winter mornings in Varanasi and Lucknow.", "वाराणसी और लखनऊ में सर्दियों की सुबह बिकने वाला केसरिया दूध का झाग।", "वाराणसी व लखनौत हिवाळ्यातील सकाळी मिळणारा केशरी दुधाचा फेस.")),
        it3("bedmi", "Bedmi puri and aloo", "बेड़मी पूरी और आलू", "बेडमी पुरी व बटाटा भाजी", d=("Lentil-stuffed puris with spicy potato curry, a breakfast of Braj and the west.", "दाल भरी पूरियाँ और तीखी आलू की सब्ज़ी, ब्रज और पश्चिम का नाश्ता।", "डाळ भरलेल्या पुऱ्या व तिखट बटाट्याची भाजी — ब्रज व पश्चिम भागाची न्याहारी.")),
        it3("pan", "Banarasi paan", "बनारसी पान", "बनारसी पान", d=("Betel leaf with fillings, a Varanasi institution.", "भरावन वाला पान, वाराणसी की पहचान।", "विविध मसाले भरलेले विड्याचे पान — वाराणसीची ओळख.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
    lst("dress", [
        it3("chikan", "Chikan kurta", "चिकन का कुर्ता", "चिकनकारी कुर्ता", d=("Fine white-on-white embroidery from Lucknow.", "लखनऊ की बारीक सफ़ेद-पर-सफ़ेद कढ़ाई।", "लखनौचे पांढऱ्यावर पांढरे बारीक भरतकाम.")),
        it3("banarasi", "Banarasi saree", "बनारसी साड़ी", "बनारसी साडी", d=("Silk saree with gold and silver zari brocade, worn at weddings.", "सोने-चाँदी की ज़री ब्रोकेड वाली रेशमी साड़ी, शादियों में पहनी जाती है।", "सोन्या-चांदीच्या जरीकामाची रेशमी साडी, लग्नसमारंभात परिधान केली जाते.")),
    ], title=L("Traditional dress", "पारंपरिक वेशभूषा", "पारंपरिक वेशभूषा"), conf="Editorial"),
])

# ---------------- H. Economy ----------------
cur = mo["gsdp"]; pc = mo["pcnsdp"]
g = mo["gsva2024_25_current_lakh"]
sect, (prim, sec, serv) = sector_table(g)
agri = 100 * g["agri"] / g["total"]
crops = table("crops", L("Agricultural production, 2021-22", "कृषि उत्पादन, 2021-22", "कृषी उत्पादन, 2021-22"),
              [col(L("Crop group", "फ़सल समूह", "पीकगट")), col(L("Production (lakh tonnes)", "उत्पादन (लाख टन)", "उत्पादन (लाख टन)"), "right")],
              [[L("Foodgrains", "खाद्यान्न", "अन्नधान्य"), "594.80"], [L("Sugarcane", "गन्ना", "ऊस"), "2,272.19"],
               [L("Potato", "आलू", "बटाटा"), "242.75"], [L("Oilseeds", "तिलहन", "तेलबिया"), "12.38"]],
              "up-des", UPF, period="2021-22",
              note=L("Economics & Statistics Division, Government of Uttar Pradesh ('Uttar Pradesh at a Glance 2022'). Yields: wheat 37.34 q/ha, rice 26.77 q/ha.",
                     "अर्थ एवं संख्या प्रभाग, उत्तर प्रदेश सरकार ('उत्तर प्रदेश एक दृष्टि में 2022')। उपज: गेहूँ 37.34 क्विंटल/हेक्टेयर, चावल 26.77 क्विंटल/हेक्टेयर।",
                     "अर्थ व सांख्यिकी विभाग, उत्तर प्रदेश शासन ('उत्तर प्रदेश दृष्टिक्षेपात 2022'). उत्पादकता: गहू 37.34 क्विं./हे., तांदूळ 26.77 क्विं./हे."))
module(R, "economy", [
    prose("p1", L(
        f"Uttar Pradesh is one of India's three largest State economies by GSDP — about ₹{cur['FY2024-25'][0]/1e5:.2f} lakh crore at current prices in FY2024-25 in the MoSPI series — but with the largest population its per capita NSDP, ₹{inr(pc['FY2024-25'][0])}, is among the lowest of the large States. Agriculture and allied activities still make up about {agri:.0f}% of GSVA and employ a large share of workers: the State is India's biggest producer of sugarcane and potatoes and a leading producer of wheat, milk and mangoes.\n\nIndustry is concentrated in the west and around a few cities: electronics and mobile-phone assembly in Noida and Greater Noida, leather in Kanpur and Agra, brass in Moradabad, glass in Firozabad, locks in Aligarh, carpets in Bhadohi–Mirzapur and silk in Varanasi. Construction and real estate have grown fast with expressways, airports and housing. The PLFS unemployment rate was 2.7% in 2025, but women's labour-force participation (32.4%) was well below the national 40%.",
        f"जीएसडीपी के हिसाब से उत्तर प्रदेश भारत की तीन सबसे बड़ी राज्य अर्थव्यवस्थाओं में है — मोस्पी शृंखला में वित्त वर्ष 2024-25 में प्रचलित मूल्यों पर लगभग ₹{cur['FY2024-25'][0]/1e5:.2f} लाख करोड़ — लेकिन सबसे बड़ी आबादी के कारण इसका प्रति व्यक्ति एनएसडीपी, ₹{inr(pc['FY2024-25'][0])}, बड़े राज्यों में सबसे कम में से है। कृषि और संबद्ध गतिविधियाँ अब भी जीएसवीए का लगभग {agri:.0f}% हैं और बड़ी संख्या में श्रमिकों को रोज़गार देती हैं: राज्य भारत में गन्ने और आलू का सबसे बड़ा उत्पादक है और गेहूँ, दूध व आम का प्रमुख उत्पादक है।\n\nउद्योग पश्चिम में और कुछ शहरों के आसपास केंद्रित है: नोएडा और ग्रेटर नोएडा में इलेक्ट्रॉनिक्स और मोबाइल फ़ोन असेंबली, कानपुर और आगरा में चमड़ा, मुरादाबाद में पीतल, फ़िरोज़ाबाद में काँच, अलीगढ़ में ताले, भदोही–मिर्ज़ापुर में क़ालीन और वाराणसी में रेशम। एक्सप्रेसवे, हवाई अड्डों और आवास के साथ निर्माण और रियल एस्टेट तेज़ी से बढ़े हैं। 2025 में पीएलएफ़एस बेरोज़गारी दर 2.7% थी, लेकिन महिलाओं की श्रम बल भागीदारी (32.4%) राष्ट्रीय 40% से काफ़ी कम थी।",
        f"जीएसडीपीच्या दृष्टीने उत्तर प्रदेश ही भारतातील तीन सर्वांत मोठ्या राज्य अर्थव्यवस्थांपैकी एक आहे — मोस्पी मालिकेनुसार आ.व. 2024-25 मध्ये चालू किमतींनुसार सुमारे ₹{cur['FY2024-25'][0]/1e5:.2f} लाख कोटी — पण सर्वाधिक लोकसंख्येमुळे दरडोई एनएसडीपी, ₹{inr(pc['FY2024-25'][0])}, मोठ्या राज्यांतील सर्वांत कमींपैकी आहे. कृषी व संलग्न क्षेत्रांचा जीएसव्हीएमध्ये अजूनही सुमारे {agri:.0f}% वाटा आहे आणि ते मोठ्या संख्येने कामगारांना रोजगार देते: राज्य हे भारतातील सर्वांत मोठे ऊस व बटाटा उत्पादक असून गहू, दूध व आंब्याचे आघाडीचे उत्पादक आहे.\n\nउद्योग पश्चिम भागात आणि काही शहरांभोवती एकवटला आहे: नोएडा व ग्रेटर नोएडात इलेक्ट्रॉनिक्स व मोबाइल फोन जुळणी, कानपूर व आग्र्यात चामडे, मुरादाबादमध्ये पितळ, फिरोजाबादमध्ये काच, अलीगढमध्ये कुलपे, भदोही–मिर्झापूरमध्ये गालिचे आणि वाराणसीत रेशीम. द्रुतगती मार्ग, विमानतळ व गृहनिर्माणामुळे बांधकाम व स्थावर मालमत्ता झपाट्याने वाढल्या आहेत. 2025 मध्ये पीएलएफएस बेरोजगारी दर 2.7% होता, पण स्त्रियांचा श्रमशक्ती सहभाग (32.4%) राष्ट्रीय 40% पेक्षा बराच कमी होता."),
        sources=["mospi", "plfs", "up-des"], conf="Official"),
    facts("f", [
        fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
             dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_NAS), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
             dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_NAS), "rupeeCrore", "higher-is-better",
             previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
        fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
             dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_NAS), "rupee", "higher-is-better",
             previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
        *plfs_facts("UP", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    crops,
    plfs_series("UP", NAME),
    lst("sectors-key", [
        it3("agri", "Sugarcane, wheat, potato and dairy", "गन्ना, गेहूँ, आलू और डेयरी", "ऊस, गहू, बटाटा व दुग्धव्यवसाय", d=("Sugar mills across the west and Terai; potato cold-storage belt around Agra and Farrukhabad.", "पश्चिम और तराई में चीनी मिलें; आगरा और फ़र्रुख़ाबाद के आसपास आलू कोल्ड स्टोरेज पट्टी।", "पश्चिम व तराईत साखर कारखाने; आग्रा व फर्रुखाबादभोवती बटाटा शीतगृह पट्टा.")),
        it3("electronics", "Electronics and mobile phones", "इलेक्ट्रॉनिक्स और मोबाइल फ़ोन", "इलेक्ट्रॉनिक्स व मोबाइल फोन", d=("Noida and Greater Noida.", "नोएडा और ग्रेटर नोएडा।", "नोएडा व ग्रेटर नोएडा.")),
        it3("leather", "Leather and footwear", "चमड़ा और जूते", "चामडे व पादत्राणे", d=("Kanpur, Agra and Unnao.", "कानपुर, आगरा और उन्नाव।", "कानपूर, आग्रा व उन्नाव.")),
        it3("crafts", "Brass, glass, carpets and silk", "पीतल, काँच, क़ालीन और रेशम", "पितळ, काच, गालिचे व रेशीम", d=("Moradabad, Firozabad, Bhadohi and Varanasi.", "मुरादाबाद, फ़िरोज़ाबाद, भदोही और वाराणसी।", "मुरादाबाद, फिरोजाबाद, भदोही व वाराणसी.")),
        it3("tourism", "Pilgrimage and heritage tourism", "तीर्थ और धरोहर पर्यटन", "तीर्थ व वारसा पर्यटन", d=("Ayodhya, Varanasi, Prayagraj, Mathura–Vrindavan and Agra.", "अयोध्या, वाराणसी, प्रयागराज, मथुरा–वृंदावन और आगरा।", "अयोध्या, वाराणसी, प्रयागराज, मथुरा–वृंदावन व आग्रा.")),
        it3("msme", "MSMEs and handicrafts", "एमएसएमई और हस्तशिल्प", "एमएसएमई व हस्तकला", d=("Many districts have a designated 'One District One Product'.", "कई ज़िलों का एक निर्धारित 'एक ज़िला एक उत्पाद' है।", "अनेक जिल्ह्यांचे ठरलेले 'एक जिल्हा एक उत्पादन' आहे.")),
    ], layout="cards", title=L("Key sectors", "प्रमुख क्षेत्र", "प्रमुख क्षेत्रे"), conf="Editorial"),
    gaps("g", [
        (L("GSDP, FY2025-26", "जीएसडीपी, वित्त वर्ष 2025-26", "जीएसडीपी, आ.व. 2025-26"), "mospi", "Not yet published by MoSPI for Uttar Pradesh at access time."),
        (L("Debt-to-GSDP ratio", "ऋण-जीएसडीपी अनुपात", "कर्ज-जीएसडीपी गुणोत्तर"), "rbi-handbook", "RBI State Finances: A Study of Budgets."),
        (L("FDI equity inflows", "एफ़डीआई इक्विटी प्रवाह", "एफडीआय समभाग गुंतवणूक"), "dpiit", "DPIIT state-wise FDI factsheet."),
        (L("Milk production", "दुग्ध उत्पादन", "दूध उत्पादन"), "india-gov", "Department of Animal Husbandry, Basic Animal Husbandry Statistics."),
    ]),
])

# ---------------- I. Government ----------------
module(R, "government", [
    prose("p1", L(
        "Uttar Pradesh has a bicameral legislature in Lucknow: the 403-member Legislative Assembly (Vidhan Sabha) — the largest State assembly in India — and a 100-member Legislative Council (Vidhan Parishad). The State elects 80 members to the Lok Sabha, more than any other State, and 31 to the Rajya Sabha.\n\nIn the 2022 Assembly election the BJP won 255 seats and Yogi Adityanath was sworn in for a second consecutive term as Chief Minister on 25 March 2022. Satish Mahana is Speaker, and Mata Prasad Pandey of the Samajwadi Party has been Leader of Opposition since July 2024. The next Assembly election is due in 2027. Anandiben Patel has been Governor since July 2019.",
        "उत्तर प्रदेश में लखनऊ में द्विसदनीय विधानमंडल है: 403 सदस्यों वाली विधानसभा — भारत की सबसे बड़ी राज्य विधानसभा — और 100 सदस्यों वाली विधान परिषद। राज्य से लोकसभा के 80 सदस्य चुने जाते हैं, जो किसी भी अन्य राज्य से अधिक हैं, और राज्यसभा के 31।\n\n2022 के विधानसभा चुनाव में भाजपा ने 255 सीटें जीतीं और योगी आदित्यनाथ ने 25 मार्च 2022 को लगातार दूसरे कार्यकाल के लिए मुख्यमंत्री पद की शपथ ली। सतीश महाना अध्यक्ष हैं, और समाजवादी पार्टी के माता प्रसाद पांडेय जुलाई 2024 से नेता प्रतिपक्ष हैं। अगला विधानसभा चुनाव 2027 में होना है। आनंदीबेन पटेल जुलाई 2019 से राज्यपाल हैं।",
        "उत्तर प्रदेशमध्ये लखनौ येथे द्विसदनी विधिमंडळ आहे: 403 सदस्यांची विधानसभा — भारतातील सर्वांत मोठी राज्य विधानसभा — आणि 100 सदस्यांची विधान परिषद. राज्यातून लोकसभेवर 80 सदस्य निवडले जातात — इतर कोणत्याही राज्यापेक्षा जास्त — आणि राज्यसभेवर 31.\n\n2022 च्या विधानसभा निवडणुकीत भाजपने 255 जागा जिंकल्या आणि योगी आदित्यनाथ यांनी 25 मार्च 2022 रोजी सलग दुसऱ्यांदा मुख्यमंत्रिपदाची शपथ घेतली. सतीश महाना अध्यक्ष आहेत, आणि समाजवादी पक्षाचे माता प्रसाद पांडे जुलै 2024 पासून विरोधी पक्षनेते आहेत. पुढील विधानसभा निवडणूक 2027 मध्ये होणार आहे. आनंदीबेन पटेल जुलै 2019 पासून राज्यपाल आहेत."),
        sources=["eci", "newsonair"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    table("results", L("Legislative Assembly election, 2022 — seats won", "विधानसभा चुनाव, 2022 — जीती गई सीटें", "विधानसभा निवडणूक, 2022 — जिंकलेल्या जागा"),
          [col(L("Party", "दल", "पक्ष")), col(L("Seats", "सीटें", "जागा"), "right")],
          [["Bharatiya Janata Party (BJP)", 255], ["Samajwadi Party (SP)", 111], ["Apna Dal (Soneylal)", 12], ["Rashtriya Lok Dal (RLD)", 8],
           ["Nirbal Indian Shoshit Hamara Aam Dal (NISHAD)", 6], ["Suheldev Bharatiya Samaj Party (SBSP)", 6],
           ["Indian National Congress (INC)", 2], ["Jansatta Dal Loktantrik", 2], ["Bahujan Samaj Party (BSP)", 1],
           [L("Total", "कुल", "एकूण"), 403]],
          "eci", ECI, period="2022",
          note=L("Seats won as listed by the Election Commission (results declared March 2022). Parties are shown by seats, without colours or commentary. By-elections and defections since 2022 have changed party strengths in the House.",
                 "चुनाव आयोग की सूची के अनुसार जीती गई सीटें (परिणाम मार्च 2022 में घोषित)। दलों को सीटों के क्रम में, बिना रंग या टिप्पणी के दिखाया गया है। 2022 के बाद उपचुनावों और दलबदल से सदन में दलों की संख्या बदली है।",
                 "निवडणूक आयोगाच्या यादीनुसार जिंकलेल्या जागा (निकाल मार्च 2022 मध्ये जाहीर). पक्ष जागांच्या क्रमाने, रंग किंवा भाष्याशिवाय दाखवले आहेत. 2022 नंतरच्या पोटनिवडणुका व पक्षांतरांमुळे सभागृहातील पक्षीय बळ बदलले आहे.")),
    table("local", L("Local bodies", "स्थानीय निकाय", "स्थानिक स्वराज्य संस्था"),
          [col(L("Type", "प्रकार", "प्रकार")), col(L("Number", "संख्या", "संख्या"), "right")],
          [[L("Nagar nigams (municipal corporations)", "नगर निगम", "महानगरपालिका"), 17], [L("Nagar palika parishads", "नगर पालिका परिषदें", "नगरपालिका परिषदा"), 200],
           [L("Nagar panchayats", "नगर पंचायतें", "नगर पंचायती"), 508], [L("Gram panchayats", "ग्राम पंचायतें", "ग्रामपंचायती"), "58,189"]],
          "up-des", UPF, note=L("Urban bodies as on 31 March 2021; gram panchayats as on 31 March 2022.", "नगरीय निकाय 31 मार्च 2021 की स्थिति में; ग्राम पंचायतें 31 मार्च 2022 की स्थिति में।", "नागरी संस्था 31 मार्च 2021 रोजीच्या; ग्रामपंचायती 31 मार्च 2022 रोजीच्या.")),
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("assembly", "Uttar Pradesh Legislative Assembly", "उत्तर प्रदेश विधानसभा", "उत्तर प्रदेश विधानसभा", url="https://uplegisassembly.gov.in", src="india-gov"),
        it3("portal", "Government of Uttar Pradesh", "उत्तर प्रदेश सरकार", "उत्तर प्रदेश शासन", url="https://up.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Governor's official page (Lok Bhavan, Uttar Pradesh)", "राज्यपाल का आधिकारिक पेज (लोक भवन, उत्तर प्रदेश)", "राज्यपालांचे अधिकृत पान (लोकभवन, उत्तर प्रदेश)"), "india-gov", "Replace the news citations with the official page."),
        (L("Current party strength in the Assembly", "विधानसभा में वर्तमान दलीय स्थिति", "विधानसभेतील सध्याचे पक्षीय बळ"), "india-gov", "Assembly secretariat member list."),
        (L("Flagship welfare schemes", "प्रमुख कल्याण योजनाएँ", "प्रमुख कल्याणकारी योजना"), "india-gov", "List with official scheme pages and current status."),
    ]),
])

# ---------------- J. Projects ----------------
module(R, "projects", [
    prose("p1", L(
        "Uttar Pradesh has built a network of access-controlled expressways over the past decade — Yamuna, Agra–Lucknow, Purvanchal, Bundelkhand, Gorakhpur Link and, in April 2026, the 594 km Ganga Expressway from Meerut to Prayagraj — along with new airports, the largest being Noida International Airport at Jewar, opened in March 2026. Both dedicated freight corridors also pass through the State. Each card shows its source and the date it was checked.",
        "उत्तर प्रदेश ने पिछले एक दशक में एक्सेस-नियंत्रित एक्सप्रेसवे का जाल बनाया है — यमुना, आगरा–लखनऊ, पूर्वांचल, बुंदेलखंड, गोरखपुर लिंक और अप्रैल 2026 में मेरठ से प्रयागराज तक 594 किमी का गंगा एक्सप्रेसवे — साथ ही नए हवाई अड्डे, जिनमें सबसे बड़ा जेवर का नोएडा अंतरराष्ट्रीय हवाई अड्डा है, जो मार्च 2026 में खुला। दोनों समर्पित माल गलियारे भी राज्य से होकर जाते हैं। हर कार्ड पर स्रोत और जाँच की तारीख़ है।",
        "उत्तर प्रदेशने गेल्या दशकात प्रवेश-नियंत्रित द्रुतगती मार्गांचे जाळे उभारले आहे — यमुना, आग्रा–लखनौ, पूर्वांचल, बुंदेलखंड, गोरखपूर लिंक आणि एप्रिल 2026 मध्ये मेरठ ते प्रयागराज 594 किमीचा गंगा द्रुतगती मार्ग — सोबत नवे विमानतळ, त्यांतील सर्वांत मोठे म्हणजे मार्च 2026 मध्ये सुरू झालेले जेवरचे नोएडा आंतरराष्ट्रीय विमानतळ. दोन्ही समर्पित मालवाहतूक मार्गिकाही राज्यातून जातात. प्रत्येक कार्डावर स्रोत व तपासणीची तारीख आहे."),
        sources=["pmindia", "newsonair"], conf="Official"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Metro projects (Kanpur, Agra) — official status", "मेट्रो परियोजनाएँ (कानपुर, आगरा) — आधिकारिक स्थिति", "मेट्रो प्रकल्प (कानपूर, आग्रा) — अधिकृत स्थिती"), "india-gov", "UP Metro Rail Corporation status pages."),
        (L("Ken–Betwa river link — UP share and status", "केन–बेतवा नदी जोड़ — उत्तर प्रदेश का हिस्सा और स्थिति", "केन–बेतवा नदीजोड — उत्तर प्रदेशचा वाटा व स्थिती"), "india-gov", "National Water Development Agency."),
        (L("State vision document", "राज्य दृष्टि दस्तावेज़", "राज्य दृष्टी दस्तऐवज"), "india-gov", "State Planning Department."),
    ]),
])

# ---------------- K. Transport ----------------
module(R, "transport", [
    prose("p1", L(
        "Uttar Pradesh sits on the main routes between Delhi and eastern India. Its railway network is one of the densest in the country, with major junctions at Prayagraj, Kanpur, Lucknow, Gorakhpur, Pt. Deen Dayal Upadhyaya (Mughalsarai) and Jhansi, and both the Eastern and Western Dedicated Freight Corridors run through it. The Grand Trunk Road and a growing network of expressways link the cities. Lucknow, Kanpur, Agra and Noida have metro systems, and Ghaziabad is served by the Delhi Metro and the Delhi–Meerut RRTS. International airports serve Lucknow, Varanasi and Noida (Jewar), with Ayodhya, Kushinagar, Prayagraj, Gorakhpur, Agra and other cities on the domestic network.",
        "उत्तर प्रदेश दिल्ली और पूर्वी भारत के बीच मुख्य मार्गों पर स्थित है। इसका रेल नेटवर्क देश के सबसे सघन नेटवर्कों में है, जिसमें प्रयागराज, कानपुर, लखनऊ, गोरखपुर, पं. दीनदयाल उपाध्याय (मुग़लसराय) और झाँसी बड़े जंक्शन हैं, और पूर्वी व पश्चिमी दोनों समर्पित माल गलियारे इससे होकर गुज़रते हैं। ग्रैंड ट्रंक रोड और एक्सप्रेसवे का बढ़ता जाल शहरों को जोड़ता है। लखनऊ, कानपुर, आगरा और नोएडा में मेट्रो है, और ग़ाज़ियाबाद को दिल्ली मेट्रो और दिल्ली–मेरठ आरआरटीएस सेवा देते हैं। लखनऊ, वाराणसी और नोएडा (जेवर) में अंतरराष्ट्रीय हवाई अड्डे हैं, और अयोध्या, कुशीनगर, प्रयागराज, गोरखपुर, आगरा व अन्य शहर घरेलू नेटवर्क पर हैं।",
        "उत्तर प्रदेश दिल्ली आणि पूर्व भारत यांच्यातील मुख्य मार्गांवर आहे. त्याचे रेल्वे जाळे देशातील सर्वांत दाट जाळ्यांपैकी असून प्रयागराज, कानपूर, लखनौ, गोरखपूर, पं. दीनदयाळ उपाध्याय (मुघलसराय) व झाशी ही मोठी जंक्शन्स आहेत, आणि पूर्व व पश्चिम दोन्ही समर्पित मालवाहतूक मार्गिका राज्यातून जातात. ग्रँड ट्रंक रोड आणि वाढते द्रुतगती मार्ग शहरे जोडतात. लखनौ, कानपूर, आग्रा व नोएडात मेट्रो आहे, आणि गाझियाबादला दिल्ली मेट्रो व दिल्ली–मेरठ आरआरटीएसची सेवा मिळते. लखनौ, वाराणसी व नोएडा (जेवर) येथे आंतरराष्ट्रीय विमानतळ आहेत, तर अयोध्या, कुशीनगर, प्रयागराज, गोरखपूर, आग्रा व इतर शहरे देशांतर्गत जाळ्यावर आहेत."),
        conf="Editorial"),
    lst("airports", [
        it3("lko", "Chaudhary Charan Singh International Airport, Lucknow", "चौधरी चरण सिंह अंतरराष्ट्रीय हवाई अड्डा, लखनऊ", "चौधरी चरणसिंह आंतरराष्ट्रीय विमानतळ, लखनौ", m=("LKO", "LKO", "LKO")),
        it3("vns", "Lal Bahadur Shastri International Airport, Varanasi", "लाल बहादुर शास्त्री अंतरराष्ट्रीय हवाई अड्डा, वाराणसी", "लाल बहादूर शास्त्री आंतरराष्ट्रीय विमानतळ, वाराणसी", m=("VNS", "VNS", "VNS")),
        it3("noida", "Noida International Airport, Jewar", "नोएडा अंतरराष्ट्रीय हवाई अड्डा, जेवर", "नोएडा आंतरराष्ट्रीय विमानतळ, जेवर", m=("Opened 2026", "2026 में खुला", "2026 मध्ये सुरू")),
        it3("ayj", "Ayodhya airport", "अयोध्या हवाई अड्डा", "अयोध्या विमानतळ"), it3("kbk", "Kushinagar airport", "कुशीनगर हवाई अड्डा", "कुशीनगर विमानतळ"),
        it3("ixd", "Prayagraj airport", "प्रयागराज हवाई अड्डा", "प्रयागराज विमानतळ"), it3("gop", "Gorakhpur airport", "गोरखपुर हवाई अड्डा", "गोरखपूर विमानतळ"),
        it3("agr", "Agra airport", "आगरा हवाई अड्डा", "आग्रा विमानतळ"),
    ], layout="chips", title=L("Airports (selected)", "हवाई अड्डे (चयनित)", "विमानतळ (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Expressway and national highway length", "एक्सप्रेसवे और राष्ट्रीय राजमार्ग की लंबाई", "द्रुतगती मार्ग व राष्ट्रीय महामार्गांची लांबी"), "morth", "MoRTH Basic Road Statistics; UPEIDA."),
        (L("Railway route length", "रेलवे मार्ग की लंबाई", "रेल्वे मार्गाची लांबी"), "railways", "Indian Railways Year Book."),
        (L("Airport passenger traffic", "हवाई अड्डा यात्री यातायात", "विमानतळ प्रवासी वाहतूक"), "aai", "AAI traffic statistics."),
    ]),
])

# ---------------- L. Energy ----------------
module(R, "energy", [
    prose("p1", L(
        "Most of Uttar Pradesh's electricity comes from coal. The largest stations are in the Singrauli coalfield region of Sonbhadra district — Anpara, Obra, Rihand and Singrauli — with others at Dadri, Unchahar, Panki and Harduaganj. The Narora Atomic Power Station on the Ganga in Bulandshahr district is the State's nuclear plant. Solar capacity has grown, especially in Bundelkhand, and rooftop solar is spreading in cities. Demand is very large and seasonal, peaking in the summer and the paddy-irrigation months; the State's distribution companies operate under UP Power Corporation Limited.",
        "उत्तर प्रदेश की अधिकांश बिजली कोयले से आती है। सबसे बड़े संयंत्र सोनभद्र ज़िले के सिंगरौली कोयला क्षेत्र में हैं — अनपरा, ओबरा, रिहंद और सिंगरौली — और अन्य दादरी, ऊँचाहार, पनकी और हरदुआगंज में। बुलंदशहर ज़िले में गंगा किनारे नरौरा परमाणु बिजलीघर राज्य का परमाणु संयंत्र है। सौर क्षमता बढ़ी है, ख़ासकर बुंदेलखंड में, और शहरों में छत पर सौर ऊर्जा फैल रही है। माँग बहुत बड़ी और मौसमी है, जो गर्मियों और धान सिंचाई के महीनों में चरम पर होती है; राज्य की वितरण कंपनियाँ उत्तर प्रदेश पावर कॉर्पोरेशन लिमिटेड के अधीन काम करती हैं।",
        "उत्तर प्रदेशची बहुतांश वीज कोळशापासून येते. सर्वांत मोठी केंद्रे सोनभद्र जिल्ह्यातील सिंगरौली कोळसा क्षेत्रात आहेत — अनपरा, ओबरा, रिहंद व सिंगरौली — आणि इतर दादरी, ऊंचाहार, पनकी व हरदुआगंज येथे. बुलंदशहर जिल्ह्यात गंगाकाठचे नरौरा अणुऊर्जा केंद्र हे राज्यातील अणुवीज केंद्र आहे. सौरक्षमता वाढली आहे, विशेषतः बुंदेलखंडमध्ये, आणि शहरांत छतावरील सौरऊर्जा पसरत आहे. मागणी प्रचंड व हंगामी असून उन्हाळ्यात आणि भातसिंचनाच्या महिन्यांत शिखरावर असते; राज्याच्या वितरण कंपन्या उत्तर प्रदेश पॉवर कॉर्पोरेशन लिमिटेडअंतर्गत चालतात."),
        conf="Editorial"),
    gaps("g", [
        (L("Installed capacity by source", "स्रोतवार स्थापित क्षमता", "स्रोतनिहाय स्थापित क्षमता"), "cea", "CEA installed capacity report."),
        (L("Solar capacity", "सौर क्षमता", "सौर क्षमता"), "mnre", "MNRE state-wise RE capacity."),
        (L("Per capita electricity consumption", "प्रति व्यक्ति बिजली खपत", "दरडोई वीज वापर"), "cea", "CEA General Review."),
    ]),
])

# ---------------- M. Digital ----------------
module(R, "digital", [
    prose("p1", L(
        "Noida and Greater Noida, in the Delhi region, are among India's largest centres of electronics manufacturing — especially mobile phones and components — and host many IT and IT-enabled services firms. Lucknow, Kanpur and Varanasi have smaller IT clusters and growing start-up activity, supported by incubators at IIT Kanpur and other institutions. Large data-centre campuses have come up around Greater Noida.",
        "दिल्ली क्षेत्र में स्थित नोएडा और ग्रेटर नोएडा भारत के सबसे बड़े इलेक्ट्रॉनिक्स विनिर्माण केंद्रों में हैं — ख़ासकर मोबाइल फ़ोन और पुर्ज़े — और यहाँ कई आईटी और आईटी-सक्षम सेवा कंपनियाँ हैं। लखनऊ, कानपुर और वाराणसी में छोटे आईटी क्लस्टर और बढ़ती स्टार्टअप गतिविधि है, जिसे आईआईटी कानपुर और अन्य संस्थानों के इनक्यूबेटर सहारा देते हैं। ग्रेटर नोएडा के आसपास बड़े डेटा सेंटर परिसर बने हैं।",
        "दिल्ली परिसरातील नोएडा व ग्रेटर नोएडा ही भारतातील सर्वांत मोठ्या इलेक्ट्रॉनिक्स उत्पादन केंद्रांपैकी आहेत — विशेषतः मोबाइल फोन व सुटे भाग — आणि तिथे अनेक आयटी व आयटी-आधारित सेवा कंपन्या आहेत. लखनौ, कानपूर व वाराणसीत लहान आयटी समूह आणि वाढती स्टार्टअप उलाढाल आहे, ज्याला आयआयटी कानपूर व इतर संस्थांचे इनक्युबेटर पाठबळ देतात. ग्रेटर नोएडाभोवती मोठी डेटा सेंटर संकुले उभी राहिली आहेत."),
        conf="Editorial"),
    gaps("g", [
        (L("Tele-density and internet subscriptions", "टेली-घनत्व और इंटरनेट कनेक्शन", "दूरध्वनी घनता व इंटरनेट जोडण्या"), "india-gov", "TRAI performance indicators (UP East and UP West circles)."),
        (L("DPIIT-recognised start-ups", "डीपीआईआईटी मान्यता प्राप्त स्टार्टअप", "डीपीआयआयटी मान्यताप्राप्त स्टार्टअप"), "startup-india", "Startup India state dashboard."),
        (L("Electronics production and exports", "इलेक्ट्रॉनिक्स उत्पादन और निर्यात", "इलेक्ट्रॉनिक्स उत्पादन व निर्यात"), "india-gov", "MeitY / State electronics policy reports."),
    ]),
])

# ---------------- N. Education ----------------
ef, es = aishe_block("UP", NAME)
module(R, "education", [
    prose("p1", L(
        "Uttar Pradesh has more colleges than any other State — 8,375 in the 2021-22 AISHE survey, alongside 91 universities — but its higher-education gross enrolment ratio (ages 18–23) was 24.1%, below the national 28.4%. Women's GER (24.4%) was slightly above men's (23.9%). Literacy at the 2011 Census was 67.7%, with a 20-point gap between men and women.\n\nThe State has some of India's oldest and best-known institutions: Banaras Hindu University (1916), Aligarh Muslim University, the University of Allahabad and the University of Lucknow; IIT Kanpur, IIT (BHU) Varanasi, IIM Lucknow, IIIT Allahabad and MNNIT Allahabad; and AIIMS at Gorakhpur and Rae Bareli.",
        "उत्तर प्रदेश में किसी भी अन्य राज्य से अधिक कॉलेज हैं — 2021-22 के एआईएसएचई सर्वेक्षण में 8,375, साथ में 91 विश्वविद्यालय — लेकिन उच्च शिक्षा का सकल नामांकन अनुपात (18–23 आयु) 24.1% था, जो राष्ट्रीय 28.4% से कम है। महिलाओं का जीईआर (24.4%) पुरुषों (23.9%) से थोड़ा अधिक था। 2011 की जनगणना में साक्षरता 67.7% थी, जिसमें पुरुषों और महिलाओं के बीच 20 अंकों का अंतर था।\n\nराज्य में भारत के सबसे पुराने और प्रसिद्ध संस्थानों में से कुछ हैं: बनारस हिंदू विश्वविद्यालय (1916), अलीगढ़ मुस्लिम विश्वविद्यालय, इलाहाबाद विश्वविद्यालय और लखनऊ विश्वविद्यालय; आईआईटी कानपुर, आईआईटी (बीएचयू) वाराणसी, आईआईएम लखनऊ, ट्रिपल आईटी इलाहाबाद और एमएनएनआईटी इलाहाबाद; और गोरखपुर व रायबरेली में एम्स।",
        "उत्तर प्रदेशमध्ये इतर कोणत्याही राज्यापेक्षा जास्त महाविद्यालये आहेत — 2021-22 च्या एआयएसएचई सर्वेक्षणात 8,375, सोबत 91 विद्यापीठे — पण उच्चशिक्षणाचे एकूण नोंदणी गुणोत्तर (18–23 वय) 24.1% होते, राष्ट्रीय 28.4% पेक्षा कमी. स्त्रियांचे जीईआर (24.4%) पुरुषांपेक्षा (23.9%) किंचित जास्त होते. 2011 च्या जनगणनेत साक्षरता 67.7% होती, आणि पुरुष-स्त्रियांमध्ये 20 अंकांची तफावत होती.\n\nराज्यात भारतातील काही सर्वांत जुन्या व प्रसिद्ध संस्था आहेत: बनारस हिंदू विद्यापीठ (1916), अलीगढ मुस्लिम विद्यापीठ, अलाहाबाद विद्यापीठ व लखनौ विद्यापीठ; आयआयटी कानपूर, आयआयटी (बीएचयू) वाराणसी, आयआयएम लखनौ, ट्रिपल आयटी अलाहाबाद व एमएनएनआयटी अलाहाबाद; आणि गोरखपूर व रायबरेली येथे एम्स."),
        sources=["aishe", "up-des"], conf="Official"),
    ef, es,
    lst("ini", [
        it3("iitk", "IIT Kanpur", "आईआईटी कानपुर", "आयआयटी कानपूर", m=("Kanpur", "कानपुर", "कानपूर")),
        it3("iitbhu", "IIT (BHU) Varanasi", "आईआईटी (बीएचयू) वाराणसी", "आयआयटी (बीएचयू) वाराणसी", m=("Varanasi", "वाराणसी", "वाराणसी")),
        it3("bhu", "Banaras Hindu University", "बनारस हिंदू विश्वविद्यालय", "बनारस हिंदू विद्यापीठ", m=("Varanasi, 1916", "वाराणसी, 1916", "वाराणसी, 1916")),
        it3("amu", "Aligarh Muslim University", "अलीगढ़ मुस्लिम विश्वविद्यालय", "अलीगढ मुस्लिम विद्यापीठ", m=("Aligarh", "अलीगढ़", "अलीगढ")),
        it3("iiml", "IIM Lucknow", "आईआईएम लखनऊ", "आयआयएम लखनौ", m=("Lucknow", "लखनऊ", "लखनौ")),
        it3("iiita", "IIIT Allahabad", "ट्रिपल आईटी इलाहाबाद", "ट्रिपल आयटी अलाहाबाद", m=("Prayagraj", "प्रयागराज", "प्रयागराज")),
        it3("au", "University of Allahabad", "इलाहाबाद विश्वविद्यालय", "अलाहाबाद विद्यापीठ", m=("Prayagraj", "प्रयागराज", "प्रयागराज")),
        it3("aiims", "AIIMS Gorakhpur and AIIMS Rae Bareli", "एम्स गोरखपुर और एम्स रायबरेली", "एम्स गोरखपूर व एम्स रायबरेली", m=("Medical", "चिकित्सा", "वैद्यकीय")),
    ], title=L("National institutions (selected)", "राष्ट्रीय संस्थान (चयनित)", "राष्ट्रीय संस्था (निवडक)"), conf="Editorial"),
    gaps("g", [
        (L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year."),
        (L("Dropout rates by level", "स्तरवार ड्रॉपआउट दर", "स्तरनिहाय गळती दर"), "udise", "UDISE+."),
        (L("NIRF-ranked institutions", "एनआईआरएफ़ रैंक वाले संस्थान", "एनआयआरएफ क्रमवारीतील संस्था"), "nirf", "Latest NIRF list filtered to Uttar Pradesh."),
    ]),
])

# ---------------- O. Health ----------------
module(R, "health", [
    prose("p1", L(
        "Uttar Pradesh has made large gains in health but still lags the national average on several measures. In NFHS-5 (2019-21), 39.7% of children under five were stunted — down from 46.3% in NFHS-4 but above the national 35.5% — and 83.4% of births took place in health facilities, against 88.6% nationally. The infant mortality rate was 38 per 1,000 live births in 2020 (SRS, as reported by the State), and life expectancy at birth was about 65–66 years in 2015-19.\n\nThe State runs a very large public health system, with AIIMS at Gorakhpur and Rae Bareli and medical colleges in most divisions. Gorakhpur and the eastern districts have long fought acute encephalitis syndrome, which has declined sharply with vaccination and sanitation drives.",
        "उत्तर प्रदेश ने स्वास्थ्य में बड़ी प्रगति की है, फिर भी कई मापदंडों पर यह राष्ट्रीय औसत से पीछे है। एनएफ़एचएस-5 (2019-21) में पाँच वर्ष से कम आयु के 39.7% बच्चे ठिगने थे — एनएफ़एचएस-4 के 46.3% से कम, लेकिन राष्ट्रीय 35.5% से अधिक — और 83.4% प्रसव स्वास्थ्य संस्थानों में हुए, जबकि राष्ट्रीय स्तर पर 88.6%। 2020 में शिशु मृत्यु दर प्रति 1,000 जीवित जन्म पर 38 थी (एसआरएस, राज्य द्वारा प्रकाशित), और 2015-19 में जन्म के समय जीवन प्रत्याशा लगभग 65–66 वर्ष थी।\n\nराज्य बहुत बड़ी सार्वजनिक स्वास्थ्य व्यवस्था चलाता है, जिसमें गोरखपुर और रायबरेली में एम्स और अधिकांश मंडलों में मेडिकल कॉलेज हैं। गोरखपुर और पूर्वी ज़िले लंबे समय से एक्यूट इन्सेफ़ेलाइटिस सिंड्रोम से जूझते रहे हैं, जो टीकाकरण और स्वच्छता अभियानों से तेज़ी से घटा है।",
        "उत्तर प्रदेशने आरोग्यात मोठी प्रगती केली आहे, तरी अनेक निकषांवर ते राष्ट्रीय सरासरीच्या मागे आहे. एनएफएचएस-5 (2019-21) मध्ये पाच वर्षांखालील 39.7% मुले खुजी होती — एनएफएचएस-4 मधील 46.3% पेक्षा कमी, पण राष्ट्रीय 35.5% पेक्षा जास्त — आणि 83.4% प्रसूती आरोग्य संस्थांत झाल्या, तर राष्ट्रीय प्रमाण 88.6%. 2020 मध्ये अर्भक मृत्युदर दर 1,000 जिवंत जन्मांमागे 38 होता (एसआरएस, राज्याने प्रकाशित केलेला), आणि 2015-19 मध्ये जन्मतः आयुर्मान सुमारे 65–66 वर्षे होते.\n\nराज्य अतिशय मोठी सार्वजनिक आरोग्य व्यवस्था चालवते — गोरखपूर व रायबरेली येथे एम्स आणि बहुतेक विभागांत वैद्यकीय महाविद्यालये. गोरखपूर व पूर्वेकडील जिल्हे दीर्घकाळ तीव्र मेंदूज्वर संलक्षणाशी लढत आले आहेत; लसीकरण व स्वच्छता मोहिमांमुळे त्याचे प्रमाण झपाट्याने घटले आहे."),
        sources=["nfhs", "up-des"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(38, "per 1,000 live births", "2020", "calendar", "srs", UPF, note="SRS 2020, as published by the Economics & Statistics Division, Government of Uttar Pradesh."), "number", "lower-is-better"),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"),
             dp(25.1, "per 1,000 population", "2020", "calendar", "srs", UPF, note="SRS 2020 via UP DES (rural 26.1, urban 22.1)."), "number"),
        fact("dr", L("Death rate", "मृत्यु दर", "मृत्युदर"),
             dp(6.5, "per 1,000 population", "2020", "calendar", "srs", UPF, note="SRS 2020 via UP DES (rural 6.8, urban 5.4)."), "number", "lower-is-better"),
    ], title=L("Vital statistics (Sample Registration System)", "महत्वपूर्ण आँकड़े (नमूना पंजीकरण प्रणाली)", "महत्त्वाची आकडेवारी (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("UP"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
    gaps("g", [
        (L("Maternal and under-five mortality (SRS 2019-21 / 2021)", "मातृ और पाँच वर्ष से कम आयु की मृत्यु दर (एसआरएस)", "माता व पाच वर्षांखालील मृत्युदर (एसआरएस)"), "srs", "SRS special bulletin; the PIB summary used for other States lists only States that met SDG targets."),
        (L("Life expectancy at birth (both sexes)", "जन्म के समय जीवन प्रत्याशा (कुल)", "जन्मतः आयुर्मान (एकूण)"), "srs", "SRS abridged life tables; State publication gives male 65.0 and female 66.2 for 2015-19 only."),
        (L("Hospitals and health centres", "अस्पताल और स्वास्थ्य केंद्र", "रुग्णालये व आरोग्य केंद्रे"), "mohfw", "Health Dynamics of India."),
    ]),
])
print("up mod2 ok")
