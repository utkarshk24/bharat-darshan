import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { getAllProjects, getDataAsOn, getSources } from "@/lib/data";
import { localeAlternates } from "@/lib/seo";
import { PageHeader } from "@/components/PageHeader";
import { Disclaimer } from "@/components/Disclaimer";
import { ProjectsDashboard } from "@/components/projects/ProjectsDashboard";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "projects" });
  return { title: t("title"), description: t("intro"), alternates: localeAlternates("/projects", locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("projects");
  const items = getAllProjects();
  const regions = new Set(items.map((i) => i.region.code)).size;
  const sourceLabels = Object.fromEntries(getSources().map((s) => [s.id, s.short]));
  return (
    <div className="mx-auto max-w-6xl px-4 py-10">
      <PageHeader title={t("title")} intro={t("intro")} asOn={getDataAsOn()} />
      <p className="mb-6 rounded-xl border border-dashed border-border bg-surface p-4 text-sm text-muted">
        {t("coverage", { count: items.length, regions })} {t("neutral")}
      </p>
      <ProjectsDashboard items={items} sourceLabels={sourceLabels} />
      <ul className="mt-8 list-disc space-y-1 pl-5 text-sm text-muted">
        <li>{t("mapPending")}</li>
        <li>{t("visionPending")}</li>
      </ul>
      <div className="mt-8"><Disclaimer /></div>
    </div>
  );
}
