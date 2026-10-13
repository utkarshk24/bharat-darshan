# Phase 2 report: Keralam, Delhi and Ladakh

Date: 13 October 2026.

**Status:** draft. All four reference profiles now exist. The India overview and the MH / TN / UP / KL comparison prototype are paused until you review.

## What was built

### Three new profiles: all 26 modules, in English, Hindi and Marathi

All Hindi and Marathi text is marked as a draft. The table counts series points individually, and gaps are fields shown as "Still to be sourced".

| | Keralam (State) | Delhi (UT with legislature) | Ladakh (UT without legislature) |
|---|---|---|---|
| Sourced data points | 132 | 139 | 32 |
| Content blocks (editorial) | 92 (38) | 84 (32) | 73 (34) |
| Gaps listed on pages | 63 | 48 | 39 + 10 core metrics |
| Registered GIs | 41 (4 shared) | 1 (Basmati, shared) | 4 |
| Projects with official status | 1 | 2 | 1 |

### Kerala is now Keralam

The new name took effect on **25 August 2026**:
- The Kerala (Alteration of Name) Bill 2026 was introduced in the Lok Sabha on 10 August 2026 and passed the next day. The Rajya Sabha passed it on 12 August (PRS).
- An MHA notification brought the name into force on 25 August (reported by Onmanorama; the Gazette link is still pending).

How the site handles it:
- **Address:** the profile is now at `/[locale]/states/keralam`. Old `/states/kerala/...` addresses return a permanent (308) redirect, which is tested.
- **Former name:** the page shows "formerly Kerala", and searching for "Kerala", "केरल" or "केरळ" still finds it.
- **ISO code:** IN-KL is unchanged.
- **Names in Hindi and Marathi:** केरलम and केरळम. These are drafts, so please confirm them.

### Time-sensitive facts (asOf 13 Oct 2026)

| Region | Role | Holder | Source |
|---|---|---|---|
| Keralam | Governor | Rajendra Vishwanath Arlekar (in office since January 2025) | UNI, June 2026 *(third-party)* |
| Keralam | Chief Minister | V. D. Satheesan (INC), sworn in 18 May 2026 | News On AIR |
| Keralam | Speaker | Thiruvanchoor Radhakrishnan (INC) | News On AIR, 22 May 2026 |
| Keralam | Leader of Opposition | Pinarayi Vijayan (CPI(M)) | Kerala Kaumudi *(third-party)* |
| Delhi | Lieutenant Governor | Taranjit Singh Sandhu, took charge 11 March 2026 | Lok Niwas (lg.delhi.gov.in) |
| Delhi | Chief Minister | Rekha Gupta (BJP), sworn in 20 February 2025 | News On AIR |
| Delhi | Speaker | Vijender Gupta (BJP) | News On AIR, January 2026 |
| Delhi | Leader of Opposition | Atishi (AAP) | The Pioneer, August 2026 *(third-party)* |
| Ladakh | Lieutenant Governor | Vinai Kumar Saxena, sworn in 13 March 2026 | News On AIR; UT portal |

Ladakh has no elected government, and the page says so plainly.

Election results are taken from ECI, show seats only, use no party colours and list parties in order of seats won:
- Keralam 2026: 140 seats
- Delhi 2025: 70 seats

### Main data series

**Keralam and Delhi:**
- GSDP and per capita NSDP from FY2011-12 to FY2024-25, at current and constant prices (MoSPI). FY2025-26 has not been published for either.
- Sectoral GSVA shares for FY2024-25.
- PLFS unemployment for 2022–25, compared with India.
- AISHE gross enrolment ratio (GER).
- NFHS-5 child nutrition, shown against NFHS-4.
- SRS mortality figures.
- ISFR forest cover.

**Delhi only:**
- Population at each census from 1951 to 2011, from the Economic Survey of Delhi 2023-24.
- A separate, labelled MoHFW projection for 2026 of 2.25 crore.

**Ladakh:** PLFS (including women's labour-force participation of 61%, against 40% nationally), AISHE, NFHS-5, forest cover, its two Ramsar sites and four GIs.

### Projects (status only where an official source exists)

| Project | Status | Source |
|---|---|---|
| Vizhinjam International Seaport, Phase 1 | Completed (May 2025) | PIB / News On AIR |
| Delhi–Meerut Namo Bharat, full 82 km corridor | Completed (22 Feb 2026) | News On AIR |
| Delhi Metro Phase IV | Under Construction | Cabinet approval, March 2024 |
| Zojila tunnel | Under Construction | Lok Sabha answer, August 2024 |

The official completion date for the Zojila tunnel was 29 September 2026. Later news reports suggest it has slipped, so the page says an official update is needed.

### Small fixes along the way

- **State symbols:** labels for flower, tree, butterfly, fish and fruit are now translated. They had been showing as raw English keys, Maharashtra included.
- **Units on ratio cards:** "females per 1,000 males" and "girls per 1,000 boys (0–6 yrs)" now appear in Hindi and Marathi.
- **Lists of official links:** the misleading "Awaiting verified source" footer no longer appears when every item already carries its own source.
- **India density:** the national figure of 382 was added, so density cards now show the India comparison.
- **Tests:** 53 tests now pass, up from 48. The new tests check that all four profiles have 26 modules, that the Keralam redirect and former name work, and that a UT without a legislature has no head of government.

## Data gaps

None of these were estimated.

### Ladakh's core Census figures

These are left as **Not available**. District Kargil's site gives Kargil's population as 1,40,802, and the page shows that figure as a district table. I couldn't reach an official page with the Leh district total, so I haven't shown a UT total.

Area is also left blank:
- India's official map includes areas under the occupation of Pakistan and China.
- District sites give administered areas instead.
- Both figures are needed, each clearly labelled.

MoSPI publishes no GSDP for Ladakh.

### Other gaps

| Area | Missing | Where to get it |
|---|---|---|
| People | Religion and mother-tongue shares, SC/ST shares, literacy by sex for Keralam | Census C-01, C-16 and PCA tables |
| Health | Infant mortality rate, life expectancy and facilities for all three; maternal mortality for Delhi | SRS, NFHS-5 fact sheets |
| Tourism | Visitor numbers for all three | India Tourism Statistics, State tourism departments |
| Energy, transport | Installed capacity, highway and rail length, metro ridership, airport traffic | CEA, MoRTH, Railways, DMRC/KMRL, AAI |
| Government | Ladakh's council heads (LAHDC CECs); Delhi's MCD Mayor; official pages for the Keralam Governor and Leader of Opposition | Council websites, Legislature sites |
| Keralam | Areas of the Ramsar sites and tiger reserves | MoEFCC Ramsar list, NTCA |

The full list is in `docs/DATA-GAP-REPORT.md` (626 gaps across all 37 files).

## Please check

1. **Third-party citations** are used for four facts. Each is labelled and should be swapped for an official page when one is available:
   - the Keralam Governor's currency (UNI)
   - the Keralam Leader of Opposition (Kerala Kaumudi)
   - the Delhi Leader of Opposition (The Pioneer)
   - the date the Keralam name took effect (Onmanorama)
2. **Editorial blocks** cover history, culture, food, places, personalities and so on: 38 in Keralam, 32 in Delhi and 34 in Ladakh. They are original writing and are tagged as editorial, but they need a subject-matter read.
3. **Sensitive topics:**
   - **Ladakh:** the page notes that groups are seeking safeguards and statehood, and that talks are under way, without taking sides.
   - **Delhi:** it notes the 239AA division of powers without commenting on the disputes over it.
   - **Ladakh's boundaries:** these are described as shown on India's official map.
4. **Hindi and Marathi** need review by native speakers. Proper nouns follow each language's usual spelling, for example तिरुवनंतपुरम, कोच्चि / कोची, लद्दाख / लडाख and ज़ोजिला / झोजिला.
5. **Ladakh's Tibetan-script name** is left out for now, because no Tibetan font is bundled and it would show as empty boxes.

## Next (after your confirmation)

1. The India overview.
2. The MH / TN / UP / KL comparison prototype.

The MoSPI, PLFS, AISHE and NFHS extracts in `scripts/authoring/research/` already cover most of what the comparison needs.

## Reproducing the content

Run these authoring scripts in order, then `npm run validate-data`:

```
python3 scripts/authoring/sources_p2b.py
for s in kl_core kl_mod1 kl_mod2 kl_mod3 dl_core dl_mod1 dl_mod2 la_core la_mod; do python3 scripts/authoring/$s.py; done
```

The shared helpers are in `scripts/authoring/common.py`, and the research notes are in `scripts/authoring/research/notes.md`.
