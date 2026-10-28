import type { TripItinerary } from "./trip";

/** The authored itinerary closest to the chosen length: exact, else the longest shorter one, else the shortest. */
export function pickItinerary(list: TripItinerary[], days: number): TripItinerary | null {
  const known = list.filter((i) => i.days !== null);
  if (!known.length) return list[0] ?? null;
  return (
    known.find((i) => i.days === days) ??
    [...known].filter((i) => i.days! < days).sort((a, b) => b.days! - a.days!)[0] ??
    [...known].sort((a, b) => a.days! - b.days!)[0]
  );
}
