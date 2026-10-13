/**
 * npm run check:links — offline check of every internal link in the static export (out/).
 * Each href/src that points inside the site must resolve to a file (or a folder with index.html).
 * Run after `npm run build:pages`. Exits 1 if any link is broken.
 */
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "../..");
const out = path.join(root, "out");
const base = (process.env.PAGES_BASE_PATH ?? "/bharat-darshan").replace(/\/$/, "");
if (!existsSync(out)) {
  console.error("check:links: out/ not found — run npm run build:pages first");
  process.exit(1);
}

const html = [];
(function walk(d) {
  for (const e of readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p);
    else if (e.name.endsWith(".html")) html.push(p);
  }
})(out);

const resolves = (url) => {
  let p = decodeURIComponent(url.split(/[?#]/)[0]);
  if (!p.startsWith(base + "/") && p !== base) return null; // outside the site (or another origin's path)
  p = p.slice(base.length) || "/";
  const f = path.join(out, p);
  if (existsSync(f) && statSync(f).isFile()) return true;
  return existsSync(path.join(f, "index.html")) || existsSync(f + ".html");
};

const broken = new Map();
let checked = 0;
const attr = /\b(?:href|src)="([^"]+)"/g;
for (const file of html) {
  const s = readFileSync(file, "utf8");
  for (const m of s.matchAll(attr)) {
    const url = m[1].replace(/&amp;/g, "&");
    if (!url.startsWith("/") || url.startsWith("//")) continue;
    const ok = resolves(url);
    if (ok === null) {
      // An absolute path without the base path would 404 on GitHub Pages.
      if (url !== "/") (broken.get(url) ?? broken.set(url, []).get(url)).push(path.relative(out, file));
      continue;
    }
    checked++;
    if (!ok) (broken.get(url) ?? broken.set(url, []).get(url)).push(path.relative(out, file));
  }
}

if (broken.size) {
  console.error(`check:links: ${broken.size} broken internal link(s):`);
  for (const [url, files] of [...broken].slice(0, 50)) console.error(`  ${url}  ← ${files.slice(0, 3).join(", ")}${files.length > 3 ? ` (+${files.length - 3} more)` : ""}`);
  process.exit(1);
}
console.log(`check:links: ${checked} internal links in ${html.length} pages, all resolve`);
