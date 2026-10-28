"use client";
import { useEffect, useState } from "react";
import { useLocale, useTranslations } from "next-intl";

interface Saved {
  href: string;
  title: string;
}

/** Lists the pages this device has saved for offline reading (newest first, titles from the saved copies). */
export function SavedPages() {
  const t = useTranslations("offline");
  const locale = useLocale();
  const [items, setItems] = useState<Saved[] | null>(null);

  useEffect(() => {
    let alive = true;
    (async () => {
      if (!("caches" in window)) return setItems([]);
      const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
      const names = (await caches.keys()).filter((n) => n.startsWith("bd-pages-"));
      const out: Saved[] = [];
      for (const n of names) {
        const c = await caches.open(n);
        const keys = [...(await c.keys())].reverse();
        for (const req of keys) {
          const u = new URL(req.url);
          if (u.search || u.pathname.endsWith(".txt") || !u.pathname.startsWith(`${base}/${locale}/`) || u.pathname.endsWith("/offline/")) continue;
          if (out.some((x) => x.href === u.pathname)) continue;
          let title = decodeURIComponent(u.pathname.slice(base.length));
          if (out.length < 60) {
            const html = await (await c.match(req))?.text();
            const m = html?.match(/<title>([^<]*)<\/title>/);
            if (m) title = m[1].replace(/&amp;/g, "&").replace(/&#x27;/g, "'");
          }
          out.push({ href: u.pathname, title });
        }
      }
      if (alive) setItems(out);
    })().catch(() => alive && setItems([]));
    return () => {
      alive = false;
    };
  }, [locale]);

  if (items === null) return <p className="text-muted">{t("checking")}</p>;
  return (
    <section aria-labelledby="saved-h" className="rounded-2xl border border-border bg-surface p-5">
      <h2 id="saved-h" className="mb-3 text-lg font-semibold">{t("savedTitle")}</h2>
      {items.length === 0 ? (
        <p className="text-muted">{t("none")}</p>
      ) : (
        <ul className="flex flex-col gap-2">
          {items.map((s) => (
            <li key={s.href}>
              {/* Plain links: the service worker serves the saved copy */}
              <a href={s.href}>{s.title}</a>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}
