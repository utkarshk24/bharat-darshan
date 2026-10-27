"use client";
import { useCallback, useEffect, useMemo, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { Check, X, ExternalLink, RotateCcw } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { QuizKind, QuizQuestion } from "@/lib/quiz";
import { pick } from "@/lib/l10n";
import { formatDate, formatPeriod, formatValue } from "@/lib/format";
import { cn } from "@/lib/cn";
import { Link } from "@/i18n/navigation";
import { Digits } from "../Num";
import type { DataPoint } from "@/lib/schema";

const ROUND = 10;
type Filter = "all" | QuizKind;
const FILTERS: Filter[] = ["all", "capital", "gi", "office", "data"];

function shuffle<T>(a: T[]): T[] {
  const b = [...a];
  for (let i = b.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [b[i], b[j]] = [b[j], b[i]];
  }
  return b;
}

export function QuizView() {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const [bank, setBank] = useState<QuizQuestion[] | null>(null);
  const [failed, setFailed] = useState(false);
  const [filter, setFilter] = useState<Filter>("all");
  const [round, setRound] = useState<QuizQuestion[]>([]);
  const [i, setI] = useState(0);
  const [chosen, setChosen] = useState<number | null>(null);
  const [score, setScore] = useState(0);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_BASE_PATH ?? ""}/learn-quiz.json`)
      .then((r) => (r.ok ? r.json() : Promise.reject()))
      .then((b: QuizQuestion[]) => setBank(b))
      .catch(() => setFailed(true));
  }, []);

  const start = useCallback(
    (f: Filter, b = bank) => {
      if (!b) return;
      setFilter(f);
      setRound(shuffle(b.filter((q) => f === "all" || q.kind === f)).slice(0, ROUND));
      setI(0);
      setChosen(null);
      setScore(0);
    },
    [bank],
  );
  useEffect(() => {
    if (bank) start("all", bank);
  }, [bank, start]);

  const counts = useMemo(() => {
    const c: Record<string, number> = { all: bank?.length ?? 0 };
    for (const q of bank ?? []) c[q.kind] = (c[q.kind] ?? 0) + 1;
    return c;
  }, [bank]);

  if (failed) return <p className="rounded-xl border border-border bg-surface p-6">{t("learn.loadError")}</p>;
  if (!bank || round.length === 0) return <p className="text-muted" aria-live="polite">{t("learn.loading")}</p>;

  const done = i >= round.length;
  const q = round[Math.min(i, round.length - 1)];
  const name = (l: QuizQuestion["options"][number]) => pick(l, locale);
  const question = () => {
    const p = q.params;
    switch (q.template) {
      case "capital":
        return t("learn.q.capital", { region: name(p.region!) });
      case "gi":
        return t("learn.q.gi", { item: name(p.item!) });
      case "office":
        return t("learn.q.office", { role: t(`roles.${p.role}` as "roles.governor"), region: name(p.region!), date: formatDate(p.asOf!, locale) });
      default:
        return t(`learn.q.${q.template}`, { indicator: name(p.indicator!), period: formatPeriod(p.period!, locale) });
    }
  };
  const val = (k: number) =>
    q.values && q.valueKind ? formatValue({ value: q.values[k].value, unit: q.values[k].unit } as DataPoint, q.valueKind, locale) : null;

  const answer = (k: number) => {
    if (chosen !== null) return;
    setChosen(k);
    if (k === q.answer) setScore((s) => s + 1);
  };

  return (
    <div className="flex flex-col gap-6">
      <fieldset className="flex flex-col gap-2">
        <legend className="mb-1 text-sm font-semibold">{t("learn.topic")}</legend>
        <div className="flex flex-wrap gap-2">
          {FILTERS.filter((f) => (counts[f] ?? 0) >= 4).map((f) => (
            <button
              key={f}
              type="button"
              aria-pressed={filter === f}
              onClick={() => start(f)}
              className={cn("rounded-full border px-3 py-1.5 text-sm", filter === f ? "border-navy bg-navy font-semibold text-bg" : "border-border hover:bg-surface-2")}
            >
              {t(`learn.kind.${f}`)} <span className="text-xs opacity-80">(<Digits>{String(counts[f])}</Digits>)</span>
            </button>
          ))}
        </div>
      </fieldset>

      {done ? (
        <section aria-live="polite" className="rounded-2xl border border-border bg-surface p-6 text-center">
          <h2 className="text-2xl font-bold"><Digits>{t("learn.final", { score, total: round.length })}</Digits></h2>
          <button type="button" onClick={() => start(filter)} className="mt-4 inline-flex items-center gap-1.5 rounded-md border border-border px-3 py-1.5 hover:bg-surface-2">
            <RotateCcw aria-hidden className="size-4" /> {t("learn.again")}
          </button>
        </section>
      ) : (
        <section aria-labelledby="q-h" className="flex flex-col gap-4 rounded-2xl border border-border bg-surface p-5">
          <p className="text-sm text-muted">
            <Digits>{t("learn.progress", { n: i + 1, total: round.length, score })}</Digits>
          </p>
          <h2 id="q-h" className="text-xl font-semibold"><Digits>{question()}</Digits></h2>
          <ul className="grid gap-2 sm:grid-cols-2">
            {q.options.map((o, k) => {
              const right = chosen !== null && k === q.answer;
              const wrong = chosen === k && k !== q.answer;
              return (
                <li key={k}>
                  <button
                    type="button"
                    onClick={() => answer(k)}
                    disabled={chosen !== null}
                    aria-describedby={chosen !== null ? "q-feedback" : undefined}
                    className={cn(
                      "flex w-full items-center justify-between gap-2 rounded-xl border-2 px-4 py-3 text-left",
                      chosen === null && "border-border hover:bg-surface-2",
                      right && "border-[var(--good)]",
                      wrong && "border-[var(--bad)]",
                      chosen !== null && !right && !wrong && "border-border opacity-80",
                    )}
                  >
                    <span>
                      {name(o)}
                      {chosen !== null && val(k) && <span className="block text-sm text-muted"><Digits>{val(k)!}</Digits></span>}
                    </span>
                    {right && <Check aria-label={t("learn.correctMark")} className="size-5 shrink-0 text-[var(--good)]" />}
                    {wrong && <X aria-label={t("learn.wrongMark")} className="size-5 shrink-0 text-[var(--bad)]" />}
                  </button>
                </li>
              );
            })}
          </ul>
          <div id="q-feedback" aria-live="polite" className="min-h-6 text-sm">
            {chosen !== null && (
              <div className="flex flex-col gap-2">
                <p className="font-semibold">{chosen === q.answer ? t("learn.right") : t("learn.wrong", { answer: name(q.options[q.answer]) })}</p>
                <p className="flex flex-wrap items-center gap-x-3 gap-y-1 text-muted">
                  {q.source.url ? (
                    <a href={q.source.url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1">
                      {t("common.source")}: {q.source.label}
                      {q.source.period && <> · <Digits>{formatPeriod(q.source.period, locale)}</Digits></>}
                      <ExternalLink aria-hidden className="size-3" />
                    </a>
                  ) : null}
                  {q.source.asOf && <span><Digits>{t("common.dataAsOn", { date: formatDate(q.source.asOf, locale) })}</Digits></span>}
                  {q.href && <Link href={q.href}>{t("learn.more")}</Link>}
                </p>
                <button
                  type="button"
                  onClick={() => {
                    setI(i + 1);
                    setChosen(null);
                  }}
                  className="mt-1 w-fit rounded-md bg-navy px-4 py-2 font-semibold text-bg"
                  autoFocus
                >
                  {i + 1 < round.length ? t("learn.next") : t("learn.finish")}
                </button>
              </div>
            )}
          </div>
        </section>
      )}
    </div>
  );
}
