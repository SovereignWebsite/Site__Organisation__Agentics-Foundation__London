# The live pages in the default design (d8, Workflow), with the picker. python3 -I gen4.py <scratchpad>
import sys
sys.path.insert(0, sys.argv[1]); import gen2
src = open(sys.argv[1] + "/gen.py").read(); src = src[:src.index('page("/", "Home"')]
ns = {}; exec(compile(src.replace("import os, html", "import os, html"), "gen.py", "exec"), ns)
import importlib.util
spec = importlib.util.spec_from_file_location("gen3", sys.argv[1] + "/gen3.py"); g3 = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0], sys.argv[1]]; spec.loader.exec_module(g3)   # also refreshes /designs/d7..d9
css = ["/assets/base.css", "/assets/designs/d8.css"]; D = "d8"
gen2.page("/", "London Agentics Foundation", "The London chapter of the Agentics Foundation, and its coming hackathon showing Sovereign Websites and AgentiCCells.", g3.d8_home("/"), css, "/", None, index=True, design=D)
gen2.page("/hackathon/", "Hackathon: London Agentics Foundation", "The London Agentics hackathon showing examples of Sovereign Websites and AgentiCCells: what is known, and what is still to be confirmed.", g3.d8_hack("/"), css, "/", "/hackathon/", index=True, design=D)
gen2.page("/about/", "About the chapter: London Agentics Foundation", "Agentics London, the London chapter of the Agentics Foundation: what it is, its leaders and its figures, from its own site.", ns["about"], css, "/", "/about/", index=True, design=D)
gen2.page("/take-part/", "Take part: London Agentics Foundation", "How to take part in the London chapter of the Agentics Foundation: Luma, Discord, LinkedIn and YouTube.", ns["take"], css, "/", "/take-part/", index=True, design=D)
print("live pages ok")
