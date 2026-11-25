# Content-hash every local stylesheet link: href="/assets/x.css" -> href="/assets/x.css?v=<sha256[:10]>", so a changed
# stylesheet is never served from an old cache. Run from the repository root, last, after the generators.
import hashlib, os, re
n = 0
for root, _, files in os.walk("site"):
    for f in files:
        if not f.endswith(".html"): continue
        p = os.path.join(root, f); s = open(p, encoding="utf-8").read()
        def rep(m):
            global n
            path = m.group(1); fs = "site" + path
            if not os.path.isfile(fs): return m.group(0)
            n += 1; return f'<link rel="stylesheet" href="{path}?v={hashlib.sha256(open(fs, "rb").read()).hexdigest()[:10]}">'
        t = re.sub(r'<link rel="stylesheet" href="(/assets/(?!sws-version\.css)[^"?]+\.css)(?:\?v=[0-9a-f]+)?">', rep, s)
        if t != s: open(p, "w", encoding="utf-8").write(t)
print("stamped", n, "links")
