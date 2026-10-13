import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { getIndia, getModule } from "@/lib/data";
import { localeAlternates, socialMeta } from "@/lib/seo";
import { PageHeader } from "@/components/PageHeader";
import { ModuleBlocks } from "@/components/blocks/ModuleBlocks";
import { Disclaimer } from "@/components/Disclaimer";
import { Link } from "@/i18n/navigation";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale });
  return { title: t("nav.india"), description: t("home.indiaIntro"), alternates: localeAlternates("/india", locale), ...socialMeta(locale, "india") };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations();
  const india = getIndia();
  const content = getModule("IN", "overview");
  if (!content) notFound();
  return (
    <div className="mx-auto max-w-6xl px-4 py-10">
      <PageHeader title={t("nav.india")} intro={t("home.indiaIntro")} asOn={content.asOf}>
        {locale !== "en" && <span className="text-xs text-muted">{t("common.translationDraft")}</span>}
        <Link href="/compare" className="rounded-full border border-border px-3 py-1 text-sm">{t("nav.compare")} →</Link>
      </PageHeader>
      <ModuleBlocks blocks={content.blocks} region={india} locale={locale} />
      <div className="mt-10">
        <Disclaimer />
      </div>
    </div>
  );
}
