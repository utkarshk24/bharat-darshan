import { useLocale, useTranslations } from "next-intl";
import { ExternalLink } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { Project } from "@/lib/schema";
import { pick } from "@/lib/l10n";
import { formatDate, formatRupeeCrore } from "@/lib/format";
import { SupportingSources } from "@/components/SupportingSources";
import { ConfidenceBadge } from "../ConfidenceBadge";
import { Digits } from "../Num";

const STATUS_STYLE: Record<Project["status"], string> = {
  Completed: "var(--good)",
  "Under Construction": "var(--badge-third)",
  Tendering: "var(--badge-estimate)",
  Announced: "var(--badge-editorial)",
  "Stalled or Delayed": "var(--bad)",
};

/** Project cards with status label, cost, agency, asOf and source (Section 7J). */
export function ProjectCards({ projects, sourceLabels, accent }: { projects: Project[]; sourceLabels: Record<string, string>; accent: string }) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const order: Project["status"][] = ["Completed", "Under Construction", "Tendering", "Announced", "Stalled or Delayed"];
  return (
    <section className="flex flex-col gap-6">
      {order.map((st) => {
        const list = projects.filter((p) => p.status === st);
        if (!list.length) return null;
        return (
          <div key={st}>
            <h3 className="mb-3 flex items-center gap-2 text-lg font-semibold">
              <span aria-hidden className="size-3 rounded-full" style={{ background: STATUS_STYLE[st] }} />
              {t(`projectStatus.${st}` as "projectStatus.Completed")} ({list.length})
            </h3>
            <ul className="grid gap-3 md:grid-cols-2">
              {list.map((p) => (
                <li key={p.id} className="flex flex-col gap-2 rounded-xl border border-border bg-surface p-4" style={{ borderLeft: `4px solid ${accent}` }}>
                  <div className="flex flex-wrap items-start justify-between gap-2">
                    <span className="font-semibold">{pick(p.name, locale)}</span>
                    <span className="rounded-full border px-2 py-0.5 text-xs font-semibold" style={{ color: STATUS_STYLE[st], borderColor: STATUS_STYLE[st] }}>
                      {t(`projectStatus.${st}` as "projectStatus.Completed")}
                    </span>
                  </div>
                  {p.objective && <p className="text-sm">{pick(p.objective, locale)}</p>}
                  <dl className="grid grid-cols-2 gap-x-3 gap-y-1 text-xs">
                    {p.agency && (<><dt className="text-muted">{t("common.agency")}</dt><dd>{p.agency}</dd></>)}
                    {p.cost && typeof p.cost.value === "number" && (<><dt className="text-muted">{t("common.cost")}</dt><dd><Digits>{formatRupeeCrore(p.cost.value, locale)}</Digits>{p.cost.note ? ` (${p.cost.note})` : ""}</dd></>)}
                    {p.start && (<><dt className="text-muted">{t("common.started")}</dt><dd><Digits>{p.start}</Digits></dd></>)}
                    {p.completion && (<><dt className="text-muted">{st === "Completed" ? t("projectStatus.Completed") : t("common.expected")}</dt><dd><Digits>{p.completion}</Digits></dd></>)}
                  </dl>
                  {p.challenges && <p className="text-xs"><span className="text-muted">{t("common.challenges")}: </span>{pick(p.challenges, locale)}</p>}
                  <p className="mt-auto flex flex-wrap items-center gap-2 pt-1 text-xs text-muted">
                    <ConfidenceBadge level={p.confidence} />
                    <a href={p.url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1">
                      {sourceLabels[p.sourceId] ?? p.sourceId} <ExternalLink aria-hidden className="size-3" />
                    </a>
                    <SupportingSources items={p.supporting} sourceLabels={sourceLabels} />
                    <span><Digits>{t("common.asOfShort", { date: formatDate(p.asOf, locale) })}</Digits></span>
                  </p>
                </li>
              ))}
            </ul>
          </div>
        );
      })}
    </section>
  );
}
