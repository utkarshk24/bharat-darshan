/**
 * Cross-script search helpers (Section 11): "Pune", "पुणे" and "puney" should all match.
 * Devanagari is romanised with a light scheme, then both scripts are reduced to a
 * phonetic key that ignores common spelling variation (ee/i, w/v, aspirates, final schwa).
 * This is for matching only — never for display.
 */

const VOWELS: Record<string, string> = {
  अ: "a", आ: "aa", इ: "i", ई: "ii", उ: "u", ऊ: "uu", ऋ: "ri", ए: "e", ऐ: "ai", ओ: "o", औ: "au", ऑ: "o", ऍ: "e",
};
const MATRAS: Record<string, string> = {
  "ा": "aa", "ि": "i", "ी": "ii", "ु": "u", "ू": "uu", "ृ": "ri", "े": "e", "ै": "ai", "ो": "o", "ौ": "au", "ॉ": "o", "ॅ": "e",
};
const CONSONANTS: Record<string, string> = {
  क: "k", ख: "kh", ग: "g", घ: "gh", ङ: "n", च: "ch", छ: "chh", ज: "j", झ: "jh", ञ: "n",
  ट: "t", ठ: "th", ड: "d", ढ: "dh", ण: "n", त: "t", थ: "th", द: "d", ध: "dh", न: "n",
  प: "p", फ: "ph", ब: "b", भ: "bh", म: "m", य: "y", र: "r", ल: "l", ळ: "l", व: "v",
  श: "sh", ष: "sh", स: "s", ह: "h",
};
const NUKTA_FORMS: Record<string, string> = { क: "q", ख: "kh", ग: "g", ज: "z", ड: "r", ढ: "rh", फ: "f" };
const VIRAMA = "्";
const NUKTA = "़";

export const hasDevanagari = (s: string) => /[ऀ-ॿ]/.test(s);

/** Romanise Devanagari text (word-final inherent vowel dropped, as in Hindi/Marathi speech). */
export function romanizeDevanagari(input: string): string {
  const chars = [...input.normalize("NFC")];
  let out = "";
  for (let i = 0; i < chars.length; i++) {
    const c = chars[i];
    if (c in CONSONANTS) {
      let base = CONSONANTS[c];
      let j = i + 1;
      if (chars[j] === NUKTA) {
        base = NUKTA_FORMS[c] ?? base;
        j++;
      }
      const next = chars[j];
      if (next === VIRAMA) {
        out += base;
        i = j;
      } else if (next && next in MATRAS) {
        out += base + MATRAS[next];
        i = j;
      } else {
        // Inherent 'a', dropped at word end.
        const atWordEnd = !next || /[\s\-,.()]/.test(next);
        out += base + (atWordEnd ? "" : "a");
        i = j - 1;
      }
    } else if (c in VOWELS) out += VOWELS[c];
    else if (c === "ं" || c === "ँ") out += "n";
    else if (c === "ः") out += "h";
    else if (c === NUKTA) continue;
    else out += c;
  }
  return out;
}

/** Reduce a Latin (or romanised) string to a spelling-tolerant phonetic key. */
export function phoneticKey(input: string): string {
  let s = (hasDevanagari(input) ? romanizeDevanagari(input) : input)
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase();
  s = s.replace(/&/g, " and ");
  return s
    .split(/[^a-z]+/)
    .filter(Boolean)
    .map((w) => {
      w = w.replace(/chh/g, "c").replace(/ch/g, "c").replace(/sh/g, "s");
      w = w.replace(/([kgtdbjpr])h/g, "$1");
      w = w.replace(/ph/g, "p").replace(/f/g, "p").replace(/w/g, "v").replace(/z/g, "j").replace(/q/g, "k").replace(/x/g, "ks");
      w = w.replace(/ey$/, "e").replace(/ay$/, "e");
      w = w.replace(/ee/g, "i").replace(/oo/g, "u");
      w = w.replace(/n(?=[bpm])/g, "m");
      w = w.replace(/(.)\1+/g, "$1");
      if (w.length > 3) w = w.replace(/a$/, "");
      return w;
    })
    .join(" ");
}
