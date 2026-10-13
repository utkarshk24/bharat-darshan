/**
 * Number and date formatting (Section 11).
 * Indian number system (lakh/crore) by default, optional Devanagari numerals.
 */
import type { Locale } from "@/i18n/routing";
import { intlTag } from "@/i18n/routing";
import type { DataPoint } from "./schema";

const DEVANAGARI = "०१२३४५६७८९";

/** Replace ASCII digits with Devanagari digits. */
export function toDevanagariDigits(s: string): string {
  return s.replace(/[0-9]/g, (d) => DEVANAGARI[Number(d)]);
}

export interface NumberOptions {
  digits?: "latin" | "devanagari";
  maximumFractionDigits?: number;
}

/** 112374333 → "11,23,74,333" (Indian grouping in every locale). */
export function formatIndianNumber(value: number, locale: Locale, opts: NumberOptions = {}): string {
  const s = new Intl.NumberFormat(intlTag[locale], {
    maximumFractionDigits: opts.maximumFractionDigits ?? 2,
    numberingSystem: "latn",
  }).format(value);
  return opts.digits === "devanagari" ? toDevanagariDigits(s) : s;
}

const SCALE_WORDS: Record<Locale, { lakh: string; crore: string; lakhCrore: string }> = {
  en: { lakh: "lakh", crore: "crore", lakhCrore: "lakh crore" },
  hi: { lakh: "लाख", crore: "करोड़", lakhCrore: "लाख करोड़" },
  mr: { lakh: "लाख", crore: "कोटी", lakhCrore: "लाख कोटी" },
};

/**
 * Compact Indian-system formatting: 112374333 → "11.24 crore".
 * Values below one lakh are written in full.
 */
export function formatCompactIndian(value: number, locale: Locale, opts: NumberOptions = {}): string {
  const w = SCALE_WORDS[locale];
  const abs = Math.abs(value);
  let num: number, word: string | null;
  if (abs >= 1e12) [num, word] = [value / 1e12, w.lakhCrore];
  else if (abs >= 1e7) [num, word] = [value / 1e7, w.crore];
  else if (abs >= 1e5) [num, word] = [value / 1e5, w.lakh];
  else [num, word] = [value, null];
  const n = formatIndianNumber(num, locale, { ...opts, maximumFractionDigits: word ? 2 : (opts.maximumFractionDigits ?? 2) });
  return word ? `${n} ${word}` : n;
}

/**
 * Rupee amounts stored in ₹ crore (MoSPI convention) → "₹36.45 lakh crore".
 */
export function formatRupeeCrore(crore: number, locale: Locale, opts: NumberOptions = {}): string {
  const w = SCALE_WORDS[locale];
  if (Math.abs(crore) >= 1e5) return `₹${formatIndianNumber(crore / 1e5, locale, { ...opts, maximumFractionDigits: 2 })} ${w.lakhCrore}`;
  return `₹${formatIndianNumber(crore, locale, opts)} ${w.crore}`;
}

const MONTHS: Record<Locale, string[]> = {
  en: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
  hi: ["जनवरी", "फ़रवरी", "मार्च", "अप्रैल", "मई", "जून", "जुलाई", "अगस्त", "सितंबर", "अक्टूबर", "नवंबर", "दिसंबर"],
  mr: ["जानेवारी", "फेब्रुवारी", "मार्च", "एप्रिल", "मे", "जून", "जुलै", "ऑगस्ट", "सप्टेंबर", "ऑक्टोबर", "नोव्हेंबर", "डिसेंबर"],
};

/**
 * ISO date (YYYY-MM-DD) → "13 October 2026" / "13 अक्टूबर 2026" / "13 ऑक्टोबर 2026".
 * Month names come from our own table rather than Intl, so server and browser
 * render identical text (ICU data differs between Node and browsers).
 */
export function formatDate(iso: string, locale: Locale, opts: NumberOptions = {}): string {
  const [y, m, d] = iso.split("-").map(Number);
  const s = `${d} ${MONTHS[locale][m - 1]} ${y}`;
  return opts.digits === "devanagari" ? toDevanagariDigits(s) : s;
}

/**
 * Period labels never mix FY and calendar years silently (Principle 4).
 * "FY2023-24" → "FY 2023-24" / "वित्त वर्ष 2023-24" / "आर्थिक वर्ष 2023-24".
 */
export function formatPeriod(period: string, locale: Locale): string {
  const fy = /^FY(\d{4}-\d{2})$/.exec(period);
  if (fy) return { en: `FY ${fy[1]}`, hi: `वित्त वर्ष ${fy[1]}`, mr: `आर्थिक वर्ष ${fy[1]}` }[locale];
  return period;
}

/**
 * Whether a change is an improvement depends on the indicator, not the direction
 * (Section 8): IMR ↓ is good, unemployment ↑ is bad.
 */
export type Polarity = "higher-is-better" | "lower-is-better" | "neutral";
export function changeTone(delta: number, polarity: Polarity): "good" | "bad" | "neutral" {
  if (delta === 0 || polarity === "neutral") return "neutral";
  const up = delta > 0;
  return (polarity === "higher-is-better") === up ? "good" : "bad";
}

/** How a value is displayed (shared by server and client components). */
export type ValueKind = "count" | "number" | "percent" | "rupeeCrore" | "rupee" | "ratio";

export function formatValue(dp: DataPoint, kind: ValueKind, locale: Locale): string | null {
  if (dp.value === null) return null;
  if (typeof dp.value === "string") return dp.value;
  const v = dp.value;
  switch (kind) {
    case "count":
      return formatCompactIndian(v, locale);
    case "percent":
      return `${formatIndianNumber(v, locale)}%`;
    case "rupeeCrore":
      return formatRupeeCrore(v, locale);
    case "rupee":
      return `₹${formatIndianNumber(v, locale, { maximumFractionDigits: 0 })}`;
    default:
      return formatIndianNumber(v, locale);
  }
}

