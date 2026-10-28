"use client";
import { useMemo, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { Award } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { GIProduct } from "@/lib/schema";
import { pick, cmp } from "@/lib/l10n";
import { formatDate } from "@/lib/format";
import { cn } from "@/lib/cn";
import { Digits } from "../Num";

/** Visual GI product cards with category filter (Section 7S). */
export function GIGrid({ products, accent }: { products: GIProduct[]; accent: string }) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const cats = useMemo(() => [...new Set(products.flatMap((p) => p.categories))], [products]);
  const [cat, setCat] = useState<string | null>(null);
  const shown = products
    .filter((p) => !cat || p.categories.includes(cat as GIProduct["categories"][number]))
    .sort((a, b) => cmp(pick(a.name, locale), pick(b.name, locale)));

  if (!products.length) return null;
  return (
    <section>
      <p className="mb-3 text-lg font-semibold">
        <Digits>{t("common.giCount", { count: products.length })}</Digits>
      </p>
      <div role="group" aria-label={t("common.filter")} className="mb-4 flex flex-wrap gap-2 text-sm print:hidden">
        <button type="button" aria-pressed={cat === null} onClick={() => setCat(null)} className={cn("rounded-full border px-3 py-1", cat === null ? "border-navy bg-navy text-bg" : "border-border")}>
          {t("common.all")}
        </button>
        {cats.map((c) => (
          <button key={c} type="button" aria-pressed={cat === c} onClick={() => setCat(c)} className={cn("rounded-full border px-3 py-1", cat === c ? "border-navy bg-navy text-bg" : "border-border")}>
            {t(`giCategory.${c}` as "giCategory.handicraft")} ({products.filter((p) => p.categories.includes(c as GIProduct["categories"][number])).length})
          </button>
        ))}
      </div>
      <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {shown.map((p) => (
          <li key={p.id} className="flex flex-col gap-1 rounded-xl border border-border bg-surface p-3">
            <span className="flex items-start gap-2">
              <Award aria-hidden className="mt-0.5 size-4 shrink-0" style={{ color: accent }} />
              <span className="font-semibold leading-snug">{pick(p.name, locale)}</span>
            </span>
            <span className="text-xs text-muted">{p.categories.map((c) => t(`giCategory.${c}` as "giCategory.handicraft")).join(" · ")}</span>
            {p.description && <span className="text-sm">{pick(p.description, locale)}</span>}
            <span className="mt-auto pt-1 text-xs text-muted">
              {p.applicationNo && <>{t("common.giApp")} {p.applicationNo}</>}
              {p.filingDate && <> · {t("common.giFiled")} <Digits>{formatDate(p.filingDate, locale)}</Digits></>}
              {p.sharedWith?.length ? <> · {t("common.sharedWith")}: {p.sharedWith.join(", ")}</> : null}
            </span>
          </li>
        ))}
      </ul>
    </section>
  );
}
