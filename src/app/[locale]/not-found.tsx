import { useTranslations } from "next-intl";
import { Link } from "@/i18n/navigation";

export default function NotFound() {
  const t = useTranslations("common");
  return (
    <section className="mx-auto max-w-2xl px-4 py-24 text-center">
      <h1 className="text-3xl font-bold">{t("notFoundTitle")}</h1>
      <p className="mt-3 text-muted">{t("notFoundBody")}</p>
      <Link href="/" className="mt-6 inline-block">{t("backHome")}</Link>
    </section>
  );
}
