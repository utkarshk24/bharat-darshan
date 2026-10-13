import type { MetadataRoute } from "next";
import { locales } from "@/i18n/routing";
import { getRegions } from "@/lib/data";
import { NAV } from "@/lib/nav";
import { SITE_URL } from "@/lib/seo";

export default function sitemap(): MetadataRoute.Sitemap {
  const paths = [
    ...NAV.map((n) => (n.href === "/" ? "" : n.href)),
    ...getRegions().map((r) => `/${r.type === "state" ? "states" : "uts"}/${r.slug}`),
  ];
  return paths.map((p) => ({
    url: `${SITE_URL}/en${p}`,
    changeFrequency: "weekly",
    alternates: { languages: Object.fromEntries(locales.map((l) => [`${l}-IN`, `${SITE_URL}/${l}${p}`])) },
  }));
}
