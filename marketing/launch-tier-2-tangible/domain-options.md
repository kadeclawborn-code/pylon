# Domain options for the Pylon benchmark site

Per the Tier-2 tangible-site plan, Pylon's fictional canon-domain is `pylon.dev` (referenced throughout `IDENTITY.md`, `product/pricing.md`, etc.). The fictional company "owns" pylon.dev. The actual benchmark site we deploy lives at a *different* real URL we own — keeping the fiction internally coherent while being honest that this site is a rendering of a synthetic company, not the synthetic company itself.

## Recommended candidates

Listed in rough order of preference. Pick one; register; update `.github/workflows/site-deploy.yml` `PYLON_SITE_URL` secret + `astro.config.mjs` if needed.

### `pylon-bench.dev` (recommended)

- **Pros:** Short, descriptive (`-bench` reads as "benchmark"), matches the project's framing. Available on .dev TLDs as of last check (verify before purchase).
- **Cons:** Slightly less canonical than `pylon.dev` would be.
- **Fits:** "The Pylon benchmark site."

### `pylon-corp.dev`

- **Pros:** Reads as a generic-corporate-website domain (which is what a synthetic B2B SaaS company "would" use). Plays the role.
- **Cons:** Less obviously a benchmark; could be mistaken for a real company more easily.
- **Fits:** Higher visual realism but requires extra disclaimer discipline.

### `pylon.kade-clawborn.dev`

- **Pros:** Free if you own `kade-clawborn.dev` (or similar). Subdomain of an existing studio domain. Cheapest. Clear it's an OSS-project URL.
- **Cons:** Loses some realism; less brand-coherent for the "real-feeling synthetic company" effect.
- **Fits:** Pragmatic if cost / time matters.

### Other plausibles

- `usepylon.dev` (very 2020s SaaS naming convention; somewhat distinctive)
- `pylon.studio` (different TLD; "studio" reads as creative agency, less like a B2B SaaS)
- `pylon-review.dev` (descriptive — Pylon-the-product is PR review automation, so this works as the company URL)
- `pylonsoft.dev` (somewhat dated; "soft" suffix evokes 2010s enterprise software)

## Domains to AVOID

- `pylon.dev` — almost certainly registered to a real entity. If you find it available, that's the win, but don't count on it.
- Any close-to-real-company domain (`pylonindustries.com`, etc.) where you risk impersonating an actual business.
- Single-letter or super-short variants — too easy to confuse with typos of real domains.

## Registration step

```bash
# Example: registering via Namecheap / Cloudflare Registrar / etc.
# (manual step — depends on your registrar of choice)

# Once registered, set up DNS pointing to Cloudflare Pages:
# CNAME @ → <project>.pages.dev
# (Cloudflare Pages domain wizard handles this if you use Cloudflare Registrar)
```

## After registration — wiring

1. Add the domain to the Cloudflare Pages project (`pylon-site`).
2. Add GitHub repo secret `PYLON_SITE_URL` set to `https://<your-domain>` (or just leave it; the workflow falls back to the placeholder otherwise).
3. Push a no-op commit on main to trigger first deploy.
4. Verify the site loads at the new URL with the synthetic-disclaimer footer visible on every page.

## Coherence rule

Once the real domain is chosen and the site deploys:

- **Don't** change `IDENTITY.md` to claim Pylon-the-fictional-company is at the real domain — the fiction stays at `pylon.dev`.
- **Do** put the real domain in `site/README.md` and the `/about` page so visitors understand the relationship.
- **Don't** put the real domain in any in-canon Pylon artifact (tickets, PRs, support conversations, KB articles) — those are the fictional company speaking, not the OSS project.

The two layers stay separate. Fictional company is in canon; benchmark site renders that canon at a real URL.
