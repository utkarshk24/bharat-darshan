import type { CompareIndicator } from "./schema";

export interface RankedRow {
  code: string;
  value: number;
  /** Standard competition rank: equal values share a rank and the next rank is skipped (1, 2, 2, 4). */
  rank: number;
  tied: boolean;
}

export interface Ranking {
  rows: RankedRow[];
  /** Regions in scope with no published value for the indicator's period. Never ranked, never estimated. */
  missing: string[];
  /** "rank" when the indicator has a favourable direction; "order" for size/structure measures. */
  mode: "rank" | "order";
}

/**
 * Rank the given regions on one compare indicator.
 * - higher-is-better and neutral sort high → low; lower-is-better sorts low → high.
 * - Ranks are computed from the raw published values, not the rounded display values.
 * - Regions whose value is null/absent go to `missing`, in the order given.
 */
export function rankIndicator(ind: CompareIndicator, codes: string[]): Ranking {
  const present: { code: string; value: number }[] = [];
  const missing: string[] = [];
  for (const code of codes) {
    const v = ind.values[code]?.value;
    if (typeof v === "number" && Number.isFinite(v)) present.push({ code, value: v });
    else missing.push(code);
  }
  const asc = ind.polarity === "lower-is-better";
  // Stable sort: ties keep the order the regions were given in.
  present.sort((a, b) => (asc ? a.value - b.value : b.value - a.value));
  const counts = new Map<number, number>();
  for (const p of present) counts.set(p.value, (counts.get(p.value) ?? 0) + 1);
  const rows: RankedRow[] = [];
  present.forEach((p, i) => {
    const prev = rows[i - 1];
    const rank = prev && prev.value === p.value ? prev.rank : i + 1;
    rows.push({ code: p.code, value: p.value, rank, tied: (counts.get(p.value) ?? 0) > 1 });
  });
  return { rows, missing, mode: ind.polarity === "neutral" ? "order" : "rank" };
}

/** Rank of one region on an indicator among `codes`, or null if it has no value. */
export function rankOf(ind: CompareIndicator, codes: string[], code: string): RankedRow | null {
  return rankIndicator(ind, codes).rows.find((r) => r.code === code) ?? null;
}
