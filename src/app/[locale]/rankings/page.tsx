import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { getCompare, getRegions, getSources } from "@/lib/data";
import { localeAlternates } from "@/lib/seo";
import { PageHeader } from "@/components/PageHeader";
import { Disclaimer } from "@/components/Disclaimer";
import { RankingsView, type RankRegion } from "@/components/rankings/RankingsView";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "rankings" });
  return { title: t("title"), description: t("intro"), alternates: localeAlternates("/rankings", locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("rankings");
  const data = getCompare();
  if (!data) notFound();
  const all = getRegions();
  const regions: RankRegion[] = data.regions.map((code) => {
    const r = all.find((x) => x.code === code)!;
    return { code, name: r.name, accent: r.accent, type: r.type === "ut" ? "ut" : "state", href: `/${r.type === "state" ? "states" : "uts"}/${r.slug}` };
  });
  const sourceLabels = Object.fromEntries(getSources().map((s) => [s.id, s.short]));
  return (
    <div className="mx-auto max-w-5xl px-4 py-10">
      <PageHeader title={t("title")} intro={t("intro")} asOn={data.asOf} />
      <RankingsView data={data} regions={regions} sourceLabels={sourceLabels} />
      <section className="mt-10 rounded-2xl border border-border bg-surface p-5 text-sm">
        <h2 className="mb-2 text-base font-semibold">{t("method")}</h2>
        <p className="text-muted">{t("methodBody")}</p>
      </section>
      <div className="mt-8">
        <Disclaimer />
      </div>
    </div>
  );
}
