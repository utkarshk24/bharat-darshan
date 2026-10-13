import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { getGlossary } from "@/lib/data";
import { pick, cmp } from "@/lib/l10n";
import { localeAlternates } from "@/lib/seo";
import { PageHeader } from "@/components/PageHeader";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "glossary" });
  return { title: t("title"), description: t("intro"), alternates: localeAlternates("/glossary", locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations();
  const entries = [...getGlossary()].sort((a, b) => cmp(pick(a.term, locale), pick(b.term, locale)));
  const others = (["en", "hi", "mr"] as const).filter((l) => l !== locale);
  return (
    <div className="mx-auto max-w-4xl px-4 py-10">
      <PageHeader title={t("glossary.title")} intro={t("glossary.intro")} />
      <dl className="flex flex-col gap-4">
        {entries.map((g) => {
          const draft = locale !== "en" && g.definition._status?.[locale] === "draft";
          return (
            <div key={g.id} id={g.id} className="scroll-mt-24 rounded-xl border border-border bg-surface p-5">
              <dt>
                <span className="text-xl font-semibold">{pick(g.term, locale)}</span>
                {g.abbreviation && <span className="ml-2 text-muted">({g.abbreviation})</span>}
                <span className="mt-1 flex flex-wrap gap-x-3 text-sm text-muted">
                  {others.map((l) => <span key={l} lang={l}>{g.term[l]}</span>)}
                </span>
              </dt>
              <dd className="mt-3">{pick(g.definition, locale)}</dd>
              {draft && <dd className="mt-2 text-xs text-saffron-ink">{t("common.translationDraft")}</dd>}
            </div>
          );
        })}
      </dl>
    </div>
  );
}
