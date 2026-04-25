"""GitHub API wrapper.

Thin wrapper around httpx for the few GitHub endpoints Pylon hits. Concrete
methods are kept narrow on purpose; broader API surface is added when a
specific feature needs it.
"""

from __future__ import annotations

import os
from typing import Any

import httpx


GITHUB_API = "https://api.github.com"


class GitHubClient:
    """Async GitHub API client. Pass ``installation_token`` for App-installed
    repos or ``user_token`` for user-flow operations."""

    def __init__(self, *, installation_token: str | None = None, user_token: str | None = None):
        if not (installation_token or user_token):
            raise ValueError("must supply installation_token or user_token")
        self._token = installation_token or user_token
        self._client = httpx.AsyncClient(
            base_url=GITHUB_API,
            timeout=httpx.Timeout(15.0, connect=5.0),
            headers={
                "Accept": "application/vnd.github.v3+json",
                "Authorization": f"Bearer {self._token}",
                "User-Agent": "pylon-api/" + os.environ.get("PYLON_VERSION", "2.4.2"),
            },
        )

    async def __aenter__(self) -> "GitHubClient":
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self._client.aclose()

    async def get_pr_diff(self, *, owner: str, repo: str, number: int) -> str:
        """Fetch the unified diff for a PR. GitHub returns it as text/plain
        when the Accept header asks for ``application/vnd.github.diff``."""
        resp = await self._client.get(
            f"/repos/{owner}/{repo}/pulls/{number}",
            headers={"Accept": "application/vnd.github.diff"},
        )
        resp.raise_for_status()
        return resp.text

    async def post_review_comment(
        self,
        *,
        owner: str,
        repo: str,
        number: int,
        commit_sha: str,
        path: str,
        line: int,
        body: str,
    ) -> dict[str, Any]:
        """Post an in-line PR review comment."""
        resp = await self._client.post(
            f"/repos/{owner}/{repo}/pulls/{number}/comments",
            json={
                "body": body,
                "commit_id": commit_sha,
                "path": path,
                "line": line,
                "side": "RIGHT",
            },
        )
        resp.raise_for_status()
        return resp.json()
