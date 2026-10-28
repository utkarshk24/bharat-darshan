import { useTranslations } from "next-intl";
import { Link } from "@/i18n/navigation";
import { MODULES, type ModuleKey } from "@/lib/nav";
import { cn } from "@/lib/cn";
import { ScrollActiveTab } from "./ScrollActiveTab";

const LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

/** Sticky side-nav on desktop, horizontally scrolling tabs on mobile (Section 7). */
export function ModuleNav({ base, current }: { base: string; current: ModuleKey }) {
  const t = useTranslations();
  return (
    <nav aria-label={t("profile.modules")} className="min-w-0 lg:sticky lg:top-24 lg:self-start print:hidden">
      <p className="mb-2 hidden text-xs font-semibold uppercase tracking-wide text-muted lg:block">{t("profile.modules")}</p>
      <ol id="module-tabs" className="-mx-4 flex gap-1 overflow-x-auto px-4 pb-2 text-sm lg:mx-0 lg:max-h-[calc(100vh-8rem)] lg:flex-col lg:overflow-y-auto lg:px-0">
        {MODULES.map((m, i) => {
          const active = m === current;
          return (
            <li key={m} className="shrink-0">
              <Link
                href={m === "overview" ? base : `${base}/${m}`}
                aria-current={active ? "page" : undefined}
                className={cn(
                  "flex items-center gap-2 whitespace-nowrap rounded-md px-2.5 py-1.5 no-underline lg:whitespace-normal",
                  active ? "bg-navy text-bg font-semibold" : "text-text hover:bg-surface-2",
                )}
              >
                <span aria-hidden className="w-4 text-xs opacity-70">{LETTERS[i]}</span>
                {t(`modules.${m}`)}
              </Link>
            </li>
          );
        })}
      </ol>
      <ScrollActiveTab containerId="module-tabs" />
    </nav>
  );
}
