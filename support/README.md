# Support Conversations

> 15 multi-turn support conversations between Pylon's CS team and customer users. Format: markdown with a metadata header. References to users and accounts resolve to `customers/users.json` and `customers/accounts.json`.

## Why these exist

Real support data is the most realistic proxy for "what does customer interaction look like?" — and the hardest to synthesize convincingly. AI POCs that triage, route, summarize, suggest responses, or detect churn signals from support data need conversations with the texture of real ones: incomplete information, multi-turn back-and-forth, occasional misdirection, mixed tone.

The 15 conversations here are crafted to cover that range. Some are short (one round of clarification + answer). Some are long, multi-day, multi-channel escalations. Some end clean; some end in a handoff to engineering.

## Conventions

Every conversation file:
- Has a YAML frontmatter block with `id`, `account`, `customer_user`, `pylon_agent`, `channel`, `status`, `opened_at`, `closed_at` (or `null` if open), and `category` tags
- Opens with the customer's first message
- Body uses `**Customer:**` and `**Pylon:**` speaker prefixes (sometimes the Pylon side is named — e.g., `**Bridget:**`)
- Internal notes (visible to Pylon team but not customer) appear as `> _internal_:` blockquotes

## Index

| ID | Customer | Topic | Status |
|---|---|---|---|
| `001` | Lumen Health | GitHub App reinstall — no comments appearing | resolved |
| `002` | Arcola Studios | python.bare-except false positives in tests | resolved |
| `003` | Stratosphere | Custom rule authoring help | resolved |
| `004` | Kaltsworth | Status check name collision with internal CI | resolved |
| `005` | Verdant Energy | GitLab MR — duplicate Pylon comments | resolved |
| `006` | Northwall Financial | Audit log export performance | resolved |
| `007` | Stratosphere | Tower team-comparison feature request | resolved |
| `008` | Patchwork Climate | Onboarding guide question | resolved |
| `009` | Lumen Health | Java timing question | resolved (with caveat) |
| `010` | Verdant Energy | SAML SSO availability + Enterprise upgrade path | open |
| `011` | Arcola Studios | C# coverage timeline | resolved (with caveat) |
| `012` | Northwall Financial | SOC 2 Type II evidence portal availability | open |
| `013` | Stratosphere | Per-rule fire rate visibility | resolved |
| `014` | Patchwork Climate | First custom rule fails on test corpus | resolved |
| `015` | Lumen Health | Beacon false positive: jolene's dismissal pattern | resolved |
