import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { getRegion, getRegions } from "@/lib/data";
import { pick } from "@/lib/l10n";
import { localeAlternates, socialMeta } from "@/lib/seo";
import { ProfilePage } from "@/components/ProfilePage";

export function generateStaticParams() {
  return getRegions().filter((r) => r.type === "state").map((r) => ({ slug: r.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale; slug: string }> }): Promise<Metadata> {
  const { locale, slug } = await params;
  const r = getRegion("state", slug);
  if (!r) return {};
  return { title: pick(r.name, locale), alternates: localeAlternates(`/states/${slug}`, locale), ...socialMeta(locale, `states-${slug}`) };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale; slug: string }> }) {
  const { locale, slug } = await params;
  setRequestLocale(locale);
  const r = getRegion("state", slug);
  if (!r) notFound();
  return <ProfilePage region={r} locale={locale} module="overview" />;
}
