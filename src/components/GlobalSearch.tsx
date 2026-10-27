"use client";
import { useCallback, useId, useMemo, useRef, useState } from "react";
import { useLocale, useTranslations } from "next-intl";
import { Search, Landmark, MapPinned, Award, Construction, BookOpen, FileText } from "lucide-react";
import { useRouter } from "@/i18n/navigation";
import type { Locale } from "@/i18n/routing";
import type { RegionSummary } from "@/lib/data";
import { buildIndex, createSearcher, type SearchItem } from "@/lib/search";
import { pick } from "@/lib/l10n";
import { cn } from "@/lib/cn";

/** Fuzzy, trilingual, transliteration-tolerant search (WAI-ARIA combobox pattern). */
export function GlobalSearch({ regions }: { regions: RegionSummary[] }) {
  const t = useTranslations();
  const locale = useLocale() as Locale;
  const router = useRouter();
  // Regions and capitals ship with the page; GI products, projects, terms and pages load on first use.
  const [extra, setExtra] = useState<SearchItem[]>([]);
  const loaded = useRef(false);
  const loadExtra = useCallback(() => {
    if (loaded.current) return;
    loaded.current = true;
    fetch(`${process.env.NEXT_PUBLIC_BASE_PATH ?? ""}/search-index.json`)
      .then((r) => (r.ok ? r.json() : []))
      .then((items: SearchItem[]) => setExtra(items))
      .catch(() => {
        loaded.current = false; // try again on the next focus
      });
  }, []);
  const search = useMemo(() => createSearcher([...buildIndex(regions), ...extra]), [regions, extra]);
  const [q, setQ] = useState("");
  const [idx, setIdx] = useState(0);
  const [open, setOpen] = useState(false);
  const listId = useId();
  const inputRef = useRef<HTMLInputElement>(null);
  const results = useMemo(() => search(q), [q, search]);

  const go = (item: SearchItem) => {
    setOpen(false);
    router.push(item.href);
  };

  const kindLabel = (k: SearchItem["kind"]) =>
    ({
      state: t("common.state"),
      ut: t("common.ut"),
      capital: t("common.capital"),
      gi: t("home.kindGi"),
      project: t("home.kindProject"),
      term: t("home.kindTerm"),
      page: t("home.kindPage"),
    })[k];
  const KindIcon = ({ k }: { k: SearchItem["kind"] }) => {
    const I = k === "capital" ? Landmark : k === "gi" ? Award : k === "project" ? Construction : k === "term" ? BookOpen : k === "page" ? FileText : MapPinned;
    return <I aria-hidden className="size-4 text-muted" />;
  };

  return (
    <div className="relative w-full max-w-2xl">
      <label htmlFor={`${listId}-input`} className="sr-only">
        {t("home.searchLabel")}
      </label>
      <div className="flex items-center gap-2 rounded-2xl border-2 border-border bg-surface px-4 py-3 shadow-sm focus-within:border-[var(--focus)]">
        <Search aria-hidden className="size-5 text-muted" />
        <input
          ref={inputRef}
          id={`${listId}-input`}
          type="search"
          role="combobox"
          aria-expanded={open && q.length > 0}
          aria-controls={listId}
          aria-autocomplete="list"
          aria-activedescendant={open && results[idx] ? `${listId}-${idx}` : undefined}
          aria-describedby={`${listId}-hint`}
          autoComplete="off"
          value={q}
          placeholder={t("home.searchPlaceholder")}
          onChange={(e) => {
            setQ(e.target.value);
            setIdx(0);
            setOpen(true);
            loadExtra();
          }}
          onFocus={() => {
            setOpen(true);
            loadExtra();
          }}
          onBlur={() => setTimeout(() => setOpen(false), 150)}
          onKeyDown={(e) => {
            if (e.key === "ArrowDown") {
              e.preventDefault();
              setIdx((i) => Math.min(i + 1, results.length - 1));
            } else if (e.key === "ArrowUp") {
              e.preventDefault();
              setIdx((i) => Math.max(i - 1, 0));
            } else if (e.key === "Enter" && results[idx]) {
              e.preventDefault();
              go(results[idx]);
            } else if (e.key === "Escape") setOpen(false);
          }}
          className="w-full bg-transparent text-base outline-none placeholder:text-muted"
        />
      </div>
      <p id={`${listId}-hint`} className="mt-1.5 text-xs text-muted">
        {t("home.searchHint")}
      </p>
      {open && q.length > 0 && (
        <ul id={listId} role="listbox" className="absolute z-30 mt-1 max-h-96 w-full overflow-auto rounded-xl border border-border bg-surface p-1 shadow-xl">
          {results.length === 0 && <li className="px-3 py-3 text-sm text-muted">{t("home.searchNoResults")}</li>}
          {results.map((r, i) => (
            <li
              key={r.id}
              id={`${listId}-${i}`}
              role="option"
              aria-selected={i === idx}
              onMouseDown={(e) => {
                e.preventDefault();
                go(r);
              }}
              onMouseEnter={() => setIdx(i)}
              className={cn("flex cursor-pointer items-center gap-3 rounded-lg px-3 py-2", i === idx && "bg-surface-2")}
            >
              <KindIcon k={r.kind} />
              <span className="flex-1">
                <span className="font-medium">{pick(r.label, locale)}</span>
                {r.context && <span className="text-muted"> — {pick(r.context, locale)}</span>}
              </span>
              <span className="text-xs text-muted">{kindLabel(r.kind)}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
