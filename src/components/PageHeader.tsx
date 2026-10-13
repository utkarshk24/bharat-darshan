import { DataAsOn } from "./DataAsOn";

export function PageHeader({ title, intro, asOn, children }: { title: string; intro?: string; asOn?: string; children?: React.ReactNode }) {
  return (
    <div className="mb-8 flex flex-col gap-3">
      <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">{title}</h1>
      {intro && <p className="max-w-3xl text-lg text-muted">{intro}</p>}
      <div className="flex flex-wrap items-center gap-2">
        {asOn && <DataAsOn date={asOn} />}
        {children}
      </div>
    </div>
  );
}
