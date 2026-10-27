import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

KL_SPB = "https://spb.kerala.gov.in/economic-review/ER2015/Chapter1/chapter01.html"
CAG_KL = "https://cag.gov.in/ag1/kerala/en/audit-report/details/6067"
mo = research("mospi_kl.json")

r = read("regions/IN-KL.json")
r["slug"] = "keralam"
r["name"] = L("Keralam", "केरलम", "केरळम")
r["formerNames"] = [L("Kerala", "केरल", "केरळ")]
r["officialPortal"] = "https://kerala.gov.in"
m = r["metrics"]
m["population2011"] = dp(33406061, "persons", "2011", "census", "census", KL_SPB,
    note="Census 2011 total as published by the Kerala State Planning Board (Economic Review). Males 1,60,27,412; females 1,73,78,649.")
m["area"] = dp(38852, "km²", "2023", "calendar", "fsi", LS_FOREST,
    note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026). State documents (CAG, LSGD) cite 38,863 km².")
m["density2011"] = dp(860, "persons per km²", "2011", "census", "census", KL_SPB, note="Kerala State Planning Board, Economic Review.")
m["sexRatio2011"] = dp(1084, "females per 1000 males", "2011", "census", "census", KL_SPB, note="Highest among States at the 2011 Census.")
m["childSexRatio2011"] = dp(964, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR,
    note="PIB release of 11 Feb 2014 (RGI data). Was 960 in 2001. The State Planning Board also gives 964.")
m["literacyRate2011"] = dp(94, "%", "2011", "census", "census", KL_SPB, note="Population aged 7+, as rounded in the Economic Review (\"94 per cent\").")
m["urbanisation2011"] = dp(47.72, "%", "2011", "census", "census", KL_SPB, note="Urban population share at the 2011 Census (Economic Review).")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2025-26 not yet published for Keralam. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note="MoSPI, base 2011-12.")
m["forestCoverPct"] = dp(56.78, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 22,059.36 km² ÷ geographical area 38,852 km².")


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Indian elephant", "भारतीय हाथी", "भारतीय हत्ती", "Elephas maximus indicus"),
    "bird": sym("Great hornbill", "मलबार धनेश (ग्रेट हॉर्नबिल)", "राज धनेश (ग्रेट हॉर्नबिल)", "Buceros bicornis"),
    "flower": sym("Golden shower (Kanikkonna)", "अमलतास (कणिक्कोन्ना)", "बहावा (कणिक्कोन्ना)", "Cassia fistula"),
    "tree": sym("Coconut palm", "नारियल", "नारळ", "Cocos nucifera"),
    "fish": sym("Pearl spot (Karimeen)", "करिमीन (पर्ल स्पॉट)", "करिमीन (पर्ल स्पॉट)", "Etroplus suratensis"),
    "fruit": sym("Jackfruit", "कटहल", "फणस", "Artocarpus heterophyllus"),
    "butterfly": sym("Malabar banded peacock", "मलबार बैंडेड पीकॉक", "मलबार बँडेड पीकॉक", "Papilio buddha"),
}

NOA = "https://www.newsonair.gov.in/congress-leader-vd-satheesan-sworn-in-as-chief-minister-of-keralam/"
SPK = "https://newsonair.gov.in/lok-sabha-speaker-congratulates-thiruvanchoor-radhakrishnan-electing-speaker-of-16th-kerala-legislative-assembly/"
LOP = "https://www.keralakaumudi.com/en/kerala/general/thiruvanchoor-radhakrishnan-elected-speaker-of-16th-kerala-assembly-1751437"
GOV = "https://test.uniindia.com/kerala-govt-objects-to-governor-s-meeting-with-officials-seeks-to-prevent-recurrence/south/news/3881569.html"
r["government"] = {
    "headOfState": office("governor", L("Rajendra Vishwanath Arlekar", "राजेंद्र विश्वनाथ आर्लेकर", "राजेंद्र विश्वनाथ आर्लेकर"), None, None,
                          "uni", GOV, "https://igod.gov.in", conf="Third-party verified",
                          note="Took office in January 2025 (oath scheduled for 2 January 2025, per Kerala Kaumudi). Named as Governor in reports of June and August 2026. Kerala's Raj Bhavan was renamed Lok Bhavan on 1 December 2025. On 12 October 2026 the President appointed Om Prakash Mathur, Governor of Sikkim, as Governor of Keralam and moved Arlekar to Tamil Nadu, with effect from the dates they assume charge (Rashtrapati Bhavan communiqué, reported by UNI and ANI). Update this card when Mathur is sworn in."),
    "headOfGovernment": office("chief-minister", L("V. D. Satheesan", "वी. डी. सतीशन", "व्ही. डी. सतीशन"), "INC", "2026-05-18",
                               "newsonair", NOA, "https://kerala.gov.in",
                               note="Sworn in on 18 May 2026 with 20 Cabinet ministers, after the UDF won the April 2026 Assembly election (News On AIR)."),
    "others": [
        office("speaker", L("Thiruvanchoor Radhakrishnan", "तिरुवंचूर राधाकृष्णन", "तिरुवंचूर राधाकृष्णन"), "INC", None, "newsonair", SPK, "https://www.niyamasabha.org",
               note="Elected Speaker of the 16th Kerala Legislative Assembly; congratulated by the Lok Sabha Speaker on 22 May 2026 (News On AIR). Won 101 of 139 votes cast (Kerala Kaumudi)."),
        office("leader-of-opposition", L("Pinarayi Vijayan", "पिनराई विजयन", "पिनराई विजयन"), "CPI(M)", None, "keralakaumudi", LOP, "https://www.niyamasabha.org",
               conf="Third-party verified",
               note="Named Opposition Leader by the CPI(M) in May 2026 (UNI) and referred to as Opposition Leader in the House on 22 May 2026 (Kerala Kaumudi). Former Chief Minister (2016–2026)."),
    ],
}

r["projects"] = [
    proj("vizhinjam", L("Vizhinjam International Deepwater Multipurpose Seaport (Phase 1)", "विझिंजम अंतरराष्ट्रीय डीपवाटर बहुउद्देशीय बंदरगाह (चरण 1)", "विझिंजम आंतरराष्ट्रीय खोल पाण्याचे बहुउद्देशीय बंदर (टप्पा 1)"),
         L("India's first dedicated container transshipment port, near Thiruvananthapuram, with a natural draught of nearly 20 metres. Dedicated to the nation on 2 May 2025; described as the country's first semi-automated port.",
           "तिरुवनंतपुरम के पास भारत का पहला समर्पित कंटेनर ट्रांसशिपमेंट बंदरगाह, जिसकी प्राकृतिक गहराई लगभग 20 मीटर है। 2 मई 2025 को राष्ट्र को समर्पित; इसे देश का पहला अर्ध-स्वचालित बंदरगाह बताया गया।",
           "तिरुवनंतपुरमजवळील भारतातील पहिले समर्पित कंटेनर ट्रान्सशिपमेंट बंदर; नैसर्गिक खोली सुमारे 20 मीटर. 2 मे 2025 रोजी राष्ट्राला समर्पित; देशातील पहिले अर्ध-स्वयंचलित बंदर म्हणून उल्लेख."),
         "ports", None, 8800, "about ₹8,800 crore", "2025", None, "May 2025", "Completed",
         "newsonair", "https://www.newsonair.gov.in/pm-modi-to-dedicate-vizhinjam-international-port-indias-1st-semi-automated-port/"),
]

GI_NAMES = {
 "Alleppey Green Cardamom": ("अलेप्पी हरी इलायची", "अलेप्पी हिरवी वेलची"),
 "Malabar Pepper": ("मलबार काली मिर्च", "मलबार मिरी"),
 "Monsooned Malabar Arabica Coffee": ("मॉनसून्ड मलबार अरेबिका कॉफ़ी", "मॉन्सून्ड मलबार अरेबिका कॉफी"),
 "Monsooned Malabar Robusta Coffee": ("मॉनसून्ड मलबार रोबस्टा कॉफ़ी", "मॉन्सून्ड मलबार रोबस्टा कॉफी"),
 "Navara Rice": ("नवारा चावल", "नवारा तांदूळ"),
 "Palakkadan Matta Rice": ("पालक्काडन मट्टा चावल", "पालक्काडन मट्टा तांदूळ"),
 "Pokkali Rice": ("पोक्काली चावल", "पोक्काली तांदूळ"),
 "Vazhakulam Pineapple": ("वाझकुलम अनानास", "वाझकुलम अननस"),
 "Wayanad Jeerakasala Rice": ("वायनाड जीरकशाला चावल", "वायनाड जीरकशाला तांदूळ"),
 "Wayanad Gandhakasala Rice": ("वायनाड गंधकशाला चावल", "वायनाड गंधकशाला तांदूळ"),
 "Kaipad Rice": ("कैपाड चावल", "कैपाड तांदूळ"),
 "Chengalikodan Nendran Banana": ("चेंगालिकोडन नेंद्रन केला", "चेंगालिकोडन नेंद्रन केळी"),
 "Nilambur Teak": ("निलांबुर सागौन", "निलांबूर साग"),
 "Wayanaad Robusta Coffee": ("वायनाड रोबस्टा कॉफ़ी", "वायनाड रोबस्टा कॉफी"),
 "Tirur Betel Leaf (Tirur Vettila)": ("तिरूर पान (तिरूर वेट्टिला)", "तिरूर विड्याचे पान (तिरूर वेट्टिला)"),
 "Kuttiattoor Mango (Kuttiattoor Manga)": ("कुट्टियाट्टूर आम", "कुट्टियाट्टूर आंबा"),
 "Edayur Chilli": ("एडयूर मिर्च", "एडयूर मिरची"),
 "Attappady Aattukombu Avara": ("अट्टप्पाडी आट्टुकोम्बु अवरा (सेम)", "अट्टप्पाडी आट्टुकोम्बु अवरा (घेवडा)"),
 "Attappady Thuvara": ("अट्टप्पाडी तुवरा (अरहर)", "अट्टप्पाडी तुवरा (तूर)"),
 "Onattukara Ellu": ("ओणाट्टुकरा एल्लु (तिल)", "ओणाट्टुकरा एल्लु (तीळ)"),
 "Kanthalloor Vattavada Veluthulli": ("कांतल्लूर वट्टवडा वेलुत्तुल्ली (लहसुन)", "कांतल्लूर वट्टवडा वेलुत्तुल्ली (लसूण)"),
 "Kodungallur Pottuvellari": ("कोडुंगल्लूर पोट्टुवेल्लरी (ककड़ी)", "कोडुंगल्लूर पोट्टुवेल्लरी (काकडी)"),
 "Thalanadan Grambu (Clove)": ("तलनाडन ग्राम्पु (लौंग)", "तलनाडन ग्राम्पु (लवंग)"),
 "Central Travancore Jaggery": ("मध्य त्रावणकोर गुड़", "मध्य त्रावणकोर गूळ"),
 "Marayoor Jaggery (Marayoor Sharkara)": ("मरयूर गुड़ (मरयूर शर्करा)", "मरयूर गूळ (मरयूर शर्करा)"),
 "Aranmula Kannadi (Aranmula Metal Mirror)": ("आरनमुला कण्णाडी (धातु दर्पण)", "आरनमुळा कण्णाडी (धातूचा आरसा)"),
 "Payyannur Pavithra Ring": ("पय्यन्नूर पवित्र अंगूठी", "पय्यन्नूर पवित्र अंगठी"),
 "Alleppey Coir": ("अलेप्पी कॉयर (नारियल रेशा)", "अलेप्पी काथ्या (कॉयर)"),
 "Brass Broidered Coconut Shell Crafts of Kerala": ("केरल के पीतल-जड़ित नारियल खोल शिल्प", "केरळची पितळ नक्षीच्या करवंटी हस्तकला"),
 "Screw Pine Craft of Kerala": ("केरल का केवड़ा पत्ती शिल्प", "केरळची केवडा पानांची हस्तकला"),
 "Maddalam of Palakkad": ("पालक्काड का मद्दलम", "पालक्काडचे मद्दलम"),
 "Cannanore Home Furnishings": ("कण्णूर गृह सज्जा वस्त्र", "कण्णूर गृहसजावट वस्त्रे"),
 "Balaramapuram Sarees and Fine Cotton Fabrics": ("बलरामपुरम साड़ियाँ और महीन सूती वस्त्र", "बलरामपुरम साड्या व तलम सुती वस्त्रे"),
 "Kasaragod Sarees": ("कासरगोड साड़ियाँ", "कासारगोड साड्या"),
 "Kuthampully Sarees": ("कुत्ताम्पुल्ली साड़ियाँ", "कुत्ताम्पुल्ली साड्या"),
 "Chendamangalam Dhoties & Set Mundu": ("चेंदमंगलम धोती और सेट मुंडु", "चेंदमंगलम धोतर व सेट मुंडू"),
 "Kuthampully Dhoties & Set Mundu": ("कुत्ताम्पुल्ली धोती और सेट मुंडु", "कुत्ताम्पुल्ली धोतर व सेट मुंडू"),
 "Maddalam of Palakkad (Logo)": ("पालक्काड का मद्दलम (लोगो)", "पालक्काडचे मद्दलम (बोधचिन्ह)"),
 "Brass Broidered Coconut Shell Crafts of Kerala (Logo)": ("केरल के पीतल-जड़ित नारियल खोल शिल्प (लोगो)", "केरळची पितळ नक्षीच्या करवंटी हस्तकला (बोधचिन्ह)"),
 "Screw Pine Craft of Kerala (Logo)": ("केरल का केवड़ा पत्ती शिल्प (लोगो)", "केरळची केवडा पानांची हस्तकला (बोधचिन्ह)"),
 "Kannadippaya (Bamboo Mat)": ("कण्णाडिप्पाया (बाँस की चटाई)", "कण्णाडिप्पाया (बांबूची चटई)"),
}
TEXTILE = {"Balaramapuram Sarees and Fine Cotton Fabrics", "Kasaragod Sarees", "Kuthampully Sarees", "Chendamangalam Dhoties & Set Mundu",
           "Kuthampully Dhoties & Set Mundu", "Cannanore Home Furnishings"}
SHARED = {"KL,TN": ["Tamil Nadu"], "KL,KA,TN": ["Karnataka", "Tamil Nadu"], "KA,KL": ["Karnataka"]}
r["giProducts"] = gi_list("gi_kl.tsv", GI_NAMES, SHARED, TEXTILE)
KL_GOV = office("governor", L("Om Prakash Mathur", "ओम प्रकाश माथुर", "ओम प्रकाश माथुर"), None, "2026-10-23",
                "president-of-india", "https://presidentofindia.nic.in/press_releases/press-communique-38", "https://igod.gov.in",
                note="Official confirmation: Rashtrapati Bhavan communiqué of 12 October 2026 appointing Om Prakash Mathur, then Governor of Sikkim, as Governor of Keralam. Sworn in as the 29th Governor of Keralam at the Lok Bhavan auditorium, Thiruvananthapuram, on 23 October 2026 by Chief Justice Soumen Sen of the Keralam High Court (ETV Bharat). Succeeded Rajendra Vishwanath Arlekar, who moved to Tamil Nadu.",
                as_of="2026-10-27")
r["government"]["headOfState"] = KL_GOV  # changed 23 Oct 2026; re-checked 27 Oct 2026
r["meta"] = {"lastUpdated": "2026-10-27",  # freshness pass; BD_TODAY stays the original authoring date
              "editorialStatus": "draft"}
write("regions/IN-KL.json", r)
print("kl core ok", len(r["giProducts"]), "GIs")
