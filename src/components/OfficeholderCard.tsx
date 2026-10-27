import { useLocale, useTranslations } from "next-intl";
import { UserRound } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { Officeholder } from "@/lib/schema";
import { pick } from "@/lib/l10n";
import { SourceInfo } from "./SourceInfo";

/** Time-sensitive officeholder with asOf + verify link (Principle 3). No party colours (Principle 6). */
export function OfficeholderCard({ o, sourceLabel }: { o: Officeholder; sourceLabel: string | null }) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  return (
    <div className="flex flex-col gap-1 rounded-xl border border-border bg-surface p-4">
      <span className="flex items-center gap-1.5 text-sm text-muted">
        <UserRound aria-hidden className="size-4" /> {t(`roles.${o.role}`)}
      </span>
      {o.name ? (
        <span className="text-lg font-semibold">{pick(o.name, locale)}</span>
      ) : (
        <span className="text-lg font-medium text-muted">{t("common.pendingVerification")}</span>
      )}
      {o.party && <span className="text-sm">{o.party}</span>}
      <SourceInfo
        subject={`${t(`roles.${o.role}`)}${o.name ? `: ${o.name.en}` : ""}`}
        sourceLabel={sourceLabel}
        asOf={o.asOf}
        url={o.url}
        verifyUrl={o.verifyUrl}
        confidence={o.confidence}
        revisionStatus={o.revisionStatus}
        note={o.note}
      />
    </div>
  );
}
