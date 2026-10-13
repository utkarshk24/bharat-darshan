import "./globals.css";

export default function GlobalNotFound() {
  return (
    <html lang="en">
      <body className="grid min-h-screen place-items-center p-8 text-center">
        <div>
          <h1 className="text-2xl font-bold">Page not found</h1>
          <p className="mt-2">
            <a href="/en">Bharat Darshan</a> · <a href="/hi" lang="hi">भारत दर्शन (हिन्दी)</a> · <a href="/mr" lang="mr">भारत दर्शन (मराठी)</a>
          </p>
        </div>
      </body>
    </html>
  );
}
