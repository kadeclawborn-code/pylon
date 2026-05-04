---
title: The signal-to-noise tax — what we learned tuning python.bare-except
description: Every false positive is a tax on the only humans who can catch the real ones. Here's how Beacon's bare-except rule got smarter.
publishedAt: 2026-04-15
author: Hugo Lefèvre
tags: [beacon, rules, python, calibration]
---

We have a phrase that comes up in almost every Pylon design discussion: *the signal-to-noise tax*. Every false positive a rule fires is a tax on the only humans who can catch the real ones. The reviewer who dismisses three Pylon comments in a row stops reading the fourth. By the time the genuinely useful rule fires, attention is gone.

We retired one rule and rescoped another this quarter explicitly because we'd let the tax creep up. Here's the story of one of them — `python.bare-except` — and what we changed.

## What the rule does

`python.bare-except` flags `except:` clauses that catch any exception type. The argument for it is simple: bare excepts swallow `KeyboardInterrupt`, `SystemExit`, and any future exception type the codebase introduces. They make debugging harder and they hide bugs. Catching `Exception` is rarely better but at least signals intent.

We shipped it on day one of Beacon's Python rule pack in early 2025. It has been firing dutifully ever since.

## What went wrong

Late January, our customer success team started noticing a pattern in the dismissal data. One customer (Arcola Studios — a game studio with a large test corpus) was dismissing every single `bare-except` finding as "false positive." Forty-seven dismissals on one PR. They weren't wrong: the file was a test fixture that intentionally used bare excepts to simulate broad exception swallowing in their game engine code. The rule was firing technically correctly and pragmatically wrongly.

Their tech lead filed a support ticket asking what we'd recommend. The honest answer was *suppress per-line and we'll fix the default* — and that's what we did, in the short term. The rule had a config option to scope it out (`paths.exclude`) but the fact that we needed customers to use that option meant the default was wrong.

## The fix

We changed the default. As of Beacon 2.1.5, `python.bare-except` skips test paths automatically:

```yaml
- "tests/**"
- "**/conftest.py"
- "**/test_*.py"
- "**/*_test.py"
```

Customers who want the rule on test files can override; nobody has. Aggregate fire rate dropped 18%. Aggregate dismissal rate dropped from 22% to 7%.

## What we learned

Two things stood out.

**Default scoping matters more than rule logic.** The detection logic for bare-except is a one-line regex. It hasn't changed. What changed is *where the rule applies*. Most rule-tuning work in Beacon is calibration on scope, not on detection. We knew this in theory; the bare-except episode made us internalize it.

**Customer dismissal data is the calibration signal.** We had been treating dismissals as noise (people reject our findings, fine). They're actually the highest-quality calibration data available. The customer is doing the rule-evaluation work for us, by hand, with full context. Beacon now feeds dismissal patterns back into the rule-tuning queue automatically. If a rule's dismissal rate crosses 25% across at least three customers, the rule appears in our weekly tuning review.

## What didn't change

The rule itself. Bare-except is still wrong in production code. We didn't soften the message or downgrade the severity. The fix was strictly scope, not stance.

There's a temptation when a rule misfires to weaken it. *"Maybe we should warn instead of error."* Almost always the wrong move. If the rule is right, the rule is right. The question is *where* it applies.

## The next bare-except story

Hugo's working through the same calibration on the async-correctness rule pack now (PYL-104) — the next 30 Python rules. We're shadow-moding each one against the last 30 days of customer PRs before promoting. First batch shipped at 6.4% aggregate FP rate. The remaining 20 are in flight; we expect a couple of them to need rescoping based on what we learn from the first cohort.

Reviewer attention is the scarcest thing we work with. Treating it that way is the hard part.

— Hugo
