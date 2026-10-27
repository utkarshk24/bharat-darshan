import { describe, expect, it } from "vitest";
import { buildQuizBank } from "@/lib/quiz";

describe("Learn quiz bank", () => {
  const bank = buildQuizBank();

  it("has questions of every kind", () => {
    for (const k of ["capital", "gi", "office", "data"]) expect(bank.filter((q) => q.kind === k).length).toBeGreaterThan(5);
  });

  it("gives every question four distinct options and one valid answer", () => {
    for (const q of bank) {
      expect(q.options).toHaveLength(4);
      expect(new Set(q.options.map((o) => o.en)).size).toBe(4);
      expect(q.answer).toBeGreaterThanOrEqual(0);
      expect(q.answer).toBeLessThan(4);
    }
  });

  it("cites a source for every non-capital question", () => {
    for (const q of bank.filter((x) => x.kind !== "capital")) expect(q.source.url).toMatch(/^https?:\/\//);
  });

  it("marks the right extreme in data questions", () => {
    for (const q of bank.filter((x) => x.kind === "data")) {
      const v = q.values!.map((x) => x.value);
      const want = q.template === "dataLow" ? Math.min(...v) : Math.max(...v);
      expect(v[q.answer]).toBe(want);
      expect(new Set(v).size).toBe(4);
    }
  });

  it("is the same on every build", () => {
    expect(JSON.stringify(buildQuizBank())).toBe(JSON.stringify(bank));
  });

  it("has unique ids", () => {
    expect(new Set(bank.map((q) => q.id)).size).toBe(bank.length);
  });
});
