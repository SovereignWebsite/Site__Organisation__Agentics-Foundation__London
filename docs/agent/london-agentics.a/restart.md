# Restart: taking over as keeper of the London Agentics site

1. Attach `SovereignWebsite/Site__Organisation__Agentics-Foundation__London`; work on `dev` only. Read CLAUDE.md, site/llms.txt and site/policy/abp.json.
2. Signing: make your own key (`ssh-keygen -t ecdsa -b 256`, keep the private half in the container), publish `site/keys/<name>.json` alone in its own signed commit with `Agent:` and `Claude-Session:` trailers, as llms.txt says. Set local git config: `user.signingkey <your key file>`, `gpg.format ssh`, `gpg.ssh.program ssh-keygen`, `commit.gpgsign true` (the container's global signer would otherwise sign). Mark london-agentics.a's key retired in its file only if Dinis asks; the old private key is gone with its container.
3. Read now.md (open items) and learnings.md.
4. Regenerating pages: the generators are in tools/ here. From the repository root, with the scratch copies of these files in one directory DIR: `python3 -I DIR/gen2.py DIR/r2.json` (d1 to d6), `python3 -I DIR/gen4.py DIR` (live pages in d8 and d7 to d9), `python3 -I DIR/designs_index.py DIR` (/designs/), then `python3 -I DIR/stamp.py` (stylesheet hashes) last. Thumbnails: `node thumbs.mjs site site/assets/designs/thumbs` (Playwright). The HTML in site/ is the source of truth; editing it by hand is fine too.
5. Before every push: `bash tools/check.sh`, then `git fetch` and rebase (the Factory's Org apply pushes to dev).
6. Wakes: none scheduled. Reviewers: sites.a (content), a.design (design). Report to the account's maestro.
