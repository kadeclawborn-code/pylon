# Pylon — Identity

> Canonical fictional identity for Pylon LLC. Cite this file when generating any Pylon artifact. If a future POC contradicts a fact here, update IDENTITY.md first, then the POC — never the other way around.

## Company

| | |
|---|---|
| Legal name | Pylon, LLC |
| Trading name | Pylon |
| Domain | pylon.dev |
| Incorporated | March 2021, Delaware |
| Stage | Series B (closed Q3 2024) |
| Funding raised | $35M total ($3M seed, $11M Series A, $21M Series B) |
| Lead investors | Index Ventures (Series B), Felicis (Series A), South Park Commons (seed) |
| Headcount | 71 (as of Q1 2026) |
| Headquarters | Remote-first; legal address in Wilmington, DE |
| US-only | Yes (no international offices, no international employees, no international customers as of Q1 2026) |
| Org type | Privately held LLC |

## Mission

Stop merging surprises. Pylon catches what review missed.

## What Pylon does

Pylon is a developer-focused **PR review automation platform**. It plugs into GitHub, GitLab, and Bitbucket Cloud. On every pull request it runs a configurable battery of checks — lint rules, security scans, architectural-drift detectors, dependency analysis, test-coverage diffs — and surfaces the highest-leverage findings as in-line PR comments. Engineering managers get aggregate dashboards showing review quality, cycle time, and where humans repeatedly miss the same class of bug.

The pitch is plain: code review catches what reviewers happen to look at. Pylon catches what reviewers don't.

## Product surface

Pylon-the-product has three named subsystems:

- **Beacon** — the static-analysis and lint engine. Owns the rule library, customer-rule-config compiler, and the per-language analyzers. Written in Python with a Rust core for the AST traversal.
- **Tower** — the analytics layer. Aggregates review data into team metrics, cycle-time charts, hotspot maps, and the "who reviews what" graph. ClickHouse-backed.
- **Switchyard** — the integration layer. Webhooks from GitHub/GitLab/Bitbucket, the comment poster, the merge-block enforcer, and the auth/identity bridge.

Customers see one product (Pylon). The three subsystem names appear in internal docs, codebases, ticket components, and the careers page.

## Pricing

| Plan | Price | Limit | Includes |
|---|---|---|---|
| Free | $0 | Up to 5 active devs, public repos only | Beacon (default rule pack), basic Tower (cycle time only) |
| Team | $29/dev/mo | Unlimited devs, private repos | All Beacon rules, full Tower, Slack/email digests |
| Business | $59/dev/mo | Same as Team | + Custom rules, SAML SSO, audit logs, priority support |
| Enterprise | Custom | Same as Business | + SOC 2 Type II evidence portal, on-prem option, dedicated CSM, contractual SLAs |

Customer count: ~250 paying accounts. ARR: ~$8.4M (NTM ~$11.5M). Net revenue retention: 121%. Gross margin: 78%.

## Tech stack

- **Backend (monolith):** Python 3.12, FastAPI, SQLAlchemy, Pydantic v2
- **Frontend:** TypeScript, React 19, Vite, TanStack Query, Tailwind
- **Mobile:** No mobile app (desktop-only product, by design)
- **Datastores:** Postgres 16 (primary OLTP), Redis (cache + queues), ClickHouse 24 (Tower analytics), S3 (artifact storage)
- **Infra:** AWS us-east-1, Cloudflare edge for the webhook ingress and marketing site, GitHub Actions for CI, Terraform for IaC
- **Observability:** Datadog (APM + logs), Sentry (errors), Grafana for the customer-facing analytics dashboards
- **Auth:** Auth.js for the dashboard, GitHub App tokens for repo access, SAML for Business+ tier

The Rust core inside Beacon is a deliberate, contained dependency — it sits behind a Python FFI binding the team carefully avoids exposing. Rust expertise on the team is concentrated in two engineers; rest of the team treats it as a black box.

## Customers (in canon)

Pylon serves engineering teams of 10–500 engineers. The strong fit is Series A through Series C software companies who already use GitHub or GitLab Cloud. The weak fit is enterprises with self-hosted Bitbucket Server (Pylon doesn't support it), ML/AI teams (Pylon's model-training-code rules are weak), and very early-stage companies (the rule complexity isn't worth it under 10 engineers).

Five flagship customer logos appear on pylon.dev/customers (all fictional, named in POC 5):
- Stratosphere Robotics
- Lumen Health
- Kaltsworth Logistics
- Verdant Energy
- Arcola Studios

## Competitors and positioning

Direct competitors:
- **GitHub Copilot Enterprise (PR review feature)** — bundled, harder to displace; weakness: shallow custom-rule story
- **Reviewable** — focuses on workflow, weak on automation
- **CodeScene** — strong on hotspot analysis, weak on lint

Pylon's positioning: "Custom rules that actually work, plus the analytics to prove they did." The Beacon custom-rule system is the defensible moat — competitors either don't expose rule customization at all, or expose it through clunky DSLs.

Adjacent (not direct) competitors: SonarQube, DeepSource, Snyk, Semgrep. Pylon is friendlier on developer experience but narrower on language coverage (no Java, no C#, no PHP — those are tracked as 2026 H2 roadmap items).

## Operating principles

These are referenced in internal docs, all-hands talks, and recruiting collateral. They're not a vibe; the team uses them as decision filters.

1. **Default to the engineer's perspective.** Pylon is built by engineers for engineers. Every UI, ticket, error message, and pricing decision should respect the reader's time and intelligence.
2. **Customizability over opinion.** Beacon ships with strong defaults but always exposes the knob. The thing you ship and turn on is rarely the thing the customer ships and turns on.
3. **Honest signal beats polished noise.** A failing test that finds a real bug is better than a passing one that doesn't. Same with PR comments.
4. **Ship narrow. Stay narrow until you can't.** No expansion into review *workflow* (assignment routing, etc.). No expansion into general-purpose CI. No expansion into IDE plugins. The narrowness is the strategy.
5. **Treat reviewer time as the scarcest resource.** Every false positive is a tax on the only humans who can catch the real ones.

## History (year-by-year)

- **2021** — Founded by Marcus Chen and Priya Subramanian. Both engineers. Open-sourced the lint engine prototype on Marcus's personal GitHub; received unexpected pull from a few well-known companies. Closed the $3M seed in Q4 2021.
- **2022** — Built the SaaS wrapper. First paying customer (Stratosphere Robotics) signed in Q2 for $400/mo. Hit $50k ARR by year-end. Hired the first 6 employees, all engineers.
- **2023** — Series A ($11M, Felicis lead). Hired CRO (Daniel Park) and CPO (Olivia Reyes). First non-engineering org (Customer Success). Hit $2M ARR by end of 2023.
- **2024** — Pricing redesign moved Pylon from per-account to per-dev pricing, doubled NRR. Series B closed Q3 2024. Hit $6M ARR end of 2024.
- **2025** — Built Tower (analytics). Built Switchyard out as a real platform component (it had been a single Python service). Crossed 200 paying accounts.
- **2026** — Current. Cross-platform expansion (GitLab + Bitbucket Cloud) shipped Q1. Q2 focus: Beacon rule-marketplace, Switchyard for self-hosted GitLab Enterprise, SOC 2 Type II completion.

## Public footprint

- Domain: pylon.dev (marketing), app.pylon.dev (dashboard)
- GitHub: github.com/pylon-dev (Pylon-the-company's public org; some open-source artifacts including the Beacon rule library)
- Twitter/X: @pylondev
- LinkedIn: /company/pylon-dev
- Status page: status.pylon.dev (StatusPage-hosted)
- Docs: pylon.dev/docs
- Blog: pylon.dev/blog
- Careers: pylon.dev/careers

## What Pylon explicitly does *not* do

These come up in sales conversations and in customer asks. The answer is no, with rationale.

- **No IDE plugin.** Reviewing in the editor is a different product. Stay narrow.
- **No general CI replacement.** Pylon is *one stage* of CI, not the whole thing.
- **No PR-assignment routing.** Adjacent product, would dilute the focus.
- **No AI-generated fixes (yet).** Scoped for late 2026 once Beacon rule semantics are stable enough that fix-suggestion is grounded.
- **No on-prem for Team/Business tiers.** Enterprise only.
- **No Bitbucket Server (self-hosted).** Cloud only.
- **No support for ML notebooks.** The reviewable artifact for ML is unclear.

## Compliance posture

- SOC 2 Type I completed Q4 2024.
- SOC 2 Type II in flight, target Q3 2026.
- GDPR-compliant (US-only customers but some have EU users).
- Data residency: US-only (no EU region as of Q1 2026; on roadmap).
- DPAs available for Business+ tier customers on request.
- Annual penetration test by an external firm (next: Q3 2026).

## Cultural shorthand

A few phrases that appear in internal docs and Slack and that newcomers pick up:

- **"The signal-to-noise tax"** — Pylon's framing for false positives. Used as a verb: *"We're paying signal-to-noise tax on this rule."*
- **"Beacon-shaped problem"** — Anything that looks like a static-analysis fit. Used loosely.
- **"Tower-shaped problem"** — Anything that requires aggregation across PRs/teams over time.
- **"Switchyard-shaped problem"** — Anything that's about the integration with the host VCS.
- **"Narrow door"** — Decision rule: when in doubt, choose the option that keeps Pylon narrower.
- **"Reviewer's bargain"** — The implicit deal: Pylon will only flag things that are worth a reviewer's time.

These are referenced casually in tickets, PR comments, all-hands talks, and (rarely) in customer-facing content.
