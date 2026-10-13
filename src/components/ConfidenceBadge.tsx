import { useTranslations } from "next-intl";
import { BadgeCheck, Calculator, ShieldCheck, PenLine } from "lucide-react";
import type { Confidence } from "@/lib/schema";
import { cn } from "@/lib/cn";

const STYLE: Record<Confidence, { color: string; Icon: typeof BadgeCheck }> = {
  Official: { color: "var(--badge-official)", Icon: BadgeCheck },
  "Official estimate/projection": { color: "var(--badge-estimate)", Icon: Calculator },
  "Third-party verified": { color: "var(--badge-third)", Icon: ShieldCheck },
  Editorial: { color: "var(--badge-editorial)", Icon: PenLine },
};

/** Confidence level tag (Principle 2). Icon + text, so colour never carries meaning alone. */
export function ConfidenceBadge({ level, className }: { level: Confidence; className?: string }) {
  const t = useTranslations("confidence");
  const { color, Icon } = STYLE[level];
  return (
    <span
      className={cn("inline-flex items-center gap-1 rounded-full border px-2 py-0.5 text-xs font-medium", className)}
      style={{ color, borderColor: color }}
    >
      <Icon aria-hidden className="size-3.5" />
      {t(level)}
    </span>
  );
}
