/** Global navigation (Section 5.1) and the build phase each destination lands in. */
export const NAV = [
  { key: "home", href: "/", phase: 1 },
  { key: "states", href: "/states", phase: 1 },
  { key: "uts", href: "/uts", phase: 1 },
  { key: "india", href: "/india", phase: 2 },
  { key: "map", href: "/map", phase: 1 },
  { key: "compare", href: "/compare", phase: 2 },
  { key: "rankings", href: "/rankings", phase: 4 },
  { key: "themes", href: "/themes", phase: 2 },
  { key: "projects", href: "/projects", phase: 2 },
  { key: "gi", href: "/gi", phase: 2 },
  { key: "learn", href: "/learn", phase: 4 },
  { key: "tripPlanner", href: "/trip-planner", phase: 4 },
  { key: "data", href: "/data", phase: 4 },
  { key: "glossary", href: "/glossary", phase: 1 },
  { key: "about", href: "/about", phase: 1 },
  { key: "accessibility", href: "/accessibility", phase: 1 },
] as const;

export const PRIMARY_NAV = ["states", "uts", "map", "compare", "rankings", "gi"] as const;

/** State/UT profile modules A–Z (Section 7), in order. */
export const MODULES = [
  "overview", "geography", "climate", "vibe", "people", "history", "culture", "economy",
  "government", "projects", "transport", "energy", "digital", "education", "health", "nature",
  "water", "safety", "gi", "tourism", "cities", "sports", "personalities", "diaspora", "civic", "trivia",
] as const;
export type ModuleKey = (typeof MODULES)[number];

/** Featured comparisons on the home page (Section 6). Editorial groupings of ISO codes. */
export const FEATURED_COMPARISONS = [
  { key: "cmpNorthSouth", group: "north-south", ids: ["IN-HR", "IN-HP", "IN-PB", "IN-RJ", "IN-AP", "IN-KA", "IN-KL", "IN-TN", "IN-TG"] },
  { key: "cmpCoastal", group: "coastal", ids: ["IN-GJ", "IN-MH", "IN-GA", "IN-KA", "IN-KL", "IN-TN", "IN-AP", "IN-OR", "IN-WB"] },
  { key: "cmpHimalayan", group: "himalayan", ids: ["IN-JK", "IN-LA", "IN-HP", "IN-UK", "IN-SK", "IN-AR"] },
  { key: "cmpNortheast", group: "northeast", ids: ["IN-AR", "IN-AS", "IN-MN", "IN-ML", "IN-MZ", "IN-NL", "IN-SK", "IN-TR"] },
  { key: "cmpIslands", group: "islands", ids: ["IN-AN", "IN-LD"] },
  { key: "cmpLargeSmall", group: "large-small", ids: ["IN-RJ", "IN-MP", "IN-MH", "IN-GA", "IN-SK", "IN-TR"] },
] as const;
