import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { localeAlternates } from "@/lib/seo";
import { PageHeader } from "@/components/PageHeader";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "a11y" });
  return { title: t("title"), alternates: localeAlternates("/accessibility", locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("a11y");
  const items = t.raw("items") as string[];
  return (
    <div className="mx-auto max-w-3xl px-4 py-10">
      <PageHeader title={t("title")} intro={t("intro")} />
      <ul className="list-disc space-y-2 pl-6">{items.map((i) => <li key={i}>{i}</li>)}</ul>
      <h2 className="mb-2 mt-10 text-2xl font-bold">{t("contactTitle")}</h2>
      <p>{t("contactBody")}</p>
    </div>
  );
}
