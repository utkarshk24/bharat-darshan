import { useTranslations } from "next-intl";
import type { Confidence } from "@/lib/schema";
import { ConfidenceBadge } from "../ConfidenceBadge";

export function BlockTitle({ children }: { children: React.ReactNode }) {
  return <h3 className="mb-3 text-xl font-semibold">{children}</h3>;
}

/** Compact provenance footer used by lists, tables and timelines. */
export function ProvenanceLine({ source, url, confidence, extra }: { source: string | null; url: string | null; confidence: Confidence; extra?: string }) {
  const t = useTranslations("common");
  return (
    <p className="mt-2 flex flex-wrap items-center gap-2 text-xs text-muted">
      <ConfidenceBadge level={confidence} />
      {!source && !url && confidence === "Editorial" ? null : <span>
        {t("source")}: {url ? <a href={url} target="_blank" rel="noopener noreferrer">{source ?? url}</a> : source ?? t("pendingVerification")}
        {extra ? ` · ${extra}` : ""}
      </span>}
    </p>
  );
}
