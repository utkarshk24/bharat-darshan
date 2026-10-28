import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { getTranslations, setRequestLocale } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import { getRegion, getRegions } from "@/lib/data";
import { pick } from "@/lib/l10n";
import { localeAlternates } from "@/lib/seo";
import { ProfilePrint } from "@/components/ProfilePrint";

export function generateStaticParams() {
  return getRegions().filter((r) => r.type === "ut").map((r) => ({ slug: r.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ locale: Locale; slug: string }> }): Promise<Metadata> {
  const { locale, slug } = await params;
  const r = getRegion("ut", slug);
  if (!r) return {};
  const t = await getTranslations({ locale, namespace: "print" });
  // Same content as the profile: kept out of search results, canonical points to the profile.
  const alt = localeAlternates(`/uts/${slug}`, locale);
  return { title: t("title", { region: pick(r.name, locale) }), robots: { index: false, follow: true }, alternates: { canonical: alt?.canonical } };
}

export default async function Page({ params }: { params: Promise<{ locale: Locale; slug: string }> }) {
  const { locale, slug } = await params;
  setRequestLocale(locale);
  const r = getRegion("ut", slug);
  if (!r) notFound();
  return <ProfilePrint region={r} locale={locale} />;
}
