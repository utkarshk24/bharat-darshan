import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

r = read("regions/IN-LA.json")
r["officialPortal"] = "https://ladakh.gov.in"
r.pop("localName", None)  # Tibetan-script font not bundled yet; avoid tofu
m = r["metrics"]
m["population2011"] = todo("persons", "2011", "census", "census",
    "Census 2011 PCA for Leh and Kargil districts (then in Jammu & Kashmir). District Kargil's website gives 1,40,802 for Kargil; an official Leh figure was not retrievable at access time, so no total is shown.")
m["area"] = todo("km²", "2023", "calendar", "survey-of-india",
    "Official figures differ: India's map includes areas under the occupation of Pakistan and China, while district websites give administered areas (Kargil 14,036 km²). Record the Survey of India figure with a note on what it covers.")
m["density2011"] = todo("persons per km²", "2011", "census", "census", "Depends on an agreed area figure; Census 2011 district PCA.")
m["sexRatio2011"] = todo("females per 1000 males", "2011", "census", "census", "Census 2011 PCA (Leh + Kargil). District websites carry conflicting older figures.")
m["childSexRatio2011"] = todo("girls per 1000 boys (0–6 yrs)", "2011", "census", "census", "Census 2011 PCA (Leh + Kargil).")
m["literacyRate2011"] = todo("%", "2011", "census", "census", "Census 2011 PCA (Leh + Kargil).")
m["urbanisation2011"] = todo("%", "2011", "census", "census", "Census 2011 PCA (Leh + Kargil).")
m["gsdpCurrent"] = todo("₹ crore", "FY2024-25", "fy", "mospi",
    "MoSPI does not publish a separate GSDP series for Ladakh (data before 2019 is within Jammu & Kashmir). Check the UT Administration's statistics directorate.", base=CUR)
m["perCapitaNsdpCurrent"] = todo("₹", "FY2024-25", "fy", "mospi", "Not published by MoSPI for Ladakh.", base=CUR)
m["forestCoverPct"] = todo("% of geographical area", "2023", "calendar", "fsi",
    "ISFR 2023 forest cover is 2,285.92 km² (Lok Sabha AU1550), but the percentage depends on which geographical area is used; see the Nature module.")


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


r["symbols"] = {
    "animal": sym("Snow leopard", "हिम तेंदुआ", "हिमबिबट्या", "Panthera uncia"),
    "bird": sym("Black-necked crane", "काली गर्दन वाला सारस", "काळ्या मानेचा करकोचा", "Grus nigricollis"),
}

NOA = "https://www.newsonair.gov.in/former-delhi-lieutenant-governor-vinai-kumar-saxena-sworn-in-as-4th-lieutenant-governor-of-ladakh"
LAG = "https://ladakh.gov.in/shri-saxena-set-to-take-oath-as-new-lg-of-ladakh-on-13th-march-shri-saxena-succeeds-shri-kavinder-gupta-as-4th-lg-of-ut-ladakh/"
r["government"] = {
    "headOfState": office("lieutenant-governor", L("Vinai Kumar Saxena", "विनय कुमार सक्सेना", "विनय कुमार सक्सेना"), None, "2026-03-13",
                          "newsonair", NOA, "https://ladakh.gov.in",
                          note="Sworn in on 13 March 2026 as the 4th Lieutenant Governor of Ladakh, succeeding Kavinder Gupta (News On AIR; UT Administration of Ladakh). Formerly Lieutenant Governor of Delhi."),
    "headOfGovernment": None,
    "others": [],
}

LS_ZOJILA = "https://eparlib.nic.in/bitstream/123456789/2980199/1/AU2921_SM4WZv.pdf"
r["projects"] = [
    proj("zojila", L("Zojila Tunnel", "ज़ोजिला सुरंग", "झोजिला बोगदा"),
         L("A 13.153 km road tunnel under the Zoji La pass on the Srinagar–Kargil–Leh highway, with approach roads making a 30.18 km project, to give Ladakh all-weather road access from the Kashmir valley. It links Sonamarg in Jammu & Kashmir with the Drass side in Ladakh.",
           "श्रीनगर–कारगिल–लेह राजमार्ग पर ज़ोजिला दर्रे के नीचे 13.153 किमी लंबी सड़क सुरंग; पहुँच मार्गों सहित परियोजना 30.18 किमी की है। उद्देश्य कश्मीर घाटी से लद्दाख तक हर मौसम में सड़क संपर्क देना है। यह जम्मू-कश्मीर के सोनमर्ग को लद्दाख के द्रास की ओर से जोड़ती है।",
           "श्रीनगर–कारगिल–लेह महामार्गावर झोजिला खिंडीखालून जाणारा 13.153 किमीचा रस्ता-बोगदा; जोडरस्त्यांसह प्रकल्प 30.18 किमीचा आहे. काश्मीर खोऱ्यातून लडाखपर्यंत बारमाही रस्ते संपर्क देणे हा उद्देश. तो जम्मू-काश्मीरमधील सोनमर्गला लडाखमधील द्रासच्या बाजूशी जोडतो."),
         "transport", "NHIDCL", 6809.69, "total project cost ₹6,809.69 crore, as stated in Parliament in August 2024", "2024", None,
         "Scheduled for 29 September 2026 (as of August 2024)", "Under Construction", "sansad", LS_ZOJILA,
         challenges=L("Physical progress was 52.13% in August 2024. Later news reports suggest the completion date has slipped; an official update is needed.",
                      "अगस्त 2024 में भौतिक प्रगति 52.13% थी। बाद की ख़बरों के अनुसार पूरा होने की तारीख़ आगे खिसकी है; आधिकारिक अद्यतन चाहिए।",
                      "ऑगस्ट 2024 मध्ये प्रत्यक्ष प्रगती 52.13% होती. नंतरच्या वृत्तांनुसार पूर्णत्वाची तारीख पुढे गेली आहे; अधिकृत अद्ययावत माहिती हवी.")),
]

GI_NAMES = {
    "Ladakh Seabuckthorn": ("लद्दाख सीबकथॉर्न", "लडाख सीबकथॉर्न"),
    "Ladakh Raktsey Karpo Apricot": ("लद्दाख रक्त्से कार्पो ख़ुबानी", "लडाख रक्त्से कार्पो जर्दाळू"),
    "Pashmina Wool of Ladakh": ("लद्दाख का पश्मीना ऊन", "लडाखची पश्मिना लोकर"),
    "Ladakh Shingskos (Wood Carving)": ("लद्दाख शिंगस्कोस (काष्ठ नक़्क़ाशी)", "लडाख शिंगस्कोस (लाकडी कोरीवकाम)"),
}
r["giProducts"] = gi_list("gi_la.tsv", GI_NAMES, {}, textile={"Pashmina Wool of Ladakh"})
r["meta"] = {"lastUpdated": TODAY, "editorialStatus": "draft"}
write("regions/IN-LA.json", r)
print("la core ok")
