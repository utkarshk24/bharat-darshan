import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import { ExternalLink } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import { getDataAsOn, getSources } from "@/lib/data";
import { localeAlternates } from "@/lib/seo";
import { Confidence } from "@/lib/schema";
import { PageHeader } from "@/components/PageHeader";
import { ConfidenceBadge } from "@/components/ConfidenceBadge";
import { Disclaimer } from "@/components/Disclaimer";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "about" });
  return { title: t("title"), description: t("intro"), alternates: localeAlternates("/about", locale) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("about");
  const sources = getSources();
  const cats = [...new Set(sources.map((s) => s.category))];
  return (
    <div className="mx-auto max-w-4xl px-4 py-10">
      <PageHeader title={t("title")} intro={t("intro")} asOn={getDataAsOn()} />
      <section className="mb-10">
        <h2 className="mb-3 text-2xl font-bold">{t("principlesTitle")}</h2>
        <ol className="list-decimal space-y-2 pl-6">
          {(["p1", "p2", "p3", "p4", "p5", "p6", "p7"] as const).map((k) => <li key={k}>{t(k)}</li>)}
        </ol>
      </section>
      <section className="mb-10">
        <h2 className="mb-3 text-2xl font-bold">{t("confidenceTitle")}</h2>
        <div className="flex flex-wrap gap-2">
          {Confidence.options.map((c) => <ConfidenceBadge key={c} level={c} className="text-sm" />)}
        </div>
      </section>
      <section className="mb-10">
        <h2 className="mb-1 text-2xl font-bold">{t("sourcesTitle")}</h2>
        <p className="mb-4 text-muted">{t("sourcesIntro")}</p>
        <div className="flex flex-col gap-6">
          {cats.map((c) => (
            <div key={c}>
              <h3 className="mb-2 font-semibold capitalize" lang="en">{c.replace(/-/g, " ")}</h3>
              <ul className="divide-y divide-border rounded-xl border border-border bg-surface" lang="en">
                {sources.filter((s) => s.category === c).sort((a, b) => a.priority - b.priority).map((s) => (
                  <li key={s.id} className="flex flex-col gap-0.5 px-4 py-3 text-sm">
                    <a href={s.url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 font-medium">
                      {s.name} <ExternalLink aria-hidden className="size-3" />
                    </a>
                    <span className="text-muted">{s.publisher}</span>
                    {s.notes && <span className="text-muted">{s.notes}</span>}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </section>
      <Disclaimer />
    </div>
  );
}
