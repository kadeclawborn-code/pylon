# Pylon v0.1.0 — Tier 0 release

> A synthetic B2B SaaS company built as an open-source benchmark substrate for AI agent tooling.

This is Pylon's first public release. It contains the Tier 0 substrate — enough scaffolding that an AI agent can be tested against a coherent, multi-domain enterprise without you writing fixtures from scratch.

## What's in v0.1.0

**Identity & brand**
- `IDENTITY.md` — fictional company facts (founding, funding, product subsystems Beacon / Tower / Switchyard, pricing, tech stack, year-by-year history)
- `BRAND.md` — voice principles, banned-phrase list, color palette, typography
- `org/employees.json` — 25 named personas across 7 departments
- `org/chart.md` — org chart with reporting peculiarities

**Product layer**
- `product/PRD.md` — Master PRD with 8 explicit non-goals, 5 user journeys, 3-subsystem architecture diagram, 6 named open questions
- `product/ROADMAP.md` — 4 quarters of commitments (Q2 2026 → Q1 2027)
- `product/pricing.md` — 4-tier pricing page with FAQ
- `product/competitive-analysis.md` — direct + adjacent competitors with honest win/loss accounting

**Engineering layer**
- `tickets/all.json` — 45 JIRA-shaped tickets across 14 sprints
- `tickets/sprints.json` — sprint metadata with themes
- `codebases/api/` — runnable FastAPI service representing Pylon's product runtime, with 12 source files, 5 working Beacon rule implementations, 30+ tests, CI workflows, issue + PR templates
- `codebases/api/HISTORY.md` — 31 synthetic commits across 6 months
- `codebases/api/CHANGELOG.md` — 15 versions in Keep-a-Changelog format
- `codebases/api/issues.json` — 50 GitHub-style issues
- `codebases/api/pull_requests.json` — 31 PRs with review threads

**Customer / support / docs**
- `customers/accounts.json` — 7 paying customer fixtures spanning Team, Business, Enterprise tiers
- `customers/users.json` — 30 user personas at those accounts
- `support/conversations/` — 15 multi-turn support conversations
- `kb/articles/` — 10 customer-facing help articles

## Cross-coherence

Every reference resolves. A persona named in the org appears as an author in PR review comments, as a CSM mapping on customer accounts, as a commenter on Paperclip-style tickets, and as an agent name in support conversations. A PR fix on the codebase references the ticket that drove it; the ticket references the customer who reported it; the customer references the user who filed the original support thread.

This is what makes Pylon useful as a benchmark: AI agents reasoning across multiple files find consistent facts.

## What this unlocks

Pylon at v0.1.0 is enough to test:
- Ticket triage agents (read incoming bugs, classify by component, suggest assignees)
- Release-notes generators (read closed issues since last tag → produce notes)
- PR-review automation (the Pylon repo *is itself* a PR-review-automation tool)
- Customer-support summarizers
- Sprint-planning assistants
- Hotspot-analysis agents
- Compliance-evidence assemblers

## Spec-driven slash commands

The `/ideas` repo's spec-driven design tooling ships in `.claude/commands/context-os/` and `.claude/agents/context-os/`. If you're using Claude Code, those commands are immediately available for shaping new fixture additions.

## Versioning

Pylon uses semantic versioning. v0.1.0 is the Tier 0 substrate. Tier 1 (live marketing site, CRM data, BI warehouse, second codebase, KB expansion to ~30 articles) ships incrementally — each addition will land as its own minor release.

## License

Apache 2.0. Use Pylon for AI tooling research, agent benchmarks, demo environments, internal training data, or anything else where a coherent fake company is more useful than a stub.

## Thanks

Pylon is built by [Bent Wire Studio](https://github.com/kadeclawborn-code/bentwire) — a small studio shipping open-source AI prototypes. If Pylon is useful to your work, [Bent Wire's Medium](https://medium.com/@kade-clawborn) is where the longer-form thinking lives. PRs welcome on this repo if you find a fixture that doesn't hold up under your testbed.

— Bent Wire Studio, 2026-04-25
