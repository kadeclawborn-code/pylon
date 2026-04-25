# Installing Pylon

Pylon supports three host platforms: **GitHub Cloud**, **GitLab Cloud**, and **Bitbucket Cloud**. Self-hosted variants are not supported except via Enterprise tier on-prem (talk to sales).

## GitHub Cloud

1. From the Pylon dashboard, click **Add repos** in the integrations panel.
2. You'll be redirected to GitHub's App install page. Choose your organization.
3. Grant access to specific repos or "all repos." We recommend starting with 2-3 repos and expanding once you've confirmed the integration.
4. Approve the permissions. Pylon needs:
   - **Read** access to: code, metadata, pull requests, issues
   - **Write** access to: pull request comments (so we can post findings), checks (so we can mark our own status check)

That's it. Pylon's dashboard now sees the repos.

## GitLab Cloud

1. From the Pylon dashboard, click **Connect GitLab** in the integrations panel.
2. OAuth round-trip with GitLab Cloud. Authorize Pylon's scope:
   - `api` (for MR comment posting and status check)
   - `read_repository` (for diff fetching)
3. Choose which projects to enable. You can enable per-project or per-group.

If your GitLab Cloud org uses 2FA, the OAuth flow handles it normally.

**GitLab self-hosted is not supported as of v2.4.x.** GitLab self-hosted Enterprise is being scoped for late 2026. Sign up at pylon.dev/early-access if interested.

## Bitbucket Cloud

1. From the Pylon dashboard, click **Connect Bitbucket** in the integrations panel.
2. Bitbucket Cloud connect flow. Authorize Pylon as a connected app at the workspace level.
3. Choose which repos to enable.

Pylon's Bitbucket Cloud support is feature-equivalent to the GitHub and GitLab integrations.

**Bitbucket Server (self-hosted) is not supported and is not on the roadmap.** This is a deliberate scope choice; see our [public PRD](https://pylon.dev/docs/master-prd) for the rationale.

## Multiple platforms in one organization

Customers using multiple platforms (e.g., GitHub Cloud for one product line and GitLab Cloud for another) can connect both. Pylon treats them as separate platform integrations on the same Pylon org.

Billing remains per-developer — a developer who's active on PRs across both platforms counts once.

## What if installation fails?

Common issues:

- **"Access denied" on GitHub** — your org admin requires approval for new GitHub Apps. Have an admin approve Pylon under Org Settings → Third-party access.
- **GitLab OAuth redirects in a loop** — clear cookies for `gitlab.com` and try again. Almost always a stale session token.
- **Bitbucket connect shows "scopes mismatch"** — the customer's workspace has a stricter app-permission policy than Pylon requires. Contact bitbucket workspace admin.

If installation fails for a reason not on this list, email bridget@pylon.dev with the error message and your org name.
