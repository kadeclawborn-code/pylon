# `pylon.yaml` reference

The `pylon.yaml` file at your repo root configures which Beacon rules run, scopes them to specific paths, and lets you author custom rules. Pylon installs a starter `pylon.yaml` on first integration; you tune it from there.

## Minimal example

```yaml
version: 1
rules:
  python.bare-except:
    enabled: true
  python.print-in-prod:
    enabled: true
  python.todo-without-author:
    enabled: true
```

## Full schema

```yaml
version: 1                    # required, always 1 in current Pylon

# Optional global settings
defaults:
  severity_floor: low         # Suppress findings below this severity
  paths:
    exclude:                  # Globs, applied to all rules unless overridden
      - "**/migrations/**"
      - "**/vendor/**"

rules:
  <rule-id>:                  # e.g. python.bare-except
    enabled: true | false
    severity: info | low | medium | high | blocking
    paths:
      include:                # Globs; if absent, rule applies to everything
        - "src/**/*.py"
      exclude:                # Globs; rule skips these
        - "tests/**"
    config:                   # Rule-specific options (varies per rule)
      ...

custom_rules:
  - id: <your-org>.<rule-name>
    message: "..."
    severity: medium
    paths:
      exclude: [...]
    match:
      language: python
      query: |
        ...                   # tree-sitter query in PRL syntax

# Optional: subscribe to Marketplace rules
marketplace_subscriptions:
  - rule_id: published-org.rule-name
    version: latest | x.y.z
    mode: on | off | shadow
```

## Rule IDs and naming

Rule IDs follow `<language>.<rule-name>` for default Pylon rules and `<org-slug>.<rule-name>` for custom rules. Examples:

- `python.bare-except`
- `python.print-in-prod`
- `typescript.no-floating-promises`
- `acme.unsafe-subprocess` (custom rule from the org "acme")

## Severity levels

| Severity | Meaning |
|---|---|
| `info` | FYI; would be a soft comment on a manual review |
| `low` | Style or paper-cut; safe to ignore for trivial PRs |
| `medium` | Should be addressed; might block merge in some teams |
| `high` | Almost always a real issue |
| `blocking` | Pylon should block merge until addressed (requires `merge_block: true` at org level) |

Customers can override the severity for any rule. Be careful not to flatten everything to `low` — that's how you teach reviewers to ignore Pylon.

## Path scoping

Both `include` and `exclude` accept globs. If both are specified, both apply (the file must match `include` and not match `exclude`).

Common patterns:

```yaml
# Skip tests
exclude:
  - "tests/**"
  - "**/test_*.py"
  - "**/*_test.py"
  - "**/conftest.py"

# Skip generated code
exclude:
  - "**/generated/**"
  - "**/*.pb.go"
  - "**/*.gen.ts"

# Apply only to a specific service
include:
  - "services/billing/**"
```

## Per-rule config

Some rules accept rule-specific config. The config schema is documented on each rule's docs page (e.g., `pylon.dev/docs/rules/python.bare-except`). Example:

```yaml
rules:
  python.todo-without-author:
    config:
      accepted_authors:       # Treat tags from these usernames as valid
        - "@hugo"
        - "@wei"
      require_ticket_id: false  # Don't enforce PYL-XXX in TODOs
```

## Validation

Pylon validates `pylon.yaml` on every push. If your config is malformed, Pylon posts a single "config error" comment on the PR with the validation message. The PR is not blocked over a bad config — it's a warning, not a gate.

## Where the file lives

`pylon.yaml` at your repo root. We don't search subdirectories. If you have a monorepo with multiple sub-services that need different configs, see the monorepo guide at pylon.dev/docs/monorepos.
