# SEO, accessibility & localisation plan

## SEO

| Item | Phase 1 | Next |
|---|---|---|
| Locale-prefixed URLs, canonical, `hreflang` (incl. `x-default`) | Done (`src/lib/seo.ts`, next-intl `Link` headers) | — |
| Unique localised titles and descriptions | Done for all routes | Richer per-module descriptions with data (Phase 2) |
| `sitemap.xml` with language alternates, `robots.txt` | Done | Add district pages (Phase 3) |
| Schema.org | `WebSite` (home), `Place`/`AdministrativeArea` (profiles) | `TouristAttraction`, `GovernmentOrganization`, `EducationalOrganization`, `Dataset`, `Article`, breadcrumbs JSON-LD (Phase 2–4) |
| OG images per state | — | Generated `opengraph-image.tsx` per region (Phase 2) |
| Static generation | All pages SSG; home revalidates daily | — |
| Set `NEXT_PUBLIC_SITE_URL` in production | Required at deploy | — |

## Accessibility (WCAG 2.1 AA)

Done in Phase 1: correct `lang` on `<html>` and on any inline text in another language or script; skip link; visible focus rings; keyboard-operable search combobox, source disclosures, filters and map tiles; table alternative for the map; colour never the only carrier (labels, icons, dashed UT outline); AA contrast measured for every token in both themes (see DESIGN-SYSTEM.md); `prefers-reduced-motion` respected; no-flash dark mode.

To do: automated axe checks in CI; Lighthouse ≥ 90 mobile in CI; manual NVDA/TalkBack passes in all three languages; captions/alt text policy enforced in the MediaAsset schema (Phase 2); chart text alternatives (Phase 2/4).

## Localisation

Done: URL-based locales with persistent cookie; fallback chain mr → hi → en (`src/i18n/routing.ts`), shown with the right `lang`; message-key parity unit-tested; Indian number system, Devanagari-numeral toggle, localised dates in IST; search across scripts and spellings; Noto Sans Devanagari with line-height 1.7.

To add a 4th (regional) language: add the code to `locales`, `intlTag` and `FALLBACKS`; add `messages/<code>.json`; extend `Localized` with an optional key; the validator's missing-translation check then covers it.

To do: native-speaker review of every Phase 1 `hi`/`mr` string (all are `draft`); per-field translation status dashboard (Phase 4 CMS).

## Tests

Unit tests (Vitest, 38 passing): number/date/period formatters, change-badge polarity, transliteration keys, every validator rule with negative cases, search results across scripts, message parity. End-to-end tests (Playwright: locale switching, search, compare) are planned for Phase 4 alongside Compare; Phase 1 was smoke-tested by script in a headless browser.
