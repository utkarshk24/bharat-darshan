import { getTranslations } from "next-intl/server";
import { Printer } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { Region } from "@/lib/schema";
import { getModule } from "@/lib/data";
import { formatDate } from "@/lib/format";
import { pick } from "@/lib/l10n";
import { MODULES } from "@/lib/nav";
import { BASE_PATH, SITE_URL } from "@/lib/seo";
import { ModuleBlocks } from "./blocks/ModuleBlocks";
import { ProfileOverview } from "./ProfileOverview";
import { PrintButton, PrintModeProvider } from "./PrintMode";
import { Disclaimer } from "./Disclaimer";
import { Digits } from "./Num";

/**
 * The whole profile on one page, laid out for printing or "Save as PDF" (Phase 4).
 * Same content and sources as the section pages; every source is written out in full,
 * series are shown as tables, and live weather is left out.
 */
export async function ProfilePrint({ region: r, locale }: { region: Region; locale: Locale }) {
  const t = await getTranslations();
  const base = `/${r.type === "state" ? "states" : "uts"}/${r.slug}`;
  const online = `${SITE_URL}/${locale}${base}`;
  const others = (["en", "hi", "mr"] as const).map((l) => r.name[l]).filter((n, i, all) => n !== r.name[locale] && all.indexOf(n) === i);

  return (
    <PrintModeProvider>
      <article className="print-doc mx-auto max-w-4xl px-4 py-8">
        <div className="mb-8 flex flex-col gap-3 rounded-2xl border border-border bg-surface p-4 print:hidden">
          <div className="flex flex-wrap items-center gap-3">
            <PrintButton
              label={t("print.save")}
              className="inline-flex items-center gap-2 rounded-md bg-navy px-4 py-2 font-semibold text-bg hover:opacity-90"
            />
            <a href={`${BASE_PATH}/${locale}${base}`}>{t("print.back", { region: pick(r.name, locale) })}</a>
          </div>
          <p className="flex items-start gap-2 text-sm text-muted">
            <Printer aria-hidden className="mt-0.5 size-4 shrink-0" /> {t("print.howTo")}
          </p>
        </div>

        <header className="mb-8 border-b-4 pb-6" style={{ borderColor: r.accent }}>
          <p className="text-sm font-semibold uppercase tracking-wide text-muted">
            {t("common.siteName")} · {r.type === "state" ? t("common.state") : t("common.ut")}
          </p>
          <h1 className="mt-1 text-4xl font-bold tracking-tight">{pick(r.name, locale)}</h1>
          {(others.length > 0 || r.localName) && (
            <p className="mt-1 flex flex-wrap gap-x-4 text-lg text-muted">
              {others.map((n) => <span key={n}>{n}</span>)}
              {r.localName && <span lang={r.localName.lang}>{r.localName.text}</span>}
            </p>
          )}
          <dl className="mt-4 grid gap-x-6 gap-y-1 text-sm sm:grid-cols-2">
            <div><dt className="inline text-muted">ISO 3166-2: </dt><dd className="inline font-medium">{r.code}</dd></div>
            <div><dt className="inline text-muted">{t("print.governance")}: </dt><dd className="inline font-medium">{t(`governance.${r.governanceModel}`)}</dd></div>
            {r.capitals.map((c) => (
              <div key={c.role + c.name.en}>
                <dt className="inline text-muted">{t(`capitalRoles.${c.role}`)}: </dt>
                <dd className="inline font-medium">{pick(c.name, locale)}</dd>
              </div>
            ))}
            <div><dt className="inline text-muted">{t("print.dataAsOn")}: </dt><dd className="inline font-medium"><Digits>{formatDate(r.meta.lastUpdated, locale)}</Digits></dd></div>
          </dl>
          <p className="mt-4 text-sm">
            {t("print.onlineAt")} <a href={online} className="print-url break-all">{online}</a>
          </p>
          <p className="mt-1 text-sm text-muted">{t("print.snapshot")}</p>
        </header>

        <nav aria-labelledby="toc-h" className="mb-10">
          <h2 id="toc-h" className="mb-2 text-xl font-semibold">{t("print.contents")}</h2>
          <ol className="grid list-decimal gap-x-8 gap-y-0.5 pl-6 text-sm sm:grid-cols-3">
            {MODULES.map((m) => (
              <li key={m}><a href={`#${m}`}>{t(`modules.${m}`)}</a></li>
            ))}
          </ol>
        </nav>

        <div className="flex flex-col gap-12 print:block">
          <section id="overview" aria-labelledby="m-overview" className="print-module flex flex-col gap-8 print:block print:space-y-8">
            <h2 id="m-overview" className="text-3xl font-bold">{t("modules.overview")}</h2>
            <ProfileOverview region={r} locale={locale} level={3} print />
          </section>

          {MODULES.filter((m) => m !== "overview").map((m) => {
            const content = getModule(r.code, m);
            return (
              <section key={m} id={m} aria-labelledby={`m-${m}`} className="print-module flex flex-col gap-4 print:block print:space-y-4">
                <div className="flex flex-wrap items-baseline justify-between gap-2">
                  <h2 id={`m-${m}`} className="text-3xl font-bold">{t(`modules.${m}`)}</h2>
                  {content && (
                    <span className="text-xs text-muted">
                      <Digits>{t("common.asOfShort", { date: formatDate(content.asOf, locale) })}</Digits>
                      {locale !== "en" ? ` · ${t("common.translationDraft")}` : ""}
                    </span>
                  )}
                </div>
                {content ? (
                  <ModuleBlocks blocks={content.blocks} region={r} locale={locale} print />
                ) : (
                  <p className="text-muted">{t("print.notYet")}</p>
                )}
              </section>
            );
          })}
        </div>

        <footer className="mt-12 flex flex-col gap-3 border-t border-border pt-6 text-sm text-muted">
          <Disclaimer />
          <p>{t("print.licence")}</p>
        </footer>
      </article>
    </PrintModeProvider>
  );
}
