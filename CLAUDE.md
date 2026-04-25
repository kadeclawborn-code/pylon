# CLAUDE.md — Pylon Repo

You are working inside [`kade-clawborn/pylon`](https://github.com/kade-clawborn/pylon) — a synthetic B2B SaaS company being built as an open-source AI agent testbed by [Bent Wire Studio](https://github.com/kade-clawborn/bentwire).

## On entry, always

1. Read `BLUEPRINT.md` end to end if you haven't this session. It's the canonical design doc.
2. Confirm which Tier 0 POC you're on (1–5 — see BLUEPRINT.md "Tier 0 POC breakdown"). Your Paperclip task description should name it.
3. Branch off `main` as `poc/<slug>` matching the POC name.

## Spec-driven slash commands available

The [Bent Wire `/ideas`](https://github.com/kade-clawborn/ideas) repo's spec-driven design commands have been copied to `.claude/commands/context-os/`:

- `/shape-spec` — Q&A loop to refine a Pylon-fixture spec into `REQUIREMENTS.md`
- `/write-spec` — Generate full `spec.md` from REQUIREMENTS.md
- `/create-tasks` — Break a spec into `tasks.md`
- `/implement-tasks` — Execute the tasks.md
- `/integrate` — Cross-spec integration helper
- `/orchestrate-tasks` — Higher-level task orchestration
- `/plan-product` — Product planning helper

Companion subagents at `.claude/agents/context-os/`:
- `spec-shaper`, `spec-initializer`, `spec-writer`, `spec-verifier`
- `product-planner`, `tasks-list-creator`
- `implementer`, `implementation-verifier`, `integrator`

Use these as you would in `/ideas` — they assume the same SPEC-TEMPLATE.md format. For Pylon work, treat each fixture-bundle (e.g. "POC 3 ticket system") as a spec to shape and write.

## Ground rules for Pylon artifacts

### Realism > volume
A hundred tickets that feel real beats ten thousand templated ones. Vary tone, length, completeness. Real tickets are messy; synthetic tickets shouldn't be too clean.

### No real-entity collisions
Don't reference real companies, people, products, or events. When in doubt, generate a fictional name.

### Voice consistency
Pylon's brand voice (per BLUEPRINT.md): *direct, technical, slightly dry. No exclamation points. Engineering-respectful — never patronizing, never over-marketed.* All Pylon-internal content (blog posts, KB articles, marketing copy, internal Slack) should match.

### Internal cross-references must hold
If you write a Pylon employee named "Marcus Chen" in `org/employees.json`, then a support ticket comment that says "Marcus on the platform team" must refer to that same Marcus. Cross-system coherence is what makes Pylon useful as a benchmark — agents reasoning across multiple files should find consistent facts.

### File format conventions
- Markdown for human-readable docs (PRDs, blog posts, KB articles, postmortems)
- JSON for structured fixtures (tickets, customers, employees, deals, accounts)
- SQL for DB schemas + seed data
- YAML for configs (CI workflows, docker-compose)
- One artifact per file when reasonable; bundle related items in arrays only when they're truly small (employees fit in one JSON; tickets do not — one file per ticket)

### Branch + commit conventions
- `main` — Tier 0/1/2 stable releases tagged here
- `poc/<slug>` — active POC work; ready-to-release PR opens against `main`
- Commit prefixes by layer: `org:`, `product:`, `tickets:`, `codebases:`, `support:`, `kb:`, `marketing:`, `finance:`, `compliance:`, `data:`, `security:`, `meta:` (BLUEPRINT/README/CLAUDE updates)
- Conventional commits inside Pylon's *product* codebase (`codebases/api/`) — that subdir gets its own `.git/` history with `feat:`, `fix:`, etc.

### Privacy posture
This repo is **public from day 1**. Don't put anything here that wouldn't be safe public:
- No real API keys, even truncated
- No real personal data
- No internal Bent Wire deliberations or memory dumps
- Synthetic data only

### What lives where (boundary clarification)

| In this repo | NOT in this repo |
|---|---|
| Pylon's fictional artifacts (org, product, tickets, code, customers, support, marketing, finance) | Bent Wire's agent identity files (those are in `~/.paperclip/...`) |
| Pylon's product code (under `codebases/`) | Bent Wire's POC build process (that's `kade-clawborn/bentwire-playground`) |
| The runnable spin-up (Makefile, docker-compose) | Bent Wire studio charter and operating docs (`kade-clawborn/bentwire`) |
| BLUEPRINT.md, README.md, this file | Anything Bent Wire-internal |

## When in doubt

- Defer to BLUEPRINT.md.
- Comment on your Paperclip task asking for Bent Wire EngineeringLead's clarification rather than guessing.
- Prefer leaving a `TODO:` marker in a fixture over inventing facts that might collide with later POCs.

## What you NEVER do here

- Push to a non-Pylon remote (this repo only goes to `kade-clawborn/pylon`)
- Commit on `main` directly (always work on `poc/<slug>`)
- Generate "Acme Corp"-style fixtures (Pylon is the company, no nested fakes)
- Reference Bent Wire Studio in Pylon's public-facing artifacts (Pylon should appear standalone — Bent Wire is in BLUEPRINT.md and README.md only as the project's origin/maintainer footer)

## License

Apache 2.0. All Pylon synthetic data and code is free to use for AI tooling research and benchmarking.
