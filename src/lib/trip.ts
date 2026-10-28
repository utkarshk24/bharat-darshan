import "server-only";
import { getModule, getRegions } from "./data";
import type { Localized } from "./schema";

/**
 * Trip Planner data, assembled from what each profile already says: the tourism section's
 * itineraries and places, the climate section's suggested seasons and the transport section's
 * airports. Nothing is written here; each part links back to its section.
 */

const MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"];

/**
 * Months covered by a season label such as "October to February", "February–March (Navratri)",
 * "May and October" or "April". Returns null when the label names no month.
 * Ranges wrap around the year end (October to February = Oct, Nov, Dec, Jan, Feb). Months are 1–12.
 */
export function monthsOf(label: string): number[] | null {
  const text = label.toLowerCase().replace(/\(.*?\)/g, " ");
  const found = [...text.matchAll(/[a-z]+/g)].map((m) => m[0]).filter((w) => MONTHS.includes(w)).map((w) => MONTHS.indexOf(w) + 1);
  if (found.length === 0) return null;
  if (found.length === 1) return found;
  const isRange = /\bto\b|–|-/.test(text) && !/\band\b/.test(text);
  if (!isRange) return [...new Set(found)].sort((a, b) => a - b);
  const [from, to] = [found[0], found[found.length - 1]];
  const out: number[] = [];
  for (let m = from; ; m = (m % 12) + 1) {
    out.push(m);
    if (m === to || out.length > 12) break;
  }
  return out;
}

/** "d3" → 3, "d2m" → 2, "d3p" → 3; null when the id carries no number. */
export const daysOf = (id: string): number | null => {
  const m = /\d+/.exec(id);
  return m ? Number(m[0]) : null;
};

export interface TripItinerary { id: string; days: number | null; label: Localized; detail: Localized | null }
export interface TripSeason { label: Localized; detail: Localized | null; months: number[] | null }
export interface TripPlace { name: Localized; meta: Localized | null }

export interface TripData {
  code: string;
  href: string;
  name: Localized;
  itineraries: TripItinerary[];
  seasons: TripSeason[];
  places: TripPlace[];
  airports: Localized[];
  /** Date the tourism section was last checked. */
  asOf: string | null;
}

type Block = { id?: string; type: string; items?: Array<Record<string, unknown>> };
const bare = (l: unknown): Localized | null => {
  const x = l as Localized | undefined;
  return x?.en ? { en: x.en, hi: x.hi, mr: x.mr } : null;
};
const listItems = (blocks: Block[] | undefined, id: string) => blocks?.find((b) => b.id === id && b.type === "list")?.items ?? [];

export function buildTrip(code: string): TripData | null {
  const r = getRegions().find((x) => x.code === code);
  if (!r) return null;
  const tourism = getModule(code, "tourism") as { blocks: Block[]; asOf?: string } | null;
  const climate = getModule(code, "climate") as { blocks: Block[] } | null;
  const transport = getModule(code, "transport") as { blocks: Block[] } | null;

  const itineraries = listItems(tourism?.blocks, "itin")
    .map((it) => ({ id: String(it.id), days: daysOf(String(it.id)), label: bare(it.name)!, detail: bare(it.detail) }))
    .filter((it) => it.label);
  const seasons = listItems(climate?.blocks, "best")
    .map((it) => ({ label: bare(it.name)!, detail: bare(it.detail), months: monthsOf(bare(it.name)?.en ?? "") }))
    .filter((s) => s.label);
  const places = listItems(tourism?.blocks, "places")
    .map((it) => ({ name: bare(it.name)!, meta: bare(it.meta) }))
    .filter((p) => p.name);
  const airports = listItems(transport?.blocks, "airports").map((it) => bare(it.name)).filter((x): x is Localized => !!x);

  if (!itineraries.length && !seasons.length && !places.length) return null;
  return {
    code,
    href: `/${r.type === "state" ? "states" : "uts"}/${r.slug}`,
    name: bare(r.name)!,
    itineraries,
    seasons,
    places,
    airports,
    asOf: tourism?.asOf ?? null,
  };
}

/** Regions the planner can offer, with what each has (for the picker). */
export function tripRegions() {
  return getRegions()
    .filter((r) => r.type !== "country")
    .map((r) => ({ code: r.code, name: bare(r.name)!, type: r.type as "state" | "ut", data: buildTrip(r.code) }))
    .filter((x) => x.data)
    .map(({ code, name, type, data }) => ({ code, name, type, itineraries: data!.itineraries.length }));
}
