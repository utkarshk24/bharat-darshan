"use client";
import { createContext, useContext } from "react";

/**
 * Set on the printable profile (`…/print`). Components that hide detail behind a click
 * (source pop-ups, chart/table toggles) show it in full instead, so the PDF keeps every source.
 */
const PrintCtx = createContext(false);

export function PrintModeProvider({ children }: { children: React.ReactNode }) {
  return <PrintCtx.Provider value={true}>{children}</PrintCtx.Provider>;
}

export const usePrintMode = () => useContext(PrintCtx);

/** Opens the browser's print dialog, where "Save as PDF" is one of the destinations. */
export function PrintButton({ label, className }: { label: string; className?: string }) {
  return (
    <button type="button" onClick={() => window.print()} className={className}>
      {label}
    </button>
  );
}
