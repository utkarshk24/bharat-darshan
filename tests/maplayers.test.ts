import { describe, expect, it } from "vitest";
import { getMapWithExtras } from "@/lib/mapLayers";
import { buildScale } from "@/components/map/layers";

describe("extra map layers", () => {
  const { regions, themes } = getMapWithExtras();

  it("adds the comparison indicators the map did not already have", () => {
    expect(themes.length).toBeGreaterThanOrEqual(10);
    expect(themes.map((t) => t.id)).not.toContain("c-population");
    for (const t of themes) expect(t.label?.en).toBeTruthy();
  });

  it("colours every region with a value, all from one period", () => {
    for (const t of themes) {
      const s = buildScale(regions, t.id);
      expect(s.period).toBe(t.period);
      expect(s.offPeriod.size).toBe(0);
    }
  });

  it("keeps the source label for every added value", () => {
    for (const r of regions)
      for (const [k, dp] of Object.entries(r.mapMetrics))
        if (k.startsWith("c-") && dp?.sourceId) expect(r.sourceLabels[dp.sourceId]).toBeTruthy();
  });
});
