"use client";
import { ArrowDownRight, ArrowUpRight, Minus } from "lucide-react";
import { useLocale } from "next-intl";
import { changeTone, formatIndianNumber, type Polarity } from "@/lib/format";
import type { Locale } from "@/i18n/routing";
import { Digits } from "./Num";

/**
 * Change badge coloured by whether the change is an improvement, not by direction (Section 8).
 * The arrow shows direction; colour + an sr-only word shows good/bad.
 */
export function TrendBadge({ delta, unit, polarity, label }: { delta: number; unit: string; polarity: Polarity; label?: string }) {
  const locale = useLocale() as Locale;
  const tone = changeTone(delta, polarity);
  const Icon = delta > 0 ? ArrowUpRight : delta < 0 ? ArrowDownRight : Minus;
  const color = tone === "good" ? "var(--good)" : tone === "bad" ? "var(--bad)" : "var(--neutral)";
  const sign = delta > 0 ? "+" : delta < 0 ? "−" : "";
  return (
    <span className="inline-flex items-center gap-0.5 text-xs font-semibold" style={{ color }}>
      <Icon aria-hidden className="size-3.5" />
      <Digits>{`${sign}${formatIndianNumber(Math.abs(delta), locale)}${unit}`}</Digits>
      <span className="sr-only">{label ?? tone}</span>
    </span>
  );
}
