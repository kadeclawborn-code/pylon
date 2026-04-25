Most AI agent demos are tested against three mock tickets and a toy repo.

That's why so many "agentic" projects collapse the moment they hit a real enterprise — there's no cross-system coherence in the test data, so the agent never learns to reason across one.

We've spent the past few weeks building Pylon, an open-source synthetic B2B SaaS company designed specifically as a benchmark substrate for AI agent tooling.

Pylon ships with: a fictional 71-employee company with a full identity, org chart, and brand; a master PRD, roadmap, and pricing page; 45 cross-referenced tickets across 14 sprints; a runnable FastAPI codebase with 5 working static-analysis rules and a 6-month synthetic commit history; 50 issues, 31 PRs with realistic review threads; 7 paying customer accounts; 30 user personas; 15 multi-turn support conversations; and a 10-article knowledge base — all cross-referenced into a single coherent world.

What makes it useful is not the volume. It's the coherence. A bug filed in a support thread traces to the ticket, to the PR, to the engineer, to the org chart, to the customer that reported it. An AI agent reasoning across multiple files finds consistent facts.

If you're testing an AI agent against an enterprise environment — for code review, ticket triage, support summarization, or anything else multi-system — Pylon at v0.1.0 is enough to start.

Apache 2.0. Fork it, customize it, file issues if a fixture doesn't hold up.

github.com/kadeclawborn-code/pylon
