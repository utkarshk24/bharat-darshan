import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { getTranslations, setRequestLocale } from "next-intl/server";
import { ArrowRight } from "lucide-react";
import { locales, type Locale } from "@/i18n/routing";
import { THEMES } from "@/lib/themes";
import { getAuthoredModules, getCompare, getRegions, getSources } from "@/lib/data";
import { pick, cmp } from "@/lib/l10n";
import { formatPeriod, formatValue } from "@/lib/format";
import { localeAlternates } from "@/lib/seo";
import { Link } from "@/i18n/navigation";
import { PageHeader } from "@/components/PageHeader";
import { Digits } from "@/components/Num";
import { Disclaimer } from "@/components/Disclaimer";

export function generateStaticParams() {
  return locales.flatMap((locale) => THEMES.map((th) => ({ locale, theme: th.key })));
}

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale; theme: string }> }): Promise<Metadata> {
  const { locale, theme } = await params;
  const th = THEMES.find((x) => x.key === theme);
  if (!th) return {};
  const t = await getTranslations({ locale, namespace: "themes" });
  return { title: `${t(`names.${th.key}`)} · ${t("title")}`, description: t(`blurbs.${th.key}`), alternates: localeAlternates(`/themes/${theme}`, locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale; theme: string }> }) {
  const { locale, theme } = await params;
  setRequestLocale(locale);
  const th = THEMES.find((x) => x.key === theme);
  if (!th) notFound();
  const t = await getTranslations();
  const regions = [...getRegions()].sort((a, b) => cmp(pick(a.name, locale), pick(b.name, locale)));
  const authored = regions.filter((r) => getAuthoredModules(r.code).length > 1);
  const others = regions.filter((r) => !authored.includes(r));
  const href = (r: (typeof regions)[number]) => `/${r.type === "state" ? "states" : "uts"}/${r.slug}`;
  const compare = getCompare();
  const groups = compare ? compare.groups.filter((g) => (th.compareGroups as readonly string[]).includes(g.id)) : [];
  const cmpRegions = compare ? compare.regions.map((c) => regions.find((r) => r.code === c)!) : [];
  const short = Object.fromEntries(getSources().map((s) => [s.id, s.short]));

  return (
    <div className="mx-auto max-w-6xl px-4 py-10">
      <nav aria-label={t("common.breadcrumb")} className="mb-4 text-sm text-muted">
        <Link href="/">{t("nav.home")}</Link> / <Link href="/themes">{t("themes.title")}</Link> / <span>{t(`themes.names.${th.key}`)}</span>
      </nav>
      <PageHeader title={t(`themes.names.${th.key}`)} intro={t(`themes.blurbs.${th.key}`)}>
        {th.link && (
          <Link href={th.link} className="rounded-full border border-border px-3 py-1 text-sm">{t("themes.related")} →</Link>
        )}
      </PageHeader>

      {groups.map((g) => (
        <section key={g.id} className="mb-10">
          <h2 className="mb-3 text-xl font-semibold">{t("themes.indicators")}: {pick(g.label, locale)}</h2>
          <div className="relative overflow-x-auto rounded-xl border border-border bg-surface">
            <table className="w-full min-w-[720px] text-sm">
              <thead className="bg-surface-2">
                <tr>
                  <th scope="col" className="px-3 py-2 text-left">{t("compare.indicator")}</th>
                  {cmpRegions.map((r) => <th key={r.code} scope="col" className="px-3 py-2 text-right" style={{ borderTop: `3px solid ${r.accent}` }}>{pick(r.name, locale)}</th>)}
                  <th scope="col" className="px-3 py-2 text-right">{t("compare.india")}</th>
                </tr>
              </thead>
              <tbody>
                {g.indicators.map((ind) => {
                  const firstSrc = Object.values(ind.values).find((v) => v.sourceId)?.sourceId ?? null;
                  return (
                    <tr key={ind.id} className="border-t border-border">
                      <th scope="row" className="px-3 py-2 text-left font-medium">
                        {pick(ind.label, locale)}
                        <span className="block text-xs font-normal text-muted">
                          <Digits>{formatPeriod(ind.period, locale)}</Digits>{firstSrc ? ` · ${short[firstSrc] ?? firstSrc}` : ""}
                        </span>
                      </th>
                      {cmpRegions.map((r) => {
                        const v = ind.values[r.code];
                        const txt = v ? formatValue(v, ind.kind, locale) : null;
                        return (
                          <td key={r.code} className={`px-3 py-2 text-right tabular-nums ${txt ? "" : "text-muted"}`}>
                            {txt ? <Digits>{txt}</Digits> : t("common.notAvailable")}
                          </td>
                        );
                      })}
                      <td className="px-3 py-2 text-right tabular-nums text-muted">
                        {ind.national && formatValue(ind.national, ind.kind, locale) ? <Digits>{formatValue(ind.national, ind.kind, locale)!}</Digits> : "—"}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
          <p className="mt-2 flex flex-wrap items-center justify-between gap-2 text-xs text-muted">
            <span>{t("themes.notes")}</span>
            <Link href="/compare" className="text-sm font-medium">{t("themes.compareLink")} →</Link>
          </p>
        </section>
      ))}

      <section className="mb-10">
        <h2 className="mb-3 text-xl font-semibold">{t("themes.explore")}</h2>
        <ul className="grid gap-4 sm:grid-cols-2">
          {authored.map((r) => {
            const have = getAuthoredModules(r.code);
            return (
              <li key={r.code} className="rounded-2xl border border-border bg-surface p-5" style={{ borderTop: `4px solid ${r.accent}` }}>
                <Link href={href(r)} className="text-lg font-semibold">{pick(r.name, locale)}</Link>
                <p className="mb-2 mt-1 text-xs uppercase tracking-wide text-muted">{t("themes.sections")}</p>
                <ul className="flex flex-col gap-1.5">
                  {th.modules.filter((m) => have.includes(m)).map((m) => (
                    <li key={m}>
                      <Link href={`${href(r)}/${m}`} className="inline-flex items-center gap-1">
                        {t(`modules.${m}`)} <ArrowRight aria-hidden className="size-3.5" />
                      </Link>
                    </li>
                  ))}
                </ul>
              </li>
            );
          })}
        </ul>
      </section>

      <section className="mb-10 rounded-2xl border border-dashed border-border bg-surface p-5">
        <h2 className="mb-1 font-semibold">{t("themes.otherRegions")}</h2>
        <p className="mb-3 text-sm text-muted"><Digits>{t("themes.pending", { count: others.length })}</Digits></p>
        <ul className="flex flex-wrap gap-2 text-sm">
          {others.map((r) => (
            <li key={r.code}><Link href={href(r)} className="rounded-full border border-border px-2.5 py-0.5 no-underline hover:bg-surface-2">{pick(r.name, locale)}</Link></li>
          ))}
        </ul>
      </section>
      <Disclaimer />
    </div>
  );
}
