/**
 * Export the current map view as a PNG. CSS variables are resolved to their computed
 * values first, so the image matches what the reader sees (light or dark).
 */
export async function exportPng(
  svg: SVGSVGElement,
  opts: { title: string; attribution: string; filename: string; period: string | null },
) {
  const css = getComputedStyle(document.documentElement);
  const clone = svg.cloneNode(true) as SVGSVGElement;
  let src = new XMLSerializer().serializeToString(clone);
  src = src.replace(/var\((--[a-z0-9-]+)(?:,\s*([^)]+))?\)/gi, (_, name: string, fb?: string) => css.getPropertyValue(name).trim() || fb || "#888");
  if (!src.includes("xmlns=")) src = src.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"');
  const vb = svg.viewBox.baseVal;
  const scale = 2;
  const pad = 24, head = 56, foot = 40;
  const w = vb.width * scale, h = vb.height * scale;
  const canvas = document.createElement("canvas");
  canvas.width = w + pad * 2;
  canvas.height = h + head + foot;
  const ctx = canvas.getContext("2d")!;
  ctx.fillStyle = css.getPropertyValue("--surface").trim() || "#fff";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  const img = new Image();
  const url = URL.createObjectURL(new Blob([src], { type: "image/svg+xml;charset=utf-8" }));
  await new Promise<void>((res, rej) => {
    img.onload = () => res();
    img.onerror = rej;
    img.src = url;
  });
  ctx.drawImage(img, pad, head, w, h);
  URL.revokeObjectURL(url);
  const ink = css.getPropertyValue("--text").trim() || "#111";
  const muted = css.getPropertyValue("--text-muted").trim() || "#555";
  ctx.fillStyle = ink;
  ctx.font = "600 26px Inter Variable, Noto Sans Devanagari Variable, sans-serif";
  ctx.fillText(opts.title + (opts.period && !opts.title.includes(opts.period) ? ` (${opts.period})` : ""), pad, 38);
  ctx.fillStyle = muted;
  ctx.font = "16px Inter Variable, Noto Sans Devanagari Variable, sans-serif";
  ctx.fillText(opts.attribution, pad, canvas.height - 14, canvas.width - pad * 2);
  const a = document.createElement("a");
  a.download = opts.filename;
  a.href = canvas.toDataURL("image/png");
  a.click();
}
