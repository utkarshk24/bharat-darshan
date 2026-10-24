import type { DataPoint } from "@/lib/schema";
import type { ValueKind } from "@/lib/format";
import type { RegionSummary } from "@/lib/data";
import type { MapMetric } from "@/lib/mapMetrics";
import { ZONAL_COLORS, TYPE_COLORS, SEQ_BLUE } from "./mapColors";

/** What the State/UT fill encodes. Categorical themes use labels; data themes use a sourced metric. */
export type ThemeId = "zonal" | "type" | MapMetric;

export interface DataTheme {
  id: MapMetric;
  kind: ValueKind;
  /** Higher values read as "more"; the ramp is always light → dark for low → high. */
  decimals: number;
}

export const DATA_THEMES: DataTheme[] = [
  { id: "population2011", kind: "count", decimals: 0 },
  { id: "density2011", kind: "number", decimals: 0 },
  { id: "literacyRate2011", kind: "percent", decimals: 2 },
  { id: "sexRatio2011", kind: "number", decimals: 0 },
  { id: "forestCoverPct", kind: "percent", decimals: 2 },
  { id: "perCapitaNsdpCurrent", kind: "rupee", decimals: 0 },
];

export const isDataTheme = (t: ThemeId): t is MapMetric => DATA_THEMES.some((d) => d.id === t);

export type Overlay = "labels" | "capitals" | "disputed";
export const OVERLAYS: Overlay[] = ["labels", "capitals", "disputed"];

/** Layers we will add only once official, sourced data is in place (shown as "planned"). */
export const PLANNED = ["districts", "rivers", "protected", "transport", "heritage", "hazards", "timeline"] as const;

export interface Scale {
  /** Period every coloured value shares (period hygiene: one period per map). */
  period: string | null;
  breaks: number[]; // upper bounds of classes 0..n-2
  colors: string[];
  /** Regions with a value for a different period: shown but not coloured. */
  offPeriod: Set<string>;
}

/**
 * Five-class quantile scale over the regions that share the most common period.
 * Regions with no figure, or a figure for another period, are not coloured.
 */
export function buildScale(regions: RegionSummary[], metric: MapMetric): Scale {
  const counts = new Map<string, number>();
  for (const r of regions) {
    const dp = r.mapMetrics[metric];
    if (dp) counts.set(dp.period, (counts.get(dp.period) ?? 0) + 1);
  }
  const period = [...counts.entries()].sort((a, b) => b[1] - a[1] || b[0].localeCompare(a[0]))[0]?.[0] ?? null;
  const vals: number[] = [];
  const offPeriod = new Set<string>();
  for (const r of regions) {
    const dp = r.mapMetrics[metric];
    if (!dp) continue;
    if (dp.period === period) vals.push(dp.value as number);
    else offPeriod.add(r.code);
  }
  vals.sort((a, b) => a - b);
  const n = Math.min(5, vals.length);
  const breaks: number[] = [];
  for (let i = 1; i < n; i++) breaks.push(vals[Math.floor((i * vals.length) / n) - 1]);
  const colors = n === 5 ? SEQ_BLUE : SEQ_BLUE.slice(5 - n);
  return { period, breaks, colors, offPeriod };
}

export function classOf(scale: Scale, v: number): number {
  let i = 0;
  while (i < scale.breaks.length && v > scale.breaks[i]) i++;
  return i;
}

export const NA_FILL = "url(#bd-na)";
export const OFF_FILL = "url(#bd-off)";

export function fillForTheme(r: RegionSummary, theme: ThemeId, scale: Scale | null): string {
  if (theme === "zonal") return ZONAL_COLORS[r.zonalCouncil ?? "islands"];
  if (theme === "type") return TYPE_COLORS[r.type];
  const dp: DataPoint | undefined = r.mapMetrics[theme];
  if (!dp || !scale) return NA_FILL;
  if (scale.offPeriod.has(r.code)) return OFF_FILL;
  return scale.colors[classOf(scale, dp.value as number)];
}
