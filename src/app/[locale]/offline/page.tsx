import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { PageHeader } from "@/components/PageHeader";
import { SavedPages } from "@/components/SavedPages";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "offline" });
  return { title: t("title"), robots: { index: false } };
}

/** Shown by the service worker when a page is requested offline and no saved copy exists. */
export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("offline");
  return (
    <div className="mx-auto max-w-3xl px-4 py-10">
      <PageHeader title={t("title")} intro={t("intro")} />
      <SavedPages />
      <p className="mt-6 text-sm text-muted">{t("note")}</p>
    </div>
  );
}
