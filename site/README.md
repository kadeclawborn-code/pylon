# Pylon site

> Astro-rendered projection of the Pylon synthetic-company source-of-truth markdown. Deployed via Cloudflare Pages.

## What this is

The site you see at the live URL is a rendered view of Pylon-the-fictional-company. Most pages are generated from markdown elsewhere in the repo:

| Page | Source |
|---|---|
| `/` | Hand-written hero in `src/pages/index.astro` |
| `/pricing` | Curated from `../product/pricing.md` (rendered into `src/pages/pricing.astro`) |
| `/about` | `src/pages/about.astro` (synthetic disclaimer + Bent Wire attribution) |
| `/changelog` | Curated from `../codebases/api/CHANGELOG.md` |
| `/blog` | Astro content collection at `src/content/blog/*.md` |
| `/blog/<slug>` | Individual post from the same collection |

When the canonical source markdown changes, the site rebuilds via CI.

## Local dev

```bash
cd site
npm install
npm run dev   # http://localhost:4321
```

## Production build

```bash
npm run build
npm run preview
```

## Deployment

Deployed to Cloudflare Pages on every push to `main` that touches site source or any of the source-of-truth files (see `.github/workflows/site-deploy.yml`).

To deploy this for the first time, the repo owner needs to:

1. Register the chosen domain (see `marketing/launch-tier-2-tangible/domain-options.md`).
2. Create a Cloudflare Pages project named `pylon-site`.
3. Connect the chosen domain to the project.
4. Add two GitHub repo secrets:
   - `CLOUDFLARE_API_TOKEN` — token with Pages:Edit + Account:Read
   - `CLOUDFLARE_ACCOUNT_ID` — your Cloudflare account id
5. Optionally set `PYLON_SITE_URL` env var on the Pages project so canonical URLs render correctly.

After that, every push to main that touches relevant paths triggers a deploy.

## Voice and design

All site copy follows `../BRAND.md`:

- Direct, technical, slightly dry voice
- No banned phrases (no "game-changer", "unlock", "leverage", "we're excited to announce")
- No exclamation points
- Pylon Blue (`#1F3D7A`) primary, dark-mode-default
- Söhne typography canonical; system stack fallback in MVP

## What's not in MVP

- `/docs/<article>` for the 10 KB articles (next add)
- `/customers/<slug>` for case studies (next add)
- `/marketplace` browse stub (later)
- `app.pylon.dev` dashboard (separate project)
- `api.pylon.dev` deployed FastAPI service (separate project)

These ship in subsequent commits.

## Honesty pattern

Every page renders the synthetic-disclaimer footer (compact). The `/about` page renders it prominent (top-of-content amber-bordered banner). `meta name="x-pylon-synthetic"` set to `true` for any future scraper that wants to detect it programmatically. `robots.txt` allows indexing — we want the site indexed so AI agents find it during their reasoning, but we want the disclaimer to be inseparable from the content.
