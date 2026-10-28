# Maps — official boundaries only (Principle 8)

## What the map uses

| Layer | Source | Notes |
|---|---|---|
| State and UT boundaries, national boundary | **Survey of India** digital boundary data, State/UT level (free product OVSF/1M/7, [onlinemaps.surveyofindia.gov.in](https://onlinemaps.surveyofindia.gov.in/Digital_Product_Show.aspx)) | Downloaded as `SOI_States.geojsonl.7z` from [ramSeraph/indian_admin_boundaries](https://github.com/ramSeraph/indian_admin_boundaries/releases/tag/states) (release "states", file dated 11 Dec 2023), which republishes the SoI file unchanged under CC0. |
| Inter-State disputed areas | Same SoI file (4 areas: MP–Gujarat, MP–Rajasthan, Rajasthan–Gujarat, West Bengal–Bihar–Jharkhand) | Drawn hatched and labelled "as shown by the Survey of India". |
| Capital locations | [Natural Earth](https://www.naturalearthdata.com/) 1:10m populated places (public domain) | Point locations only. Natural Earth is **never** used for any boundary. |
| District boundaries (selected State/UT) | Local Government Directory (LGD) district boundaries via NIC Bharatmaps ([mapservice.gov.in](https://mapservice.gov.in)) | `LGD_Districts.geojsonl.7z` from [ramSeraph/indian_admin_boundaries](https://github.com/ramSeraph/indian_admin_boundaries/releases/tag/districts) (11 Dec 2023, CC0). Its outer boundary matches the SoI file, and it includes Mirpur and Muzaffarabad (PoK) in J&K. |
| Data layers (population, density, literacy, sex ratio, forest cover, per capita income) | The sourced figures already in `data/regions/*.json` | Same provenance as the profiles. |

The National Geospatial Guidelines (DST, 2021, para xiii) say that for political maps of India "SoI published maps or SoI digital boundary data are the standard to be used", that they "shall be made easily downloadable for free", and that "their digital display and printing shall be permissible".

### Check done on 25 October 2026

- 36 features, one per State/UT (keyed by ISO 3166-2 code from the LGD code in the file), plus the 4 inter-State disputed areas.
- Jammu & Kashmir includes the areas under the occupation of Pakistan. Ladakh includes Gilgit-Baltistan and Aksai Chin. Arunachal Pradesh is shown in full.
- Extent 68.18–97.41° E and 6.75–37.09° N.
- `tests/map.test.ts` checks the features, the extent and the capitals on every build.

**Owner check still needed:** look at `/en/map/` and confirm the depiction before treating the map as final.

## Building the files

```bash
pip install py7zr
python3 scripts/maps/build_boundaries.py /tmp/bd-maps
```

This downloads the two inputs and runs `mapshaper@0.6.102` to simplify the boundaries for screen display (Visvalingam, 3%, keep-shapes; about 320 KB). `-clean` builds shared borders between neighbouring States, because the source polygons do not share exact vertices, and resolves gaps and overlaps under 3 km². No boundary is otherwise moved, added or removed. It writes:

- `public/maps/india-soi-states.topo.json` (object `states`, property `iso_code`)
- `public/maps/india-preview.svg`: a static, lighter preview (0.6%) for the home page, so the home page needs no map JavaScript until the reader hovers over or taps the map.
- `public/maps/capitals.json` (Dharamshala and Bhararisain/Gairsain are not in Natural Earth and are listed as `missing`).

`public/maps/manifest.json` names the file. `npm run validate-data` refuses a manifest whose `sourceId` isn't `survey-of-india` or that isn't `verified`, and the app only draws boundaries when both are true. Otherwise it shows the table.

## Districts

`python3 scripts/maps/build_districts.py /tmp/bd-maps` writes one file per region to `public/maps/districts/` (simplified 4%, keep-shapes, about 840 KB in all). A file loads only when a reader selects that State or UT with the Districts overlay on.

District lists change often. The build compares the number of districts in the file with the number in the region's profile. Where they differ, no district boundaries are drawn, and the info card says why. On 25 October 2026 that applied to:

| Region | In file | In profile |
|---|---|---|
| Andhra Pradesh | 26 | 28 |
| Goa | 2 | 3 |
| Gujarat | 33 | 34 |
| Haryana | 22 | 23 |
| Madhya Pradesh | 52 | 55 |
| Rajasthan | 50 | 41 |

Regions without a profile yet are drawn with the file's date shown, and their count is checked when their profile is written. District names are in English, as in LGD, on all three language versions. Hindi and Marathi names need an official source (LGD local-language names).

The older SoI district file (742 districts, with Andhra Pradesh at 13) is not used.

## What the map does

- **Colour by:** Zonal Council region, State or UT, or one of six sourced figures. Data layers use five quantile groups on a validated single-hue ramp, with separate light and dark steps (`--seq-0..4` in `globals.css`).
- **Period rule:** each data layer colours only the regions whose figure is for the most common period. Regions with a figure for another period are striped and named in the legend, and regions with no figure are hatched "Not available yet".
- **Overlays:** State and UT names, capitals (a star for New Delhi), and inter-State disputed areas.
- **Tools:** search for States, UTs and capitals; select a State or UT to zoom to it; zoom buttons, drag to pan, and pinch or Ctrl + scroll to zoom; reset; copy a link to the view (`#theme=…&on=…&r=IN-XX`); download a PNG with the attribution.
- **Accessibility:** every State/UT is a keyboard button with its name and value. There is a full table view, and values are always given as text, never by colour alone.
- **Home page:** a static preview image. It becomes the interactive map, without zoom, on hover or tap, and links to the full map. This keeps Lighthouse mobile performance at its earlier level: the eager map raised Total Blocking Time from about 60 ms to about 1,350 ms in a local test.

## Thematic layers (added 28 October 2026)

Five layers can be drawn over the Survey of India boundaries from **Map layers** on `/map`. Each loads only when switched on, has its own legend, hover names, counts and caveats, and lists its sources (publisher, link and copy date) under the map. The shareable link records them (`on=rivers,heritage…`). Turning a layer on switches the colours to **Plain map**, and the reader can switch back.

All inputs are Indian government datasets as republished, unchanged, by Datameet volunteers ([github.com/ramSeraph](https://github.com/ramSeraph), CC0 1.0, "attribute Datameet and the original government source"), the same route as the boundary file. Built by `scripts/maps/build_layers.py` into `public/maps/layers/` (index in `index.json`). Shapes are simplified for display (about 400 m; 600 m for protected areas; 1 km for roads and rail). Nothing here draws or moves a boundary.

| Layer | Source (copy date) | What is shown | Left out, and why |
|---|---|---|---|
| Rivers and lakes | India-WRIS: rivers (16 Sep 2025), lakes (29 Dec 2023), reservoirs (27 Nov 2024) | 327 major rivers; 17 lakes of 50 km² or more; 36 reservoirs of 100 km² or more | The Rann of Kutch, which WRIS records as a lake (it is a seasonal salt marsh) |
| National parks, sanctuaries, Ramsar sites | MoEFCC via PM GatiShakti (13 Feb 2026); MoEFCC Parivesh via Bharatmaps (15 Jan 2025) | 98 national parks, 554 wildlife sanctuaries, 81 Ramsar sites | Tiger reserves: the only file found mixes reserves with other areas (103 names for about 58 reserves), so it is not used. Areas notified after the copy date |
| National highways and railways | MoRTH via PM GatiShakti (layer of 30 Jun 2022; copy 16 Feb 2026); Indian Railways GIS portal (22 May 2023) | 669 national highways marked completed; all railway lines | Highways under construction or planned. Airports and ports (no official list with locations could be obtained) |
| UNESCO World Heritage Sites | UNESCO World Heritage Centre (coordinates from each property's maps page, read 28 Oct 2026; `scripts/maps/unesco_coords.txt`) | All 44 properties, with each component more than 10 km from another as its own point | Santiniketan has no point: its UNESCO page could not be read and no official fallback was found. For Konark, Kaziranga, Great Himalayan NP, Khangchendzonga and CST the point is the ASI monument, the MoEFCC park boundary or the Indian Railways station |
| Earthquakes and floods | GSI National Geoscience Data Repository (13 Feb 2025); NRSC NDEM all-India flood inundation 1998–2022 (14 Feb 2025) | 41 earthquakes of moment magnitude 6.0+ with epicentres inside India's boundary, 1897–2019; land flooded at least once, 1998–2022 | One catalogue record with body-wave magnitude 9.0 (an impossible value; 3 Jul 1996) and duplicate reports of the same event (same day, within 100 km). Seismic zones: the BIS IS 1893 zone map is not published as data. Cyclone tracks: the NDEM file mixes formats and ends in 2013 |

## State formation timeline (added 28 October 2026)

"How today's States and UTs were formed (1956–2026)" is a **Colour by** option with a year slider (`theme=formation&y=1966`). On today's Survey of India boundaries, each State or UT is coloured by what it was at the end of the chosen year: a State, a Union territory, part of another State or UT, or not yet in the Constitution's list. Names are those of the time (Madras, Mysore, Orissa, Uttaranchal, Pondicherry). Earlier boundaries are not drawn, because the Survey of India publishes only current ones.

Each change cites its Act, with the date it took effect, in `src/components/map/formation.ts`:

- **Appointed days:** read from the Act texts and their Gazette notification footnotes, via India Code and Indian Kanoon reproductions.
- **Amendment-based changes:** for Dadra and Nagar Haveli, Goa, Daman and Diu, Pondicherry and Sikkim, the source is the Constitution (Legislative Department, as on 1 May 2024).
- **Year-only events:** Sikkim's statehood and the Laccadive–Lakshadweep rename show the year only, because the day could not be confirmed from the Act.
- **Keralam (25 August 2026):** the in-force date rests on a third-party report and is marked so.

`tests/thematic.test.ts` checks that, for today, the timeline agrees with the profiles on which units are States and which are UTs.

## Still planned

- **Airports and ports:** needs an official list with locations (AAI aerodrome reference points; the Ministry of Ports' list of major ports).
- **Seismic zones:** BIS IS 1893, once published as data.
- **Tiger reserves:** needs NTCA boundaries.
