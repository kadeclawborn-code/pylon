# Suppressing false positives

Beacon will sometimes flag a finding you intentionally don't want flagged. There are three ways to suppress: per-line annotation, per-rule config, or per-rule path scoping.

## Per-line annotation (most common)

Add a comment to the line:

```python
# pylon: suppress(python.bare-except) — re-raised in caller; keeping bare for compat
try:
    ...
except:  # pylon: suppress(python.bare-except) — re-raised in caller
    raise
```

The annotation must include:
1. The rule ID being suppressed
2. A reason after the `—` (en-dash or hyphen, both fine)

Pylon enforces the reason. Suppressions without reasons are ignored — the finding still posts. This is intentional: drive-by suppressions without rationale become orphaned tech debt.

## Per-rule config (when a rule consistently misfires on a specific path)

If a rule is causing many false positives in a specific area of your codebase, scope the rule out via `pylon.yaml`:

```yaml
rules:
  python.bare-except:
    paths:
      exclude:
        - "tests/test_exception_handling.py"
        - "src/legacy/**"
```

This is preferable to suppressing line-by-line when the pattern is consistent.

## Per-rule severity downgrade (when the rule is right but the finding doesn't merit attention)

Sometimes a rule fires on something that's technically valid but routine. Downgrade the severity rather than suppressing:

```yaml
rules:
  python.todo-without-author:
    severity: info
```

This still surfaces the finding in Tower (so customers can see if the pattern grows) without bothering reviewers.

## Dismissing in the PR UI

If you don't want to commit a suppression to the codebase, you can dismiss the finding in Pylon's PR comment thread directly. Click "Dismiss" → choose a reason:

- **False positive** — the rule fired but the code is correct as-is. Feeds Beacon's calibration data.
- **Won't fix** — the code is wrong but not worth fixing now. Tracks via Tower.
- **Won't fix here** — should be fixed but in a different PR. Tracks via Tower.
- **Deferred** — explicitly marking for follow-up.

Dismissals don't suppress the rule for future PRs. They only resolve the finding on this PR.

## When to suppress vs. fix

A rough rule of thumb:

- **Fix** when the rule is right and the cost of fixing is low
- **Per-line suppress** when the rule is wrong for this specific case (rare, justified)
- **Per-path suppress** when the rule is consistently wrong for a class of files (test fixtures, generated code, etc.)
- **Severity downgrade** when the rule is right but the finding is too noisy to act on

If you find yourself suppressing the same rule on most PRs, the rule is miscalibrated. File a customer-side ticket against the rule (see [Filing rule feedback](https://pylon.dev/docs/rule-feedback)) — that's the data Pylon's calibration team uses to retire or scope rules.

## What gets logged

Pylon logs every suppression and dismissal in the audit log (Business+ tier). The log captures:
- Rule ID
- File path + line number (for per-line suppressions)
- Reason text
- User who added the suppression / dismissal
- Timestamp

This data is also available in Tower. If your team wants to track suppression patterns over time (e.g., "are we suppressing more often this quarter?"), Tower's Findings → Suppression view is the place.
