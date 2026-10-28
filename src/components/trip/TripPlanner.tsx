"use client";
import { useEffect, useId, useMemo, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { CalendarDays, MapPin, Plane, Route, Sun } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { Localized } from "@/lib/schema";
import type { TripData } from "@/lib/trip";
import { pickItinerary } from "@/lib/tripPick";
import { pick, cmp } from "@/lib/l10n";
import { formatDate } from "@/lib/format";
import { cn } from "@/lib/cn";
import { Link } from "@/i18n/navigation";
import { Digits } from "../Num";

export interface TripRegion { code: string; name: Localized; type: "state" | "ut"; itineraries: number }

const DAYS = [1, 2, 3, 4, 5, 6, 7];
const BASE = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export function TripPlanner({ regions }: { regions: TripRegion[] }) {
  const t = useTranslations("trip");
  const tc = useTranslations("common");
  const locale = useLocale() as Locale;
  const ids = { r: useId(), d: useId(), m: useId() };
  const [code, setCode] = useState("");
  const [days, setDays] = useState(3);
  const [month, setMonth] = useState(0);
  const [data, setData] = useState<TripData | null>(null);
  const [failed, setFailed] = useState(false);
  const [chosenItin, setChosenItin] = useState<string | null>(null);

  const sorted = useMemo(() => [...regions].sort((a, b) => cmp(pick(a.name, locale), pick(b.name, locale))), [regions, locale]);
  const monthName = (m: number) => new Intl.DateTimeFormat(`${locale}-IN`, { month: "long" }).format(new Date(2026, m - 1, 1));

  // Shareable: ?r=IN-GA&d=3&m=11
  useEffect(() => {
    const q = new URLSearchParams(window.location.search);
    const r = q.get("r");
    if (r && regions.some((x) => x.code === r)) setCode(r);
    const d = Number(q.get("d"));
    if (DAYS.includes(d)) setDays(d);
    const m = Number(q.get("m"));
    if (m >= 1 && m <= 12) setMonth(m);
  }, [regions]);
  useEffect(() => {
    const url = new URL(window.location.href);
    if (code) url.searchParams.set("r", code);
    else url.searchParams.delete("r");
    url.searchParams.set("d", String(days));
    if (month) url.searchParams.set("m", String(month));
    else url.searchParams.delete("m");
    window.history.replaceState(null, "", url);
  }, [code, days, month]);

  useEffect(() => {
    setChosenItin(null);
    if (!code) return setData(null);
    let alive = true;
    setFailed(false);
    fetch(`${BASE}/trip/${code}.json`)
      .then((r) => (r.ok ? r.json() : Promise.reject()))
      .then((d: TripData) => alive && setData(d))
      .catch(() => alive && setFailed(true));
    return () => {
      alive = false;
    };
  }, [code]);

  const auto = data ? pickItinerary(data.itineraries, days) : null;
  const itin = data?.itineraries.find((i) => i.id === chosenItin) ?? auto;
  const inMonth = (months: number[] | null) => month !== 0 && !!months?.includes(month);
  const monthListed = data ? data.seasons.some((s) => inMonth(s.months)) : false;

  return (
    <div className="flex flex-col gap-6">
      <section aria-label={t("controls")} className="grid gap-4 rounded-2xl border border-border bg-surface p-4 sm:grid-cols-3">
        <label htmlFor={ids.r} className="flex flex-col gap-1 text-sm font-semibold">
          {t("where")}
          <select id={ids.r} value={code} onChange={(e) => setCode(e.target.value)} className="rounded-md border border-border bg-bg px-3 py-2 font-normal">
            <option value="">{t("chooseRegion")}</option>
            {sorted.map((r) => (
              <option key={r.code} value={r.code}>{pick(r.name, locale)}</option>
            ))}
          </select>
        </label>
        <label htmlFor={ids.d} className="flex flex-col gap-1 text-sm font-semibold">
          {t("howLong")}
          <select id={ids.d} value={days} onChange={(e) => { setDays(Number(e.target.value)); setChosenItin(null); }} className="rounded-md border border-border bg-bg px-3 py-2 font-normal">
            {DAYS.map((d) => (
              <option key={d} value={d}>{t("days", { n: d })}</option>
            ))}
          </select>
        </label>
        <label htmlFor={ids.m} className="flex flex-col gap-1 text-sm font-semibold">
          {t("when")}
          <select id={ids.m} value={month} onChange={(e) => setMonth(Number(e.target.value))} className="rounded-md border border-border bg-bg px-3 py-2 font-normal">
            <option value={0}>{t("anyMonth")}</option>
            {Array.from({ length: 12 }, (_, i) => i + 1).map((m) => (
              <option key={m} value={m}>{monthName(m)}</option>
            ))}
          </select>
        </label>
      </section>

      {!code && <p className="text-muted">{t("start")}</p>}
      {failed && <p className="rounded-xl border border-border bg-surface p-4">{t("loadError")}</p>}

      {data && (
        <div aria-live="polite" className="flex flex-col gap-6">
          <h2 className="text-2xl font-bold">
            {pick(data.name, locale)} · <Digits>{t("days", { n: days })}</Digits>
            {month ? <span className="font-normal text-muted"> · {monthName(month)}</span> : null}
          </h2>

          {/* Itinerary */}
          <section aria-labelledby="it-h" className="rounded-2xl border border-border bg-surface p-5">
            <h3 id="it-h" className="mb-2 flex items-center gap-2 text-lg font-semibold"><Route aria-hidden className="size-5" /> {t("itinerary")}</h3>
            {itin ? (
              <>
                {auto && itin.id === auto.id && itin.days !== null && itin.days !== days && (
                  <p className="mb-2 text-sm text-muted"><Digits>{t("closest", { n: itin.days, wanted: days })}</Digits></p>
                )}
                <p className="font-semibold"><Digits>{pick(itin.label, locale)}</Digits></p>
                {itin.detail && <p className="mt-1">{pick(itin.detail, locale)}</p>}
                {data.itineraries.length > 1 && (
                  <div className="mt-3 flex flex-wrap gap-2 text-sm" role="group" aria-label={t("otherLengths")}>
                    {data.itineraries.map((i) => (
                      <button
                        key={i.id}
                        type="button"
                        aria-pressed={i.id === itin.id}
                        onClick={() => setChosenItin(i.id)}
                        className={cn("rounded-full border px-3 py-1", i.id === itin.id ? "border-navy bg-navy font-semibold text-bg" : "border-border hover:bg-surface-2")}
                      >
                        <Digits>{pick(i.label, locale)}</Digits>
                      </button>
                    ))}
                  </div>
                )}
              </>
            ) : (
              <p className="text-muted">{t("noItinerary")}</p>
            )}
          </section>

          {/* Seasons */}
          {data.seasons.length > 0 && (
            <section aria-labelledby="se-h" className="rounded-2xl border border-border bg-surface p-5">
              <h3 id="se-h" className="mb-2 flex items-center gap-2 text-lg font-semibold"><Sun aria-hidden className="size-5" /> {t("seasons")}</h3>
              {month !== 0 && (
                <p className="mb-3 text-sm">
                  {monthListed ? t("monthListed", { month: monthName(month) }) : t("monthNotListed", { month: monthName(month) })}
                </p>
              )}
              <ul className="grid gap-3 sm:grid-cols-2">
                {data.seasons.map((s, i) => (
                  <li key={i} className={cn("rounded-xl border p-3", inMonth(s.months) ? "border-2 border-[var(--good)]" : "border-border")}>
                    <p className="flex items-center gap-1.5 font-semibold">
                      <CalendarDays aria-hidden className="size-4" /> <Digits>{pick(s.label, locale)}</Digits>
                      {inMonth(s.months) && <span className="sr-only"> — {t("includesMonth")}</span>}
                    </p>
                    {s.detail && <p className="mt-1 text-sm text-muted">{pick(s.detail, locale)}</p>}
                  </li>
                ))}
              </ul>
            </section>
          )}

          {/* Places */}
          {data.places.length > 0 && (
            <section aria-labelledby="pl-h" className="rounded-2xl border border-border bg-surface p-5">
              <h3 id="pl-h" className="mb-2 flex items-center gap-2 text-lg font-semibold"><MapPin aria-hidden className="size-5" /> {t("places")}</h3>
              <ul className="grid gap-2 sm:grid-cols-2">
                {data.places.map((p, i) => (
                  <li key={i}>
                    <span className="font-medium">{pick(p.name, locale)}</span>
                    {p.meta && <span className="text-sm text-muted"> · {pick(p.meta, locale)}</span>}
                  </li>
                ))}
              </ul>
            </section>
          )}

          {/* Getting there */}
          {data.airports.length > 0 && (
            <section aria-labelledby="ai-h" className="rounded-2xl border border-border bg-surface p-5">
              <h3 id="ai-h" className="mb-2 flex items-center gap-2 text-lg font-semibold"><Plane aria-hidden className="size-5" /> {t("airports")}</h3>
              <ul className="flex flex-col gap-1">
                {data.airports.map((a, i) => <li key={i}>{pick(a, locale)}</li>)}
              </ul>
            </section>
          )}

          <p className="text-sm text-muted">
            {t("from")}{" "}
            <Link href={`${data.href}/tourism`}>{t("tourismLink", { region: pick(data.name, locale) })}</Link>
            {" · "}
            <Link href={`${data.href}/climate`}>{t("climateLink")}</Link>
            {" · "}
            <Link href={`${data.href}/transport`}>{t("transportLink")}</Link>
            {data.asOf && <> · <Digits>{tc("lastUpdated", { date: formatDate(data.asOf, locale) })}</Digits></>}
          </p>
        </div>
      )}
    </div>
  );
}
