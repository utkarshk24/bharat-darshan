"use client";
import { useLocale, useTranslations } from "next-intl";
import { ExternalLink } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import type { Project } from "@/lib/schema";
import { pick } from "@/lib/l10n";

/** Secondary sources on a project card, each with the details it covers. */
export function SupportingSources({ items, sourceLabels }: { items: Project["supporting"]; sourceLabels: Record<string, string> }) {
  const t = useTranslations("common");
  const locale = useLocale() as Locale;
  if (!items?.length) return null;
  return (
    <span className="basis-full">
      {items.map((s, i) => (
        <span key={i} className="block">
          {t("alsoSource")}{" "}
          <a href={s.url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1">
            {sourceLabels[s.sourceId] ?? s.sourceId} <ExternalLink aria-hidden className="size-3" />
          </a>{" "}
          ({pick(s.covers, locale)})
        </span>
      ))}
    </span>
  );
}
