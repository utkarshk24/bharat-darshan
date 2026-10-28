# Phase 4 progress report

*Last updated 28 October 2026.*

Phase 4 started from the three quick wins in the competitive analysis (`docs/COMPETITIVE-ANALYSIS.md`), then a freshness pass on officeholder cards.

## 1. Rankings (`/rankings`)

- Every comparison indicator (18) ranked across all 36 regions, or across States and UTs separately.
- Standard competition ranks from the raw published values (1, 2, 2, 4). Size measures (population, GSDP, share, urbanisation, forest cover) are shown as an *order*, not a rank.
- Regions without a published value for the period are listed separately as "Not available"; nothing is estimated.
- CSV download and a shareable link (`?i=<indicator>&scope=state|ut`). Tests: `tests/rank.test.ts`.

## 2. Data Library (`/data`)

- Nine bulk files under `/downloads/`: `indicators.csv/json`, `region-metrics.csv`, `regions.csv`, `officeholders.csv`, `gi-products.csv`, `projects.csv`, `sources.csv`, `glossary.json`.
- One complete JSON profile per region under `/downloads/profiles/IN-XX.json` (region record plus all 26 sections).
- Every row keeps source, period, access date, revision status and confidence; a missing value has status `not_available`. Tests: `tests/exports.test.ts`.
- Licence (decided 28 Oct): Bharat Darshan's compilation is CC BY 4.0 (`DATA-LICENSE.md`); each figure stays under its publisher's terms. Profile JSON files carry a `license` block.

## 3. Search

- Home-page search now also covers GI products, projects, glossary terms and site pages, from `/search-index.json`, which is loaded the first time the search box is used.

## 4. Freshness pass on officeholders

- 40 of the 56 officeholder cards that cited third-party sources now cite an official page (Rashtrapati Bhavan communiqués, News On AIR / Akashvani, PIB/PMIndia, state government, Lok Bhavan and legislature sites), each re-checked on 27 Oct 2026.
- Tripura Speaker resolved: Rampada Jamatia, elected unopposed in March 2026 (Akashvani Shillong, 19 Mar 2026).
- Officeholder cards on official sources: 101 of 117 named cards (was 60 of 116).
- **Still third-party (16):** AP Speaker; CT CM; DL LoP; J&K LG, CM, Speaker; KA Speaker, LoP; KL LoP; MP Dy CM (Rajendra Shukla); PB CM; RJ CM, Dy CM (Bairwa), Speaker; TG Speaker; WB Speaker.
- **Projects (9) unchanged:** official pages exist for Sela Tunnel, NAMO Hospital and Mopa airport, but each confirms only part of the card. Project cards hold one source, so switching would overstate provenance; a per-field source would fix this.
- Details: `scripts/authoring/research/notes.md`, section "Freshness pass, 27 Oct 2026".

## 5. Corrections workflow

- "Suggest a correction" in every source box and in the footer opens a GitHub issue form (`.github/ISSUE_TEMPLATE/correction.yml`) pre-filled with the page, the item and the language. The form requires a link to an official source. Reporters need a free GitHub account.

## 6. Project sources per detail

- Project cards can now list supporting sources, each saying which details it covers. Sela Tunnel, NAMO Hospital and Mopa airport now cite PMIndia as the main source.
- While checking, two cards were found to contain details their cited article did not support. Mopa's concessionaire and Dabolim now cite the Goa Directorate of Civil Aviation, and an unsupported naval-station detail was removed. The NAMO Hospital card now uses PMIndia's wording.
- 28 Oct: five more projects moved to PIB sources (Shillong–Silchar, Jiribam–Imphal, Dimapur–Kohima, Sivok–Rangpo, Kudankulam 3–6), with news reports kept as supporting sources. Details the sources did not support were removed (e.g. "Tamenglong", "Teesta valley", the Jaintia Hills framing). Dimapur–Kohima's length differs between PIB (82.5 km) and NFR figures (78.42 km); both are shown.
- Projects still on news sources: 1 (Rishikesh–Karnaprayag; the only official answer found dates from March 2023).

## 7. Learn (`/learn`)

- Quiz rounds of 10 from a bank of 270 questions generated at build time: capitals (31), GI products (120), officeholders (59, official sources only, with check date) and number comparisons (60, one indicator and period, no ties).
- Every answer shows its source and links to the profile, GI page or ranking. The bank is served as `/learn-quiz.json` and loaded only on this page. Tests: `tests/quiz.test.ts`.

## 8. Performance

- The CI Lighthouse check had failed on 2 of 3 runs. A side-by-side test against the pre-Phase-4 build showed no regression; the GI directory sat at the 90 threshold in both.
- GI directory now sends only the fields the list shows and renders 60 cards first ("Show all" for the rest): HTML 1.46 MB → 549 KB, DOM 7,270 → 891 elements, mobile score 89–90 → 93–94.
- Region summaries no longer carry officeholder notes (131 KB → 112 KB on the home page).

## 9. Map data layers

- The atlas (`/map`) can now colour States and UTs by 12 more comparison indicators (GSDP and growth, unemployment, women's labour-force participation, higher-education GER, stunting, institutional births, child and maternal mortality, urbanisation, child sex ratio), each for one period with its source in the side panel. Added on `/map` only, so the home page stays light. Tests: `tests/maplayers.test.ts`.
- Thematic layers (28 Oct), drawn over the Survey of India boundaries and each loaded only when switched on, with legend, hover names, counts, caveats and a source list:
  - **Rivers and lakes:** India-WRIS.
  - **National parks, sanctuaries and Ramsar sites:** MoEFCC.
  - **National highways and railways:** MoRTH and Indian Railways.
  - **UNESCO World Heritage Sites:** all 44, using UNESCO's own coordinates.
  - **Earthquakes and floods:** magnitude 6+ quakes from the GSI catalogue, 1897–2019; land flooded at least once, 1998–2022, from NRSC.
  - Details and exclusions in `docs/MAPS.md`.
- Not shown, because official data with locations could not be obtained: tiger reserves, airports and ports, BIS seismic zones. They stay on the map's "Coming layers" list with the reason.
- **State formation timeline:** a "Colour by" option with a year slider, 1956–2026. Each of today's States and UTs shows what it was that year, with names of the time, and every change cites its Act and effective date. Tests check that it agrees with today's profiles. Tests: `tests/thematic.test.ts`.
- District profiles are on hold (user decision, 28 Oct): they need a current LGD district list and district tables that cannot be downloaded from this environment; the Dec 2023 boundary file still carries pre-rename names (e.g. Ahmednagar, Aurangabad).

## 10. Maintenance (28 Oct)

- Next.js upgraded 16.4.0 → 16.4.3 for a published security advisory (same-major patch, in the main checkout as chosen).
- GitHub label `correction` created, so correction reports from the site are tagged automatically.

## 11. Offline and installable

- Web app manifest (`app/manifest.ts`) with 192/512 and maskable icons (`scripts/pwa/make-icons.mjs`), so the site can be installed on phones and desktops.
- Service worker (`/sw.js`, generated at build with a new version each deploy; old caches are dropped): pages network-first with saved copies offline (up to 300), hashed assets cache-first, fonts/maps/search/quiz data stale-while-revalidate; Data Library downloads are never cached. The three language home pages, offline pages, fonts and base map are saved on install.
- Offline page in en/hi/mr lists the pages saved on the device and explains that saved figures are as of the last online visit. Tested in Chromium: visited pages open offline from the service worker; downloads are blocked offline as intended. Tests: `tests/pwa.test.ts`.

## 12. Trip Planner (`/trip-planner`)

- Pick a State/UT, 1–7 days and a month: the plan shows the closest authored route (exact length, else the longest shorter one, with a note), the profile's suggested seasons with the chosen month highlighted, key places, airports and links back to the tourism, climate and transport sections. Covers 31 regions.
- Built only from existing profile content; nothing new is asserted. Season labels are read into months (ranges wrap the year end); a month not listed is described as "not listed", not as a bad time. Shareable links (`?r=IN-MH&d=4&m=11`); each region's data (`/trip/IN-XX.json`) loads on demand. Tests: `tests/trip.test.ts`.

## 13. End-to-end tests

- Playwright suite (`e2e/`, `npm run test:e2e`) covering 14 journeys (print view added later): search to a GI page, language switch on a profile, section navigation, the Kerala→Keralam redirect, the 404 page, Compare, Rankings, a map data layer, Data Library CSV columns and licence, a Learn answer, a shared Trip Planner link, the correction link, and offline reading.
- Runs in the Quality checks workflow against the live site after each deploy (job `e2e`), next to Lighthouse and axe.

## 14. Print and PDF export (`…/print`)

- Every State and UT has a printable profile (`/en/states/goa/print`, in all three languages, 108 pages), linked as "Print or save as PDF" from the profile header. Its button opens the browser's print dialog, where "Save as PDF" is a destination.
- One document: cover with codes, capitals, data date and the online address, contents, then all 26 sections, each starting on a new A4 page (Maharashtra: 48 pages, about 2 MB).
- Nothing is dropped from provenance: each figure's source, period, confidence, revision status, check date and link are written out in full, and outside links carry their address in print. Series appear as full tables. Live weather is left out, since a PDF would freeze it without a time. The page states that figures are as of the data date and gives the CC BY 4.0 credit line.
- Printing any normal page also hides the site header, footer and section menu, and prints in light colours.
- Print pages are not indexed by search engines (canonical points to the profile). They add about 100 KB each over the network and about 6% to the site's size.
- No pre-made PDF files: 108 of them would add about 200 MB, and the browser's own PDF keeps the Devanagari fonts exactly as on screen.

## Checks

`validate-data`: 0 errors, 1,725 gaps. End-to-end: 15 journeys (print view and map layers added). Unit tests: 108 passing. Accessibility (axe): 40/40 pages clean, including two print pages.

## Next steps

1. Finish the 16 remaining officeholder cards (mostly legislature sites that block automated reading).
2. Find a current official source for Rishikesh–Karnaprayag (Lok Sabha/Rajya Sabha answers, RVNL).
3. District profiles once a current LGD list and district tables are available.
4. Map layers still missing official data: airports and ports, tiger reserves, BIS seismic zones.
5. Phase 4 items left from the roadmap: Career Explorer and a CMS with roles (both need decisions on scope).
