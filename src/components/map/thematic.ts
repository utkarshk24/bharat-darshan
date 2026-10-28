import type { Topology } from "topojson-specification";

/**
 * Thematic map layers (docs/MAPS.md): official datasets drawn over the Survey of India boundaries.
 * Built by scripts/maps/build_layers.py into public/maps/layers/; each loads only when switched on.
 */
export const THEMATIC = ["rivers", "protected", "transport", "heritage", "hazards"] as const;
export type Thematic = (typeof THEMATIC)[number];

export interface LayerSource {
  publisher: string;
  url: string;
  /** Date the republished copy was taken from the government portal. */
  copy: string;
}

export interface LayerIndex {
  attribution: string;
  built: string;
  sources: Record<string, LayerSource>;
  layers: Record<Thematic, { files: string[]; sources: string[]; counts: Record<string, number | string | string[]> }>;
}

export interface HeritagePoint {
  /** Component name as written by UNESCO (or the property name). */
  n: string;
  lon: number;
  lat: number;
  /** Where the position comes from: UNESCO's own page, or a fallback official file. */
  src: "unesco" | "asi" | "moefcc" | "ir";
}

export interface HeritageSite {
  id: number;
  name: string;
  year: number;
  /** Cultural, Natural or Mixed. */
  cat: "C" | "N" | "M";
  regions: string[];
  url: string;
  points: HeritagePoint[];
}

export interface Quake {
  /** Date as precise as the catalogue gives it: YYYY, YYYY-MM or YYYY-MM-DD. */
  d: string;
  /** Moment magnitude (Mw). */
  m: number;
  /** Depth in km (0 or null when not recorded). */
  z: number | null;
  lon: number;
  lat: number;
}

export interface ThematicData {
  rivers?: Topology;
  protected?: Topology;
  transport?: Topology;
  hazards?: Topology;
  quakes?: Quake[];
  heritage?: HeritageSite[];
}

/** One line of a hover card: plain text, the first one bold. */
export type HoverLines = string[];

const BASE = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export async function loadIndex(): Promise<LayerIndex> {
  return (await fetch(`${BASE}/maps/layers/index.json`)).json();
}

/** Fetch the files of one layer and return the part of ThematicData it fills. */
export async function loadLayer(id: Thematic): Promise<Partial<ThematicData>> {
  const get = (f: string) => fetch(`${BASE}/maps/layers/${f}`).then((r) => {
    if (!r.ok) throw new Error(f);
    return r.json();
  });
  switch (id) {
    case "rivers":
      return { rivers: await get("rivers.topo.json") };
    case "protected":
      return { protected: await get("protected.topo.json") };
    case "transport":
      return { transport: await get("transport.topo.json") };
    case "heritage":
      return { heritage: (await get("heritage.json")).sites };
    case "hazards": {
      const [topo, pts] = await Promise.all([get("hazards.topo.json"), get("hazards-points.json")]);
      return { hazards: topo, quakes: pts.quakes };
    }
  }
}

/** Marker radius for an earthquake of magnitude m (6.0 → 3 px, 8.0 → 9 px): area grows with magnitude. */
export const quakeRadius = (m: number) => 3 + Math.max(0, m - 6) * 3;
