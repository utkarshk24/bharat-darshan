"use client";
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import type { Locale } from "@/i18n/routing";
import type { Block } from "@/lib/schema";
import { formatIndianNumber } from "@/lib/format";

type Series = Extract<Block, { type: "series" }>;
// Colour-blind-safe pair (Okabe–Ito blue / vermillion), plus dashes so colour isn't the only cue.
const COLORS = ["#0072B2", "#D55E00", "#009E73", "#CC79A7"];
const DASH = ["", "6 4", "2 3", "8 3 2 3"];

export interface LinesProps {
  rows: Record<string, string | number | null>[];
  block: Series;
  labels: string[];
  fmt: (v: number) => string;
  locale: Locale;
}

/** The Recharts drawing itself. Loaded on demand by LazyLines so the chart library stays off the critical path. */
export default function SeriesLines({ rows, block, labels, fmt, locale }: LinesProps) {
  return (
    <ResponsiveContainer width="100%" height="100%">
      <LineChart data={rows} margin={{ top: 8, right: 16, bottom: 8, left: 8 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
        <XAxis dataKey="period" tick={{ fontSize: 11, fill: "var(--text-muted)" }} interval="preserveStartEnd" />
        <YAxis
          tick={{ fontSize: 11, fill: "var(--text-muted)" }}
          width={72}
          tickFormatter={(v: number) => (block.kind === "rupeeCrore" ? `${formatIndianNumber(v / 1e5, locale, { maximumFractionDigits: 1 })}L` : formatIndianNumber(v, locale, { maximumFractionDigits: 1 }))}
        />
        <Tooltip
          formatter={(v) => (typeof v === "number" ? fmt(v) : String(v))}
          contentStyle={{ background: "var(--surface)", border: "1px solid var(--border)", color: "var(--text)", fontSize: 12 }}
        />
        {block.series.length > 1 && <Legend wrapperStyle={{ fontSize: 12 }} />}
        {block.series.map((s, i) => (
          <Line key={s.id} type="monotone" dataKey={s.id} name={labels[i]} stroke={COLORS[i % 4]} strokeDasharray={DASH[i % 4]} strokeWidth={2.2} dot={{ r: 2.5 }} connectNulls={false} isAnimationActive={false} />
        ))}
      </LineChart>
    </ResponsiveContainer>
  );
}
