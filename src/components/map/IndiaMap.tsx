"use client";
import { useEffect, useMemo, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { Grid3x3, Table2, Info } from "lucide-react";
import { Link, useRouter } from "@/i18n/navigation";
import type { Locale } from "@/i18n/routing";
import type { RegionSummary } from "@/lib/data";
import type { ZonalCouncil } from "@/lib/schema";
import { pick } from "@/lib/l10n";
import { cn } from "@/lib/cn";
import { ZONAL_COLORS, TYPE_COLORS, inkFor } from "./mapColors";
import { GeoMap, type BoundaryManifest } from "./GeoMap";

export type Layer = "zonal" | "type";
const ZONES: ZonalCouncil[] = ["northern", "central", "eastern", "western", "southern", "north-eastern", "islands"];

export function fillFor(r: RegionSummary, layer: Layer) {
  return layer === "zonal" ? ZONAL_COLORS[r.zonalCouncil ?? "islands"] : TYPE_COLORS[r.type];
}

const hrefFor = (r: RegionSummary) => (r.type === "state" ? `/states/${r.slug}` : `/uts/${r.slug}`);

/**
 * Interactive India map (Sections 6, 9.3).
 * Renders official Survey of India boundaries ONLY when a verified file is installed
 * (public/maps/manifest.json). Otherwise it shows a tile-grid cartogram, which draws no
 * boundaries at all and therefore cannot misrepresent them (Principle 8).
 */
export function IndiaMap({ regions, compact = false }: { regions: RegionSummary[]; compact?: boolean }) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const router = useRouter();
  const [layer, setLayer] = useState<Layer>("zonal");
  const [view, setView] = useState<"map" | "table">("map");
  const [focus, setFocus] = useState<ZonalCouncil | null>(null);
  const [active, setActive] = useState<RegionSummary | null>(null);
  const [manifest, setManifest] = useState<BoundaryManifest | null>(null);

  useEffect(() => {
    fetch("/maps/manifest.json")
      .then((r) => (r.ok ? r.json() : null))
      .then((m) => m?.boundaries?.file && m.boundaries.verified === true && m.boundaries.sourceId === "survey-of-india" && setManifest(m.boundaries))
      .catch(() => {});
  }, []);

  const placed = useMemo(() => regions.filter((r) => r.tile), [regions]);
  const rows = Math.max(...placed.map((r) => r.tile!.row)) + 1;
  const cols = Math.max(...placed.map((r) => r.tile!.col)) + 1;
  const S = 64, G = 6;

  const shortCode = (r: RegionSummary) => r.code.slice(3);

  return (
    <div className="flex flex-col gap-4">
      {/* Controls */}
      <div className="flex flex-wrap items-center gap-3">
        <div role="radiogroup" aria-label={t("home.layer")} className="flex overflow-hidden rounded-md border border-border text-sm">
          {(["zonal", "type"] as const).map((l) => (
            <button
              key={l}
              role="radio"
              aria-checked={layer === l}
              onClick={() => setLayer(l)}
              className={cn("px-3 py-1.5", layer === l ? "bg-navy text-bg font-semibold" : "hover:bg-surface-2")}
            >
              {l === "zonal" ? t("home.layerZonal") : t("home.layerType")}
            </button>
          ))}
        </div>
        <button
          type="button"
          onClick={() => setView(view === "map" ? "table" : "map")}
          className="inline-flex items-center gap-1.5 rounded-md border border-border px-3 py-1.5 text-sm hover:bg-surface-2"
        >
          {view === "map" ? <Table2 aria-hidden className="size-4" /> : <Grid3x3 aria-hidden className="size-4" />}
          {view === "map" ? t("home.viewAsTable") : t("home.viewAsMap")}
        </button>
      </div>

      {/* Region filters */}
      {layer === "zonal" && (
        <div role="group" aria-label={t("home.filterRegion")} className="flex flex-wrap gap-2 text-sm">
          {ZONES.map((z) => (
            <button
              key={z}
              type="button"
              aria-pressed={focus === z}
              onClick={() => setFocus(focus === z ? null : z)}
              className={cn(
                "inline-flex items-center gap-1.5 rounded-full border px-2.5 py-1",
                focus === z ? "border-text font-semibold" : "border-border hover:bg-surface-2",
              )}
            >
              <span aria-hidden className="size-3 rounded-sm" style={{ background: ZONAL_COLORS[z] }} />
              {t(`zonal.${z}`)}
            </button>
          ))}
          <span className="inline-flex items-center gap-1.5 px-1 py-1 text-muted">
            <span aria-hidden className="size-3 rounded-sm border border-dashed border-text" />
            {t("home.utOutline")}
          </span>
        </div>
      )}
      {layer === "type" && (
        <div className="flex flex-wrap gap-3 text-sm">
          {(["state", "ut"] as const).map((k) => (
            <span key={k} className="inline-flex items-center gap-1.5">
              <span aria-hidden className="size-3 rounded-sm" style={{ background: TYPE_COLORS[k] }} />
              {k === "state" ? t("common.states") : t("common.uts")}
            </span>
          ))}
        </div>
      )}

      {view === "map" ? (
        <div className={cn("grid gap-4", !compact && "lg:grid-cols-[1fr_18rem]")}>
          <div className="rounded-2xl border border-border bg-surface p-3">
            {manifest ? (
              <GeoMap manifest={manifest} regions={regions} layer={layer} focus={focus} onActive={setActive} onOpen={(r) => router.push(hrefFor(r))} />
            ) : (
              <svg viewBox={`0 0 ${cols * (S + G)} ${rows * (S + G)}`} className="mx-auto w-full max-w-xl" role="group" aria-label={t("home.mapTitle")}>
                {placed.map((r) => {
                  const x = r.tile!.col * (S + G), y = r.tile!.row * (S + G);
                  const fill = fillFor(r, layer);
                  const dim = focus && r.zonalCouncil !== focus;
                  const name = pick(r.name, locale);
                  return (
                    <a
                      key={r.code}
                      href={`/${locale}${hrefFor(r)}`}
                      onClick={(e) => {
                        e.preventDefault();
                        router.push(hrefFor(r));
                      }}
                      onMouseEnter={() => setActive(r)}
                      onFocus={() => setActive(r)}
                      aria-label={name}
                      className="outline-none [&:focus-visible>rect]:stroke-[var(--focus)] [&:focus-visible>rect]:stroke-[4]"
                    >
                      <title>{name}</title>
                      <rect
                        x={x}
                        y={y}
                        width={S}
                        height={S}
                        rx={10}
                        fill={fill}
                        opacity={dim ? 0.18 : 1}
                        stroke={active?.code === r.code ? "var(--text)" : "transparent"}
                        strokeWidth={3}
                        className="transition-opacity"
                      />
                      {r.type === "ut" && layer === "zonal" && (
                        <rect x={x + 4} y={y + 4} width={S - 8} height={S - 8} rx={7} fill="none" stroke={inkFor(fill)} strokeDasharray="4 3" strokeWidth={1.2} opacity={dim ? 0.2 : 0.7} />
                      )}
                      <text
                        x={x + S / 2}
                        y={y + S / 2 + 6}
                        textAnchor="middle"
                        fontSize="18"
                        fontWeight="700"
                        fill={inkFor(fill)}
                        opacity={dim ? 0.3 : 1}
                        style={{ pointerEvents: "none", fontFamily: "Inter Variable, sans-serif" }}
                      >
                        {shortCode(r)}
                      </text>
                    </a>
                  );
                })}
              </svg>
            )}
            <p className="mt-3 flex gap-1.5 text-xs text-muted">
              <Info aria-hidden className="mt-0.5 size-3.5 shrink-0" />
              <span>
                {t("home.mapNote")} {!manifest && t("home.mapOfficialPending")}
              </span>
            </p>
          </div>

          {!compact && (
            <aside aria-live="polite" className="rounded-2xl border border-border bg-surface p-4 text-sm">
              {active ? (
                <div className="flex flex-col gap-2">
                  <span className="h-1.5 w-12 rounded-full" style={{ background: active.accent }} />
                  <p className="text-lg font-semibold">{pick(active.name, locale)}</p>
                  {active.localName && <p lang={active.localName.lang} className="text-muted">{active.localName.text}</p>}
                  <p>{active.type === "state" ? t("common.state") : t("common.ut")} · {t(`governance.${active.governanceModel}`)}</p>
                  {active.zonalCouncil && <p>{t("common.region")}: {t(`zonal.${active.zonalCouncil}`)}</p>}
                  <p>
                    {t("common.capital")}: {active.capitals.map((c) => pick(c.name, locale)).join(" / ")}
                  </p>
                  <Link href={hrefFor(active)} className="font-medium">{t("common.viewProfile")} →</Link>
                </div>
              ) : (
                <p className="text-muted">{t("home.mapHint")}</p>
              )}
              <p className="mt-4 border-t border-border pt-3 text-xs text-muted">{t("home.layerDataPending")}</p>
            </aside>
          )}
        </div>
      ) : (
        <div className="overflow-x-auto rounded-2xl border border-border bg-surface">
          <table className="w-full text-left text-sm">
            <caption className="sr-only">{t("home.mapTitle")}</caption>
            <thead className="bg-surface-2">
              <tr>
                <th scope="col" className="px-3 py-2">{t("common.region")}</th>
                <th scope="col" className="px-3 py-2">{t("home.filterType")}</th>
                <th scope="col" className="px-3 py-2">{t("home.layerZonal")}</th>
                <th scope="col" className="px-3 py-2">{t("common.capital")}</th>
              </tr>
            </thead>
            <tbody>
              {regions.map((r) => (
                <tr key={r.code} className="border-t border-border">
                  <th scope="row" className="px-3 py-2 font-medium">
                    <Link href={hrefFor(r)}>{pick(r.name, locale)}</Link>
                  </th>
                  <td className="px-3 py-2">{r.type === "state" ? t("common.state") : t("common.ut")}</td>
                  <td className="px-3 py-2">{r.zonalCouncil ? t(`zonal.${r.zonalCouncil}`) : "—"}</td>
                  <td className="px-3 py-2">{r.capitals.map((c) => pick(c.name, locale)).join(" / ")}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
