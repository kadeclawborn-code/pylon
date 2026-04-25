---
id: 005
account: acct_verdant
customer_user: user_verdant_002
pylon_agent: emp_032
channel: chat
status: resolved
opened_at: 2026-04-16T10:34:00Z
closed_at: 2026-04-23T15:11:00Z
category: [bug, switchyard, gitlab]
---

**Customer (Ekene Amadi):**

Tom — found something. Pylon's posting two of the same comment on some MRs. Saw it on MR !314 and MR !328 in our `verdant-platform` repo. Same finding, same line, two posts. Repro should be straightforward — looks like a retry that didn't dedupe.

---

**Tom:**

Ekene — confirmed on our side. Looking at the MR you linked. It's a real bug in our GitLab integration. The GitHub side has built-in idempotency from the Reviews API; the GitLab Notes API doesn't, and we didn't add a manual dedupe layer. So when our analyzer pipeline retries on transient failure, the comment poster goes through twice.

Engineering's on it. Going out before the GitLab GA push at end of sprint.

---

**Customer:**

Cool. Not a blocker on our side — just noting since you said you wanted pilot signal early and often.

---

**Tom:**

Exactly the signal we wanted. Filing as PYL-305.

> _internal_: this is the kind of bug pilot is for. Pre-GA fix will land; pilot continues.

Couple of follow-ups if useful for the pilot retro:
1. Are duplicates causing reviewer noise on your side? Want to make sure I'm not under-rating impact.
2. Anything else surfacing that I should track?

---

**Customer:**

1. Mild noise — reviewers ignore the duplicate, but it's the kind of polish gap they'd notice if we were shipping this internally. Worth fixing.
2. One other thing: when we revoke and re-grant the GitLab OAuth scope, the Pylon dashboard sometimes doesn't pick it up for ~5 minutes. Status hangs at "reconnecting." Has happened twice; both times it cleared after a refresh. Logging it here in case it's a real signal.

---

**Tom:**

Logged the second one as a follow-up. Probably worth a 2nd ticket once we have a repro path.

> _internal_: feels like our OAuth refresh dashboard signal lags by a heartbeat cycle. Filing as a follow-up; not urgent.

---

**Tom (one week later):**

Ekene — PYL-305 fix is in. GitLab MR comment idempotency layer landed yesterday. Targeting a verify pass on your end this week if you have time.

---

**Customer:**

Verified on three MRs. No duplicates. Closing this out.

> _internal_: pilot signed off (separately, by Sigrún). Renewal track now Enterprise upgrade-track. Sales (Dave) running.
