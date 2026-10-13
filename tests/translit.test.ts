import { describe, expect, it } from "vitest";
import { phoneticKey } from "@/lib/translit";

const same = (...xs: string[]) => {
  const keys = xs.map(phoneticKey);
  expect(new Set(keys).size, `${xs.join(" / ")} → ${keys.join(" / ")}`).toBe(1);
};

describe("cross-script phonetic keys", () => {
  it("matches Pune / पुणे / puney", () => same("Pune", "पुणे", "puney"));
  it("matches Mumbai / मुंबई", () => same("Mumbai", "मुंबई"));
  it("matches Maharashtra in both scripts", () => same("Maharashtra", "महाराष्ट्र"));
  it("matches Kerala / केरळ / केरल", () => same("Kerala", "केरळ", "केरल"));
  it("matches Nashik / नाशिक / नासिक", () => same("Nashik", "नाशिक", "नासिक"));
  it("matches Thiruvananthapuram / तिरुवनंतपुरम", () => same("Thiruvananthapuram", "तिरुवनंतपुरम"));
  it("matches Ladakh / लद्दाख / लडाख", () => same("Ladakh", "लद्दाख", "लडाख"));
});
