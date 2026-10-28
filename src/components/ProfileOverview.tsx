import { getTranslations } from "next-intl/server";
import { Construction } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { Region } from "@/lib/schema";
import { getIndia, getModule, sourceName } from "@/lib/data";
import { ModuleBlocks } from "./blocks/ModuleBlocks";
import { StatCard, type ValueKind } from "./StatCard";
import { OfficeholderCard } from "./OfficeholderCard";
import { MotifDivider } from "./Motif";
import { LocalizedText } from "./LocalizedText";

const GLANCE: { key: string; label: string; kind: ValueKind }[] = [
  { key: "population2011", label: "common.population", kind: "count" },
  { key: "area", label: "profile.area", kind: "number" },
  { key: "density2011", label: "profile.density", kind: "number" },
  { key: "sexRatio2011", label: "profile.sexRatio", kind: "number" },
  { key: "childSexRatio2011", label: "profile.childSexRatio", kind: "number" },
  { key: "literacyRate2011", label: "profile.literacy", kind: "percent" },
  { key: "urbanisation2011", label: "profile.urbanisation", kind: "percent" },
  { key: "gsdpCurrent", label: "common.gsdp", kind: "rupeeCrore" },
  { key: "perCapitaNsdpCurrent", label: "profile.perCapitaNsdp", kind: "rupee" },
  { key: "forestCoverPct", label: "profile.forestCover", kind: "percent" },
];

/**
 * The overview section of a profile: intro, at-a-glance figures, governance, overview blocks and symbols.
 * `level` is the heading level of its parts: 2 on the profile page, 3 in the printable profile (under an "Overview" h2).
 */
export async function ProfileOverview({ region: r, locale, level = 2, print = false }: { region: Region; locale: Locale; level?: 2 | 3; print?: boolean }) {
  const t = await getTranslations();
  const india = getIndia();
  const label = (id: string | null) => (id ? sourceName(id)?.short ?? id : null);
  const content = getModule(r.code, "overview");
  const H = level === 2 ? "h2" : "h3";
  const hCls = level === 2 ? "mb-4 text-2xl font-bold" : "mb-4 text-xl font-semibold";
  return (
    <>
      {!content && (
        <div className="flex gap-3 rounded-xl border border-dashed border-border bg-surface p-4 text-sm">
          <Construction aria-hidden className="mt-0.5 size-5 shrink-0 text-saffron-ink" />
          <div>
            <p className="font-semibold">{t("profile.phase2")}</p>
            <p className="text-muted">{t("profile.phase2Body")}</p>
          </div>
        </div>
      )}
      {content && <ModuleBlocks blocks={content.blocks.filter((b) => b.id.startsWith("intro"))} region={r} locale={locale} headingLevel={level} print={print} />}

      <section aria-labelledby="glance-h">
        <H id="glance-h" className={hCls}>{t("profile.atAGlance")}</H>
        <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
          {GLANCE.map((g) => {
            const dp = r.metrics[g.key];
            return (
              <StatCard
                key={g.key}
                label={t(g.label as "common.population")}
                dp={dp}
                kind={g.kind}
                sourceLabel={label(dp?.sourceId ?? null)}
                national={india.metrics[g.key] ?? null}
                accent={r.accent}
              />
            );
          })}
        </div>
      </section>

      <MotifDivider motif={r.motif} color={r.accent} />

      <section aria-labelledby="gov-h">
        <H id="gov-h" className={hCls}>{t("profile.governance")}</H>
        <div className="grid gap-3 sm:grid-cols-2">
          {r.government.headOfState && <OfficeholderCard o={r.government.headOfState} sourceLabel={label(r.government.headOfState.sourceId)} />}
          {r.government.headOfGovernment ? (
            <OfficeholderCard o={r.government.headOfGovernment} sourceLabel={label(r.government.headOfGovernment.sourceId)} />
          ) : (
            <div className="rounded-xl border border-border bg-surface p-4">
              <p className="text-sm text-muted">{t("profile.headOfGovernment")}</p>
              <p className="mt-1">{t("profile.noCm")}</p>
            </div>
          )}
        </div>
      </section>

      {content && <ModuleBlocks blocks={content.blocks.filter((b) => !b.id.startsWith("intro"))} region={r} locale={locale} headingLevel={level} print={print} />}

      {Object.keys(r.symbols).length > 0 && (
        <section aria-labelledby="sym-h">
          <H id="sym-h" className={hCls}>{t("profile.symbols")}</H>
          <dl className="grid gap-3 sm:grid-cols-2">
            {Object.entries(r.symbols).map(([k, s]) => (
              <div key={k} className="rounded-xl border border-border bg-surface p-4">
                <dt className="text-sm text-muted">{t.has(`profile.symbolKinds.${k}`) ? t(`profile.symbolKinds.${k}`) : k}</dt>
                <dd className="text-lg font-semibold"><LocalizedText value={s.name} locale={locale} /></dd>
                {s.scientificName && <dd className="text-sm italic text-muted">{s.scientificName}</dd>}
                <dd className="mt-1 text-xs text-muted">{t("common.source")}: {s.sourceId ? label(s.sourceId) : t("common.pendingVerification")}</dd>
              </div>
            ))}
          </dl>
        </section>
      )}
    </>
  );
}
