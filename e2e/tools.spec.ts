import { expect, test } from "@playwright/test";
import { SITE, go } from "./site";

test("compare: picking a region updates the table and the shareable address", async ({ page }) => {
  await go(page, "/en/compare/?ids=MH,KL");
  await expect(page.getByRole("columnheader", { name: "Maharashtra" })).toBeVisible();
  await page.getByRole("button", { name: "Goa", exact: true }).click();
  await expect(page.getByRole("columnheader", { name: "Goa" })).toBeVisible();
  await expect(page).toHaveURL(/ids=.*GA/);
});

test("rankings: indicator and scope come from the address and lists are ordered", async ({ page }) => {
  await go(page, "/en/rankings/?i=ur&scope=state");
  await expect(page.getByRole("heading", { level: 2, name: /Unemployment/ })).toBeVisible();
  const rows = page.locator("tbody tr");
  await expect(rows.first()).toBeVisible();
  const ranks = (await page.locator("tbody tr td:first-child").allInnerTexts()).map((t) => parseInt(t, 10));
  expect(ranks).toEqual([...ranks].sort((a, b) => a - b));
  await expect(page.getByText("Union Territory", { exact: true })).toHaveCount(0);
});

test("map: a data layer from the address shows its legend and a region's value", async ({ page }) => {
  await go(page, "/en/map/#theme=c-stunting&on=labels,capitals&r=IN-BR");
  await expect(page.getByText(/stunted/i).first()).toBeVisible({ timeout: 20_000 });
  await expect(page.getByText(/2019-21/).first()).toBeVisible();
  await expect(page.getByRole("heading", { name: "Bihar" }).or(page.getByText("Bihar").first())).toBeVisible();
});

test("data library: downloads are real CSV with provenance columns", async ({ page, request }) => {
  await go(page, "/en/data/");
  const href = await page.locator('a[href$="/downloads/indicators.csv"]').getAttribute("href");
  const res = await request.get(new URL(href!, SITE + "/").toString());
  expect(res.ok()).toBeTruthy();
  const head = (await res.text()).replace(/^﻿/, "").split(/\r?\n/)[0];
  for (const col of ["region_code", "value", "status", "source", "url", "access_date"]) expect(head).toContain(col);
  await expect(page.getByText(/CC BY 4\.0/).first()).toBeVisible();
});

test("learn: answering shows feedback and the source", async ({ page }) => {
  await go(page, "/en/learn/");
  const first = page.locator("ul button").first();
  await expect(first).toBeVisible({ timeout: 15_000 });
  await first.click();
  await expect(page.locator("#q-feedback")).toContainText(/Correct|Not quite/);
  await expect(page.getByRole("button", { name: /Next question|See my score/ })).toBeVisible();
});

test("trip planner: a shared plan loads with the closest route and the month", async ({ page }) => {
  await go(page, "/en/trip-planner/?r=IN-MH&d=4&m=11");
  await expect(page.getByRole("heading", { level: 2, name: /Maharashtra/ })).toBeVisible();
  await expect(page.getByText(/no 4-day route/)).toBeVisible();
  await expect(page.getByText(/November falls in a season/)).toBeVisible();
});

test("corrections: the source box links to a pre-filled report form", async ({ page }) => {
  await go(page, "/en/states/goa/");
  await page.locator("button[aria-expanded]").first().click();
  const href = await page.getByRole("link", { name: /Suggest a correction/ }).first().getAttribute("href");
  const u = new URL(href!);
  expect(u.hostname).toBe("github.com");
  expect(u.searchParams.get("template")).toBe("correction.yml");
  expect(u.searchParams.get("page")).toContain("/en/states/goa/");
});

test("print: a profile opens as one printable document with every source written out", async ({ page }) => {
  await go(page, "/en/states/goa/");
  await page.getByRole("link", { name: "Print or save as PDF" }).click();
  await expect(page).toHaveURL(/\/states\/goa\/print\/?$/);
  await expect(page.getByRole("heading", { level: 1, name: "Goa" })).toBeVisible();
  // Contents plus all 26 sections.
  await expect(page.locator("section.print-module > div > h2, section.print-module > h2")).toHaveCount(26);
  await expect(page.getByRole("button", { name: "Save as PDF or print" })).toBeVisible();
  // Series show as tables, sources as full addresses; no pop-up buttons left.
  await expect(page.getByRole("button", { name: /Show table|Show chart/ })).toHaveCount(0);
  expect(await page.locator("a.print-url").count()).toBeGreaterThan(10);
  await expect(page.locator('meta[name="robots"]')).toHaveAttribute("content", /noindex/);
  await page.emulateMedia({ media: "print" });
  await expect(page.locator("body > div header, header.sticky").first()).toBeHidden();
  await expect(page.getByRole("button", { name: "Save as PDF or print" })).toBeHidden();
});
