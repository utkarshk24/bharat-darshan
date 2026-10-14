# Phase 3 progress report

Last updated: 14 October 2026. Status: **draft, awaiting your review.**

Five of the remaining 32 regions are now complete: Tamil Nadu (batch 1), and Uttar Pradesh, Karnataka, Gujarat and West Bengal (batch 2, section 3).

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

**Update, 14 October 2026:** the live-site checks had been failing because of two configuration errors, not because of the site: an invalid Lighthouse preset, and the axe command-line tool's browser driver. Both are fixed, and the axe scan now runs through Playwright (`npm run check:a11y`) on 12 pages, including the new States. The first full run against the live GitHub Pages site **passed**: Lighthouse performance and accessibility were at least 90 on all five pages, axe found no WCAG 2.1 AA violations, and the source-link check completed.

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

## 3. Phase 3, batch 2: Uttar Pradesh, Karnataka, Gujarat, West Bengal

All 26 sections of each profile are written in English, Hindi and Marathi, in the same structure as Tamil Nadu.

**Officeholders** (as of 14 October 2026):

| State | Governor | Chief Minister | Speaker | Leader of Opposition |
|---|---|---|---|---|
| Uttar Pradesh | Anandiben Patel | Yogi Adityanath (BJP) | Satish Mahana | Mata Prasad Pandey (SP) |
| Karnataka | Thaawarchand Gehlot — successor Sudha Yadav appointed 12 Oct 2026 | D. K. Shivakumar (INC), since 3 June 2026 | G. S. Patil (UNI, *third-party*) | R. Ashoka (BJP) (UNI, *third-party*) |
| Gujarat | Acharya Devvrat | Bhupendra Patel (BJP); Deputy CM Harsh Sanghavi | Shankar Chaudhary (*third-party*) | None recognised — listed as a gap |
| West Bengal | R. N. Ravi | Suvendu Adhikari (BJP), since 9 May 2026 | Rathindra Bose (*third-party*) | Disputed after the 2026 Trinamool split — listed as a gap |

Official sources are News On AIR, PMO and PIB unless marked *third-party*.

**Governor appointments of 12 October 2026.** The Rashtrapati Bhavan communiqué also moves Rajendra Arlekar from Keralam to Tamil Nadu and names Om Prakash Mathur Governor of Keralam. The Tamil Nadu and Keralam cards now say so. Each card changes only once the new Governor is sworn in.

**Election results:**
- From ECI's own pages: UP 2022, Karnataka 2023 and Gujarat 2022.
- West Bengal 2026: only the totals reported by News On AIR (BJP 207, Trinamool 80). The full table is a gap until ECI's statistical report is linked.

**Data added for all four States:**
- MoSPI GSDP and per-capita NSDP series (to FY2025-26 for KA, GJ and WB; to FY2024-25 for UP), and sector shares for FY2024-25.
- PLFS 2025 and AISHE GER 2017-18 to 2021-22.
- NFHS-5 nutrition and births, plus SRS mortality, life expectancy and IMR.
- ISFR 2023 forest cover, and every Ramsar site (UP 12, KA 4, GJ 5, WB 2).
- All GIs from the Registry list: UP 78, KA 45, GJ 29, WB 35. The GI directory now has **362 products**.

**Projects:**

| Project | Status | Source |
|---|---|---|
| Noida International Airport, Phase I | Completed | PMO |
| Ganga Expressway | Completed | News On AIR |
| Namma Metro Yellow Line | Completed | PMO |
| Bangalore Metro Phase 3 | Under construction | PMO |
| Mumbai–Ahmedabad HSR, Gujarat section | Under construction | PIB |
| Dholera semiconductor fab | Under construction | PMO |
| Kolkata Metro stretches (Aug 2025) | Completed | PIB |
| Kona Expressway | Under construction | PIB |

**Deliberately left blank** (all listed in the gap report):
- Tourism visit figures for Karnataka, Gujarat and West Bengal. No calendar-year State table could be read, and Karnataka's survey gives only part of a year.
- The 2011 urban share for Gujarat and West Bengal. No official source with the exact figure was reached.
- West Bengal's maternal mortality.
- Crop production for West Bengal.

**Also fixed:**
- The UP tourism citation is a **Rajya Sabha** question (USQ 3180), not Lok Sabha.
- Three statements were removed before publishing because they couldn't be verified:
  - a claim that Kannada has the most Jnanpith Awards;
  - a claim about Kolkata's tram network;
  - a wrongly attributed sports coach.

**Sources added:**
- Economic Survey of Karnataka and Socio-Economic Review of Gujarat. Both are read from OpenCity copies, so replace the links with the State websites in review.
- Karnataka-GIS.
- The Economic Survey of India's statistical appendix.

### Checks run (batch 2)

| Check | Result |
|---|---|
| validate-data | 0 errors, 0 warnings. Gaps 887 (was 746 before batch 2): every new section lists what is still missing. |
| Tests | 66/66 |
| Type check | clean |
| Static build | 4,051 pages |
| Internal links | 3,53,166, all resolve |
| Screenshots | Karnataka government (en), Karnataka economy (hi), Gujarat overview (mr), Gujarat GI, West Bengal government (hi), West Bengal health (mr), West Bengal projects; mobile check at 390 px with no page overflow. |

### Please check (batch 2)

1. **Karnataka Governor.** Update to Sudha Yadav once she is sworn in.
2. **Third-party officeholders.** These need official pages:
   - Karnataka and West Bengal Speakers;
   - Karnataka Leader of Opposition;
   - Gujarat Speaker.
3. **West Bengal.** The Leader of Opposition after the Trinamool split, and the full 2026 seat table.
4. **District lists.** Check Karnataka's 31 (including whether Ramanagara has been renamed) and West Bengal's 23 against State notifications.
5. **Translations.** Hindi and Marathi GI names and the text of the four new profiles need a native-speaker read.

## Next batch

Andhra Pradesh, Telangana, Rajasthan, Madhya Pradesh and Bihar. The comparison page (`/compare`) still covers six regions; adding the five new Phase 3 States to it is a small follow-up.
