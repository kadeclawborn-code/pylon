// @ts-check
import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";

// Site URL is intentionally a placeholder. Update once the domain is registered
// (see marketing/launch-tier-2-tangible/domain-options.md). The fictional company
// canon-domain is pylon.dev (see ../IDENTITY.md); the *real* benchmark site lives
// at whichever domain we actually own.
const SITE_URL = process.env.PYLON_SITE_URL || "https://pylon.example.dev";

export default defineConfig({
  site: SITE_URL,
  integrations: [tailwind(), mdx(), sitemap()],
  build: {
    format: "directory",
  },
  markdown: {
    syntaxHighlight: "shiki",
    shikiConfig: {
      theme: "github-dark",
      wrap: true,
    },
  },
});
