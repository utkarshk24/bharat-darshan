/** Pre-filled "Suggest a correction" link to the project's GitHub issue form (.github/ISSUE_TEMPLATE/correction.yml). */
export const ISSUES_NEW = "https://github.com/utkarshk24/bharat-darshan/issues/new";

const LANG = { en: "English", hi: "हिंदी", mr: "मराठी" } as const;

export function correctionUrl(o: { page: string; item?: string; locale?: keyof typeof LANG }): string {
  const q = new URLSearchParams({ template: "correction.yml", page: o.page });
  if (o.item) {
    q.set("item", o.item.slice(0, 300));
    q.set("title", `Correction: ${o.item.slice(0, 80)}`);
  }
  if (o.locale) q.set("language", LANG[o.locale]);
  return `${ISSUES_NEW}?${q.toString()}`;
}
