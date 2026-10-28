"use client";
import { useEffect } from "react";

/** Registers /sw.js in production builds so visited pages stay readable offline. */
export function ServiceWorker() {
  useEffect(() => {
    if (process.env.NODE_ENV !== "production" || !("serviceWorker" in navigator)) return;
    const base = process.env.NEXT_PUBLIC_BASE_PATH ?? "";
    navigator.serviceWorker.register(`${base}/sw.js`, { scope: `${base}/` }).catch(() => {
      /* offline support is a progressive enhancement */
    });
  }, []);
  return null;
}
