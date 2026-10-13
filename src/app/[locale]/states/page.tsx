import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { getDataAsOn, getSummaries } from "@/lib/data";
import { localeAlternates } from "@/lib/seo";
import { PageHeader } from "@/components/PageHeader";
import { RegionGrid } from "@/components/RegionGrid";
import { Disclaimer } from "@/components/Disclaimer";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "list" });
  return { title: t("statesTitle"), description: t("statesIntro"), alternates: localeAlternates("/states", locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("list");
  const regions = getSummaries().filter((r) => r.type === "state");
  return (
    <div className="mx-auto max-w-7xl px-4 py-10">
      <PageHeader title={t("statesTitle")} intro={t("statesIntro")} asOn={getDataAsOn()} />
      <RegionGrid regions={regions} initialType="state" showTypeFilter={false} />
      <div className="mt-10"><Disclaimer /></div>
    </div>
  );
}
