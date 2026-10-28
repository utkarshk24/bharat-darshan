import "server-only";
import { readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import { cache } from "react";
import { existsSync } from "node:fs";
import { MAP_METRICS } from "./mapMetrics";
import { CompareFile, GlossaryFile, ModuleContent, Region, SourcesFile, type DataPoint, type Officeholder } from "./schema";

const DATA = path.join(process.cwd(), "data");
const readJson = (p: string) => JSON.parse(readFileSync(path.join(DATA, p), "utf8"));

/** All 36 States/UTs, parsed and validated at build time. */
export const getRegions = cache((): Region[] => {
  const files = readdirSync(path.join(DATA, "regions")).filter((f) => f.endsWith(".json"));
  return files
    .map((f) => Region.parse(readJson(`regions/${f}`)))
    .sort((a, b) => a.name.en.localeCompare(b.name.en));
});

export const getIndia = cache((): Region => Region.parse(readJson("india.json")));
export const getSources = cache(() => SourcesFile.parse(readJson("sources.json")));
export const getGlossary = cache(() => GlossaryFile.parse(readJson("glossary.json")));

export function getRegion(type: "state" | "ut", slug: string): Region | undefined {
  return getRegions().find((r) => r.type === type && r.slug === slug);
}

export const sourceName = (id: string | null) => (id ? getSources().find((s) => s.id === id) : undefined);

/** Latest dataset change across all files — drives the "Data as on" badge. */
export function getDataAsOn(): string {
  return [getIndia(), ...getRegions()].map((r) => r.meta.lastUpdated).sort().at(-1)!;
}

/** Serializable subset passed to client components (cards, map, search). */
export interface RegionSummary {
  code: string;
  slug: string;
  type: "state" | "ut";
  name: Region["name"];
  localName?: Region["localName"];
  formerNames?: Region["formerNames"];
  zonalCouncil: Region["zonalCouncil"];
  accent: string;
  motif: Region["motif"];
  tile: Region["tile"];
  capitals: Region["capitals"];
  governanceModel: Region["governanceModel"];
  population2011: DataPoint | null;
  gsdpCurrent: DataPoint | null;
  headOfState: Officeholder | null;
  headOfGovernment: Officeholder | null;
  sourceLabels: Record<string, string>;
  /** Sourced figures used by the map's data layers (only the keys in MAP_METRICS). */
  /** Keys are MAP_METRICS (built in) or "c-<indicator>" (comparison layers added on the map page). */
  mapMetrics: Partial<Record<string, DataPoint>>;
}

const slimOffice = (o: Officeholder | null): Officeholder | null => (o ? { ...o, note: undefined, verifyUrl: null } : null);

export function summarize(r: Region): RegionSummary {
  const pop = r.metrics.population2011 ?? null;
  const gsdp = r.metrics.gsdpCurrent ?? null;
  const labels: Record<string, string> = {};
  const mapMetrics: Partial<Record<string, DataPoint>> = {};
  for (const k of MAP_METRICS) {
    const dp = (r.metrics as Record<string, DataPoint | null | undefined>)[k];
    // Only what the map shows, to keep page payloads small
    if (dp && typeof dp.value === "number") mapMetrics[k] = { value: dp.value, unit: dp.unit, period: dp.period, sourceId: dp.sourceId, url: dp.url } as DataPoint;
  }
  for (const id of [pop?.sourceId, gsdp?.sourceId, r.government.headOfState?.sourceId, r.government.headOfGovernment?.sourceId, ...Object.values(mapMetrics).map((d) => d?.sourceId)]) {
    if (id) labels[id] = sourceName(id)?.short ?? id;
  }
  return {
    code: r.code,
    slug: r.slug,
    type: r.type as "state" | "ut",
    name: r.name,
    localName: r.localName,
    formerNames: r.formerNames,
    zonalCouncil: r.zonalCouncil,
    accent: r.accent,
    motif: r.motif,
    tile: r.tile,
    capitals: r.capitals,
    governanceModel: r.governanceModel,
    population2011: pop,
    gsdpCurrent: gsdp,
    // Cards and the map show only the role and name; the long provenance notes stay on the profile page.
    headOfState: slimOffice(r.government.headOfState),
    headOfGovernment: slimOffice(r.government.headOfGovernment),
    sourceLabels: labels,
    mapMetrics,
  };
}

export const getSummaries = cache(() => getRegions().map(summarize));

/** Module content for a region, if authored (data/modules/IN-XX/<module>.json). */
export const getModule = cache((code: string, module: string): ModuleContent | null => {
  const p = path.join(DATA, "modules", code, `${module}.json`);
  if (!existsSync(p)) return null;
  return ModuleContent.parse(JSON.parse(readFileSync(p, "utf8")));
});

/** Which modules have authored content, for the module nav. */
export const getAuthoredModules = cache((code: string): string[] => {
  const dir = path.join(DATA, "modules", code);
  if (!existsSync(dir)) return [];
  return readdirSync(dir).filter((f) => f.endsWith(".json")).map((f) => f.replace(/\.json$/, ""));
});

/** Comparison prototype data (data/compare/indicators.json). */
export const getCompare = cache((): CompareFile | null => {
  const p = path.join(DATA, "compare", "indicators.json");
  return existsSync(p) ? CompareFile.parse(JSON.parse(readFileSync(p, "utf8"))) : null;
});

/** Region reference used by national listings (GI directory, projects dashboard). */
export interface RegionRef {
  code: string;
  name: Region["name"];
  href: string;
  accent: string;
  type: Region["type"];
}
export const regionRef = (r: Region): RegionRef => ({
  code: r.code,
  name: r.name,
  href: `/${r.type === "state" ? "states" : "uts"}/${r.slug}`,
  accent: r.accent,
  type: r.type,
});

/** Every registered GI recorded in a region file, with the region that lists it. */
export const getAllGI = cache(() =>
  getRegions().flatMap((r) => r.giProducts.map((p) => ({ product: p, region: regionRef(r) }))),
);

/** Every project recorded in a region file, with its region. */
export const getAllProjects = cache(() =>
  getRegions().flatMap((r) => r.projects.map((p) => ({ project: p, region: regionRef(r) }))),
);

/** English region name → localized name, for fields stored as English names (e.g. GI sharedWith). */
export const getRegionNameMap = cache(() => {
  const m: Record<string, Region["name"]> = {};
  for (const r of getRegions()) {
    m[r.name.en] = r.name;
    for (const f of r.formerNames ?? []) m[f.en] = r.name;
  }
  return m;
});
