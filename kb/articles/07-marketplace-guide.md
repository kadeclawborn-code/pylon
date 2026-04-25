# Beacon Rule Marketplace guide

The Beacon Rule Marketplace lets one team publish a custom rule and any other Pylon customer subscribe to it. Public preview launched March 2026.

## Who can use it

- **Browse + subscribe**: Free, Team, Business, Enterprise tiers
- **Publish**: Business, Enterprise tiers (you must be on a tier that allows custom rules to publish them)

## Browsing

Go to `app.pylon.dev/marketplace`. The browse page shows all published rules with:

- Name + description
- Publishing org
- Language(s) it covers
- Subscriber count
- Aggregate fire rate (privacy-preserved across all subscribers)
- Latest version + release date

Filter by language, category, publisher, license. Sort by subscriber count, fire rate (lower = stronger signal), or newest.

Click a rule to see the detail page: full description, examples, fire-rate trend over time, subscriber-org-count history, license, version changelog.

## Subscribing

On the rule detail page, click **Subscribe**. A modal asks how you want to integrate the rule:

- **On (default)** — rule is enabled immediately, posts findings on your PRs
- **Off** — rule is added to your config but disabled. Useful if you want to read the rule's docs before adopting.
- **Shadow mode** — rule fires but findings don't post. Visible in Tower for the shadow period (default 14 days). Promote to on after.

When you subscribe, Pylon opens a PR in your repo to add the rule to your `pylon.yaml`. Review and merge it like any config change.

## Versioning behavior

Marketplace rules use semantic versioning. By default:

- **Patch updates** (1.0.0 → 1.0.1) auto-apply to subscribers
- **Minor updates** (1.0.0 → 1.1.0) auto-apply to subscribers
- **Major updates** (1.0.0 → 2.0.0) require manual confirmation

You can pin to a specific version if you want to avoid auto-updates entirely:

```yaml
marketplace_subscriptions:
  - rule_id: northwall.unsafe-currency-conversion
    version: 1.0.0   # pin to this version, no updates
    mode: on
```

## Unsubscribing

From the rule detail page (or your dashboard's Subscriptions view), click **Unsubscribe**. The rule is removed from your `pylon.yaml` via PR.

## Publishing

If your team is on Business or Enterprise tier, you can publish your custom rules to the public Marketplace.

Steps:

1. Open the rule editor at `app.pylon.dev/marketplace/publish`
2. Fill out the publishing form:
   - Rule (selector — picks from your org's existing custom rules)
   - Public name (must be unique across the marketplace)
   - Description (≥50 characters; the description is what subscribers read first)
   - License (default: Apache 2.0)
   - Initial version (default: 1.0.0)
3. Preview screen shows what subscribers will see
4. Click **Publish**

Within minutes the rule is live in the public Marketplace, browsable by any Pylon customer.

### What gets shared

When you publish, the following is public:
- Rule name and description
- Match pattern (the PRL query)
- Aggregate fire rate across all subscribers
- License, version, publishing org

Not public:
- Per-customer fire rate or dismissal data
- Anything from your `pylon.yaml` other than the published rule itself
- Your customer-specific path scoping (subscribers configure their own)

## Anonymous publishing

If your org prefers not to be publicly attributed, you can publish without an org tag. Trade-offs:
- Subscribers can't reach out with questions
- The rule has slightly less weight in marketplace ranking signals (we treat attribution as quality signal)

To publish anonymously, check the "Publish without org attribution" box on the publish form.

## Updating a published rule

From your published rule's detail page, click **New version**. You can change:
- The match pattern
- The message
- The severity recommendation

Bump the version per semver:
- Bug fix in the rule (no behavior change for subscribers): patch
- New behavior, additive: minor
- Breaking change to the rule (different matching, different scope): major

Subscribers get notifications based on their auto-update settings.

## Unpublishing

From your rule's detail page, click **Unpublish**. Existing subscribers keep the version they have; new subscribers can't sign up. We do not force-revoke from existing subscribers — that would break their builds. This is a deliberate trade-off.

## Quality and curation

Public preview is uncurated; anyone on the right tier can publish anything. We track:
- Aggregate fire rate (rules with very high fire rate get a yellow flag, drawing subscribers' attention)
- Aggregate dismissal rate (rules with high dismissal rate get a red flag)

If a rule has consistently bad signal, we may reach out to the publisher. We do not (currently) remove rules from the marketplace unilaterally, except for clear policy violations (malicious rules, etc.).

## Trust and safety

Rules in the marketplace cannot:
- Execute arbitrary code (PRL is declarative; tree-sitter queries can't execute)
- Read repo contents beyond the diff being analyzed
- Network out
- Modify your codebase

A subscribed rule running on your code is no more privileged than a default Pylon rule. The marketplace is a content layer, not a code-execution layer.

## Future direction

Q3+ roadmap items related to Marketplace:
- Rule packs (groups of related rules with shared config)
- Curated collections (Pylon-vetted rule sets for specific use cases)
- Possibly: monetization for publishers (no commitment yet)
