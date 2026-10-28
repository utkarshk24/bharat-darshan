import { describe, expect, it } from "vitest";
import { buildTrip, daysOf, monthsOf, tripRegions } from "@/lib/trip";

describe("trip planner", () => {
  it("reads season labels as months, wrapping the year end", () => {
    expect(monthsOf("October to February")).toEqual([10, 11, 12, 1, 2]);
    expect(monthsOf("February–March (Navratri)")).toEqual([2, 3]);
    expect(monthsOf("September–October (Navratri)")).toEqual([9, 10]);
    expect(monthsOf("May and October")).toEqual([5, 10]);
    expect(monthsOf("April")).toEqual([4]);
    expect(monthsOf("Monsoon")).toBeNull();
  });

  it("reads trip lengths from itinerary ids", () => {
    expect(daysOf("d3")).toBe(3);
    expect(daysOf("d2m")).toBe(2);
    expect(daysOf("x")).toBeNull();
  });

  it("parses every authored season label that names a month", () => {
    for (const r of tripRegions()) {
      const t = buildTrip(r.code)!;
      for (const s of t.seasons) if (/january|february|march|april|may|june|july|august|september|october|november|december/i.test(s.label.en)) expect(s.months?.length).toBeGreaterThan(0);
    }
  });

  it("covers most regions", () => {
    expect(tripRegions().length).toBeGreaterThanOrEqual(30);
  });
});

import { pickItinerary } from "@/lib/tripPick";
describe("closest itinerary", () => {
  const L = (en: string) => ({ en, hi: en, mr: en });
  const list = [2, 3, 5].map((d) => ({ id: `d${d}`, days: d, label: L(`${d} days`), detail: null }));
  it("prefers an exact match, then the longest shorter route, then the shortest", () => {
    expect(pickItinerary(list, 3)?.id).toBe("d3");
    expect(pickItinerary(list, 4)?.id).toBe("d3");
    expect(pickItinerary(list, 7)?.id).toBe("d5");
    expect(pickItinerary(list, 1)?.id).toBe("d2");
    expect(pickItinerary([], 3)).toBeNull();
  });
});
