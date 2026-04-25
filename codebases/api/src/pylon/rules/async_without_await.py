"""``python.async-without-await`` — flag ``async def`` functions with no ``await``.

An async function with no await is almost always a mistake — the function
should either be sync, or it should be calling something it forgot to await.
This rule is part of the Q2 2026 async-correctness rule pack (PYL-104).

Implementation is intentionally simple — it scans added async function
bodies in the diff. False-positive case: async generators that yield but
don't await. We accept this; the customer can suppress.
"""

from __future__ import annotations

import re

from pylon.models import Diff, Finding, Severity
from pylon.rules.bare_except import _added_lines, _is_test_path


_ASYNC_DEF = re.compile(r"^\s*async\s+def\s+\w+\s*\(")
_AWAIT = re.compile(r"\bawait\s+\S+")
_YIELD = re.compile(r"\byield\b")

RULE_ID = "python.async-without-await"


def check(diff: Diff) -> list[Finding]:
    findings: list[Finding] = []
    for fc in diff.files:
        if not fc.path.endswith(".py"):
            continue
        if _is_test_path(fc.path):
            continue
        added = _added_lines(fc.patch)
        # Group consecutive added lines into bands; check each band for the pattern.
        # This is approximate: it works when the entire async body is in the diff,
        # which covers the common case of a new function being added.
        for line_no, line in added:
            if not _ASYNC_DEF.match(line):
                continue
            # Look ahead through the rest of the added band for `await` or `yield`.
            window = [text for ln, text in added if ln >= line_no and ln <= line_no + 40]
            if any(_AWAIT.search(w) or _YIELD.search(w) for w in window[1:]):
                continue
            findings.append(
                Finding(
                    rule_id=RULE_ID,
                    severity=Severity.HIGH,
                    file_path=fc.path,
                    line=line_no,
                    message=(
                        "`async def` function with no `await`. Either drop the `async` keyword "
                        "or you're missing an `await` somewhere in the body."
                    ),
                    suggestion=None,
                )
            )
    return findings
