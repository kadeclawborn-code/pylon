---
id: 001
account: acct_lumen
customer_user: user_lumen_001
pylon_agent: emp_033
channel: email
status: resolved
opened_at: 2025-10-29T08:14:00Z
closed_at: 2025-10-31T17:30:00Z
category: [bug, switchyard, urgent]
---

**Customer (Bea Okafor):**

Bridget — sending this at 5am ET because we have a week of PRs landing without Pylon comments and our security review is Friday. Our security team forced a fresh GitHub App install three weeks ago after their quarterly audit. Since then, nothing from Pylon. We assumed it was a quiet patch but checked today and our test corpus has obvious things that should have triggered Beacon's default ruleset. Logs on our side show GitHub firing webhooks; Pylon dashboard still says "all systems normal."

What's going on?

---

**Bridget:**

Bea — good morning. On it. Looking at our webhook ingest log right now.

Confirmed: we're not receiving webhook events from your installation. The reinstall path doesn't re-register webhook subscriptions in our current build — only the initial install does. That's a real bug on our side. Engineering has it; fix is going out today.

For the immediate week of missed PRs: we don't replay historical webhooks (Pylon is a forward-looking tool by design). I can run Beacon synchronously over the past 7 days of PRs in your top three repos so your security review on Friday has signal. Want me to?

---

**Customer:**

Yes please. Top three repos are `lumen-clinical`, `lumen-platform-api`, `lumen-edge`.

---

**Bridget:**

Running now. ~25 minutes for the three repos combined.

Findings will appear in your dashboard under Reports → On-Demand Scans (it's a bit of a quiet feature; Adetokunbo can find it under Settings → Reports). I'll email when done.

> _internal_: filed PYL-300 + the backfill plan with engineering. Identifying all customers with `installation_repositories.added` in our log over past 90 days where webhook subscription is missing. ~11 affected. Backfilling all once the fix merges.

---

**Customer:**

Got the email. Reviewing now. Three real things flagged in `lumen-clinical` we missed in review. Thank you.

When does the fix ship?

---

**Bridget:**

Fix merged 15 minutes ago. Backfill running for your install + 10 other affected customers. You should see live webhook events flowing again within the next hour.

I'll send a confirmation once your live stream is working.

---

**Bridget (one day later):**

Bea — confirmation. Live stream working since 18:42 ET yesterday. Three new PRs since then have Pylon comments. Closing this out.

We're filing a public postmortem about this on the engineering blog next week. The framing is "we hardcoded an event-handler list and didn't think about reinstall paths." I'll send you the draft if you want to redline.

---

**Customer:**

No need. Thanks for the speed.

> _internal_: high-trust account; the speed mattered for renewal. CSM (also Bridget per the original CS routing) flagged this in the next QBR notes.
