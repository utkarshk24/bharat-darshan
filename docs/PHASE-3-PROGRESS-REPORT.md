# Phase 3 progress report

Last updated: 16 October 2026. Status: **draft, awaiting your review.**

Fifteen of the remaining 32 regions are now complete: Tamil Nadu (batch 1); Uttar Pradesh, Karnataka, Gujarat and West Bengal (batch 2, section 3); Andhra Pradesh, Telangana, Rajasthan, Madhya Pradesh and Bihar (batch 3, section 4); and Odisha, Jharkhand, Chhattisgarh, Assam and Punjab (batch 4, section 5).

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

1. **Karnataka Governor.** Done: Sudha Yadav was sworn in on 16 October 2026 and the card now shows her (ANI, *third-party* until the Lok Bhavan page is linked).
2. **Third-party officeholders.** These need official pages:
   - Karnataka and West Bengal Speakers;
   - Karnataka Leader of Opposition;
   - Gujarat Speaker.
3. **West Bengal.** The Leader of Opposition after the Trinamool split, and the full 2026 seat table.
4. **District lists.** Check Karnataka's 31 (including whether Ramanagara has been renamed) and West Bengal's 23 against State notifications.
5. **Translations.** Hindi and Marathi GI names and the text of the four new profiles need a native-speaker read.

## 4. Phase 3, batch 3: Andhra Pradesh, Telangana, Rajasthan, Madhya Pradesh, Bihar

All 26 sections of each profile are written in English, Hindi and Marathi, in the same structure as the earlier batches.

**Officeholders** (as of 16 October 2026):

| State | Governor | Chief Minister | Deputy CM(s) | Speaker |
|---|---|---|---|---|
| Andhra Pradesh | S. Abdul Nazeer (ANI, *third-party*) | N. Chandrababu Naidu (TDP), since 12 June 2024 | Pawan Kalyan (JSP) (*third-party*) | C. Ayyanna Patrudu (*third-party*) |
| Telangana | Shiv Pratap Shukla, sworn in 11 March 2026 (IANS, *third-party*) | A. Revanth Reddy (INC), since 7 Dec 2023 (*third-party*) | Mallu Bhatti Vikramarka (*third-party*) | Gaddam Prasad Kumar (*third-party*) |
| Rajasthan | Haribhau Kisanrao Bagde, since 31 July 2024 | Bhajan Lal Sharma (BJP), since 15 Dec 2023 (*third-party*) | Diya Kumari, Prem Chand Bairwa (*third-party*) | Vasudev Devnani (*third-party*) |
| Madhya Pradesh | Mangubhai C. Patel, since 8 July 2021 (*third-party*) | Mohan Yadav (BJP), since 13 Dec 2023 (*third-party*) | Jagdish Devda, Rajendra Shukla (*third-party*) | Narendra Singh Tomar (*third-party*) |
| Bihar | Syed Ata Hasnain, sworn in 14 March 2026 | **Samrat Choudhary (BJP), since 15 April 2026** | Vijay Kumar Chaudhary, Bijendra Prasad Yadav (JD(U)) | Prem Kumar |

Official sources are News On AIR, PMO and the Rashtrapati Bhavan communiqué unless marked *third-party*. Two changes since the original plan were found and used:
- **Telangana:** Jishnu Dev Varma moved to Maharashtra in March 2026 and Shiv Pratap Shukla replaced him.
- **Bihar:** Nitish Kumar resigned in April 2026 after his election to the Rajya Sabha. Samrat Choudhary became the first BJP Chief Minister of Bihar.

Leaders of Opposition are listed as gaps for all five. Andhra Pradesh has no recognised opposition party.

**Census figures for the two divided States.** Tables that still show undivided Andhra Pradesh were not used for State figures. Instead:
- Andhra Pradesh uses the State School Education department's recast of Census 2011 for the 13 residual districts: population 4.96 crore, sex ratio 997, literacy 67.35%, urban 29.47%.
- Telangana uses the MSME-DI Hyderabad State Profile: population 3.50 crore, sex ratio 988, child sex ratio 932, literacy 66.54%, urban 38.88%.
- Andhra Pradesh's child sex ratio is a gap.

**Election results** (from ECI's own pages):
- Andhra Pradesh 2024: TDP 135, JSP 21, YSRCP 11, BJP 8.
- Telangana 2023: INC 64, BRS 39, BJP 8, AIMIM 7, CPI 1.
- Rajasthan 2023: 199 seats declared — BJP 115, INC 69, others 15.
- Madhya Pradesh 2023: BJP 163, INC 66, BAP 1.
- Bihar 2025: only "BJP 89, single largest party" (News On AIR). ECI's results page could not be read as a final table, so the full table is a gap.

**Data added for all five States:**
- MoSPI GSDP and per-capita NSDP series to FY2025-26, and sector shares for FY2024-25.
- PLFS 2025 and AISHE GER 2017-18 to 2021-22.
- NFHS-5 nutrition and births, and SRS figures:
  - Economic Survey 2023-24 table for 2020 IMR and birth rate;
  - life expectancy 2014-18;
  - maternal mortality and under-five mortality for Andhra Pradesh and Telangana only, as these are the only two in the PIB list.
- ISFR 2023 forest cover, and every Ramsar site (AP 1, TG 0, RJ 5, MP 5, BR 6).
- All GIs from the Registry list, including shared ones marked "shared with": AP 22, TG 19, RJ 22, MP 30, BR 16. The GI directory now has **469 products**.
- District lists: AP 28 (Markapuram and Polavaram added from 31 Dec 2025), TG 33, RJ 41 (after nine were cancelled in Dec 2024), MP 55 and BR 38.

**Projects:**

| Project | Status | Source |
|---|---|---|
| Bhogapuram (Alluri Sitarama Raju) airport | Completed (inaugurated 1 Aug 2026) | PMO |
| Amaravati capital works | Under construction | News On AIR |
| Polavaram Phase 1 | Under construction (target March 2026, as of Aug 2024) | Lok Sabha |
| PM MITRA park, Warangal | Completed (inaugurated 10 May 2026) | PMO |
| Zaheerabad industrial area; NH-167 four-laning | Under construction | PMO |
| Rajasthan Refinery, Pachpadra | Completed (dedicated 4 July 2026) | PMO |
| Jaipur Metro Phase 2 | Under construction | PMO |
| Ramjal Setu (PKC–ERCP) link | Announced | News On AIR |
| Ken–Betwa link | Under construction | News On AIR |
| Bhopal Metro priority corridor | Completed (20 Dec 2025) | News On AIR |
| Patna Metro priority corridor | Completed (6 Oct 2025) | News On AIR |
| AIIMS Darbhanga | Under construction | News On AIR |

**Deliberately left blank** (all listed in the gap report):
- The 2011 urban share for Rajasthan, Madhya Pradesh and Bihar.
- Maternal and under-five mortality for Rajasthan, Madhya Pradesh and Bihar.
- Tourism visit figures for all five States.
- The full Bihar 2025 seat table.

**Also fixed:**
- **Maharashtra GI numbers.** Its three shared GIs carried the Registry list's serial numbers instead of application numbers:
  - Kolhapuri Chappal is now 169 (was 164);
  - Nagpur Orange is now 385 (was 167);
  - Warli Painting is now 239 (was 168).
- **`/compare`** now covers 14 regions: the Phase 2 six plus Karnataka, Gujarat, West Bengal and the five new States.
- A data test used Bihar as its example of an empty profile. It now uses Odisha.

**Sources added:**
- AP Educational Statistics 2017-18;
- AP Socio Economic Survey 2024-25;
- MSME-DI Telangana State Profile;
- Telangana Socio Economic Outlook 2024 (OpenCity copy);
- Lok Bhavan Bihar;
- third-party: Scroll, The South First, Free Press Journal, IANS and ETV Bharat.

### Checks run (batch 3)

| Check | Result |
|---|---|
| validate-data | 0 errors, 0 warnings, 1,054 gaps (887 after batch 2) |
| Tests | 66/66 |
| Type check | clean |
| Static build | 4,372 pages |
| Internal links | 3,78,654, all resolve |
| Screenshots | Bihar government (en), Telangana overview (hi), Andhra Pradesh projects (mr), Rajasthan nature (mobile), Madhya Pradesh economy (hi), Compare. No console errors. |

### Please check (batch 3)

1. **Third-party officeholders.** Most of the AP, TG, RJ and MP cards cite news reports. Link the Lok Bhavan and Assembly pages in review.
2. **Bhogapuram airport.** It is marked Completed on the strength of the PMO's inauguration release. Confirm that commercial flights have started.
3. **Polavaram.** Find the official status after the March 2026 target.
4. **Bihar GI entries 536–538.** The Registry list prints these without "(Logo)". They are labelled as logo registrations here because they were filed with other logo marks on 28 Dec 2015.
5. **Translations.** Hindi and Marathi text of the five profiles and their GI names need a native-speaker read.

## 5. Phase 3, batch 4: Odisha, Jharkhand, Chhattisgarh, Assam, Punjab

All 26 sections of each profile are written in English, Hindi and Marathi, in the same structure as the earlier batches.

**Officeholders** (as of 16 October 2026):

| State | Governor | Chief Minister | Deputy CM(s) | Speaker |
|---|---|---|---|---|
| Odisha | Hari Babu Kambhampati, since 3 Jan 2025 | Mohan Charan Majhi (BJP), since 12 June 2024 | K. V. Singh Deo, Pravati Parida | Surama Padhy (*third-party*) |
| Jharkhand | Santosh Kumar Gangwar, since 31 July 2024 | Hemant Soren (JMM), since 28 Nov 2024 | — | Rabindra Nath Mahato |
| Chhattisgarh | Ramen Deka, since 31 July 2024 (*third-party*) | Vishnu Deo Sai (BJP), since 13 Dec 2023 (*third-party*) | Arun Sao, Vijay Sharma | Raman Singh (*third-party*) |
| Assam | Lakshman Prasad Acharya, since 30 July 2024 | **Himanta Biswa Sarma (BJP), second term from 12 May 2026** | — | Ranjeet Kumar Dass (from May 2026) |
| Punjab | Gulab Chand Kataria, since 31 July 2024 | Bhagwant Mann (AAP), since 16 Mar 2022 (*third-party*) | — | Kultar Singh Sandhwan (*third-party*) |

Official sources are News On AIR unless marked *third-party*. Points to note:
- **Assam 2026 election:** the NDA won 102 of 126 seats — BJP 82, AGP 10, BPF 10 (News On AIR). The new Speaker was elected in May 2026; his party is not stated in the source used.
- **Odisha Governor:** a communiqué reported on 13 October 2026 appoints **Braj Mohan Ram** as Governor of Odisha. Reports say he will be sworn in on 18 October. The card still shows Dr Kambhampati, with a note. Update it once the oath is taken.
- **Jharkhand 2024 election:** INDIA bloc 56, NDA 24, JLKM 1 (News On AIR).
- Party-wise results for Odisha 2024, Chhattisgarh 2023 and Punjab 2022 are listed as gaps (to be taken from ECI).

**Assam's economy figures come from the CAG.** MoSPI's state-wise API has no Assam series. The GSDP (₹6,43,667 crore, FY2024-25) and per capita income (₹1,59,185) come from the CAG's State Finances Audit Report of Assam 2024-25. So do the sector shares quoted in the text: tertiary 38%, primary 33%, secondary 20%. Assam has no GSDP chart or sector table, and it shows "Not available" for GSDP on `/compare`, which uses MoSPI only.

**Latest year differs by State.** MoSPI publishes FY2025-26 for Odisha and Chhattisgarh but only up to FY2024-25 for Jharkhand and Punjab. Each profile uses its own latest year and says so.

**Data added for all five States:**
- **Census 2011 basics:** population, sex ratio and density (Puducherry DES table), child sex ratio (PIB), literacy (Economic Survey table 8.5), and SC/ST shares (Delhi Planning table 17.2). Punjab has the highest SC share of any State (31.9%) and no Scheduled Tribes.
- **PLFS:** unemployment 2022–2025 and labour-force participation 2025. Chhattisgarh's women's participation (59.8%) is far above the national 40.0%; Punjab's (30.2%) is well below it.
- **AISHE:** GER 2017-18 to 2021-22 by sex, plus university and college counts.
- **NFHS-5:** child nutrition and institutional births. Assam's wasting and underweight rose between NFHS-4 and NFHS-5.
- **SRS:**
  - 2020 infant mortality, birth and death rates (Economic Survey 2023-24 table 8.2);
  - life expectancy 2014-18 for Odisha, Assam and Punjab;
  - Jharkhand and Chhattisgarh are not in table 8.1, so their life expectancy is a gap.
- **ISFR 2023 forest cover and every Ramsar site:** Odisha 6, Jharkhand 1 (Udhwa), Chhattisgarh 1 (Kopra Jalashay, 2025), Assam 1 (Deepor Beel), Punjab 6.
- **GIs from the Registry list:**
  - Odisha 27, including Araku coffee shared with Andhra Pradesh;
  - Jharkhand 1;
  - Chhattisgarh 7;
  - Assam 42, including two shared with Arunachal Pradesh;
  - Punjab 2, both shared (Basmati and Phulkari).
  - The GI directory now has **545 products**.
- **District lists:** Odisha 30, Jharkhand 24, Chhattisgarh 33 and Punjab 23. Assam's districts were merged and re-formed in 2022–24, so its list is a gap until the current notification is linked.

**Projects:**

| Project | Status | Source |
|---|---|---|
| SiCSem silicon-carbide fab, Bhubaneswar | Announced (Cabinet approval 12 Aug 2025) | PMO |
| 3D Glass Solutions packaging unit, Bhubaneswar | Announced (same approval) | PMO |
| Deoghar airport | Completed (12 July 2022) | New India Samachar (PIB) |
| NMDC steel plant, Nagarnar | Completed (dedicated 3 Oct 2023), about ₹24,000 crore | News On AIR |
| Antagarh–Taroki rail line | Completed (3 Oct 2023) | News On AIR |
| Bogibeel rail-cum-road bridge | Completed (25 Dec 2018), ₹5,920 crore | New India Samachar (PIB) |
| Tata semiconductor unit, Jagiroad | Under construction, ₹27,000 crore | PIB (Nov 2024) |
| AIIMS Bathinda | Completed (25 Feb 2024) | PMO |
| CDIL power-semiconductor expansion, Mohali | Announced (12 Aug 2025) | PMO |

The Jagiroad plant is kept as "Under construction". Reports in 2026 describe pilot production, but no official source yet confirms full operation.

**Deliberately left blank** (all listed in the gap report):
- The 2011 urban share for all five States.
- Maternal and under-five mortality for all five.
- Life expectancy for Jharkhand and Chhattisgarh.
- Assam's GSDP series and sector table.
- Assam's district list.
- Tourism visit figures for all five.
- Unsourced numbers were removed from the text rather than estimated, for example the death toll of Odisha's 1999 super cyclone and the evacuation totals for Phailin and Fani.

**Also changed:**
- `/compare` now covers 19 regions.
- The axe scan covers 18 pages, adding Assam GI (en), Odisha health (hi) and Punjab economy (mr).
- The data test's example of an empty profile is now Haryana.
- **Sources added:** New India Samachar (PIB). Third-party: Deccan Herald, The Statesman, The Hitavada and OdishaBytes.

### Checks run (batch 4)

| Check | Result |
|---|---|
| validate-data | 0 errors, 0 warnings, 1,295 gaps (1,054 after batch 3) |
| Tests | 66/66 |
| Type check | clean |
| Static build | 4,600 pages |
| Internal links | 3,96,786, all resolve |
| Accessibility (axe, WCAG 2.1 AA) | 18/18 pages clean |
| Screenshots | Odisha overview (en), Jharkhand government (en), Chhattisgarh economy (hi), Assam GI (mobile), Punjab people (mr), Compare. No console errors. |

### Please check (batch 4)

1. **Odisha Governor.** Switch the card to Braj Mohan Ram once he is sworn in. Reports give 18 October.
2. **Assam GSDP.** Confirm the CAG figures against the Assam Economic Survey. Check that "per capita income" in the CAG report means per capita NSDP at current prices.
3. **Third-party officeholders.** Chhattisgarh (Governor, CM, Speaker), Punjab (CM, Speaker) and the Odisha Speaker cite news reports. Link the Raj Bhavan and Assembly pages in review.
4. **Udhwa Lake's Ramsar date.** The MoEFCC list prints it as 08-01-2024. Check this against the Ramsar Sites Information Service; it is shown as printed.
5. **ISO code.** The hero shows "IN-OR" for Odisha, which is the site's internal code. Check whether the published ISO 3166-2 code is now IN-OD before relying on it.
6. **Translations.** Hindi and Marathi text of the five profiles, especially the 42 Assam GI names (many Bodo terms), need a native-speaker read.

## Next batch

Haryana, Himachal Pradesh, Uttarakhand, Jammu and Kashmir, and Goa (proposed).
