# Maps — official boundaries only (Principle 8)

## What the map uses

| Layer | Source | Notes |
|---|---|---|
| State and UT boundaries, national boundary | **Survey of India** digital boundary data, State/UT level (free product OVSF/1M/7, [onlinemaps.surveyofindia.gov.in](https://onlinemaps.surveyofindia.gov.in/Digital_Product_Show.aspx)) | Downloaded as `SOI_States.geojsonl.7z` from [ramSeraph/indian_admin_boundaries](https://github.com/ramSeraph/indian_admin_boundaries/releases/tag/states) (release "states", file dated 11 Dec 2023), which republishes the SoI file unchanged under CC0. |
| Inter-State disputed areas | Same SoI file (4 areas: MP–Gujarat, MP–Rajasthan, Rajasthan–Gujarat, West Bengal–Bihar–Jharkhand) | Drawn hatched and labelled "as shown by the Survey of India". |
| Capital locations | [Natural Earth](https://www.naturalearthdata.com/) 1:10m populated places (public domain) | Point locations only. Natural Earth is **never** used for any boundary. |
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

This downloads the two inputs and runs `mapshaper@0.6.102` to simplify the boundaries for screen display (Visvalingam, 3%, keep-shapes; about 320 KB). No line is moved, added or removed. It writes:

- `public/maps/india-soi-states.topo.json` (object `states`, property `iso_code`)
- `public/maps/capitals.json` (Dharamshala and Bhararisain/Gairsain are not in Natural Earth and are listed as `missing`).

`public/maps/manifest.json` names the file. `npm run validate-data` refuses a manifest whose `sourceId` isn't `survey-of-india` or that isn't `verified`, and the app only draws boundaries when both are true. Otherwise it shows the table.

## What the map does

- **Colour by:** Zonal Council region, State or UT, or one of six sourced figures. Data layers use five quantile groups on a validated single-hue ramp, with separate light and dark steps (`--seq-0..4` in `globals.css`).
- **Period rule:** each data layer colours only the regions whose figure is for the most common period. Regions with a figure for another period are striped and named in the legend, and regions with no figure are hatched "Not available yet".
- **Overlays:** State and UT names, capitals (a star for New Delhi), and inter-State disputed areas.
- **Tools:** search for States, UTs and capitals; select a State or UT to zoom to it; zoom buttons, drag to pan, and pinch or Ctrl + scroll to zoom; reset; copy a link to the view (`#theme=…&on=…&r=IN-XX`); download a PNG with the attribution.
- **Accessibility:** every State/UT is a keyboard button with its name and value. There is a full table view, and values are always given as text, never by colour alone.
- **Home page:** a compact version without zoom, which links to the full map.

## Planned layers

Each of these is added only with official, sourced data:

- **Districts.** The SoI district file in the same repository is older than the current district list (Andhra Pradesh shows 13 districts), so it is not used. It is needed from SoI or LGD at the current vintage.
- **Rivers and lakes:** India-WRIS.
- **Protected areas and Ramsar sites:** MoEFCC / WII ENVIS.
- **Transport:** NHAI/MoRTH, Indian Railways, AAI, the Ministry of Ports.
- **UNESCO sites:** whc.unesco.org.
- **Seismic zones:** BIS IS 1893.
- **Timeline of State formation, 1956–2019:** the Acts of Parliament.
