import { getTranslations } from "next-intl/server";
import type { Locale } from "@/i18n/routing";
import type { Block, Region } from "@/lib/schema";
import { sourceName } from "@/lib/data";
import { pick } from "@/lib/l10n";
import { formatDate } from "@/lib/format";
import { StatCard } from "../StatCard";
import { ConfidenceBadge } from "../ConfidenceBadge";
import { OfficeholderCard } from "../OfficeholderCard";
import { BlockTitle, ProvenanceLine } from "./shared";
import { SeriesChart } from "./SeriesChart";
import { WeatherWidget } from "./WeatherWidget";
import { GIGrid } from "./GIGrid";
import { ProjectCards } from "./ProjectCards";
import { Digits } from "../Num";

const short = (id: string | null | undefined) => (id ? sourceName(id)?.short ?? id : null);

/** Renders a module's typed blocks (Section 7). Server component. */
export async function ModuleBlocks({ blocks, region, locale, headingLevel = 3, print = false }: { blocks: Block[]; region: Region; locale: Locale; headingLevel?: 2 | 3; print?: boolean }) {
  const t = await getTranslations();
  const L = (v: Parameters<typeof pick>[0]) => pick(v, locale);

  return (
    <div className="flex flex-col gap-10">
      {blocks.map((b) => {
        switch (b.type) {
          case "prose":
            return (
              <section key={b.id}>
                {b.title && <BlockTitle level={headingLevel}>{L(b.title)}</BlockTitle>}
                <div className="max-w-3xl space-y-3 text-[1.05rem]">
                  {L(b.body).split(/\n\n+/).map((p, i) => <p key={i}>{p}</p>)}
                </div>
                <p className="mt-2 flex flex-wrap items-center gap-2 text-xs text-muted">
                  <ConfidenceBadge level={b.confidence} />
                  {b.sourceIds.length > 0 && (
                    <span>
                      {t("common.sourcesLine")}:{" "}
                      {b.sourceIds.map((id, i) => {
                        const s = sourceName(id);
                        return (
                          <span key={id}>
                            {i > 0 && ", "}
                            {s ? <a href={s.url} target="_blank" rel="noopener noreferrer">{s.short}</a> : id}
                          </span>
                        );
                      })}
                    </span>
                  )}
                </p>
              </section>
            );
          case "facts":
            return (
              <section key={b.id}>
                {b.title && <BlockTitle level={headingLevel}>{L(b.title)}</BlockTitle>}
                <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
                  {b.items.map((f) => (
                    <StatCard
                      key={f.id}
                      label={L(f.label)}
                      dp={f.dp}
                      kind={f.kind}
                      sourceLabel={short(f.dp.sourceId)}
                      national={f.national}
                      previous={f.previous}
                      polarity={f.polarity}
                      accent={region.accent}
                    />
                  ))}
                </div>
              </section>
            );
          case "list":
            return (
              <section key={b.id}>
                {b.title && <BlockTitle level={headingLevel}>{L(b.title)}</BlockTitle>}
                {b.layout === "chips" ? (
                  <ul className="flex flex-wrap gap-2">
                    {b.items.map((it) => (
                      <li key={it.id} className="rounded-full border border-border bg-surface px-3 py-1 text-sm">
                        {L(it.name)}
                        {it.meta && <span className="text-muted"> · {L(it.meta)}</span>}
                      </li>
                    ))}
                  </ul>
                ) : b.layout === "bullets" ? (
                  <ul className="max-w-3xl list-disc space-y-1.5 pl-5">
                    {b.items.map((it) => (
                      <li key={it.id}>
                        <span className="font-medium">{L(it.name)}</span>
                        {it.meta && <span className="text-muted"> ({L(it.meta)})</span>}
                        {it.detail && <span> — {L(it.detail)}</span>}
                      </li>
                    ))}
                  </ul>
                ) : (
                  <ul className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
                    {b.items.map((it) => (
                      <li key={it.id} className="flex flex-col gap-1 rounded-xl border border-border bg-surface p-4" style={{ borderTop: `3px solid ${region.accent}` }}>
                        <span className="font-semibold">{L(it.name)}</span>
                        {it.meta && <span className="text-sm text-muted">{L(it.meta)}</span>}
                        {it.detail && <span className="text-sm">{L(it.detail)}</span>}
                        {it.url && (
                          <a href={it.url} target="_blank" rel="noopener noreferrer" className="mt-auto pt-1 text-xs">
                            {short(it.sourceId ?? b.sourceId) ?? t("common.source")}
                          </a>
                        )}
                      </li>
                    ))}
                  </ul>
                )}
                {/* Lists whose items each carry their own source (e.g. official links) need no block-level line. */}
                {b.sourceId || b.url || !b.items.every((it) => it.sourceId) ? (
                  <ProvenanceLine
                    source={short(b.sourceId)}
                    url={b.url}
                    confidence={b.confidence}
                    extra={b.accessDate ? t("common.asOfShort", { date: formatDate(b.accessDate, locale) }) : undefined}
                  />
                ) : null}
              </section>
            );
          case "timeline":
            return (
              <section key={b.id}>
                {b.title && <BlockTitle level={headingLevel}>{L(b.title)}</BlockTitle>}
                <ol className="relative ml-3 max-w-3xl border-l-2 pl-6" style={{ borderColor: region.accent }}>
                  {[...b.events].sort((x, y) => x.year - y.year).map((e) => (
                    <li key={e.id} className="relative mb-5 last:mb-0">
                      <span aria-hidden className="absolute -left-[33px] top-1.5 size-3.5 rounded-full border-2 bg-surface" style={{ borderColor: region.accent }} />
                      <p className="text-sm font-semibold" style={{ color: region.accent }}>{L(e.when)}</p>
                      <p className="font-medium">{L(e.label)}</p>
                      {e.detail && <p className="text-sm text-muted">{L(e.detail)}</p>}
                    </li>
                  ))}
                </ol>
                <ProvenanceLine source={short(b.sourceId)} url={b.url} confidence={b.confidence} />
              </section>
            );
          case "series":
            return (
              <section key={b.id}>
                <BlockTitle level={headingLevel}>{L(b.title)}</BlockTitle>
                <SeriesChart
                  block={b}
                  labels={b.series.map((s) => L(s.label))}
                  sourceLabel={short(b.series[0].points[0].sourceId)}
                  note={b.note ? L(b.note) : undefined}
                />
              </section>
            );
          case "table":
            return (
              <section key={b.id}>
                <BlockTitle level={headingLevel}>{L(b.title)}</BlockTitle>
                <div role="region" tabIndex={0} aria-label={L(b.title)} className="overflow-x-auto rounded-xl border border-border bg-surface focus-visible:outline-2 focus-visible:outline-offset-2">
                  <table className="w-full text-sm">
                    <thead className="bg-surface-2">
                      <tr>
                        {b.columns.map((c, i) => (
                          <th key={i} scope="col" className={`px-3 py-2 ${c.align === "right" ? "text-right" : "text-left"}`}>{L(c.label)}</th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {b.rows.map((r, i) => (
                        <tr key={i} className="border-t border-border">
                          {r.map((cell, j) => {
                            const txt = typeof cell === "object" ? L(cell) : typeof cell === "number" ? new Intl.NumberFormat("en-IN").format(cell) : cell;
                            const Tag = j === 0 ? "th" : "td";
                            return (
                              <Tag key={j} scope={j === 0 ? "row" : undefined} className={`px-3 py-2 ${j === 0 ? "font-medium" : ""} ${b.columns[j]?.align === "right" ? "text-right tabular-nums" : "text-left"}`}>
                                {typeof cell === "object" ? txt : <Digits>{String(txt)}</Digits>}
                              </Tag>
                            );
                          })}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
                {b.note && <p className="mt-2 text-sm text-muted">{L(b.note)}</p>}
                <ProvenanceLine
                  source={short(b.sourceId)}
                  url={b.url}
                  confidence={b.confidence}
                  extra={[b.period, b.accessDate ? t("common.asOfShort", { date: formatDate(b.accessDate, locale) }) : null].filter(Boolean).join(" · ") || undefined}
                />
              </section>
            );
          case "links":
            return (
              <section key={b.id}>
                {b.title && <BlockTitle level={headingLevel}>{L(b.title)}</BlockTitle>}
                <ul className="grid gap-2 sm:grid-cols-2">
                  {b.items.map((l) => (
                    <li key={l.url} className="rounded-lg border border-border bg-surface px-4 py-3">
                      <a href={l.url} target="_blank" rel="noopener noreferrer" className="font-medium">{L(l.label)}</a>
                      {l.detail && <p className="text-sm text-muted">{L(l.detail)}</p>}
                    </li>
                  ))}
                </ul>
              </section>
            );
          case "weather":
            // Live readings are left out of printed profiles: a PDF would freeze them without a time.
            if (print) return null;
            return (
              <section key={b.id}>
                <WeatherWidget places={b.places.map((p) => ({ name: L(p.name), lat: p.lat, lon: p.lon }))} />
              </section>
            );
          case "projects":
            return <ProjectCards key={b.id} projects={region.projects} sourceLabels={Object.fromEntries(region.projects.flatMap((p) => [p.sourceId, ...(p.supporting ?? []).map((x) => x.sourceId)]).map((id) => [id, short(id) ?? id]))} accent={region.accent} />;
          case "gi":
            return <GIGrid key={b.id} products={region.giProducts} accent={region.accent} />;
          case "officeholders": {
            const all = [region.government.headOfState, region.government.headOfGovernment, ...region.government.others].filter(Boolean);
            return (
              <section key={b.id} className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
                {all.map((o, i) => <OfficeholderCard key={i} o={o!} sourceLabel={short(o!.sourceId)} />)}
              </section>
            );
          }
          case "gaps":
            return (
              <section key={b.id} className="rounded-xl border border-dashed border-border bg-surface p-4">
                <p className="font-semibold">{t("common.pendingTitle")}</p>
                <p className="mb-2 text-sm text-muted">{t("common.pendingBody")}</p>
                <ul className="list-disc space-y-1 pl-5 text-sm">
                  {b.items.map((g, i) => (
                    <li key={i}>
                      {L(g.label)} — <span className="text-muted">{t("common.notAvailable")} ({short(g.sourceId)})</span>
                    </li>
                  ))}
                </ul>
              </section>
            );
        }
      })}
    </div>
  );
}
