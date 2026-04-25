---
id: 008
account: acct_patchwork
customer_user: user_patch_003
pylon_agent: emp_033
channel: chat
status: resolved
opened_at: 2026-02-12T09:18:00Z
closed_at: 2026-02-12T09:42:00Z
category: [help, onboarding]
---

**Customer (Boris Cardoso):**

Hi — just joined Patchwork last week, getting up to speed. We use Pylon (Solange installed it). I see Pylon comments on PRs but I don't really know what's expected of me as a reviewer. Is there a quick guide?

---

**Bridget:**

Welcome Boris. Three short things:

1. Pylon's comments are advisory, like a teammate's review comments. You can resolve them, dismiss them, or ignore them.
2. If you think a comment is a false positive, dismiss it with the "false positive" reason — that data feeds back into our calibration.
3. If you think a comment is right, either fix the issue or leave a reply explaining why you're choosing not to (e.g., "intentional in this case because X").

Also: if you ever see a Pylon comment that feels condescending or unhelpful, please flag it to me directly. We tune for engineering-respectful tone and we want to know when we miss.

KB article that covers this end-to-end: https://pylon.dev/docs/being-reviewed-by-pylon

---

**Customer:**

That's exactly what I needed. The KB article works. Thanks.

(Side note: my first PR review on this team had a Pylon comment that caught a real bug — I was forgetting to await an httpx call in a hot path. Felt like having a senior engineer next to me.)

---

**Bridget:**

That note made my day. Mind if we use it (anonymized) in our onboarding research?

---

**Customer:**

Sure, attribute to "early-tenured engineer" if that works. No need to anonymize my name but no need to use it either.

---

**Bridget:**

Thanks Boris. Quote going in.

> _internal_: this is the quote Esther referenced in #193 (the Pylon-on-Pylon retrospective). Feeds onboarding research.
