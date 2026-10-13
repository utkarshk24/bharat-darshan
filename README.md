# Bharat Darshan — भारत दर्शन

Tri-lingual (English · हिन्दी · मराठी) encyclopedia, atlas and data dashboard of India's 28 States and 8 Union Territories.

**Status: Phase 2 complete (draft, awaiting review).** Phase 1 (foundation) is complete. Four reference profiles are populated across all 26 modules in three languages (draft translations): **Maharashtra** ([report](docs/PHASE-2-MAHARASHTRA-REPORT.md)), **Keralam** (formerly Kerala; `/states/keralam`, old address redirects), **Delhi** (UT with legislature) and **Ladakh** (UT without legislature) — see [docs/PHASE-2-REFERENCE-PROFILES-REPORT.md](docs/PHASE-2-REFERENCE-PROFILES-REPORT.md). The **India overview** (`/india`) and the **comparison prototype** (`/compare`, MH · TN · UP · KL by default, plus Delhi and Ladakh) complete Phase 2 — see [docs/PHASE-2-COMPLETION-REPORT.md](docs/PHASE-2-COMPLETION-REPORT.md). The national **GI Products** directory (`/gi`, one page per GI), **Projects & Vision** dashboard (`/projects`), **Themes** (`/themes`) and per-page social-preview images followed — see [docs/PHASE-2-FINAL-ITEMS-REPORT.md](docs/PHASE-2-FINAL-ITEMS-REPORT.md). The other 32 regions show identity data and "Not available" until Phase 3.

## Quick start

```bash
npm install
npm run dev              # http://localhost:3000 → redirects to /en
npm run validate-data    # schema + content checks, writes docs/DATA-GAP-REPORT.md
npm test                 # unit tests (formatters, transliteration, validator, search, message parity)
npm run build            # static generation of ~3,200 pages (3 locales × 36 regions × 26 modules + site pages)
npm run build:pages      # static export for GitHub Pages into out/ (see "Publishing" below)
npm run og               # re-render social-preview images into public/og (needs a local Chrome/Chromium; set CHROME=… if not found)
```

Requires Node 20+.

## Stack

Next.js 16 (App Router, TypeScript) · Tailwind CSS 4 · next-intl 4 · Zod 4 · Fuse.js · d3-geo + topojson-client · lucide-react · self-hosted Inter and Noto Sans (Devanagari + 8 regional scripts) via Fontsource · Vitest.

shadcn/ui is not installed: its CLI pulls from a remote registry that the build environment couldn't reach. Components in `src/components` follow the same pattern (Tailwind + `cn()`), so shadcn components can be added later with `npx shadcn add …` without conflicts.

## Project layout

```
data/                       ← the dataset (source of truth)
  india.json                  national reference row
  regions/IN-XX.json          one file per State/UT, named by ISO 3166-2 code
  modules/IN-XX/<module>.json profile module content (typed blocks)
  sources.json                authoritative sources (Section 15)
  glossary.json               trilingual glossary
messages/{en,hi,mr}.json    ← UI strings (key parity is unit-tested)
public/maps/manifest.json   ← official boundary file slot (see docs/MAPS.md)
scripts/validate-data.ts    ← npm run validate-data
scripts/og/generate-og.ts   ← npm run og (social-preview PNGs → public/og/<locale>/<key>.png)
scripts/authoring/          ← Python scripts + research extracts used to author region content
src/
  app/[locale]/…              routes (see docs/INFORMATION-ARCHITECTURE.md)
  components/                 design-system components
  components/map/             IndiaMap (tile grid / official boundaries), GeoMap
  i18n/                       locales, fallback chain, routing
  lib/schema.ts               Zod schema for every entity (Section 14)
  lib/validate.ts             validation rules (Section 14.4)
  lib/format.ts               lakh/crore, Devanagari numerals, FY labels, change tone
  lib/translit.ts             cross-script search keys
  lib/search.ts               trilingual fuzzy index
  proxy.ts                    locale detection + NEXT_LOCALE cookie (Next 16 "proxy" = middleware)
docs/                       ← IA, design system, style guide, quality plan, maps, roadmap, gap report
```

## Authoring a profile module

Each module is `data/modules/IN-XX/<module>.json` with `{ region, module, asOf, status, blocks[] }`. Block types: `prose`, `facts`, `list`, `timeline`, `series`, `table`, `links`, `weather`, `projects`, `gi`, `officeholders`, `gaps`. Numbers live only in `facts`, `series` and `table` blocks (with full provenance); prose that states facts must list `sourceIds` unless tagged `Editorial`. Anything the module should show but can't yet goes in a `gaps` block so it appears on the page and in the gap report.

## Publishing (GitHub Pages)

Live at **https://utkarshk24.github.io/bharat-darshan/**. Every push to `main` runs `.github/workflows/pages.yml`: validate data → tests → `npm run build:pages` → deploy `out/`.

One-time setup: repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.

`build:pages` sets `basePath` to `/<repo name>`, exports static HTML (`output: "export"`, trailing slashes), and replaces the three server features Pages can't run:

- **Locale detection:** the proxy is replaced by `out/index.html`, which picks en/hi/mr from the browser.
- **Kerala → Keralam redirect:** replaced by redirect pages at the old addresses.
- **Localized catch-all 404:** replaced by the site-wide `404.html`.

Canonical, hreflang and Open Graph URLs are absolute, built from `NEXT_PUBLIC_SITE_URL`, so the sub-path is kept. A normal `npm run build` / `npm start` (or Vercel) is unaffected.

## Data-update workflow

1. Edit the region file (`data/regions/IN-XX.json`). For every value fill `value, unit, period, periodType, sourceId, url, accessDate, dataLevel, revisionStatus, confidence` — and `priceBase` for money.
2. Unknown? Leave `value: null`, `revisionStatus: "TODO"` and a `note` saying where to find it. **Never estimate.**
3. Officeholders: set `name`, `since`, `asOf` (date you checked), `sourceId`, `url`, `verifyUrl`.
4. Bump `meta.lastUpdated` (drives the "Data as on" badge).
5. `npm run validate-data` — must show 0 errors. Commit the regenerated `docs/DATA-GAP-REPORT.md`.
6. If a region name, capital or `meta.lastUpdated` changed, run `npm run og` and commit `public/og`.
7. Before release, run `npm run validate-data:links` from an unrestricted network.

The validator rejects: schema violations, unknown sources, values without a source, nulls not marked TODO, period strings that don't match their type, mixed period types or price bases within a series, annual series for census-only indicators, a Governor on a UT or a CM on a UT without legislature, duplicate codes/slugs/tiles, wrong coverage counts, and an unverified boundary file. It warns on missing translations, unverified values (`accessDate: null`) and any `asOf` ≥ 6 months old.

## Documents

- [docs/PHASE-2-MAHARASHTRA-REPORT.md](docs/PHASE-2-MAHARASHTRA-REPORT.md) — Maharashtra profile: sources, gaps, review points
- [docs/PHASE-1-REPORT.md](docs/PHASE-1-REPORT.md) — foundation: what was built, decisions needed
- [docs/INFORMATION-ARCHITECTURE.md](docs/INFORMATION-ARCHITECTURE.md) — navigation and URL map
- [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md) — tokens, contrast, components
- [docs/STYLE-GUIDE.md](docs/STYLE-GUIDE.md) — content style guide and fact-check checklist
- [docs/QUALITY-PLAN.md](docs/QUALITY-PLAN.md) — SEO, accessibility and localisation plan
- [docs/MAPS.md](docs/MAPS.md) — official map policy and how to install the boundary file
- [docs/ROADMAP.md](docs/ROADMAP.md) — MVP → Phase 2 → Phase 3 → Phase 4
- [docs/DATA-GAP-REPORT.md](docs/DATA-GAP-REPORT.md) — generated by the validator
- [SOURCES.md](SOURCES.md) — generated from `data/sources.json`
- Trilingual glossary — `data/glossary.json`, rendered at `/{locale}/glossary`
