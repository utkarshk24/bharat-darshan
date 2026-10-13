"use client";
import { useLocale, useTranslations } from "next-intl";
import { Landmark, MapPin, Users, IndianRupee, UserRound } from "lucide-react";
import { Link } from "@/i18n/navigation";
import type { Locale } from "@/i18n/routing";
import type { RegionSummary } from "@/lib/data";
import { pick } from "@/lib/l10n";
import { formatValue } from "./StatCard";
import { SourceInfo } from "./SourceInfo";
import { Motif } from "./Motif";
import { Digits } from "./Num";

function Row({ icon: Icon, label, children }: { icon: typeof MapPin; label: string; children: React.ReactNode }) {
  return (
    <div className="flex items-start gap-2 text-sm">
      <Icon aria-hidden className="mt-0.5 size-4 shrink-0 text-muted" />
      <dt className="sr-only">{label}</dt>
      <dd className="min-w-0">{children}</dd>
    </div>
  );
}

/** Home-page card for one State/UT (Section 6). */
export function RegionCard({ r }: { r: RegionSummary }) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const name = pick(r.name, locale);
  const cap = r.capitals[0];
  const pop = r.population2011 ? formatValue(r.population2011, "count", locale) : null;
  const gsdp = r.gsdpCurrent ? formatValue(r.gsdpCurrent, "rupeeCrore", locale) : null;
  const href = r.type === "state" ? `/states/${r.slug}` : `/uts/${r.slug}`;
  const heads = [r.headOfGovernment, r.headOfState].filter(Boolean);

  return (
    <article className="group relative flex flex-col overflow-hidden rounded-2xl border border-border bg-surface shadow-sm transition hover:shadow-md focus-within:ring-2 focus-within:ring-[var(--focus)]">
      <div className="relative h-20" style={{ background: `${r.accent}1a` }}>
        <Motif motif={r.motif} color={r.accent} opacity={0.5} className="absolute inset-0" />
        <div className="absolute inset-x-0 top-0 h-1.5" style={{ background: r.accent }} />
        <span className="absolute bottom-2 left-4 rounded-full bg-surface/90 px-2 py-0.5 text-xs font-medium text-text">
          {r.type === "state" ? t("common.state") : t("common.ut")}
          {r.zonalCouncil ? ` · ${t(`zonal.${r.zonalCouncil}`)}` : ""}
        </span>
      </div>
      <div className="flex flex-1 flex-col gap-3 p-4">
        <div>
          <h3 className="text-lg font-semibold leading-snug">
            <Link href={href} className="text-text no-underline after:absolute after:inset-0 hover:underline">
              {name}
            </Link>
          </h3>
          {r.localName && (
            <p className="text-sm text-muted" lang={r.localName.lang}>
              {r.localName.text}
            </p>
          )}
        </div>
        <dl className="flex flex-col gap-1.5">
          <Row icon={Landmark} label={t("common.capital")}>
            {r.capitals.map((c) => pick(c.name, locale)).join(" / ")}
            {cap?.formerName && <span className="text-muted"> ({t("common.formerly", { name: pick(cap.formerName, locale) })})</span>}
          </Row>
          <Row icon={Users} label={t("common.population")}>
            {pop ? <Digits>{pop}</Digits> : <span className="text-muted">{t("common.population")}: {t("common.notAvailable")}</span>}
          </Row>
          <Row icon={IndianRupee} label={t("common.gsdp")}>
            {gsdp ? <Digits>{gsdp}</Digits> : <span className="text-muted">{t("common.gsdp")}: {t("common.notAvailable")}</span>}
          </Row>
          {heads.map((h) => (
            <Row key={h!.role} icon={UserRound} label={t(`roles.${h!.role}`)}>
              <span className="text-muted">{t(`roles.${h!.role}`)}: </span>
              {h!.name ? pick(h!.name, locale) : <span className="text-muted">{t("common.pendingVerification")}</span>}
            </Row>
          ))}
        </dl>
        <div className="relative z-10 mt-auto">
          {r.population2011 && (
            <SourceInfo
              sourceLabel={r.population2011.sourceId ? r.sourceLabels[r.population2011.sourceId] : null}
              period={r.population2011.period}
              url={r.population2011.url}
              accessDate={r.population2011.accessDate}
              confidence={r.population2011.confidence}
              revisionStatus={r.population2011.revisionStatus}
              note={r.population2011.note}
            />
          )}
        </div>
      </div>
    </article>
  );
}
