import { defineRouting } from "next-intl/routing";

/**
 * Locale registry. To add a 4th (regional) language later, add it here,
 * add messages/<code>.json, and extend `Localized` in src/lib/schema.ts
 * with an optional key. Content falls back per FALLBACKS below.
 */
export const locales = ["en", "hi", "mr"] as const;
export type Locale = (typeof locales)[number];

/** Fallback chain used when a content field is missing in a locale (Section 11). */
export const FALLBACKS: Record<string, string[]> = {
  en: [],
  hi: ["en"],
  mr: ["hi", "en"],
};

/** BCP-47 tags for Intl formatting and the html lang attribute. */
export const intlTag: Record<Locale, string> = { en: "en-IN", hi: "hi-IN", mr: "mr-IN" };

export const routing = defineRouting({
  locales,
  defaultLocale: "en",
  localePrefix: "always",
  // The locale cookie (NEXT_LOCALE) makes the user's choice persist across visits.
  localeCookie: { maxAge: 60 * 60 * 24 * 365 },
  alternateLinks: true,
});
