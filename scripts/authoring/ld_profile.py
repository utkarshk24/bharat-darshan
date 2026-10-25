"""Lakshadweep — Phase 3 profile (core + all modules). Run with BD_TODAY=2026-10-25."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from ut_kit import *

R = "IN-LD"
NAME = L("Lakshadweep", "लक्षद्वीप", "लक्षद्वीप")
ADM = "https://lakshadweep.gov.in/about-lakshadweep/profile-administrator/"
SOFC = "https://www.pmindia.gov.in/?p=16351284"

r = read("regions/IN-LD.json"); m = r["metrics"]
census_metrics(m, "LD", 30, "Males 33,123; females 31,350.", 2149, 90.2,
               "Computed from ISFR 2023 forest cover 27.06 km² ÷ geographical area 30 km². Most of it is coconut-dominated tree cover classed as forest by ISFR.")
m["gsdpCurrent"] = todo("₹ crore", "FY2024-25", "fy", "mospi", "MoSPI's state series returned no rows for Lakshadweep.", base=CUR)
m["perCapitaNsdpCurrent"] = todo("₹", "FY2024-25", "fy", "mospi", "Not published by MoSPI for Lakshadweep.", base=CUR)
r["officialPortal"] = "https://lakshadweep.gov.in"
r["symbols"] = {"animal": sym("Butterfly fish", "तितली मछली", "फुलपाखरू मासा", "Chaetodon spp."),
                "bird": sym("Sooty tern", "सूटी टर्न", "सुटी टर्न", "Onychoprion fuscatus"),
                "tree": sym("Breadfruit", "ब्रेडफ़्रूट", "नीरफणस", "Artocarpus altilis")}
r["government"] = {
    "headOfState": office("administrator", L("Praful Khoda Patel", "प्रफुल्ल खोड़ा पटेल", "प्रफुल्ल खोडा पटेल"), None, "2020-12-05", "ld-gov", ADM, "https://lakshadweep.gov.in", conf="Official",
                          note="Administrator of Lakshadweep since 5 December 2020 (Lakshadweep Administration profile page); also Administrator of Dadra and Nagar Haveli and Daman and Diu."),
    "headOfGovernment": None, "others": [],
}
r["projects"] = [
    proj("kli-sofc", L("Kochi–Lakshadweep Islands Submarine Optical Fibre Connection (KLI-SOFC)", "कोच्चि–लक्षद्वीप द्वीप समुद्री ऑप्टिकल फ़ाइबर कनेक्शन (केएलआई-एसओएफ़सी)", "कोची–लक्षद्वीप बेटे सागरी ऑप्टिकल फायबर जोडणी (केएलआय-एसओएफसी)"),
         L("A submarine optical-fibre cable from Kochi that connected Lakshadweep by fibre for the first time, inaugurated by the Prime Minister at Kavaratti on 3 January 2024. It raised internet capacity more than a hundredfold, from 1.7 Gbps to 200 Gbps, with benefits for telemedicine, e-governance and education. It was one of projects worth more than ₹1,150 crore launched that day.",
           "कोच्चि से समुद्री ऑप्टिकल फ़ाइबर केबल, जिसने पहली बार लक्षद्वीप को फ़ाइबर से जोड़ा; प्रधानमंत्री ने 3 जनवरी 2024 को कवरत्ती में इसका उद्घाटन किया। इससे इंटरनेट क्षमता 1.7 जीबीपीएस से 200 जीबीपीएस, यानी सौ गुना से अधिक बढ़ी, जिससे टेलीमेडिसिन, ई-शासन और शिक्षा को लाभ हुआ। यह उस दिन शुरू की गई ₹1,150 करोड़ से अधिक की परियोजनाओं में से एक थी।",
           "कोचीहून सागरी ऑप्टिकल फायबर केबल, जिने प्रथमच लक्षद्वीपला फायबरने जोडले; पंतप्रधानांनी 3 जानेवारी 2024 रोजी कवरत्ती येथे तिचे उद्घाटन केले. यामुळे इंटरनेट क्षमता 1.7 जीबीपीएसवरून 200 जीबीपीएस, म्हणजे शंभरपटीहून अधिक वाढली, ज्याचा टेलिमेडिसिन, ई-शासन व शिक्षणाला लाभ झाला. त्या दिवशी सुरू झालेल्या ₹1,150 कोटींहून अधिक किमतीच्या प्रकल्पांपैकी हा एक होता."),
         "telecom", "BSNL / Department of Telecommunications", None, None, None, None, "3 January 2024", "Completed", "pmindia", SOFC),
]
r["giProducts"] = []
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-LD.json", r)
m = r["metrics"]

module(R, "overview", [
    prose("intro", L(
        "Lakshadweep, 'a hundred thousand islands', is a Union Territory of only about 30 km² of land: a group of coral atolls, islands and reefs in the Arabian Sea, about 200–440 km off the Kerala coast. Ten islands are inhabited, among them Kavaratti, the capital, Agatti, Amini, Andrott, Kalpeni and Minicoy. The islands are low and flat, ringed by white sand and turquoise lagoons, and their people live from fishing, coconuts and government work.",
        "लक्षद्वीप, 'एक लाख द्वीप', केवल लगभग 30 वर्ग किमी भूमि वाला केंद्र शासित प्रदेश है: अरब सागर में केरल तट से लगभग 200–440 किमी दूर प्रवाल एटॉल, द्वीपों और भित्तियों का समूह। दस द्वीप बसे हुए हैं, जिनमें राजधानी कवरत्ती, अगत्ती, अमीनी, आंद्रोत, कल्पेनी और मिनिकॉय शामिल हैं। द्वीप नीचे और समतल हैं, सफ़ेद रेत और फ़िरोज़ी लैगून से घिरे, और इनके लोग मछली पकड़ने, नारियल और सरकारी काम से जीविका चलाते हैं।",
        "लक्षद्वीप, 'लाख बेटे', हा केवळ सुमारे 30 चौ.किमी जमिनीचा केंद्रशासित प्रदेश आहे: अरबी समुद्रात केरळ किनाऱ्यापासून सुमारे 200–440 किमी अंतरावरील प्रवाळ कंकणद्वीपे, बेटे व भित्तींचा समूह. दहा बेटांवर वस्ती आहे, ज्यांत राजधानी कवरत्ती, अगत्ती, अमिनी, आंद्रोत, कल्पेनी व मिनिकॉय आहेत. बेटे सखल व सपाट आहेत, पांढऱ्या वाळूने व नीलवर्णी खाजणांनी वेढलेली, आणि तेथील लोक मासेमारी, नारळ व सरकारी कामावर उपजीविका करतात."),
        sources=["census", "fsi"], conf="Editorial"),
    admin_table([
        row("Status", "दर्जा", "दर्जा", ("Union Territory without a legislature (since 1 November 1956)", "बिना विधानसभा वाला केंद्र शासित प्रदेश (1 नवंबर 1956 से)", "विधिमंडळ नसलेला केंद्रशासित प्रदेश (1 नोव्हेंबर 1956 पासून)")),
        row("Districts", "ज़िले", "जिल्हे", ("1 (Lakshadweep)", "1 (लक्षद्वीप)", "1 (लक्षद्वीप)")),
        row("Capital", "राजधानी", "राजधानी", ("Kavaratti", "कवरत्ती", "कवरत्ती")),
        row("High Court", "उच्च न्यायालय", "उच्च न्यायालय", ("High Court of Kerala", "केरल उच्च न्यायालय", "केरळ उच्च न्यायालय")),
        row("Vehicle registration code", "वाहन पंजीकरण कोड", "वाहन नोंदणी संकेतांक", "LD"),
        row("Time zone", "समय क्षेत्र", "प्रमाणवेळ", "IST (UTC+05:30)"),
    ]),
    gaps("g", [(L("Official count of islands", "द्वीपों की आधिकारिक संख्या", "बेटांची अधिकृत संख्या"), "ld-gov", "Lakshadweep Administration.")]),
])

module(R, "geography", [
    prose("p1", L(
        "The islands sit on the Laccadive–Chagos ridge, an undersea mountain chain, and are built of coral, rising only a few metres above the sea. Most are long, narrow islands on the eastern side of an atoll, with a lagoon to the west. Minicoy, the southernmost, is separated from the rest by the Nine Degree Channel and lies close to the Maldives. The total land area is only about 30 km², but the lagoons and territorial waters are many times larger.",
        "द्वीप समुद्र के नीचे की पर्वत शृंखला, लक्षद्वीप–चागोस कटक, पर बसे हैं और प्रवाल से बने हैं, जो समुद्र से कुछ ही मीटर ऊपर उठते हैं। अधिकांश एटॉल के पूर्वी किनारे पर लंबे, संकरे द्वीप हैं, पश्चिम में लैगून के साथ। सबसे दक्षिणी मिनिकॉय नौ डिग्री चैनल से बाकी द्वीपों से अलग है और मालदीव के निकट है। कुल भूमि केवल लगभग 30 वर्ग किमी है, पर लैगून और प्रादेशिक जल इससे कई गुना बड़े हैं।",
        "बेटे समुद्राखालील पर्वतरांग, लक्षद्वीप–चागोस कटक, यावर वसलेली असून प्रवाळाची बनलेली आहेत, समुद्रापासून काही मीटरच उंच. बहुतेक बेटे कंकणद्वीपाच्या पूर्व बाजूस लांब, अरुंद असून पश्चिमेला खाजण आहे. सर्वांत दक्षिणेकडील मिनिकॉय नऊ अंश खाडीने इतर बेटांपासून वेगळे असून मालदीवजवळ आहे. एकूण जमीन फक्त सुमारे 30 चौ.किमी आहे, पण खाजणे व प्रादेशिक जल याहून अनेक पटींनी मोठे आहे."),
        conf="Editorial"),
    facts("f", [fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), m["area"], "number", national=IND["area"])]),
])

module(R, "climate", [
    prose("p1", L(
        "The climate is warm and humid all year, between about 25 and 32 °C. The south-west monsoon from late May to September brings rough seas, when most boat and ship services are reduced; October to April is calm and dry and is the visiting season.",
        "जलवायु पूरे वर्ष गर्म और आर्द्र रहती है, लगभग 25 से 32 °C के बीच। मई के अंत से सितंबर तक दक्षिण-पश्चिम मानसून समुद्र को अशांत करता है, जब अधिकांश नौका और जहाज़ सेवाएँ कम हो जाती हैं; अक्टूबर से अप्रैल शांत और सूखा रहता है और घूमने का मौसम है।",
        "हवामान वर्षभर उष्ण व दमट असते, सुमारे 25 ते 32 °C. मेच्या अखेरीपासून सप्टेंबरपर्यंत नैर्ऋत्य मान्सून समुद्र खवळवतो, तेव्हा बहुतेक नौका व जहाज सेवा कमी होतात; ऑक्टोबर ते एप्रिल शांत व कोरडा असतो आणि भेटीचा हंगाम असतो."),
        conf="Editorial"),
    {"type": "weather", "id": "live", "places": [
        {"name": L("Kavaratti", "कवरत्ती", "कवरत्ती"), "lat": 10.5669, "lon": 72.6420},
        {"name": L("Minicoy", "मिनिकॉय", "मिनिकॉय"), "lat": 8.2833, "lon": 73.0500},
    ]},
])

module(R, "vibe", [
    prose("p1", L(
        "Island life is quiet and close-knit: houses of coral stone among coconut palms, small mosques, children playing in the lagoon and fishing boats returning with tuna. Alcohol is largely prohibited outside designated tourist resorts, and visitors need permits.",
        "द्वीपों का जीवन शांत और घनिष्ठ है: नारियल के पेड़ों के बीच प्रवाल पत्थर के घर, छोटी मस्जिदें, लैगून में खेलते बच्चे और टूना लेकर लौटती नावें। निर्धारित पर्यटक रिसॉर्ट के बाहर शराब पर बड़े पैमाने पर रोक है, और पर्यटकों को परमिट चाहिए।",
        "बेटांवरील जीवन शांत व घट्ट विणलेले आहे: नारळीच्या झाडांमध्ये प्रवाळ दगडांची घरे, लहान मशिदी, खाजणात खेळणारी मुले व टुना घेऊन परतणाऱ्या होड्या. ठरावीक पर्यटक रिसॉर्टबाहेर मद्यावर मोठ्या प्रमाणावर बंदी आहे, आणि पर्यटकांना परवाने लागतात."),
        conf="Editorial"),
])

module(R, "people", [
    prose("p1", L(
        "Lakshadweep had 64,473 people at the 2011 Census, about 2,149 per km² of land. The sex ratio was 946 women per 1,000 men, but the child sex ratio fell sharply from 959 in 2001 to 911. Literacy was 91.8%. Scheduled Tribes made up 94.8% of the population; nearly all islanders are Muslim. Malayalam and its local form Jeseri are spoken on most islands, and Mahl, close to the Dhivehi of the Maldives, on Minicoy. Society is traditionally matrilineal.",
        "2011 की जनगणना में लक्षद्वीप की जनसंख्या 64,473 थी, प्रति वर्ग किमी भूमि लगभग 2,149। लिंगानुपात प्रति 1,000 पुरुषों पर 946 महिलाएँ था, पर शिशु लिंगानुपात 2001 के 959 से तेज़ी से घटकर 911 हो गया। साक्षरता 91.8% थी। अनुसूचित जनजातियाँ जनसंख्या का 94.8% थीं; लगभग सभी द्वीपवासी मुसलमान हैं। अधिकांश द्वीपों पर मलयालम और उसका स्थानीय रूप जेसरी, और मिनिकॉय पर मालदीव की धिवेही से मिलती-जुलती महल बोली जाती है। समाज परंपरागत रूप से मातृवंशीय है।",
        "2011 च्या जनगणनेनुसार लक्षद्वीपची लोकसंख्या 64,473 होती, प्रति चौ.किमी जमिनीवर सुमारे 2,149. दर 1,000 पुरुषांमागे 946 स्त्रिया होत्या, पण बाल लिंग गुणोत्तर 2001 मधील 959 वरून झपाट्याने घटून 911 झाले. साक्षरता 91.8% होती. अनुसूचित जमाती लोकसंख्येच्या 94.8% होत्या; जवळपास सर्व बेटवासी मुस्लिम आहेत. बहुतेक बेटांवर मल्याळम व तिचे स्थानिक रूप जेसरी, आणि मिनिकॉयवर मालदीवच्या धिवेहीशी जवळची महल बोलली जाते. समाज परंपरेने मातृवंशीय आहे."),
        sources=["census", "es-india", "dl-planning", "pib"], conf="Official"),
    facts("f", people_facts("LD", m, "LD", fact("st", L("Scheduled Tribes, share of population", "अनुसूचित जनजातियाँ, जनसंख्या में हिस्सा", "अनुसूचित जमाती, लोकसंख्येतील वाटा"),
        dp(94.8, "%", "2011", "census", "dl-planning", SCST, note="Delhi Planning Department, table 17.2, citing Census 2011: 0.61 lakh people. No Scheduled Castes are notified for the UT."), "percent")),
        title=L("Census 2011 at a glance", "जनगणना 2011 एक नज़र में", "जनगणना 2011 दृष्टिक्षेपात")),
])

module(R, "history", [
    prose("p1", L(
        "The islands were settled by seafarers from the Kerala coast, and by tradition Islam was brought in the 7th century by the Arab preacher Ubaidullah, whose tomb is at Andrott. The northern Amindivi islands came under Tipu Sultan in the late 18th century and then the British, while the southern islands belonged to the Arakkal family of Kannur until the British took them over in 1908. After independence they were made the Union Territory of the Laccadive, Minicoy and Amindivi Islands on 1 November 1956, renamed Lakshadweep in 1973. The capital moved from Kozhikode to Kavaratti in 1964.",
        "द्वीपों को केरल तट के नाविकों ने बसाया, और परंपरा के अनुसार 7वीं सदी में अरब प्रचारक उबैदुल्लाह इस्लाम लाए, जिनकी मज़ार आंद्रोत में है। उत्तरी अमीनदीवी द्वीप 18वीं सदी के अंत में टीपू सुल्तान और फिर अंग्रेज़ों के अधीन आए, जबकि दक्षिणी द्वीप कन्नूर के अरक्कल परिवार के थे, जब तक 1908 में अंग्रेज़ों ने उन्हें अपने अधीन नहीं ले लिया। स्वतंत्रता के बाद 1 नवंबर 1956 को इन्हें लक्कदीव, मिनिकॉय और अमीनदीवी द्वीप केंद्र शासित प्रदेश बनाया गया, जिसका नाम 1973 में लक्षद्वीप रखा गया। 1964 में राजधानी कोझिकोड से कवरत्ती आई।",
        "बेटांवर केरळ किनाऱ्यावरील दर्यावर्दींनी वस्ती केली, आणि परंपरेनुसार सातव्या शतकात अरब धर्मप्रचारक उबैदुल्लाह यांनी इस्लाम आणला, ज्यांची दर्गा आंद्रोत येथे आहे. उत्तरेकडील अमिनदीवी बेटे अठराव्या शतकाच्या अखेरीस टिपू सुलतान व नंतर ब्रिटिशांच्या ताब्यात आली, तर दक्षिणेकडील बेटे कन्नूरच्या अरक्कल घराण्याकडे होती, 1908 मध्ये ब्रिटिशांनी ती ताब्यात घेईपर्यंत. स्वातंत्र्यानंतर 1 नोव्हेंबर 1956 रोजी त्यांना लक्कदीव, मिनिकॉय व अमिनदीवी बेटे केंद्रशासित प्रदेश बनवले गेले, ज्याचे 1973 मध्ये लक्षद्वीप नामकरण झाले. 1964 मध्ये राजधानी कोझिकोडहून कवरत्तीला आली."),
        conf="Editorial"),
    timeline([
        ev("ut", 1956, L("1 November 1956", "1 नवंबर 1956", "1 नोव्हेंबर 1956"), L("Union Territory formed", "केंद्र शासित प्रदेश बना", "केंद्रशासित प्रदेशाची निर्मिती")),
        ev("kavaratti", 1964, L("1964", "1964", "1964"), L("Capital moves to Kavaratti", "राजधानी कवरत्ती आई", "राजधानी कवरत्तीला")),
        ev("name", 1973, L("1973", "1973", "1973"), L("Renamed Lakshadweep", "नाम लक्षद्वीप रखा गया", "लक्षद्वीप नामकरण")),
        ev("sofc", 2024, L("3 January 2024", "3 जनवरी 2024", "3 जानेवारी 2024"), L("Submarine fibre link to Kochi", "कोच्चि तक समुद्री फ़ाइबर लिंक", "कोचीपर्यंत सागरी फायबर जोड")),
    ]),
])

module(R, "culture", [
    prose("p1", L(
        "Islander culture blends Malabar Muslim traditions with seafaring life. Kolkali (stick dance), Parichakali (shield-and-sword dance) and Oppana are performed at weddings and festivals, and Eid and the Prophet's birthday are the main celebrations. Minicoy has its own Lava dance and boat-race traditions. Coconut is at the heart of the cuisine, along with tuna, often cured as masmin.",
        "द्वीपों की संस्कृति मालाबार मुस्लिम परंपराओं को समुद्री जीवन से मिलाती है। कोलकली (डंडा नृत्य), परिचाकली (ढाल-तलवार नृत्य) और ओप्पना विवाहों और त्योहारों पर किए जाते हैं, और ईद और पैगंबर का जन्मदिन मुख्य उत्सव हैं। मिनिकॉय की अपनी लावा नृत्य और नौका दौड़ परंपराएँ हैं। व्यंजनों के केंद्र में नारियल है, साथ में टूना, जिसे अक्सर मास्मिन के रूप में सुखाया जाता है।",
        "बेटांची संस्कृती मलबार मुस्लिम परंपरांना सागरी जीवनाशी जोडते. कोलकळी (काठी नृत्य), परिचाकळी (ढाल-तलवार नृत्य) व ओप्पना विवाह व सणांना सादर होतात, आणि ईद व पैगंबर जयंती हे मुख्य उत्सव आहेत. मिनिकॉयच्या स्वतःच्या लावा नृत्य व नौकाशर्यत परंपरा आहेत. खाद्यसंस्कृतीच्या केंद्रस्थानी नारळ आहे, सोबत टुना, जो अनेकदा मास्मिन म्हणून सुकवला जातो."),
        conf="Editorial"),
])

ur = AP["plfs_ur_15plus_psss"]["LD"]; lf = AP["plfs_lfpr_2025"]["LD"]
module(R, "economy", [
    prose("p1", L(
        f"Fishing — especially pole-and-line tuna fishing — coconut and coir, and government employment are the mainstays, with tourism small and tightly controlled. MoSPI does not publish a GSDP series for Lakshadweep. The PLFS unemployment rate was {ur['2025']}% in 2025, down from {ur['2022']}% in 2022, and only {lf['female']}% of women aged 15+ were in the labour force.",
        f"मछली पकड़ना — विशेषकर पोल-एंड-लाइन टूना — नारियल और कॉयर, और सरकारी रोज़गार मुख्य आधार हैं, जबकि पर्यटन छोटा और कड़ाई से नियंत्रित है। मोस्पी लक्षद्वीप के लिए जीएसडीपी शृंखला प्रकाशित नहीं करता। पीएलएफ़एस बेरोज़गारी दर 2025 में {ur['2025']}% थी, जो 2022 के {ur['2022']}% से कम है, और 15+ आयु की केवल {lf['female']}% महिलाएँ श्रम बल में थीं।",
        f"मासेमारी — विशेषतः पोल-अँड-लाइन टुना — नारळ व काथ्या, आणि सरकारी रोजगार हे मुख्य आधार आहेत, तर पर्यटन लहान व काटेकोर नियंत्रित आहे. मोस्पी लक्षद्वीपसाठी जीएसडीपी मालिका प्रसिद्ध करत नाही. पीएलएफएस बेरोजगारी दर 2025 मध्ये {ur['2025']}% होता, 2022 मधील {ur['2022']}% वरून कमी, आणि 15+ वयाच्या केवळ {lf['female']}% स्त्रिया श्रमशक्तीत होत्या."),
        sources=["plfs"], conf="Official"),
    facts("f", plfs_facts("LD", NAME), title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
    plfs_series("LD", NAME),
    gaps("g", [(L("GSDP and per capita income", "जीएसडीपी और प्रति व्यक्ति आय", "जीएसडीपी व दरडोई उत्पन्न"), "mospi", "Not in the MoSPI State series; check the UT Planning and Statistics Department.")]),
])

module(R, "government", [
    prose("p1", L(
        "Lakshadweep is a Union Territory without a legislature, run by an Administrator appointed by the President, with an elected District Panchayat and island (dweep) panchayats. It elects one member to the Lok Sabha, and courts come under the Kerala High Court. Praful Khoda Patel has been Administrator since December 2020; some of the regulations proposed by the Administration since 2021 have been debated and challenged in court.",
        "लक्षद्वीप बिना विधानसभा वाला केंद्र शासित प्रदेश है, जिसे राष्ट्रपति द्वारा नियुक्त प्रशासक चलाते हैं, निर्वाचित ज़िला पंचायत और द्वीप पंचायतों के साथ। इससे लोकसभा का एक सदस्य चुना जाता है, और न्यायालय केरल उच्च न्यायालय के अंतर्गत हैं। प्रफुल्ल खोड़ा पटेल दिसंबर 2020 से प्रशासक हैं; 2021 से प्रशासन द्वारा प्रस्तावित कुछ विनियमों पर बहस हुई है और उन्हें न्यायालय में चुनौती दी गई है।",
        "लक्षद्वीप हा विधिमंडळ नसलेला केंद्रशासित प्रदेश असून राष्ट्रपतींनी नेमलेले प्रशासक त्याचा कारभार पाहतात, निवडून आलेली जिल्हा पंचायत व बेट (द्वीप) पंचायतींसह. येथून लोकसभेवर एक सदस्य निवडला जातो, आणि न्यायालये केरळ उच्च न्यायालयाच्या अखत्यारीत आहेत. प्रफुल्ल खोडा पटेल डिसेंबर 2020 पासून प्रशासक आहेत; 2021 पासून प्रशासनाने प्रस्तावित केलेल्या काही नियमनांवर चर्चा झाली असून त्यांना न्यायालयात आव्हान देण्यात आले आहे."),
        sources=["ld-gov"], conf="Official"),
    {"type": "officeholders", "id": "officeholders"},
    gaps("g", [(L("Status of draft regulations (2021) — official record", "मसौदा विनियमों (2021) की स्थिति — आधिकारिक अभिलेख", "मसुदा नियमनांची (2021) स्थिती — अधिकृत नोंद"), "india-gov", "MHA / Lakshadweep Administration; Kerala High Court orders.")]),
])

module(R, "projects", [
    prose("p1", L(
        "The submarine fibre link from Kochi, opened in January 2024, transformed internet access. Desalination plants that turn seawater into drinking water, solar power and tourism development on islands such as Agatti and Kadmat are other priorities.",
        "जनवरी 2024 में खुले कोच्चि से समुद्री फ़ाइबर लिंक ने इंटरनेट पहुँच बदल दी। समुद्री जल को पेयजल में बदलने वाले विलवणीकरण संयंत्र, सौर ऊर्जा और अगत्ती व कदमत जैसे द्वीपों पर पर्यटन विकास अन्य प्राथमिकताएँ हैं।",
        "जानेवारी 2024 मध्ये सुरू झालेल्या कोचीहून सागरी फायबर जोडणीने इंटरनेट उपलब्धता बदलली. समुद्राचे पाणी पिण्यायोग्य करणारे निःक्षारीकरण प्रकल्प, सौरऊर्जा व अगत्ती आणि कदमतसारख्या बेटांवरील पर्यटन विकास ही इतर प्राधान्ये आहेत."),
        sources=["pmindia"], conf="Official"),
    {"type": "projects", "id": "projects"},
])

module(R, "transport", [
    prose("p1", L(
        "Agatti has the only airport, with flights from Kochi; helicopters link it with other islands. Passenger ships run from Kochi (and sometimes Kozhikode and Mangaluru) in 14–20 hours, and high-speed boats connect the islands in the calm season. Entry needs a permit from the Lakshadweep Administration.",
        "अगत्ती में एकमात्र हवाई अड्डा है, जहाँ कोच्चि से उड़ानें आती हैं; हेलीकॉप्टर इसे अन्य द्वीपों से जोड़ते हैं। यात्री जहाज़ कोच्चि (और कभी-कभी कोझिकोड और मंगलुरु) से 14–20 घंटे में चलते हैं, और शांत मौसम में तेज़ नौकाएँ द्वीपों को जोड़ती हैं। प्रवेश के लिए लक्षद्वीप प्रशासन का परमिट चाहिए।",
        "अगत्ती येथे एकमेव विमानतळ आहे, जिथे कोचीहून उड्डाणे येतात; हेलिकॉप्टर त्याला इतर बेटांशी जोडतात. प्रवासी जहाजे कोची (व कधी कोझिकोड आणि मंगळुरू) येथून 14–20 तासांत जातात, आणि शांत हंगामात वेगवान नौका बेटे जोडतात. प्रवेशासाठी लक्षद्वीप प्रशासनाचा परवाना लागतो."),
        conf="Editorial"),
])

module(R, "energy", [
    prose("p1", L(
        "Each inhabited island has its own small power station, mostly running on diesel shipped from the mainland. Solar plants, including a battery-backed plant at Kavaratti inaugurated in January 2024, are being added to reduce diesel use.",
        "हर बसे द्वीप का अपना छोटा बिजलीघर है, जो अधिकतर मुख्य भूमि से जहाज़ से लाए डीज़ल पर चलता है। डीज़ल का उपयोग घटाने के लिए सौर संयंत्र जोड़े जा रहे हैं, जिनमें जनवरी 2024 में शुरू हुआ कवरत्ती का बैटरी-समर्थित संयंत्र शामिल है।",
        "प्रत्येक वस्तीच्या बेटाचे स्वतःचे लहान वीजकेंद्र आहे, जे बहुतांश मुख्य भूमीवरून जहाजाने आणलेल्या डिझेलवर चालते. डिझेलचा वापर कमी करण्यासाठी सौर प्रकल्प वाढवले जात आहेत, ज्यांत जानेवारी 2024 मध्ये सुरू झालेला कवरत्तीचा बॅटरी-आधारित प्रकल्प आहे."),
        sources=["pmindia"], conf="Official"),
])

module(R, "digital", [
    prose("p1", L(
        "Before 2024 the islands relied on satellite links. The KLI-SOFC cable raised capacity from 1.7 Gbps to 200 Gbps, enabling 4G and better broadband, online classes and telemedicine.",
        "2024 से पहले द्वीप उपग्रह संपर्क पर निर्भर थे। केएलआई-एसओएफ़सी केबल ने क्षमता 1.7 जीबीपीएस से 200 जीबीपीएस तक बढ़ाई, जिससे 4जी और बेहतर ब्रॉडबैंड, ऑनलाइन कक्षाएँ और टेलीमेडिसिन संभव हुए।",
        "2024 पूर्वी बेटे उपग्रह जोडणीवर अवलंबून होती. केएलआय-एसओएफसी केबलने क्षमता 1.7 जीबीपीएसवरून 200 जीबीपीएसपर्यंत वाढवली, ज्यामुळे 4जी व चांगले ब्रॉडबँड, ऑनलाइन वर्ग व टेलिमेडिसिन शक्य झाले."),
        sources=["pmindia"], conf="Official"),
])

ger = AP["aishe_ger"]["LD"]
module(R, "education", [
    prose("p1", L(
        f"Literacy was 91.8% at the 2011 Census. AISHE reported a higher-education gross enrolment ratio of {ger['2020-21']}% in 2020-21 and {ger['2021-22']}% in 2021-22; the sharp drop probably reflects changes in reporting by the few institutions, and many islanders study in Kerala. Off-campus centres of the University of Calicut operate on the islands.",
        f"2011 की जनगणना में साक्षरता 91.8% थी। एआईएसएचई ने 2020-21 में उच्च शिक्षा सकल नामांकन अनुपात {ger['2020-21']}% और 2021-22 में {ger['2021-22']}% बताया; यह तेज़ गिरावट संभवतः कुछ संस्थानों की रिपोर्टिंग में बदलाव को दर्शाती है, और बहुत से द्वीपवासी केरल में पढ़ते हैं। कालीकट विश्वविद्यालय के ऑफ़-कैंपस केंद्र द्वीपों पर चलते हैं।",
        f"2011 च्या जनगणनेत साक्षरता 91.8% होती. एआयएसएचईने 2020-21 मध्ये उच्चशिक्षण एकूण नोंदणी गुणोत्तर {ger['2020-21']}% व 2021-22 मध्ये {ger['2021-22']}% नोंदवले; ही तीव्र घसरण बहुधा मोजक्या संस्थांच्या अहवाल पद्धतीतील बदल दर्शवते, आणि अनेक बेटवासी केरळमध्ये शिकतात. कालिकत विद्यापीठाची परिसराबाहेरील केंद्रे बेटांवर चालतात."),
        sources=["aishe", "es-india"], conf="Official"),
    facts("f", [fact("ger", L("Gross enrolment ratio, higher education (18–23)", "सकल नामांकन अनुपात, उच्च शिक्षा (18–23)", "एकूण नोंदणी गुणोत्तर, उच्चशिक्षण (18–23)"),
                     dp(ger["2021-22"], "%", "2021-22", "survey", "aishe", "https://aishe.gov.in", note="AISHE via MoSPI API. The fall from 7.17% (2020-21) is likely a reporting change; treat with caution."), "percent", "higher-is-better",
                     previous=dp(ger["2020-21"], "%", "2020-21", "survey", "aishe", "https://aishe.gov.in"), national=dp(28.4, "%", "2021-22", "survey", "aishe", "https://aishe.gov.in", level="national"))]),
])

n = NF["LD"]
module(R, "health", [
    prose("p1", L(
        f"In NFHS-5, {n['institutional_N5']:.1f}% of births took place in health facilities, but {n['stunted'][1]:.1f}% of children under five were stunted, up from {n['stunted'][0]}% in NFHS-4. Each inhabited island has a hospital or health centre, the Indira Gandhi Hospital at Kavaratti is the main one, and serious cases are flown to Kochi by helicopter or air ambulance.",
        f"एनएफ़एचएस-5 में {n['institutional_N5']:.1f}% प्रसव स्वास्थ्य संस्थानों में हुए, पर पाँच वर्ष से कम आयु के {n['stunted'][1]:.1f}% बच्चे ठिगने थे, जो एनएफ़एचएस-4 के {n['stunted'][0]}% से अधिक है। हर बसे द्वीप पर अस्पताल या स्वास्थ्य केंद्र है, कवरत्ती का इंदिरा गांधी अस्पताल मुख्य है, और गंभीर मामले हेलीकॉप्टर या एयर एम्बुलेंस से कोच्चि ले जाए जाते हैं।",
        f"एनएफएचएस-5 मध्ये {n['institutional_N5']:.1f}% प्रसूती आरोग्य संस्थांत झाल्या, पण पाच वर्षांखालील {n['stunted'][1]:.1f}% मुले खुजी होती, एनएफएचएस-4 मधील {n['stunted'][0]}% पेक्षा जास्त. प्रत्येक वस्तीच्या बेटावर रुग्णालय किंवा आरोग्य केंद्र आहे, कवरत्तीचे इंदिरा गांधी रुग्णालय मुख्य आहे, आणि गंभीर रुग्णांना हेलिकॉप्टर किंवा हवाई रुग्णवाहिकेने कोचीला नेले जाते."),
        sources=["srs", "nfhs"], conf="Official"),
    srs_facts("LD"), nfhs_block("LD"),
])

module(R, "nature", [
    prose("p1", L(
        "Lakshadweep's coral reefs and lagoons hold a rich variety of corals, reef fish, sea turtles and seagrass, and Pitti island is a protected nesting site for sooty terns and other seabirds. Coral bleaching during marine heatwaves and coastal erosion are serious threats to the low islands. Coconut palms cover most of the land, which ISFR counts as about 90% forest and tree cover. There is no Ramsar site in Lakshadweep on the list as on 21 April 2026.",
        "लक्षद्वीप की प्रवाल भित्तियों और लैगूनों में प्रवाल, भित्ति मछलियों, समुद्री कछुओं और समुद्री घास की समृद्ध विविधता है, और पित्ती द्वीप सूटी टर्न और अन्य समुद्री पक्षियों का संरक्षित घोंसला स्थल है। समुद्री लू के दौरान प्रवाल विरंजन और तटीय कटाव इन नीचे द्वीपों के लिए गंभीर ख़तरे हैं। अधिकांश भूमि नारियल के पेड़ों से ढकी है, जिसे आईएसएफ़आर लगभग 90% वन आवरण गिनता है। 21 अप्रैल 2026 की सूची में लक्षद्वीप में कोई रामसर स्थल नहीं है।",
        "लक्षद्वीपच्या प्रवाळ भित्ती व खाजणांत प्रवाळ, भित्ती मासे, सागरी कासवे व समुद्री गवताची समृद्ध विविधता आहे, आणि पित्ती बेट हे सुटी टर्न व इतर सागरी पक्ष्यांचे संरक्षित घरटी स्थळ आहे. सागरी उष्णलाटांदरम्यान प्रवाळ विरंजन व किनारी धूप हे या सखल बेटांसाठी गंभीर धोके आहेत. बहुतेक जमीन नारळीच्या झाडांनी व्यापलेली आहे, जी आयएसएफआर सुमारे 90% वनाच्छादन म्हणून मोजते. 21 एप्रिल 2026 च्या यादीत लक्षद्वीपमध्ये कोणतेही रामसर स्थळ नाही."),
        sources=["fsi", "indian-wetlands"], conf="Official"),
    forest_facts("LD", m["forestCoverPct"], 0, "MoEFCC list of Ramsar sites as on 21 April 2026: none in Lakshadweep."),
])

module(R, "water", [
    prose("p1", L(
        "Fresh water is scarce: a thin lens of groundwater floats on seawater beneath each island and is easily polluted or turned salty. Low-temperature thermal desalination plants, which use cold deep-sea water, supply drinking water on Kavaratti, Agatti, Minicoy and other islands, and rainwater is harvested from roofs.",
        "मीठा पानी दुर्लभ है: हर द्वीप के नीचे समुद्री जल पर भूजल की पतली परत तैरती है, जो आसानी से प्रदूषित या खारी हो जाती है। गहरे समुद्र के ठंडे पानी का उपयोग करने वाले निम्न-तापमान तापीय विलवणीकरण संयंत्र कवरत्ती, अगत्ती, मिनिकॉय और अन्य द्वीपों पर पेयजल देते हैं, और छतों से वर्षा जल संचित किया जाता है।",
        "गोडे पाणी दुर्मीळ आहे: प्रत्येक बेटाखाली समुद्राच्या पाण्यावर भूजलाचा पातळ थर तरंगतो, जो सहज प्रदूषित किंवा खारट होतो. खोल समुद्रातील थंड पाणी वापरणारे कमी-तापमान औष्णिक निःक्षारीकरण प्रकल्प कवरत्ती, अगत्ती, मिनिकॉय व इतर बेटांवर पिण्याचे पाणी पुरवतात, आणि छपरांवरून पावसाचे पाणी साठवले जाते."),
        sources=["pmindia"], conf="Editorial"),
])

module(R, "safety", [
    prose("p1", L(
        "The low-lying islands are exposed to cyclones, storm surges and sea-level rise; Cyclone Ockhi in 2017 caused heavy damage. Ship and boat services stop in rough monsoon seas, so travel plans need flexibility. Visitors must follow permit rules and local customs.",
        "नीचे बसे द्वीप चक्रवातों, तूफ़ानी लहरों और समुद्र स्तर में वृद्धि के प्रति संवेदनशील हैं; 2017 में चक्रवात ओखी ने भारी क्षति की। अशांत मानसूनी समुद्र में जहाज़ और नौका सेवाएँ रुक जाती हैं, इसलिए यात्रा योजना लचीली रखनी चाहिए। पर्यटकों को परमिट नियमों और स्थानीय रीति-रिवाजों का पालन करना चाहिए।",
        "सखल बेटे चक्रीवादळे, वादळी लाटा व समुद्रपातळीतील वाढ यांना तोंड देतात; 2017 मध्ये ओखी चक्रीवादळाने मोठे नुकसान केले. खवळलेल्या मान्सूनी समुद्रात जहाज व नौका सेवा थांबतात, त्यामुळे प्रवासाचे नियोजन लवचिक ठेवावे. पर्यटकांनी परवाना नियम व स्थानिक रीतिरिवाज पाळावेत."),
        conf="Editorial"),
    emergency_table(("Lakshadweep", "लक्षद्वीप", "लक्षद्वीप")),
])

module(R, "gi", [
    prose("p1", L(
        "No GI on the GI Registry's list as on 31 December 2025 is registered for Lakshadweep.",
        "जीआई रजिस्ट्री की 31 दिसंबर 2025 की सूची में लक्षद्वीप के लिए कोई जीआई पंजीकृत नहीं है।",
        "जीआय रजिस्ट्रीच्या 31 डिसेंबर 2025 च्या यादीत लक्षद्वीपसाठी कोणताही जीआय नोंदणीकृत नाही."),
        sources=["gi-registry"], conf="Official"),
])

module(R, "tourism", [
    prose("p1", L(
        "Agatti, Bangaram, Kadmat, Kavaratti and Minicoy are open to tourists with permits, usually through packages from Kochi. Snorkelling, scuba diving, glass-bottom boat rides and kayaking in the lagoons are the main draws, and Minicoy has a lighthouse built in 1885 and traditional boat-building villages.",
        "अगत्ती, बंगाराम, कदमत, कवरत्ती और मिनिकॉय परमिट के साथ पर्यटकों के लिए खुले हैं, आमतौर पर कोच्चि से पैकेज के ज़रिए। लैगून में स्नॉर्कलिंग, स्कूबा डाइविंग, ग्लास-बॉटम नौका की सवारी और कयाकिंग मुख्य आकर्षण हैं, और मिनिकॉय में 1885 में बना प्रकाशस्तंभ और पारंपरिक नौका-निर्माण वाले गाँव हैं।",
        "अगत्ती, बंगाराम, कदमत, कवरत्ती व मिनिकॉय परवान्यासह पर्यटकांसाठी खुली आहेत, सहसा कोचीहून पॅकेजद्वारे. खाजणांतील स्नॉर्केलिंग, स्कूबा डायव्हिंग, काचेच्या तळाच्या नौकेतील सफर व कयाकिंग ही मुख्य आकर्षणे आहेत, आणि मिनिकॉयमध्ये 1885 मध्ये बांधलेले दीपगृह व पारंपरिक नौकाबांधणीची गावे आहेत."),
        conf="Editorial"),
])

module(R, "cities", [
    lst("cities", [
        item("kavaratti", L("Kavaratti", "कवरत्ती", "कवरत्ती"), detail=L("Capital island.", "राजधानी द्वीप।", "राजधानीचे बेट."), meta=L("Capital", "राजधानी", "राजधानी")),
        item("agatti", L("Agatti", "अगत्ती", "अगत्ती"), detail=L("Airport island.", "हवाई अड्डे वाला द्वीप।", "विमानतळ असलेले बेट."), meta=L("Transport", "परिवहन", "वाहतूक")),
        item("minicoy", L("Minicoy", "मिनिकॉय", "मिनिकॉय"), detail=L("Southernmost island; Mahl-speaking.", "सबसे दक्षिणी द्वीप; महल भाषी।", "दक्षिणेकडील बेट; महल भाषक."), meta=L("Culture", "संस्कृति", "संस्कृती")),
        item("andrott", L("Andrott", "आंद्रोत", "आंद्रोत"), detail=L("Tomb of Ubaidullah.", "उबैदुल्लाह की मज़ार।", "उबैदुल्लाह यांची दर्गा."), meta=L("Heritage", "धरोहर", "वारसा")),
    ], title=L("Inhabited islands (selected)", "बसे हुए द्वीप (चयनित)", "वस्तीची बेटे (निवडक)"), conf="Editorial"),
])

module(R, "sports", [
    prose("p1", L(
        "Football and volleyball are popular, and traditional boat races are held on Minicoy. The lagoons are ideal for water sports.",
        "फ़ुटबॉल और वॉलीबॉल लोकप्रिय हैं, और मिनिकॉय में पारंपरिक नौका दौड़ होती है। लैगून जल क्रीड़ाओं के लिए आदर्श हैं।",
        "फुटबॉल व व्हॉलीबॉल लोकप्रिय आहेत, आणि मिनिकॉयवर पारंपरिक नौकाशर्यती होतात. खाजणे जलक्रीडेसाठी आदर्श आहेत."),
        conf="Editorial"),
])

module(R, "personalities", [
    lst("people", [
        person("sayeed", ("P. M. Sayeed", "पी. एम. सईद", "पी. एम. सईद"), ("Represented Lakshadweep in the Lok Sabha for ten terms and was Deputy Speaker.", "दस कार्यकालों तक लोकसभा में लक्षद्वीप का प्रतिनिधित्व किया और उपाध्यक्ष रहे।", "दहा कारकिर्दी लोकसभेत लक्षद्वीपचे प्रतिनिधित्व केले व उपाध्यक्ष होते."), ("Public life", "सार्वजनिक जीवन", "सार्वजनिक जीवन")),
    ], title=L("Notable personalities", "प्रमुख व्यक्तित्व", "उल्लेखनीय व्यक्तिमत्त्वे"), conf="Editorial"),
])

module(R, "diaspora", [
    prose("p1", L(
        "Many islanders live and study in Kochi and Kozhikode, and some work in the Gulf countries and in merchant shipping, a traditional occupation of Minicoy's men.",
        "बहुत से द्वीपवासी कोच्चि और कोझिकोड में रहते और पढ़ते हैं, और कुछ खाड़ी देशों और व्यापारिक जहाज़रानी में काम करते हैं, जो मिनिकॉय के पुरुषों का पारंपरिक व्यवसाय है।",
        "अनेक बेटवासी कोची व कोझिकोडमध्ये राहतात व शिकतात, आणि काही आखाती देशांत व व्यापारी जहाजवाहतुकीत काम करतात, जो मिनिकॉयच्या पुरुषांचा पारंपरिक व्यवसाय आहे."),
        conf="Editorial"),
])

module(R, "civic", [links([
    it3("portal", "Lakshadweep Administration", "लक्षद्वीप प्रशासन", "लक्षद्वीप प्रशासन", url="https://lakshadweep.gov.in", src="ld-gov"), RTI])])

module(R, "trivia", [
    lst("facts", [
        triv("smallest", ("Lakshadweep had 64,473 people in 2011 on about 30 km² of land.", "2011 में लक्षद्वीप में लगभग 30 वर्ग किमी भूमि पर 64,473 लोग थे।", "2011 मध्ये लक्षद्वीपमध्ये सुमारे 30 चौ.किमी जमिनीवर 64,473 लोक होते."), PYD, "census"),
        triv("fibre", ("The 2024 fibre link raised internet capacity from 1.7 to 200 Gbps.", "2024 के फ़ाइबर लिंक ने इंटरनेट क्षमता 1.7 से 200 जीबीपीएस की।", "2024 च्या फायबर जोडणीने इंटरनेट क्षमता 1.7 वरून 200 जीबीपीएस केली."), SOFC, "pmindia"),
    ], title=L("Did you know?", "क्या आप जानते हैं?", "तुम्हाला माहीत आहे का?"), conf="Editorial"),
])
print("ld ok")
