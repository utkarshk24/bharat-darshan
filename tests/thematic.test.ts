import { readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import { getRegions } from "@/lib/data";
import { EVENTS, LAST_YEAR, PERIODS, periodAt, yearOf } from "@/components/map/formation";
import { THEMATIC, type HeritageSite, type LayerIndex, type Quake } from "@/components/map/thematic";

const dir = join(process.cwd(), "public", "maps", "layers");
const json = (f: string) => JSON.parse(readFileSync(join(dir, f), "utf8"));

describe("thematic map layers", () => {
  const index: LayerIndex = json("index.json");

  it("lists every layer with its files, each source with a publisher, link and copy date", () => {
    for (const l of THEMATIC) {
      const e = index.layers[l];
      expect(e, l).toBeTruthy();
      for (const f of e.files) expect(() => readFileSync(join(dir, f))).not.toThrow();
      for (const s of e.sources) {
        const src = index.sources[s];
        expect(src?.publisher, s).toBeTruthy();
        expect(src.url).toMatch(/^https:\/\//);
        expect(src.copy).toMatch(/^\d{4}-\d{2}-\d{2}$/);
      }
    }
  });

  it("keeps each layer file small enough to load on demand", () => {
    for (const l of THEMATIC) for (const f of index.layers[l].files) expect(readFileSync(join(dir, f)).length, f).toBeLessThan(1_200_000);
  });

  it("has all 44 World Heritage properties, each linked to its UNESCO page, with positions inside India", () => {
    const sites: HeritageSite[] = json("heritage.json").sites;
    expect(sites).toHaveLength(44);
    expect(new Set(sites.map((s) => s.id)).size).toBe(44);
    const codes = new Set(getRegions().map((r) => r.code));
    for (const s of sites) {
      expect(s.url).toBe(`https://whc.unesco.org/en/list/${s.id}/`);
      expect(["C", "N", "M"]).toContain(s.cat);
      for (const c of s.regions) expect(codes.has(c), `${s.name} ${c}`).toBe(true);
      for (const p of s.points) {
        expect(p.lon).toBeGreaterThan(68);
        expect(p.lon).toBeLessThan(98);
        expect(p.lat).toBeGreaterThan(6);
        expect(p.lat).toBeLessThan(37.5);
      }
    }
    // Every property is placed except those the map says it could not place
    expect(sites.filter((s) => !s.points.length).map((s) => s.name)).toEqual(index.layers.heritage.counts.withoutPosition);
  });

  it("lists only magnitude 6+ earthquakes, oldest first, with no duplicates", () => {
    const q: Quake[] = json("hazards-points.json").quakes;
    expect(q.length).toBeGreaterThan(20);
    for (const x of q) expect(x.m).toBeGreaterThanOrEqual(6);
    expect(q.map((x) => x.d)).toEqual([...q.map((x) => x.d)].sort());
    const keys = q.map((x) => `${x.d}|${Math.round(x.lat)}|${Math.round(x.lon)}`);
    expect(new Set(keys).size).toBe(keys.length);
  });
});

describe("State formation timeline", () => {
  const regions = getRegions().filter((r) => r.type !== "country");

  it("covers every State and UT", () => {
    expect(Object.keys(PERIODS).sort()).toEqual(regions.map((r) => r.code).sort());
  });

  it("agrees with today's profiles on which are States and which are Union territories", () => {
    for (const r of regions) expect(periodAt(r.code, LAST_YEAR)?.status, r.code).toBe(r.type === "state" ? "S" : "U");
  });

  it("has periods in date order, and names only where they differ from today's", () => {
    for (const [code, ps] of Object.entries(PERIODS)) {
      const ds = ps.map((p) => p.from);
      expect(ds, code).toEqual([...ds].sort());
      expect(ps.at(-1)!.name, code).toBeUndefined();
      for (const p of ps) if (p.status === "part") expect(p.of?.en, code).toBeTruthy();
    }
  });

  it("cites an Act for every change, and every period change has an event that year", () => {
    const codes = new Set(regions.map((r) => r.code));
    for (const e of EVENTS) {
      expect(e.act).toMatch(/Act/);
      expect(e.url).toMatch(/^https:\/\//);
      for (const c of e.codes) expect(codes.has(c), c).toBe(true);
    }
    for (const [code, ps] of Object.entries(PERIODS))
      for (const p of ps.slice(1)) expect(EVENTS.some((e) => e.date === p.from && e.codes.includes(code)), `${code} ${p.from}`).toBe(true);
    expect(EVENTS.every((e) => yearOf(e.date) >= 1956 && yearOf(e.date) <= LAST_YEAR)).toBe(true);
  });
});
