# Learnings (london-agentics.a)

- Put unconfirmed facts on the page as visible "To be confirmed" gaps; reviewers and the owner trusted the site more for it.
- The container's global git signer can override your key: always set the signing config locally and verify with `git verify-commit` against your own allowed-signers line.
- Run axe at phone width and in both colour schemes: the only contrast failures found were phone-only or dark-only.
- Content-hash stylesheet links (`?v=`) and give images width/height, or a cached old stylesheet can break a new layout.
- The Factory pushes to dev while you work: fetch and rebase before pushing.
- Keep generator scripts in the repository (docs/), not only in a scratchpad, so a new session can regenerate.
- Relayed words from the owner (via sites.a) are second-hand: act when they fit his direction and are reversible, and record them as relayed in the commit.
