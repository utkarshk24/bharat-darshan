import { getTranslations } from "next-intl/server";
import { Landmark, Printer } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { Region } from "@/lib/schema";
import { getModule } from "@/lib/data";
import { ModuleBlocks } from "./blocks/ModuleBlocks";
import { formatDate } from "@/lib/format";
import { pick } from "@/lib/l10n";
import type { ModuleKey } from "@/lib/nav";
import { BASE_PATH, SITE_URL } from "@/lib/seo";
import { ModuleNav } from "./ModuleNav";
import { ProfileOverview } from "./ProfileOverview";
import { DataAsOn } from "./DataAsOn";
import { Disclaimer } from "./Disclaimer";
import { Motif } from "./Motif";
import { LocalizedText } from "./LocalizedText";
import { ComingSoonInline } from "./ComingSoonInline";

export async function ProfilePage({ region: r, locale, module }: { region: Region; locale: Locale; module: ModuleKey }) {
  const t = await getTranslations();
  const base = `/${r.type === "state" ? "states" : "uts"}/${r.slug}`;
  const content = getModule(r.code, module);

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": ["Place", "AdministrativeArea"],
    name: r.name.en,
    alternateName: [r.name.hi, r.name.mr, r.localName?.text].filter(Boolean),
    identifier: r.code,
    containedInPlace: { "@type": "Country", name: "India" },
    url: `${SITE_URL}/${locale}${base}`,
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <section className="relative overflow-hidden border-b border-border" style={{ background: `${r.accent}14` }}>
        <Motif motif={r.motif} color={r.accent} opacity={0.18} className="absolute inset-0" />
        <div className="absolute inset-x-0 top-0 h-1.5" style={{ background: r.accent }} />
        <div className="relative mx-auto max-w-7xl px-4 py-10">
          <nav aria-label={t("common.breadcrumb")} className="breadcrumb mb-3 text-sm">
            <ol className="flex flex-wrap gap-1 text-muted">
              <li><a href={`${BASE_PATH}/${locale}`}>{t("nav.home")}</a> /</li>
              <li><a href={`${BASE_PATH}/${locale}/${r.type === "state" ? "states" : "uts"}`}>{r.type === "state" ? t("common.states") : t("common.uts")}</a> /</li>
              <li aria-current="page">{pick(r.name, locale)}</li>
            </ol>
          </nav>
          <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">{pick(r.name, locale)}</h1>
          <p className="mt-2 flex flex-wrap gap-x-4 text-lg text-muted">
            {(["en", "hi", "mr"] as const)
              .filter((l, i, all) => l !== locale && r.name[l] !== r.name[locale] && all.findIndex((x) => r.name[x] === r.name[l]) === i)
              .map((l) => (
                <span key={l} lang={l}>{r.name[l]}</span>
              ))}
            {r.localName && <span lang={r.localName.lang}>{r.localName.text}</span>}
          </p>
          {r.formerNames?.length ? (
            <p className="mt-1 text-sm text-muted">{t("common.formerly", { name: r.formerNames.map((f) => pick(f, locale)).join(", ") })}</p>
          ) : null}
          <div className="mt-4 flex flex-wrap items-center gap-2 text-sm">
            <span className="rounded-full bg-surface px-3 py-1 font-medium">{t(`governance.${r.governanceModel}`)}</span>
            {r.zonalCouncil && <span className="rounded-full bg-surface px-3 py-1">{t("common.region")}: {t(`zonal.${r.zonalCouncil}`)}</span>}
            <span className="rounded-full bg-surface px-3 py-1">ISO 3166-2: {r.code}</span>
            <DataAsOn date={r.meta.lastUpdated} />
            <a
              href={`${BASE_PATH}/${locale}${base}/print`}
              className="inline-flex items-center gap-1.5 rounded-full border border-border bg-surface px-3 py-1 font-medium no-underline hover:bg-surface-2 print:hidden"
            >
              <Printer aria-hidden className="size-4" /> {t("print.open")}
            </a>
          </div>
          <ul className="mt-4 flex flex-wrap gap-x-6 gap-y-1">
            {r.capitals.map((c) => (
              <li key={c.role + c.name.en} className="flex items-center gap-1.5">
                <Landmark aria-hidden className="size-4 text-muted" />
                <span className="text-muted">{t(`capitalRoles.${c.role}`)}:</span>
                <LocalizedText value={c.name} locale={locale} className="font-medium" />
                {c.formerName && <span className="text-sm text-muted">({t("common.formerly", { name: pick(c.formerName, locale) })})</span>}
              </li>
            ))}
          </ul>
        </div>
      </section>

      <div className="mx-auto grid max-w-7xl gap-8 px-4 py-8 lg:grid-cols-[16rem_1fr]">
        <ModuleNav base={base} current={module} />

        <div className="flex min-w-0 flex-col gap-8">
          {module === "overview" ? (
            <>
              <ProfileOverview region={r} locale={locale} />
            </>
          ) : content ? (
            <>
              <div className="flex flex-wrap items-baseline justify-between gap-2">
                <h2 className="text-3xl font-bold">{t(`modules.${module}`)}</h2>
                <span className="text-xs text-muted">{t("common.asOfShort", { date: formatDate(content.asOf, locale) })}{locale !== "en" ? ` · ${t("common.translationDraft")}` : ""}</span>
              </div>
              <ModuleBlocks blocks={content.blocks} region={r} locale={locale} />
            </>
          ) : (
            <ComingSoonInline title={t(`modules.${module}`)} />
          )}
          <Disclaimer />
        </div>
      </div>
    </>
  );
}
