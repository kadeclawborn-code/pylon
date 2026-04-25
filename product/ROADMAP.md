# Pylon — Roadmap

| | |
|---|---|
| Window | Q2 2026 → Q1 2027 (4 quarters forward) |
| Status | Active |
| Owner | Olivia Reyes (CPO) |
| Reviewed | Quarterly with engineering leadership; biannual with the board |
| Last updated | 2026-04-25 |

> Themes are durable; line items are commitments at the start of each quarter and may shift mid-quarter as customer signal lands. Strikethrough indicates an item that was on a quarter and got cut, with a brief note on why.

---

## Q2 2026 — *"Beacon ships marketplace and GitLab"* (current quarter)

**Theme:** Make custom rules easier to share and ship Pylon's second platform integration.

- [x] **Beacon Rule Marketplace (public preview)** — customers can publish their custom rules; other customers can subscribe. *Done early April; iterating on rate-of-adoption signals.*
- [ ] **Switchyard for GitLab Cloud (GA)** — full feature parity with the GitHub integration. *In flight; launch tracked for early May.*
- [ ] **Tower team-comparison views** — engineering managers can compare review-quality metrics across teams within their org without exporting data. *Mid-quarter.*
- [ ] **Beacon: 30 new Python rules** — focus on async-correctness patterns from the customer-pain log. *Late quarter.*
- [ ] **Pricing: rate-card refresh** — Business tier gains audit logs by default (was Enterprise-only); $59 → $59 (price hold, value increase). *Mid-quarter.*

---

## Q3 2026 — *"SOC 2 Type II + Tower data API"*

**Theme:** Compliance moat and analytics extensibility.

- **SOC 2 Type II completion** — second-half of the audit window closes early Q3; Type II report available to Enterprise prospects by end of quarter. *Renata + Amir co-sponsor.*
- **Tower data API (REST, beta)** — customers can pull their review data into their own warehouse (Snowflake, BigQuery, Redshift). Resolves OQ-2. *Camille leads.*
- **Beacon: Java language support (preview)** — first non-dynamic-typed language. Wei + Hugo lead. Critical for the mid-market customers Pylon's been turning away. Resolves part of OQ-5 (decided to hire, not acquire).
- **Switchyard: Bitbucket Cloud (GA)** — completes the three-platform set committed at Series B.
- **Customer-facing audit log** — every Beacon rule change, every dashboard config change, who/when. Required for SOC 2 Type II evidence; useful in sales calls.
- **Beacon: Python rule sunset cycle** — deprecate ~20 rules from the original 2022 default ruleset that have proven low-value (FP rate >25%, dismissal rate >60%). Painful but right.

---

## Q4 2026 — *"AI-suggested fixes (gated beta) + tighter eng-leader workflow"*

**Theme:** First step into AI-augmented review; deepen the dashboard's value to engineering managers.

- **Pylon Suggest (gated beta)** — for a subset of Beacon rules where the fix is mechanically determinable, Pylon proposes a one-line patch as part of the comment. Behind feature flag, opt-in per customer. Wei + Priya co-lead. Will not ship to GA in 2026; the bar for GA is "rule semantics so well-understood that a wrong-suggestion is rare enough not to break the brand."
- **Beacon: C# language support (preview)** — second new language. Lower priority than Java but tracking customer ask.
- **Tower: workforce planning view** — for engineering directors. Headcount-vs-PR-throughput modeling. Tom and Camille designed it during a customer-research sprint.
- **Slack-native digest revamp** — daily Pylon digest in Slack becomes interactive (one-click drill-in, one-click rule-tweak). Slack is the most-engaged Tower surface.
- **Onboarding redesign** — get time-to-first-comment under 15 minutes (currently 22). Felix + Tomás lead.

---

## Q1 2027 — *"EU region + rule-conflict resolver + acceleration prep"*

**Theme:** Enterprise-grade geographic coverage and Beacon depth maturity.

- **EU data residency** (eu-west-1 region) — required by 4 named Enterprise prospects. Resolves data-residency objections in the sales pipeline.
- **Beacon Rule Conflict Resolver** — when two rules disagree (one says "use this pattern," another says "avoid that pattern"), Pylon detects and helps the customer choose. Surfaces in Beacon's authoring UI.
- **Pylon Suggest (broader beta)** — opens the gate from ~20% of customers (Q4) to ~60%. Still not GA.
- **Beacon: Go rule expansion** — close the gap with Python; Go was treated as Tier 2 in 2025, ready to be Tier 1.
- **Pricing: enterprise consumption pilot** — for two Enterprise customers, trial consumption-based pricing (per-PR-analyzed) instead of per-dev. Outcome feeds into OQ-6.

---

## Beyond — directional only, not commitments

These are *intent*, not commitments. Items here may be reordered, deferred, or killed.

- **GitLab self-hosted (Enterprise)** — only if EU expansion proves out and Bitbucket Cloud customer count justifies the integration cost. Owner: Olivia + Jordan to scope late 2026.
- **Pylon Suggest GA** — gated on rule-semantics confidence; possibly H2 2027.
- **JavaScript/TypeScript framework-aware rules** — React-specific, Vue-specific, Svelte-specific rule packs. Customer-pull-driven.
- **PRDB (Pylon Review Database)** — anonymized cross-customer review patterns for industry benchmarking. Privacy and contractual review pending. Sasha and legal own this exploration.
- **Multi-region for Tower** — beyond Enterprise EU, regional analytics warehouses for compliance customers. Probably 2027 H2 at earliest.

---

## What's not on the roadmap (and why, briefly)

These come up in customer conversations and are not on the roadmap:

| Ask | Why not |
|---|---|
| IDE plugin (VS Code, JetBrains) | See PRD non-goals — different product, dilutes focus |
| AI code-quality scoring | We don't generate quality scores; misleading framing |
| Self-hosted Free/Team tier | Enterprise-only on-prem keeps support burden manageable |
| Bitbucket Server | Cloud-only by deliberate scope choice |
| ML notebook (.ipynb) review | Reviewable artifact unclear; rule semantics weak |
| General CI replacement | Pylon is one stage of CI, not all of it |

If a prospect asks about any of these, the answer is "no" with the rationale above. CRO and CMO have the talking points.

---

## How this roadmap is built

Quarterly roadmap planning happens the last two weeks of each quarter:

1. **Inputs collected:** customer asks (logged by Customer Success in Salesforce), engineering capacity (Priya + Jordan), competitive pressure (Mei + Lila log), Tower-derived insight on what customers actually use vs. ignore.
2. **Olivia drafts** the next quarter's themes and 5–8 line items.
3. **Eng leadership review** with Priya, Jordan, Wei. Cuts what's overcommitted.
4. **Marcus signs** the final cut.
5. **All-hands** the new quarter on the Tuesday after, with a slide for each line item.

The roadmap doc you're reading reflects the most recent finalized version. In-flight discussions live in `product/roadmap-drafts/<quarter>.md` (if any).
