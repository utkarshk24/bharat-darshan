# Phase 3 progress report: quality checks and Tamil Nadu

Date: 13 October 2026. Status: **draft, awaiting your review.**

## 1. Quality checks (the MVP release criteria)

**New automated checks:**
- **On every deploy** (`.github/workflows/quality.yml`), against the live GitHub Pages site:
  - Lighthouse on mobile, 3 runs per page with the median taken. The build is marked failed if performance or accessibility is below 90.
  - An axe accessibility scan (WCAG 2.1 AA) of 9 pages in all three languages.
  - A check that every source URL in the dataset still resolves. This is report-only, because government sites are often slow from overseas servers.
- **Weekly and on demand:** the same set of checks.
- **In the build itself:** an offline check that every internal link in the static site resolves (`npm run check:links`). It checks about 3,09,000 links on 3,490 pages, and the deploy stops if any is broken.

**Fixes made to pass them.** These were measured on a local compressing server; the first GitHub run on the real site may differ slightly.

| Page | Performance before → after (median) | Accessibility before → after |
|---|---|---|
| Home (en) | 51 → 88 | 100 → 100 |
| Home (hi / mr) | 76 → 92 / 90 | 100 → 100 |
| Maharashtra profile (hi) | 82 → 92 | 95 → 100 |
| Economy module | 74 → 91 | 97 → 100 |
| Compare (mr) | 53 → 91 | 100 → 100 |
| India overview | 78 → 91 | 95 → 100 |

What changed:
- **Fonts.** The eight regional-script fonts (Tamil, Telugu, Bengali and others) are only used for State names in their own scripts. They are now cut down to the characters actually used: about 800 KB became 73 KB. A test fails if new text needs a character the cut-down fonts lack.
- **Main fonts.** Inter and Noto Sans Devanagari are now preloaded. English pages no longer download an 83 KB font just for the ₹ sign.
- **Charts.** The chart library loads only when a chart scrolls into view.
- **Home page.** The off-screen State cards on the home page skip layout until they are needed.
- **Accessibility:**
  - Screen-reader names now include the visible text (the language buttons, the map tiles).
  - Links inside text and breadcrumbs are underlined.
  - Heading levels no longer skip.
  - One colour-contrast issue is fixed.

The English home page (88) is the one most likely to fall just short of 90.

## 2. Phase 3, batch 1: Tamil Nadu (complete draft)

All 26 sections are written in English, Hindi and Marathi, in the same structure as the Phase 2 profiles.

**Officeholders** (as of 13 October 2026):

| Role | Name | Source |
|---|---|---|
| Governor | Rajendra Vishwanath Arlekar, holding additional charge since 12 March 2026 (also Governor of Keralam) | Lok Bhavan, Tamil Nadu (official) |
| Chief Minister | C. Joseph Vijay (TVK), since 10 May 2026 | News On AIR |
| Speaker | J. C. D. Prabhakar (TVK), since 12 May 2026 | News On AIR |
| Leader of Opposition | Udhayanidhi Stalin (DMK) | News On AIR. Marked *provisional*: formal recognition date not found |

**2026 Assembly result.** TVK 108, DMK 59, AIADMK 47, INC 5, PMK 4, others 11; 234 seats in all. ECI's results page builds its table in the browser, so it couldn't be read here. The tally is therefore marked **third-party verified** and listed as a gap until ECI's Form-20 or statistical report is linked.

**Data added:**
- **Economy (MoSPI):**
  - GSDP series FY2011-12 to FY2025-26;
  - sector shares for FY2024-25, newly fetched (manufacturing is about 18% of GSVA);
  - PLFS jobs data;
  - major crops (Tamil Nadu statistics department, 2022-23).
- **People:** Census 2011 core figures, plus decadal growth (15.61%) and SC 20.0% / ST 1.1%. The SC/ST shares are calculated from the State's official counts.
- **Health:** maternal mortality 49, under-five mortality 14, neonatal mortality 9 (SRS 2021); life expectancy 73.2 years (2016-20); NFHS-5 child nutrition.
- **Education:** higher-education GER for 2017-18 to 2021-22 (47.0% in 2021-22, newly fetched); 62 universities and 2,829 colleges.
- **Tourism:** domestic and foreign visits for 2016–2025 (Lok Sabha answer, March 2026). 2025 is provisional: 35.7 crore domestic and 15.5 lakh foreign.
- **Nature:**
  - forest cover, ISFR 2021 → 2023;
  - all 20 Ramsar sites with dates and areas (more than any other State);
  - five tiger reserves.
- **GIs:** all 74 Tamil Nadu GIs from the Registry list as on 31 December 2025, with Hindi and Marathi names. The GI directory now has 175 products.
- **Projects (4):**

  | Project | Status | Source |
  |---|---|---|
  | Chennai Metro Phase II (₹63,246 crore; first 14.6 km stretch opened 11 October 2026) | Under construction | PMO / News On AIR |
  | New Pamban rail bridge | Completed, April 2025 | PMO |
  | ISRO launch complex, Kulasekarapattinam | Under construction | ISRO |
  | Kudankulam units 3–6 | Under construction | Third-party: The Federal. Marked as such |

- **Heritage:** UNESCO sites (Mahabalipuram, the Chola temples, the Nilgiri railway, the Western Ghats, Gingee Fort); a history timeline; culture, food, festivals, cities, all 38 districts, sports, personalities, diaspora, civic links and trivia.

**Deliberately left blank** (listed in the gap report): the infant mortality rate, because the State's own document gives two different 2020 figures; installed power capacity, because CEA couldn't be reached; and the official top elevation, coastline method, dams, groundwater and district populations.

**Also fixed:** chart titles in Hindi and Marathi had an English "to" (for example "आ.व. 2011-12 to आ.व. 2024-25"). This is now "से … तक" / "ते", and the Keralam and Delhi pages are corrected too. The chart axis note "L = ₹ lakh crore" is now translated.

## Checks run

| Check | Result |
|---|---|
| validate-data | 0 errors, 0 warnings. Gaps rose from 644 to 708 because Tamil Nadu's sections list what is still missing. |
| Tests | 66/66 |
| Type check | clean |
| Static build | 3,490 pages |
| Internal links | ~3,09,000, all resolve |
| Screenshots | Tamil Nadu overview, government, economy, nature, tourism and GI in en/hi/mr, plus 390 px mobile. No page overflow. |

## Please check

1. **Leader of Opposition.** Only a news mention was found for Udhayanidhi Stalin.
2. **Governor.** Arlekar holds additional charge of two States; a full-time appointment may follow.
3. **Seat tally.** It needs the ECI statistical report.
4. **Kudankulam status.** It needs an NPCIL or Department of Atomic Energy page.
5. **Translations.** Hindi and Marathi GI names and the State's text need a native-speaker read.

## Next batch

Uttar Pradesh (core figures already in), Karnataka, Gujarat and West Bengal. Forest cover and SRS figures for these four are already saved in `scripts/authoring/research/notes.md`.
