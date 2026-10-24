import type { ZonalCouncil } from "@/lib/schema";

/**
 * Colour-blind-safe categorical palette (Okabe–Ito), Section 12.
 * Labels are always drawn on tiles and in the legend, so colour never carries meaning alone.
 */
export const ZONAL_COLORS: Record<ZonalCouncil, string> = {
  northern: "#0072B2",
  central: "#E69F00",
  eastern: "#009E73",
  western: "#D55E00",
  southern: "#CC79A7",
  "north-eastern": "#56B4E9",
  islands: "#7F7F7F",
};

export const TYPE_COLORS = { state: "#0072B2", ut: "#E69F00" } as const;

/** Pick black or white text for a hex background using WCAG relative luminance. */
export function inkFor(hex: string): string {
  const [r, g, b] = [1, 3, 5].map((i) => {
    const c = parseInt(hex.slice(i, i + 2), 16) / 255;
    return c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
  });
  const L = 0.2126 * r + 0.7152 * g + 0.0722 * b;
  // Contrast vs white = 1.05/(L+0.05); vs black = (L+0.05)/0.05. Choose the higher.
  return 1.05 / (L + 0.05) >= (L + 0.05) / 0.05 ? "#ffffff" : "#111111";
}

/**
 * Sequential ramp for data layers, low → high. Values live in globals.css (--seq-0..4) so
 * light and dark mode each use their own validated steps. Every value is also shown as
 * text in the tooltip, info card and table, so colour never carries meaning alone.
 */
export const SEQ_BLUE = ["var(--seq-0)", "var(--seq-1)", "var(--seq-2)", "var(--seq-3)", "var(--seq-4)"];
