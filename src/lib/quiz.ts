import "server-only";
import { getCompare, getRegions, getSources } from "./data";
import type { Localized, Officeholder } from "./schema";
import type { ValueKind } from "./format";

/**
 * Question bank for the Learn page, generated at build time from sourced data only.
 * Every question carries the source that answers it; nothing is written by hand.
 */

export type QuizKind = "capital" | "gi" | "office" | "data";

export interface QuizSource {
  label: string;
  url: string | null;
  period?: string | null;
  asOf?: string | null;
}

export interface QuizQuestion {
  id: string;
  kind: QuizKind;
  /** Message key under learn.q.* and its parameters (names are Localized, filled client-side). */
  template: "capital" | "gi" | "office" | "dataHigh" | "dataLow" | "dataLarge";
  params: { region?: Localized; item?: Localized; role?: string; indicator?: Localized; period?: string; asOf?: string };
  options: Localized[];
  answer: number;
  /** For data questions: every option's value, so the explanation can show all four. */
  values?: { value: number; unit: string | null }[];
  valueKind?: ValueKind;
  href?: string;
  source: QuizSource;
}

const bare = (l: Localized): Localized => ({ en: l.en, hi: l.hi, mr: l.mr });

/** Small deterministic PRNG so the bank is identical on every build. */
function rng(seed: number) {
  let s = seed >>> 0;
  return () => {
    s = (s + 0x6d2b79f5) >>> 0;
    let t = s;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function pickOthers<T>(pool: T[], n: number, rand: () => number, exclude: (x: T) => boolean): T[] {
  const cand = pool.filter((x) => !exclude(x));
  const out: T[] = [];
  while (out.length < n && cand.length) out.push(cand.splice(Math.floor(rand() * cand.length), 1)[0]);
  return out;
}

/** Distractors with distinct English names, none equal to the answer. */
function distinct(answer: Localized, pool: Localized[], n: number, rand: () => number): Localized[] {
  const seen = new Set([answer.en]);
  const uniq = pool.filter((l) => (seen.has(l.en) ? false : (seen.add(l.en), true)));
  return pickOthers(uniq, n, rand, () => false);
}

/** Put the answer at a deterministic position among the options. */
function place<T>(answer: T, others: T[], rand: () => number): { options: T[]; answer: number } {
  const at = Math.floor(rand() * (others.length + 1));
  const options = [...others];
  options.splice(at, 0, answer);
  return { options, answer: at };
}

export function buildQuizBank(): QuizQuestion[] {
  const rand = rng(20261027);
  const regions = getRegions().filter((r) => r.type !== "country");
  const src = Object.fromEntries(getSources().map((s) => [s.id, s.short]));
  const href = (r: (typeof regions)[number]) => `/${r.type === "state" ? "states" : "uts"}/${r.slug}`;
  const qs: QuizQuestion[] = [];

  // 1. Capitals: the administrative (or sole) capital, against other regions' capitals.
  // Only regions with one administrative capital (J&K, for example, has summer and winter capitals).
  const capOf = (r: (typeof regions)[number]) => {
    const a = r.capitals.filter((c) => c.role === "administrative");
    return a.length === 1 ? a[0] : undefined;
  };
  for (const r of regions) {
    const cap = capOf(r);
    if (!cap) continue;
    // Skip UTs whose capital shares the UT's name (Chandigarh, Puducherry), which would give the answer away.
    if (cap.name.en === r.name.en) continue;
    const others = distinct(cap.name, regions.filter((x) => x.code !== r.code && capOf(x)).map((x) => bare(capOf(x)!.name)), 3, rand);
    if (others.length < 3) continue;
    const { options, answer } = place(bare(cap.name), others, rand);
    qs.push({
      id: `cap-${r.code}`, kind: "capital", template: "capital", params: { region: bare(r.name) },
      options, answer, href: href(r), source: { label: "", url: null },
    });
  }

  // 2. GI products registered for one region only (shared GIs would have several right answers).
  const gis = regions.flatMap((r) =>
    r.giProducts
      .filter((p) => !(p as { sharedWith?: string[] }).sharedWith?.length && !/\(logo\)/i.test(p.name.en) && p.sourceId)
      .map((p) => ({ p, r })),
  );
  const seen = new Set<string>();
  const giPool = gis.filter(({ p }) => (seen.has(p.id) ? false : (seen.add(p.id), true)));
  const giSample = pickOthers(giPool, Math.min(120, giPool.length), rand, () => false);
  for (const { p, r } of giSample) {
    const others = pickOthers(regions, 3, rand, (x) => x.code === r.code).map((x) => bare(x.name));
    const { options, answer } = place(bare(r.name), others, rand);
    qs.push({
      id: `gi-${p.id}`, kind: "gi", template: "gi", params: { item: bare(p.name) }, options, answer, href: `/gi/${p.id}`,
      source: { label: src[p.sourceId!] ?? p.sourceId!, url: p.url, period: p.filingDate ?? null },
    });
  }

  // 3. Officeholders: Chief Ministers and Governors/LGs whose card cites an official source.
  const offices: { o: Officeholder; r: (typeof regions)[number] }[] = [];
  for (const r of regions) for (const o of [r.government.headOfState, r.government.headOfGovernment]) if (o?.name && o.confidence === "Official" && o.asOf) offices.push({ o, r });
  for (const { o, r } of offices) {
    const same = offices.filter((x) => x.o.role === o.role && x.r.code !== r.code).map((x) => bare(x.o.name!));
    const others = distinct(o.name!, same, 3, rand);
    if (others.length < 3) continue;
    const { options, answer } = place(bare(o.name!), others, rand);
    qs.push({
      id: `office-${r.code}-${o.role}`, kind: "office", template: "office", params: { region: bare(r.name), role: o.role, asOf: o.asOf! },
      options, answer, href: `${href(r)}/government`,
      source: { label: src[o.sourceId ?? ""] ?? o.sourceId ?? "", url: o.url, asOf: o.asOf },
    });
  }

  // 4. Data: "Among these four, which had the highest …?" from the comparison indicators (one period per indicator).
  const cmp = getCompare();
  if (cmp) {
    const byCode = Object.fromEntries(regions.map((r) => [r.code, r]));
    for (const g of cmp.groups)
      for (const ind of g.indicators) {
        const withVal = cmp.regions.filter((c) => typeof ind.values[c]?.value === "number" && byCode[c]);
        if (withVal.length < 4) continue;
        const rounds = withVal.length >= 20 ? 4 : withVal.length >= 8 ? 2 : 1;
        for (let k = 0; k < rounds; k++) {
          const four = pickOthers(withVal, 4, rand, () => false);
          const vals = four.map((c) => ind.values[c]!.value as number);
          if (new Set(vals).size < 4) continue; // ties would make two answers right
          const low = ind.polarity === "lower-is-better";
          const best = low ? Math.min(...vals) : Math.max(...vals);
          const answer = vals.indexOf(best);
          const first = ind.values[four[0]]!;
          qs.push({
            id: `data-${ind.id}-${k}`, kind: "data",
            template: ind.polarity === "neutral" ? "dataLarge" : low ? "dataLow" : "dataHigh",
            params: { indicator: bare(ind.label), period: ind.period },
            options: four.map((c) => bare(byCode[c].name)), answer,
            values: four.map((c) => ({ value: ind.values[c]!.value as number, unit: ind.values[c]!.unit ?? null })),
            valueKind: ind.kind, href: `/rankings?i=${ind.id}`,
            source: { label: src[first.sourceId ?? ""] ?? first.sourceId ?? "", url: first.url, period: ind.period },
          });
        }
      }
  }
  return qs;
}
