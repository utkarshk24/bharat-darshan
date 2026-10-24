import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { getDataAsOn, getSummaries } from "@/lib/data";
import { localeAlternates } from "@/lib/seo";
import { PageHeader } from "@/components/PageHeader";
import { IndiaMap } from "@/components/map/IndiaMap";
import { Disclaimer } from "@/components/Disclaimer";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "nav" });
  return { title: t("map"), alternates: localeAlternates("/map", locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations();
  return (
    <div className="mx-auto max-w-7xl px-4 py-10">
      <PageHeader title={t("atlas.heroTitle")} intro={t("atlas.heroSub")} asOn={getDataAsOn()} />
      <IndiaMap regions={getSummaries()} />
      <div className="mt-10"><Disclaimer /></div>
    </div>
  );
}
