# Phase 2 report — Maharashtra reference profile

Date: 13 October 2026 · Status: **Maharashtra complete as a draft; paused for your review before Kerala, Delhi, Ladakh and the India overview**

## What was built

### Module system (applies to all 36 regions)
- **Typed content blocks** (`src/lib/schema.ts` → `Block`): prose, facts (stat cards with previous value, polarity and national comparison), lists (cards / chips / bullets), timeline, time series, table, links, live weather, projects, GI products, officeholders, and "still to be sourced" gap lists.
- **Content files**: one JSON per module at `data/modules/IN-XX/<module>.json`. The profile page renders whatever exists and falls back to the Phase placeholder otherwise.
- **Renderer** (`src/components/blocks/`): `ModuleBlocks`, `SeriesChart` (Recharts; 5y/10y/all range, latest/previous/change, table view, CSV download, colour-blind-safe with dashes), `WeatherWidget` (Open-Meteo, labelled Live), `GIGrid` (category filter), `ProjectCards` (status groups, cost, agency, asOf, source).
- **Validator** now checks module files: schema, known module/region, file path, duplicate block ids, sources on non-editorial prose, table row widths, period and price-base consistency inside each series, and unknown `sourceId`s anywhere. Gap blocks feed the gap report.
- **Fixes**: deterministic date formatting and sorting (server and browser ICU data differ, which caused hydration mismatches in Hindi); mobile header overflow; mobile module tabs scroll to the active tab.

### Maharashtra content
- **All 26 modules** written in English, Hindi and Marathi (all non-English text marked `draft`).
- **157 sourced data points**, all tagged Official, each with source, URL, period, revision status and access date (13 Oct 2026).
- **Verified time-sensitive fields** (asOf 13 Oct 2026):
  - Governor **Jishnu Dev Varma** (sworn in 10 Mar 2026) — Lok Bhavan, Maharashtra. Note: Raj Bhavan has been renamed Lok Bhavan.
  - Chief Minister **Devendra Fadnavis** (since 5 Dec 2024); Deputy CMs **Eknath Shinde** and **Sunetra Pawar** (since 31 Jan 2026, after Ajit Pawar's death in a plane crash) — Government of Maharashtra department pages.
  - 2024 Assembly result, party-wise — ECI.
- **Data series**: GSDP and per capita NSDP FY2011-12 to FY2025-26 (current and constant 2011-12 prices, MoSPI API); sectoral GSVA shares FY2024-25; PLFS unemployment 2022–2025 vs India; AISHE GER 2017-18 to 2021-22; tourist visits 2022–2024.
- **Registries**: all **55 registered GIs** with application numbers and filing dates (GI Registry, as on 31 Dec 2025); 7 UNESCO World Heritage properties; 6 tiger reserves (NTCA); 3 Ramsar sites; 6 major projects with official status.

## Main sources used

MoSPI API (GSDP, NSDP, GSVA, PLFS, AISHE, NFHS) · Lok Sabha answer of 9 Feb 2026 (ISFR 2021/2023 forest cover) · PIB (child sex ratio, SRS 2021, projects, tourism, classical language) · Maharashtra State Data Bank and department portals · ECI results · UNESCO WHC · NTCA · MoEFCC Ramsar list · GI Registry.

## Data gaps — 74 fields for Maharashtra

None were estimated. The biggest groups:

| Area | Missing | Where to get it |
|---|---|---|
| Energy | Installed capacity by source, RE share, per capita use | CEA monthly report (portal blocked automated access) |
| Health | IMR, life expectancy, facilities, anaemia, immunisation | SRS state tables, NFHS-5 fact sheet |
| People | Religion shares, Marathi speakers %, literacy by sex, current population projection, SDG Index score, MPI | Census C-01/C-16, MoHFW projections, NITI Aayog |
| Economy | Share of India's GDP, FDI, debt-to-GSDP, exports, BRAP rank | MoSPI national accounts, DPIIT, RBI |
| Transport | NH km, rail route km, metro km, MSRTC fleet, airport traffic | MoRTH, Indian Railways, metro corporations, AAI |
| Government | Speaker, Leader of Opposition, local-body counts, schemes | Legislature Secretariat, UDD/RDD |
| Geography & climate | Lat/long extent, official coastline, BIS seismic zones, IMD normals | Survey of India, BIS, IMD |
| Symbols | Official notifications for flower, tree, butterfly, fish (animal and bird from the brief) | State GRs |

The full list is in `docs/DATA-GAP-REPORT.md`.

## Things you should check

1. **Editorial content (34 of 95 blocks)** — history timeline, culture, food, places, personalities, city descriptions — is original writing from general knowledge, tagged *Editorial*, with no numbers. It still deserves a subject-matter read.
2. **Hindi and Marathi** are drafts and need native-speaker review. Proper nouns follow each language's usage (नागपुर / नागपूर, नासिक / नाशिक, पुणे, छत्रपति / छत्रपती संभाजीनगर).
3. **Third-party sources** used where no official page was reachable: Bar & Bench for the Kolhapur High Court bench, news reports for Sunetra Pawar's oath date. Both are labelled.
4. **GSDP FY2025-26** is the latest MoSPI year and is marked *provisional*. MoSPI has moved national accounts to a 2022-23 base; State series in that base weren't published yet.
5. **Sensitive topics**: religion data is left as a gap rather than shown from an unreliable table; caste data is limited to Census SC/ST shares; politics shows seats only, in seat order, with neutral styling.
6. **Live weather** can't be tested from the build machine (outbound blocked); it shows a clear "unavailable" message on failure.

## Next (on your confirmation)

Kerala, Delhi (UT with legislature) and Ladakh (UT without legislature) with the same depth, then the India overview and the MH / TN / UP / KL comparison prototype. Much of the MoSPI and Lok Sabha data already fetched covers those regions too.

## Reproducing the content

`scripts/authoring/` holds the Python scripts that produced the Maharashtra JSON, plus the raw research extracts (`research/`). Re-run `python3 scripts/authoring/mh_core.py` and the three `mh_mod*.py` files, then `npm run validate-data`. The JSON in `data/` remains the source of truth for the app; the scripts are a convenience.
