/** Region figures the India map can colour by (shared by server and client code). */
export const MAP_METRICS = ["population2011", "density2011", "literacyRate2011", "sexRatio2011", "forestCoverPct", "perCapitaNsdpCurrent"] as const;
export type MapMetric = (typeof MAP_METRICS)[number];
