# Pricing

> Source content for the public pricing page (pylon.dev/pricing). Voice per `BRAND.md` — direct, no exclamation points, no banned phrases. Numbers are canon and align with the Master PRD.

---

## Plans

Four tiers, per-developer pricing on paid plans. No seat minimums on Free or Team. Pricing is in USD.

### Free — $0

For solo developers and small teams getting started.

- Up to **5 active developers**
- **Public repos only**
- **Beacon** — default rule pack (Python, TypeScript, Go, JavaScript, Ruby)
- **Tower** — basic cycle-time view, 14-day history
- **Switchyard** — GitHub Cloud only on Free
- Community support (GitHub issues, public docs)

### Team — $29 / developer / month

For engineering teams who want full Pylon on private repos.

- **Unlimited developers**
- **Public + private repos**
- **All Beacon default rules** + ability to enable / disable individual rules
- **Full Tower** — all dashboards, full history retention, Slack/email digests
- **Switchyard** — GitHub Cloud, GitLab Cloud, Bitbucket Cloud
- Email support, 1 business day response

Annual billing available, 15% discount.

### Business — $59 / developer / month

For organizations that need custom rules, SSO, and audit trails.

- **Everything in Team**, plus:
- **Custom Beacon rules** — author your own rules in PRL, no rule count limit
- **Beacon Rule Marketplace** access (subscribe to rules other customers publish)
- **SAML SSO**
- **Audit logs** — every rule change, every config change, every dashboard view
- **Priority support** — email + chat, 4 business hour response
- **Tower data API** (read-only export to your warehouse — Snowflake, BigQuery, Redshift, S3)

Annual billing available, 15% discount.

### Enterprise — Custom

For large organizations with compliance and contractual needs.

- **Everything in Business**, plus:
- **SOC 2 Type II evidence portal** — pull current evidence into your audit
- **Dedicated Customer Success Manager**
- **Contractual SLAs** — uptime commitment, support response commitment
- **Single-tenant deployment option** (single-tenant on AWS managed by Pylon)
- **On-premises option** (your AWS or your data center; Pylon-supported)
- **EU data residency** (available Q1 2027; pre-orders accepted)
- **Custom DPA**
- **Net 30 / Net 45 invoice billing**

Pricing is custom and tied to organization size, deployment topology, and SLA commitments. Talk to sales: dan@pylon.dev or pylon.dev/contact.

---

## What every plan includes

Every paying plan, including Team, gets:

- All Beacon language analyzers Pylon supports (Python, TypeScript, Go, JavaScript, Ruby today; Java preview Q3 2026; C# preview Q4 2026)
- Automatic rule updates — when Pylon ships a new default rule, you get it
- All Tower charts and metrics — no metering on dashboard usage
- Pylon's bug-bounty program coverage if you find a security issue
- Status page subscription, incident notifications

What we don't do on any plan:

- Charge per-PR or per-finding (we charge per developer, regardless of how active they are)
- Cap rule executions
- Cap data retention on Team or above
- Lock historical data behind upgrade gates

---

## FAQ

**Who counts as an "active developer"?**
A developer is active in a billing month if they authored or reviewed a PR in any repo Pylon is connected to that month. Lurkers, observers, and CI service accounts don't count. Multi-account humans count once.

**What happens at the end of the trial?**
Team and Business have a 14-day trial. At day 14, if you haven't entered billing info, your account moves to Free (with the 5-dev cap). No surprise charges; we'll email at days 7, 12, and 14.

**Do you have an annual discount?**
Yes — 15% off Team and Business when paid annually. Talk to dan@pylon.dev for terms.

**Do you offer discounts for non-profits / open source / education?**
Yes for active OSS projects with public repos: Free covers most needs. For larger OSS orgs or education, email dan@pylon.dev with details.

**Can I downgrade from Business to Team?**
Yes, at any billing cycle boundary. Custom rules will become read-only (you can read them but not run them); Tower data API access stops; SSO falls back to GitHub OAuth.

**Can I run Pylon on my own AWS account?**
Enterprise tier. Talk to sales.

**What about EU data residency?**
We're shipping eu-west-1 region in Q1 2027 for Enterprise customers. Pre-orders are accepted now and will be honored at the planned per-developer rate. US customers continue to be served from us-east-1.

**Do you support Bitbucket Server (self-hosted Bitbucket)?**
No, and it's not on the roadmap. Bitbucket Cloud is supported. See the Master PRD non-goals for rationale.

**Do you support self-hosted GitLab?**
GitLab Cloud is fully supported. Self-hosted GitLab Enterprise is being scoped for late 2026; sign up at pylon.dev/early-access if interested.

**Do you have a free trial of Enterprise?**
Yes, on a per-deal basis. Typical Enterprise trials are 30 days with full SOC 2 Type II evidence access. Talk to sales.

**What's your refund policy?**
Cancel any time; we refund the unused portion of any prepaid annual term, prorated to the day of cancellation. No questions, no retention escalation calls. (We don't run a "save the customer" playbook.)

**Where can I see actual prices and sign up?**
Free and Team are self-serve at pylon.dev/signup. Business requires a brief intro call with our team to verify scope. Enterprise is always custom.

**Is there a setup fee?**
No.

**Do you sell to government / public sector?**
Currently US commercial only. FedRAMP is not on our 2026 or 2027 roadmap.
