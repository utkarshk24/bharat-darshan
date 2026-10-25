import { describe, expect, it } from "vitest";
import { readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import { feature } from "topojson-client";
import { geoBounds } from "d3-geo";
import type { Topology, GeometryCollection } from "topojson-specification";

const root = path.resolve(__dirname, "..");
const read = (p: string) => JSON.parse(readFileSync(path.join(root, p), "utf8"));

describe("India map data", () => {
  const manifest = read("public/maps/manifest.json").boundaries;
  const topo = read(`public/maps/${manifest.file}`) as Topology;
  const fc = feature(topo, topo.objects[manifest.object] as GeometryCollection<Record<string, unknown>>);
  const codes = readdirSync(path.join(root, "data/regions")).filter((f) => f.endsWith(".json")).map((f) => f.replace(".json", "")).filter((c) => c !== "IN");

  it("is a verified Survey of India file", () => {
    expect(manifest.sourceId).toBe("survey-of-india");
    expect(manifest.verified).toBe(true);
  });

  it("has exactly one shape for each of the 36 States and UTs", () => {
    const ids = fc.features.map((f) => String(f.properties?.[manifest.idProperty]));
    for (const c of codes) expect(ids.filter((i) => i === c)).toHaveLength(1);
    expect(ids.filter((i) => i !== "disputed").sort()).toEqual([...codes].sort());
  });

  it("covers India's full extent as depicted by the Survey of India", () => {
    const [[x0, y0], [x1, y1]] = geoBounds(fc);
    // Northernmost point beyond 37° N (J&K / Ladakh incl. PoK, Gilgit-Baltistan, Aksai Chin); east to Arunachal (~97.4° E)
    expect(y1).toBeGreaterThan(37);
    expect(x1).toBeGreaterThan(97.3);
    expect(x0).toBeLessThan(68.3);
    expect(y0).toBeLessThan(7);
  });

  it("places a capital for every region", () => {
    const caps = read("public/maps/capitals.json").capitals as { code: string }[];
    for (const c of codes) expect(caps.some((x) => x.code === c)).toBe(true);
  });
});

describe("district layer", () => {
  const index = read("public/maps/districts/index.json") as {
    vintage: string;
    regions: Record<string, { count: number; profileCount: number | null; status: string; file?: string }>;
  };

  it("covers every region and never draws a district list that differs from the profile", () => {
    expect(Object.keys(index.regions)).toHaveLength(36);
    for (const [code, e] of Object.entries(index.regions)) {
      if (e.profileCount !== null && e.profileCount !== e.count) expect(e.status, code).toBe("outdated");
      if (e.status === "outdated") expect(e.file, code).toBeUndefined();
    }
  });

  it("ships one file per shown region with every district in it", () => {
    for (const [code, e] of Object.entries(index.regions)) {
      if (e.status !== "shown") continue;
      const topo = read(`public/maps/districts/${e.file}`) as Topology;
      const named = (topo.objects.districts as GeometryCollection<{ lgd: number }>).geometries.filter((g) => (g.properties as { lgd: number }).lgd !== 0);
      expect(named.length, code).toBe(e.count);
    }
  });

  it("keeps the areas of J&K under the occupation of Pakistan inside J&K", () => {
    const topo = read("public/maps/districts/IN-JK.topo.json") as Topology;
    const names = (topo.objects.districts as GeometryCollection<{ name: string }>).geometries.map((g) => (g.properties as { name: string }).name);
    expect(names).toEqual(expect.arrayContaining(["Mirpur", "Muzaffarabad"]));
  });
});
