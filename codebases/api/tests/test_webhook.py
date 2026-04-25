"""Webhook signature + event-normalization tests."""

from __future__ import annotations

import hashlib
import hmac
import json

import pytest

from pylon.webhook import (
    SignatureError,
    handle_github_webhook,
    handle_gitlab_webhook,
    verify_github_signature,
    verify_gitlab_token,
)


def _sign_github(body: bytes, secret: bytes = b"test-github-secret") -> str:
    return "sha256=" + hmac.new(secret, body, hashlib.sha256).hexdigest()


def test_github_signature_pass() -> None:
    body = b'{"hello":"world"}'
    verify_github_signature(body, _sign_github(body))


def test_github_signature_fail_on_bad_sig() -> None:
    with pytest.raises(SignatureError):
        verify_github_signature(b'{"x":1}', "sha256=deadbeef")


def test_github_signature_fail_on_missing_prefix() -> None:
    with pytest.raises(SignatureError):
        verify_github_signature(b"{}", "deadbeef")


def test_gitlab_token_pass() -> None:
    verify_gitlab_token("test-gitlab-token")


def test_gitlab_token_fail() -> None:
    with pytest.raises(SignatureError):
        verify_gitlab_token("wrong-token")


async def test_github_pr_opened_normalization() -> None:
    body_dict = {
        "action": "opened",
        "repository": {"full_name": "kadeclawborn-code/pylon"},
        "pull_request": {"number": 42},
        "sender": {"login": "marcus"},
    }
    body = json.dumps(body_dict).encode()
    evt = await handle_github_webhook(
        body=body,
        signature=_sign_github(body),
        event_type="pull_request",
    )
    assert evt is not None
    assert evt.vendor == "github"
    assert evt.event_type == "pr_opened"
    assert evt.pr_number == 42
    assert evt.actor_login == "marcus"


async def test_gitlab_mr_opened_normalization() -> None:
    body_dict = {
        "object_kind": "merge_request",
        "object_attributes": {"action": "open", "iid": 7},
        "project": {"path_with_namespace": "verdant-energy/main"},
        "user": {"username": "priya"},
    }
    body = json.dumps(body_dict).encode()
    evt = await handle_gitlab_webhook(
        body=body,
        signature="test-gitlab-token",
        event_type="Merge Request Hook",
    )
    assert evt is not None
    assert evt.vendor == "gitlab"
    assert evt.event_type == "pr_opened"
    assert evt.pr_number == 7
    assert evt.actor_login == "priya"


async def test_github_ping_normalized() -> None:
    body_dict = {"repository": {"full_name": "x/y"}, "sender": {"login": "z"}}
    body = json.dumps(body_dict).encode()
    evt = await handle_github_webhook(
        body=body,
        signature=_sign_github(body),
        event_type="ping",
    )
    assert evt is not None
    assert evt.event_type == "ping"
