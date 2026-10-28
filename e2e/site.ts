import type { Page } from "@playwright/test";

/** Base address of the site under test, without a trailing slash. */
export const SITE = (process.env.SITE || "http://localhost:3200/bharat-darshan").replace(/\/$/, "");
export const go = (page: Page, path: string) => page.goto(SITE + path, { waitUntil: "domcontentloaded" });
