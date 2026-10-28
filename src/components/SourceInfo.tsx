"use client";
import { useEffect, useId, useRef, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { Info, ExternalLink, Flag } from "lucide-react";
import type { Confidence } from "@/lib/schema";
import type { Locale } from "@/i18n/routing";
import { correctionUrl } from "@/lib/correction";
import { formatDate, formatPeriod } from "@/lib/format";
import { ConfidenceBadge } from "./ConfidenceBadge";
import { Digits } from "./Num";
import { usePrintMode } from "./PrintMode";

export interface SourceInfoProps {
  sourceLabel: string | null;
  period?: string | null;
  url?: string | null;
  accessDate?: string | null;
  asOf?: string | null;
  confidence: Confidence;
  revisionStatus: string;
  note?: string;
  verifyUrl?: string | null;
  /** Icon-only trigger (dense tables); the full label stays available to screen readers. */
  compact?: boolean;
  /** What the figure is (e.g. "Population"), used to pre-fill a correction report. */
  subject?: string;
}

/**
 * The "Source · Year" line shown under every figure (Principle 1), with a
 * click/tap disclosure for full provenance. Works with keyboard and touch.
 */
export function SourceInfo(p: SourceInfoProps) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const [open, setOpen] = useState(false);
  const id = useId();
  const ref = useRef<HTMLSpanElement>(null);
  const print = usePrintMode();

  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    const onClick = (e: MouseEvent) => ref.current && !ref.current.contains(e.target as Node) && setOpen(false);
    document.addEventListener("keydown", onKey);
    document.addEventListener("mousedown", onClick);
    return () => {
      document.removeEventListener("keydown", onKey);
      document.removeEventListener("mousedown", onClick);
    };
  }, [open]);

  const label = [p.sourceLabel ?? t("common.notAvailable"), p.period ? formatPeriod(p.period, locale) : null]
    .filter(Boolean)
    .join(" · ");

  if (print) {
    const link = p.url || p.verifyUrl;
    return (
      <span className="block text-xs text-muted">
        <strong>{t("common.source")}:</strong> <Digits>{label}</Digits>
        {" · "}{t(`confidence.${p.confidence}` as "confidence.Official")}
        {" · "}{t(`revision.${p.revisionStatus}` as "revision.final")}
        {p.accessDate ? <> · <Digits>{t("common.lastUpdated", { date: formatDate(p.accessDate, locale) })}</Digits></> : null}
        {p.asOf ? <> · <Digits>{t("common.dataAsOn", { date: formatDate(p.asOf, locale) })}</Digits></> : null}
        {p.note && <span className="block" lang="en">{p.note}</span>}
        {link && <a href={link} className="print-url block break-all">{link}</a>}
      </span>
    );
  }

  return (
    <span ref={ref} className="relative inline-flex">
      <button
        type="button"
        aria-expanded={open}
        aria-controls={id}
        onClick={() => setOpen((o) => !o)}
        className="inline-flex items-center gap-1 text-xs text-muted underline decoration-dotted underline-offset-2 hover:text-text"
      >
        <Info aria-hidden className="size-3.5" />
        <span className="sr-only">{t("common.source")}: </span>
        {p.compact ? <span className="sr-only">{label}</span> : <Digits>{label}</Digits>}
      </button>
      {open && (
        <span
          id={id}
          role="dialog"
          aria-label={t("common.source")}
          className={`absolute ${p.compact ? "right-0" : "left-0"} top-full z-30 mt-1 w-72 rounded-lg border border-border bg-surface p-3 text-left text-xs text-text shadow-lg`}
        >
          <span className="mb-2 flex flex-wrap gap-1">
            <ConfidenceBadge level={p.confidence} />
            <span className="rounded-full bg-surface-2 px-2 py-0.5">{t(`revision.${p.revisionStatus}` as "revision.final")}</span>
          </span>
          <span className="block">
            <strong>{t("common.source")}:</strong> {p.sourceLabel ?? t("common.notAvailable")}
          </span>
          {p.period && (
            <span className="block">
              <strong>{t("common.period")}:</strong> <Digits>{formatPeriod(p.period, locale)}</Digits>
            </span>
          )}
          {p.accessDate ? (
            <span className="block"><Digits>{t("common.lastUpdated", { date: formatDate(p.accessDate, locale) })}</Digits></span>
          ) : null}
          {p.asOf ? (
            <span className="block"><Digits>{t("common.dataAsOn", { date: formatDate(p.asOf, locale) })}</Digits></span>
          ) : null}
          {p.note && <span className="mt-1 block text-muted" lang="en">{p.note}</span>}
          {(p.url || p.verifyUrl) && (
            <a
              href={(p.url || p.verifyUrl)!}
              target="_blank"
              rel="noopener noreferrer"
              className="mt-2 inline-flex items-center gap-1 font-medium"
            >
              {t("common.verifyOfficial")} <ExternalLink aria-hidden className="size-3" />
            </a>
          )}
          <a
            href={correctionUrl({
              page: typeof window === "undefined" ? "" : window.location.href,
              item: [p.subject, label].filter(Boolean).join(" — "),
              locale,
            })}
            target="_blank"
            rel="noopener noreferrer"
            className="mt-1 flex items-center gap-1 text-muted hover:text-text"
          >
            <Flag aria-hidden className="size-3" /> {t("common.suggestCorrection")}
            <span className="sr-only"> ({t("common.opensGithub")})</span>
          </a>
        </span>
      )}
    </span>
  );
}
