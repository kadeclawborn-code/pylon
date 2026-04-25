# Troubleshooting: Pylon isn't commenting

If Pylon stops posting comments on your PRs, run through this checklist before opening a support ticket.

## Quick diagnostic

In your Pylon dashboard, the **Health** widget shows the most recent webhook event from each connected repo. If the timestamp on a repo is more than 30 minutes old AND you've had PR activity since, that's the symptom.

## Step 1 — Check the integration is still installed

Sometimes a repo's integration gets accidentally removed (admin reorganization, old App tokens, etc.).

**GitHub:**
- Visit your GitHub org's Settings → GitHub Apps → Pylon
- Confirm Pylon has access to the repo with the missing comments
- Confirm permissions include: read repo + read pull requests + write PR comments + write checks

**GitLab:**
- Visit your GitLab project's Settings → Integrations → Pylon
- Confirm Pylon is listed and enabled

**Bitbucket:**
- Visit your workspace's Settings → Connected apps → Pylon
- Confirm authorized

If the integration is missing or has reduced permissions: re-install via the Pylon dashboard. See [Installing Pylon](./02-installing-pylon.md).

## Step 2 — Check that webhooks are firing

In your platform's webhook delivery log:

**GitHub:** Settings → GitHub Apps → Pylon → Advanced → Recent Deliveries
Look for `pull_request` events. If they're being delivered to Pylon's webhook URL successfully (200 response), the platform side is fine.

**GitLab:** Project → Settings → Webhooks → Pylon webhook → Recent deliveries
Same check.

**Bitbucket:** Workspace → Connected apps → Pylon → Activity log

If the platform shows webhooks being delivered but Pylon's dashboard shows them not received, that's a real bug — file a support ticket with the timestamp of a delivered-but-not-received webhook.

If the platform shows webhooks being delivered with a non-200 response: that's a Pylon-side issue. File a support ticket with the timestamp + status code.

## Step 3 — Check PR characteristics

Pylon won't comment on:

- **Drafts** — by default. (Configurable in `pylon.yaml`.)
- **PRs from forks** — without explicit installation on the fork. (Common gotcha for OSS workflows.)
- **PRs where Pylon's `pylon.yaml` is missing or invalid** — Pylon posts a "config error" comment instead and skips analysis.
- **PRs where every file is in an excluded path** — nothing to analyze.
- **PRs with binary changes only** — Pylon needs text diffs.

Open the PR and check:
- Is it a draft?
- Is the author from a fork?
- Does your repo have a valid `pylon.yaml`?
- Does the diff include any files Pylon would scan?

## Step 4 — Check the Pylon dashboard's run log

`app.pylon.dev/runs` shows the last 100 analyzer runs across your repos. Find your PR in the list:

- **"queued"** for >10 minutes — there's a backlog. Check status.pylon.dev for service status.
- **"running"** for >10 minutes — the analyzer is stuck. File a support ticket with the run ID.
- **"failed"** — click in for the error message. Common causes: rule compilation error, malformed `pylon.yaml`, transient network issue.
- **"completed"** but no PR comment — the run completed but the comment poster failed. File a support ticket; this is rare and we want to know.

## Step 5 — Check Pylon's status page

`status.pylon.dev`. If we're having a regional or service-level incident, it's posted there with ETA. Pylon doesn't email customers about incidents (only about planned maintenance), so the status page is the source of truth for "is Pylon down."

## Step 6 — Check API rate limits

Pylon respects GitHub's per-installation rate limit (5,000 requests/hour). If your org has a high PR volume during a burst (CI-driven PR auto-creation, mass dependency updates, etc.), Pylon may be temporarily backing off.

This auto-recovers once the rate budget refreshes. If your org consistently hits this ceiling, talk to support — Enterprise tier has options for elevated rate limits.

## Step 7 — Recently rotated tokens?

If your team rotated GitHub App credentials, GitLab OAuth tokens, or similar in the past 24 hours, the rotation may have broken Pylon's webhook authentication. Reconnect the integration from the dashboard.

## Step 8 — Recently shipped a CI workflow change?

If you added a new CI status check or branch protection rule that conflicts with Pylon, Pylon may be running but blocked from posting. Check your branch protection rules and confirm Pylon's status check name is allowed (see [Configuring pylon.yaml](./03-pylon-yaml-reference.md) for renaming Pylon's status check).

## Still stuck?

Email `bridget@pylon.dev` with:
- Your Pylon org name
- The PR URL
- Approximate timestamp the issue started
- What you've already tried from this checklist

We respond within 4 business hours on Business and Enterprise tiers; within 1 business day on Team.

## Pre-emptive: subscribing to status updates

`status.pylon.dev` supports email + RSS subscriptions. If you want to know proactively when there's a Pylon-side incident, subscribe.

## What we won't do

We don't auto-replay missed webhooks. Pylon is forward-looking; if events are missed during an incident, we don't backfill comments after recovery (that would generate confusing comments long after the PR was reviewed). We do retain webhook *records* for 30 days for postmortem purposes.
