# Authoring custom Beacon rules

Custom rules are written in **PRL** (Pylon Rule Language) — a declarative DSL built on top of tree-sitter queries. PRL is designed for engineers who want to write a rule, test it against historical PRs, and ship it without learning a new programming model.

This article walks through writing your first custom rule end-to-end.

## When to write a custom rule

Write a custom rule when you'd otherwise write a code-review checklist item. Examples of good custom-rule territory:

- "Don't call `unsafe_subprocess()` — use `safe_subprocess()` unless you have a specific reason"
- "Database migrations must include a rollback step"
- "All external HTTP calls must include a timeout"
- "Logger calls in our `billing/` module must include a `customer_id` tag"

Bad custom-rule territory (don't write rules for these):

- Things humans should obviously catch ("don't merge with TODO comments") — Pylon's defaults already cover most
- Style preferences without correctness implications — your formatter handles those
- Rules that depend on understanding the *intent* of the code — Beacon is syntax-aware, not semantics-aware

## Anatomy of a rule

Every rule has:

1. **An ID** — `<your-org>.<rule-name>` in kebab-case
2. **A message** — what the in-line PR comment will say
3. **A severity** — `info | low | medium | high | blocking`
4. **A match pattern** — a tree-sitter query that finds the syntax you want to flag
5. **Optionally**: path scoping, suppression rules, per-rule config

## Example: flag uses of `unsafe_subprocess()`

```yaml
custom_rules:
  - id: stratosphere.unsafe-subprocess
    message: |
      `unsafe_subprocess()` is allowed but discouraged. Prefer `safe_subprocess()`
      unless you have a specific reason (escape-quoting, shell expansion, etc.).
      If you need to use this function, leave a `# pylon: suppress(...)` annotation
      with the reason.
    severity: medium
    paths:
      exclude:
        - "tests/**"
        - "**/conftest.py"
    match:
      language: python
      query: |
        (call function: (identifier) @name (#eq? @name "unsafe_subprocess"))
```

## PRL query syntax

PRL queries are standard tree-sitter queries with a few Pylon-specific extensions:

```
(node_type @capture)        Match a node, capture it as @capture
(node_type field: child)    Match by field name
(#eq? @x "value")           Predicate: capture must equal "value"
(#match? @x "regex")        Predicate: capture must match regex
(#scope? @x "function")     Pylon extension: capture must be in this scope
```

For tree-sitter query syntax in detail, see the [tree-sitter docs](https://tree-sitter.github.io/tree-sitter/using-parsers#pattern-matching-with-queries).

For Pylon's extensions to the query language, see [PRL extension reference](https://pylon.dev/docs/prl-extensions).

## Iterating on a rule (preview mode)

Don't ship a rule cold. Pylon's dashboard has a **preview mode** for rule authoring:

1. Open the rule editor at `app.pylon.dev/rules/author`
2. Write your rule
3. Click "Preview against last 200 PRs" — Pylon runs the rule against historical PRs from your repo
4. Examine the findings; tune; repeat

Preview mode catches false positives before they go live.

## Shadow mode

Once preview looks good, drop the rule into **shadow mode** for a week:

```yaml
custom_rules:
  - id: stratosphere.unsafe-subprocess
    mode: shadow
    shadow_period_days: 7
    ...
```

Shadow rules fire but don't post comments. Findings appear in Tower so you can examine them. After the shadow period, promote to default-on by removing the `mode: shadow` line.

## Publishing to the Marketplace

If your rule is generally useful, you can publish it to the public Beacon Rule Marketplace. See [Marketplace guide](./07-marketplace-guide.md).

## Style guide

A few conventions that produce better rules:

- **Be specific in your message.** "Bad function call" is useless. "Use `safe_subprocess()` unless you need shell expansion" is useful.
- **Suggest the fix.** If there's a clear correct alternative, name it in the message.
- **Don't write rules for things you can't suppress.** Every rule needs an out — either path-based exclusion or a `# pylon: suppress(<rule-id>)` annotation.
- **Calibrate severity to consequences.** A rule whose violation is "this is mildly clunky" is `low`. A rule whose violation is "this might leak customer data" is `high` or `blocking`.

## Getting help

- Beacon docs: pylon.dev/docs/rules
- PRL extension reference: pylon.dev/docs/prl-extensions
- Stuck on a query? Email beacon@pylon.dev with your repo language and what you're trying to flag. Wei's team triages within a business day.
