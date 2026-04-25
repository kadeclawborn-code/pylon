"""Analyzer-level tests: rule registry, dispatch, dedup."""

from __future__ import annotations

from pylon.analyzer import default_rule_ids, run_analyzer
from tests.conftest import make_diff


def test_default_rule_set_is_nonempty() -> None:
    rules = default_rule_ids()
    assert len(rules) >= 5
    assert all(r.startswith("python.") for r in rules)


def test_unknown_rule_id_silently_ignored() -> None:
    diff = make_diff("svc/handler.py", added=["except:"])
    findings = run_analyzer(diff=diff, enabled_rules=["python.bare-except", "python.does-not-exist"])
    assert len(findings) == 1
    assert findings[0].rule_id == "python.bare-except"


def test_dedup_same_finding_not_duplicated() -> None:
    diff = make_diff("svc/handler.py", added=["except:"])
    rules = ["python.bare-except", "python.bare-except"]  # registered twice on purpose
    findings = run_analyzer(diff=diff, enabled_rules=rules)
    assert len(findings) == 1


def test_no_findings_on_empty_added_lines() -> None:
    diff = make_diff("svc/handler.py", added=[])
    findings = run_analyzer(diff=diff, enabled_rules=default_rule_ids())
    assert findings == []
