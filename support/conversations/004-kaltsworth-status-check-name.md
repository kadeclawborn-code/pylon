---
id: 004
account: acct_kaltsworth
customer_user: user_kalt_003
pylon_agent: emp_033
channel: email
status: resolved
opened_at: 2026-03-19T09:22:00Z
closed_at: 2026-03-27T17:00:00Z
category: [feature-request, switchyard, ci]
---

**Customer (Joaquín Reséndez):**

We have an internal CI gate that's also named "Pylon" (named after our dispatch system, predates Pylon-the-tool). The two collide on PR status checks. Can the Pylon-tool status check name be renamed? We can't rename our internal CI without a quarter of coordination across teams.

---

**Bridget:**

Joaquín — yes, that's a sensible ask. Today the status check name is hardcoded to "Pylon" but it should be customizable. Filing as a feature request.

Workaround in the meantime: GitHub allows multiple status checks with the same name from different sources (us + your internal one will both appear), but the merge-block enforcer config applies to whichever one is configured as required. If you set our status check name to "Pylon (lint)" via temporary GitHub branch protection rules, you can disambiguate in your UI without us shipping anything.

Not great. We'll prioritize the rename.

---

**Customer:**

Thanks. We'll wait for the proper fix; the GitHub UI workaround is a time-tax for our reviewers.

---

**Bridget:**

Reasonable. I'll let you know when it ships.

> _internal_: filing PYL-225. Three other customers have asked the same thing. Easy lift; should clear in a sprint.

---

**Bridget (8 days later):**

Joaquín — shipped. Settings → Integrations → "Pylon status check name" field. Default is still "Pylon" so existing customers see no change. Validation: alphanumeric + dashes, max 30 chars. Goes live for your org as soon as you save.

---

**Customer:**

Configured. We're using "pylon-review" to disambiguate. Working. Thanks Bridget.
