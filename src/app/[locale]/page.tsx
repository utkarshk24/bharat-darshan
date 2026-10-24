import { getTranslations, setRequestLocale } from "next-intl/server";
import { TrendingUp, BookOpenText, Sparkles, Hash, ArrowRight } from "lucide-react";
import { Link } from "@/i18n/navigation";
import type { Locale } from "@/i18n/routing";
import { getDataAsOn, getGlossary, getRegions, getSummaries } from "@/lib/data";
import { FEATURED_COMPARISONS } from "@/lib/nav";
import { pick } from "@/lib/l10n";
import { SITE_URL } from "@/lib/seo";
import { GlobalSearch } from "@/components/GlobalSearch";
import { IndiaMap } from "@/components/map/IndiaMap";
import { RegionGrid } from "@/components/RegionGrid";
import { DataAsOn } from "@/components/DataAsOn";
import { Disclaimer } from "@/components/Disclaimer";
import { Motif } from "@/components/Motif";
import { Digits } from "@/components/Num";

// Rebuild daily so "featured today" and "indicator of the day" rotate.
export const revalidate = 86400;

const HERO = {
  en: "Explore India, State by State",
  hi: "भारत को जानिए, राज्य-दर-राज्य",
  mr: "भारत जाणून घ्या, राज्याराज्यांतून",
} as const;

function dayIndex(n: number) {
  const now = new Date();
  const start = Date.UTC(now.getUTCFullYear(), 0, 0);
  return Math.floor((now.getTime() - start) / 86400000) % n;
}

export default async function Home({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations();
  const summaries = getSummaries();
  const regions = getRegions();
  const asOn = getDataAsOn();
  const glossary = getGlossary();

  const states = regions.filter((r) => r.type === "state").length;
  const uts = regions.filter((r) => r.type === "ut").length;
  const utsWithLeg = regions.filter((r) => r.governanceModel === "ut-with-legislature").length;
  const zonal = new Set(regions.map((r) => r.zonalCouncil).filter((z) => z && z !== "islands")).size;

  const featured = summaries[dayIndex(summaries.length)];
  const indicator = glossary[dayIndex(glossary.length)];
  const otherHeroes = (Object.keys(HERO) as Locale[]).filter((l) => l !== locale);

  const insights = ["insightGsdpGrowth", "insightLiteracy", "insightForest", "insightTourism", "insightProjects"] as const;

  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: t("common.siteName"),
    url: `${SITE_URL}/${locale}`,
    inLanguage: ["en-IN", "hi-IN", "mr-IN"],
    description: t("common.tagline"),
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />

      {/* Hero */}
      <section className="relative overflow-hidden border-b border-border bg-surface">
        <Motif motif="jaali" color="var(--navy)" opacity={0.05} className="absolute inset-0" />
        <div className="relative mx-auto flex max-w-7xl flex-col gap-6 px-4 py-14 sm:py-20">
          <DataAsOn date={asOn} />
          <div>
            <h1 className="max-w-4xl text-4xl font-bold tracking-tight sm:text-5xl lg:text-6xl">{HERO[locale]}</h1>
            <p className="mt-3 flex flex-wrap gap-x-4 text-lg text-muted">
              {otherHeroes.map((l) => (
                <span key={l} lang={l}>
                  {HERO[l]}
                </span>
              ))}
            </p>
          </div>
          <p className="max-w-3xl text-lg">{t("home.heroSub")}</p>
          <GlobalSearch regions={summaries} />
        </div>
      </section>

      <div className="mx-auto flex max-w-7xl flex-col gap-16 px-4 py-12">
        {/* Map */}
        <section aria-labelledby="map-h">
          <h2 id="map-h" className="mb-4 text-2xl font-bold">{t("home.mapTitle")}</h2>
          <IndiaMap regions={summaries} compact />
        </section>

        {/* Quick facts, featured region, indicator of the day */}
        <section className="grid gap-4 lg:grid-cols-3" aria-label={t("home.nationalFacts")}>
          <div className="rounded-2xl border border-border bg-surface p-5">
            <h2 className="mb-4 flex items-center gap-2 text-lg font-semibold">
              <Hash aria-hidden className="size-5 text-saffron-ink" />
              {t("home.nationalFacts")}
            </h2>
            <dl className="grid grid-cols-2 gap-4">
              {[
                [t("home.factStates"), states],
                [t("home.factUTs"), uts],
                [t("home.factUTsWithLegislature"), utsWithLeg],
                [t("home.factZonalCouncils"), zonal],
              ].map(([label, n]) => (
                <div key={String(label)}>
                  <dt className="text-sm text-muted">{label}</dt>
                  <dd className="text-3xl font-bold tabular-nums">
                    <Digits>{String(n)}</Digits>
                  </dd>
                </div>
              ))}
            </dl>
            <p className="mt-4 flex flex-wrap items-center justify-between gap-2 text-xs text-muted">
              <span>MHA · {t("confidence.Official")}</span>
              <Link href="/india" className="text-sm font-medium">{t("nav.india")} →</Link>
            </p>
          </div>

          <div className="relative overflow-hidden rounded-2xl border border-border bg-surface p-5">
            <Motif motif={featured.motif} color={featured.accent} opacity={0.12} className="absolute inset-0" />
            <div className="relative">
              <h2 className="mb-4 flex items-center gap-2 text-lg font-semibold">
                <Sparkles aria-hidden className="size-5 text-saffron-ink" />
                {t("home.featuredRegion")}
              </h2>
              <p className="text-2xl font-bold" style={{ color: featured.accent }}>
                {pick(featured.name, locale)}
              </p>
              {featured.localName && <p lang={featured.localName.lang} className="text-muted">{featured.localName.text}</p>}
              <p className="mt-2 text-sm">
                {t("common.capital")}: {featured.capitals.map((c) => pick(c.name, locale)).join(" / ")}
              </p>
              <Link href={featured.type === "state" ? `/states/${featured.slug}` : `/uts/${featured.slug}`} className="mt-4 inline-flex items-center gap-1 font-medium">
                {t("common.viewProfile")} <ArrowRight aria-hidden className="size-4" />
              </Link>
            </div>
          </div>

          <div className="rounded-2xl border border-border bg-surface p-5">
            <h2 className="mb-4 flex items-center gap-2 text-lg font-semibold">
              <BookOpenText aria-hidden className="size-5 text-saffron-ink" />
              {t("home.indicatorOfDay")}
            </h2>
            <p className="text-xl font-semibold">
              {pick(indicator.term, locale)}
              {indicator.abbreviation && <span className="text-muted"> ({indicator.abbreviation})</span>}
            </p>
            <p className="mt-2 text-sm">{pick(indicator.definition, locale)}</p>
            <p className="mt-3 text-xs text-muted">{t("home.indicatorPending")}</p>
            <Link href="/glossary" className="mt-3 inline-block text-sm">{t("nav.glossary")} →</Link>
          </div>
        </section>

        {/* Trending insights — computed only from verified data */}
        <section aria-labelledby="trend-h">
          <h2 id="trend-h" className="mb-2 flex items-center gap-2 text-2xl font-bold">
            <TrendingUp aria-hidden className="size-6 text-green-ink" />
            {t("home.trendingTitle")}
          </h2>
          <p className="mb-4 text-muted">{t("home.trendingPending")}</p>
          <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
            {insights.map((k) => (
              <li key={k} className="rounded-xl border border-dashed border-border bg-surface p-4">
                <p className="text-sm font-medium">{t(`home.${k}`)}</p>
                <p className="mt-2 text-muted">{t("common.notAvailable")}</p>
              </li>
            ))}
          </ul>
        </section>

        {/* Featured comparisons */}
        <section aria-labelledby="cmp-h">
          <h2 id="cmp-h" className="mb-4 text-2xl font-bold">{t("home.featuredTitle")}</h2>
          <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {FEATURED_COMPARISONS.map((c) => {
              const names = c.ids.map((id) => summaries.find((s) => s.code === id)!).filter(Boolean);
              return (
                <li key={c.key}>
                  <Link
                    href={{ pathname: "/compare", query: { group: c.group } }}
                    className="flex h-full flex-col gap-2 rounded-xl border border-border bg-surface p-4 text-text no-underline hover:shadow-md"
                  >
                    <span className="flex items-center justify-between font-semibold">
                      {t(`home.${c.key}`)} <ArrowRight aria-hidden className="size-4 text-muted" />
                    </span>
                    <span className="flex flex-wrap gap-1">
                      {names.map((n) => (
                        <span key={n.code} className="rounded-full px-2 py-0.5 text-xs" style={{ background: `${n.accent}22` }}>
                          {pick(n.name, locale)}
                        </span>
                      ))}
                    </span>
                  </Link>
                </li>
              );
            })}
          </ul>
        </section>

        {/* All 36 cards */}
        <section aria-labelledby="cards-h">
          <h2 id="cards-h" className="mb-4 text-2xl font-bold">{t("home.cardsTitle")}</h2>
          <RegionGrid regions={summaries} />
        </section>

        <Disclaimer />
      </div>
    </>
  );
}
