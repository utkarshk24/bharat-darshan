import type { NextConfig } from "next";
import createNextIntlPlugin from "next-intl/plugin";

const withNextIntl = createNextIntlPlugin("./src/i18n/request.ts");

const nextConfig: NextConfig = {
  reactStrictMode: true,
  poweredByHeader: false,
  /** Renamed regions keep their old addresses working (Kerala → Keralam, 25 Aug 2026). */
  async redirects() {
    return [
      { source: "/:locale(en|hi|mr)/states/kerala/:path*", destination: "/:locale/states/keralam/:path*", permanent: true },
      { source: "/states/kerala/:path*", destination: "/states/keralam/:path*", permanent: true },
    ];
  },
};

export default withNextIntl(nextConfig);
