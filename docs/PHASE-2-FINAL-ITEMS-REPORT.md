# Phase 2 final items: GI directory, projects dashboard, themes and preview images

Date: 13 October 2026. Status: **built and checked; still a draft awaiting your review before Phase 3.**

The last three placeholder pages ("Coming soon") are now real pages, and every page has a social-preview image. Nothing in this round adds new figures: these pages reuse data already in the profiles, with the same sources.

## GI Products (`/gi`)

**The directory:**
- It holds 101 Geographical Indications (GIs) from the four completed profiles: Maharashtra 55, Keralam 41, Ladakh 4, Delhi 1.
- A note says plainly that only 4 of 36 States and UTs are covered so far, and links to the GI Registry's own State-wise list as the complete record.
- **Search** works in any script. "Paithani", "पैठणी" and a romanised spelling all find the same product.
- **Filters:**
  - by category, with counts: agricultural 64, handicraft 32, textile 11, foodstuff 4, manufactured 1;
  - by State/UT.
- **Sort** is A–Z, or by newest filing date.
- GIs shared between States show the partner State, for example Alleppey Green Cardamom with Tamil Nadu.

**One page per GI** (`/gi/<id>`, 303 pages across 3 languages) shows:
- the name in all three languages;
- category;
- the State/UT it is listed under, with a link;
- application number;
- filing date;
- a provenance line: confidence badge, source and a "verify" link.

It also has a **"Still to be added"** box. Registration year, producing districts, what makes the product distinctive, artisan or farmer communities, and market all show *Not available*. These come from each GI's registration certificate and GI Journal entry, which haven't been read yet. **Nothing was filled in from general knowledge.** The note under each date makes clear it is the *filing* date from the Registry list, not the registration date.

## Projects & Vision (`/projects`)

**The dashboard:**
- **Status tiles:** 10 projects recorded, 6 Completed, 4 Under construction, 0 Tendering, 0 Announced, 0 Stalled or delayed. Clicking a tile filters the list.
- **Filters:** State/UT and sector (Transport; Ports & waterways).
- **Each card shows:**
  - objective;
  - implementing agency;
  - cost, in ₹ crore;
  - start and completion;
  - challenges, where a source records them;
  - confidence badge;
  - source link;
  - the date it was checked.

**Neutrality:**
- A status says "Completed" only when an official source says so. This was already enforced by the validator.
- Status colours are fixed per status and never tied to a party.
- A note on the page says it does not rate projects.

**Two parts are marked "pending":**
- the projects map, which needs the official Survey of India boundary file;
- State vision documents, which come with the Phase 3 profiles.

## Themes (`/themes`, `/themes/<theme>`)

There are nine themes:
- Geography;
- People;
- Economy;
- Governance;
- Infrastructure;
- Tourism & GI;
- Culture & heritage;
- Nature & environment;
- Education & health.

Each theme page has:
- **Indicator tables** where the comparison data has a matching group, for People, Economy, Nature and Education & health. These show the six comparison regions plus India, with period and source on every row, and a link to the full comparison. The values are the same validated ones the comparison page uses.
- **"Explore by State/UT"**: links into the matching modules of the four completed profiles.
- **"Other States and UTs"**: links to the 32 seed profiles, with a count still pending.

## Social-preview (Open Graph) images

There are 114 images: for each of 3 languages, the home page, India and all 36 States and UTs. They are wired into every page's metadata, including Open Graph and Twitter's `summary_large_image`.

**What each image shows:**
- name in the page's language, with the other two below;
- capital(s);
- ISO code;
- "Data as on" date;
- the region's accent colour.

**Why they are pre-rendered:**
- Next.js's built-in image generator (Satori) **cannot shape Devanagari**. In a test it rendered राज्य with a visible halant and put the i-matra of तिरुवनंतपुरम on the wrong letter.
- So the images are rendered by headless Chrome, which shapes Hindi and Marathi correctly, and saved as static PNGs in `public/og/<locale>/` (2.9 MB in total).
- Re-run `npm run og` whenever a name, capital or the dataset date changes. The README's data-update workflow now says so.

## Also changed

- The compare page now accepts **`/compare?ids=MH,KL,TN`**, the URL pattern in the brief. Older `?r=IN-MH,…` links still work.
- The shared value formatter moved to `lib/format.ts`, so server-rendered tables (Themes) can use it.

## Checks run

| Check | Result |
|---|---|
| `npm run validate-data` | 0 errors, 0 warnings, 644 gaps (unchanged: no new data) |
| `npm test` | 58/58 pass |
| `tsc --noEmit` | clean |
| `npm run build` | 3,191 pages generated |
| Screenshots | `/gi`, `/gi/<id>`, `/projects`, `/themes`, `/themes/economy` and `/compare?ids=…` checked in en/hi/mr, desktop and 390 px mobile. No horizontal page overflow; wide tables scroll inside their own box. |

## Not done here: these need you or an unrestricted network

1. **Native-speaker review** of the Hindi and Marathi text, including the new page strings.
2. **Editorial review** of the theme blurbs and page intros.
3. **The official Survey of India boundary file**, for the projects map and the main map.
4. **Third-party citations.** Five citations still rely on secondary sources and need official replacements (listed in the earlier reports).
5. **Release checks:**
   - Lighthouse (≥ 90 on mobile);
   - an axe accessibility scan;
   - `npm run validate-data:links`.

   These need outbound network access, which this build environment doesn't have.

Once you confirm, Phase 3 begins: the remaining 32 profiles in batches of five. Each batch adds its GIs and projects to these pages automatically.
