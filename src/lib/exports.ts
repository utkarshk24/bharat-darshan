import { cache } from "react";
import type { DataPoint, Localized, Officeholder } from "./schema";
import { getAuthoredModules, getCompare, getGlossary, getIndia, getModule, getRegions, getSources, getDataAsOn } from "./data";

/**
 * Bulk downloads for the Data Library (served as static files under /downloads/).
 * Every row keeps its provenance columns; a missing value is an empty cell with status "not_available".
 */

type Cell = string | number | boolean | null | undefined;
const esc = (v: Cell) => {
  if (v === null || v === undefined) return "";
  const s = String(v);
  return /[",\n\r]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
};
/** UTF-8 with a byte-order mark so spreadsheet apps show Devanagari correctly. */
export const toCsv = (head: string[], rows: Cell[][]) => "﻿" + [head, ...rows].map((r) => r.map(esc).join(",")).join("\r\n") + "\r\n";

const sourceShort = () => Object.fromEntries(getSources().map((s) => [s.id, s.short]));
const loc = (l: Localized | null | undefined) => [l?.en ?? "", l?.hi ?? "", l?.mr ?? ""];

const DP_HEAD = ["value", "unit", "period", "status", "source_id", "source", "url", "access_date", "revision_status", "confidence", "note"];
function dpCells(dp: DataPoint | null | undefined, src: Record<string, string>): Cell[] {
  if (!dp) return ["", "", "", "not_available", "", "", "", "", "", "", ""];
  const has = dp.value !== null && dp.value !== undefined;
  return [
    has ? dp.value : "",
    dp.unit,
    dp.period,
    has ? "available" : "not_available",
    dp.sourceId,
    dp.sourceId ? src[dp.sourceId] ?? dp.sourceId : "",
    dp.url,
    dp.accessDate,
    dp.revisionStatus,
    dp.confidence,
    dp.note,
  ];
}

const regionRows = () => getRegions().filter((r) => r.type !== "country");

function indicatorsCsv() {
  const c = getCompare();
  if (!c) return toCsv(["error"], [["compare data missing"]]);
  const src = sourceShort();
  const regions = Object.fromEntries(getRegions().map((r) => [r.code, r]));
  const rows: Cell[][] = [];
  for (const g of c.groups)
    for (const ind of g.indicators) {
      for (const code of c.regions) {
        const r = regions[code];
        rows.push([code, r?.name.en, r?.type, g.id, ind.id, ind.label.en, ind.polarity, ind.period, ...dpCells(ind.values[code], src)]);
      }
      rows.push(["IN", "India", "country", g.id, ind.id, ind.label.en, ind.polarity, ind.period, ...dpCells(ind.national, src)]);
    }
  return toCsv(["region_code", "region", "region_type", "group", "indicator_id", "indicator", "polarity", "indicator_period", ...DP_HEAD], rows);
}

function metricsCsv() {
  const src = sourceShort();
  const rows: Cell[][] = [];
  for (const r of [getIndia(), ...regionRows()])
    for (const [k, dp] of Object.entries(r.metrics as Record<string, DataPoint | null>)) rows.push([r.code, r.name.en, r.type, k, ...dpCells(dp, src)]);
  return toCsv(["region_code", "region", "region_type", "metric", ...DP_HEAD], rows);
}

function regionsCsv() {
  const rows = regionRows().map((r) => [
    r.code,
    r.slug,
    r.type,
    ...loc(r.name),
    r.capitals.map((c) => `${c.name.en} (${c.role})`).join("; "),
    r.zonalCouncil,
    r.governanceModel,
    r.officialPortal,
  ]);
  return toCsv(["code", "slug", "type", "name_en", "name_hi", "name_mr", "capitals", "zonal_council", "governance_model", "official_portal"], rows);
}

function officeholdersCsv() {
  const src = sourceShort();
  const rows: Cell[][] = [];
  const add = (code: string, o: Officeholder | null) => {
    if (!o) return;
    rows.push([
      code,
      o.role,
      ...loc(o.name),
      o.name ? "named" : "to_be_verified",
      o.party,
      o.since,
      o.asOf,
      o.sourceId,
      o.sourceId ? src[o.sourceId] ?? o.sourceId : "",
      o.url,
      o.verifyUrl,
      o.revisionStatus,
      o.confidence,
      o.note,
    ]);
  };
  for (const r of regionRows()) {
    add(r.code, r.government.headOfState);
    add(r.code, r.government.headOfGovernment);
    for (const o of r.government.others) add(r.code, o);
  }
  return toCsv(
    ["region_code", "role", "name_en", "name_hi", "name_mr", "status", "party", "since", "as_of", "source_id", "source", "url", "verify_url", "revision_status", "confidence", "note"],
    rows,
  );
}

function giCsv() {
  const src = sourceShort();
  const rows: Cell[][] = [];
  for (const r of regionRows())
    for (const p of r.giProducts)
      rows.push([
        r.code,
        p.id,
        ...loc(p.name),
        p.categories.join("; "),
        p.applicationNo,
        p.filingDate,
        p.registrationYear,
        (p as { sharedWith?: string[] }).sharedWith?.join("; "),
        p.sourceId,
        p.sourceId ? src[p.sourceId] ?? p.sourceId : "",
        p.url,
        p.revisionStatus,
        p.confidence,
        p.note,
      ]);
  return toCsv(
    ["region_code", "id", "name_en", "name_hi", "name_mr", "categories", "application_no", "filing_date", "registration_year", "shared_with", "source_id", "source", "url", "revision_status", "confidence", "note"],
    rows,
  );
}

function projectsCsv() {
  const src = sourceShort();
  const rows: Cell[][] = [];
  for (const r of regionRows())
    for (const p of r.projects) {
      const cost = p.cost as DataPoint | null | undefined;
      rows.push([
        r.code,
        p.id,
        ...loc(p.name),
        p.sector,
        p.agency,
        p.start,
        p.completion,
        p.status,
        cost?.value ?? "",
        cost?.unit,
        cost?.period,
        p.asOf,
        p.sourceId,
        p.sourceId ? src[p.sourceId] ?? p.sourceId : "",
        p.url,
        p.confidence,
      ]);
    }
  return toCsv(
    ["region_code", "id", "name_en", "name_hi", "name_mr", "sector", "agency", "start", "completion", "status", "cost_value", "cost_unit", "cost_period", "as_of", "source_id", "source", "url", "confidence"],
    rows,
  );
}

function sourcesCsv() {
  const rows = getSources().map((s) => [s.id, s.short, s.name, s.publisher, s.url, s.category, s.priority, s.notes]);
  return toCsv(["id", "short", "name", "publisher", "url", "category", "priority", "notes"], rows);
}

const json = (v: unknown) => JSON.stringify(v, null, 1) + "\n";

/** The full record for one region: the region file plus every authored profile module. */
export function profileJson(code: string): string | null {
  const r = getRegions().find((x) => x.code === code);
  if (!r) return null;
  const modules = Object.fromEntries(getAuthoredModules(code).map((m) => [m, getModule(code, m)]));
  return json({ generated: getDataAsOn(), region: r, modules });
}

export interface DownloadFile {
  file: string;
  kind: "csv" | "json";
  /** Message key under dataLibrary.files.* */
  key: string;
  build: () => string;
}

export const DOWNLOADS: DownloadFile[] = [
  { file: "indicators.csv", kind: "csv", key: "indicators", build: indicatorsCsv },
  { file: "indicators.json", kind: "json", key: "indicatorsJson", build: () => json(getCompare()) },
  { file: "region-metrics.csv", kind: "csv", key: "metrics", build: metricsCsv },
  { file: "regions.csv", kind: "csv", key: "regions", build: regionsCsv },
  { file: "officeholders.csv", kind: "csv", key: "officeholders", build: officeholdersCsv },
  { file: "gi-products.csv", kind: "csv", key: "gi", build: giCsv },
  { file: "projects.csv", kind: "csv", key: "projects", build: projectsCsv },
  { file: "sources.csv", kind: "csv", key: "sources", build: sourcesCsv },
  { file: "glossary.json", kind: "json", key: "glossary", build: () => json(getGlossary()) },
];

/** Built once per build; sizes are shown on the Data Library page. */
export const getDownloadSizes = cache(() =>
  Object.fromEntries(DOWNLOADS.map((d) => [d.file, Buffer.byteLength(d.build(), "utf8")])),
);

export const profileCodes = () => regionRows().map((r) => r.code);
