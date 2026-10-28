import type { Metadata } from "next";
import { getTranslations, setRequestLocale } from "next-intl/server";
import { Download, FileJson, FileSpreadsheet } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import { getDataAsOn, getRegions } from "@/lib/data";
import { DOWNLOADS, getDownloadSizes } from "@/lib/exports";
import { pick, cmp } from "@/lib/l10n";
import { localeAlternates } from "@/lib/seo";
import { PageHeader } from "@/components/PageHeader";
import { Digits } from "@/components/Num";

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale }> }): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "dataLibrary" });
  return { title: t("title"), description: t("intro"), alternates: localeAlternates("/data", locale) };
}

const BASE = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

function size(bytes: number, locale: Locale) {
  const kb = bytes / 1024;
  const n = kb >= 1024 ? kb / 1024 : kb;
  const unit = kb >= 1024 ? "MB" : "KB";
  return `${new Intl.NumberFormat(`${locale}-IN`, { maximumFractionDigits: n < 10 ? 1 : 0 }).format(n)} ${unit}`;
}

export default async function Page({ params }: { params: Promise<{ locale: Locale }> }) {
  const { locale } = await params;
  setRequestLocale(locale);
  const t = await getTranslations("dataLibrary");
  const sizes = getDownloadSizes();
  const regions = getRegions()
    .filter((r) => r.type !== "country")
    .sort((a, b) => cmp(pick(a.name, locale), pick(b.name, locale)));
  return (
    <div className="mx-auto max-w-5xl px-4 py-10">
      <PageHeader title={t("title")} intro={t("intro")} asOn={getDataAsOn()} />

      <section aria-labelledby="files-h">
        <h2 id="files-h" className="mb-3 text-xl font-semibold">{t("filesTitle")}</h2>
        <ul className="grid gap-3 sm:grid-cols-2">
          {DOWNLOADS.map((d) => {
            const Icon = d.kind === "csv" ? FileSpreadsheet : FileJson;
            return (
              <li key={d.file} className="flex flex-col gap-2 rounded-xl border border-border bg-surface p-4">
                <div className="flex items-start gap-2">
                  <Icon aria-hidden className="mt-0.5 size-5 shrink-0 text-muted" />
                  <div className="min-w-0">
                    <h3 className="font-semibold">{t(`files.${d.key}.title`)}</h3>
                    <p className="text-sm text-muted">{t(`files.${d.key}.body`)}</p>
                  </div>
                </div>
                <a
                  href={`${BASE}/downloads/${d.file}`}
                  download
                  className="mt-auto inline-flex w-fit items-center gap-1 rounded-md border border-border px-2.5 py-1 text-sm no-underline hover:bg-surface-2"
                >
                  <Download aria-hidden className="size-4" />
                  <span className="font-mono">{d.file}</span>
                  <span className="text-muted">· <Digits>{size(sizes[d.file], locale)}</Digits></span>
                </a>
              </li>
            );
          })}
        </ul>
      </section>

      <section aria-labelledby="profiles-h" className="mt-10">
        <h2 id="profiles-h" className="mb-1 text-xl font-semibold">{t("profilesTitle")}</h2>
        <p className="mb-3 text-sm text-muted">{t("profilesBody")}</p>
        <ul className="flex flex-wrap gap-2">
          {regions.map((r) => (
            <li key={r.code}>
              <a
                href={`${BASE}/downloads/profiles/${r.code}.json`}
                download
                className="inline-block rounded-full border border-border px-3 py-1 text-sm no-underline hover:bg-surface-2"
              >
                {pick(r.name, locale)} <span className="font-mono text-xs text-muted">{r.code}.json</span>
              </a>
            </li>
          ))}
        </ul>
      </section>

      <section aria-labelledby="use-h" className="mt-10 rounded-2xl border border-border bg-surface p-5 text-sm">
        <h2 id="use-h" className="mb-2 text-base font-semibold">{t("useTitle")}</h2>
        <ul className="flex list-disc flex-col gap-2 pl-5 text-muted">
          <li>{t("useStatus")}</li>
          <li>{t("useColumns")}</li>
          <li>{t("useLanguages")}</li>
          <li>{t("useCite")}</li>
          <li>
            {t("useTerms")}{" "}
            <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer license">
              {t("licenseLink")}
            </a>
          </li>
        </ul>
      </section>

      <section aria-labelledby="api-h" className="mt-6 rounded-2xl border border-border bg-surface p-5 text-sm">
        <h2 id="api-h" className="mb-2 text-base font-semibold">{t("apiTitle")}</h2>
        <p className="text-muted">{t("apiBody")}</p>
        <pre className="mt-3 overflow-x-auto rounded-md bg-surface-2 p-3 text-xs" lang="en" dir="ltr">
          {`${BASE}/downloads/indicators.csv\n${BASE}/downloads/profiles/IN-MH.json`}
        </pre>
      </section>
    </div>
  );
}
