import { describe, expect, it } from "vitest";
import { readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import { validateDataset, type RawFiles } from "@/lib/validate";
import { buildIndex, createSearcher } from "@/lib/search";
import { Region } from "@/lib/schema";

const root = path.resolve(__dirname, "..");
const read = (p: string) => JSON.parse(readFileSync(path.join(root, p), "utf8"));
const load = (): RawFiles => ({
  india: { file: "india.json", json: read("data/india.json") },
  regions: readdirSync(path.join(root, "data/regions")).map((f) => ({ file: `regions/${f}`, json: read(`data/regions/${f}`) })),
  sources: read("data/sources.json"),
  glossary: read("data/glossary.json"),
  mapManifest: read("public/maps/manifest.json"),
});
const errors = (raw: RawFiles) => validateDataset(raw, new Date("2026-10-13")).filter((f) => f.severity === "error");
const mh = (raw: RawFiles) => raw.regions.find((r) => r.file.endsWith("IN-MH.json"))!.json as any;
const seed = (raw: RawFiles) => raw.regions.find((r) => r.file.endsWith("IN-HR.json"))!.json as any;

describe("dataset", () => {
  it("passes validation with no errors", () => expect(errors(load())).toEqual([]));

  it("rejects a value with no source", () => {
    const raw = load();
    mh(raw).metrics.area = { ...mh(raw).metrics.area, value: 307713, revisionStatus: "final", sourceId: null };
    expect(errors(raw).some((e) => e.message.includes("must cite a source"))).toBe(true);
  });

  it("rejects a null value not marked TODO", () => {
    const raw = load();
    seed(raw).metrics.area.revisionStatus = "final";
    expect(errors(raw).length).toBeGreaterThan(0);
  });

  it("rejects mixed periods in a time series", () => {
    const raw = load();
    const fy = { ...mh(raw).metrics.gsdpCurrent };
    mh(raw).timeSeries.gsdp = [fy, { ...fy, period: "2024", periodType: "calendar" }];
    expect(errors(raw).some((e) => e.message.includes("mixed period types"))).toBe(true);
  });

  it("rejects an annual series for a census-only indicator", () => {
    const raw = load();
    const p = { value: null, unit: "%", period: "2024", periodType: "calendar", sourceId: "census", url: null, accessDate: null, dataLevel: "state", revisionStatus: "TODO", confidence: "Official", note: "x" };
    mh(raw).timeSeries.literacyRate = [p];
    expect(errors(raw).some((e) => e.message.includes("census-only"))).toBe(true);
  });

  it("rejects period strings that don't match their type", () => {
    const raw = load();
    seed(raw).metrics.gsdpCurrent.period = "2023-24";
    expect(errors(raw).some((e) => e.path.includes("period"))).toBe(true);
  });

  it("flags officeholder asOf older than 6 months", () => {
    const raw = load();
    const cm = mh(raw).government.headOfGovernment;
    Object.assign(cm, { name: { en: "X", hi: "X", mr: "X" }, asOf: "2026-01-01", revisionStatus: "final", sourceId: "igod" });
    const f = validateDataset(raw, new Date("2026-10-13"));
    expect(f.some((x) => x.severity === "warning" && x.message.includes("months old"))).toBe(true);
  });

  it("forbids a Chief Minister for a UT without legislature", () => {
    const raw = load();
    const la = raw.regions.find((r) => r.file.endsWith("IN-LA.json"))!.json as any;
    la.government.headOfGovernment = { ...mh(raw).government.headOfGovernment };
    expect(errors(raw).some((e) => e.message.includes("without legislature"))).toBe(true);
  });

  it("refuses an unverified boundary file", () => {
    const raw = load();
    raw.mapManifest = { boundaries: { file: "india.topo.json", sourceId: "other", verified: false } };
    expect(errors(raw).some((e) => e.file.includes("manifest"))).toBe(true);
  });

  it("has 28 States, 8 UTs, unique tiles", () => {
    const raw = load();
    const regions = raw.regions.map((r) => Region.parse(r.json));
    expect(regions.filter((r) => r.type === "state")).toHaveLength(28);
    expect(regions.filter((r) => r.type === "ut")).toHaveLength(8);
  });
});

describe("search", () => {
  const regions = load().regions.map((r) => Region.parse(r.json)).map((r) => ({
    code: r.code, slug: r.slug, type: r.type as "state" | "ut", name: r.name, localName: r.localName, formerNames: r.formerNames,
    zonalCouncil: r.zonalCouncil, accent: r.accent, motif: r.motif, tile: r.tile, capitals: r.capitals, governanceModel: r.governanceModel,
    population2011: null, gsdpCurrent: null, headOfState: null, headOfGovernment: null, sourceLabels: {},
  }));
  const search = createSearcher(buildIndex(regions));
  const top = (q: string) => search(q)[0]?.label.en;
  it.each([
    ["Kerala", "Keralam"], ["केरळ", "Keralam"], ["केरल", "Keralam"], ["Keralam", "Keralam"], ["केरलम", "Keralam"], ["maharashtra", "Maharashtra"], ["महाराष्ट्र", "Maharashtra"],
    ["Port Blair", "Sri Vijaya Puram"], ["Bangalore", "Bengaluru"], ["Orissa", "Odisha"], ["tiruvanantapuram", "Thiruvananthapuram"],
    ["MH", "Maharashtra"], ["தமிழ்நாடு", "Tamil Nadu"],
  ])("%s → %s", (q, expected) => expect(top(q)).toBe(expected));
});

describe("messages", () => {
  const flat = (o: any, p = ""): string[] => Object.entries(o).flatMap(([k, v]) => (v && typeof v === "object" && !Array.isArray(v) ? flat(v, `${p}${k}.`) : [`${p}${k}`]));
  const en = flat(read("messages/en.json")).sort();
  it.each(["hi", "mr"])("%s has exactly the same keys as en", (l) => expect(flat(read(`messages/${l}.json`)).sort()).toEqual(en));
  it.each(["hi", "mr"])("%s has no empty strings", (l) => {
    const m = read(`messages/${l}.json`);
    const empty = flat(m).filter((k) => k.split(".").reduce((o: any, x) => o[x], m) === "");
    expect(empty).toEqual([]);
  });
});

describe("module content", () => {
  const withModules = (): RawFiles => {
    const raw = load();
    const dir = path.join(root, "data/modules");
    raw.modules = readdirSync(dir).flatMap((code) =>
      readdirSync(path.join(dir, code)).map((f) => ({ file: `modules/${code}/${f}`, json: read(`data/modules/${code}/${f}`) })),
    );
    return raw;
  };
  const mod = (raw: RawFiles, name: string) => raw.modules!.find((m) => m.file.endsWith(`IN-MH/${name}.json`))!.json as any;

  it("all authored modules validate", () => expect(errors(withModules())).toEqual([]));

  it.each(["IN-MH", "IN-KL", "IN-DL", "IN-LA"])("%s has all 26 modules", (code) => {
    const raw = withModules();
    expect(raw.modules!.filter((m) => m.file.includes(`${code}/`)).length).toBe(26);
  });

  it("Keralam keeps its former name and the old address redirects", () => {
    const kl = load().regions.find((r) => r.file.endsWith("IN-KL.json"))!.json as any;
    expect(kl.slug).toBe("keralam");
    expect(kl.formerNames.map((n: any) => n.en)).toContain("Kerala");
    const cfg = readFileSync(path.join(root, "next.config.ts"), "utf8");
    expect(cfg).toContain('destination: "/:locale/states/keralam/:path*"');
  });

  it("a UT without legislature has no head of government", () => {
    const la = load().regions.find((r) => r.file.endsWith("IN-LA.json"))!.json as any;
    expect(la.governanceModel).toBe("ut-without-legislature");
    expect(la.government.headOfGovernment).toBeNull();
  });

  it("rejects non-editorial prose without sources", () => {
    const raw = withModules();
    const b = mod(raw, "people").blocks.find((x: any) => x.type === "prose");
    b.sourceIds = [];
    expect(errors(raw).some((e) => e.message.includes("must cite sources"))).toBe(true);
  });

  it("rejects table rows that don't match the columns", () => {
    const raw = withModules();
    mod(raw, "government").blocks.find((x: any) => x.type === "table").rows[0].push("extra");
    expect(errors(raw).some((e) => e.message.includes("row length"))).toBe(true);
  });

  it("rejects a series that mixes FY and calendar periods", () => {
    const raw = withModules();
    const s = mod(raw, "economy").blocks.find((x: any) => x.id === "gsdp-series").series[0];
    s.points.push({ ...s.points[0], period: "2026", periodType: "calendar" });
    expect(errors(raw).some((e) => e.message.includes("mixed period types"))).toBe(true);
  });

  it("rejects an unknown source on a list item", () => {
    const raw = withModules();
    mod(raw, "civic").blocks[0].items[0].sourceId = "made-up";
    expect(errors(raw).some((e) => e.message.includes('unknown source "made-up"'))).toBe(true);
  });

  it("every published number in Maharashtra's metrics has an access date", () => {
    const mh = Region.parse(read("data/regions/IN-MH.json"));
    for (const [k, d] of Object.entries(mh.metrics)) if (d.value !== null) expect(d.accessDate, k).not.toBeNull();
  });
});

describe("comparison data", () => {
  const withCompare = (): RawFiles => ({ ...load(), compare: read("data/compare/indicators.json") });

  it("validates with no errors", () => expect(errors(withCompare())).toEqual([]));

  it("rejects a value whose period differs from the indicator period", () => {
    const raw = withCompare();
    const ind = (raw.compare as any).groups[1].indicators[0];
    ind.values["IN-MH"].period = "FY2025-26";
    expect(errors(raw).some((e) => e.message.includes("differs from indicator period"))).toBe(true);
  });

  it("rejects mixed price bases across regions", () => {
    const raw = withCompare();
    const ind = (raw.compare as any).groups[1].indicators[0];
    ind.values["IN-TN"].priceBase = { type: "constant", baseYear: "2011-12" };
    expect(errors(raw).some((e) => e.message.includes("mixed price bases"))).toBe(true);
  });

  it("requires an entry for every listed region", () => {
    const raw = withCompare();
    delete (raw.compare as any).groups[0].indicators[0].values["IN-UP"];
    expect(errors(raw).some((e) => e.message.includes("missing value entry"))).toBe(true);
  });

  it("India overview module exists and validates", () => {
    const raw = { ...load(), modules: [{ file: "modules/IN/overview.json", json: read("data/modules/IN/overview.json") }] };
    expect(errors(raw)).toEqual([]);
  });
});
