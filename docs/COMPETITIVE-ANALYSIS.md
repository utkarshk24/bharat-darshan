# Bharat Darshan: competitive landscape and gap analysis

*Research date: 25 Oct 2026. Based on web research. Feature claims about other sites come from their own pages or from press coverage, as cited below. Where a source did not say something (for example, which languages a site supports), this report says "not stated" rather than guessing.*

## 1. Verdict

No single site I found combines all of Bharat Darshan's core features:

- profiles of all 36 States and UTs,
- in English, Hindi and Marathi,
- with source provenance on every figure,
- an official Survey of India boundary map,
- and encyclopedia, data and governance content side by side.

The space is crowded, but it is split in two:

- **Government data portals** are deep but built for officials and researchers.
- **Encyclopedias, tourism sites and quiz apps** are broad but shallow, and cite few or no sources.

Bharat Darshan sits between the two. That is its niche.

## 2. Existing products

| Product | What it is | Audience | Strengths | Weaknesses compared with Bharat Darshan |
|---|---|---|---|---|
| india.gov.in, "States of India" | Directory of links to State government sites | Citizens | Official, authoritative | A link list only: no data, maps or comparison |
| Know India (knowindia.india.gov.in) | Government state and district profiles: history, culture, geography | Students, general public | Official text; covers districts | Static narrative, few figures, no per-figure provenance, no dashboard |
| NITI for States (NITI Aayog, launched March 2024) | Governance DPI: 7,500 best practices, 5,000 policies, 900+ datasets, 1,400 data profiles; Viksit Bharat Strategy Room; multilingual support through Bhashini | Officials, down to district and block level | Very deep; integrated with NDAP and iGOT; multilingual | Built for policymakers, not citizens or learners; no encyclopedic or cultural layer |
| NITI-NCAER States Economic Forum | State finances portal | Economists, policymakers | Fiscal time series | Fiscal data only |
| ISB India Data Portal 2.0 (launched Oct 2023) | 3,400+ indicators, 120 datasets, 25 domains; built around visualisation | Researchers, journalists | Indicator breadth; user uploads | Languages not stated; no narrative, culture or governance profiles |
| MoSPI eSankhyiki | Official statistics: 2,300+ datasets, ~1.7M records, API | Analysts | Primary source with an API | Raw data with no narrative; language support not stated |
| RBI Handbook of Statistics on Indian States (yearly; 2024-25 edition released) | Annual tables | Economists | Authoritative long time series | Static tables; not interactive |
| Bharat Maps (NIC) | Multi-layer GIS: 23 categories of layers, village-level boundaries, satellite imagery | Government app builders; public viewer | Best official base-map stack | No dedicated statistics module; map services need a login |
| Indian Culture Portal (Ministry of Culture) | Archives, e-books, artefacts, state-wise cultural content | Learners, researchers | Rich primary cultural material | Culture only; no economy or governance data |
| Indiastat | Paid statistical database | Corporates, researchers | Very wide, deep tables | Paywalled; tables, not profiles |
| Statistics Times | State GDP and per-capita rankings | General readers | Simple, clear rankings | No visible source citations; GDP only; English only; no maps |
| Wikipedia (EN, HI, MR and others) | Community encyclopedia | Everyone | Breadth, multilingual, often updated | Sourcing and freshness vary by article; figures are not date-stamped consistently; no dashboard or comparison |
| Incredible India and State tourism sites | Tourism promotion | Travellers | Visuals, itineraries | Promotional; no data; each State is siloed |
| Bharat Darpan (IJERT paper, June 2026) | Student heritage site: map explorer, festivals, monuments, trivia for 36 regions | Students | Same scope idea | Content taken from Wikipedia and Know India and hard-coded; English only; prototype hosted on Replit |
| GK and quiz apps (App Store, Play Store, Microsoft Store) | Capitals, CMs, Governors, map quizzes | Exam aspirants | Gamified; mobile | Typically no sources or `asOf` dates, so officeholder lists can go stale |

## 3. Bharat Darshan's differentiators

1. **Provenance and `asOf` on every figure and officeholder.** I found no citizen-facing competitor doing this.
2. **Honest gaps.** Missing data is shown as "Not available" and logged (1,726 gaps), never estimated.
3. **Marathi alongside Hindi and English.** The data portals list no Marathi interface.
4. **Uniform 26-section profile for all 36 regions.** Every region gets the same structure, so regions can be compared.
5. **A combined view** of encyclopedia, data, governance, GI tags, projects and comparison in one place. Elsewhere this takes 5 to 6 separate sites.
6. **An official Survey of India boundary map** on a citizen product.
7. **Free, no login, a static site.** Indiastat is paid, and Bharat Maps services need a login.
8. **Political neutrality rules** and no unsourced comparative claims.

## 4. Bharat Darshan's gaps compared with competitors

Priority key: P1 = high impact and builds on what already exists; P2 = medium; P3 = later.

| # | Gap | Who does it better | Priority |
|---|---|---|---|
| 1 | No district-level drill-down (index only) and no city profiles | Know India, Bharat Maps | P1 |
| 2 | No data download, API or Data Library page (placeholder) | eSankhyiki, RBI | P1 |
| 3 | No site-wide search | Major portals | P1 |
| 4 | Shallow time series (mostly latest values plus short GSDP series) | RBI Handbook, ISB IDP | P1 |
| 5 | Rankings page is a placeholder | Statistics Times | P1 (cheap: the data already exists) |
| 6 | Freshness: 56 officeholder cards and 9 project cards still rely on third-party sources | Official sites | P1 |
| 7 | Hindi and Marathi strings mostly still marked draft (~30k) | (quality risk rather than a competitive one) | P1 |
| 8 | No choropleth data layers on the map | ISB IDP, Bharat Maps | P2 |
| 9 | No corrections or feedback workflow | Wikipedia (open editing) | P2 |
| 10 | No Learn or quiz mode | Quiz apps, Bharat Darpan | P2 (big audience: exam aspirants) |
| 11 | No offline/PWA or app | Quiz apps | P2 |
| 12 | No SEO or discoverability work yet | Wikipedia, Statistics Times | P2 |
| 13 | Only 3 languages | NITI for States (Bhashini), Wikipedia | P3 |
| 14 | No Trip Planner or tourism layer | Incredible India, State tourism sites | P3 |
| 15 | No PDF or print export of profiles | — | P3 |

## 5. Recommended positioning and next moves

**Positioning:** "The cited, trilingual citizen's handbook to every State and UT. Every number traceable, every gap admitted."

**Next 3 moves (most leverage):**

1. **Rankings, Data Library downloads (CSV/JSON of the existing data) and site search.** All three reuse data already built.
2. **Freshness pass.** Swap third-party sources for official ones, and add a visible "last verified" badge.
3. **District profiles, starting from the LGD index**, plus a Learn/quiz mode built from the existing sourced facts. A quiz with sources and `asOf` dates addresses the main weakness of GK apps.

## Sources

- [india.gov.in, States of India](https://www.india.gov.in/india-glance/states-india)
- [Know India, districts](https://knowindia.india.gov.in/districts/)
- [Outlook Business, NITI for States launch](https://www.outlookbusiness.com/news/vaishnaw-launches-niti-aayogs-digital-public-infrastructure-platform)
- [Business Standard, NITI-NCAER States Economic Forum](https://www.business-standard.com/amp/india-news/nirmala-sitharaman-niti-ncaer-portal-state-finances-125033100367_1.html)
- [ISB, India Data Portal 2.0](https://www.isb.edu/en/news-events/news-grid/ISB-Launches-Revamped-India-Data-Portal-2_0.html)
- [PIB, MoSPI eSankhyiki](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2024/aug/doc202486366701.pdf)
- [RBI, Handbook of Statistics on Indian States 2024-25](https://website.rbi.org.in/web/rbi/-/press-releases/rbi-releases-handbook-of-statistics-on-indian-states-2024-25-)
- [NIC, Bharat Maps](https://informaticsweb.nic.in/sites/default/files/Bharat%20Maps%2C%20A%20Multi-layer%20GIS%20Platform.pdf)
- [Indian Culture Portal (Journals of India)](https://journalsofindia.com/indian-culture-portal/?print=pdf)
- [Indiastat](https://www.indiastat.com/data/geographical-data)
- [Statistics Times, Indian states statistics](https://www.statisticstimes.com/m/economy/indian-states-statistics.php)
- [IJERT, Bharat Darpan (June 2026)](https://www.ijert.org/research/bharat-darpan-a-web-based-interactive-platform-for-preserving-and-promoting-indias-cultural-heritage-IJERTV15IS060917.pdf)
- [App Store, India Map Quiz](https://apps.apple.com/us/app/-/id6757759098)
