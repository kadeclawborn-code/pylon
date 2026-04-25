"""Endpoint smoke tests."""

from __future__ import annotations

from fastapi.testclient import TestClient

from pylon.main import app
from tests.conftest import make_diff


client = TestClient(app)


def test_healthz() -> None:
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_version() -> None:
    r = client.get("/version")
    assert r.status_code == 200
    body = r.json()
    assert body["service"] == "pylon-api"
    assert body["version"]


def test_analyze_returns_findings() -> None:
    d = make_diff("svc/handler.py", added=["    except:", "        pass"])
    r = client.post("/analyze", json={"diff": d.model_dump(mode="json")})
    assert r.status_code == 200
    body = r.json()
    assert body["pr_id"] == "test-pr-1"
    assert any(f["rule_id"] == "python.bare-except" for f in body["findings"])
    assert body["duration_ms"] >= 0


def test_findings_returns_empty_for_unknown_pr() -> None:
    """Empty list (not 404) by design — see main.py for rationale."""
    r = client.get("/findings/never-analyzed")
    assert r.status_code == 200
    assert r.json() == []


def test_findings_returns_after_analyze() -> None:
    d = make_diff("svc/handler.py", added=["    except:"])
    client.post("/analyze", json={"diff": d.model_dump(mode="json")})
    r = client.get(f"/findings/{d.pr_id}")
    assert r.status_code == 200
    findings = r.json()
    assert len(findings) >= 1
