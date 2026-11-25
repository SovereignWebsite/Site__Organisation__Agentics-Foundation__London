# Writes the chapter pages into site/. Plain HTML out; run from the repository root: python3 -I gen.py
import os, html

HOST = "https://london.agentics-foundation.organisation.sovereignweb.site"
CARD = HOST + "/assets/share/card-1200x630.jpg"
READ = "read 24 November 2026"
SRC = "https://london.agentics.org/"

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

NAV = [("/hackathon/", "Hackathon"), ("/about/", "About the chapter"), ("/take-part/", "Take part")]


def page(path, title, desc, body, current):
    url = HOST + path
    full = "London Agentics Foundation" if path == "/" else f"{title}: London Agentics Foundation"
    t, d = html.escape(full), html.escape(desc)
    nav = "\n    ".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{n}</a>' for h, n in NAV)
    out = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta property="og:type" content="website">
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
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{FAMILY}
<header class="top">
  <a class="name" href="/">London Agentics Foundation</a>
  <nav class="own" aria-label="This site">
    {nav}
  </nav>
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
A sovereign website, made with the <a href="https://sovereignwebsite.org/">open pattern</a>. Source: <a href="https://github.com/SovereignWebsite/Site__Organisation__Agentics-Foundation__London">github.com/SovereignWebsite/Site__Organisation__Agentics-Foundation__London</a>.</footer>
</main>
</body>
</html>
"""
    f = "site" + path + ("index.html" if path.endswith("/") else "")
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(out)


def gap(what):
    return f'<span class="gap">To be confirmed: {what}</span>'


LUMA = "https://lu.ma/calendar/cal-G5qDYRTO06rtvbs"

home = f"""
<div class="mark">London chapter of the Agentics Foundation</div>
<h1>Hands-on agentic AI in London</h1>
<p class="lead">Agentics London is the London (UK) chapter of the global <a href="https://agentics.org">Agentics Foundation</a>. It runs free meetups and hands-on workshops on agentic AI. <span class="src">(Source: <a href="{SRC}">london.agentics.org</a>, {READ}.)</span></p>

<section class="feature" aria-labelledby="hack">
  <div class="mark">Coming up</div>
  <h2 id="hack">The hackathon</h2>
  <p>The chapter is planning a hackathon that shows examples of Sovereign Websites and AgentiCCells. The date, venue, format and sign-up link are not yet confirmed, and this page says so rather than guess.</p>
  <dl class="facts">
    <dt>Date</dt><dd>{gap("in the next few weeks; date not yet published")}</dd>
    <dt>Venue</dt><dd>{gap("not yet published")}</dd>
    <dt>Sign up</dt><dd>{gap("the Luma link, once it is published")}</dd>
  </dl>
  <p><a class="button" href="/hackathon/">About the hackathon</a></p>
</section>

<h2>The chapter</h2>
<ul class="plain">
  <li>Founded in May 2025, led by six chapter co-founders. <a href="/about/">About the chapter</a></li>
  <li>Online and in-person meetups every second Wednesday; public meetups are free. <span class="src">(Source: <a href="{SRC}">london.agentics.org</a>, {READ}.)</span></li>
  <li>Events are listed on the chapter's <a href="{LUMA}">Luma calendar</a>, as its own site shows them.</li>
</ul>

<h2>Take part</h2>
<p>Come to a meetup, join the Discord, or follow the chapter on LinkedIn and YouTube: <a href="/take-part/">how to take part</a>.</p>
<p>The chapter's own site is <a href="{SRC}">london.agentics.org</a>.</p>
"""

hack = f"""
<div class="mark">Hackathon</div>
<h1>The London hackathon</h1>
<p class="lead">A hackathon run with the London chapter of the Agentics Foundation, showing examples of Sovereign Websites and AgentiCCells.</p>

<div class="note" role="note">
  <p><strong>Draft.</strong> The chapter and Dinis Cruz agreed this hackathon on a call on 24 November 2026. The details below marked "To be confirmed" have not been published yet. Nothing on this page is a date, a venue or a rule until it says so.</p>
</div>

<h2>What we know</h2>
<ul class="plain">
  <li>It is planned for the next few weeks, after a test run.</li>
  <li>It shows examples of <a href="https://sovereignwebsite.ai/">Sovereign Websites</a>: websites whose owners hold the files, the history and the address, and can move them anywhere.</li>
  <li>It shows examples of <a href="https://agenticcells.ai/">AgentiCCells</a>.</li>
</ul>

<h2>The details</h2>
<dl class="facts">
  <dt>Date and time</dt><dd>{gap("not yet published")}</dd>
  <dt>Venue</dt><dd>{gap("not yet published")}</dd>
  <dt>Format</dt><dd>{gap("in person, online or both; how long it runs")}</dd>
  <dt>Who it is for</dt><dd>{gap("not yet published")}</dd>
  <dt>What to bring</dt><dd>{gap("not yet published")}</dd>
  <dt>Rules and judging</dt><dd>{gap("not yet published")}</dd>
  <dt>Sign up</dt><dd>{gap("the event's Luma link")}</dd>
</dl>

<h2>Until then</h2>
<p>Chapter events are listed on its <a href="{LUMA}">Luma calendar</a>, as the chapter's own site shows them. When the hackathon is published there, this page will link to it.</p>
<p>To hear about it first, <a href="/take-part/">take part in the chapter</a>.</p>
"""

leaders = [
    ("Bence Csernak", "https://www.linkedin.com/in/bencecsernak/"),
    ("Mondweep Chakravorty", "https://www.linkedin.com/in/mondweepchakravorty/"),
    ("Mark De Rijk", "https://www.linkedin.com/in/markderijk/"),
    ("Chris Poulter", "https://www.linkedin.com/in/chrispoulterai/"),
    ("Rocky Verma", "https://www.linkedin.com/in/rocky-verma/"),
    ("Vincent Sider", "https://www.linkedin.com/in/vincentsider/"),
]
lead_li = "\n  ".join(f'<li>{n}, Chapter Co-Founder (<a href="{u}">LinkedIn</a>)</li>' for n, u in leaders)

about = f"""
<div class="mark">About the chapter</div>
<h1>Agentics London</h1>
<p class="lead">Agentics London is the London (UK) chapter of the global Agentics Foundation. Everything on this page is from the chapter's own site, <a href="{SRC}">london.agentics.org</a>, {READ}.</p>

<h2>What it is</h2>
<p>A community of engineers, product people, strategists and educators focused on turning agentic AI into practical adoption through hands-on, face-to-face learning. Public meetups are free; paid workshops and strategy sprints cover venues, travel and community projects.</p>

<h2>The chapter in figures</h2>
<table>
  <caption>As published by the chapter. Each figure with its source and date.</caption>
  <thead><tr><th scope="col">Figure</th><th scope="col">What the chapter says</th><th scope="col">Source</th></tr></thead>
  <tbody>
    <tr><td>Founded</td><td>May 2025; first meetup 21 May 2025</td><td><a href="{SRC}">london.agentics.org</a>, {READ}</td></tr>
    <tr><td>London members</td><td>About 300, counted as members who attended at least one event in the past 90 days (collected 23 October 2026)</td><td><a href="{SRC}">london.agentics.org</a>, {READ}</td></tr>
    <tr><td>Members listed</td><td>69 members on the chapter's members page</td><td><a href="{SRC}members">london.agentics.org/members</a>, {READ}</td></tr>
    <tr><td>Meetups</td><td>Online and in person, every second Wednesday, two to three hours</td><td><a href="{SRC}">london.agentics.org</a>, {READ}</td></tr>
    <tr><td>Workshops</td><td>Half a day to two days</td><td><a href="{SRC}">london.agentics.org</a>, {READ}</td></tr>
  </tbody>
</table>
<p class="src">The two member figures count different things; both are given as the chapter publishes them.</p>

<h2>Chapter leaders</h2>
<p>The chapter was founded by UK ambassadors Bence Csernak and Mondweep Chakravorty with four other chapter leaders. Its site names six co-founders:</p>
<ul class="plain">
  {lead_li}
</ul>

<h2>How it works</h2>
<ul class="plain">
  <li><strong>Lean and agile:</strong> experiments first; most activities run under members' existing companies.</li>
  <li><strong>Open tooling:</strong> code on GitHub, and meeting artefacts shared with participants.</li>
  <li><strong>Sustainable revenue:</strong> workshops and sprints are paid; public meetups stay free.</li>
</ul>

<h2>The Agentics Foundation</h2>
<p>The chapter is part of the global <a href="https://agentics.org">Agentics Foundation</a>, founded by Reuven Cohen. The foundation's projects are on <a href="https://github.com/ruvnet">GitHub</a>.</p>

<h2>Past events</h2>
<ul class="plain">
  <li>Inaugural London chapter meetup, 21 May 2025.</li>
  <li>Panel and hands-on workshop at the International Conference on Emerging Technologies for Sustainable Innovation, University of Greenwich, June 2025 (<a href="https://lu.ma/60l032gz">event on Luma</a>).</li>
</ul>
<p>Photos and videos are in the chapter's <a href="{SRC}gallery">events gallery</a> and on its <a href="https://www.youtube.com/@AgenticsFoundationUKLondon">YouTube channel</a>.</p>
"""

take = f"""
<div class="mark">Take part</div>
<h1>How to take part</h1>
<p class="lead">The links below are the ones the chapter's own site, <a href="{SRC}">london.agentics.org</a>, gives ({READ}).</p>

<h2>Come to an event</h2>
<p>Meetups run every second Wednesday, online and in person, and public meetups are free. Sign up for each one on the chapter's <a href="{LUMA}">Luma calendar</a>.</p>
<p>The hackathon will be listed there too: <a href="/hackathon/">what we know so far</a>.</p>

<h2>Join the chapter</h2>
<p>There is no membership fee. Join with the chapter's <a href="https://docs.google.com/forms/d/e/1FAIpQLScL067CCJSympjEV4BxOVBuKGQcQqOtOkM37taGGYBjiNNBgA/viewform?usp=header">membership form</a>.</p>

<h2>Follow and talk</h2>
<ul class="plain">
  <li><a href="https://discord.agentics.org/">Discord</a>: the Agentics Foundation community.</li>
  <li><a href="https://www.linkedin.com/company/agentics-org">LinkedIn</a>: the Agentics Foundation.</li>
  <li><a href="https://www.youtube.com/@AgenticsFoundationUKLondon">YouTube</a>: the London chapter's recordings.</li>
  <li><a href="https://community.agentics.org/">community.agentics.org</a>: the foundation's community site.</li>
</ul>

<h2>Workshops, talks and partnerships</h2>
<p>For a workshop, a talk or a partnership, use the "Get Involved" section of <a href="{SRC}">london.agentics.org</a>.</p>
"""

page("/", "Home", "The London chapter of the Agentics Foundation, and its coming hackathon showing Sovereign Websites and AgentiCCells.", home, "/")
page("/hackathon/", "Hackathon", "The London Agentics hackathon showing examples of Sovereign Websites and AgentiCCells: what is known, and what is still to be confirmed.", hack, "/hackathon/")
page("/about/", "About the chapter", "Agentics London, the London chapter of the Agentics Foundation: what it is, its leaders and its figures, from its own site.", about, "/about/")
page("/take-part/", "Take part", "How to take part in the London chapter of the Agentics Foundation: Luma, Discord, LinkedIn and YouTube.", take, "/take-part/")
print("ok")
