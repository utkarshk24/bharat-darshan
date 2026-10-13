"""India overview: national officeholders, GDP metric and the overview module (data/modules/IN/overview.json)."""
import sys, glob, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

R = "IN"
NTCA = "https://ntca.gov.in/tiger-reserves/"
gdp = research("mospi_india_gdp.json")["gdp"]
allg = research("mospi_gsdp_all_2024_25.json")["FY2024-25_FY2023-24"]
ger = AP["aishe_ger_all_2021_22"]

# --- region names by English name (Kerala is now Keralam) ---
names = {}
for f in glob.glob(os.path.join(ROOT, "regions", "*.json")):
    rr = json.load(open(f))
    key = rr["name"]["en"]
    names[key] = rr
names["Kerala"] = names["Keralam"]
def rname(en):
    rr = names[en]
    return {k: v for k, v in rr["name"].items()}

ind = read("india.json")
im = ind["metrics"]
GDP_NOTE = ("MoSPI national accounts, base 2011-12 (current series), Provisional Estimates for FY2024-25. "
            "MoSPI has since released a 2022-23 base series; the 2011-12 base is used here so that it matches the State GSDP series.")
im["gdpCurrent"] = dp(gdp["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, level="national", rev="provisional", base=CUR, note=GDP_NOTE)
im["gsdpCurrent"]["note"] = "Not applicable at national level — see gdpCurrent (GDP)."

PRES = "https://presidentofindia.gov.in"
VP = "https://vicepresidentofindia.nic.in/?p=11101"
PM = "https://www.pmindia.gov.in/en/"
SPK = "https://newsonair.gov.in/lok-sabha-speaker-om-birla-reconstitutes-four-parliamentary-committees-for-2026-27/"
ind["government"] = {
    "headOfState": office("president", L("Droupadi Murmu", "द्रौपदी मुर्मु", "द्रौपदी मुर्मू"), None, "2022-07-25", "president-of-india", PRES, PRES,
                          note="Sworn in as the 15th President of India on 25 July 2022 (President's Secretariat)."),
    "headOfGovernment": office("prime-minister", L("Narendra Modi", "नरेंद्र मोदी", "नरेंद्र मोदी"), "BJP", "2024-06-09", "pmindia", PM, PM,
                               note="Third consecutive term from 9 June 2024. Named on the PMO website (news dated 12 October 2026)."),
    "others": [
        office("vice-president", L("C. P. Radhakrishnan", "सी. पी. राधाकृष्णन", "सी. पी. राधाकृष्णन"), None, None, "vice-president-of-india", VP, "https://vicepresidentofindia.nic.in",
               note="Vice-President and Chairman, Rajya Sabha (Vice-President's Secretariat, page updated 2 September 2026). Took office in September 2025."),
        office("lok-sabha-speaker", L("Om Birla", "ओम बिरला", "ओम बिर्ला"), "BJP", None, "newsonair", SPK, "https://sansad.in/ls",
               note="Speaker of the 18th Lok Sabha; most recent official mention found: 2 May 2026 (News On AIR)."),
    ],
}
ind["meta"]["lastUpdated"] = TODAY
write("india.json", ind)

# --- overview module ---
def nat(v, unit, period, ptype, src, url, note=None, rev="final", base=None):
    return dp(v, unit, period, ptype, src, url, level="national", note=note, rev=rev, base=base)

srs = NF["SRS_2021_PIB_PRID2128024"]["IN"]
plfs = AP["plfs_ur_15plus_psss"]["IN"]; lf = AP["plfs_lfpr_2025"]["IN"]
nf = NF["IN"]

gdp_years = sorted(gdp)
def gdp_pts(idx, base):
    return [nat(gdp[y][idx], "₹ crore", y, "fy", "mospi", MOSPI,
                rev={"Provisional Estimates": "provisional", "First Advance Estimates": "provisional", "First Revised Estimates": "revised",
                     "Second Revised Estimates": "revised", "Third Revised Estimates": "final", "Final Estimates": "final", "Additional Revision": "final"}[gdp[y][2]],
                base=base, note=f"{gdp[y][2]}." if y in ("FY2024-25", "FY2025-26", "FY2023-24") else None) for y in gdp_years]

total = gdp["FY2024-25"][0]
rows = sorted(allg.items(), key=lambda kv: -kv[1][0])
econ_rows = []
for i, (en, (v25, v24)) in enumerate(rows, 1):
    econ_rows.append([L(*(lambda n: (n["en"], n["hi"], n["mr"]))(rname(en))), i, v25, f"{100 * v25 / total:.2f}", f"{100 * (v25 - v24) / v24:.1f}"])

ger_rows = sorted([(k, v) for k, v in ger.items() if k != "All India"], key=lambda kv: -kv[1])
ger_tab = [[L(*(lambda n: (n["en"], n["hi"], n["mr"]))(rname(k if k != "Dadra & Nagar Haveli and Daman & Diu" else "Dadra & Nagar Haveli and Daman & Diu"))), f"{v:.1f}"] for k, v in ger_rows]

module(R, "overview", [
    prose("intro", L(
        "India is a Union of 28 States and 8 Union Territories, home to about 121 crore people at the 2011 Census. It stretches from the Himalaya and the Karakoram in the north to the Indian Ocean in the south, and from the Thar desert in the west to the hills of the North-East. The Constitution, in force since 26 January 1950, sets up a parliamentary democracy with a federal structure: the Union and the States share power through three lists of subjects, and Union Territories are governed by the Union, three of them — Delhi, Puducherry and Jammu & Kashmir — with elected legislatures.\n\nThis page brings together national reference figures and compares States and UTs where an official State-wise series exists. Each State and UT has its own profile; the four reference profiles (Maharashtra, Keralam, Delhi and Ladakh) are the most complete so far.",
        "भारत 28 राज्यों और 8 केंद्र शासित प्रदेशों का संघ है; 2011 की जनगणना में इसकी आबादी लगभग 121 करोड़ थी। यह उत्तर में हिमालय और काराकोरम से दक्षिण में हिंद महासागर तक, और पश्चिम में थार मरुस्थल से पूर्वोत्तर की पहाड़ियों तक फैला है। 26 जनवरी 1950 से लागू संविधान संघीय ढाँचे वाला संसदीय लोकतंत्र स्थापित करता है: संघ और राज्य विषयों की तीन सूचियों के माध्यम से शक्तियाँ बाँटते हैं, और केंद्र शासित प्रदेशों का शासन संघ करता है — इनमें से तीन, दिल्ली, पुदुच्चेरी और जम्मू-कश्मीर, में निर्वाचित विधानसभाएँ हैं।\n\nयह पेज राष्ट्रीय संदर्भ आँकड़ों को एक साथ लाता है और जहाँ आधिकारिक राज्यवार शृंखला उपलब्ध है, वहाँ राज्यों और केंद्र शासित प्रदेशों की तुलना करता है। हर राज्य और केंद्र शासित प्रदेश का अपना प्रोफ़ाइल है; चार संदर्भ प्रोफ़ाइल (महाराष्ट्र, केरलम, दिल्ली और लद्दाख) अब तक सबसे पूर्ण हैं।",
        "भारत हा 28 राज्ये आणि 8 केंद्रशासित प्रदेशांचा संघ आहे; 2011 च्या जनगणनेनुसार त्याची लोकसंख्या सुमारे 121 कोटी होती. उत्तरेकडील हिमालय व काराकोरमपासून दक्षिणेकडील हिंदी महासागरापर्यंत, आणि पश्चिमेकडील थरच्या वाळवंटापासून ईशान्येकडील डोंगररांगांपर्यंत तो पसरलेला आहे. 26 जानेवारी 1950 पासून लागू असलेली राज्यघटना संघराज्यीय रचनेची संसदीय लोकशाही स्थापन करते: संघ आणि राज्ये विषयांच्या तीन सूचींद्वारे अधिकार वाटून घेतात, आणि केंद्रशासित प्रदेशांचा कारभार संघ पाहतो — त्यांपैकी दिल्ली, पुदुच्चेरी आणि जम्मू-काश्मीर या तिघांना निवडून आलेली विधिमंडळे आहेत.\n\nहे पान राष्ट्रीय संदर्भ आकडेवारी एकत्र आणते आणि जिथे अधिकृत राज्यनिहाय मालिका उपलब्ध आहे तिथे राज्ये व केंद्रशासित प्रदेशांची तुलना करते. प्रत्येक राज्य व केंद्रशासित प्रदेशाचे स्वतंत्र माहितीपान आहे; चार संदर्भ माहितीपाने (महाराष्ट्र, केरळम, दिल्ली आणि लडाख) आतापर्यंत सर्वाधिक परिपूर्ण आहेत."),
        conf="Editorial"),
    facts("glance", [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), im["population2011"], "count"),
        fact("area", L("Geographical area", "भौगोलिक क्षेत्रफल", "भौगोलिक क्षेत्रफळ"), im["area"], "number"),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), im["density2011"], "number"),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), im["sexRatio2011"], "ratio", "higher-is-better"),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), im["childSexRatio2011"], "ratio", "higher-is-better"),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), im["literacyRate2011"], "percent", "higher-is-better"),
        fact("urb", L("Urban population", "शहरी जनसंख्या", "नागरी लोकसंख्या"), im["urbanisation2011"], "percent"),
        fact("gdp", L("GDP, current prices", "जीडीपी, प्रचलित मूल्य", "जीडीपी, चालू किमती"), im["gdpCurrent"], "rupeeCrore", "higher-is-better",
             previous=nat(gdp["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="revised", base=CUR)),
        fact("forest", L("Forest cover", "वन आवरण", "वनाच्छादन"), im["forestCoverPct"], "percent", "higher-is-better"),
    ], title=L("India at a glance", "भारत एक नज़र में", "भारत दृष्टिक्षेपात")),
    {"type": "officeholders", "id": "officeholders"},
    table("structure", L("How India is organised", "भारत की संरचना", "भारताची रचना"),
          [col(L("Item", "विषय", "बाब")), col(L("Count", "संख्या", "संख्या"), "right")],
          [[L("States", "राज्य", "राज्ये"), 28], [L("Union Territories", "केंद्र शासित प्रदेश", "केंद्रशासित प्रदेश"), 8],
           [L("— of which with an elected legislature", "— जिनमें निर्वाचित विधानसभा है", "— त्यांपैकी निवडून आलेले विधिमंडळ असलेले"), 3],
           [L("Zonal Councils", "क्षेत्रीय परिषदें", "विभागीय परिषदा"), 5],
           [L("Lok Sabha seats", "लोकसभा सीटें", "लोकसभा जागा"), 543]],
          "india-gov", "https://www.india.gov.in", conf="Editorial",
          note=L("Constitutional and statutory counts, to be linked to the relevant articles and notifications in review. The North Eastern Council is a separate statutory body; this site groups regions using the five Zonal Councils plus the North-East.",
                 "संवैधानिक और वैधानिक गणनाएँ; समीक्षा में इन्हें संबंधित अनुच्छेदों और अधिसूचनाओं से जोड़ा जाएगा। पूर्वोत्तर परिषद एक अलग वैधानिक निकाय है; यह साइट क्षेत्रों को पाँच क्षेत्रीय परिषदों और पूर्वोत्तर के आधार पर समूहित करती है।",
                 "घटनात्मक व वैधानिक संख्या; तपासणीत त्या संबंधित अनुच्छेद व अधिसूचनांशी जोडल्या जातील. ईशान्य परिषद ही स्वतंत्र वैधानिक संस्था आहे; हे संकेतस्थळ प्रदेशांचे गट पाच विभागीय परिषदा आणि ईशान्य यांच्या आधारे करते.")),
    {"type": "series", "id": "gdp-series", "title": L("GDP, FY2011-12 to FY2025-26", "जीडीपी, वित्त वर्ष 2011-12 से 2025-26", "जीडीपी, आ.व. 2011-12 ते 2025-26"),
     "kind": "rupeeCrore", "polarity": "higher-is-better",
     "series": [
         {"id": "current", "label": L("Current prices", "प्रचलित मूल्य", "चालू किमती"), "points": gdp_pts(0, CUR)},
         {"id": "constant", "label": L("Constant 2011-12 prices", "स्थिर 2011-12 मूल्य", "स्थिर 2011-12 किमती"), "points": gdp_pts(1, CON)},
     ],
     "note": L("MoSPI, base 2011-12, latest available revision for each year (FY2025-26 is the First Advance Estimate). MoSPI has released a new 2022-23 base series; it is not mixed in here.",
               "मोस्पी, आधार 2011-12, हर वर्ष का नवीनतम उपलब्ध संशोधन (वित्त वर्ष 2025-26 पहला अग्रिम अनुमान है)। मोस्पी ने नई 2022-23 आधार शृंखला जारी की है; उसे यहाँ मिलाया नहीं गया है।",
               "मोस्पी, आधार 2011-12, प्रत्येक वर्षाची नवीनतम उपलब्ध सुधारणा (आ.व. 2025-26 हा पहिला आगाऊ अंदाज). मोस्पीने नवी 2022-23 आधार मालिका प्रसिद्ध केली आहे; ती येथे मिसळलेली नाही.")},
    table("economies", L("State economies, FY2024-25 (GSDP at current prices)", "राज्यों की अर्थव्यवस्थाएँ, वित्त वर्ष 2024-25 (प्रचलित मूल्यों पर जीएसडीपी)", "राज्यांच्या अर्थव्यवस्था, आ.व. 2024-25 (चालू किमतींनुसार जीएसडीपी)"),
          [col(L("State / UT", "राज्य / केंद्र शासित प्रदेश", "राज्य / केंद्रशासित प्रदेश")), col(L("Rank", "क्रम", "क्रमांक"), "right"),
           col(L("GSDP (₹ crore)", "जीएसडीपी (₹ करोड़)", "जीएसडीपी (₹ कोटी)"), "right"), col(L("Share of India's GDP (%)", "भारत के जीडीपी में हिस्सा (%)", "भारताच्या जीडीपीतील वाटा (%)"), "right"),
           col(L("Growth over FY2023-24 (%)", "वित्त वर्ष 2023-24 से वृद्धि (%)", "आ.व. 2023-24 पासून वाढ (%)"), "right")],
          econ_rows, "mospi", MOSPI, period="FY2024-25",
          note=L(f"MoSPI state-wise GSDP, base 2011-12, current prices; {len(rows)} States/UTs had an FY2024-25 value at access time (Assam, Haryana, Nagaland, Ladakh, Lakshadweep and Dadra & Nagar Haveli and Daman & Diu did not). Share is computed against India's GDP for FY2024-25 (Provisional Estimates, ₹{inr(total)} crore); because State and national estimates are compiled separately, shares are indicative and need not add up to 100. Growth is nominal (current prices).",
                 f"मोस्पी का राज्यवार जीएसडीपी, आधार 2011-12, प्रचलित मूल्य; पहुँच के समय {len(rows)} राज्यों/केंद्र शासित प्रदेशों के लिए वित्त वर्ष 2024-25 का मान उपलब्ध था (असम, हरियाणा, नगालैंड, लद्दाख, लक्षद्वीप तथा दादरा और नगर हवेली और दमन और दीव का नहीं)। हिस्सा वित्त वर्ष 2024-25 के भारत के जीडीपी (अनंतिम अनुमान, ₹{inr(total)} करोड़) के सापेक्ष गणना किया गया है; राज्य और राष्ट्रीय अनुमान अलग-अलग तैयार होते हैं, इसलिए हिस्से सांकेतिक हैं और उनका योग 100 होना ज़रूरी नहीं। वृद्धि नाममात्र (प्रचलित मूल्य) है।",
                 f"मोस्पीचे राज्यनिहाय जीएसडीपी, आधार 2011-12, चालू किमती; उपलब्धतेच्या वेळी {len(rows)} राज्ये/केंद्रशासित प्रदेशांसाठी आ.व. 2024-25 चे मूल्य उपलब्ध होते (आसाम, हरियाणा, नागालँड, लडाख, लक्षद्वीप आणि दादरा व नगर हवेली आणि दमण व दीव यांचे नाही). वाटा आ.व. 2024-25 च्या भारताच्या जीडीपीच्या (तात्पुरते अंदाज, ₹{inr(total)} कोटी) तुलनेत काढला आहे; राज्य व राष्ट्रीय अंदाज स्वतंत्रपणे तयार होतात, त्यामुळे वाटे सूचक असून त्यांची बेरीज 100 असणे आवश्यक नाही. वाढ नाममात्र (चालू किमती) आहे.")),
    facts("labour", [
        fact("ur", L("Unemployment rate, 15+ (PS+SS)", "बेरोज़गारी दर, 15+ (पीएस+एसएस)", "बेरोजगारी दर, 15+ (पीएस+एसएस)"),
             nat(plfs["2025"], "%", "2025", "calendar", "plfs", MOSPI, note="PLFS annual, calendar year, usual status (PS+SS)."), "percent", "lower-is-better",
             previous=nat(plfs["2024"], "%", "2024", "calendar", "plfs", MOSPI)),
        fact("lfpr", L("Labour force participation, 15+", "श्रम बल भागीदारी, 15+", "श्रमशक्ती सहभाग, 15+"), nat(lf["person"], "%", "2025", "calendar", "plfs", MOSPI), "percent", "higher-is-better"),
        fact("lfprf", L("Labour force participation, women 15+", "श्रम बल भागीदारी, महिलाएँ 15+", "श्रमशक्ती सहभाग, महिला 15+"), nat(lf["female"], "%", "2025", "calendar", "plfs", MOSPI), "percent", "higher-is-better"),
        fact("ger", L("Gross enrolment ratio, higher education (18–23)", "सकल नामांकन अनुपात, उच्च शिक्षा (18–23)", "एकूण नोंदणी गुणोत्तर, उच्चशिक्षण (18–23)"),
             nat(28.40, "%", "2021-22", "survey", "aishe", AISHE), "percent", "higher-is-better"),
    ], title=L("Work and education", "रोज़गार और शिक्षा", "रोजगार व शिक्षण")),
    facts("health", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"), nat(srs["IMR"], "per 1,000 live births", "2021", "calendar", "srs", SRS, note="SRS 2021, via PIB (10 May 2025)."), "number", "lower-is-better"),
        fact("u5mr", L("Under-five mortality rate", "पाँच वर्ष से कम आयु की मृत्यु दर", "पाच वर्षांखालील मृत्युदर"), nat(srs["U5MR"], "per 1,000 live births", "2021", "calendar", "srs", SRS), "number", "lower-is-better"),
        fact("mmr", L("Maternal mortality ratio", "मातृ मृत्यु अनुपात", "मातामृत्यू प्रमाण"), nat(srs["MMR_2019_21"], "per 1,00,000 live births", "2019-21", "survey", "srs", SRS), "number", "lower-is-better"),
        fact("tfr", L("Total fertility rate", "कुल प्रजनन दर", "एकूण जननदर"), nat(srs["TFR"], "children per woman", "2021", "calendar", "srs", SRS), "number", "neutral"),
        fact("stunt", L("Stunted children under 5", "5 वर्ष से कम आयु के ठिगने बच्चे", "5 वर्षांखालील खुजी मुले"),
             nat(nf["stunted"][1], "%", "2019-21", "survey", "nfhs", NFHS), "percent", "lower-is-better", previous=nat(nf["stunted"][0], "%", "2015-16", "survey", "nfhs", NFHS)),
        fact("inst", L("Institutional births", "संस्थागत प्रसव", "संस्थात्मक प्रसूती"), nat(nf["institutional_N5"], "%", "2019-21", "survey", "nfhs", NFHS), "percent", "higher-is-better"),
    ], title=L("Health", "स्वास्थ्य", "आरोग्य")),
    table("ger-table", L("Higher-education GER by State/UT, 2021-22", "राज्य/केंद्र शासित प्रदेशवार उच्च शिक्षा जीईआर, 2021-22", "राज्य/केंद्रशासित प्रदेशनिहाय उच्चशिक्षण जीईआर, 2021-22"),
          [col(L("State / UT", "राज्य / केंद्र शासित प्रदेश", "राज्य / केंद्रशासित प्रदेश")), col(L("GER, 18–23 (%)", "जीईआर, 18–23 (%)", "जीईआर, 18–23 (%)"), "right")],
          ger_tab, "aishe", AISHE, period="2021-22",
          note=L("AISHE 2021-22, all categories, both sexes (via MoSPI API). India: 28.4%. Small UTs with large colleges serving neighbouring States (Chandigarh, Puducherry) show very high ratios.",
                 "एआईएसएचई 2021-22, सभी श्रेणियाँ, दोनों लिंग (मोस्पी एपीआई से)। भारत: 28.4%। पड़ोसी राज्यों के छात्रों को पढ़ाने वाले बड़े कॉलेजों वाले छोटे केंद्र शासित प्रदेशों (चंडीगढ़, पुदुच्चेरी) में अनुपात बहुत ऊँचा दिखता है।",
                 "एआयएसएचई 2021-22, सर्व प्रवर्ग, दोन्ही लिंग (मोस्पी एपीआयद्वारे). भारत: 28.4%. शेजारी राज्यांतील विद्यार्थ्यांना शिक्षण देणारी मोठी महाविद्यालये असलेल्या लहान केंद्रशासित प्रदेशांत (चंदीगड, पुदुच्चेरी) गुणोत्तर खूप जास्त दिसते.")),
    facts("heritage", [
        fact("whs", L("UNESCO World Heritage properties", "यूनेस्को विश्व धरोहर स्थल", "युनेस्को जागतिक वारसा स्थळे"), nat(45, "count", "2026", "calendar", "unesco-whc", UNESCO, note="Including Sarnath (2026)."), "number"),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"), nat(99, "count", "2026", "calendar", "indian-wetlands", RAMSAR, note="MoEFCC list as on 21 April 2026."), "number"),
        fact("tiger", L("Tiger reserves", "बाघ अभयारण्य", "व्याघ्र प्रकल्प"), nat(58, "count", "2026", "calendar", "ntca", NTCA, note="As listed by NTCA at access time."), "number"),
    ], title=L("Heritage and nature", "धरोहर और प्रकृति", "वारसा व निसर्ग")),
    lst("links", [
        it3("india", "National Portal of India", "भारत का राष्ट्रीय पोर्टल", "भारताचे राष्ट्रीय संकेतस्थळ", url="https://www.india.gov.in", src="india-gov"),
        it3("igod", "Integrated Government Online Directory", "एकीकृत सरकारी ऑनलाइन निर्देशिका", "एकात्मिक सरकारी ऑनलाइन निर्देशिका", url="https://igod.gov.in", src="igod"),
        it3("mospi", "Ministry of Statistics and Programme Implementation", "सांख्यिकी और कार्यक्रम कार्यान्वयन मंत्रालय", "सांख्यिकी व कार्यक्रम अंमलबजावणी मंत्रालय", url="https://mospi.gov.in", src="mospi"),
        it3("census", "Census of India", "भारत की जनगणना", "भारताची जनगणना", url="https://censusindia.gov.in", src="census"),
        it3("eci", "Election Commission of India", "भारत निर्वाचन आयोग", "भारत निवडणूक आयोग", url="https://www.eci.gov.in", src="eci"),
        it3("sansad", "Parliament of India", "भारत की संसद", "भारताची संसद", url="https://sansad.in", src="sansad"),
    ], title=L("Official links", "आधिकारिक लिंक", "अधिकृत दुवे"), conf="Official"),
    gaps("g", [
        (L("Per capita net national income", "प्रति व्यक्ति शुद्ध राष्ट्रीय आय", "दरडोई निव्वळ राष्ट्रीय उत्पन्न"), "mospi", "MoSPI national accounts statement (per capita NNI)."),
        (L("GDP in the new 2022-23 base", "नए 2022-23 आधार में जीडीपी", "नव्या 2022-23 आधारातील जीडीपी"), "mospi", "Show separately, never mixed with the 2011-12 base series."),
        (L("Current population (projected)", "वर्तमान जनसंख्या (अनुमानित)", "सध्याची लोकसंख्या (प्रक्षेपित)"), "mohfw-projections", "MoHFW Technical Group projection; label as Projected. Census 2027 results will replace it."),
        (L("Chief Justice of India", "भारत के मुख्य न्यायाधीश", "भारताचे सरन्यायाधीश"), "india-gov", "Add with asOf from the Supreme Court website."),
        (L("Registered GIs (national total)", "पंजीकृत जीआई (राष्ट्रीय कुल)", "नोंदणीकृत जीआय (राष्ट्रीय एकूण)"), "gi-registry", "Count from the GI Registry list as on the latest date."),
        (L("State GSDP for Assam, Haryana, Nagaland and three UTs (FY2024-25)", "असम, हरियाणा, नगालैंड और तीन केंद्र शासित प्रदेशों का जीएसडीपी (वित्त वर्ष 2024-25)", "आसाम, हरियाणा, नागालँड व तीन केंद्रशासित प्रदेशांचे जीएसडीपी (आ.व. 2024-25)"), "mospi", "Not yet in the MoSPI State series at access time."),
    ]),
])
print("india ok", len(rows), "economies", len(ger_tab), "GER rows")
