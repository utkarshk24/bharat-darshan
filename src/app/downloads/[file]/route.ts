import { DOWNLOADS } from "@/lib/exports";

export const dynamic = "force-static";
export const dynamicParams = false;

export function generateStaticParams() {
  return DOWNLOADS.map((d) => ({ file: d.file }));
}

const TYPES = { csv: "text/csv; charset=utf-8", json: "application/json; charset=utf-8" } as const;

export async function GET(_req: Request, { params }: { params: Promise<{ file: string }> }) {
  const { file } = await params;
  const d = DOWNLOADS.find((x) => x.file === file);
  if (!d) return new Response("Not found", { status: 404 });
  return new Response(d.build(), { headers: { "content-type": TYPES[d.kind] } });
}
