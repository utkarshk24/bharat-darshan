"use client";
import { useLocale, useTranslations } from "next-intl";
import type { Locale } from "@/i18n/routing";
import type { DataPoint } from "@/lib/schema";
import { formatCompactIndian, formatIndianNumber, formatRupeeCrore } from "@/lib/format";
import { cn } from "@/lib/cn";
import { SourceInfo } from "./SourceInfo";
import { Digits } from "./Num";
import { TrendBadge } from "./TrendBadge";
import type { Polarity } from "@/lib/format";
import { formatPeriod } from "@/lib/format";

export type { ValueKind } from "@/lib/format";
export { formatValue };
import { formatValue, type ValueKind } from "@/lib/format";

/**
 * A single indicator with provenance (Section 12 "stat card").
 * Shows "Not available" for null values — never a placeholder number.
 */
export function StatCard({
  label,
  dp,
  kind = "number",
  sourceLabel,
  national,
  className,
  accent,
  previous,
  polarity = "neutral",
}: {
  label: string;
  dp: DataPoint | null | undefined;
  kind?: ValueKind;
  sourceLabel?: string | null;
  national?: DataPoint | null;
  className?: string;
  accent?: string;
  previous?: DataPoint | null;
  polarity?: Polarity;
}) {
  const t = useTranslations("common");
  const unitLabel = (u: string) =>
    u.startsWith("females per 1000") ? t("units.sexRatio") : u.startsWith("girls per 1000") ? t("units.childSexRatio") : u;
  const locale = useLocale() as Locale;
  const value = dp ? formatValue(dp, kind, locale) : null;
  const nat = national ? formatValue(national, kind, locale) : null;
  return (
    <div
      className={cn("flex flex-col gap-1 rounded-xl border border-border bg-surface p-4", className)}
      style={accent ? { borderTop: `3px solid ${accent}` } : undefined}
    >
      <span className="text-sm text-muted">{label}</span>
      {value ? (
        <span className="text-2xl font-semibold tabular-nums">
          <Digits>{value}</Digits>
        </span>
      ) : (
        <span className="text-lg font-medium text-muted">{t("notAvailable")}</span>
      )}
      {dp && dp.unit && value && kind === "ratio" && <span className="text-xs text-muted">{unitLabel(dp.unit)}</span>}
      {value && previous && typeof previous.value === "number" && typeof dp?.value === "number" && (
        <span className="flex flex-wrap items-center gap-1.5 text-xs text-muted">
          <TrendBadge
            delta={kind === "percent" || kind === "number" || kind === "ratio" ? +(dp.value - previous.value).toFixed(2) : +(((dp.value - previous.value) / previous.value) * 100).toFixed(1)}
            unit={kind === "percent" ? " pp" : kind === "number" || kind === "ratio" ? "" : "%"}
            polarity={polarity}
          />
          <span>
            {t("vs")} <Digits>{formatPeriod(previous.period, locale)}</Digits>
          </span>
        </span>
      )}
      {national !== undefined && (
        <span className="text-xs text-muted">
          {t("nationalAverage")}: {nat ? <Digits>{nat}</Digits> : t("notAvailable")}
        </span>
      )}
      {dp && (
        <SourceInfo
          sourceLabel={sourceLabel ?? dp.sourceId}
          period={dp.period}
          url={dp.url}
          accessDate={dp.accessDate}
          confidence={dp.confidence}
          revisionStatus={dp.revisionStatus}
          note={dp.note}
        />
      )}
    </div>
  );
}
