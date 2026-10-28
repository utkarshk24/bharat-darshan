import type { MetadataRoute } from "next";
import { BASE_PATH } from "@/lib/seo";

export const dynamic = "force-static";

/** Installable app (offline support comes from /sw.js). */
export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Bharat Darshan · भारत दर्शन",
    short_name: "Bharat Darshan",
    description: "Encyclopedia, atlas & data dashboard of India's States and Union Territories, in English, Hindi and Marathi.",
    start_url: `${BASE_PATH}/`,
    scope: `${BASE_PATH}/`,
    display: "standalone",
    background_color: "#fbfaf7",
    theme_color: "#0b2545",
    lang: "en",
    icons: [
      { src: `${BASE_PATH}/icons/icon-192.png`, sizes: "192x192", type: "image/png" },
      { src: `${BASE_PATH}/icons/icon-512.png`, sizes: "512x512", type: "image/png" },
      { src: `${BASE_PATH}/icons/maskable-512.png`, sizes: "512x512", type: "image/png", purpose: "maskable" },
    ],
  };
}
