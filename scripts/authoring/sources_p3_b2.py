"""Add the sources used for Phase 3 batch 2 (Karnataka, Gujarat, West Bengal) — idempotent."""
import json, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "sources.json")
src = json.load(open(P))
have = {s["id"] for s in src}

NEW = [
    dict(id="ka-des", short="Economic Survey of Karnataka", name="Economic Survey of Karnataka (Planning, Programme Monitoring and Statistics Department)",
         publisher="Government of Karnataka", url="https://des.karnataka.gov.in", category="economy", priority=8,
         notes="The PDFs are linked from the OpenCity data portal copy of the Government of Karnataka publication; replace with the des.karnataka.gov.in link in review."),
    dict(id="ka-gis", short="Karnataka GIS (KSRSAC)", name="Karnataka at a Glance — Karnataka-GIS, Karnataka State Remote Sensing Applications Centre",
         publisher="Government of Karnataka", url="https://kgis.ksrsac.in/kag/", category="governance", priority=12),
    dict(id="es-india", short="Economic Survey of India (Statistical Appendix)", name="Economic Survey, Statistical Appendix",
         publisher="Ministry of Finance, Government of India", url="https://www.indiabudget.gov.in", category="economy", priority=5),
    dict(id="gj-des", short="Socio-Economic Review, Gujarat", name="Socio-Economic Review, Gujarat State (Directorate of Economics and Statistics)",
         publisher="Government of Gujarat", url="https://gujecostat.gujarat.gov.in", category="economy", priority=8,
         notes="The PDF is linked from the OpenCity data portal copy of the Government of Gujarat publication; replace with the gujecostat link in review."),
    dict(id="ani", short="ANI", name="Asian News International (ANI)", publisher="ANI (news agency, third party)",
         url="https://www.aninews.in", category="governance", priority=27, notes="Third-party. Replace with the Lok Bhavan / Raj Bhavan page once available."),
]
added = 0
for s in NEW:
    if s["id"] not in have:
        src.append(s); added += 1
json.dump(src, open(P, "w"), ensure_ascii=False, indent=2)
print("sources added", added, "total", len(src))
