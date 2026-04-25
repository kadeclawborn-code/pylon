# Customers

> 7 paying customer accounts and 30 user personas across them. Source-of-truth fixtures for any AI agent reasoning about Pylon's customer base — sales conversations, support tickets, CS interactions, marketing case studies, billing scenarios.

## Files

| File | Contents |
|---|---|
| `accounts.json` | 7 customer account records (account profile, plan tier, MRR, health, usage signals, CSM mapping) |
| `users.json` | 30 user personas at those accounts (engineers, managers, security leads) |

## Distribution at a glance

| Account | Vertical | Plan | Engineers | MRR | Health |
|---|---|---|---|---|---|
| Stratosphere Robotics | Robotics | Business | 75 | $4,350 | 🟢 |
| Lumen Health | Healthtech | Enterprise | 180 | $13,400 | 🟡 |
| Kaltsworth Logistics | Logistics | Business | 120 | $6,960 | 🟢 |
| Verdant Energy | Climate | Team | 65 | $1,885 | 🟢 |
| Arcola Studios | Game dev | Team | 30 | $870 | 🟢 |
| Northwall Financial | Fintech | Enterprise | 250 | $18,200 | 🟢 |
| Patchwork Climate | Climate data | Team | 40 | $1,160 | 🟢 |
| **Total** | | | **760** | **$46,825** | |

## Cross-references

- Every `csm` field on accounts resolves to `org/employees.json` (Renata or Tom)
- Every `primary_contact` on accounts resolves to a `users.json` entry
- Every `account_id` on users resolves to `accounts.json`
- Customer names match BLUEPRINT.md flagship list; the additional two (Northwall, Patchwork) extend it
- `notes` fields cross-reference Paperclip ticket IDs (PYL-XXX) where customer asks tied to specific work
- Plan tiers, pricing math, and feature gating align with `product/pricing.md`

## How to use

For an AI POC reasoning about Pylon's customer base — say a churn-risk scoring POC, or a CSM-coverage-load analysis, or a Marketplace-publisher-of-the-quarter assessment — read both `accounts.json` and `users.json` and trace cross-references.

`support/conversations/` (in this same Tier 0 release) contains 15 multi-turn support tickets that reference these users by name and ID. `kb/articles/` contains 10 KB articles a user might be reading or referenced from a support ticket.

## Conventions

- All MRR figures are in cents (USD).
- All dates are ISO 8601 (YYYY-MM-DD).
- Health scores use Pylon CS's three-state convention: `green`, `yellow`, `red`. We don't model `at-risk` separately — it folds into yellow with a note.
- `expansion_potential` is a CS-side judgment field: `low` / `moderate` / `high`. Not for forecasting use; for prioritization.
- `usage_signals` are 30-day rolling.
- Free-tier customers don't appear here. Free is self-serve and Pylon doesn't track those at the account level beyond what the dashboard surfaces. For testbed purposes, assume Free customers are anonymous unless a POC explicitly needs them.
