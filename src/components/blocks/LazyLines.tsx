"use client";
import dynamic from "next/dynamic";
import { useEffect, useRef, useState } from "react";
import type { LinesProps } from "./SeriesLines";

const SeriesLines = dynamic(() => import("./SeriesLines"), { ssr: false, loading: () => null });

/**
 * Loads the chart library only when the chart is about to scroll into view.
 * Recharts measures its container, so it never rendered on the server anyway; the box keeps its
 * height meanwhile (no layout shift), and the table view and CSV download work without it.
 */
export function LazyLines(props: LinesProps) {
  const ref = useRef<HTMLDivElement>(null);
  const [show, setShow] = useState(false);
  useEffect(() => {
    const el = ref.current;
    if (!el || show) return;
    if (typeof IntersectionObserver === "undefined") return setShow(true);
    const io = new IntersectionObserver((es) => es.some((e) => e.isIntersecting) && setShow(true), { rootMargin: "200px" });
    io.observe(el);
    return () => io.disconnect();
  }, [show]);
  return <div ref={ref} className="h-full w-full">{show && <SeriesLines {...props} />}</div>;
}
