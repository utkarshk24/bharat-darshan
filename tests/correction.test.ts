import { describe, expect, it } from "vitest";
import { readFileSync } from "node:fs";
import path from "node:path";
import { correctionUrl } from "@/lib/correction";

describe("correction links", () => {
  it("pre-fill the issue form's fields by id", () => {
    const u = new URL(correctionUrl({ page: "https://x.test/en/states/goa/", item: "Population — Census of India · 2011", locale: "mr" }));
    expect(u.searchParams.get("template")).toBe("correction.yml");
    expect(u.searchParams.get("page")).toBe("https://x.test/en/states/goa/");
    expect(u.searchParams.get("item")).toContain("Population");
    expect(u.searchParams.get("language")).toBe("मराठी");
  });

  it("only use field ids that exist in the issue form", () => {
    const form = readFileSync(path.resolve(__dirname, "../.github/ISSUE_TEMPLATE/correction.yml"), "utf8");
    for (const id of ["page", "item", "language"]) expect(form).toMatch(new RegExp(`id: ${id}\\b`));
    for (const opt of ["English", "हिंदी", "मराठी"]) expect(form).toContain(opt);
  });
});
