import { describe, expect, it } from "vitest";
import { GET } from "@/app/sw.js/route";
import manifest from "@/app/manifest";

describe("offline support", () => {
  it("generates a service worker that parses and never caches downloads", async () => {
    const js = await GET().text();
    expect(() => new Function(js)).not.toThrow();
    expect(js).toContain('p.startsWith("/downloads/")');
    expect(js).toMatch(/VERSION = "\d{4}-\d{2}-\d{2}-\d+"/);
  });

  it("has an installable manifest with standard and maskable icons", () => {
    const m = manifest();
    expect(m.display).toBe("standalone");
    expect(m.icons?.some((i) => i.sizes === "512x512" && i.purpose === "maskable")).toBe(true);
    expect(m.icons?.some((i) => i.sizes === "192x192")).toBe(true);
  });
});
