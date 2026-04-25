"""``python.print-in-prod`` — flag ``print(`` calls in non-test paths.

Prefer the project's logger. Print statements bypass log routing, log levels,
and structured-logging tags; they show up in production but are easy to miss
during review.
"""

from __future__ import annotations

import re

from pylon.models import Diff, Finding, Severity
from pylon.rules.bare_except import _added_lines, _is_test_path


_PRINT_CALL = re.compile(r"^\s*print\s*\(")

RULE_ID = "python.print-in-prod"


def check(diff: Diff) -> list[Finding]:
    findings: list[Finding] = []
    for fc in diff.files:
        if not fc.path.endswith(".py"):
            continue
        if _is_test_path(fc.path):
            continue
        for line_no, line in _added_lines(fc.patch):
            if _PRINT_CALL.match(line):
                findings.append(
                    Finding(
                        rule_id=RULE_ID,
                        severity=Severity.LOW,
                        file_path=fc.path,
                        line=line_no,
                        message=(
                            "`print(` call in non-test code. Use the project logger so the message "
                            "respects log levels and structured-logging tags."
                        ),
                        suggestion="logger.info(...)",
                    )
                )
    return findings
