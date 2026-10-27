/**
 * Bharat Darshan data schema (Section 14).
 * Every number and factual claim carries provenance (Principle 1) and a
 * confidence tag (Principle 2). Unknown values are `null` with
 * revisionStatus "TODO" and a note on where to find them — never guessed.
 */
import { z } from "zod";

/* ---------- Translatable strings ---------- */

export const TranslationStatus = z.enum(["draft", "reviewed", "approved"]);

/** Every translatable string has the shape { en, hi, mr } (Section 11). */
export const Localized = z.object({
  en: z.string(),
  hi: z.string(),
  mr: z.string(),
  /** Per-field translation workflow status for the non-English locales. */
  _status: z
    .object({ hi: TranslationStatus.optional(), mr: TranslationStatus.optional() })
    .optional(),
});
export type Localized = z.infer<typeof Localized>;

/* ---------- Provenance enums ---------- */

export const Confidence = z.enum([
  "Official",
  "Official estimate/projection",
  "Third-party verified",
  "Editorial",
]);
export type Confidence = z.infer<typeof Confidence>;

export const RevisionStatus = z.enum(["final", "provisional", "revised", "projected", "TODO"]);
export const DataLevel = z.enum(["national", "state", "district", "city"]);

/**
 * Period hygiene (Principle 4).
 *  fy       → FY2023-24
 *  calendar → 2024
 *  census   → 2011
 *  survey   → 2019-21 (e.g. NFHS-5 fieldwork window)
 */
export const PeriodType = z.enum(["fy", "calendar", "census", "survey"]);
const PERIOD_PATTERNS: Record<z.infer<typeof PeriodType>, RegExp> = {
  fy: /^FY\d{4}-\d{2}$/,
  calendar: /^\d{4}$/,
  census: /^\d{4}$/,
  survey: /^\d{4}-\d{2}$/,
};

const isoDate = z.string().regex(/^\d{4}-\d{2}-\d{2}$/, "expected YYYY-MM-DD");

export const PriceBase = z.object({
  type: z.enum(["current", "constant"]),
  /** Required for constant prices, e.g. "2011-12". */
  baseYear: z.string().optional(),
});

/* ---------- The data point ---------- */

export const DataPoint = z
  .object({
    value: z.union([z.number(), z.string(), z.null()]),
    unit: z.string().min(1),
    period: z.string().min(1),
    periodType: PeriodType,
    priceBase: PriceBase.optional(),
    /** Key into data/sources.json. */
    sourceId: z.string().nullable(),
    /** Specific table/page URL (may be more precise than the source home page). */
    url: z.string().url().nullable(),
    /** Date the value was last checked against the source. null = not yet verified. */
    accessDate: isoDate.nullable(),
    dataLevel: DataLevel,
    revisionStatus: RevisionStatus,
    confidence: Confidence,
    /** For TODO values: where to find it. For others: caveats/definition notes. */
    note: z.string().optional(),
    nextUpdate: z.string().optional(),
  })
  .superRefine((d, ctx) => {
    if (!PERIOD_PATTERNS[d.periodType].test(d.period)) {
      ctx.addIssue({
        code: "custom",
        path: ["period"],
        message: `period "${d.period}" does not match periodType "${d.periodType}"`,
      });
    }
    if (d.value === null && d.revisionStatus !== "TODO") {
      ctx.addIssue({ code: "custom", path: ["revisionStatus"], message: "null value must have revisionStatus TODO" });
    }
    if (d.value === null && !d.note) {
      ctx.addIssue({ code: "custom", path: ["note"], message: "null value must carry a note saying where to find it" });
    }
    if (d.value !== null && !d.sourceId) {
      ctx.addIssue({ code: "custom", path: ["sourceId"], message: "a published value must cite a source" });
    }
    if (d.priceBase?.type === "constant" && !d.priceBase.baseYear) {
      ctx.addIssue({ code: "custom", path: ["priceBase", "baseYear"], message: "constant prices need a base year" });
    }
    if (d.revisionStatus === "projected" && d.confidence !== "Official estimate/projection") {
      ctx.addIssue({ code: "custom", path: ["confidence"], message: "projected values must be tagged 'Official estimate/projection'" });
    }
  });
export type DataPoint = z.infer<typeof DataPoint>;

/* ---------- Officeholders (time-sensitive, Principle 3) ---------- */

export const OfficeRole = z.enum([
  "governor",
  "lieutenant-governor",
  "administrator",
  "chief-minister",
  "deputy-chief-minister",
  "speaker",
  "leader-of-opposition",
  "president",
  "vice-president",
  "prime-minister",
  "lok-sabha-speaker",
]);

export const Officeholder = z
  .object({
    role: OfficeRole,
    name: Localized.nullable(),
    party: z.string().nullable().optional(),
    since: isoDate.nullable(),
    asOf: isoDate.nullable(),
    sourceId: z.string().nullable(),
    url: z.string().url().nullable(),
    /** "Verify on official site" link shown in the UI. */
    verifyUrl: z.string().url().nullable(),
    revisionStatus: RevisionStatus,
    confidence: Confidence,
    note: z.string().optional(),
  })
  .superRefine((o, ctx) => {
    if (o.name && (!o.asOf || !o.sourceId)) {
      ctx.addIssue({ code: "custom", message: "a named officeholder needs asOf and a source" });
    }
    if (!o.name && o.revisionStatus !== "TODO") {
      ctx.addIssue({ code: "custom", message: "unnamed officeholder must be TODO" });
    }
  });
export type Officeholder = z.infer<typeof Officeholder>;

/* ---------- Projects ---------- */

export const ProjectStatus = z.enum([
  "Completed",
  "Under Construction",
  "Tendering",
  "Announced",
  "Stalled or Delayed",
]);

export const Project = z
  .object({
    id: z.string(),
    name: Localized,
    objective: Localized.optional(),
    sector: z.string(),
    location: Localized.optional(),
    agency: z.string().nullable(),
    cost: DataPoint.optional(),
    start: z.string().nullable(),
    completion: z.string().nullable(),
    status: ProjectStatus,
    challenges: Localized.optional(),
    asOf: isoDate,
    sourceId: z.string(),
    url: z.string().url(),
    confidence: Confidence,
    /**
     * Other sources for details the main source does not cover (e.g. a news report for tunnel lengths when the
     * official page gives only cost and date). Each says which details it covers, so provenance stays exact.
     */
    supporting: z
      .array(z.object({ sourceId: z.string(), url: z.string().url(), covers: Localized }))
      .optional(),
  });

export type Project = z.infer<typeof Project>;

/* ---------- GI products ---------- */

export const GICategory = z.enum([
  "handicraft",
  "textile",
  "agricultural",
  "foodstuff",
  "manufactured",
  "natural",
]);

export const GIProduct = z.object({
  id: z.string(),
  name: Localized,
  categories: z.array(GICategory).min(1),
  /** GI Registry application number, once verified. */
  applicationNo: z.string().nullable(),
  /** Date of filing as listed by the GI Registry (registration certificates are dated separately). */
  filingDate: isoDate.nullable().optional(),
  registrationYear: z.number().int().nullable(),
  /** Other States/UTs sharing this GI. */
  sharedWith: z.array(z.string()).optional(),
  region: Localized.nullable(),
  description: Localized.nullable(),
  sourceId: z.string().nullable(),
  url: z.string().url().nullable(),
  revisionStatus: RevisionStatus,
  confidence: Confidence,
  note: z.string().optional(),
});

export type GIProduct = z.infer<typeof GIProduct>;

/* ---------- Symbols ---------- */

export const StateSymbol = z.object({
  name: Localized,
  scientificName: z.string().optional(),
  sourceId: z.string().nullable(),
  url: z.string().url().nullable(),
  confidence: Confidence,
  revisionStatus: RevisionStatus,
});

/* ---------- Region ---------- */

/** MHA Zonal Councils (States Reorganisation Act 1956 / NEC Act 1971) — used for region filters. */
export const ZonalCouncil = z.enum(["northern", "central", "eastern", "western", "southern", "north-eastern", "islands"]);
export type ZonalCouncil = z.infer<typeof ZonalCouncil>;

export const CapitalRole = z.enum([
  "administrative",
  "legislative",
  "judicial",
  "summer",
  "winter",
  "winter-session",
  "national",
]);

export const Capital = z.object({
  role: CapitalRole,
  name: Localized,
  formerName: Localized.optional(),
  note: Localized.optional(),
});

export const GovernanceModel = z.enum(["state", "ut-with-legislature", "ut-without-legislature", "union"]);

export const Region = z.object({
  /** ISO 3166-2 code, e.g. IN-MH. India itself is "IN". */
  code: z.string().regex(/^IN(-[A-Z]{2})?$/),
  slug: z.string().regex(/^[a-z0-9-]+$/),
  type: z.enum(["state", "ut", "country"]),
  governanceModel: GovernanceModel,
  name: Localized,
  /** Name in the region's principal local script, where different from Devanagari hi/mr. */
  localName: z.object({ lang: z.string(), script: z.string(), text: z.string() }).optional(),
  formerNames: z.array(Localized).optional(),
  zonalCouncil: ZonalCouncil.nullable(),
  /** Editorial accent colour for the visual identity (hex). */
  accent: z.string().regex(/^#[0-9a-f]{6}$/i),
  /** Card motif key (see src/components/Motif.tsx). */
  motif: z.enum(["kolam", "warli", "madhubani", "pattachitra", "ikat", "jaali"]),
  /** Position on the tile-grid cartogram (not a boundary map). */
  tile: z.object({ row: z.number().int(), col: z.number().int() }).nullable(),
  capitals: z.array(Capital),
  officialPortal: z.string().url().nullable(),
  symbols: z.record(z.string(), StateSymbol).default({}),
  metrics: z.record(z.string(), DataPoint).default({}),
  timeSeries: z.record(z.string(), z.array(DataPoint)).default({}),
  government: z.object({
    headOfState: Officeholder.nullable(),
    headOfGovernment: Officeholder.nullable(),
    /** Deputy CMs, Speaker, Leader of Opposition… */
    others: z.array(Officeholder).default([]),
  }),
  projects: z.array(Project).default([]),
  giProducts: z.array(GIProduct).default([]),
  meta: z.object({
    lastUpdated: isoDate,
    editorialStatus: z.enum(["seed", "draft", "reviewed", "published"]),
  }),
});
export type Region = z.infer<typeof Region>;

/* ---------- Sources & glossary ---------- */

export const Source = z.object({
  id: z.string(),
  /** Short label used in "Source · Year" tooltips. */
  short: z.string(),
  /** Official (English) title of the source/publication. */
  name: z.string(),
  /** Official Hindi/Marathi title where one exists; UI falls back to `name`. */
  nameLocalized: Localized.optional(),
  publisher: z.string(),
  url: z.string().url(),
  category: z.enum([
    "demographics",
    "economy",
    "development",
    "health",
    "education",
    "environment",
    "transport-energy",
    "tourism-heritage",
    "gi",
    "governance",
    "tribal-social",
    "climate-hazards",
    "maps",
    "standards",
  ]),
  /** Preference order within the category (1 = most preferred). */
  priority: z.number().int().min(1),
  notes: z.string().optional(),
});
export type Source = z.infer<typeof Source>;

export const GlossaryEntry = z.object({
  id: z.string(),
  term: Localized,
  abbreviation: z.string().optional(),
  definition: Localized,
  related: z.array(z.string()).default([]),
});
export type GlossaryEntry = z.infer<typeof GlossaryEntry>;

export const SourcesFile = z.array(Source);
export const GlossaryFile = z.array(GlossaryEntry);

/** Indicators that are census/survey-only and must never be shown as annual series (Principle 4). */
export const CENSUS_ONLY_INDICATORS = [
  "literacyRate",
  "sexRatio",
  "childSexRatio",
  "urbanisation",
  "decadalGrowth",
] as const;


/* ---------- Module content (Section 7) ----------
 * Every module is a list of typed blocks so all 36 profiles share one template.
 */

export const ValueKind = z.enum(["count", "number", "percent", "rupeeCrore", "rupee", "ratio"]);
export const Polarity = z.enum(["higher-is-better", "lower-is-better", "neutral"]);

const Provenance = {
  sourceId: z.string().nullable(),
  url: z.string().url().nullable(),
  accessDate: isoDate.nullable(),
  confidence: Confidence,
};

const ProseBlock = z.object({
  type: z.literal("prose"),
  id: z.string(),
  title: Localized.optional(),
  /** Paragraphs separated by a blank line. Original writing only (Principle 10). */
  body: Localized,
  sourceIds: z.array(z.string()).default([]),
  confidence: Confidence,
});

const FactItem = z.object({
  id: z.string(),
  label: Localized,
  dp: DataPoint,
  kind: ValueKind,
  polarity: Polarity.default("neutral"),
  previous: DataPoint.optional(),
  national: DataPoint.optional(),
});

const FactsBlock = z.object({
  type: z.literal("facts"),
  id: z.string(),
  title: Localized.optional(),
  items: z.array(FactItem).min(1),
});

const ListItem = z.object({
  id: z.string(),
  name: Localized,
  detail: Localized.optional(),
  meta: Localized.optional(),
  tags: z.array(z.string()).optional(),
  /** Item-level provenance overrides the block's. */
  sourceId: z.string().nullable().optional(),
  url: z.string().url().nullable().optional(),
  confidence: Confidence.optional(),
});

const ListBlock = z.object({
  type: z.literal("list"),
  id: z.string(),
  title: Localized.optional(),
  layout: z.enum(["cards", "chips", "bullets"]),
  items: z.array(ListItem).min(1),
  /** Default provenance for every item. */
  ...Provenance,
});

const TimelineBlock = z.object({
  type: z.literal("timeline"),
  id: z.string(),
  title: Localized.optional(),
  events: z
    .array(
      z.object({
        id: z.string(),
        when: Localized,
        /** Sort key (year; negative for BCE). */
        year: z.number(),
        label: Localized,
        detail: Localized.optional(),
      }),
    )
    .min(1),
  ...Provenance,
});

const SeriesBlock = z.object({
  type: z.literal("series"),
  id: z.string(),
  title: Localized,
  kind: ValueKind,
  polarity: Polarity,
  series: z.array(z.object({ id: z.string(), label: Localized, points: z.array(DataPoint).min(1) })).min(1),
  note: Localized.optional(),
});

const TableBlock = z.object({
  type: z.literal("table"),
  id: z.string(),
  title: Localized,
  columns: z.array(z.object({ label: Localized, align: z.enum(["left", "right"]).default("left") })).min(1),
  rows: z.array(z.array(z.union([z.string(), z.number(), Localized]))).min(1),
  note: Localized.optional(),
  period: z.string().optional(),
  ...Provenance,
});

const LinksBlock = z.object({
  type: z.literal("links"),
  id: z.string(),
  title: Localized.optional(),
  items: z.array(z.object({ label: Localized, url: z.string().url(), detail: Localized.optional() })).min(1),
});

const WeatherBlock = z.object({
  type: z.literal("weather"),
  id: z.string(),
  places: z.array(z.object({ name: Localized, lat: z.number(), lon: z.number() })).min(1),
});

/** Renders region.projects / region.giProducts / region.government. */
const ProjectsBlock = z.object({ type: z.literal("projects"), id: z.string() });
const GIBlock = z.object({ type: z.literal("gi"), id: z.string() });
const OfficeholdersBlock = z.object({ type: z.literal("officeholders"), id: z.string() });

/** Fields this module should show but that are not yet sourced (feeds the gap report). */
const GapBlock = z.object({
  type: z.literal("gaps"),
  id: z.string(),
  items: z.array(z.object({ label: Localized, sourceId: z.string(), note: z.string() })).min(1),
});

export const Block = z.discriminatedUnion("type", [
  ProseBlock, FactsBlock, ListBlock, TimelineBlock, SeriesBlock, TableBlock, LinksBlock, WeatherBlock,
  ProjectsBlock, GIBlock, OfficeholdersBlock, GapBlock,
]);
export type Block = z.infer<typeof Block>;

export const ModuleContent = z.object({
  region: z.string().regex(/^IN(-[A-Z]{2})?$/),
  module: z.string(),
  asOf: isoDate,
  status: z.enum(["draft", "reviewed", "published"]),
  blocks: z.array(Block).min(1),
});
export type ModuleContent = z.infer<typeof ModuleContent>;

/* ---------- Comparison (data/compare/indicators.json) ---------- */

export const CompareIndicator = z.object({
  id: z.string(),
  label: Localized,
  kind: ValueKind,
  polarity: Polarity,
  /** Every region's value must be for this one period (Principle 4). */
  period: z.string(),
  values: z.record(z.string(), DataPoint),
  national: DataPoint.nullable(),
  note: Localized.optional(),
});
export type CompareIndicator = z.infer<typeof CompareIndicator>;

export const CompareFile = z.object({
  asOf: isoDate,
  regions: z.array(z.string().regex(/^IN-[A-Z]{2}$/)).min(2),
  defaultSelection: z.array(z.string()).min(2).max(4),
  groups: z.array(z.object({ id: z.string(), label: Localized, indicators: z.array(CompareIndicator).min(1) })).min(1),
  trend: SeriesBlock,
});
export type CompareFile = z.infer<typeof CompareFile>;
