# Pylon LLC — Blueprint

> Starting context for any agent or human picking this project up. Read this end-to-end on first entry.

## What Pylon is

**Pylon LLC is a synthetic, open-source B2B SaaS company built as a benchmark substrate for AI agent tooling.** It exists in this repo as files, fixtures, runnable services, and (eventually) a small set of autonomous agents that simulate ongoing internal activity. Anyone — Bent Wire Studio specifically, but also the broader community — can run AI agent POCs against Pylon's coherent multi-domain world.

Pylon is **fictional**. None of its customers, employees, codebases, financials, or events refer to real entities. The plausibility is the point: it should look real enough that an LLM reasons about it as a coherent company, while being entirely controllable for testing.

## Why this exists

Most AI agent demos use disconnected fixtures: a few mock tickets, a stub repo, a sample customer chat. That's why agentic projects so often fail in real enterprise use — the demo data lacks the *cross-system coherence* that makes enterprise reasoning hard.

Pylon fills that gap. It models a real company across product, engineering, marketing, sales, support, finance, ops, security, and compliance — with the artifacts in each layer referring to each other consistently. An AI tool tested against Pylon gets a real-feeling enterprise to reason over.

For [Bent Wire Studio](https://github.com/kade-clawborn/bentwire) (the AI-experimentation studio building this), Pylon serves three purposes:

1. **Substrate** — every Bent Wire POC runs against Pylon's data
2. **Coherence** — POCs can chain: a release-notes POC consumes the same PR history that a security-review POC scanned earlier
3. **Public artifact** — Pylon itself is a published OSS deliverable, open to any team building or benchmarking AI agents

## The four foundational decisions

| Decision | Choice | Rationale |
|---|---|---|
| Vertical | **B2B SaaS** | Mirrors the customer profile most AI tooling targets; Bent Wire's POCs naturally fit this domain |
| Name | **Pylon LLC** | Short, abstract, evokes load-bearing infrastructure. Ungoogleable enough to avoid real-company collisions |
| Build path | **Series of POCs through Bent Wire's intake flow** | Bent Wire eats its own dog food. Each tier ships as a Bent Wire output (Medium post + OSS release per slice) |
| Visibility | **Public on GitHub from day 1** | Bent Wire's charter prioritizes OSS contributions; community adoption accelerates if Pylon is open from the start |

## Pylon's fictional identity (canonical)

> The next agent uses these as ground truth when generating any Pylon artifact.

- **Name:** Pylon, LLC (lowercase domain `pylon.dev`)
- **Tagline:** *"Stop merging surprises. Pylon catches what review missed."*
- **Product:** **Pylon** — a developer-focused PR review automation platform. It plugs into GitHub/GitLab/Bitbucket, runs configurable lint/security/architectural checks on pull requests, surfaces regressions before merge, and gives engineering managers metrics on review quality and cycle time. Sold to engineering teams (10–500 engineers).
- **Founded:** 2021
- **Headcount:** ~70 employees (mid-market scale)
- **Funding:** Series B, $35M raised total
- **Headquarters:** Remote-first, Delaware C-corp, US-only at launch
- **Pricing tiers:** Free (≤5 devs), Team ($29/dev/mo), Business ($59/dev/mo), Enterprise (custom)
- **Customers (canon shapes, not real):** ~250 paying accounts ranging from 10-dev startups to 800-engineer mid-market platforms
- **Tech stack:** Python (FastAPI) backend, TypeScript/React frontend, Postgres + Redis + ClickHouse for analytics, Cloudflare edge, deployed on AWS us-east-1
- **Brand voice:** Direct, technical, slightly dry. No exclamation points. Engineering-respectful — never patronizing, never over-marketed.

The choice of "PR review automation" as Pylon's product is intentional: Bent Wire will frequently build code-tooling POCs, and having a Pylon that *itself* is in that domain creates organic test scenarios (Bent Wire's POCs about PR review can be tested against Pylon's PR review codebase + its customers' usage data — meta but legible).

## Full surface area — the 12 layers

These are the artifact types a real B2B SaaS company maintains. Pylon will eventually have all of them; Tier 0 covers a viable subset.

### 1. Identity / strategy
Mission, values, brand voice, public positioning. Annual OKRs/KPIs. Strategic plan. Board materials. Investor decks. Fundraising history.

### 2. Org / people
Org chart with named personas. Job descriptions, leveling, comp bands (synthetic). Hiring pipeline (open roles, candidates, interview feedback). Performance reviews. Internal Slack history. All-hands transcripts. Memos. Reporting lines.

### 3. Product
Product portfolio. PRDs. Design specs. Feature flags. Pricing pages. Plan tiers. Roadmap (current quarter + 4 forward). Beta programs. Launch plans. Competitive analysis. Kill files.

### 4. Engineering
Multiple codebases (monolith, mobile, edge svcs, internal tools) — runnable code. Architecture diagrams. ADRs (Architecture Decision Records). API specs (OpenAPI/GraphQL). Database schemas + seed data. CI/CD configs. Incident postmortems. On-call rotation. Runbooks. Security posture. Threat models. SBOMs.

### 5. Project management / SDLC
JIRA-shaped tickets (epics, stories, tasks, bugs) — hundreds across history. Sprint history. Velocity. Burndown. PR history with comments and reviews. Release notes per version. Bug triage queue. Severity definitions.

### 6. Sales / marketing
Marketing site (running, not just markup). Brand guidelines. Blog archive (50+ posts). Whitepapers. Case studies. Social history (tweets, LinkedIn, YouTube transcripts). Email campaigns. Newsletter archive. Drip sequences. SEO content strategy + keywords. CRM (leads, accounts, opportunities, deal stages, won/lost reasons). Sales playbook. Synthetic call transcripts. ABM target lists.

### 7. Customer / support
B2B customer accounts (50–500). B2C user personas (thousands). Support ticket history (multi-channel: email, chat, phone transcripts). Knowledge base. Help docs. FAQ. Chat transcripts. NPS / CSAT survey responses. Churn data with reason codes. Health-score telemetry per account.

### 8. Finance / ops
Chart of accounts. Sample invoices. P&L, balance sheet, cash flow. Subscription/billing data with cohort breakdowns. AR aging. Vendor contracts. Procurement records. Budget vs. actuals. Forecasts. Scenario models.

### 9. Compliance / legal / risk
MSA, DPA, NDA, SOW templates with redlines. Privacy policy. ToS. Cookie disclosures. SOC 2 / ISO 27001 controls + evidence (synthetic audit artifacts). DPIAs. Data inventories. Sub-processor lists. Incident response plans. Breach drill records.

### 10. Data / BI
Production DB schema + multi-year seed data. Analytics warehouse (dim/fact tables). Dashboards (Metabase / Superset definitions). KPI definitions. Metric trees. ETL/dbt pipelines. Data dictionary. Lineage docs.

### 11. Security / IT
Asset inventory (devices, accounts, services). IAM / access control matrix. Synthetic security log samples (audit, auth, network). Phishing test results. Backup/DR runbooks. Tooling stack outputs (EDR, SIEM, vuln scanner).

### 12. Public / external
Press releases. Public statements. Career page. Glassdoor reviews (synthetic). Customer reviews on third-party sites. Public GitHub presence (open-source contributions, public repos under `pylon-dev`).

## Tier prioritization

Don't build everything at once. Three tiers, additive:

### Tier 0 — minimum viable substrate (target: 5 POCs, 1–2 weeks)

Just enough that ~70% of likely Bent Wire POCs become testable:

- Company identity + brand + named org chart of 15–25 personas
- 1 product line (Pylon itself) with PRD + roadmap + pricing page
- Ticket fixture set: 75–100 dev tickets covering epics → bugs across recent history
- 1 runnable codebase: small Python or TypeScript service that "is" Pylon's product, with tests, an OpenAPI spec, README, and a few months of commits + PRs + issues
- 5–10 B2B customer fixtures + 30 user personas
- 15 support ticket conversations
- A `seed.sql` populating a Postgres "production DB" matching the product's domain

### Tier 1 — most POCs become possible (additive 2–3 weeks)

- Live marketing site (Astro static, deployed)
- CRM-shaped data: leads, deals, accounts, won/lost reasons
- Knowledge base (~30 articles)
- 6 months of synthetic Slack history
- BI warehouse schema + Metabase dashboards
- 20 blog posts in marketing archive
- A second codebase (frontend or mobile)
- Postmortems + ADRs

### Tier 2 — full-fidelity organic (build as POCs demand)

- Finance statements, payroll, invoices
- Compliance artifacts (SOC 2 evidence, etc.)
- Full HR pipeline data
- 12+ months time-series of operational data
- Live demo apps with running mock services
- Phishing / security log samples
- Synthetic call recordings
- **Pylon as its own Paperclip company** — autonomous Pylon-CEO, Pylon-PM, Pylon-Marketing agents producing ongoing fictional activity. Only worth doing once Bent Wire POCs need a moving target.

## Tier 0 POC breakdown

Each Tier 0 piece is a Bent Wire POC, intaken via Slack DM to Jude, run through the standard Market → Critic → POC plan flow. Each ships as an OSS release inside this repo + a Medium post.

### POC 1 — Identity, brand, and org

- Company name, tagline, mission, values
- Brand guidelines: logo (placeholder SVG OK), color palette, typography, voice/tone
- Org chart of 15–25 named personas with titles, departments, reports-to, work history
- README at this repo's root with the public-facing pitch
- Output files: `IDENTITY.md`, `BRAND.md`, `org/employees.json`, `org/chart.md`

### POC 2 — Product PRD + roadmap + pricing

- Full PRD for Pylon (the product): problem, audience, key features, edge cases, non-goals
- Roadmap: 4 quarters forward, with theme + bullets per quarter
- Pricing page (markdown): tiers, features per tier, FAQ
- Output files: `product/PRD.md`, `product/ROADMAP.md`, `product/pricing.md`, `product/competitive-analysis.md`

### POC 3 — Ticket fixture system

- 75–100 JIRA-shaped tickets covering 6 months of synthetic history
- Mix: 8–12 epics, ~40 stories, ~20 bugs, ~15 tasks, ~10 spikes
- Sprint structure: 12 sprints (2 weeks each)
- Realistic ticket bodies: acceptance criteria, screenshots placeholders, comments, link references
- Output: `tickets/*.json` (one file per ticket) + `tickets/sprints.json`
- Optional stretch: spin up [Plane](https://github.com/makeplane/plane) self-hosted and seed it from the JSON

### POC 4 — Codebase + PR/issue history

- Small but real Python/FastAPI service: Pylon's PR review API endpoint
- ~6 months of synthetic git history (rebased commits, no fake-looking dates)
- 30 sample PRs with realistic descriptions, review comments, approve/request-changes outcomes
- 50 GitHub-style issues with labels, assignees, comments
- Output: `codebases/api/` (full repo with own .git history) + `codebases/api/.github/`

### POC 5 — Customers, support, KB minimal

- 5–10 B2B customer fixtures (account profile, primary contact, plan tier, MRR, health score, usage signals)
- 30 user personas (devs working at those accounts)
- 15 multi-turn support conversations across email/chat
- 10 knowledge-base articles (varied: setup guides, troubleshooting, billing FAQ)
- Output: `customers/*.json`, `support/conversations/*.md`, `kb/articles/*.md`

After POC 5: Tier 0 is shippable. Cut a `v0.1.0` tag. Write the Medium post: *"Building Pylon — a synthetic B2B SaaS company for AI agent benchmarks."*

## Architecture — three layers

1. **Source of truth: this git repo.** Everything human-readable: markdown, JSON, SQL, YAML. Reviewable, diff-able, OSS-able.
2. **Realized as runnable services.** A `Makefile` target (`make up`) spins up Docker containers seeded from this repo: Postgres + seed.sql, Plane (mock JIRA), Gitea (mock GitHub), Mailpit (mock email), Mattermost (Slack-compatible chat), Metabase (BI), Astro (the marketing site). POCs hit *real endpoints*, not static fixtures.
3. **Versioned snapshots.** Tagged releases per major change so a POC can pin to "Pylon v0.4" for reproducibility.

This three-layer design is critical: static fixtures teach AI tools different lessons than live, stateful APIs. We want the higher-fidelity signal.

## Relationship to Bent Wire Studio

| | Bent Wire Studio | Pylon LLC |
|---|---|---|
| What | The AI-experimentation studio | The synthetic B2B SaaS testbed |
| Repo | [`kade-clawborn/bentwire`](https://github.com/kade-clawborn/bentwire) | this repo (`kade-clawborn/pylon`) |
| Paperclip company ID | `cffe8772-545c-427d-8b96-561109c8343e` | none initially; possibly its own company at Tier 2 |
| Agents | CEO, IntakeLead, ResearchLead, EngineeringLead, MarketAnalyst, Critic, PrototypeEngineer, TestEngineer, CommsLead, TechScout, CommunityScout | none initially; Bent Wire's agents produce all Pylon artifacts |
| Public output | Open-source POCs + Medium/LinkedIn posts | Pylon itself (this repo) is the publish artifact |
| Mission | Grow Justin's AI fluency by shipping prototypes + content | Be the credible benchmark substrate every AI agent project tests against |

**The flow:** Bent Wire's IntakeLead receives a Slack DM with a Pylon-relevant idea (e.g., "build POC 1: Pylon identity"). Standard Bent Wire intake → spec → Market + Critic + Engineering. Engineering's pair-loop produces files in *this* repo on a `poc/<slug>` branch. Ready signal → CommsLead drafts release → CEO publishes. Each POC's output adds to Pylon.

## Conventions and guardrails

### Realism over completeness
The first 100 tickets should feel real (varied, messy, with realistic context windows). Don't try to ship 10,000 templated tickets. AI tools will detect templates instantly.

### Naming
- People: realistic but fictional names. Vary nationality, gender, seniority. Don't lean on "Alice & Bob."
- Companies (Pylon's customers): plausible mid-market names. Avoid Fortune-500 collisions.
- Products: Pylon's own product is also called Pylon. Subsystems get distinct names (Beacon for the lint engine, Tower for the analytics layer, etc.)
- Code: idiomatic for the chosen language; no AI-tells (no "shimmering," no "quantum," no "cutting-edge").

### Branch strategy in this repo
- `main` — Tier 0/1/2 stable releases tagged here
- `poc/<slug>` — active POC work; merges to `main` at ready-signal
- Each POC's commits live on its own branch until released

### Commit conventions
- Pylon-product code: standard conventional commits (`feat`, `fix`, `refactor`, `test`, `chore`, `docs`)
- Pylon-fixture work: prefix with the layer (`org:`, `product:`, `tickets:`, `codebases:`, `support:`, etc.)

### File format conventions
- Markdown for human-readable docs (PRDs, blog posts, KB articles)
- JSON for structured fixtures (tickets, customers, employees, deals)
- SQL for DB schemas + seeds
- YAML for configs (CI, docker-compose)
- Avoid binary blobs in source; reference public placeholders if needed

### What lives here vs. elsewhere
- This repo: source-of-truth fixtures, codebases, runnable spin-up
- The product's *own* git history: lives inside `codebases/<service>/.git/` (subrepos have their own histories)
- Bent Wire's POC build process: lives in [`kade-clawborn/bentwire-playground`](https://github.com/kade-clawborn/bentwire-playground), not here
- Bent Wire's agent definitions: live in `~/.paperclip/instances/default/companies/cffe8772-.../agents/`, not here

## Open questions (decide as we build)

1. **Should Pylon's product subsystems have separate codebases?** (i.e., separate `codebases/` subdirs for Beacon, Tower, etc.) — defer until Tier 1.
2. **What CI provider does Pylon "use"?** Affects the synthetic CI configs. Suggest GitHub Actions.
3. **Does Pylon use Slack or Mattermost for internal chat?** Affects the synthetic chat history schema. Suggest Slack-compatible since most AI POCs target Slack APIs.
4. **Real money in customer fixtures or notional?** Suggest notional rounded numbers ($840 MRR, not $873.42) — easier to reason about, less likely to confuse downstream POCs.
5. **Pylon-specific slash commands** in `.claude/commands/pylon/`? Likely useful for fixture management (`/pylon-fixture-add`, `/pylon-snapshot`). Add as POCs reveal need.
6. **Does Pylon have its own Paperclip company eventually?** Likely yes at Tier 2 — see "Tier 2" above. Plan but don't build yet.
7. **Subdomain structure**: `pylon.dev` for product, `pylon.dev/blog`, `pylon.dev/docs`, `pylon.dev/careers`? Define when marketing site lands in Tier 1.

## What the next agent does first

If you're a Bent Wire agent picking up Pylon work, the first concrete actions are:

1. Read this `BLUEPRINT.md` end to end (you're doing this now).
2. Read `CLAUDE.md` for working-directory conventions.
3. Confirm which Tier 0 POC you're working on (POC 1–5 above). Your assignment description in Paperclip should name it.
4. Branch off `main` as `poc/<slug>`.
5. Read the relevant `.claude/commands/context-os/*.md` slash commands (copied from Bent Wire's spec-driven-design tooling) — `shape-spec`, `write-spec`, `create-tasks` are the most relevant for adding Pylon fixtures.
6. Output your POC's artifacts under the right layer (`org/`, `product/`, `tickets/`, `codebases/`, `customers/`, `support/`, `kb/`).
7. When done, signal Bent Wire's CommsLead to draft a release post.

If you're a human picking this up: same steps, minus the Paperclip integration.

## License

Apache 2.0 (matches Bent Wire's OSS posture). All synthetic data and code published here is free to use for AI tooling research and benchmarking.

---

*Last updated: 2026-04-25. Created during initial Pylon scaffolding by Bent Wire Studio.*
