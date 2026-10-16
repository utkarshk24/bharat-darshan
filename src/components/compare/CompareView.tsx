"use client";
import { useEffect, useMemo, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { Check, Download, Link2, ArrowUp, ArrowDown } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { CompareFile, CompareIndicator, DataPoint, Localized } from "@/lib/schema";
import { pick } from "@/lib/l10n";
import { formatPeriod } from "@/lib/format";
import { cn } from "@/lib/cn";
import { Link } from "@/i18n/navigation";
import { formatValue } from "../StatCard";
import { SourceInfo } from "../SourceInfo";
import { Digits } from "../Num";
import { SeriesChart } from "../blocks/SeriesChart";

export interface CompareRegion {
  code: string;
  name: Localized;
  href: string;
  accent: string;
}

const MAX = 4;
const MIN = 2;

/** Which selected value is most / least favourable, for indicators with a clear direction. */
function extremes(ind: CompareIndicator, codes: string[]) {
  if (ind.polarity === "neutral") return { best: null, worst: null };
  const vals = codes
    .map((c) => ({ c, v: ind.values[c]?.value }))
    .filter((x): x is { c: string; v: number } => typeof x.v === "number");
  if (vals.length < 2) return { best: null, worst: null };
  const sorted = [...vals].sort((a, b) => a.v - b.v);
  const lo = sorted[0], hi = sorted[sorted.length - 1];
  if (lo.v === hi.v) return { best: null, worst: null };
  return ind.polarity === "higher-is-better" ? { best: hi.c, worst: lo.c } : { best: lo.c, worst: hi.c };
}

export function CompareView({ data, regions, sourceLabels }: { data: CompareFile; regions: CompareRegion[]; sourceLabels: Record<string, string> }) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const [selected, setSelected] = useState<string[]>(data.defaultSelection);
  const [msg, setMsg] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);

  // Read the selection from the address on first load; keep it in sync afterwards.
  useEffect(() => {
    const q = new URLSearchParams(window.location.search);
    if (q.get("group")) setMsg(t("compare.groupPending"));
    // ?ids=MH,KL,TN (short codes, as in the spec) or the older ?r=IN-MH,IN-KL
    const r = q.get("ids") ?? q.get("r");
    if (!r) return;
    const codes = r
      .split(",")
      .map((c) => c.trim().toUpperCase())
      .map((c) => (c.startsWith("IN-") ? c : `IN-${c}`))
      .filter((c) => data.regions.includes(c))
      .slice(0, MAX);
    if (codes.length >= MIN) setSelected(codes);
  }, [data.regions, t]);
  useEffect(() => {
    const url = new URL(window.location.href);
    url.searchParams.set("ids", selected.map((c) => c.slice(3)).join(","));
    url.searchParams.delete("r");
    url.searchParams.delete("group");
    window.history.replaceState(null, "", url);
  }, [selected]);

  const byCode = useMemo(() => Object.fromEntries(regions.map((r) => [r.code, r])), [regions]);
  const name = (c: string) => pick(byCode[c]?.name, locale);

  const toggle = (code: string) => {
    if (selected.includes(code)) {
      if (selected.length <= MIN) return setMsg(t("compare.minimum"));
      setMsg(null);
      return setSelected(selected.filter((c) => c !== code));
    }
    if (selected.length >= MAX) return setMsg(t("compare.limit"));
    setMsg(null);
    // keep the order in which regions are listed
    setSelected(data.regions.filter((c) => selected.includes(c) || c === code));
  };

  const cell = (dp: DataPoint | null | undefined, ind: CompareIndicator) =>
    dp && dp.value !== null ? formatValue(dp, ind.kind, locale) : null;

  const csv = () => {
    const head = [t("compare.indicator"), t("compare.period"), ...selected.map(name), t("compare.india")];
    const lines = data.groups.flatMap((g) =>
      g.indicators.map((ind) => [
        pick(ind.label, locale),
        ind.period,
        ...selected.map((c) => ind.values[c]?.value ?? ""),
        ind.national?.value ?? "",
      ]),
    );
    const esc = (v: unknown) => `"${String(v).replace(/"/g, '""')}"`;
    const blob = new Blob(["﻿" + [head, ...lines].map((r) => r.map(esc).join(",")).join("\n")], { type: "text/csv;charset=utf-8" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `compare-${selected.map((c) => c.slice(3)).join("-")}.csv`;
    a.click();
    URL.revokeObjectURL(a.href);
  };

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(window.location.href);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      /* clipboard unavailable: the address bar already holds the link */
    }
  };

  const trend = {
    ...data.trend,
    series: data.trend.series.filter((s) => selected.includes(s.id)).sort((a, b) => selected.indexOf(a.id) - selected.indexOf(b.id)),
  };

  return (
    <div className="flex min-w-0 flex-col gap-8">
      {/* Region picker */}
      <section aria-labelledby="pick-h" className="rounded-2xl border border-border bg-surface p-4">
        <h2 id="pick-h" className="mb-3 text-sm font-semibold">{t("compare.pick")}</h2>
        <div className="flex flex-wrap gap-2" role="group" aria-labelledby="pick-h">
          {data.regions.map((c) => {
            const on = selected.includes(c);
            return (
              <button
                key={c}
                type="button"
                aria-pressed={on}
                onClick={() => toggle(c)}
                className={cn(
                  "inline-flex items-center gap-1.5 rounded-full border px-3 py-1.5 text-sm",
                  on ? "border-navy bg-navy text-bg font-semibold" : "border-border hover:bg-surface-2",
                )}
              >
                {on && <Check aria-hidden className="size-4" />}
                {name(c)}
              </button>
            );
          })}
        </div>
        <p className="mt-2 min-h-5 text-xs text-muted" aria-live="polite">{msg ?? t("compare.more")}</p>
        <div className="mt-3 flex flex-wrap gap-2 text-sm">
          <button type="button" onClick={csv} className="inline-flex items-center gap-1 rounded-md border border-border px-2.5 py-1 hover:bg-surface-2">
            <Download aria-hidden className="size-4" /> {t("compare.csv")}
          </button>
          <button type="button" onClick={copy} className="inline-flex items-center gap-1 rounded-md border border-border px-2.5 py-1 hover:bg-surface-2">
            <Link2 aria-hidden className="size-4" /> <span aria-live="polite">{copied ? t("compare.copied") : t("compare.link")}</span>
          </button>
        </div>
      </section>

      {/* Table */}
      <div role="region" tabIndex={0} aria-label={t("compare.title")} className="relative w-full max-w-full overflow-x-auto rounded-2xl border border-border bg-surface focus-visible:outline-2 focus-visible:outline-offset-2">
        <table className="w-full min-w-[640px] text-sm">
          <caption className="sr-only">{t("compare.title")}</caption>
          <thead className="bg-surface-2">
            <tr>
              <th scope="col" className="sticky left-0 z-10 bg-surface-2 px-3 py-2 text-left">{t("compare.indicator")}</th>
              {selected.map((c) => (
                <th key={c} scope="col" className="px-3 py-2 text-right" style={{ borderTop: `3px solid ${byCode[c]?.accent}` }}>
                  <Link href={byCode[c]?.href ?? "/"} className="no-underline hover:underline">{name(c)}</Link>
                </th>
              ))}
              <th scope="col" className="px-3 py-2 text-right">{t("compare.india")}</th>
            </tr>
          </thead>
          {data.groups.map((g) => (
            <tbody key={g.id}>
              <tr className="border-t border-border bg-surface-2/60">
                <th scope="colgroup" colSpan={selected.length + 2} className="sticky left-0 px-3 py-1.5 text-left text-xs font-semibold uppercase tracking-wide text-muted">
                  {pick(g.label, locale)}
                </th>
              </tr>
              {g.indicators.map((ind) => {
                const { best, worst } = extremes(ind, selected);
                const nums = selected.map((c) => ind.values[c]?.value).filter((v): v is number => typeof v === "number");
                const max = Math.max(...nums, 0);
                const showBars = nums.length > 0 && nums.every((v) => v >= 0) && max > 0;
                return (
                  <tr key={ind.id} className="border-t border-border align-top">
                    <th scope="row" className="sticky left-0 z-10 max-w-[14rem] bg-surface px-3 py-2 text-left font-medium">
                      {pick(ind.label, locale)}
                      <span className="block text-xs font-normal text-muted"><Digits>{formatPeriod(ind.period, locale)}</Digits></span>
                      {ind.note && <span className="block text-xs font-normal text-muted">{pick(ind.note, locale)}</span>}
                    </th>
                    {selected.map((c) => {
                      const dp = ind.values[c];
                      const txt = cell(dp, ind);
                      const v = dp?.value;
                      return (
                        <td key={c} className="px-3 py-2 text-right">
                          <div className="flex items-center justify-end gap-1">
                            {c === best && (
                              <span title={t("compare.better")} className="text-[var(--good)]">
                                <ArrowUp aria-hidden className="size-3.5" /><span className="sr-only">{t("compare.better")}</span>
                              </span>
                            )}
                            {c === worst && (
                              <span title={t("compare.worse")} className="text-[var(--bad)]">
                                <ArrowDown aria-hidden className="size-3.5" /><span className="sr-only">{t("compare.worse")}</span>
                              </span>
                            )}
                            <span className={cn("tabular-nums", txt ? "font-semibold" : "text-muted")}>
                              {txt ? <Digits>{txt}</Digits> : t("common.notAvailable")}
                            </span>
                          </div>
                          {showBars && typeof v === "number" && (
                            <div aria-hidden className="ml-auto mt-1 h-1.5 w-full max-w-[9rem] rounded-full bg-surface-2">
                              <div className="ml-auto h-1.5 rounded-full" style={{ width: `${Math.max(2, (v / max) * 100)}%`, background: byCode[c]?.accent }} />
                            </div>
                          )}
                          {dp && (
                            <div className="mt-0.5">
                              <SourceInfo
                                compact
                                sourceLabel={dp.sourceId ? sourceLabels[dp.sourceId] ?? dp.sourceId : null}
                                period={dp.period}
                                url={dp.url}
                                accessDate={dp.accessDate}
                                confidence={dp.confidence}
                                revisionStatus={dp.revisionStatus}
                                note={dp.note}
                              />
                            </div>
                          )}
                        </td>
                      );
                    })}
                    <td className="px-3 py-2 text-right">
                      <span className="tabular-nums text-muted">
                        {cell(ind.national, ind) ? <Digits>{cell(ind.national, ind)!}</Digits> : "—"}
                      </span>
                      {ind.national && (
                        <div className="mt-0.5">
                          <SourceInfo
                            compact
                            sourceLabel={ind.national.sourceId ? sourceLabels[ind.national.sourceId] ?? ind.national.sourceId : null}
                            period={ind.national.period}
                            url={ind.national.url}
                            accessDate={ind.national.accessDate}
                            confidence={ind.national.confidence}
                            revisionStatus={ind.national.revisionStatus}
                            note={ind.national.note}
                          />
                        </div>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          ))}
        </table>
      </div>
      <p className="-mt-4 text-xs text-muted">{t("compare.legend")} {t("compare.bar")}</p>

      {/* Trend */}
      {trend.series.length > 0 && (
        <section>
          <h2 className="mb-3 text-xl font-semibold">{pick(data.trend.title, locale)}</h2>
          <SeriesChart
            block={trend}
            labels={trend.series.map((s) => pick(s.label, locale))}
            sourceLabel={sourceLabels.mospi ?? "MoSPI"}
            hideSummary
          />
        </section>
      )}
    </div>
  );
}
