# Phase 2 completion report: India overview and comparison prototype

Date: 13 October 2026. Status: **Phase 2 complete as a draft, awaiting your review before Phase 3.**

Phase 2 now has every deliverable in the brief:
- four reference profiles: Maharashtra, Keralam, Delhi and Ladakh (see the two earlier reports);
- the India overview;
- a comparison prototype for Maharashtra, Tamil Nadu, Uttar Pradesh and Keralam.

## India overview (`/[locale]/india`)

### India at a glance

Population, area, density, sex ratio, child sex ratio, literacy and urban share (Census 2011), forest cover (ISFR 2023), and GDP.

GDP for FY2024-25 is ₹330.68 lakh crore at current prices (MoSPI, base 2011-12, Provisional Estimates). The 2011-12 base keeps it consistent with the State figures. MoSPI's newer 2022-23 base series is not mixed in.

### National officeholders (asOf 13 October 2026)

| Role | Name | Source |
|---|---|---|
| President | Droupadi Murmu | President's Secretariat |
| Prime Minister | Narendra Modi | PMO, news dated 12 October 2026 |
| Vice-President | C. P. Radhakrishnan | Vice-President's Secretariat, page updated 2 September 2026 |
| Lok Sabha Speaker | Om Birla | News On AIR, May 2026 |

### Other sections

- A **GDP series** from FY2011-12 to FY2025-26. Each year shows its latest revision; FY2025-26 is the First Advance Estimate.
- **State economies, FY2024-25**: all 30 States and UTs with a MoSPI value, with:
  - rank;
  - GSDP;
  - computed share of India's GDP, labelled as indicative;
  - nominal growth.

  Assam, Haryana, Nagaland, Ladakh, Lakshadweep and Dadra & Nagar Haveli and Daman & Diu had no FY2024-25 value, so they are listed as gaps.
- **Higher-education GER** for all 36 States and UTs (AISHE 2021-22).
- **National indicators**:
  - jobs: unemployment and labour-force participation (PLFS 2025);
  - births and deaths: IMR, under-five mortality, maternal mortality and fertility (SRS);
  - child health: stunting and institutional births (NFHS-5).
- **Heritage counts**: 45 UNESCO sites, 99 Ramsar wetlands, 58 tiger reserves.
- The home page now links to the overview.

## Comparison prototype (`/[locale]/compare`)

The page compares **18 indicators** across six regions: Maharashtra, Tamil Nadu, Uttar Pradesh, Keralam, Delhi and Ladakh. It opens with Maharashtra, Tamil Nadu, Uttar Pradesh and Keralam selected; you can choose any 2–4.

**How the table works:**
- **One period per row.** Every region's value in a row is for the same period. For example, every GSDP value is FY2024-25, even though MoSPI already has FY2025-26 for Maharashtra and Tamil Nadu. The validator enforces this, and also rejects mixed price bases across regions.
- **India column.** The national figure for the same period sits alongside. For GSDP, it shows India's GDP.
- **Markers.** ↑ and ↓ mark the most and least favourable value among the regions you selected, and only where the direction is clear. Population, GSDP, urban share and forest cover get no marker. The legend says plainly that these are not rankings.
- **Sources.** Every cell has an icon that opens its source, period, revision status, access date and notes.
- **Bars.** Small bars show each value relative to the largest among the selected regions.
- **Missing values.** These show "Not available" and are counted in the gap report.

**Extras:**
- a GSDP trend chart for the selected regions, from FY2011-12 to FY2024-25;
- CSV download;
- a shareable link (`?ids=MH,KL,TN`, the pattern in the brief; older `?r=IN-MH,…` links still work).

The home page's themed comparison cards (for example, Himalayan States) need data that doesn't exist yet. They now open the prototype with a short note saying those comparisons arrive in Phase 3.

### What the prototype shows (FY2024-25 unless stated)

| | MH | TN | UP | KL | India |
|---|---|---|---|---|---|
| GSDP / GDP (₹ lakh crore) | 46.22 | 31.19 | 30.25 | 12.49 | 330.68 |
| Share of India's GDP (%) | 13.98 | 9.43 | 9.15 | 3.78 | — |
| Real GSDP growth (%) | 7.3 | 11.2 | 10.8 | 6.2 | 6.5 |
| Per capita NSDP (₹) | 3,17,801 | 3,61,619 | 1,09,844 | 3,08,338 | not shown |
| Unemployment, 2025 (%) | 2.4 | 3.4 | 2.7 | 4.4 | 3.1 |
| Women's labour-force participation, 2025 (%) | 39.9 | 47.3 | 32.4 | 41.2 | 40.0 |
| Higher-education GER, 2021-22 (%) | 35.3 | 47.0 | 24.1 | 41.3 | 28.4 |
| Stunted children, 2019-21 (%) | 35.24 | 25.04 | 39.71 | 23.41 | 35.47 |

### New data for Tamil Nadu and Uttar Pradesh

Both profiles stay "seed" until Phase 3, but their core figures are now filled in:

**Census 2011** (sex ratio and child sex ratio are girls per 1,000 boys/men)

| | Tamil Nadu | Uttar Pradesh |
|---|---|---|
| Source | State Economics and Statistics department | State Economics and Statistics department |
| Population | 7,21,47,030 | 19,98,12,341 |
| Sex ratio | 996 | 912 |
| Literacy (%) | 80.09 | 67.7 |
| Urban (%) | 48.40 | 22.27 |
| Child sex ratio (PIB) | 943 | 902 |

The State totals and sex ratios were cross-checked against the Puducherry statistics directorate's all-States table.

**Other figures added for both:**
- MoSPI GSDP series;
- PLFS, AISHE and NFHS figures;
- ISFR 2023 forest cover: 20.34% in Tamil Nadu, 6.24% in Uttar Pradesh.

## Also fixed

- **Indian digit grouping in notes.** Some notes and prose built by the authoring scripts printed Western grouping, for example "308,338". They now print "3,08,338" via a new `inr()` helper, and all content was regenerated.
- **Mobile overflow.** The comparison table pushed the page wider than a phone screen. It now scrolls within its own box.
- **Data model:**
  - new officeholder roles: President, Vice-President, Prime Minister and Lok Sabha Speaker;
  - a comparison-file schema and validator;
  - `SourceInfo` gained a compact icon-only mode for dense tables.
- **Tests:** 58 now pass, up from 53. The new tests cover period and price-base mismatches, missing region entries, and validation of the India module.

## Data gaps

**Comparison:**
- Ladakh has no Census, GSDP, maternal mortality, under-five mortality or forest-share values.
- Uttar Pradesh has no SRS figures: the 10 May 2025 PIB release lists only States that met the SDG target.
- Delhi has no maternal mortality figure.

**India overview:**
- per capita national income;
- GDP in the 2022-23 base;
- a current projected population;
- the Chief Justice;
- the national total of registered GIs;
- FY2024-25 GSDP for the six regions missing from MoSPI.

The full list is in `docs/DATA-GAP-REPORT.md`, with 644 gaps in total.

## Please check

1. **Officeholders.** The President's site lists speeches only up to November 2024, so it confirms her title rather than current activity. The Speaker's most recent official mention found is from May 2026.
2. **Computed figures.** GDP shares and real growth rates are my calculations from MoSPI figures, labelled as such. Shares are against national GDP, which is compiled separately from State GSDP, so they need not add up to 100%.
3. **Wording of the ↑/↓ markers.** They compare only the selected regions and appear only where the direction of "better" is uncontroversial.

## What's next: Phase 3

Once you confirm, Phase 3 adds the remaining 32 profiles in batches of five, with the validator run after each batch. It also adds district pages and the official boundary map, once you provide the Survey of India file.

## Reproducing

Run the authoring scripts, then validate:

```
for s in kl_core kl_mod1 kl_mod2 kl_mod3 dl_core dl_mod1 dl_mod2 la_core la_mod tn_up_core india_core compare_data gen_sources_md; do python3 scripts/authoring/$s.py; done
npm run validate-data && npm test && npm run build
```
