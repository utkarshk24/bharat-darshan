import { buildExtraIndex } from "@/lib/searchExtra";

export const dynamic = "force-static";

export function GET() {
  return new Response(JSON.stringify(buildExtraIndex()), { headers: { "content-type": "application/json; charset=utf-8" } });
}
