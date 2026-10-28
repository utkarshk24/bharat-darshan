import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { localeAlternates } from "@/lib/seo";
import { tripRegions } from "@/lib/trip";
import { PageHeader } from "@/components/PageHeader";
import { Disclaimer } from "@/components/Disclaimer";
import { TripPlanner } from "@/components/trip/TripPlanner";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "trip" });
  return { title: t("title"), description: t("intro"), alternates: localeAlternates("/trip-planner", locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("trip");
  return (
    <div className="mx-auto max-w-4xl px-4 py-10">
      <PageHeader title={t("title")} intro={t("intro")} />
      <TripPlanner regions={tripRegions()} />
      <section className="mt-10 rounded-2xl border border-border bg-surface p-5 text-sm">
        <h2 className="mb-2 text-base font-semibold">{t("method")}</h2>
        <p className="text-muted">{t("methodBody")}</p>
      </section>
      <div className="mt-8"><Disclaimer /></div>
    </div>
  );
}
