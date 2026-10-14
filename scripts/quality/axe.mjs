// WCAG 2.1 AA scan of key pages with axe-core, driven by playwright-core.
// Usage: SITE=https://host/base CHROME_PATH=/path/to/chrome node scripts/quality/axe.mjs
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { chromium } from "playwright-core";

const require = createRequire(import.meta.url);
const AXE = readFileSync(require.resolve("axe-core/axe.min.js"), "utf8");
const SITE = (process.env.SITE || "http://localhost:3200/bharat-darshan").replace(/\/$/, "");
const PATHS = [
  "/en/", "/hi/", "/mr/",
  "/en/states/maharashtra/", "/hi/uts/ladakh/economy/",
  "/en/compare/", "/en/gi/", "/mr/projects/", "/en/themes/economy/",
  "/en/states/karnataka/", "/hi/states/west-bengal/government/", "/mr/states/gujarat/gi/",
];
const TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"];

const browser = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined, args: ["--no-sandbox"] });
let failed = 0;
for (const path of PATHS) {
  const page = await browser.newPage({ viewport: { width: 1366, height: 900 } });
  try {
    await page.goto(SITE + path, { waitUntil: "networkidle", timeout: 90_000 });
    await page.addScriptTag({ content: AXE });
    const violations = await page.evaluate(async (tags) => {
      // eslint-disable-next-line no-undef
      const r = await axe.run(document, { runOnly: { type: "tag", values: tags } });
      return r.violations.map((v) => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, sample: v.nodes.slice(0, 3).map((n) => n.target.join(" ")) }));
    }, TAGS);
    if (violations.length) {
      failed++;
      console.log(`✗ ${path}`);
      for (const v of violations) console.log(`   ${v.id} (${v.impact}, ${v.nodes} nodes): ${v.sample.join(" | ")}`);
    } else {
      console.log(`✓ ${path}`);
    }
  } catch (e) {
    failed++;
    console.log(`✗ ${path} — could not load: ${e.message.split("\n")[0]}`);
  }
  await page.close();
}
await browser.close();
console.log(`axe: ${PATHS.length - failed}/${PATHS.length} pages clean`);
process.exit(failed ? 1 : 0);
