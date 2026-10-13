"use client";
import { useTranslations } from "next-intl";
import { Moon, Sun } from "lucide-react";
import { usePreferences } from "./Preferences";

export function DisplayToggles() {
  const t = useTranslations("settings");
  const { digits, setDigits, theme, setTheme } = usePreferences();
  return (
    <div className="flex items-center gap-1">
      <button
        type="button"
        onClick={() => setDigits(digits === "latin" ? "devanagari" : "latin")}
        aria-pressed={digits === "devanagari"}
        aria-label={`${t("numerals")}: ${digits === "latin" ? t("devanagariDigits") : t("latinDigits")}`}
        title={t("numerals")}
        className="rounded-md border border-border px-2 py-1.5 text-sm tabular-nums hover:bg-surface-2"
        lang={digits === "latin" ? "hi" : "en"}
      >
        {digits === "latin" ? t("devanagariDigits") : t("latinDigits")}
      </button>
      <button
        type="button"
        onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
        aria-pressed={theme === "dark"}
        aria-label={`${t("theme")}: ${theme === "dark" ? t("light") : t("dark")}`}
        title={t("theme")}
        className="rounded-md border border-border p-2 hover:bg-surface-2"
      >
        {theme === "dark" ? <Sun aria-hidden className="size-4" /> : <Moon aria-hidden className="size-4" />}
      </button>
    </div>
  );
}
