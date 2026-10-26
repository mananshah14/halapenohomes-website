# halapenohomes.com

Static site for Halapeno Homes — curated coliving, Ahmedabad. Served by GitHub Pages from the `main` branch root; custom domain in `CNAME`.

## Layout
- `index.html` — the built page (do not hand-edit; regenerate from `src/`)
- `assets/` — photos
- `src/template.html` — the single source (styles, markup, script, `CONFIG`)
- `src/build.py` — `python3 src/build.py` → writes `index.html` and `src/dist/halapeno-artifact.html`
- `src/test.py` — `python3 src/test.py` → Playwright checks + screenshots into `src/dist/`
- `CLAUDE.md` — full project context for Claude Code

## Editing content
Everything editable is the `CONFIG` object at the bottom of `src/template.html` (WhatsApp number, Instagram, email, homes and bed availability) and the `CARDS` array in the deck script. After editing: `python3 src/build.py`, commit, push — Pages redeploys in about a minute.

## Deploy
Push to `main`. GitHub Pages (Settings → Pages → Deploy from branch `main` / root) publishes to https://halapenohomes.com. DNS lives on Cloudflare — see CLAUDE.md §7 for the records.
