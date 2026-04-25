# pylon-api

> Pylon's PR review automation API. Webhook ingest, code analyzer, findings storage.

This is the runtime that powers `pylon.dev`. It receives webhooks from GitHub / GitLab / Bitbucket Cloud, runs the Beacon analyzer on PR diffs, posts findings as in-line comments, and serves the dashboard's data.

This subrepo lives inside the [`pylon` testbed repo](https://github.com/kadeclawborn-code/pylon) but maintains its own commit history (see [HISTORY.md](./HISTORY.md) for the synthetic 6-month log).

## Status

`v2.4.2` — current production version (April 2026). Switchyard for GitLab Cloud is GA-ready pending PYL-305 fix; Beacon Marketplace shipped in `v2.4.0` (March 2026).

## Quick start

```bash
# Setup
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Run tests
pytest

# Run the API locally
uvicorn pylon.main:app --reload --port 8000

# Lint
ruff check src tests
mypy src
```

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| POST | `/webhooks/github` | GitHub App webhook (PR events, etc.) |
| POST | `/webhooks/gitlab` | GitLab Cloud webhook (MR events) |
| POST | `/analyze` | Run Beacon analyzer on a code diff (synchronous, used internally + for testing) |
| GET | `/findings/{pr_id}` | Get findings for a specific PR |
| GET | `/healthz` | Liveness probe |
| GET | `/version` | Build/version info |

## Repository layout

```
pylon-api/
├── src/pylon/
│   ├── main.py          FastAPI app + routing
│   ├── webhook.py       Webhook signature verification + event routing
│   ├── analyzer.py      Beacon analyzer entry point
│   ├── rules/           Beacon rule implementations (one per file)
│   │   ├── bare_except.py
│   │   ├── print_in_prod.py
│   │   ├── todo_without_author.py
│   │   ├── bare_mutex.py
│   │   └── async_without_await.py
│   ├── models.py        Pydantic models (Finding, Diff, etc.)
│   └── github_client.py GitHub API wrapper
├── tests/               pytest tests (one file per source module)
├── docs/architecture.md
├── .github/             CI, issue templates, PR template
├── pyproject.toml
├── HISTORY.md           Synthetic 6-month git log (testbed artifact)
├── issues.json          Synthetic GitHub issues (testbed artifact)
└── pull_requests.json   Synthetic GitHub pull requests (testbed artifact)
```

## Architecture (one paragraph)

Webhooks land on `/webhooks/<vendor>`, get signature-verified, and produce a normalized `WebhookEvent`. The event dispatches to the analyzer if it's a PR-touch event. The analyzer pulls the PR diff (via `github_client` or its GitLab equivalent — Switchyard layer abstracts this), parses each changed file with tree-sitter, runs each enabled Beacon rule against the AST, and emits `Finding` objects. Findings get persisted (Postgres in production; in-memory dict in tests) and posted back to the host VCS as in-line PR comments. Tower's analytics ingest pipeline subscribes to the same finding events for aggregation. See `docs/architecture.md` for the full story.

## Versioning

This service uses semantic versioning. **2.4.x** is the current line; **2.5** ships when SOC 2 Type II audit-log evidence integration is complete (Q3 2026 target).

## Contributing

Internal team only. Conventional commits (`feat:`, `fix:`, `refactor:`, `test:`, `chore:`, `docs:`). No `--no-verify`. PR template required. CI must pass before merge. No Friday merges (per company policy; see [pylon Identity](../../IDENTITY.md)).

## License

Apache 2.0 (matches the parent `pylon` testbed).
