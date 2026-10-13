import { describe, expect, it } from "vitest";
import { changeTone, formatCompactIndian, formatIndianNumber, formatPeriod, formatRupeeCrore, toDevanagariDigits } from "@/lib/format";

describe("Indian number formatting", () => {
  it("groups by lakh/crore in every locale", () => {
    expect(formatIndianNumber(112374333, "en")).toBe("11,23,74,333");
    expect(formatIndianNumber(112374333, "hi")).toBe("11,23,74,333");
    expect(formatIndianNumber(112374333, "mr")).toBe("11,23,74,333");
  });
  it("compacts with localised scale words", () => {
    expect(formatCompactIndian(112374333, "en")).toBe("11.24 crore");
    expect(formatCompactIndian(112374333, "hi")).toBe("11.24 करोड़");
    expect(formatCompactIndian(112374333, "mr")).toBe("11.24 कोटी");
    expect(formatCompactIndian(250000, "en")).toBe("2.5 lakh");
    expect(formatCompactIndian(64473, "en")).toBe("64,473");
  });
  it("formats ₹ crore into lakh crore", () => {
    expect(formatRupeeCrore(3645000, "en")).toBe("₹36.45 lakh crore");
    expect(formatRupeeCrore(52000, "mr")).toBe("₹52,000 कोटी");
  });
  it("converts to Devanagari numerals", () => {
    expect(toDevanagariDigits("11,23,74,333")).toBe("११,२३,७४,३३३");
    expect(formatIndianNumber(929, "mr", { digits: "devanagari" })).toBe("९२९");
  });
  it("labels financial years explicitly", () => {
    expect(formatPeriod("FY2023-24", "en")).toBe("FY 2023-24");
    expect(formatPeriod("FY2023-24", "mr")).toBe("आर्थिक वर्ष 2023-24");
    expect(formatPeriod("2011", "hi")).toBe("2011");
  });
});

describe("change badges colour by improvement, not direction", () => {
  it("IMR falling is good, unemployment rising is bad", () => {
    expect(changeTone(-2, "lower-is-better")).toBe("good");
    expect(changeTone(1.5, "lower-is-better")).toBe("bad");
    expect(changeTone(3, "higher-is-better")).toBe("good");
    expect(changeTone(0, "higher-is-better")).toBe("neutral");
  });
});

describe("dates", () => {
  it("formats deterministically in all locales", async () => {
    const { formatDate } = await import("@/lib/format");
    expect(formatDate("2026-10-13", "en")).toBe("13 October 2026");
    expect(formatDate("2026-10-13", "hi")).toBe("13 अक्टूबर 2026");
    expect(formatDate("2026-10-13", "mr")).toBe("13 ऑक्टोबर 2026");
  });
});
