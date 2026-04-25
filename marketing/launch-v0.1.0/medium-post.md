# Building Pylon — a synthetic B2B SaaS company for AI agent benchmarks

If you've built an AI agent that's supposed to operate inside an enterprise — code review, ticket triage, support automation, sales coaching, compliance evidence assembly — you've already had this conversation with yourself: *what data do I test it against?*

The honest answers tend to be:

1. **A handful of stub fixtures you wrote in an afternoon.** Three mock JIRA tickets. A toy repo with two PRs. One sample customer chat. The agent reasons across these and the demo "works."
2. **Real customer data you shouldn't have.** Often pulled from a friendly customer with a wink and a PII-strip pass that doesn't really hold up to scrutiny.
3. **Public datasets shoehorned into the role.** A scrape of the Linux kernel mailing list standing in for "customer support tickets." A GitHub issues dump pretending to be a product roadmap.

None of these is great. The first one fails the moment your agent has to reason across systems — there's no consistent truth between the three mock tickets and the toy repo because they were never connected. The second one fails the legal review. The third one fails the plausibility test the moment your demo audience asks one question.

This is the gap we set out to fill with Pylon.

## What Pylon is

Pylon is a synthetic, open-source B2B SaaS company. It exists as files, fixtures, runnable services, and (eventually) a small set of autonomous agents that simulate ongoing internal activity.

The fictional company "Pylon, LLC" sells a PR review automation product called Pylon. Series B, $35M raised, 71 employees, ~250 paying customers across the engineering teams of mid-market software companies. None of that is real. All of it is plausible enough that an LLM reasons about it as a coherent enterprise.

The repo at `github.com/kadeclawborn-code/pylon` contains:

- The company's full identity, brand voice, organizational chart, and named persona directory
- A master PRD, four-quarter roadmap, pricing page, and competitive analysis
- 45 JIRA-shaped tickets across 14 sprints, complete with cross-references and realistic timelines
- A runnable FastAPI codebase representing the product runtime, including 5 working static-analysis rule implementations, tests, CI workflows, and a synthetic 6-month commit history
- 50 GitHub-style issues and 31 pull requests with realistic review threads
- 7 paying customer accounts, 30 user personas at those accounts, 15 multi-turn support conversations, and 10 customer-facing help articles

Every artifact cross-references every other artifact. A bug filed by a real-feeling customer in a support thread traces to the ticket that documented it, to the PR that fixed it, to the engineer who wrote the fix, to the org chart entry for that engineer, to the company's identity page that explains why this particular bug class was load-bearing.

That coherence is the whole point.

## Why coherence matters

The hardest thing about enterprise AI agents is that real enterprise reasoning is multi-system. An agent classifying a bug needs to understand which component owns it, who's worked on that component recently, what the team's current priorities are, whether there's a related customer thread, and whether a similar bug has fired before. A demo against three disconnected mock tickets cannot teach an agent any of that.

We built Pylon so that an agent has the texture of a real company to reason across. When it asks "who would I assign this ticket to?", the answer requires reading the org chart and the ticket history together. When it drafts release notes, the answer requires reading the PR titles and the changelog and the version history together.

We are not the first to think of synthetic enterprise data. Northwind has been a benchmark for two decades. Acme is a meme. The gap we saw is that nothing modern, AI-agent-aware, and coherent at this depth exists in the open. Pylon's bet is that closing that gap unlocks better agent evaluation across the field.

## What we learned building it

Three things stood out.

**Volume is overrated. Coherence is everything.** We initially planned 100+ tickets, hundreds of users, dozens of help articles. We ended up shipping fewer of each — 45 tickets, 30 users, 10 articles — and spent the saved time making them all reference each other consistently. An AI agent reasoning across 45 well-crafted, cross-referenced tickets gets a richer signal than across 1,000 disconnected ones.

**LLMs detect templates instantly.** Our first draft of the support conversations sounded synthetic — every conversation opened with "Hi, I'm having an issue..." and closed with "Thanks for the help!". We rewrote with explicit attention to messiness: incomplete information, multi-day gaps, mid-conversation tone shifts, mid-thread escalations to engineering. The result reads like real support data because it has the texture of real support data.

**Banned-phrase lists work.** Pylon's `BRAND.md` explicitly bans 14 phrases including "game-changer," "unlock," "leverage," and "we're excited to announce." It bans exclamation points. We applied this discipline across every artifact in the repo. The result is a fictional company that sounds like a fictional engineering company — terse, technical, slightly dry — rather than a fictional company written by a marketing department.

## What's next

Pylon at v0.1.0 is the Tier 0 substrate — enough to test most enterprise AI agents you'd realistically build. Tier 1 adds a live marketing site, CRM-shaped sales data, a BI warehouse, a second codebase (probably the dashboard frontend), and an expanded knowledge base. Tier 2 adds autonomous agents that produce ongoing fictional activity inside Pylon — making it a moving target rather than a static snapshot.

We'll ship Tier 1 incrementally. Each piece will land as its own minor release with its own changelog entry.

If Pylon is useful to your team's AI tooling, fork it and customize. If you find a fixture that doesn't hold up under your testbed, please file an issue. We'd rather know early.

## Get it

[github.com/kadeclawborn-code/pylon](https://github.com/kadeclawborn-code/pylon)

— Bent Wire Studio
