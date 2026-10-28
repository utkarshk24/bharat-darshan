"use client";
import { useMemo, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { LazyLines } from "./LazyLines";
import { Download, Table2, LineChart as LineIcon } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { Block, DataPoint } from "@/lib/schema";
import { formatPeriod } from "@/lib/format";
import { cn } from "@/lib/cn";
import { formatValue } from "../StatCard";
import { TrendBadge } from "../TrendBadge";
import { SourceInfo } from "../SourceInfo";
import { Digits } from "../Num";
import { usePrintMode } from "../PrintMode";

type Series = Extract<Block, { type: "series" }>;

/** Time-series chart with range selector, latest/previous/change summary, table view and CSV download (Section 8). */
export function SeriesChart({ block, labels, sourceLabel, note, hideSummary }: { block: Series; labels: string[]; sourceLabel: string | null; note?: string; hideSummary?: boolean }) {
  const t = useTranslations("common");
  const locale = useLocale() as Locale;
  const print = usePrintMode();
  const [rangeState, setRange] = useState<number | "all">(10);
  const [viewState, setView] = useState<"chart" | "table">("chart");
  // Printed profiles show every period as a table: no chart library, nothing hidden.
  const range = print ? "all" : rangeState;
  const view = print ? "table" : viewState;

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

      <div className="mb-3 flex flex-wrap items-center gap-2 text-sm print:hidden" hidden={print}>
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
          <LazyLines rows={rows} block={block} labels={labels} fmt={fmt} locale={locale} />
          {block.kind === "rupeeCrore" && <p className="text-right text-[11px] text-muted">{t("lakhCroreAxis")}</p>}
        </div>
      ) : (
        <div className={print ? "" : "max-h-80 overflow-auto"}>
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
