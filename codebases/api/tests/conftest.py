"""Shared pytest fixtures."""

from __future__ import annotations

import os

import pytest

from pylon.models import Diff, FileChange


@pytest.fixture(autouse=True)
def _webhook_secrets() -> None:
    """Ensure webhook secret env vars are set for any test that exercises
    the signature path. Tests that need different values can override."""
    os.environ.setdefault("PYLON_GITHUB_WEBHOOK_SECRET", "test-github-secret")
    os.environ.setdefault("PYLON_GITLAB_WEBHOOK_TOKEN", "test-gitlab-token")


def make_diff(path: str, *, added: list[str], removed: list[str] | None = None) -> Diff:
    """Build a Diff fixture from added/removed line lists."""
    removed = removed or []
    patch_lines = ["@@ -1,1 +1,{} @@".format(len(added) + 1)]
    patch_lines += [f"-{r}" for r in removed]
    patch_lines += [f"+{a}" for a in added]
    patch = "\n".join(patch_lines)
    return Diff(
        pr_id="test-pr-1",
        base_sha="0000000",
        head_sha="1111111",
        files=[
            FileChange(
                path=path,
                language="python" if path.endswith(".py") else None,
                added=len(added),
                removed=len(removed),
                patch=patch,
            )
        ],
    )
