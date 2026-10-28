import type { Metadata, Viewport } from "next";
import type { ReactNode } from "react";
import { notFound } from "next/navigation";
import { hasLocale, NextIntlClientProvider } from "next-intl";
import { getTranslations, setRequestLocale } from "next-intl/server";
import { routing, type Locale } from "@/i18n/routing";
import { PreferencesProvider, themeScript } from "@/components/Preferences";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { ServiceWorker } from "@/components/ServiceWorker";
import { getDataAsOn } from "@/lib/data";
import { preload } from "react-dom";
import { BASE_PATH, SITE_URL, localeAlternates, socialMeta } from "@/lib/seo";
import { coreFontCss, primaryFont } from "@/lib/fonts";
import "../globals.css";

export function generateStaticParams() {
  return routing.locales.map((locale) => ({ locale }));
}

export async function generateMetadata({ params }: { params: Promise<{ locale: string }> }): Promise<Metadata> {
  const { locale: requested } = await params;
  const locale: Locale = hasLocale(routing.locales, requested) ? requested : routing.defaultLocale;
  const t = await getTranslations({ locale, namespace: "common" });
  return {
    metadataBase: new URL(SITE_URL),
    title: { default: `${t("siteName")} — ${t("tagline")}`, template: `%s · ${t("siteName")}` },
    description: t("tagline"),
    alternates: localeAlternates("/", locale),
    ...socialMeta(locale),
  };
}

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#fbfaf7" },
    { media: "(prefers-color-scheme: dark)", color: "#0d1420" },
  ],
};

export default async function LocaleLayout({ children, params }: { children: ReactNode; params: Promise<{ locale: string }> }) {
  const { locale } = await params;
  if (!hasLocale(routing.locales, locale)) notFound();
  setRequestLocale(locale);
  const t = await getTranslations("common");
  // Start the main text font with the HTML instead of after the stylesheet.
  preload(primaryFont(BASE_PATH, locale), { as: "font", type: "font/woff2", crossOrigin: "anonymous" });

  return (
    <html lang={locale} suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
        <style dangerouslySetInnerHTML={{ __html: coreFontCss(BASE_PATH) }} />
      </head>
      <body className="min-h-screen bg-bg text-text antialiased">
        <a href="#main" className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-50 focus:rounded-md focus:bg-surface focus:px-4 focus:py-2">
          {t("skipToContent")}
        </a>
        <NextIntlClientProvider>
          <PreferencesProvider>
            <Header />
            <main id="main" tabIndex={-1} className="outline-none">
              {children}
            </main>
            <Footer asOn={getDataAsOn()} />
            <ServiceWorker />
          </PreferencesProvider>
        </NextIntlClientProvider>
      </body>
    </html>
  );
}
