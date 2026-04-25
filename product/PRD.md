# Pylon — Master PRD

| | |
|---|---|
| Document | Master Product Requirements Document |
| Version | 1.0 |
| Status | Active (canonical baseline) |
| Owner | Olivia Reyes (CPO) |
| Last reviewed | 2026-04-25 |
| Reviewed by | Marcus Chen (CEO), Priya Subramanian (CTO), Anika Bhattacharya (VP Product) |

> The Master PRD is the single source of truth for what Pylon is. Feature-level PRDs (in `product/features/<slug>.md`) extend this document but cannot contradict it. If a feature requires changing a Master PRD claim, update the Master first via the Master PRD change process (see end).

## Executive summary

Pylon is a developer-focused PR review automation platform. It plugs into GitHub, GitLab, and Bitbucket Cloud, runs a configurable battery of checks on every pull request, and surfaces high-leverage findings as in-line PR comments and team-level dashboards. It is sold to engineering organizations of 10–500 engineers.

The product exists because human code review catches what reviewers happen to look at. Pylon's job is to catch what reviewers don't — without burying them in noise.

## Problem statement

Engineering teams at Series A through Series C software companies face a recurring set of PR-review failures:

1. **Reviewers miss the same bug class repeatedly.** The team learns about a regression in production, retros it, identifies the missed pattern, and a quarter later the same pattern slips through review again. Human attention doesn't index well across hundreds of PRs.
2. **Review quality varies wildly across the team.** Some senior engineers leave thirty in-line comments on a PR; others approve in 90 seconds. The team has no shared signal for whether a PR was actually reviewed or rubber-stamped.
3. **Linters and static analyzers are either too quiet or too loud.** Off-the-shelf rules generate either no findings or thousands of pedantic ones. Teams turn the tools off.
4. **No common language exists for review-process metrics.** Engineering managers can't say "are we getting better at review?" with any rigor. They have throughput numbers but not quality signals.
5. **Custom rules are aspirational.** Every linter promises customization; almost no team actually ships custom rules because the DSLs are clunky and the iteration loop is too slow.

Pylon addresses all five. The first three with the **Beacon** subsystem (rule engine + smart defaults + custom rules that don't suck), the fourth with **Tower** (review analytics), the fifth with Beacon's authoring experience and rule marketplace.

## Audience

### Buyers

| Role | Title pattern | Lives at | Cares about |
|---|---|---|---|
| **Primary buyer** | VP Engineering, Director of Platform, sometimes CTO | 50–500 person eng orgs | Reducing escaped bugs, improving review consistency, defensible engineering investments to leadership |
| **Secondary buyer** | Eng Manager, Tech Lead | Same orgs | Whether the tool helps their team specifically; whether the false-positive rate is tolerable |

### Daily users

| Role | Title pattern | Cares about |
|---|---|---|
| **PR author** | Any engineer opening a PR | Pylon comments are accurate, actionable, and not condescending |
| **PR reviewer** | Senior/Staff/Principal engineers; tech leads | Pylon flags the right things, never blocks merges over taste, plays well with the human review |
| **Rule author** | One or two engineers per team who write custom rules | The Beacon rule API is ergonomic, debuggable, and fast to iterate on |
| **Eng manager / dashboard reader** | Eng managers, directors, VPs | Tower's metrics tell a defensible story about review health |

### Anti-personas (we are explicitly not for)

- **Solo developers and ≤5-engineer teams** — review process at that scale doesn't need automation; the rule complexity isn't worth it
- **Self-hosted Bitbucket Server users** — Cloud only, by deliberate scope choice
- **ML/AI training-code teams** — the reviewable artifact for ML notebooks is unclear; Pylon's rules don't fit
- **Consultancies / large agencies** — different review workflow needs (per-client policy, contractor mix); not Pylon's wedge

## Goals

1. **Findings density** — On a typical PR (median 200 lines changed, 4 files), Pylon surfaces 0–3 useful comments with a false-positive rate ≤8%. ("Useful" defined as: the PR author or a reviewer would also have flagged this if they'd noticed it.)
2. **Time-to-value** — A new customer can install Pylon, point it at their default branch, and start receiving useful comments on their next PR within 15 minutes of setup. No bespoke integration work.
3. **Custom rule velocity** — Once a team identifies a pattern they want to catch, an experienced rule author can write, test, and deploy a custom Beacon rule in under 2 hours of focused work.
4. **Tower truth** — Tower's review-quality metrics are accurate enough that an engineering leader can use them in a board conversation without hedging. Calibrated, not just available.
5. **Platform breadth** — GitHub Cloud (full), GitLab Cloud (full), Bitbucket Cloud (full). GitLab self-hosted is a 2026 stretch goal; Bitbucket Server is explicit non-goal.

## Non-goals (what Pylon will not do)

These are **explicit, durable** non-goals. Each comes up in customer conversations regularly. The answer is no, with rationale.

- **No IDE plugin.** Reviewing in the editor is a different product (a real-time linter, in effect). Pylon's wedge is the PR moment. An IDE plugin would dilute focus and would compete with much better-resourced incumbents (vendors of language servers).
- **No general CI replacement.** Pylon is one stage of CI. It is not your test runner, your build system, your container builder, or your deploy gate. Tight integration with existing CI (status checks, PR-blocking) is in scope; replacing CI is not.
- **No PR-assignment routing.** Adjacent product (who reviews which PR). Different mental model. Different sales motion. Risk of becoming "review-stuff platform" — which is exactly the not-narrow-anymore failure mode we avoid.
- **No AI-generated fixes (yet).** This is on the roadmap for late 2026, gated behind enough rule-semantics work that a fix-suggestion is grounded. Premature shipping here would burn the brand.
- **No on-prem for Free, Team, or Business tiers.** Enterprise only.
- **No Bitbucket Server (self-hosted).** Cloud only. The integration cost vs. customer count doesn't pencil.
- **No support for ML notebooks (.ipynb).** Reviewable artifact is unclear; rule semantics on cell-by-cell changes are weak.
- **No general-purpose code-quality scoring**. We don't generate "code quality scores." That framing is misleading and we won't ship it.

## System overview

Pylon comprises three named subsystems plus the customer-facing surfaces.

### Beacon — the rule engine

The static-analysis layer. Owns:
- The default rule library (~300 rules across Python, TypeScript, Go, JavaScript, Ruby — language coverage detail in `product/features/language-coverage.md`)
- The custom rule API + DSL (Pylon Rule Language, "PRL" — based on tree-sitter queries with declarative match patterns)
- The per-language analyzers (built on tree-sitter; the Rust core is a Beacon component, not a separate subsystem)
- The rule-config compiler (turns customer's `pylon.yaml` into the runtime rule set)
- The findings filter (deduplication, severity ranking, suppress-by-comment annotation handling)

### Tower — the analytics layer

The review-quality metrics layer. Owns:
- The review-event ingestion pipeline (every PR comment, approval, request-changes, merge, revert)
- The aggregation jobs (cycle time, review distribution, hotspot maps, "who reviews what" graphs)
- The dashboards customers see in app.pylon.dev/dashboards
- The KPI library (defines the canonical metrics; customers can derive their own from Tower's data API)
- The Slack/email digest scheduler

### Switchyard — the integration layer

The host-VCS bridge. Owns:
- Webhook ingress (GitHub Apps, GitLab integrations, Bitbucket Cloud connect)
- The comment poster (writes Pylon's findings as PR review comments)
- The merge-block enforcer (Pylon-as-required-status-check)
- The auth/identity bridge (GitHub user → Pylon user → customer team membership)
- Per-customer secrets management (their VCS tokens, never our problem to leak)

### Customer-facing surfaces

- **Dashboard** (app.pylon.dev) — TanStack-Query React app. Where customers configure rules, view findings, browse Tower analytics, manage billing.
- **Marketing site** (pylon.dev) — Astro static. Pricing, docs, blog, customer stories.
- **Docs** (pylon.dev/docs) — versioned by release.
- **Status** (status.pylon.dev) — StatusPage-hosted.
- **Public GitHub** (github.com/pylon-dev) — open-source rule library mirrors, customer-facing examples.

## Key user journeys

### J1 — New customer onboards (≤15 minutes)

1. Eng manager visits pylon.dev, signs up with GitHub OAuth.
2. Pylon redirects to GitHub App install; eng manager grants Pylon read access to selected repos.
3. Pylon ingests the first 30 days of PR history per repo (Switchyard) and runs Beacon's default ruleset against the most recent 50 PRs to surface "what we'd have caught" examples.
4. Tower spins up a starter dashboard with 14 days of historical cycle-time data inferred from the PR ingest.
5. Pylon installs a `pylon.yaml` in the repo via PR (using a starter ruleset matched to the detected languages). The eng manager merges it.
6. The next PR opened against the repo gets Pylon comments. End-to-end: ≤15 minutes from signup to first comment.

### J2 — Reviewer encounters a Pylon comment

1. Reviewer opens a teammate's PR. Pylon has left two in-line comments and one summary comment.
2. The summary comment links to the Beacon rule that fired and the rule's docs page.
3. Reviewer can:
   - **Acknowledge** — leave the comment in place
   - **Dismiss** with reason (false positive, won't fix, won't fix here, deferred) — feeds back into Beacon's calibration
   - **Suppress on this line** — adds a `# pylon: suppress(rule-id) — <reason>` annotation to the source file
4. Pylon's comments are styled to be visually distinct from human reviewer comments (subtle Pylon Blue accent) so a reviewer can scan past them when not relevant.

### J3 — Engineer authors a custom rule

1. Engineer opens the Pylon dashboard, navigates to Rules → Author.
2. Writes a Beacon rule in PRL — declarative match pattern (tree-sitter query), severity, message template, optional auto-suggest fix scaffold.
3. Tests the rule against historical PRs from their own repo (Pylon Dashboard provides a "preview" mode that shows what the rule would have flagged on the last 200 PRs).
4. Iterates. Drops the rule into a "shadow mode" for a week (rule fires but doesn't post comments; results visible in Tower).
5. Promotes to production. Optionally publishes to Pylon's rule marketplace for other customers to use.

### J4 — Engineering manager reads Tower

1. Eng manager opens Tower dashboard for their team.
2. Sees:
   - Median PR cycle time (ribbon chart, 90 days)
   - Distribution of review depth (binned: rubber-stamp, light review, thorough review)
   - Hotspot file map (files where Pylon comments cluster + files where post-merge bugs traced back to)
   - "Who reviews what" graph
3. Drills in: clicks a hotspot file, sees the last 30 days of PRs that touched it, with Pylon-comment density per PR.
4. Exports a snapshot for a leadership review.

### J5 — Customer hits a Beacon rule that fires too often

1. Eng manager sees in Tower that rule `python.bare-except` is firing on 18% of PRs and being dismissed >70% of the time.
2. Opens the rule in Beacon, reads the dismissal reasons, decides the rule needs to be scoped to certain paths.
3. Edits the rule config in `pylon.yaml` (excludes test files), commits.
4. Pylon's CI integration validates the rule change in the PR. Pylon merges it. Findings drop accordingly.

## Architecture overview

(High-level only. Full architecture detail lives in `codebases/api/docs/architecture/` once that subrepo lands in POC 4.)

```
                   ┌─────────────────────────────────┐
                   │        Customer's GitHub        │
                   │    (or GitLab, Bitbucket)       │
                   └─────────────┬───────────────────┘
                                 │ webhooks
                                 ▼
                    ┌────────────────────────────┐
                    │       Switchyard           │
                    │  (Cloudflare Worker edge)  │
                    └─────┬──────────┬───────────┘
                          │          │
              PR ingest   │          │ comment poster
                          ▼          ▼
   ┌─────────────────────────┐ ┌──────────────────────┐
   │       Beacon            │ │   Customer's PR UI   │
   │  (Python + Rust core,   │ │ (comments rendered)  │
   │  AWS us-east-1)         │ └──────────────────────┘
   └────────────┬────────────┘
                │ findings
                ▼
   ┌─────────────────────────┐         ┌─────────────────────┐
   │       Tower             │ ◀────── │   Customer Dashboard│
   │ (ClickHouse + dbt)      │         │  (TanStack/React)   │
   └─────────────────────────┘         └─────────────────────┘
                ▲
                │
       ┌────────┴───────┐
       │  Postgres      │
       │  (OLTP, AWS)   │
       └────────────────┘
```

**Stateful boundaries:**
- Postgres: customer accounts, billing, rule configs, suppression annotations
- ClickHouse: review events, findings history, all Tower aggregation source data
- Redis: hot path caches (rule compilation cache, GitHub API rate-limit budget cache)
- S3: rule bundles, large finding artifacts (e.g., diffs > 1MB)

## Success metrics

These are tracked as KPIs across product, eng, and revenue. Each has a current value and a 12-month target.

| Metric | Current (Q1 2026) | 12-month target |
|---|---|---|
| Useful-comment rate (per PR median) | 1.6 | ≥2.0 |
| False-positive rate (dismissed-as-FP / total findings) | 11% | ≤8% |
| Time-to-first-comment (signup → first PR comment) | 22 min | ≤15 min |
| Custom rules authored per customer (median, after 90 days) | 1.4 | ≥3.0 |
| Tower DAU / total customer eng managers | 38% | ≥55% |
| Net Promoter Score | 41 | ≥50 |
| Net Revenue Retention | 121% | ≥120% (hold) |
| Gross margin | 78% | ≥80% |

## Open questions (with named owners)

These are durable open questions tracked in this document because they affect product strategy and aren't yet resolved.

| # | Question | Owner | Target decision |
|---|---|---|---|
| OQ-1 | Should Beacon expose a Python API (in addition to PRL DSL) for rule authoring? | Wei Chen | Q3 2026 |
| OQ-2 | Tower data export: REST API, GraphQL, or push-only via webhook? | Camille Dubois | Q2 2026 |
| OQ-3 | Should Pylon support GitLab self-hosted (Enterprise) given customer demand? | Olivia Reyes | Q4 2026 |
| OQ-4 | When does AI-suggested-fix become trustworthy enough to ship beyond gated beta? | Wei Chen / Priya Subramanian | Late 2026 |
| OQ-5 | Should we expand language coverage by acquisition (buying an existing analyzer for Java/C#) or by hiring? | Marcus Chen | Q3 2026 |
| OQ-6 | Pricing: do we keep per-dev or move to consumption-based for Enterprise? | Daniel Park / Amir Hosseini | Q1 2027 |

## Master PRD change process

This document changes deliberately. To propose a change:

1. Open a PR against the `product/` directory in this repo with the change.
2. Tag CPO (Olivia) and CTO (Priya) for review.
3. Get explicit sign-off from CEO if the change touches a non-goal (the explicit "we don't do X" list).
4. Update the `Last reviewed` date and `Version` (bump minor for additions, major for non-goal changes).
5. Cascade affected feature PRDs.

The non-goals list is the most expensive part of the document to change — those statements get repeated in sales calls, internal docs, and partner conversations. Treat them as load-bearing.

## References

- `IDENTITY.md` — Pylon's company-level identity (legal, funding, history, public footprint)
- `BRAND.md` — Voice, tone, banned phrases, visual identity
- `org/employees.json` — Personas referenced in this PRD (Olivia, Priya, Marcus, Anika, Wei, Camille)
- `product/ROADMAP.md` — Forward-looking quarterly plan
- `product/pricing.md` — Public pricing page content
- `product/competitive-analysis.md` — Where Pylon sits vs. direct + adjacent competitors
- (Future) `product/features/<slug>.md` — Feature-level PRDs derived from this Master
- (Future) `codebases/api/docs/architecture/` — Detailed system architecture
