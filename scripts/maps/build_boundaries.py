"""Build the boundary and capital files for the India map (docs/MAPS.md).

Inputs (downloaded into a work folder, never committed):
  * SOI_States.geojsonl.7z  - Survey of India State/UT boundaries (free digital product,
    onlinemaps.surveyofindia.gov.in, product OVSF/1M/7), repackaged unchanged by
    github.com/ramSeraph/indian_admin_boundaries (release "states", CC0).
  * ne_10m_populated_places_simple.geojson - Natural Earth (public domain). Used ONLY for
    capital point locations, never for any boundary.

Outputs:
  public/maps/india-soi-states.topo.json  (object "states", property iso_code)
  public/maps/capitals.json               (points with region code, role and source)
  public/maps/india-preview.svg           (static zonal-colour preview for the home page)

Run:  python3 scripts/maps/build_boundaries.py <workdir>
Needs: py7zr (pip) and mapshaper (npx -y mapshaper@0.6.102).
Geometry is simplified for screen display only (Visvalingam, 3%, keep-shapes). `-clean` builds
shared borders between neighbouring States (the source polygons do not share exact vertices) and
resolves sub-3 km² gaps and overlaps between them; no boundary is otherwise moved, added or
removed, and inter-State disputed areas are kept as published.
"""
import glob, json, os, subprocess, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = sys.argv[1] if len(sys.argv) > 1 else "/tmp/bd-maps"
os.makedirs(WORK, exist_ok=True)
SOI_URL = "https://github.com/ramSeraph/indian_admin_boundaries/releases/download/states/SOI_States.geojsonl.7z"
NE_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_populated_places_simple.geojson"

# State_LGD (Local Government Directory code, as carried in the SoI file) -> ISO 3166-2
LGD_ISO = {
    35: "IN-AN", 28: "IN-AP", 12: "IN-AR", 18: "IN-AS", 10: "IN-BR", 4: "IN-CH", 22: "IN-CT",
    38: "IN-DH", 7: "IN-DL", 30: "IN-GA", 24: "IN-GJ", 6: "IN-HR", 2: "IN-HP", 1: "IN-JK",
    20: "IN-JH", 29: "IN-KA", 32: "IN-KL", 37: "IN-LA", 31: "IN-LD", 23: "IN-MP", 27: "IN-MH",
    14: "IN-MN", 17: "IN-ML", 15: "IN-MZ", 13: "IN-NL", 21: "IN-OR", 34: "IN-PY", 3: "IN-PB",
    8: "IN-RJ", 11: "IN-SK", 33: "IN-TN", 36: "IN-TG", 16: "IN-TR", 5: "IN-UK", 9: "IN-UP",
    19: "IN-WB",
}

# Region capital (as named in data/regions) -> Natural Earth name
NE_NAME = {"Sri Vijaya Puram": "Port Blair", "Dehradun": "Dehra Dun", "Shimla": "Simla"}


def fetch(url, dest):
    if not os.path.exists(dest):
        urllib.request.urlretrieve(url, dest)
    return dest


def main():
    import py7zr

    arc = fetch(SOI_URL, os.path.join(WORK, "SOI_States.geojsonl.7z"))
    py7zr.SevenZipFile(arc).extractall(WORK)
    feats = []
    for line in open(os.path.join(WORK, "SOI_States.geojsonl"), encoding="utf8"):
        f = json.loads(line)
        lgd = f["properties"]["State_LGD"]
        name = f["properties"]["STATE_C"]
        if lgd == 0:
            props = {"iso_code": "disputed", "label": name.title().replace("&", "and")}
        else:
            props = {"iso_code": LGD_ISO[lgd], "lgd": lgd}
        feats.append({"type": "Feature", "properties": props, "geometry": f["geometry"]})
    assert len({f["properties"]["iso_code"] for f in feats}) == 37, "expected 36 States/UTs + disputed"
    src = os.path.join(WORK, "states.geojson")
    json.dump({"type": "FeatureCollection", "features": feats}, open(src, "w"))
    out = os.path.join(ROOT, "public", "maps", "india-soi-states.topo.json")
    subprocess.run(["npx", "-y", "mapshaper@0.6.102", src, "-rename-layers", "states",
                    "-simplify", "3%", "keep-shapes", "-clean",
                    "-o", "format=topojson", "quantization=100000", out], check=True)

    # Static preview for the home page (no JavaScript needed): zonal colours, lighter detail.
    zonal = {"northern": "#0072B2", "central": "#E69F00", "eastern": "#009E73", "western": "#D55E00",
             "southern": "#CC79A7", "north-eastern": "#56B4E9", "islands": "#7F7F7F"}  # = mapColors.ts
    zone_of = {}
    for path in glob.glob(os.path.join(ROOT, "data", "regions", "*.json")):
        r = json.load(open(path, encoding="utf8"))
        zone_of[r["code"]] = zonal[r.get("zonalCouncil") or "islands"]
    for f in feats:
        f["properties"]["fill"] = zone_of.get(f["properties"]["iso_code"], "#d9d5cb")
    styled = os.path.join(WORK, "styled.geojson")
    json.dump({"type": "FeatureCollection", "features": feats}, open(styled, "w"))
    preview = os.path.join(ROOT, "public", "maps", "india-preview.svg")
    subprocess.run(["npx", "-y", "mapshaper@0.6.102", styled, "-simplify", "0.6%", "keep-shapes", "-clean",
                    "-proj", "merc", "-style", "stroke='#ffffff'", "stroke-width=0.6",
                    "-o", "width=600", "margin=6", "precision=0.5", preview], check=True)

    # Capitals
    ne = json.load(open(fetch(NE_URL, os.path.join(WORK, "ne_pp.geojson"))))
    india = {}
    for f in ne["features"]:
        p = f["properties"]
        if p.get("adm0name") == "India":
            india.setdefault(p["name"], f["geometry"]["coordinates"])
    caps, missing = [], []
    for path in sorted(glob.glob(os.path.join(ROOT, "data", "regions", "*.json"))):
        r = json.load(open(path, encoding="utf8"))
        for c in r["capitals"]:
            en = c["name"]["en"]
            key = NE_NAME.get(en, en.split(" (")[0])
            if key not in india:
                missing.append(f"{r['code']} {en}")
                continue
            lon, lat = india[key]
            caps.append({"code": r["code"], "role": c["role"], "name": c["name"],
                         "lon": round(lon, 4), "lat": round(lat, 4)})
    json.dump({
        "source": "Natural Earth 1:10m populated places (public domain), v5 - point locations only",
        "sourceUrl": "https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-populated-places/",
        "missing": missing,
        "capitals": caps,
    }, open(os.path.join(ROOT, "public", "maps", "capitals.json"), "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print(f"capitals: {len(caps)} placed, missing: {missing}")


if __name__ == "__main__":
    main()
