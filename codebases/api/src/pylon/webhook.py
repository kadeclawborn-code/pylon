"""Webhook signature verification + event normalization.

Supports GitHub, GitLab, and Bitbucket Cloud. Each vendor's signature scheme
is different; this module normalizes them and emits a ``WebhookEvent`` that
the rest of the pipeline can consume without caring about the source vendor.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
from datetime import UTC, datetime

from pylon.models import WebhookEvent


class SignatureError(ValueError):
    """Raised when a webhook signature fails to verify."""


def _github_secret() -> bytes:
    secret = os.environ.get("PYLON_GITHUB_WEBHOOK_SECRET", "")
    if not secret:
        raise RuntimeError("PYLON_GITHUB_WEBHOOK_SECRET not set")
    return secret.encode("utf-8")


def _gitlab_token() -> str:
    token = os.environ.get("PYLON_GITLAB_WEBHOOK_TOKEN", "")
    if not token:
        raise RuntimeError("PYLON_GITLAB_WEBHOOK_TOKEN not set")
    return token


def verify_github_signature(body: bytes, signature: str) -> None:
    """GitHub's HMAC-SHA256 in the ``X-Hub-Signature-256`` header.

    Header value format: ``sha256=<hex>``.
    """
    if not signature.startswith("sha256="):
        raise SignatureError("missing or malformed signature")
    expected = hmac.new(_github_secret(), body, hashlib.sha256).hexdigest()
    provided = signature.split("=", 1)[1]
    if not hmac.compare_digest(expected, provided):
        raise SignatureError("signature mismatch")


def verify_gitlab_token(token: str) -> None:
    """GitLab uses a shared token in ``X-Gitlab-Token``, not HMAC.

    This is one of the platform differences the Switchyard adapter layer
    handles — see PYL-206 for the kickoff and PYL-306 for the postmortem
    on a related GitHub-side rotation issue.
    """
    if not hmac.compare_digest(_gitlab_token(), token):
        raise SignatureError("token mismatch")


async def handle_github_webhook(body: bytes, signature: str, event_type: str) -> WebhookEvent | None:
    verify_github_signature(body, signature)
    payload = json.loads(body)
    if event_type == "ping":
        return WebhookEvent(
            vendor="github",
            event_type="ping",
            repo_full_name=payload.get("repository", {}).get("full_name", ""),
            actor_login=payload.get("sender", {}).get("login", ""),
            received_at=datetime.now(UTC),
            raw_payload_size_bytes=len(body),
        )
    if event_type == "pull_request":
        action = payload.get("action", "")
        mapped: str | None = None
        if action == "opened":
            mapped = "pr_opened"
        elif action == "synchronize":
            mapped = "pr_updated"
        elif action == "closed":
            mapped = "pr_closed"
        if not mapped:
            return None
        return WebhookEvent(
            vendor="github",
            event_type=mapped,
            repo_full_name=payload["repository"]["full_name"],
            pr_number=payload["pull_request"]["number"],
            actor_login=payload["sender"]["login"],
            received_at=datetime.now(UTC),
            raw_payload_size_bytes=len(body),
        )
    # Other event types are accepted but produce no normalized event yet.
    return None


async def handle_gitlab_webhook(body: bytes, signature: str, event_type: str) -> WebhookEvent | None:
    verify_gitlab_token(signature)
    payload = json.loads(body)
    if event_type == "Merge Request Hook":
        action = payload.get("object_attributes", {}).get("action", "")
        mapped: str | None = None
        if action == "open":
            mapped = "pr_opened"
        elif action == "update":
            mapped = "pr_updated"
        elif action in ("close", "merge"):
            mapped = "pr_closed"
        if not mapped:
            return None
        return WebhookEvent(
            vendor="gitlab",
            event_type=mapped,
            repo_full_name=payload["project"]["path_with_namespace"],
            pr_number=payload["object_attributes"]["iid"],
            actor_login=payload["user"]["username"],
            received_at=datetime.now(UTC),
            raw_payload_size_bytes=len(body),
        )
    return None
