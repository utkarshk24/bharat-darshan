import Fuse from "fuse.js";
import type { RegionSummary } from "./data";
import { phoneticKey, hasDevanagari } from "./translit";
import type { Localized } from "./schema";

export interface SearchItem {
  id: string;
  kind: "state" | "ut" | "capital";
  regionCode: string;
  href: string;
  label: Localized;
  context?: Localized;
  terms: string[];
  phonetic: string[];
}

const all = (l: Localized | undefined) => (l ? [l.en, l.hi, l.mr].filter(Boolean) : []);

/** Build the trilingual search index (Section 6/11). Phase 1 covers States/UTs and capitals. */
export function buildIndex(regions: RegionSummary[]): SearchItem[] {
  const items: SearchItem[] = [];
  for (const r of regions) {
    const href = r.type === "state" ? `/states/${r.slug}` : `/uts/${r.slug}`;
    const terms = [...all(r.name), ...(r.formerNames ?? []).flatMap(all), r.code, r.code.slice(3)];
    if (r.localName) terms.push(r.localName.text);
    items.push({ id: r.code, kind: r.type, regionCode: r.code, href, label: r.name, terms, phonetic: terms.map(phoneticKey) });
    for (const c of r.capitals) {
      const ct = [...all(c.name), ...all(c.formerName)];
      if (ct.some((x) => all(r.name).includes(x))) continue; // e.g. Chandigarh UT == its capital
      items.push({
        id: `${r.code}:${c.name.en}`,
        kind: "capital",
        regionCode: r.code,
        href,
        label: c.name,
        context: r.name,
        terms: ct,
        phonetic: ct.map(phoneticKey),
      });
    }
  }
  return items;
}

export function createSearcher(items: SearchItem[]) {
  const raw = new Fuse(items, { keys: ["terms"], threshold: 0.3, ignoreLocation: true, includeScore: true });
  const pho = new Fuse(items, { keys: ["phonetic"], threshold: 0.3, ignoreLocation: true, includeScore: true });
  return (query: string, limit = 8): SearchItem[] => {
    const q = query.trim();
    if (!q) return [];
    const scores = new Map<string, { item: SearchItem; score: number }>();
    const add = (res: { item: SearchItem; score?: number }[]) => {
      for (const r of res) {
        const prev = scores.get(r.item.id);
        const s = r.score ?? 1;
        if (!prev || s < prev.score) scores.set(r.item.id, { item: r.item, score: s });
      }
    };
    add(raw.search(q));
    const pk = phoneticKey(q);
    if (pk) add(pho.search(pk));
    if (hasDevanagari(q)) add(pho.search(phoneticKey(q)));
    return [...scores.values()].sort((a, b) => a.score - b.score).slice(0, limit).map((x) => x.item);
  };
}
