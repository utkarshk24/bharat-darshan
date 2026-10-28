"use client";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { Download, Info, Layers, Link2, Map as MapIcon, Minus, Plus, RotateCcw, Search, Table2, X } from "lucide-react";
import type { Topology } from "topojson-specification";
import { Link } from "@/i18n/navigation";
import type { Locale } from "@/i18n/routing";
import type { RegionSummary } from "@/lib/data";
import type { ZonalCouncil } from "@/lib/schema";
import { pick } from "@/lib/l10n";
import { cn } from "@/lib/cn";
import { formatDate, formatPeriod, formatValue, toDevanagariDigits } from "@/lib/format";
import { usePreferences } from "@/components/Preferences";
import { ZONAL_COLORS, TYPE_COLORS } from "./mapColors";
import dynamic from "next/dynamic";
import type { BoundaryManifest, Capital, GeoMapHandle } from "./GeoMap";

// d3 and the boundary renderer load only when the map is about to be seen
const GeoMap = dynamic(() => import("./GeoMap").then((m) => m.GeoMap), { ssr: false, loading: () => <div className="skeleton h-full w-full" /> });
import { DATA_THEMES, OVERLAYS, PLANNED, buildScale, fillForTheme, type DataTheme, type Overlay, type ThemeId } from "./layers";
import { exportPng } from "./exportPng";
import { FIRST_YEAR, LAST_YEAR, eventYears, eventsIn, periodAt } from "./formation";
import { THEMATIC, loadIndex, loadLayer, type HoverLines, type LayerIndex, type Thematic, type ThematicData } from "./thematic";

const ZONES: ZonalCouncil[] = ["northern", "central", "eastern", "western", "southern", "north-eastern", "islands"];
const hrefFor = (r: RegionSummary) => (r.type === "state" ? `/states/${r.slug}` : `/uts/${r.slug}`);
const BASE = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
/** On large screens the info card floats over the map's left side (w-72 + margin). */
const panelPad = () => (typeof window !== "undefined" && window.matchMedia("(min-width: 1024px)").matches ? 304 : 0);

interface DistrictIndex {
  vintage: string;
  regions: Record<string, { count: number; profileCount: number | null; status: "shown" | "outdated"; file?: string }>;
}

interface Loaded {
  manifest: BoundaryManifest;
  topo: Topology;
  capitals: Capital[];
  missingCapitals: string[];
}

/** Read #theme=…&on=labels,capitals&r=IN-MH from the URL (shareable views). */
function readHash(themes: ThemeId[]) {
  if (typeof window === "undefined") return {};
  const p = new URLSearchParams(window.location.hash.slice(1));
  const theme = p.get("theme") as ThemeId | null;
  const on = p.get("on");
  return {
    theme: theme && themes.includes(theme) ? theme : undefined,
    overlays: on !== null ? new Set(on.split(",").filter((o): o is Overlay | Thematic => OVERLAYS.includes(o as Overlay) || THEMATIC.includes(o as Thematic))) : undefined,
    region: p.get("r") ?? undefined,
    year: Number(p.get("y")) || undefined,
  };
}

/**
 * The India Atlas (Sections 6, 9.3): official Survey of India boundaries, data layers
 * from sourced figures, capitals, search, zoom, share and export. `compact` is the
 * home-page version without the side panel.
 */
export function IndiaMap({ regions, compact = false, extraThemes = [] }: { regions: RegionSummary[]; compact?: boolean; extraThemes?: DataTheme[] }) {
  const t = useTranslations();
  const ta = useTranslations("atlas");
  const locale = useLocale() as Locale;
  const { digits } = usePreferences();
  const dg = useCallback((s: string) => (digits === "devanagari" ? toDevanagariDigits(s) : s), [digits]);
  const mapRef = useRef<GeoMapHandle>(null);
  const allData = useMemo(() => [...DATA_THEMES, ...extraThemes], [extraThemes]);
  const THEMES: ThemeId[] = useMemo(() => ["zonal", "type", "plain", "formation", ...allData.map((d) => d.id)], [allData]);
  const themeLabel = useCallback(
    (id: ThemeId) => {
      const x = allData.find((d) => d.id === id);
      return x?.label ? pick(x.label, locale) : ta(`theme.${id}`);
    },
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [allData, locale],
  );
  const wrapRef = useRef<HTMLDivElement>(null);

  const [data, setData] = useState<Loaded | null>(null);
  const [failed, setFailed] = useState(false);
  const [theme, setTheme] = useState<ThemeId>("zonal");
  const [year, setYear] = useState<number>(LAST_YEAR);
  const [overlays, setOverlays] = useState<Set<Overlay | Thematic>>(new Set(compact ? ["capitals"] : ["labels", "capitals", "districts", "disputed"]));
  const [layerIndex, setLayerIndex] = useState<LayerIndex | null>(null);
  const [layerData, setLayerData] = useState<ThematicData>({});
  const [layerState, setLayerState] = useState<Partial<Record<Thematic, "loading" | "ready" | "error">>>({});
  const [fHover, setFHover] = useState<{ lines: HoverLines; pt?: { x: number; y: number } } | null>(null);
  const [focusZone, setFocusZone] = useState<ZonalCouncil | null>(null);
  const [selected, setSelected] = useState<string | null>(null);
  const [hover, setHover] = useState<{ r: RegionSummary; pt?: { x: number; y: number } } | null>(null);
  const [dHover, setDHover] = useState<{ name: string; pt?: { x: number; y: number } } | null>(null);
  const [dIndex, setDIndex] = useState<DistrictIndex | null>(null);
  const [dTopo, setDTopo] = useState<{ code: string; topo: Topology } | null>(null);
  const [view, setView] = useState<"map" | "table">("map");
  const [query, setQuery] = useState("");
  const [status, setStatus] = useState("");
  const [restored, setRestored] = useState(compact);

  // The full map loads when it is near the viewport. The home-page version shows a static
  // preview image and loads the interactive map only when the reader reaches for it.
  const [near, setNear] = useState(false);
  const [live, setLive] = useState(!compact);
  useEffect(() => {
    if (compact) return;
    const el = wrapRef.current;
    if (!el || typeof IntersectionObserver === "undefined") return setNear(true);
    const io = new IntersectionObserver((es) => es.some((e) => e.isIntersecting) && (setNear(true), io.disconnect()), { rootMargin: "300px" });
    io.observe(el);
    return () => io.disconnect();
  }, [compact]);
  useEffect(() => {
    if (live && compact) setNear(true);
  }, [live, compact]);

  // Load manifest → boundary file + capitals
  useEffect(() => {
    if (!near) return;
    (async () => {
      try {
        const m = await (await fetch(`${BASE}/maps/manifest.json`)).json();
        const b = m?.boundaries;
        if (!(b?.file && b.verified === true && b.sourceId === "survey-of-india")) throw new Error("unverified");
        const [topo, caps] = await Promise.all([
          fetch(`${BASE}/maps/${b.file}`).then((r) => r.json()),
          m.capitals?.file ? fetch(`${BASE}/maps/${m.capitals.file}`).then((r) => r.json()) : { capitals: [], missing: [] },
        ]);
        setData({ manifest: b, topo, capitals: caps.capitals ?? [], missingCapitals: caps.missing ?? [] });
      } catch {
        setFailed(true);
        setView("table");
      }
    })();
  }, [near]);

  // Districts: the index once, then the selected region's file (LGD boundaries)
  const wantDistricts = !compact && overlays.has("districts");
  useEffect(() => {
    if (!wantDistricts || dIndex) return;
    fetch(`${BASE}/maps/districts/index.json`).then((r) => r.json()).then(setDIndex).catch(() => {});
  }, [wantDistricts, dIndex]);
  useEffect(() => {
    const entry = selected && dIndex?.regions[selected];
    if (!wantDistricts || !entry || !entry.file || dTopo?.code === selected) return;
    let cancelled = false;
    fetch(`${BASE}/maps/districts/${entry.file}`)
      .then((r) => r.json())
      .then((topo: Topology) => !cancelled && setDTopo({ code: selected!, topo }))
      .catch(() => {});
    return () => {
      cancelled = true;
    };
  }, [wantDistricts, selected, dIndex, dTopo]);
  const districtTopo = wantDistricts && dTopo && dTopo.code === selected ? dTopo.topo : null;

  // Thematic layers: the index once, then each layer's files the first time it is switched on
  const activeLayers = useMemo(() => (compact ? [] : THEMATIC.filter((l) => overlays.has(l))), [overlays, compact]);
  useEffect(() => {
    if (!activeLayers.length || layerIndex) return;
    loadIndex().then(setLayerIndex).catch(() => {});
  }, [activeLayers.length, layerIndex]);
  useEffect(() => {
    for (const l of activeLayers) {
      if (layerState[l]) continue;
      setLayerState((s) => ({ ...s, [l]: "loading" }));
      loadLayer(l)
        .then((d) => {
          setLayerData((cur) => ({ ...cur, ...d }));
          setLayerState((s) => ({ ...s, [l]: "ready" }));
        })
        .catch(() => setLayerState((s) => ({ ...s, [l]: "error" })));
    }
  }, [activeLayers, layerState]);
  const thematic = useMemo<ThematicData>(() => {
    const on = new Set(activeLayers);
    return {
      rivers: on.has("rivers") ? layerData.rivers : undefined,
      protected: on.has("protected") ? layerData.protected : undefined,
      transport: on.has("transport") ? layerData.transport : undefined,
      hazards: on.has("hazards") ? layerData.hazards : undefined,
      quakes: on.has("hazards") ? layerData.quakes : undefined,
      heritage: on.has("heritage") ? layerData.heritage : undefined,
    };
  }, [activeLayers, layerData]);

  // Restore a shared view, and follow the link if it is changed in the same tab
  useEffect(() => {
    if (compact) return;
    const apply = () => {
      const h = readHash(THEMES);
      if (h.theme) setTheme(h.theme);
      if (h.overlays) setOverlays(h.overlays);
      if (h.region && regions.some((r) => r.code === h.region)) setSelected(h.region);
      if (h.year && h.year >= FIRST_YEAR && h.year <= LAST_YEAR) setYear(h.year);
    };
    apply();
    setRestored(true);
    window.addEventListener("hashchange", apply);
    return () => window.removeEventListener("hashchange", apply);
  }, [compact, regions, THEMES]);
  useEffect(() => {
    if (!data || !selected || compact) return;
    // The renderer is loaded on demand, so wait for it to mount
    let tries = 0, id = 0;
    const go = () => {
      if (mapRef.current) mapRef.current.focus(selected, panelPad());
      else if (tries++ < 120) id = requestAnimationFrame(go);
    };
    go();
    return () => cancelAnimationFrame(id);
    // only once the map has mounted
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [data]);

  // Keep the URL in step with the view (no history entries)
  useEffect(() => {
    if (compact || !restored || typeof window === "undefined") return;
    const p = new URLSearchParams();
    p.set("theme", theme);
    p.set("on", [...overlays].join(","));
    if (selected) p.set("r", selected);
    if (theme === "formation") p.set("y", String(year));
    window.history.replaceState(null, "", `#${p.toString()}`);
  }, [theme, overlays, selected, compact, restored, year]);

  const byCode = useMemo(() => new Map(regions.map((r) => [r.code, r])), [regions]);
  const dataTheme = allData.find((d) => d.id === theme) ?? null;
  const scale = useMemo(() => (dataTheme ? buildScale(regions, theme) : null), [regions, theme, dataTheme]);
  const fill = useCallback(
    (r: RegionSummary) => {
      if (theme !== "formation") return fillForTheme(r, theme, scale);
      const st = periodAt(r.code, year)?.status;
      return st === "S" ? TYPE_COLORS.state : st === "U" ? TYPE_COLORS.ut : st === "part" ? "url(#bd-na)" : "url(#bd-unlisted)";
    },
    [theme, scale, year],
  );
  /** What a region was in the chosen year, in words (formation theme). */
  const formationText = useCallback(
    (r: RegionSummary): string => {
      const p = periodAt(r.code, year);
      if (!p) return ta("notAvailable");
      const named = p.name ? ` (${pick(p.name, locale)})` : "";
      if (p.status === "S") return ta("formation.state") + named;
      if (p.status === "U") return ta("formation.ut") + named;
      if (p.status === "part") return ta("formation.partOf", { name: pick(p.of!, locale) });
      return ta("formation.unlisted");
    },
    [year, ta, locale],
  );

  const valueText = useCallback(
    (r: RegionSummary): string | null => {
      if (theme === "formation") return `${formationText(r)} · ${dg(String(year))}`;
      if (!dataTheme) return null;
      const dp = r.mapMetrics[dataTheme.id];
      if (!dp) return ta("notAvailable");
      const v = formatValue(dp, dataTheme.kind, locale) ?? ta("notAvailable");
      return dg(`${v} (${formatPeriod(dp.period, locale)})`);
    },
    [dataTheme, locale, ta, dg, theme, formationText, year],
  );
  const describe = useCallback(
    (r: RegionSummary) => {
      const kind = r.type === "state" ? t("common.state") : t("common.ut");
      const v = valueText(r);
      return `${pick(r.name, locale)}, ${kind}${v ? `. ${themeLabel(theme)}: ${v}` : ""}`;
    },
    [locale, t, ta, theme, valueText],
  );

  const select = useCallback((r: RegionSummary) => {
    setSelected((cur) => (cur === r.code ? null : r.code));
    if (!compact) mapRef.current?.focus(r.code, panelPad());
  }, [compact]);

  const toggleOverlay = (o: Overlay | Thematic) => {
    const turningOnLayer = (THEMATIC as readonly string[]).includes(o) && !overlays.has(o);
    // Thematic layers read best on a plain map; the reader can switch the colours back
    if (turningOnLayer && (theme === "zonal" || theme === "type")) setTheme("plain");
    setOverlays((s) => {
      const n = new Set(s);
      if (n.has(o)) n.delete(o);
      else n.add(o);
      return n;
    });
  };

  const matches = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return [];
    return regions
      .filter((r) => [r.name.en, r.name.hi, r.name.mr, r.code, ...r.capitals.map((c) => c.name.en), ...r.capitals.map((c) => pick(c.name, locale))].some((s) => s.toLowerCase().includes(q)))
      .slice(0, 6);
  }, [query, regions, locale]);

  const share = async () => {
    try {
      await navigator.clipboard.writeText(window.location.href);
      setStatus(ta("linkCopied"));
    } catch {
      setStatus(window.location.href);
    }
  };
  const doExport = async () => {
    const svg = mapRef.current?.svg();
    if (!svg) return;
    const title = `${ta("exportTitle")} — ${themeLabel(theme)}`;
    const extra = activeLayers.length && layerIndex
      ? ` · ${[...new Set(activeLayers.flatMap((l) => layerIndex.layers[l].sources.slice(0, 2).map((id) => layerIndex.sources[id].publisher.split(" (")[0].split(",")[0])))].join("; ")}`
      : "";
    await exportPng(svg, { title, attribution: ta("attributionShort") + extra, filename: `bharat-darshan-${theme}.png`, period: scale?.period ? formatPeriod(scale.period, locale) : null });
    setStatus(ta("exported"));
  };

  const sel = selected ? byCode.get(selected) ?? null : null;
  const dim = theme === "zonal" && focusZone ? (r: RegionSummary) => r.zonalCouncil !== focusZone : undefined;

  /* ------------------------------ pieces ------------------------------ */

  const legend = (
    <div className="flex flex-col gap-2 text-sm">
      {theme === "zonal" && (
        <div role="group" aria-label={t("home.filterRegion")} className="flex flex-wrap gap-1.5">
          {ZONES.map((z) => (
            <button
              key={z}
              type="button"
              aria-pressed={focusZone === z}
              onClick={() => setFocusZone(focusZone === z ? null : z)}
              className={cn("inline-flex items-center gap-1.5 rounded-full border px-2.5 py-1", focusZone === z ? "border-text font-semibold" : "border-border hover:bg-surface-2")}
            >
              <span aria-hidden className="size-3 rounded-sm" style={{ background: ZONAL_COLORS[z] }} />
              {t(`zonal.${z}`)}
            </button>
          ))}
        </div>
      )}
      {theme === "type" && (
        <div className="flex flex-wrap gap-3">
          {(["state", "ut"] as const).map((k) => (
            <span key={k} className="inline-flex items-center gap-1.5">
              <span aria-hidden className="size-3 rounded-sm" style={{ background: TYPE_COLORS[k] }} />
              {k === "state" ? t("common.states") : t("common.uts")}
            </span>
          ))}
        </div>
      )}
      {theme === "formation" && (() => {
        const evs = eventsIn(year);
        const prev = [...eventYears].reverse().find((y) => y < year);
        const next = eventYears.find((y) => y > year);
        const sw = (bg: string) => <span aria-hidden className="size-3 rounded-sm border border-border" style={{ background: bg }} />;
        return (
          <div className="flex flex-col gap-2">
            <div className="flex flex-wrap items-center gap-2">
              <label htmlFor="bd-year" className="font-medium">{ta("formation.year")}</label>
              <button type="button" className="rounded-md border border-border px-2 py-0.5 hover:bg-surface-2 disabled:opacity-40" disabled={prev === undefined} onClick={() => prev !== undefined && setYear(prev)} aria-label={ta("formation.prev")}>‹</button>
              <input id="bd-year" type="range" min={FIRST_YEAR} max={LAST_YEAR} step={1} value={year} onChange={(e) => setYear(Number(e.target.value))} className="w-48 accent-[var(--focus)]" aria-valuetext={dg(String(year))} />
              <button type="button" className="rounded-md border border-border px-2 py-0.5 hover:bg-surface-2 disabled:opacity-40" disabled={next === undefined} onClick={() => next !== undefined && setYear(next)} aria-label={ta("formation.next")}>›</button>
              <output htmlFor="bd-year" className="text-lg font-semibold tabular-nums">{dg(String(year))}</output>
            </div>
            <ul className="flex flex-wrap gap-x-3 gap-y-1">
              <li className="inline-flex items-center gap-1.5">{sw(TYPE_COLORS.state)}{ta("formation.state")}</li>
              <li className="inline-flex items-center gap-1.5">{sw(TYPE_COLORS.ut)}{ta("formation.ut")}</li>
              <li className="inline-flex items-center gap-1.5"><svg aria-hidden width="20" height="12"><rect width="20" height="12" rx="2" fill="url(#bd-na-legend)" /><defs><pattern id="bd-na-legend" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="var(--surface-2)" /><line x1="0" y1="0" x2="0" y2="6" stroke="var(--border)" strokeWidth="3" /></pattern></defs></svg>{ta("formation.partShort")}</li>
              <li className="inline-flex items-center gap-1.5"><svg aria-hidden width="20" height="12"><rect width="20" height="12" rx="2" fill="url(#bd-unl-legend)" /><defs><pattern id="bd-unl-legend" width="5" height="5" patternUnits="userSpaceOnUse"><rect width="5" height="5" fill="var(--surface)" /><circle cx="2.5" cy="2.5" r="1" fill="var(--text-muted)" /></pattern></defs></svg>{ta("formation.unlisted")}</li>
            </ul>
            <div aria-live="polite" className="text-sm">
              {evs.length ? (
                <ul className="flex flex-col gap-1.5">
                  {evs.map((e) => (
                    <li key={e.date + e.act}>
                      <span className="font-medium">{dg(e.date.length === 10 ? formatDate(e.date, locale) : e.date)}:</span> {pick(e.what, locale)}{" "}
                      <span className="text-xs text-muted">
                        {ta("source")}: <a href={e.url} target="_blank" rel="noopener noreferrer">{e.act}</a>
                        {e.confidence !== "Official" && <> · {t(`confidence.${e.confidence}` as "confidence.Official")}</>}
                      </span>
                    </li>
                  ))}
                </ul>
              ) : (
                <p className="text-muted">{ta("formation.noChange")}</p>
              )}
            </div>
            <p className="text-xs text-muted">{ta("formation.note")}</p>
          </div>
        );
      })()}
      {dataTheme && scale && (
        <div className="flex flex-col gap-1.5">
          <p className="font-medium">
            {themeLabel(dataTheme.id)}
            {scale.period && <span className="font-normal text-muted"> · {dg(formatPeriod(scale.period, locale))}</span>}
          </p>
          <ol className="flex flex-wrap gap-x-3 gap-y-1">
            {scale.colors.map((c, i) => {
              const lo = i === 0 ? null : scale.breaks[i - 1];
              const hi = scale.breaks[i] ?? null;
              const f = (v: number) => formatValue({ value: v } as never, dataTheme.kind, locale) ?? "";
              const txt = lo === null ? `≤ ${f(hi!)}` : hi === null ? `> ${f(lo)}` : `${f(lo)} – ${f(hi)}`;
              return (
                <li key={i} className="inline-flex items-center gap-1.5">
                  <span aria-hidden className="h-3 w-5 rounded-sm" style={{ background: c }} />
                  <span>{dg(txt)}</span>
                </li>
              );
            })}
            <li className="inline-flex items-center gap-1.5">
              <svg aria-hidden width="20" height="12"><rect width="20" height="12" rx="2" fill="url(#bd-na-legend)" /><defs><pattern id="bd-na-legend" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="var(--surface-2)" /><line x1="0" y1="0" x2="0" y2="6" stroke="var(--border)" strokeWidth="3" /></pattern></defs></svg>
              <span>{ta("notAvailableYet")}</span>
            </li>
            {scale.offPeriod.size > 0 && (
              <li className="inline-flex items-center gap-1.5">
                <svg aria-hidden width="20" height="12"><rect width="20" height="12" rx="2" fill="url(#bd-off-legend)" /><defs><pattern id="bd-off-legend" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(135)"><rect width="5" height="5" fill="var(--surface)" /><line x1="0" y1="0" x2="0" y2="5" stroke="var(--seq-2)" strokeWidth="1.5" /></pattern></defs></svg>
                <span>{ta("otherPeriod")}</span>
              </li>
            )}
          </ol>
          <p className="text-xs text-muted">{ta("quantileNote")}</p>
        </div>
      )}
    </div>
  );

  const themePicker = (
    <fieldset className="flex flex-col gap-1">
      <legend className="mb-1 text-xs font-semibold uppercase tracking-wide text-muted">{ta("colourBy")}</legend>
      {THEMES.map((id) => {
        const first = extraThemes.length > 0 && id === extraThemes[0].id;
        return (
          <div key={id}>
            {first && <p className="mb-1 mt-2 text-xs font-semibold uppercase tracking-wide text-muted">{ta("moreIndicators")}</p>}
            <label className={cn("flex cursor-pointer items-center gap-2 rounded-md px-2 py-1 text-sm", theme === id ? "bg-surface-2 font-semibold" : "hover:bg-surface-2")}>
              <input type="radio" name="bd-theme" value={id} checked={theme === id} onChange={() => setTheme(id)} className="accent-[var(--focus)]" />
              {themeLabel(id)}
            </label>
          </div>
        );
      })}
    </fieldset>
  );

  const overlayPicker = (
    <fieldset className="flex flex-col gap-1">
      <legend className="mb-1 text-xs font-semibold uppercase tracking-wide text-muted">{ta("overlays")}</legend>
      {OVERLAYS.map((o) => (
        <label key={o} className="flex cursor-pointer items-center gap-2 rounded-md px-2 py-1 text-sm hover:bg-surface-2">
          <input type="checkbox" checked={overlays.has(o)} onChange={() => toggleOverlay(o)} className="accent-[var(--focus)]" />
          {ta(`overlay.${o}`)}
        </label>
      ))}
    </fieldset>
  );

  const n = (v: unknown) => dg(new Intl.NumberFormat(`${locale}-IN`).format(Number(v)));
  const summary = (l: Thematic): string | null => {
    const c = layerIndex?.layers[l]?.counts;
    if (!c) return null;
    switch (l) {
      case "rivers":
        return ta("thematicSummary.rivers", { rivers: n(c.rivers), lakes: n(c.lakes), reservoirs: n(c.reservoirs) });
      case "protected":
        return ta("thematicSummary.protected", { np: n(c.nationalParks), ws: n(c.sanctuaries), ramsar: n(c.ramsar) });
      case "transport":
        return ta("thematicSummary.transport", { nh: n(c.nationalHighways) });
      case "heritage":
        return ta("thematicSummary.heritage", { n: n(c.properties) });
      case "hazards":
        return ta("thematicSummary.hazards", { n: n(c.earthquakes), from: dg(String(c.firstYear)), to: dg(String(c.lastYear)) });
    }
  };
  const swatch = (kind: "area" | "hatch" | "line" | "dash" | "dot" | "diamond" | "triangle" | "square" | "circle", color: string) => (
    <svg aria-hidden width="20" height="14" viewBox="0 0 20 14" className="shrink-0">
      {kind === "area" && <rect x="1" y="2" width="18" height="10" rx="2" fill={color} fillOpacity="0.55" stroke={color} />}
      {kind === "hatch" && <><rect x="1" y="2" width="18" height="10" rx="2" fill={color} fillOpacity="0.15" stroke={color} /><path d="M4 12 L10 2 M10 12 L16 2" stroke={color} strokeWidth="1.3" /></>}
      {kind === "dot" && <rect x="1" y="2" width="18" height="10" rx="2" fill={color} fillOpacity="0.45" stroke={color} strokeDasharray="2 1.5" />}
      {kind === "line" && <path d="M1 9 C6 3, 12 12, 19 5" fill="none" stroke={color} strokeWidth="2" />}
      {kind === "dash" && <path d="M1 7 H19" stroke={color} strokeWidth="2" strokeDasharray="4 1.5" />}
      {kind === "diamond" && <path d="M10 1 L16 7 L10 13 L4 7 Z" fill={color} />}
      {kind === "triangle" && <path d="M10 1 L16 12 L4 12 Z" fill={color} />}
      {kind === "square" && <rect x="5" y="2" width="10" height="10" fill={color} />}
      {kind === "circle" && <circle cx="10" cy="7" r="5" fill={color} fillOpacity="0.3" stroke={color} strokeWidth="1.4" />}
    </svg>
  );
  const KEYS: Record<Thematic, [Parameters<typeof swatch>[0], string, string][]> = {
    rivers: [["line", "var(--lyr-water)", "layer.river"], ["area", "var(--lyr-water)", "layer.lakeOrReservoir"]],
    protected: [["area", "var(--lyr-park)", "layer.nationalPark"], ["hatch", "var(--lyr-park)", "layer.sanctuary"], ["dot", "var(--lyr-ramsar)", "layer.ramsar"]],
    transport: [["line", "var(--lyr-road)", "layer.nationalHighway"], ["dash", "var(--lyr-rail)", "layer.railway"]],
    heritage: [["diamond", "var(--lyr-cultural)", "layer.whs.C"], ["triangle", "var(--lyr-natural)", "layer.whs.N"], ["square", "var(--lyr-mixed)", "layer.whs.M"]],
    hazards: [["circle", "var(--lyr-quake)", "layer.quake"], ["hatch", "var(--lyr-flood)", "layer.flood"]],
  };
  const layerLegend = activeLayers.length > 0 && (
    <ul className={cn("flex flex-wrap gap-x-4 gap-y-1 text-sm", theme !== "plain" && "mt-2 border-t border-border pt-2")}>
      {activeLayers.flatMap((l) =>
        KEYS[l].map(([kind, color, key]) => (
          <li key={l + key} className="inline-flex items-center gap-1.5">
            {swatch(kind, color)}
            <span>{ta(key)}</span>
          </li>
        )),
      )}
    </ul>
  );

  const fmtQuakeDate = (d: string) =>
    dg(d.length === 10 ? formatDate(d, locale) : d.length === 7 ? new Intl.DateTimeFormat(`${locale}-IN`, { month: "long", year: "numeric" }).format(new Date(`${d}-15`)) : d);

  const layerPicker = (
    <fieldset className="flex flex-col gap-1">
      <legend className="mb-1 text-xs font-semibold uppercase tracking-wide text-muted">{ta("thematicTitle")}</legend>
      {THEMATIC.map((l) => {
        const on = overlays.has(l);
        const st = layerState[l];
        return (
          <div key={l} className="flex flex-col">
            <label className="flex cursor-pointer items-start gap-2 rounded-md px-2 py-1 text-sm hover:bg-surface-2">
              <input type="checkbox" checked={on} onChange={() => toggleOverlay(l)} className="mt-1 accent-[var(--focus)]" />
              <span>
                {ta(`thematic.${l}`)}
                {on && st === "loading" && <span className="block text-xs text-muted">{ta("layer.loading")}</span>}
                {on && st === "error" && <span className="block text-xs text-[var(--bad)]">{ta("layer.loadError")}</span>}
              </span>
            </label>
            {on && st === "ready" && (
              <div className="mb-1 ml-8 flex flex-col gap-1 text-xs text-muted">
                {summary(l) && <p>{summary(l)}</p>}
                <p>{ta(`thematicNote.${l}`)}</p>
                {l === "heritage" && layerData.heritage && (
                  <details>
                    <summary className="cursor-pointer text-text">{ta("listTitle", { n: n(layerData.heritage.length) })}</summary>
                    <ol className="mt-1 flex max-h-64 flex-col gap-1 overflow-y-auto pr-1">
                      {layerData.heritage.map((h) => (
                        <li key={h.id}>
                          <a href={h.url} target="_blank" rel="noopener noreferrer">{h.name}</a>{" "}
                          <span>({ta(`layer.whs.${h.cat}`)}, {dg(String(h.year))}; {h.regions.map((c) => (byCode.get(c) ? pick(byCode.get(c)!.name, locale) : c)).join(", ")})</span>
                          {h.points.length === 0 && <span className="block">{ta("layer.noPosition")}</span>}
                        </li>
                      ))}
                    </ol>
                  </details>
                )}
                {l === "hazards" && layerData.quakes && (
                  <details>
                    <summary className="cursor-pointer text-text">{ta("listTitle", { n: n(layerData.quakes.length) })}</summary>
                    <ol className="mt-1 flex max-h-64 flex-col gap-0.5 overflow-y-auto pr-1">
                      {[...layerData.quakes].reverse().map((q, i) => (
                        <li key={i}>{fmtQuakeDate(q.d)} — {ta("layer.quakeTitle", { m: dg(q.m.toFixed(1)) })}</li>
                      ))}
                    </ol>
                  </details>
                )}
              </div>
            )}
          </div>
        );
      })}
    </fieldset>
  );

  const layerSources = activeLayers.length > 0 && layerIndex && (
    <div className="mt-2 text-xs text-muted">
      <p className="font-semibold">{ta("layerSources")}</p>
      <ul className="mt-1 flex flex-col gap-0.5">
        {[...new Set(activeLayers.flatMap((l) => layerIndex.layers[l].sources))].map((id) => {
          const src = layerIndex.sources[id];
          return (
            <li key={id}>
              <a href={src.url} target="_blank" rel="noopener noreferrer">{src.publisher}</a> · {ta("copyDated", { date: dg(formatDate(src.copy, locale)) })}
            </li>
          );
        })}
      </ul>
      <p className="mt-1">{ta("layerRepublished")}</p>
    </div>
  );

  const planned = (
    <div className="flex flex-col gap-1">
      <p className="mb-1 text-xs font-semibold uppercase tracking-wide text-muted">{ta("plannedTitle")}</p>
      <ul className="flex flex-col gap-1 text-sm text-muted">
        {PLANNED.map((p) => (
          <li key={p} className="flex items-center justify-between gap-2 px-2">
            <span>{ta(`planned.${p}`)}</span>
            <span className="rounded-full border border-border px-2 py-0.5 text-[11px]">{ta("plannedChip")}</span>
          </li>
        ))}
      </ul>
      <p className="px-2 pt-1 text-xs text-muted">{ta("plannedNote")}</p>
    </div>
  );

  const infoCard = sel ? (
    <div className="flex flex-col gap-2 text-sm">
      <div className="flex items-start justify-between">
        <span className="mt-1 h-1.5 w-12 rounded-full" style={{ background: sel.accent }} />
        {!compact && (
          <button type="button" onClick={() => setSelected(null)} aria-label={ta("close")} title={ta("close")} className="-mr-1 -mt-1 rounded p-1 text-muted hover:bg-surface-2">
            <X aria-hidden className="size-4" />
          </button>
        )}
      </div>
      <p className="text-lg font-semibold">{pick(sel.name, locale)}</p>
      {sel.localName && <p lang={sel.localName.lang} className="text-muted">{sel.localName.text}</p>}
      <p>{sel.type === "state" ? t("common.state") : t("common.ut")} · {t(`governance.${sel.governanceModel}`)}</p>
      {sel.zonalCouncil && <p>{t("common.region")}: {t(`zonal.${sel.zonalCouncil}`)}</p>}
      <p>{t("common.capital")}: {sel.capitals.map((c) => pick(c.name, locale)).join(" / ")}</p>
      {theme === "formation" && (
        <div className="rounded-lg bg-surface-2 p-2">
          <p className="text-xs text-muted">{themeLabel(theme)}</p>
          <p className="font-semibold">{valueText(sel)}</p>
        </div>
      )}
      {dataTheme && (
        <div className="rounded-lg bg-surface-2 p-2">
          <p className="text-xs text-muted">{themeLabel(dataTheme.id)}</p>
          <p className="font-semibold">{valueText(sel)}</p>
          {sel.mapMetrics[dataTheme.id] && (
            <p className="text-xs text-muted">
              {ta("source")}:{" "}
              <a href={sel.mapMetrics[dataTheme.id]!.url ?? undefined} target="_blank" rel="noreferrer" className="underline">
                {(() => {
                  const id = sel.mapMetrics[dataTheme.id]!.sourceId ?? "";
                  return sel.sourceLabels[id] ?? id;
                })()}
              </a>
            </p>
          )}
        </div>
      )}
      {wantDistricts && dIndex?.regions[sel.code] && (() => {
        const e = dIndex.regions[sel.code];
        const date = formatDate(dIndex.vintage, locale);
        return (
          <p className="text-xs text-muted">
            {e.status === "shown"
              ? ta("districtsShown", { count: dg(String(e.count)), date: dg(date) })
              : ta("districtsOutdated", { count: dg(String(e.count)), now: dg(String(e.profileCount)), date: dg(date) })}
          </p>
        );
      })()}
      <Link href={hrefFor(sel)} className="font-medium">{t("common.viewProfile")} →</Link>
    </div>
  ) : (
    <p className="text-sm text-muted">{ta("hint")}</p>
  );

  const table = (
    <div className="overflow-x-auto rounded-2xl border border-border">
      <table className="w-full text-left text-sm">
        <caption className="sr-only">{ta("tableCaption", { theme: themeLabel(theme) })}</caption>
        <thead className="bg-surface-2">
          <tr>
            <th scope="col" className="px-3 py-2">{ta("colRegion")}</th>
            <th scope="col" className="px-3 py-2">{ta("colType")}</th>
            <th scope="col" className="px-3 py-2">{t("common.capital")}</th>
            <th scope="col" className="px-3 py-2">{dataTheme || theme === "formation" ? themeLabel(theme) : t("common.region")}</th>
          </tr>
        </thead>
        <tbody>
          {[...regions].sort((a, b) => pick(a.name, locale).localeCompare(pick(b.name, locale))).map((r) => (
            <tr key={r.code} className="border-t border-border">
              <th scope="row" className="px-3 py-2 font-medium"><Link href={hrefFor(r)}>{pick(r.name, locale)}</Link></th>
              <td className="px-3 py-2">{r.type === "state" ? t("common.state") : t("common.ut")}</td>
              <td className="px-3 py-2">{r.capitals.map((c) => pick(c.name, locale)).join(" / ")}</td>
              <td className="px-3 py-2">{dataTheme || theme === "formation" ? valueText(r) : r.zonalCouncil ? t(`zonal.${r.zonalCouncil}`) : "—"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );

  const tip = fHover && !compact && fHover.pt ? (
    <div
      role="presentation"
      className="pointer-events-none absolute z-10 max-w-[18rem] rounded-lg border border-border bg-surface px-3 py-2 text-sm shadow-lg"
      style={{ left: Math.min(fHover.pt.x + 14, (wrapRef.current?.clientWidth ?? 600) - 220), top: fHover.pt.y + 14 }}
    >
      {fHover.lines.map((line, i) => (
        <p key={i} className={i === 0 ? "font-semibold" : "text-muted"}>{i === 0 ? line : dg(line)}</p>
      ))}
    </div>
  ) : dHover && !compact && dHover.pt && sel ? (
    <div
      role="presentation"
      className="pointer-events-none absolute z-10 max-w-[16rem] rounded-lg border border-border bg-surface px-3 py-2 text-sm shadow-lg"
      style={{ left: Math.min(dHover.pt.x + 14, (wrapRef.current?.clientWidth ?? 600) - 200), top: dHover.pt.y + 14 }}
    >
      <p className="font-semibold" lang="en">{dHover.name}</p>
      <p className="text-muted">{ta("districtOf", { region: pick(sel.name, locale) })}</p>
    </div>
  ) : hover && !compact && hover.pt ? (
    <div
      role="presentation"
      className="pointer-events-none absolute z-10 max-w-[16rem] rounded-lg border border-border bg-surface px-3 py-2 text-sm shadow-lg"
      style={{ left: Math.min(hover.pt.x + 14, (wrapRef.current?.clientWidth ?? 600) - 200), top: hover.pt.y + 14 }}
    >
      <p className="font-semibold">{pick(hover.r.name, locale)}</p>
      <p className="text-muted">{valueText(hover.r) ?? hover.r.capitals.map((c) => pick(c.name, locale)).join(" / ")}</p>
    </div>
  ) : null;

  const btn = "inline-flex size-9 items-center justify-center rounded-md border border-border bg-surface hover:bg-surface-2";

  const mapBox = (
    <div ref={wrapRef} onPointerEnter={() => setLive(true)} onTouchStart={() => setLive(true)} className={cn("relative overflow-hidden rounded-2xl border border-border bg-surface", compact ? "mx-auto aspect-[8/9] w-full max-w-[600px]" : "aspect-[8/9] lg:aspect-auto lg:h-[min(88vh,960px)]")}>
      {compact && !live ? (
        <button type="button" onClick={() => setLive(true)} className="group block h-full w-full" aria-label={ta("explore")}>
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src={`${BASE}/maps/india-preview.svg`} alt={ta("mapLabel")} width={600} height={675} loading="lazy" decoding="async" className="h-full w-full object-contain p-3" />
          <span className="absolute bottom-3 left-1/2 -translate-x-1/2 rounded-full border border-border bg-surface px-3 py-1 text-sm font-medium shadow group-hover:bg-surface-2">{ta("explore")}</span>
        </button>
      ) : data ? (
        <GeoMap
          ref={mapRef}
          topo={data.topo}
          object={data.manifest.object}
          idProperty={data.manifest.idProperty}
          capitals={data.capitals}
          regions={regions}
          fill={fill}
          overlays={overlays}
          selected={selected}
          dim={dim}
          describe={describe}
          onHover={(r, pt) => setHover(r ? { r, pt } : null)}
          districts={districtTopo}
          onDistrictHover={(name, pt) => setDHover(name ? { name, pt } : null)}
          thematic={thematic}
          onFeatureHover={(lines, pt) => setFHover(lines ? { lines, pt } : null)}
          onSelect={select}
          label={ta("mapLabel")}
          interactive={!compact}
        />
      ) : (
        <div className="skeleton h-full w-full" />
      )}
      {tip}
      {!compact && data && (
        <div className="absolute right-2 top-2 flex flex-col gap-1.5">
          <button type="button" className={btn} onClick={() => mapRef.current?.zoomIn()} aria-label={ta("zoomIn")} title={ta("zoomIn")}><Plus aria-hidden className="size-4" /></button>
          <button type="button" className={btn} onClick={() => mapRef.current?.zoomOut()} aria-label={ta("zoomOut")} title={ta("zoomOut")}><Minus aria-hidden className="size-4" /></button>
          <button type="button" className={btn} onClick={() => { mapRef.current?.reset(); setSelected(null); }} aria-label={ta("reset")} title={ta("reset")}><RotateCcw aria-hidden className="size-4" /></button>
          <button type="button" className={btn} onClick={share} aria-label={ta("share")} title={ta("share")}><Link2 aria-hidden className="size-4" /></button>
          <button type="button" className={btn} onClick={doExport} aria-label={ta("export")} title={ta("export")}><Download aria-hidden className="size-4" /></button>
        </div>
      )}
      {!compact && data && <p className="pointer-events-none absolute bottom-2 left-3 rounded bg-surface/80 px-1.5 text-[11px] text-muted">{ta("zoomHint")}</p>}
    </div>
  );

  const attribution = (
    <p className="mt-3 flex gap-1.5 text-xs text-muted">
      <Info aria-hidden className="mt-0.5 size-3.5 shrink-0" />
      <span>
        {failed ? ta("unavailable") : ta("attribution")}
        {data && data.missingCapitals.length > 0 && !compact && <> {ta("capitalsMissing", { list: data.missingCapitals.map((m) => m.slice(6)).join(", ") })}</>}
      </span>
    </p>
  );

  /* ------------------------------ layout ------------------------------ */

  if (compact) {
    return (
      <div className="flex flex-col gap-3">
        <div className="flex flex-wrap items-center gap-2">{legend}</div>
        <div className="grid gap-4 lg:grid-cols-[1fr_18rem]">
          <div>
            {mapBox}
            {attribution}
          </div>
          <aside aria-live="polite" className="rounded-2xl border border-border bg-surface p-4">
            {infoCard}
            <Link href="/map" className="mt-4 inline-flex items-center gap-1.5 border-t border-border pt-3 text-sm font-medium">
              <MapIcon aria-hidden className="size-4" /> {ta("openAtlas")} →
            </Link>
          </aside>
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-4">
      <div className="flex flex-wrap items-center gap-3">
        <div className="relative min-w-[16rem] flex-1">
          <Search aria-hidden className="pointer-events-none absolute left-3 top-1/2 size-4 -translate-y-1/2 text-muted" />
          <input
            type="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && matches[0]) {
                select(matches[0]);
                setQuery("");
              }
            }}
            placeholder={ta("searchPlaceholder")}
            aria-label={ta("searchLabel")}
            aria-controls={matches.length ? "bd-map-search" : undefined}
            className="w-full rounded-md border border-border bg-surface py-2 pl-9 pr-3 text-sm"
          />
          {matches.length > 0 && (
            <ul id="bd-map-search" className="absolute z-20 mt-1 w-full overflow-hidden rounded-md border border-border bg-surface shadow-lg">
              {matches.map((r) => (
                <li key={r.code}>
                  <button type="button" onClick={() => { select(r); setQuery(""); }} className="flex w-full items-center justify-between px-3 py-2 text-left text-sm hover:bg-surface-2">
                    <span>{pick(r.name, locale)}</span>
                    <span className="text-xs text-muted">{r.capitals.map((c) => pick(c.name, locale)).join(" / ")}</span>
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>
        <button
          type="button"
          onClick={() => setView(view === "map" ? "table" : "map")}
          disabled={failed}
          className="inline-flex items-center gap-1.5 rounded-md border border-border px-3 py-2 text-sm hover:bg-surface-2 disabled:opacity-50"
        >
          {view === "map" ? <Table2 aria-hidden className="size-4" /> : <MapIcon aria-hidden className="size-4" />}
          {view === "map" ? t("home.viewAsTable") : t("home.viewAsMap")}
        </button>
      </div>

      <div className="grid gap-4 lg:grid-cols-[15rem_1fr]">
        <details open className="group order-2 h-fit rounded-2xl border border-border bg-surface p-3 lg:order-none [&_summary::-webkit-details-marker]:hidden">
          <summary className="flex cursor-pointer items-center gap-2 text-sm font-semibold">
            <Layers aria-hidden className="size-4" /> {ta("layers")}
          </summary>
          <div className="mt-3 flex flex-col gap-4">
            {overlayPicker}
            {layerPicker}
            {themePicker}
            {planned}
          </div>
        </details>

        <div className="order-1 flex min-w-0 flex-col gap-3 lg:order-none">
          <div className="rounded-2xl border border-border bg-surface p-3">
            {legend}
            {layerLegend}
            {!sel && <p className="mt-2 text-xs text-muted">{ta("hint")}{overlays.has("districts") && ` ${ta("districtsHint")}`}</p>}
          </div>
          {view === "map" ? (
            <div className="relative">
              {mapBox}
              <aside aria-live="polite" hidden={!sel} className="mt-3 rounded-2xl border border-border bg-surface p-4 lg:absolute lg:left-3 lg:top-3 lg:mt-0 lg:w-72 lg:bg-surface/95 lg:shadow-md">
                {infoCard}
              </aside>
            </div>
          ) : (
            table
          )}
          {attribution}
          {layerSources}
        </div>
      </div>
      <p role="status" className="sr-only">{status}</p>
      {status && <p className="text-sm text-muted" aria-hidden>{status}</p>}
    </div>
  );
}

