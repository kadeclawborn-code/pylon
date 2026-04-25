---
id: 013
account: acct_strato
customer_user: user_strato_001
pylon_agent: emp_032
channel: chat
status: resolved
opened_at: 2026-02-13T15:00:00Z
closed_at: 2026-02-27T16:00:00Z
category: [feature-request, dashboard, beacon]
---

**Customer (Theo Brennan):**

Tom — the rules listing page in the dashboard is great for browsing, but I can't see fire rate per rule (how often each rule fires across our recent PRs). I know which rules I'd tune if I had that data. Can we get it surfaced?

We have ~280 rules enabled. I can guess at the worst offenders but I'd rather see the data.

---

**Tom:**

Theo — totally reasonable ask, and a clean lift on our side. Existing fire-rate data is captured in Tower; just hasn't been surfaced on the rules page. Filing as a feature request.

Quick win possible — give me a sprint or two.

---

**Customer:**

Thanks. Anything to flag in the data while we wait? Like, is there a query I could run or a Tower view I'm missing?

---

**Tom:**

Tower's existing "Findings → By Rule" view sort of has it but not in the rule-detail context where you'd want it. You can see top-firing rules but can't sort the rule list itself by fire rate.

Workaround: Tower data export → pivot in your spreadsheet of choice. Bit of friction but available now.

---

**Customer:**

I'll wait for the proper UI. Not blocking; just inefficient.

---

**Tom (2 weeks later):**

Theo — shipped. PYL-224 if you're tracking. Rules listing page now shows fire rate per rule (last 30 days). Sortable. "Tune this rule" link if FR > 15%.

---

**Customer:**

Looking now. This is exactly what I wanted. Two rules at 22% and 18% FR — high enough that I'm dropping them into shadow mode for a week to see where the dismissals concentrate. Will report back if anything noteworthy.

Thanks Tom.

> _internal_: this is the kind of small UX ask that compounds. Saving Theo 30 min/quarter; he flagged it in the QBR thanks-message.
