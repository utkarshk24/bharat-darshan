"use client";
import { useEffect } from "react";

/** On mobile, scrolls the active module tab into view in the horizontal tab strip. */
export function ScrollActiveTab({ containerId }: { containerId: string }) {
  useEffect(() => {
    const el = document.getElementById(containerId)?.querySelector<HTMLElement>('[aria-current="page"]');
    if (el && window.matchMedia("(max-width: 1023px)").matches) el.scrollIntoView({ inline: "center", block: "nearest" });
  }, [containerId]);
  return null;
}
