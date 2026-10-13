import type { Metadata } from "next";
import { notFound, redirect } from "next/navigation";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { getRegion, getRegions } from "@/lib/data";
import { pick } from "@/lib/l10n";
import { MODULES, type ModuleKey } from "@/lib/nav";
import { localeAlternates, socialMeta } from "@/lib/seo";
import { ProfilePage } from "@/components/ProfilePage";

export function generateStaticParams() {
  return getRegions()
    .filter((r) => r.type === "state")
    .flatMap((r) => MODULES.filter((m) => m !== "overview").map((module) => ({ slug: r.slug, module })));
}

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale; slug: string; module: string }> }): Promise<Metadata> {
  const { locale, slug, module } = await params;
  const r = getRegion("state", slug);
  if (!r || !(MODULES as readonly string[]).includes(module)) return {};
  const t = await getTranslations({ locale, namespace: "modules" });
  return { title: `${t(module as ModuleKey)} — ${pick(r.name, locale)}`, alternates: localeAlternates(`/states/${slug}/${module}`, locale), ...socialMeta(locale, `states-${slug}`) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale; slug: string; module: string }> }) {
  const { locale, slug, module } = await params;
  setRequestLocale(locale);
  const r = getRegion("state", slug);
  if (!r || !(MODULES as readonly string[]).includes(module)) notFound();
  if (module === "overview") redirect(`/${locale}/states/${slug}`);
  return <ProfilePage region={r} locale={locale} module={module as ModuleKey} />;
}
