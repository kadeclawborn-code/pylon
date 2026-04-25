---
id: 010
account: acct_verdant
customer_user: user_verdant_004
pylon_agent: emp_032
channel: email
status: open
opened_at: 2026-04-22T14:08:00Z
category: [sales, enterprise, saml]
---

**Customer (Hugo Restrepo):**

Tom — Sigrún's signing off the GitLab pilot. As we move from pilot to production, my piece of the work is the security/IT readiness. Two things on our side:

1. We need SAML SSO for any tool that touches our codebase. Our IdP is Okta. What's Pylon's SAML support look like, and is there an Okta-specific guide?
2. We need an audit log of administrative actions in Pylon (rule changes, member changes). Required for our internal SOC 2 in flight.

Both of these are Business+ tier per your pricing page, so I assume an Enterprise upgrade is the path. What's the rough cost difference for our 65-engineer team?

---

**Tom:**

Hugo — sensible plan. Both are squarely available:

1. **SAML SSO** — Business and Enterprise tiers. Okta-specific setup guide: https://pylon.dev/docs/saml/okta. ~30 min walkthrough; happy to pair on it during your transition.
2. **Audit logs** — same tier gating. 1-year retention on Business, 7-year on Enterprise. SOC 2 evidence portal access is Enterprise-only.

Your current Team-tier MRR is $1,885 (65 devs × $29). Business at the same headcount would be $3,835/mo (65 × $59). Enterprise pricing depends on the deployment topology and SLA we agree on. For Verdant's profile (single-region, GitLab Cloud, no on-prem), I'd expect Enterprise to land in the $4,500-$5,500/mo range — roughly 2.5-3x your current Team rate.

If audit-log retention beyond 1 year matters, Enterprise is the right tier. If 1 year is enough, Business gets you SAML + audit logs + the Tower data API at lower cost.

Let me know which direction. I can loop in Dave (sales) for the contract piece once you've decided.

---

**Customer:**

Will discuss with Sigrún and reply by end of next week.

One more: when does EU data residency ship? We have one EU-based customer (small but high-stakes) and they've asked about us specifically.

---

**Tom:**

EU residency ships Q1 2027 for Enterprise customers. Pre-orders welcome — meaning we'd commit to your slot at the planned per-developer rate when it lands. Doesn't affect your current decision; we'd serve from us-east-1 until eu-west-1 is live in early 2027 (regardless of which tier you upgrade to now).

---

**Customer:**

Got it. Will be in touch.

> _internal_: this is the path we expected. Likely Enterprise upgrade given the audit-log retention + EU residency signals. Dave should be looped in this week to start contract groundwork.
