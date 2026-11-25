# Design rounds: writes /designs/<id>/ (home) and /designs/<id>/hackathon/ for each design, plus /designs/.
# python3 -I gen2.py <round-json>   run from the repository root.
import os, html, json, sys

HOST = "https://london.agentics-foundation.organisation.sovereignweb.site"
CARD = HOST + "/assets/share/card-1200x630.jpg"
READ = "read 24 November 2026"
SRC = "https://london.agentics.org/"
LUMA = "https://lu.ma/calendar/cal-G5qDYRTO06rtvbs"

FAMILY = """<details class="family-credit">
  <summary>Sovereign Website</summary>
  <ul>
    <li><a href="/start/">Start here</a></li>
    <li><a href="/agents/">Use with your AI</a></li>
    <li class="family-gap"><a href="/admin/">How this site was made</a></li>
    <li><a href="https://sovereignwebsite.ai/">Sovereign Website</a></li>
    <li><a href="https://sovereignwebsite.org/">Principles</a></li>
    <li><a href="https://sovereignwebsite.site/">Hosted</a></li>
    <li><a href="https://hub.sovereignweb.site/">Hub</a></li>
    <li><a href="https://agents.sovereignweb.site/">Agents</a></li>
    <li><a href="https://vault.sovereignwebsite.site/">Vault</a></li>
    <li><a href="https://agenticcells.ai/">AgentiCCells</a></li>
    <li><a href="https://riskmandate.ai/">RiskMandate</a></li>
    <li><a href="https://newsroom.sgit.ai/">Newsroom</a></li>
  </ul>
</details>"""


DESIGNS = [("d1","Editorial","A printed programme: serif and warm paper"),("d2","Poster","A dark event poster, big type, one lime"),
 ("d3","Terminal","An engineer's console in monospace"),("d4","Swiss grid","Numbered sections, one red, lots of white"),
 ("d5","Community","Soft colours and rounded cards"),("d6","Signal","Poster energy on a Swiss grid"),
 ("d7","Swarm","The Foundation's look, with a live agent network"),("d8","Workflow","The hackathon as an agent run"),
 ("d9","Mission control","A dashboard, with the agents behind this site")]
DEFAULT = "d8"


FEATURED = ["d8", "d7", "d9", "d6", "d4"]
PICK = None   # the chapter's recorded pick, e.g. ("d8", "Dinis Cruz, 1 December 2026, in ...") once made


def _card(i, n, d, current):
    here = i == current
    tag = ' <span class="pk-tag">Default</span>' if i == DEFAULT else ""
    return f'<li><a href="/designs/{i}/"{' aria-current="page"' if here else ''}><img src="/assets/designs/thumbs/{i}.jpg" width="160" height="100" alt="" loading="lazy" decoding="async"><strong>{i}, {n}{tag}</strong><span>{d}</span>{'<span class="pk-now">You are here</span>' if here else ''}</a></li>'


def picker(current):
    by = {i: (i, n, d) for i, n, d in DESIGNS}
    top = "\n      ".join(_card(*by[i], current) for i in FEATURED)
    old = "\n        ".join(_card(*x, current) for x in DESIGNS if x[0] not in FEATURED)
    pick = f"Recorded pick: {PICK[0]} ({PICK[1]})." if PICK else "Recorded pick: none yet. The default is d8, Workflow, the keeper's recommendation, until the chapter chooses."
    return f"""<details class="pick-design">
  <summary>Choose a design</summary>
  <div class="pk-panel">
    <p class="pk-intro">Five designs of this site for the chapter to pick from, each with the same content. {pick} <a href="/designs/">How to choose</a></p>
    <ul>
      {top}
    </ul>
    <details class="pk-old">
      <summary>Earlier rounds (4 more)</summary>
      <ul>
        {old}
      </ul>
    </details>
  </div>
</details>"""


def gap(what):
    return f'<span class="gap"><span class="gap-label">To be confirmed</span> {what}</span>'


def src(where=SRC, label="london.agentics.org"):
    return f'<span class="src">Source: <a href="{where}">{label}</a>, {READ}</span>'


def home_body(p):
    return f"""
<section class="hero" aria-labelledby="h1">
  <div class="hero-in">
    <p class="mark">Hackathon coming up: details to be confirmed</p>
    <h1 id="h1">Hands-on agentic AI in London</h1>
    <p class="lead">Agentics London is the London (UK) chapter of the global <a href="https://agentics.org">Agentics Foundation</a>. It runs free meetups and hands-on workshops on agentic AI.</p>
    <p class="actions"><a class="button" href="/take-part/">Take part</a> <a class="button ghost" href="{p}hackathon/">The hackathon</a></p>
    <p>{src()}</p>
  </div>
</section>

<section class="feature" aria-labelledby="hack">
  <div class="feature-head">
    <p class="mark">Coming up</p>
    <h2 id="hack">The hackathon</h2>
    <p>A hackathon with the chapter, showing examples of Sovereign Websites and AgentiCCells. Its details are not confirmed yet, and this site says so rather than guess.</p>
  </div>
  <dl class="facts">
    <div><dt>Date</dt><dd>{gap("in the next few weeks")}</dd></div>
    <div><dt>Venue</dt><dd>{gap("not yet published")}</dd></div>
    <div><dt>Sign up</dt><dd>{gap("Luma link to follow")}</dd></div>
  </dl>
  <p><a class="button" href="{p}hackathon/">About the hackathon</a></p>
</section>

<section class="chapter" aria-labelledby="ch">
  <h2 id="ch">The chapter</h2>
  <div class="cards">
    <article class="card">
      <p class="card-k">Every second Wednesday</p>
      <h3>Meetups</h3>
      <p>Online and in person, two to three hours. Public meetups are free. Sign up on the <a href="{LUMA}">Luma calendar</a>.</p>
    </article>
    <article class="card">
      <p class="card-k">Half a day to two days</p>
      <h3>Workshops</h3>
      <p>Guided, hands-on builds that end with a working prototype.</p>
    </article>
    <article class="card">
      <p class="card-k">About 300 members</p>
      <h3>Community</h3>
      <p>Engineers, product people, strategists and educators, led by six chapter co-founders. <a href="/about/">About the chapter</a></p>
    </article>
  </div>
  <p class="src">Source: <a href="{SRC}">london.agentics.org</a>, {READ}. The member count is the chapter's own, collected on 23 October 2026.</p>
</section>

<section class="join" aria-labelledby="jn">
  <h2 id="jn">Take part</h2>
  <p>Come to a meetup, join the Discord, or follow the chapter on LinkedIn and YouTube.</p>
  <p class="actions"><a class="button" href="/take-part/">How to take part</a> <a class="button ghost" href="{SRC}">london.agentics.org</a></p>
</section>
"""


def hack_body(p):
    rows = [("Date and time", "not yet published"), ("Venue", "not yet published"),
            ("Format", "in person, online or both; how long it runs"), ("Who it is for", "not yet published"),
            ("What to bring", "not yet published"), ("Rules and judging", "not yet published"),
            ("Sign up", "the event's Luma link")]
    dl = "\n    ".join(f"<div><dt>{a}</dt><dd>{gap(b)}</dd></div>" for a, b in rows)
    return f"""
<section class="hero hero-small" aria-labelledby="h1">
  <div class="hero-in">
    <p class="mark">Hackathon</p>
    <h1 id="h1">The London hackathon</h1>
    <p class="lead">A hackathon with the London chapter of the Agentics Foundation, showing examples of Sovereign Websites and AgentiCCells.</p>
  </div>
</section>

<div class="note" role="note">
  <p><strong>Draft.</strong> The chapter and Dinis Cruz agreed this hackathon on a call on 24 November 2026. Details marked "To be confirmed" have not been published yet.</p>
</div>

<section class="known" aria-labelledby="kn">
  <h2 id="kn">What we know</h2>
  <ul class="plain">
    <li>It is planned for the next few weeks, after a test run.</li>
    <li>It shows examples of <a href="https://sovereignwebsite.ai/">Sovereign Websites</a>: websites whose owners hold the files, the history and the address, and can move them anywhere.</li>
    <li>It shows examples of <a href="https://agenticcells.ai/">AgentiCCells</a>.</li>
  </ul>
</section>

<section class="feature" aria-labelledby="dt">
  <div class="feature-head"><h2 id="dt">The details</h2></div>
  <dl class="facts">
    {dl}
  </dl>
</section>

<section class="join" aria-labelledby="ut">
  <h2 id="ut">Until then</h2>
  <p>Chapter events are listed on its <a href="{LUMA}">Luma calendar</a>, as the chapter's own site shows them. When the hackathon is published there, this page will link to it.</p>
  <p class="actions"><a class="button" href="/take-part/">Take part in the chapter</a></p>
</section>
"""


def page(path, title, desc, body, css, nav_prefix, current, label=None, index=False, design=None):
    url = HOST + path
    t, d = html.escape(title), html.escape(desc)
    nav = [(nav_prefix + "hackathon/", "Hackathon"), ("/about/", "About"), ("/take-part/", "Take part")]
    navh = "\n    ".join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{n}</a>' for h, n in nav)
    banner = f'<aside class="design-banner" aria-label="Design">Design {html.escape(label)}. Live: d8. <a href="/designs/">All designs</a></aside>\n' if label else ""
    links = "".join(f'\n<link rel="stylesheet" href="{c}">' for c in css + ["/assets/picker.css"])
    out = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
{"" if index else chr(60)+'meta name="robots" content="noindex">'+chr(10)}<meta property="og:type" content="website">
<meta property="og:site_name" content="London Agentics Foundation">
<meta property="og:locale" content="en_GB">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{CARD}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="London Agentics Foundation">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{CARD}">
<link rel="canonical" href="{url}">{links}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{banner}{FAMILY}
<header class="top">
  <a class="name" href="{nav_prefix}">London Agentics Foundation</a>
  <nav class="own" aria-label="This site">
    {navh}
  </nav>
  {picker(design)}
</header>
<main id="main">
{body.strip()}
<footer>
<p class="built">An independent site about the London chapter of the Agentics Foundation, built from the chapter's own site, <a href="{SRC}">london.agentics.org</a>, with the chapter leaders' agreement. The chapter's name and branding are theirs. Built by london-agentics.a, an AI agent working for Dinis Cruz, with the <a href="https://sovereignwebsite.ai/">Sovereign Website</a> pipeline: <a href="/admin/">how this site was made</a>.</p>
<nav class="site-links" aria-label="About this site">
  <a href="/start/">Start here</a>
  <a href="/agents/">Use with your AI</a>
  <a href="/admin/">How this site was made</a>
  <a href="/policy/">How this site is governed</a>
</nav>
<p class="made">A sovereign website, made with the <a href="https://sovereignwebsite.org/">open pattern</a>. Source: <a href="https://github.com/SovereignWebsite/Site__Organisation__Agentics-Foundation__London">github.com/SovereignWebsite/Site__Organisation__Agentics-Foundation__London</a>.</p>
</footer>
</main>
</body>
</html>
"""
    f = "site" + path + "index.html"
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(out)


if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    for d in cfg["designs"]:
        pre = f"/designs/{d['id']}/"
        css = ["/assets/base.css", f"/assets/designs/{d['id']}.css"]
        lab = f"{d['id']}, {d['name']}"
        page(pre, f"Design {d['id']}: {d['name']}", f"Design preview {d['id']} ({d['name']}) of the London Agentics Foundation home page.", home_body(pre), css, pre, None, lab, design=d['id'])
        page(pre + "hackathon/", f"Design {d['id']}: {d['name']}, hackathon", f"Design preview {d['id']} ({d['name']}) of the London Agentics Foundation hackathon page.", hack_body(pre), css, pre, pre + "hackathon/", lab, design=d['id'])
    print("ok", len(cfg["designs"]))
