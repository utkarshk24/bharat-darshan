import { buildTrip, tripRegions } from "@/lib/trip";

export const dynamic = "force-static";
export const dynamicParams = false;

export function generateStaticParams() {
  return tripRegions().map((r) => ({ file: `${r.code}.json` }));
}

/** One region's trip data, loaded by the planner when that region is picked. */
export async function GET(_req: Request, { params }: { params: Promise<{ file: string }> }) {
  const { file } = await params;
  const t = buildTrip(file.replace(/\.json$/, ""));
  if (!t) return new Response("Not found", { status: 404 });
  return new Response(JSON.stringify(t), { headers: { "content-type": "application/json; charset=utf-8" } });
}
