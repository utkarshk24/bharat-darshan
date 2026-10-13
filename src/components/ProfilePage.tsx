import { getTranslations } from "next-intl/server";
import { Construction, Landmark } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { Region } from "@/lib/schema";
import { getIndia, getModule, sourceName } from "@/lib/data";
import { ModuleBlocks } from "./blocks/ModuleBlocks";
import { formatDate } from "@/lib/format";
import { pick } from "@/lib/l10n";
import type { ModuleKey } from "@/lib/nav";
import { SITE_URL } from "@/lib/seo";
import { ModuleNav } from "./ModuleNav";
import { StatCard, type ValueKind } from "./StatCard";
import { OfficeholderCard } from "./OfficeholderCard";
import { DataAsOn } from "./DataAsOn";
import { Disclaimer } from "./Disclaimer";
import { Motif, MotifDivider } from "./Motif";
import { LocalizedText } from "./LocalizedText";
import { ComingSoonInline } from "./ComingSoonInline";

const GLANCE: { key: string; label: string; kind: ValueKind }[] = [
  { key: "population2011", label: "common.population", kind: "count" },
  { key: "area", label: "profile.area", kind: "number" },
  { key: "density2011", label: "profile.density", kind: "number" },
  { key: "sexRatio2011", label: "profile.sexRatio", kind: "number" },
  { key: "childSexRatio2011", label: "profile.childSexRatio", kind: "number" },
  { key: "literacyRate2011", label: "profile.literacy", kind: "percent" },
  { key: "urbanisation2011", label: "profile.urbanisation", kind: "percent" },
  { key: "gsdpCurrent", label: "common.gsdp", kind: "rupeeCrore" },
  { key: "perCapitaNsdpCurrent", label: "profile.perCapitaNsdp", kind: "rupee" },
  { key: "forestCoverPct", label: "profile.forestCover", kind: "percent" },
];

export async function ProfilePage({ region: r, locale, module }: { region: Region; locale: Locale; module: ModuleKey }) {
  const t = await getTranslations();
  const india = getIndia();
  const base = `/${r.type === "state" ? "states" : "uts"}/${r.slug}`;
  const label = (id: string | null) => (id ? sourceName(id)?.short ?? id : null);
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
          <nav aria-label="Breadcrumb" className="mb-3 text-sm">
            <ol className="flex flex-wrap gap-1 text-muted">
              <li><a href={`/${locale}`}>{t("nav.home")}</a> /</li>
              <li><a href={`/${locale}/${r.type === "state" ? "states" : "uts"}`}>{r.type === "state" ? t("common.states") : t("common.uts")}</a> /</li>
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
              {!content && (
                <div className="flex gap-3 rounded-xl border border-dashed border-border bg-surface p-4 text-sm">
                  <Construction aria-hidden className="mt-0.5 size-5 shrink-0 text-saffron-ink" />
                  <div>
                    <p className="font-semibold">{t("profile.phase2")}</p>
                    <p className="text-muted">{t("profile.phase2Body")}</p>
                  </div>
                </div>
              )}
              {content && <ModuleBlocks blocks={content.blocks.filter((b) => b.id.startsWith("intro"))} region={r} locale={locale} />}

              <section aria-labelledby="glance-h">
                <h2 id="glance-h" className="mb-4 text-2xl font-bold">{t("profile.atAGlance")}</h2>
                <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
                  {GLANCE.map((g) => {
                    const dp = r.metrics[g.key];
                    return (
                      <StatCard
                        key={g.key}
                        label={t(g.label as "common.population")}
                        dp={dp}
                        kind={g.kind}
                        sourceLabel={label(dp?.sourceId ?? null)}
                        national={india.metrics[g.key] ?? null}
                        accent={r.accent}
                      />
                    );
                  })}
                </div>
              </section>

              <MotifDivider motif={r.motif} color={r.accent} />

              <section aria-labelledby="gov-h">
                <h2 id="gov-h" className="mb-4 text-2xl font-bold">{t("profile.governance")}</h2>
                <div className="grid gap-3 sm:grid-cols-2">
                  {r.government.headOfState && <OfficeholderCard o={r.government.headOfState} sourceLabel={label(r.government.headOfState.sourceId)} />}
                  {r.government.headOfGovernment ? (
                    <OfficeholderCard o={r.government.headOfGovernment} sourceLabel={label(r.government.headOfGovernment.sourceId)} />
                  ) : (
                    <div className="rounded-xl border border-border bg-surface p-4">
                      <p className="text-sm text-muted">{t("profile.headOfGovernment")}</p>
                      <p className="mt-1">{t("profile.noCm")}</p>
                    </div>
                  )}
                </div>
              </section>

              {content && <ModuleBlocks blocks={content.blocks.filter((b) => !b.id.startsWith("intro"))} region={r} locale={locale} />}

              {Object.keys(r.symbols).length > 0 && (
                <section aria-labelledby="sym-h">
                  <h2 id="sym-h" className="mb-4 text-2xl font-bold">{t("profile.symbols")}</h2>
                  <dl className="grid gap-3 sm:grid-cols-2">
                    {Object.entries(r.symbols).map(([k, s]) => (
                      <div key={k} className="rounded-xl border border-border bg-surface p-4">
                        <dt className="text-sm text-muted">{t.has(`profile.symbolKinds.${k}`) ? t(`profile.symbolKinds.${k}`) : k}</dt>
                        <dd className="text-lg font-semibold"><LocalizedText value={s.name} locale={locale} /></dd>
                        {s.scientificName && <dd className="text-sm italic text-muted">{s.scientificName}</dd>}
                        <dd className="mt-1 text-xs text-muted">{t("common.source")}: {s.sourceId ? label(s.sourceId) : t("common.pendingVerification")}</dd>
                      </div>
                    ))}
                  </dl>
                </section>
              )}
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
