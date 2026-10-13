import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import { ArrowRight } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import { THEMES } from "@/lib/themes";
import { localeAlternates } from "@/lib/seo";
import { Link } from "@/i18n/navigation";
import { PageHeader } from "@/components/PageHeader";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "themes" });
  return { title: t("title"), description: t("intro"), alternates: localeAlternates("/themes", locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations();
  return (
    <div className="mx-auto max-w-6xl px-4 py-10">
      <PageHeader title={t("themes.title")} intro={t("themes.intro")} />
      <ul className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {THEMES.map((th) => (
          <li key={th.key}>
            <Link href={`/themes/${th.key}`} className="flex h-full flex-col gap-2 rounded-2xl border border-border bg-surface p-5 text-text no-underline hover:shadow-md">
              <span className="flex items-center justify-between text-lg font-semibold">
                {t(`themes.names.${th.key}`)} <ArrowRight aria-hidden className="size-4 text-muted" />
              </span>
              <span className="text-sm text-muted">{t(`themes.blurbs.${th.key}`)}</span>
              <span className="mt-auto flex flex-wrap gap-1 pt-2">
                {th.modules.map((m) => (
                  <span key={m} className="rounded-full bg-surface-2 px-2 py-0.5 text-xs">{t(`modules.${m}`)}</span>
                ))}
              </span>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
