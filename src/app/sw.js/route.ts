import { getDataAsOn } from "@/lib/data";
import { BASE_PATH } from "@/lib/seo";

export const dynamic = "force-static";

/**
 * Service worker for offline reading, generated at build time so it knows the base path and
 * gets a new version on every build (old caches are dropped on activate).
 *
 * - Pages: network first (fresh when online), saved copy when offline, else the offline page.
 * - /_next/static (content-hashed): cache first.
 * - Fonts, maps, icons, search and quiz data: stale-while-revalidate.
 * - Data Library downloads are never cached (large; always fetched fresh).
 */
export function GET() {
  const version = `${getDataAsOn()}-${Date.now()}`;
  const body = `/* Bharat Darshan service worker ${version} */
const BASE = ${JSON.stringify(BASE_PATH)};
const VERSION = ${JSON.stringify(version)};
const SHELL = "bd-shell-" + VERSION, PAGES = "bd-pages-" + VERSION, ASSETS = "bd-assets-" + VERSION;
const LOCALES = ["en", "hi", "mr"];
const MAX_PAGES = 300;
const PRECACHE = [
  ...LOCALES.flatMap((l) => [BASE + "/" + l + "/", BASE + "/" + l + "/offline/"]),
  BASE + "/maps/manifest.json", BASE + "/maps/india-soi-states.topo.json", BASE + "/maps/capitals.json",
  BASE + "/fonts/inter-latin.woff2", BASE + "/fonts/deva.woff2",
  BASE + "/icons/icon-192.png",
];

self.addEventListener("install", (e) => {
  // Each file separately: one missing file must not stop offline support from installing.
  // The offline and home pages also need their own scripts and styles to work offline,
  // so the /_next/static files they reference are saved too.
  e.waitUntil(
    caches.open(SHELL)
      .then((c) => Promise.allSettled(PRECACHE.map((u) => c.add(u))).then(() => c))
      .then(async (c) => {
        const assets = new Set();
        for (const u of PRECACHE.filter((x) => x.endsWith("/"))) {
          const res = await c.match(u);
          const html = res ? await res.text() : "";
          for (const part of html.split('"')) if (part.includes("/_next/static/") && !part.includes(" ")) assets.add(new URL(part, self.location.href).href);
        }
        const a = await caches.open(ASSETS);
        await Promise.allSettled([...assets].map((u) => a.add(u)));
      })
      .then(() => self.skipWaiting()),
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith("bd-") && !k.endsWith(VERSION)).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});

async function trim(name, max) {
  const c = await caches.open(name);
  const keys = await c.keys();
  for (let i = 0; i < keys.length - max; i++) await c.delete(keys[i]);
}

function localeOf(url) {
  const seg = url.pathname.slice(BASE.length).split("/")[1];
  return LOCALES.includes(seg) ? seg : "en";
}

async function networkFirst(req, cacheName) {
  try {
    const res = await fetch(req);
    if (res.ok) {
      const c = await caches.open(cacheName);
      c.put(req, res.clone());
      if (cacheName === PAGES) trim(PAGES, MAX_PAGES);
    }
    return res;
  } catch (err) {
    const hit = await caches.match(req, { ignoreSearch: req.mode === "navigate" });
    if (hit) return hit;
    if (req.mode === "navigate") {
      const off = await caches.match(BASE + "/" + localeOf(new URL(req.url)) + "/offline/");
      if (off) return off;
    }
    throw err;
  }
}

async function cacheFirst(req) {
  const hit = await caches.match(req);
  if (hit) return hit;
  const res = await fetch(req);
  if (res.ok) (await caches.open(ASSETS)).put(req, res.clone());
  return res;
}

async function staleWhileRevalidate(req) {
  const c = await caches.open(ASSETS);
  const hit = await c.match(req);
  const fresh = fetch(req).then((res) => { if (res.ok) c.put(req, res.clone()); return res; }).catch(() => hit);
  return hit || fresh;
}

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin || !url.pathname.startsWith(BASE + "/")) return;
  const p = url.pathname.slice(BASE.length);
  if (p.startsWith("/downloads/")) return;
  if (p.startsWith("/_next/static/")) return e.respondWith(cacheFirst(req));
  if (/^\\/(fonts|maps|icons|og)\\//.test(p) || p === "/search-index.json" || p === "/learn-quiz.json") return e.respondWith(staleWhileRevalidate(req));
  if (req.mode === "navigate" || p.endsWith(".txt") || req.headers.get("accept")?.includes("text/html")) return e.respondWith(networkFirst(req, PAGES));
});
`;
  return new Response(body, { headers: { "content-type": "text/javascript; charset=utf-8", "cache-control": "no-cache" } });
}
