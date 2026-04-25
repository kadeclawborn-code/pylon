"""FastAPI app entry point."""

from __future__ import annotations

import time
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI, HTTPException, Request, status

from pylon import __version__
from pylon.analyzer import run_analyzer, default_rule_ids
from pylon.models import AnalyzeRequest, AnalyzeResponse, Finding
from pylon.webhook import handle_github_webhook, handle_gitlab_webhook


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Startup / shutdown hooks. Wire up Postgres pool, Redis, etc. in prod."""
    # In production we'd initialize database connection pools, Redis client,
    # warmup the rule registry, etc. For tests we keep this lean.
    yield


app = FastAPI(
    title="Pylon API",
    version=__version__,
    description="PR review automation. Webhooks, analyzer, findings.",
    lifespan=lifespan,
)


# In-memory finding store. In production this is Postgres + Redis cache.
# Keyed by ``pr_id``. Findings are append-only within a PR; re-analyzing
# replaces the prior set. Test harness clears this between runs.
_findings_store: dict[str, list[Finding]] = {}


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    """Liveness probe. Returns 200 unconditionally if the process is up."""
    return {"status": "ok"}


@app.get("/version")
async def version() -> dict[str, str]:
    """Build / version info."""
    return {"version": __version__, "service": "pylon-api"}


@app.post("/webhooks/github", status_code=status.HTTP_202_ACCEPTED)
async def github_webhook(request: Request) -> dict[str, str]:
    body = await request.body()
    signature = request.headers.get("X-Hub-Signature-256", "")
    event_type = request.headers.get("X-GitHub-Event", "")
    try:
        await handle_github_webhook(body=body, signature=signature, event_type=event_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    return {"status": "accepted"}


@app.post("/webhooks/gitlab", status_code=status.HTTP_202_ACCEPTED)
async def gitlab_webhook(request: Request) -> dict[str, str]:
    body = await request.body()
    signature = request.headers.get("X-Gitlab-Token", "")
    event_type = request.headers.get("X-Gitlab-Event", "")
    try:
        await handle_gitlab_webhook(body=body, signature=signature, event_type=event_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    return {"status": "accepted"}


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest) -> AnalyzeResponse:
    """Run the Beacon analyzer on a diff. Synchronous; intended for the internal
    pipeline + for the dashboard's "preview" feature where customers test
    a custom rule against historical PRs.

    For production-volume webhook traffic the pipeline calls ``run_analyzer``
    directly via the worker queue, not this endpoint.
    """
    started = time.perf_counter()
    enabled = req.enabled_rules or default_rule_ids()
    findings = run_analyzer(diff=req.diff, enabled_rules=enabled)
    duration_ms = int((time.perf_counter() - started) * 1000)
    _findings_store[req.diff.pr_id] = findings
    return AnalyzeResponse(
        pr_id=req.diff.pr_id,
        findings=findings,
        rules_run=enabled,
        duration_ms=duration_ms,
    )


@app.get("/findings/{pr_id}", response_model=list[Finding])
async def get_findings(pr_id: str) -> list[Finding]:
    """Return all current findings for a PR. Returns an empty list (not 404)
    for unknown PRs because callers frequently poll before the analyzer
    has run, and 404 noise drowns out real misses.
    """
    return _findings_store.get(pr_id, [])
