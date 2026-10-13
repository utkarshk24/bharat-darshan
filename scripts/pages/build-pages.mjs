/**
 * npm run build:pages — static build for GitHub Pages (https://<user>.github.io/<repo>/) into out/.
 *
 * GitHub Pages serves files only, so three server features are replaced:
 *  - the locale-detecting proxy → out/index.html picks en/hi/mr from the saved choice or browser language;
 *  - the Kerala → Keralam redirect → small redirect pages at the old addresses;
 *  - the localized catch-all 404 → the site-wide out/404.html.
 *
 * Env: PAGES_BASE_PATH (default "/bharat-darshan"), PAGES_SITE_ORIGIN (default "https://utkarshk24.github.io").
 */
import { spawnSync } from "node:child_process";
import { cpSync, existsSync, mkdirSync, readdirSync, renameSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "../..");
const base = (process.env.PAGES_BASE_PATH ?? "/bharat-darshan").replace(/\/$/, "");
const origin = (process.env.PAGES_SITE_ORIGIN ?? "https://utkarshk24.github.io").replace(/\/$/, "");
const LOCALES = ["en", "hi", "mr"];

// Server-only files are moved aside for the export build and always restored.
const aside = path.join(tmpdir(), `bd-pages-${process.pid}`);
const serverOnly = ["src/proxy.ts", "src/app/[locale]/[...rest]"];
mkdirSync(aside, { recursive: true });
const moved = [];
let status = 1;
try {
  for (const rel of serverOnly) {
    const from = path.join(root, rel);
    if (!existsSync(from)) continue;
    const to = path.join(aside, rel.replace(/[\\/]/g, "__"));
    renameSync(from, to);
    moved.push([to, from]);
  }
  rmSync(path.join(root, "out"), { recursive: true, force: true });
  // Generated route types still list the moved-aside routes; start clean.
  rmSync(path.join(root, ".next"), { recursive: true, force: true });
  const r = spawnSync("npx", ["next", "build"], {
    cwd: root,
    stdio: "inherit",
    env: { ...process.env, STATIC_EXPORT: "1", NEXT_PUBLIC_BASE_PATH: base, NEXT_PUBLIC_SITE_URL: `${origin}${base}` },
  });
  status = r.status ?? 1;
} finally {
  for (const [to, from] of moved) renameSync(to, from);
  rmSync(aside, { recursive: true, force: true });
}
if (status !== 0) process.exit(status);

const out = path.join(root, "out");
const redirectPage = (target, lang = "en") => `<!doctype html><html lang="${lang}"><head><meta charset="utf-8">
<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=${target}">
<link rel="canonical" href="${target}"><title>Bharat Darshan</title></head>
<body><p><a href="${target}">Bharat Darshan →</a></p></body></html>`;

// 1. Root: choose a language like the proxy does (saved choice, then browser languages, then English).
writeFileSync(
  path.join(out, "index.html"),
  `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bharat Darshan · भारत दर्शन</title><link rel="canonical" href="${origin}${base}/en/">
<script>
(function () {
  var L = ${JSON.stringify(LOCALES)}, pick = "en";
  try {
    var c = document.cookie.match(/(?:^|; )NEXT_LOCALE=([a-z]{2})/);
    if (c && L.indexOf(c[1]) >= 0) pick = c[1];
    else {
      var langs = navigator.languages || [navigator.language || "en"];
      for (var i = 0; i < langs.length; i++) { var p = String(langs[i]).slice(0, 2).toLowerCase(); if (L.indexOf(p) >= 0) { pick = p; break; } }
    }
  } catch (e) {}
  location.replace("${base}/" + pick + "/" + location.search + location.hash);
})();
</script>
<noscript><meta http-equiv="refresh" content="0; url=${base}/en/"></noscript></head>
<body><p><a href="${base}/en/">English</a> · <a href="${base}/hi/" lang="hi">हिन्दी</a> · <a href="${base}/mr/" lang="mr">मराठी</a></p></body></html>`,
);

// 2. Kerala → Keralam: one redirect page per old address (profile + every module).
let redirects = 0;
for (const l of LOCALES) {
  const dir = path.join(out, l, "states", "keralam");
  if (!existsSync(dir)) continue;
  const subs = ["", ...readdirSync(dir, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name)];
  for (const s of subs) {
    const target = `${base}/${l}/states/keralam/${s ? `${s}/` : ""}`;
    const at = path.join(out, l, "states", "kerala", s);
    mkdirSync(at, { recursive: true });
    writeFileSync(path.join(at, "index.html"), redirectPage(target, l));
    redirects++;
  }
}

// 3. Jekyll would hide the _next folder; .nojekyll turns it off.
writeFileSync(path.join(out, ".nojekyll"), "");
if (!existsSync(path.join(out, "404.html"))) cpSync(path.join(out, "_not-found", "index.html"), path.join(out, "404.html"));

console.log(`build:pages: out/ ready for ${origin}${base}/ (root language picker + ${redirects} Kerala redirect pages)`);
