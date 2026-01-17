# Dynasties of Ash and Wood

Campaign wiki and session archive for our Pathfinder 2e game.

## What This Is

A shared reference site for 5 players and a GM playing remotely. Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and hosted on GitHub Pages.

## Site Structure

### Wiki
- **Player Characters** — the party
- **NPCs** — people we've met
- **Factions** — groups, organizations, powers
- **Locations** — places we've been or heard about

### Session Summaries
Recaps of each session, cross-linked to relevant wiki entries.

## Workflow

After each session:
1. Generate a session summary using the prompt (TBD)
2. Update relevant wiki pages with new information
3. Commit and push — the site rebuilds automatically

## Running Locally

```bash
# Install dependencies
pip install mkdocs-material

# Start local server
mkdocs serve
```

Then open [http://localhost:8000](http://localhost:8000).

## Contributing

Found something wrong? Want to add details to your character or an NPC? Edit the markdown files in `docs/` and open a PR — or just push if you have access.

## Deployment

Pushes to `main` automatically deploy to GitHub Pages via GitHub Actions.

---

*More setting details coming soon.*
