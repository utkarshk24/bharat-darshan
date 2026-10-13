/**
 * npm run og — renders the social-preview (Open Graph) images into public/og/<locale>/<key>.png.
 *
 * Why Chromium and not next/og: Satori, the engine behind next/og, does not shape complex
 * scripts, so Devanagari halants show and i-matras land on the wrong letter. Headless
 * Chromium shapes Hindi and Marathi correctly.
 *
 * Drives a locally installed Chrome or Chromium through playwright-core (no browser download):
 * set CHROME=/path/to/chrome, otherwise common install paths are tried.
 * Re-run after changing region names, capitals or the dataset date.
 */
import { chromium } from "playwright-core";
import { existsSync, mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { Region } from "../../src/lib/schema";
import { formatDate } from "../../src/lib/format";

const root = path.resolve(import.meta.dirname, "../..");
const LOCALES = ["en", "hi", "mr"] as const;
type L = (typeof LOCALES)[number];

const chrome =
  process.env.CHROME ??
  ["/opt/google/chrome/chrome", "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser", "/opt/pw-browsers/chromium",
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"].find(existsSync);
if (!chrome) {
  console.error("og: no Chrome/Chromium found. Set CHROME=/path/to/chrome.");
  process.exit(1);
}

const read = (p: string) => JSON.parse(readFileSync(path.join(root, p), "utf8"));
const msgs: Record<L, Record<string, Record<string, string>>> = { en: read("messages/en.json"), hi: read("messages/hi.json"), mr: read("messages/mr.json") };
const regions = readdirSync(path.join(root, "data/regions")).filter((f) => f.endsWith(".json")).map((f) => Region.parse(read(`data/regions/${f}`)));
const india = Region.parse(read("data/india.json"));
const asOn = [india, ...regions].map((r) => r.meta.lastUpdated).sort().at(-1)!;

const fontDir = path.join(root, "node_modules/@fontsource-variable/noto-sans-devanagari/files");
const font = (subset: string) => `file://${path.join(fontDir, `noto-sans-devanagari-${subset}-wght-normal.woff2`)}`;
const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

function html({ accent = "#14213d", eyebrow, title, subtitle, line, footer }: { accent?: string; eyebrow?: string; title: string; subtitle?: string; line?: string; footer: string }) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Noto;src:url(${font("devanagari")}) format("woff2");font-weight:100 900;unicode-range:U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+25CC,U+A830-A839,U+A8E0-A8FF}
@font-face{font-family:Noto;src:url(${font("latin")}) format("woff2");font-weight:100 900;unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
@font-face{font-family:Noto;src:url(${font("latin-ext")}) format("woff2");font-weight:100 900;unicode-range:U+0100-024F,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF}
*{margin:0;box-sizing:border-box}
html,body{width:1200px;height:630px;overflow:hidden}
body{font-family:Noto,sans-serif;background:#fbf8f3;color:#14213d;display:flex;flex-direction:column}
.bar{height:16px;background:${accent}}
.main{flex:1;display:flex;flex-direction:column;padding:52px 72px 40px}
.eyebrow{font-size:30px;color:#5b6475}
h1{font-size:${title.length > 22 ? 74 : 96}px;font-weight:700;line-height:1.2;margin-top:12px}
.sub{font-size:36px;color:#2b3445;margin-top:10px;line-height:1.35}
.line{font-size:30px;color:#2b3445;margin-top:22px}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:26px;color:#5b6475}
.brand{display:flex;align-items:center;gap:12px;font-weight:700;color:#14213d}
.dot{width:14px;height:14px;border-radius:50%}
</style></head><body><div class="bar"></div><div class="main">
${eyebrow ? `<div class="eyebrow">${esc(eyebrow)}</div>` : ""}
<h1>${esc(title)}</h1>
${subtitle ? `<div class="sub">${esc(subtitle)}</div>` : ""}
${line ? `<div class="line">${esc(line)}</div>` : ""}
<div class="foot"><div class="brand"><span class="dot" style="background:#e07a1f"></span><span class="dot" style="background:#14213d"></span><span class="dot" style="background:#2e7d32"></span><span style="margin-left:4px">Bharat Darshan · भारत दर्शन</span></div><div>${esc(footer)}</div></div>
</div></body></html>`;
}

const tmp = path.join(tmpdir(), `bd-og-${process.pid}`);
mkdirSync(tmp, { recursive: true });
const browser = await chromium.launch({ executablePath: chrome, args: ["--no-sandbox"] });
const tab = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
let n = 0;
async function shoot(locale: L, key: string, page: string) {
  const out = path.join(root, "public/og", locale, `${key}.png`);
  mkdirSync(path.dirname(out), { recursive: true });
  const src = path.join(tmp, `${locale}-${key}.html`);
  writeFileSync(src, page);
  await tab.goto(`file://${src}`);
  await tab.evaluate(() => document.fonts.ready);
  await tab.screenshot({ path: out });
  n++;
}

const pick = (v: { en: string; hi?: string | null; mr?: string | null }, l: L) => v[l] || v.en;

for (const l of LOCALES) {
  const c = msgs[l].common;
  const dataAsOn = c.dataAsOn.replace("{date}", formatDate(asOn, l));
  await shoot(l, "home", html({ title: c.siteName, subtitle: c.tagline, footer: "English · हिन्दी · मराठी" }));
  await shoot(l, "india", html({ eyebrow: c.siteName, title: msgs[l].nav.india, subtitle: msgs[l].home.indiaIntro, footer: `IN · ${dataAsOn}` }));
  for (const r of regions) {
    const title = pick(r.name, l);
    const others = [...new Set(LOCALES.filter((x) => x !== l).map((x) => pick(r.name, x)))].filter((x) => x !== title);
    const caps = [...new Set(r.capitals.map((cap) => pick(cap.name, l)))];
    await shoot(l, `${r.type === "state" ? "states" : "uts"}-${r.slug}`, html({
      accent: r.accent,
      eyebrow: r.type === "state" ? c.state : c.ut,
      title,
      subtitle: others.join(" · "),
      line: caps.length ? `${caps.length > 1 ? c.capitals : c.capital}: ${caps.join(" · ")}` : undefined,
      footer: `${r.code} · ${dataAsOn}`,
    }));
  }
}
await browser.close();
rmSync(tmp, { recursive: true, force: true });
console.log(`og: wrote ${n} images to public/og (data as on ${asOn})`);
