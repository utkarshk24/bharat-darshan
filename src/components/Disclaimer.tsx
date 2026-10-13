import { useTranslations } from "next-intl";
import { TriangleAlert } from "lucide-react";

/** Visible disclaimer required on every data page (Principle 11). */
export function Disclaimer() {
  const t = useTranslations("common");
  return (
    <aside className="flex gap-2 rounded-lg border border-border bg-surface-2 p-3 text-sm text-muted" role="note">
      <TriangleAlert aria-hidden className="mt-0.5 size-4 shrink-0" />
      <p>{t("disclaimer")}</p>
    </aside>
  );
}
