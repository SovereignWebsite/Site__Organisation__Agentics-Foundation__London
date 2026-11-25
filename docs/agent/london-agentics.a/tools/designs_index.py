import sys; sys.path.insert(0, sys.argv[1]); import gen2
def row(i, n, note, live=True):
    return f'<li><a href="/designs/{i}/"><strong>{i}, {n}</strong></a> (<a href="/designs/{i}/hackathon/">hackathon page</a>): {note}</li>'
body = f"""
<div class="mark">Design rounds</div>
<h1>Designs for this site</h1>
<p class="lead">Nine designs of this site, all live. The picker features five for the chapter to choose from, with the other four under "Earlier rounds". Each is the same content, the home page and the hackathon page, styled a different way.</p>
<h2>How to choose</h2>
<ol>
  <li>On any page, open <strong>Choose a design</strong> at the top and click through the five (or the four under Earlier rounds). Each opens at its own address, <code>/designs/d1/</code> to <code>/designs/d9/</code>, with its own hackathon page.</li>
  <li>Tell Dinis Cruz which number the chapter wants (or a mix: "d8, with d9's agents panel"), in writing.</li>
  <li>The keeper records the pick in three places: the "Recorded pick" line in every page's picker, the line below on this page, and the commit that makes it the default, each saying who chose and where. Until then the default is <strong>d8, Workflow</strong>, the keeper's recommendation.</li>
</ol>
<p>All designs load nothing from anywhere else: they use the visitor's own fonts, except d7, whose open-licence fonts are served from this site. None uses the chapter's logo or branding. Each passes the accessibility check (axe) in light and dark mode. Designs d2 to d9 were checked in both.</p>

<p><strong>Recorded pick:</strong> none yet.</p>

<h2>Round 6 (25 November 2026): small fixes</h2>
<ul class="plain">
  <li>d8 on phones says what the chapter is before showing the run.</li>
  <li>The design strip at the top of each preview fits on two lines on a phone.</li>
  <li>d7 on phones shows its agent network as a solid band above the heading.</li>
  <li>This page now says where the chapter's pick is recorded.</li>
</ul>

<h2>Round 5 (25 November 2026): after a.design's review</h2>
<p>a.design, the design reviewer for this account, reviewed round 4 and agreed on d8 as the default. Changes:</p>
<ul class="plain">
  <li>d8 now carries d9's fact tiles (each with its source) and its "Built by agents" panel; on phones d8's run panel comes straight under the heading.</li>
  <li>On phones the Sovereign Website credit no longer covers the design banner (this also fixes the one contrast failure, on d9).</li>
  <li>The kicker no longer repeats the site's name: it says the hackathon is coming up and its details are to be confirmed.</li>
  <li>Until the hackathon has a date, <strong>Take part</strong> is the main button and the hackathon the second.</li>
  <li>Shorter header links ("About"), so they no longer wrap on phones.</li>
  <li>The picker features five designs (d8, d7, d9, d6, d4); d1, d2, d3 and d5 stay live under Earlier rounds, and the picker records the pick.</li>
</ul>

<h2>Round 4 (24 November 2026): agent-first</h2>
<p>Designs built around agents and the agentic workflow, after a look at how the Agentics Foundation presents itself at <a href="https://agentics.org/">agentics.org</a> and <a href="https://london.agentics.org/">london.agentics.org</a>.</p>
<ul class="plain">
  {row("d7", "Swarm", "in step with the Foundation's own look: warm cream, coral, condensed headings over a monospace body, the terminal window and the [ ] brackets, with a live agent network behind the hero. Its two open-licence typefaces are served from this site. No logo or wordmark: whether to align this closely is the chapter's call.")}
  {row("d8", "Workflow", "the page is an agent run. The hero shows the hackathon as a live trace, the chapter is a pipeline of steps, and every detail still to be confirmed is a pending step rather than a gap.")}
  {row("d9", "Mission control", "the chapter as a dashboard: the hackathon is the mission, each figure a tile with its source, and one panel shows the real agents and checks behind this site.")}
</ul>

<h2>Round 3</h2>
<ul class="plain">
  {row("d6", "Signal", "Poster's dark hero and lime, the Swiss grid's numbered sections, and monospace for dates and every &quot;to be confirmed&quot;. Round 3 tightened the spacing, gave each gap its own labelled box, and fixed the numbers in dark mode. The keeper's recommendation before round 4.")}
  {row("d4", "Swiss grid", "Round 3 removed the empty rows under each section. The calmest and most readable option.")}
</ul>

<h2>Round 2</h2>
<ul class="plain">
  <li>Took d2, d4 and a new hybrid, d6, forward. Fixed in all: the design banner now sits in a landmark; the source notes are one size.</li>
  {row("d2", "Poster", "the hero button's text was white on lime (failed contrast): fixed; the top bar no longer runs under the Sovereign Website menu.")}
</ul>

<h2>Round 1: five directions</h2>
<ul class="plain">
  {row("d1", "Editorial", "a printed programme: serif, warm paper, rules. Calm, but reads as a literary magazine more than a hackathon. Not taken forward.")}
  {row("d2", "Poster", "a dark event poster with very large type and one lime accent. The most energy.")}
  {row("d3", "Terminal", "an engineer's console in monospace. On topic, but long text is tiring to read. Its monospace data labels live on in d6.")}
  {row("d4", "Swiss grid", "a strict grid with numbered sections and one red. The clearest structure.")}
  {row("d5", "Community", "soft colours and rounded cards. Friendly, but generic. Not taken forward.")}
</ul>
"""
gen2.page("/designs/", "Designs: London Agentics Foundation", "The nine designs of the London Agentics Foundation site, how to choose one, and the design rounds that made them.", body, ["/assets/base.css", "/assets/designs/d8.css"], "/", None, design=None)
print("ok")
