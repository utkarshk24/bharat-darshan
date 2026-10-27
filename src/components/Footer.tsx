import { useTranslations } from "next-intl";
import { Link } from "@/i18n/navigation";
import { NAV } from "@/lib/nav";
import { DataAsOn } from "./DataAsOn";
import { Disclaimer } from "./Disclaimer";
import { CorrectionLink } from "./CorrectionLink";

export function Footer({ asOn }: { asOn: string }) {
  const t = useTranslations();
  return (
    <footer className="mt-16 border-t border-border bg-surface">
      <div className="mx-auto grid max-w-7xl gap-8 px-4 py-10 md:grid-cols-[2fr_3fr]">
        <div className="flex flex-col gap-3">
          <p className="text-lg font-semibold">{t("common.siteName")}</p>
          <p className="text-sm text-muted">{t("common.tagline")}</p>
          <DataAsOn date={asOn} />
          <Disclaimer />
          <p className="text-sm text-muted">
            {t("common.correctionsInvite")} <CorrectionLink />
          </p>
        </div>
        <nav aria-label={t("nav.primary")}>
          <ul className="grid grid-cols-2 gap-x-6 gap-y-2 text-sm sm:grid-cols-3">
            {NAV.map((n) => (
              <li key={n.key}>
                <Link href={n.href} className="text-text">
                  {t(`nav.${n.key}`)}
                </Link>
              </li>
            ))}
          </ul>
        </nav>
      </div>
      <div className="tricolour-rule" />
    </footer>
  );
}
