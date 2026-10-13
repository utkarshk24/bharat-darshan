import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { getTranslations, setRequestLocale } from "next-intl/server";
import { Award, ExternalLink } from "lucide-react";
import { locales, type Locale } from "@/i18n/routing";
import { getAllGI, getRegionNameMap, sourceName } from "@/lib/data";
import { pick, cmp } from "@/lib/l10n";
import { formatDate } from "@/lib/format";
import { localeAlternates } from "@/lib/seo";
import { Link } from "@/i18n/navigation";
import { ConfidenceBadge } from "@/components/ConfidenceBadge";
import { Digits } from "@/components/Num";
import { Disclaimer } from "@/components/Disclaimer";

export function generateStaticParams() {
  return locales.flatMap((locale) => getAllGI().map((g) => ({ locale, slug: g.product.id })));
}

const find = (slug: string) => getAllGI().find((g) => g.product.id === slug);

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale; slug: string }> }): Promise<Metadata> {
  const { locale, slug } = await params;
  const g = find(slug);
  if (!g) return {};
  const t = await getTranslations({ locale, namespace: "gi" });
  const name = pick(g.product.name, locale);
  return {
    title: `${name} · ${t("title")}`,
    description: `${name} — ${pick(g.region.name, locale)}. ${t("intro")}`,
    alternates: localeAlternates(`/gi/${slug}`, locale),
  };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale; slug: string }> }) {
  const { locale, slug } = await params;
  setRequestLocale(locale);
  const g = find(slug);
  if (!g) notFound();
  const t = await getTranslations();
  const p = g.product;
  const nameMap = getRegionNameMap();
  const others = (["en", "hi", "mr"] as const).filter((l) => l !== locale);
  const more = getAllGI()
    .filter((x) => x.region.code === g.region.code && x.product.id !== p.id)
    .sort((a, b) => cmp(pick(a.product.name, locale), pick(b.product.name, locale)))
    .slice(0, 8);
  const src = sourceName(p.sourceId);
  const regionName = pick(g.region.name, locale);
  const pending = [t("gi.pendingRegYear"), t("gi.pendingRegion"), t("gi.pendingUnique"), t("gi.pendingArtisans"), t("gi.pendingMarket")];

  return (
    <div className="mx-auto max-w-4xl px-4 py-10">
      <nav aria-label={t("common.breadcrumb")} className="breadcrumb mb-4 text-sm text-muted">
        <Link href="/">{t("nav.home")}</Link> / <Link href="/gi">{t("gi.title")}</Link> / <span>{pick(p.name, locale)}</span>
      </nav>
      <div className="rounded-2xl border border-border bg-surface p-6" style={{ borderTop: `4px solid ${g.region.accent}` }}>
        <h1 className="flex items-start gap-3 text-3xl font-bold tracking-tight">
          <Award aria-hidden className="mt-1 size-7 shrink-0" style={{ color: g.region.accent }} />
          {pick(p.name, locale)}
        </h1>
        <p className="mt-2 flex flex-wrap gap-x-3 text-muted">
          <span className="sr-only">{t("gi.names")}: </span>
          {others.map((l) => <span key={l} lang={l}>{p.name[l]}</span>)}
        </p>
        <dl className="mt-6 grid gap-4 sm:grid-cols-2">
          <div>
            <dt className="text-sm text-muted">{t("gi.categories")}</dt>
            <dd className="font-semibold">{p.categories.map((c) => t(`giCategory.${c}` as "giCategory.handicraft")).join(" · ")}</dd>
          </div>
          <div>
            <dt className="text-sm text-muted">{t("gi.listedUnder")}</dt>
            <dd className="font-semibold"><Link href={`${g.region.href}/gi`}>{regionName}</Link></dd>
          </div>
          {p.sharedWith?.length ? (
            <div>
              <dt className="text-sm text-muted">{t("gi.shared")}</dt>
              <dd>{p.sharedWith.map((n) => pick(nameMap[n] ?? { en: n }, locale)).join(", ")}</dd>
            </div>
          ) : null}
          {p.applicationNo && (
            <div>
              <dt className="text-sm text-muted">{t("gi.appNo")}</dt>
              <dd><Digits>{p.applicationNo}</Digits></dd>
            </div>
          )}
          {p.filingDate && (
            <div>
              <dt className="text-sm text-muted">{t("gi.filed")}</dt>
              <dd><Digits>{formatDate(p.filingDate, locale)}</Digits></dd>
            </div>
          )}
        </dl>
        <p className="mt-6 flex flex-wrap items-center gap-2 text-xs text-muted">
          <ConfidenceBadge level={p.confidence} />
          <span>{t("common.source")}: {src?.short ?? t("common.notAvailable")}</span>
          {p.url && (
            <a href={p.url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1">
              {t("common.verifyOfficial")} <ExternalLink aria-hidden className="size-3" />
            </a>
          )}
        </p>
        <p className="mt-1 text-xs text-muted">{t("gi.filingNote")}</p>
      </div>

      <section className="mt-6 rounded-xl border border-dashed border-border bg-surface p-5">
        <h2 className="font-semibold">{t("gi.pendingTitle")}</h2>
        <p className="mb-2 text-sm text-muted">{t("gi.pendingNote")}</p>
        <ul className="list-disc space-y-1 pl-5 text-sm">
          {pending.map((x) => <li key={x}>{x} — <span className="text-muted">{t("common.notAvailable")}</span></li>)}
        </ul>
      </section>

      {more.length > 0 && (
        <section className="mt-8">
          <h2 className="mb-3 text-xl font-semibold">{t("gi.more", { region: regionName })}</h2>
          <ul className="grid gap-2 sm:grid-cols-2">
            {more.map((m) => (
              <li key={m.product.id}><Link href={`/gi/${m.product.id}`}>{pick(m.product.name, locale)}</Link></li>
            ))}
          </ul>
          <p className="mt-3 text-sm"><Link href={`${g.region.href}/gi`}>{t("gi.seeProfile", { region: regionName })} →</Link></p>
        </section>
      )}
      <p className="mt-8 text-sm"><Link href="/gi">← {t("gi.back")}</Link></p>
      <div className="mt-8"><Disclaimer /></div>
    </div>
  );
}
