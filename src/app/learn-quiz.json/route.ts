import { buildQuizBank } from "@/lib/quiz";

export const dynamic = "force-static";

export function GET() {
  return new Response(JSON.stringify(buildQuizBank()), { headers: { "content-type": "application/json; charset=utf-8" } });
}
