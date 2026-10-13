"use client";
import { useMemo, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { Download, Table2, LineChart as LineIcon } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { Block, DataPoint } from "@/lib/schema";
import { formatPeriod, formatIndianNumber } from "@/lib/format";
import { cn } from "@/lib/cn";
import { formatValue } from "../StatCard";
import { TrendBadge } from "../TrendBadge";
import { SourceInfo } from "../SourceInfo";
import { Digits } from "../Num";

type Series = Extract<Block, { type: "series" }>;
// Colour-blind-safe pair (Okabe–Ito blue / vermillion), plus dashes so colour isn't the only cue.
const COLORS = ["#0072B2", "#D55E00", "#009E73", "#CC79A7"];
const DASH = ["", "6 4", "2 3", "8 3 2 3"];

/** Time-series chart with range selector, latest/previous/change summary, table view and CSV download (Section 8). */
export function SeriesChart({ block, labels, sourceLabel, note, hideSummary }: { block: Series; labels: string[]; sourceLabel: string | null; note?: string; hideSummary?: boolean }) {
  const t = useTranslations("common");
  const locale = useLocale() as Locale;
  const [range, setRange] = useState<number | "all">(10);
  const [view, setView] = useState<"chart" | "table">("chart");

  const periods = useMemo(() => {
    const set = new Set<string>();
    block.series.forEach((s) => s.points.forEach((p) => set.add(p.period)));
    return [...set].sort();
  }, [block]);
  const shown = range === "all" ? periods : periods.slice(-range);
  const rows = shown.map((period) => {
    const row: Record<string, string | number | null> = { period: formatPeriod(period, locale) };
    block.series.forEach((s) => {
      const p = s.points.find((x) => x.period === period);
      row[s.id] = typeof p?.value === "number" ? p.value : null;
    });
    return row;
  });

  const first = block.series[0];
  const pts = first.points.filter((p) => typeof p.value === "number").sort((a, b) => a.period.localeCompare(b.period));
  const latest = pts.at(-1);
  const prev = pts.at(-2);
  const fmt = (v: number) => formatValue({ ...(latest as DataPoint), value: v }, block.kind, locale) ?? "";
  const delta = latest && prev ? (latest.value as number) - (prev.value as number) : null;

  const csv = () => {
    const head = ["period", ...block.series.map((s, i) => `${labels[i]} (${s.points[0].unit})`)];
    const lines = periods.map((p) => [p, ...block.series.map((s) => s.points.find((x) => x.period === p)?.value ?? "")].join(","));
    const blob = new Blob([[head.join(","), ...lines].join("\n")], { type: "text/csv;charset=utf-8" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `${block.id}.csv`;
    a.click();
    URL.revokeObjectURL(a.href);
  };

  return (
    <div className="rounded-2xl border border-border bg-surface p-4">
      {latest && !hideSummary && (
        <dl className="mb-4 grid grid-cols-2 gap-3 sm:grid-cols-4">
          <div>
            <dt className="text-xs text-muted">{t("latest")} · <Digits>{formatPeriod(latest.period, locale)}</Digits></dt>
            <dd className="text-xl font-semibold tabular-nums"><Digits>{fmt(latest.value as number)}</Digits></dd>
          </div>
          {prev && (
            <div>
              <dt className="text-xs text-muted">{t("previous")} · <Digits>{formatPeriod(prev.period, locale)}</Digits></dt>
              <dd className="text-xl font-semibold tabular-nums"><Digits>{fmt(prev.value as number)}</Digits></dd>
            </div>
          )}
          {delta !== null && prev && (
            <div>
              <dt className="text-xs text-muted">{t("change")}</dt>
              <dd className="flex flex-col">
                <span className="tabular-nums"><Digits>{(delta >= 0 ? "+" : "−") + fmt(Math.abs(delta))}</Digits></span>
                <TrendBadge
                  delta={block.kind === "percent" ? +delta.toFixed(2) : +((delta / (prev.value as number)) * 100).toFixed(1)}
                  unit={block.kind === "percent" ? " pp" : "%"}
                  polarity={block.polarity}
                />
              </dd>
            </div>
          )}
        </dl>
      )}

      <div className="mb-3 flex flex-wrap items-center gap-2 text-sm">
        <div role="radiogroup" aria-label={t("range")} className="flex overflow-hidden rounded-md border border-border">
          {([5, 10, "all"] as const).map((r) => (
            <button
              key={String(r)}
              role="radio"
              aria-checked={range === r}
              onClick={() => setRange(r)}
              className={cn("px-2.5 py-1", range === r ? "bg-navy text-bg font-semibold" : "hover:bg-surface-2")}
            >
              {r === "all" ? t("all") : <Digits>{t("years", { n: r })}</Digits>}
            </button>
          ))}
        </div>
        <button type="button" onClick={() => setView(view === "chart" ? "table" : "chart")} className="inline-flex items-center gap-1 rounded-md border border-border px-2.5 py-1 hover:bg-surface-2">
          {view === "chart" ? <Table2 aria-hidden className="size-4" /> : <LineIcon aria-hidden className="size-4" />}
          {view === "chart" ? t("showTable") : t("showChart")}
        </button>
        <button type="button" onClick={csv} className="inline-flex items-center gap-1 rounded-md border border-border px-2.5 py-1 hover:bg-surface-2">
          <Download aria-hidden className="size-4" /> {t("download")}
        </button>
      </div>

      {view === "chart" ? (
        <div className="h-72 w-full" role="img" aria-label={labels.join(", ")}>
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={rows} margin={{ top: 8, right: 16, bottom: 8, left: 8 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
              <XAxis dataKey="period" tick={{ fontSize: 11, fill: "var(--text-muted)" }} interval="preserveStartEnd" />
              <YAxis
                tick={{ fontSize: 11, fill: "var(--text-muted)" }}
                width={72}
                tickFormatter={(v: number) => (block.kind === "rupeeCrore" ? `${formatIndianNumber(v / 1e5, locale, { maximumFractionDigits: 1 })}L` : formatIndianNumber(v, locale, { maximumFractionDigits: 1 }))}
              />
              <Tooltip
                formatter={(v) => (typeof v === "number" ? fmt(v) : String(v))}
                contentStyle={{ background: "var(--surface)", border: "1px solid var(--border)", color: "var(--text)", fontSize: 12 }}
              />
              {block.series.length > 1 && <Legend wrapperStyle={{ fontSize: 12 }} />}
              {block.series.map((s, i) => (
                <Line key={s.id} type="monotone" dataKey={s.id} name={labels[i]} stroke={COLORS[i % 4]} strokeDasharray={DASH[i % 4]} strokeWidth={2.2} dot={{ r: 2.5 }} connectNulls={false} isAnimationActive={false} />
              ))}
            </LineChart>
          </ResponsiveContainer>
          {block.kind === "rupeeCrore" && <p className="text-right text-[11px] text-muted">L = ₹ lakh crore</p>}
        </div>
      ) : (
        <div className="max-h-80 overflow-auto">
          <table className="w-full text-sm">
            <thead className="sticky top-0 bg-surface-2">
              <tr>
                <th scope="col" className="px-3 py-1.5 text-left">{t("period")}</th>
                {labels.map((l) => <th key={l} scope="col" className="px-3 py-1.5 text-right">{l}</th>)}
              </tr>
            </thead>
            <tbody>
              {rows.map((r) => (
                <tr key={String(r.period)} className="border-t border-border">
                  <th scope="row" className="px-3 py-1.5 text-left font-medium"><Digits>{String(r.period)}</Digits></th>
                  {block.series.map((s) => (
                    <td key={s.id} className="px-3 py-1.5 text-right tabular-nums">
                      {typeof r[s.id] === "number" ? <Digits>{fmt(r[s.id] as number)}</Digits> : "—"}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {note && <p className="mt-3 text-sm text-muted">{note}</p>}
      {latest && (
        <div className="mt-2">
          <SourceInfo
            sourceLabel={sourceLabel}
            period={latest.period}
            url={latest.url}
            accessDate={latest.accessDate}
            confidence={latest.confidence}
            revisionStatus={latest.revisionStatus}
            note={latest.note}
          />
        </div>
      )}
    </div>
  );
}
