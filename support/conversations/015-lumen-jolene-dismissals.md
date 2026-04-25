---
id: 015
account: acct_lumen
customer_user: user_lumen_002
pylon_agent: emp_033
channel: email
status: resolved
opened_at: 2026-04-09T13:22:00Z
closed_at: 2026-04-14T17:00:00Z
category: [help, beacon, calibration]
---

**Customer (Ramon Velasco):**

Bridget — pulling our team's dismissal data for our Q1 review. One engineer (Jolene Carter) is dismissing about 40% of Beacon's findings on her PRs as "false positive." That's roughly 4x our team's average dismissal rate.

Two possibilities: (a) she's seeing real false positives we should report, or (b) she's dismissing things she should be acting on. I want to figure out which before her review tomorrow.

Can you pull the rule breakdown of her dismissals? Specifically: which rules she's dismissing, and any patterns in the surrounding code.

---

**Bridget:**

Ramon — pulling.

Top 3 rules she's dismissing:

1. `python.async-without-await` — 12 dismissals over 30 days
2. `python.bare-mutex` — 8 dismissals
3. `python.todo-without-author` — 7 dismissals

Pattern: most of #1 and #2 dismissals are on her work in `lumen-clinical/billing/queue.py` and `lumen-clinical/data/sync.py`. Both files are async-heavy infrastructure.

I'd guess her dismissals on #1 and #2 are real false positives that point to a calibration gap in our async rules — async functions that yield to a future without an explicit `await` are valid in some patterns, and our rules don't always know that. Our async rule pack (PYL-104) is partially shipping these months precisely because we've seen this calibration gap.

#3 (`todo-without-author`) is likely a stylistic disagreement; she may be choosing not to tag TODOs.

---

**Customer:**

This is helpful. I'll share with Jolene before her review and we'll sample some of those #1 and #2 dismissals together. If they're real FPs, we'll send you the repros so they can feed your calibration.

---

**Bridget:**

Yes — please. We're calibrating PYL-104's first 10 rules right now (shipping in the next sprint). Real customer FP repros are gold.

---

**Customer (4 days later):**

Sampled 6 of Jolene's #1 dismissals with her. 4 are real FPs (async pattern your rule isn't catching); 2 were patterns where Jolene was actually wrong and the rule was right. Sending the 4 FPs as a single bug report.

For #2, sampled 4 of 8. All 4 were real FPs in factory-pattern code where the lock is constructed but immediately wrapped in a `with` further down. Send those as a separate bug.

---

**Bridget:**

Thanks — both reports filed with Hugo and Wei. The factory-pattern false-positive on #2 is a known case we'd documented but not fixed. Adding it to the Q3 calibration sprint.

Jolene was right to dismiss those. The rules need to be smarter.

---

**Customer:**

Glad it's signal not noise. Closing this out.
