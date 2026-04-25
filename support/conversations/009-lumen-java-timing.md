---
id: 009
account: acct_lumen
customer_user: user_lumen_003
pylon_agent: emp_032
channel: email
status: resolved-with-caveat
opened_at: 2026-02-19T15:30:00Z
closed_at: 2026-03-04T11:00:00Z
category: [feature-request, beacon, language-coverage]
---

**Customer (Naseem Khan):**

Tom — checking in on Java timing. We're 18 months into Lumen's Pylon usage; love it on the Python and TS side; our Java codebase (~40% of our backend) gets nothing. We've been running SonarQube alongside for the Java parts. Increasingly the team's asking when we can consolidate.

What's the realistic Q3 2026 timeline for Java?

---

**Tom:**

Naseem — direct answer: Q3 2026 is the target for Java *preview*, not GA. Preview means default-off, opt-in per repo, with the customer aware that rule coverage is partial and FP rate is calibrated against an early customer corpus.

Realistic GA: late Q4 2026 to early Q1 2027, depending on the preview signal.

I know that's not the answer you wanted. Two things:

1. We're hiring (not acquiring) for Java — decision made in March after a survey. Hiring takes months. Our Java preview will be smaller and slower-shipping than your team would prefer.
2. If Lumen's renewal in August is going to hinge on Java, please let me know now so Renata and I can plan. We don't want to surprise you, and we don't want you to surprise us.

---

**Customer:**

Honest. I'll relay to Bea.

Question: if we wanted to be a preview customer (i.e., shape the rule corpus for Java in exchange for early access), what's that look like?

---

**Tom:**

We'd love that. Concretely:

1. We onboard Lumen's Java repos for the preview when it ships
2. Your team uses it; we collect FP/dismissal data and rule-impact data
3. Wei's team prioritizes rule fixes against your corpus
4. Net effect: your team gets earlier-and-less-noisy Java coverage than the broader market; we get a calibration signal

There's no extra fee. It's a beneficial exchange.

I'll loop in Wei + Renata to formalize the partnership ahead of the preview ship date.

---

**Customer:**

Sounds good. Will tell Bea.

> _internal_: closing as resolved-with-caveat — answer's clear, customer's reasonable, but the renewal-risk piece is real and Renata needs to track it through Q2.
