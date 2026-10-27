# Phase 4 progress report

*Last updated 27 October 2026.*

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

## Checks

`validate-data`: 0 errors, 1,725 gaps. Unit tests: 82 passing. Accessibility (axe): 33/33 pages clean, including the new Rankings and Data Library pages in all three languages.

## Next steps

1. Finish the 16 remaining officeholder cards (mostly legislature sites that block automated reading).
2. Add per-field sources to project cards, then move the 9 projects to official sources.
3. District profiles from the LGD index; Learn/quiz mode built from sourced facts.
4. Choropleth data layers on the map; corrections/feedback workflow.
