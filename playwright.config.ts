import { defineConfig } from "@playwright/test";

/**
 * End-to-end tests of the main user journeys.
 * Run against a deployed or locally served static build:
 *   SITE=https://utkarshk24.github.io/bharat-darshan CHROME_PATH=/path/to/chrome npm run test:e2e
 */
export default defineConfig({
  testDir: "./e2e",
  timeout: 60_000,
  retries: process.env.CI ? 1 : 0,
  workers: 2,
  reporter: process.env.CI ? [["list"], ["github"]] : "list",
  use: {
    viewport: { width: 1280, height: 900 },
    launchOptions: { executablePath: process.env.CHROME_PATH || undefined, args: ["--no-sandbox"] },
    serviceWorkers: "allow",
  },
});
