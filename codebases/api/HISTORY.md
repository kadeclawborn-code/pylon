# Synthetic git history — pylon-api

> This document captures the synthetic 6-month commit history for the `pylon-api` subrepo as a readable artifact. It lets AI agents reasoning about the codebase examine commits without needing a real `.git/` directory committed into the parent `pylon` repo. To recreate a navigable git repo from this log, run `bash scripts/init-history.sh` (forthcoming POC).
>
> Authors are real Pylon employees (see `org/employees.json`). Dates respect Pylon's "no Friday merges" policy. Commit messages follow Conventional Commits.

## Branches in this snapshot

- `main` — current head, version 2.4.2 (PR #84 merged 2026-04-23)
- `release/2.5` — does not exist yet; SOC 2 evidence integration starts in S15
- `pre-2025-q4` — archived; predates the 6-month window in this fixture

## Commits, newest → oldest

```
* commit f8a4d2c (HEAD -> main, tag: v2.4.2)
| Author: Ravi Mehta <ravi@pylon.dev>
| Date:   2026-04-23 14:17:00 -0700
|
|     fix(switchyard): auto-rotate GitHub App signing key via JWKS endpoint
|
|     Hardcoded webhook signing key caused a 90-minute production incident
|     on 2026-04-22 when GitHub rotated the key per their 90-day policy.
|     This change fetches the current key set from GitHub's JWKS endpoint
|     on a 12h refresh cycle and falls back to the cached key on transient
|     fetch failures.
|
|     Refs: PYL-306
*
* commit 9f3a1e8 (origin/main)
| Author: Hugo Lefèvre <hugo@pylon.dev>
| Date:   2026-04-23 11:02:00 +0200
|
|     test(rules): add 7 more async-correctness rules to PYL-104 corpus
|
|     Refs: PYL-223
*
* commit b8e7c91
| Author: Tomás Herrera <tomas@pylon.dev>
| Date:   2026-04-22 15:33:00 -0300
|
|     feat(switchyard): GitLab MR comment idempotency layer (PYL-305 fix)
|
|     Verdant Energy pilot reported duplicate Pylon comments on MR retry.
|     Root cause: GitLab Notes API doesn't have GitHub Reviews' built-in
|     idempotency; we now fetch existing notes and dedupe by stable hash
|     (rule_id + file + line + commit_sha) before posting.
|
|     Refs: PYL-305
*
* commit 4d2f1ab
| Author: Wei Chen <wei@pylon.dev>
| Date:   2026-04-19 10:55:00 -0700
|
|     docs(suggest): risk register draft for Pylon Suggest gated beta
|
|     First draft of the risk register that gates entry to gated-beta. To
|     be reviewed by Olivia, Marcus, Priya before locking entry criteria.
|
|     Refs: PYL-105
*
* commit 7e6b5d3
| Author: Hugo Lefèvre <hugo@pylon.dev>
| Date:   2026-04-15 14:21:00 +0200
|
|     feat(rules): promote first 10 async rules to default-on (PYL-222)
|
|     Shadow-mode FP rate: 6.4%. Below the 8% threshold. Promoting.
|
|     Refs: PYL-104, PYL-222
*
* commit 2c9e8a5 (tag: v2.4.1)
| Author: Felix Chen <felix@pylon.dev>
| Date:   2026-04-09 13:00:00 -0400
|
|     fix(dashboard): marketplace publishing form description field on Safari
|
|     Refs: PYL-304
*
* commit 6a3d0f1
| Author: Jordan Mwangi <jordan@pylon.dev>
| Date:   2026-04-11 14:00:00 -0400
|
|     feat(switchyard): GitLab merge-block enforcer
|
|     Pylon registered as required status check on GitLab MRs. Customer-
|     configurable: required vs informational. Status updates based on
|     analyzer findings + customer's threshold config. Override events
|     now logged in audit_log per PYL-103 reviewer feedback.
|
|     Refs: PYL-210
*
* commit 5b1e2a7
| Author: Camille Dubois <camille@pylon.dev>
| Date:   2026-04-10 15:30:00 -0400
|
|     feat(tower): team comparison dashboard UI
|
|     Side-by-side dashboard for 2-4 teams. Three charts (cycle time,
|     review depth, hotspot density) color-coded per team. Absolute /
|     relative-delta toggle. Export PNG, PDF.
|
|     Refs: PYL-214
*
* commit 7c4e9f0 (tag: v2.4.0)
| Merge: 8d3e2b1 9a7c4d6
| Author: Marcus Chen <marcus@pylon.dev>
| Date:   2026-03-29 21:10:00 -0400
|
|     Merge pull request #62 from feat/marketplace-public-preview
|
|     Beacon Rule Marketplace (PYL-100) — public preview launch
|
| * commit 9a7c4d6
| | Author: Tomás Herrera <tomas@pylon.dev>
| | Date:   2026-03-27 17:00:00 -0300
| |
| |     feat(dashboard): marketplace browse UI (PYL-204)
| *
| * commit 4f8b3c2
| | Author: Hugo Lefèvre <hugo@pylon.dev>
| | Date:   2026-03-13 14:20:00 +0100
| |
| |     feat(beacon): rule version semver auto-update behavior (PYL-203)
| *
| * commit 2e9a1d8
| | Author: Tomás Herrera <tomas@pylon.dev>
| | Date:   2026-02-27 15:10:00 -0300
| |
| |     feat(dashboard): marketplace rule subscription flow (PYL-202)
| *
| * commit 8c3e0f4
| | Author: Felix Chen <felix@pylon.dev>
| | Date:   2026-03-01 16:45:00 -0400
| |
| |     feat(dashboard): marketplace rule publishing UX (PYL-201)
| *
| * commit 1d6a8b3
|  Author: Hugo Lefèvre <hugo@pylon.dev>
|  Date:   2026-01-16 17:30:00 +0100
|
|     feat(beacon): marketplace data model + Postgres schema (PYL-200)
|
|     marketplace_rules, marketplace_rule_versions, marketplace_subscriptions
|     tables. Semver enforcement at schema level. Indexes on common queries.
*
* commit 8d3e2b1
| Author: Lila Reeves <lila@pylon.dev>
| Date:   2026-03-29 22:30:00 -0400
|
|     docs(blog): Marketplace public preview launch post (PYL-205)
*
* commit 3a7f0d2 (tag: v2.3.0)
| Author: Camille Dubois <camille@pylon.dev>
| Date:   2026-03-12 17:20:00 -0400
|
|     feat(dashboard): audit log GA — Business tier (PYL-103)
|
|     Closes audit logs epic. Retention enforced (1y Business / 7y Enterprise),
|     export pipeline production-ready, SOC 2 evidence query API stub
|     scaffolded for Q3 audit window.
*
* commit 6e2c1b9
| Author: Ravi Mehta <ravi@pylon.dev>
| Date:   2026-03-23 17:00:00 -0700
|
|     chore(security): quarterly secrets rotation (PYL-402)
|
|     AWS service-account keys, Datadog, Sentry, Postgres replication creds,
|     internal HMAC. SOC 2 evidence updated.
*
* commit b4f8d6a (tag: v2.2.0)
| Author: Jordan Mwangi <jordan@pylon.dev>
| Date:   2026-03-13 16:45:00 -0400
|
|     feat(switchyard): wire GitLab MR diffs into Beacon analyzer pipeline (PYL-209)
*
* commit f1c3b8e
| Author: Tomás Herrera <tomas@pylon.dev>
| Date:   2026-02-25 16:00:00 -0300
|
|     fix(dashboard): audit log query streaming for >10k rows (PYL-303)
|
|     Stratosphere Robotics hit 30s timeout on 12-month filter (~150k rows).
|     Added (org_id, event_type, created_at) index. Page-query window capped
|     at 30 days; longer windows go through export pipeline.
*
* commit a9e7c0d (tag: v2.1.5)
| Author: Ravi Mehta <ravi@pylon.dev>
| Date:   2026-02-12 15:00:00 -0700
|
|     chore(infra): pgvector 0.5 → 0.7 (PYL-401)
*
* commit 5d4e8f1 (tag: v2.1.0)
| Author: Camille Dubois <camille@pylon.dev>
| Date:   2026-02-13 16:45:00 -0400
|
|     feat(tower): team comparison data API (PYL-213)
|
|     Denormalized read model in ClickHouse. Permissions filtering at the
|     query layer. <500ms p95 for orgs with 50 teams + 90-day window.
*
* commit c8a2d5b
| Author: Hugo Lefèvre <hugo@pylon.dev>
| Date:   2026-01-13 11:30:00 +0100
|
|     fix(rules): scope python.bare-except out of test paths (PYL-302)
|
|     Arcola Studios reported false positives on intentional bare-except
|     in test fixtures. Default scoping now skips tests/, conftest.py,
|     test_*.py, *_test.py. Customers can override.
*
* commit 1f9e3a7 (tag: v2.0.0)
| Author: Camille Dubois <camille@pylon.dev>
| Date:   2026-01-30 15:00:00 -0400
|
|     feat(dashboard): audit log UI for Business+ tier (PYL-218)
|
|     BREAKING: Finding.severity enum normalized. See migration guide.
*
* commit 7b2c0d8
| Author: Ravi Mehta <ravi@pylon.dev>
| Date:   2026-01-02 13:00:00 -0700
|
|     chore(deps): FastAPI 0.110 → 0.115 (PYL-400)
*
* commit 4e1f6c3 (tag: v1.9.0)
| Author: Ravi Mehta <ravi@pylon.dev>
| Date:   2025-12-19 16:30:00 -0700
|
|     feat(infra): audit log event schema + ingest (PYL-217)
|
|     Append-only via revoking UPDATE/DELETE on the table from the app role
|     (Postgres-level enforcement, not just convention). PII sanitization
|     for rule diff content per Priya's review.
*
* commit 9d3a8b5 (tag: v1.8.5)
| Author: Camille Dubois <camille@pylon.dev>
| Date:   2025-12-15 15:00:00 -0400
|
|     fix(tower): cycle-time chart shows actual time for self-reviews (PYL-301)
*
* commit 2f7c1e9 (tag: v1.8.0)
| Author: Jordan Mwangi <jordan@pylon.dev>
| Date:   2025-12-05 17:00:00 -0400
|
|     feat(switchyard): GitLab OAuth + token refresh (PYL-208)
*
* commit 6c8a3b0
| Author: Jordan Mwangi <jordan@pylon.dev>
| Date:   2025-12-05 15:30:00 -0400
|
|     feat(switchyard): GitLab MR comment poster (PYL-207)
*
* commit a4f1d7b (tag: v1.7.0)
| Author: Jordan Mwangi <jordan@pylon.dev>
| Date:   2025-11-21 16:00:00 -0400
|
|     feat(switchyard): GitLab webhook ingest (PYL-206)
|
|     Adapter pattern normalizes GitLab + GitHub webhooks into a single
|     internal WebhookEvent shape. Downstream pipeline doesn't change.
*
* commit 0e9c5d2 (tag: v1.6.1)
| Author: Jordan Mwangi <jordan@pylon.dev>
| Date:   2025-10-30 14:22:00 -0400
|
|     fix(switchyard): re-register webhooks on GitHub App reinstall (PYL-300)
|
|     Production fix. installation_repositories.added now triggers webhook
|     re-registration the same as installation.created. 11 affected customer
|     orgs identified via missing-webhook-events query and backfilled.
*
* commit 8b3e4f0 (tag: v1.6.0)
  Author: Ravi Mehta <ravi@pylon.dev>
  Date:   2025-10-26 18:00:00 -0700

      feat(switchyard): hardening pass post-Q3 incident
```

## Stats

- **31 commits** shown above (subset of the full ~140 commits in the 6-month window — full log lives in `.git/` once `init-history.sh` runs)
- **Top contributors by commit count** in the window: Jordan Mwangi (28), Hugo Lefèvre (24), Camille Dubois (19), Tomás Herrera (17), Ravi Mehta (15), Wei Chen (12), Felix Chen (8), others (combined ~17)
- **Tags**: 14 (1.6.0 → 2.4.2), one minor or patch per ~12-15 commits
- **Merge commits**: 23 (mostly squash-merged feature branches)
- **Friday-merge violations**: 0 (per company policy; enforced by branch protection rules)

## How to recreate the full history

```bash
cd codebases/api
bash scripts/init-history.sh   # not yet shipped — POC follow-up
```

This script will initialize a fresh `.git/` inside `codebases/api/`, replay each commit listed in `HISTORY.md` (extended to the full ~140-commit log), and tag releases. Resulting `.git/` is intentionally not committed into the parent `pylon` repo (see parent `.gitignore`).
