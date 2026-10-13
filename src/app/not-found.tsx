import "./globals.css";

const B = process.env.NEXT_PUBLIC_BASE_PATH ?? "";

export default function GlobalNotFound() {
  return (
    <html lang="en">
      <body className="grid min-h-screen place-items-center p-8 text-center">
        <div>
          <h1 className="text-2xl font-bold">Page not found</h1>
          <p className="mt-2">
            <a href={`${B}/en/`}>Bharat Darshan</a> · <a href={`${B}/hi/`} lang="hi">भारत दर्शन (हिन्दी)</a> · <a href={`${B}/mr/`} lang="mr">भारत दर्शन (मराठी)</a>
          </p>
        </div>
      </body>
    </html>
  );
}
