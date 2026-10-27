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
- **Open decision:** reuse terms (licence) for Bharat Darshan's own compilation. The page currently asks users to cite the original publisher in each row.

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
- Projects still on news sources: 6 (Shillong–Silchar, Jiribam–Imphal, Dimapur–Kohima, Sivok–Rangpo, Kudankulam 3–6, Rishikesh–Karnaprayag).

## 7. Learn (`/learn`)

- Quiz rounds of 10 from a bank of 270 questions generated at build time: capitals (31), GI products (120), officeholders (59, official sources only, with check date) and number comparisons (60, one indicator and period, no ties).
- Every answer shows its source and links to the profile, GI page or ranking. The bank is served as `/learn-quiz.json` and loaded only on this page. Tests: `tests/quiz.test.ts`.

## Checks

`validate-data`: 0 errors, 1,725 gaps. Unit tests: 90 passing. Accessibility (axe): 35/35 pages clean, including Rankings, Data Library and Learn.

## Next steps

1. Finish the 16 remaining officeholder cards (mostly legislature sites that block automated reading).
2. Move the remaining 6 project cards to official sources (PIB, Lok Sabha answers, NFR/IRCON, NPCIL).
3. District profiles from the LGD index.
4. Choropleth data layers on the map; Trip Planner; offline/PWA.
