import { useLocale, useTranslations } from "next-intl";
import { CalendarClock } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import { formatDate } from "@/lib/format";
import { Digits } from "./Num";

/** "Data as on" badge shown on every page (Principle 3). */
export function DataAsOn({ date }: { date: string }) {
  const t = useTranslations("common");
  const locale = useLocale() as Locale;
  return (
    <span className="inline-flex w-fit self-start items-center gap-1.5 rounded-full border border-border bg-surface px-3 py-1 text-xs text-muted">
      <CalendarClock aria-hidden className="size-3.5" />
      <Digits>{t("dataAsOn", { date: formatDate(date, locale) })}</Digits>
    </span>
  );
}
