import { FALLBACKS, type Locale } from "@/i18n/routing";
import type { Localized } from "./schema";

/** Pick a translatable string in the current locale, following the fallback chain (mr → hi → en). */
export function pick(value: Localized | null | undefined, locale: Locale): string {
  if (!value) return "";
  const v = value as unknown as Record<string, string | undefined>;
  if (v[locale]?.trim()) return v[locale]!;
  for (const f of FALLBACKS[locale] ?? []) if (v[f]?.trim()) return v[f]!;
  return v.en ?? "";
}

/** True if the shown text came from a fallback locale (so the UI can mark it). */
export function isFallback(value: Localized | null | undefined, locale: Locale): boolean {
  if (!value) return false;
  return !(value as unknown as Record<string, string>)[locale]?.trim();
}

/**
 * Deterministic string comparison for sorting localized names. Avoids
 * locale-aware collation, which can differ between the server's and the
 * browser's ICU data and cause hydration mismatches. Devanagari code points
 * follow varnamala order closely enough for lists.
 */
export function cmp(a: string, b: string): number {
  const x = a.toLowerCase(), y = b.toLowerCase();
  return x < y ? -1 : x > y ? 1 : 0;
}
