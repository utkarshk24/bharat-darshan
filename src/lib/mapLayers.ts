import "server-only";
import { getCompare, getSources, getSummaries, type RegionSummary } from "./data";
import type { DataPoint } from "./schema";
import type { DataTheme } from "@/components/map/layers";

/** Comparison indicators the map already shows as built-in layers (Census 2011, ISFR, NSDP). */
const ALREADY = new Set(["population", "density", "sexRatio", "literacy", "forest", "pcnsdp"]);

/**
 * Extra map layers for /map from the comparison indicators: one period per indicator, every value
 * with its source. Added only on the map page so the home page payload stays small.
 */
export function getMapWithExtras(): { regions: RegionSummary[]; themes: DataTheme[] } {
  const base = getSummaries();
  const cmp = getCompare();
  if (!cmp) return { regions: base, themes: [] };
  const short = Object.fromEntries(getSources().map((s) => [s.id, s.short]));
  const inds = cmp.groups.flatMap((g) => g.indicators).filter((i) => !ALREADY.has(i.id));
  const themes: DataTheme[] = inds.map((i) => ({
    id: `c-${i.id}`,
    kind: i.kind,
    decimals: i.kind === "percent" ? 1 : 0,
    label: { en: i.label.en, hi: i.label.hi, mr: i.label.mr },
    period: i.period,
  }));
  const regions = base.map((r) => {
    const mapMetrics = { ...r.mapMetrics };
    const sourceLabels = { ...r.sourceLabels };
    for (const i of inds) {
      const dp = i.values[r.code];
      if (!dp || typeof dp.value !== "number") continue;
      mapMetrics[`c-${i.id}`] = { value: dp.value, unit: dp.unit, period: dp.period, sourceId: dp.sourceId, url: dp.url } as DataPoint;
      if (dp.sourceId) sourceLabels[dp.sourceId] = short[dp.sourceId] ?? dp.sourceId;
    }
    return { ...r, mapMetrics, sourceLabels };
  });
  return { regions, themes };
}
