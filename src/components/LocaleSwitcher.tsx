"use client";
import { useLocale, useTranslations } from "next-intl";
import { Link, usePathname } from "@/i18n/navigation";
import { locales } from "@/i18n/routing";
import { cn } from "@/lib/cn";

const LABEL: Record<string, { short: string; long: string }> = {
  en: { short: "EN", long: "English" },
  hi: { short: "हि", long: "हिन्दी" },
  mr: { short: "म", long: "मराठी" },
};

/** Instant language switch that keeps the current page (Section 11). */
export function LocaleSwitcher() {
  const t = useTranslations("settings");
  const locale = useLocale();
  const pathname = usePathname();
  return (
    <div role="group" aria-label={t("language")} className="flex overflow-hidden rounded-md border border-border text-sm">
      {locales.map((l) => (
        <Link
          key={l}
          href={pathname}
          locale={l}
          lang={l}
          hrefLang={l}
          aria-current={l === locale ? "true" : undefined}
          className={cn(
            "px-2.5 py-1.5 no-underline",
            l === locale ? "bg-navy text-bg font-semibold" : "text-text hover:bg-surface-2",
          )}
        >
          {/* Visible abbreviation first so the accessible name contains it (WCAG 2.5.3) */}
          {LABEL[l].short}
          <span className="sr-only"> {LABEL[l].long}</span>
        </Link>
      ))}
    </div>
  );
}
