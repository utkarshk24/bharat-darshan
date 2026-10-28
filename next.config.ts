import type { NextConfig } from "next";
import createNextIntlPlugin from "next-intl/plugin";

const withNextIntl = createNextIntlPlugin("./src/i18n/request.ts");

/**
 * STATIC_EXPORT=1 builds a plain static site into out/ (GitHub Pages; see scripts/pages/build-pages.mjs).
 * Redirects and the locale-detecting proxy need a server, so the Pages build replaces them with
 * small static redirect pages instead.
 */
const staticExport = process.env.STATIC_EXPORT === "1";
const basePath = process.env.NEXT_PUBLIC_BASE_PATH || undefined;

const nextConfig: NextConfig = {
  reactStrictMode: true,
  poweredByHeader: false,
  // Security advisories only: reminders recommend a patch release when the installed Next.js is affected.
  experimental: { agentUpgrade: "security" },
  ...(staticExport
    ? { output: "export" as const, trailingSlash: true, images: { unoptimized: true }, basePath }
    : {
        basePath,
        /** Renamed regions keep their old addresses working (Kerala → Keralam, 25 Aug 2026). */
        async redirects() {
          return [
            { source: "/:locale(en|hi|mr)/states/kerala/:path*", destination: "/:locale/states/keralam/:path*", permanent: true },
            { source: "/states/kerala/:path*", destination: "/states/keralam/:path*", permanent: true },
          ];
        },
      }),
};

export default withNextIntl(nextConfig);
