# Information architecture & URL map

All pages live under a locale prefix: `en`, `hi` or `mr`. `/` redirects to the visitor's saved locale (`NEXT_LOCALE` cookie) or browser language, defaulting to `en`. Every page emits `hreflang` alternates (`en-IN`, `hi-IN`, `mr-IN`, `x-default`) and a canonical URL.

| Route | Section | Phase 1 status |
|---|---|---|
| `/{locale}` | Home (§6) | **Built** — hero, trilingual search, map, facts, featured region, indicator of the day, insights (pending data), featured comparisons, 36 cards |
| `/{locale}/states` | Explore States | **Built** — filterable cards |
| `/{locale}/uts` | Explore UTs | **Built** — filterable cards |
| `/{locale}/states/{slug}` · `/{locale}/uts/{slug}` | Profile, module A (§7) | **Template built** — header, capitals, at-a-glance cards with national comparison, governance cards, symbols, A–Z module nav |
| `/{locale}/{states\|uts}/{slug}/{module}` | Modules B–Z | Routed for all 25 modules; placeholder until Phase 2 |
| `/{locale}/{states\|uts}/{slug}/districts/{district}` | District explorer | Phase 3 |
| `/{locale}/map?layer=…` | Interactive India Map (§9.3) | **Built** — tile grid, layers, region filters, table view; boundary map pending official file |
| `/{locale}/compare?ids=MH,KL` · `?group=coastal` | Compare (§9.1) | Phase 4 (placeholder; home links already use `?group=`) |
| `/{locale}/rankings/{indicator}` | Rankings (§9.2) | Phase 4 |
| `/{locale}/themes` | Themes | Phase 2 |
| `/{locale}/projects` | Projects & Vision | Phase 2 |
| `/{locale}/gi/{product-slug}` | GI Products | Phase 2 |
| `/{locale}/learn` | Quiz & flashcards | Phase 4 |
| `/{locale}/trip-planner` | Trip planner | Phase 4 |
| `/{locale}/data` | Data Library & API | Phase 4 |
| `/{locale}/glossary` | Glossary | **Built** |
| `/{locale}/about` | About, Sources & Methodology | **Built** — principles, confidence levels, full source list |
| `/{locale}/accessibility` | Accessibility & Contact | **Built** |
| `/api/v1/…` | Public API (§13.2) | Phase 4 |
| `/sitemap.xml`, `/robots.txt` | SEO | **Built** |

## Slugs and codes

- Region slug = English name, lower-case, hyphenated (`dadra-and-nagar-haveli-and-daman-and-diu`).
- Region file and API id = ISO 3166-2 code (`IN-MH`). Compare uses the short code (`MH`).
- Module slugs, in order: `overview geography climate vibe people history culture economy government projects transport energy digital education health nature water safety gi tourism cities sports personalities diaspora civic trivia` (`src/lib/nav.ts`).

## Primary navigation

Desktop (≥1280px) shows States, UTs, Map, Compare, Rankings and GI Products, with the rest under "More". Smaller screens show all 15 destinations in a menu. The footer always lists all 15.
