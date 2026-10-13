import type { ModuleKey } from "./nav";

/** Themes (Section 5.1, item 7): cross-cutting views that gather profile modules and comparison indicators. */
export const THEMES = [
  { key: "geography", modules: ["geography", "climate", "water"], compareGroups: [], link: "/map" },
  { key: "people", modules: ["people", "cities", "diaspora"], compareGroups: ["people"], link: "/compare" },
  { key: "economy", modules: ["economy", "digital", "energy"], compareGroups: ["economy"], link: "/compare" },
  { key: "governance", modules: ["government", "safety", "civic"], compareGroups: [], link: "/india" },
  { key: "infrastructure", modules: ["transport", "energy", "projects"], compareGroups: [], link: "/projects" },
  { key: "tourism", modules: ["tourism", "gi", "vibe"], compareGroups: [], link: "/gi" },
  { key: "culture", modules: ["culture", "history", "personalities", "sports"], compareGroups: [], link: null },
  { key: "nature", modules: ["nature", "water", "climate"], compareGroups: ["environment"], link: "/compare" },
  { key: "education-health", modules: ["education", "health"], compareGroups: ["wellbeing"], link: "/compare" },
] as const satisfies readonly { key: string; modules: readonly ModuleKey[]; compareGroups: readonly string[]; link: string | null }[];

export type ThemeKey = (typeof THEMES)[number]["key"];
