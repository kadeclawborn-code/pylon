# Tower dashboard reference

Tower is Pylon's analytics surface — review-quality metrics, cycle-time charts, hotspot maps, who-reviews-what graphs. This guide is what each dashboard means and how to use it.

## Audience

Tower is built for engineering managers and directors. Engineers benefit from Tower indirectly (their work shows up here) but don't typically use it day-to-day.

## Where to find Tower

`app.pylon.dev/tower` once Pylon is installed. Available on all paid tiers; the Free tier shows a limited cycle-time chart only.

## Dashboards

### Overview

Top-level snapshot per repo or per team:

- Cycle time (median, p90)
- PR throughput (PRs merged per week)
- Pylon finding density (findings per 100 lines changed)
- Review depth distribution (rubber-stamp / light / thorough)

The overview is the right starting point for a weekly review-quality sync. Don't over-interpret single weeks; the noise is high. Trust the trend over 4+ weeks.

### Cycle time

Median time from PR open → merged. Broken into:

- **Time to first review** — from open to first non-author comment
- **Time in review** — from first review to last review
- **Time to merge** — from final approval to merge

Common patterns:

- **Long time to first review** — reviewer assignment is slow or your PRs are too big
- **Long time in review** — reviewers are blocked waiting for changes from authors
- **Long time to merge** — PRs are sitting after approval; usually CI flakiness or conflicting branch policies

### Review depth distribution

Pylon classifies each PR's review into:

- **Rubber-stamp** — approved with no in-line comments and < 60 seconds spent on the diff (heuristic)
- **Light review** — 1-2 in-line comments, or > 60 seconds on the diff with no comments
- **Thorough review** — 3+ in-line comments

The classification is a heuristic, not ground truth. It works well in aggregate; don't use it to score individuals.

### Hotspot map

Files where:
- Pylon comments cluster (many findings over time)
- AND post-merge bugs traced back to (where customer reports + reverts originate)

Hotspot files are real. Refactor candidates. Often these are files no one wants to touch — which is exactly why they accumulate noise.

### "Who reviews what" graph

Visualizes which engineers review work in which areas of the codebase. Useful for:
- Spotting bus factor (one person reviewing 80% of one component)
- Seeing review-load distribution
- Onboarding new reviewers (who should they shadow?)

## Team comparison (PYL-102 — shipped April 2026)

Side-by-side comparison of 2-4 teams within your org. Same metrics as the Overview, rendered in parallel. Useful for:
- "Are platform teams getting more review than feature teams?"
- "Is one team's review depth consistently shallow?"
- Comparing your own team to a higher-performing one

## Data export (PYL-213 + Tower API)

For Business and Enterprise customers, Tower data is available via REST API for export to your warehouse (Snowflake, BigQuery, Redshift). See pylon.dev/docs/tower-api for endpoint details.

Common export use cases:
- Cross-tool dashboards (combine Pylon's review data with deployment frequency from your CI)
- Custom KPI tracking
- Leadership reporting

## Metric definitions

Tower's metric definitions are public and stable. Full glossary at pylon.dev/docs/tower-glossary. Highlights:

- **Cycle time** — median time from PR open to merged
- **Review depth** — classification of how thoroughly each PR was reviewed (heuristic)
- **Finding density** — Pylon findings per 100 lines changed
- **Suppression rate** — fraction of findings dismissed or suppressed
- **Hotspot density** — concentration of findings + post-merge bugs in a file

## When Tower is wrong

Tower aggregates data from your repo activity. If something looks wrong:

1. Verify the repo is connected — sometimes a repo is off the integration
2. Verify the time window — defaults are 90 days; older data may not be backfilled
3. Verify your view permissions — you may be filtered to a subset of teams

If Tower's numbers genuinely seem off, file a support ticket. The most common real cause is a one-off ingest gap (we replay automatically, but rare cases slip through).

## What Tower won't do

- **Score individual engineers.** Pylon does not offer per-engineer rankings. We won't ship that feature; the misuse risk is too high.
- **Generate "code quality scores."** Pylon doesn't generate code-quality scores at the repo or team level. The framing is misleading; we won't ship it. (Master PRD non-goal.)
- **Predict future performance.** Tower shows what happened. It does not project.
