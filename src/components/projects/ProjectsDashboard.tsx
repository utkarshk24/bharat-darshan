"use client";
import { useMemo, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { ExternalLink } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { Localized, Project } from "@/lib/schema";
import { pick, cmp } from "@/lib/l10n";
import { formatDate, formatRupeeCrore } from "@/lib/format";
import { cn } from "@/lib/cn";
import { Link } from "@/i18n/navigation";
import { ConfidenceBadge } from "../ConfidenceBadge";
import { Digits } from "../Num";

export interface ProjectItem {
  project: Project;
  region: { code: string; name: Localized; href: string; accent: string };
}

const ORDER: Project["status"][] = ["Completed", "Under Construction", "Tendering", "Announced", "Stalled or Delayed"];
const STATUS_STYLE: Record<Project["status"], string> = {
  Completed: "var(--good)",
  "Under Construction": "var(--badge-third)",
  Tendering: "var(--badge-estimate)",
  Announced: "var(--badge-editorial)",
  "Stalled or Delayed": "var(--bad)",
};

/** National projects dashboard: status counts (also filters), region and sector filters, sourced cards. */
export function ProjectsDashboard({ items, sourceLabels }: { items: ProjectItem[]; sourceLabels: Record<string, string> }) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const [status, setStatus] = useState<Project["status"] | null>(null);
  const [reg, setReg] = useState<string | null>(null);
  const [sector, setSector] = useState<string | null>(null);

  const regions = useMemo(() => {
    const m = new Map<string, ProjectItem["region"]>();
    items.forEach((i) => m.set(i.region.code, i.region));
    return [...m.values()].sort((a, b) => cmp(pick(a.name, locale), pick(b.name, locale)));
  }, [items, locale]);
  const sectors = useMemo(() => [...new Set(items.map((i) => i.project.sector))], [items]);
  const sectorLabel = (s: string) => (t.has(`sector.${s}`) ? t(`sector.${s}` as "sector.transport") : s);

  const scoped = items.filter((i) => (!reg || i.region.code === reg) && (!sector || i.project.sector === sector));
  const shown = scoped
    .filter((i) => !status || i.project.status === status)
    .sort((a, b) => ORDER.indexOf(a.project.status) - ORDER.indexOf(b.project.status) || cmp(pick(a.project.name, locale), pick(b.project.name, locale)));
  const chip = (on: boolean) => cn("rounded-full border px-3 py-1", on ? "border-navy bg-navy text-bg font-semibold" : "border-border hover:bg-surface-2");

  return (
    <div className="flex min-w-0 flex-col gap-6">
      <section aria-labelledby="dash-h">
        <h2 id="dash-h" className="mb-3 text-xl font-semibold">{t("projects.dashboard")}</h2>
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
          <button
            type="button"
            aria-pressed={status === null}
            onClick={() => setStatus(null)}
            className={cn("rounded-xl border bg-surface p-3 text-left", status === null ? "border-navy ring-2 ring-navy/30" : "border-border")}
          >
            <span className="block text-xs text-muted">{t("projects.total")}</span>
            <span className="text-2xl font-bold tabular-nums"><Digits>{String(scoped.length)}</Digits></span>
          </button>
          {ORDER.map((st) => {
            const n = scoped.filter((i) => i.project.status === st).length;
            return (
              <button
                key={st}
                type="button"
                aria-pressed={status === st}
                onClick={() => setStatus(status === st ? null : st)}
                className={cn("rounded-xl border bg-surface p-3 text-left", status === st ? "border-navy ring-2 ring-navy/30" : "border-border", n === 0 && "opacity-60")}
              >
                <span className="flex items-center gap-1.5 text-xs text-muted">
                  <span aria-hidden className="size-2.5 rounded-full" style={{ background: STATUS_STYLE[st] }} />
                  {t(`projectStatus.${st}` as "projectStatus.Completed")}
                </span>
                <span className="text-2xl font-bold tabular-nums"><Digits>{String(n)}</Digits></span>
              </button>
            );
          })}
        </div>
      </section>

      <div className="flex flex-col gap-3 rounded-2xl border border-border bg-surface p-4 text-sm">
        <div>
          <p id="pj-reg" className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted">{t("projects.region")}</p>
          <div role="group" aria-labelledby="pj-reg" className="flex flex-wrap gap-2">
            <button type="button" aria-pressed={reg === null} onClick={() => setReg(null)} className={chip(reg === null)}>{t("common.all")}</button>
            {regions.map((r) => (
              <button key={r.code} type="button" aria-pressed={reg === r.code} onClick={() => setReg(r.code)} className={chip(reg === r.code)}>{pick(r.name, locale)}</button>
            ))}
          </div>
        </div>
        <div>
          <p id="pj-sec" className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted">{t("projects.sector")}</p>
          <div role="group" aria-labelledby="pj-sec" className="flex flex-wrap gap-2">
            <button type="button" aria-pressed={sector === null} onClick={() => setSector(null)} className={chip(sector === null)}>{t("common.all")}</button>
            {sectors.map((s) => (
              <button key={s} type="button" aria-pressed={sector === s} onClick={() => setSector(s)} className={chip(sector === s)}>{sectorLabel(s)}</button>
            ))}
          </div>
        </div>
      </div>

      <p className="text-sm text-muted" aria-live="polite"><Digits>{t("projects.count", { shown: shown.length })}</Digits></p>

      {shown.length === 0 ? (
        <p className="rounded-xl border border-dashed border-border bg-surface p-6 text-muted">{t("projects.none")}</p>
      ) : (
        <ul className="grid gap-3 md:grid-cols-2">
          {shown.map(({ project: p, region }) => (
            <li key={`${region.code}-${p.id}`} className="flex flex-col gap-2 rounded-xl border border-border bg-surface p-4" style={{ borderLeft: `4px solid ${region.accent}` }}>
              <div className="flex flex-wrap items-start justify-between gap-2">
                <span className="font-semibold">{pick(p.name, locale)}</span>
                <span className="rounded-full border px-2 py-0.5 text-xs font-semibold" style={{ color: STATUS_STYLE[p.status], borderColor: STATUS_STYLE[p.status] }}>
                  {t(`projectStatus.${p.status}` as "projectStatus.Completed")}
                </span>
              </div>
              <p className="text-xs text-muted">
                <Link href={`${region.href}/projects`}>{pick(region.name, locale)}</Link> · {sectorLabel(p.sector)}
              </p>
              {p.objective && <p className="text-sm">{pick(p.objective, locale)}</p>}
              <dl className="grid grid-cols-2 gap-x-3 gap-y-1 text-xs">
                {p.agency && (<><dt className="text-muted">{t("common.agency")}</dt><dd>{p.agency}</dd></>)}
                {p.cost && typeof p.cost.value === "number" && (<><dt className="text-muted">{t("common.cost")}</dt><dd><Digits>{formatRupeeCrore(p.cost.value, locale)}</Digits></dd></>)}
                {p.start && (<><dt className="text-muted">{t("common.started")}</dt><dd><Digits>{p.start}</Digits></dd></>)}
                {p.completion && (<><dt className="text-muted">{p.status === "Completed" ? t("projectStatus.Completed") : t("common.expected")}</dt><dd><Digits>{p.completion}</Digits></dd></>)}
              </dl>
              {p.challenges && <p className="text-xs"><span className="text-muted">{t("common.challenges")}: </span>{pick(p.challenges, locale)}</p>}
              <p className="mt-auto flex flex-wrap items-center gap-2 pt-1 text-xs text-muted">
                <ConfidenceBadge level={p.confidence} />
                <a href={p.url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1">
                  {sourceLabels[p.sourceId] ?? p.sourceId} <ExternalLink aria-hidden className="size-3" />
                </a>
                <span><Digits>{t("projects.checked", { date: formatDate(p.asOf, locale) })}</Digits></span>
              </p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
