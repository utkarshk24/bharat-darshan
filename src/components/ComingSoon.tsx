import { useTranslations } from "next-intl";
import { Hammer } from "lucide-react";
import { Link } from "@/i18n/navigation";

/** Placeholder for a destination that lands in a later phase. States the phase; shows no fake data. */
export function ComingSoon({ title, phase }: { title: string; phase: number }) {
  const t = useTranslations("common");
  const phaseLabel = t("phase", { n: phase });
  return (
    <section className="mx-auto max-w-3xl px-4 py-16">
      <h1 className="text-3xl font-bold">{title}</h1>
      <div className="mt-6 flex gap-3 rounded-xl border border-dashed border-border bg-surface p-6">
        <Hammer aria-hidden className="mt-1 size-5 shrink-0 text-saffron-ink" />
        <div>
          <p className="font-semibold">{t("comingSoonTitle", { phase: phaseLabel })}</p>
          <p className="mt-1 text-muted">{t("comingSoonBody")}</p>
          <Link href="/" className="mt-4 inline-block">
            {t("backHome")}
          </Link>
        </div>
      </div>
    </section>
  );
}
