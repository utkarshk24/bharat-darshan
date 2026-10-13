"use client";
import { useLocale } from "next-intl";
import { usePreferences } from "./Preferences";
import { toDevanagariDigits } from "@/lib/format";

/** Renders any already-formatted string, converting digits if the user chose Devanagari numerals. */
export function Digits({ children }: { children: string }) {
  const { digits } = usePreferences();
  return <>{digits === "devanagari" ? toDevanagariDigits(children) : children}</>;
}

export function useDigitsPref() {
  const { digits } = usePreferences();
  const locale = useLocale();
  return { digits, locale };
}
