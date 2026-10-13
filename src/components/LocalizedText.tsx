import type { Locale } from "@/i18n/routing";
import type { Localized } from "@/lib/schema";
import { pick, isFallback } from "@/lib/l10n";
import { FALLBACKS } from "@/i18n/routing";

/**
 * Renders a translatable field in the current locale. If it falls back to another
 * language, the element gets the correct `lang` attribute for screen readers.
 */
export function LocalizedText({ value, locale, as: Tag = "span", className }: {
  value: Localized | null | undefined;
  locale: Locale;
  as?: "span" | "p" | "h1" | "h2" | "h3" | "div";
  className?: string;
}) {
  if (!value) return null;
  const text = pick(value, locale);
  let lang: string = locale;
  if (isFallback(value, locale)) {
    lang = (FALLBACKS[locale] ?? []).find((f) => (value as unknown as Record<string, string>)[f]?.trim()) ?? "en";
  }
  return (
    <Tag className={className} lang={lang !== locale ? lang : undefined}>
      {text}
    </Tag>
  );
}
