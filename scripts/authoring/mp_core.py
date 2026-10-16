"""Madhya Pradesh — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-16."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.freepressjournal.in/bhopal/mangubhai-to-be-5th-governor-to-remain-in-office-even-after-5-years"
CM = "https://scroll.in/latest/1060516/mohan-yadav-vishnu-deo-sai-take-oath-as-chief-ministers-of-madhya-pradesh-chhattisgarh"
SPK = "https://www.freepressjournal.in/amp/bhopal/ex-union-minister-narendra-singh-tomar-elected-speaker-of-mp-assembly"
METRO = "https://www.newsonair.gov.in/metro-train-services-officially-commenced-in-bhopal-madhya-pradesh"
KB = "https://www.newsonair.gov.in/pm-modi-to-lay-foundation-stone-of-countrys-first-ken-betwa-river-linking-project-in-madhya-pradesh"

mp = research("mospi_mp.json")
r = read("regions/IN-MP.json")
m = r["metrics"]
m["population2011"] = dp(72626809, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 3,76,12,306; females 3,50,14,503.")
m["area"] = dp(308252, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(236, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 7,26,26,809 ÷ area 3,08,252 km² = 235.6.")
m["sexRatio2011"] = dp(931, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (919 in 2001).")
m["childSexRatio2011"] = dp(918, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 932 in 2001.")
m["literacyRate2011"] = dp(69.3, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mp["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25: ₹{inr(mp['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mp["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(mp['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(25.00, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 77,073.44 km² ÷ geographical area 3,08,252 km².")

r["officialPortal"] = "https://www.mp.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Barasingha (hard-ground swamp deer)", "बारहसिंगा", "बाराशिंगा", "Rucervus duvaucelii branderi"),
    "bird": sym("Indian paradise flycatcher (dudhraj)", "दूधराज (शाह बुलबुल)", "स्वर्गीय नर्तक (दूधराज)", "Terpsiphone paradisi"),
    "flower": sym("Madonna lily", "सफ़ेद लिली", "पांढरी लिली", "Lilium candidum"),
    "tree": sym("Banyan", "बरगद", "वड", "Ficus benghalensis"),
}

r["government"] = {
    "headOfState": office("governor", L("Mangubhai C. Patel", "मंगुभाई छ. पटेल", "मंगूभाई छ. पटेल"), None, "2021-07-08",
                          "fpj", GOV, "https://igod.gov.in", conf="Third-party verified",
                          note="Appointed on 6 July 2021 and sworn in on 8 July 2021. Free Press Journal reported on 6 July 2026 that he completed five years and continues until a successor is appointed. Confirm on the Lok Bhavan, Madhya Pradesh website."),
    "headOfGovernment": office("chief-minister", L("Mohan Yadav", "मोहन यादव", "मोहन यादव"), "BJP", "2023-12-13",
                               "scroll", CM, "https://www.mp.gov.in", conf="Third-party verified",
                               note="Sworn in on 13 December 2023 (Scroll). Inaugurated Bhopal Metro services as Chief Minister on 20 December 2025 (News On AIR)."),
    "others": [
        office("deputy-chief-minister", L("Jagdish Devda", "जगदीश देवड़ा", "जगदीश देवडा"), "BJP", "2023-12-13", "scroll", CM, "https://www.mp.gov.in",
               conf="Third-party verified", note="Sworn in with the Chief Minister (Scroll)."),
        office("deputy-chief-minister", L("Rajendra Shukla", "राजेंद्र शुक्ल", "राजेंद्र शुक्ला"), "BJP", "2023-12-13", "scroll", CM, "https://www.mp.gov.in",
               conf="Third-party verified", note="Sworn in with the Chief Minister (Scroll)."),
        office("speaker", L("Narendra Singh Tomar", "नरेंद्र सिंह तोमर", "नरेंद्रसिंह तोमर"), "BJP", "2023-12-20", "fpj", SPK, "https://mpvidhansabha.nic.in",
               conf="Third-party verified", note="Former Union minister, elected unopposed in December 2023 (Free Press Journal). Confirm the date on the Assembly website."),
    ],
}

r["projects"] = [
    proj("ken-betwa", L("Ken–Betwa river link project", "केन–बेतवा नदी जोड़ परियोजना", "केन–बेतवा नदीजोड प्रकल्प"),
         L("The first project under the national river-linking plan, transferring water from the Ken to the Betwa basin through the Daudhan dam and a link canal. It is meant to irrigate more than 8 lakh hectares in 10 districts of Madhya Pradesh and over 2.5 lakh hectares in Uttar Pradesh, supply drinking water to about 65 lakh people, and add 103 MW of hydro and 27 MW of solar power. The Prime Minister laid the foundation stone at Khajuraho on 25 December 2024.",
           "राष्ट्रीय नदी-जोड़ योजना की पहली परियोजना, जो दौधन बाँध और लिंक नहर से केन का पानी बेतवा बेसिन में ले जाएगी। इसका उद्देश्य मध्य प्रदेश के 10 ज़िलों में 8 लाख हेक्टेयर से अधिक और उत्तर प्रदेश में 2.5 लाख हेक्टेयर से अधिक की सिंचाई, लगभग 65 लाख लोगों को पेयजल, और 103 मेगावाट जलविद्युत व 27 मेगावाट सौर बिजली है। प्रधानमंत्री ने 25 दिसंबर 2024 को खजुराहो में इसकी आधारशिला रखी।",
           "राष्ट्रीय नदीजोड योजनेतील पहिला प्रकल्प, जो दौधन धरण व जोड कालव्यातून केनचे पाणी बेतवा खोऱ्यात नेईल. मध्य प्रदेशच्या 10 जिल्ह्यांत 8 लाख हेक्टरहून अधिक व उत्तर प्रदेशात 2.5 लाख हेक्टरहून अधिक सिंचन, सुमारे 65 लाख लोकांना पिण्याचे पाणी, आणि 103 मेगावॅट जलविद्युत व 27 मेगावॅट सौरऊर्जा हा उद्देश आहे. पंतप्रधानांनी 25 डिसेंबर 2024 रोजी खजुराहो येथे पायाभरणी केली."),
         "water", "Ken-Betwa Link Project Authority / Ministry of Jal Shakti", 44605, "₹44,605 crore; the Centre bears 90% (News On AIR).", "2024", "December 2024", None, "Under Construction", "newsonair", KB,
         challenges=L("Part of Panna Tiger Reserve will be submerged; the approved wildlife and resettlement plans need official tracking.", "पन्ना बाघ अभयारण्य का कुछ भाग डूबेगा; स्वीकृत वन्यजीव और पुनर्वास योजनाओं पर आधिकारिक निगरानी ज़रूरी है।", "पन्ना व्याघ्र प्रकल्पाचा काही भाग बुडणार आहे; मंजूर वन्यजीव व पुनर्वसन आराखड्यांचा अधिकृत पाठपुरावा आवश्यक आहे.")),
    proj("bhopal-metro", L("Bhopal Metro — priority corridor", "भोपाल मेट्रो — प्राथमिकता गलियारा", "भोपाळ मेट्रो — प्राधान्य मार्गिका"),
         L("The first 7 km stretch of the Orange Line, with eight elevated stations from Subhash Nagar, opened to passengers in December 2025; it was inaugurated by the Union Housing and Urban Affairs Minister and the Chief Minister on 20 December 2025.",
           "ऑरेंज लाइन का पहला 7 किमी खंड, सुभाष नगर से आठ एलिवेटेड स्टेशनों के साथ, दिसंबर 2025 में यात्रियों के लिए खुला; केंद्रीय आवास और शहरी कार्य मंत्री और मुख्यमंत्री ने 20 दिसंबर 2025 को इसका उद्घाटन किया।",
           "ऑरेंज मार्गिकेचा पहिला 7 किमीचा टप्पा, सुभाष नगरपासून आठ उन्नत स्थानकांसह, डिसेंबर 2025 मध्ये प्रवाशांसाठी खुला झाला; केंद्रीय गृहनिर्माण व नागरी व्यवहार मंत्री व मुख्यमंत्र्यांनी 20 डिसेंबर 2025 रोजी उद्घाटन केले."),
         "urban", "Madhya Pradesh Metro Rail Corporation", None, None, None, None, "20 December 2025", "Completed", "newsonair", METRO),
]

GI_NAMES = {
 "Balaghat Chinnor": ("बालाघाट चिन्नौर", "बालाघाट चिन्नोर"),
 "Sharbati Gehu": ("शरबती गेहूँ", "शरबती गहू"),
 "Rewa Sunderja Mango": ("रीवा सुंदरजा आम", "रीवा सुंदरजा आंबा"),
 "Ratlam Riyawan Lahsun (Garlic)": ("रतलाम रियावन लहसुन", "रतलाम रियावन लसूण"),
 "Ratlami Sev": ("रतलामी सेव", "रतलामी शेव"),
 "Morena Gajak": ("मुरैना गजक", "मुरैना गजक"),
 "Jhabua Kadaknath Black Chicken Meat": ("झाबुआ कड़कनाथ काले मुर्गे का मांस", "झाबुआ कडकनाथ काळ्या कोंबडीचे मांस"),
 "Chanderi Sarees": ("चंदेरी साड़ियाँ", "चंदेरी साड्या"),
 "Leather Toys of Indore": ("इंदौर के चमड़े के खिलौने", "इंदूरची चामडी खेळणी"),
 "Bagh Prints of Madhya Pradesh": ("मध्य प्रदेश की बाग़ छपाई", "मध्य प्रदेशची बाग छपाई"),
 "Bell Metal Ware of Datia and Tikamgarh": ("दतिया और टीकमगढ़ के घंटा-धातु बर्तन", "दतिया व टीकमगडची घंटाधातू भांडी"),
 "Maheshwar Sarees & Fabrics": ("महेश्वर साड़ियाँ और वस्त्र", "महेश्वरी साड्या व वस्त्रे"),
 "Bell Metal Ware of Datia And Tikamgarh (Logo)": ("दतिया और टीकमगढ़ के घंटा-धातु बर्तन (लोगो)", "दतिया व टीकमगडची घंटाधातू भांडी (बोधचिन्ह)"),
 "Leather Toys of Indore (LOGO)": ("इंदौर के चमड़े के खिलौने (लोगो)", "इंदूरची चामडी खेळणी (बोधचिन्ह)"),
 "Bagh Prints of Madhya Pradesh (Logo)": ("मध्य प्रदेश की बाग़ छपाई (लोगो)", "मध्य प्रदेशची बाग छपाई (बोधचिन्ह)"),
 "Gond Painting of Madhya Pradesh": ("मध्य प्रदेश की गोंड चित्रकला", "मध्य प्रदेशची गोंड चित्रकला"),
 "Wrought Iron Crafts of Dindori": ("डिंडोरी का लौह शिल्प", "डिंडोरीची लोखंडी हस्तकला"),
 "Ujjain Batik Print": ("उज्जैन बाटिक छपाई", "उज्जैन बाटिक छपाई"),
 "Gwalior Handmade Carpet": ("ग्वालियर हस्तनिर्मित कालीन", "ग्वाल्हेर हस्तनिर्मित गालिचा"),
 "Waraseoni Handloom Saree & Fabrics": ("वारासिवनी हथकरघा साड़ी और वस्त्र", "वारासिवनी हातमाग साडी व वस्त्रे"),
 "Jabalpur Stone Craft": ("जबलपुर पत्थर शिल्प", "जबलपूर दगडी हस्तकला"),
 "Chhatarpur Furniture": ("छतरपुर फ़र्नीचर", "छतरपूर फर्निचर"),
 "Khajuraho Stone Craft Of Madhya Pradesh": ("मध्य प्रदेश का खजुराहो पत्थर शिल्प", "मध्य प्रदेशची खजुराहो दगडी हस्तकला"),
 "Betul Bharewa Metal Craft": ("बैतूल भरेवा धातु शिल्प", "बैतूल भरेवा धातुकला"),
 "Gwalior Papier Mache Craft": ("ग्वालियर पेपर माशे शिल्प", "ग्वाल्हेर पेपर माशे कला"),
 "Gwalior Stone Craft": ("ग्वालियर पत्थर शिल्प", "ग्वाल्हेर दगडी हस्तकला"),
 "Panna Diamond": ("पन्ना हीरा", "पन्ना हिरा"),
 "Nagpur Orange": ("नागपुर संतरा", "नागपुरी संत्री"),
 "Bundelkhand Kathiya Gehu (Wheat)": ("बुंदेलखंड कठिया गेहूँ", "बुंदेलखंड कठिया गहू"),
 "Mahoba Desawari Pan": ("महोबा देशावरी पान", "महोबा देशावरी पान"),
}
TEXTILE = {"Chanderi Sarees", "Maheshwar Sarees & Fabrics", "Bagh Prints of Madhya Pradesh", "Bagh Prints of Madhya Pradesh (Logo)", "Ujjain Batik Print",
           "Waraseoni Handloom Saree & Fabrics", "Gwalior Handmade Carpet"}
r["giProducts"] = gi_list("gi_mp.tsv", GI_NAMES, {"MH,MP": ["Maharashtra"], "UP,MP": ["Uttar Pradesh"]}, TEXTILE)
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-MP.json", r)
print("mp core ok", len(r["giProducts"]), "GIs")
