import { expect, test } from "@playwright/test";
import { SITE, go } from "./site";

test("visited pages open offline and others show the offline page", async ({ page, context }) => {
  await go(page, "/en/");
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.reload();
  await go(page, "/en/states/goa/");
  await page.waitForLoadState("networkidle");
  await context.setOffline(true);
  await page.goto(`${SITE}/en/states/goa/`);
  await expect(page).toHaveTitle(/Goa/);
  await page.goto(`${SITE}/en/offline/`);
  await expect(page.getByRole("heading", { level: 1 })).toContainText("offline");
  await expect(page.locator("#saved-h + ul")).toContainText("Goa");
  await context.setOffline(false);
});
