# Launch roadmap

| Phase | Scope | Exit criteria |
|---|---|---|
| **1 — Foundation** ✅ | IA & URL map, schema + validator, i18n, design system, layout & nav, map (tile grid + official-file slot), home page, profile template, glossary, about/sources, accessibility page | Build passes; validator 0 errors; tests pass; all routes render in 3 locales |
| **2 — Reference profiles** ✅ draft (Maharashtra, Keralam, Delhi, Ladakh, India overview, comparison prototype, GI directory, projects dashboard, themes, OG images) | Maharashtra, Kerala, Delhi (UT with legislature), Ladakh (UT without legislature) and India overview, all 26 modules, all 3 languages; comparison prototype for MH, TN, UP, KL; first charts (Recharts) and time series; OG images | Every figure sourced with `accessDate`; officeholders verified with `asOf`; hi/mr reviewed; validator 0 errors and no TODO in published fields |
| **MVP launch** 🟡 checks automated in CI (Lighthouse, axe, links) | Phase 1 + 2 live; remaining 32 regions show identity + "Not available" honestly | Lighthouse ≥ 90 mobile; axe clean; link check passes |
| **3 — Remaining profiles** 🟡 in progress (Tamil Nadu done; next UP, KA, GJ, WB) | 32 States/UTs in batches of 5, validator after each batch; district explorer; city profiles; official boundary map installed | Same as Phase 2, per batch |
| **4 — Advanced** | Rankings, map data layers, full Compare (2–6, radar, PDF), Learn, Trip Planner, Career Explorer, PWA/offline, PDF export, API & Data Library, CMS with roles + audit trail, correction workflow, E2E tests, SEO/a11y audit | Public API documented; correction queue live |
