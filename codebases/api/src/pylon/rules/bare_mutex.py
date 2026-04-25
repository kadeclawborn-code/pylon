"""``python.bare-mutex`` — flag ``Lock()`` / ``Semaphore()`` not used as a context manager.

Acquiring a mutex without ``with`` risks the lock being held forever if an
exception fires between acquire and release. Use ``with lock:`` instead.

This rule is intentionally syntactic — it doesn't track lock objects across
scope. False positives on factory-pattern usage are documented; customers
with that pattern can suppress per-line or scope the rule out.
"""

from __future__ import annotations

import re

from pylon.models import Diff, Finding, Severity
from pylon.rules.bare_except import _added_lines, _is_test_path


# Match a name = SomeMutex() pattern that's NOT the head of a `with` statement.
# Conservative: only flags when the assignment isn't preceded by `with `.
_MUTEX_CONSTRUCT = re.compile(
    r"^(?P<lead>\s*)(?P<rest>(?!with\s)\w+\s*=\s*(?:threading\.)?(Lock|RLock|Semaphore|BoundedSemaphore)\s*\()"
)

RULE_ID = "python.bare-mutex"


def check(diff: Diff) -> list[Finding]:
    findings: list[Finding] = []
    for fc in diff.files:
        if not fc.path.endswith(".py"):
            continue
        if _is_test_path(fc.path):
            continue
        for line_no, line in _added_lines(fc.patch):
            if _MUTEX_CONSTRUCT.match(line):
                findings.append(
                    Finding(
                        rule_id=RULE_ID,
                        severity=Severity.MEDIUM,
                        file_path=fc.path,
                        line=line_no,
                        message=(
                            "Mutex constructed but not used as a context manager. If an exception "
                            "fires between acquire and release the lock will be held forever. "
                            "Use `with lock:` or wrap acquire/release in try/finally."
                        ),
                        suggestion="with lock:",
                    )
                )
    return findings
