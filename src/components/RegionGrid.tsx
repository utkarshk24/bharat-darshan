"use client";
import { useMemo, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import type { RegionSummary } from "@/lib/data";
import type { ZonalCouncil } from "@/lib/schema";
import type { Locale } from "@/i18n/routing";
import { pick, cmp } from "@/lib/l10n";
import { cn } from "@/lib/cn";
import { RegionCard } from "./RegionCard";
import { Digits } from "./Num";

const ZONES: ZonalCouncil[] = ["northern", "central", "eastern", "western", "southern", "north-eastern", "islands"];

export function RegionGrid({ regions, initialType = "all", showTypeFilter = true }: {
  regions: RegionSummary[];
  initialType?: "all" | "state" | "ut";
  showTypeFilter?: boolean;
}) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const [type, setType] = useState<"all" | "state" | "ut">(initialType);
  const [zone, setZone] = useState<ZonalCouncil | "all">("all");

  const shown = useMemo(
    () =>
      regions
        .filter((r) => (type === "all" || r.type === type) && (zone === "all" || r.zonalCouncil === zone))
        .sort((a, b) => cmp(pick(a.name, locale), pick(b.name, locale))),
    [regions, type, zone, locale],
  );

  const chip = (active: boolean) =>
    cn("rounded-full border px-3 py-1 text-sm", active ? "border-navy bg-navy text-bg font-semibold" : "border-border hover:bg-surface-2");

  return (
    <div className="flex flex-col gap-4">
      <div className="flex flex-wrap items-center gap-x-6 gap-y-3">
        {showTypeFilter && (
          <div role="group" aria-label={t("home.filterType")} className="flex flex-wrap gap-2">
            {(["all", "state", "ut"] as const).map((k) => (
              <button key={k} type="button" aria-pressed={type === k} onClick={() => setType(k)} className={chip(type === k)}>
                {k === "all" ? t("common.all") : k === "state" ? t("common.states") : t("common.uts")}
              </button>
            ))}
          </div>
        )}
        <div role="group" aria-label={t("home.filterRegion")} className="flex flex-wrap gap-2">
          <button type="button" aria-pressed={zone === "all"} onClick={() => setZone("all")} className={chip(zone === "all")}>
            {t("common.all")}
          </button>
          {ZONES.map((z) => (
            <button key={z} type="button" aria-pressed={zone === z} onClick={() => setZone(z)} className={chip(zone === z)}>
              {t(`zonal.${z}`)}
            </button>
          ))}
        </div>
      </div>
      <p className="text-sm text-muted" aria-live="polite">
        <Digits>{t("home.showing", { count: shown.length, total: regions.length })}</Digits>
      </p>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
        {shown.map((r) => (
          <RegionCard key={r.code} r={r} />
        ))}
      </div>
    </div>
  );
}
