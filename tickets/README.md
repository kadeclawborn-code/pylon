# Pylon — Tickets Fixture Set

> Synthetic JIRA-style ticket history for Pylon's engineering team across 14 sprints (Oct 2025 – Apr 2026). The data is here to give AI agents a coherent, multi-month, multi-component ticket world to reason over: triage, retrospectives, sprint planning, release notes, hotspot analysis, assignment suggestions, etc.

## What's here

| File | Contents |
|---|---|
| `sprints.json` | 14 sprints (S1 – S14) with dates, themes, and status |
| `all.json` | All tickets in a single canonical array. **Source of truth.** |

## Schema (per ticket)

```json
{
  "key": "PYL-200",
  "type": "epic | story | bug | task | spike",
  "status": "backlog | todo | in_progress | in_review | blocked | done | cancelled",
  "priority": "low | medium | high | urgent",
  "title": "string, ≤120 chars",
  "component": "Beacon | Tower | Switchyard | Dashboard | Infra | Docs | Marketing | Security",
  "sprint": "S7",                       // null if backlog/unscheduled
  "epic": "PYL-101",                    // parent epic key, null if top-level
  "links": ["PYL-50", "PYL-52"],        // related tickets (any direction)
  "assignee": "emp_011",                // employees.json id
  "reporter": "emp_004",                // employees.json id
  "created": "2026-01-09T14:32:00Z",    // ISO 8601 UTC
  "updated": "2026-01-15T09:11:00Z",
  "story_points": 3,                    // null for epics, bugs, spikes that aren't sized
  "labels": ["beacon", "performance"],  // free-form
  "description": "...",
  "acceptance_criteria": ["...", "..."],// null on bugs/spikes/tasks where N/A
  "comments": [
    { "author": "emp_002", "at": "2025-12-05T08:14:00Z", "body": "..." }
  ]
}
```

### Status semantics

- **backlog** — ranked but not committed to a sprint
- **todo** — committed to current sprint, not yet started
- **in_progress** — actively being worked
- **in_review** — code complete, awaiting review/QA
- **blocked** — waiting on external dependency (other ticket, decision, customer)
- **done** — shipped, closed
- **cancelled** — abandoned (rare)

### Priority semantics

- **urgent** — production incident, customer escalation, security
- **high** — quarter commitment, blocking a release
- **medium** — normal sprint work
- **low** — nice-to-have, paper-cut, refactor

## How tickets reference each other

- **`epic`** points to the parent epic. Stories typically have an epic; bugs sometimes do (when a regression came from epic work); tasks/spikes usually don't.
- **`links`** is a flat list of related ticket keys, no edge-direction implied. Used for "see also," "duplicate of," "blocks," etc. Read context from the comment thread to disambiguate.
- A ticket's `sprint` matches the sprint it was actively worked in (or completed in). Backlog tickets have `sprint: null`.

## Persona references

`assignee` and `reporter` are employee IDs from `org/employees.json`. Comment authors are also employee IDs. Any agent reasoning about who-said-what should resolve the ID first.

## What's NOT modeled here

- **PR / commit links** — those live in the codebase fixtures (POC 4). Some tickets reference them in comments (e.g., "Merged in #84") but the actual PR objects are out of scope for this fixture.
- **Time-tracking** — story points are present; hours-logged is not. Pylon doesn't enforce time tracking.
- **Custom fields** — no team-specific custom fields beyond the schema above. If POCs need them, extend the schema and refactor all tickets.
- **Watchers / subscribers** — agents can infer engagement from comment authorship; no explicit watcher list.

## Conventions in the data

- All `PYL-1XX` keys are **epics**.
- All `PYL-2XX` keys are **stories**.
- All `PYL-3XX` keys are **bugs**.
- All `PYL-4XX` keys are **tasks** (engineering chores).
- All `PYL-5XX` keys are **spikes** (research / investigation).
- Real Pylon would mix all types in a single sequential numbering; we segment here for human readability of the fixture set.
- Dates are realistic relative to sprint windows. No future-dated comments. Tickets in older sprints are mostly done; tickets in S13–S14 mix in_progress and todo.
- Comment authorship reflects real roles: tech leads comment more on architectural calls, designers chime in on UX-touched tickets, support leads add context on bugs that originated from tickets they triaged.

## Stats (current snapshot)

- **Total tickets:** see `all.json` length
- **Sprints covered:** S1 (2025-10-13) → S14 (2026-04-26, current)
- **Most active component:** Beacon (rule engine work)
- **Active epics in S14:** PYL-101 (GitLab GA), PYL-102 (Tower Team Compare), PYL-104 (Async rule pack), PYL-105 (Pylon Suggest)
- **Recently shipped epics:** PYL-100 (Beacon Marketplace, S12), PYL-103 (Audit Logs, S11)

## When you add a ticket

1. Read this README first. Match the schema.
2. Bump the right number range (epic = 1XX, story = 2XX, bug = 3XX, etc.)
3. Reference `org/employees.json` for assignee/reporter/commenter IDs — never invent.
4. Pick a sprint that fits the dates in `sprints.json`.
5. If the ticket belongs to an existing epic, set `epic`. If it spawns a new epic, file the epic ticket first.
6. Don't templatize. Read 5 existing tickets before writing yours; vary structure, length, formality.
