"""``python.todo-without-author`` — flag TODO comments without an author tag.

A TODO without an owner becomes orphan tech debt. Pylon flags ``TODO`` and
``FIXME`` comments that don't include an ``@username`` to make the comment
findable by who owns it. Pattern is intentionally permissive — accepts
``@`` followed by alphanumerics, dashes, dots, and underscores.
"""

from __future__ import annotations

import re

from pylon.models import Diff, Finding, Severity
from pylon.rules.bare_except import _added_lines, _is_test_path


# Match TODO / FIXME / XXX / HACK followed eventually by some text.
# Capture the inline content to check whether @username appears.
_TODO_LINE = re.compile(r"#\s*(TODO|FIXME|XXX|HACK)\b(.*)$", re.IGNORECASE)
_AUTHOR_TAG = re.compile(r"@[A-Za-z0-9._-]+")

RULE_ID = "python.todo-without-author"


def check(diff: Diff) -> list[Finding]:
    findings: list[Finding] = []
    for fc in diff.files:
        if not fc.path.endswith(".py"):
            continue
        if _is_test_path(fc.path):
            continue
        for line_no, line in _added_lines(fc.patch):
            m = _TODO_LINE.search(line)
            if not m:
                continue
            content = m.group(2)
            if _AUTHOR_TAG.search(content):
                continue
            kind = m.group(1).upper()
            findings.append(
                Finding(
                    rule_id=RULE_ID,
                    severity=Severity.LOW,
                    file_path=fc.path,
                    line=line_no,
                    message=(
                        f"{kind} without an owner. Add `@username` so the next person to read "
                        f"this comment knows who to ask."
                    ),
                    suggestion=None,
                )
            )
    return findings
