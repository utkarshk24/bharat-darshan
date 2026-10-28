import { expect, test } from "@playwright/test";
import { SITE, go } from "./site";

test("home page search finds a GI product and opens it", async ({ page }) => {
  await go(page, "/en/");
  const box = page.getByRole("combobox");
  await box.click();
  await box.fill("paithani");
  const option = page.getByRole("option", { name: /Paithani/ });
  await expect(option).toBeVisible();
  await option.click();
  await expect(page).toHaveURL(/\/en\/gi\/paithani/);
  await expect(page.getByRole("heading", { level: 1 })).toContainText("Paithani");
});

test("language switch keeps the reader on the same profile", async ({ page }) => {
  await go(page, "/en/states/maharashtra/");
  await page.getByRole("link", { name: "मराठी" }).or(page.locator('a[hreflang="mr"]')).first().click();
  await expect(page).toHaveURL(/\/mr\/states\/maharashtra\//);
  await expect(page.locator("html")).toHaveAttribute("lang", "mr");
  await expect(page.getByRole("heading", { level: 1 })).toContainText("महाराष्ट्र");
});

test("profile sections open from the section navigation", async ({ page }) => {
  await go(page, "/en/states/goa/");
  await page.locator('a[href$="/en/states/goa/economy/"]').first().click();
  await expect(page).toHaveURL(/\/en\/states\/goa\/economy\//);
  await expect(page.getByRole("heading", { level: 1 })).toBeVisible();
});

test("old Kerala address leads to Keralam", async ({ page }) => {
  await go(page, "/en/states/kerala/");
  await expect(page).toHaveURL(/\/en\/states\/keralam\//, { timeout: 15_000 });
});

test("unknown pages show the not-found page", async ({ page }) => {
  const res = await page.goto(`${SITE}/en/no-such-page/`);
  expect(res?.status()).toBe(404);
  await expect(page.locator("body")).toContainText(/not found|couldn't find/i);
});
