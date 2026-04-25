# Getting started — first 15 minutes

Pylon is a PR review automation tool. You connect it to your repos, it runs the Beacon analyzer on every PR, and surfaces findings as in-line comments.

This guide walks you from "no Pylon yet" to "first PR comment on a real PR" in 15 minutes.

## Before you start

- Admin access to your engineering organization on GitHub, GitLab Cloud, or Bitbucket Cloud
- A repository with at least one open PR (for the immediate first-comment confirmation)

## Step 1 — Sign up (1 minute)

Go to [pylon.dev/signup](https://pylon.dev/signup). Sign in with GitHub OAuth. Free tier covers up to 5 active developers and public repos; paid plans add private repos, custom rules, and more (see [Billing & pricing FAQ](./09-billing-pricing-faq.md)).

## Step 2 — Install the integration (3 minutes)

After signup you're prompted to install the integration matching your platform.

- **GitHub** — installs the Pylon GitHub App. Grant repo access for the repos you want analyzed.
- **GitLab** — OAuth flow with GitLab Cloud. Authorize Pylon's scope.
- **Bitbucket** — Bitbucket Cloud connect flow. Authorize.

For platform-specific setup details, see [Installing Pylon](./02-installing-pylon.md).

## Step 3 — Initial scan (3 minutes, mostly automated)

Pylon ingests the last 30 days of PR history per repo and runs Beacon's default ruleset against the most recent 50 PRs to surface "what we'd have caught" examples. You don't have to do anything; the dashboard shows progress.

When the scan completes you'll see a "starter findings" view. This is mostly retrospective — confirm Pylon is detecting things that would be useful, then move on.

## Step 4 — `pylon.yaml` opens as a PR (4 minutes)

Pylon installs a starter `pylon.yaml` in each repo via PR. The PR title is "Add Pylon configuration." Review the PR like any other:

- The `pylon.yaml` enables the default Beacon rules for the languages Pylon detected in the repo
- Tune any rules you want disabled
- Merge the PR

Once merged, the next PR opened in that repo gets Pylon comments.

## Step 5 — Confirm on a real PR (4 minutes)

Open a small PR in any analyzed repo. Wait ~60 seconds (longer for very large diffs). Pylon's findings appear as in-line comments and a summary comment at the top of the PR.

If nothing appears within 5 minutes, see [Troubleshooting: Pylon isn't commenting](./10-troubleshooting-pylon-not-commenting.md).

## What's next

- Customize rules — see [`pylon.yaml` reference](./03-pylon-yaml-reference.md)
- Author your own rules — see [Authoring custom Beacon rules](./04-authoring-custom-rules.md)
- Check Tower — eng managers find the most value in the Tower dashboards. See [Tower dashboard reference](./06-tower-dashboard-reference.md)

## Time-to-first-comment target

Pylon's internal target is 15 minutes from signup to first comment. If your end-to-end took materially longer, please tell us — bridget@pylon.dev — that's a roadmap-worthy data point.
