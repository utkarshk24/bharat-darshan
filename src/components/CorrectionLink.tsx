"use client";
import { useEffect, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { Flag } from "lucide-react";
import type { Locale } from "@/i18n/routing";
import { correctionUrl, ISSUES_NEW } from "@/lib/correction";

/** Page-level "Suggest a correction" link; the current address is filled in after load. */
export function CorrectionLink({ className }: { className?: string }) {
  const t = useTranslations("common");
  const locale = useLocale() as Locale;
  const [href, setHref] = useState(`${ISSUES_NEW}?template=correction.yml`);
  useEffect(() => setHref(correctionUrl({ page: window.location.href, locale })), [locale]);
  return (
    <a href={href} target="_blank" rel="noopener noreferrer" className={className ?? "inline-flex items-center gap-1.5 text-sm"}>
      <Flag aria-hidden className="size-4" /> {t("suggestCorrection")}
      <span className="sr-only"> ({t("opensGithub")})</span>
    </a>
  );
}
