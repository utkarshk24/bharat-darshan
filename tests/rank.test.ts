import { describe, expect, it } from "vitest";
import { rankIndicator } from "@/lib/rank";
import type { CompareIndicator, DataPoint } from "@/lib/schema";

const dp = (value: number | null) => ({ value }) as unknown as DataPoint;
const ind = (polarity: CompareIndicator["polarity"], vals: Record<string, number | null>): CompareIndicator =>
  ({
    id: "x",
    label: { en: "x" },
    kind: "number",
    polarity,
    period: "2011",
    values: Object.fromEntries(Object.entries(vals).map(([k, v]) => [k, dp(v)])),
    national: null,
  }) as unknown as CompareIndicator;

describe("rankIndicator", () => {
  it("ranks higher-is-better from high to low with competition ranks for ties", () => {
    const r = rankIndicator(ind("higher-is-better", { A: 70, B: 90, C: 80, D: 80 }), ["A", "B", "C", "D"]);
    expect(r.rows.map((x) => [x.code, x.rank, x.tied])).toEqual([
      ["B", 1, false],
      ["C", 2, true],
      ["D", 2, true],
      ["A", 4, false],
    ]);
    expect(r.mode).toBe("rank");
  });

  it("ranks lower-is-better from low to high", () => {
    const r = rankIndicator(ind("lower-is-better", { A: 5, B: 2, C: 9 }), ["A", "B", "C"]);
    expect(r.rows.map((x) => x.code)).toEqual(["B", "A", "C"]);
  });

  it("orders neutral indicators by size and labels them as an order, not a rank", () => {
    const r = rankIndicator(ind("neutral", { A: 1, B: 3 }), ["A", "B"]);
    expect(r.rows.map((x) => x.code)).toEqual(["B", "A"]);
    expect(r.mode).toBe("order");
  });

  it("never ranks missing values and keeps them in the given order", () => {
    const r = rankIndicator(ind("higher-is-better", { A: null, B: 1 }), ["C", "A", "B"]);
    expect(r.rows.map((x) => x.code)).toEqual(["B"]);
    expect(r.missing).toEqual(["C", "A"]);
  });

  it("ranks within the scope it is given", () => {
    const i = ind("higher-is-better", { A: 9, B: 8, C: 7 });
    expect(rankIndicator(i, ["B", "C"]).rows[0]).toMatchObject({ code: "B", rank: 1 });
  });
});
