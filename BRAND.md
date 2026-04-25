# Pylon — Brand Guidelines

## Voice and tone

Pylon's brand voice is **direct, technical, and slightly dry**. Pylon talks to engineers the way good engineers talk to each other: respectful of the reader's time, comfortable with detail, allergic to hype.

### Voice principles

1. **Lead with the point.** State the conclusion first. Provide the reasoning afterward, not before.
2. **Use plain language.** "Use" not "utilize." "Start" not "initiate." "Help" not "facilitate." If a shorter word does the job, the shorter word wins.
3. **Be specific.** Numbers, names, examples. *"Reduces false positives by ~40% in our test corpus"* is Pylon. *"Significantly improves accuracy"* is not.
4. **Trust the reader.** Don't define terms a reader at a 50-engineer Series B would know. Don't repeat yourself.
5. **Own uncertainty.** When something is unproven or unclear, say so. *"We don't yet know if this scales beyond ~5,000 PRs/day"* beats a hedged claim of certainty.
6. **Disagree openly.** Pylon's blog posts often argue against a popular practice. The argument should be specific and falsifiable, not contrarian-for-its-own-sake.

### Tone calibration by surface

| Surface | Tone |
|---|---|
| Product UI | Terse, factual, instructive. No marketing copy. |
| Error messages | Specific, actionable, calm. *"Couldn't reach GitHub at 14:32:01. Retrying in 30s."* |
| In-PR comments | Engineering-respectful peer-review tone. Never patronizing. |
| Documentation | Reference-doc clarity. Examples first, prose second. |
| Marketing site | Plainspoken; minimal adjectives. Light use of dry humor when it earns its place. |
| Blog | Conversational technical writing. First-person plural ("we") when about Pylon's own decisions; first-person singular when an individual engineer is the byline. |
| Sales enablement | Same voice as marketing. No sales-deck euphemisms. Discounts and contract terms are stated, not insinuated. |
| Customer support | Direct, fast, action-oriented. *"That's a known bug in 2.4.1; fix shipped in 2.4.2 yesterday. Updating now."* |
| Internal Slack | Casual but precise. Engineers' Slack-vernacular is fine; trolling colleagues is not. |

### Banned phrases

These read as inauthentic to engineers and Pylon avoids them everywhere — including marketing, including blog posts, including sales:

- "Game-changer" / "next-gen" / "revolutionary"
- "Empower" / "unlock" / "harness"
- "Best-in-class" / "world-class" / "industry-leading"
- "Cutting-edge" / "bleeding-edge"
- "Synergy"
- "Robust" (as a generic adjective; specific is fine)
- "Seamless" / "frictionless"
- "Solution" (as in "our solution") — say what it is instead
- "We're excited to announce…" / "We're thrilled to share…"
- "Reach out" — say "email", "DM", "open an issue", whatever's specific

### Punctuation conventions

- **No exclamation points.** Anywhere. The product UI, the marketing site, the blog, sales decks, internal Slack — none. The exception: a single exclamation point in a customer-facing announcement when something is genuinely on fire ("Pylon is currently down. We're investigating."). Even then, use sparingly.
- **Em-dashes are fine** — they fit the voice. Don't overuse.
- **Oxford comma**: yes.
- **Title case** for product names (Pylon, Beacon, Tower, Switchyard) and feature names. Sentence case for everything else.
- **Numbers**: spelled out one through nine in prose; numerals for 10+. In product UI, always numerals.

### Examples

**Good (in Pylon's voice):**
> Beacon's default ruleset catches roughly 80% of the issues we'd want it to. The other 20% is what your custom rules are for.

> We removed the "AI-Powered Suggestions" badge from the dashboard last month. Customers told us it felt thin, and they were right.

> Pylon's Free tier limits you to 5 active devs because that's where most useful customer feedback ends. You'll outgrow Free before you'd want to keep using it.

**Bad (banned):**
> Pylon revolutionizes code review by leveraging cutting-edge AI to empower your engineering teams!

> We're excited to announce a game-changing new feature that takes Pylon to the next level!

## Visual identity

> Visual assets are placeholder for now — actual logos and color refinements are POC 1.5 work. The system below is canon for v0.1.

### Logo

Pylon's wordmark uses a custom monospace-inspired typeface set in two weights. The "P" has a slight asymmetry on the bowl that signals "engineered" rather than "designed."

A standalone glyph (an angular pylon-tower shape) exists for square avatars, app icons, and the favicon. It is not paired with the wordmark in the same surface.

### Color palette

| Role | Hex | Use |
|---|---|---|
| Pylon Blue | `#1F3D7A` | Primary brand. Wordmark, headers, primary CTAs. |
| Pylon Black | `#0D1014` | Body text on light backgrounds. |
| Surface | `#FFFFFF` | Default canvas, light mode. |
| Surface Dim | `#F5F6F8` | Cards, secondary surfaces, light mode. |
| Surface Dark | `#13161B` | Default canvas, dark mode. |
| Surface Dark Dim | `#1B1F26` | Cards, secondary surfaces, dark mode. |
| Accent Amber | `#E89236` | Warnings, "this is unusual but probably fine" findings. |
| Accent Red | `#C8473D` | Blocking findings, errors. Use sparingly. |
| Accent Green | `#4F8F5A` | Confirmations, "all clear" states. |
| Accent Slate | `#7B8794` | De-emphasized text, captions, secondary metadata. |

The dashboard and marketing site default to **dark mode** because most engineers use dark editors. Light mode is supported.

### Typography

| Use | Family | Weights |
|---|---|---|
| Headings (UI + marketing) | Söhne | 600, 700 |
| Body | Söhne | 400, 500 |
| Code, monospace data, in-PR comments | JetBrains Mono | 400, 600 |
| Display (rare; large hero text only) | Söhne Breit | 600 |

Söhne is a paid license; Pylon owns it for web + product use. The fallback stack for unloaded states is `system-ui, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif`.

### Layout

- 8px grid for product UI; 4px sub-grid for dense data displays.
- Generous line-height (1.55–1.65 in body) — engineers read a lot.
- Code blocks always have copy-to-clipboard, syntax highlighting, and a language label.
- No animation on load. Subtle micro-interactions on user-driven actions (hover, click) are fine but optional.

## Photography and illustration

- **No stock photos** of smiling people in headsets. Ever.
- **No 3D abstract gradient blobs** or generic "tech" illustrations.
- **Yes**: real photos of Pylon employees on the careers page (or carefully-staged synthetic equivalents at this scale). Real photos of customer engineering teams (with consent) on case study pages.
- **Yes**: technical diagrams. Architecture diagrams in Pylon's blog use a consistent style (boxes-and-arrows, mostly black-on-white, occasional accent color for emphasis).
- **Illustration**: minimal, hand-drawn-feeling line art when used at all. The Beacon rule pack landing page uses small isometric cartoons for each rule category — that's the upper bound of illustration density.

## Reviewing this brand

Pylon's brand is allowed to evolve. Triggers for revisiting it:

- A new audience segment becomes meaningful (e.g., security-team buyers, not just engineering)
- An adjacent product lands and needs visual differentiation
- The wordmark / glyph fail at small sizes in real product use
- Competitor positioning shifts and Pylon needs to re-stake the "narrow door" argument

Until one of those triggers fires, this guide is canon.
