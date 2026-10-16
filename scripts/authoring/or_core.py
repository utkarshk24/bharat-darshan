"""Odisha — Phase 3 profile: core metrics, identity, officeholders, projects, GIs.
Run with BD_TODAY=2026-10-16."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
GOV = "https://www.newsonair.gov.in/dr-hari-babu-kambhampati-sworn-in-as-27th-governor-of-odisha"
GOV_NEXT = "https://newsonair.gov.in/prez-murmu-appoints-six-governors-rajendra-vishwanath-arlekar-moved-to-tamil-nadu-op-mathur-to-keralam/"
CM = "https://newsonair.gov.in/odisha-bjp-to-form-government-as-mohan-charan-majhi-sworn-in-as-cm-ending-24-year-bjd-rule"
SPK = "https://odishabytes.com/odisha-assembly-gets-its-2nd-woman-speaker-as-surama-padhy-elected-unopposed/"
SEMI = "https://www.pmindia.gov.in/en/news_updates/cabinet-approves-semiconductor-manufacturing-units-in-odisha-punjab-and-andhra-pradesh-with-an-outlay-of-rs-4600-crore"

mo = research("mospi_or.json")
r = read("regions/IN-OR.json")
m = r["metrics"]
m["population2011"] = dp(41974218, "persons", "2011", "census", "census", PYD,
    note="Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. Males 2,12,12,136; females 2,07,62,082.")
m["area"] = dp(155707, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(270, "persons per km²", "2011", "census", "census", PYD,
    note="Calculated: Census 2011 population 4,19,74,218 ÷ area 1,55,707 km² = 269.6.")
m["sexRatio2011"] = dp(979, "females per 1000 males", "2011", "census", "census", PYD, note="Puducherry DES state-wise table citing ORGI (972 in 2001).")
m["childSexRatio2011"] = dp(941, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 953 in 2001.")
m["literacyRate2011"] = dp(72.9, "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
    note="Not shown: no official State or Union publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
m["gsdpCurrent"] = dp(mo["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25: ₹{inr(mo['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(mo['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(33.67, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 52,433.56 km² ÷ geographical area 1,55,707 km².")

r["officialPortal"] = "https://odisha.gov.in"


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Sambar", "सांभर", "सांबर", "Rusa unicolor"),
    "bird": sym("Indian roller", "नीलकंठ", "नीलकंठ (चास)", "Coracias benghalensis"),
    "tree": sym("Peepal (Ashwattha)", "पीपल (अश्वत्थ)", "पिंपळ (अश्वत्थ)", "Ficus religiosa"),
}

r["government"] = {
    "headOfState": office("governor", L("Hari Babu Kambhampati", "हरि बाबू कंभमपति", "हरी बाबू कंभमपती"), None, "2025-01-03",
                          "newsonair", GOV, "https://rajbhavanodisha.gov.in",
                          note="Sworn in as the 27th Governor of Odisha at Raj Bhavan, Bhubaneswar, on 3 January 2025 by Orissa High Court Chief Justice Chakradhari Sharan Singh (News On AIR). The President has since appointed Braj Mohan Ram as Governor of Odisha (communiqué reported on 13 October 2026); he had not been sworn in when this card was checked."),
    "headOfGovernment": office("chief-minister", L("Mohan Charan Majhi", "मोहन चरण माझी", "मोहन चरण माझी"), "BJP", "2024-06-12",
                               "newsonair", CM, "https://cmo.odisha.gov.in",
                               note="Sworn in on 12 June 2024 at Janata Maidan, Bhubaneswar, heading the State's first BJP government (News On AIR)."),
    "others": [
        office("deputy-chief-minister", L("Kanak Vardhan Singh Deo", "कनक वर्धन सिंह देव", "कनक वर्धन सिंह देव"), "BJP", "2024-06-12", "newsonair", CM, "https://odisha.gov.in",
               note="Sworn in with the Chief Minister on 12 June 2024 (News On AIR)."),
        office("deputy-chief-minister", L("Pravati Parida", "प्रभाती परिडा", "प्रभाती परिडा"), "BJP", "2024-06-12", "newsonair", CM, "https://odisha.gov.in",
               note="Sworn in with the Chief Minister on 12 June 2024 (News On AIR)."),
        office("speaker", L("Surama Padhy", "सुरमा पाढ़ी", "सुरमा पाढी"), "BJP", "2024-06-20", "odishabytes", SPK, "https://odishaassembly.nic.in",
               conf="Third-party verified",
               note="Elected unopposed on 20 June 2024; MLA from Ranpur and the second woman Speaker of the Assembly, after Pramila Mallik (OdishaBytes)."),
    ],
}

r["projects"] = [
    proj("sicsem-fab", L("SiCSem silicon-carbide semiconductor unit, Bhubaneswar", "सिकसेम सिलिकॉन कार्बाइड सेमीकंडक्टर इकाई, भुवनेश्वर", "सिकसेम सिलिकॉन कार्बाइड सेमीकंडक्टर प्रकल्प, भुवनेश्वर"),
         L("A compound-semiconductor fabrication unit at Info Valley, Bhubaneswar, with technology from Clas-SiC Wafer Fab of the UK — described by the Union Cabinet as the country's first commercial compound fab — with planned capacity of 60,000 wafers and 96 million packaged units a year.",
           "भुवनेश्वर की इन्फ़ो वैली में ब्रिटेन की क्लास-एसआईसी वेफ़र फ़ैब की तकनीक से कंपाउंड सेमीकंडक्टर निर्माण इकाई — केंद्रीय मंत्रिमंडल के अनुसार देश की पहली व्यावसायिक कंपाउंड फ़ैब — जिसकी नियोजित क्षमता प्रति वर्ष 60,000 वेफ़र और 9.6 करोड़ पैकेज्ड इकाइयाँ है।",
           "भुवनेश्वरच्या इन्फो व्हॅलीत ब्रिटनच्या क्लास-एसआयसी वेफर फॅबच्या तंत्रज्ञानाने उभारला जाणारा कंपाउंड सेमीकंडक्टर निर्मिती प्रकल्प — केंद्रीय मंत्रिमंडळानुसार देशातील पहिली व्यावसायिक कंपाउंड फॅब — ज्याची नियोजित क्षमता दरवर्षी 60,000 वेफर्स व 9.6 कोटी पॅकेज्ड युनिट्स आहे."),
         "industry", "SiCSem Private Limited (India Semiconductor Mission)", None, None, None, "Approved 12 August 2025", None, "Announced", "pmindia", SEMI),
    proj("3dgs-packaging", L("3D Glass Solutions advanced packaging unit, Bhubaneswar", "3डी ग्लास सॉल्यूशंस उन्नत पैकेजिंग इकाई, भुवनेश्वर", "3डी ग्लास सोल्यूशन्स प्रगत पॅकेजिंग प्रकल्प, भुवनेश्वर"),
         L("An advanced semiconductor packaging and embedded glass-substrate unit at Info Valley, approved together with the SiCSem unit. The Cabinet gave a combined investment of about ₹4,600 crore for the four units approved that day in Odisha, Punjab and Andhra Pradesh, without a break-up by unit.",
           "इन्फ़ो वैली में उन्नत सेमीकंडक्टर पैकेजिंग और एम्बेडेड ग्लास-सब्सट्रेट इकाई, जिसे सिकसेम इकाई के साथ मंज़ूरी मिली। मंत्रिमंडल ने उस दिन ओडिशा, पंजाब और आंध्र प्रदेश में मंज़ूर चार इकाइयों के लिए लगभग ₹4,600 करोड़ का संयुक्त निवेश बताया, इकाईवार विभाजन के बिना।",
           "इन्फो व्हॅलीतील प्रगत सेमीकंडक्टर पॅकेजिंग व एम्बेडेड काच-सब्सट्रेट प्रकल्प, ज्याला सिकसेम प्रकल्पासोबत मंजुरी मिळाली. मंत्रिमंडळाने त्या दिवशी ओडिशा, पंजाब व आंध्र प्रदेशात मंजूर केलेल्या चार प्रकल्पांसाठी सुमारे ₹4,600 कोटींची एकत्रित गुंतवणूक सांगितली, प्रकल्पनिहाय विभागणीशिवाय."),
         "industry", "3D Glass Solutions Inc. (India Semiconductor Mission)", None, None, None, "Approved 12 August 2025", None, "Announced", "pmindia", SEMI),
]

GI_NAMES = {
 "Ganjam Kewda Flower": ("गंजाम केवड़ा फूल", "गंजाम केवडा फूल"),
 "Kandhamal Haladi": ("कंधमाल हल्दी", "कंधमाल हळद"),
 "Nayagarh Kanteimundi Brinjal": ("नयागढ़ कंटेइमुंडी बैंगन", "नयागड कंटेइमुंडी वांगे"),
 "Koraput Kalajeera Rice": ("कोरापुट कालाजीरा चावल", "कोरापुट कालाजीरा तांदूळ"),
 "Odisha Rasagola": ("ओडिशा रसगोला", "ओडिशा रसगोला"),
 "Kendrapara Rasabali": ("केंद्रापाड़ा रसाबली", "केंद्रापाडा रसाबली"),
 "Odisha Khajuri Guda": ("ओडिशा खजूरी गुड़", "ओडिशा खजुरी गूळ"),
 "Dhenkanal Magji": ("ढेंकानाल मगजी", "ढेंकानाल मगजी"),
 "Similipal Kai Chutney of Odisha": ("ओडिशा की सिमलीपाल काई चटनी", "ओडिशाची सिमलीपाल काई चटणी"),
 "Kotpad Handloom Fabric": ("कोटपाड हथकरघा वस्त्र", "कोटपाड हातमाग वस्त्र"),
 "Orissa Ikat": ("उड़ीसा इकत", "ओरिसा इकत"),
 "Pipli Applique Work": ("पिपली एप्लिक काम", "पिपली ऍप्लिक काम"),
 "Konark Stone Carving": ("कोणार्क पत्थर नक्काशी", "कोणार्क दगडी कोरीवकाम"),
 "Orissa Pattachitra": ("उड़ीसा पट्टचित्र", "ओरिसा पट्टचित्र"),
 "Khandua Saree And Fabrics": ("खंडुआ साड़ी और वस्त्र", "खंडुआ साडी व वस्त्र"),
 "Gopalpur Tussar Fabrics": ("गोपालपुर तसर वस्त्र", "गोपालपूर टसर वस्त्र"),
 "Dhalapathar Parda & Fabrics": ("ढलपाथर पर्दा और वस्त्र", "ढलपाथर पडदा व वस्त्र"),
 "Sambalpuri Bandha Saree & Fabrics": ("संबलपुरी बांधा साड़ी और वस्त्र", "संबलपुरी बांधा साडी व वस्त्र"),
 "Bomkai Saree & Fabrics": ("बोमकाई साड़ी और वस्त्र", "बोमकाई साडी व वस्त्र"),
 "Habaspuri Saree & Fabrics": ("हबासपुरी साड़ी और वस्त्र", "हबासपुरी साडी व वस्त्र"),
 "Berhampur Patta (Phoda Kumbha) Saree & Joda": ("बरहमपुर पट्ट (फोड़ा कुंभ) साड़ी और जोड़ा", "बेरहमपूर पट्ट (फोडा कुंभ) साडी व जोडा"),
 "Orissa Pattachitra (Logo)": ("उड़ीसा पट्टचित्र (लोगो)", "ओरिसा पट्टचित्र (बोधचिन्ह)"),
 "Kapadaganda: Dungaria Kondh Embroidery Shawl": ("कपड़गंडा: डोंगरिया कोंध कढ़ाई शॉल", "कपडगंडा: डोंगरिया कोंध भरतकाम शाल"),
 "Painting of Lanjia Saura (IDITAL), Odisha": ("ओडिशा की लांजिया सौरा चित्रकला (इडिताल)", "ओडिशाची लांजिया सौरा चित्रकला (इडिताल)"),
 "Cuttack Rupa Tarakasi (Silver Filigree)": ("कटक रूपा तारकशी (चाँदी की फ़िलिग्री)", "कटक रूपा तारकशी (चांदीचे जाळीकाम)"),
 "Ganjam Kewda Rooh": ("गंजाम केवड़ा रूह", "गंजाम केवडा रूह"),
}
TEXTILE = {"Kotpad Handloom Fabric", "Orissa Ikat", "Pipli Applique Work", "Khandua Saree And Fabrics", "Gopalpur Tussar Fabrics",
           "Dhalapathar Parda & Fabrics", "Sambalpuri Bandha Saree & Fabrics", "Bomkai Saree & Fabrics", "Habaspuri Saree & Fabrics",
           "Berhampur Patta (Phoda Kumbha) Saree & Joda", "Kapadaganda: Dungaria Kondh Embroidery Shawl"}
r["giProducts"] = gi_list("gi_or.tsv", GI_NAMES, {}, TEXTILE)
for g in r["giProducts"]:
    if "&" in g["applicationNo"]:
        g["note"] += " The registry lists two application numbers for this GI; the date shown is the earlier filing."
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-OR.json", r)
print("or core ok", len(r["giProducts"]), "GIs")
