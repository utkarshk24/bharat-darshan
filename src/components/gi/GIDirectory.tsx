"use client";
import { useMemo, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { Award, Search } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { GIProduct, Localized } from "@/lib/schema";
import { pick, cmp } from "@/lib/l10n";
import { formatDate } from "@/lib/format";
import { phoneticKey } from "@/lib/translit";
import { cn } from "@/lib/cn";
import { Link } from "@/i18n/navigation";
import { Digits } from "../Num";

export interface GIItem {
  product: GIProduct;
  region: { code: string; name: Localized; href: string; accent: string };
}

const CATS: GIProduct["categories"][number][] = ["agricultural", "handicraft", "textile", "foodstuff", "manufactured", "natural"];

/** National GI directory: search across scripts, category and region filters, two sort orders. */
export function GIDirectory({ items, nameMap }: { items: GIItem[]; nameMap: Record<string, Localized> }) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const [q, setQ] = useState("");
  const [cat, setCat] = useState<string | null>(null);
  const [reg, setReg] = useState<string | null>(null);
  const [sort, setSort] = useState<"name" | "date">("name");

  const index = useMemo(
    () =>
      items.map((it) => {
        const names = [it.product.name.en, it.product.name.hi, it.product.name.mr].filter(Boolean) as string[];
        return { it, text: names.join(" ").toLowerCase(), keys: names.map(phoneticKey) };
      }),
    [items],
  );
  const regions = useMemo(() => {
    const m = new Map<string, GIItem["region"]>();
    items.forEach((i) => m.set(i.region.code, i.region));
    return [...m.values()];
  }, [items]);

  const query = q.trim().toLowerCase();
  const qk = query ? phoneticKey(query) : "";
  const base = index
    .filter(({ it }) => !reg || it.region.code === reg)
    .filter(({ text, keys }) => !query || text.includes(query) || (qk.length > 1 && keys.some((k) => k.includes(qk))));
  const shown = base
    .filter(({ it }) => !cat || it.product.categories.includes(cat as GIProduct["categories"][number]))
    .map(({ it }) => it)
    .sort((a, b) =>
      sort === "date"
        ? (b.product.filingDate ?? "").localeCompare(a.product.filingDate ?? "") || cmp(pick(a.product.name, locale), pick(b.product.name, locale))
        : cmp(pick(a.product.name, locale), pick(b.product.name, locale)),
    );
  const catCount = (c: string) => base.filter(({ it }) => it.product.categories.includes(c as GIProduct["categories"][number])).length;

  const chip = (on: boolean) => cn("rounded-full border px-3 py-1", on ? "border-navy bg-navy text-bg font-semibold" : "border-border hover:bg-surface-2");

  return (
    <div className="flex min-w-0 flex-col gap-5">
      <div className="flex flex-col gap-4 rounded-2xl border border-border bg-surface p-4">
        <label className="flex flex-col gap-1 text-sm font-semibold">
          {t("gi.search")}
          <span className="relative">
            <Search aria-hidden className="pointer-events-none absolute left-3 top-1/2 size-4 -translate-y-1/2 text-muted" />
            <input
              type="search"
              value={q}
              onChange={(e) => setQ(e.target.value)}
              placeholder={t("gi.searchPlaceholder")}
              className="w-full rounded-lg border border-border bg-bg py-2 pl-9 pr-3 font-normal"
            />
          </span>
        </label>
        <div>
          <p id="gi-cat" className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted">{t("gi.category")}</p>
          <div role="group" aria-labelledby="gi-cat" className="flex flex-wrap gap-2 text-sm">
            <button type="button" aria-pressed={cat === null} onClick={() => setCat(null)} className={chip(cat === null)}>
              {t("common.all")} (<Digits>{String(base.length)}</Digits>)
            </button>
            {CATS.filter((c) => catCount(c) > 0).map((c) => (
              <button key={c} type="button" aria-pressed={cat === c} onClick={() => setCat(c)} className={chip(cat === c)}>
                {t(`giCategory.${c}` as "giCategory.handicraft")} (<Digits>{String(catCount(c))}</Digits>)
              </button>
            ))}
          </div>
        </div>
        <div className="flex flex-wrap items-end gap-4">
          <div>
            <p id="gi-reg" className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted">{t("gi.region")}</p>
            <div role="group" aria-labelledby="gi-reg" className="flex flex-wrap gap-2 text-sm">
              <button type="button" aria-pressed={reg === null} onClick={() => setReg(null)} className={chip(reg === null)}>{t("gi.allRegions")}</button>
              {regions.map((r) => (
                <button key={r.code} type="button" aria-pressed={reg === r.code} onClick={() => setReg(r.code)} className={chip(reg === r.code)}>
                  {pick(r.name, locale)}
                </button>
              ))}
            </div>
          </div>
          <div className="ml-auto">
            <p id="gi-sort" className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted">{t("gi.sort")}</p>
            <div role="radiogroup" aria-labelledby="gi-sort" className="flex overflow-hidden rounded-md border border-border text-sm">
              {(["name", "date"] as const).map((s) => (
                <button key={s} type="button" role="radio" aria-checked={sort === s} onClick={() => setSort(s)} className={cn("px-3 py-1", sort === s ? "bg-navy text-bg font-semibold" : "hover:bg-surface-2")}>
                  {s === "name" ? t("gi.sortName") : t("gi.sortDate")}
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>

      <p className="text-sm text-muted" aria-live="polite">
        <Digits>{t("gi.count", { shown: shown.length, total: items.length })}</Digits>
      </p>

      {shown.length === 0 ? (
        <p className="rounded-xl border border-dashed border-border bg-surface p-6 text-muted">{t("gi.none")}</p>
      ) : (
        <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {shown.map(({ product: p, region }) => (
            <li key={`${region.code}-${p.id}`}>
              <Link
                href={`/gi/${p.id}`}
                className="flex h-full flex-col gap-1.5 rounded-xl border border-border bg-surface p-4 text-text no-underline hover:shadow-md"
                style={{ borderTop: `3px solid ${region.accent}` }}
              >
                <span className="flex items-start gap-2">
                  <Award aria-hidden className="mt-0.5 size-4 shrink-0" style={{ color: region.accent }} />
                  <span className="font-semibold leading-snug">{pick(p.name, locale)}</span>
                </span>
                <span className="text-xs text-muted">{p.categories.map((c) => t(`giCategory.${c}` as "giCategory.handicraft")).join(" · ")}</span>
                <span className="mt-auto pt-2 text-xs text-muted">
                  {pick(region.name, locale)}
                  {p.sharedWith?.length ? <> · {t("gi.shared")}: {p.sharedWith.map((n) => pick(nameMap[n] ?? { en: n, hi: n, mr: n }, locale)).join(", ")}</> : null}
                </span>
                <span className="text-xs text-muted">
                  {p.applicationNo && <>{t("gi.appNo")} <Digits>{p.applicationNo}</Digits></>}
                  {p.filingDate && <> · {t("gi.filed")} <Digits>{formatDate(p.filingDate, locale)}</Digits></>}
                </span>
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
