"""Beacon analyzer entry point.

The analyzer is the heart of Pylon's product surface. It takes a Diff and a
list of enabled rule IDs, runs each rule against the changed files, and
returns a list of Findings.

This file orchestrates rule execution; rule logic itself lives in the
:mod:`pylon.rules` subpackage. Adding a new rule means adding a module
under ``pylon/rules/`` and registering it in the ``_RULES`` dict below.
"""

from __future__ import annotations

from typing import Callable

from pylon.models import Diff, Finding
from pylon.rules import (
    async_without_await,
    bare_except,
    bare_mutex,
    print_in_prod,
    todo_without_author,
)


# Rule registry. Each entry maps a stable rule ID (used in customer configs,
# in suppression annotations, in Tower analytics) to the function that runs it.
# Rule IDs are namespaced by language for now; future cross-language rules
# may live under ``pylon.*``.
_RULES: dict[str, Callable[[Diff], list[Finding]]] = {
    "python.bare-except": bare_except.check,
    "python.print-in-prod": print_in_prod.check,
    "python.todo-without-author": todo_without_author.check,
    "python.bare-mutex": bare_mutex.check,
    "python.async-without-await": async_without_await.check,
}


def default_rule_ids() -> list[str]:
    """The default rule set for new customers. All registered rules currently."""
    return list(_RULES.keys())


def run_analyzer(diff: Diff, enabled_rules: list[str]) -> list[Finding]:
    """Run all enabled rules over the diff.

    Unknown rule IDs are silently ignored — the rule registry can lag a
    customer's config (e.g., during a rolling rule retirement). Logging a
    warning for unknowns is appropriate at the production call-site.
    """
    findings: list[Finding] = []
    for rule_id in enabled_rules:
        check = _RULES.get(rule_id)
        if check is None:
            continue
        findings.extend(check(diff))
    return _dedupe(findings)


def _dedupe(findings: list[Finding]) -> list[Finding]:
    """Drop duplicate findings (same rule + file + line). Beacon's filter
    layer in production also collapses near-duplicates with proximity
    heuristics; we don't replicate that here to keep this module focused."""
    seen: set[tuple[str, str, int]] = set()
    unique: list[Finding] = []
    for f in findings:
        key = (f.rule_id, f.file_path, f.line)
        if key in seen:
            continue
        seen.add(key)
        unique.append(f)
    return unique
