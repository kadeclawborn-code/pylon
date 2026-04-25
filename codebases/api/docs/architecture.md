# pylon-api — Architecture

> Runtime overview of the API service. For Pylon's overall product architecture (Beacon + Tower + Switchyard at the company level), see the [Master PRD](../../../product/PRD.md).

## What this service is

`pylon-api` is the runtime that powers `pylon.dev`. Concretely it does four things:

1. **Receives webhooks** from GitHub / GitLab / Bitbucket Cloud (Switchyard layer)
2. **Runs the analyzer** on PR diffs (Beacon layer)
3. **Stores findings** for the dashboard to read (Postgres + Redis cache)
4. **Posts in-line PR comments** back to the host VCS

Everything outside this service — the dashboard, Tower's analytics ingest, the marketing site — runs as separate workloads.

## Process model

Single FastAPI app. Three logical surfaces:

- **Webhook ingress** — synchronous request/response, returns 202 fast, dispatches the actual work to a worker queue
- **Analyzer** — invoked from the queue worker; can also be called directly via `POST /analyze` for the dashboard's preview feature
- **Findings store** — Postgres (production) backed by Redis cache for hot reads; in-memory dict for tests and local dev

In production this binary runs in two roles, distinguished by environment:

| Role | What it serves | Deployed as |
|---|---|---|
| `web` | HTTP traffic (webhooks, dashboard API) | ASGI fleet behind ALB, AWS us-east-1 |
| `worker` | Queue consumers (analyzer runs, comment posting, GitHub API calls) | ASG of long-running processes |

The same Python codebase, different entry points. Worker mode replaces uvicorn with a queue consumer (BullMQ-compatible client over Redis).

## Data flow — typical PR flow

```
GitHub webhook ─┐
                ▼
       /webhooks/github
                │ verify HMAC
                │ normalize → WebhookEvent
                │ enqueue analyzer job
                ▼
              Redis queue
                │
                ▼
            worker pool
                │ fetch PR diff (github_client)
                │ run_analyzer() → list[Finding]
                │ persist (Postgres)
                │ for each finding: post review comment
                ▼
        finding visible to PR reviewer
```

End-to-end p95 ~90s for a 200-line PR. The analyzer dominates (~70s); webhook → enqueue is ~50ms; comment posting is ~3-8s for a typical 2-finding PR.

## Stateful boundaries

| Store | What's there | Why |
|---|---|---|
| **Postgres 16** | Customer accounts, billing, rule configs, suppression annotations, marketplace data | Source of truth, ACID needed |
| **Redis** | Job queue, rule-compilation cache, GitHub rate-limit budget cache | Latency-sensitive ephemeral state |
| **ClickHouse 24** | Review events, findings history, all Tower aggregation source data | OLAP — multi-month aggregates over millions of events |
| **S3** | Rule bundles, large finding artifacts (diffs > 1MB) | Cheap object storage, content-addressable |

This service touches Postgres + Redis directly. It writes to ClickHouse via a Kafka-style fan-out (Tower's ingest service consumes, not us). It writes to S3 only for the >1MB diff cutoff.

## Code layout

See `README.md` for the file tree. Notable conventions:

- **Rules** are one-file-per-rule. Adding a rule is intentionally low-ceremony so rule velocity stays high.
- **Models** are Pydantic. We don't use SQLAlchemy ORM models in the request/response layer — only at the persistence boundary. Keeps things readable.
- **Client wrappers** (e.g., `github_client`) are thin. We don't hide the underlying API behind elaborate abstractions; if a feature needs a new endpoint, add it.
- **No service layer for service layer's sake.** Routes call handlers; handlers do the work. We add layers when there's a real reason.

## What's deliberately NOT in this codebase

- The dashboard frontend (separate repo)
- The marketing site (separate Astro repo)
- Tower's analytics ingest service (separate repo, ClickHouse-bound)
- The Beacon Rust core (separate Cargo project, called via FFI bindings — kept narrow)
- Customer-side `pylon.yaml` schema (lives in a small `pylon-config` package on PyPI, also Pylon-owned)

## Performance characteristics

- **Webhook ingress**: bounded by HMAC verification + JSON parse. p95 < 50ms for typical payloads (<10KB). >100KB payloads (rare; happens with very large PR descriptions) hit ~200ms.
- **Analyzer**: depends on diff size and language coverage. p50 ~12s for a 200-line diff with default rule set; p95 ~70s.
- **Findings store reads**: Redis cache makes p95 < 5ms; cache miss + Postgres = ~30ms.
- **Comment posting**: GitHub's rate limit (5000 reqs/hour per installation) is the practical ceiling. We back off via the rate-limit budget cache; customers with very high PR volume hit retry queues during burst.

## Failure modes & how we handle them

| Mode | Detection | Handling |
|---|---|---|
| GitHub API rate-limited | 403 with rate-limit headers | Back off, retry with jitter; surface to customer if persistent |
| Webhook signature key rotated upstream | Sudden 100% signature failures | Auto-rotate via JWKS fetch (after PYL-306; previously manual) |
| Analyzer takes > 5 min | Worker timeout | Cancel, log, surface as "analysis failed" PR comment |
| Postgres connection pool exhausted | Sentry alert | Auto-scale pool; if still failing, drop into degraded read-only mode |
| Redis down | Health probe + Sentry | Cache layer fails open: queries hit Postgres directly, slower but works |

## Observability

- **Datadog APM** — every endpoint instrumented; analyzer runs traced end-to-end with rule-level child spans
- **Sentry** — exception capture; PII-stripped at intake
- **Structured logs** — JSON; aggregate to Datadog Logs; retention 30d hot, 90d cold
- **Custom metrics** — finding-rate per rule (for calibration), analyzer duration histogram per rule, comment-post success rate per vendor

## Where to learn more

- [Master PRD](../../../product/PRD.md) — Pylon at the product level
- [Tickets fixture](../../../tickets/all.json) — historical engineering work that touched this codebase
- [Roadmap](../../../product/ROADMAP.md) — what's coming
- Inside this codebase: `src/pylon/main.py` is the smallest entry point to read first; `src/pylon/analyzer.py` is the most architecturally interesting piece.
