# SOURCES

Generated from `data/sources.json` by `scripts/authoring/gen_sources_md.py` — edit the JSON, not this file. Order within each category is the order of preference (Section 15). Every data point references a source by `sourceId`; the validator rejects unknown ids. Sources whose publisher is marked *third party* are used only where no official page was reachable, and are labelled in the UI.

## Demographics

| id | Source | Publisher | Notes |
|---|---|---|---|
| `census` | [Census of India / Office of the Registrar General & Census Commissioner](https://censusindia.gov.in) | ORGI, Ministry of Home Affairs | Census 2011 is the last completed census; Census 2027 in progress — switch only on official release. |
| `srs` | [Sample Registration System (SRS) Bulletins and Statistical Reports](https://censusindia.gov.in) | ORGI, Ministry of Home Affairs | Annual IMR, MMR (special bulletin), sex ratio at birth, life expectancy (abridged life tables). |
| `mohfw-projections` | [Report of the Technical Group on Population Projections](https://main.mohfw.gov.in) | National Commission on Population, MoHFW | Use for current population estimates; always label 'Projected'. |
| `mh-sdb` | [Maharashtra State Data Bank — Maharashtra's comparison with India](https://mahasdb.maharashtra.gov.in) | Directorate of Economics & Statistics, Government of Maharashtra | State-published compilation of Census and other official figures. |
| `kargil-nic` | [District Kargil — Demography](https://kargil.nic.in) | District Administration Kargil |  |
| `tn-des` | [Tamil Nadu at a Glance / Select Socio-Economic Indicators of Tamil Nadu and India](https://des.tn.gov.in) | Department of Economics and Statistics, Government of Tamil Nadu | State-published compilation of Census 2011 figures. |
| `up-des` | [Uttar Pradesh in Figures / UP at a Glance](https://updes.up.nic.in) | Economics & Statistics Division, State Planning Institute, Government of Uttar Pradesh | State-published compilation of Census 2011 figures. |
| `jk-des` | [Directorate of Economics and Statistics, Jammu and Kashmir](https://ecostatjk.nic.in) | Planning, Development & Monitoring Department, Government of Jammu and Kashmir |  |
| `py-des` | [State-wise Population, Census 2011](https://statistics.py.gov.in/state-wise-population) | Directorate of Economics and Statistics, Government of Puducherry (citing ORGI) | Used as a cross-check of State totals and sex ratios. |
| `ap-cse` | [Educational Statistics 2017-18 (Commissionerate of School Education)](https://cse.ap.gov.in) | Government of Andhra Pradesh | Gives Census 2011 figures recast for the residual (post-2014) State of Andhra Pradesh. |
| `msme-di` | [State Profile of Telangana 2015-16 (MSME-Development Institute, Hyderabad)](https://dcmsme.gov.in) | Ministry of MSME, Government of India | Gives Census 2011 figures recast for the State of Telangana. |

## Economy

| id | Source | Publisher | Notes |
|---|---|---|---|
| `mospi` | [Ministry of Statistics and Programme Implementation — State-wise GSDP/NSDP](https://mospi.gov.in) | MoSPI | Record price base and base year (currently 2011-12) for every value. |
| `rbi-handbook` | [Handbook of Statistics on Indian States](https://www.rbi.org.in) | Reserve Bank of India | Fiscal indicators incl. debt-to-GSDP; also republishes MoSPI GSDP series. |
| `state-economic-survey` | [State Economic Surveys and Budget documents](https://igod.gov.in) | State finance/planning departments | Link the specific state document; igod.gov.in lists state portals. |
| `plfs` | [Periodic Labour Force Survey (PLFS)](https://mospi.gov.in) | MoSPI / NSO | Unemployment rate and LFPR; state the reference period (calendar year, usual status). |
| `kl-spb` | [Economic Review (Kerala State Planning Board)](https://spb.kerala.gov.in) | Kerala State Planning Board, Government of Kerala | State-published compilation of Census 2011 and economic data. |
| `dl-planning` | [Economic Survey of Delhi 2023-24](https://delhiplanning.delhi.gov.in) | Planning Department, Government of NCT of Delhi |  |
| `dpiit` | [Department for Promotion of Industry and Internal Trade](https://dpiit.gov.in) | DPIIT, Ministry of Commerce & Industry | FDI equity inflows (state-wise from Oct 2019); BRAP rankings. |
| `es-india` | [Economic Survey, Statistical Appendix](https://www.indiabudget.gov.in) | Ministry of Finance, Government of India |  |
| `startup-india` | [Startup India — DPIIT-recognised startups](https://www.startupindia.gov.in) | DPIIT |  |
| `hr-finance` | [Haryana Finance Department — FRBM statements laid in the Vidhan Sabha](https://cms.neva.gov.in) | Government of Haryana (via NeVA) |  |
| `cag` | [Comptroller and Auditor General of India — State Finances Audit Report](https://cag.gov.in) | Office of the Comptroller and Auditor General of India |  |
| `ka-des` | [Economic Survey of Karnataka (Planning, Programme Monitoring and Statistics Department)](https://des.karnataka.gov.in) | Government of Karnataka | The PDFs are linked from the OpenCity data portal copy of the Government of Karnataka publication; replace with the des.karnataka.gov.in link in review. |
| `gj-des` | [Socio-Economic Review, Gujarat State (Directorate of Economics and Statistics)](https://gujecostat.gujarat.gov.in) | Government of Gujarat | The PDF is linked from the OpenCity data portal copy of the Government of Gujarat publication; replace with the gujecostat link in review. |
| `ap-fin` | [Socio Economic Survey 2024-25 (Planning Department)](https://apfinance.gov.in) | Government of Andhra Pradesh | The PDF is served from the Finance Department's document store (apfinance.gov.in). |
| `tg-plan` | [Telangana Socio Economic Outlook 2024 (Planning Department)](https://www.telangana.gov.in) | Government of Telangana | The PDF is linked from the OpenCity data portal copy of the Government of Telangana publication; replace with the State link in review. |

## Development

| id | Source | Publisher | Notes |
|---|---|---|---|
| `niti` | [NITI Aayog — SDG India Index and National Multidimensional Poverty Index](https://www.niti.gov.in) | NITI Aayog |  |

## Health

| id | Source | Publisher | Notes |
|---|---|---|---|
| `nfhs` | [National Family Health Survey (NFHS)](https://rchiips.org/nfhs) | IIPS / MoHFW | Survey rounds: NFHS-3 (2005-06), NFHS-4 (2015-16), NFHS-5 (2019-21); periodType 'survey'. |
| `mohfw` | [Ministry of Health and Family Welfare / National Health Mission](https://main.mohfw.gov.in) | MoHFW |  |

## Education

| id | Source | Publisher | Notes |
|---|---|---|---|
| `udise` | [UDISE+](https://udiseplus.gov.in) | Ministry of Education |  |
| `aishe` | [All India Survey on Higher Education (AISHE)](https://aishe.gov.in) | Ministry of Education |  |
| `nirf` | [National Institutional Ranking Framework (NIRF)](https://www.nirfindia.org) | Ministry of Education |  |

## Environment

| id | Source | Publisher | Notes |
|---|---|---|---|
| `fsi` | [India State of Forest Report (ISFR)](https://fsi.nic.in) | Forest Survey of India, MoEFCC | Biennial: ISFR 2019, 2021, 2023. |
| `moefcc` | [Ministry of Environment, Forest and Climate Change](https://moef.gov.in) | MoEFCC |  |
| `ntca` | [National Tiger Conservation Authority](https://ntca.gov.in) | NTCA, MoEFCC |  |
| `ramsar` | [Ramsar Sites Information Service](https://rsis.ramsar.org) | Ramsar Convention Secretariat |  |
| `indian-wetlands` | [Ramsar Sites of India (MoEFCC list)](https://indianwetlands.in) | Ministry of Environment, Forest and Climate Change (Indian Wetlands portal) |  |

## Transport & energy

| id | Source | Publisher | Notes |
|---|---|---|---|
| `morth` | [Ministry of Road Transport and Highways](https://morth.nic.in) | MoRTH |  |
| `nhai` | [National Highways Authority of India](https://nhai.gov.in) | NHAI |  |
| `railways` | [Ministry of Railways / Indian Railways](https://indianrailways.gov.in) | Ministry of Railways |  |
| `civil-aviation` | [Ministry of Civil Aviation](https://www.civilaviation.gov.in) | MoCA |  |
| `aai` | [Airports Authority of India](https://www.aai.aero) | AAI |  |
| `cea` | [Central Electricity Authority — installed capacity reports](https://cea.nic.in) | CEA, Ministry of Power |  |
| `mnre` | [Ministry of New and Renewable Energy](https://mnre.gov.in) | MNRE |  |
| `nhsrcl` | [National High Speed Rail Corporation Limited](https://www.nhsrcl.in) | Ministry of Railways |  |
| `npcil` | [Nuclear Power Corporation of India Limited](https://www.npcil.nic.in) | Department of Atomic Energy |  |
| `ncrtc` | [National Capital Region Transport Corporation](https://ncrtc.in) | NCRTC (Government of India and participating States) |  |
| `dmrc` | [Delhi Metro Rail Corporation](https://www.delhimetrorail.com) | DMRC (Government of India and GNCTD) |  |
| `thefederal` | [The Federal](https://thefederal.com) | The Federal (news, third party) | Third-party. Replace with an NPCIL or Department of Atomic Energy status page once linked. |
| `theprint` | [ThePrint](https://theprint.in) | ThePrint (news, third party) | Third-party. |

## Tourism & heritage

| id | Source | Publisher | Notes |
|---|---|---|---|
| `tourism` | [India Tourism Statistics](https://tourism.gov.in) | Ministry of Tourism |  |
| `asi` | [Archaeological Survey of India](https://asi.nic.in) | ASI, Ministry of Culture |  |
| `unesco-whc` | [UNESCO World Heritage Centre — India](https://whc.unesco.org/en/statesparties/in) | UNESCO |  |
| `mh-tourism` | [Department of Tourism, Government of Maharashtra](https://maharashtratourism.gov.in) | Government of Maharashtra |  |

## GI

| id | Source | Publisher | Notes |
|---|---|---|---|
| `gi-registry` | [Geographical Indications Registry](https://ipindia.gov.in) | Office of the CGPDTM, DPIIT | Use the GI public search for application numbers and registration dates. |

## Governance

| id | Source | Publisher | Notes |
|---|---|---|---|
| `eci` | [Election Commission of India](https://www.eci.gov.in) | ECI |  |
| `sansad` | [Lok Sabha and Rajya Sabha (Digital Sansad)](https://sansad.in) | Parliament of India |  |
| `india-gov` | [National Portal of India](https://www.india.gov.in) | NIC, MeitY |  |
| `igod` | [Integrated Government Online Directory](https://igod.gov.in) | NIC, MeitY | Default 'Verify on official site' link until each State/UT portal is verified. |
| `pib` | [Press Information Bureau](https://pib.gov.in) | Ministry of Information and Broadcasting | Project inaugurations and official announcements. |
| `president-of-india` | [President of India — official website](https://presidentofindia.gov.in) | President's Secretariat |  |
| `vice-president-of-india` | [Vice-President of India — official website](https://vicepresidentofindia.nic.in) | Vice-President's Secretariat |  |
| `hr-lokbhavan` | [Lok Bhavan (Raj Bhavan), Haryana](https://lokbhavan.haryana.gov.in) | Office of the Governor of Haryana |  |
| `goa-dip` | [Department of Information and Publicity, Goa](https://dip.goa.gov.in) | Government of Goa |  |
| `sk-gov` | [Government of Sikkim — notifications](https://sikkim.gov.in) | Government of Sikkim |  |
| `ar-governor` | [Office of the Governor of Arunachal Pradesh — press releases](https://arunachalgovernor.gov.in) | Lok Bhavan (Raj Bhavan), Itanagar |  |
| `ml-governor` | [Office of the Governor of Meghalaya — press releases](https://meggovernor.gov.in) | Lok Bhavan (Raj Bhavan), Shillong |  |
| `mn-assembly` | [Manipur Legislative Assembly — bulletins](https://assembly.mn.gov.in) | Manipur Legislative Assembly Secretariat |  |
| `ml-gov` | [Government of Meghalaya — notifications and press releases](https://meghalaya.gov.in) | Government of Meghalaya |  |
| `mz-assembly` | [Mizoram Legislative Assembly — bulletins](https://mizoramassembly.in) | Mizoram Legislative Assembly Secretariat |  |
| `py-assembly` | [Puducherry Legislative Assembly (NeVA portal)](https://puddu.neva.gov.in) | Puducherry Legislative Assembly Secretariat |  |
| `ld-gov` | [Union Territory of Lakshadweep — official portal](https://lakshadweep.gov.in) | Lakshadweep Administration |  |
| `gj-assembly` | [Gujarat Legislative Assembly — notifications (NeVA)](https://cms.neva.gov.in) | Gujarat Legislature Secretariat |  |
| `goa-gov` | [Government of Goa — official portal and press notes](https://www.goa.gov.in) | Government of Goa |  |
| `hr-assembly` | [Haryana Vidhan Sabha — official website](https://haryanaassembly.gov.in) | Haryana Vidhan Sabha Secretariat |  |
| `nl-ipr` | [Directorate of Information & Public Relations, Nagaland — press releases](https://ipr.nagaland.gov.in) | Government of Nagaland |  |
| `or-assembly` | [Odisha Legislative Assembly — official website](https://odishaassembly.nic.in) | Odisha Legislative Assembly Secretariat |  |
| `pb-ipr` | [Department of Information & Public Relations, Punjab — press releases](https://ipr.punjab.gov.in) | Government of Punjab |  |
| `tg-gov` | [Telangana State Portal](https://www.telangana.gov.in) | Government of Telangana |  |
| `tr-lokbhavan` | [Raj Bhavan, Tripura — official website](https://rajbhavan.tripura.gov.in) | Office of the Governor of Tripura |  |
| `uk-lokbhavan` | [Lok Bhavan, Uttarakhand — press notes](https://governoruk.gov.in) | Office of the Governor of Uttarakhand |  |
| `mha-zonal-councils` | [Zonal Councils](https://www.mha.gov.in) | Ministry of Home Affairs | Basis of the region filter (Northern, Central, Eastern, Western, Southern, North-Eastern). A&N and Lakshadweep are grouped as 'Island UTs' editorially. |
| `pmindia` | [Prime Minister's Office — news updates](https://www.pmindia.gov.in) | Prime Minister's Office |  |
| `isro` | [Indian Space Research Organisation — news and updates](https://www.isro.gov.in) | Department of Space, Government of India |  |
| `new-india-samachar` | [New India Samachar (fortnightly)](https://newindiasamachar.pib.gov.in) | Press Information Bureau, Government of India |  |
| `jk-planning` | [Planning, Development & Monitoring Department, Jammu and Kashmir](https://jkplanning.gov.in) | Government of Jammu and Kashmir |  |
| `mh-gov` | [Government of Maharashtra departmental portals](https://www.maharashtra.gov.in) | Government of Maharashtra | Cite the specific department page in each data point's url. |
| `kl-gov` | [Government of Kerala portal](https://kerala.gov.in) | Government of Kerala |  |
| `dl-gov` | [Government of NCT of Delhi portal](https://delhi.gov.in) | Government of NCT of Delhi |  |
| `la-gov` | [Union Territory of Ladakh portal](https://ladakh.gov.in) | Administration of Union Territory of Ladakh |  |
| `tn-gov` | [Government of Tamil Nadu portal](https://www.tn.gov.in) | Government of Tamil Nadu |  |
| `mh-lokbhavan` | [Lok Bhavan (formerly Raj Bhavan), Maharashtra](https://lokbhavan.maharashtra.gov.in) | Office of the Governor of Maharashtra |  |
| `dl-lg` | [Office of the Lieutenant Governor, Delhi](https://lg.delhi.gov.in) | Lok Niwas, Delhi |  |
| `tn-lokbhavan` | [Lok Bhavan (formerly Raj Bhavan), Tamil Nadu](https://lokbhavan.tn.gov.in) | Office of the Governor of Tamil Nadu |  |
| `bihar-lokbhavan` | [Lok Bhavan (formerly Raj Bhavan), Bihar](https://governor.bih.nic.in) | Office of the Governor of Bihar |  |
| `newsonair` | [News On AIR](https://www.newsonair.gov.in) | Prasar Bharati (public broadcaster) | Used to confirm dated public events (oaths, inaugurations) when no ministry release is available. |
| `prs` | [PRS Bill Track](https://prsindia.org) | PRS Legislative Research (independent, non-profit) | Independent tracker of Parliament's legislative record; used for bill dates. |
| `ka-gis` | [Karnataka at a Glance — Karnataka-GIS, Karnataka State Remote Sensing Applications Centre](https://kgis.ksrsac.in/kag/) | Government of Karnataka |  |
| `bar-and-bench` | [Bar & Bench](https://www.barandbench.com) | Bar & Bench (legal news, third party) | Third-party. Replace with the High Court's own notification when linked. |
| `onmanorama` | [Onmanorama (Malayala Manorama)](https://www.onmanorama.com) | Malayala Manorama (news, third party) | Third-party. Replace with the Gazette of India notification once linked. |
| `keralakaumudi` | [Kerala Kaumudi](https://keralakaumudi.com) | Kerala Kaumudi (news, third party) | Third-party. |
| `uni` | [United News of India](https://www.uniindia.com) | United News of India (news agency, third party) | Third-party. |
| `pioneer` | [The Pioneer](https://www.dailypioneer.com) | The Pioneer (news, third party) | Third-party. |
| `tribune` | [The Tribune](https://www.tribuneindia.com) | The Tribune (news, third party) | Third-party. |
| `ani` | [Asian News International (ANI)](https://www.aninews.in) | ANI (news agency, third party) | Third-party. Replace with the Lok Bhavan / Raj Bhavan page once available. |
| `scroll` | [Scroll.in](https://scroll.in) | Scroll (news, third party) | Third-party. |
| `thesouthfirst` | [The South First](https://thesouthfirst.com) | The South First (news, third party) | Third-party. |
| `fpj` | [Free Press Journal](https://www.freepressjournal.in) | Free Press Journal (news, third party) | Third-party. |
| `ians` | [Indo-Asian News Service (IANS)](https://ianslive.in) | IANS (news agency, third party) | Third-party. Replace with the Lok Bhavan page once available. |
| `etv-bharat` | [ETV Bharat](https://www.etvbharat.com) | ETV Bharat (news, third party) | Third-party. |
| `deccan-herald` | [Deccan Herald](https://www.deccanherald.com) | Deccan Herald (news, third party) | Third-party (PTI copy). Replace with the official page in review. |
| `thestatesman` | [The Statesman](https://www.thestatesman.com) | The Statesman (news, third party) | Third-party. |
| `hitavada` | [The Hitavada](https://www.thehitavada.com) | The Hitavada (news, third party) | Third-party. |
| `odishabytes` | [OdishaBytes](https://odishabytes.com) | OdishaBytes (news, third party) | Third-party. |
| `deccan-chronicle` | [Deccan Chronicle](https://www.deccanchronicle.com) | Deccan Chronicle (news, third party) | Third-party. |
| `the-week` | [The Week (PTI wire)](https://www.theweek.in) | The Week (news, third party) | Third-party (PTI copy). |
| `kashmir-life` | [Kashmir Life](https://kashmirlife.net) | Kashmir Life (news, third party) | Third-party. |
| `kashmir-reader` | [Kashmir Reader](https://kashmirreader.com) | Kashmir Reader (news, third party) | Third-party. |
| `the-goan` | [The Goan](https://www.thegoan.net) | The Goan (news, third party) | Third-party. |
| `eastmojo` | [EastMojo](https://eastmojo.com) | EastMojo (news, third party) | Third-party. |
| `eastern-mirror` | [Eastern Mirror](https://www.easternmirrornagaland.com) | Eastern Mirror, Nagaland (news, third party) | Third-party. |
| `morung-express` | [The Morung Express](https://morungexpress.com) | The Morung Express, Nagaland (news, third party) | Third-party (often IANS/PTI copy). |
| `swarajya` | [Swarajya](https://swarajyamag.com) | Swarajya (news, third party) | Third-party. |
| `sentinel-assam` | [The Sentinel (Assam)](https://www.sentinelassam.com) | The Sentinel, Guwahati (news, third party) | Third-party. |
| `udayavani` | [Udayavani (English)](https://english.udayavani.com) | Udayavani (news, third party) | Third-party (PTI copy). |
| `organiser` | [Organiser](https://organiser.org) | Organiser (news weekly, third party) | Third-party. |
| `drishti` | [Drishti IAS current affairs](https://www.drishtiias.com) | Drishti IAS (third party) | Third-party summary; replace with the Vidhan Sabha notice in review. |

## Tribal & social

| id | Source | Publisher | Notes |
|---|---|---|---|
| `tribal-affairs` | [Ministry of Tribal Affairs](https://tribal.nic.in) | MoTA | Notified STs and PVTGs. |
| `ncsc` | [National Commission for Scheduled Castes](https://ncsc.nic.in) | NCSC |  |
| `ncst` | [National Commission for Scheduled Tribes](https://ncst.nic.in) | NCST |  |

## Climate & hazards

| id | Source | Publisher | Notes |
|---|---|---|---|
| `imd` | [India Meteorological Department](https://mausam.imd.gov.in) | IMD, Ministry of Earth Sciences |  |
| `ndma` | [National Disaster Management Authority](https://ndma.gov.in) | NDMA |  |
| `bis` | [Bureau of Indian Standards — seismic zonation (IS 1893)](https://www.bis.gov.in) | BIS |  |
| `open-meteo` | [Open-Meteo weather API](https://open-meteo.com) | Open-Meteo (third party) | Live weather widget only; labelled 'Live', never used for climate normals. |

## Maps

| id | Source | Publisher | Notes |
|---|---|---|---|
| `survey-of-india` | [Survey of India — official political map](https://surveyofindia.gov.in) | Survey of India, DST | Only boundary source permitted (Principle 8). |

## Standards

| id | Source | Publisher | Notes |
|---|---|---|---|
| `iso-3166` | [ISO 3166-2:IN subdivision codes](https://www.iso.org/obp/ui/#iso:code:3166:IN) | International Organization for Standardization |  |
