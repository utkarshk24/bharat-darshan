import "server-only";
import { getAllGI, getAllProjects, getGlossary } from "./data";
import { NAV } from "./nav";
import { phoneticKey } from "./translit";
import type { Localized } from "./schema";
import type { SearchItem } from "./search";
import en from "../../messages/en.json";
import hi from "../../messages/hi.json";
import mr from "../../messages/mr.json";

const all = (l: Localized | null | undefined) => (l ? [l.en, l.hi, l.mr].filter(Boolean) : []);
const item = (x: Omit<SearchItem, "phonetic">): SearchItem => ({ ...x, phonetic: x.terms.map(phoneticKey) });
const bare = (l: Localized): Localized => ({ en: l.en, hi: l.hi, mr: l.mr });

/**
 * The part of the search index that is too large to ship with every page:
 * GI products, projects, glossary terms and site pages. Served as /search-index.json and
 * fetched by the search box the first time it is used.
 */
export function buildExtraIndex(): SearchItem[] {
  const items: SearchItem[] = [];
  const seenGi = new Set<string>();
  for (const { product: p, region: r } of getAllGI()) {
    if (seenGi.has(p.id)) continue; // a GI shared by several regions has one page
    seenGi.add(p.id);
    items.push(item({ id: `gi:${p.id}`, kind: "gi", regionCode: r.code, href: `/gi/${p.id}`, label: bare(p.name), context: bare(r.name), terms: all(p.name) }));
  }
  for (const { project: p, region: r } of getAllProjects()) {
    items.push(
      item({
        id: `project:${r.code}:${p.id}`,
        kind: "project",
        regionCode: r.code,
        href: `${r.href}/projects`,
        label: bare(p.name),
        context: bare(r.name),
        terms: all(p.name),
      }),
    );
  }
  for (const g of getGlossary()) {
    const terms = [...all(g.term), ...(g.abbreviation ? [g.abbreviation] : [])];
    items.push(item({ id: `term:${g.id}`, kind: "term", regionCode: "", href: `/glossary#${g.id}`, label: bare(g.term), terms }));
  }
  const nav = { en: en.nav, hi: hi.nav, mr: mr.nav } as Record<"en" | "hi" | "mr", Record<string, string>>;
  for (const n of NAV) {
    if (n.key === "home") continue;
    const label = { en: nav.en[n.key], hi: nav.hi[n.key], mr: nav.mr[n.key] };
    items.push(item({ id: `page:${n.key}`, kind: "page", regionCode: "", href: n.href, label, terms: all(label) }));
  }
  return items;
}
