"""Tripura modules G–O."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

R = "IN-TR"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
NOTE = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 25 Oct 2026. "
        "FY2024-25 is the latest year published for Tripura and may be revised.")
mo = research("mospi_tr.json")
C = research("census_b5plus.json")
NAME = L("Tripura", "त्रिपुरा", "त्रिपुरा")


def fest(id, en, hi, mr, m, d):
    return item(id, L(en, hi, mr), detail=L(*d), meta=L(*m))


module(R, "culture", [
    prose("p1", L(
        "Tripura's culture blends Bengali traditions — Durga Puja, Kali Puja, kirtan and the songs of Tagore and S. D. Burman — with those of its tribes. The Tripuri Hojagiri dance, performed by women balancing pots and lamps, and the Garia and Lebang Boomani dances are well known. The royal Kharchi Puja, dedicated to fourteen deities, and Ker Puja go back to the Manikya court. Tripura's weavers make the risa and rignai, and its bamboo and cane craft is used for furniture, baskets and decoration.",
        "त्रिपुरा की संस्कृति बंगाली परंपराओं — दुर्गा पूजा, काली पूजा, कीर्तन और टैगोर व एस. डी. बर्मन के गीत — को इसकी जनजातियों की परंपराओं से मिलाती है। त्रिपुरी होजागिरी नृत्य, जिसमें महिलाएँ घड़े और दीपक संतुलित करती हैं, और गड़िया व लेबांग बूमानी नृत्य प्रसिद्ध हैं। चौदह देवताओं को समर्पित राजकीय खारची पूजा और केर पूजा माणिक्य दरबार से चली आ रही हैं। त्रिपुरा के बुनकर रिसा और रिग्नाई बनाते हैं, और इसका बाँस व बेंत शिल्प फ़र्नीचर, टोकरियों और सजावट में काम आता है।",
        "त्रिपुराची संस्कृती बंगाली परंपरा — दुर्गापूजा, कालीपूजा, कीर्तन व टागोर आणि एस. डी. बर्मन यांची गीते — तेथील जमातींच्या परंपरांशी जोडते. त्रिपुरी होजागिरी नृत्य, ज्यात स्त्रिया घडे व दिवे तोलतात, आणि गडिया व लेबांग बूमानी नृत्ये प्रसिद्ध आहेत. चौदा देवतांना समर्पित राजेशाही खारची पूजा व केर पूजा माणिक्य दरबारापासून चालत आल्या आहेत. त्रिपुराचे विणकर रिसा व रिग्नाई बनवतात, आणि तेथील बांबू व वेत हस्तकला फर्निचर, टोपल्या व सजावटीसाठी वापरली जाते."),
        conf="Editorial"),
    lst("festivals", [
        fest("kharchi", "Kharchi Puja", "खारची पूजा", "खारची पूजा", ("July", "जुलाई", "जुलै"), ("Week-long worship of the fourteen deities at Old Agartala.", "पुराने अगरतला में चौदह देवताओं की सप्ताह भर पूजा।", "जुन्या आगरतळ्यात चौदा देवतांची आठवडाभर पूजा.")),
        fest("garia", "Garia Puja", "गड़िया पूजा", "गडिया पूजा", ("April", "अप्रैल", "एप्रिल"), ("Tribal festival for a good harvest.", "अच्छी फ़सल के लिए जनजातीय त्योहार।", "चांगल्या पिकासाठी आदिवासी सण.")),
        fest("durga", "Durga Puja", "दुर्गा पूजा", "दुर्गापूजा", ("September–October", "सितंबर–अक्टूबर", "सप्टेंबर–ऑक्टोबर"), ("The biggest festival in Agartala.", "अगरतला का सबसे बड़ा त्योहार।", "आगरतळ्यातील सर्वांत मोठा सण.")),
        fest("diwali", "Diwali at Tripura Sundari", "त्रिपुरा सुंदरी में दीवाली", "त्रिपुरा सुंदरी येथे दिवाळी", ("October–November", "अक्टूबर–नवंबर", "ऑक्टोबर–नोव्हेंबर"), ("Large fair at the Udaipur temple.", "उदयपुर मंदिर में बड़ा मेला।", "उदयपूर मंदिरात मोठी जत्रा.")),
    ], title=L("Festivals", "त्योहार", "सण-उत्सव"), conf="Editorial"),
    lst("food", [
        it3("mui", "Mui borok", "मुई बोरोक", "मुई बोरोक", d=("Tripuri dishes made with berma (fermented fish).", "बर्मा (किण्वित मछली) से बने त्रिपुरी व्यंजन।", "बर्मा (आंबवलेला मासा) वापरून केलेले त्रिपुरी पदार्थ.")),
        it3("wahan", "Wahan mosdeng", "वाहान मोसदेंग", "वाहान मोसदेंग", d=("Spicy pork salad.", "तीखा सूअर के मांस का सलाद।", "तिखट डुकराच्या मांसाची कोशिंबीर.")),
        it3("peda", "Matabari peda", "माताबाड़ी पेड़ा", "माताबाडी पेढा", d=("Milk sweet offered at Tripura Sundari; a registered GI.", "त्रिपुरा सुंदरी में चढ़ाई जाने वाली दूध की मिठाई; पंजीकृत जीआई।", "त्रिपुरा सुंदरीला अर्पण केली जाणारी दुधाची मिठाई; नोंदणीकृत जीआय.")),
        it3("pineapple", "Queen pineapple", "क्वीन अनानास", "क्वीन अननस", d=("Small, sweet pineapple; a registered GI.", "छोटा, मीठा अनानास; पंजीकृत जीआई।", "लहान, गोड अननस; नोंदणीकृत जीआय.")),
    ], title=L("Food", "खान-पान", "खाद्यसंस्कृती"), conf="Editorial"),
])

cur = mo["gsdp"]; pc = mo["pcnsdp"]; g = mo["gsva2024_25_current_lakh"]
sect, _ = sector_table(g)
sh = {k: 100 * v / g["total"] for k, v in g.items()}
ur = AP["plfs_ur_15plus_psss"]["TR"]; ui = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["TR"]; lfi = AP["plfs_lfpr_2025"]["IN"]
module(R, "economy", [
    prose("p1", L(
        f"Tripura's GSDP at current prices was about ₹{inr(cur['FY2024-25'][0])} crore in FY2024-25, the latest year in the MoSPI series, and per capita NSDP was ₹{inr(pc['FY2024-25'][0])}. Agriculture, livestock, forestry and fishing made up about {sh['agri']:.0f}% of GSVA — rice, vegetables, pineapples, jackfruit and fish from ponds and reservoirs. Rubber plantations, started in the 1960s, now cover large areas and support many tribal families, and tea is grown in the north. Mining and quarrying, mainly natural gas from fields operated by ONGC, was about {sh['mining']:.0f}% of GSVA, and gas fuels power stations at Palatana and Monarchak. Public administration was about {sh['public_admin']:.0f}%. Trade with Bangladesh passes through the Akhaura land port near Agartala.\n\nThe PLFS unemployment rate was {ur['2025']}% in 2025 (national {ui['2025']}%), and {lf['female']}% of women aged 15 and above were in the labour force, against {lfi['female']}% nationally.",
        f"मोस्पी शृंखला के नवीनतम वर्ष, वित्त वर्ष 2024-25 में त्रिपुरा का प्रचलित मूल्यों पर जीएसडीपी लगभग ₹{inr(cur['FY2024-25'][0])} करोड़ और प्रति व्यक्ति एनएसडीपी ₹{inr(pc['FY2024-25'][0])} था। कृषि, पशुपालन, वानिकी और मत्स्य पालन का जीएसवीए में हिस्सा लगभग {sh['agri']:.0f}% था — धान, सब्ज़ियाँ, अनानास, कटहल और तालाबों व जलाशयों की मछली। 1960 के दशक में शुरू हुए रबर बाग़ान अब बड़े क्षेत्र में फैले हैं और बहुत से जनजातीय परिवारों को सहारा देते हैं, और उत्तर में चाय उगाई जाती है। खनन और उत्खनन, मुख्यतः ओएनजीसी द्वारा संचालित क्षेत्रों की प्राकृतिक गैस, जीएसवीए का लगभग {sh['mining']:.0f}% था, और गैस पलाटाना और मोनारचक के बिजलीघरों को ईंधन देती है। लोक प्रशासन लगभग {sh['public_admin']:.0f}% था। बांग्लादेश के साथ व्यापार अगरतला के पास अखौरा भू-बंदरगाह से होता है।\n\nपीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी (राष्ट्रीय {ui['2025']}%), और 15 वर्ष से अधिक आयु की {lf['female']}% महिलाएँ श्रम बल में थीं, जबकि राष्ट्रीय स्तर पर {lfi['female']}%।",
        f"मोस्पी मालिकेतील नवीनतम वर्ष, आ.व. 2024-25 मध्ये त्रिपुराचे चालू किमतींनुसार जीएसडीपी सुमारे ₹{inr(cur['FY2024-25'][0])} कोटी व दरडोई एनएसडीपी ₹{inr(pc['FY2024-25'][0])} होते. शेती, पशुपालन, वनीकरण व मासेमारीचा जीएसव्हीएमध्ये वाटा सुमारे {sh['agri']:.0f}% होता — भात, भाज्या, अननस, फणस आणि तलाव व जलाशयांतील मासे. 1960 च्या दशकात सुरू झालेले रबराचे मळे आता मोठ्या क्षेत्रावर पसरले आहेत व अनेक आदिवासी कुटुंबांना आधार देतात, आणि उत्तरेत चहा घेतला जातो. खाणकाम व उत्खनन, मुख्यतः ओएनजीसीच्या क्षेत्रांतील नैसर्गिक वायू, जीएसव्हीएच्या सुमारे {sh['mining']:.0f}% होते, आणि वायू पलाटाना व मोनारचक वीजकेंद्रांना इंधन पुरवतो. लोकप्रशासन सुमारे {sh['public_admin']:.0f}% होते. बांगलादेशशी व्यापार आगरतळ्याजवळील अखौरा भू-बंदरातून होतो.\n\nपीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता (राष्ट्रीय {ui['2025']}%), आणि 15 वर्षांवरील {lf['female']}% स्त्रिया श्रमशक्तीत होत्या, तर राष्ट्रीय पातळीवर {lfi['female']}%."),
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
        *plfs_facts("TR", NAME),
    ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    *gdp_series(mo, "FY2011-12 to FY2024-25"),
    sect,
    plfs_series("TR", NAME),
    gaps("g", [
        (L("Rubber area and production", "रबर क्षेत्र और उत्पादन", "रबर क्षेत्र व उत्पादन"), "india-gov", "Rubber Board of India."),
        (L("Natural gas production", "प्राकृतिक गैस उत्पादन", "नैसर्गिक वायू उत्पादन"), "india-gov", "Ministry of Petroleum and Natural Gas / ONGC."),
    ]),
])

module(R, "government", [
    prose("p1", L(
        "Tripura has a unicameral, 60-member Legislative Assembly in Agartala, 20 of whose seats are reserved for Scheduled Tribes. The Tripura Tribal Areas Autonomous District Council (TTAADC), with its headquarters at Khumulwng, governs the tribal areas under the Sixth Schedule. The State elects 2 members to the Lok Sabha (Tripura West and Tripura East) and 1 to the Rajya Sabha.\n\nThe BJP and its ally won the 2023 Assembly election, and Manik Saha, Chief Minister since May 2022, was sworn in for a second term on 8 March 2023. N. Indrasena Reddy has been Governor since October 2023. Speaker Biswa Bandhu Sen died in December 2025; the current Speaker will be shown once confirmed from the Assembly. The next Assembly election is due by early 2028.",
        "त्रिपुरा में अगरतला में 60 सदस्यों वाली एकसदनीय विधानसभा है, जिसकी 20 सीटें अनुसूचित जनजातियों के लिए आरक्षित हैं। खुमुलवंग में मुख्यालय वाली त्रिपुरा जनजातीय क्षेत्र स्वायत्त ज़िला परिषद (टीटीएएडीसी) छठी अनुसूची के तहत जनजातीय क्षेत्रों का शासन करती है। राज्य से लोकसभा के 2 (त्रिपुरा पश्चिम और त्रिपुरा पूर्व) और राज्यसभा का 1 सदस्य चुना जाता है।\n\n2023 का विधानसभा चुनाव भाजपा और उसके सहयोगी ने जीता, और मई 2022 से मुख्यमंत्री माणिक साहा ने 8 मार्च 2023 को दूसरे कार्यकाल की शपथ ली। एन. इंद्रसेना रेड्डी अक्टूबर 2023 से राज्यपाल हैं। अध्यक्ष बिस्व बंधु सेन का दिसंबर 2025 में निधन हुआ; वर्तमान अध्यक्ष का नाम विधानसभा से पुष्टि होने पर दिखाया जाएगा। अगला विधानसभा चुनाव 2028 की शुरुआत तक होना है।",
        "त्रिपुरामध्ये आगरतळा येथे 60 सदस्यांची एकसदनी विधानसभा आहे, जिच्या 20 जागा अनुसूचित जमातींसाठी राखीव आहेत. खुमुलवंग येथे मुख्यालय असलेली त्रिपुरा आदिवासी क्षेत्र स्वायत्त जिल्हा परिषद (टीटीएएडीसी) सहाव्या अनुसूचीखाली आदिवासी भागांचा कारभार पाहते. राज्यातून लोकसभेवर 2 (त्रिपुरा पश्चिम व त्रिपुरा पूर्व) आणि राज्यसभेवर 1 सदस्य निवडला जातो.\n\n2023 ची विधानसभा निवडणूक भाजप व त्याच्या मित्रपक्षाने जिंकली, आणि मे 2022 पासून मुख्यमंत्री असलेले माणिक साहा यांनी 8 मार्च 2023 रोजी दुसऱ्या कारकिर्दीची शपथ घेतली. एन. इंद्रसेना रेड्डी ऑक्टोबर 2023 पासून राज्यपाल आहेत. अध्यक्ष बिस्व बंधू सेन यांचे डिसेंबर 2025 मध्ये निधन झाले; सध्याच्या अध्यक्षांचे नाव विधानसभेकडून खात्री झाल्यावर दाखवले जाईल. पुढील विधानसभा निवडणूक 2028 च्या सुरुवातीपर्यंत होणे अपेक्षित आहे."),
        sources=["the-week", "sentinel-assam", "deccan-herald"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    lst("links", [
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("portal", "Government of Tripura", "त्रिपुरा सरकार", "त्रिपुरा शासन", url="https://tripura.gov.in", src="india-gov"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Current Speaker — official source", "वर्तमान अध्यक्ष — आधिकारिक स्रोत", "सध्याचे अध्यक्ष — अधिकृत स्रोत"), "india-gov", "Tripura Legislative Assembly bulletin."),
        (L("2023 Assembly election — party-wise result", "2023 विधानसभा चुनाव — दलवार परिणाम", "2023 विधानसभा निवडणूक — पक्षनिहाय निकाल"), "eci", "ECI statistical report for Tripura 2023."),
    ]),
])

module(R, "projects", [
    prose("p1", L(
        "Major works include the Agartala–Akhaura railway link to Bangladesh, the new terminal at Maharaja Bir Bikram Airport and the Maitri Setu bridge over the Feni river at Sabroom, which links Tripura to Chittagong port in Bangladesh. They will be added as cards once their cost and status are confirmed from official sources.",
        "प्रमुख कार्यों में बांग्लादेश तक अगरतला–अखौरा रेल लिंक, महाराजा बीर बिक्रम हवाई अड्डे का नया टर्मिनल और सबरूम में फेनी नदी पर मैत्री सेतु शामिल हैं, जो त्रिपुरा को बांग्लादेश के चटगाँव बंदरगाह से जोड़ता है। आधिकारिक स्रोतों से लागत और स्थिति की पुष्टि होने पर इन्हें कार्ड के रूप में जोड़ा जाएगा।",
        "प्रमुख कामांत बांगलादेशपर्यंत आगरतळा–अखौरा रेल्वे जोड, महाराजा बीर बिक्रम विमानतळाचे नवे टर्मिनल आणि सबरूम येथे फेनी नदीवरील मैत्री सेतू यांचा समावेश आहे, जो त्रिपुराला बांगलादेशातील चितगाव बंदराशी जोडतो. अधिकृत स्रोतांतून खर्च व स्थितीची खात्री झाल्यावर त्यांची कार्डे जोडली जातील."),
        conf="Editorial"),
    {"type": "projects", "id": "projects"},
    gaps("g", [
        (L("Agartala–Akhaura rail link — official status", "अगरतला–अखौरा रेल लिंक — आधिकारिक स्थिति", "आगरतळा–अखौरा रेल्वे जोड — अधिकृत स्थिती"), "railways", "Ministry of Railways / MEA."),
        (L("Maitri Setu — official inauguration record", "मैत्री सेतु — आधिकारिक उद्घाटन अभिलेख", "मैत्री सेतू — अधिकृत उद्घाटन नोंद"), "pib", "PIB / PMO release (March 2021)."),
    ]),
])

module(R, "transport", [
    prose("p1", L(
        "NH-8 links Tripura through Assam to the rest of India, and broad-gauge railways reach Agartala and run south to Sabroom on the Bangladesh border. Maharaja Bir Bikram Airport at Agartala has flights to Kolkata, Guwahati, Delhi and other cities. Bus and border links connect Agartala with Dhaka and Chittagong.",
        "एनएच-8 त्रिपुरा को असम होकर शेष भारत से जोड़ता है, और बड़ी लाइन की रेल अगरतला तक पहुँचती है और दक्षिण में बांग्लादेश सीमा पर सबरूम तक जाती है। अगरतला के महाराजा बीर बिक्रम हवाई अड्डे से कोलकाता, गुवाहाटी, दिल्ली और अन्य नगरों की उड़ानें हैं। बस और सीमा संपर्क अगरतला को ढाका और चटगाँव से जोड़ते हैं।",
        "एनएच-8 त्रिपुराला आसाममार्गे उर्वरित भारताशी जोडतो, आणि ब्रॉडगेज रेल्वे आगरतळ्यापर्यंत पोहोचते व दक्षिणेला बांगलादेश सीमेवरील सबरूमपर्यंत जाते. आगरतळ्यातील महाराजा बीर बिक्रम विमानतळावरून कोलकाता, गुवाहाटी, दिल्ली व इतर शहरांसाठी उड्डाणे आहेत. बस व सीमा संपर्क आगरतळ्याला ढाका व चितगावशी जोडतात."),
        conf="Editorial"),
    lst("airports", [it3("ixa", "Maharaja Bir Bikram Airport, Agartala", "महाराजा बीर बिक्रम हवाई अड्डा, अगरतला", "महाराजा बीर बिक्रम विमानतळ, आगरतळा", m=("IXA", "IXA", "IXA"))], layout="chips", title=L("Airports", "हवाई अड्डे", "विमानतळ"), conf="Editorial"),
])

module(R, "energy", [
    prose("p1", L(
        "Natural gas makes Tripura a power-surplus State in normal years. ONGC Tripura Power Company's combined-cycle plant at Palatana, NEEPCO's Agartala and Monarchak stations and the State's own gas plants supply the grid, and the Gumti hydro project at Dumbur adds a little hydropower. Tripura sells power to Bangladesh and other north-eastern States.",
        "सामान्य वर्षों में प्राकृतिक गैस त्रिपुरा को बिजली अधिशेष वाला राज्य बनाती है। पलाटाना में ओएनजीसी त्रिपुरा पावर कंपनी का संयुक्त-चक्र संयंत्र, नीपको के अगरतला और मोनारचक केंद्र और राज्य के अपने गैस संयंत्र ग्रिड को बिजली देते हैं, और डुम्बुर की गुमती जलविद्युत परियोजना थोड़ी जलविद्युत जोड़ती है। त्रिपुरा बांग्लादेश और अन्य पूर्वोत्तर राज्यों को बिजली बेचता है।",
        "सामान्य वर्षांत नैसर्गिक वायूमुळे त्रिपुरा वीज-अतिरिक्त राज्य असते. पलाटाना येथील ओएनजीसी त्रिपुरा पॉवर कंपनीचा संयुक्त-चक्र प्रकल्प, नीपकोची आगरतळा व मोनारचक केंद्रे आणि राज्याचे स्वतःचे वायू प्रकल्प ग्रिडला वीज पुरवतात, आणि डुम्बुरचा गुमती जलविद्युत प्रकल्प थोडी जलविद्युत जोडतो. त्रिपुरा बांगलादेश व इतर ईशान्य राज्यांना वीज विकते."),
        conf="Editorial"),
    gaps("g", [(L("Installed capacity and exports to Bangladesh", "स्थापित क्षमता और बांग्लादेश को निर्यात", "स्थापित क्षमता व बांगलादेशला निर्यात"), "cea", "CEA / Tripura State Electricity Corporation.")]),
])

module(R, "digital", [
    prose("p1", L(
        "A submarine-cable internet link through Cox's Bazar in Bangladesh, opened in 2016, and the national optical fibre network improved bandwidth in the State. Mobile networks cover most towns and villages. NIT Agartala, Tripura University and IIIT Agartala train engineers and computer scientists.",
        "बांग्लादेश के कॉक्स बाज़ार होकर 2016 में खुले समुद्री केबल इंटरनेट लिंक और राष्ट्रीय ऑप्टिकल फ़ाइबर नेटवर्क ने राज्य में बैंडविड्थ सुधारी। मोबाइल नेटवर्क अधिकांश नगरों और गाँवों को कवर करते हैं। एनआईटी अगरतला, त्रिपुरा विश्वविद्यालय और आईआईआईटी अगरतला इंजीनियरों और कंप्यूटर वैज्ञानिकों को प्रशिक्षित करते हैं।",
        "बांगलादेशातील कॉक्स बाजारमार्गे 2016 मध्ये सुरू झालेल्या सागरी केबल इंटरनेट जोडणीमुळे व राष्ट्रीय ऑप्टिकल फायबर जाळ्यामुळे राज्यातील बँडविड्थ सुधारली. मोबाइल जाळे बहुतेक शहरे व गावांना व्यापते. एनआयटी आगरतळा, त्रिपुरा विद्यापीठ व आयआयआयटी आगरतळा अभियंते व संगणक शास्त्रज्ञ घडवतात."),
        conf="Editorial"),
    gaps("g", [(L("Cox's Bazar bandwidth link — official record", "कॉक्स बाज़ार बैंडविड्थ लिंक — आधिकारिक अभिलेख", "कॉक्स बाजार बँडविड्थ जोड — अधिकृत नोंद"), "india-gov", "BSNL / Department of Telecommunications.")]),
])

ef, es = aishe_block("TR", NAME)
gm, gf = AP["aishe_ger_mf_2021_22"]["TR"]; ger = AP["aishe_ger"]["TR"]
module(R, "education", [
    prose("p1", L(
        f"Literacy in Tripura was 87.2% at the 2011 Census. The higher-education gross enrolment ratio (ages 18–23) was {ger['2021-22']}% in 2021-22 in AISHE, below the national 28.4%, with men at {gm}% and women at {gf}%. Tripura University, a central university at Suryamaninagar, NIT Agartala, IIIT Agartala, Maharaja Bir Bikram University and two medical colleges are the main institutions.",
        f"2011 की जनगणना में त्रिपुरा की साक्षरता 87.2% थी। एआईएसएचई के अनुसार 2021-22 में उच्च शिक्षा सकल नामांकन अनुपात (18–23 आयु) {ger['2021-22']}% था, जो राष्ट्रीय 28.4% से कम है, पुरुष {gm}% और महिलाएँ {gf}%। सूर्यमणिनगर का त्रिपुरा विश्वविद्यालय (केंद्रीय), एनआईटी अगरतला, आईआईआईटी अगरतला, महाराजा बीर बिक्रम विश्वविद्यालय और दो मेडिकल कॉलेज मुख्य संस्थान हैं।",
        f"2011 च्या जनगणनेत त्रिपुराची साक्षरता 87.2% होती. एआयएसएचईनुसार 2021-22 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर (18–23 वय) {ger['2021-22']}% होते, राष्ट्रीय 28.4% पेक्षा कमी, पुरुष {gm}% व स्त्रिया {gf}%. सूर्यमणिनगर येथील त्रिपुरा विद्यापीठ (केंद्रीय), एनआयटी आगरतळा, आयआयआयटी आगरतळा, महाराजा बीर बिक्रम विद्यापीठ व दोन वैद्यकीय महाविद्यालये या मुख्य संस्था आहेत."),
        sources=["aishe", "es-india"], conf="Official"),
    ef, es,
    gaps("g", [(L("Schools, teachers and pupil–teacher ratio", "स्कूल, शिक्षक और छात्र–शिक्षक अनुपात", "शाळा, शिक्षक व विद्यार्थी–शिक्षक गुणोत्तर"), "udise", "UDISE+ latest year.")]),
])

n = NF["TR"]; s = C["srs"]["TR"]
module(R, "health", [
    prose("p1", L(
        f"Tripura's infant mortality rate was {s[5]:.0f} per 1,000 live births in 2020 in the Sample Registration System, down from {s[4]} in 2010 (national 28). The birth rate was {s[1]} and the death rate {s[3]} per 1,000. In NFHS-5, {n['institutional_N5']:.1f}% of births took place in health facilities, but child nutrition worsened: {n['stunted'][1]:.1f}% of children under five were stunted, up from {n['stunted'][0]}% in NFHS-4, {n['wasted'][1]:.1f}% wasted and {n['underweight'][1]:.1f}% underweight. Agartala Government Medical College with the G. B. Pant Hospital is the main referral centre.",
        f"नमूना पंजीकरण प्रणाली में 2020 में त्रिपुरा की शिशु मृत्यु दर प्रति 1,000 जीवित जन्म पर {s[5]:.0f} थी, जो 2010 के {s[4]} से कम है (राष्ट्रीय 28)। जन्म दर प्रति 1,000 पर {s[1]} और मृत्यु दर {s[3]} थी। एनएफ़एचएस-5 में {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, पर बाल पोषण बिगड़ा: पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने थे, जो एनएफ़एचएस-4 के {n['stunted'][0]}% से अधिक है, {n['wasted'][1]:.1f}% दुबले और {n['underweight'][1]:.1f}% कम वज़न के। जी. बी. पंत अस्पताल सहित अगरतला गवर्नमेंट मेडिकल कॉलेज मुख्य रेफ़रल केंद्र है।",
        f"नमुना नोंदणी पद्धतीनुसार 2020 मध्ये त्रिपुराचा अर्भक मृत्युदर दर 1,000 जिवंत जन्मांमागे {s[5]:.0f} होता, 2010 मधील {s[4]} वरून कमी (राष्ट्रीय 28). जन्मदर दर 1,000 मागे {s[1]} व मृत्युदर {s[3]} होता. एनएफएचएस-5 मध्ये {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, पण बालपोषण बिघडले: पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी होती, एनएफएचएस-4 मधील {n['stunted'][0]}% पेक्षा जास्त, {n['wasted'][1]:.1f}% कृश व {n['underweight'][1]:.1f}% कमी वजनाची. जी. बी. पंत रुग्णालयासह आगरतळा शासकीय वैद्यकीय महाविद्यालय हे मुख्य संदर्भ केंद्र आहे."),
        sources=["srs", "nfhs"], conf="Official"),
    facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)")),
    facts("nfhs", nfhs_facts("TR"), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)")),
])
print("tr mod2 ok")
