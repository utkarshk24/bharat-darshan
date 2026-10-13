/**
 * Core web fonts, served from public/fonts (copied by `npm run fonts`) so their URLs are known
 * up front: the layout declares them with the base path and preloads the one the page's text needs.
 * Previously they came from CSS imports, so the browser found them only after the stylesheet.
 *
 * Inter's Latin-Extended range leaves out ₹ (U+20B9): it was the only Latin-Extended character on
 * most English pages and pulled in an 83 KB file; ₹ comes from Noto Sans Devanagari instead.
 * Ranges otherwise follow @fontsource-variable/inter and /noto-sans-devanagari.
 */
const FACES: { family: string; file: string; range: string }[] = [
  {
    family: "Inter Variable",
    file: "inter-latin-ext.woff2",
    range: "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20B8,U+20BA-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF",
  },
  {
    family: "Inter Variable",
    file: "inter-latin.woff2",
    range: "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
  },
  {
    family: "Noto Sans Devanagari Variable",
    file: "deva.woff2",
    range: "U+0900-097F,U+1CD0-1CF9,U+200C-200D,U+20A8,U+20B9,U+20F0,U+25CC,U+A830-A839,U+A8E0-A8FF,U+11B00-11B09",
  },
  {
    family: "Noto Sans Devanagari Variable",
    file: "deva-latin-ext.woff2",
    range: "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF",
  },
  {
    family: "Noto Sans Devanagari Variable",
    file: "deva-latin.woff2",
    range: "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
  },
];

export function coreFontCss(base: string): string {
  return FACES.map(
    (f) =>
      `@font-face{font-family:"${f.family}";font-style:normal;font-display:swap;font-weight:100 900;` +
      `src:url(${base}/fonts/${f.file}) format("woff2-variations");unicode-range:${f.range}}`,
  ).join("");
}

/** The font the page's main text is set in: Inter for English, Noto Sans Devanagari for Hindi and Marathi. */
export function primaryFont(base: string, locale: string): string {
  return `${base}/fonts/${locale === "en" ? "inter-latin.woff2" : "deva.woff2"}`;
}
