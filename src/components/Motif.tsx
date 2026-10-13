import { useId } from "react";
import type { Region } from "@/lib/schema";

type MotifKey = Region["motif"];

/**
 * Subtle line patterns inspired by regional art forms (Section 12), drawn from scratch
 * as simple geometry — not reproductions of any artwork. Purely decorative (aria-hidden).
 */
const PATTERNS: Record<MotifKey, { size: number; body: (c: string) => React.ReactNode }> = {
  kolam: {
    size: 24,
    body: (c) => (
      <>
        <circle cx="12" cy="12" r="1.4" fill={c} />
        <path d="M12 4 Q20 4 20 12 Q20 20 12 20 Q4 20 4 12 Q4 4 12 4" fill="none" stroke={c} strokeWidth="0.8" />
      </>
    ),
  },
  warli: {
    size: 22,
    body: (c) => (
      <>
        <path d="M6 4 L16 4 L11 11 Z M11 11 L6 18 L16 18 Z" fill="none" stroke={c} strokeWidth="0.9" />
        <circle cx="11" cy="2" r="1.3" fill={c} />
      </>
    ),
  },
  madhubani: {
    size: 20,
    body: (c) => (
      <path d="M0 10 Q5 2 10 10 Q15 2 20 10 M0 16 Q5 8 10 16 Q15 8 20 16" fill="none" stroke={c} strokeWidth="0.8" />
    ),
  },
  pattachitra: {
    size: 24,
    body: (c) => (
      <>
        <path d="M12 3 Q16 9 12 15 Q8 9 12 3 Z" fill="none" stroke={c} strokeWidth="0.8" />
        <path d="M3 20 H21" stroke={c} strokeWidth="0.8" />
      </>
    ),
  },
  ikat: {
    size: 20,
    body: (c) => <path d="M10 1 L19 10 L10 19 L1 10 Z M10 6 L14 10 L10 14 L6 10 Z" fill="none" stroke={c} strokeWidth="0.8" />,
  },
  jaali: {
    size: 22,
    body: (c) => <path d="M7 1 H15 L21 7 V15 L15 21 H7 L1 15 V7 Z" fill="none" stroke={c} strokeWidth="0.8" />,
  },
};

export function Motif({ motif, color, opacity = 0.14, className }: { motif: MotifKey; color: string; opacity?: number; className?: string }) {
  const id = useId().replace(/:/g, "");
  const p = PATTERNS[motif];
  return (
    <svg aria-hidden className={className} width="100%" height="100%" style={{ opacity }}>
      <defs>
        <pattern id={`m${id}`} width={p.size} height={p.size} patternUnits="userSpaceOnUse">
          {p.body(color)}
        </pattern>
      </defs>
      <rect width="100%" height="100%" fill={`url(#m${id})`} />
    </svg>
  );
}

/** Thin decorative section divider using the same motif. */
export function MotifDivider({ motif, color }: { motif: MotifKey; color: string }) {
  return (
    <div aria-hidden className="my-8 h-6 w-full">
      <Motif motif={motif} color={color} opacity={0.35} />
    </div>
  );
}
