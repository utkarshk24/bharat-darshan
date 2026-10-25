"""Build per-State district boundary files for the India map (docs/MAPS.md).

Input: LGD_Districts.geojsonl.7z - district boundaries keyed to Local Government Directory (LGD)
codes, from NIC Bharatmaps (mapservice.gov.in, Admin_Boundary_Village layer 1), republished
unchanged by github.com/ramSeraph/indian_admin_boundaries (release "districts", file dated
11 Dec 2023, CC0). Its outer boundary matches the Survey of India State file, including the
areas of Jammu & Kashmir under the occupation of Pakistan (Mirpur and Muzaffarabad, LGD code 0).

District lists change often. For each region, the number of districts in the file is compared
with the number in the region's authored profile (data/modules/IN-XX/overview.json). Where
they differ, no district boundaries are drawn for that region (status "outdated"), so the map
never shows a superseded district map as current.

Outputs: public/maps/districts/IN-XX.topo.json (object "districts"; properties name, lgd)
         public/maps/districts/index.json
Run:     python3 scripts/maps/build_districts.py <workdir>
"""
import glob, json, os, re, subprocess, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = sys.argv[1] if len(sys.argv) > 1 else "/tmp/bd-maps"
URL = "https://github.com/ramSeraph/indian_admin_boundaries/releases/download/districts/LGD_Districts.geojsonl.7z"
VINTAGE = "2023-12-11"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_boundaries import LGD_ISO  # noqa: E402


def profile_count(code):
    """First number in the 'Districts…' row of the region's overview, if authored."""
    p = os.path.join(ROOT, "data", "modules", code, "overview.json")
    if not os.path.exists(p):
        return None
    found = []

    def walk(o):
        if found:
            return
        if isinstance(o, list):
            if len(o) >= 2 and isinstance(o[0], dict) and str(o[0].get("en", "")).startswith("Districts"):
                v = o[1]["en"] if isinstance(o[1], dict) else str(o[1])
                m = re.match(r"\s*(\d+)", v)
                if m:
                    found.append(int(m.group(1)))
                    return
            for x in o:
                walk(x)
        elif isinstance(o, dict):
            for x in o.values():
                walk(x)

    walk(json.load(open(p, encoding="utf8")))
    return found[0] if found else None


def main():
    import py7zr

    os.makedirs(WORK, exist_ok=True)
    arc = os.path.join(WORK, "LGD_Districts.geojsonl.7z")
    if not os.path.exists(arc):
        urllib.request.urlretrieve(URL, arc)
    src = os.path.join(WORK, "LGD_Districts.geojsonl")
    if not os.path.exists(src):
        py7zr.SevenZipFile(arc).extractall(WORK)
    feats, counts = [], {}
    for line in open(src, encoding="utf8"):
        f = json.loads(line)
        p = f["properties"]
        code = LGD_ISO[p["state_lgd"]]
        feats.append({"type": "Feature", "geometry": f["geometry"],
                      "properties": {"name": p["dtname"].strip(), "lgd": p["dist_lgd"], "st": code}})
        if p["dist_lgd"] != 0:
            counts[code] = counts.get(code, 0) + 1
    fc = os.path.join(WORK, "districts.geojson")
    json.dump({"type": "FeatureCollection", "features": feats}, open(fc, "w"))

    outdir = os.path.join(ROOT, "public", "maps", "districts")
    os.makedirs(outdir, exist_ok=True)
    for old in glob.glob(os.path.join(outdir, "*.json")):
        os.remove(old)
    index = {"source": "LGD district boundaries via NIC Bharatmaps (mapservice.gov.in), republished by ramSeraph/indian_admin_boundaries (CC0)",
             "sourceUrl": "https://github.com/ramSeraph/indian_admin_boundaries/releases/tag/districts",
             "vintage": VINTAGE, "regions": {}}
    for code in sorted(set(LGD_ISO.values())):
        n, prof = counts.get(code, 0), profile_count(code)
        status = "outdated" if prof is not None and prof != n else "shown"
        entry = {"count": n, "profileCount": prof, "status": status}
        if status == "shown":
            part = os.path.join(WORK, f"d_{code}.geojson")
            mine = [{**f, "properties": {"name": f["properties"]["name"], "lgd": f["properties"]["lgd"]}}
                    for f in feats if f["properties"]["st"] == code]
            json.dump({"type": "FeatureCollection", "features": mine}, open(part, "w"))
            out = os.path.join(outdir, f"{code}.topo.json")
            subprocess.run(["npx", "-y", "mapshaper@0.6.102", part, "-rename-layers", "districts",
                            "-simplify", "4%", "keep-shapes", "-clean",
                            "-o", "format=topojson", "quantization=100000", out],
                           check=True, capture_output=True)
            kept = len(json.load(open(out))["objects"]["districts"]["geometries"])
            assert kept == len(mine), f"{code}: {kept} of {len(mine)} districts kept"
            entry["file"] = f"{code}.topo.json"
        index["regions"][code] = entry
        print(code, n, prof, status)
    json.dump(index, open(os.path.join(outdir, "index.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
