"""Build the map's thematic layers (docs/MAPS.md, "Thematic layers").

Every input is an Indian government dataset, republished unchanged as GeoJSONL by Datameet
volunteers (github.com/ramSeraph, CC0 1.0, "attribute datameet and the original government
source"), the same route as the Survey of India boundaries. UNESCO coordinates are copied from
whc.unesco.org (scripts/maps/unesco_coords.txt). Nothing here draws or moves a boundary.

Inputs are downloaded into <workdir> (never committed). Outputs, in public/maps/layers/:
  rivers.topo.json     India-WRIS major rivers; lakes (>= 50 km²) and reservoirs (>= 100 km²)
  protected.topo.json  National parks and wildlife sanctuaries (MoEFCC via PM GatiShakti);
                       Ramsar sites (MoEFCC Parivesh via Bharatmaps)
  transport.topo.json  National highways (MoRTH via PM GatiShakti); railway lines (Indian Railways)
  hazards.topo.json    Area flooded at least once 1998–2022 (NRSC NDEM)
  hazards-points.json  Earthquakes of magnitude 6.0+ with epicentres in India, 1897–2019 (GSI NGDR)
  heritage.json        UNESCO World Heritage properties (points per component)
  index.json           Per-layer sources, dates, counts and caveats (read by the map)

Run:  python3 scripts/maps/build_layers.py <workdir>
Needs: py7zr (pip), mapshaper (npx -y mapshaper@0.6.102), shapely (pip).
"""
import json, math, os, re, subprocess, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = sys.argv[1] if len(sys.argv) > 1 else "/tmp/bd-layers"
OUT = os.path.join(ROOT, "public", "maps", "layers")
GH = "https://github.com/ramSeraph"
MS = ["npx", "-y", "mapshaper@0.6.102"]

FILES = {
    "rivers": f"{GH}/indian_water_features/releases/download/rivers/WRIS_Rivers.geojsonl.7z",
    "lakes": f"{GH}/indian_water_features/releases/download/waterbodies/WRIS_Lakes.geojsonl.7z",
    "reservoirs": f"{GH}/indian_water_features/releases/download/waterbodies/WRIS_Reservoirs.geojsonl.7z",
    "ramsar": f"{GH}/indian_water_features/releases/download/wetlands/Bharatmaps_Parivesh_Ramsar_Wetlands.geojsonl.7z",
    "pa": f"{GH}/indian_admin_boundaries/releases/download/forests/GatiShakti_Wildlife_Sanctuaries_and_National_Parks.geojsonl.7z",
    "nh": f"{GH}/indian_transport/releases/download/morth-roads/GatiShakti_MORTH_National_Highways.geojsonl.7z",
    "rail": f"{GH}/indian_transport/releases/download/railways/IR_Tracks.geojsonl.7z",
    "stations": f"{GH}/indian_transport/releases/download/railways/IR_Stations.geojsonl.7z",
    "floods": f"{GH}/india_natural_disasters/releases/download/floods/NDEM_All_India_Flood_Innundation_1998_to_2022.geojsonl.7z",
    "quakes": f"{GH}/india_natural_disasters/releases/download/earthquakes/NGDR_Earthquakes.geojsonl.7z",
    "asi": f"{GH}/indian_facilities/releases/download/cultural/Bhuvan_ASI_Monuments.geojsonl.7z",
}

ATTRIB = "Republished by Datameet (github.com/ramSeraph), CC0 1.0"


def fetch(key):
    url = FILES[key]
    arc = os.path.join(WORK, os.path.basename(url))
    out = arc[:-3]
    if not os.path.exists(out):
        if not os.path.exists(arc):
            print("download", url)
            urllib.request.urlretrieve(url, arc)
        import py7zr
        with py7zr.SevenZipFile(arc) as z:
            z.extractall(WORK)
    return out


def rows(path):
    with open(path) as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def write_fc(name, feats):
    p = os.path.join(WORK, f"{name}.geojson")
    with open(p, "w") as f:
        json.dump({"type": "FeatureCollection", "features": feats}, f)
    return p


def ms(*args):
    subprocess.run(MS + [str(a) for a in args], check=True, capture_output=True)


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def clean(s):
    return re.sub(r"\s+", " ", (s or "").strip())


# ---------------------------------------------------------------- rivers and lakes
def build_rivers():
    rivers = [
        {"type": "Feature", "geometry": d["geometry"], "properties": {"n": clean(d["properties"]["rivname"]).rstrip(" .")}}
        for d in rows(fetch("rivers")) if d["properties"].get("layer") == "major" and d["geometry"]
    ]
    water = []
    for key, kind, min_ha in (("lakes", "lake", 5000), ("reservoirs", "reservoir", 10000)):
        for d in rows(fetch(key)):
            p = d["properties"]
            name = clean(p.get("wbname") or p.get("setname"))
            # The Rann of Kutch is recorded as a lake in WRIS; it is a seasonal salt marsh, so it is left out.
            if (p.get("area_ha") or 0) >= min_ha and d["geometry"] and "rann" not in name.lower():
                water.append({"type": "Feature", "geometry": d["geometry"], "properties": {"n": name, "k": kind, "ha": round(p["area_ha"])}})
    r, w = write_fc("rivers", rivers), write_fc("water", water)
    out = os.path.join(OUT, "rivers.topo.json")
    ms("-i", r, w, "combine-files", "-rename-layers", "rivers,water",
       "-dissolve", "n", "target=rivers", "-simplify", "interval=400", "keep-shapes",
       "-o", "target=*", "format=topojson", "quantization=4e4", out)
    return {"rivers": len({f["properties"]["n"] for f in rivers}), "lakes": sum(f["properties"]["k"] == "lake" for f in water),
            "reservoirs": sum(f["properties"]["k"] == "reservoir" for f in water)}


# ---------------------------------------------------------------- protected areas
PA_KIND = {"National Park": "np", "Sanctuary": "ws", "National Park/Sanctuary": "np"}


def build_protected():
    pa = []
    for d in rows(fetch("pa")):
        p = d["properties"]
        if d["geometry"] and p.get("category") in PA_KIND:
            pa.append({"type": "Feature", "geometry": d["geometry"],
                       "properties": {"n": clean(p["name"]), "k": PA_KIND[p["category"]], "s": clean(p.get("state"))}})
    ramsar = [{"type": "Feature", "geometry": d["geometry"], "properties": {"n": clean(d["properties"]["name"]), "s": clean(d["properties"].get("state"))}}
              for d in rows(fetch("ramsar")) if d["geometry"]]
    a, b = write_fc("pa", pa), write_fc("ramsar", ramsar)
    out = os.path.join(OUT, "protected.topo.json")
    ms("-i", a, b, "combine-files", "-rename-layers", "pa,ramsar",
       "-dissolve2", "n,k,s", "target=pa", "-dissolve2", "n,s", "target=ramsar",
       "-simplify", "interval=600", "keep-shapes", "-o", "target=*", "format=topojson", "quantization=4e4", out)
    return {"nationalParks": len({f["properties"]["n"] for f in pa if f["properties"]["k"] == "np"}),
            "sanctuaries": len({f["properties"]["n"] for f in pa if f["properties"]["k"] == "ws"}),
            "ramsar": len({f["properties"]["n"] for f in ramsar})}


# ---------------------------------------------------------------- transport
def build_transport():
    nh = []
    for d in rows(fetch("nh")):
        p = d["properties"]
        if d["geometry"] and p.get("road_type") == "National Highway" and p.get("completi_1") == "Completed":
            nh.append({"type": "Feature", "geometry": d["geometry"], "properties": {"n": clean(p.get("road_name"))}})
    rail = [{"type": "Feature", "geometry": d["geometry"], "properties": {}} for d in rows(fetch("rail")) if d["geometry"]]
    a, b = write_fc("nh", nh), write_fc("rail", rail)
    out = os.path.join(OUT, "transport.topo.json")
    ms("-i", a, b, "combine-files", "-rename-layers", "nh,rail",
       "-dissolve", "n", "target=nh", "-dissolve", "target=rail",
       "-simplify", "interval=1000", "-o", "target=*", "format=topojson", "quantization=4e4", out)
    return {"nationalHighways": len({f["properties"]["n"] for f in nh}), "railSegments": len(rail)}


# ---------------------------------------------------------------- hazards
def india_shape():
    from shapely.geometry import shape
    from shapely.ops import unary_union
    topo = os.path.join(ROOT, "public", "maps", "india-soi-states.topo.json")
    gj = os.path.join(WORK, "states.geojson")
    ms("-i", topo, "-o", "format=geojson", gj)
    return unary_union([shape(f["geometry"]).buffer(0) for f in json.load(open(gj))["features"]])


def build_hazards(india):
    from shapely.geometry import Point
    from shapely.prepared import prep
    inside = prep(india)
    quakes = []
    for d in rows(fetch("quakes")):
        p = d["properties"]
        mw, yr = num(p.get("mw")), num(p.get("yr"))
        lon, lat = num(p.get("long_")), num(p.get("lat"))
        # Body-wave magnitude (mb) saturates near 6.5, so an mb of 9 or more is a catalogue error
        # (one record: 3 July 1996, mb 9.0 at a whole-degree position with zero depth).
        if (num(p.get("magmb")) or 0) >= 9:
            continue
        if mw and mw >= 6 and lon and lat and inside.contains(Point(lon, lat)):
            mo, dt = num(p.get("mo")), num(p.get("dt"))
            date = f"{int(yr):04d}" + (f"-{int(mo):02d}" if mo else "") + (f"-{int(dt):02d}" if mo and dt else "")
            quakes.append({"d": date, "m": round(mw, 1), "z": num(p.get("depth_km")), "lon": round(lon, 3), "lat": round(lat, 3)})
    quakes.sort(key=lambda q: q["d"])
    # The catalogue lists some events once per reporting agency: keep one record per day within 100 km.
    kept = []
    for q in quakes:
        if not any(k["d"] == q["d"] and km((k["lon"], k["lat"]), (q["lon"], q["lat"])) < 100 for k in kept):
            kept.append(q)
    quakes = kept
    with open(os.path.join(OUT, "hazards-points.json"), "w") as f:
        json.dump({"quakes": quakes}, f, separators=(",", ":"))
    fl = write_fc("floods", [{"type": "Feature", "geometry": d["geometry"], "properties": {}} for d in rows(fetch("floods")) if d["geometry"]])
    out = os.path.join(OUT, "hazards.topo.json")
    ms("-i", fl, "-rename-layers", "floods",
       "-dissolve2", "-filter-slivers", "min-area=4km2", "-simplify", "interval=400", "keep-shapes",
       "-o", "target=*", "format=topojson", "quantization=4e4", out)
    return {"earthquakes": len(quakes), "firstYear": quakes[0]["d"][:4], "lastYear": quakes[-1]["d"][:4]}


# ---------------------------------------------------------------- UNESCO World Heritage
# id: (name exactly as on the World Heritage List, year inscribed, category, State/UT codes)
WHS = {
    251: ("Agra Fort", 1983, "C", ["IN-UP"]),
    242: ("Ajanta Caves", 1983, "C", ["IN-MH"]),
    243: ("Ellora Caves", 1983, "C", ["IN-MH"]),
    252: ("Taj Mahal", 1983, "C", ["IN-UP"]),
    249: ("Group of Monuments at Mahabalipuram", 1984, "C", ["IN-TN"]),
    246: ("Sun Temple, Konârak", 1984, "C", ["IN-OR"]),
    337: ("Kaziranga National Park", 1985, "N", ["IN-AS"]),
    340: ("Keoladeo National Park", 1985, "N", ["IN-RJ"]),
    338: ("Manas Wildlife Sanctuary", 1985, "N", ["IN-AS"]),
    234: ("Churches and Convents of Goa", 1986, "C", ["IN-GA"]),
    255: ("Fatehpur Sikri", 1986, "C", ["IN-UP"]),
    241: ("Group of Monuments at Hampi", 1986, "C", ["IN-KA"]),
    240: ("Khajuraho Group of Monuments", 1986, "C", ["IN-MP"]),
    244: ("Elephanta Caves", 1987, "C", ["IN-MH"]),
    250: ("Great Living Chola Temples", 1987, "C", ["IN-TN"]),
    239: ("Group of Monuments at Pattadakal", 1987, "C", ["IN-KA"]),
    452: ("Sundarbans National Park", 1987, "N", ["IN-WB"]),
    335: ("Nanda Devi and Valley of Flowers National Parks", 1988, "N", ["IN-UK"]),
    524: ("Buddhist Monuments at Sanchi", 1989, "C", ["IN-MP"]),
    232: ("Humayun's Tomb, Delhi", 1993, "C", ["IN-DL"]),
    233: ("Qutb Minar and its Monuments, Delhi", 1993, "C", ["IN-DL"]),
    944: ("Mountain Railways of India", 1999, "C", ["IN-WB", "IN-TN", "IN-HP"]),
    1056: ("Mahabodhi Temple Complex at Bodh Gaya", 2002, "C", ["IN-BR"]),
    925: ("Rock Shelters of Bhimbetka", 2003, "C", ["IN-MP"]),
    1101: ("Champaner-Pavagadh Archaeological Park", 2004, "C", ["IN-GJ"]),
    945: ("Chhatrapati Shivaji Terminus (formerly Victoria Terminus)", 2004, "C", ["IN-MH"]),
    231: ("Red Fort Complex", 2007, "C", ["IN-DL"]),
    1338: ("The Jantar Mantar, Jaipur", 2010, "C", ["IN-RJ"]),
    1342: ("Western Ghats", 2012, "N", ["IN-KL", "IN-TN", "IN-KA", "IN-MH"]),
    247: ("Hill Forts of Rajasthan", 2013, "C", ["IN-RJ"]),
    1406: ("Great Himalayan National Park Conservation Area", 2014, "N", ["IN-HP"]),
    922: ("Rani-ki-Vav (the Queen's Stepwell) at Patan, Gujarat", 2014, "C", ["IN-GJ"]),
    1502: ("Archaeological Site of Nalanda Mahavihara at Nalanda, Bihar", 2016, "C", ["IN-BR"]),
    1513: ("Khangchendzonga National Park", 2016, "M", ["IN-SK"]),
    1321: ("The Architectural Work of Le Corbusier, an Outstanding Contribution to the Modern Movement", 2016, "C", ["IN-CH"]),
    1551: ("Historic City of Ahmadabad", 2017, "C", ["IN-GJ"]),
    1480: ("Victorian Gothic and Art Deco Ensembles of Mumbai", 2018, "C", ["IN-MH"]),
    1605: ("Jaipur City, Rajasthan", 2019, "C", ["IN-RJ"]),
    1645: ("Dholavira: a Harappan City", 2021, "C", ["IN-GJ"]),
    1570: ("Kakatiya Rudreshwara (Ramappa) Temple, Telangana", 2021, "C", ["IN-TG"]),
    1670: ("Sacred Ensembles of the Hoysalas", 2023, "C", ["IN-KA"]),
    1375: ("Santiniketan", 2023, "C", ["IN-WB"]),
    1711: ("Moidams – the Mound-Burial System of the Ahom Dynasty", 2024, "C", ["IN-AS"]),
    1739: ("Maratha Military Landscapes of India", 2025, "C", ["IN-MH", "IN-TN"]),
}

# Where UNESCO's own page could not be read, the position comes from another official file.
FALLBACK = {
    246: ("asi", "Ancient Monuments of the Black Pagoda", "Konark"),
    337: ("pa", "Kaziranga National Park Core"),
    1406: ("pa", "Great Himalayan National Park"),
    1513: ("pa", "Khangchendzonga National Park"),
    945: ("station", "CSTM"),
}


def dms(s):
    m = re.match(r"([NS])(\d+) (\d+) ([\d.]+)\s+([EW])(\d+) (\d+) ([\d.]+)", s.strip())
    if not m:
        raise ValueError(s)
    lat = int(m[2]) + int(m[3]) / 60 + float(m[4]) / 3600
    lon = int(m[6]) + int(m[7]) / 60 + float(m[8]) / 3600
    return round(lon if m[5] == "E" else -lon, 5), round(lat if m[1] == "N" else -lat, 5)


def km(a, b):
    dx = (a[0] - b[0]) * 111.32 * math.cos(math.radians((a[1] + b[1]) / 2))
    return math.hypot(dx, (a[1] - b[1]) * 110.57)


def build_heritage():
    from shapely.geometry import shape
    comps = {}
    for line in open(os.path.join(ROOT, "scripts", "maps", "unesco_coords.txt")):
        if not line.strip() or line.startswith("#"):
            continue
        wid, name, c = [x.strip() for x in line.split("|")]
        comps.setdefault(int(wid), []).append({"n": name, "lonlat": dms(c), "src": "unesco"})
    for wid, how in FALLBACK.items():
        if wid in comps:
            continue
        if how[0] == "asi":
            d = next(d for d in rows(fetch("asi")) if d["properties"]["monumentna"] == how[1] and d["properties"]["location"] == how[2])
            ll, src = d["geometry"]["coordinates"], "asi"
        elif how[0] == "pa":
            d = next(d for d in rows(fetch("pa")) if clean(d["properties"]["name"]) == how[1])
            c = shape(d["geometry"]).representative_point()
            ll, src = (c.x, c.y), "moefcc"
        else:
            d = next(d for d in rows(fetch("stations")) if (d["properties"].get("sttncode") or "").strip() == how[1])
            ll, src = d["geometry"]["coordinates"], "ir"
        comps[wid] = [{"n": WHS[wid][0], "lonlat": (round(ll[0], 5), round(ll[1], 5)), "src": src}]
    sites = []
    for wid, (name, year, cat, states) in WHS.items():
        pts = []
        for c in comps.get(wid, []):
            # Components closer than 10 km are drawn as one point at national scale.
            if all(km(c["lonlat"], p["lonlat"]) >= 10 for p in pts):
                pts.append(c)
        sites.append({"id": wid, "name": name, "year": year, "cat": cat, "regions": states,
                      "url": f"https://whc.unesco.org/en/list/{wid}/",
                      "points": [{"n": p["n"], "lon": p["lonlat"][0], "lat": p["lonlat"][1], "src": p["src"]} for p in pts]})
    sites.sort(key=lambda s: (s["year"], s["name"]))
    with open(os.path.join(OUT, "heritage.json"), "w") as f:
        json.dump({"sites": sites}, f, ensure_ascii=False, separators=(",", ":"))
    return {"properties": len(sites), "withoutPosition": [s["name"] for s in sites if not s["points"]],
            "fallback": sorted({s["name"] for s in sites for p in s["points"] if p["src"] != "unesco"})}


# Copy dates are those of the republished files (the date each was taken from the government portal).
SOURCES = {
    "wris-rivers": {"publisher": "India-WRIS (Ministry of Jal Shakti, with ISRO)", "url": "https://indiawris.gov.in/", "copy": "2025-09-16"},
    "wris-lakes": {"publisher": "India-WRIS (Ministry of Jal Shakti, with ISRO)", "url": "https://indiawris.gov.in/", "copy": "2023-12-29"},
    "wris-reservoirs": {"publisher": "India-WRIS (Ministry of Jal Shakti, with ISRO)", "url": "https://indiawris.gov.in/", "copy": "2024-11-27"},
    "moefcc-pa": {"publisher": "Ministry of Environment, Forest and Climate Change, via PM GatiShakti", "url": "https://ugi.pmgatishakti.gov.in/", "copy": "2026-02-13"},
    "moefcc-ramsar": {"publisher": "Ministry of Environment, Forest and Climate Change (Parivesh), via Bharatmaps", "url": "https://bharatmaps.gov.in/", "copy": "2025-01-15"},
    "morth-nh": {"publisher": "Ministry of Road Transport and Highways, via PM GatiShakti (layer updated 30 June 2022)", "url": "https://ugi.pmgatishakti.gov.in/", "copy": "2026-02-16"},
    "ir-tracks": {"publisher": "Indian Railways GIS portal", "url": "https://irgeoportal.gov.in/", "copy": "2023-05-22"},
    "ndem-floods": {"publisher": "National Remote Sensing Centre (ISRO), National Database for Emergency Management", "url": "https://ndem.nrsc.gov.in/", "copy": "2025-02-14"},
    "gsi-quakes": {"publisher": "Geological Survey of India, National Geoscience Data Repository", "url": "https://geodataindia.gov.in/", "copy": "2025-02-13"},
    "unesco": {"publisher": "UNESCO World Heritage Centre", "url": "https://whc.unesco.org/en/statesparties/in", "copy": "2026-10-28"},
    "asi": {"publisher": "Archaeological Survey of India, via Bhuvan (ISRO)", "url": "https://bhuvan.nrsc.gov.in/", "copy": "2025-01-08"},
    "ir-stations": {"publisher": "Indian Railways GIS portal", "url": "https://irgeoportal.gov.in/", "copy": "2023-05-22"},
}

LAYERS = {
    "rivers": {"files": ["rivers.topo.json"], "sources": ["wris-rivers", "wris-lakes", "wris-reservoirs"]},
    "protected": {"files": ["protected.topo.json"], "sources": ["moefcc-pa", "moefcc-ramsar"]},
    "transport": {"files": ["transport.topo.json"], "sources": ["morth-nh", "ir-tracks"]},
    "heritage": {"files": ["heritage.json"], "sources": ["unesco", "asi", "moefcc-pa", "ir-stations"]},
    "hazards": {"files": ["hazards.topo.json", "hazards-points.json"], "sources": ["gsi-quakes", "ndem-floods"]},
}


def write_index(counts):
    idx = {"$comment": "Thematic map layers. Built by scripts/maps/build_layers.py; see docs/MAPS.md.",
           "attribution": ATTRIB, "built": os.environ.get("BD_TODAY", "2026-10-28"),
           "sources": SOURCES,
           "layers": {k: {**v, "counts": counts[k]} for k, v in LAYERS.items()}}
    with open(os.path.join(OUT, "index.json"), "w") as f:
        json.dump(idx, f, ensure_ascii=False, indent=1)


def main():
    os.makedirs(WORK, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    counts = {
        "rivers": build_rivers(),
        "protected": build_protected(),
        "transport": build_transport(),
        "hazards": build_hazards(india_shape()),
        "heritage": build_heritage(),
    }
    print(json.dumps(counts, indent=1, ensure_ascii=False))
    write_index(counts)
    with open(os.path.join(WORK, "counts.json"), "w") as f:
        json.dump(counts, f, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
