"""Core metrics for Tamil Nadu and Uttar Pradesh (needed for the comparison prototype).
Profiles themselves stay at 'seed' until Phase 3."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *

TN23 = "https://des.tn.gov.in/sites/default/files/2024-01/At_a_glance_%2029_12_2023.pdf"
TN21 = "https://www.des.tn.gov.in/sites/default/files/2021-02/AT%20A%20GLANCE%202021%20%20Final%206.1.2021.pdf"
UPF = "https://updes.up.nic.in/updes/data/upinfigures/up%20in%20figures-%202022.pdf"
PYD = "https://statistics.py.gov.in/state-wise-population"

tn = research("mospi_tn.json"); up = research("mospi_up.json")

r = read("regions/IN-TN.json")
m = r["metrics"]
m["population2011"] = dp(72147030, "persons", "2011", "census", "census", TN23,
    note="Census 2011 total as published by the Department of Economics and Statistics, Tamil Nadu; matches the Puducherry DES state-wise table.")
m["area"] = dp(130060, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026). The State gives 1,30,058 km².")
m["density2011"] = dp(555, "persons per km²", "2011", "census", "census", TN23, note="Tamil Nadu DES.")
m["sexRatio2011"] = dp(996, "females per 1000 males", "2011", "census", "census", PYD,
    note="Puducherry DES state-wise table citing ORGI (987 in 2001). Tamil Nadu DES 'At a Glance' also gives 996.")
m["childSexRatio2011"] = dp(943, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 942 in 2001.")
m["literacyRate2011"] = dp(80.09, "%", "2011", "census", "census", TN23, note="Population aged 7+. Male 86.77%, female 73.14% (Tamil Nadu DES).")
m["urbanisation2011"] = dp(48.40, "%", "2011", "census", "census", TN21, note="Tamil Nadu DES, 'Tamil Nadu at a Glance 2021'.")
m["gsdpCurrent"] = dp(tn["gsdp"]["FY2025-26"][0], "₹ crore", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2024-25: ₹{inr(tn['gsdp']['FY2024-25'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(tn["pcnsdp"]["FY2025-26"][0], "₹", "FY2025-26", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI, base 2011-12. FY2024-25: ₹{inr(tn['pcnsdp']['FY2024-25'][0])}.")
m["forestCoverPct"] = dp(20.34, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 26,450.22 km² ÷ geographical area 1,30,060 km².")
write("regions/IN-TN.json", r)

r = read("regions/IN-UP.json")
m = r["metrics"]
m["population2011"] = dp(199812341, "persons", "2011", "census", "census", UPF,
    note="Census 2011 total as published by the Economics & Statistics Division, Government of Uttar Pradesh. Males 10,44,80,510; females 9,53,31,831.")
m["area"] = dp(240928, "km²", "2023", "calendar", "fsi", LS_FOREST, note="Geographical area used in ISFR 2023 (Lok Sabha Unstarred Q. 1550, 9 Feb 2026).")
m["density2011"] = dp(829, "persons per km²", "2011", "census", "census", UPF, note="UP DES.")
m["sexRatio2011"] = dp(912, "females per 1000 males", "2011", "census", "census", UPF, note="Also 912 in the Puducherry DES state-wise table (898 in 2001).")
m["childSexRatio2011"] = dp(902, "girls per 1000 boys (0–6 yrs)", "2011", "census", "census", PIB_CSR, note="PIB release of 11 Feb 2014 (RGI data). Was 916 in 2001.")
m["literacyRate2011"] = dp(67.7, "%", "2011", "census", "census", UPF, note="Population aged 7+, as rounded by UP DES. Male 77.3%, female 57.2%.")
m["urbanisation2011"] = dp(22.27, "%", "2011", "census", "census", UPF, note="Urban population 4,44,95,063 (UP DES).")
m["gsdpCurrent"] = dp(up["gsdp"]["FY2024-25"][0], "₹ crore", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR,
    note=f"MoSPI state-wise GSDP, base 2011-12, current series. FY2025-26 not yet published for Uttar Pradesh. FY2023-24: ₹{inr(up['gsdp']['FY2023-24'][0])} crore.")
m["perCapitaNsdpCurrent"] = dp(up["pcnsdp"]["FY2024-25"][0], "₹", "FY2024-25", "fy", "mospi", MOSPI, rev="provisional", base=CUR, note="MoSPI, base 2011-12.")
m["forestCoverPct"] = dp(6.24, "% of geographical area", "2023", "calendar", "fsi", LS_FOREST,
    note="Computed from ISFR 2023 forest cover 15,045.80 km² ÷ geographical area 2,40,928 km².")
write("regions/IN-UP.json", r)
print("tn/up core ok")
