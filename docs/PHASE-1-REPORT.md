# Phase 1 report — Foundation

Date: 13 October 2026 · Status: **complete, awaiting confirmation to start Phase 2**

## What was built

| Deliverable (§17) | Where | Notes |
|---|---|---|
| Information architecture & URL map | `docs/INFORMATION-ARCHITECTURE.md`, `src/lib/nav.ts`, `src/app/[locale]/…` | All 15 nav destinations routed in 3 locales; 26 profile modules routed for all 36 regions |
| Data schema | `src/lib/schema.ts` | Zod: Localized (with per-field translation status), DataPoint (full provenance), Officeholder, Project, GIProduct, StateSymbol, Region, Source, Glossary |
| Validator | `src/lib/validate.ts`, `npm run validate-data` | 15+ rules incl. period hygiene, census-only series, UT governance, staleness, map compliance; writes the gap report; optional link checker |
| Seed dataset | `data/` | 36 region files + India; names in en/hi/mr, local-script names (11 regions), capitals with roles and former names, ISO codes, Zonal Council, tile position. 45 sources, 20 glossary terms |
| i18n | `src/i18n`, `src/proxy.ts`, `messages/` | next-intl 4; URL locales, persistent cookie, hreflang, mr → hi → en fallback, ~200 UI strings ×3 |
| Design system & components | `src/app/globals.css`, `src/components`, `docs/DESIGN-SYSTEM.md` | Tricolour tokens, dark mode, AA contrast measured, 6 motifs, StatCard, SourceInfo, ConfidenceBadge, TrendBadge, DataAsOn, Disclaimer… |
| Layout & navigation | `Header`, `Footer`, `LocaleSwitcher`, `DisplayToggles`, `ModuleNav` | Skip link, sticky header, mobile menu, १२३ numeral toggle, theme toggle |
| India map | `src/components/map` | Tile-grid cartogram (no boundaries) with layers, region filters, quick-facts panel and table view; official boundary map wired but switched off until a verified Survey of India file is installed (`docs/MAPS.md`) |
| Home page | `src/app/[locale]/page.tsx` | Hero in 3 languages, trilingual fuzzy search, map, national facts, featured region, indicator of the day, trending insights (honestly empty), 6 featured comparisons, 36 filterable cards |
| Docs | `README.md`, `SOURCES.md`, `docs/*` | Setup & data workflow, style guide + fact-check checklist, SEO/a11y/l10n plan, roadmap |

**Verification:** `next build` passes (≈2,850 static pages). `npm run validate-data`: 0 errors. `npm test`: 38/38 pass. All routes smoke-tested in a headless browser in all three locales, light and dark, desktop and 390px mobile, with no console errors.

## Data gaps (438 TODO fields)

Nothing was estimated. Every figure except four is `null` with a note naming the source to use.

| Field | Missing | Source to use |
|---|---|---|
| Population, sex ratio, child sex ratio, literacy (2011) | 36 each (MH has values) | Census 2011 PCA |
| Area, density, urbanisation (2011) | 37 each | Census 2011 |
| GSDP, per capita NSDP (current prices) | 37 each | MoSPI, base 2011-12; confirm latest FY |
| Forest cover % | 37 | ISFR 2023 |
| Governor / Lt Governor / Administrator | 36 | Raj Bhavan / Raj Niwas / State portal; record `asOf` |
| Chief Minister | 31 (28 States + Delhi, J&K, Puducherry) | Official State/UT portal; record `asOf` |
| Official State/UT portal URL | 36 | igod.gov.in → each portal |
| Maharashtra symbols, Paithani GI details | 3 | State notification; GI Registry |
| Official boundary file | 1 | Survey of India |

**Warnings (4):** the Maharashtra Census 2011 values from the brief (population 11,23,74,333; literacy 82.34%; sex ratio 929; child sex ratio 894) are shown but flagged "never verified" until checked against the PCA and given an `accessDate`.

The full list is in `docs/DATA-GAP-REPORT.md`, regenerated on every validator run.

## Decisions and caveats for you

1. **Boundary map.** I did not bundle any India GeoJSON because I couldn't verify one matches Survey of India boundaries. The tile grid is the compliant fallback. Can you source the official vector file, or should Phase 2 keep the tile grid?
2. **Translations are drafts.** All Hindi and Marathi text is my own native-style writing, marked `draft`. It needs a native-speaker review before launch (Principle 9).
3. **Capitals to re-verify in Phase 2:** Andhra Pradesh (Amaravati) and Uttarakhand (Dehradun winter / Bhararisain-Gairsain summer) have had recent legal or official changes.
4. **Region filter** uses the MHA Zonal Councils; A&N and Lakshadweep are grouped editorially as "Island UTs". Featured comparison groupings (coastal, Himalayan, etc.) are editorial.
5. **shadcn/ui** wasn't installed because its registry wasn't reachable from the build machine. The components follow its conventions, so it can be added later.
6. **Link checking** can't run here (government sites are unreachable from the sandbox). Run `npm run validate-data:links` on an open network.
7. **E2E tests** (Playwright) are deferred to Phase 4 with Compare; Phase 1 has unit tests and scripted smoke tests.
8. **Set `NEXT_PUBLIC_SITE_URL`** at deploy time for canonical/OG URLs.

## Proposed Phase 2 plan

Fill the four reference profiles (Maharashtra, Kerala, Delhi, Ladakh) and the India overview across all 26 modules, verifying each figure by web search against the Section 15 sources and recording `accessDate`. Add charts (Recharts) and time series, then the MH/TN/UP/KL comparison prototype. I'll pause after the first profile (Maharashtra) for review before doing the other three.
