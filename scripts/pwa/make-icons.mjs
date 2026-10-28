/**
 * Render the app icons used by the web app manifest from src/app/icon.svg.
 * Run: node scripts/pwa/make-icons.mjs   (outputs public/icons/*.png; commit them)
 */
import sharp from "sharp";
import { readFileSync } from "node:fs";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "../..");
const svg = readFileSync(path.join(root, "src/app/icon.svg"));
const out = (f) => path.join(root, "public/icons", f);

for (const size of [192, 512]) {
  await sharp(svg, { density: 1200 }).resize(size, size).png().toFile(out(`icon-${size}.png`));
}
// Maskable: the emblem inside the safe zone (central 80%) on the page background colour.
const inner = await sharp(svg, { density: 1200 }).resize(360, 360).png().toBuffer();
await sharp({ create: { width: 512, height: 512, channels: 4, background: "#fbfaf7" } })
  .composite([{ input: inner, gravity: "center" }])
  .png()
  .toFile(out("maskable-512.png"));
console.log("icons written");
