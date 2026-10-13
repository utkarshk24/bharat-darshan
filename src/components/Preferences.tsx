"use client";
import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from "react";

type Digits = "latin" | "devanagari";
type Theme = "light" | "dark";
interface Prefs {
  digits: Digits;
  setDigits: (d: Digits) => void;
  theme: Theme;
  setTheme: (t: Theme) => void;
}

const Ctx = createContext<Prefs>({ digits: "latin", setDigits: () => {}, theme: "light", setTheme: () => {} });

function store(key: string, value: string) {
  try {
    localStorage.setItem(key, value);
  } catch {
    /* storage may be unavailable (private mode) — preference just won't persist */
  }
}
function load(key: string): string | null {
  try {
    return localStorage.getItem(key);
  } catch {
    return null;
  }
}

export function PreferencesProvider({ children }: { children: ReactNode }) {
  const [digits, setDigitsState] = useState<Digits>("latin");
  const [theme, setThemeState] = useState<Theme>("light");

  useEffect(() => {
    if (load("bd-digits") === "devanagari") setDigitsState("devanagari");
    setThemeState(document.documentElement.classList.contains("dark") ? "dark" : "light");
  }, []);

  const setDigits = useCallback((d: Digits) => {
    setDigitsState(d);
    store("bd-digits", d);
  }, []);
  const setTheme = useCallback((t: Theme) => {
    setThemeState(t);
    document.documentElement.classList.toggle("dark", t === "dark");
    document.documentElement.style.colorScheme = t;
    store("bd-theme", t);
  }, []);

  return <Ctx.Provider value={{ digits, setDigits, theme, setTheme }}>{children}</Ctx.Provider>;
}

export const usePreferences = () => useContext(Ctx);

/** Runs before first paint so dark mode never flashes. */
export const themeScript = `(function(){try{var t=localStorage.getItem('bd-theme');if(!t)t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';if(t==='dark')document.documentElement.classList.add('dark');document.documentElement.style.colorScheme=t;}catch(e){}})();`;
