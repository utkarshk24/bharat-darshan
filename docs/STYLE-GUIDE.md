# Content style guide & fact-check checklist

## Voice

- Clear, neutral, respectful **Indian English** (organisation, programme, lakh, crore).
- Hindi and Marathi are written natively, not translated word-for-word. Prefer the term people actually use (मुख्यमंत्री, जीएसडीपी) over coined Sanskritised equivalents.
- Summarise in your own words. Never copy passages from government sites, Wikipedia or news. Never reproduce song lyrics — state songs are given by title only.
- Present both benefits and challenges of projects and policies. No praise, criticism or ranking of parties or leaders.
- Caste, tribe, religion, border areas, insurgency and communal history: neutral, evidence-based language, official sources only. No "dominant castes", no ranking of communities.

## Names

- Use current official names and boundaries; note former names (`formerNames`, `formerName`). Examples in the seed: Sri Vijaya Puram (formerly Port Blair), Bengaluru (formerly Bangalore), Odisha (formerly Orissa), Puducherry (formerly Pondicherry), Uttarakhand (formerly Uttaranchal).
- Spell each proper noun as used in that language — they differ: नागपुर (hi) / नागपूर (mr); केरल / केरळ; तेलंगाना / तेलंगणा; छत्तीसगढ़ / छत्तीसगड; पटना / पाटणा.
- Local-script names (`localName`) are added only where the region's principal script differs from Devanagari and the spelling is certain.

## Numbers

- Indian grouping (11,23,74,333) and lakh/crore scale words in all three languages. Money is stored in ₹ crore and displayed as ₹ … crore / lakh crore.
- Content stores Latin digits; the UI converts to Devanagari numerals when the reader chooses १२३.
- Always label the period: `FY2023-24` for financial years, `2024` for calendar years, `2011` for census, `2019-21` for survey rounds. Never mix them in one series.
- Money always carries a price base (current / constant + base year).
- Census-only indicators (literacy, sex ratio, child sex ratio, urbanisation, decadal growth) are never shown as annual series.

## Translation workflow

Each `{en, hi, mr}` field may carry `_status: { hi, mr }` = `draft → reviewed → approved`. Everything authored in Phase 1 is `draft`. The glossary page marks draft definitions. A native-speaker reviewer moves fields to `reviewed`; an editor approves.

## Fact-check checklist (run before publishing any record)

1. Does every figure have a source, period, unit and confidence tag?
2. Are financial years, calendar years and price bases labelled and consistent?
3. Are officeholders and project statuses timestamped and checked against an official site?
4. Is all caste and religion data from official published sources only?
5. Is the map compliant with Principle 8 (Survey of India boundaries only)?
6. Are the Hindi and Marathi versions reviewed, not merely machine-translated?
7. Are images licensed (CC or public domain) and attributed?
8. Is the text original, with no copied passages or lyrics?
9. Does `npm run validate-data` report 0 errors, and has `meta.lastUpdated` been bumped?
