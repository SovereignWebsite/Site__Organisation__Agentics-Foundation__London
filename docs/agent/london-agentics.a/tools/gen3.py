# Round 4: agent-first designs with their own markup. Uses gen2.page(). Run from the repository root:
# python3 -I gen3.py <scratchpad dir>
import sys, random, math
sys.path.insert(0, sys.argv[1]); import gen2
from gen2 import SRC, LUMA, READ, gap

def network(seed=7, w=1200, h=520, cols=11, rows=5, cls="net"):
    """A decorative agent network: jittered grid nodes, neighbour edges, a few live edges and lead nodes."""
    r = random.Random(seed); pts = []
    for j in range(rows):
        for i in range(cols):
            x = 40 + i * (w - 80) / (cols - 1) + r.uniform(-28, 28); y = 40 + j * (h - 80) / (rows - 1) + r.uniform(-24, 24)
            pts.append((round(x), round(y)))
    edges = set()
    for a, (x1, y1) in enumerate(pts):
        near = sorted(range(len(pts)), key=lambda b: (pts[b][0] - x1) ** 2 + (pts[b][1] - y1) ** 2)[1:4]
        for b in near:
            if r.random() < .7: edges.add(tuple(sorted((a, b))))
    edges = sorted(edges); live = set(r.sample(range(len(edges)), 14)); lead = set(r.sample(range(len(pts)), 7))
    out = [f'<svg class="{cls}" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">']
    for k, (a, b) in enumerate(edges):
        (x1, y1), (x2, y2) = pts[a], pts[b]
        c = f' class="live" style="animation-delay:-{k % 7 * .6:.1f}s"' if k in live else ""
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"{c}/>')
    for k, (x, y) in enumerate(pts):
        if k in lead: out.append(f'<circle cx="{x}" cy="{y}" r="7" class="lead" style="animation-delay:-{k % 5 * .8:.1f}s"/>')
        else: out.append(f'<circle cx="{x}" cy="{y}" r="3.5"/>')
    out.append("</svg>")
    return "".join(out)

def chip(state, text):
    return f'<span class="st st-{state}"><span class="st-dot" aria-hidden="true"></span><span class="st-k">{ {"done":"Done","next":"Planned","wait":"To be confirmed"}[state] }</span> {text}</span>'

# ---------- d7 Swarm (Foundation-aligned) ----------
def d7_home(p):
    return f"""
<section class="hero swarm" aria-labelledby="h1">
  {network()}
  <div class="hero-in">
    <p class="mark"><span class="br">[</span> hackathon coming up <span class="br">]</span></p>
    <h1 id="h1">Hands-on <em>agentic AI</em> in London</h1>
    <p class="lead">Agentics London is the London (UK) chapter of the global <a href="https://agentics.org">Agentics Foundation</a>: free meetups and hands-on workshops on autonomous agents that plan, act and collaborate.</p>
    <p class="actions"><a class="button" href="/take-part/">Take part</a> <a class="button ghost" href="{p}hackathon/">The hackathon</a></p>
    <p class="src">Source: <a href="{SRC}">london.agentics.org</a>, {READ}</p>
  </div>
</section>

<section class="feature win" aria-labelledby="hack">
  <div class="win-bar" aria-hidden="true"><span></span><span></span><span></span><code>hackathon.london</code></div>
  <div class="win-body">
    <p class="mark">Coming up</p>
    <h2 id="hack">The <em>hackathon</em></h2>
    <p>A hackathon with the chapter, showing examples of Sovereign Websites and AgentiCCells. Its details are not confirmed yet, and this site says so rather than guess.</p>
    <dl class="facts">
      <div><dt>Date</dt><dd>{gap("in the next few weeks")}</dd></div>
      <div><dt>Venue</dt><dd>{gap("not yet published")}</dd></div>
      <div><dt>Sign up</dt><dd>{gap("Luma link to follow")}</dd></div>
    </dl>
    <p><a class="button" href="{p}hackathon/">About the hackathon</a></p>
  </div>
</section>

<section class="chapter" aria-labelledby="ch">
  <h2 id="ch">The <em>chapter</em></h2>
  <div class="cards">
    <article class="card"><p class="card-k">Every second Wednesday</p><h3>Meetups</h3><p>Online and in person, two to three hours. Public meetups are free. Sign up on the <a href="{LUMA}">Luma calendar</a>.</p></article>
    <article class="card"><p class="card-k">Half a day to two days</p><h3>Workshops</h3><p>Guided, hands-on builds that end with a working prototype.</p></article>
    <article class="card"><p class="card-k">About 300 members</p><h3>Community</h3><p>Engineers, product people, strategists and educators, led by six chapter co-founders. <a href="/about/">About the chapter</a></p></article>
  </div>
  <p class="src">Source: <a href="{SRC}">london.agentics.org</a>, {READ}. The member count is the chapter's own, collected on 23 October 2026.</p>
</section>

<section class="join" aria-labelledby="jn">
  <h2 id="jn">Take <em>part</em></h2>
  <p>Come to a meetup, join the Discord, or follow the chapter on LinkedIn and YouTube.</p>
  <p class="actions"><a class="button" href="/take-part/">How to take part</a> <a class="button ghost" href="{SRC}">london.agentics.org</a></p>
</section>
"""

def details_rows():
    return [("Date and time", "not yet published"), ("Venue", "not yet published"), ("Format", "in person, online or both; how long it runs"),
            ("Who it is for", "not yet published"), ("What to bring", "not yet published"), ("Rules and judging", "not yet published"), ("Sign up", "the event's Luma link")]

def d7_hack(p):
    dl = "\n      ".join(f"<div><dt>{a}</dt><dd>{gap(b)}</dd></div>" for a, b in details_rows())
    return f"""
<section class="hero swarm hero-small" aria-labelledby="h1">
  {network(seed=11, h=380, rows=4)}
  <div class="hero-in">
    <p class="mark"><span class="br">[</span> Hackathon <span class="br">]</span></p>
    <h1 id="h1">The London <em>hackathon</em></h1>
    <p class="lead">A hackathon with the London chapter of the Agentics Foundation, showing examples of Sovereign Websites and AgentiCCells.</p>
  </div>
</section>
<div class="note" role="note"><p><strong>Draft.</strong> The chapter and Dinis Cruz agreed this hackathon on a call on 24 November 2026. Details marked "To be confirmed" have not been published yet.</p></div>
<section class="known" aria-labelledby="kn">
  <h2 id="kn">What we <em>know</em></h2>
  <ul class="plain">
    <li>It is planned for the next few weeks, after a test run.</li>
    <li>It shows examples of <a href="https://sovereignwebsite.ai/">Sovereign Websites</a>: websites whose owners hold the files, the history and the address, and can move them anywhere.</li>
    <li>It shows examples of <a href="https://agenticcells.ai/">AgentiCCells</a>.</li>
  </ul>
</section>
<section class="feature win" aria-labelledby="dt">
  <div class="win-bar" aria-hidden="true"><span></span><span></span><span></span><code>details.pending</code></div>
  <div class="win-body"><h2 id="dt">The <em>details</em></h2>
    <dl class="facts">
      {dl}
    </dl>
  </div>
</section>
<section class="join" aria-labelledby="ut">
  <h2 id="ut">Until <em>then</em></h2>
  <p>Chapter events are listed on its <a href="{LUMA}">Luma calendar</a>, as the chapter's own site shows them. When the hackathon is published there, this page will link to it.</p>
  <p class="actions"><a class="button" href="/take-part/">Take part in the chapter</a></p>
</section>
"""

AGENTS = """
  <div class="panel panel-agents">
    <h2 id="ag">Built by agents</h2>
    <p>This site is itself a small example of the hackathon's subject: agents built it, and every step is public.</p>
    <ul class="roster">
      <li><span class="who">Dinis Cruz</span><span class="what">the owner: decides</span></li>
      <li><span class="who">sites.a</span><span class="what">agent: started the keeper, reviews before the chapter sees it</span></li>
      <li><span class="who">london-agentics.a</span><span class="what">agent: builds the site, signs every change with <a href="/keys/london-agentics.a.json">its own published key</a></span></li>
      <li><span class="who">Pages pipeline</span><span class="what">checks signatures, links, accessibility and leaks before it publishes</span></li>
    </ul>
    <p><a href="/admin/">How this site was made</a></p>
  </div>"""

# ---------- d8 Workflow (the page as an agent run) ----------
def trace(lines):
    li = "\n      ".join(f'<li class="t-{s}"><span class="t-ic" aria-hidden="true"></span><span class="t-sr">{ {"done":"Done:","next":"Planned:","wait":"To be confirmed:"}[s] }</span> {t}</li>' for s, t in lines)
    return f"""<div class="term">
    <div class="term-bar" aria-hidden="true"><span></span><span></span><span></span><code>agent run: london-hackathon</code></div>
    <p class="term-cmd" aria-hidden="true">$ run london-hackathon --show-gaps</p>
    <ol class="trace" aria-label="The hackathon, as a workflow">
      {li}
    </ol>
    <p class="term-cur" aria-hidden="true">waiting for the organisers</p>
  </div>"""

HACK_TRACE = [("done", "Agreed with the London chapter, 24 November 2026"),
              ("done", "This site built, signed and checked by agents"),
              ("next", "A test run first"),
              ("wait", "Date and time"), ("wait", "Venue"), ("wait", "Sign-up link on Luma")]

def d8_home(p):
    return f"""
<section class="hero flow" aria-labelledby="h1">
  <div class="hero-in">
    <p class="mark">Hackathon coming up: details to be confirmed</p>
    <h1 id="h1">Hands-on agentic AI in London</h1>
    <p class="lead">Agentics London is the London (UK) chapter of the global <a href="https://agentics.org">Agentics Foundation</a>. It runs free meetups and hands-on workshops on agentic AI.</p>
    <p class="actions"><a class="button" href="/take-part/">Take part</a> <a class="button ghost" href="{p}hackathon/">The hackathon</a></p>
    <p class="src">Source: <a href="{SRC}">london.agentics.org</a>, {READ}</p>
  </div>
  {trace(HACK_TRACE)}
</section>

<section class="glance" aria-labelledby="gl">
  <h2 id="gl" class="vh">The chapter at a glance</h2>
  <ul class="tiles">
    <li><span class="t-k">Meetups</span><span class="t-big">2nd Wed</span><span class="t-s">every second Wednesday, online and in person; free</span></li>
    <li><span class="t-k">London members</span><span class="t-big">~300</span><span class="t-s">the chapter's own count, 23 October 2026</span></li>
    <li><span class="t-k">Founded</span><span class="t-big">May 2025</span><span class="t-s">led by six chapter co-founders</span></li>
    <li><span class="t-k">Workshops</span><span class="t-big">0.5 to 2 days</span><span class="t-s">guided builds to a working prototype</span></li>
  </ul>
  <p class="src">Source: <a href="{SRC}">london.agentics.org</a>, {READ}.</p>
</section>

<section class="pipeline" aria-labelledby="pl">
  <h2 id="pl">How the chapter works, step by step</h2>
  <ol class="steps">
    <li class="step"><p class="step-k">01 / meet</p><h3>Meetups</h3><p>Two to three hours, free. Sign up on the <a href="{LUMA}">Luma calendar</a>.</p></li>
    <li class="step"><p class="step-k">02 / build</p><h3>Workshops</h3><p>Half a day to two days of guided, hands-on building that ends with a working prototype.</p></li>
    <li class="step step-hot"><p class="step-k">03 / hack</p><h3>The hackathon</h3><p>Sovereign Websites and AgentiCCells, built with the chapter. {chip("wait", "date and venue")}</p><p><a href="{p}hackathon/">About the hackathon</a></p></li>
    <li class="step"><p class="step-k">04 / join</p><h3>Community</h3><p><a href="/about/">About the chapter</a> and <a href="/take-part/">how to take part</a>.</p></li>
  </ol>
  <p class="src">Source: <a href="{SRC}">london.agentics.org</a>, {READ}. The member count is the chapter's own, collected on 23 October 2026.</p>
</section>

<section class="agents8" aria-labelledby="ag">
{AGENTS}
</section>

<section class="join" aria-labelledby="jn">
  <h2 id="jn">Take part</h2>
  <p>Come to a meetup, join the Discord, or follow the chapter on LinkedIn and YouTube.</p>
  <p class="actions"><a class="button" href="/take-part/">How to take part</a> <a class="button ghost" href="{SRC}">london.agentics.org</a></p>
</section>
"""

def d8_hack(p):
    rows = [("done", "Agreed", "with the London chapter on a call, 24 November 2026"),
            ("done", "Shows", "examples of <a href=\"https://sovereignwebsite.ai/\">Sovereign Websites</a> and <a href=\"https://agenticcells.ai/\">AgentiCCells</a>"),
            ("next", "Test run", "before the hackathon")] + [("wait", a, b) for a, b in details_rows()]
    li = "\n    ".join(f'<li class="step step-{s}"><p class="step-k">{chip(s, "")}</p><h3>{a}</h3><p>{b}</p></li>' for s, a, b in rows)
    return f"""
<section class="hero flow hero-small" aria-labelledby="h1">
  <div class="hero-in">
    <p class="mark">Hackathon</p>
    <h1 id="h1">The London hackathon</h1>
    <p class="lead">A hackathon with the London chapter of the Agentics Foundation, showing examples of Sovereign Websites and AgentiCCells.</p>
  </div>
  {trace(HACK_TRACE)}
</section>
<div class="note" role="note"><p><strong>Draft.</strong> The steps marked "To be confirmed" have not been published yet. The chapter and Dinis Cruz agreed the hackathon on a call on 24 November 2026.</p></div>
<section class="pipeline" aria-labelledby="dt">
  <h2 id="dt">The hackathon, as a workflow</h2>
  <ol class="steps steps-list">
    {li}
  </ol>
</section>
<section class="join" aria-labelledby="ut">
  <h2 id="ut">Until then</h2>
  <p>Chapter events are listed on its <a href="{LUMA}">Luma calendar</a>, as the chapter's own site shows them. When the hackathon is published there, this page will link to it.</p>
  <p class="actions"><a class="button" href="/take-part/">Take part in the chapter</a></p>
</section>
"""

# ---------- d9 Mission control (dashboard, with the real agents behind the site) ----------


def d9_home(p):
    return f"""
<section class="hero mc" aria-labelledby="h1">
  <div class="hero-in">
    <p class="mark"><span class="live-dot" aria-hidden="true"></span> Hackathon coming up: details to be confirmed</p>
    <h1 id="h1">Hands-on agentic AI in London</h1>
    <p class="lead">Agentics London is the London (UK) chapter of the global <a href="https://agentics.org">Agentics Foundation</a>. It runs free meetups and hands-on workshops on agentic AI.</p>
    <p class="actions"><a class="button" href="/take-part/">Take part</a> <a class="button ghost" href="{p}hackathon/">The hackathon</a></p>
  </div>
</section>

<section class="board" aria-label="Chapter dashboard">
  <div class="panel panel-mission" aria-labelledby="hack">
    <p class="panel-k">Mission</p>
    <h2 id="hack">The hackathon</h2>
    <p>Showing examples of Sovereign Websites and AgentiCCells, with the chapter.</p>
    <ul class="checks">
      <li>{chip("done", "agreed with the chapter, 24 November 2026")}</li>
      <li>{chip("next", "a test run first")}</li>
      <li>{chip("wait", "date, venue and sign-up")}</li>
    </ul>
    <p><a class="button" href="{p}hackathon/">About the hackathon</a></p>
  </div>
  <div class="panel stat"><p class="panel-k">Meetups</p><p class="big">2nd Wed</p><p>every second Wednesday, online and in person. Public meetups are free. <a href="{LUMA}">Luma calendar</a></p></div>
  <div class="panel stat"><p class="panel-k">London members</p><p class="big">~300</p><p>the chapter's own count, collected 23 October 2026</p></div>
  <div class="panel stat"><p class="panel-k">Founded</p><p class="big">May 2025</p><p>led by six chapter co-founders. <a href="/about/">About the chapter</a></p></div>
  <div class="panel stat"><p class="panel-k">Workshops</p><p class="big">0.5 to 2 days</p><p>guided builds that end with a working prototype</p></div>
  {AGENTS}
  <p class="src panel-src">Figures: <a href="{SRC}">london.agentics.org</a>, {READ}.</p>
</section>

<section class="join" aria-labelledby="jn">
  <h2 id="jn">Take part</h2>
  <p>Come to a meetup, join the Discord, or follow the chapter on LinkedIn and YouTube.</p>
  <p class="actions"><a class="button" href="/take-part/">How to take part</a> <a class="button ghost" href="{SRC}">london.agentics.org</a></p>
</section>
"""

def d9_hack(p):
    rows = "\n      ".join(f"<li><span class=\"k\">{a}</span>{gap(b)}</li>" for a, b in details_rows())
    return f"""
<section class="hero mc hero-small" aria-labelledby="h1">
  <div class="hero-in">
    <p class="mark"><span class="live-dot" aria-hidden="true"></span> Hackathon</p>
    <h1 id="h1">The London hackathon</h1>
    <p class="lead">A hackathon with the London chapter of the Agentics Foundation, showing examples of Sovereign Websites and AgentiCCells.</p>
  </div>
</section>
<div class="note" role="note"><p><strong>Draft.</strong> The chapter and Dinis Cruz agreed this hackathon on a call on 24 November 2026. Details marked "To be confirmed" have not been published yet.</p></div>
<section class="board" aria-label="Hackathon dashboard">
  <div class="panel panel-mission" aria-labelledby="st">
    <p class="panel-k">Status</p>
    <h2 id="st">Where it stands</h2>
    <ul class="checks">
      <li>{chip("done", "agreed with the chapter, 24 November 2026")}</li>
      <li>{chip("done", "shows Sovereign Websites and AgentiCCells")}</li>
      <li>{chip("next", "a test run first")}</li>
    </ul>
  </div>
  <div class="panel panel-wide" aria-labelledby="dt">
    <p class="panel-k">Details</p>
    <h2 id="dt">Still to be confirmed</h2>
    <ul class="pending">
      {rows}
    </ul>
  </div>
  {AGENTS}
</section>
<section class="join" aria-labelledby="ut">
  <h2 id="ut">Until then</h2>
  <p>Chapter events are listed on its <a href="{LUMA}">Luma calendar</a>, as the chapter's own site shows them. When the hackathon is published there, this page will link to it.</p>
  <p class="actions"><a class="button" href="/take-part/">Take part in the chapter</a></p>
</section>
"""

D = {"d7": ("Swarm", d7_home, d7_hack, True), "d8": ("Workflow", d8_home, d8_hack, False), "d9": ("Mission control", d9_home, d9_hack, False)}
for i, (name, h, k, fonts) in D.items():
    pre = f"/designs/{i}/"; css = (["/assets/fonts/fonts.css"] if fonts else []) + ["/assets/base.css", f"/assets/designs/{i}.css"]
    lab = f"{i}, {name}"
    gen2.page(pre, f"Design {i}: {name}", f"Design preview {i} ({name}) of the London Agentics Foundation home page.", h(pre), css, pre, None, lab, design=i)
    gen2.page(pre + "hackathon/", f"Design {i}: {name}, hackathon", f"Design preview {i} ({name}) of the London Agentics Foundation hackathon page.", k(pre), css, pre, pre + "hackathon/", lab, design=i)
print("ok")
