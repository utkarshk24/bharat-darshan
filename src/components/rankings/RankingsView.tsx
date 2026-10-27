"use client";
import { useEffect, useId, useMemo, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { Download, Link2 } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { CompareFile, CompareIndicator, Localized } from "@/lib/schema";
import { pick } from "@/lib/l10n";
import { formatPeriod } from "@/lib/format";
import { rankIndicator } from "@/lib/rank";
import { cn } from "@/lib/cn";
import { Link } from "@/i18n/navigation";
import { formatValue } from "../StatCard";
import { SourceInfo } from "../SourceInfo";
import { Digits } from "../Num";

export interface RankRegion {
  code: string;
  name: Localized;
  href: string;
  accent: string;
  type: "state" | "ut";
}

type Scope = "all" | "state" | "ut";
const SCOPES: Scope[] = ["all", "state", "ut"];

export function RankingsView({ data, regions, sourceLabels }: { data: CompareFile; regions: RankRegion[]; sourceLabels: Record<string, string> }) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const indicators = useMemo(() => data.groups.flatMap((g) => g.indicators), [data.groups]);
  const [indId, setIndId] = useState<string>("literacy");
  const [scope, setScope] = useState<Scope>("all");
  const [copied, setCopied] = useState(false);
  const selId = useId();

  // Read ?i=&scope= on first load; keep the address in sync afterwards so a ranking can be shared.
  useEffect(() => {
    const q = new URLSearchParams(window.location.search);
    const i = q.get("i");
    if (i && indicators.some((x) => x.id === i)) setIndId(i);
    const s = q.get("scope") as Scope | null;
    if (s && SCOPES.includes(s)) setScope(s);
  }, [indicators]);
  useEffect(() => {
    const url = new URL(window.location.href);
    url.searchParams.set("i", indId);
    if (scope === "all") url.searchParams.delete("scope");
    else url.searchParams.set("scope", scope);
    window.history.replaceState(null, "", url);
  }, [indId, scope]);

  const ind: CompareIndicator = indicators.find((x) => x.id === indId) ?? indicators[0];
  const byCode = useMemo(() => Object.fromEntries(regions.map((r) => [r.code, r])), [regions]);
  const inScope = useMemo(
    () => data.regions.filter((c) => scope === "all" || byCode[c]?.type === scope),
    [data.regions, scope, byCode],
  );
  const ranking = useMemo(() => rankIndicator(ind, inScope), [ind, inScope]);
  const name = (c: string) => pick(byCode[c]?.name, locale);
  const max = Math.max(0, ...ranking.rows.map((r) => r.value));
  const showBars = max > 0 && ranking.rows.every((r) => r.value >= 0);
  const period = formatPeriod(ind.period, locale);
  const nat = ind.national && ind.national.value !== null ? formatValue(ind.national, ind.kind, locale) : null;
  const scopeLabel = (s: Scope) => (s === "all" ? t("common.all") : s === "state" ? t("common.states") : t("common.uts"));
  const order =
    ind.polarity === "higher-is-better" ? t("rankings.higherBetter") : ind.polarity === "lower-is-better" ? t("rankings.lowerBetter") : t("rankings.neutral");
  const rankHead = ranking.mode === "rank" ? t("rankings.rank") : t("rankings.position");

  const csv = () => {
    const head = [rankHead, t("rankings.region"), "ISO 3166-2", pick(ind.label, locale), t("common.period"), t("common.source"), "URL", "Access date"];
    const lines = [
      ...ranking.rows.map((r) => {
        const dp = ind.values[r.code];
        return [r.rank, name(r.code), r.code, r.value, dp?.period ?? ind.period, dp?.sourceId ? sourceLabels[dp.sourceId] ?? dp.sourceId : "", dp?.url ?? "", dp?.accessDate ?? ""];
      }),
      ...ranking.missing.map((c) => ["", name(c), c, t("common.notAvailable"), ind.period, "", "", ""]),
    ];
    const esc = (v: unknown) => `"${String(v).replace(/"/g, '""')}"`;
    const blob = new Blob(["﻿" + [head, ...lines].map((r) => r.map(esc).join(",")).join("\n")], { type: "text/csv;charset=utf-8" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `ranking-${ind.id}-${scope}.csv`;
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

  return (
    <div className="flex min-w-0 flex-col gap-6">
      <section aria-label={t("rankings.controls")} className="flex flex-col gap-4 rounded-2xl border border-border bg-surface p-4 sm:flex-row sm:flex-wrap sm:items-end">
        <div className="flex min-w-0 flex-col gap-1 sm:basis-full">
          <label htmlFor={selId} className="text-sm font-semibold">{t("rankings.indicator")}</label>
          <select
            id={selId}
            value={ind.id}
            onChange={(e) => setIndId(e.target.value)}
            className="w-full min-w-0 rounded-md border border-border bg-bg px-3 py-2 text-sm sm:max-w-xl"
          >
            {data.groups.map((g) => (
              <optgroup key={g.id} label={pick(g.label, locale)}>
                {g.indicators.map((i) => (
                  <option key={i.id} value={i.id}>
                    {pick(i.label, locale)} · {formatPeriod(i.period, locale)}
                  </option>
                ))}
              </optgroup>
            ))}
          </select>
        </div>
        <fieldset className="flex flex-col gap-1">
          <legend className="mb-1 text-sm font-semibold">{t("rankings.scope")}</legend>
          <div className="flex flex-wrap gap-2">
            {SCOPES.map((s) => (
              <button
                key={s}
                type="button"
                aria-pressed={scope === s}
                onClick={() => setScope(s)}
                className={cn(
                  "rounded-full border px-3 py-1.5 text-sm",
                  scope === s ? "border-navy bg-navy font-semibold text-bg" : "border-border hover:bg-surface-2",
                )}
              >
                {scopeLabel(s)}
              </button>
            ))}
          </div>
        </fieldset>
        <div className="flex flex-wrap gap-2 text-sm">
          <button type="button" onClick={csv} className="inline-flex items-center gap-1 rounded-md border border-border px-2.5 py-1.5 hover:bg-surface-2">
            <Download aria-hidden className="size-4" /> {t("rankings.csv")}
          </button>
          <button type="button" onClick={copy} className="inline-flex items-center gap-1 rounded-md border border-border px-2.5 py-1.5 hover:bg-surface-2">
            <Link2 aria-hidden className="size-4" /> <span aria-live="polite">{copied ? t("compare.copied") : t("rankings.link")}</span>
          </button>
        </div>
      </section>

      <div aria-live="polite" className="flex flex-col gap-1 text-sm">
        <h2 className="text-xl font-semibold">
          {pick(ind.label, locale)} <span className="font-normal text-muted">· <Digits>{period}</Digits></span>
        </h2>
        <p>{order}</p>
        <p className="text-muted">
          <Digits>{t("rankings.coverage", { n: ranking.rows.length, total: inScope.length, period })}</Digits>
          {nat && (
            <>
              {" "}
              <Digits>{t("rankings.india", { value: nat })}</Digits>
            </>
          )}
        </p>
        {ind.note && <p className="text-muted">{pick(ind.note, locale)}</p>}
        {scope === "all" && <p className="text-muted">{t("rankings.mixNote")}</p>}
      </div>

      <div role="region" tabIndex={0} aria-label={pick(ind.label, locale)} className="w-full max-w-full overflow-x-auto rounded-2xl border border-border bg-surface focus-visible:outline-2 focus-visible:outline-offset-2">
        <table className="w-full min-w-[520px] text-sm">
          <caption className="sr-only">
            {pick(ind.label, locale)}, {period}. {order}
          </caption>
          <thead className="bg-surface-2">
            <tr>
              <th scope="col" className="w-16 px-3 py-2 text-right">{rankHead}</th>
              <th scope="col" className="px-3 py-2 text-left">{t("rankings.region")}</th>
              <th scope="col" className="px-3 py-2 text-right">{t("rankings.value")}</th>
              <th scope="col" className="px-3 py-2 text-left">{t("common.source")}</th>
            </tr>
          </thead>
          <tbody>
            {ranking.rows.map((r) => {
              const dp = ind.values[r.code]!;
              const reg = byCode[r.code];
              return (
                <tr key={r.code} className="border-t border-border align-top">
                  <td className="px-3 py-2 text-right tabular-nums font-semibold">
                    <Digits>{String(r.rank)}</Digits>
                    {r.tied && <span className="block text-xs font-normal text-muted">{t("rankings.tie")}</span>}
                  </td>
                  <th scope="row" className="px-3 py-2 text-left font-medium">
                    <Link href={reg?.href ?? "/"} className="no-underline hover:underline">{name(r.code)}</Link>
                    <span className="block text-xs font-normal text-muted">{reg?.type === "ut" ? t("common.ut") : t("common.state")}</span>
                  </th>
                  <td className="px-3 py-2 text-right">
                    <span className="tabular-nums font-semibold"><Digits>{formatValue(dp, ind.kind, locale) ?? t("common.notAvailable")}</Digits></span>
                    {showBars && (
                      <div aria-hidden className="ml-auto mt-1 h-1.5 w-full max-w-[10rem] rounded-full bg-surface-2">
                        <div className="ml-auto h-1.5 rounded-full" style={{ width: `${Math.max(2, (r.value / max) * 100)}%`, background: reg?.accent }} />
                      </div>
                    )}
                  </td>
                  <td className="px-3 py-2">
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
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {ranking.missing.length > 0 && (
        <section aria-labelledby="missing-h" className="rounded-2xl border border-dashed border-border p-4 text-sm">
          <h3 id="missing-h" className="font-semibold">
            {t("rankings.missingTitle")} <span className="font-normal text-muted">(<Digits>{String(ranking.missing.length)}</Digits>)</span>
          </h3>
          <p className="mt-1 text-muted">{t("rankings.missingBody")}</p>
          <ul className="mt-3 flex flex-wrap gap-2">
            {ranking.missing.map((c) => (
              <li key={c}>
                <Link href={byCode[c]?.href ?? "/"} className="inline-block rounded-full border border-border px-3 py-1 no-underline hover:bg-surface-2">
                  {name(c)}
                </Link>
              </li>
            ))}
          </ul>
        </section>
      )}
    </div>
  );
}
