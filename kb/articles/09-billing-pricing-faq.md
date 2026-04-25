# Billing & pricing FAQ

Common billing questions, with direct answers.

## Plan tiers

| Plan | Price | Best for |
|---|---|---|
| Free | $0 | Solo developers, small teams |
| Team | $29/dev/month | Engineering teams who want full Pylon on private repos |
| Business | $59/dev/month | Orgs that need custom rules, SSO, and audit trails |
| Enterprise | Custom | Large orgs with compliance and contractual needs |

Full plan comparison at pylon.dev/pricing.

## What counts as an "active developer"?

A developer is "active" in a billing month if they authored OR reviewed at least one PR in any repo connected to your Pylon org during that month.

- **Lurkers / observers** — don't count
- **CI service accounts and bots** — don't count
- **Multi-account humans** (if a human has two GitHub accounts) — count once
- **Contractors / freelancers** — count if they were active

We auto-detect activity from PR data. You don't manually mark people active or inactive.

## How is the bill calculated?

We count active developers at the **end** of the billing month, then bill at your tier's per-dev rate.

- Team: end-of-month count × $29
- Business: end-of-month count × $59

Annual contracts (15% discount) are settled at signing based on a forecast headcount and reconciled annually.

## What happens if my count goes up mid-month?

Pylon doesn't pro-rate within a billing month. If you add 5 developers on day 1 of the month, they're counted at end-of-month. If you add them on day 27, same — counted at end-of-month.

If your headcount has a sudden large jump that affects forecasting, talk to your CSM or sales — we can adjust mid-cycle for unusual situations.

## What happens if my count goes down mid-month?

Same model — end-of-month count. If you reduce headcount, your next month's bill is lower.

## Free trial

Team and Business have a 14-day free trial. No credit card required to start. At day 14, if you haven't entered billing info, your account moves to Free (with the 5-dev cap).

We email at days 7, 12, and 14 so the transition isn't a surprise.

Enterprise trials are negotiated per-deal — typically 30 days with full access including SOC 2 evidence portal.

## Can I downgrade?

Yes, at any billing-cycle boundary.

- **Business → Team**: custom rules become read-only (you can read but can't run them); Tower data API access stops; SSO falls back to GitHub OAuth.
- **Team → Free**: 5-dev cap kicks in; private repos no longer analyzed (only public).

Pylon doesn't aggressively try to retain you on a higher tier. If you downgrade, that's your call.

## Can I upgrade?

Yes, immediately. Upgrades are pro-rated.

## Refunds

Cancel any time. Pylon refunds the unused portion of any prepaid annual term, prorated to the day of cancellation. No questions, no retention escalation calls. (We don't run a "save the customer" playbook.)

## Payment methods

- **Self-serve**: credit card via Stripe
- **Enterprise**: Net 30 / Net 45 invoice billing; ACH / wire

We don't accept crypto. We don't accept POs without a contract (so this is Enterprise-only).

## Discounts

- **Annual billing**: 15% discount (Team and Business)
- **OSS / non-profit / education**: handled case-by-case. Email dan@pylon.dev with details.
- **Multi-year**: negotiable for Enterprise. Talk to sales.

## Currency

USD only. We invoice in USD even for non-US customers. Your bank handles the conversion.

## Tax

We charge sales tax based on your billing address (US states where required). For non-US customers, you may be responsible for VAT/GST in your jurisdiction; we do not collect it.

## Common questions

**My team has a hire who only reviews PRs (doesn't author). Are they billed?**

Yes — reviewing counts as activity.

**Can I exclude a specific user from billing?**

No. Active = active. If you want a user not to count, they shouldn't be reviewing or authoring PRs in the connected repos.

**What about contractors who only work for one quarter?**

They count for the months they're active. Contracting arrangements aren't special-cased.

**Do you charge per-PR or per-finding?**

No. Per-developer regardless of activity volume.

**Is there a free tier limit on rule fire counts?**

No. Free tier has a 5-dev cap and is restricted to public repos, but no rule fire metering.

**Does the Marketplace cost extra?**

No. Subscribing to Marketplace rules is free across all tiers. Publishing requires Business or Enterprise tier (because authoring custom rules requires Business+).

## More

Full pricing FAQ: pylon.dev/pricing#faq
Sales contact: dan@pylon.dev
Support contact: bridget@pylon.dev
