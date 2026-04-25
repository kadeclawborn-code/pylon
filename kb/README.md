# Knowledge Base

> 10 customer-facing help articles. Voice per `BRAND.md` (direct, technical, no exclamation points, no banned phrases). These represent a starter knowledge base — a real Pylon would have ~30-50 articles after a year. The 10 here cover the most-frequently-cited support topics.

## Articles

| File | Topic | Audience |
|---|---|---|
| `01-getting-started.md` | First 15 minutes — signup to first comment | New customers |
| `02-installing-pylon.md` | Installing the Pylon GitHub App / GitLab integration / Bitbucket | All |
| `03-pylon-yaml-reference.md` | `pylon.yaml` config schema | Engineers configuring rules |
| `04-authoring-custom-rules.md` | Writing Beacon custom rules in PRL | Rule authors |
| `05-suppressing-false-positives.md` | When and how to suppress findings | Reviewers |
| `06-tower-dashboard-reference.md` | Tower charts, metrics definitions, what each one means | Eng managers |
| `07-marketplace-guide.md` | Browsing, subscribing, publishing in the Beacon Rule Marketplace | All |
| `08-audit-log-export.md` | Exporting audit logs (CSV / JSON, large windows) | Compliance, Business+ tier |
| `09-billing-pricing-faq.md` | Plan tiers, what counts as an "active developer", billing | All |
| `10-troubleshooting-pylon-not-commenting.md` | When Pylon stops commenting on PRs | All |

## Conventions

- Each article opens with the answer; explanation follows
- Code blocks have language tags; outputs use plain `text`
- Links go to `pylon.dev/docs/<slug>` for the canonical doc, never to internal-only paths
- Examples reference real-feeling repo paths (`backend/api/users.py`) rather than generic `foo.py`
- Voice is "engineer to engineer" — don't over-explain
- No screenshot dependencies (KB articles must work as text alone)

## Article authorship

Internal: most articles drafted by Esther (DevRel) or Lila (Content), reviewed by Wei (Beacon-related) or Camille (Tower-related), with Bridget (Support) signing off on customer-facing language.
