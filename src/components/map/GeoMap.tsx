"use client";
import { forwardRef, useCallback, useEffect, useImperativeHandle, useMemo, useRef, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { geoMercator, geoPath, type GeoProjection } from "d3-geo";
import { select } from "d3-selection";
import { zoom as d3zoom, zoomIdentity, type ZoomBehavior, type ZoomTransform } from "d3-zoom";
import "d3-transition";
import { feature, mesh } from "topojson-client";
import type { Topology, GeometryCollection } from "topojson-specification";
import type { Feature, FeatureCollection, Geometry, MultiLineString } from "geojson";
import type { Locale } from "@/i18n/routing";
import type { RegionSummary } from "@/lib/data";
import { pick } from "@/lib/l10n";
import type { Overlay } from "./layers";

export interface BoundaryManifest {
  file: string;
  format: "topojson";
  object: string;
  idProperty: string;
  sourceId: "survey-of-india";
  verified: true;
}

export interface Capital {
  code: string;
  role: string;
  name: { en: string; hi: string; mr: string };
  lon: number;
  lat: number;
}

export interface GeoMapHandle {
  zoomIn(): void;
  zoomOut(): void;
  reset(): void;
  focus(code: string): void;
  svg(): SVGSVGElement | null;
}

type Props = {
  topo: Topology;
  object: string;
  idProperty: string;
  capitals: Capital[];
  regions: RegionSummary[];
  fill: (r: RegionSummary) => string;
  overlays: Set<Overlay>;
  selected: string | null;
  dim?: (r: RegionSummary) => boolean;
  describe: (r: RegionSummary) => string;
  onHover: (r: RegionSummary | null, pt?: { x: number; y: number }) => void;
  onSelect: (r: RegionSummary) => void;
  label: string;
  interactive?: boolean;
};

const W = 800, H = 900;
type F = Feature<Geometry, Record<string, unknown>>;

/**
 * India boundary map drawn from the official Survey of India file (Principle 8).
 * SVG + d3-geo; d3-zoom for pan and zoom. Each State/UT is a focusable button.
 */
export const GeoMap = forwardRef<GeoMapHandle, Props>(function GeoMap(
  { topo, object, idProperty, capitals, regions, fill, overlays, selected, dim, describe, onHover, onSelect, label, interactive = true },
  ref,
) {
  const locale = useLocale() as Locale;
  const t = useTranslations("atlas");
  const svgRef = useRef<SVGSVGElement>(null);
  const zoomRef = useRef<ZoomBehavior<SVGSVGElement, unknown> | null>(null);
  const [tf, setTf] = useState<ZoomTransform>(zoomIdentity);

  const { features, projection, path, outline, inner } = useMemo(() => {
    const obj = topo.objects[object] as GeometryCollection<Record<string, unknown>>;
    const fc = feature(topo, obj) as FeatureCollection<Geometry, Record<string, unknown>>;
    const projection: GeoProjection = geoMercator().fitExtent([[12, 12], [W - 12, H - 12]], fc);
    const path = geoPath(projection);
    const outline = path(mesh(topo, obj, (a, b) => a === b) as MultiLineString) ?? "";
    const inner = path(mesh(topo, obj, (a, b) => a !== b) as MultiLineString) ?? "";
    return { features: fc.features as F[], projection, path, outline, inner };
  }, [topo, object]);

  const byCode = useMemo(() => new Map(regions.map((r) => [r.code, r])), [regions]);
  const shapes = useMemo(
    () =>
      features
        .map((f) => {
          const code = String(f.properties?.[idProperty] ?? "");
          const d = path(f) ?? "";
          const [[x0, y0], [x1, y1]] = path.bounds(f);
          const [cx, cy] = path.centroid(f);
          return { code, d, f, box: { x0, y0, x1, y1 }, cx, cy, r: byCode.get(code) ?? null, disputedLabel: String(f.properties?.label ?? "") };
        })
        // keyboard order follows the region's name
        .sort((a, b) => (a.r && b.r ? pick(a.r.name, locale).localeCompare(pick(b.r.name, locale)) : a.r ? -1 : 1)),
    [features, idProperty, path, byCode, locale],
  );

  // Zoom behaviour
  useEffect(() => {
    if (!svgRef.current || !interactive) return;
    const svg = select(svgRef.current);
    const z = d3zoom<SVGSVGElement, unknown>()
      .scaleExtent([1, 14])
      .translateExtent([[-W * 0.25, -H * 0.25], [W * 1.25, H * 1.25]])
      .filter((ev: Event) => {
        // Wheel zoom only with Ctrl/⌘ so the page still scrolls; pinch/drag always.
        if (ev.type === "wheel") return (ev as WheelEvent).ctrlKey || (ev as WheelEvent).metaKey;
        return !(ev as MouseEvent).button;
      })
      .on("zoom", (ev: { transform: ZoomTransform }) => setTf(ev.transform));
    svg.call(z).on("dblclick.zoom", null);
    zoomRef.current = z;
    return () => {
      svg.on(".zoom", null);
    };
  }, [interactive]);

  const zoomTo = useCallback((next: ZoomTransform) => {
    if (!svgRef.current || !zoomRef.current) return;
    const reduce = typeof window !== "undefined" && window.matchMedia?.("(prefers-reduced-motion: reduce)").matches;
    const sel = select(svgRef.current);
    (reduce ? sel : sel.transition().duration(650)).call(zoomRef.current.transform as never, next);
  }, []);

  useImperativeHandle(ref, () => ({
    zoomIn: () => zoomRef.current && svgRef.current && select(svgRef.current).transition().duration(250).call(zoomRef.current.scaleBy as never, 1.6),
    zoomOut: () => zoomRef.current && svgRef.current && select(svgRef.current).transition().duration(250).call(zoomRef.current.scaleBy as never, 1 / 1.6),
    reset: () => zoomTo(zoomIdentity),
    focus: (code: string) => {
      const s = shapes.find((x) => x.code === code);
      if (!s) return;
      const { x0, y0, x1, y1 } = s.box;
      const k = Math.min(10, 0.8 / Math.max((x1 - x0) / W, (y1 - y0) / H));
      zoomTo(zoomIdentity.translate(W / 2, H / 2).scale(Math.max(1, k)).translate(-(x0 + x1) / 2, -(y0 + y1) / 2));
    },
    svg: () => svgRef.current,
  }), [shapes, zoomTo]);

  const k = tf.k;
  const at = (x: number, y: number) => [tf.applyX(x), tf.applyY(y)] as const;

  // Capitals: one marker per location (Chandigarh serves three regions)
  const capMarks = useMemo(() => {
    const m = new Map<string, { x: number; y: number; items: Capital[] }>();
    for (const c of capitals) {
      const p = projection([c.lon, c.lat]);
      if (!p) continue;
      const key = `${c.lon},${c.lat}`;
      const e = m.get(key) ?? { x: p[0], y: p[1], items: [] };
      e.items.push(c);
      m.set(key, e);
    }
    return [...m.values()];
  }, [capitals, projection]);

  const capScreen = capMarks.map((m) => at(m.x, m.y));
  const fontFamily = "Inter Variable, Noto Sans Devanagari Variable, sans-serif";

  return (
    <svg
      ref={svgRef}
      viewBox={`0 0 ${W} ${H}`}
      className={interactive ? "block h-full w-full touch-none select-none" : "block h-full w-full"}
      role="group"
      aria-label={label}
      style={{ cursor: interactive ? "grab" : undefined }}
    >
      <defs>
        <pattern id="bd-na" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
          <rect width="8" height="8" fill="var(--surface-2)" />
          <line x1="0" y1="0" x2="0" y2="8" stroke="var(--border)" strokeWidth="3" />
        </pattern>
        <pattern id="bd-off" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(135)">
          <rect width="6" height="6" fill="var(--surface)" />
          <line x1="0" y1="0" x2="0" y2="6" stroke="var(--seq-2)" strokeWidth="1.5" />
        </pattern>
        <pattern id="bd-disputed" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
          <rect width="5" height="5" fill="var(--surface)" />
          <line x1="0" y1="0" x2="0" y2="5" stroke="var(--text-muted)" strokeWidth="1.2" />
        </pattern>
        <filter id="bd-glow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="3" result="b" />
          <feMerge>
            <feMergeNode in="b" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>
      <rect width={W} height={H} fill="transparent" />

      <g transform={tf.toString()}>
        {shapes.map((s) => {
          if (!s.r) {
            if (!overlays.has("disputed")) return <path key={s.code + s.d.length} d={s.d} fill="var(--surface-2)" stroke="none" />;
            return (
              <path key={s.code + s.d.length} d={s.d} fill="url(#bd-disputed)" stroke="none">
                <title>{t("disputedArea", { name: s.disputedLabel })}</title>
              </path>
            );
          }
          const r = s.r;
          const isSel = selected === r.code;
          const faded = dim?.(r) ?? false;
          return (
            <path
              key={r.code}
              d={s.d}
              fill={fill(r)}
              opacity={faded ? 0.22 : 1}
              stroke="var(--surface)"
              strokeWidth={0.8}
              vectorEffect="non-scaling-stroke"
              tabIndex={0}
              role="button"
              aria-pressed={isSel}
              aria-label={describe(r)}
              className="cursor-pointer outline-none transition-[opacity] focus-visible:stroke-[var(--focus)] focus-visible:[stroke-width:3]"
              onMouseMove={(e) => {
                const box = svgRef.current?.getBoundingClientRect();
                onHover(r, box ? { x: e.clientX - box.left, y: e.clientY - box.top } : undefined);
              }}
              onMouseLeave={() => onHover(null)}
              onFocus={() => onHover(r)}
              onBlur={() => onHover(null)}
              onClick={() => onSelect(r)}
              onKeyDown={(e) => {
                if (e.key === "Enter" || e.key === " ") {
                  e.preventDefault();
                  onSelect(r);
                }
              }}
            />
          );
        })}
        {/* Inter-State lines and the national boundary, as in the SoI file */}
        <path d={inner} fill="none" stroke="var(--surface)" strokeWidth={0.9} vectorEffect="non-scaling-stroke" pointerEvents="none" />
        <path d={outline} fill="none" stroke="var(--text)" strokeWidth={1.3} vectorEffect="non-scaling-stroke" pointerEvents="none" />
        {selected &&
          shapes
            .filter((s) => s.code === selected)
            .map((s) => (
              <path key="sel" d={s.d} fill="none" stroke="var(--text)" strokeWidth={2.6} vectorEffect="non-scaling-stroke" filter="url(#bd-glow)" pointerEvents="none" />
            ))}
      </g>

      {/* Overlays are drawn in screen space so text and markers keep their size while zooming */}
      {overlays.has("labels") && (
        <g pointerEvents="none" style={{ fontFamily }} aria-hidden>
          {shapes.map((s) => {
            if (!s.r) return null;
            const name = pick(s.r.name, locale);
            const w = (s.box.x1 - s.box.x0) * k;
            const h = (s.box.y1 - s.box.y0) * k;
            const size = 11;
            if (w < name.length * size * 0.56 || h < size * 1.6) return null;
            const [x, y0] = at(s.cx, s.cy);
            // Move the name off a capital marker that sits on it
            const half = (name.length * size * 0.56) / 2;
            const hit = overlays.has("capitals") && capScreen.find((c) => Math.abs(c[0] - x) < half + 4 && Math.abs(c[1] - y0) < size);
            const y = hit ? hit[1] + (hit[1] >= y0 ? -size : size) : y0;
            return (
              <text key={s.code} x={x} y={y} textAnchor="middle" dominantBaseline="middle" fontSize={size} fontWeight={600} fill="var(--text)" stroke="var(--surface)" strokeWidth={3} strokeLinejoin="round" paintOrder="stroke">
                {name}
              </text>
            );
          })}
        </g>
      )}
      {overlays.has("capitals") && (
        <g style={{ fontFamily }}>
          {capMarks.map((m) => {
            const [x, y] = at(m.x, m.y);
            const national = m.items.some((c) => c.role === "national");
            const names = [...new Set(m.items.map((c) => pick(c.name, locale)))].join(" / ");
            const of = m.items
              .map((c) => byCode.get(c.code))
              .filter(Boolean)
              .map((r) => pick(r!.name, locale));
            return (
              <g key={`${m.x},${m.y}`} transform={`translate(${x},${y})`}>
                <title>{t("capitalOf", { name: names, regions: [...new Set(of)].join(", ") })}</title>
                {national ? (
                  <path d="M0,-7 L2,-2 L7,-2 L3,1 L4.5,6.5 L0,3.3 L-4.5,6.5 L-3,1 L-7,-2 L-2,-2 Z" fill="var(--saffron, #e07a1f)" stroke="var(--surface)" strokeWidth={1.2} />
                ) : (
                  <circle r={3} fill="var(--surface)" stroke="var(--text)" strokeWidth={1.6} />
                )}
                {k >= 2.2 && (
                  <text x={6} y={-6} fontSize={10.5} fontWeight={600} fill="var(--text)" stroke="var(--surface)" strokeWidth={2.5} paintOrder="stroke" pointerEvents="none">
                    {names}
                  </text>
                )}
              </g>
            );
          })}
        </g>
      )}
    </svg>
  );
});
