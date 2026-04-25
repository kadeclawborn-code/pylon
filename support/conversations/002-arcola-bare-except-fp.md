---
id: 002
account: acct_arcola
customer_user: user_arcola_001
pylon_agent: emp_033
channel: email
status: resolved
opened_at: 2026-01-08T10:14:00Z
closed_at: 2026-01-13T13:00:00Z
category: [bug, beacon, rules]
---

**Customer (Quinn Strickland):**

Hi — we've been suppressing python.bare-except line-by-line in our test fixtures for ~2 months because a lot of our tests intentionally use bare-except to simulate broad exception swallowing in our engine code. Latest test fixture file has 47 bare-except occurrences and Pylon flagged 47 of them. I can either suppress all 47 (which feels wrong — these are intentional) or scope the rule out for tests/, but I don't want to globally turn it off.

What's the right move here?

Repro repo: `arcola-studios/engine-test-corpus`

---

**Bridget:**

Quinn — that's a real Beacon scoping gap on our side, not a customer-config issue. The python.bare-except rule should default-skip test paths. We have a customer-config option (`pylon.yaml` → `rules.python.bare-except.exclude_paths`) but it shouldn't be necessary; the default is wrong.

Filing this with engineering. Two things in the meantime:

1. Use the config exclusion: `tests/**` and `**/conftest.py`. I'll send the snippet.
2. Don't suppress per-line. We'd rather you wait for the default fix than pollute your codebase with suppression annotations.

---

**Customer:**

Sounds good. Put the config exclusion in. Thanks.

If the default changes, will I need to revert my override?

---

**Bridget:**

Good question. The fix will change the default; your override will keep working but become redundant. We'll mention it in the release notes.

> _internal_: this is PYL-302. Filing.

---

**Bridget (4 days later):**

Quinn — the fix is live in Beacon as of yesterday. Default skips `tests/`, `**/conftest.py`, `**/test_*.py`, `**/*_test.py`. Your override still works. You can remove it next time you touch `pylon.yaml` if you want.

---

**Customer:**

Removed. Closing the loop. Thanks for the fast turnaround.
