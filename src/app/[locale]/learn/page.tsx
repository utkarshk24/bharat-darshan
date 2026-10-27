import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { getDataAsOn } from "@/lib/data";
import { localeAlternates } from "@/lib/seo";
import { PageHeader } from "@/components/PageHeader";
import { QuizView } from "@/components/learn/QuizView";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "learn" });
  return { title: t("title"), description: t("intro"), alternates: localeAlternates("/learn", locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("learn");
  return (
    <div className="mx-auto max-w-3xl px-4 py-10">
      <PageHeader title={t("title")} intro={t("intro")} asOn={getDataAsOn()} />
      <QuizView />
      <section className="mt-10 rounded-2xl border border-border bg-surface p-5 text-sm">
        <h2 className="mb-2 text-base font-semibold">{t("method")}</h2>
        <p className="text-muted">{t("methodBody")}</p>
      </section>
    </div>
  );
}
