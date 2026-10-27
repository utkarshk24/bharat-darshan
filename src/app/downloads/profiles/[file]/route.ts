import { profileCodes, profileJson } from "@/lib/exports";

export const dynamic = "force-static";
export const dynamicParams = false;

export function generateStaticParams() {
  return profileCodes().map((c) => ({ file: `${c}.json` }));
}

export async function GET(_req: Request, { params }: { params: Promise<{ file: string }> }) {
  const { file } = await params;
  const body = profileJson(file.replace(/\.json$/, ""));
  if (!body) return new Response("Not found", { status: 404 });
  return new Response(body, { headers: { "content-type": "application/json; charset=utf-8" } });
}
