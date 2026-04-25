---
id: 014
account: acct_patchwork
customer_user: user_patch_001
pylon_agent: emp_033
channel: chat
status: resolved
opened_at: 2026-03-08T16:18:00Z
closed_at: 2026-03-08T16:55:00Z
category: [help, beacon, custom-rules, marketplace]
---

**Customer (Solange Mahler):**

Hi Bridget. Wrote our first custom rule for Patchwork — flags any uncached `httpx.AsyncClient()` instantiation in our hot path. Tested in preview mode; flags 4 real issues. About to publish to the public Marketplace as our first contribution.

Two questions before I hit publish:

1. Does the Marketplace listing show our org name? Some folks at Patchwork prefer to keep our customizations internal.
2. Once published, can we revoke?

---

**Bridget:**

Solange — answers:

1. Yes, the publishing org is shown by default. There's an "anonymous" option in the publish form if you want to publish without org attribution. Trade-off: no attribution means subscribers can't reach out to you with questions, and the rule has slightly less weight in the marketplace's signal-density metrics.
2. Yes — you can unpublish at any time from the rule's detail page. Existing subscribers keep the version they have; unpublishing means no new subscribers can sign up. We don't force-revoke from existing subscribers because that would break their builds; that's a deliberate trade-off.

If you want an opinion: publish with attribution. Patchwork has good signal already (your CTO's contributed to other Beacon rules in the past); your name carries reputation.

---

**Customer:**

Going with attribution. Publishing.

(Actually published while typing the above response — confirming it's live now in Marketplace. Looking at the listing... clean. Thanks.)

---

**Bridget:**

Confirmed. Listed under Patchwork Climate. 0 subscribers as of right now (which is normal for the first 24 hours). I'll keep an eye on adoption signal in case there's anything to flag.

---

**Customer:**

Thanks. Ping me if a subscriber has questions — happy to help calibrate.
