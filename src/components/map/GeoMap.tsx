"use client";
import { useEffect, useMemo, useState } from "react";
import { useLocale } from "next-intl";
import { geoMercator, geoPath } from "d3-geo";
import { feature } from "topojson-client";
import type { Topology, GeometryCollection } from "topojson-specification";
import type { Feature, FeatureCollection, Geometry } from "geojson";
import type { Locale } from "@/i18n/routing";
import type { RegionSummary } from "@/lib/data";
import type { ZonalCouncil } from "@/lib/schema";
import { pick } from "@/lib/l10n";
import { fillFor, type Layer } from "./IndiaMap";

export interface BoundaryManifest {
  file: string;
  format: "topojson";
  object: string;
  idProperty: string;
  sourceId: "survey-of-india";
  verified: true;
}

const W = 600, H = 680;

/**
 * Boundary map. Only ever mounted when public/maps/manifest.json declares a verified
 * Survey of India file (Principle 8). Feature ids must be ISO 3166-2 codes (e.g. IN-MH),
 * read from `idProperty`.
 */
export function GeoMap({ manifest, regions, layer, focus, onActive, onOpen }: {
  manifest: BoundaryManifest;
  regions: RegionSummary[];
  layer: Layer;
  focus: ZonalCouncil | null;
  onActive: (r: RegionSummary | null) => void;
  onOpen: (r: RegionSummary) => void;
}) {
  const locale = useLocale() as Locale;
  const [fc, setFc] = useState<FeatureCollection<Geometry, Record<string, unknown>> | null>(null);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_BASE_PATH ?? ""}/maps/${manifest.file}`)
      .then((r) => r.json())
      .then((topo: Topology) => {
        const obj = topo.objects[manifest.object] as GeometryCollection<Record<string, unknown>>;
        setFc(feature(topo, obj) as FeatureCollection<Geometry, Record<string, unknown>>);
      })
      .catch(() => setFc(null));
  }, [manifest]);

  const byCode = useMemo(() => new Map(regions.map((r) => [r.code, r])), [regions]);
  const path = useMemo(() => (fc ? geoPath(geoMercator().fitSize([W, H], fc)) : null), [fc]);

  if (!fc || !path) return <div className="skeleton aspect-[6/7] w-full rounded-xl" />;

  return (
    <svg viewBox={`0 0 ${W} ${H}`} className="mx-auto w-full max-w-xl" role="group">
      {fc.features.map((f: Feature<Geometry, Record<string, unknown>>, i) => {
        const r = byCode.get(String(f.properties?.[manifest.idProperty] ?? ""));
        if (!r) return <path key={i} d={path(f) ?? ""} fill="var(--surface-2)" stroke="var(--border)" />;
        const dim = focus && r.zonalCouncil !== focus;
        const name = pick(r.name, locale);
        return (
          <a
            key={r.code}
            href="#"
            aria-label={name}
            onClick={(e) => {
              e.preventDefault();
              onOpen(r);
            }}
            onMouseEnter={() => onActive(r)}
            onFocus={() => onActive(r)}
          >
            <title>{name}</title>
            <path d={path(f) ?? ""} fill={fillFor(r, layer)} opacity={dim ? 0.2 : 1} stroke="var(--surface)" strokeWidth={0.8} />
          </a>
        );
      })}
    </svg>
  );
}
