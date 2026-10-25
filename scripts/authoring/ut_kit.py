"""Shared blocks for the batch 7 Union Territory profiles (A&N, Chandigarh, DNH&DD, Lakshadweep, Puducherry)."""
from common import *

PYD = "https://statistics.py.gov.in/state-wise-population"
ESI_LIT = "https://www.indiabudget.gov.in/budget2022-23/economicsurvey/doc/stat/tab85.pdf"
ESI_VS = "https://www.indiabudget.gov.in/budget2024-25/economicsurvey/doc/stat/tab82.pdf"
SCST = "https://delhiplanning.delhi.gov.in/sites/default/files/Planning/17._table_social_welfare.pdf"
C = research("census_b5plus.json")
IND = read("india.json")["metrics"]
NOTE_MO = ("MoSPI state-wise estimates, base 2011-12 (current series), accessed via the MoSPI API on 25 Oct 2026. "
           "FY2024-25 is the latest year published and may be revised.")


def sym(en, hi, mr, sci):
    return {"name": L(en, hi, mr), "scientificName": sci, "sourceId": None, "url": None, "confidence": "Editorial", "revisionStatus": "TODO"}


def census_metrics(m, key, area, males_females, density, fc_pct, fc_note):
    p = C["pop"][key]; csr = C["csr"][key]
    m["population2011"] = dp(p[0], "persons", "2011", "census", "census", PYD,
        note=f"Census 2011 (ORGI), as tabulated by the Directorate of Economics and Statistics, Puducherry. {males_females}")
    m["area"] = dp(area, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
    m["density2011"] = dp(density, "persons per km²", "2011", "census", "census", PYD, note=f"Calculated: Census 2011 population ÷ area {inr(area)} km².")
    m["sexRatio2011"] = dp(p[4], "females per 1000 males", "2011", "census", "census", PYD, note=f"Puducherry DES state-wise table citing ORGI ({p[3]} in 2001).")
    m["childSexRatio2011"] = dp(csr[1], "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note=f"PIB release of 11 Feb 2014 (RGI data). Was {csr[0]} in 2001.")
    m["literacyRate2011"] = dp(C["lit"][key], "%", "2011", "census", "es-india", ESI_LIT, note="Economic Survey 2021-22, Statistical Appendix Table 8.5 (Census 2011).")
    m["urbanisation2011"] = dp(None, "%", "2011", "census", "census", None,
        note="Not shown: no official publication giving the 2011 urban share was reached. Needs the Census 2011 Primary Census Abstract.")
    m["forestCoverPct"] = dp(fc_pct, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST, note=fc_note)


def mospi_metrics(m, mo, name_en):
    m["gsdpCurrent"] = dp(mo["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
        note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25 is the latest year published for {name_en}. FY2023-24: ₹{inr(mo['gsdp']['FY2023-24'][0])} crore.")
    m["perCapitaNsdpCurrent"] = dp(mo["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
        note=f"MoSPI, base 2011-12. FY2023-24: ₹{inr(mo['pcnsdp']['FY2023-24'][0])}.")


def people_facts(code, m, key, st_or_sc):
    p = C["pop"][key]; csr = C["csr"][key]
    out = [
        fact("pop", L("Population (Census 2011)", "जनसंख्या (जनगणना 2011)", "लोकसंख्या (जनगणना 2011)"), m["population2011"], "count", national=IND["population2011"]),
        fact("sr", L("Sex ratio", "लिंगानुपात", "लिंग गुणोत्तर"), m["sexRatio2011"], "ratio", "higher-is-better", national=IND["sexRatio2011"],
             previous=dp(p[3], "females per 1000 males", "2001", "census", "census", PYD)),
        fact("csr", L("Child sex ratio (0–6)", "शिशु लिंगानुपात (0–6)", "बाल लिंग गुणोत्तर (0–6)"), m["childSexRatio2011"], "ratio", "higher-is-better",
             previous=dp(csr[0], "girls per 1000 boys (0–6 yrs)", "2001", "census", "census", PIB_CSR), national=IND["childSexRatio2011"]),
        fact("lit", L("Literacy rate", "साक्षरता दर", "साक्षरता दर"), m["literacyRate2011"], "percent", "higher-is-better", national=IND["literacyRate2011"]),
        fact("den", L("Population density", "जनसंख्या घनत्व", "लोकसंख्या घनता"), m["density2011"], "number"),
    ]
    if st_or_sc:
        out.append(st_or_sc)
    return out


def econ_blocks(code, name, mo):
    cur = mo["gsdp"]; pc = mo["pcnsdp"]
    sect, _ = sector_table(mo["gsva2024_25_current_lakh"])
    return [
        facts("f", [
            fact("gsdp", L("GSDP, current prices", "जीएसडीपी, प्रचलित मूल्य", "जीएसडीपी, चालू किमती"),
                 dp(cur["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_MO), "rupeeCrore", "higher-is-better",
                 previous=dp(cur["FY2023-24"][0], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
            fact("gsdpk", L("GSDP, constant 2011-12 prices", "जीएसडीपी, स्थिर 2011-12 मूल्य", "जीएसडीपी, स्थिर 2011-12 किमती"),
                 dp(cur["FY2024-25"][1], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CON, note=NOTE_MO), "rupeeCrore", "higher-is-better",
                 previous=dp(cur["FY2023-24"][1], "₹ crore", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CON)),
            fact("pc", L("Per capita NSDP, current prices", "प्रति व्यक्ति एनएसडीपी, प्रचलित मूल्य", "दरडोई एनएसडीपी, चालू किमती"),
                 dp(pc["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note=NOTE_MO), "rupee", "higher-is-better",
                 previous=dp(pc["FY2023-24"][0], "₹", "FY2023-24", "fy", "mospi", MOSPI, rev="provisional", base=CUR)),
            *plfs_facts(code, name),
        ], title=L("Key indicators", "मुख्य संकेतक", "प्रमुख निर्देशक")),
        *gdp_series(mo, "FY2011-12 to FY2024-25"),
        sect,
        plfs_series(code, name),
    ]


def srs_facts(key):
    s = C["srs"][key]
    return facts("srs", [
        fact("imr", L("Infant mortality rate", "शिशु मृत्यु दर", "अर्भक मृत्युदर"),
             dp(s[5], "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, note="SRS 2020, Economic Survey 2023-24 Statistical Appendix Table 8.2. Small UTs have large sampling errors."), "number", "lower-is-better",
             previous=dp(s[4], "per 1,000 live births", "2010", "calendar", "srs", ESI_VS), national=dp(28, "per 1,000 live births", "2020", "calendar", "srs", ESI_VS, level="national")),
        fact("br", L("Birth rate", "जन्म दर", "जन्मदर"), dp(s[1], "per 1,000 population", "2020", "calendar", "srs", ESI_VS, note=f"SRS 2020 (death rate {s[3]}); {s[0]} in 2010."), "number",
             previous=dp(s[0], "per 1,000 population", "2010", "calendar", "srs", ESI_VS), national=dp(19.5, "per 1,000 population", "2020", "calendar", "srs", ESI_VS, level="national")),
    ], title=L("Mortality and vital rates (Sample Registration System)", "मृत्यु और जन्म दरें (नमूना पंजीकरण प्रणाली)", "मृत्युदर व जन्मदर (नमुना नोंदणी पद्धत)"))


def nfhs_block(code):
    return facts("nfhs", nfhs_facts(code), title=L("Child nutrition and births (NFHS-5)", "बाल पोषण और प्रसव (एनएफ़एचएस-5)", "बालपोषण व प्रसूती (एनएफएचएस-5)"))


def forest_facts(key, pct_metric, ramsar_n, ramsar_note):
    F = C["forest"][key]
    return facts("f", [
        fact("fc", L("Forest cover (ISFR 2023)", "वन आवरण (आईएसएफ़आर 2023)", "वनाच्छादन (आयएसएफआर 2023)"),
             dp(F[2], "km²", "2023", "calendar", "fsi", LS_FOREST, note="Lok Sabha Unstarred Q. 1550, 9 Feb 2026, citing ISFR 2021 and 2023."), "number", "higher-is-better",
             previous=dp(F[1], "km²", "2021", "calendar", "fsi", LS_FOREST)),
        fact("fcp", L("Forest cover, % of area", "वन आवरण, क्षेत्रफल का %", "वनाच्छादन, क्षेत्रफळाच्या %"), pct_metric, "percent", "higher-is-better", national=IND["forestCoverPct"]),
        fact("ramsar", L("Ramsar wetlands", "रामसर आर्द्रभूमियाँ", "रामसर पाणथळ स्थळे"),
             dp(ramsar_n, "sites", "2026", "calendar", "indian-wetlands", RAMSAR, note=ramsar_note), "number"),
    ])


def admin_table(rows, note=None):
    return table("admin", L("Administrative identity", "प्रशासनिक पहचान", "प्रशासकीय ओळख"),
                 [col(L("Item", "विषय", "बाब")), col(L("Value", "विवरण", "तपशील"))], rows, None, None, conf="Editorial", access=None, note=note)


def row(en, hi, mr, v):
    return [L(en, hi, mr), v if isinstance(v, (str, dict)) else L(*v)]


def links(items):
    return lst("links", items, title=L("Official websites", "आधिकारिक वेबसाइटें", "अधिकृत संकेतस्थळे"), conf="Official")


RTI = it3("rti", "RTI Online (Government of India)", "आरटीआई ऑनलाइन (भारत सरकार)", "माहितीचा अधिकार ऑनलाइन (भारत सरकार)", url="https://rtionline.gov.in", src="india-gov")


def person(id, n, d, m):
    return item(id, L(*n), detail=L(*d), meta=L(*m))


def triv(id, t, url=None, src=None):
    return item(id, L(*t), url=url, src=src)


def fest(id, n, m, d):
    return item(id, L(*n), detail=L(*d), meta=L(*m))
