import { createServer } from 'node:http'; import { readFileSync, existsSync, statSync } from 'node:fs'; import { join, extname } from 'node:path';
import { chromium } from 'playwright';
const [dir, out] = process.argv.slice(2); const T = { '.html': 'text/html', '.css': 'text/css', '.woff2': 'font/woff2', '.jpg': 'image/jpeg' };
const s = createServer((q, r) => { let f = join(dir, decodeURI(q.url.split('?')[0])); if (existsSync(f) && statSync(f).isDirectory()) f = join(f, 'index.html'); if (!existsSync(f)) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'content-type': T[extname(f)] || 'application/octet-stream' }); r.end(readFileSync(f)); });
await new Promise((ok) => s.listen(0, ok)); const base = `http://127.0.0.1:${s.address().port}`; const b = await chromium.launch();
for (let n = 1; n <= 9; n++) { const c = await b.newContext({ viewport: { width: 1280, height: 800 }, deviceScaleFactor: 0.5, colorScheme: 'light', reducedMotion: 'reduce' }); const p = await c.newPage();
  await p.goto(`${base}/designs/d${n}/`); await p.addStyleTag({ content: '.design-banner,.pick-design,.family-credit{display:none!important}' }); await p.waitForTimeout(150);
  await p.screenshot({ path: `${out}/d${n}.jpg`, type: 'jpeg', quality: 72 }); await c.close(); }
await b.close(); s.close();
