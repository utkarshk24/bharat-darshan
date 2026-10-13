import { useTranslations } from "next-intl";
import { Hammer } from "lucide-react";

export function ComingSoonInline({ title, phase = 2 }: { title: string; phase?: number }) {
  const t = useTranslations("common");
  return (
    <section>
      <h2 className="text-2xl font-bold">{title}</h2>
      <div className="mt-4 flex gap-3 rounded-xl border border-dashed border-border bg-surface p-6">
        <Hammer aria-hidden className="mt-1 size-5 shrink-0 text-saffron-ink" />
        <div>
          <p className="font-semibold">{t("comingSoonTitle", { phase: t("phase", { n: phase }) })}</p>
          <p className="mt-1 text-muted">{t("comingSoonBody")}</p>
        </div>
      </div>
    </section>
  );
}
