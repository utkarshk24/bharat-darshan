import { defineConfig } from "vitest/config";
import path from "node:path";

export default defineConfig({
  resolve: { alias: { "@": path.resolve(import.meta.dirname, "src"), "@data": path.resolve(import.meta.dirname, "data"),
      // data.ts is server-only in the app; tests run it in Node directly.
      "server-only": path.resolve(import.meta.dirname, "tests/stubs/empty.ts") } },
  test: { include: ["tests/**/*.test.ts"] },
});
