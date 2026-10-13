import { describe, expect, it } from "vitest";
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import path from "node:path";

/**
 * The regional-script fonts are subset to the characters in use (npm run fonts).
 * If new text adds a character the subset lacks, it would render in a fallback font —
 * this test fails first and says to re-run the subsetter.
 */
const root = path.resolve(__dirname, "..");
const BLOCKS: Record<string, [number, number]> = {
  bengali: [0x0980, 0x09ff],
  gurmukhi: [0x0a00, 0x0a7f],
  gujarati: [0x0a80, 0x0aff],
  oriya: [0x0b00, 0x0b7f],
  tamil: [0x0b80, 0x0bff],
  telugu: [0x0c00, 0x0c7f],
  kannada: [0x0c80, 0x0cff],
  malayalam: [0x0d00, 0x0d7f],
};

function files(dir: string, ext: RegExp, acc: string[] = []): string[] {
  for (const e of readdirSync(dir)) {
    const p = path.join(dir, e);
    if (statSync(p).isDirectory()) files(p, ext, acc);
    else if (ext.test(e)) acc.push(p);
  }
  return acc;
}

describe("regional font subsets", () => {
  const covered: Record<string, string> = JSON.parse(readFileSync(path.join(root, "src/app/fonts/regional-chars.json"), "utf8"));
  const sources = [
    ...files(path.join(root, "data"), /\.json$/),
    ...files(path.join(root, "messages"), /\.json$/),
    ...files(path.join(root, "src"), /\.tsx?$/),
  ];
  const used: Record<string, Set<string>> = Object.fromEntries(Object.keys(BLOCKS).map((k) => [k, new Set<string>()]));
  for (const f of sources) {
    for (const ch of new Set(readFileSync(f, "utf8"))) {
      const o = ch.codePointAt(0)!;
      for (const [k, [lo, hi]] of Object.entries(BLOCKS)) if (o >= lo && o <= hi) used[k].add(ch);
    }
  }

  for (const k of Object.keys(BLOCKS)) {
    it(`${k} subset covers every ${k} character in the site`, () => {
      const missing = [...used[k]].filter((ch) => !covered[k]?.includes(ch));
      expect(missing, `run \`npm run fonts\` — missing: ${missing.join(" ")}`).toEqual([]);
      if (used[k].size) expect(existsSync(path.join(root, `src/app/fonts/regional/${k}.woff2`))).toBe(true);
    });
  }
});
