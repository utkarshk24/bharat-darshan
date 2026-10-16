"""Comparison prototype data: data/compare/indicators.json.
Every indicator uses one period for all regions (period hygiene). Missing values are TODO, never estimated."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

REGIONS = ["IN-MH", "IN-TN", "IN-UP", "IN-KL", "IN-KA", "IN-GJ", "IN-WB", "IN-AP", "IN-TG", "IN-RJ", "IN-MP", "IN-BR", "IN-DL", "IN-LA"]
SHORT = {c: c[3:] for c in REGIONS}
reg = {c: read(f"regions/{c}.json") for c in REGIONS}
ind = read("india.json")
mo = {"MH": research("mospi.json"), "KL": research("mospi_kl.json"), "DL": research("mospi_dl.json"),
      "TN": research("mospi_tn.json"), "UP": research("mospi_up.json"),
      **{k: research(f"mospi_{k.lower()}.json") for k in ("KA", "GJ", "WB", "AP", "TG", "RJ", "MP", "BR")}}
gdp = research("mospi_india_gdp.json")["gdp"]
srs = NF["SRS_2021_PIB_PRID2128024"]
SRS_TN = {"MMR_2019_21": 49, "U5MR": 14, "NMR": 9}


def metric(key):
    """Census-type metrics straight from the region files (same period everywhere)."""
    return {c: reg[c]["metrics"][key] for c in REGIONS}


def gsdp_fy(code, fy, idx=0, unit="₹ crore", key="gsdp", base=CUR):
    s = SHORT[code]
    if s not in mo or fy not in mo[s][key]:
        return todo(unit, fy, "fy", "mospi", "Not published by MoSPI for this region/year at access time.", base=base)
    return dp(mo[s][key][fy][idx], unit, fy, "fy", "mospi", MOSPI, rev="provisional", base=base,
              note="MoSPI state-wise estimates, base 2011-12 (current series).")


def share(code):
    v = gsdp_fy(code, "FY2024-25")
    if v["value"] is None:
        return todo("% of India's GDP", "FY2024-25", "fy", "mospi", "No FY2024-25 GSDP in the MoSPI series.", base=CUR)
    return dp(round(100 * v["value"] / gdp["FY2024-25"][0], 2), "% of India's GDP", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
              note=f"Computed: GSDP ÷ India's GDP for FY2024-25 (Provisional Estimates, ₹{inr(gdp['FY2024-25'][0])} crore), both MoSPI base 2011-12, current prices.")


def real_growth(code):
    s = SHORT[code]
    if s not in mo or "FY2024-25" not in mo[s]["gsdp"]:
        return todo("%", "FY2024-25", "fy", "mospi", "No FY2024-25 GSDP in the MoSPI series.", base=CON)
    a, b = mo[s]["gsdp"]["FY2024-25"][1], mo[s]["gsdp"]["FY2023-24"][1]
    return dp(round(100 * (a / b - 1), 1), "%", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON,
              note="Computed from GSDP at constant 2011-12 prices, FY2024-25 over FY2023-24 (MoSPI).")


def plfs(code, kind):
    s = SHORT[code]
    if kind == "ur":
        return dp(AP["plfs_ur_15plus_psss"][s]["2025"], "%", "2025", "calendar", "plfs", MOSPI, note="PLFS annual, calendar year, PS+SS, persons 15+.")
    return dp(AP["plfs_lfpr_2025"][s]["female"], "%", "2025", "calendar", "plfs", MOSPI, note="PLFS annual 2025, PS+SS, women 15+.")


def ger(code):
    s = SHORT[code]
    return dp(AP["aishe_ger"][s]["2021-22"], "%", "2021-22", "survey", "aishe", AISHE, note="AISHE 2021-22, all categories, both sexes.")


def nfhs(code, key, n5only=False):
    s = SHORT[code]
    v = NF[s]["institutional_N5"] if key == "inst" else NF[s][key][1]
    return dp(v, "%", "2019-21", "survey", "nfhs", NFHS, note="NFHS-5, rural + urban (via MoSPI API).")


def srs_v(code, key, period):
    s = SHORT[code]
    vals = SRS_TN if s == "TN" else srs.get(s, {})
    unit = "per 1,00,000 live births" if key.startswith("MMR") else "per 1,000 live births"
    ptype = "survey" if "-" in period else "calendar"
    if key not in vals:
        return todo(unit, period, ptype, "srs", "Not reported for this region in the SRS release used (PIB, 10 May 2025).")
    return dp(vals[key], unit, period, ptype, "srs", SRS, note="SRS, as reported by PIB on 10 May 2025.")


def I(id, label, kind, polarity, period, values, national, note=None):
    d = {"id": id, "label": label, "kind": kind, "polarity": polarity, "period": period, "values": values, "national": national}
    if note:
        d["note"] = note
    return d


im = ind["metrics"]
groups = [
    {"id": "people", "label": L("People (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), "indicators": [
        I("population", L("Population", "जनसंख्या", "लोकसंख्या"), "count", "neutral", "2011", metric("population2011"), im["population2011"]),
        I("density", L("Population density (per km²)", "जनसंख्या घनत्व (प्रति किमी²)", "लोकसंख्या घनता (दर किमी²)"), "number", "neutral", "2011", metric("density2011"), im["density2011"]),
        I("sexRatio", L("Sex ratio (women per 1,000 men)", "लिंगानुपात (प्रति 1,000 पुरुषों पर महिलाएँ)", "लिंग गुणोत्तर (दर 1,000 पुरुषांमागे स्त्रिया)"), "ratio", "higher-is-better", "2011", metric("sexRatio2011"), im["sexRatio2011"]),
        I("csr", L("Child sex ratio, 0–6", "शिशु लिंगानुपात, 0–6", "बाल लिंग गुणोत्तर, 0–6"), "ratio", "higher-is-better", "2011", metric("childSexRatio2011"), im["childSexRatio2011"]),
        I("literacy", L("Literacy rate (%)", "साक्षरता दर (%)", "साक्षरता दर (%)"), "percent", "higher-is-better", "2011", metric("literacyRate2011"), im["literacyRate2011"]),
        I("urban", L("Urban population (%)", "शहरी जनसंख्या (%)", "नागरी लोकसंख्या (%)"), "percent", "neutral", "2011", metric("urbanisation2011"), im["urbanisation2011"]),
    ]},
    {"id": "economy", "label": L("Economy and work", "अर्थव्यवस्था और रोज़गार", "अर्थव्यवस्था व रोजगार"), "indicators": [
        I("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"), "rupeeCrore", "neutral", "FY2024-25",
          {c: gsdp_fy(c, "FY2024-25") for c in REGIONS}, im["gdpCurrent"],
          note=L("India column shows GDP for the same year.", "भारत वाले कॉलम में उसी वर्ष का जीडीपी है।", "भारत स्तंभात त्याच वर्षाचे जीडीपी आहे.")),
        I("share", L("Share of India's GDP (%)", "भारत के जीडीपी में हिस्सा (%)", "भारताच्या जीडीपीतील वाटा (%)"), "percent", "neutral", "FY2024-25", {c: share(c) for c in REGIONS}, None),
        I("realGrowth", L("Real GSDP growth (%)", "वास्तविक जीएसडीपी वृद्धि (%)", "वास्तविक जीएसडीपी वाढ (%)"), "percent", "higher-is-better", "FY2024-25", {c: real_growth(c) for c in REGIONS},
          dp(round(100 * (gdp["FY2024-25"][1] / gdp["FY2023-24"][1] - 1), 1), "%", "FY2024-25", "fy", "mospi", MOSPI, level="national", rev="provisional", base=CON,
             note="Computed from GDP at constant 2011-12 prices (Provisional over First Revised Estimates).")),
        I("pcnsdp", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"), "rupee", "higher-is-better", "FY2024-25",
          {c: gsdp_fy(c, "FY2024-25", unit="₹", key="pcnsdp") for c in REGIONS}, None),
        I("ur", L("Unemployment rate, 15+ (%)", "बेरोज़गारी दर, 15+ (%)", "बेरोजगारी दर, 15+ (%)"), "percent", "lower-is-better", "2025", {c: plfs(c, "ur") for c in REGIONS},
          dp(AP["plfs_ur_15plus_psss"]["IN"]["2025"], "%", "2025", "calendar", "plfs", MOSPI, level="national")),
        I("lfprF", L("Women's labour force participation, 15+ (%)", "महिला श्रम बल भागीदारी, 15+ (%)", "स्त्रियांचा श्रमशक्ती सहभाग, 15+ (%)"), "percent", "higher-is-better", "2025", {c: plfs(c, "lfpr") for c in REGIONS},
          dp(AP["plfs_lfpr_2025"]["IN"]["female"], "%", "2025", "calendar", "plfs", MOSPI, level="national")),
    ]},
    {"id": "wellbeing", "label": L("Education and health", "शिक्षा और स्वास्थ्य", "शिक्षण व आरोग्य"), "indicators": [
        I("ger", L("Higher-education GER, 18–23 (%)", "उच्च शिक्षा जीईआर, 18–23 (%)", "उच्चशिक्षण जीईआर, 18–23 (%)"), "percent", "higher-is-better", "2021-22", {c: ger(c) for c in REGIONS},
          dp(28.40, "%", "2021-22", "survey", "aishe", AISHE, level="national")),
        I("stunting", L("Stunted children under 5 (%)", "5 वर्ष से कम आयु के ठिगने बच्चे (%)", "5 वर्षांखालील खुजी मुले (%)"), "percent", "lower-is-better", "2019-21", {c: nfhs(c, "stunted") for c in REGIONS},
          dp(NF["IN"]["stunted"][1], "%", "2019-21", "survey", "nfhs", NFHS, level="national")),
        I("inst", L("Institutional births (%)", "संस्थागत प्रसव (%)", "संस्थात्मक प्रसूती (%)"), "percent", "higher-is-better", "2019-21", {c: nfhs(c, "inst") for c in REGIONS},
          dp(NF["IN"]["institutional_N5"], "%", "2019-21", "survey", "nfhs", NFHS, level="national")),
        I("u5mr", L("Under-five mortality (per 1,000 live births)", "पाँच वर्ष से कम आयु की मृत्यु दर (प्रति 1,000 जीवित जन्म)", "पाच वर्षांखालील मृत्युदर (दर 1,000 जिवंत जन्म)"), "number", "lower-is-better", "2021",
          {c: srs_v(c, "U5MR", "2021") for c in REGIONS}, dp(srs["IN"]["U5MR"], "per 1,000 live births", "2021", "calendar", "srs", SRS, level="national")),
        I("mmr", L("Maternal mortality (per 1,00,000 live births)", "मातृ मृत्यु (प्रति 1,00,000 जीवित जन्म)", "मातामृत्यू (दर 1,00,000 जिवंत जन्म)"), "number", "lower-is-better", "2019-21",
          {c: srs_v(c, "MMR_2019_21", "2019-21") for c in REGIONS}, dp(srs["IN"]["MMR_2019_21"], "per 1,00,000 live births", "2019-21", "survey", "srs", SRS, level="national")),
    ]},
    {"id": "environment", "label": L("Environment", "पर्यावरण", "पर्यावरण"), "indicators": [
        I("forest", L("Forest cover (% of area)", "वन आवरण (क्षेत्रफल का %)", "वनाच्छादन (क्षेत्रफळाच्या %)"), "percent", "neutral", "2023", metric("forestCoverPct"), im["forestCoverPct"],
          note=L("Shaped largely by geography; shown without a better/worse marker.", "मुख्यतः भूगोल से तय; बेहतर/ख़राब का संकेत नहीं दिखाया गया।", "मुख्यतः भूगोलाने ठरते; चांगले/वाईट असा निर्देश दाखवलेला नाही.")),
    ]},
]

# Keep MH's FY2025-26 out of the comparison: all GSDP values are FY2024-25 above.
trend = {"type": "series", "id": "gsdp-compare", "title": L("GSDP at current prices, FY2011-12 to FY2024-25", "प्रचलित मूल्यों पर जीएसडीपी, वित्त वर्ष 2011-12 से 2024-25", "चालू किमतींनुसार जीएसडीपी, आ.व. 2011-12 ते 2024-25"),
         "kind": "rupeeCrore", "polarity": "neutral",
         "series": [{"id": c, "label": reg[c]["name"],
                     "points": [dp(v[0], "₹ crore", y, "fy", "mospi", MOSPI, rev="provisional" if y in ("FY2023-24", "FY2024-25") else "final", base=CUR)
                                for y, v in sorted(mo[SHORT[c]]["gsdp"].items()) if y <= "FY2024-25"]}
                    for c in REGIONS if SHORT[c] in mo]}

write("compare/indicators.json", {"asOf": TODAY, "regions": REGIONS, "defaultSelection": ["IN-MH", "IN-TN", "IN-UP", "IN-KL"],
                                  "groups": groups, "trend": trend})
print("compare ok", sum(len(g["indicators"]) for g in groups), "indicators")
