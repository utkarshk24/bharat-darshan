# Design system

## Tokens (`src/app/globals.css`)

Restrained tricolour palette. Saffron and green are **decorative only**; text uses the darker "ink" variants.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` / `--surface` / `--surface-2` | #fbfaf7 / #fff / #f3f1eb | #0d1420 / #141d2b / #1b2638 | page, cards, insets |
| `--text` / `--text-muted` | #16202e / #4a5568 | #e8edf4 / #a8b3c4 | body, secondary |
| `--navy` | #0b2545 | #c9d7ee | selected pills, brand |
| `--saffron-ink` / `--green-ink` | #9a4a00 / #0b6b2e | #ffb36b / #6fd18b | icons, accents in text |
| `--good` / `--bad` | #0b6b2e / #b42318 | #6fd18b / #ff8a80 | trend badges |
| `--badge-*` | official, estimate, third-party, editorial | | confidence badges |

### Measured contrast (WCAG 2.1, AA needs 4.5:1)

Light: text 16.4 · muted on bg 7.2 · muted on surface-2 6.7 · link 6.7 · saffron-ink 6.3 · green-ink 6.7 · bad 6.6 · estimate badge 5.9 · editorial badge 6.5 · selected pill 14.7.
Dark: text 14.4 · muted 8.7 · muted on surface-2 7.2 · link 8.1 · saffron-ink 9.6 · good 9.0 · bad 7.4 · estimate 10.3 · editorial 8.9 · selected pill 12.7.

Map tiles use the Okabe–Ito colour-blind-safe palette; the label colour on each tile is chosen automatically (black or white, whichever has higher contrast — `inkFor()`), and every colour is paired with a text label.

### Region accents and motifs

Each region has an editorial `accent` colour and a `motif` (kolam, warli, madhubani, pattachitra, ikat, jaali). Motifs are simple geometric line patterns drawn from scratch, *inspired by* the named traditions — not reproductions of artwork. They are decorative (`aria-hidden`) and used at low opacity on card headers, profile headers and section dividers.

## Typography

- Latin: **Inter** (variable). Devanagari: **Noto Sans Devanagari** (variable), first in the stack for `hi`/`mr`, line-height 1.7.
- Local-script names load Noto Sans Bengali, Telugu, Tamil, Kannada, Malayalam, Gujarati, Gurmukhi and Oriya. Fontsource's `unicode-range` means each font downloads only when that script appears.
- All fonts are self-hosted (no runtime Google Fonts call).

## Components (`src/components`)

| Component | Purpose |
|---|---|
| `StatCard` | One indicator: value or "Not available", national comparison, source line |
| `SourceInfo` | "Source · Period" line + tap/click disclosure with confidence, revision, dates, note, verify link. Esc / outside-click closes |
| `ConfidenceBadge` | Icon + label per confidence level (never colour alone) |
| `TrendBadge` | Arrow shows direction; colour shows improvement per indicator polarity |
| `DataAsOn` | "Data as on" badge |
| `Disclaimer` | Mandatory data-page disclaimer |
| `OfficeholderCard` | Role, name or "Awaiting verified source", asOf, verify link; no party colours |
| `RegionCard`, `RegionGrid` | Home/list cards with type and region filters |
| `IndiaMap`, `GeoMap` | Tile grid / official boundary map, layers, filters, table view, quick-facts panel |
| `GlobalSearch` | WAI-ARIA combobox, trilingual fuzzy search |
| `ModuleNav` | A–Z module side-nav (desktop) / scrolling tabs (mobile) |
| `Motif`, `MotifDivider` | Decorative patterns |
| `LocalizedText` | Renders a `{en,hi,mr}` field with fallback and correct `lang` |
| `LocaleSwitcher`, `DisplayToggles` | Language; Devanagari numerals (१२३); dark mode |

Timeline, gallery, project card, GI card, comparison table and chart wrappers arrive with the modules that need them (Phase 2/4).
