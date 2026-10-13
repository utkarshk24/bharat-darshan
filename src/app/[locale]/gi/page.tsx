import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import { ExternalLink } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import { getAllGI, getDataAsOn, getRegionNameMap } from "@/lib/data";
import { localeAlternates } from "@/lib/seo";
import { PageHeader } from "@/components/PageHeader";
import { Disclaimer } from "@/components/Disclaimer";
import { GIDirectory } from "@/components/gi/GIDirectory";

const GI_PDF = "https://ipindia.gov.in/frontend/pdf/gi/registered/State_wise_Registered_GI_of_India.pdf";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "gi" });
  return { title: t("title"), description: t("intro"), alternates: localeAlternates("/gi", locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("gi");
  const all = getAllGI();
  const regions = new Set(all.map((g) => g.region.code)).size;
  return (
    <div className="mx-auto max-w-6xl px-4 py-10">
      <PageHeader title={t("title")} intro={t("intro")} asOn={getDataAsOn()}>
        <a href={GI_PDF} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 rounded-full border border-border px-3 py-1 text-sm">
          {t("registry")} <ExternalLink aria-hidden className="size-3.5" />
        </a>
      </PageHeader>
      <p className="mb-6 rounded-xl border border-dashed border-border bg-surface p-4 text-sm text-muted">
        {t("coverage", { regions, total: all.length })}
      </p>
      <GIDirectory items={all} nameMap={getRegionNameMap()} />
      <p className="mt-4 text-xs text-muted">{t("filingNote")}</p>
      <div className="mt-10">
        <Disclaimer />
      </div>
    </div>
  );
}
