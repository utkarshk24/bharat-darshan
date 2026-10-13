"use client";
import { useEffect, useState } from "react";
import { useTranslations } from "next-intl";
import { Radio, Droplets, Wind } from "lucide-react";
import { Digits } from "../Num";

interface Now { temp: number; humidity: number; wind: number; code: number }

// WMO weather codes → short English labels (displayed with an icon-free text label).
const WMO: Record<number, string> = { 0: "☀", 1: "🌤", 2: "⛅", 3: "☁", 45: "🌫", 48: "🌫", 51: "🌦", 53: "🌦", 55: "🌧", 61: "🌧", 63: "🌧", 65: "🌧", 80: "🌦", 81: "🌧", 82: "⛈", 95: "⛈", 96: "⛈", 99: "⛈" };

/** Live weather for major cities via Open-Meteo (free, no key). Labelled "Live" (Section 7C). */
export function WeatherWidget({ places }: { places: { name: string; lat: number; lon: number }[] }) {
  const t = useTranslations("common");
  const [data, setData] = useState<(Now | null)[] | null>(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    const lat = places.map((p) => p.lat).join(",");
    const lon = places.map((p) => p.lon).join(",");
    fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&timezone=Asia%2FKolkata`)
      .then((r) => (r.ok ? r.json() : Promise.reject()))
      .then((j) => {
        const arr = Array.isArray(j) ? j : [j];
        setData(arr.map((x) => (x?.current ? { temp: x.current.temperature_2m, humidity: x.current.relative_humidity_2m, wind: x.current.wind_speed_10m, code: x.current.weather_code } : null)));
      })
      .catch(() => setError(true));
  }, [places]);

  return (
    <div className="rounded-2xl border border-border bg-surface p-4">
      <p className="mb-3 inline-flex items-center gap-1.5 rounded-full bg-[var(--bad)] px-2.5 py-0.5 text-xs font-semibold text-white dark:text-black">
        <Radio aria-hidden className="size-3.5" /> {t("live")}
      </p>
      {error ? (
        <p className="text-sm text-muted">{t("weatherError")}</p>
      ) : (
        <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4" aria-live="polite">
          {places.map((p, i) => {
            const d = data?.[i];
            return (
              <li key={p.name} className="rounded-xl bg-surface-2 p-3">
                <p className="font-medium">{p.name}</p>
                {d ? (
                  <>
                    <p className="text-2xl font-semibold tabular-nums">
                      <span aria-hidden className="mr-1">{WMO[d.code] ?? ""}</span>
                      <Digits>{`${Math.round(d.temp)}°C`}</Digits>
                    </p>
                    <p className="flex gap-3 text-xs text-muted">
                      <span className="inline-flex items-center gap-1"><Droplets aria-hidden className="size-3" />{t("humidity")} <Digits>{`${d.humidity}%`}</Digits></span>
                      <span className="inline-flex items-center gap-1"><Wind aria-hidden className="size-3" />{t("wind")} <Digits>{`${Math.round(d.wind)} km/h`}</Digits></span>
                    </p>
                  </>
                ) : (
                  <div className="skeleton mt-2 h-8 w-24 rounded" />
                )}
              </li>
            );
          })}
        </ul>
      )}
      <p className="mt-3 text-xs text-muted">
        {t("liveWeatherNote")} <a href="https://open-meteo.com" target="_blank" rel="noopener noreferrer">open-meteo.com</a>
      </p>
    </div>
  );
}
