"""Shared helpers for the Phase 2 reference profiles (Keralam, Delhi, Ladakh)."""
import json, os, re
from bd import *

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "research")

MOSPI = "https://mospi.gov.in"
AISHE = "https://aishe.gov.in"
NFHS = "https://rchiips.org/nfhs"
SRS = "https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2128024&reg=48&lang=2"
PIB_CSR = "https://www.pib.gov.in/newsite/printrelease.aspx?relid=103437&reg=48&lang=2"
LS_FOREST = "https://eparlib.sansad.in/bitstream/123456789/3021702/1/AU1550_C0eysl.pdf"
RAMSAR = "https://indianwetlands.in/wp-content/uploads/library/1761126102.pdf"
UNESCO = "https://whc.unesco.org/en/statesparties/in"
GI_PDF = "https://ipindia.gov.in/frontend/pdf/gi/registered/State_wise_Registered_GI_of_India.pdf"

CUR = {"type": "current"}
CON = {"type": "constant", "baseYear": "2011-12"}
NOTE_NAS = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API. "
            "FY2024-25 is the latest year published for this region and may be revised.")


def research(name):
    return json.load(open(os.path.join(RES, name)))


AP = research("aishe_plfs.json")
NF = research("nfhs.json")


def fy_points(mo, key, idx, unit, base, note=NOTE_NAS):
    pts = []
    years = sorted(mo[key].keys())
    for y in years:
        rev = "provisional" if y in ("FY2023-24", "FY2024-25", "FY2025-26") else "final"
        pts.append(dp(mo[key][y][idx], unit, y, "fy", "mospi", MOSPI, rev=rev, base=base,
                      note=note if y == years[-1] else None))
    return pts


def gsva_shares(g):
    t = g["total"]
    pct = lambda v: 100 * v / t
    rows = [
        (L("Agriculture, livestock, forestry & fishing", "कृषि, पशुपालन, वानिकी और मत्स्य", "कृषी, पशुपालन, वनीकरण व मत्स्य"), "agri"),
        (L("Mining & quarrying", "खनन और उत्खनन", "खाणकाम व उत्खनन"), "mining"),
        (L("Manufacturing", "विनिर्माण", "उत्पादन उद्योग"), "manufacturing"),
        (L("Electricity, gas, water & utilities", "बिजली, गैस, जल और उपयोगिताएँ", "वीज, वायू, पाणी व उपयुक्त सेवा"), "utilities"),
        (L("Construction", "निर्माण", "बांधकाम"), "construction"),
        (L("Trade, repair, hotels & restaurants", "व्यापार, मरम्मत, होटल और रेस्तराँ", "व्यापार, दुरुस्ती, हॉटेल व उपाहारगृहे"), "trade_hotels"),
        (L("Transport, storage & communication", "परिवहन, भंडारण और संचार", "वाहतूक, साठवण व दळणवळण"), "transport_comm"),
        (L("Financial services", "वित्तीय सेवाएँ", "वित्तीय सेवा"), "financial"),
        (L("Real estate, dwellings & professional services", "रियल एस्टेट, आवास और पेशेवर सेवाएँ", "स्थावर मालमत्ता, निवास व व्यावसायिक सेवा"), "realestate_prof"),
        (L("Public administration", "लोक प्रशासन", "लोकप्रशासन"), "public_admin"),
        (L("Other services", "अन्य सेवाएँ", "इतर सेवा"), "other"),
    ]
    out = [[lab, f"{pct(g[k]):.2f}"] for lab, k in rows]
    prim = pct(g["agri"] + g["mining"])
    sec = pct(g["manufacturing"] + g["utilities"] + g["construction"])
    serv = 100 - prim - sec
    return out, prim, sec, serv


def sector_table(g, period="FY2024-25"):
    rows, prim, sec, serv = gsva_shares(g)
    return table("sectors", L(f"Sectoral shares of GSVA, {period} (current prices)", f"जीएसवीए में क्षेत्रवार हिस्सा, वित्त वर्ष {period[2:]} (प्रचलित मूल्य)",
                              f"जीएसव्हीएमधील क्षेत्रनिहाय वाटा, आ.व. {period[2:]} (चालू किमती)"),
                 [col(L("Sector", "क्षेत्र", "क्षेत्र")), col(L("Share of GSVA (%)", "जीएसवीए में हिस्सा (%)", "जीएसव्हीएमधील वाटा (%)"), "right")],
                 rows, "mospi", MOSPI, period=period,
                 note=L(f"Computed from MoSPI GSVA by industry (₹ lakh). Primary sector {prim:.1f}%, secondary {sec:.1f}%, services {serv:.1f}%.",
                        f"मोस्पी के उद्योगवार जीएसवीए (₹ लाख) से गणना। प्राथमिक क्षेत्र {prim:.1f}%, द्वितीयक {sec:.1f}%, सेवाएँ {serv:.1f}%।",
                        f"मोस्पीच्या उद्योगनिहाय जीएसव्हीए (₹ लाख) वरून गणना. प्राथमिक क्षेत्र {prim:.1f}%, द्वितीयक {sec:.1f}%, सेवा {serv:.1f}%.")), (prim, sec, serv)


def gdp_series(mo, label_years):
    _a, _b = label_years.split(" to ")  # "FY2011-12 to FY2024-25"
    return [
        {"type": "series", "id": "gsdp-series", "title": L(f"GSDP, {label_years}", f"जीएसडीपी, {_a.replace('FY', 'वित्त वर्ष ')} से {_b.replace('FY', 'वित्त वर्ष ')} तक",
                                                           f"जीएसडीपी, {_a.replace('FY', 'आ.व. ')} ते {_b.replace('FY', 'आ.व. ')}"),
         "kind": "rupeeCrore", "polarity": "higher-is-better",
         "series": [
             {"id": "current", "label": L("Current prices", "प्रचलित मूल्य", "चालू किमती"), "points": fy_points(mo, "gsdp", 0, "₹ crore", CUR)},
             {"id": "constant", "label": L("Constant 2011-12 prices", "स्थिर 2011-12 मूल्य", "स्थिर 2011-12 किमती"), "points": fy_points(mo, "gsdp", 1, "₹ crore", CON)},
         ],
         "note": L("Current prices include inflation; constant prices show real growth. The dip in FY2020-21 reflects the pandemic year.",
                   "प्रचलित मूल्यों में महँगाई शामिल है; स्थिर मूल्य वास्तविक वृद्धि दिखाते हैं। वित्त वर्ष 2020-21 की गिरावट महामारी वर्ष को दर्शाती है।",
                   "चालू किमतींमध्ये महागाई समाविष्ट असते; स्थिर किमती प्रत्यक्ष वाढ दाखवतात. आ.व. 2020-21 मधील घसरण महामारीच्या वर्षामुळे आहे.")},
        {"type": "series", "id": "pc-series", "title": L("Per capita NSDP", "प्रति व्यक्ति एनएसडीपी", "दरडोई एनएसडीपी"),
         "kind": "rupee", "polarity": "higher-is-better",
         "series": [
             {"id": "current", "label": L("Current prices", "प्रचलित मूल्य", "चालू किमती"), "points": fy_points(mo, "pcnsdp", 0, "₹", CUR)},
             {"id": "constant", "label": L("Constant 2011-12 prices", "स्थिर 2011-12 मूल्य", "स्थिर 2011-12 किमती"), "points": fy_points(mo, "pcnsdp", 1, "₹", CON)},
         ]},
    ]


def plfs_facts(code, name):
    ur = AP["plfs_ur_15plus_psss"][code]; ind = AP["plfs_ur_15plus_psss"]["IN"]
    lf = AP["plfs_lfpr_2025"][code]; lfi = AP["plfs_lfpr_2025"]["IN"]
    return [
        fact("ur", L("Unemployment rate, 15+ (PS+SS)", "बेरोज़गारी दर, 15+ (पीएस+एसएस)", "बेरोजगारी दर, 15+ (पीएस+एसएस)"),
             dp(ur["2025"], "%", "2025", "calendar", "plfs", MOSPI, note="PLFS annual, calendar year, usual status (PS+SS), persons 15 years and above."),
             "percent", "lower-is-better", previous=dp(ur["2024"], "%", "2024", "calendar", "plfs", MOSPI),
             national=dp(ind["2025"], "%", "2025", "calendar", "plfs", MOSPI, level="national")),
        fact("lfpr", L("Labour force participation, women 15+", "श्रम बल भागीदारी, महिलाएँ 15+", "श्रमशक्ती सहभाग, महिला 15+"),
             dp(lf["female"], "%", "2025", "calendar", "plfs", MOSPI, note=f"PLFS annual 2025, PS+SS. All persons: {lf['person']}% (India {lfi['person']}%)."),
             "percent", "higher-is-better", national=dp(lfi["female"], "%", "2025", "calendar", "plfs", MOSPI, level="national")),
    ]


def plfs_series(code, name):
    ur = AP["plfs_ur_15plus_psss"][code]; ind = AP["plfs_ur_15plus_psss"]["IN"]
    return {"type": "series", "id": "ur-series", "title": L("Unemployment rate, persons 15+ (PLFS)", "बेरोज़गारी दर, 15+ आयु (पीएलएफ़एस)", "बेरोजगारी दर, 15+ वय (पीएलएफएस)"),
            "kind": "percent", "polarity": "lower-is-better",
            "series": [
                {"id": code.lower(), "label": name, "points": [dp(ur[y], "%", y, "calendar", "plfs", MOSPI, note="PS+SS, calendar year.") for y in sorted(ur)]},
                {"id": "in", "label": L("India", "भारत", "भारत"), "points": [dp(ind[y], "%", y, "calendar", "plfs", MOSPI, level="national") for y in sorted(ind)]},
            ]}


def aishe_block(code, name):
    ger = AP["aishe_ger"][code]
    ys = sorted(ger)
    f = facts("f", [
        fact("ger", L("Gross enrolment ratio, higher education (18–23)", "सकल नामांकन अनुपात, उच्च शिक्षा (18–23)", "एकूण नोंदणी गुणोत्तर, उच्चशिक्षण (18–23)"),
             dp(ger[ys[-1]], "%", ys[-1], "survey", "aishe", AISHE, note="AISHE, all categories, both sexes (via MoSPI API)."), "percent", "higher-is-better",
             previous=dp(ger[ys[-2]], "%", ys[-2], "survey", "aishe", AISHE), national=dp(28.40, "%", "2021-22", "survey", "aishe", AISHE, level="national")),
        fact("univ", L("Universities", "विश्वविद्यालय", "विद्यापीठे"), dp(AP["aishe_universities_2021_22"].get(code), "count", "2021-22", "survey", "aishe", AISHE, note=None if AP["aishe_universities_2021_22"].get(code) is not None else "Not reported for this region in AISHE 2021-22 as returned by the MoSPI API."), "number"),
        fact("coll", L("Colleges", "कॉलेज", "महाविद्यालये"), dp(AP["aishe_colleges_2021_22"].get(code), "count", "2021-22", "survey", "aishe", AISHE, note=None if AP["aishe_colleges_2021_22"].get(code) is not None else "Not reported for this region in AISHE 2021-22 as returned by the MoSPI API."), "number"),
    ])
    s = {"type": "series", "id": "ger-series", "title": L(f"Higher-education GER, {ys[0]} to {ys[-1]}", f"उच्च शिक्षा जीईआर, {ys[0]} से {ys[-1]}", f"उच्चशिक्षण जीईआर, {ys[0]} ते {ys[-1]}"),
         "kind": "percent", "polarity": "higher-is-better",
         "series": [{"id": code.lower(), "label": name, "points": [dp(ger[y], "%", y, "survey", "aishe", AISHE) for y in ys]}]}
    return f, s


def nfhs_facts(code):
    n = NF[code]; i = NF["IN"]
    def nf(id, lab, key, pol="lower-is-better"):
        prev = dp(n[key][0], "%", "2015-16", "survey", "nfhs", NFHS) if n[key][0] is not None else None
        return fact(id, lab, dp(n[key][1], "%", "2019-21", "survey", "nfhs", NFHS, note="NFHS-5, children under 5 (via MoSPI API)."), "percent", pol,
                    previous=prev, national=dp(i[key][1], "%", "2019-21", "survey", "nfhs", NFHS, level="national"))
    return [
        nf("stunt", L("Stunted children under 5", "5 वर्ष से कम आयु के ठिगने बच्चे", "5 वर्षांखालील खुजी मुले"), "stunted"),
        nf("waste", L("Wasted children under 5", "5 वर्ष से कम आयु के दुबले (वेस्टेड) बच्चे", "5 वर्षांखालील कृश मुले"), "wasted"),
        nf("under", L("Underweight children under 5", "5 वर्ष से कम आयु के कम वज़न वाले बच्चे", "5 वर्षांखालील कमी वजनाची मुले"), "underweight"),
        fact("inst", L("Institutional births", "संस्थागत प्रसव", "संस्थात्मक प्रसूती"),
             dp(n["institutional_N5"], "%", "2019-21", "survey", "nfhs", NFHS, note="NFHS-5, births in the five years before the survey."), "percent", "higher-is-better",
             national=dp(i["institutional_N5"], "%", "2019-21", "survey", "nfhs", NFHS, level="national")),
    ]


def ev(id, year, when, label, detail=None):
    e = {"id": id, "year": year, "when": when, "label": label}
    if detail:
        e["detail"] = detail
    return e


def timeline(events):
    return {"type": "timeline", "id": "t", "title": L("Timeline", "समयरेखा", "कालरेषा"), "sourceId": None, "url": None,
            "accessDate": None, "confidence": "Editorial", "events": events}


def it3(id, en, hi, mr, d=None, m=None, url=None, src=None):
    """item with trilingual name; d and m are (en, hi, mr) tuples."""
    return item(id, L(en, hi, mr), detail=L(*d) if d else None, meta=L(*m) if m else None, url=url, src=src)


def emergency_table(where):
    return table("numbers", L("Emergency numbers", "आपातकालीन नंबर", "आपत्कालीन क्रमांक"),
                 [col(L("Service", "सेवा", "सेवा")), col(L("Number", "नंबर", "क्रमांक"), "right")],
                 [[L("Emergency response (police, fire, ambulance)", "आपातकालीन सहायता (पुलिस, अग्निशमन, एंबुलेंस)", "आपत्कालीन मदत (पोलीस, अग्निशमन, रुग्णवाहिका)"), "112"],
                  [L("Ambulance", "एंबुलेंस", "रुग्णवाहिका"), "108"],
                  [L("Women's helpline", "महिला हेल्पलाइन", "महिला हेल्पलाइन"), "181"],
                  [L("Child helpline", "चाइल्ड हेल्पलाइन", "चाइल्ड हेल्पलाइन"), "1098"],
                  [L("Cybercrime", "साइबर अपराध", "सायबर गुन्हे"), "1930"],
                  [L("Tourist helpline (Ministry of Tourism)", "पर्यटक हेल्पलाइन (पर्यटन मंत्रालय)", "पर्यटक हेल्पलाइन (पर्यटन मंत्रालय)"), "1800-11-1363"]],
                 "india-gov", "https://www.india.gov.in", conf="Official", access=None,
                 note=L(f"National numbers that work in {where[0]}.", f"राष्ट्रीय नंबर जो {where[1]} में काम करते हैं।", f"{where[2]}मध्ये चालणारे राष्ट्रीय क्रमांक."))


def gi_list(path, names, shared_map, textile=()):
    out = []
    for line in open(os.path.join(RES, path)):
        app, name, cat, date, states = line.rstrip("\n").split("\t")
        hi, mr = names[name]
        cats = [cat] + (["textile"] if name in textile else [])
        g = {"id": re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-"), "name": L(name, hi, mr), "categories": cats,
             "applicationNo": app, "filingDate": date, "registrationYear": None, "region": None, "description": None,
             "sourceId": "gi-registry", "url": GI_PDF, "revisionStatus": "final", "confidence": "Official",
             "note": "Registered GI as listed by the GI Registry (as on 31 Dec 2025). Date shown is the filing date."}
        if not date:
            g["filingDate"] = None
            g["note"] = "Registered GI as listed by the GI Registry (as on 31 Dec 2025). The filing date printed in the registry list is not a valid past date, so it is not shown."
        if states in shared_map:
            g["sharedWith"] = shared_map[states]
        out.append(g)
    return out


def office(role, name, party, since, src, url, verify, conf="Official", note=None, rev="final"):
    o = {"role": role, "name": name, "party": party, "since": since, "asOf": TODAY, "sourceId": src, "url": url,
         "verifyUrl": verify, "revisionStatus": rev, "confidence": conf}
    if note:
        o["note"] = note
    return o


def office_todo(role, src, verify, note):
    return {"role": role, "name": None, "party": None, "since": None, "asOf": None, "sourceId": src, "url": None,
            "verifyUrl": verify, "revisionStatus": "TODO", "confidence": "Official", "note": note}


def proj(id, name, objective, sector, agency, cost, costnote, costperiod, start, completion, status, src, url, challenges=None, conf="Official"):
    p = {"id": id, "name": name, "objective": objective, "sector": sector, "agency": agency,
         "start": start, "completion": completion, "status": status, "asOf": TODAY, "sourceId": src, "url": url, "confidence": conf}
    if cost is not None:
        p["cost"] = dp(cost, "₹ crore", costperiod, "calendar", src, url, note=costnote)
    if challenges:
        p["challenges"] = challenges
    return p
