/**
 * Dataset validation (Section 14.4). Pure functions so they can be unit-tested;
 * scripts/validate-data.ts does the file I/O and reporting.
 */
import { CENSUS_ONLY_INDICATORS, CompareFile, GlossaryFile, ModuleContent, Region, SourcesFile } from "./schema";
import { MODULES } from "./nav";
import type { z } from "zod";

export type Severity = "error" | "warning" | "gap";
export interface Finding {
  severity: Severity;
  file: string;
  path: string;
  message: string;
}

export interface RawFiles {
  india: { file: string; json: unknown };
  regions: { file: string; json: unknown }[];
  sources: unknown;
  glossary: unknown;
  mapManifest?: unknown;
  /** data/modules/IN-XX/<module>.json files */
  modules?: { file: string; json: unknown }[];
  /** data/compare/indicators.json */
  compare?: unknown;
}

const STALE_MONTHS = 6;

function monthsBetween(a: Date, b: Date) {
  return (b.getFullYear() - a.getFullYear()) * 12 + (b.getMonth() - a.getMonth()) - (b.getDate() < a.getDate() ? 1 : 0);
}

function isLocalized(v: unknown): v is { en: string; hi: string; mr: string } {
  return !!v && typeof v === "object" && "en" in v && "hi" in v && "mr" in v;
}

/** Walk any JSON value, calling fn for every object node with its dotted path. */
function walk(v: unknown, path: string, fn: (node: Record<string, unknown>, path: string) => void) {
  if (Array.isArray(v)) v.forEach((x, i) => walk(x, `${path}[${i}]`, fn));
  else if (v && typeof v === "object") {
    fn(v as Record<string, unknown>, path);
    for (const [k, x] of Object.entries(v)) walk(x, path ? `${path}.${k}` : k, fn);
  }
}

function zodIssues(file: string, err: z.ZodError): Finding[] {
  return err.issues.map((i) => ({
    severity: "error" as const,
    file,
    path: i.path.join("."),
    message: i.message,
  }));
}

export function validateDataset(raw: RawFiles, today = new Date()): Finding[] {
  const out: Finding[] = [];

  /* Sources */
  const sources = SourcesFile.safeParse(raw.sources);
  if (!sources.success) out.push(...zodIssues("sources.json", sources.error));
  const sourceIds = new Set(sources.success ? sources.data.map((s) => s.id) : []);
  if (sources.success) {
    const seen = new Set<string>();
    for (const s of sources.data) {
      if (seen.has(s.id)) out.push({ severity: "error", file: "sources.json", path: s.id, message: "duplicate source id" });
      seen.add(s.id);
    }
  }

  /* Glossary */
  const glossary = GlossaryFile.safeParse(raw.glossary);
  if (!glossary.success) out.push(...zodIssues("glossary.json", glossary.error));

  /* Regions */
  const all = [raw.india, ...raw.regions];
  const parsed: { file: string; region: Region }[] = [];
  for (const { file, json } of all) {
    const r = Region.safeParse(json);
    if (!r.success) out.push(...zodIssues(file, r.error));
    else parsed.push({ file, region: r.data });
  }

  /* Coverage (Section 4) */
  const states = parsed.filter((p) => p.region.type === "state").length;
  const uts = parsed.filter((p) => p.region.type === "ut").length;
  if (states !== 28) out.push({ severity: "error", file: "regions/", path: "", message: `expected 28 States, found ${states}` });
  if (uts !== 8) out.push({ severity: "error", file: "regions/", path: "", message: `expected 8 UTs, found ${uts}` });

  const codes = new Map<string, string>();
  const slugs = new Map<string, string>();
  const tiles = new Map<string, string>();
  for (const { file, region } of parsed) {
    if (codes.has(region.code)) out.push({ severity: "error", file, path: "code", message: `duplicate code ${region.code} (also in ${codes.get(region.code)})` });
    codes.set(region.code, file);
    if (slugs.has(region.slug)) out.push({ severity: "error", file, path: "slug", message: `duplicate slug ${region.slug}` });
    slugs.set(region.slug, file);
    if (region.tile) {
      const k = `${region.tile.row},${region.tile.col}`;
      if (tiles.has(k)) out.push({ severity: "error", file, path: "tile", message: `tile ${k} collides with ${tiles.get(k)}` });
      tiles.set(k, region.code);
    }
    if (region.type !== "country" && !file.endsWith(`${region.code}.json`)) {
      out.push({ severity: "error", file, path: "code", message: `file name must be ${region.code}.json` });
    }
    // Governance model consistency (Section 7, UT adaptations)
    const hos = region.government.headOfState;
    if (region.type === "state" && hos && hos.role !== "governor") {
      out.push({ severity: "error", file, path: "government.headOfState.role", message: "a State's head is the Governor" });
    }
    if (region.type === "ut" && hos && hos.role === "governor") {
      out.push({ severity: "error", file, path: "government.headOfState.role", message: "a UT is headed by a Lt Governor or Administrator" });
    }
    if (region.governanceModel === "ut-without-legislature" && region.government.headOfGovernment) {
      out.push({ severity: "error", file, path: "government.headOfGovernment", message: "UT without legislature cannot have a Chief Minister" });
    }
  }

  /* Module content */
  const regionCodes = new Set(parsed.map((p) => p.region.code));
  const moduleFiles = raw.modules ?? [];
  for (const { file, json } of moduleFiles) {
    const m = ModuleContent.safeParse(json);
    if (!m.success) {
      out.push(...zodIssues(file, m.error));
      continue;
    }
    const mc = m.data;
    if (!(MODULES as readonly string[]).includes(mc.module)) out.push({ severity: "error", file, path: "module", message: `unknown module "${mc.module}"` });
    if (!file.endsWith(`${mc.region}/${mc.module}.json`)) out.push({ severity: "error", file, path: "", message: `file must be modules/${mc.region}/${mc.module}.json` });
    if (!regionCodes.has(mc.region)) out.push({ severity: "error", file, path: "region", message: `unknown region ${mc.region}` });
    const ids = new Set<string>();
    mc.blocks.forEach((b, i) => {
      if (ids.has(b.id)) out.push({ severity: "error", file, path: `blocks[${i}].id`, message: `duplicate block id ${b.id}` });
      ids.add(b.id);
      if (b.type === "prose") {
        for (const sid of b.sourceIds) if (!sourceIds.has(sid)) out.push({ severity: "error", file, path: `blocks[${i}].sourceIds`, message: `unknown source "${sid}"` });
        if (b.confidence !== "Editorial" && b.sourceIds.length === 0) out.push({ severity: "error", file, path: `blocks[${i}]`, message: "non-editorial prose must cite sources" });
      }
      if (b.type === "series") {
        for (const s of b.series) {
          const types = new Set(s.points.map((p) => p.periodType));
          if (types.size > 1) out.push({ severity: "error", file, path: `blocks[${i}].${s.id}`, message: `mixed period types: ${[...types].join(", ")}` });
          const bases = new Set(s.points.map((p) => (p.priceBase ? `${p.priceBase.type}:${p.priceBase.baseYear ?? ""}` : "none")));
          if (bases.size > 1) out.push({ severity: "error", file, path: `blocks[${i}].${s.id}`, message: "mixed price bases" });
        }
      }
      if (b.type === "table") {
        b.rows.forEach((r, j) => {
          if (r.length !== b.columns.length) out.push({ severity: "error", file, path: `blocks[${i}].rows[${j}]`, message: "row length does not match columns" });
        });
      }
      if (b.type === "gaps") for (const g of b.items) out.push({ severity: "gap", file, path: `blocks[${i}]`, message: `${g.label.en}: ${g.note}` });
    });
  }

  /* Comparison file: one period per indicator, every listed region present, known regions only */
  if (raw.compare !== undefined) {
    const file = "compare/indicators.json";
    const c = CompareFile.safeParse(raw.compare);
    if (!c.success) out.push(...zodIssues(file, c.error));
    else {
      for (const code of [...c.data.regions, ...c.data.defaultSelection]) {
        if (!regionCodes.has(code)) out.push({ severity: "error", file, path: "regions", message: `unknown region ${code}` });
      }
      for (const code of c.data.defaultSelection) {
        if (!c.data.regions.includes(code)) out.push({ severity: "error", file, path: "defaultSelection", message: `${code} is not in regions` });
      }
      for (const g of c.data.groups) {
        for (const ind of g.indicators) {
          const path = `${g.id}.${ind.id}`;
          for (const code of c.data.regions) {
            const v = ind.values[code];
            if (!v) out.push({ severity: "error", file, path, message: `missing value entry for ${code} (use a TODO data point)` });
            else if (v.period !== ind.period) out.push({ severity: "error", file, path: `${path}.${code}`, message: `period ${v.period} differs from indicator period ${ind.period}` });
            else if (v.value === null) out.push({ severity: "gap", file, path: `${path}.${code}`, message: `${ind.label.en} (${code}): ${v.note ?? ""}` });
          }
          const bases = new Set(Object.values(ind.values).map((v) => (v.priceBase ? `${v.priceBase.type}:${v.priceBase.baseYear ?? ""}` : "none")));
          if (bases.size > 1) out.push({ severity: "error", file, path, message: "mixed price bases across regions" });
          if (ind.national && ind.national.period !== ind.period) out.push({ severity: "error", file, path: `${path}.national`, message: `national period ${ind.national.period} differs from ${ind.period}` });
        }
      }
      for (const s of c.data.trend.series) {
        if (!regionCodes.has(s.id)) out.push({ severity: "error", file, path: `trend.${s.id}`, message: "trend series id must be a region code" });
        if (new Set(s.points.map((p) => p.periodType)).size > 1) out.push({ severity: "error", file, path: `trend.${s.id}`, message: "mixed period types" });
      }
    }
  }

  /* Per-file content checks on the raw JSON (so translation gaps are caught even in nested optional fields) */
  for (const { file, json } of [...all, ...moduleFiles, ...(raw.compare !== undefined ? [{ file: "compare/indicators.json", json: raw.compare }] : [])]) {
    walk(json, "", (node, path) => {
      // Missing translations
      if (isLocalized(node)) {
        for (const loc of ["en", "hi", "mr"] as const) {
          if (typeof node[loc] === "string" && node[loc].trim() === "") {
            out.push({ severity: "warning", file, path: `${path}.${loc}`, message: "missing translation" });
          }
        }
      }
      if (!("revisionStatus" in node) && typeof node.sourceId === "string" && !sourceIds.has(node.sourceId)) {
        out.push({ severity: "error", file, path: `${path}.sourceId`, message: `unknown source "${node.sourceId}"` });
      }
      // Data points & officeholders share these keys
      if ("revisionStatus" in node) {
        const sid = node.sourceId as string | null | undefined;
        if (sid && !sourceIds.has(sid)) {
          out.push({ severity: "error", file, path: `${path}.sourceId`, message: `unknown source "${sid}"` });
        }
        if (node.revisionStatus === "TODO") {
          out.push({ severity: "gap", file, path, message: String(node.note ?? "value not yet sourced") });
        }
        if ("value" in node && node.value !== null && node.accessDate === null) {
          out.push({ severity: "warning", file, path, message: "value present but never verified (accessDate is null)" });
        }
        if ("sourceId" in node && node.sourceId === null && node.revisionStatus !== "TODO") {
          out.push({ severity: "warning", file, path, message: "missing source" });
        }
        if (typeof node.asOf === "string") {
          const m = monthsBetween(new Date(node.asOf), today);
          if (m >= STALE_MONTHS) {
            out.push({ severity: "warning", file, path: `${path}.asOf`, message: `asOf ${node.asOf} is ${m} months old — re-verify` });
          }
        }
      }
    });
  }

  /* Period hygiene in time series (Principle 4) */
  for (const { file, region } of parsed) {
    for (const [key, series] of Object.entries(region.timeSeries)) {
      const types = new Set(series.map((p) => p.periodType));
      if (types.size > 1) {
        out.push({ severity: "error", file, path: `timeSeries.${key}`, message: `mixed period types: ${[...types].join(", ")}` });
      }
      const bases = new Set(series.map((p) => (p.priceBase ? `${p.priceBase.type}:${p.priceBase.baseYear ?? ""}` : "none")));
      if (bases.size > 1) {
        out.push({ severity: "error", file, path: `timeSeries.${key}`, message: `mixed price bases: ${[...bases].join(", ")}` });
      }
      const periods = series.map((p) => p.period);
      if (new Set(periods).size !== periods.length) {
        out.push({ severity: "error", file, path: `timeSeries.${key}`, message: "duplicate periods" });
      }
      const censusOnly = CENSUS_ONLY_INDICATORS.some((c) => key.toLowerCase().startsWith(c.toLowerCase()));
      if (censusOnly && series.some((p) => p.periodType === "fy" || p.periodType === "calendar")) {
        out.push({ severity: "error", file, path: `timeSeries.${key}`, message: "census-only indicator cannot have an annual series" });
      }
    }
  }

  /* Official map (Principle 8) */
  const mm = raw.mapManifest as { boundaries?: { file?: string | null; sourceId?: string; verified?: boolean } } | undefined;
  if (!mm?.boundaries?.file) {
    out.push({ severity: "gap", file: "public/maps/manifest.json", path: "boundaries", message: "No official Survey of India boundary file installed; the site uses the tile-grid cartogram (no boundaries drawn)." });
  } else if (mm.boundaries.sourceId !== "survey-of-india" || mm.boundaries.verified !== true) {
    out.push({ severity: "error", file: "public/maps/manifest.json", path: "boundaries", message: "Boundary file must be sourced from Survey of India and marked verified before use." });
  }

  return out;
}

/** Collect every URL in the dataset, for the optional link checker. */
export function collectUrls(raw: RawFiles): string[] {
  const urls = new Set<string>();
  for (const v of [raw.india.json, ...raw.regions.map((r) => r.json), raw.sources]) {
    walk(v, "", (node) => {
      for (const k of ["url", "verifyUrl", "officialPortal"]) {
        const u = node[k];
        if (typeof u === "string" && /^https?:\/\//.test(u)) urls.add(u);
      }
    });
  }
  return [...urls].sort();
}
