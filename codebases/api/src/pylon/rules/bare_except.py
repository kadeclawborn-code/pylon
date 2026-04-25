"""``python.bare-except`` — flag bare ``except:`` clauses without an exception type.

Bare excepts swallow ``KeyboardInterrupt``, ``SystemExit``, and silent bugs.
Catching ``Exception`` is rarely better but at least signals intent.

This rule is scoped to skip test-fixture paths (``tests/``, ``conftest.py``,
``test_*.py``, ``*_test.py``) by default per PYL-302. Customers can override
via their ``pylon.yaml`` config.
"""

from __future__ import annotations

import re

from pylon.models import Diff, Finding, Severity


_BARE_EXCEPT = re.compile(r"^\s*except\s*:\s*(?:#.*)?$")
_TEST_PATHS = (
    "tests/",
    "/tests/",
    "test_",
    "_test.py",
    "conftest.py",
)

RULE_ID = "python.bare-except"


def _is_test_path(path: str) -> bool:
    return any(t in path for t in _TEST_PATHS)


def check(diff: Diff) -> list[Finding]:
    findings: list[Finding] = []
    for fc in diff.files:
        if not fc.path.endswith(".py"):
            continue
        if _is_test_path(fc.path):
            continue
        for line_no, line in _added_lines(fc.patch):
            if _BARE_EXCEPT.match(line):
                findings.append(
                    Finding(
                        rule_id=RULE_ID,
                        severity=Severity.MEDIUM,
                        file_path=fc.path,
                        line=line_no,
                        message=(
                            "Bare `except:` swallows KeyboardInterrupt, SystemExit, and any "
                            "future exception type. Catch `Exception` if you genuinely want all "
                            "errors, or a specific subclass if you don't."
                        ),
                        suggestion="except Exception:",
                    )
                )
    return findings


def _added_lines(patch: str) -> list[tuple[int, str]]:
    """Yield (new_line_number, line_text) for each added line in a unified diff."""
    out: list[tuple[int, str]] = []
    new_line = 0
    for raw in patch.splitlines():
        if raw.startswith("@@"):
            # @@ -a,b +c,d @@ — pull the new file's starting line
            try:
                seg = raw.split("+", 1)[1].split(" ", 1)[0]
                new_line = int(seg.split(",")[0]) - 1
            except (IndexError, ValueError):
                continue
            continue
        if raw.startswith("+++") or raw.startswith("---"):
            continue
        if raw.startswith("+"):
            new_line += 1
            out.append((new_line, raw[1:]))
        elif raw.startswith("-"):
            continue  # removed line, no new-line counter advance
        else:
            new_line += 1  # context line
    return out
