import { describe, expect, it } from "vitest";
import { DOWNLOADS, profileCodes, profileJson } from "@/lib/exports";
import { getCompare } from "@/lib/data";

const lines = (s: string) => s.replace(/^﻿/, "").trimEnd().split("\r\n");

describe("Data Library downloads", () => {
  it("builds every file without throwing, with a header and rows", () => {
    for (const d of DOWNLOADS) {
      const body = d.build();
      if (d.kind === "json") expect(() => JSON.parse(body)).not.toThrow();
      else expect(lines(body).length).toBeGreaterThan(1);
    }
  });

  it("has one indicators row per region and indicator, plus India", () => {
    const c = getCompare()!;
    const n = c.groups.reduce((a, g) => a + g.indicators.length, 0);
    const body = DOWNLOADS.find((d) => d.file === "indicators.csv")!.build();
    expect(lines(body).length - 1).toBe(n * (c.regions.length + 1));
  });

  it("marks missing values as not_available instead of inventing them", () => {
    const body = DOWNLOADS.find((d) => d.file === "indicators.csv")!.build();
    const rows = lines(body).slice(1);
    const missing = rows.filter((r) => r.includes(",not_available,"));
    expect(missing.length).toBeGreaterThan(0);
  });

  it("publishes a full profile for each of the 36 regions", () => {
    const codes = profileCodes();
    expect(codes).toHaveLength(36);
    const mh = JSON.parse(profileJson("IN-MH")!);
    expect(mh.region.code).toBe("IN-MH");
    expect(Object.keys(mh.modules).length).toBeGreaterThan(20);
  });
});
