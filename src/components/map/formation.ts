import type { Localized } from "@/lib/schema";

/**
 * How today's States and UTs took shape, 1 November 1956 – 2026 (map theme "formation").
 *
 * Drawn on today's Survey of India boundaries: the map shows what each of today's States and UTs
 * was at a given date (a State, a Union territory, part of another unit, or not yet listed in the
 * Constitution). Earlier boundaries are not drawn. Every change cites the Act that made it; dates are
 * the appointed day notified under the Act (or the commencement written into it).
 */

export type Status = "S" | "U" | "part" | "unlisted";

export interface Period {
  /** ISO date (or year) from which this status applies. */
  from: string;
  status: Status;
  /** For "part": the unit it was part of, as named then. */
  of?: Localized;
  /** Name then, when it differs from today's. */
  name?: Localized;
}

export interface FormationEvent {
  /** ISO date, or a year when the day could not be confirmed from the Act. */
  date: string;
  act: string;
  url: string;
  confidence: "Official" | "Third-party verified";
  /** Regions (ISO codes) whose status or name changed. */
  codes: string[];
  what: Localized;
}

const L = (en: string, hi: string, mr: string): Localized => ({ en, hi, mr, _status: { hi: "draft", mr: "draft" } }) as Localized;

const BOMBAY = L("Bombay State", "बंबई राज्य", "मुंबई राज्य");
const PUNJAB = L("Punjab", "पंजाब", "पंजाब");
const ASSAM = L("Assam", "असम", "आसाम");
const AP = L("Andhra Pradesh", "आंध्र प्रदेश", "आंध्र प्रदेश");
const MP = L("Madhya Pradesh", "मध्य प्रदेश", "मध्य प्रदेश");
const BIHAR = L("Bihar", "बिहार", "बिहार");
const UP = L("Uttar Pradesh", "उत्तर प्रदेश", "उत्तर प्रदेश");
const JK = L("Jammu and Kashmir", "जम्मू और कश्मीर", "जम्मू आणि काश्मीर");

const START = "1956-11-01";

/** Status periods for each of today's States and UTs, oldest first. */
export const PERIODS: Record<string, Period[]> = {
  "IN-AN": [{ from: START, status: "U" }],
  "IN-AP": [{ from: START, status: "S" }],
  "IN-AR": [{ from: START, status: "part", of: ASSAM }, { from: "1972-01-21", status: "U" }, { from: "1987-02-20", status: "S" }],
  "IN-AS": [{ from: START, status: "S" }],
  "IN-BR": [{ from: START, status: "S" }],
  "IN-CH": [{ from: START, status: "part", of: PUNJAB }, { from: "1966-11-01", status: "U" }],
  "IN-CT": [{ from: START, status: "part", of: MP }, { from: "2000-11-01", status: "S" }],
  "IN-DH": [
    { from: START, status: "unlisted" },
    { from: "1961-08-11", status: "U", name: L("Dadra and Nagar Haveli (Daman and Diu: part of Goa, Daman and Diu)", "दादरा और नगर हवेली (दमन और दीव: गोवा, दमन और दीव का भाग)", "दादरा आणि नगर हवेली (दमण आणि दीव: गोवा, दमण आणि दीवचा भाग)") },
    { from: "1987-05-30", status: "U", name: L("Dadra and Nagar Haveli; Daman and Diu (two Union territories)", "दादरा और नगर हवेली; दमन और दीव (दो केंद्रशासित प्रदेश)", "दादरा आणि नगर हवेली; दमण आणि दीव (दोन केंद्रशासित प्रदेश)") },
    { from: "2020-01-26", status: "U" },
  ],
  "IN-DL": [{ from: START, status: "U" }],
  "IN-GA": [{ from: START, status: "unlisted" }, { from: "1961-12-20", status: "U", name: L("Goa, Daman and Diu", "गोवा, दमन और दीव", "गोवा, दमण आणि दीव") }, { from: "1987-05-30", status: "S" }],
  "IN-GJ": [{ from: START, status: "part", of: BOMBAY }, { from: "1960-05-01", status: "S" }],
  "IN-HP": [{ from: START, status: "U" }, { from: "1971-01-25", status: "S" }],
  "IN-HR": [{ from: START, status: "part", of: PUNJAB }, { from: "1966-11-01", status: "S" }],
  "IN-JH": [{ from: START, status: "part", of: BIHAR }, { from: "2000-11-15", status: "S" }],
  "IN-JK": [{ from: START, status: "S" }, { from: "2019-10-31", status: "U" }],
  "IN-KA": [{ from: START, status: "S", name: L("Mysore", "मैसूर", "म्हैसूर") }, { from: "1973-11-01", status: "S" }],
  "IN-KL": [{ from: START, status: "S", name: L("Kerala", "केरल", "केरळ") }, { from: "2026-08-25", status: "S" }],
  "IN-LA": [{ from: START, status: "part", of: JK }, { from: "2019-10-31", status: "U" }],
  "IN-LD": [{ from: START, status: "U", name: L("Laccadive, Minicoy and Amindivi Islands", "लक्कादीव, मिनिकॉय और अमीनदीवी द्वीप", "लक्कादीव, मिनिकॉय आणि अमिनदिवी बेटे") }, { from: "1973", status: "U" }],
  "IN-MH": [{ from: START, status: "part", of: BOMBAY }, { from: "1960-05-01", status: "S" }],
  "IN-ML": [{ from: START, status: "part", of: ASSAM }, { from: "1972-01-21", status: "S" }],
  "IN-MN": [{ from: START, status: "U" }, { from: "1972-01-21", status: "S" }],
  "IN-MP": [{ from: START, status: "S" }],
  "IN-MZ": [{ from: START, status: "part", of: ASSAM }, { from: "1972-01-21", status: "U" }, { from: "1987-02-20", status: "S" }],
  "IN-NL": [{ from: START, status: "part", of: ASSAM }, { from: "1963-12-01", status: "S" }],
  "IN-OR": [{ from: START, status: "S", name: L("Orissa", "उड़ीसा", "ओरिसा") }, { from: "2011-11-01", status: "S" }],
  "IN-PB": [{ from: START, status: "S" }],
  "IN-PY": [{ from: START, status: "unlisted" }, { from: "1962-08-16", status: "U", name: L("Pondicherry", "पांडिचेरी", "पाँडिचेरी") }, { from: "2006-10-01", status: "U" }],
  "IN-RJ": [{ from: START, status: "S" }],
  "IN-SK": [{ from: START, status: "unlisted" }, { from: "1975", status: "S" }],
  "IN-TG": [{ from: START, status: "part", of: AP }, { from: "2014-06-02", status: "S" }],
  "IN-TN": [{ from: START, status: "S", name: L("Madras", "मद्रास", "मद्रास") }, { from: "1969-01-14", status: "S" }],
  "IN-TR": [{ from: START, status: "U" }, { from: "1972-01-21", status: "S" }],
  "IN-UK": [{ from: START, status: "part", of: UP }, { from: "2000-11-09", status: "S", name: L("Uttaranchal", "उत्तरांचल", "उत्तरांचल") }, { from: "2007-01-01", status: "S" }],
  "IN-UP": [{ from: START, status: "S" }],
  "IN-WB": [{ from: START, status: "S" }],
};

const IC = (h: number) => `https://www.indiacode.nic.in/handle/123456789/${h}`;
/** The Constitution of India as on 1 May 2024 (Legislative Department): First Schedule entries and footnotes. */
const COI = "https://cdnbbsr.s3waas.gov.in/s380537a945c7aaa788ccfcdf1b99b5d8f/uploads/2024/07/20240716890312078.pdf";

export const EVENTS: FormationEvent[] = [
  { date: START, act: "States Reorganisation Act, 1956 (37 of 1956)", url: IC(1680), confidence: "Official", codes: ["IN-AP", "IN-KL", "IN-KA", "IN-MP", "IN-RJ", "IN-PB", "IN-LD", "IN-DL", "IN-HP", "IN-MN", "IN-TR", "IN-AN"],
    what: L("States reorganised on linguistic lines: Andhra Pradesh, Kerala, Mysore, Bombay, Madhya Pradesh, Rajasthan and Punjab formed or reshaped; Delhi, Himachal Pradesh, Manipur, Tripura, the Andaman and Nicobar Islands and the Laccadive, Minicoy and Amindivi Islands become Union territories.",
      "भाषाई आधार पर राज्यों का पुनर्गठन: आंध्र प्रदेश, केरल, मैसूर, बंबई, मध्य प्रदेश, राजस्थान और पंजाब बने या बदले; दिल्ली, हिमाचल प्रदेश, मणिपुर, त्रिपुरा, अंडमान और निकोबार द्वीप तथा लक्कादीव, मिनिकॉय और अमीनदीवी द्वीप केंद्रशासित प्रदेश बने।",
      "भाषिक आधारावर राज्यांची पुनर्रचना: आंध्र प्रदेश, केरळ, म्हैसूर, मुंबई, मध्य प्रदेश, राजस्थान आणि पंजाब यांची निर्मिती किंवा फेररचना; दिल्ली, हिमाचल प्रदेश, मणिपूर, त्रिपुरा, अंदमान आणि निकोबार बेटे तसेच लक्कादीव, मिनिकॉय आणि अमिनदिवी बेटे केंद्रशासित प्रदेश झाले.") },
  { date: "1960-05-01", act: "Bombay Reorganisation Act, 1960 (11 of 1960)", url: IC(1535), confidence: "Official", codes: ["IN-GJ", "IN-MH"],
    what: L("Bombay State divided into Gujarat and Maharashtra.", "बंबई राज्य को गुजरात और महाराष्ट्र में बाँटा गया।", "मुंबई राज्याचे गुजरात आणि महाराष्ट्र असे विभाजन.") },
  { date: "1961-08-11", act: "Constitution (Tenth Amendment) Act, 1961", url: COI, confidence: "Official", codes: ["IN-DH"],
    what: L("Dadra and Nagar Haveli becomes a Union territory.", "दादरा और नगर हवेली केंद्रशासित प्रदेश बना।", "दादरा आणि नगर हवेली केंद्रशासित प्रदेश झाला.") },
  { date: "1961-12-20", act: "Constitution (Twelfth Amendment) Act, 1962", url: COI, confidence: "Official", codes: ["IN-GA", "IN-DH"],
    what: L("Goa, Daman and Diu becomes a Union territory.", "गोवा, दमन और दीव केंद्रशासित प्रदेश बना।", "गोवा, दमण आणि दीव केंद्रशासित प्रदेश झाला.") },
  { date: "1962-08-16", act: "Constitution (Fourteenth Amendment) Act, 1962", url: COI, confidence: "Official", codes: ["IN-PY"],
    what: L("Pondicherry (Puducherry, Karaikal, Mahe and Yanam) becomes a Union territory.", "पांडिचेरी (पुदुच्चेरी, कराईकल, माहे और यानम) केंद्रशासित प्रदेश बना।", "पाँडिचेरी (पुदुच्चेरी, कराईकल, माहे आणि यानम) केंद्रशासित प्रदेश झाला.") },
  { date: "1963-12-01", act: "State of Nagaland Act, 1962 (27 of 1962)", url: IC(1384), confidence: "Official", codes: ["IN-NL"],
    what: L("Nagaland becomes a State, separated from Assam.", "नागालैंड असम से अलग होकर राज्य बना।", "नागालँड आसाममधून वेगळा होऊन राज्य झाले.") },
  { date: "1966-11-01", act: "Punjab Reorganisation Act, 1966 (31 of 1966)", url: IC(1645), confidence: "Official", codes: ["IN-HR", "IN-CH", "IN-PB", "IN-HP"],
    what: L("Haryana formed from Punjab; Chandigarh becomes a Union territory; Punjab's hill areas join Himachal Pradesh.", "पंजाब से हरियाणा बना; चंडीगढ़ केंद्रशासित प्रदेश बना; पंजाब के पहाड़ी क्षेत्र हिमाचल प्रदेश में मिले।", "पंजाबमधून हरियाणाची निर्मिती; चंडीगड केंद्रशासित प्रदेश झाले; पंजाबचे डोंगरी भाग हिमाचल प्रदेशात सामील.") },
  { date: "1969-01-14", act: "Madras State (Alteration of Name) Act, 1968 (53 of 1968)", url: COI, confidence: "Official", codes: ["IN-TN"],
    what: L("Madras State renamed Tamil Nadu.", "मद्रास राज्य का नाम तमिलनाडु हुआ।", "मद्रास राज्याचे नाव तमिळनाडू झाले.") },
  { date: "1971-01-25", act: "State of Himachal Pradesh Act, 1970 (53 of 1970)", url: IC(1464), confidence: "Official", codes: ["IN-HP"],
    what: L("Himachal Pradesh becomes a State.", "हिमाचल प्रदेश राज्य बना।", "हिमाचल प्रदेश राज्य झाले.") },
  { date: "1972-01-21", act: "North-Eastern Areas (Reorganisation) Act, 1971 (81 of 1971)", url: IC(1534), confidence: "Official", codes: ["IN-MN", "IN-TR", "IN-ML", "IN-MZ", "IN-AR"],
    what: L("Manipur, Tripura and Meghalaya become States; Mizoram and Arunachal Pradesh become Union territories.", "मणिपुर, त्रिपुरा और मेघालय राज्य बने; मिज़ोरम और अरुणाचल प्रदेश केंद्रशासित प्रदेश बने।", "मणिपूर, त्रिपुरा आणि मेघालय राज्ये झाली; मिझोरम आणि अरुणाचल प्रदेश केंद्रशासित प्रदेश झाले.") },
  { date: "1973", act: "Laccadive, Minicoy and Amindivi Islands (Alteration of Name) Act, 1973", url: COI, confidence: "Official", codes: ["IN-LD"],
    what: L("The Laccadive, Minicoy and Amindivi Islands renamed Lakshadweep.", "लक्कादीव, मिनिकॉय और अमीनदीवी द्वीप का नाम लक्षद्वीप हुआ।", "लक्कादीव, मिनिकॉय आणि अमिनदिवी बेटांचे नाव लक्षद्वीप झाले.") },
  { date: "1973-11-01", act: "Mysore State (Alteration of Name) Act, 1973 (31 of 1973)", url: COI, confidence: "Official", codes: ["IN-KA"],
    what: L("Mysore State renamed Karnataka.", "मैसूर राज्य का नाम कर्नाटक हुआ।", "म्हैसूर राज्याचे नाव कर्नाटक झाले.") },
  { date: "1975", act: "Constitution (Thirty-sixth Amendment) Act, 1975", url: COI, confidence: "Official", codes: ["IN-SK"],
    what: L("Sikkim becomes a State of India.", "सिक्किम भारत का राज्य बना।", "सिक्कीम भारताचे राज्य झाले.") },
  { date: "1987-02-20", act: "State of Mizoram Act, 1986 (34 of 1986); State of Arunachal Pradesh Act, 1986 (69 of 1986)", url: IC(1869), confidence: "Official", codes: ["IN-MZ", "IN-AR"],
    what: L("Mizoram and Arunachal Pradesh become States.", "मिज़ोरम और अरुणाचल प्रदेश राज्य बने।", "मिझोरम आणि अरुणाचल प्रदेश राज्ये झाली.") },
  { date: "1987-05-30", act: "Goa, Daman and Diu Reorganisation Act, 1987 (18 of 1987)", url: IC(1886), confidence: "Official", codes: ["IN-GA", "IN-DH"],
    what: L("Goa becomes a State; Daman and Diu becomes a separate Union territory.", "गोवा राज्य बना; दमन और दीव अलग केंद्रशासित प्रदेश बना।", "गोवा राज्य झाले; दमण आणि दीव स्वतंत्र केंद्रशासित प्रदेश झाला.") },
  { date: "2000-11-01", act: "Madhya Pradesh Reorganisation Act, 2000 (28 of 2000)", url: IC(1992), confidence: "Official", codes: ["IN-CT", "IN-MP"],
    what: L("Chhattisgarh formed from Madhya Pradesh.", "मध्य प्रदेश से छत्तीसगढ़ बना।", "मध्य प्रदेशातून छत्तीसगडची निर्मिती.") },
  { date: "2000-11-09", act: "Uttar Pradesh Reorganisation Act, 2000 (29 of 2000)", url: IC(2000), confidence: "Official", codes: ["IN-UK", "IN-UP"],
    what: L("Uttaranchal formed from Uttar Pradesh.", "उत्तर प्रदेश से उत्तरांचल बना।", "उत्तर प्रदेशातून उत्तरांचलची निर्मिती.") },
  { date: "2000-11-15", act: "Bihar Reorganisation Act, 2000 (30 of 2000)", url: IC(2001), confidence: "Official", codes: ["IN-JH", "IN-BR"],
    what: L("Jharkhand formed from Bihar.", "बिहार से झारखंड बना।", "बिहारमधून झारखंडची निर्मिती.") },
  { date: "2006-10-01", act: "Pondicherry (Alteration of Name) Act, 2006 (44 of 2006)", url: IC(2075), confidence: "Official", codes: ["IN-PY"],
    what: L("Pondicherry renamed Puducherry.", "पांडिचेरी का नाम पुदुच्चेरी हुआ।", "पाँडिचेरीचे नाव पुदुच्चेरी झाले.") },
  { date: "2007-01-01", act: "Uttaranchal (Alteration of Name) Act, 2006 (52 of 2006)", url: IC(2047), confidence: "Official", codes: ["IN-UK"],
    what: L("Uttaranchal renamed Uttarakhand.", "उत्तरांचल का नाम उत्तराखंड हुआ।", "उत्तरांचलचे नाव उत्तराखंड झाले.") },
  { date: "2011-11-01", act: "Orissa (Alteration of Name) Act, 2011 (15 of 2011)", url: IC(2108), confidence: "Official", codes: ["IN-OR"],
    what: L("Orissa renamed Odisha.", "उड़ीसा का नाम ओडिशा हुआ।", "ओरिसाचे नाव ओडिशा झाले.") },
  { date: "2014-06-02", act: "Andhra Pradesh Reorganisation Act, 2014 (6 of 2014)", url: IC(2123), confidence: "Official", codes: ["IN-TG", "IN-AP"],
    what: L("Telangana formed from Andhra Pradesh.", "आंध्र प्रदेश से तेलंगाना बना।", "आंध्र प्रदेशातून तेलंगणाची निर्मिती.") },
  { date: "2019-10-31", act: "Jammu and Kashmir Reorganisation Act, 2019 (34 of 2019)", url: IC(12030), confidence: "Official", codes: ["IN-JK", "IN-LA"],
    what: L("The State of Jammu and Kashmir reorganised into the Union territories of Jammu and Kashmir and of Ladakh.", "जम्मू और कश्मीर राज्य का जम्मू और कश्मीर तथा लद्दाख केंद्रशासित प्रदेशों में पुनर्गठन।", "जम्मू आणि काश्मीर राज्याची जम्मू आणि काश्मीर व लडाख या केंद्रशासित प्रदेशांमध्ये पुनर्रचना.") },
  { date: "2020-01-26", act: "Dadra and Nagar Haveli and Daman and Diu (Merger of Union territories) Act, 2019 (44 of 2019)", url: IC(13079), confidence: "Official", codes: ["IN-DH"],
    what: L("Dadra and Nagar Haveli and Daman and Diu merged into one Union territory.", "दादरा और नगर हवेली तथा दमन और दीव एक केंद्रशासित प्रदेश में विलय।", "दादरा आणि नगर हवेली व दमण आणि दीव यांचे एका केंद्रशासित प्रदेशात विलीनीकरण.") },
  { date: "2026-08-25", act: "Kerala (Alteration of Name) Act, 2026", url: "https://prsindia.org", confidence: "Third-party verified", codes: ["IN-KL"],
    what: L("Kerala renamed Keralam.", "केरल का नाम केरलम हुआ।", "केरळचे नाव केरळम झाले.") },
];

export const FIRST_YEAR = 1956;
export const LAST_YEAR = 2026;

/** Year of a date or year string. */
export const yearOf = (d: string) => Number(d.slice(0, 4));

/**
 * Status of a region at the end of a year (the map shows the position on 31 December, or today for the current year).
 * A year-only date counts from the start of that year.
 */
export function periodAt(code: string, year: number): Period | null {
  const ps = PERIODS[code];
  if (!ps) return null;
  let cur: Period | null = null;
  for (const p of ps) if (yearOf(p.from) <= year) cur = p;
  return cur;
}

export const eventsIn = (year: number) => EVENTS.filter((e) => yearOf(e.date) === year);
export const eventYears = [...new Set(EVENTS.map((e) => yearOf(e.date)))];
