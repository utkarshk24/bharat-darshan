# Maps — official boundaries only (Principle 8)

## Current state

No boundary file is bundled. Freely available India GeoJSON/TopoJSON files frequently show boundaries that differ from the Government of India's position, and none could be verified from the build environment. Rather than risk it, the site renders a **tile-grid cartogram**: one rounded square per State/UT placed by approximate position. It draws no boundaries, says so in its caption, and is fully keyboard- and screen-reader-accessible, with a table alternative.

## Installing the official boundary file

1. Obtain the political map of India from the **Survey of India** (surveyofindia.gov.in) in a vector format and convert it to TopoJSON (e.g. with `mapshaper`), keeping the official boundaries unchanged. Simplification is fine; changing boundary geometry is not.
2. Each State/UT feature must carry its ISO 3166-2 code (e.g. `IN-MH`) in a property, by default `iso_code`.
3. Put the file in `public/maps/` and update `public/maps/manifest.json`:

```json
{
  "boundaries": {
    "file": "india-soi-2026.topo.json",
    "format": "topojson",
    "object": "states",
    "idProperty": "iso_code",
    "sourceId": "survey-of-india",
    "verified": true,
    "verifiedBy": "<reviewer name>",
    "verifiedOn": "YYYY-MM-DD"
  }
}
```

4. Have a reviewer confirm that the whole of Jammu & Kashmir, Ladakh and Arunachal Pradesh are shown as per the Government of India, then set `verified: true`.
5. `npm run validate-data` refuses any manifest whose `sourceId` isn't `survey-of-india` or that isn't `verified`. The app only mounts the boundary map (`GeoMap`) when both are true; otherwise it keeps the tile grid.

District boundaries (Phase 3) follow the same rule.
