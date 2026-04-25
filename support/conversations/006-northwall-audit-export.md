---
id: 006
account: acct_northwall
customer_user: user_north_004
pylon_agent: emp_033
channel: email
status: resolved
opened_at: 2026-02-19T13:47:00Z
closed_at: 2026-02-25T16:30:00Z
category: [bug, dashboard, audit, performance]
---

**Customer (Tobias Akkerman):**

Trying to export 12 months of audit logs for our compliance team. Browser hangs at ~30 seconds and times out. Tried twice. Smaller windows (3 months) work fine. We have ~150k audit log entries.

Same audit logs we already use for our internal reviews so the data IS there — just can't get it out at the volume we need.

---

**Bridget:**

Tobias — that's a known pain point at your scale. Two things:

1. The page-level query has a 30-second cap (we don't kill it; the browser does). Background-job-based export was on the roadmap; this conversation moves it up. Can you wait 5 days for a fix?
2. Workaround in the meantime: I can run the export server-side and email you the CSV. Takes ~15 minutes for 150k rows. Would that get you through this week's compliance review?

---

**Customer:**

Yes please run server-side. Window we need: 2025-02-19 to 2026-02-19, all event types, all actors. CSV.

---

**Bridget:**

Running. I'll email when ready (signed link, valid 24h).

> _internal_: filing PYL-303.

---

**Bridget:**

Sent. 14 minutes. ~150k rows, 23MB CSV.

---

**Customer:**

Got it. Compliance team has it. Thanks Bridget.

What's the timeline on the proper fix?

---

**Bridget:**

Fix is in this sprint (PYL-303 if your team's tracking). Two changes:

1. Page-level query window capped at 30 days at the UI layer (so customers don't hit the 30s cap unintentionally)
2. Anything beyond 30 days flows through a background export job that emails the result when ready

Should land within 5 days. I'll let you know.

---

**Bridget (3 days later):**

Tobias — fix shipped. UI now caps at 30 days; longer windows route to export automatically. The dialog shows estimated time when you start the export.

---

**Customer:**

Exported a 12-month window again. Worked. 9 minutes. Got the email. Thanks.
