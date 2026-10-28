import { useTranslations } from "next-intl";
import { Menu, ChevronDown } from "lucide-react";
import { Link } from "@/i18n/navigation";
import { NAV, PRIMARY_NAV } from "@/lib/nav";
import { LocaleSwitcher } from "./LocaleSwitcher";
import { DisplayToggles } from "./DisplayToggles";

export function Header() {
  const t = useTranslations();
  const secondary = NAV.filter((n) => n.key !== "home" && !(PRIMARY_NAV as readonly string[]).includes(n.key));
  return (
    <header className="sticky top-0 z-40 border-b border-border bg-surface/95 backdrop-blur print:hidden">
      <div className="tricolour-rule" />
      <div className="mx-auto flex max-w-7xl items-center gap-3 px-4 py-3">
        <Link href="/" className="flex shrink-0 items-center gap-2 text-text no-underline">
          <Chakra />
          <span className="text-base font-bold tracking-tight sm:text-lg">{t("common.siteName")}</span>
        </Link>

        <nav aria-label={t("nav.primary")} className="ml-4 hidden flex-1 xl:block">
          <ul className="flex items-center gap-1 text-sm">
            {PRIMARY_NAV.map((k) => {
              const item = NAV.find((n) => n.key === k)!;
              return (
                <li key={k}>
                  <Link href={item.href} className="whitespace-nowrap rounded-md px-2.5 py-1.5 text-text no-underline hover:bg-surface-2">
                    {t(`nav.${k}`)}
                  </Link>
                </li>
              );
            })}
            <li className="relative">
              <details className="group">
                <summary className="flex cursor-pointer list-none items-center gap-1 whitespace-nowrap rounded-md px-2.5 py-1.5 hover:bg-surface-2">
                  {t("nav.more")} <ChevronDown aria-hidden className="size-4 transition group-open:rotate-180" />
                </summary>
                <ul className="absolute right-0 mt-1 w-64 rounded-lg border border-border bg-surface p-1 shadow-lg">
                  {secondary.map((n) => (
                    <li key={n.key}>
                      <Link href={n.href} className="block rounded-md px-3 py-2 text-text no-underline hover:bg-surface-2">
                        {t(`nav.${n.key}`)}
                      </Link>
                    </li>
                  ))}
                </ul>
              </details>
            </li>
          </ul>
        </nav>

        <div className="ml-auto flex items-center gap-2">
          <LocaleSwitcher />
          <div className="hidden sm:block">
            <DisplayToggles />
          </div>
          <details className="group relative xl:hidden">
            <summary className="flex cursor-pointer list-none items-center rounded-md border border-border p-2" aria-label={t("common.menu")}>
              <Menu aria-hidden className="size-5" />
            </summary>
            <nav aria-label={t("nav.primary")} className="absolute right-0 mt-2 w-72 rounded-lg border border-border bg-surface p-2 shadow-lg">
              <div className="mb-2 flex justify-end border-b border-border pb-2 sm:hidden">
                <DisplayToggles />
              </div>
              <ul>
                {NAV.map((n) => (
                  <li key={n.key}>
                    <Link href={n.href} className="block rounded-md px-3 py-2 text-text no-underline hover:bg-surface-2">
                      {t(`nav.${n.key}`)}
                    </Link>
                  </li>
                ))}
              </ul>
            </nav>
          </details>
        </div>
      </div>
    </header>
  );
}

/** A simple 24-spoke wheel mark. Decorative, not the national emblem. */
function Chakra() {
  return (
    <svg aria-hidden viewBox="0 0 32 32" className="size-7">
      <circle cx="16" cy="16" r="14" fill="none" stroke="var(--navy)" strokeWidth="2" />
      <circle cx="16" cy="16" r="2.5" fill="var(--navy)" />
      {Array.from({ length: 24 }, (_, i) => {
        const a = (i * Math.PI) / 12;
        return <line key={i} x1={16} y1={16} x2={16 + 12.5 * Math.cos(a)} y2={16 + 12.5 * Math.sin(a)} stroke="var(--navy)" strokeWidth="0.8" />;
      })}
    </svg>
  );
}
