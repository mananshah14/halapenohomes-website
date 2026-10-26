# Deploying halapenohomes.com — GitHub Pages + Cloudflare DNS

Repo: https://github.com/mananshah14/halapenohomes-website (public). The site is static; nothing to build on the server.

## 1. Push the code (2 minutes, from your Mac)

Unzip `halapenohomes-website-repo.zip`. It is a ready git repository (commit already made, remote already set to your repo).

```bash
cd halapenohomes-website
git push -u origin main
```

If the repo on GitHub is not empty (e.g. it has a README), push once with `git push -u origin main --force` — nothing of value is there yet.

## 2. Turn on GitHub Pages (1 minute)

GitHub → the repo → **Settings → Pages**
- Build and deployment → Source: **Deploy from a branch**
- Branch: **main**, folder **/ (root)** → Save
- Custom domain: it should auto-fill **halapenohomes.com** from the `CNAME` file in the repo. If it's empty, type it and Save.
- Leave **Enforce HTTPS** unticked for now — it becomes available once DNS resolves and GitHub has issued the certificate (usually 10–60 min after step 3).

The site is immediately live at https://mananshah14.github.io/halapenohomes-website/ while the domain propagates (it will redirect to the custom domain once set).

## 3. DNS on Cloudflare (3 minutes)

Cloudflare dashboard → halapenohomes.com → **DNS → Records**. Delete any existing A / AAAA / CNAME records for `@` and `www` that point elsewhere (parking pages etc.), then add:

| Type  | Name | Content                      | Proxy status |
|-------|------|------------------------------|--------------|
| A     | @    | 185.199.108.153              | DNS only (grey cloud) |
| A     | @    | 185.199.109.153              | DNS only |
| A     | @    | 185.199.110.153              | DNS only |
| A     | @    | 185.199.111.153              | DNS only |
| AAAA  | @    | 2606:50c0:8000::153          | DNS only |
| AAAA  | @    | 2606:50c0:8001::153          | DNS only |
| AAAA  | @    | 2606:50c0:8002::153          | DNS only |
| AAAA  | @    | 2606:50c0:8003::153          | DNS only |
| CNAME | www  | mananshah14.github.io        | DNS only |

Keep every record **DNS only (grey cloud)** until GitHub shows the certificate as issued and you've ticked **Enforce HTTPS**. After that you may switch them to Proxied (orange) if you want Cloudflare's CDN — if you do, set **SSL/TLS → Overview → Full (strict)** first, otherwise you get a redirect loop.

Cloudflare DNS propagates in a minute or two; GitHub's "DNS check" on the Pages settings page goes green shortly after.

## 4. Lock the domain to your GitHub account (optional, recommended)

GitHub → your profile **Settings → Pages → Add a domain** → `halapenohomes.com`. GitHub gives you a TXT record (`_github-pages-challenge-mananshah14`) — add it in Cloudflare, click Verify. This stops anyone else's repo from claiming the domain if Pages is ever turned off.

## 5. After go-live

- Open https://halapenohomes.com on a phone and a laptop; scroll the hero (portal opens), throw the deck cards, click a WhatsApp button.
- **The WhatsApp number, Instagram and email are still placeholders** (`910000000000`, `halapenohomes`, `hello@halapenohomes.com`) and bed availability is sample data. Edit the `CONFIG` block at the bottom of `src/template.html`, run `python3 src/build.py`, commit, push. Pages redeploys in about a minute.
- Every future change is the same loop: edit `src/template.html` → `python3 src/build.py` → commit → push.

## Troubleshooting

- "Domain's DNS record could not be retrieved" on the Pages page → records not saved yet or still proxied (orange); set to DNS only and wait 5 min, then click Check again.
- Certificate stuck → remove the custom domain in Pages settings, save, re-add it, save. Then wait.
- Site shows the README instead of the page → Pages source is wrong (must be branch `main`, folder `/ (root)`), or `index.html` isn't at the repo root.
- Changes not showing → hard refresh (Cmd-Shift-R); GitHub Pages caches for ~10 min.
